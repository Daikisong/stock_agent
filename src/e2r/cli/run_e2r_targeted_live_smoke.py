"""Run the bounded Phase 35 targeted live smoke."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    run_targeted_live_smoke,
    write_targeted_live_smoke,
)


def _parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean, got {value!r}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default="configs/e2r_targeted_live_smoke_v1.json",
    )
    parser.add_argument(
        "--live-root",
        default="output/live_materialization/2026-07-10",
    )
    parser.add_argument(
        "--current-state",
        default="output/current_state/2026-07-10/current_state_store.jsonl",
    )
    parser.add_argument(
        "--recipes",
        default="output/research_intelligence/v1/recipes/evidence_recipes.jsonl",
    )
    parser.add_argument(
        "--output-root",
        default="output/targeted_smoke/2026-07-10",
    )
    parser.add_argument(
        "--operational-report",
        default="docs/operational/e2r_live_targeted_smoke_report.json",
    )
    parser.add_argument("--live-authorized", type=_parse_bool, default=False)
    parser.add_argument("--fail-on-critical", type=_parse_bool, default=True)
    args = parser.parse_args(argv)
    if not args.live_authorized:
        print(
            json.dumps(
                {
                    "status": "TARGETED_LIVE_SMOKE_AUTHORIZATION_REQUIRED",
                    "live_authorized": False,
                },
                ensure_ascii=False,
            )
        )
        return 2
    result = run_targeted_live_smoke(
        config_path=args.config,
        live_root=args.live_root,
        current_state_path=args.current_state,
        recipe_path=args.recipes,
    )
    paths = write_targeted_live_smoke(
        result,
        output_root=Path(args.output_root),
        operational_report_path=Path(args.operational_report),
    )
    print(
        json.dumps(
            {
                "status": result.status,
                "critical_count_sum": result.report["critical_count_sum"],
                "output_paths": {key: str(value) for key, value in paths.items()},
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2 if args.fail_on_critical and result.report["critical_count_sum"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
