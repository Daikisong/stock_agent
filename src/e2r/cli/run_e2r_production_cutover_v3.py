"""Run E2R Production Cutover Gate v3."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from e2r.production.cutover_v3 import (
    ProductionCutoverV3Config,
    build_production_cutover_v3_bundle,
    write_production_cutover_v3_bundle,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", default=date.today().isoformat())
    parser.add_argument("--planner-provider", default="real")
    parser.add_argument("--candidate-min-count", type=int, default=20)
    parser.add_argument("--live-shadow-days", type=int, default=5)
    parser.add_argument("--frozen-replay-days", type=int, default=10)
    parser.add_argument("--repeated-frozen-days", type=int, default=3)
    parser.add_argument("--output-root", default="output/production_cutover_v3")
    parser.add_argument("--validation-output-root", default=None)
    parser.add_argument("--docs-dir", default="docs/operational")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--fetch-a2-live", default="true")
    parser.add_argument("--run-llm-extractor", default="true")
    parser.add_argument("--a2-fetch-limit-per-arch", type=int, default=80)
    parser.add_argument("--llm-extractor-document-limit", type=int, default=50)
    parser.add_argument("--final-cutover-approved", default="false")
    parser.add_argument("--fail-on-critical-audit", default="true")
    args = parser.parse_args(argv)

    validation_root = args.validation_output_root or args.output_root
    config = ProductionCutoverV3Config(
        as_of_date=args.as_of_date,
        planner_provider=args.planner_provider,
        candidate_min_count=args.candidate_min_count,
        live_shadow_days=args.live_shadow_days,
        frozen_replay_days=args.frozen_replay_days,
        repeated_frozen_days=args.repeated_frozen_days,
        output_root=args.output_root,
        validation_output_root=validation_root,
        fetch_a2_live=str(args.fetch_a2_live).lower() == "true",
        run_llm_extractor=str(args.run_llm_extractor).lower() == "true",
        a2_fetch_limit_per_arch=args.a2_fetch_limit_per_arch,
        llm_extractor_document_limit=args.llm_extractor_document_limit,
        final_cutover_approved=str(args.final_cutover_approved).lower() == "true",
    )
    command = " ".join(
        [
            "PYTHONPATH=src",
            "python",
            "-m",
            "e2r.cli.run_e2r_production_cutover_v3",
            "--as-of-date",
            args.as_of_date,
            "--planner-provider",
            args.planner_provider,
            "--candidate-min-count",
            str(args.candidate_min_count),
            "--live-shadow-days",
            str(args.live_shadow_days),
            "--output-root",
            args.output_root,
        ]
    )
    bundle = build_production_cutover_v3_bundle(repo_root=args.repo_root, config=config, command=command)
    paths = write_production_cutover_v3_bundle(bundle=bundle, docs_dir=args.docs_dir, output_root=Path(args.output_root))
    result = {
        "production_verdict": bundle["verdict"]["production_verdict"],
        "production_ready": bundle["verdict"]["production_ready"],
        "labels": bundle["labels"],
        "blockers": bundle["verdict"]["blockers"],
        "static_critical_count_sum": bundle["static_logic_audit"]["summary"]["critical_count_sum"],
        "paths": paths,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    if str(args.fail_on_critical_audit).lower() == "true" and bundle["static_logic_audit"]["summary"]["critical_count_sum"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
