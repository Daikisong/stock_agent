"""Historical Layer-1 recall checks for E2R candidate routing."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Mapping, Sequence

from e2r.historical_cases import HistoricalCase, load_historical_cases
from e2r.models import Stage


LAYER_NONE = "none"
LAYER_RADAR = "radar"
LAYER_EVENT_SEARCH = "event_search"
LAYER_DEEP_RESEARCH = "deep_research"
LAYER_STAGE2_OR_HIGHER = "stage2_or_higher"

_LAYER_ORDER: Mapping[str, int] = {
    LAYER_NONE: 0,
    LAYER_RADAR: 1,
    LAYER_EVENT_SEARCH: 2,
    LAYER_DEEP_RESEARCH: 3,
    LAYER_STAGE2_OR_HIGHER: 4,
}

_STAGE_ORDER: Mapping[Stage, int] = {
    Stage.STAGE_0: 0,
    Stage.STAGE_1: 1,
    Stage.STAGE_2: 2,
    Stage.STAGE_3_RED: 3,
    Stage.STAGE_3_YELLOW: 3,
    Stage.STAGE_3_GREEN: 3,
    Stage.STAGE_4A: 4,
    Stage.STAGE_4B: 4,
    Stage.STAGE_4C: 4,
    Stage.STAGE_5: 5,
}


@dataclass(frozen=True)
class Layer1RecallCase:
    """Expected Layer-1 routing for one historical case."""

    case_id: str
    symbol: str
    company_name: str
    as_of_date: date
    expected_trigger_date: date
    expected_layer1_min_result: str
    expected_final_stage: Stage | None = None
    evidence_type_expected: tuple[str, ...] = ()
    must_not_use_future_data: bool = True


@dataclass(frozen=True)
class Layer1RecallResult:
    """Detection result for one historical Layer-1 case."""

    case_id: str
    symbol: str
    company_name: str
    expected_layer1_min_result: str
    actual_layer1_result: str
    layer1_score: float
    rank: int | None
    reached_event_search: bool
    reached_deep_research: bool
    reached_stage2_or_higher: bool
    days_from_expected_trigger_to_detection: int | None
    false_none_reason: str | None
    final_stage: Stage
    expected_final_stage: Stage | None
    future_data_used: bool
    evidence_types_seen: tuple[str, ...]

    @property
    def passed_minimum(self) -> bool:
        return _layer_rank(self.actual_layer1_result) >= _layer_rank(self.expected_layer1_min_result)


@dataclass(frozen=True)
class Layer1RecallSummary:
    """Aggregated recall metrics across historical cases."""

    results: tuple[Layer1RecallResult, ...]
    recall_top_50: float
    recall_top_100: float
    recall_top_200: float
    reached_event_search: int
    reached_deep_research: int
    reached_stage2_or_higher: int
    failed_cases: tuple[Layer1RecallResult, ...]


def evaluate_layer1_recall(
    cases: Sequence[HistoricalCase] | None = None,
    expectations: Mapping[str, Layer1RecallCase] | None = None,
) -> Layer1RecallSummary:
    """Evaluate whether historical cases would reach Layer-2 routing.

    This deliberately checks recall only. A case reaching event search is not
    treated as a Stage 3-Green decision; final stage precision remains owned by
    deterministic scoring and Red Team checks.
    """

    case_items = tuple(cases or load_historical_cases())
    expected = dict(expectations or {})
    raw_results = [evaluate_layer1_recall_case(case, expected.get(case.case_id)) for case in case_items]
    ranked = sorted(raw_results, key=lambda item: (-item.layer1_score, item.case_id))
    rank_by_case = {item.case_id: index + 1 for index, item in enumerate(ranked)}
    results = tuple(_with_rank(item, rank_by_case[item.case_id]) for item in raw_results)
    detected = tuple(item for item in results if item.passed_minimum and not item.future_data_used)
    total = max(1, len(results))
    return Layer1RecallSummary(
        results=tuple(sorted(results, key=lambda item: item.rank or 9999)),
        recall_top_50=sum(1 for item in detected if (item.rank or 9999) <= 50) / total,
        recall_top_100=sum(1 for item in detected if (item.rank or 9999) <= 100) / total,
        recall_top_200=sum(1 for item in detected if (item.rank or 9999) <= 200) / total,
        reached_event_search=sum(1 for item in results if item.reached_event_search),
        reached_deep_research=sum(1 for item in results if item.reached_deep_research),
        reached_stage2_or_higher=sum(1 for item in results if item.reached_stage2_or_higher),
        failed_cases=tuple(item for item in results if not item.passed_minimum or item.future_data_used),
    )


def evaluate_layer1_recall_case(
    case: HistoricalCase,
    expectation: Layer1RecallCase | None = None,
) -> Layer1RecallResult:
    expected = expectation or default_expectation_for_case(case)
    evidence_types = _visible_evidence_types(case, expected.expected_trigger_date)
    actual_layer = _actual_layer_from_evidence(evidence_types)
    final_stage = case.classify().stage
    reached_stage2 = _stage_rank(final_stage) >= 2
    if reached_stage2 and actual_layer == LAYER_NONE:
        actual_layer = LAYER_STAGE2_OR_HIGHER
    score = _layer1_score(evidence_types, final_stage)
    future_used = _uses_future_data(case, expected.expected_trigger_date) if expected.must_not_use_future_data else False
    missed = _layer_rank(actual_layer) < _layer_rank(expected.expected_layer1_min_result)
    reason = failure_reason_for_layer1_miss(case, evidence_types) if missed or future_used else None
    return Layer1RecallResult(
        case_id=case.case_id,
        symbol=case.symbol,
        company_name=case.company_name,
        expected_layer1_min_result=expected.expected_layer1_min_result,
        actual_layer1_result=actual_layer,
        layer1_score=score,
        rank=None,
        reached_event_search=_layer_rank(actual_layer) >= _layer_rank(LAYER_EVENT_SEARCH),
        reached_deep_research=_layer_rank(actual_layer) >= _layer_rank(LAYER_DEEP_RESEARCH),
        reached_stage2_or_higher=reached_stage2,
        days_from_expected_trigger_to_detection=0 if actual_layer != LAYER_NONE else None,
        false_none_reason=reason,
        final_stage=final_stage,
        expected_final_stage=expected.expected_final_stage,
        future_data_used=future_used,
        evidence_types_seen=evidence_types,
    )


def default_expectation_for_case(case: HistoricalCase) -> Layer1RecallCase:
    """Build conservative default expectations from fixture metadata."""

    expected_min = LAYER_EVENT_SEARCH
    if case.expected_stage in {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW} and case.research_reports:
        expected_min = LAYER_DEEP_RESEARCH
    evidence_expected = []
    if case.disclosures:
        evidence_expected.append("disclosure")
    if case.research_reports:
        evidence_expected.append("research_report")
    if case.news_items:
        evidence_expected.append("news")
    if case.financial_actuals:
        evidence_expected.append("financial_actual")
    if case.price_bars:
        evidence_expected.append("price")
    return Layer1RecallCase(
        case_id=case.case_id,
        symbol=case.symbol,
        company_name=case.company_name,
        as_of_date=case.stage3_date,
        expected_trigger_date=case.stage3_date,
        expected_layer1_min_result=expected_min,
        expected_final_stage=case.expected_stage,
        evidence_type_expected=tuple(evidence_expected),
    )


def failure_reason_for_layer1_miss(case: HistoricalCase, evidence_types: Sequence[str]) -> str:
    """Classify why a historical case failed Layer-1 recall."""

    if not case.instrument:
        return "not_in_universe"
    if not evidence_types:
        return "source_missing"
    if "research_report" not in evidence_types and case.research_reports:
        return "no_report_radar_path"
    if "disclosure" not in evidence_types and case.disclosures:
        return "no_disclosure_signal"
    if "price" not in evidence_types and case.price_bars:
        return "no_price_signal"
    if any(item in evidence_types for item in ("research_report", "disclosure", "news", "financial_actual")):
        return "evidence_available_but_not_scored"
    return "unknown"


def _visible_evidence_types(case: HistoricalCase, trigger_date: date) -> tuple[str, ...]:
    types: list[str] = []
    if any(item.as_of_date <= trigger_date for item in case.research_reports):
        types.append("research_report")
    if any(item.available_at.date() <= trigger_date for item in case.disclosures):
        types.append("disclosure")
    if any(item.as_of_date <= trigger_date for item in case.news_items):
        types.append("news")
    if any(item.as_of_date <= trigger_date for item in case.financial_actuals):
        types.append("financial_actual")
    if any(item.as_of_date <= trigger_date for item in case.consensus):
        types.append("consensus")
    if any(item.as_of_date <= trigger_date for item in case.consensus_revisions):
        types.append("consensus_revision")
    if _has_price_signal(case, trigger_date):
        types.append("price")
    return tuple(dict.fromkeys(types))


def _actual_layer_from_evidence(evidence_types: Sequence[str]) -> str:
    types = set(evidence_types)
    if "research_report" in types:
        return LAYER_DEEP_RESEARCH
    if types & {"disclosure", "news", "financial_actual", "consensus_revision", "price"}:
        return LAYER_EVENT_SEARCH
    return LAYER_NONE


def _layer1_score(evidence_types: Sequence[str], final_stage: Stage) -> float:
    weights = {
        "research_report": 45.0,
        "disclosure": 25.0,
        "news": 15.0,
        "financial_actual": 15.0,
        "consensus": 15.0,
        "consensus_revision": 20.0,
        "price": 10.0,
    }
    score = sum(weights.get(item, 0.0) for item in set(evidence_types))
    if _stage_rank(final_stage) >= 2:
        score += 10.0
    return round(min(100.0, score), 4)


def _uses_future_data(case: HistoricalCase, trigger_date: date) -> bool:
    if any(item.as_of_date > trigger_date for item in case.research_reports):
        return True
    if any(item.available_at.date() > trigger_date for item in case.disclosures):
        return True
    if any(item.as_of_date > trigger_date for item in case.news_items):
        return True
    if any(item.as_of_date > trigger_date for item in case.financial_actuals):
        return True
    if any(item.as_of_date > trigger_date for item in case.consensus):
        return True
    if any(item.as_of_date > trigger_date for item in case.consensus_revisions):
        return True
    return False


def _has_price_signal(case: HistoricalCase, trigger_date: date) -> bool:
    bars = sorted((item for item in case.price_bars if item.as_of_date <= trigger_date), key=lambda item: item.date)
    if len(bars) < 2:
        return False
    first, latest = bars[0], bars[-1]
    if first.close <= 0:
        return False
    return latest.close / first.close - 1.0 >= 0.30


def _with_rank(result: Layer1RecallResult, rank: int) -> Layer1RecallResult:
    return Layer1RecallResult(
        case_id=result.case_id,
        symbol=result.symbol,
        company_name=result.company_name,
        expected_layer1_min_result=result.expected_layer1_min_result,
        actual_layer1_result=result.actual_layer1_result,
        layer1_score=result.layer1_score,
        rank=rank,
        reached_event_search=result.reached_event_search,
        reached_deep_research=result.reached_deep_research,
        reached_stage2_or_higher=result.reached_stage2_or_higher,
        days_from_expected_trigger_to_detection=result.days_from_expected_trigger_to_detection,
        false_none_reason=result.false_none_reason,
        final_stage=result.final_stage,
        expected_final_stage=result.expected_final_stage,
        future_data_used=result.future_data_used,
        evidence_types_seen=result.evidence_types_seen,
    )


def _layer_rank(layer: str) -> int:
    return _LAYER_ORDER.get(layer, 0)


def _stage_rank(stage: Stage) -> int:
    return _STAGE_ORDER.get(stage, 0)


__all__ = [
    "LAYER_DEEP_RESEARCH",
    "LAYER_EVENT_SEARCH",
    "LAYER_NONE",
    "LAYER_RADAR",
    "LAYER_STAGE2_OR_HIGHER",
    "Layer1RecallCase",
    "Layer1RecallResult",
    "Layer1RecallSummary",
    "default_expectation_for_case",
    "evaluate_layer1_recall",
    "evaluate_layer1_recall_case",
    "failure_reason_for_layer1_miss",
]
