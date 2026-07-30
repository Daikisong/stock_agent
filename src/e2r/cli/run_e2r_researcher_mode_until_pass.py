"""Run the isolated Phase 94 current Researcher Mode checkpoint until semantic pass."""

from __future__ import annotations

import argparse
from datetime import date, timedelta
import json
from pathlib import Path
import re
from typing import Any, Mapping

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.researcher_mode import (
    PHASE93_POST_RUN_PASS,
    CurrentResearcherModeConfig,
    CurrentResearcherModeTargetRunner,
    CodexSubagentFallbackResearchProvider,
    OllamaResearcherProvider,
    compare_phase93_gold_post_run,
    load_current_research_targets,
    refresh_canary_target_manifest_hash,
    validate_source_graph_checkpoint,
    write_canary_post_run_gold_comparison,
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
    parser.add_argument(
        "--research-provider",
        choices=("codex", "codex-subagent", "ollama"),
        default="codex",
        help=(
            "Structured LLM provider. codex-subagent preserves exact Codex CLI "
            "cache hits and journals only usage-limit cache misses for an "
            "audited Codex collaboration-subagent response."
        ),
    )
    parser.add_argument("--ollama-base-url")
    parser.add_argument("--ollama-model")
    parser.add_argument("--ollama-context-length", type=int)
    parser.add_argument("--ollama-max-output-tokens", type=int)
    parser.add_argument("--ollama-prompt-character-limit", type=int)
    parser.add_argument("--ollama-fact-document-chunk-chars", type=int)
    parser.add_argument("--ollama-timeout-seconds", type=float)
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
    provider = _build_research_provider(args)
    runner = CurrentResearcherModeTargetRunner(provider=provider)
    provider_manifest = _research_provider_manifest(runner.provider)
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
            "research_provider": provider_manifest,
        },
    )
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
        for run in runs:
            write_canary_post_run_gold_comparison(
                run.output_root,
                target_id=run.target.target_id,
                as_of_date=config.as_of_date,
                comparison_rows=tuple(
                    row
                    for row in comparison.comparisons
                    if str(row.get("target_id") or "") == run.target.target_id
                ),
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
        "research_provider": provider_manifest,
        "production_lane_manifest": str(paths["lane"]),
    }
    write_json(output_root / "phase94_run_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if complete else 2


def _build_research_provider(args: argparse.Namespace):
    if args.research_provider in {"codex", "codex-subagent"}:
        ollama_options = {
            key: value
            for key, value in vars(args).items()
            if key.startswith("ollama_") and value is not None
        }
        if ollama_options:
            raise ValueError(
                "Ollama options require --research-provider ollama:"
                f" {sorted(ollama_options)}"
            )
        if args.research_provider == "codex":
            return None
        return CodexSubagentFallbackResearchProvider.default(
            working_directory=Path.cwd(),
            timeout_seconds=300.0,
        )
    return OllamaResearcherProvider.default(
        base_url=args.ollama_base_url or "http://127.0.0.1:11434",
        model=args.ollama_model or "qwen3.5:27b",
        timeout_seconds=args.ollama_timeout_seconds or 900.0,
        context_length=args.ollama_context_length or 262_144,
        max_output_tokens=args.ollama_max_output_tokens or 32_768,
        prompt_character_limit=(
            args.ollama_prompt_character_limit or 500_000
        ),
        fact_document_chunk_chars=(
            args.ollama_fact_document_chunk_chars or 100_000
        ),
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
            "context_length": getattr(transport, "context_length", None),
            "max_output_tokens": getattr(
                transport, "max_output_tokens", None
            ),
            "prompt_character_limit": getattr(
                transport, "prompt_character_limit", None
            ),
            "temperature": getattr(transport, "temperature", None),
            "seed": getattr(transport, "seed", None),
            "think": getattr(transport, "think", None),
            "keep_alive": getattr(transport, "keep_alive", None),
            "fact_document_chunk_chars": getattr(
                provider, "fact_document_chunk_chars", None
            ),
        }
        identity_error = (
            f"{type(exc).__name__}:"
            + (" ".join(str(exc).split())[-500:] or "no detail")
        )
    public_identity = {
        key: value
        for key, value in identity.items()
        if key != "base_url"
    }
    return {
        "provider_name": str(
            getattr(provider, "provider_name", type(provider).__name__)
        ),
        "transport_class": (
            type(transport).__qualname__ if transport is not None else None
        ),
        "provider_identity": public_identity,
        "provider_identity_hash": stable_hash(identity),
        "provider_identity_resolved": identity_error is None,
        "provider_identity_error": identity_error,
        "provider_selected_explicitly": isinstance(
            provider,
            (
                OllamaResearcherProvider,
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
    first_checkpoint = True
    while True:
        result = runner.run_checkpoint(
            config=config,
            target=target,
            source_resume_mode=(
                "REUSE_READY_CHECKPOINT" if first_checkpoint else "ADVANCE"
            ),
        )
        first_checkpoint = False
        signature = _semantic_signature(result)
        semantic_state = _semantic_state(result)
        source_checkpoint_readonly_replayed = bool(
            (
                getattr(result, "audit", {})
                if isinstance(getattr(result, "audit", {}), Mapping)
                else {}
            ).get("source_checkpoint_readonly_replayed")
        )
        source_transport_snapshot = _result_source_transport_work_state(
            result,
            target_id=target.target_id,
            as_of_date=config.as_of_date,
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
                "source_transport_chain_valid": (
                    source_transport_chain_valid
                ),
                "source_transport_advanced": source_transport_advanced,
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
        if source_checkpoint_readonly_replayed and source_transport_chain_valid:
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
            if row.get("execution_status") == "PENDING"
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
