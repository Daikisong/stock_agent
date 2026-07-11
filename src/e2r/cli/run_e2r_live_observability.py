"""Compile Phase 37 live conversion, SLA, and provider reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    compile_live_observability,
    write_live_observability,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/e2r_live_observability_v1.json")
    args = parser.parse_args(argv)
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    reports = compile_live_observability(config_path=args.config)
    paths = write_live_observability(
        reports,
        output_paths=config["output_paths"],
    )
    critical = max(
        int(report.get("critical_count_sum") or 0) for report in reports.values()
    )
    print(
        json.dumps(
            {
                "status": {key: value["status"] for key, value in reports.items()},
                "critical_count_sum": critical,
                "output_paths": {key: str(value) for key, value in paths.items()},
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2 if critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
