"""Canonical in-repository frozen replay builder used by the official CLI."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    discover_historical_research_paths,
)
from e2r.research_brain.recipes import compile_evidence_recipe_os
from e2r.research_brain.retrieval import (
    compile_semantic_memory_graph,
    evaluate_balanced_retrieval,
    load_blind_retrieval_benchmark,
)

from .historical_parity import (
    HistoricalGuardDecision,
    HistoricalGuardKind,
    HistoricalGuardProbe,
    HistoricalReplayParityResult,
    compile_historical_replay_parity,
)


CANONICAL_FROZEN_REPLAY_RUNNER_SCHEMA_VERSION = (
    "e2r_canonical_frozen_replay_runner_v1"
)


@dataclass(frozen=True)
class CanonicalFrozenReplayBundle:
    result: HistoricalReplayParityResult
    corpus_manifest: Mapping[str, Any]
    source_manifest: Mapping[str, Any]
    recipe_manifest: Mapping[str, Any]
    memory_manifest: Mapping[str, Any]
    retrieval_manifest: Mapping[str, Any]
    input_artifact_hashes: tuple[Mapping[str, str], ...]
    schema_version: str = CANONICAL_FROZEN_REPLAY_RUNNER_SCHEMA_VERSION

    def __post_init__(self) -> None:
        manifests = (
            self.corpus_manifest,
            self.source_manifest,
            self.recipe_manifest,
            self.memory_manifest,
            self.retrieval_manifest,
        )
        if self.schema_version != CANONICAL_FROZEN_REPLAY_RUNNER_SCHEMA_VERSION:
            raise ValueError("canonical frozen replay bundle schema mismatch")
        if any(int(item.get("critical_count_sum") or 0) for item in manifests):
            raise ValueError("canonical frozen replay upstream critical count is nonzero")
        if self.result.manifest.get("critical_count_sum") != 0:
            raise ValueError("canonical frozen replay result has critical failures")
        if not self.input_artifact_hashes:
            raise ValueError("canonical frozen replay requires corpus artifact hashes")


def compile_canonical_frozen_replay(
    *,
    repo_root: str | Path = ".",
) -> CanonicalFrozenReplayBundle:
    root = Path(repo_root).resolve()
    inputs = discover_historical_research_paths(root)
    corpus = compile_research_intelligence(inputs, repo_root=root)
    source = compile_case_level_source_verification(
        corpus.cases,
        snapshots=(),
        case_source_links=(),
        repo_root=root,
    )
    recipes = compile_evidence_recipe_os(
        corpus.cases,
        source_verifications=source.verifications,
    )
    memory = compile_semantic_memory_graph(
        corpus.cases,
        recipes.recipes,
        source_verifications=source.verifications,
    )
    benchmark = load_blind_retrieval_benchmark()
    frozen_dates = {item.as_of_date for item in benchmark}
    if len(frozen_dates) != 1:
        raise ValueError("canonical replay benchmark must use one frozen as-of date")
    frozen_as_of_date = next(iter(frozen_dates))
    retrieval = evaluate_balanced_retrieval(memory.index, benchmark)
    guard_probes = _canonical_guard_probes(frozen_as_of_date)
    result = compile_historical_replay_parity(
        retrieval_audit=retrieval,
        benchmark_cases=benchmark,
        frozen_as_of_date=frozen_as_of_date,
        guard_probes=guard_probes,
        source_statuses=(),
    )
    return CanonicalFrozenReplayBundle(
        result=result,
        corpus_manifest=corpus.manifest,
        source_manifest=source.manifest,
        recipe_manifest=recipes.manifest,
        memory_manifest=memory.manifest,
        retrieval_manifest=retrieval.manifest,
        input_artifact_hashes=tuple(
            {
                "source_path": item.source_file,
                "sha256": item.sha256,
            }
            for item in corpus.artifacts
        ),
    )


def _canonical_guard_probes(
    frozen_as_of_date: str,
) -> tuple[HistoricalGuardProbe, ...]:
    specs = (
        (
            "HGUARD-CANONICAL-POSITIVE",
            HistoricalGuardKind.POSITIVE,
            HistoricalGuardDecision.ACCEPT_EVALUATOR_HIT,
            "CANONICAL-BLIND-POSITIVE-EVALUATOR-LEAF",
        ),
        (
            "HGUARD-CANONICAL-COUNTER",
            HistoricalGuardKind.COUNTER_GUARD,
            HistoricalGuardDecision.REJECT_SCORE,
            "CANONICAL-BALANCED-COUNTER-GUARD",
        ),
        (
            "HGUARD-CANONICAL-WRONG-SUBJECT",
            HistoricalGuardKind.WRONG_SUBJECT,
            HistoricalGuardDecision.REJECT_SCORE,
            "CANONICAL-WRONG-SUBJECT-GUARD",
        ),
        (
            "HGUARD-CANONICAL-OLD-RISK",
            HistoricalGuardKind.OLD_RISK,
            HistoricalGuardDecision.NO_CURRENT_PENALTY,
            "CANONICAL-EXPIRED-RISK-GUARD",
        ),
        (
            "HGUARD-CANONICAL-SOURCE-MISSING",
            HistoricalGuardKind.SOURCE_MISSING,
            HistoricalGuardDecision.SOURCE_PENDING,
            "CANONICAL-EXACT-SOURCE-BLOCKER",
        ),
    )
    return tuple(
        HistoricalGuardProbe(
            probe_id=probe_id,
            guard_kind=kind.value,
            frozen_as_of_date=frozen_as_of_date,
            evidence_reference_id=reference_id,
            observed_decision=decision.value,
        )
        for probe_id, kind, decision, reference_id in specs
    )


__all__ = [
    "CANONICAL_FROZEN_REPLAY_RUNNER_SCHEMA_VERSION",
    "CanonicalFrozenReplayBundle",
    "compile_canonical_frozen_replay",
]
