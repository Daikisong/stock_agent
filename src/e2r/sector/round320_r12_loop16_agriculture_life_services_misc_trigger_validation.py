"""Round-320 R12 Loop-16 agriculture/life-service/misc trigger validation.

This module converts ``docs/round/round_320.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a food-delivery M&A teaser can be Stage2 evidence, but it is not
Stage3-Green until final SPA, regulatory approval, GMV, take-rate and margin
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


ROUND320_SOURCE_ROUND_PATH = "docs/round/round_320.md"
ROUND320_ANALYST_ROUND_ID = "round_248"
ROUND320_LARGE_SECTOR = "AGRICULTURE_LIFE_SERVICES_MISC"
ROUND320_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND320_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round320_r12_loop16_agriculture_life_services_misc_trigger_validation"
ROUND320_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop16_round248.jsonl"
ROUND320_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r12_loop16_round248.jsonl"
ROUND320_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round320_r12_loop16_agriculture_life_services_misc_trigger_validation_audit.json"
ROUND320_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round248_r12_loop16_v1.csv"

ROUND320_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B": E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B.value,
    "EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C": E2RArchetype.EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C.value,
    "FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B": E2RArchetype.FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B.value,
    "FEED_WHEAT_COST_SHOCK_4B": E2RArchetype.FEED_WHEAT_COST_SHOCK_4B.value,
    "PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE": E2RArchetype.PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE.value,
    "EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE": E2RArchetype.EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE.value,
    "FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE": E2RArchetype.FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE.value,
    "MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF": E2RArchetype.MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF.value,
}

ROUND320_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "final_MA_approval_or_financing_confirmed",
    "event_return_at_least_5pct",
    "user_shift_connects_to_GMV_spending_shipment_or_margin",
    "food_agri_policy_connects_to_cost_decline_or_margin_recovery",
    "demographic_or_education_demand_connects_to_listed_revenue_or_ARPU",
    "pet_welfare_policy_connects_to_listed_pet_food_vet_or_service_revenue",
    "no_data_breach_commodity_cost_shock_regulatory_backlash_or_service_disruption_4B_4C",
)

ROUND320_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_signal_exists_after_EPS_OP_FCF_path_can_change",
    "approval_revenue_conversion_margin_or_durability_remains_open",
    "reported_event_anchor_exists_but_full_adjusted_OHLC_is_missing",
    "date_and_source_context_are_visible_but_company_specific_bridge_is_incomplete",
)

ROUND320_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "life_service_MA_final_approved_and_GMV_take_rate_margin_connected",
    "user_shift_confirmed_in_revenue_profit_and_retention",
    "food_agri_cost_shock_eased_and_price_pass_through_succeeds",
    "education_birthrate_or_pet_policy_converts_to_listed_company_revenue",
    "no_commodity_cost_data_breach_regulation_or_subsidy_execution_4B",
    "full_window_MFE_MAE_favorable",
)

ROUND320_GREEN_BLOCKERS: tuple[str, ...] = (
    "MA_headline_without_approval",
    "user_shift_without_revenue",
    "food_policy_without_company_margin",
    "commodity_cost_ignored",
    "pet_policy_without_listed_beneficiary",
    "education_cohort_spike_without_revenue",
    "birthrate_rebound_one_year",
    "medical_policy_relief_without_service_data",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND320_SCORE_UP_AXES: tuple[str, ...] = (
    "platform_MA_final_approval",
    "delivery_GMV_take_rate_conversion",
    "consumer_trust_security",
    "food_price_pass_through",
    "import_quota_margin_relief",
    "feed_cost_sensitivity",
    "pet_welfare_revenue_conversion",
    "education_demand_ARPU",
    "fertility_trend_durability",
    "service_disruption_normalization",
)

ROUND320_SCORE_DOWN_AXES: tuple[str, ...] = (
    "MA_headline_without_approval",
    "user_shift_without_revenue",
    "food_policy_without_company_margin",
    "commodity_cost_ignored",
    "pet_policy_without_listed_beneficiary",
    "education_cohort_spike_without_revenue",
    "birthrate_rebound_one_year",
    "medical_policy_relief_without_service_data",
)

ROUND320_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "M&A_teaser_before_final_SPA_or_approval",
    "rival_share_shift_before_GMV_and_margin_conversion",
    "food_price_policy_before_company_margin_recovery",
    "feed_wheat_cost_shock_before_pass_through",
    "pet_welfare_policy_before_listed_revenue_conversion",
    "education_or_birthrate_headline_before_ARPU_and_retention",
    "medical_quota_relief_before_trainee_return_and_service_normalization",
)

ROUND320_HARD_4C_GATES: tuple[str, ...] = (
    "major_data_breach_in_everyday_service_platform",
    "food_price_shock_causes_volume_decline_and_margin_squeeze",
    "commodity_cost_spike_without_pass_through",
    "failed_MA_or_antitrust_rejection",
    "subsidy_execution_failure",
    "service_system_disruption_such_as_medical_or_education_crisis",
)

ROUND320_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_policy_deal_price_or_service_disruption_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_life_service_agri_education_pet_or_demographic_headline_as_Green_without_final_approval_revenue_margin_ARPU_pass_through_or_service_normalization",
)


@dataclass(frozen=True)
class Round320TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: str
    evidence_available: str
    event_return_pct: float | str | None
    trigger_outcome_label: str
    promote_to: str
    extra_metrics: Mapping[str, object]

    def as_dict(self) -> dict[str, object]:
        return {
            "trigger_id": self.trigger_id,
            "case_id": self.case_id,
            "trigger_type": self.trigger_type,
            "trigger_date": self.trigger_date,
            "evidence_available": self.evidence_available,
            "event_return_pct": self.event_return_pct,
            "trigger_outcome_label": self.trigger_outcome_label,
            "promote_to": self.promote_to,
            "extra_metrics": dict(self.extra_metrics),
        }

    def as_row(self) -> dict[str, str]:
        row = {key: _value_text(value) for key, value in self.as_dict().items() if key != "extra_metrics"}
        row["extra_metrics"] = json.dumps(self.extra_metrics, ensure_ascii=False, sort_keys=True)
        return row


@dataclass(frozen=True)
class Round320CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    best_trigger: str
    best_trigger_type: str
    stage_candidate: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    event_mfe_pct: float | None
    event_mae_pct: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    stage_failure_type: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type

    def to_case_record(self) -> E2RCaseRecord:
        guardrails = [
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "stage_candidate_not_downgraded_for_missing_full_ohlc",
            "do_not_use_round320_cases_as_candidate_generation_input",
            "do_not_treat_life_service_agri_education_pet_or_demographic_headline_as_Green_without_final_approval_revenue_margin_ARPU_pass_through_or_service_normalization",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "approval" in field
            or "margin" in field
            or "ARPU" in field
            or "subsidy" in field
            or "pass_through" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "breach" in field
            or "security" in field
            or "cost_shock" in field
            or "service_disruption" in field
            or "medical" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND320_LARGE_SECTOR,
            large_sector=ROUND320_LARGE_SECTOR,
            primary_archetype=self.primary_archetype,
            secondary_archetypes=self.secondary_archetypes,
            expected_group=self.expected_group,
            case_type=self.case_type,
            stage1_date=self.stage1_date,
            stage2_date=self.stage2_date,
            stage3_date=self.stage3_date,
            stage4b_date=self.stage4b_date,
            stage4c_date=self.stage4c_date,
            evidence_summary=self.notes,
            stage1_evidence=self.evidence_fields,
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=self.evidence_fields if self.stage3_date else (),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=ROUND320_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating", "overheat"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.78,
            ),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": "|".join(archetype.value for archetype in self.secondary_archetypes),
            "case_type": self.case_type,
            "round_case_type": self.round_case_type,
            "best_trigger": self.best_trigger,
            "best_trigger_type": self.best_trigger_type,
            "stage_candidate": self.stage_candidate,
            "stage1_date": _date_text(self.stage1_date),
            "stage2_date": _date_text(self.stage2_date),
            "stage3_date": _date_text(self.stage3_date),
            "stage4b_date": _date_text(self.stage4b_date),
            "stage4c_date": _date_text(self.stage4c_date),
            "hard_4c_confirmed": str(self.hard_4c_confirmed).lower(),
            "evidence_fields": "|".join(self.evidence_fields),
            "red_flag_fields": "|".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND320_CASE_CANDIDATES: tuple[Round320CaseCandidate, ...] = (
    Round320CaseCandidate(
        "r12_loop16_baemin_naver_uber_food_delivery_ma",
        "035420/UBER/Delivery_Hero_readthrough",
        "Naver / Uber / Delivery Hero food-delivery M&A read-through",
        E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B,
        (E2RArchetype.FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B, E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2),
        "event_premium",
        "Stage2_food_delivery_platform_MA_not_Green",
        "r12l16_baemin_naver_uber_T1",
        "Stage2_MA_teaser_with_approval_4B",
        "Stage2 + 4B-watch",
        date(2026, 5, 18),
        date(2026, 5, 18),
        None,
        date(2026, 5, 18),
        None,
        False,
        ("Baemin_bid_value_8T_KRW", "bid_value_5_34B_usd", "Uber_80pct_Naver_20pct", "Naver_teaser_letter_received_no_final_decision", "Uber_Delivery_Hero_stake_19_5pct", "Delivery_Hero_event_return_plus_5_6pct"),
        ("final_SPA_missing", "regulatory_approval_missing", "financing_structure_missing", "Naver_economics_missing", "Baemin_GMV_take_rate_missing", "commission_regulation_4B", "full_OHLC_MFE_MAE_missing"),
        5.6,
        None,
        {"trigger_date": "2026-05-18", "bid_value_krw_trn": 8.0, "bid_value_usd_bn": 5.34, "uber_ratio_pct": 80, "naver_ratio_pct": 20, "delivery_hero_stake_pct": 19.5, "delivery_hero_stake_value_eur_bn": 1.7, "delivery_hero_event_return_pct": 5.6, "naver_status": "teaser_letter_received_no_final_decision"},
        "aligned",
        "Stage2_food_delivery_platform_MA_not_Green",
        "event_premium",
        "stage2_watch_success",
        "Food-delivery M&A is Stage2 evidence only. Green waits for final SPA, approval, financing, GMV, take-rate and margin.",
    ),
    Round320CaseCandidate(
        "r12_loop16_coupang_everyday_delivery_share_shift",
        "CPNG/035420/139480/000120/Kurly_private",
        "Coupang breach and everyday-delivery rival share shift",
        E2RArchetype.EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C,
        (E2RArchetype.ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2, E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C),
        "4c_thesis_break",
        "everyday_delivery_security_4C_with_rival_stage2",
        "r12l16_coupang_delivery_shift_T0",
        "4C_security_with_rival_Stage2",
        "4C + Stage2 rival watch",
        date(2025, 11, 1),
        date(2025, 12, 1),
        None,
        None,
        date(2025, 11, 1),
        True,
        ("affected_users_33_to_34_mn", "Coupang_return_since_breach_minus_34pct", "Dec_report_return_minus_17pct", "MAU_minus_3_5pct", "daily_spending_minus_6_3pct", "daily_spending_Jan_139_2B_won", "Naver_online_users_plus_23pct", "CJ_Logistics_Q4_overnight_one_day_volume_plus_120pct"),
        ("Coupang_data_breach_hard_4C", "Naver_GMV_conversion_missing", "E_Mart_delivery_revenue_missing", "CJ_Logistics_margin_missing", "Coupang_churn_duration_missing", "hypermarket_rule_change_missing", "fine_finalization_missing"),
        None,
        -34.0,
        {"breach_context": "2025-11_to_2025-12", "affected_users_mn_low": 33, "affected_users_mn_high": 34, "coupang_return_since_breach_pct": -34, "dec_report_return_pct": -17, "mobile_MAU_change_pct": -3.5, "daily_spending_change_pct": -6.3, "daily_spending_jan_krw_bn": 139.2, "naver_online_users_change_pct": 23, "cj_logistics_q4_overnight_one_day_volume_pct": 120},
        "aligned",
        "hard_4C_security_with_rival_stage2",
        "thesis_break",
        "should_have_been_red",
        "The breach is hard 4C for the damaged platform. Rival Stage2 needs GMV, shipment margin and retention conversion.",
    ),
    Round320CaseCandidate(
        "r12_loop16_food_price_inflation_import_quota",
        "food_processor_basket/restaurant_basket/grocer_basket",
        "Food price inflation and import-quota policy relief basket",
        E2RArchetype.FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B,
        (E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH, E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH),
        "4b_watch",
        "food_price_policy_stage2_with_margin_4B",
        "r12l16_food_price_inflation_T0",
        "Stage2_policy_with_margin_4B",
        "Stage2 + 4B-watch",
        date(2025, 12, 1),
        date(2025, 12, 1),
        None,
        date(2025, 12, 1),
        None,
        False,
        ("CPI_2_4pct", "agri_fishery_5_6pct", "rice_18_6pct", "mandarin_26_5pct", "supplementary_budget_2025_06_16", "import_quota_increases", "oil_tax_break_extension", "cash_like_consumption_support"),
        ("company_specific_price_pass_through_missing", "volume_elasticity_missing", "gross_margin_recovery_missing", "retail_distribution_reform_missing", "weather_normalization_missing", "KRW_stabilization_missing", "food_policy_without_company_margin_4B"),
        None,
        None,
        {"inflation_reference_date": "2025-12-01", "CPI_pct": 2.4, "agri_fishery_pct": 5.6, "rice_pct": 18.6, "mandarin_pct": 26.5, "supplementary_budget_date": "2025-06-16", "policy_measures": ["food_price_burden_support", "import_quota_increases", "oil_tax_break_extension", "cash_like_consumption_support"]},
        "evidence_good_but_price_failed",
        "food_price_policy_stage2_with_margin_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Food-price relief is Stage2 only when it maps to company pass-through, volume elasticity and gross-margin recovery.",
    ),
    Round320CaseCandidate(
        "r12_loop16_feed_wheat_cost_shock",
        "136480/027740/088910/003380/feed_livestock_basket",
        "Feed wheat tender failure and livestock-feed cost shock",
        E2RArchetype.FEED_WHEAT_COST_SHOCK_4B,
        (E2RArchetype.AGRI_FEED_PRICE_INPUT_COST_4C_WATCH, E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH),
        "4b_watch",
        "feed_cost_4B_not_actionable",
        "r12l16_feed_wheat_T0",
        "4B_feed_cost_shock",
        "4B-watch",
        date(2026, 5, 13),
        None,
        None,
        date(2026, 5, 13),
        date(2026, 5, 13),
        False,
        ("feed_wheat_tender_65000_tons", "believed_no_purchase", "offers_too_high_after_US_wheat_futures_surge", "lowest_offer_298_50_usd", "unloading_surcharge_2_00_usd", "arrival_target_2026_08_31"),
        ("feed_price_pass_through_missing", "livestock_product_price_missing", "gross_margin_recovery_missing", "government_support_missing", "volume_impact_missing", "grain_price_normalization_missing", "commodity_cost_spike_4C_watch"),
        None,
        None,
        {"trigger_date": "2026-05-13", "tender_volume_tons": 65000, "purchase_result": "believed_no_purchase", "reason": "offers_too_high_after_US_wheat_futures_surge", "lowest_offer_usd": 298.50, "unloading_surcharge_usd": 2.00, "arrival_target": "2026-08-31"},
        "evidence_good_but_price_failed",
        "feed_cost_4B_not_actionable",
        "no_rerating",
        "should_have_been_red",
        "Feed wheat cost shock is a margin-risk overlay. It is not positive Stage2 unless pass-through and gross-margin recovery are visible.",
    ),
    Round320CaseCandidate(
        "r12_loop16_dog_meat_ban_pet_welfare_transition",
        "pet_food_vet_shelter_basket/policy_reference",
        "Dog-meat ban and pet welfare transition reference",
        E2RArchetype.PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE,
        (E2RArchetype.PET_WELFARE_POLICY_TRANSITION, E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT),
        "event_premium",
        "pet_welfare_policy_stage2_reference_not_Green",
        "r12l16_dog_meat_pet_T1",
        "Stage2_policy_reference",
        "Stage2 reference + 4B-watch",
        date(2024, 1, 1),
        date(2024, 9, 26),
        None,
        date(2024, 9, 26),
        None,
        False,
        ("dog_meat_ban_passed_2024_01", "ban_effective_early_2027", "government_incentives_100B_KRW", "government_incentives_75M_usd", "max_per_dog_600000_KRW", "dogs_to_rehome_nearly_500000"),
        ("listed_pet_food_sales_missing", "vet_service_revenue_missing", "shelter_capacity_missing", "adoption_rate_missing", "farmer_transition_success_missing", "subsidy_execution_missing", "pet_policy_without_listed_beneficiary_4B"),
        None,
        None,
        {"law_passed_context": "2024-01", "ban_effective": "early_2027", "incentive_plan_date": "2024-09-26", "government_incentives_krw_bn": 100, "government_incentives_usd_mn": 75, "max_per_dog_krw": 600000, "dogs_to_rehome_context": "nearly_500000"},
        "evidence_good_but_price_failed",
        "pet_welfare_policy_stage2_reference_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Dog-meat ban is a policy reference. Green requires listed pet-food, vet-service or shelter economics.",
    ),
    Round320CaseCandidate(
        "r12_loop16_csat_education_service_demand",
        "education_service_basket/online_education/publishing_reference",
        "CSAT and education-service demand reference",
        E2RArchetype.EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE,
        (E2RArchetype.HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2, E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C),
        "event_premium",
        "education_demand_stage2_reference_not_Green",
        "r12l16_csat_education_T0",
        "Stage2_reference",
        "Stage2 reference + 4B-watch",
        date(2025, 11, 13),
        date(2025, 11, 13),
        None,
        date(2025, 11, 13),
        None,
        False,
        ("CSAT_registered_applicants_554174", "YoY_plus_6pct", "highest_since_2019", "flight_restriction_35_minutes", "affected_flights_140", "market_office_delay_1_hour"),
        ("listed_education_revenue_missing", "ARPU_missing", "online_conversion_missing", "margin_missing", "repeat_enrollment_missing", "cohort_spike_from_2007_births_4B", "household_affordability_missing"),
        None,
        None,
        {"trigger_date": "2025-11-13", "registered_applicants": 554174, "YoY_pct": 6, "highest_since": 2019, "flight_restriction_minutes": 35, "affected_flights": 140, "market_office_delay_hours": 1, "stage4b_overlay": ["cohort_spike_from_2007_births", "long_term_low_birthrate", "education_regulation", "household_affordability"]},
        "evidence_good_but_price_failed",
        "education_demand_stage2_reference_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "CSAT applicant rebound is Stage2 reference only. Green needs listed revenue, ARPU, margin and repeat enrolment.",
    ),
    Round320CaseCandidate(
        "r12_loop16_birthrate_childcare_pipeline",
        "childcare_basket/baby_goods/education_pipeline_reference",
        "Birthrate rebound and childcare/baby-service pipeline reference",
        E2RArchetype.FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE,
        (E2RArchetype.DEMOGRAPHIC_CHILDCARE_STAGE2, E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT),
        "event_premium",
        "demographic_stage2_reference_not_Green",
        "r12l16_birthrate_childcare_T0",
        "Stage2_reference",
        "Stage2 reference + 4B-watch",
        date(2026, 2, 25),
        date(2026, 2, 25),
        None,
        date(2026, 2, 25),
        None,
        False,
        ("fertility_2025_0_80", "fertility_2024_0_75", "births_plus_6_8pct", "marriages_plus_8_1pct", "Seoul_fertility_plus_8_9pct", "five_year_demographic_response_plan", "childbirth_incentives", "skilled_foreign_worker_recruitment"),
        ("listed_childcare_revenue_missing", "baby_goods_sales_missing", "daycare_enrollment_missing", "education_pipeline_conversion_missing", "policy_budget_execution_missing", "multi_year_birthrate_durability_missing", "birthrate_rebound_one_year_4B"),
        None,
        None,
        {"trigger_date": "2026-02-25", "fertility_2025": 0.80, "fertility_2024": 0.75, "births_change_pct": 6.8, "marriages_change_pct": 8.1, "seoul_fertility_change_pct": 8.9, "policy_plans": ["five_year_demographic_response_plan", "childbirth_incentives", "skilled_foreign_worker_recruitment"]},
        "evidence_good_but_price_failed",
        "demographic_stage2_reference_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Birthrate rebound is useful signal, but Green requires multi-year durability and listed childcare or baby-service economics.",
    ),
    Round320CaseCandidate(
        "r12_loop16_medical_education_quota_freeze",
        "medical_education_reference/hospital_service_reference/education_policy",
        "Medical education quota freeze and service disruption relief",
        E2RArchetype.MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF,
        (E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA, E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT),
        "4b_watch",
        "medical_education_service_relief_not_Green",
        "r12l16_medical_quota_relief_T1",
        "relief_reference",
        "4B relief reference",
        date(2025, 3, 7),
        None,
        None,
        date(2025, 3, 7),
        date(2025, 3, 7),
        False,
        ("relief_trigger_2025_03_07", "proposed_medical_students_about_3000_annually", "dispute_duration_13_months", "trainee_walkout_context_90pct", "emergency_care_stress", "surgery_delay", "medical_student_boycott", "trust_breakdown"),
        ("trainee_doctor_return_missing", "hospital_service_normalization_missing", "medical_school_schedule_normalization_missing", "hospital_revenue_recovery_missing", "policy_consensus_missing", "service_system_disruption_4C_watch"),
        None,
        None,
        {"relief_trigger_date": "2025-03-07", "proposed_medical_student_number_annually_context": 3000, "dispute_duration_months": 13, "trainee_walkout_context_pct": 90, "service_disruption_channels": ["emergency_care_stress", "surgery_delay", "medical_student_boycott", "trust_breakdown"]},
        "evidence_good_but_price_failed",
        "medical_education_service_relief_not_Green",
        "policy_event_rerating",
        "should_have_been_red",
        "Medical quota freeze is relief reference only. Green waits for trainee return, service normalization and hospital revenue recovery.",
    ),
)

ROUND320_TRIGGER_RECORDS: tuple[Round320TriggerRecord, ...] = (
    Round320TriggerRecord("r12l16_baemin_naver_uber_T1", "r12_loop16_baemin_naver_uber_food_delivery_ma", "Stage2_food_delivery_MA_teaser", "2026-05-18", "Baemin consortium headline; bid value 8T KRW / $5.34B, Uber 80%, Naver 20%, Naver only received teaser letter; Delivery Hero +5.6%.", "Delivery_Hero_proxy_+5.6", "food_delivery_MA_teaser_not_Green", "Stage2", {"bid_value_krw_trn": 8.0, "bid_value_usd_bn": 5.34, "delivery_hero_event_return_pct": 5.6}),
    Round320TriggerRecord("r12l16_coupang_delivery_shift_T0", "r12_loop16_coupang_everyday_delivery_share_shift", "hard_4C_security_with_rival_stage2", "2025-11_to_2025-12", "Coupang breach affects 33-34M users; stock -34%; MAU -3.5%, spending -6.3%; Naver users +23%, CJ one-day volume +120%.", "Coupang_-34_context", "hard_4C_with_rival_stage2_watch", "4C+Stage2", {"affected_users_mn_low": 33, "affected_users_mn_high": 34, "coupang_return_since_breach_pct": -34, "naver_users_change_pct": 23, "cj_volume_change_pct": 120}),
    Round320TriggerRecord("r12l16_food_price_inflation_T0", "r12_loop16_food_price_inflation_import_quota", "Stage2_food_price_policy_with_4B", "2025-12-01", "CPI 2.4%, agri/fishery 5.6%, rice 18.6%, mandarin 26.5%; import quota and support measures need company margin bridge.", "price_data_unavailable_after_deep_search", "food_policy_stage2_margin_4B", "Stage2+4B", {"CPI_pct": 2.4, "rice_pct": 18.6, "mandarin_pct": 26.5}),
    Round320TriggerRecord("r12l16_feed_wheat_T0", "r12_loop16_feed_wheat_cost_shock", "4B_feed_wheat_cost_shock", "2026-05-13", "65,000-ton feed wheat tender believed no purchase after high offers; lowest offer $298.50 plus $2.00 unloading surcharge.", "price_data_unavailable_after_deep_search", "feed_cost_4B_not_actionable", "4B-watch", {"tender_volume_tons": 65000, "lowest_offer_usd": 298.50, "unloading_surcharge_usd": 2.00}),
    Round320TriggerRecord("r12l16_dog_meat_pet_T1", "r12_loop16_dog_meat_ban_pet_welfare_transition", "Stage2_pet_welfare_policy_reference", "2024-09-26", "Dog-meat ban transition includes 100B KRW support, up to 600,000 KRW per dog, nearly 500,000 dogs to rehome.", "price_data_unavailable_after_deep_search", "pet_welfare_policy_reference_not_Green", "Stage2_reference", {"government_incentives_krw_bn": 100, "max_per_dog_krw": 600000, "dogs_to_rehome_context": "nearly_500000"}),
    Round320TriggerRecord("r12l16_csat_education_T0", "r12_loop16_csat_education_service_demand", "Stage2_education_exam_demand_reference", "2025-11-13", "CSAT applicants 554,174, +6% YoY, highest since 2019; ARPU and listed revenue bridge missing.", "price_data_unavailable_after_deep_search", "education_demand_stage2_reference_not_Green", "Stage2_reference", {"registered_applicants": 554174, "YoY_pct": 6, "affected_flights": 140}),
    Round320TriggerRecord("r12l16_birthrate_childcare_T0", "r12_loop16_birthrate_childcare_pipeline", "Stage2_demographic_childcare_reference", "2026-02-25", "Fertility rises to 0.80 from 0.75; births +6.8%, marriages +8.1%, Seoul fertility +8.9%; multi-year listed revenue bridge missing.", "price_data_unavailable_after_deep_search", "demographic_stage2_reference_not_Green", "Stage2_reference", {"fertility_2025": 0.80, "fertility_2024": 0.75, "births_change_pct": 6.8, "marriages_change_pct": 8.1}),
    Round320TriggerRecord("r12l16_medical_quota_relief_T1", "r12_loop16_medical_education_quota_freeze", "4B_medical_education_service_relief", "2025-03-07", "Medical quota relief after 13-month dispute; proposed about 3,000 annually and trainee walkout context around 90%. Service normalization still missing.", "price_data_unavailable_after_deep_search", "medical_education_service_relief_not_Green", "relief_reference", {"proposed_medical_student_number_annually_context": 3000, "dispute_duration_months": 13, "trainee_walkout_context_pct": 90}),
)

ROUND320_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B.value, "platform_MA_final_approval": "+5", "delivery_GMV_take_rate_conversion": "+5", "consumer_trust_security": "+0", "food_price_pass_through": "+0", "import_quota_margin_relief": "+0", "feed_cost_sensitivity": "+0", "pet_welfare_revenue_conversion": "+0", "education_demand_ARPU": "+0", "fertility_trend_durability": "+0", "service_disruption_normalization": "+0", "MA_headline_without_approval_penalty": "-5", "user_shift_without_revenue_penalty": "-1", "food_policy_without_company_margin_penalty": "-1", "commodity_cost_ignored_penalty": "-1", "stage2_actionable_promote": "final SPA/approval/financing", "stage3_yellow_gate": "GMV and take-rate pending", "stage3_green_gate": "approval+GMV+margin", "notes": "Baemin/Naver/Uber."},
    {"archetype": E2RArchetype.EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C.value, "platform_MA_final_approval": "+0", "delivery_GMV_take_rate_conversion": "+5", "consumer_trust_security": "+5", "food_price_pass_through": "+0", "import_quota_margin_relief": "+0", "feed_cost_sensitivity": "+0", "pet_welfare_revenue_conversion": "+0", "education_demand_ARPU": "+0", "fertility_trend_durability": "+0", "service_disruption_normalization": "+0", "MA_headline_without_approval_penalty": "-1", "user_shift_without_revenue_penalty": "-5", "food_policy_without_company_margin_penalty": "-1", "commodity_cost_ignored_penalty": "-1", "stage2_actionable_promote": "security 4C plus rival GMV conversion", "stage3_yellow_gate": "rival margin pending", "stage3_green_gate": "rival revenue+profit retention", "notes": "Coupang breach."},
    {"archetype": E2RArchetype.FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B.value, "platform_MA_final_approval": "+0", "delivery_GMV_take_rate_conversion": "+0", "consumer_trust_security": "+0", "food_price_pass_through": "+5", "import_quota_margin_relief": "+5", "feed_cost_sensitivity": "+2", "pet_welfare_revenue_conversion": "+0", "education_demand_ARPU": "+0", "fertility_trend_durability": "+0", "service_disruption_normalization": "+0", "MA_headline_without_approval_penalty": "-1", "user_shift_without_revenue_penalty": "-1", "food_policy_without_company_margin_penalty": "-5", "commodity_cost_ignored_penalty": "-3", "stage2_actionable_promote": "policy to margin bridge", "stage3_yellow_gate": "volume elasticity pending", "stage3_green_gate": "pass-through+gross margin", "notes": "food CPI/import quota."},
    {"archetype": E2RArchetype.FEED_WHEAT_COST_SHOCK_4B.value, "platform_MA_final_approval": "+0", "delivery_GMV_take_rate_conversion": "+0", "consumer_trust_security": "+0", "food_price_pass_through": "+1", "import_quota_margin_relief": "+0", "feed_cost_sensitivity": "+5", "pet_welfare_revenue_conversion": "+0", "education_demand_ARPU": "+0", "fertility_trend_durability": "+0", "service_disruption_normalization": "+0", "MA_headline_without_approval_penalty": "-1", "user_shift_without_revenue_penalty": "-1", "food_policy_without_company_margin_penalty": "-2", "commodity_cost_ignored_penalty": "-5", "stage2_actionable_promote": "none without pass-through", "stage3_yellow_gate": "margin recovery pending", "stage3_green_gate": "N/A until pass-through", "notes": "feed wheat."},
    {"archetype": E2RArchetype.PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE.value, "platform_MA_final_approval": "+0", "delivery_GMV_take_rate_conversion": "+0", "consumer_trust_security": "+0", "food_price_pass_through": "+0", "import_quota_margin_relief": "+0", "feed_cost_sensitivity": "+0", "pet_welfare_revenue_conversion": "+5", "education_demand_ARPU": "+0", "fertility_trend_durability": "+0", "service_disruption_normalization": "+0", "MA_headline_without_approval_penalty": "-1", "user_shift_without_revenue_penalty": "-1", "food_policy_without_company_margin_penalty": "-1", "commodity_cost_ignored_penalty": "-1", "stage2_actionable_promote": "listed pet-food/vet revenue", "stage3_yellow_gate": "subsidy execution pending", "stage3_green_gate": "listed revenue+margin", "notes": "dog-meat ban."},
    {"archetype": E2RArchetype.EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE.value, "platform_MA_final_approval": "+0", "delivery_GMV_take_rate_conversion": "+0", "consumer_trust_security": "+0", "food_price_pass_through": "+0", "import_quota_margin_relief": "+0", "feed_cost_sensitivity": "+0", "pet_welfare_revenue_conversion": "+0", "education_demand_ARPU": "+5", "fertility_trend_durability": "+1", "service_disruption_normalization": "+0", "MA_headline_without_approval_penalty": "-1", "user_shift_without_revenue_penalty": "-1", "food_policy_without_company_margin_penalty": "-1", "commodity_cost_ignored_penalty": "-1", "stage2_actionable_promote": "listed ARPU/revenue", "stage3_yellow_gate": "retention/margin pending", "stage3_green_gate": "ARPU+margin+retention", "notes": "CSAT."},
    {"archetype": E2RArchetype.FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE.value, "platform_MA_final_approval": "+0", "delivery_GMV_take_rate_conversion": "+0", "consumer_trust_security": "+0", "food_price_pass_through": "+0", "import_quota_margin_relief": "+0", "feed_cost_sensitivity": "+0", "pet_welfare_revenue_conversion": "+0", "education_demand_ARPU": "+2", "fertility_trend_durability": "+5", "service_disruption_normalization": "+0", "MA_headline_without_approval_penalty": "-1", "user_shift_without_revenue_penalty": "-1", "food_policy_without_company_margin_penalty": "-1", "commodity_cost_ignored_penalty": "-1", "stage2_actionable_promote": "childcare revenue bridge", "stage3_yellow_gate": "multi-year durability pending", "stage3_green_gate": "multi-year+listed revenue", "notes": "birthrate."},
    {"archetype": E2RArchetype.MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF.value, "platform_MA_final_approval": "+0", "delivery_GMV_take_rate_conversion": "+0", "consumer_trust_security": "+0", "food_price_pass_through": "+0", "import_quota_margin_relief": "+0", "feed_cost_sensitivity": "+0", "pet_welfare_revenue_conversion": "+0", "education_demand_ARPU": "+1", "fertility_trend_durability": "+0", "service_disruption_normalization": "+5", "MA_headline_without_approval_penalty": "-1", "user_shift_without_revenue_penalty": "-1", "food_policy_without_company_margin_penalty": "-1", "commodity_cost_ignored_penalty": "-1", "stage2_actionable_promote": "service normalization", "stage3_yellow_gate": "hospital revenue recovery pending", "stage3_green_gate": "trainee return+hospital revenue", "notes": "medical quota."},
)


def round320_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND320_CASE_CANDIDATES]


def round320_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND320_CASE_CANDIDATES]


def round320_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND320_TRIGGER_RECORDS]


def round320_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND320_SHADOW_WEIGHT_ROWS]


def round320_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND320_REQUIRED_TARGET_ALIASES.items()]


def round320_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND320_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND320_SCORE_DOWN_AXES]
    )


def round320_summary() -> dict[str, object]:
    return {
        "source_round": ROUND320_SOURCE_ROUND_PATH,
        "round_id": ROUND320_ANALYST_ROUND_ID,
        "large_sector": ROUND320_LARGE_SECTOR,
        "method": ROUND320_METHOD,
        "case_candidate_count": len(ROUND320_CASE_CANDIDATES),
        "trigger_count": len(ROUND320_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND320_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 0,
        "stage2_candidate_count": 6,
        "stage3_yellow_candidate_count": 5,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 7,
        "stage4c_watch_count": 3,
        "hard_4c_case_count": 1,
        "evidence_good_but_price_failed_or_unavailable_count": 6,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R13 Loop 16",
    }


def round320_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND320_SOURCE_ROUND_PATH,
        "round_id": ROUND320_ANALYST_ROUND_ID,
        "large_sector": ROUND320_LARGE_SECTOR,
        "method": ROUND320_METHOD,
        "summary": round320_summary(),
        "required_target_aliases": dict(ROUND320_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND320_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND320_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND320_STAGE3_GREEN_RULES,
        "green_blockers": ROUND320_GREEN_BLOCKERS,
        "score_up_axes": ROUND320_SCORE_UP_AXES,
        "score_down_axes": ROUND320_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND320_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND320_HARD_4C_GATES,
        "row_separation_rules": ROUND320_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round320_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_life_service_agri_education_pet_or_demographic_headline_as_Green_without_final_approval_revenue_margin_ARPU_pass_through_or_service_normalization",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round320_summary_markdown() -> str:
    summary = round320_summary()
    lines = [
        "# R12 Loop 16 Agriculture / Life Services / Misc Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: a CSAT applicant rebound can be Stage2 reference evidence, but it is not Green until listed education revenue, ARPU, retention and margin appear.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Baemin / Naver / Uber M&A is Stage2 reference, not Green before final SPA, approval, GMV and margin.",
            "- Coupang breach is hard 4C for trust, while rival share shift needs GMV and margin conversion.",
            "- Food inflation and import quota are Stage2/4B until pass-through, volume elasticity and gross margin are visible.",
            "- Feed wheat tender failure is 4B/4C cost-risk overlay, not a positive demand signal.",
            "- Dog-meat ban, CSAT, birthrate and medical-quota relief are policy or demand references only.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C confirmed: `1`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round320_trigger_grid_markdown() -> str:
    lines = [
        "# Round 320 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round320_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round320_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 320 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND320_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND320_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND320_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND320_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND320_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round320_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 320 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND320_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND320_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND320_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round320_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 320 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND320_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round320_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 320 Row Separation Plan",
        "",
        "Life-service, agriculture, education, pet and demographic headlines must be separated from trigger anchors and full OHLC windows.",
        "",
        "Easy example: dog-meat ban can support a pet-welfare watch case, but it is not a listed pet-food Stage2 until revenue or vet-service conversion appears.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND320_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round320_r12_loop16_reports(
    output_directory: str | Path = ROUND320_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND320_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND320_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND320_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND320_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round320_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND320_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round320_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round320_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round320_r12_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round320_r12_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round320_r12_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round320_r12_loop16_trigger_grid.md",
        "summary": output_dir / "round320_r12_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round320_r12_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round320_r12_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round320_r12_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round320_r12_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round320_r12_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round320_r12_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round320_case_rows())
    _write_csv(paths["target_aliases"], round320_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round320_trigger_rows())
    _write_csv(paths["score_adjustments"], round320_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round320_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round320_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round320_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round320_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round320_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round320_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round320_row_separation_plan_markdown(), encoding="utf-8")
    return paths


def _write_csv(path: Path, rows: Iterable[Mapping[str, str]]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_jsonl(path: Path, rows: Iterable[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    return [f"- {item}" for item in items]


__all__ = [
    "ROUND320_CASE_CANDIDATES",
    "ROUND320_GREEN_BLOCKERS",
    "ROUND320_HARD_4C_GATES",
    "ROUND320_LARGE_SECTOR",
    "ROUND320_REQUIRED_TARGET_ALIASES",
    "ROUND320_ROW_SEPARATION_RULES",
    "ROUND320_SCORE_DOWN_AXES",
    "ROUND320_SCORE_UP_AXES",
    "ROUND320_SHADOW_WEIGHT_ROWS",
    "ROUND320_STAGE2_ACTIONABLE_RULES",
    "ROUND320_STAGE3_GREEN_RULES",
    "ROUND320_STAGE3_YELLOW_RULES",
    "ROUND320_STAGE4B_WATCH_TRIGGERS",
    "ROUND320_TRIGGER_RECORDS",
    "render_round320_stage4b_4c_review_markdown",
    "render_round320_stage_rules_markdown",
    "render_round320_trigger_grid_markdown",
    "round320_audit_payload",
    "round320_case_records",
    "round320_case_rows",
    "round320_shadow_weight_rows",
    "round320_summary",
    "round320_trigger_rows",
    "write_round320_r12_loop16_reports",
]
