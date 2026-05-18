"""Round-184 R13 Loop-11 cross-archetype RedTeam / 4B / price validation.

Round 184 is the Korea-focused common checkpoint over R1-R12 candidates. It
classifies strong structures, Stage 2-but-not-Green candidates, event rallies,
4B crowded winners, hard 4C breaks, disclosure-confidence caps, and private or
holdco link caps.

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
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture


ROUND184_SOURCE_ROUND_PATH = "docs/round/round_184.md"
ROUND184_LARGE_SECTOR = "CROSS_ARCHETYPE_REDTEAM_4B_PRICE_VALIDATION"
ROUND184_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round184_r13_loop11_cross_archetype_redteam"
ROUND184_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r13_loop11_round184.jsonl"
ROUND184_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round184_r13_loop11_v11.csv"
ROUND184_SOURCE_CANONICAL_TARGET_IDS: tuple[str, ...] = (
    "STRUCTURAL_STAGE3_EARLY_CAPTURE",
    "STAGE2_STRONG_NOT_GREEN",
    "EVENT_PRICE_RALLY_NOT_STAGE3",
    "STRUCTURAL_SUCCESS_BUT_4B_WATCH",
    "CYCLE_SUCCESS_NOT_STRUCTURAL",
    "DISCLOSURE_CONFIDENCE_CAP",
    "PRIVATE_OR_HOLDCO_LINK_CAP",
    "OPERATIONAL_TRUST_HARD_4C",
    "LEGAL_GOVERNANCE_4C_WATCH",
    "POLICY_MARKET_SHOCK_OVERLAY",
)
ROUND184_SOURCE_CANONICAL_TARGET_COUNT = len(ROUND184_SOURCE_CANONICAL_TARGET_IDS)


@dataclass(frozen=True)
class Round184OverlayWeightDraft:
    eps_fcf_roe_affo_opm_bodyweight: int | str
    cross_evidence_visibility: int | str
    price_path_early_validation: int | str
    repeatability_durability: int | str
    redteam_hard_4c_risk: int | str
    disclosure_confidence: int | str
    valuation_room_4b_margin: int | str

    def as_dict(self) -> dict[str, int | str]:
        return {
            "eps_fcf_roe_affo_opm_bodyweight": self.eps_fcf_roe_affo_opm_bodyweight,
            "cross_evidence_visibility": self.cross_evidence_visibility,
            "price_path_early_validation": self.price_path_early_validation,
            "repeatability_durability": self.repeatability_durability,
            "redteam_hard_4c_risk": self.redteam_hard_4c_risk,
            "disclosure_confidence": self.disclosure_confidence,
            "valuation_room_4b_margin": self.valuation_room_4b_margin,
        }


@dataclass(frozen=True)
class Round184OverlayAxis:
    axis_id: str
    points: int
    loop11_direction: str
    reason: str


@dataclass(frozen=True)
class Round184StageCap:
    stage_band: str
    max_score: str
    required_evidence: tuple[str, ...]
    example_cases: tuple[str, ...]
    green_policy: str


@dataclass(frozen=True)
class Round184OverlayTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round184OverlayWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    validation_role: str
    normalization_point: str
    hard_gate: bool = False
    stage3_green_allowed: bool = False

    @property
    def large_sector(self) -> str:
        return ROUND184_LARGE_SECTOR

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round184CaseCandidate:
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
class Round184ScoreStagePriceAlignment:
    case_id: str
    detected_stage: str
    price_path_status: str
    verdict: str
    normalization_adjustment: str


def _weights(
    eps: int | str,
    visibility: int | str,
    price: int | str,
    repeatability: int | str,
    redteam: int | str,
    disclosure: int | str,
    valuation: int | str,
) -> Round184OverlayWeightDraft:
    return Round184OverlayWeightDraft(eps, visibility, price, repeatability, redteam, disclosure, valuation)


def _target(
    target_id: str,
    archetype: E2RArchetype,
    posture: Round10ThemePosture,
    weight: Round184OverlayWeightDraft,
    *,
    stage1: tuple[str, ...],
    stage2: tuple[str, ...],
    stage3: tuple[str, ...],
    stage4b: tuple[str, ...],
    stage4c: tuple[str, ...],
    green: tuple[str, ...],
    red: tuple[str, ...],
    role: str,
    note: str,
    hard_gate: bool = False,
    green_allowed: bool = False,
) -> Round184OverlayTarget:
    return Round184OverlayTarget(target_id, archetype, posture, weight, stage1, stage2, stage3, stage4b, stage4c, green, red, role, note, hard_gate, green_allowed)


def _d(value: str) -> date:
    return date.fromisoformat(value)


GATE_WEIGHT = _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate")
CAP_WEIGHT = _weights("cap", "cap", "cap", "cap", "+", "+", "cap")

ROUND184_OVERLAY_AXES: tuple[Round184OverlayAxis, ...] = (
    Round184OverlayAxis("eps_fcf_roe_affo_opm_bodyweight_change", 24, "raise_actual_bodyweight", "Stage 3 early capture starts with OP/EPS/FCF, ROE, AFFO, or OPM bodyweight change."),
    Round184OverlayAxis("cross_evidence_visibility", 20, "raise_detail_visibility", "Contracts, customers, amount, duration, backlog, royalty, ARR/bookings, NOI/AFFO, prescriptions, repeat revenue, and equity-method income must be visible."),
    Round184OverlayAxis("price_path_early_validation", 14, "raise_price_validation", "Stage 2/3 must be checked against event returns, MFE/MAE, relative strength, and volume spike."),
    Round184OverlayAxis("repeatability_durability", 14, "raise_durability", "Long-term contracts, recurring software, repeat procedures, shareholder returns, occupancy, renewal, and repeat consumption separate structure from event."),
    Round184OverlayAxis("redteam_hard_4c_risk", 14, "hard_redteam_gate", "PF, safety, legal, cyber, policy reversal, contract cancellation, CRL/patent/CMC, accounting, and audit issues block unsafe Green."),
    Round184OverlayAxis("disclosure_confidence", 8, "cap_list_only_or_media_only", "OpenDART detail, contract details, customer, amount, duration, and routine disclosure filtering set confidence."),
    Round184OverlayAxis("valuation_room_4b_margin", 6, "cool_crowded_winners", "Good structures with crowded price paths need 4B monitoring rather than fresh Green promotion."),
)

ROUND184_STAGE_CAPS: tuple[Round184StageCap, ...] = (
    Round184StageCap(
        "Stage 3",
        "requires_6_of_9",
        ("op_eps_fcf_or_roe_affo_opm_improvement", "two_or_more_contract_customer_amount_duration_repeat_revenue", "stage2_60d_mfe_20pct", "relative_strength_vs_market_or_sector", "detail_based_disclosure_confidence", "repeatability_durability", "no_hard_4c_flag", "valuation_not_overheated", "op_eps_revision_keeps_up_with_price"),
        ("hanmi_hbm_equipment_stage3_early_capture_case", "alteogen_keytruda_sc_royalty_stage3_candidate_case"),
        "Stage 3 is an all-around validation outcome, not a sector label or price-only outcome.",
    ),
    Round184StageCap(
        "Stage 2 strong",
        "70",
        ("large_contract", "strategic_investment", "approval_or_fda", "equity_transaction", "ipo", "policy_execution", "some_customer_visibility", "short_term_price_reaction"),
        ("samsung_sds_kkr_cb_stage2_not_green_case", "samsung_sdi_ess_contract_stage2_strong_case"),
        "Stage 2 strong stays below Green until EPS/FCF/OPM conversion is confirmed.",
    ),
    Round184StageCap(
        "Stage 4B",
        "requires_4_of_7",
        ("stage2_120d_mfe_80pct", "stage3_252d_mfe_150pct", "one_day_event_return_20pct_or_limit_up", "narrative_ahead_of_earnings", "report_news_community_crowding", "op_eps_revision_lags_price", "peer_top_quartile_valuation"),
        ("kogas_daesung_gas_event_4b_case", "pinkfong_ip_ipo_event_not_stage3_case"),
        "4B catches strong but crowded winners or event rallies before they are mislabeled as fresh Green.",
    ),
    Round184StageCap(
        "Stage 4C",
        "hard_gate",
        ("contract_cancellation_or_customer_strategy_retreat", "pf_workout_or_debt_rescheduling", "fatal_accident_or_safety_inspection", "cyber_incident_or_ransomware_or_privacy_leak", "founder_or_management_legal_risk", "fda_crl_cmc_or_patent_overhang", "ipo_valuation_cut_or_guidance_miss", "no_tenant_no_revenue_no_commerciality", "media_report_only_fails_to_convert", "policy_reversal_or_market_shock"),
        ("jeju_air_fatal_accident_hard_4c_case", "naver_line_data_leak_operational_trust_case"),
        "One hard trust, legal, policy, contract, safety, cyber, or no-revenue issue blocks Stage 3-Green.",
    ),
)

ROUND184_OVERLAY_TARGETS: tuple[Round184OverlayTarget, ...] = (
    _target("STRUCTURAL_STAGE3_EARLY_CAPTURE", E2RArchetype.STRUCTURAL_STAGE3_EARLY_CAPTURE, Round10ThemePosture.GREEN_POSSIBLE, _weights("+", "+", "+", "+", "pass", "+", "check"), stage1=("structure_change", "price_attention", "sector_old_frame"), stage2=("contract_or_customer", "revision_or_profit", "cross_evidence"), stage3=("eps_fcf_bodyweight_change", "price_path_aligned", "detail_confidence", "no_hard_redteam"), stage4b=("crowding", "revision_lags_price"), stage4c=("hard_redteam", "revision_down", "thesis_break"), green=("eps_fcf_bodyweight_change", "cross_evidence", "price_path_aligned", "no_hard_redteam"), red=("hard_redteam", "crowded_4b", "revision_down"), role="positive_validation", note="Early Stage 3 capture requires evidence, price path, and RedTeam alignment.", green_allowed=True),
    _target("STAGE2_STRONG_NOT_GREEN", E2RArchetype.STAGE2_STRONG_NOT_GREEN, Round10ThemePosture.WATCH_YELLOW_FIRST, _weights("+", "+", "+", "partial", "check", "+", "check"), stage1=("large_event_or_contract", "strategic_investment", "approval_or_policy"), stage2=("large_contract", "strategic_investment", "approval", "equity_transaction", "price_response"), stage3=("eps_fcf_opm_conversion", "repeatability", "redteam_clean"), stage4b=("stage2_story_crowded_before_earnings",), stage4c=("conversion_missing", "detail_missing", "hard_redteam"), green=("eps_fcf_opm_conversion", "repeatability", "redteam_clean"), red=("stage3_evidence_missing", "conversion_missing", "detail_missing"), role="stage2_cap", note="Strong Stage 2 evidence is not Green until cash-flow conversion appears."),
    _target("EVENT_PRICE_RALLY_NOT_STAGE3", E2RArchetype.EVENT_PRICE_RALLY_NOT_STAGE3, Round10ThemePosture.REDTEAM_FIRST, _weights("0", "0", "+", "0", "+", "cap", "-"), stage1=("one_day_20pct", "limit_up", "policy_ipo_media_resource_event"), stage2=("verified_event_path", "some_visibility"), stage3=("blocked_without_eps_fcf_contract_repeat_revenue",), stage4b=("event_rally_4b_watch", "basket_rally"), stage4c=("event_fade", "no_commerciality", "no_revenue_conversion"), green=(), red=("price_only", "no_eps_fcf", "no_contract", "event_only"), role="green_block", note="Real price rally can be evidence of attention, not Stage 3 proof.", hard_gate=True),
    _target("STRUCTURAL_SUCCESS_BUT_4B_WATCH", E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH, Round10ThemePosture.WATCH_YELLOW_FIRST, _weights("maintain", "maintain", "high", "maintain", "+", "+", "deduct"), stage1=("strong_structure", "large_runup"), stage2=("stage2_120d_mfe_80pct", "stage3_252d_mfe_150pct", "new_frame_accepted"), stage3=("fundamentals_intact_but_mispricing_reduced",), stage4b=("4b_watch", "crowded_new_frame", "valuation_saturation"), stage4c=("revision_down", "demand_slowdown", "margin_peak"), green=("evidence_intact", "valuation_room_remaining"), red=("crowding", "valuation_saturation", "revision_slowdown"), role="graduation_monitoring", note="Good structure can become 4B when price and narrative run ahead."),
    _target("CYCLE_SUCCESS_NOT_STRUCTURAL", E2RArchetype.CYCLE_SUCCESS_NOT_STRUCTURAL, Round10ThemePosture.WATCH_YELLOW_FIRST, _weights("+", "low", "+", "low", "+", "medium", "low"), stage1=("freight_rate", "commodity_spread", "disease_price", "lithium_or_rare_earth_event"), stage2=("op_eps_spike", "cycle_cash_generation"), stage3=("durable_supply_discipline_required",), stage4b=("cycle_peak_crowded", "spot_price_peak"), stage4c=("spread_reversal", "freight_rate_crash", "new_supply", "price_normalization"), green=("multi_period_margin_stability", "supply_discipline"), red=("cycle_normalization", "new_supply", "spot_reversal"), role="cycle_cap", note="Cycle wins can be real but are not automatically structural rerating."),
    _target("DISCLOSURE_CONFIDENCE_CAP", E2RArchetype.DISCLOSURE_CONFIDENCE_CAP, Round10ThemePosture.REDTEAM_FIRST, CAP_WEIGHT, stage1=("media_report", "mou", "loi", "non_binding", "list_only_disclosure"), stage2=("detail_fetch_required", "customer_amount_duration_margin_required"), stage3=("binding_contract", "detail_verified", "eps_fcf_path"), stage4b=("headline_priced_before_detail",), stage4c=("report_denied", "fails_to_convert", "detail_missing"), green=("binding_contract", "customer_amount_duration_margin", "eps_fcf_path"), red=("media_only", "mou_loi", "non_binding", "detail_missing"), role="confidence_cap", note="Media report, MOU, LOI, or non-binding evidence cannot create Stage 3."),
    _target("PRIVATE_OR_HOLDCO_LINK_CAP", E2RArchetype.PRIVATE_OR_HOLDCO_LINK_CAP, Round10ThemePosture.WATCH_YELLOW_FIRST, _weights("0~+", "+", "+", "partial", "+", "+", "check"), stage1=("private_asset_value", "equity_stake", "holdco_discount"), stage2=("equity_transaction", "valuation_marker", "market_share_visible"), stage3=("equity_method_income", "dividend_or_cash_upstream", "listed_company_eps_fcf_link"), stage4b=("private_asset_premium_crowded",), stage4c=("security_incident", "regulatory_failure", "valuation_link_break"), green=("listed_company_eps_fcf_link", "cash_upstream", "regulatory_security_clean"), red=("holdco_link_missing", "security_risk", "regulatory_risk"), role="private_asset_cap", note="Private assets and holdco value are Stage 2 until listed EPS/FCF linkage is visible."),
    _target("OPERATIONAL_TRUST_HARD_4C", E2RArchetype.OPERATIONAL_TRUST_HARD_4C, Round10ThemePosture.REDTEAM_FIRST, GATE_WEIGHT, stage1=("safety_accident", "cyber_incident", "quality_failure", "ransomware"), stage2=("trust_repair_plan", "inspection_or_remediation"), stage3=("blocked_until_trust_restored",), stage4b=("trust_break_ignored_by_recovery_story",), stage4c=("fatal_accident", "safety_inspection", "data_leak", "ransomware", "quality_collapse"), green=(), red=("fatal_accident", "cyber_incident", "safety", "quality", "ransomware"), role="hard_4c", note="Operational trust breaks outrank demand recovery or sector score.", hard_gate=True),
    _target("LEGAL_GOVERNANCE_4C_WATCH", E2RArchetype.LEGAL_GOVERNANCE_4C_WATCH, Round10ThemePosture.REDTEAM_FIRST, GATE_WEIGHT, stage1=("founder_legal_risk", "management_lawsuit", "governance_conflict"), stage2=("legal_scope_known", "settlement_or_resolution_path"), stage3=("blocked_until_legal_scope_resolved",), stage4b=("legal_risk_ignored_by_rally",), stage4c=("injunction", "lawsuit_damage", "governance_break", "settlement_cost"), green=(), red=("founder_legal", "management_legal", "lawsuit", "governance"), role="legal_governance_gate", note="Legal and governance overhangs cap Green even in strong sectors.", hard_gate=True),
    _target("POLICY_MARKET_SHOCK_OVERLAY", E2RArchetype.POLICY_MARKET_SHOCK_OVERLAY, Round10ThemePosture.REDTEAM_FIRST, GATE_WEIGHT, stage1=("political_shock", "geopolitical_energy_shock", "short_selling_resumption"), stage2=("policy_resolution_or_market_stabilization",), stage3=("not_company_green_evidence",), stage4b=("crowded_trade_unwind", "risk_premium_spike"), stage4c=("market_wide_riskoff", "policy_reversal", "valuation_compression"), green=(), red=("policy_market_shock", "risk_premium", "valuation_compression"), role="market_overlay", note="Policy and market shocks adjust valuation room across candidates; they are not company evidence.", hard_gate=True),
)

ROUND184_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round184ScoreStagePriceAlignment, ...] = (
    Round184ScoreStagePriceAlignment("hanmi_hbm_equipment_stage3_early_capture_case", "Stage 2.5/3 candidate plus cap", "HBM equipment contract and customer diversification reports caused large price reaction", "structural_candidate_with_disclosure_cap", "credit confirmed SK Hynix contracts; cap unconfirmed Micron report until binding contract"),
    Round184ScoreStagePriceAlignment("samsung_sds_kkr_cb_stage2_not_green_case", "Stage 2 strong plus 4B-watch", "KKR CB and AI cloud narrative drove +20.8% intraday move", "strategic_validation_not_green", "treat CB as strategic validation and dilution watch; require ARR/OPM/FCF"),
    Round184ScoreStagePriceAlignment("kogas_daesung_gas_event_4b_case", "Stage 1 event plus 4B-watch", "KOGAS and Daesung Energy rallied +30% before drill-bit commerciality", "event_price_rally_not_stage3", "capture price-path but block Stage 3 before commerciality and earnings"),
    Round184ScoreStagePriceAlignment("jeju_air_fatal_accident_hard_4c_case", "hard 4C", "Fatal accident and safety inspection override travel recovery", "operational_trust_hard_4c", "safety and trust break outrank demand recovery"),
    Round184ScoreStagePriceAlignment("naver_dunamu_holdco_link_stage2_case", "Stage 2 not Green", "Dunamu stake transaction validates asset value but listed EPS/FCF linkage is not enough", "private_holdco_link_cap", "require equity-method income, dividend/cash upstream, security, and regulation stability"),
)

ROUND184_CASE_CANDIDATES: tuple[Round184CaseCandidate, ...] = (
    Round184CaseCandidate("hanmi_hbm_equipment_stage3_early_capture_case", "STRUCTURAL_STAGE3_EARLY_CAPTURE", "042700", "Hanmi Semiconductor HBM equipment early-capture case", "KR", "success_candidate", None, None, None, None, None, ("sk_hynix_contract", "hbm_equipment_bottleneck", "micron_supply_report", "recent_contracts_200bn_krw", "intraday_plus_22pct"), ("unconfirmed_customer_report", "valuation_crowding", "stage4b_watch"), "stage3_candidate_with_disclosure_cap", "needs_contract_customer_op_revision_price_backfill", ("round_184.md WSJ Hanmi Semiconductor Micron report",), "Hanmi is a structural early-capture candidate, but unconfirmed customer reports are capped until binding contracts appear.", (E2RArchetype.DISCLOSURE_CONFIDENCE_CAP, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH)),
    Round184CaseCandidate("samsung_ea_fadhili_epc_stage2_strong_case", "STAGE2_STRONG_NOT_GREEN", "028050", "Samsung E&A Fadhili EPC Stage 2 strong case", "KR", "success_candidate", None, None, None, None, None, ("saudi_aramco_customer", "fadhili_gas_plant_contract", "contract_value_6bn_usd", "intraday_plus_8_5pct"), ("epc_margin_unconfirmed", "cash_conversion_unconfirmed", "project_delay_or_low_margin_risk"), "large_epc_contract_stage2_until_margin_cash_conversion", "needs_margin_cash_conversion_op_revision_price_backfill", ("round_184.md WSJ Samsung E&A Saudi contract",), "Samsung E&A has contract amount and customer evidence, but EPC margin and cash conversion decide Stage 3."),
    Round184CaseCandidate("samsung_sds_kkr_cb_stage2_not_green_case", "STAGE2_STRONG_NOT_GREEN", "018260", "Samsung SDS KKR CB AI cloud Stage 2 not Green", "KR", "4b_watch", _d("2026-04-15"), _d("2026-04-15"), None, _d("2026-04-15"), None, ("kkr_820m_usd_convertible_bond", "ai_offering_advisory", "mna_capital_allocation", "intraday_plus_20_8pct"), ("cb_dilution", "ai_revenue_arr_missing", "opm_fcf_missing"), "strategic_validation_plus_dilution_watch", "needs_arr_ai_revenue_cb_dilution_price_backfill", ("round_184.md Reuters Samsung SDS KKR CB",), "Samsung SDS gets Stage 2 strategic validation, but CB dilution and missing AI ARR/FCF block Green.", (E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,)),
    Round184CaseCandidate("alteogen_keytruda_sc_royalty_stage3_candidate_case", "STRUCTURAL_STAGE3_EARLY_CAPTURE", "196170", "Alteogen Keytruda SC royalty platform candidate", "KR", "success_candidate", _d("2024-11-19"), None, None, None, None, ("merck_partner", "keytruda_sc_formulation", "injection_time_reduced", "enzyme_supply_royalty_option"), ("royalty_revenue_missing", "adoption_backfill_required", "stage4b_watch_if_priced_ahead"), "platform_royalty_candidate_requires_backfill", "needs_royalty_adoption_milestone_op_revision_price_backfill", ("round_184.md Reuters Keytruda SC trial",), "Alteogen can be Stage 2/3 candidate after royalty/adoption backfill; expectation-only periods need 4B monitoring.", (E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,)),
    Round184CaseCandidate("pinkfong_ip_ipo_event_not_stage3_case", "EVENT_PRICE_RALLY_NOT_STAGE3", "PINKFONG", "Pinkfong IP IPO price-path not Stage 3", "KR", "4b_watch", None, None, None, None, None, ("ipo_max_plus_62pct", "ipo_close_plus_9pct", "ipo_raise_76bn_krw", "revenue_97_4bn_krw", "operating_profit_18_8bn_krw"), ("baby_shark_one_hit_risk", "ipo_premium", "multi_ip_revenue_unconfirmed"), "stage2_strong_price_path_not_green", "needs_listing_date_multi_ip_opm_fcf_price_backfill", ("round_184.md FT Pinkfong IPO",), "Pinkfong has strong Stage 2 IP price-path, but IPO pop and one-hit risk block Stage 3 until multi-IP OPM/FCF are proven.", (E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,)),
    Round184CaseCandidate("samsung_sdi_ess_contract_stage2_strong_case", "STAGE2_STRONG_NOT_GREEN", "006400", "Samsung SDI ESS LFP contract Stage 2 strong", "KR", "success_candidate", _d("2025-12-09"), _d("2025-12-09"), None, None, None, ("ess_lfp_contract_over_2tn_krw", "three_year_supply", "delivery_from_2027", "line_conversion", "intraday_plus_6_1pct"), ("customer_name_undisclosed", "revenue_recognition_delayed", "ess_opm_unconfirmed", "utilization_unconfirmed"), "ess_contract_stage2_until_customer_opm_utilization", "needs_customer_utilization_opm_fcf_price_backfill", ("round_184.md Reuters Samsung SDI ESS contract",), "Samsung SDI ESS is Stage 2 strong, but customer, utilization, OPM, and FCF are needed before Green.", (E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,)),
    Round184CaseCandidate("kogas_daesung_gas_event_4b_case", "EVENT_PRICE_RALLY_NOT_STAGE3", "036460/117580/096770/018670", "KOGAS Daesung Energy East Sea gas event", "KR", "4b_watch", _d("2024-06-03"), None, None, _d("2024-06-03"), None, ("kogas_plus_30pct", "daesung_energy_plus_30pct", "sk_innovation_plus_6pct", "sk_gas_plus_7pct", "possible_14bn_barrels", "exploration_approval"), ("success_probability_20pct", "failure_probability_80pct", "commerciality_unconfirmed", "pre_drilling"), "event_price_success_not_stage3", "needs_drill_bit_commerciality_eps_price_backfill", ("round_184.md Reuters East Sea gas",), "The East Sea gas event is the canonical +30% price-path that remains Stage 1/4B-watch before commerciality.", (E2RArchetype.RESOURCE_EXPLORATION_DRILL_BIT_GATE,)),
    Round184CaseCandidate("kia_sdv_ev_target_cut_4c_watch_case", "STAGE2_STRONG_NOT_GREEN", "000270", "Kia hybrid localization with SDV delay EV target cut", "KR", "failed_rerating", _d("2026-04-09"), None, None, None, _d("2026-04-09"), ("hybrid_us_localization", "sdv_launch_delayed_to_2028", "ev_target_cut", "investment_plan_plus_30pct", "shares_minus_5_5pct"), ("sdv_delay", "ev_target_cut", "capex_increase_margin_pressure"), "stage2_with_product_roadmap_4c_watch", "needs_margin_capex_revision_price_backfill", ("round_184.md Reuters Kia SDV delay",), "Kia localization evidence is useful, but SDV delay, EV target cut, and capex pressure are 4C-watch fields."),
    Round184CaseCandidate("jeju_air_fatal_accident_hard_4c_case", "OPERATIONAL_TRUST_HARD_4C", "089590", "Jeju Air fatal accident hard 4C", "KR", "4c_thesis_break", _d("2024-12-30"), None, None, None, _d("2024-12-30"), ("fatal_accident", "intraday_minus_15_7pct", "record_low", "market_cap_loss_95_7bn_krw", "government_safety_inspection"), ("fatal_accident", "safety_inspection", "consumer_trust_damage", "travel_demand_impact"), "safety_hard_4c_overrides_reopening", "needs_accident_date_mae_safety_recovery_price_backfill", ("round_184.md Reuters Jeju Air crash",), "Jeju Air is a hard 4C example where safety and trust override travel recovery."),
    Round184CaseCandidate("naver_dunamu_holdco_link_stage2_case", "PRIVATE_OR_HOLDCO_LINK_CAP", "035420/DUNAMU_PRIVATE", "NAVER-Dunamu digital asset equity value cap", "KR", "success_candidate", _d("2026-05-14"), _d("2026-05-14"), None, None, None, ("hana_bank_dunamu_stake_6_55pct", "stake_value_1tn_krw", "naver_financial_dunamu_share_swap_option", "digital_asset_market_share"), ("listed_eps_fcf_link_missing", "security_regulatory_risk", "equity_method_income_unconfirmed"), "private_asset_stage2_until_listed_cashflow_link", "needs_equity_method_income_security_regulatory_price_backfill", ("round_184.md Reuters Hana Bank Dunamu stake",), "Dunamu stake value is Stage 2 validation, not listed-company Green until EPS/FCF linkage and security/regulation are clean."),
    Round184CaseCandidate("oci_spacex_mipo_loi_lgchem_nonbinding_cap_case", "DISCLOSURE_CONFIDENCE_CAP", "010060/010620/051910", "OCI SpaceX media report HD Hyundai Mipo LOI LG Chem non-binding cap", "KR", "failed_rerating", None, None, None, None, None, ("media_report_only", "mou_loi", "non_binding_agreement", "customer_or_amount_or_duration_missing"), ("contract_amount_missing", "customer_detail_missing", "binding_status_missing", "margin_missing"), "media_mou_loi_nonbinding_not_stage3", "needs_binding_contract_detail_price_backfill", ("round_184.md media report MOU LOI non-binding section",), "Media report, LOI, and non-binding evidence cannot become Stage 3 until binding contract details are parsed."),
    Round184CaseCandidate("cycle_success_not_structural_korea_basket_case", "CYCLE_SUCCESS_NOT_STRUCTURAL", "HMM/PAN_OCEAN/STEEL/LITHIUM/LIVESTOCK", "Korea freight commodity disease cycle basket", "KR", "cyclical_success", None, None, None, None, None, ("freight_rate_spike", "commodity_spread", "lithium_or_rare_earth_event", "livestock_disease_price_event", "op_eps_spike_possible"), ("spot_reversal", "new_supply", "price_normalization", "cycle_peak_crowding"), "cycle_win_not_structural_green", "needs_cycle_price_spread_mfe_mae_backfill", ("round_184.md cycle success not structural section",), "Cycle success can be real, but R13 caps it below structural Green until durability is proven."),
    Round184CaseCandidate("naver_line_data_leak_operational_trust_case", "OPERATIONAL_TRUST_HARD_4C", "035420/LINE", "NAVER-LY LINE data leak operational trust watch", "KR/JP", "4c_thesis_break", None, None, None, None, None, ("data_leak", "regulatory_pressure", "operational_trust_damage"), ("privacy_breach", "regulatory_pressure", "customer_trust_damage"), "platform_operational_trust_4c_watch", "needs_regulatory_scope_retention_price_backfill", ("round_184.md hard 4C common list",), "Data leak and regulatory pressure are operational trust hard-review fields for platform candidates."),
    Round184CaseCandidate("kakao_hybe_krafton_legal_governance_watch_case", "LEGAL_GOVERNANCE_4C_WATCH", "035720/352820/259960", "Kakao HYBE Krafton legal governance watch", "KR", "4c_thesis_break", None, None, None, None, None, ("founder_or_management_legal_overhang", "developer_lawsuit_or_release_delay", "governance_conflict"), ("legal_overhang", "release_delay", "injunction_or_lawsuit_damage", "governance_risk"), "legal_governance_4c_watch", "needs_legal_scope_release_schedule_price_backfill", ("round_184.md legal governance hard 4C list",), "Legal and governance overhang can block otherwise good platform/content candidates."),
    Round184CaseCandidate("policy_market_shock_overlay_korea_case", "POLICY_MARKET_SHOCK_OVERLAY", "KR_MARKET", "Korea policy market shock overlay", "KR", "4c_thesis_break", None, None, None, None, None, ("martial_law", "hormuz_energy_shock", "short_selling_resumption", "valuation_compression"), ("market_wide_riskoff", "policy_reversal", "risk_premium_spike", "valuation_room_cut"), "market_overlay_cuts_stage3_confidence", "needs_policy_shock_market_mae_backfill", ("round_184.md policy market shock overlay section",), "Policy, political, and geopolitical shocks are market overlays, not company Green evidence."),
)

ROUND184_PRICE_FIELDS: tuple[str, ...] = (
    "ticker", "company_name", "sector_round", "canonical_archetype", "case_type",
    "stage1_date", "stage2_date", "stage3_date", "stage4b_date", "stage4c_date",
    "stage1_trigger", "stage2_trigger", "stage3_trigger", "stage4b_trigger", "stage4c_trigger",
    "price_at_stage1", "price_at_stage2", "price_at_stage3", "price_at_stage4b", "price_at_stage4c",
    "return_1d_after_event", "return_5d_after_event", "return_20d_after_stage2", "return_60d_after_stage2", "return_120d_after_stage2", "return_252d_after_stage2",
    "mfe_20d_after_stage2", "mae_20d_after_stage2", "mfe_60d_after_stage2", "mae_60d_after_stage2", "mfe_120d_after_stage2", "mae_120d_after_stage2", "mfe_252d_after_stage2", "mae_252d_after_stage2",
    "relative_strength_vs_kospi", "relative_strength_vs_kosdaq", "relative_strength_vs_sector_basket",
    "op_revision_before_stage3", "op_revision_after_stage3", "eps_revision_before_stage3", "eps_revision_after_stage3", "fcf_signal", "roe_or_affo_signal", "opm_signal",
    "contract_amount", "contract_counterparty", "contract_period", "customer_name", "revenue_recognition_timing", "royalty_revenue", "arr_or_bookings", "noi_or_affo", "prescription_volume", "repeat_revenue_signal",
    "disclosure_source_type", "opendart_list_only_flag", "opendart_detail_flag", "media_report_only_flag", "mou_loi_flag", "non_binding_flag", "parser_confidence", "disclosure_confidence",
    "event_price_only_flag", "price_only_event_allowed", "stage3_green_allowed", "stage4b_watch_flag", "stage4c_hard_flag",
    "hard_4c_reason", "valuation_at_stage3", "valuation_at_stage4b",
)


def round184_target_for(target_id: str) -> Round184OverlayTarget | None:
    for target in ROUND184_OVERLAY_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round184_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND184_CASE_CANDIDATES:
        target = round184_target_for(candidate.target_id)
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
            large_sector=target.large_sector,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                f"Round184 R13 Loop-11 case for {candidate.target_id}; "
                "cross-archetype validation separates Stage 3 early capture from Stage 2 strong, event price-path, 4B, 4C, private/holdco caps, and disclosure caps."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions or field in target.green_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type != "structural_success" else None,
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint=_score_weight_hint(target),
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "stage3_green_requires_6_of_9_loop11_checks",
                "hard_4c_blocks_green",
                "event_price_path_is_not_stage3_evidence_alone",
                "do_not_invent_stage_prices_mfe_mae_or_contract_details",
                "opendart_list_only_cannot_create_stage3",
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


def round184_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND184_OVERLAY_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf_roe_affo_opm_bodyweight": str(weights["eps_fcf_roe_affo_opm_bodyweight"]),
                "cross_evidence_visibility": str(weights["cross_evidence_visibility"]),
                "price_path_early_validation": str(weights["price_path_early_validation"]),
                "repeatability_durability": str(weights["repeatability_durability"]),
                "redteam_hard_4c_risk": str(weights["redteam_hard_4c_risk"]),
                "disclosure_confidence": str(weights["disclosure_confidence"]),
                "valuation_room_4b_margin": str(weights["valuation_room_4b_margin"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "validation_role": target.validation_role,
                "hard_gate": str(target.hard_gate).lower(),
                "stage3_green_allowed": str(target.stage3_green_allowed).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round184_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND184_CASE_CANDIDATES:
        target = round184_target_for(candidate.target_id)
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


def round184_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "hard_gate": str(target.hard_gate).lower(),
            "stage3_green_allowed": str(target.stage3_green_allowed).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND184_OVERLAY_TARGETS
    )


def round184_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round184_backfill": "true"} for field in ROUND184_PRICE_FIELDS)


def round184_overlay_axis_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "axis_id": item.axis_id,
            "points": str(item.points),
            "loop11_direction": item.loop11_direction,
            "reason": item.reason,
            "production_scoring_changed": "false",
        }
        for item in ROUND184_OVERLAY_AXES
    )


def round184_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "stage_band": item.stage_band,
            "max_score": item.max_score,
            "required_evidence": "|".join(item.required_evidence),
            "example_cases": "|".join(item.example_cases),
            "green_policy": item.green_policy,
            "production_scoring_changed": "false",
        }
        for item in ROUND184_STAGE_CAPS
    )


def round184_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": item.case_id,
            "detected_stage": item.detected_stage,
            "price_path_status": item.price_path_status,
            "verdict": item.verdict,
            "normalization_adjustment": item.normalization_adjustment,
            "production_scoring_changed": "false",
        }
        for item in ROUND184_SCORE_STAGE_PRICE_ALIGNMENT
    )


def round184_summary() -> dict[str, int | bool]:
    records = round184_case_records()
    return {
        "target_count": len(ROUND184_OVERLAY_TARGETS),
        "source_canonical_target_count": ROUND184_SOURCE_CANONICAL_TARGET_COUNT,
        "case_candidate_count": len(records),
        "overlay_axis_count": len(ROUND184_OVERLAY_AXES),
        "stage_cap_count": len(ROUND184_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND184_SCORE_STAGE_PRICE_ALIGNMENT),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "hard_gate_target_count": sum(1 for target in ROUND184_OVERLAY_TARGETS if target.hard_gate),
        "stage3_green_allowed_target_count": sum(1 for target in ROUND184_OVERLAY_TARGETS if target.stage3_green_allowed),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round184_r13_loop11_reports(
    *,
    output_directory: str | Path = ROUND184_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND184_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND184_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round184_r13_loop11_cross_archetype_redteam_summary.md",
        "case_matrix": output / "round184_r13_loop11_case_matrix.csv",
        "stage_date_plan": output / "round184_r13_loop11_stage_date_plan.csv",
        "redteam_gate_plan": output / "round184_r13_loop11_redteam_gate_plan.md",
        "price_validation_plan": output / "round184_r13_loop11_price_validation_plan.md",
        "price_fields": output / "round184_r13_loop11_price_fields.csv",
        "overlay_axes": output / "round184_r13_loop11_overlay_axes.csv",
        "stage_caps": output / "round184_r13_loop11_stage_caps.csv",
        "score_stage_price_alignment": output / "round184_r13_loop11_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round184_r13_loop11_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round184_case_records(), cases)
    _write_rows(round184_score_profile_rows(), score_profiles)
    _write_rows(round184_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round184_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round184_price_field_rows(), paths["price_fields"])
    _write_rows(round184_overlay_axis_rows(), paths["overlay_axes"])
    _write_rows(round184_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round184_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round184_summary_markdown(), encoding="utf-8")
    paths["redteam_gate_plan"].write_text(render_round184_redteam_gate_plan_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round184_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(render_round184_score_stage_price_alignment_markdown(), encoding="utf-8")
    return paths


def render_round184_summary_markdown() -> str:
    summary = round184_summary()
    lines = [
        "# Round-184 R13 Loop-11 Cross-Archetype RedTeam / 4B / Price Validation Summary",
        "",
        f"- source_round: `{ROUND184_SOURCE_ROUND_PATH}`",
        f"- large_sector: `{ROUND184_LARGE_SECTOR}`",
        "- loop: `R13 Loop 11 / v11.0`",
        f"- target_count: {summary['target_count']}",
        f"- source_canonical_target_count: {summary['source_canonical_target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- overlay_axis_count: {summary['overlay_axis_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- hard_gate_target_count: {summary['hard_gate_target_count']}",
        f"- stage3_green_allowed_target_count: {summary['stage3_green_allowed_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R13 Loop 11 is a common validation overlay, not a new sector.",
        "- Example: Hanmi Semiconductor can be a structural early-capture candidate, but unconfirmed customer reports remain disclosure-capped.",
        "- Example: Samsung SDS and Samsung SDI are Stage 2 strong until AI ARR, ESS utilization, OPM, and FCF convert.",
        "- Example: Jeju Air fatal accident and NAVER/LINE data-leak style issues are hard 4C trust gates.",
    ]
    return "\n".join(lines) + "\n"


def render_round184_redteam_gate_plan_markdown() -> str:
    lines = [
        "# Round-184 R13 Loop-11 RedTeam Gate Plan",
        "",
        "| target | hard gate | stage3 allowed | red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND184_OVERLAY_TARGETS:
        lines.append(f"| `{target.target_id}` | {str(target.hard_gate).lower()} | {str(target.stage3_green_allowed).lower()} | {', '.join(target.red_flags)} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply Round184 overlay weights to production scoring yet.",
            "- Do not use case records as candidate-generation input.",
            "- Do not convert event rallies, private asset value, media reports, MOU, LOI, or non-binding terms into Stage 3 evidence.",
            "- Do not invent stage prices, MFE/MAE, customer names, contract amounts, durations, royalties, ARR, AFFO, prescription volume, or FCF signals.",
            "- Hard 4C gates such as PF workout, fatal accident, cyber incident, legal overhang, policy shock, and contract cancellation block Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round184_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-184 R13 Loop-11 Price Validation Plan",
        "",
        "R13 unifies price-path, disclosure-confidence, RedTeam, and cash-flow validation across R1-R12.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND184_PRICE_FIELDS)
    lines.extend(
        [
            "",
            "## Case Backfill Priorities",
            "",
            "- `hanmi_hbm_equipment_stage3_early_capture_case`: contract detail, confirmed customers, OP/EPS revision, MFE/MAE, and 4B crowding.",
            "- `samsung_sds_kkr_cb_stage2_not_green_case`: AI ARR/revenue, CB dilution, OPM/FCF, and one-day event return.",
            "- `kogas_daesung_gas_event_4b_case`: drill-bit result, commerciality, event returns, and price-only unwind risk.",
            "- `jeju_air_fatal_accident_hard_4c_case`: accident date MAE, safety inspections, trust recovery, and demand impact.",
            "- `naver_dunamu_holdco_link_stage2_case`: equity-method income, cash upstream, security incidents, regulation, and listed EPS/FCF linkage.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round184_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-184 R13 Loop-11 Score / Stage / Price Alignment",
        "",
        "| case | detected stage | price path status | verdict | adjustment |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in ROUND184_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(f"| `{row.case_id}` | {row.detected_stage} | {row.price_path_status} | {row.verdict} | {row.normalization_adjustment} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Hanmi shows structural early-capture plus disclosure confidence cap.",
            "- Samsung SDS shows Stage 2 strong with dilution and AI revenue checks.",
            "- KOGAS/Daesung Energy show price-path success without Stage 3 evidence.",
            "- Jeju Air shows hard 4C operational trust break.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_weight_hint(target: Round184OverlayTarget) -> Mapping[str, float]:
    values: dict[str, float] = {}
    for key, value in target.score_weight.as_dict().items():
        if isinstance(value, int):
            values[key] = float(value)
    return values


def _score_price_alignment(candidate: Round184CaseCandidate) -> str:
    if candidate.case_type in {"success_candidate", "structural_success"}:
        return "unknown"
    if candidate.case_type in {"event_premium", "4b_watch", "cyclical_success"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type == "failed_rerating":
        return "evidence_good_but_price_failed"
    return "unknown"


def _rerating_result(candidate: Round184CaseCandidate) -> str:
    if candidate.case_type in {"success_candidate", "structural_success"}:
        return "unknown"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown"


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> None:
    lines = []
    for record in records:
        record.validate()
        lines.append(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> None:
    rows = tuple(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


__all__ = [
    "ROUND184_CASE_CANDIDATES",
    "ROUND184_DEFAULT_CASES_PATH",
    "ROUND184_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND184_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND184_LARGE_SECTOR",
    "ROUND184_OVERLAY_AXES",
    "ROUND184_OVERLAY_TARGETS",
    "ROUND184_PRICE_FIELDS",
    "ROUND184_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND184_SOURCE_CANONICAL_TARGET_COUNT",
    "ROUND184_SOURCE_CANONICAL_TARGET_IDS",
    "ROUND184_STAGE_CAPS",
    "render_round184_price_validation_plan_markdown",
    "render_round184_redteam_gate_plan_markdown",
    "render_round184_score_stage_price_alignment_markdown",
    "render_round184_summary_markdown",
    "round184_case_candidate_rows",
    "round184_case_records",
    "round184_overlay_axis_rows",
    "round184_price_field_rows",
    "round184_score_profile_rows",
    "round184_score_stage_price_alignment_rows",
    "round184_stage_cap_rows",
    "round184_stage_date_rows",
    "round184_summary",
    "round184_target_for",
    "write_round184_r13_loop11_reports",
]
