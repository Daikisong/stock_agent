"""Round-281 R12 Loop-13 agriculture/life-service/other validation pack.

This module converts ``docs/round/round_281.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: cabbage prices can jump because of a heatwave. That is not food
company Green by itself. Green needs pass-through, inventory/waste control,
gross margin, volume, and cash conversion.
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


ROUND281_SOURCE_ROUND_PATH = "docs/round/round_281.md"
ROUND281_ANALYST_ROUND_ID = "round_209"
ROUND281_LARGE_SECTOR = "AGRICULTURE_LIFE_SERVICE_OTHER"
ROUND281_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation"
ROUND281_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop13_round281.jsonl"
ROUND281_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round281_r12_loop13_agriculture_life_service_other_price_validation_audit.json"

ROUND281_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "FOOD_INFLATION_CLIMATE_INPUT_4C": E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C.value,
    "ANIMAL_FEED_GRAIN_COST_4C": E2RArchetype.ANIMAL_FEED_GRAIN_COST_4C.value,
    "POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK": E2RArchetype.POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK.value,
    "AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY": E2RArchetype.AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY.value,
    "LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2": E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2.value,
    "ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE": E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE.value,
    "WASTE_RECYCLING_INFRA_PLATFORM_STAGE2": E2RArchetype.WASTE_RECYCLING_INFRA_PLATFORM_STAGE2.value,
    "DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT": E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT.value,
    "OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE": E2RArchetype.OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE.value,
}

ROUND281_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "input_cost_pass_through_confirmed",
    "inventory_waste_control_confirmed",
    "gross_margin_stability_confirmed",
    "feed_cost_hedging_confirmed",
    "disease_supply_chain_resilience_confirmed",
    "actual_order_backlog_confirmed",
    "dealer_sellthrough_confirmed",
    "logistics_unit_economics_confirmed",
    "data_trust_service_continuity_confirmed",
    "waste_tipping_fee_utilization_confirmed",
    "enrolment_arpu_retention_confirmed",
    "post_listing_order_book_and_export_margin_confirmed",
    "cash_conversion_confirmed",
    "price_path_after_evidence",
)

ROUND281_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "food_inflation_headline_only",
    "grain_price_event_only",
    "disease_supply_shock_as_benefit_only",
    "aging_farm_theme_only",
    "logistics_revenue_uplift_without_margin",
    "birthrate_headline_without_enrolment",
    "recycling_policy_without_tipping_fee",
    "IPO_size_without_aftermarket_demand",
    "data_breach_or_trust_failure",
)

ROUND281_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "food_or_feed_price_spike_basket_rally_before_pass_through",
    "birthrate_rebound_baby_education_basket_rally",
    "agri_machinery_smart_farm_theme_without_orders",
    "waste_recycling_policy_before_fee_or_utilization",
    "large_IPO_bookbuilding_before_aftermarket_demand",
    "coupang_breach_competitor_benefit_overpriced",
)

ROUND281_HARD_4C_GATES: tuple[str, ...] = (
    "crop_failure_input_cost_spike_without_pass_through",
    "feed_tender_failure_or_grain_shock",
    "bird_flu_or_livestock_disease_import_disruption",
    "data_breach_or_service_trust_failure",
    "logistics_labor_or_delivery_interruption",
    "waste_treatment_permit_loss_or_utilization_collapse",
    "birthrate_rebound_reversal",
    "IPO_weak_debut_or_tariff_export_shock",
)

ROUND281_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "input_cost_anchor",
    "policy_or_demographic_anchor",
    "service_trust_anchor",
    "business_metric_anchor",
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
class Round281ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round281ShadowWeightRow:
    archetype: E2RArchetype
    input_cost_pass_through: int
    inventory_waste_control: int
    feed_cost_hedging: int
    disease_supply_chain_resilience: int
    actual_order_backlog: int
    dealer_sellthrough: int
    logistics_unit_economics: int
    data_trust_service_continuity: int
    waste_tipping_fee_utilization: int
    enrolment_arpu_conversion: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "input_cost_pass_through": _signed(self.input_cost_pass_through),
            "inventory_waste_control": _signed(self.inventory_waste_control),
            "feed_cost_hedging": _signed(self.feed_cost_hedging),
            "disease_supply_chain_resilience": _signed(self.disease_supply_chain_resilience),
            "actual_order_backlog": _signed(self.actual_order_backlog),
            "dealer_sellthrough": _signed(self.dealer_sellthrough),
            "logistics_unit_economics": _signed(self.logistics_unit_economics),
            "data_trust_service_continuity": _signed(self.data_trust_service_continuity),
            "waste_tipping_fee_utilization": _signed(self.waste_tipping_fee_utilization),
            "enrolment_arpu_conversion": _signed(self.enrolment_arpu_conversion),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round281DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round281CaseCandidate:
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


ROUND281_SCORE_ADJUSTMENTS: tuple[Round281ScoreAdjustment, ...] = (
    Round281ScoreAdjustment("input_cost_pass_through", 5, "raise", "농식품 원가 shock 이후 판가 전가가 확인되어야 한다."),
    Round281ScoreAdjustment("inventory_waste_control", 5, "raise", "배추·식품·폐기물은 재고와 폐기 관리가 gross margin을 좌우한다."),
    Round281ScoreAdjustment("feed_cost_hedging", 5, "raise", "사료·축산은 곡물가격 hedge와 재고 buffer가 핵심이다."),
    Round281ScoreAdjustment("disease_supply_chain_resilience", 5, "raise", "bird flu 같은 질병 shock는 수입규제와 공급망 회복을 같이 봐야 한다."),
    Round281ScoreAdjustment("actual_order_backlog", 5, "raise", "농기계와 IPO 제조업은 theme보다 실제 order book이 중요하다."),
    Round281ScoreAdjustment("dealer_sellthrough", 5, "raise", "농기계는 dealer inventory와 North America sell-through가 Stage 3 조건이다."),
    Round281ScoreAdjustment("logistics_unit_economics", 5, "raise", "물류 계약은 물동량, 단가, 자동화, 인건비가 닫혀야 한다."),
    Round281ScoreAdjustment("data_trust_service_continuity", 5, "raise", "생활서비스는 편의성보다 데이터 trust와 서비스 연속성이 먼저다."),
    Round281ScoreAdjustment("waste_tipping_fee_utilization", 5, "raise", "폐기물 인프라는 처리량, tipping fee, utilization, capex 회수를 봐야 한다."),
    Round281ScoreAdjustment("enrolment_ARPU_conversion", 5, "raise", "출산율 headline은 enrolment, ARPU, retention으로 내려와야 한다."),
    Round281ScoreAdjustment("food_inflation_headline_only", -5, "lower", "식품가격 상승 headline만으로 식품주 Green을 만들지 않는다."),
    Round281ScoreAdjustment("grain_price_event_only", -5, "lower", "곡물가격 이벤트는 사료·축산 margin gate다."),
    Round281ScoreAdjustment("disease_supply_shock_as_benefit_only", -5, "lower", "질병 shock를 가격상승 수혜로만 보면 4C risk를 놓친다."),
    Round281ScoreAdjustment("aging_farm_theme_only", -5, "lower", "농촌 고령화 theme만으로 농기계 주문을 만들지 않는다."),
    Round281ScoreAdjustment("logistics_revenue_uplift_without_margin", -5, "lower", "물류 매출 증가 추정은 unit margin 없이는 Stage 2에 그친다."),
    Round281ScoreAdjustment("birthrate_headline_without_enrolment", -5, "lower", "출생률 반등만으로 교육·돌봄 매출을 만들지 않는다."),
    Round281ScoreAdjustment("recycling_policy_without_tipping_fee", -5, "lower", "폐기물 정책 headline은 fee/utilization/FCF 전까지 제한한다."),
    Round281ScoreAdjustment("IPO_size_without_aftermarket_demand", -5, "lower", "IPO 규모는 상장 후 수요와 order book 전까지 품질 증거가 아니다."),
    Round281ScoreAdjustment("data_breach_or_trust_failure", -5, "lower", "데이터 breach는 생활서비스 hard gate다."),
)


ROUND281_SHADOW_WEIGHT_ROWS: tuple[Round281ShadowWeightRow, ...] = (
    Round281ShadowWeightRow(E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C, 5, 5, 0, 2, 0, 0, 1, 1, 0, 0, -5, 5, 4, "Cabbage price spike is input-cost gate unless pass-through and margin hold."),
    Round281ShadowWeightRow(E2RArchetype.ANIMAL_FEED_GRAIN_COST_4C, 5, 4, 5, 3, 0, 0, 1, 1, 0, 0, -5, 5, 4, "Feed wheat tender failure shows grain-cost pressure before margin proof."),
    Round281ShadowWeightRow(E2RArchetype.POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK, 5, 4, 4, 5, 0, 0, 1, 1, 0, 0, -5, 5, 5, "Disease shock needs import rules, flock health, pass-through and margin."),
    Round281ShadowWeightRow(E2RArchetype.AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY, 1, 2, 0, 1, 5, 5, 1, 1, 0, 0, -5, 5, 3, "Daedong/TYM aging-farm theme needs backlog, dealer sell-through, FX and margin."),
    Round281ShadowWeightRow(E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2, 1, 2, 0, 1, 2, 0, 5, 4, 0, 0, -5, 5, 4, "CJ Logistics needs unit economics, automation, wage/fuel cost and volume conversion."),
    Round281ShadowWeightRow(E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE, 0, 1, 0, 0, 0, 0, 5, 5, 0, 0, 0, 4, 5, "Coupang breach confirms trust hard gate for life-service platforms."),
    Round281ShadowWeightRow(E2RArchetype.WASTE_RECYCLING_INFRA_PLATFORM_STAGE2, 0, 5, 0, 0, 2, 0, 2, 2, 5, 0, -5, 4, 4, "Waste/recycling policy needs tipping fee, utilization, permit and FCF."),
    Round281ShadowWeightRow(E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT, 0, 1, 0, 0, 0, 0, 1, 2, 0, 5, -5, 5, 3, "Birthrate rebound needs enrolment, ARPU, retention and margin."),
    Round281ShadowWeightRow(E2RArchetype.OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE, 2, 2, 0, 0, 5, 3, 1, 1, 0, 0, -5, 5, 3, "DN Solutions IPO needs order book, export margin, tariff pass-through and aftermarket demand."),
)


ROUND281_DEEP_SUB_ARCHETYPES: tuple[Round281DeepSubArchetype, ...] = (
    Round281DeepSubArchetype("농산물/식품", E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C, ("napa cabbage", "kimchi input cost", "24,000 tonnes stock release", "9,537 won cabbage", "CJ CheilJedang / Daesang / Pulmuone")),
    Round281DeepSubArchetype("사료/축산", E2RArchetype.ANIMAL_FEED_GRAIN_COST_4C, ("feed wheat tender", "65,000 tonnes", "$300.50/t effective offer", "Black Sea loading ports prohibited", "Harim / Easy Bio")),
    Round281DeepSubArchetype("계육/계란", E2RArchetype.POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK, ("Brazil bird flu", "chicken and egg prices", "import restriction easing", "26% U.S. egg tariff risk")),
    Round281DeepSubArchetype("농기계", E2RArchetype.AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY, ("Daedong", "TYM", "Kioti", "tractors", "North America sell-through")),
    Round281DeepSubArchetype("생활물류", E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2, ("CJ Logistics", "Shinsegae", "SSG.com", "300B won revenue uplift", "unit economics")),
    Round281DeepSubArchetype("생활서비스 trust", E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE, ("Coupang data breach", "34M users", "shares -34%", "Naver users +23%", "CJ Logistics volume +120%")),
    Round281DeepSubArchetype("폐기물/환경", E2RArchetype.WASTE_RECYCLING_INFRA_PLATFORM_STAGE2, ("KJ Environment", "EQT", "food-waste RFID", "96.8% recycling rate", "tipping fee utilization")),
    Round281DeepSubArchetype("저출산/교육", E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT, ("fertility 0.80", "births +6.8%", "marriages +8.1%", "echo-boomer", "enrolment ARPU")),
    Round281DeepSubArchetype("기타 IPO", E2RArchetype.OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE, ("DN Solutions", "1.6T won IPO", "65,000-89,700 won price range", "machine tools", "tariff risk")),
)


ROUND281_CASE_CANDIDATES: tuple[Round281CaseCandidate, ...] = (
    Round281CaseCandidate(
        case_id="r12_loop13_kimchi_cabbage_climate_food_input_cost",
        symbol="097950/001680/017810_food_basket",
        company_name="CJ CheilJedang / Daesang / Pulmuone food-input basket",
        primary_archetype=E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C,
        secondary_archetypes=(E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK, E2RArchetype.FOOD_INPUT_REGULATED_CYCLE),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=date(2024, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 10, 23),
        stage3_decision="crop_price_spike_is_not_food_company_green_until_pass_through_margin_and_cash_conversion_confirm",
        stage4b_status="4C-watch/input-cost",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("government_cabbage_stock_release_24000t", "wholesale_price_9537_krw_per_cabbage", "record_hot_weather_damaged_crop", "selling_price_pass_through_false"),
        red_flag_fields=("food_inflation_headline_only", "crop_failure_input_cost_spike_without_pass_through", "gross_margin_stability_unconfirmed"),
        price_data_source="Reuters cabbage-climate input-cost anchor",
        reported_price_anchor="24,000t stock release; cabbage wholesale price 9,537 KRW in September",
        reported_return_anchor="Food input-cost shock; company-level OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_cabbage_stock_release_tonnes": 24000, "wholesale_price_per_cabbage_krw_september": 9537, "cause": "record hot weather damaged napa cabbage crop", "affected_businesses": ["kimchi processors", "food manufacturers", "restaurant/meal-service operators"], "selling_price_pass_through_confirmed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="food_input_climate_cost_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="crop_price_spike_not_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Food inflation headline is not Green without pass-through and margin stability.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_feed_wheat_tender_livestock_cost_watch",
        symbol="136480/028150/003960_feed_livestock_basket",
        company_name="Harim / Easy Bio / livestock-feed basket",
        primary_archetype=E2RArchetype.ANIMAL_FEED_GRAIN_COST_4C,
        secondary_archetypes=(E2RArchetype.FEED_GRAIN_INPUT_COST_4C, E2RArchetype.AGRI_LIVESTOCK_FOOD_COMMODITY),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=date(2026, 5, 13),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 13),
        stage3_decision="feed_tender_failure_is_margin_gate_until_feed_cost_pass_through_and_conversion_confirm",
        stage4b_status="4C-watch/feed-cost",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("feed_wheat_tender_65000t", "believed_no_purchase", "effective_lowest_offer_300_50_usd_per_tonne", "black_sea_ports_prohibited"),
        red_flag_fields=("grain_price_event_only", "feed_tender_failure_or_grain_shock", "feed_cost_pass_through_unconfirmed"),
        price_data_source="Reuters feed-wheat tender anchor",
        reported_price_anchor="65,000t tender believed no purchase; effective low offer $300.50/t",
        reported_return_anchor="Feed input-cost pressure; company-level OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"tender_volume_tonnes": 65000, "purchase_result": "believed_no_purchase", "lowest_offer_usd_per_tonne": 298.5, "additional_unloading_surcharge_usd_per_tonne": 2.0, "effective_lowest_offer_usd_per_tonne": 300.5, "arrival_target": "2026-08-31", "black_sea_russia_ukraine_loading_ports_prohibited": True, "feed_cost_pass_through_confirmed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="livestock_feed_cost_pressure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="grain_cost_event_not_livestock_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Grain-cost event is a margin gate, not automatic livestock/feed Green.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_poultry_egg_birdflu_supply_shock",
        symbol="136480/003960_poultry_food_basket",
        company_name="Harim / poultry and egg-food processors",
        primary_archetype=E2RArchetype.POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK,
        secondary_archetypes=(E2RArchetype.LIVESTOCK_DISEASE_PRICE_EVENT_KOREA, E2RArchetype.AGRI_DISEASE_EVENT_OVERLAY),
        case_type="event_premium",
        round_case_type="event_premium + 4C-watch",
        stage1_date=date(2025, 5, 1),
        stage2_date=date(2025, 6, 23),
        stage3_date=None,
        stage4b_date=date(2025, 4, 3),
        stage4c_date=date(2025, 6, 9),
        stage3_decision="disease_supply_event_is_two_sided_until_import_rules_flock_health_tariff_and_margin_bridge_confirm",
        stage4b_status="4B-watch/4C-watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("chicken_egg_price_rise", "brazil_bird_flu_import_restriction", "restriction_eased_after_28_days", "us_egg_tariff_risk_26pct"),
        red_flag_fields=("disease_supply_shock_as_benefit_only", "bird_flu_or_livestock_disease_import_disruption", "margin_bridge_unconfirmed"),
        price_data_source="Reuters bird-flu chicken/egg price and import-policy anchors",
        reported_price_anchor="Brazil bird flu drove Korean chicken/egg price concerns; U.S. egg import tariff risk 26%",
        reported_return_anchor="Two-sided disease/tariff case; company-level OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"price_items_flagged": ["instant noodles", "chicken", "eggs"], "brazil_import_restriction": "eased_to_affected_region_only", "brazil_commercial_flock_no_new_outbreak_period_days": 28, "us_south_korea_egg_import_tariff_risk_pct": 26, "us_import_context": "imports from Turkey, Brazil and South Korea to ease bird-flu shortage", "margin_bridge_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4C_watch",
        rerating_result="event_premium",
        round_rerating_label="poultry_egg_supply_shock_two_sided",
        stage_failure_type="false_yellow",
        round_stage_failure_label="disease_supply_event_not_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Disease and import-policy shock can be both price support and cost/regulatory risk.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_daedong_tym_agri_machinery_labor_substitution",
        symbol="000490/002900",
        company_name="Daedong / TYM",
        primary_archetype=E2RArchetype.AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.AGRI_MACHINERY_EXPORT_CYCLE_KOREA, E2RArchetype.AGRI_MACHINERY_AUTONOMOUS_ROBOT_OPTION),
        case_type="success_candidate",
        round_case_type="success_candidate + insufficient_evidence",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="aging_farm_and_labor_substitution_theme_needs_order_backlog_dealer_sellthrough_fx_and_margin",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("listed_agri_machinery_companies", "daedong_kioti_north_america_brand", "tym_more_than_40_countries", "tractors_combines_rice_transplanters"),
        red_flag_fields=("aging_farm_theme_only", "actual_order_backlog_unconfirmed", "north_america_sellthrough_unconfirmed"),
        price_data_source="company-profile / listed-business anchor; no reliable event OHLC located",
        reported_price_anchor="Daedong/TYM products and global presence mapped; event OHLC unavailable",
        reported_return_anchor="Agri automation optionality only",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"daedong_ticker": "000490", "tym_ticker": "002900", "daedong_products": ["tractors", "combines", "forage equipment", "seeding/tillage equipment", "diesel engines"], "daedong_north_america_brand": "Kioti", "tym_products": ["tractors", "combine harvesters", "cultivators", "rice transplanters", "diesel engines"], "tym_country_presence": "more_than_40_countries", "actual_order_backlog_confirmed": False, "north_america_sellthrough_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_evidence",
        rerating_result="unknown",
        round_rerating_label="agri_machinery_labor_substitution_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="aging_farm_theme_not_order_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Aging-farm theme is not Green until orders, dealer inventory, financing cost, FX and margin confirm.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_cj_logistics_shinsegae_alliance_unit_economics",
        symbol="000120",
        company_name="CJ Logistics",
        primary_archetype=E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_LOGISTICS_REPEAT_CONTRACT, E2RArchetype.LOGISTICS_PARCEL_FREIGHT),
        case_type="success_candidate",
        round_case_type="success_candidate + evidence_good_but_price_failed",
        stage1_date=date(2024, 6, 17),
        stage2_date=date(2024, 6, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="revenue_uplift_is_stage2_until_logistics_unit_economics_volume_automation_and_costs_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("shinsegae_ssg_alliance", "annual_revenue_uplift_300bn_won", "three_year_partnership", "event_price_99100_krw"),
        red_flag_fields=("logistics_revenue_uplift_without_margin", "slower_local_growth", "overseas_recovery_delay"),
        price_data_source="MarketWatch / Dow Jones CJ Logistics alliance anchor",
        reported_price_anchor="300B KRW annual revenue uplift estimate; shares -0.2% at 99,100 KRW; target cut 17%",
        reported_return_anchor="Good contract but price failed",
        event_mfe_pct=None,
        event_mae_pct=-0.2,
        stage1_price_anchor=None,
        stage2_price_anchor=99100,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"annual_revenue_uplift_estimate_krw_bn": 300, "partnership_duration_years": 3, "partners": ["Shinsegae Group", "SSG.com"], "target_price_krw": 116000, "target_price_cut_pct": -17, "event_price_krw": 99100, "event_mae_pct": -0.2, "target_upside_from_event_price_pct": 17.1, "issues": ["slower local business growth", "delay in overseas-business recovery"]},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="life_service_logistics_contract_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="revenue_uplift_not_unit_economics_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Revenue uplift estimate is Stage 2; logistics unit economics, automation productivity and cost control required.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_coupang_life_service_trust_break_reference",
        symbol="CPNG/035420/139480/000120_readthrough",
        company_name="Coupang / Naver / E-Mart / CJ Logistics read-through",
        primary_archetype=E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C, E2RArchetype.ECOMMERCE_PLATFORM_DATA_BREACH_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4C_reference + competitor_event_premium",
        stage1_date=date(2025, 11, 1),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 2, 25),
        stage3_decision="life_service_trust_break_is_hard_reference_and_competitor_readthrough_is_not_automatic_green",
        stage4b_status="hard-4C/service-trust",
        hard_4c_confirmed=True,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("affected_users_34mn", "coupang_share_decline_minus_34pct", "mobile_user_activity_minus_3_5pct", "daily_spending_minus_6_3pct", "naver_users_plus_23pct", "cj_logistics_volume_plus_120pct"),
        red_flag_fields=("data_breach_or_trust_failure", "competitor_readthrough_not_green", "earnings_estimate_cut"),
        price_data_source="Reuters Coupang data-breach and competitor read-through anchor",
        reported_price_anchor="34M users affected; Coupang shares down about 34%; spending -6.3%",
        reported_return_anchor="Life-service trust hard reference; competitor read-through is not automatic Green",
        event_mfe_pct=None,
        event_mae_pct=-34,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"affected_users_mn": 34, "exposed_data": ["names", "phone_numbers", "shipping_addresses"], "payment_or_login_data_exposed": False, "government_cause_assessment": "management_failure_rather_than_sophisticated_cyberattack", "coupang_share_decline_since_disclosure_pct": -34, "mobile_user_activity_change_pct": -3.5, "daily_consumer_spending_change_pct": -6.3, "daily_consumer_spending_jan_krw_bn": 139.2, "revenue_estimate_cut_pct": -2.2, "core_earnings_estimate_cut_pct": -6.7, "naver_mobile_users_change_pct": 23, "cj_logistics_overnight_one_day_volume_growth_q4_pct": 120, "direct_korean_competitor_stage3_confirmed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="ecommerce_life_service_trust_hard_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="data_breach_trust_break",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Life-service trust break can move users/spending; competitor read-through is not automatic Green.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_waste_recycling_food_waste_rfid_platform",
        symbol="environmental_services_basket/unlisted_KJ_Environment",
        company_name="KJ Environment / Korean food-waste RFID system",
        primary_archetype=E2RArchetype.WASTE_RECYCLING_INFRA_PLATFORM_STAGE2,
        secondary_archetypes=(E2RArchetype.WASTE_RECYCLING_ENVIRONMENT, E2RArchetype.POLICY_LOCAL_SERVICE_THEME),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_infra",
        stage1_date=date(2024, 8, 16),
        stage2_date=date(2025, 12, 18),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="waste_policy_infra_is_stage2_until_tipping_fee_utilization_permit_capex_recovery_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("kj_environment_platform_ev_over_1tn_won", "food_waste_recycling_rate_96_8pct", "national_rfid_units_150738", "8_54mn_households_served"),
        red_flag_fields=("recycling_policy_without_tipping_fee", "utilization_unconfirmed", "capex_recovery_unconfirmed"),
        price_data_source="Reuters EQT waste-platform anchor + Guardian food-waste RFID policy anchor",
        reported_price_anchor="Platform EV >1T KRW; food-waste recycling 96.8%; national RFID 150,738 units",
        reported_return_anchor="Structural policy infra Stage 2; listed OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kj_environment_platform_ev_krw_trn": 1.0, "kj_environment_platform_ev_usd_mn": 733, "catchment_population_coverage_pct": 50, "business_lines": ["recyclable_waste_sorting", "plastic_recycling", "waste_to_energy"], "food_waste_recycling_rate_2023_pct": 96.8, "food_waste_2023_mn_tonnes": 4.81, "seoul_rfid_units": 27289, "seoul_apartment_resident_coverage_pct": 81.6, "national_rfid_units": 150738, "national_apartment_households_served_mn": 8.54, "seoul_food_waste_decline_decade_pct": -23.9},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_infra",
        rerating_result="policy_event_rerating",
        round_rerating_label="waste_recycling_infra_platform_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="recycling_policy_not_tipping_fee_FCF_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Recycling policy and infra scale are Stage 2; tipping fee, utilization, permit and FCF required.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_birthrate_rebound_childcare_education_event",
        symbol="096240/068930/215200_childcare_education_basket",
        company_name="Childcare / baby / education-service basket",
        primary_archetype=E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT, E2RArchetype.EDUCATION_POLICY_EVENT_KOREA),
        case_type="event_premium",
        round_case_type="event_premium + structural_watch",
        stage1_date=date(2025, 2, 26),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="birthrate_rebound_is_demographic_stage2_until_enrolment_arpu_retention_margin_confirm",
        stage4b_status="4B-watch/demographic-headline",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("fertility_rate_0_80", "births_plus_6_8pct", "marriages_plus_8_1pct", "deaths_exceeded_births_108900"),
        red_flag_fields=("birthrate_headline_without_enrolment", "echo_boomer_temporary_effect_watch", "company_enrolment_ARPU_unconfirmed"),
        price_data_source="Reuters / Guardian birthrate rebound anchors",
        reported_price_anchor="2025 fertility 0.80; births +6.8%; marriages +8.1%",
        reported_return_anchor="Demographic Stage 2, not company Green",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fertility_rate_2023": 0.72, "fertility_rate_2024": 0.75, "fertility_rate_2025": 0.80, "births_2025": 254500, "births_2025_growth_pct": 6.8, "marriage_growth_2025_pct": 8.1, "deaths_exceeded_births_2025": 108900, "policy_plan": "five_year_demographic_response_plan_and_childbirth_incentives", "echo_boomer_temporary_effect_watch": True, "company_enrolment_ARPU_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_structural_watch",
        rerating_result="event_premium",
        round_rerating_label="childcare_education_demographic_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="birthrate_headline_not_enrolment_ARPU_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Birthrate rebound is not company Green until enrolment, ARPU, retention and margin confirm.",
    ),
    Round281CaseCandidate(
        case_id="r12_loop13_dn_solutions_other_manufacturing_tools_ipo",
        symbol="DN_Solutions",
        company_name="DN Solutions",
        primary_archetype=E2RArchetype.OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE,
        secondary_archetypes=(E2RArchetype.EVENT_PRICE_RALLY_NOT_STAGE3, E2RArchetype.TARIFF_IMPORT_MARGIN_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate + IPO_4B_watch",
        stage1_date=date(2025, 4, 14),
        stage2_date=date(2025, 4, 14),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="ipo_bookbuilding_and_end_market_exposure_are_stage2_until_aftermarket_demand_order_book_tariff_margin_and_integration_confirm",
        stage4b_status="4B-watch/IPO-quality-gate",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("ipo_raise_up_to_1_6tn_won", "price_range_65000_89700_krw", "machine_tools_end_markets", "tariff_short_term_risk_acknowledged"),
        red_flag_fields=("IPO_size_without_aftermarket_demand", "tariff_export_risk", "post_listing_order_book_unconfirmed"),
        price_data_source="Reuters DN Solutions IPO anchor + company-profile Heller acquisition reference",
        reported_price_anchor="IPO up to 1.6T KRW / $1.1B; 17.5M shares; price range 65,000-89,700 KRW",
        reported_return_anchor="IPO quality gate; post-listing OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_raise_max_krw_trn": 1.6, "ipo_raise_max_usd_bn": 1.1, "shares_offered_mn": 17.5, "price_range_krw": "65000-89700", "final_price_set_date_planned": "2025-04-30", "listing_planned": "2025-05", "end_markets": ["automotive", "semiconductor", "aerospace", "medical"], "tariff_short_term_risk_acknowledged": True, "heller_acquisition_completed_reference": "2026-01-28"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_IPO_4B_watch",
        rerating_result="unknown",
        round_rerating_label="other_manufacturing_tools_IPO_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="IPO_bookbuilding_not_order_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="IPO size and end-market exposure are Stage 2; listed demand, order book, export margin and tariff pass-through required.",
    ),
)


def round281_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND281_CASE_CANDIDATES:
        stage3_terms = ("pass_through", "gross_margin", "order_backlog", "sellthrough", "unit_economics", "trust", "tipping_fee", "enrolment", "arpu", "cash", "fcf", "order_book")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND281_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round281 R12 Loop-13 agriculture/life-service/other price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND281_GREEN_REQUIRED_FIELDS) if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(term in field.lower() for term in ("event", "headline", "ipo", "theme", "rally", "competitor"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(term in field.lower() for term in ("failure", "breach", "shock", "4c", "unconfirmed", "risk", "cost", "disease"))),
            must_have_fields=ROUND281_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "failed_rerating", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND281_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "hard_4c_confirmed_true_for_life_service_trust_reference",
                "direct_listed_hard_4c_confirmed_false",
                "do_not_use_round281_cases_as_candidate_generation_input",
                "do_not_treat_agri_food_life_service_demographic_waste_or_ipo_headline_as_green",
                *ROUND281_GREEN_REQUIRED_FIELDS,
                *ROUND281_GREEN_FORBIDDEN_PATTERNS,
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
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.86 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round281_case_rows() -> tuple[dict[str, str], ...]:
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
        for candidate in ROUND281_CASE_CANDIDATES
    )


def round281_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND281_SCORE_ADJUSTMENTS)


def round281_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND281_SHADOW_WEIGHT_ROWS)


def round281_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND281_DEEP_SUB_ARCHETYPES)


def round281_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round281_price_validation": "true"} for field in ROUND281_PRICE_VALIDATION_FIELDS)


def round281_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round281_label": label, "canonical_archetype": canonical} for label, canonical in ROUND281_REQUIRED_TARGET_ALIASES.items())


def round281_summary() -> dict[str, int | bool | str]:
    cases = ROUND281_CASE_CANDIDATES
    return {
        "source_round": ROUND281_SOURCE_ROUND_PATH,
        "round_id": ROUND281_ANALYST_ROUND_ID,
        "large_sector": ROUND281_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_reference_count": sum(1 for case in cases if case.case_type == "4c_thesis_break"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "direct_listed_hard_4c_case_count": sum(1 for case in cases if case.direct_listed_hard_4c_confirmed),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND281_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND281_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND281_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "direct_listed_hard_4c_confirmed": any(case.direct_listed_hard_4c_confirmed for case in cases),
    }


def round281_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND281_SOURCE_ROUND_PATH,
        "round_id": ROUND281_ANALYST_ROUND_ID,
        "large_sector": ROUND281_LARGE_SECTOR,
        "summary": round281_summary(),
        "target_aliases": dict(ROUND281_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND281_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND281_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND281_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND281_HARD_4C_GATES),
        "score_adjustments": list(round281_score_adjustment_rows()),
        "shadow_weights": list(round281_shadow_weight_rows()),
        "deep_sub_archetypes": list(round281_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND281_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round281_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_agri_food_life_service_demographic_waste_or_ipo_headline_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round281_summary_markdown() -> str:
    summary = round281_summary()
    lines = [
        "# Round 281 R12 Loop 13 Agriculture Life Service Other Price Validation",
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
        f"- hard_reference: {summary['hard_reference_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- direct_listed_hard_4c: {summary['direct_listed_hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND281_CASE_CANDIDATES:
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
            "- Cabbage and feed wheat are input-cost gates, not automatic food or livestock winners.",
            "- Poultry/egg shortage is two-sided because disease, import rules and tariff risk travel with the price spike.",
            "- Daedong/TYM need order backlog and dealer sell-through before Stage 3 review.",
            "- CJ Logistics has Stage 2 contract evidence, but unit economics and margin remain open.",
            "- Coupang is the R12 life-service trust hard reference; competitor read-through is not automatic Green.",
            "- Waste/RFID and birthrate are Stage 2 policy/demographic evidence until fee, utilization, enrolment, ARPU and FCF close.",
            "- DN Solutions IPO is a quality gate; IPO size is not aftermarket demand or margin evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round281_green_gate_review_markdown() -> str:
    lines = [
        "# Round 281 R12 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R12 Stage 3-Green is not `food inflation`, `birthrate rebound`, `waste policy`, `logistics alliance`, `agri automation theme`, or `IPO size`. It requires pass-through, volume, utilization, trust, enrolment, order backlog, margin, FCF, and price-after-evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND281_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND281_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND281_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `cabbage price spike` is a cost gate until pass-through and margin hold.",
            "- `CJ Logistics revenue uplift` is Stage 2 until unit economics and automation productivity are visible.",
            "- `birthrate rebound` is not education/childcare Green until enrolment, ARPU and retention appear.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round281_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 281 R12 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND281_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND281_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | direct listed hard 4C | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND281_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | "
            f"{str(case.hard_4c_confirmed).lower()} | {str(case.direct_listed_hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round281_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 281 R12 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- direct_listed_hard_4c_confirmed: false",
        "- Do not invent OHLC, stage prices, pass-through, utilization, trust recovery, enrolment, order backlog, IPO aftermarket demand, or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND281_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND281_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round281_r12_loop13_reports(
    output_directory: str | Path = ROUND281_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND281_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND281_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round281_case_records(), cases_path),
        "audit": _write_json(round281_audit_payload(), audit_path),
        "summary": output / "round281_r12_loop13_price_validation_summary.md",
        "case_matrix": output / "round281_r12_loop13_case_matrix.csv",
        "target_aliases": output / "round281_r12_loop13_target_aliases.csv",
        "score_adjustments": output / "round281_r12_loop13_score_adjustments.csv",
        "shadow_weights": output / "round281_r12_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round281_r12_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round281_r12_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round281_r12_loop13_green_gate_review.md",
        "price_validation_plan": output / "round281_r12_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round281_r12_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round281_summary_markdown(), encoding="utf-8")
    _write_csv(round281_case_rows(), paths["case_matrix"])
    _write_csv(round281_target_alias_rows(), paths["target_aliases"])
    _write_csv(round281_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round281_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round281_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round281_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round281_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round281_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round281_stage4b_4c_review_markdown(), encoding="utf-8")
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
