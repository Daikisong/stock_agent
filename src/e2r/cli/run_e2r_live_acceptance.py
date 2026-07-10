"""Run the frozen Phase 36 full live acceptance and deterministic replay."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    run_full_live_acceptance,
    write_full_live_acceptance,
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
    parser.add_argument("--config", default="configs/e2r_live_acceptance_v1.json")
    parser.add_argument("--fail-on-critical", type=_parse_bool, default=True)
    args = parser.parse_args(argv)
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    result = run_full_live_acceptance(config_path=args.config)
    paths = write_full_live_acceptance(
        result,
        output_root=Path(config["output_root"]),
        operational_report_path=Path(config["operational_report_path"]),
        shard_count=int(config["shard_count"]),
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
