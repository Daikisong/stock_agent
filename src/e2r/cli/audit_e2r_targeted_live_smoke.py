"""Audit frozen Phase 35 smoke leaves without provider calls."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.runtime.live_materialization import (
    audit_targeted_smoke_snapshot,
)


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
    args = parser.parse_args(argv)
    report = audit_targeted_smoke_snapshot(
        config_path=args.config,
        snapshot_root=args.snapshot_root,
        operational_report_path=args.operational_report,
    )
    print(
        json.dumps(
            {
                "status": report["status"],
                "critical_count_sum": report["critical_count_sum"],
                "frozen_snapshot_audit": report["frozen_snapshot_audit"],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if report["critical_count_sum"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
