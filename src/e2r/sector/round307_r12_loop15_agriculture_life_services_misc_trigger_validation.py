"""Round-307 R12 Loop-15 agriculture/life-services/misc trigger pack.

This module turns ``docs/round/round_307.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a fertilizer export restriction is a real Stage2 event, but it
does not become Stage3 until domestic ASP, inventory, sales volume and margin
pass-through are visible. The same separation applies to AI textbook policy,
food-delivery M&A teasers, viral IP IPOs and recycling policy headlines.
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


ROUND307_SOURCE_ROUND_PATH = "docs/round/round_307.md"
ROUND307_ANALYST_ROUND_ID = "round_235"
ROUND307_LARGE_SECTOR = "AGRICULTURE_LIFE_SERVICES_MISC"
ROUND307_METHOD = "trigger_level_backtest_v1"
ROUND307_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round307_r12_loop15_agriculture_life_services_misc_trigger_validation"
ROUND307_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop15_round235.jsonl"
ROUND307_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r12_loop15_round235.jsonl"
ROUND307_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round307_r12_loop15_agriculture_life_services_misc_trigger_validation_audit.json"
ROUND307_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round235_r12_loop15_v1.csv"

ROUND307_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT": E2RArchetype.FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT.value,
    "AGRI_FEED_PRICE_INPUT_COST_4C_WATCH": E2RArchetype.AGRI_FEED_PRICE_INPUT_COST_4C_WATCH.value,
    "AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C": E2RArchetype.AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C.value,
    "HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2": E2RArchetype.HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2.value,
    "FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B": E2RArchetype.FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B.value,
    "ECOMMERCE_DATA_BREACH_HARD_4C": E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C.value,
    "CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B": E2RArchetype.CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B.value,
    "PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE": E2RArchetype.PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE.value,
    "SHRINKFLATION_PRICE_REGULATION_4C_WATCH": E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH.value,
}

ROUND307_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "policy_or_supply_shock_closes_into_domestic_asp_margin_contract_or_paid_adoption",
    "education_policy_has_actual_contract_paid_adoption_and_teacher_parent_acceptance",
    "life_service_ma_has_binding_offer_financing_approval_path_and_take_rate_economics",
    "platform_life_service_keeps_data_security_trust_intact",
    "ip_edutainment_has_recurring_licensing_merchandise_or_next_ip_evidence",
    "waste_recycling_has_cleanup_contract_tipping_fee_utilization_or_carbon_pass_through",
    "market_relative_event_reaction_exceeds_5pp_and_is_linked_to_public_evidence",
)

ROUND307_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "trigger_can_change_eps_op_fcf_path_but_one_core_gate_remains",
    "pinkfong_next_ip_or_licensing_revenue_starts_to_confirm_but_durability_is_pending",
    "hagwon_listed_company_enrollment_arpu_and_margin_confirm_despite_regulatory_risk",
    "food_delivery_ma_has_binding_acquisition_but_integration_or_take_rate_is_pending",
    "fertilizer_domestic_asp_or_margin_pass_through_appears_but_full_volume_cash_proof_is_pending",
)

ROUND307_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "agriculture_input_shock_links_to_domestic_asp_margin_volume_and_cash_conversion",
    "edtech_has_paid_adoption_school_contract_teacher_acceptance_and_privacy_safety",
    "private_education_has_enrollment_arpu_margin_and_low_regulatory_risk",
    "life_platform_has_ma_approval_take_rate_data_security_and_retention_closed",
    "children_ip_has_recurring_franchise_revenue_not_one_hit_only",
    "waste_recycling_has_contracts_tipping_fee_facility_utilization_and_margin",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND307_GREEN_BLOCKERS: tuple[str, ...] = (
    "commodity_supply_shock_without_company_margin",
    "edtech_policy_headline_without_school_contract",
    "ai_textbook_without_teacher_parent_acceptance",
    "hagwon_demand_without_listed_company_margin",
    "ma_teaser_without_binding_offer",
    "platform_scale_without_security",
    "viral_ip_without_next_franchise",
    "recycling_rate_headline_without_economics",
    "full_adjusted_ohlc_missing_for_stage3_confirmation",
)

ROUND307_SCORE_UP_AXES: tuple[str, ...] = (
    "domestic_ASP_margin_pass_through",
    "inventory_and_import_mix_visibility",
    "school_contract_paid_adoption",
    "policy_rollback_risk",
    "listed_company_enrollment_ARPU",
    "platform_data_security_trust",
    "binding_MA_approval_take_rate",
    "recurring_IP_revenue",
    "cleanup_contract_tipping_fee_visibility",
)

ROUND307_SCORE_DOWN_AXES: tuple[str, ...] = (
    "commodity_supply_shock_without_company_margin",
    "edtech_policy_headline_without_school_contract",
    "AI_textbook_without_teacher_parent_acceptance",
    "hagwon_structural_demand_without_margin",
    "M&A_teaser_without_binding_offer",
    "platform_scale_without_security",
    "viral_IP_without_next_franchise",
    "recycling_rate_headline_without_economics",
)

ROUND307_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "fertilizer_basket_rerates_on_china_export_controls_before_domestic_margin_evidence",
    "edtech_policy_announcement_prices_before_school_adoption",
    "ma_teaser_is_priced_as_binding_acquisition",
    "platform_scale_ignores_data_security_or_customer_trust",
    "viral_ip_ipo_prices_without_next_franchise_revenue",
    "recycling_policy_headline_prices_without_cleanup_economics",
)

ROUND307_HARD_4C_GATES: tuple[str, ...] = (
    "large_customer_data_breach",
    "policy_rollback_or_official_status_downgrade",
    "classroom_device_ban_reduces_edtech_adoption",
    "input_cost_shock_cannot_pass_through",
    "cleanup_liability_without_profitable_treatment_contract",
    "social_backlash_against_education_or_childcare_burden",
    "ma_blocked_by_regulator_or_merchant_fee_politics",
)


@dataclass(frozen=True)
class Round307ShadowWeightRow:
    archetype: E2RArchetype
    domestic_asp_margin_pass_through: int
    inventory_import_mix_visibility: int
    school_contract_paid_adoption: int
    policy_rollback_risk: int
    listed_company_enrollment_arpu: int
    platform_data_security_trust: int
    binding_ma_approval_take_rate: int
    recurring_ip_revenue: int
    cleanup_contract_tipping_fee_visibility: int
    commodity_supply_shock_without_company_margin_penalty: int
    edtech_policy_without_school_contract_penalty: int
    ai_textbook_without_teacher_parent_acceptance_penalty: int
    ma_teaser_without_binding_offer_penalty: int
    platform_scale_without_security_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "domestic_asp_margin_pass_through": _signed(self.domestic_asp_margin_pass_through),
            "inventory_import_mix_visibility": _signed(self.inventory_import_mix_visibility),
            "school_contract_paid_adoption": _signed(self.school_contract_paid_adoption),
            "policy_rollback_risk": _signed(self.policy_rollback_risk),
            "listed_company_enrollment_arpu": _signed(self.listed_company_enrollment_arpu),
            "platform_data_security_trust": _signed(self.platform_data_security_trust),
            "binding_ma_approval_take_rate": _signed(self.binding_ma_approval_take_rate),
            "recurring_ip_revenue": _signed(self.recurring_ip_revenue),
            "cleanup_contract_tipping_fee_visibility": _signed(self.cleanup_contract_tipping_fee_visibility),
            "commodity_supply_shock_without_company_margin_penalty": _signed(self.commodity_supply_shock_without_company_margin_penalty),
            "edtech_policy_without_school_contract_penalty": _signed(self.edtech_policy_without_school_contract_penalty),
            "ai_textbook_without_teacher_parent_acceptance_penalty": _signed(self.ai_textbook_without_teacher_parent_acceptance_penalty),
            "ma_teaser_without_binding_offer_penalty": _signed(self.ma_teaser_without_binding_offer_penalty),
            "platform_scale_without_security_penalty": _signed(self.platform_scale_without_security_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round307TriggerRecord:
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
class Round307CaseCandidate:
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
            "do_not_use_round307_cases_as_candidate_generation_input",
            "do_not_treat_agriculture_life_service_policy_or_event_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND307_LARGE_SECTOR,
            large_sector=ROUND307_LARGE_SECTOR,
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
            stage1_evidence=tuple(field for field in self.evidence_fields if "policy" in field or "headline" in field or "awareness" in field),
            stage2_evidence=tuple(field for field in self.evidence_fields if "stage2" in field or "price_anchor" in field or "arpu" in field or "bid" in field or "ipo" in field),
            stage3_evidence=tuple(field for field in self.evidence_fields if "margin" in field or "recurring" in field or "paid" in field),
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4b" in field or "teaser" in field or "one_hit" in field),
            stage4c_evidence=tuple(field for field in self.red_flag_fields if "4c" in field or "breach" in field or "rollback" in field or "liability" in field),
            must_have_fields=ROUND307_STAGE3_GREEN_RULES,
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
            price_validation=PriceValidation(price_validation_status="price_data_unavailable_after_deep_search"),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.7,
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


ROUND307_CASE_CANDIDATES: tuple[Round307CaseCandidate, ...] = (
    Round307CaseCandidate(
        case_id="r12_loop15_fertilizer_export_control_korea_basket",
        symbol="025860/001390/001550/fertilizer_basket",
        company_name="Namhae Chemical / KG Chemical / Chobi / fertilizer basket",
        primary_archetype=E2RArchetype.FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT,
        secondary_archetypes=(E2RArchetype.FERTILIZER_INPUT_PRICE_COST_KOREA,),
        case_type="event_premium",
        round_case_type="Stage2_event_with_4B_supply_watch",
        best_trigger="T1/T3",
        best_trigger_type="Stage2_event_with_4B_supply_watch",
        stage_candidate="Stage2 event",
        stage1_date=date(2021, 1, 1),
        stage2_date=date(2026, 3, 19),
        stage3_date=None,
        stage4b_date=date(2026, 4, 28),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("fertilizer_export_control_policy", "stage2_supply_shock", "urea_price_anchor", "korea_urea_supply_memory"),
        red_flag_fields=("domestic_ASP_missing", "margin_pass_through_missing", "inventory_mix_missing", "company_sales_missing", "supply_shock_4b_watch"),
        event_mfe_pct=None,
        event_mae_pct=None,
        extra_price_metrics={
            "china_fertilizer_exports_usd_bn": 13,
            "potential_export_restriction_volume_mn_tons": 40,
            "restricted_export_share_range_pct": "50-75",
            "international_urea_price_rise_from_prewar_pct": 40,
            "ammonium_sulphate_inspection_tightening": True,
        },
        score_price_alignment="false_positive_score",
        round_alignment_label="Stage2_event_not_Green",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        notes="Global fertilizer supply shock is Stage2; domestic ASP, inventory, margin and sales evidence are required before Yellow or Green.",
    ),
    Round307CaseCandidate(
        case_id="r12_loop15_feed_wheat_tender_input_cost",
        symbol="feed_livestock_food_cost_basket",
        company_name="Feed / livestock / food-cost read-through",
        primary_archetype=E2RArchetype.AGRI_FEED_PRICE_INPUT_COST_4C_WATCH,
        secondary_archetypes=(E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH,),
        case_type="4c_thesis_break",
        round_case_type="input_cost_4C_watch",
        best_trigger="T1/T2",
        best_trigger_type="4C_watch_input_cost",
        stage_candidate="4C-watch",
        stage1_date=date(2026, 5, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 13),
        hard_4c_confirmed=False,
        evidence_fields=("feed_wheat_tender_failure", "grain_input_cost_pressure", "cargill_offer_price_anchor"),
        red_flag_fields=("input_cost_shock_4c_watch", "pass_through_missing", "inventory_buffer_missing", "margin_compression_risk"),
        event_mfe_pct=None,
        event_mae_pct=None,
        extra_price_metrics={"feed_wheat_tender_volume_tons": 65000, "lowest_offer_cargill_usd_per_ton_cnf": 298.5, "extra_unloading_surcharge_usd_per_ton": 2.0},
        score_price_alignment="aligned",
        round_alignment_label="agri_input_cost_4C_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Failed feed wheat tender is input-cost pressure, not growth. It belongs in RedTeam/4C watch until pass-through is proved.",
    ),
    Round307CaseCandidate(
        case_id="r12_loop15_ai_digital_textbook_policy_rollback",
        symbol="095720/133750/289010/edtech_basket",
        company_name="Woongjin ThinkBig / MegaStudy / Icecream Edu / edtech basket",
        primary_archetype=E2RArchetype.AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C,
        secondary_archetypes=(E2RArchetype.EDTECH_POLICY_ROLLBACK_4C, E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL),
        case_type="4c_thesis_break",
        round_case_type="Stage2_policy_with_rollback_4C",
        best_trigger="T0/T2",
        best_trigger_type="Stage2_policy_with_rollback_4C",
        stage_candidate="Stage2 policy to 4C-watch",
        stage1_date=date(2024, 8, 18),
        stage2_date=date(2024, 8, 18),
        stage3_date=None,
        stage4b_date=date(2024, 8, 18),
        stage4c_date=date(2025, 8, 4),
        hard_4c_confirmed=False,
        evidence_fields=("ai_textbook_policy_headline", "planned_2025_rollout", "parent_petition_backlash", "policy_rollback_evidence"),
        red_flag_fields=("official_textbook_status_downgrade", "classroom_device_ban", "teacher_parent_acceptance_missing", "paid_adoption_missing", "rollback_4c_watch"),
        event_mfe_pct=None,
        event_mae_pct=None,
        extra_price_metrics={"planned_rollout_year": 2025, "parent_petition_count_context": ">50000", "classroom_device_ban_effective": "2026-03"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="policy_rollback_4C_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="AI textbook policy was real Stage2, but official-status rollback and classroom device restrictions cap edtech Green.",
    ),
    Round307CaseCandidate(
        case_id="r12_loop15_hagwon_preschool_private_education",
        symbol="215200/019680/095720/133750/private_education_basket",
        company_name="MegaStudy / Daekyo / Woongjin ThinkBig / Creverse / hagwon basket",
        primary_archetype=E2RArchetype.HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2,
        secondary_archetypes=(E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C,),
        case_type="success_candidate",
        round_case_type="structural_stage2_with_social_4B",
        best_trigger="T0/T1",
        best_trigger_type="Stage2_structural_with_4B_social_overlay",
        stage_candidate="Stage2 structural",
        stage1_date=date(2025, 3, 16),
        stage2_date=date(2025, 3, 16),
        stage3_date=None,
        stage4b_date=date(2025, 3, 16),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("under_six_enrollment_arpu", "hagwon_tuition_arpu", "structural_private_education_demand", "stage2_demographic_arpu_evidence"),
        red_flag_fields=("social_regulatory_4b", "listed_company_margin_missing", "policy_tolerance_missing", "low_birthrate_pressure"),
        event_mfe_pct=None,
        event_mae_pct=None,
        extra_price_metrics={"under_six_hagwon_enrollment_pct": 47.6, "under_two_hagwon_enrollment_pct": 25, "preschool_monthly_tuition_avg_krw": 332000, "english_kindergarten_monthly_tuition_avg_krw": 1500000},
        score_price_alignment="unknown",
        round_alignment_label="structural_stage2_with_social_4B",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        notes="Hagwon demand and ARPU are structural, but listed-company enrollment, ARPU, margin and policy tolerance are still the gates.",
    ),
    Round307CaseCandidate(
        case_id="r12_loop15_naver_uber_baemin_food_delivery_ma",
        symbol="035420/Baemin_private/Delivery_Hero_readthrough",
        company_name="Naver / Uber / Baedal Minjok / Delivery Hero",
        primary_archetype=E2RArchetype.FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B,
        secondary_archetypes=(E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2,),
        case_type="event_premium",
        round_case_type="Stage2_MA_optionality_with_4B",
        best_trigger="T0/T3",
        best_trigger_type="Stage2_MA_optionality_with_4B_regulatory_overlay",
        stage_candidate="Stage2 M&A",
        stage1_date=date(2026, 5, 18),
        stage2_date=date(2026, 5, 18),
        stage3_date=None,
        stage4b_date=date(2026, 5, 18),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("reported_bid_value", "consortium_split", "delivery_hero_price_anchor", "ma_stage2_headline"),
        red_flag_fields=("binding_offer_missing", "kftc_approval_missing", "take_rate_economics_missing", "ma_teaser_4b_watch"),
        event_mfe_pct=5.6,
        event_mae_pct=None,
        extra_price_metrics={"reported_baemin_bid_krw_trn": 8.0, "reported_baemin_bid_usd_bn": 5.34, "uber_pct": 80, "naver_pct": 20, "delivery_hero_event_return_pct": 5.6},
        score_price_alignment="false_positive_score",
        round_alignment_label="Stage2_MA_not_Green",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        notes="Food-delivery M&A optionality is Stage2; binding bid, KFTC approval, funding and take-rate economics are required.",
    ),
    Round307CaseCandidate(
        case_id="r12_loop15_coupang_data_breach_life_service_4c",
        symbol="CPNG/Korea_ecommerce_readthrough",
        company_name="Coupang / Korea e-commerce life-service reference",
        primary_archetype=E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE, E2RArchetype.ECOMMERCE_PLATFORM_DATA_BREACH_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4C_with_false_break_relief",
        best_trigger="T0/T3",
        best_trigger_type="hard_4C_with_false_break_relief",
        stage_candidate="4C",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 12, 26),
        stage4c_date=date(2025, 12, 1),
        hard_4c_confirmed=True,
        evidence_fields=("data_breach_hard_4c", "affected_customer_accounts", "ceo_resignation", "regulatory_probe", "false_break_relief"),
        red_flag_fields=("large_customer_data_breach", "platform_trust_break", "police_probe", "tax_agency_audit", "customer_churn_risk"),
        event_mfe_pct=9.0,
        event_mae_pct=-4.4,
        extra_price_metrics={"affected_customer_accounts_mn": 33.7, "premarket_event_return_pct": -4.4, "relief_event_return_pct": 9.0, "stock_performance_before_breach_ytd_pct": 28},
        score_price_alignment="aligned",
        round_alignment_label="hard_4c_security_with_false_break_relief",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Life-service platform scale without data security becomes hard 4C. Later relief is false-break relief, not growth.",
    ),
    Round307CaseCandidate(
        case_id="r12_loop15_pinkfong_babyshark_ipo",
        symbol="Pinkfong/Samsung_Publishing_readthrough",
        company_name="Pinkfong / Baby Shark / Samsung Publishing read-through",
        primary_archetype=E2RArchetype.CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B,
        secondary_archetypes=(E2RArchetype.KIDS_IP_PLATFORM_KOREA,),
        case_type="success_candidate",
        round_case_type="Stage2_Actionable_with_4B_one_hit_overlay",
        best_trigger="T1/T2",
        best_trigger_type="Stage2-Actionable_with_4B_one_hit_overlay",
        stage_candidate="Stage2-Actionable",
        stage1_date=date(2018, 1, 1),
        stage2_date=date(2025, 11, 18),
        stage3_date=None,
        stage4b_date=date(2025, 11, 18),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("ipo_price_anchor", "debut_return", "global_ip_views", "op_sales_evidence", "stage2_actionable_ip_event"),
        red_flag_fields=("one_hit_wonder_4b", "next_ip_revenue_missing", "recurring_licensing_missing", "valuation_25x_context"),
        event_mfe_pct=62.0,
        event_mae_pct=None,
        extra_price_metrics={"ipo_price_krw": 38000, "ipo_raise_krw_bn": 76, "debut_intraday_high_krw": 61500, "debut_intraday_mfe_pct": 62, "debut_close_krw": 41550, "debut_close_return_pct": 9, "baby_shark_youtube_views_bn": 16, "sales_2024_krw_bn": 97.4, "op_2024_krw_bn": 18.8, "valuation_context_2025e_pe": 25},
        score_price_alignment="aligned",
        round_alignment_label="Stage2_Actionable_IPO_with_4B_one_hit_risk",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        notes="IPO pop and global IP evidence are Actionable; recurring licensing, merchandise and next-IP revenue are required for Yellow or Green.",
    ),
    Round307CaseCandidate(
        case_id="r12_loop15_plastic_recycling_policy_false_positive",
        symbol="waste_recycling_basket/KG_ETS_readthrough/SK_ecoplant_private_readthrough",
        company_name="Waste / recycling policy basket",
        primary_archetype=E2RArchetype.PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.WASTE_RECYCLING_INFRA_STAGE2, E2RArchetype.WASTE_RECYCLING_ENVIRONMENT),
        case_type="failed_rerating",
        round_case_type="policy_false_positive_watch",
        best_trigger="T0/T2",
        best_trigger_type="Stage2_policy_false_positive_watch",
        stage_candidate="Stage2 policy only",
        stage1_date=date(2024, 11, 22),
        stage2_date=date(2024, 11, 22),
        stage3_date=None,
        stage4b_date=date(2024, 11, 22),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("recycling_policy_headline", "official_recycling_rate", "true_recycling_rate_gap", "cleanup_liability_evidence"),
        red_flag_fields=("cleanup_contract_missing", "tipping_fee_missing", "true_recycling_economics_weak", "untreated_waste_liability", "policy_theme_false_positive"),
        event_mfe_pct=None,
        event_mae_pct=None,
        extra_price_metrics={"claimed_plastic_recycling_rate_pct": 73, "greenpeace_estimated_real_recycling_rate_pct": 27, "plastic_waste_growth_2019_2022_pct": 31, "asan_untreated_plastic_waste_tons": 19000, "estimated_cleanup_cost_krw_bn": "2-3"},
        score_price_alignment="false_positive_score",
        round_alignment_label="policy_theme_false_positive_watch",
        rerating_result="no_rerating",
        stage_failure_type="false_yellow",
        notes="Recycling policy headline is not Green without cleanup contracts, tipping fees, facility utilization and treatment economics.",
    ),
)


ROUND307_TRIGGER_RECORDS: tuple[Round307TriggerRecord, ...] = (
    Round307TriggerRecord("r12l15_fertilizer_china_T1", "r12_loop15_fertilizer_export_control_korea_basket", "Stage2_event", "2026-03-19", "China restricts fertilizer exports; exported more than $13B fertilizer; restrictions may affect 50-75% exports, up to 40M tons; urea +40% from pre-war levels", "price_data_unavailable_after_deep_search", "Stage2_event_not_Green", "Stage2", {"potential_export_restriction_volume_mn_tons": 40}),
    Round307TriggerRecord("r12l15_feed_wheat_T1", "r12_loop15_feed_wheat_tender_input_cost", "4C-watch", "2026-05-13", "Korea FLC believed no purchase in 65,000t feed wheat tender due high offers; lowest offer $298.50/t C&F plus $2 surcharge", "price_data_unavailable_after_deep_search", "agri_input_cost_4C_watch", "4C-watch", {"lowest_offer_cargill_usd_per_ton_cnf": 298.5}),
    Round307TriggerRecord("r12l15_ai_textbook_T0", "r12_loop15_ai_digital_textbook_policy_rollback", "Stage2_policy", "2024-08-18", "Korea planned AI digital textbooks from 2025 for children as young as 8; 50k+ parents petitioned against screen/misinformation/privacy concerns", "price_data_unavailable_after_deep_search", "Stage2_policy_with_4B_social_backlash", "Stage2", {"parent_petition_count_context": ">50000"}),
    Round307TriggerRecord("r12l15_ai_textbook_T2", "r12_loop15_ai_digital_textbook_policy_rollback", "4C-watch", "2025-08-04", "National Assembly stripped AI textbooks of official textbook status and reclassified them as supplementary materials", "price_data_unavailable_after_deep_search", "policy_rollback_4C_watch", "4C-watch", {"rollback": "official_textbook_to_supplementary_material"}),
    Round307TriggerRecord("r12l15_hagwon_preschool_T0", "r12_loop15_hagwon_preschool_private_education", "Stage2_structural", "2025-03-16", "47.6% of under-six children and 25% of under-two children attend hagwon; preschool average tuition Won332k/month; English kindergartens Won1.5mn/month", "price_data_unavailable_after_deep_search", "structural_stage2_with_social_4B", "Stage2", {"under_six_hagwon_enrollment_pct": 47.6}),
    Round307TriggerRecord("r12l15_baemin_naver_T0", "r12_loop15_naver_uber_baemin_food_delivery_ma", "Stage2_MA", "2026-05-18", "Uber/Naver consortium reportedly bids up to 8T won for Baemin; Uber 80%, Naver 20%; Naver received teaser letter but no decision", "Naver price unavailable / Delivery Hero +5.6 related", "Stage2_MA_not_Green", "Stage2", {"reported_baemin_bid_krw_trn": 8.0}),
    Round307TriggerRecord("r12l15_coupang_breach_T0", "r12_loop15_coupang_data_breach_life_service_4c", "hard_4C", "2025-12-01", "Coupang data breach affects 33.7M customer accounts; stock -4.4% premarket", -4.4, "hard_4c_security", "4C", {"affected_customer_accounts_mn": 33.7}),
    Round307TriggerRecord("r12l15_coupang_breach_T3", "r12_loop15_coupang_data_breach_life_service_4c", "false_break_relief", "2025-12-26", "Coupang shares +9% after update says limited retained data and no payment/login/customs data compromised", 9.0, "false_break_relief", "4C_watch_relief", {"payment_login_customs_data_compromised": False}),
    Round307TriggerRecord("r12l15_pinkfong_ipo_T2", "r12_loop15_pinkfong_babyshark_ipo", "Stage2-Actionable+4B-watch", "2025-11-18", "Pinkfong IPO debut: +62% intraday to 61,500 won, close +9% at 41,550 won; Baby Shark 16B+ YouTube views; IPO raised 76B won", 62.0, "Stage2_Actionable_with_4B_one_hit_overlay", "Stage2-Actionable", {"debut_intraday_mfe_pct": 62}),
    Round307TriggerRecord("r12l15_plastic_recycling_T1", "r12_loop15_plastic_recycling_policy_false_positive", "false_positive_watch", "2024-11-22", "Korea claims 73% plastic recycling but Greenpeace estimates true rate 27%; plastic waste +31% 2019-2022; Asan site has 19,000t untreated waste", "price_data_unavailable_after_deep_search", "policy_theme_false_positive_watch", "Stage2_policy_only", {"greenpeace_estimated_real_recycling_rate_pct": 27}),
)


ROUND307_SHADOW_WEIGHT_ROWS: tuple[Round307ShadowWeightRow, ...] = (
    Round307ShadowWeightRow(E2RArchetype.FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT, 5, 4, 0, 1, 0, 0, 0, 0, 0, -5, -1, -1, -1, -1, "global supply shock", "domestic ASP/margin missing", "ASP+inventory+margin pass-through", "Fertilizer event Stage2 only."),
    Round307ShadowWeightRow(E2RArchetype.AGRI_FEED_PRICE_INPUT_COST_4C_WATCH, 4, 3, 0, 1, 0, 0, 0, 0, 0, -4, -1, -1, -1, -1, "input cost shock", "pass-through missing", "feed cost stabilization", "Feed wheat tender 4C-watch."),
    Round307ShadowWeightRow(E2RArchetype.AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C, 0, 0, 5, 5, 2, 4, 0, 1, 0, -1, -5, -5, -1, -1, "policy rollout", "school contracts/acceptance missing", "paid adoption+acceptance+learning outcomes", "AI textbook rollback."),
    Round307ShadowWeightRow(E2RArchetype.HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2, 0, 0, 1, 4, 5, 1, 0, 0, 0, -1, -2, -2, -1, -1, "enrollment+tuition ARPU", "listed-company margin missing", "enrollment+ARPU+margin", "Hagwon structural Stage2."),
    Round307ShadowWeightRow(E2RArchetype.FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B, 0, 0, 0, 2, 0, 4, 5, 0, 0, -1, -1, -1, -5, -4, "reported M&A bid", "binding offer/KFTC/take-rate missing", "approval+take-rate+synergy", "Baemin/Naver Stage2 M&A."),
    Round307ShadowWeightRow(E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C, 0, 0, 0, 2, 0, 5, 1, 0, 0, -1, -1, -1, -1, -5, "data breach", "trust recovery pending", "security restored+churn controlled", "Coupang hard 4C."),
    Round307ShadowWeightRow(E2RArchetype.CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B, 0, 0, 0, 1, 0, 1, 0, 5, 0, -1, -1, -1, -1, -1, "IPO pop+global IP", "next-IP revenue missing", "recurring licensing+next franchise", "Pinkfong Stage2-Actionable."),
    Round307ShadowWeightRow(E2RArchetype.PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE, 0, 0, 0, 3, 0, 0, 0, 0, 5, -1, -1, -1, -1, -1, "recycling policy", "cleanup contract/tipping fee missing", "contracted treatment economics", "Plastic recycling false-positive watch."),
    Round307ShadowWeightRow(E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH, 3, 1, 0, 4, 0, 0, 0, 0, 0, -2, -1, -1, -1, -1, "price regulation", "margin/label compliance missing", "compliance+pricing power", "Consumer-life price regulation watch."),
)


def round307_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND307_CASE_CANDIDATES]


def round307_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND307_CASE_CANDIDATES]


def round307_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND307_TRIGGER_RECORDS]


def round307_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND307_SHADOW_WEIGHT_ROWS]


def round307_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND307_REQUIRED_TARGET_ALIASES.items()]


def round307_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND307_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND307_SCORE_DOWN_AXES]
    )


def round307_summary() -> dict[str, object]:
    return {
        "source_round": ROUND307_SOURCE_ROUND_PATH,
        "round_id": ROUND307_ANALYST_ROUND_ID,
        "large_sector": ROUND307_LARGE_SECTOR,
        "method": ROUND307_METHOD,
        "case_candidate_count": len(ROUND307_CASE_CANDIDATES),
        "trigger_count": len(ROUND307_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND307_REQUIRED_TARGET_ALIASES),
        "stage2_event_candidate_count": 5,
        "stage2_actionable_candidate_count": 1,
        "stage3_yellow_candidate_count": 4,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 5,
        "hard_4c_case_count": 1,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round307_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND307_SOURCE_ROUND_PATH,
        "round_id": ROUND307_ANALYST_ROUND_ID,
        "large_sector": ROUND307_LARGE_SECTOR,
        "method": ROUND307_METHOD,
        "summary": round307_summary(),
        "required_target_aliases": dict(ROUND307_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND307_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND307_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND307_STAGE3_GREEN_RULES,
        "green_blockers": ROUND307_GREEN_BLOCKERS,
        "score_up_axes": ROUND307_SCORE_UP_AXES,
        "score_down_axes": ROUND307_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND307_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND307_HARD_4C_GATES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round307_cases_as_candidate_generation_input",
            "do_not_treat_policy_supply_shock_ma_teaser_or_viral_ip_as_green",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round307_summary_markdown() -> str:
    summary = round307_summary()
    lines = [
        "# R12 Loop 15 Agriculture / Life Services / Misc Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: fertilizer export controls are like a smoke alarm. They justify Stage2 attention, but without domestic ASP and margin proof they are not Stage3 evidence.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Stage2 events: fertilizer export controls, AI textbook rollout, hagwon demand, Baemin/Naver M&A, plastic recycling policy.",
            "- Stage2-Actionable: Pinkfong IPO, with a one-hit/valuation 4B overlay.",
            "- Hard 4C: Coupang data breach. Strong 4C-watch: AI textbook rollback, feed wheat input-cost pressure, recycling cleanup liability.",
            "- Stage3-Green confirmed: `0`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round307_trigger_grid_markdown() -> str:
    lines = [
        "# Round 307 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round307_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round307_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 307 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND307_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND307_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND307_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND307_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND307_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round307_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 307 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND307_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C / Watch Cases",
    ]
    for case in ROUND307_CASE_CANDIDATES:
        if case.stage4c_date or case.stage4b_date or "4C" in case.stage_candidate:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round307_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 307 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event returns, IPO/debut anchors, policy quantities and affected-user anchors are retained without inventing MFE/MAE.",
        "",
    ]
    for case in ROUND307_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def write_round307_r12_loop15_reports(
    output_directory: str | Path = ROUND307_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND307_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND307_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND307_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND307_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round307_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND307_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round307_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round307_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round307_r12_loop15_case_matrix.csv",
        "target_aliases": output_dir / "round307_r12_loop15_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round307_r12_loop15_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round307_r12_loop15_trigger_grid.md",
        "summary": output_dir / "round307_r12_loop15_trigger_validation_summary.md",
        "stage_rules": output_dir / "round307_r12_loop15_stage_rules.md",
        "stage4b_4c_review": output_dir / "round307_r12_loop15_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round307_r12_loop15_score_adjustments.csv",
        "shadow_weights": output_dir / "round307_r12_loop15_shadow_weights.csv",
        "price_validation_plan": output_dir / "round307_r12_loop15_price_validation_plan.md",
    }

    _write_csv(paths["case_matrix"], round307_case_rows())
    _write_csv(paths["target_aliases"], round307_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round307_trigger_rows())
    _write_csv(paths["score_adjustments"], round307_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round307_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round307_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round307_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round307_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round307_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round307_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def _write_csv(path: Path, rows: Iterable[Mapping[str, str]]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
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
