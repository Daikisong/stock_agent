"""Run Research Brain v1 planner replay."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.memory_acceptance import build_planner_replay_results
from e2r.research_brain.memory_store import ResearchMemoryStore


DEFAULT_STORE = "output/research_brain_v1/research_memory_records.jsonl"
DEFAULT_OUTPUT = "output/research_brain_v1"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run C06/C08/C15/C17/C24/C28 Research Brain planner replay.")
    parser.add_argument("--memory-store", default=DEFAULT_STORE)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    store = ResearchMemoryStore(args.memory_store)
    results = build_planner_replay_results(store)
    output_dir = Path(args.output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "research_brain_planner_replay_results.json"
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"planner_replay={output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
