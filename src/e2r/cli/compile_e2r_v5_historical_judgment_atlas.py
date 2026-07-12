"""Compile the full registered research corpus into the E2R v5 Judgment Atlas."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.researcher_mode import (
    compile_historical_judgment_atlas,
    write_historical_judgment_atlas,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output-root",
        default="output/researcher_parity/judgment_atlas",
    )
    parser.add_argument(
        "--audit-output",
        default="docs/operational/e2r_v5_historical_judgment_atlas_audit.json",
    )
    args = parser.parse_args(argv)
    result = compile_historical_judgment_atlas(repo_root=args.repo_root)
    paths = write_historical_judgment_atlas(
        result,
        output_root=args.output_root,
        audit_path=args.audit_output,
    )
    print(
        json.dumps(
            {
                "status": result.audit["status"],
                "critical_count_sum": result.audit["critical_count_sum"],
                "judgment_count": result.audit["judgment_count"],
                "score_anchor_count": result.audit["score_anchor_count"],
                "registry_archetype_coverage_rate": result.audit[
                    "registry_archetype_coverage_rate"
                ],
                "paths": {key: str(path) for key, path in paths.items()},
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if result.audit["critical_count_sum"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
