"""Run E2R Production Cutover Gate v2."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from e2r.production.cutover_v2 import (
    ProductionCutoverV2Config,
    build_production_cutover_v2_bundle,
    write_production_cutover_v2_bundle,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", default=date.today().isoformat())
    parser.add_argument("--planner-provider", default="real")
    parser.add_argument("--candidate-min-count", type=int, default=50)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--validation-output-root", default=None)
    parser.add_argument("--docs-dir", default="docs/operational")
    parser.add_argument("--config-dir", default="configs")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--fetch-a2-live", default="true")
    parser.add_argument("--run-llm-extractor", default="true")
    parser.add_argument("--a2-fetch-limit-per-arch", type=int, default=80)
    parser.add_argument("--llm-extractor-document-limit", type=int, default=50)
    parser.add_argument("--fail-on-critical-audit", default="true")
    args = parser.parse_args(argv)

    output_dir = args.output_dir or f"output/production_cutover_v2/{args.as_of_date}"
    validation_output_root = args.validation_output_root or str(Path(output_dir).parent)
    config = ProductionCutoverV2Config(
        as_of_date=args.as_of_date,
        planner_provider=args.planner_provider,
        candidate_min_count=args.candidate_min_count,
        output_dir=output_dir,
        validation_output_root=validation_output_root,
        fetch_a2_live=str(args.fetch_a2_live).lower() == "true",
        run_llm_extractor=str(args.run_llm_extractor).lower() == "true",
        a2_fetch_limit_per_arch=args.a2_fetch_limit_per_arch,
        llm_extractor_document_limit=args.llm_extractor_document_limit,
    )
    command = " ".join(
        [
            "PYTHONPATH=src",
            "python",
            "-m",
            "e2r.cli.run_e2r_production_cutover_v2",
            "--as-of-date",
            args.as_of_date,
            "--planner-provider",
            args.planner_provider,
            "--candidate-min-count",
            str(args.candidate_min_count),
            "--output-dir",
            output_dir,
            "--validation-output-root",
            validation_output_root,
            "--fetch-a2-live",
            str(args.fetch_a2_live).lower(),
            "--run-llm-extractor",
            str(args.run_llm_extractor).lower(),
            "--a2-fetch-limit-per-arch",
            str(args.a2_fetch_limit_per_arch),
            "--llm-extractor-document-limit",
            str(args.llm_extractor_document_limit),
        ]
    )
    bundle = build_production_cutover_v2_bundle(repo_root=args.repo_root, config=config, command=command)
    paths = write_production_cutover_v2_bundle(
        bundle=bundle,
        docs_dir=args.docs_dir,
        output_dir=output_dir,
        config_dir=args.config_dir,
    )
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
