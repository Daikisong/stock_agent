"""Research Brain v4 production-shadow orchestrator."""

from __future__ import annotations

import json
import os
import re
import time
from collections import Counter
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.agentic.evidence_os import AppendOnlyEvidenceLedger, LedgerEvent, LedgerEventType
from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.production.claim_extraction import CodexCLIExtractorProvider, LLMContractBlindRawAssertionExtractor, RuleFallbackExtractorProvider
from e2r.production.candidate_event_purity import (
    ProductionMode,
    evaluate_candidate_event_production_eligibility,
    load_instrument_registry,
)
from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix
from e2r.research_brain.schemas import SourceTask, SourceTaskType, deterministic_id
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2, EventMagnitudeV2
from e2r.research_brain.v4_evidence_extraction_bridge import (
    EvidenceOSExecutionBundleV4,
    execute_source_tasks_with_evidence_os_v4,
)
from e2r.research_brain.v4_planner_runtime import (
    CONTRACT_COMPATIBLE_PRIMITIVES,
    FrozenRealPlannerProviderV4,
    ResearchBrainPlannerProviderV4,
    build_planner_provider_v4,
    run_planner_provider_v4,
    sanitize_existing_evidence_summary_v4,
    source_tasks_from_planner_output_v4,
)
from e2r.research_brain.v4_schemas import (
    ClaimExtractorProviderModeV4,
    DailyWatchlistItemV4,
    PlannerProviderModeV4,
    PlannerRunV4,
    ProductionShadowV4Config,
    SourceAcquisitionModeV4,
    SourceTaskExecutionStatusV4,
    SourceTaskExecutionV4,
)
from e2r.research_brain.v4_scoring_stage import build_claim_backed_watchlist_item_v4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4


DEFAULT_V1_ARCHETYPE_MATRIX = Path("docs/operational/research_brain_v1_archetype_matrix.json")
_FORBIDDEN_PLANNER_CONTEXT_ASSIGNMENT_RE = re.compile(
    r"(^|[;\s])([A-Za-z0-9_]*(?:score|stage)[A-Za-z0-9_]*)=([^;]*)(;?)",
    re.IGNORECASE,
)


def run_research_brain_v4_production_shadow(
    *,
    config: ProductionShadowV4Config,
    v1_archetype_matrix: Mapping[str, Any],
    planner_provider: ResearchBrainPlannerProviderV4 | None = None,
    repo_root: str | Path = ".",
) -> Mapping[str, Any]:
    config.validate()
    started_at = time.monotonic()
    runtime_budget_exhausted = False
    as_of_date = date.fromisoformat(config.as_of_date)
    cards = build_memory_cards_from_v1_matrix(v1_archetype_matrix)
    cards_by_id = {card.archetype_id: card for card in cards}
    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    discovered_events = discover_daily_candidate_events_v4(
        repo_root=repo_root,
        as_of_date=as_of_date,
        universe_limit=_discovery_limit_for_config(config),
    )
    seed_events = _candidate_seed_events_from_config(config=config, as_of_date=as_of_date, repo_root=repo_root)
    events = _select_unique_candidate_events(
        (*seed_events, *discovered_events),
        limit=_discovery_limit_for_config(config),
    )
    runtime_progress_events: list[dict[str, Any]] = []
    _record_runtime_progress_v4(
        config=config,
        progress_events=runtime_progress_events,
        phase="events_selected",
        candidate_event_count=len(events),
        seed_event_count=len(seed_events),
        discovered_event_count=len(discovered_events),
        ordered_event_limit=_discovery_limit_for_config(config),
    )
    if planner_provider is None:
        planner_provider = build_planner_provider_v4(mode=config.planner_provider, working_directory=repo_root)
    claim_extractor = _claim_extractor_for_config(config=config, repo_root=repo_root, started_at=started_at)
    ordered_events = _planner_candidate_order(events=events, config=config, repo_root=repo_root, as_of_date=as_of_date)
    _record_runtime_progress_v4(
        config=config,
        progress_events=runtime_progress_events,
        phase="events_ordered",
        ordered_event_count=len(ordered_events),
        first_candidate_event_ids=[event.candidate_event_id for event in ordered_events[:10]],
    )
    planner_runs: list[PlannerRunV4] = []
    next_event_index = 0
    planner_attempt_limit = min(len(ordered_events), config.max_distinct_candidate_attempts)
    if config.planner_provider == PlannerProviderModeV4.FAKE.value:
        for event_batch in _chunks(ordered_events[:planner_attempt_limit], config.planner_batch_size):
            if _runtime_budget_exhausted_v4(config=config, started_at=started_at):
                runtime_budget_exhausted = True
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=runtime_progress_events,
                    phase="runtime_budget_exhausted",
                    next_event_index=next_event_index,
                    planned_event_count=len(planner_runs),
                    total_event_count=len(ordered_events),
                    runtime_budget_seconds=config.runtime_budget_seconds,
                )
                break
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="planner_batch_start",
                provider_mode=config.planner_provider,
                batch_candidate_event_ids=[event.candidate_event_id for event in event_batch],
                next_event_index=next_event_index,
            )
            planner_runs.extend(
                run_planner_provider_v4(
                    provider=planner_provider,
                    events=event_batch,
                    memory_cards=cards,
                    existing_evidence_by_event_id=_evidence_context_by_event(events=event_batch, config=config),
                )
            )
            _flush_runtime_planner_leafs_v4(config=config, planner_runs=planner_runs)
            next_event_index += len(event_batch)
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="planner_batch_end",
                provider_mode=config.planner_provider,
                planner_run_count=len(planner_runs),
                real_provider_success_count=sum(1 for run in planner_runs if run.real_provider_success),
            )
        if not runtime_budget_exhausted:
            next_event_index = planner_attempt_limit
    else:
        real_success_count = 0
        while next_event_index < planner_attempt_limit and real_success_count < config.planner_success_limit:
            if _runtime_budget_exhausted_v4(config=config, started_at=started_at):
                runtime_budget_exhausted = True
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=runtime_progress_events,
                    phase="runtime_budget_exhausted",
                    next_event_index=next_event_index,
                    planned_event_count=len(planner_runs),
                    total_event_count=len(ordered_events),
                    runtime_budget_seconds=config.runtime_budget_seconds,
                )
                break
            remaining_success_budget = max(1, config.planner_success_limit - real_success_count)
            remaining_attempt_budget = max(0, planner_attempt_limit - next_event_index)
            if remaining_attempt_budget <= 0:
                break
            event_batch = ordered_events[
                next_event_index : next_event_index + min(config.planner_batch_size, remaining_success_budget, remaining_attempt_budget)
            ]
            if not event_batch:
                break
            next_event_index += len(event_batch)
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="planner_batch_start",
                provider_mode=config.planner_provider,
                batch_candidate_event_ids=[event.candidate_event_id for event in event_batch],
                next_event_index=next_event_index,
                real_success_count=real_success_count,
                remaining_success_budget=remaining_success_budget,
            )
            batch_runs = run_planner_provider_v4(
                provider=planner_provider,
                events=event_batch,
                memory_cards=cards,
                existing_evidence_by_event_id=_evidence_context_by_event(events=event_batch, config=config),
            )
            planner_runs.extend(batch_runs)
            _flush_runtime_planner_leafs_v4(config=config, planner_runs=planner_runs)
            real_success_count += sum(1 for run in batch_runs if run.real_provider_success)
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="planner_batch_end",
                provider_mode=config.planner_provider,
                batch_run_count=len(batch_runs),
                batch_success_count=sum(1 for run in batch_runs if run.real_provider_success),
                planner_run_count=len(planner_runs),
                real_success_count=real_success_count,
                next_event_index=next_event_index,
            )
    _record_runtime_progress_v4(
        config=config,
        progress_events=runtime_progress_events,
        phase="missing_external_web_plan_retry_start",
        planner_run_count=len(planner_runs),
    )
    if runtime_budget_exhausted or _runtime_budget_exhausted_v4(config=config, started_at=started_at):
        runtime_budget_exhausted = True
        _record_runtime_progress_v4(
            config=config,
            progress_events=runtime_progress_events,
            phase="missing_external_web_plan_retry_skipped_runtime_budget",
            planner_run_count=len(planner_runs),
            runtime_budget_seconds=config.runtime_budget_seconds,
        )
    elif _optional_retry_would_starve_source_execution_v4(config=config, started_at=started_at):
        _record_runtime_progress_v4(
            config=config,
            progress_events=runtime_progress_events,
            phase="missing_external_web_plan_retry_skipped_insufficient_source_budget",
            planner_run_count=len(planner_runs),
            runtime_budget_seconds=config.runtime_budget_seconds,
            runtime_budget_remaining_seconds=_runtime_budget_remaining_seconds_v4(config=config, started_at=started_at),
            source_execution_reserved_budget_seconds=_source_execution_reserved_budget_seconds_v4(config=config),
        )
    else:
        planner_runs = list(
            _retry_planner_for_missing_external_web_plan(
                planner_runs=planner_runs,
                provider=planner_provider,
                memory_cards=cards,
                config=config,
                started_at=started_at,
                progress_events=runtime_progress_events,
            )
        )
        _flush_runtime_planner_leafs_v4(config=config, planner_runs=planner_runs)
    _record_runtime_progress_v4(
        config=config,
        progress_events=runtime_progress_events,
        phase="missing_external_web_plan_retry_end",
        planner_run_count=len(planner_runs),
        real_provider_success_count=sum(1 for run in planner_runs if run.real_provider_success),
    )

    source_runner = SourceAcquisitionRunnerV4(mode=config.source_acquisition, repo_root=repo_root)
    executions: list[SourceTaskExecutionV4] = []
    bundles: dict[str, EvidenceOSExecutionBundleV4] = {}
    watchlist_items: list[DailyWatchlistItemV4] = []
    routed_rows: list[Mapping[str, Any]] = []
    feedback_retry_planner_runs: list[PlannerRunV4] = []
    run_index = 0
    planned_event_ids = {run.event.candidate_event_id for run in planner_runs}
    while run_index < len(planner_runs):
        run = planner_runs[run_index]
        run_index += 1
        event = run.event
        primary = _primary_from_planner(run)
        secondary = _secondary_from_planner(run)
        card = cards_by_id.get(primary or "")
        contract = contracts.get(primary or "") if primary else None
        item_planner_run = run
        tasks = ()
        bundle = None
        skip_source_due_runtime_budget = runtime_budget_exhausted or _runtime_budget_exhausted_v4(config=config, started_at=started_at)
        if skip_source_due_runtime_budget:
            runtime_budget_exhausted = True
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="source_execution_skipped_runtime_budget",
                candidate_event_id=event.candidate_event_id,
                symbol=event.symbol,
                company_name=event.company_name,
                run_index=run_index,
                planner_run_count=len(planner_runs),
                runtime_budget_seconds=config.runtime_budget_seconds,
            )
        _record_runtime_progress_v4(
            config=config,
            progress_events=runtime_progress_events,
            phase="planner_run_processing_start",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            run_index=run_index,
            planner_run_count=len(planner_runs),
            primary_archetype=primary,
            planner_provider_failed=run.provider_failed,
        )
        if not skip_source_due_runtime_budget and run.output and primary and card and contract:
            planner_tasks = source_tasks_from_planner_output_v4(
                event=event,
                planner_output=run.output,
                card_by_id=cards_by_id,
                max_tasks=config.max_source_tasks_per_plan,
                max_fetches_per_task=config.max_fetches_per_task,
            )
            event_origin_tasks = _event_origin_structured_replay_tasks(event=event, primary_archetype=primary, contract=contract)
            mandatory_official_tasks = _mandatory_official_status_tasks(event=event, primary_archetype=primary)
            tasks = tuple(
                (
                    *planner_tasks,
                    *event_origin_tasks,
                    *mandatory_official_tasks,
                )
            )
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="source_execution_start",
                candidate_event_id=event.candidate_event_id,
                symbol=event.symbol,
                company_name=event.company_name,
                primary_archetype=primary,
                source_task_count=len(tasks),
                planner_generated_source_task_count=len(planner_tasks),
                event_origin_source_task_count=len(event_origin_tasks),
                mandatory_official_source_task_count=len(mandatory_official_tasks),
                primitive_gaps=_primitive_gaps_from_tasks(tasks),
            )
            bundle = execute_source_tasks_with_evidence_os_v4(
                event=event,
                tasks=tasks,
                contract=contract,
                as_of_date=as_of_date,
                source_runner=source_runner,
                claim_extractor=claim_extractor,
                runtime_budget_exhausted=lambda: _runtime_budget_exhausted_v4(config=config, started_at=started_at),
            )
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="source_execution_end",
                candidate_event_id=event.candidate_event_id,
                symbol=event.symbol,
                company_name=event.company_name,
                source_task_execution_count=len(bundle.executions),
                accepted_claim_count=_accepted_claim_count_from_bundle(bundle),
                raw_assertion_count=len(bundle.raw_assertions),
                claim_extractor_run_count=len(bundle.claim_extractor_runs),
            )
            seen_retry_signatures: set[tuple[Any, ...]] = set()
            retry_attempt_count = 0
            while retry_attempt_count < max(0, config.retry_max - 1):
                if _runtime_budget_exhausted_v4(config=config, started_at=started_at):
                    runtime_budget_exhausted = True
                    _record_runtime_progress_v4(
                        config=config,
                        progress_events=runtime_progress_events,
                        phase="feedback_retry_skipped_runtime_budget",
                        candidate_event_id=event.candidate_event_id,
                        symbol=event.symbol,
                        company_name=event.company_name,
                        retry_attempt_number=retry_attempt_count + 1,
                        runtime_budget_seconds=config.runtime_budget_seconds,
                    )
                    break
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=runtime_progress_events,
                    phase="feedback_retry_planner_start",
                    candidate_event_id=event.candidate_event_id,
                    symbol=event.symbol,
                    company_name=event.company_name,
                    retry_attempt_number=retry_attempt_count + 1,
                    current_accepted_claim_count=_accepted_claim_count_from_bundle(bundle),
                )
                retry_run = _next_feedback_retry_planner_run(
                    planner_run=run,
                    bundle=bundle,
                    provider=planner_provider,
                    memory_cards=cards,
                    config=config,
                )
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=runtime_progress_events,
                    phase="feedback_retry_planner_end",
                    candidate_event_id=event.candidate_event_id,
                    symbol=event.symbol,
                    company_name=event.company_name,
                    retry_attempt_number=retry_attempt_count + 1,
                    retry_created=retry_run is not None,
                    retry_real_provider_success=bool(retry_run and retry_run.real_provider_success),
                    retry_provider_error=retry_run.provider_error if retry_run else None,
                )
                if retry_run is None:
                    break
                retry_signature = _feedback_retry_signature(retry_run)
                if retry_signature in seen_retry_signatures:
                    break
                seen_retry_signatures.add(retry_signature)
                feedback_retry_planner_runs.append(retry_run)
                _flush_runtime_planner_leafs_v4(
                    config=config,
                    planner_runs=tuple((*planner_runs, *feedback_retry_planner_runs)),
                )
                if not retry_run.output:
                    break
                retry_primary = _primary_from_planner(retry_run)
                retry_card = cards_by_id.get(retry_primary or "")
                retry_contract = contracts.get(retry_primary or "") if retry_primary else None
                retry_can_execute = bool(retry_primary and retry_card and retry_contract)
                if not retry_can_execute:
                    break
                retry_tasks = source_tasks_from_planner_output_v4(
                    event=event,
                    planner_output=retry_run.output,
                    card_by_id=cards_by_id,
                    max_tasks=config.max_source_tasks_per_plan,
                    max_fetches_per_task=config.max_fetches_per_task,
                )
                retry_tasks = tuple(
                    (
                        *retry_tasks,
                        *_event_origin_structured_replay_tasks(
                            event=event,
                            primary_archetype=retry_primary,
                            contract=retry_contract,
                        ),
                        *_mandatory_official_status_tasks(event=event, primary_archetype=retry_primary),
                    )
                )
                retry_reason_tag = (
                    _feedback_retry_reason_tag(retry_run)
                    if retry_run.source_rejection_feedback_count > 0 or retry_run.rerouted_claim_feedback_count > 0
                    else "rejected_claim_mapping"
                )
                rerouted_feedback = _rerouted_claim_feedback_from_bundle(bundle) if retry_run.rerouted_claim_feedback_count > 0 else ()
                retry_tasks, dropped_retry_executions = _deduplicated_feedback_retry_tasks_with_rejections(
                    event=event,
                    original_tasks=tasks,
                    retry_tasks=retry_tasks,
                    reason_tag=retry_reason_tag,
                    rerouted_claim_feedback=rerouted_feedback,
                )
                if dropped_retry_executions:
                    bundle = _append_retry_drop_executions_to_bundle(
                        bundle=bundle,
                        executions=dropped_retry_executions,
                    )
                if not retry_tasks:
                    break
                had_initial_acceptance = _bundle_has_accepted_claims(bundle)
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=runtime_progress_events,
                    phase="feedback_retry_source_execution_start",
                    candidate_event_id=event.candidate_event_id,
                    symbol=event.symbol,
                    company_name=event.company_name,
                    retry_attempt_number=retry_attempt_count + 1,
                    retry_primary_archetype=retry_primary,
                    retry_source_task_count=len(retry_tasks),
                    primitive_gaps=_primitive_gaps_from_tasks(retry_tasks),
                )
                retry_bundle = execute_source_tasks_with_evidence_os_v4(
                    event=event,
                    tasks=retry_tasks,
                    contract=retry_contract,
                    as_of_date=as_of_date,
                    source_runner=source_runner,
                    claim_extractor=claim_extractor,
                    runtime_budget_exhausted=lambda: _runtime_budget_exhausted_v4(config=config, started_at=started_at),
                )
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=runtime_progress_events,
                    phase="feedback_retry_source_execution_end",
                    candidate_event_id=event.candidate_event_id,
                    symbol=event.symbol,
                    company_name=event.company_name,
                    retry_attempt_number=retry_attempt_count + 1,
                    retry_source_task_execution_count=len(retry_bundle.executions),
                    retry_accepted_claim_count=_accepted_claim_count_from_bundle(retry_bundle),
                    total_accepted_claim_count=_accepted_claim_count_from_bundle(bundle)
                    + _accepted_claim_count_from_bundle(retry_bundle),
                )
                tasks = tuple((*tasks, *retry_tasks))
                bundle = _merge_evidence_os_bundles_v4(bundle, retry_bundle)
                if _bundle_has_accepted_claims(retry_bundle) and not had_initial_acceptance:
                    item_planner_run = retry_run
                    primary = retry_primary
                    secondary = _secondary_from_planner(retry_run)
                    card = retry_card
                    contract = retry_contract
                retry_attempt_count += 1
            executions.extend(bundle.executions)
            bundles[event.candidate_event_id] = bundle
        item = build_claim_backed_watchlist_item_v4(
            event=event,
            planner_run=item_planner_run,
            primary_archetype=primary,
            secondary_archetypes=secondary,
            card=card,
            contract=contract,
            tasks=tasks,
            bundle=bundle,
            as_of_date=as_of_date,
        )
        watchlist_items.append(item)
        routed_rows.append(
            {
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "event_type": event.event_type,
                "source_family": event.source_family,
                "primary_archetype": primary,
                "large_sector_id": large_sector_for_archetype(primary or "") if primary else None,
                "planner_provider_failed": item_planner_run.provider_failed,
                "source_task_count": len(tasks),
                "accepted_claim_count": _accepted_claim_count_from_bundle(bundle),
                "verified_score": item.verified_score,
                "base_stage": item.base_stage,
                "score_valid_status": item.score_valid_status,
            }
        )
        _record_runtime_progress_v4(
            config=config,
            progress_events=runtime_progress_events,
            phase="planner_run_processing_end",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            run_index=run_index,
            accepted_claim_count=_accepted_claim_count_from_bundle(bundle),
            verified_score=item.verified_score,
            base_stage=item.base_stage,
            score_valid_status=item.score_valid_status,
        )
        if run_index >= len(planner_runs) and _should_continue_for_accepted_claim_target(
            config=config,
            accepted_claim_count=_accepted_claim_count_from_bundles(bundles.values()),
            attempted_candidate_count=len(planned_event_ids),
        ):
            if _runtime_budget_exhausted_v4(config=config, started_at=started_at):
                runtime_budget_exhausted = True
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=runtime_progress_events,
                    phase="accepted_claim_target_plan_more_skipped_runtime_budget",
                    accepted_claim_count=_accepted_claim_count_from_bundles(bundles.values()),
                    attempted_candidate_count=len(planned_event_ids),
                    next_event_index=next_event_index,
                    runtime_budget_seconds=config.runtime_budget_seconds,
                )
                continue
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="accepted_claim_target_plan_more_start",
                accepted_claim_count=_accepted_claim_count_from_bundles(bundles.values()),
                attempted_candidate_count=len(planned_event_ids),
                next_event_index=next_event_index,
            )
            more_runs, next_event_index = _plan_more_events_for_accepted_claim_target(
                ordered_events=ordered_events,
                next_event_index=next_event_index,
                planned_event_ids=planned_event_ids,
                provider=planner_provider,
                cards=cards,
                config=config,
            )
            _record_runtime_progress_v4(
                config=config,
                progress_events=runtime_progress_events,
                phase="accepted_claim_target_plan_more_end",
                added_planner_run_count=len(more_runs),
                next_event_index=next_event_index,
            )
            if more_runs:
                more_runs = list(
                    _retry_planner_for_missing_external_web_plan(
                        planner_runs=more_runs,
                        provider=planner_provider,
                        memory_cards=cards,
                        config=config,
                        started_at=started_at,
                        progress_events=runtime_progress_events,
                    )
                )
                planner_runs.extend(more_runs)
                planned_event_ids.update(run.event.candidate_event_id for run in more_runs)
                _flush_runtime_planner_leafs_v4(config=config, planner_runs=planner_runs)
    if not runtime_budget_exhausted and _runtime_budget_exhausted_v4(config=config, started_at=started_at):
        runtime_budget_exhausted = True
        _record_runtime_progress_v4(
            config=config,
            progress_events=runtime_progress_events,
            phase="runtime_budget_exhausted_after_source_execution",
            next_event_index=next_event_index,
            planned_event_count=len(planner_runs),
            total_event_count=len(ordered_events),
            runtime_budget_seconds=config.runtime_budget_seconds,
        )
    for event in events:
        if event.candidate_event_id in planned_event_ids:
            continue
        pending_reason = (
            "planner_not_attempted_after_runtime_budget_exhausted"
            if runtime_budget_exhausted
            else "planner_not_attempted_after_real_planner_limit"
        )
        pending_provider_name = (
            "not_attempted_after_runtime_budget_exhausted"
            if runtime_budget_exhausted
            else "not_attempted_after_real_planner_limit"
        )
        pending_run = PlannerRunV4(
            event=event,
            provider_name=pending_provider_name,
            provider_mode=PlannerProviderModeV4.NONE.value,
            real_provider_exercised=False,
            real_provider_success=False,
            fake_provider_used=False,
            provider_error=pending_reason,
        )
        planner_runs.append(pending_run)
        _flush_runtime_planner_leafs_v4(config=config, planner_runs=planner_runs)
        item = build_claim_backed_watchlist_item_v4(
            event=event,
            planner_run=pending_run,
            primary_archetype=None,
            secondary_archetypes=(),
            card=None,
            contract=None,
            tasks=(),
            bundle=None,
            as_of_date=as_of_date,
        )
        watchlist_items.append(item)
        routed_rows.append(
            {
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "event_type": event.event_type,
                "source_family": event.source_family,
                "primary_archetype": None,
                "large_sector_id": None,
                "planner_provider_failed": pending_run.provider_failed,
                "source_task_count": 0,
                "accepted_claim_count": 0,
                "verified_score": item.verified_score,
                "base_stage": item.base_stage,
                "score_valid_status": item.score_valid_status,
            }
        )
    candidate_report = build_candidate_event_report_v4(events=events, routed_rows=routed_rows)
    all_planner_runs = tuple((*planner_runs, *feedback_retry_planner_runs))
    _flush_runtime_planner_leafs_v4(config=config, planner_runs=all_planner_runs)
    planner_report = build_real_planner_report_v4(all_planner_runs)
    source_report = build_source_acquisition_report_v4(executions)
    extraction_audit = build_evidence_extraction_audit_v4(bundles.values())
    watchlist_report = build_daily_watchlist_report_v4(watchlist_items)
    static_audit = build_static_logic_audit_from_reports_v4(
        planner_report=planner_report,
        source_report=source_report,
        extraction_audit=extraction_audit,
        watchlist_report=watchlist_report,
        config=config.to_dict(),
    )
    readiness = build_v4_readiness_verdict(
        candidate_report=candidate_report,
        planner_report=planner_report,
        source_report=source_report,
        extraction_audit=extraction_audit,
        watchlist_report=watchlist_report,
        static_audit=static_audit,
        multi_day_shadow={"summary": {"five_day_run_count": 0}},
    )
    _record_runtime_progress_v4(
        config=config,
        progress_events=runtime_progress_events,
        phase="completed",
        planner_run_count=len(all_planner_runs),
        source_task_execution_count=len(executions),
        watchlist_item_count=len(watchlist_items),
        real_provider_success_count=int(planner_report["summary"].get("real_provider_success_count") or 0),
        accepted_claim_count=int(source_report["summary"].get("accepted_claim_count") or 0),
        runtime_budget_exhausted=runtime_budget_exhausted,
        runtime_elapsed_seconds=round(time.monotonic() - started_at, 6),
    )
    return {
        "config": config.to_dict(),
        "cards": cards,
        "events": events,
        "candidate_report": candidate_report,
        "sector_coverage_report": build_sector_coverage_report_v4(routed_rows),
        "planner_report": planner_report,
        "source_acquisition_report": source_report,
        "source_provider_gap_report": build_source_provider_gap_report_v4(executions),
        "evidence_extraction_audit": extraction_audit,
        "watchlist_report": watchlist_report,
        "static_audit": static_audit,
        "readiness": readiness,
        "watchlist_items": watchlist_items,
        "planner_runs": all_planner_runs,
        "executions": tuple(executions),
        "bundles": bundles,
    }


