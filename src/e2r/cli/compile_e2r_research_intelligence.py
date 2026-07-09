"""Compile canonical E2R research intelligence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.compiler import (
    compile_research_intelligence,
    discover_historical_research_paths,
    write_research_intelligence,
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
    args = parser.parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    try:
        inputs = _resolve_inputs(args.input, repo_root=repo_root)
        result = compile_research_intelligence(inputs, repo_root=repo_root)
        output_paths = write_research_intelligence(result, output_root=args.output_root)
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
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    passed = result.manifest["status"] == "RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS"
    return 0 if passed or not args.strict else 2


if __name__ == "__main__":
    raise SystemExit(main())
