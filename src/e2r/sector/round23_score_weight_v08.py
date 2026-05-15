"""Round-23 cases_v05 expansion and score-weight v0.8 hypotheses.

Round 23 adds thin archetypes and recalibrates HBM/data-center infrastructure.
It is report-only calibration material. Production feature engineering,
scoring, staging, and RedTeam code must not import this module.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND23_SOURCE_ROUND_PATH = "docs/round/round_23.md"
ROUND23_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round23_score_weight_v08"
ROUND23_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v05_round23.jsonl"
ROUND23_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round23_v08.csv"


@dataclass(frozen=True)
class Round23ScoreWeightDraft:
    eps_fcf: int
    structural_visibility: int
    bottleneck_pricing: int
    market_mispricing: int
    valuation: int
    capital_allocation: int = 0
    information_confidence: int = 5

    def as_dict(self) -> dict[str, int]:
        return {
            "eps_fcf": self.eps_fcf,
            "structural_visibility": self.structural_visibility,
            "bottleneck_pricing": self.bottleneck_pricing,
            "market_mispricing": self.market_mispricing,
            "valuation": self.valuation,
            "capital_allocation": self.capital_allocation,
            "information_confidence": self.information_confidence,
        }


@dataclass(frozen=True)
class Round23ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round23ScoreWeightDraft
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    normalization_point: str

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round23CaseCandidate:
    case_id: str
    target_id: str
    symbol: str
    company_name: str
    market: str
    case_type: str
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND23_SCORE_TARGETS: tuple[Round23ScoreTarget, ...] = (
    Round23ScoreTarget(
        "DIGITAL_HEALTHCARE_AI",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round23ScoreWeightDraft(18, 17, 8, 13, 12, 0, 7),
        ("regulatory_clearance", "hospital_adoption", "reimbursement_or_paid_usage", "external_clinical_validation", "revenue_or_op_conversion"),
        ("paper_only", "no_reimbursement", "overtrust_risk", "liability_unclear", "subgroup_validation_gap"),
        ("medical_ai_theme_overheated", "valuation_priced_before_revenue"),
        ("regulatory_rejection", "liability_event", "hospital_adoption_failure", "reimbursement_denial"),
        "Medical AI can move Watch-to-Green only with clearance, workflow adoption, reimbursement/paid use, and revenue conversion.",
    ),
    Round23ScoreTarget(
        "TELECOM_5G_6G_AI_NETWORK",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round23ScoreWeightDraft(16, 18, 10, 12, 10, 3, 5),
        ("confirmed_network_or_idc_capex", "equipment_order", "arpu_or_idc_revenue", "security_reliability"),
        ("generation_upgrade_theme_only", "capex_burden", "security_breach", "no_revenue_conversion"),
        ("network_generation_theme_priced", "capex_peak"),
        ("capex_cut", "security_breach", "arpu_decline", "equipment_order_cancellation"),
        "Telecom/5G/6G is Watch-first; AI data-center revenue or equipment orders must be visible before scoring rises.",
    ),
    Round23ScoreTarget(
        "MEDIA_AD_CONTENT_CYCLE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.GAME_CONTENT_IP,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round23ScoreWeightDraft(18, 16, 6, 14, 12, 0, 5),
        ("repeat_ip_monetization", "global_tour_or_distribution", "subscription_or_arpu", "opm_improvement"),
        ("hit_driven", "ad_cycle_down", "single_artist_contract_risk", "broadcast_ad_decline"),
        ("ip_success_fully_priced", "fan_platform_crowding"),
        ("artist_contract_break", "new_release_failure", "ad_recession", "platform_distribution_loss"),
        "Media/content is Watch-first. Repeat IP monetization can score; comeback or hit expectations alone cannot.",
    ),
    Round23ScoreTarget(
        "SERVICE_KIOSK_AUTOMATION",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.ROBOTICS_FACTORY_AUTOMATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round23ScoreWeightDraft(18, 17, 7, 13, 11, 0, 5),
        ("installed_base", "maintenance_or_saas_revenue", "payment_fee_revenue", "customer_cost_saving", "opm_improvement"),
        ("one_off_hardware_sales", "minimum_wage_theme_only", "margin_competition", "no_maintenance_revenue"),
        ("automation_theme_priced", "hardware_order_peak"),
        ("customer_churn", "price_competition", "maintenance_attach_rate_down", "order_cancellation"),
        "Service automation is more practical than humanoid robotics, but Green needs recurring maintenance, SaaS, or payment revenue.",
    ),
    Round23ScoreTarget(
        "SMART_FARM_AGRI_TECH",
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        E2RArchetype.ROBOTICS_FACTORY_AUTOMATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round23ScoreWeightDraft(18, 14, 12, 9, 9, 0, 5),
        ("export_order", "recurring_service", "overseas_sales", "opm_improvement"),
        ("commodity_cycle", "subsidy_only", "weather_event", "feed_cost_pressure", "policy_theme_only"),
        ("food_security_theme_priced", "grain_price_peak"),
        ("order_failure", "commodity_price_reversal", "subsidy_cut", "weather_normalization"),
        "Smart farm/agri-tech is Watch-first; policy and crop-price themes need actual orders, recurring services, and margin evidence.",
    ),
    Round23ScoreTarget(
        "HOME_LIVING_APPLIANCE",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round23ScoreWeightDraft(17, 13, 6, 12, 10, 0, 5),
        ("export_growth", "premium_mix", "smart_home_subscription", "opm_improvement"),
        ("replacement_cycle_only", "birthrate", "inventory", "single_product_fad", "no_recurring_service"),
        ("consumer_export_theme_priced", "premium_brand_crowding"),
        ("inventory_build", "export_slowdown", "price_cut", "birthrate_tam_decline"),
        "Home/living goods are Green-restricted unless export, premiumization, or recurring services offset replacement-cycle and birthrate limits.",
    ),
    Round23ScoreTarget(
        "CONSUMER_REGULATED_PRODUCT",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round23ScoreWeightDraft(18, 14, 8, 12, 10, 0, 5),
        ("repeat_consumption", "distribution_network", "regulatory_stability", "brand_margin"),
        ("regulation_crackdown", "legal_uncertainty", "social_backlash", "license_expectation_only", "one_off_demand"),
        ("regulated_product_theme_priced", "policy_event_priced"),
        ("regulation_crackdown", "license_denial", "social_discount_expands", "demand_reversal"),
        "Regulated consumer products can have repeat demand, but legal and social risk keeps them Watch-first.",
    ),
    Round23ScoreTarget(
        "MEMORY_HBM_CAPACITY",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round23ScoreWeightDraft(24, 21, 19, 15, 12, 0, 5),
        ("hbm_demand", "dram_nand_price", "supply_discipline", "long_term_contract_or_prepayment", "multi_year_revision"),
        ("cycle_peak", "capex_reversal", "crowding", "memory_price_down", "customer_ai_capex_slowdown"),
        ("one_to_two_year_price_surge", "market_cap_multiple_saturation", "global_hardware_crowding", "capex_expansion_news"),
        ("memory_price_down", "supply_glut", "customer_capex_collapse", "revision_down"),
        "HBM is Green-possible, but large post-rerating price moves require explicit 4B-watch diagnostics.",
    ),
    Round23ScoreTarget(
        "AI_DATA_CENTER_INFRASTRUCTURE",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round23ScoreWeightDraft(22, 23, 20, 14, 12, 0, 5),
        ("confirmed_order", "data_center_capex_link", "power_cooling_server_bottleneck", "op_eps_revision"),
        ("ai_capex_expectation_only", "project_delay", "no_revenue_conversion", "customer_capex_cut"),
        ("ai_infra_narrative_crowded", "orders_fully_priced"),
        ("ai_capex_cut", "project_delay", "order_cancellation", "margin_damage"),
        "AI data-center infra is Green-possible only with orders, delivery, bottleneck evidence, and EPS revision.",
    ),
)


ROUND23_CASE_CANDIDATES: tuple[Round23CaseCandidate, ...] = (
    Round23CaseCandidate("lunit_mammography_ai_candidate", "DIGITAL_HEALTHCARE_AI", "328130", "루닛 mammography AI", "KR", "success_candidate", ("external_clinical_validation", "medical_imaging_ai"), ("subgroup_validation_gap", "no_reimbursement"), "Performance evidence is useful but not enough without reimbursement and revenue."),
    Round23CaseCandidate("medical_ai_no_reimbursement_counterexample", "DIGITAL_HEALTHCARE_AI", "MED_AI_NO_PAY", "의료AI_수가부재", "KR", "failed_rerating", ("ai_clinical_performance",), ("no_reimbursement", "no_paid_usage"), "No reimbursement blocks Green."),
    Round23CaseCandidate("ai_medical_overtrust_risk_counterexample", "DIGITAL_HEALTHCARE_AI", "MED_AI_TRUST", "의료AI_과신리스크", "US", "failed_rerating", ("medical_ai_response",), ("overtrust_risk", "liability_unclear"), "Overtrust/liability risk remains a RedTeam factor."),
    Round23CaseCandidate("hospital_workflow_ai_revenue_candidate", "DIGITAL_HEALTHCARE_AI", "HOSP_AI_REV", "병원워크플로우AI", "KR", "success_candidate", ("hospital_adoption", "paid_usage", "workflow_integration"), ("liability_unclear", "churn"), "Workflow AI can score only when paid use and adoption are real."),
    Round23CaseCandidate("sk_aws_ulsan_ai_datacenter_candidate", "TELECOM_5G_6G_AI_NETWORK", "017670", "SK/AWS 울산 AI 데이터센터", "KR", "success_candidate", ("confirmed_idc_capex", "ai_datacenter_project"), ("project_delay", "capex_burden"), "Telecom/data-center candidate; revenue conversion needs backfill."),
    Round23CaseCandidate("5g_capex_peak_counterexample", "TELECOM_5G_6G_AI_NETWORK", "5G_PEAK", "5G_CAPEX피크", "KR", "failed_rerating", ("network_generation_capex",), ("capex_peak", "equipment_order_slowdown"), "Network generation cycle can fade after CAPEX peak."),
    Round23CaseCandidate("6g_policy_no_revenue_watch", "TELECOM_5G_6G_AI_NETWORK", "6G_POLICY", "6G정책_무매출", "KR", "event_premium", ("6g_policy",), ("no_revenue_conversion", "policy_theme_only"), "6G policy is radar evidence, not score evidence."),
    Round23CaseCandidate("telecom_security_breach_4c", "TELECOM_5G_6G_AI_NETWORK", "TELCO_SEC_4C", "통신보안사고", "KR", "4c_thesis_break", ("telecom_recurring_revenue",), ("security_breach", "regulatory_risk"), "Security breach can break telecom trust thesis."),
    Round23CaseCandidate("hybe_global_tour_ip_monetization_candidate", "MEDIA_AD_CONTENT_CYCLE", "352820", "HYBE 글로벌투어 IP", "KR", "success_candidate", ("global_tour", "ip_monetization", "fan_platform"), ("artist_contract_risk", "hit_driven"), "K-pop IP candidate needs repeat monetization and contract risk controls."),
    Round23CaseCandidate("kpop_single_artist_contract_risk_counterexample", "MEDIA_AD_CONTENT_CYCLE", "KPOP_CONTRACT", "K-pop 단일아티스트계약리스크", "KR", "failed_rerating", ("single_artist_ip",), ("single_artist_contract_risk", "hit_driven"), "Single-artist dependence blocks Green."),
    Round23CaseCandidate("advertising_cycle_recovery_candidate", "MEDIA_AD_CONTENT_CYCLE", "AD_RECOVERY", "광고경기회복", "KR", "success_candidate", ("ad_cycle_recovery", "digital_ad_mix"), ("ad_cycle_down", "opm_pressure"), "Ad recovery needs OPM conversion."),
    Round23CaseCandidate("broadcast_ad_decline_counterexample", "MEDIA_AD_CONTENT_CYCLE", "BROADCAST_DECLINE", "방송광고둔화", "KR", "failed_rerating", ("broadcast_revenue",), ("broadcast_ad_decline", "platform_shift_failure"), "Broadcast ad decline caps rerating."),
    Round23CaseCandidate("kiosk_recurring_maintenance_candidate", "SERVICE_KIOSK_AUTOMATION", "KIOSK_MAINT", "키오스크유지보수", "KR", "success_candidate", ("installed_base", "maintenance_revenue"), ("hardware_margin_competition", "customer_churn"), "Kiosk success requires recurring maintenance economics."),
    Round23CaseCandidate("contact_center_ai_subscription_candidate", "SERVICE_KIOSK_AUTOMATION", "CONTACT_AI", "컨택센터AI구독", "KR", "success_candidate", ("saas_subscription", "customer_cost_saving"), ("churn", "ai_cost_overrun"), "Contact-center AI can score with subscription and margin."),
    Round23CaseCandidate("kiosk_hardware_oneoff_counterexample", "SERVICE_KIOSK_AUTOMATION", "KIOSK_ONEOFF", "키오스크일회성장비", "KR", "failed_rerating", ("hardware_sales",), ("one_off_hardware_sales", "no_maintenance_revenue"), "One-off hardware sales do not create Green."),
    Round23CaseCandidate("unmanned_store_no_margin_counterexample", "SERVICE_KIOSK_AUTOMATION", "UNMANNED_NO_MARGIN", "무인점포_마진부재", "KR", "failed_rerating", ("unmanned_store_installation",), ("no_margin", "no_recurring_fee"), "Deployment count without margin is insufficient."),
    Round23CaseCandidate("smart_farm_export_order_candidate", "SMART_FARM_AGRI_TECH", "SMART_FARM_EXPORT", "스마트팜수출수주", "KR", "success_candidate", ("export_order", "operation_contract"), ("subsidy_dependency", "project_delay"), "Smart farm needs actual export or operating contract."),
    Round23CaseCandidate("agri_machinery_overseas_sales_candidate", "SMART_FARM_AGRI_TECH", "AGRI_MACHINERY", "농기계해외판매", "KR", "success_candidate", ("overseas_sales", "parts_service_revenue"), ("commodity_cycle", "dealer_inventory"), "Agri machinery can score through overseas and service revenue."),
    Round23CaseCandidate("soybean_feed_cost_pressure_counterexample", "SMART_FARM_AGRI_TECH", "FEED_COST", "대두사료원가압박", "KR", "failed_rerating", ("feed_cost",), ("commodity_cycle", "margin_pressure"), "Feed/soybean pressure is a cost risk, not Green evidence."),
    Round23CaseCandidate("weather_event_agri_theme_counterexample", "SMART_FARM_AGRI_TECH", "WEATHER_AGRI", "날씨이벤트농업테마", "KR", "event_premium", ("weather_event",), ("weather_event", "one_off_demand"), "Weather event demand stays event/watch."),
    Round23CaseCandidate("premium_home_appliance_export_candidate", "HOME_LIVING_APPLIANCE", "HOME_PREMIUM_EXPORT", "프리미엄생활가전수출", "KR", "success_candidate", ("export_growth", "premium_mix"), ("inventory", "replacement_cycle_only"), "Home appliance needs export and premium mix."),
    Round23CaseCandidate("smart_home_subscription_candidate", "HOME_LIVING_APPLIANCE", "SMART_HOME_SUB", "스마트홈구독", "KR", "success_candidate", ("smart_home_subscription", "platform_lock_in"), ("no_recurring_service", "churn"), "Smart-home needs recurring service, not device theme."),
    Round23CaseCandidate("low_birthrate_kids_goods_counterexample", "HOME_LIVING_APPLIANCE", "KIDS_GOODS_BIRTH", "유아용품저출산", "KR", "failed_rerating", ("kids_goods",), ("birthrate", "tam_decline"), "Kids goods need export/premiumization to offset low birthrate."),
    Round23CaseCandidate("single_product_home_appliance_counterexample", "HOME_LIVING_APPLIANCE", "HOME_SINGLE_PRODUCT", "단일생활가전유행", "KR", "failed_rerating", ("single_product_sales",), ("single_product_fad", "inventory"), "Single-product fad remains Watch."),
    Round23CaseCandidate("e_cigarette_repeat_consumption_candidate", "CONSUMER_REGULATED_PRODUCT", "ECIG_REPEAT", "전자담배반복소비", "KR", "success_candidate", ("repeat_consumption", "distribution_network"), ("regulation_crackdown", "social_backlash"), "Regulated repeat consumption needs stable rules."),
    Round23CaseCandidate("cannabis_regulation_event_watch", "CONSUMER_REGULATED_PRODUCT", "CANNABIS_EVENT", "마리화나규제이벤트", "KR", "event_premium", ("license_expectation",), ("legal_uncertainty", "license_expectation_only"), "Cannabis-like themes are event/watch under KR constraints."),
    Round23CaseCandidate("regulation_crackdown_4c", "CONSUMER_REGULATED_PRODUCT", "REG_CRACKDOWN_4C", "규제강화4C", "KR", "4c_thesis_break", ("regulated_product_revenue",), ("regulation_crackdown", "license_denial"), "Regulatory crackdown can break repeat consumption thesis."),
    Round23CaseCandidate("alcohol_tobacco_social_discount_counterexample", "CONSUMER_REGULATED_PRODUCT", "SOCIAL_DISCOUNT", "주류담배사회적할인", "KR", "failed_rerating", ("repeat_consumption",), ("social_backlash", "valuation_discount"), "Repeat demand can still be capped by social/regulatory discount."),
)


def target_for(target_id: str) -> Round23ScoreTarget | None:
    for target in ROUND23_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round23_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND23_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_dict()
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market=candidate.market,
            sector_raw=candidate.target_id,
            primary_archetype=target.canonical_archetype,
            expected_group=candidate.expected_group,
            large_sector=target.large_sector.value,
            case_type=candidate.case_type,
            evidence_summary=(
                f"Round23 v0.8 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4b_evidence=candidate.evidence_fields if candidate.case_type == "4b_watch" else (),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"success_candidate", "structural_success"} else None,
            score_price_alignment="unknown",
            rerating_result="event_premium" if candidate.case_type == "event_premium" else "unknown",
            price_pattern="unknown",
            score_weight_hint={
                "eps_fcf": float(weights["eps_fcf"]),
                "visibility": float(weights["structural_visibility"]),
                "bottleneck": float(weights["bottleneck_pricing"]),
                "mispricing": float(weights["market_mispricing"]),
                "valuation": float(weights["valuation"]),
                "capital_allocation": float(weights["capital_allocation"]),
                "information_confidence": float(weights["information_confidence"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                *target.red_flags,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status="needs_price_backfill"),
            data_quality=CaseDataQuality(False, False, False, 0.0),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round23_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND23_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf": str(weights["eps_fcf"]),
                "structural_visibility": str(weights["structural_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "market_mispricing": str(weights["market_mispricing"]),
                "valuation": str(weights["valuation"]),
                "capital_allocation": str(weights["capital_allocation"]),
                "information_confidence": str(weights["information_confidence"]),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round23_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND23_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        assert target is not None
        rows.append(
            {
                "case_id": candidate.case_id,
                "target_id": candidate.target_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "market": candidate.market,
                "case_type": candidate.case_type,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "price_validation_status": "needs_price_backfill",
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round23_summary() -> dict[str, int | bool]:
    records = round23_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success"})
    return {
        "target_count": len(ROUND23_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "green_possible_count": sum(1 for target in ROUND23_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND23_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round23_score_weight_reports(
    *,
    output_directory: str | Path = ROUND23_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND23_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND23_DEFAULT_SCORE_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = Path(cases_path)
    score_profiles = Path(score_profile_path)
    cases.parent.mkdir(parents=True, exist_ok=True)
    score_profiles.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "score_profiles": score_profiles,
        "summary": output / "round23_score_weight_v08_summary.md",
        "case_matrix": output / "round23_case_candidate_matrix.csv",
        "green_guardrails": output / "round23_green_guardrail_review.md",
        "price_validation_plan": output / "round23_price_validation_plan.md",
        "stage4b_watch_review": output / "round23_stage4b_watch_review.md",
    }
    _write_case_jsonl(round23_case_records(), cases)
    _write_rows(round23_score_profile_rows(), score_profiles)
    _write_rows(round23_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round23_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round23_green_guardrail_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round23_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_watch_review"].write_text(render_round23_stage4b_watch_markdown(), encoding="utf-8")
    return paths


def render_round23_summary_markdown() -> str:
    summary = round23_summary()
    lines = [
        "# Round-23 Score-Weight v0.8 Summary",
        "",
        f"- source_round: `{ROUND23_SOURCE_ROUND_PATH}`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- counterexample_or_risk_count: {summary['counterexample_or_risk_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "- Round 23 expands v0.8 calibration, not production scoring.",
        "- Example: 의료AI needs clearance, hospital adoption, reimbursement or paid use, and revenue conversion.",
        "- Example: 6G policy is useful for search routing, but cannot become Green without revenue or equipment orders.",
        "- Example: HBM can be structural, but big post-rerating price moves require 4B-watch diagnostics.",
        "- Theme names, case IDs, papers, PoCs, and policy headlines are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round23_green_guardrail_markdown() -> str:
    lines = [
        "# Round-23 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND23_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v0.8 weights to production scoring yet.",
            "- Do not score papers, policy plans, PoCs, or theme labels without revenue/usage/order evidence.",
            "- Do not invent stage dates, prices, AUC, reimbursement, paid usage, ARR, FCF, or contract values.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round23_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-23 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep reference, policy, and synthetic counterexample cases as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before production scoring changes.",
            "",
            "## Priority Validation",
            "- Medical AI: clinical proof versus reimbursement and paid usage.",
            "- Telecom/6G: CAPEX theme versus actual orders/revenue.",
            "- Media/content: repeat IP monetization versus hit-driven risk.",
            "- HBM/data-center: structural EPS evidence versus 4B crowding.",
        ]
    ) + "\n"


def render_round23_stage4b_watch_markdown() -> str:
    hbm = target_for("MEMORY_HBM_CAPACITY")
    ai_dc = target_for("AI_DATA_CENTER_INFRASTRUCTURE")
    lines = [
        "# Round-23 4B Watch Review",
        "",
        "Round 23 keeps Green strict while strengthening post-rerating monitoring.",
        "",
        "## MEMORY_HBM_CAPACITY",
    ]
    if hbm:
        lines.extend(f"- {item}" for item in hbm.stage4b_conditions)
    lines.append("")
    lines.append("## AI_DATA_CENTER_INFRASTRUCTURE")
    if ai_dc:
        lines.extend(f"- {item}" for item in ai_dc.stage4b_conditions)
    lines.extend(
        [
            "",
            "## Rule",
            "- Price-only warning remains `price_only_4b_watch`, not full evidence-based 4B.",
            "- Full 4B requires crowding, saturation, order slowdown, revision slowdown, capex reversal, or other deterioration evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    lines = []
    for record in records:
        record.validate()
        lines.append(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    row_tuple = tuple(rows)
    if not row_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(row_tuple[0].keys()))
        writer.writeheader()
        for row in row_tuple:
            writer.writerow(row)
    return path


__all__ = [
    "ROUND23_CASE_CANDIDATES",
    "ROUND23_DEFAULT_CASES_PATH",
    "ROUND23_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND23_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND23_SCORE_TARGETS",
    "ROUND23_SOURCE_ROUND_PATH",
    "Round23CaseCandidate",
    "Round23ScoreTarget",
    "Round23ScoreWeightDraft",
    "render_round23_green_guardrail_markdown",
    "render_round23_price_validation_plan_markdown",
    "render_round23_stage4b_watch_markdown",
    "render_round23_summary_markdown",
    "round23_case_candidate_rows",
    "round23_case_records",
    "round23_score_profile_rows",
    "round23_summary",
    "target_for",
    "write_round23_score_weight_reports",
]
