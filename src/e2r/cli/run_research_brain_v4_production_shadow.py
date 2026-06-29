"""Run Research Brain v4 production shadow."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.v4_production_orchestrator import (
    DEFAULT_V1_ARCHETYPE_MATRIX,
    build_v4_readiness_verdict,
    run_multi_day_shadow_v4,
    run_research_brain_v4_production_shadow,
)
from e2r.research_brain.v4_reports import build_stability_audit_v4, write_research_brain_v4_report_bundle
from e2r.research_brain.v4_schemas import ProductionShadowV4Config
from e2r.research_brain.v4_source_quality_promotion import (
    build_a2_real_replay_claims_sample_v4,
    build_research_memory_usage_audit_v4,
    build_source_quality_promotion_report_v4,
    build_url_repair_queue_v4,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", default=date.today().isoformat())
    parser.add_argument("--planner-provider", default="real", choices=("real", "codex", "codex_cli", "fake", "none"))
    parser.add_argument(
        "--source-acquisition",
        default="frozen_real_source_snapshot",
        choices=("frozen_real_source_snapshot", "live_official_only", "live_full_bounded", "test_fake"),
    )
    parser.add_argument("--universe-limit", type=int, default=40)
    parser.add_argument("--planner-success-limit", type=int, default=10)
    parser.add_argument("--max-fetches-per-task", type=int, default=3)
    parser.add_argument("--top-results", type=int, default=20)
    parser.add_argument("--retry-max", type=int, default=2)
    parser.add_argument("--output-dir", default="docs/operational")
    parser.add_argument("--v1-archetype-matrix", default=str(DEFAULT_V1_ARCHETYPE_MATRIX))
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--allow-fake-provider", action="store_true")
    parser.add_argument("--skip-multi-day", action="store_true")
    parser.add_argument("--test-status", default="not_run_by_cli")
    args = parser.parse_args(argv)

    matrix = _load_json(Path(args.v1_archetype_matrix))
    config = ProductionShadowV4Config(
        as_of_date=args.as_of_date,
        planner_provider=args.planner_provider,
        source_acquisition=args.source_acquisition,
        universe_limit=args.universe_limit,
        planner_success_limit=args.planner_success_limit,
        max_fetches_per_task=args.max_fetches_per_task,
        top_results=args.top_results,
        retry_max=args.retry_max,
        fake_provider_allowed=args.allow_fake_provider,
    )
    result = run_research_brain_v4_production_shadow(
        config=config,
        v1_archetype_matrix=matrix,
        repo_root=args.repo_root,
    )
    if args.skip_multi_day:
        multi_day = {
            "schema_version": "research_brain_v4_multi_day_shadow_runs",
            "summary": {
                "five_day_run_count": 0,
                "real_provider_success_count_total": 0,
                "real_document_fetched_total": 0,
                "accepted_claim_total": 0,
                "deterministic_stage_output_total": 0,
                "fake_provider_used_total": 0,
                "repeated_frozen_run_variance": 0,
                "production_ready_despite_provider_gap": 0,
            },
            "rows": [],
        }
    else:
        multi_day = run_multi_day_shadow_v4(base_config=config, v1_archetype_matrix=matrix, repo_root=args.repo_root)
    stability = build_stability_audit_v4(multi_day)
    result = dict(result)
    result["readiness"] = build_v4_readiness_verdict(
        candidate_report=result["candidate_report"],
        planner_report=result["planner_report"],
        source_report=result["source_acquisition_report"],
        extraction_audit=result["evidence_extraction_audit"],
        watchlist_report=result["watchlist_report"],
        static_audit=result["static_audit"],
        multi_day_shadow=multi_day,
    )
    source_quality = build_source_quality_promotion_report_v4(
        as_of_date=date.fromisoformat(args.as_of_date),
        repo_root=args.repo_root,
    )
    a2_sample = build_a2_real_replay_claims_sample_v4(source_quality)
    repair_queue = build_url_repair_queue_v4(source_quality)
    memory_usage = build_research_memory_usage_audit_v4()
    paths = write_research_brain_v4_report_bundle(
        result=result,
        output_directory=args.output_dir,
        source_quality_promotion=source_quality,
        a2_real_replay_sample=a2_sample,
        url_repair_queue=repair_queue,
        memory_usage_audit=memory_usage,
        multi_day_shadow=multi_day,
        stability_audit=stability,
        as_of_date=args.as_of_date,
        test_summary={
            "command": "PYTHONPATH=src python -m unittest discover -s tests -v",
            "status": args.test_status,
        },
    )
    print(json.dumps({"status": result["readiness"]["summary"]["final_status"], "paths": {k: str(v) for k, v in paths.items()}}, ensure_ascii=False, indent=2))
    return 0


def _load_json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
