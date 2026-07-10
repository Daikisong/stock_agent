"""Run canonical bounded current E2R operation."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.runtime.current_operation_runner import (
    load_current_operation_runner_input,
    run_current_daily_census,
    write_current_daily_census,
)
from e2r.research_brain.runtime.command_status import reconstruction_pending_payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument(
        "--mode",
        choices=("production_bounded", "test"),
        default="production_bounded",
    )
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--fail-on-critical", default="true")
    parser.add_argument("--input-manifest")
    args = parser.parse_args(argv)
    if args.input_manifest:
        try:
            inputs = load_current_operation_runner_input(args.input_manifest)
            if inputs.as_of_date != args.as_of_date:
                raise ValueError("CLI and input manifest as_of_date differ")
            if args.mode == "production_bounded" and inputs.config.test_mode:
                raise ValueError("test fixture manifest cannot run as production_bounded")
            if args.mode == "test" and not inputs.config.test_mode:
                raise ValueError("production manifest cannot run under test mode")
            result = run_current_daily_census(inputs)
            paths = write_current_daily_census(
                result,
                output_root=args.output_root,
            )
        except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
            print(
                json.dumps(
                    {
                        "schema_version": "e2r_current_operation_cli_v1",
                        "status": "CURRENT_OPERATION_INPUT_REJECTED",
                        "error": str(exc),
                        "production_runtime_ready": False,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            return 2
        print(
            json.dumps(
                {
                    **dict(result.manifest),
                    "output_paths": {
                        key: str(value) for key, value in paths.items()
                    },
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0
    print(
        json.dumps(
            reconstruction_pending_payload(
                command="run_e2r_current_operation",
                required_phase=13,
                inputs=vars(args),
            ),
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