def _flush_runtime_planner_leafs_v4(
    *,
    config: ProductionShadowV4Config,
    planner_runs: Sequence[PlannerRunV4],
) -> None:
    root = _runtime_output_root_v4(config)
    if root is None:
        return
    root.mkdir(parents=True, exist_ok=True)
    rows = [run.to_dict() for run in planner_runs]
    _write_runtime_jsonl_v4(root / "planner_runs.jsonl", rows)
    prompt_rows: list[dict[str, Any]] = []
    response_rows: list[dict[str, Any]] = []
    for run in planner_runs:
        event = run.event
        if run.prompt_hash:
            prompt_rows.append(
                {
                    "schema_version": "research_brain_v4_planner_prompt_leaf_v1",
                    "planner_run_id": run.planner_run_id,
                    "candidate_event_id": event.candidate_event_id,
                    "symbol": event.symbol,
                    "provider_name": run.provider_name,
                    "model": run.model,
                    "prompt_hash": run.prompt_hash,
                    "raw_prompt_path": run.raw_prompt_path,
                }
            )
        if run.response_hash:
            response_rows.append(
                {
                    "schema_version": "research_brain_v4_planner_response_leaf_v1",
                    "planner_run_id": run.planner_run_id,
                    "candidate_event_id": event.candidate_event_id,
                    "symbol": event.symbol,
                    "provider_name": run.provider_name,
                    "model": run.model,
                    "response_hash": run.response_hash,
                    "raw_response_path": run.raw_response_path,
                }
            )
    _write_runtime_jsonl_v4(root / "llm_prompts.jsonl", prompt_rows)
    _write_runtime_jsonl_v4(root / "llm_responses.jsonl", response_rows)


def _runtime_output_root_v4(config: ProductionShadowV4Config) -> Path | None:
    if not config.runtime_progress_path:
        return None
    return Path(config.runtime_progress_path).parent


def _write_runtime_jsonl_v4(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True, default=str) + "\n" for row in rows)
    tmp_path = path.with_name(path.name + ".tmp")
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def _record_runtime_progress_v4(
    *,
    config: ProductionShadowV4Config,
    progress_events: list[dict[str, Any]],
    phase: str,
    **payload: Any,
) -> None:
    if not config.runtime_progress_path:
        return
    now = datetime.now(timezone.utc).isoformat()
    event = {
        "event_index": len(progress_events) + 1,
        "created_at_utc": now,
        "phase": phase,
        **payload,
    }
    progress_events.append(event)
    progress_path = Path(config.runtime_progress_path)
    progress_path.parent.mkdir(parents=True, exist_ok=True)
    recent_events = progress_events[-200:]
    document = {
        "schema_version": "e2r_research_brain_v4_runtime_progress_v1",
        "status": "COMPLETED" if phase == "completed" else "RUNNING",
        "updated_at_utc": now,
        "pid": os.getpid(),
        "latest_phase": phase,
        "event_count": len(progress_events),
        "recent_event_count": len(recent_events),
        "latest_event": event,
        "recent_events": recent_events,
        "config": {
            "as_of_date": config.as_of_date,
            "planner_provider": config.planner_provider,
            "source_acquisition": config.source_acquisition,
            "candidate_event_seed_path": config.candidate_event_seed_path,
            "universe_limit": config.universe_limit,
            "planner_success_limit": config.planner_success_limit,
            "planner_batch_size": config.planner_batch_size,
            "max_source_tasks_per_plan": config.max_source_tasks_per_plan,
            "max_fetches_per_task": config.max_fetches_per_task,
            "accepted_claim_target": config.accepted_claim_target,
            "max_distinct_candidate_attempts": config.max_distinct_candidate_attempts,
            "retry_max": config.retry_max,
            "claim_extractor_provider": config.claim_extractor_provider,
            "claim_extractor_timeout_seconds": config.claim_extractor_timeout_seconds,
            "runtime_budget_seconds": config.runtime_budget_seconds,
        },
    }
    tmp_path = progress_path.with_name(progress_path.name + ".tmp")
    tmp_path.write_text(json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    tmp_path.replace(progress_path)


def _runtime_budget_exhausted_v4(*, config: ProductionShadowV4Config, started_at: float) -> bool:
    if config.runtime_budget_seconds is None:
        return False
    return (time.monotonic() - started_at) >= float(config.runtime_budget_seconds)


def _runtime_budget_remaining_seconds_v4(*, config: ProductionShadowV4Config, started_at: float) -> float | None:
    if config.runtime_budget_seconds is None:
        return None
    return max(0.0, float(config.runtime_budget_seconds) - (time.monotonic() - started_at))


def _source_execution_reserved_budget_seconds_v4(*, config: ProductionShadowV4Config) -> float:
    timeout = float(config.claim_extractor_timeout_seconds or 0.0)
    if timeout <= 0:
        return 30.0
    return max(30.0, min(90.0, timeout * 3.0))


def _optional_retry_would_starve_source_execution_v4(*, config: ProductionShadowV4Config, started_at: float) -> bool:
    remaining = _runtime_budget_remaining_seconds_v4(config=config, started_at=started_at)
    if remaining is None:
        return False
    return remaining < _source_execution_reserved_budget_seconds_v4(config=config)


def _primitive_gaps_from_tasks(tasks: Sequence[SourceTask]) -> list[str]:
    gaps: list[str] = []
    for task in tasks:
        gap = task.get("primitive_gap") if isinstance(task, Mapping) else getattr(task, "primitive_gap", "")
        if gap and str(gap) not in gaps:
            gaps.append(str(gap))
    return gaps


def _claim_extractor_for_config(
    *,
    config: ProductionShadowV4Config,
    repo_root: str | Path,
    started_at: float | None = None,
) -> LLMContractBlindRawAssertionExtractor:
    """Select the unstructured-text claim extractor for the v4 run mode.

    Frozen snapshots and fixture-like paths stay on the deterministic fallback
    so unit tests and replay audits do not spawn external tools. Live full
    source acquisition uses the Codex CLI-backed extractor by default, because
    Brain/Web evidence pass must leave a provider_mode=llm extraction trace.
    """

    mode = ClaimExtractorProviderModeV4(config.claim_extractor_provider)
    if mode == ClaimExtractorProviderModeV4.AUTO:
        mode = (
            ClaimExtractorProviderModeV4.CODEX_CLI
            if config.source_acquisition == SourceAcquisitionModeV4.LIVE_FULL_BOUNDED.value
            and config.planner_provider not in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}
            else ClaimExtractorProviderModeV4.RULE_FALLBACK
        )
    if mode == ClaimExtractorProviderModeV4.CODEX_CLI:
        return LLMContractBlindRawAssertionExtractor(
            provider=CodexCLIExtractorProvider(
                repo_root=repo_root,
                timeout_seconds=config.claim_extractor_timeout_seconds,
                remaining_budget_seconds=(
                    (lambda: _runtime_budget_remaining_seconds_v4(config=config, started_at=started_at))
                    if started_at is not None
                    else None
                ),
            )
        )
    return LLMContractBlindRawAssertionExtractor(provider=RuleFallbackExtractorProvider())


def discover_daily_candidate_events_v4(
    *,
    repo_root: str | Path,
    as_of_date: date,
    universe_limit: int,
) -> tuple[CandidateEventV2, ...]:
    root = Path(repo_root)
    rows: list[CandidateEventV2] = []
    rows.extend(_production_cutover_leaf_candidate_events(root=root, as_of_date=as_of_date, limit=max(15, universe_limit)))
    rows.extend(_official_source_events(root=root, as_of_date=as_of_date, limit=max(15, universe_limit)))
    cache_root = root / "data/cache/company_guide"
    company_guide_limit = max(universe_limit * 4, universe_limit + 20)
    company_guide_count = 0
    for path in sorted(cache_root.glob("*/??????_recent_reports.json"), reverse=True):
        if company_guide_count >= company_guide_limit:
            break
        symbol = path.name.split("_", 1)[0]
        payload = _load_json(path)
        if not isinstance(payload, Mapping):
            continue
        lists = [row for row in payload.get("lists") or () if isinstance(row, Mapping)]
        if not lists:
            continue
        for first in lists[:3]:
            if company_guide_count >= company_guide_limit:
                break
            publish_date = _yy_mm_dd_date(first.get("ANL_DT"), as_of_date) or _date_from_path(path) or as_of_date
            if publish_date > as_of_date:
                continue
            company = str(first.get("CMP_NM_KOR") or symbol)
            comment = _strip_html(str(first.get("COMMENT") or first.get("COMMENT2") or ""))
            title = str(first.get("RPT_TITLE") or "CompanyGuide report radar")
            rpt_id = str(first.get("RPT_ID") or title or "no_rpt_id")
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-CG-{symbol}-{rpt_id}-{publish_date.isoformat()}",
                    symbol=symbol,
                    company_name=company,
                    event_date=publish_date.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="CompanyGuide",
                    source_id=str(path),
                    event_type="report_radar",
                    raw_reason_codes=tuple(_reason_codes_from_report(first, comment)),
                    primary_disclosure_type=None,
                    event_title=title,
                    event_summary=f"{title}. {comment[:500]}",
                    magnitude=EventMagnitudeV2(),
                    event_freshness_days=max(0, (as_of_date - publish_date).days),
                    issuer_directness="DIRECT",
                    structured_payload={"snapshot_path": str(path), "report_count": len(lists), "rpt_id": rpt_id},
                    research_brain_eligible=True,
                )
            )
            company_guide_count += 1
    rows.extend(_historical_source_events(root=root, as_of_date=as_of_date, limit=max(15, universe_limit)))
    return _select_unique_candidate_events(rows, limit=universe_limit)


def _candidate_seed_events_from_config(
    *,
    config: ProductionShadowV4Config,
    as_of_date: date,
    repo_root: str | Path = ".",
) -> tuple[CandidateEventV2, ...]:
    if not config.candidate_event_seed_path:
        return ()
    path = Path(config.candidate_event_seed_path)
    if not path.exists():
        return ()
    rows: list[CandidateEventV2] = []
    registry = load_instrument_registry(repo_root)
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if not text:
                continue
            payload = json.loads(text)
            if payload.get("research_brain_eligible") is False:
                continue
            event_date = _date_from_any(payload.get("event_date") or payload.get("as_of_date")) or as_of_date
            if event_date > as_of_date:
                continue
            structured_payload = dict(payload.get("structured_payload") or payload)
            target_symbol_mode = str(payload.get("target_symbol_mode") or structured_payload.get("target_symbol_mode") or "")
            seed_role = str(payload.get("seed_role") or structured_payload.get("seed_role") or "")
            source_family = str(payload.get("source_family") or "CensusFullThesisQueue")
            is_archetype_level_planner_seed = (
                target_symbol_mode == "ARCHETYPE_LEVEL_DISCOVERY"
                and seed_role == "planner_input_only"
                and source_family == "AllArchetypeRuntimeParityFollowUp"
            )
            raw_symbol = str(payload.get("symbol") or "").strip()
            symbol = raw_symbol.zfill(6) if raw_symbol else ""
            if not raw_symbol and not is_archetype_level_planner_seed:
                continue
            if raw_symbol and not symbol.strip("0"):
                continue
            target_archetype = str(structured_payload.get("target_archetype") or payload.get("target_archetype") or "")
            company_name = _seed_event_company_name(
                payload=payload,
                structured_payload=structured_payload,
                symbol=symbol,
                registry=registry,
                target_archetype=target_archetype,
                is_archetype_level_planner_seed=is_archetype_level_planner_seed,
            )
            rows.append(
                CandidateEventV2(
                    candidate_event_id=str(payload.get("candidate_event_id") or f"CEV4-SEED-{symbol}-{event_date.isoformat()}"),
                    symbol=symbol,
                    company_name=company_name,
                    event_date=event_date.isoformat(),
                    detected_at=str(payload.get("detected_at") or as_of_date.isoformat()),
                    source_family=source_family,
                    source_id=str(payload.get("source_id") or path),
                    event_type=str(payload.get("event_type") or "full_thesis_refresh_seed"),
                    raw_reason_codes=tuple(str(item) for item in payload.get("raw_reason_codes") or ()),
                    primary_disclosure_type=payload.get("primary_disclosure_type"),
                    event_title=str(payload.get("event_title") or f"{symbol} full thesis refresh seed"),
                    event_summary=str(payload.get("event_summary") or ""),
                    event_freshness_days=max(0, (as_of_date - event_date).days),
                    issuer_directness=str(payload.get("issuer_directness") or ("INDUSTRY" if is_archetype_level_planner_seed else "DIRECT")),
                    structured_payload=structured_payload,
                    research_brain_eligible=payload.get("research_brain_eligible") is not False,
                )
            )
    return tuple(rows)


def _seed_event_company_name(
    *,
    payload: Mapping[str, Any],
    structured_payload: Mapping[str, Any],
    symbol: str,
    registry: Any,
    target_archetype: str,
    is_archetype_level_planner_seed: bool,
) -> str:
    raw_name = str(payload.get("company_name") or structured_payload.get("company_name") or "").strip()
    if raw_name and raw_name != target_archetype and not _looks_like_archetype_id(raw_name):
        return raw_name
    if symbol:
        registry_name = str(getattr(registry, "names_by_symbol", {}).get(symbol) or "").strip()
        if registry_name:
            return registry_name
        return symbol
    if is_archetype_level_planner_seed:
        return target_archetype or "ARCHETYPE_LEVEL_DISCOVERY"
    return raw_name or target_archetype or "UNKNOWN_COMPANY"


