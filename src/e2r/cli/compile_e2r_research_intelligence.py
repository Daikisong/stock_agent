"""Compile canonical E2R research intelligence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    discover_historical_research_paths,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
    write_case_level_source_verification,
    write_research_intelligence,
)
from e2r.research_brain.recipes import (
    compile_evidence_recipe_os,
    write_evidence_recipe_os,
)
from e2r.research_brain.retrieval import (
    compile_semantic_memory_graph,
    evaluate_balanced_retrieval,
    load_blind_retrieval_benchmark,
    write_balanced_retrieval_benchmark,
    write_semantic_memory_graph,
)


_SUPPORTED_SUFFIXES = {".md", ".json", ".jsonl", ".csv"}


def _parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean, got {value!r}")


def _resolve_inputs(values: list[str], *, repo_root: Path) -> tuple[Path, ...]:
    if not values:
        return discover_historical_research_paths(repo_root)
    paths: dict[str, Path] = {}
    for value in values:
        candidate = Path(value)
        candidate = candidate if candidate.is_absolute() else repo_root / candidate
        if candidate.is_dir():
            discovered = (
                path
                for path in candidate.rglob("*")
                if path.is_file() and path.suffix.lower() in _SUPPORTED_SUFFIXES
            )
        else:
            discovered = (candidate,)
        for path in discovered:
            if not path.is_file():
                raise FileNotFoundError(path)
            if path.suffix.lower() not in _SUPPORTED_SUFFIXES:
                raise ValueError(f"unsupported research artifact: {path}")
            paths[path.resolve().as_posix()] = path
    return tuple(sorted(paths.values(), key=lambda path: path.as_posix()))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-root", required=True)
    parser.add_argument(
        "--input",
        action="append",
        default=[],
        help="research file or directory; repeatable (default: canonical V12 registry)",
    )
    parser.add_argument("--strict", type=_parse_bool, default=True)
    parser.add_argument(
        "--snapshot-registry",
        help="canonical historical provider snapshot JSONL",
    )
    parser.add_argument(
        "--case-source-links",
        help="verified historical case/source link JSONL",
    )
    parser.add_argument(
        "--recipe-semantics",
        help="reviewed EvidenceRecipe semantic definition JSON (default: canonical config)",
    )
    parser.add_argument(
        "--retrieval-benchmark",
        help="evaluator-only blind semantic retrieval benchmark JSONL",
    )
    args = parser.parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    try:
        inputs = _resolve_inputs(args.input, repo_root=repo_root)
        result = compile_research_intelligence(inputs, repo_root=repo_root)
        output_paths = write_research_intelligence(result, output_root=args.output_root)
        snapshots = (
            load_historical_provider_snapshots(
                _resolve_optional_path(args.snapshot_registry, repo_root=repo_root)
            )
            if args.snapshot_registry
            else ()
        )
        case_source_links = (
            load_historical_case_source_links(
                _resolve_optional_path(args.case_source_links, repo_root=repo_root)
            )
            if args.case_source_links
            else ()
        )
        source_result = compile_case_level_source_verification(
            result.cases,
            snapshots=snapshots,
            case_source_links=case_source_links,
            repo_root=repo_root,
        )
        source_output_paths = write_case_level_source_verification(
            source_result,
            output_root=args.output_root,
        )
        recipe_result = compile_evidence_recipe_os(
            result.cases,
            source_verifications=source_result.verifications,
            semantics_path=(
                _resolve_optional_path(args.recipe_semantics, repo_root=repo_root)
                if args.recipe_semantics
                else None
            )
            or _default_recipe_semantics_path(),
        )
        recipe_output_paths = write_evidence_recipe_os(
            recipe_result,
            output_root=args.output_root,
        )
        memory_result = compile_semantic_memory_graph(
            result.cases,
            recipe_result.recipes,
            source_verifications=source_result.verifications,
        )
        memory_output_paths = write_semantic_memory_graph(
            memory_result,
            output_root=args.output_root,
        )
        retrieval_benchmark = load_blind_retrieval_benchmark(
            _resolve_optional_path(args.retrieval_benchmark, repo_root=repo_root)
            if args.retrieval_benchmark
            else None
        )
        retrieval_audit = evaluate_balanced_retrieval(
            memory_result.index,
            retrieval_benchmark,
        )
        retrieval_output_paths = write_balanced_retrieval_benchmark(
            retrieval_audit,
            output_root=args.output_root,
        )
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(
            json.dumps(
                {
                    "command": "compile_e2r_research_intelligence",
                    "status": "RESEARCH_CORPUS_SEMANTIC_COMPILER_ERROR",
                    "error": f"{type(exc).__name__}: {exc}",
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 2

    payload = {
        "command": "compile_e2r_research_intelligence",
        "status": result.manifest["status"],
        "input_artifact_count": len(inputs),
        "historical_case_count": len(result.cases),
        "historical_outcome_count": len(result.outcomes),
        "historical_rule_count": len(result.rules),
        "quarantine_count": len(result.quarantine),
        "linkage_error_count": len(result.linkage_errors),
        "critical_count_sum": result.manifest["critical_count_sum"],
        "output_paths": {key: str(path) for key, path in output_paths.items()},
        "source_verification_status": source_result.manifest["status"],
        "historical_replay_ready_count": source_result.manifest[
            "historical_replay_ready_count"
        ],
        "source_repair_task_count": source_result.manifest["repair_task_count"],
        "source_verification_critical_count_sum": source_result.manifest[
            "critical_count_sum"
        ],
        "source_verification_output_paths": {
            key: str(path) for key, path in source_output_paths.items()
        },
        "evidence_recipe_status": recipe_result.manifest["status"],
        "executable_recipe_count": recipe_result.manifest["executable_recipe_count"],
        "explicit_unsupported_recipe_count": recipe_result.manifest[
            "explicit_unsupported_count"
        ],
        "evidence_recipe_critical_count_sum": recipe_result.manifest[
            "critical_count_sum"
        ],
        "evidence_recipe_output_paths": {
            key: str(path) for key, path in recipe_output_paths.items()
        },
        "semantic_memory_status": memory_result.manifest["status"],
        "semantic_memory_node_count": memory_result.manifest["node_count"],
        "semantic_memory_edge_count": memory_result.manifest["edge_count"],
        "semantic_memory_critical_count_sum": memory_result.manifest[
            "critical_count_sum"
        ],
        "semantic_memory_output_paths": {
            key: str(path) for key, path in memory_output_paths.items()
        },
        "balanced_retrieval_status": retrieval_audit.manifest["status"],
        "top3_archetype_hit_rate": retrieval_audit.manifest[
            "top3_archetype_hit_rate"
        ],
        "required_recipe_hit_rate": retrieval_audit.manifest[
            "required_recipe_hit_rate"
        ],
        "positive_guard_pair_rate": retrieval_audit.manifest[
            "positive_guard_pair_rate"
        ],
        "balanced_retrieval_critical_count_sum": retrieval_audit.manifest[
            "critical_count_sum"
        ],
        "balanced_retrieval_output_paths": {
            key: str(path) for key, path in retrieval_output_paths.items()
        },
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    passed = (
        result.manifest["status"] == "RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS"
        and source_result.manifest["status"]
        == "CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_PASS"
        and recipe_result.manifest["status"] == "EVIDENCE_RECIPE_OS_COMPILER_PASS"
        and memory_result.manifest["status"]
        == "SEMANTIC_MEMORY_GRAPH_COMPILER_PASS"
        and retrieval_audit.manifest["status"]
        == "BALANCED_SEMANTIC_RETRIEVAL_PASS"
    )
    return 0 if passed or not args.strict else 2


def _resolve_optional_path(value: str, *, repo_root: Path) -> Path:
    path = Path(value)
    path = path if path.is_absolute() else repo_root / path
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def _default_recipe_semantics_path() -> Path:
    return Path(__file__).resolve().parents[3] / "configs" / "e2r_evidence_recipe_semantics_v1.json"


if __name__ == "__main__":
    raise SystemExit(main())
