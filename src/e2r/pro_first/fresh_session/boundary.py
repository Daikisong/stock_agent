"""Fresh-session identity and answer-leakage boundaries for Pro V2.1."""

from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import ProResearchJob, ResearchMode, ScanWindow


class FreshSessionBoundaryError(RuntimeError):
    """A fresh run attempted to reuse an old identity or answer."""


class FreshSessionRerunRequired(FreshSessionBoundaryError):
    """The current fresh conversation is diagnostic-only; start another one."""


FROZEN_PREDECESSOR_BOUNDARY = "FROZEN_PREDECESSOR"
INDEPENDENT_CANARY_BOUNDARY = "INDEPENDENT_CROSS_ARCHETYPE_CANARY"


@dataclass(frozen=True)
class OldAnswerLeakageManifest:
    """Exact old-run values that may never become fresh research answers.

    Target metadata and ``as_of_date`` are intentionally absent because the
    fresh canary must preserve them.  This manifest contains only answer-
    bearing identities and values discovered by the diagnostic run.
    """

    old_job_id: str
    old_run_id: str
    old_conversation_id: str
    old_fact_ids: tuple[str, ...] = ()
    old_route_receipt_ids: tuple[str, ...] = ()
    old_research_pass_ids: tuple[str, ...] = ()
    old_question_answers: tuple[str, ...] = ()
    old_score_values: tuple[str, ...] = ()
    old_stage_values: tuple[str, ...] = ()
    expected_source_urls: tuple[str, ...] = ()
    expected_fact_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for value, label in (
            (self.old_job_id, "old_job_id"),
            (self.old_run_id, "old_run_id"),
            (self.old_conversation_id, "old_conversation_id"),
        ):
            if not value.strip():
                raise ValueError(f"{label} is required")
        for name in (
            "old_fact_ids",
            "old_route_receipt_ids",
            "old_research_pass_ids",
            "old_question_answers",
            "old_score_values",
            "old_stage_values",
            "expected_source_urls",
            "expected_fact_ids",
        ):
            values = tuple(str(value).strip() for value in getattr(self, name))
            if any(not value for value in values):
                raise ValueError(f"{name} contains an empty leakage token")
            if len(values) != len(set(values)):
                raise ValueError(f"{name} contains duplicate leakage tokens")
            object.__setattr__(self, name, values)


@dataclass(frozen=True)
class FreshBlindLeakageAudit:
    schema_version: str
    packet_hash: str
    old_identity_input_count: int
    old_pro_fact_input_count: int
    old_route_receipt_input_count: int
    old_question_answer_input_count: int
    old_score_stage_input_count: int
    expected_source_input_count: int
    expected_fact_id_input_count: int
    forbidden_answer_field_count: int
    offending_paths: tuple[str, ...]
    score_authority: bool = False
    stage_authority: bool = False

    @property
    def leakage_count(self) -> int:
        return sum(
            (
                self.old_identity_input_count,
                self.old_pro_fact_input_count,
                self.old_route_receipt_input_count,
                self.old_question_answer_input_count,
                self.old_score_stage_input_count,
                self.expected_source_input_count,
                self.expected_fact_id_input_count,
                self.forbidden_answer_field_count,
            )
        )

    @property
    def passed(self) -> bool:
        return self.leakage_count == 0

    def to_dict(self) -> Mapping[str, Any]:
        unsigned = {
            "schema_version": self.schema_version,
            "status": "PASS" if self.passed else "FAIL",
            "packet_hash": self.packet_hash,
            "old_identity_input_count": self.old_identity_input_count,
            "old_pro_fact_input_count": self.old_pro_fact_input_count,
            "old_route_receipt_input_count": self.old_route_receipt_input_count,
            "old_question_answer_input_count": (
                self.old_question_answer_input_count
            ),
            "old_score_stage_input_count": self.old_score_stage_input_count,
            "expected_source_input_count": self.expected_source_input_count,
            "expected_fact_id_input_count": self.expected_fact_id_input_count,
            "forbidden_answer_field_count": self.forbidden_answer_field_count,
            "leakage_count": self.leakage_count,
            "offending_paths": list(self.offending_paths),
            "score_authority": self.score_authority,
            "stage_authority": self.stage_authority,
        }
        return {**unsigned, "receipt_hash": canonical_hash(unsigned)}