def _looks_like_archetype_id(value: str) -> bool:
    return bool(re.match(r"^(?:C\d{2}|R13)_", str(value or "").strip()))


def _production_cutover_leaf_candidate_events(*, root: Path, as_of_date: date, limit: int) -> list[CandidateEventV2]:
    """Load URL-backed live official candidate events before cached fallbacks.

    Easy example: if the leaf artifact already has
    ``CE-LIVE-DART-396470-20260624900961`` with a DART viewer URL, a live
    official Brain probe should plan on that before spending the only real
    planner slot on ``data/cache/company_guide/...``.
    """

    rows: list[CandidateEventV2] = []
    cutover_root = root / "output" / "production_cutover_v3"
    if not cutover_root.exists():
        return rows
    day_roots = sorted(
        (
            path
            for path in cutover_root.glob("20??-??-??")
            if path.is_dir() and _date_from_any(path.name) and _date_from_any(path.name) <= as_of_date
        ),
        reverse=True,
    )
    for day_root in day_roots:
        if len(rows) >= limit:
            break
        payload = _load_json(day_root / "candidate_events.json")
        if not isinstance(payload, list):
            continue
        for row in payload:
            if len(rows) >= limit:
                break
            if not isinstance(row, Mapping):
                continue
            event = _candidate_event_from_leaf_row(row=row, as_of_date=as_of_date)
            if event is not None:
                rows.append(event)
    return rows


def _candidate_event_from_leaf_row(*, row: Mapping[str, Any], as_of_date: date) -> CandidateEventV2 | None:
    symbol = str(row.get("symbol") or "").zfill(6)
    if not symbol.strip("0"):
        return None
    event_date = _date_from_any(row.get("event_date") or row.get("detected_at"))
    if event_date is None or event_date > as_of_date:
        return None
    source_id = str(row.get("source_id") or "")
    source_family = str(row.get("source_family") or "")
    if not source_id or not source_family:
        return None
    raw_reason_codes = row.get("raw_reason_codes") or ()
    if isinstance(raw_reason_codes, str):
        raw_reason_codes = (raw_reason_codes,)
    elif not isinstance(raw_reason_codes, Sequence):
        raw_reason_codes = ()
    return CandidateEventV2(
        candidate_event_id=str(row.get("candidate_event_id") or f"CEV4-LEAF-{symbol}-{event_date.isoformat()}"),
        symbol=symbol,
        company_name=str(row.get("company_name") or symbol),
        event_date=event_date.isoformat(),
        detected_at=str(row.get("detected_at") or as_of_date.isoformat()),
        source_family=source_family,
        source_id=source_id,
        event_type=str(row.get("event_type") or row.get("event_title") or "production_cutover_leaf_event"),
        raw_reason_codes=tuple(str(code) for code in raw_reason_codes if str(code).strip()),
        primary_disclosure_type=str(row.get("event_type") or row.get("primary_disclosure_type") or ""),
        event_title=str(row.get("event_title") or row.get("event_type") or ""),
        event_summary=str(row.get("event_summary") or row.get("event_title") or "")[:700],
        magnitude=EventMagnitudeV2(),
        event_freshness_days=max(0, (as_of_date - event_date).days),
        issuer_directness=str(row.get("issuer_directness") or "UNKNOWN"),
        structured_payload=row.get("structured_payload") if isinstance(row.get("structured_payload"), Mapping) else dict(row),
        research_brain_eligible=bool(row.get("research_brain_eligible", True)),
    )


def _planner_candidate_order(
    *,
    events: Sequence[CandidateEventV2],
    config: ProductionShadowV4Config,
    repo_root: str | Path,
    as_of_date: date,
) -> tuple[CandidateEventV2, ...]:
    """Prioritize production-live candidates before fixture/cache examples.

    Easy example: a stored fixture symbol like ``111111`` can be useful in
    frozen replay tests, but it should not be the first real Codex/OpenDART
    planner target in a live official acquisition run. The candidate can remain
    in the diagnostic event report; it just should not consume the scarce live
    planner slot before a real KRX symbol.
    """

    live_modes = {
        SourceAcquisitionModeV4.LIVE_OFFICIAL_FIRST.value,
        SourceAcquisitionModeV4.LIVE_OFFICIAL_ONLY.value,
        SourceAcquisitionModeV4.LIVE_FULL_BOUNDED.value,
    }
    if config.source_acquisition not in live_modes:
        return tuple(events)
    registry = load_instrument_registry(repo_root)

    def sort_key(event: CandidateEventV2) -> tuple[int, int, int, int, int, int, str]:
        eligibility = evaluate_candidate_event_production_eligibility(
            event,
            registry=registry,
            mode=ProductionMode.PRODUCTION_SHADOW_LIVE,
            repo_root=repo_root,
            as_of_date=as_of_date.isoformat(),
        )
        queue_seed_priority = 0 if _is_full_thesis_refresh_seed_event(event) else 1
        fixture_penalty = 1 if eligibility.fixture_like_symbol else 0
        source_penalty = 1 if eligibility.source_id_cached_or_fixture or eligibility.source_id_snapshot_uri else 0
        return (
            queue_seed_priority,
            0 if eligibility.eligible else 1,
            fixture_penalty,
            source_penalty,
            _candidate_evidence_likelihood_rank(event),
            max(0, int(event.event_freshness_days or 0)),
            event.candidate_event_id,
        )

    return tuple(sorted(events, key=sort_key))


def _is_full_thesis_refresh_seed_event(event: CandidateEventV2) -> bool:
    structured = event.structured_payload if isinstance(event.structured_payload, Mapping) else {}
    return (
        str(event.source_family or "") == "CensusFullThesisQueue"
        or str(event.source_family or "") == "AllArchetypeRuntimeParityFollowUp"
        or str(event.event_type or "") == "full_thesis_refresh_seed"
        or str(event.event_type or "") == "all_archetype_runtime_parity_follow_up_seed"
        or str(structured.get("seed_role") or "") == "planner_input_only"
    )


def _candidate_evidence_likelihood_rank(event: CandidateEventV2) -> int:
    """Return an investigation-order bucket, never a score signal.

    Easy example: a direct sales-contract disclosure is more likely to produce a
    score-eligible claim than a facility-investment end-date correction. That
    only decides which candidate gets the scarce live planner slot first. It
    does not make either candidate score-eligible.
    """

    source_family = str(event.source_family or "").strip().lower()
    text = _candidate_event_text(event)
    has_contract = _contains_any(
        text,
        (
            "단일판매",
            "공급계약",
            "판매계약",
            "수주",
            "supply contract",
            "sales contract",
            "order backlog",
        ),
    )
    has_report = source_family in {"companyguide", "report", "researchreport"} or _contains_any(
        text,
        (
            "report_radar",
            "리포트",
            "실적",
            "컨센서스",
            "목표주가",
            "상향",
            "revision",
            "guidance",
            "earnings",
        ),
    )
    has_facility = _contains_any(text, ("신규시설투자", "시설투자", "공장", "증설", "capacity", "capa"))
    has_admin_or_correction = _contains_any(
        text,
        (
            "정정",
            "종료일 연장",
            "연장",
            "관리종목",
            "거래정지",
            "해명공시",
            "자기주식",
            "주식담보",
            "유상증자",
            "기재정정",
        ),
    )
    if has_contract and not has_admin_or_correction:
        return 0
    if has_contract:
        return 1
    if has_report:
        return 2
    if source_family in {"issuerir", "issuerofficial", "ir"}:
        return 3
    if has_facility and not has_admin_or_correction:
        return 4
    if source_family in {"dart", "opendart", "kind", "krx", "trustednews"} and not has_admin_or_correction:
        return 5
    if has_facility:
        return 6
    if has_admin_or_correction:
        return 7
    return 8


def _candidate_event_text(event: CandidateEventV2) -> str:
    structured = event.structured_payload if isinstance(event.structured_payload, Mapping) else {}
    return " ".join(
        str(value or "")
        for value in (
            event.source_family,
            event.event_type,
            event.primary_disclosure_type,
            event.event_title,
            event.event_summary,
            " ".join(str(code) for code in event.raw_reason_codes),
            json.dumps(structured, ensure_ascii=False, sort_keys=True),
        )
    ).lower()


def _contains_any(text: str, tokens: Sequence[str]) -> bool:
    return any(str(token).lower() in text for token in tokens)


def _should_continue_for_accepted_claim_target(
    *,
    config: ProductionShadowV4Config,
    accepted_claim_count: int,
    attempted_candidate_count: int,
) -> bool:
    if config.accepted_claim_target <= 0:
        return False
    if config.planner_provider in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}:
        return False
    if accepted_claim_count >= config.accepted_claim_target:
        return False
    return attempted_candidate_count < config.max_distinct_candidate_attempts


def _plan_more_events_for_accepted_claim_target(
    *,
    ordered_events: Sequence[CandidateEventV2],
    next_event_index: int,
    planned_event_ids: set[str],
    provider: ResearchBrainPlannerProviderV4 | None,
    cards: Sequence[ArchetypeMemoryCard],
    config: ProductionShadowV4Config,
) -> tuple[list[PlannerRunV4], int]:
    if provider is None:
        return [], next_event_index
    batch: list[CandidateEventV2] = []
    cursor = next_event_index
    while cursor < len(ordered_events) and len(batch) < config.planner_batch_size:
        event = ordered_events[cursor]
        cursor += 1
        if event.candidate_event_id in planned_event_ids:
            continue
        batch.append(event)
    if not batch:
        return [], cursor
    return (
        list(
            run_planner_provider_v4(
                provider=provider,
                events=tuple(batch),
                memory_cards=cards,
                existing_evidence_by_event_id=_evidence_context_by_event(events=tuple(batch), config=config),
            )
        ),
        cursor,
    )


def _accepted_claim_count_from_bundles(bundles: Sequence[EvidenceOSExecutionBundleV4]) -> int:
    return len(
        {
            claim_id
            for bundle in bundles
            for execution in bundle.executions
            for claim_id in execution.accepted_claim_ids
        }
    )


def _accepted_claim_count_from_bundle(bundle: EvidenceOSExecutionBundleV4 | None) -> int:
    if bundle is None:
        return 0
    return len(
        {
            claim_id
            for execution in bundle.executions
            for claim_id in execution.accepted_claim_ids
        }
    )


def _discovery_limit_for_config(config: ProductionShadowV4Config) -> int:
    live_modes = {
        SourceAcquisitionModeV4.LIVE_OFFICIAL_FIRST.value,
        SourceAcquisitionModeV4.LIVE_OFFICIAL_ONLY.value,
        SourceAcquisitionModeV4.LIVE_FULL_BOUNDED.value,
    }
    if config.source_acquisition not in live_modes or config.planner_provider == PlannerProviderModeV4.FAKE.value:
        return config.universe_limit
    return max(config.universe_limit, config.planner_success_limit * 10, config.planner_success_limit + 20)


def run_multi_day_shadow_v4(
    *,
    base_config: ProductionShadowV4Config,
    v1_archetype_matrix: Mapping[str, Any],
    repo_root: str | Path = ".",
    planner_provider_factory: Any | None = None,
) -> Mapping[str, Any]:
    base_day = date.fromisoformat(base_config.as_of_date)
    days = tuple(base_day - timedelta(days=offset) for offset in (0, 1, 2, 3, 4))
    rows = []
    signatures = []
    frozen_repeat_provider: FrozenRealPlannerProviderV4 | None = None
    for day in days:
        provider = planner_provider_factory() if planner_provider_factory else build_planner_provider_v4(
            mode=base_config.planner_provider,
            working_directory=repo_root,
        )
        config = ProductionShadowV4Config(
            as_of_date=day.isoformat(),
            planner_provider=base_config.planner_provider,
            source_acquisition=base_config.source_acquisition,
            universe_limit=base_config.universe_limit,
            planner_success_limit=base_config.planner_success_limit,
            planner_batch_size=base_config.planner_batch_size,
            max_source_tasks_per_plan=base_config.max_source_tasks_per_plan,
            max_fetches_per_task=base_config.max_fetches_per_task,
            accepted_claim_target=base_config.accepted_claim_target,
            max_distinct_candidate_attempts=base_config.max_distinct_candidate_attempts,
            top_results=base_config.top_results,
            retry_max=base_config.retry_max,
            claim_extractor_provider=base_config.claim_extractor_provider,
            claim_extractor_timeout_seconds=base_config.claim_extractor_timeout_seconds,
            runtime_budget_seconds=base_config.runtime_budget_seconds,
            fake_provider_allowed=base_config.fake_provider_allowed,
        )
        result = run_research_brain_v4_production_shadow(
            config=config,
            v1_archetype_matrix=v1_archetype_matrix,
            planner_provider=provider,
            repo_root=repo_root,
        )
        if day == base_day:
            frozen_repeat_provider = _frozen_real_planner_provider_from_result(result)
        signature = _watchlist_signature(result["watchlist_report"])
        signatures.append(signature)
        rows.append(
            {
                "as_of_date": day.isoformat(),
                "candidate_event_count": result["candidate_report"]["summary"]["candidate_event_count"],
                "unique_candidate_event_count": result["candidate_report"]["summary"].get("unique_candidate_event_count"),
                "real_provider_success_count": result["planner_report"]["summary"]["real_provider_success_count"],
                "unique_real_provider_success_count": result["planner_report"]["summary"].get("unique_real_provider_success_count"),
                "fake_provider_used_count": result["planner_report"]["summary"]["fake_provider_used_count"],
                "real_document_fetched_count": result["source_acquisition_report"]["summary"]["real_document_fetched_count"],
                "unique_real_document_fetched_count": result["source_acquisition_report"]["summary"].get("unique_real_document_fetched_count"),
                "accepted_claim_count": result["evidence_extraction_audit"]["summary"]["adjudicated_claim_to_accepted_claim_count"],
                "deterministic_stage_output_count": result["watchlist_report"]["summary"]["deterministic_scorer_output_count"],
                "unique_deterministic_stage_output_count": result["watchlist_report"]["summary"].get("unique_deterministic_scorer_output_count"),
                "provider_failure_count": result["planner_report"]["summary"]["real_provider_failure_count"],
                "watchlist_signature": signature,
            }
        )
    repeat_rows = []
    repeat_signatures = []
    repeat_day = base_day
    for repeat_index in range(3):
        provider = frozen_repeat_provider or (
            planner_provider_factory() if planner_provider_factory else build_planner_provider_v4(
                mode=base_config.planner_provider,
                working_directory=repo_root,
            )
        )
        config = ProductionShadowV4Config(
            as_of_date=repeat_day.isoformat(),
            planner_provider=base_config.planner_provider,
            source_acquisition=base_config.source_acquisition,
            universe_limit=base_config.universe_limit,
            planner_success_limit=base_config.planner_success_limit,
            planner_batch_size=base_config.planner_batch_size,
            max_source_tasks_per_plan=base_config.max_source_tasks_per_plan,
            max_fetches_per_task=base_config.max_fetches_per_task,
            accepted_claim_target=base_config.accepted_claim_target,
            max_distinct_candidate_attempts=base_config.max_distinct_candidate_attempts,
            top_results=base_config.top_results,
            retry_max=base_config.retry_max,
            claim_extractor_provider=base_config.claim_extractor_provider,
            claim_extractor_timeout_seconds=base_config.claim_extractor_timeout_seconds,
            runtime_budget_seconds=base_config.runtime_budget_seconds,
            fake_provider_allowed=base_config.fake_provider_allowed,
        )
        result = run_research_brain_v4_production_shadow(
            config=config,
            v1_archetype_matrix=v1_archetype_matrix,
            planner_provider=provider,
            repo_root=repo_root,
        )
        signature = _watchlist_signature(result["watchlist_report"])
        repeat_signatures.append(signature)
        repeat_rows.append(
            {
                "repeat_index": repeat_index,
                "repeat_mode": "frozen_real_planner_snapshot" if frozen_repeat_provider is not None else "live_planner_fallback",
                "as_of_date": repeat_day.isoformat(),
                "candidate_event_count": result["candidate_report"]["summary"]["candidate_event_count"],
                "unique_candidate_event_count": result["candidate_report"]["summary"].get("unique_candidate_event_count"),
                "real_provider_success_count": result["planner_report"]["summary"]["real_provider_success_count"],
                "unique_real_provider_success_count": result["planner_report"]["summary"].get("unique_real_provider_success_count"),
                "real_document_fetched_count": result["source_acquisition_report"]["summary"]["real_document_fetched_count"],
                "unique_real_document_fetched_count": result["source_acquisition_report"]["summary"].get("unique_real_document_fetched_count"),
                "deterministic_stage_output_count": result["watchlist_report"]["summary"]["deterministic_scorer_output_count"],
                "unique_deterministic_stage_output_count": result["watchlist_report"]["summary"].get("unique_deterministic_scorer_output_count"),
                "watchlist_signature": signature,
            }
        )
    repeated_variance = len(set(repeat_signatures)) - 1 if repeat_signatures else 1
    return {
        "schema_version": "research_brain_v4_multi_day_shadow_runs",
        "summary": {
            "five_day_run_count": len(rows),
            "real_provider_success_count_total": sum(row["real_provider_success_count"] for row in rows),
            "real_document_fetched_total": sum(row["real_document_fetched_count"] for row in rows),
            "unique_real_document_fetched_total": sum(
                int(row.get("unique_real_document_fetched_count") or row["real_document_fetched_count"])
                for row in rows
            ),
            "accepted_claim_total": sum(row["accepted_claim_count"] for row in rows),
            "deterministic_stage_output_total": sum(row["deterministic_stage_output_count"] for row in rows),
            "unique_deterministic_stage_output_total": sum(
                int(row.get("unique_deterministic_stage_output_count") or row["deterministic_stage_output_count"])
                for row in rows
            ),
            "fake_provider_used_total": sum(row["fake_provider_used_count"] for row in rows),
            "repeat_run_count": len(repeat_rows),
            "repeated_frozen_run_variance": repeated_variance,
            "production_ready_despite_provider_gap": 0,
            "max_signature_variance_count": len(set(signatures)) - 1 if signatures else 0,
        },
        "rows": rows,
        "repeat_rows": repeat_rows,
    }


def _frozen_real_planner_provider_from_result(result: Mapping[str, Any]) -> FrozenRealPlannerProviderV4 | None:
    outputs = {
        run.event.candidate_event_id: run.output
        for run in result.get("planner_runs", ())
        if isinstance(run, PlannerRunV4) and run.real_provider_success and run.output is not None
    }
    if not outputs:
        return None
    return FrozenRealPlannerProviderV4(outputs_by_event_id=outputs)


