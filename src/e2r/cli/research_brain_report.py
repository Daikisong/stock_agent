"""Build Research Brain v1 operational report bundle."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.candidate_context import load_candidate_events_from_korea_live_lite
from e2r.research_brain.memory_acceptance import (
    build_discovery_dry_run_results,
    build_planner_replay_results,
    build_research_brain_acceptance,
)
from e2r.research_brain.memory_leakage_audit import audit_memory_leakage, audit_research_brain_hardcoding
from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.reports import write_research_brain_operational_reports
from e2r.research_brain.runtime_planner import plan_candidate_events


DEFAULT_STORE = "output/research_brain_v1/research_memory_records.jsonl"
DEFAULT_COMPILE_MANIFEST = "output/research_brain_v1/research_memory_compile_manifest.json"
DEFAULT_CANDIDATES = (
    "output/0628_goal2_operational_discovery_dry_run/"
    "korea_live_lite/2024-05-21_candidates.json"
)
DEFAULT_EVIDENCE_OS_REPORT = "docs/operational/evidence_os_v2_acceptance_report.md"
DEFAULT_OUTPUT = "docs/operational"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Research Brain v1 operational report bundle.")
    parser.add_argument("--memory-store", default=DEFAULT_STORE)
    parser.add_argument("--compile-manifest", default=DEFAULT_COMPILE_MANIFEST)
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES)
    parser.add_argument("--evidence-os-report", default=DEFAULT_EVIDENCE_OS_REPORT)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT)
    parser.add_argument("--commit-sha", default=None)
    parser.add_argument("--test-command", default="PYTHONPATH=src python -m unittest discover -s tests -v")
    parser.add_argument("--test-pass-count", type=int, default=0)
    parser.add_argument("--test-fail-count", type=int, default=0)
    parser.add_argument("--test-skip-count", type=int, default=0)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    store = ResearchMemoryStore(args.memory_store)
    records = store.records()
    compile_manifest = _read_json_mapping(Path(args.compile_manifest))
    candidate_events = load_candidate_events_from_korea_live_lite(candidates_path=args.candidates)
    plans = plan_candidate_events(candidate_events=candidate_events, memory_store=store)
    planner_replay = build_planner_replay_results(store)
    discovery = build_discovery_dry_run_results(candidate_events=candidate_events, plans=plans)
    leakage = audit_memory_leakage(records=records, plans=plans)
    hardcoding = audit_research_brain_hardcoding(tuple(Path("src/e2r/research_brain").glob("*.py")))
    evidence_os_summary = _evidence_os_summary(Path(args.evidence_os_report))
    acceptance = build_research_brain_acceptance(
        records=records,
        memory_store=store,
        plans=plans,
        evidence_os_summary=evidence_os_summary,
        discovery_results=discovery,
        planner_replay_results=planner_replay,
    )
    source_route_audit = acceptance["source_route_audit"]
    paths = write_research_brain_operational_reports(
        output_directory=args.output_directory,
        compile_manifest=compile_manifest,
        records=records,
        leakage_audit=leakage,
        planner_replay_results=planner_replay,
        discovery_dry_run_results=discovery,
        source_route_audit=source_route_audit,
        hardcoding_audit=hardcoding,
        evidence_os_summary=evidence_os_summary,
        acceptance=acceptance,
        commit_sha=args.commit_sha or _git_head_sha(),
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
    if not path.exists():
        return {"production_verdict": "MISSING", "production_cutover_ready": False}
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {
        "production_verdict": "READY" if "verdict: READY" in text else "NOT_READY",
        "production_cutover_ready": "verdict: READY" in text,
    }


def _git_head_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
