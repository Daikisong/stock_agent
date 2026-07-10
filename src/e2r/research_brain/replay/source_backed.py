"""Live-fetch and freeze URL-backed historical Evidence OS replay leaves."""

from __future__ import annotations

import hashlib
import html
import io
import json
from dataclasses import dataclass
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

import requests
from pypdf import PdfReader

from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    Directness,
    EvidenceAnchor,
    EvidenceDocument,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    RawAssertion,
    RelationToTarget,
    SemanticStatus,
    SourceType,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    derive_score_eligibility,
)
from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text


HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION = (
    "e2r_historical_source_backed_replay_v1"
)
HISTORICAL_SOURCE_REGISTRY_SCHEMA_VERSION = (
    "e2r_historical_source_backed_replay_registry_v1"
)


@dataclass(frozen=True)
class HistoricalHttpResponse:
    url: str
    status_code: int
    content_type: str
    body: bytes
    error: str | None = None


class HistoricalSourceTransport(Protocol):
    def fetch(self, *, url: str, timeout_seconds: int) -> HistoricalHttpResponse:
        ...


class RequestsHistoricalSourceTransport:
    def __init__(self, *, user_agent: str = "E2R-Historical-Replay/1.0") -> None:
        self._user_agent = user_agent

    def fetch(self, *, url: str, timeout_seconds: int) -> HistoricalHttpResponse:
        try:
            response = requests.get(
                url,
                timeout=timeout_seconds,
                headers={"User-Agent": self._user_agent},
            )
            return HistoricalHttpResponse(
                url=str(response.url),
                status_code=int(response.status_code),
                content_type=str(response.headers.get("content-type") or ""),
                body=bytes(response.content),
                error=None,
            )
        except requests.RequestException as exc:
            return HistoricalHttpResponse(
                url=url,
                status_code=0,
                content_type="",
                body=b"",
                error=f"{type(exc).__name__}:{exc}",
            )


@dataclass(frozen=True)
class HistoricalFrozenDocument:
    document: EvidenceDocument
    canonical_url: str
    raw_content_sha256: str
    raw_byte_count: int
    content_type: str
    extracted_text: str
    page_spans: tuple[tuple[int, int], ...]

    def provenance_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION,
            "document_id": self.document.document_id,
            "canonical_url": self.canonical_url,
            "source_type": self.document.source_type.value,
            "source_name": self.document.source_name,
            "raw_content_sha256": self.raw_content_sha256,
            "raw_byte_count": self.raw_byte_count,
            "extracted_text_sha256": self.document.content_hash,
            "extracted_text_char_count": len(self.extracted_text),
            "published_date": _date_string(self.document.published_at),
            "available_date": _date_string(self.document.available_at),
            "fetched_date": _date_string(self.document.fetched_at),
            "source_proxy_only": self.document.source_proxy_only,
            "score_block_reasons": list(self.document.score_block_reasons),
        }


@dataclass(frozen=True)
class HistoricalSourceBackedReplayResult:
    replay_rows: tuple[Mapping[str, Any], ...]
    repair_rows: tuple[Mapping[str, Any], ...]
    documents: tuple[HistoricalFrozenDocument, ...]
    manifest: Mapping[str, Any]

    def __post_init__(self) -> None:
        if self.manifest.get("schema_version") != HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION:
            raise ValueError("historical source-backed replay manifest schema mismatch")
        if self.manifest.get("critical_count_sum") != sum(
            int(value) for value in self.manifest.get("hard_acceptance_counts", {}).values()
        ):
            raise ValueError("historical source-backed replay critical count mismatch")