@dataclass(frozen=True)
class FreshSessionBoundary:
    fresh_session_id: str
    old_job_id: str
    old_run_id: str
    old_conversation_id: str
    fresh_job_id: str
    old_runtime_root: Path
    fresh_runtime_root: Path
    leakage_manifest: OldAnswerLeakageManifest
    boundary_receipt_path: Path
    predecessor_required: bool = True

    @property
    def fresh_job_root(self) -> Path:
        return self.fresh_runtime_root / "jobs" / self.fresh_job_id


class FreshSessionBoundaryService:
    """Create one new job/runtime identity linked to one frozen old job."""

    def __init__(self, store: ProFirstJobStore) -> None:
        self.store = store

    def start(
        self,
        *,
        old_job_id: str,
        old_run_id: str,
        old_conversation_id: str,
        fresh_session_id: str,
        old_runtime_root: str | Path,
        fresh_runtime_root: str | Path,
        archetype_ids: Sequence[str],
        leakage_manifest: OldAnswerLeakageManifest | None = None,
    ) -> tuple[FreshSessionBoundary, ProResearchJob]:
        old = self.store.get_job(old_job_id)
        if old.old_job_frozen_at is None:
            raise FreshSessionBoundaryError(
                "old diagnostic job must be frozen before a fresh run starts"
            )
        if old.conversation_id and old.conversation_id != old_conversation_id:
            raise FreshSessionBoundaryError(
                "declared old conversation differs from the durable old job"
            )
        if not fresh_session_id.strip():
            raise ValueError("fresh_session_id is required")
        primary_ids = tuple(dict.fromkeys(str(value) for value in archetype_ids))
        if not 1 <= len(primary_ids) <= 3:
            raise ValueError("fresh canary requires one to three primary contracts")

        manifest = leakage_manifest or OldAnswerLeakageManifest(
            old_job_id=old_job_id,
            old_run_id=old_run_id,
            old_conversation_id=old_conversation_id,
        )
        if (
            manifest.old_job_id != old_job_id
            or manifest.old_run_id != old_run_id
            or manifest.old_conversation_id != old_conversation_id
        ):
            raise FreshSessionBoundaryError(
                "leakage manifest is bound to a different old run"
            )

        old_root = Path(old_runtime_root).expanduser().resolve()
        fresh_root = Path(fresh_runtime_root).expanduser().resolve()
        _assert_disjoint_runtime_roots(old_root, fresh_root)
        boundary_path = fresh_root / "fresh_session_boundary_receipt.json"
        _prepare_new_runtime_root(
            fresh_root,
            boundary_path=boundary_path,
            fresh_session_id=fresh_session_id,
            old_job_id=old_job_id,
        )

        trigger = canonical_hash(
            {
                "selection_mode": ResearchMode.FORCED_VALIDATION_CANARY.value,
                "symbol": old.symbol,
                "as_of_date": old.as_of_date,
                "fresh_session_id": fresh_session_id,
                "packet_contract": "e2r_pro_research_packet_v3",
            }
        )
        candidate = self.store.create_candidate(
            symbol=old.symbol,
            company_name=old.company_name,
            as_of_date=old.as_of_date,
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint=trigger,
            research_mode=ResearchMode.FORCED_VALIDATION_CANARY,
            selection_receipt={
                "schema_version": "e2r_pro_fresh_canary_selection_v1",
                "selection_mode": "FRESH_BLIND_FORCED_VALIDATION_CANARY",
                "fresh_session_id": fresh_session_id,
                "production_candidate": False,
                "test_injected": False,
                "final_score_visible_at_selection": False,
                "final_stage_visible_at_selection": False,
                "trigger_ids": [
                    stable_id(
                        "FRESHTRIGGER",
                        {
                            "fresh_session_id": fresh_session_id,
                            "symbol": old.symbol,
                            "as_of_date": old.as_of_date,
                        },
                    )
                ],
                "reason_codes": [
                    "EXPLICIT_USER_AUTHORIZED_FRESH_BLIND_VALIDATION"
                ],
                "old_answer_inputs_allowed": False,
            },
        )
        fresh = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=primary_ids,
            actor="v2.1-fresh-session-boundary",
        )
        if fresh.job_id == old.job_id:
            raise FreshSessionBoundaryError("fresh job reused the old job identity")
        old = self.store.bind_superseding_fresh_job(
            old.job_id,
            fresh.job_id,
            expected_version=old.state_version,
            actor="v2.1-fresh-session-boundary",
            idempotency_key=f"fresh-successor:{old.job_id}:{fresh.job_id}",
        )
        if old.superseded_by_fresh_job_id != fresh.job_id:
            raise FreshSessionBoundaryError("old job was not bound to the fresh successor")

        receipt = {
            "schema_version": "e2r_pro_fresh_session_boundary_receipt_v1",
            "status": "FRESH_SESSION_BOUNDARY_ESTABLISHED",
            "boundary_mode": FROZEN_PREDECESSOR_BOUNDARY,
            "predecessor_required": True,
            "fresh_session_id": fresh_session_id,
            "old_job_id": old_job_id,
            "old_run_id": old_run_id,
            "old_conversation_id": old_conversation_id,
            "fresh_job_id": fresh.job_id,
            "old_runtime_root": str(old_root),
            "fresh_runtime_root": str(fresh_root),
            "new_runtime_root": old_root != fresh_root,
            "new_job_id": fresh.job_id != old_job_id,
            "old_job_frozen": True,
            "old_conversation_followup_allowed": False,
            "fresh_packet_old_answer_allowed": False,
            "score_authority": False,
            "stage_authority": False,
        }
        receipt = {**receipt, "receipt_hash": canonical_hash(receipt)}
        _write_json_once(boundary_path, receipt)
        boundary = FreshSessionBoundary(
            fresh_session_id=fresh_session_id,
            old_job_id=old_job_id,
            old_run_id=old_run_id,
            old_conversation_id=old_conversation_id,
            fresh_job_id=fresh.job_id,
            old_runtime_root=old_root,
            fresh_runtime_root=fresh_root,
            leakage_manifest=manifest,
            boundary_receipt_path=boundary_path,
            predecessor_required=True,
        )
        return boundary, fresh

    def start_independent(
        self,
        *,
        symbol: str,
        company_name: str,
        as_of_date: str,
        fresh_session_id: str,
        reference_runtime_root: str | Path,
        fresh_runtime_root: str | Path,
        archetype_ids: Sequence[str],
        leakage_manifest: OldAnswerLeakageManifest | None = None,
    ) -> tuple[FreshSessionBoundary, ProResearchJob]:
        """Start a cross-archetype canary with no fabricated predecessor run.

        C06 has a real repair-heavy predecessor whose answers must be denied.
        C17/C28 do not.  This path creates the fresh job directly and uses a
        deterministic empty-answer manifest, rather than manufacturing a fake
        frozen job or borrowing C06's target identity.
        """

        target = {
            "fresh_session_id": fresh_session_id.strip(),
            "symbol": symbol.strip(),
            "company_name": company_name.strip(),
            "as_of_date": as_of_date.strip(),
        }
        if any(not value for value in target.values()):
            raise ValueError("independent fresh canary target fields are required")
        primary_ids = tuple(
            dict.fromkeys(str(value).strip() for value in archetype_ids)
        )
        if not 1 <= len(primary_ids) <= 3 or any(not value for value in primary_ids):
            raise ValueError("fresh canary requires one to three primary contracts")

        manifest = leakage_manifest or build_independent_leakage_manifest(
            fresh_session_id=target["fresh_session_id"],
            symbol=target["symbol"],
            as_of_date=target["as_of_date"],
        )
        expected_manifest = build_independent_leakage_manifest(
            fresh_session_id=target["fresh_session_id"],
            symbol=target["symbol"],
            as_of_date=target["as_of_date"],
        )
        if manifest != expected_manifest:
            raise FreshSessionBoundaryError(
                "independent canary leakage manifest differs from its target identity"
            )

        reference_root = Path(reference_runtime_root).expanduser().resolve()
        fresh_root = Path(fresh_runtime_root).expanduser().resolve()
        _assert_disjoint_runtime_roots(reference_root, fresh_root)
        boundary_path = fresh_root / "fresh_session_boundary_receipt.json"
        _prepare_new_runtime_root(
            fresh_root,
            boundary_path=boundary_path,
            fresh_session_id=target["fresh_session_id"],
            old_job_id=manifest.old_job_id,
        )

        trigger = canonical_hash(
            {
                "selection_mode": ResearchMode.FORCED_VALIDATION_CANARY.value,
                "boundary_mode": INDEPENDENT_CANARY_BOUNDARY,
                "symbol": target["symbol"],
                "as_of_date": target["as_of_date"],
                "fresh_session_id": target["fresh_session_id"],
                "packet_contract": "e2r_pro_research_packet_v3",
            }
        )
        candidate = self.store.create_candidate(
            symbol=target["symbol"],
            company_name=target["company_name"],
            as_of_date=target["as_of_date"],
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint=trigger,
            research_mode=ResearchMode.FORCED_VALIDATION_CANARY,
            selection_receipt={
                "schema_version": "e2r_pro_independent_fresh_canary_selection_v1",
                "selection_mode": "INDEPENDENT_FRESH_BLIND_FORCED_VALIDATION_CANARY",
                "boundary_mode": INDEPENDENT_CANARY_BOUNDARY,
                "fresh_session_id": target["fresh_session_id"],
                "production_candidate": False,
                "test_injected": False,
                "predecessor_required": False,
                "final_score_visible_at_selection": False,
                "final_stage_visible_at_selection": False,
                "trigger_ids": [
                    stable_id(
                        "FRESHTRIGGER",
                        {
                            "fresh_session_id": target["fresh_session_id"],
                            "symbol": target["symbol"],
                            "as_of_date": target["as_of_date"],
                        },
                    )
                ],
                "reason_codes": [
                    "EXPLICIT_USER_AUTHORIZED_CROSS_ARCHETYPE_FRESH_BLIND_VALIDATION"
                ],
                "old_answer_inputs_allowed": False,
            },
        )
        fresh = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=primary_ids,
            actor="v2.1-independent-fresh-session-boundary",
        )
        receipt = {
            "schema_version": "e2r_pro_fresh_session_boundary_receipt_v1",
            "status": "FRESH_SESSION_BOUNDARY_ESTABLISHED",
            "boundary_mode": INDEPENDENT_CANARY_BOUNDARY,
            "predecessor_required": False,
            "fresh_session_id": target["fresh_session_id"],
            "old_job_id": manifest.old_job_id,
            "old_run_id": manifest.old_run_id,
            "old_conversation_id": manifest.old_conversation_id,
            "fresh_job_id": fresh.job_id,
            "old_runtime_root": str(reference_root),
            "fresh_runtime_root": str(fresh_root),
            "target": {
                "symbol": fresh.symbol,
                "company_name": fresh.company_name,
                "as_of_date": fresh.as_of_date,
                "archetype_ids": list(fresh.archetype_ids),
            },
            "new_runtime_root": reference_root != fresh_root,
            "new_job_id": True,
            "old_job_frozen": None,
            "old_conversation_followup_allowed": False,
            "fresh_packet_old_answer_allowed": False,
            "score_authority": False,
            "stage_authority": False,
        }
        receipt = {**receipt, "receipt_hash": canonical_hash(receipt)}
        _write_json_once(boundary_path, receipt)
        return (
            FreshSessionBoundary(
                fresh_session_id=target["fresh_session_id"],
                old_job_id=manifest.old_job_id,
                old_run_id=manifest.old_run_id,
                old_conversation_id=manifest.old_conversation_id,
                fresh_job_id=fresh.job_id,
                old_runtime_root=reference_root,
                fresh_runtime_root=fresh_root,
                leakage_manifest=manifest,
                boundary_receipt_path=boundary_path,
                predecessor_required=False,
            ),
            fresh,
        )

    def load_existing(
        self,
        *,
        fresh_runtime_root: str | Path,
        leakage_manifest: OldAnswerLeakageManifest,
    ) -> tuple[FreshSessionBoundary, ProResearchJob]:
        """Load one immutable boundary without creating another successor."""

        fresh_root = Path(fresh_runtime_root).expanduser().resolve()
        boundary_path = fresh_root / "fresh_session_boundary_receipt.json"
        if not boundary_path.is_file():
            raise FreshSessionBoundaryError("fresh boundary receipt is missing")
        receipt = json.loads(boundary_path.read_text(encoding="utf-8"))
        unsigned = {key: value for key, value in receipt.items() if key != "receipt_hash"}
        if (
            receipt.get("schema_version")
            != "e2r_pro_fresh_session_boundary_receipt_v1"
            or receipt.get("receipt_hash") != canonical_hash(unsigned)
            or receipt.get("fresh_runtime_root") != str(fresh_root)
        ):
            raise FreshSessionBoundaryError("fresh boundary receipt failed hash/path validation")
        for field in ("old_job_id", "old_run_id", "old_conversation_id"):
            if receipt.get(field) != getattr(leakage_manifest, field):
                raise FreshSessionBoundaryError(
                    "fresh boundary differs from the old-answer leakage manifest"
                )
        boundary_mode = str(
            receipt.get("boundary_mode") or FROZEN_PREDECESSOR_BOUNDARY
        )
        predecessor_required = boundary_mode != INDEPENDENT_CANARY_BOUNDARY
        fresh_job_id = str(receipt.get("fresh_job_id") or "")
        fresh = self.store.get_job(fresh_job_id)
        if predecessor_required:
            old = self.store.get_job(leakage_manifest.old_job_id)
            if (
                old.superseded_by_fresh_job_id != fresh_job_id
                or fresh.job_id == old.job_id
                or fresh.old_job_frozen_at is not None
            ):
                raise FreshSessionBoundaryError(
                    "durable old/fresh successor binding is not recoverable"
                )
        else:
            target = receipt.get("target") or {}
            if (
                receipt.get("predecessor_required") is not False
                or fresh.old_job_frozen_at is not None
                or target.get("symbol") != fresh.symbol
                or target.get("company_name") != fresh.company_name
                or target.get("as_of_date") != fresh.as_of_date
                or tuple(target.get("archetype_ids") or ()) != fresh.archetype_ids
            ):
                raise FreshSessionBoundaryError(
                    "independent fresh boundary target/state is not recoverable"
                )
        old_root = Path(str(receipt.get("old_runtime_root") or "")).resolve()
        _assert_disjoint_runtime_roots(old_root, fresh_root)
        return (
            FreshSessionBoundary(
                fresh_session_id=str(receipt["fresh_session_id"]),
                old_job_id=leakage_manifest.old_job_id,
                old_run_id=leakage_manifest.old_run_id,
                old_conversation_id=leakage_manifest.old_conversation_id,
                fresh_job_id=fresh_job_id,
                old_runtime_root=old_root,
                fresh_runtime_root=fresh_root,
                leakage_manifest=leakage_manifest,
                boundary_receipt_path=boundary_path,
                predecessor_required=predecessor_required,
            ),
            fresh,
        )


