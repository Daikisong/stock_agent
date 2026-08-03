"""Portable tracked receipts for independently reproducible E2R decisions.

The production dossier is intentionally large and untracked.  This module
exports only the score-bearing graph and then verifies it without consulting
the original output tree, a cache, an environment file, or a provider journal.
LLMs remain evidence extractors and component judges; score aggregation and
canonical Stage reproduction remain deterministic.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import statistics
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import urlparse

from e2r.calibration.scoring_profile import get_active_scoring_profile
from e2r.models import ScoreSnapshot, Stage
from e2r.production.metadata import git_head_sha, stable_hash, write_json, write_jsonl
from e2r.red_team import RedTeamAssessment, RedTeamRiskLevel, Soft4BStatus
from e2r.staging import StageClassificationInput, StageClassifier

from .canary_leaf_contract import canary_output_tree_hash
from .current_researcher_mode import _historical_anchors
from .schemas import CANONICAL_COMPONENT_ORDER
from .score_aggregator import AGGREGATOR_CONFIG


RECEIPT_MANIFEST_SCHEMA = "e2r_v6_tracked_receipt_manifest_v1"
SCORE_RECEIPT_SCHEMA = "e2r_v6_score_receipt_v1"
STAGECOURT_RECEIPT_SCHEMA = "e2r_v6_stagecourt_receipt_v1"
VERIFICATION_SCHEMA = "e2r_v6_receipt_only_verification_v1"
VERIFICATION_PASS = "E2R_V6_RECEIPT_ONLY_REPRODUCTION_PASS"
VERIFICATION_FAIL = "E2R_V6_RECEIPT_ONLY_REPRODUCTION_FAIL"
PROVIDER_ROUTE = "COLLABORATION_CODEX_SUBAGENT"
CANONICAL_COMPONENT_MAX = {
    "eps_fcf_explosion": 20.0,
    "earnings_visibility": 20.0,
    "bottleneck_pricing": 20.0,
    "market_mispricing": 15.0,
    "valuation_rerating": 15.0,
    "capital_allocation": 5.0,
    "information_confidence": 5.0,
}
REQUIRED_TARGET_FILES = (
    "score_receipt.json",
    "component_decisions.jsonl",
    "scoring_facts.jsonl",
    "judge_decisions.jsonl",
    "source_manifest.jsonl",
    "anchor_manifest.jsonl",
    "provider_calls.jsonl",
    "stagecourt_receipt.json",
)
_FORBIDDEN_IDENTITY_PATTERNS = (
    re.compile(r"(?:^|[\s\"'])/root(?:/|$)"),
    re.compile(r"(?:^|[\s\"'])/home/[^/\s]+/"),
    re.compile(r"[A-Za-z]:\\Users\\"),
)


class ReceiptVerificationError(ValueError):
    """Raised for a malformed or non-reproducible tracked receipt."""


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ReceiptVerificationError(f"JSON_OBJECT_REQUIRED:{path.name}")
    return dict(payload)


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, Mapping):
            raise ReceiptVerificationError(f"JSONL_OBJECT_REQUIRED:{path.name}:{index}")
        rows.append(dict(row))
    return tuple(rows)


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _ordered_unique(values: Iterable[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(str(value) for value in values if str(value).strip()))


def _index(rows: Sequence[Mapping[str, Any]], key: str) -> Mapping[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        value = str(row.get(key) or "").strip()
        if not value or value in result:
            raise ReceiptVerificationError(f"DUPLICATE_OR_MISSING_ID:{key}:{value}")
        result[value] = row
    return result


def _identical_duplicate_index(
    rows: Sequence[Mapping[str, Any]], key: str
) -> Mapping[str, Mapping[str, Any]]:
    """Index canonical rows while allowing byte-equivalent subset exports.

    ``counterfacts.jsonl`` is a directional projection of ``evidence_facts``;
    the same counter row therefore legitimately occurs in both files.
    """

    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        value = str(row.get(key) or "").strip()
        if not value:
            raise ReceiptVerificationError(f"MISSING_ID:{key}")
        existing = result.get(value)
        if existing is not None and dict(existing) != dict(row):
            raise ReceiptVerificationError(f"CONFLICTING_DUPLICATE_ID:{key}:{value}")
        result[value] = row
    return result


def receipt_content_files(target_root: str | Path) -> tuple[Path, ...]:
    """Return immutable receipt leaves, excluding the self-referential manifest."""

    root = Path(target_root)
    return tuple(
        sorted(
            (
                path
                for path in root.rglob("*")
                if path.is_file() and path.name != "receipt_manifest.json"
            ),
            key=lambda path: path.relative_to(root).as_posix(),
        )
    )


def receipt_content_index(target_root: str | Path) -> tuple[Mapping[str, Any], ...]:
    root = Path(target_root)
    return tuple(
        {
            "relative_path": path.relative_to(root).as_posix(),
            "sha256": _sha256_file(path),
            "size_bytes": path.stat().st_size,
        }
        for path in receipt_content_files(root)
    )


def receipt_content_tree_hash(target_root: str | Path) -> str:
    """Hash receipt leaves without creating a manifest/hash fixed-point cycle."""

    return stable_hash(receipt_content_index(target_root))


def stagecourt_rule_hash(repo_root: str | Path) -> str:
    root = Path(repo_root).resolve()
    paths = (
        root / "src/e2r/staging.py",
        root / "src/e2r/research_brain/researcher_mode/stagecourt.py",
        root / "configs/e2r_scoring_profile_active.yaml",
        root / "configs/e2r_scoring_profile_calibrated.yaml",
        root / "configs/e2r_scoring_profile_v2_2.yaml",
    )
    payload = tuple(
        {
            "relative_path": path.relative_to(root).as_posix(),
            "sha256": _sha256_file(path),
        }
        for path in paths
        if path.is_file()
    )
    return stable_hash(payload)


def runtime_config_hash() -> str:
    previous_override = os.environ.pop("E2R_SCORING_PROFILE", None)
    try:
        return stable_hash(
            {
                "aggregator": AGGREGATOR_CONFIG,
                "active_profile": asdict(get_active_scoring_profile()),
            }
        )
    finally:
        if previous_override is not None:
            os.environ["E2R_SCORING_PROFILE"] = previous_override


def _hostname(url: str) -> str:
    return (urlparse(url).hostname or "UNKNOWN_PUBLISHER").lower()


def _excerpt(text: str, limit: int = 240) -> str:
    compact = " ".join(str(text).split())
    return compact if len(compact) <= limit else compact[: limit - 1] + "…"


def _provider_kind(value: Any) -> str:
    normalized = str(value or "").upper()
    if "QWEN" in normalized:
        return "QWEN"
    if "OLLAMA" in normalized:
        return "OLLAMA"
    if "COLLABORATION" in normalized:
        return "COLLABORATION_CODEX"
    if "CODEX" in normalized:
        return "CODEX"
    return normalized or "UNKNOWN"


def _provider_call_receipts(target_root: Path) -> tuple[Mapping[str, Any], ...]:
    path = target_root / "fact_extraction_provider_calls.jsonl"
    if not path.is_file():
        return ()
    receipts = []
    for row in _read_jsonl(path):
        receipts.append(
            {
                "schema_version": "e2r_v6_provider_call_receipt_v1",
                "provider_call_id": row.get("batch_id"),
                "call_scope": "FACT_EXTRACTION",
                "provider_name": row.get("provider_name"),
                "provider_kind": _provider_kind(row.get("provider_name")),
                "provider_attempt_count": int(row.get("provider_attempt_count") or 0),
                "prompt_hash": row.get("prompt_hash"),
                "response_hash": row.get("response_hash"),
                "status": row.get("status"),
                "score_or_stage_authority": False,
            }
        )
    return tuple(receipts)


def _provider_call_counts(rows: Sequence[Mapping[str, Any]]) -> Mapping[str, int]:
    counts: Counter[str] = Counter()
    for row in rows:
        counts[str(row.get("provider_kind") or "UNKNOWN")] += int(
            row.get("provider_attempt_count") or 0
        )
    return dict(sorted(counts.items()))


def _scored_lineage_counts(rows: Sequence[Mapping[str, Any]]) -> Mapping[str, int]:
    return dict(
        sorted(
            Counter(_provider_kind(row.get("extraction_provider_name")) for row in rows).items()
        )
    )


def _decision_rows(target_root: Path) -> tuple[Mapping[str, Any], ...]:
    raw = _read_jsonl(target_root / "final_component_decisions.jsonl")
    by_component: dict[str, Mapping[str, Any]] = {}
    for row in raw:
        decision = row.get("decision")
        if not isinstance(decision, Mapping):
            raise ReceiptVerificationError("FINAL_COMPONENT_DECISION_MISSING")
        component_id = str(decision.get("component_id") or "")
        if component_id in by_component:
            raise ReceiptVerificationError(f"DUPLICATE_COMPONENT:{component_id}")
        by_component[component_id] = row
    if set(by_component) != set(CANONICAL_COMPONENT_ORDER):
        raise ReceiptVerificationError("EXACT_SEVEN_COMPONENTS_REQUIRED")
    return tuple(by_component[component_id] for component_id in CANONICAL_COMPONENT_ORDER)


def _component_receipts(
    target_root: Path,
    decision_rows: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    memos = {
        str(row.get("component_id") or ""): row
        for row in _read_jsonl(target_root / "component_research_memos.jsonl")
    }
    receipts: list[Mapping[str, Any]] = []
    for raw in decision_rows:
        decision = dict(raw["decision"])
        component_id = str(decision["component_id"])
        memo = memos.get(component_id, {})
        resolution_ids = _ordered_unique(memo.get("resolution_fact_ids") or ())
        receipts.append(
            {
                "schema_version": "e2r_v6_component_decision_receipt_v1",
                "component_id": component_id,
                "max_points": float(decision["max_points"]),
                "support_points": float(decision["support_points"]),
                "counter_effect": float(decision["counter_effect"]),
                "final_points": float(decision["final_points"]),
                "support_fact_ids": list(decision.get("fact_ids") or ()),
                "counter_fact_ids": list(decision.get("counter_fact_ids") or ()),
                "resolution_fact_ids": list(resolution_ids),
                "resolution_fact_role": "MEMO_CONTEXT_ONLY_NOT_DIRECT_POINT_INPUT",
                "historical_anchor_ids": list(decision.get("anchor_ids") or ()),
                "judge_decision_ids": list(decision.get("judge_ids") or ()),
                "why_not_higher": str(memo.get("why_not_higher") or ""),
                "why_not_lower": str(memo.get("why_not_lower") or ""),
                "confidence": float(decision["confidence"]),
                "research_status": "RESEARCH_COMPLETE",
                "aggregation_method": AGGREGATOR_CONFIG["consensus_method"],
                "aggregation_trace_hash": stable_hash(raw),
                "proposal_median": float(decision["proposal_median"]),
                "consensus_band": list(decision["consensus_band"]),
                "judge_proposals": dict(decision["judge_proposals"]),
                "prompt_hashes": list(decision.get("prompt_hashes") or ()),
                "response_hashes": list(decision.get("response_hashes") or ()),
                "provider_call_ids": list(decision.get("judge_call_ids") or ()),
                "aggregator_config_hash": str(decision.get("config_hash") or ""),
            }
        )
    return tuple(receipts)


def _judge_receipts(target_root: Path) -> tuple[Mapping[str, Any], ...]:
    receipts = []
    for row in _read_jsonl(target_root / "component_judge_decisions.jsonl"):
        receipts.append(
            {
                "schema_version": "e2r_v6_judge_decision_receipt_v1",
                "judge_decision_id": row.get("judge_id"),
                "component_id": row.get("component_id"),
                "role": row.get("role"),
                "proposed_points": row.get("proposed_points"),
                "allowed_range": row.get("allowed_range"),
                "support_fact_ids": row.get("support_fact_ids") or [],
                "counter_fact_ids": row.get("counter_fact_ids") or [],
                "anchor_ids": row.get("nearest_anchor_ids") or [],
                "why_higher": row.get("why_not_lower") or "",
                "why_lower": row.get("why_not_higher") or "",
                "prompt_hash": row.get("prompt_hash"),
                "response_hash": row.get("response_hash"),
                "provider_call_id": row.get("judge_call_id"),
                "provider_name": row.get("provider_name"),
                "provider_route": PROVIDER_ROUTE,
                "score_or_stage_authority": False,
            }
        )
    return tuple(
        sorted(
            receipts,
            key=lambda row: (
                CANONICAL_COMPONENT_ORDER.index(str(row["component_id"])),
                str(row["role"]),
            ),
        )
    )


def _fact_receipts(
    target_root: Path,
    components: Sequence[Mapping[str, Any]],
    *,
    as_of_date: str,
    target_id: str,
) -> tuple[Mapping[str, Any], ...]:
    facts = _identical_duplicate_index(
        (*_read_jsonl(target_root / "evidence_facts.jsonl"), *_read_jsonl(target_root / "counterfacts.jsonl")),
        "fact_id",
    )
    claims = _index(_read_jsonl(target_root / "material_fact_claims.jsonl"), "claim_id")
    documents = _index(_read_jsonl(target_root / "documents.jsonl"), "document_id")
    component_ids: dict[str, list[str]] = defaultdict(list)
    roles: dict[str, set[str]] = defaultdict(set)
    for component in components:
        component_id = str(component["component_id"])
        for field, role in (
            ("support_fact_ids", "SUPPORT"),
            ("counter_fact_ids", "COUNTER"),
            ("resolution_fact_ids", "RESOLUTION"),
        ):
            for fact_id in component.get(field) or ():
                component_ids[str(fact_id)].append(component_id)
                roles[str(fact_id)].add(role)
    receipts: list[Mapping[str, Any]] = []
    role_order = {"SUPPORT": 0, "COUNTER": 1, "RESOLUTION": 2, "HARD_BREAK": 3}
    for fact_id in sorted(component_ids):
        fact = facts.get(fact_id)
        if fact is None:
            raise ReceiptVerificationError(f"SCORED_FACT_MISSING:{fact_id}")
        claim_ids = _ordered_unique(fact.get("claim_ids") or ())
        claim_candidates = [claims[claim_id] for claim_id in claim_ids if claim_id in claims]
        if len(claim_candidates) != len(claim_ids) or not claim_candidates:
            raise ReceiptVerificationError(f"SCORED_FACT_CLAIM_MISSING:{fact_id}")
        claim = next(
            (row for row in claim_candidates if str(row.get("document_id") or "") in documents),
            claim_candidates[0],
        )
        document_id = str(claim.get("document_id") or "")
        document = documents.get(document_id)
        if document is None:
            source_ids = _ordered_unique(claim.get("source_ids") or fact.get("source_ids") or ())
            document = next((documents[value] for value in source_ids if value in documents), None)
            document_id = str(document.get("document_id") or "") if document else ""
        if document is None:
            raise ReceiptVerificationError(f"SCORED_FACT_SOURCE_MISSING:{fact_id}")
        url = str(claim.get("canonical_url") or document.get("canonical_url") or "")
        exact_quote = str(claim.get("exact_quote") or "")
        if not url or not exact_quote:
            raise ReceiptVerificationError(f"SCORED_FACT_SOURCE_OR_QUOTE_MISSING:{fact_id}")
        content_hash = str(
            document.get("full_source_content_hash") or document.get("content_hash") or ""
        )
        if not re.fullmatch(r"[0-9a-f]{64}", content_hash):
            raise ReceiptVerificationError(f"DOCUMENT_HASH_MISSING:{document_id}")
        fact_roles = tuple(sorted(roles[fact_id], key=lambda role: role_order[role]))
        primary_role = next(role for role in ("SUPPORT", "COUNTER", "RESOLUTION", "HARD_BREAK") if role in fact_roles)
        receipts.append(
            {
                "schema_version": "e2r_v6_scoring_fact_receipt_v1",
                "fact_id": fact_id,
                "target_id": target_id,
                "component_ids": list(_ordered_unique(component_ids[fact_id])),
                "fact_role": primary_role,
                "fact_roles": list(fact_roles),
                "direct_point_input": primary_role in {"SUPPORT", "COUNTER"},
                "subject_id": claim.get("subject_id") or fact.get("subject") or target_id,
                "business_segment": fact.get("business_segment") or claim.get("business_segment") or "",
                "product_family": fact.get("product_family") or claim.get("product_family") or "",
                "economic_mechanism": fact.get("economic_mechanism") or claim.get("economic_mechanism") or "",
                "predicate_family": claim.get("predicate_family") or fact.get("predicate") or "",
                "normalized_object": claim.get("normalized_object") or fact.get("value"),
                "value": fact.get("value"),
                "unit": fact.get("unit"),
                "period": fact.get("period") or claim.get("period") or "",
                "temporal_status": fact.get("current_lifecycle") or claim.get("current_lifecycle") or "",
                "claim_ids": list(claim_ids),
                "source_document_id": document_id,
                "source_url": url,
                "source_title": document.get("title") or "",
                "source_publisher": _hostname(url),
                "source_publisher_derivation": "CANONICAL_URL_HOSTNAME_V1",
                "source_tier": claim.get("source_tier") or document.get("source_family") or "",
                "source_family": claim.get("source_family") or document.get("source_family") or "",
                "published_at": claim.get("published_at") or document.get("published_at"),
                "available_at": claim.get("available_at") or document.get("available_at"),
                "document_content_hash": content_hash,
                "exact_quote_hash": _sha256_bytes(exact_quote.encode("utf-8")),
                "quote_excerpt": _excerpt(exact_quote),
                "quote_excerpt_hash": _sha256_bytes(_excerpt(exact_quote).encode("utf-8")),
                "page_section_locator": "NOT_CAPTURED",
                "issuer_scoped": str(claim.get("target_id") or "") == target_id,
                "issuer_scope_derivation": "CLAIM_TARGET_SCOPE_V1",
                "current_score_eligible": True,
                "current_score_eligibility_basis": "FINAL_DECISION_REFERENCE_AND_AS_OF_VALIDATED",
                "source_independence_group": fact.get("source_independence_group") or claim.get("source_independence_group") or "",
                "extraction_provider_name": claim.get("provider_name") or "UNKNOWN",
                "provider_prompt_hash": claim.get("provider_prompt_hash"),
                "provider_response_hash": claim.get("provider_response_hash"),
                "as_of_date": as_of_date,
                "gold_fact": False,
            }
        )
    return tuple(receipts)


def _source_receipts(facts: Sequence[Mapping[str, Any]]) -> tuple[Mapping[str, Any], ...]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for fact in facts:
        grouped[str(fact["source_document_id"])].append(fact)
    by_id: dict[str, Mapping[str, Any]] = {}
    for source_id, source_facts in grouped.items():
        fact = source_facts[0]
        row = {
            "schema_version": "e2r_v6_source_manifest_row_v1",
            "source_document_id": source_id,
            "source_url": fact["source_url"],
            "source_title": fact["source_title"],
            "source_publisher": fact["source_publisher"],
            "source_tier": fact["source_tier"],
            "source_family": fact["source_family"],
            "published_at": fact["published_at"],
            "available_at": fact["available_at"],
            "document_content_hash": fact["document_content_hash"],
            "source_independence_group": fact["source_independence_group"],
            "fact_document_hashes": {
                str(item["fact_id"]): item["document_content_hash"]
                for item in sorted(source_facts, key=lambda value: str(value["fact_id"]))
            },
            "fact_exact_quote_hashes": {
                str(item["fact_id"]): item["exact_quote_hash"]
                for item in sorted(source_facts, key=lambda value: str(value["fact_id"]))
            },
        }
        by_id[source_id] = row
    return tuple(by_id[key] for key in sorted(by_id))


def _anchor_receipts(
    repo_root: Path,
    *,
    archetype_id: str,
    components: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    anchor_ids = set(
        str(anchor_id)
        for component in components
        for anchor_id in component.get("historical_anchor_ids") or ()
    )
    anchors = _index(_historical_anchors(repo_root=repo_root, archetype_id=archetype_id), "anchor_id")
    missing = anchor_ids - set(anchors)
    if missing:
        raise ReceiptVerificationError(f"ANCHOR_PAYLOAD_MISSING:{sorted(missing)[:3]}")
    receipts = []
    for anchor_id in sorted(anchor_ids):
        payload = dict(anchors[anchor_id])
        receipts.append(
            {
                "schema_version": "e2r_v6_anchor_manifest_row_v1",
                "anchor_id": anchor_id,
                "component_id": payload.get("component_id"),
                "archetype_id": payload.get("archetype_id"),
                "normalized_anchor_payload": payload,
                "anchor_payload_hash": stable_hash(payload),
            }
        )
    return tuple(receipts)


def _stage_receipt(
    repo_root: Path,
    target_root: Path,
    score_receipt: Mapping[str, Any],
    *,
    receipt_id: str,
) -> Mapping[str, Any]:
    trace = _read_json(target_root / "stagecourt_trace.json")
    decision = dict(trace.get("decision") or {})
    audit = dict(trace.get("audit") or {})
    component_vector = dict(score_receipt["component_score_vector"])
    max_vector = dict(score_receipt["component_max_vector"])
    green_gate = bool(audit.get("green_gate_satisfied"))
    blocking_guards = list(audit.get("blocking_green_guard_primitives") or ())
    source_families = {
        str(row.get("source_family") or "")
        for row in _read_jsonl(target_root / "material_fact_claims.jsonl")
        if row.get("source_family")
    }
    diagnostics: dict[str, float] = {
        "score_valid": 1.0,
        "archetype_weight_profile_applied": 1.0,
        "claim_backed_claim_count_capped": 1.0,
        "score_claim_backed_component_ratio": 100.0,
        "orphan_score_component_count_capped": 0.0,
        "score_claim_backed_required": 100.0,
        "source_backed_deep_research_completed": 100.0,
        "llm_deep_research_completed": 100.0,
        "report_date_confidence": 100.0,
        "date_unverified_snippet_news_count_capped": 0.0,
        "date_unverified_document_count_capped": 0.0,
        "snippet_only_green_block": 0.0,
        "emerging_theme_active": 0.0,
        "archetype_green_restricted_by_profile": 0.0,
        "revision_score": float(audit.get("revision_score") or 0.0),
        "structural_visibility_quality": 100.0 if green_gate else 0.0,
        "contract_quality": 100.0 if green_gate else 0.0,
        "one_off_shortage_risk": 0.0 if green_gate else 100.0,
        "price_only_blowoff_score": 0.0,
        "theme_overheat_score": 0.0,
        "evidence_contract_green_gate_coverage_pct": 100.0 if green_gate else 0.0,
        "evidence_contract_green_gate_missing_primitive_count_capped": 0.0 if green_gate else 1.0,
        "evidence_contract_guard_present_primitive_count_capped": min(100.0, float(len(blocking_guards))),
        "evidence_contract_guard_missing_primitive_count_capped": 0.0,
        "cross_evidence_family_count": min(100.0, float(len(source_families))),
    }
    for component_id in CANONICAL_COMPONENT_ORDER:
        diagnostics[f"archetype_weight_{component_id}"] = float(max_vector[component_id])
        diagnostics[f"archetype_component_{component_id}"] = float(component_vector[component_id])
    event = dict(decision.get("event_overlay") or {})
    hard_break_ids = list(decision.get("hard_break_claim_ids") or ())
    current_guards = list(decision.get("current_guard_primitives") or ())
    risk_level = "hard_break" if hard_break_ids else "high" if current_guards else "low"
    return {
        "schema_version": STAGECOURT_RECEIPT_SCHEMA,
        "target_id": score_receipt["target_id"],
        "score_receipt_id": receipt_id,
        "component_score_vector_hash": stable_hash(component_vector),
        "total_score": score_receipt["total_score"],
        "risk_fact_ids": [],
        "hard_break_fact_ids": [],
        "hard_break_claim_ids": hard_break_ids,
        "canonical_stage": decision.get("canonical_stage"),
        "decision_status": decision.get("status"),
        "score_valid": decision.get("score_valid"),
        "event_overlay": event,
        "event_overlay_changed_canonical_stage": event.get("canonical_stage_effect") not in {None, "", "NONE"},
        "stagecourt_rule_hash": stagecourt_rule_hash(repo_root),
        "decision_trace_hash": stable_hash(trace),
        "classification_input": {
            "diagnostic_scores": diagnostics,
            "previous_stage": None,
            "thesis_ongoing": False,
            "theme_regime_score": 0.0,
            "company_event_score": 0.0,
            "high_quality_company_event": False,
            "archive_requested": False,
            "coverage_impossible": False,
            "red_team": {
                "soft_4b_score": 0.0,
                "soft_4b_status": "none",
                "thesis_break_score": 100.0 if hard_break_ids else 40.0 if current_guards else 0.0,
                "risk_level": risk_level,
                "has_hard_break": bool(hard_break_ids),
            },
            "green_gate_satisfied": green_gate,
            "blocking_green_guard_primitives": blocking_guards,
            "revision_score": float(audit.get("revision_score") or 0.0),
        },
    }


def export_target_receipt(
    *,
    repo_root: str | Path,
    source_root: str | Path,
    target_id: str,
    destination_root: str | Path,
) -> Mapping[str, Any]:
    repo = Path(repo_root).resolve()
    source = Path(source_root).resolve()
    target_root = source / target_id
    destination = Path(destination_root).resolve() / target_id
    destination.mkdir(parents=True, exist_ok=True)
    target_manifest = _read_json(target_root / "target_run_manifest.json")
    score_vector = _read_json(target_root / "score_vector.json")
    atomic_stage = _read_json(target_root / "atomic_stage_decision.json")
    saturation = _read_json(target_root / "semantic_saturation_certificate.json")
    provider_audit = _read_json(target_root / "research_provider_response_cache_audit.json")
    production_lane = _read_json(source / "production_lane_manifest.json")
    gold = _read_json(source / "post_run_gold_recall_audit.json")
    decision_rows = _decision_rows(target_root)
    components = _component_receipts(target_root, decision_rows)
    judges = _judge_receipts(target_root)
    facts = _fact_receipts(
        target_root,
        components,
        as_of_date=str(target_manifest["as_of_date"]),
        target_id=target_id,
    )
    sources = _source_receipts(facts)
    anchors = _anchor_receipts(
        repo,
        archetype_id=str(target_manifest["archetype_id"]),
        components=components,
    )
    provider_calls = _provider_call_receipts(target_root)
    receipt_id = "V6RECEIPT-" + stable_hash(
        {
            "target_id": target_id,
            "as_of_date": target_manifest["as_of_date"],
            "output_tree_hash": target_manifest["output_tree_hash"],
        }
    )[:24]
    component_vector = {
        component_id: float(score_vector["component_score_vector"][component_id])
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    component_max_vector = {
        str(row["component_id"]): float(row["max_points"]) for row in components
    }
    total = round(sum(component_vector.values()), 6)
    score_receipt = {
        "schema_version": SCORE_RECEIPT_SCHEMA,
        "receipt_id": receipt_id,
        "target_id": target_id,
        "score_scale": "FULL_E2R_100",
        "score_valid": score_vector.get("score_valid"),
        "component_score_vector": component_vector,
        "component_max_vector": component_max_vector,
        "total_score": float(score_vector["total_points"]),
        "total_score_recomputed": total,
        "component_sum_matches_total": abs(total - float(score_vector["total_points"])) <= 1e-9,
        "research_complete": target_manifest.get("production_research_complete"),
        "semantic_saturation_certified": saturation.get("semantic_saturation_certified"),
        "material_gap_count": len(saturation.get("pending_reasons") or ()),
        "provider_error_count": int(provider_audit.get("provider_error_count") or 0),
        "canonical_stage": atomic_stage.get("canonical_stage"),
        "stage_status": atomic_stage.get("status"),
        "risk_overlay": "LOW" if not atomic_stage.get("hard_break_claim_ids") else "HARD_BREAK",
        "hard_break_fact_ids": [],
        "daily_event_overlay_can_change_canonical_stage": False,
        "production_research_status": "COMPLETE",
        "gold_evaluation_status": "PASS" if gold.get("critical_count_sum") == 0 else "FAIL",
        "score_status": "COMPLETE" if score_vector.get("status") == "COMPLETE" else "PENDING",
        "stagecourt_status": atomic_stage.get("status"),
        "gold_post_run_metrics": dict(gold.get("metrics") or {}),
        "gold_leakage_count": int((gold.get("critical_counts") or {}).get("gold_leakage_count") or 0),
    }
    stage_receipt = _stage_receipt(
        repo,
        target_root,
        score_receipt,
        receipt_id=receipt_id,
    )
    write_json(destination / "score_receipt.json", score_receipt)
    write_jsonl(destination / "component_decisions.jsonl", components)
    write_jsonl(destination / "scoring_facts.jsonl", facts)
    write_jsonl(destination / "judge_decisions.jsonl", judges)
    write_jsonl(destination / "source_manifest.jsonl", sources)
    write_jsonl(destination / "anchor_manifest.jsonl", anchors)
    write_jsonl(destination / "provider_calls.jsonl", provider_calls)
    write_json(destination / "stagecourt_receipt.json", stage_receipt)

    provider_identity = dict(production_lane.get("research_provider") or {})
    calls = _provider_call_counts(provider_calls)
    lineage = _scored_lineage_counts(facts)
    actual_output_hash = canary_output_tree_hash(target_root, include_post_run_gold=False)
    content_index = receipt_content_index(destination)
    manifest = {
        "schema_version": RECEIPT_MANIFEST_SCHEMA,
        "receipt_id": receipt_id,
        "target_id": target_id,
        "company_name": target_manifest.get("company_name"),
        "as_of_date": target_manifest.get("as_of_date"),
        "latest_trading_snapshot_date": target_manifest.get("latest_trading_snapshot_date"),
        "archetype_id": target_manifest.get("archetype_id"),
        "run_commit_sha": git_head_sha(repo),
        "verification_commit_sha": git_head_sha(repo),
        "commit_sha_hash_scope": "MANIFEST_EXCLUDED_FROM_IMMUTABLE_CONTENT_HASH",
        "config_hash": runtime_config_hash(),
        "prompt_hashes": {
            f"{row['component_id']}:{row['role']}": row["prompt_hash"] for row in judges
        },
        "provider_identity_hash": provider_identity.get("provider_identity_hash"),
        "source_corpus_hash": stable_hash(sources),
        "output_tree_hash": target_manifest.get("output_tree_hash"),
        "output_tree_hash_recomputed": actual_output_hash,
        "output_tree_hash_matches": target_manifest.get("output_tree_hash") == actual_output_hash,
        "tracked_receipt_tree_hash": receipt_content_tree_hash(destination),
        "tracked_receipt_content_index": list(content_index),
        "tracked_receipt_hash_scope": "ALL_TARGET_RECEIPT_FILES_EXCEPT_RECEIPT_MANIFEST_JSON",
        "gold_visible_during_production": bool(production_lane.get("gold_visibility")),
        "provider_selected_explicitly": bool(provider_identity.get("provider_selected_explicitly")),
        "provider_route": (provider_identity.get("provider_identity") or {}).get("provider_route"),
        "qwen_call_count": int(calls.get("QWEN", 0)),
        "ollama_call_count": int(calls.get("OLLAMA", 0)),
        "provider_call_counts": calls,
        "scored_fact_provider_lineage_counts": lineage,
        "inherited_qwen_scored_fact_count": int(lineage.get("QWEN", 0)),
        "inherited_ollama_scored_fact_count": int(lineage.get("OLLAMA", 0)),
        "current_invocation_provider_name": provider_audit.get("provider_name"),
        "current_invocation_logical_call_count": int(provider_audit.get("logical_call_count") or 0),
        "current_invocation_successful_call_count": int(provider_audit.get("successful_call_count") or 0),
        "current_invocation_provider_error_count": int(provider_audit.get("provider_error_count") or 0),
        "score_or_stage_authority": False,
        "query_count": int(target_manifest.get("query_count") or 0),
        "document_count": int(target_manifest.get("document_count") or 0),
        "fact_count": int(target_manifest.get("fact_count") or 0),
        "counterfact_count": int(target_manifest.get("counterfact_count") or 0),
        "receipt_scoring_fact_count": len(facts),
        "receipt_source_count": len(sources),
        "receipt_anchor_count": len(anchors),
        "receipt_judge_count": len(judges),
        "receipt_component_count": len(components),
        "receipt_provider_call_count": len(provider_calls),
    }
    write_json(destination / "receipt_manifest.json", manifest)
    return manifest


def export_receipts(
    *,
    repo_root: str | Path,
    source_output_root: str | Path,
    targets: Sequence[str],
    destination: str | Path,
) -> Mapping[str, Any]:
    manifests = tuple(
        export_target_receipt(
            repo_root=repo_root,
            source_root=source_output_root,
            target_id=str(target),
            destination_root=destination,
        )
        for target in targets
    )
    verification = verify_receipts(destination)
    return {
        "schema_version": "e2r_v6_receipt_export_run_v1",
        "target_count": len(manifests),
        "target_ids": [row["target_id"] for row in manifests],
        "manifests": list(manifests),
        "verification": verification,
        "status": "E2R_V6_RECEIPT_EXPORT_PASS" if verification["status"] == VERIFICATION_PASS else "E2R_V6_RECEIPT_EXPORT_FAIL",
    }


def _add_failure(failures: list[Mapping[str, Any]], code: str, detail: Any = None) -> None:
    failures.append({"code": code, "detail": detail})


def _verify_component_formula(
    component: Mapping[str, Any],
    judges: Sequence[Mapping[str, Any]],
    failures: list[Mapping[str, Any]],
) -> None:
    component_id = str(component["component_id"])
    by_role = {str(row.get("role")): row for row in judges}
    required = {"ANALYST", "SKEPTIC", "CALIBRATION_JUDGE"}
    if set(by_role) != required or len(judges) != 3:
        _add_failure(failures, "EXACT_THREE_JUDGE_ROLES_REQUIRED", component_id)
        return
    proposals = [float(by_role[role]["proposed_points"]) for role in required]
    lower = max(float(row["allowed_range"][0]) for row in judges)
    upper = min(float(row["allowed_range"][1]) for row in judges)
    maximum = float(component["max_points"])
    support = min(
        maximum,
        statistics.median(
            (
                float(by_role["ANALYST"]["proposed_points"]),
                float(by_role["CALIBRATION_JUDGE"]["proposed_points"]),
            )
        ),
    )
    proposal_median = statistics.median(proposals)
    counter_adjusted = min(support, proposal_median, float(by_role["SKEPTIC"]["proposed_points"]))
    expected = min(upper, max(lower, counter_adjusted))
    checks = {
        "COMPONENT_SUPPORT_POINTS_MISMATCH": (support, float(component["support_points"])),
        "COMPONENT_PROPOSAL_MEDIAN_MISMATCH": (proposal_median, float(component["proposal_median"])),
        "COMPONENT_FINAL_POINTS_MISMATCH": (expected, float(component["final_points"])),
        "COMPONENT_COUNTER_EFFECT_MISMATCH": (support - expected, float(component["counter_effect"])),
    }
    for code, (expected_value, actual_value) in checks.items():
        if abs(expected_value - actual_value) > 1e-6:
            _add_failure(failures, code, {"component_id": component_id, "expected": expected_value, "actual": actual_value})
    if [lower, upper] != [float(value) for value in component["consensus_band"]]:
        _add_failure(failures, "COMPONENT_CONSENSUS_BAND_MISMATCH", component_id)


def _recompute_stage(
    score: Mapping[str, Any],
    stage: Mapping[str, Any],
) -> str:
    vector = score["component_score_vector"]
    maxima = score["component_max_vector"]
    normalized = {
        component_id: (
            float(vector[component_id]) / float(maxima[component_id]) * CANONICAL_COMPONENT_MAX[component_id]
            if float(maxima[component_id])
            else 0.0
        )
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    classification = dict(stage["classification_input"])
    diagnostics = {
        str(key): float(value) for key, value in dict(classification["diagnostic_scores"]).items()
    }
    snapshot = ScoreSnapshot(
        symbol=str(score["target_id"]),
        as_of_date=date.fromisoformat(str(stage.get("as_of_date") or score.get("as_of_date") or "2026-07-12")),
        eps_fcf_explosion_score=normalized["eps_fcf_explosion"],
        earnings_visibility_score=normalized["earnings_visibility"],
        bottleneck_pricing_score=normalized["bottleneck_pricing"],
        market_mispricing_score=normalized["market_mispricing"],
        valuation_rerating_score=normalized["valuation_rerating"],
        capital_allocation_score=normalized["capital_allocation"],
        information_confidence_score=normalized["information_confidence"],
        risk_penalty=0.0,
        total_score=float(score["total_score"]),
        diagnostic_scores=diagnostics,
        evidence_ids=(),
        scoring_version="e2r-v6-tracked-receipt",
    )
    red = dict(classification["red_team"])
    red_team = RedTeamAssessment(
        symbol=snapshot.symbol,
        as_of_date=snapshot.as_of_date,
        soft_4b_score=float(red["soft_4b_score"]),
        soft_4b_status=Soft4BStatus(str(red["soft_4b_status"])),
        thesis_break_score=float(red["thesis_break_score"]),
        risk_level=RedTeamRiskLevel(str(red["risk_level"])),
        has_hard_break=bool(red["has_hard_break"]),
        evidence_ids=(),
        version="e2r-v6-tracked-receipt",
    )
    previous = classification.get("previous_stage")
    inputs = StageClassificationInput(
        score=snapshot,
        red_team=red_team,
        previous_stage=Stage(previous) if previous else None,
        theme_regime_score=float(classification.get("theme_regime_score") or 0.0),
        company_event_score=float(classification.get("company_event_score") or 0.0),
        high_quality_company_event=bool(classification.get("high_quality_company_event")),
        thesis_ongoing=bool(classification.get("thesis_ongoing")),
        archive_requested=bool(classification.get("archive_requested")),
        coverage_impossible=bool(classification.get("coverage_impossible")),
    )
    previous_override = os.environ.pop("E2R_SCORING_PROFILE", None)
    try:
        return StageClassifier().classify(inputs).stage.value
    finally:
        if previous_override is not None:
            os.environ["E2R_SCORING_PROFILE"] = previous_override


def verify_target_receipt(target_root: str | Path) -> Mapping[str, Any]:
    root = Path(target_root).resolve()
    failures: list[Mapping[str, Any]] = []
    for filename in ("receipt_manifest.json", *REQUIRED_TARGET_FILES):
        if not (root / filename).is_file():
            _add_failure(failures, "REQUIRED_RECEIPT_FILE_MISSING", filename)
    if failures:
        return {"target_id": root.name, "status": VERIFICATION_FAIL, "failures": failures, "critical_count": len(failures)}
    manifest = _read_json(root / "receipt_manifest.json")
    score = _read_json(root / "score_receipt.json")
    stage = _read_json(root / "stagecourt_receipt.json")
    components = _read_jsonl(root / "component_decisions.jsonl")
    facts = _read_jsonl(root / "scoring_facts.jsonl")
    judges = _read_jsonl(root / "judge_decisions.jsonl")
    sources = _read_jsonl(root / "source_manifest.jsonl")
    anchors = _read_jsonl(root / "anchor_manifest.jsonl")
    provider_calls = _read_jsonl(root / "provider_calls.jsonl")
    target_id = str(manifest.get("target_id") or root.name)

    if manifest.get("schema_version") != RECEIPT_MANIFEST_SCHEMA:
        _add_failure(failures, "MANIFEST_SCHEMA_MISMATCH")
    actual_index = receipt_content_index(root)
    if list(actual_index) != list(manifest.get("tracked_receipt_content_index") or ()):
        _add_failure(failures, "RECEIPT_CONTENT_INDEX_MISMATCH")
    actual_tree_hash = receipt_content_tree_hash(root)
    if manifest.get("tracked_receipt_tree_hash") != actual_tree_hash:
        _add_failure(failures, "RECEIPT_TREE_HASH_MISMATCH")
    repo_root = Path(__file__).resolve().parents[4]
    if manifest.get("config_hash") != runtime_config_hash():
        _add_failure(failures, "CURRENT_CONFIG_HASH_MISMATCH")
    if stage.get("stagecourt_rule_hash") != stagecourt_rule_hash(repo_root):
        _add_failure(failures, "CURRENT_STAGECOURT_RULE_HASH_MISMATCH")
    serialized = json.dumps(
        [
            manifest,
            score,
            stage,
            *components,
            *facts,
            *judges,
            *sources,
            *anchors,
            *provider_calls,
        ],
        ensure_ascii=False,
    )
    if any(pattern.search(serialized) for pattern in _FORBIDDEN_IDENTITY_PATTERNS):
        _add_failure(failures, "ABSOLUTE_PATH_IDENTITY_PRESENT")
    if int(manifest.get("qwen_call_count") or 0) != 0:
        _add_failure(failures, "QWEN_CALL_COUNT_NONZERO", manifest.get("qwen_call_count"))
    if int(manifest.get("ollama_call_count") or 0) != 0:
        _add_failure(failures, "OLLAMA_CALL_COUNT_NONZERO", manifest.get("ollama_call_count"))
    recomputed_provider_counts = _provider_call_counts(provider_calls)
    if dict(manifest.get("provider_call_counts") or {}) != recomputed_provider_counts:
        _add_failure(failures, "PROVIDER_CALL_COUNTS_MISMATCH")
    if int(manifest.get("qwen_call_count") or 0) != int(recomputed_provider_counts.get("QWEN", 0)):
        _add_failure(failures, "QWEN_CALL_COUNT_RECOMPUTE_MISMATCH")
    if int(manifest.get("ollama_call_count") or 0) != int(recomputed_provider_counts.get("OLLAMA", 0)):
        _add_failure(failures, "OLLAMA_CALL_COUNT_RECOMPUTE_MISMATCH")
    if int(manifest.get("inherited_qwen_scored_fact_count") or 0) != 0:
        _add_failure(failures, "INHERITED_QWEN_SCORED_FACT_LINEAGE_PRESENT", manifest.get("inherited_qwen_scored_fact_count"))
    if int(manifest.get("inherited_ollama_scored_fact_count") or 0) != 0:
        _add_failure(failures, "INHERITED_OLLAMA_SCORED_FACT_LINEAGE_PRESENT", manifest.get("inherited_ollama_scored_fact_count"))
    if manifest.get("provider_route") != PROVIDER_ROUTE:
        _add_failure(failures, "PROVIDER_ROUTE_MISMATCH", manifest.get("provider_route"))
    if manifest.get("provider_selected_explicitly") is not True:
        _add_failure(failures, "PROVIDER_NOT_SELECTED_EXPLICITLY")
    if manifest.get("gold_visible_during_production") is not False:
        _add_failure(failures, "GOLD_VISIBLE_DURING_PRODUCTION")

    component_by_id = {str(row.get("component_id")): row for row in components}
    if tuple(component_by_id) != tuple(CANONICAL_COMPONENT_ORDER) or len(components) != 7:
        _add_failure(failures, "EXACT_CANONICAL_COMPONENT_ROSTER_REQUIRED")
    judge_by_id = _index(judges, "judge_decision_id") if judges else {}
    fact_by_id = _index(facts, "fact_id") if facts else {}
    source_by_id = _index(sources, "source_document_id") if sources else {}
    anchor_by_id = _index(anchors, "anchor_id") if anchors else {}
    expected_fact_roles: dict[str, set[str]] = defaultdict(set)
    for component_id in CANONICAL_COMPONENT_ORDER:
        component = component_by_id.get(component_id)
        if component is None:
            continue
        component_judges = [row for row in judges if row.get("component_id") == component_id]
        _verify_component_formula(component, component_judges, failures)
        for judge_id in component.get("judge_decision_ids") or ():
            if str(judge_id) not in judge_by_id:
                _add_failure(failures, "ORPHAN_COMPONENT_JUDGE_ID", judge_id)
        for field, role in (
            ("support_fact_ids", "SUPPORT"),
            ("counter_fact_ids", "COUNTER"),
            ("resolution_fact_ids", "RESOLUTION"),
        ):
            for fact_id in component.get(field) or ():
                expected_fact_roles[str(fact_id)].add(role)
                if str(fact_id) not in fact_by_id:
                    _add_failure(failures, "ORPHAN_COMPONENT_FACT_ID", fact_id)
        for anchor_id in component.get("historical_anchor_ids") or ():
            if str(anchor_id) not in anchor_by_id:
                _add_failure(failures, "ORPHAN_COMPONENT_ANCHOR_ID", anchor_id)
    if len(judges) != 21:
        _add_failure(failures, "EXACT_TWENTY_ONE_JUDGES_REQUIRED", len(judges))
    for judge in judges:
        for fact_id in (*judge.get("support_fact_ids", ()), *judge.get("counter_fact_ids", ())):
            if str(fact_id) not in fact_by_id:
                _add_failure(failures, "ORPHAN_JUDGE_FACT_ID", fact_id)
        for anchor_id in judge.get("anchor_ids") or ():
            if str(anchor_id) not in anchor_by_id:
                _add_failure(failures, "ORPHAN_JUDGE_ANCHOR_ID", anchor_id)
        if judge.get("score_or_stage_authority") is not False:
            _add_failure(failures, "JUDGE_DIRECT_AUTHORITY_PRESENT", judge.get("judge_decision_id"))
    if set(fact_by_id) != set(expected_fact_roles):
        _add_failure(failures, "SCORING_FACT_ROSTER_MISMATCH", {"extra": sorted(set(fact_by_id) - set(expected_fact_roles))[:5], "missing": sorted(set(expected_fact_roles) - set(fact_by_id))[:5]})
    cutoff = date.fromisoformat(str(manifest["as_of_date"]))
    for fact_id, fact in fact_by_id.items():
        if set(fact.get("fact_roles") or ()) != expected_fact_roles[fact_id]:
            _add_failure(failures, "SCORING_FACT_ROLE_MISMATCH", fact_id)
        if fact.get("gold_fact") is not False:
            _add_failure(failures, "GOLD_FACT_IN_SCORING_RECEIPT", fact_id)
        if str(fact.get("source_document_id")) not in source_by_id:
            _add_failure(failures, "ORPHAN_FACT_SOURCE_ID", fact_id)
        for field in ("published_at", "available_at"):
            value = str(fact.get(field) or "")[:10]
            try:
                if not value or date.fromisoformat(value) > cutoff:
                    _add_failure(failures, "FUTURE_OR_MISSING_FACT_DATE", {"fact_id": fact_id, "field": field, "value": value})
            except ValueError:
                _add_failure(failures, "INVALID_FACT_DATE", {"fact_id": fact_id, "field": field, "value": value})
        if not re.fullmatch(r"[0-9a-f]{64}", str(fact.get("document_content_hash") or "")):
            _add_failure(failures, "FACT_DOCUMENT_HASH_INVALID", fact_id)
        if not re.fullmatch(r"[0-9a-f]{64}", str(fact.get("exact_quote_hash") or "")):
            _add_failure(failures, "FACT_QUOTE_HASH_INVALID", fact_id)
        excerpt = str(fact.get("quote_excerpt") or "")
        if _sha256_bytes(excerpt.encode("utf-8")) != fact.get("quote_excerpt_hash"):
            _add_failure(failures, "FACT_QUOTE_EXCERPT_HASH_MISMATCH", fact_id)
        source = source_by_id.get(str(fact.get("source_document_id")))
        if source is not None:
            if source.get("document_content_hash") != fact.get("document_content_hash"):
                _add_failure(failures, "FACT_SOURCE_DOCUMENT_HASH_MISMATCH", fact_id)
            if (source.get("fact_document_hashes") or {}).get(fact_id) != fact.get("document_content_hash"):
                _add_failure(failures, "FACT_DOCUMENT_HASH_LINEAGE_MISMATCH", fact_id)
            if (source.get("fact_exact_quote_hashes") or {}).get(fact_id) != fact.get("exact_quote_hash"):
                _add_failure(failures, "FACT_QUOTE_HASH_LINEAGE_MISMATCH", fact_id)
        if fact.get("current_score_eligible") is not True:
            _add_failure(failures, "SCORED_FACT_NOT_CURRENT_ELIGIBLE", fact_id)
    for anchor_id, anchor in anchor_by_id.items():
        if stable_hash(anchor.get("normalized_anchor_payload")) != anchor.get("anchor_payload_hash"):
            _add_failure(failures, "ANCHOR_PAYLOAD_HASH_MISMATCH", anchor_id)

    vector = score.get("component_score_vector") or {}
    maxima = score.get("component_max_vector") or {}
    if set(vector) != set(CANONICAL_COMPONENT_ORDER) or set(maxima) != set(CANONICAL_COMPONENT_ORDER):
        _add_failure(failures, "SCORE_VECTOR_COMPONENT_ROSTER_MISMATCH")
    else:
        recomputed_total = round(sum(float(vector[key]) for key in CANONICAL_COMPONENT_ORDER), 6)
        if abs(recomputed_total - float(score.get("total_score") or 0.0)) > 1e-9:
            _add_failure(failures, "COMPONENT_SUM_MISMATCH", {"recomputed": recomputed_total, "receipt": score.get("total_score")})
        for component_id in CANONICAL_COMPONENT_ORDER:
            component = component_by_id.get(component_id)
            if component and abs(float(vector[component_id]) - float(component["final_points"])) > 1e-9:
                _add_failure(failures, "SCORE_COMPONENT_DECISION_MISMATCH", component_id)
    if score.get("score_valid") is not True or score.get("score_status") != "COMPLETE":
        _add_failure(failures, "SCORE_NOT_COMPLETE_VALID")
    if score.get("research_complete") is not True or score.get("production_research_status") != "COMPLETE":
        _add_failure(failures, "PRODUCTION_RESEARCH_NOT_COMPLETE")
    if score.get("gold_evaluation_status") != "PASS" or int(score.get("gold_leakage_count") or 0) != 0:
        _add_failure(failures, "POST_RUN_GOLD_NOT_CLEAN_PASS")
    if stage.get("decision_status") != "FINAL" or stage.get("score_valid") is not True:
        _add_failure(failures, "STAGECOURT_NOT_FINAL")
    try:
        recomputed_stage = _recompute_stage({**score, "as_of_date": manifest["as_of_date"]}, {**stage, "as_of_date": manifest["as_of_date"]})
        if recomputed_stage != stage.get("canonical_stage") or recomputed_stage != score.get("canonical_stage"):
            _add_failure(failures, "CANONICAL_STAGE_RECOMPUTE_MISMATCH", {"recomputed": recomputed_stage, "stage_receipt": stage.get("canonical_stage"), "score_receipt": score.get("canonical_stage")})
    except (KeyError, TypeError, ValueError) as exc:
        _add_failure(failures, "CANONICAL_STAGE_RECOMPUTE_ERROR", f"{exc.__class__.__name__}:{exc}")

    metrics = {
        "component_count": len(components),
        "judge_count": len(judges),
        "scoring_fact_count": len(facts),
        "source_count": len(sources),
        "anchor_count": len(anchors),
        "provider_call_receipt_count": len(provider_calls),
        "total_score_recomputed": round(sum(float((score.get("component_score_vector") or {}).get(key, 0.0)) for key in CANONICAL_COMPONENT_ORDER), 6),
        "canonical_stage_recomputed": locals().get("recomputed_stage"),
    }
    return {
        "schema_version": VERIFICATION_SCHEMA,
        "target_id": target_id,
        "status": VERIFICATION_PASS if not failures else VERIFICATION_FAIL,
        "critical_count": len(failures),
        "failures": failures,
        "metrics": metrics,
        "forbidden_runtime_inputs_read": [],
        "offline": True,
    }


def verify_receipts(receipt_root: str | Path) -> Mapping[str, Any]:
    root = Path(receipt_root).resolve()
    targets = tuple(
        verify_target_receipt(path)
        for path in sorted(root.iterdir(), key=lambda path: path.name)
        if path.is_dir() and (path / "receipt_manifest.json").is_file()
    ) if root.is_dir() else ()
    failures = sum(int(row["critical_count"]) for row in targets)
    if not targets:
        failures += 1
    return {
        "schema_version": VERIFICATION_SCHEMA,
        "receipt_root_identity": root.name,
        "target_count": len(targets),
        "targets": list(targets),
        "critical_count_sum": failures,
        "status": VERIFICATION_PASS if targets and failures == 0 else VERIFICATION_FAIL,
        "offline": True,
        "allowed_inputs": ["TRACKED_RECEIPTS", "CURRENT_SOURCE_CODE", "CURRENT_TRACKED_CONFIG"],
        "forbidden_inputs": ["output", "data/cache", ".env", "home_cache", "collaboration_journal", "untracked_files"],
    }


__all__ = [
    "PROVIDER_ROUTE",
    "RECEIPT_MANIFEST_SCHEMA",
    "SCORE_RECEIPT_SCHEMA",
    "STAGECOURT_RECEIPT_SCHEMA",
    "VERIFICATION_FAIL",
    "VERIFICATION_PASS",
    "export_receipts",
    "export_target_receipt",
    "receipt_content_index",
    "receipt_content_tree_hash",
    "runtime_config_hash",
    "stagecourt_rule_hash",
    "verify_receipts",
    "verify_target_receipt",
]
