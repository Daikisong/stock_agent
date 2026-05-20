"""Round-268 R12 Loop-12 agriculture/life-service/misc validation pack.

This module converts ``docs/round/round_268.md`` into structured,
calibration-only case records. It does not change production scoring, staging,
or candidate generation.

Easy example: a medical-school quota headline can move education stocks. It is
still not Stage 3-Green until paid enrollment, ARPU, repeat-course revenue,
OPM, and cash conversion are visible.
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


ROUND268_SOURCE_ROUND_PATH = "docs/round/round_268.md"
ROUND268_ANALYST_ROUND_ID = "round_196"
ROUND268_RAW_LARGE_SECTOR_LABEL = "AGRI_LIFE_SERVICE_MISC"
ROUND268_LARGE_SECTOR = Round10LargeSector.EDUCATION_LIFE_AGRI_MISC
ROUND268_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round268_r12_loop12_agri_life_service_misc_price_validation"
ROUND268_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop12_round268.jsonl"
ROUND268_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round268_r12_loop12_agri_life_service_misc_price_validation_audit.json"
ROUND268_DEFAULT_STAGE3_BIAS = "conservative_until_repeat_purchase_paid_conversion_and_cash_conversion"

ROUND268_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION": E2RArchetype.K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION.value,
    "AGRI_FOOD_INPUT_COST_SHOCK": E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK.value,
    "FEED_GRAIN_INPUT_COST_4C": E2RArchetype.FEED_GRAIN_INPUT_COST_4C.value,
    "EDUCATION_POLICY_MEDICAL_QUOTA_EVENT": E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT.value,
    "EDTECH_POLICY_ROLLBACK_4C": E2RArchetype.EDTECH_POLICY_ROLLBACK_4C.value,
    "CHILDCARE_FOREIGN_HELPER_POLICY_EVENT": E2RArchetype.CHILDCARE_FOREIGN_HELPER_POLICY_EVENT.value,
    "PET_WELFARE_TRANSITION_POLICY_EVENT": E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT.value,
    "FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM": E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM.value,
}

ROUND268_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "repeat_purchase_or_repeat_service_usage_confirmed",
    "overseas_sell_through_or_channel_reorder_confirmed",
    "capacity_utilization_confirmed",
    "paid_enrollment_or_paid_household_usage_confirmed",
    "service_utilization_confirmed",
    "arpu_or_price_pass_through_confirmed",
    "input_cost_pass_through_confirmed",
    "inventory_and_receivables_stable",
    "subsidy_or_policy_dependency_low",
    "cash_conversion_confirmed",
    "price_path_after_evidence",
)

ROUND268_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_headline_only",
    "fertility_headline_only",
    "medical_quota_only",
    "ai_textbook_theme_only",
    "pet_welfare_policy_only",
    "raw_material_price_spike_only",
    "feed_cost_spike_only",
    "celebrity_food_event_only",
    "unconfirmed_demand_conversion",
)

ROUND268_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "k_food_export_headline_rally_before_margin",
    "medical_quota_rally_before_paid_enrollment",
    "fertility_rebound_rally_before_utilization",
    "ai_textbook_theme_rally_before_paid_contract",
    "dog_meat_ban_pet_policy_rally_before_monetization",
    "celebrity_food_event_stock_spike_without_sales",
    "agri_input_shock_rally_before_pass_through",
)

ROUND268_HARD_4C_GATES: tuple[str, ...] = (
    "raw_material_shock_without_pass_through",
    "feed_cost_spike_with_no_inventory_buffer",
    "policy_rollback",
    "paid_enrollment_failure",
    "service_utilization_failure",
    "inventory_build",
    "cash_conversion_deterioration",
    "product_recall_or_food_safety",
    "shelter_capacity_failure",
    "celebrity_event_fade",
)

ROUND268_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "mfe_event",
    "mae_event",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round268ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round268ShadowWeightRow:
    archetype: E2RArchetype
    repeat_purchase: int
    overseas_sell_through: int
    capacity_utilization: int
    paid_conversion: int
    service_utilization: int
    arpu_price_pass: int
    input_cost_pass_through: int
    inventory_quality: int
    cash_conversion: int
    policy_to_revenue_bridge: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "repeat_purchase": _signed(self.repeat_purchase),
            "overseas_sell_through": _signed(self.overseas_sell_through),
            "capacity_utilization": _signed(self.capacity_utilization),
            "paid_conversion": _signed(self.paid_conversion),
            "service_utilization": _signed(self.service_utilization),
            "arpu_price_pass": _signed(self.arpu_price_pass),
            "input_cost_pass_through": _signed(self.input_cost_pass_through),
            "inventory_quality": _signed(self.inventory_quality),
            "cash_conversion": _signed(self.cash_conversion),
            "policy_to_revenue_bridge": _signed(self.policy_to_revenue_bridge),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round268DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round268CaseCandidate:
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
    mfe_event: float | None
    mae_event: float | None
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
        return ROUND268_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND268_SCORE_ADJUSTMENTS: tuple[Round268ScoreAdjustment, ...] = (
    Round268ScoreAdjustment("repeat_purchase", 5, "raise", "K-food, 펫, 생활서비스는 반복구매나 반복이용이 있어야 구조적이다."),
    Round268ScoreAdjustment("overseas_sell_through", 5, "raise", "수출 출하보다 해외 sell-through와 channel reorder가 중요하다."),
    Round268ScoreAdjustment("capacity_utilization", 5, "raise", "해외 공장·서비스 CAPA는 가동률이 확인되어야 Stage 2 이후 품질이 오른다."),
    Round268ScoreAdjustment("paid_enrollment_conversion", 5, "raise", "의대정원 이벤트는 유료수강 전환이 확인되어야 한다."),
    Round268ScoreAdjustment("service_utilization", 5, "raise", "돌봄·교육·펫 서비스는 실제 이용률이 핵심이다."),
    Round268ScoreAdjustment("ARPU_or_price_pass_through", 5, "raise", "ARPU나 가격전가가 없으면 수요가 좋아도 FCF로 닫히기 어렵다."),
    Round268ScoreAdjustment("input_cost_pass_through", 5, "raise", "배추·사료곡물 shock 이후 가격전가가 확인되어야 한다."),
    Round268ScoreAdjustment("inventory_quality", 4, "raise", "재고·매출채권 안정은 원가 shock 통과 조건이다."),
    Round268ScoreAdjustment("cash_conversion", 5, "raise", "생활서비스와 식품은 성장보다 현금전환이 Green 가드레일이다."),
    Round268ScoreAdjustment("policy_to_revenue_bridge", 5, "raise", "정책이 실제 매출·마진으로 닫힐 때만 높게 본다."),
    Round268ScoreAdjustment("policy_headline_only", -5, "lower", "정책 뉴스만으로는 회사 EPS/FCF evidence가 아니다."),
    Round268ScoreAdjustment("fertility_headline_only", -5, "lower", "출산율 반등만으로 유아·교육·돌봄주 매출을 만들지 않는다."),
    Round268ScoreAdjustment("medical_quota_only", -5, "lower", "의대정원 headline은 수강생·ARPU 전까지 event premium이다."),
    Round268ScoreAdjustment("AI_textbook_theme_only", -5, "lower", "AI 교과서 테마는 채택·예산·매출 전까지 Green 금지다."),
    Round268ScoreAdjustment("pet_welfare_policy_only", -5, "lower", "펫/동물복지 정책은 상장사 매출전환 전까지 제한한다."),
    Round268ScoreAdjustment("celebrity_food_event_only", -5, "lower", "바이럴 외식 이벤트는 매출 evidence 전 price_moved_without_evidence다."),
    Round268ScoreAdjustment("raw_material_price_spike_without_pass_through", -5, "lower", "농산물 가격 상승이 가격전가 없이 오면 margin 4C-watch다."),
    Round268ScoreAdjustment("feed_cost_spike_without_inventory_buffer", -5, "lower", "사료곡물 가격 shock은 재고 buffer와 판가전가가 없으면 4C-watch다."),
    Round268ScoreAdjustment("unconfirmed_demand_conversion", -5, "lower", "트래픽·정책 관심이 유료수요로 전환되지 않으면 Stage 3 금지다."),
)


ROUND268_SHADOW_WEIGHT_ROWS: tuple[Round268ShadowWeightRow, ...] = (
    Round268ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION, 5, 5, 5, 2, 0, 5, 4, 4, 5, 3, -2, 4, 3, "Nongshim export structure is Stage 2 until margin/FCF/price path confirm."),
    Round268ShadowWeightRow(E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK, 2, 1, 1, 0, 0, 5, 5, 5, 5, 1, 0, 4, 5, "Cabbage climate/input shock is 4C-watch unless pass-through and inventory control prove out."),
    Round268ShadowWeightRow(E2RArchetype.FEED_GRAIN_INPUT_COST_4C, 1, 0, 1, 0, 0, 4, 5, 5, 4, 0, 0, 4, 5, "Feed wheat cost shock hits livestock/feed margin unless pass-through and inventory buffer exist."),
    Round268ShadowWeightRow(E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT, 2, 0, 0, 5, 4, 5, 0, 1, 5, 5, -5, 5, 4, "Medical quota is event until paid enrollment, ARPU and repeat-course revenue confirm."),
    Round268ShadowWeightRow(E2RArchetype.EDTECH_POLICY_ROLLBACK_4C, 2, 0, 0, 4, 4, 4, 0, 1, 4, 5, 0, 4, 5, "AI textbook rollback and phone ban block edtech Green."),
    Round268ShadowWeightRow(E2RArchetype.CHILDCARE_FOREIGN_HELPER_POLICY_EVENT, 4, 0, 2, 5, 5, 5, 1, 2, 5, 5, -5, 5, 4, "Fertility and foreign-helper policy need paid utilization and margin."),
    Round268ShadowWeightRow(E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT, 4, 0, 2, 3, 5, 4, 1, 2, 4, 5, -5, 5, 4, "Dog-meat ban is policy event until pet-service revenue and shelter capacity confirm."),
    Round268ShadowWeightRow(E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM, 2, 0, 1, 2, 2, 3, 3, 3, 3, 0, -5, 5, 3, "Kyochon/Cherrybro/Neuromeka Jensen event is price_moved_without_evidence."),
)


ROUND268_DEEP_SUB_ARCHETYPES: tuple[Round268DeepSubArchetype, ...] = (
    Round268DeepSubArchetype("K-food / 라면", E2RArchetype.K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION, ("Nongshim Shin Ramyun", "U.S. / Europe export", "Walmart / Costco channel", "sell-through / ASP / capacity")),
    Round268DeepSubArchetype("김치·농산물", E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK, ("Daesang", "CJ CheilJedang", "napa cabbage heat shock", "Chinese kimchi price pressure")),
    Round268DeepSubArchetype("사료·축산", E2RArchetype.FEED_GRAIN_INPUT_COST_4C, ("Harim", "Maniker", "Farm Story", "feed wheat tender failure", "grain cost / FX / pass-through")),
    Round268DeepSubArchetype("교육", E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT, ("Megastudy", "YBMNet", "NE Neungyule", "medical-school quota", "paid enrollment / ARPU")),
    Round268DeepSubArchetype("AI 교과서", E2RArchetype.EDTECH_POLICY_ROLLBACK_4C, ("Woongjin Thinkbig", "AI textbook rollback", "classroom device ban", "teacher support gap")),
    Round268DeepSubArchetype("돌봄·출산", E2RArchetype.CHILDCARE_FOREIGN_HELPER_POLICY_EVENT, ("foreign housekeeper pilot", "fertility rebound", "paid household demand", "service utilization")),
    Round268DeepSubArchetype("펫·동물복지", E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT, ("dog-meat ban", "pet-food / shelter", "adoption", "subsidy / capacity")),
    Round268DeepSubArchetype("생활서비스 이벤트", E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM, ("Kyochon F&B", "Cherrybro", "Neuromeka", "Jensen Huang chicken event", "same-store sales / meme fade")),
)


ROUND268_CASE_CANDIDATES: tuple[Round268CaseCandidate, ...] = (
    Round268CaseCandidate(
        case_id="r12_loop12_nongshim_shin_export_capacity",
        symbol="004370",
        company_name="Nongshim",
        primary_archetype=E2RArchetype.K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION,
        secondary_archetypes=(E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND),
        case_type="success_candidate",
        round_case_type="structural_success_candidate_k_food_export_capacity",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 5, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="k_food_export_stage2_until_overseas_sell_through_margin_fcf_and_price_path_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("shin_ramyun_2023_sales_1_2tn_won", "overseas_sales_share_nearly_60pct", "north_america_sales_538mn_usd", "us_market_share_25_4pct", "us_sales_target_1_5bn_2030", "europe_sales_growth_30pct_context"),
        red_flag_fields=("overseas_sell_through_unverified", "capacity_utilization_unverified", "margin_fcf_unverified", "china_slowdown_watch", "channel_inventory_watch"),
        price_data_source="FT business anchor + attempted KRX/Naver/Yahoo/Stooq query",
        reported_price_anchor="Shin Ramyun 2023 sales 1.2T won / $883M; nearly 60% overseas; North America $538M +10%",
        reported_return_anchor="U.S. share 25.4%; U.S. sales target $1.5B by 2030; price OHLC unavailable after deep search",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"shin_ramyun_2023_sales_krw_trn": 1.2, "shin_ramyun_2023_sales_usd_mn": 883.0, "overseas_sales_share_pct": 60.0, "north_america_sales_usd_mn": 538.0, "north_america_sales_growth_pct": 10.0, "us_market_share_pct": 25.4, "us_sales_target_2030_usd_bn": 1.5, "us_target_growth_from_2023_na_sales_pct": 178.8, "europe_1q_sales_growth_context_pct": 30.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_result="K_food_export_capacity_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="export_growth_not_green_until_margin_FCF_price_path",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="K-food export structure is strong Stage 2; Green requires overseas sell-through, capacity utilization, margin, FCF and price path.",
    ),
    Round268CaseCandidate(
        case_id="r12_loop12_kimchi_cabbage_input_cost_watch",
        symbol="001680/097950/kimchi_food_processing_basket",
        company_name="Daesang / CJ CheilJedang / kimchi processors",
        primary_archetype=E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK,
        secondary_archetypes=(E2RArchetype.K_FOOD_INPUT_PACKAGING_4C, E2RArchetype.FOOD_AGRI_LIVESTOCK_CYCLE),
        case_type="failed_rerating",
        round_case_type="4c_watch_cabbage_climate_input_cost",
        stage1_date=date(2024, 9, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 10, 23),
        stage3_decision="cabbage_input_cost_shock_is_redteam_until_pass_through_inventory_and_margin_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("napa_cabbage_heat_shock", "government_cabbage_release_24000t", "cabbage_price_3000_to_9537_won", "highland_cabbage_area_minus_54_6pct", "chinese_kimchi_price_pressure"),
        red_flag_fields=("raw_material_price_spike_without_pass_through", "input_cost_pass_through_unverified", "inventory_control_unverified", "climate_supply_shock_persists"),
        price_data_source="Reuters crop/input-cost evidence + attempted stock-price query",
        reported_price_anchor="Government released 24,000t cabbage; wholesale cabbage rose from about 3,000 won to 9,537 won",
        reported_return_anchor="Highland cabbage area fell from 8,796ha to 3,995ha over 20 years; stock OHLC unavailable",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_cabbage_release_tonnes": 24000.0, "cabbage_price_early_july_krw": 3000.0, "cabbage_price_mid_sept_krw": 9537.0, "cabbage_price_jump_pct": 217.9, "cabbage_price_late_oct_krw": 5610.0, "late_oct_vs_mid_sept_pct": -41.2, "highland_cabbage_area_20y_ago_ha": 8796.0, "highland_cabbage_area_recent_ha": 3995.0, "area_decline_pct": -54.6},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="kimchi_input_cost_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="raw_material_shock_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Cabbage climate/input shock is 4C-watch unless processors prove pass-through and inventory control.",
    ),
    Round268CaseCandidate(
        case_id="r12_loop12_feed_wheat_livestock_cost_watch",
        symbol="136480/027710/195500/feed_livestock_basket",
        company_name="Harim / Farm Story / Maniker / feed-livestock basket",
        primary_archetype=E2RArchetype.FEED_GRAIN_INPUT_COST_4C,
        secondary_archetypes=(E2RArchetype.AGRI_LIVESTOCK_FOOD_COMMODITY, E2RArchetype.FOOD_AGRI_LIVESTOCK_CYCLE),
        case_type="failed_rerating",
        round_case_type="4c_watch_feed_wheat_cost",
        stage1_date=date(2026, 5, 13),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 13),
        stage3_decision="feed_cost_shock_is_margin_risk_until_pass_through_inventory_demand_and_opm_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("flc_feed_wheat_tender_65000t", "believed_no_purchase", "lowest_offer_298_50_usd_per_t", "extra_surcharge_2_usd_per_t", "effective_offer_300_50_usd_per_t"),
        red_flag_fields=("feed_cost_spike_without_inventory_buffer", "feed_cost_spike_only", "price_pass_through_unverified", "feed_inventory_buffer_unverified"),
        price_data_source="Reuters feed-wheat tender evidence + attempted stock-price query",
        reported_price_anchor="65,000t feed wheat tender believed no purchase; effective low offer $300.50/t",
        reported_return_anchor="Input cost risk anchor; stock OHLC unavailable",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"tender_volume_tonnes": 65000.0, "purchase_result": "believed_no_purchase", "lowest_offer_usd_per_t": 298.5, "extra_unloading_surcharge_usd_per_t": 2.0, "effective_lowest_offer_usd_per_t": 300.5, "effective_offer_for_65000t_usd_mn": 19.53, "arrival_target": "2026-08-31"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="feed_grain_input_cost_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="input_cost_4C_watch_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Feed wheat cost is 4C-watch for feed/livestock names until price pass-through and feed inventory buffer confirm.",
    ),
    Round268CaseCandidate(
        case_id="r12_loop12_medical_quota_private_education_event",
        symbol="072870/057030/053290/education_basket",
        company_name="Megastudy / YBMNet / NE Neungyule / education basket",
        primary_archetype=E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT,
        secondary_archetypes=(E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA, E2RArchetype.EDUCATION_SPECIALTY_SERVICES),
        case_type="event_premium",
        round_case_type="event_premium_policy_watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2026, 2, 10),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 7),
        stage3_decision="medical_quota_event_is_not_green_until_paid_enrollment_arpu_repeat_course_opm_and_cash_conversion_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("medical_quota_3058_to_3548", "2030_quota_3871", "private_education_demand_expectation", "trainee_doctor_dispute", "90pct_trainee_doctors_resigned"),
        red_flag_fields=("medical_quota_only", "paid_enrollment_unverified", "arpu_unverified", "policy_uncertainty_healthcare_disruption"),
        price_data_source="Reuters policy evidence + attempted education-stock price query",
        reported_price_anchor="Medical quota 3,058 to 3,548 in 2027 and 3,871 by 2030",
        reported_return_anchor="90% trainee doctors resigned during dispute; stock OHLC unavailable",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"original_quota": 3058.0, "quota_2027": 3548.0, "quota_increase_2027": 490.0, "quota_increase_2027_pct": 16.0, "quota_2030": 3871.0, "quota_increase_2030_vs_original": 813.0, "quota_increase_2030_pct": 26.6, "trainee_doctor_resignation_share_2025_pct": 90.0},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_policy_watch",
        rerating_result="event_premium",
        round_rerating_result="education_policy_quota_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_type="quota_policy_not_paid_enrollment_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Medical quota is Stage 2; paid enrollment, ARPU, repeat course, OPM and cash conversion required before Green.",
    ),
    Round268CaseCandidate(
        case_id="r12_loop12_ai_textbook_edtech_policy_rollback",
        symbol="095720/057030/edtech_basket",
        company_name="Woongjin Thinkbig / YBMNet / edtech basket",
        primary_archetype=E2RArchetype.EDTECH_POLICY_ROLLBACK_4C,
        secondary_archetypes=(E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL, E2RArchetype.EDTECH_AI_DISRUPTION),
        case_type="failed_rerating",
        round_case_type="4c_watch_edtech_policy_rollback",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 8, 4),
        stage3_decision="edtech_policy_rollback_and_device_ban_block_green_until_paid_adoption_and_teacher_acceptance_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ai_textbook_official_to_supplementary", "teacher_unprepared_87_4pct", "classroom_phone_device_ban_2026_03", "teacher_parent_backlash", "digital_device_policy_friction"),
        red_flag_fields=("ai_textbook_theme_only", "policy_rollback", "teacher_acceptance_unverified", "paid_contract_unverified", "classroom_device_ban"),
        price_data_source="Business Insider / Reuters policy evidence + attempted edtech stock-price query",
        reported_price_anchor="AI textbooks downgraded from official textbooks to supplementary materials; 87.4% teachers reported lack of preparation/support",
        reported_return_anchor="Classroom phone/device ban effective March 2026; stock OHLC unavailable",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ai_textbook_status": "official_textbook_to_supplementary_material", "teacher_unprepared_share_pct": 87.4, "classroom_phone_device_ban_effective": "2026-03", "students_social_media_affects_daily_life_pct": 37.0, "students_anxious_without_social_media_pct": 22.0, "device_exception": "disability_or_educational_purpose"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="edtech_policy_rollback_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="policy_rollback_blocks_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="AI education theme is blocked by policy rollback, teacher-preparation gap and classroom device restrictions.",
    ),
    Round268CaseCandidate(
        case_id="r12_loop12_childcare_foreign_helper_fertility_policy",
        symbol="childcare/infant_goods/care_service_basket",
        company_name="Childcare / foreign housekeeper / fertility basket",
        primary_archetype=E2RArchetype.CHILDCARE_FOREIGN_HELPER_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT, E2RArchetype.EDUCATION_SPECIALTY_SERVICES),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_event",
        stage1_date=date(2024, 7, 28),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="childcare_policy_and_fertility_rebound_are_stage2_until_paid_utilization_margin_and_cash_conversion_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("foreign_housekeeper_pilot_100_workers", "possible_expansion_1200_workers", "fertility_0_72_to_0_80", "births_2025_plus_6_8pct", "marriages_2025_plus_8_1pct"),
        red_flag_fields=("fertility_headline_only", "paid_household_demand_unverified", "service_utilization_unverified", "subsidy_dependency_watch"),
        price_data_source="FT foreign-housekeeper policy anchor + Reuters fertility anchor",
        reported_price_anchor="Foreign helper pilot 100 workers could expand to 1,200; fertility rose 0.72 to 0.80",
        reported_return_anchor="Births +6.8%, marriages +8.1%, Seoul fertility +8.9%; stock OHLC unavailable",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"foreign_housekeeper_pilot_workers": 100.0, "possible_expansion_workers": 1200.0, "pilot_expansion_multiple": 12.0, "fertility_rate_2023": 0.72, "fertility_rate_2024": 0.75, "fertility_rate_2025": 0.80, "fertility_rebound_2023_to_2025_pct": 11.1, "births_2025_growth_pct": 6.8, "marriages_2025_growth_pct": 8.1, "seoul_fertility_growth_pct": 8.9},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_policy_event",
        rerating_result="policy_event_rerating",
        round_rerating_result="childcare_service_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="demographic_policy_not_paid_utilization_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Policy and fertility rebound are Stage 2; paid household demand, utilization, margin and cash conversion required before Green.",
    ),
    Round268CaseCandidate(
        case_id="r12_loop12_dog_meat_ban_pet_welfare_transition",
        symbol="pet_food/pet_care/animal_welfare_basket",
        company_name="Dog-meat ban / pet-welfare transition basket",
        primary_archetype=E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.PET_WELFARE_POLICY_TRANSITION, E2RArchetype.RETAIL_DOMESTIC_CONSUMER),
        case_type="event_premium",
        round_case_type="event_premium_policy_watch",
        stage1_date=date(2024, 9, 26),
        stage2_date=date(2027, 2, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="dog_meat_ban_transition_is_policy_event_until_pet_service_revenue_shelter_capacity_and_margin_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("dog_meat_ban_transition", "government_support_100bn_won", "nearly_500000_dogs_to_rehome", "farmer_subsidy_up_to_600000_won_per_dog", "1500_breeding_farms"),
        red_flag_fields=("pet_welfare_policy_only", "pet_service_revenue_unverified", "shelter_capacity_unverified", "subsidy_dependency_watch", "policy_delay_watch"),
        price_data_source="Reuters dog-meat ban / transition policy evidence",
        reported_price_anchor="Government support about 100B won; nearly 500k dogs to rehome; up to 600k won per surrendered dog",
        reported_return_anchor="Policy transition anchor, not listed-company revenue evidence",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_support_krw_bn": 100.0, "dogs_to_rehome": 500000.0, "farmer_subsidy_per_dog_krw": 600000.0, "dog_breeding_farms": 1500.0, "slaughter_houses": 200.0, "restaurants_serving_dog_meat": 2300.0, "ban_effective": "2027-02", "potential_subsidy_liability_if_all_dogs_max_krw_bn": 300.0},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_policy_watch",
        rerating_result="event_premium",
        round_rerating_result="pet_welfare_transition_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_type="policy_not_revenue_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dog-meat ban transition is policy event; pet-food/service revenue conversion and shelter capacity required before Green.",
    ),
    Round268CaseCandidate(
        case_id="r12_loop12_kyochon_cherrybro_neuromeka_jensen_event",
        symbol="339770/066360/348340",
        company_name="Kyochon F&B / Cherrybro / Neuromeka",
        primary_archetype=E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE, E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM),
        case_type="overheat",
        round_case_type="overheat_price_moved_without_evidence",
        stage1_date=date(2025, 10, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 31),
        stage4c_date=None,
        stage3_decision="celebrity_food_event_is_price_moved_without_same_store_sales_franchise_margin_or_repeat_demand",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("jensen_huang_fried_chicken_dinner", "kyochon_plus_20pct", "cherrybro_plus_30pct", "neuromeka_surge", "non_listed_kkanbu_chicken_event"),
        red_flag_fields=("celebrity_food_event_only", "same_store_sales_unconfirmed", "franchise_margin_unconfirmed", "repeat_demand_unconfirmed"),
        price_data_source="Tom's Hardware / MarketWatch event-return summary",
        reported_price_anchor="Kyochon up to +20%, Cherrybro up to +30%; restaurant visited was non-listed Kkanbu Chicken",
        reported_return_anchor="Only Neuromeka retained gains by close according to MarketWatch; no same-store sales evidence",
        mfe_event=30.0,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kyochon_event_mfe_pct": 20.0, "cherrybro_event_mfe_pct": 30.0, "neuromeka_event": "surged; only one of three retained gains by close according to MarketWatch", "event_driver": "viral dinner at non-listed Kkanbu Chicken", "fundamental_revenue_evidence_confirmed": False, "same_store_sales_confirmed": False, "franchise_margin_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_result="celebrity_food_event_premium",
        stage_failure_type="false_yellow",
        round_stage_failure_type="should_have_been_stage1_or_4B_watch",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="Celebrity food-service event is 4B/event premium until same-store sales, franchise margin and repeat demand confirm.",
    ),
)


def round268_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND268_CASE_CANDIDATES:
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
                "Round268 R12 Loop-12 agri/life-service/misc price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "paid" in field or "margin" in field or "fcf" in field or "cash" in field or "sell_through" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field or "rally" in field or "headline" in field or "unconfirmed" in field or "mfe" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "shock" in field
                or "rollback" in field
                or "failure" in field
                or "spike" in field
                or "ban" in field
                or "unverified" in field
            ),
            must_have_fields=ROUND268_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND268_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                f"r12_default_stage3_bias_{ROUND268_DEFAULT_STAGE3_BIAS}",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_k_food_education_childcare_pet_or_celebrity_headline_as_green",
                *ROUND268_GREEN_REQUIRED_FIELDS,
                *ROUND268_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_event,
                mae_30d=candidate.mae_event,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.mfe_event is not None
                    or candidate.mae_event is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.88 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round268_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND268_CASE_CANDIDATES:
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
                "mfe_event": _float_text(candidate.mfe_event),
                "mae_event": _float_text(candidate.mae_event),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
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


def round268_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND268_SCORE_ADJUSTMENTS)


def round268_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND268_SHADOW_WEIGHT_ROWS)


def round268_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND268_DEEP_SUB_ARCHETYPES)


def round268_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round268_price_validation": "true"} for field in ROUND268_PRICE_VALIDATION_FIELDS)


def round268_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round268_label": label, "canonical_archetype": canonical} for label, canonical in ROUND268_REQUIRED_TARGET_ALIASES.items())


def round268_summary() -> dict[str, int | bool | str]:
    cases = ROUND268_CASE_CANDIDATES
    return {
        "source_round": ROUND268_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND268_ANALYST_ROUND_ID,
        "raw_large_sector_label": ROUND268_RAW_LARGE_SECTOR_LABEL,
        "large_sector": ROUND268_LARGE_SECTOR.value,
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
        "target_archetype_count": len(ROUND268_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND268_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND268_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r12_default_stage3_bias": ROUND268_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round268_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND268_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND268_ANALYST_ROUND_ID,
        "raw_large_sector_label": ROUND268_RAW_LARGE_SECTOR_LABEL,
        "large_sector": ROUND268_LARGE_SECTOR.value,
        "summary": round268_summary(),
        "target_aliases": dict(ROUND268_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND268_CASE_CANDIDATES},
        "green_required_fields": list(ROUND268_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND268_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND268_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND268_HARD_4C_GATES),
        "deep_sub_archetypes": round268_deep_sub_archetype_rows(),
        "shadow_weights": round268_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round268_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_k_food_education_childcare_pet_agri_input_or_celebrity_event_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_hard_4c_confirmed_false_for_round268",
        ],
    }


def render_round268_summary_markdown() -> str:
    summary = round268_summary()
    lines = [
        "# Round 268 R12 Loop 12 Agriculture / Life Service / Misc Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- raw_large_sector_label: {summary['raw_large_sector_label']}",
        f"- large_sector: {summary['large_sector']}",
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
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND268_CASE_CANDIDATES:
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
            "- Nongshim is K-food export Stage 2, not Green until sell-through, margin, FCF and price path close.",
            "- Cabbage and feed-wheat shocks are input-cost 4C-watch cases.",
            "- Medical quota, childcare, and pet-welfare policies are event/policy candidates until paid conversion and utilization appear.",
            "- AI textbook rollback and classroom device restrictions block edtech Green.",
            "- Jensen chicken event is price_moved_without_evidence: price moved before same-store sales or franchise margin evidence.",
            "- Easy example: `fertility rebound + childcare basket rally` is watch; `paid service usage + utilization + margin + cash conversion` is needed before deeper Stage review.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round268_green_gate_review_markdown() -> str:
    lines = [
        "# Round 268 R12 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND268_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND268_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `medical quota + education basket rally` is event premium.",
            "- `quota + paid enrollment + ARPU + OPM + cash conversion` is the type of evidence bundle required before Stage 3 review.",
            "- `celebrity dinner + stock +30%` is 4B-watch until same-store sales and franchise margin confirm.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round268_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 268 R12 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND268_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND268_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND268_CASE_CANDIDATES:
        if case.stage4b_status in {"watch", "hard_4c"} or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round268_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 268 R12 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND268_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def render_round268_deep_sub_archetypes_markdown() -> str:
    lines = ["# Round 268 Deep Sub-Archetypes", "", "| category | archetype | terms |", "|---|---|---|"]
    for row in ROUND268_DEEP_SUB_ARCHETYPES:
        lines.append(f"| {row.category} | {row.primary_archetype.value} | {', '.join(row.terms)} |")
    return "\n".join(lines) + "\n"


def write_round268_r12_loop12_reports(
    output_directory: str | Path = ROUND268_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND268_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND268_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round268_case_records(), cases_path),
        "audit": _write_json(round268_audit_payload(), audit_path),
        "summary": output / "round268_r12_loop12_price_validation_summary.md",
        "case_matrix": output / "round268_r12_loop12_case_matrix.csv",
        "target_aliases": output / "round268_r12_loop12_target_aliases.csv",
        "score_adjustments": output / "round268_r12_loop12_score_adjustments.csv",
        "shadow_weights": output / "round268_r12_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round268_r12_loop12_deep_sub_archetypes.csv",
        "deep_sub_archetypes_md": output / "round268_r12_loop12_deep_sub_archetypes.md",
        "price_validation_fields": output / "round268_r12_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round268_r12_loop12_green_gate_review.md",
        "price_validation_plan": output / "round268_r12_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round268_r12_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round268_summary_markdown(), encoding="utf-8")
    _write_csv(round268_case_rows(), paths["case_matrix"])
    _write_csv(round268_target_alias_rows(), paths["target_aliases"])
    _write_csv(round268_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round268_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round268_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round268_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round268_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round268_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round268_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetypes_md"].write_text(render_round268_deep_sub_archetypes_markdown(), encoding="utf-8")
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
