"""Pre-deep current canary selection for E2R v6 operational acceptance.

The selector consumes the immutable upstream KRX, trigger, depth, and planner
artifacts.  It never consumes a score, Stage, post-run result, or Gold row.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from collections import Counter
from datetime import date, timedelta
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile
from typing import Any

from e2r.production.metadata import stable_hash
from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.runtime.live_materialization.depth_selector import (
    LiveDepthDecision,
)
from e2r.research_brain.runtime.live_materialization.trigger_fusion import (
    CandidateEvent,
    TriggerSignal,
)
from e2r.research_brain.runtime.live_materialization.universe_materializer import (
    LiveUniverseRow,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)


SELECTION_SCHEMA = "e2r_v6_pre_deep_canary_selection_v1"
SELECTION_RECEIPT_SCHEMA = "e2r_v6_pre_deep_selection_receipt_v1"
SELECTION_PASS = "E2R_V6_CROSS_ARCHETYPE_CANARY_SELECTION_PASS"
SELECTION_FAIL = "E2R_V6_CROSS_ARCHETYPE_CANARY_SELECTION_FAIL"
SELECTION_SUMMARY_SCHEMA = "e2r_v6_cross_archetype_canary_summary_v1"
NATURAL_SELECTION = "NATURAL_TRIGGER_CANARY"
FORCED_SELECTION = "FORCED_VALIDATION_CANARY"
REQUIRED_ARCHETYPES = (
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C24_BIO_TRIAL_DATA_EVENT_RISK",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
)

_CANDIDATE_KEYS = frozenset(
    {
        "universe_row",
        "candidate_event",
        "depth_decision",
        "planner_run",
    }
)
_PLANNER_RUN_KEYS = frozenset(
    {
        "schema_version",
        "planner_run_id",
        "target_id",
        "target_name",
        "as_of_date",
        "depth_decision_id",
        "candidate_event_id",
        "trigger_signal_ids",
        "source_refs",
        "blind_input_id",
        "compiled_fact_count",
        "input_compilation_audit",
        "provider_name",
        "provider_real",
        "provider_fake",
        "provider_call_count",
        "real_provider_success",
        "terminal_status",
        "plan",
    }
)
_FORBIDDEN_DEEP_KEY_TOKENS = frozenset(
    {
        "score",
        "scores",
        "stage",
        "stages",
        "scorevalid",
        "finalscore",
        "canonicalstage",
        "componentscore",
        "stagecourt",
        "gold",
        "outcome",
        "return",
        "points",
        "ranking",
        "mfe",
        "mae",
    }
)
_SAFE_NEGATIVE_AUTHORITY_KEYS = frozenset(
    {
        "scoreevidenceeligible",
        "deterministicstageorscoremutation",
        "scorestagefieldforwardedcount",
        "scorestagefieldforwarded",
        "scoreorstageauthority",
    }
)
_SAFE_PRE_DEEP_NUMERIC_KEYS = frozenset({"priorityscore"})
_HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
_TARGET_RE = re.compile(r"^[0-9A-Z]{6}$")
_KRX_ENDPOINTS = {
    "KOSPI": "stk_isu_base_info",
    "KOSDAQ": "ksq_isu_base_info",
}
_KRX_BASE = "https://data-dbg.krx.co.kr/svc/apis/sto"
_PLANNER_PROVIDER_NAMES = frozenset({"codex_cli_two_pass_planner"})
_SELECTION_MANIFEST_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "selection_as_of_date",
        "required_archetypes",
        "selections",
        "selection_count",
        "critical_counts",
        "critical_count_sum",
        "failures",
        "score_or_stage_authority",
        "selection_roster_hash",
    }
)
_SELECTION_CRITICAL_KEYS = frozenset(
    {
        "required_archetype_missing_count",
        "invalid_candidate_lineage_count",
        "post_score_target_selection_count",
        "target_specific_code_branch_count",
        "forced_canary_mislabeled_natural_count",
        "duplicate_target_count",
    }
)
_SELECTION_RECEIPT_KEYS = frozenset(
    {
        "schema_version",
        "selection_id",
        "archetype_id",
        "target_id",
        "company_name",
        "selection_mode",
        "selection_as_of_date",
        "pre_deep_input_hash",
        "krx_effective_date",
        "krx_source_url",
        "krx_source_hash",
        "krx_request_id",
        "candidate_event_hash",
        "depth_decision_hash",
        "planner_run_id",
        "blind_input_id",
        "plan_hash",
        "issuer_profile_hash",
        "business_profile_hash",
        "direct_current_supporting_fact_ids",
        "recipe_ids",
        "trigger_event_ids",
        "available_source_families",
        "selection_rationale",
        "final_score_visible_at_selection",
        "final_stage_visible_at_selection",
        "production_daily_candidate",
        "score_or_stage_authority",
    }
)
_LIVE_SELECTION_INPUT_FILES = (
    "universe_eligible.jsonl",
    "universe_provenance.json",
    "universe_audit.json",
    "trigger_signals.jsonl",
    "candidate_events.jsonl",
    "trigger_fusion_audit.json",
    "depth_decisions.jsonl",
    "candidate_selection_audit.json",
    "planner_runs.jsonl",
    "llm_prompts.jsonl",
    "llm_responses.jsonl",
    "planner_validation.json",
)


def _normalized_key(value: object) -> str:
    return "".join(character for character in str(value).casefold() if character.isalnum())


def _deep_result_keys(value: object) -> tuple[str, ...]:
    found: set[str] = set()

    def visit(item: object) -> None:
        if isinstance(item, Mapping):
            for key, child in item.items():
                normalized = _normalized_key(key)
                safe_negative = (
                    normalized in _SAFE_NEGATIVE_AUTHORITY_KEYS
                    and (child is False or child == 0)
                )
                safe_pre_deep = normalized in _SAFE_PRE_DEEP_NUMERIC_KEYS and (
                    isinstance(child, (int, float)) and not isinstance(child, bool)
                )
                if not safe_negative and not safe_pre_deep and any(
                    token in normalized for token in _FORBIDDEN_DEEP_KEY_TOKENS
                ):
                    found.add(str(key))
                visit(child)
        elif isinstance(item, Sequence) and not isinstance(
            item, (str, bytes, bytearray)
        ):
            for child in item:
                visit(child)

    visit(value)
    return tuple(sorted(found))


def _strings(value: object) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return ()
    return tuple(sorted({str(item).strip() for item in value if str(item).strip()}))


def _mapping(value: object, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def _read_live_input_file(path: Path) -> bytes:
    """Read one immutable regular live-root leaf without following links."""

    if path.is_symlink():
        raise ValueError(f"live selection input symlink is forbidden: {path.name}")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise ValueError(f"live selection input is unavailable: {path.name}") from exc
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise ValueError(
                f"live selection input must be a single regular file: {path.name}"
            )
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        path_stat = path.stat(follow_symlinks=False)
        identity = (before.st_dev, before.st_ino, before.st_size)
        if identity != (after.st_dev, after.st_ino, after.st_size) or identity != (
            path_stat.st_dev,
            path_stat.st_ino,
            path_stat.st_size,
        ):
            raise ValueError(f"live selection input changed while read: {path.name}")
        return b"".join(chunks)
    finally:
        os.close(descriptor)


def _json_object(encoded: bytes, *, context: str) -> Mapping[str, Any]:
    try:
        payload = json.loads(encoded.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{context} is not valid JSON") from exc
    return _mapping(payload, context=context)


def _jsonl_objects(encoded: bytes, *, context: str) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    try:
        text = encoded.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{context} is not UTF-8 JSONL") from exc
    for line_number, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{context} line {line_number} is invalid JSON") from exc
        rows.append(_mapping(payload, context=f"{context} line {line_number}"))
    return tuple(rows)


def _accepted_live_audit(
    payload: Mapping[str, Any], *, as_of_date: str, context: str
) -> None:
    if (
        str(payload.get("as_of_date") or "") != as_of_date
        or payload.get("hard_acceptance_pass") is not True
        or isinstance(payload.get("critical_count_sum"), bool)
        or not isinstance(payload.get("critical_count_sum"), int)
        or int(payload.get("critical_count_sum") or 0) != 0
    ):
        raise ValueError(f"{context} is not an accepted current live audit")


def _validate_planner_call_receipts(
    *,
    planner_runs: Sequence[Mapping[str, Any]],
    prompt_rows: Sequence[Mapping[str, Any]],
    response_rows: Sequence[Mapping[str, Any]],
) -> None:
    prompts: dict[str, Mapping[str, Any]] = {}
    responses: dict[str, Mapping[str, Any]] = {}
    for label, rows, destination in (
        ("prompt", prompt_rows, prompts),
        ("response", response_rows, responses),
    ):
        for row in rows:
            call_id = str(row.get("call_id") or "")
            if not call_id or call_id in destination:
                raise ValueError(f"planner {label} call identities are not unique")
            destination[call_id] = row
    if set(prompts) != set(responses):
        raise ValueError("planner prompt/response call roster mismatch")
    for call_id, prompt in prompts.items():
        response = responses[call_id]
        expected_call_id = "LLMCALL-" + stable_hash(
            {
                "target": str(prompt.get("target_id") or ""),
                "attempt_id": str(prompt.get("attempt_id") or ""),
                "planner_pass": str(prompt.get("planner_pass") or ""),
                "prompt_hash": str(prompt.get("prompt_hash") or ""),
            }
        )[:24]
        if (
            call_id != expected_call_id
            or prompt.get("schema_version") != "e2r_live_llm_prompt_v1"
            or response.get("schema_version") != "e2r_live_llm_response_v1"
            or prompt.get("target_id") != response.get("target_id")
            or prompt.get("planner_pass") != response.get("planner_pass")
            or prompt.get("provider_name") != response.get("provider_name")
            or prompt.get("attempt_id") != response.get("attempt_id")
            or str(prompt.get("prompt_hash") or "")
            != hashlib.sha256(
                str(prompt.get("prompt_text") or "").encode("utf-8")
            ).hexdigest()
        ):
            raise ValueError("planner call receipt content does not recompute")
        raw_response = response.get("raw_response")
        if response.get("status") == "COMPLETED":
            try:
                decoded_response = json.loads(str(raw_response))
            except (TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError("planner response receipt is not exact JSON") from exc
            if (
                not isinstance(raw_response, str)
                or str(response.get("response_hash") or "")
                != hashlib.sha256(raw_response.encode("utf-8")).hexdigest()
                or decoded_response != response.get("response_payload")
            ):
                raise ValueError("planner response receipt hash does not recompute")

    run_by_target: dict[str, Mapping[str, Any]] = {}
    for run in planner_runs:
        target_id = str(run.get("target_id") or "")
        if not target_id or target_id in run_by_target:
            raise ValueError("planner run target roster is not unique")
        run_by_target[target_id] = run
    calls_by_target = Counter(
        str(prompt.get("target_id") or "") for prompt in prompts.values()
    )
    if set(calls_by_target) - set(run_by_target) or any(
        isinstance(run.get("provider_call_count"), bool)
        or not isinstance(run.get("provider_call_count"), int)
        or int(run.get("provider_call_count") or 0) < 0
        or calls_by_target.get(target_id, 0) != run.get("provider_call_count")
        or any(
            prompt.get("provider_name") != run.get("provider_name")
            for prompt in prompts.values()
            if str(prompt.get("target_id") or "") == target_id
        )
        for target_id, run in run_by_target.items()
    ):
        raise ValueError("planner call journal does not exactly bind the run roster")
    completed_run_by_target = {
        target_id: run
        for target_id, run in run_by_target.items()
        if run.get("terminal_status") == "COMPLETE"
    }
    for target_id, run in completed_run_by_target.items():
        target_call_ids = tuple(
            call_id
            for call_id, prompt in prompts.items()
            if str(prompt.get("target_id") or "") == target_id
        )
        if (
            len(target_call_ids) != 2
            or run.get("provider_call_count") != 2
            or Counter(
                str(prompts[call_id].get("planner_pass") or "")
                for call_id in target_call_ids
            )
            != Counter({"BLIND_HYPOTHESIS": 1, "MEMORY_CRITIQUE": 1})
            or any(
                responses[call_id].get("status") != "COMPLETED"
                for call_id in target_call_ids
            )
        ):
            raise ValueError(
                "completed planner target requires exactly its two successful calls"
            )

    calls_by_edge: dict[tuple[str, str, str, str, str], int] = {}
    for call_id, prompt in prompts.items():
        response = responses[call_id]
        if response.get("status") != "COMPLETED":
            continue
        edge = (
            str(prompt.get("target_id") or ""),
            str(prompt.get("planner_pass") or ""),
            str(prompt.get("provider_name") or ""),
            str(prompt.get("prompt_hash") or ""),
            str(response.get("response_hash") or ""),
        )
        calls_by_edge[edge] = calls_by_edge.get(edge, 0) + 1
    response_payload_by_edge: dict[
        tuple[str, str, str, str, str], Mapping[str, Any]
    ] = {}
    for call_id, prompt in prompts.items():
        response = responses[call_id]
        if response.get("status") != "COMPLETED":
            continue
        edge = (
            str(prompt.get("target_id") or ""),
            str(prompt.get("planner_pass") or ""),
            str(prompt.get("provider_name") or ""),
            str(prompt.get("prompt_hash") or ""),
            str(response.get("response_hash") or ""),
        )
        response_payload_by_edge[edge] = _mapping(
            response.get("response_payload"), context="planner response payload"
        )
    for run in planner_runs:
        traces = tuple((run.get("plan") or {}).get("provider_traces") or ())
        if run.get("terminal_status") == "COMPLETE" and (
            run.get("provider_call_count") != 2
            or len(traces) != 2
            or Counter(
                str(trace.get("planner_pass") or "")
                for trace in traces
                if isinstance(trace, Mapping)
            )
            != Counter({"BLIND_HYPOTHESIS": 1, "MEMORY_CRITIQUE": 1})
        ):
            raise ValueError(
                "completed planner run requires one exact call for each two-pass role"
            )
        for trace in traces:
            trace = _mapping(trace, context="planner provider trace")
            edge = (
                str(run.get("target_id") or ""),
                str(trace.get("planner_pass") or ""),
                str(trace.get("provider_name") or ""),
                str(trace.get("prompt_hash") or ""),
                str(trace.get("response_hash") or ""),
            )
            if calls_by_edge.get(edge) != 1:
                raise ValueError("planner trace lacks one exact prompt/response receipt")
            expected_output = (
                (run.get("plan") or {}).get("blind_output")
                if trace.get("planner_pass") == "BLIND_HYPOTHESIS"
                else (run.get("plan") or {}).get("critique_output")
                if trace.get("planner_pass") == "MEMORY_CRITIQUE"
                else None
            )
            if response_payload_by_edge.get(edge) != expected_output:
                raise ValueError("planner response payload does not bind the stored plan")
    trace_edges = Counter(
        (
            str(run.get("target_id") or ""),
            str(trace.get("planner_pass") or ""),
            str(trace.get("provider_name") or ""),
            str(trace.get("prompt_hash") or ""),
            str(trace.get("response_hash") or ""),
        )
        for run in planner_runs
        for trace in ((run.get("plan") or {}).get("provider_traces") or ())
        if isinstance(trace, Mapping)
    )
    if trace_edges != Counter(calls_by_edge):
        raise ValueError("planner trace and completed call roster are not exact-once")


def load_current_live_selection_inputs(
    live_root: str | Path,
    *,
    selection_as_of_date: str,
) -> tuple[tuple[Mapping[str, Any], ...], tuple[Mapping[str, Any], ...]]:
    """Load the selector input only from one audited current live root.

    The operational CLI uses this loader instead of accepting hand-authored
    candidate rows.  Pure mapping compilation remains available for unit tests.
    """

    selection_date = _iso_date(
        selection_as_of_date, context="selection as_of_date"
    )
    repo = canonical_repository_root()
    if not _repository_identity_is_trusted(repo):
        raise ValueError("live selection repository identity is not trusted")
    raw_root = Path(live_root)
    if raw_root.is_symlink():
        raise ValueError("live selection root symlink is forbidden")
    root = raw_root.resolve()
    expected_root = (repo / "output" / "live_materialization" / selection_date).resolve()
    if root != expected_root:
        raise ValueError("live selection root is not the canonical repository path")
    if not root.is_dir():
        raise ValueError("live selection root is unavailable")
    encoded = {
        name: _read_live_input_file(root / name) for name in _LIVE_SELECTION_INPUT_FILES
    }
    universe_rows = _jsonl_objects(
        encoded["universe_eligible.jsonl"], context="eligible KRX universe"
    )
    provenance = _json_object(
        encoded["universe_provenance.json"], context="KRX universe provenance"
    )
    universe_audit = _json_object(
        encoded["universe_audit.json"], context="KRX universe audit"
    )
    signals = _jsonl_objects(
        encoded["trigger_signals.jsonl"], context="trigger signals"
    )
    events = _jsonl_objects(
        encoded["candidate_events.jsonl"], context="candidate events"
    )
    trigger_audit = _json_object(
        encoded["trigger_fusion_audit.json"], context="trigger fusion audit"
    )
    depths = _jsonl_objects(
        encoded["depth_decisions.jsonl"], context="depth decisions"
    )
    depth_audit = _json_object(
        encoded["candidate_selection_audit.json"], context="depth selection audit"
    )
    planner_runs = _jsonl_objects(
        encoded["planner_runs.jsonl"], context="planner runs"
    )
    prompts = _jsonl_objects(encoded["llm_prompts.jsonl"], context="planner prompts")
    responses = _jsonl_objects(
        encoded["llm_responses.jsonl"], context="planner responses"
    )
    planner_audit = _json_object(
        encoded["planner_validation.json"], context="planner validation"
    )
    for audit, context in (
        (universe_audit, "KRX universe audit"),
        (trigger_audit, "trigger fusion audit"),
        (depth_audit, "depth selection audit"),
        (planner_audit, "planner validation"),
    ):
        _accepted_live_audit(audit, as_of_date=selection_date, context=context)
    attempts = tuple(provenance.get("request_attempts") or ())
    attempt_by_edge: dict[tuple[str, str], Mapping[str, Any]] = {}
    for raw_attempt in attempts:
        attempt = _mapping(raw_attempt, context="KRX provenance request attempt")
        edge = (
            str(attempt.get("market") or ""),
            str(attempt.get("effective_date") or ""),
        )
        if not all(edge) or edge in attempt_by_edge:
            raise ValueError("KRX provenance request attempts are not unique")
        attempt_by_edge[edge] = attempt
    if (
        provenance.get("schema_version")
        != "e2r_live_krx_universe_provenance_v1"
        or provenance.get("status") != "CURRENT_UNIVERSE_MATERIALIZATION_PASS"
        or str(provenance.get("as_of_date") or "") != selection_date
        or provenance.get("eligible_universe_hash")
        != stable_hash([dict(row) for row in universe_rows])
        or int(universe_audit.get("eligible_universe_count") or -1)
        != len(universe_rows)
        or len(universe_rows) < 1000
        or int(universe_audit.get("provider_request_count") or -1) != len(attempts)
        or int(trigger_audit.get("trigger_signal_count") or -1) != len(signals)
        or int(trigger_audit.get("candidate_event_count") or -1) != len(events)
        or int(depth_audit.get("depth_decision_count") or -1) != len(depths)
        or int(planner_audit.get("planner_run_count") or -1) != len(planner_runs)
        or int(planner_audit.get("planner_call_count") or -1) != len(responses)
    ):
        raise ValueError("live selection audit roster or provenance mismatch")
    for row in universe_rows:
        member = _universe_row(row, selection_date=selection_date)
        attempt = attempt_by_edge.get((member.market, member.source_effective_date))
        if (
            attempt is None
            or attempt.get("status") != "FETCHED"
            or str(attempt.get("canonical_url") or "").split("?", 1)[0]
            != member.source_url
            or str(attempt.get("request_id") or "") != member.source_request_id
            or str(attempt.get("content_hash") or "") != member.source_content_hash
        ):
            raise ValueError("eligible KRX row lacks exact fetched request provenance")
    signals = _validated_trigger_rows(
        signals,
        selection_date=selection_date,
        include_inactive=True,
    )
    _validate_planner_call_receipts(
        planner_runs=planner_runs,
        prompt_rows=prompts,
        response_rows=responses,
    )

    universe_by_target = {str(row.get("symbol") or ""): row for row in universe_rows}
    event_by_target = {str(row.get("target_id") or ""): row for row in events}
    depth_by_target = {str(row.get("target_id") or ""): row for row in depths}
    if (
        "" in universe_by_target
        or len(universe_by_target) != len(universe_rows)
        or "" in event_by_target
        or len(event_by_target) != len(events)
        or "" in depth_by_target
        or len(depth_by_target) != len(depths)
    ):
        raise ValueError("live selection upstream target identities are not unique")
    candidates: list[Mapping[str, Any]] = []
    for run in planner_runs:
        if run.get("terminal_status") != "COMPLETE":
            continue
        target_id = str(run.get("target_id") or "")
        universe = universe_by_target.get(target_id)
        event = event_by_target.get(target_id)
        depth = depth_by_target.get(target_id)
        if universe is None or event is None or depth is None:
            raise ValueError("completed planner run lacks KRX/trigger/depth lineage")
        candidates.append(
            {
                "universe_row": universe,
                "candidate_event": event,
                "depth_decision": depth,
                "planner_run": run,
            }
        )
    return tuple(candidates), tuple(signals)


def _iso_date(value: object, *, context: str) -> str:
    text = str(value or "")
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError as exc:
        raise ValueError(f"{context} must be an ISO date") from exc


def _universe_row(raw: object, *, selection_date: str) -> LiveUniverseRow:
    row = dict(_mapping(raw, context="universe row"))
    for key in ("raw_fields",):
        row[key] = dict(_mapping(row.get(key), context=f"universe row {key}"))
    member = LiveUniverseRow(**row)
    if (
        not member.eligible
        or member.exclusion_reason is not None
        or member.listing_status != "LISTED"
        or member.source_mode != "LIVE"
        or not member.symbol
        or not _TARGET_RE.fullmatch(member.symbol)
        or member.market not in _KRX_ENDPOINTS
        or member.source_effective_date > selection_date
        or date.fromisoformat(member.source_effective_date)
        < date.fromisoformat(selection_date) - timedelta(days=7)
    ):
        raise ValueError("candidate is not an eligible current live KRX common equity")
    endpoint = _KRX_ENDPOINTS[member.market]
    expected_url = f"{_KRX_BASE}/{endpoint}"
    expected_request = "KRXREQ-" + stable_hash(
        {
            "market": member.market,
            "effective_date": member.source_effective_date,
            "endpoint": endpoint,
        }
    )[:24]
    if member.source_url != expected_url or member.source_request_id != expected_request:
        raise ValueError("KRX source URL/request identity does not recompute")
    return member


def _candidate_event(raw: object) -> CandidateEvent:
    row = dict(_mapping(raw, context="candidate event"))
    for key in ("trigger_types", "trigger_signal_ids", "source_refs"):
        row[key] = tuple(row.get(key) or ())
    event = CandidateEvent(**row)
    expected_id = "CAND-" + stable_hash(
        {
            "target": event.target_id,
            "as_of_date": event.as_of_date,
            "signals": tuple(event.trigger_signal_ids),
        }
    )[:24]
    if event.candidate_event_id != expected_id:
        raise ValueError("candidate event identity does not recompute")
    return event


def _depth_decision(raw: object) -> LiveDepthDecision:
    row = dict(_mapping(raw, context="depth decision"))
    for key in ("completed_depths", "trigger_signal_ids", "selection_reasons"):
        row[key] = tuple(row.get(key) or ())
    for key in ("source_task_budget", "llm_budget", "general_web_budget"):
        row[key] = dict(_mapping(row.get(key), context=f"depth decision {key}"))
    decision = LiveDepthDecision(**row)
    expected_id = "DEPTH-" + stable_hash(
        {
            "target": decision.target_id,
            "as_of_date": decision.as_of_date,
            "maximum": decision.maximum_depth,
            "candidate": decision.candidate_event_id,
        }
    )[:24]
    if decision.depth_decision_id != expected_id:
        raise ValueError("depth decision identity does not recompute")
    if (
        not decision.selected_for_deep
        or not decision.selected_for_brain
        or not decision.acquisition_eligible
    ):
        raise ValueError("canary selection requires an acquisition-eligible L3 plan")
    return decision


def _planner_projection(raw: object) -> Mapping[str, Any]:
    run = _mapping(raw, context="planner run")
    if set(run) != _PLANNER_RUN_KEYS:
        raise ValueError("planner run schema keys are not exact")
    plan = _mapping(run.get("plan"), context="planner plan")
    critique = _mapping(plan.get("critique_output"), context="planner critique")
    top = tuple(critique.get("top_k_archetypes") or ())
    if not top or not isinstance(top[0], Mapping):
        raise ValueError("planner critique requires a leading archetype")
    leading = str(top[0].get("archetype_id") or "")
    blind_input_id = str(run.get("blind_input_id") or "")
    expected_plan_id = stable_intelligence_id(
        "two-pass-plan", {"blind_input_id": blind_input_id}
    )
    traces = tuple(plan.get("provider_traces") or ())
    trace_passes = Counter(
        str(trace.get("planner_pass") or "")
        for trace in traces
        if isinstance(trace, Mapping)
    )
    if (
        run.get("schema_version") != "e2r_live_planner_run_v1"
        or run.get("terminal_status") != "COMPLETE"
        or run.get("provider_real") is not True
        or run.get("provider_fake") is not False
        or run.get("real_provider_success") is not True
        or isinstance(run.get("provider_call_count"), bool)
        or not isinstance(run.get("provider_call_count"), int)
        or int(run.get("provider_call_count") or 0) != 2
        or str(run.get("provider_name") or "") not in _PLANNER_PROVIDER_NAMES
        or len(traces) != int(run.get("provider_call_count") or 0)
        or trace_passes != Counter(
            {"BLIND_HYPOTHESIS": 1, "MEMORY_CRITIQUE": 1}
        )
        or any(
            not isinstance(trace, Mapping)
            or trace.get("provider_name") != run.get("provider_name")
            or trace.get("real_provider") is not True
            or trace.get("fake_provider") is not False
            or _HEX64_RE.fullmatch(str(trace.get("prompt_hash") or "")) is None
            or _HEX64_RE.fullmatch(str(trace.get("response_hash") or "")) is None
            for trace in traces
        )
        or plan.get("plan_id") != expected_plan_id
        or plan.get("blind_input_id") != blind_input_id
        or plan.get("status") != "COMPLETE"
        or plan.get("pending") is not None
        or plan.get("deterministic_stage_or_score_mutation") is not False
        or not isinstance(plan.get("blind_output"), Mapping)
        or critique.get("abstain") is not False
    ):
        raise ValueError("planner run is not a current real completed blind plan")
    target_id = str(run.get("target_id") or "")
    expected_run_id = "LIVEPLAN-" + stable_hash(
        {
            "target": target_id,
            "blind_input": blind_input_id,
            "plan": expected_plan_id,
        }
    )[:24]
    if run.get("planner_run_id") != expected_run_id:
        raise ValueError("planner run identity does not recompute")
    drafts = tuple(critique.get("source_task_drafts") or ())
    supporting = _strings(critique.get("supporting_current_fact_ids"))
    recipes = _strings(
        [
            item
            for draft in drafts
            if isinstance(draft, Mapping)
            for item in (draft.get("recipe_id"),)
            if item
        ]
    )
    sources = _strings(
        [
            family
            for draft in drafts
            if isinstance(draft, Mapping)
            for field in ("preferred_source_families", "fallback_source_families")
            for family in (draft.get(field) or ())
        ]
    )
    if not supporting or not recipes or not sources:
        raise ValueError("planner run lacks current support, recipes, or source lanes")
    return {
        "planner_run_id": expected_run_id,
        "target_id": target_id,
        "target_name": str(run.get("target_name") or ""),
        "as_of_date": str(run.get("as_of_date") or ""),
        "depth_decision_id": str(run.get("depth_decision_id") or ""),
        "candidate_event_id": str(run.get("candidate_event_id") or ""),
        "trigger_signal_ids": list(_strings(run.get("trigger_signal_ids"))),
        "source_refs": list(_strings(run.get("source_refs"))),
        "blind_input_id": blind_input_id,
        "plan_hash": stable_hash(plan),
        "leading_archetype_id": leading,
        "direct_current_supporting_fact_ids": list(supporting),
        "recipe_ids": list(recipes),
        "available_source_families": list(sources),
    }


def _candidate_projection(
    row: Mapping[str, Any], *, selection_date: str
) -> Mapping[str, Any]:
    if set(row) != _CANDIDATE_KEYS:
        raise ValueError("candidate schema keys are not exact")
    universe = _universe_row(row.get("universe_row"), selection_date=selection_date)
    event = _candidate_event(row.get("candidate_event"))
    depth = _depth_decision(row.get("depth_decision"))
    planner = _planner_projection(row.get("planner_run"))
    target = str(universe.symbol or "")
    if (
        event.target_id != target
        or depth.target_id != target
        or planner["target_id"] != target
        or event.target_name != universe.company_name
        or depth.target_name != universe.company_name
        or planner["target_name"] != universe.company_name
        or event.as_of_date != selection_date
        or depth.as_of_date != selection_date
        or planner["as_of_date"] != selection_date
        or event.investigation_required is not True
        or depth.candidate_event_id != event.candidate_event_id
        or planner["candidate_event_id"] != event.candidate_event_id
        or planner["depth_decision_id"] != depth.depth_decision_id
        or tuple(planner["trigger_signal_ids"])
        != tuple(sorted(event.trigger_signal_ids))
        or tuple(planner["source_refs"]) != tuple(sorted(event.source_refs))
        or tuple(depth.trigger_signal_ids) != tuple(event.trigger_signal_ids)
    ):
        raise ValueError("candidate KRX/trigger/depth/planner lineage mismatch")
    return {
        **planner,
        "target_id": target,
        "company_name": str(universe.company_name or ""),
        "market": universe.market,
        "krx_effective_date": universe.source_effective_date,
        "krx_source_url": universe.source_url,
        "krx_source_hash": universe.source_content_hash,
        "krx_request_id": universe.source_request_id,
        "candidate_event_hash": stable_hash(event.to_dict()),
        "event_latest_effective_date": event.latest_effective_date,
        "event_trigger_types": list(event.trigger_types),
        "event_trigger_signal_ids": list(event.trigger_signal_ids),
        "event_source_refs": list(event.source_refs),
        "event_summary": event.summary,
        "depth_decision_hash": stable_hash(depth.to_dict()),
        "issuer_profile_hash": stable_hash(
            {
                "target_id": target,
                "company_name": universe.company_name,
                "market": universe.market,
                "security_group": universe.security_group,
                "stock_certificate_type": universe.stock_certificate_type,
                "sector_type": universe.sector_type,
            }
        ),
        "business_profile_hash": stable_hash(
            {
                "target_id": target,
                "leading_archetype_id": planner["leading_archetype_id"],
                "direct_current_supporting_fact_ids": planner[
                    "direct_current_supporting_fact_ids"
                ],
                "recipe_ids": planner["recipe_ids"],
                "available_source_families": planner[
                    "available_source_families"
                ],
            }
        ),
    }


def _validated_trigger_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    selection_date: str,
    include_inactive: bool = False,
) -> tuple[Mapping[str, Any], ...]:
    validated: list[Mapping[str, Any]] = []
    for raw in rows:
        row = dict(raw)
        for key in ("source_refs", "provider_names"):
            row[key] = tuple(row.get(key) or ())
        row["payload"] = dict(_mapping(row.get("payload"), context="trigger payload"))
        signal = TriggerSignal(**row)
        expected_signal_id = "TRIG-" + stable_hash(
            {
                "target": signal.target_id,
                "source_event": signal.source_event_id,
                "effective_date": signal.effective_date,
                "trigger_type": signal.trigger_type,
                "lifecycle_status": signal.lifecycle_status,
                "providers": tuple(signal.provider_names),
                "payload": dict(signal.payload),
            }
        )[:24]
        if signal.trigger_signal_id != expected_signal_id:
            raise ValueError("trigger signal identity does not recompute")
        if signal.effective_date > selection_date or signal.detected_at > selection_date:
            raise ValueError("future trigger signal is forbidden")
        if signal.score_evidence_eligible or signal.lifecycle_status not in {
            "CURRENT",
            "OPEN",
        }:
            continue
        if not include_inactive and not signal.investigation_required:
            continue
        validated.append(signal.to_dict())
    return tuple(validated)


def compile_cross_archetype_canary_selection(
    *,
    selection_as_of_date: str,
    candidates: Sequence[Mapping[str, Any]],
    trigger_events: Sequence[Mapping[str, Any]],
    required_archetypes: Sequence[str] = REQUIRED_ARCHETYPES,
) -> Mapping[str, Any]:
    """Select one unique current issuer per required archetype pre-deep."""

    failures: list[Mapping[str, Any]] = []
    try:
        selection_date = _iso_date(selection_as_of_date, context="selection as_of_date")
    except ValueError as exc:
        selection_date = str(selection_as_of_date or "")
        failures.append({"code": "INVALID_SELECTION_AS_OF_DATE", "detail": str(exc)})
    if tuple(required_archetypes) != REQUIRED_ARCHETYPES:
        failures.append(
            {
                "code": "REQUIRED_ARCHETYPE_CONTRACT_MISMATCH",
                "detail": list(required_archetypes),
            }
        )
    forbidden_keys = _deep_result_keys((candidates, trigger_events))
    if forbidden_keys:
        failures.append(
            {
                "code": "POST_DEEP_SCORE_OR_STAGE_VISIBLE_AT_SELECTION",
                "detail": list(forbidden_keys),
            }
        )

    projected: list[Mapping[str, Any]] = []
    for index, row in enumerate(candidates):
        try:
            projected.append(_candidate_projection(row, selection_date=selection_date))
        except (TypeError, ValueError) as exc:
            failures.append(
                {
                    "code": "INVALID_PRE_DEEP_CANDIDATE_LINEAGE",
                    "detail": {"index": index, "reason": str(exc)},
                }
            )
    projected_candidates = tuple(projected)
    duplicate_target_count = len(projected_candidates) - len(
        {row["target_id"] for row in projected_candidates}
    )
    if duplicate_target_count:
        failures.append(
            {"code": "DUPLICATE_PRE_DEEP_TARGET", "detail": duplicate_target_count}
        )
    try:
        all_signals = _validated_trigger_rows(
            trigger_events,
            selection_date=selection_date,
            include_inactive=True,
        )
        signals = tuple(
            row for row in all_signals if row.get("investigation_required") is True
        )
    except (TypeError, ValueError) as exc:
        all_signals = ()
        signals = ()
        failures.append({"code": "INVALID_TRIGGER_LINEAGE", "detail": str(exc)})
    signal_by_id = {str(row["trigger_signal_id"]): row for row in signals}
    if len(signal_by_id) != len(signals):
        failures.append({"code": "DUPLICATE_TRIGGER_SIGNAL_ID", "detail": None})
    all_signal_by_id = {
        str(row.get("trigger_signal_id") or ""): row for row in all_signals
    }
    if "" in all_signal_by_id or len(all_signal_by_id) != len(all_signals):
        failures.append({"code": "INVALID_TRIGGER_ROSTER", "detail": None})
    signals_by_target: dict[str, list[Mapping[str, Any]]] = {}
    for signal in all_signals:
        signals_by_target.setdefault(str(signal.get("target_id") or ""), []).append(
            signal
        )
    lineage_valid_candidates: list[Mapping[str, Any]] = []
    for row in projected_candidates:
        referenced = tuple(str(value) for value in row["event_trigger_signal_ids"])
        ordered_target_signals = tuple(
            sorted(
                signals_by_target.get(str(row["target_id"]), ()),
                key=lambda item: (
                    str(item.get("effective_date") or ""),
                    str(item.get("trigger_signal_id") or ""),
                ),
            )
        )
        expected_ids = tuple(
            str(signal.get("trigger_signal_id") or "")
            for signal in ordered_target_signals
        )
        expected_types = tuple(
            sorted(
                {
                    str(signal.get("trigger_type") or "")
                    for signal in ordered_target_signals
                }
            )
        )
        expected_sources = tuple(
            dict.fromkeys(
                str(source)
                for signal in ordered_target_signals
                for source in (signal.get("source_refs") or ())
            )
        )
        expected_latest = max(
            (str(signal.get("effective_date") or "") for signal in ordered_target_signals),
            default="",
        )
        expected_summary = (
            f"{row['company_name']}: {', '.join(expected_types)} current trigger "
            f"{len(ordered_target_signals)}건 검증 필요"
        )
        missing = tuple(value for value in referenced if value not in all_signal_by_id)
        wrong_target = tuple(
            value
            for value in referenced
            if value in all_signal_by_id
            and str(all_signal_by_id[value].get("target_id") or "")
            != row["target_id"]
        )
        wrong_source = tuple(
            value
            for value in referenced
            if value in all_signal_by_id
            and not set(all_signal_by_id[value].get("source_refs") or ())
            <= set(row["source_refs"])
        )
        aggregate_mismatch = (
            not ordered_target_signals
            or referenced != expected_ids
            or tuple(row["event_trigger_types"]) != expected_types
            or tuple(row["event_source_refs"]) != expected_sources
            or str(row["event_latest_effective_date"]) != expected_latest
            or str(row["event_summary"]) != expected_summary
            or any(
                str(signal.get("target_name") or "") != row["company_name"]
                for signal in ordered_target_signals
            )
        )
        if missing or wrong_target or wrong_source or aggregate_mismatch:
            failures.append(
                {
                    "code": "CANDIDATE_TRIGGER_ROSTER_MISMATCH",
                    "detail": {
                        "target_id": row["target_id"],
                        "missing": list(missing),
                        "wrong_target": list(wrong_target),
                        "wrong_source": list(wrong_source),
                        "aggregate_mismatch": aggregate_mismatch,
                    },
                }
            )
            continue
        lineage_valid_candidates.append(row)
    projected_candidates = tuple(lineage_valid_candidates)

    used_targets: set[str] = set()
    receipts: list[Mapping[str, Any]] = []
    for archetype_id in REQUIRED_ARCHETYPES:
        eligible = tuple(
            row
            for row in projected_candidates
            if row["leading_archetype_id"] == archetype_id
            and row["target_id"] not in used_targets
        )
        ranked: list[
            tuple[int, int, int, str, Mapping[str, Any], tuple[Mapping[str, Any], ...]]
        ] = []
        for row in eligible:
            matching = tuple(
                signal_by_id[signal_id]
                for signal_id in row["trigger_signal_ids"]
                if signal_id in signal_by_id
                and signal_by_id[signal_id]["target_id"] == row["target_id"]
                and set(signal_by_id[signal_id]["source_refs"])
                <= set(row["source_refs"])
            )
            ranked.append(
                (
                    0 if matching else 1,
                    -len(matching),
                    -len(row["available_source_families"]),
                    str(row["target_id"]),
                    row,
                    matching,
                )
            )
        if not ranked:
            failures.append(
                {
                    "code": "REQUIRED_ARCHETYPE_HAS_NO_PRE_DEEP_CANARY",
                    "detail": archetype_id,
                }
            )
            continue
        _, _, _, _, selected, matching = min(ranked, key=lambda item: item[:4])
        used_targets.add(str(selected["target_id"]))
        pre_deep_payload = {
            "selection_as_of_date": selection_date,
            "archetype_id": archetype_id,
            "candidate": selected,
            "trigger_signal_ids": [row["trigger_signal_id"] for row in matching],
        }
        pre_deep_hash = stable_hash(pre_deep_payload)
        selection_mode = NATURAL_SELECTION if matching else FORCED_SELECTION
        receipts.append(
            {
                "schema_version": SELECTION_RECEIPT_SCHEMA,
                "selection_id": "SELREC-" + pre_deep_hash[:24],
                "archetype_id": archetype_id,
                "target_id": selected["target_id"],
                "company_name": selected["company_name"],
                "selection_mode": selection_mode,
                "selection_as_of_date": selection_date,
                "pre_deep_input_hash": pre_deep_hash,
                "krx_effective_date": selected["krx_effective_date"],
                "krx_source_url": selected["krx_source_url"],
                "krx_source_hash": selected["krx_source_hash"],
                "krx_request_id": selected["krx_request_id"],
                "candidate_event_hash": selected["candidate_event_hash"],
                "depth_decision_hash": selected["depth_decision_hash"],
                "planner_run_id": selected["planner_run_id"],
                "blind_input_id": selected["blind_input_id"],
                "plan_hash": selected["plan_hash"],
                "issuer_profile_hash": selected["issuer_profile_hash"],
                "business_profile_hash": selected["business_profile_hash"],
                "direct_current_supporting_fact_ids": list(
                    selected["direct_current_supporting_fact_ids"]
                ),
                "recipe_ids": list(selected["recipe_ids"]),
                "trigger_event_ids": [row["trigger_signal_id"] for row in matching],
                "available_source_families": list(
                    selected["available_source_families"]
                ),
                "selection_rationale": (
                    "current source-backed trigger lineage matches the current blind plan"
                    if matching
                    else "forced validation canary from a current KRX issuer and completed blind plan"
                ),
                "final_score_visible_at_selection": False,
                "final_stage_visible_at_selection": False,
                "production_daily_candidate": selection_mode == NATURAL_SELECTION,
                "score_or_stage_authority": False,
            }
        )

    roster = tuple(row["archetype_id"] for row in receipts)
    if roster != REQUIRED_ARCHETYPES:
        failures.append(
            {"code": "REQUIRED_ARCHETYPE_SELECTION_ROSTER_MISMATCH", "detail": list(roster)}
        )
    if len({row["target_id"] for row in receipts}) != len(receipts):
        failures.append({"code": "CROSS_ARCHETYPE_TARGET_REUSE", "detail": None})

    critical_counts = {
        "required_archetype_missing_count": len(REQUIRED_ARCHETYPES)
        - len(set(roster)),
        "invalid_candidate_lineage_count": sum(
            row["code"] == "INVALID_PRE_DEEP_CANDIDATE_LINEAGE" for row in failures
        ),
        "post_score_target_selection_count": int(bool(forbidden_keys)),
        # Selection is driven only by the supplied current upstream roster;
        # this compiler has no symbol/company allowlist or branch table.
        "target_specific_code_branch_count": 0,
        "forced_canary_mislabeled_natural_count": sum(
            row["selection_mode"] == NATURAL_SELECTION and not row["trigger_event_ids"]
            for row in receipts
        ),
        "duplicate_target_count": len(receipts)
        - len({row["target_id"] for row in receipts}),
    }
    critical_count_sum = max(len(failures), sum(critical_counts.values()))
    result = {
        "schema_version": SELECTION_SCHEMA,
        "status": SELECTION_PASS if critical_count_sum == 0 else SELECTION_FAIL,
        "selection_as_of_date": selection_date,
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "selections": receipts,
        "selection_count": len(receipts),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_count_sum,
        "failures": failures,
        "score_or_stage_authority": False,
    }
    return {**result, "selection_roster_hash": stable_hash(result["selections"])}


def summarize_cross_archetype_canary_selection(
    payload: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project the compact tracked Phase-105 acceptance summary."""

    if (
        payload.get("schema_version") != SELECTION_SCHEMA
        or payload.get("status") != SELECTION_PASS
        or int(payload.get("critical_count_sum") or 0) != 0
        or tuple(payload.get("required_archetypes") or ()) != REQUIRED_ARCHETYPES
    ):
        raise ValueError("cannot summarize a failed or noncanonical selection")
    receipts = tuple(payload.get("selections") or ())
    summary = {
        "schema_version": SELECTION_SUMMARY_SCHEMA,
        "status": SELECTION_PASS,
        "selection_as_of_date": str(payload.get("selection_as_of_date") or ""),
        "required_archetype_count": len(REQUIRED_ARCHETYPES),
        "selected_archetype_count": len(receipts),
        "natural_canary_count": sum(
            row.get("selection_mode") == NATURAL_SELECTION for row in receipts
        ),
        "forced_validation_canary_count": sum(
            row.get("selection_mode") == FORCED_SELECTION for row in receipts
        ),
        "target_ids": sorted(str(row.get("target_id") or "") for row in receipts),
        "selection_ids": [str(row.get("selection_id") or "") for row in receipts],
        "selection_roster_hash": str(payload.get("selection_roster_hash") or ""),
        "post_score_target_selection_count": int(
            (payload.get("critical_counts") or {}).get(
                "post_score_target_selection_count", -1
            )
        ),
        "target_specific_code_branch_count": int(
            (payload.get("critical_counts") or {}).get(
                "target_specific_code_branch_count", -1
            )
        ),
        "forced_canary_mislabeled_natural_count": int(
            (payload.get("critical_counts") or {}).get(
                "forced_canary_mislabeled_natural_count", -1
            )
        ),
        "score_or_stage_authority": False,
    }
    return {**summary, "summary_id": "SELSUM-" + stable_hash(summary)[:24]}


