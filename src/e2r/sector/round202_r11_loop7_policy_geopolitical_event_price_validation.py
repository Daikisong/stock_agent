"""Round-202 R11 Loop-7 policy/geopolitical/event price-path pack.

Round 202 is a calibration-only layer for Korean policy, geopolitics,
resource discovery, disease, speculative science, market-structure, and
macro-political shock events. The default posture is Event/Watch/RedTeam, not
Green. Large headlines must turn into contracts, budgets, financing, actual
orders, revenue conversion, and EPS/FCF revisions before they can support
higher-stage conviction.

Simple example: an offshore oil and gas exploration approval can move a stock
on the event date. It is not Stage 3-Green until drilling, commerciality,
development cost, sales contract, and cash-flow evidence are visible as-of
the case date.

This module is report/evaluation material only. Production candidate
generation, feature engineering, scoring, staging, and RedTeam code must not
import it.
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


ROUND202_SOURCE_ROUND_PATH = "docs/round/round_202.md"
ROUND202_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round202_r11_loop7_policy_geopolitical_event_price_validation"
ROUND202_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop7_round202.jsonl"
ROUND202_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round202_r11_loop7_policy_geopolitical_event_price_validation_audit.json"

ROUND202_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DOMESTIC_RESOURCE_DISCOVERY_EVENT": E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT.value,
    "ENERGY_SECURITY_POLICY_EVENT": E2RArchetype.ENERGY_SECURITY_POLICY_EVENT.value,
    "EVENT_PRICE_RALLY_NOT_STAGE3": E2RArchetype.EVENT_PRICE_RALLY_NOT_STAGE3.value,
    "POLICY_DIRECTIONALITY_ERROR": E2RArchetype.POLICY_DIRECTIONALITY_ERROR.value,
    "GEOPOLITICAL_RECONSTRUCTION": E2RArchetype.GEOPOLITICAL_RECONSTRUCTION.value,
    "REAL_RECONSTRUCTION_FINANCING": E2RArchetype.REAL_RECONSTRUCTION_FINANCING.value,
    "CRITICAL_INFRA_RECONSTRUCTION_FINANCING": E2RArchetype.CRITICAL_INFRA_RECONSTRUCTION_FINANCING.value,
    "NORTH_KOREA_POLICY_EVENT": E2RArchetype.NORTH_KOREA_POLICY_EVENT.value,
    "CLIMATE_DISASTER_EVENT": E2RArchetype.CLIMATE_DISASTER_EVENT.value,
    "EVENT_DISEASE_PEST_DEMAND": E2RArchetype.EVENT_DISEASE_PEST_DEMAND.value,
    "GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE": E2RArchetype.GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE.value,
    "PUBLIC_HEALTH_PROCUREMENT_REVERSAL": E2RArchetype.PUBLIC_HEALTH_PROCUREMENT_REVERSAL.value,
    "SPECULATIVE_SCIENCE_THEME": E2RArchetype.SPECULATIVE_SCIENCE_THEME.value,
    "ADVANCED_MATERIAL_SPECULATIVE_THEME": E2RArchetype.ADVANCED_MATERIAL_SPECULATIVE_THEME.value,
    "POLICY_LOCAL_THEME": E2RArchetype.POLICY_LOCAL_THEME.value,
    "MARKET_STRUCTURE_SHORT_SELLING_POLICY": E2RArchetype.MARKET_STRUCTURE_SHORT_SELLING_POLICY.value,
    "POLICY_MARKET_SHOCK_EVENT": E2RArchetype.POLICY_MARKET_SHOCK_EVENT.value,
}

ROUND202_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_level_contract_confirmed",
    "budget_or_contract_amount_confirmed",
    "financing_secured",
    "actual_order_or_procurement_award_confirmed",
    "revenue_conversion_confirmed",
    "margin_or_eps_fcf_revision_confirmed",
    "repeat_demand_not_event_fade_confirmed",
    "price_path_after_contract_evidence",
)

ROUND202_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_news_only",
    "mou_only",
    "geopolitical_headline_only",
    "resource_estimate_without_drilling",
    "preprint_or_science_claim_only",
    "disease_import_ban_only",
    "tourist_or_reconstruction_policy_only",
    "market_structure_reform_without_earnings",
    "price_rally_before_contract",
    "event_fade_risk",
    "unfunded_budget",
    "policy_reversal",
)

ROUND202_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND202_HARD_4C_GATES: tuple[str, ...] = (
    "drilling_failure",
    "commerciality_absent",
    "mou_failure",
    "budget_not_funded",
    "policy_reversal",
    "import_restriction_easing_event_fade",
    "independent_replication_failure",
    "regulatory_reversal",
    "political_system_shock",
    "market_access_upgrade_path_failure",
    "contract_cancellation",
    "financing_failure",
)

ROUND202_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
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
    "peak_date",
    "peak_price",
    "MFE_5D",
    "MFE_20D",
    "MFE_30D",
    "MFE_60D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_5D",
    "MAE_20D",
    "MAE_30D",
    "MAE_60D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_policy_event_basket",
    "relative_strength_vs_resource_discovery_basket",
    "relative_strength_vs_nuclear_smr_basket",
    "relative_strength_vs_poultry_basket",
    "relative_strength_vs_speculative_science_basket",
    "event_volume_spike",
    "event_turnover_spike",
    "contract_amount",
    "funded_budget",
    "financing_secured",
    "actual_order",
    "revenue_conversion",
    "eps_fcf_revision",
    "drilling_result",
    "commerciality_confirmed",
    "replication_result",
    "import_restriction_status",
    "policy_reversal_flag",
    "macro_fx_shock",
    "foreign_outflow",
    "liquidity_support",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round202ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "axis": self.axis,
            "points": str(self.points),
            "direction": self.direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round202CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
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
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.POLICY_GEOPOLITICAL_EVENT

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND202_SCORE_ADJUSTMENTS: tuple[Round202ScoreAdjustment, ...] = (
    Round202ScoreAdjustment("funded_budget", 5, "raise", "R11 이벤트는 예산이 붙어야 회사 단위 증거가 된다."),
    Round202ScoreAdjustment("actual_contract", 5, "raise", "정책·MOU는 실제 계약으로 승격될 때만 강해진다."),
    Round202ScoreAdjustment("revenue_conversion", 5, "raise", "계약이 매출 인식으로 내려와야 Stage 3 후보가 된다."),
    Round202ScoreAdjustment("financing_secured", 4, "raise", "재건·인프라·원전 이벤트는 financing 확인이 필요하다."),
    Round202ScoreAdjustment("government_stockpile_order", 4, "raise", "정부 비축/조달은 실제 order와 guidance가 있어야 한다."),
    Round202ScoreAdjustment("procurement_award", 4, "raise", "발주·조달계약은 단순 headline보다 강한 Stage 2 증거다."),
    Round202ScoreAdjustment("commerciality_confirmed", 4, "raise", "자원 발견은 상업성이 확인되어야 현금흐름 후보가 된다."),
    Round202ScoreAdjustment("independent_replication_or_validation", 4, "raise", "과학/신소재 claim은 독립 검증 전까지 Stage 1이다."),
    Round202ScoreAdjustment("event_to_contract_escalation", 4, "raise", "이벤트가 계약으로 승격되는 순간을 따로 보상한다."),
    Round202ScoreAdjustment("policy_durability", 3, "raise", "정책 지속성과 예산 집행 가능성이 있어야 event fade를 줄인다."),
    Round202ScoreAdjustment("policy_news_only", -5, "lower", "정책 뉴스만으로 Stage 3-Green을 만들지 않는다."),
    Round202ScoreAdjustment("mou_only", -5, "lower", "MOU는 계약이 아니며 revenue conversion 전까지 Watch다."),
    Round202ScoreAdjustment("geopolitical_headline_only", -5, "lower", "지정학 headline은 회사 단위 계약 전까지 event premium이다."),
    Round202ScoreAdjustment("resource_estimate_without_drilling", -5, "lower", "매장 가능성은 시추·상업성 전까지 Green 금지다."),
    Round202ScoreAdjustment("preprint_or_science_claim_only", -5, "lower", "preprint와 과학 claim은 독립 재현 전까지 Green 금지다."),
    Round202ScoreAdjustment("disease_import_ban_only", -4, "lower", "질병·수입금지는 마진 확인 전까지 one-off event다."),
    Round202ScoreAdjustment("tourist_or_reconstruction_policy_only", -4, "lower", "관광·재건 정책은 funded order 전까지 제한한다."),
    Round202ScoreAdjustment("market_structure_reform_without_earnings", -3, "lower", "시장구조 개선은 기업 EPS 전까지 개별 Green이 아니다."),
    Round202ScoreAdjustment("price_rally_before_contract", -5, "lower", "계약 전 가격 급등은 4B-watch 우선이다."),
    Round202ScoreAdjustment("event_fade_risk", -4, "lower", "후속 evidence 없는 이벤트는 drawdown 위험을 크게 본다."),
)


ROUND202_CASE_CANDIDATES: tuple[Round202CaseCandidate, ...] = (
    Round202CaseCandidate(
        case_id="kogas_east_sea_resource_discovery_event_premium",
        symbol="036460",
        company_name="한국가스공사",
        primary_archetype=E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT,
        secondary_archetypes=(
            E2RArchetype.ENERGY_SECURITY_POLICY_EVENT,
            E2RArchetype.EVENT_PRICE_RALLY_NOT_STAGE3,
            E2RArchetype.RESOURCE_EXPLORATION_DRILL_BIT_GATE,
        ),
        case_type="event_premium",
        stage1_date=date(2024, 6, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2024, 6, 3),
        stage4c_date=None,
        stage3_decision="blocked_until_drilling_commerciality_development_cost_sales_contract_and_cash_flow_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("east_sea_oil_gas_exploration_approval", "14bn_barrel_possible_resource_claim", "20pct_success_probability", "intraday_price_surge"),
        red_flag_fields=("resource_estimate_without_drilling", "commerciality_unknown", "development_cost_unknown", "revenue_conversion_absent"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="needs_ohlc_backfill",
        notes="Resource discovery approval is Stage 1/event premium; commercial drilling and cash-flow evidence are required before Stage 3.",
    ),
    Round202CaseCandidate(
        case_id="doosan_enerbility_nuclear_smr_policy_to_contract_watch",
        symbol="034020",
        company_name="두산에너빌리티",
        primary_archetype=E2RArchetype.ENERGY_SECURITY_POLICY_EVENT,
        secondary_archetypes=(
            E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
            E2RArchetype.EVENT_TO_CONTRACT_ESCALATION,
            E2RArchetype.MOU_LOI_NOT_CONTRACT,
        ),
        case_type="success_candidate",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2025, 8, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_final_contract_equipment_order_backlog_margin_cash_flow_and_eps_revision_are_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("czech_nuclear_preferred_bidder", "x_energy_aws_smr_cooperation", "fermi_ai_power_equipment_supply_agreement", "nuclear_export_recovery_theme"),
        red_flag_fields=("preferred_bidder_not_final_contract", "mou_only", "financing_unverified", "equipment_backlog_unverified"),
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Nuclear/SMR policy can reach Stage 2, but Green waits for final contract, equipment backlog, margin, and EPS revision.",
    ),
    Round202CaseCandidate(
        case_id="hdhyundai_samsungheavy_us_shipbuilding_policy_mou_watch",
        symbol="267250|010140",
        company_name="HD현대 / 삼성중공업",
        primary_archetype=E2RArchetype.GEOPOLITICAL_RECONSTRUCTION,
        secondary_archetypes=(
            E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY,
            E2RArchetype.MOU_LOI_NOT_CONTRACT,
            E2RArchetype.EVENT_TO_CONTRACT_ESCALATION,
        ),
        case_type="success_candidate",
        stage1_date=date(2025, 8, 26),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 8, 26),
        stage4c_date=None,
        stage3_decision="blocked_until_funded_order_contract_amount_duration_margin_delivery_schedule_and_revenue_conversion_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_shipbuilding_policy_package", "hdhyundai_cerberus_mou", "samsung_heavy_vigor_preliminary_deal", "mro_shipyard_modernization_theme"),
        red_flag_fields=("mou_only", "geopolitical_headline_only", "funded_order_absent", "delivery_schedule_unverified"),
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="U.S. shipbuilding policy is useful attention evidence, but MOU/preliminary deal must become funded orders before Green.",
    ),
    Round202CaseCandidate(
        case_id="poultry_basket_brazil_bird_flu_import_ban_event_fade",
        symbol="BASKET",
        company_name="하림 / 마니커류 poultry basket",
        primary_archetype=E2RArchetype.EVENT_DISEASE_PEST_DEMAND,
        secondary_archetypes=(
            E2RArchetype.LIVESTOCK_DISEASE_PRICE_EVENT_KOREA,
            E2RArchetype.PUBLIC_HEALTH_PROCUREMENT_REVERSAL,
            E2RArchetype.EVENT_PRICE_RALLY_NOT_STAGE3,
        ),
        case_type="event_premium",
        stage1_date=date(2025, 5, 19),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 5, 19),
        stage4c_date=date(2025, 6, 23),
        stage3_decision="blocked_until_company_level_price_pass_through_volume_margin_feed_cost_inventory_and_repeat_demand_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("brazil_bird_flu_import_restriction", "domestic_poultry_substitution_theme", "short_term_supply_disruption", "regional_ban_easing"),
        red_flag_fields=("disease_import_ban_only", "import_restriction_easing_event_fade", "feed_cost_unverified", "margin_unverified"),
        score_price_alignment="unknown",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="needs_ohlc_backfill",
        notes="Disease/import-ban events can create short MFE, but company margin and repeat demand are required before higher-stage use.",
    ),
    Round202CaseCandidate(
        case_id="lk99_superconductor_speculative_science_thesis_break",
        symbol="BASKET",
        company_name="LK-99 초전도체 basket",
        primary_archetype=E2RArchetype.SPECULATIVE_SCIENCE_THEME,
        secondary_archetypes=(
            E2RArchetype.ADVANCED_MATERIAL_SPECULATIVE_THEME,
            E2RArchetype.EVENT_PRICE_RALLY_NOT_STAGE3,
            E2RArchetype.THEME_VALUATION_OVERHEAT,
        ),
        case_type="overheat",
        stage1_date=date(2023, 7, 22),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2023, 8, 1),
        stage4c_date=date(2023, 8, 15),
        stage3_decision="hard_blocked_by_preprint_only_no_independent_replication_no_commercial_contract_and_replication_failure",
        stage4b_status="elevated",
        hard_4c_confirmed=True,
        evidence_fields=("lk99_arxiv_preprint", "room_temperature_superconductor_claim", "speculative_science_rally", "replication_failure"),
        red_flag_fields=("preprint_or_science_claim_only", "independent_replication_failure", "commercial_path_absent", "price_rally_before_contract"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Speculative science preprints are Stage 1 at most; failed replication is a thesis break.",
    ),
    Round202CaseCandidate(
        case_id="korea_martial_law_policy_market_shock_overlay",
        symbol="KOSPI",
        company_name="2024 계엄·정치 shock",
        primary_archetype=E2RArchetype.POLICY_MARKET_SHOCK_EVENT,
        secondary_archetypes=(E2RArchetype.POLITICAL_SYSTEM_SHOCK_KOREA, E2RArchetype.POLICY_MARKET_SHOCK_OVERLAY),
        case_type="4b_watch",
        stage1_date=date(2024, 12, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 4),
        stage3_decision="macro_overlay_only_not_company_stage3_evidence",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("martial_law_declaration_and_reversal", "kospi_drawdown", "krw_weakness", "liquidity_support_watch"),
        red_flag_fields=("political_system_shock", "macro_risk_premium", "foreign_outflow_risk", "fx_volatility"),
        score_price_alignment="unknown",
        rerating_result="no_rerating",
        stage_failure_type="unknown",
        price_validation_status="needs_ohlc_backfill",
        notes="Political shock is a macro RedTeam overlay; it should not directly create or remove company Stage 3 without company evidence.",
    ),
    Round202CaseCandidate(
        case_id="short_selling_msci_market_structure_stage2_watch",
        symbol="BROAD_MARKET",
        company_name="공매도 재개 / MSCI 접근성",
        primary_archetype=E2RArchetype.MARKET_STRUCTURE_SHORT_SELLING_POLICY,
        secondary_archetypes=(E2RArchetype.SHORT_SELLING_RESUMPTION_RISK, E2RArchetype.POLICY_MARKET_SHOCK_EVENT),
        case_type="success_candidate",
        stage1_date=date(2025, 3, 31),
        stage2_date=date(2025, 6, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_foreign_inflow_trading_value_broker_earnings_market_multiple_and_msci_upgrade_path_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("short_selling_full_resumption", "msci_market_accessibility_improved", "developed_market_watch_expectation", "foreign_access_reform"),
        red_flag_fields=("market_structure_reform_without_earnings", "fx_access_constraint_remaining", "upgrade_path_failure_watch", "policy_reversal_watch"),
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Market-structure reform can support the market frame, but individual Green needs earnings, inflow, and trading-value evidence.",
    ),
)


def round202_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND202_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round202 R11 Loop-7 policy/geopolitical/event price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "claim" in field
                or "approval" in field
                or "theme" in field
                or "policy" in field
                or "preprint" in field
                or "shock" in field
                or "resumption" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "contract" in field or "order" in field or "revenue" in field or "eps" in field or "cash" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "rally" in field or "surge" in field or "price" in field or "theme" in field or "mou" in field or "headline" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "failure" in field
                or "fade" in field
                or "shock" in field
                or "reversal" in field
                or "commerciality" in field
                or "replication" in field
                or "financing" in field
            ),
            must_have_fields=ROUND202_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={
                "funded_budget_delta": 5.0,
                "actual_contract_delta": 5.0,
                "revenue_conversion_delta": 5.0,
                "financing_secured_delta": 4.0,
                "commerciality_confirmed_delta": 4.0,
                "independent_replication_or_validation_delta": 4.0,
                "policy_news_only_delta": -5.0,
                "mou_only_delta": -5.0,
                "resource_estimate_without_drilling_delta": -5.0,
                "preprint_or_science_claim_only_delta": -5.0,
                "price_rally_before_contract_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "r11_default_stage3_bias_conservative",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_mou_resource_disease_science_or_market_structure_headline_as_green_evidence",
                *ROUND202_GREEN_REQUIRED_FIELDS,
                *ROUND202_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4c_date else 0.55,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round202_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND202_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
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
                "score_price_alignment": candidate.score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round202_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND202_SCORE_ADJUSTMENTS)


def round202_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round202_backfill": "true"} for field in ROUND202_PRICE_BACKFILL_FIELDS)


def round202_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round202_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND202_REQUIRED_TARGET_ALIASES.items()
    )


def round202_summary() -> dict[str, int | bool | str]:
    cases = round202_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND202_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND202_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND202_PRICE_BACKFILL_FIELDS),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in ROUND202_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND202_CASE_CANDIDATES if case.stage3_date),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND202_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "needs_ohlc_backfill_count": sum(
            1 for case in ROUND202_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"
        ),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
        "r11_default_stage3_bias": "conservative",
    }


def write_round202_r11_loop7_reports(
    *,
    output_directory: str | Path = ROUND202_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND202_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND202_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round202_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round202_r11_loop7_price_validation_summary.md",
        "case_matrix": output / "round202_r11_loop7_case_matrix.csv",
        "target_aliases": output / "round202_r11_loop7_target_aliases.csv",
        "score_adjustments": output / "round202_r11_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round202_r11_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round202_r11_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round202_r11_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round202_r11_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round202_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round202_case_rows(), paths["case_matrix"])
    _write_rows(round202_target_alias_rows(), paths["target_aliases"])
    _write_rows(round202_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round202_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round202_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round202_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round202_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round202_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round202_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND202_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value,
        "summary": round202_summary(),
        "target_aliases": list(round202_target_alias_rows()),
        "green_required_fields": list(ROUND202_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND202_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND202_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND202_HARD_4C_GATES),
        "score_adjustments": list(round202_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND202_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round202_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_policy_mou_resource_disease_science_market_structure_or_geopolitical_headline_as_green_evidence",
            "do_not_invent_contract_budget_financing_orders_revenue_eps_fcf_or_stage_prices",
            "keep_r11_default_stage3_bias_conservative",
        ],
    }


def render_round202_summary_markdown() -> str:
    summary = round202_summary()
    lines = [
        "# Round-202 R11 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND202_SOURCE_ROUND_PATH}`",
        "- large_sector: `POLICY_GEOPOLITICAL_EVENT`",
        "- scope: resource discovery, nuclear/SMR policy, shipbuilding MOU, disease demand, speculative science, political shock, and market-structure events",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- overheat_count: {summary['overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- needs_ohlc_backfill_count: {summary['needs_ohlc_backfill_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- needs_ohlc_backfill: true",
        "- r11_default_stage3_bias: conservative",
        "",
        "## Interpretation",
        "",
        "- R11은 대부분 Stage 3가 아니라 Event/Watch/RedTeam이다.",
        "- 한국가스공사 동해 가스 이벤트는 강한 Stage 1이지만 시추·상업성 전 Green이 아니다.",
        "- 두산에너빌리티 원전·SMR은 Stage 2 후보지만 final contract와 장비 backlog 전 Green이 아니다.",
        "- HD현대·삼성중공업 미국 조선정책 MOU는 funded order 전 Stage 3가 아니다.",
        "- 조류독감 poultry basket은 단기 MFE가 가능하지만 수입제한 완화가 event fade가 될 수 있다.",
        "- LK-99는 speculative science hard 반례이며 failed replication은 thesis break다.",
        "- 계엄·정치 shock은 개별 기업 Stage가 아니라 macro RedTeam overlay다.",
        "- 공매도·MSCI 접근성은 시장구조 Stage 2 watch지만 개별 기업 EPS 전 Green이 아니다.",
        "",
        "쉬운 예: `as_of_date=2024-06-03`에 동해 가스 뉴스로 주가가 급등해도, 시추 성공과 상업성이 없으면 Stage 3-Green이 아니라 4B-watch다.",
    ]
    return "\n".join(lines) + "\n"


def render_round202_green_gate_review_markdown() -> str:
    lines = [
        "# Round-202 R11 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND202_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND202_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND202_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round202 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent contract, budget, financing, order, revenue, EPS/FCF, stage prices, or MFE/MAE.",
            "- Do not treat policy news, MOU, resource discovery, disease event, science preprint, or market-structure reform as Green evidence alone.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round202_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-202 R11 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND202_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND202_CASE_CANDIDATES:
        stage_marker = case.stage3_date or case.stage2_date or case.stage4b_date or case.stage4c_date or case.stage1_date
        lines.append(
            f"| `{case.case_id}` | {_date_text(stage_marker) or 'undated'} | "
            f"{case.price_validation_status} | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use official OHLC data for exact MFE/MAE.",
            "- R11 needs short-window MFE/MAE: 5D, 20D, and 60D matter because event fade can be fast.",
            "- Keep unknown values null or `needs_ohlc_backfill`.",
            "- Split event date, contract date, failure/reversal date, and market-shock date.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round202_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-202 R11 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: headline, policy, MOU, resource estimate, disease, science claim, or market-structure news moves price before contracts.",
        "- `elevated`: follow-up evidence is absent while valuation and turnover remain high.",
        "- `graduated`: additional news stops moving price and event premium fades.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND202_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## R11 Interpretation",
            "",
            "- drilling failure or commerciality absence breaks resource-discovery narratives.",
            "- MOU failure, unfunded budget, or financing failure breaks policy-to-contract paths.",
            "- disease import-ban easing can quickly fade one-off demand.",
            "- independent replication failure is hard 4C for speculative science themes.",
            "- political system shock is a macro overlay, not company Green evidence.",
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C confirmed | interpretation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for case in ROUND202_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


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


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


__all__ = [
    "ROUND202_CASE_CANDIDATES",
    "ROUND202_DEFAULT_AUDIT_PATH",
    "ROUND202_DEFAULT_CASES_PATH",
    "ROUND202_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND202_GREEN_FORBIDDEN_PATTERNS",
    "ROUND202_GREEN_REQUIRED_FIELDS",
    "ROUND202_HARD_4C_GATES",
    "ROUND202_PRICE_BACKFILL_FIELDS",
    "ROUND202_REQUIRED_TARGET_ALIASES",
    "ROUND202_SCORE_ADJUSTMENTS",
    "ROUND202_SOURCE_ROUND_PATH",
    "ROUND202_STAGE4B_STATUSES",
    "Round202CaseCandidate",
    "Round202ScoreAdjustment",
    "render_round202_green_gate_review_markdown",
    "render_round202_price_backfill_plan_markdown",
    "render_round202_stage4b_4c_review_markdown",
    "render_round202_summary_markdown",
    "round202_audit_payload",
    "round202_case_records",
    "round202_case_rows",
    "round202_price_backfill_field_rows",
    "round202_score_adjustment_rows",
    "round202_summary",
    "round202_target_alias_rows",
    "write_round202_r11_loop7_reports",
]
