"""Round-6 missing-sector correction framework.

Round 6 adds a cross-sector overlay on top of Round 5. It is useful for
themes that cut across ordinary sectors, such as AI data-center infrastructure
or national-strategy policy chains. This module is report/calibration material
only and is not imported by production scoring.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import E2RCaseRecord, load_case_library


ROUND6_SOURCE_ROUND_PATH = "docs/round/round_06.md"


class Round6OverlaySector(str, Enum):
    """Six missing-sector correction buckets from Round 6."""

    AI_POWER_INFRA = "AI_POWER_INFRA"
    NATIONAL_STRATEGY_POLICY = "NATIONAL_STRATEGY_POLICY"
    CAPITAL_ALLOCATION_VALUEUP = "CAPITAL_ALLOCATION_VALUEUP"
    CYCLE_MACRO_CREDIT = "CYCLE_MACRO_CREDIT"
    THEME_TECH_EXPECTATION = "THEME_TECH_EXPECTATION"
    RECURRING_EXPORT_BRAND = "RECURRING_EXPORT_BRAND"


class Round6ValidationPosture(str, Enum):
    """How aggressively the overlay can support future Green scoring."""

    STRUCTURAL_GREEN_POSSIBLE = "STRUCTURAL_GREEN_POSSIBLE"
    WATCH_YELLOW_FIRST = "WATCH_YELLOW_FIRST"
    CYCLE_OR_EVENT_CAPPED = "CYCLE_OR_EVENT_CAPPED"
    REDTEAM_FIRST = "REDTEAM_FIRST"


@dataclass(frozen=True)
class Round6OverlayDefinition:
    """One Round-6 overlay sector."""

    overlay_sector: Round6OverlaySector
    korean_name: str
    archetypes: tuple[E2RArchetype, ...]
    posture: Round6ValidationPosture
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_requires: tuple[str, ...]
    stage4b_signals: tuple[str, ...]
    stage4c_signals: tuple[str, ...]
    price_validation_focus: tuple[str, ...]
    green_policy: str
    examples: tuple[str, ...]


ROUND6_PRICE_VALIDATION_FIELDS = (
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "mfe_30d",
    "mfe_90d",
    "mfe_180d",
    "mfe_1y",
    "mfe_2y",
    "mae_30d",
    "mae_90d",
    "mae_180d",
    "mae_1y",
    "mae_2y",
    "below_stage3_price_flag",
    "time_to_50pct",
    "time_to_100pct",
    "drawdown_after_peak",
)


ROUND6_PRICE_PATTERN_VALUES = (
    "straight_rerating",
    "stair_step_rerating",
    "cycle_boom_bust",
    "theme_overheat",
    "accounting_trust_break",
    "event_premium",
    "credit_relief_rally",
    "reopening_cycle",
)


ROUND6_OVERLAY_DEFINITIONS: Mapping[Round6OverlaySector, Round6OverlayDefinition] = {
    Round6OverlaySector.AI_POWER_INFRA: Round6OverlayDefinition(
        overlay_sector=Round6OverlaySector.AI_POWER_INFRA,
        korean_name="AI/전력/인프라",
        archetypes=(
            E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
            E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
            E2RArchetype.SEMI_EQUIPMENT_CAPEX,
            E2RArchetype.MEMORY_HBM_CAPACITY,
        ),
        posture=Round6ValidationPosture.STRUCTURAL_GREEN_POSSIBLE,
        stage1_signals=("ai_data_center_capex", "power_shortage_keyword", "cooling_or_grid_keyword", "trading_value_spike"),
        stage2_signals=("confirmed_order_or_contract", "customer_capex_visibility", "op_eps_revision", "official_or_report_evidence"),
        stage3_requires=("multi_year_capex_visibility", "capacity_bottleneck", "pricing_power", "fy1_fy2_fy3_revision"),
        stage4b_signals=("ai_capex_narrative_overheated", "sector_wide_rally", "new_capacity_risk", "crowded_report_tone"),
        stage4c_signals=("ai_capex_cut", "data_center_delay", "permit_or_grid_delay", "order_cancellation"),
        price_validation_focus=("stair_step_rerating", "theme_overheat", "mfe_180d", "time_to_100pct"),
        green_policy="Green possible only after orders, delivery/revenue conversion, and EPS revision are visible.",
        examples=("HD현대일렉트릭", "효성중공업", "LS ELECTRIC", "이수페타시스", "데이터센터 냉각/전력망"),
    ),
    Round6OverlaySector.NATIONAL_STRATEGY_POLICY: Round6OverlayDefinition(
        overlay_sector=Round6OverlaySector.NATIONAL_STRATEGY_POLICY,
        korean_name="정책/국가전략",
        archetypes=(
            E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
            E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
            E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        ),
        posture=Round6ValidationPosture.WATCH_YELLOW_FIRST,
        stage1_signals=("policy_event", "preferred_bidder", "government_customer", "strategic_material_keyword"),
        stage2_signals=("contract_or_loi", "project_financing", "delivery_schedule", "legal_risk_reduced"),
        stage3_requires=("binding_contract_economics", "multi_year_revenue_path", "margin_visibility", "low_policy_legal_risk"),
        stage4b_signals=("policy_premium_overpriced", "theme_group_rally", "contract_before_economics"),
        stage4c_signals=("legal_delay", "policy_reversal", "project_delay", "cost_overrun"),
        price_validation_focus=("event_premium", "stair_step_rerating", "stage4c_price", "drawdown_after_peak"),
        green_policy="Watch/Yellow first; Green needs contract economics, revenue conversion, and low legal/policy risk.",
        examples=("체코 원전", "두산에너빌리티", "한화에어로스페이스", "Korea Zinc 전략소재"),
    ),
    Round6OverlaySector.CAPITAL_ALLOCATION_VALUEUP: Round6OverlayDefinition(
        overlay_sector=Round6OverlaySector.CAPITAL_ALLOCATION_VALUEUP,
        korean_name="자본배분/밸류업",
        archetypes=(
            E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
            E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
            E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
            E2RArchetype.TURNAROUND_COST_RESTRUCTURING,
        ),
        posture=Round6ValidationPosture.WATCH_YELLOW_FIRST,
        stage1_signals=("value_up_disclosure", "buyback_or_dividend", "low_pbr", "governance_event"),
        stage2_signals=("roe_improvement", "cet1_or_capital_ratio_stable", "executed_return", "nav_discount_catalyst"),
        stage3_requires=("pbr_roe_frame_change", "recurring_roe_or_fcf", "credible_shareholder_return", "credit_risk_low"),
        stage4b_signals=("pbr_normalized", "event_premium_fully_priced", "return_policy_no_longer_incremental"),
        stage4c_signals=("credit_cost_up", "return_not_executed", "subsidiary_value_impairment", "capital_ratio_deterioration"),
        price_validation_focus=("event_premium", "straight_rerating", "mfe_1y", "below_stage3_price_flag"),
        green_policy="Green requires ROE/PBR/shareholder-return consistency or durable NAV/FCF improvement.",
        examples=("KB금융", "메리츠금융", "SK스퀘어", "Korea Zinc event premium"),
    ),
    Round6OverlaySector.CYCLE_MACRO_CREDIT: Round6OverlayDefinition(
        overlay_sector=Round6OverlaySector.CYCLE_MACRO_CREDIT,
        korean_name="경기/사이클",
        archetypes=(
            E2RArchetype.SHIPPING_FREIGHT_CYCLE,
            E2RArchetype.COMMODITY_SPREAD,
            E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
            E2RArchetype.TRAVEL_LEISURE_REOPENING,
            E2RArchetype.AUTO_MOBILITY_COMPONENTS,
            E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE,
        ),
        posture=Round6ValidationPosture.CYCLE_OR_EVENT_CAPPED,
        stage1_signals=("freight_or_spread_spike", "pf_relief", "traffic_recovery", "sales_or_fx_mix_improvement"),
        stage2_signals=("op_eps_revision", "contract_or_margin_support", "cash_flow_improvement", "shareholder_return_execution"),
        stage3_requires=("cycle_risk_control", "multi_quarter_margin_support", "fcf_or_balance_sheet_support"),
        stage4b_signals=("freight_or_margin_peak", "reopening_expectation_priced", "valuation_rerating_done"),
        stage4c_signals=("overcapacity", "pf_stress", "demand_slowdown", "oil_fx_or_tariff_shock"),
        price_validation_focus=("cycle_boom_bust", "credit_relief_rally", "reopening_cycle", "mfe_90d", "mae_180d"),
        green_policy="Green is capped unless cycle/credit risk is controlled and FCF durability is visible.",
        examples=("HMM 2020~2021", "Maersk downturn", "Taeyoung E&C PF stress", "Hyundai Motor value-up"),
    ),
    Round6OverlaySector.THEME_TECH_EXPECTATION: Round6OverlayDefinition(
        overlay_sector=Round6OverlaySector.THEME_TECH_EXPECTATION,
        korean_name="테마/기술 기대",
        archetypes=(
            E2RArchetype.ROBOTICS_FACTORY_AUTOMATION,
            E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
            E2RArchetype.GAME_CONTENT_IP,
            E2RArchetype.BIOTECH_REGULATORY,
            E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY,
            E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION,
            E2RArchetype.ONE_OFF_EVENT_DEMAND,
            E2RArchetype.THEME_VALUATION_OVERHEAT,
        ),
        posture=Round6ValidationPosture.REDTEAM_FIRST,
        stage1_signals=("strategic_investment", "mau_or_download_spike", "new_game_or_trial_news", "theme_rally"),
        stage2_signals=("revenue_conversion", "op_eps_revision", "royalty_or_milestone", "repeat_monetization"),
        stage3_requires=("actual_cash_flow_conversion", "repeat_revenue", "low_dilution_or_regulation_risk", "valuation_not_overheated"),
        stage4b_signals=("narrative_overheated", "tam_report_crowding", "price_ahead_of_eps", "multiple_saturation"),
        stage4c_signals=("revenue_conversion_failure", "clinical_failure", "governance_legal_risk", "ai_cost_overrun"),
        price_validation_focus=("theme_overheat", "accounting_trust_break", "price_moved_without_evidence", "false_green"),
        green_policy="Green is blocked or rare until revenue, OP, FCF, or royalty conversion is proven.",
        examples=("Rainbow Robotics", "NAVER/Kakao", "Krafton/Shift Up", "pre-revenue biotech"),
    ),
    Round6OverlaySector.RECURRING_EXPORT_BRAND: Round6OverlayDefinition(
        overlay_sector=Round6OverlaySector.RECURRING_EXPORT_BRAND,
        korean_name="반복수출/브랜드",
        archetypes=(
            E2RArchetype.EXPORT_RECURRING_CONSUMER,
            E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
            E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
            E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        ),
        posture=Round6ValidationPosture.STRUCTURAL_GREEN_POSSIBLE,
        stage1_signals=("export_growth", "channel_expansion", "regulatory_or_export_approval", "opm_surprise"),
        stage2_signals=("fy1_fy2_revision", "repeat_order_or_consumable", "opm_roe_improvement", "customer_or_channel_diversification"),
        stage3_requires=("recurring_demand", "global_channel_scale", "high_fcf_conversion", "low_inventory_or_regulatory_risk"),
        stage4b_signals=("margin_peak", "crowded_export_reports", "channel_inventory_risk", "target_multiple_saturated"),
        stage4c_signals=("export_slowdown", "inventory_or_receivables_spike", "approval_delay", "asp_decline"),
        price_validation_focus=("stair_step_rerating", "straight_rerating", "mfe_1y", "time_to_100pct"),
        green_policy="Green possible when repeat demand/channel expansion, OPM, and revisions move together.",
        examples=("삼양식품", "실리콘투", "Classys", "삼성바이오로직스 CDMO"),
    ),
}


ROUND6_ARCHETYPE_OVERLAYS: Mapping[E2RArchetype, tuple[Round6OverlaySector, ...]] = {}
for _sector, _definition in ROUND6_OVERLAY_DEFINITIONS.items():
    for _archetype in _definition.archetypes:
        ROUND6_ARCHETYPE_OVERLAYS = {
            **ROUND6_ARCHETYPE_OVERLAYS,
            _archetype: tuple(dict.fromkeys((*ROUND6_ARCHETYPE_OVERLAYS.get(_archetype, ()), _sector))),
        }


def round6_overlays_for(archetype: E2RArchetype | str) -> tuple[Round6OverlaySector, ...]:
    item = _archetype(archetype)
    return ROUND6_ARCHETYPE_OVERLAYS.get(item, (Round6OverlaySector.THEME_TECH_EXPECTATION,))


def round6_primary_overlay_for(archetype: E2RArchetype | str) -> Round6OverlaySector:
    return round6_overlays_for(archetype)[0]


def round6_definition(overlay: Round6OverlaySector | str) -> Round6OverlayDefinition:
    item = overlay if isinstance(overlay, Round6OverlaySector) else Round6OverlaySector(str(overlay))
    return ROUND6_OVERLAY_DEFINITIONS[item]


def round6_overlay_rows() -> tuple[dict[str, object], ...]:
    rows: list[dict[str, object]] = []
    for archetype in E2RArchetype:
        overlays = round6_overlays_for(archetype)
        primary = overlays[0]
        definition = round6_definition(primary)
        rows.append(
            {
                "archetype": archetype.value,
                "primary_overlay": primary.value,
                "secondary_overlays": "|".join(item.value for item in overlays[1:]),
                "korean_name": definition.korean_name,
                "posture": definition.posture.value,
                "green_policy": definition.green_policy,
                "price_validation_focus": "|".join(definition.price_validation_focus),
            }
        )
    return tuple(rows)


def round6_case_coverage(records: Iterable[E2RCaseRecord]) -> tuple[dict[str, object], ...]:
    record_tuple = tuple(records)
    rows: list[dict[str, object]] = []
    for overlay in Round6OverlaySector:
        definition = round6_definition(overlay)
        subset = tuple(record for record in record_tuple if overlay in round6_overlays_for(record.primary_archetype))
        rows.append(
            {
                "overlay_sector": overlay.value,
                "korean_name": definition.korean_name,
                "posture": definition.posture.value,
                "case_count": len(subset),
                "price_backfill_needed_count": sum(
                    1 for record in subset if record.price_validation.price_validation_status != "price_filled"
                ),
                "unknown_alignment_count": sum(1 for record in subset if record.score_price_alignment == "unknown"),
                "false_positive_or_theme_count": sum(
                    1
                    for record in subset
                    if record.score_price_alignment == "false_positive_score"
                    or record.rerating_result in {"theme_overheat", "event_premium", "credit_relief_rally"}
                ),
            }
        )
    return tuple(rows)


def write_round6_missing_sector_reports(
    *,
    case_path: str | Path = "data/e2r_case_library/cases_v02.jsonl",
    output_directory: str | Path = "output/e2r_round6_missing_sector_correction",
) -> dict[str, Path]:
    records = load_case_library(case_path)
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "framework": output / "round6_missing_sector_framework.md",
        "overlay_matrix": output / "round6_archetype_overlay_matrix.csv",
        "price_contract": output / "round6_price_path_validation_contract.md",
        "coverage": output / "round6_case_coverage_by_overlay.csv",
        "next_plan": output / "round6_next_case_backfill_plan.md",
    }
    paths["framework"].write_text(render_round6_framework_markdown(), encoding="utf-8")
    _write_overlay_matrix(paths["overlay_matrix"])
    paths["price_contract"].write_text(render_round6_price_contract_markdown(), encoding="utf-8")
    _write_case_coverage_csv(records, paths["coverage"])
    paths["next_plan"].write_text(render_round6_next_plan_markdown(records), encoding="utf-8")
    return paths


def render_round6_framework_markdown() -> str:
    lines = [
        "# Round-6 Missing-Sector Correction Framework",
        "",
        f"Source round: `{ROUND6_SOURCE_ROUND_PATH}`",
        "",
        "This is calibration material. It does not change production scoring.",
        "",
        "## Overlay Sectors",
        "",
        "| overlay | Korean name | posture | archetypes |",
        "|---|---|---|---:|",
    ]
    for definition in ROUND6_OVERLAY_DEFINITIONS.values():
        lines.append(
            f"| {definition.overlay_sector.value} | {definition.korean_name} | "
            f"{definition.posture.value} | {len(definition.archetypes)} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Overlays are cross-sector corrections. They do not replace Round-5 large sectors.",
            "- Example: AI data-center infrastructure can touch transformers, PCB, cooling, and memory/HBM.",
            "- Example: construction and utilities can look cheap, but PF, debt, tariff, and cash-flow risk dominate.",
            "",
            "## Guardrails",
            "- Do not use overlay labels as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds from this report.",
            "- Fill price paths before applying any score-weight changes.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round6_price_contract_markdown() -> str:
    lines = [
        "# Round-6 Price-Path Validation Contract",
        "",
        "Round 6 requires case records to explain whether score, stage, price path, 4B, and 4C fit together.",
        "",
        "## Required Price Fields",
    ]
    for item in ROUND6_PRICE_VALIDATION_FIELDS:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Price Pattern Values"])
    for item in ROUND6_PRICE_PATTERN_VALUES:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## Easy Example",
            "",
            "`HMM 2020~2021` can have explosive EPS and price movement, but if freight normalizes and EPS collapses, "
            "the price pattern is closer to `cycle_boom_bust` than structural Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round6_next_plan_markdown(records: Iterable[E2RCaseRecord]) -> str:
    rows = round6_case_coverage(records)
    lines = [
        "# Round-6 Next Case Backfill Plan",
        "",
        "| overlay | cases | price_backfill_needed | unknown_alignment | priority |",
        "|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['overlay_sector']} | {row['case_count']} | {row['price_backfill_needed_count']} | "
            f"{row['unknown_alignment_count']} | {_priority(row)} |"
        )
    lines.extend(
        [
            "",
            "## Next Work",
            "- Backfill MFE/MAE and time-to-return fields first.",
            "- Classify price patterns before changing score weights.",
            "- Keep robotics, platform, games, pre-revenue biotech, shipping, construction, and theme cases RedTeam-first.",
        ]
    )
    return "\n".join(lines) + "\n"


def _write_overlay_matrix(path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = (
            "archetype",
            "primary_overlay",
            "secondary_overlays",
            "korean_name",
            "posture",
            "green_policy",
            "price_validation_focus",
        )
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in round6_overlay_rows():
            writer.writerow(row)
    return path


def _write_case_coverage_csv(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = (
            "overlay_sector",
            "korean_name",
            "posture",
            "case_count",
            "price_backfill_needed_count",
            "unknown_alignment_count",
            "false_positive_or_theme_count",
        )
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in round6_case_coverage(records):
            writer.writerow(row)
    return path


def _priority(row: Mapping[str, object]) -> str:
    if int(row["price_backfill_needed_count"]) > 0:
        return "backfill_price_path"
    if int(row["unknown_alignment_count"]) > 0:
        return "classify_score_price_alignment"
    if str(row["posture"]) in {Round6ValidationPosture.REDTEAM_FIRST.value, Round6ValidationPosture.CYCLE_OR_EVENT_CAPPED.value}:
        return "add_counterexamples"
    return "ready_for_shadow_weight_review"


def _archetype(value: E2RArchetype | str) -> E2RArchetype:
    if isinstance(value, E2RArchetype):
        return value
    return E2RArchetype(str(value))


__all__ = [
    "ROUND6_ARCHETYPE_OVERLAYS",
    "ROUND6_OVERLAY_DEFINITIONS",
    "ROUND6_PRICE_PATTERN_VALUES",
    "ROUND6_PRICE_VALIDATION_FIELDS",
    "ROUND6_SOURCE_ROUND_PATH",
    "Round6OverlayDefinition",
    "Round6OverlaySector",
    "Round6ValidationPosture",
    "render_round6_framework_markdown",
    "render_round6_next_plan_markdown",
    "render_round6_price_contract_markdown",
    "round6_case_coverage",
    "round6_definition",
    "round6_overlay_rows",
    "round6_overlays_for",
    "round6_primary_overlay_for",
    "write_round6_missing_sector_reports",
]
