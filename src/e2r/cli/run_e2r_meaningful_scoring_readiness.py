"""Compile the canonical leaf-backed E2R scoring readiness verdict."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.scoring.scoring_readiness import (
    compile_meaningful_scoring_readiness,
    write_meaningful_scoring_readiness,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config", default="configs/e2r_meaningful_scoring_readiness_v3.json"
    )
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_meaningful_scoring_readiness_v3.md",
    )
    parser.add_argument("--verify-repository", action="store_true")
    args = parser.parse_args(argv)
    verdict = compile_meaningful_scoring_readiness(
        config_path=args.config, verify_repository=args.verify_repository
    )
    output = write_meaningful_scoring_readiness(verdict, output_path=args.output)
    print(
        json.dumps(
            {
                "status": verdict["status"],
                "critical_count_sum": verdict["critical_count_sum"],
                "blockers": verdict["blockers"],
                "output": str(output),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if verdict["hard_acceptance_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
