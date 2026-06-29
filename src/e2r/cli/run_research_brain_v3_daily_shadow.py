"""Run Research Brain v3 production-shadow daily pipeline."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence

from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix
from e2r.research_brain.v3_memory_cards import (
    build_memory_card_conflicts_report_v3,
    build_memory_card_distillation_report_v3,
    distill_memory_cards_v3,
)
from e2r.research_brain.v3_production_orchestrator import (
    build_v3_readiness_verdict,
    load_v1_archetype_matrix,
    run_five_day_frozen_shadow_v3,
    run_research_brain_v3_daily_shadow,
    select_planner_provider,
)
from e2r.research_brain.v3_reports import write_research_brain_v3_report_bundle
from e2r.research_brain.v3_source_quality import (
    build_a2_promoted_claims_sample_v3,
    build_source_quality_promotion_report_v3,
    build_url_repair_failures_v3,
)
from e2r.research_brain.v3_static_audit import build_static_logic_audit_v3


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Research Brain v3 daily shadow pipeline.")
    parser.add_argument("--as-of-date", default="2026-06-29")
    parser.add_argument("--universe-limit", type=int, default=40)
    parser.add_argument("--sector-min-events", type=int, default=3)
    parser.add_argument("--candidate-event-min-count", type=int, default=30)
    parser.add_argument("--output-dir", default="docs/operational")
    parser.add_argument("--fixture-mode", action="store_true", default=False)
    parser.add_argument("--live-mode", action="store_true", default=False)
    parser.add_argument("--frozen-mode", action="store_true", default=True)
    parser.add_argument("--planner-provider", choices=("real", "fake", "none"), default="none")
    parser.add_argument("--source-acquisition", choices=("live", "snapshot", "frozen"), default="snapshot")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    as_of = date.fromisoformat(args.as_of_date)
    matrix = load_v1_archetype_matrix()
    provider = select_planner_provider(args.planner_provider)
    source_mode = "snapshot" if args.source_acquisition == "frozen" else args.source_acquisition
    result = run_research_brain_v3_daily_shadow(
        as_of_date=as_of,
        v1_archetype_matrix=matrix,
        planner_provider=provider,
        universe_limit=args.universe_limit,
        source_acquisition_mode=source_mode,
    )
    frozen = run_five_day_frozen_shadow_v3(
        base_as_of_date=as_of,
        v1_archetype_matrix=matrix,
        planner_provider=provider,
    )
    result = dict(result)
    result["readiness"] = build_v3_readiness_verdict(
        candidate_report=result["candidate_report"],
        planner_report=result["planner_report"],
        source_task_audit=result["source_task_audit"],
        watchlist_report=result["watchlist_report"],
        raw_router_matrix=result["raw_router_matrix"],
        frozen_daily_run_count=frozen["summary"]["frozen_daily_run_count"],
    )
    source_quality = build_source_quality_promotion_report_v3(as_of_date=as_of)
    url_failures = build_url_repair_failures_v3(source_quality)
    a2_sample = build_a2_promoted_claims_sample_v3(source_quality)
    v3_cards = distill_memory_cards_v3(build_memory_cards_from_v1_matrix(matrix))
    memory_report = build_memory_card_distillation_report_v3(v3_cards)
    memory_conflicts = build_memory_card_conflicts_report_v3(v3_cards)
    stability = {
        "schema_version": "research_brain_v3_stability_audit",
        "summary": {
            "frozen_daily_run_count": frozen["summary"]["frozen_daily_run_count"],
            "max_repeat_variance_count": frozen["summary"]["max_repeat_variance_count"],
            "no_score_stage_variance": frozen["summary"]["no_score_stage_variance"],
        },
        "rows": frozen["rows"],
    }
    static_audit = build_static_logic_audit_v3(
        result=result,
        source_quality_promotion=source_quality,
        frozen_daily_runs=frozen,
    )
    paths = write_research_brain_v3_report_bundle(
        result=result,
        output_directory=Path(args.output_dir),
        source_quality_promotion=source_quality,
        url_repair_failures=url_failures,
        a2_promoted_sample=a2_sample,
        memory_distillation=memory_report,
        memory_conflicts=memory_conflicts,
        static_audit=static_audit,
        frozen_daily_runs=frozen,
        stability_audit=stability,
        as_of_date=as_of.isoformat(),
        test_summary={"command": "PYTHONPATH=src python -m unittest discover -s tests -v", "status": "not_run_by_cli"},
    )
    for key, path in sorted(paths.items()):
        print(f"{key}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
