"""Case-level historical source verification for canonical research intelligence."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import urlsplit, urlunsplit

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.intelligence_schema import (
    HistoricalCaseSourceLink,
    HistoricalCaseSourceRelationship,
    HistoricalEvidenceReference,
    HistoricalProviderSnapshot,
    HistoricalResearchCase,
    HistoricalSnapshotAnchor,
    HistoricalSourceRepairTask,
    HistoricalSourceState,
    HistoricalSourceVerification,
    stable_intelligence_id,
)


_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_DIRECT_RELATIONSHIPS = {
    HistoricalCaseSourceRelationship.CASE_MATCH.value,
    HistoricalCaseSourceRelationship.COUNTER_CASE_MATCH.value,
}
_STATE_RANK = {
    HistoricalSourceState.SOURCE_PROXY_ONLY.value: 0,
    HistoricalSourceState.EVIDENCE_URL_PENDING.value: 1,
    HistoricalSourceState.URL_PRESENT_UNVERIFIED.value: 2,
    HistoricalSourceState.URL_FETCH_FAILED.value: 3,
    HistoricalSourceState.URL_FETCHED_NO_ANCHOR.value: 4,
    HistoricalSourceState.URL_FETCHED_WRONG_SUBJECT.value: 5,
    HistoricalSourceState.URL_FETCHED_DATE_INVALID.value: 6,
    HistoricalSourceState.URL_FETCHED_ANCHORED.value: 7,
    HistoricalSourceState.URL_FETCHED_ANCHORED_CASE_MATCH.value: 8,
    HistoricalSourceState.HISTORICAL_REPLAY_READY.value: 9,
}


@dataclass(frozen=True)
class SourceVerificationCompilationResult:
    snapshots: tuple[HistoricalProviderSnapshot, ...]
    case_source_links: tuple[HistoricalCaseSourceLink, ...]
    verifications: tuple[HistoricalSourceVerification, ...]
    repair_tasks: tuple[HistoricalSourceRepairTask, ...]
    case_statuses: tuple[Mapping[str, Any], ...]
    manifest: Mapping[str, Any]


def load_historical_provider_snapshots(
    path: str | Path,
) -> tuple[HistoricalProviderSnapshot, ...]:
    rows = _load_jsonl(path)
    snapshots: list[HistoricalProviderSnapshot] = []
    seen: set[str] = set()
    for row in rows:
        anchors = tuple(
            HistoricalSnapshotAnchor(
                anchor_id=str(anchor["anchor_id"]),
                locator=str(anchor["locator"]),
                exact_text=str(anchor["exact_text"]),
                anchor_type=str(anchor.get("anchor_type") or "TEXT_SPAN"),
            )
            for anchor in row.get("anchors", [])
        )
        snapshot = HistoricalProviderSnapshot(
            snapshot_id=str(row["snapshot_id"]),
            canonical_url=_optional_text(row.get("canonical_url")),
            official_document_id=_optional_text(row.get("official_document_id")),
            provider_name=str(row["provider_name"]),
            provider_record_id=str(row["provider_record_id"]),
            fetch_status=str(row.get("fetch_status") or "FAILED").upper(),
            content_path=_optional_text(row.get("content_path")),
            content_sha256=_optional_text(row.get("content_sha256")),
            published_date=_optional_text(row.get("published_date")),
            available_date=_optional_text(row.get("available_date")),
            captured_at=_optional_text(row.get("captured_at")),
            title=_optional_text(row.get("title")),
            source_type=str(row.get("source_type") or "unknown"),
            subject_symbols=tuple(str(item) for item in row.get("subject_symbols", [])),
            subject_names=tuple(str(item) for item in row.get("subject_names", [])),
            anchors=anchors,
            valid_provider_snapshot=_bool_value(
                row.get("valid_provider_snapshot"),
                field="valid_provider_snapshot",
            ),
            replay_only=_bool_value(
                row.get("replay_only", True),
                field="replay_only",
            ),
            production_score_evidence_allowed=_bool_value(
                row.get("production_score_evidence_allowed", False),
                field="production_score_evidence_allowed",
            ),
            metadata=dict(row.get("metadata") or {}),
        )
        if snapshot.snapshot_id in seen:
            raise ValueError(f"duplicate provider snapshot id: {snapshot.snapshot_id}")
        seen.add(snapshot.snapshot_id)
        snapshots.append(snapshot)
    return tuple(snapshots)


def load_historical_case_source_links(
    path: str | Path,
) -> tuple[HistoricalCaseSourceLink, ...]:
    rows = _load_jsonl(path)
    links: list[HistoricalCaseSourceLink] = []
    seen: set[str] = set()
    for row in rows:
        link = HistoricalCaseSourceLink(
            link_id=str(row["link_id"]),
            case_id=str(row["case_id"]),
            snapshot_id=str(row["snapshot_id"]),
            anchor_ids=tuple(str(item) for item in row.get("anchor_ids", [])),
            relationship=str(row["relationship"]),
            target_directness=str(row.get("target_directness") or "UNKNOWN").upper(),
            summary_consistent=_bool_value(
                row.get("summary_consistent"),
                field="summary_consistent",
            ),
            rationale=str(row.get("rationale") or ""),
            verifier_origin=str(row.get("verifier_origin") or ""),
            verifier_prompt_hash=str(row.get("verifier_prompt_hash") or ""),
            verifier_response_hash=str(row.get("verifier_response_hash") or ""),
            verified=_bool_value(row.get("verified", True), field="verified"),
            current_score_evidence_allowed=_bool_value(
                row.get("current_score_evidence_allowed", False),
                field="current_score_evidence_allowed",
            ),
        )
        if link.link_id in seen:
            raise ValueError(f"duplicate case/source link id: {link.link_id}")
        seen.add(link.link_id)
        links.append(link)
    return tuple(links)


def compile_case_level_source_verification(
    cases: Iterable[HistoricalResearchCase],
    *,
    snapshots: Sequence[HistoricalProviderSnapshot] = (),
    case_source_links: Sequence[HistoricalCaseSourceLink] = (),
    repo_root: str | Path = ".",
    url_backed_golden_case_ids: Iterable[str] = (),
    source_proxy_golden_case_ids: Iterable[str] = (),
) -> SourceVerificationCompilationResult:
    root = Path(repo_root).resolve()
    ordered_cases = tuple(sorted(cases, key=lambda item: item.case_id))
    case_ids = {case.case_id for case in ordered_cases}
    snapshot_by_id = {snapshot.snapshot_id: snapshot for snapshot in snapshots}
    if len(snapshot_by_id) != len(snapshots):
        raise ValueError("duplicate snapshot ids")
    links_by_case_snapshot: dict[tuple[str, str], list[HistoricalCaseSourceLink]] = {}
    for link in case_source_links:
        if link.case_id not in case_ids:
            raise ValueError(f"case/source link references unknown case: {link.case_id}")
        if link.snapshot_id not in snapshot_by_id:
            raise ValueError(f"case/source link references unknown snapshot: {link.snapshot_id}")
        links_by_case_snapshot.setdefault((link.case_id, link.snapshot_id), []).append(link)
    snapshot_index = _snapshot_reference_index(snapshots)

    verifications: list[HistoricalSourceVerification] = []
    for case in ordered_cases:
        quality = str(case.declared_source_quality or "").upper()
        if quality == HistoricalSourceState.SOURCE_PROXY_ONLY.value:
            verifications.append(
                _terminal_without_snapshot(
                    case,
                    state=HistoricalSourceState.SOURCE_PROXY_ONLY,
                    blocker_code="SOURCE_PROXY_REQUIRES_CASE_LEVEL_SOURCE",
                    blocker_detail="research summary exists but no verified case-level source is attached",
                )
            )
            continue
        if quality == HistoricalSourceState.EVIDENCE_URL_PENDING.value:
            verifications.append(
                _terminal_without_snapshot(
                    case,
                    state=HistoricalSourceState.EVIDENCE_URL_PENDING,
                    blocker_code="EVIDENCE_URL_REPAIR_REQUIRED",
                    blocker_detail="case declares that its evidence URL still needs repair",
                )
            )
            continue

        references = tuple(
            reference
            for reference in case.evidence_references
            if reference.url or reference.document_id
        )
        if not references:
            verifications.append(
                _terminal_without_snapshot(
                    case,
                    state=HistoricalSourceState.SOURCE_PROXY_ONLY,
                    blocker_code="CASE_LEVEL_SOURCE_ASSOCIATION_MISSING",
                    blocker_detail="no URL or official document id is attached to this case",
                )
            )
            continue

        for reference_index, reference in enumerate(references):
            matching_snapshots = _matching_snapshots(reference, snapshot_index)
            if not matching_snapshots:
                verifications.append(
                    _terminal_reference_only(
                        case,
                        reference,
                        reference_index=reference_index,
                        blocker_code="PROVIDER_SNAPSHOT_NOT_FOUND",
                        blocker_detail="URL/document id exists, but no fetched or valid provider snapshot is registered",
                    )
                )
                continue
            for snapshot in matching_snapshots:
                links = links_by_case_snapshot.get((case.case_id, snapshot.snapshot_id), [])
                verifications.append(
                    _verify_snapshot_reference(
                        case=case,
                        reference=reference,
                        reference_index=reference_index,
                        snapshot=snapshot,
                        links=links,
                        repo_root=root,
                    )
                )

    case_statuses = _build_case_statuses(ordered_cases, verifications)
    repair_tasks = _build_repair_tasks(case_statuses, verifications)
    manifest = _build_source_verification_manifest(
        cases=ordered_cases,
        snapshots=snapshots,
        links=case_source_links,
        verifications=verifications,
        repair_tasks=repair_tasks,
        case_statuses=case_statuses,
        url_backed_golden_case_ids=set(url_backed_golden_case_ids),
        source_proxy_golden_case_ids=set(source_proxy_golden_case_ids),
    )
    return SourceVerificationCompilationResult(
        snapshots=tuple(snapshots),
        case_source_links=tuple(case_source_links),
        verifications=tuple(verifications),
        repair_tasks=tuple(repair_tasks),
        case_statuses=tuple(case_statuses),
        manifest=manifest,
    )


def write_case_level_source_verification(
    result: SourceVerificationCompilationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root) / "source_verification"
    paths = {
        "snapshots": root / "provider_snapshots.jsonl",
        "case_source_links": root / "case_source_links.jsonl",
        "verifications": root / "source_verifications.jsonl",
        "replay_ready": root / "historical_replay_ready_sources.jsonl",
        "repair_queue": root / "source_repair_queue.jsonl",
        "case_statuses": root / "case_source_statuses.jsonl",
        "manifest": root / "source_verification_manifest.json",
        "report": root / "source_verification_report.md",
    }
    write_jsonl(paths["snapshots"], (item.to_dict() for item in result.snapshots))
    write_jsonl(
        paths["case_source_links"],
        (item.to_dict() for item in result.case_source_links),
    )
    write_jsonl(paths["verifications"], (item.to_dict() for item in result.verifications))
    write_jsonl(
        paths["replay_ready"],
        (
            item.to_dict()
            for item in result.verifications
            if item.historical_replay_ready
        ),
    )
    write_jsonl(paths["repair_queue"], (item.to_dict() for item in result.repair_tasks))
    write_jsonl(paths["case_statuses"], result.case_statuses)
    write_json(paths["manifest"], dict(result.manifest))
    write_text(paths["report"], render_source_verification_report(result.manifest))
    return paths


def render_source_verification_report(manifest: Mapping[str, Any]) -> str:
    lines = [
        "# E2R Case-Level Historical Source Verification",
        "",
        f"- status: {manifest['status']}",
        f"- case_count: {manifest['case_count']}",
        f"- verification_count: {manifest['verification_count']}",
        f"- historical_replay_ready_count: {manifest['historical_replay_ready_count']}",
        f"- repair_task_count: {manifest['repair_task_count']}",
        f"- critical_count_sum: {manifest['critical_count_sum']}",
        "",
        "URL presence alone is never historical A2. Every ready row has a content hash,",
        "published/available date, direct target, exact anchor, semantic case match,",
        "summary-consistency decision, and historical/current separation.",
    ]
    return "\n".join(lines) + "\n"


def _verify_snapshot_reference(
    *,
    case: HistoricalResearchCase,
    reference: HistoricalEvidenceReference,
    reference_index: int,
    snapshot: HistoricalProviderSnapshot,
    links: Sequence[HistoricalCaseSourceLink],
    repo_root: Path,
) -> HistoricalSourceVerification:
    trace = [HistoricalSourceState.URL_PRESENT_UNVERIFIED.value]
    checks = _blank_checks()
    checks["url_or_official_document"] = bool(reference.url or reference.document_id)
    checks["case_level_source_association"] = _reference_matches_snapshot(reference, snapshot)
    historical_as_of = _parse_date(case.trigger_date or case.entry_date)

    if snapshot.fetch_status != "FETCHED":
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCH_FAILED,
            blocker_code="SNAPSHOT_FETCH_FAILED",
            blocker_detail=f"snapshot fetch_status={snapshot.fetch_status}",
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
        )
    content_path = _resolve_content_path(snapshot.content_path, repo_root)
    if content_path is None or not content_path.is_file():
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCH_FAILED,
            blocker_code="SNAPSHOT_CONTENT_MISSING",
            blocker_detail=f"content_path={snapshot.content_path!r}",
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
        )
    raw_bytes = content_path.read_bytes()
    content_hash = hashlib.sha256(raw_bytes).hexdigest()
    content = raw_bytes.decode("utf-8", errors="replace")
    checks["fetch_or_valid_snapshot"] = bool(content.strip())
    checks["content_hash_verified"] = bool(
        snapshot.content_sha256
        and _SHA256_RE.fullmatch(snapshot.content_sha256)
        and content_hash == snapshot.content_sha256
    )
    if not checks["fetch_or_valid_snapshot"] or not checks["content_hash_verified"]:
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCH_FAILED,
            blocker_code=(
                "SNAPSHOT_CONTENT_EMPTY"
                if not checks["fetch_or_valid_snapshot"]
                else "CONTENT_HASH_MISMATCH"
            ),
            blocker_detail=(
                "snapshot content is empty"
                if not checks["fetch_or_valid_snapshot"]
                else f"expected={snapshot.content_sha256};actual={content_hash}"
            ),
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
            content_hash=content_hash,
        )

    published = _parse_date(snapshot.published_date)
    available = _parse_date(snapshot.available_date)
    checks["published_date_present"] = published is not None
    checks["historical_as_of_present"] = historical_as_of is not None
    checks["published_on_or_before_as_of"] = bool(
        published and historical_as_of and published <= historical_as_of
    )
    checks["available_on_or_before_as_of"] = bool(
        available and historical_as_of and available <= historical_as_of
    )
    if not all(
        checks[key]
        for key in (
            "published_date_present",
            "historical_as_of_present",
            "published_on_or_before_as_of",
            "available_on_or_before_as_of",
        )
    ):
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCHED_DATE_INVALID,
            blocker_code="HISTORICAL_DATE_OR_AVAILABILITY_INVALID",
            blocker_detail=(
                f"published={snapshot.published_date};available={snapshot.available_date};"
                f"historical_as_of={case.trigger_date or case.entry_date}"
            ),
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
            content_hash=content_hash,
        )

    checks["target_direct"] = _target_is_direct(case, snapshot, content)
    if not checks["target_direct"]:
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCHED_WRONG_SUBJECT,
            blocker_code="TARGET_DIRECTNESS_FAILED",
            blocker_detail=(
                f"case={case.symbol}:{case.company_name};"
                f"snapshot_symbols={list(snapshot.subject_symbols)};"
                f"snapshot_names={list(snapshot.subject_names)}"
            ),
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
            content_hash=content_hash,
        )

    selected_link = _select_verified_link(links)
    anchors_by_id = {anchor.anchor_id: anchor for anchor in snapshot.anchors}
    selected_anchor_ids = (
        selected_link.anchor_ids if selected_link else tuple(anchors_by_id)
    )
    anchors = tuple(
        anchors_by_id[anchor_id]
        for anchor_id in selected_anchor_ids
        if anchor_id in anchors_by_id
    )
    checks["exact_anchor_verified"] = bool(anchors) and len(anchors) == len(selected_anchor_ids) and all(
        anchor.exact_text in content and bool(anchor.locator.strip())
        for anchor in anchors
    )
    if not checks["exact_anchor_verified"]:
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCHED_NO_ANCHOR,
            blocker_code="EXACT_ANCHOR_MISSING_OR_INVALID",
            blocker_detail=f"requested_anchor_ids={list(selected_anchor_ids)}",
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
            content_hash=content_hash,
        )
    trace.append(HistoricalSourceState.URL_FETCHED_ANCHORED.value)

    if selected_link is None:
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCHED_ANCHORED,
            blocker_code="CASE_SEMANTIC_LINK_MISSING",
            blocker_detail="snapshot has a verified anchor but no verified case/source adjudication",
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
            content_hash=content_hash,
            anchors=anchors,
        )

    checks["link_verification_provenance"] = _link_provenance_valid(selected_link)
    checks["case_semantic_match"] = bool(
        selected_link.verified
        and selected_link.relationship in _DIRECT_RELATIONSHIPS
        and selected_link.target_directness == "DIRECT"
        and checks["link_verification_provenance"]
    )
    if not checks["case_semantic_match"]:
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCHED_ANCHORED,
            blocker_code="CASE_SEMANTIC_MATCH_FAILED",
            blocker_detail=(
                f"relationship={selected_link.relationship};"
                f"directness={selected_link.target_directness};verified={selected_link.verified}"
            ),
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
            content_hash=content_hash,
            anchors=anchors,
            link=selected_link,
        )
    trace.append(HistoricalSourceState.URL_FETCHED_ANCHORED_CASE_MATCH.value)
    checks["summary_consistent"] = selected_link.summary_consistent
    checks["provider_snapshot_valid"] = bool(
        snapshot.valid_provider_snapshot
        and snapshot.provider_name.strip()
        and snapshot.provider_record_id.strip()
        and _parse_datetime(snapshot.captured_at) is not None
    )
    checks["historical_current_separation"] = bool(
        snapshot.replay_only
        and not snapshot.production_score_evidence_allowed
        and not selected_link.current_score_evidence_allowed
        and not case.runtime_score_eligible
    )
    if not checks["summary_consistent"]:
        blocker_code = "CASE_SUMMARY_SOURCE_CONTRADICTION"
        blocker_detail = selected_link.rationale
    elif not checks["provider_snapshot_valid"]:
        blocker_code = "PROVIDER_SNAPSHOT_NOT_VALID"
        blocker_detail = "snapshot is fetched but does not carry valid provider/archive provenance"
    elif not checks["historical_current_separation"]:
        blocker_code = "HISTORICAL_CURRENT_EVIDENCE_BOUNDARY_FAILED"
        blocker_detail = "historical replay material attempted to enter current scoring"
    else:
        blocker_code = None
        blocker_detail = None

    if blocker_code:
        return _verification(
            case=case,
            reference=reference,
            reference_index=reference_index,
            snapshot=snapshot,
            state=HistoricalSourceState.URL_FETCHED_ANCHORED_CASE_MATCH,
            blocker_code=blocker_code,
            blocker_detail=blocker_detail,
            checks=checks,
            trace=trace,
            historical_as_of=historical_as_of,
            content_hash=content_hash,
            anchors=anchors,
            link=selected_link,
        )

    trace.append(HistoricalSourceState.HISTORICAL_REPLAY_READY.value)
    return _verification(
        case=case,
        reference=reference,
        reference_index=reference_index,
        snapshot=snapshot,
        state=HistoricalSourceState.HISTORICAL_REPLAY_READY,
        blocker_code=None,
        blocker_detail=None,
        checks=checks,
        trace=trace,
        historical_as_of=historical_as_of,
        content_hash=content_hash,
        anchors=anchors,
        link=selected_link,
    )


def _verification(
    *,
    case: HistoricalResearchCase,
    reference: HistoricalEvidenceReference,
    reference_index: int,
    snapshot: HistoricalProviderSnapshot,
    state: HistoricalSourceState,
    blocker_code: str | None,
    blocker_detail: str | None,
    checks: Mapping[str, bool],
    trace: Sequence[str],
    historical_as_of: date | None,
    content_hash: str | None = None,
    anchors: Sequence[HistoricalSnapshotAnchor] = (),
    link: HistoricalCaseSourceLink | None = None,
) -> HistoricalSourceVerification:
    ready = state is HistoricalSourceState.HISTORICAL_REPLAY_READY
    payload = {
        "case_id": case.case_id,
        "reference_index": reference_index,
        "snapshot_id": snapshot.snapshot_id,
        "state": state.value,
    }
    return HistoricalSourceVerification(
        verification_id=stable_intelligence_id("HSVER", payload),
        case_id=case.case_id,
        artifact_id=case.artifact_id,
        source_state=state.value,
        source_url=reference.url,
        official_document_id=reference.document_id,
        snapshot_id=snapshot.snapshot_id,
        content_sha256=content_hash,
        published_date=snapshot.published_date,
        historical_as_of_date=historical_as_of.isoformat() if historical_as_of else None,
        anchor_ids=tuple(anchor.anchor_id for anchor in anchors),
        anchor_locators=tuple(anchor.locator for anchor in anchors),
        exact_quotes=tuple(anchor.exact_text for anchor in anchors),
        target_directness=(link.target_directness if link else ("DIRECT" if checks.get("target_direct") else "UNKNOWN")),
        case_relationship=link.relationship if link else None,
        summary_consistent=link.summary_consistent if link else None,
        blocker_code=blocker_code,
        blocker_detail=blocker_detail,
        checks=dict(checks),
        state_trace=tuple(dict.fromkeys([*trace, state.value])),
        historical_replay_ready=ready,
        a2_historical_evidence_eligible=ready,
    )


def _terminal_without_snapshot(
    case: HistoricalResearchCase,
    *,
    state: HistoricalSourceState,
    blocker_code: str,
    blocker_detail: str,
) -> HistoricalSourceVerification:
    return HistoricalSourceVerification(
        verification_id=stable_intelligence_id(
            "HSVER", {"case_id": case.case_id, "state": state.value}
        ),
        case_id=case.case_id,
        artifact_id=case.artifact_id,
        source_state=state.value,
        source_url=None,
        official_document_id=None,
        snapshot_id=None,
        content_sha256=None,
        published_date=None,
        historical_as_of_date=case.trigger_date or case.entry_date,
        anchor_ids=(),
        anchor_locators=(),
        exact_quotes=(),
        target_directness="UNKNOWN",
        case_relationship=None,
        summary_consistent=None,
        blocker_code=blocker_code,
        blocker_detail=blocker_detail,
        checks=_blank_checks(),
        state_trace=(state.value,),
        historical_replay_ready=False,
        a2_historical_evidence_eligible=False,
    )


def _terminal_reference_only(
    case: HistoricalResearchCase,
    reference: HistoricalEvidenceReference,
    *,
    reference_index: int,
    blocker_code: str,
    blocker_detail: str,
) -> HistoricalSourceVerification:
    checks = _blank_checks()
    checks["url_or_official_document"] = bool(reference.url or reference.document_id)
    checks["case_level_source_association"] = True
    return HistoricalSourceVerification(
        verification_id=stable_intelligence_id(
            "HSVER",
            {
                "case_id": case.case_id,
                "reference_index": reference_index,
                "url": reference.url,
                "document_id": reference.document_id,
            },
        ),
        case_id=case.case_id,
        artifact_id=case.artifact_id,
        source_state=HistoricalSourceState.URL_PRESENT_UNVERIFIED.value,
        source_url=reference.url,
        official_document_id=reference.document_id,
        snapshot_id=None,
        content_sha256=None,
        published_date=None,
        historical_as_of_date=case.trigger_date or case.entry_date,
        anchor_ids=(),
        anchor_locators=(),
        exact_quotes=(),
        target_directness="UNKNOWN",
        case_relationship=None,
        summary_consistent=None,
        blocker_code=blocker_code,
        blocker_detail=blocker_detail,
        checks=checks,
        state_trace=(HistoricalSourceState.URL_PRESENT_UNVERIFIED.value,),
        historical_replay_ready=False,
        a2_historical_evidence_eligible=False,
    )


def _build_case_statuses(
    cases: Sequence[HistoricalResearchCase],
    verifications: Sequence[HistoricalSourceVerification],
) -> list[Mapping[str, Any]]:
    by_case: dict[str, list[HistoricalSourceVerification]] = {}
    for verification in verifications:
        by_case.setdefault(verification.case_id, []).append(verification)
    statuses: list[Mapping[str, Any]] = []
    for case in cases:
        rows = by_case.get(case.case_id, [])
        best = max(rows, key=lambda item: _STATE_RANK[item.source_state])
        ready = [item.verification_id for item in rows if item.historical_replay_ready]
        blockers = [
            {
                "verification_id": item.verification_id,
                "blocker_code": item.blocker_code,
                "blocker_detail": item.blocker_detail,
            }
            for item in rows
            if item.blocker_code
        ]
        statuses.append(
            {
                "case_id": case.case_id,
                "canonical_archetype_id": case.canonical_archetype_id,
                "declared_source_quality": case.declared_source_quality,
                "best_source_state": best.source_state,
                "historical_replay_ready": bool(ready),
                "ready_verification_ids": ready,
                "exact_blockers": blockers,
                "current_score_eligible": False,
            }
        )
    return statuses


def _build_repair_tasks(
    case_statuses: Sequence[Mapping[str, Any]],
    verifications: Sequence[HistoricalSourceVerification],
) -> list[HistoricalSourceRepairTask]:
    verification_by_id = {item.verification_id: item for item in verifications}
    tasks: list[HistoricalSourceRepairTask] = []
    for status in case_statuses:
        if status["historical_replay_ready"]:
            continue
        blockers = list(status["exact_blockers"])
        if not blockers:
            continue
        blocker = blockers[0]
        verification = verification_by_id[blocker["verification_id"]]
        resolution = _required_resolution(str(blocker["blocker_code"]))
        tasks.append(
            HistoricalSourceRepairTask(
                repair_task_id=stable_intelligence_id(
                    "HSREPAIR",
                    {
                        "case_id": status["case_id"],
                        "blocker_code": blocker["blocker_code"],
                        "source_url": verification.source_url,
                    },
                ),
                case_id=str(status["case_id"]),
                source_state=str(status["best_source_state"]),
                source_url=verification.source_url,
                official_document_id=verification.official_document_id,
                blocker_code=str(blocker["blocker_code"]),
                blocker_detail=str(blocker["blocker_detail"] or ""),
                required_resolution=resolution,
            )
        )
    return tasks


def _build_source_verification_manifest(
    *,
    cases: Sequence[HistoricalResearchCase],
    snapshots: Sequence[HistoricalProviderSnapshot],
    links: Sequence[HistoricalCaseSourceLink],
    verifications: Sequence[HistoricalSourceVerification],
    repair_tasks: Sequence[HistoricalSourceRepairTask],
    case_statuses: Sequence[Mapping[str, Any]],
    url_backed_golden_case_ids: set[str],
    source_proxy_golden_case_ids: set[str],
) -> Mapping[str, Any]:
    case_by_id = {case.case_id: case for case in cases}
    status_by_case = {str(row["case_id"]): row for row in case_statuses}
    ready = [item for item in verifications if item.historical_replay_ready]
    critical = {
        "case_level_url_association_missing_a2": sum(
            not item.checks.get("case_level_source_association", False) for item in ready
        ),
        "url_string_only_a2": sum(item.snapshot_id is None for item in ready),
        "wrong_subject_replay_ready": sum(
            item.target_directness != "DIRECT" for item in ready
        ),
        "source_proxy_replay_ready": sum(
            case_by_id[item.case_id].declared_source_quality
            == HistoricalSourceState.SOURCE_PROXY_ONLY.value
            for item in ready
        ),
        "ready_missing_required_check": sum(
            not item.checks or not all(item.checks.values()) for item in ready
        ),
        "historical_current_score_leak": sum(
            item.current_score_eligible for item in verifications
        )
        + sum(task.current_score_eligible for task in repair_tasks),
        "url_backed_golden_without_ready_or_exact_blocker": sum(
            case_id not in status_by_case
            or not (
                status_by_case[case_id]["historical_replay_ready"]
                or status_by_case[case_id]["exact_blockers"]
            )
            for case_id in url_backed_golden_case_ids
        ),
        "source_proxy_not_planning_only": sum(
            case_id not in status_by_case
            or status_by_case[case_id]["historical_replay_ready"]
            or not any(task.case_id == case_id and task.planning_only for task in repair_tasks)
            for case_id in source_proxy_golden_case_ids
        ),
    }
    state_counts = Counter(item.source_state for item in verifications)
    return {
        "schema_version": "e2r_case_level_source_verification_manifest_v1",
        "status": (
            "CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_PASS"
            if cases and sum(critical.values()) == 0
            else "CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_FAIL"
        ),
        "case_count": len(cases),
        "snapshot_count": len(snapshots),
        "case_source_link_count": len(links),
        "verification_count": len(verifications),
        "historical_replay_ready_count": len(ready),
        "repair_task_count": len(repair_tasks),
        "source_state_counts": dict(sorted(state_counts.items())),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "verification_hash": stable_hash([item.to_dict() for item in verifications]),
        "historical_outcome_or_current_score_payload_allowed": False,
    }


def _snapshot_reference_index(
    snapshots: Sequence[HistoricalProviderSnapshot],
) -> Mapping[tuple[str, str], tuple[HistoricalProviderSnapshot, ...]]:
    index: dict[tuple[str, str], list[HistoricalProviderSnapshot]] = {}
    for snapshot in snapshots:
        if snapshot.canonical_url:
            index.setdefault(("url", _normalize_url(snapshot.canonical_url)), []).append(snapshot)
        if snapshot.official_document_id:
            index.setdefault(("document_id", snapshot.official_document_id.strip()), []).append(snapshot)
    return {key: tuple(value) for key, value in index.items()}


def _matching_snapshots(
    reference: HistoricalEvidenceReference,
    index: Mapping[tuple[str, str], tuple[HistoricalProviderSnapshot, ...]],
) -> tuple[HistoricalProviderSnapshot, ...]:
    matches: dict[str, HistoricalProviderSnapshot] = {}
    if reference.url:
        for snapshot in index.get(("url", _normalize_url(reference.url)), ()):
            matches[snapshot.snapshot_id] = snapshot
    if reference.document_id:
        for snapshot in index.get(("document_id", reference.document_id.strip()), ()):
            matches[snapshot.snapshot_id] = snapshot
    return tuple(matches[key] for key in sorted(matches))


def _reference_matches_snapshot(
    reference: HistoricalEvidenceReference,
    snapshot: HistoricalProviderSnapshot,
) -> bool:
    return bool(
        reference.url
        and snapshot.canonical_url
        and _normalize_url(reference.url) == _normalize_url(snapshot.canonical_url)
    ) or bool(
        reference.document_id
        and snapshot.official_document_id
        and reference.document_id.strip() == snapshot.official_document_id.strip()
    )


def _target_is_direct(
    case: HistoricalResearchCase,
    snapshot: HistoricalProviderSnapshot,
    content: str,
) -> bool:
    case_symbol = _identity_text(case.symbol)
    snapshot_symbols = {_identity_text(item) for item in snapshot.subject_symbols}
    symbol_match = bool(case_symbol and case_symbol in snapshot_symbols)
    case_name = _identity_text(case.company_name)
    snapshot_names = {_identity_text(item) for item in snapshot.subject_names}
    name_match = bool(case_name and case_name in snapshot_names)
    normalized_content = _identity_text(content)
    content_match = bool(
        case_name and case_name in normalized_content
    ) or any(name and name in normalized_content for name in snapshot_names)
    return bool((symbol_match or name_match) and content_match)


def _select_verified_link(
    links: Sequence[HistoricalCaseSourceLink],
) -> HistoricalCaseSourceLink | None:
    verified = sorted(
        (link for link in links if link.verified),
        key=lambda item: item.link_id,
    )
    if len(verified) == 1:
        return verified[0]
    return None


def _link_provenance_valid(link: HistoricalCaseSourceLink) -> bool:
    return bool(
        link.verifier_origin
        and _SHA256_RE.fullmatch(link.verifier_prompt_hash)
        and _SHA256_RE.fullmatch(link.verifier_response_hash)
    )


def _resolve_content_path(value: str | None, repo_root: Path) -> Path | None:
    if not value:
        return None
    path = Path(value)
    resolved = (path if path.is_absolute() else repo_root / path).resolve()
    try:
        resolved.relative_to(repo_root)
    except ValueError:
        return None
    return resolved


def _blank_checks() -> dict[str, bool]:
    return {
        "url_or_official_document": False,
        "case_level_source_association": False,
        "fetch_or_valid_snapshot": False,
        "content_hash_verified": False,
        "published_date_present": False,
        "historical_as_of_present": False,
        "published_on_or_before_as_of": False,
        "available_on_or_before_as_of": False,
        "target_direct": False,
        "exact_anchor_verified": False,
        "link_verification_provenance": False,
        "case_semantic_match": False,
        "summary_consistent": False,
        "provider_snapshot_valid": False,
        "historical_current_separation": False,
    }


def _required_resolution(blocker_code: str) -> tuple[str, ...]:
    mapping = {
        "SOURCE_PROXY_REQUIRES_CASE_LEVEL_SOURCE": (
            "attach a case-level URL or official document id",
            "fetch and hash the source",
            "verify direct target and exact anchor",
        ),
        "CASE_LEVEL_SOURCE_ASSOCIATION_MISSING": (
            "attach a case-level URL or official document id",
        ),
        "EVIDENCE_URL_REPAIR_REQUIRED": (
            "repair the missing evidence URL using historical as-of constraints",
        ),
        "PROVIDER_SNAPSHOT_NOT_FOUND": (
            "fetch the URL or register a valid provider snapshot with content SHA-256",
        ),
        "SNAPSHOT_FETCH_FAILED": ("retry or replace the failed historical source fetch",),
        "SNAPSHOT_CONTENT_MISSING": ("restore the provider snapshot content",),
        "SNAPSHOT_CONTENT_EMPTY": ("replace the empty provider snapshot",),
        "CONTENT_HASH_MISMATCH": ("recompute provenance or restore the exact captured content",),
        "HISTORICAL_DATE_OR_AVAILABILITY_INVALID": (
            "verify published/available dates on or before the case as-of date",
        ),
        "TARGET_DIRECTNESS_FAILED": ("find a source directly about the case target",),
        "EXACT_ANCHOR_MISSING_OR_INVALID": (
            "record an exact quote/table/API locator that exists in the snapshot",
        ),
        "CASE_SEMANTIC_LINK_MISSING": (
            "adjudicate the anchor against the historical case meaning",
        ),
        "CASE_SEMANTIC_MATCH_FAILED": (
            "replace or re-adjudicate the unrelated case/source link",
        ),
        "CASE_SUMMARY_SOURCE_CONTRADICTION": (
            "resolve the contradiction between research summary and source",
        ),
        "PROVIDER_SNAPSHOT_NOT_VALID": (
            "supply valid provider/archive provenance for the fetched content",
        ),
        "HISTORICAL_CURRENT_EVIDENCE_BOUNDARY_FAILED": (
            "remove historical replay material from current scoring",
        ),
    }
    return mapping.get(blocker_code, ("review and repair the exact source verification blocker",))


def _load_jsonl(path: str | Path) -> list[Mapping[str, Any]]:
    source = Path(path)
    rows: list[Mapping[str, Any]] = []
    for line_number, line in enumerate(
        source.read_text(encoding="utf-8", errors="strict").splitlines(),
        start=1,
    ):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"malformed JSONL {source}:{line_number}: {exc}") from exc
        if not isinstance(row, Mapping):
            raise ValueError(f"JSONL row must be an object: {source}:{line_number}")
        rows.append(row)
    return rows


def _normalize_url(value: str) -> str:
    stripped = value.strip().rstrip("`.,;")
    parsed = urlsplit(stripped)
    path = parsed.path.rstrip("/") or "/"
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, ""))


def _identity_text(value: Any) -> str:
    return re.sub(r"[^0-9A-Za-z가-힣]", "", str(value or "")).lower()


def _parse_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value)) if value else None
    except ValueError:
        return None


def _parse_datetime(value: Any) -> datetime | None:
    try:
        return datetime.fromisoformat(str(value)) if value else None
    except ValueError:
        return None


def _optional_text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _bool_value(value: Any, *, field: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in {0, 1}:
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1", "yes"}:
            return True
        if normalized in {"false", "0", "no"}:
            return False
    raise ValueError(f"{field} must be an explicit boolean")


__all__ = [
    "SourceVerificationCompilationResult",
    "compile_case_level_source_verification",
    "load_historical_case_source_links",
    "load_historical_provider_snapshots",
    "render_source_verification_report",
    "write_case_level_source_verification",
]
