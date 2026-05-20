"""Round-280 R11 Loop-13 policy/geopolitical/disaster/event pack.

This module converts ``docs/round/round_280.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: a tariff cut from 25% to 15% is relief, but not Stage 3-Green by
itself. Green needs the company-level margin, price pass-through, local
production, FX bridge, and FCF path to close.
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


ROUND280_SOURCE_ROUND_PATH = "docs/round/round_280.md"
ROUND280_ANALYST_ROUND_ID = "round_208"
ROUND280_LARGE_SECTOR = "POLICY_GEOPOLITICS_DISASTER_EVENT"
ROUND280_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation"
ROUND280_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop13_round280.jsonl"
ROUND280_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round280_r11_loop13_policy_geopolitical_disaster_event_price_validation_audit.json"

ROUND280_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE": E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE.value,
    "MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C": E2RArchetype.MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C.value,
    "AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT": E2RArchetype.AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT.value,
    "SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION": E2RArchetype.SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION.value,
    "RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C": E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C.value,
    "US_KOREA_TARIFF_POLICY_4C_WATCH": E2RArchetype.US_KOREA_TARIFF_POLICY_4C_WATCH.value,
    "CHINA_FAB_EXPORT_LICENSE_RELIEF": E2RArchetype.CHINA_FAB_EXPORT_LICENSE_RELIEF.value,
    "CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE": E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE.value,
}

ROUND280_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "policy_law_budget_execution_confirmed",
    "company_eps_fcf_bridge_confirmed",
    "gross_margin_tariff_bridge_confirmed",
    "price_pass_through_confirmed",
    "local_production_economics_confirmed",
    "fx_energy_hedge_confirmed",
    "actual_supply_chain_license_confirmed",
    "critical_material_inventory_confirmed",
    "labor_production_continuity_confirmed",
    "disaster_loss_assessment_confirmed",
    "rebuild_contract_margin_confirmed",
    "sovereign_credit_fx_stability_confirmed",
    "price_path_after_evidence",
)

ROUND280_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_headline_only",
    "relief_package_without_execution",
    "tariff_cut_without_margin_bridge",
    "rare_earth_truce_without_actual_license",
    "strike_risk_unresolved",
    "AI_tax_or_bonus_comment_without_legislation",
    "disaster_rebuild_story_without_loss_assessment",
    "geopolitical_risk_ignored",
    "annual_license_treated_as_multiyear_visibility",
)

ROUND280_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "AI_chip_rally_then_redistribution_tax_comment_selloff",
    "policy_support_or_tariff_relief_headline_before_margin_bridge",
    "rare_earth_truce_headline_before_actual_license",
    "disaster_rebuild_theme_before_loss_assessment",
    "government_arbitration_relief_before_production_continuity",
    "foreign_positioning_crowded_with_fx_volatility",
)

ROUND280_HARD_4C_GATES: tuple[str, ...] = (
    "martial_law_or_political_crisis",
    "index_circuit_breaker_or_record_market_drawdown",
    "fx_disorderly_move_or_won_1500_breach",
    "middle_east_oil_chokepoint_shock",
    "rare_earth_license_denial",
    "semiconductor_fab_tool_license_denial",
    "systemic_strike_halting_production",
    "tariff_shock_directly_cutting_OP_margin",
    "climate_disaster_large_insured_or_uninsured_losses",
)

ROUND280_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "index_anchor",
    "fx_anchor",
    "policy_amount_anchor",
    "supply_chain_license_anchor",
    "labor_anchor",
    "disaster_loss_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round280ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round280ShadowWeightRow:
    archetype: E2RArchetype
    political_risk_premium: int
    fx_energy_sensitivity: int
    supply_chain_license_visibility: int
    tariff_pass_through: int
    policy_to_eps_bridge: int
    labor_continuity: int
    critical_material_inventory: int
    disaster_loss_exposure: int
    government_relief_execution: int
    sovereign_credit_stability: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "political_risk_premium": _signed(self.political_risk_premium),
            "fx_energy_sensitivity": _signed(self.fx_energy_sensitivity),
            "supply_chain_license_visibility": _signed(self.supply_chain_license_visibility),
            "tariff_pass_through": _signed(self.tariff_pass_through),
            "policy_to_eps_bridge": _signed(self.policy_to_eps_bridge),
            "labor_continuity": _signed(self.labor_continuity),
            "critical_material_inventory": _signed(self.critical_material_inventory),
            "disaster_loss_exposure": _signed(self.disaster_loss_exposure),
            "government_relief_execution": _signed(self.government_relief_execution),
            "sovereign_credit_stability": _signed(self.sovereign_credit_stability),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round280DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round280CaseCandidate:
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


ROUND280_SCORE_ADJUSTMENTS: tuple[Round280ScoreAdjustment, ...] = (
    Round280ScoreAdjustment("political_risk_premium", 5, "raise", "계엄 같은 정치 충격은 KOSPI와 원화를 즉시 재가격화한다."),
    Round280ScoreAdjustment("FX_energy_sensitivity", 5, "raise", "중동 에너지 shock는 수입물가, 원화, 자동차, 반도체, 항공을 동시에 흔든다."),
    Round280ScoreAdjustment("supply_chain_license_visibility", 5, "raise", "희토류와 중국 fab 장비는 실제 license가 생산의 전제다."),
    Round280ScoreAdjustment("tariff_pass_through", 5, "raise", "관세 relief보다 기업별 gross margin과 가격전가가 더 중요하다."),
    Round280ScoreAdjustment("policy_to_EPS_bridge", 5, "raise", "정책은 법안/예산/시행과 회사 EPS bridge로 닫혀야 한다."),
    Round280ScoreAdjustment("labor_continuity", 5, "raise", "삼성 파업처럼 노사 이슈가 수출·공급망 이슈로 확장될 수 있다."),
    Round280ScoreAdjustment("critical_material_inventory", 5, "raise", "희토류는 headline보다 재고와 대체조달이 핵심이다."),
    Round280ScoreAdjustment("disaster_loss_exposure", 5, "raise", "재난은 복구수혜보다 피해비용과 보험손해율을 먼저 봐야 한다."),
    Round280ScoreAdjustment("government_relief_actual_execution", 4, "raise", "지원책은 실제 집행과 기업별 수혜 확인 후에만 올라간다."),
    Round280ScoreAdjustment("sovereign_credit_stability", 4, "raise", "정치/FX 충격 후 sovereign credibility 안정이 필요하다."),
    Round280ScoreAdjustment("policy_headline_only", -5, "lower", "정책 발언만으로 Green을 만들지 않는다."),
    Round280ScoreAdjustment("tariff_cut_without_margin_bridge", -5, "lower", "관세율 인하는 margin bridge 없이는 relief에 그친다."),
    Round280ScoreAdjustment("rare_earth_truce_without_actual_license", -5, "lower", "희토류 완화 headline은 실제 license 전에는 부족하다."),
    Round280ScoreAdjustment("strike_risk_unresolved", -5, "lower", "파업 risk가 열려 있으면 생산연속성이 깨진다."),
    Round280ScoreAdjustment("disaster_rebuild_story_without_loss_assessment", -5, "lower", "재난 복구 테마는 피해액과 실제 복구계약 전까지 제한한다."),
)

ROUND280_SHADOW_WEIGHT_ROWS: tuple[Round280ShadowWeightRow, ...] = (
    Round280ShadowWeightRow(E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE, 5, 4, 1, 1, 3, 2, 1, 2, 5, 5, 0, 4, 5, "Martial law shows political shock can reprice KOSPI/won immediately."),
    Round280ShadowWeightRow(E2RArchetype.MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C, 3, 5, 3, 4, 3, 2, 4, 3, 4, 5, 0, 5, 5, "Iran shock confirms energy/FX macro hard gate for Korea."),
    Round280ShadowWeightRow(E2RArchetype.AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT, 4, 2, 1, 1, 5, 3, 1, 0, 4, 4, -4, 5, 4, "AI bonus comment is policy event; legislation and EPS bridge required."),
    Round280ShadowWeightRow(E2RArchetype.SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION, 3, 2, 3, 1, 3, 5, 3, 0, 5, 4, 0, 5, 5, "Samsung strike risk affects exports, suppliers, index and chip supply."),
    Round280ShadowWeightRow(E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C, 2, 2, 5, 3, 3, 1, 5, 0, 3, 4, 0, 5, 5, "China rare-earth controls require actual licences, inventory and alternative sourcing."),
    Round280ShadowWeightRow(E2RArchetype.US_KOREA_TARIFF_POLICY_4C_WATCH, 2, 3, 2, 5, 5, 1, 1, 0, 4, 4, -5, 5, 4, "Tariff cut is not Green without gross margin and pass-through."),
    Round280ShadowWeightRow(E2RArchetype.CHINA_FAB_EXPORT_LICENSE_RELIEF, 1, 1, 5, 1, 4, 1, 3, 0, 4, 3, -4, 4, 4, "Annual fab-tool licence is relief but not multiyear visibility."),
    Round280ShadowWeightRow(E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE, 1, 2, 1, 1, 2, 1, 2, 5, 5, 4, -5, 4, 5, "Wildfire disaster shows loss exposure before rebuild-beneficiary scoring."),
)

ROUND280_DEEP_SUB_ARCHETYPES: tuple[Round280DeepSubArchetype, ...] = (
    Round280DeepSubArchetype("정치 충격", E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE, ("martial law", "KOSPI", "won", "10T stabilisation fund", "Korea discount")),
    Round280DeepSubArchetype("중동 전쟁·에너지", E2RArchetype.MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C, ("Iran conflict", "KOSPI -12.06%", "won 1505.8", "Middle East oil purchase share", "Samsung Hyundai Korean Air selloff")),
    Round280DeepSubArchetype("AI 초과세수·분배", E2RArchetype.AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT, ("AI bonus", "citizen dividend", "Samsung -3.5%", "SK Hynix -1.4%", "excess tax revenue")),
    Round280DeepSubArchetype("삼성 파업·공급망", E2RArchetype.SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION, ("Samsung strike", "45,000 workers", "emergency arbitration", "1T won one-day loss", "22.8% exports")),
    Round280DeepSubArchetype("희토류·전략광물", E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C, ("rare-earth export controls", "yttrium", "dysprosium", "terbium", "defence users denied", "advanced semiconductor case-by-case")),
    Round280DeepSubArchetype("한미 관세", E2RArchetype.US_KOREA_TARIFF_POLICY_4C_WATCH, ("15% auto tariff", "Hyundai -4.5%", "Kia -6.6%", "FTA advantage lost", "semiconductor pharma cap")),
    Round280DeepSubArchetype("중국 fab 장비", E2RArchetype.CHINA_FAB_EXPORT_LICENSE_RELIEF, ("Samsung China fab", "SK Hynix China fab", "annual 2026 licence", "validated end user expiry", "tool access")),
    Round280DeepSubArchetype("재난", E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE, ("2025 wildfires", "32 deaths", "104000 hectares", "5000 buildings", "climate change twice as likely")),
)

ROUND280_CASE_CANDIDATES: tuple[Round280CaseCandidate, ...] = (
    Round280CaseCandidate(
        case_id="r11_loop13_martial_law_korea_discount_political_shock",
        symbol="KOSPI/KRW/005930/000660",
        company_name="Korea political shock / martial law reference",
        primary_archetype=E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE,
        secondary_archetypes=(E2RArchetype.POLITICAL_SYSTEM_SHOCK_KOREA, E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK, E2RArchetype.MACRO_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="4C-thesis-break-reference",
        stage1_date=date(2024, 12, 3),
        stage2_date=date(2024, 12, 4),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 4),
        stage3_decision="political_shock_is_sovereign_credibility_and_korea_discount_hard_gate_not_company_green",
        stage4b_status="hard-4C/political-risk-premium",
        hard_4c_confirmed=True,
        evidence_fields=("martial_law_duration_6h", "kospi_minus_1_4pct", "won_two_year_low", "10trn_stabilisation_fund", "unlimited_liquidity_commitment"),
        red_flag_fields=("martial_law_or_political_crisis", "political_risk_premium", "sovereign_credit_stability_unconfirmed"),
        price_data_source="Reuters martial-law political-shock anchors",
        reported_price_anchor="KOSPI -1.4%, won near two-year low, 10T KRW stabilisation fund prepared",
        reported_return_anchor="Political shock immediately repriced KOSPI/won risk premium",
        event_mfe_pct=None,
        event_mae_pct=-1.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_close_mae_pct": -1.4, "kospi_intraday_context_pct": -2.0, "kospi_ytd_loss_context_pct": -7.0, "won_context": "near_two_year_low", "won_ytd_decline_context_pct": -9.0, "stock_market_stabilisation_fund_krw_trn": 10.0, "liquidity_commitment": "unlimited_liquidity_if_needed", "martial_law_duration_hours": 6},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="political_risk_premium_hard_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="Korea_discount_political_shock",
        price_validation_status="reported_index_fx_anchor_not_full_ohlc",
        notes="Political shock is a Korea-discount hard reference, not positive company evidence.",
    ),
    Round280CaseCandidate(
        case_id="r11_loop13_iran_middle_east_energy_fx_macro_hard_4c",
        symbol="KOSPI/KRW/005930/000660/005380/003490",
        company_name="Iran / Middle East energy and FX shock",
        primary_archetype=E2RArchetype.MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C, E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C, E2RArchetype.MACRO_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="macro hard 4C",
        stage1_date=date(2026, 2, 28),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 4),
        stage3_decision="middle_east_oil_fx_shock_is_macro_hard_4c_for_korea",
        stage4b_status="hard-4C/energy-FX-index-deleveraging",
        hard_4c_confirmed=True,
        evidence_fields=("kospi_minus_12_06pct", "won_1505_8_per_usd", "market_cap_wipeout_817_6tn_krw", "middle_east_oil_share_70pct", "large_cap_selloff"),
        red_flag_fields=("middle_east_oil_chokepoint_shock", "fx_disorderly_move_or_won_1500_breach", "index_circuit_breaker_or_record_market_drawdown"),
        price_data_source="Reuters Iran conflict macro-market anchors",
        reported_price_anchor="KOSPI -12.06%, won 1,505.8/USD, two-day market cap wipeout 817.6T KRW",
        reported_return_anchor="Samsung -11.7%, SK Hynix -9.6%, Hyundai -15.8%, Korean Air -7.9%",
        event_mfe_pct=None,
        event_mae_pct=-12.06,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=5093.54,
        extra_price_metrics={"kospi_close": 5093.54, "kospi_close_mae_pct": -12.06, "kospi_intraday_mae_pct": -12.65, "kospi_previous_day_mae_pct": -7.24, "two_day_market_cap_wipeout_krw_trn": 817.6, "two_day_market_cap_wipeout_usd_bn": 553.82, "won_intraday_low_per_usd": 1505.8, "won_close_per_usd": 1485.7, "won_close_decline_pct": -3.1, "middle_east_oil_purchase_share_pct": 70, "samsung_event_mae_pct": -11.7, "sk_hynix_event_mae_pct": -9.6, "hyundai_motor_event_mae_pct": -15.8, "korean_air_event_mae_pct": -7.9},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="middle_east_energy_fx_macro_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="oil_FX_index_deleveraging",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Energy and FX shock is macro hard 4C; company positives must be rechecked after stabilization.",
    ),
    Round280CaseCandidate(
        case_id="r11_loop13_ai_bonus_fiscal_redistribution_event",
        symbol="005930/000660/KOSPI",
        company_name="AI windfall / citizen dividend policy discussion",
        primary_archetype=E2RArchetype.AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT,
        secondary_archetypes=(E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK, E2RArchetype.AI_WINDFALL_TAX_POLICY_SHOCK),
        case_type="event_premium",
        round_case_type="event_premium + 4B-watch",
        stage1_date=date(2026, 5, 12),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2026, 5, 12),
        stage4c_date=None,
        stage3_decision="ai_bonus_comment_is_policy_risk_watch_until_legislation_and_company_tax_exposure_are_clear",
        stage4b_status="4B-watch/AI-policy-confidence-selloff",
        hard_4c_confirmed=False,
        evidence_fields=("ai_bonus_policy_comment", "samsung_minus_3_5pct", "sk_hynix_minus_1_4pct", "kospi_intraday_minus_5pct", "excess_tax_revenue_clarification"),
        red_flag_fields=("AI_tax_or_bonus_comment_without_legislation", "policy_headline_only", "corporate_profit_seizure_unconfirmed"),
        price_data_source="FT / Barron's / MarketWatch AI bonus policy-reaction anchors",
        reported_price_anchor="Samsung -3.5%, SK Hynix -1.4%, KOSPI intraday -5%, KOSPI close -2.3%",
        reported_return_anchor="Policy comment moved market before legislation or direct corporate-profit seizure proof",
        event_mfe_pct=None,
        event_mae_pct=-3.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_event_mae_pct": -3.5, "sk_hynix_event_mae_pct": -1.4, "kospi_intraday_mae_pct": -5.0, "kospi_close_mae_pct": -2.3, "policy_object": "excess_tax_revenue_from_AI_semiconductor_boom", "corporate_profit_seizure_confirmed": False, "ai_tax_or_windfall_tax_legislation_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="AI_windfall_fiscal_redistribution_policy_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="policy_comment_not_production_EPS_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="AI fiscal redistribution language is policy-risk watch, not company Green evidence.",
    ),
    Round280CaseCandidate(
        case_id="r11_loop13_samsung_strike_emergency_arbitration_supply_chain",
        symbol="005930",
        company_name="Samsung Electronics labor strike / government arbitration",
        primary_archetype=E2RArchetype.SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION,
        secondary_archetypes=(E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C, E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C),
        case_type="4b_watch",
        round_case_type="4C-watch",
        stage1_date=date(2026, 4, 1),
        stage2_date=date(2026, 5, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 19),
        stage3_decision="systemic_labor_risk_is_4c_watch_until_production_continuity_clears",
        stage4b_status="4C-watch/systemic-labor-supply-chain",
        hard_4c_confirmed=False,
        evidence_fields=("45000_workers", "18_day_strike_threat", "emergency_arbitration_possible", "one_day_direct_loss_1trn_krw", "samsung_export_share_22_8pct"),
        red_flag_fields=("strike_risk_unresolved", "systemic_strike_halting_production", "labor_production_continuity_unconfirmed"),
        price_data_source="Reuters Samsung strike / government intervention anchors",
        reported_price_anchor="45,000 workers threatened 18-day strike; Samsung -2.5%, KOSPI -3.2%",
        reported_return_anchor="One-day semiconductor halt risk up to 1T KRW direct loss; wider damage up to 100T KRW",
        event_mfe_pct=None,
        event_mae_pct=-2.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"threatened_workers": 45000, "strike_duration_days": 18, "one_day_direct_loss_krw_trn": 1.0, "potential_economic_damage_krw_trn": 100, "emergency_arbitration_ban_days": 30, "samsung_export_share_pct": 22.8, "samsung_domestic_stock_market_share_pct": 26, "samsung_employees": 120000, "supplier_count": 1700, "samsung_event_mae_pct": -2.5, "kospi_same_context_mae_pct": -3.2, "court_essential_staffing_required": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="systemic_labor_supply_chain_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="AI_supercycle_profit_sharing_disruption",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung labor risk is systemic supply-chain watch until production continuity is proven.",
    ),
    Round280CaseCandidate(
        case_id="r11_loop13_china_rare_earth_export_control_supply_chain",
        symbol="005930/000660/042660/supply_chain_basket",
        company_name="China rare-earth export controls / Korean semiconductor and defence supply chain",
        primary_archetype=E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C,
        secondary_archetypes=(E2RArchetype.RARE_EARTH_END_USE_RESTRICTION_4C, E2RArchetype.STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT),
        case_type="4b_watch",
        round_case_type="4C-watch",
        stage1_date=date(2025, 4, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 10, 22),
        stage3_decision="rare_earth_controls_are_supply_chain_gate_until_actual_license_inventory_and_alternative_sourcing_confirm",
        stage4b_status="4C-watch/supply-chain-license-gate",
        hard_4c_confirmed=False,
        evidence_fields=("china_over_90pct_processed_rare_earths", "heavy_exports_down_50pct", "defence_users_denied", "advanced_semiconductor_case_by_case"),
        red_flag_fields=("rare_earth_truce_without_actual_license", "rare_earth_license_denial", "critical_material_inventory_unconfirmed"),
        price_data_source="Reuters rare-earth export-control and Korea trade-envoy anchors",
        reported_price_anchor="Heavy rare-earth exports down about 50% since controls; direct Korean stock anchor unavailable",
        reported_return_anchor="Defence users denied licences; advanced semiconductor applications reviewed case-by-case",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"processed_rare_earths_china_share_pct": 90, "rare_earth_magnets_china_share_pct": 90, "heavy_rare_earth_exports_decline_since_controls_pct": -50, "affected_elements": ["yttrium", "dysprosium", "terbium", "scandium", "indium"], "defence_user_license_policy": "not_granted", "advanced_semiconductor_license_policy": "case_by_case", "korea_affected_companies_context": ["Samsung Electronics", "SK Hynix", "Hanwha Ocean"]},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="rare_earth_export_control_supply_chain_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="supply_chain_policy_risk_not_company_green",
        price_validation_status="supply_chain_policy_anchor_not_full_ohlc",
        notes="Rare-earth controls are supply-chain gates; truce headlines need actual licences and inventory proof.",
    ),
    Round280CaseCandidate(
        case_id="r11_loop13_us_korea_tariff_auto_semis_pharma_policy",
        symbol="005380/000270/004020/semiconductor_pharma_basket",
        company_name="U.S.-Korea tariff policy shock and relief",
        primary_archetype=E2RArchetype.US_KOREA_TARIFF_POLICY_4C_WATCH,
        secondary_archetypes=(E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH, E2RArchetype.INDUSTRIAL_POLICY_TARIFF_EVENT, E2RArchetype.TARIFF_IMPORT_REGULATION_OVERLAY),
        case_type="4b_watch",
        round_case_type="4C-watch + policy_relief",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 12, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 7, 31),
        stage3_decision="tariff_relief_is_not_green_without_company_margin_pass_through_local_production_and_FCF_bridge",
        stage4b_status="4C-watch/tariff-margin-bridge",
        hard_4c_confirmed=False,
        evidence_fields=("auto_tariff_15pct", "hyundai_minus_4_5pct", "kia_minus_6_6pct", "strategic_us_investment_350bn_usd", "semiconductor_pharma_cap_15pct"),
        red_flag_fields=("tariff_cut_without_margin_bridge", "tariff_shock_directly_cutting_OP_margin", "local_production_economics_unconfirmed"),
        price_data_source="Reuters U.S.-Korea tariff trade-deal anchors",
        reported_price_anchor="Hyundai -4.5%, Kia -6.6% after 15% tariff announcement",
        reported_return_anchor="15% lower than 25%, but FTA advantage versus Japan was removed",
        event_mfe_pct=None,
        event_mae_pct=-6.6,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_event_mae_pct": -4.5, "kia_event_mae_pct": -6.6, "auto_tariff_new_pct": 15, "auto_tariff_prior_pct": 25, "tariff_reduction_pp": -10, "korea_fta_prior_advantage_vs_japan_pct": 2.5, "requested_tariff_pct_by_korea": 12.5, "retroactive_effective_date": "2025-11-01", "strategic_us_investment_commitment_usd_bn": 350, "future_semiconductor_pharma_tariff_cap_pct": 15, "airplane_parts_tariffs_removed": True},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch_plus_policy_relief",
        rerating_result="policy_event_rerating",
        round_rerating_label="US_Korea_tariff_policy_gate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="tariff_relief_not_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tariff relief remains gated by margin, pass-through, local production and FCF.",
    ),
    Round280CaseCandidate(
        case_id="r11_loop13_samsung_sk_china_fab_tool_license_relief",
        symbol="005930/000660",
        company_name="Samsung Electronics / SK Hynix China fab tool license relief",
        primary_archetype=E2RArchetype.CHINA_FAB_EXPORT_LICENSE_RELIEF,
        secondary_archetypes=(E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH, E2RArchetype.MEMORY_HBM_CAPACITY),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2025, 12, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="annual_china_fab_tool_license_is_relief_not_multiyear_green",
        stage4b_status="watch/annual-license-regime",
        hard_4c_confirmed=False,
        evidence_fields=("2026_annual_license", "validated_end_user_status_expiry", "annual_approval_system", "traditional_memory_china_facility_role"),
        red_flag_fields=("annual_license_treated_as_multiyear_visibility", "license_denial_risk_removed_false", "multi_year_visibility_unconfirmed"),
        price_data_source="Reuters U.S. approval for Samsung/SK Hynix China tool shipments",
        reported_price_anchor="Annual 2026 licence granted; price data unavailable after deep search",
        reported_return_anchor="Annual licence is relief after waiver revocation, not durable Green",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"license_period": "2026_annual_license", "validated_end_user_status_expiry": "2025-12-31", "annual_approval_system": True, "company_context": ["Samsung Electronics", "SK Hynix"], "china_facility_role": "key_production_base_for_traditional_memory", "multi_year_visibility_confirmed": False, "license_denial_risk_removed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_relief",
        rerating_result="unknown",
        round_rerating_label="China_fab_tool_license_relief_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="annual_license_not_multiyear_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Annual license is Stage 2 relief; multiyear tool access and margin continuity remain open.",
    ),
    Round280CaseCandidate(
        case_id="r11_loop13_2025_south_korea_wildfires_disaster_reference",
        symbol="insurers/construction/utilities/agriculture/logistics_basket",
        company_name="2025 South Korea wildfires climate-disaster reference",
        primary_archetype=E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE,
        secondary_archetypes=(E2RArchetype.CLIMATE_DISASTER_EVENT, E2RArchetype.DISASTER_REBUILD_EVENT),
        case_type="4c_thesis_break",
        round_case_type="disaster_hard_reference",
        stage1_date=date(2025, 3, 21),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 30),
        stage3_decision="climate_disaster_is_loss_and_supply_chain_reference_before_rebuild_beneficiary_scoring",
        stage4b_status="hard-reference/disaster-loss-before-rebuild",
        hard_4c_confirmed=True,
        evidence_fields=("fatalities_32", "buildings_destroyed_5000", "area_burned_104000_hectares", "climate_change_likelihood_2x", "intensity_plus_15pct"),
        red_flag_fields=("climate_disaster_large_insured_or_uninsured_losses", "disaster_rebuild_story_without_loss_assessment", "disaster_loss_assessment_unconfirmed"),
        price_data_source="Reuters climate-attribution wildfire report + AP early disaster anchor",
        reported_price_anchor="32 deaths, about 5,000 buildings destroyed, 104,000 hectares burned",
        reported_return_anchor="Disaster cost reference; listed stock price anchor unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fatalities_final_context": 32, "buildings_destroyed_context": 5000, "area_burned_hectares": 104000, "prior_record_multiple": 4, "climate_change_likelihood_increase_multiple": 2, "climate_change_intensity_increase_pct": 15, "ap_early_fatalities": 24, "ap_early_injured": 26, "ap_early_evacuated": 28800, "ap_early_structures_destroyed": 300},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="climate_disaster_supply_chain_hard_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="disaster_cost_before_rebuild_beneficiary",
        price_validation_status="disaster_reference_not_full_ohlc",
        notes="Wildfire disaster is a hard reference; rebuild stories need loss assessment and actual contracts.",
    ),
)


def round280_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND280_CASE_CANDIDATES:
        stage3_terms = ("eps", "fcf", "margin", "bridge", "license", "inventory", "continuity", "loss", "contract", "fx", "execution")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND280_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round280 R11 Loop-13 policy/geopolitical/disaster/event price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND280_GREEN_REQUIRED_FIELDS) if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("rally", "premium", "bonus", "tariff", "relief", "rebuild", "headline"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("shock", "crisis", "strike", "license", "disaster", "tariff", "fx", "won", "loss", "hard"))),
            must_have_fields=ROUND280_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND280_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_macro_geopolitical_political_disaster_reference",
                "do_not_use_round280_cases_as_candidate_generation_input",
                "do_not_treat_policy_geopolitical_disaster_fx_energy_labor_tariff_or_license_headline_as_green",
                *ROUND280_GREEN_REQUIRED_FIELDS,
                *ROUND280_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
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
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.86 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round280_case_rows() -> tuple[dict[str, str], ...]:
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
        for candidate in ROUND280_CASE_CANDIDATES
    )


def round280_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND280_SCORE_ADJUSTMENTS)


def round280_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND280_SHADOW_WEIGHT_ROWS)


def round280_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND280_DEEP_SUB_ARCHETYPES)


def round280_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round280_price_validation": "true"} for field in ROUND280_PRICE_VALIDATION_FIELDS)


def round280_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round280_label": label, "canonical_archetype": canonical} for label, canonical in ROUND280_REQUIRED_TARGET_ALIASES.items())


def round280_summary() -> dict[str, int | bool | str]:
    cases = ROUND280_CASE_CANDIDATES
    return {
        "source_round": ROUND280_SOURCE_ROUND_PATH,
        "round_id": ROUND280_ANALYST_ROUND_ID,
        "large_sector": ROUND280_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "policy_relief_count": sum(1 for case in cases if "policy" in case.round_case_type.lower() or "relief" in case.round_case_type.lower()),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND280_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND280_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND280_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round280_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND280_SOURCE_ROUND_PATH,
        "round_id": ROUND280_ANALYST_ROUND_ID,
        "large_sector": ROUND280_LARGE_SECTOR,
        "summary": round280_summary(),
        "target_aliases": dict(ROUND280_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND280_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND280_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND280_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND280_HARD_4C_GATES),
        "score_adjustments": list(round280_score_adjustment_rows()),
        "shadow_weights": list(round280_shadow_weight_rows()),
        "deep_sub_archetypes": list(round280_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND280_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round280_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_policy_geopolitical_disaster_fx_energy_labor_tariff_or_license_headline_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round280_summary_markdown() -> str:
    summary = round280_summary()
    lines = [
        "# Round 280 R11 Loop 13 Policy Geopolitical Disaster Event Price Validation",
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
        f"- policy_relief: {summary['policy_relief_count']}",
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
    for case in ROUND280_CASE_CANDIDATES:
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
            "- Political shock and Middle East energy/FX shock are hard gates before company scoring.",
            "- AI bonus, tariff relief, and annual China fab licences are policy events until law, margin, or multiyear visibility closes.",
            "- Samsung labor disruption and rare-earth controls are supply-chain gates, not positive company evidence.",
            "- Disaster rebuild stories must wait for loss assessment, insurance burden, rebuild contracts, margin, and cashflow.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round280_green_gate_review_markdown() -> str:
    lines = [
        "# Round 280 R11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R11 Stage 3-Green is not `policy headline`, `tariff relief`, `rare-earth truce`, `strike relief`, `AI dividend comment`, or `disaster rebuild story`. It requires law/budget execution, EPS/FCF bridge, margin, actual licences, production continuity, loss assessment, FX stability, and price-after-evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND280_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND280_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND280_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Hyundai/Kia tariff relief` is not Green until gross margin and pass-through are visible.",
            "- `AI bonus comment` can create 4B-watch even if it is later clarified as excess tax revenue.",
            "- `Wildfire rebuild theme` is not Green until loss assessment and actual rebuild contract economics appear.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round280_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 280 R11 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND280_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND280_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND280_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round280_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 280 R11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, policy execution, tariff margin, licences, labor continuity, disaster losses, or FX stabilization where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND280_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND280_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round280_r11_loop13_reports(
    output_directory: str | Path = ROUND280_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND280_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND280_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round280_case_records(), cases_path),
        "audit": _write_json(round280_audit_payload(), audit_path),
        "summary": output / "round280_r11_loop13_price_validation_summary.md",
        "case_matrix": output / "round280_r11_loop13_case_matrix.csv",
        "target_aliases": output / "round280_r11_loop13_target_aliases.csv",
        "score_adjustments": output / "round280_r11_loop13_score_adjustments.csv",
        "shadow_weights": output / "round280_r11_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round280_r11_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round280_r11_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round280_r11_loop13_green_gate_review.md",
        "price_validation_plan": output / "round280_r11_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round280_r11_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round280_summary_markdown(), encoding="utf-8")
    _write_csv(round280_case_rows(), paths["case_matrix"])
    _write_csv(round280_target_alias_rows(), paths["target_aliases"])
    _write_csv(round280_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round280_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round280_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round280_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round280_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round280_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round280_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"+{value}" if value > 0 else str(value)
