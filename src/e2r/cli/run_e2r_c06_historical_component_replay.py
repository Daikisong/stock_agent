"""Run blind source-backed C06 component attribution replay."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.replay.c06_component_replay import (
    run_c06_component_replay,
    write_c06_component_replay,
)
from e2r.research_brain.scoring import CodexEvidenceImpactProvider


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config", default="configs/e2r_c06_historical_component_replay_v1.json"
    )
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_c06_historical_component_replay.json",
    )
    args = parser.parse_args(argv)
    provider = CodexEvidenceImpactProvider.default(working_directory=Path.cwd())
    result = run_c06_component_replay(
        config_path=args.config,
        provider=provider,
    )
    output = write_c06_component_replay(result, output_path=args.output)
    print(
        json.dumps(
            {
                "status": result["status"],
                "critical_count_sum": result["critical_count_sum"],
                "case_count": result["case_count"],
                "output": str(output),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if result["critical_count_sum"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
