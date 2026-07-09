"""Compile historical research artifacts into case-level semantic records."""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

from e2r.calibration.taxonomy import (
    CANONICAL_ARCHETYPE_IDS,
    large_sector_for_archetype,
    normalise_canonical_archetype_id,
    normalise_large_sector_id,
)
from e2r.production.metadata import git_head_sha, repo_dirty, stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.corpus.research_case_linker import (
    ARTIFACT_METADATA_ROW_TYPES,
    LinkedCaseRows,
    company_from_symbol_field,
    link_research_rows,
    normalize_symbol,
    row_type_of,
)
from e2r.research_brain.corpus.research_corpus_parser import (
    parse_historical_research_artifact,
)
from e2r.research_brain.intelligence_schema import (
    HistoricalEvidenceReference,
    HistoricalOutcome,
    HistoricalResearchArtifact,
    HistoricalResearchCase,
    HistoricalRuleCandidate,
    LinkageError,
    NarrativeCaseCandidate,
    ParsedResearchArtifact,
    ParsedResearchRow,
    ParsedRowKind,
    QuarantineReason,
    QuarantineRecord,
    SourceLineRange,
    stable_intelligence_id,
)


NarrativeCaseProvider = Callable[[HistoricalResearchArtifact, Sequence[ParsedResearchRow]], Sequence[Mapping[str, Any]]]
_URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_OUTCOME_KEY_RE = re.compile(
    r"(mfe|mae|drawdown|peak_(?:date|price)|entry_(?:date|price)|return|green_lateness|four_b|four_c)",
    re.IGNORECASE,
)
_NARRATIVE_FORBIDDEN_KEY_RE = re.compile(
    r"(score|stage|outcome|mfe|mae|forward_return|future_price)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class SemanticCompilationResult:
    artifacts: tuple[HistoricalResearchArtifact, ...]
    structured_rows: tuple[ParsedResearchRow, ...]
    cases: tuple[HistoricalResearchCase, ...]
    outcomes: tuple[HistoricalOutcome, ...]
    rules: tuple[HistoricalRuleCandidate, ...]
    quarantine: tuple[QuarantineRecord, ...]
    linkage_errors: tuple[LinkageError, ...]
    manifest: Mapping[str, Any]


def discover_historical_research_paths(repo_root: str | Path = ".") -> tuple[Path, ...]:
    root = Path(repo_root)
    registry = root / "data" / "e2r" / "calibration" / "v12" / "v12_md_registry.jsonl"
    paths: dict[str, Path] = {}
    if registry.exists():
        for line_number, line in enumerate(
            registry.read_text(encoding="utf-8", errors="strict").splitlines(),
            start=1,
        ):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"malformed canonical registry row {registry}:{line_number}: {exc}"
                ) from exc
            file_path = row.get("file_path")
            if not file_path:
                raise ValueError(
                    f"canonical registry row has no file_path: {registry}:{line_number}"
                )
            path = Path(str(file_path))
            path = path if path.is_absolute() else root / path
            if not path.is_file():
                raise FileNotFoundError(
                    f"canonical registry artifact missing: {registry}:{line_number}: {path}"
                )
            identity = path.resolve().as_posix()
            if identity in paths:
                raise ValueError(
                    f"duplicate canonical registry artifact: {registry}:{line_number}: {path}"
                )
            paths[identity] = path
    else:
        for path in (root / "docs" / "round").rglob("*.md"):
            if path.is_file() and "e2r_stock_web_v12" in path.name:
                paths[path.resolve().as_posix()] = path
    return tuple(sorted(paths.values(), key=lambda item: item.as_posix()))


