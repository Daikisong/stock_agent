"""Run the isolated Phase 94 current Researcher Mode checkpoint until semantic pass."""

from __future__ import annotations

import argparse
from datetime import date, timedelta
import json
from pathlib import Path
import re

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.researcher_mode import (
    PHASE93_POST_RUN_PASS,
    CurrentResearcherModeConfig,
    CurrentResearcherModeTargetRunner,
    compare_phase93_gold_post_run,
    load_current_research_targets,
    write_phase93_post_run_comparison,
    write_production_lane,
)


def _bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().casefold()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean, got {value!r}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--symbols", required=True)
    parser.add_argument("--archetype", required=True)
    parser.add_argument("--live-materialization-authorized", type=_bool, required=True)
    parser.add_argument("--checkpoint-resume", type=_bool, required=True)
    parser.add_argument("--gold-lane-isolated", type=_bool, required=True)
    parser.add_argument("--require-researcher-parity", type=_bool, required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument(
        "--target-registry",
        default="configs/e2r_targeted_live_smoke_v1.json",
    )
    parser.add_argument("--latest-trading-snapshot-date")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    symbols = tuple(
        dict.fromkeys(
            value.strip() for value in args.symbols.split(",") if value.strip()
        )
    )
    if not symbols:
        raise ValueError("--symbols must contain at least one symbol")
    targets = load_current_research_targets(
        symbols=symbols,
        registry_path=args.target_registry,
        as_of_date=args.as_of_date,
    )
    trading_date = (
        args.latest_trading_snapshot_date
        or _latest_calendar_trading_candidate(args.as_of_date)
    )
    config = CurrentResearcherModeConfig(
        as_of_date=args.as_of_date,
        archetype_id=args.archetype,
        output_root=args.output_root,
        live_materialization_authorized=args.live_materialization_authorized,
        checkpoint_resume=args.checkpoint_resume,
        gold_lane_isolated=args.gold_lane_isolated,
        require_researcher_parity=args.require_researcher_parity,
        latest_trading_snapshot_date=trading_date,
    )
    output_root = Path(config.output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    # This manifest is closed before any target production call.  No Gold
    # module is touched until every production target reports completion.
    write_json(
        output_root / "production_lane_manifest.json",
        {
            "schema_version": "e2r_v5_phase94_production_lane_v1",
            "status": "PRODUCTION_RESEARCH_RUNNING",
            "as_of_date": config.as_of_date,
            "archetype_id": config.archetype_id,
            "target_ids": [target.target_id for target in targets],
            "gold_visibility": False,
            "gold_query_visibility": False,
            "gold_url_visibility": False,
            "gold_fact_visibility": False,
            "comparison_timing": "POST_RUN_ONLY",
            "completion_based_on_fixed_rounds": False,
            "latest_trading_snapshot_date": trading_date,
            "latest_trading_snapshot_verification": (
                "CALENDAR_CANDIDATE_PENDING_STRUCTURED_KRX_CONFIRMATION"
            ),
        },
    )
    runner = CurrentResearcherModeTargetRunner()
    runs = tuple(
        _run_target_until_semantic_terminal(
            runner=runner,
            config=config,
            target=target,
        )
        for target in targets
    )
    paths = write_production_lane(config=config, target_runs=runs)
    production_complete = all(
        run.status == "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
        for run in runs
    )
    post_run_status = "PENDING_PRODUCTION_RESEARCH_COMPLETION"
    gold_critical_fact_miss_count = None
    if production_complete:
        # Deliberately imported data access happens only now, after the clean
        # production files and lane manifest have been closed.
        comparison = compare_phase93_gold_post_run(
            production_root=output_root,
        )
        write_phase93_post_run_comparison(
            result=comparison,
            comparison_path=output_root / "gold_fact_comparison.jsonl",
            audit_path=output_root / "post_run_gold_recall_audit.json",
        )
        post_run_status = comparison.status
        gold_critical_fact_miss_count = comparison.audit["critical_counts"].get(
            "critical_material_fact_recall_below_threshold_count"
        )
    else:
        write_json(
            output_root / "post_run_gold_recall_audit.json",
            {
                "schema_version": "e2r_v5_phase94_post_run_gold_pending_v1",
                "status": post_run_status,
                "as_of_date": config.as_of_date,
                "gold_visibility_during_production": False,
                "comparison_executed": False,
                "reason": "7/7 component, structured data, judges, and supervisor gates are not complete.",
            },
        )
    complete = production_complete and post_run_status == PHASE93_POST_RUN_PASS
    summary = {
        "status": (
            "PHASE94_CURRENT_RESEARCHER_MODE_PASS"
            if complete
            else "PHASE94_CURRENT_RESEARCHER_MODE_PENDING"
        ),
        "as_of_date": config.as_of_date,
        "latest_trading_snapshot_date": trading_date,
        "target_statuses": {
            run.target.target_id: run.status for run in runs
        },
        "target_completion_gates": {
            run.target.target_id: dict(run.completion_gates) for run in runs
        },
        "production_research_complete": production_complete,
        "post_run_gold_status": post_run_status,
        "gold_critical_fact_miss_count": gold_critical_fact_miss_count,
        "gold_visibility_during_production": False,
        "completion_based_on_fixed_rounds": False,
        "production_lane_manifest": str(paths["lane"]),
    }
    write_json(output_root / "phase94_run_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if complete else 2


def _latest_calendar_trading_candidate(as_of_date: str) -> str:
    value = date.fromisoformat(as_of_date)
    while value.weekday() >= 5:
        value -= timedelta(days=1)
    return value.isoformat()


def _run_target_until_semantic_terminal(*, runner, config, target):
    """Resume checkpoints until pass or an unchanged semantic state.

    There is intentionally no round limit.  An unchanged state is a pending
    checkpoint/blocker, never research completion or source absence.
    """

    seen_signatures: set[str] = set()
    while True:
        result = runner.run_checkpoint(config=config, target=target)
        signature = _semantic_signature(result)
        progress_path = Path(config.output_root) / target.target_id / "until_pass_progress.json"
        write_json(
            progress_path,
            {
                "schema_version": "e2r_v5_phase94_until_pass_progress_v1",
                "target_id": target.target_id,
                "status": result.status,
                "semantic_signature": signature,
                "seen_semantic_state_count": len(seen_signatures) + 1,
                "completion_based_on_fixed_rounds": False,
                "transport_budget_treated_as_completion": False,
                "completion_gates": dict(result.completion_gates),
            },
        )
        if result.status == "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD":
            return result
        if signature in seen_signatures:
            write_json(
                Path(config.output_root)
                / target.target_id
                / "semantic_no_progress_checkpoint.json",
                {
                    "schema_version": "e2r_v5_phase94_semantic_no_progress_v1",
                    "status": "RESEARCH_PENDING_NO_NEW_SEMANTIC_STATE",
                    "target_id": target.target_id,
                    "semantic_signature": signature,
                    "research_complete": False,
                    "source_absence_proven": False,
                    "score_valid": False,
                    "completion_based_on_fixed_rounds": False,
                    "next_action": (
                        "repair provider/source/parser/structured route or feed the "
                        "supervisor failure class back to the LLM query planner"
                    ),
                },
            )
            return result
        seen_signatures.add(signature)


def _semantic_signature(result) -> str:
    source = result.source_graph.checkpoint
    return stable_hash(
        {
            "query_states": sorted(
                (
                    str(row.get("literal_query") or "").casefold(),
                    str(row.get("execution_status") or ""),
                )
                for row in source.get("generated_queries") or ()
            ),
            "candidate_states": sorted(
                (
                    str(row.get("candidate_id") or ""),
                    str(row.get("ranking_status") or ""),
                    str(row.get("fetch_status") or ""),
                )
                for row in source.get("search_candidates") or ()
            ),
            "source_failure_states": sorted(
                (
                    str(row.get("query_id") or ""),
                    str(row.get("candidate_id") or ""),
                    str(row.get("failure_stage") or ""),
                    _semantic_failure_reason(
                        str(row.get("failure_reason") or "")
                    ),
                    bool(row.get("alternate_route_required")),
                )
                for row in source.get("query_failures") or ()
            ),
            "document_ids": sorted(
                str(row.get("document_id") or "")
                for row in result.source_graph.evidence_documents
            ),
            "source_graph_status": result.source_graph.status,
            "fact_extraction_status": result.fact_extraction.status,
            "fact_extraction_pending": sorted(
                _semantic_failure_reason(reason)
                for reason in result.fact_extraction.pending_reasons
            ),
            "fact_ids": sorted(row.fact_id for row in result.fact_extraction.facts),
            "component_states": [
                (
                    row.component_id,
                    row.status,
                    tuple(
                        _semantic_failure_reason(reason)
                        for reason in row.pending_reasons
                    ),
                )
                for row in result.dossier.component_results
            ],
            "structured_status": result.structured_result.status,
            "structured_record_ids": sorted(
                row.record_id for row in result.structured_result.records
            ),
            "aggregation_status": result.score_aggregation.status,
            "aggregation_pending": [
                _semantic_failure_reason(reason)
                for reason in result.score_aggregation.pending_reasons
            ],
            "stagecourt_status": getattr(
                getattr(result, "stagecourt", None),
                "decision",
                None,
            ).status
            if getattr(getattr(result, "stagecourt", None), "decision", None)
            is not None
            else "LEGACY_STAGECOURT_NOT_PRESENT",
            "supervisor_status": result.research_epoch.supervisor_review.status,
        }
    )


def _semantic_failure_reason(reason: str) -> str:
    """Remove transport noise that cannot represent new research semantics."""

    value = " ".join(str(reason).split())
    folded = value.casefold()
    prefix = value.split(":", 2)[:2]
    stable_prefix = ":".join(prefix)
    if "usage limit" in folded or "purchase more credits" in folded:
        return f"{stable_prefix}:PROVIDER_USAGE_LIMIT"
    if "timed out" in folded or "timeouterror" in folded:
        return f"{stable_prefix}:PROVIDER_TIMEOUT"
    if any(
        marker in folded
        for marker in (
            "missing credential",
            "missing api key",
            "api_key is required",
            "authentication failed",
        )
    ):
        return f"{stable_prefix}:PROVIDER_CREDENTIAL_MISSING"
    # Provider transports create a fresh temporary directory on each call.
    # Its name and a retry timestamp are runtime noise, not evidence progress.
    value = re.sub(
        r"/tmp/e2r_structured_provider_[^/\s]+",
        "/tmp/e2r_structured_provider_<TMP>",
        value,
    )
    value = re.sub(
        r"try again at [A-Za-z]{3} \d{1,2}(?:st|nd|rd|th), \d{4} [0-9: ]+[AP]M",
        "try again at <PROVIDER_RESET_TIME>",
        value,
        flags=re.IGNORECASE,
    )
    return value


if __name__ == "__main__":
    raise SystemExit(main())
