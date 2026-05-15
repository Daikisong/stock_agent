"""Round-20 score-weight v0.6 research matrix.

Round 20 adds thinner sub-archetypes to the calibration layer. It is still
report-only: theme tags route research and case mining, but production
FeatureEngineering, scoring, staging, and RedTeam code must not import this
module.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND20_SOURCE_ROUND_PATH = "docs/round/round_20.md"


@dataclass(frozen=True)
class Round20ScoreWeightDraft:
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
class Round20ScoreWeightTarget:
    sub_archetype: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    theme_tags: tuple[str, ...]
    score_weight: Round20ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    must_have_evidence: tuple[str, ...]
    red_flags: tuple[str, ...]
    success_candidates: tuple[str, ...]
    counterexamples: tuple[str, ...]
    normalization_point: str

    @property
    def theme_is_score_input(self) -> bool:
        return False

    @property
    def production_scoring_changed(self) -> bool:
        return False


ROUND20_SCORE_WEIGHT_TARGETS: tuple[Round20ScoreWeightTarget, ...] = (
    Round20ScoreWeightTarget(
        sub_archetype="RAIL_INFRASTRUCTURE",
        large_sector=Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        canonical_archetype=E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        theme_tags=("철도", "고속철 수출", "현대로템 철도", "대형 인프라", "우크라 재건 일부", "네옴시티 일부"),
        score_weight=Round20ScoreWeightDraft(20, 23, 12, 14, 12, 1, 5),
        stage1_signals=("rail_policy", "overseas_bid", "large_infra_news", "trading_value_spike"),
        stage2_signals=("confirmed_contract", "contract_to_sales", "delivery_schedule", "op_eps_revision_possible"),
        stage3_conditions=("multi_year_backlog", "margin_visible_delivery", "overseas_customer_diversification", "old_rail_discount_frame"),
        stage4b_conditions=("large_order_expectation_priced", "follow_on_order_gap", "valuation_normalized"),
        stage4c_conditions=("contract_cancellation", "delivery_delay", "cost_overrun", "project_financing_failure"),
        must_have_evidence=("confirmed_contract", "delivery_schedule", "contract_to_sales", "margin_visibility"),
        red_flags=("policy_theme_only", "project_financing_delay", "margin_uncertainty", "low_margin_order"),
        success_candidates=("hyundai_rotem_morocco_rail_order",),
        counterexamples=("rail_policy_only_theme", "reconstruction_theme_without_order"),
        normalization_point="Rail can reach Stage 2 with real orders, but policy/reconstruction headlines stay event-watch.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="AI_DATA_CENTER_COOLING",
        large_sector=Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        canonical_archetype=E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        posture=Round10ThemePosture.GREEN_POSSIBLE,
        theme_tags=("냉각시스템", "액침냉각", "HVAC", "AI 데이터센터", "클린룸", "서버 인프라"),
        score_weight=Round20ScoreWeightDraft(21, 22, 22, 13, 12, 0, 5),
        stage1_signals=("ai_server_heat_load", "cooling_demand", "hvac_keyword", "liquid_cooling_keyword"),
        stage2_signals=("confirmed_customer_order", "data_center_capex_link", "revenue_timing", "op_eps_revision"),
        stage3_conditions=("multi_year_data_center_capex", "cooling_bottleneck_position", "service_or_maintenance_repeat_revenue", "pricing_power"),
        stage4b_conditions=("ai_capex_narrative_overheated", "cooling_theme_group_rally", "equipment_capacity_overbuild"),
        stage4c_conditions=("data_center_project_delay", "ai_capex_cut", "margin_damage", "customer_cancellation"),
        must_have_evidence=("confirmed_customer_order", "data_center_capex_link", "revenue_conversion", "project_margin"),
        red_flags=("cooling_theme_only", "no_customer", "ai_capex_delay", "low_margin_installation"),
        success_candidates=("ecolab_coolit_ai_cooling", "samsung_flaktgroup_hvac"),
        counterexamples=("liquid_cooling_theme_no_order", "data_center_capex_delay"),
        normalization_point="Cooling is a real AI infra sub-archetype, but Green needs customer, order, delivery, and service economics.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="WASTE_RECYCLING_ENVIRONMENT",
        large_sector=Round10LargeSector.BATTERY_EV_GREEN,
        canonical_archetype=E2RArchetype.UTILITIES_REGULATED_TARIFF,
        posture=Round10ThemePosture.GREEN_POSSIBLE,
        theme_tags=("폐기물처리", "재활용", "폐배터리", "탈 플라스틱", "플라스틱 재활용", "폐기물 에너지화"),
        score_weight=Round20ScoreWeightDraft(18, 22, 15, 13, 12, 0, 5),
        stage1_signals=("waste_regulation", "recycling_facility", "battery_recycling_news", "plastic_recycling_news"),
        stage2_signals=("processing_volume_growth", "long_term_contract", "utilization_up", "op_fcf_improvement"),
        stage3_conditions=("permitted_facility_bottleneck", "repeat_fcf", "customer_diversification", "esg_theme_frame_still_used"),
        stage4b_conditions=("esg_recycling_theme_overheated", "battery_recycling_expectation_priced"),
        stage4c_conditions=("utilization_down", "metal_price_down", "capex_burden", "regulatory_delay"),
        must_have_evidence=("processing_volume", "utilization", "long_term_contract", "fcf_after_capex"),
        red_flags=("recycling_theme_only", "low_utilization", "commodity_price_dependency", "capex_without_fcf"),
        success_candidates=("kj_environment_waste_platform",),
        counterexamples=("battery_recycling_no_volume", "metal_price_margin_reversal"),
        normalization_point="Waste treatment can be Green-possible with permitted assets and repeat FCF; battery recycling theme alone remains Watch.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="SECURITY_IDENTITY_DEEPFAKE",
        large_sector=Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        canonical_archetype=E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        theme_tags=("IT 보안", "딥페이크", "생체인식", "CCTV", "클라우드 보안", "AI 보안"),
        score_weight=Round20ScoreWeightDraft(20, 20, 10, 14, 13, 0, 5),
        stage1_signals=("security_incident_growth", "deepfake_regulation", "government_or_enterprise_security_spend"),
        stage2_signals=("actual_contract", "subscription_or_arr_growth", "customer_diversification", "opm_improvement"),
        stage3_conditions=("recurring_security_subscription", "low_churn", "regulatory_demand", "security_theme_frame_still_used"),
        stage4b_conditions=("security_theme_overheated", "multiple_saturation", "new_competition"),
        stage4c_conditions=("large_outage", "customer_lawsuit", "trust_damage", "renewal_rate_down"),
        must_have_evidence=("recurring_contract", "arr_or_subscription", "opm_improvement", "renewal_or_retention"),
        red_flags=("theme_only_security", "large_outage", "legal_risk", "churn", "no_recurring_revenue"),
        success_candidates=("deepfake_security_regulation_demand",),
        counterexamples=("crowdstrike_operational_trust_4c", "security_theme_no_revenue"),
        normalization_point="Security can be structural, but ARR/contracts and operational trust matter; a major outage can be hard 4C.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="CLOUD_AI_SOFTWARE_INFRA",
        large_sector=Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        canonical_archetype=E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        posture=Round10ThemePosture.GREEN_POSSIBLE,
        theme_tags=("클라우드 컴퓨팅", "ERP", "B2B SaaS", "컨택센터", "원격근무", "AI 소프트웨어"),
        score_weight=Round20ScoreWeightDraft(20, 23, 8, 16, 14, 0, 5),
        stage1_signals=("cloud_transition", "erp_saas_demand", "ai_feature_launch", "b2b_customer_growth"),
        stage2_signals=("recurring_revenue_growth", "arpu_up", "opm_improvement", "retention_confirmed"),
        stage3_conditions=("customer_lock_in", "high_fcf_conversion", "pricing_power", "old_software_frame"),
        stage4b_conditions=("saas_ai_narrative_overheated", "multiple_saturation"),
        stage4c_conditions=("churn", "ai_cost_overrun", "opm_decline", "competition_intensifies"),
        must_have_evidence=("recurring_revenue", "arpu", "retention", "opm_or_fcf_improvement"),
        red_flags=("ai_feature_only", "mau_without_monetization", "ai_cost_overrun", "churn"),
        success_candidates=("douzone_bizon_smb_cloud_erp",),
        counterexamples=("ai_software_no_paid_usage", "cloud_cost_margin_pressure"),
        normalization_point="SaaS can be Green-possible only when recurring revenue, margin, and FCF improve; AI keywords are not enough.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="EDUCATION_SPECIALTY_SERVICES",
        large_sector=Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        canonical_archetype=E2RArchetype.EDUCATION_SPECIALTY_SERVICES,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        theme_tags=("교육", "취업일자리", "키즈", "유아용품", "학습지", "에듀테크", "입시", "성인교육"),
        score_weight=Round20ScoreWeightDraft(18, 18, 5, 12, 12, 0, 5),
        stage1_signals=("entrance_exam_change", "student_count_or_price_up", "education_spending_growth"),
        stage2_signals=("repeat_revenue", "opm_improvement", "adult_or_online_expansion", "overseas_students"),
        stage3_conditions=("adult_or_overseas_growth_offsets_birthrate", "pricing_power", "fcf_improvement"),
        stage4b_conditions=("entrance_exam_theme_overheated", "policy_expectation_priced"),
        stage4c_conditions=("private_education_regulation", "student_population_decline", "price_cut", "ai_substitution"),
        must_have_evidence=("repeat_revenue", "opm_improvement", "adult_or_overseas_expansion", "fcf_improvement"),
        red_flags=("birthrate_decline", "regulation", "exam_policy_event_only", "ai_substitution"),
        success_candidates=("adult_education_subscription_candidate",),
        counterexamples=("birthrate_exposed_kids_product", "policy_regulation_education"),
        normalization_point="Education is Watch-first; Green needs adult/overseas/subscription expansion that offsets birthrate risk.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="APPAREL_BRAND_OEM",
        large_sector=Round10LargeSector.CONSUMER_RETAIL_BRAND,
        canonical_archetype=E2RArchetype.EXPORT_RECURRING_CONSUMER,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        theme_tags=("의류 브랜드", "의류 OEM", "의류 ODM", "의류소재", "K패션 브랜드", "키즈·유아용품 일부"),
        score_weight=Round20ScoreWeightDraft(18, 16, 8, 14, 12, 0, 5),
        stage1_signals=("overseas_popup", "kfashion_collaboration", "order_growth", "celebrity_ip_collaboration"),
        stage2_signals=("overseas_sales_growth", "inventory_turnover_stable", "opm_improvement", "customer_diversification"),
        stage3_conditions=("repeat_brand_purchase", "global_channel_expansion", "fcf_improvement", "old_domestic_apparel_frame"),
        stage4b_conditions=("brand_hype_overheated", "inventory_risk_expands"),
        stage4c_conditions=("inventory_increase", "discount_sales", "channel_slowdown", "order_cancellation"),
        must_have_evidence=("overseas_sales_growth", "inventory_turnover", "opm_improvement", "customer_diversification"),
        red_flags=("single_fad_brand", "inventory_build", "discounting", "channel_concentration"),
        success_candidates=("kfashion_export_channel_candidate",),
        counterexamples=("single_brand_fad_inventory", "oem_order_slowdown"),
        normalization_point="Apparel is more conservative than K-food/K-beauty; inventory and discount rate are core Red flags.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="BUILDING_MATERIALS_CYCLE",
        large_sector=Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS,
        canonical_archetype=E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        theme_tags=("건자재", "시멘트", "레미콘", "콘크리트", "철근", "거푸집", "가구"),
        score_weight=Round20ScoreWeightDraft(17, 12, 12, 12, 12, 5, 5),
        stage1_signals=("price_hike", "rate_down", "housing_start_recovery", "dividend_appeal"),
        stage2_signals=("opm_improvement", "cost_stability", "shipment_recovery", "dividend_stability"),
        stage3_conditions=("supply_rationalization", "pricing_power", "recurring_rental_or_material_revenue", "low_debt_risk"),
        stage4b_conditions=("property_recovery_priced", "dividend_theme_overheated"),
        stage4c_conditions=("pf_stress", "housing_starts_down", "vacancy_up", "dividend_cut"),
        must_have_evidence=("price_pass_through", "volume_recovery", "cost_stability", "credit_risk_contained"),
        red_flags=("pf_stress", "rates_up", "vacancy_up", "price_hike_failure"),
        success_candidates=("cement_price_cost_spread_candidate",),
        counterexamples=("housing_slowdown_materials_4c", "pf_materials_counterexample"),
        normalization_point="Building materials need price and volume, but PF/rate risk keeps Green conservative.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="REIT_DEVELOPMENT_TRUST",
        large_sector=Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS,
        canonical_archetype=E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        theme_tags=("리츠", "개발신탁", "부동산 자산 보유", "배당", "임대수익"),
        score_weight=Round20ScoreWeightDraft(17, 12, 12, 12, 12, 5, 5),
        stage1_signals=("rate_down", "dividend_appeal", "occupancy_recovery", "asset_revaluation"),
        stage2_signals=("rental_income_stability", "occupancy_stable", "refinancing_cost_stable", "dividend_stability"),
        stage3_conditions=("repeat_rental_income", "low_refinancing_risk", "nav_discount_mispricing", "dividend_coverage"),
        stage4b_conditions=("property_recovery_priced", "yield_compression_crowded"),
        stage4c_conditions=("vacancy_up", "refinancing_stress", "asset_impairment", "dividend_cut"),
        must_have_evidence=("occupancy", "rental_income", "refinancing_cost", "dividend_coverage"),
        red_flags=("rate_up", "vacancy_up", "asset_impairment", "dividend_cut"),
        success_candidates=("reit_rate_down_occupancy_candidate",),
        counterexamples=("reit_refinancing_stress", "development_trust_credit_risk"),
        normalization_point="REIT/development trust is Watch-first; rates, vacancy, debt, and dividend coverage decide quality.",
    ),
    Round20ScoreWeightTarget(
        sub_archetype="CRO_CLINICAL_SERVICE",
        large_sector=Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        canonical_archetype=E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        theme_tags=("CRO", "임상시험수탁기관", "AI 신약개발 일부", "제약바이오 서비스"),
        score_weight=Round20ScoreWeightDraft(18, 20, 8, 12, 12, 0, 5),
        stage1_signals=("clinical_trial_count_growth", "pharma_rd_growth", "order_backlog_growth"),
        stage2_signals=("sales_op_growth", "customer_diversification", "repeat_service_revenue"),
        stage3_conditions=("multi_year_backlog", "customer_portfolio_diversified", "high_fcf_conversion"),
        stage4b_conditions=("biotech_rd_expectation_overheated"),
        stage4c_conditions=("clinical_trial_cut", "customer_budget_cut", "order_cancellation"),
        must_have_evidence=("service_contract", "clinical_volume", "customer_diversification", "opm_fcf_conversion"),
        red_flags=("biotech_funding_cycle_down", "customer_concentration", "trial_delay", "low_margin_backlog"),
        success_candidates=("cro_service_backlog_candidate",),
        counterexamples=("cro_customer_budget_cut", "clinical_volume_without_margin"),
        normalization_point="CRO can move Watch-to-Green, but it is weaker than CDMO and needs backlog plus customer diversification.",
    ),
)


def round20_target_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for item in ROUND20_SCORE_WEIGHT_TARGETS:
        weights = item.score_weight.as_dict()
        rows.append(
            {
                "sub_archetype": item.sub_archetype,
                "large_sector": item.large_sector.value,
                "canonical_archetype": item.canonical_archetype.value,
                "posture": item.posture.value,
                "theme_tags": "|".join(item.theme_tags),
                "eps_fcf": str(weights["eps_fcf"]),
                "structural_visibility": str(weights["structural_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "market_mispricing": str(weights["market_mispricing"]),
                "valuation": str(weights["valuation"]),
                "capital_allocation": str(weights["capital_allocation"]),
                "information_confidence": str(weights["information_confidence"]),
                "stage1_signals": "|".join(item.stage1_signals),
                "stage2_signals": "|".join(item.stage2_signals),
                "stage3_conditions": "|".join(item.stage3_conditions),
                "stage4b_conditions": "|".join(item.stage4b_conditions),
                "stage4c_conditions": "|".join(item.stage4c_conditions),
                "must_have_evidence": "|".join(item.must_have_evidence),
                "red_flags": "|".join(item.red_flags),
                "success_candidates": "|".join(item.success_candidates),
                "counterexamples": "|".join(item.counterexamples),
                "theme_is_score_input": str(item.theme_is_score_input).lower(),
                "production_scoring_changed": str(item.production_scoring_changed).lower(),
                "normalization_point": item.normalization_point,
            }
        )
    return tuple(rows)


def round20_theme_tag_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for item in ROUND20_SCORE_WEIGHT_TARGETS:
        for tag in item.theme_tags:
            rows.append(
                {
                    "theme_tag": tag,
                    "large_sector": item.large_sector.value,
                    "primary_sub_archetype": item.sub_archetype,
                    "canonical_archetype": item.canonical_archetype.value,
                    "posture": item.posture.value,
                    "theme_is_score_input": str(item.theme_is_score_input).lower(),
                    "must_have_evidence": "|".join(item.must_have_evidence),
                    "red_flags": "|".join(item.red_flags),
                }
            )
    return tuple(rows)


def target_for(sub_archetype: str) -> Round20ScoreWeightTarget | None:
    for item in ROUND20_SCORE_WEIGHT_TARGETS:
        if item.sub_archetype == sub_archetype:
            return item
    return None


def round20_policy_groups() -> dict[str, tuple[str, ...]]:
    groups: dict[str, list[str]] = {posture.value: [] for posture in Round10ThemePosture}
    for item in ROUND20_SCORE_WEIGHT_TARGETS:
        groups[item.posture.value].append(item.sub_archetype)
    return {key: tuple(value) for key, value in groups.items()}


def write_round20_score_weight_reports(
    *,
    output_directory: str | Path = "output/e2r_round20_score_weight_v06",
    score_profile_path: str | Path = "data/sector_taxonomy/score_weight_profiles_round20_v06.csv",
    theme_map_path: str | Path = "data/sector_taxonomy/theme_tag_map_round20_v06.csv",
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    score_profile = Path(score_profile_path)
    theme_map = Path(theme_map_path)
    score_profile.parent.mkdir(parents=True, exist_ok=True)
    theme_map.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "score_profiles": score_profile,
        "theme_map": theme_map,
        "summary": output / "round20_score_weight_v06_summary.md",
        "target_matrix": output / "round20_score_weight_targets.csv",
        "theme_policy": output / "round20_theme_policy_v06.md",
        "case_candidate_plan": output / "round20_case_candidate_plan.md",
        "next_plan": output / "round20_shadow_scoring_next_plan.md",
    }
    _write_rows(round20_target_rows(), paths["score_profiles"])
    _write_rows(round20_target_rows(), paths["target_matrix"])
    _write_rows(round20_theme_tag_rows(), paths["theme_map"])
    paths["summary"].write_text(render_round20_summary_markdown(), encoding="utf-8")
    paths["theme_policy"].write_text(render_round20_theme_policy_markdown(), encoding="utf-8")
    paths["case_candidate_plan"].write_text(render_round20_case_candidate_plan_markdown(), encoding="utf-8")
    paths["next_plan"].write_text(render_round20_next_plan_markdown(), encoding="utf-8")
    return paths


def render_round20_summary_markdown() -> str:
    groups = round20_policy_groups()
    lines = [
        "# Round-20 Score-Weight v0.6 Summary",
        "",
        f"- source_round: `{ROUND20_SOURCE_ROUND_PATH}`",
        f"- target_count: {len(ROUND20_SCORE_WEIGHT_TARGETS)}",
        f"- theme_tag_count: {len(round20_theme_tag_rows())}",
        f"- green_possible_count: {len(groups[Round10ThemePosture.GREEN_POSSIBLE.value])}",
        f"- watch_yellow_first_count: {len(groups[Round10ThemePosture.WATCH_YELLOW_FIRST.value])}",
        f"- redteam_first_count: {len(groups[Round10ThemePosture.REDTEAM_FIRST.value])}",
        "- production_scoring_changed: false",
        "- theme_tags_are_score_input: false",
        "",
        "## Interpretation",
        "- Round 20 is a v0.6 scoring hypothesis, not a production score change.",
        "- Theme tags route search and case mining. Evidence fields create score.",
        "- Example: `액침냉각` routes to AI data-center cooling research, but needs orders, customers, revenue timing, and margin evidence.",
        "- Example: `교육` can remain Watch when birthrate/regulation risk is not offset by adult, overseas, or recurring revenue.",
        "- Price-path validation and shadow score-price alignment are still required before production scoring.",
    ]
    return "\n".join(lines) + "\n"


def render_round20_theme_policy_markdown() -> str:
    groups = round20_policy_groups()
    lines = ["# Round-20 Theme Policy v0.6", ""]
    for posture in Round10ThemePosture:
        lines.append(f"## {posture.value}")
        for label in groups[posture.value]:
            lines.append(f"- `{label}`")
        lines.append("")
    lines.extend(
        [
            "## Easy Examples",
            "- Rail infrastructure needs confirmed orders and delivery schedules; policy headlines stay Watch.",
            "- AI cooling can be structural only when customers, orders, delivery, and service economics appear.",
            "- Security can have structural demand, but a large outage or trust break can be hard 4C.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round20_case_candidate_plan_markdown() -> str:
    lines = ["# Round-20 Case Candidate Plan", ""]
    for item in ROUND20_SCORE_WEIGHT_TARGETS:
        lines.append(f"## {item.sub_archetype}")
        lines.append("### Success / Candidate")
        for case_id in item.success_candidates:
            lines.append(f"- `{case_id}`")
        lines.append("### Counterexample / Risk")
        for case_id in item.counterexamples:
            lines.append(f"- `{case_id}`")
        lines.append("")
    return "\n".join(lines)


def render_round20_next_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-20 Next Plan",
            "",
            "1. Convert these v0.6 targets into case records only after evidence is collected.",
            "2. Backfill stage prices, peak prices, MFE/MAE, and drawdown for each case.",
            "3. Compare shadow score against price path and EPS/FCF evidence.",
            "4. Keep production StageClassifier thresholds unchanged.",
            "",
            "## What Not To Change",
            "- Do not use these v0.6 weights in production scoring yet.",
            "- Do not treat theme names as score evidence.",
            "- Do not make rail, cooling, waste, SaaS, education, apparel, REIT, or CRO cases Green without actual evidence fields.",
            "- Do not invent contract amounts, utilization, ARR, retention, FCF, dates, or prices.",
            "",
        ]
    )


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
    "ROUND20_SCORE_WEIGHT_TARGETS",
    "ROUND20_SOURCE_ROUND_PATH",
    "Round20ScoreWeightDraft",
    "Round20ScoreWeightTarget",
    "render_round20_case_candidate_plan_markdown",
    "render_round20_next_plan_markdown",
    "render_round20_summary_markdown",
    "render_round20_theme_policy_markdown",
    "round20_policy_groups",
    "round20_target_rows",
    "round20_theme_tag_rows",
    "target_for",
    "write_round20_score_weight_reports",
]
