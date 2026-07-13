"""Compile the Phase 96 all-archetype Researcher Mode audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.researcher_mode import (
    ALL_ARCHETYPE_GENERALIZATION_PASS,
    DEFAULT_GENERALIZATION_AS_OF_DATE,
    DEFAULT_GENERALIZATION_OUTPUT_PATH,
    compile_all_archetype_generalization,
    write_all_archetype_generalization,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--as-of-date", default=DEFAULT_GENERALIZATION_AS_OF_DATE)
    parser.add_argument("--output", default=DEFAULT_GENERALIZATION_OUTPUT_PATH)
    args = parser.parse_args(argv)

    payload = compile_all_archetype_generalization(
        repo_root=args.repo_root,
        as_of_date=args.as_of_date,
    )
    output = Path(args.output)
    if not output.is_absolute():
        output = Path(args.repo_root) / output
    write_all_archetype_generalization(payload, output_path=output)
    print(
        json.dumps(
            {
                "status": payload["status"],
                "critical_count_sum": payload["critical_count_sum"],
                "registry_archetype_count": payload["registry_archetype_count"],
                "mandatory_canaries": payload["mandatory_canaries"],
                "output": str(output),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if payload["status"] == ALL_ARCHETYPE_GENERALIZATION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