def _assert_no_symlink_ancestor(path: Path) -> None:
    current = path
    while True:
        # ``Path.exists()`` follows a symlink and is false for a dangling
        # target.  Inspect the directory entry itself so a broken link cannot
        # later become a valid seal destination when its target appears.
        if current.is_symlink():
            raise ValueError("selection seal symlink is forbidden")
        if current.parent == current:
            return
        current = current.parent


def _validate_selection_manifest_shape(payload: Mapping[str, Any]) -> None:
    critical = payload.get("critical_counts")
    receipts = tuple(payload.get("selections") or ())
    if (
        set(payload) != _SELECTION_MANIFEST_KEYS
        or payload.get("schema_version") != SELECTION_SCHEMA
        or payload.get("status") != SELECTION_PASS
        or tuple(payload.get("required_archetypes") or ()) != REQUIRED_ARCHETYPES
        or payload.get("failures") != []
        or payload.get("score_or_stage_authority") is not False
        or int(payload.get("selection_count") or -1) != len(REQUIRED_ARCHETYPES)
        or isinstance(payload.get("critical_count_sum"), bool)
        or not isinstance(payload.get("critical_count_sum"), int)
        or payload.get("critical_count_sum") != 0
        or not isinstance(critical, Mapping)
        or set(critical) != _SELECTION_CRITICAL_KEYS
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value != 0
            for value in critical.values()
        )
        or len(receipts) != len(REQUIRED_ARCHETYPES)
        or payload.get("selection_roster_hash") != stable_hash(list(receipts))
    ):
        raise ValueError("selection manifest is not the exact accepted five-target roster")
    targets: list[str] = []
    for expected_archetype, receipt in zip(REQUIRED_ARCHETYPES, receipts):
        receipt = _mapping(receipt, context="selection receipt")
        target = str(receipt.get("target_id") or "")
        company = str(receipt.get("company_name") or "")
        pre_deep_hash = str(receipt.get("pre_deep_input_hash") or "")
        hash_fields = (
            "krx_source_hash",
            "candidate_event_hash",
            "depth_decision_hash",
            "plan_hash",
            "issuer_profile_hash",
            "business_profile_hash",
        )
        mode = receipt.get("selection_mode")
        trigger_ids = tuple(receipt.get("trigger_event_ids") or ())
        if (
            set(receipt) != _SELECTION_RECEIPT_KEYS
            or receipt.get("schema_version") != SELECTION_RECEIPT_SCHEMA
            or receipt.get("archetype_id") != expected_archetype
            or target != target.strip()
            or _TARGET_RE.fullmatch(target) is None
            or company != company.strip()
            or not company
            or _HEX64_RE.fullmatch(pre_deep_hash) is None
            or receipt.get("selection_id") != "SELREC-" + pre_deep_hash[:24]
            or receipt.get("selection_as_of_date")
            != payload.get("selection_as_of_date")
            or mode not in {NATURAL_SELECTION, FORCED_SELECTION}
            or (mode == NATURAL_SELECTION and not trigger_ids)
            or receipt.get("production_daily_candidate")
            is not (mode == NATURAL_SELECTION)
            or receipt.get("final_score_visible_at_selection") is not False
            or receipt.get("final_stage_visible_at_selection") is not False
            or receipt.get("score_or_stage_authority") is not False
            or any(
                _HEX64_RE.fullmatch(str(receipt.get(field) or "")) is None
                for field in hash_fields
            )
            or not tuple(receipt.get("direct_current_supporting_fact_ids") or ())
            or not tuple(receipt.get("recipe_ids") or ())
            or not tuple(receipt.get("available_source_families") or ())
        ):
            raise ValueError("selection receipt identity or blind lineage is invalid")
        targets.append(target)
    if len(targets) != len(set(targets)):
        raise ValueError("selection target roster is not canonical and unique")


