"""JSONL-backed ResearchMemoryStore."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS, large_sector_for_archetype
from e2r.research_brain.schemas import (
    ArchetypeMemoryProfile,
    MemoryType,
    ResearchMemoryRecord,
    SourceQualityClass,
)


class ResearchMemoryStore:
    """Small append-safe JSONL memory store with idempotent add semantics."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._records: dict[str, ResearchMemoryRecord] | None = None
        self._by_archetype: dict[str, tuple[ResearchMemoryRecord, ...]] | None = None
        self._by_large_sector: dict[str, tuple[ResearchMemoryRecord, ...]] | None = None

    def add_records(self, records: Iterable[ResearchMemoryRecord]) -> Mapping[str, int]:
        loaded = self._load()
        before = len(loaded)
        incoming = tuple(records)
        for record in incoming:
            loaded.setdefault(record.record_id, record)
        after = len(loaded)
        self._records = loaded
        self._by_archetype = None
        self._by_large_sector = None
        self._write()
        return {
            "before_count": before,
            "after_count": after,
            "added_count": after - before,
            "duplicate_count": len(incoming) - (after - before),
        }

    def query(
        self,
        *,
        archetype_id: str | None = None,
        large_sector_id: str | None = None,
        memory_type: str | None = None,
        primitive_id: str | None = None,
        source_quality_class: str | None = None,
        allowed_for_runtime_planning: bool = True,
        exclude_future_leakage: bool = True,
        limit: int | None = None,
    ) -> tuple[ResearchMemoryRecord, ...]:
        rows = []
        for record in self._candidate_records(archetype_id=archetype_id, large_sector_id=large_sector_id):
            if archetype_id and record.canonical_archetype_id != archetype_id:
                continue
            if large_sector_id and record.large_sector_id != large_sector_id:
                continue
            if memory_type and record.memory_type != memory_type:
                continue
            if primitive_id and primitive_id not in record.primitive_ids:
                continue
            if source_quality_class and record.source_quality_class != source_quality_class:
                continue
            if allowed_for_runtime_planning and not record.usage_policy.allowed_for_runtime_planning:
                continue
            if exclude_future_leakage and not record.leakage_controls.may_be_seen_by_planner_llm_as_pattern_summary:
                continue
            rows.append(record)
            if limit is not None and len(rows) >= limit:
                break
        return tuple(rows)

    def get_archetype_profile(self, archetype_id: str) -> ArchetypeMemoryProfile:
        return build_archetype_profile(archetype_id, self._records_by_archetype().get(archetype_id, ()))

    def get_source_routes(self, archetype_id: str, primitive_id: str | None = None) -> tuple[ResearchMemoryRecord, ...]:
        return self.query(
            archetype_id=archetype_id,
            memory_type=MemoryType.SOURCE_ROUTE_PATTERN.value,
            primitive_id=primitive_id,
            limit=None,
        )

    def get_false_positive_patterns(self, archetype_id: str) -> tuple[ResearchMemoryRecord, ...]:
        return self.query(archetype_id=archetype_id, memory_type=MemoryType.FALSE_POSITIVE_PATTERN.value, limit=None)

    def get_green_blockers(self, archetype_id: str) -> tuple[ResearchMemoryRecord, ...]:
        return self.query(archetype_id=archetype_id, memory_type=MemoryType.GREEN_BLOCKER.value, limit=None)

    def get_replay_fixtures(self, archetype_id: str) -> tuple[ResearchMemoryRecord, ...]:
        return self.query(archetype_id=archetype_id, memory_type=MemoryType.REPLAY_FIXTURE_CANDIDATE.value, limit=None)

    def get_source_gaps(self, archetype_id: str) -> tuple[ResearchMemoryRecord, ...]:
        return self.query(archetype_id=archetype_id, memory_type=MemoryType.SOURCE_GAP.value, limit=None)

    def records(self) -> tuple[ResearchMemoryRecord, ...]:
        return tuple(self._load().values())

    def summary(self) -> Mapping[str, object]:
        rows = self.records()
        return {
            "memory_record_count": len(rows),
            "memory_type_counts": dict(Counter(row.memory_type for row in rows)),
            "source_quality_class_counts": dict(Counter(row.source_quality_class for row in rows)),
            "usage_policy_counts": {
                "allowed_for_runtime_planning": sum(row.usage_policy.allowed_for_runtime_planning for row in rows),
                "allowed_for_evidence_extraction_prompt": sum(
                    row.usage_policy.allowed_for_evidence_extraction_prompt for row in rows
                ),
                "allowed_for_score_contribution": sum(row.usage_policy.allowed_for_score_contribution for row in rows),
                "allowed_for_replay_fixture": sum(row.usage_policy.allowed_for_replay_fixture for row in rows),
                "allowed_for_ontology": sum(row.usage_policy.allowed_for_ontology for row in rows),
                "allowed_for_query_planning": sum(row.usage_policy.allowed_for_query_planning for row in rows),
                "allowed_for_red_team_planning": sum(row.usage_policy.allowed_for_red_team_planning for row in rows),
            },
            "source_proxy_only_count": sum(row.source_proxy_only for row in rows),
            "evidence_url_pending_count": sum(row.evidence_url_pending for row in rows),
            "runtime_score_eligible_count": sum(row.runtime_score_eligible for row in rows),
        }

    def _load(self) -> dict[str, ResearchMemoryRecord]:
        if self._records is not None:
            return self._records
        records: dict[str, ResearchMemoryRecord] = {}
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    if not line.strip():
                        continue
                    record = ResearchMemoryRecord.from_dict(json.loads(line))
                    records.setdefault(record.record_id, record)
        self._records = records
        return records

    def _candidate_records(
        self,
        *,
        archetype_id: str | None,
        large_sector_id: str | None,
    ) -> Iterable[ResearchMemoryRecord]:
        if archetype_id:
            return self._records_by_archetype().get(archetype_id, ())
        if large_sector_id:
            return self._records_by_large_sector().get(large_sector_id, ())
        return self._load().values()

    def _records_by_archetype(self) -> dict[str, tuple[ResearchMemoryRecord, ...]]:
        if self._by_archetype is None:
            grouped: dict[str, list[ResearchMemoryRecord]] = {}
            for record in self._load().values():
                grouped.setdefault(record.canonical_archetype_id, []).append(record)
            self._by_archetype = {key: tuple(value) for key, value in grouped.items()}
        return self._by_archetype

    def _records_by_large_sector(self) -> dict[str, tuple[ResearchMemoryRecord, ...]]:
        if self._by_large_sector is None:
            grouped: dict[str, list[ResearchMemoryRecord]] = {}
            for record in self._load().values():
                grouped.setdefault(record.large_sector_id, []).append(record)
            self._by_large_sector = {key: tuple(value) for key, value in grouped.items()}
        return self._by_large_sector

    def _write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        rows = sorted(self._load().values(), key=lambda item: item.record_id)
        with self.path.open("w", encoding="utf-8") as handle:
            for record in rows:
                handle.write(json.dumps(record.to_dict(), ensure_ascii=False, sort_keys=True) + "\n")


