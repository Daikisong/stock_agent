"""Round-1 E2R sector research framework.

This module captures the analyst's research taxonomy before production scoring
changes. It separates the Round-1 core archetypes from later extension
archetypes so the case library can grow without pretending that every extension
is ready for Green scoring.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import E2RCaseRecord, load_case_library


class E2RArchetypeBlock(str, Enum):
    """Research block from the analyst's Round-1 synthesis."""

    STRUCTURAL_E2R = "STRUCTURAL_E2R"
    CYCLICAL_SPREAD_GUARDRAILED = "CYCLICAL_SPREAD_GUARDRAILED"
    RED_YELLOW_GUARDRAIL = "RED_YELLOW_GUARDRAIL"
    EXTENSION_REFINEMENT = "EXTENSION_REFINEMENT"


ROUND1_STRUCTURAL_CORE = (
    E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
    E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
    E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,
    E2RArchetype.EXPORT_RECURRING_CONSUMER,
    E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
    E2RArchetype.MEMORY_HBM_CAPACITY,
    E2RArchetype.SEMI_EQUIPMENT_CAPEX,
    E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
    E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
    E2RArchetype.TURNAROUND_COST_RESTRUCTURING,
)

ROUND1_CYCLICAL_CORE = (
    E2RArchetype.COMMODITY_SPREAD,
    E2RArchetype.SHIPPING_FREIGHT_CYCLE,
    E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
    E2RArchetype.AUTO_MOBILITY_COMPONENTS,
    E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
    E2RArchetype.UTILITIES_REGULATED_TARIFF,
)

ROUND1_GUARDRAIL_CORE = (
    E2RArchetype.BIOTECH_REGULATORY,
    E2RArchetype.ROBOTICS_FACTORY_AUTOMATION,
    E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
    E2RArchetype.GAME_CONTENT_IP,
    E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
    E2RArchetype.ONE_OFF_EVENT_DEMAND,
    E2RArchetype.THEME_VALUATION_OVERHEAT,
    E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
    E2RArchetype.GENERIC_UNCLASSIFIED,
)

ROUND1_CORE_ARCHETYPES = ROUND1_STRUCTURAL_CORE + ROUND1_CYCLICAL_CORE + ROUND1_GUARDRAIL_CORE


EXTENSION_TO_ROUND1_CORE: Mapping[E2RArchetype, E2RArchetype] = {
    E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE: E2RArchetype.SEMI_EQUIPMENT_CAPEX,
    E2RArchetype.NUCLEAR_SMR_GRID_POLICY: E2RArchetype.UTILITIES_REGULATED_TARIFF,
    E2RArchetype.TRAVEL_LEISURE_REOPENING: E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
    E2RArchetype.EDUCATION_SPECIALTY_SERVICES: E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
    E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS: E2RArchetype.COMMODITY_SPREAD,
    E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN: E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
    E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY: E2RArchetype.BIOTECH_REGULATORY,
    E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION: E2RArchetype.BIOTECH_REGULATORY,
    E2RArchetype.CDMO_HEALTHCARE_CONTRACT: E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
    E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE: E2RArchetype.AUTO_MOBILITY_COMPONENTS,
}


def _weights(
    eps_fcf: float,
    visibility: float,
    bottleneck: float,
    mispricing: float,
    valuation: float,
) -> Mapping[str, float]:
    return {
        "eps_fcf_explosion": eps_fcf,
        "structural_visibility": visibility,
        "bottleneck_pricing": bottleneck,
        "market_mispricing": mispricing,
        "valuation_rerating": valuation,
    }


