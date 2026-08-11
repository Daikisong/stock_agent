"""Materialize the canonical Phase-105 official issuer-profile manifest.

The existing natural roster remains the stable KRX-order intersection of
current L3 depth decisions and real, successful, two-call planner abstentions.
A separate forced-validation lane may inspect the full current eligible KRX
roster with bounded OpenDART company/industry discovery, retain only sectors
required by the exact archetype roster, and then require the same full periodic
profile compatibility validation.  Natural COMPLETE planner runs keep using
the existing selector lane; PENDING attempts receive no forced authority.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
import json
import os
from pathlib import Path
import secrets
from typing import Any, Mapping, Sequence

from e2r.env import load_project_env
from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import (
    ISSUER_PROFILE_MANIFEST_NAME,
    _LIVE_SELECTION_INPUT_FILES,
    _PLANNER_RUN_KEYS,
    _candidate_event,
    _deep_result_keys,
    _depth_decision,
    _jsonl_objects,
    _planner_projection,
    _read_live_input_file,
    _universe_row,
    load_current_live_selection_inputs,
    publish_current_issuer_business_profile_manifest,
)
from e2r.production.v6_issuer_business_profile import (
    IssuerBusinessProfileConfig,
    IssuerBusinessProfileFetcher,
    IssuerBusinessCompatibilityProvider,
    PROFILE_PASS,
    RequestsOpenDartIssuerBusinessProfileFetcher,
    V6IssuerBusinessProfileMaterializer,
    validate_forced_validation_profile_manifest,
)
from e2r.production.v6_issuer_business_profile_collaboration import (
    CollaborationIssuerBusinessCompatibilityProvider,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)
from e2r.research_brain.intelligence_schema import stable_intelligence_id


PROFILE_MANIFEST_NAME = ISSUER_PROFILE_MANIFEST_NAME
PROFILE_JOURNAL_DIRECTORY = "issuer_business_profile_collaboration"
_PLANNER_PROVIDER_NAME = "codex_cli_two_pass_planner"
CUTOVER_RELATIVE_ROOT = Path("docs/operational/e2r_v6_operational_cutover")


@dataclass(frozen=True)
class CanonicalProfileInputs:
    universe_rows: tuple[Mapping[str, Any], ...]
    forced_discovery_rows: tuple[Mapping[str, Any], ...]
    l3_target_count: int
    natural_complete_count: int
    eligible_abstained_count: int
    ineligible_abstained_count: int
    pending_count: int


def _snapshot_live_inputs(root: Path) -> Mapping[str, bytes]:
    return {
        name: _read_live_input_file(root / name)
        for name in _LIVE_SELECTION_INPUT_FILES
    }


def _planner_common_lineage(
    run: Mapping[str, Any],
    *,
    as_of_date: str,
    universe_row: Mapping[str, Any],
    event: Any,
    depth: Any,
) -> None:
    if set(run) != _PLANNER_RUN_KEYS:
        raise ValueError("planner run schema keys are not exact")
    plan = run.get("plan")
    audit = run.get("input_compilation_audit")
    if not isinstance(plan, Mapping) or not isinstance(audit, Mapping):
        raise ValueError("planner plan/audit must be objects")
    blind_input_id = str(run.get("blind_input_id") or "")
    expected_plan_id = stable_intelligence_id(
        "two-pass-plan", {"blind_input_id": blind_input_id}
    )
    target_id = str(universe_row.get("symbol") or "")
    expected_run_id = "LIVEPLAN-" + stable_hash(
        {
            "target": target_id,
            "blind_input": blind_input_id,
            "plan": expected_plan_id,
        }
    )[:24]
    traces = tuple(plan.get("provider_traces") or ())
    provider_call_count = run.get("provider_call_count")
    if (
        run.get("schema_version") != "e2r_live_planner_run_v1"
        or run.get("planner_run_id") != expected_run_id
        or run.get("target_id") != target_id
        or run.get("target_name") != universe_row.get("company_name")
        or run.get("as_of_date") != as_of_date
        or run.get("candidate_event_id") != event.candidate_event_id
        or run.get("depth_decision_id") != depth.depth_decision_id
        or tuple(sorted(str(value) for value in run.get("trigger_signal_ids") or ()))
        != tuple(sorted(event.trigger_signal_ids))
        or tuple(sorted(str(value) for value in run.get("source_refs") or ()))
        != tuple(sorted(event.source_refs))
        or run.get("provider_name") != _PLANNER_PROVIDER_NAME
        or run.get("provider_real") is not True
        or run.get("provider_fake") is not False
        or isinstance(provider_call_count, bool)
        or not isinstance(provider_call_count, int)
        or provider_call_count < 0
        or len(traces) > provider_call_count
        or any(
            not isinstance(trace, Mapping)
            or trace.get("provider_name") != _PLANNER_PROVIDER_NAME
            or trace.get("real_provider") is not True
            or trace.get("fake_provider") is not False
            for trace in traces
        )
        or plan.get("plan_id") != expected_plan_id
        or plan.get("blind_input_id") != blind_input_id
        or plan.get("status") != run.get("terminal_status")
        or plan.get("deterministic_stage_or_score_mutation") is not False
        or isinstance(run.get("compiled_fact_count"), bool)
        or not isinstance(run.get("compiled_fact_count"), int)
        or run.get("compiled_fact_count") <= 0
        or audit.get("compiled_fact_count") != run.get("compiled_fact_count")
        or audit.get("input_row_count") != run.get("compiled_fact_count")
        or audit.get("score_stage_field_forwarded_count") != 0
        or audit.get("archetype_label_field_forwarded_count") != 0
        or audit.get("sector_context_forwarded_to_pass_a_count") != 0
    ):
        raise ValueError("planner/depth/KRX current identity binding is invalid")


def load_canonical_profile_inputs(
    live_root: str | Path,
    *,
    as_of_date: str,
) -> CanonicalProfileInputs:
    """Load the exact forced-profile lane from one fully audited live snapshot."""

    date.fromisoformat(as_of_date)
    root = Path(live_root)

    # The canonical selector owns the full twelve-leaf audit contract: accepted
    # universe/trigger/depth/planner audits, exact KRX request provenance, and
    # exact prompt/response/trace journal pairing.  Read the same leaves before
    # and after that validation so candidate derivation cannot silently mix two
    # concurrently changing live snapshots.
    before = _snapshot_live_inputs(root)
    load_current_live_selection_inputs(
        root,
        selection_as_of_date=as_of_date,
    )
    encoded = _snapshot_live_inputs(root)
    if encoded != before:
        raise ValueError("canonical profile inputs changed during full live audit")

    universe = _jsonl_objects(
        encoded["universe_eligible.jsonl"], context="profile eligible KRX universe"
    )
    signals = _jsonl_objects(
        encoded["trigger_signals.jsonl"], context="profile trigger signals"
    )
    events = _jsonl_objects(
        encoded["candidate_events.jsonl"], context="profile candidate events"
    )
    depths = _jsonl_objects(
        encoded["depth_decisions.jsonl"], context="profile depth decisions"
    )
    planners = _jsonl_objects(
        encoded["planner_runs.jsonl"], context="profile planner runs"
    )
    if not universe or not depths or not planners:
        raise ValueError("canonical profile inputs require universe, depth, and planner rows")
    forbidden_planner_keys = _deep_result_keys(planners)
    if forbidden_planner_keys:
        raise ValueError(
            "canonical profile planner lane exposes post-deep authority: "
            + ", ".join(forbidden_planner_keys)
        )

    universe_by_target: dict[str, Mapping[str, Any]] = {}
    for row in universe:
        member = _universe_row(row, selection_date=as_of_date)
        target = member.symbol
        if not target or target in universe_by_target:
            raise ValueError("eligible KRX universe target identity is invalid or duplicated")
        universe_by_target[target] = row

    depth_by_target: dict[str, Mapping[str, Any]] = {}
    depth_object_by_target: dict[str, Any] = {}
    for row in depths:
        depth = _depth_decision(row, require_acquisition_eligible=False)
        target = depth.target_id
        universe_row = universe_by_target.get(target)
        if (
            not target
            or target in depth_by_target
            or universe_row is None
            or depth.as_of_date != as_of_date
            or depth.target_name != universe_row.get("company_name")
        ):
            raise ValueError("depth-decision target identity is invalid or duplicated")
        depth_by_target[target] = row
        depth_object_by_target[target] = depth
    if set(depth_by_target) != set(universe_by_target):
        raise ValueError("depth-decision roster does not exactly bind the KRX universe")

    signal_by_id: dict[str, Mapping[str, Any]] = {}
    for row in signals:
        signal_id = str(row.get("trigger_signal_id") or "")
        if not signal_id or signal_id in signal_by_id:
            raise ValueError("trigger-signal identity is invalid or duplicated")
        signal_by_id[signal_id] = row

    event_by_target: dict[str, Mapping[str, Any]] = {}
    event_object_by_target: dict[str, Any] = {}
    for row in events:
        event = _candidate_event(row)
        target = event.target_id
        universe_row = universe_by_target.get(target)
        event_signals = tuple(
            signal_by_id.get(signal_id) for signal_id in event.trigger_signal_ids
        )
        signal_source_refs = tuple(
            sorted(
                {
                    str(source_ref)
                    for signal in event_signals
                    if isinstance(signal, Mapping)
                    for source_ref in signal.get("source_refs") or ()
                }
            )
        )
        if (
            not target
            or target in event_by_target
            or universe_row is None
            or event.as_of_date != as_of_date
            or event.latest_effective_date > as_of_date
            or event.target_name != universe_row.get("company_name")
            or any(
                not isinstance(signal, Mapping)
                or signal.get("target_id") != target
                or signal.get("target_name") != universe_row.get("company_name")
                for signal in event_signals
            )
            or signal_source_refs != tuple(sorted(event.source_refs))
        ):
            raise ValueError("candidate-event current source lineage is invalid")
        event_by_target[target] = row
        event_object_by_target[target] = event

    planner_by_target: dict[str, Mapping[str, Any]] = {}
    for run in planners:
        target = str(run.get("target_id") or "")
        if not target or target in planner_by_target:
            raise ValueError("planner target identity is invalid or duplicated")
        planner_by_target[target] = run
    l3_targets = {
        target
        for target, row in depth_by_target.items()
        if row.get("maximum_depth") == "L3_RESEARCH_BRAIN"
        and row.get("selected_for_brain") is True
        and row.get("selected_for_deep") is True
        and row.get("selected_for_official_light") is True
        and row.get("as_of_date") == as_of_date
    }
    if set(planner_by_target) != l3_targets:
        raise ValueError("planner roster does not exactly bind current selected L3 targets")

    eligible_targets: set[str] = set()
    natural_complete_count = 0
    ineligible_abstained_count = 0
    pending_count = 0
    for target, run in planner_by_target.items():
        universe_row = universe_by_target[target]
        event = event_object_by_target.get(target)
        if event is None:
            raise ValueError("current L3 planner target lacks its candidate event")
        depth = depth_object_by_target[target]
        if (
            depth.maximum_depth != "L3_RESEARCH_BRAIN"
            or depth.selected_for_official_light is not True
            or depth.as_of_date != as_of_date
            or depth.target_name != universe_row.get("company_name")
            or depth.candidate_event_id != event.candidate_event_id
            or tuple(depth.trigger_signal_ids) != tuple(event.trigger_signal_ids)
            or event.as_of_date != as_of_date
            or event.target_id != target
            or event.target_name != universe_row.get("company_name")
            or event.investigation_required is not True
        ):
            raise ValueError("candidate event/depth/KRX current lineage is invalid")
        _planner_common_lineage(
            run,
            as_of_date=as_of_date,
            universe_row=universe_row,
            event=event,
            depth=depth,
        )
        terminal = str(run.get("terminal_status") or "")
        if terminal == "COMPLETE":
            _planner_projection(run)
            natural_complete_count += 1
            continue
        if terminal == "PENDING":
            if (
                run.get("real_provider_success") is not False
                or (run.get("plan") or {}).get("pending") is None
            ):
                raise ValueError("pending planner run has invalid provider/pending state")
            pending_count += 1
            continue
        if terminal != "ABSTAINED":
            raise ValueError("planner terminal status is outside the Phase-105 contract")
        if (
            run.get("provider_call_count") != 2
            or run.get("real_provider_success") is not True
            or (run.get("plan") or {}).get("pending") is not None
            or len(tuple((run.get("plan") or {}).get("provider_traces") or ())) != 2
        ):
            ineligible_abstained_count += 1
            continue
        projection = _planner_projection(run, allow_abstained=True)
        if projection.get("planner_terminal_status") != "ABSTAINED":
            raise ValueError("forced profile candidate is not an exact abstention")
        eligible_targets.add(target)

    # Preserve the authoritative KRX row order instead of sorting by a company,
    # sector, or archetype hint.  This makes budget truncation deterministic.
    selected_rows = tuple(
        row for row in universe if str(row.get("symbol") or "") in eligible_targets
    )
    if len(selected_rows) != len(eligible_targets):
        raise ValueError("forced profile candidate roster escaped the KRX universe")
    return CanonicalProfileInputs(
        universe_rows=selected_rows,
        forced_discovery_rows=tuple(universe),
        l3_target_count=len(l3_targets),
        natural_complete_count=natural_complete_count,
        eligible_abstained_count=len(selected_rows),
        ineligible_abstained_count=ineligible_abstained_count,
        pending_count=pending_count,
    )


def _atomic_write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink() or any(parent.is_symlink() for parent in path.parents):
        raise ValueError("canonical profile manifest path cannot traverse a symlink")
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    temporary = path.parent / f".{path.name}.{secrets.token_hex(12)}.tmp"
    descriptor = os.open(
        temporary,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o600,
    )
    try:
        offset = 0
        while offset < len(encoded):
            offset += os.write(descriptor, encoded[offset:])
        os.fsync(descriptor)
    except BaseException:
        os.close(descriptor)
        temporary.unlink(missing_ok=True)
        raise
    else:
        os.close(descriptor)
    try:
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        temporary.unlink(missing_ok=True)


def materialize_canonical_profile_manifest(
    *,
    repo_root: str | Path,
    config: IssuerBusinessProfileConfig,
    credential: str | None,
    fetcher: IssuerBusinessProfileFetcher,
    compatibility_provider: IssuerBusinessCompatibilityProvider,
    replace_current_seal: bool = False,
) -> tuple[Mapping[str, Any], Path, CanonicalProfileInputs]:
    root = Path(repo_root).resolve()
    live_root = root / "output" / "live_materialization" / config.as_of_date
    inputs = load_canonical_profile_inputs(
        live_root,
        as_of_date=config.as_of_date,
    )
    result = V6IssuerBusinessProfileMaterializer().materialize(
        config,
        universe_rows=inputs.universe_rows,
        discovery_universe_rows=inputs.forced_discovery_rows,
        credential=credential,
        fetcher=fetcher,
        compatibility_provider=compatibility_provider,
    )
    validated = validate_forced_validation_profile_manifest(result)
    if validated["status"] == PROFILE_PASS:
        destination = root / CUTOVER_RELATIVE_ROOT / PROFILE_MANIFEST_NAME
        # This path is a tracked *current-state pointer*, not an immutable
        # historical receipt.  Replacement remains opt-in so an ordinary run
        # cannot silently overwrite a prior COMPLETE selection.
        publish_current_issuer_business_profile_manifest(
            destination,
            validated,
            replace_existing=replace_current_seal,
        )
    else:
        # Pending diagnostics remain mutable run output.  Only a COMPLETE,
        # self-contained profile may enter the immutable tracked cutover root.
        destination = live_root / PROFILE_MANIFEST_NAME
        _atomic_write_json(destination, validated)
    return validated, destination, inputs


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--max-profile-fetches", type=int, default=100)
    parser.add_argument("--max-list-pages", type=int, default=3)
    parser.add_argument("--request-timeout-seconds", type=float, default=30.0)
    parser.add_argument("--max-compatibility-prompt-chars", type=int, default=2_000_000)
    parser.add_argument("--max-discovery-fetches", type=int, default=3_000)
    parser.add_argument(
        "--max-forced-candidates-per-required-slot", type=int, default=10
    )
    parser.add_argument(
        "--replace-current-seal",
        action="store_true",
        help=(
            "explicitly replace the tracked current COMPLETE profile for the "
            "same as-of date after compare-and-swap validation"
        ),
    )
    return parser


def main() -> int:
    args = _parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    if repo_root != canonical_repository_root() or not _repository_identity_is_trusted(
        repo_root
    ):
        raise SystemExit("issuer profile materialization requires the trusted canonical repository")
    load_project_env(repo_root / ".env")
    credential = os.environ.get("OPENDART_API_KEY") or os.environ.get(
        "OPEN_DART_API_KEY"
    )
    live_root = repo_root / "output" / "live_materialization" / args.as_of_date
    result, destination, inputs = materialize_canonical_profile_manifest(
        repo_root=repo_root,
        config=IssuerBusinessProfileConfig(
            as_of_date=args.as_of_date,
            max_profile_fetches=args.max_profile_fetches,
            max_list_pages=args.max_list_pages,
            request_timeout_seconds=args.request_timeout_seconds,
            max_compatibility_prompt_chars=args.max_compatibility_prompt_chars,
            max_discovery_fetches=args.max_discovery_fetches,
            max_forced_candidates_per_required_slot=(
                args.max_forced_candidates_per_required_slot
            ),
            test_mode=False,
        ),
        credential=credential,
        fetcher=RequestsOpenDartIssuerBusinessProfileFetcher(),
        compatibility_provider=CollaborationIssuerBusinessCompatibilityProvider(
            journal_root=live_root / PROFILE_JOURNAL_DIRECTORY
        ),
        replace_current_seal=args.replace_current_seal,
    )
    print(
        json.dumps(
            {
                "status": result["status"],
                "manifest_path": str(destination),
                "manifest": result,
                "input_audit": {
                    "l3_target_count": inputs.l3_target_count,
                    "natural_complete_count": inputs.natural_complete_count,
                    "eligible_abstained_count": inputs.eligible_abstained_count,
                    "ineligible_abstained_count": inputs.ineligible_abstained_count,
                    "pending_count": inputs.pending_count,
                    "full_krx_discovery_count": len(inputs.forced_discovery_rows),
                },
                "forced_validation_authority": False,
                "score_or_stage_authority": False,
                "gold_authority": False,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result["status"] == PROFILE_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "CanonicalProfileInputs",
    "CUTOVER_RELATIVE_ROOT",
    "PROFILE_JOURNAL_DIRECTORY",
    "PROFILE_MANIFEST_NAME",
    "load_canonical_profile_inputs",
    "main",
    "materialize_canonical_profile_manifest",
]
