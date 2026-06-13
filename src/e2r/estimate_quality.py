"""Source-quality guards for forward estimate and revision metrics."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Mapping, Sequence

from .evidence_ids import stable_consensus_evidence_id, stable_revision_evidence_id
from .models import ConsensusRevision, ConsensusSnapshot, ResearchReport


CONSENSUS_METRICS: tuple[str, ...] = (
    "sales_e",
    "op_e",
    "eps_e",
    "fcf_e",
    "per_e",
    "pbr_e",
    "target_price",
)

REVISION_METRICS: tuple[str, ...] = (
    "eps_revision_1m",
    "op_revision_1m",
    "fcf_revision_1m",
    "target_price_revision_1m",
)

REVISION_OUTLIER_ABS_PCT = 300.0


@dataclass(frozen=True)
class EstimateMetricCandidate:
    metric: str
    value: float
    source: str
    source_quality: int
    date: date
    fiscal_year: int | None = None
    evidence_id: str | None = None
    parser_confidence: float | None = None
    score_eligible: bool = True
    analyst_count: int | None = None
    weak_reasons: tuple[str, ...] = ()
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "weak_reasons", tuple(self.weak_reasons))
        object.__setattr__(self, "parsed_fields", dict(self.parsed_fields))


@dataclass(frozen=True)
class EstimateMetricSelection:
    metric: str
    selected_value: float | None
    selected_source: str | None
    selected_quality: int | None
    selected_evidence_id: str | None = None
    quarantined_count: int = 0
    conflict_count: int = 0
    outlier_count: int = 0
    weak_reasons: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "weak_reasons", tuple(self.weak_reasons))


@dataclass(frozen=True)
class EstimateQualityContext:
    selections: Mapping[str, EstimateMetricSelection]
    revision_selection: EstimateMetricSelection
    diagnostic_scores: Mapping[str, float]
    source_fields: Mapping[str, float | str]

    def value(self, metric: str) -> float | None:
        selection = self.selections.get(metric)
        return selection.selected_value if selection is not None else None


def build_estimate_quality_context(inputs: Any) -> EstimateQualityContext:
    """Build one deterministic source-quality context for feature scoring."""

    consensus_candidates = _consensus_candidates(tuple(inputs.consensus), tuple(inputs.research_reports))
    selections: dict[str, EstimateMetricSelection] = {}
    for metric in CONSENSUS_METRICS:
        metric_candidates = tuple(candidate for candidate in consensus_candidates if candidate.metric == metric)
        selections[metric] = (
            select_best_consensus_metric(metric_candidates)
            if metric_candidates
            else EstimateMetricSelection(metric=metric, selected_value=None, selected_source=None, selected_quality=None)
        )

    revision_candidates = _revision_candidates(tuple(inputs.consensus_revisions))
    revision_metric_selections = {
        metric: (
            select_best_consensus_metric(metric_candidates)
            if (metric_candidates := tuple(candidate for candidate in revision_candidates if candidate.metric == metric))
            else EstimateMetricSelection(metric=metric, selected_value=None, selected_source=None, selected_quality=None)
        )
        for metric in REVISION_METRICS
    }
    selections.update(revision_metric_selections)
    revision_selection = _aggregate_revision_selection(tuple(revision_metric_selections.values()))
    diagnostics, source_fields = estimate_quality_diagnostics(tuple(selections.values()), revision_selection)
    return EstimateQualityContext(
        selections=selections,
        revision_selection=revision_selection,
        diagnostic_scores=diagnostics,
        source_fields=source_fields,
    )


def consensus_source_quality(source: str | None, parsed_fields: Mapping[str, Any] | None = None) -> int:
    fields = parsed_fields or {}
    source_text = (source or fields.get("source") or "unknown").strip()
    lowered = source_text.lower()
    proxy_quality = str(fields.get("consensus_proxy_quality") or "").strip().lower()
    if fields.get("search_snippet_only") or fields.get("search_snippet_date_unverified"):
        return 10
    if lowered == "company_guide_snapshot":
        return 90
    if lowered == "company_guide_recent_report":
        return 75
    if lowered == "report_proxy":
        if proxy_quality == "source_backed_revision" and fields.get("consensus_proxy_score_eligible") is not False:
            return 60
        if proxy_quality == "full_text_report" and fields.get("consensus_proxy_score_eligible") is not False:
            return 60
        return 35
    if "snippet" in lowered or lowered in {"news", "search"}:
        return 10
    if lowered in {"consensus-csv", "file", "fixture-consensus", "historicalconsensus", "structured_revision", "test"}:
        return 90
    if "consensus" in lowered and "proxy" not in lowered:
        return 90
    if lowered in {"unknown", "unknown-source"}:
        return 55
    return 70


def is_report_derived_estimate(source: str | None, parsed_fields: Mapping[str, Any] | None = None) -> bool:
    fields = parsed_fields or {}
    source_text = (source or fields.get("source") or "").strip().lower()
    return (
        source_text in {"report_proxy", "company_guide_recent_report"}
        or fields.get("derived_from_source_type") == "research_report"
        or bool(fields.get("consensus_proxy_created"))
    )


def is_independent_consensus(item: ConsensusSnapshot | ConsensusRevision) -> bool:
    return not is_report_derived_estimate(getattr(item, "source", None), getattr(item, "parsed_fields", {}))


def select_best_consensus_metric(candidates: Sequence[EstimateMetricCandidate]) -> EstimateMetricSelection:
    if not candidates:
        return EstimateMetricSelection(metric="unknown", selected_value=None, selected_source=None, selected_quality=None)
    metric = candidates[0].metric
    outlier_count = sum(1 for candidate in candidates if _is_revision_outlier(candidate))
    weak_reasons: list[str] = []
    eligible: list[EstimateMetricCandidate] = []
    quarantined_count = 0
    for candidate in candidates:
        weak_reasons.extend(candidate.weak_reasons)
        if _is_revision_outlier(candidate):
            quarantined_count += 1
            continue
        if not candidate.score_eligible:
            quarantined_count += 1
            continue
        eligible.append(candidate)
    if not eligible:
        return EstimateMetricSelection(
            metric=metric,
            selected_value=None,
            selected_source=None,
            selected_quality=None,
            quarantined_count=quarantined_count,
            outlier_count=outlier_count,
            weak_reasons=tuple(dict.fromkeys(weak_reasons)),
        )
    selected = max(
        eligible,
        key=lambda candidate: (
            candidate.source_quality,
            candidate.analyst_count or 0,
            candidate.date,
            candidate.fiscal_year or 0,
        ),
    )
    conflict_count = 0
    for candidate in candidates:
        if candidate is selected:
            continue
        if _values_conflict(selected.value, candidate.value):
            conflict_count += 1
            if candidate.source_quality < selected.source_quality:
                quarantined_count += 1
    return EstimateMetricSelection(
        metric=metric,
        selected_value=selected.value,
        selected_source=selected.source,
        selected_quality=selected.source_quality,
        selected_evidence_id=selected.evidence_id,
        quarantined_count=quarantined_count,
        conflict_count=conflict_count,
        outlier_count=outlier_count,
        weak_reasons=tuple(dict.fromkeys(weak_reasons)),
    )


def estimate_quality_diagnostics(
    selections: Sequence[EstimateMetricSelection],
    revision_selection: EstimateMetricSelection,
) -> tuple[dict[str, float], dict[str, float | str]]:
    diagnostics: dict[str, float] = {}
    source_fields: dict[str, float | str] = {}
    conflict_count = sum(selection.conflict_count for selection in selections)
    quarantined_count = sum(selection.quarantined_count for selection in selections)
    outlier_count = sum(selection.outlier_count for selection in selections)
    diagnostics["estimate_conflict_count_capped"] = min(float(conflict_count), 100.0)
    diagnostics["estimate_proxy_quarantined_count_capped"] = min(float(quarantined_count), 100.0)
    diagnostics["estimate_revision_outlier_count_capped"] = min(float(outlier_count), 100.0)
    for selection in selections:
        label = _metric_label(selection.metric)
        if selection.selected_quality is not None:
            diagnostics[f"estimate_selected_{label}_source_quality"] = float(min(selection.selected_quality, 100))
        if selection.selected_source:
            source_fields[f"estimate_selected_{label}_source"] = selection.selected_source
        else:
            diagnostics[f"estimate_missing_{label}_source"] = 100.0
        if selection.selected_evidence_id:
            source_fields[f"estimate_selected_{label}_evidence_id"] = selection.selected_evidence_id
    if revision_selection.selected_quality is not None:
        diagnostics["estimate_selected_revision_source_quality"] = float(min(revision_selection.selected_quality, 100))
    if revision_selection.selected_source:
        source_fields["estimate_selected_revision_source"] = revision_selection.selected_source
    else:
        diagnostics["estimate_missing_revision_source"] = 100.0
    return diagnostics, source_fields


def _consensus_candidates(
    consensus: Sequence[ConsensusSnapshot],
    reports: Sequence[ResearchReport],
) -> tuple[EstimateMetricCandidate, ...]:
    candidates: list[EstimateMetricCandidate] = []
    for item in consensus:
        fields = dict(item.parsed_fields)
        quality = consensus_source_quality(item.source, fields)
        score_eligible = _score_eligible(item.source, quality, fields)
        weak_reasons = _weak_reasons(fields)
        evidence_id = stable_consensus_evidence_id(
            symbol=item.symbol,
            estimate_date=item.date,
            fiscal_year=item.fiscal_year,
            source=item.source,
        )
        for metric in CONSENSUS_METRICS:
            value = _to_float(getattr(item, metric, None))
            if value is None:
                continue
            candidates.append(
                EstimateMetricCandidate(
                    metric=metric,
                    value=value,
                    source=item.source,
                    source_quality=quality,
                    date=item.date,
                    fiscal_year=item.fiscal_year,
                    evidence_id=evidence_id,
                    parser_confidence=_to_float(fields.get("parser_confidence")),
                    score_eligible=score_eligible,
                    analyst_count=item.analyst_count,
                    weak_reasons=weak_reasons,
                    parsed_fields=fields,
                )
            )
    for report in reports:
        fields = dict(report.parsed_fields)
        if fields.get("source") != "company_guide_recent_report":
            continue
        source = "company_guide_recent_report"
        quality = consensus_source_quality(source, fields)
        fiscal_year = _report_fiscal_year(report)
        evidence_id = f"research:{report.symbol}:{report.publish_date.isoformat()}:{report.broker}"
        for metric, value in (
            ("sales_e", report.fy1_sales),
            ("op_e", report.fy1_op),
            ("eps_e", report.fy1_eps),
            ("per_e", report.est_per),
            ("pbr_e", report.est_pbr),
            ("target_price", report.target_price),
        ):
            numeric = _to_float(value)
            if numeric is None:
                continue
            candidates.append(
                EstimateMetricCandidate(
                    metric=metric,
                    value=numeric,
                    source=source,
                    source_quality=quality,
                    date=report.publish_date,
                    fiscal_year=fiscal_year,
                    evidence_id=evidence_id,
                    parser_confidence=_to_float(fields.get("parser_confidence")),
                    score_eligible=True,
                    parsed_fields={**fields, "derived_from_source_type": "research_report"},
                )
            )
    return tuple(candidates)


def _revision_candidates(revisions: Sequence[ConsensusRevision]) -> tuple[EstimateMetricCandidate, ...]:
    candidates: list[EstimateMetricCandidate] = []
    for item in revisions:
        fields = dict(item.parsed_fields)
        quality = consensus_source_quality(item.source, fields)
        score_eligible = _score_eligible(item.source, quality, fields)
        weak_reasons = _weak_reasons(fields)
        evidence_id = stable_revision_evidence_id(
            symbol=item.symbol,
            estimate_date=item.date,
            fiscal_year=item.fiscal_year,
            source=item.source,
        )
        for metric in REVISION_METRICS:
            value = _percent_value(_to_float(getattr(item, metric, None)))
            if value is None:
                continue
            candidates.append(
                EstimateMetricCandidate(
                    metric=metric,
                    value=value,
                    source=item.source,
                    source_quality=quality,
                    date=item.date,
                    fiscal_year=item.fiscal_year,
                    evidence_id=evidence_id,
                    parser_confidence=_to_float(fields.get("parser_confidence")),
                    score_eligible=score_eligible,
                    analyst_count=item.analyst_count_change,
                    weak_reasons=weak_reasons,
                    parsed_fields=fields,
                )
            )
    return tuple(candidates)


def _aggregate_revision_selection(selections: Sequence[EstimateMetricSelection]) -> EstimateMetricSelection:
    available = tuple(selection for selection in selections if selection.selected_value is not None)
    if not available:
        return EstimateMetricSelection(
            metric="revision",
            selected_value=None,
            selected_source=None,
            selected_quality=None,
            quarantined_count=sum(selection.quarantined_count for selection in selections),
            conflict_count=sum(selection.conflict_count for selection in selections),
            outlier_count=sum(selection.outlier_count for selection in selections),
        )
    selected = max(available, key=lambda selection: selection.selected_value or 0.0)
    return EstimateMetricSelection(
        metric="revision",
        selected_value=selected.selected_value,
        selected_source=selected.selected_source,
        selected_quality=selected.selected_quality,
        selected_evidence_id=selected.selected_evidence_id,
        quarantined_count=sum(selection.quarantined_count for selection in selections),
        conflict_count=sum(selection.conflict_count for selection in selections),
        outlier_count=sum(selection.outlier_count for selection in selections),
    )


def _score_eligible(source: str | None, quality: int, fields: Mapping[str, Any]) -> bool:
    if fields.get("consensus_proxy_score_eligible") is False:
        return False
    if fields.get("search_snippet_only") or fields.get("search_snippet_date_unverified"):
        return False
    if fields.get("green_allowed_by_date") is False:
        return False
    if (source or "").strip().lower() == "report_proxy" and quality < 60:
        return False
    return quality > 10


def _weak_reasons(fields: Mapping[str, Any]) -> tuple[str, ...]:
    raw = fields.get("consensus_proxy_weak_reasons") or fields.get("weak_reasons") or ()
    if isinstance(raw, str):
        return (raw,)
    if isinstance(raw, Sequence):
        return tuple(str(item) for item in raw if item)
    return ()


def _is_revision_outlier(candidate: EstimateMetricCandidate) -> bool:
    return candidate.metric in REVISION_METRICS and abs(candidate.value) > REVISION_OUTLIER_ABS_PCT


def _values_conflict(selected_value: float, candidate_value: float) -> bool:
    if selected_value <= 0 or candidate_value <= 0:
        return False
    base = max(abs(selected_value), abs(candidate_value), 1.0)
    return abs(selected_value - candidate_value) / base >= 0.50


def _report_fiscal_year(report: ResearchReport) -> int:
    value = _to_float(report.parsed_fields.get("fy1_fiscal_year") or report.parsed_fields.get("fiscal_year"))
    if value is not None and value >= 1900:
        return int(value)
    return report.publish_date.year


def _metric_label(metric: str) -> str:
    labels = {
        "sales_e": "sales",
        "op_e": "op",
        "eps_e": "eps",
        "fcf_e": "fcf",
        "per_e": "per",
        "pbr_e": "pbr",
        "target_price": "target_price",
        "eps_revision_1m": "eps_revision",
        "op_revision_1m": "op_revision",
        "fcf_revision_1m": "fcf_revision",
        "target_price_revision_1m": "target_price_revision",
    }
    return labels.get(metric, metric)


def _to_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _percent_value(value: float | None) -> float | None:
    if value is None:
        return None
    if -2.0 <= value <= 2.0:
        return value * 100.0
    return value


__all__ = [
    "EstimateMetricCandidate",
    "EstimateMetricSelection",
    "EstimateQualityContext",
    "REVISION_OUTLIER_ABS_PCT",
    "build_estimate_quality_context",
    "consensus_source_quality",
    "estimate_quality_diagnostics",
    "is_independent_consensus",
    "is_report_derived_estimate",
    "select_best_consensus_metric",
]