def build_independent_leakage_manifest(
    *,
    fresh_session_id: str,
    symbol: str,
    as_of_date: str,
) -> OldAnswerLeakageManifest:
    """Return deterministic deny sentinels for a canary with no predecessor."""

    identity = {
        "fresh_session_id": fresh_session_id.strip(),
        "symbol": symbol.strip(),
        "as_of_date": as_of_date.strip(),
    }
    if any(not value for value in identity.values()):
        raise ValueError("independent leakage manifest identity is incomplete")
    return OldAnswerLeakageManifest(
        old_job_id=stable_id("NOPREDECESSORJOB", identity),
        old_run_id=stable_id("NOPREDECESSORRUN", identity),
        old_conversation_id=stable_id("NOPREDECESSORCONVERSATION", identity),
    )


def audit_fresh_blind_payload(
    payload: Mapping[str, Any],
    manifest: OldAnswerLeakageManifest,
) -> FreshBlindLeakageAudit:
    """Count exact old-answer leakage and fail closed at the caller."""

    counts = {
        "old_identity_input_count": 0,
        "old_pro_fact_input_count": 0,
        "old_route_receipt_input_count": 0,
        "old_question_answer_input_count": 0,
        "old_score_stage_input_count": 0,
        "expected_source_input_count": 0,
        "expected_fact_id_input_count": 0,
        "forbidden_answer_field_count": 0,
    }
    paths: list[str] = []
    old_identities = {
        manifest.old_job_id,
        manifest.old_run_id,
        manifest.old_conversation_id,
        *manifest.old_research_pass_ids,
    }
    old_facts = set(manifest.old_fact_ids)
    old_routes = set(manifest.old_route_receipt_ids)
    old_answers = set(manifest.old_question_answers)
    old_scores = set(manifest.old_score_values)
    old_stages = set(manifest.old_stage_values)
    expected_sources = set(manifest.expected_source_urls)
    expected_facts = set(manifest.expected_fact_ids)
    forbidden_fields = {
        "existing_thesis_digest",
        "historical_anchor_digest",
        "known_positive_facts",
        "known_counterfacts",
        "old_pro_accepted_facts",
        "old_pro_route_receipts",
        "old_pro_verifier_rejection_roster",
        "old_pro_question_terminal_answers",
        "verification_repair_register",
        "proposed_score_ranges",
        "gate1_score",
        "gate_1_score",
        "old_v2_prospective_score",
        "expected_source_urls",
        "expected_fact_ids",
    }

    def visit(value: Any, path: tuple[str, ...] = ()) -> None:
        if path and path[0] == "dossier_output_schema":
            # The embedded canonical JSON Schema contains property names such
            # as score_authority for validation purposes.  It is code-owned
            # contract metadata, not prior-run answer input, and is separately
            # protected by its canonical schema hash.
            return
        if isinstance(value, Mapping):
            for key, child in value.items():
                normalized = str(key).strip().casefold().replace("-", "_")
                next_path = (*path, str(key))
                path_text = "/".join(next_path)
                if normalized in forbidden_fields:
                    counts["forbidden_answer_field_count"] += 1
                    paths.append(path_text)
                if normalized in {"score", "stage", "final_score", "final_stage"}:
                    counts["old_score_stage_input_count"] += 1
                    paths.append(path_text)
                if normalized in {"score_authority", "stage_authority"}:
                    if child is not False:
                        counts["old_score_stage_input_count"] += 1
                        paths.append(path_text)
                    continue
                visit(child, next_path)
        elif isinstance(value, Sequence) and not isinstance(
            value, (str, bytes, bytearray)
        ):
            for index, child in enumerate(value):
                visit(child, (*path, str(index)))
        elif isinstance(value, (str, int, float)) and not isinstance(value, bool):
            token = str(value).strip()
            path_text = "/".join(path)
            field = next(
                (
                    item.strip().casefold().replace("-", "_")
                    for item in reversed(path)
                    if not item.isdigit()
                ),
                "",
            )
            if token in old_identities:
                counts["old_identity_input_count"] += 1
                paths.append(path_text)
            if token in old_facts:
                counts["old_pro_fact_input_count"] += 1
                paths.append(path_text)
            if token in old_routes:
                counts["old_route_receipt_input_count"] += 1
                paths.append(path_text)
            if token in old_answers:
                counts["old_question_answer_input_count"] += 1
                paths.append(path_text)
            if (
                ("score" in field and token in old_scores)
                or ("stage" in field and token in old_stages)
            ):
                counts["old_score_stage_input_count"] += 1
                paths.append(path_text)
            if token in expected_sources:
                counts["expected_source_input_count"] += 1
                paths.append(path_text)
            if token in expected_facts:
                counts["expected_fact_id_input_count"] += 1
                paths.append(path_text)

    visit(payload)
    return FreshBlindLeakageAudit(
        schema_version="e2r_pro_fresh_blind_packet_audit_v1",
        packet_hash=canonical_hash(payload),
        offending_paths=tuple(sorted(set(paths))),
        **counts,
    )