def build_archetype_profile(archetype_id: str, records: Sequence[ResearchMemoryRecord]) -> ArchetypeMemoryProfile:
    rows = tuple(records)
    quality_counts = Counter(row.source_quality_class for row in rows)
    memory_count = Counter(row.memory_type for row in rows)
    primitive_ids = _unique(item for row in rows for item in row.primitive_ids)
    source_routes = _unique(item for row in rows for item in row.free_source_route_hints)
    source_family_reliability = _unique(row.source_family for row in rows if row.source_family)
    green_blockers = _unique(item for row in rows for item in row.green_blockers)
    false_positives = _unique(item for row in rows for item in row.false_positive_patterns)
    runtime_usage_policy = _runtime_usage_policy(rows)
    fixture_status = {
        "positive_url_backed": any(
            row.source_quality_class == SourceQualityClass.A_URL_BACKED_REPLAY_READY.value
            and row.memory_type in {MemoryType.REPLAY_FIXTURE_CANDIDATE.value, MemoryType.PRODUCTION_FIXTURE_CANDIDATE.value}
            for row in rows
        ),
        "guard_url_backed": any(
            row.source_quality_class == SourceQualityClass.A_URL_BACKED_REPLAY_READY.value
            and row.memory_type
            in {
                MemoryType.FALSE_POSITIVE_PATTERN.value,
                MemoryType.COUNTEREXAMPLE.value,
                MemoryType.HARD_BREAK_PATTERN.value,
            }
            for row in rows
        ),
        "wrong_subject": any("target_scope_guard" in row.guard_primitives for row in rows),
        "old_risk_resolved": any("temporal_lifecycle_guard" in row.guard_primitives for row in rows),
        "current_hard_break": any(row.memory_type == MemoryType.HARD_BREAK_PATTERN.value for row in rows),
        "source_missing_pending": any(row.memory_type == MemoryType.SOURCE_GAP.value for row in rows),
    }
    return ArchetypeMemoryProfile(
        canonical_archetype_id=archetype_id,
        large_sector_id=large_sector_for_archetype(archetype_id),
        memory_record_count=len(rows),
        url_backed_count=quality_counts[SourceQualityClass.A_URL_BACKED_REPLAY_READY.value]
        + quality_counts[SourceQualityClass.B_URL_BACKED_REPAIR_NEEDED.value],
        source_proxy_count=quality_counts[SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY.value],
        price_path_only_count=quality_counts[SourceQualityClass.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK.value],
        production_fixture_count=memory_count[MemoryType.PRODUCTION_FIXTURE_CANDIDATE.value],
        ontology_only_count=memory_count[MemoryType.ONTOLOGY_ONLY_RULE_CANDIDATE.value],
        positive_patterns=_sample_notes(rows, MemoryType.PRIMITIVE_SUCCESS_CASE.value),
        failure_patterns=_sample_notes(rows, MemoryType.PRIMITIVE_FAILURE_CASE.value),
        false_positive_patterns=false_positives,
        green_blockers=green_blockers,
        yellow_blockers=_sample_notes(rows, MemoryType.YELLOW_BLOCKER.value),
        stage2_unlock_conditions=_sample_notes(rows, MemoryType.STAGE2_ACTIONABLE_UNLOCK.value),
        stage2_cap_conditions=_sample_notes(rows, MemoryType.STAGE2_WATCH_CAP.value),
        four_b_watch_conditions=_sample_notes(rows, MemoryType.FOUR_B_WATCH_CONDITION.value),
        four_c_thesis_break_conditions=_sample_notes(rows, MemoryType.FOUR_C_THESIS_BREAK_CONDITION.value),
        required_primitives_observed=primitive_ids,
        optional_primitives_observed=primitive_ids,
        guard_primitives_observed=_unique(item for row in rows for item in row.guard_primitives),
        hard_break_primitives_observed=_unique(item for row in rows for item in row.hard_break_primitives),
        source_routes=source_routes,
        source_family_reliability=source_family_reliability,
        query_pattern_hints=_unique(item for row in rows for item in row.query_pattern_hints),
        bad_query_patterns=_unique(item for row in rows for item in row.bad_query_patterns),
        fixture_status=fixture_status,
        source_gap_summary=_sample_notes(rows, MemoryType.SOURCE_GAP.value),
        runtime_usage_policy=runtime_usage_policy,
    )