def build_real_planner_report_v4(planner_runs: Sequence[PlannerRunV4]) -> Mapping[str, Any]:
    initial_runs = tuple(run for run in planner_runs if run.planner_run_role != "feedback_retry")
    retry_runs = tuple(run for run in planner_runs if run.planner_run_role == "feedback_retry")
    unique_event_ids = {run.event.candidate_event_id for run in initial_runs}
    unique_all_event_ids = {run.event.candidate_event_id for run in planner_runs}
    unique_success_event_ids = {
        run.event.candidate_event_id
        for run in planner_runs
        if run.real_provider_success
    }
    return {
        "schema_version": "research_brain_v4_real_planner_report",
        "summary": {
            "planner_run_count": len(planner_runs),
            "initial_planner_run_count": len(initial_runs),
            "feedback_retry_planner_run_count": len(retry_runs),
            "unique_planner_candidate_count": len(unique_event_ids),
            "unique_planner_event_count_including_retries": len(unique_all_event_ids),
            "real_provider_attempt_count": sum(run.provider_mode == PlannerProviderModeV4.REAL.value for run in planner_runs),
            "real_provider_success_count": sum(run.real_provider_success for run in planner_runs),
            "unique_real_provider_success_count": len(unique_success_event_ids),
            "real_provider_failure_count": sum(run.provider_failed and run.provider_mode == PlannerProviderModeV4.REAL.value for run in planner_runs),
            "planner_not_attempted_count": sum(
                run.provider_mode == PlannerProviderModeV4.NONE.value for run in initial_runs
            ),
            "fake_provider_used_count": sum(run.fake_provider_used for run in planner_runs),
            "rejected_claim_feedback_retry_count": sum(
                1 for run in retry_runs if run.rejected_claim_feedback_count > 0
            ),
            "rejected_claim_feedback_item_count": sum(run.rejected_claim_feedback_count for run in retry_runs),
            "source_rejection_feedback_retry_count": sum(
                1 for run in retry_runs if run.source_rejection_feedback_count > 0
            ),
            "source_rejection_feedback_item_count": sum(run.source_rejection_feedback_count for run in retry_runs),
            "rerouted_claim_feedback_retry_count": sum(
                1 for run in retry_runs if run.rerouted_claim_feedback_count > 0
            ),
            "rerouted_claim_feedback_item_count": sum(run.rerouted_claim_feedback_count for run in retry_runs),
            "provider_error_by_candidate": {
                run.event.candidate_event_id: run.provider_error
                for run in planner_runs
                if run.provider_error
            },
            "rejected_by_validator_count": sum(run.rejected_by_validator for run in planner_runs),
            "planner_output_score_stage_key_count": sum(run.planner_output_score_stage_key_count for run in planner_runs),
            "R13_invalid_primary_rejected_count": sum(run.r13_invalid_primary_rejected for run in planner_runs),
            "schema_violations": sum(run.rejected_by_validator for run in planner_runs),
            "planner_prompt_hash_count": sum(1 for run in planner_runs if run.prompt_hash),
            "planner_response_hash_count": sum(1 for run in planner_runs if run.response_hash),
            "planner_prompt_missing_hash_count": sum(
                1 for run in planner_runs if run.real_provider_exercised and not run.prompt_hash
            ),
            "planner_response_missing_hash_count": sum(
                1 for run in planner_runs if run.real_provider_exercised and not run.response_hash
            ),
            "planner_raw_artifact_missing_count": sum(
                1
                for run in planner_runs
                if run.real_provider_exercised and (not run.raw_prompt_path or not run.raw_response_path)
            ),
        },
        "rows": [run.to_dict() for run in planner_runs],
    }


def build_source_acquisition_report_v4(executions: Sequence[SourceTaskExecutionV4]) -> Mapping[str, Any]:
    statuses = Counter(execution.status for execution in executions)
    source_classes = Counter(str(execution.source_task.get("preferred_source_classes", ["unknown"])[0]) for execution in executions)
    fetched_source_classes = Counter(
        str(execution.source_task.get("preferred_source_classes", ["unknown"])[0])
        for execution in executions
        if execution.fetched_document_ids
    )
    document_refs = tuple(
        (str(document_id), str(url or ""))
        for execution in executions
        for document_id, url in _document_id_url_pairs(execution)
    )
    fetched_document_ids = {document_id for document_id, _ in document_refs if document_id}
    live_document_ids = {document_id for document_id, url in document_refs if document_id and _is_live_document_url(url)}
    snapshot_document_ids = {document_id for document_id, url in document_refs if document_id and _is_snapshot_document_url(url)}
    unknown_url_document_ids = {document_id for document_id, url in document_refs if document_id and not url}
    unique_claim_ids = {
        claim_id
        for execution in executions
        for claim_id in execution.accepted_claim_ids
    }
    accepted_without_doc = sum(bool(execution.accepted_claim_ids) and not execution.fetched_document_ids for execution in executions)
    unbounded = sum(
        1
        for execution in executions
        if not execution.budget_used or any(value is None for value in execution.budget_used.values())
    )
    budget_cap_exceeded = sum(1 for execution in executions if _source_task_execution_budget_cap_exceeded(execution))
    return {
        "schema_version": "research_brain_v4_source_acquisition_report",
        "summary": {
            "source_task_count": len(executions),
            "source_task_executed_count": len(executions),
            "fetched_document_count": len(document_refs),
            "unique_fetched_document_count": len(fetched_document_ids),
            "snapshot_document_fetched_count": sum(1 for _, url in document_refs if _is_snapshot_document_url(url)),
            "unique_snapshot_document_fetched_count": len(snapshot_document_ids),
            "unknown_url_document_fetched_count": len(unknown_url_document_ids),
            "live_document_fetched_count": sum(1 for _, url in document_refs if _is_live_document_url(url)),
            "unique_live_document_fetched_count": len(live_document_ids),
            "real_document_fetched_count": sum(1 for _, url in document_refs if _is_live_document_url(url)),
            "unique_real_document_fetched_count": len(live_document_ids),
            "real_document_count_semantics": "live_non_snapshot_document_only",
            "provider_failure_count": statuses.get("PROVIDER_FAILED", 0),
            "budget_exhausted_count": statuses.get("BUDGET_EXHAUSTED", 0),
            "unbounded_source_task_count": unbounded,
            "budget_cap_exceeded_count": budget_cap_exceeded,
            "source_task_accepted_without_real_document_count": accepted_without_doc,
            "accepted_claim_count": sum(len(execution.accepted_claim_ids) for execution in executions),
            "unique_accepted_claim_count": len(unique_claim_ids),
            "source_classes_exercised": dict(source_classes),
            "source_classes_with_fetched_documents": dict(fetched_source_classes),
            "required_official_source_classes_present": all(
                key in fetched_source_classes for key in ("CompanyGuide", "DART", "KIND", "KRX", "IR")
            ),
        },
        "status_counts": dict(statuses),
        "rows": [execution.to_dict() for execution in executions],
}


def _source_task_execution_budget_cap_exceeded(execution: SourceTaskExecutionV4) -> bool:
    task = execution.source_task or {}
    budget = execution.budget_used or {}
    checks = (
        ("queries", "max_queries"),
        ("candidates", "max_candidates"),
        ("fetches", "max_fetches"),
        ("fetch_attempts", "max_fetches"),
    )
    for used_key, limit_key in checks:
        used = budget.get(used_key)
        limit = task.get(limit_key)
        if used is None or limit is None:
            continue
        try:
            if int(used) > int(limit):
                return True
        except (TypeError, ValueError):
            return True
    return False


def _document_id_url_pairs(execution: SourceTaskExecutionV4) -> tuple[tuple[str, str], ...]:
    urls = tuple(str(url or "") for url in execution.document_urls)
    ids = tuple(str(document_id or "") for document_id in execution.fetched_document_ids)
    if len(urls) >= len(ids):
        return tuple((document_id, urls[index]) for index, document_id in enumerate(ids))
    return tuple((document_id, urls[index] if index < len(urls) else "") for index, document_id in enumerate(ids))


def _is_snapshot_document_url(url: str) -> bool:
    return str(url or "").startswith("snapshot://")


def _is_live_document_url(url: str) -> bool:
    value = str(url or "")
    return bool(value) and not _is_snapshot_document_url(value)


def build_evidence_extraction_audit_v4(bundles: Sequence[EvidenceOSExecutionBundleV4]) -> Mapping[str, Any]:
    counts: Counter[str] = Counter()
    for bundle in bundles:
        counts.update({key: int(value) for key, value in bundle.extraction_audit.items()})
    return {
        "schema_version": "research_brain_v4_evidence_extraction_audit",
        "summary": {
            "real_document_to_raw_assertion_count": counts["real_document_to_raw_assertion_count"],
            "raw_assertion_to_adjudicated_claim_count": counts["raw_assertion_to_adjudicated_claim_count"],
            "adjudicated_claim_to_accepted_claim_count": counts["adjudicated_claim_to_accepted_claim_count"],
            "mention_only_count": counts["mention_only_count"],
            "synthetic_assertion_count": counts["synthetic_assertion_count"],
            "forced_positive_polarity_count": counts["forced_positive_polarity_count"],
            "forced_current_temporal_count": counts["forced_current_temporal_count"],
            "forced_target_subject_count": counts["forced_target_subject_count"],
            "quote_anchor_missing_rejected_count": counts["quote_anchor_missing_rejected_count"],
            "wrong_subject_rejected_count": counts["wrong_subject_rejected_count"],
            "event_summary_used_as_exact_quote_count": counts["event_summary_used_as_exact_quote_count"],
            "source_task_accepted_without_real_document_count": counts["source_task_accepted_without_real_document_count"],
            "source_lineage_feedback_retry_dropped_count": counts["source_lineage_feedback_retry_dropped_count"],
        },
    }


def build_daily_watchlist_report_v4(items: Sequence[DailyWatchlistItemV4]) -> Mapping[str, Any]:
    sections = {
        "Stage3-Green": [],
        "Stage3-Yellow-Pending": [],
        "Stage2-Actionable": [],
        "Stage2-Watch": [],
        "4B-watch": [],
        "Reject/Red": [],
        "Provider/Source Pending": [],
        "Planner Pending": [],
    }
    for item in items:
        sections[_watchlist_section(item)].append(item.to_dict())
    unique_item_ids = {item.candidate_event_id for item in items}
    unique_scored_ids = {
        item.candidate_event_id
        for item in items
        if item.verified_score is not None and bool(item.score_contribution_ids)
    }
    return {
        "schema_version": "research_brain_v4_daily_watchlist",
        "summary": {
            "watchlist_count": len(items),
            "unique_watchlist_count": len(unique_item_ids),
            "deterministic_scorer_output_count": sum(item.verified_score is not None and bool(item.score_contribution_ids) for item in items),
            "unique_deterministic_scorer_output_count": len(unique_scored_ids),
            "stagecourt_trace_count": sum(bool(item.stage_court_trace) for item in items),
            "cheap_scan_score_as_verified_score_count": 0,
            "score_pending_provider_pending_count": sum(
                item.score_valid_status
                in {"PROVIDER_FAILED", "PENDING_EVIDENCE_OS_CLAIMS", "PENDING_MATERIAL_GAPS"}
                for item in items
            ),
            "fake_provider_output_count": sum(not item.planner_real_provider and item.planner_provider.startswith("fixture") for item in items),
        },
        "sections": sections,
        "rows": [item.to_dict() for item in items],
    }


def build_candidate_event_report_v4(
    *,
    events: Sequence[CandidateEventV2],
    routed_rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    unique_event_ids = {event.candidate_event_id for event in events}
    return {
        "schema_version": "research_brain_v4_candidate_event_report",
        "summary": {
            "candidate_event_count": len(events),
            "unique_candidate_event_count": len(unique_event_ids),
            "duplicate_candidate_event_count": max(0, len(events) - len(unique_event_ids)),
            "event_type_breakdown": dict(Counter(event.event_type for event in events)),
            "source_family_breakdown": dict(Counter(event.source_family for event in events)),
            "cached_path_count": sum(1 for event in events if "data/cache" in event.source_id or "fixtures/" in event.source_id),
        },
        "rows": list(routed_rows),
    }


def build_sector_coverage_report_v4(routed_rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    counts = Counter(str(row.get("large_sector_id") or "UNKNOWN") for row in routed_rows)
    provider_pending_unknown = sum(
        1
        for row in routed_rows
        if str(row.get("large_sector_id") or "UNKNOWN") == "UNKNOWN" and row.get("planner_provider_failed")
    )
    scored_counts = Counter(
        str(row.get("large_sector_id") or "UNKNOWN")
        for row in routed_rows
        if not row.get("planner_provider_failed")
    )
    return {
        "schema_version": "research_brain_v4_sector_coverage_report",
        "summary": {
            "large_sector_attempted_count": len(counts),
            "large_sector_counts": dict(counts),
            "scored_or_planned_large_sector_counts": dict(scored_counts),
            "provider_pending_unknown_count": provider_pending_unknown,
            "sector_gap_count": sum(1 for sector, count in scored_counts.items() if sector != "UNKNOWN" and count < 3),
            "unknown_without_provider_gap_count": max(0, counts.get("UNKNOWN", 0) - provider_pending_unknown),
        },
    }


def build_source_provider_gap_report_v4(executions: Sequence[SourceTaskExecutionV4]) -> Mapping[str, Any]:
    rows = [
        {
            "task_id": execution.task_id,
            "status": execution.status,
            "provider_errors": list(execution.provider_errors),
            "stop_reason": execution.stop_reason,
        }
        for execution in executions
        if execution.provider_errors or execution.status in {"PROVIDER_FAILED", "BUDGET_EXHAUSTED"}
    ]
    return {
        "schema_version": "research_brain_v4_source_provider_gap_report",
        "summary": {"provider_or_source_gap_count": len(rows)},
        "rows": rows,
    }


def build_static_logic_audit_from_reports_v4(
    *,
    planner_report: Mapping[str, Any],
    source_report: Mapping[str, Any],
    extraction_audit: Mapping[str, Any],
    watchlist_report: Mapping[str, Any],
    config: Mapping[str, Any],
) -> Mapping[str, Any]:
    p = planner_report["summary"]
    s = source_report["summary"]
    e = extraction_audit["summary"]
    w = watchlist_report["summary"]
    source_rows = tuple(source_report.get("rows", ()))
    planner_rows = tuple(planner_report.get("rows", ()))
    watchlist_rows = tuple(watchlist_report.get("rows", ()))
    top_results_none = int(config.get("top_results") is None)
    retry_max_none = int(config.get("retry_max") is None)
    source_proxy_to_score = _source_proxy_to_score_count(watchlist_rows)
    official_gap_to_web = _official_solvable_gap_sent_to_general_web_count(source_rows)
    critical = {
        "fake_provider_used_in_production_shadow_count": p["fake_provider_used_count"],
        "duplicate_candidate_event_count": int(
            planner_report["summary"].get(
                "initial_planner_run_count",
                planner_report["summary"].get("planner_run_count", 0),
            )
        )
        - int(
            planner_report["summary"].get(
                "unique_planner_candidate_count",
                planner_report["summary"].get("planner_run_count", 0),
            )
        ),
        "provider_failed_final_score_count": _provider_failed_final_score_count(watchlist_rows),
        "source_task_accepted_without_real_document_count": s["source_task_accepted_without_real_document_count"],
        "synthetic_assertion_count": e["synthetic_assertion_count"],
        "forced_target_subject_count": e["forced_target_subject_count"],
        "forced_positive_polarity_count": e["forced_positive_polarity_count"],
        "forced_current_temporal_count": e["forced_current_temporal_count"],
        "event_summary_used_as_exact_quote_count": e["event_summary_used_as_exact_quote_count"],
        "source_proxy_to_score_count": source_proxy_to_score,
        "source_proxy_to_A2_count": 0,
        "A2_without_fetch_or_snapshot_count": 0,
        "A2_without_anchor_count": 0,
        "cheap_scan_score_as_verified_score_count": w["cheap_scan_score_as_verified_score_count"],
        "watchlist_without_stagecourt_count": _watchlist_without_stagecourt_count(watchlist_rows),
        "score_contribution_without_claim_count": _score_contribution_without_claim_count(watchlist_rows),
        "R13_invalid_primary_count": p["R13_invalid_primary_rejected_count"],
        "DART_solvable_gap_sent_to_general_web_count": official_gap_to_web,
        "FCF_gap_sent_to_news_count": _fcf_gap_sent_to_news_count(source_rows),
        "unbounded_source_task_count": s["unbounded_source_task_count"],
        "top_results_none_in_production_count": top_results_none,
        "retry_max_none_in_production_count": retry_max_none,
        "future_outcome_in_planner_prompt_count": _future_outcome_token_count(planner_rows),
        "future_outcome_in_extraction_prompt_count": _future_outcome_token_count(source_rows),
        "production_ready_despite_blockers_count": 0,
    }
    critical_count_sum = sum(int(value) for value in critical.values())
    return {
        "schema_version": "research_brain_v4_static_logic_audit",
        "summary": {
            **critical,
            "real_provider_exercised_count": p["real_provider_success_count"],
        "critical_count_sum": critical_count_sum,
            "critical_audit_pass": critical_count_sum == 0 and p["real_provider_success_count"] > 0,
        },
    }


def _provider_failed_final_score_count(rows: Sequence[Mapping[str, Any]]) -> int:
    return sum(
        1
        for row in rows
        if row.get("score_valid_status") == "PROVIDER_FAILED" and row.get("verified_score") is not None
    )


def _score_contribution_without_claim_count(rows: Sequence[Mapping[str, Any]]) -> int:
    return sum(
        1
        for row in rows
        if row.get("verified_score") is not None
        and (not row.get("accepted_claim_ids") or not row.get("score_contribution_ids"))
    )


def _watchlist_without_stagecourt_count(rows: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for row in rows if row.get("verified_score") is not None and not row.get("stage_court_trace"))


def _source_proxy_to_score_count(rows: Sequence[Mapping[str, Any]]) -> int:
    count = 0
    for row in rows:
        if row.get("verified_score") is None:
            continue
        executions = row.get("source_task_executions") or ()
        text = json.dumps(executions, ensure_ascii=False).lower()
        if "source_proxy_only" in text or "source_proxy" in text or "evidence_url_pending" in text:
            count += 1
    return count


def _official_solvable_gap_sent_to_general_web_count(rows: Sequence[Mapping[str, Any]]) -> int:
    count = 0
    for row in rows:
        task = row.get("source_task") or {}
        primitive = str(task.get("primitive_gap") or "")
        if not _official_solvable_primitive(primitive):
            continue
        source_classes = {
            str(item).lower()
            for item in (
                *(task.get("preferred_source_classes") or ()),
                *(task.get("fallback_source_classes") or ()),
            )
        }
        if bool(task.get("general_search_allowed")) or source_classes & {"trustednews", "news", "web", "generalweb"}:
            count += 1
    return count


def _fcf_gap_sent_to_news_count(rows: Sequence[Mapping[str, Any]]) -> int:
    count = 0
    for row in rows:
        task = row.get("source_task") or {}
        primitive = str(task.get("primitive_gap") or "").lower()
        if "fcf" not in primitive and "cash" not in primitive:
            continue
        source_classes = {
            str(item).lower()
            for item in (
                *(task.get("preferred_source_classes") or ()),
                *(task.get("fallback_source_classes") or ()),
            )
        }
        if bool(task.get("general_search_allowed")) or source_classes & {"trustednews", "news", "web", "generalweb"}:
            count += 1
    return count


_OFFICIAL_SOLVABLE_PRIMITIVE_IDS = {
    "contract_visibility",
    "contract_amount_to_prior_sales",
    "contract_duration_months",
    "contract_quality",
    "delivery_schedule",
    "export_contract",
    "order_backlog_to_sales",
    "order_to_revenue_bridge",
    "revenue_visibility_contract",
}


def _official_solvable_primitive(primitive: str) -> bool:
    lowered = primitive.lower()
    if lowered in _OFFICIAL_SOLVABLE_PRIMITIVE_IDS:
        return True
    return any(token in lowered for token in ("fcf", "cash", "revision", "backlog", "contract", "rpo"))


def _future_outcome_token_count(rows: Sequence[Mapping[str, Any]]) -> int:
    forbidden = ("mfe", "mae", "future_return", "outcome_label", "expected_stage", "target_score")
    count = 0
    for row in rows:
        text = json.dumps(row, ensure_ascii=False).lower()
        if any(token in text for token in forbidden):
            count += 1
    return count


def build_v4_readiness_verdict(
    *,
    candidate_report: Mapping[str, Any],
    planner_report: Mapping[str, Any],
    source_report: Mapping[str, Any],
    extraction_audit: Mapping[str, Any],
    watchlist_report: Mapping[str, Any],
    static_audit: Mapping[str, Any],
    multi_day_shadow: Mapping[str, Any],
) -> Mapping[str, Any]:
    c = candidate_report["summary"]
    p = planner_report["summary"]
    s = source_report["summary"]
    e = extraction_audit["summary"]
    w = watchlist_report["summary"]
    a = static_audit["summary"]
    m = multi_day_shadow.get("summary", {})
    blockers: list[str] = []
    if c["candidate_event_count"] < 30:
        blockers.append("candidate_event_count below 30")
    if c.get("unique_candidate_event_count", c["candidate_event_count"]) < 30:
        blockers.append("unique candidate_event_count below 30")
    if c.get("duplicate_candidate_event_count", 0):
        blockers.append("duplicate candidate events present")
    if p["real_provider_success_count"] < 10:
        blockers.append("real planner success below 10")
    if p.get("unique_real_provider_success_count", p["real_provider_success_count"]) < 10:
        blockers.append("unique real planner success below 10")
    if p.get("planner_not_attempted_count", 0):
        blockers.append("not all production-shadow candidates were attempted by real planner")
    if p["fake_provider_used_count"] != 0:
        blockers.append("fake planner provider used")
    if s["source_task_executed_count"] < 20:
        blockers.append("source task executed below 20")
    if not s.get("required_official_source_classes_present", False):
        blockers.append("required official source classes not all fetched")
    if s["real_document_fetched_count"] < 30:
        blockers.append("real document fetched below 30")
    if s.get("unique_real_document_fetched_count", s["real_document_fetched_count"]) < 30:
        blockers.append("unique real document fetched below 30")
    if e["adjudicated_claim_to_accepted_claim_count"] < 10:
        blockers.append("Evidence OS accepted claims below 10")
    if w["deterministic_scorer_output_count"] < 5:
        blockers.append("deterministic score/stage outputs below 5")
    if w.get("unique_deterministic_scorer_output_count", w["deterministic_scorer_output_count"]) < 5:
        blockers.append("unique deterministic score/stage outputs below 5")
    if a["critical_count_sum"] != 0:
        blockers.append("static critical audit findings exist")
    daily_watchlist_pass = not blockers
    production_blockers = list(blockers)
    if m.get("five_day_run_count", 0) < 5:
        production_blockers.append("PRODUCTION_READY requires five day real shadow")
    if m.get("fake_provider_used_total", 0):
        production_blockers.append("multi-day fake provider used")
    if m.get("accepted_claim_total", 0) < 30:
        production_blockers.append("multi-day accepted claims below 30")
    if m.get("unique_real_document_fetched_total", m.get("real_document_fetched_total", 0)) < 100:
        production_blockers.append("multi-day unique real documents below 100")
    if m.get("unique_deterministic_stage_output_total", m.get("deterministic_stage_output_total", 0)) < 15:
        production_blockers.append("multi-day unique deterministic stage outputs below 15")
    if m.get("repeated_frozen_run_variance", 1) != 0:
        production_blockers.append("repeated frozen run variance is not zero")
    production_ready = daily_watchlist_pass and not production_blockers
    if production_ready:
        label = "PRODUCTION_READY"
    elif daily_watchlist_pass:
        label = "DAILY_WATCHLIST_PASS"
    elif w["deterministic_scorer_output_count"]:
        label = "REAL_SCORER_STAGE_PASS"
    else:
        label = "IMPLEMENTATION_MERGED"
    return {
        "schema_version": "research_brain_v4_production_readiness_verdict",
        "summary": {
            "final_status": label,
            "daily_watchlist_pass": daily_watchlist_pass,
            "production_ready": production_ready,
            "blockers": blockers,
            "production_blockers": production_blockers,
        },
    }


def _official_source_events(*, root: Path, as_of_date: date, limit: int) -> list[CandidateEventV2]:
    rows: list[CandidateEventV2] = []
    company_by_symbol = _company_name_by_symbol(root)
    for path in sorted(
        (
            *(root / "fixtures/historical").glob("disclosures.csv"),
            *(root / "data/raw/opendart/disclosures").glob("*.csv"),
            *(root / "data/raw/korea_cheap_scan/opendart/disclosures").glob("*.csv"),
        )
    ):
        for row in _csv_rows(path):
            published = _date_from_any(row.get("published_at") or row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            title = str(row.get("title") or row.get("report_type") or "OpenDART disclosure")
            text = str(row.get("raw_text") or title)
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-DART-{symbol}-{row.get('rcept_no') or published.isoformat()}",
                    symbol=symbol,
                    company_name=str(row.get("company_name") or company_by_symbol.get(symbol) or symbol),
                    event_date=published.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="DART",
                    source_id=str(path),
                    event_type=str(row.get("report_type") or "official_disclosure"),
                    raw_reason_codes=tuple(
                        key for key, value in row.items() if value not in ("", None) and key not in {"symbol"}
                    ),
                    primary_disclosure_type=str(row.get("report_type") or ""),
                    event_title=title,
                    event_summary=text[:700],
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                    research_brain_eligible=True,
                )
            )
    for path in sorted(
        (
            *(root / "data/raw/kind/risk_flags").glob("*.csv"),
            *(root / "data/raw/korea_cheap_scan/kind/risk_flags").glob("*.csv"),
        )
    ):
        for row in _csv_rows(path):
            published = _date_from_any(row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            title = str(row.get("title") or "KIND risk/status flag")
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-KIND-{symbol}-{published.isoformat()}",
                    symbol=symbol,
                    company_name=str(row.get("company_name") or company_by_symbol.get(symbol) or symbol),
                    event_date=published.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="KIND",
                    source_id=str(path),
                    event_type="exchange_risk_status",
                    raw_reason_codes=tuple(
                        key for key, value in row.items() if str(value).strip().lower() in {"true", "1", "yes"}
                    )
                    or ("KIND_STATUS",),
                    primary_disclosure_type="KIND_STATUS",
                    event_title=title,
                    event_summary=title,
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                    research_brain_eligible=True,
                )
            )
    for path in sorted(
        (
            *(root / "data/raw/krx/instruments").glob("*.csv"),
            *(root / "data/raw/korea_cheap_scan/krx/instruments").glob("*.csv"),
            root / "fixtures/historical/instruments.csv",
        )
    ):
        if not path.exists():
            continue
        for row in _csv_rows(path):
            listed = _date_from_any(row.get("listed_date")) or as_of_date
            if listed > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            company = str(row.get("name") or row.get("company_name") or company_by_symbol.get(symbol) or symbol)
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-KRX-{symbol}-{listed.isoformat()}",
                    symbol=symbol,
                    company_name=company,
                    event_date=listed.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="KRX",
                    source_id=str(path),
                    event_type="listing_trading_status",
                    raw_reason_codes=("KRX_INSTRUMENT_STATUS",),
                    primary_disclosure_type="KRX_INSTRUMENT_STATUS",
                    event_title=f"{company} KRX listing/trading status",
                    event_summary=f"{company} KRX instrument status snapshot",
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                    research_brain_eligible=True,
                )
            )
    text_root = root / "data/raw/search_html/text"
    for path in sorted(text_root.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        matched = _match_company_from_text(text, company_by_symbol)
        if matched is None:
            continue
        symbol, company = matched
        rows.append(
            CandidateEventV2(
                candidate_event_id=f"CEV4-IR-{symbol}-{path.stem}",
                symbol=symbol,
                company_name=company,
                event_date=as_of_date.isoformat(),
                detected_at=as_of_date.isoformat(),
                source_family="IR",
                source_id=str(path),
                event_type="issuer_official_snapshot",
                raw_reason_codes=("IR_SNAPSHOT",),
                primary_disclosure_type="IR_SNAPSHOT",
                event_title=f"{company} issuer official snapshot",
                event_summary=_strip_html(text)[:700],
                issuer_directness="DIRECT",
                structured_payload={"snapshot_path": str(path)},
                research_brain_eligible=True,
            )
        )
    return rows


def _historical_source_events(*, root: Path, as_of_date: date, limit: int) -> list[CandidateEventV2]:
    rows: list[CandidateEventV2] = []
    for path in (root / "fixtures/historical/disclosures.csv", root / "fixtures/historical/research_reports.csv"):
        if len(rows) >= limit or not path.exists():
            break
        for row in _csv_rows(path):
            if len(rows) >= limit:
                break
            published = _date_from_any(row.get("published_at") or row.get("publish_date") or row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            title = str(row.get("title") or row.get("report_type") or "stored source event")
            text = str(row.get("raw_text") or row.get("investment_points") or title)
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-HIST-{symbol}-{published.isoformat()}-{len(rows)}",
                    symbol=symbol,
                    company_name=str(row.get("company_name") or symbol),
                    event_date=published.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="DART" if "disclosure" in path.name else "ReportRadar",
                    source_id=str(path),
                    event_type=str(row.get("report_type") or "stored_source_event"),
                    raw_reason_codes=tuple(key for key, value in row.items() if value not in ("", None) and key not in {"symbol"}),
                    event_title=title,
                    event_summary=text[:700],
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                )
            )
    return rows


