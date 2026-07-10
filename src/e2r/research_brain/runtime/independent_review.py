"""Independent A-E reviewers that recompute verdicts from leaf artifacts."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence
from urllib.parse import urlsplit

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.runtime.atomic_score_stage import (
    AtomicScoreType,
    CanonicalStage,
    audit_atomic_stage_decisions,
)
from e2r.research_brain.runtime.run_mode_separation import (
    CanonicalRunMode,
    forbidden_planner_context_paths,
)


INDEPENDENT_REVIEWER_SCHEMA_VERSION = "e2r_independent_reviewer_v1"
INDEPENDENT_REVIEW_SCHEMA_VERSION = "e2r_independent_review_v1"
REVIEWER_IDS = ("A", "B", "C", "D", "E")
_SHA256_CHARS = frozenset("0123456789abcdef")


@dataclass(frozen=True)
class ReviewerVerdict:
    reviewer_id: str
    focus: str
    verdict: str
    critical_counts: Mapping[str, int]
    metrics: Mapping[str, Any]
    leaf_inputs: tuple[Mapping[str, Any], ...]
    result_hash: str
    schema_version: str = INDEPENDENT_REVIEWER_SCHEMA_VERSION
    production_runtime_ready: bool = False

    def __post_init__(self) -> None:
        if self.reviewer_id not in REVIEWER_IDS or not self.focus.strip():
            raise ValueError("independent reviewer identity is invalid")
        if self.verdict not in {"PASS", "FAIL"}:
            raise ValueError("independent reviewer verdict is invalid")
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in self.critical_counts.values()
        ):
            raise ValueError("independent reviewer critical counts are invalid")
        expected = "PASS" if sum(self.critical_counts.values()) == 0 else "FAIL"
        if self.verdict != expected or not _is_sha256(self.result_hash):
            raise ValueError("independent reviewer verdict/hash mismatch")
        paths = tuple(str(item.get("path") or "") for item in self.leaf_inputs)
        if not paths or len(paths) != len(set(paths)):
            raise ValueError("independent reviewer leaf inputs are missing/duplicated")
        if self.production_runtime_ready:
            raise ValueError("individual reviewer cannot declare runtime ready")

    @property
    def critical_count_sum(self) -> int:
        return sum(self.critical_counts.values())

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "critical_counts": dict(self.critical_counts),
            "metrics": dict(self.metrics),
            "leaf_inputs": [dict(item) for item in self.leaf_inputs],
            "critical_count_sum": self.critical_count_sum,
        }


@dataclass(frozen=True)
class IndependentReviewResult:
    reviewers: tuple[ReviewerVerdict, ...]
    status: str
    result_hash: str
    schema_version: str = INDEPENDENT_REVIEW_SCHEMA_VERSION
    production_runtime_ready: bool = False

    def __post_init__(self) -> None:
        if tuple(item.reviewer_id for item in self.reviewers) != REVIEWER_IDS:
            raise ValueError("independent review requires ordered reviewers A-E")
        expected = (
            "INDEPENDENT_E2R_REVIEW_PASS"
            if self.critical_count_sum == 0
            else "INDEPENDENT_E2R_REVIEW_FAIL"
        )
        if self.status != expected or not _is_sha256(self.result_hash):
            raise ValueError("independent review status/hash mismatch")
        if self.production_runtime_ready:
            raise ValueError("review result alone cannot declare runtime ready")

    @property
    def critical_count_sum(self) -> int:
        return sum(item.critical_count_sum for item in self.reviewers)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "status": self.status,
            "reviewer_ids": list(REVIEWER_IDS),
            "reviewer_verdicts": {
                item.reviewer_id: item.verdict for item in self.reviewers
            },
            "reviewer_critical_counts": {
                item.reviewer_id: item.critical_count_sum
                for item in self.reviewers
            },
            "critical_count_sum": self.critical_count_sum,
            "result_hash": self.result_hash,
            "production_runtime_ready": False,
        }


def run_independent_review(
    *,
    compile_root: str | Path,
    replay_root: str | Path,
    current_root: str | Path,
    repo_root: str | Path = ".",
    funnel_root: str | Path | None = None,
    require_live_current: bool = True,
) -> IndependentReviewResult:
    # Each function opens its own leaves and computes its own counters. No
    # compile/replay/current report counter is passed between reviewers.
    reviewers = (
        review_corpus_fidelity(compile_root=compile_root, repo_root=repo_root),
        review_recipe_retrieval(compile_root=compile_root),
        review_source_claim_realness(
            compile_root=compile_root,
            current_root=current_root,
            funnel_root=funnel_root,
            require_live_current=require_live_current,
        ),
        review_score_stage_integrity(current_root=current_root),
        review_historical_current_separation(
            replay_root=replay_root,
            current_root=current_root,
        ),
    )
    payload = [item.to_dict() for item in reviewers]
    critical = sum(item.critical_count_sum for item in reviewers)
    return IndependentReviewResult(
        reviewers=reviewers,
        status=(
            "INDEPENDENT_E2R_REVIEW_PASS"
            if critical == 0
            else "INDEPENDENT_E2R_REVIEW_FAIL"
        ),
        result_hash=stable_hash(payload),
    )


def review_corpus_fidelity(
    *,
    compile_root: str | Path,
    repo_root: str | Path = ".",
) -> ReviewerVerdict:
    root = Path(compile_root)
    paths = (
        root / "corpus" / "historical_artifacts.jsonl",
        root / "corpus" / "structured_rows.jsonl",
        root / "corpus" / "historical_cases.jsonl",
        root / "corpus" / "historical_outcomes.jsonl",
    )
    artifacts, rows, cases, outcomes = (_read_jsonl(path) for path in paths)
    artifact_ids = tuple(str(item.get("artifact_id") or "") for item in artifacts)
    row_ids = tuple(str(item.get("row_id") or "") for item in rows)
    case_ids = tuple(str(item.get("case_id") or "") for item in cases)
    outcome_ids = tuple(str(item.get("outcome_id") or "") for item in outcomes)
    artifact_by_id = _index(artifacts, "artifact_id")
    row_by_id = _index(rows, "row_id")
    structured_counts = Counter(
        str(item.get("artifact_id") or "")
        for item in rows
        if item.get("structured") is True
    )
    source_hash_mismatch = 0
    for artifact in artifacts:
        source = Path(str(artifact.get("source_file") or ""))
        source = source if source.is_absolute() else Path(repo_root) / source
        if (
            not source.is_file()
            or _file_sha256(source) != artifact.get("sha256")
        ):
            source_hash_mismatch += 1
    missing_case_row = 0
    cross_artifact_case_row = 0
    handoff_as_case = 0
    for case in cases:
        for row_id in case.get("source_row_ids") or ():
            row = row_by_id.get(str(row_id))
            if row is None:
                missing_case_row += 1
            elif row.get("artifact_id") != case.get("artifact_id"):
                cross_artifact_case_row += 1
            elif row.get("handoff_metadata") is True:
                handoff_as_case += 1
    critical = {
        "required_leaf_missing": sum(not path.is_file() for path in paths),
        "required_leaf_empty": sum(
            not values for values in (artifacts, rows, cases, outcomes)
        ),
        "duplicate_artifact_id": _duplicate_count(artifact_ids),
        "duplicate_row_id": _duplicate_count(row_ids),
        "duplicate_case_id": _duplicate_count(case_ids),
        "duplicate_outcome_id": _duplicate_count(outcome_ids),
        "artifact_source_hash_mismatch": source_hash_mismatch,
        "row_outside_artifact": sum(
            str(item.get("artifact_id") or "") not in artifact_by_id
            for item in rows
        ),
        "structured_row_count_mismatch": sum(
            int(item.get("structured_row_count") or 0)
            != structured_counts.get(str(item.get("artifact_id") or ""), 0)
            for item in artifacts
        ),
        "case_outside_artifact": sum(
            str(item.get("artifact_id") or "") not in artifact_by_id
            for item in cases
        ),
        "case_source_row_missing": missing_case_row,
        "case_source_row_cross_artifact": cross_artifact_case_row,
        "handoff_metadata_parsed_as_case": handoff_as_case,
        "case_company_or_symbol_loss": sum(
            not str(item.get("company_name") or "").strip()
            or not str(item.get("symbol") or "").strip()
            for item in cases
        ),
        "case_runtime_score_leak": sum(
            item.get("runtime_score_eligible") is not False for item in cases
        ),
        "outcome_runtime_or_prompt_leak": sum(
            item.get("evaluator_only") is not True
            or item.get("runtime_prompt_allowed") is not False
            or item.get("runtime_score_eligible") is not False
            for item in outcomes
        ),
    }
    metrics = {
        "artifact_count": len(artifacts),
        "structured_row_count": len(rows),
        "historical_case_count": len(cases),
        "historical_outcome_count": len(outcomes),
    }
    return _verdict("A", "Corpus Fidelity", critical, metrics, paths)


def review_recipe_retrieval(
    *,
    compile_root: str | Path,
) -> ReviewerVerdict:
    root = Path(compile_root)
    paths = (
        root / "recipes" / "evidence_recipes.jsonl",
        root / "recipes" / "unsupported_evidence_recipes.jsonl",
        root / "retrieval" / "research_memory_nodes.jsonl",
        root / "retrieval" / "research_memory_edges.jsonl",
        root / "retrieval" / "semantic_memory_index.jsonl",
        root / "retrieval" / "blind_retrieval_results.jsonl",
    )
    recipes, unsupported, nodes, edges, index, retrieval = (
        _read_jsonl(path) for path in paths
    )
    recipe_ids = tuple(str(item.get("recipe_id") or "") for item in recipes)
    unsupported_ids = tuple(
        str(item.get("unsupported_id") or "") for item in unsupported
    )
    node_ids = tuple(str(item.get("node_id") or "") for item in nodes)
    edge_ids = tuple(str(item.get("edge_id") or "") for item in edges)
    index_ids = tuple(str(item.get("node_id") or "") for item in index)
    benchmark_ids = tuple(
        str(item.get("benchmark_id") or "") for item in retrieval
    )
    node_id_set = set(node_ids)
    recipe_id_set = set(recipe_ids)
    recipe_pairs = {
        (str(item.get("archetype_id") or ""), str(item.get("primitive_id") or ""))
        for item in recipes
    }
    unsupported_pairs = {
        (str(item.get("archetype_id") or ""), str(item.get("primitive_id") or ""))
        for item in unsupported
    }
    archetype_rows = tuple(
        item for item in retrieval if item.get("archetype_retrieval_expected") is True
    )
    recipe_rows = tuple(
        item for item in retrieval if item.get("required_recipe_expected") is True
    )
    top3_rate = _rate(archetype_rows, lambda item: item.get("top3_archetype_hit") is True)
    recipe_rate = _rate(recipe_rows, lambda item: item.get("required_recipe_hit") is True)
    pair_rate = _rate(recipe_rows, lambda item: item.get("positive_guard_pair") is True)
    critical = {
        "required_leaf_missing": sum(not path.is_file() for path in paths),
        "required_leaf_empty": sum(
            not values
            for values in (recipes, unsupported, nodes, edges, index, retrieval)
        ),
        "duplicate_recipe_id": _duplicate_count(recipe_ids),
        "duplicate_unsupported_id": _duplicate_count(unsupported_ids),
        "recipe_pair_overlap": len(recipe_pairs & unsupported_pairs),
        "invalid_executable_recipe": sum(
            item.get("executable") is not True
            or item.get("runtime_score_eligible") is not False
            or bool(item.get("literal_queries"))
            or not item.get("accepted_claim_predicates")
            or not item.get("counterexamples")
            or not item.get("wrong_subject_examples")
            or not item.get("source_success_examples")
            or not item.get("source_failure_examples")
            or not item.get("stop_conditions")
            for item in recipes
        ),
        "invalid_unsupported_boundary": sum(
            item.get("planning_only") is not True
            or item.get("runtime_route_available") is not False
            or not str(item.get("reason_detail") or "").strip()
            for item in unsupported
        ),
        "duplicate_memory_node_id": _duplicate_count(node_ids),
        "duplicate_memory_edge_id": _duplicate_count(edge_ids),
        "broken_memory_edge": sum(
            str(item.get("source_node_id") or "") not in node_id_set
            or str(item.get("target_node_id") or "") not in node_id_set
            for item in edges
        ),
        "memory_node_runtime_score_leak": sum(
            item.get("runtime_score_eligible") is not False for item in nodes
        ),
        "duplicate_index_node": _duplicate_count(index_ids),
        "index_outside_graph": sum(item not in node_id_set for item in index_ids),
        "retrieval_unknown_recipe": sum(
            str(recipe_id) not in recipe_id_set
            for item in retrieval
            for recipe_id in item.get("direct_recipe_ids") or ()
        ),
        "duplicate_benchmark_id": _duplicate_count(benchmark_ids),
        "retrieval_future_leakage": sum(
            max(0, _int(item.get("future_leakage_count"))) for item in retrieval
        ),
        "retrieval_missing_balanced_role": sum(
            bool(item.get("missing_roles")) for item in recipe_rows
        ),
        "retrieval_input_order_bias": sum(
            item.get("input_order_invariant") is not True for item in retrieval
        ),
        "retrieval_popularity_bias": sum(
            item.get("popularity_invariant") is not True for item in retrieval
        ),
        "unjustified_benchmark_exclusion": sum(
            (
                item.get("archetype_retrieval_expected") is not True
                or item.get("required_recipe_expected") is not True
            )
            and not str(item.get("exclusion_reason") or "").strip()
            for item in retrieval
        ),
        "top3_below_0_95": int(top3_rate < 0.95),
        "recipe_hit_below_0_95": int(recipe_rate < 0.95),
        "positive_guard_pair_below_0_90": int(pair_rate < 0.90),
    }
    metrics = {
        "executable_recipe_count": len(recipes),
        "explicit_unsupported_count": len(unsupported),
        "memory_node_count": len(nodes),
        "memory_edge_count": len(edges),
        "benchmark_count": len(retrieval),
        "top3_rate": top3_rate,
        "required_recipe_hit_rate": recipe_rate,
        "positive_guard_pair_rate": pair_rate,
    }
    return _verdict("B", "Recipe/Retrieval", critical, metrics, paths)


def review_source_claim_realness(
    *,
    compile_root: str | Path,
    current_root: str | Path,
    funnel_root: str | Path | None = None,
    require_live_current: bool = True,
) -> ReviewerVerdict:
    compile_path = Path(compile_root) / "source_verification" / "source_verifications.jsonl"
    current = Path(current_root)
    current_paths = (
        current / "current_daily_claim_provenance.jsonl",
        current / "current_daily_source_tasks.jsonl",
        current / "current_daily_deep_executions.jsonl",
        current / "current_daily_atomic_decisions.jsonl",
    )
    paths = (compile_path, *current_paths)
    verifications = _read_jsonl(compile_path)
    provenance, tasks, executions, decisions = (
        _read_jsonl(path) for path in current_paths
    )
    provenance_by_claim = _index(provenance, "claim_id")
    effective_claim_ids = {
        str(claim_id)
        for decision in decisions
        for claim_id in (
            *(decision.get("accepted_claim_ids") or ()),
            *(decision.get("hard_break_claim_ids") or ()),
        )
    }
    hard_break_claim_ids = {
        str(claim_id)
        for decision in decisions
        for claim_id in decision.get("hard_break_claim_ids") or ()
    }
    score_claims = {
        str(claim.get("claim_id") or ""): claim
        for decision in decisions
        for claim in _rows(decision.get("claims"))
        if str(claim.get("claim_id") or "") in effective_claim_ids
    }
    provenance_mismatch = 0
    for claim_id, claim in score_claims.items():
        item = provenance_by_claim.get(claim_id)
        if item is None:
            provenance_mismatch += 1
            continue
        published_date = _date_or_none(str(item.get("published_date") or ""))
        available_date = _date_or_none(str(item.get("available_date") or ""))
        claim_observed_date = _date_or_none(
            str(claim.get("observed_date") or "")
        )
        if (
            str(item.get("target_id") or "") != str(claim.get("target_id") or "")
            or tuple(item.get("source_ids") or ()) != tuple(claim.get("source_ids") or ())
            or tuple(item.get("anchor_ids") or ()) != tuple(claim.get("anchor_ids") or ())
            or tuple(item.get("mapping_ids") or ()) != tuple(claim.get("mapping_ids") or ())
            or item.get("fetched") is not True
            or item.get("anchor_verified") is not True
            or item.get("source_proxy_only") is not False
            or item.get("directness") != "DIRECT"
            or item.get("temporal_status") != "CURRENT"
            or (
                claim_id in hard_break_claim_ids
                and (
                    item.get("decision_use") != "HARD_BREAK"
                    or item.get("mapping_status") != "NOT_REQUIRED_HARD_BREAK"
                )
            )
            or (
                claim_id not in hard_break_claim_ids
                and (
                    item.get("decision_use") != "SCORE"
                    or item.get("mapping_status") != "ACCEPTED"
                )
            )
            or item.get("extraction_provider_kind") != "CODEX"
            or item.get("mapping_provider_kind") != "CODEX"
            or item.get("test_only") is not False
            or not _is_live_source_url(str(item.get("source_url") or ""))
            or published_date is None
            or available_date is None
            or claim_observed_date is None
            or available_date < published_date
            or available_date > claim_observed_date
            or not _is_sha256(str(item.get("content_sha256") or ""))
            or hashlib.sha256(
                str(item.get("document_text") or "").encode("utf-8")
            ).hexdigest()
            != item.get("content_sha256")
            or not str(item.get("exact_quote") or "").strip()
            or str(item.get("exact_quote") or "")
            not in str(item.get("document_text") or "")
        ):
            provenance_mismatch += 1
    ready_rows = tuple(
        item for item in verifications if item.get("historical_replay_ready") is True
    )
    blocked_rows = tuple(
        item for item in verifications if item.get("historical_replay_ready") is not True
    )
    critical = {
        "historical_source_leaf_missing": int(not compile_path.is_file()),
        "historical_source_leaf_empty": int(not verifications),
        "historical_ready_contract_failure": sum(
            item.get("a2_historical_evidence_eligible") is not True
            or item.get("evaluator_only") is not True
            or item.get("current_score_eligible") is not False
            or not item.get("content_sha256")
            or not item.get("published_date")
            or not item.get("anchor_ids")
            or not item.get("exact_quotes")
            or item.get("target_directness") != "DIRECT"
            or item.get("summary_consistent") is not True
            or not all(bool(value) for value in dict(item.get("checks") or {}).values())
            for item in ready_rows
        ),
        "historical_blocker_missing_reason": sum(
            not str(item.get("blocker_code") or "").strip()
            or not str(item.get("blocker_detail") or "").strip()
            or item.get("current_score_eligible") is not False
            for item in blocked_rows
        ),
        "current_required_leaf_missing": (
            sum(not path.is_file() for path in current_paths)
            if require_live_current
            else 0
        ),
        "current_score_claim_without_real_provenance": (
            provenance_mismatch if require_live_current else 0
        ),
        "duplicate_current_provenance_claim": (
            _duplicate_count(
                tuple(str(item.get("claim_id") or "") for item in provenance)
            )
            if require_live_current
            else 0
        ),
        "unbounded_source_task": sum(
            _int(item.get("max_queries")) <= 0
            or _int(item.get("max_candidates")) <= 0
            or _int(item.get("max_fetches")) <= 0
            or item.get("stop_condition") != "stop_on_resolution"
            for item in tasks
        ),
        "general_web_without_official_gap": sum(
            item.get("allows_general_web") is True
            and (
                item.get("official_first_attempted") is not True
                or not item.get("official_gap_reasons")
            )
            for item in tasks
        ),
        "production_fixture_provider": (
            sum(
                item.get("provider_kind") == "FIXTURE"
                for item in executions
            )
            if require_live_current
            else 0
        ),
        "live_current_has_no_source_fetch": (
            int(not executions or not any(_int(item.get("fetches")) > 0 for item in executions))
            if require_live_current
            else 0
        ),
    }
    funnel_metrics: dict[str, int] = {}
    if funnel_root is not None:
        funnel_path = Path(funnel_root) / "conversion_funnel_stage_leaves.jsonl"
        paths = (*paths, funnel_path)
        leaves = _read_jsonl(funnel_path)
        accepted_direct = sum(
            item.get("stage") == "CLAIM" and item.get("status") == "ACCEPTED_DIRECT"
            for item in leaves
        )
        fetched = sum(item.get("stage") == "FETCHED_DOCUMENT" for item in leaves)
        full = sum(
            item.get("stage") == "TERMINAL" and item.get("status") == "FULL_THESIS"
            for item in leaves
        )
        critical["funnel_leaf_missing"] = int(require_live_current and not funnel_path.is_file())
        critical["live_funnel_without_direct_claim"] = int(
            require_live_current and accepted_direct == 0
        )
        critical["live_funnel_without_fetched_document"] = int(
            require_live_current and fetched == 0
        )
        funnel_metrics = {
            "funnel_accepted_direct_claim_count": accepted_direct,
            "funnel_fetched_document_count": fetched,
            "funnel_full_thesis_count": full,
        }
    elif require_live_current:
        critical["funnel_leaf_missing"] = 1
    metrics = {
        "historical_verification_count": len(verifications),
        "historical_replay_ready_count": len(ready_rows),
        "historical_exact_blocker_count": len(blocked_rows),
        "current_score_claim_count": len(score_claims),
        "current_provenance_count": len(provenance),
        "current_execution_count": len(executions),
        **funnel_metrics,
    }
    return _verdict("C", "Source/Claim Realness", critical, metrics, paths)


def review_score_stage_integrity(
    *,
    current_root: str | Path,
) -> ReviewerVerdict:
    root = Path(current_root)
    paths = (
        root / "current_daily_atomic_decisions.jsonl",
        root / "current_daily_census_stage_statuses.jsonl",
        root / "current_daily_watchlist.jsonl",
    )
    decisions, statuses, watchlist = (_read_jsonl(path) for path in paths)
    atomic = audit_atomic_stage_decisions(decisions)
    decision_by_id = _index(decisions, "decision_id")
    status_by_target = _index(statuses, "target_id")
    projection_mismatch = 0
    for status in statuses:
        decision_id = str(status.get("atomic_decision_id") or "")
        decision = decision_by_id.get(decision_id)
        if decision_id:
            if decision is None or any(
                status.get(key) != decision.get(key)
                for key in (
                    "target_id",
                    "as_of_date",
                    "canonical_stage",
                    "score_type",
                    "score_value",
                    "raw_reference_score",
                    "score_valid",
                    "score_finalization_allowed",
                )
            ):
                projection_mismatch += 1
        elif (
            status.get("score_type") != AtomicScoreType.NO_SCORE.value
            or status.get("score_value") is not None
            or status.get("canonical_stage") not in {"0", "1"}
        ):
            projection_mismatch += 1
    canonical_stages = {item.value for item in CanonicalStage}
    watchlist_target_ids = tuple(
        str(item.get("target_id") or "") for item in watchlist
    )
    expected_watchlist_targets = {
        str(item.get("target_id") or "")
        for item in statuses
        if (
            item.get("trigger_signal_ids")
            or item.get("accepted_claim_ids")
            or item.get("terminal_status") != "BASELINE_ONLY"
        )
    }
    watchlist_projection_mismatch = 0
    for item in watchlist:
        target_id = str(item.get("target_id") or "")
        status = status_by_target.get(target_id)
        if status is None:
            watchlist_projection_mismatch += 1
            continue
        expected_gap_ids = tuple(
            dict.fromkeys(
                (
                    *(status.get("material_gap_ids") or ()),
                    *(status.get("provider_gaps") or ()),
                    *(status.get("source_gaps") or ()),
                )
            )
        )
        expected_watchlist_id = "DWL-" + stable_hash(
            {
                "target_id": target_id,
                "as_of_date": status.get("as_of_date"),
                "status_id": status.get("status_id"),
                "next_action": status.get("next_action"),
            }
        )[:24]
        expected_projection = {
            "watchlist_id": expected_watchlist_id,
            "target_id": target_id,
            "target_name": status.get("target_name"),
            "as_of_date": status.get("as_of_date"),
            "canonical_stage": status.get("canonical_stage"),
            "terminal_status": status.get("terminal_status"),
            "score_type": status.get("score_type"),
            "score_value": status.get("score_value"),
            "raw_reference_score": status.get("raw_reference_score"),
            "confidence": status.get("confidence"),
            "claim_ids": tuple(status.get("accepted_claim_ids") or ()),
            "missing_conditions": tuple(status.get("missing_conditions") or ()),
            "gap_ids": expected_gap_ids,
            "trigger_families": tuple(status.get("trigger_families") or ()),
            "next_action": status.get("next_action"),
            "monitoring_label": _expected_monitoring_label(status),
        }
        if any(
            (
                tuple(item.get(key) or ())
                if key
                in {
                    "claim_ids",
                    "missing_conditions",
                    "gap_ids",
                    "trigger_families",
                }
                else item.get(key)
            )
            != expected
            for key, expected in expected_projection.items()
        ):
            watchlist_projection_mismatch += 1
    critical = {
        "required_leaf_missing": sum(not path.is_file() for path in paths),
        "status_leaf_empty": int(not statuses),
        "atomic_decision_integrity_failure": int(atomic["critical_count_sum"]),
        "duplicate_atomic_decision_id": _duplicate_count(
            tuple(str(item.get("decision_id") or "") for item in decisions)
        ),
        "duplicate_status_target": _duplicate_count(
            tuple(str(item.get("target_id") or "") for item in statuses)
        ),
        "status_decision_projection_mismatch": projection_mismatch,
        "noncanonical_stage": sum(
            str(item.get("canonical_stage") or "") not in canonical_stages
            for item in (*decisions, *statuses, *watchlist)
        ),
        "scoring_threshold_mutation": sum(
            dict(item.get("stage_config") or {})
            != {
                "stage1_threshold": 40.0,
                "stage2_threshold": 65.0,
                "yellow_threshold": 80.0,
                "green_threshold": 90.0,
                "config_version": "canonical_stage_thresholds_v1",
            }
            for item in decisions
        ),
        "pending_finalized_score": sum(
            str(item.get("terminal_status") or "").endswith("PENDING")
            and (
                item.get("score_value") is not None
                or item.get("score_finalization_allowed") is True
            )
            for item in statuses
        ),
        "duplicate_watchlist_target": _duplicate_count(watchlist_target_ids),
        "watchlist_coverage_gap": len(
            expected_watchlist_targets - set(watchlist_target_ids)
        ),
        "watchlist_outside_expected_status": len(
            set(watchlist_target_ids) - expected_watchlist_targets
        ),
        "watchlist_projection_mismatch": watchlist_projection_mismatch,
        "investment_recommendation_language": sum(
            any(
                term in (
                    str(item.get("next_action") or "")
                    + " "
                    + str(item.get("monitoring_label") or "")
                ).casefold()
                for term in ("매수", "매도", "비중 확대", "비중 축소", "buy", "sell")
            )
            for item in watchlist
        ),
    }
    metrics = {
        "atomic_decision_count": len(decisions),
        "status_count": len(statuses),
        "watchlist_count": len(watchlist),
        "full_score_count": sum(
            item.get("score_type") == AtomicScoreType.FULL_E2R_100.value
            for item in decisions
        ),
    }
    return _verdict("D", "Score/Stage Integrity", critical, metrics, paths)


def review_historical_current_separation(
    *,
    replay_root: str | Path,
    current_root: str | Path,
) -> ReviewerVerdict:
    replay = Path(replay_root)
    current = Path(current_root)
    paths = (
        replay / "e2r_run_mode.json",
        replay / "historical_replay_planner_inputs.jsonl",
        replay / "historical_replay_evaluator_leaves.jsonl",
        replay / "historical_replay_guard_probes.jsonl",
        replay / "historical_replay_archetype_parity.jsonl",
        current / "e2r_run_mode.json",
        current / "current_daily_universe.jsonl",
        current / "current_daily_source_timelines.jsonl",
        current / "current_daily_depth_decisions.jsonl",
        current / "current_daily_census_stage_statuses.jsonl",
    )
    replay_marker = _read_json(paths[0])
    planner = _read_jsonl(paths[1])
    evaluator = _read_jsonl(paths[2])
    guards = _read_jsonl(paths[3])
    archetypes = _read_jsonl(paths[4])
    current_marker = _read_json(paths[5])
    universe = _read_jsonl(paths[6])
    timelines = _read_jsonl(paths[7])
    depths = _read_jsonl(paths[8])
    statuses = _read_jsonl(paths[9])
    planner_by_id = _index(planner, "benchmark_id")
    evaluator_by_id = _index(evaluator, "benchmark_id")
    current_dates = {
        str(item.get("as_of_date") or "")
        for item in (*universe, *timelines, *statuses)
    }
    current_as_of = next(iter(current_dates), "") if len(current_dates) == 1 else ""
    as_of = _date_or_none(current_as_of)
    timeline_events = tuple(
        event for timeline in timelines for event in _rows(timeline.get("events"))
    )
    critical = {
        "required_leaf_missing": sum(not path.is_file() for path in paths),
        "historical_leaf_empty": sum(
            not values for values in (planner, evaluator, guards, archetypes)
        ),
        "current_leaf_empty": sum(
            not values for values in (universe, timelines, depths, statuses)
        ),
        "historical_mode_marker_mismatch": int(
            replay_marker.get("mode") != CanonicalRunMode.HISTORICAL_REPLAY.value
            or replay_marker.get("output_namespace") != "historical_replay"
        ),
        "current_mode_marker_mismatch": int(
            current_marker.get("mode") != CanonicalRunMode.CURRENT_OPERATION.value
            or current_marker.get("output_namespace") != "current_operation"
        ),
        "shared_run_identity": int(
            bool(replay_marker.get("run_id"))
            and replay_marker.get("run_id") == current_marker.get("run_id")
        ),
        "planner_evaluator_identity_mismatch": len(
            set(planner_by_id) ^ set(evaluator_by_id)
        ),
        "planner_input_hash_mismatch": sum(
            stable_hash(item.get("planner_input"))
            != item.get("planner_input_hash")
            for item in planner
        ),
        "historical_outcome_in_planner": sum(
            len(forbidden_planner_context_paths(item.get("planner_input")))
            for item in planner
        ),
        "historical_evaluator_current_contamination": sum(
            item.get("future_leakage_count", 0) != 0
            or item.get("source_proxy_score_credit", 0) != 0
            or item.get("current_watchlist_eligible") is not False
            for item in evaluator
        ),
        "historical_guard_current_contamination": sum(
            item.get("evaluator_only") is not True
            or item.get("current_score_credit", 0) != 0
            or item.get("current_watchlist_eligible") is not False
            for item in guards
        ),
        "historical_archetype_current_contamination": sum(
            item.get("current_watchlist_eligible") is not False
            for item in archetypes
        ),
        "current_as_of_inconsistent": int(not current_as_of or as_of is None),
        "future_current_timeline_event": sum(
            as_of is None
            or _date_or_none(str(item.get("event_date") or "")) is None
            or _date_or_none(str(item.get("event_date") or "")) > as_of
            for item in timeline_events
        ),
        "current_trigger_used_as_score": sum(
            item.get("role") == "TRIGGER"
            and item.get("score_evidence_eligible") is True
            for item in timeline_events
        ),
        "current_historical_or_evaluator_field": sum(
            _contains_forbidden_current_context(item)
            for item in (*universe, *timelines, *depths, *statuses)
        ),
        "forced_current_archetype_materialization": sum(
            "quota" in json.dumps(item, ensure_ascii=False).casefold()
            or "forced_archetype" in json.dumps(item, ensure_ascii=False).casefold()
            for item in depths
        ),
        "canonical_archetype_replay_coverage_gap": len(
            set(CANONICAL_ARCHETYPE_IDS)
            - {str(item.get("archetype_id") or "") for item in archetypes}
        ),
    }
    metrics = {
        "historical_planner_leaf_count": len(planner),
        "historical_evaluator_leaf_count": len(evaluator),
        "historical_archetype_row_count": len(archetypes),
        "current_universe_count": len(universe),
        "current_status_count": len(statuses),
        "current_as_of_date": current_as_of,
    }
    return _verdict("E", "Historical/Current Separation", critical, metrics, paths)


def write_independent_review(
    result: IndependentReviewResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths: dict[str, Path] = {}
    for reviewer in result.reviewers:
        path = root / f"reviewer_{reviewer.reviewer_id}_verdict.json"
        write_json(path, reviewer.to_dict())
        paths[f"reviewer_{reviewer.reviewer_id.lower()}"] = path
    manifest_path = root / "independent_review_manifest.json"
    write_json(manifest_path, result.to_dict())
    paths["manifest"] = manifest_path
    return paths


def _verdict(
    reviewer_id: str,
    focus: str,
    critical: Mapping[str, int],
    metrics: Mapping[str, Any],
    paths: Sequence[Path],
) -> ReviewerVerdict:
    normalized = {key: max(0, _int(value)) for key, value in critical.items()}
    inputs = tuple(_leaf_descriptor(path) for path in paths)
    payload = {
        "reviewer_id": reviewer_id,
        "focus": focus,
        "critical_counts": normalized,
        "metrics": dict(metrics),
        "leaf_inputs": list(inputs),
    }
    return ReviewerVerdict(
        reviewer_id=reviewer_id,
        focus=focus,
        verdict="PASS" if sum(normalized.values()) == 0 else "FAIL",
        critical_counts=normalized,
        metrics=dict(metrics),
        leaf_inputs=inputs,
        result_hash=stable_hash(payload),
    )


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    rows: list[Mapping[str, Any]] = []
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            value = json.loads(line)
            if isinstance(value, Mapping):
                rows.append(dict(value))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return ()
    return tuple(rows)


def _read_json(path: Path) -> Mapping[str, Any]:
    if not path.is_file():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {}
    return dict(value) if isinstance(value, Mapping) else {}


def _leaf_descriptor(path: Path) -> Mapping[str, Any]:
    exists = path.is_file()
    return {
        "path": str(path.resolve()),
        "exists": exists,
        "sha256": _file_sha256(path) if exists else None,
        "byte_count": path.stat().st_size if exists else 0,
    }


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _index(
    rows: Sequence[Mapping[str, Any]],
    key: str,
) -> dict[str, Mapping[str, Any]]:
    return {
        str(item.get(key) or ""): item
        for item in rows
        if str(item.get(key) or "").strip()
    }


def _rows(value: Any) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(item for item in value if isinstance(item, Mapping))


def _duplicate_count(values: Sequence[str]) -> int:
    return len(values) - len(set(values))


def _int(value: Any) -> int:
    return value if isinstance(value, int) and not isinstance(value, bool) else 0


def _rate(
    rows: Sequence[Mapping[str, Any]],
    predicate: Callable[[Mapping[str, Any]], bool],
) -> float:
    return round(sum(predicate(item) for item in rows) / len(rows), 6) if rows else 0.0


def _date_or_none(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _is_sha256(value: str) -> bool:
    return len(value) == 64 and set(value).issubset(_SHA256_CHARS)


def _is_live_source_url(value: str) -> bool:
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    host = (parsed.hostname or "").casefold().rstrip(".")
    return bool(
        parsed.scheme in {"http", "https"}
        and host
        and host
        not in {
            "example.com",
            "example.net",
            "example.org",
            "example.test",
            "localhost",
        }
        and not host.endswith(
            (
                ".example.com",
                ".example.net",
                ".example.org",
                ".test",
                ".invalid",
                ".localhost",
            )
        )
    )


def _expected_monitoring_label(status: Mapping[str, Any]) -> str:
    if status.get("canonical_stage") == "4C":
        return "Stage 4C 논리 훼손 감시"
    if status.get("canonical_stage") == "3-Red":
        return "Stage 3-Red 현재 counter claim 감시"
    if status.get("terminal_status") == "FULL_THESIS":
        return "다음 실적과 수주잔고 확인"
    if status.get("terminal_status") in {
        "SOURCE_PENDING",
        "PROVIDER_PENDING",
        "BUDGET_PENDING",
    }:
        return "근거 보완 후 Stage 재검증"
    return "daily trigger 변화 관찰"


def _contains_forbidden_current_context(payload: Mapping[str, Any]) -> int:
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True).casefold()
    return int(
        any(
            token in text
            for token in (
                "expected_archetype",
                "expected_stage",
                "expected_outcome",
                "future_outcome",
                "historical_replay\": true",
            )
        )
    )


__all__ = [
    "INDEPENDENT_REVIEWER_SCHEMA_VERSION",
    "INDEPENDENT_REVIEW_SCHEMA_VERSION",
    "REVIEWER_IDS",
    "IndependentReviewResult",
    "ReviewerVerdict",
    "review_corpus_fidelity",
    "review_historical_current_separation",
    "review_recipe_retrieval",
    "review_score_stage_integrity",
    "review_source_claim_realness",
    "run_independent_review",
    "write_independent_review",
]
