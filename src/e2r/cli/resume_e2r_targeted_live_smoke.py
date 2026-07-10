"""Resume Phase 35 official acquisition and claims from frozen LLM queries."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.runtime.live_materialization import (
    resume_targeted_smoke_claims,
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
        "--snapshot-root",
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
        print(json.dumps({"status": "TARGETED_SMOKE_RESUME_AUTHORIZATION_REQUIRED"}))
        return 2
    report = resume_targeted_smoke_claims(
        config_path=args.config,
        snapshot_root=args.snapshot_root,
        operational_report_path=args.operational_report,
    )
    print(
        json.dumps(
            {
                "status": report["status"],
                "critical_count_sum": report["critical_count_sum"],
                "resume": report["resume"],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2 if args.fail_on_critical and report["critical_count_sum"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
