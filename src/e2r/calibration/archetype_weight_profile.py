"""Runtime archetype-specific score weight profiles.

The v12 research loop produces two kinds of useful information:

* explicit score-weight research tables, and
* stage-transition / price-path validation by canonical archetype.

This module turns that research layer into a deterministic runtime profile. It
does not use stock names or benchmark labels. Matching is done only by
``large_sector_id`` and ``canonical_archetype_id`` already carried by
``ScoringPayload``.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping
import json


RUNTIME_WEIGHT_PROFILE_PATH = Path("configs/e2r_archetype_weight_profile_v2_2.json")
RUNTIME_WEIGHT_REPORT_PATH = Path("reports/e2r_calibration/v12/archetype_weight_runtime_report.md")

SCORE_COMPONENT_KEYS = (
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
)

CANONICAL_COMPONENT_MAX_POINTS: dict[str, float] = {
    "eps_fcf_explosion": 20.0,
    "earnings_visibility": 20.0,
    "bottleneck_pricing": 20.0,
    "market_mispricing": 15.0,
    "valuation_rerating": 15.0,
    "capital_allocation": 5.0,
    "information_confidence": 5.0,
}

DEFAULT_RUNTIME_WEIGHTS = dict(CANONICAL_COMPONENT_MAX_POINTS)


def _normalise_weights(weights: Mapping[str, float]) -> dict[str, float]:
    missing = [key for key in SCORE_COMPONENT_KEYS if key not in weights]
    if missing:
        raise ValueError(f"missing runtime score weights: {missing}")
    values = {key: float(weights[key]) for key in SCORE_COMPONENT_KEYS}
    if any(value < 0 for value in values.values()):
        raise ValueError("runtime score weights must be non-negative")
    total = sum(values.values())
    if total <= 0:
        raise ValueError("runtime score weights must have a positive total")
    scaled = {key: round(value * 100.0 / total, 6) for key, value in values.items()}
    rounding_gap = round(100.0 - sum(scaled.values()), 6)
    scaled["information_confidence"] = round(scaled["information_confidence"] + rounding_gap, 6)
    return scaled


def _weights(
    eps_fcf: float,
    visibility: float,
    bottleneck: float,
    mispricing: float,
    valuation: float,
    capital: float,
    information: float,
) -> dict[str, float]:
    return _normalise_weights(
        {
            "eps_fcf_explosion": eps_fcf,
            "earnings_visibility": visibility,
            "bottleneck_pricing": bottleneck,
            "market_mispricing": mispricing,
            "valuation_rerating": valuation,
            "capital_allocation": capital,
            "information_confidence": information,
        }
    )


LARGE_SECTOR_WEIGHT_SEEDS: dict[str, dict[str, Any]] = {
    "L1_INDUSTRIALS_INFRA_DEFENSE_GRID": {
        "weights": _weights(20, 24, 20, 12, 12, 7, 5),
        "green_policy": "green_allowed_with_contract_or_backlog_visibility",
    },
    "L2_AI_SEMICONDUCTOR_ELECTRONICS": {
        "weights": _weights(24, 21, 19, 14, 10, 5, 7),
        "green_policy": "green_allowed_with_capacity_and_revision",
    },
    "L3_BATTERY_EV_GREEN_MOBILITY": {
        "weights": _weights(20, 16, 14, 10, 10, 8, 22),
        "green_policy": "green_restricted_by_capex_cycle",
    },
    "L4_MATERIALS_SPREAD_RESOURCE": {
        "weights": _weights(20, 12, 18, 10, 10, 5, 25),
        "green_policy": "green_restricted_by_spread_cycle",
    },
    "L5_CONSUMER_BRAND_DISTRIBUTION": {
        "weights": _weights(22, 23, 12, 16, 13, 4, 10),
        "green_policy": "green_allowed_with_channel_and_repeat_demand",
    },
    "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL": {
        "weights": _weights(15, 20, 5, 15, 25, 15, 5),
        "green_policy": "green_allowed_with_roe_capital_return_and_credit_guard",
    },
    "L7_BIO_HEALTHCARE_MEDICAL": {
        "weights": _weights(14, 22, 8, 12, 10, 7, 27),
        "green_policy": "green_restricted_until_revenue_or_approval_conversion",
    },
    "L8_PLATFORM_CONTENT_SW_SECURITY": {
        "weights": _weights(20, 22, 8, 16, 14, 10, 10),
        "green_policy": "green_allowed_with_monetization_and_margin_leverage",
    },
    "L9_CONSTRUCTION_REALESTATE_HOUSING": {
        "weights": _weights(18, 12, 8, 12, 10, 10, 30),
        "green_policy": "green_restricted_by_credit_pf_risk",
    },
    "L10_POLICY_EVENT_CROSS_REDTEAM_MISC": {
        "weights": _weights(12, 15, 8, 15, 15, 10, 25),
        "green_policy": "green_restricted_without_contract_or_cashflow_conversion",
    },
}


ARCHETYPE_WEIGHT_SEEDS: dict[str, dict[str, Any]] = {
    "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": {
        "weights": _weights(20, 24, 17, 14, 14, 6, 5),
        "green_policy": "green_allowed_with_government_backlog_and_delivery_visibility",
        "basis": "defense government backlog: contract, delivery schedule, margin conversion",
    },
    "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY": {
        "weights": _weights(15, 22, 10, 15, 18, 10, 10),
        "green_policy": "watch_to_green_only_after_final_contract_and_legal_clarity",
        "basis": "nuclear policy events need final project economics before Green",
    },
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY": {
        "weights": _weights(24, 21, 19, 15, 12, 4, 5),
        "green_policy": "green_allowed_with_hbm_capacity_customer_and_revision",
        "basis": "HBM/memory rerating: customer capacity, price discipline, multi-year revisions",
    },
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH": {
        "weights": _weights(22, 22, 19, 14, 12, 6, 5),
        "green_policy": "green_allowed_with_orders_and_revenue_conversion",
        "basis": "semi equipment: orders, backlog, customer capex, revenue conversion",
    },
    "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF": {
        "weights": _weights(22, 20, 18, 13, 11, 6, 10),
        "green_policy": "watch_to_green_with_valuation_blowoff_guard",
        "basis": "advanced equipment keeps bottleneck credit but raises valuation/4B guard attention",
    },
    "C11_BATTERY_ORDERBOOK_RERATING": {
        "weights": _weights(20, 20, 15, 12, 10, 8, 15),
        "green_policy": "green_restricted_until_margin_and_fcf_after_capex",
        "basis": "battery orderbook needs contract margin, FCF, utilization and EV demand support",
    },
    "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK": {
        "weights": _weights(20, 18, 14, 10, 10, 8, 20),
        "green_policy": "green_restricted_by_calloff_and_customer_demand_risk",
        "basis": "battery contract call-off risk makes information confidence and red-team gates heavier",
    },
    "C13_BATTERY_JV_UTILIZATION_AMPC_IRA": {
        "weights": _weights(20, 18, 14, 12, 10, 10, 16),
        "green_policy": "watch_to_green_with_utilization_and_policy_durability",
        "basis": "battery JV/AMPC needs utilization and durable subsidy economics",
    },
    "C14_EV_DEMAND_SLOWDOWN_4B_4C": {
        "weights": _weights(15, 12, 10, 8, 8, 7, 40),
        "green_policy": "red_watch",
        "basis": "EV slowdown is primarily a 4B/4C protection archetype",
    },
    "C15_MATERIAL_SPREAD_SUPERCYCLE": {
        "weights": _weights(20, 12, 20, 10, 10, 8, 20),
        "green_policy": "green_restricted_by_cycle_reversal",
        "basis": "spread supercycle needs cost-curve or supply-discipline proof, not price only",
    },
    "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY": {
        "weights": _weights(18, 18, 18, 12, 12, 7, 15),
        "green_policy": "watch_to_green_with_supply_contract_and_policy_durability",
        "basis": "strategic resources need policy plus supply/contract economics",
    },
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": {
        "weights": _weights(20, 12, 18, 10, 10, 5, 25),
        "green_policy": "red_watch",
        "basis": "chemical/commodity spread has high reversal risk",
    },
    "C18_CONSUMER_EXPORT_CHANNEL_REORDER": {
        "weights": _weights(22, 23, 12, 16, 13, 4, 10),
        "green_policy": "green_allowed_with_export_channel_repeat_demand",
        "basis": "consumer export: channel expansion, repeat demand, OPM and revision replace contract quality",
    },
    "C19_BRAND_RETAIL_INVENTORY_MARGIN": {
        "weights": _weights(18, 18, 8, 15, 14, 7, 20),
        "green_policy": "watch_to_green_with_inventory_and_margin_proof",
        "basis": "brand/retail needs sell-through, inventory and cash conversion checks",
    },
    "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION": {
        "weights": _weights(22, 23, 12, 16, 13, 4, 10),
        "green_policy": "green_allowed_with_global_distribution_and_repeat_sellthrough",
        "basis": "K-food/K-beauty: export growth, global channel, recurring demand, OPM and EPS revision",
    },
    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN": {
        "weights": _weights(15, 20, 5, 15, 25, 15, 5),
        "green_policy": "green_allowed_with_roe_pbr_and_executed_capital_return",
        "basis": "financial value-up: ROE/PBR, capital return, credit cost and reserve quality",
    },
    "C22_INSURANCE_RATE_CYCLE_RESERVE": {
        "weights": _weights(12, 22, 5, 14, 24, 18, 5),
        "green_policy": "green_allowed_with_reserve_rate_cycle_and_capital_return",
        "basis": "insurance rerating: reserve, rate cycle, ROE/PBR and shareholder return outrank contracts",
    },
    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION": {
        "weights": _weights(12, 24, 5, 12, 10, 7, 30),
        "green_policy": "watch_to_green_after_approval_revenue_or_royalty_conversion",
        "basis": "commercializing biotech needs approval and revenue/royalty conversion",
    },
    "C24_BIO_TRIAL_DATA_EVENT_RISK": {
        "weights": _weights(5, 15, 5, 10, 5, 5, 55),
        "green_policy": "event_only_red_watch",
        "basis": "trial data is event-risk-first until revenue and dilution risk are resolved",
    },
    "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT": {
        "weights": _weights(20, 22, 13, 14, 12, 9, 10),
        "green_policy": "green_allowed_with_export_reimbursement_and_repeat_consumable_revenue",
        "basis": "medical device export: approval, channel, reimbursement, repeat consumables",
    },
    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE": {
        "weights": _weights(20, 22, 8, 16, 14, 10, 10),
        "green_policy": "green_allowed_with_arpu_monetization_and_op_leverage",
        "basis": "platform: traffic is insufficient without monetization and operating leverage",
    },
    "C27_CONTENT_IP_GLOBAL_MONETIZATION": {
        "weights": _weights(20, 18, 8, 14, 12, 8, 20),
        "green_policy": "watch_to_green_with_repeat_ip_monetization",
        "basis": "content/IP needs repeat monetization and hit-risk control",
    },
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION": {
        "weights": _weights(20, 24, 8, 16, 14, 8, 10),
        "green_policy": "green_allowed_with_arr_retention_and_margin_leverage",
        "basis": "software/security: recurring revenue, retention, ARR/RPO and OPM leverage",
    },
    "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": {
        "weights": _weights(20, 18, 10, 15, 17, 15, 5),
        "green_policy": "watch_to_green_with_mix_margin_and_capital_return",
        "basis": "mobility: volume/mix/margin plus valuation and capital return",
    },
    "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK": {
        "weights": _weights(18, 12, 8, 12, 10, 10, 30),
        "green_policy": "red_watch",
        "basis": "construction/PF is credit-risk-first until balance sheet repair is proven",
    },
    "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": {
        "weights": _weights(12, 15, 8, 15, 15, 10, 25),
        "green_policy": "event_only_until_cashflow_conversion",
        "basis": "policy/subsidy events need conversion into contract, margin or FCF",
    },
    "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP": {
        "weights": _weights(12, 18, 5, 20, 25, 15, 5),
        "green_policy": "event_premium_not_structural_green_without_fcf_or_return",
        "basis": "governance/tender premium is event rerating unless NAV/FCF/shareholder return improves",
    },
}


@dataclass(frozen=True)
class RuntimeWeightMatch:
    matched_scope: str
    profile_key: str
    weights: Mapping[str, float]
    green_policy: str
    basis: str
    support: Mapping[str, Any]


@dataclass(frozen=True)
class WeightedComponents:
    components: Mapping[str, float]
    diagnostics: Mapping[str, float]
    match: RuntimeWeightMatch | None


@dataclass(frozen=True)
class ArchetypeWeightProfile:
    profile_id: str
    profile_status: str
    enabled: bool
    default_weights: Mapping[str, float]
    large_sector_weights: Mapping[str, Mapping[str, Any]]
    archetype_weights: Mapping[str, Mapping[str, Any]]

    def match(self, *, canonical_archetype_id: str | None, large_sector_id: str | None) -> RuntimeWeightMatch | None:
        if not self.enabled:
            return None
        if canonical_archetype_id and canonical_archetype_id in self.archetype_weights:
            payload = self.archetype_weights[canonical_archetype_id]
            return _match_from_payload("canonical_archetype", canonical_archetype_id, payload)
        if large_sector_id and large_sector_id in self.large_sector_weights:
            payload = self.large_sector_weights[large_sector_id]
            return _match_from_payload("large_sector", large_sector_id, payload)
        return None

    def apply(
        self,
        components: Mapping[str, float],
        *,
        canonical_archetype_id: str | None = None,
        large_sector_id: str | None = None,
    ) -> WeightedComponents:
        match = self.match(canonical_archetype_id=canonical_archetype_id, large_sector_id=large_sector_id)
        if match is None:
            return WeightedComponents(components=dict(components), diagnostics={}, match=None)
        weighted_components: dict[str, float] = {}
        diagnostics: dict[str, float] = {
            "archetype_weight_profile_applied": 1.0,
            "archetype_weight_match_is_archetype": 1.0 if match.matched_scope == "canonical_archetype" else 0.0,
            "archetype_weight_match_is_large_sector": 1.0 if match.matched_scope == "large_sector" else 0.0,
        }
        for key in SCORE_COMPONENT_KEYS:
            canonical_max = CANONICAL_COMPONENT_MAX_POINTS[key]
            weight_max = float(match.weights[key])
            raw_value = max(0.0, min(float(components[key]), canonical_max))
            weighted_value = round((raw_value / canonical_max) * weight_max, 4)
            weighted_components[key] = weighted_value
            diagnostics[f"archetype_weight_{key}"] = round(weight_max, 4)
            diagnostics[f"archetype_component_{key}"] = weighted_value
        diagnostics["archetype_weighted_total_before_calibration"] = round(sum(weighted_components.values()), 4)
        return WeightedComponents(components=weighted_components, diagnostics=diagnostics, match=match)


def _match_from_payload(scope: str, key: str, payload: Mapping[str, Any]) -> RuntimeWeightMatch:
    return RuntimeWeightMatch(
        matched_scope=scope,
        profile_key=key,
        weights=_normalise_weights(payload["weights"]),
        green_policy=str(payload.get("green_policy", "watch_only")),
        basis=str(payload.get("basis", "")),
        support=dict(payload.get("support", {})),
    )


def load_archetype_weight_profile(path: str | Path = RUNTIME_WEIGHT_PROFILE_PATH) -> ArchetypeWeightProfile:
    path_obj = Path(path)
    if not path_obj.exists():
        return ArchetypeWeightProfile(
            profile_id="e2r_archetype_weight_disabled_missing_profile",
            profile_status="missing_profile",
            enabled=False,
            default_weights=DEFAULT_RUNTIME_WEIGHTS,
            large_sector_weights={},
            archetype_weights={},
        )
    payload = json.loads(path_obj.read_text(encoding="utf-8"))
    return ArchetypeWeightProfile(
        profile_id=str(payload.get("profile_id", path_obj.stem)),
        profile_status=str(payload.get("profile_status", "unknown")),
        enabled=bool(payload.get("enabled", False)),
        default_weights=_normalise_weights(payload.get("default_weights", DEFAULT_RUNTIME_WEIGHTS)),
        large_sector_weights=dict(payload.get("large_sector_weights", {})),
        archetype_weights=dict(payload.get("archetype_weights", {})),
    )


def _aggregate_support_by_group(aggregate_rows: list[dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    support: dict[tuple[str, str], dict[str, Any]] = {}
    for row in aggregate_rows:
        group_name = str(row.get("group_name") or "")
        group_value = str(row.get("group_value") or "")
        if group_name not in {"large_sector_id", "canonical_archetype_id"} or not group_value:
            continue
        support[(group_name, group_value)] = {
            "row_count": int(row.get("row_count", 0) or 0),
            "unique_case_count": int(row.get("unique_case_count", 0) or 0),
            "unique_symbol_count": int(row.get("unique_symbol_count", 0) or 0),
            "positive_case_count": int(row.get("positive_case_count", 0) or 0),
            "counterexample_count": int(row.get("counterexample_count", 0) or 0),
            "good_stage2_count": int(row.get("good_stage2_count", 0) or 0),
            "bad_stage2_count": int(row.get("bad_stage2_count", 0) or 0),
            "good_4b_timing_count": int(row.get("good_4b_timing_count", 0) or 0),
            "4c_late_count": int(row.get("4c_late_count", 0) or 0),
            "source_proxy_only_count": int(row.get("source_proxy_only_count", 0) or 0),
            "evidence_url_pending_count": int(row.get("evidence_url_pending_count", 0) or 0),
            "avg_stage2_MFE90": row.get("avg_stage2_MFE90"),
            "avg_stage2_MAE90": row.get("avg_stage2_MAE90"),
            "stage2_hit_rate_MFE90_ge_20": row.get("stage2_hit_rate_MFE90_ge_20"),
            "stage2_bad_entry_rate_MAE90_le_minus_20": row.get("stage2_bad_entry_rate_MAE90_le_minus_20"),
        }
    return support


def build_archetype_weight_profile_payload(
    *,
    aggregate_rows: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    support_by_group = _aggregate_support_by_group(aggregate_rows or [])
    large_sector_weights: dict[str, Any] = {}
    for key, seed in LARGE_SECTOR_WEIGHT_SEEDS.items():
        payload = dict(seed)
        payload["support"] = support_by_group.get(("large_sector_id", key), {})
        large_sector_weights[key] = payload
    archetype_weights: dict[str, Any] = {}
    for key, seed in ARCHETYPE_WEIGHT_SEEDS.items():
        payload = dict(seed)
        payload["support"] = support_by_group.get(("canonical_archetype_id", key), {})
        archetype_weights[key] = payload
    return {
        "profile_id": "e2r_2_2_archetype_weight_runtime",
        "profile_status": "default_enabled",
        "enabled": True,
        "profile_basis": "v12_stage_transition_price_validation_plus_score_weight_research",
        "default_weights": DEFAULT_RUNTIME_WEIGHTS,
        "large_sector_weights": large_sector_weights,
        "archetype_weights": archetype_weights,
        "guardrails": {
            "weights_sum_to_100": True,
            "stock_name_rules_forbidden": True,
            "case_library_not_candidate_input": True,
            "future_price_not_runtime_input": True,
            "stage3_green_not_loosened_by_weight_profile": True,
        },
    }


def write_archetype_weight_runtime_profile(
    *,
    aggregate_metrics_path: str | Path = "data/e2r/calibration/v12/v12_aggregate_metrics.json",
    output_path: str | Path = RUNTIME_WEIGHT_PROFILE_PATH,
    report_path: str | Path = RUNTIME_WEIGHT_REPORT_PATH,
) -> dict[str, Any]:
    aggregate_path = Path(aggregate_metrics_path)
    aggregate_rows = json.loads(aggregate_path.read_text(encoding="utf-8")) if aggregate_path.exists() else []
    payload = build_archetype_weight_profile_payload(aggregate_rows=aggregate_rows)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report = Path(report_path)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(render_archetype_weight_runtime_report(payload), encoding="utf-8")
    return {
        "profile_path": str(output),
        "report_path": str(report),
        "profile_id": payload["profile_id"],
        "archetype_count": len(payload["archetype_weights"]),
        "large_sector_count": len(payload["large_sector_weights"]),
    }


def render_archetype_weight_runtime_report(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Archetype Weight Runtime Report",
        "",
        "v12 연구와 가격경로 검증을 production scoring의 아키타입별 점수비중에 연결했습니다.",
        "런타임 판단에는 미래 가격을 쓰지 않고, 과거 가격경로는 이 weight profile을 보정한 근거로만 남습니다.",
        "",
        f"- profile_id: `{payload.get('profile_id')}`",
        f"- enabled: `{payload.get('enabled')}`",
        f"- large_sector_weight_count: `{len(payload.get('large_sector_weights', {}))}`",
        f"- canonical_archetype_weight_count: `{len(payload.get('archetype_weights', {}))}`",
        "",
        "## Runtime Example",
        "",
        "- C20 K-food/K-beauty: 계약공시보다 수출, 채널 확장, 반복수요, OPM, EPS revision 비중이 커집니다.",
        "- C03 Defense/Grid: 정부 고객, 계약, 수주잔고, 납품 visibility가 약하면 Stage 3 쪽으로 쉽게 못 갑니다.",
        "- C22 Insurance: 계약품질보다 ROE/PBR, reserve/rate cycle, 자본환원 비중이 커집니다.",
        "",
        "## Top Archetype Weights",
        "",
        "| archetype | EPS/FCF | visibility | bottleneck | mispricing | valuation | capital | info | support | green_policy |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for key, payload_row in sorted(payload.get("archetype_weights", {}).items()):
        weights = payload_row["weights"]
        support = payload_row.get("support", {})
        lines.append(
            f"| {key} | {weights['eps_fcf_explosion']:.1f} | {weights['earnings_visibility']:.1f} | "
            f"{weights['bottleneck_pricing']:.1f} | {weights['market_mispricing']:.1f} | "
            f"{weights['valuation_rerating']:.1f} | {weights['capital_allocation']:.1f} | "
            f"{weights['information_confidence']:.1f} | {support.get('row_count', 0)} rows / "
            f"{support.get('unique_symbol_count', 0)} symbols | {payload_row.get('green_policy')} |"
        )
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- 종목명은 weight 선택에 쓰지 않습니다.",
            "- benchmark label과 case library는 후보 생성 input이 아닙니다.",
            "- 미래 MFE/MAE/peak는 runtime 판단에 쓰지 않고, weight 보정 근거로만 사용합니다.",
            "- Stage 3-Green 전역 total/revision 기준은 낮추지 않습니다.",
        ]
    )
    return "\n".join(lines) + "\n"


__all__ = [
    "ARCHETYPE_WEIGHT_SEEDS",
    "CANONICAL_COMPONENT_MAX_POINTS",
    "DEFAULT_RUNTIME_WEIGHTS",
    "LARGE_SECTOR_WEIGHT_SEEDS",
    "RUNTIME_WEIGHT_PROFILE_PATH",
    "ArchetypeWeightProfile",
    "RuntimeWeightMatch",
    "WeightedComponents",
    "build_archetype_weight_profile_payload",
    "load_archetype_weight_profile",
    "render_archetype_weight_runtime_report",
    "write_archetype_weight_runtime_profile",
]