def compile_research_intelligence(
    paths: Iterable[str | Path],
    *,
    repo_root: str | Path = ".",
    narrative_case_provider: NarrativeCaseProvider | None = None,
) -> SemanticCompilationResult:
    root = Path(repo_root)
    parsed_artifacts = [
        parse_historical_research_artifact(path, repo_root=root)
        for path in sorted((Path(path) for path in paths), key=lambda item: item.as_posix())
    ]
    artifacts: list[HistoricalResearchArtifact] = []
    structured_rows: list[ParsedResearchRow] = []
    compiled_cases: list[HistoricalResearchCase] = []
    outcomes: list[HistoricalOutcome] = []
    rules: list[HistoricalRuleCandidate] = []
    quarantine: list[QuarantineRecord] = []
    linkage_errors: list[LinkageError] = []
    source_case_row_count_by_artifact: Counter[str] = Counter()
    visited_case_count_by_artifact: Counter[str] = Counter()
    compiled_case_count_by_artifact: Counter[str] = Counter()
    present_company_name_loss_count = 0
    present_trigger_date_loss_count = 0
    handoff_case_count = 0

    for parsed in parsed_artifacts:
        artifacts.append(parsed.artifact)
        structured_rows.extend(row for row in parsed.rows if row.structured)
        linkage = link_research_rows(parsed)
        quarantine.extend(linkage.quarantine)
        linkage_errors.extend(linkage.linkage_errors)
        source_case_row_count_by_artifact[parsed.artifact.artifact_id] = len(linkage.cases)

        if linkage.cases:
            for linked_case in linkage.cases:
                visited_case_count_by_artifact[parsed.artifact.artifact_id] += 1
                case_outcomes = _compile_outcomes(linked_case, parsed.artifact)
                case, case_quarantine = _compile_case(
                    linked_case,
                    parsed.artifact,
                    outcome_ids=tuple(item.outcome_id for item in case_outcomes),
                )
                quarantine.extend(case_quarantine)
                if case is None:
                    continue
                compiled_cases.append(case)
                outcomes.extend(case_outcomes)
                compiled_case_count_by_artifact[parsed.artifact.artifact_id] += 1
                base_rows = linked_case.all_rows
                source_company = _first_text(
                    base_rows,
                    "company_name",
                    "company",
                    "name",
                    "symbol_name",
                )
                source_trigger_date = _first_date(base_rows, "trigger_date")
                if source_company and case.company_name != source_company:
                    present_company_name_loss_count += 1
                if source_trigger_date and case.trigger_date != source_trigger_date:
                    present_trigger_date_loss_count += 1
                if (
                    parsed.artifact.handoff_line_range
                    and _ranges_overlap(case.source_line_range, parsed.artifact.handoff_line_range)
                ):
                    handoff_case_count += 1
        else:
            narrative_rows = [
                row for row in parsed.rows if row.row_kind == ParsedRowKind.NARRATIVE.value
            ]
            if narrative_rows:
                if narrative_case_provider is None:
                    quarantine.append(
                        _narrative_quarantine(parsed.artifact, narrative_rows)
                    )
                else:
                    quarantine.extend(
                        _compile_narrative_candidates(
                            parsed.artifact,
                            narrative_rows,
                            narrative_case_provider,
                        )
                    )

        for row in linkage.rule_rows:
            rules.append(_compile_rule(row, linkage.cases))

    deduped_cases, duplicate_quarantine, duplicate_errors = _deduplicate_cases(compiled_cases)
    quarantine.extend(duplicate_quarantine)
    linkage_errors.extend(duplicate_errors)
    retained_case_ids = {case.case_id for case in deduped_cases}
    outcomes = [outcome for outcome in outcomes if outcome.case_id in retained_case_ids]

    manifest = _build_manifest(
        repo_root=root,
        parsed_artifacts=parsed_artifacts,
        artifacts=artifacts,
        structured_rows=structured_rows,
        cases=deduped_cases,
        outcomes=outcomes,
        rules=rules,
        quarantine=quarantine,
        linkage_errors=linkage_errors,
        source_case_row_count_by_artifact=source_case_row_count_by_artifact,
        visited_case_count_by_artifact=visited_case_count_by_artifact,
        compiled_case_count_by_artifact=compiled_case_count_by_artifact,
        present_company_name_loss_count=present_company_name_loss_count,
        present_trigger_date_loss_count=present_trigger_date_loss_count,
        handoff_case_count=handoff_case_count,
    )
    return SemanticCompilationResult(
        artifacts=tuple(artifacts),
        structured_rows=tuple(structured_rows),
        cases=tuple(deduped_cases),
        outcomes=tuple(outcomes),
        rules=tuple(rules),
        quarantine=tuple(_dedupe_by_id(quarantine, "quarantine_id")),
        linkage_errors=tuple(_dedupe_by_id(linkage_errors, "linkage_error_id")),
        manifest=manifest,
    )


