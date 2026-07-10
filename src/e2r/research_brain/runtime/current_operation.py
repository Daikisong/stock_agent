"""Current-only candidate and bounded deep-operation contracts."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.runtime.run_mode_separation import (
    CanonicalRunMode,
    claim_mode_output_root,
)


CURRENT_OPERATION_SCHEMA_VERSION = "e2r_current_operation_mode_v1"


class CurrentTriggerType(str, Enum):
    OFFICIAL = "OFFICIAL"
    EARNINGS = "EARNINGS"
    IR = "IR"
    REPORT = "REPORT"
    NEWS = "NEWS"
    MARKET = "MARKET"
    RISK = "RISK"
    EXISTING_LEDGER = "EXISTING_LEDGER"


class CurrentDeepOutcome(str, Enum):
    FULL_THESIS = "FULL_THESIS"
    DISPROVED = "DISPROVED"
    SOURCE_PENDING = "SOURCE_PENDING"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    BUDGET_PENDING = "BUDGET_PENDING"


_PENDING_OUTCOMES = frozenset(
    {
        CurrentDeepOutcome.SOURCE_PENDING,
        CurrentDeepOutcome.PROVIDER_PENDING,
        CurrentDeepOutcome.BUDGET_PENDING,
    }
)


@dataclass(frozen=True)
class CurrentUniverseBaseline:
    target_id: str
    target_name: str
    as_of_date: str
    baseline_source_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.target_id.strip() or not self.target_name.strip():
            raise ValueError("current universe baseline target identity is required")
        date.fromisoformat(self.as_of_date)
        _require_unique_text(self.baseline_source_ids, context="baseline source ids")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentClaimReference:
    claim_id: str
    target_id: str
    observed_date: str
    source_id: str
    source_backed: bool
    current_open: bool
    historical_replay: bool
    score_eligible: bool

    def __post_init__(self) -> None:
        if not self.claim_id.strip() or not self.target_id.strip() or not self.source_id.strip():
            raise ValueError("current claim reference identity is required")
        date.fromisoformat(self.observed_date)
        for name in (
            "source_backed",
            "current_open",
            "historical_replay",
            "score_eligible",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"current claim {name} must be boolean")
        if self.score_eligible and (
            not self.source_backed or not self.current_open or self.historical_replay
        ):
            raise ValueError("score-eligible current claim violates source/lifecycle mode")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentTriggerSignal:
    signal_id: str
    target_id: str
    observed_date: str
    trigger_type: str
    source_id: str
    historical_replay: bool = False
    expected_or_outcome_context: bool = False
    counts_as_score_evidence: bool = False

    def __post_init__(self) -> None:
        CurrentTriggerType(self.trigger_type)
        if not self.signal_id.strip() or not self.target_id.strip() or not self.source_id.strip():
            raise ValueError("current trigger signal identity is required")
        date.fromisoformat(self.observed_date)
        for name in (
            "historical_replay",
            "expected_or_outcome_context",
            "counts_as_score_evidence",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"current trigger {name} must be boolean")
        if self.historical_replay or self.expected_or_outcome_context:
            raise ValueError("historical/evaluator context cannot enter current trigger")
        if self.counts_as_score_evidence:
            raise ValueError("trigger signal is not direct score evidence")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentDeepCandidate:
    candidate_id: str
    target_id: str
    trigger_signal_ids: tuple[str, ...]
    current_claim_ids: tuple[str, ...]
    inferred_archetype_ids: tuple[str, ...]
    selected_for_deep: bool
    selection_reason: str
    forced_archetype_materialization: bool = False

    def __post_init__(self) -> None:
        if not self.candidate_id.strip() or not self.target_id.strip() or not self.selection_reason.strip():
            raise ValueError("current candidate identity and selection reason are required")
        _require_unique_text(self.trigger_signal_ids, context="candidate trigger ids")
        _require_unique_text(
            self.current_claim_ids,
            context="candidate current claim ids",
            required=False,
        )
        _require_unique_text(
            self.inferred_archetype_ids,
            context="candidate inferred archetypes",
            required=False,
        )
        if any(item not in CANONICAL_ARCHETYPE_IDS for item in self.inferred_archetype_ids):
            raise ValueError("current candidate uses unknown inferred archetype")
        if not isinstance(self.selected_for_deep, bool) or not isinstance(
            self.forced_archetype_materialization, bool
        ):
            raise ValueError("current candidate flags must be boolean")
        if self.forced_archetype_materialization:
            raise ValueError("current operation cannot force archetype materialization")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentDeepDisposition:
    candidate_id: str
    target_id: str
    outcome: str
    supporting_claim_ids: tuple[str, ...]
    score_claim_ids: tuple[str, ...]
    missing_conditions: tuple[str, ...]
    pending_reason: str | None = None

    def __post_init__(self) -> None:
        selected_outcome = CurrentDeepOutcome(self.outcome)
        if not self.candidate_id.strip() or not self.target_id.strip():
            raise ValueError("current deep disposition identity is required")
        _require_unique_text(
            self.supporting_claim_ids,
            context="deep supporting claim ids",
            required=False,
        )
        _require_unique_text(
            self.score_claim_ids,
            context="deep score claim ids",
            required=False,
        )
        _require_unique_text(
            self.missing_conditions,
            context="deep missing conditions",
            required=False,
        )
        if selected_outcome == CurrentDeepOutcome.FULL_THESIS:
            if not self.score_claim_ids or self.pending_reason is not None:
                raise ValueError("full thesis requires score claims and no pending reason")
        elif selected_outcome == CurrentDeepOutcome.DISPROVED:
            if not self.supporting_claim_ids or self.score_claim_ids or self.pending_reason:
                raise ValueError("disproved disposition requires counter support only")
        elif selected_outcome in _PENDING_OUTCOMES:
            if not str(self.pending_reason or "").strip() or self.score_claim_ids:
                raise ValueError("pending disposition requires exact reason and no score claims")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentOperationInput:
    as_of_date: str
    universe: tuple[CurrentUniverseBaseline, ...]
    signals: tuple[CurrentTriggerSignal, ...]
    claims: tuple[CurrentClaimReference, ...]
    candidates: tuple[CurrentDeepCandidate, ...]
    deep_dispositions: tuple[CurrentDeepDisposition, ...]
    max_deep_candidates: int
    archetype_quota: Mapping[str, int] | None = None
    force_registry_materialization: bool = False
    historical_replay_input_count: int = 0
    expected_or_outcome_context_count: int = 0
    test_only: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not self.universe:
            raise ValueError("current operation requires a full-universe baseline")
        if (
            isinstance(self.max_deep_candidates, bool)
            or not isinstance(self.max_deep_candidates, int)
            or self.max_deep_candidates <= 0
        ):
            raise ValueError("current max_deep_candidates must be a positive integer")
        for name in ("force_registry_materialization", "test_only"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"current operation {name} must be boolean")
        if self.archetype_quota is not None:
            raise ValueError("current operation forbids archetype quotas")
        if self.force_registry_materialization:
            raise ValueError("current operation forbids registry materialization")
        if self.historical_replay_input_count != 0:
            raise ValueError("historical replay input cannot enter current operation")
        if self.expected_or_outcome_context_count != 0:
            raise ValueError("expected/outcome evaluator context cannot enter current operation")


@dataclass(frozen=True)
class CurrentOperationResult:
    run_id: str
    as_of_date: str
    universe: tuple[CurrentUniverseBaseline, ...]
    signals: tuple[CurrentTriggerSignal, ...]
    claims: tuple[CurrentClaimReference, ...]
    candidates: tuple[CurrentDeepCandidate, ...]
    deep_dispositions: tuple[CurrentDeepDisposition, ...]
    manifest: Mapping[str, Any]
    mode: str = CanonicalRunMode.CURRENT_OPERATION.value
    production_runtime_ready: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not self.run_id.strip() or not self.universe:
            raise ValueError("current operation result requires run and universe")
        if self.mode != CanonicalRunMode.CURRENT_OPERATION.value:
            raise ValueError("current operation result mode mismatch")
        if self.production_runtime_ready:
            raise ValueError("Phase 11 current mode cannot claim production readiness")
        expected_leaf_hash = stable_hash(
            {
                "universe": [item.to_dict() for item in self.universe],
                "signals": [item.to_dict() for item in self.signals],
                "claims": [item.to_dict() for item in self.claims],
                "candidates": [item.to_dict() for item in self.candidates],
                "deep_dispositions": [item.to_dict() for item in self.deep_dispositions],
            }
        )
        if (
            self.manifest.get("run_id") != self.run_id
            or self.manifest.get("mode") != self.mode
            or self.manifest.get("as_of_date") != self.as_of_date
            or self.manifest.get("leaf_hash") != expected_leaf_hash
        ):
            raise ValueError("current operation result manifest identity mismatch")


def compile_current_operation(inputs: CurrentOperationInput) -> CurrentOperationResult:
    as_of = date.fromisoformat(inputs.as_of_date)
    baseline_by_target = _unique_by(
        inputs.universe,
        key=lambda item: item.target_id,
        context="current universe target",
    )
    if any(item.as_of_date != inputs.as_of_date for item in inputs.universe):
        raise ValueError("current universe baseline as-of mismatch")
    signal_by_id = _unique_by(
        inputs.signals,
        key=lambda item: item.signal_id,
        context="current signal",
    )
    for signal in inputs.signals:
        if signal.target_id not in baseline_by_target:
            raise ValueError("current signal target is outside universe baseline")
        if date.fromisoformat(signal.observed_date) > as_of:
            raise ValueError("future signal entered current operation")
    claim_by_id = _unique_by(
        inputs.claims,
        key=lambda item: item.claim_id,
        context="current claim",
    )
    for claim in inputs.claims:
        if claim.target_id not in baseline_by_target:
            raise ValueError("current claim target is outside universe baseline")
        if date.fromisoformat(claim.observed_date) > as_of:
            raise ValueError("future claim entered current operation")
        if claim.historical_replay:
            raise ValueError("historical replay claim entered current operation")
    candidate_by_id = _unique_by(
        inputs.candidates,
        key=lambda item: item.candidate_id,
        context="current candidate",
    )
    for candidate in inputs.candidates:
        if candidate.target_id not in baseline_by_target:
            raise ValueError("current candidate target is outside universe baseline")
        for signal_id in candidate.trigger_signal_ids:
            signal = signal_by_id.get(signal_id)
            if signal is None or signal.target_id != candidate.target_id:
                raise ValueError("current candidate trigger leaf mismatch")
        for claim_id in candidate.current_claim_ids:
            claim = claim_by_id.get(claim_id)
            if claim is None or claim.target_id != candidate.target_id:
                raise ValueError("current candidate claim leaf mismatch")
    selected = tuple(item for item in inputs.candidates if item.selected_for_deep)
    if len(selected) > inputs.max_deep_candidates:
        raise ValueError("current selective-deep candidate budget exceeded")
    disposition_by_candidate = _unique_by(
        inputs.deep_dispositions,
        key=lambda item: item.candidate_id,
        context="current deep disposition",
    )
    if set(disposition_by_candidate) != {item.candidate_id for item in selected}:
        raise ValueError("every selected deep candidate requires exactly one terminal outcome")
    for disposition in inputs.deep_dispositions:
        candidate = candidate_by_id[disposition.candidate_id]
        if disposition.target_id != candidate.target_id:
            raise ValueError("current deep disposition target mismatch")
        allowed_claim_ids = set(candidate.current_claim_ids)
        if not set(disposition.supporting_claim_ids).issubset(allowed_claim_ids):
            raise ValueError("deep supporting claim is outside candidate current claims")
        if not set(disposition.score_claim_ids).issubset(allowed_claim_ids):
            raise ValueError("deep score claim is outside candidate current claims")
        for claim_id in disposition.score_claim_ids:
            claim = claim_by_id[claim_id]
            if not claim.score_eligible:
                raise ValueError("deep score claim is not current/source-backed eligible")

    outcome_counts = {
        outcome.value: sum(item.outcome == outcome.value for item in inputs.deep_dispositions)
        for outcome in CurrentDeepOutcome
    }
    inferred_archetypes = {
        archetype_id
        for candidate in inputs.candidates
        for archetype_id in candidate.inferred_archetype_ids
    }
    critical = {
        "universe_baseline_missing": 0,
        "candidate_without_current_trigger": sum(
            not item.trigger_signal_ids for item in inputs.candidates
        ),
        "selected_deep_without_terminal_outcome": len(selected)
        - len(inputs.deep_dispositions),
        "selective_deep_budget_exceeded": int(
            len(selected) > inputs.max_deep_candidates
        ),
        "historical_replay_input": inputs.historical_replay_input_count,
        "expected_or_outcome_context": inputs.expected_or_outcome_context_count,
        "forced_archetype_materialization": sum(
            item.forced_archetype_materialization for item in inputs.candidates
        ),
        "archetype_quota": int(inputs.archetype_quota is not None),
        "trigger_used_as_score_evidence": sum(
            item.counts_as_score_evidence for item in inputs.signals
        ),
        "historical_or_noncurrent_score_claim": sum(
            not claim.source_backed
            or not claim.current_open
            or claim.historical_replay
            for disposition in inputs.deep_dispositions
            for claim in (
                claim_by_id[claim_id] for claim_id in disposition.score_claim_ids
            )
        ),
    }
    leaf_payload = {
        "universe": [item.to_dict() for item in inputs.universe],
        "signals": [item.to_dict() for item in inputs.signals],
        "claims": [item.to_dict() for item in inputs.claims],
        "candidates": [item.to_dict() for item in inputs.candidates],
        "deep_dispositions": [item.to_dict() for item in inputs.deep_dispositions],
    }
    leaf_hash = stable_hash(leaf_payload)
    run_id = f"CURRENT-{stable_hash({'as_of': inputs.as_of_date, 'leaf_hash': leaf_hash})[:24]}"
    manifest = {
        "schema_version": CURRENT_OPERATION_SCHEMA_VERSION,
        "status": (
            "CURRENT_OPERATION_MODE_SEPARATION_PASS"
            if sum(critical.values()) == 0
            else "CURRENT_OPERATION_MODE_SEPARATION_FAIL"
        ),
        "run_id": run_id,
        "mode": CanonicalRunMode.CURRENT_OPERATION.value,
        "output_namespace": "current_operation",
        "as_of_date": inputs.as_of_date,
        "full_universe_baseline_count": len(inputs.universe),
        "trigger_signal_count": len(inputs.signals),
        "real_trigger_candidate_count": len(inputs.candidates),
        "selected_deep_candidate_count": len(selected),
        "max_deep_candidates": inputs.max_deep_candidates,
        "deep_outcome_counts": outcome_counts,
        "deep_terminal_outcome_count": len(inputs.deep_dispositions),
        "historical_replay_input_count": 0,
        "expected_or_outcome_context_count": 0,
        "forced_archetype_materialization_count": 0,
        "archetype_quota_count": 0,
        "canonical_registry_archetype_count": len(CANONICAL_ARCHETYPE_IDS),
        "materialized_current_archetype_count": len(inferred_archetypes),
        "missing_current_archetype_row_critical_count": 0,
        "trigger_score_evidence_count": 0,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "leaf_hash": leaf_hash,
        "test_only": inputs.test_only,
        "production_runtime_ready": False,
    }
    return CurrentOperationResult(
        run_id=run_id,
        as_of_date=inputs.as_of_date,
        universe=inputs.universe,
        signals=inputs.signals,
        claims=inputs.claims,
        candidates=inputs.candidates,
        deep_dispositions=inputs.deep_dispositions,
        manifest=manifest,
    )


def write_current_operation(
    result: CurrentOperationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    marker = claim_mode_output_root(
        root,
        mode=CanonicalRunMode.CURRENT_OPERATION,
        run_id=result.run_id,
    )
    paths = {
        "mode_marker": marker,
        "manifest": root / "current_operation_manifest.json",
        "universe": root / "current_universe_baseline.jsonl",
        "signals": root / "current_trigger_signals.jsonl",
        "claims": root / "current_claim_references.jsonl",
        "candidates": root / "current_deep_candidates.jsonl",
        "dispositions": root / "current_deep_dispositions.jsonl",
        "report": root / "current_operation_report.md",
    }
    write_json(paths["manifest"], result.manifest)
    write_jsonl(paths["universe"], (item.to_dict() for item in result.universe))
    write_jsonl(paths["signals"], (item.to_dict() for item in result.signals))
    write_jsonl(paths["claims"], (item.to_dict() for item in result.claims))
    write_jsonl(paths["candidates"], (item.to_dict() for item in result.candidates))
    write_jsonl(paths["dispositions"], (item.to_dict() for item in result.deep_dispositions))
    write_text(paths["report"], render_current_operation_report(result.manifest))
    return paths


def render_current_operation_report(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        (
            "# Current Operation Mode Separation",
            "",
            f"- status: {manifest['status']}",
            f"- as_of_date: {manifest['as_of_date']}",
            f"- full-universe baseline: {manifest['full_universe_baseline_count']}",
            f"- real trigger candidates: {manifest['real_trigger_candidate_count']}",
            f"- bounded selected deep: {manifest['selected_deep_candidate_count']}/{manifest['max_deep_candidates']}",
            f"- materialized current archetypes: {manifest['materialized_current_archetype_count']}",
            "- forced archetype quota: false",
            "- historical replay input: 0",
            f"- critical_count_sum: {manifest['critical_count_sum']}",
            "- production_runtime_ready: false",
            "",
        )
    )


def _require_unique_text(
    values: Sequence[str],
    *,
    context: str,
    required: bool = True,
) -> None:
    if required and not values:
        raise ValueError(f"{context} cannot be empty")
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains empty text")
    if len(values) != len(set(values)):
        raise ValueError(f"{context} contains duplicates")


def _unique_by(
    values: Sequence[Any],
    *,
    key: Any,
    context: str,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for item in values:
        identity = str(key(item))
        if identity in result:
            raise ValueError(f"duplicate {context}: {identity}")
        result[identity] = item
    return result


__all__ = [
    "CURRENT_OPERATION_SCHEMA_VERSION",
    "CurrentClaimReference",
    "CurrentDeepCandidate",
    "CurrentDeepDisposition",
    "CurrentDeepOutcome",
    "CurrentOperationInput",
    "CurrentOperationResult",
    "CurrentTriggerSignal",
    "CurrentTriggerType",
    "CurrentUniverseBaseline",
    "compile_current_operation",
    "render_current_operation_report",
    "write_current_operation",
]
