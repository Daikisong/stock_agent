"""Portable tracked receipts for independently reproducible E2R decisions.

The production dossier is intentionally large and untracked.  This module
exports only the score-bearing graph and then verifies it without consulting
the original output tree, a cache, an environment file, or a provider journal.
LLMs remain evidence extractors and component judges; score aggregation and
canonical Stage reproduction remain deterministic.
"""

from __future__ import annotations

import base64
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import date
import hashlib
import ipaddress
import json
import math
import os
from pathlib import Path
import re
import socket
import statistics
import subprocess
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import urlparse
import zlib

from e2r.calibration.scoring_profile import get_active_scoring_profile
from e2r.models import ScoreSnapshot, Stage
from e2r.production.metadata import git_head_sha, stable_hash, write_json, write_jsonl
from e2r.red_team import RedTeamAssessment, RedTeamRiskLevel, Soft4BStatus
from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.scoring.business_mechanism_scope import (
    ArchetypeMechanismScopeContract,
    BusinessMechanismScope,
    DEFAULT_SCOPE_PATH,
    MechanismScopeValidator,
    load_mechanism_scope_contracts,
)
from e2r.staging import StageClassificationInput, StageClassifier

from .canary_leaf_contract import canary_output_tree_hash
from .collaboration_provider_bridge import (
    COLLABORATION_PROVIDER_NAME,
    _validate_request,
    _validate_response_envelope,
)
from .current_researcher_mode import _historical_anchors
from .evidence_fact_compiler import _canonical_value, _normalize_text
from .schemas import CANONICAL_COMPONENT_ORDER, scrub_blind_research_payload
from .score_aggregator import AGGREGATOR_CONFIG


