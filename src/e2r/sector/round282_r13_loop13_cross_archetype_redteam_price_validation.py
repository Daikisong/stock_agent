"""Round-282 R13 Loop-13 cross-archetype RedTeam price-validation pack.

This module converts ``docs/round/round_282.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: a Tesla-name supply contract is not Stage 3-Green by itself. It
must close into actual call-off, shipment, revenue recognition, margin, and
cash conversion. If the contract value later collapses, it becomes a 4C lesson.
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


ROUND282_SOURCE_ROUND_PATH = "docs/round/round_282.md"
ROUND282_ANALYST_ROUND_ID = "round_210"
ROUND282_LARGE_SECTOR = "CROSS_ARCHETYPE_REDTEAM_4B_ACCOUNTING_TRUST_PRICE_VALIDATION"
ROUND282_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round282_r13_loop13_cross_archetype_redteam_price_validation"
ROUND282_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r13_loop13_round282.jsonl"
ROUND282_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round282_r13_loop13_cross_archetype_redteam_price_validation_audit.json"

ROUND282_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "CYBERSECURITY_TRUST_HARD_4C": E2RArchetype.CYBERSECURITY_TRUST_HARD_4C.value,
    "AVIATION_SAFETY_HARD_4C": E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
    "CONTRACT_VALUE_COLLAPSE_HARD_4C": E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C.value,
    "DIGITAL_ASSET_TRUST_4C_WATCH": E2RArchetype.DIGITAL_ASSET_TRUST_4C_WATCH.value,
    "IPO_QUALITY_GATE_FALSE_POSITIVE": E2RArchetype.IPO_QUALITY_GATE_FALSE_POSITIVE.value,
    "CONTROL_PREMIUM_DILUTION_4B": E2RArchetype.CONTROL_PREMIUM_DILUTION_4B.value,
    "ORDER_HEADLINE_NOT_MARGIN_GREEN": E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN.value,
    "CAPITAL_RECYCLING_IPO_FAILED_RERATING": E2RArchetype.CAPITAL_RECYCLING_IPO_FAILED_RERATING.value,
}

ROUND282_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_calloff_revenue_recognition_confirmed",
    "shipment_or_delivery_conversion_confirmed",
    "project_margin_cash_conversion_confirmed",
    "working_capital_unbilled_receivables_confirmed",
    "aftermarket_ipo_demand_confirmed",
    "parent_ROI_bridge_confirmed",
    "M&A_closing_regulatory_integration_confirmed",
    "data_trust_internal_control_confirmed",
    "custody_and_digital_asset_control_confirmed",
    "fatal_safety_event_absent_or_resolved",
    "dilution_and_governance_risk_cleared",
    "accounting_investigation_absent_or_resolved",
    "price_path_after_evidence",
)

ROUND282_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "customer_name_headline_only",
    "order_backlog_headline_only",
    "IPO_size_or_oversubscription_only",
    "control_premium_only",
    "M&A_synergy_before_trust",
    "AI_cloud_keyword_without_aftermarket_demand",
    "governance_fight_or_dilution",
    "accounting_fraud_review",
    "safety_or_data_trust_unresolved",
)

ROUND282_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "tender_control_premium_15_25pct_rally",
    "IPO_oversub_or_large_IPO_headline_near_issue_price",
    "mega_order_announcement_day_5_10pct_rally",
    "M&A_day_5pct_plus_rally_before_closing_or_trust",
    "AI_cloud_stablecoin_robotics_customer_name_headline_before_revenue_bridge",
    "large_contract_but_calloff_unclear",
    "management_control_fight_new_share_issue_dilution_risk",
)

ROUND282_HARD_4C_GATES: tuple[str, ...] = (
    "data_breach_with_revenue_fine_compensation",
    "fatal_safety_event",
    "contract_value_collapse_or_customer_program_cancellation",
    "abnormal_withdrawal_or_custody_failure",
    "accounting_fraud_investigation_or_disclosure_control_failure",
    "dilutive_issuance_after_control_premium_rally",
    "IPO_debut_failure_after_valuation_heavy_bookbuilding",
    "EPC_cost_overrun_unbilled_receivables_or_working_capital_stress",
)

ROUND282_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "deal_value_anchor",
    "IPO_price_anchor",
    "fine_anchor",
    "revenue_cut_anchor",
    "market_cap_wipeout_anchor",
    "contract_collapse_value_anchor",
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
class Round282ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round282ShadowWeightRow:
    archetype: E2RArchetype
    trust_and_internal_control: int
    fatal_safety_event: int
    actual_calloff_vs_contract: int
    custody_and_digital_asset_control: int
    aftermarket_ipo_demand: int
    governance_dilution_control: int
    accounting_investigation_flag: int
    project_margin_cash_conversion: int
    working_capital_unbilled_receivables: int
    parent_roi_bridge: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "trust_and_internal_control": _signed(self.trust_and_internal_control),
            "fatal_safety_event": _signed(self.fatal_safety_event),
            "actual_calloff_vs_contract": _signed(self.actual_calloff_vs_contract),
            "custody_and_digital_asset_control": _signed(self.custody_and_digital_asset_control),
            "aftermarket_ipo_demand": _signed(self.aftermarket_ipo_demand),
            "governance_dilution_control": _signed(self.governance_dilution_control),
            "accounting_investigation_flag": _signed(self.accounting_investigation_flag),
            "project_margin_cash_conversion": _signed(self.project_margin_cash_conversion),
            "working_capital_unbilled_receivables": _signed(self.working_capital_unbilled_receivables),
            "parent_ROI_bridge": _signed(self.parent_roi_bridge),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round282DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round282CaseCandidate:
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


ROUND282_SCORE_ADJUSTMENTS: tuple[Round282ScoreAdjustment, ...] = (
    Round282ScoreAdjustment("trust_and_internal_control", 5, "raise", "보안·개인정보·내부통제 훼손은 EPS보다 먼저 Green을 막는다."),
    Round282ScoreAdjustment("fatal_safety_event", 5, "raise", "항공·건설·배터리·의료기기에서는 사망사고가 hard 4C gate다."),
    Round282ScoreAdjustment("actual_calloff_vs_contract", 5, "raise", "고객명 계약 headline은 call-off, shipment, revenue로 닫혀야 한다."),
    Round282ScoreAdjustment("custody_and_digital_asset_control", 5, "raise", "디지털자산 M&A는 수탁·인출·규제 통제가 확인되어야 한다."),
    Round282ScoreAdjustment("aftermarket_IPO_demand", 5, "raise", "IPO 수요예측보다 상장 후 가격·거래 수요가 품질 검증이다."),
    Round282ScoreAdjustment("governance_dilution_control", 5, "raise", "경영권 분쟁 프리미엄은 신주발행·희석·지배구조 리스크와 함께 본다."),
    Round282ScoreAdjustment("accounting_investigation_flag", 5, "raise", "회계조사·공시통제 실패는 구조적 rerating을 차단한다."),
    Round282ScoreAdjustment("project_margin_cash_conversion", 5, "raise", "대형 EPC 수주는 프로젝트 마진과 현금회수가 보여야 한다."),
    Round282ScoreAdjustment("working_capital_unbilled_receivables", 5, "raise", "미청구공사·운전자본 stress는 수주 headline보다 중요하다."),
    Round282ScoreAdjustment("parent_ROI_bridge", 4, "raise", "자회사 IPO는 모회사 ROIC/FCF/환원 bridge가 있어야 한다."),
    Round282ScoreAdjustment("customer_name_headline_only", -5, "lower", "고객명이 유명하다는 이유만으로 Green을 만들지 않는다."),
    Round282ScoreAdjustment("order_backlog_headline_only", -5, "lower", "수주잔고 headline만 있고 마진·현금화가 없으면 제한한다."),
    Round282ScoreAdjustment("IPO_size_or_oversubscription_only", -5, "lower", "IPO 규모와 청약경쟁률은 상장 후 수요 검증 전에는 부족하다."),
    Round282ScoreAdjustment("control_premium_only", -5, "lower", "경영권 프리미엄은 운영 EPS/FCF 변화가 아니다."),
    Round282ScoreAdjustment("M&A_synergy_before_trust", -5, "lower", "M&A synergy는 신뢰·수탁·규제 이슈보다 뒤에 본다."),
    Round282ScoreAdjustment("AI_cloud_keyword_without_aftermarket_demand", -5, "lower", "AI/cloud 키워드만으로 IPO 품질을 인정하지 않는다."),
    Round282ScoreAdjustment("governance_fight_or_dilution", -5, "lower", "분쟁·희석은 자본배분 질을 훼손한다."),
    Round282ScoreAdjustment("accounting_fraud_review", -5, "lower", "회계부정 검토 flag는 hard RedTeam 입력이다."),
    Round282ScoreAdjustment("safety_or_data_trust_unresolved", -5, "lower", "안전·데이터 신뢰가 열려 있으면 Green은 차단한다."),
)


ROUND282_SHADOW_WEIGHT_ROWS: tuple[Round282ShadowWeightRow, ...] = (
    Round282ShadowWeightRow(E2RArchetype.CYBERSECURITY_TRUST_HARD_4C, 5, 0, 0, 2, 0, 1, 4, 0, 0, 0, -5, 5, 5, "SK Telecom shows data breach can cut revenue, add compensation, capex and fines."),
    Round282ShadowWeightRow(E2RArchetype.AVIATION_SAFETY_HARD_4C, 2, 5, 0, 0, 0, 0, 1, 0, 0, 0, -5, 4, 5, "Jeju Air confirms fatal aviation accident overrides demand recovery."),
    Round282ShadowWeightRow(E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C, 1, 0, 5, 0, 0, 0, 1, 2, 1, 0, -5, 5, 5, "L&F/Tesla confirms customer-name contract requires actual call-off and revenue."),
    Round282ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_TRUST_4C_WATCH, 4, 0, 0, 5, 0, 2, 2, 0, 0, 1, -5, 5, 4, "Naver/Dunamu shows digital-asset M&A must pass custody and trust gates."),
    Round282ShadowWeightRow(E2RArchetype.IPO_QUALITY_GATE_FALSE_POSITIVE, 1, 0, 0, 0, 5, 1, 1, 1, 0, 2, -5, 4, 4, "LG CNS shows AI/cloud IPO story needs aftermarket demand."),
    Round282ShadowWeightRow(E2RArchetype.CONTROL_PREMIUM_DILUTION_4B, 2, 0, 0, 0, 0, 5, 5, 0, 0, 3, -5, 5, 4, "Korea Zinc confirms control premium must be capped by dilution and accounting flags."),
    Round282ShadowWeightRow(E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN, 1, 0, 1, 0, 0, 0, 1, 5, 5, 0, -4, 5, 4, "Samsung E&A mega order needs margin, WC and cash collection before Green."),
    Round282ShadowWeightRow(E2RArchetype.CAPITAL_RECYCLING_IPO_FAILED_RERATING, 1, 0, 0, 0, 5, 2, 1, 0, 0, 4, -5, 4, 4, "Hyundai Motor India IPO shows parent capital recycling needs ROI and listing validation."),
)


ROUND282_DEEP_SUB_ARCHETYPES: tuple[Round282DeepSubArchetype, ...] = (
    Round282DeepSubArchetype("Trust break", E2RArchetype.CYBERSECURITY_TRUST_HARD_4C, ("SK Telecom data breach", "26.96M data pieces", "PIPC fine 134B KRW", "revenue forecast cut 800B KRW", "customer benefit 500B KRW")),
    Round282DeepSubArchetype("Safety hard gate", E2RArchetype.AVIATION_SAFETY_HARD_4C, ("Jeju Air fatal crash", "179 fatalities", "event low 6,920 KRW", "market cap wipeout 95.7B KRW", "government safety inspection")),
    Round282DeepSubArchetype("Contract quality", E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C, ("L&F Tesla 4680 cathode", "$2.9B projected value", "$7,386 revised value", "actual call-off failure", "contract value collapse")),
    Round282DeepSubArchetype("Digital asset trust", E2RArchetype.DIGITAL_ASSET_TRUST_4C_WATCH, ("Naver Financial Dunamu", "Upbit 54B KRW abnormal withdrawal", "15.13T KRW deal", "custody trust", "M&A synergy before trust")),
    Round282DeepSubArchetype("IPO quality", E2RArchetype.IPO_QUALITY_GATE_FALSE_POSITIVE, ("LG CNS IPO", "AI/cloud 54% sales", "IPO price 61,900", "weak debut", "aftermarket demand")),
    Round282DeepSubArchetype("Control and governance", E2RArchetype.CONTROL_PREMIUM_DILUTION_4B, ("Korea Zinc tender offer", "660,000 KRW offer", "$1.8B new share issue", "accounting fraud review", "control premium dilution")),
    Round282DeepSubArchetype("Order headline", E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN, ("Samsung E&A Fadhili", "$6B contract", "77.9% project share", "EPC margin", "working capital")),
    Round282DeepSubArchetype("Capital recycling IPO", E2RArchetype.CAPITAL_RECYCLING_IPO_FAILED_RERATING, ("Hyundai Motor India IPO", "$3.3B IPO", "17.5% parent stake", "weak debut", "parent ROI bridge")),
)


ROUND282_CASE_CANDIDATES: tuple[Round282CaseCandidate, ...] = (
    Round282CaseCandidate(
        case_id="r13_loop13_skt_cybersecurity_hard_4c",
        symbol="017670",
        company_name="SK Telecom data breach hard 4C",
        primary_archetype=E2RArchetype.CYBERSECURITY_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C, E2RArchetype.OPERATIONAL_TRUST_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="hard 4C / cybersecurity trust break",
        stage1_date=date(2025, 4, 18),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="data_breach_revenue_fine_compensation_and_security_capex_block_green",
        stage4b_status="hard-4C/data-trust-internal-control",
        hard_4c_confirmed=True,
        evidence_fields=("malware_customer_data_leak", "23mn_users_free_USIM_replacement", "5_54mn_USIM_protection_signups", "26_96mn_data_pieces_leaked", "PIPC_fine_134bn_krw"),
        red_flag_fields=("data_breach_with_revenue_fine_compensation", "revenue_forecast_cut_800bn_krw", "customer_benefit_cost_500bn_krw", "data_protection_investment_700bn_krw"),
        price_data_source="Reuters event-return anchors",
        reported_price_anchor="intraday -8.5%, close -6.7%, July event close -5.6%",
        reported_return_anchor="Revenue forecast cut, compensation cost, data-protection investment and fine validate hard 4C.",
        event_mfe_pct=None,
        event_mae_pct=-8.5,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_intraday_mae_pct": -8.5, "initial_close_mae_pct": -6.7, "kospi_same_context_pct": 0.1, "relative_underperformance_initial_pp": -6.8, "usim_replacement_users_mn": 23, "retail_stores_involved": 2600, "usim_protection_service_signups_mn": 5.54, "leaked_data_pieces_mn": 26.96, "july_event_close_mae_pct": -5.6, "data_protection_investment_krw_bn": 700, "revenue_forecast_cut_krw_bn": 800, "customer_benefit_package_cost_krw_bn": 500, "pipc_fine_krw_bn": 134},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="hard_4C_successfully_identified",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="data_trust_cybersecurity_internal_control_hard_gate",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Data trust break must outrank telecom demand or dividend narratives.",
    ),
    Round282CaseCandidate(
        case_id="r13_loop13_jeju_air_safety_hard_4c",
        symbol="089590",
        company_name="Jeju Air fatal crash hard 4C",
        primary_archetype=E2RArchetype.AVIATION_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.OPERATIONAL_SAFETY_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="hard 4C / aviation safety",
        stage1_date=date(2024, 12, 29),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 30),
        stage3_decision="fatal_safety_event_blocks_travel_recovery_green",
        stage4b_status="hard-4C/fatal-safety-event",
        hard_4c_confirmed=True,
        evidence_fields=("fatalities_179", "deadliest_south_korea_aviation_accident", "government_emergency_safety_inspection", "AK_Holdings_minus_12pct"),
        red_flag_fields=("fatal_safety_event", "consumer_trust_collapse", "operation_system_safety_inspection"),
        price_data_source="Reuters event-price anchor",
        reported_price_anchor="event low 6,920 KRW; intraday -15.7%; market-cap wipeout 95.7B KRW",
        reported_return_anchor="Fatal crash validates hard safety gate before demand or route scoring.",
        event_mfe_pct=None,
        event_mae_pct=-15.7,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=6920,
        extra_price_metrics={"fatalities": 179, "event_low_price_krw": 6920, "event_intraday_mae_pct": -15.7, "event_midday_mae_pct": -8.5, "market_cap_wipeout_krw_bn": 95.7, "market_cap_wipeout_usd_mn": 65.2, "ak_holdings_mae_pct": -12},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="hard_4C_successfully_identified",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="fatal_safety_event_overrides_demand_capacity_score",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Fatal aviation accident is a hard gate for airline and travel recovery narratives.",
    ),
    Round282CaseCandidate(
        case_id="r13_loop13_lnf_tesla_contract_collapse",
        symbol="066970",
        company_name="L&F Tesla 4680 cathode contract collapse",
        primary_archetype=E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C,
        secondary_archetypes=(E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C, E2RArchetype.CONTRACT_QUALITY_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="hard 4C / contract value collapse",
        stage1_date=date(2023, 2, 1),
        stage2_date=date(2023, 2, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="customer_name_contract_never_became_actual_calloff_revenue",
        stage4b_status="hard-4C/contract-value-collapse",
        hard_4c_confirmed=True,
        evidence_fields=("Tesla_and_affiliates_customer_name", "4680_high_nickel_cathode_context", "initial_projected_value_2_9bn_usd", "supply_period_2024_01_to_2025_12"),
        red_flag_fields=("contract_value_collapse_or_customer_program_cancellation", "calloff_failure", "customer_name_headline_only", "EV_demand_slowdown"),
        price_data_source="Reuters contract-collapse value anchor",
        reported_price_anchor="initial projected value $2.9B revised to $7,386",
        reported_return_anchor="Contract headline collapsed before Stage 3 revenue validation.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_projected_value_usd_bn": 2.9, "revised_value_usd": 7386, "contract_value_collapse_pct": -99.9997, "supply_start": "2024-01", "supply_end": "2025-12", "customer": "Tesla and affiliates", "context": "4680 high-nickel cathode"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="customer_name_contract_headline_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="actual_calloff_revenue_recognition_missing",
        price_validation_status="contract_value_anchor_not_full_ohlc",
        notes="Named-customer supply deal must not become Green without call-off, shipment and revenue recognition.",
    ),
    Round282CaseCandidate(
        case_id="r13_loop13_naver_dunamu_upbit_trust_4c_watch",
        symbol="035420",
        company_name="Naver Financial / Dunamu / Upbit trust watch",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_TRUST_4C_WATCH,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH, E2RArchetype.PLATFORM_TRUST_4C_WATCH),
        case_type="event_premium",
        round_case_type="event premium + 4C-watch",
        stage1_date=date(2025, 11, 27),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="M&A_synergy_is_not_green_before_custody_trust_and_closing",
        stage4b_status="4B-watch/4C-watch/digital-asset-trust",
        hard_4c_confirmed=False,
        evidence_fields=("Naver_Financial_Dunamu_merger", "deal_value_15_13trn_krw", "Upbit_share_70pct", "exchange_ratio_2_54"),
        red_flag_fields=("abnormal_withdrawal_or_custody_failure", "M&A_synergy_before_trust", "custody_control_unconfirmed", "regulatory_integration_unconfirmed"),
        price_data_source="Reuters M&A and abnormal-withdrawal event anchors",
        reported_price_anchor="Naver initially +7%, later -4.2%; Upbit abnormal withdrawal 54B KRW",
        reported_return_anchor="M&A price move reversed when digital-asset custody trust entered RedTeam.",
        event_mfe_pct=7.0,
        event_mae_pct=-4.2,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio_naver_financial_per_dunamu": 2.54, "upbit_market_share_pct": 70, "naver_initial_mfe_pct": 7.0, "naver_later_mae_pct": -4.2, "intraday_swing_pp": -11.2, "abnormal_withdrawal_krw_bn": 54, "upbit_loss_covered_with_own_assets": True},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_trust_watch",
        rerating_result="event_premium",
        round_rerating_label="digital_asset_M&A_4B_then_4C_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="M&A_synergy_before_custody_trust",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Digital-asset M&A must clear custody, withdrawal, reserve and regulatory trust gates.",
    ),
    Round282CaseCandidate(
        case_id="r13_loop13_lg_cns_ipo_quality_false_positive",
        symbol="064400",
        company_name="LG CNS AI/cloud IPO weak debut",
        primary_archetype=E2RArchetype.IPO_QUALITY_GATE_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE, E2RArchetype.IPO_EVENT_PREMIUM),
        case_type="failed_rerating",
        round_case_type="IPO quality false positive",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 2, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="AI_cloud_IPO_keyword_needs_aftermarket_demand_and_margin",
        stage4b_status="watch/weak-aftermarket-demand",
        hard_4c_confirmed=False,
        evidence_fields=("IPO_raise_1_2trn_krw", "retail_oversubscription_123x", "institutional_bids_76trn_krw", "cloud_AI_54pct_9m_sales"),
        red_flag_fields=("AI_cloud_keyword_without_aftermarket_demand", "IPO_size_or_oversubscription_only", "weak_debut_below_IPO_price"),
        price_data_source="IPO debut price anchors",
        reported_price_anchor="IPO price 61,900; open 60,500; morning 59,700",
        reported_return_anchor="Weak aftermarket demand capped the AI/cloud IPO story.",
        event_mfe_pct=None,
        event_mae_pct=-3.23,
        stage1_price_anchor=61900,
        stage2_price_anchor=59700,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_krw": 61900, "open_price_krw": 60500, "morning_price_krw": 59700, "debut_mae_vs_ipo_pct": -3.23, "ipo_raise_krw_trn": 1.2, "ipo_raise_usd_mn": 827.1, "market_valuation_krw_trn": 5.79, "retail_oversubscription_x": 123, "institutional_bids_krw_trn": 76, "cloud_ai_share_9m_2024_sales_pct": 54, "revenue_krw_trn": 4.0, "operating_profit_krw_bn": 313, "opm_pct": 7.8},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="IPO_quality_not_validated_by_aftermarket",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_size_AI_cloud_keyword_not_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="IPO size and AI/cloud exposure need post-listing demand, margin and FCF validation.",
    ),
    Round282CaseCandidate(
        case_id="r13_loop13_korea_zinc_control_premium_dilution_4b",
        symbol="010130",
        company_name="Korea Zinc control premium / dilution watch",
        primary_archetype=E2RArchetype.CONTROL_PREMIUM_DILUTION_4B,
        secondary_archetypes=(E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION, E2RArchetype.GOVERNANCE_DILUTION_EVENT),
        case_type="4b_watch",
        round_case_type="4B-watch + governance dilution watch",
        stage1_date=date(2024, 9, 13),
        stage2_date=date(2024, 9, 13),
        stage3_date=None,
        stage4b_date=date(2024, 9, 13),
        stage4c_date=date(2024, 10, 31),
        stage3_decision="control_premium_is_not_operating_green_before_dilution_and_accounting_risk_clear",
        stage4b_status="4B-watch/4C-watch/control-premium-dilution",
        hard_4c_confirmed=False,
        evidence_fields=("tender_offer_2trn_krw", "offer_660000_krw", "prior_close_556000_krw", "target_stake_6_98_to_14_61pct"),
        red_flag_fields=("dilutive_issuance_after_control_premium_rally", "accounting_fraud_investigation_or_disclosure_control_failure", "control_premium_only", "governance_fight_or_dilution"),
        price_data_source="Reuters / WSJ tender and issuance anchors",
        reported_price_anchor="offer 660,000 KRW vs prior close 556,000; high 690,000; new share issue $1.8B",
        reported_return_anchor="Control premium produced 4B-watch before dilution/accounting review risk.",
        event_mfe_pct=24.0,
        event_mae_pct=None,
        stage1_price_anchor=556000,
        stage2_price_anchor=660000,
        stage3_price_anchor=None,
        stage4b_price_anchor=690000,
        stage4c_price_anchor=None,
        extra_price_metrics={"tender_offer_krw_trn": 2.0, "tender_offer_usd_bn": 1.5, "offer_price_krw": 660000, "prior_close_krw": 556000, "reuters_mfe_pct": 19.8, "wsj_mfe_pct": 24.0, "reported_high_krw": 690000, "target_stake_low_pct": 6.98, "target_stake_high_pct": 14.61, "new_share_issue_usd_bn": 1.8, "accounting_fraud_review_flag": True},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="control_premium_before_dilution_accounting_clearance",
        stage_failure_type="false_yellow",
        round_stage_failure_label="governance_dilution_accounting_redteam",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Control premium can be a 4B/watch event, not an operating Green source.",
    ),
    Round282CaseCandidate(
        case_id="r13_loop13_samsung_ea_fadhili_order_not_margin_green",
        symbol="028050",
        company_name="Samsung E&A Fadhili mega-order margin gate",
        primary_archetype=E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN,
        secondary_archetypes=(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN, E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN),
        case_type="success_candidate",
        round_case_type="success_candidate + order-headline 4B-watch",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="mega_EPC_order_needs_margin_working_capital_cash_collection",
        stage4b_status="4B-watch/mega-order-before-margin",
        hard_4c_confirmed=False,
        evidence_fields=("Fadhili_contract_6bn_usd", "total_project_7_7bn_usd", "Samsung_share_77_9pct", "capacity_increase_60pct", "completion_2027_11"),
        red_flag_fields=("order_backlog_headline_only", "EPC_cost_overrun_unbilled_receivables_or_working_capital_stress", "project_margin_cash_conversion_unconfirmed"),
        price_data_source="Reuters order event and analyst target anchors",
        reported_price_anchor="event price 26,750 KRW; event MFE +8.5%; KOSPI -1.4%; target 35,000",
        reported_return_anchor="Order headline is Stage 2 valid, but Green needs EPC margin and cash conversion.",
        event_mfe_pct=8.5,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=26750,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"contract_value_usd_bn": 6.0, "total_project_value_usd_bn": 7.7, "samsung_share_pct": 77.9, "event_price_krw": 26750, "event_mfe_pct": 8.5, "kospi_same_context_pct": -1.4, "relative_outperformance_pp": 9.9, "target_price_krw": 35000, "target_upside_pct": 30.8, "capacity_increase_pct": 60, "expected_completion": "2027-11"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="order_headline_stage2_not_margin_green",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="project_margin_WC_cash_conversion_required",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Mega order can enter Stage 2/watch, but not Green until margin and cash collection are proven.",
    ),
    Round282CaseCandidate(
        case_id="r13_loop13_hyundai_motor_india_ipo_failed_rerating",
        symbol="005380/HYUN.NS",
        company_name="Hyundai Motor India IPO failed parent rerating",
        primary_archetype=E2RArchetype.CAPITAL_RECYCLING_IPO_FAILED_RERATING,
        secondary_archetypes=(E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING, E2RArchetype.IPO_EVENT_PREMIUM),
        case_type="failed_rerating",
        round_case_type="capital recycling IPO failed rerating",
        stage1_date=date(2024, 10, 1),
        stage2_date=date(2024, 10, 14),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 10, 22),
        stage3_decision="subsidiary_IPO_size_needs_parent_ROI_bridge_and_aftermarket_validation",
        stage4b_status="4C-watch/weak-IPO-debut",
        hard_4c_confirmed=False,
        evidence_fields=("IPO_value_3_3bn_usd", "parent_stake_sold_17_5pct", "target_valuation_19bn_usd", "India_share_15pct"),
        red_flag_fields=("IPO_debut_failure_after_valuation_heavy_bookbuilding", "IPO_size_or_oversubscription_only", "parent_ROI_bridge_unconfirmed"),
        price_data_source="Reuters IPO debut anchors",
        reported_price_anchor="offer INR 1,960; listing INR 1,934; morning INR 1,882.10",
        reported_return_anchor="Large subsidiary IPO did not validate parent rerating without aftermarket demand.",
        event_mfe_pct=None,
        event_mae_pct=-6.0,
        stage1_price_anchor=1960,
        stage2_price_anchor=1934,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=1882.10,
        extra_price_metrics={"ipo_value_usd_bn": 3.3, "parent_stake_sold_pct": 17.5, "target_valuation_usd_bn": 19.0, "offer_price_inr": 1960, "listing_price_inr": 1934, "morning_price_inr": 1882.10, "listing_discount_pct": -1.33, "debut_mae_pct": -6.0, "valuation_inr_trn": 1.53, "valuation_usd_bn": 18.2, "india_share_pct": 15, "oversubscription_x": 2.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="capital_recycling_IPO_failed_rerating",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_size_not_parent_ROI_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="Capital recycling IPO needs parent ROIC/FCF and post-listing demand before rerating claims.",
    ),
)


def round282_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND282_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND282_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round282 R13 Loop-13 cross-archetype RedTeam price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=(),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("premium", "ipo", "m&a", "order", "control", "rally", "headline"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("breach", "fatal", "collapse", "custody", "withdrawal", "dilution", "accounting", "weak", "4c"))),
            must_have_fields=ROUND282_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type != "structural_success" else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND282_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_trust_safety_contract_cases",
                "do_not_use_round282_cases_as_candidate_generation_input",
                "do_not_treat_customer_name_IPO_size_control_premium_M&A_or_order_headline_as_green",
                *ROUND282_GREEN_REQUIRED_FIELDS,
                *ROUND282_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.86 if candidate.stage4c_date or candidate.stage4b_date else 0.78,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round282_case_rows() -> tuple[dict[str, str], ...]:
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
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "stage1_price_anchor": _float_text(candidate.stage1_price_anchor),
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
        for candidate in ROUND282_CASE_CANDIDATES
    )


def round282_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND282_SCORE_ADJUSTMENTS)


def round282_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND282_SHADOW_WEIGHT_ROWS)


def round282_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND282_DEEP_SUB_ARCHETYPES)


def round282_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round282_price_validation": "true"} for field in ROUND282_PRICE_VALIDATION_FIELDS)


def round282_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round282_label": label, "canonical_archetype": canonical} for label, canonical in ROUND282_REQUIRED_TARGET_ALIASES.items())


def round282_summary() -> dict[str, int | bool | str]:
    cases = ROUND282_CASE_CANDIDATES
    return {
        "source_round": ROUND282_SOURCE_ROUND_PATH,
        "round_id": ROUND282_ANALYST_ROUND_ID,
        "large_sector": ROUND282_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "event_premium_or_result_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND282_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND282_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND282_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round282_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND282_SOURCE_ROUND_PATH,
        "round_id": ROUND282_ANALYST_ROUND_ID,
        "large_sector": ROUND282_LARGE_SECTOR,
        "summary": round282_summary(),
        "target_aliases": dict(ROUND282_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND282_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND282_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND282_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND282_HARD_4C_GATES),
        "score_adjustments": list(round282_score_adjustment_rows()),
        "shadow_weights": list(round282_shadow_weight_rows()),
        "deep_sub_archetypes": list(round282_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND282_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round282_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_customer_name_IPO_size_control_premium_M&A_or_order_headline_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round282_summary_markdown() -> str:
    summary = round282_summary()
    lines = [
        "# Round 282 R13 Loop 13 Cross-Archetype RedTeam Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- stage4b_watch: {summary['stage4b_watch_count']}",
        f"- stage4c_watch: {summary['stage4c_watch_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND282_CASE_CANDIDATES:
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
            "- SK Telecom and Jeju Air are hard trust/safety 4C examples.",
            "- L&F/Tesla shows customer-name contracts need actual call-off and revenue conversion.",
            "- Digital-asset M&A, IPOs, control premiums, and mega-orders can be 4B/watch or Stage 2, not automatic Green.",
            "- Full adjusted OHLC is still missing; reported event anchors are stored separately from invented MFE/MAE.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round282_green_gate_review_markdown() -> str:
    lines = [
        "# Round 282 R13 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R13 Stage 3-Green is not `customer name`, `IPO size`, `control premium`, `M&A synergy`, or `mega order`. It requires conversion into revenue, margin, cashflow, trust, governance, and post-evidence price validation.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND282_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND282_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND282_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Tesla customer name` is Stage 2 evidence at most until call-off and revenue recognition are confirmed.",
            "- `large IPO oversubscription` needs aftermarket price validation before it supports rerating.",
            "- `mega EPC order` needs project margin, working capital, and cash collection before Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round282_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 282 R13 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND282_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND282_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND282_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round282_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 282 R13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, full MFE/MAE, call-off, custody control, IPO aftermarket demand, EPC margin, or parent ROI where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND282_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND282_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round282_r13_loop13_reports(
    output_directory: str | Path = ROUND282_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND282_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND282_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round282_case_records(), cases_path),
        "audit": _write_json(round282_audit_payload(), audit_path),
        "summary": output / "round282_r13_loop13_price_validation_summary.md",
        "case_matrix": output / "round282_r13_loop13_case_matrix.csv",
        "target_aliases": output / "round282_r13_loop13_target_aliases.csv",
        "score_adjustments": output / "round282_r13_loop13_score_adjustments.csv",
        "shadow_weights": output / "round282_r13_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round282_r13_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round282_r13_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round282_r13_loop13_green_gate_review.md",
        "price_validation_plan": output / "round282_r13_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round282_r13_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round282_summary_markdown(), encoding="utf-8")
    _write_csv(round282_case_rows(), paths["case_matrix"])
    _write_csv(round282_target_alias_rows(), paths["target_aliases"])
    _write_csv(round282_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round282_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round282_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round282_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round282_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round282_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round282_stage4b_4c_review_markdown(), encoding="utf-8")
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


__all__ = [
    "ROUND282_CASE_CANDIDATES",
    "ROUND282_GREEN_FORBIDDEN_PATTERNS",
    "ROUND282_GREEN_REQUIRED_FIELDS",
    "ROUND282_HARD_4C_GATES",
    "ROUND282_LARGE_SECTOR",
    "ROUND282_PRICE_VALIDATION_FIELDS",
    "ROUND282_REQUIRED_TARGET_ALIASES",
    "ROUND282_SHADOW_WEIGHT_ROWS",
    "ROUND282_STAGE4B_WATCH_TRIGGERS",
    "render_round282_green_gate_review_markdown",
    "render_round282_stage4b_4c_review_markdown",
    "round282_audit_payload",
    "round282_case_records",
    "round282_case_rows",
    "round282_deep_sub_archetype_rows",
    "round282_shadow_weight_rows",
    "round282_summary",
    "write_round282_r13_loop13_reports",
]
