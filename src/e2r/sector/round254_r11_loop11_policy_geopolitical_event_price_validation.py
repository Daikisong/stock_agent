"""Round-254 R11 Loop-11 policy/geopolitical/event price-validation pack.

This module converts ``docs/round/round_254.md`` into calibration-only case
records. It does not change production scoring, staging, or candidate
generation.

Easy example: WGBI inclusion plus actual foreign bond inflow can be Stage 2
market-structure evidence. It is still not company Stage 3-Green until company
revenue, EPS/FCF, funding-cost, and FX bridges are visible.
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


ROUND254_SOURCE_ROUND_PATH = "docs/round/round_254.md"
ROUND254_ANALYST_ROUND_ID = "round_182"
ROUND254_LARGE_SECTOR = Round10LargeSector.POLICY_GEOPOLITICAL_EVENT
ROUND254_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round254_r11_loop11_policy_geopolitical_event_price_validation"
ROUND254_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop11_round254.jsonl"
ROUND254_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round254_r11_loop11_policy_geopolitical_event_price_validation_audit.json"
ROUND254_DEFAULT_STAGE3_BIAS = "very_conservative"

ROUND254_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "POLITICAL_INSTITUTIONAL_TRUST_BREAK": E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK.value,
    "GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW": E2RArchetype.GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW.value,
    "SHORT_SELLING_MARKET_ACCESS_REFORM": E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM.value,
    "CORPORATE_GOVERNANCE_VALUEUP_POLICY": E2RArchetype.CORPORATE_GOVERNANCE_VALUEUP_POLICY.value,
    "AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK": E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK.value,
    "GEOPOLITICAL_ENERGY_SECURITY_HARD_4C": E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C.value,
    "HORMUZ_POLICY_RELIEF_RESPONSE": E2RArchetype.HORMUZ_POLICY_RELIEF_RESPONSE.value,
    "FX_LIQUIDITY_STABLECOIN_OUTFLOW": E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW.value,
    "FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW": E2RArchetype.FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW.value,
    "POLICY_HEADLINE_NOT_GREEN": E2RArchetype.POLICY_HEADLINE_NOT_GREEN.value,
}

ROUND254_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "policy_actual_law_budget_index_inclusion_or_capital_inflow_confirmed",
    "company_revenue_eps_fcf_bridge_exists",
    "foreign_flow_or_funding_cost_improvement_confirmed",
    "fx_rates_or_credit_cost_effect_positive",
    "political_institutional_regulatory_trust_intact",
    "no_tax_or_redistribution_surprise",
    "no_energy_or_geopolitical_hard_risk",
    "price_path_after_evidence",
)

ROUND254_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_speech_only",
    "election_pledge_only",
    "tax_or_redistribution_surprise",
    "geopolitical_headline_only",
    "wgbi_msci_expectation_only",
    "fx_policy_without_actual_flow",
    "stablecoin_theme_only",
    "event_rally_before_earnings_bridge",
)

ROUND254_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "wgbi_msci_expectation_rally",
    "commercial_act_expectation_rally",
    "policy_speech_theme_rally",
    "ai_dividend_tax_selloff_rebound_before_clarity",
    "energy_security_headline_rally",
    "fx_policy_relief_bank_exporter_rerating",
    "stablecoin_theme_two_to_three_times",
)

ROUND254_HARD_4C_GATES: tuple[str, ...] = (
    "martial_law_or_coup_like_institutional_shock",
    "major_political_legitimacy_crisis",
    "tax_or_windfall_redistribution_shock",
    "geopolitical_energy_chokepoint_closure",
    "kospi_circuit_breaker",
    "krw_disorderly_depreciation",
    "foreign_capital_flight",
    "index_inclusion_failure",
    "msci_access_disappointment",
    "fx_liquidity_breakdown",
    "stablecoin_driven_capital_outflow",
    "policy_reversal",
)

ROUND254_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "index_anchor",
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
class Round254ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round254ShadowWeightRow:
    archetype: E2RArchetype
    actual_capital_inflow: int
    funded_policy: int
    market_access_improvement: int
    governance_implementation: int
    institutional_trust: int
    fx_stability: int
    energy_security_resilience: int
    policy_to_company_revenue_bridge: int
    foreign_flow_confirmation: int
    event_penalty: int
    macro_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_capital_inflow": _signed(self.actual_capital_inflow),
            "funded_policy": _signed(self.funded_policy),
            "market_access_improvement": _signed(self.market_access_improvement),
            "governance_implementation": _signed(self.governance_implementation),
            "institutional_trust": _signed(self.institutional_trust),
            "fx_stability": _signed(self.fx_stability),
            "energy_security_resilience": _signed(self.energy_security_resilience),
            "policy_to_company_revenue_bridge": _signed(self.policy_to_company_revenue_bridge),
            "foreign_flow_confirmation": _signed(self.foreign_flow_confirmation),
            "event_penalty": _signed(self.event_penalty),
            "macro_4c_sensitivity": _signed(self.macro_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round254DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round254CaseCandidate:
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
        return ROUND254_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND254_SCORE_ADJUSTMENTS: tuple[Round254ScoreAdjustment, ...] = (
    Round254ScoreAdjustment("actual_capital_inflow", 5, "raise", "WGBI 같은 정책도 실제 외국인 자금유입이 확인될 때만 Stage 2 품질이 오른다."),
    Round254ScoreAdjustment("funded_policy", 5, "raise", "법안·예산·집행 재원이 확인된 정책만 정책 발언보다 높게 본다."),
    Round254ScoreAdjustment("market_access_improvement", 5, "raise", "공매도 정상화와 MSCI 접근성 개선은 시장구조 Stage 2 증거다."),
    Round254ScoreAdjustment("governance_implementation", 4, "raise", "자사주소각 의무처럼 실제 이행 규칙이 있을 때 value-up 신뢰도가 오른다."),
    Round254ScoreAdjustment("institutional_trust", 5, "raise", "정치·제도 신뢰가 유지되어야 Korea discount 축소 논리가 유지된다."),
    Round254ScoreAdjustment("FX_stability", 5, "raise", "원화 안정은 funding cost와 외국인 flow의 기본 조건이다."),
    Round254ScoreAdjustment("energy_security_resilience", 5, "raise", "에너지 충격 후 비용 안정과 공급망 복구가 확인되어야 한다."),
    Round254ScoreAdjustment("policy_to_company_revenue_bridge", 5, "raise", "정책이 회사 매출·마진·EPS/FCF로 내려와야 Green 검토가 가능하다."),
    Round254ScoreAdjustment("foreign_flow_confirmation", 5, "raise", "실제 외국인 flow 확인은 기대 기반 리레이팅과 구분된다."),
    Round254ScoreAdjustment("policy_speech_only", -5, "lower", "발언만 있고 법안·예산·자금유입·회사 bridge가 없으면 Green 금지다."),
    Round254ScoreAdjustment("tax_or_redistribution_surprise", -5, "lower", "AI dividend/tax 같은 surprise는 risk premium을 먼저 깬다."),
    Round254ScoreAdjustment("political_institutional_shock", -5, "lower", "martial-law shock은 시장 전체 4C-watch다."),
    Round254ScoreAdjustment("geopolitical_energy_shock", -5, "lower", "Hormuz shock은 에너지·환율·수출주 리스크를 동시에 키운다."),
    Round254ScoreAdjustment("stablecoin_policy_theme_only", -5, "lower", "stablecoin 테마만 있고 규제수익/FX 안정이 없으면 Green 근거가 아니다."),
    Round254ScoreAdjustment("FX_policy_without_flow", -4, "lower", "FX 정책만 있고 실제 안정/유입이 없으면 Stage 2 watch에 머문다."),
    Round254ScoreAdjustment("index_inclusion_expectation_only", -3, "lower", "WGBI/MSCI 기대만으로 특정 종목 Green은 금지한다."),
    Round254ScoreAdjustment("market_reform_without_foreign_flow", -3, "lower", "공매도 정상화만 있고 foreign flow가 없으면 Stage 2 watch다."),
    Round254ScoreAdjustment("foreign_investment_pledge_outflow", -4, "lower", "대규모 해외투자 약속은 관세 relief와 별개로 FX outflow watch다."),
    Round254ScoreAdjustment("event_rally_before_earnings_bridge", -5, "lower", "이벤트가 먼저 가격을 움직이면 4B-watch부터 확인한다."),
)


ROUND254_SHADOW_WEIGHT_ROWS: tuple[Round254ShadowWeightRow, ...] = (
    Round254ShadowWeightRow(E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK, 0, 0, 0, 0, 5, 2, 0, 0, 0, -5, 5, "Martial law crisis is institutional trust 4C-watch, not company Green."),
    Round254ShadowWeightRow(E2RArchetype.GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW, 5, 4, 3, 0, 4, 5, 0, 2, 5, -2, 2, "WGBI is Stage 2 only after actual capital inflow; company Green needs EPS/FCF bridge."),
    Round254ShadowWeightRow(E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM, 3, 3, 5, 0, 4, 2, 0, 1, 3, -2, 3, "Short-selling normalization helps market access, but not company earnings by itself."),
    Round254ShadowWeightRow(E2RArchetype.CORPORATE_GOVERNANCE_VALUEUP_POLICY, 2, 5, 2, 4, 4, 2, 0, 3, 2, -2, 2, "Commercial Act value-up is Stage 2 until actual cancellation, ROE/PBR, and shareholder return bridge appear."),
    Round254ShadowWeightRow(E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK, 0, 0, 0, 0, 2, 1, 0, 0, 0, -5, 5, "AI dividend/tax language can break policy confidence before law text is known."),
    Round254ShadowWeightRow(E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C, 0, 0, 0, 0, 2, 5, 5, 0, 0, 0, 5, "Hormuz/Iran shock is hard macro 4C for oil-import dependent Korea."),
    Round254ShadowWeightRow(E2RArchetype.HORMUZ_POLICY_RELIEF_RESPONSE, 1, 5, 0, 0, 3, 4, 5, 2, 1, -3, 3, "Hormuz response is policy relief until oil/LNG cost and margin stabilization is verified."),
    Round254ShadowWeightRow(E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW, 2, 4, 2, 0, 3, 5, 0, 1, 2, -5, 5, "Kimchi bond relief and stablecoin outflow risk must be separated."),
    Round254ShadowWeightRow(E2RArchetype.FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW, 1, 4, 1, 0, 3, 5, 0, 2, 1, -4, 5, "$350B pledge can be tariff relief and FX outflow risk at the same time."),
    Round254ShadowWeightRow(E2RArchetype.POLICY_HEADLINE_NOT_GREEN, 0, 1, 0, 0, 1, 0, 0, 0, 0, -5, 3, "Policy headline alone is not Stage 3-Green."),
)


ROUND254_DEEP_SUB_ARCHETYPES: tuple[Round254DeepSubArchetype, ...] = (
    Round254DeepSubArchetype("정치·제도 신뢰", E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK, ("martial law crisis", "Korea discount risk premium", "won / KOSPI shock", "unlimited liquidity")),
    Round254DeepSubArchetype("시장구조", E2RArchetype.GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW, ("WGBI inclusion", "actual foreign bond inflow", "2.22% weight", "largest monthly inflow since 2016")),
    Round254DeepSubArchetype("공매도 / MSCI 접근성", E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM, ("short-selling normalization", "MSCI accessibility", "one-strike-out", "100% order penalty")),
    Round254DeepSubArchetype("밸류업·상법", E2RArchetype.CORPORATE_GOVERNANCE_VALUEUP_POLICY, ("treasury share cancellation mandate", "minority shareholder rights", "Korea Discount policy", "ROE/PBR bridge")),
    Round254DeepSubArchetype("AI dividend / tax", E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK, ("AI boom excess tax revenue", "Samsung / SK Hynix selloff", "policy-confidence 4C-watch")),
    Round254DeepSubArchetype("지정학·에너지", E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C, ("Iran / Hormuz conflict", "KOSPI circuit breaker level selloff", "KRW 17-year low", "Middle East oil dependency")),
    Round254DeepSubArchetype("Hormuz 정책대응", E2RArchetype.HORMUZ_POLICY_RELIEF_RESPONSE, ("maritime-security support", "information sharing", "oil above $100/bbl", "policy relief not Green")),
    Round254DeepSubArchetype("FX / capital flow", E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW, ("kimchi bond deregulation", "dollar-backed stablecoin trading", "overseas-stock retail outflow", "500M won issuer equity")),
    Round254DeepSubArchetype("대미투자 / FX outflow", E2RArchetype.FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW, ("$350B U.S. investment pledge", "$20B annual outflow limit", "$5B FX bond cap", "retail U.S. stock holdings")),
)


ROUND254_CASE_CANDIDATES: tuple[Round254CaseCandidate, ...] = (
    Round254CaseCandidate(
        case_id="r11_loop11_martial_law_institutional_trust_4c_watch",
        symbol="KOSPI/KRW/Korea_risk_premium",
        company_name="Martial law crisis institutional trust break",
        primary_archetype=E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK,
        secondary_archetypes=(E2RArchetype.MACRO_HARD_4C, E2RArchetype.POLICY_CONFIDENCE_EVENT_PREMIUM),
        case_type="failed_rerating",
        round_case_type="4c_watch_macro_institutional_trust_break",
        stage1_date=date(2024, 12, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 4),
        stage3_decision="institutional_trust_shock_is_red_team_4c_watch_not_positive_stage",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("martial_law_declaration", "won_two_year_low", "kospi_nearly_minus_2pct", "unlimited_liquidity_pledge", "market_stabilization_fund_10tn_won"),
        red_flag_fields=("martial_law_or_institutional_shock", "political_legitimacy_crisis", "korea_discount_risk_premium_up"),
        price_data_source="Reuters political-crisis / market-stabilization anchors",
        reported_price_anchor="KOSPI nearly -2%; won two-year low; up to 10T won market-stabilization fund",
        reported_return_anchor="market-level anchor, not company OHLC",
        mfe_1d=None,
        mae_1d=-2.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_event_mae_pct": -2.0, "krw_status": "two-year low", "liquidity_response": "unlimited", "market_stabilization_fund_krw_trn": 10.0},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="institutional_trust_break_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="macro_4C_watch_not_company_green",
        price_validation_status="market_level_anchor_not_full_ohlc",
        notes="Institutional trust shock raises Korea discount risk premium and must block unsafe company Green.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_wgbi_actual_bond_inflow_stage2",
        symbol="Korean_government_bonds/KRW/financial_market_access_basket",
        company_name="WGBI inclusion actual bond inflow",
        primary_archetype=E2RArchetype.GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW,
        secondary_archetypes=(E2RArchetype.GLOBAL_INDEX_INCLUSION, E2RArchetype.MARKET_STRUCTURE_REFORM),
        case_type="success_candidate",
        round_case_type="success_candidate_capital_flow_stage2",
        stage1_date=date(2024, 10, 8),
        stage2_date=date(2025, 12, 15),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="wgbi_actual_inflow_is_stage2_until_company_funding_cost_eps_fcf_bridge_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("wgbi_inclusion_confirmed", "wgbi_weight_2_22pct", "foreign_bond_inflow_11_08bn_usd", "largest_monthly_inflow_since_2016"),
        red_flag_fields=("index_inclusion_expectation_only", "company_funding_cost_effect_unverified", "company_eps_bridge_absent"),
        price_data_source="Reuters WGBI inclusion / foreign bond inflow anchors",
        reported_price_anchor="WGBI weight 2.22%; Korean bonds +$11.08B net foreign inflow in November 2025",
        reported_return_anchor="regional bond inflows $10.86B across selected Asian markets",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"wgbi_weight_pct": 2.22, "foreign_bond_inflow_nov_2025_usd_bn": 11.08, "regional_bond_inflows_nov_2025_usd_bn": 10.86, "record_status": "largest monthly net inflow since at least 2016"},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_result="global_index_inclusion_capital_flow_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_market_structure_not_company_green",
        price_validation_status="capital_flow_anchor_not_company_ohlc",
        notes="Actual WGBI-related bond inflow is Stage 2 market-structure evidence; company Green waits for funding-cost and EPS/FCF bridge.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_short_selling_market_access_reform",
        symbol="KOSPI/KOSDAQ/brokerages/foreign_access_basket",
        company_name="Short-selling normalization and unfair-trading crackdown",
        primary_archetype=E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM,
        secondary_archetypes=(E2RArchetype.SHORT_SELLING_NORMALIZATION, E2RArchetype.MARKET_STRUCTURE_REFORM),
        case_type="success_candidate",
        round_case_type="success_candidate_market_access_stage2",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 6, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="short_selling_access_reform_is_stage2_until_msci_foreign_flow_and_company_bridge_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("five_year_short_selling_ban_lifted", "msci_short_selling_accessibility_improved", "one_strike_out_policy", "penalty_up_to_100pct_short_sale_orders"),
        red_flag_fields=("market_reform_without_foreign_flow", "msci_watchlist_unverified", "company_eps_bridge_absent"),
        price_data_source="Reuters market-access / short-selling reform anchors",
        reported_price_anchor="Five-year ban lifted; MSCI access improved; one-strike-out policy strengthened",
        reported_return_anchor="Severe penalties up to 100% of short-sale orders",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ban_duration_years": 5.0, "msci_assessment": "short-selling accessibility improved / no major issue", "penalty_for_serious_short_sale_violation_pct_of_orders": 100.0, "one_strike_out_policy_date": "2025-07-09"},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_result="MSCI_market_access_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_market_structure_not_green",
        price_validation_status="policy_anchor_not_full_ohlc",
        notes="Market-access reform is Stage 2; it is not direct company EPS/FCF evidence.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_commercial_act_treasury_share_valueup",
        symbol="KOSPI/low_PBR/financial_holding_basket",
        company_name="Commercial Act treasury-share cancellation",
        primary_archetype=E2RArchetype.CORPORATE_GOVERNANCE_VALUEUP_POLICY,
        secondary_archetypes=(E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN, E2RArchetype.MARKET_STRUCTURE_REFORM),
        case_type="success_candidate",
        round_case_type="success_candidate_governance_valueup_stage2",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="commercial_act_policy_is_stage2_until_actual_cancellation_roe_pbr_and_shareholder_return_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("treasury_share_cancellation_mandate", "newly_acquired_cancel_within_one_year", "existing_treasury_share_six_month_grace", "administrative_fine_possible"),
        red_flag_fields=("policy_stage2_not_company_green", "implementation_delay_watch", "weak_roe_watch"),
        price_data_source="Reuters Commercial Act / value-up policy anchor",
        reported_price_anchor="Newly acquired treasury shares must be cancelled within one year; existing shares receive six-month grace period",
        reported_return_anchor="Policy anchor only; company ROE/PBR and cancellation execution required",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"newly_acquired_treasury_share_cancel_within_years": 1.0, "existing_treasury_share_grace_months": 6.0, "administrative_fine_possible": True},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_result="governance_valueup_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="policy_stage2_not_company_green",
        price_validation_status="policy_anchor_not_full_ohlc",
        notes="Value-up policy is Stage 2; actual cancellation, ROE, PBR gap and shareholder return bridge are required.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_ai_dividend_tax_policy_confidence_shock",
        symbol="KOSPI/Samsung/SK_Hynix/AI_semiconductor_basket",
        company_name="AI dividend / AI tax policy confidence shock",
        primary_archetype=E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK,
        secondary_archetypes=(E2RArchetype.AI_WINDFALL_TAX_POLICY_SHOCK, E2RArchetype.POLICY_CONFIDENCE_EVENT_PREMIUM, E2RArchetype.MEMORY_HBM_CAPACITY),
        case_type="failed_rerating",
        round_case_type="4c_watch_policy_confidence_break",
        stage1_date=date(2026, 5, 12),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 12),
        stage3_decision="ai_tax_or_redistribution_surprise_is_red_team_4c_watch_before_positive_ai_semiconductor_stage",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ai_dividend_or_bonus_comment", "initial_windfall_tax_interpretation", "kospi_intraday_minus_5_1pct", "kospi_close_minus_2_3pct", "clarification_excess_tax_revenue_not_direct_corporate_profit_tax"),
        red_flag_fields=("tax_or_redistribution_surprise", "policy_confidence_break", "ai_semiconductor_risk_premium_up"),
        price_data_source="MarketWatch / Barron's / FT policy-shock anchors",
        reported_price_anchor="KOSPI intraday -5.1%, close -2.3%; Samsung/SK Hynix selloff",
        reported_return_anchor="Clarification said excess tax revenue, not direct corporate-profit tax",
        mfe_1d=None,
        mae_1d=-5.1,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_intraday_mae_pct": -5.1, "kospi_close_mae_pct": -2.3, "policy_read_initial": "AI windfall tax / redistribution concern", "clarification": "excess tax revenue, not direct corporate profit tax"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="AI_policy_confidence_break",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="4C_watch_not_hard_4C",
        price_validation_status="reported_market_anchor_not_full_ohlc",
        notes="Policy-confidence shock should cap AI semiconductor optimism until tax design and EPS exposure are clear.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_hormuz_iran_energy_security_hard_4c",
        symbol="KOSPI/KRW/exporters/autos/chips/airlines/refiners",
        company_name="Hormuz / Iran geopolitical energy shock",
        primary_archetype=E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK, E2RArchetype.MACRO_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="macro_hard_4c",
        stage1_date=date(2026, 3, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 4),
        stage3_decision="hormuz_iran_energy_shock_is_macro_hard_4c_for_oil_import_dependent_korea",
        stage4b_status="hard_4c",
        hard_4c_confirmed=True,
        evidence_fields=("hormuz_disruption", "kospi_minus_12_06pct", "kospi_close_5093_54", "krw_1505_8_intraday", "hyundai_minus_15_8pct", "samsung_minus_11_7pct", "sk_hynix_minus_9_6pct"),
        red_flag_fields=("geopolitical_energy_chokepoint_closure", "krw_disorderly_depreciation", "market_wide_crash", "oil_import_dependency"),
        price_data_source="Reuters Korean-market geopolitical shock anchor",
        reported_price_anchor="KOSPI -12.06% to 5,093.54; KRW touched 1,505.8/USD",
        reported_return_anchor="Hyundai -15.8%, Samsung -11.7%, SK Hynix -9.6%; $553.82B market cap wiped out over two days",
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
        notes="Confirmed hard 4C: energy chokepoint shock, KRW stress, and broad exporter/chip/auto drawdown.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_hormuz_policy_relief_response",
        symbol="refiners/LNG/shipping/defense/energy_security_basket",
        company_name="Hormuz maritime-security policy response",
        primary_archetype=E2RArchetype.HORMUZ_POLICY_RELIEF_RESPONSE,
        secondary_archetypes=(E2RArchetype.POLICY_RELIEF_RESPONSE, E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2026, 4, 1),
        stage2_date=date(2026, 5, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="hormuz_policy_response_is_relief_until_oil_lng_shipping_cost_and_margin_stabilize",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("phased_hormuz_role", "political_support", "personnel_or_information_sharing", "military_assets_possible", "no_immediate_troop_expansion", "oil_above_100_bbl"),
        red_flag_fields=("energy_security_headline_without_cost_stabilization", "margin_unverified", "war_risk_premium_watch"),
        price_data_source="Reuters Hormuz policy-response / global corporate-cost anchors",
        reported_price_anchor="Phased maritime support possible; global company cost from Iran war at least $25B; oil above $100/bbl",
        reported_return_anchor="No equity OHLC path; policy relief anchor only",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"policy_tools": ["political_support", "personnel_deployment", "information_sharing", "military_assets"], "troop_expansion_immediate": False, "global_company_cost_from_iran_war_usd_bn": 25.0, "oil_price_context_usd_per_bbl_above": 100.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_policy_relief",
        rerating_result="event_premium",
        round_rerating_result="energy_security_policy_response_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_relief_not_green",
        price_validation_status="policy_anchor_not_equity_ohlc",
        notes="Hormuz response is relief, not Green, until actual energy cost and sector-margin stability is visible.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_fx_stablecoin_kimchi_bond_outflow_watch",
        symbol="KRW/banks/brokers/fintech/FX_sensitive_basket",
        company_name="FX liquidity, stablecoin outflow, and kimchi bond relief",
        primary_archetype=E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW,
        secondary_archetypes=(E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE, E2RArchetype.STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO),
        case_type="success_candidate",
        round_case_type="success_candidate_fx_relief_plus_4c_watch",
        stage1_date=date(2025, 6, 1),
        stage2_date=date(2025, 6, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 7, 27),
        stage3_decision="fx_policy_relief_and_stablecoin_outflow_watch_are_not_green_without_krw_stability_and_regulated_revenue",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("q1_stablecoin_trading_57tn_krw", "q1_stablecoin_trading_42bn_usd", "kimchi_bond_ban_lifted_after_14_years", "krw_1347_to_1353_anchor", "stablecoin_capital_outflow_watch"),
        red_flag_fields=("stablecoin_policy_theme_only", "stablecoin_driven_capital_outflow", "fx_policy_without_actual_flow", "overseas_stock_outflow_watch"),
        price_data_source="FT FX-liquidity / stablecoin policy anchors",
        reported_price_anchor="Stablecoin trading 57T won / $42B; KRW 1,347 to 1,353/USD after kimchi bond relief",
        reported_return_anchor="BoK warns non-bank stablecoin issuance can create capital outflow / FX crisis response risk",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stablecoin_trading_q1_2025_krw_trn": 57.0, "stablecoin_trading_q1_2025_usd_bn": 42.0, "krw_strength_after_policy_per_usd": 1347.0, "krw_stabilization_level_per_usd": 1353.0, "kimchi_bond_ban_duration_years": 14.0, "capital_outflow_context_usd_bn": 19.0, "proposed_minimum_equity_for_won_stablecoin_issuers_krw_mn": 500.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_fx_relief_plus_4C_watch",
        rerating_result="policy_event_rerating",
        round_rerating_result="FX_liquidity_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_macro_relief_not_green",
        price_validation_status="fx_policy_anchor_not_company_ohlc",
        notes="Kimchi bond relief is Stage 2, but stablecoin outflow is a simultaneous FX 4C-watch.",
    ),
    Round254CaseCandidate(
        case_id="r11_loop11_us_investment_pledge_fx_outflow_watch",
        symbol="KRW/exporters/banks/FX_sensitive_basket",
        company_name="$350B U.S. investment pledge and FX bond cap",
        primary_archetype=E2RArchetype.FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW,
        secondary_archetypes=(E2RArchetype.FX_OUTFLOW_TRADE_DEAL_OVERLAY, E2RArchetype.STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO, E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE),
        case_type="failed_rerating",
        round_case_type="macro_4c_watch_policy_relief",
        stage1_date=date(2025, 12, 1),
        stage2_date=date(2025, 12, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 3),
        stage3_decision="tariff_relief_has_fx_outflow_watch_until_krw_reserves_and_company_margin_bridge_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_investment_pledge_350bn_usd", "annual_dollar_outflow_limit_20bn_usd", "fx_bond_cap_2026_5bn_usd", "retail_us_stock_holdings_160bn_usd", "krw_down_8pct_since_end_june"),
        red_flag_fields=("foreign_investment_pledge_outflow", "capital_outflow_pressure", "krw_depreciation_watch", "tariff_relief_without_fx_stability"),
        price_data_source="FT FX-bond / capital-outflow anchor",
        reported_price_anchor="FX bond cap $3.5B to $5B; KRW -8%; retail U.S. stock holdings $160B",
        reported_return_anchor="$350B U.S. investment pledge with $20B annual dollar outflow limit",
        mfe_1d=None,
        mae_1d=-8.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"us_investment_pledge_usd_bn": 350.0, "annual_dollar_outflow_limit_usd_bn": 20.0, "fx_bond_cap_2026_usd_bn": 5.0, "fx_bond_cap_2025_usd_bn": 3.5, "cap_increase_pct": 42.9, "retail_us_stock_net_buy_2025_usd_bn": 30.0, "retail_us_stock_holdings_usd_bn": 160.0, "krw_decline_since_end_june_pct": -8.0, "fx_reserves_context_usd_bn": 430.7},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="macro_4C_watch_policy_relief",
        rerating_result="thesis_break",
        round_rerating_result="tariff_relief_with_FX_outflow_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="macro_watch_not_green",
        price_validation_status="macro_anchor_not_equity_ohlc",
        notes="Tariff relief and FX outflow pressure coexist; company Green needs KRW stability and margin bridge.",
    ),
)


def round254_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND254_CASE_CANDIDATES:
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
                "Round254 R11 Loop-11 policy/geopolitical/disaster/event price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "policy" in field
                or "shock" in field
                or "inclusion" in field
                or "bond" in field
                or "hormuz" in field
                or "martial" in field
                or "stablecoin" in field
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
                if "rally" in field or "expectation" in field or "headline" in field or "theme" in field or "event" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "shock" in field
                or "crisis" in field
                or "break" in field
                or "outflow" in field
                or "depreciation" in field
                or "chokepoint" in field
                or "crash" in field
            ),
            must_have_fields=ROUND254_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND254_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "r11_default_stage3_bias_very_conservative",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_geopolitical_disaster_fx_or_index_headline_as_green",
                *ROUND254_GREEN_REQUIRED_FIELDS,
                *ROUND254_GREEN_FORBIDDEN_PATTERNS,
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
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.88 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round254_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND254_CASE_CANDIDATES:
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


def round254_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND254_SCORE_ADJUSTMENTS)


def round254_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND254_SHADOW_WEIGHT_ROWS)


def round254_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND254_DEEP_SUB_ARCHETYPES)


def round254_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round254_price_validation": "true"} for field in ROUND254_PRICE_VALIDATION_FIELDS)


def round254_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round254_label": label, "canonical_archetype": canonical} for label, canonical in ROUND254_REQUIRED_TARGET_ALIASES.items())


def round254_summary() -> dict[str, int | bool | str]:
    cases = ROUND254_CASE_CANDIDATES
    return {
        "source_round": ROUND254_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND254_ANALYST_ROUND_ID,
        "large_sector": ROUND254_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "policy_relief_count": sum(1 for case in cases if "policy_relief" in case.round_case_type),
        "target_archetype_count": len(ROUND254_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND254_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND254_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r11_default_stage3_bias": ROUND254_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round254_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND254_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND254_ANALYST_ROUND_ID,
        "large_sector": ROUND254_LARGE_SECTOR.value,
        "summary": round254_summary(),
        "target_aliases": dict(ROUND254_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND254_CASE_CANDIDATES},
        "green_required_fields": list(ROUND254_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND254_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND254_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND254_HARD_4C_GATES),
        "deep_sub_archetypes": round254_deep_sub_archetype_rows(),
        "shadow_weights": round254_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round254_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_policy_geopolitical_disaster_fx_index_energy_or_stablecoin_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_hormuz_iran_energy_shock_as_macro_hard_4c_reference",
        ],
    }


def render_round254_summary_markdown() -> str:
    summary = round254_summary()
    lines = [
        "# Round 254 R11 Loop 11 Policy Geopolitical Disaster Event Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- policy_relief_count: {summary['policy_relief_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND254_CASE_CANDIDATES:
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
            "- WGBI, short-selling normalization, and Commercial Act reform are Stage 2 market-structure or governance evidence, not company Green.",
            "- Martial law and AI dividend/tax shocks are policy-confidence 4C-watch cases.",
            "- Hormuz/Iran energy shock is the confirmed macro hard 4C reference for this pack.",
            "- FX/stablecoin and U.S. investment pledge cases can contain both relief and outflow risk.",
            "- Easy example: `policy headline + basket rally` is Stage 1/2; `policy + actual flow + company EPS/FCF bridge` is required before deeper Stage review.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round254_green_gate_review_markdown() -> str:
    lines = [
        "# Round 254 R11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND254_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND254_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `WGBI inclusion + actual bond inflow` can be Stage 2 market-structure evidence.",
            "- `WGBI + actual flow + lower funding cost + company EPS/FCF bridge` is the kind of bundle required before Stage 3 review.",
            "- `AI dividend/tax speech + KOSPI selloff` is 4C-watch, not a positive rerating input.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round254_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 254 R11 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND254_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND254_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND254_CASE_CANDIDATES:
        if case.stage4b_status in {"watch", "hard_4c"} or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round254_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 254 R11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND254_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round254_r11_loop11_reports(
    output_directory: str | Path = ROUND254_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND254_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND254_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round254_case_records(), cases_path),
        "audit": _write_json(round254_audit_payload(), audit_path),
        "summary": output / "round254_r11_loop11_price_validation_summary.md",
        "case_matrix": output / "round254_r11_loop11_case_matrix.csv",
        "target_aliases": output / "round254_r11_loop11_target_aliases.csv",
        "score_adjustments": output / "round254_r11_loop11_score_adjustments.csv",
        "shadow_weights": output / "round254_r11_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round254_r11_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round254_r11_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round254_r11_loop11_green_gate_review.md",
        "price_validation_plan": output / "round254_r11_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round254_r11_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round254_summary_markdown(), encoding="utf-8")
    _write_csv(round254_case_rows(), paths["case_matrix"])
    _write_csv(round254_target_alias_rows(), paths["target_aliases"])
    _write_csv(round254_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round254_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round254_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round254_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round254_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round254_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round254_stage4b_4c_review_markdown(), encoding="utf-8")
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
