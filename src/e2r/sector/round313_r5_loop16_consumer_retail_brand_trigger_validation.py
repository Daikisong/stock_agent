"""Round-313 R5 Loop-16 consumer, retail and brand trigger validation.

This module converts ``docs/round/round_313.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a Chinese-tourism policy can move duty-free stocks on the event
date. It is still Stage2 until visitor count, per-capita spend and margin are
visible as of the replay date.
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


ROUND313_SOURCE_ROUND_PATH = "docs/round/round_313.md"
ROUND313_ANALYST_ROUND_ID = "round_241"
ROUND313_LARGE_SECTOR = "CONSUMER_RETAIL_BRANDS"
ROUND313_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND313_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round313_r5_loop16_consumer_retail_brand_trigger_validation"
ROUND313_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop16_round241.jsonl"
ROUND313_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r5_loop16_round241.jsonl"
ROUND313_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round313_r5_loop16_consumer_retail_brand_trigger_validation_audit.json"
ROUND313_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round241_r5_loop16_v1.csv"

ROUND313_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW": E2RArchetype.KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW.value,
    "KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE": E2RArchetype.KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE.value,
    "BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B": E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B.value,
    "CHINA_TOURISM_DUTYFREE_STAGE2_EVENT": E2RArchetype.CHINA_TOURISM_DUTYFREE_STAGE2_EVENT.value,
    "ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2": E2RArchetype.ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2.value,
    "RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B": E2RArchetype.RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B.value,
    "OFFLINE_GROCERY_RESTRUCTURING_HARD_4C": E2RArchetype.OFFLINE_GROCERY_RESTRUCTURING_HARD_4C.value,
    "SHRINKFLATION_PRICE_REGULATION_4C_WATCH": E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH.value,
}

ROUND313_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "export_ASP_shipment_capacity_or_offline_channel_metric_is_specific",
    "OP_EPS_estimate_revision_or_reported_margin_bridge_exists",
    "event_return_at_least_5pct_or_reported_price_anchor_supports_trigger",
    "overseas_channel_or_platform_shift_is_linked_to_sales_spending_delivery_volume_or_margin",
    "hard_security_restructuring_or_price_regulation_gate_is_not_dominant_for_positive_candidate",
)

ROUND313_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_repeat_margin_sellthrough_GMV_conversion_or_recurring_revenue_gate_remains_open",
    "reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing",
    "case_is_not_pure_policy_viral_JV_or_regulatory_headline",
)

ROUND313_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "export_or_brand_channel_evidence_converts_to_quarterly_OP_and_margin",
    "overseas_channel_sales_are_sell_through_not_inventory_push",
    "tourism_event_converts_to_visitor_spending_and_margin",
    "platform_share_capture_converts_to_GMV_and_delivery_margin",
    "data_security_price_regulation_and_restructuring_hard_gates_are_absent",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND313_GREEN_BLOCKERS: tuple[str, ...] = (
    "viral_brand_without_margin",
    "tourism_policy_without_spending",
    "ecommerce_user_shift_without_GMV",
    "JV_without_integration_economics",
    "offline_retail_assets_without_cashflow",
    "hidden_price_increase_without_disclosure",
    "post_IPO_or_YTD_rally_without_trigger_OHLC",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND313_SCORE_UP_AXES: tuple[str, ...] = (
    "export_ASP_shipment_capacity",
    "US_physical_channel_sellthrough",
    "overseas_revenue_mix",
    "repeat_purchase_or_recurring_revenue",
    "tourist_arrival_spending_margin",
    "platform_security_trust",
    "rival_share_capture",
    "retail_restructuring_risk",
    "pricing_transparency_regulation",
)

ROUND313_SCORE_DOWN_AXES: tuple[str, ...] = (
    "brand_viral_without_margin",
    "tourism_policy_without_spend",
    "ecommerce_user_shift_without_GMV",
    "JV_without_integration_economics",
    "offline_retail_assets_without_cashflow",
    "hidden_price_increase_without_disclosure",
    "post_IPO_or_YTD_rally_without_trigger_OHLC",
)

ROUND313_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "viral_beauty_or_device_stock_rises_before_repeat_sales_margin",
    "tourism_policy_moves_stocks_before_visitor_spending",
    "ecommerce_rival_stocks_move_before_GMV_conversion",
    "JV_or_MA_announced_before_integration_economics",
    "K_food_single_product_concentration_becomes_excessive",
    "shrinkflation_or_price_regulation_limits_hidden_ASP_pass_through",
)

ROUND313_4C_WATCH_GATES: tuple[str, ...] = (
    "ecommerce_data_breach_customer_trust_collapse",
    "offline_retail_court_restructuring_liquidation_value_above_going_concern",
    "hidden_price_increase_regulation_blocks_ASP_pass_through",
    "food_safety_recall_or_contamination",
    "tourism_demand_collapse_due_geopolitics_or_safety_image",
    "brand_channel_saturation_and_inventory_write_down",
)

ROUND313_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_user_spending_channel_policy_or_regulation_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_brand_channel_policy_JV_or_user_shift_headline_as_Green_without_margin_sellthrough_GMV_or_FCF",
)


@dataclass(frozen=True)
class Round313ShadowWeightRow:
    archetype: E2RArchetype
    export_asp_shipment_capacity: int
    us_physical_channel_sellthrough: int
    overseas_revenue_mix: int
    repeat_purchase_or_recurring_revenue: int
    tourist_arrival_spending_margin: int
    platform_security_trust: int
    rival_share_capture: int
    retail_restructuring_risk: int
    pricing_transparency_regulation: int
    brand_viral_without_margin_penalty: int
    tourism_policy_without_spend_penalty: int
    ecommerce_user_shift_without_gmv_penalty: int
    jv_without_integration_economics_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "export_ASP_shipment_capacity": _signed(self.export_asp_shipment_capacity),
            "US_physical_channel_sellthrough": _signed(self.us_physical_channel_sellthrough),
            "overseas_revenue_mix": _signed(self.overseas_revenue_mix),
            "repeat_purchase_or_recurring_revenue": _signed(self.repeat_purchase_or_recurring_revenue),
            "tourist_arrival_spending_margin": _signed(self.tourist_arrival_spending_margin),
            "platform_security_trust": _signed(self.platform_security_trust),
            "rival_share_capture": _signed(self.rival_share_capture),
            "retail_restructuring_risk": _signed(self.retail_restructuring_risk),
            "pricing_transparency_regulation": _signed(self.pricing_transparency_regulation),
            "brand_viral_without_margin_penalty": _signed(self.brand_viral_without_margin_penalty),
            "tourism_policy_without_spend_penalty": _signed(self.tourism_policy_without_spend_penalty),
            "ecommerce_user_shift_without_GMV_penalty": _signed(self.ecommerce_user_shift_without_gmv_penalty),
            "JV_without_integration_economics_penalty": _signed(self.jv_without_integration_economics_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round313TriggerRecord:
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
class Round313CaseCandidate:
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
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
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
            "do_not_use_round313_cases_as_candidate_generation_input",
            "do_not_treat_brand_channel_policy_JV_user_shift_or_price_regulation_headline_as_green_without_margin_sellthrough_GMV_or_FCF",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND313_LARGE_SECTOR,
            large_sector=ROUND313_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4B" in field or "4b" in field or "overheat" in field or "inventory" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4C" in field
                or "4c" in field
                or "breach" in field
                or "liquidation" in field
                or "regulation" in field
                or "shrinkflation" in field
            ),
            must_have_fields=ROUND313_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage1_price=self.stage1_price_anchor,
                stage2_price=self.stage2_price_anchor,
                stage3_price=self.stage2_price_anchor if self.stage3_date else None,
                stage4b_price=self.stage4b_price_anchor,
                stage4c_price=self.stage4c_price_anchor,
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if not self.hard_4c_confirmed else 0.86,
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
            "stage1_price_anchor": _value_text(self.stage1_price_anchor),
            "stage2_price_anchor": _value_text(self.stage2_price_anchor),
            "stage4b_price_anchor": _value_text(self.stage4b_price_anchor),
            "stage4c_price_anchor": _value_text(self.stage4c_price_anchor),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND313_CASE_CANDIDATES: tuple[Round313CaseCandidate, ...] = (
    Round313CaseCandidate(
        "r5_loop16_samyang_buldak_export",
        "003230",
        "Samyang Foods / Buldak",
        E2RArchetype.KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW,
        (E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.CONSUMER_REGULATED_PRODUCT_KOREA),
        "structural_success",
        "Stage2_promote_candidate",
        "r5l16_samyang_buldak_T1",
        "Stage2-Actionable_to_Stage3-Yellow_candidate",
        "Stage2-Actionable to Stage3-Yellow candidate",
        date(2023, 1, 1),
        date(2024, 6, 14),
        date(2024, 6, 14),
        date(2024, 6, 14),
        None,
        False,
        ("OP_estimate_2Q_81_2bn_krw", "OP_estimate_yoy_plus_84pct", "Buldak_ASP_increase", "US_Europe_shipment_growth", "production_capacity_expansion", "shares_plus_5_7pct_close_647000_krw", "target_price_plus_26pct_to_830000_krw"),
        ("full_OHLC_MFE_MAE_missing", "repeat_quarter_export_margin_missing", "channel_inventory_missing", "raw_material_cost_pass_through_missing", "single_product_concentration_4B_watch"),
        5.7,
        None,
        None,
        647000,
        None,
        None,
        {"op_estimate_2q_krw_bn": 81.2, "op_estimate_yoy_pct": 84, "event_return_pct": 5.7, "entry_price_anchor_krw": 647000, "target_price_krw": 830000, "target_price_raise_pct": 26},
        "aligned",
        "excellent_stage2_to_yellow_candidate",
        "true_rerating",
        "yellow_success",
        "ASP, shipment, capacity, OP estimate and price reaction close together, but repeat export margin and inventory remain Green gates.",
    ),
    Round313CaseCandidate(
        "r5_loop16_kbeauty_us_channel",
        "483650/257720/192820/161890/090430",
        "d'Alba Global / Silicon2 / Cosmax / Kolmar / Amorepacific read-through",
        E2RArchetype.KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE,
        (E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION, E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL),
        "success_candidate",
        "Stage2_Actionable_channel_expansion",
        "r5l16_kbeauty_us_channel_T1",
        "Stage2-Actionable_with_4B_channel_gate",
        "Stage2-Actionable",
        date(2024, 1, 1),
        date(2025, 6, 5),
        None,
        date(2025, 6, 5),
        None,
        False,
        ("Korea_US_cosmetics_export_rank_1", "top5_Korean_US_ecommerce_growth_71pct_2y", "overall_US_market_growth_21pct", "top5_French_growth_15pct", "dAlba_post_debut_return_over_100pct", "Ulta_Sephora_Costco_Target_channel"),
        ("physical_store_sellthrough_missing", "repeat_orders_missing", "brand_specific_margin_missing", "tariff_pass_through_missing", "China_decline_offset_missing", "inventory_turnover_missing"),
        100.0,
        None,
        None,
        None,
        None,
        None,
        {"korea_us_cosmetics_export_rank_2024": 1, "top5_korean_us_ecommerce_growth_2y_pct": 71, "overall_us_market_growth_2y_pct": 21, "top5_french_brands_growth_2y_pct": 15, "dalba_post_debut_return_pct_context": ">100", "retailers": ["Ulta", "Sephora", "Costco", "Target"]},
        "aligned",
        "Stage2_Actionable_channel_expansion",
        "unknown",
        "stage2_watch_success",
        "K-beauty U.S. channel expansion is real, but physical-store sell-through and listed-company margin are the Green gates.",
    ),
    Round313CaseCandidate(
        "r5_loop16_apr_medicube_beauty_device",
        "278470",
        "APR / Medicube",
        E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B,
        (E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B, E2RArchetype.K_BEAUTY_DEVICE_BRAND_4B),
        "4b_watch",
        "Stage2_structural_with_4B_overheat",
        "r5l16_apr_medicube_T1",
        "Stage2_structural_with_4B_overheat",
        "Stage2 + 4B-watch",
        date(2024, 1, 1),
        date(2025, 10, 20),
        None,
        date(2025, 10, 20),
        None,
        False,
        ("stock_return_since_january_over_4x", "market_value_around_6bn_usd", "device_price_180_usd_context", "q2_2025_overseas_revenue_near_80pct", "device_one_third_US_sales", "Kylie_Jenner_TikTok_trigger"),
        ("celebrity_viral_concentration_4B", "repeat_device_purchase_cycle_missing", "consumables_or_recurring_revenue_missing", "gross_margin_durability_missing", "tariff_absorption_missing", "valuation_multiple_absorption_missing"),
        300.0,
        None,
        None,
        None,
        None,
        None,
        {"stock_return_since_january_context": ">4x", "market_value_usd_bn": 6, "device_price_usd_context": 180, "q2_2025_overseas_revenue_share_pct": "~80", "device_share_of_us_sales_pct": "~33", "celebrity_trigger": "Kylie_Jenner_TikTok"},
        "aligned",
        "Stage2_structural_but_overheat_4B",
        "theme_overheat",
        "stage2_watch_success",
        "Beauty-device overseas revenue is structural evidence, but a fourfold rally and celebrity trigger require a 4B overlay.",
    ),
    Round313CaseCandidate(
        "r5_loop16_china_visa_free_tourism_retail",
        "069960/008770/034230/123690",
        "Hyundai Department Store / Hotel Shilla / Paradise / Hankook Cosmetics",
        E2RArchetype.CHINA_TOURISM_DUTYFREE_STAGE2_EVENT,
        (E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT, E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT),
        "event_premium",
        "Stage2_tourism_event",
        "r5l16_china_tourism_T1",
        "Stage2-Actionable_tourism_event",
        "Stage2 event",
        date(2025, 3, 20),
        date(2025, 8, 6),
        None,
        date(2025, 9, 29),
        None,
        False,
        ("visa_free_Chinese_groups_2025_09_29_to_2026_06", "visa_free_stay_15_days", "Hyundai_Department_plus_7_1pct", "Hotel_Shilla_plus_4_8pct", "Paradise_plus_2_9pct", "Hankook_Cosmetics_plus_9_9pct"),
        ("actual_chinese_arrivals_missing", "per_capita_spending_missing", "duty_free_sales_missing", "hotel_occupancy_missing", "casino_drop_amount_missing", "cosmetics_sellthrough_missing"),
        9.9,
        None,
        None,
        None,
        None,
        None,
        {"policy_announcement_date": "2025-08-06", "pilot_start_date": "2025-09-29", "pilot_end_date": "2026-06", "visa_free_stay_days": 15, "hyundai_department_store_event_return_pct": 7.1, "hotel_shilla_event_return_pct": 4.8, "paradise_event_return_pct": 2.9, "hankook_cosmetics_event_return_pct": 9.9},
        "aligned",
        "Stage2_tourism_event_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Visa-free tourism policy aligns with event returns, but visitor spending and margin must appear before Yellow or Green.",
    ),
    Round313CaseCandidate(
        "r5_loop16_coupang_breach_rival_retail_shift",
        "CPNG/035420/139480/000120",
        "Coupang / Naver / E-Mart / CJ Logistics",
        E2RArchetype.ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2,
        (E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C, E2RArchetype.RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2),
        "4c_thesis_break",
        "hard_4C_plus_rival_Stage2",
        "r5l16_coupang_breach_T0/r5l16_coupang_rival_T2",
        "hard_4C_plus_rival_Stage2",
        "4C + Stage2 rival opportunity",
        date(2025, 12, 1),
        date(2026, 2, 25),
        None,
        None,
        date(2025, 12, 1),
        True,
        ("affected_accounts_33_7mn", "Coupang_premarket_minus_4_4pct", "Coupang_return_since_breach_minus_34pct", "mobile_MAU_minus_3_5pct", "daily_spending_minus_6_3pct", "Naver_online_users_plus_23pct", "CJ_Logistics_volume_plus_120pct"),
        ("platform_security_hard_4C", "regulatory_penalty_final_amount_missing", "Naver_GMV_conversion_missing", "E_Mart_fast_delivery_revenue_missing", "CJ_Logistics_margin_missing", "Coupang_churn_persistence_missing"),
        23.0,
        -34.0,
        None,
        None,
        None,
        None,
        {"affected_accounts_mn": 33.7, "coupang_premarket_event_return_pct": -4.4, "coupang_return_since_breach_pct": -34, "mobile_mau_change_jan_vs_nov_pct": -3.5, "daily_consumer_spending_change_pct": -6.3, "daily_consumer_spending_jan_krw_bn": 139.2, "naver_online_users_change_pct": 23, "cj_logistics_overnight_one_day_volume_q4_yoy_pct": 120},
        "aligned",
        "platform_security_4C_with_rival_stage2",
        "thesis_break",
        "should_have_been_red",
        "Coupang breach is hard 4C; rival user and logistics gains are Stage2 until GMV and margin convert.",
    ),
    Round313CaseCandidate(
        "r5_loop16_shinsegae_emart_alibaba_gmarket_jv",
        "004170/139480",
        "Shinsegae / E-Mart / Alibaba International / Gmarket",
        E2RArchetype.RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B,
        (E2RArchetype.ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B, E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE),
        "success_candidate",
        "Stage2_JV_with_integration_4B",
        "r5l16_emart_alibaba_T0",
        "Stage2_JV_with_integration_4B",
        "Stage2 JV",
        date(2024, 12, 26),
        date(2024, 12, 26),
        None,
        date(2025, 1, 1),
        None,
        False,
        ("Gmarket_100pct_stake_contributed", "AliExpress_Korea_in_JV", "Korea_ecommerce_world_fourth_largest", "Gmarket_struggling_vs_Coupang_Naver_AliExpress_Temu"),
        ("JV_completion_missing", "GMV_growth_missing", "take_rate_missing", "seller_retention_missing", "regulatory_approval_missing", "logistics_integration_missing", "loss_reduction_missing"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2024-12-26", "assets_contributed": ["Gmarket_100pct_stake", "AliExpress_Korea"], "market_context": "Korea_ecommerce_world_fourth_largest", "competitors": ["Coupang", "Naver", "AliExpress", "Temu"]},
        "evidence_good_but_price_failed",
        "Stage2_platform_JV_not_Green",
        "unknown",
        "stage2_watch_success",
        "The Alibaba/Gmarket JV is Stage2 platform restructuring, but integration economics and seller retention block Green.",
    ),
    Round313CaseCandidate(
        "r5_loop16_homeplus_offline_grocery_restructuring",
        "private/139480_readthrough/004170_readthrough",
        "Homeplus / offline grocery reference",
        E2RArchetype.OFFLINE_GROCERY_RESTRUCTURING_HARD_4C,
        (E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C, E2RArchetype.GROCERY_RETAIL_CREDIT_4C_REFERENCE),
        "4c_thesis_break",
        "hard_4C_offline_retail_restructuring",
        "r5l16_homeplus_T1",
        "hard_4C_offline_retail_restructuring",
        "4C",
        date(2025, 3, 1),
        None,
        None,
        None,
        date(2025, 6, 13),
        True,
        ("court_led_restructuring", "liquidation_value_3_7tn_krw", "total_assets_6_8tn_krw", "liquidation_value_above_going_concern", "MBK_share_writeoff_2_5tn_krw"),
        ("COVID_fallout", "ecommerce_competition", "liquidity_stress", "creditor_repayment_need", "private_company_no_stock_price"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"liquidation_value_krw_trn": 3.7, "total_assets_krw_trn": 6.8, "mbk_share_writeoff_krw_trn": 2.5, "court_sale_approval": True},
        "aligned",
        "offline_grocery_hard_4C_reference",
        "thesis_break",
        "should_have_been_red",
        "Liquidation value above going-concern value turns an offline grocery asset story into a hard 4C reference.",
    ),
    Round313CaseCandidate(
        "r5_loop16_shrinkflation_price_regulation",
        "097950/004370/003230/processed_food_basket",
        "CJ CheilJedang / Nongshim / Samyang / processed food basket",
        E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH,
        (E2RArchetype.CONSUMER_REGULATED_PRODUCT_KOREA, E2RArchetype.CONSUMER_REGULATED_PRODUCT),
        "4b_watch",
        "4C_watch_price_regulation",
        "r5l16_shrinkflation_T0",
        "4C_watch_price_regulation",
        "4C-watch",
        date(2024, 5, 3),
        None,
        None,
        date(2024, 8, 1),
        None,
        False,
        ("KFTC_shrinkflation_unfair_transaction", "rule_effective_2024_08", "first_offence_fine_5mn_krw", "second_offence_fine_10mn_krw", "notice_period_3_months", "CJ_sausage_weight_cut_12_5pct"),
        ("transparent_price_hike_acceptance_missing", "brand_pricing_power_missing", "raw_material_cost_normalization_missing", "volume_elasticity_missing", "retailer_negotiation_missing"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2024-05-03", "rule_effective": "2024-08", "first_offence_fine_krw_mn": 5, "second_offence_fine_krw_mn": 10, "notice_period_months": 3, "cj_sausage_weight_cut_pct": 12.5},
        "aligned",
        "consumer_price_regulation_4C_watch",
        "unknown",
        "stage2_watch_success",
        "Shrinkflation crackdown limits hidden ASP pass-through and requires transparent pricing plus volume resilience.",
    ),
)


ROUND313_TRIGGER_RECORDS: tuple[Round313TriggerRecord, ...] = (
    Round313TriggerRecord("r5l16_samyang_buldak_T1", "r5_loop16_samyang_buldak_export", "Stage2-Actionable_to_Stage3-Yellow_candidate", "2024-06-14", "Kiwoom raises Samyang 2Q OP estimate to 81.2B won, +84% YoY, citing Buldak ASP, U.S./Europe shipments and capacity; shares +5.7% to 647,000 won", 5.7, "excellent_stage2_to_yellow_candidate", "Stage3-Yellow_candidate", {"entry_price_krw": 647000, "target_price_krw": 830000}),
    Round313TriggerRecord("r5l16_kbeauty_us_channel_T1", "r5_loop16_kbeauty_us_channel", "Stage2-Actionable", "2025-06-05", "Korea became top cosmetics exporter to U.S.; top-five Korean U.S. e-commerce beauty brands +71% over two years; d'Alba shares more than doubled since debut", "d'Alba >100% post-debut context", "Stage2_Actionable_channel_expansion", "Stage2-Actionable", {"top5_korean_us_ecommerce_growth_2y_pct": 71}),
    Round313TriggerRecord("r5l16_apr_medicube_T1", "r5_loop16_apr_medicube_beauty_device", "Stage2_structural_with_4B", "2025-10-20", "APR stock more than four-fold since January, market value around $6B, Q2 overseas revenue nearly 80%, beauty device about one-third of U.S. sales", ">4x since January", "Stage2_structural_but_overheat_4B", "Stage2+4B", {"market_value_usd_bn": 6}),
    Round313TriggerRecord("r5l16_china_tourism_T1", "r5_loop16_china_visa_free_tourism_retail", "Stage2_tourism_event", "2025-08-06", "South Korea announces Chinese tourist group visa-free entry; Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%", "Hyundai +7.1 / Shilla +4.8 / Hankook +9.9", "Stage2_tourism_event_not_Green", "Stage2-Actionable_event", {"visa_free_stay_days": 15}),
    Round313TriggerRecord("r5l16_coupang_breach_T0", "r5_loop16_coupang_breach_rival_retail_shift", "hard_4C", "2025-12-01", "Coupang data breach affects 33.7M accounts; stock -4.4% premarket; later shares down around 34% since breach", -4.4, "platform_security_hard_4C", "4C", {"affected_accounts_mn": 33.7}),
    Round313TriggerRecord("r5l16_coupang_rival_T2", "r5_loop16_coupang_breach_rival_retail_shift", "rival_Stage2_opportunity", "2026-02-25", "Coupang MAU -3.5%, spending -6.3%; Naver online users +23%; CJ Logistics overnight/one-day delivery volume +120% in Q4", "price_data_unavailable_after_deep_search", "rival_share_capture_stage2", "Stage2", {"naver_online_users_change_pct": 23, "cj_logistics_volume_yoy_pct": 120}),
    Round313TriggerRecord("r5l16_emart_alibaba_T0", "r5_loop16_shinsegae_emart_alibaba_gmarket_jv", "Stage2_JV", "2024-12-26", "Shinsegae/E-Mart to set JV with Alibaba International, contributing 100% Gmarket stake; AliExpress Korea and Gmarket included", "price_data_unavailable_after_deep_search", "Stage2_platform_JV_not_Green", "Stage2", {"assets": ["Gmarket_100pct", "AliExpress_Korea"]}),
    Round313TriggerRecord("r5l16_homeplus_T1", "r5_loop16_homeplus_offline_grocery_restructuring", "hard_4C", "2025-06-13/2025-06-20", "Homeplus liquidation value exceeds going-concern value; liquidation value 3.7T won, total assets 6.8T won, MBK to write off 2.5T won shares", "private_company_no_stock_price", "offline_grocery_hard_4C_reference", "4C", {"liquidation_value_krw_trn": 3.7}),
    Round313TriggerRecord("r5l16_shrinkflation_T0", "r5_loop16_shrinkflation_price_regulation", "4C-watch", "2024-05-03", "KFTC designates undisclosed shrinkflation as unfair transaction; rule from Aug 2024, fines 5M/10M won; CJ sausage weight cut 12.5% example", "price_data_unavailable_after_deep_search", "consumer_price_regulation_4C_watch", "4C-watch", {"cj_sausage_weight_cut_pct": 12.5}),
)


ROUND313_SHADOW_WEIGHT_ROWS: tuple[Round313ShadowWeightRow, ...] = (
    Round313ShadowWeightRow(E2RArchetype.KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW, 5, 1, 4, 4, 0, 1, 0, 0, 2, -3, -1, -1, -1, "ASP+shipment+capacity+OP estimate", "repeat margin pending", "quarterly OP+margin+OHLC", "Samyang Buldak template."),
    Round313ShadowWeightRow(E2RArchetype.KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE, 2, 5, 5, 4, 1, 1, 0, 0, 1, -5, -1, -1, -1, "U.S. e-commerce+retailer channel", "physical sell-through/margin pending", "retail sell-through+margin", "K-beauty/d'Alba/Cosmax."),
    Round313ShadowWeightRow(E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B, 1, 3, 5, 5, 0, 1, 0, 0, 0, -5, -1, -1, -1, "overseas device growth", "recurring revenue/valuation pending", "repeat device+consumables margin", "APR/Medicube."),
    Round313ShadowWeightRow(E2RArchetype.CHINA_TOURISM_DUTYFREE_STAGE2_EVENT, 0, 2, 1, 1, 5, 1, 0, 0, 0, -1, -5, -1, -1, "visa-free tourism policy", "actual spend/margin pending", "visitor spend+duty-free margin", "Hotel Shilla/Hyundai Dept/Hankook Cosmetics."),
    Round313ShadowWeightRow(E2RArchetype.ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2, 0, 0, 0, 1, 0, 5, 4, 2, 1, -1, -1, -4, -1, "data breach/rival shift", "GMV/margin conversion pending", "security restored or rival GMV captured", "Coupang/Naver/E-Mart/CJ."),
    Round313ShadowWeightRow(E2RArchetype.RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B, 0, 1, 1, 2, 0, 2, 3, 3, 1, -1, -1, -2, -5, "Alibaba/Gmarket JV", "integration/take-rate missing", "GMV+take-rate+seller retention", "Shinsegae/E-Mart."),
    Round313ShadowWeightRow(E2RArchetype.OFFLINE_GROCERY_RESTRUCTURING_HARD_4C, 0, 0, 0, 0, 0, 1, 0, 5, 1, -1, -1, -1, -1, "court-led restructuring", "strategic buyer missing", "N/A", "Homeplus reference."),
    Round313ShadowWeightRow(E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH, 3, 0, 0, 1, 0, 1, 0, 1, 5, -2, -1, -1, -1, "hidden ASP pass-through constrained", "transparent pricing pending", "pricing power+volume resilience", "Processed food basket."),
)


def round313_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND313_CASE_CANDIDATES]


def round313_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND313_CASE_CANDIDATES]


def round313_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND313_TRIGGER_RECORDS]


def round313_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND313_SHADOW_WEIGHT_ROWS]


def round313_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND313_REQUIRED_TARGET_ALIASES.items()]


def round313_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND313_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND313_SCORE_DOWN_AXES]
    )


def round313_summary() -> dict[str, object]:
    return {
        "source_round": ROUND313_SOURCE_ROUND_PATH,
        "round_id": ROUND313_ANALYST_ROUND_ID,
        "large_sector": ROUND313_LARGE_SECTOR,
        "method": ROUND313_METHOD,
        "case_candidate_count": len(ROUND313_CASE_CANDIDATES),
        "trigger_count": len(ROUND313_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND313_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 4,
        "stage2_event_candidate_count": 3,
        "stage3_yellow_candidate_count": 1,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 3,
        "hard_4c_case_count": 2,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round313_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND313_SOURCE_ROUND_PATH,
        "round_id": ROUND313_ANALYST_ROUND_ID,
        "large_sector": ROUND313_LARGE_SECTOR,
        "method": ROUND313_METHOD,
        "summary": round313_summary(),
        "required_target_aliases": dict(ROUND313_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND313_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND313_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND313_STAGE3_GREEN_RULES,
        "green_blockers": ROUND313_GREEN_BLOCKERS,
        "score_up_axes": ROUND313_SCORE_UP_AXES,
        "score_down_axes": ROUND313_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND313_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND313_4C_WATCH_GATES,
        "row_separation_rules": ROUND313_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round313_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_brand_channel_policy_JV_user_shift_or_price_regulation_headline_as_green_without_margin_sellthrough_GMV_or_FCF",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round313_summary_markdown() -> str:
    summary = round313_summary()
    lines = [
        "# R5 Loop 16 Consumer / Retail / Brands Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: K-beauty U.S. channel expansion is Stage2 when e-commerce and retailer entry are visible. It is not Green until sell-through, repeat orders and margin are visible.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Brand, channel, tourism, JV and user-shift narratives must be separated from company margin, sell-through, GMV and FCF.",
            "- Stage3-Yellow candidates: `Samyang Buldak`.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C references: Coupang breach and Homeplus restructuring.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round313_trigger_grid_markdown() -> str:
    lines = [
        "# Round 313 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round313_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round313_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 313 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND313_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND313_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND313_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND313_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND313_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round313_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 313 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND313_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND313_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND313_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round313_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 313 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND313_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round313_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 313 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: a Coupang breach can create a rival Stage2 opportunity. It is still not rival Green until GMV and logistics margin convert.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND313_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round313_r5_loop16_reports(
    output_directory: str | Path = ROUND313_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND313_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND313_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND313_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND313_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round313_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND313_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round313_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round313_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round313_r5_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round313_r5_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round313_r5_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round313_r5_loop16_trigger_grid.md",
        "summary": output_dir / "round313_r5_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round313_r5_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round313_r5_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round313_r5_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round313_r5_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round313_r5_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round313_r5_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round313_case_rows())
    _write_csv(paths["target_aliases"], round313_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round313_trigger_rows())
    _write_csv(paths["score_adjustments"], round313_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round313_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round313_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round313_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round313_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round313_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round313_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round313_row_separation_plan_markdown(), encoding="utf-8")
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


def _signed(value: int) -> str:
    return f"{value:+d}" if value else "+0"


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    return [f"- {item}" for item in items]


__all__ = [
    "ROUND313_4C_WATCH_GATES",
    "ROUND313_CASE_CANDIDATES",
    "ROUND313_GREEN_BLOCKERS",
    "ROUND313_LARGE_SECTOR",
    "ROUND313_REQUIRED_TARGET_ALIASES",
    "ROUND313_ROW_SEPARATION_RULES",
    "ROUND313_SCORE_DOWN_AXES",
    "ROUND313_SCORE_UP_AXES",
    "ROUND313_SHADOW_WEIGHT_ROWS",
    "ROUND313_STAGE2_ACTIONABLE_RULES",
    "ROUND313_STAGE3_GREEN_RULES",
    "ROUND313_STAGE3_YELLOW_RULES",
    "ROUND313_STAGE4B_WATCH_TRIGGERS",
    "ROUND313_TRIGGER_RECORDS",
    "render_round313_stage4b_4c_review_markdown",
    "render_round313_stage_rules_markdown",
    "render_round313_trigger_grid_markdown",
    "round313_audit_payload",
    "round313_case_records",
    "round313_case_rows",
    "round313_shadow_weight_rows",
    "round313_summary",
    "round313_trigger_rows",
    "write_round313_r5_loop16_reports",
]