def _read_regular_no_follow(path: Path) -> bytes:
    if path.is_symlink():
        raise ValueError("selection seal symlink is forbidden")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise ValueError("selection seal must be a private regular file") from exc
    try:
        metadata = os.fstat(descriptor)
        if (
            not stat.S_ISREG(metadata.st_mode)
            or metadata.st_nlink != 1
            or metadata.st_mode & 0o022
        ):
            raise ValueError("selection seal must be a private regular file")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        encoded = b"".join(chunks)
        final_metadata = os.fstat(descriptor)
        path_metadata = path.stat(follow_symlinks=False)
        identity = (metadata.st_dev, metadata.st_ino, metadata.st_uid, metadata.st_gid)
        if (
            identity
            != (
                final_metadata.st_dev,
                final_metadata.st_ino,
                final_metadata.st_uid,
                final_metadata.st_gid,
            )
            or identity
            != (
                path_metadata.st_dev,
                path_metadata.st_ino,
                path_metadata.st_uid,
                path_metadata.st_gid,
            )
            or stat.S_IMODE(metadata.st_mode)
            != stat.S_IMODE(final_metadata.st_mode)
            or stat.S_IMODE(metadata.st_mode)
            != stat.S_IMODE(path_metadata.st_mode)
        ):
            raise ValueError("selection seal changed while it was read")
        return encoded
    finally:
        os.close(descriptor)


