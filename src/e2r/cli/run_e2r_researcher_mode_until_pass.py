"""Run the isolated Phase 94 current Researcher Mode checkpoint until semantic pass."""

from __future__ import annotations

import argparse
from datetime import date, timedelta
import json
from pathlib import Path
import re
from typing import Any, Mapping

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    refresh_canary_target_manifest_hash,
    write_canary_post_run_gold_comparison,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexResearcherProvider,
    CodexSubagentFallbackResearchProvider,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeConfig,
    CurrentResearcherModeTargetRunner,
    FactExtractionCheckpointPending,
    load_current_research_target_registry,
    load_current_research_targets,
    write_production_lane,
)
from e2r.research_brain.researcher_mode.source_graph_explorer import (
    validate_source_graph_checkpoint,
)
from e2r.research_brain.researcher_mode.prompt_projection import (
    normalize_collaboration_transport_wait,
)
from e2r.research_brain.researcher_mode.evidence_fact_extractor import (
    fact_extraction_has_exact_checkpoint_recovery_wait,
)
from e2r.research_brain.researcher_mode.sealed_production import (
    SEALED_PRODUCTION_SEMANTICS_MATCH,
    SealedProductionVerification,
    assert_frozen_production_unchanged,
    build_current_production_semantics,
    make_production_semantics_seal,
    reviewed_post_run_semantic_files_present,
    verify_sealed_production,
)


_EXACT_COLLABORATION_RESPONSE_WAIT_RE = re.compile(
    r"COLLABORATION_RESPONSE_PENDING:COLLABREQ-[0-9a-f]{64}"
)

