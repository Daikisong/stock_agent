"""Compile the frozen 52f09f3 same-corpus semantic repair audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.frozen_corpus_repair import (
    FROZEN_REPAIR_PASS,
    compile_frozen_52f09f3_repair_audit,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default="configs/e2r_frozen_52f09f3_repair_v1.json",
    )
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_frozen_52f09f3_repair_audit.json",
    )
    args = parser.parse_args(argv)
    audit = compile_frozen_52f09f3_repair_audit(config_path=args.config)
    write_json(Path(args.output), audit)
    print(
        json.dumps(
            {
                "status": audit["status"],
                "critical_count_sum": audit["critical_count_sum"],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if audit["status"] == FROZEN_REPAIR_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
