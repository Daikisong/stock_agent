"""Round-174 R3 Loop-11 Korea battery, EV, and green-energy pack.

Round 174 applies Loop 11 to Korea-listed battery cell, ESS, cathode/anode,
separator, electrolyte, lithium/resource-security, and battery-material
overheat cases. It is calibration/report material only. Production feature
engineering, scoring, staging, and RedTeam code must not import it.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND174_SOURCE_ROUND_PATH = "docs/round/round_174.md"
ROUND174_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round174_r3_loop11_battery_ev_green"
ROUND174_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop11_round174.jsonl"
ROUND174_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round174_r3_loop11_v11.csv"
ROUND174_SOURCE_CANONICAL_TARGET_IDS: tuple[str, ...] = (
    "ESS_LFP_GRID_STORAGE_KOREA",
    "EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA",
    "ANODE_GRAPHITE_SUPPLYCHAIN_KOREA",
    "CATHODE_LONG_CONTRACT_VISIBILITY",
    "LITHIUM_RESOURCE_SECURITY_KOREA",
    "BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA",
    "SEPARATOR_EV_DEMAND_CYCLE",
    "ELECTROLYTE_CAPA_SUPPLYCHAIN",
    "SILICON_ANODE_COMMERCIALIZATION",
    "EVENT_LITHIUM_PRICE_RALLY",
    "CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK",
    "DISCLOSURE_CONFIDENCE_CAP",
)
ROUND174_SOURCE_CANONICAL_TARGET_COUNT = len(ROUND174_SOURCE_CANONICAL_TARGET_IDS)


@dataclass(frozen=True)
class Round174ScoreWeightDraft:
    eps_fcf_opm: int | str
    contract_visibility: int | str
    capa_utilization_line_conversion: int | str
    structural_demand_shift: int | str
    early_price_validation: int | str
    safety_regulatory_disclosure: int | str
    valuation_4b_room: int | str

    def as_dict(self) -> dict[str, int | str]:
        return {
            "eps_fcf_opm": self.eps_fcf_opm,
            "contract_visibility": self.contract_visibility,
            "capa_utilization_line_conversion": self.capa_utilization_line_conversion,
            "structural_demand_shift": self.structural_demand_shift,
            "early_price_validation": self.early_price_validation,
            "safety_regulatory_disclosure": self.safety_regulatory_disclosure,
            "valuation_4b_room": self.valuation_4b_room,
        }


@dataclass(frozen=True)
class Round174ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round174ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop11_penalty_axes: tuple[str, ...]
    normalization_point: str
    hard_gate: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.BATTERY_EV_GREEN

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round174CaseCandidate:
    case_id: str
    target_id: str
    symbol: str
    company_name: str
    market: str
    case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    alignment_hint: str
    price_validation_status: str
    source_refs: tuple[str, ...]
    notes: str
    secondary_archetypes: tuple[E2RArchetype, ...] = ()

    @property
    def expected_group(self) -> str:
        return self.case_type


@dataclass(frozen=True)
class Round174BaseScoreWeight:
    component: str
    points: int
    loop11_direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "component": self.component,
            "points": str(self.points),
            "loop11_direction": self.loop11_direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round174StageCap:
    stage_band: str
    max_score: str
    required_evidence: tuple[str, ...]
    example_cases: tuple[str, ...]
    green_policy: str

    def as_row(self) -> dict[str, str]:
        return {
            "stage_band": self.stage_band,
            "max_score": self.max_score,
            "required_evidence": "|".join(self.required_evidence),
            "example_cases": "|".join(self.example_cases),
            "green_policy": self.green_policy,
        }


@dataclass(frozen=True)
class Round174ScoreStagePriceAlignment:
    case_id: str
    detected_stage: str
    price_path_status: str
    verdict: str
    normalization_adjustment: str

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "detected_stage": self.detected_stage,
            "price_path_status": self.price_path_status,
            "verdict": self.verdict,
            "normalization_adjustment": self.normalization_adjustment,
        }


ROUND174_BASE_SCORE_WEIGHTS: tuple[Round174BaseScoreWeight, ...] = (
    Round174BaseScoreWeight("eps_fcf_opm_conversion", 24, "keep_high", "Stage 3 requires OP/EPS/FCF and margin conversion, not EV or ESS keywords."),
    Round174BaseScoreWeight("contract_visibility", 22, "raise_detail_requirement", "Customer, amount, GWh/tonnage, period, production start, offtake, and JV stake drive Stage 2."),
    Round174BaseScoreWeight("capa_utilization_line_conversion", 14, "raise_after_ev_slowdown", "After EV slowdown, installed CAPA is not a positive unless it can be utilized or converted."),
    Round174BaseScoreWeight("structural_demand_shift", 12, "focus_ess_supply_chain_security", "EV-to-ESS, data-center power, graphite security, and resource security matter when they convert to earnings."),
    Round174BaseScoreWeight("early_price_path_validation", 10, "loop11_axis", "The score must test 60D/120D price validation and avoid late event-rally chasing."),
    Round174BaseScoreWeight("safety_regulatory_disclosure_confidence", 8, "hard_review", "Safety, regulation, disclosure gaps, customer secrecy, and non-binding terms cap Stage 3."),
    Round174BaseScoreWeight("valuation_room_4b_runway", 10, "raise_4b_focus", "Battery materials often require 4B cooling when policy or commodity events drive price before revisions."),
)


ROUND174_STAGE_CAPS: tuple[Round174StageCap, ...] = (
    Round174StageCap(
        "Stage 1",
        "45",
        ("ev_growth", "ess_growth", "lithium_rebound", "graphite_tariff", "cathode_anode_separator_electrolyte_theme"),
        ("lnf_lithium_event_rally_case",),
        "Theme keywords route research only. Green is blocked before contract, utilization, margin, and FCF evidence.",
    ),
    Round174StageCap(
        "Stage 2",
        "70",
        ("contract_amount", "customer_name", "gwh_or_tonnage", "supply_period", "offtake_or_jv_stake", "production_start"),
        ("samsung_sdi_ess_lfp_stage2_case", "posco_holdings_lithium_resource_stage2_case"),
        "Stage 2 can be strong, but Stage 3 waits for OPM, utilization, revenue recognition, and repeat orders.",
    ),
    Round174StageCap(
        "Stage 2 strong",
        "watch",
        ("large_contract", "line_conversion", "price_reaction", "customer_or_use_case_visible", "stage3_fields_pending"),
        ("samsung_sdi_ess_lfp_stage2_case",),
        "Diagnostic band only. It is not canonical Stage 3 and cannot override missing OPM/utilization.",
    ),
    Round174StageCap(
        "Stage 3",
        "requires_4_of_7",
        ("confirmed_customer_amount_period", "op_eps_revision_or_beat", "ev_capa_to_ess_conversion", "utilization_recovery", "60d_mfe_20pct", "opm_defended_despite_raw_materials", "repeat_contract_or_new_customer"),
        ("samsung_sdi_ess_lfp_stage2_case",),
        "Stage 3 is possible only when contracts and utilization convert into earnings and price path before 4B.",
    ),
    Round174StageCap(
        "Stage 4B",
        "requires_3_of_5",
        ("stage2_120d_mfe_80pct", "one_day_event_rally_10_20pct", "policy_or_commodity_event_drives_price", "op_eps_revision_lags_price", "lithium_graphite_ess_keyword_crowding"),
        ("posco_future_m_graphite_tariff_4b_case", "lnf_lithium_event_rally_case"),
        "Policy, tariff, and commodity rallies are cooled when earnings cannot follow.",
    ),
    Round174StageCap(
        "Stage 4C",
        "hard_gate",
        ("customer_contract_cancelled", "factory_idle_or_utilization_collapse", "sale_review_or_restructuring", "automaker_ev_strategy_retreat", "lithium_nickel_price_crash_inventory_loss", "customer_terms_undisclosed", "operating_loss_persistent"),
        ("skiet_separator_sale_review_4c_case", "ecopro_materials_ev_slowdown_4c_case"),
        "Hard RedTeam overrides battery growth narratives when EV demand, utilization, customer strategy, or losses break the path.",
    ),
)


ROUND174_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round174ScoreStagePriceAlignment, ...] = (
    Round174ScoreStagePriceAlignment("samsung_sdi_ess_lfp_stage2_case", "Stage 2 strong", "Contract day +6.1% reference reaction; KRX exact price path needs backfill", "stage2_strong_not_green_yet", "credit contract value, period, ESS line conversion; cap customer undisclosed and OPM/utilization missing"),
    Round174ScoreStagePriceAlignment("posco_future_m_graphite_tariff_4b_case", "Stage 2 + 4B-watch", "Graphite offtake is Stage 2; tariff +20% is event-rally 4B watch", "supply_chain_event_not_green", "credit graphite supply security; haircut quarterly pricing, anode OPM missing, and tariff rally"),
    Round174ScoreStagePriceAlignment("posco_holdings_lithium_resource_stage2_case", "Stage 2", "$765m lithium JV stake is resource security, but lithium cycle caps Green", "resource_security_with_cycle_cap", "credit named mines and stake; cap before offtake economics, FCF, and low-cost proof"),
    Round174ScoreStagePriceAlignment("lg_chem_cathode_toyota_stage2_case", "Stage 2", "Toyota Tsusho stake reduces China dependency but plant OPM and utilization remain pending", "supply_chain_realign_not_green_yet", "credit ownership realignment; cap before customer contract, utilization, and FCF"),
    Round174ScoreStagePriceAlignment("lg_chem_exxon_non_binding_lithium_case", "Stage 1/2 option", "Non-binding lithium deal is not final offtake", "non_binding_cap_correct", "support research routing; block Stage 3 before final terms"),
    Round174ScoreStagePriceAlignment("lnf_lithium_event_rally_case", "Stage 1 event / 4B-watch", "CATL mine suspension +10% reference move is commodity event premium", "event_rally_not_structural", "credit price reaction only lightly; block Green without contract, margin, and demand evidence"),
    Round174ScoreStagePriceAlignment("skiet_separator_sale_review_4c_case", "4C-watch", "EV slowdown, SK On losses, and sale review break separator demand visibility", "hard_redteam_alignment", "apply separator utilization and parent restructuring penalty"),
    Round174ScoreStagePriceAlignment("ecopro_materials_ev_slowdown_4c_case", "4C-watch", "Weak EV demand, operating losses, and Ford EV strategy shock hit the material thesis", "customer_strategy_break", "apply EV demand slowdown, loss, and customer strategy risk gates"),
    Round174ScoreStagePriceAlignment("enchem_electrolyte_capa_watch_case", "Watch", "Electrolyte CAPA needs customer, OPM, and price path backfill", "watch_not_green_yet", "cap before contract and margin evidence"),
    Round174ScoreStagePriceAlignment("daejoo_silicon_anode_commercialization_case", "Stage 1/2 watch", "Silicon anode commercialization needs customer qualification and volume revenue", "commercialization_not_green_yet", "cap before commercial volume, ASP, and margin proof"),
)


def _weights(
    eps: int | str,
    contract: int | str,
    capa: int | str,
    demand: int | str,
    price: int | str,
    safety: int | str,
    valuation: int | str,
) -> Round174ScoreWeightDraft:
    return Round174ScoreWeightDraft(eps, contract, capa, demand, price, safety, valuation)


ROUND174_SCORE_TARGETS: tuple[Round174ScoreTarget, ...] = (
    Round174ScoreTarget(
        "ESS_LFP_GRID_STORAGE_KOREA",
        E2RArchetype.ESS_LFP_GRID_STORAGE_KOREA,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(24, 22, 14, 12, 10, 8, 10),
        ("ess_growth", "lfp_ess", "data_center_power", "ev_line_conversion"),
        ("ess_contract_value", "supply_period", "production_start_2027", "line_conversion", "price_reaction"),
        ("ess_revenue_recognition", "ess_opm", "converted_line_utilization", "repeat_ess_contract", "fcf_improvement"),
        ("ess_basket_crowded", "contract_priced_before_margin"),
        ("customer_undisclosed", "line_conversion_delay", "ess_margin_miss", "revenue_recognition_delay"),
        ("customer_or_use_case", "contract_value", "supply_period", "utilization", "ess_opm", "fcf_conversion"),
        ("customer_undisclosed", "opm_missing", "utilization_missing", "line_conversion_delay"),
        ("customer_disclosure", "opm_utilization", "line_conversion"),
        "Samsung SDI-style ESS LFP contract is Stage 2 strong, but Stage 3 waits for OPM, utilization, revenue recognition, and repeat contracts.",
    ),
    Round174ScoreTarget(
        "EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA",
        E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(20, 19, 18, 14, 9, 8, 8),
        ("ev_demand_slowdown", "ev_line_to_ess", "storage_redeployment"),
        ("line_conversion_plan", "ess_customer_contract", "converted_line_capacity", "production_start"),
        ("converted_line_utilization", "ess_opm", "ev_idle_cost_offset", "fcf_conversion"),
        ("ev_failure_reframed_as_ess_crowded", "redeployment_priced_before_utilization"),
        ("conversion_cost_increase", "low_utilization", "ess_contract_absent", "ev_write_down_continues"),
        ("ess_customer_contract", "converted_line_utilization", "ess_opm", "fcf_conversion"),
        ("low_utilization", "conversion_cost", "contract_absent", "ev_write_down"),
        ("utilization", "conversion_cost", "contract_absent"),
        "EV-to-ESS redeployment is positive only if idle EV fixed cost is offset by real ESS contracts, utilization, and margin.",
    ),
    Round174ScoreTarget(
        "ANODE_GRAPHITE_SUPPLYCHAIN_KOREA",
        E2RArchetype.ANODE_GRAPHITE_SUPPLYCHAIN_KOREA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(20, 22, 12, 16, 10, 8, 8),
        ("graphite_dependency", "us_graphite_tariff", "ira_feoc_supply_chain", "anode_material"),
        ("six_year_graphite_offtake", "monthly_tonnage", "expansion_option", "quarterly_price_negotiation"),
        ("anode_revenue", "gross_margin", "customer_reorder", "china_substitution_actual", "fcf"),
        ("tariff_event_rally_20pct", "graphite_keyword_crowded"),
        ("quality_or_supply_capacity_issue", "quarterly_pricing_margin_risk", "anode_opm_missing", "customer_adoption_missing"),
        ("graphite_offtake", "tonnage", "customer_adoption", "anode_margin", "fcf_conversion"),
        ("opm_missing", "quality_risk", "quarterly_price_risk", "event_rally"),
        ("event_rally", "pricing_risk", "opm_missing"),
        "Graphite supply security is Stage 2 evidence; tariff-driven rallies need 4B-watch before anode revenue and margin are visible.",
    ),
    Round174ScoreTarget(
        "CATHODE_LONG_CONTRACT_VISIBILITY",
        E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(21, 22, 12, 12, 9, 8, 8),
        ("cathode_contract", "cathode_plant_ownership", "north_america_supply_chain", "china_dependency_reduction"),
        ("long_term_order", "customer_name", "plant_stake_realign", "ownership_change", "supply_chain_realignment"),
        ("plant_utilization", "customer_contract", "opm_fcf_improvement", "lithium_pass_through_stable"),
        ("cathode_policy_rally", "ownership_event_priced_before_margin"),
        ("asp_linked_to_lithium_downturn", "margin_compression", "customer_concentration", "opm_missing"),
        ("customer_contract", "plant_utilization", "opm_fcf", "price_pass_through"),
        ("opm_missing", "customer_concentration", "lithium_asp_downturn", "margin_compression"),
        ("margin", "lithium_price", "customer_concentration"),
        "Cathode visibility requires long-term orders plus margin and utilization, not just ownership or supply-chain realignment.",
    ),
    Round174ScoreTarget(
        "LITHIUM_RESOURCE_SECURITY_KOREA",
        E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(18, 20, 10, 16, 8, 8, 8),
        ("lithium_resource_security", "mine_stake", "spodumene", "offtake"),
        ("mine_name", "jv_stake", "deal_value", "spodumene_rights"),
        ("low_cost_offtake", "material_margin_improvement", "fcf_improvement", "cycle_bottom_evidence"),
        ("resource_security_narrative_priced", "lithium_rebound_crowded"),
        ("lithium_price_long_weakness", "impairment", "capex_burden", "offtake_economics_missing"),
        ("offtake_economics", "low_cost_structure", "margin_benefit", "fcf_improvement"),
        ("lithium_cycle", "impairment", "capex_burden", "offtake_missing"),
        ("commodity_cycle", "capex", "impairment"),
        "Lithium resource security is Stage 2; commodity cycle and FCF proof cap Stage 3.",
    ),
    Round174ScoreTarget(
        "BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA",
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights(14, 12, 10, 8, 8, 8, 6),
        ("precursor_vertical_integration", "cathode_material_capa", "ipo_or_capa_narrative"),
        ("ipo", "capa_expansion", "customer_supply_chain_exposure"),
        ("not_green_until_utilization_margin_fcf_and_customer_demand_recover",),
        ("retail_investor_rally", "materials_theme_crowded", "capa_narrative_priced"),
        ("weak_ev_demand", "mineral_price_drop", "operating_loss", "customer_strategy_retreat", "capa_overbuild"),
        ("utilization", "margin", "fcf", "customer_demand"),
        ("weak_ev_demand", "operating_loss", "customer_strategy_risk", "mineral_price_drop"),
        ("ev_demand", "losses", "customer_strategy", "capa_overbuild"),
        "Battery materials CAPA is RedTeam-first in Loop 11 because EV demand and mineral prices can break the story quickly.",
    ),
    Round174ScoreTarget(
        "SEPARATOR_EV_DEMAND_CYCLE",
        E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights(12, 12, 8, 8, 7, 8, 5),
        ("separator_demand", "ev_battery_shipments", "panasonic_or_sk_on_customer"),
        ("separator_customer_exposure", "capacity_plan", "utilization_signal"),
        ("not_green_until_utilization_margin_and_customer_diversification_recover",),
        ("separator_rebound_priced_before_ev_recovery",),
        ("ev_demand_slowdown", "sk_on_loss_expansion", "sale_review", "utilization_risk", "customer_capex_cut"),
        ("utilization_recovery", "margin", "customer_diversification"),
        ("ev_demand_slowdown", "sale_review", "utilization_risk", "loss_expansion"),
        ("ev_demand", "utilization", "sale_review"),
        "Separator exposure is Watch/Red because EV battery shipment slowdown directly hits utilization.",
    ),
    Round174ScoreTarget(
        "ELECTROLYTE_CAPA_SUPPLYCHAIN",
        E2RArchetype.ELECTROLYTE_CAPA_SUPPLYCHAIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(18, 17, 12, 10, 8, 8, 7),
        ("electrolyte_capa", "electrolyte_supply_chain", "customer_capa_plan"),
        ("customer_contract", "capa_ramp", "regional_supply_chain", "shipment_schedule"),
        ("electrolyte_revenue", "opm", "customer_diversification", "fcf_conversion"),
        ("electrolyte_capa_theme_crowded",),
        ("customer_contract_missing", "price_pressure", "utilization_miss", "single_customer"),
        ("customer_contract", "shipment", "opm", "fcf_conversion"),
        ("contract_missing", "utilization_miss", "price_pressure"),
        ("contract_missing", "utilization", "price_pressure"),
        "Electrolyte CAPA can be Stage 1/2; Green waits for customer, OPM, and FCF backfill.",
    ),
    Round174ScoreTarget(
        "SILICON_ANODE_COMMERCIALIZATION",
        E2RArchetype.SILICON_ANODE_COMMERCIALIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(17, 16, 13, 10, 8, 8, 7),
        ("silicon_anode", "energy_density", "potential_cell_customers"),
        ("customer_qualification", "pilot_volume", "commercialization_schedule"),
        ("commercial_volume_revenue", "asp_margin", "customer_diversification", "op_eps_revision"),
        ("silicon_anode_theme_crowded", "commercialization_priced_before_volume"),
        ("qualification_delay", "commercial_volume_missing", "margin_unknown", "cash_burn"),
        ("commercial_volume", "customer_qualification", "asp_margin", "op_eps_revision"),
        ("commercial_volume_missing", "qualification_delay", "margin_unknown"),
        ("commercialization", "volume", "margin"),
        "Silicon anode is Stage 1/2 before commercial volume and margin proof.",
    ),
    Round174ScoreTarget(
        "EVENT_LITHIUM_PRICE_RALLY",
        E2RArchetype.EVENT_LITHIUM_PRICE_RALLY,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("event", "event", "event", "event", "event", "event", "event"),
        ("catl_mine_suspension", "lithium_price_rebound", "battery_materials_price_rally"),
        ("one_day_10pct_rally", "sentiment_driven_lithium_supply_shock"),
        ("not_green_without_contract_margin_fcf_customer_demand",),
        ("one_day_10_20pct_event_rally", "lithium_keyword_crowding"),
        ("mine_license_renewed", "supply_resumes", "lithium_price_redeclines", "op_eps_not_following"),
        (),
        ("event_rally_only", "contract_missing", "margin_missing", "demand_missing"),
        ("event_rally", "commodity_cycle", "op_eps_missing"),
        "Lithium mine suspension rallies are event premium, not structural Stage 3 evidence.",
        hard_gate=True,
    ),
    Round174ScoreTarget(
        "CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK",
        E2RArchetype.CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("customer_strategy_change", "ev_model_cancel", "supply_contract_review", "battery_content_cut"),
        ("risk_event_detected",),
        ("not_green_until_customer_strategy_and_contract_visibility_recovered",),
        ("positive_capa_story_ignores_customer_strategy_risk",),
        ("customer_contract_cancelled", "automaker_ev_retreat", "factory_idle", "operating_loss", "expected_revenue_loss"),
        ("customer_strategy_stable", "contract_reaffirmed", "utilization_recovered"),
        ("customer_strategy_risk", "contract_cancelled", "factory_idle", "losses"),
        ("customer_strategy_risk", "contract_cancelled", "factory_idle", "losses"),
        "Customer EV strategy retreat and contract cancellation are hard 4C gates.",
        hard_gate=True,
    ),
    Round174ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("cap", "cap", "cap", "cap", "cap", "+", "cap"),
        ("battery_contract_headline", "opendart_list_only", "customer_confidential"),
        ("detail_fetched", "contract_amount", "counterparty", "contract_period", "gwh_or_tonnage"),
        ("multi_source_confirmation", "contract_terms_verified", "opm_utilization_visible"),
        ("undisclosed_battery_contract_theme_crowded",),
        ("customer_undisclosed", "amount_missing", "period_missing", "margin_unknown", "production_start_unknown"),
        ("customer", "amount", "period", "gwh_or_tonnage", "opm", "utilization"),
        ("detail_missing", "customer_undisclosed", "margin_unknown", "production_start_unknown"),
        ("disclosure_confidence", "detail_missing"),
        "Battery contract headlines cannot support Stage 3-Green until customer, amount, period, GWh/tonnage, margin, and utilization are verified.",
    ),
)


ROUND174_CASE_CANDIDATES: tuple[Round174CaseCandidate, ...] = (
    Round174CaseCandidate(
        "samsung_sdi_ess_lfp_stage2_case",
        "ESS_LFP_GRID_STORAGE_KOREA",
        "006400",
        "Samsung SDI ESS LFP",
        "KR",
        "success_candidate",
        date(2025, 12, 9),
        date(2025, 12, 9),
        None,
        None,
        None,
        ("ess_lfp_contract", "contract_value_2tn_krw_plus", "delivery_start_2027", "three_year_supply", "line_conversion", "price_reaction_6_1pct"),
        ("customer_undisclosed", "ess_opm_missing", "utilization_missing", "revenue_recognition_delay"),
        "stage2_strong_price_aligned_but_stage3_cap",
        "needs_price_backfill",
        ("round_174.md Reuters Samsung SDI ESS LFP contract",),
        "Clean R3 Stage 2 strong case. Stage 3 waits for customer detail, ESS OPM, converted-line utilization, repeat contracts, and FCF.",
        (E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
    ),
    Round174CaseCandidate(
        "posco_future_m_graphite_tariff_4b_case",
        "ANODE_GRAPHITE_SUPPLYCHAIN_KOREA",
        "003670",
        "POSCO Future M graphite supply chain",
        "KR",
        "4b_watch",
        date(2024, 2, 29),
        date(2024, 2, 29),
        None,
        None,
        None,
        ("syrah_six_year_graphite_offtake", "balama_natural_graphite", "2kt_month_initial", "5kt_month_expansion_option", "quarterly_price_negotiation", "us_graphite_tariff_93_5pct", "price_reaction_20pct"),
        ("anode_opm_missing", "quality_supply_capacity_caveat", "quarterly_pricing_margin_risk", "event_rally_4b_watch"),
        "graphite_supply_stage2_plus_tariff_event_4b_watch",
        "needs_price_backfill",
        ("round_174.md Reuters Syrah-POSCO Future M offtake", "round_174.md FT graphite tariff rally"),
        "Actual graphite offtake is Stage 2, but tariff-driven +20% rally is event premium until anode revenue, margin, and reorder evidence appear.",
        (E2RArchetype.BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY, E2RArchetype.EVENT_LITHIUM_PRICE_RALLY),
    ),
    Round174CaseCandidate(
        "posco_holdings_lithium_resource_stage2_case",
        "LITHIUM_RESOURCE_SECURITY_KOREA",
        "005490",
        "POSCO Holdings lithium resource security",
        "KR",
        "success_candidate",
        date(2025, 11, 11),
        date(2025, 11, 11),
        None,
        None,
        None,
        ("minres_765m_usd_lithium_jv_stake", "wodgina", "mt_marion", "spodumene_rights", "first_australia_lithium_mine_entry"),
        ("lithium_price_cycle", "offtake_economics_missing", "fcf_impact_missing", "capex_balance_sheet_risk"),
        "resource_security_stage2_with_commodity_cycle_cap",
        "needs_price_backfill",
        ("round_174.md Reuters MinRes POSCO lithium JV stake",),
        "Resource security is Stage 2, but lithium price cycle and FCF proof cap Stage 3.",
        (E2RArchetype.LITHIUM_CYCLE_OVERLAY,),
    ),
    Round174CaseCandidate(
        "lg_chem_cathode_toyota_stage2_case",
        "CATHODE_LONG_CONTRACT_VISIBILITY",
        "051910",
        "LG Chem cathode ownership realignment",
        "KR",
        "success_candidate",
        date(2025, 9, 8),
        date(2025, 9, 8),
        None,
        None,
        None,
        ("toyota_tsusho_25pct_stake", "huayou_cobalt_stake_reduced", "cathode_plant_realignment", "china_dependency_reduction"),
        ("opm_missing", "plant_utilization_missing", "customer_contract_missing", "fcf_missing"),
        "cathode_supplychain_realign_stage2_not_green",
        "needs_price_backfill",
        ("round_174.md Reuters Toyota Tsusho LG Chem cathode stake",),
        "Cathode supply-chain realignment is Stage 2 evidence, not Stage 3 before plant utilization, customer contract, OPM, and FCF.",
        (E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA,),
    ),
    Round174CaseCandidate(
        "lg_chem_exxon_non_binding_lithium_case",
        "LITHIUM_RESOURCE_SECURITY_KOREA",
        "051910",
        "LG Chem-Exxon non-binding lithium option",
        "KR",
        "event_premium",
        date(2024, 11, 20),
        None,
        None,
        None,
        None,
        ("exxon_arkansas_lithium_supply_deal", "non_binding", "final_price_terms_pending"),
        ("non_binding_offtake", "final_terms_missing", "price_unknown", "stage3_cap"),
        "non_binding_lithium_offtake_cap",
        "needs_price_backfill",
        ("round_174.md Reuters Exxon non-binding lithium supply deal",),
        "Non-binding lithium supply option routes research but cannot create Stage 3 before final offtake terms.",
        (E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
    ),
    Round174CaseCandidate(
        "lnf_lithium_event_rally_case",
        "EVENT_LITHIUM_PRICE_RALLY",
        "066970/003670",
        "L&F / POSCO Future M lithium event rally",
        "KR",
        "event_premium",
        date(2025, 8, 1),
        None,
        None,
        None,
        None,
        ("catl_yichun_mine_suspension", "lithium_supply_sentiment", "lnf_price_reaction_10pct", "posco_future_m_price_reaction_8_3pct", "lithium_price_down_90pct_from_peak"),
        ("contract_missing", "opm_missing", "fcf_missing", "commodity_event_only", "mine_restart_risk"),
        "lithium_event_rally_not_structural",
        "needs_exact_stage_date_backfill",
        ("round_174.md WSJ CATL lithium mine suspension",),
        "Lithium mine suspension can create price reaction, but it is Stage 1 event premium without contract, OPM, FCF, and customer demand.",
        (E2RArchetype.LITHIUM_CYCLE_OVERLAY,),
    ),
    Round174CaseCandidate(
        "skiet_separator_sale_review_4c_case",
        "SEPARATOR_EV_DEMAND_CYCLE",
        "361610",
        "SK IE Technology separator demand cycle",
        "KR",
        "4c_thesis_break",
        date(2024, 5, 15),
        None,
        None,
        None,
        date(2024, 5, 15),
        ("separator_customer_exposure", "sk_on_loss_expansion", "sale_review", "ev_demand_slowdown", "utilization_risk"),
        ("sale_review", "ev_demand_slowdown", "sk_on_losses", "utilization_risk", "customer_capex_cut"),
        "separator_cycle_4c_watch",
        "needs_price_backfill",
        ("round_174.md Reuters SK Innovation considering SKIET sale",),
        "Separator exposure is directly hit by EV shipment slowdown and parent restructuring pressure.",
        (E2RArchetype.CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK,),
    ),
    Round174CaseCandidate(
        "ecopro_materials_ev_slowdown_4c_case",
        "BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA",
        "450080",
        "EcoPro Materials EV slowdown / operating loss",
        "KR",
        "4c_thesis_break",
        date(2023, 11, 17),
        None,
        None,
        None,
        None,
        ("precursor_vertical_integration", "ipo_capa_narrative", "weak_ev_demand", "mineral_price_drop", "operating_loss", "ford_ev_retreat_price_drop_5pct"),
        ("weak_ev_demand", "operating_loss", "customer_strategy_risk", "mineral_price_drop", "capa_overbuild"),
        "battery_materials_capa_overheat_to_4c_watch",
        "needs_price_backfill",
        ("round_174.md EcoPro Materials IPO / operating loss context", "round_174.md MarketWatch Ford EV retreat shock"),
        "Vertical integration and CAPA narrative are not enough when EV demand, mineral prices, and operating losses break the path.",
        (E2RArchetype.CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK,),
    ),
    Round174CaseCandidate(
        "wcp_separator_watch_red_case",
        "SEPARATOR_EV_DEMAND_CYCLE",
        "393890",
        "WCP separator utilization watch",
        "KR",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("separator_demand_cycle", "ev_battery_shipments", "utilization_backfill_needed"),
        ("utilization_missing", "customer_diversification_missing", "ev_demand_slowdown"),
        "separator_watch_red_until_utilization_customer_backfill",
        "needs_case_backfill",
        ("round_174.md WCP separator demand-cycle backfill note",),
        "Separator peers require utilization and customer diversification before any Green path.",
        (E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE,),
    ),
    Round174CaseCandidate(
        "enchem_electrolyte_capa_watch_case",
        "ELECTROLYTE_CAPA_SUPPLYCHAIN",
        "348370",
        "Enchem electrolyte CAPA watch",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("electrolyte_capa", "customer_backfill_needed", "opm_backfill_needed", "price_path_backfill_needed"),
        ("customer_contract_missing", "opm_missing", "utilization_missing", "price_only_risk"),
        "electrolyte_watch_until_contract_margin_backfill",
        "needs_case_backfill",
        ("round_174.md Enchem electrolyte CAPA backfill note",),
        "Electrolyte CAPA is watch material; customer contract, OPM, and price path must be backfilled.",
        (E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA,),
    ),
    Round174CaseCandidate(
        "daejoo_silicon_anode_commercialization_case",
        "SILICON_ANODE_COMMERCIALIZATION",
        "078600",
        "Daejoo Electronic Materials silicon anode",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("silicon_anode", "energy_density", "potential_cell_customers", "commercial_volume_needed"),
        ("commercial_volume_missing", "customer_qualification_pending", "asp_margin_missing"),
        "silicon_anode_stage1_2_until_commercial_volume",
        "needs_case_backfill",
        ("round_174.md Silicon anode commercialization backfill note",),
        "Silicon anode remains Stage 1/2 until commercial volume, ASP, margin, and OP/EPS evidence exist.",
        (E2RArchetype.SPECULATIVE_BATTERY_TECH,),
    ),
)


ROUND174_PRICE_FIELDS: tuple[str, ...] = (
    "case_id",
    "ticker",
    "symbol",
    "company_name",
    "primary_archetype",
    "secondary_archetypes",
    "stage1_date",
    "stage2_date",
    "stage3_date",
    "stage4b_date",
    "stage4c_date",
    "stage1_trigger",
    "stage2_trigger",
    "stage3_trigger",
    "stage4b_trigger",
    "stage4c_trigger",
    "price_at_stage1",
    "price_at_stage2",
    "price_at_stage3",
    "price_at_stage4b",
    "price_at_stage4c",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "peak_date",
    "return_20d_after_stage2",
    "return_60d_after_stage2",
    "return_120d_after_stage2",
    "return_252d_after_stage2",
    "mfe_60d_after_stage2",
    "mae_60d_after_stage2",
    "mfe_120d_after_stage2",
    "mae_120d_after_stage2",
    "mfe_252d_after_stage2",
    "mae_252d_after_stage2",
    "relative_strength_vs_kospi",
    "relative_strength_vs_kosdaq",
    "relative_strength_vs_battery_basket",
    "contract_amount",
    "contract_counterparty",
    "contract_period",
    "contract_amount_to_prior_sales",
    "gwh_or_tonnage",
    "production_start_date",
    "line_conversion_flag",
    "utilization_signal",
    "converted_line_utilization",
    "ess_opm",
    "op_revision_before_stage3",
    "op_revision_after_stage3",
    "eps_revision_before_stage3",
    "eps_revision_after_stage3",
    "raw_material_price_exposure",
    "lithium_price_exposure",
    "graphite_tariff_flag",
    "quarterly_price_negotiation_flag",
    "anode_revenue_flag",
    "cathode_plant_stake_flag",
    "non_binding_offtake_flag",
    "lithium_jv_stake_value_usd",
    "mine_name",
    "spodumene_offtake_flag",
    "inventory_loss_flag",
    "customer_strategy_risk",
    "sale_review_flag",
    "factory_idle_flag",
    "operating_loss_flag",
    "customer_undisclosed_flag",
    "disclosure_confidence",
    "opendart_rcept_no",
    "opendart_detail_fetched_flag",
    "detail_parser_confidence",
    "valuation_at_stage3",
    "valuation_at_stage4b",
    "stage_before_redteam",
    "stage_after_redteam",
    "score_before_redteam",
    "score_after_redteam",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def round174_target_for(target_id: str) -> Round174ScoreTarget | None:
    for target in ROUND174_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round174_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND174_CASE_CANDIDATES:
        target = round174_target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_dict()
        stage4b_evidence = candidate.evidence_fields if candidate.case_type == "4b_watch" or candidate.stage4b_date else ()
        stage4c_evidence = candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" or candidate.stage4c_date or target.hard_gate else ()
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market=candidate.market,
            sector_raw=candidate.target_id,
            primary_archetype=target.canonical_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=target.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                f"Round174 R3 Loop-11 Korea battery/EV/green case for {candidate.target_id}; "
                "calibration-only and focused on Stage 2 strength, Stage 3 caps, plus 4B/4C cooling."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions or field in target.green_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break", "one_off"}
                else None
            ),
            score_price_alignment=_round174_score_price_alignment(candidate),
            rerating_result=_round174_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint={
                "eps_fcf": _numeric_weight(weights["eps_fcf_opm"]),
                "visibility": _numeric_weight(weights["contract_visibility"]),
                "capa_utilization": _numeric_weight(weights["capa_utilization_line_conversion"]),
                "structural_demand_shift": _numeric_weight(weights["structural_demand_shift"]),
                "early_price_validation": _numeric_weight(weights["early_price_validation"]),
                "safety_regulatory_disclosure": _numeric_weight(weights["safety_regulatory_disclosure"]),
                "valuation_4b_room": _numeric_weight(weights["valuation_4b_room"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "ev_growth_is_not_fcf_evidence",
                "require_contract_utilization_opm_fcf_and_customer_detail_for_green",
                "stage3_early_catch_requires_4_of_7_loop11_conditions",
                "stage4b_cooling_requires_3_of_5_loop11_conditions",
                "do_not_invent_contract_value_margin_utilization_customer_stage_prices_or_tonnage",
                "policy_tariff_lithium_event_non_binding_deal_and_capa_narrative_do_not_create_green",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75
                if candidate.stage1_date or candidate.stage2_date or candidate.stage3_date or candidate.stage4b_date or candidate.stage4c_date
                else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round174_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND174_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf_opm": str(weights["eps_fcf_opm"]),
                "contract_visibility": str(weights["contract_visibility"]),
                "capa_utilization_line_conversion": str(weights["capa_utilization_line_conversion"]),
                "structural_demand_shift": str(weights["structural_demand_shift"]),
                "early_price_validation": str(weights["early_price_validation"]),
                "safety_regulatory_disclosure": str(weights["safety_regulatory_disclosure"]),
                "valuation_4b_room": str(weights["valuation_4b_room"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "loop11_penalty_axes": "|".join(target.loop11_penalty_axes),
                "hard_gate": str(target.hard_gate).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round174_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND174_CASE_CANDIDATES:
        target = round174_target_for(candidate.target_id)
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
                "stage1_date": candidate.stage1_date.isoformat() if candidate.stage1_date else "",
                "stage2_date": candidate.stage2_date.isoformat() if candidate.stage2_date else "",
                "stage3_date": candidate.stage3_date.isoformat() if candidate.stage3_date else "",
                "stage4b_date": candidate.stage4b_date.isoformat() if candidate.stage4b_date else "",
                "stage4c_date": candidate.stage4c_date.isoformat() if candidate.stage4c_date else "",
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "alignment_hint": candidate.alignment_hint,
                "price_validation_status": candidate.price_validation_status,
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round174_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop11_penalty_axes": "|".join(target.loop11_penalty_axes),
            "hard_gate": str(target.hard_gate).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND174_SCORE_TARGETS
    )


def round174_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round174_backfill": "true"} for field in ROUND174_PRICE_FIELDS)


def round174_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(weight.as_row() for weight in ROUND174_BASE_SCORE_WEIGHTS)


def round174_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(cap.as_row() for cap in ROUND174_STAGE_CAPS)


def round174_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND174_SCORE_STAGE_PRICE_ALIGNMENT)


def round174_summary() -> dict[str, int | bool]:
    records = round174_case_records()
    return {
        "target_count": len(ROUND174_SCORE_TARGETS),
        "source_canonical_target_count": ROUND174_SOURCE_CANONICAL_TARGET_COUNT,
        "case_candidate_count": len(records),
        "base_score_component_count": len(ROUND174_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND174_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND174_SCORE_STAGE_PRICE_ALIGNMENT),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND174_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND174_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND174_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "hard_gate_target_count": sum(1 for target in ROUND174_SCORE_TARGETS if target.hard_gate),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round174_r3_loop11_reports(
    *,
    output_directory: str | Path = ROUND174_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND174_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND174_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round174_r3_loop11_battery_ev_green_summary.md",
        "case_matrix": output / "round174_r3_loop11_case_matrix.csv",
        "stage_date_plan": output / "round174_r3_loop11_stage_date_plan.csv",
        "green_guardrails": output / "round174_r3_loop11_green_guardrails.md",
        "loop11_risk_overlays": output / "round174_r3_loop11_risk_overlays.md",
        "price_validation_plan": output / "round174_r3_loop11_price_validation_plan.md",
        "price_fields": output / "round174_r3_loop11_price_fields.csv",
        "base_score_weights": output / "round174_r3_loop11_base_score_weights.csv",
        "stage_caps": output / "round174_r3_loop11_stage_caps.csv",
        "score_stage_price_alignment": output / "round174_r3_loop11_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round174_r3_loop11_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round174_case_records(), cases)
    _write_rows(round174_score_profile_rows(), score_profiles)
    _write_rows(round174_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round174_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round174_price_field_rows(), paths["price_fields"])
    _write_rows(round174_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round174_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round174_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round174_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round174_green_guardrail_markdown(), encoding="utf-8")
    paths["loop11_risk_overlays"].write_text(render_round174_loop11_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round174_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(render_round174_score_stage_price_alignment_markdown(), encoding="utf-8")
    return paths


def render_round174_summary_markdown() -> str:
    summary = round174_summary()
    lines = [
        "# Round-174 R3 Loop-11 Korea Battery / EV / Green Summary",
        "",
        f"- source_round: `{ROUND174_SOURCE_ROUND_PATH}`",
        "- large_sector: `BATTERY_EV_GREEN`",
        "- loop: `R3 Loop 11 / v11.0`",
        f"- target_count: {summary['target_count']}",
        f"- source_canonical_target_count: {summary['source_canonical_target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_component_count: {summary['base_score_component_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        f"- hard_gate_target_count: {summary['hard_gate_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R3 Loop 11 is Korea-first and treats EV CAPA growth as insufficient unless utilization, OPM, FCF, and customer contracts follow.",
        "- Loop 11 raises line conversion and utilization because idle EV capacity can become a cost problem, not evidence.",
        "- Stage 3-Green remains strict. ESS, lithium, graphite, cathode, anode, separator, electrolyte, or silicon-anode keywords do not create Green by themselves.",
        "- The base score weights are EPS/FCF/OPM 24, contract visibility 22, CAPA/utilization 14, structural demand shift 12, early price path 10, safety/disclosure 8, valuation/4B room 10.",
        "- Example: Samsung SDI ESS LFP is Stage 2 strong, but customer secrecy, delayed revenue, OPM, and line utilization cap Stage 3.",
        "- Example: POSCO Future M graphite offtake is Stage 2, but a +20% tariff rally is 4B-watch until anode revenue and margin appear.",
        "- Example: SKIET separator exposure is Watch/Red when EV slowdown, parent losses, and sale review appear.",
        "- Example: EcoPro Materials vertical integration narrative is cooled by weak EV demand, mineral-price weakness, operating loss, and customer strategy risk.",
    ]
    return "\n".join(lines) + "\n"


def render_round174_green_guardrail_markdown() -> str:
    lines = [
        "# Round-174 R3 Loop-11 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-11 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND174_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.loop11_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R3 Loop-11 v11.0 weights to production scoring yet.",
            "- Do not lower Stage 3-Green thresholds because ESS or battery-material stocks moved.",
            "- Do not use Round 174 case records as candidate-generation input.",
            "- Do not treat EV growth, ESS keyword, lithium rebound, graphite tariff, non-binding offtake, or CAPA narrative as Green by itself.",
            "- Do not invent customer names, contract amounts, GWh/tonnage, utilization, margins, stage prices, MFE/MAE, or raw-material exposure.",
            "- Apply 4B-watch when policy, tariff, lithium, graphite, or ESS keyword rallies outrun OP/EPS revision.",
            "- Apply 4C/hard review for contract cancellation, factory idle, sale review, customer EV strategy retreat, operating losses, or missing contract terms.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round174_loop11_risk_overlay_markdown() -> str:
    lines = [
        "# Round-174 R3 Loop-11 Risk Overlays",
        "",
        "- `STAGE2_STRONG_NOT_GREEN`: large ESS contract and line conversion can be strong Stage 2, but OPM/utilization gates Stage 3.",
        "- `GRAPHITE_TARIFF_4B`: graphite offtake can be real Stage 2, while tariff-driven price spikes require 4B-watch.",
        "- `LITHIUM_RESOURCE_CYCLE_CAP`: mine stake and spodumene rights are resource security, but lithium cycle and FCF proof cap Green.",
        "- `NON_BINDING_OFFTAKE_CAP`: non-binding lithium supply deals are options, not final contracts.",
        "- `LITHIUM_EVENT_PREMIUM`: CATL mine suspension or lithium supply shock is event premium without customer/margin evidence.",
        "- `SEPARATOR_DEMAND_4C`: EV slowdown and sale review break separator utilization visibility.",
        "- `CUSTOMER_STRATEGY_4C`: automaker EV retreat, factory idle, or expected revenue loss is hard RedTeam.",
        "- `DISCLOSURE_CONFIDENCE_CAPPED`: battery contract headlines are capped until customer, amount, period, GWh/tonnage, OPM, and utilization are parsed.",
        "",
        "Simple example: if `as_of_date=2025-12-09`, Samsung SDI's ESS contract can be Stage 2 strong. A 2027 revenue ramp or later ESS margin proof cannot be used on that date.",
    ]
    return "\n".join(lines) + "\n"


def render_round174_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-174 R3 Loop-11 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign Stage 1/2/3/4B/4C dates from dated source evidence only.",
        "2. Backfill KRX daily bars for `price_at_stage1` through `price_at_stage4c`.",
        "3. Calculate 20D/60D/120D/252D returns and MFE/MAE after Stage 2.",
        "4. Compare price speed against OP/EPS revision and utilization/margin evidence.",
        "5. Separate contract-led Stage 2 from event-led 4B-watch and demand-break 4C-watch.",
        "6. Keep non-binding, customer-undisclosed, policy/tariff, and commodity-cycle caps explicit.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round174_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `stage2_strong_not_green_yet`: contract evidence is strong but Stage 3 fields are missing.",
            "- `supply_chain_event_not_green`: supply-chain evidence exists, but policy/tariff event rally must be cooled.",
            "- `resource_security_with_cycle_cap`: resources are useful but commodity-cycle and FCF proof remain gates.",
            "- `non_binding_cap_correct`: non-binding deals can route research, not Green.",
            "- `event_rally_not_structural`: commodity price event is not structural evidence.",
            "- `hard_redteam_alignment`: sale review, operating losses, customer strategy break, or utilization collapse blocks positive narrative.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round174_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-174 R3 Loop-11 Score -> Stage -> Price Alignment",
        "",
        "## Base Score Weights",
        "",
        "| component | points | direction | reason |",
        "| --- | ---: | --- | --- |",
    ]
    for row in ROUND174_BASE_SCORE_WEIGHTS:
        lines.append(f"| `{row.component}` | {row.points} | {row.loop11_direction} | {row.reason} |")
    lines.extend(
        [
            "",
            "## Stage Caps",
            "",
            "| stage band | max score | evidence | examples | Green policy |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for cap in ROUND174_STAGE_CAPS:
        lines.append(
            f"| `{cap.stage_band}` | {cap.max_score} | {', '.join(cap.required_evidence)} | "
            f"{', '.join(cap.example_cases)} | {cap.green_policy} |"
        )
    lines.extend(
        [
            "",
            "## Alignment Cases",
            "",
            "| case | detected stage | price-path status | verdict | adjustment |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in ROUND174_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(
            f"| `{row.case_id}` | {row.detected_stage} | {row.price_path_status} | "
            f"{row.verdict} | {row.normalization_adjustment} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Samsung SDI is the cleanest R3 Stage 2 strong test, but it remains capped before OPM/utilization proof.",
            "- POSCO Future M graphite proves why supply-chain security and event-rally 4B can coexist.",
            "- POSCO Holdings and LG Chem resource/cathode cases are Stage 2 options until FCF and utilization are visible.",
            "- SKIET and EcoPro Materials show why EV slowdown, operating loss, and customer strategy risk must cool CAPA narratives.",
        ]
    )
    return "\n".join(lines) + "\n"


def _round174_score_price_alignment(candidate: Round174CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "aligned"
    if candidate.case_type == "success_candidate" and "stage2_strong" in candidate.alignment_hint:
        return "aligned"
    if candidate.case_type == "success_candidate":
        return "unknown"
    if candidate.case_type in {"event_premium", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"4c_thesis_break", "failed_rerating"}:
        return "false_positive_score"
    return "unknown"


def _round174_rerating_result(candidate: Round174CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown"


def _numeric_weight(value: int | str) -> float:
    if isinstance(value, int):
        return float(value)
    if value in {"gate", "cap", "+", "event"}:
        return 0.0
    return float(value)


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


__all__ = [
    "ROUND174_BASE_SCORE_WEIGHTS",
    "ROUND174_CASE_CANDIDATES",
    "ROUND174_DEFAULT_CASES_PATH",
    "ROUND174_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND174_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND174_PRICE_FIELDS",
    "ROUND174_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND174_SCORE_TARGETS",
    "ROUND174_SOURCE_CANONICAL_TARGET_COUNT",
    "ROUND174_SOURCE_CANONICAL_TARGET_IDS",
    "ROUND174_STAGE_CAPS",
    "Round174BaseScoreWeight",
    "Round174CaseCandidate",
    "Round174ScoreStagePriceAlignment",
    "Round174ScoreTarget",
    "Round174ScoreWeightDraft",
    "Round174StageCap",
    "render_round174_green_guardrail_markdown",
    "render_round174_loop11_risk_overlay_markdown",
    "render_round174_price_validation_plan_markdown",
    "render_round174_score_stage_price_alignment_markdown",
    "render_round174_summary_markdown",
    "round174_base_score_weight_rows",
    "round174_case_candidate_rows",
    "round174_case_records",
    "round174_price_field_rows",
    "round174_score_profile_rows",
    "round174_score_stage_price_alignment_rows",
    "round174_stage_cap_rows",
    "round174_stage_date_rows",
    "round174_summary",
    "round174_target_for",
    "write_round174_r3_loop11_reports",
]
