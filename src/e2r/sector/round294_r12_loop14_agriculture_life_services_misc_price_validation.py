"""Round-294 R12 Loop-14 agriculture/life-services/misc validation pack.

This module converts ``docs/round/round_294.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: Jensen Huang eating fried chicken can move chicken-related
stocks, but it is not Stage 3-Green unless same-store sales, franchise fees,
raw-material spread, repeat demand, and FCF are visible.
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


ROUND294_SOURCE_ROUND_PATH = "docs/round/round_294.md"
ROUND294_ANALYST_ROUND_ID = "round_222"
ROUND294_LARGE_SECTOR = "AGRICULTURE_LIFE_SERVICES_MISC"
ROUND294_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round294_r12_loop14_agriculture_life_services_misc_price_validation"
ROUND294_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop14_round294.jsonl"
ROUND294_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round294_r12_loop14_agriculture_life_services_misc_price_validation_audit.json"

ROUND294_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH": E2RArchetype.AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH.value,
    "AGRI_FOOD_INPUT_COST_4C_WATCH": E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH.value,
    "FRIED_CHICKEN_MEME_EVENT_PREMIUM": E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM.value,
    "FOOD_DELIVERY_CONSOLIDATION_STAGE2": E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2.value,
    "DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE": E2RArchetype.DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE.value,
    "WASTE_RECYCLING_INFRA_STAGE2": E2RArchetype.WASTE_RECYCLING_INFRA_STAGE2.value,
    "DEMOGRAPHIC_CHILDCARE_STAGE2": E2RArchetype.DEMOGRAPHIC_CHILDCARE_STAGE2.value,
    "PRIVATE_EDUCATION_HAGWON_STAGE2_4C": E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C.value,
}

ROUND294_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "farm_income_order_visibility_confirmed",
    "dealer_inventory_normalization_confirmed",
    "export_order_and_ASP_margin_confirmed",
    "food_input_cost_pass_through_confirmed",
    "volume_retention_after_price_increase_confirmed",
    "same_store_sales_franchise_fee_confirmed",
    "delivery_take_rate_unit_economics_confirmed",
    "labor_service_continuity_confirmed",
    "recycling_yield_gate_fee_utilization_confirmed",
    "cleanup_liability_control_confirmed",
    "childcare_customer_count_ARPU_margin_confirmed",
    "education_enrolment_retention_regulatory_durability_confirmed",
    "price_path_after_evidence",
)

ROUND294_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "farm_equipment_recovery_headline_only",
    "food_input_inflation_as_pricing_power",
    "celebrity_AI_visit_without_restaurant_economics",
    "M&A_scale_without_take_rate_margin",
    "fast_delivery_without_labor_continuity",
    "waste_platform_EV_without_recycling_yield",
    "birthrate_headline_without_customer_count",
    "hagwon_demand_without_policy_and_demographic_check",
)

ROUND294_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "celebrity_visit_photo_moves_food_service_peers",
    "birthrate_headline_baby_education_basket_rally",
    "M&A_bid_headline_food_delivery_premium",
    "waste_infra_EV_headline_listed_readthrough",
    "farm_equipment_recovery_hope_before_global_order_data",
    "food_price_inflation_scored_as_pricing_power",
)

ROUND294_HARD_4C_GATES: tuple[str, ...] = (
    "farm_income_decline_and_dealer_inventory_overhang",
    "input_cost_inflation_without_pass_through",
    "delivery_service_interruption_from_labor_or_regulation",
    "recycling_yield_failure_or_cleanup_liability",
    "temporary_birthrate_rebound_after_echo_boomer_effect",
    "hagwon_regulation_or_child_population_decline",
    "franchisee_profitability_collapse_after_brand_virality",
)

ROUND294_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "food_input_cost_anchor",
    "farm_equipment_cycle_anchor",
    "delivery_deal_anchor",
    "labor_service_anchor",
    "waste_infra_anchor",
    "demographic_anchor",
    "education_demand_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round294ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round294ShadowWeightRow:
    archetype: E2RArchetype
    farm_income_order_visibility: int
    dealer_inventory_normalization: int
    food_input_cost_pass_through: int
    same_store_sales_franchise_fee: int
    delivery_take_rate_unit_economics: int
    labor_service_continuity: int
    recycling_yield_gate_fee_margin: int
    childcare_actual_customer_growth: int
    education_enrolment_retention: int
    policy_regulatory_durability: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "farm_income_order_visibility": _signed(self.farm_income_order_visibility),
            "dealer_inventory_normalization": _signed(self.dealer_inventory_normalization),
            "food_input_cost_pass_through": _signed(self.food_input_cost_pass_through),
            "same_store_sales_franchise_fee": _signed(self.same_store_sales_franchise_fee),
            "delivery_take_rate_unit_economics": _signed(self.delivery_take_rate_unit_economics),
            "labor_service_continuity": _signed(self.labor_service_continuity),
            "recycling_yield_gate_fee_margin": _signed(self.recycling_yield_gate_fee_margin),
            "childcare_actual_customer_growth": _signed(self.childcare_actual_customer_growth),
            "education_enrolment_retention": _signed(self.education_enrolment_retention),
            "policy_regulatory_durability": _signed(self.policy_regulatory_durability),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round294DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round294CaseCandidate:
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
    direct_listed_hard_4c_confirmed: bool
    sector_hard_reference_confirmed: bool
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


ROUND294_SCORE_ADJUSTMENTS: tuple[Round294ScoreAdjustment, ...] = (
    Round294ScoreAdjustment("farm_income_order_visibility", 5, "raise", "농기계는 회복 기대보다 농가소득, dealer inventory, order와 ASP/margin이 먼저다."),
    Round294ScoreAdjustment("dealer_inventory_normalization", 5, "raise", "수출 농기계는 dealer inventory overhang이 풀려야 Stage 3 후보가 된다."),
    Round294ScoreAdjustment("food_input_cost_pass_through", 5, "raise", "식품 원가 상승은 판가 전가와 volume retention 전에는 margin 악재다."),
    Round294ScoreAdjustment("same_store_sales_franchise_fee", 5, "raise", "프랜차이즈 밈은 동일점 매출과 가맹 수수료로 닫혀야 한다."),
    Round294ScoreAdjustment("delivery_take_rate_unit_economics", 5, "raise", "배달앱 M&A는 GMV보다 take-rate, rider cost, merchant churn이 핵심이다."),
    Round294ScoreAdjustment("labor_service_continuity", 5, "raise", "생활물류 moat는 빠른 배송뿐 아니라 노동·규제·운영 연속성이다."),
    Round294ScoreAdjustment("recycling_yield_gate_fee_margin", 5, "raise", "폐기물 인프라는 EV보다 recycling yield, gate fee, utilization, cleanup liability가 중요하다."),
    Round294ScoreAdjustment("childcare_actual_customer_growth", 5, "raise", "출산율 headline은 실제 고객수, ARPU, 보조금 capture와 margin으로 내려와야 한다."),
    Round294ScoreAdjustment("education_enrolment_retention", 5, "raise", "사교육 수요는 등록률, retention, 교사 비용, 규제 내구성으로 검증한다."),
    Round294ScoreAdjustment("headline_only_event", -5, "lower", "유명인 방문, 출산율 headline, M&A headline만으로 Green을 만들지 않는다."),
)


ROUND294_SHADOW_WEIGHT_ROWS: tuple[Round294ShadowWeightRow, ...] = (
    Round294ShadowWeightRow(E2RArchetype.AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH, 5, 5, 1, 0, 0, 1, 0, 0, 0, 3, 0, 4, 4, "Daedong/TYM require farm income, dealer inventory, export orders and ASP/margin confirmation."),
    Round294ShadowWeightRow(E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH, 1, 0, 5, 2, 0, 0, 0, 0, 0, 3, 0, 4, 4, "Food inflation can be margin-negative unless pass-through and volume retention confirm."),
    Round294ShadowWeightRow(E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM, 0, 0, 2, 5, 0, 0, 0, 0, 0, 1, -5, 5, 3, "Jensen fried-chicken rally is meme premium without same-store sales or franchise economics."),
    Round294ShadowWeightRow(E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2, 0, 0, 1, 0, 5, 5, 0, 0, 0, 5, -5, 5, 4, "Baemin M&A needs approval, take-rate, rider cost, merchant churn and integration economics."),
    Round294ShadowWeightRow(E2RArchetype.DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE, 0, 0, 0, 0, 5, 5, 0, 0, 0, 5, 0, 4, 4, "Delivery service moat depends on labor continuity and service reliability."),
    Round294ShadowWeightRow(E2RArchetype.WASTE_RECYCLING_INFRA_STAGE2, 0, 0, 0, 0, 0, 2, 5, 0, 0, 5, -5, 4, 4, "Waste infra needs recycling yield, gate fee, utilization and cleanup liability control."),
    Round294ShadowWeightRow(E2RArchetype.DEMOGRAPHIC_CHILDCARE_STAGE2, 0, 0, 0, 0, 0, 1, 0, 5, 3, 5, -5, 5, 3, "Birthrate rebound is Stage 2 until customer growth and ARPU/margin confirm."),
    Round294ShadowWeightRow(E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C, 0, 0, 0, 0, 0, 1, 0, 2, 5, 5, -4, 4, 3, "Hagwon demand is strong but demographic and regulatory burden remain."),
)


ROUND294_DEEP_SUB_ARCHETYPES: tuple[Round294DeepSubArchetype, ...] = (
    Round294DeepSubArchetype("농기계 수출사이클", E2RArchetype.AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH, ("Daedong", "TYM", "CNH forecast cut", "AGCO recovery reference", "dealer inventory")),
    Round294DeepSubArchetype("식품 원가", E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH, ("CJ CheilJedang", "Pulmuone", "CJ Freshway", "rice +18.6%", "mandarin +26.5%")),
    Round294DeepSubArchetype("치킨 밈 이벤트", E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM, ("Kyochon", "Cherrybro", "Neuromeka", "Jensen Huang", "Kkanbu Chicken")),
    Round294DeepSubArchetype("배달앱 M&A", E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2, ("Naver", "Uber", "Baemin", "Delivery Hero", "8T won bid")),
    Round294DeepSubArchetype("배송 노동 연속성", E2RArchetype.DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE, ("CJ Logistics", "Hanjin", "Coupang", "Rocket Delivery pause", "courier labor")),
    Round294DeepSubArchetype("폐기물/재활용", E2RArchetype.WASTE_RECYCLING_INFRA_STAGE2, ("KJ Environment", "EQT", "plastic recycling", "actual recycling 27%", "cleanup liability")),
    Round294DeepSubArchetype("출산/육아", E2RArchetype.DEMOGRAPHIC_CHILDCARE_STAGE2, ("fertility 0.72 to 0.80", "births +6.8%", "Agabang", "Zero to Seven", "echo-boomer")),
    Round294DeepSubArchetype("사교육/학원", E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C, ("MegaStudy", "Chungdahm", "under-6 hagwon 47.6%", "tuition 332000 KRW", "English kindergarten 1.5M KRW")),
)


ROUND294_CASE_CANDIDATES: tuple[Round294CaseCandidate, ...] = (
    Round294CaseCandidate(
        case_id="r12_loop14_daedong_tym_agri_equipment_export_cycle",
        symbol="000490/002900",
        company_name="Daedong / TYM",
        primary_archetype=E2RArchetype.AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH,
        secondary_archetypes=(E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE, E2RArchetype.AGRI_MACHINERY_EXPORT_CYCLE_KOREA),
        case_type="4b_watch",
        round_case_type="4C-watch",
        stage1_date=date(2024, 5, 1),
        stage2_date=date(2026, 2, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 11, 8),
        stage3_decision="farm_equipment_export_recovery_needs_farm_income_dealer_inventory_orders_ASP_and_margin",
        stage4b_status="4C-watch/agri-equipment-cycle",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=True,
        evidence_fields=("CNH_profit_miss_forecast_cut", "farm_equipment_sales_decline", "AGCO_2026_recovery_reference", "Deere_flat_close"),
        red_flag_fields=("farm_equipment_recovery_headline_only", "dealer_inventory_overhang", "tractor_and_combine_sales_decline"),
        price_data_source="Reuters CNH / Barron's AGCO-Deere global farm-equipment anchors",
        reported_price_anchor="CNH premarket -10%; AGCO +2.2%; Deere -0.3%",
        reported_return_anchor="Global farm-equipment cycle gate; Daedong/TYM direct OHLC unavailable",
        event_mfe_pct=2.2,
        event_mae_pct=-10.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"cnh_premarket_mae_pct": -10, "cnh_prior_eps_view_usd": "1.30-1.40", "cnh_revised_eps_view_usd": "1.05-1.15", "cnh_agriculture_sales_decline_2024_pct": "22-23", "cnh_emea_tractor_sales_decline_pct": -20, "cnh_emea_combine_sales_decline_pct": -50, "agco_2025_north_america_tractor_sales_decline_pct": -10, "agco_2025_combine_sales_decline_pct": -27, "agco_event_mfe_pct": 2.2, "deere_event_close_pct": -0.3, "daedong_tym_direct_ohlc": "price_data_unavailable_after_deep_search"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="global_ag_equipment_slump_not_KR_export_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Korean tractor export thesis needs farm income, dealer inventory, orders, export ASP and margin.",
    ),
    Round294CaseCandidate(
        case_id="r12_loop14_food_input_cost_inflation_basket",
        symbol="097950/017810/051500/food_service_basket",
        company_name="CJ CheilJedang / Pulmuone / CJ Freshway / food-service basket",
        primary_archetype=E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH,
        secondary_archetypes=(E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C, E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK),
        case_type="4b_watch",
        round_case_type="4C-watch",
        stage1_date=date(2025, 12, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 1),
        stage3_decision="food_input_inflation_is_margin_gate_until_pass_through_volume_retention_and_gross_margin_confirm",
        stage4b_status="4C-watch/food-input-cost",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=True,
        evidence_fields=("headline_CPI_2_4pct", "agri_fishery_prices_5_6pct", "rice_18_6pct", "mandarin_26_5pct"),
        red_flag_fields=("food_input_inflation_as_pricing_power", "pass_through_unconfirmed", "volume_retention_unconfirmed"),
        price_data_source="Reuters Korea inflation / food-cost anchor",
        reported_price_anchor="CPI +2.4%; agri/fishery +5.6%; rice +18.6%; mandarin +26.5%",
        reported_return_anchor="Food input-cost shock; company-level OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"headline_cpi_yoy_pct": 2.4, "agri_fishery_price_index_yoy_pct": 5.6, "rice_price_yoy_pct": 18.6, "mandarin_price_yoy_pct": 26.5, "bok_policy_rate_pct": 2.5, "direct_company_ohlc": "price_data_unavailable_after_deep_search"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="AGRI_FOOD_INPUT_COST_4C_WATCH",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="input_cost_inflation_not_food_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Food input inflation is not pricing power unless pass-through, volume retention and margin confirm.",
    ),
    Round294CaseCandidate(
        case_id="r12_loop14_fried_chicken_jensen_huang_meme_rally",
        symbol="339770/066360/348340",
        company_name="Kyochon F&B / Cherrybro / Neuromeka",
        primary_archetype=E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM, E2RArchetype.THEME_VALUATION_OVERHEAT),
        case_type="event_premium",
        round_case_type="price_moved_without_evidence",
        stage1_date=date(2025, 10, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 31),
        stage4c_date=None,
        stage3_decision="celebrity_AI_visit_is_not_food_service_green_without_same_store_sales_franchise_fee_or_margin",
        stage4b_status="4B-watch/meme-event",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=True,
        evidence_fields=("Jensen_Huang_Kkanbu_visit", "Kyochon_plus_20pct", "Cherrybro_plus_30pct", "Kkanbu_not_listed"),
        red_flag_fields=("celebrity_AI_visit_without_restaurant_economics", "direct_revenue_link_unconfirmed", "same_store_sales_unconfirmed"),
        price_data_source="MarketWatch / FT Jensen Huang fried-chicken rally anchors",
        reported_price_anchor="Kyochon +20%; Cherrybro +30%; Neuromeka retained gains by close",
        reported_return_anchor="Meme event moved listed peers without direct economics",
        event_mfe_pct=30.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kyochon_event_mfe_pct": 20, "cherrybro_event_mfe_pct": 30, "neuromeka_retained_gains_by_close": True, "kkanbu_listed": False, "nvidia_korea_ai_chip_deals_context": True, "direct_revenue_link_confirmed": False, "same_store_sales_confirmed": False, "franchise_fee_margin_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_label="FRIED_CHICKEN_MEME_EVENT_PREMIUM",
        stage_failure_type="false_yellow",
        round_stage_failure_label="celebrity_AI_visit_not_food_service_unit_economics",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Celebrity/AI visit moved stocks without same-store sales, royalty, or input-cost margin evidence.",
    ),
    Round294CaseCandidate(
        case_id="r12_loop14_naver_uber_baemin_food_delivery_consolidation",
        symbol="035420/DHER/Baemin_readthrough",
        company_name="Naver / Uber / Baemin / Delivery Hero",
        primary_archetype=E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2,
        secondary_archetypes=(E2RArchetype.PLATFORM_SOFTWARE_INTERNET, E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2),
        case_type="success_candidate",
        round_case_type="success_candidate_stage2",
        stage1_date=date(2025, 11, 13),
        stage2_date=date(2026, 5, 18),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="food_delivery_MA_is_stage2_until_approval_take_rate_rider_cost_merchant_churn_and_integration_economics_close",
        stage4b_status="Stage2/M&A-scale-premium-watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=False,
        evidence_fields=("Korea_orders_returned_to_growth", "quick_commerce_first_quarterly_profit", "Baemin_bid_up_to_8T_won", "Uber_Naver_80_20_split"),
        red_flag_fields=("M&A_scale_without_take_rate_margin", "final_decision_unconfirmed", "regulatory_approval_unconfirmed"),
        price_data_source="Reuters Delivery Hero Korea recovery and Uber/Naver Baemin bid anchors",
        reported_price_anchor="Delivery Hero +5%; Baemin bid up to 8T KRW / $5.34B",
        reported_return_anchor="Consolidation Stage 2; Naver direct event return unavailable",
        event_mfe_pct=5.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"delivery_hero_q3_gmv_eur_bn": 12.2, "delivery_hero_q3_gmv_like_for_like_growth_pct": 7, "asia_gmv_q3_decline_pct": -3, "south_korea_orders_returned_to_growth": True, "quick_commerce_first_quarterly_profit": True, "delivery_hero_event_mfe_pct": 5, "baemin_bid_value_krw_trn": 8, "baemin_bid_value_usd_bn": 5.34, "uber_naver_consortium_split": "80/20", "final_decision_confirmed": False, "naver_direct_event_return": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_deal_stage2",
        rerating_result="policy_event_rerating",
        round_rerating_label="FOOD_DELIVERY_CONSOLIDATION_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="M&A_scale_not_take_rate_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Food-delivery M&A scale needs approval, take-rate, rider cost, merchant churn and integration economics.",
    ),
    Round294CaseCandidate(
        case_id="r12_loop14_delivery_labor_service_continuity_reference",
        symbol="000120/002320/CPNG_readthrough",
        company_name="CJ Logistics / Hanjin / Coupang read-through",
        primary_archetype=E2RArchetype.DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE, E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2),
        case_type="4c_thesis_break",
        round_case_type="service_continuity_reference",
        stage1_date=date(2025, 6, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 6, 3),
        stage3_decision="delivery_service_green_requires_labor_continuity_unit_economics_service_reliability_and_regulation",
        stage4b_status="4C-reference/service-continuity",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=True,
        evidence_fields=("Rocket_Delivery_first_daytime_pause_since_2014", "pause_window_0700_2000", "CJ_Logistics_and_Hanjin_joined_halt", "union_and_activist_pressure"),
        red_flag_fields=("fast_delivery_without_labor_continuity", "delivery_service_interruption", "gig_worker_classification_risk"),
        price_data_source="Reuters delivery-worker election pause anchor",
        reported_price_anchor="Rocket Delivery first daytime pause since 2014; CJ Logistics and Hanjin joined halt",
        reported_return_anchor="Delivery labor continuity reference; direct listed OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"coupang_rocket_delivery_first_pause_since": 2014, "pause_window": "07:00-20:00", "participating_companies": ["Coupang", "CJ Logistics", "Hanjin Logistics"], "trigger": "snap presidential election voting access", "labor_model_risk": ["gig worker classification", "self-employed couriers", "union pressure", "service continuity"], "direct_listed_price_anchor": "price_data_unavailable_after_deep_search"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="delivery_speed_not_green_without_labor_operating_continuity",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Delivery speed moat needs labor continuity, service reliability and unit economics.",
    ),
    Round294CaseCandidate(
        case_id="r12_loop14_waste_recycling_infra_stage2",
        symbol="060150/009440/waste_management_readthrough",
        company_name="Insun ENT / KC Green / KJ Environment read-through",
        primary_archetype=E2RArchetype.WASTE_RECYCLING_INFRA_STAGE2,
        secondary_archetypes=(E2RArchetype.WASTE_RECYCLING_INFRA_PLATFORM_STAGE2, E2RArchetype.WASTE_RECYCLING_ENVIRONMENT),
        case_type="success_candidate",
        round_case_type="success_candidate_stage2 + 4C-watch",
        stage1_date=date(2024, 8, 16),
        stage2_date=date(2024, 8, 16),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 11, 22),
        stage3_decision="waste_infra_EV_is_stage2_until_recycling_yield_gate_fee_utilization_and_cleanup_liability_control_close",
        stage4b_status="Stage2/4C-watch/recycling-yield",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=True,
        evidence_fields=("KJ_Environment_EV_over_1T_won", "catchment_over_50pct_population", "business_lines_recycling_waste_to_energy", "actual_recycling_estimate_27pct"),
        red_flag_fields=("waste_platform_EV_without_recycling_yield", "cleanup_liability", "untreated_plastic_waste"),
        price_data_source="Reuters EQT KJ Environment acquisition and South Korea plastic-waste anchors",
        reported_price_anchor="KJ Environment platform EV >1T KRW; actual recycling estimate 27%; cleanup cost 2-3B KRW",
        reported_return_anchor="Waste infra Stage 2 plus recycling yield and cleanup liability gate",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kj_environment_platform_ev_krw_trn_min": 1.0, "kj_environment_platform_ev_usd_mn": 733, "catchment_population_coverage_pct": 50, "business_lines": ["recyclable waste sorting", "plastic recycling", "waste-to-energy"], "official_plastic_recycling_claim_pct": 73, "greenpeace_actual_recycling_estimate_pct": 27, "plastic_waste_growth_2019_2022_pct": 31, "untreated_plastic_waste_tonnes": 19000, "cleanup_cost_krw_bn": "2-3", "direct_listed_price_anchor": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="WASTE_RECYCLING_INFRA_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="infrastructure_EV_not_recycling_yield_cash_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Waste infra EV is Stage 2; recycling yield, gate fee, utilization and cleanup-liability control are Green gates.",
    ),
    Round294CaseCandidate(
        case_id="r12_loop14_birthrate_childcare_infant_goods_stage2",
        symbol="013990/159910/childcare_infant_goods_basket",
        company_name="Agabang / Zero to Seven / childcare and infant-goods read-through",
        primary_archetype=E2RArchetype.DEMOGRAPHIC_CHILDCARE_STAGE2,
        secondary_archetypes=(E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT, E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT),
        case_type="success_candidate",
        round_case_type="success_candidate_stage2",
        stage1_date=date(2025, 2, 26),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="birthrate_rebound_is_stage2_until_actual_sales_customer_count_enrolment_ARPU_subsidy_and_margin_confirm",
        stage4b_status="4B-watch/demographic-headline",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=True,
        evidence_fields=("fertility_0_72_to_0_75_to_0_80", "births_2025_plus_6_8pct", "marriages_plus_8_1pct", "deaths_exceeded_births_108900"),
        red_flag_fields=("birthrate_headline_without_customer_count", "echo_boomer_effect_watch", "actual_sales_unconfirmed"),
        price_data_source="Reuters birthrate rebound anchors",
        reported_price_anchor="fertility 0.72 -> 0.75 -> 0.80; births +6.8% in 2025",
        reported_return_anchor="Demographic Stage 2, not automatic childcare revenue Green",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fertility_rate_2023": 0.72, "fertility_rate_2024": 0.75, "fertility_rate_2025": 0.80, "births_2024": 238300, "births_2024_growth_pct": 3.6, "births_2025": 254500, "births_2025_growth_pct": 6.8, "marriages_2025_growth_pct": 8.1, "deaths_exceeded_births_2025": 108900, "echo_boomer_effect_watch": True, "direct_listed_price_anchor": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_demographic_stage2",
        rerating_result="policy_event_rerating",
        round_rerating_label="DEMOGRAPHIC_CHILDCARE_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="birthrate_rebound_not_childcare_revenue_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Birthrate rebound is Stage 2; actual sales, customer count, ARPU, subsidy capture and margin required.",
    ),
    Round294CaseCandidate(
        case_id="r12_loop14_private_education_hagwon_demand_stage2",
        symbol="072870/096240/education_service_basket",
        company_name="MegaStudy Education / Chungdahm / private-education basket",
        primary_archetype=E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C,
        secondary_archetypes=(E2RArchetype.EDUCATION_SPECIALTY_SERVICES, E2RArchetype.EDUCATION_POLICY_EVENT_KOREA),
        case_type="success_candidate",
        round_case_type="success_candidate_stage2 + demographic_policy_4C_watch",
        stage1_date=date(2025, 3, 16),
        stage2_date=date(2025, 3, 16),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 16),
        stage3_decision="hagwon_demand_is_stage2_until_enrolment_pricing_retention_teacher_cost_online_margin_and_regulatory_durability_confirm",
        stage4b_status="Stage2/4C-watch/demographic-policy-burden",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        sector_hard_reference_confirmed=True,
        evidence_fields=("under6_hagwon_enrolment_47_6pct", "under2_hagwon_enrolment_25pct", "preschool_tuition_332000_krw", "English_kindergarten_1_5M_krw"),
        red_flag_fields=("hagwon_demand_without_policy_and_demographic_check", "household_burden", "regulatory_durability_unconfirmed"),
        price_data_source="FT under-6 hagwon survey anchor",
        reported_price_anchor="under-6 hagwon 47.6%; under-2 hagwon 25%; preschool tuition 332,000 KRW/month",
        reported_return_anchor="Education-service demand Stage 2 plus social/policy 4C watch",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"under6_hagwon_enrolment_pct": 47.6, "under2_hagwon_enrolment_pct": 25, "preschool_monthly_tuition_avg_krw": 332000, "private_class_hours_per_week_avg": 5.6, "english_kindergarten_monthly_tuition_avg_krw": 1500000, "direct_listed_price_anchor": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="PRIVATE_EDUCATION_HAGWON_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="high_private_education_demand_not_green_if_demographic_policy_burden",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Private education demand is strong but demographic burden and policy/regulatory risk remain.",
    ),
)


def round294_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND294_CASE_CANDIDATES:
        stage3_terms = ("confirmed", "sales", "fee", "take_rate", "yield", "customer", "arpu", "margin", "retention", "fcf")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND294_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round294 R12 Loop-14 agriculture/life-services/misc price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND294_GREEN_REQUIRED_FIELDS) if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(term in field.lower() for term in ("headline", "meme", "event", "premium", "rally", "m&a"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(term in field.lower() for term in ("unconfirmed", "liability", "decline", "interruption", "overhang", "cost", "regulatory", "burden"))),
            must_have_fields=ROUND294_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND294_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "direct_KRX_hard_4c_confirmed_false",
                "sector_hard_reference_confirmed_true",
                "do_not_use_round294_cases_as_candidate_generation_input",
                "do_not_treat_agri_life_service_headline_as_green",
                *ROUND294_GREEN_REQUIRED_FIELDS,
                *ROUND294_GREEN_FORBIDDEN_PATTERNS,
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
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.86 if candidate.stage2_date or candidate.stage4c_date else 0.74,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round294_case_rows() -> tuple[dict[str, str], ...]:
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
            "direct_listed_hard_4c_confirmed": str(candidate.direct_listed_hard_4c_confirmed).lower(),
            "sector_hard_reference_confirmed": str(candidate.sector_hard_reference_confirmed).lower(),
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
        for candidate in ROUND294_CASE_CANDIDATES
    )


def round294_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND294_SCORE_ADJUSTMENTS)


def round294_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND294_SHADOW_WEIGHT_ROWS)


def round294_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND294_DEEP_SUB_ARCHETYPES)


def round294_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round294_price_validation": "true"} for field in ROUND294_PRICE_VALIDATION_FIELDS)


def round294_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round294_label": label, "canonical_archetype": canonical} for label, canonical in ROUND294_REQUIRED_TARGET_ALIASES.items())


def round294_summary() -> dict[str, int | bool | str]:
    cases = ROUND294_CASE_CANDIDATES
    return {
        "source_round": ROUND294_SOURCE_ROUND_PATH,
        "round_id": ROUND294_ANALYST_ROUND_ID,
        "large_sector": ROUND294_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "watch_counterexample_count": sum(1 for case in cases if case.case_type in {"4b_watch", "4c_thesis_break"}),
        "hard_reference_count": sum(1 for case in cases if case.case_type == "4c_thesis_break"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "direct_listed_hard_4c_case_count": sum(1 for case in cases if case.direct_listed_hard_4c_confirmed),
        "sector_hard_reference_count": sum(1 for case in cases if case.sector_hard_reference_confirmed),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "target_archetype_count": len(ROUND294_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND294_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND294_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "direct_KRX_hard_4c_confirmed": False,
        "sector_hard_reference_confirmed": any(case.sector_hard_reference_confirmed for case in cases),
    }


def round294_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND294_SOURCE_ROUND_PATH,
        "round_id": ROUND294_ANALYST_ROUND_ID,
        "large_sector": ROUND294_LARGE_SECTOR,
        "summary": round294_summary(),
        "target_aliases": dict(ROUND294_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND294_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND294_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND294_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND294_HARD_4C_GATES),
        "score_adjustments": list(round294_score_adjustment_rows()),
        "shadow_weights": list(round294_shadow_weight_rows()),
        "deep_sub_archetypes": list(round294_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND294_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round294_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_agri_life_service_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round294_summary_markdown() -> str:
    summary = round294_summary()
    lines = [
        "# Round 294 R12 Loop 14 Agriculture Life Services Misc Price Validation",
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
        f"- watch_counterexample: {summary['watch_counterexample_count']}",
        f"- hard_reference: {summary['hard_reference_count']}",
        f"- direct_KRX_hard_4c_confirmed: {str(summary['direct_KRX_hard_4c_confirmed']).lower()}",
        f"- sector_hard_reference_confirmed: {str(summary['sector_hard_reference_confirmed']).lower()}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND294_CASE_CANDIDATES:
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
            "- Daedong/TYM are agri-equipment export-cycle watch cases until global demand, dealer inventory, order and margin data turn.",
            "- Food input inflation is a margin gate, not automatic pricing power.",
            "- Jensen fried-chicken rally is price moved without evidence because Kkanbu is not listed and same-store sales were absent.",
            "- Baemin/Naver/Uber is Stage 2 until approval, take-rate, rider cost and merchant churn are visible.",
            "- Delivery labor pause is a service-continuity reference for logistics and quick-commerce moats.",
            "- Waste/recycling is Stage 2 plus 4C-watch until yield, gate fee, utilization and cleanup liability close.",
            "- Birthrate and hagwon demand are Stage 2 signals, but Green needs customer count, ARPU, margin, retention and policy durability.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round294_green_gate_review_markdown() -> str:
    lines = [
        "# Round 294 R12 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R12 Stage 3-Green is not `headline is good`. It requires concrete operating numbers. For example, a birthrate rebound becomes useful only when childcare customer count, ARPU and margin appear.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND294_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND294_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND294_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Jensen chicken photo` is not restaurant Green without same-store sales.",
            "- `rice price +18.6%` is not food-company Green before pass-through and margin.",
            "- `Baemin 8T won bid` is Stage 2 until approval and unit economics close.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round294_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 294 R12 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND294_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND294_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "이번 라운드에서는 direct KRX hard 4C를 확정하지 않는다. 대신 sector hard reference를 남겨 다음 가격경로 backfill과 Stage lifecycle 검증에 쓴다.",
            "",
            "## Case Review",
            "",
            "| case | company | 4B status | hard 4C | direct listed hard 4C | sector reference | interpretation |",
            "|---|---|---|---|---|---|---|",
        ]
    )
    for case in ROUND294_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | "
            f"{str(case.hard_4c_confirmed).lower()} | {str(case.direct_listed_hard_4c_confirmed).lower()} | "
            f"{str(case.sector_hard_reference_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round294_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 294 R12 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- direct_KRX_hard_4c_confirmed: false",
        "- sector_hard_reference_confirmed: true",
        "- Do not invent OHLC, stage prices, pass-through, same-store sales, take-rate, recycling yield, customer count, retention, or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND294_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND294_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round294_r12_loop14_reports(
    output_directory: str | Path = ROUND294_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND294_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND294_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round294_case_records(), cases_path),
        "audit": _write_json(round294_audit_payload(), audit_path),
        "summary": output / "round294_r12_loop14_price_validation_summary.md",
        "case_matrix": output / "round294_r12_loop14_case_matrix.csv",
        "target_aliases": output / "round294_r12_loop14_target_aliases.csv",
        "score_adjustments": output / "round294_r12_loop14_score_adjustments.csv",
        "shadow_weights": output / "round294_r12_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round294_r12_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round294_r12_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round294_r12_loop14_green_gate_review.md",
        "price_validation_plan": output / "round294_r12_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round294_r12_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round294_summary_markdown(), encoding="utf-8")
    _write_csv(round294_case_rows(), paths["case_matrix"])
    _write_csv(round294_target_alias_rows(), paths["target_aliases"])
    _write_csv(round294_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round294_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round294_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round294_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round294_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round294_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round294_stage4b_4c_review_markdown(), encoding="utf-8")
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
