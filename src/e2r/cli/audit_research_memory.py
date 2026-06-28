"""Audit Research Brain v1 memory for leakage and hardcoding."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.memory_leakage_audit import audit_memory_leakage, audit_research_brain_hardcoding
from e2r.research_brain.memory_store import ResearchMemoryStore


DEFAULT_STORE = "output/research_brain_v1/research_memory_records.jsonl"
DEFAULT_OUTPUT = "output/research_brain_v1"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit Research Brain v1 memory.")
    parser.add_argument("--memory-store", default=DEFAULT_STORE)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    store = ResearchMemoryStore(args.memory_store)
    records = store.records()
    leakage = audit_memory_leakage(records=records)
    hardcoding = audit_research_brain_hardcoding(tuple(Path("src/e2r/research_brain").glob("*.py")))
    output_dir = Path(args.output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    leakage_path = output_dir / "research_brain_leakage_audit.json"
    hardcoding_path = output_dir / "research_brain_hardcoding_audit.json"
    leakage_path.write_text(json.dumps(leakage, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    hardcoding_path.write_text(json.dumps(hardcoding, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"leakage_audit={leakage_path}")
    print(f"hardcoding_audit={hardcoding_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