def seal_cross_archetype_canary_selection(
    path: str | Path,
    payload: Mapping[str, Any],
) -> Path:
    """Create a private regular-file seal; identical replay is idempotent."""

    destination = Path(path)
    if payload.get("schema_version") == SELECTION_SCHEMA:
        _validate_selection_manifest_shape(payload)
    _assert_no_symlink_ancestor(destination.parent)
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        + "\n"
    ).encode("utf-8")
    if destination.exists() or destination.is_symlink():
        if _read_regular_no_follow(destination) != encoded:
            raise ValueError("selection seal already exists with different payload")
        return destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    _assert_no_symlink_ancestor(destination.parent)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    temporary = Path(temporary_name)
    linked = False
    guard_descriptor: int | None = None
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
            # Keep the original inode alive until every final-path check has
            # completed.  Otherwise an attacker can unlink it and make the
            # filesystem immediately reuse the same inode number.
            guard_descriptor = os.dup(handle.fileno())
        temporary_stat = os.fstat(guard_descriptor)
        try:
            os.link(temporary, destination, follow_symlinks=False)
            linked = True
        except FileExistsError:
            if _read_regular_no_follow(destination) != encoded:
                raise ValueError(
                    "selection seal was concurrently created with different payload"
                )
            return destination
        destination_stat = destination.stat(follow_symlinks=False)
        if not stat.S_ISREG(destination_stat.st_mode) or (
            destination_stat.st_dev,
            destination_stat.st_ino,
        ) != (temporary_stat.st_dev, temporary_stat.st_ino):
            raise ValueError("selection seal changed during atomic creation")
        if _read_regular_no_follow_allow_link(destination) != encoded:
            raise ValueError("selection seal bytes changed during atomic creation")
        temporary.unlink()
        linked = False
        final_bytes = _read_regular_no_follow(destination)
        final_stat = destination.stat(follow_symlinks=False)
        guarded_stat = os.fstat(guard_descriptor)
        if (
            final_bytes != encoded
            or (
                final_stat.st_dev,
                final_stat.st_ino,
                final_stat.st_uid,
                final_stat.st_gid,
                stat.S_IMODE(final_stat.st_mode),
            )
            != (
                temporary_stat.st_dev,
                temporary_stat.st_ino,
                temporary_stat.st_uid,
                temporary_stat.st_gid,
                stat.S_IMODE(temporary_stat.st_mode),
            )
            or (
                guarded_stat.st_dev,
                guarded_stat.st_ino,
                guarded_stat.st_uid,
                guarded_stat.st_gid,
                stat.S_IMODE(guarded_stat.st_mode),
            )
            != (
                temporary_stat.st_dev,
                temporary_stat.st_ino,
                temporary_stat.st_uid,
                temporary_stat.st_gid,
                stat.S_IMODE(temporary_stat.st_mode),
            )
        ):
            raise ValueError("selection seal changed after atomic creation")
        directory_fd = os.open(destination.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if guard_descriptor is not None:
            os.close(guard_descriptor)
        if temporary.exists():
            temporary.unlink()
        if linked and destination.exists():
            # A failed validation must not leave an untrusted seal behind.
            destination.unlink()
    return destination


def load_sealed_cross_archetype_canary_selection(
    path: str | Path,
) -> Mapping[str, Any]:
    """Read one canonical, non-link selection seal for downstream execution."""

    source = Path(path)
    _assert_no_symlink_ancestor(source)
    encoded = _read_regular_no_follow(source)
    try:
        payload = json.loads(encoded.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("selection seal is not canonical JSON") from exc
    if not isinstance(payload, Mapping):
        raise ValueError("selection seal must contain one JSON object")
    canonical = (
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")
    if encoded != canonical:
        raise ValueError("selection seal JSON encoding is not canonical")
    _validate_selection_manifest_shape(payload)
    return dict(payload)


def _read_regular_no_follow_allow_link(path: Path) -> bytes:
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags)
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 2:
            raise ValueError("selection seal link state changed during creation")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)
    finally:
        os.close(descriptor)


__all__ = [
    "FORCED_SELECTION",
    "NATURAL_SELECTION",
    "REQUIRED_ARCHETYPES",
    "SELECTION_FAIL",
    "SELECTION_PASS",
    "compile_cross_archetype_canary_selection",
    "load_current_live_selection_inputs",
    "load_sealed_cross_archetype_canary_selection",
    "seal_cross_archetype_canary_selection",
    "summarize_cross_archetype_canary_selection",
]
