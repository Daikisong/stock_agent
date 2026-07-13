"""Compile the Phase 97 daily Census/Researcher Mode integration audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.researcher_mode.daily_census_integration import (
    DAILY_CENSUS_INTEGRATION_PASS,
    DEFAULT_DAILY_CENSUS_INTEGRATION_OUTPUT_PATH,
    compile_phase97_daily_census_integration_audit,
    write_phase97_daily_census_integration_audit,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=DEFAULT_DAILY_CENSUS_INTEGRATION_OUTPUT_PATH)
    args = parser.parse_args(argv)

    payload = compile_phase97_daily_census_integration_audit()
    path = write_phase97_daily_census_integration_audit(
        payload,
        output_path=Path(args.output),
    )
    print(
        json.dumps(
            {
                "status": payload["status"],
                "critical_count_sum": payload["critical_count_sum"],
                "output": str(path),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if payload["status"] == DAILY_CENSUS_INTEGRATION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
