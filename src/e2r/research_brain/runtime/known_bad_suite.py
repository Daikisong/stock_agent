"""Unified evidence for required known-bad rejection probes."""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text


KNOWN_BAD_SUITE_SCHEMA_VERSION = "e2r_unified_known_bad_suite_v1"
KNOWN_BAD_SUITE_AUDIT_SCHEMA_VERSION = "e2r_unified_known_bad_suite_audit_v1"


class KnownBadCategory(str, Enum):
    CORPUS = "CORPUS"
    SOURCE = "SOURCE"
    PLANNER = "PLANNER"
    SEMANTIC = "SEMANTIC"
    CLAIM = "CLAIM"
    SCORE_STAGE = "SCORE_STAGE"
    MODE = "MODE"
    CURRENT = "CURRENT"


class KnownBadProbeId(str, Enum):
    FILE_LEVEL_CASE_COLLAPSE = "FILE_LEVEL_CASE_COLLAPSE"
    FIRST_SYMBOL_EXTRACTION = "FIRST_SYMBOL_EXTRACTION"
    COMPANY_DATE_LOSS = "COMPANY_DATE_LOSS"
    ONE_URL_WHOLE_FILE_A2 = "ONE_URL_WHOLE_FILE_A2"
    HANDOFF_PROMPT_AS_CASE = "HANDOFF_PROMPT_AS_CASE"
    SOURCE_PROXY_PROMOTED = "SOURCE_PROXY_PROMOTED"
    C05_CONTEXT_COPY_CORPUS = "C05_CONTEXT_COPY_CORPUS"
    C05_CONTEXT_COPY_CURRENT = "C05_CONTEXT_COPY_CURRENT"
    PRODUCT_PROFILE_AS_ORDER = "PRODUCT_PROFILE_AS_ORDER"
    HBM_KEYWORD_POSITIVE = "HBM_KEYWORD_POSITIVE"
    SECURITY_KEYWORD_ARR = "SECURITY_KEYWORD_ARR"
    COMMODITY_HEADLINE_MARGIN = "COMMODITY_HEADLINE_MARGIN"
    SNIPPET_SCORE = "SNIPPET_SCORE"
    WRONG_SUBJECT = "WRONG_SUBJECT"
    CUSTOMER_CAPA_AS_TARGET_CAPA = "CUSTOMER_CAPA_AS_TARGET_CAPA"
    INDUSTRY_DEMAND_AS_ISSUER_ORDER = "INDUSTRY_DEMAND_AS_ISSUER_ORDER"
    FINANCIAL_CONTRACT_AS_COMMERCIAL = "FINANCIAL_CONTRACT_AS_COMMERCIAL"
    STALE_RISK_PENALTY = "STALE_RISK_PENALTY"
    REROUTED_GAP_CLOSURE = "REROUTED_GAP_CLOSURE"
    PROVIDER_FAILURE_RED = "PROVIDER_FAILURE_RED"
    REPLAY_AS_REAL_FETCH = "REPLAY_AS_REAL_FETCH"
    EVENT_SCORE_FULL_SCORE = "EVENT_SCORE_FULL_SCORE"
    STAGE_TRACE_MISMATCH = "STAGE_TRACE_MISMATCH"
    HISTORICAL_OUTCOME_LEAKAGE = "HISTORICAL_OUTCOME_LEAKAGE"
    HISTORICAL_REPLAY_CURRENT_WATCHLIST = (
        "HISTORICAL_REPLAY_CURRENT_WATCHLIST"
    )
    FORCED_CURRENT_ARCHETYPE_MATERIALIZATION = (
        "FORCED_CURRENT_ARCHETYPE_MATERIALIZATION"
    )


REQUIRED_KNOWN_BAD_PROBE_IDS = tuple(item.value for item in KnownBadProbeId)