def build_all_archetype_profiles(records: Sequence[ResearchMemoryRecord]) -> tuple[ArchetypeMemoryProfile, ...]:
    by_archetype: dict[str, list[ResearchMemoryRecord]] = {archetype_id: [] for archetype_id in CANONICAL_ARCHETYPE_IDS}
    for record in records:
        if record.canonical_archetype_id in by_archetype:
            by_archetype[record.canonical_archetype_id].append(record)
    return tuple(build_archetype_profile(archetype_id, tuple(rows)) for archetype_id, rows in by_archetype.items())


def _runtime_usage_policy(rows: Sequence[ResearchMemoryRecord]) -> str:
    if not rows:
        return "source_gap"
    if any(row.source_quality_class == SourceQualityClass.A_URL_BACKED_REPLAY_READY.value for row in rows):
        return "ready"
    if any(row.usage_policy.allowed_for_runtime_planning for row in rows):
        return "planning_only"
    return "unsupported"


def _sample_notes(rows: Sequence[ResearchMemoryRecord], memory_type: str, limit: int = 8) -> tuple[str, ...]:
    values: list[str] = []
    for row in rows:
        if row.memory_type != memory_type:
            continue
        note = row.notes or row.source_line_or_span or row.record_id
        values.append(note)
        if len(values) >= limit:
            break
    return tuple(dict.fromkeys(values))


def _unique(values: Iterable[str | None], limit: int = 40) -> tuple[str, ...]:
    result: list[str] = []
    for value in values:
        if not value:
            continue
        if value not in result:
            result.append(value)
        if len(result) >= limit:
            break
    return tuple(result)


__all__ = ["ResearchMemoryStore", "build_all_archetype_profiles", "build_archetype_profile"]