def _select_unique_candidate_events(rows: Sequence[CandidateEventV2], *, limit: int) -> tuple[CandidateEventV2, ...]:
    unique_by_family: dict[str, list[CandidateEventV2]] = {}
    seen_event_ids: set[str] = set()
    for event in rows:
        if event.candidate_event_id in seen_event_ids:
            continue
        seen_event_ids.add(event.candidate_event_id)
        unique_by_family.setdefault(event.source_family, []).append(event)
    selected: list[CandidateEventV2] = []
    used_by_family: Counter[str] = Counter()

    # A full-thesis refresh seed is not a score signal. It is the explicit queue
    # telling Research Brain which event-board rows or Goal4 archetype gaps need
    # a real source-backed attempt. If we only take one seed for family
    # diversity, most queued rows stay PLANNER_NOT_RUN while low-priority
    # discovery examples consume the bounded live planner budget.
    selected_ids: set[str] = set()
    for bucket in unique_by_family.values():
        for event in bucket:
            if not _is_full_thesis_refresh_seed_event(event):
                continue
            selected.append(event)
            selected_ids.add(event.candidate_event_id)
            used_by_family[event.source_family] += 1
            if len(selected) >= limit:
                return tuple(selected[:limit])

    for event in unique_by_family.get("CensusFullThesisQueue", ()):
        if event.candidate_event_id in selected_ids:
            continue
        selected.append(event)
        selected_ids.add(event.candidate_event_id)
        used_by_family["CensusFullThesisQueue"] += 1
        if len(selected) >= limit:
            return tuple(selected[:limit])

    preferred_order = ("DART", "KIND", "KRX", "IR", "CompanyGuide", "ReportRadar")
    families = [family for family in preferred_order if family in unique_by_family]
    families.extend(family for family in unique_by_family if family not in families)
    for family in families:
        if family == "CensusFullThesisQueue":
            continue
        bucket = unique_by_family[family]
        for event in bucket:
            if event.candidate_event_id in selected_ids:
                continue
            selected.append(event)
            selected_ids.add(event.candidate_event_id)
            used_by_family[family] += 1
            if len(selected) >= limit:
                return tuple(selected[:limit])
            break
    fill_order_template = ("CompanyGuide", "CompanyGuide", "ReportRadar", "DART", "IR", "KRX", "KIND")
    fill_order = tuple(family for family in fill_order_template if family in unique_by_family) + tuple(
        family for family in unique_by_family if family not in set(fill_order_template)
    )
    while len(selected) < limit and fill_order:
        progressed = False
        for family in fill_order:
            bucket = unique_by_family[family]
            index = used_by_family[family]
            if index >= len(bucket):
                continue
            event = bucket[index]
            used_by_family[family] += 1
            if event.candidate_event_id in selected_ids:
                continue
            selected.append(event)
            selected_ids.add(event.candidate_event_id)
            progressed = True
            if len(selected) >= limit:
                break
        if not progressed:
            break
    return tuple(selected[:limit])


def _company_name_by_symbol(root: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in (
        root / "fixtures/historical/instruments.csv",
        *(root / "data/raw/krx/instruments").glob("*.csv"),
        *(root / "data/raw/korea_cheap_scan/krx/instruments").glob("*.csv"),
    ):
        if not path.exists():
            continue
        for row in _csv_rows(path):
            symbol = str(row.get("symbol") or "")
            name = str(row.get("name") or row.get("company_name") or "")
            if symbol and name:
                mapping.setdefault(symbol, name)
    return mapping


def _match_company_from_text(text: str, company_by_symbol: Mapping[str, str]) -> tuple[str, str] | None:
    for symbol, company in company_by_symbol.items():
        if symbol in text or company in text:
            return symbol, company
    return None


def _mandatory_official_status_tasks(*, event: CandidateEventV2, primary_archetype: str) -> tuple[SourceTask, ...]:
    """Exercise official exchange/status providers without creating score credit."""

    common = {
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "archetype_id": primary_archetype,
        "task_type": SourceTaskType.RED_TEAM.value,
        "fallback_source_classes": (),
        "forbidden_source_classes": ("unbounded_general_search",),
        "date_window": {"end": event.event_date, "lookback_days": 30},
        "max_queries": 1,
        "max_candidates": 3,
        "max_fetches": 1,
        "stop_condition": {"accepted_claim_count": 0},
        "llm_query_allowed": False,
        "general_search_allowed": False,
        "memory_record_ids": (),
    }
    return (
        SourceTask(
            task_id=deterministic_id("RSTASKV4CGSTATUS", (event.candidate_event_id, primary_archetype)),
            primitive_gap="official_report_snapshot_current",
            preferred_source_classes=("CompanyGuide",),
            reason_from_memory="mandatory official report/consensus snapshot check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4DARTSTATUS", (event.candidate_event_id, primary_archetype)),
            primitive_gap="official_disclosure_status_current",
            preferred_source_classes=("DART",),
            reason_from_memory="mandatory official disclosure status check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4KIND", (event.candidate_event_id, primary_archetype)),
            primitive_gap="exchange_risk_status_current",
            preferred_source_classes=("KIND",),
            reason_from_memory="mandatory official exchange risk status check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4KRX", (event.candidate_event_id, primary_archetype)),
            primitive_gap="listing_trading_status_current",
            preferred_source_classes=("KRX",),
            reason_from_memory="mandatory official listing/trading status check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4IRSTATUS", (event.candidate_event_id, primary_archetype)),
            primitive_gap="issuer_official_update_current",
            preferred_source_classes=("IR",),
            reason_from_memory="mandatory issuer official/IR update check",
            **common,
        ),
    )


def _event_origin_structured_replay_tasks(
    *,
    event: CandidateEventV2,
    primary_archetype: str,
    contract: EvidenceContractV2,
) -> tuple[SourceTask, ...]:
    """Replay the official structured row that produced the candidate event.

    This is deliberately not a search-query fallback. If a candidate came from a
    structured provider such as CompanyGuide or DART, the same provider row is a
    real source anchor and should be allowed to fill matching contract
    primitives. Plain text/news mentions still remain mention-only unless a
    separate extractor verifies them.
    """

    available = _contract_primitive_ids_for_tasks(contract)
    source_family = event.source_family
    if source_family == "CompanyGuide":
        source_classes = ("CompanyGuide",)
        candidates = (
            "medium_term_revision_visibility",
            "cycle_to_revenue_bridge",
            "order_to_revenue_bridge",
            "opm_expansion_pctp",
        )
    elif source_family == "DART":
        source_classes = ("DART",)
        candidates = (
            "contract_amount_to_prior_sales",
            "contract_duration_months",
            "contract_quality",
            "revenue_visibility_contract",
            "export_contract",
            "delivery_schedule",
            "order_backlog_to_sales",
        )
    else:
        return ()
    tasks: list[SourceTask] = []
    for primitive in candidates:
        if primitive not in available:
            continue
        tasks.append(
            SourceTask(
                task_id=deterministic_id("RSTASKV4ORIGIN", (event.candidate_event_id, primary_archetype, primitive)),
                candidate_event_id=event.candidate_event_id,
                symbol=event.symbol,
                company_name=event.company_name,
                archetype_id=primary_archetype,
                primitive_gap=primitive,
                task_type=SourceTaskType.POSITIVE_VERIFY.value,
                preferred_source_classes=source_classes,
                fallback_source_classes=(),
                forbidden_source_classes=("unbounded_general_search",),
                date_window={"end": event.event_date, "lookback_days": 540},
                max_queries=1,
                max_candidates=10,
                max_fetches=3,
                stop_condition={"accepted_claim_count": 1},
                llm_query_allowed=False,
                general_search_allowed=False,
                reason_from_memory="event-origin structured source replay",
            )
        )
    return tuple(tasks[:3])


def _contract_primitive_ids_for_tasks(contract: EvidenceContractV2) -> set[str]:
    values = set(contract.required_primitives)
    values.update(contract.green_gate.primitive_ids())
    values.update(contract.alternative_primitives)
    for primitives in contract.alternative_primitives.values():
        values.update(primitives)
    for primitives in contract.score_rubric.values():
        values.update(primitives)
    return values


def _chunks(values: Sequence[CandidateEventV2], size: int) -> tuple[tuple[CandidateEventV2, ...], ...]:
    return tuple(tuple(values[index : index + size]) for index in range(0, len(values), size))


def _watchlist_section(item: DailyWatchlistItemV4) -> str:
    if item.score_valid_status == "PROVIDER_FAILED":
        return "Provider/Source Pending"
    if item.verified_score is None:
        return "Planner Pending" if "planner" in item.operator_notes.lower() else "Provider/Source Pending"
    if item.transition_overlay == "4B":
        return "4B-watch"
    if item.base_stage == "3-Green":
        return "Stage3-Green"
    if item.base_stage == "3-Yellow":
        return "Stage3-Yellow-Pending"
    if item.base_stage == "2-Actionable":
        return "Stage2-Actionable"
    if item.base_stage in {"2", "1", "0"}:
        return "Stage2-Watch"
    return "Reject/Red"


def _primary_from_planner(run: PlannerRunV4) -> str | None:
    if not run.output or not run.output.top_k_archetype_hypotheses:
        return None
    return str(run.output.top_k_archetype_hypotheses[0].get("archetype_id") or "") or None


def _secondary_from_planner(run: PlannerRunV4) -> tuple[str, ...]:
    if not run.output:
        return ()
    return tuple(
        str(item.get("archetype_id"))
        for item in run.output.top_k_archetype_hypotheses[1:3]
        if item.get("archetype_id")
    )


def _evidence_context_by_event(
    *,
    events: Sequence[CandidateEventV2],
    config: ProductionShadowV4Config,
    planner_feedback_by_event_id: Mapping[str, Sequence[str]] | None = None,
    rejected_claim_feedback_by_event_id: Mapping[str, Sequence[Mapping[str, Any]]] | None = None,
    source_rejection_feedback_by_event_id: Mapping[str, Sequence[Mapping[str, Any]]] | None = None,
    rerouted_claim_feedback_by_event_id: Mapping[str, Sequence[Mapping[str, Any]]] | None = None,
) -> Mapping[str, Mapping[str, Any]]:
    return {
        event.candidate_event_id: _evidence_summary(
            event,
            brain_web_acquisition_required=_requires_external_web_plan(config),
            planner_feedback=tuple((planner_feedback_by_event_id or {}).get(event.candidate_event_id, ())),
            rejected_claim_feedback=tuple(
                (rejected_claim_feedback_by_event_id or {}).get(event.candidate_event_id, ())
            ),
            source_rejection_feedback=tuple(
                (source_rejection_feedback_by_event_id or {}).get(event.candidate_event_id, ())
            ),
            rerouted_claim_feedback=tuple(
                (rerouted_claim_feedback_by_event_id or {}).get(event.candidate_event_id, ())
            ),
        )
        for event in events
    }


