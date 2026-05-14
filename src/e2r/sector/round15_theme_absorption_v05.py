"""Round-15 missing-theme absorption and score-weight v0.5 matrix.

Round 15 extends Round 14 by separating additional theme families that were
still too broad. This remains calibration/report material only: theme tags
route research and case mining, while production scoring remains unchanged.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND15_SOURCE_ROUND_PATH = "docs/round/round_15.md"


@dataclass(frozen=True)
class Round15ScoreWeightDraft:
    eps_fcf: int
    structural_visibility: int
    bottleneck_pricing: int
    market_mispricing: int
    valuation: int
    capital_allocation: int = 0
    information_confidence: int = 5
    risk_penalty: str = ""

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
class Round15ThemeAbsorptionTarget:
    sub_archetype: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    theme_tags: tuple[str, ...]
    score_weight: Round15ScoreWeightDraft
    green_conditions: tuple[str, ...]
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


ROUND15_THEME_ABSORPTION_TARGETS: tuple[Round15ThemeAbsorptionTarget, ...] = (
    Round15ThemeAbsorptionTarget(
        "WASTE_RECYCLING_ENVIRONMENT",
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("폐기물처리", "폐배터리", "탈 플라스틱", "전자폐기물", "플라스틱 재활용", "폐기물 에너지화"),
        Round15ScoreWeightDraft(18, 22, 15, 13, 12, 3, 5, "utilization / material price / CAPEX"),
        ("permitted_facility_bottleneck", "repeat_fcf", "customer_diversification", "infrastructure_frame_rerating"),
        ("esg_recycling_theme_overheated", "battery_recycling_expectation_fully_priced"),
        ("utilization_down", "metal_price_down", "regulation_delay", "capex_burden"),
        ("processing_volume", "long_term_contract", "utilization", "op_fcf_improvement"),
        ("theme_only_recycling", "low_utilization", "metal_price_dependency", "capex_without_fcf"),
        ("waste_treatment_platform_candidate", "plastic_recycling_infra_candidate", "waste_to_energy_candidate"),
        ("battery_recycling_volume_absent_counterexample", "recycling_capex_low_utilization_4c"),
        "Waste treatment can become infrastructure-like E2R, but recycling themes need actual volume and FCF.",
    ),
    Round15ThemeAbsorptionTarget(
        "REFINING_OIL_SPREAD",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("정유", "화학-정유", "윤활유", "LPG", "유가 상승 수혜"),
        Round15ScoreWeightDraft(20, 10, 18, 10, 10, 0, 5, "oil / refining margin / inventory gain-loss"),
        ("refining_margin_recovery", "demand_sustained", "inventory_risk_low", "fcf_improvement"),
        ("spread_recovery_fully_priced", "inventory_gain_mistaken_for_structure"),
        ("refining_margin_down", "inventory_loss", "demand_slowdown"),
        ("refining_margin", "product_mix", "inventory_status", "fcf_improvement"),
        ("margin_bounce_only", "inventory_gain_only", "demand_visibility_weak"),
        ("refining_spread_recovery_candidate", "lube_mix_candidate"),
        ("inventory_gain_false_signal", "refining_recovery_takes_time_counterexample"),
        "Refining can rebound hard, but structural visibility starts low unless FCF and demand persistence are visible.",
    ),
    Round15ThemeAbsorptionTarget(
        "CHEMICAL_SPREAD",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        ("화학", "석유화학", "페인트", "주정", "탈 플라스틱 소재"),
        Round15ScoreWeightDraft(20, 8, 16, 8, 8, 0, 5, "China oversupply very high"),
        ("product_spread_improves", "oversupply_eases", "restructuring_or_capacity_closure", "op_fcf_improvement"),
        ("cheap_valuation_cycle_bounce_crowded", "spread_recovery_over_extrapolated"),
        ("china_oversupply_persists", "spread_reversal", "capacity_addition", "loss_expands"),
        ("product_spread", "capacity_discipline", "inventory_status", "restructuring"),
        ("cheap_only", "china_oversupply", "no_capacity_closure", "spread_only"),
        ("chemical_restructuring_candidate", "specialty_chemical_spread_candidate"),
        ("petrochemical_oversupply_4c", "cheap_chemical_value_trap"),
        "Chemical Green is highly restricted because China/Middle-East oversupply can turn EPS rebound into 4C.",
    ),
    Round15ThemeAbsorptionTarget(
        "STEEL_METAL_SPREAD",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        ("철강", "철강 주요업체", "철강 중소형업체", "비철금속", "철근", "강관"),
        Round15ScoreWeightDraft(18, 10, 16, 10, 10, 0, 5, "China supply / construction demand / cost"),
        ("high_value_mix", "shipbuilding_auto_demand", "china_supply_discipline", "cost_stable"),
        ("steel_cycle_recovery_fully_priced", "construction_demand_over_extrapolated"),
        ("cheap_imports", "construction_slowdown", "rebar_oversupply", "cost_up"),
        ("steel_spread", "value_added_mix", "china_supply", "cost_status"),
        ("china_low_price_import", "construction_demand_weak", "cost_inflation"),
        ("high_value_steel_mix_candidate", "shipbuilding_steel_demand_candidate"),
        ("rebar_oversupply_counterexample", "china_import_margin_4c"),
        "Steel is mostly cycle/watch; structural Green needs supply discipline and value-added mix.",
    ),
    Round15ThemeAbsorptionTarget(
        "RETAIL_ECOMMERCE_LOGISTICS",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("편의점", "홈쇼핑", "음식료 유통", "마켓컬리", "오아시스", "콜드체인", "택배", "종합물류"),
        Round15ScoreWeightDraft(18, 16, 5, 14, 14, 0, 5, "logistics cost / competition / inventory"),
        ("opm_fcf_improvement", "store_or_logistics_efficiency", "pb_or_high_margin_mix", "old_retail_frame"),
        ("consumption_recovery_fully_priced", "listing_premium_crowded"),
        ("china_direct_purchase_pressure", "logistics_loss", "inventory_increase", "home_shopping_decline"),
        ("same_store_sales", "unit_economics", "opm_improvement", "fcf_improvement"),
        ("listing_event_only", "gmv_without_profit", "delivery_cost_pressure", "traffic_only"),
        ("convenience_store_efficiency_success_candidate", "cold_chain_repeat_logistics_candidate"),
        ("fresh_ecommerce_loss_counterexample", "china_direct_purchase_margin_pressure_counterexample"),
        "Retail/e-commerce needs OPM and FCF proof; GMV, traffic, or listing events are not enough.",
    ),
    Round15ThemeAbsorptionTarget(
        "INSURANCE_FINANCIAL_VALUEUP",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        ("손해보험", "생명보험", "화재", "금융지주회사", "은행", "증권사", "VC", "고배당주", "신용정보"),
        Round15ScoreWeightDraft(15, 20, 5, 15, 25, 10, 5, "loss ratio / capital ratio / credit cost"),
        ("roe_pbr_frame_change", "csm_or_cet1_stable", "return_policy_executed", "credit_cost_contained"),
        ("pbr_roe_gap_normalized", "valueup_success_crowded"),
        ("loss_ratio_worsens", "capital_ratio_down", "pf_credit_cost", "return_policy_retreat"),
        ("roe", "csm_or_cet1", "capital_ratio", "shareholder_return_execution"),
        ("low_pbr_only", "weak_capital_ratio", "credit_cost", "brokerage_cycle_only"),
        ("nonlife_insurance_loss_ratio_success_candidate", "bank_valueup_roe_return_candidate", "securities_ib_cycle_candidate"),
        ("low_pbr_no_roe_value_trap", "pf_credit_cost_financial", "capital_ratio_weak_insurer"),
        "Financial value-up scoring must connect ROE/PBR, capital strength, and executed return.",
    ),
    Round15ThemeAbsorptionTarget(
        "DIGITAL_ASSET_TOKENIZATION",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        ("스테이블코인", "STO", "디지털자산", "블록체인", "결제서비스", "토스 관련주", "지역화폐", "NFT"),
        Round15ScoreWeightDraft(16, 18, 8, 16, 12, 0, 5, "regulation / security / adoption"),
        ("regulation_approved", "real_issuance_or_volume", "fee_model", "recurring_financial_infra_revenue"),
        ("law_expectation_overheated", "related_stocks_rally_without_revenue"),
        ("regulation_denied_or_delayed", "security_issue", "volume_absent", "no_revenue_model"),
        ("regulation_approval", "transaction_volume", "fee_model", "regulated_revenue"),
        ("coin_theme_only", "nft_theme", "law_expectation_only", "security_issue"),
        ("stablecoin_payment_infra_candidate", "sto_platform_candidate", "credit_data_recurring_revenue_candidate"),
        ("crypto_theme_no_revenue_counterexample", "sto_law_expectation_only_counterexample", "nft_theme_overheat_counterexample"),
        "Digital finance stays non-Green until regulation, volume, and monetization are real.",
    ),
    Round15ThemeAbsorptionTarget(
        "HYDROGEN_RENEWABLE_POLICY",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("수소차 연료전지", "수소차 인프라", "태양광", "풍력", "탄소배출권", "LNG 발전유통", "스마트그리드"),
        Round15ScoreWeightDraft(18, 18, 12, 12, 10, 0, 5, "policy / subsidy / supply chain"),
        ("actual_orders_or_utilization", "op_eps_conversion", "low_policy_risk", "cost_competitiveness"),
        ("policy_subsidy_premium_fully_priced", "capex_burden_visible"),
        ("subsidy_cut", "tariff_customs_issue", "project_delay", "utilization_down"),
        ("actual_contract", "utilization", "policy_support", "margin_visibility"),
        ("policy_only", "no_customer", "subsidy_dependency", "project_delay"),
        ("hydrogen_fuel_cell_plant_candidate", "wind_equipment_project_candidate", "smart_grid_order_candidate"),
        ("hydrogen_theme_no_revenue_counterexample", "solar_tariff_supplychain_4c", "wind_project_delay_counterexample"),
        "Policy news is Stage 1; Stage 2-plus needs orders, utilization, and OP/EPS conversion.",
    ),
    Round15ThemeAbsorptionTarget(
        "BATTERY_RECYCLING_ESS_SHIFT",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("폐배터리", "ESS", "전고체 배터리", "전기차 화재", "2차전지 소재", "2차전지 부품", "리튬"),
        Round15ScoreWeightDraft(20, 16, 14, 10, 10, 0, 5, "very high"),
        ("recycling_volume", "ess_revenue_conversion", "price_pass_through", "fcf_after_capex"),
        ("ev_and_ess_story_crowded", "battery_valuation_overheated"),
        ("ev_demand_slows", "mineral_price_down", "capex_overbuild", "recycling_volume_shortfall"),
        ("ess_demand", "recycling_volume", "utilization_improvement", "fcf_after_capex"),
        ("ev_headline_only", "solid_state_theme_only", "mineral_price_dependency", "collection_volume_absent"),
        ("ess_shift_battery_candidate", "battery_recycling_material_recovery_candidate"),
        ("ecopro_bm_overheat_counterexample", "battery_capa_overbuild", "solid_state_theme_no_revenue"),
        "Battery recycling/ESS is a watch path, but Green defense remains more important than optimism.",
    ),
    Round15ThemeAbsorptionTarget(
        "TIRE_AUTO_COMPONENT_SPREAD",
        Round10LargeSector.MOBILITY_TRANSPORT_LEISURE,
        E2RArchetype.AUTO_MOBILITY_COMPONENTS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("타이어", "현대·기아차 부품주", "자동차 경량화", "전기차 부품", "자율주행", "카메라"),
        Round15ScoreWeightDraft(20, 18, 10, 14, 14, 0, 5, "raw materials / customer concentration"),
        ("customer_diversification", "raw_material_spread", "opm_improvement", "repeat_supply_visibility"),
        ("peak_margin", "auto_cycle_peak", "valuation_normalized"),
        ("raw_material_spike", "factory_disruption", "ev_demand_slowdown", "recall_quality_cost"),
        ("oe_re_mix", "asp", "raw_material_spread", "customer_diversification"),
        ("single_customer_dependency", "raw_material_inflation", "factory_disruption", "auto_demand_slowdown"),
        ("tire_spread_success_candidate", "adas_component_customer_diversification_candidate"),
        ("factory_fire_4c_counterexample", "ev_demand_slowdown_component"),
        "Auto components need customer and cost evidence; supplier theme exposure alone is weak.",
    ),
    Round15ThemeAbsorptionTarget(
        "DIAGNOSTICS_INFECTIOUS_EVENT",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.ONE_OFF_EVENT_DEMAND,
        Round10ThemePosture.REDTEAM_FIRST,
        ("엠폭스", "코로나19", "전염병 진단", "동물백신", "방역", "빈대퇴치", "황사미세먼지 마스크", "공기정화"),
        Round15ScoreWeightDraft(20, 5, 5, 5, 5, 0, 5, "one-off very high"),
        ("recurring_diagnostic_platform", "consumable_installed_base", "government_long_term_contract"),
        ("pandemic_margin_extrapolated", "temporary_eps_annualized"),
        ("demand_normalization", "guidance_down", "inventory_build", "event_fades"),
        ("recurring_non_event_demand", "post_event_revenue", "margin_normalization"),
        ("one_off_demand", "inventory_build", "guidance_down", "demand_cliff"),
        ("recurring_diagnostic_platform_candidate", "government_prevention_contract_candidate"),
        ("seegene_2020_red", "mask_theme_oneoff_counterexample", "mpox_pest_event_counterexample"),
        "Even explosive EPS can be Red/Yellow when demand is one-off and normalizes quickly.",
    ),
    Round15ThemeAbsorptionTarget(
        "SPECULATIVE_SCIENCE_THEME",
        Round10LargeSector.POLICY_GEOPOLITICAL_EVENT,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        ("초전도체", "맥신", "그래핀", "양자 기술", "스페이스X", "퓨리오사AI 관련주", "뉴로모픽 반도체"),
        Round15ScoreWeightDraft(5, 5, 5, 5, 5, 0, 5, "extreme"),
        ("commercial_revenue", "government_or_enterprise_long_contract", "verified_product", "fy1_fy2_op_confirmed"),
        ("price_only_theme_rally", "relatedness_unclear_but_crowded"),
        ("validation_failure", "relatedness_denied", "commercialization_failure", "demand_fades"),
        ("commercial_contract", "revenue_conversion", "verified_product"),
        ("paper_only", "relatedness_unclear", "price_only_rally", "commercialization_failure"),
        ("verified_science_product_candidate",),
        ("superconductor_theme_overheat", "mxene_graphene_theme_counterexample", "quantum_theme_no_revenue_counterexample"),
        "Speculative science is mainly a Green-blocking filter until commercialization produces real revenue.",
    ),
    Round15ThemeAbsorptionTarget(
        "AGRI_LIVESTOCK_FOOD_COMMODITY",
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        ("양돈주", "육계주", "배합사료", "대두", "농업 종자", "비료", "농약", "참치 원양어업", "스마트팜", "농기계"),
        Round15ScoreWeightDraft(18, 10, 14, 8, 8, 0, 5, "commodity / disease event"),
        ("price_pass_through", "repeat_demand", "op_eps_revision", "smartfarm_or_equipment_orders"),
        ("commodity_price_cycle_fully_priced", "disease_event_extrapolated"),
        ("feed_cost_squeeze", "commodity_reversal", "weather_event_fades", "inventory_loss"),
        ("price_pass_through", "feed_cost", "inventory_status", "op_eps_revision"),
        ("disease_event_only", "feed_cost_squeeze", "commodity_reversal", "weather_theme"),
        ("smart_farm_order_candidate", "fishery_price_spread_candidate", "agri_equipment_export_candidate"),
        ("pork_price_cycle_counterexample", "feed_cost_squeeze_counterexample", "weather_event_theme_counterexample"),
        "Agri/livestock is usually cycle/event; Green requires pass-through plus repeat demand.",
    ),
)


def round15_target_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for item in ROUND15_THEME_ABSORPTION_TARGETS:
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
                "risk_penalty": item.score_weight.risk_penalty,
                "green_conditions": "|".join(item.green_conditions),
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


def round15_theme_tag_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for item in ROUND15_THEME_ABSORPTION_TARGETS:
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
                    "risk_penalty": item.score_weight.risk_penalty,
                }
            )
    return tuple(rows)


def target_for(sub_archetype: str) -> Round15ThemeAbsorptionTarget | None:
    for item in ROUND15_THEME_ABSORPTION_TARGETS:
        if item.sub_archetype == sub_archetype:
            return item
    return None


def round15_policy_groups() -> dict[str, tuple[str, ...]]:
    groups: dict[str, list[str]] = {posture.value: [] for posture in Round10ThemePosture}
    for item in ROUND15_THEME_ABSORPTION_TARGETS:
        groups[item.posture.value].append(item.sub_archetype)
    return {key: tuple(value) for key, value in groups.items()}


def write_round15_theme_absorption_reports(
    *,
    output_directory: str | Path = "output/e2r_round15_theme_absorption_v05",
    score_profile_path: str | Path = "data/sector_taxonomy/score_weight_profiles_round15.csv",
    theme_map_path: str | Path = "data/sector_taxonomy/theme_tag_map_round15.csv",
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
        "summary": output / "round15_theme_absorption_v05_summary.md",
        "target_matrix": output / "round15_theme_absorption_targets.csv",
        "theme_policy": output / "round15_green_watch_red_policy.md",
        "case_candidate_plan": output / "round15_case_candidate_plan.md",
        "next_plan": output / "round15_cases_v03_next_plan.md",
    }
    _write_rows(round15_target_rows(), paths["score_profiles"])
    _write_rows(round15_target_rows(), paths["target_matrix"])
    _write_rows(round15_theme_tag_rows(), paths["theme_map"])
    paths["summary"].write_text(render_round15_summary_markdown(), encoding="utf-8")
    paths["theme_policy"].write_text(render_round15_theme_policy_markdown(), encoding="utf-8")
    paths["case_candidate_plan"].write_text(render_round15_case_candidate_plan_markdown(), encoding="utf-8")
    paths["next_plan"].write_text(render_round15_next_plan_markdown(), encoding="utf-8")
    return paths


def render_round15_summary_markdown() -> str:
    groups = round15_policy_groups()
    lines = [
        "# Round-15 Theme Absorption v0.5 Summary",
        "",
        f"- source_round: `{ROUND15_SOURCE_ROUND_PATH}`",
        f"- target_count: {len(ROUND15_THEME_ABSORPTION_TARGETS)}",
        f"- theme_tag_count: {len(round15_theme_tag_rows())}",
        f"- green_possible_count: {len(groups[Round10ThemePosture.GREEN_POSSIBLE.value])}",
        f"- watch_yellow_first_count: {len(groups[Round10ThemePosture.WATCH_YELLOW_FIRST.value])}",
        f"- redteam_first_count: {len(groups[Round10ThemePosture.REDTEAM_FIRST.value])}",
        "- production_scoring_changed: false",
        "- theme_tags_are_score_input: false",
        "",
        "## Interpretation",
        "- Round 15 absorbs missing theme families and ties them to success/counterexample evidence.",
        "- Theme names remain search labels; evidence fields and price-path validation decide future score weights.",
        "- Example: `폐기물처리` can be infrastructure-like if permits, utilization, contracts, and repeat FCF exist.",
        "- Example: `전염병 진단` can show explosive EPS but stays RedTeam-first if demand is one-off.",
    ]
    return "\n".join(lines) + "\n"


def render_round15_theme_policy_markdown() -> str:
    groups = round15_policy_groups()
    lines = ["# Round-15 Green / Watch / Red Policy", ""]
    for posture in Round10ThemePosture:
        lines.append(f"## {posture.value}")
        for label in groups[posture.value]:
            lines.append(f"- `{label}`")
        lines.append("")
    lines.extend(
        [
            "## Easy Examples",
            "- `WASTE_RECYCLING_ENVIRONMENT` is Watch/Yellow until actual processing volume and FCF are visible.",
            "- `INSURANCE_FINANCIAL_VALUEUP` can be Green-possible only with ROE, capital strength, and executed return.",
            "- `CHEMICAL_SPREAD` is RedTeam-first because oversupply can turn a cheap rebound into 4C.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round15_case_candidate_plan_markdown() -> str:
    lines = ["# Round-15 Case Candidate Plan", ""]
    for item in ROUND15_THEME_ABSORPTION_TARGETS:
        lines.append(f"## {item.sub_archetype}")
        lines.append("### Success / Candidate")
        for case_id in item.success_candidates:
            lines.append(f"- `{case_id}`")
        lines.append("### Counterexample / Risk")
        for case_id in item.counterexamples:
            lines.append(f"- `{case_id}`")
        lines.append("")
    return "\n".join(lines)


def render_round15_next_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-15 cases_v03 Next Plan",
            "",
            "1. Convert the Round-15 success/counterexample plan into `cases_v03.jsonl` candidates.",
            "2. Add stage date candidates only when the source text supports them.",
            "3. Backfill stage2/stage3 price, MFE/MAE, peak price, and drawdown.",
            "4. Run score-price alignment before any shadow scoring.",
            "5. Keep production StageClassifier and Stage 3-Green thresholds unchanged.",
            "",
            "## What Not To Change",
            "- Do not use theme tags as production evidence.",
            "- Do not use Round-15 targets as candidate-generation labels.",
            "- Do not treat one-off EPS spikes, cheap commodity rebounds, or policy headlines as structural E2R without repeat FCF evidence.",
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
    "ROUND15_SOURCE_ROUND_PATH",
    "ROUND15_THEME_ABSORPTION_TARGETS",
    "Round15ScoreWeightDraft",
    "Round15ThemeAbsorptionTarget",
    "render_round15_case_candidate_plan_markdown",
    "render_round15_next_plan_markdown",
    "render_round15_summary_markdown",
    "render_round15_theme_policy_markdown",
    "round15_policy_groups",
    "round15_target_rows",
    "round15_theme_tag_rows",
    "target_for",
    "write_round15_theme_absorption_reports",
]
