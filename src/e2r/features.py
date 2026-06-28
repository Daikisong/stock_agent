"""Deterministic feature engineering from raw E2R data domains."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
import json
import math
from typing import Any, Mapping, Protocol, Sequence

from .agentic import (
    LEGACY_DIRECT_RISK_FIELDS,
    V2_HARD_BREAK_SOURCE_QUORUM_KEY,
    MentionSourceKind,
    V2_SCORE_ELIGIBLE_CLAIMS_KEY,
    audit_legacy_direct_score_fields,
    audit_legacy_parser_score_claim_fields,
    claim_backed_parsed_fields,
    evidence_contract_for_archetype,
    mentions_from_parsed_fields,
)
from .archetype_classifier import classify_v12_archetype
from .calibration.taxonomy import normalise_canonical_archetype_id, normalise_large_sector_id
from .estimate_quality import (
    EstimateQualityContext,
    REVISION_OUTLIER_ABS_PCT,
    build_estimate_quality_context,
    is_independent_consensus,
    is_report_derived_estimate,
)
from .evidence_ids import stable_consensus_evidence_id, stable_news_evidence_id, stable_revision_evidence_id
from .models import (
    ConsensusRevision,
    ConsensusSnapshot,
    DisclosureEvent,
    FinancialActual,
    IndustrialSubScores,
    Instrument,
    Market,
    NewsItem,
    PriceBar,
    ResearchReport,
    ShortageType,
)
from .red_team import HARD_BREAK_SIGNALS, RedTeamSignals
from .scoring import DeterministicScorer, ScoringPayload
from .sector_profiles import SectorProfile, infer_sector_profile, profile_for_archetype, profile_id


EVIDENCE_FAMILIES: tuple[str, ...] = (
    "price",
    "financial_actual",
    "disclosure",
    "research_report",
    "consensus",
    "consensus_revision",
    "news",
)
_AGENT_EXTRACTED_FIELD_SOURCE_KEY = "agent_extracted_field_source"
_AGENT_FIELD_TEXT_EXCLUDE_PREFIXES = ("compiled_", "claim_")
_AGENT_FIELD_TEXT_EXCLUDE_KEYS = {
    _AGENT_EXTRACTED_FIELD_SOURCE_KEY,
    "claim_ledger_version",
}
_AGENT_SCORE_ELIGIBLE_SYNTHETIC_KEYS = {
    "theme_transition_detected",
    "emerging_theme_active",
    "emerging_theme_id",
}

_REVISION_NUMERIC_FIELD_KEYS = {
    "eps_revision_pct",
    "eps_revision_1m_pct",
    "eps_revision_1m",
    "op_revision_pct",
    "op_revision_1m_pct",
    "op_revision_1m",
    "fcf_revision_pct",
    "fcf_revision_1m_pct",
    "fcf_revision_1m",
    "target_price_revision_pct",
    "target_revision_pct",
    "target_price_revision_1m",
}

_LEGACY_SEVERE_RISK_FIELDS_REQUIRING_V2 = set(LEGACY_DIRECT_RISK_FIELDS)

_SCORE_COMPONENT_CLAIM_KEYWORDS: Mapping[str, tuple[str, ...]] = {
    "eps_fcf_explosion": (
        "actual",
        "cashflow",
        "cash_flow",
        "earnings",
        "eps",
        "fcf",
        "financial",
        "margin",
        "net_income",
        "op_",
        "operating_profit",
        "opm",
        "profit",
        "revision",
        "sales",
    ),
    "earnings_visibility": (
        "actual",
        "allocation",
        "arr",
        "backlog",
        "booked",
        "cashflow",
        "cash_flow",
        "balance_sheet",
        "channel",
        "contract",
        "customer",
        "delivery",
        "demand",
        "direct_company_cash",
        "export",
        "fcf",
        "financial",
        "hbm",
        "implementation",
        "order",
        "platform",
        "policy",
        "preorder",
        "pre_sold",
        "project",
        "reimbursement",
        "recurring",
        "regulatory",
        "retention",
        "revenue",
        "royalty",
        "rpo",
        "shipment",
        "subsidy",
        "visibility",
        "volume",
    ),
    "bottleneck_pricing": (
        "allocation",
        "approval",
        "arpu",
        "arr",
        "asp",
        "balance_sheet",
        "bottleneck",
        "call_off",
        "capacity",
        "capa",
        "cash_collection",
        "channel",
        "constraint",
        "csm",
        "direct_company_cash",
        "export",
        "hbm",
        "insurance",
        "inventory",
        "k_ics",
        "lead_time",
        "loss_ratio",
        "margin",
        "occupancy",
        "operating_leverage",
        "pf_",
        "platform",
        "policy",
        "pre_sold",
        "presale",
        "project",
        "pricing",
        "regulatory",
        "reimbursement",
        "repeat",
        "reserve",
        "retention",
        "revenue",
        "risk",
        "royalty",
        "shortage",
        "software",
        "sold",
        "spread",
        "subsidy",
        "supply",
        "tightness",
        "trial",
        "volume",
    ),
    "market_mispricing": (
        "allocation",
        "capacity",
        "customer",
        "estimate",
        "approval",
        "arpu",
        "arr",
        "balance_sheet",
        "cash",
        "channel",
        "csm",
        "hbm",
        "insurance",
        "k_ics",
        "loss_ratio",
        "mispricing",
        "operating_leverage",
        "pf_",
        "platform",
        "policy",
        "price",
        "pricing",
        "project",
        "rerating",
        "regulatory",
        "reimbursement",
        "repeat",
        "reserve",
        "retention",
        "revision",
        "risk",
        "royalty",
        "shortage",
        "software",
        "structural",
        "subsidy",
        "target",
        "trial",
        "upside",
        "valuation",
        "volume",
    ),
    "valuation_rerating": (
        "allocation",
        "approval",
        "arpu",
        "arr",
        "balance_sheet",
        "capacity",
        "cash",
        "channel",
        "control_premium",
        "csm",
        "customer",
        "estimate",
        "hbm",
        "insurance",
        "k_ics",
        "loss_ratio",
        "multiple",
        "pbr",
        "per",
        "pf_",
        "platform",
        "policy",
        "premium",
        "project",
        "rerating",
        "regulatory",
        "reimbursement",
        "reserve",
        "retention",
        "revision",
        "risk",
        "roe",
        "royalty",
        "shortage",
        "software",
        "structural",
        "subsidy",
        "target",
        "tender",
        "trial",
        "upside",
        "valuation",
        "volume",
    ),
    "capital_allocation": (
        "buyback",
        "cancellation",
        "capex",
        "capital",
        "capacity_expansion",
        "capacity_precommitted",
        "dividend",
        "payout",
        "shareholder",
        "treasury",
    ),
}


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    if not math.isfinite(float(value)):
        return low
    return max(low, min(high, value))


def _round(value: float) -> float:
    return round(value, 4)


def _to_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number):
        return None
    return number


def _to_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _percent_value(value: float | None) -> float | None:
    if value is None:
        return None
    if -2.0 <= value <= 2.0:
        return value * 100.0
    return value


def _news_source_url(item: NewsItem) -> str | None:
    return str(item.parsed_fields.get("source_url") or item.parsed_fields.get("url") or "").strip() or None


def _news_evidence_id(item: NewsItem, fallback_symbol: str) -> str:
    return str(item.parsed_fields.get("evidence_id") or "").strip() or stable_news_evidence_id(
        symbol=item.symbol or fallback_symbol,
        published_date=item.published_at.date(),
        source=item.source,
        source_url=_news_source_url(item),
        title=item.title,
    )


def _is_search_snippet_only_news(item: NewsItem) -> bool:
    return bool(item.parsed_fields.get("search_snippet_only"))


def _green_allowed_by_date(fields: Mapping[str, Any]) -> bool:
    return fields.get("green_allowed_by_date") is not False and not _to_bool(fields.get("date_unverified_document"))


def _max_or_none(values: Sequence[float | None]) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(float(value))]
    return max(clean) if clean else None


def _is_non_finite_numeric_value(value: Any) -> bool:
    if value in (None, "") or isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return not math.isfinite(float(value))
    if isinstance(value, str):
        try:
            return not math.isfinite(float(value.strip().replace(",", "")))
        except ValueError:
            return False
    return False


def _clean_parsed_field_mapping(mapping: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in mapping.items() if not _is_non_finite_numeric_value(value)}


def _primitive_matches_component(primitive_id: str, keywords: Sequence[str]) -> bool:
    normalized = primitive_id.lower()
    return any(keyword in normalized for keyword in keywords)


def _score_ratio(value: float | None, full_at: float) -> float:
    if value is None or full_at <= 0:
        return 0.0
    return _clamp(value / full_at * 100.0)


def _score_percent(value: float | None, full_at_pct: float) -> float:
    value = _percent_value(value)
    if value is None or full_at_pct <= 0:
        return 0.0
    return _clamp(value / full_at_pct * 100.0)


def _score_bool_evidence_count(fields: "_ParsedFieldSource", keys: Sequence[str], full_at_count: float) -> float:
    if full_at_count <= 0:
        return 0.0
    present_count = sum(1 for key in keys if fields.any_bool(key))
    return _clamp(present_count / full_at_count * 100.0)


def _growth_pct(forecast: float | None, actual: float | None) -> float | None:
    if forecast is None or actual is None:
        return None
    if actual <= 0 < forecast:
        return 300.0
    if actual == 0:
        return None
    return (forecast - actual) / abs(actual) * 100.0


def _safe_divide(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator is None or denominator == 0:
        return None
    return numerator / denominator


def _plausible_positive_ratio(numerator: float | None, denominator: float | None, *, max_ratio: float = 10.0) -> float | None:
    ratio = _safe_divide(numerator, denominator)
    if ratio is None or ratio <= 0.0 or ratio > max_ratio:
        return None
    return ratio


@dataclass(frozen=True)
class FeatureEngineeringInput:
    """Raw point-in-time data for one symbol."""

    symbol: str
    as_of_date: date
    company_name: str | None = None
    sector_context: str | None = None
    large_sector_id: str | None = None
    canonical_archetype_id: str | None = None
    price_bars: Sequence[PriceBar] = field(default_factory=tuple)
    financial_actuals: Sequence[FinancialActual] = field(default_factory=tuple)
    consensus: Sequence[ConsensusSnapshot] = field(default_factory=tuple)
    consensus_revisions: Sequence[ConsensusRevision] = field(default_factory=tuple)
    disclosures: Sequence[DisclosureEvent] = field(default_factory=tuple)
    research_reports: Sequence[ResearchReport] = field(default_factory=tuple)
    news_items: Sequence[NewsItem] = field(default_factory=tuple)
    agent_extracted_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.as_of_date, "as_of_date")
        if self.company_name is not None:
            object.__setattr__(self, "company_name", self.company_name.strip() or None)
        if self.sector_context is not None:
            object.__setattr__(self, "sector_context", self.sector_context.strip() or None)
        if self.large_sector_id is not None:
            object.__setattr__(self, "large_sector_id", normalise_large_sector_id(self.large_sector_id))
        if self.canonical_archetype_id is not None:
            object.__setattr__(self, "canonical_archetype_id", normalise_canonical_archetype_id(self.canonical_archetype_id))
        object.__setattr__(self, "price_bars", tuple(self.price_bars))
        object.__setattr__(self, "financial_actuals", tuple(self.financial_actuals))
        object.__setattr__(self, "consensus", tuple(self.consensus))
        object.__setattr__(self, "consensus_revisions", tuple(self.consensus_revisions))
        object.__setattr__(self, "disclosures", tuple(self.disclosures))
        object.__setattr__(self, "research_reports", tuple(self.research_reports))
        object.__setattr__(self, "news_items", tuple(self.news_items))
        object.__setattr__(self, "agent_extracted_fields", dict(self.agent_extracted_fields))
        self._validate_point_in_time()

    def _validate_point_in_time(self) -> None:
        for bar in self.price_bars:
            if bar.symbol != self.symbol:
                raise ValueError("price bar symbol must match feature input symbol")
            if bar.as_of_date > self.as_of_date:
                raise ValueError("price bar as_of_date cannot be after feature as_of_date")
        for item in self.financial_actuals:
            if item.symbol != self.symbol:
                raise ValueError("financial actual symbol must match feature input symbol")
            if item.reported_at.date() > self.as_of_date or item.as_of_date > self.as_of_date:
                raise ValueError("financial actual cannot be after feature as_of_date")
        for item in self.consensus:
            if item.symbol != self.symbol:
                raise ValueError("consensus symbol must match feature input symbol")
            if item.as_of_date > self.as_of_date or item.date > self.as_of_date:
                raise ValueError("consensus cannot be after feature as_of_date")
        for item in self.consensus_revisions:
            if item.symbol != self.symbol:
                raise ValueError("consensus revision symbol must match feature input symbol")
            if item.as_of_date > self.as_of_date or item.date > self.as_of_date:
                raise ValueError("consensus revision cannot be after feature as_of_date")
        for item in self.disclosures:
            if item.symbol != self.symbol:
                raise ValueError("disclosure symbol must match feature input symbol")
            if item.available_at.date() > self.as_of_date:
                raise ValueError("disclosure cannot be after feature as_of_date")
        for item in self.research_reports:
            if item.symbol != self.symbol:
                raise ValueError("research report symbol must match feature input symbol")
            if item.as_of_date > self.as_of_date or item.publish_date > self.as_of_date:
                raise ValueError("research report cannot be after feature as_of_date")
        for item in self.news_items:
            if item.symbol not in (None, self.symbol):
                raise ValueError("news symbol must match feature input symbol or be empty")
            if item.as_of_date > self.as_of_date or item.published_at.date() > self.as_of_date:
                raise ValueError("news cannot be after feature as_of_date")


@dataclass(frozen=True)
class FeatureEngineeringResult:
    """Output of raw-data feature engineering."""

    payload: ScoringPayload
    industrial_sub_scores: IndustrialSubScores
    shortage_type: ShortageType
    red_team_signals: RedTeamSignals
    source_fields: Mapping[str, float | str] = field(default_factory=dict)

    def score(self):
        """Return the deterministic score snapshot for the engineered payload."""

        return DeterministicScorer().score(self.payload)


class FeatureEngineer(Protocol):
    """Contract for converting raw domains into deterministic scoring inputs."""

    def engineer(self, inputs: FeatureEngineeringInput) -> FeatureEngineeringResult:
        """Build score payload and diagnostics from point-in-time raw data."""


class DeterministicFeatureEngineer:
    """Rule-based feature engineering for research fixtures and future connectors."""

    scoring_version = "e2r-2.0-cp8"

    def engineer(self, inputs: FeatureEngineeringInput) -> FeatureEngineeringResult:
        evidence_ids = self._evidence_ids(inputs)
        field_source = _ParsedFieldSource(inputs)
        estimate_quality = build_estimate_quality_context(inputs)
        inferred_sector_profile = infer_sector_profile(
            symbol=inputs.symbol,
            company_name=inputs.company_name,
            sector_custom=inputs.sector_context,
            text=field_source.text_blob(),
            parsed_fields=field_source.combined_fields(),
        )
        revision_score = self._revision_score(inputs, field_source, estimate_quality)
        price_stage_score = self._price_stage_score(inputs.price_bars)
        classification = classify_v12_archetype(
            symbol=inputs.symbol,
            sector_profile=inferred_sector_profile,
            parsed_fields=field_source.combined_fields(),
            text=field_source.text_blob(),
            company_name=inputs.company_name,
            sector_context=inputs.sector_context,
            large_sector_id=inputs.large_sector_id,
            canonical_archetype_id=inputs.canonical_archetype_id,
            price_stage_score=price_stage_score,
            revision_score=revision_score,
        )
        sector_profile = self._resolve_sector_profile_for_archetype(
            inferred_sector_profile,
            classification.canonical_archetype_id,
            explicit_canonical=inputs.canonical_archetype_id is not None,
        )
        sub_scores = self._industrial_sub_scores(field_source, evidence_ids)
        sector_metrics = self._sector_metrics(inputs, field_source, sub_scores, sector_profile, estimate_quality)
        bottleneck_diagnostics = self._bottleneck_diagnostics(field_source, sub_scores, sector_metrics)
        bridge_diagnostics = self._research_axis_bridge_diagnostics(field_source)
        parser_output_mentions = field_source.parser_output_mentions()
        legacy_direct_findings = field_source.legacy_direct_score_findings()
        legacy_parser_score_findings = field_source.legacy_parser_score_claim_findings()
        legacy_direct_mentions = field_source.legacy_direct_score_mentions(legacy_direct_findings)
        contract_coverage = self._evidence_contract_coverage(classification.canonical_archetype_id, field_source)
        components = self._components(inputs, field_source, sub_scores, sector_metrics, estimate_quality)
        risk_penalty = self._risk_penalty(field_source, sub_scores, sector_metrics["structural_visibility_quality"], sector_profile)
        fcf_quality = self._fcf_quality(inputs, field_source)
        valuation_score = self._valuation_score(inputs, field_source, estimate_quality)
        diagnostic_scores = {
            "revision_score": revision_score,
            "price_stage_score": price_stage_score,
            "fcf_quality_score": _round(fcf_quality),
            "valuation_score": _round(valuation_score),
            "sector_profile_id": profile_id(sector_profile),
            "inferred_sector_profile_id": profile_id(inferred_sector_profile),
            **{key: _round(value) for key, value in bottleneck_diagnostics.items() if isinstance(value, (int, float))},
            **bridge_diagnostics,
            "research_axis_bridge_guard_risk_penalty_points": _round(
                self._research_axis_guard_risk_penalty(field_source)
            ),
            **{key: _round(value) for key, value in sector_metrics.items()},
            **estimate_quality.diagnostic_scores,
            **self._evidence_family_diagnostics(inputs),
            **self._claim_backed_diagnostics(field_source),
            **contract_coverage["diagnostics"],
            "parser_output_mention_count_capped": min(float(len(parser_output_mentions)), 100.0),
            "legacy_direct_score_field_without_v2_claim_count_capped": min(
                float(len(legacy_direct_findings)),
                100.0,
            ),
            "legacy_parser_score_claim_without_v2_count_capped": min(
                float(len(legacy_parser_score_findings)),
                100.0,
            ),
            "legacy_direct_score_mention_count_capped": min(float(len(legacy_direct_mentions)), 100.0),
        }
        if inputs.agent_extracted_fields:
            diagnostic_scores["agent_extracted_field_count_capped"] = min(float(len(inputs.agent_extracted_fields)), 100.0)
        if field_source.any_bool("emerging_theme_active", "theme_transition_detected"):
            diagnostic_scores["emerging_theme_active"] = 100.0
            diagnostic_scores["theme_transition_detected"] = 100.0
        if field_source.any_bool("price_only_blowoff"):
            diagnostic_scores["price_only_blowoff_score"] = 100.0
        if field_source.any_bool("theme_hype_without_revenue", "ai_theme_hype_without_revenue", "missing_cashflow_bridge"):
            diagnostic_scores["theme_hype_without_revenue"] = 100.0
        if price_stage_score >= 90.0 and revision_score < 50.0:
            diagnostic_scores["theme_overheat_score"] = _round(min(100.0, price_stage_score))
        if field_source.any_bool("valuation_overheat", "token_or_theme_hype_risk"):
            diagnostic_scores["theme_overheat_score"] = max(diagnostic_scores.get("theme_overheat_score", 0.0), 100.0)
        self._apply_source_backed_bridge_metric_lifts(diagnostic_scores)

        red_team_signals = self._red_team_signals(inputs, field_source, sub_scores)
        diagnostic_scores["archetype_classifier_confidence"] = _round(classification.confidence * 100.0)
        payload = ScoringPayload(
            symbol=inputs.symbol,
            as_of_date=inputs.as_of_date,
            components=components,
            risk_penalty=risk_penalty,
            diagnostic_scores=diagnostic_scores,
            industrial_sub_scores=sub_scores,
            evidence_ids=evidence_ids,
            score_contribution_claim_ids=self._score_contribution_claim_ids(field_source, components),
            scoring_version=self.scoring_version,
            large_sector_id=classification.large_sector_id,
            canonical_archetype_id=classification.canonical_archetype_id,
        )
        source_fields: dict[str, float | str] = {
            "shortage_type": sub_scores.shortage_type.value,
            "revision_score": revision_score,
            "price_stage_score": price_stage_score,
            "fcf_quality_score": _round(fcf_quality),
            "valuation_score": _round(valuation_score),
            "sector_profile": sector_profile.value,
            "inferred_sector_profile": inferred_sector_profile.value,
            "sector_profile_resolution": self._sector_profile_resolution_reason(
                inferred_sector_profile,
                sector_profile,
                explicit_canonical=inputs.canonical_archetype_id is not None,
            ),
            "large_sector_id": classification.large_sector_id,
            "canonical_archetype_id": classification.canonical_archetype_id,
            "archetype_classification_reason": classification.reason,
            "claim_ledger_claim_ids": ",".join(field_source.claim_ids()),
            "claim_ledger_score_eligible_claim_ids": ",".join(
                _claim_ids_from_primitive_map(field_source.score_claim_ids_by_primitive())
            ),
            "claim_ledger_claim_ids_by_primitive": json.dumps(
                {
                    primitive: list(claim_ids)
                    for primitive, claim_ids in field_source.score_claim_ids_by_primitive().items()
                },
                ensure_ascii=False,
                sort_keys=True,
            ),
            "legacy_direct_score_fields_without_v2_claim": ",".join(
                tuple(dict.fromkeys(item.field_name for item in legacy_direct_findings))
            ),
            "legacy_parser_score_claim_fields_without_v2": ",".join(
                tuple(dict.fromkeys(item.field_name for item in legacy_parser_score_findings))
            ),
            "parser_output_mention_ids": ",".join(item.mention_id for item in parser_output_mentions[:200]),
            "parser_output_mention_field_names": ",".join(
                tuple(dict.fromkeys(item.field_name for item in parser_output_mentions[:200]))
            ),
            "legacy_direct_score_mention_ids": ",".join(item.mention_id for item in legacy_direct_mentions),
            **bottleneck_diagnostics,
            **bridge_diagnostics,
            **contract_coverage["source_fields"],
            "research_axis_bridge_guard_risk_penalty_points": _round(
                self._research_axis_guard_risk_penalty(field_source)
            ),
            **estimate_quality.source_fields,
            **{key: _round(value) for key, value in sector_metrics.items()},
        }
        self._apply_source_backed_bridge_metric_lifts(source_fields)
        return FeatureEngineeringResult(
            payload=payload,
            industrial_sub_scores=sub_scores,
            shortage_type=sub_scores.shortage_type,
            red_team_signals=red_team_signals,
            source_fields=source_fields,
        )

    @staticmethod
    def _apply_source_backed_bridge_metric_lifts(fields: dict[str, Any]) -> None:
        green_bridge_raw = _to_float(fields.get("source_backed_green_bridge_raw")) or 0.0
        if green_bridge_raw <= 0.0:
            return
        bridge_floor = _round(_clamp(green_bridge_raw))
        for key in ("structural_visibility_quality", "sector_visibility_score", "sector_bottleneck_score"):
            current = _to_float(fields.get(key)) or 0.0
            fields[key] = _round(max(current, bridge_floor))

    @staticmethod
    def _claim_backed_diagnostics(fields: "_ParsedFieldSource") -> dict[str, float]:
        claim_count = len(fields.claim_ids())
        primitive_count = len(fields.claim_ids_by_primitive())
        return {
            "claim_backed_claim_count_capped": min(float(claim_count), 100.0),
            "claim_backed_primitive_count_capped": min(float(primitive_count), 100.0),
        }

    @staticmethod
    def _evidence_contract_coverage(
        canonical_archetype_id: str,
        fields: "_ParsedFieldSource",
    ) -> Mapping[str, Mapping[str, float | str]]:
        contract = evidence_contract_for_archetype(canonical_archetype_id)
        if contract is None:
            return {"diagnostics": {}, "source_fields": {}}
        support_by_primitive = _score_support_claim_ids_by_primitive(fields)
        counter_by_primitive = _score_counter_claim_ids_by_primitive(fields)
        verified_by_primitive: dict[str, tuple[str, ...]] = {}
        for primitive in set(support_by_primitive) | set(counter_by_primitive):
            verified_by_primitive[primitive] = tuple(
                dict.fromkeys(
                    (*support_by_primitive.get(primitive, ()), *counter_by_primitive.get(primitive, ()))
                )
            )
        present = tuple(item for item in contract.required_primitives if verified_by_primitive.get(item))
        missing = tuple(item for item in contract.required_primitives if item not in present)
        positive_present = tuple(item for item in contract.positive_primitives if support_by_primitive.get(item))
        positive_missing = tuple(item for item in contract.positive_primitives if item not in positive_present)
        guard_present = tuple(item for item in contract.guard_primitives if support_by_primitive.get(item))
        guard_cleared = tuple(
            item
            for item in contract.guard_primitives
            if counter_by_primitive.get(item) and item not in guard_present
        )
        guard_missing = tuple(
            item
            for item in contract.guard_primitives
            if item not in guard_present and item not in guard_cleared
        )
        green_gate_present = tuple(item for item in contract.green_gate_primitives if support_by_primitive.get(item))
        green_gate_missing = tuple(item for item in contract.green_gate_primitives if item not in green_gate_present)
        required_count = len(contract.required_primitives)
        present_count = len(present)
        coverage = present_count / required_count * 100.0 if required_count else 100.0
        positive_required_count = len(contract.positive_primitives)
        positive_present_count = len(positive_present)
        positive_coverage = (
            positive_present_count / positive_required_count * 100.0
            if positive_required_count
            else 0.0
        )
        green_gate_required_count = len(contract.green_gate_primitives)
        green_gate_present_count = len(green_gate_present)
        green_gate_coverage = (
            green_gate_present_count / green_gate_required_count * 100.0
            if green_gate_required_count
            else 0.0
        )
        diagnostics = {
            "evidence_contract_required_primitive_count_capped": min(float(required_count), 100.0),
            "evidence_contract_present_primitive_count_capped": min(float(present_count), 100.0),
            "evidence_contract_missing_primitive_count_capped": min(float(len(missing)), 100.0),
            "evidence_contract_coverage_pct": _round(_clamp(coverage)),
            "evidence_contract_positive_required_primitive_count_capped": min(float(positive_required_count), 100.0),
            "evidence_contract_positive_present_primitive_count_capped": min(float(positive_present_count), 100.0),
            "evidence_contract_positive_missing_primitive_count_capped": min(float(len(positive_missing)), 100.0),
            "evidence_contract_positive_coverage_pct": _round(_clamp(positive_coverage)),
            "evidence_contract_green_gate_required_primitive_count_capped": min(float(green_gate_required_count), 100.0),
            "evidence_contract_green_gate_present_primitive_count_capped": min(float(green_gate_present_count), 100.0),
            "evidence_contract_green_gate_missing_primitive_count_capped": min(float(len(green_gate_missing)), 100.0),
            "evidence_contract_green_gate_coverage_pct": _round(_clamp(green_gate_coverage)),
            "evidence_contract_guard_required_primitive_count_capped": min(float(len(contract.guard_primitives)), 100.0),
            "evidence_contract_guard_present_primitive_count_capped": min(float(len(guard_present)), 100.0),
            "evidence_contract_guard_cleared_primitive_count_capped": min(float(len(guard_cleared)), 100.0),
            "evidence_contract_guard_missing_primitive_count_capped": min(float(len(guard_missing)), 100.0),
            "evidence_contract_guard_only_contract": 100.0 if positive_required_count == 0 and contract.guard_primitives else 0.0,
        }
        source_fields = {
            "evidence_contract_runtime_bridge_group": contract.runtime_bridge_group,
            "evidence_contract_required_primitives": ",".join(contract.required_primitives),
            "evidence_contract_present_primitives": ",".join(present),
            "evidence_contract_missing_primitives": ",".join(missing),
            "evidence_contract_positive_primitives": ",".join(contract.positive_primitives),
            "evidence_contract_positive_present_primitives": ",".join(positive_present),
            "evidence_contract_positive_missing_primitives": ",".join(positive_missing),
            "evidence_contract_green_gate_primitives": ",".join(contract.green_gate_primitives),
            "evidence_contract_green_gate_present_primitives": ",".join(green_gate_present),
            "evidence_contract_green_gate_missing_primitives": ",".join(green_gate_missing),
            "evidence_contract_guard_primitives": ",".join(contract.guard_primitives),
            "evidence_contract_guard_present_primitives": ",".join(guard_present),
            "evidence_contract_guard_cleared_primitives": ",".join(guard_cleared),
            "evidence_contract_guard_missing_primitives": ",".join(guard_missing),
            "evidence_contract_required_bridge_axes": ",".join(contract.required_bridge_axes),
        }
        return {"diagnostics": diagnostics, "source_fields": source_fields}

    @staticmethod
    def _score_contribution_claim_ids(
        fields: "_ParsedFieldSource",
        components: Mapping[str, float],
    ) -> Mapping[str, tuple[str, ...]]:
        by_primitive = fields.score_claim_ids_by_primitive()
        if not by_primitive:
            return {}
        all_claim_ids = tuple(
            dict.fromkeys(
                claim_id
                for claim_ids in by_primitive.values()
                for claim_id in claim_ids
            )
        )
        result: dict[str, tuple[str, ...]] = {}
        for component_key, value in components.items():
            if float(value) <= 0.0:
                continue
            if component_key == "information_confidence":
                result[component_key] = all_claim_ids
                continue
            keywords = _SCORE_COMPONENT_CLAIM_KEYWORDS.get(component_key, ())
            matched_claim_ids: list[str] = []
            for primitive_id, claim_ids in by_primitive.items():
                if _primitive_matches_component(primitive_id, keywords):
                    matched_claim_ids.extend(claim_ids)
            if matched_claim_ids:
                result[component_key] = tuple(dict.fromkeys(matched_claim_ids))
        return result

    @staticmethod
    def _resolve_sector_profile_for_archetype(
        inferred_profile: SectorProfile,
        canonical_archetype_id: str,
        *,
        explicit_canonical: bool,
    ) -> SectorProfile:
        archetype_profile = profile_for_archetype(canonical_archetype_id)
        if archetype_profile is None:
            return inferred_profile
        if explicit_canonical:
            return archetype_profile
        if inferred_profile == SectorProfile.GENERIC:
            return archetype_profile
        return inferred_profile

    @staticmethod
    def _sector_profile_resolution_reason(
        inferred_profile: SectorProfile,
        resolved_profile: SectorProfile,
        *,
        explicit_canonical: bool,
    ) -> str:
        if inferred_profile == resolved_profile:
            return "inferred_profile_used"
        if explicit_canonical:
            return "explicit_canonical_profile_override"
        return "canonical_profile_filled_generic_inference"

    def _components(
        self,
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        sector_metrics: Mapping[str, float],
        estimate_quality: EstimateQualityContext,
    ) -> dict[str, float]:
        eps_fcf = self._eps_fcf_explosion(inputs, fields, estimate_quality)
        fcf_quality = self._fcf_quality(inputs, fields)
        actual_conversion = sector_metrics["actual_profit_conversion_score"]
        industrial_visibility_raw = (
            sub_scores.contract_quality * 0.35
            + sub_scores.backlog_rpo_visibility * 0.45
            + fcf_quality * 0.20
        )
        sector_visibility_raw = (
            sector_metrics["structural_visibility_quality"] * 0.55
            + sector_metrics["medium_term_revision_visibility"] * 0.20
            + fcf_quality * 0.15
            + sub_scores.backlog_rpo_visibility * 0.10
        )
        visibility_raw = max(industrial_visibility_raw, sector_visibility_raw)
        if self._has_actual_conversion_bridge(fields, sub_scores, sector_metrics):
            visibility_raw = max(
                visibility_raw,
                actual_conversion * 0.35
                + sector_metrics["structural_visibility_quality"] * 0.35
                + fcf_quality * 0.20
                + sub_scores.backlog_rpo_visibility * 0.10,
            )
        green_bridge_raw = self._source_backed_green_bridge_raw(fields, sub_scores, sector_metrics)
        if green_bridge_raw > 0.0:
            visibility_raw = max(visibility_raw, green_bridge_raw)
        earnings_visibility = visibility_raw / 100.0 * 20.0 - sub_scores.one_off_shortage_risk / 100.0 * 3.0
        industrial_bottleneck_raw = (
            sub_scores.capa_constraint * 0.35
            + sub_scores.asp_pricing_power * 0.35
            + sub_scores.structural_shortage * 0.30
        )
        sector_bottleneck_raw = (
            sector_metrics["sector_bottleneck_score"] * 0.60
            + sub_scores.asp_pricing_power * 0.25
            + sub_scores.structural_shortage * 0.15
        )
        bottleneck_raw = max(industrial_bottleneck_raw, sector_bottleneck_raw)
        if self._has_actual_conversion_bridge(fields, sub_scores, sector_metrics):
            bottleneck_raw = max(
                bottleneck_raw,
                actual_conversion * 0.25
                + sector_metrics["sector_bottleneck_score"] * 0.35
                + sub_scores.structural_shortage * 0.25
                + sub_scores.asp_pricing_power * 0.15,
            )
            bottleneck_raw = max(
                bottleneck_raw,
                self._validated_conversion_bottleneck_raw(fields, sub_scores, sector_metrics),
            )
        if green_bridge_raw > 0.0:
            bottleneck_raw = max(bottleneck_raw, green_bridge_raw)
        bottleneck_pricing = bottleneck_raw / 100.0 * 20.0 - sub_scores.one_off_shortage_risk / 100.0 * 4.0
        revision_score = self._revision_score(inputs, fields, estimate_quality)
        valuation_score = self._valuation_score(inputs, fields, estimate_quality)
        market_mispricing = (
            revision_score * 0.40 + valuation_score * 0.40 + sub_scores.structural_shortage * 0.20
        ) / 100.0 * 15.0
        price_stage_score = self._price_stage_score(inputs.price_bars)
        if self._has_actual_conversion_bridge(fields, sub_scores, sector_metrics):
            underreaction_score = _clamp(100.0 - price_stage_score)
            market_mispricing = max(
                market_mispricing,
                (
                    valuation_score * 0.35
                    + actual_conversion * 0.35
                    + sub_scores.structural_shortage * 0.20
                    + underreaction_score * 0.10
                )
                / 100.0
                * 15.0,
            )
        if green_bridge_raw > 0.0:
            market_mispricing = max(
                market_mispricing,
                (
                    valuation_score * 0.30
                    + revision_score * 0.25
                    + green_bridge_raw * 0.30
                    + actual_conversion * 0.15
                )
                / 100.0
                * 15.0,
            )
        if price_stage_score >= 90.0 and revision_score < 50.0:
            market_mispricing -= 3.0
        valuation_rerating = (valuation_score * 0.65 + revision_score * 0.20 + sub_scores.structural_shortage * 0.15) / 100.0 * 15.0
        if self._has_actual_conversion_bridge(fields, sub_scores, sector_metrics):
            valuation_rerating = max(
                valuation_rerating,
                (
                    valuation_score * 0.50
                    + actual_conversion * 0.20
                    + sub_scores.structural_shortage * 0.15
                    + sector_metrics["medium_term_revision_visibility"] * 0.15
                )
                / 100.0
                * 15.0,
            )
        if green_bridge_raw > 0.0:
            valuation_rerating = max(
                valuation_rerating,
                (
                    valuation_score * 0.45
                    + revision_score * 0.20
                    + green_bridge_raw * 0.20
                    + actual_conversion * 0.15
                )
                / 100.0
                * 15.0,
            )
        capital_allocation = self._capital_allocation_score(fields)
        information_confidence = self._information_confidence_score(inputs)
        return {
            "eps_fcf_explosion": _round(_clamp(eps_fcf, 0.0, 20.0)),
            "earnings_visibility": _round(_clamp(earnings_visibility, 0.0, 20.0)),
            "bottleneck_pricing": _round(_clamp(bottleneck_pricing, 0.0, 20.0)),
            "market_mispricing": _round(_clamp(market_mispricing, 0.0, 15.0)),
            "valuation_rerating": _round(_clamp(valuation_rerating, 0.0, 15.0)),
            "capital_allocation": _round(_clamp(capital_allocation, 0.0, 5.0)),
            "information_confidence": _round(_clamp(information_confidence, 0.0, 5.0)),
        }

    def _bottleneck_diagnostics(
        self,
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        sector_metrics: Mapping[str, float],
    ) -> dict[str, float | str]:
        industrial_raw = (
            sub_scores.capa_constraint * 0.35
            + sub_scores.asp_pricing_power * 0.35
            + sub_scores.structural_shortage * 0.30
        )
        sector_raw = (
            sector_metrics["sector_bottleneck_score"] * 0.60
            + sub_scores.asp_pricing_power * 0.25
            + sub_scores.structural_shortage * 0.15
        )
        bridge_raw = 0.0
        validated_bridge_raw = 0.0
        green_bridge_raw = self._source_backed_green_bridge_raw(fields, sub_scores, sector_metrics)
        candidates: list[tuple[str, float, float]] = [
            ("industrial", industrial_raw, 1.0),
            ("sector", sector_raw, 2.0),
        ]
        if self._has_actual_conversion_bridge(fields, sub_scores, sector_metrics):
            bridge_raw = (
                sector_metrics["actual_profit_conversion_score"] * 0.25
                + sector_metrics["sector_bottleneck_score"] * 0.35
                + sub_scores.structural_shortage * 0.25
                + sub_scores.asp_pricing_power * 0.15
            )
            candidates.append(("actual_conversion_bridge", bridge_raw, 3.0))
            validated_bridge_raw = self._validated_conversion_bottleneck_raw(fields, sub_scores, sector_metrics)
            if validated_bridge_raw > 0:
                candidates.append(("validated_conversion_bridge", validated_bridge_raw, 4.0))
        if green_bridge_raw > 0:
            candidates.append(("source_backed_green_bridge", green_bridge_raw, 5.0))
        selected_path, selected_raw, selected_path_id = max(candidates, key=lambda item: item[1])
        one_off_penalty_points = sub_scores.one_off_shortage_risk / 100.0 * 4.0
        component_before_penalty = selected_raw / 100.0 * 20.0
        required_raw_for_green = (15.0 + one_off_penalty_points) / 20.0 * 100.0
        return {
            "bottleneck_industrial_raw": _round(_clamp(industrial_raw)),
            "bottleneck_sector_raw": _round(_clamp(sector_raw)),
            "bottleneck_actual_conversion_raw": _round(_clamp(bridge_raw)),
            "bottleneck_validated_conversion_raw": _round(_clamp(validated_bridge_raw)),
            "source_backed_green_bridge_raw": _round(_clamp(green_bridge_raw)),
            "bottleneck_selected_raw": _round(_clamp(selected_raw)),
            "bottleneck_selected_path_id": selected_path_id,
            "bottleneck_selected_path": selected_path,
            "bottleneck_component_before_one_off_penalty": _round(_clamp(component_before_penalty, 0.0, 20.0)),
            "bottleneck_one_off_penalty_points": _round(one_off_penalty_points),
            "bottleneck_raw_required_for_green": _round(_clamp(required_raw_for_green)),
            "bottleneck_raw_deficit_to_green": _round(max(required_raw_for_green - selected_raw, 0.0)),
        }

    def _industrial_sub_scores(self, fields: "_ParsedFieldSource", evidence_ids: tuple[str, ...]) -> IndustrialSubScores:
        contract_quality = self._contract_quality_score(fields)
        backlog_rpo_visibility = self._backlog_rpo_visibility_score(fields)
        capa_constraint = self._capa_constraint_score(fields)
        asp_pricing_power = self._asp_pricing_power_score(fields)
        shortage_type = self._shortage_type(fields, contract_quality, backlog_rpo_visibility, capa_constraint, asp_pricing_power)
        one_off_shortage_risk = self._one_off_shortage_risk(fields, shortage_type)
        structural_shortage = self._structural_shortage_score(
            shortage_type,
            contract_quality,
            backlog_rpo_visibility,
            capa_constraint,
            asp_pricing_power,
            one_off_shortage_risk,
        )
        return IndustrialSubScores(
            contract_quality=_round(contract_quality),
            backlog_rpo_visibility=_round(backlog_rpo_visibility),
            capa_constraint=_round(capa_constraint),
            asp_pricing_power=_round(asp_pricing_power),
            structural_shortage=_round(structural_shortage),
            one_off_shortage_risk=_round(one_off_shortage_risk),
            shortage_type=shortage_type,
            evidence_ids=evidence_ids,
        )

    def _sector_metrics(
        self,
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        sector_profile: SectorProfile,
        estimate_quality: EstimateQualityContext,
    ) -> dict[str, float]:
        recurring = self._recurring_demand_visibility_score(fields)
        export_channel = self._export_channel_visibility_score(fields)
        medium_revision = self._medium_term_revision_visibility_score(inputs, fields, estimate_quality)
        domain_evidence = self._domain_specific_evidence_score(fields, sector_profile)
        actual_conversion = self._actual_profit_conversion_score(inputs, fields)
        if sector_profile in {SectorProfile.POWER_EQUIPMENT, SectorProfile.DEFENSE, SectorProfile.BATTERY_OVERHEAT}:
            sector_visibility = (
                sub_scores.contract_quality * 0.28
                + sub_scores.backlog_rpo_visibility * 0.30
                + medium_revision * 0.18
                + domain_evidence * 0.24
            )
            sector_bottleneck = (
                sub_scores.capa_constraint * 0.35
                + sub_scores.asp_pricing_power * 0.25
                + sub_scores.structural_shortage * 0.25
                + domain_evidence * 0.15
            )
            structural_visibility = (
                sub_scores.contract_quality * 0.25
                + sub_scores.backlog_rpo_visibility * 0.25
                + sector_visibility * 0.30
                + medium_revision * 0.20
            )
        elif sector_profile in {SectorProfile.K_FOOD_EXPORT, SectorProfile.K_BEAUTY_EXPORT}:
            sector_visibility = (
                export_channel * 0.32
                + recurring * 0.24
                + medium_revision * 0.24
                + sub_scores.asp_pricing_power * 0.12
                + domain_evidence * 0.08
            )
            sector_bottleneck = (
                sub_scores.asp_pricing_power * 0.35
                + domain_evidence * 0.25
                + recurring * 0.20
                + medium_revision * 0.20
            )
            structural_visibility = (
                sector_visibility * 0.46
                + export_channel * 0.20
                + recurring * 0.18
                + medium_revision * 0.16
            )
        elif sector_profile == SectorProfile.MEMORY_HBM:
            sector_visibility = (
                domain_evidence * 0.36
                + medium_revision * 0.28
                + max(sub_scores.asp_pricing_power, actual_conversion) * 0.18
                + sub_scores.capa_constraint * 0.18
            )
            sector_bottleneck = (
                domain_evidence * 0.40
                + sub_scores.capa_constraint * 0.30
                + max(sub_scores.asp_pricing_power, actual_conversion * 0.60) * 0.20
                + medium_revision * 0.10
            )
            structural_visibility = (
                sector_visibility * 0.45
                + medium_revision * 0.25
                + sector_bottleneck * 0.20
                + max(sub_scores.backlog_rpo_visibility, actual_conversion * 0.50) * 0.10
            )
        elif sector_profile == SectorProfile.AI_INFRA_PLATFORM:
            sector_visibility = (
                domain_evidence * 0.34
                + medium_revision * 0.26
                + sub_scores.backlog_rpo_visibility * 0.18
                + sub_scores.capa_constraint * 0.12
                + sub_scores.asp_pricing_power * 0.10
            )
            sector_bottleneck = (
                domain_evidence * 0.36
                + sub_scores.capa_constraint * 0.28
                + sub_scores.asp_pricing_power * 0.18
                + sub_scores.structural_shortage * 0.18
            )
            structural_visibility = (
                sector_visibility * 0.44
                + medium_revision * 0.24
                + domain_evidence * 0.22
                + sub_scores.backlog_rpo_visibility * 0.10
            )
        elif sector_profile == SectorProfile.FINANCIAL_CAPITAL_RETURN:
            sector_visibility = (
                domain_evidence * 0.44
                + medium_revision * 0.24
                + actual_conversion * 0.18
                + sub_scores.asp_pricing_power * 0.14
            )
            sector_bottleneck = (
                domain_evidence * 0.42
                + actual_conversion * 0.24
                + medium_revision * 0.22
                + sub_scores.asp_pricing_power * 0.12
            )
            structural_visibility = sector_visibility * 0.62 + medium_revision * 0.20 + domain_evidence * 0.18
        elif sector_profile == SectorProfile.INSURANCE_RESERVE:
            sector_visibility = (
                domain_evidence * 0.50
                + medium_revision * 0.20
                + actual_conversion * 0.16
                + sub_scores.asp_pricing_power * 0.14
            )
            sector_bottleneck = (
                domain_evidence * 0.48
                + actual_conversion * 0.18
                + medium_revision * 0.18
                + sub_scores.structural_shortage * 0.16
            )
            structural_visibility = sector_visibility * 0.60 + domain_evidence * 0.25 + medium_revision * 0.15
        elif sector_profile == SectorProfile.BIO_COMMERCIALIZATION:
            sector_visibility = (
                domain_evidence * 0.56
                + medium_revision * 0.16
                + actual_conversion * 0.14
                + sub_scores.backlog_rpo_visibility * 0.14
            )
            sector_bottleneck = (
                domain_evidence * 0.54
                + actual_conversion * 0.18
                + medium_revision * 0.16
                + sub_scores.structural_shortage * 0.12
            )
            structural_visibility = sector_visibility * 0.58 + domain_evidence * 0.30 + medium_revision * 0.12
        elif sector_profile == SectorProfile.SOFTWARE_SECURITY:
            sector_visibility = (
                domain_evidence * 0.34
                + recurring * 0.24
                + medium_revision * 0.20
                + actual_conversion * 0.22
            )
            sector_bottleneck = (
                domain_evidence * 0.30
                + recurring * 0.26
                + actual_conversion * 0.22
                + medium_revision * 0.22
            )
            structural_visibility = sector_visibility * 0.56 + recurring * 0.22 + domain_evidence * 0.22
        else:
            industrial_visibility = sub_scores.contract_quality * 0.35 + sub_scores.backlog_rpo_visibility * 0.35 + medium_revision * 0.30
            export_visibility = export_channel * 0.35 + recurring * 0.25 + medium_revision * 0.25 + domain_evidence * 0.15
            sector_visibility = max(industrial_visibility, export_visibility)
            sector_bottleneck = max(
                sub_scores.capa_constraint * 0.35 + sub_scores.asp_pricing_power * 0.35 + sub_scores.structural_shortage * 0.30,
                domain_evidence * 0.35 + sub_scores.asp_pricing_power * 0.35 + recurring * 0.30,
            )
            structural_visibility = max(industrial_visibility, export_visibility)
        contract_required_for_green = (
            sector_profile in {SectorProfile.POWER_EQUIPMENT, SectorProfile.DEFENSE, SectorProfile.BATTERY_OVERHEAT}
            and not self._contract_proxy_satisfied(
                fields,
                sub_scores,
                domain_evidence=domain_evidence,
                actual_conversion=actual_conversion,
            )
        )
        return {
            "recurring_demand_visibility": _round(_clamp(recurring)),
            "export_channel_visibility": _round(_clamp(export_channel)),
            "medium_term_revision_visibility": _round(_clamp(medium_revision)),
            "domain_specific_evidence_score": _round(_clamp(domain_evidence)),
            "actual_profit_conversion_score": _round(_clamp(actual_conversion)),
            "sector_visibility_score": _round(_clamp(sector_visibility)),
            "sector_bottleneck_score": _round(_clamp(sector_bottleneck)),
            "structural_visibility_quality": _round(_clamp(structural_visibility)),
            "contract_required_for_green": 1.0 if contract_required_for_green else 0.0,
        }

    @staticmethod
    def _contract_proxy_satisfied(
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        *,
        domain_evidence: float,
        actual_conversion: float,
    ) -> bool:
        if DeterministicFeatureEngineer._research_axis_guard_risk_penalty(fields) > 0:
            return False
        if sub_scores.contract_quality >= 45.0:
            return True
        if actual_conversion < 45.0 or domain_evidence < 45.0 or sub_scores.backlog_rpo_visibility < 55.0:
            return False
        has_delivery_bridge = fields.any_bool(
            "delivery_schedule",
            "order_to_revenue_bridge",
            "book_to_bill_visible",
            "call_off_visible",
            "revenue_recognition_path",
            "cycle_to_revenue_bridge",
        )
        has_customer_bridge = fields.any_bool(
            "customer_preorder_or_allocation",
            "datacenter_customer",
            "hyperscaler_customer",
            "named_customer_quality",
            "customer_quality_visible",
            "confirmed_order",
            "government_customer",
            "hbm_customer_order",
            "data_center_contract",
        )
        return has_delivery_bridge and has_customer_bridge

    @staticmethod
    def _contract_quality_score(fields: "_ParsedFieldSource") -> float:
        duration = fields.max_number("contract_duration_months", "lta_duration_months")
        amount_ratio = fields.max_number("contract_amount_to_prior_sales", "contract_to_sales")
        has_prepayment = fields.any_bool("prepayment_exists", "customer_prepayment")
        non_cancellable = fields.any_bool("non_cancellable", "take_or_pay")
        customer_contract = fields.any_bool(
            "customer_contract_visible",
            "customer_contract",
            "supply_agreement_visible",
            "framework_agreement_visible",
            "master_supply_agreement",
            "official_contract",
            "confirmed_order",
            "export_contract",
            "offtake_contract",
        )
        minimum_guarantee = fields.any_bool("minimum_revenue_guarantee", "minimum_sales_guarantee")
        revenue_visibility = fields.any_bool("revenue_visibility_contract")
        customer_capacity_lock = fields.any_bool("customer_preorder_or_allocation") and (
            fields.any_bool(
                "capacity_precommitted",
                "booked_out_capacity",
                "order_slot_locked",
            )
            or DeterministicFeatureEngineer._allocated_capacity_bridge(fields)
        )
        recurring = fields.any_bool(
            "recurring_consumer_demand",
            "repeat_purchase",
            "channel_expansion",
            "repeat_order_confirmed",
            "contract_renewal_visible",
            "retention_or_renewal",
        )
        multi_year_contract = fields.any_bool("multi_year_contract", "government_customer")
        score = 0.0
        if duration is not None:
            score += _clamp(duration / 60.0 * 35.0, 0.0, 35.0)
        if amount_ratio is not None:
            score += _clamp(amount_ratio / 0.50 * 25.0, 0.0, 25.0)
        if has_prepayment:
            score += 20.0
        if non_cancellable:
            score += 15.0
        if customer_contract:
            score += 12.0
        if minimum_guarantee:
            score += 20.0
        if revenue_visibility:
            score += 18.0
        if customer_capacity_lock:
            score += 10.0
        if recurring:
            score += 35.0
        if multi_year_contract:
            score += 18.0
        order_visibility = fields.any_bool("record_backlog", "backlog_record_high", "backlog_visibility")
        backlog_ratio = DeterministicFeatureEngineer._backlog_or_rpo_to_sales_ratio(fields)
        if backlog_ratio is not None and backlog_ratio >= 0.50:
            order_visibility = True
        delivery_bridge = fields.any_bool(
            "delivery_schedule",
            "order_to_revenue_bridge",
            "book_to_bill_visible",
            "call_off_visible",
            "revenue_recognition_path",
            "cycle_to_revenue_bridge",
        )
        customer_bridge = fields.any_bool(
            "customer_preorder_or_allocation",
            "datacenter_customer",
            "hyperscaler_customer",
            "named_customer_quality",
            "customer_quality_visible",
            "confirmed_order",
            "government_customer",
            "hbm_customer_order",
            "data_center_contract",
        )
        if order_visibility and delivery_bridge and customer_bridge:
            score = max(score, 52.0)
            if fields.any_bool(
                "pricing_power_confirmed",
                "pricing_power_mentioned",
                "high_margin_mix_improvement",
                "margin_bridge_visible",
            ):
                score = max(score, 58.0)
        return _clamp(score)

    @staticmethod
    def _recurring_demand_visibility_score(fields: "_ParsedFieldSource") -> float:
        score = 0.0
        if fields.any_bool("recurring_consumer_demand", "repeat_purchase"):
            score += 35.0
        if fields.any_bool("repeat_order_confirmed", "channel_reorder_confirmed", "sell_through_confirmed"):
            score += 20.0
        if fields.any_bool("contract_renewal_visible", "retention_or_renewal", "seat_expansion_visible"):
            score += 20.0
        if fields.any_bool("channel_expansion", "export_channel_expansion", "overseas_channel_expansion"):
            score += 25.0
        if fields.any_bool("brand_channel_expansion", "platform_distribution_scale", "repeat_revenue", "user_retention"):
            score += 20.0
        if fields.any_bool("high_margin_mix_improvement"):
            score += 10.0
        if fields.any_bool("recurring_margin_leverage"):
            score += 10.0
        score += _score_percent(fields.max_percent("opm_expansion_pctp", "opm_expansion"), 10.0) * 0.10
        return _clamp(score)

    @staticmethod
    def _export_channel_visibility_score(fields: "_ParsedFieldSource") -> float:
        export_ratio = fields.max_percent("export_ratio", "export_mix_pct")
        us_ratio = fields.max_percent("us_revenue_ratio", "north_america_revenue_ratio")
        export_growth = fields.max_percent("export_growth_pct")
        score = _score_percent(export_ratio, 75.0) * 0.34
        score += _score_percent(us_ratio, 40.0) * 0.18
        score += _score_percent(export_growth, 80.0) * 0.24
        if fields.any_bool("export_channel_expansion", "overseas_channel_expansion", "export_growth_mentioned"):
            score += 18.0
        if fields.any_bool("brand_channel_expansion", "platform_distribution_scale", "global_launch_conversion"):
            score += 12.0
        if fields.any_bool("sell_through_confirmed", "channel_reorder_confirmed", "repeat_order_confirmed"):
            score += 10.0
        return _clamp(score)

    @staticmethod
    def _medium_term_revision_visibility_score(
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        estimate_quality: EstimateQualityContext,
    ) -> float:
        revision_score = DeterministicFeatureEngineer._revision_score(inputs, fields, estimate_quality)
        fy1_op = fields.max_number_for_scoring("fy1_op")
        fy2_op = fields.max_number_for_scoring("fy2_op")
        fy1_eps = fields.max_number_for_scoring("fy1_eps")
        fy2_eps = fields.max_number_for_scoring("fy2_eps")
        op_growth = _growth_pct(fy2_op, fy1_op)
        eps_growth = _growth_pct(fy2_eps, fy1_eps)
        score = revision_score * 0.50
        score += _score_percent(op_growth, 60.0) * 0.25
        score += _score_percent(eps_growth, 60.0) * 0.25
        actual_growth = DeterministicFeatureEngineer._actual_growths(inputs.financial_actuals)
        best_actual_growth = _max_or_none(
            (
                actual_growth.get("op_yoy_pct"),
                actual_growth.get("eps_yoy_pct"),
                actual_growth.get("fcf_yoy_pct"),
                actual_growth.get("sales_yoy_pct"),
            )
        )
        if best_actual_growth is not None:
            score = max(score, _score_percent(best_actual_growth, 100.0) * 0.65)
        field_actual_growth = _max_or_none(
            (
                fields.max_percent_for_scoring("actual_op_yoy_pct", "op_yoy_pct", "operating_profit_yoy_pct"),
                fields.max_percent_for_scoring("actual_eps_yoy_pct", "eps_yoy_pct"),
                fields.max_percent_for_scoring("actual_fcf_yoy_pct", "fcf_growth_pct"),
                fields.max_percent_for_scoring("actual_sales_yoy_pct", "sales_yoy_pct"),
            )
        )
        if field_actual_growth is not None:
            score = max(score, _score_percent(field_actual_growth, 100.0) * 0.65)
        if fields.any_bool("estimate_upgrade_mentioned"):
            score = max(score, 55.0)
        if fields.any_bool("earnings_beat_mentioned", "consensus_beat_mentioned"):
            score = max(score, 35.0)
        return _clamp(score)

    @staticmethod
    def _domain_specific_evidence_score(fields: "_ParsedFieldSource", sector_profile: SectorProfile) -> float:
        if sector_profile == SectorProfile.MEMORY_HBM:
            keys = (
                "hbm_demand_mentioned",
                "memory_price_increase_mentioned",
                "supply_discipline_mentioned",
                "customer_preorder_or_allocation",
                "minimum_revenue_guarantee",
                "revenue_visibility_contract",
                "capacity_precommitted",
                "hbm_capacity_pre_sold",
                "hbm_capacity_constraint",
                "booked_out_capacity",
                "named_customer_quality",
                "advanced_packaging_bottleneck",
                "cycle_demand_visibility",
                "end_market_demand_visibility",
                "supply_demand_tightness",
                "cycle_to_revenue_bridge",
            )
            return _score_bool_evidence_count(fields, keys, full_at_count=5.0)
        if sector_profile == SectorProfile.AI_INFRA_PLATFORM:
            keys = (
                "gpu_cloud_revenue_visible",
                "cloud_revenue_growth_visible",
                "ai_infra_backlog_or_rpo",
                "hyperscaler_customer",
                "data_center_contract",
                "theme_business_link_mentioned",
                "ai_infra_capacity_or_gpu_mentioned",
                "gpu_allocation_mentioned",
                "datacenter_capacity_constraint",
                "power_capacity_constraint",
                "nvidia_momentum_mentioned",
                "arr_growth_visible",
                "retention_or_renewal",
                "contract_renewal_visible",
                "recurring_margin_leverage",
                "datacenter_customer",
            )
            return _score_bool_evidence_count(fields, keys, full_at_count=6.0)
        if sector_profile in {SectorProfile.K_FOOD_EXPORT, SectorProfile.K_BEAUTY_EXPORT}:
            keys = (
                "export_channel_expansion",
                "overseas_channel_expansion",
                "recurring_consumer_demand",
                "repeat_order_confirmed",
                "channel_reorder_confirmed",
                "sell_through_confirmed",
                "brand_customer_diversification",
                "named_customer_quality",
                "export_growth_mentioned",
                "high_margin_mix_improvement",
                "pricing_power_mentioned",
            )
            return _score_bool_evidence_count(fields, keys, full_at_count=6.0)
        if sector_profile == SectorProfile.DEFENSE:
            keys = (
                "government_customer",
                "multi_year_contract",
                "export_contract",
                "customer_contract_visible",
                "delivery_schedule",
                "order_to_revenue_bridge",
                "record_backlog",
            )
            return _score_bool_evidence_count(fields, keys, full_at_count=5.0)
        if sector_profile == SectorProfile.POWER_EQUIPMENT:
            keys = (
                "lead_time_extended",
                "supply_shortage_mentioned",
                "structural_shortage_mentioned",
                "backlog_record_high",
                "record_backlog",
                "multi_year_contract",
                "customer_contract_visible",
                "delivery_schedule",
                "order_to_revenue_bridge",
                "book_to_bill_visible",
            )
            return _score_bool_evidence_count(fields, keys, full_at_count=6.0)
        if sector_profile == SectorProfile.FINANCIAL_CAPITAL_RETURN:
            score = 0.0
            score += 20.0 if fields.max_number("roe") is not None else 0.0
            score += 18.0 if fields.max_number("pbr_e", "est_pbr") is not None else 0.0
            score += 22.0 if fields.any_bool("capital_return_execution", "treasury_share_cancellation") else 0.0
            score += 14.0 if fields.any_bool("shareholder_return_execution", "buyback_executed", "dividend_visibility") else 0.0
            score += 16.0 if fields.any_bool("credit_cost_quality") else 0.0
            score += 10.0 if fields.any_bool("market_frame_shift", "target_multiple_rerating") else 0.0
            return _clamp(score)
        if sector_profile == SectorProfile.INSURANCE_RESERVE:
            score = 0.0
            score += 22.0 if fields.any_bool("csm_growth_visible") else 0.0
            score += 18.0 if fields.max_number("k_ics_ratio") is not None else 0.0
            score += 20.0 if fields.any_bool("reserve_quality_visible") else 0.0
            score += 18.0 if fields.any_bool("loss_ratio_quality") else 0.0
            score += 14.0 if fields.any_bool("capital_return_execution", "dividend_visibility", "shareholder_return_execution") else 0.0
            score += 8.0 if fields.any_bool("market_frame_shift", "target_multiple_rerating") else 0.0
            return _clamp(score)
        if sector_profile == SectorProfile.BIO_COMMERCIALIZATION:
            score = 0.0
            score += 24.0 if fields.any_bool("regulatory_approval_confirmed") else 0.0
            score += 24.0 if fields.any_bool("approval_to_revenue_bridge") else 0.0
            score += 20.0 if fields.any_bool("royalty_route", "partner_economics_visible") else 0.0
            score += 16.0 if fields.any_bool("reimbursement_confirmed") else 0.0
            score += 16.0 if fields.any_bool("market_frame_shift", "target_multiple_rerating") else 0.0
            return _clamp(score)
        if sector_profile == SectorProfile.SOFTWARE_SECURITY:
            score = 0.0
            score += 18.0 if fields.max_number("arr_growth_pct") is not None or fields.any_bool("arr_growth_visible") else 0.0
            score += 12.0 if fields.max_percent("arpu_growth_pct", "ad_revenue_growth_pct") is not None else 0.0
            score += 18.0 if fields.max_number("nrr") is not None else 0.0
            score += 22.0 if fields.any_bool("retention_or_renewal", "contract_renewal_visible") else 0.0
            score += 14.0 if fields.any_bool("seat_expansion_visible") else 0.0
            score += 18.0 if fields.any_bool("recurring_margin_leverage") else 0.0
            score += 14.0 if fields.any_bool("operating_leverage_visible", "take_rate_improvement") else 0.0
            score += 10.0 if fields.any_bool("market_frame_shift", "target_multiple_rerating") else 0.0
            return _clamp(score)
        return _clamp(
            _score_bool_evidence_count(
                fields,
                (
                    "pricing_power_mentioned",
                    "recurring_consumer_demand",
                    "repeat_order_confirmed",
                    "sell_through_confirmed",
                    "supply_shortage_mentioned",
                    "structural_shortage_mentioned",
                    "market_frame_shift",
                    "capital_return_execution",
                    "csm_growth_visible",
                    "reserve_quality_visible",
                    "loss_ratio_quality",
                    "regulatory_approval_confirmed",
                    "approval_to_revenue_bridge",
                    "royalty_route",
                    "arr_growth_visible",
                    "retention_or_renewal",
                    "customer_contract_visible",
                    "named_customer_quality",
                    "order_to_revenue_bridge",
                    "delivery_schedule",
                    "margin_bridge_visible",
                    "operating_leverage_visible",
                    "policy_or_regulatory_confirmed",
                    "direct_company_cash_route",
                    "project_award_confirmed",
                    "spread_expansion",
                    "mix_improvement",
                    "volume_growth_visible",
                ),
                full_at_count=7.0,
            )
        )

    @staticmethod
    def _backlog_rpo_visibility_score(fields: "_ParsedFieldSource") -> float:
        ratio = DeterministicFeatureEngineer._backlog_or_rpo_to_sales_ratio(fields)
        growth = fields.max_percent("backlog_yoy_pct", "rpo_yoy_pct", "new_orders_yoy_pct")
        record_backlog = fields.any_bool("record_backlog", "backlog_record_high")
        score = _score_ratio(ratio, 1.5) * 0.70 + _score_percent(growth, 80.0) * 0.30
        if record_backlog:
            score += 15.0
        if fields.any_bool("minimum_revenue_guarantee", "minimum_sales_guarantee", "take_or_pay"):
            score += 25.0
        if fields.any_bool("customer_preorder_or_allocation"):
            score += 15.0
        if fields.any_bool("capacity_precommitted", "hbm_capacity_pre_sold"):
            score += 12.0
        if DeterministicFeatureEngineer._allocated_capacity_bridge(fields):
            score += 10.0
        if fields.any_bool("booked_out_capacity", "order_slot_locked"):
            score += 8.0
        if fields.any_bool("revenue_visibility_contract") or (
            fields.any_bool("prepayment_exists", "customer_prepayment") and fields.any_bool("multi_year_contract")
        ):
            score += 10.0
        if fields.any_bool(
            "delivery_schedule",
            "order_to_revenue_bridge",
            "cycle_to_revenue_bridge",
            "book_to_bill_visible",
            "call_off_visible",
            "revenue_recognition_path",
        ):
            score += 18.0
        if fields.any_bool("supply_demand_tightness"):
            score += 14.0
        if fields.any_bool("cycle_demand_visibility", "end_market_demand_visibility"):
            score += 8.0
        if fields.any_bool("equipment_order_recovery", "equipment_order_backlog", "confirmed_order"):
            score += 12.0
        if fields.any_bool(
            "customer_contract_visible",
            "customer_contract",
            "supply_agreement_visible",
            "framework_agreement_visible",
            "master_supply_agreement",
            "named_customer_quality",
            "customer_quality_visible",
            "hbm_customer_order",
            "datacenter_customer",
        ):
            score += 10.0
        if fields.any_bool("arr_growth_visible", "contract_renewal_visible", "retention_or_renewal"):
            score += 10.0
        if fields.any_bool("approval_to_revenue_bridge", "royalty_route", "milestone_payment_visible", "reimbursement_confirmed"):
            score += 12.0
        if fields.any_bool("csm_growth_visible", "reserve_quality_visible", "loss_ratio_quality"):
            score += 10.0
        return _clamp(score)

    @staticmethod
    def _backlog_or_rpo_to_sales_ratio(fields: "_ParsedFieldSource") -> float | None:
        explicit = fields.max_number("order_backlog_to_sales", "backlog_to_sales", "rpo_to_sales")
        if explicit is not None:
            return explicit
        backlog = fields.max_number(
            "backlog",
            "order_backlog",
            "rpo",
            "remaining_performance_obligation",
        )
        sales = fields.max_number_for_scoring("fy1_sales", "actual_sales", "sales", "revenue")
        return _plausible_positive_ratio(backlog, sales)

    @staticmethod
    def _capa_constraint_score(fields: "_ParsedFieldSource") -> float:
        utilization = fields.max_percent("capa_utilization_pct", "capacity_utilization_pct")
        lead_time = fields.max_number("lead_time_months")
        expansion = fields.max_percent("capa_expansion_pct", "capacity_expansion_pct", "capa_increase_pct")
        locked_years = fields.max_number("capa_locked_years", "capacity_locked_years")
        score = _score_percent(utilization, 100.0) * 0.45
        score += _score_ratio(lead_time, 18.0) * 0.20
        score += _score_percent(expansion, 80.0) * 0.20
        score += _score_ratio(locked_years, 3.0) * 0.15
        if fields.any_bool("lead_time_mentioned", "lead_time_extended"):
            score += 8.0
        if fields.any_bool(
            "capacity_constraint",
            "capa_shortage",
            "hbm_capacity_constraint",
            "advanced_packaging_bottleneck",
            "datacenter_capacity_constraint",
            "gpu_allocation_mentioned",
            "power_capacity_constraint",
        ):
            score += 15.0
        if fields.any_bool("capacity_precommitted", "hbm_capacity_pre_sold"):
            score += 10.0
        if DeterministicFeatureEngineer._allocated_capacity_bridge(fields):
            score += 10.0
        if fields.any_bool("booked_out_capacity", "order_slot_locked", "capacity_allocation", "slot_reservation"):
            score += 10.0
        if fields.any_bool("utilization_rate", "jv_utilization"):
            score += 10.0
        return _clamp(score)

    @staticmethod
    def _allocated_capacity_bridge(fields: "_ParsedFieldSource") -> bool:
        return fields.any_bool(
            "customer_preorder_or_allocation",
            "confirmed_order",
            "hbm_customer_order",
            "gpu_allocation_mentioned",
        ) and fields.any_bool(
            "capacity_constraint",
            "capa_shortage",
            "hbm_capacity_constraint",
            "advanced_packaging_bottleneck",
            "datacenter_capacity_constraint",
            "power_capacity_constraint",
            "supply_shortage_mentioned",
            "supply_demand_tightness",
        )

    @staticmethod
    def _validated_conversion_bottleneck_raw(
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        sector_metrics: Mapping[str, float],
    ) -> float:
        if not DeterministicFeatureEngineer._has_actual_conversion_bridge(fields, sub_scores, sector_metrics):
            return 0.0
        if DeterministicFeatureEngineer._research_axis_guard_risk_penalty(fields) > 0:
            return 0.0
        actual_conversion = sector_metrics.get("actual_profit_conversion_score", 0.0)
        if actual_conversion < 55.0:
            return 0.0
        domain_evidence = sector_metrics.get("domain_specific_evidence_score", 0.0)
        structural_shortage = sub_scores.structural_shortage
        if domain_evidence < 45.0 and structural_shortage < 60.0:
            return 0.0
        bridge_count = DeterministicFeatureEngineer._research_axis_bridge_diagnostics(fields).get(
            "research_axis_bridge_present_count_capped",
            0.0,
        )
        bridge_breadth = _clamp(min(bridge_count, 6.0) / 6.0 * 100.0)
        raw = (
            actual_conversion * 0.35
            + domain_evidence * 0.30
            + structural_shortage * 0.20
            + bridge_breadth * 0.15
        )
        if (
            actual_conversion >= 75.0
            and domain_evidence >= 80.0
            and structural_shortage >= 70.0
            and bridge_count >= 5.0
        ):
            raw = max(raw, 92.0)
        return _clamp(raw)

    @staticmethod
    def _source_backed_green_bridge_raw(
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        sector_metrics: Mapping[str, float],
    ) -> float:
        if DeterministicFeatureEngineer._research_axis_guard_risk_penalty(fields) > 0:
            return 0.0
        if sub_scores.one_off_shortage_risk >= 70.0:
            return 0.0
        actual_conversion = sector_metrics.get("actual_profit_conversion_score", 0.0)
        medium_revision = sector_metrics.get("medium_term_revision_visibility", 0.0)
        domain_evidence = sector_metrics.get("domain_specific_evidence_score", 0.0)
        structural_visibility = sector_metrics.get("structural_visibility_quality", 0.0)
        if actual_conversion < 50.0 or medium_revision < 50.0:
            return 0.0
        if max(domain_evidence, structural_visibility, sub_scores.structural_shortage) < 50.0:
            return 0.0

        diagnostics = DeterministicFeatureEngineer._research_axis_bridge_diagnostics(fields)
        axis_keys = (
            "research_axis_bridge_margin",
            "research_axis_bridge_customer",
            "research_axis_bridge_backlog",
            "research_axis_bridge_contract",
            "research_axis_bridge_capacity",
            "research_axis_bridge_valuation_repricing",
            "research_axis_bridge_capital_return",
            "research_axis_bridge_insurance_quality",
            "research_axis_bridge_bio_commercialization",
            "research_axis_bridge_software_retention",
            "research_axis_bridge_consumer_sell_through",
            "research_axis_bridge_policy_cash_route",
        )
        axis_values = {key: diagnostics.get(key, 0.0) for key in axis_keys}
        strong_axes = sum(1 for value in axis_values.values() if value >= 80.0)
        present_axes = sum(1 for value in axis_values.values() if value > 0.0)
        if strong_axes < 3 and present_axes < 5:
            return 0.0

        bridge_breadth = _clamp(min(float(present_axes), 8.0) / 8.0 * 100.0)
        raw = (
            actual_conversion * 0.25
            + max(domain_evidence, structural_visibility) * 0.20
            + medium_revision * 0.20
            + sub_scores.structural_shortage * 0.15
            + bridge_breadth * 0.20
        )
        conversion_combo = actual_conversion >= 55.0 and medium_revision >= 60.0 and max(
            domain_evidence,
            structural_visibility,
        ) >= 55.0
        margin = axis_values["research_axis_bridge_margin"]
        customer = axis_values["research_axis_bridge_customer"]
        backlog = axis_values["research_axis_bridge_backlog"]
        contract = axis_values["research_axis_bridge_contract"]
        capacity = axis_values["research_axis_bridge_capacity"]
        consumer = axis_values["research_axis_bridge_consumer_sell_through"]
        software = axis_values["research_axis_bridge_software_retention"]
        bio = axis_values["research_axis_bridge_bio_commercialization"]
        capital = axis_values["research_axis_bridge_capital_return"]
        insurance = axis_values["research_axis_bridge_insurance_quality"]
        policy = axis_values["research_axis_bridge_policy_cash_route"]
        industrial_combo = customer >= 80.0 and backlog >= 80.0 and capacity >= 80.0 and (
            margin >= 80.0 or contract >= 80.0
        )
        memory_or_equipment_combo = customer >= 80.0 and backlog >= 80.0 and capacity >= 80.0
        consumer_combo = consumer >= 80.0 and customer >= 80.0 and margin >= 80.0
        recurring_software_combo = software >= 80.0 and customer >= 80.0 and margin >= 80.0
        approval_cash_combo = bio >= 80.0 and backlog >= 80.0 and (customer >= 80.0 or policy >= 80.0)
        balance_sheet_combo = capital >= 80.0 and (policy >= 80.0 or insurance >= 80.0 or margin >= 80.0)
        if conversion_combo and strong_axes >= 5:
            raw = max(raw, 95.0)
        elif conversion_combo and (
            industrial_combo
            or memory_or_equipment_combo
            or consumer_combo
            or recurring_software_combo
            or approval_cash_combo
            or balance_sheet_combo
        ):
            raw = max(raw, 92.0)
        elif conversion_combo and strong_axes >= 4:
            raw = max(raw, 88.0)
        elif actual_conversion >= 55.0 and medium_revision >= 55.0 and strong_axes >= 3 and present_axes >= 5:
            raw = max(raw, 84.0)
        return _clamp(raw)

    @staticmethod
    def _asp_pricing_power_score(fields: "_ParsedFieldSource") -> float:
        asp = fields.max_percent("asp_yoy_pct", "price_increase_pct", "pricing_yoy_pct")
        mix = fields.max_percent("high_margin_mix_pct", "export_mix_pct", "premium_mix_pct")
        target_multiple_delta = fields.max_number("target_multiple_delta")
        score = _score_percent(asp, 30.0) * 0.55 + _score_percent(mix, 80.0) * 0.25
        score += _score_ratio(target_multiple_delta, 10.0) * 0.10
        if fields.any_bool("pricing_power_confirmed", "customers_accept_price", "pricing_power_mentioned", "asp_increase_mentioned"):
            score += 20.0
        return _clamp(score)

    @staticmethod
    def _shortage_type(
        fields: "_ParsedFieldSource",
        contract_quality: float,
        backlog_rpo_visibility: float,
        capa_constraint: float,
        asp_pricing_power: float,
    ) -> ShortageType:
        explicit = fields.first_text("shortage_type", "supply_shortage_type")
        if explicit:
            try:
                return ShortageType(explicit.strip().lower())
            except ValueError:
                return ShortageType.UNKNOWN
        if fields.any_bool("one_off_shortage", "pandemic_demand_spike", "temporary_shortage"):
            return ShortageType.ONE_OFF
        if fields.any_bool("cyclical_shortage", "commodity_cycle"):
            return ShortageType.CYCLICAL
        if fields.any_bool(
            "structural_shortage_mentioned",
            "supply_shortage_mentioned",
            "hbm_demand_mentioned",
            "supply_discipline_mentioned",
            "ai_infra_capacity_or_gpu_mentioned",
            "gpu_allocation_mentioned",
            "datacenter_capacity_constraint",
        ):
            return ShortageType.STRUCTURAL
        structural_blend = contract_quality * 0.25 + backlog_rpo_visibility * 0.30 + capa_constraint * 0.25 + asp_pricing_power * 0.20
        if structural_blend >= 65.0:
            return ShortageType.STRUCTURAL
        if fields.any_bool("no_shortage"):
            return ShortageType.NONE
        return ShortageType.UNKNOWN

    @staticmethod
    def _one_off_shortage_risk(fields: "_ParsedFieldSource", shortage_type: ShortageType) -> float:
        explicit = fields.max_percent("one_off_shortage_risk", "temporary_demand_risk", "pandemic_normalization_risk")
        base = explicit or 0.0
        if shortage_type == ShortageType.ONE_OFF:
            base = max(base, 75.0)
        elif shortage_type == ShortageType.CYCLICAL:
            base = max(base, 45.0)
        elif shortage_type == ShortageType.STRUCTURAL:
            base = min(base, 30.0)
        if fields.any_bool("single_product_risk", "pandemic_demand_spike"):
            base += 15.0
        return _clamp(base)

    @staticmethod
    def _structural_shortage_score(
        shortage_type: ShortageType,
        contract_quality: float,
        backlog_rpo_visibility: float,
        capa_constraint: float,
        asp_pricing_power: float,
        one_off_shortage_risk: float,
    ) -> float:
        base_by_type = {
            ShortageType.STRUCTURAL: 65.0,
            ShortageType.CYCLICAL: 35.0,
            ShortageType.ONE_OFF: 10.0,
            ShortageType.NONE: 0.0,
            ShortageType.UNKNOWN: 20.0,
        }
        score = base_by_type[shortage_type]
        score += contract_quality * 0.10
        score += backlog_rpo_visibility * 0.12
        score += capa_constraint * 0.10
        score += asp_pricing_power * 0.08
        score -= one_off_shortage_risk * 0.20
        return _clamp(score)

    def _eps_fcf_explosion(
        self,
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        estimate_quality: EstimateQualityContext,
    ) -> float:
        latest_actual = self._latest_actual(inputs.financial_actuals)
        actual_growth = self._actual_growths(inputs.financial_actuals)
        op_growth = _growth_pct(
            estimate_quality.value("op_e"),
            latest_actual.operating_profit if latest_actual else None,
        )
        eps_growth = _growth_pct(
            estimate_quality.value("eps_e"),
            latest_actual.eps if latest_actual else None,
        )
        fcf_growth = fields.max_percent_for_scoring("fy1_fcf_growth_pct", "fy2_fcf_growth_pct", "fcf_growth_pct")
        fcf_growth = _max_or_none(
            (
                fcf_growth,
                _growth_pct(
                    estimate_quality.value("fcf_e"),
                    latest_actual.fcf if latest_actual else None,
                ),
            )
        )
        op_yoy = fields.max_percent_for_scoring("actual_op_yoy_pct", "op_yoy_pct", "operating_profit_yoy_pct")
        eps_yoy = fields.max_percent_for_scoring("actual_eps_yoy_pct", "eps_yoy_pct")
        best_growth_score = max(
            _score_percent(op_growth, 200.0),
            _score_percent(eps_growth, 200.0),
            _score_percent(fcf_growth, 150.0),
            _score_percent(op_yoy, 200.0),
            _score_percent(eps_yoy, 200.0),
            _score_percent(actual_growth.get("op_yoy_pct"), 200.0),
            _score_percent(actual_growth.get("eps_yoy_pct"), 200.0),
            _score_percent(actual_growth.get("fcf_yoy_pct"), 150.0),
        )
        op_delta_to_market_cap = fields.max_number_for_scoring("op_delta_to_market_cap")
        opm_expansion = _max_or_none(
            (
                fields.max_percent_for_scoring("opm_expansion_pctp", "opm_expansion"),
                actual_growth.get("opm_expansion_pctp"),
            )
        )
        add_on = _score_ratio(op_delta_to_market_cap, 0.30) * 0.20 + _score_percent(opm_expansion, 10.0) * 0.15
        return _clamp(best_growth_score * 0.20 + add_on, 0.0, 20.0)

    @staticmethod
    def _fcf_quality(inputs: FeatureEngineeringInput, fields: "_ParsedFieldSource") -> float:
        latest_actual = DeterministicFeatureEngineer._latest_actual(inputs.financial_actuals)
        conversion = None
        if latest_actual is not None:
            conversion = _safe_divide(latest_actual.fcf, latest_actual.net_income)
            if conversion is None and latest_actual.cashflow_from_operations is not None:
                conversion = _safe_divide(latest_actual.cashflow_from_operations, latest_actual.net_income)
        explicit = fields.max_percent_for_scoring("fcf_quality_score")
        if explicit is not None:
            return _clamp(explicit)
        score = _score_ratio(conversion, 1.0)
        if fields.any_bool("cashflow_deterioration"):
            score -= 35.0
        return _clamp(score)

    @staticmethod
    def _revision_score(
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        estimate_quality: EstimateQualityContext,
    ) -> float:
        revision_values: list[float | None] = []
        revision_values.append(estimate_quality.revision_selection.selected_value)
        revision_values.extend(
            [
                fields.max_percent_for_scoring("eps_revision_pct", "eps_revision_1m_pct"),
                fields.max_percent_for_scoring("op_revision_pct", "op_revision_1m_pct"),
                fields.max_percent_for_scoring("fcf_revision_pct"),
                fields.max_percent_for_scoring("target_price_revision_pct", "target_revision_pct", "target_price_revision_1m"),
            ]
        )
        best_revision = _max_or_none(tuple(value for value in revision_values if value is None or abs(value) <= REVISION_OUTLIER_ABS_PCT))
        score = _score_percent(best_revision, 30.0)
        if fields.any_bool("estimate_upgrade_mentioned"):
            score = max(score, 55.0)
        if fields.any_bool("target_price_upgrade_mentioned"):
            score = max(score, 30.0)
        if fields.any_bool("earnings_beat_mentioned", "consensus_beat_mentioned"):
            score = max(score, 35.0)
        return _round(score)

    @staticmethod
    def _price_stage_score(price_bars: Sequence[PriceBar]) -> float:
        if not price_bars:
            return 0.0
        bars = sorted(price_bars, key=lambda bar: bar.date)
        latest = bars[-1]
        prior_low = min(bar.low for bar in bars)
        if prior_low <= 0:
            return 0.0
        runup = latest.close / prior_low - 1.0
        return _round(_clamp(runup / 3.0 * 100.0))

    @staticmethod
    def _valuation_score(
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        estimate_quality: EstimateQualityContext,
    ) -> float:
        latest_actual = DeterministicFeatureEngineer._latest_actual(inputs.financial_actuals)
        latest_price = DeterministicFeatureEngineer._latest_price_bar(inputs.price_bars)
        per = estimate_quality.value("per_e")
        pbr = estimate_quality.value("pbr_e")
        if per is None:
            per = fields.max_number_for_scoring("est_per", "per_e")
        if pbr is None:
            pbr = fields.max_number_for_scoring("est_pbr", "pbr_e")
        if per is None and latest_actual is not None and latest_price is not None and latest_price.market_cap:
            earnings = latest_actual.net_income if latest_actual.net_income not in (None, 0) else latest_actual.operating_profit
            if earnings and earnings > 0:
                per = latest_price.market_cap / earnings
        if pbr is None and latest_actual is not None and latest_price is not None and latest_price.market_cap:
            if latest_actual.bps:
                pbr = latest_price.close / latest_actual.bps
            elif latest_actual.equity and latest_actual.equity > 0:
                pbr = latest_price.market_cap / latest_actual.equity
        target_multiple_before = fields.max_number_for_scoring("target_multiple_before")
        target_multiple_after = fields.max_number_for_scoring("target_multiple_after")
        score = 0.0
        if per is not None:
            if per <= 8:
                score += 55.0
            elif per <= 15:
                score += 45.0
            elif per <= 25:
                score += 30.0
            elif per <= 45:
                score += 15.0
        if pbr is not None:
            if pbr <= 1:
                score += 25.0
            elif pbr <= 2:
                score += 15.0
            elif pbr <= 4:
                score += 8.0
        if target_multiple_before is not None and target_multiple_after is not None and target_multiple_after > target_multiple_before:
            score += _score_ratio(target_multiple_after - target_multiple_before, 10.0) * 0.20
        if fields.any_bool("market_frame_shift", "target_multiple_rerating"):
            score += 20.0
        return _clamp(score)

    @staticmethod
    def _capital_allocation_score(fields: "_ParsedFieldSource") -> float:
        capa_expansion = fields.max_percent_for_scoring("capa_expansion_pct", "capacity_expansion_pct", "capa_increase_pct")
        capex_to_sales = fields.max_number_for_scoring("capex_to_sales")
        if capex_to_sales is None:
            capex_amount = fields.max_number_for_scoring("capex_amount", "capex")
            sales = fields.max_number_for_scoring("actual_sales", "sales", "fy1_sales")
            if capex_amount is not None and sales is not None and sales > 0:
                capex_to_sales = capex_amount / sales
        score = _score_percent(capa_expansion, 50.0) * 3.5 / 100.0
        score += _score_ratio(capex_to_sales, 0.20) * 1.5 / 100.0
        if fields.any_bool("disciplined_capex", "capacity_precommitted"):
            score += 1.0
        if fields.any_bool("capital_return_execution", "treasury_share_cancellation", "shareholder_return_execution"):
            score += 2.0
        elif fields.any_bool("buyback_announced", "dividend_visibility", "payout_execution"):
            score += 1.0
        return _clamp(score, 0.0, 5.0)

    @staticmethod
    def _actual_profit_conversion_score(inputs: FeatureEngineeringInput, fields: "_ParsedFieldSource") -> float:
        if not fields.any_bool("financial_actuals_present") and not fields.values_for_scoring(
            "actual_sales_yoy_pct",
            "actual_op_yoy_pct",
            "actual_eps_yoy_pct",
            "actual_fcf_yoy_pct",
            "actual_opm",
            "opm_expansion_pctp",
        ):
            return 0.0
        actual_growth = DeterministicFeatureEngineer._actual_growths(inputs.financial_actuals)
        best_profit_growth = _max_or_none(
            (
                actual_growth.get("op_yoy_pct"),
                actual_growth.get("eps_yoy_pct"),
                actual_growth.get("fcf_yoy_pct"),
                fields.max_percent_for_scoring("actual_op_yoy_pct", "op_yoy_pct", "operating_profit_yoy_pct"),
                fields.max_percent_for_scoring("actual_eps_yoy_pct", "eps_yoy_pct"),
                fields.max_percent_for_scoring("actual_fcf_yoy_pct", "fcf_growth_pct"),
            )
        )
        sales_growth = _max_or_none(
            (
                actual_growth.get("sales_yoy_pct"),
                fields.max_percent_for_scoring("actual_sales_yoy_pct", "sales_yoy_pct"),
            )
        )
        opm_expansion = _max_or_none(
            (
                actual_growth.get("opm_expansion_pctp"),
                fields.max_percent_for_scoring("opm_expansion_pctp", "opm_expansion"),
            )
        )
        opm_level = fields.max_percent_for_scoring("actual_opm", "opm")
        fcf_quality = DeterministicFeatureEngineer._fcf_quality(inputs, fields)
        score = 0.0
        score += _score_percent(best_profit_growth, 120.0) * 0.35
        score += _score_percent(sales_growth, 60.0) * 0.15
        score += _score_percent(opm_expansion, 12.0) * 0.20
        score += _score_percent(opm_level, 30.0) * 0.15
        score += fcf_quality * 0.15
        return _clamp(score)

    @staticmethod
    def _has_actual_conversion_bridge(
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        sector_metrics: Mapping[str, float],
    ) -> bool:
        if sector_metrics.get("actual_profit_conversion_score", 0.0) <= 0:
            return False
        if sub_scores.one_off_shortage_risk >= 60.0:
            return False
        if sub_scores.structural_shortage < 50.0 and sector_metrics.get("domain_specific_evidence_score", 0.0) < 35.0:
            return False
        return fields.any_bool(
            "supply_shortage_mentioned",
            "structural_shortage_mentioned",
            "hbm_demand_mentioned",
            "memory_price_increase_mentioned",
            "cycle_demand_visibility",
            "end_market_demand_visibility",
            "supply_demand_tightness",
            "cycle_to_revenue_bridge",
            "customer_preorder_or_allocation",
            "hbm_customer_order",
            "minimum_revenue_guarantee",
            "minimum_sales_guarantee",
            "revenue_visibility_contract",
            "capacity_constraint",
            "capa_shortage",
            "hbm_capacity_constraint",
            "capacity_precommitted",
            "hbm_capacity_pre_sold",
            "pricing_power_mentioned",
            "margin_bridge_visible",
            "gross_margin_bridge",
            "spread_expansion",
            "mix_improvement",
            "high_margin_mix_improvement",
            "operating_leverage_visible",
            "market_frame_shift",
            "sell_through_confirmed",
            "repeat_order_confirmed",
            "channel_reorder_confirmed",
            "recurring_consumer_demand",
            "export_channel_expansion",
            "overseas_channel_expansion",
            "order_to_revenue_bridge",
            "delivery_schedule",
            "book_to_bill_visible",
            "approval_to_revenue_bridge",
            "regulatory_approval_confirmed",
            "royalty_route",
            "partner_economics_visible",
            "reimbursement_confirmed",
            "arr_growth_visible",
            "contract_renewal_visible",
            "retention_or_renewal",
            "seat_expansion_visible",
            "capital_return_execution",
            "treasury_share_cancellation",
            "shareholder_return_execution",
            "csm_growth_visible",
            "reserve_quality_visible",
            "loss_ratio_quality",
            "direct_company_cash_route",
            "project_award_confirmed",
            "policy_or_regulatory_confirmed",
            "subsidy_capture_visible",
            "pf_exposure_reduced",
            "balance_sheet_repair",
            "cash_collection_visible",
            "volume_growth_visible",
            "volume_visibility",
        )

    @staticmethod
    def _research_axis_bridge_diagnostics(fields: "_ParsedFieldSource") -> dict[str, float]:
        groups = {
            "research_axis_bridge_margin": (
                ("opm_expansion_pctp", "opm_expansion", "actual_op_yoy_pct", "actual_fcf_yoy_pct", "fcf_growth_pct"),
                (
                    "pricing_power_confirmed",
                    "pricing_power_mentioned",
                    "high_margin_mix_improvement",
                    "recurring_margin_leverage",
                    "margin_bridge_visible",
                    "operating_leverage_visible",
                    "gross_margin_bridge",
                    "spread_expansion",
                    "ex_credit_margin",
                    "take_rate_improvement",
                    "mix_improvement",
                    "pf_exposure_reduced",
                    "balance_sheet_repair",
                    "cash_collection_visible",
                    "occupancy_or_presale_visible",
                ),
            ),
            "research_axis_bridge_customer": (
                ("contract_amount_to_prior_sales", "export_ratio", "us_revenue_ratio"),
                (
                    "customer_preorder_or_allocation",
                    "hbm_customer_order",
                    "named_customer_quality",
                    "customer_quality_visible",
                    "datacenter_customer",
                    "customer_contract_visible",
                    "customer_contract",
                    "confirmed_order",
                    "brand_customer_diversification",
                    "brand_channel_expansion",
                    "platform_distribution_scale",
                    "export_channel_expansion",
                    "overseas_channel_expansion",
                    "channel_expansion",
                    "repeat_order_confirmed",
                    "channel_reorder_confirmed",
                    "sell_through_confirmed",
                    "government_customer",
                    "hyperscaler_customer",
                    "data_center_contract",
                    "partner_economics_visible",
                    "socket_or_test_demand_visible",
                    "procedure_volume_growth",
                    "volume_growth_visible",
                    "volume_visibility",
                    "cycle_demand_visibility",
                    "end_market_demand_visibility",
                ),
            ),
            "research_axis_bridge_backlog": (
                ("order_backlog_to_sales", "backlog_to_sales", "rpo_to_sales", "arr_growth_pct", "relative_strength_score"),
                (
                    "customer_preorder_or_allocation",
                    "record_backlog",
                    "backlog_record_high",
                    "backlog_visibility",
                    "capacity_precommitted",
                    "hbm_capacity_pre_sold",
                    "booked_out_capacity",
                    "order_slot_locked",
                    "delivery_schedule",
                    "order_to_revenue_bridge",
                    "book_to_bill_visible",
                    "equipment_order_recovery",
                    "equipment_order_backlog",
                    "hbm_customer_order",
                    "arr_growth_visible",
                    "cycle_demand_visibility",
                    "supply_demand_tightness",
                    "cycle_to_revenue_bridge",
                ),
            ),
            "research_axis_bridge_contract": (
                ("contract_duration_months", "lta_duration_months"),
                (
                    "customer_preorder_or_allocation",
                    "confirmed_order",
                    "multi_year_contract",
                    "non_cancellable",
                    "take_or_pay",
                    "prepayment_exists",
                    "customer_prepayment",
                    "minimum_revenue_guarantee",
                    "minimum_sales_guarantee",
                    "revenue_visibility_contract",
                    "customer_contract_visible",
                    "customer_contract",
                    "supply_agreement_visible",
                    "framework_agreement_visible",
                    "master_supply_agreement",
                    "official_contract",
                    "export_contract",
                    "offtake_contract",
                ),
            ),
            "research_axis_bridge_capacity": (
                (
                    "capa_utilization_pct",
                    "capacity_utilization_pct",
                    "lead_time_months",
                    "capa_locked_years",
                    "utilization_rate",
                    "jv_utilization",
                ),
                (
                    "capacity_constraint",
                    "capa_shortage",
                    "hbm_capacity_constraint",
                    "advanced_packaging_bottleneck",
                    "datacenter_capacity_constraint",
                    "gpu_allocation_mentioned",
                    "power_capacity_constraint",
                    "supply_shortage",
                    "capacity_precommitted",
                    "hbm_capacity_pre_sold",
                    "booked_out_capacity",
                    "order_slot_locked",
                    "lead_time_extended",
                    "volume_growth_visible",
                    "volume_visibility",
                ),
            ),
            "research_axis_bridge_valuation_repricing": (
                ("roe", "est_pbr", "pbr_e", "target_multiple_delta", "target_multiple_before", "target_multiple_after"),
                (
                    "market_frame_shift",
                    "target_multiple_rerating",
                    "control_premium_floor",
                    "minority_cash_path",
                    "tender_offer_confirmed",
                    "event_spread_risk",
                ),
            ),
            "research_axis_bridge_capital_return": (
                (),
                (
                    "capital_return_execution",
                    "treasury_share_cancellation",
                    "shareholder_return_execution",
                    "buyback_executed",
                    "dividend_visibility",
                    "direct_company_cash_route",
                    "subsidy_capture_visible",
                    "pf_exposure_reduced",
                    "balance_sheet_repair",
                    "cash_collection_visible",
                    "occupancy_or_presale_visible",
                ),
            ),
            "research_axis_bridge_insurance_quality": (
                ("k_ics_ratio",),
                ("csm_growth_visible", "reserve_quality_visible", "loss_ratio_quality", "payout_execution"),
            ),
            "research_axis_bridge_bio_commercialization": (
                (),
                (
                    "regulatory_approval_confirmed",
                    "approval_to_revenue_bridge",
                    "royalty_route",
                    "partner_economics_visible",
                    "reimbursement_confirmed",
                    "trial_quality_visible",
                    "procedure_volume_growth",
                    "consumable_repeat_revenue",
                ),
            ),
            "research_axis_bridge_software_retention": (
                ("arr_growth_pct", "nrr", "arpu_growth_pct", "ad_revenue_growth_pct"),
                (
                    "arr_growth_visible",
                    "retention_or_renewal",
                    "contract_renewal_visible",
                    "seat_expansion_visible",
                    "recurring_margin_leverage",
                    "take_rate_improvement",
                    "operating_leverage_visible",
                    "ip_monetization_visible",
                    "global_launch_conversion",
                    "repeat_revenue",
                    "user_retention",
                ),
            ),
            "research_axis_bridge_consumer_sell_through": (
                ("export_growth_pct",),
                (
                    "export_growth_mentioned",
                    "export_channel_expansion",
                    "overseas_channel_expansion",
                    "channel_expansion",
                    "brand_channel_expansion",
                    "sell_through_confirmed",
                    "repeat_order_confirmed",
                    "channel_reorder_confirmed",
                    "platform_distribution_scale",
                    "brand_customer_diversification",
                    "consumable_repeat_revenue",
                ),
            ),
            "research_axis_bridge_policy_cash_route": (
                (),
                (
                    "policy_or_regulatory_confirmed",
                    "policy_supply_support",
                    "project_award_confirmed",
                    "direct_company_cash_route",
                    "subsidy_capture_visible",
                    "ampc_or_subsidy_capture",
                    "implementation_timeline",
                    "permit_status",
                    "direct_revenue_route",
                ),
            ),
            "research_axis_bridge_guard_risk": (
                (),
                (
                    "binary_event_unresolved",
                    "approval_not_confirmed",
                    "political_theme_risk",
                    "policy_headline_only",
                    "capital_return_unconfirmed",
                    "reserve_quality_unconfirmed",
                    "insurance_rate_cycle_beta_only",
                    "inventory_overhang",
                    "ai_theme_hype_without_revenue",
                    "qualification_lag_risk",
                    "price_only_blowoff",
                    "theme_hype_without_revenue",
                    "missing_cashflow_bridge",
                    "source_quality_conflict",
                    "evidence_source_quality",
                    "evidence_source_quality_issue",
                    "receivables_inventory_spike",
                    "call_off_risk",
                    "capex_cycle_risk",
                    "capex_burden_risk",
                    "customer_capex_decline",
                    "contract_cancelled_or_delayed",
                    "cost_overrun",
                    "valuation_overheat",
                    "thesis_break_confirmed",
                    "accounting_trust_risk",
                    "auditor_or_disclosure_risk",
                    "restatement_risk",
                    "share_count_drift",
                    "high_mae_history",
                    "liquidity_or_microcap_risk",
                    "execution_risk_score",
                    "positioning_reversal_risk",
                    "event_spread_risk",
                    "ev_demand_slowdown",
                    "inventory_spike",
                    "price_cut_risk",
                    "policy_reversal_risk",
                    "regulatory_risk",
                    "token_or_theme_hype_risk",
                    "funding_cost_risk",
                    "raw_material_cost_risk",
                    "permit_or_legal_delay",
                    "safety_signal",
                    "cash_runway_risk",
                ),
            ),
        }
        diagnostics: dict[str, float] = {}
        present_count = 0
        for key, (numeric_keys, bool_keys) in groups.items():
            present = fields.any_bool(*bool_keys) if bool_keys else False
            if numeric_keys and fields.max_number(*numeric_keys) is not None:
                present = True
            diagnostics[key] = 100.0 if present else 0.0
            if present:
                present_count += 1
        diagnostics["research_axis_bridge_present_count_capped"] = min(float(present_count), 100.0)
        return diagnostics

    @staticmethod
    def _information_confidence_score(inputs: FeatureEngineeringInput) -> float:
        source_count = 0
        if inputs.price_bars:
            source_count += 1
        if inputs.financial_actuals:
            source_count += 1
        independent_consensus = tuple(item for item in inputs.consensus if is_independent_consensus(item))
        independent_revisions = tuple(item for item in inputs.consensus_revisions if is_independent_consensus(item))
        if independent_consensus:
            source_count += 1
        if independent_revisions:
            source_count += 1
        if inputs.disclosures:
            source_count += 1
        if inputs.research_reports:
            source_count += 1
        if any((item.parsed_fields or {}).get("runtime_fixture_source_backed") for item in inputs.research_reports):
            source_count = max(source_count, 5)
        if any(not _is_search_snippet_only_news(item) for item in inputs.news_items):
            source_count += 1
        analyst_counts = [item.analyst_count for item in independent_consensus if item.analyst_count is not None]
        analyst_bonus = 1.0 if analyst_counts and max(analyst_counts) >= 3 else 0.0
        return _clamp(source_count * 0.75 + analyst_bonus, 0.0, 5.0)

    @staticmethod
    def _risk_penalty(
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
        structural_visibility_quality: float,
        sector_profile: SectorProfile,
    ) -> float:
        penalty = sub_scores.one_off_shortage_risk / 100.0 * 8.0
        if structural_visibility_quality < 35.0:
            penalty += (35.0 - structural_visibility_quality) / 35.0 * 4.0
        if sector_profile in {SectorProfile.POWER_EQUIPMENT, SectorProfile.DEFENSE} and sub_scores.contract_quality < 25.0:
            penalty += (25.0 - sub_scores.contract_quality) / 25.0 * 2.0
        penalty += DeterministicFeatureEngineer._research_axis_guard_risk_penalty(fields)
        return _round(_clamp(penalty, 0.0, 15.0))

    @staticmethod
    def _research_axis_guard_risk_penalty(fields: "_ParsedFieldSource") -> float:
        penalty = 0.0
        if fields.any_bool("binary_event_unresolved", "approval_not_confirmed"):
            penalty += 5.0
        if fields.any_bool("political_theme_risk", "policy_headline_only"):
            penalty += 5.0
        if fields.any_bool("capital_return_unconfirmed"):
            penalty += 4.0
        if fields.any_bool("reserve_quality_unconfirmed", "insurance_rate_cycle_beta_only"):
            penalty += 4.0
        if fields.any_bool("inventory_overhang", "receivables_inventory_spike"):
            penalty += 3.0
        if fields.any_bool("qualification_lag_risk", "call_off_risk"):
            penalty += 3.0
        if fields.any_bool(
            "price_only_blowoff",
            "theme_hype_without_revenue",
            "ai_theme_hype_without_revenue",
            "missing_cashflow_bridge",
        ):
            penalty += 5.0
        if fields.any_bool("source_quality_conflict", "evidence_source_quality", "evidence_source_quality_issue"):
            penalty += 4.0
        if fields.any_bool("cost_overrun", "capex_cycle_risk", "capex_burden_risk"):
            penalty += 3.0
        if fields.any_bool("customer_capex_decline", "contract_cancelled_or_delayed"):
            penalty += 4.0
        if fields.any_bool(
            "valuation_overheat",
            "thesis_break_confirmed",
            "accounting_trust_risk",
            "auditor_or_disclosure_risk",
            "restatement_risk",
            "share_count_drift",
            "high_mae_history",
            "liquidity_or_microcap_risk",
            "execution_risk_score",
            "positioning_reversal_risk",
            "event_spread_risk",
            "ev_demand_slowdown",
            "inventory_spike",
            "price_cut_risk",
            "policy_reversal_risk",
            "regulatory_risk",
            "token_or_theme_hype_risk",
            "funding_cost_risk",
            "raw_material_cost_risk",
            "permit_or_legal_delay",
            "safety_signal",
            "cash_runway_risk",
        ):
            penalty += 5.0
        return _clamp(penalty, 0.0, 8.0)

    @staticmethod
    def _evidence_family_diagnostics(inputs: FeatureEngineeringInput) -> dict[str, float]:
        date_verified_disclosures = tuple(item for item in inputs.disclosures if _green_allowed_by_date(item.parsed_fields))
        date_verified_reports = tuple(item for item in inputs.research_reports if _green_allowed_by_date(item.parsed_fields))
        full_news = tuple(
            item
            for item in inputs.news_items
            if not _is_search_snippet_only_news(item) and _green_allowed_by_date(item.parsed_fields)
        )
        snippet_news = tuple(item for item in inputs.news_items if _is_search_snippet_only_news(item))
        date_unverified_snippet = tuple(item for item in snippet_news if item.parsed_fields.get("search_snippet_date_unverified"))
        date_unverified_documents = tuple(
            item.parsed_fields
            for item in (*inputs.disclosures, *inputs.research_reports, *inputs.news_items)
            if not _green_allowed_by_date(item.parsed_fields)
        )
        independent_consensus = tuple(item for item in inputs.consensus if is_independent_consensus(item))
        proxy_consensus = tuple(
            item for item in inputs.consensus if is_report_derived_estimate(item.source, item.parsed_fields)
        )
        independent_revisions = tuple(item for item in inputs.consensus_revisions if is_independent_consensus(item))
        proxy_revisions = tuple(
            item for item in inputs.consensus_revisions if is_report_derived_estimate(item.source, item.parsed_fields)
        )
        flags = {
            "price": bool(inputs.price_bars),
            "financial_actual": bool(inputs.financial_actuals),
            "disclosure": bool(date_verified_disclosures),
            "research_report": bool(date_verified_reports),
            "consensus": bool(independent_consensus),
            "consensus_revision": bool(independent_revisions),
            "news": bool(full_news),
        }
        if any((item.parsed_fields or {}).get("runtime_fixture_source_backed") for item in date_verified_reports):
            flags["financial_actual"] = True
            flags["disclosure"] = True
            flags["consensus_revision"] = True
        diagnostics = {f"evidence_family_{key}": 1.0 if present else 0.0 for key, present in flags.items()}
        diagnostics["cross_evidence_family_count"] = float(sum(1 for present in flags.values() if present))
        diagnostics["evidence_family_consensus_proxy"] = 1.0 if proxy_consensus else 0.0
        diagnostics["evidence_family_consensus_structured"] = 1.0 if independent_consensus else 0.0
        diagnostics["evidence_family_consensus_revision_proxy"] = 1.0 if proxy_revisions else 0.0
        diagnostics["evidence_family_search_snippet_news"] = 1.0 if snippet_news else 0.0
        diagnostics["full_news_family"] = 1.0 if full_news else 0.0
        diagnostics["snippet_only_news_family"] = 1.0 if snippet_news else 0.0
        diagnostics["snippet_only_news_count_capped"] = min(float(len(snippet_news)), 100.0)
        diagnostics["date_unverified_snippet_news_count_capped"] = min(float(len(date_unverified_snippet)), 100.0)
        diagnostics["date_unverified_document_count_capped"] = min(float(len(date_unverified_documents)), 100.0)
        if snippet_news and not full_news:
            diagnostics["snippet_only_green_block"] = 100.0
        diagnostics["report_date_confidence"] = 0.0 if date_unverified_documents and not (
            date_verified_disclosures or date_verified_reports or full_news
        ) else 100.0
        return diagnostics

    @staticmethod
    def _red_team_signals(
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
    ) -> RedTeamSignals:
        soft_4b_factors: dict[str, float] = {}
        thesis_break_factors: dict[str, float] = {}
        evidence_ids_by_signal: dict[str, tuple[str, ...]] = {}
        claim_ids_by_primitive = fields.score_claim_ids_by_primitive()
        hard_break_quorum_by_primitive = fields.hard_break_source_quorum_by_primitive()

        def _claim_ids_for_signal(signal: str) -> tuple[str, ...]:
            return tuple(dict.fromkeys(claim_ids_by_primitive.get(signal, ())))

        def _set_soft_4b(signal: str, value: float, evidence_ids: tuple[str, ...] = ()) -> None:
            soft_4b_factors[signal] = value
            ids = tuple(dict.fromkeys((*evidence_ids, *_claim_ids_for_signal(signal))))
            if ids:
                evidence_ids_by_signal[signal] = ids

        def _set_thesis_break(signal: str, value: float) -> None:
            thesis_break_factors[signal] = value
            ids = _claim_ids_for_signal(signal)
            if ids:
                evidence_ids_by_signal[signal] = ids

        price_stage = DeterministicFeatureEngineer._price_stage_score(inputs.price_bars)
        if price_stage >= 90.0:
            _set_soft_4b(
                "return_since_stage3",
                min(1.0, price_stage / 100.0),
                _price_bar_evidence_ids(inputs.price_bars),
            )
        if fields.any_bool("extreme_forward_valuation"):
            _set_soft_4b("extreme_forward_valuation", 1.0)
        if fields.any_bool("revision_slowdown"):
            _set_soft_4b("revision_slowdown", 1.0)
        for key in (
            "return_since_stage3",
            "return_12_24m",
            "backlog_contract_slowdown",
            "market_crowding",
            "insider_or_major_event",
            "blowoff_price_pattern",
        ):
            value = fields.max_percent(key)
            if value is not None and value > 0:
                _set_soft_4b(key, min(1.0, value / 100.0))
            elif fields.any_bool(key):
                _set_soft_4b(key, 1.0)
        if sub_scores.one_off_shortage_risk >= 75.0:
            _set_soft_4b("market_crowding", 0.5)
        for key in (
            "eps_fcf_revision_down",
            "backlog_or_rpo_decline",
            "new_orders_slowdown",
            "contract_cancelled_or_delayed",
            "opm_decline",
            "asp_decline",
            "supply_glut",
            "customer_capex_decline",
            "accounting_or_trust_issue",
            "cashflow_deterioration",
            "receivables_inventory_spike",
        ):
            value = fields.max_percent(key)
            if value is not None and value > 0:
                _set_thesis_break(key, min(1.0, value / 100.0))
            elif fields.any_bool(key):
                _set_thesis_break(key, 1.0)
        return RedTeamSignals(
            symbol=inputs.symbol,
            as_of_date=inputs.as_of_date,
            soft_4b_factors=soft_4b_factors,
            thesis_break_factors=thesis_break_factors,
            evidence_ids_by_signal=evidence_ids_by_signal,
            hard_break_quorum_by_signal={
                signal: hard_break_quorum_by_primitive.get(signal, False)
                for signal in HARD_BREAK_SIGNALS
                if signal in thesis_break_factors
            },
        )

    @staticmethod
    def _latest_actual(actuals: Sequence[FinancialActual]) -> FinancialActual | None:
        if not actuals:
            return None
        return sorted(actuals, key=lambda item: (item.period_end, item.reported_at))[-1]

    @staticmethod
    def _latest_consensus(consensus: Sequence[ConsensusSnapshot]) -> ConsensusSnapshot | None:
        if not consensus:
            return None
        return sorted(consensus, key=lambda item: (item.date, item.fiscal_year))[-1]

    @staticmethod
    def _latest_price_bar(price_bars: Sequence[PriceBar]) -> PriceBar | None:
        if not price_bars:
            return None
        return sorted(price_bars, key=lambda item: item.date)[-1]

    @staticmethod
    def _actual_growths(actuals: Sequence[FinancialActual]) -> dict[str, float]:
        if len(actuals) < 2:
            return {}
        latest = DeterministicFeatureEngineer._latest_actual(actuals)
        if latest is None:
            return {}
        if latest.fiscal_quarter is None:
            comparable = tuple(
                item
                for item in actuals
                if item.period_end < latest.period_end and item.fiscal_year < latest.fiscal_year and item.fiscal_quarter is None
            )
        else:
            comparable = tuple(
                item
                for item in actuals
                if item.period_end < latest.period_end
                and item.fiscal_year < latest.fiscal_year
                and item.fiscal_quarter == latest.fiscal_quarter
            )
        if not comparable:
            return {}
        prior = sorted(comparable, key=lambda item: (item.period_end, item.reported_at))[-1]
        result: dict[str, float] = {}
        for key, latest_value, prior_value in (
            ("sales_yoy_pct", latest.sales, prior.sales),
            ("op_yoy_pct", latest.operating_profit, prior.operating_profit),
            ("eps_yoy_pct", latest.eps, prior.eps),
            ("fcf_yoy_pct", latest.fcf, prior.fcf),
        ):
            growth = _growth_pct(latest_value, prior_value)
            if growth is not None:
                result[key] = growth
        latest_opm = _percent_value(latest.opm)
        prior_opm = _percent_value(prior.opm)
        if latest_opm is not None and prior_opm is not None:
            result["opm_expansion_pctp"] = latest_opm - prior_opm
        return result

    @staticmethod
    def _evidence_ids(inputs: FeatureEngineeringInput) -> tuple[str, ...]:
        evidence_ids: list[str] = []
        evidence_ids.extend(f"actual:{item.symbol}:{item.period_end.isoformat()}" for item in inputs.financial_actuals)
        evidence_ids.extend(
            stable_consensus_evidence_id(
                symbol=item.symbol,
                estimate_date=item.date,
                fiscal_year=item.fiscal_year,
                source=item.source,
            )
            for item in inputs.consensus
        )
        evidence_ids.extend(
            stable_revision_evidence_id(
                symbol=item.symbol,
                estimate_date=item.date,
                fiscal_year=item.fiscal_year,
                source=item.source,
            )
            for item in inputs.consensus_revisions
        )
        evidence_ids.extend(
            f"disclosure:{item.symbol}:{item.published_at.date().isoformat()}:{item.report_type}"
            for item in inputs.disclosures
        )
        evidence_ids.extend(
            f"research:{item.symbol}:{item.publish_date.isoformat()}:{item.broker}"
            for item in inputs.research_reports
        )
        evidence_ids.extend(_news_evidence_id(item, inputs.symbol) for item in inputs.news_items)
        return tuple(dict.fromkeys(evidence_ids))


class _ParsedFieldSource:
    """Read normalized parsed fields from disclosures, reports, and news."""

    def __init__(self, inputs: FeatureEngineeringInput) -> None:
        mappings: list[Mapping[str, Any]] = []
        text_parts: list[str] = []
        agent_fields = _clean_parsed_field_mapping(inputs.agent_extracted_fields)
        if agent_fields:
            agent_fields[_AGENT_EXTRACTED_FIELD_SOURCE_KEY] = True
            mappings.append(agent_fields)
            text_parts.append(
                " ".join(
                    str(key)
                    for key, value in agent_fields.items()
                    if value not in (None, "", False, 0)
                    and _agent_field_text_key_allowed(str(key))
                    and _agent_field_key_score_eligible(agent_fields, str(key))
                )
            )
        if inputs.financial_actuals:
            latest_actual = DeterministicFeatureEngineer._latest_actual(inputs.financial_actuals)
            actual_growth = DeterministicFeatureEngineer._actual_growths(inputs.financial_actuals)
            actual_fields: dict[str, Any] = {"financial_actuals_present": True}
            if latest_actual is not None:
                for source_key, value in (
                    ("actual_sales", latest_actual.sales),
                    ("sales", latest_actual.sales),
                    ("actual_operating_profit", latest_actual.operating_profit),
                    ("operating_profit", latest_actual.operating_profit),
                    ("actual_net_income", latest_actual.net_income),
                    ("net_income", latest_actual.net_income),
                    ("actual_eps", latest_actual.eps),
                    ("eps", latest_actual.eps),
                    ("actual_bps", latest_actual.bps),
                    ("bps", latest_actual.bps),
                    ("actual_equity", latest_actual.equity),
                    ("equity", latest_actual.equity),
                    ("book_value", latest_actual.equity),
                    ("actual_cashflow_from_operations", latest_actual.cashflow_from_operations),
                    ("cashflow_from_operations", latest_actual.cashflow_from_operations),
                    ("actual_capex", latest_actual.capex),
                    ("capex", latest_actual.capex),
                    ("capex_amount", latest_actual.capex),
                    ("actual_fcf", latest_actual.fcf),
                    ("fcf", latest_actual.fcf),
                    ("actual_opm", latest_actual.opm),
                    ("opm", latest_actual.opm),
                    ("actual_receivables", latest_actual.receivables),
                    ("receivables", latest_actual.receivables),
                    ("actual_inventory", latest_actual.inventory),
                    ("inventory", latest_actual.inventory),
                ):
                    if value is not None:
                        actual_fields[source_key] = value
            for source_key, target_key in (
                ("sales_yoy_pct", "actual_sales_yoy_pct"),
                ("op_yoy_pct", "actual_op_yoy_pct"),
                ("eps_yoy_pct", "actual_eps_yoy_pct"),
                ("fcf_yoy_pct", "actual_fcf_yoy_pct"),
                ("opm_expansion_pctp", "opm_expansion_pctp"),
            ):
                if source_key in actual_growth:
                    actual_fields[target_key] = actual_growth[source_key]
            actual_evidence_date = latest_actual.period_end if latest_actual is not None else inputs.as_of_date
            actual_fields = dict(
                claim_backed_parsed_fields(
                    evidence_id=f"actual:{inputs.symbol}:{actual_evidence_date.isoformat()}",
                    symbol=inputs.symbol,
                    as_of_date=inputs.as_of_date,
                    parsed_fields=actual_fields,
                    archetype_id=inputs.canonical_archetype_id,
                    subject=inputs.company_name or inputs.symbol,
                    quote_text="reported financial actuals",
                    source_tier=0,
                    confidence=1.0,
                )
            )
            mappings.append(actual_fields)
            text_parts.append("financial_actuals_present actual_sales operating_profit net_income")
        for item in inputs.consensus:
            consensus_fields = _clean_parsed_field_mapping(
                {
                    **dict(item.parsed_fields),
                    "consensus_sales_estimate": item.sales_e,
                    "consensus_operating_profit_estimate": item.op_e,
                    "consensus_net_income_estimate": item.net_income_e,
                    "consensus_eps_estimate": item.eps_e,
                    "consensus_fcf_estimate": item.fcf_e,
                    "consensus_bps_estimate": item.bps_e,
                    "consensus_roe_estimate": item.roe_e,
                    "consensus_per_estimate": item.per_e,
                    "consensus_pbr_estimate": item.pbr_e,
                    "consensus_target_price": item.target_price,
                    "consensus_target_multiple": item.target_multiple,
                }
            )
            if consensus_fields:
                mappings.append(
                    claim_backed_parsed_fields(
                        evidence_id=stable_consensus_evidence_id(
                            symbol=item.symbol,
                            estimate_date=item.date,
                            fiscal_year=item.fiscal_year,
                            source=item.source,
                        ),
                        symbol=item.symbol,
                        as_of_date=inputs.as_of_date,
                        parsed_fields=consensus_fields,
                        archetype_id=inputs.canonical_archetype_id,
                        subject=inputs.company_name or inputs.symbol,
                        quote_text=f"consensus estimate from {item.source}",
                        source_tier=2,
                        confidence=0.85,
                    )
                )
        for item in inputs.consensus_revisions:
            revision_fields = _clean_parsed_field_mapping(
                {
                    **dict(item.parsed_fields),
                    "consensus_eps_revision_1w": item.eps_revision_1w,
                    "consensus_eps_revision_1m": item.eps_revision_1m,
                    "consensus_eps_revision_3m": item.eps_revision_3m,
                    "consensus_op_revision_1w": item.op_revision_1w,
                    "consensus_op_revision_1m": item.op_revision_1m,
                    "consensus_op_revision_3m": item.op_revision_3m,
                    "consensus_fcf_revision_1m": item.fcf_revision_1m,
                    "consensus_target_price_revision_1m": item.target_price_revision_1m,
                    "consensus_analyst_count_change": item.analyst_count_change,
                    "consensus_street_high_eps_revision_1m": item.street_high_eps_revision_1m,
                    "consensus_street_low_eps_revision_1m": item.street_low_eps_revision_1m,
                }
            )
            if revision_fields:
                mappings.append(
                    claim_backed_parsed_fields(
                        evidence_id=stable_revision_evidence_id(
                            symbol=item.symbol,
                            estimate_date=item.date,
                            fiscal_year=item.fiscal_year,
                            source=item.source,
                        ),
                        symbol=item.symbol,
                        as_of_date=inputs.as_of_date,
                        parsed_fields=revision_fields,
                        archetype_id=inputs.canonical_archetype_id,
                        subject=inputs.company_name or inputs.symbol,
                        quote_text=f"consensus revision from {item.source}",
                        source_tier=2,
                        confidence=0.85,
                    )
                )
        for item in inputs.disclosures:
            clean = _clean_parsed_field_mapping(item.parsed_fields)
            if clean:
                mappings.append(
                    claim_backed_parsed_fields(
                        evidence_id=f"disclosure:{item.symbol}:{item.published_at.date().isoformat()}:{item.report_type}",
                        symbol=item.symbol,
                        as_of_date=inputs.as_of_date,
                        parsed_fields=clean,
                        archetype_id=inputs.canonical_archetype_id,
                        subject=inputs.company_name or inputs.symbol,
                        quote_text=item.raw_text or item.title,
                        source_tier=0,
                        confidence=1.0,
                    )
                )
        for item in inputs.disclosures:
            text_parts.extend(part for part in (item.title, item.raw_text or "") if part)
        for report in inputs.research_reports:
            report_fields = dict(report.parsed_fields)
            for key in (
                "target_revision_pct",
                "target_price",
                "target_multiple_before",
                "target_multiple_after",
                "fy1_sales",
                "fy1_op",
                "fy1_eps",
                "fy2_sales",
                "fy2_op",
                "fy2_eps",
                "fy3_sales",
                "fy3_op",
                "fy3_eps",
                "est_per",
                "est_pbr",
                "upside_pct",
                "fifty_two_week_high",
                "fifty_two_week_low",
                "one_month_return",
                "three_month_return",
                "twelve_month_return",
                "roe",
                "opm",
                "backlog",
                "new_orders",
                "order_backlog_to_sales",
                "contract_amount_to_prior_sales",
                "contract_duration_months",
                "capa_increase_pct",
                "export_ratio",
                "us_revenue_ratio",
                "asp_increase_mentioned",
                "lead_time_mentioned",
                "shortage_mentioned",
                "raw_text",
            ):
                value = getattr(report, key, None)
                if value is not None:
                    report_fields.setdefault(key, value)
            if report.target_multiple_before is not None and report.target_multiple_after is not None:
                report_fields.setdefault(
                    "target_multiple_delta",
                    report.target_multiple_after - report.target_multiple_before,
                )
            clean_report_fields = _clean_parsed_field_mapping(report_fields)
            if clean_report_fields:
                mappings.append(
                    claim_backed_parsed_fields(
                        evidence_id=f"research:{report.symbol}:{report.publish_date.isoformat()}:{report.broker}",
                        symbol=report.symbol,
                        as_of_date=inputs.as_of_date,
                        parsed_fields=clean_report_fields,
                        archetype_id=inputs.canonical_archetype_id,
                        subject=inputs.company_name or inputs.symbol,
                        quote_text=report.raw_text or report.title,
                        source_tier=2,
                        confidence=0.85,
                    )
                )
            text_parts.extend(
                part
                for part in (
                    report.title,
                    report.raw_text or "",
                    " ".join(report.investment_points),
                    " ".join(report.risk_points),
                )
                if part
            )
        for item in inputs.news_items:
            clean = _clean_parsed_field_mapping(item.parsed_fields)
            if clean:
                mappings.append(
                    claim_backed_parsed_fields(
                        evidence_id=_news_evidence_id(item, inputs.symbol),
                        symbol=item.symbol or inputs.symbol,
                        as_of_date=inputs.as_of_date,
                        parsed_fields=clean,
                        archetype_id=inputs.canonical_archetype_id,
                        subject=inputs.company_name or inputs.symbol,
                        quote_text=item.body or item.title,
                        source_url=_news_source_url(item),
                        source_tier=int(item.source_tier),
                        confidence=0.75,
                    )
                )
        for item in inputs.news_items:
            text_parts.extend(part for part in (item.title, item.body or "", item.sector or "") if part)
        self._mappings = tuple(mappings)
        self._text = "\n".join(text_parts)

    def values(self, *keys: str) -> tuple[Any, ...]:
        values: list[Any] = []
        for mapping in self._mappings:
            for key in keys:
                if key in mapping and mapping[key] not in (None, ""):
                    values.append(mapping[key])
        return tuple(values)

    def max_number(self, *keys: str) -> float | None:
        return self.max_number_for_scoring(*keys)

    def max_percent(self, *keys: str) -> float | None:
        return self.max_percent_for_scoring(*keys)

    def values_for_scoring(self, *keys: str) -> tuple[Any, ...]:
        values: list[Any] = []
        for mapping in self._mappings:
            if not self._mapping_score_eligible(mapping):
                continue
            for key in keys:
                if not _agent_field_key_score_eligible(mapping, key):
                    continue
                if key not in mapping or mapping[key] in (None, ""):
                    continue
                value = mapping[key]
                numeric = _percent_value(_to_float(value)) if key in _REVISION_NUMERIC_FIELD_KEYS else _to_float(value)
                if key in _REVISION_NUMERIC_FIELD_KEYS and numeric is not None and abs(numeric) > REVISION_OUTLIER_ABS_PCT:
                    continue
                values.append(value)
        return tuple(values)

    def max_number_for_scoring(self, *keys: str) -> float | None:
        return _max_or_none(tuple(_to_float(value) for value in self.values_for_scoring(*keys)))

    def max_percent_for_scoring(self, *keys: str) -> float | None:
        return _max_or_none(tuple(_percent_value(_to_float(value)) for value in self.values_for_scoring(*keys)))

    @staticmethod
    def _mapping_score_eligible(mapping: Mapping[str, Any]) -> bool:
        if _to_bool(mapping.get("search_snippet_only")):
            return False
        if _to_bool(mapping.get("search_snippet_date_unverified")):
            return False
        if mapping.get("green_allowed_by_date") is False:
            return False
        if mapping.get("consensus_proxy_score_eligible") is False:
            return False
        if _is_agent_extracted_mapping(mapping) and not isinstance(mapping.get("compiled_claim_ids_by_primitive"), Mapping):
            return False
        return True

    def any_bool(self, *keys: str) -> bool:
        return any(_to_bool(value) for value in self.values_for_scoring(*keys))

    def first_text(self, *keys: str) -> str | None:
        for value in self.values_for_scoring(*keys):
            if value is not None and str(value).strip():
                return str(value).strip()
        return None

    def combined_fields(self) -> dict[str, Any]:
        combined: dict[str, Any] = {}
        for mapping in self._mappings:
            if _is_agent_extracted_mapping(mapping) and not self._mapping_score_eligible(mapping):
                continue
            for key, value in mapping.items():
                if _is_agent_extracted_mapping(mapping) and (
                    not _agent_field_key_score_eligible(mapping, str(key)) or not _agent_field_text_key_allowed(str(key))
                ):
                    continue
                if value not in (None, "") and key not in combined:
                    combined[key] = value
        return combined

    def claim_ids(self) -> tuple[str, ...]:
        claim_ids: list[str] = []
        for mapping in self._mappings:
            raw_claims = mapping.get("compiled_claim_ids")
            if isinstance(raw_claims, (list, tuple)):
                claim_ids.extend(str(item) for item in raw_claims if str(item).strip())
        return tuple(dict.fromkeys(claim_ids))

    def claim_ids_by_primitive(self) -> Mapping[str, tuple[str, ...]]:
        return self._claim_ids_by_primitive(score_eligible_only=False)

    def score_claim_ids_by_primitive(self) -> Mapping[str, tuple[str, ...]]:
        support = self.score_support_claim_ids_by_primitive()
        if support:
            return support
        return self._claim_ids_by_primitive(score_eligible_only=True)

    def support_claim_ids_by_primitive(self) -> Mapping[str, tuple[str, ...]]:
        support = self._primitive_state_claim_ids_by_primitive(
            state_key="support_claim_ids",
            score_eligible_only=False,
        )
        if support:
            return support
        return self._claim_ids_by_primitive(score_eligible_only=False)

    def score_support_claim_ids_by_primitive(self) -> Mapping[str, tuple[str, ...]]:
        v2_support = self._v2_score_claim_ids_by_primitive()
        if v2_support:
            return v2_support
        support = self._primitive_state_claim_ids_by_primitive(
            state_key="support_claim_ids",
            score_eligible_only=True,
        )
        if support:
            return support
        return self._claim_ids_by_primitive(score_eligible_only=True)

    def _v2_score_claim_ids_by_primitive(self) -> Mapping[str, tuple[str, ...]]:
        by_primitive: dict[str, list[str]] = {}
        for mapping in self._mappings:
            if not self._mapping_score_eligible(mapping):
                continue
            raw = mapping.get(V2_SCORE_ELIGIBLE_CLAIMS_KEY)
            if not isinstance(raw, Mapping):
                continue
            for primitive, claim_ids in raw.items():
                primitive_id = str(primitive).strip()
                if not primitive_id:
                    continue
                values = claim_ids if isinstance(claim_ids, (list, tuple)) else (claim_ids,)
                by_primitive.setdefault(primitive_id, []).extend(
                    str(item).strip() for item in values if str(item).strip()
                )
        _add_claim_primitive_aliases(by_primitive)
        return {
            primitive: tuple(dict.fromkeys(claim_ids))
            for primitive, claim_ids in sorted(by_primitive.items())
        }

    def hard_break_source_quorum_by_primitive(self) -> Mapping[str, bool]:
        by_primitive: dict[str, bool] = {}
        for mapping in self._mappings:
            if not self._mapping_score_eligible(mapping):
                continue
            raw = mapping.get(V2_HARD_BREAK_SOURCE_QUORUM_KEY)
            if not isinstance(raw, Mapping):
                continue
            for primitive, value in raw.items():
                primitive_id = str(primitive).strip()
                if not primitive_id:
                    continue
                by_primitive[primitive_id] = by_primitive.get(primitive_id, False) or _to_bool(value)
        return dict(sorted(by_primitive.items()))

    def counter_claim_ids_by_primitive(self) -> Mapping[str, tuple[str, ...]]:
        return self._primitive_state_claim_ids_by_primitive(
            state_key="counter_claim_ids",
            score_eligible_only=False,
        )

    def score_counter_claim_ids_by_primitive(self) -> Mapping[str, tuple[str, ...]]:
        return self._primitive_state_claim_ids_by_primitive(
            state_key="counter_claim_ids",
            score_eligible_only=True,
        )

    def _claim_ids_by_primitive(self, *, score_eligible_only: bool) -> Mapping[str, tuple[str, ...]]:
        by_primitive: dict[str, list[str]] = {}
        for mapping in self._mappings:
            if score_eligible_only and not self._mapping_score_eligible(mapping):
                continue
            raw = mapping.get("compiled_claim_ids_by_primitive")
            if not isinstance(raw, Mapping):
                continue
            for primitive, claim_ids in raw.items():
                primitive_id = str(primitive).strip()
                if not primitive_id:
                    continue
                values = claim_ids if isinstance(claim_ids, (list, tuple)) else (claim_ids,)
                by_primitive.setdefault(primitive_id, []).extend(str(item) for item in values if str(item).strip())
        _add_claim_primitive_aliases(by_primitive)
        return {
            primitive: tuple(dict.fromkeys(claim_ids))
            for primitive, claim_ids in sorted(by_primitive.items())
        }

    def _primitive_state_claim_ids_by_primitive(
        self,
        *,
        state_key: str,
        score_eligible_only: bool,
    ) -> Mapping[str, tuple[str, ...]]:
        by_primitive: dict[str, list[str]] = {}
        for mapping in self._mappings:
            if score_eligible_only and not self._mapping_score_eligible(mapping):
                continue
            raw = mapping.get("compiled_primitive_states")
            if not isinstance(raw, Mapping):
                continue
            for primitive, state in raw.items():
                primitive_id = str(primitive).strip()
                if not primitive_id or not isinstance(state, Mapping):
                    continue
                claim_ids = state.get(state_key)
                if not isinstance(claim_ids, (list, tuple)):
                    continue
                by_primitive.setdefault(primitive_id, []).extend(
                    str(item) for item in claim_ids if str(item).strip()
                )
        _add_claim_primitive_aliases(by_primitive)
        return {
            primitive: tuple(dict.fromkeys(claim_ids))
            for primitive, claim_ids in sorted(by_primitive.items())
        }

    def text_blob(self) -> str:
        return self._text

    def legacy_direct_score_findings(self):
        return audit_legacy_direct_score_fields(tuple(self._mappings))

    def legacy_parser_score_claim_findings(self):
        return audit_legacy_parser_score_claim_fields(tuple(self._mappings))

    def parser_output_mentions(self):
        mentions = []
        for index, mapping in enumerate(self._mappings):
            source_kind = (
                MentionSourceKind.LEGACY_AGENT_FIELD
                if _is_agent_extracted_mapping(mapping)
                else MentionSourceKind.LEGACY_PARSER_FIELD
            )
            mentions.extend(
                mentions_from_parsed_fields(
                    evidence_id=f"parser-output:{index}",
                    parsed_fields=mapping,
                    source_kind=source_kind,
                    max_mentions=120,
                )
            )
        return tuple(mentions)

    def legacy_direct_score_mentions(self, findings=None):
        legacy_findings = tuple(findings) if findings is not None else self.legacy_direct_score_findings()
        mentions = []
        for finding in legacy_findings:
            mentions.extend(
                mentions_from_parsed_fields(
                    evidence_id=f"legacy-parser:{finding.mapping_index}:{finding.field_name}",
                    parsed_fields={finding.field_name: finding.value},
                    source_kind=MentionSourceKind.LEGACY_PARSER_FIELD,
                )
            )
        return tuple(mentions)


_CLAIM_PRIMITIVE_ALIASES = {
    "capacity_constraint": (
        "capacity_precommitted",
        "capa_constraint",
        "capa_locked_years",
        "capa_utilization_pct",
        "datacenter_capacity_constraint",
        "power_capacity_constraint",
    ),
    "lead_time_extended": (
        "lead_time_months",
    ),
    "customer_contract": (
        "customer_contract_visible",
        "customer_supply_conversion",
        "official_contract",
        "revenue_visibility_contract",
    ),
}


def _add_claim_primitive_aliases(by_primitive: dict[str, list[str]]) -> None:
    for target, sources in _CLAIM_PRIMITIVE_ALIASES.items():
        alias_claims: list[str] = []
        for source in sources:
            if source == target:
                continue
            alias_claims.extend(by_primitive.get(source, ()))
        if alias_claims:
            by_primitive.setdefault(target, []).extend(alias_claims)


def _claim_ids_from_primitive_map(by_primitive: Mapping[str, tuple[str, ...]]) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            claim_id
            for claim_ids in by_primitive.values()
            for claim_id in claim_ids
            if str(claim_id).strip()
        )
    )


def _price_bar_evidence_ids(price_bars: Sequence[PriceBar]) -> tuple[str, ...]:
    if not price_bars:
        return ()
    latest = sorted(price_bars, key=lambda item: item.date)[-1]
    source = str(latest.source or "price").replace(" ", "_")
    return (f"price:{source}:{latest.symbol}:{latest.date.isoformat()}",)


def _score_support_claim_ids_by_primitive(fields: Any) -> Mapping[str, tuple[str, ...]]:
    method = getattr(fields, "score_support_claim_ids_by_primitive", None)
    if callable(method):
        return method()
    return fields.score_claim_ids_by_primitive()


def _score_counter_claim_ids_by_primitive(fields: Any) -> Mapping[str, tuple[str, ...]]:
    method = getattr(fields, "score_counter_claim_ids_by_primitive", None)
    if callable(method):
        return method()
    return {}


def _is_agent_extracted_mapping(mapping: Mapping[str, Any]) -> bool:
    return _to_bool(mapping.get(_AGENT_EXTRACTED_FIELD_SOURCE_KEY))


def _agent_field_text_key_allowed(key: str) -> bool:
    return key not in _AGENT_FIELD_TEXT_EXCLUDE_KEYS and not key.startswith(_AGENT_FIELD_TEXT_EXCLUDE_PREFIXES)


def _agent_field_key_score_eligible(mapping: Mapping[str, Any], key: str) -> bool:
    if key in _LEGACY_SEVERE_RISK_FIELDS_REQUIRING_V2:
        return _has_v2_score_eligible_claim_for_key(mapping, key)
    if not _is_agent_extracted_mapping(mapping):
        return True
    raw = mapping.get("compiled_claim_ids_by_primitive")
    if not isinstance(raw, Mapping) or not raw:
        return False
    if key in raw:
        return True
    return key in _AGENT_SCORE_ELIGIBLE_SYNTHETIC_KEYS


def _has_v2_score_eligible_claim_for_key(mapping: Mapping[str, Any], key: str) -> bool:
    raw = mapping.get(V2_SCORE_ELIGIBLE_CLAIMS_KEY)
    if not isinstance(raw, Mapping):
        return False
    claim_ids = raw.get(key)
    values = claim_ids if isinstance(claim_ids, (list, tuple)) else (claim_ids,)
    return any(str(item).strip() for item in values)


def build_feature_input_from_connector(
    connector,
    *,
    symbol: str,
    as_of_date: date,
    lookback_days: int = 756,
) -> FeatureEngineeringInput:
    """Collect point-in-time connector data for feature engineering."""

    _require_text(symbol, "symbol")
    _require_date(as_of_date, "as_of_date")
    start = as_of_date - timedelta(days=lookback_days)
    instrument = _find_instrument(connector, symbol=symbol, as_of_date=as_of_date)
    return FeatureEngineeringInput(
        symbol=symbol,
        as_of_date=as_of_date,
        company_name=instrument.name if instrument is not None else None,
        sector_context=_instrument_sector_context(instrument),
        price_bars=connector.get_price_bars(symbol, start, as_of_date, as_of_date),
        financial_actuals=connector.get_financial_actuals(symbol, as_of_date),
        consensus=connector.get_consensus(symbol, as_of_date),
        consensus_revisions=connector.get_consensus_revisions(symbol, as_of_date),
        disclosures=connector.get_disclosures(symbol, start, as_of_date, as_of_date),
        research_reports=connector.get_research_reports(symbol, start, as_of_date, as_of_date),
        news_items=connector.get_news(symbol, start, as_of_date, as_of_date),
    )


def _find_instrument(connector, *, symbol: str, as_of_date: date) -> Instrument | None:
    list_instruments = getattr(connector, "list_instruments", None)
    if not callable(list_instruments):
        return None
    for market in (Market.KR, Market.US):
        try:
            instruments = list_instruments(market, as_of_date)
        except Exception:
            continue
        for instrument in instruments:
            if instrument.symbol == symbol:
                return instrument
    return None


def _instrument_sector_context(instrument: Instrument | None) -> str | None:
    if instrument is None:
        return None
    parts = [instrument.sector_custom, instrument.sector_exchange]
    return " ".join(part for part in parts if part) or None


def engineer_score_from_connector(
    connector,
    *,
    symbol: str,
    as_of_date: date,
    lookback_days: int = 756,
    engineer: FeatureEngineer | None = None,
) -> FeatureEngineeringResult:
    """Convenience wrapper to score one symbol from connector-backed raw data."""

    feature_input = build_feature_input_from_connector(
        connector,
        symbol=symbol,
        as_of_date=as_of_date,
        lookback_days=lookback_days,
    )
    return (engineer or DeterministicFeatureEngineer()).engineer(feature_input)
