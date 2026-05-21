"""Round-326 R5 Loop-17 consumer, retail and brand trigger validation.

This module converts ``docs/round/round_326.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: Samyang's Buldak export case is Stage2-Actionable because ASP,
shipments, capacity and event price are all visible. It is not Stage3-Green
until repeat sell-through, margin durability and food-safety risk are checked.
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


ROUND326_SOURCE_ROUND_PATH = "docs/round/round_326.md"
ROUND326_ANALYST_ROUND_ID = "round_254"
ROUND326_LOOP_NAME = "R5 Loop 17"
ROUND326_LARGE_SECTOR = "CONSUMER_RETAIL_BRAND"
ROUND326_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND326_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round326_r5_loop17_consumer_retail_brand_trigger_validation"
ROUND326_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop17_round254.jsonl"
ROUND326_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r5_loop17_round254.jsonl"
ROUND326_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round326_r5_loop17_consumer_retail_brand_trigger_validation_audit.json"
ROUND326_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round254_r5_loop17_v1.csv"

ROUND326_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE": E2RArchetype.K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE.value,
    "K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW": E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW.value,
    "K_BEAUTY_INDIE_US_RETAIL_STAGE2": E2RArchetype.K_BEAUTY_INDIE_US_RETAIL_STAGE2.value,
    "CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE": E2RArchetype.CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE.value,
    "ECOMMERCE_TRUST_BREAK_HARD_4C": E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_4C.value,
    "FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B": E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B.value,
    "CHINA_PRESTIGE_BEAUTY_FAILED_RERATING": E2RArchetype.CHINA_PRESTIGE_BEAUTY_FAILED_RERATING.value,
    "K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE": E2RArchetype.K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE.value,
}

ROUND326_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct",
    "brand_export_ASP_shipment_capacity_two_or_more_confirmed",
    "overseas_revenue_mix_or_channel_expansion_confirmed",
    "tourism_or_retail_policy_stock_reaction_confirmed",
    "MAU_spending_GMV_or_delivery_volume_moves_with_platform_event",
    "M_and_A_final_SPA_binding_bid_or_approval_path_visible",
    "tariff_regulation_data_breach_or_China_weakness_4B_is_identified",
)

ROUND326_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "overseas_sellthrough_and_repeat_orders_visible",
    "margin_durability_after_tariff_or_distributor_fee_visible",
    "capacity_expansion_without_inventory_build_visible",
    "physical_retail_shelf_in_and_reorder_data_visible",
    "visitor_volume_basket_size_and_OP_conversion_visible",
    "MAU_spending_recovery_or_rival_GMV_conversion_visible",
    "final_MA_agreement_or_regulatory_approval_visible",
)

ROUND326_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "brand_demand_converts_into_repeat_revenue_and_margin",
    "overseas_channel_expansion_is_sellthrough_not_inventory_stuffing",
    "tourism_policy_converts_into_OP_not_only_visitor_count",
    "platform_trust_recovery_appears_in_MAU_spending_or_GMV",
    "M_and_A_finality_and_integration_economics_confirmed",
    "tariff_regulatory_and_China_weakness_4B_reduced",
    "full_window_MFE_MAE_available_and_supportive",
)

ROUND326_GREEN_BLOCKERS: tuple[str, ...] = (
    "viral_brand_without_sellthrough",
    "Kbeauty_export_without_offline_sales",
    "tourism_headline_without_basket_size",
    "legacy_china_exposure_ignored",
    "M_and_A_teaser_without_final_SPA",
    "trust_recovery_claim_without_spending",
    "supplier_regulation_ignored",
    "tariff_margin_ignored",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND326_SCORE_UP_AXES: tuple[str, ...] = (
    "export_ASP_shipment_capacity",
    "brand_viral_to_export_conversion",
    "overseas_revenue_mix",
    "US_retail_shelf_in",
    "tourism_policy_price_reaction",
    "consumer_trust_security",
    "MAU_spending_conversion",
    "M_and_A_finality",
)

ROUND326_SCORE_DOWN_AXES: tuple[str, ...] = (
    "viral_brand_without_sellthrough",
    "Kbeauty_export_without_offline_sales",
    "tourism_headline_without_basket_size",
    "legacy_china_exposure_ignored",
    "M_and_A_teaser_without_final_SPA",
    "trust_recovery_claim_without_spending",
    "supplier_regulation_ignored",
    "tariff_margin_ignored",
)

ROUND326_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "viral_brand_without_repeat_sellthrough",
    "US_tariff_risk_for_Kbeauty",
    "China_prestige_beauty_weakness",
    "tourism_visitor_count_without_basket_size",
    "data_breach_and_supplier_regulation",
    "M_and_A_teaser_without_final_SPA",
    "food_safety_or_recall_risk",
    "platform_growth_based_on_supplier_squeeze",
)

ROUND326_HARD_4C_GATES: tuple[str, ...] = (
    "consumer_trust_breach_with_MAU_spending_deterioration",
    "food_safety_issue_creates_sustained_overseas_ban",
    "platform_regulatory_sanction_changes_margin_model",
    "M_and_A_failure_after_price_premium",
    "China_demand_collapse_for_legacy_brand",
)

ROUND326_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_event_price_user_spending_deal_or_policy_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_viral_tourism_MA_or_private_reference_headline_as_Green_without_sellthrough_margin_basket_GMV_or_finality",
)


@dataclass(frozen=True)
class Round326TriggerRecord:
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
class Round326ShadowWeightRow:
    archetype: E2RArchetype
    export_asp_shipment_capacity: int
    brand_viral_to_export_conversion: int
    overseas_revenue_mix: int
    us_retail_shelf_in: int
    tourism_policy_price_reaction: int
    consumer_trust_security: int
    mau_spending_conversion: int
    ma_finality: int
    viral_brand_without_sellthrough_penalty: int
    kbeauty_export_without_offline_sales_penalty: int
    tourism_headline_without_basket_size_penalty: int
    legacy_china_exposure_ignored_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "export_ASP_shipment_capacity": _signed(self.export_asp_shipment_capacity),
            "brand_viral_to_export_conversion": _signed(self.brand_viral_to_export_conversion),
            "overseas_revenue_mix": _signed(self.overseas_revenue_mix),
            "US_retail_shelf_in": _signed(self.us_retail_shelf_in),
            "tourism_policy_price_reaction": _signed(self.tourism_policy_price_reaction),
            "consumer_trust_security": _signed(self.consumer_trust_security),
            "MAU_spending_conversion": _signed(self.mau_spending_conversion),
            "M&A_finality": _signed(self.ma_finality),
            "viral_brand_without_sellthrough_penalty": _signed(self.viral_brand_without_sellthrough_penalty),
            "Kbeauty_export_without_offline_sales_penalty": _signed(self.kbeauty_export_without_offline_sales_penalty),
            "tourism_headline_without_basket_size_penalty": _signed(self.tourism_headline_without_basket_size_penalty),
            "legacy_china_exposure_ignored_penalty": _signed(self.legacy_china_exposure_ignored_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round326CaseCandidate:
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
            "do_not_use_round326_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_viral_tourism_MA_or_private_reference_headline_as_Green_without_sellthrough_margin_basket_GMV_or_finality",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")

        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "tariff" in field
            or "recall" in field
            or "teaser" in field
            or "China" in field
            or "supplier" in field
            or "basket" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "trust_breach" in field
            or "data_breach" in field
            or "thesis_break" in field
            or "China_demand_collapse" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND326_LARGE_SECTOR,
            large_sector=ROUND326_LARGE_SECTOR,
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
            must_have_fields=ROUND326_STAGE3_GREEN_RULES,
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
                stage2_price=_float_or_none(self.extra_price_metrics.get("entry_price_krw")),
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8,
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


ROUND326_CASE_CANDIDATES: tuple[Round326CaseCandidate, ...] = (
    Round326CaseCandidate(
        "r5_loop17_samyang_buldak_export",
        "003230",
        "Samyang Foods",
        E2RArchetype.K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE,
        (E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, E2RArchetype.FOOD_SAFETY_RECALL_OVERLAY),
        "success_candidate",
        "Stage2_Actionable_K_food_export_with_regulatory_4B",
        "T1/T3",
        "Stage2-Actionable_K_food_export_with_regulatory_4B",
        "Stage2-Actionable",
        date(2023, 1, 1),
        date(2024, 6, 14),
        None,
        date(2024, 6, 14),
        None,
        False,
        ("Buldak_ASP_increase", "US_Europe_shipments", "capacity_expansion", "Q2_OP_estimate_plus_84pct", "target_price_raise_26pct", "shares_plus_5_7pct_close_647000"),
        ("food_safety_regulation_4B", "spiciness_recall_risk", "viral_trend_fatigue", "capacity_margin_execution"),
        5.7,
        None,
        {"trigger_date": "2024-06-14", "op_estimate_q2_2024_krw_bn": 81.2, "op_estimate_yoy_pct": 84, "target_price_krw": 830000, "target_price_raise_pct": 26, "event_return_pct": 5.7, "entry_price_krw": 647000},
        "aligned",
        "excellent_stage2_actionable_k_food_export",
        "true_rerating",
        "stage2_watch_success",
        "Samyang/Buldak has ASP, shipment, capacity, OP estimate and event price anchors, but food-safety and repeat sell-through gates block Green.",
    ),
    Round326CaseCandidate(
        "r5_loop17_apr_medicube_beauty_device",
        "278470",
        "APR / Medicube",
        E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW,
        (E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B, E2RArchetype.BEAUTY_DEVICE_REGULATORY_SAFETY),
        "success_candidate",
        "Stage2_promote_candidate_K_beauty_device",
        "T1/T3",
        "Stage2_promote_candidate_K_beauty_device",
        "Stage3-Yellow_candidate",
        date(2025, 1, 1),
        date(2025, 10, 20),
        None,
        date(2025, 10, 20),
        None,
        False,
        ("stock_more_than_4x_since_Jan_2025", "market_value_about_6B_usd", "overseas_revenue_nearly_80pct", "device_about_one_third_of_US_sales"),
        ("celebrity_virality_overheat_4B", "US_tariff", "beauty_device_regulation", "repeat_purchase_unknown"),
        None,
        None,
        {"trigger_date": "2025-10-20", "reported_stock_return_since_jan_2025": ">4x", "market_value_context_usd_bn": 6, "device_price_usd_context": 180, "overseas_revenue_share_q2_2025_pct": "nearly_80", "device_share_of_us_sales_context": "about_one_third"},
        "aligned",
        "Stage3_Yellow_candidate_K_beauty_device_not_Green",
        "true_rerating",
        "yellow_success",
        "APR/Medicube is a strong K-beauty device Stage2/Yellow candidate, but celebrity virality, tariff and regulation remain 4B gates.",
    ),
    Round326CaseCandidate(
        "r5_loop17_kbeauty_indie_us_retail",
        "483650/257720/CJ_Olive_Young_readthrough/090430",
        "d'Alba / Silicon2 / Olive Young / Amorepacific readthrough",
        E2RArchetype.K_BEAUTY_INDIE_US_RETAIL_STAGE2,
        (E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL, E2RArchetype.K_BEAUTY_INDIE_PHYSICAL_STORE_TEST),
        "success_candidate",
        "Stage2_K_beauty_US_retail_channel",
        "T0/T3",
        "Stage2_Kbeauty_US_retail_channel",
        "Stage2",
        date(2025, 6, 5),
        date(2025, 6, 5),
        None,
        date(2025, 6, 5),
        None,
        False,
        ("Korea_top_US_cosmetics_exporter_2024", "top5_Korean_US_ecommerce_growth_71pct", "overall_US_market_growth_21pct", "dAlba_more_than_2x_since_debut"),
        ("US_tariff_10_to_25pct_4B", "brand_saturation", "COSRX_growth_plateau", "offline_sellthrough_unknown"),
        None,
        None,
        {"trigger_date": "2025-06-05", "korea_us_cosmetics_export_rank_2024": 1, "top5_korean_us_ecommerce_sales_growth_2yr_pct": 71, "overall_us_market_growth_2yr_pct": 21, "dalba_share_return_since_debut": ">2x"},
        "aligned",
        "Stage2_kbeauty_channel_expansion_not_Green",
        "true_rerating",
        "stage2_watch_success",
        "Indie K-beauty U.S. e-commerce and channel expansion are Stage2, but physical-store sell-through and tariff margin are the Yellow/Green gates.",
    ),
    Round326CaseCandidate(
        "r5_loop17_china_visa_free_tourism_retail",
        "069960/008770/034230/123690",
        "Hyundai Department Store / Hotel Shilla / Paradise / Hankook Cosmetics",
        E2RArchetype.CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE,
        (E2RArchetype.CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE, E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT),
        "event_premium",
        "Stage2_Actionable_tourism_retail_policy",
        "T1/T3",
        "Stage2-Actionable_tourism_retail_policy",
        "Stage2-Actionable",
        date(2025, 3, 20),
        date(2025, 8, 6),
        None,
        date(2025, 8, 6),
        None,
        False,
        ("visa_free_period_2025_09_29_to_2026_06", "Hyundai_Dept_plus_7_1pct", "Hotel_Shilla_plus_4_8pct", "Paradise_plus_2_9pct", "Hankook_Cosmetics_plus_9_9pct"),
        ("temporary_policy_window_4B", "low_spend_budget_tourism", "experience_over_shopping", "anti_chinese_rally_risk", "duty_free_basket_size_unknown"),
        9.9,
        None,
        {"trigger_date": "2025-08-06", "visa_free_period": "2025-09-29_to_2026-06", "hyundai_department_store_event_return_pct": 7.1, "hotel_shilla_event_return_pct": 4.8, "paradise_event_return_pct": 2.9, "hankook_cosmetics_event_return_pct": 9.9, "pilot_rules": "groups_of_3_or_more_can_stay_15_days"},
        "aligned",
        "excellent_stage2_actionable_china_tourism_retail",
        "event_premium",
        "stage2_watch_success",
        "Chinese visa-free policy created a clear retail/tourism Stage2 event, but basket size and OP conversion are still missing.",
    ),
    Round326CaseCandidate(
        "r5_loop17_coupang_trust_break_retail_shift",
        "CPNG/035420/139480/000120/retail_basket",
        "Coupang / Naver / E-Mart / CJ Logistics",
        E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_4C,
        (E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C, E2RArchetype.DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY),
        "4c_thesis_break",
        "hard_4C_ecommerce_trust_break_with_rival_stage2",
        "T0/T5",
        "hard_4C_ecommerce_trust_break_with_rival_stage2",
        "4C + rival Stage2",
        date(2025, 11, 1),
        date(2026, 2, 25),
        None,
        date(2026, 2, 26),
        date(2026, 2, 25),
        True,
        ("affected_users_34M", "Coupang_return_since_breach_minus_34pct", "MAU_minus_3_5pct", "daily_spending_minus_6_3pct", "Naver_users_plus_23pct", "CJ_Logistics_volume_plus_120pct", "Q4_loss_26M_usd", "KFTC_fine_2_2B_won"),
        ("data_breach_hard_4C", "supplier_pressure_regulation_4B", "delayed_vendor_payments", "trust_recovery_uncertain"),
        None,
        -34.0,
        {"affected_users_mn": 34, "coupang_return_since_breach_pct": -34, "mobile_mau_change_pct": -3.5, "daily_spending_change_pct": -6.3, "daily_spending_krw_bn": 139.2, "naver_online_users_change_pct": 23, "cj_logistics_overnight_one_day_volume_yoy_pct": 120, "q4_2025_loss_usd_mn": 26, "q4_2025_revenue_usd_bn": 8.8, "kftc_fine_krw_bn": 2.2},
        "aligned",
        "hard_4C_success_with_rival_stage2_and_recovery_watch",
        "thesis_break",
        "should_have_been_red",
        "Coupang is a hard 4C trust-break reference; rivals remain Stage2 until GMV, revenue and margin conversion are visible.",
    ),
    Round326CaseCandidate(
        "r5_loop17_baemin_uber_naver_ma",
        "035420/UBER/Delivery_Hero_readthrough",
        "Naver / Uber / Delivery Hero / Baemin",
        E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B,
        (E2RArchetype.FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B,),
        "event_premium",
        "Stage2_food_delivery_MA_with_approval_4B",
        "T0/T3",
        "Stage2_food_delivery_platform_MA",
        "Stage2 + 4B-watch",
        date(2026, 5, 18),
        date(2026, 5, 18),
        None,
        date(2026, 5, 18),
        None,
        False,
        ("Baemin_bid_value_8T_won", "bid_value_5_34B_usd", "Uber_Naver_80_20_consortium", "Delivery_Hero_plus_5_6pct"),
        ("final_SPA_missing_4B", "regulatory_approval", "financing", "integration", "commission_regulation", "Naver_economics_missing"),
        5.6,
        None,
        {"trigger_date": "2026-05-18", "baemin_bid_value_krw_trn": 8.0, "baemin_bid_value_usd_bn": 5.34, "consortium_ratio": "Uber_80pct_Naver_20pct", "naver_status": "teaser_letter_received_no_final_decision", "uber_delivery_hero_stake_pct": 19.5, "delivery_hero_stake_value_eur_bn": 1.7, "delivery_hero_event_return_pct": 5.6},
        "aligned",
        "Stage2_platform_MA_not_Green",
        "event_premium",
        "stage2_watch_success",
        "Baemin/Uber/Naver is Stage2 M&A, but teaser status, approval and economics block Actionable/Green.",
    ),
    Round326CaseCandidate(
        "r5_loop17_amorepacific_china_prestige_failed_rerating",
        "090430",
        "Amorepacific",
        E2RArchetype.CHINA_PRESTIGE_BEAUTY_FAILED_RERATING,
        (E2RArchetype.LEGACY_BEAUTY_CHINA_EXPOSURE_4C, E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C),
        "failed_rerating",
        "failed_rerating_china_prestige_beauty",
        "T0/T3",
        "failed_rerating_china_prestige_beauty",
        "failed_rerating + 4B-watch",
        date(2024, 8, 1),
        None,
        None,
        date(2024, 8, 1),
        None,
        False,
        ("worst_market_day_since_listing_context", "weak_China_demand", "C_beauty_competition", "prestige_beauty_pressure"),
        ("legacy_china_exposure_4B", "US_Europe_mix_shift_missing", "COSRX_growth_reacceleration_missing", "gross_margin_recovery_missing"),
        None,
        None,
        {"trigger_period": "2024-08", "reported_price_context": "worst_market_day_since_listing_14_years"},
        "evidence_good_but_price_failed",
        "failed_rerating_china_exposure_4B",
        "no_rerating",
        "should_have_been_red",
        "Amorepacific separates China-exposed prestige beauty from U.S.-focused indie K-beauty; macro K-beauty evidence cannot be copied across.",
    ),
    Round326CaseCandidate(
        "r5_loop17_dr_g_loreal_kbeauty_ma",
        "Gowoonsesang_private/K_beauty_MA_reference/090430_readthrough",
        "Dr.G / Gowoonsesang / L'Oreal",
        E2RArchetype.K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE,
        (E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION, E2RArchetype.K_BEAUTY_BRAND_MNA_VALIDATION_STAGE2_REFERENCE),
        "event_premium",
        "Stage2_K_beauty_MA_valuation_reference_no_price",
        "T0/T2",
        "Stage2_Kbeauty_MA_reference_no_price",
        "Stage2 reference",
        date(2024, 12, 23),
        date(2024, 12, 23),
        None,
        date(2024, 12, 23),
        None,
        False,
        ("L_Oreal_acquires_Gowoonsesang_Dr_G", "global_growth_potential", "pan_Asian_presence", "valuation_undisclosed"),
        ("direct_price_anchor_missing", "valuation_undisclosed", "direct_listed_beneficiary_missing", "China_slowdown_4B"),
        None,
        None,
        {"trigger_date": "2024-12-23", "buyer": "L_Oreal", "target": "Gowoonsesang_Cosmetics_Dr_G", "valuation": "undisclosed", "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "Stage2_MA_reference_not_actionable",
        "event_premium",
        "stage2_watch_success",
        "Dr.G/L'Oreal validates K-beauty M&A appetite, but no valuation or public-stock price anchor means reference only.",
    ),
)

ROUND326_TRIGGER_RECORDS: tuple[Round326TriggerRecord, ...] = (
    Round326TriggerRecord("r5l17_samyang_buldak_T1", "r5_loop17_samyang_buldak_export", "Stage2-Actionable_K_food_export", "2024-06-14", "reported_event_anchor", 5.7, "excellent_stage2_actionable_k_food_export", "Stage2-Actionable", {"entry_price_krw": 647000, "target_price_krw": 830000, "op_estimate_yoy_pct": 84}),
    Round326TriggerRecord("r5l17_samyang_denmark_T3", "r5_loop17_samyang_buldak_export", "4B_food_safety_regulatory_watch", "2024-06_to_2024-08", "reported_event_anchor", "price_data_unavailable_after_deep_search", "regulatory_4B_but_brand_resilience", "4B-watch", {"recall_risk": "spiciness_recall_risk"}),
    Round326TriggerRecord("r5l17_apr_medicube_T1", "r5_loop17_apr_medicube_beauty_device", "Stage3-Yellow_candidate_K_beauty_device", "2025-10-20", "reported_event_anchor", "reported_>4x_since_Jan_2025", "Stage3_Yellow_candidate_not_Green", "Stage3-Yellow_candidate", {"market_value_context_usd_bn": 6, "overseas_revenue_share_q2_2025_pct": "nearly_80"}),
    Round326TriggerRecord("r5l17_kbeauty_us_channel_T0", "r5_loop17_kbeauty_indie_us_retail", "Stage2_Kbeauty_US_ecommerce_retail", "2025-06-05", "reported_event_anchor", "dAlba_>2x_since_debut", "Stage2_channel_expansion_not_Green", "Stage2", {"top5_korean_us_ecommerce_sales_growth_2yr_pct": 71, "overall_us_market_growth_2yr_pct": 21}),
    Round326TriggerRecord("r5l17_china_tourism_T1", "r5_loop17_china_visa_free_tourism_retail", "Stage2-Actionable_tourism_retail_policy", "2025-08-06", "reported_event_anchor", "Hyundai_Dept_+7.1_Hotel_Shilla_+4.8_Hankook_Cosmetics_+9.9", "excellent_stage2_actionable_china_tourism_retail", "Stage2-Actionable", {"visa_free_period": "2025-09-29_to_2026-06"}),
    Round326TriggerRecord("r5l17_coupang_breach_T1", "r5_loop17_coupang_trust_break_retail_shift", "hard_4C_ecommerce_trust_break", "2025-11_to_2026-02", "reported_event_anchor", -34, "hard_4C_success", "4C", {"affected_users_mn": 34, "mobile_mau_change_pct": -3.5, "daily_spending_change_pct": -6.3}),
    Round326TriggerRecord("r5l17_coupang_rival_T2", "r5_loop17_coupang_trust_break_retail_shift", "rival_Stage2_retail_share_shift", "2026-02-25", "reported_event_anchor", "price_data_unavailable_after_deep_search", "rival_stage2_needs_revenue_margin", "Stage2", {"naver_online_users_change_pct": 23, "cj_logistics_overnight_one_day_volume_yoy_pct": 120}),
    Round326TriggerRecord("r5l17_baemin_naver_T0", "r5_loop17_baemin_uber_naver_ma", "Stage2_food_delivery_platform_MA", "2026-05-18", "reported_event_anchor", "Delivery_Hero_proxy_+5.6", "Stage2_MA_not_Green", "Stage2+4B", {"baemin_bid_value_krw_trn": 8.0, "delivery_hero_event_return_pct": 5.6}),
    Round326TriggerRecord("r5l17_amore_china_T0", "r5_loop17_amorepacific_china_prestige_failed_rerating", "failed_rerating_china_prestige_beauty", "2024-08", "reported_event_anchor", "price_data_unavailable_after_deep_search", "legacy_china_exposure_4B", "4B-watch", {"reported_price_context": "worst_market_day_since_listing_14_years"}),
    Round326TriggerRecord("r5l17_dr_g_loreal_T0", "r5_loop17_dr_g_loreal_kbeauty_ma", "Stage2_Kbeauty_MA_reference_no_price", "2024-12-23", "reported_event_anchor", "price_data_unavailable_after_deep_search", "MA_reference_not_actionable", "Stage2_reference", {"buyer": "L_Oreal", "valuation": "undisclosed"}),
)

ROUND326_SHADOW_WEIGHT_ROWS: tuple[Round326ShadowWeightRow, ...] = (
    Round326ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE, 5, 5, 3, 2, 0, 1, 0, 0, -5, -1, -1, -1, "Samyang Buldak export", "regulatory/viral risk", "repeat sell-through+margin+capacity", "Samyang"),
    Round326ShadowWeightRow(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW, 2, 5, 5, 3, 0, 1, 0, 0, -5, -3, -1, -1, "APR device global momentum", "overheat/regulation/tariff", "repeat device sales+margin", "APR"),
    Round326ShadowWeightRow(E2RArchetype.K_BEAUTY_INDIE_US_RETAIL_STAGE2, 1, 4, 4, 5, 0, 1, 0, 0, -4, -5, -1, -2, "U.S. K-beauty ecommerce growth", "physical sell-through missing", "retail reorder+margin", "d'Alba/Silicon2/Olive Young"),
    Round326ShadowWeightRow(E2RArchetype.CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE, 0, 1, 1, 0, 5, 1, 0, 0, -1, -1, -5, -2, "visa-free Chinese tourism stock reaction", "basket size missing", "visitor volume+basket+OP", "Hotel Shilla/Hyundai Dept"),
    Round326ShadowWeightRow(E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_4C, 0, 0, 0, 0, 0, 5, 5, 0, -1, -1, -1, -1, "Coupang breach damaged trust", "hard 4C", "rival GMV/margin conversion", "Coupang/Naver/CJ"),
    Round326ShadowWeightRow(E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B, 0, 1, 0, 0, 0, 1, 3, 5, -1, -1, -1, -1, "Baemin M&A headline", "final SPA missing", "approval+economics", "Baemin/Naver/Uber"),
    Round326ShadowWeightRow(E2RArchetype.CHINA_PRESTIGE_BEAUTY_FAILED_RERATING, 0, 0, 2, 1, 1, 0, 0, 0, -1, -1, -1, -5, "Amore China exposure", "failed rerating", "US/EU mix+margin recovery", "Amorepacific"),
    Round326ShadowWeightRow(E2RArchetype.K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE, 0, 2, 2, 2, 0, 0, 0, 3, -2, -1, -1, -1, "Dr.G L'Oreal M&A reference", "no valuation/public price", "valuation comps+listed beneficiary", "Dr.G"),
)


def round326_case_records() -> tuple[E2RCaseRecord, ...]:
    records = tuple(candidate.to_case_record() for candidate in ROUND326_CASE_CANDIDATES)
    for record in records:
        record.validate()
    return records


def round326_case_rows() -> list[dict[str, str]]:
    return [candidate.as_row() for candidate in ROUND326_CASE_CANDIDATES]


def round326_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND326_TRIGGER_RECORDS]


def round326_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND326_SHADOW_WEIGHT_ROWS]


def round326_summary() -> dict[str, object]:
    return {
        "source_round": ROUND326_SOURCE_ROUND_PATH,
        "round_id": ROUND326_ANALYST_ROUND_ID,
        "loop_name": ROUND326_LOOP_NAME,
        "large_sector": ROUND326_LARGE_SECTOR,
        "method": ROUND326_METHOD,
        "case_candidate_count": len(ROUND326_CASE_CANDIDATES),
        "trigger_count": len(ROUND326_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND326_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": sum(1 for case in ROUND326_CASE_CANDIDATES if "Stage2-Actionable" in case.stage_candidate),
        "stage2_candidate_count": sum(1 for case in ROUND326_CASE_CANDIDATES if "Stage2" in case.stage_candidate),
        "stage3_yellow_candidate_count": sum(1 for case in ROUND326_CASE_CANDIDATES if "Yellow" in case.stage_candidate),
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in ROUND326_CASE_CANDIDATES if case.stage4b_date is not None),
        "hard_4c_case_count": sum(1 for case in ROUND326_CASE_CANDIDATES if case.hard_4c_confirmed),
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round326_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND326_SOURCE_ROUND_PATH,
        "round_id": ROUND326_ANALYST_ROUND_ID,
        "large_sector": ROUND326_LARGE_SECTOR,
        "method": ROUND326_METHOD,
        "summary": round326_summary(),
        "target_archetypes": dict(ROUND326_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND326_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND326_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND326_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND326_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND326_SCORE_UP_AXES),
        "score_down_axes": list(ROUND326_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND326_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND326_HARD_4C_GATES),
        "row_separation_rules": list(ROUND326_ROW_SEPARATION_RULES),
        "shadow_weights": round326_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_change_production_scoring",
            "do_not_use_round326_cases_as_candidate_generation_input",
            "do_not_force_Stage3_Green",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_viral_tourism_MA_or_private_reference_headline_as_Green_without_sellthrough_margin_basket_GMV_or_finality",
        ],
    }


def render_round326_summary_markdown() -> str:
    summary = round326_summary()
    lines = [
        "# Round 326 R5 Loop 17 Consumer Retail Brand Trigger Validation",
        "",
        f"- source_round: `{ROUND326_SOURCE_ROUND_PATH}`",
        f"- analyst_round_id: `{ROUND326_ANALYST_ROUND_ID}`",
        f"- large_sector: `{ROUND326_LARGE_SECTOR}`",
        f"- method: `{ROUND326_METHOD}`",
        f"- case candidates: `{summary['case_candidate_count']}`",
        f"- triggers: `{summary['trigger_count']}`",
        f"- Stage2-Actionable candidates: `{summary['stage2_actionable_candidate_count']}`",
        f"- Stage3-Yellow candidates: `{summary['stage3_yellow_candidate_count']}`",
        "- Stage3-Green confirmed: `0`",
        "- production_scoring_changed: `false`",
        "- candidate_generation_input: `false`",
        "- shadow_weight_only: `true`",
        "",
        "## 핵심 결론",
        "",
        "- Samyang/Buldak은 ASP, U.S./Europe shipment, capacity, OP estimate와 +5.7% 가격 anchor가 같이 닫힌 Stage2-Actionable이다.",
        "- APR/Medicube는 해외 매출 비중과 주가 rerating이 강하지만 celebrity/viral, tariff, device regulation 때문에 Yellow 후보로 둔다.",
        "- K-beauty indie/Silicon2/d'Alba는 U.S. e-commerce와 channel 확장이 Stage2지만 physical-store sell-through가 Green gate다.",
        "- China visa-free tourism은 retail basket price reaction이 강한 Stage2-Actionable이지만 basket size와 OP conversion이 필요하다.",
        "- Coupang은 MAU/spending 악화가 붙은 hard 4C이며, rival Stage2는 GMV/revenue/margin conversion을 요구한다.",
        "- Baemin/Naver/Uber는 Stage2 M&A지만 final SPA, approval, Naver economics 전에는 Green 금지다.",
        "- Amorepacific은 China prestige failed rerating으로, U.S.-focused indie K-beauty와 분리해야 한다.",
        "- Dr.G/L'Oreal은 K-beauty M&A reference일 뿐 valuation과 listed price anchor가 없어 Actionable이 아니다.",
    ]
    return "\n".join(lines) + "\n"


def render_round326_trigger_grid_markdown() -> str:
    lines = [
        "# Round 326 R5 Loop 17 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | date | event_return | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round326_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round326_stage_rules_markdown() -> str:
    sections = [
        ("Stage2-Actionable Rules", ROUND326_STAGE2_ACTIONABLE_RULES),
        ("Stage3-Yellow Rules", ROUND326_STAGE3_YELLOW_RULES),
        ("Stage3-Green Rules", ROUND326_STAGE3_GREEN_RULES),
        ("Green Blockers", ROUND326_GREEN_BLOCKERS),
        ("Score Up Axes", ROUND326_SCORE_UP_AXES),
        ("Score Down Axes", ROUND326_SCORE_DOWN_AXES),
        ("Row Separation Rules", ROUND326_ROW_SEPARATION_RULES),
    ]
    lines = ["# Round 326 R5 Loop 17 Stage Rules", "", "Do not apply these weights to production scoring yet.", ""]
    for title, values in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(f"- `{value}`" for value in values)
        lines.append("")
    return "\n".join(lines)


def render_round326_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 326 R5 Loop 17 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- `{item}`" for item in ROUND326_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{item}`" for item in ROUND326_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND326_CASE_CANDIDATES:
        lines.append(f"- `{case.case_id}`: {case.stage_candidate}; {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round326_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 326 R5 Loop 17 Price Validation Plan",
            "",
            "Full adjusted OHLC is still unavailable for this round.",
            "Reported event anchors are stored separately from future OHLC backfill rows.",
            "",
            "Required future backfill:",
            "- adjusted OHLC around each trigger date",
            "- MFE/MAE 30D/90D/180D/1Y",
            "- below-entry and drawdown-after-peak flags",
            "- basket-level validation for tourism and K-beauty where a single listed beneficiary is ambiguous",
            "- no invented price paths",
        ]
    ) + "\n"


def _write_json(path: str | Path, payload: Mapping[str, object]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return path


def _write_jsonl(path: str | Path, rows: Iterable[Mapping[str, object]]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False, sort_keys=True, default=_json_default) + "\n")
    return path


def _write_csv(path: str | Path, rows: Iterable[Mapping[str, str]]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_round326_r5_loop17_reports(
    output_directory: str | Path = ROUND326_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND326_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND326_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND326_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND326_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    cases = write_case_library(round326_case_records(), cases_path)
    triggers = _write_jsonl(triggers_path, (trigger.as_dict() for trigger in ROUND326_TRIGGER_RECORDS))
    audit = _write_json(audit_path, round326_audit_payload())
    weights = _write_csv(weight_profile_path, round326_shadow_weight_rows())

    paths = {
        "cases": cases,
        "triggers": triggers,
        "audit": audit,
        "weight_profile": weights,
        "case_matrix": _write_csv(output_directory / "round326_r5_loop17_case_matrix.csv", round326_case_rows()),
        "trigger_grid": _write_csv(output_directory / "round326_r5_loop17_trigger_grid.csv", round326_trigger_rows()),
        "shadow_weights": _write_csv(output_directory / "round326_r5_loop17_shadow_weights.csv", round326_shadow_weight_rows()),
        "summary": output_directory / "round326_r5_loop17_consumer_retail_brand_summary.md",
        "trigger_grid_md": output_directory / "round326_r5_loop17_trigger_grid.md",
        "stage_rules": output_directory / "round326_r5_loop17_stage_rules.md",
        "stage4b_4c_review": output_directory / "round326_r5_loop17_stage4b_4c_review.md",
        "price_validation_plan": output_directory / "round326_r5_loop17_price_validation_plan.md",
    }
    paths["summary"].write_text(render_round326_summary_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round326_trigger_grid_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round326_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round326_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round326_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def _signed(value: int) -> str:
    return f"{value:+d}" if value else "+0"


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_or_none(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, default=_json_default)
    return str(value)


def _json_default(value: object) -> str:
    if isinstance(value, date):
        return value.isoformat()
    return str(value)
