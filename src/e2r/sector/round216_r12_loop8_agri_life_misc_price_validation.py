"""Round-216 R12 Loop-8 agriculture/life-service/misc price validation pack.

Round 216 is calibration/evaluation material only. It structures
``docs/round/round_216.md`` into R12 case records, reported anchors, and
shadow scoring notes.

Easy example: Coway's rental account base can become real structural evidence,
but a viral fried-chicken dinner can only route a watch/event case. The first
can move toward Stage 3 after churn, ARPU, OPM, FCF, and price-path evidence;
the second stays event premium until store traffic, repeat demand, margin, and
cash conversion are visible.
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


ROUND216_SOURCE_ROUND_PATH = "docs/round/round_216.md"
ROUND216_LARGE_SECTOR = Round10LargeSector.EDUCATION_LIFE_AGRI_MISC
ROUND216_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round216_r12_loop8_agri_life_misc_price_validation"
ROUND216_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop8_round216.jsonl"
ROUND216_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round216_r12_loop8_agri_life_misc_price_validation_audit.json"
ROUND216_DEFAULT_STAGE3_BIAS = "conservative_except_recurring_service"

ROUND216_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HOME_LIVING_APPLIANCE_RENTAL": E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL.value,
    "AGRI_MACHINERY_DEMAND_CYCLE": E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE.value,
    "AGRI_MACHINERY_SOFTWARE_LOCKIN": E2RArchetype.AGRI_MACHINERY_SOFTWARE_LOCKIN.value,
    "EDUCATION_SPECIALTY_SERVICES": E2RArchetype.EDUCATION_SPECIALTY_SERVICES.value,
    "HOME_CHILD_EDUCATION": E2RArchetype.HOME_CHILD_EDUCATION.value,
    "EDTECH_AI_DISRUPTION": E2RArchetype.EDTECH_AI_DISRUPTION.value,
    "EDUCATION_POLICY_EVENT": E2RArchetype.EDUCATION_POLICY_EVENT.value,
    "LIVESTOCK_DISEASE_PRICE_REGULATORY": E2RArchetype.LIVESTOCK_DISEASE_PRICE_REGULATORY.value,
    "AGRI_DISEASE_EVENT_OVERLAY": E2RArchetype.AGRI_DISEASE_EVENT_OVERLAY.value,
    "FOOD_SERVICE_EVENT_PREMIUM": E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM.value,
    "SMART_FARM_AGRI_TECH": E2RArchetype.SMART_FARM_AGRI_TECH.value,
    "VERTICAL_FARMING_UNIT_ECONOMICS": E2RArchetype.VERTICAL_FARMING_UNIT_ECONOMICS.value,
    "CONSUMER_REGULATED_PRODUCT": E2RArchetype.CONSUMER_REGULATED_PRODUCT.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND216_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "recurring_revenue_or_repeat_purchase_confirmed",
    "churn_or_retention_stable",
    "arpu_or_price_pass_through_confirmed",
    "unit_economics_positive",
    "cash_conversion_confirmed",
    "inventory_and_receivables_stable",
    "regulatory_risk_passed",
    "subsidy_dependency_low",
    "price_path_after_evidence",
)

ROUND216_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_news_only",
    "disease_event_only",
    "import_ban_event_only",
    "smart_farm_theme_only",
    "agri_machinery_export_theme_only",
    "education_policy_expectation_only",
    "celebrity_food_event_only",
    "defensive_theme_only",
    "same_day_theme_basket_rally_only",
)

ROUND216_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "education_smart_farm_agri_policy_basket_rally",
    "poultry_disease_event_basket_rally",
    "celebrity_or_viral_food_event_basket_rally",
    "defensive_dividend_frame_multiple_expansion",
    "rental_or_regulated_consumer_multiple_before_growth",
    "medical_quota_policy_priced_before_student_arpu",
)

ROUND216_HARD_4C_GATES: tuple[str, ...] = (
    "recall_or_product_safety_issue",
    "churn_spike",
    "arpu_decline",
    "dealer_inventory_build",
    "farmer_financing_stress",
    "education_policy_reversal",
    "private_education_regulation",
    "birth_rate_demand_collapse",
    "import_ban_reversal",
    "disease_event_cleared",
    "celebrity_event_fade",
    "regulatory_ban_or_youth_safety_restriction",
    "subsidy_withdrawal",
    "unit_economics_failure",
    "cash_conversion_deterioration",
)

ROUND216_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "reported_event_mfe_1d_range",
    "reported_event_mfe_1d_midpoint",
    "quota_original",
    "quota_2027",
    "quota_2030",
    "quota_increase_pct",
    "event_duration_days",
    "uav_counting_accuracy",
    "uav_weight_estimation_accuracy",
    "business_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round216ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "axis": self.axis,
            "points": str(self.points),
            "direction": self.direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round216ShadowWeightRow:
    archetype: E2RArchetype
    recurring_revenue: int
    churn_stability: int
    arpu_or_price_pass_through: int
    unit_economics: int
    cash_conversion: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "recurring_revenue": _signed_int_text(self.recurring_revenue),
            "churn_stability": _signed_int_text(self.churn_stability),
            "arpu_or_price_pass_through": _signed_int_text(self.arpu_or_price_pass_through),
            "unit_economics": _signed_int_text(self.unit_economics),
            "cash_conversion": _signed_int_text(self.cash_conversion),
            "event_penalty": _signed_int_text(self.event_penalty),
            "4b_watch_sensitivity": _signed_int_text(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed_int_text(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round216DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {
            "category": self.category,
            "primary_archetype": self.primary_archetype.value,
            "terms": "|".join(self.terms),
        }


@dataclass(frozen=True)
class Round216CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
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
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND216_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND216_SCORE_ADJUSTMENTS: tuple[Round216ScoreAdjustment, ...] = (
    Round216ScoreAdjustment("recurring_revenue", 5, "raise", "R12 Green에 가장 가까운 증거는 반복 매출이다."),
    Round216ScoreAdjustment("churn_stability", 5, "raise", "렌탈·교육·서비스는 churn 안정성이 visibility를 만든다."),
    Round216ScoreAdjustment("ARPU_or_repeat_course", 4, "raise", "ARPU나 반복 수강 매출이 정책 이벤트를 숫자로 연결한다."),
    Round216ScoreAdjustment("cash_conversion", 5, "raise", "반복매출도 현금전환이 확인되어야 Stage 3 후보가 된다."),
    Round216ScoreAdjustment("unit_economics", 5, "raise", "스마트팜·렌탈·생활서비스는 unit economics가 핵심 splitter다."),
    Round216ScoreAdjustment("commercial_installation", 4, "raise", "스마트팜은 정책보다 상업 설치와 운영계약을 우선한다."),
    Round216ScoreAdjustment("service_contract_visibility", 4, "raise", "유지보수·서비스 계약은 일회성 하드웨어 매출보다 강하다."),
    Round216ScoreAdjustment("dealer_sell_through", 4, "raise", "농기계는 딜러 재고가 아니라 실제 sell-through가 중요하다."),
    Round216ScoreAdjustment("inventory_quality", 4, "raise", "재고와 매출채권 안정은 R12 false positive를 줄인다."),
    Round216ScoreAdjustment("regulatory_pass", 4, "raise", "규제 소비재는 규제 통과와 허용 범위 확인이 필요하다."),
    Round216ScoreAdjustment("pricing_power_after_input_cost", 4, "raise", "원가 상승 후 가격전가가 확인되어야 한다."),
    Round216ScoreAdjustment("defensive_theme_only", -5, "lower", "방어주라는 이유만으로 Stage 3를 만들지 않는다."),
    Round216ScoreAdjustment("education_policy_only", -5, "lower", "교육정책은 routing 증거이며 수강생·ARPU 전 Green이 아니다."),
    Round216ScoreAdjustment("agri_cycle_only", -4, "lower", "농기계 수출·사이클만으로 구조적 visibility를 주지 않는다."),
    Round216ScoreAdjustment("smart_farm_policy_only", -5, "lower", "스마트팜 정책/AI농업 narrative는 설치·수주 전 Stage 1이다."),
    Round216ScoreAdjustment("disease_event_only", -5, "lower", "질병 이벤트는 단기 MFE용이며 반복수요가 아니다."),
    Round216ScoreAdjustment("celebrity_food_event_only", -5, "lower", "유명인/바이럴 외식 이벤트는 매출 증거가 아니다."),
    Round216ScoreAdjustment("import_ban_event_only", -4, "lower", "수입금지 뉴스는 완화되면 event fade가 될 수 있다."),
    Round216ScoreAdjustment("unconfirmed_export_theme", -3, "lower", "수출 기대는 sell-through와 OPM 전까지 제한한다."),
    Round216ScoreAdjustment("dealer_inventory_unknown", -4, "lower", "농기계 딜러 재고가 확인되지 않으면 visibility를 낮춘다."),
    Round216ScoreAdjustment("subsidy_dependent_unit_economics", -4, "lower", "보조금 의존 unit economics는 Green blocker다."),
    Round216ScoreAdjustment("regulated_product_without_growth", -3, "lower", "규제소비재 현금흐름은 성장·환원 없이 re-rating이 제한된다."),
)

ROUND216_SHADOW_WEIGHT_ROWS: tuple[Round216ShadowWeightRow, ...] = (
    Round216ShadowWeightRow(E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL, 5, 5, 4, 4, 5, -2, 3, 4, "Coway-like rental service can become Green-capable only after churn, ARPU, OPM, FCF, and price-path checks."),
    Round216ShadowWeightRow(E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE, 1, 0, 1, 3, 2, -4, 4, 4, "Daedong/TYM export story needs dealer sell-through, inventory, farmer financing, OPM, and FCF."),
    Round216ShadowWeightRow(E2RArchetype.EDUCATION_SPECIALTY_SERVICES, 2, 2, 4, 2, 3, -5, 4, 4, "Medical-quota policy is routing evidence until actual students, repeat courses, ARPU, and OPM appear."),
    Round216ShadowWeightRow(E2RArchetype.EDTECH_AI_DISRUPTION, 0, 0, 0, 0, 0, -5, 4, 5, "Classroom phone/device policy is directionally ambiguous and can be RedTeam evidence."),
    Round216ShadowWeightRow(E2RArchetype.LIVESTOCK_DISEASE_PRICE_REGULATORY, 1, 0, 3, 1, 2, -5, 5, 5, "Bird-flu import bans are one-off until volume, pricing, feed cost, inventory, and margin confirm."),
    Round216ShadowWeightRow(E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM, 0, 0, 0, 0, 0, -5, 5, 4, "Celebrity food events are price-moved-without-evidence unless store traffic and repeat demand are visible."),
    Round216ShadowWeightRow(E2RArchetype.SMART_FARM_AGRI_TECH, 1, 0, 1, 5, 3, -5, 4, 5, "Smart-farm papers or policy need commercial installation, service revenue, unit economics, and FCF."),
    Round216ShadowWeightRow(E2RArchetype.CONSUMER_REGULATED_PRODUCT, 2, 1, 4, 1, 4, -3, 3, 5, "KT&G-like regulated cash flow needs shareholder return, HNB/global growth, and regulation/volume checks."),
)

ROUND216_DEEP_SUB_ARCHETYPES: tuple[Round216DeepSubArchetype, ...] = (
    Round216DeepSubArchetype("렌탈 / 생활서비스", E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL, ("Coway", "water purifier rental", "air purifier / bidet / mattress rental", "Malaysia / overseas subsidiaries", "recurring account base", "churn / ARPU / service network", "product safety / recall risk")),
    Round216DeepSubArchetype("농기계", E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE, ("Daedong / KIOTI", "TYM", "North America tractor channel", "dealer sell-through", "inventory / financing", "autonomous tractor / precision agriculture", "export cycle")),
    Round216DeepSubArchetype("교육", E2RArchetype.EDUCATION_SPECIALTY_SERVICES, ("MegaStudy Education", "medical school quota policy", "repeat course / ARPU", "phone ban / edtech friction", "AI education disruption", "birth-rate structural decline")),
    Round216DeepSubArchetype("축산 / 생활 이벤트", E2RArchetype.LIVESTOCK_DISEASE_PRICE_REGULATORY, ("Brazil bird flu", "import restriction / easing", "Harim / Maniker / poultry basket", "Kyochon / chicken franchise event", "one-off disease demand", "celebrity / viral food event")),
    Round216DeepSubArchetype("스마트팜", E2RArchetype.SMART_FARM_AGRI_TECH, ("Green Plus / Woomdungi Farm", "greenhouse automation", "adoption barrier", "government subsidy", "unit economics", "maintenance / recurring service")),
)

ROUND216_CASE_CANDIDATES: tuple[Round216CaseCandidate, ...] = (
    Round216CaseCandidate(
        case_id="r12_loop8_coway_recurring_rental_service_candidate",
        symbol="021240",
        company_name="코웨이",
        primary_archetype=E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL,
        secondary_archetypes=(),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="recurring_rental_service_can_promote_only_after_account_growth_churn_arpu_opm_fcf_and_price_path_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("water_purifier_air_bidet_mattress_rental", "recurring_account_base", "malaysia_overseas_subsidiaries", "domestic_largest_water_purifier_profile"),
        red_flag_fields=("latest_ir_unverified", "churn_unverified", "arpu_unverified", "fcf_conversion_unverified", "product_safety_recall_watch", "overseas_growth_slowdown_watch", "capital_allocation_governance_watch"),
        price_data_source="Public company profile / Yahoo-reference summary only",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="No reliable event price anchor found",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"known_business_anchor": "domestic_largest_water_purifier_company; global_subsidiaries_present; rental_service_recurring_model"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="R12에서 가장 구조적인 후보지만 Green은 렌탈 계정, churn, ARPU, OPM, FCF 확인 뒤에만 가능하다.",
    ),
    Round216CaseCandidate(
        case_id="r12_loop8_daedong_tym_agri_machinery_export_watch",
        symbol="000490/002900",
        company_name="대동 / TYM",
        primary_archetype=E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE,
        secondary_archetypes=(E2RArchetype.AGRI_MACHINERY_SOFTWARE_LOCKIN,),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="export_and_autonomous_tractor_theme_blocked_until_dealer_sell_through_inventory_farmer_financing_opm_fcf_and_software_attach_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("kioti_north_america_channel", "tym_40_plus_country_business", "tractor_combine_utv_engine_business", "autonomous_tractor_precision_agriculture_expectation"),
        red_flag_fields=("unconfirmed_export_theme", "dealer_inventory_unknown", "farmer_financing_unverified", "agri_cycle_only", "opm_fcf_unverified"),
        price_data_source="Public company profile evidence only",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="No reliable event price anchor found",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"business_anchor": "Daedong_KIOTI; TYM_40_plus_countries; tractor_combine_engine_business"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="unknown",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="농기계는 export theme보다 dealer sell-through, inventory, financing, OPM, FCF를 우선한다.",
    ),
    Round216CaseCandidate(
        case_id="r12_loop8_megastudy_medical_quota_policy_event",
        symbol="215200",
        company_name="메가스터디교육",
        primary_archetype=E2RArchetype.EDUCATION_SPECIALTY_SERVICES,
        secondary_archetypes=(E2RArchetype.EDUCATION_POLICY_EVENT, E2RArchetype.HOME_CHILD_EDUCATION),
        case_type="event_premium",
        stage1_date=None,
        stage2_date=date(2025, 3, 7),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="medical_quota_policy_is_routing_until_student_growth_repeat_course_arpu_opm_and_cash_conversion_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("medical_school_quota_policy", "quota_3058_to_3548_to_3871", "private_education_demand_expectation", "policy_direction_changed"),
        red_flag_fields=("education_policy_expectation_only", "education_policy_reversal", "private_education_regulation_watch", "birth_rate_demand_collapse_watch"),
        price_data_source="Reuters / AP policy evidence",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="Quota 3,058 -> 3,548 -> 3,871; no stock anchor",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "original_quota": 3058.0,
            "quota_2027": 3548.0,
            "quota_increase_2027": 490.0,
            "quota_increase_2027_pct": 16.0,
            "quota_2030": 3871.0,
            "quota_increase_2030_vs_original": 813.0,
            "quota_increase_2030_pct": 26.6,
        },
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="교육정책은 routing이고 실제 수강생, repeat course, ARPU, OPM 전에는 Stage 3가 아니다.",
    ),
    Round216CaseCandidate(
        case_id="r12_loop8_edtech_phone_ban_policy_watch",
        symbol="NE/YBM/WJ_basket",
        company_name="교육·에듀테크 basket",
        primary_archetype=E2RArchetype.EDTECH_AI_DISRUPTION,
        secondary_archetypes=(E2RArchetype.HOME_CHILD_EDUCATION, E2RArchetype.EDUCATION_POLICY_EVENT),
        case_type="4b_watch",
        stage1_date=date(2025, 8, 27),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="classroom_phone_ban_is_policy_overlay_until_company_revenue_path_is_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("classroom_phone_digital_device_ban_from_2026_03", "education_policy_edtech_friction", "student_social_media_survey"),
        red_flag_fields=("education_policy_expectation_only", "policy_directionality_unclear", "company_revenue_impact_unverified", "edtech_ai_disruption_watch"),
        price_data_source="Reuters policy evidence",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="37% daily-life impact survey; 22% anxiety without social media",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"law_effective_date": "2026-03", "students_social_media_daily_life_impact_pct": 37.0, "students_anxious_without_social_media_pct": 22.0},
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="unknown",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="같은 정책도 오프라인 학원에는 우호적, 에듀테크에는 악재일 수 있어 회사별 매출경로 전 Green 금지다.",
    ),
    Round216CaseCandidate(
        case_id="r12_loop8_poultry_brazil_bird_flu_import_ban_event",
        symbol="Harim/Maniker/Cherrybro_basket",
        company_name="Poultry basket",
        primary_archetype=E2RArchetype.LIVESTOCK_DISEASE_PRICE_REGULATORY,
        secondary_archetypes=(E2RArchetype.AGRI_DISEASE_EVENT_OVERLAY, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        stage1_date=date(2025, 5, 19),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 5, 19),
        stage4c_date=date(2025, 6, 23),
        stage3_decision="bird_flu_import_ban_blocked_until_company_price_volume_feed_cost_inventory_and_opm_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("brazil_bird_flu_import_restriction", "domestic_poultry_substitution_theme", "brazil_2024_poultry_exports_over_5m_tons", "restriction_easing_after_35_days"),
        red_flag_fields=("disease_event_only", "import_ban_event_only", "import_ban_reversal", "one_off_disease_event", "feed_cost_unverified", "margin_unverified"),
        price_data_source="Reuters import restriction / easing evidence",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="Brazil ban -> Korea easing in 35 calendar days",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"brazil_2024_poultry_exports_mn_tons": 5.0, "event_duration_days": 35.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="축산 질병 이벤트는 Stage 1이며 판매량, 가격전가, feed cost, OPM 확인 전 Stage 3 금지다.",
    ),
    Round216CaseCandidate(
        case_id="r12_loop8_kyochon_chicken_celebrity_food_event",
        symbol="Kyochon/Cherrybro/Neuromeka_basket",
        company_name="Kyochon F&B / chicken-event basket",
        primary_archetype=E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.EVENT_PREMIUM),
        case_type="overheat",
        stage1_date=date(2025, 10, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 31),
        stage4c_date=None,
        stage3_decision="celebrity_food_viral_event_is_4b_event_premium_until_store_traffic_same_store_sales_franchise_margin_repeat_demand_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("jensen_huang_chicken_dinner_viral_event", "fried_chicken_basket_intraday_20_to_30pct", "robot_chicken_side_theme"),
        red_flag_fields=("celebrity_food_event_only", "viral_food_story", "same_day_theme_basket_rally_only", "price_rally_before_company_evidence"),
        price_data_source="Tom's Hardware / Bloomberg-reported event summary",
        reported_price_anchor="Event-day return range only; no raw close OHLC",
        reported_return_anchor="Fried-chicken basket +20% to +30%; midpoint +25%",
        mfe_1d=25.0,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"reported_event_mfe_1d_low_pct": 20.0, "reported_event_mfe_1d_high_pct": 30.0, "reported_event_mfe_1d_midpoint_pct": 25.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="유명인/바이럴 외식 이벤트는 매출 evidence가 아니라 price_moved_without_evidence다.",
    ),
    Round216CaseCandidate(
        case_id="r12_loop8_smart_farm_unit_economics_watch",
        symbol="GreenPlus/Woomdungi_basket",
        company_name="스마트팜 basket",
        primary_archetype=E2RArchetype.SMART_FARM_AGRI_TECH,
        secondary_archetypes=(E2RArchetype.VERTICAL_FARMING_UNIT_ECONOMICS,),
        case_type="event_premium",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="smart_farm_policy_and_technology_papers_blocked_until_commercial_installation_order_backlog_maintenance_revenue_unit_economics_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("smart_farm_ai_agriculture_narrative", "adoption_barrier_research", "greenhouse_uav_yield_estimation_research"),
        red_flag_fields=("smart_farm_theme_only", "subsidy_dependent_unit_economics", "commercial_installation_unverified", "maintenance_revenue_unverified", "unit_economics_unverified"),
        price_data_source="arXiv smart-farm adoption / greenhouse UAV evidence",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="UAV counting accuracy 94.4%; weight-estimation accuracy 87.5%; no stock anchor",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"uav_greenhouse_counting_accuracy_pct": 94.4, "uav_weight_estimation_accuracy_pct": 87.5, "flight_distance_m": 13.2, "flight_time_seconds": 10.5},
        score_price_alignment="unknown",
        rerating_result="no_rerating",
        stage_failure_type="unknown",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="스마트팜은 정책/논문보다 상업 설치, 유지보수 계약, unit economics, FCF 확인이 먼저다.",
    ),
    Round216CaseCandidate(
        case_id="r12_loop8_ktng_regulated_consumer_cashflow_watch",
        symbol="033780",
        company_name="KT&G",
        primary_archetype=E2RArchetype.CONSUMER_REGULATED_PRODUCT,
        secondary_archetypes=(E2RArchetype.CONSUMER_REGULATED_PRODUCT_KOREA, E2RArchetype.NICOTINE_ALTERNATIVE_REGULATED),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="regulated_cashflow_candidate_deferred_until_shareholder_return_hnb_growth_global_sales_volume_regulation_and_fcf_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("regulated_consumer_cashflow", "tobacco_ginseng_business", "2024_revenue_about_5_9tn_won", "shareholder_return_expectation"),
        red_flag_fields=("regulated_product_without_growth", "volume_decline_watch", "tobacco_tax_or_regulation_watch", "hnb_competition_watch", "source_confidence_medium_low"),
        price_data_source="Public company profile evidence only",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="No reliable event price anchor found",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"reported_2024_revenue_krw_tn_lower_confidence": 5.9, "source_confidence": "medium_low"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="규제소비재 cashflow 후보지만 최신 배당·소각·HNB 성장·volume decline·규제 리스크 확인 전 Stage 3 보류다.",
    ),
)


def round216_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND216_CASE_CANDIDATES:
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
                "Round216 R12 Loop-8 agriculture, life service, education, "
                "smart-farm, disease, food-event, and regulated-consumer "
                "price-path validation case. Calibration-only."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "policy" in field
                or "event" in field
                or "theme" in field
                or "rental" in field
                or "cashflow" in field
                or "restriction" in field
                or "narrative" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "recurring" in field
                or "account" in field
                or "cashflow" in field
                or "revenue" in field
                or "installation" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field
                or "rally" in field
                or "theme" in field
                or "policy" in field
                or "viral" in field
                or "price" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "reversal" in field
                or "fade" in field
                or "decline" in field
                or "regulation" in field
                or "churn" in field
                or "inventory" in field
                or "safety" in field
                or "unit_economics" in field
            ),
            must_have_fields=ROUND216_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={
                "recurring_revenue_delta": 5.0,
                "churn_stability_delta": 5.0,
                "arpu_or_repeat_course_delta": 4.0,
                "cash_conversion_delta": 5.0,
                "unit_economics_delta": 5.0,
                "commercial_installation_delta": 4.0,
                "dealer_sell_through_delta": 4.0,
                "regulatory_pass_delta": 4.0,
                "defensive_theme_only_delta": -5.0,
                "education_policy_only_delta": -5.0,
                "smart_farm_policy_only_delta": -5.0,
                "disease_event_only_delta": -5.0,
                "celebrity_food_event_only_delta": -5.0,
                "dealer_inventory_unknown_delta": -4.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "r12_default_stage3_bias_conservative_except_recurring_service",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_disease_smart_farm_agri_export_celebrity_or_defensive_theme_as_green_alone",
                *ROUND216_GREEN_REQUIRED_FIELDS,
                *ROUND216_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage1_price_anchor if candidate.stage4b_date else None,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.8 if candidate.stage1_date or candidate.stage2_date or candidate.stage4c_date else 0.55,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round216_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND216_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
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
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "score_price_alignment": candidate.score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round216_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND216_SCORE_ADJUSTMENTS)


def round216_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND216_SHADOW_WEIGHT_ROWS)


def round216_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND216_DEEP_SUB_ARCHETYPES)


def round216_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round216_price_validation": "true"} for field in ROUND216_PRICE_VALIDATION_FIELDS)


def round216_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round216_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND216_REQUIRED_TARGET_ALIASES.items()
    )


def round216_summary() -> dict[str, int | bool | str]:
    cases = ROUND216_CASE_CANDIDATES
    return {
        "source_round": ROUND216_SOURCE_ROUND_PATH,
        "large_sector": ROUND216_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND216_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND216_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND216_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r12_default_stage3_bias": ROUND216_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round216_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND216_SOURCE_ROUND_PATH,
        "large_sector": ROUND216_LARGE_SECTOR.value,
        "summary": round216_summary(),
        "target_aliases": dict(ROUND216_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND216_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND216_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND216_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND216_HARD_4C_GATES),
        "deep_sub_archetypes": round216_deep_sub_archetype_rows(),
        "shadow_weights": round216_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round216_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_policy_disease_smart_farm_agri_export_celebrity_or_defensive_theme_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round216_summary_markdown() -> str:
    summary = round216_summary()
    lines = [
        "# Round 216 R12 Loop 8 Agri Life Service Misc Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- watch: {summary['watch_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- r12_default_stage3_bias: {summary['r12_default_stage3_bias']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND216_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- R12 Green is possible mainly for recurring rental/service or regulated cashflow cases after unit economics and FCF are visible.",
            "- Coway and KT&G stay success candidates, not Green, until fresh account, churn, ARPU, shareholder return, regulation, and price-path evidence are checked.",
            "- Medical-quota policy, phone-ban policy, bird flu, smart-farm papers, and celebrity food events are routing or event premium evidence.",
            "- Kyochon/chicken-event basket is the clean example: +20~30% without store traffic or margin evidence is 4B/event premium, not E2R.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round216_green_gate_review_markdown() -> str:
    lines = [
        "# Round 216 R12 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND216_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND216_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `Rental account growth + stable churn + ARPU + FCF` can support promotion.",
            "- `Medical-school quota policy` is routing evidence until students, repeat courses, ARPU, and OPM appear.",
            "- `Celebrity fried-chicken event` remains price-moved-without-evidence until same-store sales and franchise margin appear.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round216_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 216 R12 4B/4C Review",
        "",
        "## 4B Watch Triggers",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND216_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND216_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND216_CASE_CANDIDATES:
        if case.stage4b_status == "watch" or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round216_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 216 R12 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- r12_default_stage3_bias: conservative_except_recurring_service",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND216_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round216_r12_loop8_reports(
    output_directory: str | Path = ROUND216_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND216_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND216_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round216_case_records(), cases_path),
        "audit": _write_json(round216_audit_payload(), audit_path),
        "summary": output / "round216_r12_loop8_price_validation_summary.md",
        "case_matrix": output / "round216_r12_loop8_case_matrix.csv",
        "target_aliases": output / "round216_r12_loop8_target_aliases.csv",
        "score_adjustments": output / "round216_r12_loop8_score_adjustments.csv",
        "shadow_weights": output / "round216_r12_loop8_shadow_weights.csv",
        "deep_sub_archetypes": output / "round216_r12_loop8_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round216_r12_loop8_price_validation_fields.csv",
        "green_gate_review": output / "round216_r12_loop8_green_gate_review.md",
        "price_validation_plan": output / "round216_r12_loop8_price_validation_plan.md",
        "stage4b_4c_review": output / "round216_r12_loop8_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round216_summary_markdown(), encoding="utf-8")
    _write_csv(round216_case_rows(), paths["case_matrix"])
    _write_csv(round216_target_alias_rows(), paths["target_aliases"])
    _write_csv(round216_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round216_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round216_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round216_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round216_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round216_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round216_stage4b_4c_review_markdown(), encoding="utf-8")
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
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed_int_text(value: int) -> str:
    return f"+{value}" if value > 0 else str(value)