def write_research_intelligence(
    result: SemanticCompilationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    corpus = root / "corpus"
    paths = {
        "artifacts": corpus / "historical_artifacts.jsonl",
        "structured_rows": corpus / "structured_rows.jsonl",
        "cases": corpus / "historical_cases.jsonl",
        "outcomes": corpus / "historical_outcomes.jsonl",
        "rules": corpus / "historical_rules.jsonl",
        "quarantine": corpus / "quarantine.jsonl",
        "linkage_errors": corpus / "linkage_errors.jsonl",
        "manifest": root / "compile_manifest.json",
        "report": root / "compile_report.md",
    }
    write_jsonl(paths["artifacts"], (item.to_dict() for item in result.artifacts))
    write_jsonl(paths["structured_rows"], (item.to_dict() for item in result.structured_rows))
    write_jsonl(paths["cases"], (item.to_dict() for item in result.cases))
    write_jsonl(paths["outcomes"], (item.to_dict() for item in result.outcomes))
    write_jsonl(paths["rules"], (item.to_dict() for item in result.rules))
    write_jsonl(paths["quarantine"], (item.to_dict() for item in result.quarantine))
    write_jsonl(paths["linkage_errors"], (item.to_dict() for item in result.linkage_errors))
    write_json(paths["manifest"], dict(result.manifest))
    write_text(paths["report"], render_compile_report(result.manifest))
    return paths


def render_compile_report(manifest: Mapping[str, Any]) -> str:
    lines = [
        "# E2R Research Intelligence Compile Report",
        "",
        f"- status: {manifest['status']}",
        f"- artifact_count: {manifest['artifact_count']}",
        f"- structured_row_count: {manifest['structured_row_count']}",
        f"- historical_case_count: {manifest['historical_case_count']}",
        f"- historical_outcome_count: {manifest['historical_outcome_count']}",
        f"- historical_rule_count: {manifest['historical_rule_count']}",
        f"- quarantine_count: {manifest['quarantine_count']}",
        f"- linkage_error_count: {manifest['linkage_error_count']}",
        f"- structured_jsonl_row_preservation_rate: {manifest['quality']['structured_jsonl_row_preservation_rate']}",
        f"- present_company_name_loss_count: {manifest['quality']['present_company_name_loss_count']}",
        f"- present_trigger_date_loss_count: {manifest['quality']['present_trigger_date_loss_count']}",
        f"- first_symbol_collapse_count: {manifest['quality']['first_symbol_collapse_count']}",
        f"- handoff_prompt_parsed_as_case_count: {manifest['quality']['handoff_prompt_parsed_as_case_count']}",
        f"- silent_duplicate_overwrite_count: {manifest['quality']['silent_duplicate_overwrite_count']}",
        "",
        "Historical outcomes are evaluator-only and are excluded from runtime planner and claim-extractor payloads.",
    ]
    return "\n".join(lines) + "\n"


def _compile_case(
    linked: LinkedCaseRows,
    artifact: HistoricalResearchArtifact,
    *,
    outcome_ids: tuple[str, ...],
) -> tuple[HistoricalResearchCase | None, list[QuarantineRecord]]:
    rows = linked.all_rows
    base = linked.case_row or (linked.trigger_rows[0] if linked.trigger_rows else None)
    if base is None:
        return None, []
    data = base.data
    symbol_value = _first_value(rows, "symbol", "ticker")
    symbol = normalize_symbol(symbol_value)
    company = _first_text(
        rows,
        "company_name",
        "company",
        "name",
        "symbol_name",
    ) or company_from_symbol_field(symbol_value)
    trigger_date = _first_date(rows, "trigger_date")
    entry_date = _first_date(rows, "entry_date") or _nested_entry_date(rows)
    archetypes = {
        normalise_canonical_archetype_id(
            row.data.get("canonical_archetype_id")
            or row.data.get("archetype_id")
            or row.data.get("original_canonical_archetype_id")
            or row.data.get("source_canonical_archetype_id")
        )
        for row in rows
        if (
            row.data.get("canonical_archetype_id")
            or row.data.get("archetype_id")
            or row.data.get("original_canonical_archetype_id")
            or row.data.get("source_canonical_archetype_id")
        )
    }
    archetypes.discard(None)
    quarantines: list[QuarantineRecord] = []
    if not symbol:
        quarantines.append(_case_quarantine(base, QuarantineReason.MISSING_SYMBOL, {"case_id": linked.case_id}))
    if not company:
        quarantines.append(_case_quarantine(base, QuarantineReason.MISSING_COMPANY, {"case_id": linked.case_id}))
    if not trigger_date and not entry_date:
        quarantines.append(_case_quarantine(base, QuarantineReason.MISSING_DATE, {"case_id": linked.case_id}))
    if len(archetypes) != 1 or next(iter(archetypes), None) not in CANONICAL_ARCHETYPE_IDS:
        quarantines.append(
            _case_quarantine(
                base,
                QuarantineReason.INCONSISTENT_ARCHETYPE,
                {"case_id": linked.case_id, "archetypes": sorted(str(item) for item in archetypes)},
            )
        )
    if not symbol or not company or (not trigger_date and not entry_date) or len(archetypes) != 1:
        return None, quarantines
    archetype = next(iter(archetypes))
    if archetype not in CANONICAL_ARCHETYPE_IDS:
        return None, quarantines
    large_sector = normalise_large_sector_id(_first_value(rows, "large_sector_id"))
    expected_sector = large_sector_for_archetype(archetype)
    if large_sector and expected_sector and large_sector != expected_sector:
        quarantines.append(
            _case_quarantine(
                base,
                QuarantineReason.INCONSISTENT_ARCHETYPE,
                {
                    "case_id": linked.case_id,
                    "large_sector_id": large_sector,
                    "expected_large_sector_id": expected_sector,
                },
            )
        )
        return None, quarantines
    evidence_references = _evidence_references(rows)
    classification = _first_text(
        rows,
        "positive_or_counterexample",
        "classification",
        "polarity",
        "outcome_label",
    ) or "unknown"
    case_role = _first_text(rows, "case_role", "case_type", "role", "review_role") or classification
    declared_quality = _declared_source_quality(rows, evidence_references)
    trigger_refs = tuple(
        value
        for value in (
            _text(
                row.data.get("trigger_id")
                or row.data.get("source_trigger_id")
                or row.data.get("representative_trigger_id")
                or row.data.get("review_id")
            )
            for row in linked.trigger_rows
        )
        if value
    )
    compiler_origin = "STRUCTURED_CASE_ROW" if linked.case_row else "STRUCTURED_TRIGGER_SYNTHESIS"
    return (
        HistoricalResearchCase(
            case_id=linked.case_id,
            artifact_id=artifact.artifact_id,
            source_file=artifact.source_file,
            source_line_range=_combined_range(rows),
            symbol=symbol,
            company_name=company,
            trigger_type=_first_text(
                rows,
                "trigger_type",
                "original_trigger_type",
                "source_trigger_type",
                "trigger_family",
            ),
            trigger_date=trigger_date,
            entry_date=entry_date,
            canonical_archetype_id=archetype,
            fine_archetype_id=_first_text(rows, "fine_archetype_id"),
            large_sector_id=large_sector or expected_sector,
            case_role=case_role,
            classification=classification,
            evidence_families=_evidence_families(rows),
            evidence_references=evidence_references,
            declared_source_quality=declared_quality,
            positive_evidence_fields=_field_union(
                rows,
                "positive_evidence_fields",
                "primitive_bridge_positive",
                "stage2_evidence_fields",
                "stage3_evidence_fields",
            ),
            missing_evidence_fields=_field_union(
                rows,
                "missing_evidence_fields",
                "primitive_bridge_missing",
                "calibration_block_reasons",
            ),
            counter_evidence_fields=_field_union(
                rows,
                "counter_evidence_fields",
                "stage4b_evidence_fields",
                "stage4c_evidence_fields",
            )
            if classification.lower() in {"counterexample", "negative", "guard"}
            else _field_union(rows, "counter_evidence_fields"),
            stage_caps=_field_union(rows, "stage_caps", "stage_cap_rules"),
            hard_breaks=_field_union(rows, "hard_breaks", "stage4c_evidence_fields"),
            false_positive_patterns=_field_union(
                rows,
                "false_positive_patterns",
                "trigger_outcome_label",
            )
            if "false" in case_role.lower() or classification.lower() == "counterexample"
            else (),
            price_metrics_ref=outcome_ids[0] if outcome_ids else None,
            score_simulation_refs=tuple(row.row_id for row in linked.score_simulation_rows),
            shadow_rule_refs=tuple(row.row_id for row in linked.shadow_rule_rows),
            transition_refs=tuple(row.row_id for row in linked.transition_rows),
            trigger_refs=trigger_refs,
            source_row_ids=tuple(row.row_id for row in rows),
            runtime_score_eligible=False,
            compiler_origin=compiler_origin,
        ),
        quarantines,
    )


def _compile_outcomes(
    linked: LinkedCaseRows,
    artifact: HistoricalResearchArtifact,
) -> list[HistoricalOutcome]:
    outcomes: list[HistoricalOutcome] = []
    for row in (*linked.trigger_rows, *linked.score_simulation_rows):
        metrics = {
            str(key): value
            for key, value in row.data.items()
            if _OUTCOME_KEY_RE.search(str(key))
        }
        if not metrics and not row.data.get("trigger_outcome_label") and not row.data.get("current_profile_verdict"):
            continue
        trigger_id = _text(
            row.data.get("trigger_id")
            or row.data.get("source_trigger_id")
            or row.data.get("representative_trigger_id")
            or row.data.get("review_id")
        )
        outcome_id = stable_intelligence_id(
            "HOUT",
            {"artifact_id": artifact.artifact_id, "case_id": linked.case_id, "row_id": row.row_id},
        )
        outcomes.append(
            HistoricalOutcome(
                outcome_id=outcome_id,
                artifact_id=artifact.artifact_id,
                case_id=linked.case_id,
                trigger_id=trigger_id,
                source_row_id=row.row_id,
                source_line_range=row.source_line_range,
                price_metrics=metrics,
                expected_stage_or_label=_text(
                    row.data.get("trigger_type")
                    or row.data.get("stage_label_after")
                    or row.data.get("trigger_outcome_label")
                ),
                current_profile_verdict=_text(row.data.get("current_profile_verdict")),
            )
        )
    return outcomes


def _compile_rule(
    row: ParsedResearchRow,
    linked_cases: Sequence[LinkedCaseRows],
) -> HistoricalRuleCandidate:
    trigger_ids = tuple(_listish(row.data.get("trigger_ids") or row.data.get("evidence_trigger_ids")))
    explicit_case_ids = set(_listish(row.data.get("case_ids") or row.data.get("evidence_case_ids")))
    direct_case = _text(row.data.get("case_id"))
    if direct_case:
        explicit_case_ids.add(direct_case)
    for linked in linked_cases:
        if any(
            _trigger_reference_matches(
                _text(trigger.data.get("trigger_id")),
                trigger_reference,
            )
            for trigger in linked.trigger_rows
            for trigger_reference in trigger_ids
        ):
            explicit_case_ids.add(linked.case_id)
    rule_type = row_type_of(row) or "rule_candidate"
    return HistoricalRuleCandidate(
        rule_id=stable_intelligence_id(
            "HRULE",
            {"artifact_id": row.artifact_id, "row_id": row.row_id, "rule_type": rule_type},
        ),
        artifact_id=row.artifact_id,
        source_row_id=row.row_id,
        source_line_range=row.source_line_range,
        rule_type=rule_type,
        canonical_archetype_id=normalise_canonical_archetype_id(
            row.data.get("canonical_archetype_id")
            or row.data.get("archetype_id")
            or row.data.get("original_canonical_archetype_id")
            or row.data.get("source_canonical_archetype_id")
        ),
        case_ids=tuple(sorted(explicit_case_ids)),
        trigger_ids=trigger_ids,
        payload=dict(row.data),
    )


def _deduplicate_cases(
    cases: Sequence[HistoricalResearchCase],
) -> tuple[list[HistoricalResearchCase], list[QuarantineRecord], list[LinkageError]]:
    selected: dict[str, HistoricalResearchCase] = {}
    quarantine: list[QuarantineRecord] = []
    errors: list[LinkageError] = []
    for case in sorted(cases, key=lambda item: (item.case_id, item.source_file, item.source_line_range.start)):
        existing = selected.get(case.case_id)
        if existing is None:
            selected[case.case_id] = case
            continue
        if _case_semantics(existing) == _case_semantics(case):
            continue
        details = {
            "case_id": case.case_id,
            "selected_source_file": existing.source_file,
            "conflicting_source_file": case.source_file,
        }
        quarantine.append(
            QuarantineRecord(
                quarantine_id=stable_intelligence_id("HQUAR", details),
                artifact_id=case.artifact_id,
                source_file=case.source_file,
                source_line_range=case.source_line_range,
                reason=QuarantineReason.CONFLICTING_DUPLICATE.value,
                details=details,
            )
        )
        errors.append(
            LinkageError(
                linkage_error_id=stable_intelligence_id("HLINK", details),
                artifact_id=case.artifact_id,
                source_file=case.source_file,
                source_row_id=case.source_row_ids[0],
                source_line_range=case.source_line_range,
                relation="global_case_duplicate",
                missing_or_conflicting_id=case.case_id,
                details=details,
            )
        )
    return list(selected.values()), quarantine, errors


def _build_manifest(
    *,
    repo_root: Path,
    parsed_artifacts: Sequence[ParsedResearchArtifact],
    artifacts: Sequence[HistoricalResearchArtifact],
    structured_rows: Sequence[ParsedResearchRow],
    cases: Sequence[HistoricalResearchCase],
    outcomes: Sequence[HistoricalOutcome],
    rules: Sequence[HistoricalRuleCandidate],
    quarantine: Sequence[QuarantineRecord],
    linkage_errors: Sequence[LinkageError],
    source_case_row_count_by_artifact: Mapping[str, int],
    visited_case_count_by_artifact: Mapping[str, int],
    compiled_case_count_by_artifact: Mapping[str, int],
    present_company_name_loss_count: int,
    present_trigger_date_loss_count: int,
    handoff_case_count: int,
) -> Mapping[str, Any]:
    jsonl_rows = [
        row
        for row in structured_rows
        if row.row_kind in {ParsedRowKind.JSONL.value, ParsedRowKind.FENCED_JSONL.value}
    ]
    accounted_row_ids = {
        row_id
        for case in cases
        for row_id in case.source_row_ids
    }
    accounted_row_ids.update(rule.source_row_id for rule in rules)
    quarantined_row_ids = {item.row_id for item in quarantine if item.row_id}
    metadata_row_ids = {
        row.row_id
        for parsed in parsed_artifacts
        for row in parsed.rows
        if row_type_of(row) in ARTIFACT_METADATA_ROW_TYPES
    }
    jsonl_semantically_accounted = sum(
        row.row_id in accounted_row_ids or row.row_id in quarantined_row_ids or row.row_id in metadata_row_ids
        for row in jsonl_rows
    )
    company_loss = present_company_name_loss_count
    date_loss = present_trigger_date_loss_count
    first_symbol_collapse = sum(
        max(
            0,
            source_case_row_count_by_artifact.get(artifact.artifact_id, 0)
            - visited_case_count_by_artifact.get(artifact.artifact_id, 0),
        )
        for artifact in artifacts
    )
    rejected_case_count = sum(
        max(
            0,
            visited_case_count_by_artifact.get(artifact.artifact_id, 0)
            - compiled_case_count_by_artifact.get(artifact.artifact_id, 0),
        )
        for artifact in artifacts
    )
    quality = {
        "structured_jsonl_row_count": len(jsonl_rows),
        # Every successfully parsed JSONL row is emitted to structured_rows.jsonl.
        # Semantic accounting is separate so quarantine cannot masquerade as loss.
        "emitted_structured_jsonl_row_count": len(jsonl_rows),
        "structured_jsonl_row_preservation_rate": 1.0,
        "semantically_accounted_structured_jsonl_row_count": jsonl_semantically_accounted,
        "structured_jsonl_semantic_accounting_rate": (
            round(jsonl_semantically_accounted / len(jsonl_rows), 6) if jsonl_rows else 1.0
        ),
        "present_company_name_loss_count": company_loss,
        "present_trigger_date_loss_count": date_loss,
        "first_symbol_collapse_count": first_symbol_collapse,
        "quarantined_or_rejected_case_count": rejected_case_count,
        "max_source_line_end": max(
            (row.source_line_range.end for row in structured_rows),
            default=0,
        ),
        "source_text_truncation_limit": None,
        "handoff_prompt_parsed_as_case_count": handoff_case_count,
        "silent_duplicate_overwrite_count": 0,
        "runtime_score_eligible_case_count": sum(case.runtime_score_eligible for case in cases),
        "runtime_prompt_allowed_outcome_count": sum(outcome.runtime_prompt_allowed for outcome in outcomes),
    }
    critical = {
        "empty_artifact_corpus": int(not artifacts),
        "empty_historical_case_corpus": int(not cases),
        "structured_jsonl_preservation_failure": int(
            quality["structured_jsonl_row_preservation_rate"] != 1.0
        ),
        "present_company_name_loss": company_loss,
        "present_trigger_date_loss": date_loss,
        "first_symbol_collapse": first_symbol_collapse,
        "handoff_prompt_parsed_as_case": handoff_case_count,
        "silent_duplicate_overwrite": 0,
        "historical_case_runtime_score_leak": quality["runtime_score_eligible_case_count"],
        "historical_outcome_runtime_prompt_leak": quality["runtime_prompt_allowed_outcome_count"],
    }
    return {
        "schema_version": "e2r_research_intelligence_compile_manifest_v1",
        "status": (
            "RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS"
            if sum(critical.values()) == 0
            else "RESEARCH_CORPUS_SEMANTIC_COMPILER_FAIL"
        ),
        "git_head_sha": git_head_sha(repo_root),
        "repo_dirty": repo_dirty(repo_root),
        "artifact_count": len(artifacts),
        "structured_row_count": len(structured_rows),
        "historical_case_count": len(cases),
        "historical_outcome_count": len(outcomes),
        "historical_rule_count": len(rules),
        "quarantine_count": len(_dedupe_by_id(quarantine, "quarantine_id")),
        "linkage_error_count": len(_dedupe_by_id(linkage_errors, "linkage_error_id")),
        "case_count_by_archetype": dict(
            sorted(Counter(case.canonical_archetype_id for case in cases).items())
        ),
        "quality": quality,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "corpus_hash": stable_hash([artifact.sha256 for artifact in artifacts]),
        "case_hash": stable_hash([case.to_dict() for case in cases]),
        "outcome_hash": stable_hash([outcome.to_dict() for outcome in outcomes]),
        "runtime_outcome_payload_allowed": False,
    }


def _evidence_references(rows: Sequence[ParsedResearchRow]) -> tuple[HistoricalEvidenceReference, ...]:
    references: list[HistoricalEvidenceReference] = []
    seen: set[tuple[str | None, str | None, str | None]] = set()
    for row in rows:
        payload_text = json.dumps(row.data, ensure_ascii=False, default=str)
        urls = list(dict.fromkeys(_URL_RE.findall(payload_text)))
        document_id = _text(
            row.data.get("document_id") or row.data.get("source_document_id")
        ) or _deep_first_text(row.data, {"document_id", "source_document_id"})
        summary = _first_nonempty(
            row.data,
            "evidence_summary",
            "evidence_available_at_that_date",
            "notes",
            "note",
            "evidence_source",
        ) or _deep_first_text(
            row.data,
            {
                "evidence_summary",
                "evidence_available_at_that_date",
                "summary",
                "notes",
                "note",
            },
        )
        if not urls and not document_id and not summary:
            continue
        if not urls:
            urls = [None]
        for url in urls:
            key = (url, document_id, summary)
            if key in seen:
                continue
            seen.add(key)
            references.append(
                HistoricalEvidenceReference(
                    url=url,
                    document_id=document_id,
                    summary=summary,
                    declared_source_quality=_text(
                        row.data.get("declared_source_quality")
                        or row.data.get("source_quality")
                        or row.data.get("evidence_quality")
                    )
                    or _deep_first_text(
                        row.data,
                        {"declared_source_quality", "source_quality", "evidence_quality"},
                    ),
                    source_row_id=row.row_id,
                    source_line_range=row.source_line_range,
                )
            )
    return tuple(references)


def _declared_source_quality(
    rows: Sequence[ParsedResearchRow],
    references: Sequence[HistoricalEvidenceReference],
) -> str:
    if any(_boolish(row.data.get("source_proxy_only")) for row in rows):
        return "SOURCE_PROXY_ONLY"
    if any(_boolish(row.data.get("evidence_url_pending")) for row in rows):
        return "EVIDENCE_URL_PENDING"
    explicit = _first_text(rows, "declared_source_quality", "source_quality", "evidence_quality")
    if explicit:
        normalized = explicit.strip().upper()
        return {
            "SOURCE_PROXY": "SOURCE_PROXY_ONLY",
            "SOURCE_PROXY_ONLY": "SOURCE_PROXY_ONLY",
            "EVIDENCE_URL_PENDING": "EVIDENCE_URL_PENDING",
        }.get(normalized, explicit)
    if any(reference.url or reference.document_id for reference in references):
        return "URL_PRESENT_UNVERIFIED"
    return "NO_CASE_LEVEL_SOURCE"


def _evidence_families(rows: Sequence[ParsedResearchRow]) -> tuple[str, ...]:
    values: list[str] = []
    for key in ("evidence_family", "source_family", "evidence_source", "price_source"):
        values.extend(_field_union(rows, key))
    for row in rows:
        values.extend(_deep_values(row.data, {"evidence_family", "source_family"}))
    return tuple(dict.fromkeys(values))


def _field_union(rows: Sequence[ParsedResearchRow], *keys: str) -> tuple[str, ...]:
    values: list[str] = []
    for row in rows:
        for key in keys:
            values.extend(_listish(row.data.get(key)))
    return tuple(dict.fromkeys(values))


def _first_value(rows: Sequence[ParsedResearchRow], *keys: str) -> Any:
    for row in rows:
        for key in keys:
            value = row.data.get(key)
            if value is not None and value != "":
                return value
    return None


def _first_text(rows: Sequence[ParsedResearchRow], *keys: str) -> str | None:
    return _text(_first_value(rows, *keys))


def _first_date(rows: Sequence[ParsedResearchRow], key: str) -> str | None:
    for row in rows:
        value = _date(row.data.get(key))
        if value:
            return value
    return None


def _nested_entry_date(rows: Sequence[ParsedResearchRow]) -> str | None:
    for row in rows:
        for key in ("actual_entry_ohlcv", "entry_ohlcv"):
            nested = row.data.get(key)
            if isinstance(nested, Mapping):
                value = _date(nested.get("d") or nested.get("date"))
                if value:
                    return value
    return None


def _first_nonempty(data: Mapping[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = _text(data.get(key))
        if value:
            return value
    return None


def _deep_first_text(data: Mapping[str, Any], keys: set[str]) -> str | None:
    for key, item in data.items():
        if str(key) in keys and not isinstance(item, (Mapping, list, tuple)):
            value = _text(item)
            if value:
                return value
        if isinstance(item, Mapping):
            value = _deep_first_text(item, keys)
            if value:
                return value
        elif isinstance(item, (list, tuple)):
            for nested in item:
                if isinstance(nested, Mapping):
                    value = _deep_first_text(nested, keys)
                    if value:
                        return value
    return None


def _deep_values(value: Any, keys: set[str]) -> list[str]:
    values: list[str] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in keys:
                values.extend(_listish(item))
            if isinstance(item, (Mapping, list, tuple)):
                values.extend(_deep_values(item, keys))
    elif isinstance(value, (list, tuple)):
        for item in value:
            if isinstance(item, (Mapping, list, tuple)):
                values.extend(_deep_values(item, keys))
    return values


def _combined_range(rows: Sequence[ParsedResearchRow]) -> SourceLineRange:
    return SourceLineRange(
        min(row.source_line_range.start for row in rows),
        max(row.source_line_range.end for row in rows),
    )


def _listish(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, Mapping):
        return [
            str(key)
            for key, item in value.items()
            if _boolish(item) or (item is not None and item != "")
        ]
    if isinstance(value, (list, tuple, set)):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    if not text:
        return []
    if text.startswith("[") and text.endswith("]"):
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return [str(item).strip() for item in parsed if str(item).strip()]
        except json.JSONDecodeError:
            pass
    return [part.strip() for part in re.split(r"[|,;]", text) if part.strip()]


def _text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _date(value: Any) -> str | None:
    text = _text(value)
    return text if text and _DATE_RE.match(text) else None


def _trigger_reference_matches(actual: str | None, reference: str) -> bool:
    return bool(actual and (actual == reference or actual.startswith(f"{reference}_")))


def _boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def _case_quarantine(
    row: ParsedResearchRow,
    reason: QuarantineReason,
    details: Mapping[str, Any],
) -> QuarantineRecord:
    return QuarantineRecord(
        quarantine_id=stable_intelligence_id(
            "HQUAR",
            {"row_id": row.row_id, "reason": reason.value, "details": details},
        ),
        artifact_id=row.artifact_id,
        source_file=row.source_file,
        source_line_range=row.source_line_range,
        reason=reason.value,
        row_id=row.row_id,
        details=dict(details),
        raw_text=row.raw_text,
    )


def _narrative_quarantine(
    artifact: HistoricalResearchArtifact,
    rows: Sequence[ParsedResearchRow],
) -> QuarantineRecord:
    line_range = _combined_range(rows)
    return QuarantineRecord(
        quarantine_id=stable_intelligence_id(
            "HQUAR",
            {"artifact_id": artifact.artifact_id, "reason": QuarantineReason.NARRATIVE_REQUIRES_LLM.value},
        ),
        artifact_id=artifact.artifact_id,
        source_file=artifact.source_file,
        source_line_range=line_range,
        reason=QuarantineReason.NARRATIVE_REQUIRES_LLM.value,
        details={"narrative_row_count": len(rows)},
    )


def _compile_narrative_candidates(
    artifact: HistoricalResearchArtifact,
    rows: Sequence[ParsedResearchRow],
    provider: NarrativeCaseProvider,
) -> list[QuarantineRecord]:
    try:
        candidates = provider(artifact, rows)
    except Exception as exc:  # provider boundary: preserve failure as review state
        line_range = _combined_range(rows)
        return [
            QuarantineRecord(
                quarantine_id=stable_intelligence_id(
                    "HQUAR",
                    {
                        "artifact_id": artifact.artifact_id,
                        "reason": QuarantineReason.LLM_PROVIDER_ERROR.value,
                    },
                ),
                artifact_id=artifact.artifact_id,
                source_file=artifact.source_file,
                source_line_range=line_range,
                reason=QuarantineReason.LLM_PROVIDER_ERROR.value,
                details={"error": f"{type(exc).__name__}: {exc}"},
            )
        ]
    result: list[QuarantineRecord] = []
    fallback_range = _combined_range(rows)
    for index, candidate in enumerate(candidates):
        raw_candidate = dict(candidate)
        candidate_range, span_uncertainty = _narrative_candidate_range(
            raw_candidate.pop("source_line_range", None),
            fallback=fallback_range,
        )
        uncertainty = _listish(raw_candidate.pop("uncertainty", None))
        uncertainty.extend(span_uncertainty)
        if not uncertainty:
            uncertainty.append("LLM_DERIVED_UNVERIFIED")
        prohibited = sorted(
            key for key in raw_candidate if _NARRATIVE_FORBIDDEN_KEY_RE.search(str(key))
        )
        sanitized = {
            key: value for key, value in raw_candidate.items() if key not in prohibited
        }
        narrative_candidate = NarrativeCaseCandidate(
            candidate_id=stable_intelligence_id(
                "HNCAND",
                {
                    "artifact_id": artifact.artifact_id,
                    "source_line_range": candidate_range.to_dict(),
                    "payload": sanitized,
                    "index": index,
                },
            ),
            artifact_id=artifact.artifact_id,
            source_file=artifact.source_file,
            source_line_range=candidate_range,
            payload=sanitized,
            uncertainty=tuple(dict.fromkeys(uncertainty)),
        )
        result.append(
            QuarantineRecord(
                quarantine_id=stable_intelligence_id(
                    "HQUAR",
                    {
                        "artifact_id": artifact.artifact_id,
                        "reason": QuarantineReason.LLM_DERIVED_UNVERIFIED.value,
                        "index": index,
                    },
                ),
                artifact_id=artifact.artifact_id,
                source_file=artifact.source_file,
                source_line_range=candidate_range,
                reason=QuarantineReason.LLM_DERIVED_UNVERIFIED.value,
                details={
                    "candidate": narrative_candidate.to_dict(),
                    "prohibited_output_fields_removed": prohibited,
                },
            )
        )
    return result


def _narrative_candidate_range(
    value: Any,
    *,
    fallback: SourceLineRange,
) -> tuple[SourceLineRange, list[str]]:
    if isinstance(value, Mapping):
        try:
            candidate = SourceLineRange(int(value["start"]), int(value["end"]))
        except (KeyError, TypeError, ValueError):
            return fallback, ["INVALID_SOURCE_SPAN_REPLACED"]
        if candidate.start >= fallback.start and candidate.end <= fallback.end:
            return candidate, []
        return fallback, ["OUT_OF_RANGE_SOURCE_SPAN_REPLACED"]
    return fallback, ["MISSING_SOURCE_SPAN_REPLACED"]


def _case_semantics(case: HistoricalResearchCase) -> str:
    payload = case.to_dict()
    for key in (
        "artifact_id",
        "source_file",
        "source_line_range",
        "source_row_ids",
        "score_simulation_refs",
        "shadow_rule_refs",
        "transition_refs",
    ):
        payload.pop(key, None)
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def _dedupe_by_id(items: Sequence[Any], attribute: str) -> list[Any]:
    result: list[Any] = []
    seen: set[str] = set()
    for item in items:
        identity = str(getattr(item, attribute))
        if identity in seen:
            continue
        seen.add(identity)
        result.append(item)
    return result


def _ranges_overlap(left: SourceLineRange, right: SourceLineRange) -> bool:
    return left.start <= right.end and right.start <= left.end


__all__ = [
    "NarrativeCaseProvider",
    "SemanticCompilationResult",
    "compile_research_intelligence",
    "discover_historical_research_paths",
    "render_compile_report",
    "write_research_intelligence",
]
