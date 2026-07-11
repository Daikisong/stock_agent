"""Run Phase 38 known-bad/full tests, independent reviewers, and final verdict."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    compile_final_readiness,
    run_known_bad_detectors,
    run_unittest_command,
    write_final_readiness,
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
    parser.add_argument("--config", default="configs/e2r_live_final_readiness_v1.json")
    parser.add_argument("--run-full-tests", type=_parse_bool, default=True)
    args = parser.parse_args(argv)
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    paths = {key: Path(value) for key, value in config["paths"].items()}
    known_bad = run_known_bad_detectors(
        config=config,
        result_path=paths["known_bad_result"],
        log_path=paths["known_bad_log"],
    )
    if args.run_full_tests:
        run_unittest_command(
            test_ids=(),
            result_path=paths["full_test_result"],
            log_path=paths["full_test_log"],
            full_discovery=True,
        )
    verdict = compile_final_readiness(config_path=args.config)
    output_paths = write_final_readiness(verdict, config_path=args.config)
    print(
        json.dumps(
            {
                "status": verdict["status"],
                "critical_count_sum": verdict["critical_count_sum"],
                "known_bad_status": known_bad["status"],
                "output_paths": {key: str(value) for key, value in output_paths.items()},
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if verdict["hard_acceptance_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
