"""Build Research Brain v2 operational report bundle."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.v2_production_orchestrator import DEFAULT_CANDIDATES_PATH, run_research_brain_v2_shadow
from e2r.research_brain.v2_reports import write_research_brain_v2_report_bundle


DEFAULT_V1_INVENTORY = "docs/operational/research_brain_v1_inventory.json"
DEFAULT_V1_ARCHETYPE_MATRIX = "docs/operational/research_brain_v1_archetype_matrix.json"
DEFAULT_EVIDENCE_OS_REPORT = "docs/operational/evidence_os_v2_acceptance_report.md"
DEFAULT_EVIDENCE_OS_REPLAY = "docs/operational/evidence_os_v2_replay_results.json"
DEFAULT_OUTPUT = "docs/operational"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Research Brain v2 report bundle.")
    parser.add_argument("--v1-inventory", default=DEFAULT_V1_INVENTORY)
    parser.add_argument("--v1-archetype-matrix", default=DEFAULT_V1_ARCHETYPE_MATRIX)
    parser.add_argument("--evidence-os-report", default=DEFAULT_EVIDENCE_OS_REPORT)
    parser.add_argument("--evidence-os-replay", default=DEFAULT_EVIDENCE_OS_REPLAY)
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES_PATH)
    parser.add_argument("--candidate-limit", type=int, default=60)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT)
    parser.add_argument("--test-command", default="PYTHONPATH=src python -m unittest discover -s tests -v")
    parser.add_argument("--test-pass-count", type=int, default=0)
    parser.add_argument("--test-fail-count", type=int, default=0)
    parser.add_argument("--test-skip-count", type=int, default=0)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    v1_inventory = _read_json_mapping(Path(args.v1_inventory))
    v1_matrix = _read_json_mapping(Path(args.v1_archetype_matrix))
    evidence_os_replay = _read_json_mapping(Path(args.evidence_os_replay))
    evidence_os_summary = _evidence_os_summary(Path(args.evidence_os_report))
    result = run_research_brain_v2_shadow(
        v1_inventory=v1_inventory,
        v1_archetype_matrix=v1_matrix,
        evidence_os_replay_results=evidence_os_replay,
        evidence_os_ready=evidence_os_summary.get("production_verdict") == "READY",
        candidates_path=args.candidates,
        candidate_limit=args.candidate_limit,
    )
    paths = write_research_brain_v2_report_bundle(
        result=result,
        output_directory=args.output_directory,
        evidence_os_summary=evidence_os_summary,
        test_summary={
            "command": args.test_command,
            "passed": args.test_pass_count,
            "failed": args.test_fail_count,
            "skipped": args.test_skip_count,
        },
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise TypeError(f"expected JSON object at {path}")
    return data


def _evidence_os_summary(path: Path) -> Mapping[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    ready = "verdict: READY" in text
    return {
        "production_verdict": "READY" if ready else "NOT_READY",
        "production_cutover_ready": ready,
    }


if __name__ == "__main__":
    raise SystemExit(main())
