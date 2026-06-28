"""Compile research artifacts into a ResearchMemoryStore."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Mapping, Sequence

from e2r.research_brain.artifact_discovery import discover_research_artifacts, inventory_summary
from e2r.research_brain.memory_store import ResearchMemoryStore, build_all_archetype_profiles
from e2r.research_brain.research_artifact_parser import parse_research_artifact
from e2r.research_brain.research_row_normalizer import normalize_raw_research_row
from e2r.research_brain.schemas import ArtifactInventoryRow, ResearchMemoryRecord


_ROW_ARCHETYPE_RE = re.compile(r"\b(?:C\d{2}_[A-Za-z0-9_]+|R13_[A-Za-z0-9_]+)\b")


def compile_research_memory(
    *,
    repo_root: str | Path = ".",
    output_store_path: str | Path,
    discovery_roots: Sequence[str | Path] | None = None,
    max_rows_per_artifact: int | None = 200,
    max_total_compiled_rows: int | None = 50_000,
) -> Mapping[str, object]:
    inventory_rows = discover_research_artifacts(
        root=repo_root,
        discovery_roots=tuple(discovery_roots) if discovery_roots is not None else ("docs", "output", "reports/e2r_calibration", "fixtures/historical", "configs"),
    )
    parsed_row_count = 0
    records_by_id: dict[str, ResearchMemoryRecord] = {}
    parse_errors: list[Mapping[str, str]] = []
    compiled_row_count = 0
    for artifact in inventory_rows:
        if max_total_compiled_rows is not None and compiled_row_count >= max_total_compiled_rows:
            break
        if artifact.parse_error_count:
            continue
        if not _artifact_may_contain_research_memory(artifact):
            continue
        try:
            raw_rows = parse_research_artifact(artifact.path, artifact)
            parsed_row_count += len(raw_rows)
            compiled_for_artifact = 0
            for raw_row in raw_rows:
                if not _raw_row_may_contain_research_memory(raw_row.text, raw_row.source_artifact_path):
                    continue
                for record in normalize_raw_research_row(raw_row):
                    records_by_id.setdefault(record.record_id, record)
                compiled_for_artifact += 1
                compiled_row_count += 1
                if max_rows_per_artifact is not None and compiled_for_artifact >= max_rows_per_artifact:
                    break
                if max_total_compiled_rows is not None and compiled_row_count >= max_total_compiled_rows:
                    break
        except Exception as exc:  # pragma: no cover - defensive bulk compiler path
            parse_errors.append({"path": artifact.path, "error": f"{type(exc).__name__}: {exc}"})
    records = tuple(records_by_id.values())
    store = ResearchMemoryStore(output_store_path)
    first_add = store.add_records(records)
    second_add = store.add_records(records)
    profiles = build_all_archetype_profiles(store.records())
    summary = build_memory_compile_summary(
        inventory_rows=inventory_rows,
        parsed_row_count=parsed_row_count,
        records=store.records(),
        add_result=first_add,
        second_add_result=second_add,
        parse_error_count=len(parse_errors),
        max_rows_per_artifact=max_rows_per_artifact,
        max_total_compiled_rows=max_total_compiled_rows,
        compiled_row_count=compiled_row_count,
    )
    return {
        "schema_version": "research_brain_memory_compile_manifest_v1",
        "summary": summary,
        "inventory_rows": [row.__dict__ for row in inventory_rows],
        "memory_store_path": str(output_store_path),
        "profiles": [profile.to_dict() for profile in profiles],
        "parse_errors": parse_errors[:200],
    }


def _artifact_may_contain_research_memory(artifact: ArtifactInventoryRow) -> bool:
    if artifact.detected_canonical_archetype_id or artifact.detected_large_sector_id:
        return True
    if artifact.schema_family in {"research_memory", "evidence_os", "v12_research", "score_stage_report"}:
        return True
    if artifact.source_proxy_count or artifact.evidence_url_pending_count or artifact.calibration_usable_count:
        return True
    path = artifact.path.lower()
    return any(token in path for token in ("research", "v12", "round", "archetype", "calibration", "replay"))


def _raw_row_may_contain_research_memory(text: str, path: str) -> bool:
    if _ROW_ARCHETYPE_RE.search(text):
        return True
    lower = text.lower()
    return any(
        token in lower
        for token in (
            "source_proxy_only",
            "evidence_url_pending",
            "archetype_id",
            "canonical_archetype_id",
            "source_url",
            "evidence_url",
            "primitive",
            "green",
            "stage",
            "green blocker",
            "false positive",
            "source route",
            "query",
            "4b",
            "4c",
        )
    )


def build_memory_compile_summary(
    *,
    inventory_rows: Sequence[ArtifactInventoryRow],
    parsed_row_count: int,
    records: Sequence[ResearchMemoryRecord],
    add_result: Mapping[str, int],
    second_add_result: Mapping[str, int],
    parse_error_count: int,
    max_rows_per_artifact: int | None,
    max_total_compiled_rows: int | None,
    compiled_row_count: int,
) -> Mapping[str, object]:
    quality_counts = Counter(record.source_quality_class for record in records)
    memory_type_counts = Counter(record.memory_type for record in records)
    usage_counts = {
        "allowed_for_runtime_planning": sum(record.usage_policy.allowed_for_runtime_planning for record in records),
        "allowed_for_evidence_extraction_prompt": sum(
            record.usage_policy.allowed_for_evidence_extraction_prompt for record in records
        ),
        "allowed_for_score_contribution": sum(record.usage_policy.allowed_for_score_contribution for record in records),
        "allowed_for_replay_fixture": sum(record.usage_policy.allowed_for_replay_fixture for record in records),
        "allowed_for_ontology": sum(record.usage_policy.allowed_for_ontology for record in records),
        "allowed_for_query_planning": sum(record.usage_policy.allowed_for_query_planning for record in records),
        "allowed_for_red_team_planning": sum(record.usage_policy.allowed_for_red_team_planning for record in records),
    }
    inventory = inventory_summary(inventory_rows)
    return {
        **inventory,
        "parsed_row_count": parsed_row_count,
        "memory_record_count": len(records),
        "memory_type_counts": dict(memory_type_counts),
        "source_quality_class_counts": dict(quality_counts),
        "usage_policy_counts": usage_counts,
        "source_proxy_only_count": sum(record.source_proxy_only for record in records),
        "evidence_url_pending_count": sum(record.evidence_url_pending for record in records),
        "production_fixture_count": sum(record.fixture_usable for record in records),
        "runtime_score_eligible_count": sum(record.runtime_score_eligible for record in records),
        "memory_record_without_usage_policy_count": sum(record.usage_policy is None for record in records),
        "first_import_added_count": add_result.get("added_count", 0),
        "frozen_import_duplicate_growth_count": second_add_result.get("added_count", 0),
        "parser_parse_error_count": parse_error_count,
        "row_sample_strategy": "bounded_research_rows_per_artifact" if max_rows_per_artifact is not None else "all_research_rows",
        "max_rows_per_artifact": max_rows_per_artifact,
        "max_total_compiled_rows": max_total_compiled_rows,
        "compiled_row_count": compiled_row_count,
        "compiled_row_budget_exhausted": bool(max_total_compiled_rows is not None and compiled_row_count >= max_total_compiled_rows),
    }


__all__ = ["compile_research_memory", "build_memory_compile_summary"]
