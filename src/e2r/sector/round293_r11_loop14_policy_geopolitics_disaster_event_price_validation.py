"""Round-293 R11 Loop-14 policy/geopolitics/disaster/event pack.

This module converts ``docs/round/round_293.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: an oil/gas resource headline can move Korea Gas by 30%. It is
still not Stage 3-Green until drilling results, commerciality, CAPEX/IRR and a
cash-flow bridge are visible.
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


ROUND293_SOURCE_ROUND_PATH = "docs/round/round_293.md"
ROUND293_ANALYST_ROUND_ID = "round_221"
ROUND293_LARGE_SECTOR = "POLICY_GEOPOLITICS_DISASTER_EVENT"
ROUND293_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round293_r11_loop14_policy_geopolitics_disaster_event_price_validation"
ROUND293_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop14_round293.jsonl"
ROUND293_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round293_r11_loop14_policy_geopolitics_disaster_event_price_validation_audit.json"

ROUND293_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM": E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM.value,
    "GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C": E2RArchetype.GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C.value,
    "POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE": E2RArchetype.POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE.value,
    "TAX_POLICY_MARKET_CONFIDENCE_4C": E2RArchetype.TAX_POLICY_MARKET_CONFIDENCE_4C.value,
    "MARKET_ACCESS_REFORM_STAGE2": E2RArchetype.MARKET_ACCESS_REFORM_STAGE2.value,
    "MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE": E2RArchetype.MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE.value,
    "NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE": E2RArchetype.NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE.value,
    "GEOPOLITICAL_DEFENSE_ORDER_STAGE2": E2RArchetype.GEOPOLITICAL_DEFENSE_ORDER_STAGE2.value,
    "LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C": E2RArchetype.LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C.value,
}

ROUND293_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "policy_implementation_certainty_confirmed",
    "legal_regulatory_finality_confirmed",
    "company_eps_fcf_bridge_confirmed",
    "foreign_flow_or_market_access_flow_confirmed",
    "drilling_result_confirmed",
    "resource_economic_viability_confirmed",
    "CAPEX_IRR_confirmed",
    "sanction_export_control_exposure_cleared",
    "service_or_production_continuity_confirmed",
    "disaster_claims_budget_contract_confirmed",
    "defense_delivery_margin_cash_collection_confirmed",
    "tax_policy_consistency_confirmed",
    "price_path_after_evidence",
)

ROUND293_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "government_announcement_only",
    "presidential_headline_only",
    "resource_estimate_without_drilling",
    "policy_beneficiary_theme_only",
    "sanction_ignored_order_backlog",
    "tax_reform_without_market_consistency",
    "market_access_reform_without_foreign_flow",
    "disaster_recovery_without_budget_contract",
    "defense_order_without_delivery_margin",
    "labor_relief_without_production_continuity",
)

ROUND293_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "presidential_resource_announcement_plus_20_to_30pct",
    "defense_order_record_high_before_delivery_margin",
    "tax_relief_expectation_broad_rally",
    "market_access_reform_brokerage_prepricing",
    "disaster_recovery_theme_before_claims_budget_contract",
    "policy_beneficiary_basket_before_law_budget_execution",
)

ROUND293_HARD_4C_GATES: tuple[str, ...] = (
    "martial_law_or_constitutional_crisis",
    "foreign_sanctions_blocking_transactions_or_cooperation",
    "tax_policy_directly_damaging_investor_return_expectation",
    "resource_exploration_failure_after_speculative_rally",
    "nationwide_medical_service_disruption",
    "major_natural_disaster_claims_recovery_uncertainty",
    "prolonged_strike_threat_at_systemic_exporter",
    "export_control_or_shipbuilding_sanction_hits_supply_chain",
)

ROUND293_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "policy_amount_anchor",
    "liquidity_facility_anchor",
    "sanction_scope_anchor",
    "disaster_casualty_anchor",
    "labor_loss_estimate_anchor",
    "order_value_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round293ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round293ShadowWeightRow:
    archetype: E2RArchetype
    policy_implementation: int
    regulatory_finality: int
    geopolitical_counterparty_risk: int
    political_liquidity_risk: int
    tax_policy_consistency: int
    market_access_flow: int
    service_continuity: int
    disaster_cashflow_damage: int
    labor_systemic_risk: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "policy_implementation": _signed(self.policy_implementation),
            "regulatory_finality": _signed(self.regulatory_finality),
            "geopolitical_counterparty_risk": _signed(self.geopolitical_counterparty_risk),
            "political_liquidity_risk": _signed(self.political_liquidity_risk),
            "tax_policy_consistency": _signed(self.tax_policy_consistency),
            "market_access_flow": _signed(self.market_access_flow),
            "service_continuity": _signed(self.service_continuity),
            "disaster_cashflow_damage": _signed(self.disaster_cashflow_damage),
            "labor_systemic_risk": _signed(self.labor_systemic_risk),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round293DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round293CaseCandidate:
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
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    round_rerating_label: str
    stage_failure_type: str
    round_stage_failure_label: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND293_SCORE_ADJUSTMENTS: tuple[Round293ScoreAdjustment, ...] = (
    Round293ScoreAdjustment("policy_implementation_certainty", 5, "raise", "정책은 발표보다 법안, 예산, 시행, 기업 EPS bridge가 중요하다."),
    Round293ScoreAdjustment("legal_regulatory_finality", 5, "raise", "우선협상, 완화 발언, clarification은 final law/contract와 다르다."),
    Round293ScoreAdjustment("geopolitical_counterparty_risk", 5, "raise", "제재와 export-control은 수주잔고보다 먼저 거래 가능성을 흔든다."),
    Round293ScoreAdjustment("political_liquidity_risk", 5, "raise", "계엄·헌정 충격은 환율, 외국인 신뢰, 유동성 프리미엄을 재가격화한다."),
    Round293ScoreAdjustment("tax_policy_consistency", 5, "raise", "Value-Up narrative도 세제 일관성이 깨지면 시장 신뢰가 훼손된다."),
    Round293ScoreAdjustment("market_access_foreign_flow", 4, "raise", "시장접근성 개혁은 실제 외국인 flow와 증권사 수익으로 닫혀야 한다."),
    Round293ScoreAdjustment("service_continuity_under_policy", 4, "raise", "의료개혁은 서비스 capacity가 깨지면 수혜보다 disruption이 먼저다."),
    Round293ScoreAdjustment("disaster_damage_to_cashflow", 4, "raise", "재난은 복구테마보다 claims, budget, contract, margin을 먼저 본다."),
    Round293ScoreAdjustment("labor_continuity_systemic_risk", 5, "raise", "시스템 수출기업 파업은 단일 노사 이슈가 아니라 공급망 gate다."),
    Round293ScoreAdjustment("government_announcement_only", -5, "lower", "대통령 발표만으로 Green을 만들지 않는다."),
    Round293ScoreAdjustment("resource_estimate_without_drilling", -5, "lower", "매장량 가능성은 시추·경제성 전에는 event premium이다."),
    Round293ScoreAdjustment("sanction_ignored_order_backlog", -5, "lower", "제재가 거래를 막으면 order backlog가 방어막이 아니다."),
    Round293ScoreAdjustment("tax_reform_without_market_consistency", -5, "lower", "세제 충격은 shareholder return rerating을 막을 수 있다."),
    Round293ScoreAdjustment("market_access_reform_without_foreign_flow", -4, "lower", "제도개편만 있고 외국인 flow가 없으면 Stage 2에 머문다."),
    Round293ScoreAdjustment("defense_order_without_delivery_margin", -4, "lower", "방산 수주는 납품, margin, cash collection 전에는 Green이 아니다."),
)

ROUND293_SHADOW_WEIGHT_ROWS: tuple[Round293ShadowWeightRow, ...] = (
    Round293ShadowWeightRow(E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM, 3, 2, 0, 0, 0, 0, 0, 0, 0, -5, 5, 3, "Blue Whale is event premium until drilling, economics and CAPEX/IRR close."),
    Round293ShadowWeightRow(E2RArchetype.GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C, 2, 4, 5, 0, 0, 0, 0, 0, 0, -5, 5, 5, "China sanctions can override U.S.-ROK shipbuilding backlog narratives."),
    Round293ShadowWeightRow(E2RArchetype.POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE, 2, 4, 1, 5, 3, 1, 0, 0, 0, 0, 4, 5, "Martial-law shock is cross-sector political liquidity hard reference."),
    Round293ShadowWeightRow(E2RArchetype.TAX_POLICY_MARKET_CONFIDENCE_4C, 4, 5, 0, 4, 5, 2, 0, 0, 0, -5, 5, 4, "Tax uncertainty can break Korea Discount reform narrative."),
    Round293ShadowWeightRow(E2RArchetype.MARKET_ACCESS_REFORM_STAGE2, 4, 4, 0, 0, 3, 5, 0, 0, 0, -2, 3, 2, "Short-selling reform is Stage 2 until foreign flow and earnings confirm."),
    Round293ShadowWeightRow(E2RArchetype.MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE, 3, 4, 0, 0, 0, 0, 5, 0, 0, -5, 3, 5, "Medical reform needs service capacity before beneficiary scoring."),
    Round293ShadowWeightRow(E2RArchetype.NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE, 3, 3, 0, 0, 0, 0, 0, 5, 0, -5, 4, 5, "Disaster recovery trades need claims, budget, contracts and margin."),
    Round293ShadowWeightRow(E2RArchetype.GEOPOLITICAL_DEFENSE_ORDER_STAGE2, 4, 4, 3, 0, 0, 0, 0, 0, 0, -4, 5, 3, "Defense order is Stage 2 until delivery, margin, cash and dilution-adjusted EPS close."),
    Round293ShadowWeightRow(E2RArchetype.LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C, 3, 4, 1, 0, 0, 0, 2, 0, 5, -5, 4, 5, "Samsung strike risk is systemic export-chain gate."),
)

ROUND293_DEEP_SUB_ARCHETYPES: tuple[Round293DeepSubArchetype, ...] = (
    Round293DeepSubArchetype("정책 자원개발", E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM, ("Korea Gas", "Blue Whale", "14B boe", "20% success probability", "drilling economics")),
    Round293DeepSubArchetype("중국 제재", E2RArchetype.GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C, ("Hanwha Ocean", "China sanctions", "Philly Shipyard", "transaction ban", "shipbuilding cooperation")),
    Round293DeepSubArchetype("정치 유동성", E2RArchetype.POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE, ("martial law", "unlimited liquidity", "10T stock fund", "40T bond fund", "won near two-year low")),
    Round293DeepSubArchetype("세제 신뢰", E2RArchetype.TAX_POLICY_MARKET_CONFIDENCE_4C, ("capital-gains threshold", "transaction tax", "AI windfall tax", "KOSPI -3.9%", "KOSPI intraday -5%")),
    Round293DeepSubArchetype("시장접근성", E2RArchetype.MARKET_ACCESS_REFORM_STAGE2, ("short-selling normalization", "MSCI accessibility", "100% order fine", "foreign flow", "brokerage earnings")),
    Round293DeepSubArchetype("의료개혁", E2RArchetype.MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE, ("medical-school quota", "9000 trainee doctors", "surgery cancellations", "military doctors", "service capacity")),
    Round293DeepSubArchetype("자연재난", E2RArchetype.NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE, ("2025 wildfires", "28 deaths", "118265 acres", "30000 displaced", "recovery budget")),
    Round293DeepSubArchetype("방산 지정학 수주", E2RArchetype.GEOPOLITICAL_DEFENSE_ORDER_STAGE2, ("Hanwha Aerospace", "Romania K9", "$1B order", "backlog 5.1T to 30T", "dilution-adjusted EPS")),
    Round293DeepSubArchetype("노동정책 수출 리스크", E2RArchetype.LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C, ("Samsung strike", "emergency arbitration", "1T one-day loss", "100T prolonged disruption", "22.8% exports")),
)

ROUND293_CASE_CANDIDATES: tuple[Round293CaseCandidate, ...] = (
    Round293CaseCandidate(
        case_id="r11_loop14_kogas_blue_whale_resource_event_premium",
        symbol="036460/096770/117580/018670",
        company_name="Korea Gas / Blue Whale East Sea resource event basket",
        primary_archetype=E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT, E2RArchetype.ENERGY_SECURITY_POLICY_EVENT, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="price_moved_without_evidence",
        stage1_date=date(2024, 6, 3),
        stage2_date=date(2024, 6, 3),
        stage3_date=None,
        stage4b_date=date(2024, 6, 3),
        stage4c_date=None,
        stage3_decision="resource_discovery_headline_needs_drilling_result_economic_viability_CAPEX_IRR_and_cashflow_bridge",
        stage4b_status="4B-watch/resource-event-before-commerciality",
        hard_4c_confirmed=False,
        evidence_fields=("presidential_drilling_approval", "potential_resource_14bn_boe", "success_probability_20pct", "kogas_plus_30pct", "commercial_production_target_2035"),
        red_flag_fields=("resource_estimate_without_drilling", "presidential_headline_only", "economic_viability_unconfirmed", "CAPEX_IRR_unconfirmed"),
        price_data_source="Reuters / WSJ resource-discovery event anchors",
        reported_price_anchor="Korea Gas event price 38,700 KRW; KOGAS +30%; Daesung Energy +30%; SK Innovation +6%; SK Gas +7%",
        reported_return_anchor="Resource headline moved price before reserve confirmation, drilling result, CAPEX/IRR or production cashflow",
        event_mfe_pct=30.0,
        event_mae_pct=None,
        stage1_price_anchor=38700.0,
        stage2_price_anchor=38700.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=38700.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"korea_gas_event_mfe_pct": 30.0, "korea_gas_event_price_krw": 38700, "daesung_energy_event_mfe_pct": 30.0, "sk_innovation_event_mfe_pct": 6.0, "sk_gas_event_mfe_pct": 7.0, "potential_resource_boe_bn": 14.0, "project_cost_krw_bn_min": 500, "per_well_cost_krw_bn": 100, "success_probability_pct": 20, "commercial_production_target": 2035, "economic_viability_confirmed": False, "drilling_result_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_label="resource_discovery_policy_event_premium",
        stage_failure_type="false_yellow",
        round_stage_failure_label="policy_resource_headline_without_drilling_IRR",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Resource discovery headline is Stage 2/4B-watch until drilling, commerciality and cashflow close.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_hanwha_ocean_china_sanctions_4c_watch",
        symbol="042660",
        company_name="Hanwha Ocean / China sanctions on U.S.-linked units",
        primary_archetype=E2RArchetype.GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_RECONSTRUCTION, E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG, E2RArchetype.MACRO_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="geopolitical 4C-watch",
        stage1_date=date(2025, 10, 14),
        stage2_date=date(2025, 10, 22),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 10, 14),
        stage3_decision="foreign_sanctions_can_override_shipbuilding_order_theme_until_transaction_and_project_execution_risk_clears",
        stage4b_status="hard-4C-watch/geopolitical-sanctions",
        hard_4c_confirmed=True,
        evidence_fields=("china_sanctions_five_us_linked_units", "transaction_cooperation_ban", "hanwha_ocean_minus_5_8pct", "philly_shipyard_pledge_5bn_usd"),
        red_flag_fields=("foreign_sanctions_blocking_transactions_or_cooperation", "sanction_ignored_order_backlog", "counterparty_access_unconfirmed"),
        price_data_source="Reuters / AP China sanctions anchors",
        reported_price_anchor="Hanwha Ocean -5.8%; HD Hyundai Heavy -4.1%; five units sanctioned; $5B Philly Shipyard pledge context",
        reported_return_anchor="China sanctions hit shipbuilding geopolitics before order execution clarity",
        event_mfe_pct=None,
        event_mae_pct=-5.8,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hanwha_ocean_event_mae_pct": -5.8, "hd_hyundai_heavy_event_mae_pct": -4.1, "sanctioned_units_count": 5, "philly_shipyard_investment_pledge_usd_bn": 5, "korea_trade_envoy_requested_removal": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="geopolitical_sanctions_supply_chain_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="geopolitical_sanction_overrides_order_theme",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Sanction risk must remain visible to RedTeam before shipbuilding order rerating.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_martial_law_political_liquidity_shock",
        symbol="KOSPI/EWY/market_basket",
        company_name="Korea martial-law political liquidity shock",
        primary_archetype=E2RArchetype.POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK, E2RArchetype.POLITICAL_SYSTEM_SHOCK_KOREA, E2RArchetype.MACRO_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="political liquidity hard reference",
        stage1_date=date(2024, 12, 3),
        stage2_date=date(2024, 12, 4),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 4),
        stage3_decision="political_liquidity_shock_is_not_investable_green_it_is_cross_sector_hard_gate",
        stage4b_status="hard-4C/political-liquidity-shock",
        hard_4c_confirmed=True,
        evidence_fields=("martial_law_declaration", "unlimited_liquidity_pledge", "stock_stabilization_fund_10trn_krw", "bond_stabilization_fund_40trn_krw", "kospi_minus_1_4_to_nearly_2pct"),
        red_flag_fields=("martial_law_or_constitutional_crisis", "political_liquidity_risk", "foreign_capital_confidence_break"),
        price_data_source="Reuters / FT martial-law market-stabilization anchors",
        reported_price_anchor="KOSPI -1.4% to nearly -2%; won near two-year low; 10T KRW stock fund; 40T KRW bond fund",
        reported_return_anchor="Political shock repriced KOSPI/won before any company evidence",
        event_mfe_pct=None,
        event_mae_pct=-1.4,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_close_mae_pct_ft": -1.4, "kospi_session_context_reuters_pct": -2.0, "stock_stabilization_fund_krw_trn": 10, "bond_market_stabilization_fund_krw_trn": 40, "liquidity_commitment": "unlimited_liquidity", "won_context": "near_two_year_low"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="political_liquidity_shock_hard_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="political_legitimacy_and_liquidity_risk",
        price_validation_status="reported_index_fx_anchor_not_full_ohlc",
        notes="Martial-law shock is a political liquidity hard reference, not positive company evidence.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_tax_policy_market_confidence_4c",
        symbol="KOSPI/005930/000660/securities_basket",
        company_name="Korea stock tax policy and AI windfall-tax confidence shock",
        primary_archetype=E2RArchetype.TAX_POLICY_MARKET_CONFIDENCE_4C,
        secondary_archetypes=(E2RArchetype.TAX_POLICY_MARKET_SHOCK_OVERLAY, E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK, E2RArchetype.POLICY_CONFIDENCE_EVENT_PREMIUM),
        case_type="4c_thesis_break",
        round_case_type="tax policy 4C-watch plus relief",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2025, 9, 11),
        stage3_date=None,
        stage4b_date=date(2026, 5, 12),
        stage4c_date=date(2026, 5, 12),
        stage3_decision="valueup_reform_narrative_breaks_if_tax_policy_damages_investor_return_expectation",
        stage4b_status="4C-watch/tax-policy-market-confidence",
        hard_4c_confirmed=False,
        evidence_fields=("kospi_tax_proposal_minus_3_9pct", "capital_gains_threshold_5bn_to_1bn", "transaction_tax_0_15_to_0_20pct", "ai_tax_intraday_minus_5pct"),
        red_flag_fields=("tax_policy_directly_damaging_investor_return_expectation", "tax_reform_without_market_consistency", "AI_windfall_tax_surprise"),
        price_data_source="MarketWatch / Reuters / Barron's tax-policy anchors",
        reported_price_anchor="KOSPI -3.9% on tax package; AI tax comment KOSPI -5% intraday and -2.3% close",
        reported_return_anchor="Tax policy can break Value-Up and AI rerating confidence even when later clarified",
        event_mfe_pct=None,
        event_mae_pct=-5.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_tax_proposal_mae_pct": -3.9, "capital_gains_threshold_before_krw_bn": 5, "capital_gains_threshold_proposed_krw_bn": 1, "transaction_tax_before_pct": 0.15, "transaction_tax_proposed_pct": 0.20, "ai_tax_intraday_mae_pct": -5.0, "ai_tax_close_mae_pct": -2.3, "ai_tax_comment_later_clarified_as_personal_view": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch_then_policy_relief",
        rerating_result="thesis_break",
        round_rerating_label="tax_policy_market_confidence_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="reform_narrative_breaks_if_tax_policy_hits_equity_returns",
        price_validation_status="reported_market_anchor_not_full_ohlc",
        notes="Tax policy consistency is a Green prerequisite for value-up or AI rerating narratives.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_short_selling_market_access_reform_stage2",
        symbol="securities_basket/KRX_market_reference",
        company_name="Short-selling normalization and market-access reform",
        primary_archetype=E2RArchetype.MARKET_ACCESS_REFORM_STAGE2,
        secondary_archetypes=(E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM, E2RArchetype.SHORT_SELLING_NORMALIZATION, E2RArchetype.MARKET_STRUCTURE_REFORM),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_stage2",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 7, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="market_access_reform_is_stage2_until_foreign_flow_trading_value_brokerage_earnings_and_index_upgrade_path_confirm",
        stage4b_status="Stage2/market-access-reform",
        hard_4c_confirmed=False,
        evidence_fields=("short_selling_ban_lifted_after_five_years", "MSCI_accessibility_improved", "serious_short_sale_violation_fine_100pct", "one_strike_out_policy"),
        red_flag_fields=("market_access_reform_without_foreign_flow", "FX_market_access_hurdle", "offshore_market_absent"),
        price_data_source="Reuters MSCI accessibility and unfair-trading reform anchors",
        reported_price_anchor="Direct price anchor unavailable; MSCI short-selling accessibility and 100% short-sale order fine mapped",
        reported_return_anchor="Market access reform is Stage 2 until foreign flow and brokerage earnings confirm",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"short_selling_ban_lifted_after_years": 5, "msci_short_selling_accessibility_rating_change": "improvements_needed_to_no_major_issues_improvements_possible", "serious_short_sale_violation_fine_pct_of_order": 100, "remaining_hurdles": ["FX market access", "lack of offshore market", "onshore limitations"]},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_stage2",
        rerating_result="policy_event_rerating",
        round_rerating_label="market_access_reform_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="accessibility_reform_not_foreign_flow_brokerage_profit_green",
        price_validation_status="policy_anchor_not_full_ohlc",
        notes="Short-selling reform is Stage 2; Green needs foreign flow and earnings bridge.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_medical_reform_doctors_strike_service_disruption",
        symbol="healthcare_service_basket/telemedicine_readthrough",
        company_name="Medical-school quota reform and doctors strike service disruption",
        primary_archetype=E2RArchetype.MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE,
        secondary_archetypes=(E2RArchetype.BIOTECH_REGULATORY, E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT),
        case_type="4c_thesis_break",
        round_case_type="medical reform service-disruption reference",
        stage1_date=date(2024, 2, 20),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 2, 28),
        stage3_decision="medical_reform_policy_goal_is_not_green_if_service_capacity_and_implementation_stability_break",
        stage4b_status="hard-4C/service-disruption-reference",
        hard_4c_confirmed=True,
        evidence_fields=("trainee_doctors_walkout_9000", "surgery_cancellations", "military_doctors_deployed", "community_doctors_deployed"),
        red_flag_fields=("nationwide_medical_service_disruption", "service_capacity_break", "license_suspension_conflict"),
        price_data_source="Reuters / Guardian doctors strike anchors",
        reported_price_anchor="9,000 trainee doctors walked out; service disruption and surgery cancellations reported",
        reported_return_anchor="Policy objective cannot become investable Green while hospital operations are disrupted",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"trainee_doctors_walkout_count_reuters": 9000, "reported_doctors_in_teaching_hospitals_context": 12000, "teaching_hospitals_context_count": 100, "service_disruptions": ["surgery_cancellations", "hospital_service_delay"], "government_response": ["military_doctors", "community_doctors", "license_suspension_warning"]},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="medical_reform_service_disruption_4C_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="policy_goal_not_green_if_service_capacity_breaks",
        price_validation_status="service_disruption_reference_not_full_ohlc",
        notes="Healthcare reform must preserve service capacity before any beneficiary evidence can promote.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_2025_wildfire_disaster_recovery_reference",
        symbol="insurers/construction/materials_basket",
        company_name="2025 South Korea wildfires disaster recovery reference",
        primary_archetype=E2RArchetype.NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE,
        secondary_archetypes=(E2RArchetype.DISASTER_REBUILD_EVENT, E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE, E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE),
        case_type="4c_thesis_break",
        round_case_type="natural-disaster recovery reference",
        stage1_date=date(2025, 3, 21),
        stage2_date=date(2025, 3, 28),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 28),
        stage3_decision="disaster_recovery_readthrough_needs_claims_budget_reconstruction_orders_material_margin_and_cashflow",
        stage4b_status="hard-4C/disaster-reference",
        hard_4c_confirmed=True,
        evidence_fields=("wildfire_deaths_28", "injuries_37", "acres_burned_118265", "displaced_people_30000", "disaster_zone_designation"),
        red_flag_fields=("major_natural_disaster_claims_recovery_uncertainty", "disaster_recovery_without_budget_contract", "loss_assessment_unconfirmed"),
        price_data_source="Reuters / AP wildfire-disaster anchors",
        reported_price_anchor="28 deaths, 37 injuries, 118,265 acres burned, more than 30,000 displaced",
        reported_return_anchor="Disaster recovery theme requires claims, government budget, actual contracts and margin",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"reuters_active_phase_deaths": 16, "ap_later_deaths": 28, "ap_injuries": 37, "ap_acres_burned": 118265, "ap_displaced_people": 30000, "reuters_hectares_destroyed_active_phase_min": 15000, "disaster_zone_designation": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="disaster_reference",
        rerating_result="thesis_break",
        round_rerating_label="natural_disaster_recovery_policy_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="disaster_damage_not_reconstruction_margin_green",
        price_validation_status="disaster_reference_not_full_ohlc",
        notes="Disaster read-through is not Green until losses, budget, contracts and margins are visible.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_hanwha_aerospace_romania_k9_geopolitical_order",
        symbol="012450",
        company_name="Hanwha Aerospace Romania K9 geopolitical defense order",
        primary_archetype=E2RArchetype.GEOPOLITICAL_DEFENSE_ORDER_STAGE2,
        secondary_archetypes=(E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.DILUTION_AFTER_RERATING_4B),
        case_type="success_candidate",
        round_case_type="structural_success_candidate plus 4B/dilution watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 7, 9),
        stage3_date=None,
        stage4b_date=date(2025, 3, 1),
        stage4c_date=None,
        stage3_decision="defense_order_backlog_needs_delivery_margin_cash_collection_local_production_and_dilution_adjusted_EPS",
        stage4b_status="4B-watch/defense-order-premium-before-delivery-margin",
        hard_4c_confirmed=False,
        evidence_fields=("romania_k9_order_1bn_usd", "k9_howitzers_54", "k10_resupply_vehicles_36", "contract_end_2029_07", "backlog_5_1trn_to_30trn_krw"),
        red_flag_fields=("defense_order_without_delivery_margin", "dilution_adjusted_EPS_unconfirmed", "delivery_margin_cash_collection_unconfirmed"),
        price_data_source="Reuters Romania K9 order and later dilution-watch anchors",
        reported_price_anchor="$1B Romania order; shares +5% to record high; backlog from 5.1T to 30T KRW; later 3.6T KRW share-sale watch",
        reported_return_anchor="Defense order is Stage 2 until delivery, margin, cash collection and dilution-adjusted EPS confirm",
        event_mfe_pct=5.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"order_value_usd_bn": 1.0, "k9_howitzers": 54, "k10_resupply_vehicles": 36, "contract_end": "2029-07", "backlog_end_2021_krw_trn": 5.1, "backlog_march_2024_krw_trn": 30, "backlog_growth_multiple": 5.88, "event_mfe_pct": 5.0, "later_share_sale_krw_trn": 3.6, "later_dilution_event_mae_pct": -13},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_but_4B_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="geopolitical_defense_order_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="order_backlog_not_delivery_margin_dilution_adjusted_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Defense order is strong Stage 2, but Green requires delivery, margin, cash and dilution-adjusted EPS.",
    ),
    Round293CaseCandidate(
        case_id="r11_loop14_samsung_strike_labor_policy_systemic_export_risk",
        symbol="005930/000660/KOSPI_export_chain",
        company_name="Samsung strike risk and government emergency arbitration",
        primary_archetype=E2RArchetype.LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C,
        secondary_archetypes=(E2RArchetype.SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION, E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C, E2RArchetype.MEMORY_HBM_CAPACITY),
        case_type="4c_thesis_break",
        round_case_type="labor-policy systemic export 4C-watch",
        stage1_date=date(2026, 5, 17),
        stage2_date=date(2026, 5, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 17),
        stage3_decision="labor_resolution_is_not_green_until_production_continuity_yield_delivery_customer_allocation_and_settlement_durability_confirm",
        stage4b_status="hard-4C-watch/systemic-export-labor-risk",
        hard_4c_confirmed=True,
        evidence_fields=("samsung_union_18_day_strike_threat", "emergency_arbitration_possible", "one_day_halt_loss_1trn_krw", "prolonged_disruption_100trn_krw", "samsung_export_share_22_8pct"),
        red_flag_fields=("prolonged_strike_threat_at_systemic_exporter", "labor_relief_without_production_continuity", "customer_allocation_unconfirmed"),
        price_data_source="Reuters Samsung strike / government emergency arbitration anchor",
        reported_price_anchor="18-day strike threat; emergency arbitration possible; 1-day halt loss up to 1T KRW; prolonged disruption up to 100T KRW",
        reported_return_anchor="Samsung labor dispute is national export-chain risk until production continuity clears",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"strike_threat_days": 18, "emergency_arbitration_possible": True, "industrial_action_bar_period_days": 30, "single_day_halt_loss_krw_trn_max": 1, "prolonged_disruption_damage_krw_trn_max": 100, "samsung_export_share_pct": 22.8, "samsung_employee_count": 120000},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="labor_policy_systemic_export_risk_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="labor_supply_continuity_is_semiconductor_export_gate",
        price_validation_status="labor_policy_anchor_not_full_ohlc",
        notes="Systemic exporter labor risk blocks Green until production continuity and customer allocation clear.",
    ),
)


def round293_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND293_CASE_CANDIDATES:
        stage3_terms = ("eps", "fcf", "flow", "margin", "cash", "drilling", "economic", "continuity", "contract", "delivery", "budget", "claims", "tax")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND293_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round293 R11 Loop-14 policy/geopolitics/disaster/event price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND293_GREEN_REQUIRED_FIELDS) if any(token.lower() in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("rally", "premium", "headline", "order", "relief", "theme", "event"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("shock", "sanction", "crisis", "disruption", "strike", "tax", "disaster", "loss", "service", "foreign"))),
            must_have_fields=ROUND293_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND293_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_political_liquidity_and_disaster_references",
                "do_not_use_round293_cases_as_candidate_generation_input",
                "do_not_treat_policy_geopolitical_disaster_tax_resource_or_labor_headline_as_green",
                *ROUND293_GREEN_REQUIRED_FIELDS,
                *ROUND293_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.86 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round293_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
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
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "stage1_price_anchor": _float_text(candidate.stage1_price_anchor),
            "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
            "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
            "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
            "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": candidate.score_price_alignment,
            "round_alignment_label": candidate.round_alignment_label,
            "rerating_result": candidate.rerating_result,
            "round_rerating_label": candidate.round_rerating_label,
            "stage_failure_type": candidate.stage_failure_type,
            "round_stage_failure_label": candidate.round_stage_failure_label,
            "price_validation_status": candidate.price_validation_status,
            "evidence_fields": "|".join(candidate.evidence_fields),
            "red_flag_fields": "|".join(candidate.red_flag_fields),
            "notes": candidate.notes,
        }
        for candidate in ROUND293_CASE_CANDIDATES
    )


def round293_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND293_SCORE_ADJUSTMENTS)


def round293_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND293_SHADOW_WEIGHT_ROWS)


def round293_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND293_DEEP_SUB_ARCHETYPES)


def round293_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round293_price_validation": "true"} for field in ROUND293_PRICE_VALIDATION_FIELDS)


def round293_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round293_label": label, "canonical_archetype": canonical} for label, canonical in ROUND293_REQUIRED_TARGET_ALIASES.items())


def round293_summary() -> dict[str, int | bool | str]:
    cases = ROUND293_CASE_CANDIDATES
    return {
        "source_round": ROUND293_SOURCE_ROUND_PATH,
        "round_id": ROUND293_ANALYST_ROUND_ID,
        "large_sector": ROUND293_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "target_archetype_count": len(ROUND293_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND293_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND293_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round293_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND293_SOURCE_ROUND_PATH,
        "round_id": ROUND293_ANALYST_ROUND_ID,
        "large_sector": ROUND293_LARGE_SECTOR,
        "summary": round293_summary(),
        "target_aliases": dict(ROUND293_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND293_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND293_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND293_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND293_HARD_4C_GATES),
        "score_adjustments": list(round293_score_adjustment_rows()),
        "shadow_weights": list(round293_shadow_weight_rows()),
        "deep_sub_archetypes": list(round293_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND293_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round293_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_policy_geopolitical_disaster_tax_resource_or_labor_headline_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round293_summary_markdown() -> str:
    summary = round293_summary()
    lines = [
        "# Round 293 R11 Loop 14 Policy Geopolitics Disaster Event Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND293_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.round_alignment_label,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Policy/resource headlines and disaster recovery themes are not Green until cash-flow evidence closes.",
            "- Sanctions, martial law, medical disruption, wildfire damage and systemic labor risk are RedTeam gates.",
            "- Market-access reform and defense export orders can be Stage 2, but Green needs flow, delivery, margin and cash collection.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round293_green_gate_review_markdown() -> str:
    lines = [
        "# Round 293 R11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R11 Stage 3-Green is not `presidential resource headline`, `sanction relief request`, `tax clarification`, `market-access reform`, `disaster recovery theme`, or `defense order headline`. It requires implementation, legal finality, EPS/FCF bridge, production/service continuity, claims/budget/contracts, and price-after-evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND293_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND293_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND293_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `14B boe resource possibility` is not Green until drilling and economics prove it.",
            "- `short-selling reform` is Stage 2 until foreign flow and brokerage earnings appear.",
            "- `wildfire recovery theme` is not Green until claims, budget, contracts and margins are visible.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round293_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 293 R11 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND293_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND293_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND293_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round293_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 293 R11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, drilling result, sanction removal, tax law, foreign flow, claims, contract margin, labor continuity or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND293_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND293_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round293_r11_loop14_reports(
    output_directory: str | Path = ROUND293_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND293_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND293_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round293_case_records(), cases_path),
        "audit": _write_json(round293_audit_payload(), audit_path),
        "summary": output / "round293_r11_loop14_price_validation_summary.md",
        "case_matrix": output / "round293_r11_loop14_case_matrix.csv",
        "target_aliases": output / "round293_r11_loop14_target_aliases.csv",
        "score_adjustments": output / "round293_r11_loop14_score_adjustments.csv",
        "shadow_weights": output / "round293_r11_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round293_r11_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round293_r11_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round293_r11_loop14_green_gate_review.md",
        "price_validation_plan": output / "round293_r11_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round293_r11_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round293_summary_markdown(), encoding="utf-8")
    _write_csv(round293_case_rows(), paths["case_matrix"])
    _write_csv(round293_target_alias_rows(), paths["target_aliases"])
    _write_csv(round293_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round293_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round293_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round293_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round293_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round293_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round293_stage4b_4c_review_markdown(), encoding="utf-8")
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