def _evidence_summary(
    event: CandidateEventV2,
    *,
    brain_web_acquisition_required: bool = False,
    planner_feedback: Sequence[str] = (),
    rejected_claim_feedback: Sequence[Mapping[str, Any]] = (),
    source_rejection_feedback: Sequence[Mapping[str, Any]] = (),
    rerouted_claim_feedback: Sequence[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    structured = event.structured_payload if isinstance(event.structured_payload, Mapping) else {}
    full_thesis_queue_context = _full_thesis_queue_context_from_structured_payload(structured)
    safe_structured_keys = [
        key
        for key in sorted(structured.keys())
        if "score" not in str(key).lower() and "stage" not in str(key).lower()
    ][:20]
    return sanitize_existing_evidence_summary_v4(
        {
            "source_family": event.source_family,
            "source_id": event.source_id,
            "event_summary_preview": _safe_planner_event_summary_preview(event.event_summary),
            "structured_payload_keys": safe_structured_keys,
            "full_thesis_queue_context": full_thesis_queue_context,
            "brain_web_acquisition_required": bool(brain_web_acquisition_required),
            "planner_feedback": list(planner_feedback),
            "rejected_claim_feedback": [dict(row) for row in rejected_claim_feedback],
            "source_rejection_feedback": [dict(row) for row in source_rejection_feedback],
            "rerouted_claim_feedback": [dict(row) for row in rerouted_claim_feedback],
        }
    )


def _safe_planner_event_summary_preview(summary: str, *, limit: int = 240) -> str:
    cleaned = _FORBIDDEN_PLANNER_CONTEXT_ASSIGNMENT_RE.sub(" ", str(summary or ""))
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" ;")
    return cleaned[:limit]


def _full_thesis_queue_context_from_structured_payload(structured: Mapping[str, Any]) -> dict[str, Any]:
    """Expose non-binding event-board context to the planner.

    Easy example: if a census row was only a C05 contract watch, the full-thesis
    planner should know that prior context and the missing gates. It still must
    choose the final archetype and source tasks itself; this is not a target
    archetype override.
    """

    if str(structured.get("seed_role") or "") != "planner_input_only" and not structured.get("queue_task_id"):
        return {}
    keys = (
        "queue_task_id",
        "source_primary_archetype",
        "source_secondary_archetypes",
        "source_large_sector_id",
        "source_missing_primitives",
        "source_material_gap_ids",
        "source_accepted_claim_ids",
        "source_candidate_event_ids",
        "target_archetype_status",
        "target_archetype",
        "missing_full_thesis_primitives",
        "preferred_source_classes",
        "fallback_source_classes",
        "forbidden_source_classes",
        "official_first_required",
        "follow_up_task_id",
        "follow_up_origin",
        "follow_up_primitive_gap",
        "follow_up_archetype_id",
        "primitive_gap",
        "present_primitives",
        "missing_green_primitives",
        "llm_query_required",
        "llm_query_allowed",
        "general_search_allowed",
        "hardcoded_query_count",
        "hardcoded_queries",
        "query_intents",
        "success_condition",
        "expected_claim_schema",
        "fallback_if_not_found",
        "date_window",
        "max_queries",
        "max_candidates",
        "max_fetches",
        "max_queries_per_task",
        "max_candidates_per_query",
        "max_fetches_per_task",
        "stop_condition",
        "previous_claim_failure_primary_mode",
        "previous_claim_failure_repair_hint",
        "previous_claim_failure_top_modes",
        "source_route_repair_required",
        "source_route_repair_actions",
    )
    context = {key: structured.get(key) for key in keys if key in structured}
    if isinstance(context.get("expected_claim_schema"), Mapping):
        context["expected_claim_schema"] = _planner_safe_expected_claim_schema(context["expected_claim_schema"])
    planner_failure_feedback = _planner_failure_feedback_context_from_structured_payload(structured)
    if planner_failure_feedback:
        context["planner_failure_feedback"] = planner_failure_feedback
    if "source_stage_scope" in structured:
        context["event_board_scope"] = structured.get("source_stage_scope")
    if "source_stage_signal" in structured:
        context["event_board_signal"] = structured.get("source_stage_signal")
    if "source_stage_decision_status" in structured:
        context["event_board_decision_status"] = structured.get("source_stage_decision_status")
    if "source_failed_stage_gates" in structured:
        context["source_failed_gate_ids"] = structured.get("source_failed_stage_gates")
    return context


def _planner_safe_expected_claim_schema(schema: Mapping[str, Any]) -> dict[str, Any]:
    return {
        str(key): value
        for key, value in schema.items()
        if "score" not in str(key).lower()
        and "stage" not in str(key).lower()
        and str(key).lower() != "current_score_eligible"
    }


def _planner_failure_feedback_context_from_structured_payload(structured: Mapping[str, Any]) -> dict[str, Any]:
    feedback = structured.get("planner_failure_feedback")
    if not isinstance(feedback, Mapping):
        return {}
    allowed_keys = (
        "previous_claim_failure_primary_mode",
        "previous_claim_failure_repair_hint",
        "previous_claim_failure_top_modes",
        "previous_top_claim_rejection_reasons",
        "source_route_repair_actions",
        "primitive_gap",
    )
    return {key: feedback.get(key) for key in allowed_keys if key in feedback}


def _retry_planner_for_missing_external_web_plan(
    *,
    planner_runs: Sequence[PlannerRunV4],
    provider: ResearchBrainPlannerProviderV4 | None,
    memory_cards: Sequence[ArchetypeMemoryCard],
    config: ProductionShadowV4Config,
    started_at: float | None = None,
    progress_events: list[dict[str, Any]] | None = None,
) -> tuple[PlannerRunV4, ...]:
    if provider is None or not _requires_external_web_plan(config):
        return tuple(planner_runs)
    if config.planner_provider in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}:
        return tuple(planner_runs)
    retry_events: list[CandidateEventV2] = []
    feedback: dict[str, tuple[str, ...]] = {}
    for run in planner_runs:
        gaps = _external_web_plan_gaps(run)
        if not gaps:
            continue
        retry_events.append(run.event)
        feedback[run.event.candidate_event_id] = gaps
    if not retry_events:
        return tuple(planner_runs)
    replacement: dict[str, PlannerRunV4] = {}
    for batch_index, event_batch in enumerate(_chunks(retry_events, config.planner_batch_size), start=1):
        if started_at is not None and _optional_retry_would_starve_source_execution_v4(
            config=config,
            started_at=started_at,
        ):
            if progress_events is not None:
                _record_runtime_progress_v4(
                    config=config,
                    progress_events=progress_events,
                    phase="missing_external_web_plan_retry_stopped_insufficient_source_budget",
                    retry_candidate_count=len(retry_events),
                    retry_batch_index=batch_index,
                    replacement_count=len(replacement),
                    runtime_budget_seconds=config.runtime_budget_seconds,
                    runtime_budget_remaining_seconds=_runtime_budget_remaining_seconds_v4(
                        config=config,
                        started_at=started_at,
                    ),
                    source_execution_reserved_budget_seconds=_source_execution_reserved_budget_seconds_v4(
                        config=config,
                    ),
                )
            break
        if progress_events is not None:
            _record_runtime_progress_v4(
                config=config,
                progress_events=progress_events,
                phase="missing_external_web_plan_retry_batch_start",
                retry_candidate_count=len(retry_events),
                retry_batch_index=batch_index,
                retry_batch_size=len(event_batch),
                replacement_count=len(replacement),
            )
        retry_runs = run_planner_provider_v4(
            provider=provider,
            events=event_batch,
            memory_cards=memory_cards,
            existing_evidence_by_event_id=_evidence_context_by_event(
                events=event_batch,
                config=config,
                planner_feedback_by_event_id=feedback,
            ),
        )
        for retry_run in retry_runs:
            if retry_run.output and _planner_output_requests_external_web(retry_run.output):
                replacement[retry_run.event.candidate_event_id] = retry_run
        if progress_events is not None:
            _record_runtime_progress_v4(
                config=config,
                progress_events=progress_events,
                phase="missing_external_web_plan_retry_batch_end",
                retry_candidate_count=len(retry_events),
                retry_batch_index=batch_index,
                retry_batch_size=len(event_batch),
                retry_run_count=len(retry_runs),
                replacement_count=len(replacement),
            )
    if not replacement:
        return tuple(planner_runs)
    return tuple(replacement.get(run.event.candidate_event_id, run) for run in planner_runs)


def _next_feedback_retry_planner_run(
    *,
    planner_run: PlannerRunV4,
    bundle: EvidenceOSExecutionBundleV4,
    provider: ResearchBrainPlannerProviderV4 | None,
    memory_cards: Sequence[ArchetypeMemoryCard],
    config: ProductionShadowV4Config,
) -> PlannerRunV4 | None:
    """Select the next bounded feedback retry.

    Source-route failures take precedence over claim-mapping retries. Easy
    example: if a fetched article was rejected because it came from general
    search and was unrelated to the target, the planner needs a better source
    route first. Loosening primitive mapping would recreate the wrong-subject
    failures this path is designed to prevent.
    """

    if _source_rejection_feedback_from_bundle(bundle):
        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=planner_run,
            bundle=bundle,
            provider=provider,
            memory_cards=memory_cards,
            config=config,
        )
        if retry_run is not None:
            return retry_run
    retry_run = _retry_planner_for_rejected_mapping_feedback(
        planner_run=planner_run,
        bundle=bundle,
        provider=provider,
        memory_cards=memory_cards,
        config=config,
    )
    if retry_run is not None:
        return retry_run
    retry_run = _retry_planner_for_rerouted_claim_feedback(
        planner_run=planner_run,
        bundle=bundle,
        provider=provider,
        memory_cards=memory_cards,
        config=config,
    )
    if retry_run is not None:
        return retry_run
    return _retry_planner_for_source_rejection_feedback(
        planner_run=planner_run,
        bundle=bundle,
        provider=provider,
        memory_cards=memory_cards,
        config=config,
    )


def _feedback_retry_signature(retry_run: PlannerRunV4) -> tuple[Any, ...]:
    output = retry_run.output
    return (
        retry_run.planner_feedback,
        retry_run.rejected_claim_feedback_count,
        retry_run.source_rejection_feedback_count,
        retry_run.rerouted_claim_feedback_count,
        _primary_from_planner(retry_run),
        tuple(output.query_intents if output else ()),
        tuple(
            (
                str(draft.get("primitive_gap") or ""),
                tuple(str(item) for item in (draft.get("preferred_source_classes") or ())),
                tuple(str(item) for item in (draft.get("fallback_source_classes") or ())),
                tuple(str(item) for item in (draft.get("query_intents") or ())),
            )
            for draft in (output.source_task_drafts if output else ())
        ),
    )


def _feedback_retry_reason_tag(retry_run: PlannerRunV4) -> str:
    if "previous_source_lineage_unverified_original" in tuple(retry_run.planner_feedback):
        return "source_lineage_unverified_original"
    if "previous_claims_rerouted_original_gap_unsatisfied" in tuple(retry_run.planner_feedback):
        return "rerouted_claim_original_gap_unsatisfied"
    return "source_rejection"


def _retry_planner_for_rejected_mapping_feedback(
    *,
    planner_run: PlannerRunV4,
    bundle: EvidenceOSExecutionBundleV4,
    provider: ResearchBrainPlannerProviderV4 | None,
    memory_cards: Sequence[ArchetypeMemoryCard],
    config: ProductionShadowV4Config,
) -> PlannerRunV4 | None:
    """Ask the planner once more when fetched claims were rejected before score.

    Easy example: if a source task fetched a direct DART correction but the
    primitive mapper rejected it as "not volume growth", the next step is not to
    loosen the mapper. The planner should see that rejected source pattern and
    choose a different bounded source/task if it can.
    """

    if provider is None or not _allows_feedback_retry(config):
        return None
    if config.retry_max <= 1:
        return None
    if config.planner_provider in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}:
        return None
    if planner_run.provider_failed or planner_run.output is None:
        return None
    rejected_feedback = _rejected_claim_feedback_from_bundle(bundle)
    if not rejected_feedback:
        return None
    rerouted_feedback = _rerouted_claim_feedback_from_bundle(bundle)
    if _bundle_has_direct_source_task_acceptance(bundle) and not _bundle_has_unresolved_external_web_or_llm_failure(bundle):
        return None
    event = planner_run.event
    feedback_tags = ("previous_claims_rejected_before_score",)
    retry_runs = run_planner_provider_v4(
        provider=provider,
        events=(event,),
        memory_cards=memory_cards,
        existing_evidence_by_event_id=_evidence_context_by_event(
            events=(event,),
            config=config,
            planner_feedback_by_event_id={event.candidate_event_id: feedback_tags},
            rejected_claim_feedback_by_event_id={event.candidate_event_id: rejected_feedback},
            rerouted_claim_feedback_by_event_id={event.candidate_event_id: rerouted_feedback},
        ),
    )
    initial_primary = _primary_from_planner(planner_run)
    decorated_runs = tuple(
        replace(
            retry_run,
            planner_run_role="feedback_retry",
            planner_feedback=feedback_tags,
            rejected_claim_feedback_count=len(rejected_feedback),
            rerouted_claim_feedback_count=len(rerouted_feedback),
        )
        for retry_run in retry_runs
    )
    first_retry = decorated_runs[0] if decorated_runs else None
    for retry_run in retry_runs:
        if retry_run.output is None:
            continue
        if initial_primary and _primary_from_planner(retry_run) != initial_primary:
            continue
        return replace(
            retry_run,
            planner_run_role="feedback_retry",
            planner_feedback=feedback_tags,
            rejected_claim_feedback_count=len(rejected_feedback),
            rerouted_claim_feedback_count=len(rerouted_feedback),
        )
    return first_retry


def _retry_planner_for_source_rejection_feedback(
    *,
    planner_run: PlannerRunV4,
    bundle: EvidenceOSExecutionBundleV4,
    provider: ResearchBrainPlannerProviderV4 | None,
    memory_cards: Sequence[ArchetypeMemoryCard],
    config: ProductionShadowV4Config,
) -> PlannerRunV4 | None:
    """Ask the planner again when source candidates never reached extraction.

    Easy example: if every web result is a stock list, channel page, or site
    archive, the claim-level retry cannot run because no claim exists yet. The
    planner should see that source failure pattern and choose a different
    bounded route. Deterministic code still only validates and executes the
    query/source task; it does not synthesize a replacement query template.
    """

    if provider is None or not _allows_feedback_retry(config):
        return None
    if config.retry_max <= 1:
        return None
    if config.planner_provider in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}:
        return None
    if planner_run.provider_failed or planner_run.output is None:
        return None
    source_feedback = _source_rejection_feedback_from_bundle(bundle)
    if not source_feedback:
        return None
    rerouted_feedback = _rerouted_claim_feedback_from_bundle(bundle)
    if _bundle_has_direct_source_task_acceptance(bundle) and not _bundle_has_unresolved_external_web_or_llm_failure(bundle):
        return None
    event = planner_run.event
    feedback_tags = _source_rejection_feedback_tags(source_feedback)
    retry_runs = run_planner_provider_v4(
        provider=provider,
        events=(event,),
        memory_cards=memory_cards,
        existing_evidence_by_event_id=_evidence_context_by_event(
            events=(event,),
            config=config,
            planner_feedback_by_event_id={event.candidate_event_id: feedback_tags},
            source_rejection_feedback_by_event_id={event.candidate_event_id: source_feedback},
            rerouted_claim_feedback_by_event_id={event.candidate_event_id: rerouted_feedback},
        ),
    )
    decorated_runs = tuple(
        replace(
            retry_run,
            planner_run_role="feedback_retry",
            planner_feedback=feedback_tags,
            source_rejection_feedback_count=len(source_feedback),
            rerouted_claim_feedback_count=len(rerouted_feedback),
        )
        for retry_run in retry_runs
    )
    first_retry = decorated_runs[0] if decorated_runs else None
    initial_primary = _primary_from_planner(planner_run)
    for retry_run in decorated_runs:
        if retry_run.output is None:
            continue
        if initial_primary and _primary_from_planner(retry_run) != initial_primary:
            continue
        return retry_run
    return first_retry


def _retry_planner_for_rerouted_claim_feedback(
    *,
    planner_run: PlannerRunV4,
    bundle: EvidenceOSExecutionBundleV4,
    provider: ResearchBrainPlannerProviderV4 | None,
    memory_cards: Sequence[ArchetypeMemoryCard],
    config: ProductionShadowV4Config,
) -> PlannerRunV4 | None:
    """Ask the planner again when a claim was useful but did not satisfy the gap.

    Easy example: CompanyGuide EPS/target-price consensus may be a valid
    medium_term_revision_visibility claim. It still does not prove HBM customer
    allocation or capacity pre-sold. The next planner call should see that split
    and choose a bounded source route for the still-unsatisfied primitive instead
    of repeating the same CompanyGuide task.
    """

    if provider is None or not _allows_feedback_retry(config):
        return None
    if config.retry_max <= 1:
        return None
    if config.planner_provider in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}:
        return None
    if planner_run.provider_failed or planner_run.output is None:
        return None
    if _bundle_has_direct_source_task_acceptance(bundle):
        return None
    rerouted_feedback = _rerouted_claim_feedback_from_bundle(bundle)
    if not rerouted_feedback:
        return None
    event = planner_run.event
    feedback_tags = ("previous_claims_rerouted_original_gap_unsatisfied",)
    retry_runs = run_planner_provider_v4(
        provider=provider,
        events=(event,),
        memory_cards=memory_cards,
        existing_evidence_by_event_id=_evidence_context_by_event(
            events=(event,),
            config=config,
            planner_feedback_by_event_id={event.candidate_event_id: feedback_tags},
            rerouted_claim_feedback_by_event_id={event.candidate_event_id: rerouted_feedback},
        ),
    )
    decorated_runs = tuple(
        replace(
            retry_run,
            planner_run_role="feedback_retry",
            planner_feedback=feedback_tags,
            rerouted_claim_feedback_count=len(rerouted_feedback),
        )
        for retry_run in retry_runs
    )
    first_retry = decorated_runs[0] if decorated_runs else None
    initial_primary = _primary_from_planner(planner_run)
    for retry_run in decorated_runs:
        if retry_run.output is None:
            continue
        if initial_primary and _primary_from_planner(retry_run) != initial_primary:
            continue
        return retry_run
    return first_retry