def assert_fresh_prompt_has_no_old_answers(
    prompt_text: str,
    manifest: OldAnswerLeakageManifest,
) -> Mapping[str, Any]:
    forbidden_tokens = tuple(
        value
        for value in (
            manifest.old_job_id,
            manifest.old_run_id,
            manifest.old_conversation_id,
            *manifest.old_fact_ids,
            *manifest.old_route_receipt_ids,
            *manifest.old_research_pass_ids,
            *manifest.old_question_answers,
            *manifest.old_score_values,
            *manifest.old_stage_values,
            *manifest.expected_source_urls,
            *manifest.expected_fact_ids,
        )
        if value
    )
    matched = sorted({token for token in forbidden_tokens if token in prompt_text})
    forbidden_field_tokens = sorted(
        token
        for token in (
            "known_positive_facts",
            "known_counterfacts",
            "old_pro_accepted_facts",
            "old_pro_route_receipts",
            "old_pro_question_terminal_answers",
            "verification_repair_register",
            "proposed_score_ranges",
            "expected_source_urls",
            "expected_fact_ids",
        )
        if token in prompt_text
    )
    unsigned = {
        "schema_version": "e2r_pro_fresh_initial_prompt_leakage_audit_v1",
        "status": "PASS" if not matched and not forbidden_field_tokens else "FAIL",
        "prompt_hash": canonical_hash({"prompt": prompt_text}),
        "old_answer_token_count": len(matched),
        "forbidden_answer_field_token_count": len(forbidden_field_tokens),
        "matched_token_hashes": [canonical_hash({"token": value}) for value in matched],
        "forbidden_field_tokens": forbidden_field_tokens,
        "score_authority": False,
        "stage_authority": False,
    }
    receipt = {**unsigned, "receipt_hash": canonical_hash(unsigned)}
    if matched or forbidden_field_tokens:
        raise FreshSessionBoundaryError(
            "fresh Initial Prompt V3 contains old answer-bearing content"
        )
    return receipt


