"""Round-295 R13 Loop-14 cross-archetype RedTeam validation pack.

This module converts ``docs/round/round_295.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: a 2.9B USD signed contract is not Stage 3-Green if the actual
call-off later collapses to almost zero. The Green gate must check shipped
volume, revenue recognition, margin, cash collection, and customer demand.
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


ROUND295_SOURCE_ROUND_PATH = "docs/round/round_295.md"
ROUND295_ANALYST_ROUND_ID = "round_223"
ROUND295_LARGE_SECTOR = "CROSS_ARCHETYPE_REDTEAM_4B_ACCOUNTING_TRUST_PRICE_VALIDATION"
ROUND295_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round295_r13_loop14_cross_archetype_redteam_price_validation"
ROUND295_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r13_loop14_round295.jsonl"
ROUND295_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round295_r13_loop14_cross_archetype_redteam_price_validation_audit.json"

ROUND295_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DEFENSE_BACKLOG_DILUTION_4B": E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B.value,
    "SIGNED_CONTRACT_COLLAPSE_HARD_4C": E2RArchetype.SIGNED_CONTRACT_COLLAPSE_HARD_4C.value,
    "RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE": E2RArchetype.RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE.value,
    "AI_CLOUD_IPO_FALSE_POSITIVE": E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE.value,
    "VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE": E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE.value,
    "DATA_TRUST_HARD_4C": E2RArchetype.DATA_TRUST_HARD_4C.value,
    "LOCALIZATION_CAPEX_FALSE_POSITIVE": E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE.value,
    "CONTROL_PREMIUM_4B_GOVERNANCE_WATCH": E2RArchetype.CONTROL_PREMIUM_4B_GOVERNANCE_WATCH.value,
}

ROUND295_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_calloff_vs_signed_contract",
    "actual_calloff_revenue_recognition_confirmed",
    "dilution_adjusted_EPS",
    "capital_raise_disclosure_quality",
    "capex_IRR_and_funding_clarity",
    "aftermarket_price_validation",
    "data_trust_internal_control",
    "contingent_liability_risk",
    "governance_execution_not_proposal",
    "control_premium_separation",
    "resource_economic_viability",
    "price_path_after_evidence",
)

ROUND295_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "headline_order_backlog_only",
    "large_customer_name_only",
    "policy_or_presidential_announcement_only",
    "IPO_oversubscription_only",
    "activist_or_valueup_proposal_only",
    "control_premium_as_operating_green",
    "capex_localization_headline_only",
    "resource_estimate_without_drilling",
    "data_breach_treated_as_oneoff",
)

ROUND295_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "6_to_12m_double_plus_before_large_capital_raise_or_CB",
    "order_backlog_defense_AI_resource_headline_before_PER_rerating",
    "IPO_oversubscription_high_but_debut_below_IPO",
    "control_premium_15_to_30pct_without_operating_cashflow",
    "government_or_presidential_announcement_20_to_30pct_without_proof",
    "capex_localization_headline_without_funding_IRR_customer_demand",
    "activist_proposal_without_board_adoption",
)

ROUND295_HARD_4C_GATES: tuple[str, ...] = (
    "signed_contract_value_collapse",
    "data_breach_or_trust_failure_with_compensation_capex_revenue_forecast_impact",
    "fatal_safety_or_service_trust_event",
    "financing_plan_blocked_or_revised_due_disclosure_quality",
    "capex_debt_or_dilution_without_IRR_clarity",
    "governance_proposal_fails_after_valueup_rerating",
    "resource_drilling_fails_after_speculative_rally",
    "customer_calloff_or_model_cancellation_destroys_expected_revenue",
)

ROUND295_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "contract_value_collapse_anchor",
    "share_sale_dilution_anchor",
    "resource_economic_viability_anchor",
    "IPO_aftermarket_anchor",
    "valueup_execution_anchor",
    "data_trust_liability_anchor",
    "localization_capex_IRR_anchor",
    "control_premium_separation_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round295ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round295ShadowWeightRow:
    archetype: E2RArchetype
    actual_calloff_vs_signed_contract: int
    dilution_adjusted_eps: int
    capital_raise_disclosure_quality: int
    capex_irr_funding_clarity: int
    aftermarket_price_validation: int
    data_trust_internal_control: int
    contingent_liability_risk: int
    governance_execution_not_proposal: int
    control_premium_separation: int
    resource_economic_viability: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_calloff_vs_signed_contract": _signed(self.actual_calloff_vs_signed_contract),
            "dilution_adjusted_eps": _signed(self.dilution_adjusted_eps),
            "capital_raise_disclosure_quality": _signed(self.capital_raise_disclosure_quality),
            "capex_irr_funding_clarity": _signed(self.capex_irr_funding_clarity),
            "aftermarket_price_validation": _signed(self.aftermarket_price_validation),
            "data_trust_internal_control": _signed(self.data_trust_internal_control),
            "contingent_liability_risk": _signed(self.contingent_liability_risk),
            "governance_execution_not_proposal": _signed(self.governance_execution_not_proposal),
            "control_premium_separation": _signed(self.control_premium_separation),
            "resource_economic_viability": _signed(self.resource_economic_viability),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round295DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round295CaseCandidate:
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
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
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


ROUND295_SCORE_ADJUSTMENTS: tuple[Round295ScoreAdjustment, ...] = (
    Round295ScoreAdjustment("actual_calloff_vs_signed_contract", 5, "raise", "계약 headline은 매출이 아니다. 실제 call-off와 매출 인식이 필요하다."),
    Round295ScoreAdjustment("dilution_adjusted_EPS", 5, "raise", "수주가 좋아도 증자·CB가 EPS를 희석하면 Green이 아니다."),
    Round295ScoreAdjustment("capital_raise_disclosure_quality", 5, "raise", "대규모 자금조달은 사용처와 투자자 의사결정 정보가 충분해야 한다."),
    Round295ScoreAdjustment("capex_IRR_and_funding_clarity", 5, "raise", "현지화 CAPEX는 IRR, funding, customer demand가 닫혀야 한다."),
    Round295ScoreAdjustment("aftermarket_price_validation", 5, "raise", "IPO 청약경쟁률보다 상장 후 가격과 첫 실적이 더 강한 검증이다."),
    Round295ScoreAdjustment("data_trust_internal_control", 5, "raise", "데이터 신뢰 훼손은 보상, 보안투자, 매출전망, 우발부채로 이어진다."),
    Round295ScoreAdjustment("contingent_liability_risk", 5, "raise", "보상·소송·규제 리스크는 일회성 비용으로 단정하면 안 된다."),
    Round295ScoreAdjustment("governance_execution_not_proposal", 5, "raise", "Value-Up 제안은 실행 전까지 현금흐름 증거가 아니다."),
    Round295ScoreAdjustment("control_premium_separation", 4, "raise", "지배권 premium은 영업현금흐름 리레이팅과 분리한다."),
    Round295ScoreAdjustment("resource_economic_viability", 5, "raise", "자원 estimate는 시추·경제성·IRR 전까지 Green 증거가 아니다."),
    Round295ScoreAdjustment("headline_only_event", -5, "lower", "좋은 headline 하나로 Stage 3-Green을 만들지 않는다."),
)


ROUND295_SHADOW_WEIGHT_ROWS: tuple[Round295ShadowWeightRow, ...] = (
    Round295ShadowWeightRow(E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B, 2, 5, 5, 4, 2, 1, 3, 3, 2, 1, 0, 5, 4, "Hanwha shows backlog premium must be corrected for dilution and disclosure quality."),
    Round295ShadowWeightRow(E2RArchetype.SIGNED_CONTRACT_COLLAPSE_HARD_4C, 5, 2, 2, 2, 1, 1, 3, 2, 1, 1, 0, 4, 5, "L&F/Tesla proves signed amount is not Green without actual call-off."),
    Round295ShadowWeightRow(E2RArchetype.RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE, 1, 1, 2, 3, 1, 0, 2, 1, 0, 5, -5, 5, 4, "Blue Whale shows resource estimate requires drilling and economic viability."),
    Round295ShadowWeightRow(E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE, 1, 2, 2, 2, 5, 2, 1, 2, 0, 0, -5, 5, 3, "LG CNS shows AI/cloud mix and oversubscription need aftermarket validation."),
    Round295ShadowWeightRow(E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE, 1, 3, 3, 1, 2, 1, 1, 5, 2, 0, 0, 5, 4, "Samsung C&T shows shareholder-return proposal is not execution."),
    Round295ShadowWeightRow(E2RArchetype.DATA_TRUST_HARD_4C, 1, 2, 3, 3, 2, 5, 5, 3, 0, 0, 0, 4, 5, "SK Telecom confirms data trust breach can alter revenue, capex and liabilities."),
    Round295ShadowWeightRow(E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE, 1, 4, 4, 5, 2, 1, 3, 2, 0, 0, 0, 5, 4, "Hyundai Steel shows localization capex needs funding clarity and IRR."),
    Round295ShadowWeightRow(E2RArchetype.CONTROL_PREMIUM_4B_GOVERNANCE_WATCH, 1, 2, 3, 2, 2, 1, 3, 4, 5, 1, -4, 5, 3, "Korea Zinc shows control premium must be separated from operating Green."),
)


ROUND295_DEEP_SUB_ARCHETYPES: tuple[Round295DeepSubArchetype, ...] = (
    Round295DeepSubArchetype("방산 backlog 희석", E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B, ("Hanwha Aerospace", "3.6T KRW share sale", "FSS filing revision", "dilution-adjusted EPS")),
    Round295DeepSubArchetype("signed contract call-off", E2RArchetype.SIGNED_CONTRACT_COLLAPSE_HARD_4C, ("L&F", "Tesla", "$2.9B to $7,386", "4680 ramp")),
    Round295DeepSubArchetype("자원개발 event premium", E2RArchetype.RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE, ("Korea Gas", "Blue Whale", "14B barrels", "20% success probability")),
    Round295DeepSubArchetype("AI/cloud IPO quality gate", E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE, ("LG CNS", "IPO 61,900 KRW", "59,700 KRW debut", "123x oversubscription")),
    Round295DeepSubArchetype("Value-Up proposal vs execution", E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE, ("Samsung C&T", "activist proposal failed", "NPS sided with management", "dividend buyback proposal")),
    Round295DeepSubArchetype("data trust hard 4C", E2RArchetype.DATA_TRUST_HARD_4C, ("SK Telecom", "USIM leak", "26.96M data pieces", "800B KRW revenue forecast cut")),
    Round295DeepSubArchetype("localization capex IRR", E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE, ("Hyundai Steel", "$6B US plant", "funding unclear", "IRR unconfirmed")),
    Round295DeepSubArchetype("control premium separation", E2RArchetype.CONTROL_PREMIUM_4B_GOVERNANCE_WATCH, ("Korea Zinc", "Young Poong", "MBK tender", "operating cashflow unconfirmed")),
)


ROUND295_CASE_CANDIDATES: tuple[Round295CaseCandidate, ...] = (
    Round295CaseCandidate(
        case_id="r13_loop14_hanwha_aerospace_backlog_dilution_4b",
        symbol="012450",
        company_name="Hanwha Aerospace",
        primary_archetype=E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B,
        secondary_archetypes=(E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.THEME_VALUATION_OVERHEAT),
        case_type="4b_watch",
        round_case_type="overheat / false_positive_score / 4B-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 3, 21),
        stage4c_date=date(2025, 3, 27),
        stage3_decision="defense backlog is not Green until dilution-adjusted EPS, delivery margin, funding and disclosure quality close",
        stage4b_status="4B-watch/backlog-dilution-reset",
        hard_4c_confirmed=False,
        evidence_fields=("defense_order_backlog", "share_sale_3_6T_KRW", "offer_price_605000_KRW", "FSS_filing_revision_order"),
        red_flag_fields=("headline_order_backlog_only", "dilution_adjusted_EPS_unconfirmed", "capital_raise_disclosure_quality_issue"),
        price_data_source="FT / Reuters share-sale and FSS filing-revision anchors",
        reported_price_anchor="3.6T KRW share sale; offer 605,000 KRW; 16% discount",
        reported_return_anchor="shares -13% after share-sale plan; YTD pre-event gain more than double",
        event_mfe_pct=None,
        event_mae_pct=-13.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=605000,
        stage4c_price_anchor=None,
        extra_price_metrics={"share_sale_krw_trn": 3.6, "share_sale_usd_bn": 2.5, "offer_price_krw": 605000, "discount_to_prior_close_pct": 16, "event_mae_pct": -13, "ytd_pre_event_gain_context": "more_than_double", "fss_revision_order": True, "disclosure_quality_issue": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="theme_overheat",
        round_rerating_label="defense_backlog_4B_dilution_reset",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="order_backlog_not_dilution_adjusted_EPS_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Order backlog and geopolitical premium must be adjusted for dilution and disclosure quality.",
    ),
    Round295CaseCandidate(
        case_id="r13_loop14_lnf_tesla_signed_contract_collapse_hard_4c",
        symbol="066970",
        company_name="L&F",
        primary_archetype=E2RArchetype.SIGNED_CONTRACT_COLLAPSE_HARD_4C,
        secondary_archetypes=(E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT, E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4C",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2023, 2, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="customer-name contract is not Green without actual call-off and revenue recognition",
        stage4b_status="hard-4C/signed-contract-collapse",
        hard_4c_confirmed=True,
        evidence_fields=("Tesla_contract_headline", "initial_contract_value_2_9B_USD", "revised_contract_value_7386_USD"),
        red_flag_fields=("large_customer_name_only", "actual_calloff_unconfirmed", "customer_model_ramp_failure"),
        price_data_source="Reuters L&F/Tesla contract-value collapse anchor",
        reported_price_anchor="$2.9B expected deal cut to $7,386",
        reported_return_anchor="contract value collapse -99.9997%",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_contract_value_usd_bn": 2.9, "revised_contract_value_usd": 7386, "contract_value_collapse_pct": -99.9997, "supply_period": "2024-01_to_2025-12", "customer": "Tesla and affiliates", "material": "high-nickel cathode materials", "application_context": "Tesla 4680 cells", "reported_likely_drivers": ["EV demand slowdown", "4680 production/ramp difficulty", "Cybertruck underperformance"]},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="signed_contract_collapse_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="signed_contract_without_actual_calloff",
        price_validation_status="reported_contract_collapse_anchor_not_full_ohlc",
        notes="Customer-name and signed contract amount are not Green without actual call-off or revenue recognition.",
    ),
    Round295CaseCandidate(
        case_id="r13_loop14_kogas_blue_whale_resource_event_premium",
        symbol="036460/117580/096770/018670",
        company_name="Korea Gas / Daesung Energy / SK Innovation / SK Gas",
        primary_archetype=E2RArchetype.RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE,
        secondary_archetypes=(E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="price_moved_without_evidence",
        stage1_date=date(2024, 6, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2024, 6, 3),
        stage4c_date=None,
        stage3_decision="resource estimate is not Green before drilling result, reserve certification, economics and IRR",
        stage4b_status="4B-watch/resource-event-premium",
        hard_4c_confirmed=False,
        evidence_fields=("presidential_drilling_approval", "14B_boe_potential_resource", "KOGAS_plus_30pct"),
        red_flag_fields=("policy_or_presidential_announcement_only", "resource_estimate_without_drilling", "economic_viability_unconfirmed"),
        price_data_source="Reuters / WSJ resource-discovery event anchors",
        reported_price_anchor="Korea Gas event price 38,700 KRW; Korea Gas +30%",
        reported_return_anchor="KOGAS +30%, Daesung +30%, SK Innovation +6%, SK Gas +7%",
        event_mfe_pct=30.0,
        event_mae_pct=None,
        stage1_price_anchor=38700,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=38700,
        stage4c_price_anchor=None,
        extra_price_metrics={"korea_gas_event_mfe_pct": 30, "korea_gas_event_price_krw": 38700, "daesung_energy_event_mfe_pct": 30, "sk_innovation_event_mfe_pct": 6, "sk_gas_event_mfe_pct": 7, "kospi_same_context_pct": 1.9, "potential_resource_boe_bn": 14, "project_cost_krw_bn_min": 500, "per_well_cost_krw_bn": 100, "success_probability_pct": 20, "commercial_production_target": 2035, "drilling_result_confirmed": False, "economic_viability_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_label="resource_discovery_event_premium",
        stage_failure_type="false_yellow",
        round_stage_failure_label="resource_estimate_without_drilling_IRR",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Resource estimate and presidential announcement moved price before drilling and economic viability.",
    ),
    Round295CaseCandidate(
        case_id="r13_loop14_lg_cns_ai_cloud_ipo_false_positive",
        symbol="064400",
        company_name="LG CNS",
        primary_archetype=E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.IPO_QUALITY_GATE_FALSE_POSITIVE, E2RArchetype.PLATFORM_SOFTWARE_INTERNET),
        case_type="failed_rerating",
        round_case_type="evidence_good_but_price_failed",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 2, 5),
        stage3_date=None,
        stage4b_date=date(2025, 2, 5),
        stage4c_date=None,
        stage3_decision="AI/cloud IPO story is not Green when aftermarket price fails the IPO price test",
        stage4b_status="4B-watch/IPO-demand-with-weak-debut",
        hard_4c_confirmed=False,
        evidence_fields=("cloud_AI_sales_mix_over_half", "IPO_1_2T_KRW", "retail_oversubscription_123x"),
        red_flag_fields=("IPO_oversubscription_only", "aftermarket_price_validation_failed", "first_earnings_unconfirmed"),
        price_data_source="Reuters LG CNS IPO/debut anchor",
        reported_price_anchor="IPO 61,900 KRW; open 60,500 KRW; morning trade 59,700 KRW",
        reported_return_anchor="morning trade -3.55% vs IPO price",
        event_mfe_pct=None,
        event_mae_pct=-3.55,
        stage1_price_anchor=None,
        stage2_price_anchor=61900,
        stage3_price_anchor=None,
        stage4b_price_anchor=59700,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_krw": 61900, "open_price_krw": 60500, "morning_trading_price_krw": 59700, "debut_mae_vs_ipo_pct": -3.55, "ipo_raise_krw_trn": 1.2, "ipo_raise_usd_mn": 827.1, "retail_oversubscription_multiple": 123, "institutional_bids_krw_trn": 76, "cloud_ai_sales_share_context": "over_half_of_9m_2024_sales", "aftermarket_demand_confirmed": False},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="AI_cloud_IPO_quality_gate",
        stage_failure_type="false_yellow",
        round_stage_failure_label="AI_cloud_sales_mix_not_aftermarket_green",
        price_validation_status="reported_IPO_aftermarket_anchor_not_full_ohlc",
        notes="AI/cloud sales mix and IPO oversubscription failed aftermarket validation.",
    ),
    Round295CaseCandidate(
        case_id="r13_loop14_samsung_ct_valueup_proposal_failure",
        symbol="028260",
        company_name="Samsung C&T",
        primary_archetype=E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN),
        case_type="failed_rerating",
        round_case_type="false_positive_score",
        stage1_date=date(2024, 3, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 3, 15),
        stage3_decision="Value-Up proposal is not Green until board adoption and cash-return execution occur",
        stage4b_status="4C-watch/valueup-proposal-failure",
        hard_4c_confirmed=False,
        evidence_fields=("activist_dividend_buyback_proposal", "Norway_oil_fund_support", "Canadian_pension_support"),
        red_flag_fields=("activist_or_valueup_proposal_only", "proposal_passed_false", "NPS_sided_with_management"),
        price_data_source="FT activist proposal failure anchor",
        reported_price_anchor="activist proposals failed; shares closed almost -10%",
        reported_return_anchor="Samsung C&T almost -10% after proposal failure",
        event_mfe_pct=None,
        event_mae_pct=-10.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mae_pct": -10.0, "activist_backers": ["Norway oil fund", "Canadian pension investors"], "nps_vote": "sided_with_management", "proposal_type": ["dividend increase", "share buyback increase"], "proposal_passed": False, "stage3_conditions": ["board adoption", "payout execution", "treasury-share cancellation", "minority shareholder alignment"]},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="no_rerating",
        round_rerating_label="shareholder_return_proposal_failed",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="governance_proposal_not_capital_return_execution",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Value-Up proposal is not Green unless board adoption and cash-return execution occur.",
    ),
    Round295CaseCandidate(
        case_id="r13_loop14_skt_data_trust_hard_4c",
        symbol="017670",
        company_name="SK Telecom",
        primary_archetype=E2RArchetype.DATA_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.PLATFORM_TRUST_4C_WATCH, E2RArchetype.OPERATIONAL_TRUST_AND_MACRO_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4C",
        stage1_date=date(2025, 4, 18),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="data trust breach blocks Green when it changes revenue forecast, capex, compensation and liabilities",
        stage4b_status="hard-4C/data-trust",
        hard_4c_confirmed=True,
        evidence_fields=("data_breach_detected", "USIM_replacement_23M_users", "revenue_forecast_cut_800B_KRW"),
        red_flag_fields=("data_breach_treated_as_oneoff", "contingent_liability_risk", "data_trust_internal_control_failed"),
        price_data_source="Reuters SK Telecom breach, government investigation and compensation anchors",
        reported_price_anchor="intraday -8.5%, close -6.7%, July event close -5.6%",
        reported_return_anchor="revenue forecast cut 800B KRW; possible compensation 2.3T KRW",
        event_mfe_pct=None,
        event_mae_pct=-8.5,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_intraday_mae_pct": -8.5, "initial_close_mae_pct": -6.7, "kospi_same_context_pct": 0.1, "relative_underperformance_initial_pp": -6.8, "free_usim_replacement_users_mn": 23, "retail_stores_involved": 2600, "usim_protection_service_signups_mn": 5.54, "leaked_data_pieces_mn": 26.96, "july_event_close_mae_pct": -5.6, "data_protection_investment_krw_bn": 700, "revenue_forecast_cut_krw_bn": 800, "customer_benefit_package_cost_krw_bn": 500, "consumer_agency_possible_total_compensation_krw_trn": 2.3, "stage4c_validation_dates": ["2025-04-28", "2025-07-04", "2025-12-21"]},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="data_trust_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="customer_data_internal_control_break",
        price_validation_status="reported_hard_4c_anchor_not_full_ohlc",
        notes="Data breach is not a one-off event when it changes revenue forecast, capex, compensation and contingent liability.",
    ),
    Round295CaseCandidate(
        case_id="r13_loop14_hyundai_steel_us_localization_capex_false_positive",
        symbol="004020",
        company_name="Hyundai Steel",
        primary_archetype=E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.US_LOCALIZATION_CAPEX_FALSE_POSITIVE, E2RArchetype.COMMODITY_SPREAD),
        case_type="failed_rerating",
        round_case_type="false_positive_score",
        stage1_date=date(2025, 3, 24),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="localization capex is not Green without funding clarity, IRR, demand and tariff-saving durability",
        stage4b_status="4C-watch/localization-capex-backlash",
        hard_4c_confirmed=False,
        evidence_fields=("US_plant_6B_USD", "Hyundai_group_package_21B_USD", "vehicle_equivalent_output_1_8M"),
        red_flag_fields=("capex_localization_headline_only", "funding_plan_unclear", "IRR_unconfirmed"),
        price_data_source="Reuters Hyundai Steel U.S. plant investor-backlash anchor",
        reported_price_anchor="Hyundai Steel -21.2% after U.S. plant plan",
        reported_return_anchor="Hyundai Steel -21.2%, POSCO -18.3%, KOSPI -5.5%",
        event_mfe_pct=None,
        event_mae_pct=-21.2,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"us_plant_investment_usd_bn": 6, "hyundai_group_us_package_usd_bn": 21, "hyundai_steel_stock_decline_since_announcement_pct": -21.2, "posco_same_period_decline_pct": -18.3, "kospi_same_period_decline_pct": -5.5, "hyundai_motor_same_period_decline_pct": -12.9, "planned_output_vehicle_equivalent_mn": 1.8, "hyundai_kia_us_production_target_mn": 1.2, "debt_funding_share_pct": 50, "full_funding_plan_disclosed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="no_rerating",
        round_rerating_label="localization_capex_false_positive",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="capex_without_IRR_funding_clarity",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Localization capex needs funding clarity, IRR, customer demand and tariff-saving durability.",
    ),
    Round295CaseCandidate(
        case_id="r13_loop14_korea_zinc_control_premium_4b",
        symbol="010130/000670",
        company_name="Korea Zinc / Young Poong / MBK",
        primary_archetype=E2RArchetype.CONTROL_PREMIUM_4B_GOVERNANCE_WATCH,
        secondary_archetypes=(E2RArchetype.CONTROL_PREMIUM_DILUTION_4B, E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE),
        case_type="4b_watch",
        round_case_type="4B-watch",
        stage1_date=date(2024, 9, 13),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2024, 9, 13),
        stage4c_date=None,
        stage3_decision="control premium is not operating Green without cashflow, smelter margin and FCF improvement",
        stage4b_status="4B-watch/control-premium-governance-watch",
        hard_4c_confirmed=False,
        evidence_fields=("MBK_Young_Poong_tender_offer", "offer_price_660000_KRW", "Korea_Zinc_plus_19_8pct"),
        red_flag_fields=("control_premium_as_operating_green", "operating_cashflow_improvement_unconfirmed", "governance_dispute"),
        price_data_source="Reuters Korea Zinc tender-offer anchor",
        reported_price_anchor="2T KRW tender offer; offer 660,000 KRW; prior close 556,000 KRW",
        reported_return_anchor="Korea Zinc +19.8%, Young Poong +30%",
        event_mfe_pct=30.0,
        event_mae_pct=None,
        stage1_price_anchor=556000,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=660000,
        stage4c_price_anchor=None,
        extra_price_metrics={"tender_offer_value_krw_trn": 2.0, "tender_offer_value_usd_bn": 1.5, "offer_price_krw": 660000, "prior_close_krw": 556000, "tender_premium_to_prior_close_pct": 18.7, "target_stake_min_pct": 6.98, "target_stake_max_pct": 14.61, "korea_zinc_event_mfe_pct": 19.8, "young_poong_event_mfe_pct": 30.0, "young_poong_existing_stake_pct": 25.4, "combined_stake_if_success_pct": 40.0, "operating_cashflow_improvement_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="control_premium_not_operating_green",
        stage_failure_type="false_yellow",
        round_stage_failure_label="tender_offer_governance_premium_not_margin_FCF",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tender/control premium must be separated from operating cashflow, smelter margin and FCF.",
    ),
)


def round295_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(_case_record(case) for case in ROUND295_CASE_CANDIDATES)


def round295_summary() -> dict[str, object]:
    cases = ROUND295_CASE_CANDIDATES
    return {
        "source_round": ROUND295_SOURCE_ROUND_PATH,
        "round_id": ROUND295_ANALYST_ROUND_ID,
        "large_sector": ROUND295_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "watch_counterexample_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round295_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(_case_row(case) for case in ROUND295_CASE_CANDIDATES)


def round295_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND295_REQUIRED_TARGET_ALIASES.items())


def round295_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND295_SCORE_ADJUSTMENTS)


def round295_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND295_SHADOW_WEIGHT_ROWS)


def round295_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND295_DEEP_SUB_ARCHETYPES)


def round295_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field} for field in ROUND295_PRICE_VALIDATION_FIELDS)


def round295_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND295_SOURCE_ROUND_PATH,
        "round_id": ROUND295_ANALYST_ROUND_ID,
        "large_sector": ROUND295_LARGE_SECTOR,
        "summary": round295_summary(),
        "target_aliases": dict(ROUND295_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND295_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND295_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND295_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND295_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND295_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_round295_shadow_weights_to_production_scoring_yet",
            "do_not_use_round295_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_headlines_as_cashflow",
            "do_not_invent_full_adjusted_ohlc",
        ],
    }


def render_round295_summary_markdown() -> str:
    summary = round295_summary()
    lines = [
        "# Round 295 R13 Loop 14 Cross-archetype RedTeam Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- 4B watch cases: {summary['stage4b_watch_count']}",
        f"- 4C watch cases: {summary['stage4c_watch_count']}",
        f"- hard 4C cases: {summary['hard_4c_case_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- false_positive_score: {summary['false_positive_score_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        "- price_validation_completed: partial_with_reported_event_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND295_CASE_CANDIDATES:
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
            "- Hanwha Aerospace is a backlog-dilution 4B example: strong orders do not remove dilution math.",
            "- L&F/Tesla is hard 4C: signed amount and customer name did not become actual call-off revenue.",
            "- Korea Gas/Blue Whale is price moved without evidence: resource headline moved price before drilling and economics.",
            "- LG CNS is an IPO quality gate: oversubscription did not survive aftermarket price validation.",
            "- Samsung C&T separates Value-Up proposal from actual capital return execution.",
            "- SK Telecom is data-trust hard 4C because the event affected revenue forecast, capex, compensation and liability.",
            "- Hyundai Steel shows localization capex can be a funding/IRR risk, not automatic tariff hedge Green.",
            "- Korea Zinc separates control premium from operating cashflow rerating.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round295_green_gate_review_markdown() -> str:
    lines = [
        "# Round 295 R13 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R13 Stage 3-Green is not `headline is good`. It requires the headline to close into cashflow, delivered revenue, margin, internal controls, and post-event price validation.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND295_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND295_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND295_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Tesla contract` is not Green until actual call-off and revenue recognition appear.",
            "- `Value-Up proposal` is not Green until the board adopts and executes cash return.",
            "- `data breach` is not one-off if revenue forecast, capex, compensation and liability change.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round295_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 295 R13 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND295_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND295_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "이번 라운드에서 hard 4C는 L&F/Tesla signed-contract collapse와 SK Telecom data-trust breach다.",
            "",
            "## Case Review",
            "",
            "| case | company | 4B status | hard 4C | interpretation |",
            "|---|---|---|---|---|",
        ]
    )
    for case in ROUND295_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round295_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 295 R13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_event_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent adjusted OHLC, stage prices, contract call-off, IRR, post-IPO validation, governance execution, drilling economics, or operating cashflow where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND295_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND295_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round295_r13_loop14_reports(
    output_directory: str | Path = ROUND295_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND295_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND295_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round295_case_records(), cases_path),
        "audit": _write_json(round295_audit_payload(), audit_path),
        "summary": output / "round295_r13_loop14_price_validation_summary.md",
        "case_matrix": output / "round295_r13_loop14_case_matrix.csv",
        "target_aliases": output / "round295_r13_loop14_target_aliases.csv",
        "score_adjustments": output / "round295_r13_loop14_score_adjustments.csv",
        "shadow_weights": output / "round295_r13_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round295_r13_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round295_r13_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round295_r13_loop14_green_gate_review.md",
        "price_validation_plan": output / "round295_r13_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round295_r13_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round295_summary_markdown(), encoding="utf-8")
    _write_csv(round295_case_rows(), paths["case_matrix"])
    _write_csv(round295_target_alias_rows(), paths["target_aliases"])
    _write_csv(round295_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round295_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round295_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round295_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round295_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round295_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round295_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def _case_record(case: Round295CaseCandidate) -> E2RCaseRecord:
    return E2RCaseRecord(
        case_id=case.case_id,
        symbol=case.symbol,
        company_name=case.company_name,
        market="KR",
        sector_raw=ROUND295_LARGE_SECTOR,
        primary_archetype=case.primary_archetype,
        expected_group=case.expected_group,
        large_sector=ROUND295_LARGE_SECTOR,
        secondary_archetypes=case.secondary_archetypes,
        case_type=case.case_type,
        stage1_date=case.stage1_date,
        stage2_date=case.stage2_date,
        stage3_date=case.stage3_date,
        stage4b_date=case.stage4b_date,
        stage4c_date=case.stage4c_date,
        evidence_summary=case.notes,
        stage1_evidence=case.evidence_fields,
        stage2_evidence=case.evidence_fields if case.stage2_date else (),
        stage3_evidence=(),
        stage4b_evidence=case.evidence_fields if case.stage4b_date else (),
        stage4c_evidence=case.red_flag_fields if case.stage4c_date else (),
        must_have_fields=ROUND295_GREEN_REQUIRED_FIELDS,
        red_flag_fields=case.red_flag_fields,
        key_evidence_fields=case.evidence_fields,
        false_positive_reason=case.round_stage_failure_label,
        score_price_alignment=case.score_price_alignment,
        rerating_result=case.rerating_result,
        stage_failure_type=case.stage_failure_type,
        price_pattern=case.round_alignment_label,
        score_weight_hint={},
        green_guardrails=(
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "do_not_use_round295_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_headlines_as_cashflow",
        ),
        notes=case.notes,
        price_validation=PriceValidation(
            stage1_price=case.stage1_price_anchor,
            stage2_price=case.stage2_price_anchor,
            stage3_price=case.stage3_price_anchor,
            stage4b_price=case.stage4b_price_anchor,
            stage4c_price=case.stage4c_price_anchor,
            mfe_30d=case.event_mfe_pct,
            mae_30d=case.event_mae_pct,
            price_validation_status=case.price_validation_status,
        ),
        data_quality=CaseDataQuality(official_data_available=False, report_data_available=True, price_data_available=False, stage_dates_confidence=0.7),
    )


def _case_row(case: Round295CaseCandidate) -> dict[str, str]:
    return {
        "case_id": case.case_id,
        "symbol": case.symbol,
        "company_name": case.company_name,
        "primary_archetype": case.primary_archetype.value,
        "secondary_archetypes": "|".join(item.value for item in case.secondary_archetypes),
        "case_type": case.case_type,
        "round_case_type": case.round_case_type,
        "stage1_date": _date_text(case.stage1_date),
        "stage2_date": _date_text(case.stage2_date),
        "stage3_date": _date_text(case.stage3_date),
        "stage4b_date": _date_text(case.stage4b_date),
        "stage4c_date": _date_text(case.stage4c_date),
        "stage3_decision": case.stage3_decision,
        "stage4b_status": case.stage4b_status,
        "hard_4c_confirmed": str(case.hard_4c_confirmed).lower(),
        "evidence_fields": "|".join(case.evidence_fields),
        "red_flag_fields": "|".join(case.red_flag_fields),
        "price_data_source": case.price_data_source,
        "reported_price_anchor": case.reported_price_anchor,
        "reported_return_anchor": case.reported_return_anchor,
        "event_mfe_pct": _float_text(case.event_mfe_pct),
        "event_mae_pct": _float_text(case.event_mae_pct),
        "score_price_alignment": case.score_price_alignment,
        "round_alignment_label": case.round_alignment_label,
        "rerating_result": case.rerating_result,
        "round_rerating_label": case.round_rerating_label,
        "stage_failure_type": case.stage_failure_type,
        "round_stage_failure_label": case.round_stage_failure_label,
        "price_validation_status": case.price_validation_status,
        "extra_price_metrics": json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True),
        "notes": case.notes,
    }


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