_POST_RUN_SEMANTIC_ADJUDICATION_PENDING = (
    "PENDING_POST_RUN_SEMANTIC_ADJUDICATION"
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
    parser.add_argument(
        "--fact-documents-per-call",
        type=int,
        default=1,
        help=(
            "Prompt-transport batch size only; every production document and "
            "continuation page remains loss-accounted."
        ),
    )
    parser.add_argument(
        "--research-provider",
        # Keep the production surface Codex-only.  Do not add a local-model
        # provider, endpoint, CLI option, or fallback here: old local lineage
        # is rejected by audits and must be regenerated through Codex.
        choices=(
            "codex",
            "codex-subagent",
            "codex-collaboration",
        ),
        default="codex",
        help=(
            "Structured LLM provider. codex-subagent preserves exact Codex CLI "
            "cache hits and journals only usage-limit cache misses for an "
            "audited Codex collaboration-subagent response; "
            "codex-collaboration routes every uncached leaf directly through "
            "the audited collaboration-subagent journal."
        ),
    )
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
    registry_rows = load_current_research_target_registry(
        args.target_registry
    )
    mandatory_target_ids = tuple(
        str(row.get("symbol") or row.get("target_id") or "")
        for row in registry_rows
    )
    targets = load_current_research_targets(
        symbols=symbols,
        registry_path=args.target_registry,
        as_of_date=args.as_of_date,
        registry_rows=registry_rows,
    )
    selected_target_ids = tuple(target.target_id for target in targets)
    selected_target_id_set = set(selected_target_ids)
    mandatory_target_id_set = set(mandatory_target_ids)
    full_mandatory_target_roster_selected = bool(
        len(selected_target_ids) == len(mandatory_target_ids)
        and selected_target_id_set == mandatory_target_id_set
    )
    missing_mandatory_target_ids = tuple(
        target_id
        for target_id in mandatory_target_ids
        if target_id not in selected_target_id_set
    )
    unexpected_selected_target_ids = tuple(
        target_id
        for target_id in selected_target_ids
        if target_id not in mandatory_target_id_set
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
        fact_documents_per_call=args.fact_documents_per_call,
    )
    output_root = Path(config.output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    provider = _build_research_provider(args)
    runner = CurrentResearcherModeTargetRunner(provider=provider)
    provider_manifest = _research_provider_manifest(runner.provider)
    current_semantics_before_run = build_current_production_semantics(
        config=config,
        targets=targets,
        registry_rows=registry_rows,
        target_registry_path=args.target_registry,
        provider_manifest=provider_manifest,
        repo_root=Path.cwd(),
    )
    sealed_verification: SealedProductionVerification | None = None
    reviewed_semantic_files_present = bool(
        full_mandatory_target_roster_selected
        and reviewed_post_run_semantic_files_present(output_root)
    )
    sealed_verification_reasons = [
        "reviewed_post_run_semantic_files_not_ready"
    ]
    if reviewed_semantic_files_present:
        # This verifier never imports or reads the Gold corpus/reviews.  A
        # mismatch therefore still permits a clean Gold-blind production run.
        candidate = verify_sealed_production(
            output_root=output_root,
            target_ids=selected_target_ids,
            as_of_date=config.as_of_date,
            archetype_id=config.archetype_id,
            expected_semantics=current_semantics_before_run,
        )
        sealed_verification_reasons = list(candidate.reasons)
        if candidate.eligible:
            sealed_verification = candidate

    post_run_only = sealed_verification is not None
    runs = ()
    fact_gate_pending: FactExtractionCheckpointPending | None = None
    if post_run_only:
        # The production lane and all target leaves remain byte-for-byte
        # sealed.  Only the post-run Gold section below may write files.
        paths = {"lane": output_root / "production_lane_manifest.json"}
        target_statuses = dict(sealed_verification.target_statuses)
        target_completion_gates = {
            target_id: dict(gates)
            for target_id, gates in (
                sealed_verification.target_completion_gates.items()
            )
        }
        production_complete = True
    else:
        # This manifest is closed before any target production call.  No Gold
        # module or Gold review content is touched on this path.
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
                "research_provider": provider_manifest,
                "expected_production_semantics": dict(
                    current_semantics_before_run
                ),
            },
        )
        completed_runs = []
        for target in targets:
            try:
                completed_runs.append(
                    _run_target_until_semantic_terminal(
                        runner=runner,
                        config=config,
                        target=target,
                    )
                )
            except FactExtractionCheckpointPending as exc:
                fact_gate_pending = exc
                break
        runs = tuple(completed_runs)
        if fact_gate_pending is not None:
            # Do not synthesize a partial production lane from stale
            # downstream outputs.  The exact fact request/response journal is
            # the only authorized continuation point for this target.
            target_statuses = {
                target.target_id: (
                    next(
                        (
                            run.status
                            for run in runs
                            if run.target.target_id == target.target_id
                        ),
                        "RESEARCH_CHECKPOINT_PENDING"
                        if target.target_id
                        == fact_gate_pending.target.target_id
                        else "NOT_STARTED_AFTER_UPSTREAM_FACT_GATE",
                    )
                )
                for target in targets
            }
            target_completion_gates = {
                run.target.target_id: dict(run.completion_gates)
                for run in runs
            }
            target_completion_gates[
                fact_gate_pending.target.target_id
            ] = dict(
                fact_gate_pending.audit.get("completion_gates") or {}
            )
            write_json(
                output_root / "production_lane_manifest.json",
                {
                    "schema_version": "e2r_v5_phase94_production_lane_v1",
                    "status": "RESEARCH_CHECKPOINT_PENDING",
                    "as_of_date": config.as_of_date,
                    "archetype_id": config.archetype_id,
                    "target_ids": list(selected_target_ids),
                    "target_statuses": target_statuses,
                    "exact_completion_gate": str(
                        fact_gate_pending.audit.get("exact_completion_gate")
                        or "fact_extraction_complete"
                    ),
                    "pending_target_id": (
                        fact_gate_pending.target.target_id
                    ),
                    "gold_visibility": False,
                    "gold_query_visibility": False,
                    "gold_url_visibility": False,
                    "gold_fact_visibility": False,
                    "comparison_timing": "POST_RUN_ONLY",
                    "production_research_complete": False,
                    "completion_based_on_fixed_rounds": False,
                    "research_provider": provider_manifest,
                },
            )
            paths = {"lane": output_root / "production_lane_manifest.json"}
            production_complete = False
        else:
            current_semantics_after_run = build_current_production_semantics(
                config=config,
                targets=targets,
                registry_rows=registry_rows,
                target_registry_path=args.target_registry,
                provider_manifest=provider_manifest,
                repo_root=Path.cwd(),
            )
            production_semantics_seal = make_production_semantics_seal(
                before_run=current_semantics_before_run,
                after_run=current_semantics_after_run,
            )
            paths = write_production_lane(
                config=config,
                target_runs=runs,
                research_provider=provider_manifest,
                production_semantics_seal=production_semantics_seal,
            )
            target_statuses = {
                run.target.target_id: run.status for run in runs
            }
            target_completion_gates = {
                run.target.target_id: dict(run.completion_gates)
                for run in runs
            }
            production_complete = bool(
                all(
                    run.status
                    == "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                    for run in runs
                )
                and production_semantics_seal.get("status")
                == SEALED_PRODUCTION_SEMANTICS_MATCH
            )
    post_run_status = "PENDING_PRODUCTION_RESEARCH_COMPLETION"
    gold_critical_fact_miss_count = None
    comparison_executed = False
    post_run_pass_status = None
    post_run_semantic_reviews_ready = bool(
        production_complete
        and full_mandatory_target_roster_selected
        and reviewed_post_run_semantic_files_present(output_root)
    )
    if post_run_semantic_reviews_ready:
        # Deliberately imported data access happens only now, after the clean
        # production files and lane manifest have been closed.
        (
            post_run_pass_status,
            compare_phase93_gold_post_run,
            write_phase93_post_run_comparison,
        ) = _load_post_run_gold_tools()
        try:
            comparison = compare_phase93_gold_post_run(
                production_root=output_root,
                require_post_run_semantic_adjudication=True,
            )
            comparison_executed = True
            write_phase93_post_run_comparison(
                result=comparison,
                comparison_path=output_root / "gold_fact_comparison.jsonl",
                audit_path=output_root / "post_run_gold_recall_audit.json",
            )
            for target in targets:
                write_canary_post_run_gold_comparison(
                    output_root / target.target_id,
                    target_id=target.target_id,
                    as_of_date=config.as_of_date,
                    comparison_rows=tuple(
                        row
                        for row in comparison.comparisons
                        if str(row.get("target_id") or "")
                        == target.target_id
                    ),
                )
                # Keep the manifest hash Gold-blind.  The canary audit still
                # records the post-run result, while the tree binding excludes
                # Gold leaves exactly like the production seal verifier.
                refresh_canary_target_manifest_hash(
                    output_root / target.target_id
                )
        finally:
            if sealed_verification is not None:
                assert_frozen_production_unchanged(
                    output_root=output_root,
                    verification=sealed_verification,
                )
        post_run_status = comparison.status
        gold_critical_fact_miss_count = comparison.audit["critical_counts"].get(
            "critical_material_fact_recall_below_threshold_count"
        )
    elif production_complete and full_mandatory_target_roster_selected:
        # Gold and the production lane intentionally use independent semantic
        # vocabularies.  Literal-key fallback is useful for controlled
        # fixtures, but it is not an operational recall verdict.  Wait for the
        # sealed post-run primary adjudication plus two independent reviews
        # instead of materializing a misleading 0%-recall failure.
        post_run_status = _POST_RUN_SEMANTIC_ADJUDICATION_PENDING
        write_json(
            output_root / "post_run_gold_recall_audit.json",
            {
                "schema_version": (
                    "e2r_v6_post_run_semantic_adjudication_pending_v1"
                ),
                "status": post_run_status,
                "as_of_date": config.as_of_date,
                "gold_visibility_during_production": False,
                "comparison_executed": False,
                "production_research_complete": True,
                "required_primary_file": (
                    "post_run_gold_semantic_primary.json"
                ),
                "required_review_directory": (
                    "post_run_gold_semantic_reviews"
                ),
                "minimum_independent_review_count": 2,
                "reason": (
                    "Gold-to-production core-economic-event adjudication "
                    "must complete after the production lane is sealed and "
                    "before recall is computed."
                ),
            },
        )
    elif production_complete:
        post_run_status = "PENDING_FULL_MANDATORY_TARGET_ROSTER"
        write_json(
            output_root / "post_run_gold_recall_audit.json",
            {
                "schema_version": (
                    "e2r_v5_phase94_post_run_gold_full_roster_pending_v1"
                ),
                "status": post_run_status,
                "as_of_date": config.as_of_date,
                "gold_visibility_during_production": False,
                "comparison_executed": False,
                "reason": (
                    "Post-run Gold comparison requires the selected "
                    "production target roster to exactly match the target "
                    "registry mandatory_targets roster."
                ),
                "selected_target_ids": list(selected_target_ids),
                "mandatory_target_ids": list(mandatory_target_ids),
                "missing_target_ids": list(missing_mandatory_target_ids),
                "unexpected_target_ids": list(
                    unexpected_selected_target_ids
                ),
            },
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
    complete = bool(
        production_complete
        and full_mandatory_target_roster_selected
        and post_run_pass_status is not None
        and post_run_status == post_run_pass_status
    )
    summary = {
        "status": (
            "PHASE94_CURRENT_RESEARCHER_MODE_PASS"
            if complete
            else "PHASE94_CURRENT_RESEARCHER_MODE_PENDING"
        ),
        "as_of_date": config.as_of_date,
        "latest_trading_snapshot_date": trading_date,
        "target_statuses": target_statuses,
        "target_completion_gates": target_completion_gates,
        "selected_target_ids": list(selected_target_ids),
        "mandatory_target_ids": list(mandatory_target_ids),
        "full_mandatory_target_roster_selected": (
            full_mandatory_target_roster_selected
        ),
        "missing_mandatory_target_ids": list(
            missing_mandatory_target_ids
        ),
        "unexpected_selected_target_ids": list(
            unexpected_selected_target_ids
        ),
        "production_research_complete": production_complete,
        "post_run_gold_status": post_run_status,
        "comparison_executed": comparison_executed,
        "production_execution_mode": (
            "SEALED_PRODUCTION_POST_RUN_ONLY"
            if post_run_only
            else "PRODUCTION_RUN"
        ),
        "sealed_production_verified": post_run_only,
        "sealed_production_verification_reasons": (
            []
            if sealed_verification is not None
            else sealed_verification_reasons
        ),
        "frozen_production_file_count": (
            len(sealed_verification.frozen_file_sha256)
            if sealed_verification is not None
            else None
        ),
        "gold_critical_fact_miss_count": gold_critical_fact_miss_count,
        "gold_visibility_during_production": False,
        "completion_based_on_fixed_rounds": False,
        "research_provider": provider_manifest,
        "production_lane_manifest": str(paths["lane"]),
    }
    write_json(output_root / "phase94_run_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if complete else 2


def _load_post_run_gold_tools():
    """Open Gold comparison code only after the full production roster closes."""

    from e2r.research_brain.researcher_mode.full_thesis_gold_benchmark import (
        PHASE93_POST_RUN_PASS,
        compare_phase93_gold_post_run,
        write_phase93_post_run_comparison,
    )

    return (
        PHASE93_POST_RUN_PASS,
        compare_phase93_gold_post_run,
        write_phase93_post_run_comparison,
    )


def _build_research_provider(args: argparse.Namespace):
    if args.research_provider == "codex":
        return None
    if args.research_provider == "codex-collaboration":
        return CollaborationCodexResearcherProvider.default()
    return CodexSubagentFallbackResearchProvider.default(
        working_directory=Path.cwd(),
        timeout_seconds=300.0,
    )


def _research_provider_manifest(provider) -> Mapping[str, Any]:
    transport = getattr(provider, "transport", None)
    try:
        identity = dict(provider._provider_identity())
        identity_error = None
    except (OSError, RuntimeError, TypeError, ValueError) as exc:
        identity = {
            "transport_class": (
                type(transport).__qualname__ if transport is not None else None
            ),
            "model": getattr(transport, "model", None),
            "profile": getattr(transport, "profile", None),
            "sandbox": getattr(transport, "sandbox", None),
            "approval_policy": getattr(
                transport, "approval_policy", None
            ),
            "extra_args": list(getattr(transport, "extra_args", ())),
        }
        identity_error = (
            f"{type(exc).__name__}:"
            + (" ".join(str(exc).split())[-500:] or "no detail")
        )
    return {
        "provider_name": str(
            getattr(provider, "provider_name", type(provider).__name__)
        ),
        "transport_class": (
            type(transport).__qualname__ if transport is not None else None
        ),
        "provider_identity": identity,
        "provider_identity_hash": stable_hash(identity),
        "provider_identity_resolved": identity_error is None,
        "provider_identity_error": identity_error,
        "provider_selected_explicitly": isinstance(
            provider,
            (
                CollaborationCodexResearcherProvider,
                CodexSubagentFallbackResearchProvider,
            ),
        ),
        "score_or_stage_authority": False,
    }


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

    target_root = Path(config.output_root) / target.target_id
    no_progress_path = target_root / "semantic_no_progress_checkpoint.json"
    prior_source_transport_snapshot = (
        _load_prior_source_transport_work_state(
            path=target_root / "source_graph_checkpoint.json",
            target_id=target.target_id,
            as_of_date=config.as_of_date,
        )
    )
    prior_no_progress_signature = _load_prior_no_progress_signature(
        path=no_progress_path,
        target_id=target.target_id,
        as_of_date=config.as_of_date,
        source_checkpoint_binding=(
            prior_source_transport_snapshot["checkpoint_binding"]
            if prior_source_transport_snapshot is not None
            else None
        ),
    )
    # A resumed run still executes one real checkpoint so a recovered provider
    # can make progress.  Seeding only the previously confirmed no-progress
    # signature prevents a second identical provider-failure epoch afterward.
    seen_signatures: set[str] = (
        {prior_no_progress_signature}
        if prior_no_progress_signature is not None
        else set()
    )
    next_source_resume_mode = "REUSE_READY_CHECKPOINT"
    while True:
        source_resume_mode = next_source_resume_mode
        result = runner.run_checkpoint(
            config=config,
            target=target,
            source_resume_mode=source_resume_mode,
        )
        signature = _semantic_signature(result)
        semantic_state = _semantic_state(result)
        result_audit = (
            getattr(result, "audit", {})
            if isinstance(getattr(result, "audit", {}), Mapping)
            else {}
        )
        source_checkpoint_readonly_replayed = bool(
            result_audit.get("source_checkpoint_readonly_replayed")
        )
        source_checkpoint_fact_extraction_recovery_replayed = bool(
            result_audit.get(
                "source_checkpoint_fact_extraction_recovery_replayed"
            )
        )
        source_transport_snapshot = _result_source_transport_work_state(
            result,
            target_id=target.target_id,
            as_of_date=config.as_of_date,
        )
        research_epoch_checkpoint_binding = (
            _result_research_epoch_checkpoint_binding(result)
        )
        source_transport_chain_valid = _source_transport_chain_is_valid(
            prior_source_transport_snapshot,
            source_transport_snapshot,
            readonly_replayed=source_checkpoint_readonly_replayed,
        )
        source_transport_advanced = bool(
            source_transport_chain_valid
            and prior_source_transport_snapshot is not None
            and _source_transport_advanced(
                prior_source_transport_snapshot["work_state"],
                source_transport_snapshot["work_state"],
            )
        )
        collaboration_response_waiting = (
            _result_has_exact_collaboration_response_wait(result)
        )
        next_source_resume_mode = (
            "REUSE_READY_CHECKPOINT"
            if (
                collaboration_response_waiting
                or _terminal_source_snapshot_has_pending_fact_extraction(
                    result,
                    source_transport_snapshot["work_state"],
                )
            )
            else "ADVANCE"
        )
        progress_path = target_root / "until_pass_progress.json"
        write_json(
            progress_path,
            {
                "schema_version": "e2r_v5_phase94_until_pass_progress_v1",
                "target_id": target.target_id,
                "as_of_date": config.as_of_date,
                "status": result.status,
                "semantic_signature": signature,
                "semantic_state_component_hashes": {
                    key: stable_hash(value)
                    for key, value in sorted(semantic_state.items())
                },
                "seen_semantic_state_count": len(seen_signatures) + 1,
                "completion_based_on_fixed_rounds": False,
                "transport_budget_treated_as_completion": False,
                "source_checkpoint_binding": dict(
                    source_transport_snapshot["checkpoint_binding"]
                ),
                "research_epoch_checkpoint_binding": (
                    dict(research_epoch_checkpoint_binding)
                    if research_epoch_checkpoint_binding is not None
                    else None
                ),
                "source_transport_chain_valid": (
                    source_transport_chain_valid
                ),
                "source_transport_advanced": source_transport_advanced,
                "collaboration_response_waiting": (
                    collaboration_response_waiting
                ),
                "source_transport_work": _source_transport_work_summary(
                    source_transport_snapshot["work_state"]
                ),
                "completion_gates": dict(result.completion_gates),
            },
        )
        refresh_canary_target_manifest_hash(progress_path.parent)
        if result.status == "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD":
            no_progress_path.unlink(missing_ok=True)
            refresh_canary_target_manifest_hash(progress_path.parent)
            return result
        if collaboration_response_waiting:
            # An exact audited Codex request cannot resolve by immediately
            # rerunning the same checkpoint.  Return control after one pass;
            # the imported response will be consumed on the next clean resume.
            no_progress_path.unlink(missing_ok=True)
            refresh_canary_target_manifest_hash(progress_path.parent)
            return result
        if (
            source_checkpoint_readonly_replayed
            and not source_checkpoint_fact_extraction_recovery_replayed
            and next_source_resume_mode != "REUSE_READY_CHECKPOINT"
            and source_transport_chain_valid
        ):
            # A ready source snapshot was intentionally held immutable so a
            # recovered downstream provider/output contract could be retried
            # first.  If that retry remains pending, allow one ordinary source
            # ADVANCE before applying either the in-process or persisted
            # semantic no-progress stop.
            seen_signatures.add(signature)
            prior_source_transport_snapshot = source_transport_snapshot
            continue
        if (
            signature in seen_signatures
            and not source_transport_advanced
            and source_transport_chain_valid
            and not source_checkpoint_readonly_replayed
            and next_source_resume_mode == "ADVANCE"
            and _source_query_generation_was_deferred(result)
            and _source_transport_work_is_drained(
                source_transport_snapshot["work_state"]
            )
            and _supervisor_has_open_query_routes(result)
        ):
            # Candidate/reference work is scheduled before query generation.
            # It may be created and fully drained inside one checkpoint, so it
            # has no prior pending id for _source_transport_advanced() to
            # recognize.  That checkpoint did not give the LLM planner a turn.
            # Grant exactly the following ADVANCE; once the planner is called,
            # the acquisition audit flag is false and ordinary no-progress
            # handling applies.
            seen_signatures.add(signature)
            prior_source_transport_snapshot = source_transport_snapshot
            continue
        if signature in seen_signatures and not source_transport_advanced:
            write_json(
                no_progress_path,
                {
                    "schema_version": "e2r_v5_phase94_semantic_no_progress_v1",
                    "status": "RESEARCH_PENDING_NO_NEW_SEMANTIC_STATE",
                    "target_id": target.target_id,
                    "as_of_date": config.as_of_date,
                    "source_checkpoint_binding": dict(
                        source_transport_snapshot["checkpoint_binding"]
                    ),
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
            refresh_canary_target_manifest_hash(progress_path.parent)
            return result
        if prior_no_progress_signature is not None and no_progress_path.exists():
            # The provider or evidence state recovered.  The old pending leaf
            # is current-state output, not append-only research lineage.
            no_progress_path.unlink()
            refresh_canary_target_manifest_hash(progress_path.parent)
            prior_no_progress_signature = None
        seen_signatures.add(signature)
        prior_source_transport_snapshot = source_transport_snapshot


def _load_prior_no_progress_signature(
    *,
    path: Path,
    target_id: str,
    as_of_date: str,
    source_checkpoint_binding: Mapping[str, Any] | None,
) -> str | None:
    """Load only an exact source-generation-bound semantic stop leaf."""

    if not path.is_file() or source_checkpoint_binding is None:
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    if not isinstance(payload, Mapping):
        return None
    if (
        payload.get("schema_version")
        != "e2r_v5_phase94_semantic_no_progress_v1"
        or payload.get("status") != "RESEARCH_PENDING_NO_NEW_SEMANTIC_STATE"
        or str(payload.get("target_id") or "") != target_id
        or str(payload.get("as_of_date") or "") != as_of_date
        or not isinstance(payload.get("source_checkpoint_binding"), Mapping)
        or dict(payload["source_checkpoint_binding"])
        != dict(source_checkpoint_binding)
    ):
        return None
    signature = str(payload.get("semantic_signature") or "")
    if re.fullmatch(r"[0-9a-f]{64}", signature) is None:
        return None
    return signature


def _load_prior_source_transport_work_state(
    *,
    path: Path,
    target_id: str,
    as_of_date: str,
) -> Mapping[str, Any] | None:
    """Load a target-bound, hash-validated source lifecycle baseline."""

    if not path.is_file():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        checkpoint = validate_source_graph_checkpoint(
            payload,
            target_id=target_id,
            as_of_date=as_of_date,
        )
    except (
        OSError,
        UnicodeDecodeError,
        json.JSONDecodeError,
        TypeError,
        ValueError,
    ):
        return None
    return _source_transport_snapshot(checkpoint)


def _result_source_transport_work_state(
    result: Any,
    *,
    target_id: str,
    as_of_date: str,
) -> Mapping[str, Any]:
    source_graph = getattr(result, "source_graph", None)
    checkpoint = getattr(source_graph, "checkpoint", None)
    if not isinstance(checkpoint, Mapping):
        raise ValueError("current source checkpoint is missing")
    validated = validate_source_graph_checkpoint(
        checkpoint,
        target_id=target_id,
        as_of_date=as_of_date,
    )
    return _source_transport_snapshot(validated)


def _result_research_epoch_checkpoint_binding(
    result: Any,
) -> Mapping[str, Any] | None:
    """Bind progress to the exact epoch output used for this source replay."""

    epoch_run = getattr(result, "research_epoch", None)
    checkpoint = getattr(epoch_run, "checkpoint", None)
    if checkpoint is None:
        return None

    def field(name: str, default: Any = None) -> Any:
        if isinstance(checkpoint, Mapping):
            return checkpoint.get(name, default)
        return getattr(checkpoint, name, default)

    binding = {
        "target_id": str(field("target_id") or ""),
        "as_of_date": str(field("as_of_date") or ""),
        "checkpoint_id": str(field("checkpoint_id") or ""),
        "checkpoint_hash": str(field("checkpoint_hash") or ""),
        "epoch": int(field("epoch") or 0),
        "source_graph_checkpoint_id": str(
            field("source_graph_checkpoint_id") or ""
        ),
    }
    if (
        not binding["target_id"]
        or not binding["as_of_date"]
        or not binding["checkpoint_id"]
        or not binding["checkpoint_hash"]
        or binding["epoch"] < 1
        or not binding["source_graph_checkpoint_id"]
    ):
        return None
    return binding


def _source_transport_snapshot(
    checkpoint: Mapping[str, Any],
) -> Mapping[str, Any]:
    return {
        "checkpoint_binding": {
            "target_id": str(checkpoint.get("target_id") or ""),
            "as_of_date": str(checkpoint.get("as_of_date") or ""),
            "checkpoint_id": str(checkpoint.get("checkpoint_id") or ""),
            "checkpoint_hash": str(checkpoint.get("checkpoint_hash") or ""),
            "epoch": int(checkpoint.get("epoch") or 0),
        },
        "resumed_from_checkpoint_id": (
            str(checkpoint.get("resumed_from_checkpoint_id") or "")
            or None
        ),
        "work_state": _source_transport_work_state(checkpoint),
    }


def _source_transport_chain_is_valid(
    prior: Mapping[str, Any] | None,
    current: Mapping[str, Any],
    *,
    readonly_replayed: bool,
) -> bool:
    if prior is None:
        return False
    prior_binding = prior.get("checkpoint_binding")
    current_binding = current.get("checkpoint_binding")
    if not isinstance(prior_binding, Mapping) or not isinstance(
        current_binding,
        Mapping,
    ):
        return False
    if readonly_replayed:
        return dict(current_binding) == dict(prior_binding)
    return bool(
        current_binding.get("target_id") == prior_binding.get("target_id")
        and current_binding.get("as_of_date") == prior_binding.get("as_of_date")
        and int(current_binding.get("epoch") or 0)
        == int(prior_binding.get("epoch") or 0) + 1
        and current.get("resumed_from_checkpoint_id")
        == prior_binding.get("checkpoint_id")
    )


def _source_transport_work_state(
    checkpoint: Mapping[str, Any],
) -> Mapping[str, Mapping[str, str]]:
    """Project only query/rank/fetch lifecycle states from a checkpoint."""

    queries: dict[str, str] = {}
    for row in checkpoint.get("generated_queries") or ():
        if not isinstance(row, Mapping):
            continue
        query_id = str(row.get("query_id") or "").strip()
        if not query_id:
            continue
        queries[query_id] = (
            "QUERY_PENDING"
            if row.get("execution_status")
            in {"PENDING", "BLOCKED_OFFICIAL_FIRST"}
            else "TERMINAL"
        )
    candidates: dict[str, str] = {}
    for row in checkpoint.get("search_candidates") or ():
        if not isinstance(row, Mapping):
            continue
        candidate_id = str(row.get("candidate_id") or "").strip()
        if not candidate_id:
            continue
        if row.get("ranking_status") == "PENDING":
            state = "RANK_PENDING"
        elif row.get("fetch_status") in {
            "MATERIAL_PENDING_FETCH",
            "FETCH_RETRY_PENDING",
        }:
            state = "FETCH_PENDING"
        else:
            state = "TERMINAL"
        candidates[candidate_id] = state
    return {
        "queries": queries,
        "candidates": candidates,
    }


def _source_transport_advanced(
    prior: Mapping[str, Mapping[str, str]] | None,
    current: Mapping[str, Mapping[str, str]],
) -> bool:
    """Recognize progress only for a persisted pending row's next lifecycle."""

    if prior is None:
        return False
    prior_queries = prior.get("queries") or {}
    current_queries = current.get("queries") or {}
    if any(
        state == "QUERY_PENDING"
        and current_queries.get(row_id) == "TERMINAL"
        for row_id, state in prior_queries.items()
    ):
        return True
    prior_candidates = prior.get("candidates") or {}
    current_candidates = current.get("candidates") or {}
    for row_id, state in prior_candidates.items():
        next_state = current_candidates.get(row_id)
        if state == "RANK_PENDING" and next_state in {
            "FETCH_PENDING",
            "TERMINAL",
        }:
            return True
        if state == "FETCH_PENDING" and next_state == "TERMINAL":
            return True
    return False


def _source_transport_work_summary(
    state: Mapping[str, Mapping[str, str]],
) -> Mapping[str, Any]:
    """Expose counts and an opaque state hash without raw transport IDs."""

    queries = state.get("queries") or {}
    candidates = state.get("candidates") or {}
    return {
        "pending_query_count": sum(
            value == "QUERY_PENDING" for value in queries.values()
        ),
        "pending_ranking_count": sum(
            value == "RANK_PENDING" for value in candidates.values()
        ),
        "pending_fetch_count": sum(
            value == "FETCH_PENDING" for value in candidates.values()
        ),
        "state_hash": stable_hash(state),
    }


def _source_transport_work_is_drained(
    state: Mapping[str, Mapping[str, str]],
) -> bool:
    summary = _source_transport_work_summary(state)
    return not any(
        int(summary[key])
        for key in (
            "pending_query_count",
            "pending_ranking_count",
            "pending_fetch_count",
        )
    )


def _terminal_source_snapshot_has_pending_fact_extraction(
    result: Any,
    source_transport_work_state: Mapping[str, Mapping[str, str]],
) -> bool:
    """Keep a terminal immutable source snapshot until its fact queue drains."""

    source_graph = getattr(result, "source_graph", None)
    fact_extraction = getattr(result, "fact_extraction", None)
    result_audit = getattr(result, "audit", None)
    fact_recovery_replayed = bool(
        isinstance(result_audit, Mapping)
        and result_audit.get(
            "source_checkpoint_fact_extraction_recovery_replayed"
        )
        is True
    )
    terminal_source_identity = bool(
        getattr(source_graph, "status", None)
        in {"EPOCH_COMPLETE_REQUIRES_SUPERVISOR", "STOPPED_ON_RESOLUTION"}
        or fact_recovery_replayed
    )
    return bool(
        terminal_source_identity
        and (
            fact_recovery_replayed
            or _source_transport_work_is_drained(
                source_transport_work_state
            )
        )
        and getattr(fact_extraction, "status", None)
        == "FACT_EXTRACTION_PENDING"
        and fact_extraction_has_exact_checkpoint_recovery_wait(
            getattr(fact_extraction, "pending_reasons", ())
        )
    )


def _result_has_exact_collaboration_response_wait(result: Any) -> bool:
    """Keep the source snapshot fixed while a downstream Codex reply is due."""

    def field(row: Any, key: str, default: Any = None) -> Any:
        if isinstance(row, Mapping):
            return row.get(key, default)
        return getattr(row, key, default) if row is not None else default

    def add_reasons(values: list[str], row: Any) -> None:
        reasons = field(row, "pending_reasons", ())
        if isinstance(reasons, (list, tuple)):
            values.extend(str(value) for value in reasons)

    values: list[str] = []
    fact_extraction = getattr(result, "fact_extraction", None)
    add_reasons(values, fact_extraction)

    dossier = getattr(result, "dossier", None)
    add_reasons(values, dossier)
    business_model = field(dossier, "business_model_result")
    add_reasons(values, business_model)
    for component in field(dossier, "component_results", ()) or ():
        add_reasons(values, component)
    add_reasons(values, field(dossier, "red_team_result"))
    scoring_memos = getattr(result, "scoring_memos", None)
    for component in field(scoring_memos, "component_memos", ()) or ():
        add_reasons(values, component)
    score_aggregation = getattr(result, "score_aggregation", None)
    add_reasons(values, score_aggregation)
    for component in field(score_aggregation, "component_results", ()) or ():
        add_reasons(values, component)
    stagecourt = getattr(result, "stagecourt", None)
    add_reasons(values, field(stagecourt, "decision"))

    epoch = getattr(result, "research_epoch", None)
    supervisor = field(epoch, "supervisor_review")
    for key in (
        "unresolved_material_questions",
        "next_actions",
    ):
        rows = field(supervisor, key, ())
        if isinstance(rows, (list, tuple)):
            values.extend(str(value) for value in rows)
    values.append(str(field(supervisor, "rationale", "")))
    for review_result in field(
        epoch,
        "saturation_reviewer_results",
        (),
    ) or ():
        add_reasons(values, review_result)

    return any(
        _EXACT_COLLABORATION_RESPONSE_WAIT_RE.search(value) is not None
        for value in values
    )


def _source_query_generation_was_deferred(result: Any) -> bool:
    source_graph = getattr(result, "source_graph", None)
    audit = getattr(source_graph, "audit", None)
    return bool(
        isinstance(audit, Mapping)
        and audit.get("query_generation_deferred_by_candidate_work") is True
    )


def _supervisor_has_open_query_routes(result: Any) -> bool:
    epoch = getattr(result, "research_epoch", None)
    review = getattr(epoch, "supervisor_review", None)
    if review is None:
        return False

    def field(key: str, default: Any = None) -> Any:
        if isinstance(review, Mapping):
            return review.get(key, default)
        return getattr(review, key, default)

    return bool(
        field("status") == "NEXT_RESEARCH_REQUIRED"
        and (
            field("reasonable_positive_routes_remaining") is True
            or field("query_direction_briefs", ())
            or field("new_source_family_directions", ())
        )
    )


def _semantic_signature(result) -> str:
    return stable_hash(_semantic_state(result))


def _semantic_state(result) -> Mapping[str, Any]:
    return {
        # Query/candidate/document identifiers describe transport attempts,
        # not research progress.  A planner can keep wording the same open
        # objective differently and receive fresh candidate IDs without
        # producing a new citable fact.  Counting those IDs makes the
        # until-pass loop immortal even when every material gate is stable.
        # Per-attempt source failures are transport diagnostics too.  The
        # same URL can alternate between timeout, HTTP 403, unreadable
        # text, and unknown publication date without changing any citable
        # fact or research conclusion.  Material failure progress is
        # already represented by source_graph_status, pending reasons, and
        # the supervisor's deduplicated failure/gap state below.
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
        "supervisor_state": _supervisor_semantic_state(
            result.research_epoch.supervisor_review
        ),
    }


def _supervisor_semantic_state(review: Any) -> Mapping[str, Any]:
    """Keep deterministic supervisor progress while ignoring prose churn."""

    def field(row: Any, key: str, default: Any = None) -> Any:
        if isinstance(row, Mapping):
            return row.get(key, default)
        return getattr(row, key, default)

    def rows(key: str) -> tuple[Any, ...]:
        value = field(review, key, ())
        return tuple(value) if isinstance(value, (list, tuple)) else ()

    provider_or_output_errors = sorted(
        _semantic_failure_reason(str(question))
        for question in rows("unresolved_material_questions")
        if str(question).startswith("SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:")
    )
    failure_states = [
        (
            str(field(row, "classification", "")),
            bool(field(row, "retryable", False)),
            bool(field(row, "source_absence_claim_allowed", False)),
        )
        for row in rows("failure_assessments")
    ]
    return {
        "status": str(field(review, "status", "")),
        "provider_or_output_errors": provider_or_output_errors,
        "gates": {
            key: field(review, key, None)
            for key in (
                "counter_and_supersession_checked",
                "structured_data_complete",
                "component_memos_sufficient",
                "reasonable_positive_routes_remaining",
                "ready_for_independent_saturation_review",
            )
        },
        "missing_material_fact_states": sorted(
            (
                str(field(row, "component_id", "")),
                str(field(row, "direction", "")),
            )
            for row in rows("missing_material_facts")
        ),
        "source_direction_states": sorted(
            (
                str(field(row, "objective_id", "")),
                str(field(row, "source_family", "")),
                bool(field(row, "counter_or_supersession", False)),
            )
            for row in rows("new_source_family_directions")
        ),
        "query_direction_states": sorted(
            (
                str(field(row, "objective_id", "")),
                bool(field(row, "counter_or_supersession", False)),
            )
            for row in rows("query_direction_briefs")
        ),
        "source_family_gaps": sorted(
            str(value) for value in rows("source_family_gaps")
        ),
        # Recounting another document in an already-known failure class is an
        # additional transport attempt, not a new research state.
        "failure_states": sorted(set(failure_states)),
    }


def _semantic_failure_reason(reason: str) -> str:
    """Remove transport noise that cannot represent new research semantics."""

    value = " ".join(str(reason).split())
    value = normalize_collaboration_transport_wait(value)
    folded = value.casefold()
    prefix = value.split(":", 2)[:2]
    stable_prefix = ":".join(prefix)
    if "prompt_transport_too_large" in folded:
        return f"{stable_prefix}:PROMPT_TRANSPORT_TOO_LARGE"
    if any(
        marker in folded
        for marker in (
            "ran out of room in the model's context window",
            "context window is too large",
            "context length exceeded",
            "maximum context length",
        )
    ):
        return f"{stable_prefix}:PROVIDER_CONTEXT_WINDOW_EXHAUSTED"
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
