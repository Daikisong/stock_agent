"""Round-260 R4 Loop-12 materials/spread/strategic-resources pack.

This module converts ``docs/round/round_260.md`` into calibration-only
case-library records and reports. It intentionally leaves production scoring,
candidate generation, and StageClassifier thresholds unchanged.

Easy example: a Korean anti-dumping tariff can help Hyundai Steel for a day,
but the same steel company can be hurt by U.S. export tariffs. That is why this
pack treats policy relief as Stage 2/watch until product spread, working
capital, and FCF are visible.
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


ROUND260_SOURCE_ROUND_PATH = "docs/round/round_260.md"
ROUND260_ROUND_ID = "round_188"
ROUND260_LARGE_SECTOR = Round10LargeSector.MATERIALS_SPREAD_STRATEGIC.value
ROUND260_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round260_r4_loop12_materials_spread_strategic_price_validation"
ROUND260_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop12_round260.jsonl"
ROUND260_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round260_r4_loop12_materials_spread_strategic_price_validation_audit.json"

ROUND260_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DEFENSE_METALS_AMMUNITION_OPTIONALITY": E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY.value,
    "CRITICAL_MINERALS_RECYCLING_SMELTER": E2RArchetype.CRITICAL_MINERALS_RECYCLING_SMELTER.value,
    "RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C": E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C.value,
    "STEEL_TARIFF_TWO_SIDED_RELIEF_RISK": E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK.value,
    "POLICY_CAPEX_FALSE_POSITIVE": E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE.value,
    "PETROCHEMICAL_CAPACITY_RESTRUCTURING": E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING.value,
    "STANDALONE_NCC_CREDIT_BREAK": E2RArchetype.STANDALONE_NCC_CREDIT_BREAK.value,
    "CRITICAL_MINERALS_POLICY_RELIEF": E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF.value,
}

ROUND260_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "product_spread_confirmed",
    "cost_curve_advantage_confirmed",
    "offtake_price_floor_or_take_or_pay_confirmed",
    "supply_discipline_or_capacity_shutdown_confirmed",
    "restructuring_after_opm_fcf_improvement",
    "working_capital_stable",
    "china_tariff_rare_earth_end_use_risk_passed",
    "dilution_governance_risk_passed",
    "price_path_after_evidence",
)

ROUND260_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "mna_rumor_only",
    "policy_relief_only",
    "strategic_material_headline_only",
    "us_capex_without_roi",
    "capacity_shutdown_without_spread_recovery",
    "restructuring_plan_undisclosed",
    "rare_earth_end_use_restriction_present",
    "tariff_export_risk_unresolved",
    "dilution_for_project_capex_unresolved",
)

ROUND260_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "mna_rumor_materials_rally",
    "strategic_minerals_headline_price_first",
    "anti_dumping_tariff_relief_rally",
    "critical_minerals_policy_basket_rally",
    "us_capex_announcement_rally_then_fade",
    "petrochemical_restructuring_relief_rally",
    "support_package_without_debt_cleanup",
)

ROUND260_HARD_4C_GATES: tuple[str, ...] = (
    "rare_earth_export_restriction_causing_supply_halt",
    "china_end_use_sanction",
    "us_tariff_destroying_export_margin",
    "project_capex_funding_failure",
    "equity_dilution_without_roi",
    "ncc_credit_break_or_workout",
    "standalone_cracker_shutdown_from_distress",
    "spread_collapse",
    "working_capital_blowout",
    "offtake_failure",
)

ROUND260_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "project_or_policy_anchor",
    "spread_capacity_or_import_anchor",
    "dilution_or_credit_anchor",
    "tariff_or_export_control_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round260ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round260ShadowWeightRow:
    archetype: E2RArchetype
    product_spread: int
    cost_curve: int
    offtake_quality: int
    supply_discipline: int
    capacity_shutdown: int
    working_capital: int
    fcf_after_restructuring: int
    critical_minerals_security: int
    governance_dilution: int
    export_control_resilience: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "product_spread": _signed(self.product_spread),
            "cost_curve": _signed(self.cost_curve),
            "offtake_quality": _signed(self.offtake_quality),
            "supply_discipline": _signed(self.supply_discipline),
            "capacity_shutdown": _signed(self.capacity_shutdown),
            "working_capital": _signed(self.working_capital),
            "fcf_after_restructuring": _signed(self.fcf_after_restructuring),
            "critical_minerals_security": _signed(self.critical_minerals_security),
            "governance_dilution": _signed(self.governance_dilution),
            "export_control_resilience": _signed(self.export_control_resilience),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round260DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round260CaseCandidate:
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
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    round_rerating_label: str
    stage_failure_type: str
    round_stage_failure_label: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND260_SCORE_ADJUSTMENTS: tuple[Round260ScoreAdjustment, ...] = (
    Round260ScoreAdjustment("product_spread", 5, "raise", "R4는 전략자원 headline보다 제품 spread 확인이 먼저다."),
    Round260ScoreAdjustment("cost_curve_advantage", 5, "raise", "원가곡선 우위가 있어야 spread가 흔들려도 FCF가 남는다."),
    Round260ScoreAdjustment("offtake_quality", 5, "raise", "전략광물은 offtake, price floor, take-or-pay로 cycle과 분리되어야 한다."),
    Round260ScoreAdjustment("supply_discipline", 5, "raise", "공급규율과 실제 capacity shutdown은 spread 지속성을 높인다."),
    Round260ScoreAdjustment("capacity_shutdown_confirmed", 5, "raise", "shutdown이 실제이고 지속될 때만 구조조정 relief 품질이 올라간다."),
    Round260ScoreAdjustment("working_capital_control", 5, "raise", "운전자본이 무너지면 spread 회복도 현금흐름으로 닫히지 않는다."),
    Round260ScoreAdjustment("FCF_after_restructuring", 5, "raise", "구조조정 뒤 OPM과 FCF가 보여야 Green 후보가 된다."),
    Round260ScoreAdjustment("critical_minerals_supply_security", 4, "raise", "전략광물 공급 안정은 실제 supply contract와 inventory로 내려와야 한다."),
    Round260ScoreAdjustment("governance_and_dilution_control", 4, "raise", "프로젝트 품질이 좋아도 희석과 지배구조를 통과해야 한다."),
    Round260ScoreAdjustment("export_control_resilience", 5, "raise", "중국 end-use 제한과 관세 리스크를 견뎌야 한다."),
    Round260ScoreAdjustment("M&A_rumor_only", -5, "lower", "M&A rumor는 event premium이지 Green 근거가 아니다."),
    Round260ScoreAdjustment("policy_relief_only", -5, "lower", "정책지원은 실제 spread와 FCF 전에는 Stage 2 relief다."),
    Round260ScoreAdjustment("strategic_material_headline_only", -5, "lower", "전략자원 headline만으로 EPS/FCF 체급 변화가 증명되지 않는다."),
    Round260ScoreAdjustment("US_CAPEX_without_ROI", -5, "lower", "미국 CAPEX는 고객수요, spread, margin, FCF가 확인되어야 한다."),
    Round260ScoreAdjustment("capacity_shutdown_without_spread_recovery", -4, "lower", "shutdown만 있고 spread 회복이 없으면 crisis relief다."),
    Round260ScoreAdjustment("restructuring_plan_undisclosed", -4, "lower", "공개되지 않은 구조조정 계획은 Green 근거가 아니다."),
    Round260ScoreAdjustment("China_customer_or_material_concentration", -5, "lower", "중국 원료·고객 집중은 sanction과 tariff risk를 키운다."),
    Round260ScoreAdjustment("rare_earth_end_use_restriction", -5, "lower", "희토류 end-use 제한은 sector 4C-watch다."),
    Round260ScoreAdjustment("tariff_export_risk", -5, "lower", "수출 관세가 margin을 훼손하면 domestic relief를 상쇄한다."),
    Round260ScoreAdjustment("dilution_for_project_capex", -4, "lower", "ROI 없는 프로젝트 증자는 RedTeam 입력이다."),
)


ROUND260_SHADOW_WEIGHT_ROWS: tuple[Round260ShadowWeightRow, ...] = (
    Round260ShadowWeightRow(E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY, 3, 3, 4, 2, 0, 4, 4, 3, 3, 3, -5, 5, 3, "Poongsan M&A rumor is event premium until confirmed transaction/order/spread."),
    Round260ShadowWeightRow(E2RArchetype.CRITICAL_MINERALS_RECYCLING_SMELTER, 4, 5, 5, 3, 0, 5, 5, 5, 5, 5, -3, 5, 4, "Korea Zinc is strong Stage 2 but dilution/offtake/project execution must clear."),
    Round260ShadowWeightRow(E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C, 0, 0, 0, 0, 0, 3, 3, 5, 2, 5, 0, 4, 5, "China rare-earth end-use restriction is sector 4C-watch."),
    Round260ShadowWeightRow(E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK, 5, 4, 2, 3, 0, 4, 4, 0, 3, 5, -4, 5, 5, "Domestic tariff relief and export tariff risk must be scored together."),
    Round260ShadowWeightRow(E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, 3, 3, 2, 1, 0, 5, 5, 1, 5, 4, -5, 5, 5, "Hyundai Steel U.S. CAPEX failed price validation due funding/ROI uncertainty."),
    Round260ShadowWeightRow(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, 5, 4, 1, 5, 5, 5, 5, 0, 3, 2, -3, 4, 5, "Capacity shutdown is relief until spread/OPM/FCF improve."),
    Round260ShadowWeightRow(E2RArchetype.STANDALONE_NCC_CREDIT_BREAK, 5, 3, 0, 5, 5, 5, 5, 0, 3, 2, 0, 3, 5, "YNCC debt/equity 249% and cracker shutdown are 4C-watch."),
    Round260ShadowWeightRow(E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF, 2, 2, 3, 3, 0, 2, 2, 5, 2, 5, -5, 4, 4, "Policy support is Stage 2 only; actual supply/of-take/margin required."),
)


ROUND260_DEEP_SUB_ARCHETYPES: tuple[Round260DeepSubArchetype, ...] = (
    Round260DeepSubArchetype("방산·금속 optionality", E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY, ("Poongsan", "copper products", "ammunition", "Hanwha acquisition rumor", "denial")),
    Round260DeepSubArchetype("전략광물 smelter", E2RArchetype.CRITICAL_MINERALS_RECYCLING_SMELTER, ("Korea Zinc", "Tennessee smelter", "data-center waste", "antimony", "gallium", "germanium")),
    Round260DeepSubArchetype("희토류·중국 end-use overlay", E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C, ("China letters", "U.S. defense firms", "transformers", "batteries", "aerospace")),
    Round260DeepSubArchetype("철강 관세 양면성", E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK, ("POSCO", "Hyundai Steel", "SeAH Steel", "anti-dumping", "U.S. tariff 50%")),
    Round260DeepSubArchetype("정책 CAPEX false positive", E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, ("Hyundai Steel Louisiana plant", "funding uncertainty", "CAPEX without ROI")),
    Round260DeepSubArchetype("석유화학 credit break", E2RArchetype.STANDALONE_NCC_CREDIT_BREAK, ("LG Chem", "Hanwha Solutions", "DL Chemical", "YNCC", "debt-to-equity 249%")),
    Round260DeepSubArchetype("석유화학 구조조정 relief", E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, ("Lotte Chemical", "HD Hyundai Chemical", "Daesan NCC shutdown", "support package")),
    Round260DeepSubArchetype("전략자원 정책 relief", E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF, ("17 monitored minerals", "China hotline", "FORGE", "250B won overseas mining support")),
)


ROUND260_CASE_CANDIDATES: tuple[Round260CaseCandidate, ...] = (
    Round260CaseCandidate(
        case_id="r4_loop12_poongsan_defense_metals_mna_rumor",
        symbol="103140",
        company_name="Poongsan",
        primary_archetype=E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE, E2RArchetype.DEFENSE_AMMO_EVENT_PREMIUM, E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY),
        case_type="event_premium",
        round_case_type="event_premium / defense-metals optionality",
        stage1_date=date(2026, 4, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2026, 4, 9),
        stage4c_date=None,
        stage3_decision="mna_rumor_is_not_green_before_confirmed_transaction_defense_order_copper_spread_or_cash_return",
        stage4b_status="4B/event premium",
        hard_4c_confirmed=False,
        evidence_fields=("reported_hanwha_bid_for_defense_business", "potential_deal_value_1_5tn_krw", "copper_products", "ammunition_business"),
        red_flag_fields=("mna_rumor_only", "hanwha_dropped_review", "poongsan_denied_sale_plan", "confirmed_order_absent"),
        price_data_source="Reuters M&A rumor / denial anchors",
        reported_price_anchor="Potential sale rumor around 1.5T KRW / $1.1B, then review dropped and sale denied",
        reported_return_anchor="Full adjusted OHLC unavailable; rumor-driven optionality only",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"reported_potential_deal_value_krw_trn": 1.5, "reported_potential_deal_value_usd_bn": 1.1, "businesses": ["copper products", "small-caliber rounds", "large-caliber shells", "missile warheads"], "transaction_status": "not confirmed; Hanwha dropped review; Poongsan denied sale plan"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_insufficient_price_data",
        rerating_result="event_premium",
        round_rerating_label="defense_metals_M&A_optional_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="rumor_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="M&A rumor는 Green이 아니다. 예: 실제 인수계약, 탄약 수주, 구리 spread, 현금환원이 확인돼야 Stage 2 이후로 간다.",
    ),
    Round260CaseCandidate(
        case_id="r4_loop12_korea_zinc_critical_minerals_dilution_watch",
        symbol="010130",
        company_name="Korea Zinc",
        primary_archetype=E2RArchetype.CRITICAL_MINERALS_RECYCLING_SMELTER,
        secondary_archetypes=(E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN, E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE),
        case_type="success_candidate",
        round_case_type="success_candidate + dilution/governance 4B-watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 3, 12),
        stage3_date=None,
        stage4b_date=date(2025, 12, 31),
        stage4c_date=None,
        stage3_decision="strategic_minerals_stage2_not_green_until_fid_offtake_minimum_price_margin_fcf_and_dilution_control",
        stage4b_status="4B-watch dilution/governance",
        hard_4c_confirmed=False,
        evidence_fields=("tennessee_smelter_project_7_4bn_usd", "planned_output_540000_tonnes", "eleven_critical_minerals", "target_margin_17_19pct", "op_2025_1_2tn_krw"),
        red_flag_fields=("share_issuance_2_833tn_krw", "share_issuance_26_2pct_of_project_value", "offtake_unconfirmed", "fid_permit_execution_unconfirmed", "governance_risk"),
        price_data_source="Reuters critical-minerals / share-issuance anchors",
        reported_price_anchor="U.S. Tennessee smelter $7.4B; 2.833T KRW share issuance means dilution gate",
        reported_return_anchor="Full adjusted OHLC unavailable; project quality high but offtake/FCF not closed",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"us_smelter_project_value_usd_bn": 7.4, "planned_output_tonnes": 540000, "critical_minerals_count": 11, "target_margin_pct": "17-19", "operating_profit_2025_krw_trn": 1.2, "antimony_price_2025_usd_per_lb": 25.0, "share_issuance_krw_trn": 2.833, "share_issuance_usd_bn": 1.94, "share_issuance_vs_project_value_pct": 26.2, "planned_construction": "early_2027", "planned_operation_year": 2030},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_dilution_watch",
        rerating_result="unknown",
        round_rerating_label="critical_minerals_project_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="strategic_stage2_not_green_until_offtake_FCF",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="전략광물 구조는 강하지만, offtake·최저가격·마진·FCF·희석 통과 전에는 Green이 아니다.",
    ),
    Round260CaseCandidate(
        case_id="r4_loop12_china_rare_earth_end_use_restriction_overlay",
        symbol="transformer/battery/display/EV/aerospace/medical_equipment_basket",
        company_name="Korean rare-earth-dependent manufacturers",
        primary_archetype=E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C,
        secondary_archetypes=(E2RArchetype.RARE_EARTH_THEME_KOREA, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="4b_watch",
        round_case_type="4C-watch / strategic supply-chain overlay",
        stage1_date=date(2025, 4, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="rare_earth_end_use_restriction_is_redteam_overlay_not_green",
        stage4b_status="4C-watch sector overlay",
        hard_4c_confirmed=False,
        evidence_fields=("china_letters_to_korean_companies", "rare_earth_containing_products", "affected_power_transformers_batteries_displays_ev_aerospace_medical_equipment", "us_defense_end_use_restriction"),
        red_flag_fields=("rare_earth_end_use_restriction", "sanction_warning", "china_material_concentration", "customer_export_control_risk"),
        price_data_source="Reuters rare-earth export-control report",
        reported_price_anchor="Sector overlay; no company-level adjusted OHLC in this pass",
        reported_return_anchor="China reportedly asked Korean firms not to export Chinese rare-earth-containing products to U.S. defense firms",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"affected_sectors": ["power transformers", "batteries", "displays", "electric vehicles", "aerospace", "medical equipment"], "reported_action": "China sent letters asking Korean companies not to export products using Chinese rare earths to U.S. defense firms", "sanction_warning": True},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="rare_earth_end_use_restriction_overlay",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="sector_4C_watch",
        price_validation_status="sector_overlay_no_company_ohlc",
        notes="전략자원 수혜와 동시에 중국 end-use restriction이 붙으면 RedTeam overlay다.",
    ),
    Round260CaseCandidate(
        case_id="r4_loop12_posco_hyundai_seah_steel_tariff_two_sided",
        symbol="005490/004020/306200",
        company_name="POSCO Holdings / Hyundai Steel / SeAH Steel",
        primary_archetype=E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK,
        secondary_archetypes=(E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF, E2RArchetype.STEEL_TARIFF_EXPORT_RISK),
        case_type="event_premium",
        round_case_type="event_premium + 4C-watch",
        stage1_date=date(2025, 2, 1),
        stage2_date=date(2025, 2, 20),
        stage3_date=None,
        stage4b_date=date(2025, 2, 20),
        stage4c_date=date(2025, 6, 2),
        stage3_decision="domestic_antidumping_relief_is_not_green_when_us_export_tariff_risk_is_unresolved",
        stage4b_status="4B-watch policy relief plus 4C-watch export tariff",
        hard_4c_confirmed=False,
        evidence_fields=("korea_antidumping_tariff_27_91_38_02pct", "hyundai_steel_plus_5_8pct", "posco_plus_3_9pct", "china_steel_imports_10_4bn_usd"),
        red_flag_fields=("us_25pct_tariff_talk", "us_50pct_tariff_event", "seah_steel_minus_8pct", "export_margin_risk", "policy_relief_only"),
        price_data_source="Reuters steel tariff / event-return anchors",
        reported_price_anchor="Hyundai Steel +5.8%, POSCO +3.9% on Korea relief; SeAH Steel -8% on U.S. 50% tariff event",
        reported_return_anchor="Domestic anti-dumping relief and U.S. export tariff risk point in opposite directions",
        mfe_1d=5.8,
        mae_1d=-8.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"korea_antidumping_tariff_pct": "27.91-38.02", "hyundai_steel_relief_mfe_pct": 5.8, "posco_relief_mfe_pct": 3.9, "kospi_relief_context_pct": -0.7, "hyundai_relative_outperformance_pp": 6.5, "posco_relative_outperformance_pp": 4.6, "us_25pct_tariff_posco_mae_pct": -3.6, "us_25pct_tariff_hyundai_mae_pct": -2.9, "us_50pct_tariff_posco_hyundai_mae_pct": -3.0, "seah_steel_50pct_tariff_mae_pct": -8.0, "china_steel_imports_2024_usd_bn": 10.4, "china_share_of_korea_steel_imports_pct": 49.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_thesis_break_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="steel_policy_relief_with_export_tariff_risk",
        stage_failure_type="false_yellow",
        round_stage_failure_label="policy_relief_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="국내 anti-dumping relief만 보면 Stage 2지만, U.S. tariff가 export margin을 때리면 Green이 막힌다.",
    ),
    Round260CaseCandidate(
        case_id="r4_loop12_hyundai_steel_us_capex_false_positive",
        symbol="004020",
        company_name="Hyundai Steel",
        primary_archetype=E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK, E2RArchetype.STEEL_TARIFF_EXPORT_RISK),
        case_type="failed_rerating",
        round_case_type="failed_rerating / policy CAPEX false positive",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 3, 25),
        stage3_date=None,
        stage4b_date=date(2025, 3, 25),
        stage4c_date=date(2025, 4, 22),
        stage3_decision="us_plant_and_tariff_hedge_are_not_green_without_confirmed_demand_spread_margin_fcf_and_funding",
        stage4b_status="4C-watch / CAPEX fade",
        hard_4c_confirmed=False,
        evidence_fields=("louisiana_plant_5_8bn_usd", "annual_capacity_2_7mn_tonnes", "hyundai_group_us_package_21bn_usd", "capital_increase_2_9bn_usd"),
        red_flag_fields=("funding_unclear", "announcement_plus_5_then_minus_4_4pct", "post_announcement_drawdown_21_2pct", "capex_without_confirmed_roi", "equity_and_borrowing_burden"),
        price_data_source="Reuters U.S. steel plant / investor backlash / capital-increase anchors",
        reported_price_anchor="Initial >+5% reversed to -4.4%, then -21.2% since announcement",
        reported_return_anchor="$5.8B Louisiana plant; later funding clarified as $2.9B equity + $2.9B external borrowing",
        mfe_1d=5.0,
        mae_1d=-21.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"plant_investment_usd_bn": 5.8, "annual_capacity_mn_tonnes": 2.7, "group_us_investment_package_usd_bn": 21.0, "announcement_initial_mfe_pct": 5.0, "announcement_session_mae_pct": -4.4, "post_announcement_drawdown_pct": -21.2, "posco_same_period_pct": -18.3, "kospi_same_period_pct": -5.5, "relative_underperformance_vs_kospi_pp": -15.7, "capital_increase_2026_usd_bn": 2.9, "funding_structure": "$2.9B equity + $2.9B external borrowing", "production_start_target": 2029},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="no_rerating",
        round_rerating_label="policy_CAPEX_failed_rerating",
        stage_failure_type="false_green",
        round_stage_failure_label="CAPEX_without_confirmed_ROI",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="미국 공장과 tariff hedge는 좋아 보이지만, 고객수요·spread·margin·FCF가 없으면 policy CAPEX false positive다.",
    ),
    Round260CaseCandidate(
        case_id="r4_loop12_lgchem_hanwha_dl_yncc_petrochemical_credit_watch",
        symbol="051910/009830/DL_Chemical_exposure",
        company_name="LG Chem / Hanwha Solutions / DL Chemical / YNCC",
        primary_archetype=E2RArchetype.STANDALONE_NCC_CREDIT_BREAK,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, E2RArchetype.COMMODITY_PRICE_4C_OVERLAY),
        case_type="4b_watch",
        round_case_type="4C-watch / petrochemical overcapacity",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2025, 12, 19),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 8, 27),
        stage3_decision="restructuring_plan_is_relief_not_green_until_capacity_cut_spread_opm_fcf_and_debt_cleanup_confirm",
        stage4b_status="4C-watch petrochemical credit stress",
        hard_4c_confirmed=False,
        evidence_fields=("capacity_cut_target_2_7_3_7mn_tpy", "standalone_naphtha_cracker_shutdown_risk", "yncc_debt_to_equity_249pct", "yncc_no3_cracker_shut"),
        red_flag_fields=("standalone_ncc_credit_break", "restructuring_plan_undisclosed", "shaheen_new_supply_1_8mn_tpy", "china_middle_east_overcapacity", "debt_cleanup_unconfirmed"),
        price_data_source="Reuters petrochemical overhaul / restructuring-plan anchors",
        reported_price_anchor="Full adjusted OHLC unavailable; sector capacity cut and credit-stress anchors only",
        reported_return_anchor="YNCC debt-to-equity 249%; one or two crackers may shut; No.3 cracker already shut",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"capacity_cut_target_mn_tpy": "2.7-3.7", "capacity_cut_equivalent_pct": 25.0, "naphtha_feedstock_share_for_ethylene_pct": 82.0, "yncc_debt_to_equity_1h2025_pct": 249.0, "yncc_possible_shutdown": "one or two of three crackers", "yncc_no3_cracker_status": "shut in August 2025", "shaheen_new_supply_2026_mn_tpy": 1.8, "lg_chem_plan_status": "submitted but details undisclosed", "dl_hanwha_yncc_plan_status": "submitted but details undisclosed"},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="petrochemical_credit_and_capacity_break_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="restructuring_plan_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="정부가 capacity cut을 요구한 것은 sector crisis 증거다. spread와 FCF 전에는 구조적 Green이 아니다.",
    ),
    Round260CaseCandidate(
        case_id="r4_loop12_lotte_hd_hyundai_chemical_restructuring_relief",
        symbol="011170/267250_exposure",
        company_name="Lotte Chemical / HD Hyundai Chemical",
        primary_archetype=E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA, E2RArchetype.STANDALONE_NCC_CREDIT_BREAK),
        case_type="failed_rerating",
        round_case_type="failed_rerating_then_policy_relief",
        stage1_date=date(2025, 11, 26),
        stage2_date=date(2026, 2, 24),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="daesan_ncc_shutdown_and_support_package_are_relief_not_green_before_spread_opm_fcf_and_debt_cleanup",
        stage4b_status="relief watch",
        hard_4c_confirmed=False,
        evidence_fields=("daesan_ncc_shutdown_1_1mn_tpy", "shutdown_duration_3_years", "capital_increase_1_2tn_krw", "government_support_above_2tn_krw"),
        red_flag_fields=("capacity_shutdown_without_spread_recovery", "capital_increase_required", "china_middle_east_oversupply_persists", "shaheen_supply_addition", "debt_cleanup_unconfirmed"),
        price_data_source="Reuters first petrochemical restructuring approval anchors",
        reported_price_anchor="1.1M tpy Daesan NCC shutdown for three years; 1.2T KRW capital increase",
        reported_return_anchor="Support package is relief; spread/OPM/FCF not yet confirmed",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"daesan_ncc_shutdown_capacity_mn_tpy": 1.1, "shutdown_duration_years": 3, "capital_increase_krw_trn": 1.2, "each_parent_injection_krw_bn": 600.0, "government_support_package_krw_trn_min": 2.0, "utility_cost_savings_krw_bn": 115.0, "rnd_funding_krw_bn": 26.0, "equity_split_after_restructuring": "50:50", "national_capacity_cut_target_mn_tpy": 3.7},
        score_price_alignment="unknown",
        round_alignment_label="failed_rerating_then_policy_relief",
        rerating_result="credit_relief_rally",
        round_rerating_label="petrochemical_restructuring_relief",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="relief_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Daesan shutdown과 정부지원은 crisis relief다. spread·OPM·FCF가 돌아오기 전 Stage 3가 아니다.",
    ),
    Round260CaseCandidate(
        case_id="r4_loop12_korea_critical_minerals_policy_relief",
        symbol="critical_minerals_basket",
        company_name="Korea critical-minerals policy basket",
        primary_archetype=E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF,
        secondary_archetypes=(E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN, E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C),
        case_type="success_candidate",
        round_case_type="success_candidate policy relief",
        stage1_date=date(2026, 2, 5),
        stage2_date=date(2026, 2, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="policy_relief_is_stage2_until_actual_supply_contract_offtake_inventory_margin_and_fcf_confirm",
        stage4b_status="policy relief watch",
        hard_4c_confirmed=False,
        evidence_fields=("critical_minerals_monitored_17", "china_hotline_and_joint_committee", "us_led_forge_bloc", "overseas_mining_support_250bn_krw"),
        red_flag_fields=("policy_relief_only", "china_restriction_recurrence", "us_china_conflict", "minerals_shortage", "sanction_risk"),
        price_data_source="Reuters critical-minerals policy anchor",
        reported_price_anchor="17 monitored minerals and 250B KRW overseas mining support",
        reported_return_anchor="Policy relief only; actual supply/offtake/margin not yet visible",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"critical_minerals_monitored": 17, "overseas_mining_support_krw_bn": 250.0, "overseas_mining_support_usd_mn": 172.0, "policy_tools": ["China hotline", "China joint committee", "U.S.-led FORGE bloc", "cooperation with Vietnam and Laos"], "forge_chair_period": "until June 2026"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_relief",
        rerating_result="policy_event_rerating",
        round_rerating_label="critical_minerals_supply_chain_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_not_green",
        price_validation_status="policy_anchor_not_full_ohlc",
        notes="정책은 좋은 Stage 2 relief지만 공급계약·offtake·재고·마진으로 닫혀야 한다.",
    ),
)


def round260_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND260_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND260_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round260 R4 Loop-12 materials/spread/strategic-resources price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if any(token in field for token in ("spread", "offtake", "margin", "fcf", "output", "shutdown", "supply", "contract"))
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if any(token in field for token in ("rumor", "policy", "headline", "relief", "dilution", "capex", "tariff"))
            ),
            stage4c_evidence=tuple(
                field
                for field in (*candidate.red_flag_fields, *candidate.evidence_fields)
                if any(token in field for token in ("restriction", "sanction", "tariff", "credit", "shutdown", "drawdown", "funding", "dilution", "oversupply", "risk"))
            ),
            must_have_fields=ROUND260_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND260_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_spreads_offtakes_or_fcf",
                "do_not_treat_mna_policy_strategic_material_capex_restructuring_or_tariff_as_green_alone",
                *ROUND260_GREEN_REQUIRED_FIELDS,
                *ROUND260_GREEN_FORBIDDEN_PATTERNS,
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
                    candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round260_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
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
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "mfe_1d": _float_text(candidate.mfe_1d),
            "mae_1d": _float_text(candidate.mae_1d),
            "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": candidate.score_price_alignment,
            "round_alignment_label": candidate.round_alignment_label,
            "rerating_result": candidate.rerating_result,
            "round_rerating_label": candidate.round_rerating_label,
            "stage_failure_type": candidate.stage_failure_type,
            "round_stage_failure_label": candidate.round_stage_failure_label,
            "price_validation_status": candidate.price_validation_status,
            "evidence_fields": "|".join(candidate.evidence_fields),
            "red_flag_fields": "|".join(candidate.red_flag_fields),
            "notes": candidate.notes,
        }
        for candidate in ROUND260_CASE_CANDIDATES
    )


def round260_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND260_SCORE_ADJUSTMENTS)


def round260_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND260_SHADOW_WEIGHT_ROWS)


def round260_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND260_DEEP_SUB_ARCHETYPES)


def round260_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round260_price_validation": "true"} for field in ROUND260_PRICE_VALIDATION_FIELDS)


def round260_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round260_label": label, "canonical_archetype": canonical} for label, canonical in ROUND260_REQUIRED_TARGET_ALIASES.items())


def round260_summary() -> dict[str, int | bool | str]:
    cases = ROUND260_CASE_CANDIDATES
    return {
        "source_round": ROUND260_SOURCE_ROUND_PATH,
        "round_id": ROUND260_ROUND_ID,
        "large_sector": ROUND260_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "watch_case_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None or "4C-watch" in case.stage4b_status),
        "policy_relief_not_green_count": sum(1 for case in cases if "policy" in case.round_alignment_label or "relief" in case.round_alignment_label),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND260_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND260_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND260_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round260_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND260_SOURCE_ROUND_PATH,
        "round_id": ROUND260_ROUND_ID,
        "large_sector": ROUND260_LARGE_SECTOR,
        "summary": round260_summary(),
        "target_aliases": dict(ROUND260_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND260_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND260_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND260_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND260_HARD_4C_GATES),
        "score_adjustments": list(round260_score_adjustment_rows()),
        "shadow_weights": list(round260_shadow_weight_rows()),
        "deep_sub_archetypes": list(round260_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND260_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round260_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_policy_mna_capex_or_strategic_material_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round260_summary_markdown() -> str:
    summary = round260_summary()
    lines = [
        "# Round 260 R4 Loop 12 Materials Spread Strategic Resources Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- watch_cases: {summary['watch_case_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND260_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.round_alignment_label,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Poongsan is defense-metals optionality, but M&A rumor is event premium, not Green.",
            "- Korea Zinc is strategic-minerals Stage 2 plus dilution/governance watch.",
            "- China rare-earth end-use pressure is a sector 4C-watch overlay.",
            "- Steel tariff is two-sided: domestic anti-dumping relief can be offset by U.S. export tariff risk.",
            "- Hyundai Steel U.S. plant is policy CAPEX false positive until demand, spread, margin and FCF confirm.",
            "- Petrochemical restructuring is relief; spread, OPM, FCF and debt cleanup are required before Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round260_green_gate_review_markdown() -> str:
    lines = [
        "# Round 260 R4 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R4 Stage 3-Green is not `strategic minerals`, `tariff`, `policy support`, `M&A rumor`, `U.S. CAPEX`, or `restructuring`. It requires spread, offtake, cost curve, working capital, FCF and risk clearance.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND260_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND260_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND260_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `M&A rumor` moves attention, but it is not business conversion.",
            "- `anti-dumping tariff relief` is Stage 2 only until steel spread and export margin confirm.",
            "- `capacity shutdown` is crisis relief unless OPM and FCF recover after restructuring.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round260_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 260 R4 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND260_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND260_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND260_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round260_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 260 R4 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, spreads, offtakes, MFE, MAE, margin, or FCF where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND260_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND260_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round260_r4_loop12_reports(
    output_directory: str | Path = ROUND260_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND260_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND260_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round260_case_records(), cases_path),
        "audit": _write_json(round260_audit_payload(), audit_path),
        "summary": output / "round260_r4_loop12_price_validation_summary.md",
        "case_matrix": output / "round260_r4_loop12_case_matrix.csv",
        "target_aliases": output / "round260_r4_loop12_target_aliases.csv",
        "score_adjustments": output / "round260_r4_loop12_score_adjustments.csv",
        "shadow_weights": output / "round260_r4_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round260_r4_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round260_r4_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round260_r4_loop12_green_gate_review.md",
        "price_validation_plan": output / "round260_r4_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round260_r4_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round260_summary_markdown(), encoding="utf-8")
    _write_csv(round260_case_rows(), paths["case_matrix"])
    _write_csv(round260_target_alias_rows(), paths["target_aliases"])
    _write_csv(round260_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round260_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round260_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round260_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round260_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round260_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round260_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"+{value}" if value > 0 else str(value)
