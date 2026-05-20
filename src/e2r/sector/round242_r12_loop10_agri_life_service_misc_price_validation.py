"""Round-242 R12 Loop-10 agri/life-service/misc validation pack.

Round 242 converts ``docs/round/round_242.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a medical-school quota headline can route education stocks to
watch, but it is not Stage 3-Green until paid enrollment, ARPU, OPM, and cash
conversion are visible.
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


ROUND242_SOURCE_ROUND_PATH = "docs/round/round_242.md"
ROUND242_ANALYST_ROUND_ID = "round_170"
ROUND242_RAW_LARGE_SECTOR_LABEL = "AGRI_LIFE_SERVICE_MISC"
ROUND242_LARGE_SECTOR = Round10LargeSector.EDUCATION_LIFE_AGRI_MISC
ROUND242_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round242_r12_loop10_agri_life_service_misc_price_validation"
ROUND242_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop10_round242.jsonl"
ROUND242_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round242_r12_loop10_agri_life_service_misc_price_validation_audit.json"
ROUND242_DEFAULT_STAGE3_BIAS = "conservative_except_verified_recurring_service"

ROUND242_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HOME_LIVING_RENTAL_RECURRING": E2RArchetype.HOME_LIVING_RENTAL_RECURRING.value,
    "EDUCATION_POLICY_MEDICAL_QUOTA": E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA.value,
    "EDTECH_AI_TEXTBOOK_POLICY_REVERSAL": E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL.value,
    "CHILDCARE_DEMOGRAPHIC_POLICY_EVENT": E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT.value,
    "AGRI_FOOD_INPUT_COST_SHOCK": E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK.value,
    "FEED_GRAIN_INPUT_COST_4C": E2RArchetype.FEED_GRAIN_INPUT_COST_4C.value,
    "PET_WELFARE_POLICY_TRANSITION": E2RArchetype.PET_WELFARE_POLICY_TRANSITION.value,
    "FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM": E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND242_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "recurring_revenue_or_repeat_purchase_confirmed",
    "churn_or_retention_stable",
    "arpu_or_pricing_power_confirmed",
    "paid_enrollment_or_utilization_confirmed",
    "unit_economics_confirmed",
    "cash_conversion_visible",
    "input_cost_pass_through_confirmed",
    "inventory_or_receivables_stable",
    "subsidy_dependency_low",
    "price_path_after_evidence",
)

ROUND242_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_news_only",
    "education_quota_only",
    "ai_textbook_theme_only",
    "birthrate_headline_only",
    "pet_welfare_policy_only",
    "agri_input_price_spike_only",
    "feed_cost_spike_without_pass_through",
    "celebrity_food_event_only",
    "subsidy_dependent_revenue",
    "unconfirmed_demand_conversion",
)

ROUND242_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "education_quota_rally_before_paid_enrollment",
    "birthrate_rebound_rally_before_utilization",
    "pet_welfare_policy_rally_before_monetization",
    "agri_input_shock_rally_before_pass_through",
    "celebrity_food_event_plus_20_to_30pct_without_sales",
    "rental_multiple_expands_before_account_arpu_fcf",
)

ROUND242_HARD_4C_GATES: tuple[str, ...] = (
    "product_recall",
    "churn_spike",
    "arpu_decline",
    "paid_enrollment_failure",
    "ai_education_policy_rollback",
    "subsidy_withdrawal",
    "food_input_cost_spike_without_pass_through",
    "feed_cost_shock",
    "inventory_build",
    "cash_conversion_deterioration",
    "celebrity_event_fade",
    "policy_transition_failure",
)

ROUND242_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "business_metric_anchor",
    "policy_metric_anchor",
    "input_cost_anchor",
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
class Round242ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round242ShadowWeightRow:
    archetype: E2RArchetype
    recurring_revenue: int
    churn_stability: int
    arpu_or_repeat_purchase: int
    paid_conversion: int
    unit_economics: int
    cash_conversion: int
    input_cost_pass_through: int
    inventory_quality: int
    subsidy_independence: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "recurring_revenue": _signed(self.recurring_revenue),
            "churn_stability": _signed(self.churn_stability),
            "arpu_or_repeat_purchase": _signed(self.arpu_or_repeat_purchase),
            "paid_conversion": _signed(self.paid_conversion),
            "unit_economics": _signed(self.unit_economics),
            "cash_conversion": _signed(self.cash_conversion),
            "input_cost_pass_through": _signed(self.input_cost_pass_through),
            "inventory_quality": _signed(self.inventory_quality),
            "subsidy_independence": _signed(self.subsidy_independence),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round242DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round242CaseCandidate:
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
        return ROUND242_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND242_SCORE_ADJUSTMENTS: tuple[Round242ScoreAdjustment, ...] = (
    Round242ScoreAdjustment("recurring_revenue", 5, "raise", "렌탈·구독·반복구매는 R12의 가장 강한 구조 증거다."),
    Round242ScoreAdjustment("churn_stability", 5, "raise", "반복매출은 churn이 안정적일 때만 구조적이다."),
    Round242ScoreAdjustment("ARPU_or_repeat_purchase", 4, "raise", "ARPU 또는 반복구매가 확인되어야 수요 질을 인정한다."),
    Round242ScoreAdjustment("unit_economics", 5, "raise", "교육·돌봄·펫·외식은 unit economics가 없으면 정책/이벤트에 머문다."),
    Round242ScoreAdjustment("cash_conversion", 5, "raise", "성장보다 현금전환이 R12 Green 가드레일이다."),
    Round242ScoreAdjustment("paid_enrollment_conversion", 4, "raise", "의대정원 정책은 유료수강 전환이 확인되어야 한다."),
    Round242ScoreAdjustment("utilization_rate", 4, "raise", "돌봄·서비스는 실제 이용률이 Stage 2 이후 핵심이다."),
    Round242ScoreAdjustment("input_cost_pass_through", 5, "raise", "배추·사료곡물 shock 이후 가격전가가 확인되어야 한다."),
    Round242ScoreAdjustment("inventory_quality", 4, "raise", "재고·매출채권 안정은 원가 shock 통과 조건이다."),
    Round242ScoreAdjustment("subsidy_independence", 4, "raise", "보조금 의존 매출은 Green을 제한한다."),
    Round242ScoreAdjustment("policy_news_only", -5, "lower", "정책 뉴스만으로는 회사 EPS/FCF evidence가 아니다."),
    Round242ScoreAdjustment("education_quota_only", -5, "lower", "의대정원 headline은 수강생·ARPU 전까지 event premium이다."),
    Round242ScoreAdjustment("AI_textbook_theme_only", -5, "lower", "AI 교과서 테마는 채택·예산·매출 전까지 Green 금지다."),
    Round242ScoreAdjustment("birthrate_headline_only", -4, "lower", "출산율 반등만으로 유아·교육·돌봄주 매출을 만들지 않는다."),
    Round242ScoreAdjustment("pet_welfare_policy_only", -4, "lower", "펫/동물복지 정책은 상장사 매출전환 전까지 제한한다."),
    Round242ScoreAdjustment("celebrity_food_event_only", -5, "lower", "바이럴 외식 이벤트는 매출 evidence 전 price_moved_without_evidence다."),
    Round242ScoreAdjustment("input_price_spike_without_pass_through", -5, "lower", "원재료 가격 상승이 가격전가 없이 오면 margin 4C-watch다."),
    Round242ScoreAdjustment("subsidy_dependent_revenue", -4, "lower", "보조금 의존 수익은 지속성 점수를 제한한다."),
    Round242ScoreAdjustment("unconfirmed_demand_conversion", -5, "lower", "트래픽·정책 관심이 유료수요로 전환되지 않으면 Stage 3 금지다."),
)


ROUND242_SHADOW_WEIGHT_ROWS: tuple[Round242ShadowWeightRow, ...] = (
    Round242ShadowWeightRow(E2RArchetype.HOME_LIVING_RENTAL_RECURRING, 5, 5, 4, 3, 5, 5, 2, 4, 3, -1, 3, 4, "Coway recurring rental can be Stage 3 candidate but needs accounts/churn/ARPU/FCF."),
    Round242ShadowWeightRow(E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA, 3, 2, 5, 5, 4, 4, 0, 1, 2, -5, 5, 4, "Medical quota is event until paid enrollment/ARPU/OPM confirm."),
    Round242ShadowWeightRow(E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL, 2, 2, 3, 4, 4, 4, 0, 1, 2, -5, 4, 4, "AI textbook rollback and phone ban create edtech policy friction."),
    Round242ShadowWeightRow(E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT, 4, 3, 4, 5, 4, 4, 1, 1, 3, -4, 5, 3, "Fertility rebound is Stage 2; company utilization and recurring revenue must confirm."),
    Round242ShadowWeightRow(E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK, 2, 0, 3, 2, 4, 4, 5, 5, 2, -4, 4, 4, "Kimchi cabbage shock requires pass-through and inventory control."),
    Round242ShadowWeightRow(E2RArchetype.FEED_GRAIN_INPUT_COST_4C, 2, 0, 2, 1, 4, 4, 5, 5, 2, -4, 4, 4, "Feed wheat cost spike is 4C-watch for livestock/feed names."),
    Round242ShadowWeightRow(E2RArchetype.PET_WELFARE_POLICY_TRANSITION, 2, 2, 3, 3, 4, 4, 1, 2, 3, -5, 5, 3, "Dog-meat ban is policy event until pet/service monetization confirms."),
    Round242ShadowWeightRow(E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM, 2, 0, 3, 3, 4, 4, 3, 3, 1, -5, 5, 3, "Celebrity food event is price_moved_without_evidence until traffic and margins confirm."),
)


ROUND242_DEEP_SUB_ARCHETYPES: tuple[Round242DeepSubArchetype, ...] = (
    Round242DeepSubArchetype("생활 렌탈", E2RArchetype.HOME_LIVING_RENTAL_RECURRING, ("Coway", "water purifier", "air purifier", "bidet", "mattress rental", "Malaysia", "churn", "ARPU", "FCF")),
    Round242DeepSubArchetype("의대정원 교육", E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA, ("MegaStudy", "YBM Net", "NE Neungyule", "Woongjin Thinkbig", "medical-school quota", "repeat course", "ARPU")),
    Round242DeepSubArchetype("AI 교과서 정책마찰", E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL, ("AI textbook rollback", "supplementary material", "classroom phone ban", "teacher parent backlash")),
    Round242DeepSubArchetype("출산·돌봄", E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT, ("fertility rebound", "childcare support", "foreign housekeeper pilot", "paid utilization")),
    Round242DeepSubArchetype("김치·농식품 input", E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK, ("Daesang", "CJ CheilJedang", "napa cabbage", "kimchi input cost", "government cabbage stock release")),
    Round242DeepSubArchetype("사료·축산 input", E2RArchetype.FEED_GRAIN_INPUT_COST_4C, ("Harim", "Maniker", "Farm Story", "feed wheat tender", "grain cost", "FX input cost")),
    Round242DeepSubArchetype("동물복지·펫 전환", E2RArchetype.PET_WELFARE_POLICY_TRANSITION, ("dog-meat ban", "pet food", "animal welfare", "shelter", "adoption", "transition subsidy")),
    Round242DeepSubArchetype("생활서비스 이벤트", E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM, ("Kyochon F&B", "Cherrybro", "Neuromeka", "Jensen Huang chicken event", "celebrity food event")),
)


ROUND242_CASE_CANDIDATES: tuple[Round242CaseCandidate, ...] = (
    Round242CaseCandidate(
        case_id="r12_loop10_coway_recurring_rental_watch",
        symbol="021240",
        company_name="Coway",
        primary_archetype=E2RArchetype.HOME_LIVING_RENTAL_RECURRING,
        secondary_archetypes=(E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL,),
        case_type="success_candidate",
        round_case_type="structural_success_candidate_recurring_rental",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="recurring_rental_is_stage3_candidate_only_after_accounts_churn_arpu_overseas_growth_fcf_and_price_path_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("water_purifier_air_purifier_bidet_mattress_rental", "overseas_subsidiaries_present", "recurring_service_model"),
        red_flag_fields=("rental_accounts_unverified", "churn_unverified", "arpu_unverified", "fcf_unverified", "product_recall_watch", "netmarble_capital_allocation_watch"),
        price_data_source="public company profile only",
        reported_price_anchor="price_data_unavailable_after_deep_search",
        reported_return_anchor="business model anchor only; no event-day OHLC",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"business_anchor": "water purifier / air purifier / bidet / mattress rental recurring model", "overseas_subsidiaries": ["Malaysia", "United States", "Thailand", "Indonesia", "Vietnam", "Europe", "Japan", "China"]},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="unknown",
        round_rerating_result="recurring_service_rerating_candidate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_watch_success_candidate",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Recurring rental structure is R12 Stage 3 candidate, but rental accounts, churn, ARPU, OPM/FCF and OHLC are required.",
    ),
    Round242CaseCandidate(
        case_id="r12_loop10_medical_quota_private_education_watch",
        symbol="215200/YBMNet/NE_Neungyule/Woongjin_Thinkbig_basket",
        company_name="Medical quota / private education basket",
        primary_archetype=E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA,
        secondary_archetypes=(E2RArchetype.EDUCATION_POLICY_EVENT, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_policy_watch",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2026, 2, 10),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="medical_quota_policy_is_stage1_or_stage2_until_paid_enrollment_arpu_opm_and_cash_conversion_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("medical_school_quota_policy", "quota_3058_to_3548_in_2027", "quota_3871_by_2030"),
        red_flag_fields=("education_quota_only", "paid_enrollment_unverified", "repeat_course_unverified", "arpu_unverified", "opm_unverified", "private_education_regulation_watch"),
        price_data_source="Reuters policy evidence",
        reported_price_anchor="education stock OHLC unavailable after deep search",
        reported_return_anchor="medical quota +16.0% in 2027 and +26.6% by 2030 vs original 3,058",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"original_quota": 3058.0, "quota_2027": 3548.0, "quota_increase_2027": 490.0, "quota_increase_2027_pct": 16.0, "quota_2030": 3871.0, "quota_increase_2030_vs_original": 813.0, "quota_increase_2030_pct": 26.6},
        score_price_alignment="unknown",
        round_score_price_alignment="event_premium_policy_watch",
        rerating_result="event_premium",
        round_rerating_result="education_policy_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_type="stage1_or_stage2_attention_only",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Medical quota is Stage 1/2; paid enrollment, repeat course, ARPU, OPM and cash conversion required before Green.",
    ),
    Round242CaseCandidate(
        case_id="r12_loop10_edtech_ai_textbook_rollback_phone_ban",
        symbol="Woongjin_Thinkbig/YBMNet/NE_Neungyule_edtech_basket",
        company_name="Edtech / AI textbook / classroom device regulation basket",
        primary_archetype=E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL,
        secondary_archetypes=(E2RArchetype.EDTECH_AI_DISRUPTION_KOREA, E2RArchetype.AI_EDUCATION_DISRUPTION_OVERLAY),
        case_type="failed_rerating",
        round_case_type="4c_watch_edtech_policy_friction",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 8, 1),
        stage3_decision="ai_textbook_theme_is_blocked_by_textbook_rollback_and_classroom_device_regulation_until_adoption_budget_and_revenue_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ai_textbook_reclassified_supplementary_material", "teacher_parent_backlash", "classroom_phone_device_ban_effective_2026_03"),
        red_flag_fields=("ai_textbook_theme_only", "ai_education_policy_rollback", "classroom_device_regulation", "company_revenue_impact_unverified"),
        price_data_source="Business Insider / Reuters policy evidence",
        reported_price_anchor="edtech stock OHLC unavailable after deep search",
        reported_return_anchor="AI textbooks reclassified; phone/device ban effective 2026-03; 37% daily-life impact and 22% anxiety survey anchors",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ai_textbook_status": "official_textbook_to_supplementary_material", "phone_device_ban_effective": "2026-03", "students_social_media_affects_daily_life_pct": 37.0, "students_anxious_without_social_media_pct": 22.0, "digital_device_exception": "disability_or_educational_purpose"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="edtech_policy_friction_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="should_have_been_yellow_or_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="AI education theme is blocked by textbook rollback and classroom-device regulation until actual school adoption and revenue are proven.",
    ),
    Round242CaseCandidate(
        case_id="r12_loop10_childcare_fertility_policy_watch",
        symbol="childcare/infant_goods/education/care_service_basket",
        company_name="Fertility / childcare / care-service basket",
        primary_archetype=E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.HOME_CHILD_EDUCATION, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium_demographic_policy",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 2, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="fertility_and_childcare_policy_are_stage2_until_paid_demand_utilization_margin_and_recurring_revenue_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("fertility_0_72_to_0_80", "marriages_2025_plus_8_1pct", "births_2025_plus_6_8pct", "foreign_housekeeper_pilot"),
        red_flag_fields=("birthrate_headline_only", "paid_utilization_unverified", "margin_unverified", "labor_cost_burden_watch", "policy_subsidy_watch"),
        price_data_source="Reuters fertility data + FT foreign-housekeeper policy anchor",
        reported_price_anchor="childcare stock OHLC unavailable after deep search",
        reported_return_anchor="fertility 0.72 to 0.80, marriages +8.1%, births +6.8%, housekeeper pilot 100 to possible 1,200 workers",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fertility_rate_2023": 0.72, "fertility_rate_2024": 0.75, "fertility_rate_2025": 0.80, "fertility_rebound_2023_to_2025_pct": 11.1, "marriages_2025_growth_pct": 8.1, "births_2025_growth_pct": 6.8, "foreign_housekeeper_pilot_workers": 100.0, "possible_expansion_workers": 1200.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_event_premium",
        rerating_result="policy_event_rerating",
        round_rerating_result="demographic_childcare_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_policy_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Fertility rebound and care policy are Stage 2; paid demand, utilization, margin and recurring revenue required before Green.",
    ),
    Round242CaseCandidate(
        case_id="r12_loop10_kimchi_cabbage_input_cost_watch",
        symbol="Daesang/CJ_CheilJedang/kimchi_food_processing_basket",
        company_name="Kimchi cabbage / agri-food input cost basket",
        primary_archetype=E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK,
        secondary_archetypes=(E2RArchetype.FOOD_INPUT_REGULATED_CYCLE,),
        case_type="failed_rerating",
        round_case_type="4c_watch_food_input_cost",
        stage1_date=date(2024, 9, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 10, 23),
        stage3_decision="cabbage_climate_input_shock_is_4c_watch_until_food_processors_prove_pass_through_inventory_and_margin_stability",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("hot_weather_cabbage_crop_damage", "government_cabbage_release_24000t", "cabbage_price_3000_to_9537_krw"),
        red_flag_fields=("agri_input_price_spike_only", "input_price_spike_without_pass_through", "inventory_quality_unverified", "margin_compression_watch", "climate_supply_shock"),
        price_data_source="Reuters crop/input-cost evidence",
        reported_price_anchor="cabbage 3,000 KRW to 9,537 KRW then 5,610 KRW",
        reported_return_anchor="cabbage +217.9%, late October -37.2% vs mid-September; highland area -54.6%",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_cabbage_release_tonnes": 24000.0, "cabbage_price_early_july_krw": 3000.0, "cabbage_price_mid_sept_krw": 9537.0, "cabbage_price_jump_pct": 217.9, "cabbage_price_late_oct_krw": 5610.0, "late_oct_vs_mid_sept_pct": -37.2, "highland_cabbage_area_20y_ago_ha": 8796.0, "highland_cabbage_area_recent_ha": 3995.0, "area_decline_pct": -54.6},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="agri_food_input_cost_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="4C_watch_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Cabbage climate/input shock is 4C-watch unless food processors prove pass-through and margin stability.",
    ),
    Round242CaseCandidate(
        case_id="r12_loop10_feed_wheat_livestock_input_cost_watch",
        symbol="Harim/Maniker/Farm_Story/feed_livestock_basket",
        company_name="Feed wheat / livestock input-cost basket",
        primary_archetype=E2RArchetype.FEED_GRAIN_INPUT_COST_4C,
        secondary_archetypes=(E2RArchetype.FEED_GRAIN_COST_PASS_THROUGH, E2RArchetype.FOOD_AGRI_LIVESTOCK_CYCLE),
        case_type="failed_rerating",
        round_case_type="4c_watch_feed_cost",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 13),
        stage3_decision="high_feed_wheat_cost_is_4c_watch_for_feed_livestock_processors_until_pass_through_and_inventory_quality_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("feed_wheat_tender_65000t_no_purchase", "lowest_offer_298_50_usd_per_t", "extra_surcharge_2_usd_per_t"),
        red_flag_fields=("feed_cost_spike_without_pass_through", "feed_cost_shock", "grain_fx_cost_pressure", "inventory_quality_unverified", "margin_compression_watch"),
        price_data_source="Reuters feed-wheat tender evidence",
        reported_price_anchor="feed/livestock stock OHLC unavailable after deep search",
        reported_return_anchor="65,000t tender no purchase; effective lowest offer $300.50/t, about $19.53M for full tender",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"tender_volume_tonnes": 65000.0, "purchase_result": "believed_no_purchase", "lowest_offer_usd_per_t": 298.5, "extra_unloading_surcharge_usd_per_t": 2.0, "effective_lowest_offer_usd_per_t": 300.5, "effective_offer_for_65000t_usd_mn": 19.53},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="feed_grain_input_cost_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="4C_watch_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="High feed-wheat cost is 4C-watch for feed/livestock processors until pass-through and inventory quality confirm.",
    ),
    Round242CaseCandidate(
        case_id="r12_loop10_dog_meat_ban_pet_welfare_transition",
        symbol="pet_food/animal_welfare/livestock_transition_basket",
        company_name="Dog-meat ban / pet-welfare transition basket",
        primary_archetype=E2RArchetype.PET_WELFARE_POLICY_TRANSITION,
        secondary_archetypes=(E2RArchetype.POLICY_LOCAL_SERVICE_THEME, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_policy_watch",
        stage1_date=date(2024, 9, 26),
        stage2_date=date(2027, 2, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="dog_meat_ban_transition_is_policy_event_until_pet_food_service_revenue_utilization_and_margin_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("dog_meat_ban_transition", "government_support_100bn_krw", "dogs_to_rehome_500k", "farmer_subsidy_per_dog_600k_krw"),
        red_flag_fields=("pet_welfare_policy_only", "listed_company_revenue_unverified", "subsidy_dependent_revenue", "shelter_capacity_failure_watch", "policy_transition_failure_watch"),
        price_data_source="Reuters dog-meat ban / transition policy evidence",
        reported_price_anchor="pet welfare stock OHLC unavailable after deep search",
        reported_return_anchor="support about 100B KRW, nearly 500k dogs, up to 600k KRW per surrendered dog",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_support_krw_bn": 100.0, "dogs_to_rehome": 500000.0, "farmer_subsidy_per_dog_krw": 600000.0, "dog_breeding_farms": 1500.0, "slaughter_houses": 200.0, "restaurants_serving_dog_meat": 2300.0, "ban_effective": "2027-02"},
        score_price_alignment="unknown",
        round_score_price_alignment="event_premium_policy_watch",
        rerating_result="event_premium",
        round_rerating_result="pet_welfare_transition_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_type="stage1_or_stage2_attention_only",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dog-meat ban transition is Stage 1/2 policy event; pet-food/service revenue conversion required before Green.",
    ),
    Round242CaseCandidate(
        case_id="r12_loop10_kyochon_cherrybro_neuromeka_jensen_event",
        symbol="339770/066360/348340",
        company_name="Kyochon F&B / Cherrybro / Neuromeka",
        primary_archetype=E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="overheat",
        round_case_type="overheat_price_moved_without_evidence",
        stage1_date=date(2025, 10, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 31),
        stage4c_date=None,
        stage3_decision="celebrity_fried_chicken_event_is_4b_event_premium_until_store_traffic_same_store_sales_franchise_margin_and_repeat_demand_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("jensen_huang_fried_chicken_dinner", "kyochon_up_to_20pct", "cherrybro_daily_limit_30pct", "neuromeka_jump"),
        red_flag_fields=("celebrity_food_event_only", "fundamental_revenue_evidence_not_confirmed", "event_driver_nonlisted_kkanbu_chicken", "viral_fade_watch", "franchise_margin_unverified"),
        price_data_source="Tom's Hardware / MarketWatch event-return summary",
        reported_price_anchor="Kyochon up to +20%, Cherrybro up to daily limit +30%",
        reported_return_anchor="viral dinner at non-listed Kkanbu Chicken; Neuromeka retained gains by close according to MarketWatch",
        mfe_1d=30.0,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kyochon_event_mfe_pct": 20.0, "cherrybro_event_mfe_pct": 30.0, "neuromeka_event": "jumped; only one of the three to retain gains by close according to MarketWatch", "fundamental_revenue_evidence_confirmed": False, "event_driver": "viral dinner at non-listed Kkanbu Chicken"},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_result="celebrity_food_event_premium",
        stage_failure_type="false_yellow",
        round_stage_failure_type="should_have_been_stage1_or_4B_watch",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="Celebrity fried-chicken event is 4B/event premium until store traffic, same-store sales, franchise margin and repeat demand confirm.",
    ),
)


def round242_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND242_CASE_CANDIDATES:
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
                "Round242 R12 Loop-10 agri/life-service/misc price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "recurring" in field
                or "rental" in field
                or "paid" in field
                or "utilization" in field
                or "margin" in field
                or "pass_through" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field or "viral" in field or "mfe" in field or "rally" in field or "headline" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "shock" in field
                or "rollback" in field
                or "failure" in field
                or "cost" in field
                or "regulation" in field
                or "fade" in field
                or "recall" in field
                or "churn" in field
                or "inventory" in field
            ),
            must_have_fields=ROUND242_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND242_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "r12_default_stage3_bias_conservative_except_verified_recurring_service",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_birthrate_input_cost_pet_or_celebrity_event_as_green_alone",
                *ROUND242_GREEN_REQUIRED_FIELDS,
                *ROUND242_GREEN_FORBIDDEN_PATTERNS,
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
                    candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.8 if candidate.stage1_date or candidate.stage2_date or candidate.stage4c_date else 0.6,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round242_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND242_CASE_CANDIDATES:
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


def round242_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND242_SCORE_ADJUSTMENTS)


def round242_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND242_SHADOW_WEIGHT_ROWS)


def round242_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND242_DEEP_SUB_ARCHETYPES)


def round242_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round242_price_validation": "true"} for field in ROUND242_PRICE_VALIDATION_FIELDS)


def round242_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round242_label": label, "canonical_archetype": canonical} for label, canonical in ROUND242_REQUIRED_TARGET_ALIASES.items())


def round242_summary() -> dict[str, int | bool | str]:
    cases = ROUND242_CASE_CANDIDATES
    return {
        "source_round": ROUND242_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND242_ANALYST_ROUND_ID,
        "raw_large_sector_label": ROUND242_RAW_LARGE_SECTOR_LABEL,
        "large_sector": ROUND242_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND242_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND242_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND242_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r12_default_stage3_bias": ROUND242_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round242_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND242_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND242_ANALYST_ROUND_ID,
        "raw_large_sector_label": ROUND242_RAW_LARGE_SECTOR_LABEL,
        "large_sector": ROUND242_LARGE_SECTOR.value,
        "summary": round242_summary(),
        "target_aliases": dict(ROUND242_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND242_CASE_CANDIDATES},
        "green_required_fields": list(ROUND242_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND242_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND242_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND242_HARD_4C_GATES),
        "deep_sub_archetypes": round242_deep_sub_archetype_rows(),
        "shadow_weights": round242_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round242_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_policy_birthrate_input_cost_pet_or_celebrity_food_event_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_hard_4c_unconfirmed_for_round242",
        ],
    }


def render_round242_summary_markdown() -> str:
    summary = round242_summary()
    lines = [
        "# Round 242 R12 Loop 10 Agri Life Service Misc Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- raw_large_sector_label: {summary['raw_large_sector_label']}",
        f"- mapped_large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- deep_sub_archetype_count: {summary['deep_sub_archetype_count']}",
        f"- shadow_weight_row_count: {summary['shadow_weight_row_count']}",
        f"- r12_default_stage3_bias: {summary['r12_default_stage3_bias']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND242_CASE_CANDIDATES:
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
            "- R12 Green needs recurring revenue, paid conversion, unit economics, price pass-through, and cash conversion.",
            "- Coway is the cleanest recurring-service watch case, but accounts/churn/ARPU/FCF and OHLC are missing.",
            "- Medical quota, fertility, and pet-welfare policies are Stage 1/2 routing signals until company revenue converts.",
            "- AI textbook rollback, cabbage shock, and feed wheat cost are 4C-watch inputs.",
            "- Jensen fried-chicken event is the clean price_moved_without_evidence example.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round242_green_gate_review_markdown() -> str:
    lines = ["# Round 242 R12 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND242_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND242_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `출산율 반등 + 유아주 기대` is Stage 1/2 routing.",
            "- `유료 이용률 + 반복매출 + margin + cash conversion` is the evidence bundle required for deeper Stage review.",
            "- `치킨 이벤트 +20-30%` is 4B-watch/event premium until repeat demand and margin prove otherwise.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round242_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 242 R12 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND242_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND242_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- Policy headlines are not company revenue.",
            "- Input-cost spikes are RedTeam inputs unless pass-through and inventory quality are visible.",
            "- Celebrity food events can move prices before evidence; keep them in 4B-watch/event premium.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND242_CASE_CANDIDATES:
        if case.stage4b_status == "watch" or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round242_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 242 R12 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND242_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round242_r12_loop10_reports(
    output_directory: str | Path = ROUND242_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND242_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND242_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round242_case_records(), cases_path),
        "audit": _write_json(round242_audit_payload(), audit_path),
        "summary": output / "round242_r12_loop10_price_validation_summary.md",
        "case_matrix": output / "round242_r12_loop10_case_matrix.csv",
        "target_aliases": output / "round242_r12_loop10_target_aliases.csv",
        "score_adjustments": output / "round242_r12_loop10_score_adjustments.csv",
        "shadow_weights": output / "round242_r12_loop10_shadow_weights.csv",
        "deep_sub_archetypes": output / "round242_r12_loop10_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round242_r12_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round242_r12_loop10_green_gate_review.md",
        "price_validation_plan": output / "round242_r12_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round242_r12_loop10_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round242_summary_markdown(), encoding="utf-8")
    _write_csv(round242_case_rows(), paths["case_matrix"])
    _write_csv(round242_target_alias_rows(), paths["target_aliases"])
    _write_csv(round242_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round242_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round242_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round242_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round242_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round242_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round242_stage4b_4c_review_markdown(), encoding="utf-8")
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
