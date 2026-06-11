"""Deterministic feature engineering from raw E2R data domains."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any, Mapping, Protocol, Sequence

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
from .red_team import RedTeamSignals
from .scoring import DeterministicScorer, ScoringPayload
from .sector_profiles import SectorProfile, infer_sector_profile, profile_id


EVIDENCE_FAMILIES: tuple[str, ...] = (
    "price",
    "financial_actual",
    "disclosure",
    "research_report",
    "consensus",
    "consensus_revision",
    "news",
)

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


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def _round(value: float) -> float:
    return round(value, 4)


def _to_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


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


def _max_or_none(values: Sequence[float | None]) -> float | None:
    clean = [value for value in values if value is not None]
    return max(clean) if clean else None


def _score_ratio(value: float | None, full_at: float) -> float:
    if value is None or full_at <= 0:
        return 0.0
    return _clamp(value / full_at * 100.0)


def _score_percent(value: float | None, full_at_pct: float) -> float:
    value = _percent_value(value)
    if value is None or full_at_pct <= 0:
        return 0.0
    return _clamp(value / full_at_pct * 100.0)


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
        sector_profile = infer_sector_profile(
            symbol=inputs.symbol,
            company_name=inputs.company_name,
            sector_custom=inputs.sector_context,
            text=field_source.text_blob(),
            parsed_fields=field_source.combined_fields(),
        )
        sub_scores = self._industrial_sub_scores(field_source, evidence_ids)
        sector_metrics = self._sector_metrics(inputs, field_source, sub_scores, sector_profile, estimate_quality)
        components = self._components(inputs, field_source, sub_scores, sector_metrics, estimate_quality)
        risk_penalty = self._risk_penalty(sub_scores, sector_metrics["structural_visibility_quality"], sector_profile)
        revision_score = self._revision_score(inputs, field_source, estimate_quality)
        price_stage_score = self._price_stage_score(inputs.price_bars)
        diagnostic_scores = {
            "revision_score": revision_score,
            "price_stage_score": price_stage_score,
            "sector_profile_id": profile_id(sector_profile),
            **{key: _round(value) for key, value in sector_metrics.items()},
            **estimate_quality.diagnostic_scores,
            **self._evidence_family_diagnostics(inputs),
        }
        if inputs.agent_extracted_fields:
            diagnostic_scores["agent_extracted_field_count_capped"] = min(float(len(inputs.agent_extracted_fields)), 100.0)
        if field_source.any_bool("emerging_theme_active", "theme_transition_detected"):
            diagnostic_scores["emerging_theme_active"] = 100.0
            diagnostic_scores["theme_transition_detected"] = 100.0
        if price_stage_score >= 90.0 and revision_score < 50.0:
            diagnostic_scores["theme_overheat_score"] = _round(min(100.0, price_stage_score))

        red_team_signals = self._red_team_signals(inputs, field_source, sub_scores)
        classification = classify_v12_archetype(
            symbol=inputs.symbol,
            sector_profile=sector_profile,
            parsed_fields=field_source.combined_fields(),
            text=field_source.text_blob(),
            company_name=inputs.company_name,
            sector_context=inputs.sector_context,
            large_sector_id=inputs.large_sector_id,
            canonical_archetype_id=inputs.canonical_archetype_id,
            price_stage_score=price_stage_score,
            revision_score=revision_score,
        )
        diagnostic_scores["archetype_classifier_confidence"] = _round(classification.confidence * 100.0)
        payload = ScoringPayload(
            symbol=inputs.symbol,
            as_of_date=inputs.as_of_date,
            components=components,
            risk_penalty=risk_penalty,
            diagnostic_scores=diagnostic_scores,
            industrial_sub_scores=sub_scores,
            evidence_ids=evidence_ids,
            scoring_version=self.scoring_version,
            large_sector_id=classification.large_sector_id,
            canonical_archetype_id=classification.canonical_archetype_id,
        )
        source_fields: dict[str, float | str] = {
            "shortage_type": sub_scores.shortage_type.value,
            "revision_score": revision_score,
            "price_stage_score": price_stage_score,
            "sector_profile": sector_profile.value,
            "large_sector_id": classification.large_sector_id,
            "canonical_archetype_id": classification.canonical_archetype_id,
            "archetype_classification_reason": classification.reason,
            **estimate_quality.source_fields,
            **{key: _round(value) for key, value in sector_metrics.items()},
        }
        return FeatureEngineeringResult(
            payload=payload,
            industrial_sub_scores=sub_scores,
            shortage_type=sub_scores.shortage_type,
            red_team_signals=red_team_signals,
            source_fields=source_fields,
        )

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
        else:
            industrial_visibility = sub_scores.contract_quality * 0.35 + sub_scores.backlog_rpo_visibility * 0.35 + medium_revision * 0.30
            export_visibility = export_channel * 0.35 + recurring * 0.25 + medium_revision * 0.25 + domain_evidence * 0.15
            sector_visibility = max(industrial_visibility, export_visibility)
            sector_bottleneck = max(
                sub_scores.capa_constraint * 0.35 + sub_scores.asp_pricing_power * 0.35 + sub_scores.structural_shortage * 0.30,
                domain_evidence * 0.35 + sub_scores.asp_pricing_power * 0.35 + recurring * 0.30,
            )
            structural_visibility = max(industrial_visibility, export_visibility)
        return {
            "recurring_demand_visibility": _round(_clamp(recurring)),
            "export_channel_visibility": _round(_clamp(export_channel)),
            "medium_term_revision_visibility": _round(_clamp(medium_revision)),
            "domain_specific_evidence_score": _round(_clamp(domain_evidence)),
            "actual_profit_conversion_score": _round(_clamp(actual_conversion)),
            "sector_visibility_score": _round(_clamp(sector_visibility)),
            "sector_bottleneck_score": _round(_clamp(sector_bottleneck)),
            "structural_visibility_quality": _round(_clamp(structural_visibility)),
            "contract_required_for_green": 1.0
            if sector_profile in {SectorProfile.POWER_EQUIPMENT, SectorProfile.DEFENSE, SectorProfile.BATTERY_OVERHEAT}
            else 0.0,
        }

    @staticmethod
    def _contract_quality_score(fields: "_ParsedFieldSource") -> float:
        duration = fields.max_number("contract_duration_months", "lta_duration_months")
        amount_ratio = fields.max_number("contract_amount_to_prior_sales", "contract_to_sales")
        has_prepayment = fields.any_bool("prepayment_exists", "customer_prepayment")
        non_cancellable = fields.any_bool("non_cancellable", "take_or_pay")
        recurring = fields.any_bool("recurring_consumer_demand", "repeat_purchase", "channel_expansion")
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
        if recurring:
            score += 35.0
        if multi_year_contract:
            score += 18.0
        return _clamp(score)

    @staticmethod
    def _recurring_demand_visibility_score(fields: "_ParsedFieldSource") -> float:
        score = 0.0
        if fields.any_bool("recurring_consumer_demand", "repeat_purchase"):
            score += 35.0
        if fields.any_bool("channel_expansion", "export_channel_expansion", "overseas_channel_expansion"):
            score += 25.0
        if fields.any_bool("brand_channel_expansion", "platform_distribution_scale"):
            score += 20.0
        if fields.any_bool("high_margin_mix_improvement"):
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
        if fields.any_bool("brand_channel_expansion", "platform_distribution_scale"):
            score += 12.0
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
                "hbm_capacity_constraint",
                "advanced_packaging_bottleneck",
            )
            return _clamp(sum(20.0 for key in keys if fields.any_bool(key)))
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
            )
            return _clamp(sum(13.0 for key in keys if fields.any_bool(key)))
        if sector_profile in {SectorProfile.K_FOOD_EXPORT, SectorProfile.K_BEAUTY_EXPORT}:
            keys = (
                "export_channel_expansion",
                "overseas_channel_expansion",
                "recurring_consumer_demand",
                "export_growth_mentioned",
                "high_margin_mix_improvement",
                "pricing_power_mentioned",
            )
            return _clamp(sum(16.0 for key in keys if fields.any_bool(key)))
        if sector_profile == SectorProfile.DEFENSE:
            keys = ("government_customer", "multi_year_contract", "export_contract", "delivery_schedule", "record_backlog")
            return _clamp(sum(20.0 for key in keys if fields.any_bool(key)))
        if sector_profile == SectorProfile.POWER_EQUIPMENT:
            keys = (
                "lead_time_extended",
                "supply_shortage_mentioned",
                "structural_shortage_mentioned",
                "backlog_record_high",
                "record_backlog",
                "multi_year_contract",
            )
            return _clamp(sum(18.0 for key in keys if fields.any_bool(key)))
        return _clamp(
            sum(
                14.0
                for key in (
                    "pricing_power_mentioned",
                    "recurring_consumer_demand",
                    "supply_shortage_mentioned",
                    "structural_shortage_mentioned",
                    "market_frame_shift",
                )
                if fields.any_bool(key)
            )
        )

    @staticmethod
    def _backlog_rpo_visibility_score(fields: "_ParsedFieldSource") -> float:
        ratio = fields.max_number("order_backlog_to_sales", "backlog_to_sales", "rpo_to_sales")
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
        if fields.any_bool("revenue_visibility_contract") or (
            fields.any_bool("prepayment_exists", "customer_prepayment") and fields.any_bool("multi_year_contract")
        ):
            score += 10.0
        return _clamp(score)

    @staticmethod
    def _capa_constraint_score(fields: "_ParsedFieldSource") -> float:
        utilization = fields.max_percent("capa_utilization_pct", "capacity_utilization_pct")
        lead_time = fields.max_number("lead_time_months")
        expansion = fields.max_percent("capa_expansion_pct", "capacity_expansion_pct")
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
        return _clamp(score)

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
        capa_expansion = fields.max_percent_for_scoring("capa_expansion_pct", "capacity_expansion_pct")
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
            "customer_preorder_or_allocation",
            "minimum_revenue_guarantee",
            "minimum_sales_guarantee",
            "revenue_visibility_contract",
            "capacity_constraint",
            "capa_shortage",
            "hbm_capacity_constraint",
            "capacity_precommitted",
            "hbm_capacity_pre_sold",
            "pricing_power_mentioned",
            "market_frame_shift",
        )

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
        if any(not _is_search_snippet_only_news(item) for item in inputs.news_items):
            source_count += 1
        analyst_counts = [item.analyst_count for item in independent_consensus if item.analyst_count is not None]
        analyst_bonus = 1.0 if analyst_counts and max(analyst_counts) >= 3 else 0.0
        return _clamp(source_count * 0.75 + analyst_bonus, 0.0, 5.0)

    @staticmethod
    def _risk_penalty(
        sub_scores: IndustrialSubScores,
        structural_visibility_quality: float,
        sector_profile: SectorProfile,
    ) -> float:
        penalty = sub_scores.one_off_shortage_risk / 100.0 * 8.0
        if structural_visibility_quality < 35.0:
            penalty += (35.0 - structural_visibility_quality) / 35.0 * 4.0
        if sector_profile in {SectorProfile.POWER_EQUIPMENT, SectorProfile.DEFENSE} and sub_scores.contract_quality < 25.0:
            penalty += (25.0 - sub_scores.contract_quality) / 25.0 * 2.0
        return _round(_clamp(penalty, 0.0, 15.0))

    @staticmethod
    def _evidence_family_diagnostics(inputs: FeatureEngineeringInput) -> dict[str, float]:
        full_news = tuple(item for item in inputs.news_items if not _is_search_snippet_only_news(item))
        snippet_news = tuple(item for item in inputs.news_items if _is_search_snippet_only_news(item))
        date_unverified_snippet = tuple(item for item in snippet_news if item.parsed_fields.get("search_snippet_date_unverified"))
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
            "disclosure": bool(inputs.disclosures),
            "research_report": bool(inputs.research_reports),
            "consensus": bool(independent_consensus),
            "consensus_revision": bool(independent_revisions),
            "news": bool(full_news),
        }
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
        if snippet_news and not full_news:
            diagnostics["snippet_only_green_block"] = 100.0
        diagnostics["report_date_confidence"] = 100.0
        return diagnostics

    @staticmethod
    def _red_team_signals(
        inputs: FeatureEngineeringInput,
        fields: "_ParsedFieldSource",
        sub_scores: IndustrialSubScores,
    ) -> RedTeamSignals:
        soft_4b_factors: dict[str, float] = {}
        thesis_break_factors: dict[str, float] = {}
        price_stage = DeterministicFeatureEngineer._price_stage_score(inputs.price_bars)
        if price_stage >= 90.0:
            soft_4b_factors["return_since_stage3"] = min(1.0, price_stage / 100.0)
        if fields.any_bool("extreme_forward_valuation"):
            soft_4b_factors["extreme_forward_valuation"] = 1.0
        if fields.any_bool("revision_slowdown"):
            soft_4b_factors["revision_slowdown"] = 1.0
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
                soft_4b_factors[key] = min(1.0, value / 100.0)
            elif fields.any_bool(key):
                soft_4b_factors[key] = 1.0
        if sub_scores.one_off_shortage_risk >= 75.0:
            soft_4b_factors["market_crowding"] = 0.5
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
                thesis_break_factors[key] = min(1.0, value / 100.0)
            elif fields.any_bool(key):
                thesis_break_factors[key] = 1.0
        return RedTeamSignals(
            symbol=inputs.symbol,
            as_of_date=inputs.as_of_date,
            soft_4b_factors=soft_4b_factors,
            thesis_break_factors=thesis_break_factors,
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
        if inputs.agent_extracted_fields:
            mappings.append(inputs.agent_extracted_fields)
            text_parts.append(
                " ".join(
                    str(key)
                    for key, value in inputs.agent_extracted_fields.items()
                    if value not in (None, "", False, 0)
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
            mappings.append(actual_fields)
            text_parts.append("financial_actuals_present actual_sales operating_profit net_income")
        mappings.extend(item.parsed_fields for item in inputs.disclosures)
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
            mappings.append(report_fields)
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
        mappings.extend(item.parsed_fields for item in inputs.news_items)
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
        return _max_or_none(tuple(_to_float(value) for value in self.values(*keys)))

    def max_percent(self, *keys: str) -> float | None:
        return _max_or_none(tuple(_percent_value(_to_float(value)) for value in self.values(*keys)))

    def values_for_scoring(self, *keys: str) -> tuple[Any, ...]:
        values: list[Any] = []
        for mapping in self._mappings:
            if not self._mapping_score_eligible(mapping):
                continue
            for key in keys:
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
        return True

    def any_bool(self, *keys: str) -> bool:
        return any(_to_bool(value) for value in self.values(*keys))

    def first_text(self, *keys: str) -> str | None:
        for value in self.values(*keys):
            if value is not None and str(value).strip():
                return str(value).strip()
        return None

    def combined_fields(self) -> dict[str, Any]:
        combined: dict[str, Any] = {}
        for mapping in self._mappings:
            for key, value in mapping.items():
                if value not in (None, "") and key not in combined:
                    combined[key] = value
        return combined

    def text_blob(self) -> str:
        return self._text


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
