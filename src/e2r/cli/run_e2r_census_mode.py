"""Run canonical selective-depth Census on the bounded current-only brain."""

from __future__ import annotations

import argparse
import sys
from typing import Any

from e2r.census.census_runner import CensusRunConfig, run_census_mode
from e2r.cli.run_e2r_current_operation import main as run_current_operation_main


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
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument(
        "--mode",
        choices=("census_light", "census_selective_deep"),
        default="census_selective_deep",
    )
    parser.add_argument("--brain", choices=("canonical_v1",), default="canonical_v1")
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--fail-on-critical", type=_parse_bool, default=True)
    parser.add_argument("--input-manifest")

    # Explicit fixture/backward-compatibility surface. None of these options is
    # consulted by the canonical path.
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--planner-provider", choices=("real", "none"), default="none")
    parser.add_argument("--source-mode", default="live_official_first")
    parser.add_argument("--depth-policy", default="configs/e2r_census_depth_policy_v1.json")
    parser.add_argument("--sla", default="configs/e2r_census_sla_v1.json")
    parser.add_argument("--universe-file")
    parser.add_argument("--fail-on-critical-audit", type=_parse_bool, default=True)
    parser.add_argument("--allow-legacy-v1", action="store_true")
    args = parser.parse_args(argv)
    effective_argv = tuple(argv) if argv is not None else tuple(sys.argv[1:])

    if args.allow_legacy_v1:
        return _run_explicit_legacy_v1(args)

    translated = [
        "--as-of-date",
        args.as_of_date,
        "--mode",
        "production_bounded",
        "--universe",
        args.universe,
        "--output-root",
        args.output_root,
        "--fail-on-critical",
        str(args.fail_on_critical).lower(),
    ]
    if args.input_manifest:
        translated.extend(("--input-manifest", args.input_manifest))
    return run_current_operation_main(
        translated,
        command_name="run_e2r_census_mode",
        manifest_args=_canonical_manifest_args(args),
        recorded_argv=effective_argv,
    )


def _canonical_manifest_args(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "as_of_date": args.as_of_date,
        "mode": args.mode,
        "brain": args.brain,
        "universe": args.universe,
        "output_root": args.output_root,
        "fail_on_critical": args.fail_on_critical,
        "input_manifest": args.input_manifest,
        "allow_legacy_v1": False,
    }


def _run_explicit_legacy_v1(args: argparse.Namespace) -> int:
    if not args.allow_legacy_v1:
        return 2
    result = run_census_mode(
        CensusRunConfig(
            as_of_date=args.as_of_date,
            mode=args.mode,
            universe=args.universe,
            output_root=args.output_root,
            max_symbols=args.max_symbols,
            shard_count=args.shard_count,
            shard_index=args.shard_index,
            planner_provider=args.planner_provider,
            source_mode=args.source_mode,
            depth_policy_path=args.depth_policy,
            sla_path=args.sla,
            universe_file=args.universe_file,
            fail_on_critical_audit=args.fail_on_critical_audit,
        )
    )
    print(result.readiness_verdict["verdict"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
