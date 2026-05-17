"""Round-152 R7 Loop-9 biotech, healthcare, and medical-device pack.

Round 152 tightens the R7 healthcare pack. It separates approvals, clinical
wins, AI papers, user growth, large TAM stories, and capacity narratives from
actual commercialization evidence: prescriptions, reimbursement, revenue
conversion, capacity utilization, recurring procedures, consumables, OPM, FCF,
cash runway, and device safety.

This module is calibration/report material only. Production feature
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


ROUND152_SOURCE_ROUND_PATH = "docs/round/round_152.md"
ROUND152_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round152_r7_loop9_biotech_healthcare_device"
ROUND152_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop9_round152.jsonl"
ROUND152_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round152_r7_loop9_v9.csv"


@dataclass(frozen=True)
class Round152ScoreWeightDraft:
    eps_fcf: int | str
    structural_visibility: int | str
    bottleneck_pricing: int | str
    market_mispricing: int | str
    valuation: int | str
    capital_allocation: int | str
    information_confidence: int | str

    def as_dict(self) -> dict[str, int | str]:
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
class Round152ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round152ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop9_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round152CaseCandidate:
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
class Round152BaseScoreWeight:
    component: str
    weight: int
    interpretation: str


@dataclass(frozen=True)
class Round152StageCap:
    cap_id: str
    max_stage: str
    condition: str
    example: str


@dataclass(frozen=True)
class Round152ScoreStagePriceAlignment:
    case_id: str
    score_stage: str
    price_path_signal: str
    verdict: str
    normalization_adjustment: str


GATE_WEIGHT = Round152ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate")
CAP_WEIGHT = Round152ScoreWeightDraft("cap", "cap", "cap", "cap", "cap", "cap", "+")


ROUND152_BASE_SCORE_WEIGHTS: tuple[Round152BaseScoreWeight, ...] = (
    Round152BaseScoreWeight(
        "eps_fcf_commercialization_conversion",
        24,
        "Approvals, trials, and papers matter only when they convert into prescriptions, revenue, OPM, FCF, or cash runway.",
    ),
    Round152BaseScoreWeight(
        "prescription_reimbursement_recurring_visibility",
        22,
        "Scripts, PBM/insurance, reimbursement, procedure growth, consumables, and CDMO utilization decide Stage 2 to Stage 3 promotion.",
    ),
    Round152BaseScoreWeight(
        "barrier_recurring_bottleneck",
        14,
        "Installed base, long-term contracts, regulatory barrier, switching cost, and repeat consumables provide durable visibility.",
    ),
    Round152BaseScoreWeight(
        "market_mispricing_rerating_gap",
        8,
        "The market must still be using an old approval/TAM/capacity frame after commercialization evidence appears.",
    ),
    Round152BaseScoreWeight(
        "valuation_room_4b_runway",
        6,
        "GLP-1, surgical robot, CDMO, medical AI, and biosimilar narratives can become crowded before FCF confirms.",
    ),
    Round152BaseScoreWeight(
        "cash_runway_capital_discipline",
        10,
        "Cash runway, dilution, take-private risk, capex burden, and funding-cycle exposure are central healthcare gates.",
    ),
    Round152BaseScoreWeight(
        "safety_regulatory_disclosure_confidence",
        16,
        "Safety, reimbursement, FDA/DOJ, patent litigation, subgroup validation, device counterfeit, and disclosure detail are stronger Loop-9 hard gates.",
    ),
)


ROUND152_STAGE_CAPS: tuple[Round152StageCap, ...] = (
    Round152StageCap(
        "stage1_science_tam_capacity_cap",
        "Stage 1",
        "clinical result, FDA/EMA expectation, medical AI paper, CDMO capacity, GLP-1 TAM, biosimilar approval expectation, or device launch only",
        "Pre-revenue biotech, AI drug platform, medical-AI AUC paper, or GLP-1 TAM headline.",
    ),
    Round152StageCap(
        "stage2_approval_access_validation_cap",
        "Stage 2",
        "approval, PBM/formulary, contract or facility acquisition, procedure growth, external validation, pricing, launch plan, or initial stock reaction",
        "Lilly Foundayo approval, Samsung Biologics Rockville facility, Cigna Humira biosimilar $0 copay, or Lunit DBT validation.",
    ),
    Round152StageCap(
        "stage3_commercial_revenue_required",
        "Stage 3 candidate",
        "prescriptions, insurance/reimbursement, commercial revenue, OPM/FCF, procedure growth plus consumables, repeat CDMO contracts, utilization, and aligned price path",
        "Intuitive Surgical procedure growth plus instruments/accessories revenue and guidance raise.",
    ),
    Round152StageCap(
        "stage4b_healthcare_consensus_crowding",
        "4B-watch",
        "GLP-1, surgical robot, CDMO, medical AI, or biosimilar consensus is crowded and valuation moves before scripts or FCF",
        "GLP-1 mega-TAM or medtech platform premium before gross-to-net, scripts, procedure mix, and FCF remain confirmed.",
    ),
    Round152StageCap(
        "stage4c_healthcare_hard_redteam",
        "4C",
        "sales/profit decline warning, price war, compounded crackdown, cash crunch, discounted take-private, forecast cut, impairment, patent litigation, counterfeit or safety warning",
        "Novo price-war warning, Hims compounded GLP-1 crackdown, bluebird cash crunch, Charles River forecast cut, Teladoc impairment, or Botox counterfeit warning.",
    ),
)


ROUND152_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round152ScoreStagePriceAlignment, ...] = (
    Round152ScoreStagePriceAlignment(
        "samsung_biologics_gsk_us_facility_case",
        "Stage 2",
        "strategic US CDMO site and 60,000L capacity, but announcement price path lagged the market",
        "capacity improves visibility but is not Stage 3 without customers, utilization, tech transfer, OPM, and FCF",
        "raise CDMO visibility; cap EPS/FCF until contracted utilization and margin conversion are visible",
    ),
    Round152ScoreStagePriceAlignment(
        "intuitive_surgical_q1_2026_procedure_growth_case",
        "Stage 2->3",
        "procedure growth, instruments/accessories revenue, guidance raise, and positive price reaction aligned",
        "surgical robot installed-base recurring consumables are the cleanest R7 structural medtech pattern",
        "raise procedure growth, installed base, consumables, and OPM/FCF conversion weight",
    ),
    Round152ScoreStagePriceAlignment(
        "lilly_foundayo_fda_approval_case",
        "Stage 2",
        "FDA approval and launch price aligned with positive price reaction",
        "approval was correctly captured, but Stage 3 waits for scripts, insurance, gross-to-net, refill, and OP/EPS",
        "add oral GLP-1 approval target; keep prescription and reimbursement gate strict",
    ),
    Round152ScoreStagePriceAlignment(
        "lilly_foundayo_switch_maintenance_case",
        "Stage 2 reinforcement",
        "maintenance data supports injection-to-pill switch durability, but commercial proof is still missing",
        "maintenance therapy strengthens visibility without replacing scripts and coverage",
        "add refill/adherence field; cap Stage 3 until coverage, price, scripts, and OP/EPS are visible",
    ),
    Round152ScoreStagePriceAlignment(
        "boehringer_goodrx_humira_biosimilar_case",
        "Stage 2",
        "PBM/cash-pay access and deep discount improved access, but uptake remained slow",
        "biosimilar access without prescription switch is not Green",
        "raise PBM/formulary and prescription conversion weight; keep discount-only cap",
    ),
    Round152ScoreStagePriceAlignment(
        "lunit_dbt_subgroup_validation_case",
        "Stage 1~2",
        "large external validation showed AUC/recall but subgroup weaknesses remained",
        "medical AI evidence is research-quality until deployment, reimbursement, workflow, and liability pass",
        "add subgroup generalization overlay and keep paper/AUC-only cap",
    ),
    Round152ScoreStagePriceAlignment(
        "novo_glp1_price_pressure_case",
        "4B->4C",
        "price war, competition, copycat pressure, and sales/profit warning matched sharp drawdown",
        "GLP-1 TAM does not override price/gross-to-net and competition risk",
        "raise GLP-1 price-war and gross-to-net RedTeam weight",
    ),
    Round152ScoreStagePriceAlignment(
        "hims_branded_glp1_pivot_loss_case",
        "4C-watch",
        "branded pivot cost, legal/restructuring cost, revenue recognition, and loss matched drawdown",
        "telehealth GLP-1 is channel economics and compliance, not drug TAM",
        "raise CAC, legal cost, revenue recognition, and compliance gates",
    ),
    Round152ScoreStagePriceAlignment(
        "bluebird_gene_therapy_cash_crunch_case",
        "hard 4C",
        "approved gene therapies still failed through slow uptake, cash crunch, and discounted take-private",
        "approval without patient uptake and reimbursement is a commercialization failure",
        "raise patient uptake, reimbursement, cash runway, and going-concern gates",
    ),
    Round152ScoreStagePriceAlignment(
        "charles_river_cro_funding_crunch_case",
        "4C-watch",
        "CRO forecast cut and biotech funding crunch matched negative price reaction",
        "CRO recurring service is exposed to customer funding cycle",
        "add explicit CRO funding-cycle overlay and customer R&D budget gate",
    ),
    Round152ScoreStagePriceAlignment(
        "teladoc_betterhelp_impairment_case",
        "hard 4C",
        "impairment, CAC pressure, forecast withdrawal, and record-low price path matched RedTeam",
        "telehealth user demand is not enough without unit economics and contract durability",
        "increase DTC telehealth CAC/impairment/forecast-withdrawal penalty",
    ),
    Round152ScoreStagePriceAlignment(
        "amgen_samsung_bioepis_biosimilar_litigation_case",
        "4C-watch",
        "patent litigation can delay biosimilar launch and damage economics",
        "filing or approval does not remove launch-timing risk",
        "make patent litigation a mandatory biosimilar RedTeam field",
    ),
    Round152ScoreStagePriceAlignment(
        "botox_counterfeit_fda_warning_case",
        "4C-watch",
        "counterfeit/unapproved injectable and injury reports triggered safety warnings",
        "repeat aesthetic demand is capped by licensed channel and safety",
        "keep device safety/counterfeit as hard gate for aesthetic repeat-demand stories",
    ),
)


ROUND152_SCORE_TARGETS: tuple[Round152ScoreTarget, ...] = (
    Round152ScoreTarget(
        "CDMO_HEALTHCARE_CONTRACT",
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round152ScoreWeightDraft(20, 24, 12, 12, 12, 0, 5),
        ("cdmo_contract", "capacity_expansion", "new_manufacturing_site", "us_eu_local_production"),
        ("long_term_contract", "capacity_utilization", "customer_diversification", "op_eps_revision"),
        ("multi_year_production_visibility", "fcf_conversion", "utilization_leverage", "high_value_modality_mix"),
        ("capacity_premium_overheated", "capex_story_priced_before_utilization"),
        ("utilization_down", "contract_delay", "capex_burden", "tariff_or_quality_issue", "us_operating_cost"),
        ("long_term_contract", "capacity_utilization", "customer_diversification", "fcf_conversion"),
        ("underutilization", "customer_concentration", "capex_burden", "quality_issue", "tariff", "us_operating_cost"),
        ("utilization", "customer_contract", "capex", "quality"),
        "CDMO is Green-capable, but capacity alone is not Stage 3 without utilization, contracts, margin, and FCF.",
    ),
    Round152ScoreTarget(
        "CDMO_US_TARIFF_HEDGE_CAPACITY",
        E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(19, 21, 12, 12, 11, 0, 5),
        ("us_manufacturing_site", "tariff_hedge", "facility_acquisition", "capacity_liters"),
        ("facility_close", "customer_contract", "technology_transfer", "capacity_utilization"),
        ("us_capacity_revenue_conversion", "opm_fcf_conversion", "customer_diversification", "operating_cost_control"),
        ("us_cdmo_capacity_premium_overheated", "tariff_hedge_story_crowded"),
        ("customer_contract_missing", "site_upgrade_capex_overrun", "utilization_low", "us_operating_cost_up", "technology_transfer_delay"),
        ("customer_contract", "capacity_utilization", "technology_transfer", "opm_fcf_conversion"),
        ("customer_contract_missing", "underutilization", "us_operating_cost", "capex_burden", "technology_transfer_delay"),
        ("us_capacity", "utilization", "customer_contract", "technology_transfer", "operating_cost"),
        "A US CDMO footprint is strategic Stage 1/2; Green waits for customers, utilization, technology transfer, OPM, and FCF.",
    ),
    Round152ScoreTarget(
        "CDMO_ADC_CELL_GENE_CAPABILITY",
        E2RArchetype.CDMO_ADC_CELL_GENE_CAPABILITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(19, 20, 11, 12, 10, 0, 5),
        ("adc_cell_gene_capacity", "high_value_modality_capacity", "technology_transfer_plan", "site_upgrade_capex"),
        ("customer_contract", "regulatory_tech_transfer", "capacity_utilization", "quality_system_ready"),
        ("repeat_high_value_modality_revenue", "opm_fcf_conversion", "customer_diversification", "utilization_leverage"),
        ("adc_cell_gene_capacity_premium_overheated", "modality_story_priced_before_contract"),
        ("customer_contract_missing", "technology_transfer_delay", "quality_issue", "utilization_low", "capex_overrun"),
        ("customer_contract", "capacity_utilization", "regulatory_tech_transfer", "opm_fcf_conversion"),
        ("customer_contract_missing", "regulatory_tech_transfer_missing", "underutilization", "quality_issue", "capex_burden"),
        ("customer_contract", "technology_transfer", "utilization", "quality", "capex"),
        "ADC/cell/gene CDMO capability is high-value, but Green waits for customer contracts, tech transfer, utilization, and margin.",
    ),
    Round152ScoreTarget(
        "CRO_CLINICAL_SERVICE",
        E2RArchetype.CRO_CLINICAL_SERVICE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(16, 17, 7, 11, 9, 0, 5),
        ("clinical_service_backlog", "pharma_rd_budget", "trial_volume_growth"),
        ("service_revenue_growth", "customer_diversification", "repeat_service_revenue", "funding_cycle_stable"),
        ("multi_year_backlog", "funding_cycle_stable", "high_fcf_conversion"),
        ("cro_recovery_expectation_overheated",),
        ("biotech_funding_crunch", "customer_rd_budget_cut", "forecast_cut", "order_cancellation", "revenue_decline"),
        ("service_backlog", "customer_diversification", "repeat_service_revenue", "opm_improvement"),
        ("biotech_funding_cycle_down", "customer_budget_cut", "trial_delay", "low_margin_backlog", "forecast_cut"),
        ("funding_cycle", "customer_budget", "forecast_cut"),
        "CRO is service revenue, but funding-cycle cuts can break backlog and forecast visibility.",
    ),
    Round152ScoreTarget(
        "CRO_FUNDING_CYCLE_OVERLAY",
        E2RArchetype.CRO_FUNDING_CYCLE_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("biotech_funding_crunch", "customer_rd_budget_cut", "trial_delay", "order_cancellation"),
        ("forecast_cut", "revenue_decline", "backlog_conversion_weak", "restructuring"),
        ("not_applicable_gate_only",),
        ("cro_recovery_story_ignores_funding_cycle",),
        ("biotech_funding_crunch", "forecast_cut", "customer_rd_budget_cut", "trial_delay", "revenue_decline"),
        (),
        ("biotech_funding_crunch", "forecast_cut", "customer_rd_budget_cut", "trial_delay", "revenue_decline"),
        ("funding_cycle", "forecast_cut", "customer_budget", "backlog_conversion"),
        "CRO funding-cycle deterioration is a RedTeam gate because backlog can fail when biotech clients lose funding.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "BIOSIMILAR_COMMERCIALIZATION",
        E2RArchetype.BIOSIMILAR_COMMERCIALIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(18, 18, 6, 12, 9, 0, 6),
        ("fda_ema_approval", "patent_expiry", "biosimilar_launch", "discount_access_program"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "launch_revenue"),
        ("prescription_growth", "margin_defense", "multi_country_launch", "payer_access"),
        ("approval_news_overheated", "biosimilar_launch_crowded"),
        ("price_competition", "prescription_conversion_delay", "margin_collapse", "pbm_incentive_gap"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "revenue_conversion"),
        ("price_competition", "coverage_gap", "slow_switching", "margin_pressure", "pbm_incentive_gap"),
        ("pbm", "coverage", "prescription_switch", "margin"),
        "Biosimilar approval and discount are Stage 1; PBM, coverage, prescriptions, and margin decide higher stages.",
    ),
    Round152ScoreTarget(
        "BIOSIMILAR_ACCESS_CASH_PAY",
        E2RArchetype.BIOSIMILAR_ACCESS_CASH_PAY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(16, 15, 5, 11, 8, 0, 6),
        ("cash_pay_discount", "goodrx_access_program", "interchangeable_biosimilar", "patient_access_news"),
        ("discount_program_live", "pharmacy_substitution", "prescription_conversion", "margin_defense"),
        ("sustained_prescription_growth", "pbm_or_cash_channel_scaled", "gross_margin_stable", "payer_access"),
        ("discount_access_story_overheated", "biosimilar_discount_crowded"),
        ("prescription_conversion_delay", "margin_pressure", "pbm_incentive_gap", "coverage_gap", "originator_rebate_defense"),
        ("prescription_conversion", "margin_defense", "pbm_or_cash_channel_scaled", "payer_access"),
        ("slow_switching", "margin_pressure", "pbm_incentive_gap", "coverage_gap", "discount_without_uptake"),
        ("discount", "prescription_switch", "pbm", "margin", "access"),
        "Biosimilar cash-pay access is helpful Stage 2 evidence, but prescription conversion and margin defense decide promotion.",
    ),
    Round152ScoreTarget(
        "BIOSIMILAR_PBM_FORMULARY_SWITCH",
        E2RArchetype.BIOSIMILAR_PBM_FORMULARY_SWITCH,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(18, 19, 6, 12, 9, 0, 7),
        ("pbm_preferred_list", "formulary_switch", "zero_copay_program", "interchangeable_biosimilar"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "switching_incentive_visible"),
        ("sustained_prescription_switch", "payer_access_scaled", "margin_defense", "revenue_conversion"),
        ("pbm_switch_story_crowded", "discount_access_priced_before_uptake"),
        ("slow_switching", "originator_rebate_defense", "pbm_incentive_gap", "margin_pressure", "patent_litigation"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "margin_defense"),
        ("slow_switching", "pbm_incentive_gap", "margin_pressure", "patent_litigation", "discount_without_uptake"),
        ("pbm", "formulary", "prescription_switch", "margin", "patent"),
        "PBM/formulary access is stronger than approval, but Stage 3 waits for prescription switching and margin defense.",
    ),
    Round152ScoreTarget(
        "BIOSIMILAR_PATENT_LITIGATION",
        E2RArchetype.BIOSIMILAR_PATENT_LITIGATION,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("patent_litigation", "injunction_risk", "settlement_negotiation", "launch_delay_risk"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("patent_litigation", "launch_delay", "injunction_risk", "settlement_cost", "margin_compression", "pbm_exclusion"),
        (),
        ("patent_litigation", "launch_delay", "injunction_risk", "settlement_cost", "margin_compression"),
        ("patent", "launch_timing", "settlement", "margin"),
        "Biosimilar patent litigation is a RedTeam gate because launch timing and economics can break approval-led narratives.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "OBESITY_GLP1_COMMERCIALIZATION",
        E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round152ScoreWeightDraft(22, 20, 12, 13, 8, 0, 6),
        ("glp1_approval", "oral_glp1_trial", "prescription_growth", "maintenance_therapy_data"),
        ("weekly_scripts", "insurance_coverage", "supply_capacity", "sales_ramp", "price_defense"),
        ("durable_prescription_growth", "price_defense", "op_eps_revision", "coverage_expansion", "maintenance_use_case"),
        ("obesity_market_narrative_crowded", "scripts_lag_valuation", "market_size_priced_before_uptake"),
        ("compounded_alternative", "price_cut", "coverage_denial", "prescription_slowdown", "telehealth_channel_risk"),
        ("prescription_volume", "insurance_coverage", "supply_capacity", "price_defense", "op_eps_revision"),
        ("competition", "compounded_alternative", "coverage_gap", "price_regulation", "slow_uptake", "telehealth_channel_risk"),
        ("scripts", "coverage", "price", "competition", "compounded_drugs"),
        "GLP-1 can be Green, but TAM is not enough; scripts, coverage, price, supply, and OP/EPS must follow.",
    ),
    Round152ScoreTarget(
        "ORAL_GLP1_APPROVAL_COMMERCIALIZATION",
        E2RArchetype.ORAL_GLP1_APPROVAL_COMMERCIALIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(21, 20, 11, 13, 9, 0, 6),
        ("oral_glp1_trial", "oral_glp1_approval", "launch_price", "obesity_tam"),
        ("fda_approval", "self_pay_price", "launch_plan", "distribution_channel", "initial_stock_reaction"),
        ("weekly_scripts", "insurance_coverage", "gross_to_net_visible", "repeat_refill", "op_eps_revision"),
        ("oral_glp1_convenience_story_crowded", "approval_priced_before_scripts"),
        ("prescription_ramp_failure", "insurance_not_listed", "gross_to_net_pressure", "price_competition", "boxed_warning"),
        ("weekly_scripts", "insurance_coverage", "gross_to_net_visible", "repeat_refill", "op_eps_revision"),
        ("scripts_missing", "coverage_gap", "gross_to_net_pressure", "price_competition", "slow_uptake"),
        ("scripts", "coverage", "gross_to_net", "refill", "price"),
        "Oral GLP-1 approval is Stage 2; commercialization requires scripts, insurance, gross-to-net, refill, and OP/EPS.",
    ),
    Round152ScoreTarget(
        "ORAL_GLP1_MAINTENANCE_THERAPY",
        E2RArchetype.ORAL_GLP1_MAINTENANCE_THERAPY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(21, 19, 11, 13, 9, 0, 6),
        ("oral_glp1_trial", "oral_glp1_approval", "maintenance_therapy_data", "injection_to_pill_switch"),
        ("fda_approval", "self_pay_price", "distribution_channel", "maintenance_trial_data"),
        ("weekly_scripts", "insurance_coverage", "repeat_refill", "op_eps_revision", "real_world_adherence"),
        ("oral_glp1_convenience_story_crowded", "market_size_priced_before_scripts"),
        ("prescription_ramp_failure", "insurance_not_listed", "price_competition", "boxed_warning", "safety_issue"),
        ("weekly_scripts", "insurance_coverage", "repeat_refill", "op_eps_revision", "price_defense"),
        ("scripts_missing", "coverage_gap", "price_competition", "boxed_warning", "slow_uptake"),
        ("scripts", "coverage", "price", "maintenance", "safety"),
        "Oral GLP-1 approval and maintenance data are Stage 2; Green waits for scripts, coverage, refills, and OP/EPS revision.",
    ),
    Round152ScoreTarget(
        "GLP1_PRICE_WAR_OVERLAY",
        E2RArchetype.GLP1_PRICE_WAR_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("glp1_price_cut", "gross_to_net_pressure", "copycat_drug_pressure", "insurance_pressure"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("price_cut", "gross_to_net_pressure", "copycat_pressure", "coverage_denial", "sales_profit_decline"),
        (),
        ("price_cut", "gross_to_net_pressure", "copycat_pressure", "insurance_pressure", "sales_profit_decline"),
        ("price", "gross_to_net", "competition", "coverage", "scripts"),
        "GLP-1 price war is a RedTeam gate because TAM can still break when price, insurance, and copycat pressure hit OP/EPS.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "GLP1_TELEHEALTH_CHANNEL",
        E2RArchetype.GLP1_TELEHEALTH_CHANNEL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(18, 15, 5, 13, 7, 0, 6),
        ("telehealth_glp1_offering", "compounded_product", "branded_partnership_news"),
        ("subscriber_growth", "branded_drug_attach", "legal_settlement", "channel_revenue"),
        ("cac_stable", "gross_margin_stable", "compliance_clean", "fcf_conversion"),
        ("dtc_glp1_channel_valuation_overheated", "channel_event_premium_crowded"),
        ("fda_crackdown", "compounding_ban", "legal_cost", "revenue_recognition_shock", "cac_spike"),
        ("branded_drug_attach", "cac_stable", "gross_margin_stable", "compliance_clean", "fcf_conversion"),
        ("compounding_crackdown", "revenue_recognition", "legal_cost", "cac", "margin_compression"),
        ("cac", "compounding", "revenue_recognition", "legal_cost"),
        "GLP-1 telehealth channels are separated from drug commercialization because channel economics and compliance can break the thesis.",
    ),
    Round152ScoreTarget(
        "COMPOUNDED_GLP1_REGULATORY_RISK",
        E2RArchetype.COMPOUNDED_GLP1_REGULATORY_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("compounded_glp1", "unapproved_copycat", "online_pharmacy", "fda_crackdown"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("fda_crackdown", "unapproved_copycat_drug", "doj_referral", "quality_safety_concern", "channel_shutdown"),
        (),
        ("compounded_drug", "fda_crackdown", "unapproved_copycat", "doj_referral", "quality_safety_concern"),
        ("compounding", "fda", "doj", "quality", "legal"),
        "Compounded GLP-1 channels are gate-only RedTeam risks; demand size does not offset illegal or unsafe distribution.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "GENE_THERAPY_RARE_DISEASE",
        E2RArchetype.GENE_THERAPY_RARE_DISEASE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round152ScoreWeightDraft(7, 10, 8, 9, 5, 0, 5),
        ("gene_therapy_approval", "rare_disease_unmet_need", "patient_recruitment"),
        ("treated_patients", "reimbursement", "commercial_sales", "cash_runway"),
        ("repeat_commercial_uptake", "dilution_risk_controlled", "pipeline_revenue"),
        ("approval_news_overheated", "rare_disease_story_crowded"),
        ("slow_uptake", "cash_crunch", "going_concern", "discounted_take_private", "dilution"),
        ("patient_uptake", "reimbursement", "cash_runway", "commercial_revenue"),
        ("cash_burn", "reimbursement_failure", "slow_uptake", "dilution", "going_concern"),
        ("cash_runway", "reimbursement", "patient_uptake", "dilution"),
        "Approval without commercial uptake and cash runway is not Green.",
    ),
    Round152ScoreTarget(
        "AI_DRUG_DISCOVERY_PLATFORM",
        E2RArchetype.AI_DRUG_DISCOVERY_PLATFORM,
        Round10ThemePosture.REDTEAM_FIRST,
        Round152ScoreWeightDraft(6, 10, 7, 12, 6, 0, 5),
        ("ai_drug_discovery_platform", "candidate_molecule", "platform_partnership"),
        ("big_pharma_milestone", "clinical_entry", "cash_runway"),
        ("validated_pipeline", "partner_funded_progress", "commercial_or_royalty_path"),
        ("ai_drug_platform_overheated", "poc_story_crowded"),
        ("clinical_failure", "cash_burn", "platform_hype_unwind", "no_approved_drug"),
        ("big_pharma_partnership", "clinical_progress", "cash_runway", "milestone_revenue"),
        ("no_approved_drug", "cash_burn", "clinical_failure", "platform_hype"),
        ("milestone", "clinical_progress", "cash_runway", "approved_drug"),
        "AI drug-discovery labels are not score evidence without milestones, clinical progress, and cash runway.",
    ),
    Round152ScoreTarget(
        "DIGITAL_HEALTHCARE_AI",
        E2RArchetype.DIGITAL_HEALTHCARE_AI,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(18, 17, 8, 13, 12, 0, 7),
        ("clinical_ai_paper", "external_validation", "hospital_pilot", "regulatory_clearance"),
        ("hospital_adoption", "reimbursement", "paid_workflow", "recurring_revenue"),
        ("workflow_embedded", "recurring_revenue", "op_improvement", "liability_risk_low"),
        ("medical_ai_narrative_overheated", "paper_only_valuation_premium"),
        ("subgroup_performance_issue", "reimbursement_denial", "liability_event", "hospital_adoption_failure"),
        ("external_validation", "hospital_adoption", "reimbursement_or_paid_usage", "recurring_revenue"),
        ("subgroup_bias", "no_reimbursement", "liability", "poc_only", "date_unverified"),
        ("hospital_adoption", "reimbursement", "subgroup", "liability"),
        "Medical AI papers lift Stage 1/2, but Green requires paid adoption and reimbursement.",
    ),
    Round152ScoreTarget(
        "MEDICAL_AI_EXTERNAL_VALIDATION",
        E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(16, 16, 8, 13, 11, 0, 7),
        ("ai_model_auc", "external_validation", "subgroup_analysis", "regulatory_clearance"),
        ("external_validation", "subgroup_analysis", "pilot_deployment"),
        ("hospital_adoption", "reimbursement_code", "recurring_revenue", "workflow_lock_in", "liability_risk_low"),
        ("medical_ai_auc_story_overheated", "paper_only_valuation_premium"),
        ("subgroup_performance_issue", "deployment_failure", "reimbursement_absent", "liability_event", "workflow_not_integrated"),
        ("external_validation", "hospital_adoption", "reimbursement_or_paid_usage", "recurring_revenue"),
        ("subgroup_performance_risk", "no_reimbursement", "no_hospital_adoption", "liability", "paper_only"),
        ("external_validation", "subgroup", "deployment", "reimbursement", "liability"),
        "External validation and AUC are Stage 1/2; Green needs hospital deployment, reimbursement, recurring revenue, and liability control.",
    ),
    Round152ScoreTarget(
        "MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK",
        E2RArchetype.MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("subgroup_performance_issue", "dataset_bias", "dense_tissue_underperformance", "calcification_underperformance"),
        ("risk_event_detected", "external_validation_subgroup_gap"),
        ("not_applicable_gate_only",),
        ("medical_ai_auc_story_ignores_subgroup_risk",),
        ("subgroup_performance_issue", "dataset_bias", "liability_event", "workflow_failure", "reimbursement_absent"),
        (),
        ("subgroup_performance_issue", "dataset_bias", "liability_event", "workflow_failure", "reimbursement_absent"),
        ("subgroup", "dataset_bias", "liability", "deployment", "reimbursement"),
        "Medical AI subgroup underperformance is a RedTeam gate because high AUC can fail in deployment and reimbursement.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "DIGITAL_HEALTHCARE_REMOTE_MEDICINE",
        E2RArchetype.DIGITAL_HEALTHCARE_REMOTE_MEDICINE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(16, 16, 7, 12, 9, 1, 6),
        ("remote_medicine_policy", "wearable_or_emr_integration", "digital_health_platform"),
        ("hospital_or_insurer_contract", "b2b_b2b2c_contract", "recurring_subscription", "unit_economics"),
        ("embedded_workflow", "reimbursement_visible", "repeat_usage", "opm_improvement"),
        ("telehealth_theme_crowded",),
        ("regulatory_reversal", "reimbursement_failure", "privacy_incident", "unit_economics_failure"),
        ("hospital_or_insurer_contract", "recurring_revenue", "unit_economics", "regulatory_clearance"),
        ("regulation", "privacy", "reimbursement", "cac", "churn"),
        ("regulation", "reimbursement", "unit_economics", "privacy"),
        "Remote medicine needs contracts, reimbursement, and unit economics, not usage story alone.",
    ),
    Round152ScoreTarget(
        "TELEHEALTH_BEHAVIORAL_HEALTH",
        E2RArchetype.TELEHEALTH_BEHAVIORAL_HEALTH,
        Round10ThemePosture.REDTEAM_FIRST,
        Round152ScoreWeightDraft(15, 13, 5, 10, 8, 0, 6),
        ("online_behavioral_health_demand", "subscriber_growth", "dtc_health_platform"),
        ("employer_or_insurer_contract", "cac_stable", "repeat_usage"),
        ("low_churn_contract_revenue", "fcf_margin", "privacy_clean"),
        ("dtc_telehealth_growth_crowded",),
        ("cac_spike", "privacy_incident", "impairment", "forecast_withdrawal", "churn"),
        ("employer_or_insurer_contract", "cac_stable", "churn_stable", "fcf_margin"),
        ("cac", "privacy", "impairment", "forecast_withdrawal", "churn"),
        ("cac", "privacy", "impairment", "churn"),
        "DTC telehealth is RedTeam-first unless contract revenue and unit economics are clear.",
    ),
    Round152ScoreTarget(
        "MEDICAL_DEVICE_HEALTHCARE_EXPORT",
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round152ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("medical_device_export", "new_approval", "procedure_growth"),
        ("export_country_expansion", "recurring_procedure", "consumable_revenue", "opm_roe_improvement"),
        ("repeat_procedure_demand", "asp_stable", "fcf_improvement", "channel_quality"),
        ("device_premium_crowded", "target_multiple_saturated"),
        ("approval_delay", "safety_issue", "price_control", "channel_failure", "single_device_no_consumable"),
        ("export_growth", "consumable_repeat_revenue", "regulatory_approval", "opm_roe_improvement"),
        ("approval_delay", "safety", "competition", "channel_quality", "single_device_no_consumable"),
        ("approval", "safety", "channel_quality", "procedure_repeat"),
        "Medical-device Green needs repeat procedures, consumables, approvals, and export/channel proof.",
    ),
    Round152ScoreTarget(
        "MEDICAL_DEVICE_DENTAL_IMPLANT",
        E2RArchetype.MEDICAL_DEVICE_DENTAL_IMPLANT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round152ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("dental_implant_growth", "procedure_growth", "approval_or_channel"),
        ("export_country_expansion", "recurring_procedure_consumable", "opm_roe_improvement"),
        ("approval_stable", "repeat_consumable_revenue", "pricing_pressure_low", "channel_quality"),
        ("implant_premium_crowded", "vbp_risk_ignored"),
        ("vbp_price_control", "asp_drop", "approval_delay", "safety_issue", "competition"),
        ("recurring_procedure_consumable", "approval_stable", "opm_roe_improvement", "channel_quality"),
        ("vbp_price_control", "approval", "safety", "competition", "asp_drop"),
        ("vbp", "asp", "approval", "procedure_repeat"),
        "Dental implant Green is possible, but VBP and ASP compression are hard risk gates.",
    ),
    Round152ScoreTarget(
        "SURGICAL_ROBOT_INSTALLED_BASE",
        E2RArchetype.SURGICAL_ROBOT_INSTALLED_BASE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round152ScoreWeightDraft(21, 23, 13, 14, 12, 1, 5),
        ("new_robot_launch", "installed_base_growth", "procedure_growth"),
        ("procedure_growth", "system_placement", "instruments_accessories_revenue"),
        ("recurring_consumable_revenue", "installed_base_expansion", "opm_fcf_improvement"),
        ("surgical_robot_platform_premium_overheated", "installed_base_fully_priced"),
        ("hospital_capex_slowdown", "procedure_mix_worse", "glp1_bariatric_slowdown", "competition"),
        ("installed_base", "procedure_growth", "instruments_accessories_revenue", "opm_fcf_improvement"),
        ("hospital_capex", "procedure_mix", "glp1_bariatric_slowdown", "competition"),
        ("installed_base", "procedure_growth", "consumables", "hospital_capex"),
        "Surgical robots are separated from generic medical devices because installed base plus instruments/accessories can create recurring revenue.",
    ),
    Round152ScoreTarget(
        "SURGICAL_ROBOT_GLP1_PROCEDURE_MIX_OVERLAY",
        E2RArchetype.SURGICAL_ROBOT_GLP1_PROCEDURE_MIX_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("glp1_bariatric_slowdown", "procedure_mix_risk", "hospital_capex_slowdown", "bariatric_procedure_decline"),
        ("risk_event_detected", "procedure_mix_shift_visible"),
        ("not_applicable_gate_only",),
        ("surgical_robot_platform_premium_ignores_glp1_mix"),
        ("glp1_bariatric_slowdown", "procedure_mix_worse", "system_placement_slowdown", "hospital_capex_slowdown"),
        (),
        ("glp1_bariatric_slowdown", "procedure_mix_worse", "system_placement_slowdown", "hospital_capex_slowdown"),
        ("procedure_mix", "glp1_bariatric", "system_placements", "hospital_capex"),
        "Surgical robot recurring revenue remains Green-capable, but GLP-1-driven procedure mix slowdown is a RedTeam overlay.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "BOTULINUM_AESTHETIC_REGULATED",
        E2RArchetype.BOTULINUM_AESTHETIC_REGULATED,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round152ScoreWeightDraft(19, 20, 12, 13, 11, 0, 5),
        ("botulinum_toxin_demand", "aesthetic_procedure_growth", "licensed_channel"),
        ("repeat_procedure", "regulatory_approval", "safe_distribution_channel", "op_eps_revision"),
        ("licensed_repeat_procedure", "safety_clean", "export_channel", "fcf_conversion"),
        ("aesthetic_toxin_premium_crowded",),
        ("counterfeit_product", "unapproved_product", "injury_report", "channel_failure", "safety_issue"),
        ("regulatory_approval", "repeat_procedure", "safe_distribution_channel", "op_eps_revision"),
        ("counterfeit", "unapproved_product", "safety", "channel_failure"),
        ("counterfeit", "approval", "licensed_channel", "safety"),
        "Aesthetic toxins are Watch-to-Green only through licensed, safe, repeat-procedure channels.",
    ),
    Round152ScoreTarget(
        "DIAGNOSTICS_INFECTIOUS_DISEASE",
        E2RArchetype.DIAGNOSTICS_INFECTIOUS_DISEASE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round152ScoreWeightDraft(20, 5, 5, 5, 5, 0, 5),
        ("infectious_disease_diagnostic_demand", "pandemic_or_mpox_event", "test_kit_sales_spike"),
        ("recurring_non_event_demand", "installed_base_consumables", "post_event_revenue"),
        ("recurring_platform_revenue", "margin_normalization", "non_event_demand"),
        ("diagnostic_event_extrapolated",),
        ("one_off_demand", "guidance_down", "inventory_build", "demand_cliff"),
        ("recurring_non_event_demand", "post_event_revenue", "margin_normalization"),
        ("one_off_demand", "inventory_build", "guidance_down", "demand_cliff"),
        ("one_off_demand", "inventory", "guidance_down"),
        "Infectious diagnostics are RedTeam-first because event demand can disappear quickly.",
    ),
    Round152ScoreTarget(
        "COMMERCIALIZATION_FAILURE_OVERLAY",
        E2RArchetype.COMMERCIALIZATION_FAILURE_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("approval_without_uptake", "launch_without_revenue", "commercialization_gap"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("slow_uptake", "reimbursement_failure", "commercial_revenue_missing", "cash_crunch", "going_concern"),
        (),
        ("slow_uptake", "reimbursement_failure", "commercial_revenue_missing", "cash_runway_short", "going_concern"),
        ("uptake", "reimbursement", "commercial_revenue", "cash_runway"),
        "Approval after commercialization failure is a RedTeam gate, not positive evidence.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "REIMBURSEMENT_ACCESS_OVERLAY",
        E2RArchetype.REIMBURSEMENT_ACCESS_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("coverage_gap", "pbm_access_issue", "reimbursement_denial", "pricing_pressure"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("insurance_denial", "pbm_exclusion", "reimbursement_failure", "gross_to_net_pressure", "prescription_conversion_delay"),
        (),
        ("insurance_denial", "pbm_exclusion", "reimbursement_failure", "gross_to_net_pressure", "prescription_conversion_delay"),
        ("coverage", "pbm", "reimbursement", "gross_to_net", "prescription_conversion"),
        "Insurance, PBM, reimbursement, and access failures can block GLP-1, biosimilar, gene therapy, and medical AI theses.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "DEVICE_SAFETY_COUNTERFEIT_OVERLAY",
        E2RArchetype.DEVICE_SAFETY_COUNTERFEIT_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("counterfeit_product", "unapproved_device", "recall_or_warning", "product_safety_issue"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("counterfeit_product", "unapproved_injectable", "fda_warning", "injury_report", "licensed_channel_failure", "recall"),
        (),
        ("counterfeit_product", "unapproved_injectable", "fda_warning", "injury_report", "licensed_channel_failure", "recall"),
        ("safety", "license", "channel", "recall", "counterfeit"),
        "Safety, counterfeit, unapproved product, and recall issues are device/aesthetic RedTeam gates.",
        gate_only=True,
    ),
    Round152ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        CAP_WEIGHT,
        ("contract_or_clinical_disclosure_missing_key_fields", "prescription_volume_undisclosed", "reimbursement_undisclosed"),
        ("confidence_cap_detected",),
        ("stage3_cap_until_key_fields_verified",),
        ("not_applicable_cap_only",),
        ("contract_value_missing", "contract_duration_missing", "counterparty_missing", "prescription_or_reimbursement_missing", "disclosure_confidence_low"),
        (),
        ("contract_value_missing", "contract_duration_missing", "counterparty_missing", "prescription_volume_missing", "reimbursement_missing", "disclosure_confidence_low"),
        ("disclosure_confidence", "contract_terms", "prescriptions", "reimbursement"),
        "Missing contract amount, term, counterparty, reimbursement, prescription, or fee fields cap Stage 3 even when the narrative is strong.",
    ),
)


ROUND152_CASE_CANDIDATES: tuple[Round152CaseCandidate, ...] = (
    Round152CaseCandidate(
        "samsung_biologics_gsk_us_facility_case",
        "CDMO_US_TARIFF_HEDGE_CAPACITY",
        "207940",
        "Samsung Biologics GSK US facility acquisition",
        "KR",
        "success_candidate",
        None,
        date(2025, 12, 21),
        None,
        None,
        None,
        ("us_manufacturing_site_flag", "facility_location_rockville", "capacity_liters_60000", "tariff_hedge_flag", "technology_transfer_flag"),
        ("utilization_unverified", "capex_burden", "customer_contract_unverified", "us_operating_cost"),
        "us_capacity_tariff_hedge_but_delayed_price",
        "needs_price_backfill",
        ("round_152.md Reuters Samsung Biologics GSK US facility",),
        "US capacity is strategic, but utilization, customer contracts, technology transfer, OPM, and FCF must be verified.",
        (E2RArchetype.CDMO_HEALTHCARE_CONTRACT,),
    ),
    Round152CaseCandidate(
        "samsung_biologics_cdmo_capacity_reference",
        "CDMO_HEALTHCARE_CONTRACT",
        "207940",
        "Samsung Biologics CDMO capacity reference",
        "KR",
        "structural_success",
        None,
        None,
        None,
        None,
        None,
        ("major_pharma_contracts", "customer_diversification", "capacity_liters", "capacity_utilization", "high_value_modality_mix"),
        ("customer_concentration", "contract_delay", "quality_issue", "underutilization"),
        "cdmo_structural_reference",
        "needs_source_date_and_price_backfill",
        ("round_152.md Samsung Biologics CDMO structure reference",),
        "CDMO references are Green-eligible only after contract, utilization, margin, and FCF conversion are matched to stage dates.",
    ),
    Round152CaseCandidate(
        "intuitive_surgical_q1_2026_procedure_growth_case",
        "SURGICAL_ROBOT_INSTALLED_BASE",
        "ISRG",
        "Intuitive Surgical Q1 2026 procedure growth and recurring consumables",
        "US",
        "structural_success",
        None,
        date(2026, 4, 22),
        None,
        None,
        None,
        ("surgical_robot_installed_base", "procedure_growth_17pct", "system_placements", "instruments_accessories_revenue", "revenue_growth_23pct", "guidance_raise"),
        ("hospital_capex_cycle", "procedure_mix_risk", "glp1_bariatric_slowdown", "medtech_valuation_compression"),
        "surgical_robot_recurring_consumable_success",
        "needs_exact_stage_date_and_price_backfill",
        ("round_152.md Investors Intuitive Surgical Q1 2026",),
        "Installed base, procedure growth, and instruments/accessories revenue make surgical robots a separate recurring-revenue archetype.",
        (E2RArchetype.SURGICAL_ROBOT_GLP1_PROCEDURE_MIX_OVERLAY,),
    ),
    Round152CaseCandidate(
        "straumann_dental_implant_vbp_case",
        "MEDICAL_DEVICE_DENTAL_IMPLANT",
        "STMN.SW",
        "Straumann dental implant growth with VBP risk",
        "CH",
        "success_candidate",
        None,
        date(2026, 2, 18),
        None,
        None,
        None,
        ("sales_growth", "procedure_growth", "regional_growth", "guidance_growth"),
        ("vbp_price_control", "asp_pressure", "china_procurement_uncertainty"),
        "medical_device_aligned_candidate",
        "needs_price_backfill",
        ("round_152.md Reuters Straumann dental implant growth",),
        "Dental implant growth is aligned when procedure and sales growth persist, but VBP price control is a hard gate.",
    ),
    Round152CaseCandidate(
        "lilly_foundayo_fda_approval_case",
        "ORAL_GLP1_APPROVAL_COMMERCIALIZATION",
        "LLY",
        "Lilly oral GLP-1 Foundayo FDA approval",
        "US",
        "success_candidate",
        None,
        date(2026, 4, 1),
        None,
        None,
        None,
        ("fda_approval", "oral_glp1_flag", "trial_weight_loss", "self_pay_price", "maintenance_therapy_flag"),
        ("coverage_unverified", "weekly_scripts_unverified", "competition", "price_pressure", "boxed_warning_unverified"),
        "approval_stage2_not_green",
        "needs_price_backfill",
        ("round_152.md Reuters Lilly oral GLP-1 approval",),
        "Approval and TAM support Stage 1/2; scripts, coverage, supply, price, and OP/EPS decide higher stages.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION, E2RArchetype.ORAL_GLP1_MAINTENANCE_THERAPY),
    ),
    Round152CaseCandidate(
        "lilly_foundayo_switch_maintenance_case",
        "ORAL_GLP1_MAINTENANCE_THERAPY",
        "LLY",
        "Lilly Foundayo switch-maintenance therapy data",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 12),
        None,
        None,
        None,
        ("maintenance_therapy_data", "weight_maintenance", "oral_glp1_flag", "injection_to_pill_switch_flag", "real_world_adherence_signal", "long_term_use_case"),
        ("coverage_unverified", "price_pressure", "competition", "scripts_needed"),
        "glp1_maintenance_structural_candidate",
        "needs_price_backfill",
        ("round_152.md Reuters Foundayo switch maintenance",),
        "Maintenance evidence can support a more durable GLP-1 path, but insurance, price, and scripts still gate Green.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,),
    ),
    Round152CaseCandidate(
        "boehringer_goodrx_humira_biosimilar_case",
        "BIOSIMILAR_ACCESS_CASH_PAY",
        "BIOSIMILAR_ACCESS_REF",
        "Boehringer / GoodRx Humira biosimilar access but uptake watch",
        "US",
        "success_candidate",
        None,
        date(2024, 7, 18),
        None,
        None,
        None,
        ("biosimilar_discount_pct", "access_program", "prescription_volume"),
        ("slow_switching", "pbm_incentive_gap", "margin_pressure", "humira_prescription_dominance"),
        "biosimilar_access_candidate_but_slow_uptake",
        "missing_direct_symbol_mapping",
        ("round_152.md Reuters Humira biosimilar GoodRx access",),
        "A 92% discount improves access, but slow prescription switching and margin defense remain core gates.",
        (E2RArchetype.BIOSIMILAR_COMMERCIALIZATION,),
    ),
    Round152CaseCandidate(
        "cigna_accredo_humira_biosimilar_zero_copay_case",
        "BIOSIMILAR_PBM_FORMULARY_SWITCH",
        "BIOSIMILAR_ACCESS_REF",
        "Cigna / Accredo Humira biosimilar $0 copay formulary switch",
        "US",
        "success_candidate",
        None,
        date(2024, 4, 25),
        None,
        None,
        None,
        ("pbm_listing", "zero_copay_program", "biosimilar_discount_pct", "insurance_coverage", "prescription_conversion_watch"),
        ("slow_switching", "originator_rebate_defense", "pbm_incentive_gap", "margin_pressure"),
        "pbm_formulary_stage2_without_uptake",
        "missing_direct_symbol_mapping",
        ("round_152.md Reuters Cigna Humira biosimilar $0 copay",),
        "PBM/formulary and $0 copay are stronger than approval, but prescription conversion and margin defense still gate Stage 3.",
        (E2RArchetype.BIOSIMILAR_COMMERCIALIZATION, E2RArchetype.BIOSIMILAR_ACCESS_CASH_PAY),
    ),
    Round152CaseCandidate(
        "novo_glp1_price_pressure_case",
        "GLP1_PRICE_WAR_OVERLAY",
        "NVO",
        "Novo Nordisk GLP-1 price pressure and competition",
        "DK",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 2, 3),
        ("glp1_market_growth", "wegovy_sales_base"),
        ("price_pressure", "competition", "compounded_alternative", "outlook_cut", "sales_profit_decline", "gross_to_net_pressure"),
        "glp1_4b_to_4c",
        "needs_price_backfill",
        ("round_152.md Reuters Novo 2026 outlook warning",),
        "GLP-1 TAM can still break when price, competition, coverage, and scripts hit estimates.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,),
    ),
    Round152CaseCandidate(
        "hims_branded_glp1_pivot_loss_case",
        "GLP1_TELEHEALTH_CHANNEL",
        "HIMS",
        "Hims branded GLP-1 pivot and unexpected loss",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 12),
        ("telehealth_glp1_channel", "branded_drug_pivot"),
        ("revenue_miss", "unexpected_loss", "restructuring_cost", "revenue_recognition_timing", "margin_pressure"),
        "telehealth_channel_volatility",
        "needs_price_backfill",
        ("round_152.md Reuters Hims GLP-1 revenue miss",),
        "Telehealth GLP-1 channel stories require legal channel, CAC, margin, revenue recognition, and FCF checks.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION, E2RArchetype.COMPOUNDED_GLP1_REGULATORY_RISK),
    ),
    Round152CaseCandidate(
        "hims_compounded_glp1_crackdown_case",
        "COMPOUNDED_GLP1_REGULATORY_RISK",
        "HIMS",
        "Hims compounded GLP-1 regulatory crackdown",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 2, 7),
        ("compounded_drug_flag", "compounded_glp1_channel", "online_pharmacy"),
        ("fda_crackdown_flag", "doj_referral_flag", "unapproved_copycat_flag", "compounded_quality_issue", "channel_shutdown"),
        "compounded_glp1_regulatory_4c_watch",
        "needs_price_backfill",
        ("round_152.md Reuters Hims compounded GLP-1 crackdown",),
        "Large obesity demand does not offset an unproven or illegal drug-channel risk.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION, E2RArchetype.GLP1_TELEHEALTH_CHANNEL),
    ),
    Round152CaseCandidate(
        "bluebird_gene_therapy_cash_crunch_case",
        "GENE_THERAPY_RARE_DISEASE",
        "BLUE",
        "bluebird bio gene therapy cash crunch",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 2, 21),
        ("approved_gene_therapies",),
        ("cash_crunch", "slow_uptake", "discounted_take_private", "going_concern", "commercialization_failure"),
        "gene_therapy_cash_crunch",
        "needs_price_backfill",
        ("round_152.md Reuters bluebird bio take-private cash crunch",),
        "Approved gene therapies still fail E2R if uptake, reimbursement, and cash runway do not support FCF.",
    ),
    Round152CaseCandidate(
        "charles_river_cro_funding_crunch_case",
        "CRO_FUNDING_CYCLE_OVERLAY",
        "CRL",
        "Charles River CRO funding crunch",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 8, 7),
        ("cro_service_revenue",),
        ("biotech_funding_crunch", "forecast_cut", "revenue_decline", "customer_budget_cut"),
        "cro_funding_cycle_4c_watch",
        "needs_price_backfill",
        ("round_152.md Reuters Charles River forecast cut",),
        "CRO is service revenue, but funding-cycle cuts can break backlog and forecast visibility.",
        (E2RArchetype.CRO_CLINICAL_SERVICE,),
    ),
    Round152CaseCandidate(
        "teladoc_betterhelp_impairment_case",
        "TELEHEALTH_BEHAVIORAL_HEALTH",
        "TDOC",
        "Teladoc BetterHelp impairment and DTC unit economics failure",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 8, 1),
        ("telehealth_usage", "behavioral_health_platform"),
        ("impairment_charge", "forecast_withdrawal", "advertising_cost_increase", "cac_spike", "revenue_slowdown"),
        "telehealth_dtc_failure_4c",
        "needs_price_backfill",
        ("round_152.md Reuters Teladoc record low",),
        "Telehealth demand is not enough when CAC, impairment, churn, privacy, and FCF are weak.",
    ),
    Round152CaseCandidate(
        "recursion_exscientia_ai_drug_case",
        "AI_DRUG_DISCOVERY_PLATFORM",
        "RXRX",
        "Recursion Exscientia AI drug discovery platform merger",
        "US",
        "success_candidate",
        None,
        date(2024, 8, 8),
        None,
        None,
        None,
        ("ai_drug_discovery_platform", "pipeline_combination", "cash_runway", "candidate_molecules"),
        ("no_approved_drug", "clinical_validation_unproven", "cash_burn", "platform_hype"),
        "ai_drug_platform_watch",
        "needs_price_backfill",
        ("round_152.md Reuters Recursion Exscientia merger",),
        "AI drug-discovery consolidation is Watch until milestones, clinical proof, and commercial economics appear.",
    ),
    Round152CaseCandidate(
        "lunit_dbt_subgroup_validation_case",
        "MEDICAL_AI_EXTERNAL_VALIDATION",
        "328130",
        "Lunit DBT external validation and subgroup risk",
        "KR",
        "success_candidate",
        None,
        date(2025, 3, 17),
        None,
        None,
        None,
        ("external_validation_flag", "ai_model_auc", "clinical_ai_paper", "subgroup_performance_risk"),
        ("subgroup_performance_risk", "no_reimbursement_verified", "hospital_adoption_unverified", "workflow_integration_unverified", "liability_risk"),
        "ai_clinical_validation_not_commercial",
        "needs_price_backfill",
        ("round_152.md arXiv Lunit DBT subgroup performance",),
        "AUC and external validation support Stage 1/2, but reimbursement, hospital workflow, and recurring revenue are separate gates.",
        (E2RArchetype.DIGITAL_HEALTHCARE_AI, E2RArchetype.MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK),
    ),
    Round152CaseCandidate(
        "amgen_samsung_bioepis_biosimilar_litigation_case",
        "BIOSIMILAR_PATENT_LITIGATION",
        "BIOSIMILAR_LITIGATION_REF",
        "Amgen / Samsung Bioepis biosimilar patent litigation risk",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 8, 13),
        ("biosimilar_application", "patent_litigation", "launch_timing_risk"),
        ("patent_litigation", "launch_delay", "pbm_exclusion", "price_competition", "margin_compression"),
        "biosimilar_patent_litigation_4c_watch",
        "missing_direct_symbol_mapping",
        ("round_152.md Reuters Amgen Samsung Bioepis patent litigation",),
        "Biosimilar approval or filing is not enough when patent litigation can delay launch and damage economics.",
        (E2RArchetype.BIOSIMILAR_COMMERCIALIZATION, E2RArchetype.REIMBURSEMENT_ACCESS_OVERLAY),
    ),
    Round152CaseCandidate(
        "botox_counterfeit_fda_warning_case",
        "DEVICE_SAFETY_COUNTERFEIT_OVERLAY",
        "BOTOX_SAFETY_REF",
        "FDA counterfeit Botox safety warning",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 11, 5),
        ("aesthetic_procedure_demand",),
        ("counterfeit_product", "unapproved_product", "injury_report", "licensed_channel_failure"),
        "device_safety_regulatory_4c",
        "missing_direct_symbol_mapping",
        ("round_152.md AP FDA unapproved Botox warning",),
        "Aesthetic demand cannot offset counterfeit, unapproved-product, and safety-channel risks.",
        (E2RArchetype.BOTULINUM_AESTHETIC_REGULATED,),
    ),
)


ROUND152_PRICE_FIELDS: tuple[str, ...] = (
    "case_id",
    "symbol",
    "company_name",
    "primary_archetype",
    "secondary_archetypes",
    "stage1_date",
    "stage2_date",
    "stage3_date",
    "stage4b_date",
    "stage4c_date",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "peak_date",
    "MFE_30D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_30D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "drawdown_after_peak",
    "below_stage2_price_flag",
    "below_stage3_price_flag",
    "contract_value",
    "contract_duration",
    "contract_duration_months",
    "customer_name",
    "facility_location",
    "us_manufacturing_site_flag",
    "tariff_hedge_flag",
    "technology_transfer_flag",
    "capacity_liters",
    "capacity_utilization",
    "adc_capability_flag",
    "cell_gene_capability_flag",
    "us_operating_cost",
    "capex_amount",
    "backlog_growth",
    "customer_concentration",
    "op_margin_change",
    "fcf_margin",
    "prescription_volume",
    "weekly_scripts",
    "prescriber_count",
    "new_prescriber_ratio",
    "insurance_coverage",
    "pbm_listing_flag",
    "pbm_coverage_flag",
    "zero_copay_flag",
    "formulary_preferred_flag",
    "biosimilar_discount_pct",
    "biosimilar_approval_flag",
    "interchangeable_flag",
    "biosimilar_prescription_volume",
    "price_discount_pct",
    "margin_compression_flag",
    "prescription_conversion_rate",
    "drug_price_change",
    "price_war_flag",
    "monthly_price",
    "gross_to_net_discount",
    "gross_to_net_visible_flag",
    "refill_rate",
    "script_growth_rate",
    "generic_competition_flag",
    "telehealth_channel_flag",
    "coverage_gap_flag",
    "pbm_exclusion_flag",
    "patent_litigation_flag",
    "launch_delay_flag",
    "compounded_alternative_flag",
    "oral_glp1_flag",
    "maintenance_therapy_flag",
    "injection_to_pill_switch_flag",
    "self_pay_price",
    "boxed_warning_flag",
    "real_world_adherence_signal",
    "compounded_drug_flag",
    "fda_crackdown_flag",
    "doj_referral_flag",
    "unapproved_copycat_flag",
    "branded_drug_attach_rate",
    "legal_settlement_flag",
    "legal_cost",
    "restructuring_cost",
    "revenue_recognition_issue_flag",
    "launch_date",
    "commercial_revenue",
    "clinical_trial_phase",
    "approval_status",
    "milestone_payment",
    "big_pharma_partner",
    "pipeline_count",
    "ai_platform_flag",
    "approved_drug_count",
    "patient_uptake",
    "reimbursement_status",
    "cash_runway_months",
    "cash_runway_years",
    "going_concern_flag",
    "dilution_or_take_private_flag",
    "dilution_flag",
    "take_private_flag",
    "discounted_take_private_flag",
    "hospital_adoption_count",
    "reimbursement_code_flag",
    "paid_workflow_flag",
    "recurring_revenue_ratio",
    "ai_model_auc",
    "external_validation_flag",
    "workflow_integration_flag",
    "subgroup_performance_risk",
    "dataset_bias_flag",
    "dense_tissue_underperformance_flag",
    "calcification_underperformance_flag",
    "liability_risk_flag",
    "device_export_country_count",
    "installed_base",
    "surgical_robot_installed_base",
    "system_placement_count",
    "system_placements",
    "procedure_volume",
    "procedure_growth",
    "procedure_growth_rate",
    "instruments_accessories_revenue",
    "consumable_revenue_ratio",
    "hospital_capex_cycle_flag",
    "hospital_capex_risk",
    "procedure_mix_risk",
    "procedure_mix_risk_flag",
    "procedure_mix_shift_flag",
    "bariatric_slowdown_flag",
    "glp1_bariatric_slowdown_flag",
    "vbp_price_control_flag",
    "asp_change",
    "asp_drop_flag",
    "fda_warning_flag",
    "licensed_channel_flag",
    "counterfeit_safety_flag",
    "unapproved_product_flag",
    "fda_ftc_scrutiny_flag",
    "compounded_quality_issue_flag",
    "doj_referral_risk_flag",
    "advertising_cost_change",
    "cac",
    "churn",
    "privacy_incident_flag",
    "impairment_charge",
    "forecast_withdrawal_flag",
    "opendart_rcept_no",
    "opendart_detail_fetched_flag",
    "disclosure_confidence_score",
    "detail_parser_confidence",
    "disclosure_signal_class",
    "routine_disclosure_flag",
    "risk_disclosure_flag",
    "high_signal_disclosure_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def round152_target_for(target_id: str) -> Round152ScoreTarget | None:
    for target in ROUND152_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round152_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND152_CASE_CANDIDATES:
        target = round152_target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        stage4b_evidence = candidate.evidence_fields if candidate.case_type == "4b_watch" or candidate.stage4b_date else ()
        stage4c_evidence = candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" or candidate.stage4c_date else ()
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
                f"Round152 R7 Loop-9 case for {candidate.target_id}; "
                "approval, AI, capacity, telehealth, and device narratives are separated from commercialization evidence."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions),
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
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint=_score_weight_hint(target),
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "approval_or_clinical_news_is_not_revenue",
                "paper_auc_or_ai_label_is_not_green_evidence_alone",
                "commercialization_reimbursement_fcf_required_for_green",
                "capacity_without_utilization_is_not_stage3",
                "glp1_tam_is_not_green_without_scripts_coverage_price_and_eps",
                "compounded_glp1_channel_is_redteam_gate",
                "external_validation_is_not_paid_deployment",
                "do_not_invent_prescriptions_reimbursement_capacity_uptake_cash_runway_hospital_adoption_external_validation_or_stage_prices",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round152_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND152_SCORE_TARGETS:
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
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "loop9_penalty_axes": "|".join(target.loop9_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round152_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND152_CASE_CANDIDATES:
        target = round152_target_for(candidate.target_id)
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


def round152_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop9_penalty_axes": "|".join(target.loop9_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND152_SCORE_TARGETS
    )


def round152_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round152_backfill": "true"} for field in ROUND152_PRICE_FIELDS)


def round152_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "component": item.component,
            "weight": str(item.weight),
            "interpretation": item.interpretation,
            "production_scoring_changed": "false",
        }
        for item in ROUND152_BASE_SCORE_WEIGHTS
    )


def round152_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "cap_id": item.cap_id,
            "max_stage": item.max_stage,
            "condition": item.condition,
            "example": item.example,
            "production_scoring_changed": "false",
        }
        for item in ROUND152_STAGE_CAPS
    )


def round152_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": item.case_id,
            "score_stage": item.score_stage,
            "price_path_signal": item.price_path_signal,
            "verdict": item.verdict,
            "normalization_adjustment": item.normalization_adjustment,
            "production_scoring_changed": "false",
        }
        for item in ROUND152_SCORE_STAGE_PRICE_ALIGNMENT
    )


def round152_summary() -> dict[str, int | bool]:
    records = round152_case_records()
    return {
        "target_count": len(ROUND152_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "base_score_component_count": len(ROUND152_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND152_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND152_SCORE_STAGE_PRICE_ALIGNMENT),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND152_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND152_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND152_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND152_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round152_r7_loop9_reports(
    *,
    output_directory: str | Path = ROUND152_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND152_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND152_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round152_r7_loop9_biotech_healthcare_device_summary.md",
        "case_matrix": output / "round152_r7_loop9_case_matrix.csv",
        "stage_date_plan": output / "round152_r7_loop9_stage_date_plan.csv",
        "green_guardrails": output / "round152_r7_loop9_green_guardrails.md",
        "risk_overlays": output / "round152_r7_loop9_risk_overlays.md",
        "price_validation_plan": output / "round152_r7_loop9_price_validation_plan.md",
        "price_fields": output / "round152_r7_loop9_price_fields.csv",
        "base_score_weights": output / "round152_r7_loop9_base_score_weights.csv",
        "stage_caps": output / "round152_r7_loop9_stage_caps.csv",
        "score_stage_price_alignment": output / "round152_r7_loop9_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round152_r7_loop9_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round152_case_records(), cases)
    _write_rows(round152_score_profile_rows(), score_profiles)
    _write_rows(round152_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round152_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round152_price_field_rows(), paths["price_fields"])
    _write_rows(round152_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round152_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round152_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round152_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round152_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round152_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round152_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(
        render_round152_score_stage_price_alignment_markdown(),
        encoding="utf-8",
    )
    return paths


def render_round152_summary_markdown() -> str:
    summary = round152_summary()
    lines = [
        "# Round-152 R7 Loop-9 Biotech / Healthcare / Medical Device Summary",
        "",
        f"- source_round: `{ROUND152_SOURCE_ROUND_PATH}`",
        "- large_sector: `BIOTECH_HEALTHCARE_DEVICE`",
        "- loop: `R7 Loop 9 / v9.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_component_count: {summary['base_score_component_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        f"- gate_only_target_count: {summary['gate_only_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R7 Loop 9 says approval, clinical success, AI papers, and TAM are not commercialization by themselves.",
        "- Example: CDMO capacity is useful, but utilization, customer contracts, OPM, and FCF decide Stage 3 review.",
        "- Example: GLP-1 approval is Stage 1/2; weekly scripts, insurance, price defense, and OP/EPS must follow.",
        "- Example: medical AI AUC supports research quality, but hospital adoption, reimbursement, and recurring revenue decide higher stages.",
        "- Example: gene therapy approval can still become 4C if uptake, reimbursement, and cash runway fail.",
    ]
    return "\n".join(lines) + "\n"


def render_round152_green_guardrail_markdown() -> str:
    lines = [
        "# Round-152 R7 Loop-9 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-9 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND152_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.loop9_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R7 Loop-9 v9.0 weights to production scoring yet.",
            "- Do not treat FDA/EMA approval, clinical success, AI model AUC, external-validation paper, pilot, user growth, or disease-event demand as Green evidence by itself.",
            "- Do not invent prescription volume, PBM/insurance coverage, reimbursement, capacity utilization, patient uptake, hospital adoption, external validation, procedure volume, consumable revenue, cash runway, CAC, churn, legal costs, restructuring costs, or stage prices.",
            "- Green requires commercialization, reimbursement, recurring revenue, FCF conversion, contracted utilization, or repeated procedure/consumable evidence.",
            "- Treat slow uptake, cash crunch, dilution, take-private, forecast cut, FDA crackdown, DOJ referral, unapproved copycat, biosimilar patent litigation, privacy breach, impairment, counterfeit product, safety issue, price control, and one-off diagnostic normalization as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round152_risk_overlay_markdown() -> str:
    lines = [
        "# Round-152 R7 Loop-9 Risk Overlays",
        "",
        "- `COMMERCIALIZATION_ALIGNED`: approval/contract is followed by prescriptions, revenue, OPM, FCF, or price-path confirmation.",
        "- `APPROVAL_WITHOUT_UPTAKE`: approval exists, but prescription, reimbursement, patient uptake, or sales are weak.",
        "- `CAPACITY_WITHOUT_UTILIZATION`: CDMO/device capacity exists, but utilization and customer contracts are unverified.",
        "- `US_CAPACITY_TARIFF_HEDGE_BUT_DELAYED_PRICE`: US CDMO capacity improves strategic positioning, but customer contract, technology transfer, utilization, OPM, and FCF still gate Stage 3.",
        "- `GLP1_APPROVAL_BUT_SCRIPT_GATE`: GLP-1 approval exists, but weekly scripts, coverage, and price defense are not yet proven.",
        "- `ORAL_GLP1_MAINTENANCE_STAGE2`: oral approval or switch-maintenance data is useful, but refills, coverage, price, adherence, and OP/EPS decide promotion.",
        "- `COMPOUNDED_GLP1_REGULATORY_BREAK`: compounded or unapproved GLP-1 channels become RedTeam gates when FDA, DOJ, quality, or copycat risks appear.",
        "- `GLP1_4B_TO_4C`: obesity-market narrative breaks through price, competition, coverage, or compounded-drug pressure.",
        "- `TELEHEALTH_CHANNEL_VOLATILITY`: telehealth partnership, compounded drug, branded pivot, CAC, or revenue recognition drives unstable price action.",
        "- `AI_CLINICAL_VALIDATION_NOT_COMMERCIAL`: AI paper or AUC is strong, but deployment, reimbursement, and recurring revenue are missing.",
        "- `MEDICAL_AI_EXTERNAL_VALIDATION`: external validation can lift Stage 1/2, but hospital adoption and paid workflow are separate gates.",
        "- `BIOSIMILAR_PATENT_LITIGATION`: approval-led narratives can break if litigation delays launch or compresses economics.",
        "- `BIOSIMILAR_ACCESS_WITHOUT_UPTAKE`: discount or cash-pay access helps patients, but does not prove prescription switching or margin defense.",
        "- `GENE_THERAPY_CASH_CRUNCH`: approved therapy fails because uptake, reimbursement, and cash runway break.",
        "- `GLP1_PRICE_WAR_4C`: price cuts, gross-to-net pressure, copycats, or insurance pressure can turn GLP-1 TAM into a thesis break.",
        "- `DISCLOSURE_CONFIDENCE_CAP`: missing contract amount, term, counterparty, reimbursement, prescription, or fee fields cap Stage 3 confidence.",
        "- `DEVICE_SAFETY_REGULATORY_4C`: device, Botox, implant, counterfeit, VBP, or safety risk blocks unsafe Green.",
        "- `SURGICAL_ROBOT_RECURRING_CONSUMABLE_SUCCESS`: installed base, procedure growth, and instruments/accessories revenue move together.",
        "",
        "Simple example: `FDA 허가` is useful Stage 1/2 evidence. It is not Green if scripts, coverage, revenue, and FCF are still missing.",
    ]
    return "\n".join(lines) + "\n"


def render_round152_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-152 R7 Loop-9 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare capacity, utilization, prescriptions, PBM/insurance, reimbursement, patient uptake, hospital adoption, procedure volume, consumables, cash runway, CAC, churn, safety, and regulatory events with price path.",
        "6. Mark capacity-without-utilization, approval-without-uptake, GLP-1 4B-to-4C, telehealth volatility, AI validation-not-commercial, gene-therapy cash crunch, and device safety 4C explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round152_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `COMMERCIALIZATION_ALIGNED`: commercialization, utilization, prescriptions, procedures, reimbursement, or FCF moves with price rerating.",
            "- `APPROVAL_WITHOUT_UPTAKE`: approval exists but patient uptake, reimbursement, prescriptions, or sales are missing.",
            "- `CAPACITY_WITHOUT_UTILIZATION`: capacity/site expansion exists, but contract and utilization are still missing.",
            "- `GLP1_APPROVAL_BUT_SCRIPT_GATE`: approval is useful, but weekly scripts, insurance, price defense, and OP/EPS still gate Green.",
            "- `GLP1_4B_TO_4C`: price/competition/coverage/compounded-drug pressure breaks a GLP-1 narrative.",
            "- `GLP1_PRICE_WAR_4C`: price cuts, gross-to-net pressure, copycat pressure, or insurance pressure break price defense.",
            "- `TELEHEALTH_CHANNEL_VOLATILITY`: partnership or channel change creates price action without durable economics.",
            "- `BIOSIMILAR_ACCESS_WITHOUT_UPTAKE`: access program exists but prescription conversion, PBM incentives, or margin defense are not verified.",
            "- `AI_CLINICAL_VALIDATION_NOT_COMMERCIAL`: paper/AUC validates model quality but not paid deployment.",
            "- `GENE_THERAPY_CASH_CRUNCH`: approval fails to convert into cash-flow-safe commercialization.",
            "- `DISCLOSURE_CONFIDENCE_CAP`: key disclosed terms are missing, so Stage 3 confidence must be capped.",
            "- `DEVICE_SAFETY_REGULATORY_4C`: counterfeit, VBP, safety, or unapproved-channel risk blocks Green.",
            "- `SURGICAL_ROBOT_RECURRING_CONSUMABLE_SUCCESS`: installed base, procedure growth, and consumable revenue validate recurring medtech economics.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round152_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-152 R7 Loop-9 Score / Stage / Price Alignment",
        "",
        "Round 152 checks whether R7 healthcare evidence is actually moving from science, approval, and TAM into commercialization, recurring revenue, and price-path confirmation.",
        "This is calibration material only; it does not change production scoring.",
        "",
        "| case | score-stage view | price-path signal | verdict | normalization adjustment |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in ROUND152_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(
            "| "
            f"`{item.case_id}` | {item.score_stage} | {item.price_path_signal} | "
            f"{item.verdict} | {item.normalization_adjustment} |"
        )
    lines.extend(
        [
            "",
            "## What This Means",
            "",
            "- Approval, AUC, TAM, and capacity can open Stage 1/2, but Stage 3 waits for scripts, reimbursement, repeat revenue, utilization, OPM/FCF, and price-path alignment.",
            "- RedTeam overlays such as GLP-1 price war, compounded-drug crackdown, cash crunch, patent litigation, subgroup AI failure, and device safety can block or break promotion.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round152CaseCandidate) -> str:
    if candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type == "structural_success":
        return "aligned"
    if candidate.case_type == "success_candidate" and "aligned" in candidate.alignment_hint:
        return "aligned"
    if candidate.case_type == "success_candidate" and "structural_candidate" in candidate.alignment_hint:
        return "aligned"
    return "unknown"


def _rerating_result(candidate: Round152CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown"


def _score_weight_hint(target: Round152ScoreTarget) -> dict[str, float]:
    weights = target.score_weight.as_dict()
    return {
        "eps_fcf": _numeric_weight(weights["eps_fcf"]),
        "visibility": _numeric_weight(weights["structural_visibility"]),
        "bottleneck": _numeric_weight(weights["bottleneck_pricing"]),
        "mispricing": _numeric_weight(weights["market_mispricing"]),
        "valuation": _numeric_weight(weights["valuation"]),
        "capital_allocation": _numeric_weight(weights["capital_allocation"]),
    }


def _numeric_weight(value: int | str) -> float:
    if isinstance(value, int):
        return float(value)
    return 0.0


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
    "ROUND152_BASE_SCORE_WEIGHTS",
    "ROUND152_CASE_CANDIDATES",
    "ROUND152_DEFAULT_CASES_PATH",
    "ROUND152_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND152_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND152_PRICE_FIELDS",
    "ROUND152_SCORE_TARGETS",
    "ROUND152_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND152_STAGE_CAPS",
    "Round152BaseScoreWeight",
    "Round152CaseCandidate",
    "Round152ScoreStagePriceAlignment",
    "Round152ScoreTarget",
    "Round152ScoreWeightDraft",
    "Round152StageCap",
    "render_round152_green_guardrail_markdown",
    "render_round152_price_validation_plan_markdown",
    "render_round152_risk_overlay_markdown",
    "render_round152_score_stage_price_alignment_markdown",
    "render_round152_summary_markdown",
    "round152_base_score_weight_rows",
    "round152_case_candidate_rows",
    "round152_case_records",
    "round152_price_field_rows",
    "round152_score_stage_price_alignment_rows",
    "round152_score_profile_rows",
    "round152_stage_cap_rows",
    "round152_stage_date_rows",
    "round152_summary",
    "round152_target_for",
    "write_round152_r7_loop9_reports",
]
