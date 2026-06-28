"""Run Research Brain v1 discovery dry run from candidate events."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.candidate_context import load_candidate_events_from_korea_live_lite
from e2r.research_brain.memory_acceptance import build_discovery_dry_run_results
from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.runtime_planner import plan_candidate_events


DEFAULT_STORE = "output/research_brain_v1/research_memory_records.jsonl"
DEFAULT_CANDIDATES = (
    "output/0628_goal2_operational_discovery_dry_run/"
    "korea_live_lite/2024-05-21_candidates.json"
)
DEFAULT_OUTPUT = "output/research_brain_v1"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Research Brain discovery dry run with targeted_smoke_only=false.")
    parser.add_argument("--memory-store", default=DEFAULT_STORE)
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int, default=None)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    store = ResearchMemoryStore(args.memory_store)
    events = load_candidate_events_from_korea_live_lite(candidates_path=args.candidates)
    selected = tuple(events if args.limit is None else events[: args.limit])
    plans = plan_candidate_events(candidate_events=selected, memory_store=store)
    results = build_discovery_dry_run_results(candidate_events=selected, plans=plans)
    output_dir = Path(args.output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "research_brain_discovery_dry_run_results.json"
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"discovery_dry_run={output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
