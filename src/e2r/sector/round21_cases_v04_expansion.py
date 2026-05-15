"""Round-21 cases_v04 expansion and v0.6 score-weight hypotheses.

Round 21 turns the analyst's thin-archetype notes into calibration artifacts:
case-mining candidates, score-weight drafts, and guardrail reports. It is
report-only. Production feature engineering, scoring, staging, and RedTeam code
must not import this module.
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


ROUND21_SOURCE_ROUND_PATH = "docs/round/round_21.md"
ROUND21_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round21_cases_v04"
ROUND21_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v04_round21.jsonl"
ROUND21_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round21_v06.csv"


@dataclass(frozen=True)
class Round21ScoreWeightDraft:
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
class Round21ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round21ScoreWeightDraft
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    normalization_point: str

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round21CaseCandidate:
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


ROUND21_SCORE_TARGETS: tuple[Round21ScoreTarget, ...] = (
    Round21ScoreTarget(
        "RAIL_INFRASTRUCTURE",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round21ScoreWeightDraft(20, 23, 12, 14, 12, 1, 5),
        ("contract_to_sales", "delivery_schedule", "project_margin", "fy1_fy2_op_revision", "backlog_reflection"),
        ("project_delay", "margin_uncertainty", "policy_theme_only", "mou_without_order"),
        "Rail resembles backlog industrial, but project margin and delivery risk must be heavier than power equipment.",
    ),
    Round21ScoreTarget(
        "AI_DATA_CENTER_COOLING",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round21ScoreWeightDraft(21, 22, 22, 13, 12, 0, 5),
        ("data_center_capex_link", "confirmed_order", "cooling_bottleneck", "service_repeat_revenue", "fy1_fy2_op_revision"),
        ("liquid_cooling_theme_only", "ai_capex_delay", "no_customer", "low_margin_installation"),
        "AI cooling can be structural, but only when orders, customers, delivery, and service economics are visible.",
    ),
    Round21ScoreTarget(
        "WASTE_RECYCLING_ENVIRONMENT",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round21ScoreWeightDraft(18, 22, 15, 13, 12, 3, 5),
        ("permits_or_entry_barrier", "processing_volume", "utilization", "long_term_contract", "repeat_fcf"),
        ("low_utilization", "commodity_price_margin", "capex_without_fcf", "policy_theme_only"),
        "Waste treatment can be infrastructure-like E2R; recycling themes need actual volume and FCF.",
    ),
    Round21ScoreTarget(
        "CLOUD_AI_SOFTWARE_INFRA",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round21ScoreWeightDraft(20, 23, 8, 16, 14, 0, 5),
        ("recurring_revenue", "arpu", "opm_improvement", "customer_lock_in", "fcf_conversion"),
        ("ai_feature_only", "ai_cost_overrun", "churn", "si_revenue_only"),
        "Cloud/SaaS needs recurring revenue, margin, and FCF; AI keywords are routing only.",
    ),
    Round21ScoreTarget(
        "SECURITY_IDENTITY_DEEPFAKE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round21ScoreWeightDraft(20, 20, 10, 14, 13, 0, 5),
        ("recurring_subscription", "low_churn", "customer_diversification", "opm_improvement", "operational_trust"),
        ("large_outage", "lawsuit", "trust_break", "no_recurring_revenue", "security_theme_only"),
        "Security demand can be structural, but an outage or trust break is a hard 4C-style guardrail.",
    ),
    Round21ScoreTarget(
        "CRO_CLINICAL_SERVICE",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round21ScoreWeightDraft(18, 20, 8, 12, 12, 0, 5),
        ("service_backlog", "customer_diversification", "repeat_clinical_service_revenue", "opm_improvement", "funding_cycle_stable"),
        ("biotech_funding_crunch", "customer_budget_cut", "customer_concentration", "clinical_trial_cut"),
        "CRO is weaker than CDMO; funding cycle and customer budgets decide whether it can move beyond Watch.",
    ),
    Round21ScoreTarget(
        "APPAREL_BRAND_OEM",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.EXPORT_RECURRING_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round21ScoreWeightDraft(18, 16, 8, 14, 12, 0, 5),
        ("overseas_channel_expansion", "inventory_turnover", "low_discount_rate", "opm_improvement", "repeat_orders"),
        ("inventory_build", "markdown", "fashion_cycle", "channel_concentration"),
        "Apparel is more conservative than K-food/K-beauty; inventory and markdown are core red flags.",
    ),
    Round21ScoreTarget(
        "BUILDING_MATERIALS_REIT",
        Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS,
        E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round21ScoreWeightDraft(17, 12, 12, 12, 12, 5, 5),
        ("cost_stability", "price_pass_through", "volume_recovery", "pf_risk_low", "dividend_or_fcf_stability"),
        ("pf_stress", "rates_up", "vacancy_up", "liquidity_support_only", "dividend_cut"),
        "Building materials and REITs stay rate/PF sensitive; relief rallies are not structural evidence.",
    ),
    Round21ScoreTarget(
        "CDMO_HEALTHCARE_CONTRACT",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round21ScoreWeightDraft(20, 24, 12, 12, 12, 0, 5),
        ("multi_year_production_visibility", "capacity_utilization", "customer_diversification", "long_term_contract", "fcf_conversion"),
        ("capacity_overbuild", "underutilization", "contract_delay", "litigation", "customer_concentration"),
        "CDMO is contract and utilization driven; capacity without utilization is not Green evidence.",
    ),
    Round21ScoreTarget(
        "RARE_METALS_STRATEGIC_MATERIALS",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round21ScoreWeightDraft(18, 16, 15, 16, 15, 10, 5),
        ("smelting_margin_or_fcf", "supply_chain_bottleneck", "capital_allocation_improvement", "governance_rerating"),
        ("event_premium_only", "commodity_price_only", "governance_dispute", "takeover_uncertainty"),
        "Strategic metals can rerate, but tender offers and control fights are event premium until FCF or governance change is proven.",
    ),
)


ROUND21_CASE_CANDIDATES: tuple[Round21CaseCandidate, ...] = (
    Round21CaseCandidate("hyundai_rotem_morocco_rail_order_success_candidate", "RAIL_INFRASTRUCTURE", "064350", "현대로템", "KR", "success_candidate", ("confirmed_contract", "delivery_schedule", "contract_to_sales"), ("project_delay", "margin_uncertainty"), "Morocco rail order candidate; price and stage dates need backfill."),
    Round21CaseCandidate("rail_policy_no_contract_counterexample", "RAIL_INFRASTRUCTURE", "RAIL_POLICY", "철도정책_무계약", "KR", "failed_rerating", ("rail_policy_headline",), ("mou_without_order", "policy_theme_only"), "Policy headline without binding order should stay Watch."),
    Round21CaseCandidate("reconstruction_rail_theme_event_watch", "RAIL_INFRASTRUCTURE", "RAIL_RECON", "재건철도테마", "KR", "event_premium", ("reconstruction_theme",), ("no_confirmed_contract", "project_financing_delay"), "Reconstruction rail theme is event premium until order evidence appears."),
    Round21CaseCandidate("ecolab_coolit_ai_liquid_cooling_candidate", "AI_DATA_CENTER_COOLING", "ECL", "Ecolab/CoolIT", "US", "success_candidate", ("ai_data_center_capex", "cooling_bottleneck", "confirmed_deal"), ("integration_risk", "ai_capex_delay"), "AI liquid cooling reference candidate; not a KR production input."),
    Round21CaseCandidate("samsung_flaktgroup_hvac_candidate", "AI_DATA_CENTER_COOLING", "005930", "삼성전자 FlaktGroup", "KR", "success_candidate", ("ai_data_center_cooling", "hvac_capacity", "strategic_acquisition"), ("project_margin", "integration_risk"), "Cooling/HVAC strategic capacity candidate; operating evidence needs backfill."),
    Round21CaseCandidate("liquid_cooling_theme_no_order_counterexample", "AI_DATA_CENTER_COOLING", "COOL_THEME", "액침냉각테마_무수주", "KR", "failed_rerating", ("liquid_cooling_keyword",), ("no_customer", "no_order", "theme_only"), "Theme tag alone cannot create score."),
    Round21CaseCandidate("ai_capex_delay_cooling_4c", "AI_DATA_CENTER_COOLING", "COOL_4C", "AI냉각_CAPEX지연", "US", "4c_thesis_break", ("project_delay",), ("ai_capex_cut", "customer_cancellation"), "Cooling demand breaks if hyperscaler CAPEX is delayed or cut."),
    Round21CaseCandidate("eqt_kj_environment_waste_platform_candidate", "WASTE_RECYCLING_ENVIRONMENT", "KJ_ENV", "KJ Environment", "KR", "success_candidate", ("waste_platform", "permitted_facility", "processing_coverage"), ("capex_burden", "utilization_down"), "Waste platform candidate; private deal evidence needs conversion to case fixture."),
    Round21CaseCandidate("recycling_capacity_low_utilization_counterexample", "WASTE_RECYCLING_ENVIRONMENT", "RECYCLE_LOW_UTIL", "재활용설비_저가동률", "KR", "failed_rerating", ("recycling_capacity",), ("low_utilization", "capex_without_fcf"), "Capacity without utilization should not become Green."),
    Round21CaseCandidate("battery_recycling_no_volume_counterexample", "WASTE_RECYCLING_ENVIRONMENT", "BAT_REC_NO_VOL", "폐배터리_물량부족", "KR", "failed_rerating", ("battery_recycling_theme",), ("no_processing_volume", "commodity_price_dependency"), "Battery recycling theme needs actual volume."),
    Round21CaseCandidate("waste_capex_burden_4c", "WASTE_RECYCLING_ENVIRONMENT", "WASTE_CAPEX_4C", "폐기물_CAPEX부담", "KR", "4c_thesis_break", ("capex_expansion",), ("fcf_negative_after_capex", "low_utilization"), "FCF deterioration after CAPEX is a thesis-break candidate."),
    Round21CaseCandidate("douzone_bizon_cloud_erp_candidate", "CLOUD_AI_SOFTWARE_INFRA", "012510", "더존비즈온", "KR", "success_candidate", ("cloud_erp", "smb_lock_in", "recurring_revenue"), ("ai_cost_overrun", "churn"), "Cloud ERP recurring revenue candidate; margin/FCF evidence needs backfill."),
    Round21CaseCandidate("ai_feature_no_fcf_counterexample", "CLOUD_AI_SOFTWARE_INFRA", "AI_SW_NO_FCF", "AI기능_무현금흐름", "KR", "failed_rerating", ("ai_feature_launch",), ("no_paid_usage", "no_fcf"), "AI feature without paid usage is not structural evidence."),
    Round21CaseCandidate("cloud_cost_margin_pressure_4c", "CLOUD_AI_SOFTWARE_INFRA", "CLOUD_MARGIN_4C", "클라우드비용_마진압박", "KR", "4c_thesis_break", ("cloud_growth",), ("ai_cost_overrun", "opm_decline"), "Revenue growth with margin damage can break the thesis."),
    Round21CaseCandidate("churn_saas_counterexample", "CLOUD_AI_SOFTWARE_INFRA", "SAAS_CHURN", "SaaS_Churn", "US", "failed_rerating", ("subscription_revenue",), ("churn", "retention_down"), "Subscription label needs retention evidence."),
    Round21CaseCandidate("recurring_security_subscription_candidate", "SECURITY_IDENTITY_DEEPFAKE", "SEC_ARR", "반복보안구독", "KR", "success_candidate", ("recurring_subscription", "customer_diversification"), ("trust_break", "churn"), "Security candidate only if ARR and retention are shown."),
    Round21CaseCandidate("crowdstrike_outage_4c_counterexample", "SECURITY_IDENTITY_DEEPFAKE", "CRWD", "CrowdStrike outage", "US", "4c_thesis_break", ("security_subscription",), ("large_outage", "lawsuit", "trust_damage"), "Operational trust break is hard 4C-style evidence."),
    Round21CaseCandidate("deepfake_regulation_stage1_candidate", "SECURITY_IDENTITY_DEEPFAKE", "DEEPFAKE_REG", "딥페이크규제", "KR", "event_premium", ("deepfake_regulation",), ("no_contract", "regulation_headline_only"), "Regulation can route search but does not score without contracts."),
    Round21CaseCandidate("security_theme_no_contract_counterexample", "SECURITY_IDENTITY_DEEPFAKE", "SEC_THEME", "보안테마_무계약", "KR", "failed_rerating", ("security_keyword",), ("no_contract", "no_recurring_revenue"), "Theme-only security should stay below Green."),
    Round21CaseCandidate("iqvia_clinical_data_scale_candidate", "CRO_CLINICAL_SERVICE", "IQV", "IQVIA", "US", "success_candidate", ("clinical_service_scale", "healthcare_data", "guidance_revision"), ("funding_cycle", "customer_budget_cut"), "CRO scale reference; not a production scoring input."),
    Round21CaseCandidate("icon_global_cro_scale_candidate", "CRO_CLINICAL_SERVICE", "ICLR", "ICON", "US", "success_candidate", ("global_cro_scale", "clinical_service_revenue"), ("funding_cycle", "customer_concentration"), "Global CRO scale candidate; price validation needed."),
    Round21CaseCandidate("charles_river_biotech_funding_crunch_4c", "CRO_CLINICAL_SERVICE", "CRL", "Charles River funding crunch", "US", "4c_thesis_break", ("biotech_service_revenue",), ("biotech_funding_crunch", "forecast_cut"), "Funding crunch can turn CRO-like service visibility into 4C."),
    Round21CaseCandidate("cro_customer_budget_cut_counterexample", "CRO_CLINICAL_SERVICE", "CRO_BUDGET_CUT", "CRO고객예산축소", "US", "failed_rerating", ("clinical_volume",), ("customer_budget_cut", "volume_without_margin"), "Clinical volume is insufficient if budgets and margin decline."),
    Round21CaseCandidate("inditex_inventory_speed_reference_success", "APPAREL_BRAND_OEM", "ITX", "Inditex", "ES", "success_candidate", ("inventory_speed", "channel_response", "brand_scale"), ("fashion_cycle", "markdown"), "Inventory speed is a positive apparel reference; local evidence still required."),
    Round21CaseCandidate("shein_fast_fashion_efficiency_reference", "APPAREL_BRAND_OEM", "SHEIN", "Shein", "CN", "success_candidate", ("fast_inventory_model", "dtc_scale"), ("regulatory_labor_risk", "tariff"), "Fast fashion efficiency reference with major red flags."),
    Round21CaseCandidate("forever21_fast_fashion_bankruptcy_4c", "APPAREL_BRAND_OEM", "FOREVER21", "Forever 21", "US", "4c_thesis_break", ("fast_fashion_brand",), ("inventory_failure", "channel_adaptation_failure"), "Bankruptcy-style channel/inventory failure is 4C evidence."),
    Round21CaseCandidate("apparel_inventory_markdown_counterexample", "APPAREL_BRAND_OEM", "APPAREL_MARKDOWN", "의류재고할인", "KR", "failed_rerating", ("sales_growth",), ("inventory_build", "markdown"), "Sales growth without inventory discipline is not structural."),
    Round21CaseCandidate("cement_price_hike_candidate", "BUILDING_MATERIALS_REIT", "CEMENT_PRICE", "시멘트가격인상", "KR", "success_candidate", ("price_hike", "cost_stability"), ("volume_decline", "pf_stress"), "Cement price hike candidate needs volume and margin confirmation."),
    Round21CaseCandidate("reit_rate_cut_dividend_candidate", "BUILDING_MATERIALS_REIT", "REIT_DIV", "리츠금리하락배당", "KR", "success_candidate", ("rate_down", "dividend_coverage", "occupancy"), ("refinancing_stress", "vacancy_up"), "REIT candidate needs occupancy and dividend coverage."),
    Round21CaseCandidate("korea_pf_delinquency_4c", "BUILDING_MATERIALS_REIT", "KR_PF_4C", "한국PF연체", "KR", "4c_thesis_break", ("pf_exposure",), ("pf_stress", "credit_risk"), "PF stress is a red-team-first condition."),
    Round21CaseCandidate("builder_liquidity_support_relief_rally_counterexample", "BUILDING_MATERIALS_REIT", "BUILDER_RELIEF", "건설유동성지원랠리", "KR", "event_premium", ("liquidity_support",), ("relief_rally_only", "credit_risk_remaining"), "Liquidity support can create relief rally but not structural Green."),
    Round21CaseCandidate("samsung_biologics_us_capacity_candidate", "CDMO_HEALTHCARE_CONTRACT", "207940", "삼성바이오로직스", "KR", "success_candidate", ("us_capacity", "drug_substance_capacity", "customer_diversification"), ("underutilization", "customer_concentration"), "CDMO capacity candidate; utilization and FCF evidence needed."),
    Round21CaseCandidate("celltrion_biosimilar_candidate", "CDMO_HEALTHCARE_CONTRACT", "068270", "셀트리온", "KR", "success_candidate", ("biosimilar_revenue", "production_scale"), ("litigation", "price_competition"), "Biosimilar/CDMO adjacent candidate; contract and margin evidence needed."),
    Round21CaseCandidate("cdmo_capacity_underutilization_4c", "CDMO_HEALTHCARE_CONTRACT", "CDMO_UNDERUTIL", "CDMO가동률부족", "KR", "4c_thesis_break", ("capacity_expansion",), ("underutilization", "fcf_damage"), "Capacity without utilization is not Green and can become 4C."),
    Round21CaseCandidate("cdmo_patent_litigation_delay_4c", "CDMO_HEALTHCARE_CONTRACT", "CDMO_LITIGATION", "CDMO특허소송지연", "KR", "4c_thesis_break", ("production_plan",), ("litigation", "contract_delay"), "Patent/litigation delay can break production visibility."),
    Round21CaseCandidate("korea_zinc_tender_event_premium", "RARE_METALS_STRATEGIC_MATERIALS", "010130", "고려아연 공개매수", "KR", "event_premium", ("tender_offer", "control_premium"), ("event_premium_only", "takeover_uncertainty"), "Tender premium must be separated from structural FCF rerating."),
    Round21CaseCandidate("korea_zinc_strategic_materials_candidate", "RARE_METALS_STRATEGIC_MATERIALS", "010130", "고려아연 전략금속", "KR", "success_candidate", ("strategic_materials", "smelting_margin", "supply_chain_value"), ("commodity_price_reversal", "governance_dispute"), "Strategic materials candidate requires FCF and governance evidence."),
    Round21CaseCandidate("korea_zinc_share_issue_governance_risk_4c", "RARE_METALS_STRATEGIC_MATERIALS", "010130", "고려아연 신주발행 리스크", "KR", "4c_thesis_break", ("governance_event",), ("share_issue_dispute", "trust_break"), "Governance deterioration can become thesis-break evidence."),
    Round21CaseCandidate("pure_metal_price_cycle_counterexample", "RARE_METALS_STRATEGIC_MATERIALS", "METAL_CYCLE", "순수금속가격사이클", "KR", "failed_rerating", ("metal_price",), ("commodity_price_only", "no_fcf_evidence"), "Metal price alone is cyclical, not structural Green."),
)


def target_for(target_id: str) -> Round21ScoreTarget | None:
    for target in ROUND21_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round21_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND21_CASE_CANDIDATES:
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
                f"Round21 cases_v04 mining candidate for {candidate.target_id}; "
                "stage dates, prices, and source-backed numbers remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type != "success_candidate" else None,
            score_price_alignment="unknown",
            rerating_result="event_premium" if candidate.case_type == "event_premium" else "unknown",
            price_pattern="unknown",
            score_weight_hint={
                "eps_fcf": float(weights["eps_fcf"]),
                "visibility": float(weights["structural_visibility"]),
                "bottleneck": float(weights["bottleneck_pricing"]),
                "mispricing": float(weights["market_mispricing"]),
                "valuation": float(weights["valuation"]),
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


def round21_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND21_SCORE_TARGETS:
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
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round21_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND21_CASE_CANDIDATES:
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


def round21_summary() -> dict[str, int | bool]:
    targets = ROUND21_SCORE_TARGETS
    records = round21_case_records()
    positive = sum(1 for record in records if record.case_type == "success_candidate")
    risk = len(records) - positive
    return {
        "target_count": len(targets),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": risk,
        "green_possible_count": sum(1 for target in targets if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in targets if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round21_case_expansion_reports(
    *,
    output_directory: str | Path = ROUND21_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND21_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND21_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round21_cases_v04_summary.md",
        "case_matrix": output / "round21_case_candidate_matrix.csv",
        "green_guardrails": output / "round21_green_guardrail_review.md",
        "price_validation_plan": output / "round21_price_validation_plan.md",
    }
    _write_case_jsonl(round21_case_records(), cases)
    _write_rows(round21_score_profile_rows(), score_profiles)
    _write_rows(round21_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round21_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round21_green_guardrail_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round21_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round21_summary_markdown() -> str:
    summary = round21_summary()
    lines = [
        "# Round-21 cases_v04 Expansion Summary",
        "",
        f"- source_round: `{ROUND21_SOURCE_ROUND_PATH}`",
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
        "- Round 21 expands the calibration pack, not production scoring.",
        "- Example: `현대로템 모로코 철도 수주` is a case-mining candidate, but Stage dates and prices stay empty until backfill.",
        "- Example: `CrowdStrike outage` is a security counterexample; repeated revenue does not protect a broken trust thesis.",
        "- Theme names and case IDs must never become score evidence.",
    ]
    return "\n".join(lines) + "\n"


def render_round21_green_guardrail_markdown() -> str:
    lines = [
        "# Round-21 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND21_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply these v0.6 weights to production scoring yet.",
            "- Do not turn event premium, policy relief, or theme tags into Stage 3-Green.",
            "- Do not invent stage dates, prices, utilization, ARR, FCF, contract size, or margins.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round21_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-21 Price Validation Plan",
        "",
        "1. Backfill official price paths for every `cases_v04_round21` record where a tradable symbol exists.",
        "2. Keep private/reference cases as `missing_price_data` or `needs_price_backfill` until usable data exists.",
        "3. Calculate stage price, peak price, MFE/MAE, and drawdown only from source data.",
        "4. Compare shadow score weight hypotheses against price-path and EPS/FCF evidence.",
        "5. Promote no weight to production until the archetype has enough success and counterexample coverage.",
        "",
        "## Priority Checks",
        "- AI cooling: real customers/orders versus cooling theme only.",
        "- Waste/recycling: processing volume and FCF versus capacity theme.",
        "- CDMO: utilization and customer diversification versus capacity overbuild.",
        "- Rare metals: FCF/governance rerating versus tender-offer event premium.",
    ]
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
    "ROUND21_CASE_CANDIDATES",
    "ROUND21_DEFAULT_CASES_PATH",
    "ROUND21_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND21_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND21_SCORE_TARGETS",
    "ROUND21_SOURCE_ROUND_PATH",
    "Round21CaseCandidate",
    "Round21ScoreTarget",
    "Round21ScoreWeightDraft",
    "render_round21_green_guardrail_markdown",
    "render_round21_price_validation_plan_markdown",
    "render_round21_summary_markdown",
    "round21_case_candidate_rows",
    "round21_case_records",
    "round21_score_profile_rows",
    "round21_summary",
    "target_for",
    "write_round21_case_expansion_reports",
]