@dataclass(frozen=True)
class KnownBadProbeObservation:
    probe_id: str
    category: str
    source_phase: int
    detector_ids: tuple[str, ...]
    mutation_description: str
    detected: bool
    signal_ids: tuple[str, ...]
    test_only: bool = True
    production_runtime_ready: bool = False
    schema_version: str = KNOWN_BAD_SUITE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != KNOWN_BAD_SUITE_SCHEMA_VERSION:
            raise ValueError("known-bad observation schema version mismatch")
        KnownBadProbeId(self.probe_id)
        KnownBadCategory(self.category)
        if (
            isinstance(self.source_phase, bool)
            or not isinstance(self.source_phase, int)
            or not 2 <= self.source_phase <= 15
        ):
            raise ValueError("known-bad source phase must be within 2..15")
        if not isinstance(self.detector_ids, tuple) or not isinstance(
            self.signal_ids, tuple
        ):
            raise ValueError("known-bad detector and signal ids must be tuples")
        _require_unique_text(self.detector_ids, context="known-bad detector ids")
        _require_unique_text(self.signal_ids, context="known-bad signal ids")
        if not self.detector_ids or not self.signal_ids:
            raise ValueError("known-bad observation requires detector and signal")
        if not self.mutation_description.strip():
            raise ValueError("known-bad mutation description is required")
        for name in ("detected", "test_only", "production_runtime_ready"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"known-bad {name} must be boolean")
        if self.production_runtime_ready:
            raise ValueError("known-bad fixture observation cannot claim production ready")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class KnownBadSuiteResult:
    run_id: str
    observations: tuple[KnownBadProbeObservation, ...]
    audit: Mapping[str, Any]
    manifest: Mapping[str, Any]
    production_runtime_ready: bool = False

    def __post_init__(self) -> None:
        leaf_payload = _leaf_payload(self.observations)
        leaf_hash = stable_hash(leaf_payload)
        expected_run_id = _run_id(leaf_hash)
        expected_audit = audit_known_bad_suite(
            {
                "schema_version": KNOWN_BAD_SUITE_SCHEMA_VERSION,
                "run_id": self.run_id,
                **leaf_payload,
                "manifest": dict(self.manifest),
                "production_runtime_ready": self.production_runtime_ready,
            }
        )
        if (
            self.run_id != expected_run_id
            or dict(self.audit) != dict(expected_audit)
            or expected_audit.get("critical_count_sum") != 0
            or self.manifest.get("run_id") != self.run_id
            or self.manifest.get("leaf_hash") != leaf_hash
            or self.manifest.get("critical_counts")
            != expected_audit.get("critical_counts")
            or self.production_runtime_ready
        ):
            raise ValueError("unified known-bad result integrity mismatch")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": KNOWN_BAD_SUITE_SCHEMA_VERSION,
            "run_id": self.run_id,
            "observations": [item.to_dict() for item in self.observations],
            "audit": dict(self.audit),
            "manifest": dict(self.manifest),
            "production_runtime_ready": False,
        }


def compile_known_bad_suite(
    observations: Sequence[KnownBadProbeObservation],
) -> KnownBadSuiteResult:
    frozen = tuple(observations)
    leaf_payload = _leaf_payload(frozen)
    leaf_hash = stable_hash(leaf_payload)
    run_id = _run_id(leaf_hash)
    category_counts = Counter(item.category for item in frozen)
    manifest = {
        "schema_version": KNOWN_BAD_SUITE_SCHEMA_VERSION,
        "status": "UNIFIED_KNOWN_BAD_SUITE_PASS",
        "run_id": run_id,
        "required_probe_count": len(REQUIRED_KNOWN_BAD_PROBE_IDS),
        "observed_probe_count": len(frozen),
        "detected_probe_count": sum(item.detected for item in frozen),
        "undetected_probe_count": sum(not item.detected for item in frozen),
        "category_counts": dict(sorted(category_counts.items())),
        "unique_detector_count": len(
            {detector for item in frozen for detector in item.detector_ids}
        ),
        "leaf_hash": leaf_hash,
        "test_only": all(item.test_only for item in frozen),
        "production_runtime_ready": False,
    }
    audit_payload = {
        "schema_version": KNOWN_BAD_SUITE_SCHEMA_VERSION,
        "run_id": run_id,
        **leaf_payload,
        "manifest": manifest,
        "production_runtime_ready": False,
    }
    audit = audit_known_bad_suite(audit_payload)
    if audit["critical_count_sum"]:
        raise ValueError(f"unified known-bad audit failed: {audit['critical_counts']}")
    manifest = {
        **manifest,
        "critical_counts": dict(audit["critical_counts"]),
        "critical_count_sum": 0,
    }
    return KnownBadSuiteResult(
        run_id=run_id,
        observations=frozen,
        audit=audit,
        manifest=manifest,
    )


