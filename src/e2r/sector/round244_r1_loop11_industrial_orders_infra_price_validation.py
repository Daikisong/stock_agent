"""Round-244 R1 Loop-11 industrial orders/infrastructure validation pack.

Round 244 converts ``docs/round/round_244.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a Czech nuclear signed contract is stronger than a preferred
bidder headline, but listed-company package, margin, delivery, and cash
collection are still required before Stage 3-Green. Likewise, an IPO first-day
double is 4B-watch if recurring MRO service economics are not yet proven.
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


ROUND244_SOURCE_ROUND_PATH = "docs/round/round_244.md"
ROUND244_ROUND_ID = "round_172"
ROUND244_LARGE_SECTOR = "INDUSTRIAL_ORDERS_INFRA"
ROUND244_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round244_r1_loop11_industrial_orders_infra_price_validation"
ROUND244_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop11_round244.jsonl"
ROUND244_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round244_r1_loop11_industrial_orders_infra_price_validation_audit.json"

ROUND244_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "NUCLEAR_EPC_EXPORT_ORDER": E2RArchetype.NUCLEAR_EPC_EXPORT_ORDER.value,
    "NUCLEAR_SMR_POLICY_MOU": E2RArchetype.NUCLEAR_SMR_POLICY_MOU.value,
    "POWER_GRID_CABLE_TRANSFORMER_EXPORT": E2RArchetype.POWER_GRID_CABLE_TRANSFORMER_EXPORT.value,
    "MARINE_MRO_RECURRING_SERVICE": E2RArchetype.MARINE_MRO_RECURRING_SERVICE.value,
    "SHIPBUILDING_US_POLICY_MASGA": E2RArchetype.SHIPBUILDING_US_POLICY_MASGA.value,
    "SHIPBUILDING_CONTRACT_CANCELLATION_4C": E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C.value,
    "DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH": E2RArchetype.DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH.value,
    "RAIL_EXPORT_ORDER_TO_DELIVERY": E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY.value,
    "GEOPOLITICAL_SHIPBUILDING_SANCTION": E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION.value,
    "CONTRACT_HEADLINE_NOT_STAGE3": E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3.value,
    "PRICE_ONLY_POLICY_RALLY": E2RArchetype.PRICE_ONLY_POLICY_RALLY.value,
}

ROUND244_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "signed_contract_or_firm_order",
    "contract_amount_customer_delivery_confirmed",
    "actual_delivery_or_revenue_recognition",
    "opm_eps_revision_confirmed",
    "working_capital_cash_collection_stable",
    "geopolitical_legal_sanction_risk_passed",
    "dilution_capital_allocation_risk_passed",
    "price_path_after_evidence",
)

ROUND244_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "preferred_bidder_only",
    "mou_without_funded_order",
    "policy_summit_headline_only",
    "ipo_first_day_surge_only",
    "record_high_policy_rally",
    "sanctioned_or_russia_customer_exposure",
    "contract_cancellation_risk_unpriced",
    "delivery_margin_cash_collection_unknown",
)

ROUND244_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "preferred_bidder_period_plus_40_to_50pct",
    "ipo_first_day_plus_40_to_100pct",
    "policy_masga_mou_record_high",
    "large_order_announcement_day_surge",
    "dilution_or_capital_raise_after_rerating",
    "us_shipbuilding_or_smr_theme_before_funded_order",
)

ROUND244_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "customer_unilateral_termination",
    "advance_payment_dispute",
    "sanctions_or_war_exposure",
    "arbitration_risk",
    "legal_injunction_blocking_contract",
    "geopolitical_sanction_transaction_ban",
    "capital_raise_regulator_revision_order",
    "delivery_delay",
    "cost_overrun",
    "cash_collection_failure",
)

ROUND244_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "mfe_30d",
    "mae_30d",
    "contract_value_anchor",
    "ipo_price_anchor",
    "target_price_anchor",
    "legal_or_sanction_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round244ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round244ShadowWeightRow:
    archetype: E2RArchetype
    signed_contract: int
    contract_amount: int
    order_to_revenue: int
    delivery_schedule: int
    backlog_margin: int
    cash_collection: int
    recurring_service: int
    geopolitical_risk: int
    event_penalty: int
    dilution_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "signed_contract": _signed(self.signed_contract),
            "contract_amount": _signed(self.contract_amount),
            "order_to_revenue": _signed(self.order_to_revenue),
            "delivery_schedule": _signed(self.delivery_schedule),
            "backlog_margin": _signed(self.backlog_margin),
            "cash_collection": _signed(self.cash_collection),
            "recurring_service": _signed(self.recurring_service),
            "geopolitical_risk": _signed(self.geopolitical_risk),
            "event_penalty": _signed(self.event_penalty),
            "dilution_redteam": _signed(self.dilution_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round244DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round244CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    source_sector: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
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
    peak_price_anchor: float | None
    peak_return_from_stage3_pct: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
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


ROUND244_SCORE_ADJUSTMENTS: tuple[Round244ScoreAdjustment, ...] = (
    Round244ScoreAdjustment("signed_contract", 5, "raise", "preferred bidder보다 signed contract가 강한 Stage 2 증거다."),
    Round244ScoreAdjustment("confirmed_contract_amount", 5, "raise", "계약금액과 고객이 확인되어야 한다."),
    Round244ScoreAdjustment("order_to_revenue_conversion", 5, "raise", "수주가 납품·매출로 내려와야 Stage 3 후보가 된다."),
    Round244ScoreAdjustment("delivery_schedule", 4, "raise", "납기와 인도 일정은 visibility를 높인다."),
    Round244ScoreAdjustment("backlog_margin_visibility", 5, "raise", "수주잔고가 마진과 EPS revision으로 이어져야 한다."),
    Round244ScoreAdjustment("cash_collection_quality", 5, "raise", "EPC·철도·방산은 현금회수와 working capital이 중요하다."),
    Round244ScoreAdjustment("recurring_MRO_service", 4, "raise", "MRO 반복서비스는 일회성 선박수주보다 질이 좋다."),
    Round244ScoreAdjustment("customer_quality", 4, "raise", "정부·유틸리티·국영 고객은 신뢰도를 높인다."),
    Round244ScoreAdjustment("geopolitical_risk_cleared", 4, "raise", "법적·지정학 리스크가 해소되어야 한다."),
    Round244ScoreAdjustment("preferred_bidder_only", -4, "lower", "preferred bidder만으로는 Green 금지다."),
    Round244ScoreAdjustment("MOU_without_funded_order", -5, "lower", "MOU는 funded order 전 Stage 2 watch다."),
    Round244ScoreAdjustment("policy_shipbuilding_headline", -5, "lower", "MASGA·정책 headline은 수주와 마진 전 event premium이다."),
    Round244ScoreAdjustment("IPO_premium_without_post_listing_FCF", -5, "lower", "IPO 첫날 프리미엄은 4B-watch다."),
    Round244ScoreAdjustment("contract_headline_without_execution", -5, "lower", "계약 headline보다 실행·납품·마진이 중요하다."),
    Round244ScoreAdjustment("geopolitical_customer_risk", -5, "lower", "Russia·제재 고객 노출은 RedTeam으로 강하게 깎는다."),
    Round244ScoreAdjustment("dilution_after_rerating", -5, "lower", "리레이팅 후 대형 증자·CB는 4B/dilution watch다."),
    Round244ScoreAdjustment("legal_delay_risk", -4, "lower", "계약 체결을 막는 법적 지연은 Stage 3를 차단한다."),
)


ROUND244_SHADOW_WEIGHT_ROWS: tuple[Round244ShadowWeightRow, ...] = (
    Round244ShadowWeightRow(E2RArchetype.NUCLEAR_EPC_EXPORT_ORDER, 5, 5, 4, 4, 5, 5, 0, 4, -2, 1, 5, 4, "Czech signed contract is Stage 2; listed-company package/margin/cashflow required."),
    Round244ShadowWeightRow(E2RArchetype.NUCLEAR_SMR_POLICY_MOU, 2, 2, 1, 1, 3, 3, 0, 3, -5, 1, 5, 3, "SMR/AI MOU is attention only until funded order."),
    Round244ShadowWeightRow(E2RArchetype.POWER_GRID_CABLE_TRANSFORMER_EXPORT, 5, 5, 4, 4, 5, 4, 0, 2, -2, 1, 4, 3, "LS contract and U.S. grid mix are good but event price failed."),
    Round244ShadowWeightRow(E2RArchetype.MARINE_MRO_RECURRING_SERVICE, 4, 3, 4, 3, 5, 5, 5, 2, -5, 2, 5, 3, "HD Hyundai Marine has recurring-service story but IPO premium is 4B."),
    Round244ShadowWeightRow(E2RArchetype.SHIPBUILDING_US_POLICY_MASGA, 3, 3, 2, 2, 4, 4, 0, 4, -5, 1, 5, 4, "MASGA/merger is Stage 2 and 4B until funded U.S. orders/margins confirm."),
    Round244ShadowWeightRow(E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1, 3, 5, "Samsung Heavy/Zvezda cancellation is hard 4C."),
    Round244ShadowWeightRow(E2RArchetype.DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH, 4, 4, 4, 4, 5, 4, 0, 3, -3, 5, 5, 4, "Hanwha Aerospace JV is Stage 2 but dilution after rerating is 4B-watch."),
    Round244ShadowWeightRow(E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY, 5, 5, 4, 5, 5, 5, 0, 3, -2, 1, 3, 4, "Hyundai Rotem rail order is Stage 2 until delivery/margin/cash collection confirm."),
    Round244ShadowWeightRow(E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1, 4, 5, "Hanwha Ocean China sanctions require 4C-watch."),
)


ROUND244_DEEP_SUB_ARCHETYPES: tuple[Round244DeepSubArchetype, ...] = (
    Round244DeepSubArchetype("원전 EPC", E2RArchetype.NUCLEAR_EPC_EXPORT_ORDER, ("KHNP", "Doosan Enerbility", "KEPCO E&C", "KEPCO KPS", "Czech Dukovany", "signed contract")),
    Round244DeepSubArchetype("SMR / AI power", E2RArchetype.NUCLEAR_SMR_POLICY_MOU, ("Doosan Enerbility", "X-energy", "AWS", "Fermi America", "funded order required")),
    Round244DeepSubArchetype("전력망·케이블", E2RArchetype.POWER_GRID_CABLE_TRANSFORMER_EXPORT, ("LS Electric", "LS Corp", "Elia Asset", "data-center grid demand", "price failed")),
    Round244DeepSubArchetype("조선 MRO", E2RArchetype.MARINE_MRO_RECURRING_SERVICE, ("HD Hyundai Marine Solution", "maintenance", "repair", "retrofit", "IPO 4B")),
    Round244DeepSubArchetype("조선정책 MASGA", E2RArchetype.SHIPBUILDING_US_POLICY_MASGA, ("HD Hyundai Heavy", "HD Hyundai Mipo", "MASGA", "US shipbuilding", "record high")),
    Round244DeepSubArchetype("계약취소", E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C, ("Samsung Heavy", "Zvezda", "Russia sanctions", "contract cancellation", "arbitration")),
    Round244DeepSubArchetype("방산 현지생산", E2RArchetype.DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH, ("Hanwha Aerospace", "Poland missile JV", "CGR-080", "capital raise", "dilution")),
    Round244DeepSubArchetype("철도 수출", E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY, ("Hyundai Rotem", "Morocco ONCF", "110 trains", "delivery margin cash collection")),
    Round244DeepSubArchetype("지정학 제재", E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION, ("Hanwha Ocean", "China sanctions", "US-linked subsidiaries", "4C-watch")),
)


ROUND244_CASE_CANDIDATES: tuple[Round244CaseCandidate, ...] = (
    Round244CaseCandidate(
        case_id="r1_loop11_czech_nuclear_doosan_kepco_stage2",
        symbol="034020/052690/051600/015760",
        company_name="Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO",
        source_sector="R1",
        primary_archetype=E2RArchetype.NUCLEAR_EPC_EXPORT_ORDER,
        secondary_archetypes=(E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER, E2RArchetype.NUCLEAR_EXPORT_LEGAL_GATE, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="success_candidate",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2025, 6, 4),
        stage3_date=None,
        stage4b_date=date(2024, 7, 17),
        stage4c_date=date(2025, 5, 6),
        stage3_decision="signed_czech_nuclear_contract_is_strong_stage2_but_listed_company_package_margin_and_cash_collection_required_before_green",
        stage4b_status="4B-watch/legal-watch",
        hard_4c_confirmed=False,
        evidence_fields=("khpn_czech_preferred_bidder", "czech_contract_signed", "contract_value_18_7bn_usd", "two_dukrowany_reactors", "trial_operation_2036_2038"),
        red_flag_fields=("preferred_bidder_rally_before_scope", "edf_legal_challenge", "listed_company_package_unconfirmed", "margin_cash_collection_unknown"),
        price_data_source="Reuters / AP nuclear-contract and sector-return anchors",
        reported_price_anchor="Doosan +48%, KEPCO E&C +41%, KEPCO Plant S&E +14% in three-month preferred-bidder period",
        reported_return_anchor="Signed Czech contract 407B koruna / $18.7B for two reactors",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"doosan_3m_mfe_pct": 48.0, "kepco_ec_3m_mfe_pct": 41.0, "kepco_plant_se_3m_mfe_pct": 14.0, "czech_contract_value_koruna_bn": 407.0, "czech_contract_value_usd_bn": 18.7, "reactor_count": 2.0, "unit_cost_context_koruna_bn": 200.0, "unit_cost_context_usd_bn": 9.1, "first_trial_operation_year": 2036.0, "second_trial_operation_year": 2038.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4b_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="nuclear_EPC_export_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="reported_sector_return_not_full_ohlc",
        notes="Preferred bidder에서 signed contract로 올라온 강한 Stage 2지만 상장사별 package, margin, cash collection 전 Green은 금지다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_doosan_smr_ai_power_mou",
        symbol="034020",
        company_name="Doosan Enerbility / SMR-AI power cooperation",
        source_sector="R1",
        primary_archetype=E2RArchetype.NUCLEAR_SMR_POLICY_MOU,
        secondary_archetypes=(E2RArchetype.SMR_AI_POWER_POLICY_EVENT, E2RArchetype.PRICE_ONLY_POLICY_RALLY, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="success_candidate",
        stage1_date=date(2025, 8, 26),
        stage2_date=date(2025, 8, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="smr_ai_power_mou_is_stage2_attention_not_green_before_funded_order_equipment_package_margin_and_cash_collection",
        stage4b_status="4B-watch-if-MOU-rally",
        hard_4c_confirmed=False,
        evidence_fields=("x_energy_aws_smr_cooperation", "fermi_america_texas_ai_project_agreement", "khnp_samsung_ct_link", "south_korean_firms_150bn_us_investment_context"),
        red_flag_fields=("mou_without_funded_order", "confirmed_revenue_false", "equipment_package_unconfirmed", "permitting_financing_risk"),
        price_data_source="Reuters U.S. investment / SMR policy-MOU anchor",
        reported_price_anchor="Doosan stock OHLC unavailable after deep search",
        reported_return_anchor="X-energy/AWS/Fermi cooperation; funded order not confirmed",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"south_korean_firms_us_investment_pledge_usd_bn": 150.0, "confirmed_revenue": False, "funded_order_confirmed": False, "partners": "X-energy|Amazon Web Services|Fermi America|KHNP|Samsung C&T"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="SMR_AI_power_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="MOU_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="SMR/AI power 협력은 좋은 Stage 2 후보지만 funded order 전에는 Green이 아니다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_ls_grid_cable_transformer_price_failed",
        symbol="010120/006260",
        company_name="LS Electric / LS Corp",
        source_sector="R1",
        primary_archetype=E2RArchetype.POWER_GRID_CABLE_TRANSFORMER_EXPORT,
        secondary_archetypes=(E2RArchetype.GRID_POWER_EQUIPMENT_AI_DATACENTER, E2RArchetype.TRANSFORMER_CAPACITY_BOTTLENECK, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="grid_cable_contract_and_us_mix_are_stage2_but_event_day_price_failed_and_delivery_margin_fcf_unverified",
        stage4b_status="4B-watch-if-theme-multiple-prepays-delivery",
        hard_4c_confirmed=False,
        evidence_fields=("ls_power_cable_contract_282_13bn_krw", "elia_asset_belgium_customer", "ls_electric_target_raise_86_7pct", "us_revenue_share_expected_20pct"),
        red_flag_fields=("event_day_price_failed_minus_5_4pct", "delivery_margin_fcf_unverified", "copper_steel_cost_risk", "transformer_cycle_normalization"),
        price_data_source="MarketWatch contract / target / price anchors",
        reported_price_anchor="LS Electric 208,500 KRW with -5.4% event-day move",
        reported_return_anchor="Target 150,000 -> 280,000 KRW; LS cable contract 282.13B KRW",
        mfe_1d=None,
        mae_1d=-5.4,
        stage2_price_anchor=208500.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"ls_power_cable_contract_krw_bn": 282.13, "ls_electric_stage2_price_anchor_krw": 208500.0, "target_price_krw": 280000.0, "target_raise_pct": 86.7, "target_upside_from_stage2_price_pct": 34.3, "us_revenue_share_2022_max_pct": 5.0, "us_revenue_share_expected_2024_pct": 20.0, "minimum_mix_increase_pct": 300.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="unknown",
        round_rerating_label="grid_cable_transformer_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_not_green",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="계약과 U.S. mix 증거는 좋지만 가격경로가 즉시 실패했다. 납품·마진·FCF 전 Green은 보류다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_hd_hyundai_marine_solution_ipo_4b",
        symbol="443060",
        company_name="HD Hyundai Marine Solution",
        source_sector="R1",
        primary_archetype=E2RArchetype.MARINE_MRO_RECURRING_SERVICE,
        secondary_archetypes=(E2RArchetype.SHIP_MRO_RECURRING_PLATFORM, E2RArchetype.IPO_EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_POLICY_RALLY),
        case_type="success_candidate",
        stage1_date=date(2024, 5, 1),
        stage2_date=date(2024, 5, 8),
        stage3_date=None,
        stage4b_date=date(2024, 5, 8),
        stage4c_date=None,
        stage3_decision="marine_mro_recurring_service_candidate_but_ipo_debut_96_5pct_is_4b_before_post_listing_fcf_and_margin",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("marine_after_sales_mro_retrofit", "eco_friendly_vessel_servicing", "earnings_2023_151_1bn_krw", "earnings_growth_44pct"),
        red_flag_fields=("ipo_first_day_surge_only", "post_listing_fcf_unverified", "kkr_overhang", "valuation_compression_risk"),
        price_data_source="Reuters Breakingviews / WSJ IPO price anchors",
        reported_price_anchor="IPO 83,400 KRW; open 119,900 KRW; first-day close 163,900 KRW",
        reported_return_anchor="Opening +43.8%; first-day close +96.5%; IPO raised 742B KRW",
        mfe_1d=96.5,
        mae_1d=None,
        stage2_price_anchor=83400.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=163900.0,
        stage4c_price_anchor=None,
        peak_price_anchor=163900.0,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"ipo_price_krw": 83400.0, "opening_price_krw": 119900.0, "opening_mfe_pct": 43.8, "first_day_close_krw": 163900.0, "first_day_close_mfe_pct": 96.5, "ipo_raise_krw_bn": 742.0, "market_cap_close_context_krw_trn": 7.29, "earnings_2023_krw_bn": 151.1, "earnings_growth_pct": 44.0, "parent_hd_hyundai_stake_pct": 55.8, "kkr_vehicle_stake_pct": 24.2},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_4b_watch",
        rerating_result="event_premium",
        round_rerating_label="marine_MRO_recurring_service_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="IPO_event_not_green",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="MRO 반복서비스 스토리는 좋지만 IPO debut +96.5%는 실적검증 전 4B다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_hd_hyundai_heavy_mipo_masga_merger",
        symbol="329180/010620",
        company_name="HD Hyundai Heavy / HD Hyundai Mipo",
        source_sector="R1",
        primary_archetype=E2RArchetype.SHIPBUILDING_US_POLICY_MASGA,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_US_PLATFORM_RESTRUCTURING, E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_POLICY_RALLY),
        case_type="success_candidate",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2025, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        stage3_decision="masga_merger_policy_event_is_stage2_and_4b_watch_until_funded_us_order_yard_utilization_margin_and_fcf_confirm",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("masga_us_shipbuilding_cooperation", "hd_hyundai_heavy_mipo_merger", "share_exchange_ratio", "us_icebreaker_demand_context"),
        red_flag_fields=("record_high_policy_rally", "funded_us_order_missing", "margin_unknown", "integration_cost_risk"),
        price_data_source="Reuters merger / event-return anchor",
        reported_price_anchor="Both names reached record highs; Mipo exchange ratio 1.04059146 Heavy shares",
        reported_return_anchor="HD Hyundai Heavy +11.3%; HD Hyundai Mipo +14.6%",
        mfe_1d=14.6,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"hd_hyundai_heavy_event_mfe_1d_pct": 11.3, "hd_hyundai_mipo_event_mfe_1d_pct": 14.6, "record_high_status": True, "share_exchange_ratio_mipo_per_heavy": 1.04059146, "us_coast_guard_icebreaker_allocation_usd_bn": 8.6},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="U.S._shipbuilding_policy_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_4B",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="MASGA/합병은 Stage 2와 4B-watch다. funded U.S. order와 margin 전에는 Stage 3가 아니다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_samsung_heavy_zvezda_contract_cancellation",
        symbol="010140",
        company_name="Samsung Heavy Industries",
        source_sector="R1",
        primary_archetype=E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C,
        secondary_archetypes=(E2RArchetype.CONTRACT_QUALITY_BREAK, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        stage1_date=date(2020, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 6, 18),
        stage3_decision="zvezda_contract_cancellation_is_hard_4c_and_russia_sanctioned_customer_backlog_should_be_redteam_before_green",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("zvezda_icebreaker_lng_and_shuttle_tanker_orders", "cancelled_contract_value_4_85tn_krw", "cancelled_contract_value_3_54bn_usd"),
        red_flag_fields=("contract_cancellation", "customer_unilateral_termination", "advance_payment_dispute", "sanctions_or_war_exposure", "singapore_arbitration"),
        price_data_source="Reuters contract-cancellation anchor",
        reported_price_anchor="Stock OHLC unavailable beyond reported contract-cancellation anchor",
        reported_return_anchor="Two Zvezda orders worth 4.85T KRW / $3.54B cancelled",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"cancelled_contract_value_krw_trn": 4.85, "cancelled_contract_value_usd_bn": 3.54, "icebreaker_lng_carriers": 10.0, "icebreaker_shuttle_tankers": 7.0, "contract_origin_start_year": 2020.0, "contract_origin_end_year": 2021.0, "arbitration": "Singapore arbitration requested"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="shipbuilding_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="Zvezda 취소는 hard 4C다. 러시아·제재 고객 수주잔고는 Green 전 RedTeam으로 강하게 걸러야 한다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_hanwha_aerospace_poland_jv_dilution_watch",
        symbol="012450",
        company_name="Hanwha Aerospace",
        source_sector="R1",
        primary_archetype=E2RArchetype.DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH,
        secondary_archetypes=(E2RArchetype.DEFENSE_LOCAL_PRODUCTION_PLATFORM, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY, E2RArchetype.DEFENSE_CAPITAL_ALLOCATION_SHOCK),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 4, 15),
        stage3_date=None,
        stage4b_date=date(2025, 3, 21),
        stage4c_date=None,
        stage3_decision="poland_missile_jv_is_stage2_but_actual_order_volume_delivery_margin_cash_collection_and_local_economics_required",
        stage4b_status="4B-watch/dilution",
        hard_4c_confirmed=False,
        evidence_fields=("poland_wb_electronics_missile_jv", "cgr_080_guided_missiles", "k239_chunmoo", "technology_transfer_local_production"),
        red_flag_fields=("capital_raise_3_6tn_krw", "capital_raise_event_mae_minus_13pct", "dilution_after_rerating", "local_production_margin_unclear"),
        price_data_source="Reuters missile-JV / capital-raising anchors",
        reported_price_anchor="Affiliate issue price 758,000 KRW/share; capital raise event price path -13%",
        reported_return_anchor="3.6T KRW capital raise shock; revised 2.3T rights offering plus 1.3T affiliate issue",
        mfe_1d=None,
        mae_1d=-13.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"capital_raise_initial_krw_trn": 3.6, "capital_raise_initial_usd_bn": 2.46, "capital_raise_event_mae_pct": -13.0, "revised_rights_offering_krw_trn": 2.3, "affiliate_share_issue_krw_trn": 1.3, "total_revised_related_raise_krw_trn": 3.6, "affiliate_issue_price_krw": 758000.0, "guidance_2025_revenue_krw_trn": 30.0, "guidance_2025_op_krw_trn": 3.0, "revenue_2024_krw_trn": 11.24, "op_2024_krw_trn": 1.73, "op_growth_vs_2024_guidance_pct": 73.4},
        score_price_alignment="aligned",
        round_alignment_label="success_candidate_aligned_4B_detection",
        rerating_result="unknown",
        round_rerating_label="defense_localization_watch_with_dilution",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="4B_watch_not_hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Poland missile JV는 Stage 2지만 대형 증자 shock 때문에 dilution 4B-watch가 필수다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_hyundai_rotem_morocco_rail_order",
        symbol="064350",
        company_name="Hyundai Rotem",
        source_sector="R1",
        primary_archetype=E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY,
        secondary_archetypes=(E2RArchetype.RAIL_INFRASTRUCTURE, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 2, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="morocco_rail_order_is_strong_stage2_but_delivery_margin_working_capital_and_cash_collection_required_before_green",
        stage4b_status="4B-watch-if-rail-export-headline-rallies",
        hard_4c_confirmed=False,
        evidence_fields=("morocco_oncf_order", "110_urban_trains", "order_value_2_2tn_krw", "order_value_1_54bn_usd", "largest_railway_business_order"),
        red_flag_fields=("delivery_margin_unknown", "working_capital_unknown", "concessionary_financing_delay", "fx_margin_deterioration"),
        price_data_source="Reuters rail-contract evidence",
        reported_price_anchor="Hyundai Rotem stock OHLC unavailable after deep search",
        reported_return_anchor="Morocco ONCF 110 urban trains, 2.2T KRW / $1.54B order",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"morocco_total_train_purchase": 168.0, "morocco_total_program_value_usd_bn": 2.9, "hyundai_rotem_order_krw_trn": 2.2, "hyundai_rotem_order_usd_bn": 1.54, "hyundai_train_count": 110.0, "hyundai_order_share_of_total_program_pct": 53.1, "alstom_high_speed_trains": 18.0, "caf_intercity_trains": 40.0, "network_target_cities": 43.0, "network_target_population_coverage_pct": 87.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="rail_export_order_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Morocco rail order는 강한 Stage 2다. 납품·마진·working capital 전 Stage 3는 보류다.",
    ),
    Round244CaseCandidate(
        case_id="r1_loop11_hanwha_ocean_china_sanction_watch",
        symbol="042660",
        company_name="Hanwha Ocean",
        source_sector="R1",
        primary_archetype=E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY, E2RArchetype.DEFENSE_US_SHIPBUILDING_PLATFORM),
        case_type="failed_rerating",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 10, 14),
        stage3_decision="us_shipbuilding_policy_exposure_is_not_green_when_china_sanction_transaction_ban_watch_is_present",
        stage4b_status="4C-watch-not-hard-4C",
        hard_4c_confirmed=False,
        evidence_fields=("philly_shipyard_acquisition", "us_shipbuilding_rebuild_exposure", "us_investment_plan_5bn_usd", "china_sanctions_five_us_linked_subsidiaries"),
        red_flag_fields=("geopolitical_sanction_transaction_ban", "transactions_cooperation_ban", "event_close_mae_minus_5_8pct", "actual_revenue_module_contract_disruption_unconfirmed"),
        price_data_source="Reuters / AP sanction and price anchors",
        reported_price_anchor="Hanwha Ocean close -5.8%; intraday down as much as -8%; HD Hyundai Heavy -4.1%",
        reported_return_anchor="China sanctioned five U.S.-linked subsidiaries; U.S. investment plan $5B",
        mfe_1d=None,
        mae_1d=-5.8,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"hanwha_ocean_close_mae_pct": -5.8, "hd_hyundai_heavy_same_context_pct": -4.1, "ft_intraday_context_pct": -8.0, "sanctioned_entities": 5.0, "philly_shipyard_acquisition_usd_mn": 100.0, "announced_us_investment_usd_bn": 5.0, "investment_vs_acquisition_multiple": 50.0, "hard_4c_confirmed": False},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="geopolitical_sanction_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="U.S. shipbuilding exposure가 좋아도 China sanctions는 4C-watch다. 실제 매출·부품·계약 차질 확인 시 hard 4C다.",
    ),
)


def round244_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("delivery", "revenue", "opm", "eps", "fcf", "margin", "cash", "working_capital", "package")
    for candidate in ROUND244_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND244_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round244 R1 Loop-11 industrial orders/infrastructure price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "ipo" in field.lower()
                or "rally" in field.lower()
                or "record" in field.lower()
                or "dilution" in field.lower()
                or "policy" in field.lower()
                or "mou" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "cancellation" in field.lower()
                or "termination" in field.lower()
                or "sanction" in field.lower()
                or "legal" in field.lower()
                or "arbitration" in field.lower()
                or "dispute" in field.lower()
                or "delay" in field.lower()
                or "risk" in field.lower()
            ),
            must_have_fields=ROUND244_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND244_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_orders_policy_mou_ipo_or_merger_as_green_alone",
                *ROUND244_GREEN_REQUIRED_FIELDS,
                *ROUND244_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                peak_return_from_stage3=candidate.peak_return_from_stage3_pct,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.mfe_1d is not None
                or candidate.mae_1d is not None,
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round244_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND244_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": candidate.source_sector,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
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
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
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
        )
    return tuple(rows)


def round244_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND244_SCORE_ADJUSTMENTS)


def round244_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND244_SHADOW_WEIGHT_ROWS)


def round244_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND244_DEEP_SUB_ARCHETYPES)


def round244_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round244_price_validation": "true"} for field in ROUND244_PRICE_VALIDATION_FIELDS)


def round244_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round244_label": label, "canonical_archetype": canonical} for label, canonical in ROUND244_REQUIRED_TARGET_ALIASES.items())


def round244_summary() -> dict[str, int | bool | str]:
    cases = ROUND244_CASE_CANDIDATES
    return {
        "source_round": ROUND244_SOURCE_ROUND_PATH,
        "round_id": ROUND244_ROUND_ID,
        "large_sector": ROUND244_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND244_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND244_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND244_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round244_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND244_SOURCE_ROUND_PATH,
        "round_id": ROUND244_ROUND_ID,
        "large_sector": ROUND244_LARGE_SECTOR,
        "summary": round244_summary(),
        "target_aliases": dict(ROUND244_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND244_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND244_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND244_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND244_HARD_4C_GATES),
        "deep_sub_archetypes": round244_deep_sub_archetype_rows(),
        "shadow_weights": round244_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round244_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_orders_policy_mou_ipo_or_merger_as_green_alone",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round244_summary_markdown() -> str:
    summary = round244_summary()
    lines = [
        "# Round 244 R1 Loop 11 Industrial Orders / Infrastructure Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        f"- target_archetype_count: {summary['target_archetype_count']}",
        f"- deep_sub_archetype_count: {summary['deep_sub_archetype_count']}",
        f"- shadow_weight_row_count: {summary['shadow_weight_row_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND244_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
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
            "- R1 Stage 3 is not an order headline. It needs delivery, revenue, margin, EPS revision, cash collection, and post-evidence price path.",
            "- Czech nuclear is strong Stage 2 after the signed contract, but listed-company scope and margin are still required.",
            "- SMR/AI power, MASGA, IPO, and merger events are Stage 2/4B-watch until funded orders and economics confirm.",
            "- Samsung Heavy/Zvezda is a hard 4C contract-cancellation anchor.",
            "- Hanwha Ocean sanctions are 4C-watch, not hard 4C until actual revenue, module, or contract disruption appears.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round244_green_gate_review_markdown() -> str:
    lines = [
        "# Round 244 R1 Loop 11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND244_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND244_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `signed contract` is Stage 2; `listed supplier package + margin + cash collection` is what can support Stage 3.",
            "- `MOU / MASGA / IPO / merger price spike` is 4B-watch when revenue economics are missing.",
            "- `contract cancellation`, `legal block`, and `sanction transaction ban` are RedTeam gates.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round244_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 244 R1 Loop 11 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND244_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND244_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B means price or event premium has run ahead of delivery/margin/cash evidence.",
            "- 4C means the original order or policy thesis is damaged by cancellation, legal block, sanction, funding, or execution failure.",
            "- 4C-watch is not hard 4C until actual revenue, module, contract, or cash disruption is confirmed.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND244_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round244_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 244 R1 Loop 11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND244_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round244_r1_loop11_reports(
    output_directory: str | Path = ROUND244_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND244_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND244_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round244_case_records(), cases_path),
        "audit": _write_json(round244_audit_payload(), audit_path),
        "summary": output / "round244_r1_loop11_price_validation_summary.md",
        "case_matrix": output / "round244_r1_loop11_case_matrix.csv",
        "target_aliases": output / "round244_r1_loop11_target_aliases.csv",
        "score_adjustments": output / "round244_r1_loop11_score_adjustments.csv",
        "shadow_weights": output / "round244_r1_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round244_r1_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round244_r1_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round244_r1_loop11_green_gate_review.md",
        "price_validation_plan": output / "round244_r1_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round244_r1_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round244_summary_markdown(), encoding="utf-8")
    _write_csv(round244_case_rows(), paths["case_matrix"])
    _write_csv(round244_target_alias_rows(), paths["target_aliases"])
    _write_csv(round244_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round244_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round244_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round244_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round244_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round244_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round244_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"{value:+d}" if isinstance(value, int) else str(value)
