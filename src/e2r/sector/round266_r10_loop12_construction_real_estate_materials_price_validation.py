"""Round-266 R10 Loop-12 construction/real-estate/materials validation pack.

This pack converts ``docs/round/round_266.md`` into calibration-only case
records, shadow weights, and guardrail reports. Production scoring is not
changed.

Easy example: Czech nuclear preferred-bidder news is strong Stage 2 evidence,
but it is not Stage 3-Green until final contract, legal clearance, project
scope, margin, working capital, and cash collection are visible.
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
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector


ROUND266_SOURCE_ROUND_PATH = "docs/round/round_266.md"
ROUND266_ANALYST_ROUND_ID = "round_194"
ROUND266_LARGE_SECTOR = Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value
ROUND266_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round266_r10_loop12_construction_real_estate_materials_price_validation"
ROUND266_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop12_round266.jsonl"
ROUND266_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round266_r10_loop12_construction_real_estate_materials_price_validation_audit.json"

ROUND266_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "NUCLEAR_EPC_EXPORT_STAGE2": E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2.value,
    "NUCLEAR_EXPORT_LEGAL_4C_WATCH": E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH.value,
    "CONSTRUCTION_SAFETY_HARD_REFERENCE": E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE.value,
    "RECURRING_FATAL_ACCIDENT_REGULATORY_4C": E2RArchetype.RECURRING_FATAL_ACCIDENT_REGULATORY_4C.value,
    "HOUSING_SUPPLY_POLICY_EVENT": E2RArchetype.HOUSING_SUPPLY_POLICY_EVENT.value,
    "PUBLIC_INFRASTRUCTURE_POLICY_EVENT": E2RArchetype.PUBLIC_INFRASTRUCTURE_POLICY_EVENT.value,
    "LNG_POWER_INFRA_CONSORTIUM_OPTION": E2RArchetype.LNG_POWER_INFRA_CONSORTIUM_OPTION.value,
    "BUILDING_MATERIALS_DEMAND_BREAK": E2RArchetype.BUILDING_MATERIALS_DEMAND_BREAK.value,
}

ROUND266_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Czech Dukovany nuclear preferred bidder / legal 4C-watch",
    "Bulgaria Kozloduy nuclear talks / Hyundai E&C pipeline",
    "Hyundai Engineering Anseong bridge collapse / sector safety hard reference",
    "POSCO E&C / DL Construction recurring fatal-accident regulation",
    "Seoul LTV tightening and state-owned land housing supply policy",
    "Sejong presidential office public infrastructure headline",
    "Daewoo E&C Vietnam Nghi Son LNG power consortium option",
    "Hyundai Steel rebar construction-demand break",
)

ROUND266_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "final_contract_signed",
    "scope_value_payment_schedule_confirmed",
    "progress_revenue_or_delivery_milestone_confirmed",
    "construction_margin_or_opm_confirmed",
    "working_capital_and_receivables_stable",
    "cash_collection_quality_confirmed",
    "legal_appeal_permit_license_risk_cleared",
    "safety_incident_absent_or_remediated",
    "presales_unsold_inventory_pf_stability_confirmed",
    "price_path_after_evidence",
)

ROUND266_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "preferred_bidder_only",
    "talks_or_parliament_nod_only",
    "candidate_consortium_only",
    "public_infra_headline_only",
    "housing_policy_only",
    "safety_incident_unresolved",
    "legal_appeal_pending",
    "building_material_demand_break",
)

ROUND266_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "nuclear_preferred_bidder_rally_before_final_contract",
    "housing_supply_policy_rally_before_presales",
    "public_infra_tender_notice_theme_rally",
    "lng_consortium_candidate_price_rally_before_award",
    "safety_relief_bounce_before_investigation_clears",
    "building_material_rebound_without_demand_recovery",
)

ROUND266_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_construction_collapse",
    "repeated_fatal_accidents",
    "license_revocation",
    "work_suspension",
    "major_defect_or_collapse_investigation",
    "legal_block_on_project_signing",
    "contract_cancellation",
    "pf_refinancing_failure",
    "unsold_inventory_spike",
    "construction_cost_overrun",
    "rebar_or_materials_demand_collapse",
)

ROUND266_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_1d",
    "event_mae_1d",
    "reported_3m_mfe",
    "project_value_or_capacity_anchor",
    "safety_or_regulatory_anchor",
    "policy_or_ltv_anchor",
    "materials_demand_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round266ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round266ShadowWeightRow:
    archetype: E2RArchetype
    final_contract_signed: int
    progress_revenue: int
    construction_margin: int
    working_capital: int
    cash_collection: int
    safety_execution: int
    legal_clearance: int
    presales_unsold_pf: int
    building_material_spread: int
    public_contract_quality: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "final_contract_signed": _signed(self.final_contract_signed),
            "progress_revenue": _signed(self.progress_revenue),
            "construction_margin": _signed(self.construction_margin),
            "working_capital": _signed(self.working_capital),
            "cash_collection": _signed(self.cash_collection),
            "safety_execution": _signed(self.safety_execution),
            "legal_clearance": _signed(self.legal_clearance),
            "presales_unsold_pf": _signed(self.presales_unsold_pf),
            "building_material_spread": _signed(self.building_material_spread),
            "public_contract_quality": _signed(self.public_contract_quality),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round266CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    stage3_decision: str
    stage4b_status: str
    hard_4c_confirmed: bool
    direct_listed_hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    mfe_1d: float | None
    mae_1d: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool | list[str] | None]
    round_score_price_alignment: str
    score_price_alignment: str
    round_rerating_result: str
    rerating_result: str
    round_stage_failure_type: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND266_SCORE_ADJUSTMENTS: tuple[Round266ScoreAdjustment, ...] = (
    Round266ScoreAdjustment("final_contract_signed", 5, "raise", "R10 원전/EPC는 preferred bidder가 아니라 final contract가 핵심이다."),
    Round266ScoreAdjustment("progress_revenue_visibility", 5, "raise", "공정률과 진행매출이 보여야 수주가 EPS/FCF로 닫힌다."),
    Round266ScoreAdjustment("construction_margin_visibility", 5, "raise", "건설은 계약금액보다 원가율과 OPM 확인이 중요하다."),
    Round266ScoreAdjustment("working_capital_control", 5, "raise", "미청구공사·매출채권이 흔들리면 수주가 현금으로 닫히지 않는다."),
    Round266ScoreAdjustment("cash_collection_quality", 5, "raise", "현금회수 확인 전에는 대형 프로젝트도 Stage 2다."),
    Round266ScoreAdjustment("safety_execution_trust", 5, "raise", "건설 안전 신뢰는 R10 hard gate다."),
    Round266ScoreAdjustment("permit_and_legal_clearance", 5, "raise", "법적 항소와 인허가가 풀려야 프로젝트가 실적이 된다."),
    Round266ScoreAdjustment("presales_and_unsold_inventory", 5, "raise", "주택정책은 분양률, 미분양, PF 안정으로 확인해야 한다."),
    Round266ScoreAdjustment("building_material_spread", 4, "raise", "건자재는 수요, spread, inventory, FCF가 함께 회복돼야 한다."),
    Round266ScoreAdjustment("public_contract_award_quality", 4, "raise", "공공공사는 실제 낙찰사와 계약금액이 있어야 한다."),
    Round266ScoreAdjustment("preferred_bidder_only", -5, "lower", "preferred bidder는 Stage 2 후보일 뿐 Green이 아니다."),
    Round266ScoreAdjustment("talks_or_MOU_only", -5, "lower", "협상 승인과 MOU는 final EPC contract가 아니다."),
    Round266ScoreAdjustment("public_infra_headline_only", -5, "lower", "공공청사 headline은 listed contractor award 전 Green이 아니다."),
    Round266ScoreAdjustment("housing_policy_only", -5, "lower", "주택정책은 presales/margin/PF 확인 전 event premium이다."),
    Round266ScoreAdjustment("candidate_consortium_only", -5, "lower", "컨소시엄 후보군은 award가 아니다."),
    Round266ScoreAdjustment("safety_incident", -5, "lower", "치명적 안전사고는 수주·정책 점수를 덮는 4C gate다."),
    Round266ScoreAdjustment("recurring_fatality_risk", -5, "lower", "반복 사망사고는 벌금과 면허 리스크를 만든다."),
    Round266ScoreAdjustment("license_revocation_risk", -5, "lower", "면허취소 가능성은 R10 Green을 차단한다."),
    Round266ScoreAdjustment("rebar_demand_weakness", -4, "lower", "철근 수요 약화는 건자재 spread와 이익을 깨뜨린다."),
    Round266ScoreAdjustment("legal_appeal_pending", -4, "lower", "법적 항소가 남아 있으면 final contract cashflow로 볼 수 없다."),
)

ROUND266_SHADOW_WEIGHT_ROWS: tuple[Round266ShadowWeightRow, ...] = (
    Round266ShadowWeightRow(E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2, 5, 5, 5, 5, 5, 4, 5, 0, 0, 4, -5, 5, 5, "Czech/Bulgaria nuclear is Stage 2 until final contract and legal clearance confirm."),
    Round266ShadowWeightRow(E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH, 0, 0, 0, 0, 0, 2, 5, 0, 0, 0, 0, 4, 5, "EDF/Westinghouse/Czech court halt requires legal 4C-watch."),
    Round266ShadowWeightRow(E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE, 0, 0, 0, 0, 0, 5, 2, 0, 0, 0, 0, 3, 5, "Anseong bridge collapse is sector hard safety reference."),
    Round266ShadowWeightRow(E2RArchetype.RECURRING_FATAL_ACCIDENT_REGULATORY_4C, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 4, 5, "Recurring fatalities can trigger 5% OP fine and license revocation."),
    Round266ShadowWeightRow(E2RArchetype.HOUSING_SUPPLY_POLICY_EVENT, 2, 2, 3, 4, 4, 2, 3, 5, 1, 2, -5, 5, 4, "Housing policy requires presales, margin, PF stability and FCF."),
    Round266ShadowWeightRow(E2RArchetype.PUBLIC_INFRASTRUCTURE_POLICY_EVENT, 3, 3, 3, 3, 3, 3, 3, 0, 0, 5, -5, 4, 3, "Public-infra headline needs listed award, contract value and margin."),
    Round266ShadowWeightRow(E2RArchetype.LNG_POWER_INFRA_CONSORTIUM_OPTION, 4, 4, 4, 4, 4, 3, 4, 0, 0, 4, -5, 4, 4, "Consortium candidate is not award; EPC scope/value/offtake required."),
    Round266ShadowWeightRow(E2RArchetype.BUILDING_MATERIALS_DEMAND_BREAK, 0, 0, 0, 4, 4, 2, 0, 3, 5, 0, 0, 3, 5, "Rebar/construction demand weakness requires spread/inventory/FCF watch."),
)

ROUND266_CASE_CANDIDATES: tuple[Round266CaseCandidate, ...] = (
    Round266CaseCandidate(
        case_id="r10_loop12_czech_nuclear_preferred_bid_legal_watch",
        symbol="034020/052690/051600/000720",
        company_name="Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / Hyundai E&C read-through",
        primary_archetype=E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2,
        secondary_archetypes=(E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="success_candidate",
        round_case_type="success_candidate_plus_legal_4c_watch",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2024, 7, 17),
        stage3_date=None,
        stage4b_date=date(2024, 7, 17),
        stage4c_date=date(2024, 8, 27),
        stage3_decision="preferred_bidder_not_green_until_final_contract_scope_margin_legal_clearance_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("czech_preferred_bidder", "two_reactors", "two_unit_implied_value_17_3bn_usd", "doosan_3m_plus_48pct", "kepco_ec_3m_plus_41pct"),
        red_flag_fields=("preferred_bidder_only", "legal_appeal_pending", "court_halt_risk", "scope_margin_unverified", "cash_collection_unverified"),
        price_data_source="Reuters / AP project and reported equity-return anchors",
        reported_price_anchor="Doosan Enerbility +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months",
        reported_return_anchor="Two-unit implied project value about $17.3B; later legal context around $18B contract halt",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"unit_cost_same_site_czk_bn": 200.0, "unit_cost_same_site_usd_bn": 8.65, "two_unit_implied_value_usd_bn": 17.3, "court_halt_project_value_context_usd_bn": 18.0, "doosan_enerbility_3m_mfe_pct": 48.0, "kepco_plant_se_3m_mfe_pct": 14.0, "kepco_ec_3m_mfe_pct": 41.0, "doosan_vs_kepco_ec_spread_pp": 7.0, "doosan_vs_kepco_plant_spread_pp": 34.0, "legal_watch_dates": "2024-08-27|2024-10-30|2025-05-06"},
        round_score_price_alignment="success_candidate_legal_4C_watch",
        score_price_alignment="aligned",
        round_rerating_result="nuclear_EPC_export_stage2",
        rerating_result="unknown",
        round_stage_failure_type="preferred_bidder_not_final_contract_green",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Preferred bidder is Stage 2; final contract, legal clearance, listed-company scope, margin and cash collection required before Green.",
    ),
    Round266CaseCandidate(
        case_id="r10_loop12_hyundai_ec_bulgaria_kozloduy_talks",
        symbol="000720",
        company_name="Hyundai E&C",
        primary_archetype=E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2,
        secondary_archetypes=(E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="success_candidate",
        round_case_type="success_candidate_insufficient_price_data",
        stage1_date=date(2024, 2, 23),
        stage2_date=date(2024, 2, 23),
        stage3_date=None,
        stage4b_date=date(2024, 2, 23),
        stage4c_date=None,
        stage3_decision="parliament_nod_and_talks_not_green_until_final_epc_value_scope_margin_financing_and_payment_schedule_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("bulgaria_parliament_nod", "two_reactors", "additional_capacity_2300mw", "unit7_completion_target_2033", "hyundai_outbid_bechtel"),
        red_flag_fields=("talks_or_MOU_only", "final_contract_unverified", "financing_unverified", "payment_schedule_unverified"),
        price_data_source="Reuters Bulgaria nuclear talks anchor",
        reported_price_anchor="Hyundai E&C OHLC unavailable after deep search",
        reported_return_anchor="Two reactors, 2,300MW added capacity, Unit 7 target 2033, Hyundai outbid Bechtel",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"new_reactors": 2.0, "additional_capacity_mw": 2300.0, "average_capacity_per_reactor_mw": 1150.0, "unit7_completion_target": 2033.0, "bid_context": "Hyundai outbid Bechtel"},
        round_score_price_alignment="success_candidate_but_insufficient_price_data",
        score_price_alignment="unknown",
        round_rerating_result="nuclear_EPC_pipeline_watch",
        rerating_result="unknown",
        round_stage_failure_type="talks_not_contract",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Parliament nod and talks are Stage 2; final EPC value, scope, margin, financing and payment schedule required.",
    ),
    Round266CaseCandidate(
        case_id="r10_loop12_hyundai_engineering_anseong_bridge_collapse",
        symbol="unlisted_Hyundai_Engineering/construction_safety_basket",
        company_name="Hyundai Engineering / Anseong bridge collapse",
        primary_archetype=E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="construction_safety_hard_reference",
        stage1_date=date(2025, 2, 25),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 25),
        stage3_decision="fatal_construction_collapse_is_sector_hard_reference_not_green_source",
        stage4b_status="none",
        hard_4c_confirmed=True,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("anseong_bridge_collapse", "fatalities_reuters_at_least_3", "fatalities_ap_4", "six_injured", "five_50m_support_structures"),
        red_flag_fields=("fatal_construction_collapse", "bridge_collapse", "site_manager_investigation", "unlisted_sector_reference"),
        price_data_source="Reuters / AP / Washington Post construction-collapse anchors",
        reported_price_anchor="Direct listed OHLC not applicable because Hyundai Engineering is not directly listed",
        reported_return_anchor="Reuters at least 3 dead, AP 4 dead, 6 injured, five 50m support structures collapsed sequentially",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fatalities_reuters_min": 3.0, "fatalities_ap": 4.0, "injured": 6.0, "support_structures": "five 50m structures", "collapse_type": "sequential collapse during bridge construction", "direct_listed_ticker": "N/A"},
        round_score_price_alignment="thesis_break_reference",
        score_price_alignment="false_positive_score",
        round_rerating_result="construction_safety_hard_reference",
        rerating_result="thesis_break",
        round_stage_failure_type="unlisted_but_sector_4C_reference",
        stage_failure_type="should_have_been_red",
        price_validation_status="unlisted_sector_reference",
        notes="Fatal collapse is sector hard 4C reference; Hyundai Engineering is not directly listed.",
    ),
    Round266CaseCandidate(
        case_id="r10_loop12_posco_dl_recurring_fatal_accident_regulation",
        symbol="construction_safety_basket",
        company_name="POSCO E&C / DL Construction safety read-through",
        primary_archetype=E2RArchetype.RECURRING_FATAL_ACCIDENT_REGULATORY_4C,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_SAFETY_REGULATORY_4C, E2RArchetype.WORKPLACE_FATALITY_REGULATORY_4C),
        case_type="4c_thesis_break",
        round_case_type="recurring_fatal_accident_regulatory_4c_watch",
        stage1_date=date(2025, 9, 15),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 15),
        stage3_decision="recurring_fatal_accident_regulation_blocks_green_until_safety_execution_and_license_risk_clear",
        stage4b_status="none",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("fine_up_to_5pct_operating_profit", "license_revocation_risk", "workplace_deaths_2024_589", "dl_executives_resigned_80"),
        red_flag_fields=("repeated_fatal_accidents", "license_revocation_risk", "work_suspension", "executive_resignations", "safety_incident"),
        price_data_source="Reuters safety-regulation / company-response anchors",
        reported_price_anchor="Direct OHLC unavailable after deep search",
        reported_return_anchor="Up to 5% OP fine, license revocation risk, 589 workplace deaths in 2024, about 80 DL executives resigned",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"proposed_fine_pct_of_operating_profit": 5.0, "license_revocation_risk": True, "workplace_deaths_2024": 589.0, "construction_share": "nearly_half", "implied_construction_deaths_approx": 295.0, "dl_executives_resigned": 80.0},
        round_score_price_alignment="thesis_break_watch",
        score_price_alignment="false_positive_score",
        round_rerating_result="recurring_fatal_accident_regulatory_watch",
        rerating_result="thesis_break",
        round_stage_failure_type="safety_4C_watch_not_green",
        stage_failure_type="should_have_been_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Repeated fatality regulation is 4C-watch; safety execution must override backlog and policy-score.",
    ),
    Round266CaseCandidate(
        case_id="r10_loop12_seoul_housing_ltv_supply_policy",
        symbol="housing_construction_basket",
        company_name="Seoul housing policy / construction basket",
        primary_archetype=E2RArchetype.HOUSING_SUPPLY_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_policy_watch",
        stage1_date=date(2025, 9, 7),
        stage2_date=date(2025, 9, 7),
        stage3_date=None,
        stage4b_date=date(2025, 9, 7),
        stage4c_date=None,
        stage3_decision="housing_policy_not_green_until_presales_margin_pf_unsold_inventory_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("ltv_50_to_40pct", "state_owned_lh_land_supply", "reconstruction_rule_streamlining", "affordable_housing_supply"),
        red_flag_fields=("housing_policy_only", "ltv_demand_shock", "presales_unverified", "pf_stability_unverified", "unsold_inventory_unverified"),
        price_data_source="Reuters housing-policy anchor",
        reported_price_anchor="Housing basket OHLC unavailable after deep search",
        reported_return_anchor="Gangnam/Yongsan LTV 50% to 40%, state-owned land and reconstruction simplification",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ltv_before_pct": 50.0, "ltv_after_pct": 40.0, "ltv_change_pp": -10.0, "ltv_change_relative_pct": -20.0, "policy_supply_tools": ["state-owned land / LH land", "reconstruction-rule streamlining", "affordable housing supply"]},
        round_score_price_alignment="event_premium_policy_watch",
        score_price_alignment="price_moved_without_evidence",
        round_rerating_result="housing_supply_policy_watch",
        rerating_result="event_premium",
        round_stage_failure_type="policy_not_presales_margin_green",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Policy mix is Stage 2; presales, margin, PF stability, unsold inventory and FCF required before Green.",
    ),
    Round266CaseCandidate(
        case_id="r10_loop12_sejong_presidential_office_public_infra",
        symbol="public_construction_basket",
        company_name="Sejong presidential office public-infra basket",
        primary_archetype=E2RArchetype.PUBLIC_INFRASTRUCTURE_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.INFRA_RECONSTRUCTION_POLICY, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_insufficient_evidence",
        stage1_date=date(2026, 4, 14),
        stage2_date=date(2026, 4, 14),
        stage3_date=None,
        stage4b_date=date(2026, 4, 14),
        stage4c_date=None,
        stage3_decision="public_infra_headline_not_green_until_listed_award_contract_value_margin_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("sejong_presidential_office", "site_area_350000_sqm", "site_preparation_cost_9_8bn_krw", "construction_period_14_months"),
        red_flag_fields=("public_infra_headline_only", "listed_contract_winner_not_disclosed", "contract_value_unverified", "margin_unverified"),
        price_data_source="Reuters public-infrastructure policy anchor",
        reported_price_anchor="Public construction basket OHLC unavailable after deep search",
        reported_return_anchor="350,000 sqm site, 9.8B won preparation cost, 14-month construction period, start target August 2027",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"site_area_sqm": 350000.0, "site_preparation_cost_krw_bn": 9.8, "site_preparation_cost_usd_mn": 6.6, "site_preparation_cost_per_sqm_krw": 28000.0, "construction_period_months": 14.0, "construction_start_target": "2027-08", "listed_contract_winner": "not_disclosed"},
        round_score_price_alignment="event_premium_insufficient_evidence",
        score_price_alignment="price_moved_without_evidence",
        round_rerating_result="public_infra_headline_watch",
        rerating_result="event_premium",
        round_stage_failure_type="no_listed_contract_no_green",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Public-infra headline is not Green without listed contractor, contract value, margin and cash collection.",
    ),
    Round266CaseCandidate(
        case_id="r10_loop12_daewoo_ec_nghi_son_lng_candidate",
        symbol="047040",
        company_name="Daewoo E&C / Nghi Son LNG candidate",
        primary_archetype=E2RArchetype.LNG_POWER_INFRA_CONSORTIUM_OPTION,
        secondary_archetypes=(E2RArchetype.GAS_INFRA_DELIVERY_VALIDATION, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="success_candidate",
        round_case_type="success_candidate_insufficient_evidence",
        stage1_date=date(2024, 8, 21),
        stage2_date=date(2024, 8, 21),
        stage3_date=None,
        stage4b_date=date(2024, 8, 21),
        stage4c_date=None,
        stage3_decision="consortium_candidate_not_green_until_award_epc_scope_margin_financing_and_offtake_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("vietnam_nghi_son_lng_project", "project_value_2_5bn_usd", "capacity_1_5gw", "commercial_operation_target_2030", "daewoo_potential_participant"),
        red_flag_fields=("candidate_consortium_only", "award_not_confirmed", "financing_unverified", "offtake_unverified", "epc_scope_unverified"),
        price_data_source="Reuters Vietnam LNG power project anchor",
        reported_price_anchor="Daewoo E&C OHLC unavailable after deep search",
        reported_return_anchor="$2.5B project, 1.5GW capacity, commercial operation target 2030, Daewoo named as possible consortium participant",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"project_value_usd_bn": 2.5, "capacity_gw": 1.5, "project_value_per_gw_usd_bn": 1.67, "commercial_operation_target": 2030.0, "potential_korean_participants": ["Korea Southern Power", "KOGAS", "Daewoo E&C", "SK E&S"], "award_status": "not confirmed in source"},
        round_score_price_alignment="success_candidate_but_insufficient_evidence",
        score_price_alignment="unknown",
        round_rerating_result="LNG_power_infra_consortium_option",
        rerating_result="unknown",
        round_stage_failure_type="candidate_not_award",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Consortium candidate is not award; EPC scope, value, margin, financing and offtake required before Green.",
    ),
    Round266CaseCandidate(
        case_id="r10_loop12_hyundai_steel_rebar_construction_demand_break",
        symbol="004020",
        company_name="Hyundai Steel / rebar proxy",
        primary_archetype=E2RArchetype.BUILDING_MATERIALS_DEMAND_BREAK,
        secondary_archetypes=(E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE, E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE),
        case_type="4c_thesis_break",
        round_case_type="building_material_4c_watch",
        stage1_date=date(2024, 6, 21),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2024, 6, 21),
        stage4c_date=date(2024, 6, 21),
        stage3_decision="building_material_green_requires_construction_demand_spread_inventory_and_fcf_recovery",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("event_price_29000_krw", "net_profit_forecast_cut_73pct", "target_price_cut_14pct", "rebar_price_expected_decline_10pct"),
        red_flag_fields=("building_material_demand_break", "rebar_demand_weakness", "net_profit_forecast_cut", "construction_demand_weakness", "shipbuilding_plate_competition"),
        price_data_source="MarketWatch / Dow Jones Market Talk price and estimate anchor",
        reported_price_anchor="shares -1.2% to 29,000 won; target cut 14% to 30,000 won",
        reported_return_anchor="2024 net-profit forecast cut 73% to 215B won; rebar price expected -10%",
        mfe_1d=None,
        mae_1d=-1.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=29000.0,
        extra_price_metrics={"event_price_krw": 29000.0, "event_mae_pct": -1.2, "implied_pre_event_reference_price_krw": 29352.0, "target_price_krw": 30000.0, "target_cut_pct": -14.0, "implied_prior_target_krw": 34884.0, "target_upside_from_event_price_pct": 3.45, "net_profit_forecast_2024_krw_bn": 215.0, "net_profit_forecast_cut_pct": -73.0, "implied_prior_net_profit_forecast_krw_bn": 796.3, "expected_rebar_price_decline_pct": -10.0},
        round_score_price_alignment="thesis_break_watch",
        score_price_alignment="false_positive_score",
        round_rerating_result="building_materials_demand_break",
        rerating_result="thesis_break",
        round_stage_failure_type="demand_spread_not_green",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Weak construction demand and rebar-price decline block building-material Green until spread, inventory and FCF recover.",
    ),
)


def round266_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND266_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND266_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round266 R10 Loop-12 construction/real-estate/materials price validation case. Calibration-only; not production scoring input.",
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "policy" in field or "collapse" in field or "project" in field or "bidder" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "final_contract" in field or "margin" in field or "cash" in field or "presales" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "rally" in field or "price" in field or "preferred" in field or "policy" in field or "candidate" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "collapse" in field or "fatal" in field or "legal" in field or "license" in field or "demand" in field or "appeal" in field or "safety" in field),
            must_have_fields=ROUND266_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=("; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "failed_rerating", "4c_thesis_break"} else None),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND266_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "direct_listed_hard_4c_confirmed_false",
                "do_not_invent_ohlc_stage_prices_mfe_mae_margin_working_capital_cash_collection_presales_or_pf_data",
                "do_not_treat_preferred_bidder_talks_policy_public_infra_candidate_consortium_or_rebar_target_upside_as_green",
                "do_not_ignore_safety_legal_pf_or_building_material_demand_hard_gates",
                f"round_case_type={candidate.round_case_type}",
                f"round_score_price_alignment={candidate.round_score_price_alignment}",
                f"round_rerating_result={candidate.round_rerating_result}",
                f"round_stage_failure_type={candidate.round_stage_failure_type}",
                *ROUND266_GREEN_REQUIRED_FIELDS,
                *ROUND266_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.stage2_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                    or "return_anchor" in candidate.price_validation_status
                ),
                stage_dates_confidence=0.86 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round266_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND266_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
                "round_case_type": candidate.round_case_type,
                "stage1_date": _date_text(candidate.stage1_date),
                "stage2_date": _date_text(candidate.stage2_date),
                "stage3_date": _date_text(candidate.stage3_date),
                "stage4b_date": _date_text(candidate.stage4b_date),
                "stage4c_date": _date_text(candidate.stage4c_date),
                "stage3_decision": candidate.stage3_decision,
                "stage4b_status": candidate.stage4b_status,
                "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
                "direct_listed_hard_4c_confirmed": str(candidate.direct_listed_hard_4c_confirmed).lower(),
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "round_score_price_alignment": candidate.round_score_price_alignment,
                "score_price_alignment": candidate.score_price_alignment,
                "round_rerating_result": candidate.round_rerating_result,
                "rerating_result": candidate.rerating_result,
                "round_stage_failure_type": candidate.round_stage_failure_type,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round266_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND266_SCORE_ADJUSTMENTS)


def round266_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND266_SHADOW_WEIGHT_ROWS)


def round266_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round266_price_validation": "true"} for field in ROUND266_PRICE_VALIDATION_FIELDS)


def round266_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round266_label": label, "canonical_archetype": canonical} for label, canonical in ROUND266_REQUIRED_TARGET_ALIASES.items())


def round266_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "large_sector": ROUND266_LARGE_SECTOR} for item in ROUND266_DEEP_SUB_ARCHETYPES)


def round266_summary() -> dict[str, int | bool | str]:
    cases = ROUND266_CASE_CANDIDATES
    return {
        "source_round": ROUND266_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND266_ANALYST_ROUND_ID,
        "large_sector": ROUND266_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "safety_hard_reference_count": sum(1 for case in cases if case.primary_archetype == E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "direct_listed_hard_4c_case_count": sum(1 for case in cases if case.direct_listed_hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "thesis_break_watch_count": sum(1 for case in cases if "watch" in case.round_score_price_alignment or case.case_type == "4c_thesis_break"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND266_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND266_DEEP_SUB_ARCHETYPES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
        "direct_listed_hard_4c_confirmed": False,
    }


def round266_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND266_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND266_ANALYST_ROUND_ID,
        "large_sector": ROUND266_LARGE_SECTOR,
        "summary": round266_summary(),
        "target_aliases": dict(ROUND266_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND266_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND266_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND266_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND266_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND266_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND266_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round266_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_preferred_bidder_talks_policy_public_infra_candidate_consortium_or_rebar_target_upside_as_green",
            "do_not_ignore_safety_legal_pf_or_building_material_demand_hard_gates",
            "do_not_invent_ohlc_margin_working_capital_cash_collection_presales_pf_or_contract_award_data",
        ],
    }


def render_round266_summary_markdown() -> str:
    summary = round266_summary()
    lines = [
        "# Round 266 R10 Loop 12 Construction Real Estate Materials Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- safety_hard_reference_count: {summary['safety_hard_reference_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- direct_listed_hard_4c_case_count: {summary['direct_listed_hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | direct listed hard 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND266_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    str(case.hard_4c_confirmed).lower(),
                    str(case.direct_listed_hard_4c_confirmed).lower(),
                    case.round_score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Czech nuclear is strong Stage 2 plus legal 4C-watch, not Green before final contract and legal clearance.",
            "- Bulgaria Kozloduy is Stage 2 pipeline evidence; talks are not a final EPC contract.",
            "- Anseong bridge collapse is an unlisted but sector-level hard safety reference.",
            "- POSCO E&C / DL safety regulation is recurring fatality 4C-watch.",
            "- Seoul housing policy is event premium until presales, margin, PF and unsold inventory confirm.",
            "- Sejong presidential office is public-infra headline until listed award and contract value exist.",
            "- Nghi Son LNG is a consortium option until award, EPC scope, financing and offtake confirm.",
            "- Hyundai Steel rebar weakness is building-material demand 4C-watch.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round266_green_gate_review_markdown() -> str:
    lines = [
        "# Round 266 R10 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND266_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND266_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND266_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `preferred bidder` is Stage 2 until final contract, legal clearance, scope, margin and cash collection are visible.",
            "- `housing policy` is event premium until presales, PF stability, unsold inventory and FCF are visible.",
            "- `public-infra headline` is not Green until a listed contractor wins a contract with value and margin.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round266_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 266 R10 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND266_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND266_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | 4C date | hard 4C | direct listed hard 4C | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND266_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {str(case.direct_listed_hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round266_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 266 R10 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- hard_4c_confirmed: true_for_safety_reference",
        "- direct_listed_hard_4c_confirmed: false",
        "- Do not invent OHLC, peak, MFE, MAE, margin, working capital, cash collection, presales, PF, contract award, or legal clearance.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND266_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND266_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round266_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 266 R10 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND266_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round266_r10_loop12_reports(
    output_directory: str | Path = ROUND266_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND266_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND266_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round266_case_records(), cases_path),
        "audit": _write_json(round266_audit_payload(), audit_path),
        "summary": output / "round266_r10_loop12_price_validation_summary.md",
        "case_matrix": output / "round266_r10_loop12_case_matrix.csv",
        "target_aliases": output / "round266_r10_loop12_target_aliases.csv",
        "deep_sub_archetypes": output / "round266_r10_loop12_deep_sub_archetypes.csv",
        "score_adjustments": output / "round266_r10_loop12_score_adjustments.csv",
        "shadow_weights": output / "round266_r10_loop12_shadow_weights.csv",
        "price_validation_fields": output / "round266_r10_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round266_r10_loop12_green_gate_review.md",
        "price_validation_plan": output / "round266_r10_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round266_r10_loop12_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round266_r10_loop12_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round266_summary_markdown(), encoding="utf-8")
    _write_csv(round266_case_rows(), paths["case_matrix"])
    _write_csv(round266_target_alias_rows(), paths["target_aliases"])
    _write_csv(round266_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round266_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round266_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round266_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round266_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round266_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round266_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round266_deep_sub_archetypes_markdown(), encoding="utf-8")
    return paths


def _write_json(payload: object, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[dict[str, str]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows = tuple(rows)
    if not rows:
        target.write_text("", encoding="utf-8")
        return target
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed(value: int) -> str:
    return f"{value:+d}"
