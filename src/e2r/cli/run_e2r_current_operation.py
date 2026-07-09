"""Run canonical bounded current E2R operation."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.runtime.command_status import reconstruction_pending_payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--mode", default="production_bounded")
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--fail-on-critical", default="true")
    args = parser.parse_args(argv)
    print(
        json.dumps(
            reconstruction_pending_payload(
                command="run_e2r_current_operation",
                required_phase=11,
                inputs=vars(args),
            ),
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
