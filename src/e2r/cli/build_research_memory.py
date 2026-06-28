"""Build Research Brain v1 memory store from repository artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.memory_compiler import compile_research_memory


DEFAULT_STORE = "output/research_brain_v1/research_memory_records.jsonl"
DEFAULT_OUTPUT = "output/research_brain_v1"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compile Research Brain v1 memory records.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--memory-store", default=DEFAULT_STORE)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT)
    parser.add_argument("--max-rows-per-artifact", type=int, default=200)
    parser.add_argument("--max-total-compiled-rows", type=int, default=50000)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    manifest = compile_research_memory(
        repo_root=args.repo_root,
        output_store_path=args.memory_store,
        max_rows_per_artifact=args.max_rows_per_artifact,
        max_total_compiled_rows=args.max_total_compiled_rows,
    )
    output_dir = Path(args.output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "research_memory_compile_manifest.json"
    output_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"compile_manifest={output_path}")
    print(f"memory_store={args.memory_store}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
