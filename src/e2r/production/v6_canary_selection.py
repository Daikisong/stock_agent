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
import math
import os
from pathlib import Path
import re
import secrets
import stat
from typing import Any

from e2r.production.metadata import stable_hash
from e2r.production.v6_issuer_business_profile import (
    PROFILE_PASS as ISSUER_PROFILE_COMPLETE,
    PROFILE_RESULT_SCHEMA_VERSION as ISSUER_PROFILE_SCHEMA,
    validate_issuer_business_profile_result,
)
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
SELECTION_SUMMARY_SCHEMA = "e2r_v6_pre_deep_canary_selection_summary_v1"
NATURAL_SELECTION = "NATURAL_TRIGGER_CANARY"
FORCED_SELECTION = "FORCED_VALIDATION_CANARY"
FORCED_PROFILE_EXPANSION_ORIGIN = "OFFICIAL_PROFILE_CANDIDATE_EXPANSION"
ISSUER_PROFILE_MANIFEST_NAME = "issuer_business_profile_manifest.json"
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
_FORCED_EXPANDED_CANDIDATE_KEYS = frozenset(
    {
        "universe_row",
        "forced_profile_target_id",
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
        "goldauthority",
        "forcedvalidationauthority",
        "outcomeevidencedroppedcount",
    }
)
_SAFE_PRE_DEEP_NUMERIC_KEYS = frozenset({"priorityscore", "returnpct"})
_SAFE_PRE_DEEP_ENUM_VALUES = {
    "pricescoreusage": frozenset({"INVESTIGATION_ONLY"}),
}
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
_FORCED_PROFILE_RECEIPT_KEYS = frozenset(
    {
        "official_profile_manifest_hash",
        "official_profile_id",
        "official_profile_hash",
        "official_profile_selection_id",
        "official_profile_selection_hash",
        "official_profile_compatibility_request_id",
        "official_profile_compatibility_response_id",
        "official_profile_compatibility_response_hash",
        "official_profile_compatibility_receipt_hash",
        "official_profile_document_id",
        "official_profile_document_hash",
        "official_profile_exact_quote_hash",
        "official_profile_large_sector_id",
        "official_profile_confidence",
        "forced_validation_authority",
        "gold_authority",
    }
)
_FORCED_EXPANSION_RECEIPT_KEYS = frozenset(
    {
        "forced_candidate_origin",
        "candidate_expansion_receipt_hash",
        "candidate_expansion_entry_hash",
    }
)
_SELECTION_SUMMARY_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "selection_as_of_date",
        "required_archetype_count",
        "selected_archetype_count",
        "natural_canary_count",
        "forced_validation_canary_count",
        "target_ids",
        "selection_ids",
        "selection_roster_hash",
        "post_score_target_selection_count",
        "target_specific_code_branch_count",
        "forced_canary_mislabeled_natural_count",
        "score_or_stage_authority",
        "summary_id",
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