ROUND1_SCORE_WEIGHT_DRAFT: Mapping[E2RArchetype, Mapping[str, float]] = {
    E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL: _weights(20, 24, 22, 14, 12),
    E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG: _weights(20, 24, 17, 14, 14),
    E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG: _weights(20, 22, 18, 13, 13),
    E2RArchetype.EXPORT_RECURRING_CONSUMER: _weights(22, 23, 12, 16, 13),
    E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION: _weights(22, 23, 12, 16, 13),
    E2RArchetype.MEMORY_HBM_CAPACITY: _weights(24, 21, 19, 15, 12),
    E2RArchetype.SEMI_EQUIPMENT_CAPEX: _weights(22, 20, 18, 14, 12),
    E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT: _weights(20, 16, 14, 10, 10),
    E2RArchetype.COMMODITY_SPREAD: _weights(20, 12, 18, 10, 10),
    E2RArchetype.SHIPPING_FREIGHT_CYCLE: _weights(20, 10, 18, 8, 8),
    E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET: _weights(15, 20, 5, 15, 25),
    E2RArchetype.BIOTECH_REGULATORY: _weights(5, 15, 5, 10, 5),
    E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT: _weights(20, 22, 13, 14, 12),
    E2RArchetype.PLATFORM_SOFTWARE_INTERNET: _weights(20, 22, 8, 16, 14),
    E2RArchetype.TURNAROUND_COST_RESTRUCTURING: _weights(22, 18, 8, 15, 12),
    E2RArchetype.ONE_OFF_EVENT_DEMAND: _weights(20, 5, 5, 5, 5),
    E2RArchetype.THEME_VALUATION_OVERHEAT: _weights(10, 5, 5, 5, 5),
}


@dataclass(frozen=True)
class Round1ArchetypeMapping:
    """One archetype's Round-1 core/extension mapping."""

    archetype: E2RArchetype
    block: E2RArchetypeBlock
    round1_core_archetype: E2RArchetype
    is_round1_core: bool
    notes: str


def round1_block(archetype: E2RArchetype | str) -> E2RArchetypeBlock:
    """Return the Round-1 research block for an archetype."""

    item = _archetype(archetype)
    core = round1_core_for(item)
    if item not in ROUND1_CORE_ARCHETYPES:
        return E2RArchetypeBlock.EXTENSION_REFINEMENT
    if core in ROUND1_STRUCTURAL_CORE:
        return E2RArchetypeBlock.STRUCTURAL_E2R
    if core in ROUND1_CYCLICAL_CORE:
        return E2RArchetypeBlock.CYCLICAL_SPREAD_GUARDRAILED
    return E2RArchetypeBlock.RED_YELLOW_GUARDRAIL


def round1_core_for(archetype: E2RArchetype | str) -> E2RArchetype:
    """Map extension archetypes back to a Round-1 core bucket."""

    item = _archetype(archetype)
    return EXTENSION_TO_ROUND1_CORE.get(item, item)


def round1_mapping(archetype: E2RArchetype | str) -> Round1ArchetypeMapping:
    item = _archetype(archetype)
    core = round1_core_for(item)
    is_core = item in ROUND1_CORE_ARCHETYPES
    block = round1_block(item)
    notes = "round1_core" if is_core else f"extension_refinement_of:{core.value}"
    return Round1ArchetypeMapping(item, block, core, is_core, notes)


def all_round1_mappings() -> tuple[Round1ArchetypeMapping, ...]:
    return tuple(round1_mapping(item) for item in E2RArchetype)


def summarize_round1_case_mapping(records: Iterable[E2RCaseRecord]) -> dict[str, object]:
    rows = tuple(records)
    block_counts: dict[str, int] = {}
    core_counts: dict[str, int] = {}
    extension_count = 0
    for record in rows:
        mapping = round1_mapping(record.primary_archetype)
        block_counts[mapping.block.value] = block_counts.get(mapping.block.value, 0) + 1
        core_counts[mapping.round1_core_archetype.value] = core_counts.get(mapping.round1_core_archetype.value, 0) + 1
        if not mapping.is_round1_core:
            extension_count += 1
    return {
        "case_count": len(rows),
        "round1_core_archetype_count": len(ROUND1_CORE_ARCHETYPES),
        "current_archetype_enum_count": len(tuple(E2RArchetype)),
        "extension_archetype_count": len(tuple(E2RArchetype)) - len(ROUND1_CORE_ARCHETYPES),
        "cases_using_extension_archetypes": extension_count,
        "block_counts": block_counts,
        "core_counts": core_counts,
    }


def write_round1_framework_reports(
    *,
    case_path: str | Path = "data/e2r_case_library/cases_v02.jsonl",
    output_directory: str | Path = "output/e2r_research_framework",
) -> dict[str, Path]:
    """Write Round-1 framework reports."""

    records = load_case_library(case_path)
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    summary_path = output / "round1_framework_summary.md"
    block_path = output / "round1_archetype_blocks.csv"
    case_path_out = output / "round1_case_mapping.csv"
    weight_path = output / "round1_score_weight_draft.md"
    summary_path.write_text(render_round1_framework_summary(records), encoding="utf-8")
    _write_block_csv(block_path)
    _write_case_mapping_csv(records, case_path_out)
    weight_path.write_text(render_round1_score_weight_draft(), encoding="utf-8")
    return {
        "summary": summary_path,
        "archetype_blocks": block_path,
        "case_mapping": case_path_out,
        "score_weight_draft": weight_path,
    }