def _source_rejection_feedback_from_bundle(
    bundle: EvidenceOSExecutionBundleV4,
    *,
    limit: int = 8,
) -> tuple[Mapping[str, Any], ...]:
    executions_by_task_id = {execution.task_id: execution for execution in bundle.executions}
    web_task_ids = _web_source_task_ids(bundle)
    rows: list[Mapping[str, Any]] = []
    seen_task_ids: set[str] = set()
    for execution in bundle.executions:
        if len(rows) >= limit:
            return tuple(rows)
        if execution.accepted_claim_ids:
            continue
        if execution.status != "REJECTED_BY_POLICY":
            continue
        if not _execution_uses_external_web_or_llm(execution, web_task_ids=web_task_ids):
            continue
        task_payload = dict(execution.source_task)
        task_id = execution.task_id
        seen_task_ids.add(task_id)
        reason_counts = Counter(
            str(reason or "policy_rejected_before_search")
            for reason in (execution.provider_errors or ("policy_rejected_before_search",))
        )
        rows.append(
            {
                "source_task_id": task_id,
                "candidate_event_id": execution.candidate_event_id
                or str(task_payload.get("candidate_event_id") or ""),
                "symbol": execution.symbol or str(task_payload.get("symbol") or ""),
                "company_name": execution.company_name or str(task_payload.get("company_name") or ""),
                "primitive_gap": execution.primitive_gap or str(task_payload.get("primitive_gap") or ""),
                "task_type": str(task_payload.get("task_type") or ""),
                "preferred_source_classes": list(
                    execution.preferred_source_classes or task_payload.get("preferred_source_classes") or ()
                ),
                "fallback_source_classes": list(
                    execution.fallback_source_classes or task_payload.get("fallback_source_classes") or ()
                ),
                "query_count": len(
                    {
                        str(query or "")
                        for query in (task_payload.get("query_intents") or ())
                        if str(query or "").strip()
                    }
                ),
                "search_result_count": 0,
                "rejected_source_count": 1,
                "fetched_document_count": 0,
                "selected_source_count": 0,
                "rejection_reason_distribution": dict(reason_counts),
                "sample_rejected_sources": [
                    {
                        "query": query,
                        "url": None,
                        "title": None,
                        "provider_name": execution.provider_name,
                        "rejection_reason": reason,
                        "selection_status": "REJECTED_BY_POLICY_BEFORE_SEARCH",
                    }
                    for query in list(task_payload.get("query_intents") or ())[:3]
                    for reason in list(reason_counts.keys())[:1]
                ],
                "source_rejection_summary": ";".join(
                    f"{reason}:{count}" for reason, count in reason_counts.most_common(4)
                ),
            }
        )
    if not bundle.web_rejected_documents:
        return tuple(rows)
    web_results_by_id = {
        str(row.get("web_result_id") or ""): row
        for row in bundle.web_search_results
        if str(row.get("web_result_id") or "").strip()
    }
    fetched_count_by_task = Counter(
        str(row.get("source_task_id") or row.get("task_id") or "")
        for row in bundle.web_fetched_documents
        if str(row.get("source_task_id") or row.get("task_id") or "").strip()
    )
    result_count_by_task = Counter(
        str(row.get("source_task_id") or row.get("task_id") or "")
        for row in bundle.web_search_results
        if str(row.get("source_task_id") or row.get("task_id") or "").strip()
    )
    rejected_by_task: dict[str, list[Mapping[str, Any]]] = {}
    for row in bundle.web_rejected_documents:
        task_id = str(row.get("source_task_id") or row.get("task_id") or "")
        if not task_id or task_id in seen_task_ids:
            continue
        execution = executions_by_task_id.get(task_id)
        rejection_phase = str(row.get("rejection_phase") or "")
        if execution is not None and execution.accepted_claim_ids and rejection_phase != "post_extraction_evidence_os":
            continue
        rejected_by_task.setdefault(task_id, []).append(row)
    for task_id in sorted(rejected_by_task):
        rejected_rows = rejected_by_task[task_id]
        execution = executions_by_task_id.get(task_id)
        task_payload = dict(execution.source_task) if execution is not None else {}
        reason_counts = Counter(str(row.get("rejection_reason") or "unknown_source_rejection") for row in rejected_rows)
        phase_counts = Counter(
            str(row.get("rejection_phase") or "pre_extraction_source_filter") for row in rejected_rows
        )
        not_eligible_counts = Counter(
            str(reason)
            for row in rejected_rows
            for reason in (row.get("not_eligible_reasons") or ())
            if str(reason).strip()
        )
        provider_error_counts = Counter(
            str(reason)
            for row in rejected_rows
            for reason in (row.get("provider_errors") or ())
            if str(reason).strip()
        )
        examples: list[Mapping[str, Any]] = []
        for row in rejected_rows[:3]:
            result_row = web_results_by_id.get(str(row.get("web_result_id") or ""))
            examples.append(
                {
                    "query": row.get("query"),
                    "url": row.get("url"),
                    "title": row.get("title"),
                    "provider_name": row.get("provider_name"),
                    "rejection_phase": row.get("rejection_phase") or "pre_extraction_source_filter",
                    "rejection_reason": row.get("rejection_reason"),
                    "not_eligible_reasons": list(row.get("not_eligible_reasons") or ())[:6],
                    "selection_status": (result_row or {}).get("selection_status"),
                }
            )
        primitive_gap = str(task_payload.get("primitive_gap") or rejected_rows[0].get("primitive_gap") or "")
        rows.append(
            {
                "source_task_id": task_id,
                "candidate_event_id": str(rejected_rows[0].get("candidate_event_id") or task_payload.get("candidate_event_id") or ""),
                "symbol": str(rejected_rows[0].get("symbol") or task_payload.get("symbol") or ""),
                "company_name": str(rejected_rows[0].get("company_name") or task_payload.get("company_name") or ""),
                "primitive_gap": primitive_gap,
                "task_type": str(task_payload.get("task_type") or ""),
                "preferred_source_classes": list(task_payload.get("preferred_source_classes") or ()),
                "fallback_source_classes": list(task_payload.get("fallback_source_classes") or ()),
                "query_count": len({str(row.get("query") or "") for row in rejected_rows if str(row.get("query") or "").strip()}),
                "search_result_count": int(result_count_by_task.get(task_id, len(rejected_rows))),
                "rejected_source_count": len(rejected_rows),
                "fetched_document_count": int(fetched_count_by_task.get(task_id, 0)),
                "selected_source_count": int(fetched_count_by_task.get(task_id, 0)),
                "rejection_phase_distribution": dict(phase_counts),
                "rejection_reason_distribution": dict(reason_counts),
                "not_eligible_reason_distribution": dict(not_eligible_counts),
                "provider_error_distribution": dict(provider_error_counts),
                "sample_rejected_sources": examples,
                "source_rejection_summary": ";".join(
                    f"{reason}:{count}"
                    for reason, count in (
                        *phase_counts.most_common(2),
                        *reason_counts.most_common(4),
                        *not_eligible_counts.most_common(4),
                    )
                ),
            }
        )
        if len(rows) >= limit:
            return tuple(rows)
    return tuple(rows)


