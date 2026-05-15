"""Round-28 cases_v10 expansion and score-weight v1.3 hypotheses.

Round 28 broadens calibration into nuclear/SMR, strategic metals,
data-center REITs, AI power PPAs, grid flexibility, policy-event themes,
NFT/metaverse, speculative advanced materials, value-up, and integrated AI
infrastructure. It is report-only calibration material. Production feature
engineering, scoring, staging, and RedTeam code must not import this module.
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


ROUND28_SOURCE_ROUND_PATH = "docs/round/round_28.md"
ROUND28_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round28_score_weight_v13"
ROUND28_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v10_round28.jsonl"
ROUND28_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round28_v13.csv"


@dataclass(frozen=True)
class Round28ScoreWeightDraft:
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
class Round28ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round28ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    normalization_point: str

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round28CaseCandidate:
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


ROUND28_SCORE_TARGETS: tuple[Round28ScoreTarget, ...] = (
    Round28ScoreTarget(
        "NUCLEAR_SMR_GRID_POLICY",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round28ScoreWeightDraft(18, 22, 10, 14, 12, 2, 5),
        ("nuclear_policy", "smr_keyword", "ai_power_demand", "reactor_restart"),
        ("ppa_or_power_contract", "licensed_project", "equipment_revenue_path", "financing_visible"),
        ("long_term_power_contract", "low_licensing_risk", "fy2_fy3_revenue_visibility", "cost_overrun_risk_low"),
        ("actual_ppa_or_long_term_contract", "licensed_or_restarted_asset", "equipment_revenue_path", "legal_risk_low", "financing_visible"),
        ("licensing", "cost_overrun", "legal_delay", "project_financing", "loi_only", "smr_theme_only"),
        ("project_cancelled", "cost_overrun", "licensing_delay", "financing_failure", "ppa_missing"),
        "Nuclear/SMR is Watch-to-Green: existing nuclear PPA can score, but SMR theme or LOI alone cannot.",
    ),
    Round28ScoreTarget(
        "RARE_METALS_STRATEGIC_MATERIALS",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round28ScoreWeightDraft(18, 18, 18, 14, 13, 5, 5),
        ("rare_earth_keyword", "lithium_or_copper_price", "geopolitical_supply_chain", "government_support"),
        ("government_support", "price_floor", "offtake_agreement", "production_capacity"),
        ("government_or_defense_customer", "long_term_offtake", "fcf_conversion", "production_execution"),
        ("government_support", "price_floor_or_purchase_guarantee", "long_term_offtake", "production_capacity", "fcf_conversion"),
        ("commodity_price", "geopolitical_policy", "project_execution", "governance_event", "price_theme_only"),
        ("commodity_price_collapse", "project_execution_failure", "governance_dispute", "offtake_failure"),
        "Strategic metals can be Green only when offtake, price floor, production, and FCF are source-backed.",
    ),
    Round28ScoreTarget(
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round28ScoreWeightDraft(18, 23, 18, 13, 13, 5, 5),
        ("ai_datacenter_demand", "reit_or_idc_asset", "hyperscale_tenant", "liquid_cooling_facility"),
        ("hyperscale_lease", "power_cooling_land_secured", "occupancy_high", "ffo_affo_growth"),
        ("tenant_quality", "funding_cost_controlled", "ffo_affo_visibility", "power_water_constraint_low"),
        ("hyperscale_tenant_long_lease", "power_cooling_land_secured", "ffo_affo_growth", "occupancy_high", "funding_cost_controlled"),
        ("capex_burden", "power_water_constraint", "tenant_concentration", "funding_cost", "asset_not_operational"),
        ("capex_burden", "funding_cost_spike", "tenant_loss", "power_water_constraint", "affo_dilution"),
        "Data-center REITs are Green-possible, but FFO/AFFO, occupancy, tenant quality, and funding cost are gates.",
    ),
    Round28ScoreTarget(
        "UTILITIES_AI_POWER_PPA",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round28ScoreWeightDraft(17, 22, 12, 12, 10, 5, 5),
        ("ai_power_demand", "utility_power_supply", "nuclear_life_extension", "ppa_headline"),
        ("long_term_ppa", "tariff_or_price_visible", "capacity_secured", "regulatory_risk_low"),
        ("stable_cash_flow", "fcf_or_dividend_stability", "grid_connection_confirmed", "debt_risk_low"),
        ("long_term_ppa", "power_sale_price_visible", "capacity_secured", "regulatory_risk_low", "fcf_or_dividend_stability"),
        ("regulation", "tariff", "debt", "grid_connection", "capex", "power_demand_theme_only"),
        ("tariff_no_pass_through", "debt_capex_burden", "grid_connection_delay", "policy_reversal"),
        "Utilities with AI PPA can score, but power-demand theme without tariff/FCF visibility stays Watch.",
    ),
    Round28ScoreTarget(
        "SMART_GRID_FLEXIBLE_DATACENTER",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round28ScoreWeightDraft(18, 18, 16, 13, 11, 2, 6),
        ("smart_grid", "ess", "grid_interactive_datacenter", "peak_power_reduction_demo"),
        ("datacenter_or_utility_customer", "repeat_software_or_service_revenue", "regulatory_incentive", "commercialization_path"),
        ("paid_grid_flexibility_service", "verified_peak_reduction", "utility_adoption", "op_fcf_conversion"),
        ("datacenter_or_utility_customer", "repeat_software_or_service_revenue", "verified_peak_reduction", "regulatory_incentive", "commercialization_path"),
        ("commercialization", "utility_adoption", "regulation", "project_delay", "poc_only", "no_revenue_model"),
        ("utility_adoption_delay", "project_delay", "no_revenue_model", "regulatory_incentive_failure"),
        "Smart-grid flexibility is Watch-to-Green: PoC is not enough without customer, repeat revenue, and commercialization.",
    ),
    Round28ScoreTarget(
        "NORTH_KOREA_POLICY_EVENT",
        Round10LargeSector.POLICY_GEOPOLITICAL_EVENT,
        E2RArchetype.ONE_OFF_EVENT_DEMAND,
        Round10ThemePosture.REDTEAM_FIRST,
        Round28ScoreWeightDraft(5, 5, 5, 8, 5, 0, 3),
        ("inter_korea_policy", "dmz_theme", "kaesong_reopen_expectation", "kumgang_tourism_expectation"),
        ("actual_business_reopen_contract", "sanction_relief_confirmed", "cash_flow_path"),
        ("multi_year_contract", "revenue_recognition", "security_risk_low"),
        ("actual_contract", "revenue_recognition", "security_risk_low", "sanction_relief_confirmed"),
        ("extreme_policy_security", "military_risk", "sanction", "event_only", "no_cash_flow"),
        ("military_security_risk", "sanction_tightening", "diplomacy_breakdown", "business_suspension"),
        "North Korea policy themes are RedTeam-first event premium; Green is effectively blocked without real contracts and cash flow.",
    ),
    Round28ScoreTarget(
        "METAVERSE_NFT_THEME",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round28ScoreWeightDraft(5, 5, 5, 6, 5, 0, 3),
        ("nft_keyword", "metaverse_keyword", "digital_collectible", "token_volume_spike"),
        ("repeat_platform_revenue", "stable_fee_revenue", "regulatory_risk_low"),
        ("eps_fcf_conversion", "customer_lock_in", "sustainable_transaction_fee"),
        ("repeat_platform_revenue", "stable_fee_revenue", "eps_fcf_conversion", "regulatory_risk_low"),
        ("extreme_theme", "no_revenue", "liquidity_collapse", "price_only_rally", "speculative_volume"),
        ("liquidity_collapse", "revenue_model_failure", "regulatory_hit", "user_activity_collapse"),
        "NFT/metaverse is RedTeam-first; separate regulated payment/tokenization infra from speculative NFT themes.",
    ),
    Round28ScoreTarget(
        "ADVANCED_MATERIAL_SPECULATIVE_THEME",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round28ScoreWeightDraft(5, 5, 5, 5, 5, 0, 3),
        ("superconductor_keyword", "mxene_keyword", "graphene_keyword", "quantum_policy", "sample_or_patent"),
        ("commercial_customer", "product_supply_contract", "revenue_recognition"),
        ("repeat_revenue", "eps_fcf_conversion", "customer_contracts"),
        ("product_supply_contract", "commercial_customer", "revenue_recognition", "eps_fcf_conversion"),
        ("extreme_speculative", "no_commercialization", "paper_only", "sample_only", "no_contract"),
        ("commercialization_failure", "contract_absence", "technology_reversal", "liquidity_collapse"),
        "Advanced-material narratives are Green-restricted until products, customers, contracts, revenue, and FCF exist.",
    ),
    Round28ScoreTarget(
        "VALUE_UP_SHAREHOLDER_RETURN",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round28ScoreWeightDraft(12, 18, 4, 20, 25, 10, 5),
        ("low_pbr", "value_up_index", "buyback_or_dividend", "nav_discount"),
        ("roe_improvement", "buyback_cancellation", "repeat_shareholder_return", "dividend_sustainability"),
        ("pbr_roe_frame_change", "nav_discount_close", "capital_return_execution", "fcf_support"),
        ("roe_improvement", "actual_cancellation", "repeat_shareholder_return", "dividend_sustainability", "nav_or_pbr_discount_logic"),
        ("governance", "execution", "low_roe", "no_cancellation", "index_inclusion_only", "weak_fcf"),
        ("return_execution_failure", "roe_deterioration", "governance_risk", "fcf_shortfall"),
        "Value-up is Green-possible only with ROE, actual cancellation, repeat return, and discount closure evidence.",
    ),
    Round28ScoreTarget(
        "AI_DATA_CENTER_INFRASTRUCTURE",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round28ScoreWeightDraft(22, 23, 20, 14, 12, 2, 5),
        ("ai_capex", "power_cooling_server_network", "datacenter_reit", "power_ppa"),
        ("orders_or_leases", "capex_visibility", "op_eps_revision", "bottleneck_asset"),
        ("multi_axis_infra_bottleneck", "delivery_or_lease_revenue", "project_delay_low", "old_frame_removed"),
        ("orders_or_leases", "power_or_cooling_or_network_bottleneck", "op_eps_revision", "capex_visibility", "project_delay_low"),
        ("ai_capex_cut", "project_delay", "grid_constraint", "overbuild", "no_revenue_exposure"),
        ("ai_capex_cut", "project_delay", "grid_interconnection_delay", "overbuild", "revenue_exposure_failure"),
        "AI data-center infrastructure is Green-possible, but each sub-axis needs its own evidence rather than AI-theme grouping.",
    ),
)


ROUND28_CASE_CANDIDATES: tuple[Round28CaseCandidate, ...] = (
    Round28CaseCandidate("meta_constellation_20y_nuclear_ppa_success_candidate", "NUCLEAR_SMR_GRID_POLICY", "CEG_META", "Meta-Constellation 20y nuclear PPA", "US", "success_candidate", ("actual_ppa_or_long_term_contract", "licensed_or_restarted_asset"), ("legal_delay", "regulatory_risk"), "Existing nuclear PPA is stronger than generic SMR theme."),
    Round28CaseCandidate("microsoft_tmi_reopen_ppa_candidate", "NUCLEAR_SMR_GRID_POLICY", "TMI_MSFT", "Microsoft TMI restart PPA", "US", "success_candidate", ("reactor_restart", "ppa_or_power_contract"), ("licensing_delay", "cost_overrun"), "Restart PPA candidate still needs licensing and economics verification."),
    Round28CaseCandidate("nuscale_uamps_cost_cancel_4c", "NUCLEAR_SMR_GRID_POLICY", "SMR_CANCEL_4C", "NuScale UAMPS cost cancel", "US", "4c_thesis_break", ("smr_project",), ("project_cancelled", "cost_overrun"), "SMR cost escalation and cancellation are hard 4C-style evidence."),
    Round28CaseCandidate("smr_policy_no_financing_counterexample", "NUCLEAR_SMR_GRID_POLICY", "SMR_POLICY", "SMR정책_금융미확정", "KR", "failed_rerating", ("smr_policy",), ("loi_only", "project_financing"), "SMR policy or LOI without financing is not Green evidence."),
    Round28CaseCandidate("mp_materials_dod_price_floor_offtake_success_candidate", "RARE_METALS_STRATEGIC_MATERIALS", "MP", "MP Materials DoD price floor offtake", "US", "success_candidate", ("government_support", "price_floor_or_purchase_guarantee", "long_term_offtake"), ("project_execution", "commodity_price"), "DoD support plus price floor/offtake is rare-metals visibility evidence."),
    Round28CaseCandidate("korea_zinc_tender_event_premium", "RARE_METALS_STRATEGIC_MATERIALS", "010130", "Korea Zinc tender event premium", "KR", "event_premium", ("tender_offer", "governance_event"), ("governance_event", "event_only"), "Tender offer can move price without structural FCF rerating."),
    Round28CaseCandidate("pure_rare_earth_price_theme_counterexample", "RARE_METALS_STRATEGIC_MATERIALS", "RARE_PRICE", "희토류가격테마", "KR", "failed_rerating", ("rare_earth_keyword",), ("price_theme_only", "commodity_price"), "Rare-earth price news alone is commodity/theme evidence."),
    Round28CaseCandidate("mining_project_no_production_counterexample", "RARE_METALS_STRATEGIC_MATERIALS", "MINE_NOPROD", "광산개발_무생산", "KR", "failed_rerating", ("mining_project_plan",), ("no_production", "project_execution"), "Mining plan without production and sales is not FCF evidence."),
    Round28CaseCandidate("blackstone_digital_infra_reit_candidate", "DATA_CENTER_REIT_INFRASTRUCTURE", "BDIV", "Blackstone digital infra REIT", "US", "success_candidate", ("reit_or_idc_asset", "hyperscale_tenant"), ("funding_cost", "capex_burden"), "Data-center REIT candidate needs FFO/AFFO and tenant quality validation."),
    Round28CaseCandidate("equinix_malaysia_ai_liquid_cooling_candidate", "DATA_CENTER_REIT_INFRASTRUCTURE", "EQIX_MY", "Equinix Malaysia AI liquid cooling", "US", "success_candidate", ("ai_datacenter_demand", "liquid_cooling_facility"), ("funding_cost", "power_water_constraint"), "AI data-center expansion needs occupancy, funding, and AFFO checks."),
    Round28CaseCandidate("data_center_reit_capex_burden_4c", "DATA_CENTER_REIT_INFRASTRUCTURE", "REIT_CAPEX_4C", "데이터센터REIT_CAPEX부담", "US", "4c_thesis_break", ("ai_datacenter_demand",), ("capex_burden", "affo_dilution"), "Strong demand can still break if CAPEX dilutes AFFO."),
    Round28CaseCandidate("hyperscale_tenant_concentration_counterexample", "DATA_CENTER_REIT_INFRASTRUCTURE", "TENANT_CONC", "Hyperscale tenant concentration", "US", "failed_rerating", ("hyperscale_tenant",), ("tenant_concentration", "tenant_loss"), "Hyperscale tenant quality helps, but concentration risk caps confidence."),
    Round28CaseCandidate("meta_constellation_power_ppa_candidate", "UTILITIES_AI_POWER_PPA", "CEG_PPA", "Meta-Constellation power PPA", "US", "success_candidate", ("long_term_ppa", "power_sale_price_visible"), ("regulatory_risk", "grid_connection"), "Long-term PPA can support utility visibility if economics are clear."),
    Round28CaseCandidate("nuclear_no_ppa_utility_theme_counterexample", "UTILITIES_AI_POWER_PPA", "UTILITY_THEME", "원전전력수요테마_무PPA", "KR", "failed_rerating", ("ai_power_demand",), ("power_demand_theme_only", "ppa_missing"), "Power demand theme without PPA is Stage 1 only."),
    Round28CaseCandidate("tariff_no_pass_through_4c", "UTILITIES_AI_POWER_PPA", "TARIFF_4C", "요금전가부재4C", "KR", "4c_thesis_break", ("utility_power_supply",), ("tariff_no_pass_through", "fcf_deterioration"), "No tariff pass-through can break utility EPS/FCF."),
    Round28CaseCandidate("utility_debt_capex_burden_counterexample", "UTILITIES_AI_POWER_PPA", "UTILITY_DEBT", "유틸리티부채CAPEX부담", "KR", "failed_rerating", ("capacity_expansion",), ("debt_capex_burden", "dividend_risk"), "Debt/CAPEX burden can offset power demand."),
    Round28CaseCandidate("ai_datacenter_grid_interactive_demo_candidate", "SMART_GRID_FLEXIBLE_DATACENTER", "GRID_DEMO", "AI data-center grid interactive demo", "US", "success_candidate", ("grid_interactive_datacenter", "verified_peak_reduction"), ("poc_only", "commercialization"), "Demo is useful Stage 1/2 evidence but needs paying customers."),
    Round28CaseCandidate("smart_grid_policy_no_revenue_counterexample", "SMART_GRID_FLEXIBLE_DATACENTER", "GRID_POLICY", "스마트그리드정책_무매출", "KR", "failed_rerating", ("smart_grid",), ("poc_only", "no_revenue_model"), "Smart-grid policy alone is not score evidence."),
    Round28CaseCandidate("ess_no_revenue_model_counterexample", "SMART_GRID_FLEXIBLE_DATACENTER", "ESS_NOREV", "ESS_수익모델부재", "KR", "failed_rerating", ("ess",), ("no_revenue_model", "regulatory_incentive_failure"), "ESS installation without revenue model remains Watch."),
    Round28CaseCandidate("utility_adoption_delay_4c", "SMART_GRID_FLEXIBLE_DATACENTER", "GRID_ADOPT_4C", "유틸리티채택지연4C", "US", "4c_thesis_break", ("grid_flexibility_service",), ("utility_adoption_delay", "project_delay"), "Utility adoption delay can break grid software thesis."),
    Round28CaseCandidate("north_korea_policy_rally_event_only", "NORTH_KOREA_POLICY_EVENT", "NK_RALLY", "남북정책랠리", "KR", "event_premium", ("inter_korea_policy",), ("event_only", "no_cash_flow"), "Policy rally is event premium unless contracts and cash flow exist."),
    Round28CaseCandidate("kaesong_reopen_expectation_counterexample", "NORTH_KOREA_POLICY_EVENT", "KAESONG_EXP", "개성공단재개기대", "KR", "failed_rerating", ("kaesong_reopen_expectation",), ("sanction", "no_cash_flow"), "Reopen expectation is not E2R evidence."),
    Round28CaseCandidate("kumgang_tourism_policy_event_only", "NORTH_KOREA_POLICY_EVENT", "KUMGANG_EVENT", "금강산관광정책이벤트", "KR", "event_premium", ("kumgang_tourism_expectation",), ("event_only", "sanction"), "Tourism policy expectation is event premium without contracts."),
    Round28CaseCandidate("military_security_risk_4c", "NORTH_KOREA_POLICY_EVENT", "NK_SECURITY_4C", "군사안보리스크4C", "KR", "4c_thesis_break", ("inter_korea_policy",), ("military_security_risk", "sanction_tightening"), "Military/security risk is hard RedTeam evidence."),
    Round28CaseCandidate("nft_price_rally_no_revenue_counterexample", "METAVERSE_NFT_THEME", "NFT_PRICE", "NFT가격랠리_무매출", "KR", "overheat", ("token_volume_spike",), ("price_only_rally", "no_revenue"), "NFT price rally without revenue is overheat evidence."),
    Round28CaseCandidate("metaverse_platform_no_fcf_counterexample", "METAVERSE_NFT_THEME", "META_NOFCF", "메타버스플랫폼_무FCF", "KR", "failed_rerating", ("metaverse_keyword",), ("no_revenue", "fcf_absence"), "Metaverse platform narrative needs FCF conversion."),
    Round28CaseCandidate("digital_asset_infra_vs_nft_split_case", "METAVERSE_NFT_THEME", "NFT_SPLIT", "디지털자산인프라_NFT분리", "KR", "event_premium", ("digital_asset_theme",), ("speculative_volume", "theme_blur"), "Stablecoin/payment infra must be separated from speculative NFT themes."),
    Round28CaseCandidate("nft_liquidity_collapse_4c", "METAVERSE_NFT_THEME", "NFT_LIQ_4C", "NFT유동성붕괴4C", "KR", "4c_thesis_break", ("nft_keyword",), ("liquidity_collapse", "user_activity_collapse"), "Liquidity collapse breaks NFT/metaverse thesis."),
    Round28CaseCandidate("superconductor_theme_counterexample", "ADVANCED_MATERIAL_SPECULATIVE_THEME", "SUPERCON_THEME", "초전도체테마", "KR", "overheat", ("superconductor_keyword",), ("paper_only", "no_commercialization"), "Superconductor theme is not evidence without commercialization."),
    Round28CaseCandidate("graphene_mxene_no_commercialization_counterexample", "ADVANCED_MATERIAL_SPECULATIVE_THEME", "GRAPHENE_MXENE", "그래핀맥신_상용화부재", "KR", "failed_rerating", ("mxene_keyword", "graphene_keyword"), ("no_commercialization", "sample_only"), "Graphene/MXene keyword needs product and customer evidence."),
    Round28CaseCandidate("quantum_policy_no_revenue_watch", "ADVANCED_MATERIAL_SPECULATIVE_THEME", "QUANTUM_POLICY", "양자정책_무매출", "KR", "event_premium", ("quantum_policy",), ("policy_keyword_only", "no_revenue"), "Quantum policy is event/watch material until revenue exists."),
    Round28CaseCandidate("material_sample_no_contract_counterexample", "ADVANCED_MATERIAL_SPECULATIVE_THEME", "MATERIAL_SAMPLE", "소재샘플_무계약", "KR", "failed_rerating", ("sample_or_patent",), ("sample_only", "no_contract"), "Sample or patent without contract is not Stage 3 evidence."),
    Round28CaseCandidate("financial_valueup_roe_pbr_success_candidate", "VALUE_UP_SHAREHOLDER_RETURN", "VALUE_ROE", "금융밸류업ROE_PBR", "KR", "success_candidate", ("roe_improvement", "low_pbr", "shareholder_return"), ("execution", "credit_cost"), "Value-up candidate needs ROE and return execution."),
    Round28CaseCandidate("buyback_cancellation_success_candidate", "VALUE_UP_SHAREHOLDER_RETURN", "BUYBACK_CANCEL", "자사주소각성공", "KR", "success_candidate", ("actual_cancellation", "repeat_shareholder_return"), ("weak_fcf", "governance"), "Actual cancellation is stronger than buyback announcement."),
    Round28CaseCandidate("buyback_no_cancel_counterexample", "VALUE_UP_SHAREHOLDER_RETURN", "BUYBACK_NOCANCEL", "자사주미소각", "KR", "failed_rerating", ("buyback_or_dividend",), ("no_cancellation", "execution"), "Buyback without cancellation can be weak value-up evidence."),
    Round28CaseCandidate("low_roe_low_pbr_value_trap_counterexample", "VALUE_UP_SHAREHOLDER_RETURN", "LOWROE_TRAP", "저ROE저PBR가치함정", "KR", "failed_rerating", ("low_pbr",), ("low_roe", "weak_fcf"), "Low PBR without ROE/FCF can be value trap."),
    Round28CaseCandidate("ai_power_cooling_reit_integrated_success_candidate", "AI_DATA_CENTER_INFRASTRUCTURE", "AI_INFRA_INT", "AI전력냉각REIT통합", "US", "success_candidate", ("power_or_cooling_or_network_bottleneck", "orders_or_leases"), ("overbuild", "project_delay"), "Integrated AI infra candidate needs axis-specific evidence."),
    Round28CaseCandidate("ai_capex_overbuild_4c", "AI_DATA_CENTER_INFRASTRUCTURE", "AI_OVERBUILD_4C", "AI_CAPEX과잉4C", "US", "4c_thesis_break", ("ai_capex",), ("overbuild", "ai_capex_cut"), "Overbuild can break AI infrastructure thesis."),
    Round28CaseCandidate("grid_interconnection_delay_4c", "AI_DATA_CENTER_INFRASTRUCTURE", "GRID_DELAY_4C", "전력망접속지연4C", "US", "4c_thesis_break", ("datacenter_reit",), ("grid_interconnection_delay", "project_delay"), "Grid interconnection delay can break data-center infrastructure visibility."),
    Round28CaseCandidate("ai_theme_no_revenue_counterexample", "AI_DATA_CENTER_INFRASTRUCTURE", "AI_THEME_NOREV", "AI테마_무매출", "KR", "failed_rerating", ("ai_capex",), ("no_revenue_exposure", "theme_only"), "AI theme grouping without revenue exposure is not score evidence."),
)


def target_for(target_id: str) -> Round28ScoreTarget | None:
    for target in ROUND28_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round28_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND28_CASE_CANDIDATES:
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
                f"Round28 v1.3 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
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


def round28_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND28_SCORE_TARGETS:
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
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round28_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND28_CASE_CANDIDATES:
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


def round28_summary() -> dict[str, int | bool]:
    records = round28_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND28_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND28_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND28_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND28_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round28_score_weight_reports(
    *,
    output_directory: str | Path = ROUND28_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND28_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND28_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round28_score_weight_v13_summary.md",
        "case_matrix": output / "round28_case_candidate_matrix.csv",
        "green_guardrails": output / "round28_green_guardrail_review.md",
        "event_theme_boundary": output / "round28_event_theme_boundary_review.md",
        "risk_boundary": output / "round28_risk_boundary_review.md",
        "price_validation_plan": output / "round28_price_validation_plan.md",
    }
    _write_case_jsonl(round28_case_records(), cases)
    _write_rows(round28_score_profile_rows(), score_profiles)
    _write_rows(round28_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round28_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round28_green_guardrail_markdown(), encoding="utf-8")
    paths["event_theme_boundary"].write_text(render_round28_event_theme_boundary_markdown(), encoding="utf-8")
    paths["risk_boundary"].write_text(render_round28_risk_boundary_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round28_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round28_summary_markdown() -> str:
    summary = round28_summary()
    lines = [
        "# Round-28 Score-Weight v1.3 Summary",
        "",
        f"- source_round: `{ROUND28_SOURCE_ROUND_PATH}`",
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
        "- Round 28 expands v1.3 calibration, not production scoring.",
        "- Example: nuclear/SMR needs PPA, licensing, financing, and revenue path; policy wording is not enough.",
        "- Example: data-center REITs need FFO/AFFO, occupancy, tenant quality, power/cooling/land, and funding-cost checks.",
        "- Example: North Korea policy, NFT/metaverse, and speculative advanced materials are RedTeam-first unless real contracts and cash flow exist.",
        "- Theme names, case IDs, policies, PoCs, and price rallies are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round28_green_guardrail_markdown() -> str:
    lines = [
        "# Round-28 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND28_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.3 weights to production scoring yet.",
            "- Do not score policy headlines, LOIs, PoCs, samples, patents, or price rallies without source-backed economics.",
            "- Do not invent stage dates, prices, PPA economics, FFO/AFFO, offtake terms, revenue, FCF, or cancellation status.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round28_event_theme_boundary_markdown() -> str:
    lines = [
        "# Round-28 Event / Theme Boundary Review",
        "",
        "Round 28 explicitly separates structural E2R from event premium and speculative theme rallies.",
        "",
        "## RedTeam-First Targets",
    ]
    for target in ROUND28_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.REDTEAM_FIRST:
            lines.append(f"- {target.target_id}: {target.normalization_point}")
    lines.extend(
        [
            "",
            "## Examples",
            "- NORTH_KOREA_POLICY_EVENT: policy rally can be event premium without contracts and cash flow.",
            "- METAVERSE_NFT_THEME: NFT price/volume rally is not E2R without stable fee revenue and EPS/FCF conversion.",
            "- ADVANCED_MATERIAL_SPECULATIVE_THEME: paper, sample, patent, or quantum/superconductor keyword is not Green evidence.",
            "- VALUE_UP_SHAREHOLDER_RETURN: index inclusion is not enough; actual cancellation, ROE, return execution, and FCF matter.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round28_risk_boundary_markdown() -> str:
    lines = [
        "# Round-28 Risk Boundary Review",
        "",
        "Round 28 separates Green-possible structures, Watch-to-Green structures, and RedTeam-first themes.",
        "",
        "## Green-Possible With Strict Gates",
    ]
    for target in ROUND28_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.GREEN_POSSIBLE:
            lines.append(f"- {target.target_id}: {target.normalization_point}")
    lines.extend(["", "## Watch-First / 4C-Sensitive"])
    for target in ROUND28_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST:
            lines.append(f"- {target.target_id}: {', '.join(target.stage4c_conditions)}")
    lines.extend(["", "## RedTeam-First"])
    for target in ROUND28_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.REDTEAM_FIRST:
            lines.append(f"- {target.target_id}: {', '.join(target.stage4c_conditions)}")
    lines.extend(
        [
            "",
            "## Rule",
            "- Stage 3-Green still requires cross-evidence and price-path validation.",
            "- SMR cancellation, data-center REIT AFFO dilution, tariff non-pass-through, utility adoption delay, sanction risk, NFT liquidity collapse, and AI CAPEX overbuild are 4C-style examples.",
            "- Case records are calibration examples, not production labels.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round28_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-28 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep synthetic, policy, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before production scoring changes.",
            "",
            "## Priority Validation",
            "- Nuclear/SMR: PPA and restart economics versus cost, licensing, and financing failure.",
            "- Strategic metals: government support/offtake/price floor versus commodity price and governance events.",
            "- Data-center REIT and utilities: FFO/AFFO, PPA, tariff, funding cost, debt, and CAPEX risk.",
            "- RedTeam-first themes: North Korea, NFT/metaverse, advanced materials, and price-only rallies.",
            "- AI infrastructure: integrated power/cooling/REIT/PPA evidence versus overbuild and grid-delay 4C cases.",
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
    "ROUND28_CASE_CANDIDATES",
    "ROUND28_DEFAULT_CASES_PATH",
    "ROUND28_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND28_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND28_SCORE_TARGETS",
    "ROUND28_SOURCE_ROUND_PATH",
    "Round28CaseCandidate",
    "Round28ScoreTarget",
    "Round28ScoreWeightDraft",
    "render_round28_event_theme_boundary_markdown",
    "render_round28_green_guardrail_markdown",
    "render_round28_price_validation_plan_markdown",
    "render_round28_risk_boundary_markdown",
    "render_round28_summary_markdown",
    "round28_case_candidate_rows",
    "round28_case_records",
    "round28_score_profile_rows",
    "round28_summary",
    "target_for",
    "write_round28_score_weight_reports",
]
