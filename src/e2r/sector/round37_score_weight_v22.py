"""Round-37 cases_v19 expansion and score-weight validation v2.2.

Round 37 expands defense-tech, semiconductor utility infrastructure, cold
chain logistics, data-center water reuse, satellite connectivity, defense AI
software, AI data-center power equipment, and counter-UAS cases. It is
calibration/report material only. Production feature engineering, scoring,
staging, and RedTeam code must not import this module.
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


ROUND37_SOURCE_ROUND_PATH = "docs/round/round_37.md"
ROUND37_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round37_score_weight_v22"
ROUND37_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v19_round37.jsonl"
ROUND37_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round37_v22.csv"


@dataclass(frozen=True)
class Round37ScoreWeightDraft:
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
class Round37ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    validation_group: str
    score_weight: Round37ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    validation_metrics: tuple[str, ...]
    success_criteria: str
    failure_criteria: str
    normalization_point: str

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round37CaseCandidate:
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


ROUND37_SCORE_TARGETS: tuple[Round37ScoreTarget, ...] = (
    Round37ScoreTarget(
        "DEFENSE_TECH_AUTONOMOUS_SYSTEMS",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        "backlog_contract",
        Round37ScoreWeightDraft(20, 22, 15, 15, 14, 2, 5),
        ("defense_autonomy", "low_cost_munition", "containerized_missile", "c_uas"),
        ("government_framework", "procurement_quantity", "production_capacity", "delivery_schedule"),
        ("multi_year_procurement", "op_eps_revision", "valuation_frame_shift"),
        ("government_framework", "procurement_quantity", "production_capacity", "delivery_schedule", "op_eps_revision"),
        ("program_delay", "procurement_uncertainty", "valuation_overheat", "export_control", "prototype_only"),
        ("procurement_delay", "program_cancel", "export_control_block", "valuation_unwind"),
        ("mfe_90d", "mfe_180d", "mfe_1y", "mae_180d", "backlog_growth", "contract_conversion", "gross_margin"),
        "Framework agreement converting into procurement, delivery, EPS revision, and rerating is aligned.",
        "Prototype, news, or private valuation without revenue is price_moved_without_evidence.",
        "Defense autonomous systems need government framework, volume, production, and delivery evidence.",
    ),
    Round37ScoreTarget(
        "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.GREEN_POSSIBLE,
        "utility_like_infra",
        Round37ScoreWeightDraft(19, 23, 13, 13, 12, 3, 5),
        ("fab_capex", "ultrapure_gas", "onsite_gas_plant", "advanced_memory_fab"),
        ("long_term_supply_contract", "take_or_pay", "plant_investment", "fab_ramp_schedule"),
        ("utility_like_revenue", "fcf_conversion", "customer_concentration_controlled"),
        ("long_term_supply_contract", "onsite_gas_plant", "take_or_pay", "advanced_memory_fab", "fab_ramp_schedule"),
        ("fab_delay", "customer_concentration", "energy_cost", "contract_terms", "theme_only"),
        ("fab_delay", "customer_capex_cut", "energy_cost_spike", "plant_underutilization"),
        ("mfe_180d", "mfe_1y", "fab_schedule", "op_margin", "capex_payback", "customer_concentration"),
        "Fab ramp-up and gas supplier FCF moving together is aligned.",
        "Fab delay or customer capex cut turning plant utilization weak is thesis_break.",
        "Semiconductor gases are fab utility-like only when long-term onsite contracts are explicit.",
    ),
    Round37ScoreTarget(
        "COLD_CHAIN_REIT_LOGISTICS",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        "reit_utility_like",
        Round37ScoreWeightDraft(17, 21, 12, 12, 11, 5, 5),
        ("cold_storage", "temperature_controlled_logistics", "reit_ipo", "pharma_food_chain"),
        ("occupancy", "long_term_tenant_contract", "noi_affo_growth", "energy_cost_control"),
        ("stable_affo", "funding_cost_controlled", "tenant_concentration_low"),
        ("occupancy", "long_term_tenant_contract", "noi_affo_growth", "energy_cost_control"),
        ("energy_cost", "occupancy", "funding_cost", "capex", "tenant_concentration", "ipo_event_only"),
        ("energy_cost_spike", "occupancy_drop", "funding_cost_spike", "dividend_coverage_break"),
        ("mfe_180d", "mae_1y", "affo_growth", "occupancy", "energy_cost_margin", "debt_cost", "dividend_coverage"),
        "NOI/AFFO and occupancy moving with price is aligned.",
        "Scale or IPO without AFFO quality, funding discipline, and occupancy is no_rerating.",
        "Cold chain is infrastructure/REIT-like, not simple e-commerce logistics.",
    ),
    Round37ScoreTarget(
        "DATA_CENTER_WATER_REUSE_INFRA",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        "infra_utility_like",
        Round37ScoreWeightDraft(16, 18, 14, 12, 10, 2, 5),
        ("datacenter_water_use", "water_reuse", "closed_loop_cooling", "municipal_water_infra"),
        ("datacenter_customer", "water_reuse_contract", "water_savings_metric", "recurring_service_revenue"),
        ("permitting_advantage", "service_margin_visible", "policy_dependency_low"),
        ("datacenter_customer", "water_reuse_contract", "water_savings_metric", "recurring_service_revenue"),
        ("permitting", "local_opposition", "project_economics", "policy_dependency", "no_customer"),
        ("permitting_denial", "local_opposition", "project_delay", "policy_reversal"),
        ("mfe_180d", "mfe_1y", "contract_to_revenue", "permitting_success", "service_margin", "policy_drawdown"),
        "Water-reuse contracts plus recurring service revenue can support Watch-to-Green.",
        "Policy or water-scarcity narrative without customer revenue is event_watch.",
        "Data-center water reuse is a useful AI infra sub-axis, but customer and revenue proof are required.",
    ),
    Round37ScoreTarget(
        "SATELLITE_CONNECTIVITY_INFRA",
        Round10LargeSector.MOBILITY_TRANSPORT_LEISURE,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        "software_recurring",
        Round37ScoreWeightDraft(18, 20, 10, 13, 11, 2, 5),
        ("satellite_connectivity", "airline_connectivity", "maritime_connectivity", "secure_comms"),
        ("recurring_service_revenue", "airline_or_defense_contract", "backlog_growth", "ebitda_margin"),
        ("low_churn", "capex_debt_controlled", "customer_contract_duration"),
        ("recurring_service_revenue", "airline_or_defense_contract", "backlog_growth", "ebitda_margin"),
        ("launch_delay", "capex_debt", "customer_concentration", "constellation_competition", "spacex_theme_only"),
        ("launch_delay", "debt_stress", "customer_loss", "constellation_overbuild"),
        ("mfe_90d", "mfe_180d", "mfe_1y", "backlog_growth", "revenue_growth", "ebitda_margin", "debt_capex"),
        "Contract, backlog, recurring connectivity revenue, and margin growth moving together is aligned.",
        "Space or satellite theme without revenue or with debt/capex pressure is false_positive.",
        "Satellite connectivity must separate SpaceX theme labels from recurring service revenue.",
    ),
    Round37ScoreTarget(
        "DEFENSE_AI_SOFTWARE_INTELLIGENCE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        "software_recurring",
        Round37ScoreWeightDraft(19, 21, 10, 15, 14, 0, 5),
        ("defense_ai", "maven_like_system", "intelligence_fusion", "command_software"),
        ("government_software_contract", "program_of_record", "recurring_license", "data_lock_in"),
        ("gross_margin_visible", "rpo_backlog_growth", "budget_cycle_controlled"),
        ("government_software_contract", "program_of_record", "recurring_license", "gross_margin_visible"),
        ("procurement_delay", "ethical_regulation", "customer_concentration", "budget_cycle", "prototype_only"),
        ("program_nonrenewal", "ethical_regulatory_block", "budget_cut", "prototype_nonconversion"),
        ("mfe_180d", "mae_1y", "government_revenue_growth", "gross_margin", "rpo_backlog", "program_renewal"),
        "Prototype converting into program-of-record and recurring revenue is aligned.",
        "Prototype/news without follow-on contracts is price_only.",
        "Defense AI software needs software-like recurring contract evidence, not only AI defense headlines.",
    ),
    Round37ScoreTarget(
        "AI_DATA_CENTER_POWER_EQUIPMENT",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        "backlog_contract",
        Round37ScoreWeightDraft(21, 22, 18, 13, 12, 0, 5),
        ("ups", "pdu", "switchgear", "modular_power", "datacenter_power_density"),
        ("bookings_growth", "backlog_growth", "direct_datacenter_customer", "service_revenue"),
        ("backlog_conversion", "op_margin_improvement", "ai_capex_risk_controlled"),
        ("bookings_growth", "backlog_growth", "direct_datacenter_customer", "op_margin_improvement"),
        ("ai_capex_delay", "low_margin_project", "supply_chain", "bookings_slowdown", "theme_only"),
        ("bookings_slowdown", "margin_miss", "ai_capex_cut", "supply_chain_break"),
        ("mfe_180d", "mfe_1y", "bookings_growth", "backlog_conversion", "gross_margin", "valuation_crowding"),
        "Bookings converting into revenue and OP is aligned.",
        "Theme rally followed by bookings slowdown or margin miss becomes 4B/4C.",
        "AI data-center power equipment is internal power infra, distinct from grid transformers.",
    ),
    Round37ScoreTarget(
        "DEFENSE_DRONE_COUNTER_UAS",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        "backlog_contract",
        Round37ScoreWeightDraft(20, 22, 14, 14, 13, 3, 5),
        ("loitering_munition", "counter_uas", "directed_energy", "switchblade"),
        ("military_delivery_contract", "idiq_framework", "production_capacity", "backlog_growth"),
        ("op_eps_revision", "gross_margin_visible", "export_control_risk_controlled"),
        ("military_delivery_contract", "idiq_framework", "production_capacity", "backlog_growth", "op_eps_revision"),
        ("production_capacity", "mna_dilution", "export_control", "program_delay", "prototype_only"),
        ("program_delay", "export_control_block", "production_shortfall", "mna_dilution_unwind"),
        ("mfe_180d", "mfe_1y", "mna_drawdown", "backlog_conversion", "gross_margin", "program_renewal"),
        "Defense-tech narrative converting into delivery, backlog, and EPS is aligned.",
        "M&A/prototype/theme without OP/FCF is false_positive.",
        "Counter-UAS and drones need actual military delivery and production-capacity proof.",
    ),
)


ROUND37_CASE_CANDIDATES: tuple[Round37CaseCandidate, ...] = (
    Round37CaseCandidate("anduril_low_cost_containerized_munitions_framework_candidate", "DEFENSE_TECH_AUTONOMOUS_SYSTEMS", "ANDURIL_FW", "Anduril low-cost containerized munitions framework candidate", "US", "success_candidate", ("government_framework", "procurement_quantity", "production_capacity"), ("procurement_uncertainty", "valuation_overheat"), "Framework plus volume procurement is stronger than drone-tech headlines."),
    Round37CaseCandidate("anduril_high_private_valuation_4b_watch", "DEFENSE_TECH_AUTONOMOUS_SYSTEMS", "ANDURIL_4B", "Anduril high private valuation 4B watch", "US", "4b_watch", ("defense_autonomy",), ("valuation_overheat", "valuation_unwind"), "Private valuation can be 4B-watch, not public scoring evidence."),
    Round37CaseCandidate("defense_autonomy_prototype_no_revenue_counterexample", "DEFENSE_TECH_AUTONOMOUS_SYSTEMS", "DEF_PROTO", "Defense autonomy prototype no revenue counterexample", "GLOBAL", "failed_rerating", ("defense_autonomy",), ("prototype_only", "procurement_uncertainty"), "Prototype without procurement or revenue remains weak."),
    Round37CaseCandidate("procurement_delay_autonomous_systems_4c", "DEFENSE_TECH_AUTONOMOUS_SYSTEMS", "AUTON_DELAY_4C", "Procurement delay autonomous systems 4C", "GLOBAL", "4c_thesis_break", ("containerized_missile",), ("procurement_delay", "program_cancel"), "Procurement delay can break autonomous defense thesis."),
    Round37CaseCandidate("air_liquide_micron_ultrapure_gas_plant_candidate", "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA", "AI_MICRON_GAS", "Air Liquide Micron ultrapure gas plant candidate", "US", "success_candidate", ("onsite_gas_plant", "advanced_memory_fab", "fab_ramp_schedule"), ("fab_delay", "customer_concentration"), "Onsite gas plant tied to advanced-memory fab is utility-like infrastructure evidence."),
    Round37CaseCandidate("semiconductor_gas_fab_delay_4c", "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA", "GAS_FAB_4C", "Semiconductor gas fab delay 4C", "GLOBAL", "4c_thesis_break", ("fab_capex",), ("fab_delay", "plant_underutilization"), "Fab delay can break gas plant utilization."),
    Round37CaseCandidate("gas_supplier_customer_concentration_counterexample", "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA", "GAS_CONC", "Gas supplier customer concentration counterexample", "GLOBAL", "failed_rerating", ("ultrapure_gas",), ("customer_concentration", "contract_terms"), "Single fab/customer exposure caps visibility."),
    Round37CaseCandidate("advanced_memory_gas_contract_success_candidate", "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA", "MEM_GAS", "Advanced memory gas contract success candidate", "GLOBAL", "success_candidate", ("long_term_supply_contract", "take_or_pay", "advanced_memory_fab"), ("energy_cost", "fab_delay"), "Take-or-pay gas contract can support recurring utility-like revenue."),
    Round37CaseCandidate("lineage_cold_storage_reit_ipo_candidate", "COLD_CHAIN_REIT_LOGISTICS", "LINEAGE", "Lineage cold storage REIT IPO candidate", "US", "success_candidate", ("cold_storage", "reit_ipo", "temperature_controlled_logistics"), ("ipo_event_only", "funding_cost"), "IPO and scale are Stage 1; AFFO and occupancy must be validated."),
    Round37CaseCandidate("lineage_scale_but_net_loss_counterexample", "COLD_CHAIN_REIT_LOGISTICS", "LINEAGE_LOSS", "Lineage scale but net loss counterexample", "US", "failed_rerating", ("cold_storage",), ("capex", "funding_cost"), "Scale without AFFO quality is not rerating proof."),
    Round37CaseCandidate("cold_chain_energy_cost_4c", "COLD_CHAIN_REIT_LOGISTICS", "COLD_ENERGY_4C", "Cold chain energy cost 4C", "GLOBAL", "4c_thesis_break", ("temperature_controlled_logistics",), ("energy_cost_spike", "dividend_coverage_break"), "Energy-cost spike can break cold-storage economics."),
    Round37CaseCandidate("pharma_food_cold_chain_recurring_contract_candidate", "COLD_CHAIN_REIT_LOGISTICS", "COLD_RECUR", "Pharma food cold-chain recurring contract candidate", "GLOBAL", "success_candidate", ("long_term_tenant_contract", "noi_affo_growth", "occupancy"), ("tenant_concentration", "energy_cost"), "Recurring pharma/food contracts are stronger than logistics theme labels."),
    Round37CaseCandidate("data_center_water_reuse_tax_credit_candidate", "DATA_CENTER_WATER_REUSE_INFRA", "DC_WATER_TC", "Data center water reuse tax credit candidate", "US", "event_premium", ("datacenter_water_use", "water_reuse"), ("policy_dependency", "no_customer"), "Tax credit is an event signal until customer contracts appear."),
    Round37CaseCandidate("datacenter_water_opposition_4c", "DATA_CENTER_WATER_REUSE_INFRA", "DC_WATER_OPP_4C", "Datacenter water opposition 4C", "US", "4c_thesis_break", ("municipal_water_infra",), ("local_opposition", "permitting_denial"), "Local water opposition can break data-center projects."),
    Round37CaseCandidate("water_reuse_no_customer_counterexample", "DATA_CENTER_WATER_REUSE_INFRA", "WATER_NOCUST", "Water reuse no customer counterexample", "GLOBAL", "failed_rerating", ("water_reuse",), ("no_customer", "project_economics"), "Water-reuse theme without customer revenue remains weak."),
    Round37CaseCandidate("closed_loop_cooling_service_candidate", "DATA_CENTER_WATER_REUSE_INFRA", "CLOSED_LOOP", "Closed-loop cooling service candidate", "GLOBAL", "success_candidate", ("closed_loop_cooling", "recurring_service_revenue", "water_savings_metric"), ("project_economics", "policy_dependency"), "Closed-loop cooling can support Watch-to-Green when service revenue is visible."),
    Round37CaseCandidate("ses_airline_connectivity_backlog_candidate", "SATELLITE_CONNECTIVITY_INFRA", "SES_AIR", "SES airline connectivity backlog candidate", "EU", "success_candidate", ("airline_connectivity", "backlog_growth", "recurring_service_revenue"), ("capex_debt", "customer_concentration"), "Airline connectivity contracts and backlog are recurring service evidence."),
    Round37CaseCandidate("satellite_capex_debt_counterexample", "SATELLITE_CONNECTIVITY_INFRA", "SAT_DEBT", "Satellite capex debt counterexample", "GLOBAL", "failed_rerating", ("satellite_connectivity",), ("capex_debt", "debt_stress"), "Connectivity growth can be offset by capex/debt pressure."),
    Round37CaseCandidate("spacex_theme_no_revenue_counterexample", "SATELLITE_CONNECTIVITY_INFRA", "SPACEX_THEME", "SpaceX theme no revenue counterexample", "GLOBAL", "failed_rerating", ("satellite_connectivity",), ("spacex_theme_only", "customer_loss"), "SpaceX-related label without revenue is not score evidence."),
    Round37CaseCandidate("secure_comms_defense_connectivity_candidate", "SATELLITE_CONNECTIVITY_INFRA", "SAT_SECURE", "Secure comms defense connectivity candidate", "GLOBAL", "success_candidate", ("secure_comms", "airline_or_defense_contract"), ("launch_delay", "capex_debt"), "Defense secure communications can support recurring connectivity visibility."),
    Round37CaseCandidate("palantir_maven_contract_candidate", "DEFENSE_AI_SOFTWARE_INTELLIGENCE", "PLTR_MAVEN", "Palantir Maven contract candidate", "US", "success_candidate", ("government_software_contract", "maven_like_system"), ("procurement_delay", "ethical_regulation"), "Maven-like software contract is Stage 1-2; recurring program evidence unlocks higher conviction."),
    Round37CaseCandidate("defense_ai_prototype_no_program_counterexample", "DEFENSE_AI_SOFTWARE_INTELLIGENCE", "DEF_AI_PROTO", "Defense AI prototype no program counterexample", "GLOBAL", "failed_rerating", ("defense_ai",), ("prototype_only", "prototype_nonconversion"), "Prototype without program-of-record stays capped."),
    Round37CaseCandidate("ethical_regulation_defense_ai_4c", "DEFENSE_AI_SOFTWARE_INTELLIGENCE", "DEF_AI_ETH_4C", "Ethical regulation defense AI 4C", "GLOBAL", "4c_thesis_break", ("command_software",), ("ethical_regulatory_block", "budget_cut"), "Ethical/political restriction can break defense AI software."),
    Round37CaseCandidate("recurring_government_ai_platform_candidate", "DEFENSE_AI_SOFTWARE_INTELLIGENCE", "GOV_AI_RECUR", "Recurring government AI platform candidate", "GLOBAL", "success_candidate", ("program_of_record", "recurring_license", "gross_margin_visible"), ("budget_cycle", "customer_concentration"), "Program-of-record plus recurring license is stronger than AI headline."),
    Round37CaseCandidate("vertiv_data_center_power_infra_candidate", "AI_DATA_CENTER_POWER_EQUIPMENT", "VRT_POWER", "Vertiv data center power infra candidate", "US", "success_candidate", ("bookings_growth", "direct_datacenter_customer", "op_margin_improvement"), ("valuation_crowding", "ai_capex_delay"), "Data-center power equipment needs bookings, margin, and conversion evidence."),
    Round37CaseCandidate("power_equipment_bookings_slowdown_4c", "AI_DATA_CENTER_POWER_EQUIPMENT", "POWER_BOOK_4C", "Power equipment bookings slowdown 4C", "GLOBAL", "4c_thesis_break", ("datacenter_power_density",), ("bookings_slowdown", "margin_miss"), "Bookings slowdown or margin miss can break AI power equipment thesis."),
    Round37CaseCandidate("low_margin_power_project_counterexample", "AI_DATA_CENTER_POWER_EQUIPMENT", "PWR_LOWMARGIN", "Low-margin power project counterexample", "GLOBAL", "failed_rerating", ("switchgear", "modular_power"), ("low_margin_project", "supply_chain"), "AI power project is weak if margin is low."),
    Round37CaseCandidate("ups_pdu_service_revenue_candidate", "AI_DATA_CENTER_POWER_EQUIPMENT", "UPS_PDU_SERVICE", "UPS PDU service revenue candidate", "GLOBAL", "success_candidate", ("ups", "pdu", "service_revenue"), ("ai_capex_delay", "bookings_slowdown"), "Service revenue can make power equipment more recurring."),
    Round37CaseCandidate("aerovironment_bluehalo_counter_uas_candidate", "DEFENSE_DRONE_COUNTER_UAS", "AVAV_BLUE", "AeroVironment BlueHalo counter-UAS candidate", "US", "success_candidate", ("counter_uas", "military_delivery_contract", "backlog_growth"), ("mna_dilution", "production_capacity"), "Counter-UAS expansion needs backlog and delivery, not M&A headline alone."),
    Round37CaseCandidate("avav_mna_dilution_risk_counterexample", "DEFENSE_DRONE_COUNTER_UAS", "AVAV_DILUTION", "AVAV M&A dilution risk counterexample", "US", "failed_rerating", ("counter_uas",), ("mna_dilution", "mna_dilution_unwind"), "M&A can dilute or disappoint despite strategic fit."),
    Round37CaseCandidate("switchblade_long_term_contract_candidate", "DEFENSE_DRONE_COUNTER_UAS", "SWITCHBLADE", "Switchblade long-term contract candidate", "US", "success_candidate", ("loitering_munition", "idiq_framework", "production_capacity"), ("export_control", "program_delay"), "Loitering munition needs long-term delivery contract and production capacity."),
    Round37CaseCandidate("drone_prototype_no_mass_production_counterexample", "DEFENSE_DRONE_COUNTER_UAS", "DRONE_PROTO", "Drone prototype no mass production counterexample", "GLOBAL", "failed_rerating", ("loitering_munition",), ("prototype_only", "production_shortfall"), "Prototype without mass production should not become Green."),
)


def target_for(target_id: str) -> Round37ScoreTarget | None:
    for target in ROUND37_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round37_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND37_CASE_CANDIDATES:
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
                f"Round37 v2.2 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4b_evidence=candidate.red_flag_fields if candidate.case_type == "4b_watch" else (),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"success_candidate", "structural_success", "cyclical_success"} else None,
            score_price_alignment="unknown",
            rerating_result="thesis_break" if candidate.case_type == "4c_thesis_break" else "unknown",
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
                "theme_label_is_not_score_evidence",
                "do_not_invent_contracts_backlog_or_prices",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Validation group: {target.validation_group}.",
            price_validation=PriceValidation(price_validation_status="needs_price_backfill"),
            data_quality=CaseDataQuality(False, False, False, 0.0),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round37_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND37_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "validation_group": target.validation_group,
                "eps_fcf": str(weights["eps_fcf"]),
                "structural_visibility": str(weights["structural_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "market_mispricing": str(weights["market_mispricing"]),
                "valuation": str(weights["valuation"]),
                "capital_allocation": str(weights["capital_allocation"]),
                "information_confidence": str(weights["information_confidence"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "validation_metrics": "|".join(target.validation_metrics),
                "success_criteria": target.success_criteria,
                "failure_criteria": target.failure_criteria,
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round37_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND37_CASE_CANDIDATES:
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
                "validation_group": target.validation_group,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "price_validation_status": "needs_price_backfill",
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round37_summary() -> dict[str, int | bool]:
    records = round37_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success", "cyclical_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND37_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND37_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND37_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND37_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round37_score_weight_reports(
    *,
    output_directory: str | Path = ROUND37_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND37_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND37_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round37_score_weight_v22_summary.md",
        "case_matrix": output / "round37_case_candidate_matrix.csv",
        "green_guardrails": output / "round37_green_guardrail_review.md",
        "validation_plan": output / "round37_archetype_price_validation_plan.md",
        "defense_tech": output / "round37_defense_tech_review.md",
        "utility_infra": output / "round37_utility_infra_review.md",
        "recurring_platform": output / "round37_recurring_platform_review.md",
    }
    _write_case_jsonl(round37_case_records(), cases)
    _write_rows(round37_score_profile_rows(), score_profiles)
    _write_rows(round37_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round37_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round37_green_guardrail_markdown(), encoding="utf-8")
    paths["validation_plan"].write_text(render_round37_validation_plan_markdown(), encoding="utf-8")
    paths["defense_tech"].write_text(render_round37_defense_tech_markdown(), encoding="utf-8")
    paths["utility_infra"].write_text(render_round37_utility_infra_markdown(), encoding="utf-8")
    paths["recurring_platform"].write_text(render_round37_recurring_platform_markdown(), encoding="utf-8")
    return paths


def render_round37_summary_markdown() -> str:
    summary = round37_summary()
    lines = [
        "# Round-37 Score-Weight Validation v2.2 Summary",
        "",
        f"- source_round: `{ROUND37_SOURCE_ROUND_PATH}`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- counterexample_or_risk_count: {summary['counterexample_or_risk_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "- Round 37 adds cases_v19 and v2.2 validation plans.",
        "- Example: defense autonomous systems need framework, actual procurement, production capacity, and EPS conversion.",
        "- Example: semiconductor industrial gases behave like fab utility infrastructure only when long-term onsite contracts are explicit.",
        "- Example: satellite connectivity needs recurring service revenue and backlog, not a SpaceX-related label.",
        "- Theme names, case IDs, private valuations, prototypes, and price rallies are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round37_green_guardrail_markdown() -> str:
    lines = [
        "# Round-37 Green Guardrail Review",
        "",
        "| target | posture | validation_group | Green unlock evidence | Red flags |",
        "|---|---|---|---|---|",
    ]
    for target in ROUND37_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | {target.validation_group} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v2.2 weights to production scoring yet.",
            "- Do not use case IDs, theme labels, private valuations, prototypes, or SpaceX/AI/defense labels as candidate-generation input.",
            "- Do not invent stage dates, prices, contract terms, backlog, AFFO, water savings, recurring revenue, or program renewals.",
            "- Do not lower Stage 3-Green thresholds to improve recall.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round37_validation_plan_markdown() -> str:
    lines = [
        "# Round-37 Archetype Price Validation Plan",
        "",
        "Round 37 expands score-price validation for backlog, utility-like infrastructure, and recurring software/platform archetypes.",
        "",
        "| target | validation_group | metrics | success | failure |",
        "|---|---|---|---|---|",
    ]
    for target in ROUND37_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.validation_group} | {', '.join(target.validation_metrics)} | "
            f"{target.success_criteria} | {target.failure_criteria} |"
        )
    lines.extend(
        [
            "",
            "## Group Rules",
            "- backlog_contract: validate contract-to-backlog-to-revenue conversion, OP/EPS revisions, and MFE/MAE after Stage 2.",
            "- utility_like_infra/reit_utility_like/infra_utility_like: validate occupancy, plant/facility utilization, AFFO/FCF, and funding or energy cost.",
            "- software_recurring: validate recurring revenue, gross margin, RPO/backlog, churn or renewal, and legal/security drawdowns.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round37_defense_tech_markdown() -> str:
    return "\n".join(
        [
            "# Round-37 Defense Tech Review",
            "",
            "Defense tech can be Green-possible, but only after procurement and delivery evidence.",
            "",
            "## Autonomous / Containerized Munitions",
            "- Needs framework agreement, actual procurement quantity, production capacity, delivery schedule, and OP/EPS revision.",
            "- Prototype or private valuation alone is not score evidence.",
            "",
            "## Defense AI Software",
            "- Needs government software contract, program-of-record conversion, recurring license, and gross margin evidence.",
            "- Ethical, budget, and procurement risks are explicit RedTeam gates.",
            "",
            "## Counter-UAS / Drone",
            "- Needs military delivery contract, IDIQ/framework, production capacity, backlog, and EPS revision.",
            "- M&A dilution and export-control risk must be tracked.",
        ]
    ) + "\n"


def render_round37_utility_infra_markdown() -> str:
    return "\n".join(
        [
            "# Round-37 Utility / Physical Infrastructure Review",
            "",
            "Round 37 separates physical infrastructure cash-flow evidence from narrative labels.",
            "",
            "## Industrial Gases",
            "- Onsite gas plant, long-term supply, take-or-pay, and fab ramp schedules can create utility-like visibility.",
            "- Fab delay and customer concentration are 4C-style risks.",
            "",
            "## Cold Chain",
            "- Occupancy, NOI/AFFO, energy cost, debt cost, and dividend coverage matter more than IPO scale.",
            "",
            "## Data-Center Water Reuse",
            "- Water-savings contracts and recurring service revenue are needed.",
            "- Local opposition, permitting, policy dependency, and no-customer risk block Green.",
        ]
    ) + "\n"


def render_round37_recurring_platform_markdown() -> str:
    return "\n".join(
        [
            "# Round-37 Recurring Platform Review",
            "",
            "Satellite and AI power equipment need recurring economics or backlog conversion, not theme labels.",
            "",
            "## Satellite Connectivity",
            "- Airline, maritime, or defense connectivity contracts plus recurring service revenue and backlog can support Watch-to-Green.",
            "- SpaceX-related label, launch delay, capex/debt pressure, and constellation competition cap Green.",
            "",
            "## AI Data-Center Power Equipment",
            "- Bookings, backlog, direct data-center exposure, service revenue, and margin conversion are the core checks.",
            "- Bookings slowdown, low-margin projects, AI capex cuts, and supply-chain issues are 4B/4C gates.",
        ]
    ) + "\n"


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
    "ROUND37_CASE_CANDIDATES",
    "ROUND37_DEFAULT_CASES_PATH",
    "ROUND37_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND37_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND37_SCORE_TARGETS",
    "ROUND37_SOURCE_ROUND_PATH",
    "Round37CaseCandidate",
    "Round37ScoreTarget",
    "Round37ScoreWeightDraft",
    "render_round37_defense_tech_markdown",
    "render_round37_green_guardrail_markdown",
    "render_round37_recurring_platform_markdown",
    "render_round37_summary_markdown",
    "render_round37_utility_infra_markdown",
    "render_round37_validation_plan_markdown",
    "round37_case_candidate_rows",
    "round37_case_records",
    "round37_score_profile_rows",
    "round37_summary",
    "target_for",
    "write_round37_score_weight_reports",
]
