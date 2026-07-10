"""Deterministic full-universe depth policy with bounded selective deep."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl

from .baseline_materializer import BaselineLaneRecord, BaselineLaneStatus
from .schemas import LiveRunProfile
from .trigger_fusion import CandidateEvent, TriggerSignal, TriggerType
from .universe_materializer import LiveUniverseRow


DEPTH_DECISION_SCHEMA_VERSION = "e2r_live_depth_decision_v1"
_FAILURE_STATUSES = {
    BaselineLaneStatus.PROVIDER_FAILED.value,
    BaselineLaneStatus.AUTH_FAILED.value,
    BaselineLaneStatus.RATE_LIMITED.value,
    BaselineLaneStatus.BUDGET_EXHAUSTED.value,
}


class LiveDepth(str, Enum):
    L0_UNIVERSE = "L0_UNIVERSE"
    L1_BASELINE = "L1_BASELINE"
    L2_OFFICIAL_LIGHT = "L2_OFFICIAL_LIGHT"
    L3_RESEARCH_BRAIN = "L3_RESEARCH_BRAIN"
    L4_ACQUISITION = "L4_ACQUISITION"
    L5_FULL_THESIS = "L5_FULL_THESIS"


@dataclass(frozen=True)
class DepthSelectionConfig:
    as_of_date: str
    max_official_light_targets: int
    max_deep_candidates: int
    max_brain_candidates: int
    max_acquisition_candidates: int
    max_llm_calls_per_candidate: int
    max_source_tasks_per_candidate: int
    max_fetches_per_candidate: int
    max_retries_per_candidate: int
    max_general_web_fetches_per_candidate: int
    max_runtime_seconds: int
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        positive = (
            "max_official_light_targets",
            "max_deep_candidates",
            "max_brain_candidates",
            "max_acquisition_candidates",
            "max_llm_calls_per_candidate",
            "max_source_tasks_per_candidate",
            "max_fetches_per_candidate",
            "max_runtime_seconds",
        )
        nonnegative = (
            "max_retries_per_candidate",
            "max_general_web_fetches_per_candidate",
        )
        for name in positive:
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"depth budget {name} must be bounded and positive")
        for name in nonnegative:
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"depth budget {name} must be bounded and nonnegative")
        if not (
            self.max_acquisition_candidates
            <= self.max_brain_candidates
            <= self.max_deep_candidates
        ):
            raise ValueError("depth candidate budgets must remain nested")

    @classmethod
    def from_run_profile(
        cls,
        *,
        as_of_date: str,
        profile: LiveRunProfile,
        test_mode: bool = False,
    ) -> "DepthSelectionConfig":
        return cls(
            as_of_date=as_of_date,
            test_mode=test_mode,
            **{key: int(value) for key, value in profile.budgets.items()},
        )


@dataclass(frozen=True)
class LiveDepthDecision:
    depth_decision_id: str
    target_id: str
    target_name: str
    as_of_date: str
    completed_depths: tuple[str, ...]
    maximum_depth: str
    candidate_event_id: str | None
    trigger_signal_ids: tuple[str, ...]
    priority_score: float
    selected_for_official_light: bool
    selected_for_deep: bool
    selected_for_brain: bool
    acquisition_eligible: bool
    selection_reasons: tuple[str, ...]
    not_selected_reason: str | None
    source_task_budget: Mapping[str, int]
    llm_budget: Mapping[str, int]
    general_web_budget: Mapping[str, int]
    forced_archetype_quota: bool = False
    schema_version: str = DEPTH_DECISION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        maximum = LiveDepth(self.maximum_depth)
        depths = tuple(LiveDepth(item) for item in self.completed_depths)
        if not all((self.depth_decision_id.strip(), self.target_id.strip(), self.target_name.strip())):
            raise ValueError("depth decision identity required")
        if not depths or depths[-1] != maximum:
            raise ValueError("depth maximum must match completed path tail")
        expected = tuple(LiveDepth)
        positions = tuple(expected.index(item) for item in depths)
        if positions != tuple(range(positions[-1] + 1)):
            raise ValueError("depth path must be contiguous from L0")
        if not self.selection_reasons:
            raise ValueError("depth decision needs an explicit reason")
        if self.selected_for_brain != self.selected_for_deep:
            raise ValueError("L3 deep selection and Brain selection must stay aligned")
        if self.selected_for_deep and maximum != LiveDepth.L3_RESEARCH_BRAIN:
            raise ValueError("Phase 24 selected deep target must stop at L3")
        if self.acquisition_eligible and not self.selected_for_brain:
            raise ValueError("acquisition eligibility requires Brain selection")
        if not self.selected_for_deep and not self.not_selected_reason:
            raise ValueError("non-selected target requires exact reason")
        if self.forced_archetype_quota:
            raise ValueError("current depth policy cannot force archetype quotas")
        for budget in (self.source_task_budget, self.llm_budget, self.general_web_budget):
            if any(
                isinstance(value, bool) or not isinstance(value, int) or value < 0
                for value in budget.values()
            ):
                raise ValueError("depth leaf budget must use bounded nonnegative integers")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "completed_depths": list(self.completed_depths),
            "trigger_signal_ids": list(self.trigger_signal_ids),
            "selection_reasons": list(self.selection_reasons),
            "source_task_budget": dict(self.source_task_budget),
            "llm_budget": dict(self.llm_budget),
            "general_web_budget": dict(self.general_web_budget),
        }


@dataclass(frozen=True)
class DepthSelectionResult:
    as_of_date: str
    status: str
    decisions: tuple[LiveDepthDecision, ...]
    budget_allocation: Mapping[str, Any]
    not_selected_budget: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)


class CurrentDepthSelector:
    def select(
        self,
        config: DepthSelectionConfig,
        *,
        universe: Sequence[LiveUniverseRow],
        baseline_lanes: Sequence[BaselineLaneRecord],
        candidate_events: Sequence[CandidateEvent],
        trigger_signals: Sequence[TriggerSignal],
    ) -> DepthSelectionResult:
        eligible = tuple(row for row in universe if row.eligible)
        universe_by_symbol = _unique_universe(eligible)
        candidates_by_symbol = _unique_candidates(candidate_events, universe_by_symbol)
        signals_by_id = _unique_signals(trigger_signals, universe_by_symbol)
        signals_by_symbol: dict[str, tuple[TriggerSignal, ...]] = {}
        for symbol in universe_by_symbol:
            signals_by_symbol[symbol] = tuple(
                signal for signal in trigger_signals if signal.target_id == symbol
            )
        lanes_by_symbol: dict[str, list[BaselineLaneRecord]] = {}
        for lane in baseline_lanes:
            if lane.target_id in universe_by_symbol:
                lanes_by_symbol.setdefault(lane.target_id, []).append(lane)
        rankings: list[tuple[str, float, tuple[str, ...]]] = []
        for symbol in universe_by_symbol:
            reasons = _selection_reasons(
                candidate=candidates_by_symbol.get(symbol),
                signals=signals_by_symbol[symbol],
                lanes=lanes_by_symbol.get(symbol, ()),
            )
            rankings.append(
                (
                    symbol,
                    _priority_score(
                        candidate=candidates_by_symbol.get(symbol),
                        signals=signals_by_symbol[symbol],
                        lanes=lanes_by_symbol.get(symbol, ()),
                    ),
                    reasons,
                )
            )
        signal_ranked = tuple(
            item
            for item in sorted(rankings, key=lambda row: (-row[1], row[0]))
            if item[1] > 0
        )
        official_light_ids = {
            symbol
            for symbol, _, _ in signal_ranked[: config.max_official_light_targets]
        }
        deep_pool = signal_ranked[: config.max_deep_candidates]
        deep_pool_ids = {symbol for symbol, _, _ in deep_pool}
        brain_ids = {
            symbol for symbol, _, _ in deep_pool[: config.max_brain_candidates]
        }
        acquisition_ids = {
            symbol
            for symbol, _, _ in deep_pool[: config.max_acquisition_candidates]
            if symbol in brain_ids
        }
        rank_by_symbol = {
            symbol: (rank + 1, score, reasons)
            for rank, (symbol, score, reasons) in enumerate(signal_ranked)
        }
        decisions: list[LiveDepthDecision] = []
        not_selected: list[Mapping[str, Any]] = []
        for symbol, member in sorted(universe_by_symbol.items()):
            candidate = candidates_by_symbol.get(symbol)
            rank, priority, reasons = rank_by_symbol.get(
                symbol,
                (None, 0.0, ("NO_CURRENT_TRIGGER",)),
            )
            selected_brain = symbol in brain_ids
            selected_official = symbol in official_light_ids
            acquisition_eligible = symbol in acquisition_ids
            maximum = (
                LiveDepth.L3_RESEARCH_BRAIN
                if selected_brain
                else LiveDepth.L2_OFFICIAL_LIGHT
                if selected_official
                else LiveDepth.L1_BASELINE
            )
            completed = tuple(item.value for item in tuple(LiveDepth)[: tuple(LiveDepth).index(maximum) + 1])
            not_selected_reason = None
            if not selected_brain:
                not_selected_reason = (
                    "NO_CURRENT_TRIGGER"
                    if priority <= 0
                    else "BRAIN_BUDGET_LIMIT"
                    if symbol in deep_pool_ids
                    else "DEEP_BUDGET_LIMIT"
                    if candidate is not None
                    else "SOURCE_GAP_OFFICIAL_LIGHT_ONLY"
                )
                not_selected.append(
                    {
                        "schema_version": "e2r_live_not_selected_budget_v1",
                        "target_id": symbol,
                        "target_name": str(member.company_name),
                        "priority_rank": rank,
                        "priority_score": priority,
                        "candidate_event_id": candidate.candidate_event_id if candidate else None,
                        "reason": not_selected_reason,
                    }
                )
            decision = LiveDepthDecision(
                depth_decision_id="DEPTH-"
                + stable_hash(
                    {
                        "target": symbol,
                        "as_of_date": config.as_of_date,
                        "maximum": maximum.value,
                        "candidate": candidate.candidate_event_id if candidate else None,
                    }
                )[:24],
                target_id=symbol,
                target_name=str(member.company_name),
                as_of_date=config.as_of_date,
                completed_depths=completed,
                maximum_depth=maximum.value,
                candidate_event_id=candidate.candidate_event_id if candidate else None,
                trigger_signal_ids=(
                    tuple(candidate.trigger_signal_ids) if candidate else ()
                ),
                priority_score=priority,
                selected_for_official_light=selected_official,
                selected_for_deep=selected_brain,
                selected_for_brain=selected_brain,
                acquisition_eligible=acquisition_eligible,
                selection_reasons=reasons,
                not_selected_reason=not_selected_reason,
                source_task_budget={
                    "max_tasks": config.max_source_tasks_per_candidate if selected_brain else 0,
                    "max_fetches": config.max_fetches_per_candidate if selected_brain else 0,
                    "max_retries": config.max_retries_per_candidate if selected_brain else 0,
                },
                llm_budget={
                    "max_calls": config.max_llm_calls_per_candidate if selected_brain else 0,
                },
                general_web_budget={
                    "max_fetches": (
                        config.max_general_web_fetches_per_candidate
                        if acquisition_eligible
                        else 0
                    )
                },
            )
            if candidate:
                missing_signal_ids = set(candidate.trigger_signal_ids) - set(signals_by_id)
                if missing_signal_ids:
                    raise ValueError("candidate depth lineage references unknown trigger")
            decisions.append(decision)
        audit = _audit_depth_selection(
            eligible=eligible,
            decisions=tuple(decisions),
            config=config,
            not_selected=tuple(not_selected),
        )
        budget_allocation = {
            "schema_version": "e2r_live_budget_allocation_v1",
            "as_of_date": config.as_of_date,
            "limits": {
                name: getattr(config, name)
                for name in (
                    "max_official_light_targets",
                    "max_deep_candidates",
                    "max_brain_candidates",
                    "max_acquisition_candidates",
                    "max_llm_calls_per_candidate",
                    "max_source_tasks_per_candidate",
                    "max_fetches_per_candidate",
                    "max_retries_per_candidate",
                    "max_general_web_fetches_per_candidate",
                    "max_runtime_seconds",
                )
            },
            "allocated": {
                "official_light_targets": len(official_light_ids),
                "deep_candidate_pool": len(deep_pool_ids),
                "brain_targets": len(brain_ids),
                "acquisition_eligible_targets": len(acquisition_ids),
            },
            "unbounded_budget_count": 0,
        }
        return DepthSelectionResult(
            as_of_date=config.as_of_date,
            status=(
                "CURRENT_DEPTH_SELECTION_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_DEPTH_SELECTION_FAIL"
            ),
            decisions=tuple(decisions),
            budget_allocation=budget_allocation,
            not_selected_budget=tuple(not_selected),
            audit=audit,
        )


def write_depth_selection(
    result: DepthSelectionResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "decisions": root / "depth_decisions.jsonl",
        "audit": root / "candidate_selection_audit.json",
        "budgets": root / "budget_allocation.json",
        "not_selected": root / "not_selected_budget.jsonl",
    }
    write_jsonl(paths["decisions"], (item.to_dict() for item in result.decisions))
    write_json(paths["audit"], {**dict(result.audit), "status": result.status})
    write_json(paths["budgets"], result.budget_allocation)
    write_jsonl(paths["not_selected"], result.not_selected_budget)
    return paths


def load_depth_decisions(path: str | Path) -> tuple[LiveDepthDecision, ...]:
    source = Path(path)
    if not source.is_file():
        return ()
    rows: list[LiveDepthDecision] = []
    with source.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
                completed = tuple(payload.pop("completed_depths"))
                triggers = tuple(payload.pop("trigger_signal_ids"))
                reasons = tuple(payload.pop("selection_reasons"))
                rows.append(
                    LiveDepthDecision(
                        **payload,
                        completed_depths=completed,
                        trigger_signal_ids=triggers,
                        selection_reasons=reasons,
                    )
                )
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"invalid depth decision row at line {line_number}: {exc}"
                ) from exc
    if len({row.target_id for row in rows}) != len(rows):
        raise ValueError("duplicate target in depth decision file")
    return tuple(rows)


def _priority_score(
    *,
    candidate: CandidateEvent | None,
    signals: Sequence[TriggerSignal],
    lanes: Sequence[BaselineLaneRecord],
) -> float:
    if not candidate and not any(lane.status in _FAILURE_STATUSES for lane in lanes):
        return 0.0
    score = 0.0
    for signal in signals:
        score += {
            TriggerType.RISK.value: 70.0 if "OPEN" in signal.lifecycle_status else 20.0,
            TriggerType.EARNINGS.value: 65.0,
            TriggerType.OFFICIAL.value: 55.0,
            TriggerType.REPORT.value: 50.0,
            TriggerType.EXISTING_LEDGER.value: 60.0,
            TriggerType.IR.value: 45.0,
            TriggerType.NEWS.value: 30.0,
            TriggerType.MARKET.value: 15.0,
        }[signal.trigger_type]
    if candidate and candidate.active_thesis_present:
        score += 80.0
    provider_failures = sum(lane.status in _FAILURE_STATUSES for lane in lanes)
    score += min(provider_failures * 10.0, 30.0)
    return round(score, 4)


def _selection_reasons(
    *,
    candidate: CandidateEvent | None,
    signals: Sequence[TriggerSignal],
    lanes: Sequence[BaselineLaneRecord],
) -> tuple[str, ...]:
    reasons: list[str] = []
    if candidate and candidate.active_thesis_present:
        reasons.append("EXISTING_ACTIVE_THESIS")
    for trigger_type in sorted({signal.trigger_type for signal in signals}):
        reasons.append("TRIGGER_" + trigger_type)
    for lane in lanes:
        if lane.status in _FAILURE_STATUSES:
            reasons.append("PROVIDER_GAP_" + lane.lane)
    return tuple(dict.fromkeys(reasons)) or ("NO_CURRENT_TRIGGER",)


def _audit_depth_selection(
    *,
    eligible: Sequence[LiveUniverseRow],
    decisions: Sequence[LiveDepthDecision],
    config: DepthSelectionConfig,
    not_selected: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    selected_deep = sum(item.selected_for_deep for item in decisions)
    official_light = sum(item.selected_for_official_light for item in decisions)
    brain = sum(item.selected_for_brain for item in decisions)
    acquisition = sum(item.acquisition_eligible for item in decisions)
    depth_counts: dict[str, int] = {}
    for item in decisions:
        depth_counts[item.maximum_depth] = depth_counts.get(item.maximum_depth, 0) + 1
    unbounded = sum(
        any(value is None for value in budget.values())
        for item in decisions
        for budget in (item.source_task_budget, item.llm_budget, item.general_web_budget)
    )
    forced_archetype = sum(item.forced_archetype_quota for item in decisions)
    not_selected_without_reason = sum(
        not str(item.get("reason") or "").strip() for item in not_selected
    )
    critical = {
        "eligible_depth_decision_count_mismatch": int(len(decisions) != len(eligible)),
        "duplicate_depth_target": len(decisions) - len({item.target_id for item in decisions}),
        "selected_deep_empty": int(selected_deep <= 0),
        "official_light_budget_exceeded": max(0, official_light - config.max_official_light_targets),
        "deep_budget_exceeded": max(0, selected_deep - config.max_deep_candidates),
        "brain_budget_exceeded": max(0, brain - config.max_brain_candidates),
        "acquisition_budget_exceeded": max(
            0, acquisition - config.max_acquisition_candidates
        ),
        "unbounded_candidate": unbounded,
        "forced_archetype_quota": forced_archetype,
        "not_selected_without_reason": not_selected_without_reason,
    }
    return {
        "schema_version": "e2r_live_depth_selection_audit_v1",
        "as_of_date": config.as_of_date,
        "eligible_universe_count": len(eligible),
        "depth_decision_count": len(decisions),
        "selected_official_light_count": official_light,
        "selected_deep_count": selected_deep,
        "selected_brain_count": brain,
        "acquisition_eligible_count": acquisition,
        "not_selected_count": len(not_selected),
        "depth_distribution": dict(sorted(depth_counts.items())),
        "unbounded_candidate_count": unbounded,
        "forced_archetype_quota_count": forced_archetype,
        "not_selected_without_reason_count": not_selected_without_reason,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
    }


def _unique_universe(rows: Sequence[LiveUniverseRow]) -> dict[str, LiveUniverseRow]:
    result: dict[str, LiveUniverseRow] = {}
    for row in rows:
        symbol = str(row.symbol or "")
        if not symbol or symbol in result:
            raise ValueError("eligible depth universe has missing or duplicate symbol")
        result[symbol] = row
    return result


def _unique_candidates(
    rows: Sequence[CandidateEvent],
    universe: Mapping[str, LiveUniverseRow],
) -> dict[str, CandidateEvent]:
    result: dict[str, CandidateEvent] = {}
    for row in rows:
        if row.target_id not in universe:
            raise ValueError("depth candidate is outside eligible universe")
        if row.target_id in result:
            raise ValueError("duplicate target candidate entered depth selection")
        result[row.target_id] = row
    return result


def _unique_signals(
    rows: Sequence[TriggerSignal],
    universe: Mapping[str, LiveUniverseRow],
) -> dict[str, TriggerSignal]:
    result: dict[str, TriggerSignal] = {}
    for row in rows:
        if row.target_id not in universe:
            raise ValueError("depth trigger is outside eligible universe")
        if row.trigger_signal_id in result:
            raise ValueError("duplicate trigger signal entered depth selection")
        result[row.trigger_signal_id] = row
    return result


__all__ = [
    "DEPTH_DECISION_SCHEMA_VERSION",
    "CurrentDepthSelector",
    "DepthSelectionConfig",
    "DepthSelectionResult",
    "LiveDepth",
    "LiveDepthDecision",
    "load_depth_decisions",
    "write_depth_selection",
]