def compile_historical_source_backed_replay(
    *,
    registry_path: str | Path,
    repo_root: str | Path = ".",
    transport: HistoricalSourceTransport | None = None,
) -> HistoricalSourceBackedReplayResult:
    root = Path(repo_root).resolve()
    registry_file = _resolve_path(root, registry_path)
    registry = json.loads(registry_file.read_text(encoding="utf-8"))
    if registry.get("schema_version") != HISTORICAL_SOURCE_REGISTRY_SCHEMA_VERSION:
        raise ValueError("historical source registry schema mismatch")
    cases = tuple(_mapping_rows(registry.get("cases")))
    if not cases:
        raise ValueError("historical source registry has no cases")
    case_ids = tuple(str(item.get("case_id") or "") for item in cases)
    if len(case_ids) != len(set(case_ids)) or any(not item for item in case_ids):
        raise ValueError("historical source registry case ids must be unique")
    max_attempts = _positive_int(registry.get("max_fetch_attempts_per_case"))
    timeout_seconds = _positive_int(registry.get("request_timeout_seconds"))
    snapshot_date = date.fromisoformat(
        str(registry.get("snapshot_acquired_date") or date.today().isoformat())
    )
    source_transport = transport or RequestsHistoricalSourceTransport()

    response_cache: dict[str, HistoricalHttpResponse] = {}
    document_cache: dict[str, HistoricalFrozenDocument] = {}
    replay_rows: list[Mapping[str, Any]] = []
    curated_repairs: list[Mapping[str, Any]] = []
    for case in cases:
        url = str(case.get("url") or "")
        response = response_cache.get(url)
        if response is None:
            response = _fetch_with_attempts(
                transport=source_transport,
                url=url,
                timeout_seconds=timeout_seconds,
                max_attempts=max_attempts,
            )
            response_cache[url] = response
        try:
            if response.error or response.status_code != 200 or not response.body:
                raise ValueError(
                    response.error
                    or f"HTTP_{response.status_code}:empty={not bool(response.body)}"
                )
            frozen = document_cache.get(url)
            if frozen is None:
                frozen = _freeze_document(
                    case=case,
                    response=response,
                    snapshot_date=snapshot_date,
                )
                document_cache[url] = frozen
            replay_rows.append(_compile_case(case=case, frozen=frozen))
        except (OSError, TypeError, ValueError) as exc:
            curated_repairs.append(
                _repair_row(
                    case_id=str(case.get("case_id") or ""),
                    archetype_id=str(case.get("archetype_id") or ""),
                    source_url=url,
                    blocker_code="SOURCE_FETCH_OR_ANCHOR_VERIFICATION_FAILED",
                    blocker_detail=f"{type(exc).__name__}:{exc}",
                    source_proxy_only=False,
                    evidence_url_pending=False,
                )
            )

    inventory_path = _resolve_path(root, str(registry.get("inventory_path") or ""))
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    inventory_repairs = _inventory_source_repairs(inventory)
    repair_rows = tuple(
        sorted(
            (*inventory_repairs, *curated_repairs),
            key=lambda item: (str(item["archetype_id"]), str(item["case_id"])),
        )
    )
    replay_tuple = tuple(sorted(replay_rows, key=lambda item: str(item["case_id"])))
    documents = tuple(
        sorted(document_cache.values(), key=lambda item: item.document.document_id)
    )
    hard_counts = _hard_acceptance_counts(
        replay_rows=replay_tuple,
        repair_rows=repair_rows,
        canary_archetype_ids=tuple(
            str(item) for item in registry.get("canary_archetype_ids") or ()
        ),
        inventory=inventory,
    )
    critical_sum = sum(hard_counts.values())
    manifest = {
        "schema_version": HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION,
        "status": (
            "HISTORICAL_SOURCE_BACKED_REPLAY_PASS"
            if critical_sum == 0
            else "HISTORICAL_SOURCE_BACKED_REPLAY_FAIL"
        ),
        "registry_id": registry.get("registry_id"),
        "snapshot_acquired_date": snapshot_date.isoformat(),
        "curated_case_count": len(cases),
        "replay_ready_count": len(replay_tuple),
        "positive_replay_ready_count": sum(
            item.get("source_role") == "POSITIVE" for item in replay_tuple
        ),
        "guard_replay_ready_count": sum(
            item.get("source_role") == "GUARD" for item in replay_tuple
        ),
        "wrong_subject_probe_count": sum(
            item.get("source_role") == "WRONG_SUBJECT" for item in replay_tuple
        ),
        "fetched_unique_document_count": len(documents),
        "actual_full_source_fetch_count": len(response_cache),
        "registry_source_repair_count": len(inventory_repairs),
        "curated_source_repair_count": len(curated_repairs),
        "source_corpus_hash": stable_hash(
            [item.provenance_dict() for item in documents]
        ),
        "replay_leaf_hash": stable_hash(replay_tuple),
        "repair_queue_hash": stable_hash(repair_rows),
        "hard_acceptance_counts": hard_counts,
        "critical_count_sum": critical_sum,
        "production_runtime_ready": False,
    }
    return HistoricalSourceBackedReplayResult(
        replay_rows=replay_tuple,
        repair_rows=repair_rows,
        documents=documents,
        manifest=manifest,
    )