def _assert_disjoint_runtime_roots(old_root: Path, fresh_root: Path) -> None:
    if old_root == fresh_root:
        raise FreshSessionBoundaryError("fresh runtime root reused the old runtime root")
    if _is_relative_to(fresh_root, old_root) or _is_relative_to(old_root, fresh_root):
        raise FreshSessionBoundaryError(
            "old and fresh runtime roots must be disjoint, not nested"
        )


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _prepare_new_runtime_root(
    root: Path,
    *,
    boundary_path: Path,
    fresh_session_id: str,
    old_job_id: str,
) -> None:
    if root.exists():
        entries = tuple(root.iterdir())
        if entries:
            if not boundary_path.is_file():
                raise FreshSessionBoundaryError(
                    "fresh runtime root is not empty and has no matching boundary receipt"
                )
            existing = json.loads(boundary_path.read_text(encoding="utf-8"))
            if (
                existing.get("fresh_session_id") != fresh_session_id
                or existing.get("old_job_id") != old_job_id
            ):
                raise FreshSessionBoundaryError(
                    "fresh runtime root belongs to a different session"
                )
            return
    root.mkdir(parents=True, exist_ok=True)


def write_runtime_json_once(path: str | Path, payload: Mapping[str, Any]) -> Path:
    destination = Path(path)
    _write_json_once(destination, payload)
    return destination


def _write_json_once(path: Path, payload: Mapping[str, Any]) -> None:
    if path.is_file():
        existing = json.loads(path.read_text(encoding="utf-8"))
        if existing != payload:
            raise FreshSessionBoundaryError(
                f"immutable fresh-session receipt already differs: {path.name}"
            )
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(canonical_json(payload) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        fsync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


__all__ = [
    "FROZEN_PREDECESSOR_BOUNDARY",
    "INDEPENDENT_CANARY_BOUNDARY",
    "FreshBlindLeakageAudit",
    "FreshSessionBoundary",
    "FreshSessionBoundaryError",
    "FreshSessionBoundaryService",
    "FreshSessionRerunRequired",
    "OldAnswerLeakageManifest",
    "assert_fresh_prompt_has_no_old_answers",
    "audit_fresh_blind_payload",
    "build_independent_leakage_manifest",
    "write_runtime_json_once",
]
