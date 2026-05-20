"""Round-273 R4 Loop-13 materials/spread/strategic-resources pack.

Round 273 converts ``docs/round/round_273.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a graphite tariff or control premium can move price first, but
R4 Green needs product spread, offtake/call-off, utilization, working capital,
FCF, and governance/dilution risk to clear.
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


ROUND273_SOURCE_ROUND_PATH = "docs/round/round_273.md"
ROUND273_ANALYST_ROUND_ID = "round_201"
ROUND273_LARGE_SECTOR = "MATERIALS_SPREAD_STRATEGIC_RESOURCES"
ROUND273_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round273_r4_loop13_materials_spread_strategic_price_validation"
ROUND273_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop13_round273.jsonl"
ROUND273_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round273_r4_loop13_materials_spread_strategic_price_validation_audit.json"

ROUND273_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION": E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION.value,
    "GRAPHITE_LITHIUM_POLICY_PRICE_EVENT": E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT.value,
    "STEEL_TARIFF_TWO_SIDED_RELIEF_RISK": E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK.value,
    "POLICY_CAPEX_FALSE_POSITIVE": E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE.value,
    "PETROCHEMICAL_CAPACITY_RESTRUCTURING": E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING.value,
    "PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE": E2RArchetype.PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE.value,
    "DEFENSE_METALS_AMMUNITION_OPTIONALITY": E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY.value,
    "COPPER_COMMODITY_OVERHEAT_4B": E2RArchetype.COPPER_COMMODITY_OVERHEAT_4B.value,
}

ROUND273_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "product_spread_visibility_confirmed",
    "cost_curve_advantage_confirmed",
    "offtake_or_actual_contract_confirmed",
    "capacity_utilization_confirmed",
    "working_capital_control_confirmed",
    "fcf_after_restructuring_confirmed",
    "governance_dilution_risk_cleared",
    "export_control_or_tariff_risk_cleared",
    "restructuring_margin_recovery_confirmed",
    "price_path_after_evidence",
)

ROUND273_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "control_premium_only",
    "mna_rumor_only",
    "commodity_price_event_only",
    "tariff_relief_only",
    "policy_capex_only",
    "restructuring_plan_only",
    "capacity_shutdown_only",
    "dilution_or_governance_fight_unresolved",
    "export_tariff_exposure_unresolved",
    "capex_without_funding_or_roi",
)

ROUND273_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "tender_offer_or_control_premium_plus_20pct",
    "commodity_tariff_or_lithium_event_plus_10_to_20pct",
    "anti_dumping_relief_steel_rally",
    "policy_capex_before_funding_roi",
    "mna_rumor_before_confirmed_transaction",
    "restructuring_support_package_before_spread_recovery",
)

ROUND273_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "dilutive_issuance_destroying_existing_holders",
    "export_tariff_destroying_margin",
    "china_end_use_restriction_or_sanction",
    "commodity_price_collapse_without_hedge",
    "petrochemical_credit_event_or_workout",
    "capacity_cut_fails_to_restore_spread",
    "capex_funding_failure",
    "mna_denial_after_rumor_driven_rally",
)

ROUND273_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_anchor",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "policy_or_tariff_anchor",
    "capacity_or_capex_anchor",
    "spread_or_margin_anchor",
    "governance_dilution_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round273ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round273ShadowWeightRow:
    archetype: E2RArchetype
    product_spread_visibility: int
    cost_curve_advantage: int
    offtake_actual_contract: int
    capacity_utilization: int
    working_capital_control: int
    fcf_after_restructuring: int
    governance_dilution_control: int
    export_control_resilience: int
    commodity_price_pass_through: int
    policy_relief_to_margin_bridge: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "product_spread_visibility": _signed(self.product_spread_visibility),
            "cost_curve_advantage": _signed(self.cost_curve_advantage),
            "offtake_actual_contract": _signed(self.offtake_actual_contract),
            "capacity_utilization": _signed(self.capacity_utilization),
            "working_capital_control": _signed(self.working_capital_control),
            "fcf_after_restructuring": _signed(self.fcf_after_restructuring),
            "governance_dilution_control": _signed(self.governance_dilution_control),
            "export_control_resilience": _signed(self.export_control_resilience),
            "commodity_price_pass_through": _signed(self.commodity_price_pass_through),
            "policy_relief_to_margin_bridge": _signed(self.policy_relief_to_margin_bridge),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round273DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round273CaseCandidate:
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
    peak_return_from_stage3_pct: float | None
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


ROUND273_SCORE_ADJUSTMENTS: tuple[Round273ScoreAdjustment, ...] = (
    Round273ScoreAdjustment("product_spread_visibility", 5, "raise", "R4는 제품 스프레드가 실제 이익으로 닫혀야 한다."),
    Round273ScoreAdjustment("cost_curve_advantage", 5, "raise", "원가곡선 우위가 있어야 commodity event를 넘어선다."),
    Round273ScoreAdjustment("offtake_or_actual_contract", 5, "raise", "전략자원은 실제 offtake나 계약이 필요하다."),
    Round273ScoreAdjustment("capacity_utilization", 5, "raise", "CAPEX나 shutdown보다 가동률이 중요하다."),
    Round273ScoreAdjustment("working_capital_control", 5, "raise", "소재/화학은 운전자본이 FCF를 크게 흔든다."),
    Round273ScoreAdjustment("FCF_after_restructuring", 5, "raise", "구조조정 후 FCF가 돌아와야 Green 후보가 된다."),
    Round273ScoreAdjustment("governance_dilution_control", 5, "raise", "전략광물 프리미엄은 희석·거버넌스 통과가 필요하다."),
    Round273ScoreAdjustment("export_control_resilience", 5, "raise", "관세·수출통제 리스크를 통과해야 한다."),
    Round273ScoreAdjustment("commodity_price_pass_through", 4, "raise", "가격 이벤트가 실제 판가/마진으로 전가되어야 한다."),
    Round273ScoreAdjustment("policy_relief_to_margin_bridge", 4, "raise", "정책 relief가 마진으로 이어지는 bridge를 본다."),
    Round273ScoreAdjustment("control_premium_only", -5, "lower", "지배권 프리미엄은 operating Green이 아니다."),
    Round273ScoreAdjustment("M&A_rumor_only", -5, "lower", "M&A rumor는 확정 거래 전 event premium이다."),
    Round273ScoreAdjustment("tariff_relief_only", -5, "lower", "관세 relief만으로 제품 스프레드와 FCF를 만들지 않는다."),
    Round273ScoreAdjustment("policy_CAPEX_without_ROI", -5, "lower", "정책 CAPEX는 funding/ROI가 없으면 false positive가 된다."),
    Round273ScoreAdjustment("commodity_price_event_only", -5, "lower", "graphite/lithium 가격 이벤트만으로는 Green 금지다."),
    Round273ScoreAdjustment("restructuring_plan_undisclosed", -4, "lower", "비공개 구조조정 계획은 relief이지 Green이 아니다."),
    Round273ScoreAdjustment("capacity_shutdown_without_spread", -4, "lower", "capacity shutdown만 있고 spread가 없으면 Green 금지다."),
    Round273ScoreAdjustment("dilution_or_governance_fight", -5, "lower", "희석·지배권 분쟁이 열려 있으면 Green을 막는다."),
    Round273ScoreAdjustment("export_tariff_exposure", -5, "lower", "수출 관세 노출은 R4 4C-watch다."),
)


ROUND273_SHADOW_WEIGHT_ROWS: tuple[Round273ShadowWeightRow, ...] = (
    Round273ShadowWeightRow(E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION, 4, 5, 5, 4, 5, 5, 5, 5, 3, 3, -5, 5, 5, "Korea Zinc needs offtake/margin/funding/dilution control beyond control premium."),
    Round273ShadowWeightRow(E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT, 5, 4, 5, 5, 4, 5, 3, 5, 5, 3, -5, 5, 4, "POSCO Future M graphite/lithium events need supply contract and margin proof."),
    Round273ShadowWeightRow(E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK, 5, 5, 3, 4, 4, 5, 2, 5, 4, 4, -5, 5, 5, "Domestic tariff relief and export tariff risk must be scored together."),
    Round273ShadowWeightRow(E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, 3, 3, 2, 4, 5, 5, 3, 4, 2, 2, -5, 5, 5, "Hyundai Steel U.S. CAPEX failed without funding/ROI clarity."),
    Round273ShadowWeightRow(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, 5, 4, 2, 5, 5, 5, 3, 2, 4, 5, -4, 5, 5, "NCC shutdown/support package is relief until spread/OPM/FCF recover."),
    Round273ShadowWeightRow(E2RArchetype.PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE, 5, 4, 3, 5, 5, 5, 3, 3, 4, 3, -4, 4, 4, "Lotte overseas capex/asset sale requires utilization, ROIC and spread."),
    Round273ShadowWeightRow(E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY, 4, 4, 5, 4, 4, 5, 3, 4, 4, 2, -5, 5, 4, "Poongsan M&A rumor is event premium until confirmed order/transaction/cash return."),
    Round273ShadowWeightRow(E2RArchetype.COPPER_COMMODITY_OVERHEAT_4B, 5, 4, 3, 3, 4, 4, 2, 3, 5, 2, -5, 5, 4, "Copper/metal price rallies need pass-through, demand and FCF confirmation."),
)


ROUND273_DEEP_SUB_ARCHETYPES: tuple[Round273DeepSubArchetype, ...] = (
    Round273DeepSubArchetype("strategic minerals governance", E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION, ("Korea Zinc", "MBK", "Young Poong", "Tennessee refinery", "dilution")),
    Round273DeepSubArchetype("graphite lithium price event", E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT, ("POSCO Future M", "graphite tariff", "CATL lithium mine", "L&F read-through")),
    Round273DeepSubArchetype("steel tariff two-sided", E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK, ("POSCO", "Hyundai Steel", "SeAH Steel", "anti-dumping", "U.S. 50% tariff")),
    Round273DeepSubArchetype("policy capex false positive", E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, ("Hyundai Steel", "Louisiana plant", "$5.8B", "funding ROI missing")),
    Round273DeepSubArchetype("petrochemical restructuring", E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, ("LG Chem", "Hanwha Solutions", "DL Chemical", "YNCC", "NCC shutdown")),
    Round273DeepSubArchetype("overseas petrochemical capex", E2RArchetype.PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE, ("Lotte Chemical", "Indonesia cracker", "Pakistan PTA sale", "utilization")),
    Round273DeepSubArchetype("defense metals optionality", E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY, ("Poongsan", "Hanwha Aerospace", "ammunition", "copper products", "M&A rumor")),
    Round273DeepSubArchetype("copper commodity overheat", E2RArchetype.COPPER_COMMODITY_OVERHEAT_4B, ("copper price", "commodity beta", "pass-through", "working capital")),
)


ROUND273_CASE_CANDIDATES: tuple[Round273CaseCandidate, ...] = (
    Round273CaseCandidate(
        case_id="r4_loop13_korea_zinc_control_premium_dilution_watch",
        symbol="010130",
        company_name="Korea Zinc",
        primary_archetype=E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION,
        secondary_archetypes=(E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="4b_watch",
        round_case_type="success_candidate_overheat_4B_watch",
        stage1_date=date(2024, 9, 13),
        stage2_date=date(2024, 9, 13),
        stage3_date=None,
        stage4b_date=date(2024, 9, 13),
        stage4c_date=date(2025, 12, 16),
        stage3_decision="control_premium_and_critical_minerals_refinery_plan_are_stage2_not_green_until_offtake_margin_funding_dilution_and_fcf_clear",
        stage4b_status="4B-watch/governance-dilution",
        hard_4c_confirmed=False,
        evidence_fields=("mbk_young_poong_tender_offer", "world_largest_refined_zinc_producer", "tennessee_critical_minerals_refinery_project"),
        red_flag_fields=("control_premium_only", "withdrawn_share_sale", "injunction_event_mae_minus_13pct", "dilution_or_governance_fight"),
        price_data_source="WSJ / Reuters tender-offer, share-sale, injunction anchors",
        reported_price_anchor="Tender offer 660,000 won; event high 690,000 won; Tennessee refinery project $7.4B",
        reported_return_anchor="+24% record-high control premium; later -13% injunction event",
        event_mfe_pct=24.0,
        event_mae_pct=-13.0,
        stage2_price_anchor=660000.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=690000.0,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"tender_offer_price_krw": 660000.0, "event_high_price_krw": 690000.0, "event_mfe_pct": 24.0, "tender_offer_value_krw_trn": 2.0, "tender_offer_value_usd_bn": 1.5, "target_controlling_stake_pct": 47.74, "withdrawn_share_sale_usd_bn": 1.8, "withdrawal_initial_mfe_pct": 6.0, "withdrawal_later_mae_pct": -7.0, "tennessee_refinery_project_usd_bn": 7.4, "injunction_event_mae_pct": -13.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="critical_minerals_control_premium_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="control_premium_and_dilution_not_operating_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="전략광물 후보이지만 지배권 프리미엄과 희석·거버넌스가 먼저 가격을 움직였다.",
    ),
    Round273CaseCandidate(
        case_id="r4_loop13_posco_futurem_graphite_lithium_event",
        symbol="003670",
        company_name="POSCO Future M",
        primary_archetype=E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT,
        secondary_archetypes=(E2RArchetype.BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY, E2RArchetype.LITHIUM_PRICE_EVENT_KOREA),
        case_type="event_premium",
        round_case_type="event_premium_price_moved_without_evidence",
        stage1_date=date(2025, 7, 18),
        stage2_date=date(2025, 7, 18),
        stage3_date=None,
        stage4b_date=date(2025, 7, 18),
        stage4c_date=None,
        stage3_decision="graphite_tariff_and_lithium_mine_events_are_not_green_until_contract_certification_spread_margin_and_fcf_confirm",
        stage4b_status="4B-watch/policy-price-event",
        hard_4c_confirmed=False,
        evidence_fields=("us_93_5pct_antidumping_tariff_chinese_graphite", "catl_lithium_mine_suspension", "posco_future_m_graphite_lithium_readthrough"),
        red_flag_fields=("actual_graphite_supply_contract_unconfirmed", "margin_unconfirmed", "commodity_price_event_only", "tariff_relief_only"),
        price_data_source="FT graphite-tariff anchor + WSJ CATL lithium event anchor",
        reported_price_anchor="POSCO Future M +20% graphite tariff event; +8.3% CATL lithium event",
        reported_return_anchor="Syrah +22%, Nouveau Monde +26%, Novonix +15%; L&F +10% in lithium context",
        event_mfe_pct=20.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"graphite_tariff_event_mfe_pct": 20.0, "us_antidumping_tariff_on_chinese_graphite_pct": 93.5, "approx_total_us_tariff_rate_on_chinese_graphite_pct": 160.0, "catl_lithium_event_mfe_pct": 8.3, "lnf_same_context_mfe_pct": 10.0, "samsung_sdi_same_context_mfe_pct": 3.2, "lges_same_context_mfe_pct": 2.8, "actual_graphite_supply_contract_confirmed": False, "margin_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_label="graphite_lithium_policy_price_event",
        stage_failure_type="false_yellow",
        round_stage_failure_label="tariff_or_lithium_event_not_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="graphite/lithium event는 가격을 움직였지만 실제 공급계약·인증·마진 전에는 Green이 아니다.",
    ),
    Round273CaseCandidate(
        case_id="r4_loop13_steel_tariff_two_sided_posco_hyundai_seah",
        symbol="005490/004020/306200",
        company_name="POSCO Holdings / Hyundai Steel / SeAH Steel",
        primary_archetype=E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK,
        secondary_archetypes=(E2RArchetype.STEEL_TARIFF_EXPORT_RISK, E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF),
        case_type="event_premium",
        round_case_type="event_premium_4C_watch",
        stage1_date=date(2025, 2, 10),
        stage2_date=date(2025, 2, 20),
        stage3_date=None,
        stage4b_date=date(2025, 2, 20),
        stage4c_date=date(2025, 6, 2),
        stage3_decision="domestic_antidumping_relief_and_us_export_tariff_risk_coexist; green_requires_spread_export_margin_and_fcf",
        stage4b_status="4B-watch/two-sided-policy-relief",
        hard_4c_confirmed=False,
        evidence_fields=("korea_antidumping_tariff_27_91_to_38_02pct", "hyundai_steel_antidumping_plus_5_8pct", "posco_antidumping_plus_3_9pct"),
        red_flag_fields=("us_25pct_tariff_event", "us_50pct_tariff_event", "seah_steel_minus_8pct", "export_tariff_exposure"),
        price_data_source="Reuters steel tariff / anti-dumping event anchors",
        reported_price_anchor="POSCO 25% tariff event low 230,500 won; anti-dumping relief and U.S. 50% tariff shock both visible",
        reported_return_anchor="Hyundai +5.8% relief, POSCO +3.9% relief; later POSCO/Hyundai -3%, SeAH -8%",
        event_mfe_pct=5.8,
        event_mae_pct=-8.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"posco_25pct_tariff_event_low_krw": 230500.0, "posco_25pct_tariff_event_mae_pct": -3.6, "hyundai_steel_25pct_tariff_event_mae_pct": -2.9, "kospi_25pct_tariff_context_pct": -0.5, "korea_antidumping_tariff_pct": "27.91-38.02", "hyundai_steel_antidumping_mfe_pct": 5.8, "posco_antidumping_mfe_pct": 3.9, "hyundai_relative_outperformance_pp": 6.5, "posco_relative_outperformance_pp": 4.6, "us_50pct_tariff_posco_hyundai_mae_pct": -3.0, "seah_steel_50pct_tariff_mae_pct": -8.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="event_premium_plus_thesis_break_watch",
        rerating_result="event_premium",
        round_rerating_label="steel_tariff_two_sided_relief_risk",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="policy_relief_not_spread_FCF_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="국내 anti-dumping relief와 미국 수출 관세 리스크를 같이 봐야 한다.",
    ),
    Round273CaseCandidate(
        case_id="r4_loop13_hyundai_steel_us_plant_policy_capex_false_positive",
        symbol="004020",
        company_name="Hyundai Steel",
        primary_archetype=E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.STEEL_TARIFF_EXPORT_RISK, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="failed_rerating",
        round_case_type="failed_rerating_policy_CAPEX_false_positive",
        stage1_date=date(2025, 3, 24),
        stage2_date=date(2025, 3, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="us_plant_tariff_hedge_capex_is_not_green_without_funding_roi_margin_and_demand_conversion",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("5_8bn_usd_louisiana_steel_plant", "annual_capacity_2_7mn_tonnes", "hyundai_group_21bn_usd_us_package"),
        red_flag_fields=("post_announcement_drawdown_minus_21_2pct", "funding_plan_incomplete", "policy_CAPEX_without_ROI", "relative_underperformance_vs_kospi_minus_15_7pp"),
        price_data_source="Reuters U.S. plant / investor backlash anchor",
        reported_price_anchor="$5.8B Louisiana plant / 2.7M tonnes annual capacity",
        reported_return_anchor="Hyundai Steel -21.2% since announcement vs KOSPI -5.5%",
        event_mfe_pct=None,
        event_mae_pct=-21.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"plant_investment_usd_bn": 5.8, "annual_capacity_mn_tonnes": 2.7, "group_us_investment_package_usd_bn": 21.0, "post_announcement_drawdown_pct": -21.2, "posco_same_period_pct": -18.3, "kospi_same_period_pct": -5.5, "relative_underperformance_vs_kospi_pp": -15.7, "funding_plan_status": "incomplete_at_event_stage"},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="no_rerating",
        round_rerating_label="policy_CAPEX_failed_rerating",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="CAPEX_without_funding_ROI_green",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="정책 CAPEX headline은 funding/ROI가 없으면 false positive가 된다.",
    ),
    Round273CaseCandidate(
        case_id="r4_loop13_lgchem_hanwha_dl_yncc_petchem_credit_watch",
        symbol="051910/009830/DL_Chemical_exposure",
        company_name="LG Chem / Hanwha Solutions / DL Chemical / YNCC",
        primary_archetype=E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.STANDALONE_NCC_CREDIT_BREAK, E2RArchetype.CHEMICAL_SPREAD_KOREA),
        case_type="failed_rerating",
        round_case_type="4C-watch_credit_spread",
        stage1_date=date(2025, 8, 27),
        stage2_date=date(2025, 12, 19),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 8, 27),
        stage3_decision="petrochemical_restructuring_plan_is_relief_not_green_until_spread_opm_debt_cleanup_and_fcf_confirm",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("capacity_cut_target_2_7_to_3_7mn_tpy", "about_25pct_total_capacity", "yncc_restructuring_plan_submitted"),
        red_flag_fields=("yncc_debt_to_equity_249pct", "yncc_no3_cracker_shut", "shaheen_new_supply_2026", "restructuring_plan_undisclosed"),
        price_data_source="Reuters petrochemical overhaul / restructuring-plan anchors",
        reported_price_anchor="Capacity cut target 2.7M-3.7M tpy; YNCC D/E 249%",
        reported_return_anchor="Full adjusted OHLC unavailable in this pass",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"capacity_cut_target_mn_tpy": "2.7-3.7", "capacity_cut_equivalent_pct": 25.0, "naphtha_feedstock_share_for_ethylene_pct": 82.0, "yncc_debt_to_equity_1h2025_pct": 249.0, "yncc_possible_shutdown": "one or two of three crackers", "yncc_no3_cracker_status": "shut in August 2025", "shaheen_new_supply_2026_mn_tpy": 1.8, "lg_chem_plan_status": "submitted; details undisclosed", "hanwha_dl_yncc_plan_status": "submitted; details undisclosed"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="petrochemical_credit_and_capacity_break_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="restructuring_plan_not_spread_FCF_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="YNCC D/E 249%와 cracker shutdown은 구조조정 relief 전에 보는 credit/spread 4C-watch다.",
    ),
    Round273CaseCandidate(
        case_id="r4_loop13_lotte_hd_hyundai_petchem_restructuring_relief",
        symbol="011170/267250_exposure",
        company_name="Lotte Chemical / HD Hyundai Chemical",
        primary_archetype=E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE,),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2025, 11, 26),
        stage2_date=date(2026, 2, 24),
        stage3_date=None,
        stage4b_date=date(2026, 2, 24),
        stage4c_date=None,
        stage3_decision="shutdown_and_support_package_are_crisis_relief_not_green_until_product_spread_opm_fcf_and_debt_cleanup_confirm",
        stage4b_status="4B-watch/restructuring-relief-before-spread",
        hard_4c_confirmed=False,
        evidence_fields=("daesan_ncc_1_1mn_tpy_shutdown", "1_2tn_krw_capital_increase", "government_support_package_over_2tn_krw"),
        red_flag_fields=("capacity_shutdown_without_spread", "support_package_not_margin", "debt_cleanup_unconfirmed", "fcf_unconfirmed"),
        price_data_source="Reuters restructuring approval / plan anchors",
        reported_price_anchor="Daesan NCC 1.1M tpy shutdown for 3 years; 1.2T won capital increase",
        reported_return_anchor="Full adjusted OHLC unavailable in this pass",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"daesan_ncc_shutdown_capacity_mn_tpy": 1.1, "shutdown_duration_years": 3.0, "capital_increase_krw_trn": 1.2, "each_parent_injection_krw_bn": 600.0, "government_support_package_krw_trn": 2.0, "utility_cost_savings_krw_bn": 115.0, "rnd_funding_krw_bn": 26.0, "combined_capacity_before_shutdown_mn_tpy": 1.95, "daesan_shutdown_share_of_combined_capacity_pct": 56.4},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_relief",
        rerating_result="policy_event_rerating",
        round_rerating_label="petrochemical_restructuring_relief",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="capacity_shutdown_support_not_green_until_spread_FCF",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Daesan shutdown과 2T won support package는 위기 완화다. spread/FCF 전에는 Stage 3가 아니다.",
    ),
    Round273CaseCandidate(
        case_id="r4_loop13_lotte_chemical_overseas_portfolio_spread_gate",
        symbol="011170",
        company_name="Lotte Chemical",
        primary_archetype=E2RArchetype.PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING,),
        case_type="success_candidate",
        round_case_type="success_candidate_but_spread_gated",
        stage1_date=date(2025, 11, 6),
        stage2_date=date(2025, 11, 13),
        stage3_date=None,
        stage4b_date=date(2025, 11, 13),
        stage4c_date=None,
        stage3_decision="overseas_capex_and_asset_sale_are_not_green_without_ethylene_spread_utilization_working_capital_roic_and_fcf",
        stage4b_status="4B-watch/portfolio-capex-before-spread",
        hard_4c_confirmed=False,
        evidence_fields=("indonesia_4bn_usd_petrochemical_facility", "1mn_tpy_ethylene_capacity", "pakistan_75pct_stake_sale_98bn_krw"),
        red_flag_fields=("ethane_naphtha_spread_unconfirmed", "utilization_unconfirmed", "capex_without_funding_or_roi", "working_capital_unconfirmed"),
        price_data_source="Reuters Indonesia plant / Pakistan asset-sale anchors",
        reported_price_anchor="$4B Indonesia cracker; 75% Pakistan PTA stake sale for 98B won",
        reported_return_anchor="Full adjusted OHLC unavailable in this pass",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"indonesia_project_value_usd_bn": 4.0, "indonesia_ethylene_capacity_mn_tpy": 1.0, "indonesia_import_reduction_target_pct": 90.0, "pakistan_stake_sold_pct": 75.0, "pakistan_sale_value_krw_bn": 98.0, "pakistan_sale_value_usd_mn": 68.94, "pakistan_pta_capacity_tpy": 500000.0, "ethane_naphtha_spread_confirmed": False, "utilization_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="overseas_petrochemical_portfolio_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="capex_asset_sale_not_spread_FCF_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="해외 capex와 asset sale은 utilization, ROIC, spread가 확인되어야 한다.",
    ),
    Round273CaseCandidate(
        case_id="r4_loop13_poongsan_defense_metals_mna_rumor",
        symbol="103140",
        company_name="Poongsan",
        primary_archetype=E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.COPPER_COMMODITY_OVERHEAT_4B, E2RArchetype.MOU_LOI_NOT_CONTRACT),
        case_type="event_premium",
        round_case_type="event_premium_mna_rumor",
        stage1_date=date(2026, 4, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2026, 4, 9),
        stage4c_date=None,
        stage3_decision="mna_rumor_is_not_green_until_confirmed_transaction_copper_spread_ammunition_order_or_cash_return_confirm",
        stage4b_status="4B-watch/M&A-rumor",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_aerospace_reported_bid", "poongsan_copper_products", "ammunition_business_optionality"),
        red_flag_fields=("hanwha_dropped_acquisition_review", "poongsan_denied_sale_plan", "M&A_rumor_only", "confirmed_transaction_absent"),
        price_data_source="Reuters M&A rumor / denial anchors",
        reported_price_anchor="Reported deal value 1.5T won / $1.1B; later review dropped and sale denied",
        reported_return_anchor="Full adjusted OHLC unavailable in this pass",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"reported_deal_value_krw_trn": 1.5, "reported_deal_value_usd_bn": 1.1, "businesses": ["copper products", "ammunition manufacturing", "small-caliber rounds", "large-caliber shells", "missile warheads"], "transaction_status": "not confirmed; Hanwha dropped review; Poongsan denied sale plan"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="defense_metals_optional_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="M&A_rumor_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="방산금속 optionality는 있지만 M&A rumor는 Green이 아니다.",
    ),
)


def round273_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("spread", "offtake", "contract", "utilization", "working_capital", "fcf", "margin", "roic")
    for candidate in ROUND273_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND273_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round273 R4 Loop-13 materials/spread/strategic-resources price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "premium" in field.lower()
                or "event" in field.lower()
                or "rumor" in field.lower()
                or "tender" in field.lower()
                or "policy" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "4c" in field.lower()
                or "minus" in field.lower()
                or "tariff" in field.lower()
                or "credit" in field.lower()
                or "dilution" in field.lower()
                or "denied" in field.lower()
                or "failure" in field.lower()
            ),
            must_have_fields=ROUND273_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND273_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_control_premium_tariff_policy_capex_or_restructuring_headlines_as_green_alone",
                *ROUND273_GREEN_REQUIRED_FIELDS,
                *ROUND273_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_return_from_stage3=candidate.peak_return_from_stage3_pct,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.event_mfe_pct is not None
                or candidate.event_mae_pct is not None,
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round273_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND273_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": "R4",
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
                "peak_return_from_stage3_pct": _float_text(candidate.peak_return_from_stage3_pct),
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
        )
    return tuple(rows)


def round273_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND273_SCORE_ADJUSTMENTS)


def round273_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND273_SHADOW_WEIGHT_ROWS)


def round273_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND273_DEEP_SUB_ARCHETYPES)


def round273_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round273_price_validation": "true"} for field in ROUND273_PRICE_VALIDATION_FIELDS)


def round273_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round273_label": label, "canonical_archetype": canonical} for label, canonical in ROUND273_REQUIRED_TARGET_ALIASES.items())


def round273_summary() -> dict[str, int | bool | str]:
    cases = ROUND273_CASE_CANDIDATES
    return {
        "source_round": ROUND273_SOURCE_ROUND_PATH,
        "round_id": ROUND273_ANALYST_ROUND_ID,
        "large_sector": ROUND273_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "four_b_watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None),
        "price_data_unavailable_count": sum(1 for case in cases if case.price_validation_status == "price_data_unavailable_after_deep_search"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND273_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND273_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND273_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round273_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND273_SOURCE_ROUND_PATH,
        "round_id": ROUND273_ANALYST_ROUND_ID,
        "large_sector": ROUND273_LARGE_SECTOR,
        "summary": round273_summary(),
        "target_aliases": dict(ROUND273_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND273_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND273_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND273_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND273_HARD_4C_GATES),
        "deep_sub_archetypes": round273_deep_sub_archetype_rows(),
        "shadow_weights": round273_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round273_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_control_premium_tariff_policy_capex_or_restructuring_headlines_as_green_alone",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round273_summary_markdown() -> str:
    summary = round273_summary()
    lines = [
        "# Round 273 R4 Loop 13 Materials Spread Strategic Resources Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- 4B-watch case_type: {summary['four_b_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- price_data_unavailable: {summary['price_data_unavailable_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- false_positive_score: {summary['false_positive_score_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND273_CASE_CANDIDATES:
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
            "- R4 Stage 3 is not the word strategic minerals, graphite, lithium, steel tariff, capex, restructuring, or defense metals.",
            "- Korea Zinc is strategic-minerals Stage 2 plus governance/dilution 4B-watch, not operating Green.",
            "- POSCO Future M graphite/lithium moves are price events until contracts, certification, margin and FCF confirm.",
            "- Steel tariff relief is two-sided because domestic protection and export tariff damage can coexist.",
            "- Petrochemical restructuring is relief before spread, OPM, debt cleanup and FCF prove out.",
            "- Poongsan M&A rumor is event premium until a confirmed transaction, ammunition orders, copper spread or cash return appears.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round273_green_gate_review_markdown() -> str:
    lines = ["# Round 273 R4 Loop 13 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND273_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND273_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `control premium +24%`는 operating Green이 아니다. offtake, margin, FCF가 필요하다.",
            "- `graphite tariff로 +20%`도 실제 공급계약과 customer certification 전에는 price event다.",
            "- `NCC shutdown`은 위기 완화일 수 있지만, spread와 FCF 회복 전에는 Green이 아니다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round273_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 273 R4 Loop 13 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND273_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND273_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B는 control premium, tariff relief, policy CAPEX, restructuring package가 실적보다 먼저 가격화된 상태다.",
            "- 4C-watch는 export tariff, dilution, petrochemical credit stress처럼 Green을 막는 위험이다.",
            "- 이번 라운드에서는 hard 4C를 확정하지 않고 watch로 둔다.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND273_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round273_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 273 R4 Loop 13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND273_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round273_r4_loop13_reports(
    output_directory: str | Path = ROUND273_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND273_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND273_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round273_case_records(), cases_path),
        "audit": _write_json(round273_audit_payload(), audit_path),
        "summary": output / "round273_r4_loop13_price_validation_summary.md",
        "case_matrix": output / "round273_r4_loop13_case_matrix.csv",
        "target_aliases": output / "round273_r4_loop13_target_aliases.csv",
        "score_adjustments": output / "round273_r4_loop13_score_adjustments.csv",
        "shadow_weights": output / "round273_r4_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round273_r4_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round273_r4_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round273_r4_loop13_green_gate_review.md",
        "price_validation_plan": output / "round273_r4_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round273_r4_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round273_summary_markdown(), encoding="utf-8")
    _write_csv(round273_case_rows(), paths["case_matrix"])
    _write_csv(round273_target_alias_rows(), paths["target_aliases"])
    _write_csv(round273_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round273_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round273_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round273_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round273_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round273_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round273_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"{value:+d}" if isinstance(value, int) else str(value)
