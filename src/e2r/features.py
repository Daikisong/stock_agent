"""Deterministic feature engineering from raw E2R data domains."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any, Mapping, Protocol, Sequence

from .models import (
    ConsensusRevision,
    ConsensusSnapshot,
    DisclosureEvent,
    FinancialActual,
    IndustrialSubScores,
    NewsItem,
    PriceBar,
    ResearchReport,
    ShortageType,
)
from .red_team import RedTeamSignals
from .scoring import DeterministicScorer, ScoringPayload


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
    price_bars: Sequence[PriceBar] = field(default_factory=tuple)
    financial_actuals: Sequence[FinancialActual] = field(default_factory=tuple)
    consensus: Sequence[ConsensusSnapshot] = field(default_factory=tuple)
    consensus_revisions: Sequence[ConsensusRevision] = field(default_factory=tuple)
    disclosures: Sequence[DisclosureEvent] = field(default_factory=tuple)
    research_reports: Sequence[ResearchReport] = field(default_factory=tuple)
    news_items: Sequence[NewsItem] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.as_of_date, "as_of_date")
        object.__setattr__(self, "price_bars", tuple(self.price_bars))
        object.__setattr__(self, "financial_actuals", tuple(self.financial_actuals))
        object.__setattr__(self, "consensus", tuple(self.consensus))
        object.__setattr__(self, "consensus_revisions", tuple(self.consensus_revisions))
        object.__setattr__(self, "disclosures", tuple(self.disclosures))
        object.__setattr__(self, "research_reports", tuple(self.research_reports))
        object.__setattr__(self, "news_items", tuple(self.news_items))
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
        sub_scores = self._industrial_sub_scores(field_source, evidence_ids)
        components = self._components(inputs, field_source, sub_scores)
        risk_penalty = self._risk_penalty(sub_scores)
        revision_score = self._revision_score(inputs, field_source)
        price_stage_score = self._price_stage_score(inputs.price_bars)
        diagnostic_scores = {
            "revision_score": revision_score,
            "price_stage_score": price_stage_score,
        }
        if price_stage_score >= 90.0 and revision_score < 50.0:
            diagnostic_scores["theme_overheat_score"] = _round(min(100.0, price_stage_score))

        red_team_signals = self._red_team_signals(inputs, field_source, sub_scores)
        payload = ScoringPayload(
            symbol=inputs.symbol,
            as_of_date=inputs.as_of_date,
            components=components,
            risk_penalty=risk_penalty,
            diagnostic_scores=diagnostic_scores,
            industrial_sub_scores=sub_scores,
            evidence_ids=evidence_ids,
            scoring_version=self.scoring_version,
        )
        source_fields: dict[str, float | str] = {
            "shortage_type": sub_scores.shortage_type.value,
            "revision_score": revision_score,
            "price_stage_score": price_stage_score,
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
    ) -> dict[str, float]:
        eps_fcf = self._eps_fcf_explosion(inputs, fields)
        fcf_quality = self._fcf_quality(inputs, fields)
        visibility_raw = (
            sub_scores.contract_quality * 0.35
            + sub_scores.backlog_rpo_visibility * 0.45
            + fcf_quality * 0.20
        )
        earnings_visibility = visibility_raw / 100.0 * 20.0 - sub_scores.one_off_shortage_risk / 100.0 * 3.0
        bottleneck_raw = (
            sub_scores.capa_constraint * 0.35
            + sub_scores.asp_pricing_power * 0.35
            + sub_scores.structural_shortage * 0.30
        )
        bottleneck_pricing = bottleneck_raw / 100.0 * 20.0 - sub_scores.one_off_shortage_risk / 100.0 * 4.0
        revision_score = self._revision_score(inputs, fields)
        valuation_score = self._valuation_score(inputs, fields)
        market_mispricing = (
            revision_score * 0.40 + valuation_score * 0.40 + sub_scores.structural_shortage * 0.20
        ) / 100.0 * 15.0
        price_stage_score = self._price_stage_score(inputs.price_bars)
        if price_stage_score >= 90.0 and revision_score < 50.0:
            market_mispricing -= 3.0
        valuation_rerating = (valuation_score * 0.65 + revision_score * 0.20 + sub_scores.structural_shortage * 0.15) / 100.0 * 15.0
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

    @staticmethod
    def _contract_quality_score(fields: "_ParsedFieldSource") -> float:
        duration = fields.max_number("contract_duration_months", "lta_duration_months")
        amount_ratio = fields.max_number("contract_amount_to_prior_sales", "contract_to_sales")
        has_prepayment = fields.any_bool("prepayment_exists", "customer_prepayment")
        non_cancellable = fields.any_bool("non_cancellable", "take_or_pay")
        recurring = fields.any_bool("recurring_consumer_demand", "repeat_purchase", "channel_expansion")
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
        return _clamp(score)

    @staticmethod
    def _backlog_rpo_visibility_score(fields: "_ParsedFieldSource") -> float:
        ratio = fields.max_number("order_backlog_to_sales", "backlog_to_sales", "rpo_to_sales")
        growth = fields.max_percent("backlog_yoy_pct", "rpo_yoy_pct", "new_orders_yoy_pct")
        record_backlog = fields.any_bool("record_backlog", "backlog_record_high")
        score = _score_ratio(ratio, 1.5) * 0.70 + _score_percent(growth, 80.0) * 0.30
        if record_backlog:
            score += 15.0
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
        if fields.any_bool("capacity_constraint", "capa_shortage"):
            score += 15.0
        return _clamp(score)

    @staticmethod
    def _asp_pricing_power_score(fields: "_ParsedFieldSource") -> float:
        asp = fields.max_percent("asp_yoy_pct", "price_increase_pct", "pricing_yoy_pct")
        mix = fields.max_percent("high_margin_mix_pct", "export_mix_pct", "premium_mix_pct")
        target_multiple_delta = fields.max_number("target_multiple_delta")
        score = _score_percent(asp, 30.0) * 0.55 + _score_percent(mix, 80.0) * 0.25
        score += _score_ratio(target_multiple_delta, 10.0) * 0.10
        if fields.any_bool("pricing_power_confirmed", "customers_accept_price"):
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

    def _eps_fcf_explosion(self, inputs: FeatureEngineeringInput, fields: "_ParsedFieldSource") -> float:
        latest_actual = self._latest_actual(inputs.financial_actuals)
        latest_consensus = self._latest_consensus(inputs.consensus)
        op_growth = _growth_pct(
            latest_consensus.op_e if latest_consensus else None,
            latest_actual.operating_profit if latest_actual else None,
        )
        eps_growth = _growth_pct(
            latest_consensus.eps_e if latest_consensus else None,
            latest_actual.eps if latest_actual else None,
        )
        fcf_growth = fields.max_percent("fy1_fcf_growth_pct", "fy2_fcf_growth_pct", "fcf_growth_pct")
        fcf_growth = _max_or_none(
            (
                fcf_growth,
                _growth_pct(
                    latest_consensus.fcf_e if latest_consensus else None,
                    latest_actual.fcf if latest_actual else None,
                ),
            )
        )
        op_yoy = fields.max_percent("op_yoy_pct", "operating_profit_yoy_pct")
        eps_yoy = fields.max_percent("eps_yoy_pct")
        best_growth_score = max(
            _score_percent(op_growth, 200.0),
            _score_percent(eps_growth, 200.0),
            _score_percent(fcf_growth, 150.0),
            _score_percent(op_yoy, 200.0),
            _score_percent(eps_yoy, 200.0),
        )
        op_delta_to_market_cap = fields.max_number("op_delta_to_market_cap")
        opm_expansion = fields.max_percent("opm_expansion_pctp", "opm_expansion")
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
        explicit = fields.max_percent("fcf_quality_score")
        if explicit is not None:
            return _clamp(explicit)
        score = _score_ratio(conversion, 1.0)
        if fields.any_bool("cashflow_deterioration"):
            score -= 35.0
        return _clamp(score)

    @staticmethod
    def _revision_score(inputs: FeatureEngineeringInput, fields: "_ParsedFieldSource") -> float:
        revision_values: list[float | None] = []
        for revision in inputs.consensus_revisions:
            revision_values.extend(
                [
                    _percent_value(revision.eps_revision_1m),
                    _percent_value(revision.op_revision_1m),
                    _percent_value(revision.fcf_revision_1m),
                    _percent_value(revision.target_price_revision_1m),
                ]
            )
        revision_values.extend(
            [
                fields.max_percent("eps_revision_pct", "eps_revision_1m_pct"),
                fields.max_percent("op_revision_pct", "op_revision_1m_pct"),
                fields.max_percent("fcf_revision_pct", "target_revision_pct"),
            ]
        )
        best_revision = _max_or_none(revision_values)
        return _round(_score_percent(best_revision, 30.0))

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
    def _valuation_score(inputs: FeatureEngineeringInput, fields: "_ParsedFieldSource") -> float:
        latest_consensus = DeterministicFeatureEngineer._latest_consensus(inputs.consensus)
        per = latest_consensus.per_e if latest_consensus else None
        pbr = latest_consensus.pbr_e if latest_consensus else None
        if per is None:
            per = fields.max_number("est_per", "per_e")
        if pbr is None:
            pbr = fields.max_number("est_pbr", "pbr_e")
        target_multiple_before = fields.max_number("target_multiple_before")
        target_multiple_after = fields.max_number("target_multiple_after")
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
        capa_expansion = fields.max_percent("capa_expansion_pct", "capacity_expansion_pct")
        capex_to_sales = fields.max_number("capex_to_sales")
        score = _score_percent(capa_expansion, 50.0) * 3.5 / 100.0
        score += _score_ratio(capex_to_sales, 0.20) * 1.5 / 100.0
        if fields.any_bool("disciplined_capex", "capacity_precommitted"):
            score += 1.0
        return _clamp(score, 0.0, 5.0)

    @staticmethod
    def _information_confidence_score(inputs: FeatureEngineeringInput) -> float:
        source_count = 0
        if inputs.financial_actuals:
            source_count += 1
        if inputs.consensus:
            source_count += 1
        if inputs.consensus_revisions:
            source_count += 1
        if inputs.disclosures:
            source_count += 1
        if inputs.research_reports:
            source_count += 1
        if inputs.news_items:
            source_count += 1
        analyst_counts = [item.analyst_count for item in inputs.consensus if item.analyst_count is not None]
        analyst_bonus = 1.0 if analyst_counts and max(analyst_counts) >= 3 else 0.0
        return _clamp(source_count * 0.75 + analyst_bonus, 0.0, 5.0)

    @staticmethod
    def _risk_penalty(sub_scores: IndustrialSubScores) -> float:
        penalty = sub_scores.one_off_shortage_risk / 100.0 * 8.0
        if sub_scores.contract_quality < 35.0:
            penalty += (35.0 - sub_scores.contract_quality) / 35.0 * 4.0
        return _round(_clamp(penalty, 0.0, 15.0))

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
    def _evidence_ids(inputs: FeatureEngineeringInput) -> tuple[str, ...]:
        evidence_ids: list[str] = []
        evidence_ids.extend(f"actual:{item.symbol}:{item.period_end.isoformat()}" for item in inputs.financial_actuals)
        evidence_ids.extend(f"consensus:{item.symbol}:{item.date.isoformat()}:{item.fiscal_year}" for item in inputs.consensus)
        evidence_ids.extend(f"revision:{item.symbol}:{item.date.isoformat()}:{item.fiscal_year}" for item in inputs.consensus_revisions)
        evidence_ids.extend(
            f"disclosure:{item.symbol}:{item.published_at.date().isoformat()}:{item.report_type}"
            for item in inputs.disclosures
        )
        evidence_ids.extend(
            f"research:{item.symbol}:{item.publish_date.isoformat()}:{item.broker}"
            for item in inputs.research_reports
        )
        evidence_ids.extend(
            f"news:{item.symbol or inputs.symbol}:{item.published_at.date().isoformat()}:{item.source}"
            for item in inputs.news_items
        )
        return tuple(dict.fromkeys(evidence_ids))


class _ParsedFieldSource:
    """Read normalized parsed fields from disclosures, reports, and news."""

    def __init__(self, inputs: FeatureEngineeringInput) -> None:
        mappings: list[Mapping[str, Any]] = []
        mappings.extend(item.parsed_fields for item in inputs.disclosures)
        for report in inputs.research_reports:
            report_fields = dict(report.parsed_fields)
            for key in (
                "target_revision_pct",
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
                "capa_increase_pct",
                "export_ratio",
                "us_revenue_ratio",
                "asp_increase_mentioned",
                "lead_time_mentioned",
                "shortage_mentioned",
            ):
                value = getattr(report, key)
                if value is not None:
                    report_fields.setdefault(key, value)
            if report.target_multiple_before is not None and report.target_multiple_after is not None:
                report_fields.setdefault(
                    "target_multiple_delta",
                    report.target_multiple_after - report.target_multiple_before,
                )
            mappings.append(report_fields)
        mappings.extend(item.parsed_fields for item in inputs.news_items)
        self._mappings = tuple(mappings)

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

    def any_bool(self, *keys: str) -> bool:
        return any(_to_bool(value) for value in self.values(*keys))

    def first_text(self, *keys: str) -> str | None:
        for value in self.values(*keys):
            if value is not None and str(value).strip():
                return str(value).strip()
        return None


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
    return FeatureEngineeringInput(
        symbol=symbol,
        as_of_date=as_of_date,
        price_bars=connector.get_price_bars(symbol, start, as_of_date, as_of_date),
        financial_actuals=connector.get_financial_actuals(symbol, as_of_date),
        consensus=connector.get_consensus(symbol, as_of_date),
        consensus_revisions=connector.get_consensus_revisions(symbol, as_of_date),
        disclosures=connector.get_disclosures(symbol, start, as_of_date, as_of_date),
        research_reports=connector.get_research_reports(symbol, start, as_of_date, as_of_date),
        news_items=connector.get_news(symbol, start, as_of_date, as_of_date),
    )


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