def audit_known_bad_suite(
    result: KnownBadSuiteResult | Mapping[str, Any],
) -> Mapping[str, Any]:
    payload = result.to_dict() if isinstance(result, KnownBadSuiteResult) else dict(result)
    raw_rows = payload.get("observations")
    rows = tuple(_mapping_rows(raw_rows))
    probe_ids = tuple(str(item.get("probe_id") or "") for item in rows)
    required = set(REQUIRED_KNOWN_BAD_PROBE_IDS)
    observed = set(probe_ids)
    invalid_contract = sum(not _observation_mapping_valid(item) for item in rows)
    leaf_payload = {"observations": list(rows)}
    leaf_hash = stable_hash(leaf_payload)
    expected_run_id = _run_id(leaf_hash)
    manifest = payload.get("manifest")
    manifest_mapping = dict(manifest) if isinstance(manifest, Mapping) else {}
    category_counts = dict(
        sorted(Counter(str(item.get("category") or "") for item in rows).items())
    )
    detector_ids = {
        detector
        for item in rows
        for detector in _text_sequence(item.get("detector_ids"))
    }
    detected_count = sum(item.get("detected") is True for item in rows)
    undetected_count = sum(item.get("detected") is not True for item in rows)
    critical = {
        "payload_schema_version_mismatch": int(
            payload.get("schema_version") != KNOWN_BAD_SUITE_SCHEMA_VERSION
        ),
        "invalid_nonmapping_observation": _sequence_size(raw_rows) - len(rows),
        "invalid_observation_contract": invalid_contract,
        "duplicate_required_probe": len(probe_ids) - len(set(probe_ids)),
        "missing_required_probe": len(required - observed),
        "unexpected_probe": len(observed - required),
        "undetected_required_probe": sum(
            item.get("probe_id") in required and item.get("detected") is not True
            for item in rows
        ),
        "missing_detector_lineage": sum(
            not item.get("detector_ids") for item in rows
        ),
        "missing_detection_signal": sum(not item.get("signal_ids") for item in rows),
        "non_fixture_observation_in_acceptance": sum(
            item.get("test_only") is not True for item in rows
        ),
        "run_id_mismatch": int(
            str(payload.get("run_id") or "") != expected_run_id
        ),
        "manifest_missing_or_invalid": int(
            not isinstance(manifest, Mapping) or not manifest_mapping
        ),
        "manifest_schema_version_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("schema_version")
            != KNOWN_BAD_SUITE_SCHEMA_VERSION
        ),
        "manifest_run_id_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("run_id") != expected_run_id
        ),
        "manifest_status_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("status")
            != "UNIFIED_KNOWN_BAD_SUITE_PASS"
        ),
        "manifest_leaf_hash_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("leaf_hash") != leaf_hash
        ),
        "manifest_probe_count_mismatch": int(
            bool(manifest_mapping)
            and (
                manifest_mapping.get("required_probe_count") != len(required)
                or manifest_mapping.get("observed_probe_count") != len(rows)
                or manifest_mapping.get("detected_probe_count")
                != detected_count
                or manifest_mapping.get("undetected_probe_count")
                != undetected_count
            )
        ),
        "manifest_category_count_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("category_counts") != category_counts
        ),
        "manifest_detector_count_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("unique_detector_count") != len(detector_ids)
        ),
        "manifest_fixture_boundary_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("test_only")
            != all(item.get("test_only") is True for item in rows)
        ),
        "production_runtime_ready_overclaim": int(
            payload.get("production_runtime_ready") is True
            or manifest_mapping.get("production_runtime_ready") is True
            or any(item.get("production_runtime_ready") is True for item in rows)
        ),
    }
    return {
        "schema_version": KNOWN_BAD_SUITE_AUDIT_SCHEMA_VERSION,
        "status": (
            "UNIFIED_KNOWN_BAD_SUITE_PASS"
            if rows and sum(critical.values()) == 0
            else "UNIFIED_KNOWN_BAD_SUITE_FAIL"
        ),
        "required_probe_count": len(required),
        "observed_probe_count": len(rows),
        "detected_probe_count": detected_count,
        "critical_check_count": len(critical),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": leaf_hash,
        "production_runtime_ready": False,
    }


