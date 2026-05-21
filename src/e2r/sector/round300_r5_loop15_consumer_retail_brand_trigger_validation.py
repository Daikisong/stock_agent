"""Round-300 R5 Loop-15 consumer/retail/brand trigger validation pack.

This module converts ``docs/round/round_300.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: a celebrity fried-chicken event can move listed peers, but it is
not Stage3 evidence until same-store sales, franchise fees, or repeat demand
are visible.
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


ROUND300_SOURCE_ROUND_PATH = "docs/round/round_300.md"
ROUND300_ANALYST_ROUND_ID = "round_228"
ROUND300_LARGE_SECTOR = "CONSUMER_RETAIL_BRAND"
ROUND300_METHOD = "trigger_level_backtest_v1"
ROUND300_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round300_r5_loop15_consumer_retail_brand_trigger_validation"
ROUND300_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop15_round228.jsonl"
ROUND300_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r5_loop15_round228.jsonl"
ROUND300_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round300_r5_loop15_consumer_retail_brand_trigger_validation_audit.json"
ROUND300_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round228_r5_loop15_v1.csv"

ROUND300_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW": E2RArchetype.K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW.value,
    "K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH": E2RArchetype.K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH.value,
    "K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE": E2RArchetype.K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE.value,
    "BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B": E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B.value,
    "CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE": E2RArchetype.CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE.value,
    "ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B": E2RArchetype.ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B.value,
    "BRAND_MA_CONTROL_RIGHTS_STAGE2": E2RArchetype.BRAND_MA_CONTROL_RIGHTS_STAGE2.value,
    "FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE": E2RArchetype.FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE.value,
    "RAMEN_GLOBAL_EXPANSION_STAGE2": E2RArchetype.RAMEN_GLOBAL_EXPANSION_STAGE2.value,
    "TOURISM_REROUTE_EVENT_PREMIUM": E2RArchetype.TOURISM_REROUTE_EVENT_PREMIUM.value,
}

ROUND300_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "asp_increase_or_price_pass_through_visible",
    "shipment_export_or_ecommerce_sellthrough_visible_by_region",
    "op_estimate_or_target_revision_has_operating_reason",
    "capacity_or_distribution_channel_expansion_visible",
    "event_or_market_relative_price_reaction_is_strong",
    "viral_or_sns_signal_converts_to_revenue_mix_or_sales",
    "tourism_policy_can_bridge_to_arrivals_spending_or_store_sales",
)

ROUND300_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "two_or_three_operating_numbers_change_eps_op_path",
    "repeat_purchase_offline_channel_regulatory_or_margin_gate_still_pending",
    "valuation_4b_overlay_applied_if_price_already_reran",
)

ROUND300_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "export_or_sales_are_confirmed_in_actual_quarter",
    "asp_and_volume_hold_together",
    "capacity_expansion_converts_to_revenue_and_margin",
    "offline_sellthrough_and_repeat_purchase_confirm",
    "tourism_spending_adr_dutyfree_or_store_sales_confirm",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND300_GREEN_BLOCKERS: tuple[str, ...] = (
    "viral_celebrity_event_only",
    "brand_name_only",
    "tourism_policy_without_spending",
    "jv_without_data_rights",
    "ma_option_without_funding_control",
    "target_market_size_only",
    "social_media_hype_without_repeat_purchase",
)

ROUND300_SCORE_UP_AXES: tuple[str, ...] = (
    "export_shipment_growth",
    "asp_increase",
    "op_estimate_revision",
    "production_capacity_expansion",
    "us_europe_sellthrough",
    "physical_retail_channel_entry",
    "repeat_purchase_or_same_store_sales",
    "tourist_arrival_spending_conversion",
    "customer_data_monetization_permission",
    "brand_ma_control_execution",
)

ROUND300_SCORE_DOWN_AXES: tuple[str, ...] = (
    "viral_celebrity_event_only",
    "brand_name_only",
    "tourism_policy_without_spending",
    "jv_without_data_rights",
    "ma_option_without_funding_control",
    "target_market_size_only",
    "social_media_hype_without_repeat_purchase",
)

ROUND300_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "sns_or_influencer_trigger_rallies_without_direct_sales",
    "stock_rises_three_to_four_times_before_channel_margin_confirm",
    "tourism_policy_rally_without_spending_data",
    "jv_or_ma_headline_without_data_rights_funding_control_or_roic",
    "regulatory_recall_or_social_backlash_watch",
)

ROUND300_HARD_4C_GATES: tuple[str, ...] = (
    "food_safety_or_recall_quality_problem_confirmed",
    "major_market_ban_persists",
    "meme_rally_collapses_without_direct_revenue",
    "tourism_policy_reversal_or_diplomatic_conflict_blocks_flow",
    "ecommerce_jv_data_regulation_blocks_monetization",
    "brand_ma_funding_or_control_failure",
)


@dataclass(frozen=True)
class Round300ShadowWeightRow:
    archetype: E2RArchetype
    export_shipment_growth: int
    asp_increase: int
    op_estimate_revision: int
    production_capacity_expansion: int
    us_europe_sellthrough: int
    physical_retail_channel_entry: int
    repeat_purchase_same_store_sales: int
    tourist_arrival_spending_conversion: int
    customer_data_monetization_permission: int
    brand_ma_control_execution: int
    viral_celebrity_event_only_penalty: int
    brand_name_only_penalty: int
    tourism_policy_without_spending_penalty: int
    jv_without_data_rights_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "export_shipment_growth": _signed(self.export_shipment_growth),
            "asp_increase": _signed(self.asp_increase),
            "op_estimate_revision": _signed(self.op_estimate_revision),
            "production_capacity_expansion": _signed(self.production_capacity_expansion),
            "us_europe_sellthrough": _signed(self.us_europe_sellthrough),
            "physical_retail_channel_entry": _signed(self.physical_retail_channel_entry),
            "repeat_purchase_same_store_sales": _signed(self.repeat_purchase_same_store_sales),
            "tourist_arrival_spending_conversion": _signed(self.tourist_arrival_spending_conversion),
            "customer_data_monetization_permission": _signed(self.customer_data_monetization_permission),
            "brand_ma_control_execution": _signed(self.brand_ma_control_execution),
            "viral_celebrity_event_only_penalty": _signed(self.viral_celebrity_event_only_penalty),
            "brand_name_only_penalty": _signed(self.brand_name_only_penalty),
            "tourism_policy_without_spending_penalty": _signed(self.tourism_policy_without_spending_penalty),
            "jv_without_data_rights_penalty": _signed(self.jv_without_data_rights_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round300TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: date
    evidence_available: str
    entry_price_krw: float | None
    event_return_pct: float | str | None
    target_price_krw: float | None
    trigger_outcome_label: str
    promote_to: str
    extra_metrics: Mapping[str, object]

    def as_dict(self) -> dict[str, object]:
        return {
            "trigger_id": self.trigger_id,
            "case_id": self.case_id,
            "trigger_type": self.trigger_type,
            "trigger_date": self.trigger_date.isoformat(),
            "evidence_available": self.evidence_available,
            "entry_price_krw": self.entry_price_krw,
            "event_return_pct": self.event_return_pct,
            "target_price_krw": self.target_price_krw,
            "trigger_outcome_label": self.trigger_outcome_label,
            "promote_to": self.promote_to,
            "extra_metrics": dict(self.extra_metrics),
        }

    def as_row(self) -> dict[str, str]:
        row = {key: _value_text(value) for key, value in self.as_dict().items() if key != "extra_metrics"}
        row["extra_metrics"] = json.dumps(self.extra_metrics, ensure_ascii=False, sort_keys=True)
        return row


@dataclass(frozen=True)
class Round300CaseCandidate:
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
    entry_price_anchor: float | None
    target_price_anchor: float | None
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
            "do_not_use_round300_cases_as_candidate_generation_input",
            "do_not_treat_celebrity_policy_jv_or_ma_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND300_LARGE_SECTOR,
            large_sector=ROUND300_LARGE_SECTOR,
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
            stage1_evidence=self.evidence_fields if self.stage1_date else (),
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=self.evidence_fields if self.stage3_date else (),
            stage4b_evidence=self.red_flag_fields if self.stage4b_date else (),
            stage4c_evidence=self.red_flag_fields if self.stage4c_date else (),
            must_have_fields=ROUND300_STAGE2_ACTIONABLE_RULES + ROUND300_STAGE3_YELLOW_RULES + ROUND300_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.red_flag_fields else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern=self.round_alignment_label,
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage1_price=self.entry_price_anchor if self.stage1_date and not self.stage2_date else None,
                stage2_price=self.entry_price_anchor if self.stage2_date else None,
                stage3_price=self.entry_price_anchor if self.stage3_date else None,
                stage4b_price=self.entry_price_anchor if self.stage4b_date and not self.stage3_date else None,
                mfe_30d=self.event_mfe_pct if self.event_mfe_pct and self.event_mfe_pct > 0 else None,
                mae_30d=self.event_mae_pct if self.event_mae_pct and self.event_mae_pct < 0 else None,
                price_validation_status="reported_event_anchor_not_full_ohlc",
            ),
            data_quality=CaseDataQuality(False, True, False, 0.7),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": ";".join(item.value for item in self.secondary_archetypes),
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
            "evidence_fields": ";".join(self.evidence_fields),
            "red_flag_fields": ";".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "entry_price_anchor": _value_text(self.entry_price_anchor),
            "target_price_anchor": _value_text(self.target_price_anchor),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "price_validation_status": "reported_event_anchor_not_full_ohlc",
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "notes": self.notes,
        }


ROUND300_SHADOW_WEIGHT_ROWS: tuple[Round300ShadowWeightRow, ...] = (
    Round300ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW, 5, 5, 5, 4, 5, 1, 4, 0, 0, 0, -4, -3, -1, -1, "ASP+shipment+capacity+OP revision", "actual result/repeat demand pending", "export margin+capacity+repeat demand", "Samyang Buldak trigger should promote to Yellow."),
    Round300ShadowWeightRow(E2RArchetype.K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH, 2, 2, 2, 1, 2, 0, 2, 0, 0, 0, -2, -2, -1, -1, "recall/watch", "quality defect or market ban pending", "ban reversal or no sales impact", "Denmark Buldak recall was watch not hard 4C."),
    Round300ShadowWeightRow(E2RArchetype.RAMEN_GLOBAL_EXPANSION_STAGE2, 4, 2, 2, 3, 5, 2, 4, 0, 0, 0, -3, -2, -1, -1, "global sales+U.S. target", "OP/price trigger missing", "ASP/OP/export margin confirmed", "Nongshim remains Stage2 without price/OP trigger."),
    Round300ShadowWeightRow(E2RArchetype.K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE, 4, 3, 3, 2, 5, 5, 5, 2, 0, 0, -4, -3, -1, -1, "U.S. ecommerce sell-through+physical retail talks", "store sell-through/tariff pending", "repeat purchase+margin+offline channel", "K-beauty basket Stage2-Actionable."),
    Round300ShadowWeightRow(E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B, 4, 3, 4, 2, 5, 4, 5, 1, 0, 0, -2, -2, -1, -1, "viral device demand+overseas revenue", "valuation/tariff/channel pending", "sustained repeat purchase+margin", "APR Yellow with 4B overlay."),
    Round300ShadowWeightRow(E2RArchetype.CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE, 0, 0, 1, 0, 2, 2, 3, 5, 0, 0, -2, -2, -5, -1, "visa policy+multi-stock rally", "arrival/spending conversion pending", "duty-free sales+hotel ADR+beauty sellthrough", "Chinese tourism basket Stage2-Actionable."),
    Round300ShadowWeightRow(E2RArchetype.TOURISM_REROUTE_EVENT_PREMIUM, 0, 0, 0, 0, 1, 1, 2, 3, 0, 0, -2, -2, -4, -1, "reroute event premium", "arrival/spending conversion pending", "booking+spending+margin", "Tourism reroute is event premium until spending converts."),
    Round300ShadowWeightRow(E2RArchetype.ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B, 0, 0, 1, 0, 0, 0, 2, 0, 5, 3, -2, -2, -1, -5, "JV+conditional approval", "GMV/take-rate/data rights pending", "customer data monetization+margin", "E-Mart/Alibaba JV Stage2 with data gate."),
    Round300ShadowWeightRow(E2RArchetype.BRAND_MA_CONTROL_RIGHTS_STAGE2, 0, 0, 1, 0, 1, 1, 3, 0, 0, 5, -2, -4, -1, -2, "brand M&A optionality", "funding/control/ROIC pending", "control execution+ROIC", "F&F TaylorMade Stage2."),
    Round300ShadowWeightRow(E2RArchetype.FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, -5, -1, -1, "no direct revenue", "same-store/franchise fee missing", "N/A", "Kyochon/Jensen meme is price moved without evidence."),
)


ROUND300_TRIGGER_RECORDS: tuple[Round300TriggerRecord, ...] = (
    Round300TriggerRecord("r5l15_samyang_T1", "r5_loop15_samyang_buldak_export", "Stage2-Actionable", date(2024, 6, 14), "Kiwoom raises 2Q OP estimate to 81.2B won, +84% YoY, driven by ASP increase, U.S./Europe shipments and capacity expansion", 647000, 5.7, 830000, "excellent_stage2_promote_candidate", "Stage3-Yellow", {"q2_2024_op_estimate_krw_bn": 81.2, "q2_2024_op_estimate_yoy_pct": 84, "target_price_raise_pct": 26, "target_upside_from_entry_pct": 28.3}),
    Round300TriggerRecord("r5l15_samyang_T3", "r5_loop15_samyang_buldak_export", "4C-watch", date(2024, 6, 12), "Denmark recalls three Buldak variants due capsaicin/spiciness risk", None, "price_data_unavailable_after_deep_search", None, "regulatory_false_break_watch", "4C-watch_false_break", {"denmark_recall_variants": 3, "ban_partially_reversed_date": "2024-08-08"}),
    Round300TriggerRecord("r5l15_nongshim_T1", "r5_loop15_nongshim_shinramyun_global", "Stage2", date(2024, 5, 27), "Shin Ramyun 2023 sales 1.2T won / $883M, nearly 60% abroad, U.S. sales target $1.5B by 2030", None, "price_data_unavailable_after_deep_search", None, "success_candidate_stage2", "Stage2", {"shin_ramyun_2023_sales_krw_trn": 1.2, "shin_ramyun_2023_sales_usd_mn": 883, "overseas_sales_share_pct": 60, "us_sales_target_2030_usd_bn": 1.5}),
    Round300TriggerRecord("r5l15_kbeauty_T2", "r5_loop15_kbeauty_us_export_basket", "Stage2-Actionable", date(2025, 6, 5), "Korea top U.S. cosmetics exporter, top-five Korean U.S. ecommerce brands +71% over two years vs U.S. market +21%, physical retail talks", None, "price_data_unavailable_after_deep_search", None, "Stage2_promote_candidate", "Stage2-Actionable", {"top5_korean_us_ecommerce_sales_growth_2y_pct": 71, "overall_us_market_growth_2y_pct": 21, "top5_french_brands_growth_2y_pct": 15}),
    Round300TriggerRecord("r5l15_apr_T2", "r5_loop15_apr_medicube_beauty_device", "Stage3-Yellow+4B-watch", date(2025, 10, 20), "APR stock more than fourfold since January, valuation $6B, overseas revenue nearly 80% of Q2, beauty device about one-third of U.S. sales", None, 300, None, "Stage3_Yellow_with_4B_overlay", "Stage3-Yellow+4B", {"valuation_usd_bn": 6, "overseas_revenue_share_q2_2025_pct": 80, "beauty_device_share_of_us_sales_pct": 33}),
    Round300TriggerRecord("r5l15_china_tourism_T1", "r5_loop15_china_tourist_visa_free_retail_basket", "Stage2-Actionable", date(2025, 8, 6), "Chinese group visa-free policy confirmed; Hyundai Department +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%", None, "7.1/4.8/2.9/9.9", None, "Stage2_promote_candidate", "Stage2-Actionable", {"hyundai_department_store_event_return_pct": 7.1, "hotel_shilla_event_return_pct": 4.8, "paradise_event_return_pct": 2.9, "hankook_cosmetics_event_return_pct": 9.9}),
    Round300TriggerRecord("r5l15_emart_jv_T2", "r5_loop15_emart_shinsegae_alibaba_gmarket_jv", "Stage2_with_regulatory_overlay", date(2025, 9, 18), "KFTC conditionally approves Gmarket/AliExpress JV; 50M customer database; 3-year data-sharing restriction; cross-border share 41%", None, "price_data_unavailable_after_deep_search", None, "success_candidate_stage2_with_data_gate", "Stage2", {"jv_estimated_value_usd_bn": 4, "gmarket_customer_database_mn": 50, "data_sharing_restriction_years": 3, "cross_border_ecommerce_market_share_pct": 41}),
    Round300TriggerRecord("r5l15_fnf_T1", "r5_loop15_fnf_taylormade_brand_ma", "Stage2_brand_MA", date(2025, 7, 21), "F&F hires Goldman for TaylorMade acquisition; potential $3.5B sale; F&F has 358B won prior investment and claims consent rights/ROFR", None, "price_data_unavailable_after_deep_search", None, "success_candidate_stage2", "Stage2", {"fnf_2021_investment_krw_bn": 358, "taylormade_possible_sale_value_usd_bn": 3.5}),
    Round300TriggerRecord("r5l15_kyochon_T1", "r5_loop15_kyochon_cherrybro_jensen_meme", "price_moved_without_evidence", date(2025, 10, 31), "Jensen Huang dined at non-listed Kkanbu Chicken; Kyochon/Cherrybro/Neuromeka surged without direct revenue link", None, "Kyochon up to 20 / Cherrybro up to 30", None, "price_moved_without_evidence", "N/A", {"kyochon_event_mfe_pct": 20, "cherrybro_event_mfe_pct": 30, "kkanbu_listed": False, "direct_revenue_link_confirmed": False}),
)


ROUND300_CASE_CANDIDATES: tuple[Round300CaseCandidate, ...] = (
    Round300CaseCandidate("r5_loop15_samyang_buldak_export", "003230", "Samyang Foods", E2RArchetype.K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW, (E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE, E2RArchetype.K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable_to_Stage3-Yellow", "Stage3-Yellow", date(2023, 1, 1), date(2024, 6, 14), date(2024, 6, 14), date(2024, 6, 12), None, False, ("Buldak_ASP_increase", "US_Europe_shipment_growth", "production_capacity_expansion", "q2_op_estimate_plus_84pct", "target_price_830000"), ("denmark_spiciness_recall_watch", "actual_quarterly_result_pending", "repeat_demand_pending"), 5.7, None, 647000, 830000, {"q2_2024_op_estimate_krw_bn": 81.2, "q2_2024_op_estimate_yoy_pct": 84, "target_price_raise_pct": 26, "target_upside_from_entry_pct": 28.3, "denmark_recall_variants": 3, "ban_partially_reversed_date": "2024-08-08", "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "missed_structural_if_old_stage2_gate_used", "true_rerating", "yellow_success", "ASP, shipment, capacity and OP estimate revision should promote Samyang from Stage2 to Stage3-Yellow."),
    Round300CaseCandidate("r5_loop15_nongshim_shinramyun_global", "004370", "Nongshim", E2RArchetype.RAMEN_GLOBAL_EXPANSION_STAGE2, (E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND, E2RArchetype.K_FOOD_EXPORT_RECURRING), "success_candidate", "success_candidate_stage2", "T1/T2", "Stage2_success_candidate", "Stage2", date(2023, 1, 1), date(2024, 5, 27), None, None, None, False, ("shin_ramyun_2023_sales_1_2T_KRW", "overseas_sales_share_60pct", "US_sales_target_2030_1_5B_USD"), ("op_estimate_revision_missing", "asp_increase_missing", "event_price_anchor_missing", "china_slowdown_execution_watch"), None, None, None, None, {"korean_ramen_exports_2023_usd_bn": 1.0, "shin_ramyun_2023_sales_krw_trn": 1.2, "shin_ramyun_2023_sales_usd_mn": 883, "overseas_sales_share_pct": 60, "us_sales_target_2030_usd_bn": 1.5, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "aligned", "success_candidate_stage2_not_yellow", "unknown", "stage2_watch_success", "Nongshim has strong global ramen evidence but lacks OP-estimate and event-price anchors for Yellow."),
    Round300CaseCandidate("r5_loop15_kbeauty_us_export_basket", "257720/192820/161890/090430/beauty_basket", "Silicon2 / Cosmax / Kolmar Korea / Amorepacific / K-beauty basket", E2RArchetype.K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE, (E2RArchetype.K_BEAUTY_US_EXPANSION_STAGE2, E2RArchetype.K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA), "success_candidate", "Stage2_promote_candidate", "T2/T3", "Stage2-Actionable_to_Stage3-Yellow_candidate", "Stage2-Actionable_to_Stage3-Yellow_candidate", date(2024, 1, 1), date(2025, 6, 5), None, date(2025, 6, 5), None, False, ("Korea_top_US_cosmetics_exporter", "top5_Korean_US_ecommerce_growth_71pct", "physical_retail_talks", "ODM_beneficiaries_Cosmax_Kolmar"), ("physical_store_sellthrough_missing", "tariff_pass_through_missing", "inventory_margin_pending"), None, None, None, None, {"korea_replaced_france_as_top_us_cosmetics_exporter": True, "top5_korean_us_ecommerce_sales_growth_2y_pct": 71, "overall_us_market_growth_2y_pct": 21, "top5_french_brands_growth_2y_pct": 15, "retail_channels_under_discussion": ["Ulta Beauty", "Sephora", "Target", "Costco"], "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "Stage2_promote_candidate", "unknown", "stage2_watch_success", "K-beauty export rank, ecommerce sell-through and physical-channel trigger are stronger than plain Stage2."),
    Round300CaseCandidate("r5_loop15_apr_medicube_beauty_device", "APR/beauty_device_basket", "APR / Medicube", E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B, (E2RArchetype.K_BEAUTY_DEVICE_BRAND_4B, E2RArchetype.BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER), "success_candidate", "Stage3_Yellow_with_4B_overlay", "T1/T2", "Stage3-Yellow_with_4B_overlay", "Stage3-Yellow + 4B-watch", date(2024, 1, 1), date(2025, 10, 20), date(2025, 10, 20), date(2025, 10, 20), None, False, ("stock_fourfold_since_january", "valuation_6B_USD", "overseas_revenue_share_80pct", "beauty_device_one_third_US_sales"), ("valuation_4B_overlay", "repeat_purchase_pending", "tariff_competition_watch"), 300, None, None, None, {"stock_return_since_january_pct": 300, "valuation_usd_bn": 6, "overseas_revenue_share_q2_2025_pct": 80, "beauty_device_share_of_us_sales_pct": 33, "product_price_usd": 180, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "aligned", "Stage3-Yellow_candidate_with_4B", "unknown", "yellow_success", "APR links viral device demand to overseas revenue, but a fourfold rally requires 4B valuation overlay."),
    Round300CaseCandidate("r5_loop15_china_tourist_visa_free_retail_basket", "008770/069960/123690/034230/032350", "Hotel Shilla / Hyundai Department Store / Hankook Cosmetics / Paradise / Lotte Tour Development", E2RArchetype.CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE, (E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT, E2RArchetype.TOURISM_REROUTE_EVENT_PREMIUM), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable", "Stage2-Actionable", date(2025, 3, 20), date(2025, 8, 6), None, date(2025, 10, 2), None, False, ("china_group_visa_free_policy", "Hyundai_Department_plus_7_1pct", "Hotel_Shilla_plus_4_8pct", "Hankook_Cosmetics_plus_9_9pct"), ("actual_arrivals_missing", "spending_conversion_missing", "dutyfree_sales_missing", "diplomatic_social_risk"), 9.9, None, None, None, {"hyundai_department_store_event_return_pct": 7.1, "hotel_shilla_event_return_pct": 4.8, "paradise_event_return_pct": 2.9, "hankook_cosmetics_event_return_pct": 9.9, "group_size_min": 3, "visa_free_stay_days": 15, "china_share_of_2024_korea_visitors_pct": 28, "korea_2024_visitors_mn": 16.4, "lotte_tour_event_return_pct": 9.6, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "Stage2_Actionable_tourism_consumption", "policy_event_rerating", "stage2_watch_success", "China visa-free policy plus multi-consumer-stock rally is Stage2-Actionable, not Green before spending conversion."),
    Round300CaseCandidate("r5_loop15_emart_shinsegae_alibaba_gmarket_jv", "139480/004170", "E-Mart / Shinsegae / Gmarket / AliExpress Korea", E2RArchetype.ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B, (E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE, E2RArchetype.RETAIL_PLATFORM_DATA_REGULATION_OVERLAY), "success_candidate", "success_candidate_stage2_with_regulatory_overlay", "T1/T2", "Stage2_with_regulatory_4B_overlay", "Stage2", date(2024, 12, 26), date(2025, 9, 18), None, date(2025, 9, 18), None, False, ("Gmarket_AliExpress_JV_4B_USD", "KFTC_conditional_approval", "Gmarket_customer_database_50M", "cross_border_share_41pct"), ("data_sharing_restriction_3y", "gmv_growth_missing", "take_rate_margin_pending"), None, None, None, None, {"jv_estimated_value_usd_bn": 4, "gmarket_customer_database_mn": 50, "data_sharing_restriction_years": 3, "cross_border_ecommerce_market_share_pct": 41, "china_import_online_spending_2024_krw_trn": 4.7, "alibaba_share_of_china_online_import_sales_pct": 62, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "evidence_good_but_price_failed", "Stage2_restructuring_with_data_regulatory_overlay", "unknown", "stage2_watch_success", "E-Mart/Shinsegae JV is Stage2 restructuring, but data-sharing and unit-economics gates block Green."),
    Round300CaseCandidate("r5_loop15_fnf_taylormade_brand_ma", "383220", "F&F / TaylorMade", E2RArchetype.BRAND_MA_CONTROL_RIGHTS_STAGE2, (E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION, E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE), "success_candidate", "success_candidate_stage2", "T1/T2", "Stage2_brand_MA_optional", "Stage2_brand_MA_optional", date(2021, 1, 1), date(2025, 7, 21), None, date(2025, 7, 21), None, False, ("FNF_2021_investment_358B_KRW", "TaylorMade_possible_sale_3_5B_USD", "Goldman_advisor", "consent_rights_ROFR"), ("funding_missing", "control_execution_missing", "ROIC_pending", "legal_dispute_watch"), None, None, None, None, {"fnf_2021_investment_krw_bn": 358, "taylormade_possible_sale_value_usd_bn": 3.5, "advisor": "Goldman Sachs", "claimed_rights": ["Consent Rights", "ROFR"], "dispute_party": "Centroid Investment Partners", "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "aligned", "success_candidate_stage2", "unknown", "stage2_watch_success", "F&F TaylorMade optionality is Stage2; funding, control and ROIC are required for Yellow or Green."),
    Round300CaseCandidate("r5_loop15_kyochon_cherrybro_jensen_meme", "339770/066360/348340", "Kyochon F&B / Cherrybro / Neuromeka", E2RArchetype.FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE, (E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE), "event_premium", "price_moved_without_evidence", "T1", "price_moved_without_evidence", "N/A_no_valid_stage3", date(2025, 10, 31), None, None, date(2025, 10, 31), None, False, ("Jensen_Huang_Kkanbu_Chicken_event", "Kyochon_up_to_20pct", "Cherrybro_up_to_30pct", "Kkanbu_not_listed"), ("direct_revenue_link_missing", "same_store_sales_missing", "franchise_fee_missing"), 30, None, None, None, {"kyochon_event_mfe_pct": 20, "cherrybro_event_mfe_pct": 30, "neuromeka_retained_gains_by_close": True, "kkanbu_listed": False, "nvidia_korea_ai_chip_deals_units": 260000, "direct_revenue_link_confirmed": False, "same_store_sales_confirmed": False, "franchise_fee_confirmed": False, "full_ohlc_status": "N/A_no_valid_stage3"}, "price_moved_without_evidence", "price_moved_without_evidence", "event_premium", "false_green", "Celebrity/AI visit at non-listed Kkanbu moved listed peers without direct same-store sales or franchise economics."),
)


def round300_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND300_CASE_CANDIDATES)


def round300_summary() -> dict[str, object]:
    return {
        "source_round": ROUND300_SOURCE_ROUND_PATH,
        "round_id": ROUND300_ANALYST_ROUND_ID,
        "large_sector": ROUND300_LARGE_SECTOR,
        "method": ROUND300_METHOD,
        "case_candidate_count": len(ROUND300_CASE_CANDIDATES),
        "trigger_count": len(ROUND300_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 4,
        "stage3_yellow_candidate_count": 2,
        "stage3_green_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 0,
        "missed_structural_count": 1,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round300_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND300_CASE_CANDIDATES)


def round300_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND300_TRIGGER_RECORDS)


def round300_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND300_REQUIRED_TARGET_ALIASES.items())


def round300_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND300_SHADOW_WEIGHT_ROWS)


def round300_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    rows = []
    for axis in ROUND300_SCORE_UP_AXES:
        rows.append({"axis": axis, "points": "+5", "direction": "raise", "reason": "R5 consumer trigger quality axis"})
    for axis in ROUND300_SCORE_DOWN_AXES:
        rows.append({"axis": axis, "points": "-5", "direction": "lower", "reason": "R5 headline, meme, data-rights or repeat-demand blocker"})
    return tuple(rows)


def round300_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND300_SOURCE_ROUND_PATH,
        "round_id": ROUND300_ANALYST_ROUND_ID,
        "large_sector": ROUND300_LARGE_SECTOR,
        "method": ROUND300_METHOD,
        "summary": round300_summary(),
        "target_archetypes": dict(ROUND300_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND300_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND300_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND300_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND300_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND300_SCORE_UP_AXES),
        "score_down_axes": list(ROUND300_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND300_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND300_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round300_shadow_weights_to_production_scoring_yet",
            "do_not_use_round300_cases_as_candidate_generation_input",
            "do_not_treat_celebrity_meme_policy_jv_or_ma_optional_headline_as_green",
            "do_not_ignore_repeat_purchase_spending_conversion_data_rights_or_funding_gates",
        ],
    }


def render_round300_summary_markdown() -> str:
    summary = round300_summary()
    lines = [
        "# Round 300 R5 Loop 15 Consumer/Retail/Brand Trigger Validation",
        "",
        "이번 라운드는 브랜드 headline이 아니라 ASP, shipment, capacity, OP estimate, sell-through, spending conversion, data rights, control execution을 분리한다.",
        "",
        "쉬운 예: Jensen Huang이 치킨집에 갔다고 치킨 관련주가 올라도, 상장사의 same-store sales나 franchise fee가 없으면 Stage3 근거가 아니다.",
        "",
        "## Summary",
        "",
    ]
    for key in (
        "round_id",
        "large_sector",
        "case_candidate_count",
        "trigger_count",
        "stage2_actionable_candidate_count",
        "stage3_yellow_candidate_count",
        "stage3_green_confirmed_count",
        "stage4b_watch_count",
        "stage4c_watch_count",
        "hard_4c_case_count",
        "missed_structural_count",
        "production_scoring_changed",
        "candidate_generation_input",
        "full_adjusted_ohlc_complete",
        "shadow_weight_only",
    ):
        lines.append(f"- {key}: {summary[key]}")
    lines.extend(
        [
            "",
            "## Core Findings",
            "",
            "- Samyang/Buldak은 ASP, shipment, capacity, OP estimate가 동시에 닫혀 Stage3-Yellow 후보로 승격해야 한다.",
            "- Samyang Denmark recall은 4C-watch였지만 일부 ban reversal로 hard 4C는 아니다.",
            "- Nongshim은 글로벌 매출과 U.S. target은 강하지만 OP estimate / price trigger가 없어 Stage2다.",
            "- K-beauty basket은 U.S. ecommerce sell-through와 physical retail channel trigger로 Stage2-Actionable이다.",
            "- APR/Medicube는 해외 매출과 device category가 붙었지만 4x rally라 4B valuation overlay가 필요하다.",
            "- Chinese tourism basket은 visa-free policy와 소비주 동반 상승으로 Stage2-Actionable이지만 spending conversion 전에는 Green이 아니다.",
            "- E-Mart/Shinsegae/Alibaba JV와 F&F/TaylorMade는 각각 data rights, funding/control/ROIC gate가 남는다.",
            "- Kyochon/Cherrybro/Neuromeka Jensen rally는 price_moved_without_evidence다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round300_trigger_grid_markdown() -> str:
    lines = [
        "# Round 300 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND300_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round300_stage_rules_markdown() -> str:
    lines = ["# Round 300 Stage Rules", "", "Do not apply these weights to production scoring yet.", "", "## Stage2-Actionable", ""]
    lines.extend(f"- {rule}" for rule in ROUND300_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND300_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND300_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND300_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round300_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 300 4B/4C Review",
        "",
        "이번 라운드에서 확정 Green과 hard 4C는 없다. 대신 consumer headline을 걸러내는 4B/4C-watch가 많다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND300_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND300_HARD_4C_GATES)
    return "\n".join(lines) + "\n"


def render_round300_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 300 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2/Yellow 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 trigger date 기준 30/90/180일 MFE/MAE, below-entry, repeat purchase, spending conversion, data rights gate를 채운다.",
            "",
        ]
    )


def write_round300_r5_loop15_reports(
    *,
    output_directory: str | Path = ROUND300_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND300_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND300_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND300_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND300_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round300_case_records(), cases_path),
        "triggers": write_round300_triggers(triggers_path),
        "audit": _write_json(round300_audit_payload(), audit_path),
        "weight_profile": _write_csv(round300_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round300_r5_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round300_r5_loop15_case_matrix.csv",
        "trigger_grid": output / "round300_r5_loop15_trigger_grid.csv",
        "target_aliases": output / "round300_r5_loop15_target_aliases.csv",
        "score_adjustments": output / "round300_r5_loop15_score_adjustments.csv",
        "shadow_weights": output / "round300_r5_loop15_shadow_weights.csv",
        "stage_rules": output / "round300_r5_loop15_stage_rules.md",
        "trigger_grid_md": output / "round300_r5_loop15_trigger_grid.md",
        "price_validation_plan": output / "round300_r5_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round300_r5_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round300_summary_markdown(), encoding="utf-8")
    _write_csv(round300_case_rows(), paths["case_matrix"])
    _write_csv(round300_trigger_rows(), paths["trigger_grid"])
    _write_csv(round300_target_alias_rows(), paths["target_aliases"])
    _write_csv(round300_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round300_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round300_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round300_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round300_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round300_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round300_triggers(path: str | Path = ROUND300_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND300_TRIGGER_RECORDS]
    target.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return target


def _write_json(payload: Mapping[str, object], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[Mapping[str, object]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows_tuple = tuple(rows)
    with target.open("w", encoding="utf-8", newline="") as handle:
        if not rows_tuple:
            handle.write("")
            return target
        writer = csv.DictWriter(handle, fieldnames=list(rows_tuple[0].keys()))
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow({key: _value_text(value) for key, value in row.items()})
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def _signed(value: int) -> str:
    return f"{value:+d}"


__all__ = [
    "ROUND300_CASE_CANDIDATES",
    "ROUND300_GREEN_BLOCKERS",
    "ROUND300_HARD_4C_GATES",
    "ROUND300_LARGE_SECTOR",
    "ROUND300_REQUIRED_TARGET_ALIASES",
    "ROUND300_SCORE_DOWN_AXES",
    "ROUND300_SCORE_UP_AXES",
    "ROUND300_SHADOW_WEIGHT_ROWS",
    "ROUND300_STAGE2_ACTIONABLE_RULES",
    "ROUND300_STAGE3_GREEN_RULES",
    "ROUND300_STAGE3_YELLOW_RULES",
    "ROUND300_STAGE4B_WATCH_TRIGGERS",
    "ROUND300_TRIGGER_RECORDS",
    "render_round300_stage_rules_markdown",
    "render_round300_stage4b_4c_review_markdown",
    "render_round300_trigger_grid_markdown",
    "round300_audit_payload",
    "round300_case_records",
    "round300_case_rows",
    "round300_shadow_weight_rows",
    "round300_summary",
    "round300_trigger_rows",
    "write_round300_r5_loop15_reports",
]