class _LoadedSealedSelection(dict[str, Any]):
    """Dict-compatible seal carrying its already re-opened sibling profile.

    The attachment is deliberately not a JSON field, so the immutable Phase-105
    schema and roster hash stay unchanged.  Downstream Phase-106 validators that
    receive the loader result can nevertheless revalidate forced receipts
    without reaching back into ignored live output.
    """

    def __init__(
        self,
        payload: Mapping[str, Any],
        issuer_business_profile_manifest: Mapping[str, Any] | None,
    ) -> None:
        super().__init__(payload)
        self._issuer_business_profile_manifest = (
            dict(issuer_business_profile_manifest)
            if issuer_business_profile_manifest is not None
            else None
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
                safe_pre_deep_enum = (
                    normalized in _SAFE_PRE_DEEP_ENUM_VALUES
                    and child in _SAFE_PRE_DEEP_ENUM_VALUES[normalized]
                )
                if (
                    not safe_negative
                    and not safe_pre_deep
                    and not safe_pre_deep_enum
                    and any(
                        token in normalized
                        for token in _FORBIDDEN_DEEP_KEY_TOKENS
                    )
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


def load_current_issuer_business_profile_manifest(
    path: str | Path,
    *,
    selection_as_of_date: str,
) -> Mapping[str, Any]:
    """Load one immutable official profile manifest for forced canaries."""

    selection_date = _iso_date(
        selection_as_of_date, context="selection as_of_date"
    )
    payload = _json_object(
        _read_live_input_file(Path(path)),
        context="issuer business profile manifest",
    )
    validated = validate_issuer_business_profile_result(payload)
    if (
        validated.get("status") != ISSUER_PROFILE_COMPLETE
        or validated.get("as_of_date") != selection_date
    ):
        raise ValueError("forced issuer profile manifest is not current COMPLETE")
    return dict(validated)


def _official_profile_bindings(
    manifest: Mapping[str, Any] | None,
    *,
    selection_date: str,
) -> tuple[Mapping[str, Mapping[str, Any]], str | None]:
    if manifest is None:
        return {}, None
    validated = validate_issuer_business_profile_result(manifest)
    if (
        validated.get("status") != ISSUER_PROFILE_COMPLETE
        or validated.get("as_of_date") != selection_date
        or tuple(validated.get("required_archetypes") or ())
        != REQUIRED_ARCHETYPES
    ):
        raise ValueError("forced issuer profile manifest scope is not exact COMPLETE")
    manifest_hash = stable_hash(dict(validated))
    expansion_receipt = _mapping(
        validated.get("candidate_expansion_receipt"),
        context="official profile candidate expansion receipt",
    )
    expansion_receipt_hash = stable_hash(dict(expansion_receipt))
    natural_targets = {
        str(target)
        for target in expansion_receipt.get("natural_candidate_roster") or ()
    }
    legacy_natural_origin = (
        expansion_receipt.get("status") == "NOT_REQUESTED"
        and not tuple(expansion_receipt.get("expanded_candidates") or ())
    )
    expanded_entries = {
        str(row.get("target_id") or ""): dict(row)
        for row in expansion_receipt.get("expanded_candidates") or ()
        if isinstance(row, Mapping)
    }
    if "" in expanded_entries or len(expanded_entries) != len(
        expansion_receipt.get("expanded_candidates") or ()
    ):
        raise ValueError("official profile candidate expansion targets are not unique")
    profiles = {
        str(row["profile_id"]): row for row in validated["profiles"]
    }
    compatibility = {
        str(row["response_id"]): row
        for row in validated["compatibility_receipts"]
    }
    bindings: dict[str, Mapping[str, Any]] = {}
    for selection in validated["selections"]:
        target_id = str(selection["target_id"])
        profile = profiles[str(selection["profile_id"])]
        compatibility_receipt = compatibility[
            str(selection["compatibility_response_id"])
        ]
        expanded_entry = expanded_entries.get(target_id)
        is_natural = target_id in natural_targets or legacy_natural_origin
        if is_natural is (expanded_entry is not None):
            raise ValueError(
                "official profile target must have one exact natural or expanded origin"
            )
        if target_id in bindings:
            raise ValueError("forced issuer profile target is not unique")
        bindings[target_id] = {
            "archetype_id": selection["archetype_id"],
            "target_id": target_id,
            "company_name": selection["company_name"],
            "as_of_date": selection["as_of_date"],
            "krx_row": selection["krx_row"],
            "krx_request_id": selection["krx_request_id"],
            "krx_content_hash": selection["krx_content_hash"],
            "manifest_hash": manifest_hash,
            "profile_id": profile["profile_id"],
            "profile_hash": stable_hash(dict(profile)),
            "selection_id": selection["selection_id"],
            "selection_hash": stable_hash(dict(selection)),
            "compatibility_request_id": selection[
                "compatibility_request_id"
            ],
            "compatibility_response_id": selection[
                "compatibility_response_id"
            ],
            "compatibility_response_hash": selection[
                "compatibility_response_envelope_hash"
            ],
            "compatibility_receipt_hash": stable_hash(
                dict(compatibility_receipt)
            ),
            "document_id": selection["periodic_report_document_id"],
            "document_hash": selection["periodic_report_full_text_hash"],
            "exact_quote_hash": selection["exact_quote_hash"],
            "large_sector_id": selection["large_sector_id"],
            "confidence": selection["confidence"],
            "forced_candidate_origin": (
                "NATURAL_ABSTAINED_PLANNER"
                if is_natural
                else FORCED_PROFILE_EXPANSION_ORIGIN
            ),
            "candidate_expansion_receipt_hash": expansion_receipt_hash,
            "candidate_expansion_entry_hash": (
                stable_hash(expanded_entry) if expanded_entry is not None else None
            ),
        }
    if tuple(
        binding["archetype_id"] for binding in bindings.values()
    ) != REQUIRED_ARCHETYPES:
        raise ValueError("forced issuer profile selection roster is not exact")
    return bindings, manifest_hash


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
    def accepted_output(payload: object) -> object:
        # The planner decoder canonicalizes an optional empty abstention reason
        # to ``None`` before storing an accepted plan.  Preserve every other
        # response field exactly when binding the immutable journal to that
        # stored plan.
        if not isinstance(payload, Mapping):
            return payload
        normalized = dict(payload)
        if normalized.get("abstention_reason") == "":
            normalized["abstention_reason"] = None
        return normalized

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
    two_pass_run_by_target = {
        target_id: run
        for target_id, run in run_by_target.items()
        if run.get("terminal_status") == "COMPLETE"
        or (
            run.get("terminal_status") == "ABSTAINED"
            and run.get("provider_call_count") == 2
        )
    }
    for target_id, run in two_pass_run_by_target.items():
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
                "eligible two-pass planner target requires exactly its two successful calls"
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
        requires_two_pass = run.get("terminal_status") == "COMPLETE" or (
            run.get("terminal_status") == "ABSTAINED"
            and run.get("provider_call_count") == 2
        )
        if requires_two_pass and (
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
                "eligible two-pass planner run requires one exact call for each role"
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
            if (
                run.get("terminal_status") in {"COMPLETE", "ABSTAINED"}
                and accepted_output(response_payload_by_edge.get(edge))
                != expected_output
            ):
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
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> tuple[tuple[Mapping[str, Any], ...], tuple[Mapping[str, Any], ...]]:
    """Load the selector input only from one audited current live root.

    The operational CLI uses this loader instead of accepting hand-authored
    candidate rows.  Pure mapping compilation remains available for unit tests.
    """

    selection_date = _iso_date(
        selection_as_of_date, context="selection as_of_date"
    )
    forced_profile_bindings, _profile_manifest_hash = _official_profile_bindings(
        issuer_business_profile_manifest,
        selection_date=selection_date,
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
            or str(attempt.get("canonical_url") or "")
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
    loaded_forced_targets: set[str] = set()
    for run in planner_runs:
        terminal_status = run.get("terminal_status")
        target_id = str(run.get("target_id") or "")
        is_forced_profile_target = (
            terminal_status == "ABSTAINED"
            and target_id in forced_profile_bindings
        )
        if terminal_status != "COMPLETE" and not is_forced_profile_target:
            continue
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
        if is_forced_profile_target:
            loaded_forced_targets.add(target_id)
    for target_id, binding in forced_profile_bindings.items():
        if target_id in loaded_forced_targets:
            continue
        if binding.get("forced_candidate_origin") != FORCED_PROFILE_EXPANSION_ORIGIN:
            continue
        universe = universe_by_target.get(target_id)
        if universe is None:
            raise ValueError(
                "expanded forced issuer profile lacks an exact KRX universe row"
            )
        member = _universe_row(universe, selection_date=selection_date)
        if (
            binding.get("target_id") != member.symbol
            or binding.get("company_name") != member.company_name
            or binding.get("as_of_date") != selection_date
            or binding.get("krx_row") != universe
            or binding.get("krx_request_id") != member.source_request_id
            or binding.get("krx_content_hash") != member.source_content_hash
        ):
            raise ValueError(
                "expanded forced issuer profile does not bind the live KRX universe"
            )
        candidates.append(
            {
                "universe_row": universe,
                "forced_profile_target_id": target_id,
            }
        )
        loaded_forced_targets.add(target_id)
    if loaded_forced_targets != set(forced_profile_bindings):
        raise ValueError(
            "forced issuer profile requires an exact abstained-planner or official-expanded roster"
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
    expected_url = (
        f"{_KRX_BASE}/{endpoint}"
        f"?basDd={member.source_effective_date.replace('-', '')}"
    )
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


def _depth_decision(
    raw: object,
    *,
    require_acquisition_eligible: bool = True,
) -> LiveDepthDecision:
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
    if require_acquisition_eligible and (
        not decision.selected_for_deep
        or not decision.selected_for_brain
        or not decision.acquisition_eligible
    ):
        raise ValueError("canary selection requires an acquisition-eligible L3 plan")
    return decision


def _planner_projection(
    raw: object,
    *,
    allow_abstained: bool = False,
) -> Mapping[str, Any]:
    run = _mapping(raw, context="planner run")
    if set(run) != _PLANNER_RUN_KEYS:
        raise ValueError("planner run schema keys are not exact")
    plan = _mapping(run.get("plan"), context="planner plan")
    critique = _mapping(plan.get("critique_output"), context="planner critique")
    terminal_status = str(run.get("terminal_status") or "")
    top = tuple(critique.get("top_k_archetypes") or ())
    if any(not isinstance(row, Mapping) for row in top):
        raise ValueError("planner critique archetype rows must be objects")
    if not top and not (
        allow_abstained and terminal_status == "ABSTAINED"
    ):
        raise ValueError("planner critique requires a leading archetype")
    leading = str(top[0].get("archetype_id") or "") if top else ""
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
    accepted_terminal = terminal_status == "COMPLETE" or (
        allow_abstained and terminal_status == "ABSTAINED"
    )
    if (
        run.get("schema_version") != "e2r_live_planner_run_v1"
        or not accepted_terminal
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
        or plan.get("status") != terminal_status
        or plan.get("pending") is not None
        or plan.get("deterministic_stage_or_score_mutation") is not False
        or not isinstance(plan.get("blind_output"), Mapping)
        or critique.get("abstain") is not (terminal_status == "ABSTAINED")
    ):
        raise ValueError("planner run is not a current real terminal blind plan")
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
    if terminal_status == "COMPLETE" and (
        not supporting or not recipes or not sources
    ):
        raise ValueError("planner run lacks current support, recipes, or source lanes")
    if terminal_status == "ABSTAINED":
        supporting = ()
        recipes = ()
        sources = ()
    return {
        "planner_terminal_status": terminal_status,
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
    row: Mapping[str, Any],
    *,
    selection_date: str,
    official_profile_binding: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    if set(row) != _CANDIDATE_KEYS:
        raise ValueError("candidate schema keys are not exact")
    universe = _universe_row(row.get("universe_row"), selection_date=selection_date)
    event = _candidate_event(row.get("candidate_event"))
    depth = _depth_decision(row.get("depth_decision"))
    planner = _planner_projection(
        row.get("planner_run"),
        allow_abstained=official_profile_binding is not None,
    )
    target = str(universe.symbol or "")
    forced = planner["planner_terminal_status"] == "ABSTAINED"
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
    if forced:
        binding = _mapping(
            official_profile_binding,
            context="official forced profile binding",
        )
        if (
            binding.get("target_id") != target
            or binding.get("company_name") != universe.company_name
            or binding.get("as_of_date") != selection_date
            or binding.get("krx_row") != row.get("universe_row")
            or binding.get("krx_request_id") != universe.source_request_id
            or binding.get("krx_content_hash") != universe.source_content_hash
            or binding.get("archetype_id") not in REQUIRED_ARCHETYPES
        ):
            raise ValueError("forced profile does not bind exact KRX issuer lineage")
    elif official_profile_binding is not None:
        raise ValueError("official profile cannot relabel a completed natural planner")
    leading_archetype = (
        str(official_profile_binding["archetype_id"])
        if forced and official_profile_binding is not None
        else planner["leading_archetype_id"]
    )
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
            dict(official_profile_binding)
            if forced and official_profile_binding is not None
            else {
                "target_id": target,
                "leading_archetype_id": leading_archetype,
                "direct_current_supporting_fact_ids": planner[
                    "direct_current_supporting_fact_ids"
                ],
                "recipe_ids": planner["recipe_ids"],
                "available_source_families": planner[
                    "available_source_families"
                ],
            }
        ),
        "leading_archetype_id": leading_archetype,
        "official_profile_binding": (
            dict(official_profile_binding)
            if forced and official_profile_binding is not None
            else None
        ),
        "forced_profile_expansion": False,
    }


def _expanded_profile_candidate_projection(
    row: Mapping[str, Any],
    *,
    selection_date: str,
    official_profile_binding: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project a forced candidate sealed by full-KRX profile expansion.

    This is deliberately separate from planner projection: an issuer recovered
    from the full KRX roster has no L3 trigger/depth/planner lineage and must not
    be mislabeled as a real two-call planner abstention.
    """

    if set(row) != _FORCED_EXPANDED_CANDIDATE_KEYS:
        raise ValueError("expanded forced candidate schema keys are not exact")
    universe = _universe_row(row.get("universe_row"), selection_date=selection_date)
    binding = _mapping(
        official_profile_binding,
        context="official expanded forced profile binding",
    )
    target = str(universe.symbol or "")
    expansion_receipt_hash = str(
        binding.get("candidate_expansion_receipt_hash") or ""
    )
    expansion_entry_hash = str(binding.get("candidate_expansion_entry_hash") or "")
    if (
        row.get("forced_profile_target_id") != target
        or binding.get("forced_candidate_origin")
        != FORCED_PROFILE_EXPANSION_ORIGIN
        or binding.get("target_id") != target
        or binding.get("company_name") != universe.company_name
        or binding.get("as_of_date") != selection_date
        or binding.get("krx_row") != row.get("universe_row")
        or binding.get("krx_request_id") != universe.source_request_id
        or binding.get("krx_content_hash") != universe.source_content_hash
        or binding.get("archetype_id") not in REQUIRED_ARCHETYPES
        or _HEX64_RE.fullmatch(expansion_receipt_hash) is None
        or _HEX64_RE.fullmatch(expansion_entry_hash) is None
    ):
        raise ValueError("expanded profile does not bind exact official issuer lineage")
    expansion_identity = {
        "origin": FORCED_PROFILE_EXPANSION_ORIGIN,
        "target_id": target,
        "candidate_expansion_receipt_hash": expansion_receipt_hash,
        "candidate_expansion_entry_hash": expansion_entry_hash,
        "compatibility_request_id": binding["compatibility_request_id"],
        "compatibility_response_id": binding["compatibility_response_id"],
    }
    candidate_event_hash = stable_hash(
        {**expansion_identity, "projection": "FORCED_PROFILE_EVENT"}
    )
    depth_decision_hash = stable_hash(
        {**expansion_identity, "projection": "FORCED_PROFILE_DEPTH"}
    )
    planner_identity_hash = stable_hash(
        {**expansion_identity, "projection": "FORCED_PROFILE_COMPATIBILITY"}
    )
    leading_archetype = str(binding["archetype_id"])
    return {
        "planner_terminal_status": "PROFILE_EXPANDED",
        "planner_run_id": "PROFILEEXPAND-" + planner_identity_hash[:24],
        "target_id": target,
        "target_name": str(universe.company_name or ""),
        "as_of_date": selection_date,
        "depth_decision_id": "PROFILEDEPTH-" + depth_decision_hash[:24],
        "candidate_event_id": "PROFILEEVENT-" + candidate_event_hash[:24],
        "trigger_signal_ids": [],
        "source_refs": [universe.source_document_id, str(binding["document_id"])],
        "blind_input_id": "PROFILECOMPAT-" + planner_identity_hash[:24],
        "plan_hash": planner_identity_hash,
        "leading_archetype_id": leading_archetype,
        "direct_current_supporting_fact_ids": [],
        "recipe_ids": [],
        "available_source_families": ["KRX", "OPENDART"],
        "company_name": str(universe.company_name or ""),
        "market": universe.market,
        "krx_effective_date": universe.source_effective_date,
        "krx_source_url": universe.source_url,
        "krx_source_hash": universe.source_content_hash,
        "krx_request_id": universe.source_request_id,
        "candidate_event_hash": candidate_event_hash,
        "event_latest_effective_date": universe.source_effective_date,
        "event_trigger_types": [],
        "event_trigger_signal_ids": [],
        "event_source_refs": [
            universe.source_document_id,
            str(binding["document_id"]),
        ],
        "event_summary": (
            f"{universe.company_name}: official full-KRX issuer-profile "
            "expansion validation"
        ),
        "depth_decision_hash": depth_decision_hash,
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
        "business_profile_hash": stable_hash(dict(binding)),
        "official_profile_binding": dict(binding),
        "forced_profile_expansion": True,
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
        price_score_usage = signal.payload.get("price_score_usage")
        return_pct = signal.payload.get("return_pct")
        if (price_score_usage is not None or return_pct is not None) and (
            price_score_usage != "INVESTIGATION_ONLY"
            or isinstance(return_pct, bool)
            or not isinstance(return_pct, (int, float))
            or not math.isfinite(float(return_pct))
        ):
            raise ValueError("market trigger payload is not pre-deep investigation-only")
        if not str(signal.lifecycle_status or "").strip():
            raise ValueError("trigger lifecycle status is required")
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
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
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
    try:
        official_bindings, official_manifest_hash = _official_profile_bindings(
            issuer_business_profile_manifest,
            selection_date=selection_date,
        )
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        official_bindings = {}
        official_manifest_hash = None
        failures.append(
            {
                "code": "INVALID_ISSUER_BUSINESS_PROFILE_MANIFEST",
                "detail": str(exc),
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
            if set(row) == _FORCED_EXPANDED_CANDIDATE_KEYS:
                target_id = str(row.get("forced_profile_target_id") or "")
                projected.append(
                    _expanded_profile_candidate_projection(
                        row,
                        selection_date=selection_date,
                        official_profile_binding=_mapping(
                            official_bindings.get(target_id),
                            context="expanded official profile binding",
                        ),
                    )
                )
            else:
                planner_run = _mapping(
                    row.get("planner_run"), context="planner run"
                )
                target_id = str(planner_run.get("target_id") or "")
                binding = (
                    official_bindings.get(target_id)
                    if planner_run.get("terminal_status") == "ABSTAINED"
                    else None
                )
                projected.append(
                    _candidate_projection(
                        row,
                        selection_date=selection_date,
                        official_profile_binding=binding,
                    )
                )
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
        if row.get("forced_profile_expansion") is True:
            if (
                row.get("planner_terminal_status") != "PROFILE_EXPANDED"
                or tuple(row.get("trigger_signal_ids") or ())
                or tuple(row.get("event_trigger_signal_ids") or ())
                or tuple(row.get("event_trigger_types") or ())
                or not tuple(row.get("event_source_refs") or ())
            ):
                failures.append(
                    {
                        "code": "CANDIDATE_TRIGGER_ROSTER_MISMATCH",
                        "detail": {
                            "target_id": row.get("target_id"),
                            "aggregate_mismatch": True,
                            "expanded_profile_origin": True,
                        },
                    }
                )
                continue
            lineage_valid_candidates.append(row)
            continue
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
            forced_candidate = row["planner_terminal_status"] in {
                "ABSTAINED",
                "PROFILE_EXPANDED",
            }
            if not forced_candidate and not matching:
                continue
            ranked.append(
                (
                    1 if forced_candidate else 0,
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
        selection_mode = (
            FORCED_SELECTION
            if selected["planner_terminal_status"]
            in {"ABSTAINED", "PROFILE_EXPANDED"}
            else NATURAL_SELECTION
        )
        pre_deep_payload = {
            "selection_as_of_date": selection_date,
            "archetype_id": archetype_id,
            "candidate": selected,
            "trigger_signal_ids": (
                [row["trigger_signal_id"] for row in matching]
                if selection_mode == NATURAL_SELECTION
                else []
            ),
        }
        pre_deep_hash = stable_hash(pre_deep_payload)
        binding = selected.get("official_profile_binding")
        receipt = {
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
                    if selection_mode == NATURAL_SELECTION
                    else ()
                ),
                "recipe_ids": list(
                    selected["recipe_ids"]
                    if selection_mode == NATURAL_SELECTION
                    else ()
                ),
                "trigger_event_ids": (
                    [row["trigger_signal_id"] for row in matching]
                    if selection_mode == NATURAL_SELECTION
                    else []
                ),
                "available_source_families": list(
                    selected["available_source_families"]
                    if selection_mode == NATURAL_SELECTION
                    else ("KRX", "OPENDART")
                ),
                "selection_rationale": (
                    "current source-backed trigger lineage matches the current blind plan"
                    if selection_mode == NATURAL_SELECTION
                    else (
                        "forced validation canary from exact KRX, bounded official "
                        "profile expansion, and Codex compatibility lineage"
                        if selected.get("forced_profile_expansion") is True
                        else "forced validation canary from exact KRX, real two-call abstention, and official issuer profile lineage"
                    )
                ),
                "final_score_visible_at_selection": False,
                "final_stage_visible_at_selection": False,
                "production_daily_candidate": selection_mode == NATURAL_SELECTION,
                "score_or_stage_authority": False,
            }
        if selection_mode == FORCED_SELECTION:
            binding = _mapping(binding, context="forced profile binding")
            receipt.update(
                {
                    "official_profile_manifest_hash": binding["manifest_hash"],
                    "official_profile_id": binding["profile_id"],
                    "official_profile_hash": binding["profile_hash"],
                    "official_profile_selection_id": binding["selection_id"],
                    "official_profile_selection_hash": binding["selection_hash"],
                    "official_profile_compatibility_request_id": binding[
                        "compatibility_request_id"
                    ],
                    "official_profile_compatibility_response_id": binding[
                        "compatibility_response_id"
                    ],
                    "official_profile_compatibility_response_hash": binding[
                        "compatibility_response_hash"
                    ],
                    "official_profile_compatibility_receipt_hash": binding[
                        "compatibility_receipt_hash"
                    ],
                    "official_profile_document_id": binding["document_id"],
                    "official_profile_document_hash": binding["document_hash"],
                    "official_profile_exact_quote_hash": binding[
                        "exact_quote_hash"
                    ],
                    "official_profile_large_sector_id": binding[
                        "large_sector_id"
                    ],
                    "official_profile_confidence": binding["confidence"],
                    "forced_validation_authority": False,
                    "gold_authority": False,
                }
            )
            if selected.get("forced_profile_expansion") is True:
                receipt.update(
                    {
                        "forced_candidate_origin": binding[
                            "forced_candidate_origin"
                        ],
                        "candidate_expansion_receipt_hash": binding[
                            "candidate_expansion_receipt_hash"
                        ],
                        "candidate_expansion_entry_hash": binding[
                            "candidate_expansion_entry_hash"
                        ],
                    }
                )
        receipts.append(receipt)

    roster = tuple(row["archetype_id"] for row in receipts)
    if roster != REQUIRED_ARCHETYPES:
        failures.append(
            {"code": "REQUIRED_ARCHETYPE_SELECTION_ROSTER_MISMATCH", "detail": list(roster)}
        )
    if len({row["target_id"] for row in receipts}) != len(receipts):
        failures.append({"code": "CROSS_ARCHETYPE_TARGET_REUSE", "detail": None})
    forced_receipt_targets = {
        str(row["target_id"])
        for row in receipts
        if row["selection_mode"] == FORCED_SELECTION
    }
    if official_bindings and forced_receipt_targets != set(official_bindings):
        failures.append(
            {
                "code": "OFFICIAL_PROFILE_FORCED_TARGET_ROSTER_MISMATCH",
                "detail": {
                    "selected": sorted(forced_receipt_targets),
                    "profile": sorted(official_bindings),
                },
            }
        )

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
    # Keep the established natural-selection manifest byte/schema compatible.
    # The extra binding exists only when the separate official-profile lane is
    # actually authorizing one or more forced validation canaries.
    if official_manifest_hash is not None:
        result["issuer_business_profile_manifest_hash"] = official_manifest_hash
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
        set(payload)
        not in {
            _SELECTION_MANIFEST_KEYS,
            _SELECTION_MANIFEST_KEYS
            | {"issuer_business_profile_manifest_hash"},
        }
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
    forced_manifest_hashes: set[str] = set()
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
        expanded_forced = (
            mode == FORCED_SELECTION
            and receipt.get("forced_candidate_origin")
            == FORCED_PROFILE_EXPANSION_ORIGIN
        )
        expected_receipt_keys = _SELECTION_RECEIPT_KEYS
        if mode == FORCED_SELECTION:
            expected_receipt_keys |= _FORCED_PROFILE_RECEIPT_KEYS
        if expanded_forced:
            expected_receipt_keys |= _FORCED_EXPANSION_RECEIPT_KEYS
        if (
            set(receipt) != expected_receipt_keys
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
            or not tuple(receipt.get("available_source_families") or ())
        ):
            raise ValueError("selection receipt identity or blind lineage is invalid")
        if mode == NATURAL_SELECTION:
            if (
                not tuple(receipt.get("direct_current_supporting_fact_ids") or ())
                or not tuple(receipt.get("recipe_ids") or ())
            ):
                raise ValueError("natural selection lacks current fact/recipe lineage")
        else:
            forced_hash_fields = (
                "official_profile_manifest_hash",
                "official_profile_hash",
                "official_profile_selection_hash",
                "official_profile_compatibility_response_hash",
                "official_profile_compatibility_receipt_hash",
                "official_profile_document_hash",
                "official_profile_exact_quote_hash",
            )
            confidence = receipt.get("official_profile_confidence")
            if (
                trigger_ids
                or tuple(receipt.get("direct_current_supporting_fact_ids") or ())
                or tuple(receipt.get("recipe_ids") or ())
                or tuple(receipt.get("available_source_families") or ())
                != ("KRX", "OPENDART")
                or receipt.get("production_daily_candidate") is not False
                or receipt.get("forced_validation_authority") is not False
                or receipt.get("gold_authority") is not False
                or any(
                    _HEX64_RE.fullmatch(str(receipt.get(field) or "")) is None
                    for field in forced_hash_fields
                )
                or re.fullmatch(
                    r"ISSUERPROFILE-[0-9a-f]{24}",
                    str(receipt.get("official_profile_id") or ""),
                )
                is None
                or re.fullmatch(
                    r"PROFILESEL-[0-9a-f]{24}",
                    str(receipt.get("official_profile_selection_id") or ""),
                )
                is None
                or re.fullmatch(
                    r"PROFILECLASSREQ-[0-9a-f]{24}",
                    str(
                        receipt.get(
                            "official_profile_compatibility_request_id"
                        )
                        or ""
                    ),
                )
                is None
                or re.fullmatch(
                    r"PROFILECLASSRESP-[0-9a-f]{24}",
                    str(
                        receipt.get(
                            "official_profile_compatibility_response_id"
                        )
                        or ""
                    ),
                )
                is None
                or not str(receipt.get("official_profile_document_id") or "").startswith(
                    "opendart:disclosure:"
                )
                or not str(receipt.get("official_profile_large_sector_id") or "").startswith(
                    "L"
                )
                or isinstance(confidence, bool)
                or not isinstance(confidence, (int, float))
                or not 0.0 <= float(confidence) <= 1.0
            ):
                raise ValueError("forced selection lacks exact official profile lineage")
            if expanded_forced:
                expansion_receipt_hash = str(
                    receipt.get("candidate_expansion_receipt_hash") or ""
                )
                expansion_entry_hash = str(
                    receipt.get("candidate_expansion_entry_hash") or ""
                )
                expansion_identity = {
                    "origin": FORCED_PROFILE_EXPANSION_ORIGIN,
                    "target_id": target,
                    "candidate_expansion_receipt_hash": expansion_receipt_hash,
                    "candidate_expansion_entry_hash": expansion_entry_hash,
                    "compatibility_request_id": receipt[
                        "official_profile_compatibility_request_id"
                    ],
                    "compatibility_response_id": receipt[
                        "official_profile_compatibility_response_id"
                    ],
                }
                expected_event_hash = stable_hash(
                    {**expansion_identity, "projection": "FORCED_PROFILE_EVENT"}
                )
                expected_depth_hash = stable_hash(
                    {**expansion_identity, "projection": "FORCED_PROFILE_DEPTH"}
                )
                expected_plan_hash = stable_hash(
                    {
                        **expansion_identity,
                        "projection": "FORCED_PROFILE_COMPATIBILITY",
                    }
                )
                if (
                    _HEX64_RE.fullmatch(expansion_receipt_hash) is None
                    or _HEX64_RE.fullmatch(expansion_entry_hash) is None
                    or receipt.get("candidate_event_hash") != expected_event_hash
                    or receipt.get("depth_decision_hash") != expected_depth_hash
                    or receipt.get("plan_hash") != expected_plan_hash
                    or receipt.get("planner_run_id")
                    != "PROFILEEXPAND-" + expected_plan_hash[:24]
                    or receipt.get("blind_input_id")
                    != "PROFILECOMPAT-" + expected_plan_hash[:24]
                ):
                    raise ValueError(
                        "expanded forced selection lineage does not recompute"
                    )
            forced_manifest_hashes.add(
                str(receipt["official_profile_manifest_hash"])
            )
        targets.append(target)
    manifest_hash = payload.get("issuer_business_profile_manifest_hash")
    if (
        forced_manifest_hashes
        and (
            forced_manifest_hashes != {str(manifest_hash or "")}
            or _HEX64_RE.fullmatch(str(manifest_hash or "")) is None
        )
    ) or (not forced_manifest_hashes and manifest_hash is not None):
        raise ValueError("selection manifest official profile hash binding is invalid")
    if len(targets) != len(set(targets)):
        raise ValueError("selection target roster is not canonical and unique")


def validate_cross_archetype_canary_selection_manifest(
    payload: Mapping[str, Any],
    *,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> None:
    """Validate the complete sealed Phase-105 selection contract."""

    if issuer_business_profile_manifest is None:
        attached_profile = getattr(
            payload, "_issuer_business_profile_manifest", None
        )
        if isinstance(attached_profile, Mapping):
            issuer_business_profile_manifest = attached_profile
    _validate_selection_manifest_shape(payload)
    forced_receipts = tuple(
        row
        for row in payload.get("selections") or ()
        if row.get("selection_mode") == FORCED_SELECTION
    )
    if not forced_receipts:
        if issuer_business_profile_manifest is not None:
            raise ValueError("natural selection must not bind a forced profile manifest")
        return
    bindings, manifest_hash = _official_profile_bindings(
        issuer_business_profile_manifest,
        selection_date=str(payload.get("selection_as_of_date") or ""),
    )
    if (
        not bindings
        or manifest_hash != payload.get("issuer_business_profile_manifest_hash")
        or {str(row["target_id"]) for row in forced_receipts} != set(bindings)
    ):
        raise ValueError("forced selection external profile manifest binding is missing")
    receipt_fields = {
        "official_profile_manifest_hash": "manifest_hash",
        "official_profile_id": "profile_id",
        "official_profile_hash": "profile_hash",
        "official_profile_selection_id": "selection_id",
        "official_profile_selection_hash": "selection_hash",
        "official_profile_compatibility_request_id": "compatibility_request_id",
        "official_profile_compatibility_response_id": "compatibility_response_id",
        "official_profile_compatibility_response_hash": "compatibility_response_hash",
        "official_profile_compatibility_receipt_hash": "compatibility_receipt_hash",
        "official_profile_document_id": "document_id",
        "official_profile_document_hash": "document_hash",
        "official_profile_exact_quote_hash": "exact_quote_hash",
        "official_profile_large_sector_id": "large_sector_id",
        "official_profile_confidence": "confidence",
    }
    for receipt in forced_receipts:
        binding = bindings[str(receipt["target_id"])]
        expanded = (
            binding.get("forced_candidate_origin")
            == FORCED_PROFILE_EXPANSION_ORIGIN
        )
        expansion_fields = {
            "forced_candidate_origin": "forced_candidate_origin",
            "candidate_expansion_receipt_hash": (
                "candidate_expansion_receipt_hash"
            ),
            "candidate_expansion_entry_hash": "candidate_expansion_entry_hash",
        }
        if (
            receipt.get("archetype_id") != binding["archetype_id"]
            or receipt.get("company_name") != binding["company_name"]
            or any(
                receipt.get(receipt_field) != binding[binding_field]
                for receipt_field, binding_field in receipt_fields.items()
            )
            or (
                expanded
                and any(
                    receipt.get(receipt_field) != binding[binding_field]
                    for receipt_field, binding_field in expansion_fields.items()
                )
            )
            or (
                not expanded
                and any(receipt_field in receipt for receipt_field in expansion_fields)
            )
        ):
            raise ValueError("forced selection receipt differs from official profile")


def validate_cross_archetype_canary_selection_summary(
    payload: Mapping[str, Any],
) -> None:
    """Validate a compact summary before it becomes a tracked artifact."""

    target_ids = tuple(payload.get("target_ids") or ())
    selection_ids = tuple(payload.get("selection_ids") or ())
    natural_count = payload.get("natural_canary_count")
    forced_count = payload.get("forced_validation_canary_count")
    numeric_zero_fields = (
        "post_score_target_selection_count",
        "target_specific_code_branch_count",
        "forced_canary_mislabeled_natural_count",
    )
    if (
        set(payload) != _SELECTION_SUMMARY_KEYS
        or payload.get("schema_version") != SELECTION_SUMMARY_SCHEMA
        or payload.get("status") != SELECTION_PASS
        or payload.get("required_archetype_count") != len(REQUIRED_ARCHETYPES)
        or payload.get("selected_archetype_count") != len(REQUIRED_ARCHETYPES)
        or not isinstance(natural_count, int)
        or isinstance(natural_count, bool)
        or not isinstance(forced_count, int)
        or isinstance(forced_count, bool)
        or natural_count < 0
        or forced_count < 0
        or natural_count + forced_count != len(REQUIRED_ARCHETYPES)
        or len(target_ids) != len(REQUIRED_ARCHETYPES)
        or target_ids != tuple(sorted(target_ids))
        or len(set(target_ids)) != len(target_ids)
        or any(_TARGET_RE.fullmatch(str(target_id)) is None for target_id in target_ids)
        or len(selection_ids) != len(REQUIRED_ARCHETYPES)
        or len(set(selection_ids)) != len(selection_ids)
        or any(
            re.fullmatch(r"SELREC-[0-9a-f]{24}", str(selection_id)) is None
            for selection_id in selection_ids
        )
        or _HEX64_RE.fullmatch(str(payload.get("selection_roster_hash") or ""))
        is None
        or any(
            isinstance(payload.get(field), bool)
            or not isinstance(payload.get(field), int)
            or payload.get(field) != 0
            for field in numeric_zero_fields
        )
        or payload.get("score_or_stage_authority") is not False
    ):
        raise ValueError("selection summary contract is invalid")
    summary_without_id = {
        key: value for key, value in payload.items() if key != "summary_id"
    }
    if payload.get("summary_id") != "SELSUM-" + stable_hash(summary_without_id)[:24]:
        raise ValueError("selection summary identity does not recompute")


def _open_or_create_directory_no_symlinks(path: Path) -> int:
    """Pin a directory from the filesystem root without following links."""

    absolute = path.absolute()
    descriptor = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            if part in {"", ".", ".."}:
                raise ValueError("unsafe selection seal parent component")
            try:
                child = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=descriptor,
                )
            except FileNotFoundError:
                try:
                    os.mkdir(part, mode=0o700, dir_fd=descriptor)
                except FileExistsError:
                    pass
                child = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=descriptor,
                )
            os.close(descriptor)
            descriptor = child
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _open_existing_directory_no_symlinks(path: Path) -> int:
    """Re-open an existing directory path for final pathname identity checks."""

    absolute = path.absolute()
    descriptor = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            if part in {"", ".", ".."}:
                raise ValueError("unsafe selection seal parent component")
            child = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = child
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _read_regular_from_directory(
    parent_fd: int,
    name: str,
    *,
    expected_link_count: int = 1,
) -> tuple[bytes, os.stat_result]:
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(name, flags, dir_fd=parent_fd)
    try:
        before = os.fstat(descriptor)
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_nlink != expected_link_count
            or before.st_mode & 0o022
        ):
            raise ValueError("selection seal must be a private regular file")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        path_stat = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        identity = (
            before.st_dev,
            before.st_ino,
            before.st_uid,
            before.st_gid,
            stat.S_IMODE(before.st_mode),
        )
        if identity != (
            after.st_dev,
            after.st_ino,
            after.st_uid,
            after.st_gid,
            stat.S_IMODE(after.st_mode),
        ) or identity != (
            path_stat.st_dev,
            path_stat.st_ino,
            path_stat.st_uid,
            path_stat.st_gid,
            stat.S_IMODE(path_stat.st_mode),
        ):
            raise ValueError("selection seal changed while it was read")
        return b"".join(chunks), before
    finally:
        os.close(descriptor)


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
    *,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Path:
    """Create a private regular-file seal; identical replay is idempotent."""

    destination = Path(path).absolute()
    if payload.get("schema_version") == SELECTION_SCHEMA:
        validate_cross_archetype_canary_selection_manifest(
            payload,
            issuer_business_profile_manifest=issuer_business_profile_manifest,
        )
    elif payload.get("schema_version") == SELECTION_SUMMARY_SCHEMA:
        validate_cross_archetype_canary_selection_summary(payload)
    elif payload.get("schema_version") == ISSUER_PROFILE_SCHEMA:
        validated_profile = validate_issuer_business_profile_result(payload)
        if validated_profile.get("status") != ISSUER_PROFILE_COMPLETE:
            raise ValueError(
                "only a current COMPLETE issuer profile manifest may be sealed"
            )
    else:
        raise ValueError("selection seal schema is not supported")
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        + "\n"
    ).encode("utf-8")
    try:
        parent_fd = _open_or_create_directory_no_symlinks(destination.parent)
    except OSError as exc:
        raise ValueError("selection seal parent symlink or unsafe path is forbidden") from exc
    temporary_name = f".{destination.name}.{secrets.token_hex(16)}.tmp"
    temporary_fd = -1
    guard_fd = -1
    linked = False
    created_destination = False
    completed = False
    try:
        try:
            existing, _metadata = _read_regular_from_directory(
                parent_fd, destination.name
            )
        except FileNotFoundError:
            existing = None
        except OSError as exc:
            raise ValueError("selection seal symlink or unsafe file is forbidden") from exc
        if existing is not None:
            if existing != encoded:
                raise ValueError("selection seal already exists with different payload")
            return destination

        temporary_fd = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        with os.fdopen(temporary_fd, "wb") as handle:
            temporary_fd = -1
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
            guard_fd = os.dup(handle.fileno())
        temporary_stat = os.fstat(guard_fd)
        try:
            os.link(
                temporary_name,
                destination.name,
                src_dir_fd=parent_fd,
                dst_dir_fd=parent_fd,
                follow_symlinks=False,
            )
            linked = True
            created_destination = True
        except FileExistsError:
            existing, _metadata = _read_regular_from_directory(
                parent_fd, destination.name
            )
            if existing != encoded:
                raise ValueError(
                    "selection seal was concurrently created with different payload"
                )
            return destination
        destination_stat = os.stat(
            destination.name, dir_fd=parent_fd, follow_symlinks=False
        )
        if not stat.S_ISREG(destination_stat.st_mode) or (
            destination_stat.st_dev,
            destination_stat.st_ino,
        ) != (temporary_stat.st_dev, temporary_stat.st_ino):
            raise ValueError("selection seal changed during atomic creation")
        linked_bytes, _metadata = _read_regular_from_directory(
            parent_fd, destination.name, expected_link_count=2
        )
        if linked_bytes != encoded:
            raise ValueError("selection seal bytes changed during atomic creation")
        os.unlink(temporary_name, dir_fd=parent_fd)
        linked = False
        final_bytes, final_stat = _read_regular_from_directory(
            parent_fd, destination.name
        )
        guarded_stat = os.fstat(guard_fd)
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
        os.fsync(parent_fd)
        try:
            reopened_parent_fd = _open_existing_directory_no_symlinks(
                destination.parent
            )
        except OSError as exc:
            os.unlink(destination.name, dir_fd=parent_fd)
            raise ValueError(
                "selection seal parent changed during atomic creation"
            ) from exc
        try:
            pinned = os.fstat(parent_fd)
            reopened = os.fstat(reopened_parent_fd)
            if (pinned.st_dev, pinned.st_ino) != (reopened.st_dev, reopened.st_ino):
                os.unlink(destination.name, dir_fd=parent_fd)
                raise ValueError("selection seal parent changed during atomic creation")
        finally:
            os.close(reopened_parent_fd)
        completed = True
    finally:
        if temporary_fd >= 0:
            os.close(temporary_fd)
        if guard_fd >= 0:
            os.close(guard_fd)
        try:
            os.unlink(temporary_name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        if linked:
            try:
                os.unlink(destination.name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
        elif created_destination and not completed:
            try:
                os.unlink(destination.name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
        os.close(parent_fd)
    return destination


def seal_current_issuer_business_profile_manifest(
    path: str | Path,
    payload: Mapping[str, Any],
) -> Path:
    """Seal one self-contained COMPLETE profile beside the Phase-105 selection.

    The underlying writer is the same no-symlink, no-hardlink, atomic writer
    used by the selection seal.  Keeping the validated profile in the tracked
    cutover directory lets a clean clone re-open a forced selection without
    reading the ignored live-output tree or a Collaboration journal.
    """

    validated = validate_issuer_business_profile_result(payload)
    if validated.get("status") != ISSUER_PROFILE_COMPLETE:
        raise ValueError(
            "only a current COMPLETE issuer profile manifest may be sealed"
        )
    return seal_cross_archetype_canary_selection(path, validated)


def _validate_legacy_current_issuer_profile_for_replacement(
    raw: Mapping[str, Any],
    *,
    replacement: Mapping[str, Any],
) -> None:
    """Admit only the old COMPLETE Phase-105 leaf for an explicit migration.

    Phase-105 originally used a create-only seal.  That is correct for an
    immutable historical receipt, but this filename is the *current* profile
    pointer.  When a validator bug is repaired, the old bytes must be replaced
    without pretending that the stale target is still current.  The legacy
    v2 leaf predates the listed-mechanism-owner fields, so the current strict
    validator cannot reopen it; this bounded check is intentionally only a
    replacement precondition and never makes the legacy leaf authoritative.
    """

    selections = raw.get("selections")
    compatibility_receipts = raw.get("compatibility_receipts")
    audit = raw.get("audit")
    legacy_decision_keys = {
        "archetype_id",
        "status",
        "target_id",
        "company_name",
        "profile_id",
        "large_sector_id",
        "periodic_report_document_id",
        "exact_quote",
        "mechanism_rationale",
        "confidence",
    }
    if (
        raw.get("schema_version") != ISSUER_PROFILE_SCHEMA
        or raw.get("status") != ISSUER_PROFILE_COMPLETE
        or raw.get("as_of_date") != replacement.get("as_of_date")
        or tuple(raw.get("required_archetypes") or ()) != REQUIRED_ARCHETYPES
        or not isinstance(selections, list)
        or len(selections) != len(REQUIRED_ARCHETYPES)
        or tuple(
            str(row.get("archetype_id") or "")
            for row in selections
            if isinstance(row, Mapping)
        )
        != REQUIRED_ARCHETYPES
        or len(
            {
                str(row.get("target_id") or "")
                for row in selections
                if isinstance(row, Mapping)
            }
        )
        != len(REQUIRED_ARCHETYPES)
        or any(
            not isinstance(row, Mapping)
            or not str(row.get("target_id") or "")
            or not str(row.get("company_name") or "")
            or not str(row.get("profile_id") or "")
            or not str(row.get("periodic_report_document_id") or "")
            or row.get("forced_validation_authority") is not False
            or row.get("score_or_stage_authority") is not False
            or row.get("gold_authority") is not False
            for row in selections
        )
        # Do not let a damaged current-schema file fall back to the legacy
        # migration path.  Only the exact pre-owner-field decision shape is
        # admitted; current decisions must pass the current strict validator.
        or not isinstance(compatibility_receipts, list)
        or any(
            not isinstance(receipt, Mapping)
            or not isinstance(receipt.get("decisions"), list)
            or any(
                not isinstance(decision, Mapping)
                or set(decision) != legacy_decision_keys
                for decision in receipt.get("decisions") or ()
            )
            for receipt in compatibility_receipts
        )
        or any(
            "mechanism_owner_target_id" in row
            or "mechanism_owner_company_name" in row
            for row in selections
        )
        or not isinstance(audit, Mapping)
        or audit.get("production_acceptance_pass") is not True
        or audit.get("provider_status") != "COMPLETED"
        or audit.get("selected_archetype_count") != len(REQUIRED_ARCHETYPES)
        or audit.get("unique_selected_target_count") != len(REQUIRED_ARCHETYPES)
        or raw.get("forced_validation_authority") is not False
        or raw.get("score_or_stage_authority") is not False
        or raw.get("gold_authority") is not False
    ):
        raise ValueError("existing current issuer profile is not replaceable COMPLETE")


def _replace_private_regular_file(
    destination: Path,
    *,
    expected_existing: bytes,
    replacement: bytes,
) -> None:
    """Atomically compare-and-swap one private regular file."""

    try:
        parent_fd = _open_existing_directory_no_symlinks(destination.parent)
    except OSError as exc:
        raise ValueError("current seal parent symlink or unsafe path is forbidden") from exc
    temporary_name = f".{destination.name}.{secrets.token_hex(16)}.replace.tmp"
    temporary_fd = -1
    try:
        existing, _metadata = _read_regular_from_directory(
            parent_fd, destination.name
        )
        if existing != expected_existing:
            raise ValueError("current seal changed before explicit replacement")
        if existing == replacement:
            return
        temporary_fd = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        offset = 0
        while offset < len(replacement):
            offset += os.write(temporary_fd, replacement[offset:])
        os.fsync(temporary_fd)
        temporary_stat = os.fstat(temporary_fd)
        if not stat.S_ISREG(temporary_stat.st_mode) or temporary_stat.st_nlink != 1:
            raise ValueError("replacement seal temporary file is not private")
        concurrent, _metadata = _read_regular_from_directory(
            parent_fd, destination.name
        )
        if concurrent != expected_existing:
            raise ValueError("current seal changed during explicit replacement")
        os.replace(
            temporary_name,
            destination.name,
            src_dir_fd=parent_fd,
            dst_dir_fd=parent_fd,
        )
        final, final_stat = _read_regular_from_directory(parent_fd, destination.name)
        if final != replacement or (
            final_stat.st_dev,
            final_stat.st_ino,
            final_stat.st_uid,
            final_stat.st_gid,
            stat.S_IMODE(final_stat.st_mode),
        ) != (
            temporary_stat.st_dev,
            temporary_stat.st_ino,
            temporary_stat.st_uid,
            temporary_stat.st_gid,
            stat.S_IMODE(temporary_stat.st_mode),
        ):
            raise ValueError("current seal replacement did not publish exact bytes")
        os.fsync(parent_fd)
    finally:
        if temporary_fd >= 0:
            os.close(temporary_fd)
        try:
            os.unlink(temporary_name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        os.close(parent_fd)


def publish_current_issuer_business_profile_manifest(
    path: str | Path,
    payload: Mapping[str, Any],
    *,
    replace_existing: bool = False,
) -> Path:
    """Publish the current Phase-105 profile, with explicit CAS migration.

    Normal calls retain the immutable create/idempotent behavior.  A caller
    must explicitly opt into replacement, and both the stale leaf and the new
    leaf must be COMPLETE, authority-free manifests for the same as-of date.
    """

    validated = validate_issuer_business_profile_result(payload)
    if validated.get("status") != ISSUER_PROFILE_COMPLETE:
        raise ValueError("only a current COMPLETE issuer profile may be published")
    destination = Path(path).absolute()
    if not replace_existing:
        return seal_current_issuer_business_profile_manifest(destination, validated)
    existing = _read_regular_no_follow(destination)
    try:
        previous = json.loads(existing.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("existing current issuer profile is not canonical JSON") from exc
    if not isinstance(previous, Mapping):
        raise ValueError("existing current issuer profile is not an object")
    try:
        previous_validated = validate_issuer_business_profile_result(previous)
    except ValueError:
        _validate_legacy_current_issuer_profile_for_replacement(
            previous,
            replacement=validated,
        )
    else:
        if (
            previous_validated.get("status") != ISSUER_PROFILE_COMPLETE
            or previous_validated.get("as_of_date") != validated.get("as_of_date")
        ):
            raise ValueError("existing current issuer profile scope is not replaceable")
    encoded = (
        json.dumps(validated, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        + "\n"
    ).encode("utf-8")
    _replace_private_regular_file(
        destination,
        expected_existing=existing,
        replacement=encoded,
    )
    return destination


def publish_current_cross_archetype_canary_selection(
    path: str | Path,
    payload: Mapping[str, Any],
    *,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
    replace_existing: bool = False,
) -> Path:
    """Publish the current pre-deep selection with explicit CAS replacement."""

    validate_cross_archetype_canary_selection_manifest(
        payload,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    destination = Path(path).absolute()
    if not replace_existing:
        return seal_cross_archetype_canary_selection(
            destination,
            payload,
            issuer_business_profile_manifest=issuer_business_profile_manifest,
        )
    existing = _read_regular_no_follow(destination)
    try:
        previous = json.loads(existing.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("existing current selection is not canonical JSON") from exc
    if not isinstance(previous, Mapping):
        raise ValueError("existing current selection is not an object")
    # The previous current pointer is bound to the previous profile manifest,
    # which has already been superseded before this publication step.  Its
    # self-contained receipt/hash shape is still auditable, but rebinding it
    # to the *new* profile would be false lineage.  Validate that immutable
    # shape here and validate the replacement against the new profile above.
    _validate_selection_manifest_shape(previous)
    if (
        previous.get("status") != SELECTION_PASS
        or previous.get("selection_as_of_date") != payload.get("selection_as_of_date")
    ):
        raise ValueError("existing current selection scope is not replaceable")
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        + "\n"
    ).encode("utf-8")
    _replace_private_regular_file(
        destination,
        expected_existing=existing,
        replacement=encoded,
    )
    return destination


def load_sealed_cross_archetype_canary_selection(
    path: str | Path,
    *,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
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
    forced_receipts = tuple(
        row
        for row in payload.get("selections") or ()
        if isinstance(row, Mapping)
        and row.get("selection_mode") == FORCED_SELECTION
    )
    if forced_receipts and issuer_business_profile_manifest is None:
        issuer_business_profile_manifest = (
            load_current_issuer_business_profile_manifest(
                source.parent / ISSUER_PROFILE_MANIFEST_NAME,
                selection_as_of_date=str(
                    payload.get("selection_as_of_date") or ""
                ),
            )
        )
    validate_cross_archetype_canary_selection_manifest(
        payload,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    return _LoadedSealedSelection(
        payload,
        issuer_business_profile_manifest,
    )


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
    "ISSUER_PROFILE_MANIFEST_NAME",
    "NATURAL_SELECTION",
    "REQUIRED_ARCHETYPES",
    "SELECTION_FAIL",
    "SELECTION_PASS",
    "compile_cross_archetype_canary_selection",
    "load_current_issuer_business_profile_manifest",
    "load_current_live_selection_inputs",
    "load_sealed_cross_archetype_canary_selection",
    "publish_current_cross_archetype_canary_selection",
    "publish_current_issuer_business_profile_manifest",
    "seal_cross_archetype_canary_selection",
    "seal_current_issuer_business_profile_manifest",
    "summarize_cross_archetype_canary_selection",
    "validate_cross_archetype_canary_selection_manifest",
    "validate_cross_archetype_canary_selection_summary",
]
