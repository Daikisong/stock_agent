"""Phase 93 full-thesis Gold research benchmark.

The Gold lane is a private, post-run evaluation corpus.  Production may not
see its queries, URLs, facts, component memos, or any expected score/stage.
This module validates the evaluation corpus and, only after an independently
completed production run, computes the four recall gates required by the v5
master goal.

Target names and symbols live in the benchmark data, not in this generic
validator.  The validator therefore cannot become a target-specific query or
scoring branch.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.research_quality import BlindResearchQualityBenchmark


PHASE93_SCHEMA_VERSION = "e2r_v5_full_thesis_gold_research_recall_v1"
PHASE93_MANIFEST_SCHEMA_VERSION = "e2r_v5_full_thesis_gold_manifest_v1"
PHASE93_READY = "V5_PHASE93_FULL_THESIS_GOLD_BENCHMARK_READY"
PHASE93_POST_RUN_PASS = "V5_FULL_THESIS_GOLD_POST_RUN_RECALL_PASS"
PHASE93_POST_RUN_FAIL = "V5_FULL_THESIS_GOLD_POST_RUN_RECALL_FAIL"
PHASE93_POST_RUN_PENDING = "PENDING_PHASE94_CLEAN_PRODUCTION_RERUN"
PHASE93_GOLD_ROOT = (
    "data/benchmark_labels/e2r_v5_full_thesis_gold_2026-07-12"
)
PHASE93_AUDIT_PATH = "docs/operational/e2r_v5_gold_research_recall.json"
PHASE94_TRACKED_POST_RUN_ROOT = (
    "docs/operational/e2r_v5_phase94_post_run"
)
PHASE94_POST_RUN_AUDIT_FILE = "post_run_gold_recall_audit.json"
PHASE94_PRODUCTION_LANE_FILE = "production_lane_manifest.json"
PHASE93_BASELINE_PRODUCTION_ROOT = (
    "output/evidence_to_score_v2/blind_2026-07-11/production"
)

PHASE93_OUTPUT_FILES = {
    "manifest": "manifest.json",
    "pre_gold_production_isolation": "pre_gold_production_isolation.json",
    "query_ledger": "gold_query_ledger.jsonl",
    "source_map": "gold_source_map.jsonl",
    "material_facts": "gold_material_facts.jsonl",
    "counterfacts": "gold_counterfacts.jsonl",
    "component_memos": "gold_component_memos.jsonl",
    "question_coverage": "gold_question_coverage.json",
}

PHASE93_SOURCE_FAMILIES = (
    "DART",
    "ISSUER_IR",
    "EARNINGS_RELEASE",
    "CONFERENCE_CALL_MATERIAL",
    "NEWSROOM",
    "CUSTOMER_OFFICIAL",
    "TRUSTED_MEDIA",
    "NAVER_WEB_DISCOVERY",
    "PUBLIC_REPORT",
    "STRUCTURED_CONSENSUS_VALUATION",
)

PHASE93_RECALL_THRESHOLDS: Mapping[str, float] = {
    "critical_material_fact_recall_min": 1.0,
    "counter_supersession_recall_min": 1.0,
    "all_material_fact_recall_min": 0.95,
    "component_research_topic_coverage_min": 1.0,
}
_POST_RUN_METRIC_NAMES = tuple(
    name.removesuffix("_min") for name in PHASE93_RECALL_THRESHOLDS
)

_RED_TEAM_TOPIC = "red_team_counter_thesis"
_QUERY_INTENTS = {
    "SUPPORT_DISCOVERY",
    "COUNTER_OR_SUPERSESSION_DISCOVERY",
}
_FACT_ROLES = {"SUPPORT", "COUNTER", "SUPERSESSION"}
_MATERIALITIES = {"CRITICAL", "NONCRITICAL"}
_FORBIDDEN_GOLD_AUTHORITY_KEYS = {
    "score",
    "scores",
    "total_score",
    "final_score",
    "component_score",
    "component_scores",
    "component_points",
    "expected_score",
    "stage",
    "stages",
    "final_stage",
    "expected_stage",
    "investment_recommendation",
}


@dataclass(frozen=True)
class FullThesisPostRunComparison:
    """A post-run result that is safe to publish after production completes."""

    status: str
    comparisons: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


def load_phase93_gold_corpus(
    repo_root: str | Path = ".",
    *,
    gold_root: str | Path = PHASE93_GOLD_ROOT,
) -> Mapping[str, Any]:
    """Load and validate every private Gold leaf."""

    root = Path(repo_root).resolve()
    gold = Path(gold_root)
    if not gold.is_absolute():
        gold = root / gold
    corpus: dict[str, Any] = {
        "root": gold,
        "manifest": _read_json(gold / PHASE93_OUTPUT_FILES["manifest"]),
        "isolation_baseline": _read_json(
            gold / PHASE93_OUTPUT_FILES["pre_gold_production_isolation"]
        ),
        "queries": _read_jsonl(gold / PHASE93_OUTPUT_FILES["query_ledger"]),
        "sources": _read_jsonl(gold / PHASE93_OUTPUT_FILES["source_map"]),
        "facts": _read_jsonl(gold / PHASE93_OUTPUT_FILES["material_facts"]),
        "counterfacts": _read_jsonl(
            gold / PHASE93_OUTPUT_FILES["counterfacts"]
        ),
        "memos": _read_jsonl(gold / PHASE93_OUTPUT_FILES["component_memos"]),
        "coverage": _read_json(
            gold / PHASE93_OUTPUT_FILES["question_coverage"]
        ),
    }
    _validate_phase93_gold_corpus(corpus)
    return corpus


def compile_phase93_gold_research_recall_audit(
    repo_root: str | Path = ".",
    *,
    gold_root: str | Path = PHASE93_GOLD_ROOT,
    production_root: str | Path = PHASE93_BASELINE_PRODUCTION_ROOT,
    post_run_audit_path: str | Path | None = None,
) -> Mapping[str, Any]:
    """Compile the Phase 93 build audit and project a verified Phase 94 result."""

    root = Path(repo_root).resolve()
    corpus = load_phase93_gold_corpus(root, gold_root=gold_root)
    gold = Path(corpus["root"])
    production = Path(production_root)
    if not production.is_absolute():
        production = root / production
    manifest = corpus["manifest"]
    facts = tuple(corpus["facts"])
    sources = tuple(corpus["sources"])
    queries = tuple(corpus["queries"])
    memos = tuple(corpus["memos"])
    target_ids = tuple(str(value) for value in manifest["target_ids"])
    component_ids = tuple(str(value) for value in manifest["component_ids"])
    leakage = _audit_production_gold_leakage(
        corpus=corpus,
        production_root=production,
    )
    authority_paths = gold_authority_leakage_paths(corpus)
    output_hashes = {
        name: _file_sha256(gold / file_name)
        for name, file_name in PHASE93_OUTPUT_FILES.items()
    }
    per_target = {}
    for target_id in target_ids:
        target_facts = tuple(
            row for row in facts if str(row["target_id"]) == target_id
        )
        target_queries = tuple(
            row for row in queries if str(row["target_id"]) == target_id
        )
        target_sources = tuple(
            row for row in sources if str(row["target_id"]) == target_id
        )
        target_memos = tuple(
            row for row in memos if str(row["target_id"]) == target_id
        )
        per_target[target_id] = {
            "target_name": next(
                str(row["target_name"])
                for row in manifest["targets"]
                if str(row["target_id"]) == target_id
            ),
            "query_count": len(target_queries),
            "source_count": len(target_sources),
            "material_fact_count": len(target_facts),
            "critical_fact_count": sum(
                row["materiality"] == "CRITICAL" for row in target_facts
            ),
            "counter_supersession_fact_count": sum(
                row["fact_role"] in {"COUNTER", "SUPERSESSION"}
                for row in target_facts
            ),
            "component_memo_count": len(target_memos),
            "component_ids": sorted(
                str(row["component_id"]) for row in target_memos
            ),
            "observed_source_families": sorted(
                {str(row["source_family"]) for row in target_sources}
            ),
        }

    production_lane = _read_optional_json(
        production / "production_lane_manifest.json"
    )
    production_as_of = str(
        production_lane.get("as_of_date")
        or corpus["isolation_baseline"].get("production_as_of_date")
        or ""
    )
    gold_as_of = str(manifest["as_of_date"])
    clean_run_comparable = bool(
        production_as_of == gold_as_of
        and (production / "production_component_memos.jsonl").exists()
    )
    verified_post_run = _load_verified_phase94_post_run_audit(
        root=root,
        explicit_path=post_run_audit_path,
        production_root=production,
        gold_as_of=gold_as_of,
        target_ids=target_ids,
    )
    post_run_comparison = {
        "status": (
            "READY_TO_COMPARE"
            if clean_run_comparable
            else PHASE93_POST_RUN_PENDING
        ),
        "current_baseline_production_as_of_date": production_as_of or None,
        "gold_as_of_date": gold_as_of,
        "current_baseline_is_phase94_clean_rerun": False,
        "critical_material_fact_recall": None,
        "counter_supersession_recall": None,
        "all_material_fact_recall": None,
        "component_research_topic_coverage": None,
        "thresholds": dict(PHASE93_RECALL_THRESHOLDS),
        "pending_reason": (
            None
            if clean_run_comparable
            else f"{gold_as_of} Gold를 숨긴 Phase 94 clean production rerun이 아직 없다."
        ),
    }
    if verified_post_run is not None:
        post_run_audit = verified_post_run["audit"]
        metrics = post_run_audit["metrics"]
        post_run_comparison = {
            "status": PHASE93_POST_RUN_PASS,
            "current_baseline_production_as_of_date": gold_as_of,
            "gold_as_of_date": gold_as_of,
            "current_baseline_is_phase94_clean_rerun": True,
            **{
                metric_name: metrics[metric_name]
                for metric_name in _POST_RUN_METRIC_NAMES
            },
            "thresholds": dict(PHASE93_RECALL_THRESHOLDS),
            "pending_reason": None,
            "source_audit_path": verified_post_run["relative_path"],
        }
    critical_counts = {
        "gold_output_file_missing_count": sum(
            not (gold / file_name).exists()
            for file_name in PHASE93_OUTPUT_FILES.values()
        ),
        "gold_authority_leakage_count": len(authority_paths),
        "gold_source_injected_into_production_count": leakage[
            "gold_source_injected_into_production_count"
        ],
        "gold_query_leaked_into_production_count": leakage[
            "gold_query_leaked_into_production_count"
        ],
        "gold_fact_leaked_into_production_prompt_count": leakage[
            "gold_fact_leaked_into_production_prompt_count"
        ],
        "production_lane_gold_visibility_count": leakage[
            "production_lane_gold_visibility_count"
        ],
        "nine_fact_false_completeness_count": int(len(facts) <= 9),
        "target_component_topic_missing_count": sum(
            set(component_ids)
            != {
                str(row["component_id"])
                for row in memos
                if str(row["target_id"]) == target_id
            }
            for target_id in target_ids
        ),
    }
    critical_sum = sum(critical_counts.values())
    return {
        "schema_version": PHASE93_SCHEMA_VERSION,
        "status": PHASE93_READY if critical_sum == 0 else "V5_PHASE93_FAIL",
        "phase": 93,
        "as_of_date": gold_as_of,
        "benchmark_mode": "PRIVATE_POST_RUN_FULL_THESIS_GOLD",
        "gold_lane_role": "EVALUATION_ONLY_PRIVATE_POST_RUN",
        "production_lane_role": "INDEPENDENT_CLEAN_RESEARCHER_RUN",
        "legacy_nine_fact_audit_is_authoritative": False,
        "supersedes_for_full_thesis_recall": (
            "docs/operational/e2r_research_quality_gold_audit.json"
        ),
        "gold_fact_count": len(facts),
        "gold_counter_supersession_fact_count": sum(
            row["fact_role"] in {"COUNTER", "SUPERSESSION"}
            for row in facts
        ),
        "gold_query_count": len(queries),
        "gold_source_count": len(sources),
        "gold_component_memo_count": len(memos),
        "target_count": len(target_ids),
        "component_count_per_target": len(component_ids),
        "gold_component_research_topic_coverage": 1.0,
        "required_source_families": list(PHASE93_SOURCE_FAMILIES),
        "per_target": per_target,
        "lane_isolation": {
            "gold_visibility_during_production": False,
            "comparison_timing": "POST_RUN_ONLY",
            "gold_url_injection_allowed": False,
            "gold_query_injection_allowed": False,
            "gold_fact_injection_allowed": False,
            "gold_expected_score_or_stage_exists": False,
            "clean_rerun_required_after_research_fix": True,
            "leakage_audit": leakage,
        },
        "post_run_comparison": post_run_comparison,
        "reproducibility": {
            "gold_root": str(gold.relative_to(root)),
            "gold_output_sha256": output_hashes,
            "gold_payload_sha256": stable_hash(
                {
                    "manifest": manifest,
                    "isolation_baseline": corpus["isolation_baseline"],
                    "queries": queries,
                    "sources": sources,
                    "facts": facts,
                    "counterfacts": tuple(corpus["counterfacts"]),
                    "memos": memos,
                    "coverage": corpus["coverage"],
                }
            ),
        },
        "phase93_scope_truth": {
            "benchmark_corpus_complete": True,
            "post_run_recall_attested": verified_post_run is not None,
            "production_readiness_claimed": False,
            "phase94_clean_rerun_required": True,
        },
        "gold_authority_leakage_paths": list(authority_paths),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
    }


def compare_phase93_gold_post_run(
    repo_root: str | Path = ".",
    *,
    production_root: str | Path,
    gold_root: str | Path = PHASE93_GOLD_ROOT,
) -> FullThesisPostRunComparison:
    """Compute full-thesis recall only for a same-as-of, completed blind run."""

    root = Path(repo_root).resolve()
    production = Path(production_root)
    if not production.is_absolute():
        production = root / production
    lane = _read_json(production / "production_lane_manifest.json")
    production_target_ids = _validate_post_run_production_lane(lane)

    # The private corpus may only be opened after the production lane proves
    # that every target is closed under the blind-run contract.
    corpus = load_phase93_gold_corpus(root, gold_root=gold_root)
    gold = Path(corpus["root"])
    if str(lane.get("as_of_date") or "") != str(
        corpus["manifest"]["as_of_date"]
    ):
        raise ValueError("post-run production and Gold as_of_date must match")
    gold_target_ids = tuple(
        str(value) for value in corpus["manifest"]["target_ids"]
    )
    if (
        len(production_target_ids) != len(gold_target_ids)
        or set(production_target_ids) != set(gold_target_ids)
    ):
        raise ValueError("post-run production and Gold target roster must match")
    memo_path = production / "production_component_memos.jsonl"
    production_memos = _read_jsonl(memo_path)
    _validate_production_component_memos(
        production_memos,
        target_ids=tuple(str(value) for value in corpus["manifest"]["target_ids"]),
        component_ids=tuple(
            str(value) for value in corpus["manifest"]["component_ids"]
        ),
    )
    blind = BlindResearchQualityBenchmark().compare(
        gold_root=gold,
        production_root=production,
        post_run_semantic_adjudication_root=production,
    )
    full_leakage = _audit_production_gold_leakage(
        corpus=corpus,
        production_root=production,
    )
    comparison_rows = tuple(row.to_dict() for row in blind.comparisons)
    qualified_ids = {
        str(row["gold_fact_id"])
        for row in comparison_rows
        if row["semantic_match"]
        and row["source_quality_match"]
        and row["currentness_match"]
        and row["mechanism_scope_match"]
    }
    facts = tuple(corpus["facts"])
    critical = tuple(row for row in facts if row["materiality"] == "CRITICAL")
    counter = tuple(
        row
        for row in facts
        if row["fact_role"] in {"COUNTER", "SUPERSESSION"}
    )
    critical_recall = _recall(critical, qualified_ids)
    counter_recall = _recall(counter, qualified_ids)
    all_recall = _recall(facts, qualified_ids)
    complete_memo_keys = {
        (str(row["target_id"]), str(row["component_id"]))
        for row in production_memos
        if row.get("research_status") == "RESEARCH_COMPLETE"
    }
    covered_component_keys = set()
    for target_id in corpus["manifest"]["target_ids"]:
        for component_id in corpus["manifest"]["component_ids"]:
            scoped = tuple(
                row
                for row in facts
                if str(row["target_id"]) == str(target_id)
                and str(row["component_id"]) == str(component_id)
            )
            support_found = any(
                row["fact_role"] == "SUPPORT"
                and str(row["fact_id"]) in qualified_ids
                for row in scoped
            )
            counter_found = any(
                row["fact_role"] in {"COUNTER", "SUPERSESSION"}
                and str(row["fact_id"]) in qualified_ids
                for row in scoped
            )
            key = (str(target_id), str(component_id))
            if support_found and counter_found and key in complete_memo_keys:
                covered_component_keys.add(key)
    required_component_count = (
        len(corpus["manifest"]["target_ids"])
        * len(corpus["manifest"]["component_ids"])
    )
    topic_coverage = len(covered_component_keys) / required_component_count
    metrics = {
        "critical_material_fact_recall": round(critical_recall, 6),
        "counter_supersession_recall": round(counter_recall, 6),
        "all_material_fact_recall": round(all_recall, 6),
        "component_research_topic_coverage": round(topic_coverage, 6),
    }
    threshold_failures = {
        f"{metric_key}_below_threshold_count": int(
            metrics[metric_key] < threshold
        )
        for threshold_key, threshold in PHASE93_RECALL_THRESHOLDS.items()
        for metric_key in (threshold_key.removesuffix("_min"),)
    }
    leakage_count = sum(
        int(full_leakage[key])
        for key in (
            "gold_source_injected_into_production_count",
            "gold_query_leaked_into_production_count",
            "gold_fact_leaked_into_production_prompt_count",
            "production_lane_gold_visibility_count",
        )
    )
    critical_counts = {
        **threshold_failures,
        "gold_leakage_count": leakage_count,
        "production_component_memo_incomplete_count": (
            required_component_count - len(complete_memo_keys)
        ),
    }
    critical_sum = sum(critical_counts.values())
    status = PHASE93_POST_RUN_PASS if critical_sum == 0 else PHASE93_POST_RUN_FAIL
    audit = {
        "schema_version": PHASE93_SCHEMA_VERSION,
        "status": status,
        "as_of_date": corpus["manifest"]["as_of_date"],
        "comparison_timing": "POST_RUN_ONLY",
        "gold_visibility_during_production": False,
        "metrics": metrics,
        "thresholds": dict(PHASE93_RECALL_THRESHOLDS),
        "gold_fact_count": len(facts),
        "qualified_material_fact_match_count": len(qualified_ids),
        "covered_target_component_count": len(covered_component_keys),
        "required_target_component_count": required_component_count,
        "blind_leakage_audit": full_leakage,
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "comparisons": list(comparison_rows),
    }
    return FullThesisPostRunComparison(
        status=status,
        comparisons=comparison_rows,
        audit=audit,
    )


def _validate_post_run_production_lane(
    lane: Mapping[str, Any],
) -> tuple[str, ...]:
    target_ids_raw = lane.get("target_ids")
    target_statuses = lane.get("target_statuses")
    if (
        lane.get("schema_version") != "e2r_v5_phase94_production_lane_v1"
        or lane.get("lane_role") != "PRODUCTION"
        or lane.get("production_research_complete") is not True
        or lane.get("gold_visibility") is not False
        or lane.get("gold_query_visibility") is not False
        or lane.get("gold_url_visibility") is not False
        or lane.get("gold_fact_visibility") is not False
        or lane.get("comparison_timing") != "POST_RUN_ONLY"
        or lane.get("completion_based_on_fixed_rounds") is not False
        or not isinstance(target_ids_raw, (list, tuple))
        or not isinstance(target_statuses, Mapping)
    ):
        raise ValueError("post-run Gold requires a completed blind production lane")
    target_ids = tuple(str(value).strip() for value in target_ids_raw)
    if (
        not target_ids
        or any(not value for value in target_ids)
        or len(target_ids) != len(set(target_ids))
        or set(target_statuses) != set(target_ids)
        or any(
            target_statuses[target_id]
            != "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
            for target_id in target_ids
        )
    ):
        raise ValueError("post-run Gold requires an exact completed target roster")
    return target_ids


def write_phase93_gold_research_recall_audit(
    repo_root: str | Path = ".",
    *,
    output_path: str | Path | None = None,
    production_root: str | Path = PHASE93_BASELINE_PRODUCTION_ROOT,
    post_run_audit_path: str | Path | None = None,
) -> Path:
    root = Path(repo_root).resolve()
    path = Path(output_path) if output_path is not None else root / PHASE93_AUDIT_PATH
    if not path.is_absolute():
        path = root / path
    write_json(
        path,
        compile_phase93_gold_research_recall_audit(
            root,
            production_root=production_root,
            post_run_audit_path=post_run_audit_path,
        ),
    )
    return path


def write_phase94_tracked_post_run_receipt(
    repo_root: str | Path = ".",
    *,
    production_root: str | Path,
) -> Mapping[str, Path]:
    """Publish the minimal verified Phase 94 receipt needed for clean rebuilds."""

    root = Path(repo_root).resolve()
    production = Path(production_root)
    if not production.is_absolute():
        production = root / production
    audit = _read_json(production / PHASE94_POST_RUN_AUDIT_FILE)
    lane = _read_json(production / PHASE94_PRODUCTION_LANE_FILE)
    corpus = load_phase93_gold_corpus(root)
    manifest = corpus["manifest"]
    target_ids = tuple(str(value) for value in manifest["target_ids"])
    gold_as_of = str(manifest["as_of_date"])
    if not _phase94_post_run_audit_is_scope_matched_pass(
        audit=audit,
        lane=lane,
        gold_as_of=gold_as_of,
        target_ids=target_ids,
    ):
        raise ValueError("tracked Phase 94 receipt requires a scope-matched PASS")
    destination = root / PHASE94_TRACKED_POST_RUN_ROOT
    paths = {
        "audit": destination / PHASE94_POST_RUN_AUDIT_FILE,
        "production_lane": destination / PHASE94_PRODUCTION_LANE_FILE,
    }
    write_json(paths["audit"], audit)
    write_json(paths["production_lane"], lane)
    return paths


def write_phase93_post_run_comparison(
    *,
    result: FullThesisPostRunComparison,
    comparison_path: str | Path,
    audit_path: str | Path,
) -> None:
    write_jsonl(Path(comparison_path), result.comparisons)
    write_json(Path(audit_path), result.audit)


def gold_authority_leakage_paths(corpus: Mapping[str, Any]) -> tuple[str, ...]:
    """Return paths where Gold attempts to carry a score, Stage, or advice."""

    paths: list[str] = []

    def visit(value: Any, path: str) -> None:
        if isinstance(value, Mapping):
            for key, child in value.items():
                child_path = f"{path}.{key}" if path else str(key)
                if str(key).casefold() in _FORBIDDEN_GOLD_AUTHORITY_KEYS:
                    paths.append(child_path)
                visit(child, child_path)
        elif isinstance(value, (list, tuple)):
            for index, child in enumerate(value):
                visit(child, f"{path}[{index}]")

    for key in (
        "manifest",
        "isolation_baseline",
        "queries",
        "sources",
        "facts",
        "counterfacts",
        "memos",
        "coverage",
    ):
        visit(corpus[key], key)
    return tuple(sorted(set(paths)))


def _load_verified_phase94_post_run_audit(
    *,
    root: Path,
    explicit_path: str | Path | None,
    production_root: Path,
    gold_as_of: str,
    target_ids: Sequence[str],
) -> Mapping[str, Any] | None:
    candidate_paths: tuple[Path, ...]
    if explicit_path is not None:
        path = Path(explicit_path)
        candidate_paths = (path if path.is_absolute() else root / path,)
    else:
        scoped = production_root / "post_run_gold_recall_audit.json"
        tracked = (
            root
            / PHASE94_TRACKED_POST_RUN_ROOT
            / PHASE94_POST_RUN_AUDIT_FILE
        )
        if scoped.is_file():
            candidate_paths = (scoped,)
        elif tracked.is_file():
            candidate_paths = (tracked,)
        else:
            candidate_paths = tuple(
                sorted(
                    root.glob(
                        "output/researcher_mode/**/"
                        "post_run_gold_recall_audit.json"
                    ),
                    key=lambda path: str(path),
                )
            )

    for path in candidate_paths:
        audit = _safe_read_mapping(path)
        lane = _safe_read_mapping(path.parent / "production_lane_manifest.json")
        if not _phase94_post_run_audit_is_scope_matched_pass(
            audit=audit,
            lane=lane,
            gold_as_of=gold_as_of,
            target_ids=target_ids,
        ):
            continue
        try:
            relative_path = str(path.resolve().relative_to(root.resolve()))
        except ValueError:
            relative_path = str(path.resolve())
        return {
            "audit": audit,
            "relative_path": relative_path,
        }
    return None


def _phase94_post_run_audit_is_scope_matched_pass(
    *,
    audit: Mapping[str, Any],
    lane: Mapping[str, Any],
    gold_as_of: str,
    target_ids: Sequence[str],
) -> bool:
    critical_count_sum = audit.get("critical_count_sum")
    if (
        audit.get("schema_version") != PHASE93_SCHEMA_VERSION
        or audit.get("status") != PHASE93_POST_RUN_PASS
        or str(audit.get("as_of_date") or "") != gold_as_of
        or audit.get("comparison_timing") != "POST_RUN_ONLY"
        or audit.get("gold_visibility_during_production") is not False
        or not isinstance(critical_count_sum, int)
        or isinstance(critical_count_sum, bool)
        or critical_count_sum != 0
    ):
        return False
    expected_targets = tuple(str(value) for value in target_ids)
    lane_targets = tuple(str(value) for value in lane.get("target_ids") or ())
    if (
        str(lane.get("as_of_date") or "") != gold_as_of
        or lane.get("production_research_complete") is not True
        or lane.get("gold_visibility") is not False
        or lane.get("gold_query_visibility") is not False
        or lane.get("gold_url_visibility") is not False
        or lane.get("gold_fact_visibility") is not False
        or lane.get("comparison_timing") != "POST_RUN_ONLY"
        or len(lane_targets) != len(expected_targets)
        or set(lane_targets) != set(expected_targets)
    ):
        return False

    metrics = audit.get("metrics")
    if not isinstance(metrics, Mapping):
        return False
    for threshold_name, expected_threshold in PHASE93_RECALL_THRESHOLDS.items():
        metric_name = threshold_name.removesuffix("_min")
        metric = metrics.get(metric_name)
        if (
            not _is_number(metric)
            or float(metric) < float(expected_threshold)
        ):
            return False
    return True


def _safe_read_mapping(path: Path) -> Mapping[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, Mapping) else {}


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _validate_phase93_gold_corpus(corpus: Mapping[str, Any]) -> None:
    manifest = corpus["manifest"]
    queries = tuple(corpus["queries"])
    sources = tuple(corpus["sources"])
    facts = tuple(corpus["facts"])
    counterfacts = tuple(corpus["counterfacts"])
    memos = tuple(corpus["memos"])
    coverage = corpus["coverage"]
    isolation_baseline = corpus["isolation_baseline"]
    if manifest.get("schema_version") != PHASE93_MANIFEST_SCHEMA_VERSION:
        raise ValueError("Phase 93 Gold manifest schema mismatch")
    if manifest.get("evaluation_only") is not True:
        raise ValueError("Gold corpus must be evaluation-only")
    if manifest.get("production_visibility") is not False:
        raise ValueError("Gold corpus cannot be visible during production")
    if manifest.get("comparison_timing") != "POST_RUN_ONLY":
        raise ValueError("Gold comparison must be post-run only")
    if manifest.get("production_score_authority") is not False:
        raise ValueError("Gold corpus cannot own production score")
    if manifest.get("production_stage_authority") is not False:
        raise ValueError("Gold corpus cannot own production Stage")
    expected_outputs = {
        key: value
        for key, value in PHASE93_OUTPUT_FILES.items()
        if key != "manifest"
    }
    if manifest.get("outputs") != expected_outputs:
        raise ValueError("Gold manifest output contract is incomplete")
    if tuple(manifest.get("required_source_families") or ()) != PHASE93_SOURCE_FAMILIES:
        raise ValueError("Gold manifest source-family contract mismatch")
    if manifest.get("red_team_topic_id") != _RED_TEAM_TOPIC:
        raise ValueError("Gold manifest red-team topic mismatch")
    if manifest.get("post_run_recall_contract") != PHASE93_RECALL_THRESHOLDS:
        raise ValueError("Gold manifest recall threshold contract mismatch")

    target_ids = tuple(str(value) for value in manifest.get("target_ids") or ())
    component_ids = tuple(
        str(value) for value in manifest.get("component_ids") or ()
    )
    if not target_ids or not component_ids:
        raise ValueError("Gold targets and components are required")
    _require_unique_values(target_ids, "target_ids")
    _require_unique_values(component_ids, "component_ids")
    targets = tuple(manifest.get("targets") or ())
    _require_unique_rows(targets, "target_id")
    if {str(row["target_id"]) for row in targets} != set(target_ids):
        raise ValueError("Gold target registry does not match target_ids")
    as_of_date = str(manifest.get("as_of_date") or "")
    as_of = date.fromisoformat(as_of_date)
    _require_not_future(str(manifest["gold_research_completed_at"]), as_of)
    if len(facts) <= 9:
        raise ValueError("full-thesis Gold cannot be the legacy nine-fact corpus")
    _validate_isolation_baseline(
        isolation_baseline,
        queries=queries,
        sources=sources,
        facts=facts,
        target_ids=target_ids,
        as_of=as_of,
    )

    _require_unique_rows(queries, "query_id")
    _require_unique_rows(sources, "source_id")
    _require_unique_rows(facts, "fact_id")
    _require_unique_rows(counterfacts, "fact_id")
    _require_unique_rows(memos, "memo_id")
    query_ids = {str(row["query_id"]) for row in queries}
    query_by_id = {str(row["query_id"]): row for row in queries}
    source_by_id = {str(row["source_id"]): row for row in sources}
    fact_by_id = {str(row["fact_id"]): row for row in facts}

    for row in queries:
        _require_fields(
            row,
            {
                "query_id",
                "target_id",
                "topic_id",
                "intent",
                "literal_query",
                "executed_at",
                "generator_kind",
                "result_source_ids",
                "production_execution_allowed",
            },
            "Gold query",
        )
        if str(row["target_id"]) not in target_ids:
            raise ValueError("Gold query target is outside the manifest")
        if str(row["topic_id"]) not in {*component_ids, _RED_TEAM_TOPIC}:
            raise ValueError("Gold query topic is unknown")
        if row["intent"] not in _QUERY_INTENTS:
            raise ValueError("Gold query intent is unknown")
        if row["generator_kind"] != "INDEPENDENT_GOLD_RESEARCHER":
            raise ValueError("Gold query must have independent researcher lineage")
        if row["production_execution_allowed"] is not False:
            raise ValueError("Gold query cannot be a production query")
        _require_not_future(str(row["executed_at"]), as_of)
        if not str(row["literal_query"]).strip():
            raise ValueError("Gold query text is empty")

    for target_id in target_ids:
        for topic_id in (*component_ids, _RED_TEAM_TOPIC):
            intents = {
                str(row["intent"])
                for row in queries
                if str(row["target_id"]) == target_id
                and str(row["topic_id"]) == topic_id
            }
            if intents != _QUERY_INTENTS:
                raise ValueError(
                    f"Gold query ledger lacks balanced intents: {target_id}/{topic_id}"
                )

    for row in sources:
        _require_fields(
            row,
            {
                "source_id",
                "target_id",
                "source_family",
                "research_route",
                "source_tier",
                "source_url",
                "title",
                "published_date",
                "availability_status",
                "full_source_verified",
                "evidence_eligible",
                "anchor",
                "query_ids",
            },
            "Gold source",
        )
        if str(row["target_id"]) not in target_ids:
            raise ValueError("Gold source target is outside the manifest")
        if str(row["source_family"]) not in PHASE93_SOURCE_FAMILIES:
            raise ValueError("Gold source family is unknown")
        if not str(row["source_url"]).startswith(("https://", "http://")):
            raise ValueError("Gold source URL must be public http(s)")
        _require_not_future(str(row["published_date"]), as_of)
        if row["availability_status"] != "AVAILABLE":
            raise ValueError("Phase 93 Gold source must be available")
        if not str(row["anchor"]).strip():
            raise ValueError("Gold source anchor is empty")
        linked_queries = tuple(str(value) for value in row["query_ids"])
        if not linked_queries or not set(linked_queries) <= query_ids:
            raise ValueError("Gold source query lineage is missing")
        if any(
            str(query_by_id[query_id]["target_id"])
            != str(row["target_id"])
            for query_id in linked_queries
        ):
            raise ValueError("Gold source has cross-target query lineage")
        if str(row["source_family"]) == "NAVER_WEB_DISCOVERY":
            if row["evidence_eligible"] is not False:
                raise ValueError("Naver/Web discovery page cannot be evidence")
        elif row["evidence_eligible"] is True and row["full_source_verified"] is not True:
            raise ValueError("evidence-eligible Gold source needs full-source review")

    for row in queries:
        linked_sources = tuple(str(value) for value in row["result_source_ids"])
        if not linked_sources:
            raise ValueError("Gold query has no accounted result source")
        for source_id in linked_sources:
            source = source_by_id.get(source_id)
            if source is None:
                raise ValueError("Gold query references an unknown result source")
            if str(source["target_id"]) != str(row["target_id"]):
                raise ValueError("Gold query has cross-target result lineage")
            if str(row["query_id"]) not in {
                str(value) for value in source["query_ids"]
            }:
                raise ValueError("Gold query/source lineage is not bidirectional")

    required_families = set(PHASE93_SOURCE_FAMILIES)
    for target_id in target_ids:
        observed = {
            str(row["source_family"])
            for row in sources
            if str(row["target_id"]) == target_id
        }
        if observed != required_families:
            missing = sorted(required_families - observed)
            extra = sorted(observed - required_families)
            raise ValueError(
                f"Gold source family coverage mismatch for {target_id}: "
                f"missing={missing} extra={extra}"
            )

    required_fact_fields = {
        "fact_id",
        "target_id",
        "component_id",
        "question_family_id",
        "subject_id",
        "predicate_family",
        "normalized_object",
        "period",
        "mechanism_scope_id",
        "source_id",
        "source_tier",
        "temporal_status",
        "as_of_date",
        "materiality",
        "fact_role",
        "independent_fact",
        "exact_anchor",
    }
    for row in facts:
        _require_fields(row, required_fact_fields, "Gold fact")
        target_id = str(row["target_id"])
        component_id = str(row["component_id"])
        if target_id not in target_ids or component_id not in component_ids:
            raise ValueError("Gold fact target/component is outside the manifest")
        source = source_by_id.get(str(row["source_id"]))
        if source is None or str(source["target_id"]) != target_id:
            raise ValueError("Gold fact source lineage is missing or cross-target")
        if source["evidence_eligible"] is not True or source["full_source_verified"] is not True:
            raise ValueError("Gold fact cannot use discovery-only or partial source")
        if str(row["source_tier"]) != str(source["source_tier"]):
            raise ValueError("Gold fact/source tier mismatch")
        if str(row["as_of_date"]) != as_of_date:
            raise ValueError("Gold fact has a wrong as_of_date")
        if row["temporal_status"] != "CURRENT":
            raise ValueError("Gold material fact must be current or explicitly superseded")
        if row["materiality"] not in _MATERIALITIES:
            raise ValueError("Gold materiality is unknown")
        if row["fact_role"] not in _FACT_ROLES:
            raise ValueError("Gold fact role is unknown")
        if not str(row["independent_fact"]).strip() or not str(row["exact_anchor"]).strip():
            raise ValueError("Gold fact needs a source-backed statement and anchor")

    for target_id in target_ids:
        for component_id in component_ids:
            scoped = tuple(
                row
                for row in facts
                if str(row["target_id"]) == target_id
                and str(row["component_id"]) == component_id
            )
            if not any(row["fact_role"] == "SUPPORT" for row in scoped):
                raise ValueError(f"Gold support fact missing: {target_id}/{component_id}")
            if not any(
                row["fact_role"] in {"COUNTER", "SUPERSESSION"}
                for row in scoped
            ):
                raise ValueError(f"Gold counter fact missing: {target_id}/{component_id}")

    expected_counter_ids = {
        str(row["fact_id"])
        for row in facts
        if row["fact_role"] in {"COUNTER", "SUPERSESSION"}
    }
    if {str(row["fact_id"]) for row in counterfacts} != expected_counter_ids:
        raise ValueError("Gold counterfact leaf is not an exact counter projection")
    for row in counterfacts:
        if row != fact_by_id[str(row["fact_id"])]:
            raise ValueError("Gold counterfact content diverges from material fact")

    expected_memo_keys = {
        (target_id, component_id)
        for target_id in target_ids
        for component_id in component_ids
    }
    memo_keys = {
        (str(row.get("target_id") or ""), str(row.get("component_id") or ""))
        for row in memos
    }
    if memo_keys != expected_memo_keys or len(memos) != len(expected_memo_keys):
        raise ValueError("Gold component memos must cover every target/component once")
    for row in memos:
        _require_fields(
            row,
            {
                "memo_id",
                "target_id",
                "component_id",
                "as_of_date",
                "research_status",
                "research_topics",
                "support_fact_ids",
                "counterfact_ids",
                "supersession_fact_ids",
                "source_ids",
                "why_higher",
                "why_lower",
                "red_team_question",
                "red_team_resolution",
                "information_gaps",
            },
            "Gold component memo",
        )
        if row["research_status"] != "GOLD_RESEARCH_COMPLETE":
            raise ValueError("Gold component memo is incomplete")
        if str(row["as_of_date"]) != as_of_date:
            raise ValueError("Gold component memo has a wrong as_of_date")
        support_ids = tuple(str(value) for value in row["support_fact_ids"])
        counter_ids = tuple(str(value) for value in row["counterfact_ids"])
        if not support_ids or not counter_ids:
            raise ValueError("Gold memo needs support and counter facts")
        memo_fact_ids = (*support_ids, *counter_ids, *row["supersession_fact_ids"])
        for fact_id in memo_fact_ids:
            fact = fact_by_id.get(str(fact_id))
            if fact is None:
                raise ValueError("Gold memo references an unknown fact")
            if (
                str(fact["target_id"]) != str(row["target_id"])
                or str(fact["component_id"]) != str(row["component_id"])
            ):
                raise ValueError("Gold memo has cross-target/component fact lineage")
        if any(fact_by_id[fact_id]["fact_role"] != "SUPPORT" for fact_id in support_ids):
            raise ValueError("Gold memo support IDs contain a non-support fact")
        if any(
            fact_by_id[fact_id]["fact_role"] not in {"COUNTER", "SUPERSESSION"}
            for fact_id in counter_ids
        ):
            raise ValueError("Gold memo counter IDs contain a support fact")
        expected_sources = {
            str(fact_by_id[str(fact_id)]["source_id"])
            for fact_id in memo_fact_ids
        }
        if not expected_sources <= {str(value) for value in row["source_ids"]}:
            raise ValueError("Gold memo source lineage is incomplete")
        for key in ("why_higher", "why_lower", "red_team_question", "red_team_resolution"):
            if not str(row[key]).strip():
                raise ValueError(f"Gold memo {key} is empty")

    if coverage.get("schema_version") != "e2r_v5_full_thesis_gold_coverage_v1":
        raise ValueError("Gold coverage schema mismatch")
    if coverage.get("as_of_date") != as_of_date:
        raise ValueError("Gold coverage has a wrong as_of_date")
    coverage_rows = tuple(coverage.get("questions") or ())
    _require_unique_rows(coverage_rows, "question_family_id")
    coverage_keys = {
        (str(row.get("target_id") or ""), str(row.get("component_id") or ""))
        for row in coverage_rows
    }
    if coverage_keys != expected_memo_keys:
        raise ValueError("Gold question coverage is not full-thesis complete")
    if any(row.get("evaluation") != "SUPPORT_AND_COUNTER_EVIDENCE_FOUND" for row in coverage_rows):
        raise ValueError("Gold question coverage lacks two-sided evidence")

    authority_paths = gold_authority_leakage_paths(corpus)
    if authority_paths:
        raise ValueError(
            f"Gold carries forbidden score/Stage/advice authority: {authority_paths}"
        )


def _validate_production_component_memos(
    rows: Sequence[Mapping[str, Any]],
    *,
    target_ids: Sequence[str],
    component_ids: Sequence[str],
) -> None:
    expected = {
        (str(target_id), str(component_id))
        for target_id in target_ids
        for component_id in component_ids
    }
    observed = {
        (str(row.get("target_id") or ""), str(row.get("component_id") or ""))
        for row in rows
    }
    if observed != expected or len(rows) != len(expected):
        raise ValueError("production component memos are not 7/7 for every target")
    if any(row.get("research_status") != "RESEARCH_COMPLETE" for row in rows):
        raise ValueError("production component memo is not research-complete")


def _audit_production_gold_leakage(
    *,
    corpus: Mapping[str, Any],
    production_root: Path,
) -> Mapping[str, Any]:
    input_path = production_root / "production_input_manifest.jsonl"
    lane_path = production_root / "production_lane_manifest.json"
    inputs = _read_optional_jsonl(input_path)
    lane = _read_optional_json(lane_path)
    isolation_baseline = corpus["isolation_baseline"]
    if not inputs and not lane:
        counts = isolation_baseline["exact_overlap_counts"]
        return {
            "proof_source": "TRACKED_PRE_GOLD_FINGERPRINT_SNAPSHOT",
            "gold_source_injected_into_production_count": int(
                counts["gold_source_injected_into_production_count"]
            ),
            "gold_query_leaked_into_production_count": int(
                counts["gold_query_leaked_into_production_count"]
            ),
            "gold_fact_leaked_into_production_prompt_count": int(
                counts["gold_fact_leaked_into_production_prompt_count"]
            ),
            "production_lane_gold_visibility_count": int(
                counts["production_lane_gold_visibility_count"]
            ),
            "source_injection_input_ids": [],
            "query_leak_input_ids": [],
            "fact_leak_input_ids": [],
        }
    gold_root = Path(corpus["root"]).resolve()
    gold_urls = {
        str(row["source_url"])
        for row in corpus["sources"]
        if row.get("source_url")
    }
    gold_queries = {
        str(row["literal_query"]).strip().casefold() for row in corpus["queries"]
    }
    gold_fact_ids = {str(row["fact_id"]) for row in corpus["facts"]}
    source_ids: list[str] = []
    query_ids: list[str] = []
    fact_ids: list[str] = []
    for row in inputs:
        input_id = str(row.get("input_id") or "")
        input_type = str(row.get("input_type") or "").upper()
        origin = str(row.get("origin") or "").upper()
        value = str(row.get("value") or "")
        path_value = str(row.get("path") or "")
        path_is_gold = bool(
            path_value
            and _is_relative_to(Path(path_value).resolve(), gold_root)
        )
        if (
            path_is_gold
            or origin.startswith("GOLD")
            or (input_type == "SEED_URL" and value in gold_urls)
        ):
            source_ids.append(input_id)
        if input_type == "QUERY" and value.strip().casefold() in gold_queries:
            query_ids.append(input_id)
        if input_type == "PROMPT_CONTEXT" and any(
            fact_id in value for fact_id in gold_fact_ids
        ):
            fact_ids.append(input_id)
    visibility_count = int(bool(lane) and lane.get("gold_visibility") is not False)
    result = {
        "proof_source": "LIVE_POST_RUN_INPUT_MANIFEST",
        "gold_source_injected_into_production_count": len(source_ids),
        "gold_query_leaked_into_production_count": len(query_ids),
        "gold_fact_leaked_into_production_prompt_count": len(fact_ids),
        "production_lane_gold_visibility_count": visibility_count,
        "source_injection_input_ids": source_ids,
        "query_leak_input_ids": query_ids,
        "fact_leak_input_ids": fact_ids,
    }
    if (
        input_path.exists()
        and lane_path.exists()
        and _file_sha256(input_path)
        == isolation_baseline["production_input_manifest_sha256"]
        and _file_sha256(lane_path)
        == isolation_baseline["production_lane_manifest_sha256"]
    ):
        expected = isolation_baseline["exact_overlap_counts"]
        for key, value in expected.items():
            if int(result[key]) != int(value):
                raise ValueError("tracked pre-Gold isolation proof no longer matches")
        result["proof_source"] = "TRACKED_PRE_GOLD_FINGERPRINT_SNAPSHOT"
    return result


def _validate_isolation_baseline(
    baseline: Mapping[str, Any],
    *,
    queries: Sequence[Mapping[str, Any]],
    sources: Sequence[Mapping[str, Any]],
    facts: Sequence[Mapping[str, Any]],
    target_ids: Sequence[str],
    as_of: date,
) -> None:
    if baseline.get("schema_version") != "e2r_v5_pre_gold_production_isolation_v1":
        raise ValueError("pre-Gold production isolation schema mismatch")
    if baseline.get("baseline_completed_before_gold_research") is not True:
        raise ValueError("pre-Gold production completion is not attested")
    if baseline.get("gold_visibility") is not False:
        raise ValueError("pre-Gold production lane was not blind")
    if baseline.get("gold_research_was_not_input_to_baseline") is not True:
        raise ValueError("Gold research entered the production baseline")
    _require_not_future(str(baseline["production_as_of_date"]), as_of)
    if set(str(value) for value in baseline.get("target_ids") or ()) != set(target_ids):
        raise ValueError("pre-Gold production targets do not match Gold targets")
    expected_hashes = {
        "gold_query_set_sha256": stable_hash(
            sorted(str(row["literal_query"]).strip().casefold() for row in queries)
        ),
        "gold_source_url_set_sha256": stable_hash(
            sorted(str(row["source_url"]) for row in sources)
        ),
        "gold_fact_id_set_sha256": stable_hash(
            sorted(str(row["fact_id"]) for row in facts)
        ),
        "gold_fact_statement_set_sha256": stable_hash(
            sorted(str(row["independent_fact"]) for row in facts)
        ),
    }
    for key, expected in expected_hashes.items():
        if baseline.get(key) != expected:
            raise ValueError(f"pre-Gold isolation fingerprint is stale: {key}")
    counts = baseline.get("exact_overlap_counts") or {}
    required_counts = {
        "gold_source_injected_into_production_count",
        "gold_query_leaked_into_production_count",
        "gold_fact_leaked_into_production_prompt_count",
        "production_lane_gold_visibility_count",
    }
    if set(counts) != required_counts or any(int(value) != 0 for value in counts.values()):
        raise ValueError("pre-Gold production isolation contains leakage")


def _recall(
    rows: Sequence[Mapping[str, Any]], qualified_ids: set[str]
) -> float:
    if not rows:
        return 1.0
    return sum(str(row["fact_id"]) in qualified_ids for row in rows) / len(rows)


def _require_fields(
    row: Mapping[str, Any], required: set[str], label: str
) -> None:
    missing = required - set(row)
    if missing:
        raise ValueError(f"{label} fields missing: {sorted(missing)}")


def _require_unique_rows(
    rows: Sequence[Mapping[str, Any]], key: str
) -> None:
    values = tuple(str(row.get(key) or "") for row in rows)
    _require_unique_values(values, key)


def _require_unique_values(values: Sequence[str], key: str) -> None:
    if any(not value for value in values) or len(values) != len(set(values)):
        raise ValueError(f"{key} must be present and unique")


def _require_not_future(value: str, as_of: date) -> None:
    observed = date.fromisoformat(value[:10])
    if observed > as_of:
        raise ValueError(f"future Gold data is forbidden: {value} > {as_of.isoformat()}")


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _read_json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _read_optional_json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        return {}
    return _read_json(path)


def _read_jsonl(path: Path) -> list[Mapping[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _read_optional_jsonl(path: Path) -> list[Mapping[str, Any]]:
    if not path.exists():
        return []
    return _read_jsonl(path)


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


__all__ = [
    "FullThesisPostRunComparison",
    "PHASE93_AUDIT_PATH",
    "PHASE93_BASELINE_PRODUCTION_ROOT",
    "PHASE93_GOLD_ROOT",
    "PHASE93_OUTPUT_FILES",
    "PHASE93_POST_RUN_FAIL",
    "PHASE93_POST_RUN_PASS",
    "PHASE93_POST_RUN_PENDING",
    "PHASE93_READY",
    "PHASE93_RECALL_THRESHOLDS",
    "PHASE93_SCHEMA_VERSION",
    "PHASE93_SOURCE_FAMILIES",
    "PHASE94_POST_RUN_AUDIT_FILE",
    "PHASE94_PRODUCTION_LANE_FILE",
    "PHASE94_TRACKED_POST_RUN_ROOT",
    "compare_phase93_gold_post_run",
    "compile_phase93_gold_research_recall_audit",
    "gold_authority_leakage_paths",
    "load_phase93_gold_corpus",
    "write_phase93_gold_research_recall_audit",
    "write_phase93_post_run_comparison",
    "write_phase94_tracked_post_run_receipt",
]