def write_known_bad_suite(
    result: KnownBadSuiteResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "manifest": root / "unified_known_bad_manifest.json",
        "audit": root / "unified_known_bad_audit.json",
        "observations": root / "unified_known_bad_observations.jsonl",
        "report": root / "unified_known_bad_report.md",
    }
    write_json(paths["manifest"], result.manifest)
    write_json(paths["audit"], result.audit)
    write_jsonl(
        paths["observations"],
        (item.to_dict() for item in result.observations),
    )
    write_text(paths["report"], render_known_bad_suite_report(result.manifest))
    return paths


def render_known_bad_suite_report(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        (
            "# Unified Known-Bad Suite",
            "",
            f"- status: {manifest['status']}",
            f"- required probes: {manifest['required_probe_count']}",
            f"- detected probes: {manifest['detected_probe_count']}",
            f"- undetected probes: {manifest['undetected_probe_count']}",
            f"- categories: {manifest['category_counts']}",
            f"- unique detectors: {manifest['unique_detector_count']}",
            "- fixture-only acceptance: true",
            "- production_runtime_ready: false",
            "",
        )
    )


def _leaf_payload(
    observations: Sequence[KnownBadProbeObservation],
) -> Mapping[str, Any]:
    return {"observations": [item.to_dict() for item in observations]}


def _observation_mapping_valid(payload: Mapping[str, Any]) -> bool:
    detector_ids = payload.get("detector_ids")
    signal_ids = payload.get("signal_ids")
    if not isinstance(detector_ids, (list, tuple)) or not isinstance(
        signal_ids, (list, tuple)
    ):
        return False
    try:
        KnownBadProbeObservation(
            **{
                **dict(payload),
                "detector_ids": tuple(detector_ids),
                "signal_ids": tuple(signal_ids),
            }
        )
    except (TypeError, ValueError):
        return False
    return True


def _mapping_rows(value: Any) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(item for item in value if isinstance(item, Mapping))


def _sequence_size(value: Any) -> int:
    if isinstance(value, (list, tuple)):
        return len(value)
    return 0 if value is None else 1


def _text_sequence(value: Any) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(item for item in value if isinstance(item, str) and item.strip())


def _run_id(leaf_hash: str) -> str:
    return "KNOWNBAD-" + stable_hash(
        {"schema_version": KNOWN_BAD_SUITE_SCHEMA_VERSION, "leaf_hash": leaf_hash}
    )[:24]


def _require_unique_text(values: Sequence[str], *, context: str) -> None:
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains empty text")
    if len(values) != len(set(values)):
        raise ValueError(f"{context} contains duplicates")


__all__ = [
    "KNOWN_BAD_SUITE_AUDIT_SCHEMA_VERSION",
    "KNOWN_BAD_SUITE_SCHEMA_VERSION",
    "REQUIRED_KNOWN_BAD_PROBE_IDS",
    "KnownBadCategory",
    "KnownBadProbeId",
    "KnownBadProbeObservation",
    "KnownBadSuiteResult",
    "audit_known_bad_suite",
    "compile_known_bad_suite",
    "render_known_bad_suite_report",
    "write_known_bad_suite",
]