def write_historical_source_backed_replay(
    result: HistoricalSourceBackedReplayResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    frozen_root = root / "frozen_documents"
    provenance_rows: list[Mapping[str, Any]] = []
    for item in result.documents:
        frozen_path = frozen_root / f"{item.document.document_id}.txt"
        write_text(frozen_path, item.extracted_text + "\n")
        provenance_rows.append(
            {
                **item.provenance_dict(),
                "frozen_text_path": str(
                    Path("frozen_documents") / frozen_path.name
                ),
                "frozen_text_file_sha256": hashlib.sha256(
                    frozen_path.read_bytes()
                ).hexdigest(),
            }
        )
    paths = {
        "source_backed_replay": root / "historical_source_backed_replay.jsonl",
        "source_repair_queue": root / "historical_source_repair_queue.jsonl",
        "replay_provenance": root / "historical_replay_provenance.jsonl",
        "source_backed_manifest": root / "historical_source_backed_manifest.json",
        "source_backed_report": root / "historical_source_backed_report.md",
    }
    write_jsonl(paths["source_backed_replay"], result.replay_rows)
    write_jsonl(paths["source_repair_queue"], result.repair_rows)
    write_jsonl(paths["replay_provenance"], provenance_rows)
    write_json(paths["source_backed_manifest"], result.manifest)
    write_text(paths["source_backed_report"], _render_report(result.manifest))
    return paths


def load_historical_source_backed_snapshot(
    snapshot_root: str | Path,
) -> HistoricalSourceBackedReplayResult:
    """Load a frozen source corpus and independently recheck hashes/anchors."""

    root = Path(snapshot_root)
    manifest = json.loads(
        (root / "historical_source_backed_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    replay_rows = _read_jsonl(root / "historical_source_backed_replay.jsonl")
    repair_rows = _read_jsonl(root / "historical_source_repair_queue.jsonl")
    provenance_rows = _read_jsonl(root / "historical_replay_provenance.jsonl")
    documents: list[HistoricalFrozenDocument] = []
    document_by_id: dict[str, HistoricalFrozenDocument] = {}
    for row in provenance_rows:
        frozen_path = Path(str(row.get("frozen_text_path") or ""))
        if not frozen_path.is_absolute():
            frozen_path = root / frozen_path
        text_with_newline = frozen_path.read_text(encoding="utf-8")
        text = (
            text_with_newline[:-1]
            if text_with_newline.endswith("\n")
            else text_with_newline
        )
        if (
            hashlib.sha256(text.encode("utf-8")).hexdigest()
            != row.get("extracted_text_sha256")
            or hashlib.sha256(frozen_path.read_bytes()).hexdigest()
            != row.get("frozen_text_file_sha256")
            or len(text) != row.get("extracted_text_char_count")
        ):
            raise ValueError("frozen historical source text hash mismatch")
        document = EvidenceDocument(
            document_id=str(row.get("document_id") or ""),
            canonical_url=str(row.get("canonical_url") or ""),
            source_type=SourceType(str(row.get("source_type") or "")),
            source_name=str(row.get("source_name") or ""),
            content_hash=str(row.get("extracted_text_sha256") or ""),
            published_at=date.fromisoformat(str(row.get("published_date") or "")),
            available_at=date.fromisoformat(str(row.get("available_date") or "")),
            fetched_at=date.fromisoformat(str(row.get("fetched_date") or "")),
            parser_version="e2r-historical-fulltext-v1",
            source_lineage_id="HIST-SOURCE-"
            + stable_hash(str(row.get("canonical_url") or ""))[:20],
            source_proxy_only=bool(row.get("source_proxy_only")),
            score_block_reasons=tuple(row.get("score_block_reasons") or ()),
        )
        expected_document = EvidenceDocument.from_text(
            text=text,
            canonical_url=document.canonical_url,
            source_type=document.source_type,
            source_name=document.source_name,
            published_at=document.published_at,
            available_at=document.available_at,
            fetched_at=document.fetched_at,
            parser_version=document.parser_version,
            source_lineage_id=document.source_lineage_id,
            source_proxy_only=document.source_proxy_only,
            score_block_reasons=document.score_block_reasons,
        )
        if expected_document.document_id != document.document_id:
            raise ValueError("frozen historical document id/content mismatch")
        frozen = HistoricalFrozenDocument(
            document=document,
            canonical_url=str(row.get("canonical_url") or ""),
            raw_content_sha256=str(row.get("raw_content_sha256") or ""),
            raw_byte_count=int(row.get("raw_byte_count") or 0),
            content_type="FROZEN_EXTRACTED_TEXT",
            extracted_text=text,
            page_spans=(),
        )
        if document.document_id in document_by_id:
            raise ValueError("duplicate frozen historical document id")
        document_by_id[document.document_id] = frozen
        documents.append(frozen)

    _verify_frozen_replay_rows(replay_rows, document_by_id=document_by_id)
    if stable_hash(replay_rows) != manifest.get("replay_leaf_hash"):
        raise ValueError("frozen historical replay leaf hash mismatch")
    if stable_hash(repair_rows) != manifest.get("repair_queue_hash"):
        raise ValueError("frozen historical repair queue hash mismatch")
    if stable_hash(
        [item.provenance_dict() for item in sorted(documents, key=lambda item: item.document.document_id)]
    ) != manifest.get("source_corpus_hash"):
        raise ValueError("frozen historical source corpus hash mismatch")
    if any(int(value) for value in manifest.get("hard_acceptance_counts", {}).values()):
        raise ValueError("frozen historical source manifest has critical failures")
    return HistoricalSourceBackedReplayResult(
        replay_rows=replay_rows,
        repair_rows=repair_rows,
        documents=tuple(sorted(documents, key=lambda item: item.document.document_id)),
        manifest=manifest,
    )


def _fetch_with_attempts(
    *,
    transport: HistoricalSourceTransport,
    url: str,
    timeout_seconds: int,
    max_attempts: int,
) -> HistoricalHttpResponse:
    last: HistoricalHttpResponse | None = None
    for _ in range(max_attempts):
        last = transport.fetch(url=url, timeout_seconds=timeout_seconds)
        if last.error is None and last.status_code == 200 and last.body:
            return last
    if last is None:
        raise ValueError("historical source fetch was not attempted")
    return last


def _freeze_document(
    *,
    case: Mapping[str, Any],
    response: HistoricalHttpResponse,
    snapshot_date: date,
) -> HistoricalFrozenDocument:
    text, page_spans = _extract_full_text(
        response.body,
        content_type=response.content_type,
    )
    if len(text) < 80:
        raise ValueError("full source extraction is too short")
    published = date.fromisoformat(str(case.get("published_date") or ""))
    available = date.fromisoformat(str(case.get("available_date") or ""))
    as_of = date.fromisoformat(str(case.get("as_of_date") or ""))
    if published > available or available > as_of:
        raise ValueError("historical source date is future-leaking")
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=str(case.get("url") or ""),
        source_type=SourceType(str(case.get("source_type") or "")),
        source_name=str(case.get("source_name") or ""),
        published_at=published,
        available_at=available,
        fetched_at=snapshot_date,
        parser_version="e2r-historical-fulltext-v1",
        source_lineage_id="HIST-SOURCE-" + stable_hash(str(case.get("url") or ""))[:20],
        source_proxy_only=False,
    )
    return HistoricalFrozenDocument(
        document=document,
        canonical_url=str(case.get("url") or ""),
        raw_content_sha256=hashlib.sha256(response.body).hexdigest(),
        raw_byte_count=len(response.body),
        content_type=response.content_type,
        extracted_text=text,
        page_spans=page_spans,
    )


def _compile_case(
    *,
    case: Mapping[str, Any],
    frozen: HistoricalFrozenDocument,
) -> Mapping[str, Any]:
    role = str(case.get("source_role") or "")
    expected_decision = str(case.get("expected_decision") or "")
    expected_directness = Directness(str(case.get("expected_directness") or ""))
    if role not in {"POSITIVE", "GUARD", "WRONG_SUBJECT"}:
        raise ValueError("historical replay role is invalid")
    if expected_decision not in {"ACCEPT_REPLAY_EVIDENCE", "REJECT_SCORE"}:
        raise ValueError("historical replay expected decision is invalid")
    quote_needle = str(case.get("quote_contains") or "").strip()
    start = frozen.extracted_text.casefold().find(quote_needle.casefold())
    if start < 0:
        raise ValueError("exact quote locator was not found in fetched document")
    exact_quote = frozen.extracted_text[start : start + len(quote_needle)]
    page_number = _page_number_for_offset(start, frozen.page_spans)
    locator = (
        f"pdf_page:{page_number};char:{start}:{start + len(exact_quote)}"
        if page_number is not None
        else f"html_char:{start}:{start + len(exact_quote)}"
    )
    markers = tuple(str(item) for item in case.get("target_markers") or ())
    marker_found = any(
        marker.casefold() in frozen.extracted_text.casefold() for marker in markers
    )
    if expected_directness == Directness.DIRECT and not marker_found:
        raise ValueError("target marker missing from direct historical source")
    if expected_directness == Directness.NOT_TARGET_SCOPED and marker_found:
        raise ValueError("wrong-subject probe unexpectedly contains target marker")

    anchor = EvidenceAnchor.text_span(
        document=frozen.document,
        document_text=frozen.extracted_text,
        exact_text=exact_quote,
        locator=locator,
    )
    if not anchor.anchor_verified:
        raise ValueError("historical replay anchor verification failed")
    raw_id = "HRAW-" + stable_hash(
        {
            "case_id": case.get("case_id"),
            "anchor_id": anchor.anchor_id,
            "predicate": case.get("predicate"),
        }
    )[:24]
    raw = RawAssertion(
        raw_assertion_id=raw_id,
        anchor_id=anchor.anchor_id,
        subject_text=str(case.get("target_name") or ""),
        predicate=str(case.get("predicate") or ""),
        object_text=exact_quote,
        polarity_proposal=(
            Polarity.POSITIVE if role == "POSITIVE" else Polarity.CONDITIONAL
        ),
        event_date_text=str(case.get("published_date") or ""),
        exact_quote=exact_quote,
        span=(start, start + len(exact_quote)),
        extractor_model="FROZEN_SOURCE_REPLAY_REGISTRY_V1",
        extractor_prompt_hash=stable_hash(
            {"schema": HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION}
        ),
    )
    accepted = expected_decision == "ACCEPT_REPLAY_EVIDENCE"
    claim = AdjudicatedClaim.from_raw(
        raw=raw,
        document=frozen.document,
        anchor=anchor,
        subject_entity_id=(
            str(case.get("target_entity_id") or "")
            if expected_directness == Directness.DIRECT
            else "ENTITY-OTHER-SUBJECT"
        ),
        target_entity_id=str(case.get("target_entity_id") or ""),
        relation_to_target=(
            RelationToTarget.SELF
            if expected_directness == Directness.DIRECT
            else RelationToTarget.UNRELATED
        ),
        directness=expected_directness,
        verification_status=(
            VerificationStatus.SEMANTIC_VERIFIED
            if accepted
            else VerificationStatus.ANCHOR_VERIFIED
        ),
        target_scope_status=(
            TargetScopeStatus.DIRECT
            if expected_directness == Directness.DIRECT
            else TargetScopeStatus.UNRELATED
        ),
        polarity=Polarity.POSITIVE if accepted else Polarity.CONDITIONAL,
        temporal_status=TemporalStatus.HISTORICAL,
        semantic_status=SemanticStatus.PASS_ if accepted else SemanticStatus.REJECTED,
        investigation_status=InvestigationStatus.COMPLETE,
        event_date=date.fromisoformat(str(case.get("published_date") or "")),
        adjudication_rationale=(
            "fetched URL, exact anchor, historical date, and target directness verified"
            if accepted
            else "guard or wrong-subject evidence is anchored but score-ineligible"
        ),
    )
    mapping = PrimitiveMappingProposal.build(
        claim_id=claim.claim_id,
        archetype_id=str(case.get("archetype_id") or ""),
        primitive_id=str(case.get("primitive_id") or ""),
        support_direction=(
            SupportDirection.SUPPORT if accepted else SupportDirection.NEUTRAL
        ),
        mapping_status=MappingStatus.ACCEPTED if accepted else MappingStatus.REJECTED,
        rationale=(
            "frozen positive replay mapping accepted"
            if accepted
            else "frozen guard mapping rejected"
        ),
    )
    eligibility = derive_score_eligibility(
        document=frozen.document,
        anchor=anchor,
        claim=claim,
        mapping=mapping,
        as_of_date=date.fromisoformat(str(case.get("as_of_date") or "")),
        allowed_temporal_statuses=(TemporalStatus.HISTORICAL,),
    )
    observed_decision = (
        "ACCEPT_REPLAY_EVIDENCE" if eligibility.eligible else "REJECT_SCORE"
    )
    if observed_decision != expected_decision:
        raise ValueError("historical replay observed decision mismatch")
    return {
        "schema_version": HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION,
        "case_id": case.get("case_id"),
        "archetype_id": case.get("archetype_id"),
        "primitive_id": case.get("primitive_id"),
        "source_role": role,
        "replay_status": "REPLAY_READY",
        "as_of_date": case.get("as_of_date"),
        "published_date": case.get("published_date"),
        "available_date": case.get("available_date"),
        "target_entity_id": case.get("target_entity_id"),
        "target_name": case.get("target_name"),
        "target_marker_found": marker_found,
        "directness": claim.directness.value,
        "target_scope_status": claim.target_scope_status.value,
        "canonical_url": frozen.canonical_url,
        "document_id": frozen.document.document_id,
        "raw_content_sha256": frozen.raw_content_sha256,
        "extracted_text_sha256": frozen.document.content_hash,
        "raw_assertion_id": raw.raw_assertion_id,
        "anchor_id": anchor.anchor_id,
        "anchor_type": anchor.anchor_type.value,
        "anchor_locator": anchor.locator,
        "anchor_verified": anchor.anchor_verified,
        "exact_quote": exact_quote,
        "claim_id": claim.claim_id,
        "verification_status": claim.verification_status.value,
        "semantic_status": claim.semantic_status.value,
        "temporal_status": claim.temporal_status.value,
        "mapping_id": mapping.mapping_id,
        "mapping_status": mapping.mapping_status.value,
        "score_eligible_in_frozen_replay": eligibility.eligible,
        "score_eligibility_reasons": list(eligibility.reasons),
        "expected_decision": expected_decision,
        "observed_decision": observed_decision,
        "historical_score_credit": 0,
        "current_score_credit": 0,
        "current_watchlist_eligible": False,
        "source_proxy_only": False,
        "url_string_only": False,
    }


def _inventory_source_repairs(inventory: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    repairs: list[Mapping[str, Any]] = []
    for row in _mapping_rows(inventory.get("records")):
        urls = tuple(str(item) for item in row.get("source_urls") or () if str(item).strip())
        if not urls:
            continue
        proxy = row.get("source_proxy_only") is True
        pending = row.get("evidence_url_pending") is True
        if proxy:
            blocker = "SOURCE_PROXY_ONLY"
            detail = "research memory row is a planning proxy and has no score-eligible frozen source"
        elif pending:
            blocker = "EVIDENCE_URL_PENDING"
            detail = "research memory row explicitly lacks a verified evidence URL snapshot"
        else:
            blocker = "URL_ONLY_WITHOUT_FROZEN_CONTENT_AND_ANCHOR"
            detail = "URL strings exist but full content hash, historical date, and exact anchor are unverified"
        repairs.append(
            _repair_row(
                case_id=str(row.get("research_case_id") or ""),
                archetype_id=str(row.get("canonical_archetype_id") or ""),
                source_url=urls[0],
                blocker_code=blocker,
                blocker_detail=detail,
                source_proxy_only=proxy,
                evidence_url_pending=pending,
            )
        )
    return tuple(repairs)


def _verify_frozen_replay_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    document_by_id: Mapping[str, HistoricalFrozenDocument],
) -> None:
    case_ids: set[str] = set()
    for row in rows:
        case_id = str(row.get("case_id") or "")
        if not case_id or case_id in case_ids:
            raise ValueError("duplicate or empty frozen replay case id")
        case_ids.add(case_id)
        frozen = document_by_id.get(str(row.get("document_id") or ""))
        if frozen is None:
            raise ValueError("frozen replay row references missing document")
        exact_quote = str(row.get("exact_quote") or "")
        anchor = EvidenceAnchor.text_span(
            document=frozen.document,
            document_text=frozen.extracted_text,
            exact_text=exact_quote,
            locator=str(row.get("anchor_locator") or ""),
        )
        as_of = date.fromisoformat(str(row.get("as_of_date") or ""))
        published = date.fromisoformat(str(row.get("published_date") or ""))
        available = date.fromisoformat(str(row.get("available_date") or ""))
        if (
            not anchor.anchor_verified
            or anchor.anchor_id != row.get("anchor_id")
            or row.get("anchor_verified") is not True
            or row.get("canonical_url") != frozen.canonical_url
            or row.get("raw_content_sha256") != frozen.raw_content_sha256
            or row.get("extracted_text_sha256") != frozen.document.content_hash
            or published > available
            or available > as_of
            or row.get("url_string_only") is not False
            or row.get("source_proxy_only") is not False
            or int(row.get("historical_score_credit") or 0) != 0
            or int(row.get("current_score_credit") or 0) != 0
            or row.get("current_watchlist_eligible") is not False
        ):
            raise ValueError("frozen historical replay row integrity failure")
        positive = row.get("source_role") == "POSITIVE"
        if positive and (
            row.get("mapping_status") != MappingStatus.ACCEPTED.value
            or row.get("score_eligible_in_frozen_replay") is not True
            or row.get("observed_decision") != "ACCEPT_REPLAY_EVIDENCE"
        ):
            raise ValueError("frozen historical positive replay decision mismatch")
        if not positive and (
            row.get("mapping_status") != MappingStatus.REJECTED.value
            or row.get("score_eligible_in_frozen_replay") is not False
            or row.get("observed_decision") != "REJECT_SCORE"
        ):
            raise ValueError("frozen historical guard replay decision mismatch")
        if row.get("source_role") == "WRONG_SUBJECT" and (
            row.get("directness") != Directness.NOT_TARGET_SCOPED.value
            or row.get("target_scope_status") != TargetScopeStatus.UNRELATED.value
            or row.get("target_marker_found") is not False
        ):
            raise ValueError("frozen wrong-subject guard was not rejected")


def _repair_row(
    *,
    case_id: str,
    archetype_id: str,
    source_url: str,
    blocker_code: str,
    blocker_detail: str,
    source_proxy_only: bool,
    evidence_url_pending: bool,
) -> Mapping[str, Any]:
    return {
        "schema_version": HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION,
        "repair_id": "HREPAIR-" + stable_hash(
            {"case_id": case_id, "archetype_id": archetype_id, "url": source_url}
        )[:24],
        "case_id": case_id,
        "archetype_id": archetype_id,
        "source_url": source_url,
        "status": "SOURCE_REPAIR_REQUIRED",
        "blocker_code": blocker_code,
        "blocker_detail": blocker_detail,
        "source_proxy_only": source_proxy_only,
        "evidence_url_pending": evidence_url_pending,
        "score_eligible": False,
        "historical_score_credit": 0,
        "current_score_credit": 0,
    }


def _hard_acceptance_counts(
    *,
    replay_rows: Sequence[Mapping[str, Any]],
    repair_rows: Sequence[Mapping[str, Any]],
    canary_archetype_ids: Sequence[str],
    inventory: Mapping[str, Any],
) -> Mapping[str, int]:
    inventory_url_rows = tuple(
        row
        for row in _mapping_rows(inventory.get("records"))
        if row.get("source_urls")
    )
    ready_by_archetype: dict[str, set[str]] = {}
    for row in replay_rows:
        ready_by_archetype.setdefault(str(row.get("archetype_id") or ""), set()).add(
            str(row.get("source_role") or "")
        )
    return {
        "url_string_only_replay_ready_count": sum(
            row.get("replay_status") == "REPLAY_READY"
            and (
                row.get("url_string_only") is not False
                or not row.get("raw_content_sha256")
                or not row.get("extracted_text_sha256")
                or row.get("anchor_verified") is not True
            )
            for row in replay_rows
        ),
        "source_proxy_replay_score_count": sum(
            row.get("source_proxy_only") is True
            and int(row.get("historical_score_credit") or 0) != 0
            for row in (*replay_rows, *repair_rows)
        ),
        "future_leakage_count": sum(
            date.fromisoformat(str(row["published_date"]))
            > date.fromisoformat(str(row["as_of_date"]))
            or date.fromisoformat(str(row["available_date"]))
            > date.fromisoformat(str(row["as_of_date"]))
            for row in replay_rows
        ),
        "wrong_subject_replay_accepted_count": sum(
            row.get("source_role") == "WRONG_SUBJECT"
            and row.get("observed_decision") != "REJECT_SCORE"
            for row in replay_rows
        ),
        "canary_missing_positive_count": sum(
            "POSITIVE" not in ready_by_archetype.get(archetype_id, set())
            for archetype_id in canary_archetype_ids
        ),
        "canary_missing_guard_count": sum(
            "GUARD" not in ready_by_archetype.get(archetype_id, set())
            for archetype_id in canary_archetype_ids
        ),
        "canary_source_backed_replay_zero_count": int(not replay_rows),
        "curated_case_not_replay_ready_count": sum(
            row.get("blocker_code") == "SOURCE_FETCH_OR_ANCHOR_VERIFICATION_FAILED"
            for row in repair_rows
        ),
        "registry_url_case_unresolved_count": abs(
            len(inventory_url_rows)
            - sum(
                row.get("blocker_code")
                != "SOURCE_FETCH_OR_ANCHOR_VERIFICATION_FAILED"
                for row in repair_rows
            )
        ),
        "duplicate_replay_case_count": len(replay_rows)
        - len({str(row.get("case_id") or "") for row in replay_rows}),
    }


def _extract_full_text(
    body: bytes,
    *,
    content_type: str,
) -> tuple[str, tuple[tuple[int, int], ...]]:
    if body.startswith(b"%PDF") or "pdf" in content_type.casefold():
        reader = PdfReader(io.BytesIO(body))
        parts: list[str] = []
        spans: list[tuple[int, int]] = []
        cursor = 0
        for page in reader.pages:
            page_text = _normalize_text(page.extract_text() or "")
            start = cursor
            parts.append(page_text)
            cursor += len(page_text)
            spans.append((start, cursor))
            cursor += 1
        return "\n".join(parts), tuple(spans)
    decoded = body.decode("utf-8", errors="replace")
    parser = _VisibleTextParser()
    parser.feed(decoded)
    return _normalize_text("".join(parser.parts)), ()


class _VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
        elif not self._skip_depth and tag in {"p", "br", "li", "h1", "h2", "h3", "td", "th"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self._skip_depth:
            self._skip_depth -= 1
        elif not self._skip_depth and tag in {"p", "li", "h1", "h2", "h3", "td", "th"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self.parts.append(data)


def _normalize_text(value: str) -> str:
    lines = []
    for line in html.unescape(value).splitlines():
        normalized = " ".join(line.split())
        if normalized:
            lines.append(normalized)
    return "\n".join(lines)


def _page_number_for_offset(
    offset: int,
    spans: Sequence[tuple[int, int]],
) -> int | None:
    for index, (start, end) in enumerate(spans, start=1):
        if start <= offset <= end:
            return index
    return None


def _render_report(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        (
            "# Historical Source-Backed Replay",
            "",
            f"- status: {manifest['status']}",
            f"- replay-ready cases: {manifest['replay_ready_count']}",
            f"- positive / guard: {manifest['positive_replay_ready_count']} / {manifest['guard_replay_ready_count']}",
            f"- unique full documents: {manifest['fetched_unique_document_count']}",
            f"- registry repair queue: {manifest['registry_source_repair_count']}",
            f"- hard acceptance: {manifest['hard_acceptance_counts']}",
            "- historical replay evidence is isolated from current scoring/watchlist.",
            "- direct investment recommendation: none",
            "",
        )
    )


def _resolve_path(root: Path, path: str | Path) -> Path:
    selected = Path(path)
    return selected if selected.is_absolute() else root / selected


def _mapping_rows(value: Any) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return ()
    return tuple(dict(item) for item in value if isinstance(item, Mapping))


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        rows = tuple(json.loads(line) for line in handle if line.strip())
    if any(not isinstance(row, Mapping) for row in rows):
        raise ValueError("historical snapshot JSONL contains a non-object row")
    return rows


def _positive_int(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("historical source fetch budget must be a positive integer")
    return value


def _date_string(value: Any) -> str | None:
    if isinstance(value, date):
        return value.isoformat()
    return None


__all__ = [
    "HISTORICAL_SOURCE_BACKED_REPLAY_SCHEMA_VERSION",
    "HistoricalFrozenDocument",
    "HistoricalHttpResponse",
    "HistoricalSourceBackedReplayResult",
    "HistoricalSourceTransport",
    "RequestsHistoricalSourceTransport",
    "compile_historical_source_backed_replay",
    "load_historical_source_backed_snapshot",
    "write_historical_source_backed_replay",
]
