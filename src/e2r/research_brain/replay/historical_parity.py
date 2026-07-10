"""Frozen, evaluator-separated historical replay parity contracts."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.retrieval import (
    BalancedRetrievalBenchmarkAudit,
    BlindRetrievalBenchmarkCase,
)
from e2r.research_brain.runtime.run_mode_separation import (
    CanonicalRunMode,
    claim_mode_output_root,
    forbidden_planner_context_paths,
)


HISTORICAL_REPLAY_PARITY_SCHEMA_VERSION = "e2r_historical_replay_parity_v1"


class HistoricalAttemptStatus(str, Enum):
    RETRIEVAL_ATTEMPTED = "RETRIEVAL_ATTEMPTED"
    NOT_ATTEMPTED = "NOT_ATTEMPTED"


class HistoricalSourceResolution(str, Enum):
    URL_BACKED_REPLAY = "URL_BACKED_REPLAY"
    EXACT_BLOCKER = "EXACT_BLOCKER"


class HistoricalGuardKind(str, Enum):
    POSITIVE = "POSITIVE"
    COUNTER_GUARD = "COUNTER_GUARD"
    WRONG_SUBJECT = "WRONG_SUBJECT"
    OLD_RISK = "OLD_RISK"
    SOURCE_MISSING = "SOURCE_MISSING"


class HistoricalGuardDecision(str, Enum):
    ACCEPT_EVALUATOR_HIT = "ACCEPT_EVALUATOR_HIT"
    REJECT_SCORE = "REJECT_SCORE"
    NO_CURRENT_PENALTY = "NO_CURRENT_PENALTY"
    SOURCE_PENDING = "SOURCE_PENDING"


_EXPECTED_GUARD_DECISION: Mapping[HistoricalGuardKind, HistoricalGuardDecision] = {
    HistoricalGuardKind.POSITIVE: HistoricalGuardDecision.ACCEPT_EVALUATOR_HIT,
    HistoricalGuardKind.COUNTER_GUARD: HistoricalGuardDecision.REJECT_SCORE,
    HistoricalGuardKind.WRONG_SUBJECT: HistoricalGuardDecision.REJECT_SCORE,
    HistoricalGuardKind.OLD_RISK: HistoricalGuardDecision.NO_CURRENT_PENALTY,
    HistoricalGuardKind.SOURCE_MISSING: HistoricalGuardDecision.SOURCE_PENDING,
}


@dataclass(frozen=True)
class HistoricalGuardProbe:
    probe_id: str
    guard_kind: str
    frozen_as_of_date: str
    evidence_reference_id: str
    observed_decision: str
    evaluator_only: bool = True
    current_score_credit: int = 0
    current_watchlist_eligible: bool = False

    def __post_init__(self) -> None:
        kind = HistoricalGuardKind(self.guard_kind)
        decision = HistoricalGuardDecision(self.observed_decision)
        date.fromisoformat(self.frozen_as_of_date)
        if not self.probe_id.strip() or not self.evidence_reference_id.strip():
            raise ValueError("historical guard probe identity is required")
        if not isinstance(self.evaluator_only, bool) or not self.evaluator_only:
            raise ValueError("historical guard probe must remain evaluator-only")
        if decision != _EXPECTED_GUARD_DECISION[kind]:
            raise ValueError("historical guard probe observed the wrong decision")
        if self.current_score_credit != 0:
            raise ValueError("historical guard probe cannot receive current score credit")
        if self.current_watchlist_eligible:
            raise ValueError("historical guard probe cannot enter current watchlist")

    @property
    def passed(self) -> bool:
        return HistoricalGuardDecision(self.observed_decision) == _EXPECTED_GUARD_DECISION[
            HistoricalGuardKind(self.guard_kind)
        ]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FrozenReplaySourceStatus:
    archetype_id: str
    resolution: str
    replay_source_reference_ids: tuple[str, ...] = ()
    blocker_reason: str | None = None
    source_proxy_reference_ids: tuple[str, ...] = ()
    source_proxy_score_credit: int = 0

    def __post_init__(self) -> None:
        if self.archetype_id not in CANONICAL_ARCHETYPE_IDS:
            raise ValueError("historical source status uses unknown archetype")
        resolution = HistoricalSourceResolution(self.resolution)
        if resolution == HistoricalSourceResolution.URL_BACKED_REPLAY:
            if not self.replay_source_reference_ids or self.blocker_reason is not None:
                raise ValueError("URL-backed replay requires source ids and no blocker")
        elif self.replay_source_reference_ids or not str(self.blocker_reason or "").strip():
            raise ValueError("blocked replay source requires one exact blocker reason")
        for values in (
            self.replay_source_reference_ids,
            self.source_proxy_reference_ids,
        ):
            if len(values) != len(set(values)) or any(not item.strip() for item in values):
                raise ValueError("historical source references must be unique and non-empty")
        if self.source_proxy_score_credit != 0:
            raise ValueError("source proxy cannot receive historical replay score credit")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class HistoricalReplayBenchmarkLeaf:
    benchmark_id: str
    archetype_id: str
    expected_primitive_id: str
    frozen_as_of_date: str
    planner_input: Mapping[str, Any]
    planner_input_hash: str
    evaluator_expected_hash: str
    predicted_archetype_ids: tuple[str, ...]
    predicted_recipe_ids: tuple[str, ...]
    top1_hit: bool
    top3_hit: bool
    mapping_evaluated: bool
    mapping_correct: bool | None
    positive_evaluated: bool
    positive_retrieved: bool | None
    guard_evaluated: bool
    guard_correct: bool | None
    source_resolution: str
    replay_source_reference_ids: tuple[str, ...]
    source_blocker_reason: str | None
    source_proxy_reference_ids: tuple[str, ...]
    source_proxy_score_credit: int
    future_leakage_count: int
    planner_forbidden_context_paths: tuple[str, ...]
    current_watchlist_eligible: bool = False
    schema_version: str = HISTORICAL_REPLAY_PARITY_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.archetype_id not in CANONICAL_ARCHETYPE_IDS:
            raise ValueError("historical benchmark leaf uses unknown archetype")
        date.fromisoformat(self.frozen_as_of_date)
        HistoricalSourceResolution(self.source_resolution)
        if not all(
            item.strip()
            for item in (
                self.benchmark_id,
                self.expected_primitive_id,
                self.planner_input_hash,
                self.evaluator_expected_hash,
            )
        ):
            raise ValueError("historical benchmark leaf identity is required")
        for name in (
            "top1_hit",
            "top3_hit",
            "mapping_evaluated",
            "positive_evaluated",
            "guard_evaluated",
            "current_watchlist_eligible",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"historical benchmark {name} must be boolean")
        for evaluated, value, context in (
            (self.mapping_evaluated, self.mapping_correct, "mapping"),
            (self.positive_evaluated, self.positive_retrieved, "positive"),
            (self.guard_evaluated, self.guard_correct, "guard"),
        ):
            if evaluated != isinstance(value, bool):
                raise ValueError(f"historical benchmark {context} evaluation mismatch")
        if self.future_leakage_count < 0:
            raise ValueError("historical benchmark future leakage cannot be negative")
        if self.planner_forbidden_context_paths:
            raise ValueError("historical evaluator/outcome context entered planner input")
        if self.source_proxy_score_credit != 0:
            raise ValueError("historical source proxy received score credit")
        if self.current_watchlist_eligible:
            raise ValueError("historical replay leaf cannot enter current watchlist")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_planner_record(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "benchmark_id": self.benchmark_id,
            "frozen_as_of_date": self.frozen_as_of_date,
            "planner_input": dict(self.planner_input),
            "planner_input_hash": self.planner_input_hash,
        }

    def to_evaluator_record(self) -> dict[str, Any]:
        payload = self.to_dict()
        payload.pop("planner_input")
        return payload


@dataclass(frozen=True)
class HistoricalArchetypeParityRow:
    archetype_id: str
    attempt_status: str
    attempt_reason: str | None
    benchmark_ids: tuple[str, ...]
    source_resolution: str
    source_blocker_reason: str | None
    top1_hit_count: int
    top3_hit_count: int
    benchmark_count: int
    mapping_evaluated_count: int
    mapping_correct_count: int
    positive_evaluated_count: int
    positive_retrieved_count: int
    guard_evaluated_count: int
    guard_correct_count: int
    current_watchlist_eligible: bool = False

    def __post_init__(self) -> None:
        if self.archetype_id not in CANONICAL_ARCHETYPE_IDS:
            raise ValueError("historical parity row uses unknown archetype")
        status = HistoricalAttemptStatus(self.attempt_status)
        HistoricalSourceResolution(self.source_resolution)
        if status == HistoricalAttemptStatus.NOT_ATTEMPTED:
            if self.benchmark_ids or not str(self.attempt_reason or "").strip():
                raise ValueError("NOT_ATTEMPTED replay row requires an exact reason")
        elif not self.benchmark_ids or self.attempt_reason is not None:
            raise ValueError("attempted replay row requires benchmark leaves")
        if self.benchmark_count != len(self.benchmark_ids):
            raise ValueError("historical parity benchmark count mismatch")
        counts = (
            self.top1_hit_count,
            self.top3_hit_count,
            self.mapping_evaluated_count,
            self.mapping_correct_count,
            self.positive_evaluated_count,
            self.positive_retrieved_count,
            self.guard_evaluated_count,
            self.guard_correct_count,
        )
        if any(value < 0 for value in counts):
            raise ValueError("historical parity counts cannot be negative")
        if self.top1_hit_count > self.benchmark_count or self.top3_hit_count > self.benchmark_count:
            raise ValueError("historical parity hit count exceeds benchmark count")
        if (
            self.mapping_correct_count > self.mapping_evaluated_count
            or self.positive_retrieved_count > self.positive_evaluated_count
            or self.guard_correct_count > self.guard_evaluated_count
        ):
            raise ValueError("historical parity correct count exceeds evaluated count")
        if self.current_watchlist_eligible:
            raise ValueError("historical parity row cannot enter current watchlist")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class HistoricalReplayParityResult:
    run_id: str
    frozen_as_of_date: str
    benchmark_leaves: tuple[HistoricalReplayBenchmarkLeaf, ...]
    archetype_rows: tuple[HistoricalArchetypeParityRow, ...]
    guard_probes: tuple[HistoricalGuardProbe, ...]
    manifest: Mapping[str, Any]
    mode: str = CanonicalRunMode.HISTORICAL_REPLAY.value
    production_runtime_ready: bool = False

    def __post_init__(self) -> None:
        CanonicalRunMode(self.mode)
        date.fromisoformat(self.frozen_as_of_date)
        if (
            not self.run_id.strip()
            or not self.benchmark_leaves
            or not self.archetype_rows
        ):
            raise ValueError("historical replay result requires run and leaf artifacts")
        if self.mode != CanonicalRunMode.HISTORICAL_REPLAY.value:
            raise ValueError("historical replay result mode mismatch")
        if self.production_runtime_ready:
            raise ValueError("Phase 11 replay parity cannot claim production readiness")
        if any(
            item.frozen_as_of_date != self.frozen_as_of_date
            for item in (*self.benchmark_leaves, *self.guard_probes)
        ):
            raise ValueError("historical replay result mixes frozen as-of dates")
        expected_leaf_hash = stable_hash(
            {
                "leaves": [item.to_dict() for item in self.benchmark_leaves],
                "rows": [item.to_dict() for item in self.archetype_rows],
                "guard_probes": [item.to_dict() for item in self.guard_probes],
            }
        )
        if (
            self.manifest.get("run_id") != self.run_id
            or self.manifest.get("mode") != self.mode
            or self.manifest.get("frozen_as_of_date") != self.frozen_as_of_date
            or self.manifest.get("leaf_hash") != expected_leaf_hash
        ):
            raise ValueError("historical replay result manifest identity mismatch")


def compile_historical_replay_parity(
    *,
    retrieval_audit: BalancedRetrievalBenchmarkAudit,
    benchmark_cases: Sequence[BlindRetrievalBenchmarkCase],
    frozen_as_of_date: str,
    guard_probes: Sequence[HistoricalGuardProbe],
    source_statuses: Sequence[FrozenReplaySourceStatus] = (),
) -> HistoricalReplayParityResult:
    frozen_date = date.fromisoformat(frozen_as_of_date)
    guard_by_id = {item.probe_id: item for item in guard_probes}
    if len(guard_by_id) != len(guard_probes):
        raise ValueError("historical guard probe ids are not unique")
    if any(date.fromisoformat(item.frozen_as_of_date) != frozen_date for item in guard_probes):
        raise ValueError("historical guard probes are not frozen to replay as-of date")
    benchmark_by_id = {item.benchmark_id: item for item in benchmark_cases}
    if len(benchmark_by_id) != len(benchmark_cases):
        raise ValueError("historical replay benchmark ids are not unique")
    if any(date.fromisoformat(item.as_of_date) != frozen_date for item in benchmark_cases):
        raise ValueError("historical replay benchmark is not frozen to one as-of date")
    source_by_archetype = {item.archetype_id: item for item in source_statuses}
    if len(source_by_archetype) != len(source_statuses):
        raise ValueError("historical replay source status archetypes are not unique")
    leaves: list[HistoricalReplayBenchmarkLeaf] = []
    seen_rows: set[str] = set()
    for raw_row in retrieval_audit.rows:
        benchmark_id = str(raw_row["benchmark_id"])
        if benchmark_id in seen_rows or benchmark_id not in benchmark_by_id:
            raise ValueError("historical replay retrieval row identity mismatch")
        seen_rows.add(benchmark_id)
        benchmark = benchmark_by_id[benchmark_id]
        planner_input = benchmark.to_request().to_dict()
        source = source_by_archetype.get(
            benchmark.expected_archetype_id,
            FrozenReplaySourceStatus(
                archetype_id=benchmark.expected_archetype_id,
                resolution=HistoricalSourceResolution.EXACT_BLOCKER.value,
                blocker_reason="NO_URL_BACKED_FROZEN_SOURCE_FOR_ARCHETYPE",
            ),
        )
        predicted_archetypes = tuple(str(item) for item in raw_row["top_archetype_ids"])
        predicted_recipes = tuple(str(item) for item in raw_row["direct_recipe_ids"])
        mapping_evaluated = bool(raw_row["required_recipe_expected"])
        expected_recipe_id = raw_row.get("expected_recipe_id")
        balanced_roles = set(raw_row.get("balanced_roles") or ())
        leaves.append(
            HistoricalReplayBenchmarkLeaf(
                benchmark_id=benchmark_id,
                archetype_id=benchmark.expected_archetype_id,
                expected_primitive_id=benchmark.expected_primitive_id,
                frozen_as_of_date=benchmark.as_of_date,
                planner_input=planner_input,
                planner_input_hash=stable_hash(planner_input),
                evaluator_expected_hash=stable_hash(
                    {
                        "archetype_id": benchmark.expected_archetype_id,
                        "primitive_id": benchmark.expected_primitive_id,
                        "recipe_id": expected_recipe_id,
                    }
                ),
                predicted_archetype_ids=predicted_archetypes,
                predicted_recipe_ids=predicted_recipes,
                top1_hit=bool(
                    predicted_archetypes
                    and predicted_archetypes[0] == benchmark.expected_archetype_id
                ),
                top3_hit=bool(raw_row["top3_archetype_hit"]),
                mapping_evaluated=mapping_evaluated,
                mapping_correct=(
                    bool(
                        predicted_recipes
                        and expected_recipe_id
                        and predicted_recipes[0] == expected_recipe_id
                    )
                    if mapping_evaluated
                    else None
                ),
                positive_evaluated=mapping_evaluated,
                positive_retrieved=(
                    "POSITIVE" in balanced_roles if mapping_evaluated else None
                ),
                guard_evaluated=mapping_evaluated,
                guard_correct=(
                    {
                        "COUNTEREXAMPLE_GUARD",
                        "SEMANTIC_GUARD",
                    }
                    <= balanced_roles
                    if mapping_evaluated
                    else None
                ),
                source_resolution=source.resolution,
                replay_source_reference_ids=source.replay_source_reference_ids,
                source_blocker_reason=source.blocker_reason,
                source_proxy_reference_ids=source.source_proxy_reference_ids,
                source_proxy_score_credit=source.source_proxy_score_credit,
                future_leakage_count=int(raw_row["future_leakage_count"]),
                planner_forbidden_context_paths=forbidden_planner_context_paths(
                    planner_input
                ),
            )
        )
    if seen_rows != set(benchmark_by_id):
        raise ValueError("historical replay has benchmark cases without retrieval leaves")

    rows: list[HistoricalArchetypeParityRow] = []
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        related = tuple(item for item in leaves if item.archetype_id == archetype_id)
        source = source_by_archetype.get(
            archetype_id,
            FrozenReplaySourceStatus(
                archetype_id=archetype_id,
                resolution=HistoricalSourceResolution.EXACT_BLOCKER.value,
                blocker_reason="NO_URL_BACKED_FROZEN_SOURCE_FOR_ARCHETYPE",
            ),
        )
        mapping_related = tuple(item for item in related if item.mapping_evaluated)
        positive_related = tuple(item for item in related if item.positive_evaluated)
        guard_related = tuple(item for item in related if item.guard_evaluated)
        rows.append(
            HistoricalArchetypeParityRow(
                archetype_id=archetype_id,
                attempt_status=(
                    HistoricalAttemptStatus.RETRIEVAL_ATTEMPTED.value
                    if related
                    else HistoricalAttemptStatus.NOT_ATTEMPTED.value
                ),
                attempt_reason=(None if related else "NO_BLIND_BENCHMARK_CASE"),
                benchmark_ids=tuple(item.benchmark_id for item in related),
                source_resolution=source.resolution,
                source_blocker_reason=source.blocker_reason,
                top1_hit_count=sum(item.top1_hit for item in related),
                top3_hit_count=sum(item.top3_hit for item in related),
                benchmark_count=len(related),
                mapping_evaluated_count=len(mapping_related),
                mapping_correct_count=sum(
                    item.mapping_correct is True for item in mapping_related
                ),
                positive_evaluated_count=len(positive_related),
                positive_retrieved_count=sum(
                    item.positive_retrieved is True for item in positive_related
                ),
                guard_evaluated_count=len(guard_related),
                guard_correct_count=sum(
                    item.guard_correct is True for item in guard_related
                ),
            )
        )

    archetype_benchmarks = tuple(
        item for item in leaves if benchmark_by_id[item.benchmark_id].archetype_retrieval_expected
    )
    mapping_leaves = tuple(item for item in leaves if item.mapping_evaluated)
    positive_leaves = tuple(item for item in leaves if item.positive_evaluated)
    guard_leaves = tuple(item for item in leaves if item.guard_evaluated)

    def rate(numerator: int, denominator: int) -> float:
        return round(numerator / denominator, 6) if denominator else 0.0

    top1_rate = rate(sum(item.top1_hit for item in archetype_benchmarks), len(archetype_benchmarks))
    top3_rate = rate(sum(item.top3_hit for item in archetype_benchmarks), len(archetype_benchmarks))
    mapping_precision = rate(
        sum(item.mapping_correct is True for item in mapping_leaves),
        len(mapping_leaves),
    )
    positive_recall = rate(
        sum(item.positive_retrieved is True for item in positive_leaves),
        len(positive_leaves),
    )
    guard_accuracy = rate(
        sum(item.guard_correct is True for item in guard_leaves),
        len(guard_leaves),
    )
    critical = {
        "registry_coverage_below_1_00": int(
            sum(bool(item.benchmark_ids) for item in rows) != len(CANONICAL_ARCHETYPE_IDS)
        ),
        "parity_row_missing": len(CANONICAL_ARCHETYPE_IDS) - len(rows),
        "not_attempted_without_reason": sum(
            item.attempt_status == HistoricalAttemptStatus.NOT_ATTEMPTED.value
            and not item.attempt_reason
            for item in rows
        ),
        "source_without_url_or_blocker": sum(
            (
                item.source_resolution
                == HistoricalSourceResolution.URL_BACKED_REPLAY.value
                and (
                    source_by_archetype.get(item.archetype_id) is None
                    or not source_by_archetype[
                        item.archetype_id
                    ].replay_source_reference_ids
                )
            )
            or (
                item.source_resolution
                == HistoricalSourceResolution.EXACT_BLOCKER.value
                and not item.source_blocker_reason
            )
            for item in rows
        ),
        "critical_guard_not_checked": sum(
            item.guard_evaluated and item.guard_correct is not True for item in leaves
        ),
        "guard_probe_kind_missing": len(HistoricalGuardKind)
        - len({HistoricalGuardKind(item.guard_kind) for item in guard_probes}),
        "guard_probe_failed": sum(not item.passed for item in guard_probes),
        "source_proxy_score_credit": sum(item.source_proxy_score_credit for item in leaves),
        "top3_below_0_95": int(top3_rate < 0.95),
        "top1_below_0_85": int(top1_rate < 0.85),
        "mapping_precision_below_0_95": int(mapping_precision < 0.95),
        "positive_recall_below_0_90": int(positive_recall < 0.90),
        "guard_accuracy_below_0_95": int(guard_accuracy < 0.95),
        "future_leakage": sum(item.future_leakage_count for item in leaves),
        "evaluator_or_outcome_prompt_leakage": sum(
            len(item.planner_forbidden_context_paths) for item in leaves
        ),
        "historical_current_watchlist_contamination": sum(
            item.current_watchlist_eligible for item in leaves
        )
        + sum(item.current_watchlist_eligible for item in guard_probes),
    }
    leaf_payload = [item.to_dict() for item in leaves]
    row_payload = [item.to_dict() for item in rows]
    guard_payload = [item.to_dict() for item in guard_probes]
    leaf_hash = stable_hash(
        {
            "leaves": leaf_payload,
            "rows": row_payload,
            "guard_probes": guard_payload,
        }
    )
    run_id = f"HREPLAY-{stable_hash({'as_of': frozen_as_of_date, 'leaf_hash': leaf_hash})[:24]}"
    manifest = {
        "schema_version": HISTORICAL_REPLAY_PARITY_SCHEMA_VERSION,
        "status": (
            "HISTORICAL_REPLAY_PARITY_PASS"
            if leaves and sum(critical.values()) == 0
            else "HISTORICAL_REPLAY_PARITY_FAIL"
        ),
        "run_id": run_id,
        "mode": CanonicalRunMode.HISTORICAL_REPLAY.value,
        "output_namespace": "historical_replay",
        "frozen_as_of_date": frozen_as_of_date,
        "registry_archetype_count": len(CANONICAL_ARCHETYPE_IDS),
        "registry_covered_archetype_count": sum(bool(item.benchmark_ids) for item in rows),
        "registry_coverage_rate": rate(
            sum(bool(item.benchmark_ids) for item in rows),
            len(CANONICAL_ARCHETYPE_IDS),
        ),
        "archetype_parity_row_count": len(rows),
        "benchmark_leaf_count": len(leaves),
        "guard_probe_count": len(guard_probes),
        "guard_probe_kind_count": len(
            {HistoricalGuardKind(item.guard_kind) for item in guard_probes}
        ),
        "guard_probe_pass_rate": rate(
            sum(item.passed for item in guard_probes),
            len(guard_probes),
        ),
        "guard_probe_counts": {
            kind.value: sum(item.guard_kind == kind.value for item in guard_probes)
            for kind in HistoricalGuardKind
        },
        "url_backed_archetype_count": sum(
            item.source_resolution == HistoricalSourceResolution.URL_BACKED_REPLAY.value
            for item in rows
        ),
        "exact_source_blocker_archetype_count": sum(
            item.source_resolution == HistoricalSourceResolution.EXACT_BLOCKER.value
            for item in rows
        ),
        "top1_accuracy": top1_rate,
        "top3_accuracy": top3_rate,
        "mapping_precision": mapping_precision,
        "positive_recall": positive_recall,
        "guard_accuracy": guard_accuracy,
        "future_leakage_count": critical["future_leakage"],
        "source_proxy_score_credit_count": critical["source_proxy_score_credit"],
        "current_watchlist_eligible_count": 0,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "leaf_hash": leaf_hash,
        "production_runtime_ready": False,
    }
    return HistoricalReplayParityResult(
        run_id=run_id,
        frozen_as_of_date=frozen_as_of_date,
        benchmark_leaves=tuple(leaves),
        archetype_rows=tuple(rows),
        guard_probes=tuple(guard_probes),
        manifest=manifest,
    )


def write_historical_replay_parity(
    result: HistoricalReplayParityResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    marker = claim_mode_output_root(
        root,
        mode=CanonicalRunMode.HISTORICAL_REPLAY,
        run_id=result.run_id,
    )
    paths = {
        "mode_marker": marker,
        "manifest": root / "historical_replay_manifest.json",
        "planner_inputs": root / "historical_replay_planner_inputs.jsonl",
        "evaluator_leaves": root / "historical_replay_evaluator_leaves.jsonl",
        "guard_probes": root / "historical_replay_guard_probes.jsonl",
        "archetype_rows": root / "historical_replay_archetype_parity.jsonl",
        "report": root / "historical_replay_report.md",
    }
    write_json(paths["manifest"], result.manifest)
    write_jsonl(
        paths["planner_inputs"],
        (item.to_planner_record() for item in result.benchmark_leaves),
    )
    write_jsonl(
        paths["evaluator_leaves"],
        (item.to_evaluator_record() for item in result.benchmark_leaves),
    )
    write_jsonl(paths["guard_probes"], (item.to_dict() for item in result.guard_probes))
    write_jsonl(paths["archetype_rows"], (item.to_dict() for item in result.archetype_rows))
    write_text(paths["report"], render_historical_replay_report(result.manifest))
    return paths


def render_historical_replay_report(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        (
            "# Historical Replay Parity",
            "",
            f"- status: {manifest['status']}",
            f"- frozen_as_of_date: {manifest['frozen_as_of_date']}",
            f"- registry coverage: {manifest['registry_covered_archetype_count']}/{manifest['registry_archetype_count']}",
            f"- top1/top3: {manifest['top1_accuracy']}/{manifest['top3_accuracy']}",
            f"- mapping precision: {manifest['mapping_precision']}",
            f"- positive recall: {manifest['positive_recall']}",
            f"- guard accuracy: {manifest['guard_accuracy']}",
            f"- critical guard probes: {manifest['guard_probe_count']} / pass {manifest['guard_probe_pass_rate']}",
            f"- exact source blockers: {manifest['exact_source_blocker_archetype_count']}",
            f"- critical_count_sum: {manifest['critical_count_sum']}",
            "- current_watchlist_eligible: false",
            "- production_runtime_ready: false",
            "",
        )
    )


__all__ = [
    "HISTORICAL_REPLAY_PARITY_SCHEMA_VERSION",
    "FrozenReplaySourceStatus",
    "HistoricalArchetypeParityRow",
    "HistoricalAttemptStatus",
    "HistoricalGuardDecision",
    "HistoricalGuardKind",
    "HistoricalGuardProbe",
    "HistoricalReplayBenchmarkLeaf",
    "HistoricalReplayParityResult",
    "HistoricalSourceResolution",
    "compile_historical_replay_parity",
    "render_historical_replay_report",
    "write_historical_replay_parity",
]