def _rerouted_claim_feedback_from_bundle(
    bundle: EvidenceOSExecutionBundleV4,
    *,
    limit: int = 8,
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    for execution in bundle.executions:
        if len(rows) >= limit:
            return tuple(rows)
        if execution.satisfies_source_task:
            continue
        if not execution.rerouted_accepted_claim_ids:
            continue
        task = dict(execution.source_task)
        accepted_primitives = tuple(
            str(item)
            for item in (execution.accepted_primitive_ids or ())
            if str(item).strip()
        )
        unsatisfied_primitives = tuple(
            str(item)
            for item in (execution.primitive_gap_unsatisfied_ids or ())
            if str(item).strip()
        ) or (str(execution.primitive_gap or task.get("primitive_gap") or ""),)
        rows.append(
            {
                "source_task_id": execution.task_id,
                "candidate_event_id": execution.candidate_event_id
                or str(task.get("candidate_event_id") or ""),
                "symbol": execution.symbol or str(task.get("symbol") or ""),
                "company_name": execution.company_name or str(task.get("company_name") or ""),
                "requested_primitive_gap": str(execution.primitive_gap or task.get("primitive_gap") or ""),
                "accepted_claim_ids": list(execution.rerouted_accepted_claim_ids),
                "accepted_primitive_ids": list(accepted_primitives),
                "primitive_gap_unsatisfied_ids": list(unsatisfied_primitives),
                "satisfaction_type": execution.satisfaction_type,
                "source_class": execution.source_class,
                "provider_name": execution.provider_name,
                "preferred_source_classes": list(
                    execution.preferred_source_classes or task.get("preferred_source_classes") or ()
                ),
                "fallback_source_classes": list(
                    execution.fallback_source_classes or task.get("fallback_source_classes") or ()
                ),
                "document_ids": list(execution.fetched_document_ids),
                "document_urls": list(execution.document_urls),
                "feedback_summary": (
                    "accepted_claim_rerouted_to_"
                    f"{','.join(accepted_primitives) or 'other_primitive'};"
                    "original_gap_still_unsatisfied:"
                    f"{','.join(unsatisfied_primitives)}"
                ),
            }
        )
    return tuple(rows)


def _source_rejection_feedback_tags(source_feedback: Sequence[Mapping[str, Any]]) -> tuple[str, ...]:
    has_unverified_original = any(
        str(reason).startswith("source_lineage_unverified_original")
        for row in source_feedback
        for reason in (
            (row.get("not_eligible_reason_distribution") or {}).keys()
            if isinstance(row.get("not_eligible_reason_distribution"), Mapping)
            else ()
        )
    )
    for row in source_feedback:
        phase_distribution = row.get("rejection_phase_distribution") or {}
        phases = phase_distribution.keys() if isinstance(phase_distribution, Mapping) else ()
        if any(str(phase) == "post_extraction_evidence_os" for phase in phases):
            if has_unverified_original:
                return (
                    "previous_source_lineage_unverified_original",
                    "previous_sources_failed_before_or_after_extraction",
                )
            return ("previous_sources_failed_before_or_after_extraction",)
    if has_unverified_original:
        return (
            "previous_source_lineage_unverified_original",
            "previous_sources_rejected_before_extraction",
        )
    return ("previous_sources_rejected_before_extraction",)


def _rejected_claim_feedback_from_bundle(
    bundle: EvidenceOSExecutionBundleV4,
    *,
    limit: int = 8,
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    raw_rejections_by_claim = _raw_assertion_rejections_by_claim(bundle)
    for execution in bundle.executions:
        if execution.accepted_claim_ids or not execution.rejected_claim_ids:
            continue
        task = dict(execution.source_task)
        for claim_id in execution.rejected_claim_ids:
            claim = bundle.ledger.claims.get(claim_id)
            if claim is None:
                continue
            mapping = _mapping_for_claim(bundle, claim_id)
            document = bundle.documents.get(claim.source_document_id)
            anchor = bundle.anchors.get(claim.source_anchor_id)
            raw = bundle.raw_assertions.get(claim.raw_assertion_id)
            raw_rejection = raw_rejections_by_claim.get(claim_id) or raw_rejections_by_claim.get(claim.raw_assertion_id)
            reasons = tuple(
                str(reason)
                for reason in (
                    (raw_rejection or {}).get("not_eligible_reasons")
                    or execution.not_eligible_reasons
                    or ()
                )
                if str(reason).strip()
            )
            rationale = str((raw_rejection or {}).get("mapping_rationale") or getattr(mapping, "rationale", "") or "")
            rejection_reason = str((raw_rejection or {}).get("rejection_reason") or "")
            target_scope_status = str((raw_rejection or {}).get("target_scope_status") or _enum_value(claim.target_scope_status) or "")
            directness = str((raw_rejection or {}).get("directness") or _enum_value(claim.directness) or "")
            semantic_status = str((raw_rejection or {}).get("semantic_status") or _enum_value(claim.semantic_status) or "")
            temporal_status = str((raw_rejection or {}).get("temporal_status") or _enum_value(claim.temporal_status) or "")
            polarity = str((raw_rejection or {}).get("polarity") or _enum_value(claim.polarity) or "")
            mapping_status = str((raw_rejection or {}).get("mapping_status") or _enum_value(getattr(mapping, "mapping_status", None)) or "")
            mapped_primitive_id = (raw_rejection or {}).get("mapped_primitive_id") or getattr(mapping, "primitive_id", None)
            support_direction = str((raw_rejection or {}).get("support_direction") or _enum_value(getattr(mapping, "support_direction", None)) or "")
            contract_feedback = _contract_compatibility_feedback(
                task=task,
                claim=claim,
                raw=raw,
                anchor=anchor,
                reasons=reasons,
                rationale=rationale,
                rejection_reason=rejection_reason,
                mapped_primitive_id=str(mapped_primitive_id or ""),
            )
            rows.append(
                {
                    "source_task_execution_id": deterministic_id(
                        "SRCEXEC-FEEDBACK",
                        (execution.task_id, claim_id, reasons, rationale),
                    ),
                    "source_task_id": execution.task_id,
                    "primitive_gap": str(task.get("primitive_gap") or ""),
                    "task_type": str(task.get("task_type") or ""),
                    "preferred_source_classes": list(task.get("preferred_source_classes") or ()),
                    "fallback_source_classes": list(task.get("fallback_source_classes") or ()),
                    "claim_id": claim.claim_id,
                    "raw_assertion_id": claim.raw_assertion_id,
                    "mapping_id": getattr(mapping, "mapping_id", None),
                    "document_id": claim.source_document_id,
                    "anchor_id": claim.source_anchor_id,
                    "source_url": document.canonical_url if document else None,
                    "source_provider": document.source_name if document else None,
                    "anchor_verified": bool(anchor.anchor_verified) if anchor else False,
                    "raw_assertion_rejection_id": (raw_rejection or {}).get("raw_assertion_rejection_id"),
                    "raw_assertion_rejection_reason": rejection_reason or None,
                    "quote_preview": _preview_text(
                        (raw.exact_quote if raw else "") or (anchor.exact_text if anchor else ""),
                        limit=360,
                    ),
                    "target_scope_status": target_scope_status,
                    "directness": directness,
                    "semantic_status": semantic_status,
                    "temporal_status": temporal_status,
                    "polarity": polarity,
                    "mapping_status": mapping_status,
                    "mapped_primitive_id": mapped_primitive_id,
                    "support_direction": support_direction,
                    "eligibility_reasons": list(reasons),
                    "mapping_rationale": rationale,
                    "rejection_summary": _rejection_summary(
                        reasons=((rejection_reason,) if rejection_reason else ()) + reasons,
                        rationale=rationale,
                    ),
                    **contract_feedback,
                }
            )
            if len(rows) >= limit:
                return tuple(rows)
    return tuple(rows)


def _contract_compatibility_feedback(
    *,
    task: Mapping[str, Any],
    claim: Any,
    raw: Any | None,
    anchor: Any | None,
    reasons: Sequence[str],
    rationale: str,
    rejection_reason: str,
    mapped_primitive_id: str,
) -> Mapping[str, Any]:
    primitive_gap = str(task.get("primitive_gap") or "")
    text = " ".join(
        str(value or "")
        for value in (
            primitive_gap,
            mapped_primitive_id,
            rejection_reason,
            rationale,
            " ".join(str(reason) for reason in reasons),
            getattr(raw, "predicate", ""),
            getattr(raw, "object_text", ""),
            getattr(raw, "value", ""),
            getattr(raw, "exact_quote", ""),
            getattr(anchor, "exact_text", ""),
            getattr(claim, "adjudication_rationale", ""),
        )
    ).lower()
    contract_signal = any(
        token in text
        for token in (
            "structured_field_contract_quality",
            "revenue_visibility_contract",
            "export_contract",
            "contract_amount_to_prior_sales",
            "contract_duration_months",
            "contract_or_order_claim",
            "단일판매",
            "공급계약",
            "판매공급계약",
            "판매ㆍ공급계약",
            "판매·공급계약",
        )
    )
    requested_compatible = primitive_gap in CONTRACT_COMPATIBLE_PRIMITIVES or mapped_primitive_id in CONTRACT_COMPATIBLE_PRIMITIVES
    required = bool(contract_signal and not requested_compatible)
    return {
        "contract_compatible_route_required": required,
        "contract_signal_detected": bool(contract_signal),
        "rejected_primitive_contract_compatible": bool(requested_compatible),
        "contract_compatible_primitive_hints": sorted(CONTRACT_COMPATIBLE_PRIMITIVES) if required else [],
        "contract_compatibility_feedback": (
            "contract_fields_found_but_selected_primitive_incompatible"
            if required
            else ""
        ),
    }


def _raw_assertion_rejections_by_claim(bundle: EvidenceOSExecutionBundleV4) -> dict[str, Mapping[str, Any]]:
    rows: dict[str, Mapping[str, Any]] = {}
    for row in bundle.raw_assertion_rejections:
        claim_id = str(row.get("claim_id") or row.get("adjudicated_claim_id") or "")
        raw_assertion_id = str(row.get("raw_assertion_id") or "")
        if claim_id and claim_id not in rows:
            rows[claim_id] = row
        if raw_assertion_id and raw_assertion_id not in rows:
            rows[raw_assertion_id] = row
    return rows


def _mapping_for_claim(bundle: EvidenceOSExecutionBundleV4, claim_id: str) -> Any | None:
    rejected = [
        mapping
        for mapping in bundle.ledger.mappings.values()
        if mapping.claim_id == claim_id and _enum_value(mapping.mapping_status) == "REJECTED"
    ]
    if rejected:
        return rejected[-1]
    for mapping in bundle.ledger.mappings.values():
        if mapping.claim_id == claim_id:
            return mapping
    return None


def _deduplicated_feedback_retry_tasks(
    *,
    event: CandidateEventV2,
    original_tasks: Sequence[SourceTask],
    retry_tasks: Sequence[SourceTask],
    reason_tag: str = "rejected_claim_mapping",
    rerouted_claim_feedback: Sequence[Mapping[str, Any]] = (),
) -> tuple[SourceTask, ...]:
    kept, _ = _deduplicated_feedback_retry_tasks_with_rejections(
        event=event,
        original_tasks=original_tasks,
        retry_tasks=retry_tasks,
        reason_tag=reason_tag,
        rerouted_claim_feedback=rerouted_claim_feedback,
    )
    return kept


def _deduplicated_feedback_retry_tasks_with_rejections(
    *,
    event: CandidateEventV2,
    original_tasks: Sequence[SourceTask],
    retry_tasks: Sequence[SourceTask],
    reason_tag: str = "rejected_claim_mapping",
    rerouted_claim_feedback: Sequence[Mapping[str, Any]] = (),
) -> tuple[tuple[SourceTask, ...], tuple[SourceTaskExecutionV4, ...]]:
    original_signatures = {_source_task_signature(task) for task in original_tasks}
    seen = set(original_signatures)
    blocked_sources_by_primitive = _rerouted_blocked_sources_by_primitive(rerouted_claim_feedback)
    rows: list[SourceTask] = []
    rejected: list[SourceTaskExecutionV4] = []
    for index, task in enumerate(retry_tasks):
        original_task = task
        sanitized_task, removed_sources = _remove_rerouted_only_sources_from_retry_task(
            task=task,
            blocked_sources_by_primitive=blocked_sources_by_primitive,
        )
        if sanitized_task is None:
            rejected.append(
                _rerouted_source_retry_drop_execution(
                    event=event,
                    task=original_task,
                    index=index,
                    removed_sources=removed_sources,
                    reason_tag=reason_tag,
                )
            )
            continue
        task = sanitized_task
        if (
            reason_tag == "source_lineage_unverified_original"
            and _source_lineage_retry_task_is_discovery_only(task)
        ):
            rejected.append(
                _source_lineage_retry_drop_execution(
                    event=event,
                    task=task,
                    index=index,
                    reason_tag=reason_tag,
                )
            )
            continue
        signature = _source_task_signature(task)
        if signature in seen:
            continue
        seen.add(signature)
        rows.append(
            replace(
                task,
                task_id=deterministic_id(
                    "RSTASKV4RETRY",
                    (event.candidate_event_id, index, task.task_id, signature),
                ),
                reason_from_memory=_feedback_retry_reason_from_memory(
                    base=task.reason_from_memory,
                    reason_tag=reason_tag,
                    removed_sources=removed_sources,
                ),
            )
        )
    return tuple(rows), tuple(rejected)


def _rerouted_blocked_sources_by_primitive(
    rerouted_claim_feedback: Sequence[Mapping[str, Any]],
) -> dict[str, set[str]]:
    blocked: dict[str, set[str]] = {}
    for row in rerouted_claim_feedback:
        source_names = {
            _source_name_key(row.get("source_class")),
            _source_name_key(row.get("provider_name")),
        }
        source_names = {name for name in source_names if name}
        if not source_names:
            continue
        primitive_ids = {
            str(item or "").strip()
            for item in (row.get("primitive_gap_unsatisfied_ids") or ())
            if str(item or "").strip()
        }
        requested = str(row.get("requested_primitive_gap") or "").strip()
        if requested:
            primitive_ids.add(requested)
        for primitive_id in primitive_ids:
            blocked.setdefault(primitive_id, set()).update(source_names)
    return blocked


def _remove_rerouted_only_sources_from_retry_task(
    *,
    task: SourceTask,
    blocked_sources_by_primitive: Mapping[str, set[str]],
) -> tuple[SourceTask | None, tuple[str, ...]]:
    blocked = blocked_sources_by_primitive.get(task.primitive_gap) or set()
    if not blocked:
        return task, ()
    removed: list[str] = []

    def keep(values: Sequence[str]) -> tuple[str, ...]:
        kept: list[str] = []
        for value in values:
            if _source_name_key(value) in blocked:
                removed.append(str(value))
                continue
            kept.append(str(value))
        return tuple(kept)

    preferred = keep(task.preferred_source_classes)
    fallback = keep(task.fallback_source_classes)
    if not removed:
        return task, ()
    if not preferred and fallback:
        preferred = (fallback[0],)
        fallback = tuple(fallback[1:])
    if not preferred:
        return None, tuple(dict.fromkeys(removed))
    return replace(task, preferred_source_classes=preferred, fallback_source_classes=fallback), tuple(dict.fromkeys(removed))


def _feedback_retry_reason_from_memory(*, base: str, reason_tag: str, removed_sources: Sequence[str]) -> str:
    value = f"{base};feedback_retry:{reason_tag}"
    if removed_sources:
        value = f"{value};rerouted_source_removed:{','.join(removed_sources)}"
    return value


def _source_name_key(value: Any) -> str:
    return "".join(ch for ch in str(value or "").lower() if ch.isalnum())


def _rerouted_source_retry_drop_execution(
    *,
    event: CandidateEventV2,
    task: SourceTask,
    index: int,
    removed_sources: Sequence[str],
    reason_tag: str,
) -> SourceTaskExecutionV4:
    reason = "rerouted_feedback_removed_all_candidate_source_classes"
    task_payload = {
        **task.to_dict(),
        "reason_from_memory": _feedback_retry_reason_from_memory(
            base=task.reason_from_memory,
            reason_tag=reason_tag,
            removed_sources=removed_sources,
        ),
    }
    return SourceTaskExecutionV4(
        task_id=deterministic_id("RSTASKV4RETRYDROP", (event.candidate_event_id, index, task.task_id, reason)),
        source_task=task_payload,
        status=SourceTaskExecutionStatusV4.REJECTED_BY_POLICY.value,
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id=task.archetype_id,
        primitive_gap=task.primitive_gap,
        source_class="policy",
        provider_name="research_brain_v4_retry_policy",
        source_task_origin="feedback_retry",
        preferred_source_classes=task.preferred_source_classes,
        fallback_source_classes=task.fallback_source_classes,
        forbidden_source_classes=task.forbidden_source_classes,
        requested_source_classes=(*task.preferred_source_classes, *task.fallback_source_classes),
        not_eligible_reasons=(reason,),
        provider_errors=(reason,),
        budget_used={"queries": 0, "candidates": 0, "fetches": 0},
        stop_reason=reason,
    )


def _source_lineage_retry_drop_execution(
    *,
    event: CandidateEventV2,
    task: SourceTask,
    index: int,
    reason_tag: str,
) -> SourceTaskExecutionV4:
    reason = "source_lineage_retry_discovery_only_after_unverified_original"
    task_payload = {
        **task.to_dict(),
        "reason_from_memory": f"{task.reason_from_memory};feedback_retry:{reason_tag};dropped:{reason}",
    }
    requested_classes = tuple((*task.preferred_source_classes, *task.fallback_source_classes))
    return SourceTaskExecutionV4(
        task_id=deterministic_id("RSTASKV4RETRYDROP", (event.candidate_event_id, index, task.task_id, reason)),
        source_task=task_payload,
        status=SourceTaskExecutionStatusV4.REJECTED_BY_POLICY.value,
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id=task.archetype_id,
        primitive_gap=task.primitive_gap,
        source_class="policy",
        provider_name="research_brain_v4_retry_policy",
        source_task_origin="feedback_retry",
        preferred_source_classes=task.preferred_source_classes,
        fallback_source_classes=task.fallback_source_classes,
        forbidden_source_classes=task.forbidden_source_classes,
        requested_source_classes=requested_classes,
        not_eligible_reasons=(reason,),
        provider_errors=(reason,),
        budget_used={"queries": 0, "candidates": 0, "fetches": 0},
        stop_reason=reason,
    )


def _append_retry_drop_executions_to_bundle(
    *,
    bundle: EvidenceOSExecutionBundleV4,
    executions: Sequence[SourceTaskExecutionV4],
) -> EvidenceOSExecutionBundleV4:
    if not executions:
        return bundle
    audit = Counter({key: int(value) for key, value in bundle.extraction_audit.items()})
    audit["source_lineage_feedback_retry_dropped_count"] += len(executions)
    return EvidenceOSExecutionBundleV4(
        ledger=bundle.ledger,
        executions=tuple((*bundle.executions, *executions)),
        documents=bundle.documents,
        anchors=bundle.anchors,
        document_text_by_id=bundle.document_text_by_id,
        extraction_audit=dict(audit),
        raw_assertions=bundle.raw_assertions,
        web_search_tasks=bundle.web_search_tasks,
        web_search_results=bundle.web_search_results,
        web_fetched_documents=bundle.web_fetched_documents,
        web_rejected_documents=bundle.web_rejected_documents,
        claim_extractor_runs=bundle.claim_extractor_runs,
        raw_assertion_rejections=bundle.raw_assertion_rejections,
    )


def _source_lineage_retry_task_is_discovery_only(task: SourceTask) -> bool:
    classes = {
        str(item or "").strip().lower()
        for item in (*task.preferred_source_classes, *task.fallback_source_classes)
        if str(item or "").strip()
    }
    if not classes:
        return False
    original_capable = {
        "brokerreportpublicpdf",
        "companynewsroom",
        "dart",
        "ir",
        "issuerofficial",
        "kind",
        "krx",
        "reportpdf",
        "trustednews",
    }
    discovery_only = {
        "generalweb",
        "generalwebsearch",
        "industrymedia",
        "naversearch",
        "news",
        "web",
    }
    return bool(classes & discovery_only) and not bool(classes & original_capable)


def _source_task_signature(task: SourceTask) -> tuple[Any, ...]:
    return (
        task.primitive_gap,
        task.task_type,
        tuple(str(item).lower() for item in task.preferred_source_classes),
        tuple(str(item).lower() for item in task.fallback_source_classes),
        tuple(str(item).lower() for item in task.query_intents),
    )


def _merge_evidence_os_bundles_v4(
    base: EvidenceOSExecutionBundleV4,
    follow_up: EvidenceOSExecutionBundleV4,
) -> EvidenceOSExecutionBundleV4:
    ledger = AppendOnlyEvidenceLedger()
    for source in (base, follow_up):
        for claim in source.ledger.claims.values():
            _append_claim_for_bundle_merge(ledger=ledger, claim=claim)
        for mapping in source.ledger.mappings.values():
            _append_mapping_for_bundle_merge(ledger=ledger, mapping=mapping)
        for event in source.ledger.events:
            ledger.append_event(event)
    audit = Counter({key: int(value) for key, value in base.extraction_audit.items()})
    audit.update({key: int(value) for key, value in follow_up.extraction_audit.items()})
    return EvidenceOSExecutionBundleV4(
        ledger=ledger,
        executions=tuple((*base.executions, *follow_up.executions)),
        documents={**base.documents, **follow_up.documents},
        anchors={**base.anchors, **follow_up.anchors},
        document_text_by_id={**base.document_text_by_id, **follow_up.document_text_by_id},
        extraction_audit=dict(audit),
        raw_assertions={**base.raw_assertions, **follow_up.raw_assertions},
        web_search_tasks=tuple((*base.web_search_tasks, *follow_up.web_search_tasks)),
        web_search_results=tuple((*base.web_search_results, *follow_up.web_search_results)),
        web_fetched_documents=tuple((*base.web_fetched_documents, *follow_up.web_fetched_documents)),
        web_rejected_documents=tuple((*base.web_rejected_documents, *follow_up.web_rejected_documents)),
        claim_extractor_runs=tuple((*base.claim_extractor_runs, *follow_up.claim_extractor_runs)),
        raw_assertion_rejections=tuple((*base.raw_assertion_rejections, *follow_up.raw_assertion_rejections)),
    )


def _append_claim_for_bundle_merge(*, ledger: AppendOnlyEvidenceLedger, claim: Any) -> None:
    try:
        ledger.append_claim(claim)
    except ValueError as exc:
        if "claim_id collision with different claim" not in str(exc):
            raise
        # A retry can re-adjudicate the same source assertion differently. Keep
        # the first immutable claim row and record that a retry attempted to
        # update it; do not crash the entire Brain/Web attempt.
        ledger.append_event(
            LedgerEvent.build(
                event_type=LedgerEventType.UPDATES,
                from_id=claim.claim_id,
                reason="merge_retry_claim_id_collision_existing_claim_retained",
            )
        )


def _append_mapping_for_bundle_merge(*, ledger: AppendOnlyEvidenceLedger, mapping: Any) -> None:
    try:
        ledger.append_mapping(mapping)
    except ValueError as exc:
        if "mapping_id collision with different mapping" not in str(exc):
            raise
        retry_mapping = replace(
            mapping,
            mapping_id=deterministic_id(
                "MAPRETRY",
                (
                    mapping.mapping_id,
                    mapping.claim_id,
                    mapping.archetype_id,
                    mapping.primitive_id,
                    _enum_value(mapping.support_direction),
                    _enum_value(mapping.mapping_status),
                    mapping.rationale,
                ),
            ),
        )
        ledger.append_mapping(retry_mapping)


def _bundle_has_accepted_claims(bundle: EvidenceOSExecutionBundleV4 | None) -> bool:
    if bundle is None:
        return False
    return any(execution.accepted_claim_ids for execution in bundle.executions)


def _bundle_has_direct_source_task_acceptance(bundle: EvidenceOSExecutionBundleV4 | None) -> bool:
    if bundle is None:
        return False
    return any(execution.satisfies_source_task and execution.direct_accepted_claim_ids for execution in bundle.executions)


def _bundle_has_unresolved_external_web_or_llm_failure(bundle: EvidenceOSExecutionBundleV4 | None) -> bool:
    if bundle is None:
        return False
    if _source_rejection_feedback_from_bundle(bundle):
        return True
    web_task_ids = _web_source_task_ids(bundle)
    executions_by_task_id = {execution.task_id: execution for execution in bundle.executions}
    for row in bundle.raw_assertion_rejections:
        task_id = str(row.get("source_task_id") or row.get("task_id") or "")
        execution = executions_by_task_id.get(task_id)
        if execution is not None and execution.accepted_claim_ids:
            continue
        raw_id = str(row.get("raw_assertion_id") or "")
        if raw_id.startswith("RAWLLM-") or task_id in web_task_ids or _row_uses_external_web(row):
            return True
        if execution is not None and _execution_uses_external_web_or_llm(execution, web_task_ids=web_task_ids):
            return True
    for execution in bundle.executions:
        if execution.accepted_claim_ids:
            continue
        if not (execution.rejected_claim_ids or execution.not_eligible_reasons or execution.provider_errors):
            continue
        if _execution_uses_external_web_or_llm(execution, web_task_ids=web_task_ids):
            return True
    return False


def _web_source_task_ids(bundle: EvidenceOSExecutionBundleV4) -> set[str]:
    rows: list[Mapping[str, Any]] = []
    rows.extend(bundle.web_search_tasks)
    rows.extend(bundle.web_search_results)
    rows.extend(bundle.web_fetched_documents)
    rows.extend(bundle.web_rejected_documents)
    task_ids: set[str] = set()
    for row in rows:
        task_id = str(row.get("source_task_id") or row.get("task_id") or "")
        if task_id:
            task_ids.add(task_id)
    return task_ids


def _execution_uses_external_web_or_llm(execution: SourceTaskExecutionV4, *, web_task_ids: set[str]) -> bool:
    if execution.task_id in web_task_ids:
        return True
    payload = dict(execution.source_task)
    if _row_uses_external_web(
        {
            "source_class": execution.source_class,
            "provider_name": execution.provider_name,
            "preferred_source_classes": execution.preferred_source_classes or payload.get("preferred_source_classes"),
            "fallback_source_classes": execution.fallback_source_classes or payload.get("fallback_source_classes"),
            "requested_source_classes": execution.requested_source_classes or (),
        }
    ):
        # A fallback class alone should not mark a DART/KIND claim as external.
        return bool(execution.source_class or execution.provider_name or execution.task_id in web_task_ids)
    return any(str(raw_id).startswith("RAWLLM-") for raw_id in execution.raw_assertion_ids)


def _row_uses_external_web(row: Mapping[str, Any]) -> bool:
    external_names = {
        "naversearch",
        "generalwebsearch",
        "trustednews",
        "news",
        "industrymedia",
        "companynewsroom",
        "reportpdf",
        "brokerreportpublicpdf",
        "naverfreesearchprovider",
    }
    values: list[Any] = []
    for key in (
        "source_class",
        "provider_name",
        "preferred_source_classes",
        "fallback_source_classes",
        "requested_source_classes",
    ):
        value = row.get(key)
        if isinstance(value, (list, tuple, set)):
            values.extend(value)
        else:
            values.append(value)
    normalized = {"".join(ch for ch in str(value or "").lower() if ch.isalnum()) for value in values}
    return bool(normalized & external_names)


def _rejection_summary(*, reasons: Sequence[str], rationale: str) -> str:
    clean_reasons = [str(reason).strip() for reason in reasons if str(reason).strip()]
    if clean_reasons:
        return ";".join(clean_reasons[:4])
    return _preview_text(rationale, limit=180) or "rejected_before_score"


def _preview_text(value: str, *, limit: int) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else f"{text[: max(0, limit - 3)]}..."


def _enum_value(value: Any) -> Any:
    return getattr(value, "value", value)


def _requires_external_web_plan(config: ProductionShadowV4Config) -> bool:
    return (
        config.source_acquisition == SourceAcquisitionModeV4.LIVE_FULL_BOUNDED.value
        and config.planner_provider not in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}
    )


def _allows_feedback_retry(config: ProductionShadowV4Config) -> bool:
    """Allow planner repair after source/claim rejection in live acquisition modes.

    External-web planning is stricter and only applies to live_full_bounded.
    Rejected-claim feedback is different: even official-first runs can fetch the
    wrong official document, such as a financing disclosure for a capacity gap.
    In that case the planner should see the rejection and choose another bounded
    official/IR/report route instead of letting the first failed task end the
    full-thesis refresh.
    """

    live_modes = {
        SourceAcquisitionModeV4.LIVE_OFFICIAL_FIRST.value,
        SourceAcquisitionModeV4.LIVE_OFFICIAL_ONLY.value,
        SourceAcquisitionModeV4.LIVE_FULL_BOUNDED.value,
    }
    return (
        config.source_acquisition in live_modes
        and config.planner_provider not in {PlannerProviderModeV4.NONE.value, PlannerProviderModeV4.FAKE.value}
    )


def _external_web_plan_gaps(run: PlannerRunV4) -> tuple[str, ...]:
    if not run.output:
        return ()
    gaps: list[str] = []
    if not tuple(str(item).strip() for item in run.output.query_intents if str(item).strip()):
        gaps.append("query_intents_empty")
    if not tuple(run.output.source_task_drafts) and not _planner_output_requests_external_web(run.output):
        gaps.append("no_external_web_source_task")
    return tuple(dict.fromkeys(gaps))


def _planner_output_requests_external_web(output: Any) -> bool:
    if not tuple(str(item).strip() for item in getattr(output, "query_intents", ()) if str(item).strip()):
        return False
    external = {
        "naversearch",
        "generalwebsearch",
        "trustednews",
        "news",
        "industrymedia",
        "companynewsroom",
        "reportpdf",
        "brokerreportpublicpdf",
    }
    for draft in getattr(output, "source_task_drafts", ()) or ():
        primitive = str(draft.get("primitive_gap") or draft.get("primitive_id") or "")
        if _planner_official_solvable_gap(primitive):
            continue
        source_names = {
            _planner_source_name(item)
            for item in (
                *(draft.get("preferred_source_classes") or ()),
                *(draft.get("fallback_source_classes") or ()),
            )
        }
        if source_names & external:
            return True
    return False


def _planner_source_name(value: object) -> str:
    return "".join(ch for ch in str(value or "").strip().lower() if ch.isalnum())


def _planner_official_solvable_gap(primitive: str) -> bool:
    lower = primitive.lower()
    if lower in _OFFICIAL_SOLVABLE_PRIMITIVE_IDS:
        return True
    return any(token in lower for token in ("backlog", "cash", "fcf", "revision", "rpo"))


def _reason_codes_from_report(row: Mapping[str, Any], comment: str) -> list[str]:
    codes = []
    for key in ("EPS_ACTION_TYP_NM", "PRC_ACTION_TYP_NM", "RECOMM_ACTION_TYP_NM"):
        value = str(row.get(key) or "")
        if "상향" in value:
            codes.append(f"{key}_UP")
    text = f"{row.get('RPT_TITLE') or ''} {comment}"
    for token, code in (("HBM", "HBM"), ("메모리", "MEMORY"), ("공급", "SUPPLY"), ("계약", "CONTRACT")):
        if token in text:
            codes.append(code)
    return codes or ["REPORT_RADAR"]


def _watchlist_signature(report: Mapping[str, Any]) -> str:
    rows = report.get("rows", ())
    parts = [
        f"{row.get('candidate_event_id')}:{row.get('verified_score')}:{row.get('base_stage')}:{row.get('score_valid_status')}"
        for row in rows
    ]
    return "|".join(parts)


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _csv_rows(path: Path) -> tuple[dict[str, str], ...]:
    if not path.exists():
        return ()
    import csv

    with path.open("r", encoding="utf-8", newline="") as handle:
        return tuple(dict(row) for row in csv.DictReader(handle))


def _date_from_path(path: Path) -> date | None:
    for part in reversed(path.parts):
        parsed = _date_from_any(part)
        if parsed:
            return parsed
    return None


def _date_from_any(value: Any) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    text = str(value).strip().replace(".", "-")
    if len(text) >= 8 and text[:8].isdigit():
        text = f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def _yy_mm_dd_date(value: Any, as_of_date: date) -> date | None:
    text = str(value or "").strip()
    import re

    match = re.match(r"(?P<yy>\d{2})[./-](?P<mm>\d{1,2})[./-](?P<dd>\d{1,2})$", text)
    if not match:
        return _date_from_any(value)
    year = 2000 + int(match.group("yy"))
    parsed = date(year, int(match.group("mm")), int(match.group("dd")))
    if parsed > as_of_date and year - 100 >= 1990:
        parsed = date(year - 100, parsed.month, parsed.day)
    return parsed


def _strip_html(value: str) -> str:
    import re

    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


__all__ = [
    "DEFAULT_V1_ARCHETYPE_MATRIX",
    "build_candidate_event_report_v4",
    "build_daily_watchlist_report_v4",
    "build_evidence_extraction_audit_v4",
    "build_real_planner_report_v4",
    "build_sector_coverage_report_v4",
    "build_source_acquisition_report_v4",
    "build_source_provider_gap_report_v4",
    "build_static_logic_audit_from_reports_v4",
    "build_v4_readiness_verdict",
    "discover_daily_candidate_events_v4",
    "run_multi_day_shadow_v4",
    "run_research_brain_v4_production_shadow",
]