def render_round1_framework_summary(records: Iterable[E2RCaseRecord]) -> str:
    summary = summarize_round1_case_mapping(records)
    lines = [
        "# Round-1 E2R Research Framework",
        "",
        f"- round1_core_archetype_count: {summary['round1_core_archetype_count']}",
        f"- current_archetype_enum_count: {summary['current_archetype_enum_count']}",
        f"- extension_archetype_count: {summary['extension_archetype_count']}",
        f"- case_count: {summary['case_count']}",
        f"- cases_using_extension_archetypes: {summary['cases_using_extension_archetypes']}",
        "",
        "## Three Research Blocks",
    ]
    for block, count in sorted(dict(summary["block_counts"]).items()):
        lines.append(f"- {block}: {count}")
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Round-1 core keeps the analyst's 25-archetype frame.",
            "- Extension archetypes are retained as refinements, but they roll up to a Round-1 core bucket.",
            "- This report does not change production scoring.",
            "- Score-weight draft values are research notes and must not be applied until case/path coverage is sufficient.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round1_score_weight_draft() -> str:
    lines = [
        "# Round-1 Score Weight Draft",
        "",
        "These weights are copied into a research report only. They are not applied to production scoring.",
        "",
        "| archetype | EPS/FCF | visibility | bottleneck/pricing | mispricing | valuation |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for archetype in ROUND1_CORE_ARCHETYPES:
        weights = ROUND1_SCORE_WEIGHT_DRAFT.get(archetype)
        if not weights:
            continue
        lines.append(
            "| "
            + archetype.value
            + f" | {weights['eps_fcf_explosion']:g} | {weights['structural_visibility']:g} | "
            + f"{weights['bottleneck_pricing']:g} | {weights['market_mispricing']:g} | {weights['valuation_rerating']:g} |"
        )
    lines.extend(
        [
            "",
            "## Guardrails",
            "- Contract/backlog evidence is not universal.",
            "- Cycle/spread archetypes need Green caps and stronger Red/Yellow handling.",
            "- One-off and theme/overheat archetypes are primarily guardrail archetypes.",
        ]
    )
    return "\n".join(lines) + "\n"


def _write_block_csv(path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("archetype", "round1_core_archetype", "block", "is_round1_core", "notes"),
        )
        writer.writeheader()
        for mapping in all_round1_mappings():
            writer.writerow(
                {
                    "archetype": mapping.archetype.value,
                    "round1_core_archetype": mapping.round1_core_archetype.value,
                    "block": mapping.block.value,
                    "is_round1_core": str(mapping.is_round1_core).lower(),
                    "notes": mapping.notes,
                }
            )
    return path


def _write_case_mapping_csv(records: tuple[E2RCaseRecord, ...], path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("case_id", "symbol", "company_name", "archetype", "round1_core_archetype", "block", "case_type"),
        )
        writer.writeheader()
        for record in records:
            mapping = round1_mapping(record.primary_archetype)
            writer.writerow(
                {
                    "case_id": record.case_id,
                    "symbol": record.symbol,
                    "company_name": record.company_name,
                    "archetype": record.primary_archetype.value,
                    "round1_core_archetype": mapping.round1_core_archetype.value,
                    "block": mapping.block.value,
                    "case_type": record.case_type,
                }
            )
    return path


def _archetype(value: E2RArchetype | str) -> E2RArchetype:
    if isinstance(value, E2RArchetype):
        return value
    return E2RArchetype(str(value))


__all__ = [
    "E2RArchetypeBlock",
    "EXTENSION_TO_ROUND1_CORE",
    "ROUND1_CORE_ARCHETYPES",
    "ROUND1_CYCLICAL_CORE",
    "ROUND1_GUARDRAIL_CORE",
    "ROUND1_SCORE_WEIGHT_DRAFT",
    "ROUND1_STRUCTURAL_CORE",
    "Round1ArchetypeMapping",
    "all_round1_mappings",
    "render_round1_framework_summary",
    "render_round1_score_weight_draft",
    "round1_block",
    "round1_core_for",
    "round1_mapping",
    "summarize_round1_case_mapping",
    "write_round1_framework_reports",
]
