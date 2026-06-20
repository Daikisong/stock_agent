"""Select v12 Green rows that should become runtime replay fixtures."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import json
import re

from .evidence_flags import normalise_evidence_quality_flags
from .taxonomy import ARCHETYPE_TO_LARGE_SECTOR, CANONICAL_ARCHETYPE_IDS


GREEN_TRIGGER_TYPES = {"Stage3-Green"}
GREEN_EQUIVALENT_TRIGGER_TYPES = {"Stage2-Actionable", "Stage3-Yellow"}
GUARD_TRIGGER_PREFIXES = ("Stage2-FalsePositive", "Stage3-FalseGreen", "Price-only", "PriceOnly")
GUARD_TRIGGER_TYPES = {
    "Stage4B",
    "Stage4C",
    "4B",
    "4C",
    "R13-4B4CRedTeam",
    "R13-AccountingTrustPriceValidation",
    "R13-Stage2FalsePositiveReview",
}
GUARD_CASE_TYPES = {"one_off", "overheat", "failed_rerating", "4c_thesis_break", "boom_bust"}
GREEN_GUARD_MARKERS = (
    "false_green",
    "false-positive",
    "false_positive",
    "falsepositive",
    "false_stage",
    "false_stage2",
    "policy_only",
    "policyonly",
    "headline_only",
)
GREEN_EQUIVALENT_POSITIVE_MARKERS = (
    "structural_success",
    "positive",
    "missed_structural",
    "too_late",
    "large_mfe_success",
    "direct_supply_tightness_positive",
    "direct_project_bridge_positive",
    "named_sk_hynix",
    "repeat_export_order_to_large_mfe_success",
)
GREEN_EQUIVALENT_BLOCK_MARKERS = (
    "counterexample",
    "false_positive",
    "false-positive",
    "false_green",
    "hard4c",
    "hard_4c",
    "contract_delay",
    "calloff",
    "call-off",
    "margin_or_asp_gap",
    "margin_bridge_unconfirmed",
    "shipment_or_revenue_margin_bridge_missing",
    "local_4b_watch_guard",
    "stage3-green이 아니라",
    "not stage3-green",
    "no separate stage3-green",
)

SOURCE_GREEN_PRIMITIVES_BY_ARCHETYPE: dict[str, tuple[str, ...]] = {
    "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": (
        "export_contract",
        "government_customer",
        "contract_amount_to_prior_sales",
        "contract_duration_months",
        "customer_contract_visible",
        "record_backlog",
        "delivery_schedule",
        "order_to_revenue_bridge",
        "margin_bridge_visible",
        "medium_term_revision_visibility",
    ),
    "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY": (
        "policy_or_regulatory_confirmed",
        "project_award_confirmed",
        "legal_overhang_removed",
        "project_export_route_reopened",
        "direct_company_cash_route",
        "direct_revenue_route",
        "implementation_timeline",
        "official_contract",
        "customer_contract_visible",
        "contract_amount_to_prior_sales",
        "contract_duration_months",
        "government_customer",
        "order_to_revenue_bridge",
        "margin_bridge_visible",
        "medium_term_revision_visibility",
    ),
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH": (
        "hbm_customer_order",
        "customer_contract_visible",
        "equipment_order_backlog",
        "advanced_packaging_bottleneck",
        "relative_strength_score",
        "order_to_revenue_bridge",
        "margin_bridge_visible",
        "medium_term_revision_visibility",
        "capacity_constraint",
    ),
    "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY": (
        "offtake_contract",
        "supply_shortage",
        "named_counterparty_TC_benchmark",
        "zinc_concentrate_supply_tightness",
        "direct_smelter_economics",
        "policy_supply_support",
        "direct_company_cash_route",
        "direct_revenue_route",
        "margin_bridge_visible",
        "medium_term_revision_visibility",
        "pricing_power_confirmed",
    ),
}
SOURCE_GREEN_REQUIRED_MARKERS_BY_ARCHETYPE: dict[str, tuple[str, ...]] = {
    "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": (
        "repeat_export",
        "export_order",
        "export deal",
        "iraq",
        "m-sam",
    ),
    "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY": (
        "legal_overhang_removed",
        "westinghouse",
        "settlement",
        "direct_project_bridge_positive",
    ),
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH": (
        "named_sk_hynix",
        "sk hynix",
        "tc_bonder",
        "tc-bonder",
    ),
    "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY": (
        "tc_benchmark",
        "teck",
        "zinc_concentrate",
        "direct_smelter",
        "direct_supply_tightness_positive",
    ),
}

ARCHETYPE_RUNTIME_BRIDGE_SPECS: dict[str, dict[str, Any]] = {
    "C01_ORDER_BACKLOG_MARGIN_BRIDGE": {
        "runtime_bridge_group": "industrial_backlog_margin_bridge",
        "expected_runtime_primitives": (
            "order_backlog_to_sales",
            "named_customer_quality",
            "contract_quality",
            "delivery_schedule",
            "opm_expansion_pctp",
            "fcf_quality_score",
        ),
    },
    "C02_POWER_GRID_DATACENTER_CAPEX": {
        "runtime_bridge_group": "industrial_backlog_margin_bridge",
        "expected_runtime_primitives": (
            "datacenter_customer",
            "order_backlog_to_sales",
            "lead_time_extended",
            "capacity_constraint",
            "pricing_power_confirmed",
        ),
    },
    "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": {
        "runtime_bridge_group": "industrial_backlog_margin_bridge",
        "expected_runtime_primitives": (
            "export_contract",
            "government_customer",
            "order_backlog_to_sales",
            "delivery_schedule",
            "cost_overrun",
        ),
    },
    "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY": {
        "runtime_bridge_group": "policy_project_cash_bridge",
        "expected_runtime_primitives": (
            "policy_or_regulatory_confirmed",
            "project_award_confirmed",
            "permit_or_legal_delay",
            "direct_company_cash_route",
            "cost_overrun",
        ),
    },
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": {
        "runtime_bridge_group": "industrial_backlog_margin_bridge",
        "expected_runtime_primitives": (
            "contract_amount_to_prior_sales",
            "contract_duration_months",
            "margin_bridge_visible",
            "cost_overrun",
            "delivery_schedule",
        ),
    },
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY": {
        "runtime_bridge_group": "semiconductor_customer_capacity_bridge",
        "expected_runtime_primitives": (
            "customer_preorder_or_allocation",
            "revenue_visibility_contract",
            "hbm_capacity_constraint",
            "hbm_capacity_pre_sold",
            "memory_price_increase_mentioned",
            "medium_term_revision_visibility",
        ),
    },
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH": {
        "runtime_bridge_group": "semiconductor_customer_capacity_bridge",
        "expected_runtime_primitives": (
            "hbm_customer_order",
            "customer_contract_visible",
            "equipment_order_backlog",
            "advanced_packaging_bottleneck",
            "relative_strength_score",
            "order_to_revenue_bridge",
        ),
    },
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": {
        "runtime_bridge_group": "semiconductor_customer_capacity_bridge",
        "expected_runtime_primitives": (
            "named_customer_quality",
            "qualification_confirmed",
            "repeat_order_confirmed",
            "socket_or_test_demand_visible",
            "margin_bridge_visible",
        ),
    },
    "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF": {
        "runtime_bridge_group": "valuation_blowoff_guard_bridge",
        "expected_runtime_primitives": (
            "valuation_overheat",
            "price_only_blowoff",
            "order_to_revenue_bridge",
            "customer_quality_visible",
            "capex_cycle_risk",
        ),
    },
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": {
        "runtime_bridge_group": "semiconductor_memory_recovery_bridge",
        "expected_runtime_primitives": (
            "memory_price_increase_mentioned",
            "supply_discipline_mentioned",
            "cycle_demand_visibility",
            "end_market_demand_visibility",
            "supply_demand_tightness",
            "cycle_to_revenue_bridge",
            "advanced_packaging_bottleneck",
            "equipment_order_recovery",
            "order_to_revenue_bridge",
            "inventory_cycle_repair",
            "fcf_quality_score",
        ),
    },
    "C11_BATTERY_ORDERBOOK_RERATING": {
        "runtime_bridge_group": "battery_mobility_contract_bridge",
        "expected_runtime_primitives": (
            "order_backlog_to_sales",
            "customer_contract",
            "call_off_risk",
            "ex_credit_margin",
            "fcf_quality_score",
        ),
    },
    "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK": {
        "runtime_bridge_group": "battery_mobility_contract_bridge",
        "expected_runtime_primitives": (
            "customer_contract",
            "call_off_risk",
            "customer_capex_decline",
            "contract_cancelled_or_delayed",
            "volume_visibility",
        ),
    },
    "C13_BATTERY_JV_UTILIZATION_AMPC_IRA": {
        "runtime_bridge_group": "battery_mobility_contract_bridge",
        "expected_runtime_primitives": (
            "jv_utilization",
            "ampc_or_subsidy_capture",
            "ex_credit_margin",
            "customer_contract",
            "policy_reversal_risk",
        ),
    },
    "C14_EV_DEMAND_SLOWDOWN_4B_4C": {
        "runtime_bridge_group": "battery_mobility_contract_bridge",
        "expected_runtime_primitives": (
            "ev_demand_slowdown",
            "inventory_spike",
            "price_cut_risk",
            "customer_capex_decline",
            "thesis_break_confirmed",
        ),
    },
    "C15_MATERIAL_SPREAD_SUPERCYCLE": {
        "runtime_bridge_group": "materials_spread_supply_bridge",
        "expected_runtime_primitives": (
            "spread_expansion",
            "utilization_rate",
            "inventory_cycle",
            "pricing_power_confirmed",
            "fcf_quality_score",
        ),
    },
    "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY": {
        "runtime_bridge_group": "materials_spread_supply_bridge",
        "expected_runtime_primitives": (
            "offtake_contract",
            "supply_shortage",
            "policy_supply_support",
            "permit_status",
            "direct_company_cash_route",
        ),
    },
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": {
        "runtime_bridge_group": "materials_spread_supply_bridge",
        "expected_runtime_primitives": (
            "spread_expansion",
            "raw_material_cost_risk",
            "utilization_rate",
            "inventory_cycle",
            "opm_expansion_pctp",
        ),
    },
    "C18_CONSUMER_EXPORT_CHANNEL_REORDER": {
        "runtime_bridge_group": "consumer_sellthrough_reorder_bridge",
        "expected_runtime_primitives": (
            "export_growth_pct",
            "sell_through_confirmed",
            "repeat_order_confirmed",
            "channel_reorder_confirmed",
            "opm_expansion_pctp",
        ),
    },
    "C19_BRAND_RETAIL_INVENTORY_MARGIN": {
        "runtime_bridge_group": "consumer_sellthrough_reorder_bridge",
        "expected_runtime_primitives": (
            "inventory_spike",
            "sell_through_confirmed",
            "pricing_power_confirmed",
            "channel_reorder_confirmed",
            "raw_material_cost_risk",
        ),
    },
    "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION": {
        "runtime_bridge_group": "consumer_sellthrough_reorder_bridge",
        "expected_runtime_primitives": (
            "export_growth_pct",
            "platform_distribution_scale",
            "brand_customer_diversification",
            "repeat_order_confirmed",
            "high_margin_mix_improvement",
        ),
    },
    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN": {
        "runtime_bridge_group": "financial_capital_return_bridge",
        "expected_runtime_primitives": (
            "roe",
            "pbr_e",
            "treasury_share_cancellation",
            "capital_return_execution",
            "credit_cost_quality",
        ),
    },
    "C22_INSURANCE_RATE_CYCLE_RESERVE": {
        "runtime_bridge_group": "insurance_reserve_capital_bridge",
        "expected_runtime_primitives": (
            "csm_growth_visible",
            "k_ics_ratio",
            "reserve_quality_visible",
            "loss_ratio_quality",
            "capital_return_execution",
        ),
    },
    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION": {
        "runtime_bridge_group": "bio_commercialization_reimbursement_bridge",
        "expected_runtime_primitives": (
            "regulatory_approval_confirmed",
            "approval_to_revenue_bridge",
            "royalty_route",
            "partner_economics_visible",
            "reimbursement_confirmed",
        ),
    },
    "C24_BIO_TRIAL_DATA_EVENT_RISK": {
        "runtime_bridge_group": "bio_commercialization_reimbursement_bridge",
        "expected_runtime_primitives": (
            "trial_quality_visible",
            "binary_event_unresolved",
            "approval_not_confirmed",
            "safety_signal",
            "cash_runway_risk",
        ),
    },
    "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT": {
        "runtime_bridge_group": "bio_commercialization_reimbursement_bridge",
        "expected_runtime_primitives": (
            "reimbursement_confirmed",
            "procedure_volume_growth",
            "export_growth_pct",
            "consumable_repeat_revenue",
            "gross_margin_bridge",
        ),
    },
    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE": {
        "runtime_bridge_group": "software_platform_recurring_revenue_bridge",
        "expected_runtime_primitives": (
            "arpu_growth_pct",
            "ad_revenue_growth_pct",
            "take_rate_improvement",
            "operating_leverage_visible",
            "regulatory_risk",
        ),
    },
    "C27_CONTENT_IP_GLOBAL_MONETIZATION": {
        "runtime_bridge_group": "software_platform_recurring_revenue_bridge",
        "expected_runtime_primitives": (
            "ip_monetization_visible",
            "global_launch_conversion",
            "repeat_revenue",
            "user_retention",
            "token_or_theme_hype_risk",
        ),
    },
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION": {
        "runtime_bridge_group": "software_platform_recurring_revenue_bridge",
        "expected_runtime_primitives": (
            "arr_growth_visible",
            "nrr",
            "retention_or_renewal",
            "rpo_to_sales",
            "recurring_margin_leverage",
        ),
    },
    "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": {
        "runtime_bridge_group": "battery_mobility_contract_bridge",
        "expected_runtime_primitives": (
            "volume_growth_visible",
            "mix_improvement",
            "operating_leverage_visible",
            "pricing_power_confirmed",
            "fcf_quality_score",
        ),
    },
    "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK": {
        "runtime_bridge_group": "construction_pf_cash_bridge",
        "expected_runtime_primitives": (
            "pf_exposure_reduced",
            "balance_sheet_repair",
            "cash_collection_visible",
            "occupancy_or_presale_visible",
            "funding_cost_risk",
        ),
    },
    "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": {
        "runtime_bridge_group": "policy_project_cash_bridge",
        "expected_runtime_primitives": (
            "policy_or_regulatory_confirmed",
            "direct_company_cash_route",
            "subsidy_capture_visible",
            "implementation_timeline",
            "policy_headline_only",
        ),
    },
    "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP": {
        "runtime_bridge_group": "governance_tender_cash_bridge",
        "expected_runtime_primitives": (
            "tender_offer_confirmed",
            "minority_cash_path",
            "control_premium_floor",
            "regulatory_approval_confirmed",
            "event_spread_risk",
        ),
    },
    "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW": {
        "runtime_bridge_group": "cross_archetype_guard_bridge",
        "expected_runtime_primitives": (
            "price_only_blowoff",
            "policy_headline_only",
            "evidence_source_quality",
            "missing_cashflow_bridge",
            "theme_hype_without_revenue",
        ),
    },
    "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM": {
        "runtime_bridge_group": "cross_archetype_guard_bridge",
        "expected_runtime_primitives": (
            "thesis_break_confirmed",
            "contract_cancelled_or_delayed",
            "revision_slowdown",
            "accounting_trust_risk",
            "valuation_overheat",
        ),
    },
    "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION": {
        "runtime_bridge_group": "cross_archetype_guard_bridge",
        "expected_runtime_primitives": (
            "auditor_or_disclosure_risk",
            "restatement_risk",
            "share_count_drift",
            "price_only_blowoff",
            "source_quality_conflict",
        ),
    },
    "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL": {
        "runtime_bridge_group": "cross_archetype_guard_bridge",
        "expected_runtime_primitives": (
            "high_mae_history",
            "valuation_overheat",
            "liquidity_or_microcap_risk",
            "execution_risk_score",
            "positioning_reversal_risk",
        ),
    },
}

DEFAULT_RUNTIME_BRIDGE_SPEC = {
    "runtime_bridge_group": "generic_research_to_runtime_bridge",
    "expected_runtime_primitives": (
        "margin_bridge_visible",
        "customer_quality_visible",
        "backlog_visibility",
        "contract_quality",
        "guard_risk",
    ),
}
SEMANTIC_TOKEN_STOPWORDS = {
    "and",
    "bridge",
    "confirmed",
    "green",
    "risk",
    "score",
    "stage",
    "visible",
    "visibility",
}


def _read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _marker_text(row: dict[str, Any]) -> str:
    return " ".join(
        str(row.get(key) or "")
        for key in (
            "case_id",
            "trigger_id",
            "trigger_type",
            "case_type",
            "positive_or_counterexample",
            "evidence_available_at_that_date",
            "evidence_source",
        )
    ).lower()


def _has_green_guard_marker(row: dict[str, Any]) -> bool:
    text = _marker_text(row)
    return any(marker in text for marker in GREEN_GUARD_MARKERS)


def _is_raw_green_trigger(row: dict[str, Any]) -> bool:
    return str(row.get("trigger_type") or "") in GREEN_TRIGGER_TYPES


def _as_text(value: Any) -> str:
    if isinstance(value, list):
        return " ".join(_as_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{key} {_as_text(item)}" for key, item in value.items())
    return str(value or "")


def _green_equivalent_positive_text(row: dict[str, Any]) -> str:
    return " ".join(
        _as_text(row.get(key))
        for key in (
            "case_id",
            "trigger_id",
            "trigger_type",
            "case_type",
            "positive_or_counterexample",
            "trigger_outcome_label",
            "current_profile_verdict",
            "stage2_evidence_fields",
            "stage3_evidence_fields",
            "evidence_available_at_that_date",
        )
    ).lower()


def _green_equivalent_risk_text(row: dict[str, Any]) -> str:
    return " ".join(
        _as_text(row.get(key))
        for key in (
            "case_id",
            "trigger_id",
            "case_type",
            "positive_or_counterexample",
            "trigger_outcome_label",
            "current_profile_verdict",
            "stage4b_evidence_fields",
            "stage4c_evidence_fields",
            "evidence_available_at_that_date",
        )
    ).lower()


def _is_green_equivalent_positive_row(row: dict[str, Any]) -> bool:
    trigger_type = str(row.get("trigger_type") or "")
    if trigger_type not in GREEN_EQUIVALENT_TRIGGER_TYPES:
        return False
    archetype = str(row.get("canonical_archetype_id") or "")
    required_markers = SOURCE_GREEN_REQUIRED_MARKERS_BY_ARCHETYPE.get(archetype)
    if not required_markers:
        return False
    if _has_green_guard_marker(row):
        return False
    positive_text = _green_equivalent_positive_text(row)
    risk_text = _green_equivalent_risk_text(row)
    if not any(marker in positive_text for marker in GREEN_EQUIVALENT_POSITIVE_MARKERS):
        return False
    if not any(marker in positive_text for marker in required_markers):
        return False
    if any(marker in risk_text for marker in GREEN_EQUIVALENT_BLOCK_MARKERS):
        return False
    stage3_fields = row.get("stage3_evidence_fields")
    if not stage3_fields:
        return False
    return _safe_float(row.get("MFE_180D_pct")) >= 80.0


def _is_green_row(row: dict[str, Any]) -> bool:
    if _is_raw_green_trigger(row):
        return not _has_green_guard_marker(row)
    return _is_green_equivalent_positive_row(row)


def _is_guard_row(row: dict[str, Any]) -> bool:
    if _is_green_row(row):
        return False
    if _has_green_guard_marker(row):
        return True
    trigger_type = str(row.get("trigger_type") or "")
    case_type = str(row.get("case_type") or "").lower()
    label = str(row.get("positive_or_counterexample") or "").lower()
    if trigger_type in GUARD_TRIGGER_TYPES:
        return True
    if any(trigger_type.startswith(prefix) for prefix in GUARD_TRIGGER_PREFIXES):
        return True
    return label == "counterexample" or case_type in GUARD_CASE_TYPES


def _clean_source(row: dict[str, Any]) -> bool:
    return not bool(row.get("source_proxy_only")) and not bool(row.get("evidence_url_pending"))


def _fixture_ready(row: dict[str, Any]) -> bool:
    has_symbol = bool(str(row.get("symbol") or "").strip())
    has_date = bool(str(row.get("trigger_date") or row.get("entry_date") or "").strip())
    has_source_backed_context = any(
        bool(str(row.get(key) or "").strip())
        for key in ("evidence_available_at_that_date", "evidence_source", "source_file")
    )
    return _clean_source(row) and has_symbol and has_date and has_source_backed_context


def _green_fixture_ready(row: dict[str, Any]) -> bool:
    return _fixture_ready(row) and _is_green_row(row)


def _case_key(row: dict[str, Any], archetype: str | None = None) -> tuple[int, int, int, float, str]:
    clean = 1 if _fixture_ready(row) else 0
    weight = 1 if row.get("usable_for_weight_calibration") else 0
    semantic = _semantic_match_score(row, archetype or str(row.get("canonical_archetype_id") or ""))
    mfe = _safe_float(row.get("MFE_180D_pct"))
    date = str(row.get("trigger_date") or row.get("entry_date") or "")
    return (clean, semantic, weight, mfe, date)


def _guard_case_key(row: dict[str, Any], archetype: str | None = None) -> tuple[int, int, int, float, str]:
    clean = 1 if _fixture_ready(row) else 0
    priority = _guard_priority(row)
    semantic = _semantic_match_score(row, archetype or str(row.get("canonical_archetype_id") or ""))
    mae = abs(_safe_float(row.get("MAE_180D_pct")))
    date = str(row.get("trigger_date") or row.get("entry_date") or "")
    return (clean, priority, semantic, mae, date)


def _safe_float(value: Any) -> float:
    if isinstance(value, bool) or value is None:
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _guard_priority(row: dict[str, Any]) -> int:
    trigger_type = str(row.get("trigger_type") or "")
    case_type = str(row.get("case_type") or "").lower()
    label = str(row.get("positive_or_counterexample") or "").lower()
    text = _marker_text(row)
    if _has_green_guard_marker(row):
        return 5
    if label == "counterexample":
        return 4
    if trigger_type in {"Stage4C", "4C"} or case_type == "4c_thesis_break":
        return 3
    if "price_only" in text or "price-only" in text or "policy_headline_only" in text:
        return 3
    if trigger_type in {"Stage4B", "4B"}:
        return 2
    return 1


def _tokenize(value: Any) -> list[str]:
    text = str(value or "").lower()
    tokens = re.split(r"[^0-9a-z가-힣]+", text)
    return [
        token
        for token in tokens
        if len(token) >= 3 and not token.isdigit() and token not in SEMANTIC_TOKEN_STOPWORDS
    ]


def _semantic_match_score(row: dict[str, Any], archetype: str) -> int:
    """Prefer rows that actually describe the archetype bridge, not just high MFE."""

    bridge_spec = _bridge_spec_for_archetype(archetype)
    archetype_tokens = set(_tokenize(archetype))
    primitive_tokens = set()
    for primitive in bridge_spec.get("expected_runtime_primitives", ()):
        primitive_tokens.update(_tokenize(primitive))
    bridge_tokens = set(_tokenize(bridge_spec.get("runtime_bridge_group")))

    row_text = " ".join(
        str(row.get(key) or "")
        for key in (
            "case_id",
            "trigger_id",
            "symbol",
            "trigger_type",
            "evidence_available_at_that_date",
            "evidence_source",
            "evidence_family",
            "trigger_family",
            "supporting_evidence_fields",
            "must_have_fields",
            "key_evidence_fields",
            "positive_evidence_fields",
            "negative_evidence_fields",
        )
    ).lower()
    score = 0
    for token in archetype_tokens:
        if token in row_text:
            score += 2
    for token in primitive_tokens | bridge_tokens:
        if token in row_text:
            score += 1
    return score


def _row_view(row: dict[str, Any]) -> dict[str, Any]:
    view = {
        "case_id": row.get("case_id"),
        "trigger_id": row.get("trigger_id"),
        "symbol": row.get("symbol"),
        "trigger_type": row.get("trigger_type"),
        "trigger_date": row.get("trigger_date"),
        "entry_date": row.get("entry_date"),
        "MFE_180D_pct": row.get("MFE_180D_pct"),
        "MAE_180D_pct": row.get("MAE_180D_pct"),
        "evidence_available_at_that_date": row.get("evidence_available_at_that_date"),
        "evidence_source": row.get("evidence_source"),
        "source_file": row.get("source_file"),
        "source_proxy_only": bool(row.get("source_proxy_only")),
        "evidence_url_pending": bool(row.get("evidence_url_pending")),
        "usable_for_weight_calibration": bool(row.get("usable_for_weight_calibration")),
    }
    source_primitives = _source_expected_runtime_primitives_for_row(row)
    if source_primitives:
        view["source_expected_runtime_primitives"] = list(source_primitives)
    return view


def _source_expected_runtime_primitives_for_row(row: dict[str, Any]) -> tuple[str, ...]:
    if _is_raw_green_trigger(row):
        return ()
    if not _is_green_equivalent_positive_row(row):
        return ()
    archetype = str(row.get("canonical_archetype_id") or "")
    return SOURCE_GREEN_PRIMITIVES_BY_ARCHETYPE.get(archetype, ())


def _bridge_spec_for_archetype(archetype: str) -> dict[str, Any]:
    return dict(ARCHETYPE_RUNTIME_BRIDGE_SPECS.get(archetype, DEFAULT_RUNTIME_BRIDGE_SPEC))


def _first_row_view(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not rows:
        return None
    return _row_view(rows[0])


def build_v12_green_runtime_fixture_candidates(
    representative_rows: list[dict[str, Any]],
    *,
    max_examples_per_archetype: int = 3,
) -> dict[str, Any]:
    """Build archetype-level Green/guard pairs for runtime replay fixture work.

    The output is diagnostic. It does not feed production scoring and it does not
    promote Stage 3-Green by itself.
    """

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in representative_rows:
        normalised_row = normalise_evidence_quality_flags(row)
        archetype = normalised_row.get("canonical_archetype_id")
        if archetype:
            grouped[str(archetype)].append(normalised_row)

    canonical_archetype_set = set(CANONICAL_ARCHETYPE_IDS)
    archetype_ids = list(CANONICAL_ARCHETYPE_IDS)
    archetype_ids.extend(sorted(archetype for archetype in grouped if archetype not in canonical_archetype_set))

    archetypes: list[dict[str, Any]] = []
    for archetype in archetype_ids:
        rows = grouped.get(archetype, [])
        raw_green_rows = sorted(
            (row for row in rows if _is_raw_green_trigger(row)),
            key=lambda row, current_archetype=archetype: _case_key(row, current_archetype),
            reverse=True,
        )
        green_rows = sorted(
            (row for row in rows if _is_green_row(row)),
            key=lambda row, current_archetype=archetype: _case_key(row, current_archetype),
            reverse=True,
        )
        guard_rows = sorted(
            (row for row in rows if _is_guard_row(row)),
            key=lambda row, current_archetype=archetype: _guard_case_key(row, current_archetype),
            reverse=True,
        )
        clean_green = [row for row in green_rows if _green_fixture_ready(row)]
        clean_guard = [row for row in guard_rows if _fixture_ready(row)]
        large_sector = Counter(row.get("large_sector_id") for row in rows if row.get("large_sector_id")).most_common(1)
        if clean_green and clean_guard:
            status = "ready_for_runtime_replay_fixture"
        elif not green_rows:
            status = "needs_green_row"
        elif not clean_green:
            status = "needs_verified_green_source"
        elif not clean_guard:
            status = "needs_guard_pair"
        else:
            status = "hold"
        bridge_spec = _bridge_spec_for_archetype(archetype)
        archetypes.append(
            {
                "canonical_archetype_id": archetype,
                "large_sector_id": large_sector[0][0] if large_sector else ARCHETYPE_TO_LARGE_SECTOR.get(archetype),
                "runtime_bridge_group": bridge_spec["runtime_bridge_group"],
                "expected_runtime_primitives": list(bridge_spec["expected_runtime_primitives"]),
                "research_row_count": len(rows),
                "raw_stage3_green_row_count": len(raw_green_rows),
                "green_row_count": len(green_rows),
                "clean_green_row_count": len(clean_green),
                "green_guard_marker_row_count": len(raw_green_rows) - len(green_rows),
                "guard_row_count": len(guard_rows),
                "clean_guard_row_count": len(clean_guard),
                "source_proxy_only_count": sum(1 for row in rows if row.get("source_proxy_only")),
                "evidence_url_pending_count": sum(1 for row in rows if row.get("evidence_url_pending")),
                "fixture_status": status,
                "green_fixture_candidate": _first_row_view(clean_green or green_rows),
                "guard_fixture_candidate": _first_row_view(clean_guard or guard_rows),
                "green_candidates": [_row_view(row) for row in green_rows[:max_examples_per_archetype]],
                "guard_candidates": [_row_view(row) for row in guard_rows[:max_examples_per_archetype]],
            }
        )

    status_counts = Counter(row["fixture_status"] for row in archetypes)
    ready = [row for row in archetypes if row["fixture_status"] == "ready_for_runtime_replay_fixture"]
    return {
        "schema_version": "v12_green_runtime_fixture_candidates_v2",
        "archetype_count": len(archetypes),
        "status_counts": dict(sorted(status_counts.items())),
        "green_archetype_count": sum(1 for row in archetypes if row["green_row_count"] > 0),
        "ready_archetype_count": status_counts.get("ready_for_runtime_replay_fixture", 0),
        "ready_bridge_groups": dict(sorted(Counter(row["runtime_bridge_group"] for row in ready).items())),
        "total_raw_stage3_green_rows": sum(row["raw_stage3_green_row_count"] for row in archetypes),
        "total_green_rows": sum(row["green_row_count"] for row in archetypes),
        "total_clean_green_rows": sum(row["clean_green_row_count"] for row in archetypes),
        "total_green_guard_marker_rows": sum(row["green_guard_marker_row_count"] for row in archetypes),
        "archetypes": archetypes,
    }


def render_v12_green_runtime_fixture_candidates_report(payload: dict[str, Any]) -> str:
    """Render a concise Markdown report for the fixture candidate payload."""

    archetypes = list(payload.get("archetypes", []))
    green_archetypes = [row for row in archetypes if row.get("green_row_count", 0) > 0]
    ready = [row for row in green_archetypes if row.get("fixture_status") == "ready_for_runtime_replay_fixture"]
    lines = [
        "# V12 Green Runtime Fixture Candidates",
        "",
        "이 보고서는 누적 연구 Green row를 runtime replay fixture로 고정하기 위한 후보 장부다.",
        "여기 있는 후보는 production scoring 입력이 아니며, Green을 직접 만들지 않는다.",
        "",
        "## Summary",
        "",
        f"- archetype_count: `{payload.get('archetype_count', 0)}`",
        f"- green_archetype_count: `{payload.get('green_archetype_count', 0)}`",
        f"- ready_archetype_count: `{payload.get('ready_archetype_count', 0)}`",
        f"- total_raw_stage3_green_rows: `{payload.get('total_raw_stage3_green_rows', 0)}`",
        f"- total_green_rows: `{payload.get('total_green_rows', 0)}`",
        f"- total_clean_green_rows: `{payload.get('total_clean_green_rows', 0)}`",
        f"- total_green_guard_marker_rows: `{payload.get('total_green_guard_marker_rows', 0)}`",
        f"- status_counts: `{payload.get('status_counts', {})}`",
        f"- ready_bridge_groups: `{payload.get('ready_bridge_groups', {})}`",
        "",
        "`raw Stage3-Green`은 원본 trigger label 기준이고, `fixture Green`은 source-backed Stage3-Green 및 구조적 성공/too-late로 검증된 Green-equivalent 후보를 센다.",
        "`fixture Green`에서도 `false_green`, `false_positive`, `policy_only`, `local_4B_watch` 같은 guard marker는 제외한다.",
        "대표 fixture는 MFE가 가장 큰 row가 아니라 archetype/bridge primitive와 의미가 더 잘 맞는 row를 우선한다.",
        "",
        "## Archetype Coverage",
        "",
        "| archetype | bridge group | large sector | raw Green | fixture Green | clean Green | guard markers | guard | clean guard | status |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in sorted(archetypes, key=lambda item: (-int(item["green_row_count"]), str(item["canonical_archetype_id"]))):
        lines.append(
            "| {arch} | {bridge} | {sector} | {raw_green} | {green} | {clean_green} | {guard_markers} | {guard} | {clean_guard} | {status} |".format(
                arch=row["canonical_archetype_id"],
                bridge=row.get("runtime_bridge_group") or "",
                sector=row.get("large_sector_id") or "",
                raw_green=row["raw_stage3_green_row_count"],
                green=row["green_row_count"],
                clean_green=row["clean_green_row_count"],
                guard_markers=row["green_guard_marker_row_count"],
                guard=row["guard_row_count"],
                clean_guard=row["clean_guard_row_count"],
                status=row["fixture_status"],
            )
        )
    lines.extend(["", "## Replay Fixture Matrix", ""])
    lines.extend(
        [
            "| archetype | Green fixture | guard fixture | expected runtime primitives | status |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in sorted(green_archetypes, key=lambda item: (-int(item["green_row_count"]), str(item["canonical_archetype_id"]))):
        green = row.get("green_fixture_candidate") or {}
        guard = row.get("guard_fixture_candidate") or {}
        green_id = green.get("case_id") or green.get("trigger_id") or ""
        guard_id = guard.get("case_id") or guard.get("trigger_id") or ""
        green_label = " ".join(
            item
            for item in (
                str(green.get("symbol") or ""),
                str(green.get("trigger_date") or green.get("entry_date") or ""),
                str(green_id),
            )
            if item
        )
        guard_label = " ".join(
            item
            for item in (
                str(guard.get("symbol") or ""),
                str(guard.get("trigger_date") or guard.get("entry_date") or ""),
                str(guard_id),
            )
            if item
        )
        primitives = ", ".join(str(item) for item in row.get("expected_runtime_primitives", [])[:5])
        lines.append(
            "| {arch} | {green} | {guard} | {primitives} | {status} |".format(
                arch=row["canonical_archetype_id"],
                green=green_label or "-",
                guard=guard_label or "-",
                primitives=primitives,
                status=row["fixture_status"],
            )
        )
    lines.extend(["", "## Ready Examples", ""])
    for row in sorted(ready, key=lambda item: (-int(item["green_row_count"]), str(item["canonical_archetype_id"])))[:12]:
        green = row.get("green_fixture_candidate") or {}
        guard = row.get("guard_fixture_candidate") or {}
        green_id = green.get("case_id") or green.get("trigger_id")
        guard_id = guard.get("case_id") or guard.get("trigger_id")
        green_evidence = green.get("evidence_available_at_that_date") or green.get("evidence_source") or green.get("source_file") or ""
        guard_evidence = guard.get("evidence_available_at_that_date") or guard.get("evidence_source") or guard.get("source_file") or ""
        lines.extend(
            [
                f"### {row['canonical_archetype_id']}",
                "",
                f"- Bridge group: `{row.get('runtime_bridge_group')}`",
                f"- Expected runtime primitives: `{', '.join(str(item) for item in row.get('expected_runtime_primitives', []))}`",
                f"- Green candidate: `{green.get('symbol')}` `{green.get('trigger_date')}` `{green_id}`",
                f"- Green evidence: {green_evidence}",
                f"- Guard candidate: `{guard.get('symbol')}` `{guard.get('trigger_date')}` `{guard_id}`",
                f"- Guard evidence: {guard_evidence}",
                "",
            ]
        )
    lines.extend(
        [
            "## How To Use",
            "",
            "1. Ready archetype부터 Green/guard pair를 runtime replay fixture로 만든다.",
            "2. Green pair는 source-backed primitive가 component/gate까지 올라오는지 검증한다.",
            "3. Guard pair는 threshold 완화나 positive unlock 때문에 false positive가 열리지 않는지 검증한다.",
            "4. 이 fixture를 통과하지 못하면 Green 기준을 낮추는 것이 아니라 parser/feature adapter/candidate funnel 중 어느 층이 끊겼는지 다시 본다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_green_runtime_fixture_candidates(
    *,
    representative_rows_path: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
    max_examples_per_archetype: int = 3,
) -> dict[str, Path]:
    rows = _read_jsonl(representative_rows_path)
    payload = build_v12_green_runtime_fixture_candidates(
        rows,
        max_examples_per_archetype=max_examples_per_archetype,
    )
    json_path = Path(output_json_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_green_runtime_fixture_candidates_report(payload), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}
