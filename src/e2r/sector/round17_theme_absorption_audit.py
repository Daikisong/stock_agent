"""Round-17 theme absorption audit.

Round 17 turns the v0.5 theme coverage discussion into an explicit audit:
raw theme tags are checked against the current coverage map, unmatched tags are
reported, and the Green/Watch/Red distribution is made machine-readable.

This module is calibration/report material only. Theme tags route research and
case mining; they do not become score evidence or production candidate labels.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round16_theme_coverage_v05 import Round16ThemeCoverageEntry, round16_coverage_entries


ROUND17_SOURCE_ROUND_PATH = "docs/round/round_17.md"
ROUND17_ARCHIVED_SOURCE_ROUND_PATH = "docs/round/achieve/round_17.md"
ROUND17_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round17_theme_absorption_audit"
ROUND17_DEFAULT_THEME_MAP_PATH = "data/sector_taxonomy/theme_tag_map_v05.csv"
ROUND17_DEFAULT_ALIAS_PATH = "data/sector_taxonomy/theme_aliases_round17.yml"


@dataclass(frozen=True)
class Round17ThemeExpectation:
    theme_tag: str
    large_sector_korean: str
    primary_archetype: str
    green_policy: str


@dataclass(frozen=True)
class _SupplementalProfile:
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    must_have_evidence: tuple[str, ...]
    red_flag_evidence: tuple[str, ...]
    note: str


@dataclass(frozen=True)
class Round17ThemeAuditRecord:
    theme_tag: str
    large_sector_korean: str
    primary_archetype: str
    canonical_archetype: str
    posture: str
    green_policy: str
    mapped: bool
    mapped_via: str
    matched_theme_tag: str
    must_have_evidence: tuple[str, ...]
    red_flag_evidence: tuple[str, ...]
    theme_is_score_input: bool
    production_scoring_changed: bool
    source_round: str
    mapping_note: str = ""

    def as_row(self) -> dict[str, str]:
        return {
            "theme_tag": self.theme_tag,
            "large_sector": self.large_sector_korean,
            "primary_archetype": self.primary_archetype,
            "canonical_archetype": self.canonical_archetype,
            "posture": self.posture,
            "green_policy": self.green_policy,
            "mapped": str(self.mapped).lower(),
            "mapped_via": self.mapped_via,
            "matched_theme_tag": self.matched_theme_tag,
            "must_have_evidence": "|".join(self.must_have_evidence),
            "red_flag_evidence": "|".join(self.red_flag_evidence),
            "theme_is_score_input": str(self.theme_is_score_input).lower(),
            "production_scoring_changed": str(self.production_scoring_changed).lower(),
            "source_round": self.source_round,
            "mapping_note": self.mapping_note,
        }


ROUND17_SUPPLEMENTAL_PROFILES: Mapping[str, _SupplementalProfile] = {
    "CRO_CLINICAL_SERVICE": _SupplementalProfile(
        canonical_archetype=E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        must_have_evidence=("service_contract", "clinical_volume", "utilization", "opm_fcf_conversion"),
        red_flag_evidence=("project_delay", "customer_concentration", "trial_volume_without_margin"),
        note="CRO is kept as a healthcare service route; Green needs contract/utilization and cash-flow conversion.",
    ),
    "CONSUMER_REGULATED_PRODUCT": _SupplementalProfile(
        canonical_archetype=E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        posture=Round10ThemePosture.WATCH_YELLOW_FIRST,
        must_have_evidence=("regulated_revenue", "repeat_demand", "margin_visibility", "compliance_record"),
        red_flag_evidence=("regulatory_change", "tax_hike", "youth_access_risk", "one_product_event"),
        note="Regulated consumer products stay Watch until repeat demand and compliance economics are visible.",
    ),
}


def parse_round17_theme_expectations(
    path: str | Path = ROUND17_SOURCE_ROUND_PATH,
) -> tuple[Round17ThemeExpectation, ...]:
    """Parse the Round-17 v0.5 markdown theme table."""

    text_path = _resolve_round17_source_path(path)
    lines = text_path.read_text(encoding="utf-8").splitlines()
    in_theme_table = False
    expectations: list[Round17ThemeExpectation] = []
    for line in lines:
        if line.startswith("| theme_tag") and "primary_archetype" in line and "green_policy" in line:
            in_theme_table = True
            continue
        if not in_theme_table:
            continue
        if not line.startswith("|"):
            break
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 4 or _is_separator_row(parts):
            continue
        expectations.append(
            Round17ThemeExpectation(
                theme_tag=parts[0],
                large_sector_korean=parts[1],
                primary_archetype=parts[2],
                green_policy=parts[3],
            )
        )
    return tuple(expectations)


def _resolve_round17_source_path(path: str | Path) -> Path:
    text_path = Path(path)
    if text_path.exists():
        return text_path
    archived_path = Path(ROUND17_ARCHIVED_SOURCE_ROUND_PATH)
    if text_path.as_posix() == ROUND17_SOURCE_ROUND_PATH and archived_path.exists():
        return archived_path
    return text_path


def round17_theme_audit_records(path: str | Path = ROUND17_SOURCE_ROUND_PATH) -> tuple[Round17ThemeAuditRecord, ...]:
    entries = round16_coverage_entries()
    by_theme = _index_entries_by_theme(entries)
    by_sub_archetype = _index_entries_by_sub_archetype(entries)
    by_canonical_archetype = _index_entries_by_canonical(entries)
    records: list[Round17ThemeAuditRecord] = []
    for expectation in parse_round17_theme_expectations(path):
        records.append(
            _resolve_expectation(
                expectation,
                by_theme=by_theme,
                by_sub_archetype=by_sub_archetype,
                by_canonical_archetype=by_canonical_archetype,
            )
        )
    return tuple(records)


def round17_theme_map_rows(path: str | Path = ROUND17_SOURCE_ROUND_PATH) -> tuple[dict[str, str], ...]:
    return tuple(record.as_row() for record in round17_theme_audit_records(path))


def round17_coverage_summary(path: str | Path = ROUND17_SOURCE_ROUND_PATH) -> dict[str, int | bool | str]:
    records = round17_theme_audit_records(path)
    mapped = sum(1 for record in records if record.mapped)
    unmatched = len(records) - mapped
    return {
        "total_theme_tags": len(records),
        "mapped_theme_tags": mapped,
        "unmatched_theme_tags": unmatched,
        "large_sector_count": len({record.large_sector_korean for record in records}),
        "archetype_count": len({record.primary_archetype for record in records}),
        "green_allowed": sum(1 for record in records if record.green_policy == "green_allowed"),
        "watch_to_green": sum(1 for record in records if record.green_policy == "watch_to_green"),
        "watch_only": sum(1 for record in records if record.green_policy == "watch_only"),
        "red_watch": sum(1 for record in records if record.green_policy == "red_watch"),
        "event_watch": sum(1 for record in records if record.green_policy == "event_watch"),
        "event_only": sum(1 for record in records if record.green_policy == "event_only"),
        "red_flag": sum(1 for record in records if record.green_policy == "red_flag"),
        "production_scoring_changed": False,
        "theme_tags_are_score_input": False,
        "scoring_ready": False,
        "coverage_status": "mapped_ready_for_case_mining" if unmatched == 0 else "needs_unmatched_theme_review",
    }


def round17_green_policy_distribution(path: str | Path = ROUND17_SOURCE_ROUND_PATH) -> tuple[dict[str, str], ...]:
    records = round17_theme_audit_records(path)
    counts: dict[str, int] = {}
    for record in records:
        counts[record.green_policy] = counts.get(record.green_policy, 0) + 1
    return tuple({"green_policy": key, "count": str(value)} for key, value in sorted(counts.items()))


def round17_unmatched_theme_rows(path: str | Path = ROUND17_SOURCE_ROUND_PATH) -> tuple[dict[str, str], ...]:
    return tuple(row for row in round17_theme_map_rows(path) if row["mapped"] == "false")


def render_round17_theme_coverage_report(path: str | Path = ROUND17_SOURCE_ROUND_PATH) -> str:
    summary = round17_coverage_summary(path)
    lines = [
        "# Round-17 Theme Absorption Audit",
        "",
        f"- source_round: `{ROUND17_SOURCE_ROUND_PATH}`",
        f"- total_theme_tags: {summary['total_theme_tags']}",
        f"- mapped_theme_tags: {summary['mapped_theme_tags']}",
        f"- unmatched_theme_tags: {summary['unmatched_theme_tags']}",
        f"- large_sector_count: {summary['large_sector_count']}",
        f"- archetype_count: {summary['archetype_count']}",
        f"- production_scoring_changed: {str(summary['production_scoring_changed']).lower()}",
        f"- theme_tags_are_score_input: {str(summary['theme_tags_are_score_input']).lower()}",
        f"- scoring_ready: {str(summary['scoring_ready']).lower()}",
        f"- coverage_status: `{summary['coverage_status']}`",
        "",
        "## Green Policy Distribution",
    ]
    for row in round17_green_policy_distribution(path):
        lines.append(f"- {row['green_policy']}: {row['count']}")
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Round 17 confirms structural theme absorption, not production scoring readiness.",
            "- Raw theme tags are search/routing tags. They are not score evidence.",
            "- Example: `초전도체` routes to speculative science RedTeam review; it does not create E2R score.",
            "- Example: `전력설비` may route to contract/backlog research, but Stage 3 needs contracts, "
            "backlog, margin, and revision evidence.",
            "",
            "## Unmatched Theme Tags",
        ]
    )
    unmatched = round17_unmatched_theme_rows(path)
    if unmatched:
        for row in unmatched:
            lines.append(f"- {row['theme_tag']} -> expected `{row['primary_archetype']}`")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not lower Stage 3-Green thresholds to improve theme coverage.",
            "- Do not use raw theme names as score evidence.",
            "- Do not use benchmark or case labels as candidate-generation input.",
            "- Do not treat event/policy/speculative tags as structural E2R without EPS/FCF evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round17_alias_yaml(path: str | Path = ROUND17_SOURCE_ROUND_PATH) -> str:
    aliases: dict[str, str] = {}
    for record in round17_theme_audit_records(path):
        if (
            record.mapped
            and record.matched_theme_tag
            and record.matched_theme_tag != record.theme_tag
            and _is_reasonable_alias(record.theme_tag, record.matched_theme_tag)
        ):
            aliases[record.theme_tag] = record.matched_theme_tag
    lines = [
        "# Round-17 generated theme aliases.",
        "# Aliases normalize raw theme labels for coverage audit only.",
        "# They are not production scoring evidence.",
        "aliases:",
    ]
    for key, value in sorted(aliases.items()):
        lines.append(f'  "{key}": "{value}"')
    if not aliases:
        lines.append("  {}")
    return "\n".join(lines) + "\n"


def write_round17_theme_absorption_reports(
    *,
    round_doc_path: str | Path = ROUND17_SOURCE_ROUND_PATH,
    output_directory: str | Path = ROUND17_DEFAULT_OUTPUT_DIRECTORY,
    theme_map_path: str | Path = ROUND17_DEFAULT_THEME_MAP_PATH,
    alias_path: str | Path = ROUND17_DEFAULT_ALIAS_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    theme_map = Path(theme_map_path)
    alias_file = Path(alias_path)
    theme_map.parent.mkdir(parents=True, exist_ok=True)
    alias_file.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "theme_map": theme_map,
        "aliases": alias_file,
        "summary_json": output / "round17_theme_coverage_audit.json",
        "summary_md": output / "theme_coverage_report.md",
        "coverage_matrix": output / "theme_coverage_matrix.csv",
        "unmatched": output / "unmatched_theme_tags.csv",
        "green_policy_distribution": output / "green_policy_distribution.csv",
    }
    rows = round17_theme_map_rows(round_doc_path)
    _write_rows(rows, paths["theme_map"])
    _write_rows(rows, paths["coverage_matrix"])
    _write_rows(round17_unmatched_theme_rows(round_doc_path), paths["unmatched"])
    _write_rows(round17_green_policy_distribution(round_doc_path), paths["green_policy_distribution"])
    paths["aliases"].write_text(render_round17_alias_yaml(round_doc_path), encoding="utf-8")
    paths["summary_json"].write_text(
        json.dumps(round17_coverage_summary(round_doc_path), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    paths["summary_md"].write_text(render_round17_theme_coverage_report(round_doc_path), encoding="utf-8")
    return paths


def _resolve_expectation(
    expectation: Round17ThemeExpectation,
    *,
    by_theme: Mapping[str, tuple[Round16ThemeCoverageEntry, ...]],
    by_sub_archetype: Mapping[str, tuple[Round16ThemeCoverageEntry, ...]],
    by_canonical_archetype: Mapping[str, tuple[Round16ThemeCoverageEntry, ...]],
) -> Round17ThemeAuditRecord:
    exact_matches = by_theme.get(_normalize_theme_tag(expectation.theme_tag), ())
    if exact_matches:
        best = _choose_best_entry(expectation.primary_archetype, exact_matches)
        if (
            best.primary_sub_archetype == expectation.primary_archetype
            or best.canonical_archetype.value == expectation.primary_archetype
        ):
            return _record_from_entry(expectation, best, mapped_via="round16_exact_theme")
    if expectation.primary_archetype in by_sub_archetype:
        best = by_sub_archetype[expectation.primary_archetype][0]
        return _record_from_entry(expectation, best, mapped_via="round16_sub_archetype")
    supplemental = ROUND17_SUPPLEMENTAL_PROFILES.get(expectation.primary_archetype)
    if supplemental is not None:
        return Round17ThemeAuditRecord(
            theme_tag=expectation.theme_tag,
            large_sector_korean=expectation.large_sector_korean,
            primary_archetype=expectation.primary_archetype,
            canonical_archetype=supplemental.canonical_archetype.value,
            posture=supplemental.posture.value,
            green_policy=expectation.green_policy,
            mapped=True,
            mapped_via="round17_supplemental",
            matched_theme_tag=expectation.theme_tag,
            must_have_evidence=supplemental.must_have_evidence,
            red_flag_evidence=supplemental.red_flag_evidence,
            theme_is_score_input=False,
            production_scoring_changed=False,
            source_round="round17",
            mapping_note=supplemental.note,
        )
    if exact_matches:
        best = _choose_best_entry(expectation.primary_archetype, exact_matches)
        return _record_from_entry(expectation, best, mapped_via="round16_exact_theme_fallback")
    if expectation.primary_archetype in by_canonical_archetype:
        best = by_canonical_archetype[expectation.primary_archetype][0]
        return _record_from_entry(expectation, best, mapped_via="round16_canonical_archetype")
    return Round17ThemeAuditRecord(
        theme_tag=expectation.theme_tag,
        large_sector_korean=expectation.large_sector_korean,
        primary_archetype=expectation.primary_archetype,
        canonical_archetype="",
        posture="",
        green_policy=expectation.green_policy,
        mapped=False,
        mapped_via="unmatched",
        matched_theme_tag="",
        must_have_evidence=(),
        red_flag_evidence=(),
        theme_is_score_input=False,
        production_scoring_changed=False,
        source_round="round17",
        mapping_note="No Round-16 or Round-17 supplemental profile matched this tag.",
    )


def _record_from_entry(
    expectation: Round17ThemeExpectation,
    entry: Round16ThemeCoverageEntry,
    *,
    mapped_via: str,
) -> Round17ThemeAuditRecord:
    return Round17ThemeAuditRecord(
        theme_tag=expectation.theme_tag,
        large_sector_korean=expectation.large_sector_korean,
        primary_archetype=expectation.primary_archetype,
        canonical_archetype=entry.canonical_archetype.value,
        posture=entry.posture.value,
        green_policy=expectation.green_policy,
        mapped=True,
        mapped_via=mapped_via,
        matched_theme_tag=entry.theme_tag,
        must_have_evidence=entry.must_have_evidence,
        red_flag_evidence=entry.red_flag_evidence,
        theme_is_score_input=False,
        production_scoring_changed=False,
        source_round=entry.source_round,
    )


def _choose_best_entry(
    expected_archetype: str,
    candidates: tuple[Round16ThemeCoverageEntry, ...],
) -> Round16ThemeCoverageEntry:
    for candidate in candidates:
        if candidate.primary_sub_archetype == expected_archetype:
            return candidate
    for candidate in candidates:
        if candidate.canonical_archetype.value == expected_archetype:
            return candidate
    return candidates[0]


def _index_entries_by_theme(
    entries: Iterable[Round16ThemeCoverageEntry],
) -> dict[str, tuple[Round16ThemeCoverageEntry, ...]]:
    grouped: dict[str, list[Round16ThemeCoverageEntry]] = {}
    for entry in entries:
        grouped.setdefault(_normalize_theme_tag(entry.theme_tag), []).append(entry)
    return {key: tuple(value) for key, value in grouped.items()}


def _index_entries_by_sub_archetype(
    entries: Iterable[Round16ThemeCoverageEntry],
) -> dict[str, tuple[Round16ThemeCoverageEntry, ...]]:
    grouped: dict[str, list[Round16ThemeCoverageEntry]] = {}
    for entry in entries:
        grouped.setdefault(entry.primary_sub_archetype, []).append(entry)
    return {key: tuple(value) for key, value in grouped.items()}


def _index_entries_by_canonical(
    entries: Iterable[Round16ThemeCoverageEntry],
) -> dict[str, tuple[Round16ThemeCoverageEntry, ...]]:
    grouped: dict[str, list[Round16ThemeCoverageEntry]] = {}
    for entry in entries:
        grouped.setdefault(entry.canonical_archetype.value, []).append(entry)
    return {key: tuple(value) for key, value in grouped.items()}


def _normalize_theme_tag(value: str) -> str:
    return (
        value.casefold()
        .replace(" ", "")
        .replace("-", "")
        .replace("·", "")
        .replace("/", "")
        .replace("_", "")
    )


def _is_reasonable_alias(raw_tag: str, matched_tag: str) -> bool:
    raw = _normalize_theme_tag(raw_tag)
    matched = _normalize_theme_tag(matched_tag)
    if raw == matched:
        return True
    if raw in matched or matched in raw:
        return True
    separators = ("·", "/", "-", " ")
    parts = [raw_tag]
    for separator in separators:
        next_parts: list[str] = []
        for part in parts:
            next_parts.extend(part.split(separator))
        parts = next_parts
    return any(_normalize_theme_tag(part) == matched for part in parts if part)


def _is_separator_row(parts: tuple[str, ...] | list[str]) -> bool:
    return all(part and set(part) <= {"-", ":"} for part in parts)


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    row_tuple = tuple(rows)
    if not row_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(row_tuple[0].keys()))
        writer.writeheader()
        for row in row_tuple:
            writer.writerow(row)
    return path


__all__ = [
    "ROUND17_DEFAULT_ALIAS_PATH",
    "ROUND17_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND17_DEFAULT_THEME_MAP_PATH",
    "ROUND17_SOURCE_ROUND_PATH",
    "Round17ThemeAuditRecord",
    "Round17ThemeExpectation",
    "parse_round17_theme_expectations",
    "render_round17_alias_yaml",
    "render_round17_theme_coverage_report",
    "round17_coverage_summary",
    "round17_green_policy_distribution",
    "round17_theme_audit_records",
    "round17_theme_map_rows",
    "round17_unmatched_theme_rows",
    "write_round17_theme_absorption_reports",
]
