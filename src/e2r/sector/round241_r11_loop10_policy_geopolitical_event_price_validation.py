"""Round-241 R11 Loop-10 policy/geopolitical/event price-validation pack.

This module turns ``docs/round/round_241.md`` into calibration-only records.
It deliberately does not touch production scoring or candidate generation.

Easy example: WGBI inclusion can improve Korea market structure, but it is not
company Stage 3-Green until actual flows and company EPS/FCF bridges appear.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation, write_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector


ROUND241_SOURCE_ROUND_PATH = "docs/round/round_241.md"
ROUND241_ANALYST_ROUND_ID = "round_169"
ROUND241_LARGE_SECTOR = Round10LargeSector.POLICY_GEOPOLITICAL_EVENT
ROUND241_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round241_r11_loop10_policy_geopolitical_event_price_validation"
ROUND241_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop10_round241.jsonl"
ROUND241_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round241_r11_loop10_policy_geopolitical_event_price_validation_audit.json"
ROUND241_DEFAULT_STAGE3_BIAS = "very_conservative"

ROUND241_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "POLITICAL_INSTITUTIONAL_TRUST_BREAK": E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK.value,
    "MARKET_STRUCTURE_REFORM": E2RArchetype.MARKET_STRUCTURE_REFORM.value,
    "GLOBAL_INDEX_INCLUSION": E2RArchetype.GLOBAL_INDEX_INCLUSION.value,
    "SHORT_SELLING_NORMALIZATION": E2RArchetype.SHORT_SELLING_NORMALIZATION.value,
    "AI_WINDFALL_TAX_POLICY_SHOCK": E2RArchetype.AI_WINDFALL_TAX_POLICY_SHOCK.value,
    "GEOPOLITICAL_ENERGY_SUPPLY_SHOCK": E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK.value,
    "FX_LIQUIDITY_POLICY_RESPONSE": E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE.value,
    "STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO": E2RArchetype.STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO.value,
    "POLICY_CONFIDENCE_EVENT_PREMIUM": E2RArchetype.POLICY_CONFIDENCE_EVENT_PREMIUM.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "FX_OUTFLOW_TRADE_DEAL_OVERLAY": E2RArchetype.FX_OUTFLOW_TRADE_DEAL_OVERLAY.value,
    "MACRO_HARD_4C": E2RArchetype.MACRO_HARD_4C.value,
}

ROUND241_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "policy_escalated_to_law_budget_index_contract_or_capital_inflow",
    "company_revenue_eps_fcf_bridge_exists",
    "actual_capital_inflow_or_funding_cost_effect_confirmed",
    "fx_rate_credit_cost_or_energy_cost_effect_positive",
    "sustained_effect_not_headline_only",
    "political_institutional_regulatory_trust_intact",
    "price_path_after_evidence",
)

ROUND241_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_speech_only",
    "election_pledge_only",
    "tax_or_redistribution_surprise",
    "martial_law_or_institutional_shock",
    "geopolitical_chokepoint_headline_only",
    "index_inclusion_expectation_only",
    "market_reform_without_foreign_flow",
    "fx_policy_without_actual_flow",
    "energy_security_headline_without_cost_stabilization",
    "event_rally_before_earnings_bridge",
)

ROUND241_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "wgbi_msci_expectation_basket_rally",
    "short_selling_normalization_brokerage_rally_before_flow",
    "policy_speech_theme_rally_before_law_or_budget",
    "ai_dividend_tax_shock_rebound_before_clarity",
    "energy_security_headline_rally_before_margin_stabilization",
    "fx_policy_relief_rally_without_krw_stabilization",
    "tariff_relief_rally_ignores_dollar_outflow",
)

ROUND241_HARD_4C_GATES: tuple[str, ...] = (
    "martial_law_or_coup_like_institutional_shock",
    "major_political_legitimacy_crisis",
    "tax_or_windfall_redistribution_shock",
    "geopolitical_energy_chokepoint_closure",
    "kospi_circuit_breaker_or_market_crash",
    "krw_disorderly_depreciation",
    "foreign_capital_flight",
    "index_inclusion_failure",
    "msci_access_disappointment",
    "fx_liquidity_breakdown",
    "policy_reversal",
)

ROUND241_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "market_index_anchor",
    "fx_anchor",
    "capital_flow_anchor",
    "policy_amount_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round241ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round241ShadowWeightRow:
    archetype: E2RArchetype
    funded_policy: int
    capital_inflow: int
    index_inclusion: int
    market_access: int
    institutional_trust: int
    fx_stability: int
    energy_security: int
    policy_to_revenue: int
    event_penalty: int
    macro_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "funded_policy": _signed(self.funded_policy),
            "capital_inflow": _signed(self.capital_inflow),
            "index_inclusion": _signed(self.index_inclusion),
            "market_access": _signed(self.market_access),
            "institutional_trust": _signed(self.institutional_trust),
            "fx_stability": _signed(self.fx_stability),
            "energy_security": _signed(self.energy_security),
            "policy_to_revenue": _signed(self.policy_to_revenue),
            "event_penalty": _signed(self.event_penalty),
            "macro_4c_sensitivity": _signed(self.macro_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round241DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round241CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    stage3_decision: str
    stage4b_status: str
    hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    mfe_1d: float | None
    mae_1d: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool | list[str]]
    score_price_alignment: str
    round_score_price_alignment: str
    rerating_result: str
    round_rerating_result: str
    stage_failure_type: str
    round_stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND241_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND241_SCORE_ADJUSTMENTS: tuple[Round241ScoreAdjustment, ...] = (
    Round241ScoreAdjustment("funded_policy", 5, "raise", "R11은 정책이 실제 법안·예산·집행으로 내려올 때만 강하게 본다."),
    Round241ScoreAdjustment("actual_capital_inflow", 5, "raise", "WGBI/MSCI 같은 구조 변화도 실제 자금유입이 확인되어야 Stage 2 이상 품질이 오른다."),
    Round241ScoreAdjustment("index_inclusion_confirmed", 5, "raise", "확정된 index inclusion은 기대보다 강하지만 회사 Green은 별도 EPS/FCF bridge가 필요하다."),
    Round241ScoreAdjustment("market_access_improvement", 4, "raise", "공매도 정상화와 불공정거래 단속은 외국인 접근성 개선 신호다."),
    Round241ScoreAdjustment("institutional_trust", 5, "raise", "정치·제도 신뢰가 유지되어야 Korea discount 완화 논리가 유지된다."),
    Round241ScoreAdjustment("fx_stability", 5, "raise", "KRW 안정은 자금조달비용과 외국인 flow의 기초 조건이다."),
    Round241ScoreAdjustment("energy_security_resilience", 5, "raise", "에너지 충격 후 비용 안정과 공급망 회복이 확인되어야 한다."),
    Round241ScoreAdjustment("policy_to_company_revenue_bridge", 5, "raise", "정책/거시 이벤트가 회사 매출·마진·EPS/FCF로 내려와야 Green 검토가 가능하다."),
    Round241ScoreAdjustment("regulatory_clarity", 4, "raise", "세금·규제 디테일이 명확해야 policy-confidence risk를 통과한다."),
    Round241ScoreAdjustment("policy_speech_only", -5, "lower", "발언만 있고 법안·예산·계약·flow가 없으면 Stage 3 금지다."),
    Round241ScoreAdjustment("tax_or_redistribution_surprise", -5, "lower", "AI dividend/tax 같은 surprise는 EPS/FCF보다 risk premium을 먼저 깨뜨린다."),
    Round241ScoreAdjustment("political_institutional_shock", -5, "lower", "martial-law shock은 시장 전체 4C-watch다."),
    Round241ScoreAdjustment("geopolitical_energy_shock", -5, "lower", "Hormuz 같은 chokepoint shock은 에너지·환율·수출주 리스크를 동시에 키운다."),
    Round241ScoreAdjustment("capital_outflow_pressure", -4, "lower", "대규모 해외투자·해외주식 순매수는 FX outflow watch다."),
    Round241ScoreAdjustment("fx_policy_without_actual_flow", -4, "lower", "FX 정책만 있고 실제 안정/유입이 없으면 Green 근거가 아니다."),
    Round241ScoreAdjustment("index_inclusion_expectation_only", -3, "lower", "WGBI/MSCI 기대만으로 특정 종목 Green은 금지한다."),
    Round241ScoreAdjustment("market_reform_without_foreign_flow", -3, "lower", "공매도 정상화만 있고 foreign flow가 없으면 Stage 2 watch다."),
    Round241ScoreAdjustment("event_rally_before_earnings_bridge", -5, "lower", "이벤트가 먼저 가격을 움직이면 4B-watch부터 확인한다."),
)


ROUND241_SHADOW_WEIGHT_ROWS: tuple[Round241ShadowWeightRow, ...] = (
    Round241ShadowWeightRow(E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK, 0, 0, 0, 0, 5, 3, 0, 0, -5, 5, "Martial law crisis raises Korea discount and should trigger macro 4C-watch."),
    Round241ShadowWeightRow(E2RArchetype.GLOBAL_INDEX_INCLUSION, 4, 5, 5, 4, 4, 5, 0, 2, -2, 3, "WGBI inclusion is Stage 2; actual flow and funding-cost impact needed for Green."),
    Round241ShadowWeightRow(E2RArchetype.SHORT_SELLING_NORMALIZATION, 3, 4, 3, 5, 4, 2, 0, 1, -2, 3, "Short-selling normalization helps MSCI access but is not company Green."),
    Round241ShadowWeightRow(E2RArchetype.AI_WINDFALL_TAX_POLICY_SHOCK, 0, 0, 0, 0, 3, 2, 0, 0, -5, 5, "AI dividend/tax surprise can break policy confidence even if clarified later."),
    Round241ShadowWeightRow(E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK, 0, 0, 0, 0, 3, 5, 5, 0, 0, 5, "Hormuz/Iran shock is macro hard 4C for oil-import dependent Korea."),
    Round241ShadowWeightRow(E2RArchetype.POLICY_RELIEF_RESPONSE, 5, 2, 0, 0, 3, 4, 5, 2, -3, 3, "Energy-security policy response is relief, not Green, until cost/margin improves."),
    Round241ShadowWeightRow(E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE, 4, 4, 0, 3, 3, 5, 0, 1, -3, 4, "Kimchi bond/FX reform is Stage 2; actual KRW stabilization and inflow required."),
    Round241ShadowWeightRow(E2RArchetype.FX_OUTFLOW_TRADE_DEAL_OVERLAY, 3, 2, 0, 2, 3, 5, 0, 2, -4, 5, "$350B U.S. pledge creates FX-outflow watch despite tariff relief."),
)


ROUND241_DEEP_SUB_ARCHETYPES: tuple[Round241DeepSubArchetype, ...] = (
    Round241DeepSubArchetype("정치·제도 신뢰", E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK, ("martial law crisis", "institutional trust break", "Korea discount", "KRW two-year low")),
    Round241DeepSubArchetype("WGBI / 글로벌 채권지수", E2RArchetype.GLOBAL_INDEX_INCLUSION, ("WGBI inclusion", "80T won inflow", "2.22% weight", "phase-in schedule")),
    Round241DeepSubArchetype("공매도 / MSCI 접근성", E2RArchetype.SHORT_SELLING_NORMALIZATION, ("short-selling ban lifted", "MSCI developed market access", "unfair-trading penalty", "foreign flow")),
    Round241DeepSubArchetype("AI 세금 / 정책 신뢰", E2RArchetype.AI_WINDFALL_TAX_POLICY_SHOCK, ("AI dividend", "windfall tax concern", "redistribution surprise", "AI semiconductor basket")),
    Round241DeepSubArchetype("Hormuz / 에너지 안보", E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK, ("Hormuz disruption", "Middle East oil import dependency", "KRW 17-year low", "energy chokepoint")),
    Round241DeepSubArchetype("에너지 안보 대응", E2RArchetype.POLICY_RELIEF_RESPONSE, ("alternative suppliers", "strategic reserves", "Red Sea vessels", "maritime security support")),
    Round241DeepSubArchetype("Kimchi bond / FX 유동성", E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE, ("kimchi bond ban lifted", "FX futures ceiling raised", "stablecoin trading", "KRW stabilization")),
    Round241DeepSubArchetype("대미투자 / FX outflow", E2RArchetype.FX_OUTFLOW_TRADE_DEAL_OVERLAY, ("$350B U.S. investment pledge", "FX bond cap", "retail U.S. stock holdings", "capital outflow")),
)


ROUND241_CASE_CANDIDATES: tuple[Round241CaseCandidate, ...] = (
    Round241CaseCandidate(
        case_id="r11_loop10_martial_law_institutional_trust_shock",
        symbol="KOSPI/KRW",
        company_name="South Korea political institutional trust shock",
        primary_archetype=E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK,
        secondary_archetypes=(E2RArchetype.MACRO_HARD_4C, E2RArchetype.POLICY_CONFIDENCE_EVENT_PREMIUM),
        case_type="4c_thesis_break",
        round_case_type="4c_watch_macro_institutional_trust_break",
        stage1_date=date(2024, 12, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 4),
        stage3_decision="martial_law_crisis_is_institutional_trust_4c_watch_not_company_green",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("martial_law_declaration", "short_lived_reversal", "kospi_nearly_minus_2pct", "won_two_year_low"),
        red_flag_fields=("martial_law_or_institutional_shock", "political_legitimacy_crisis", "korea_discount_risk_premium_up"),
        price_data_source="Reuters political-crisis / market-reaction anchor",
        reported_price_anchor="KOSPI nearly -2%; won two-year low after short-lived martial-law crisis",
        reported_return_anchor="market-level anchor, not company OHLC",
        mfe_1d=None,
        mae_1d=-2.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_event_mae_pct": "nearly -2", "krw_status": "two-year low", "event_scope": "market_level"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="institutional_trust_break_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="macro_4c_watch_not_company_green",
        price_validation_status="market_level_anchor_not_full_ohlc",
        notes="Martial law crisis is macro 4C-watch; no company Green until institutional risk premium normalizes.",
    ),
    Round241CaseCandidate(
        case_id="r11_loop10_wgbi_inclusion_market_structure",
        symbol="Korean_government_bonds/KRW/Korea_assets",
        company_name="WGBI inclusion",
        primary_archetype=E2RArchetype.GLOBAL_INDEX_INCLUSION,
        secondary_archetypes=(E2RArchetype.MARKET_STRUCTURE_REFORM,),
        case_type="success_candidate",
        round_case_type="success_candidate_market_structure_stage2",
        stage1_date=date(2024, 10, 8),
        stage2_date=date(2025, 11, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="wgbi_is_market_structure_stage2_until_actual_inflows_rates_fx_and_company_funding_cost_bridge_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("wgbi_inclusion_confirmed", "expected_inflows_80tn_krw", "wgbi_weight_2_22pct", "one_year_quarterly_phase_in"),
        red_flag_fields=("index_inclusion_expectation_only", "actual_flow_unverified", "company_funding_cost_effect_unverified"),
        price_data_source="Reuters WGBI inclusion anchors",
        reported_price_anchor="Expected inflow up to 80T KRW / $59.7B; WGBI weight 2.22%",
        reported_return_anchor="KOSPI 2024 context -2.3%; bond market $2.2T",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"expected_inflows_krw_trn": 80.0, "expected_inflows_usd_bn": 59.7, "wgbi_weight_pct": 2.22, "bond_market_size_usd_trn": 2.2, "kospi_2024_context_pct": -2.3, "phase_in_period": "one_year_quarterly"},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_result="market_structure_bond_inflow_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_market_structure_not_company_green",
        price_validation_status="market_structure_anchor_not_company_ohlc",
        notes="WGBI is Stage 2 market-structure evidence; actual inflows, rates, FX and corporate funding-cost effects required before company Green.",
    ),
    Round241CaseCandidate(
        case_id="r11_loop10_short_selling_msci_access_reform",
        symbol="KOSPI/KOSDAQ/brokerage_foreign_access_basket",
        company_name="Short-selling normalization / MSCI access reform",
        primary_archetype=E2RArchetype.SHORT_SELLING_NORMALIZATION,
        secondary_archetypes=(E2RArchetype.MARKET_STRUCTURE_REFORM,),
        case_type="success_candidate",
        round_case_type="success_candidate_market_access_stage2",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 4, 21),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="short_selling_normalization_is_stage2_until_msci_inclusion_foreign_flow_and_company_bridge_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("market_wide_short_selling_ban_lifted", "five_year_ban_ended", "msci_issues_over_90pct_addressed", "one_strike_out_unfair_trading_penalty"),
        red_flag_fields=("market_reform_without_foreign_flow", "msci_watchlist_unverified", "company_eps_bridge_absent"),
        price_data_source="Reuters market-access / short-selling reform anchors",
        reported_price_anchor="Five-year ban lifted; regulator said over 90% of MSCI issues addressed",
        reported_return_anchor="Penalties up to 100% of short-sale orders for serious violations",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ban_duration_years": 5.0, "msci_issue_resolution_pct": 90.0, "penalty_for_serious_short_sale_violation_pct_of_orders": 100.0, "unfair_trading_rule_date": "2025-07-09"},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_result="MSCI_market_access_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_market_structure_not_green",
        price_validation_status="policy_anchor_not_full_ohlc",
        notes="Short-selling normalization is Stage 2 market access; MSCI watchlist/inclusion and foreign flow required before Green.",
    ),
    Round241CaseCandidate(
        case_id="r11_loop10_ai_dividend_tax_policy_confidence_shock",
        symbol="KOSPI/Samsung/SK_Hynix/AI_semiconductor_basket",
        company_name="AI dividend / AI windfall policy shock",
        primary_archetype=E2RArchetype.AI_WINDFALL_TAX_POLICY_SHOCK,
        secondary_archetypes=(E2RArchetype.POLICY_CONFIDENCE_EVENT_PREMIUM, E2RArchetype.MEMORY_HBM_CAPACITY),
        case_type="4c_thesis_break",
        round_case_type="4c_watch_policy_confidence_break",
        stage1_date=date(2026, 5, 12),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 12),
        stage3_decision="ai_dividend_tax_language_is_policy_confidence_4c_watch_before_any_positive_ai_semiconductor_green",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ai_dividend_comment", "windfall_tax_concern", "clarification_excess_tax_revenue_not_direct_corporate_tax", "kospi_intraday_minus_5_1pct", "kospi_close_minus_2_3pct"),
        red_flag_fields=("tax_or_redistribution_surprise", "policy_confidence_break", "ai_semiconductor_risk_premium_up"),
        price_data_source="FT/Barron's/MarketWatch policy-shock anchors",
        reported_price_anchor="KOSPI intraday -5.1%, close -2.3%",
        reported_return_anchor="AI boom tax revenue redistribution interpreted as windfall-tax risk before clarification",
        mfe_1d=None,
        mae_1d=-5.1,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_intraday_mae_pct": -5.1, "kospi_close_mae_pct": -2.3, "policy_read": "AI windfall redistribution / possible tax concern", "clarification": "excess tax revenue, not direct corporate-profit windfall tax"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="AI_windfall_tax_policy_confidence_break",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="4c_watch_not_hard_4c",
        price_validation_status="reported_market_anchor_not_full_ohlc",
        notes="AI dividend/tax language is 4C-watch because it hit risk premium before any law or company earnings bridge.",
    ),
    Round241CaseCandidate(
        case_id="r11_loop10_hormuz_iran_energy_shock_hard_4c",
        symbol="KOSPI/KRW/exporters/refiners/airlines/autos/chips",
        company_name="Hormuz / Iran geopolitical energy shock",
        primary_archetype=E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK,
        secondary_archetypes=(E2RArchetype.MACRO_HARD_4C,),
        case_type="4c_thesis_break",
        round_case_type="macro_hard_4c",
        stage1_date=date(2026, 3, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 4),
        stage3_decision="hormuz_iran_energy_shock_is_macro_hard_4c_due_to_kospi_krw_auto_chip_energy_drawdown",
        stage4b_status="hard_4c",
        hard_4c_confirmed=True,
        evidence_fields=("hormuz_disruption", "kospi_minus_12_06pct", "krw_17_year_low", "hyundai_minus_15_8pct", "samsung_minus_11_7pct", "sk_hynix_minus_9_6pct"),
        red_flag_fields=("geopolitical_energy_chokepoint_closure", "krw_disorderly_depreciation", "market_wide_crash", "oil_import_dependency"),
        price_data_source="Reuters geopolitical energy-shock / market-return anchor",
        reported_price_anchor="KOSPI -12.06% to 5,093.54; won touched 1,505.8/USD",
        reported_return_anchor="Hyundai -15.8%, Samsung Electronics -11.7%, SK Hynix -9.6%; $553.82B wiped out over two days",
        mfe_1d=None,
        mae_1d=-12.06,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=5093.54,
        extra_price_metrics={"kospi_event_mae_pct": -12.06, "kospi_close": 5093.54, "market_cap_wipeout_2d_usd_bn": 553.82, "krw_intraday_low_per_usd": 1505.8, "krw_close_per_usd": 1485.7, "hyundai_motor_mae_pct": -15.8, "samsung_electronics_mae_pct": -11.7, "sk_hynix_mae_pct": -9.6, "middle_east_oil_import_dependency_pct": 70.0},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break",
        rerating_result="thesis_break",
        round_rerating_result="geopolitical_energy_security_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="macro_hard_4C",
        price_validation_status="reported_market_and_stock_anchor_not_full_ohlc",
        notes="Hormuz/Iran shock is macro hard 4C due to KOSPI crash, KRW 17-year low, and exporter/chip/auto drawdown.",
    ),
    Round241CaseCandidate(
        case_id="r11_loop10_hormuz_energy_security_policy_relief",
        symbol="refiners/LNG/shipping/defense/energy_security_basket",
        company_name="Hormuz energy-security policy response",
        primary_archetype=E2RArchetype.POLICY_RELIEF_RESPONSE,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK,),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2026, 4, 6),
        stage2_date=date(2026, 5, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="energy_security_policy_response_is_stage2_relief_until_oil_lng_costs_sector_margin_and_fx_stabilize",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("alternative_routes_suppliers", "Saudi_Oman_Algeria_talks", "strategic_oil_reserves", "five_korean_vessels_via_red_sea", "phased_hormuz_maritime_security_support"),
        red_flag_fields=("energy_security_headline_without_cost_stabilization", "margin_unverified", "troop_or_security_escalation_watch"),
        price_data_source="Reuters energy-security policy-response anchors",
        reported_price_anchor="Alternative suppliers/routes, reserves, Red Sea vessels and phased maritime-security role discussed",
        reported_return_anchor="No equity OHLC path; policy relief anchor only",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"policy_tools": ["alternative_routes_suppliers", "Saudi/Oman/Algeria_talks", "strategic_oil_reserves", "five_Korean_vessels_via_Red_Sea", "phased_Hormuz_maritime_security_support"]},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_policy_relief",
        rerating_result="event_premium",
        round_rerating_result="energy_security_policy_response_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_relief_not_green",
        price_validation_status="policy_anchor_not_equity_ohlc",
        notes="Policy response is Stage 2 relief, not Green, until oil/LNG costs and sector margins stabilize.",
    ),
    Round241CaseCandidate(
        case_id="r11_loop10_kimchi_bond_fx_liquidity_policy",
        symbol="KRW/banks/brokers/exporters",
        company_name="Kimchi bond / FX liquidity policy response",
        primary_archetype=E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE,
        secondary_archetypes=(E2RArchetype.STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO,),
        case_type="success_candidate",
        round_case_type="success_candidate_fx_policy_stage2",
        stage1_date=date(2024, 12, 20),
        stage2_date=date(2025, 6, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="fx_policy_response_is_stage2_until_actual_krw_stabilization_funding_cost_relief_and_foreign_inflow_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("corporate_foreign_currency_borrowing_allowed", "kimchi_bond_ban_lifted", "fx_futures_ceiling_raised", "stablecoin_trading_57tn_krw", "krw_1347_to_1353_anchor"),
        red_flag_fields=("fx_policy_without_actual_flow", "stablecoin_outflow_pressure", "overseas_stock_outflow_watch"),
        price_data_source="FT/Reuters FX-policy anchors",
        reported_price_anchor="KRW strengthened to 1,347/USD then stabilized around 1,353/USD",
        reported_return_anchor="Q1 stablecoin trading 57T KRW / $42B; local bank FX futures ceiling 50% to 75%",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"q1_stablecoin_trading_krw_trn": 57.0, "q1_stablecoin_trading_usd_bn": 42.0, "krw_strength_after_policy_per_usd": 1347.0, "krw_stabilization_level_per_usd": 1353.0, "fx_futures_ceiling_local_banks_before_pct": 50.0, "fx_futures_ceiling_local_banks_after_pct": 75.0, "fx_futures_ceiling_foreign_branches_before_pct": 250.0, "fx_futures_ceiling_foreign_branches_after_pct": 375.0, "ceiling_increase_pct": 50.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_result="FX_liquidity_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_macro_relief_not_company_green",
        price_validation_status="fx_policy_anchor_not_company_ohlc",
        notes="FX policy response is Stage 2; actual KRW stabilization, funding-cost relief and foreign inflows required before Green.",
    ),
    Round241CaseCandidate(
        case_id="r11_loop10_us_investment_fx_outflow_watch",
        symbol="KRW/exporters/banks/FX_sensitive_basket",
        company_name="$350B U.S. investment pledge / FX outflow watch",
        primary_archetype=E2RArchetype.FX_OUTFLOW_TRADE_DEAL_OVERLAY,
        secondary_archetypes=(E2RArchetype.STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO, E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE),
        case_type="4c_thesis_break",
        round_case_type="macro_4c_watch_policy_relief",
        stage1_date=date(2025, 12, 1),
        stage2_date=date(2025, 12, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 3),
        stage3_decision="us_investment_pledge_has_tariff_relief_but_fx_outflow_watch_blocks_green_until_krw_and_reserves_stabilize",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_investment_pledge_350bn_usd", "fx_bond_cap_2026_5bn_usd", "annual_dollar_outflow_limit_20bn_usd", "retail_us_stock_holdings_160bn_usd", "krw_down_8pct_since_end_june"),
        red_flag_fields=("capital_outflow_pressure", "krw_depreciation_watch", "tariff_relief_without_fx_stability", "foreign_bond_cap_is_defensive_policy"),
        price_data_source="FT FX-bond / capital-outflow anchor",
        reported_price_anchor="FX bond cap $3.5B to $5B; KRW -8% since end-June; retail U.S. stock holdings $160B",
        reported_return_anchor="$350B U.S. investment pledge with $20B annual dollar outflow limit",
        mfe_1d=None,
        mae_1d=-8.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"us_investment_pledge_usd_bn": 350.0, "annual_dollar_outflow_limit_usd_bn": 20.0, "fx_bond_cap_2026_usd_bn": 5.0, "fx_bond_cap_2025_usd_bn": 3.5, "cap_increase_pct": 42.9, "krw_decline_since_end_june_pct": -8.0, "retail_us_stock_net_buy_2025_usd_bn": 30.0, "retail_us_stock_holdings_usd_bn": 160.0, "fx_reserves_context_usd_bn": 430.7},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="macro_4C_watch_policy_relief",
        rerating_result="thesis_break",
        round_rerating_result="tariff_relief_with_FX_outflow_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="macro_watch_not_green",
        price_validation_status="macro_anchor_not_equity_ohlc",
        notes="Tariff relief is offset by structural dollar-outflow pressure; FX stabilization needed before Green.",
    ),
)


def round241_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND241_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round241 R11 Loop-10 policy/geopolitical/event price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "policy" in field
                or "shock" in field
                or "inclusion" in field
                or "ban" in field
                or "bond" in field
                or "hormuz" in field
                or "martial" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "inflow" in field or "funding" in field or "company" in field or "eps" in field or "fcf" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "rally" in field or "expectation" in field or "headline" in field or "price" in field or "event" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "shock" in field
                or "crisis" in field
                or "break" in field
                or "depreciation" in field
                or "outflow" in field
                or "chokepoint" in field
                or "crash" in field
            ),
            must_have_fields=ROUND241_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND241_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "r11_default_stage3_bias_very_conservative",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_geopolitical_fx_or_index_headline_as_green",
                *ROUND241_GREEN_REQUIRED_FIELDS,
                *ROUND241_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round241_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND241_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
                "round_case_type": candidate.round_case_type,
                "stage1_date": _date_text(candidate.stage1_date),
                "stage2_date": _date_text(candidate.stage2_date),
                "stage3_date": _date_text(candidate.stage3_date),
                "stage4b_date": _date_text(candidate.stage4b_date),
                "stage4c_date": _date_text(candidate.stage4c_date),
                "stage3_decision": candidate.stage3_decision,
                "stage4b_status": candidate.stage4b_status,
                "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "score_price_alignment": candidate.score_price_alignment,
                "round_score_price_alignment": candidate.round_score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "round_rerating_result": candidate.round_rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "round_stage_failure_type": candidate.round_stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round241_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND241_SCORE_ADJUSTMENTS)


def round241_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND241_SHADOW_WEIGHT_ROWS)


def round241_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND241_DEEP_SUB_ARCHETYPES)


def round241_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round241_price_validation": "true"} for field in ROUND241_PRICE_VALIDATION_FIELDS)


def round241_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round241_label": label, "canonical_archetype": canonical} for label, canonical in ROUND241_REQUIRED_TARGET_ALIASES.items())


def round241_summary() -> dict[str, int | bool | str]:
    cases = ROUND241_CASE_CANDIDATES
    return {
        "source_round": ROUND241_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND241_ANALYST_ROUND_ID,
        "large_sector": ROUND241_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "policy_relief_count": sum(1 for case in cases if "policy_relief" in case.round_case_type),
        "target_archetype_count": len(ROUND241_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND241_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND241_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r11_default_stage3_bias": ROUND241_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round241_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND241_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND241_ANALYST_ROUND_ID,
        "large_sector": ROUND241_LARGE_SECTOR.value,
        "summary": round241_summary(),
        "target_aliases": dict(ROUND241_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND241_CASE_CANDIDATES},
        "green_required_fields": list(ROUND241_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND241_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND241_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND241_HARD_4C_GATES),
        "deep_sub_archetypes": round241_deep_sub_archetype_rows(),
        "shadow_weights": round241_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round241_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_policy_geopolitical_fx_index_or_energy_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_hormuz_iran_energy_shock_as_macro_hard_4c_reference",
        ],
    }


def render_round241_summary_markdown() -> str:
    summary = round241_summary()
    lines = [
        "# Round 241 R11 Loop 10 Policy Geopolitical Event Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- policy_relief_count: {summary['policy_relief_count']}",
        f"- deep_sub_archetype_count: {summary['deep_sub_archetype_count']}",
        f"- shadow_weight_row_count: {summary['shadow_weight_row_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND241_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    str(case.hard_4c_confirmed).lower(),
                    case.round_score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- WGBI and short-selling normalization are market-structure Stage 2, not company Green.",
            "- Martial-law and AI dividend/tax shocks are policy-confidence 4C-watch cases.",
            "- Hormuz/Iran energy shock is the macro hard 4C reference for R11.",
            "- FX relief and foreign-bond caps are defensive policy responses until KRW stability and funding-cost relief are visible.",
            "- Easy example: `policy headline + basket rally` is Stage 1/2; `policy + actual flow + company EPS/FCF bridge` is required before deeper Stage review.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round241_green_gate_review_markdown() -> str:
    lines = [
        "# Round 241 R11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND241_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND241_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `WGBI inclusion` can be Stage 2 market-structure evidence.",
            "- `WGBI inclusion + actual inflow + lower funding cost + company EPS/FCF bridge` is the kind of bundle that can support later Stage review.",
            "- `AI tax speech + KOSPI selloff` is 4C-watch, not a positive rerating input.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round241_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 241 R11 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND241_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND241_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND241_CASE_CANDIDATES:
        if case.stage4b_status in {"watch", "hard_4c"} or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round241_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 241 R11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND241_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round241_r11_loop10_reports(
    output_directory: str | Path = ROUND241_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND241_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND241_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round241_case_records(), cases_path),
        "audit": _write_json(round241_audit_payload(), audit_path),
        "summary": output / "round241_r11_loop10_price_validation_summary.md",
        "case_matrix": output / "round241_r11_loop10_case_matrix.csv",
        "target_aliases": output / "round241_r11_loop10_target_aliases.csv",
        "score_adjustments": output / "round241_r11_loop10_score_adjustments.csv",
        "shadow_weights": output / "round241_r11_loop10_shadow_weights.csv",
        "deep_sub_archetypes": output / "round241_r11_loop10_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round241_r11_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round241_r11_loop10_green_gate_review.md",
        "price_validation_plan": output / "round241_r11_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round241_r11_loop10_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round241_summary_markdown(), encoding="utf-8")
    _write_csv(round241_case_rows(), paths["case_matrix"])
    _write_csv(round241_target_alias_rows(), paths["target_aliases"])
    _write_csv(round241_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round241_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round241_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round241_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round241_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round241_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round241_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def _write_json(payload: object, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[dict[str, str]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows = tuple(rows)
    if not rows:
        target.write_text("", encoding="utf-8")
        return target
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed(value: int) -> str:
    return f"{value:+d}"