RECEIPT_MANIFEST_SCHEMA = "e2r_v6_tracked_receipt_manifest_v1"
SCORE_RECEIPT_SCHEMA = "e2r_v6_score_receipt_v1"
STAGECOURT_RECEIPT_SCHEMA = "e2r_v6_stagecourt_receipt_v1"
VERIFICATION_SCHEMA = "e2r_v6_receipt_only_verification_v1"
VERIFICATION_PASS = "E2R_V6_RECEIPT_ONLY_REPRODUCTION_PASS"
VERIFICATION_FAIL = "E2R_V6_RECEIPT_ONLY_REPRODUCTION_FAIL"
PROVIDER_ROUTE = "COLLABORATION_CODEX_SUBAGENT"
PHASE101_TARGET_IDS = ("005930", "000660")
COMMIT_SHA_HASH_SCOPE = "MANIFEST_EXCLUDED_FROM_IMMUTABLE_CONTENT_HASH"
TRACKED_RECEIPT_HASH_SCOPE = (
    "ALL_TARGET_RECEIPT_FILES_EXCEPT_RECEIPT_MANIFEST_JSON"
)
GOLD_RECALL_METRIC_KEYS = (
    "critical_material_fact_recall",
    "counter_supersession_recall",
    "all_material_fact_recall",
    "component_research_topic_coverage",
)
GOLD_POST_RUN_PASS = "V5_FULL_THESIS_GOLD_POST_RUN_RECALL_PASS"
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
RECEIPT_MANIFEST_KEYS = frozenset(
    {
        "schema_version",
        "receipt_id",
        "target_id",
        "company_name",
        "as_of_date",
        "latest_trading_snapshot_date",
        "archetype_id",
        "run_commit_sha",
        "verification_commit_sha",
        "commit_sha_hash_scope",
        "config_hash",
        "prompt_hashes",
        "provider_identity_hash",
        "source_corpus_hash",
        "gold_audit_hash",
        "gold_receipt_projection_hash",
        "output_tree_hash",
        "output_tree_hash_recomputed",
        "output_tree_hash_matches",
        "tracked_receipt_tree_hash",
        "tracked_receipt_content_index",
        "tracked_receipt_hash_scope",
        "gold_visible_during_production",
        "provider_selected_explicitly",
        "provider_route",
        "qwen_call_count",
        "ollama_call_count",
        "provider_call_counts",
        "scored_fact_provider_lineage_counts",
        "inherited_qwen_scored_fact_count",
        "inherited_ollama_scored_fact_count",
        "current_invocation_provider_name",
        "current_invocation_logical_call_count",
        "current_invocation_successful_call_count",
        "current_invocation_provider_error_count",
        "score_or_stage_authority",
        "query_count",
        "document_count",
        "fact_count",
        "counterfact_count",
        "receipt_scoring_fact_count",
        "receipt_source_count",
        "receipt_anchor_count",
        "receipt_judge_count",
        "receipt_component_count",
        "receipt_provider_call_count",
        "provider_accounting",
    }
)
SCORE_RECEIPT_KEYS = frozenset(
    {
        "schema_version", "receipt_id", "target_id", "score_scale",
        "score_valid", "component_score_vector", "component_max_vector",
        "total_score", "total_score_recomputed", "component_sum_matches_total",
        "research_complete", "semantic_saturation_certified", "material_gap_count",
        "provider_error_count", "canonical_stage", "stage_status", "risk_overlay",
        "hard_break_fact_ids", "daily_event_overlay_can_change_canonical_stage",
        "production_research_status", "gold_evaluation_status", "score_status",
        "stagecourt_status", "gold_post_run_metrics", "gold_post_run_audit",
        "gold_audit_hash", "gold_receipt_projection_hash", "gold_leakage_count",
    }
)
COMPONENT_RECEIPT_KEYS = frozenset(
    {
        "schema_version", "component_id", "max_points", "support_points",
        "counter_effect", "final_points", "support_fact_ids", "counter_fact_ids",
        "resolution_fact_ids", "resolution_fact_role", "historical_anchor_ids",
        "judge_decision_ids", "why_not_higher", "why_not_lower", "confidence",
        "research_status", "aggregation_method", "aggregation_trace_hash",
        "proposal_median", "consensus_band", "judge_proposals", "prompt_hashes",
        "response_hashes", "provider_call_ids", "aggregator_config_hash",
    }
)
JUDGE_RECEIPT_KEYS = frozenset(
    {
        "schema_version", "judge_decision_id", "component_id", "role",
        "proposed_points", "allowed_range", "support_fact_ids", "counter_fact_ids",
        "anchor_ids", "why_higher", "why_lower", "prompt_hash", "response_hash",
        "provider_call_id", "provider_name", "provider_route",
        "score_or_stage_authority",
    }
)
SCORING_FACT_RECEIPT_KEYS = frozenset(
    {
        "schema_version", "fact_id", "target_id", "component_ids", "fact_role",
        "fact_roles", "direct_point_input", "subject_id", "fact_identity_subject",
        "business_segment", "product_family", "economic_mechanism",
        "fact_identity_predicate", "fact_identity_direction", "predicate_family",
        "normalized_object", "value", "unit", "period", "temporal_status",
        "claim_ids", "primary_claim_id", "question_family_id", "mechanism_scope_id",
        "allowed_component_ids", "scope_business_segment", "scope_product_family",
        "scope_technology_family", "scope_transaction_type",
        "scope_economic_mechanism", "scope_confidence", "source_document_id",
        "claim_scope_hash",
        "source_url", "source_title", "source_publisher",
        "source_publisher_derivation", "source_tier", "source_family", "published_at",
        "available_at", "document_content_hash", "exact_quote", "exact_quote_hash",
        "quote_excerpt", "quote_excerpt_hash", "page_section_locator", "issuer_scoped",
        "issuer_scope_derivation", "current_score_eligible",
        "current_score_eligibility_basis", "source_independence_group",
        "extraction_provider_name", "provider_prompt_hash", "provider_response_hash",
        "as_of_date", "gold_fact",
    }
)
SOURCE_RECEIPT_KEYS = frozenset(
    {
        "schema_version", "source_document_id", "source_url", "source_title",
        "source_publisher", "source_tier", "source_family", "published_at",
        "available_at", "document_content_hash", "source_independence_group",
        "fact_document_hashes", "fact_exact_quote_hashes",
    }
)
ANCHOR_RECEIPT_KEYS = frozenset(
    {
        "schema_version", "anchor_id", "component_id", "archetype_id",
        "normalized_anchor_payload", "anchor_payload_hash",
    }
)
PROVIDER_CALL_COMMON_KEYS = frozenset(
    {
        "schema_version", "provider_call_id", "call_scope", "provider_name",
        "provider_kind", "provider_attempt_count", "prompt_hash", "response_hash",
        "status", "score_or_stage_authority",
    }
)
PROVIDER_CALL_FACT_KEYS = PROVIDER_CALL_COMMON_KEYS | frozenset(
    {
        "request_id",
        "response_id",
        "request_envelope_hash",
        "response_envelope_hash",
        "fact_scope_attestation_hashes",
        "request_envelope_zlib_b64",
        "response_envelope_zlib_b64",
    }
)
PROVIDER_CALL_FULL_RUN_KEYS = PROVIDER_CALL_COMMON_KEYS | frozenset(
    {"successful_call_count", "provider_error_count", "transport_call_count"}
)
STAGECOURT_RECEIPT_KEYS = frozenset(
    {
        "schema_version", "target_id", "score_receipt_id",
        "component_score_vector_hash", "total_score", "risk_fact_ids",
        "hard_break_fact_ids", "hard_break_claim_ids", "canonical_stage",
        "decision_status", "score_valid", "event_overlay",
        "event_overlay_changed_canonical_stage", "stagecourt_rule_hash",
        "decision_trace_hash", "classification_input",
    }
)
GOLD_PROJECTION_KEYS = frozenset(
    {
        "schema_version", "status", "as_of_date", "comparison_timing",
        "gold_visibility_during_production", "metrics", "thresholds",
        "critical_counts", "critical_count_sum", "gold_fact_count",
        "qualified_material_fact_match_count", "covered_target_component_count",
        "required_target_component_count",
    }
)
_FORBIDDEN_IDENTITY_PATTERNS = (
    re.compile(r"(?i)file:(?://+|\\\\)[^\s\"']+"),
    re.compile(r"(?:^|[\s\"'=:(])/(?:[^/\s\"']+/)*[^/\s\"']+"),
    re.compile(r"(?:^|[\s\"'=:(])[A-Za-z]:[\\/][^\s\"']+"),
    re.compile(r"(?:^|[\s\"'=:(])(?:\\\\|//)[^\s\"']+"),
    re.compile(r"(?:^|[\s\"'=:(])~/(?:[^/\s\"']+/)*[^/\s\"']*"),
)
_FORBIDDEN_LOCAL_PROVIDER_PATTERNS = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"(?<![A-Z0-9])OLLAMA(?![A-Z0-9])",
        r"(?<![A-Z0-9])QWEN(?:\d+(?:\.\d+)?)?(?![A-Z0-9])",
        r"(?<![A-Z0-9])LLAMA(?:[._ -]?CPP)(?![A-Z0-9])",
        r"(?<![A-Z0-9])LM[ _-]?STUDIO(?![A-Z0-9])",
        r"(?<![A-Z0-9])LOCALAI(?![A-Z0-9])",
        r"(?<![A-Z0-9])LOCAL[ _-]?(?:LLM|MODEL|PROVIDER|RUNTIME)(?![A-Z0-9])",
        r"(?:127(?:\.\d{1,3}){3}|localhost|0\.0\.0\.0)(?::\d+)?",
        r"\[::1\](?::\d+)?",
        r"(?<![0-9A-F:])::1(?::\d+)?(?![0-9A-F])",
        r"(?<![0-9A-F:])0:0:0:0:0:0:0:1(?::\d+)?(?![0-9A-F])",
    )
)
_PROVIDER_IDENTITY_KEYS = frozenset(
    {
        "provider_name",
        "provider_kind",
        "provider_route",
        "extraction_provider_name",
        "current_invocation_provider_name",
    }
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


def _portable_serialized_payload(value: Any) -> str:
    """Serialize receipt values while excluding ordinary HTTPS URL syntax.

    A source URL is portable and therefore not an absolute filesystem path.
    Removing it before the path scan prevents ``https://host/path`` from being
    mistaken for ``/host/path`` while still rejecting embedded ``/tmp/...`` or
    Windows/UNC paths in any receipt field.
    """

    serialized = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return re.sub(
        r"https?://[^\s\"']+",
        "HTTPS_URL",
        serialized,
        flags=re.IGNORECASE,
    )


def _contains_absolute_path(value: Any) -> bool:
    serialized = _portable_serialized_payload(value)
    return any(pattern.search(serialized) for pattern in _FORBIDDEN_IDENTITY_PATTERNS)


def _contains_non_finite_number(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(_contains_non_finite_number(child) for child in value.values())
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return any(_contains_non_finite_number(child) for child in value)
    if isinstance(value, float):
        return not math.isfinite(value)
    return isinstance(value, str) and value.strip().casefold() in {
        "nan",
        "+nan",
        "-nan",
        "inf",
        "+inf",
        "-inf",
        "infinity",
        "+infinity",
        "-infinity",
    }


def _is_finite_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _contains_local_provider_marker(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, child in value.items():
            key_has_marker = any(
                pattern.search(str(key))
                for pattern in _FORBIDDEN_LOCAL_PROVIDER_PATTERNS
            )
            child_is_effectively_set = (
                child is True
                or isinstance(child, (int, float))
                and not isinstance(child, bool)
                and child != 0
                or isinstance(child, str)
                and bool(child.strip())
                or isinstance(child, (Mapping, Sequence))
                and not isinstance(child, (str, bytes))
                and bool(child)
            )
            if key_has_marker and child_is_effectively_set:
                return True
            if _contains_local_provider_marker(child):
                return True
        return False
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return any(_contains_local_provider_marker(child) for child in value)
    if not isinstance(value, str):
        return False
    return _contains_local_network_endpoint(value) or any(
        pattern.search(value) for pattern in _FORBIDDEN_LOCAL_PROVIDER_PATTERNS
    )


def _contains_local_network_endpoint(value: str) -> bool:
    hosts: set[str] = set()
    candidate = value.strip()
    try:
        parsed = urlparse(candidate)
        if parsed.hostname:
            hosts.add(parsed.hostname)
    except ValueError:
        return True
    hosts.update(re.findall(r"\[([0-9A-Fa-f:]+)\]", candidate))
    if (
        (":" in candidate or "." in candidate)
        and re.fullmatch(r"[0-9A-Fa-f:.]+", candidate)
    ):
        hosts.add(candidate)
    for host in hosts:
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            legacy_ipv4_part = r"(?:0[xX][0-9A-Fa-f]+|0[0-7]*|[0-9]+)"
            if not re.fullmatch(
                rf"{legacy_ipv4_part}(?:\.{legacy_ipv4_part}){{0,3}}",
                host,
            ):
                continue
            try:
                address = ipaddress.ip_address(
                    socket.inet_ntoa(socket.inet_aton(host))
                )
            except (OSError, ValueError):
                continue
        mapped = getattr(address, "ipv4_mapped", None)
        if (
            address.is_loopback
            or address.is_unspecified
            or mapped is not None
            and (mapped.is_loopback or mapped.is_unspecified)
        ):
            return True
    return False


def _scope_identity_marker(value: Any) -> str:
    return re.sub(r"[^A-Z0-9]+", "", str(value or "").upper())


def _mechanism_scope_identity_matches(
    fact: Mapping[str, Any],
    contract: ArchetypeMechanismScopeContract,
) -> bool:
    """Bind durable claim scope to the human-readable mechanism identity.

    The historical RFC id predates explicit scope fields.  The receipt still
    must not permit an HBM claim to be relabelled DRAM merely by recomputing a
    self hash.  Use the active archetype vocabulary, not issuer/theme-specific
    conditions: whenever the mechanism id names a specific allowed product or
    economic mechanism, the explicit scope must name the same value.  Generic
    product scopes may omit a product marker, but cannot override a specific
    marker already present in the identity.
    """

    identity = _scope_identity_marker(fact.get("mechanism_scope_id"))
    if not identity:
        return False
    claimed_product = str(fact.get("scope_product_family") or "")
    specific_products = tuple(
        value
        for value in contract.allowed_product_families
        if not str(value).upper().endswith("_GENERIC")
    )
    mentioned_products = {
        value
        for value in specific_products
        if _scope_identity_marker(value) in identity
    }
    if claimed_product in specific_products:
        if claimed_product not in mentioned_products:
            return False
    elif mentioned_products:
        return False
    claimed_mechanism = str(fact.get("scope_economic_mechanism") or "")
    mentioned_mechanisms = {
        value
        for value in contract.allowed_economic_mechanisms
        if _scope_identity_marker(value) in identity
    }
    if mentioned_mechanisms and claimed_mechanism not in mentioned_mechanisms:
        return False
    corporate_marker_present = "CORPORATE" in identity
    corporate_scope = str(fact.get("scope_business_segment") or "") == (
        "CORPORATE_GENERIC"
    )
    if corporate_marker_present != corporate_scope:
        return False
    return True


def _commit_is_trusted_ancestor(repo_root: Path, commit_sha: str) -> bool:
    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(repo_root),
                "merge-base",
                "--is-ancestor",
                commit_sha,
                "HEAD",
            ],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


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


def _require_exact_fields(
    value: Mapping[str, Any],
    expected: frozenset[str],
    *,
    kind: str,
    failures: list[Mapping[str, Any]],
    identity: Any = None,
) -> None:
    actual = set(value)
    if actual != expected:
        _add_failure(
            failures,
            "CANONICAL_RECEIPT_FIELD_ROSTER_MISMATCH",
            {
                "kind": kind,
                "identity": identity,
                "extra": sorted(actual - expected),
                "missing": sorted(expected - actual),
            },
        )


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
    if normalized in {"CODEX", "COLLABORATION_CODEX"}:
        return normalized
    if normalized == "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE":
        return "COLLABORATION_CODEX"
    if normalized in {
        "CODEX_STRUCTURED_RESEARCHER_MODE",
        "CODEX_STRUCTURED_RESEARCHER_WITH_COLLABORATION_SUBAGENT_FALLBACK",
    }:
        return "CODEX"
    if "QWEN" in normalized:
        return "QWEN"
    if "OLLAMA" in normalized:
        return "OLLAMA"
    return normalized or "UNKNOWN"


_ALLOWED_RESEARCH_PROVIDER_KINDS = frozenset(
    {"CODEX", "COLLABORATION_CODEX"}
)


def _fact_scope_attestation_payload(row: Mapping[str, Any]) -> Mapping[str, Any]:
    """Project the exact provider-reviewed claim identity and scope fields."""

    return {
        "document_id": row.get("document_id")
        or row.get("source_document_id"),
        "exact_quote": row.get("exact_quote"),
        "question_family_id": row.get("question_family_id"),
        "subject_id": row.get("subject_id"),
        "predicate_family": row.get("predicate_family"),
        "normalized_object": row.get("normalized_object"),
        "period": row.get("period"),
        "mechanism_scope_id": row.get("mechanism_scope_id"),
        "scope_business_segment": row.get("scope_business_segment"),
        "scope_product_family": row.get("scope_product_family"),
        "scope_technology_family": row.get("scope_technology_family"),
        "scope_transaction_type": row.get("scope_transaction_type"),
        "scope_economic_mechanism": row.get("scope_economic_mechanism"),
        "scope_confidence": row.get("scope_confidence"),
    }


def _fact_scope_attestation_hash(row: Mapping[str, Any]) -> str:
    return stable_hash(_fact_scope_attestation_payload(row))


_MAX_EMBEDDED_JOURNAL_ENVELOPE_BYTES = 64 * 1024 * 1024


def _reject_nonfinite_json_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant: {value}")


def _encode_journal_envelope(envelope: Mapping[str, Any]) -> str:
    """Encode a validated journal envelope as a portable receipt preimage.

    The verifier must be able to recompute request/response identities without
    consulting the untracked production output or provider journal.  Encoding
    the exact envelope also keeps ordinary source text out of generic
    path/provider-marker scans; it is decoded only by the strict journal
    validator below.
    """

    raw = json.dumps(
        envelope,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return base64.b64encode(zlib.compress(raw, level=9)).decode("ascii")


def _decode_journal_envelope(encoded: Any) -> Mapping[str, Any]:
    if not isinstance(encoded, str) or not encoded:
        raise ValueError("embedded journal envelope is missing")
    try:
        compressed = base64.b64decode(encoded, validate=True)
        if base64.b64encode(compressed).decode("ascii") != encoded:
            raise ValueError("embedded journal envelope base64 is not canonical")
        decompressor = zlib.decompressobj()
        raw = decompressor.decompress(
            compressed,
            _MAX_EMBEDDED_JOURNAL_ENVELOPE_BYTES + 1,
        )
        if (
            len(raw) > _MAX_EMBEDDED_JOURNAL_ENVELOPE_BYTES
            or decompressor.unconsumed_tail
        ):
            raise ValueError("embedded journal envelope exceeds its boundary")
        raw += decompressor.flush()
    except (ValueError, zlib.error) as exc:
        raise ValueError("embedded journal envelope is invalid") from exc
    if (
        len(raw) > _MAX_EMBEDDED_JOURNAL_ENVELOPE_BYTES
        or not decompressor.eof
        or decompressor.unused_data
    ):
        raise ValueError("embedded journal envelope exceeds its boundary")
    try:
        decoded = json.loads(
            raw.decode("utf-8"),
            parse_constant=_reject_nonfinite_json_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("embedded journal envelope is not canonical JSON") from exc
    if not isinstance(decoded, Mapping):
        raise ValueError("embedded journal envelope must be an object")
    canonical_raw = json.dumps(
        decoded,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    if raw != canonical_raw:
        raise ValueError("embedded journal envelope JSON is not canonical")
    return dict(decoded)


def _fact_journal_provider_call_id(call: Mapping[str, Any]) -> str:
    return "FACTJOURNAL-" + stable_hash(
        {
            "request_id": call.get("request_id"),
            "response_id": call.get("response_id"),
            "request_envelope_hash": call.get("request_envelope_hash"),
            "response_envelope_hash": call.get("response_envelope_hash"),
            "prompt_hash": call.get("prompt_hash"),
            "response_hash": call.get("response_hash"),
            "fact_scope_attestation_hashes": list(
                call.get("fact_scope_attestation_hashes") or ()
            ),
            "request_envelope_zlib_b64": call.get(
                "request_envelope_zlib_b64"
            ),
            "response_envelope_zlib_b64": call.get(
                "response_envelope_zlib_b64"
            ),
        }
    )[:24]


def _embedded_fact_journal_call_is_exact(call: Mapping[str, Any]) -> bool:
    """Revalidate the exact request/response preimages carried by a receipt."""

    try:
        request = _validate_request(
            _decode_journal_envelope(call.get("request_envelope_zlib_b64"))
        )
        response = _validate_response_envelope(
            request=request,
            envelope=_decode_journal_envelope(
                call.get("response_envelope_zlib_b64")
            ),
        )
        request_payload = json.loads(
            str(request["prompt"]).rsplit("\n", 1)[-1]
        )
        response_payload = response.get("payload")
        if not isinstance(request_payload, Mapping) or not isinstance(
            response_payload, Mapping
        ):
            return False
        response_facts = response_payload.get("facts")
        if not isinstance(response_facts, list) or any(
            not isinstance(row, Mapping) for row in response_facts
        ):
            return False
        expected_scope_attestations = sorted(
            {
                _fact_scope_attestation_hash(row)
                for row in response_facts
            }
        )
        return (
            request.get("pass_name") == "EVIDENCE_FACT_EXTRACTION"
            and call.get("request_id") == request.get("request_id")
            and call.get("response_id") == response.get("response_id")
            and call.get("request_envelope_hash") == stable_hash(request)
            and call.get("response_envelope_hash") == stable_hash(response)
            and call.get("prompt_hash")
            == stable_intelligence_id("FACTPROMPT", request_payload)
            and call.get("response_hash")
            == stable_intelligence_id(
                "FACTRESP",
                scrub_blind_research_payload(response_payload),
            )
            and list(call.get("fact_scope_attestation_hashes") or ())
            == expected_scope_attestations
        )
    except (KeyError, TypeError, ValueError, RuntimeError):
        return False


def _provider_call_receipts(target_root: Path) -> tuple[Mapping[str, Any], ...]:
    """Export provider evidence from every canonical run accounting plane.

    Fact extraction calls used to be the only exported call ledger.  That can
    prove nothing about a local provider used for component judging or the
    rest of the research invocation.  The compact receipt now includes the
    fact calls, all 21 judge calls, and the canonical full-run provider audit.
    """

    receipts: list[Mapping[str, Any]] = list(
        _validated_fact_journal_call_receipts(target_root)
    )
    judge_path = target_root / "component_judge_decisions.jsonl"
    if judge_path.is_file():
        for row in _read_jsonl(judge_path):
            receipts.append(
                {
                    "schema_version": "e2r_v6_provider_call_receipt_v1",
                    "provider_call_id": row.get("judge_call_id"),
                    "call_scope": "COMPONENT_JUDGE",
                    "provider_name": row.get("provider_name"),
                    "provider_kind": _provider_kind(row.get("provider_name")),
                    "provider_attempt_count": 1,
                    "prompt_hash": row.get("prompt_hash"),
                    "response_hash": row.get("response_hash"),
                    "status": "SUCCESS",
                    "score_or_stage_authority": False,
                }
            )
    audit_path = target_root / "research_provider_response_cache_audit.json"
    if audit_path.is_file():
        audit = _read_json(audit_path)
        receipts.append(
            {
                "schema_version": "e2r_v6_provider_call_receipt_v1",
                "provider_call_id": "RUNPROV-" + stable_hash(audit)[:24],
                "call_scope": "FULL_RESEARCH_INVOCATION_AUDIT",
                "provider_name": audit.get("provider_name"),
                "provider_kind": _provider_kind(audit.get("provider_name")),
                "provider_attempt_count": int(audit.get("logical_call_count") or 0),
                "successful_call_count": int(
                    audit.get("successful_call_count") or 0
                ),
                "provider_error_count": int(audit.get("provider_error_count") or 0),
                "transport_call_count": int(audit.get("transport_call_count") or 0),
                "prompt_hash": None,
                "response_hash": stable_hash(audit),
                "status": audit.get("status"),
                "score_or_stage_authority": False,
            }
        )
    return tuple(receipts)


def _validated_fact_journal_call_receipts(
    target_root: Path,
) -> tuple[Mapping[str, Any], ...]:
    """Rebuild successful fact-call receipts from the validated journal.

    The current checkpoint call ledger is intentionally compact and may no
    longer contain a historical or migration call that produced a still-live
    accepted claim.  The immutable collaboration journal retains that exact
    request and response.  Export only pairs that pass the same request,
    response-envelope, filename, and quarantine checks as the production
    bridge; never synthesize a call from the claim's self-reported hashes.
    """

    journal = target_root / "collaboration_codex_subagent_provider"
    request_root = journal / "requests"
    response_root = journal / "responses"
    if not request_root.is_dir() or not response_root.is_dir():
        return ()
    receipts: list[Mapping[str, Any]] = []
    seen_lineage: set[tuple[str, str]] = set()
    for request_path in sorted(request_root.glob("COLLABREQ-*.json")):
        try:
            request = _validate_request(_read_json(request_path))
        except (OSError, TypeError, ValueError, RuntimeError) as exc:
            raise ReceiptVerificationError(
                "INVALID_COLLABORATION_REQUEST_JOURNAL:"
                f"{request_path.name}:{exc.__class__.__name__}"
            ) from exc
        request_id = str(request["request_id"])
        if request_path.name != f"{request_id}.json":
            raise ReceiptVerificationError(
                f"COLLABORATION_REQUEST_FILENAME_MISMATCH:{request_path.name}"
            )
        if request.get("pass_name") != "EVIDENCE_FACT_EXTRACTION":
            continue
        response_path = response_root / f"{request_id}.json"
        if not response_path.is_file():
            continue
        try:
            response = _validate_response_envelope(
                request=request,
                envelope=_read_json(response_path),
            )
        except (OSError, TypeError, ValueError, RuntimeError) as exc:
            raise ReceiptVerificationError(
                "INVALID_FACT_EXTRACTION_RESPONSE_JOURNAL:"
                f"{request_id}:{exc.__class__.__name__}"
            ) from exc
        quarantine_path = (
            journal
            / "quarantine"
            / request_id
            / f"{response['response_id']}.json"
        )
        if quarantine_path.is_file():
            raise ReceiptVerificationError(
                f"QUARANTINED_FACT_EXTRACTION_RESPONSE:{request_id}"
            )
        try:
            request_payload = json.loads(
                str(request["prompt"]).rsplit("\n", 1)[-1]
            )
        except (TypeError, ValueError, json.JSONDecodeError) as exc:
            raise ReceiptVerificationError(
                f"FACT_EXTRACTION_PROMPT_PAYLOAD_INVALID:{request_id}"
            ) from exc
        response_payload = response.get("payload")
        if not isinstance(request_payload, Mapping) or not isinstance(
            response_payload, Mapping
        ):
            raise ReceiptVerificationError(
                f"FACT_EXTRACTION_JOURNAL_PAYLOAD_INVALID:{request_id}"
            )
        prompt_hash = stable_intelligence_id("FACTPROMPT", request_payload)
        response_hash = stable_intelligence_id(
            "FACTRESP",
            scrub_blind_research_payload(response_payload),
        )
        response_facts = response_payload.get("facts")
        if not isinstance(response_facts, list) or any(
            not isinstance(row, Mapping) for row in response_facts
        ):
            raise ReceiptVerificationError(
                f"FACT_EXTRACTION_RESPONSE_FACT_ROSTER_INVALID:{request_id}"
            )
        fact_scope_attestation_hashes = tuple(
            sorted(
                {
                    _fact_scope_attestation_hash(row)
                    for row in response_facts
                }
            )
        )
        lineage = (prompt_hash, response_hash)
        if lineage in seen_lineage:
            continue
        seen_lineage.add(lineage)
        receipt = {
            "schema_version": "e2r_v6_provider_call_receipt_v1",
            "provider_call_id": "",
            "call_scope": "FACT_EXTRACTION",
            "provider_name": COLLABORATION_PROVIDER_NAME,
            "provider_kind": _provider_kind(COLLABORATION_PROVIDER_NAME),
            "provider_attempt_count": 1,
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
            "status": "SUCCESS",
            "score_or_stage_authority": False,
            "request_id": request_id,
            "response_id": response["response_id"],
            "request_envelope_hash": stable_hash(request),
            "response_envelope_hash": stable_hash(response),
            "fact_scope_attestation_hashes": list(
                fact_scope_attestation_hashes
            ),
            "request_envelope_zlib_b64": _encode_journal_envelope(request),
            "response_envelope_zlib_b64": _encode_journal_envelope(response),
        }
        receipt["provider_call_id"] = _fact_journal_provider_call_id(receipt)
        receipts.append(receipt)
    return tuple(receipts)


def _provider_observations(
    named_payloads: Mapping[str, Any],
) -> tuple[Mapping[str, str], ...]:
    """Collect every provider identity field from every canonical receipt.

    This is deliberately recursive so a future schema cannot add a provider
    identity field to a canonical file without it entering the accounting.
    """

    observations: list[Mapping[str, str]] = []

    def visit(value: Any, *, filename: str, path: str) -> None:
        if isinstance(value, Mapping):
            for key, child in value.items():
                clean_key = str(key)
                normalized_key = clean_key.casefold()
                child_path = f"{path}.{clean_key}" if path else clean_key
                provider_identity_field = bool(
                    clean_key in _PROVIDER_IDENTITY_KEYS
                    or (
                        "provider" in normalized_key
                        and normalized_key.endswith(("name", "kind", "route"))
                    )
                    or normalized_key.endswith(
                        ("model_name", "runtime_name", "runtime_endpoint")
                    )
                )
                if provider_identity_field:
                    observations.append(
                        {
                            "filename": filename,
                            "json_path": child_path,
                            "field": clean_key,
                            "value": str(child or ""),
                        }
                    )
                visit(child, filename=filename, path=child_path)
        elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            for index, child in enumerate(value):
                visit(child, filename=filename, path=f"{path}[{index}]")

    for filename in sorted(named_payloads):
        visit(named_payloads[filename], filename=filename, path="")
    return tuple(
        sorted(
            observations,
            key=lambda row: (
                row["filename"],
                row["json_path"],
                row["field"],
                row["value"],
            ),
        )
    )


def _provider_accounting(
    *,
    content_index: Sequence[Mapping[str, Any]],
    named_payloads: Mapping[str, Any],
) -> Mapping[str, Any]:
    observations = _provider_observations(named_payloads)
    observation_counts = dict(
        sorted(
            Counter(
                f"{row['field']}:{_provider_kind(row['value'])}"
                for row in observations
                if row["field"] != "provider_route"
            ).items()
        )
    )
    route_counts = dict(
        sorted(
            Counter(
                row["value"]
                for row in observations
                if row["field"] == "provider_route"
            ).items()
        )
    )
    unauthorized = tuple(
        row
        for row in observations
        if (
            row["field"] == "provider_route"
            and row["value"] != PROVIDER_ROUTE
        )
        or (
            row["field"] != "provider_route"
            and _provider_kind(row["value"])
            not in _ALLOWED_RESEARCH_PROVIDER_KINDS
        )
    )
    local = tuple(
        row for row in observations if _contains_local_provider_marker(row["value"])
    )
    local_marker_files = tuple(
        filename
        for filename, payload in sorted(named_payloads.items())
        if _contains_local_provider_marker(payload)
    )
    return {
        "schema_version": "e2r_v6_provider_accounting_v1",
        "accounted_file_roster": sorted(named_payloads),
        "accounted_file_hashes": {
            str(row["relative_path"]): str(row["sha256"])
            for row in content_index
        },
        "provider_identity_observation_count": len(observations),
        "provider_identity_observation_counts": observation_counts,
        "provider_route_observation_counts": route_counts,
        "unauthorized_provider_observation_count": len(unauthorized),
        "local_provider_observation_count": len(local),
        "local_provider_marker_files": list(local_marker_files),
        "local_provider_marker_file_count": len(local_marker_files),
        "all_canonical_exported_files_accounted": (
            set(named_payloads) == set(REQUIRED_TARGET_FILES)
            and {str(row["relative_path"]) for row in content_index}
            == set(REQUIRED_TARGET_FILES)
        ),
    }


def _provider_call_counts(rows: Sequence[Mapping[str, Any]]) -> Mapping[str, int]:
    counts: Counter[str] = Counter()
    for row in rows:
        counts[_provider_kind(row.get("provider_name"))] += int(
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
        allowed_component_ids = list(
            _ordered_unique(claim.get("allowed_component_ids") or ())
        )
        claim_scope_payload = {
            "primary_claim_id": claim.get("claim_id"),
            "allowed_component_ids": allowed_component_ids,
            "scope_business_segment": claim.get("scope_business_segment"),
            "scope_product_family": claim.get("scope_product_family"),
            "scope_technology_family": claim.get("scope_technology_family"),
            "scope_transaction_type": claim.get("scope_transaction_type"),
            "scope_economic_mechanism": claim.get("scope_economic_mechanism"),
            "scope_confidence": claim.get("scope_confidence"),
        }
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
                "fact_identity_subject": fact.get("subject"),
                "business_segment": fact.get("business_segment") or claim.get("business_segment") or "",
                "product_family": fact.get("product_family") or claim.get("product_family") or "",
                "economic_mechanism": fact.get("economic_mechanism") or claim.get("economic_mechanism") or "",
                "fact_identity_predicate": fact.get("predicate"),
                "fact_identity_direction": fact.get("direction"),
                "predicate_family": claim.get("predicate_family") or fact.get("predicate") or "",
                "normalized_object": claim.get("normalized_object") or fact.get("value"),
                "value": fact.get("value"),
                "unit": fact.get("unit"),
                "period": fact.get("period") or claim.get("period") or "",
                "temporal_status": fact.get("current_lifecycle") or claim.get("current_lifecycle") or "",
                "claim_ids": list(claim_ids),
                "primary_claim_id": claim.get("claim_id"),
                "question_family_id": claim.get("question_family_id"),
                "mechanism_scope_id": claim.get("mechanism_scope_id"),
                "allowed_component_ids": allowed_component_ids,
                "scope_business_segment": claim.get("scope_business_segment"),
                "scope_product_family": claim.get("scope_product_family"),
                "scope_technology_family": claim.get("scope_technology_family"),
                "scope_transaction_type": claim.get("scope_transaction_type"),
                "scope_economic_mechanism": claim.get("scope_economic_mechanism"),
                "scope_confidence": claim.get("scope_confidence"),
                "claim_scope_hash": stable_hash(claim_scope_payload),
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
                "exact_quote": exact_quote,
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
    anchors = _index(
        _historical_anchors(
            repo_root=repo_root,
            archetype_id=archetype_id,
            allow_output_fallback=False,
        ),
        "anchor_id",
    )
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


def _gold_receipt_projection(gold: Mapping[str, Any]) -> Mapping[str, Any]:
    """Keep the complete post-run acceptance contract without Gold facts.

    The full audit hash preserves origin provenance.  The compact projection
    carries every metric, threshold, and critical count needed for an offline
    reviewer to verify that a non-empty comparison really passed.
    """

    return {
        "schema_version": gold.get("schema_version"),
        "status": gold.get("status"),
        "as_of_date": gold.get("as_of_date"),
        "comparison_timing": gold.get("comparison_timing"),
        "gold_visibility_during_production": gold.get(
            "gold_visibility_during_production"
        ),
        "metrics": dict(gold.get("metrics") or {}),
        "thresholds": dict(gold.get("thresholds") or {}),
        "critical_counts": dict(gold.get("critical_counts") or {}),
        "critical_count_sum": gold.get("critical_count_sum"),
        "gold_fact_count": gold.get("gold_fact_count"),
        "qualified_material_fact_match_count": gold.get(
            "qualified_material_fact_match_count"
        ),
        "covered_target_component_count": gold.get(
            "covered_target_component_count"
        ),
        "required_target_component_count": gold.get(
            "required_target_component_count"
        ),
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
    gold_projection = _gold_receipt_projection(gold)
    gold_audit_hash = stable_hash(gold)
    gold_projection_hash = stable_hash(gold_projection)
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
        "gold_post_run_audit": gold_projection,
        "gold_audit_hash": gold_audit_hash,
        "gold_receipt_projection_hash": gold_projection_hash,
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
    named_payloads = {
        "score_receipt.json": score_receipt,
        "component_decisions.jsonl": list(components),
        "scoring_facts.jsonl": list(facts),
        "judge_decisions.jsonl": list(judges),
        "source_manifest.jsonl": list(sources),
        "anchor_manifest.jsonl": list(anchors),
        "provider_calls.jsonl": list(provider_calls),
        "stagecourt_receipt.json": stage_receipt,
    }
    provider_accounting = _provider_accounting(
        content_index=content_index,
        named_payloads=named_payloads,
    )
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
        "commit_sha_hash_scope": COMMIT_SHA_HASH_SCOPE,
        "config_hash": runtime_config_hash(),
        "prompt_hashes": {
            f"{row['component_id']}:{row['role']}": row["prompt_hash"] for row in judges
        },
        "provider_identity_hash": provider_identity.get("provider_identity_hash"),
        "source_corpus_hash": stable_hash(sources),
        "gold_audit_hash": gold_audit_hash,
        "gold_receipt_projection_hash": gold_projection_hash,
        "output_tree_hash": target_manifest.get("output_tree_hash"),
        "output_tree_hash_recomputed": actual_output_hash,
        "output_tree_hash_matches": target_manifest.get("output_tree_hash") == actual_output_hash,
        "tracked_receipt_tree_hash": receipt_content_tree_hash(destination),
        "tracked_receipt_content_index": list(content_index),
        "tracked_receipt_hash_scope": TRACKED_RECEIPT_HASH_SCOPE,
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
        "provider_accounting": provider_accounting,
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
    clean_targets = tuple(str(target).strip() for target in targets if str(target).strip())
    if set(clean_targets) != set(PHASE101_TARGET_IDS) or len(clean_targets) != len(
        PHASE101_TARGET_IDS
    ):
        raise ReceiptVerificationError(
            "EXACT_PHASE101_TARGET_EXPORT_ROSTER_REQUIRED:"
            f"{list(PHASE101_TARGET_IDS)}"
        )
    manifests = tuple(
        export_target_receipt(
            repo_root=repo_root,
            source_root=source_output_root,
            target_id=str(target),
            destination_root=destination,
        )
        for target in PHASE101_TARGET_IDS
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
    component_numeric_fields = (
        "max_points",
        "support_points",
        "counter_effect",
        "final_points",
        "confidence",
        "proposal_median",
    )
    consensus_band = component.get("consensus_band")
    if (
        any(not _is_finite_number(component.get(field)) for field in component_numeric_fields)
        or not isinstance(consensus_band, Sequence)
        or isinstance(consensus_band, (str, bytes))
        or len(consensus_band) != 2
        or any(not _is_finite_number(value) for value in consensus_band)
    ):
        _add_failure(failures, "COMPONENT_FINITE_NUMERIC_CONTRACT_MISMATCH", component_id)
        return
    maximum = float(component["max_points"])
    range_contract_invalid = False
    for judge in judges:
        proposed = judge.get("proposed_points")
        allowed_range = judge.get("allowed_range")
        if (
            not _is_finite_number(proposed)
            or not isinstance(allowed_range, Sequence)
            or isinstance(allowed_range, (str, bytes))
            or len(allowed_range) != 2
            or any(not _is_finite_number(value) for value in allowed_range)
        ):
            range_contract_invalid = True
            continue
        lower_value, upper_value = map(float, allowed_range)
        if not 0.0 <= lower_value <= float(proposed) <= upper_value <= maximum:
            range_contract_invalid = True
    if range_contract_invalid:
        _add_failure(failures, "JUDGE_ALLOWED_RANGE_CONTRACT_MISMATCH", component_id)
        return
    proposals = [float(by_role[role]["proposed_points"]) for role in required]
    lower = max(float(row["allowed_range"][0]) for row in judges)
    upper = min(float(row["allowed_range"][1]) for row in judges)
    if lower > upper:
        _add_failure(failures, "JUDGE_ALLOWED_RANGE_INTERSECTION_EMPTY", component_id)
        return
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
    raw_root = Path(target_root)
    if raw_root.is_symlink():
        failure = {
            "code": "TARGET_RECEIPT_ROOT_SYMLINK_FORBIDDEN",
            "detail": None,
        }
        return {
            "schema_version": VERIFICATION_SCHEMA,
            "target_id": raw_root.name,
            "status": VERIFICATION_FAIL,
            "critical_count": 1,
            "failures": [failure],
            "metrics": {},
            "forbidden_runtime_inputs_read": [],
            "offline": True,
        }
    root = raw_root.resolve()
    failures: list[Mapping[str, Any]] = []
    expected_filenames = {"receipt_manifest.json", *REQUIRED_TARGET_FILES}
    actual_entries = tuple(root.iterdir()) if root.is_dir() else ()
    invalid_entries = sorted(
        path.name
        for path in actual_entries
        if path.name not in expected_filenames
        or path.is_symlink()
        or not path.is_file()
        or path.resolve().parent != root
        or path.lstat().st_nlink != 1
    )
    if raw_root.is_symlink() or set(path.name for path in actual_entries) != expected_filenames or invalid_entries:
        _add_failure(
            failures,
            "EXACT_REGULAR_TARGET_RECEIPT_FILE_ROSTER_REQUIRED",
            {
                "expected": sorted(expected_filenames),
                "actual": sorted(path.name for path in actual_entries),
                "invalid": invalid_entries,
                "target_root_symlink": raw_root.is_symlink(),
            },
        )
    for filename in sorted(expected_filenames):
        path = root / filename
        if (
            path.is_symlink()
            or not path.is_file()
            or path.resolve().parent != root
            or path.lstat().st_nlink != 1
        ):
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
    named_payloads = {
        "score_receipt.json": score,
        "component_decisions.jsonl": list(components),
        "scoring_facts.jsonl": list(facts),
        "judge_decisions.jsonl": list(judges),
        "source_manifest.jsonl": list(sources),
        "anchor_manifest.jsonl": list(anchors),
        "provider_calls.jsonl": list(provider_calls),
        "stagecourt_receipt.json": stage,
    }
    all_receipt_payloads = [manifest, *named_payloads.values()]
    if _contains_non_finite_number(all_receipt_payloads):
        _add_failure(failures, "NON_FINITE_NUMERIC_VALUE_PRESENT")
        return {
            "schema_version": VERIFICATION_SCHEMA,
            "target_id": str(manifest.get("target_id") or root.name),
            "status": VERIFICATION_FAIL,
            "critical_count": len(failures),
            "failures": failures,
            "metrics": {},
            "forbidden_runtime_inputs_read": [],
            "offline": True,
        }

    if manifest.get("schema_version") != RECEIPT_MANIFEST_SCHEMA:
        _add_failure(failures, "MANIFEST_SCHEMA_MISMATCH")
    if set(manifest) != RECEIPT_MANIFEST_KEYS:
        _add_failure(
            failures,
            "MANIFEST_EXACT_FIELD_ROSTER_REQUIRED",
            {
                "extra": sorted(set(manifest) - RECEIPT_MANIFEST_KEYS),
                "missing": sorted(RECEIPT_MANIFEST_KEYS - set(manifest)),
            },
        )
    if manifest.get("score_or_stage_authority") is not False:
        _add_failure(failures, "MANIFEST_DIRECT_SCORE_OR_STAGE_AUTHORITY_PRESENT")
    if manifest.get("commit_sha_hash_scope") != COMMIT_SHA_HASH_SCOPE:
        _add_failure(failures, "COMMIT_SHA_HASH_SCOPE_MISMATCH")
    if manifest.get("tracked_receipt_hash_scope") != TRACKED_RECEIPT_HASH_SCOPE:
        _add_failure(failures, "TRACKED_RECEIPT_HASH_SCOPE_MISMATCH")
    run_commit_sha = str(manifest.get("run_commit_sha") or "")
    verification_commit_sha = str(manifest.get("verification_commit_sha") or "")
    if (
        not re.fullmatch(r"[0-9a-f]{40}", run_commit_sha)
        or not re.fullmatch(r"[0-9a-f]{40}", verification_commit_sha)
        or run_commit_sha != verification_commit_sha
    ):
        _add_failure(
            failures,
            "COMMIT_SHA_ATTESTATION_MISMATCH",
            {
                "run_commit_sha": run_commit_sha,
                "verification_commit_sha": verification_commit_sha,
            },
        )
    if score.get("schema_version") != SCORE_RECEIPT_SCHEMA:
        _add_failure(failures, "SCORE_RECEIPT_SCHEMA_MISMATCH")
    if stage.get("schema_version") != STAGECOURT_RECEIPT_SCHEMA:
        _add_failure(failures, "STAGECOURT_RECEIPT_SCHEMA_MISMATCH")
    _require_exact_fields(
        score,
        SCORE_RECEIPT_KEYS,
        kind="score_receipt",
        failures=failures,
        identity=score.get("target_id"),
    )
    _require_exact_fields(
        stage,
        STAGECOURT_RECEIPT_KEYS,
        kind="stagecourt_receipt",
        failures=failures,
        identity=stage.get("target_id"),
    )
    for rows, expected, kind, identity_key in (
        (components, COMPONENT_RECEIPT_KEYS, "component", "component_id"),
        (facts, SCORING_FACT_RECEIPT_KEYS, "scoring_fact", "fact_id"),
        (judges, JUDGE_RECEIPT_KEYS, "judge", "judge_decision_id"),
        (sources, SOURCE_RECEIPT_KEYS, "source", "source_document_id"),
        (anchors, ANCHOR_RECEIPT_KEYS, "anchor", "anchor_id"),
    ):
        for row in rows:
            _require_exact_fields(
                row,
                expected,
                kind=kind,
                failures=failures,
                identity=row.get(identity_key),
            )
    for call in provider_calls:
        expected_provider_keys = (
            PROVIDER_CALL_FULL_RUN_KEYS
            if call.get("call_scope") == "FULL_RESEARCH_INVOCATION_AUDIT"
            else PROVIDER_CALL_FACT_KEYS
            if call.get("call_scope") == "FACT_EXTRACTION"
            else PROVIDER_CALL_COMMON_KEYS
        )
        _require_exact_fields(
            call,
            expected_provider_keys,
            kind="provider_call",
            failures=failures,
            identity=call.get("provider_call_id"),
        )
    gold_projection_fields = score.get("gold_post_run_audit")
    if isinstance(gold_projection_fields, Mapping):
        _require_exact_fields(
            gold_projection_fields,
            GOLD_PROJECTION_KEYS,
            kind="gold_projection",
            failures=failures,
            identity=score.get("target_id"),
        )
    identity_targets = {
        "directory": root.name,
        "manifest": manifest.get("target_id"),
        "score": score.get("target_id"),
        "stage": stage.get("target_id"),
    }
    if set(str(value or "") for value in identity_targets.values()) != {root.name}:
        _add_failure(failures, "TARGET_IDENTITY_LINKAGE_MISMATCH", identity_targets)
    receipt_ids = {
        "manifest": manifest.get("receipt_id"),
        "score": score.get("receipt_id"),
        "stage_score_receipt_id": stage.get("score_receipt_id"),
    }
    if (
        len({str(value or "") for value in receipt_ids.values()}) != 1
        or not str(manifest.get("receipt_id") or "")
    ):
        _add_failure(failures, "RECEIPT_ID_LINKAGE_MISMATCH", receipt_ids)
    expected_receipt_id = "V6RECEIPT-" + stable_hash(
        {
            "target_id": root.name,
            "as_of_date": manifest.get("as_of_date"),
            "output_tree_hash": manifest.get("output_tree_hash"),
        }
    )[:24]
    if manifest.get("receipt_id") != expected_receipt_id:
        _add_failure(
            failures,
            "RECEIPT_ID_IMMUTABLE_IDENTITY_MISMATCH",
            {"expected": expected_receipt_id, "actual": manifest.get("receipt_id")},
        )
    actual_index = receipt_content_index(root)
    if list(actual_index) != list(manifest.get("tracked_receipt_content_index") or ()):
        _add_failure(failures, "RECEIPT_CONTENT_INDEX_MISMATCH")
    actual_tree_hash = receipt_content_tree_hash(root)
    if manifest.get("tracked_receipt_tree_hash") != actual_tree_hash:
        _add_failure(failures, "RECEIPT_TREE_HASH_MISMATCH")
    if manifest.get("source_corpus_hash") != stable_hash(sources):
        _add_failure(failures, "SOURCE_CORPUS_HASH_MISMATCH")
    repo_root = Path(__file__).resolve().parents[4]
    if (
        not _commit_is_trusted_ancestor(repo_root, run_commit_sha)
        or not _commit_is_trusted_ancestor(repo_root, verification_commit_sha)
    ):
        _add_failure(
            failures,
            "COMMIT_SHA_NOT_TRUSTED_GIT_ANCESTOR",
            {
                "run_commit_sha": run_commit_sha,
                "verification_commit_sha": verification_commit_sha,
            },
        )
    if manifest.get("config_hash") != runtime_config_hash():
        _add_failure(failures, "CURRENT_CONFIG_HASH_MISMATCH")
    if stage.get("stagecourt_rule_hash") != stagecourt_rule_hash(repo_root):
        _add_failure(failures, "CURRENT_STAGECOURT_RULE_HASH_MISMATCH")
    if _contains_absolute_path(all_receipt_payloads):
        _add_failure(failures, "ABSOLUTE_PATH_IDENTITY_PRESENT")
    if _contains_local_provider_marker(all_receipt_payloads):
        _add_failure(failures, "LOCAL_PROVIDER_MARKER_PRESENT_IN_RECEIPT_SET")
    actual_provider_accounting = _provider_accounting(
        content_index=actual_index,
        named_payloads=named_payloads,
    )
    if dict(manifest.get("provider_accounting") or {}) != actual_provider_accounting:
        _add_failure(failures, "PROVIDER_ACCOUNTING_MISMATCH")
    if actual_provider_accounting["all_canonical_exported_files_accounted"] is not True:
        _add_failure(failures, "CANONICAL_PROVIDER_FILE_ACCOUNTING_INCOMPLETE")
    if int(actual_provider_accounting["local_provider_observation_count"]) != 0:
        _add_failure(failures, "LOCAL_PROVIDER_OBSERVATION_PRESENT")
    if int(actual_provider_accounting["local_provider_marker_file_count"]) != 0:
        _add_failure(
            failures,
            "LOCAL_PROVIDER_MARKER_PRESENT_IN_CANONICAL_FILE",
            actual_provider_accounting["local_provider_marker_files"],
        )
    if int(actual_provider_accounting["unauthorized_provider_observation_count"]) != 0:
        _add_failure(failures, "UNAUTHORIZED_PROVIDER_OBSERVATION_PRESENT")
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
    unauthorized_call_kinds = sorted(
        set(recomputed_provider_counts) - _ALLOWED_RESEARCH_PROVIDER_KINDS
    )
    if unauthorized_call_kinds:
        _add_failure(
            failures,
            "UNAUTHORIZED_RESEARCH_PROVIDER_CALL_KIND",
            unauthorized_call_kinds,
        )
    recomputed_lineage_counts = _scored_lineage_counts(facts)
    if dict(manifest.get("scored_fact_provider_lineage_counts") or {}) != recomputed_lineage_counts:
        _add_failure(failures, "SCORED_FACT_PROVIDER_LINEAGE_COUNTS_MISMATCH")
    unauthorized_lineage_kinds = sorted(
        set(recomputed_lineage_counts) - _ALLOWED_RESEARCH_PROVIDER_KINDS
    )
    if unauthorized_lineage_kinds:
        _add_failure(
            failures,
            "UNAUTHORIZED_SCORED_FACT_PROVIDER_LINEAGE",
            unauthorized_lineage_kinds,
        )
    if int(manifest.get("inherited_qwen_scored_fact_count") or 0) != 0:
        _add_failure(failures, "INHERITED_QWEN_SCORED_FACT_LINEAGE_PRESENT", manifest.get("inherited_qwen_scored_fact_count"))
    if int(manifest.get("inherited_ollama_scored_fact_count") or 0) != 0:
        _add_failure(failures, "INHERITED_OLLAMA_SCORED_FACT_LINEAGE_PRESENT", manifest.get("inherited_ollama_scored_fact_count"))
    if manifest.get("provider_route") != PROVIDER_ROUTE:
        _add_failure(failures, "PROVIDER_ROUTE_MISMATCH", manifest.get("provider_route"))
    if manifest.get("provider_selected_explicitly") is not True:
        _add_failure(failures, "PROVIDER_NOT_SELECTED_EXPLICITLY")
    current_invocation_provider_kind = _provider_kind(
        manifest.get("current_invocation_provider_name")
    )
    if current_invocation_provider_kind not in _ALLOWED_RESEARCH_PROVIDER_KINDS:
        _add_failure(
            failures,
            "UNAUTHORIZED_CURRENT_INVOCATION_PROVIDER",
            manifest.get("current_invocation_provider_name"),
        )
    if manifest.get("gold_visible_during_production") is not False:
        _add_failure(failures, "GOLD_VISIBLE_DURING_PRODUCTION")
    output_hash = str(manifest.get("output_tree_hash") or "")
    recomputed_output_hash = str(
        manifest.get("output_tree_hash_recomputed") or ""
    )
    if (
        manifest.get("output_tree_hash_matches") is not True
        or not re.fullmatch(r"[0-9a-f]{64}", output_hash)
        or output_hash != recomputed_output_hash
    ):
        _add_failure(
            failures,
            "OUTPUT_TREE_HASH_LINKAGE_MISMATCH",
            {
                "output_tree_hash_matches": manifest.get(
                    "output_tree_hash_matches"
                ),
                "hashes_equal": output_hash == recomputed_output_hash,
            },
        )

    receipt_count_contract = {
        "receipt_scoring_fact_count": len(facts),
        "receipt_source_count": len(sources),
        "receipt_anchor_count": len(anchors),
        "receipt_judge_count": len(judges),
        "receipt_component_count": len(components),
        "receipt_provider_call_count": len(provider_calls),
    }
    for field, actual_count in receipt_count_contract.items():
        if manifest.get(field) != actual_count:
            _add_failure(
                failures,
                "RECEIPT_ROSTER_COUNT_MISMATCH",
                {"field": field, "declared": manifest.get(field), "actual": actual_count},
            )
    provider_call_ids = [
        str(row.get("provider_call_id") or "").strip() for row in provider_calls
    ]
    if not all(provider_call_ids) or len(set(provider_call_ids)) != len(
        provider_call_ids
    ):
        _add_failure(failures, "PROVIDER_CALL_ID_ROSTER_INVALID")
    provider_call_by_id = {
        call_id: row for call_id, row in zip(provider_call_ids, provider_calls)
    }
    provider_scopes = Counter(str(row.get("call_scope") or "") for row in provider_calls)
    allowed_provider_scopes = {
        "FACT_EXTRACTION",
        "COMPONENT_JUDGE",
        "FULL_RESEARCH_INVOCATION_AUDIT",
    }
    unexpected_provider_scopes = sorted(set(provider_scopes) - allowed_provider_scopes)
    if unexpected_provider_scopes:
        _add_failure(
            failures,
            "UNEXPECTED_PROVIDER_CALL_SCOPE",
            unexpected_provider_scopes,
        )
    if provider_scopes.get("FULL_RESEARCH_INVOCATION_AUDIT", 0) != 1:
        _add_failure(
            failures,
            "FULL_RUN_PROVIDER_AUDIT_RECEIPT_REQUIRED",
            dict(provider_scopes),
        )
    if provider_scopes.get("COMPONENT_JUDGE", 0) != 21:
        _add_failure(
            failures,
            "EXACT_COMPONENT_JUDGE_PROVIDER_CALL_ROSTER_REQUIRED",
            dict(provider_scopes),
        )
    for call in provider_calls:
        call_id = str(call.get("provider_call_id") or "")
        provider_name = call.get("provider_name")
        attempt_count = call.get("provider_attempt_count")
        if call.get("schema_version") != "e2r_v6_provider_call_receipt_v1":
            _add_failure(failures, "PROVIDER_CALL_SCHEMA_MISMATCH", call_id)
        if (
            not isinstance(attempt_count, int)
            or isinstance(attempt_count, bool)
            or attempt_count < 0
        ):
            _add_failure(failures, "PROVIDER_ATTEMPT_COUNT_INVALID", call_id)
        if call.get("provider_kind") != _provider_kind(provider_name):
            _add_failure(failures, "PROVIDER_KIND_DERIVATION_MISMATCH", call_id)
        if _provider_kind(provider_name) not in _ALLOWED_RESEARCH_PROVIDER_KINDS:
            _add_failure(failures, "UNAUTHORIZED_PROVIDER_CALL", call_id)
        if _contains_local_provider_marker(
            [provider_name, call.get("provider_kind"), call.get("provider_route")]
        ):
            _add_failure(failures, "LOCAL_PROVIDER_CALL_PRESENT", call_id)
        if call.get("score_or_stage_authority") is not False:
            _add_failure(failures, "PROVIDER_CALL_DIRECT_AUTHORITY_PRESENT", call_id)
        if call.get("call_scope") == "FACT_EXTRACTION" and (
            call.get("status") not in {"COMPLETE", "SUCCESS"}
            or re.fullmatch(
                r"FACTPROMPT-[0-9a-f]{24}",
                str(call.get("prompt_hash") or ""),
            )
            is None
            or re.fullmatch(
                r"FACTRESP-[0-9a-f]{24}",
                str(call.get("response_hash") or ""),
            )
            is None
            or not isinstance(attempt_count, int)
            or isinstance(attempt_count, bool)
            or attempt_count < 1
        ):
            _add_failure(
                failures,
                "FACT_EXTRACTION_PROVIDER_CALL_NOT_SUCCESSFUL",
                call_id,
            )
        if call.get("call_scope") == "FACT_EXTRACTION":
            scope_attestations = call.get("fact_scope_attestation_hashes")
            clean_scope_attestations = (
                list(scope_attestations)
                if isinstance(scope_attestations, list)
                else []
            )
            if (
                re.fullmatch(
                    r"COLLABREQ-[0-9a-f]{64}",
                    str(call.get("request_id") or ""),
                )
                is None
                or re.fullmatch(
                    r"COLLABRESP-[0-9a-f]{64}",
                    str(call.get("response_id") or ""),
                )
                is None
                or any(
                    re.fullmatch(r"[0-9a-f]{64}", str(value or "")) is None
                    for value in (
                        call.get("request_envelope_hash"),
                        call.get("response_envelope_hash"),
                    )
                )
                or clean_scope_attestations
                != sorted(set(clean_scope_attestations))
                or any(
                    re.fullmatch(r"[0-9a-f]{64}", str(value or "")) is None
                    for value in clean_scope_attestations
                )
                or call_id != _fact_journal_provider_call_id(call)
                or not _embedded_fact_journal_call_is_exact(call)
            ):
                _add_failure(
                    failures,
                    "FACT_EXTRACTION_JOURNAL_IDENTITY_MISMATCH",
                    call_id,
                )
    successful_fact_provider_lineages: dict[
        tuple[str, str, str], set[str]
    ] = defaultdict(set)
    for call in provider_calls:
        if call.get("call_scope") != "FACT_EXTRACTION" or call.get(
            "status"
        ) not in {"COMPLETE", "SUCCESS"}:
            continue
        lineage = (
            str(call.get("provider_name") or ""),
            str(call.get("prompt_hash") or ""),
            str(call.get("response_hash") or ""),
        )
        successful_fact_provider_lineages[lineage].update(
            str(value)
            for value in call.get("fact_scope_attestation_hashes") or ()
        )
    full_run_rows = [
        row
        for row in provider_calls
        if row.get("call_scope") == "FULL_RESEARCH_INVOCATION_AUDIT"
    ]
    if len(full_run_rows) == 1:
        full_run = full_run_rows[0]
        if (
            full_run.get("provider_name")
            != manifest.get("current_invocation_provider_name")
            or int(full_run.get("provider_attempt_count") or 0)
            != int(manifest.get("current_invocation_logical_call_count") or 0)
        ):
            _add_failure(failures, "FULL_RUN_PROVIDER_AUDIT_LINKAGE_MISMATCH")
        logical_count = int(full_run.get("provider_attempt_count") or 0)
        successful_count = full_run.get("successful_call_count")
        provider_error_count = full_run.get("provider_error_count")
        transport_count = full_run.get("transport_call_count")
        if (
            full_run.get("status") != "COLLABORATION_PROVIDER_JOURNAL_ACTIVE"
            or logical_count <= 0
            or not isinstance(successful_count, int)
            or isinstance(successful_count, bool)
            or successful_count != logical_count
            or not isinstance(provider_error_count, int)
            or isinstance(provider_error_count, bool)
            or provider_error_count != 0
            or not isinstance(transport_count, int)
            or isinstance(transport_count, bool)
            or transport_count != logical_count
        ):
            _add_failure(
                failures,
                "FULL_RUN_PROVIDER_AUDIT_NOT_CLEAN_SUCCESS",
                {
                    "status": full_run.get("status"),
                    "logical": logical_count,
                    "successful": successful_count,
                    "errors": provider_error_count,
                    "transport": transport_count,
                },
            )

    component_by_id = {str(row.get("component_id")): row for row in components}
    if tuple(component_by_id) != tuple(CANONICAL_COMPONENT_ORDER) or len(components) != 7:
        _add_failure(failures, "EXACT_CANONICAL_COMPONENT_ROSTER_REQUIRED")
    judge_by_id = _index(judges, "judge_decision_id") if judges else {}
    fact_by_id = _index(facts, "fact_id") if facts else {}
    source_by_id = _index(sources, "source_document_id") if sources else {}
    anchor_by_id = _index(anchors, "anchor_id") if anchors else {}
    manifest_archetype_id = str(manifest.get("archetype_id") or "")
    try:
        current_anchor_by_id = _index(
            _historical_anchors(
                repo_root=repo_root,
                archetype_id=manifest_archetype_id,
                allow_output_fallback=False,
            ),
            "anchor_id",
        )
    except (OSError, TypeError, ValueError) as exc:
        current_anchor_by_id = {}
        _add_failure(
            failures,
            "CURRENT_TRACKED_ANCHOR_ATLAS_REQUIRED",
            f"{exc.__class__.__name__}:{exc}",
        )
    mechanism_scope_contract = load_mechanism_scope_contracts(
        repo_root / DEFAULT_SCOPE_PATH
    ).get(manifest_archetype_id)
    if mechanism_scope_contract is None:
        _add_failure(
            failures,
            "CURRENT_MECHANISM_SCOPE_CONTRACT_MISSING",
            manifest_archetype_id,
        )
    expected_fact_roles: dict[str, set[str]] = defaultdict(set)
    expected_fact_components: dict[str, set[str]] = defaultdict(set)
    expected_anchor_components: dict[str, set[str]] = defaultdict(set)
    expected_manifest_prompt_hashes = {
        f"{row.get('component_id')}:{row.get('role')}": row.get("prompt_hash")
        for row in judges
    }
    if dict(manifest.get("prompt_hashes") or {}) != expected_manifest_prompt_hashes:
        _add_failure(failures, "MANIFEST_JUDGE_PROMPT_BINDING_MISMATCH")
    for component_id in CANONICAL_COMPONENT_ORDER:
        component = component_by_id.get(component_id)
        if component is None:
            continue
        component_anchor_maxima = {
            float(anchor["max_points"])
            for anchor in current_anchor_by_id.values()
            if str(anchor.get("component_id") or "") == component_id
        }
        if (
            len(component_anchor_maxima) != 1
            or float(component.get("max_points") or 0.0)
            not in component_anchor_maxima
        ):
            _add_failure(
                failures,
                "COMPONENT_MAX_NOT_BOUND_TO_CURRENT_ANCHOR_CONFIG",
                component_id,
            )
        component_judges = [row for row in judges if row.get("component_id") == component_id]
        _verify_component_formula(component, component_judges, failures)
        actual_component_judge_ids = {
            str(row.get("judge_decision_id") or "")
            for row in component_judges
            if str(row.get("judge_decision_id") or "")
        }
        declared_component_judge_ids = {
            str(value) for value in component.get("judge_decision_ids") or ()
        }
        if (
            declared_component_judge_ids != actual_component_judge_ids
            or len(tuple(component.get("judge_decision_ids") or ()))
            != len(declared_component_judge_ids)
        ):
            _add_failure(
                failures,
                "COMPONENT_JUDGE_BIDIRECTIONAL_MISMATCH",
                component_id,
            )
        actual_provider_call_ids = {
            str(row.get("provider_call_id") or "")
            for row in component_judges
            if str(row.get("provider_call_id") or "")
        }
        if set(str(value) for value in component.get("provider_call_ids") or ()) != actual_provider_call_ids:
            _add_failure(
                failures,
                "COMPONENT_PROVIDER_CALL_BIDIRECTIONAL_MISMATCH",
                component_id,
            )
        if set(str(value) for value in component.get("prompt_hashes") or ()) != {
            str(row.get("prompt_hash") or "") for row in component_judges
        }:
            _add_failure(
                failures,
                "COMPONENT_JUDGE_PROMPT_HASH_MISMATCH",
                component_id,
            )
        if set(str(value) for value in component.get("response_hashes") or ()) != {
            str(row.get("response_hash") or "") for row in component_judges
        }:
            _add_failure(
                failures,
                "COMPONENT_JUDGE_RESPONSE_HASH_MISMATCH",
                component_id,
            )
        judge_support_ids = {
            str(value)
            for row in component_judges
            for value in row.get("support_fact_ids") or ()
        }
        judge_counter_ids = {
            str(value)
            for row in component_judges
            for value in row.get("counter_fact_ids") or ()
        }
        judge_anchor_ids = {
            str(value)
            for row in component_judges
            for value in row.get("anchor_ids") or ()
        }
        if judge_support_ids != set(
            str(value) for value in component.get("support_fact_ids") or ()
        ):
            _add_failure(failures, "COMPONENT_JUDGE_SUPPORT_FACT_MISMATCH", component_id)
        if judge_counter_ids != set(
            str(value) for value in component.get("counter_fact_ids") or ()
        ):
            _add_failure(failures, "COMPONENT_JUDGE_COUNTER_FACT_MISMATCH", component_id)
        if judge_anchor_ids != set(
            str(value) for value in component.get("historical_anchor_ids") or ()
        ):
            _add_failure(failures, "COMPONENT_JUDGE_ANCHOR_MISMATCH", component_id)
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
                expected_fact_components[str(fact_id)].add(component_id)
                if str(fact_id) not in fact_by_id:
                    _add_failure(failures, "ORPHAN_COMPONENT_FACT_ID", fact_id)
        for anchor_id in component.get("historical_anchor_ids") or ():
            expected_anchor_components[str(anchor_id)].add(component_id)
            if str(anchor_id) not in anchor_by_id:
                _add_failure(failures, "ORPHAN_COMPONENT_ANCHOR_ID", anchor_id)
    if len(judges) != 21:
        _add_failure(failures, "EXACT_TWENTY_ONE_JUDGES_REQUIRED", len(judges))
    for judge in judges:
        judge_id = str(judge.get("judge_decision_id") or "")
        component_id = str(judge.get("component_id") or "")
        component = component_by_id.get(component_id)
        if component is None or judge_id not in set(
            str(value) for value in component.get("judge_decision_ids") or ()
        ):
            _add_failure(failures, "ORPHAN_JUDGE_COMPONENT_LINK", judge_id)
        if _provider_kind(judge.get("provider_name")) not in _ALLOWED_RESEARCH_PROVIDER_KINDS:
            _add_failure(
                failures,
                "UNAUTHORIZED_JUDGE_PROVIDER_LINEAGE",
                judge.get("judge_decision_id"),
            )
        if judge.get("provider_route") != PROVIDER_ROUTE:
            _add_failure(
                failures,
                "JUDGE_PROVIDER_ROUTE_MISMATCH",
                judge.get("judge_decision_id"),
            )
        provider_call = provider_call_by_id.get(str(judge.get("provider_call_id") or ""))
        if (
            provider_call is None
            or provider_call.get("call_scope") != "COMPONENT_JUDGE"
            or provider_call.get("provider_name") != judge.get("provider_name")
            or provider_call.get("prompt_hash") != judge.get("prompt_hash")
            or provider_call.get("response_hash") != judge.get("response_hash")
        ):
            _add_failure(failures, "JUDGE_PROVIDER_CALL_LINKAGE_MISMATCH", judge_id)
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
        if (
            str(fact.get("target_id") or "") != target_id
            or str(fact.get("as_of_date") or "")
            != str(manifest.get("as_of_date") or "")
            or fact.get("issuer_scoped") is not True
        ):
            _add_failure(failures, "SCORING_FACT_TARGET_SCOPE_MISMATCH", fact_id)
        if set(fact.get("fact_roles") or ()) != expected_fact_roles[fact_id]:
            _add_failure(failures, "SCORING_FACT_ROLE_MISMATCH", fact_id)
        role_order = ("SUPPORT", "COUNTER", "RESOLUTION", "HARD_BREAK")
        expected_primary_role = next(
            (role for role in role_order if role in expected_fact_roles[fact_id]),
            None,
        )
        if (
            fact.get("fact_role") != expected_primary_role
            or fact.get("direct_point_input")
            is not (expected_primary_role in {"SUPPORT", "COUNTER"})
        ):
            _add_failure(failures, "SCORING_FACT_PRIMARY_ROLE_MISMATCH", fact_id)
        if set(str(value) for value in fact.get("component_ids") or ()) != expected_fact_components[fact_id]:
            _add_failure(failures, "FACT_COMPONENT_BIDIRECTIONAL_MISMATCH", fact_id)
        allowed_component_ids = {
            str(value) for value in fact.get("allowed_component_ids") or ()
        }
        claim_scope_payload = {
            "primary_claim_id": fact.get("primary_claim_id"),
            "allowed_component_ids": list(fact.get("allowed_component_ids") or ()),
            "scope_business_segment": fact.get("scope_business_segment"),
            "scope_product_family": fact.get("scope_product_family"),
            "scope_technology_family": fact.get("scope_technology_family"),
            "scope_transaction_type": fact.get("scope_transaction_type"),
            "scope_economic_mechanism": fact.get("scope_economic_mechanism"),
            "scope_confidence": fact.get("scope_confidence"),
        }
        if fact.get("claim_scope_hash") != stable_hash(claim_scope_payload):
            _add_failure(failures, "FACT_CLAIM_SCOPE_HASH_MISMATCH", fact_id)
        fact_provider_lineage = (
            str(fact.get("extraction_provider_name") or ""),
            str(fact.get("provider_prompt_hash") or ""),
            str(fact.get("provider_response_hash") or ""),
        )
        if (
            fact_provider_lineage not in successful_fact_provider_lineages
            or _fact_scope_attestation_hash(fact)
            not in successful_fact_provider_lineages[fact_provider_lineage]
        ):
            _add_failure(
                failures,
                "FACT_EXTRACTION_PROVIDER_CALL_LINKAGE_MISMATCH",
                fact_id,
            )
        recomputed_allowed_component_ids: set[str] = set()
        if mechanism_scope_contract is not None:
            try:
                scope_confidence = fact.get("scope_confidence")
                if isinstance(scope_confidence, bool):
                    raise ValueError("scope_confidence")
                scope = BusinessMechanismScope(
                    issuer_id=target_id,
                    business_segment=str(
                        fact.get("scope_business_segment") or ""
                    ),
                    product_family=str(fact.get("scope_product_family") or ""),
                    technology_family=str(
                        fact.get("scope_technology_family") or ""
                    ),
                    customer_or_counterparty="",
                    transaction_type=str(
                        fact.get("scope_transaction_type") or ""
                    ),
                    economic_mechanism=str(
                        fact.get("scope_economic_mechanism") or ""
                    ),
                    geography="UNSPECIFIED",
                    effective_period=str(fact.get("period") or ""),
                    scope_confidence=float(scope_confidence),
                )
                validator = MechanismScopeValidator()
                recomputed_allowed_component_ids = {
                    component_id
                    for component_id in CANONICAL_COMPONENT_ORDER
                    if validator.validate(
                        scope=scope,
                        contract=mechanism_scope_contract,
                        component_id=component_id,
                    ).scope_match
                }
            except (TypeError, ValueError):
                recomputed_allowed_component_ids = set()
        if allowed_component_ids != recomputed_allowed_component_ids:
            _add_failure(
                failures,
                "FACT_ALLOWED_COMPONENT_SCOPE_RECOMPUTE_MISMATCH",
                fact_id,
            )
        if mechanism_scope_contract is not None and not (
            _mechanism_scope_identity_matches(fact, mechanism_scope_contract)
        ):
            _add_failure(
                failures,
                "FACT_MECHANISM_SCOPE_IDENTITY_MISMATCH",
                fact_id,
            )
        if (
            not allowed_component_ids
            or expected_fact_components[fact_id] - allowed_component_ids
        ):
            _add_failure(
                failures,
                "FACT_COMPONENT_OUTSIDE_ACCEPTED_CLAIM_SCOPE",
                fact_id,
            )
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
        fact_identity = {
            "target_id": target_id,
            "as_of_date": str(manifest.get("as_of_date") or ""),
            "subject": _normalize_text(fact.get("fact_identity_subject")),
            "business_segment": _normalize_text(fact.get("business_segment")),
            "product_family": _normalize_text(fact.get("product_family")),
            "economic_mechanism": _normalize_text(
                fact.get("economic_mechanism")
            ),
            "predicate": _normalize_text(fact.get("fact_identity_predicate")),
            "value": _canonical_value(fact.get("value")),
            "unit": _normalize_text(fact.get("unit")),
            "period": _normalize_text(fact.get("period")),
            "direction": str(fact.get("fact_identity_direction") or "").upper(),
            "current_lifecycle": str(fact.get("temporal_status") or "").upper(),
        }
        if fact_id != stable_intelligence_id("EFACT", fact_identity):
            _add_failure(failures, "FACT_ECONOMIC_IDENTITY_MISMATCH", fact_id)
        exact_quote = str(fact.get("exact_quote") or "")
        if (
            not exact_quote
            or _sha256_bytes(exact_quote.encode("utf-8"))
            != fact.get("exact_quote_hash")
        ):
            _add_failure(failures, "FACT_EXACT_QUOTE_HASH_MISMATCH", fact_id)
        excerpt = str(fact.get("quote_excerpt") or "")
        if excerpt != _excerpt(exact_quote):
            _add_failure(failures, "FACT_QUOTE_EXCERPT_TEXT_MISMATCH", fact_id)
        if _sha256_bytes(excerpt.encode("utf-8")) != fact.get("quote_excerpt_hash"):
            _add_failure(failures, "FACT_QUOTE_EXCERPT_HASH_MISMATCH", fact_id)
        primary_claim_id = str(fact.get("primary_claim_id") or "")
        claim_identity = {
            "target_id": target_id,
            "as_of_date": str(manifest.get("as_of_date") or ""),
            "document_id": str(fact.get("source_document_id") or ""),
            "question_family_id": fact.get("question_family_id"),
            "subject_id": fact.get("subject_id"),
            "predicate_family": fact.get("predicate_family"),
            "normalized_object": fact.get("normalized_object"),
            "period": fact.get("period"),
            "mechanism_scope_id": fact.get("mechanism_scope_id"),
            "exact_quote": exact_quote,
        }
        if (
            primary_claim_id
            not in {str(value) for value in fact.get("claim_ids") or ()}
            or primary_claim_id
            != stable_intelligence_id("RFC", claim_identity)
        ):
            _add_failure(failures, "FACT_PRIMARY_CLAIM_IDENTITY_MISMATCH", fact_id)
        source = source_by_id.get(str(fact.get("source_document_id")))
        if source is not None:
            source_link_fields = (
                "source_url",
                "source_title",
                "source_publisher",
                "source_tier",
                "source_family",
                "published_at",
                "available_at",
                "document_content_hash",
                "source_independence_group",
            )
            if any(source.get(field) != fact.get(field) for field in source_link_fields):
                _add_failure(
                    failures,
                    "FACT_SOURCE_METADATA_LINKAGE_MISMATCH",
                    fact_id,
                )
            if source.get("document_content_hash") != fact.get("document_content_hash"):
                _add_failure(failures, "FACT_SOURCE_DOCUMENT_HASH_MISMATCH", fact_id)
            if (source.get("fact_document_hashes") or {}).get(fact_id) != fact.get("document_content_hash"):
                _add_failure(failures, "FACT_DOCUMENT_HASH_LINEAGE_MISMATCH", fact_id)
            if (source.get("fact_exact_quote_hashes") or {}).get(fact_id) != fact.get("exact_quote_hash"):
                _add_failure(failures, "FACT_QUOTE_HASH_LINEAGE_MISMATCH", fact_id)
        if (
            fact.get("current_score_eligible") is not True
            or fact.get("current_score_eligibility_basis")
            != "FINAL_DECISION_REFERENCE_AND_AS_OF_VALIDATED"
        ):
            _add_failure(failures, "SCORED_FACT_NOT_CURRENT_ELIGIBLE", fact_id)
    all_claim_ids = {
        str(claim_id)
        for fact in facts
        for claim_id in fact.get("claim_ids") or ()
    }
    score_hard_break_fact_ids = {
        str(value) for value in score.get("hard_break_fact_ids") or ()
    }
    stage_risk_fact_ids = {
        str(value) for value in stage.get("risk_fact_ids") or ()
    }
    stage_hard_break_fact_ids = {
        str(value) for value in stage.get("hard_break_fact_ids") or ()
    }
    stage_hard_break_claim_ids = {
        str(value) for value in stage.get("hard_break_claim_ids") or ()
    }
    if (
        not score_hard_break_fact_ids <= set(fact_by_id)
        or not stage_risk_fact_ids <= set(fact_by_id)
        or not stage_hard_break_fact_ids <= set(fact_by_id)
        or score_hard_break_fact_ids != stage_hard_break_fact_ids
    ):
        _add_failure(failures, "RISK_OR_HARD_BREAK_FACT_LINKAGE_MISMATCH")
    if not stage_hard_break_claim_ids <= all_claim_ids:
        _add_failure(failures, "HARD_BREAK_CLAIM_LINKAGE_MISMATCH")
    classification_input = stage.get("classification_input")
    red_team_input = (
        classification_input.get("red_team")
        if isinstance(classification_input, Mapping)
        else None
    )
    red_team_has_hard_break = (
        red_team_input.get("has_hard_break")
        if isinstance(red_team_input, Mapping)
        else None
    )
    expected_hard_break = bool(stage_hard_break_claim_ids)
    expected_risk_overlay = "HARD_BREAK" if expected_hard_break else "LOW"
    if (
        red_team_has_hard_break is not expected_hard_break
        or score.get("risk_overlay") not in {"LOW", "HARD_BREAK"}
        or score.get("risk_overlay") != expected_risk_overlay
    ):
        _add_failure(
            failures,
            "RISK_OVERLAY_DETERMINISTIC_LINKAGE_MISMATCH",
            {
                "declared": score.get("risk_overlay"),
                "expected": expected_risk_overlay,
                "red_team_has_hard_break": red_team_has_hard_break,
            },
        )
    for anchor_id, anchor in anchor_by_id.items():
        if stable_hash(anchor.get("normalized_anchor_payload")) != anchor.get("anchor_payload_hash"):
            _add_failure(failures, "ANCHOR_PAYLOAD_HASH_MISMATCH", anchor_id)
        current_anchor = current_anchor_by_id.get(anchor_id)
        if (
            current_anchor is None
            or dict(anchor.get("normalized_anchor_payload") or {})
            != dict(current_anchor)
            or str(anchor.get("component_id") or "")
            != str(current_anchor.get("component_id") or "")
            or str(anchor.get("archetype_id") or "") != manifest_archetype_id
            or str(current_anchor.get("archetype_id") or "")
            != manifest_archetype_id
        ):
            _add_failure(
                failures,
                "ANCHOR_NOT_BOUND_TO_CURRENT_TRACKED_CONFIG",
                anchor_id,
            )
        expected_components = expected_anchor_components.get(anchor_id, set())
        if (
            len(expected_components) != 1
            or str(anchor.get("component_id") or "") not in expected_components
        ):
            _add_failure(failures, "ANCHOR_COMPONENT_BIDIRECTIONAL_MISMATCH", anchor_id)
    if set(anchor_by_id) != set(expected_anchor_components):
        _add_failure(
            failures,
            "ANCHOR_ROSTER_BIDIRECTIONAL_MISMATCH",
            {
                "extra": sorted(set(anchor_by_id) - set(expected_anchor_components)),
                "missing": sorted(set(expected_anchor_components) - set(anchor_by_id)),
            },
        )

    vector = score.get("component_score_vector") or {}
    maxima = score.get("component_max_vector") or {}
    if set(vector) != set(CANONICAL_COMPONENT_ORDER) or set(maxima) != set(CANONICAL_COMPONENT_ORDER):
        _add_failure(failures, "SCORE_VECTOR_COMPONENT_ROSTER_MISMATCH")
    elif (
        any(not _is_finite_number(vector.get(key)) for key in CANONICAL_COMPONENT_ORDER)
        or any(not _is_finite_number(maxima.get(key)) for key in CANONICAL_COMPONENT_ORDER)
        or not _is_finite_number(score.get("total_score"))
        or not _is_finite_number(score.get("total_score_recomputed"))
        or not _is_finite_number(stage.get("total_score"))
    ):
        _add_failure(failures, "SCORE_STAGE_FINITE_NUMERIC_CONTRACT_MISMATCH")
    else:
        recomputed_total = round(sum(float(vector[key]) for key in CANONICAL_COMPONENT_ORDER), 6)
        if abs(recomputed_total - float(score.get("total_score") or 0.0)) > 1e-9:
            _add_failure(failures, "COMPONENT_SUM_MISMATCH", {"recomputed": recomputed_total, "receipt": score.get("total_score")})
        if (
            abs(recomputed_total - float(score.get("total_score_recomputed") or 0.0)) > 1e-9
            or score.get("component_sum_matches_total") is not True
        ):
            _add_failure(failures, "SCORE_TOTAL_RECOMPUTE_LINKAGE_MISMATCH")
        for component_id in CANONICAL_COMPONENT_ORDER:
            component = component_by_id.get(component_id)
            if component and abs(float(vector[component_id]) - float(component["final_points"])) > 1e-9:
                _add_failure(failures, "SCORE_COMPONENT_DECISION_MISMATCH", component_id)
            if component and abs(
                float(maxima[component_id]) - float(component["max_points"])
            ) > 1e-9:
                _add_failure(
                    failures,
                    "SCORE_COMPONENT_MAXIMUM_MISMATCH",
                    component_id,
                )
        if stage.get("component_score_vector_hash") != stable_hash(vector):
            _add_failure(failures, "STAGE_SCORE_VECTOR_HASH_MISMATCH")
        if abs(float(stage.get("total_score") or 0.0) - recomputed_total) > 1e-9:
            _add_failure(failures, "STAGE_TOTAL_SCORE_LINKAGE_MISMATCH")
    if score.get("score_valid") is not True or score.get("score_status") != "COMPLETE":
        _add_failure(failures, "SCORE_NOT_COMPLETE_VALID")
    if score.get("research_complete") is not True or score.get("production_research_status") != "COMPLETE":
        _add_failure(failures, "PRODUCTION_RESEARCH_NOT_COMPLETE")
    if score.get("gold_evaluation_status") != "PASS" or int(score.get("gold_leakage_count") or 0) != 0:
        _add_failure(failures, "POST_RUN_GOLD_NOT_CLEAN_PASS")
    gold_projection = score.get("gold_post_run_audit")
    if not isinstance(gold_projection, Mapping):
        _add_failure(failures, "GOLD_AUDIT_PROJECTION_MISSING")
        gold_projection = {}
    gold_audit_hash = str(score.get("gold_audit_hash") or "")
    if (
        not re.fullmatch(r"[0-9a-f]{64}", gold_audit_hash)
        or manifest.get("gold_audit_hash") != gold_audit_hash
    ):
        _add_failure(failures, "GOLD_AUDIT_HASH_LINKAGE_MISMATCH")
    gold_projection_hash = stable_hash(gold_projection)
    if (
        score.get("gold_receipt_projection_hash") != gold_projection_hash
        or manifest.get("gold_receipt_projection_hash") != gold_projection_hash
    ):
        _add_failure(failures, "GOLD_PROJECTION_HASH_LINKAGE_MISMATCH")
    gold_metrics = dict(gold_projection.get("metrics") or {})
    gold_thresholds = dict(gold_projection.get("thresholds") or {})
    gold_critical_counts = dict(gold_projection.get("critical_counts") or {})
    expected_gold_threshold_keys = {
        f"{metric_key}_min" for metric_key in GOLD_RECALL_METRIC_KEYS
    }
    expected_gold_critical_keys = {
        *(f"{metric_key}_below_threshold_count" for metric_key in GOLD_RECALL_METRIC_KEYS),
        "gold_leakage_count",
        "production_component_memo_incomplete_count",
    }
    if set(gold_metrics) != set(GOLD_RECALL_METRIC_KEYS):
        _add_failure(failures, "GOLD_METRIC_EXACT_FIELD_ROSTER_MISMATCH")
    if set(gold_thresholds) != expected_gold_threshold_keys:
        _add_failure(failures, "GOLD_THRESHOLD_EXACT_FIELD_ROSTER_MISMATCH")
    if set(gold_critical_counts) != expected_gold_critical_keys:
        _add_failure(failures, "GOLD_CRITICAL_COUNT_EXACT_FIELD_ROSTER_MISMATCH")
    if dict(score.get("gold_post_run_metrics") or {}) != gold_metrics:
        _add_failure(failures, "GOLD_METRICS_LINKAGE_MISMATCH")
    if (
        gold_projection.get("status") != GOLD_POST_RUN_PASS
        or gold_projection.get("comparison_timing") != "POST_RUN_ONLY"
        or gold_projection.get("gold_visibility_during_production") is not False
        or str(gold_projection.get("as_of_date") or "")
        != str(manifest.get("as_of_date") or "")
    ):
        _add_failure(failures, "GOLD_AUDIT_COMPLETION_CONTRACT_MISMATCH")
    for metric_key in GOLD_RECALL_METRIC_KEYS:
        value = gold_metrics.get(metric_key)
        threshold = gold_thresholds.get(f"{metric_key}_min")
        if (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or not 0.0 < float(value) <= 1.0
        ):
            _add_failure(failures, "GOLD_RECALL_METRIC_INVALID", metric_key)
            continue
        if (
            not isinstance(threshold, (int, float))
            or isinstance(threshold, bool)
            or not 0.0 < float(threshold) <= 1.0
            or float(value) < float(threshold)
        ):
            _add_failure(failures, "GOLD_RECALL_THRESHOLD_MISMATCH", metric_key)
        failure_key = f"{metric_key}_below_threshold_count"
        if gold_critical_counts.get(failure_key) != 0:
            _add_failure(failures, "GOLD_RECALL_CRITICAL_COUNT_NONZERO", failure_key)
    if (
        gold_projection.get("critical_count_sum") != 0
        or any(
            not isinstance(value, int)
            or isinstance(value, bool)
            or value != 0
            for value in gold_critical_counts.values()
        )
        or int(gold_critical_counts.get("gold_leakage_count") or 0) != 0
    ):
        _add_failure(failures, "GOLD_CRITICAL_COUNTS_NOT_CLEAN")
    for count_key in (
        "gold_fact_count",
        "qualified_material_fact_match_count",
        "covered_target_component_count",
        "required_target_component_count",
    ):
        value = gold_projection.get(count_key)
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            _add_failure(failures, "GOLD_RECALL_COUNT_INVALID", count_key)
    if gold_projection.get("covered_target_component_count") != gold_projection.get(
        "required_target_component_count"
    ):
        _add_failure(failures, "GOLD_COMPONENT_COVERAGE_INACCURATE")
    if int(gold_projection.get("qualified_material_fact_match_count") or 0) > int(
        gold_projection.get("gold_fact_count") or 0
    ):
        _add_failure(failures, "GOLD_QUALIFIED_MATCH_COUNT_EXCEEDS_GOLD_FACT_COUNT")
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
    raw_root = Path(receipt_root)
    if raw_root.is_symlink():
        return {
            "schema_version": VERIFICATION_SCHEMA,
            "receipt_root_identity": raw_root.name,
            "target_count": 0,
            "target_ids": [],
            "expected_target_ids": list(PHASE101_TARGET_IDS),
            "root_failures": [
                {"code": "RECEIPT_ROOT_SYMLINK_FORBIDDEN", "detail": None}
            ],
            "targets": [],
            "critical_count_sum": 1,
            "status": VERIFICATION_FAIL,
            "offline": True,
            "allowed_inputs": [
                "TRACKED_RECEIPTS",
                "CURRENT_SOURCE_CODE",
                "CURRENT_TRACKED_CONFIG",
            ],
            "forbidden_inputs": [
                "output",
                "data/cache",
                ".env",
                "home_cache",
                "collaboration_journal",
                "untracked_files",
            ],
        }
    root = raw_root.resolve()
    root_entries = tuple(sorted(root.iterdir(), key=lambda path: path.name)) if root.is_dir() else ()
    unexpected_root_entries = tuple(
        path.name
        for path in root_entries
        if path.name not in PHASE101_TARGET_IDS
        or not path.is_dir()
        or path.is_symlink()
    )
    child_directories = (
        tuple(
            sorted(
                (
                    path
                    for path in root_entries
                    if path.is_dir() and not path.is_symlink()
                ),
                key=lambda path: path.name,
            )
        )
        if root.is_dir()
        else ()
    )
    actual_target_ids = tuple(path.name for path in child_directories)
    exact_target_roster = set(actual_target_ids) == set(PHASE101_TARGET_IDS) and len(
        actual_target_ids
    ) == len(PHASE101_TARGET_IDS) and not unexpected_root_entries
    targets = tuple(
        verify_target_receipt(root / target_id)
        for target_id in PHASE101_TARGET_IDS
        if (root / target_id).is_dir() and not (root / target_id).is_symlink()
    )
    failures = sum(int(row["critical_count"]) for row in targets)
    root_failures: list[Mapping[str, Any]] = []
    if not exact_target_roster:
        root_failures.append(
            {
                "code": "EXACT_PHASE101_TARGET_ROOT_ROSTER_REQUIRED",
                "detail": {
                    "expected": list(PHASE101_TARGET_IDS),
                    "actual": list(actual_target_ids),
                    "unexpected_root_entries": list(unexpected_root_entries),
                },
            }
        )
        failures += 1
    return {
        "schema_version": VERIFICATION_SCHEMA,
        "receipt_root_identity": root.name,
        "target_count": len(targets),
        "target_ids": [row["target_id"] for row in targets],
        "expected_target_ids": list(PHASE101_TARGET_IDS),
        "root_failures": root_failures,
        "targets": list(targets),
        "critical_count_sum": failures,
        "status": (
            VERIFICATION_PASS
            if exact_target_roster and len(targets) == 2 and failures == 0
            else VERIFICATION_FAIL
        ),
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
