"""Research-to-runtime parity audit for Census V4 full-thesis runs.

This module does not rerun live research.  It audits existing operational
artifacts and answers a narrower question: for every registered archetype, did
the latest run actually attempt source routing, produce accepted claims, reach
StageCourt, and promote a production full-thesis row?
"""

from __future__ import annotations

import ast
import csv
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.census.placeholder_symbols import is_placeholder_symbol


DEFAULT_MANDATORY_ARCHETYPE_PREFIXES = ("C06", "C08", "C15", "C17", "C24", "C28")


def _read_json(path: Path, default: Any | None = None) -> Any:
    if not path.exists():
        return {} if default is None else default
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _short_archetype_id(value: str | None) -> str | None:
    if not value:
        return None
    if value == "UNKNOWN":
        return None
    return str(value).split("_", 1)[0]


def _parse_listish(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    text = str(value).strip()
    if not text:
        return []
    if text in {"[]", "null", "None"}:
        return []
    if text.startswith("[") and text.endswith("]"):
        try:
            parsed = ast.literal_eval(text)
            if isinstance(parsed, list):
                return parsed
        except (SyntaxError, ValueError):
            pass
    if "|" in text:
        return [part.strip() for part in text.split("|") if part.strip()]
    if ";" in text:
        return [part.strip() for part in text.split(";") if part.strip()]
    if "," in text:
        return [part.strip() for part in text.split(",") if part.strip()]
    return [text]


def _load_contract_ids(repo_root: Path) -> list[str]:
    contract_path = repo_root / "configs" / "e2r_agentic_evidence_contracts_v2.json"
    payload = _read_json(contract_path)
    contracts = payload.get("contracts", [])
    contract_ids = [row.get("archetype_id") or row.get("canonical_archetype_id") for row in contracts]
    return [str(value) for value in contract_ids if value]


def _contract_scope_counts(contract_ids: Sequence[str]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for archetype_id in contract_ids:
        prefix = _short_archetype_id(archetype_id) or ""
        if prefix.startswith("C"):
            counts["C_CANONICAL_ARCHETYPE"] += 1
        elif prefix.startswith("R13"):
            counts["R13_CROSS_ARCHETYPE"] += 1
        else:
            counts["OTHER_REGISTERED_ARCHETYPE"] += 1
    return dict(sorted(counts.items()))


def _normalizer(contract_ids: Sequence[str]):
    by_short = {_short_archetype_id(value): value for value in contract_ids if _short_archetype_id(value)}
    full_set = set(contract_ids)

    def normalize(value: str | None) -> str | None:
        if not value:
            return None
        text = str(value)
        if text in full_set:
            return text
        short = _short_archetype_id(text)
        if short and short in by_short:
            return by_short[short]
        return None

    return normalize


def _resolve_output_root(repo_root: Path, docs_dir: Path, explicit_output_root: str | Path | None) -> Path:
    if explicit_output_root:
        path = Path(explicit_output_root)
        return path if path.is_absolute() else repo_root / path
    manifest = _read_json(docs_dir / "census_mode_v4_artifact_manifest.json")
    output_root = manifest.get("output_root")
    if not output_root:
        raise FileNotFoundError("Cannot resolve output root from census_mode_v4_artifact_manifest.json")
    path = Path(output_root)
    return path if path.is_absolute() else repo_root / path


@dataclass
class ArchetypeRuntimeAccumulator:
    archetype_id: str
    replay_status: str | None = None
    replay_scope: str | None = None
    source_backed_fixture_count: int = 0
    replay_accepted_claim_count: int = 0
    replay_score_contribution_count: int = 0
    source_proxy_leak_count: int = 0
    runtime_refresh_queue_count: int = 0
    runtime_seed_source_primary_count: int = 0
    runtime_seed_target_count: int = 0
    runtime_seed_effective_attempt_count: int = 0
    archetype_level_discovery_seed_count: int = 0
    target_materialization_required_seed_count: int = 0
    placeholder_symbol_seed_count: int = 0
    runtime_planner_top1_count: int = 0
    runtime_planner_topk_count: int = 0
    runtime_source_task_execution_count: int = 0
    targetless_source_task_execution_count: int = 0
    runtime_source_task_accepted_claim_count: int = 0
    runtime_follow_up_source_task_count: int = 0
    runtime_candidate_attempt_count: int = 0
    runtime_blocked_candidate_count: int = 0
    runtime_accepted_claim_count: int = 0
    runtime_score_contribution_count: int = 0
    runtime_stagecourt_trace_count: int = 0
    runtime_full_thesis_row_count: int = 0
    runtime_full_thesis_row_with_required_positive_missing_count: int = 0
    runtime_full_thesis_row_with_green_gap_count: int = 0
    promoted_target_unknown_count: int = 0
    promoted_source_primary_context_count: int = 0
    source_pending_required_or_green_gap_count: int = 0
    symbols: set[str] = field(default_factory=set)
    full_thesis_symbols: set[str] = field(default_factory=set)
    blocked_symbols: set[str] = field(default_factory=set)
    planner_top1_symbols: set[str] = field(default_factory=set)
    accepted_claim_symbols: set[str] = field(default_factory=set)
    blocker_classes: set[str] = field(default_factory=set)

    def attempted(self) -> bool:
        return any(
            [
                self.runtime_seed_effective_attempt_count,
                self.archetype_level_discovery_seed_count,
                self.target_materialization_required_seed_count,
                self.runtime_planner_top1_count,
                self.runtime_source_task_execution_count,
                self.targetless_source_task_execution_count,
                self.runtime_follow_up_source_task_count,
                self.runtime_candidate_attempt_count,
                self.runtime_accepted_claim_count,
                self.runtime_stagecourt_trace_count,
                self.runtime_full_thesis_row_count,
            ]
        )

    def source_route_status(self) -> str:
        if self.runtime_full_thesis_row_count:
            return "FULL_THESIS_SCORE_PATH_CLOSED"
        if self.runtime_blocked_candidate_count:
            return "BLOCKED_FULL_THESIS_CANDIDATE"
        if self.runtime_stagecourt_trace_count:
            return "STAGECOURT_TRACE_NO_PRODUCTION_PROMOTION"
        if self.runtime_accepted_claim_count or self.runtime_source_task_accepted_claim_count:
            return "ACCEPTED_CLAIM_NO_FULL_THESIS"
        if self.runtime_source_task_execution_count or self.runtime_follow_up_source_task_count:
            return "SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM"
        if self.targetless_source_task_execution_count:
            return "ARCHETYPE_DISCOVERY_SOURCE_SHELL_NO_TARGET"
        if self.runtime_planner_top1_count or self.runtime_planner_topk_count:
            return "PLANNER_ATTEMPTED_NO_SOURCE_CLOSURE"
        if self.source_backed_fixture_count:
            return "RESEARCH_REPLAY_ONLY_NOT_RUNTIME_ATTEMPTED"
        return "NOT_ATTEMPTED"

    def runtime_parity_status(self) -> str:
        if self.runtime_full_thesis_row_count:
            if (
                self.runtime_full_thesis_row_with_required_positive_missing_count == 0
                and self.runtime_full_thesis_row_with_green_gap_count == 0
            ):
                return "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS"
            return "PRODUCTION_FULL_E2R_SCORE_PATH_ONLY"
        if self.runtime_blocked_candidate_count:
            return "FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP"
        if self.runtime_stagecourt_trace_count:
            return "STAGECOURT_TRACE_PRESENT_BUT_NOT_PROMOTED"
        if self.runtime_accepted_claim_count or self.runtime_source_task_accepted_claim_count:
            return "ACCEPTED_CLAIM_PRESENT_BUT_FULL_THESIS_NOT_CLOSED"
        if self.runtime_source_task_execution_count or self.runtime_follow_up_source_task_count:
            return "SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM"
        if self.targetless_source_task_execution_count or self.target_materialization_required_seed_count:
            return "ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED"
        if self.runtime_planner_top1_count or self.runtime_planner_topk_count:
            return "PLANNER_ATTEMPTED_BUT_NO_RUNTIME_SOURCE_CLOSURE"
        if self.source_backed_fixture_count:
            return "RESEARCH_REPLAY_READY_BUT_NOT_RUNTIME_PROVEN"
        return "NOT_RUNTIME_ATTEMPTED"

    def to_row(self, *, mandatory: bool) -> dict[str, Any]:
        blockers = set(self.blocker_classes)
        if self.runtime_full_thesis_row_with_required_positive_missing_count:
            blockers.add("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW")
        if self.runtime_full_thesis_row_with_green_gap_count:
            blockers.add("GREEN_GAP_ON_PROMOTED_ROW")
        if self.runtime_blocked_candidate_count:
            blockers.add("FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP")
        if mandatory and self.runtime_full_thesis_row_count == 0:
            blockers.add("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW")
        if self.source_backed_fixture_count and not self.attempted():
            blockers.add("SOURCE_BACKED_REPLAY_NOT_CONNECTED_TO_RUNTIME")
        if self.runtime_planner_top1_count and not (
            self.runtime_accepted_claim_count
            or self.runtime_source_task_accepted_claim_count
            or self.runtime_stagecourt_trace_count
            or self.runtime_full_thesis_row_count
        ):
            blockers.add("PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM")
        if self.target_materialization_required_seed_count or self.targetless_source_task_execution_count:
            blockers.add("TARGET_MATERIALIZATION_REQUIRED")
        if self.placeholder_symbol_seed_count:
            blockers.add("PLACEHOLDER_SYMBOL_REJECTED")
        if self.promoted_target_unknown_count:
            blockers.add("TARGET_ARCHETYPE_UNKNOWN_PROMOTED")
        if self.promoted_source_primary_context_count:
            blockers.add("SOURCE_PRIMARY_CONTEXT_PROMOTED")

        return {
            "schema_version": "e2r_research_to_runtime_parity_row_v1",
            "archetype_id": self.archetype_id,
            "mandatory_archetype": mandatory,
            "replay_status": self.replay_status,
            "replay_scope": self.replay_scope,
            "source_backed_fixture_count": self.source_backed_fixture_count,
            "replay_accepted_claim_count": self.replay_accepted_claim_count,
            "replay_score_contribution_count": self.replay_score_contribution_count,
            "source_proxy_leak_count": self.source_proxy_leak_count,
            "runtime_refresh_queue_count": self.runtime_refresh_queue_count,
            "runtime_seed_source_primary_count": self.runtime_seed_source_primary_count,
            "runtime_seed_target_count": self.runtime_seed_target_count,
            "runtime_seed_effective_attempt_count": self.runtime_seed_effective_attempt_count,
            "archetype_level_discovery_seed_count": self.archetype_level_discovery_seed_count,
            "target_materialization_required_seed_count": self.target_materialization_required_seed_count,
            "placeholder_symbol_seed_count": self.placeholder_symbol_seed_count,
            "runtime_planner_top1_count": self.runtime_planner_top1_count,
            "runtime_planner_topk_count": self.runtime_planner_topk_count,
            "runtime_source_task_execution_count": self.runtime_source_task_execution_count,
            "targetless_source_task_execution_count": self.targetless_source_task_execution_count,
            "runtime_source_task_accepted_claim_count": self.runtime_source_task_accepted_claim_count,
            "runtime_follow_up_source_task_count": self.runtime_follow_up_source_task_count,
            "runtime_candidate_attempt_count": self.runtime_candidate_attempt_count,
            "runtime_blocked_candidate_count": self.runtime_blocked_candidate_count,
            "runtime_accepted_claim_count": self.runtime_accepted_claim_count,
            "runtime_score_contribution_count": self.runtime_score_contribution_count,
            "runtime_stagecourt_trace_count": self.runtime_stagecourt_trace_count,
            "runtime_full_thesis_row_count": self.runtime_full_thesis_row_count,
            "runtime_full_thesis_row_with_required_positive_missing_count": (
                self.runtime_full_thesis_row_with_required_positive_missing_count
            ),
            "runtime_full_thesis_row_with_green_gap_count": self.runtime_full_thesis_row_with_green_gap_count,
            "promoted_target_unknown_count": self.promoted_target_unknown_count,
            "promoted_source_primary_context_count": self.promoted_source_primary_context_count,
            "source_pending_required_or_green_gap_count": self.source_pending_required_or_green_gap_count,
            "source_route_status": self.source_route_status(),
            "runtime_parity_status": self.runtime_parity_status(),
            "blocker_classes": sorted(blockers),
            "symbols_sample": sorted(self.symbols)[:20],
            "full_thesis_symbols": sorted(self.full_thesis_symbols),
            "blocked_symbols": sorted(self.blocked_symbols),
            "planner_top1_symbols_sample": sorted(self.planner_top1_symbols)[:20],
            "accepted_claim_symbols_sample": sorted(self.accepted_claim_symbols)[:20],
        }


def build_research_to_runtime_parity_audit(
    *,
    repo_root: str | Path = ".",
    output_root: str | Path | None = None,
    docs_dir: str | Path = "docs/operational",
    as_of_date: str | None = None,
    mandatory_archetype_prefixes: Sequence[str] = DEFAULT_MANDATORY_ARCHETYPE_PREFIXES,
) -> dict[str, Any]:
    repo_root = Path(repo_root).resolve()
    docs_path = Path(docs_dir)
    docs_path = docs_path if docs_path.is_absolute() else repo_root / docs_path
    output_path = _resolve_output_root(repo_root, docs_path, output_root)

    contract_ids = _load_contract_ids(repo_root)
    normalize = _normalizer(contract_ids)
    accumulators = {archetype_id: ArchetypeRuntimeAccumulator(archetype_id) for archetype_id in contract_ids}
    mandatory_ids = {value for value in (normalize(prefix) for prefix in mandatory_archetype_prefixes) if value}

    replay_matrix = _read_json(docs_path / "census_mode_v4_all_archetype_replay_matrix.json")
    for replay_row in replay_matrix.get("archetypes", []):
        archetype_id = normalize(replay_row.get("archetype_id"))
        if not archetype_id:
            continue
        row = accumulators[archetype_id]
        row.replay_status = replay_row.get("replay_status")
        row.replay_scope = replay_row.get("replay_scope")
        row.source_backed_fixture_count = int(replay_row.get("source_backed_fixture_count") or 0)
        row.replay_accepted_claim_count = int(replay_row.get("accepted_claim_count") or 0)
        row.replay_score_contribution_count = int(replay_row.get("score_contribution_count") or 0)
        row.source_proxy_leak_count = int(replay_row.get("source_proxy_leak_count") or 0)

    refresh_rows = _read_jsonl(docs_path / "census_mode_v4_full_thesis_refresh_queue.jsonl")
    for refresh in refresh_rows:
        archetype_id = normalize(refresh.get("source_primary_archetype"))
        if not archetype_id:
            continue
        row = accumulators[archetype_id]
        row.runtime_refresh_queue_count += 1
        if refresh.get("symbol") and not is_placeholder_symbol(refresh.get("symbol")):
            row.symbols.add(str(refresh["symbol"]))

    planner_top1_by_run: dict[str, str] = {}
    planner_top1_by_event: dict[str, str] = {}
    planner_rows = _read_jsonl(output_path / "planner_runs.jsonl")
    for planner in planner_rows:
        output = planner.get("output") or {}
        hypotheses = output.get("top_k_archetype_hypotheses") or output.get("archetype_hypotheses") or []
        normalized_hypotheses: list[str] = []
        for hypothesis in hypotheses:
            if isinstance(hypothesis, Mapping):
                archetype_id = normalize(
                    hypothesis.get("archetype_id")
                    or hypothesis.get("canonical_archetype_id")
                    or hypothesis.get("id")
                )
            else:
                archetype_id = normalize(str(hypothesis))
            if archetype_id:
                normalized_hypotheses.append(archetype_id)
        if not normalized_hypotheses:
            continue
        event = planner.get("event") or {}
        symbol = event.get("symbol")
        candidate_event_id = event.get("candidate_event_id")
        planner_run_id = planner.get("planner_run_id")
        top1 = normalized_hypotheses[0]
        if planner_run_id:
            planner_top1_by_run[str(planner_run_id)] = top1
        if candidate_event_id:
            planner_top1_by_event[str(candidate_event_id)] = top1
        for index, archetype_id in enumerate(normalized_hypotheses):
            row = accumulators[archetype_id]
            row.runtime_planner_topk_count += 1
            if index == 0:
                row.runtime_planner_top1_count += 1
                if symbol and not is_placeholder_symbol(symbol):
                    row.planner_top1_symbols.add(str(symbol))
                    row.symbols.add(str(symbol))

    seed_trace_rows = _read_jsonl(docs_path / "census_mode_v4_full_thesis_seed_materialization_trace.jsonl")
    target_unknown_promoted_count = 0
    source_primary_context_promoted_count = 0
    for seed in seed_trace_rows:
        target_id = normalize(seed.get("target_archetype"))
        source_primary_id = normalize(seed.get("source_primary_archetype"))
        planner_ids = [planner_top1_by_run.get(str(run_id)) for run_id in seed.get("planner_run_ids") or []]
        planner_ids = [value for value in planner_ids if value]
        effective_id = source_primary_id or (planner_ids[0] if planner_ids else None)
        if target_id:
            accumulators[target_id].runtime_seed_target_count += 1
        if source_primary_id:
            accumulators[source_primary_id].runtime_seed_source_primary_count += 1
        if effective_id:
            row = accumulators[effective_id]
            seed_symbol = seed.get("symbol")
            targetless_seed = is_placeholder_symbol(seed_symbol)
            target_symbol_mode = str(seed.get("target_symbol_mode") or "")
            target_materialization_status = str(seed.get("target_materialization_status") or "")
            row.runtime_seed_effective_attempt_count += 1
            if target_symbol_mode == "ARCHETYPE_LEVEL_DISCOVERY":
                row.archetype_level_discovery_seed_count += 1
            if targetless_seed or target_materialization_status == "TARGET_MATERIALIZATION_REQUIRED":
                row.target_materialization_required_seed_count += 1
            if seed.get("target_symbol_placeholder_rejected") is True:
                row.placeholder_symbol_seed_count += 1
            source_execution_count = int(seed.get("source_task_execution_count") or 0)
            if targetless_seed:
                row.targetless_source_task_execution_count += source_execution_count
            else:
                row.runtime_source_task_execution_count += source_execution_count
                row.runtime_accepted_claim_count += int(seed.get("accepted_claim_count") or 0)
                row.runtime_score_contribution_count += int(seed.get("score_contribution_count") or 0)
                row.runtime_stagecourt_trace_count += int(seed.get("stagecourt_trace_count") or 0)
            if seed.get("symbol") and not targetless_seed:
                row.symbols.add(str(seed["symbol"]))
            if int(seed.get("accepted_claim_count") or 0) > 0 and seed.get("symbol") and not targetless_seed:
                row.accepted_claim_symbols.add(str(seed["symbol"]))
            if seed.get("promoted_to_full_thesis"):
                target_status = seed.get("target_archetype_status")
                if not target_id or target_status in {None, "UNKNOWN", "TARGET_ARCHETYPE_UNKNOWN"}:
                    target_unknown_promoted_count += 1
                    row.promoted_target_unknown_count += 1
                if source_primary_id and not target_id:
                    source_primary_context_promoted_count += 1
                    row.promoted_source_primary_context_count += 1

    for execution in _read_jsonl(output_path / "source_task_executions.jsonl"):
        archetype_id = normalize(execution.get("archetype_id"))
        if not archetype_id:
            candidate_event_id = execution.get("candidate_event_id")
            archetype_id = planner_top1_by_event.get(str(candidate_event_id)) if candidate_event_id else None
        if not archetype_id:
            continue
        row = accumulators[archetype_id]
        execution_symbol = execution.get("symbol")
        targetless_execution = is_placeholder_symbol(execution_symbol)
        if targetless_execution:
            row.targetless_source_task_execution_count += 1
            row.target_materialization_required_seed_count += 1
            continue
        row.runtime_source_task_execution_count += 1
        accepted_count = len(execution.get("accepted_claim_ids") or [])
        row.runtime_source_task_accepted_claim_count += accepted_count
        if execution.get("symbol") and not is_placeholder_symbol(execution.get("symbol")):
            row.symbols.add(str(execution["symbol"]))
            if accepted_count:
                row.accepted_claim_symbols.add(str(execution["symbol"]))

    runner_audit = _read_json(docs_path / "census_mode_v4_full_thesis_production_runner_audit.json")
    for blocked in runner_audit.get("blocked_candidates", []):
        archetype_id = normalize(blocked.get("primary_archetype"))
        if not archetype_id:
            continue
        row = accumulators[archetype_id]
        row.runtime_candidate_attempt_count += 1
        row.runtime_blocked_candidate_count += 1
        row.source_pending_required_or_green_gap_count += int(
            "source_pending_required_or_green_primitives" in set(blocked.get("blockers") or [])
        )
        if blocked.get("symbol") and not is_placeholder_symbol(blocked.get("symbol")):
            row.symbols.add(str(blocked["symbol"]))
            row.blocked_symbols.add(str(blocked["symbol"]))
        if blocked.get("blockers"):
            row.blocker_classes.update(str(value).upper() for value in blocked.get("blockers") or [])

    for follow_up in _read_jsonl(docs_path / "census_mode_v4_full_thesis_blocker_follow_up_source_tasks.jsonl"):
        archetype_id = normalize(follow_up.get("archetype_id") or follow_up.get("follow_up_archetype_id"))
        if not archetype_id:
            continue
        row = accumulators[archetype_id]
        row.runtime_follow_up_source_task_count += 1
        if follow_up.get("symbol") and not is_placeholder_symbol(follow_up.get("symbol")):
            row.symbols.add(str(follow_up["symbol"]))

    stage_map_path = output_path / "census_stage_map.csv"
    if stage_map_path.exists():
        with stage_map_path.open(newline="", encoding="utf-8") as handle:
            for stage_row in csv.DictReader(handle):
                is_full_thesis = (
                    stage_row.get("stage_scope") == "FULL_THESIS"
                    or stage_row.get("operator_stage_use") == "FULL_THESIS_STAGE"
                    or stage_row.get("score_scale") == "FULL_E2R_100"
                    or stage_row.get("full_thesis_score_scale") == "FULL_E2R_100"
                )
                if not is_full_thesis:
                    continue
                archetype_id = normalize(stage_row.get("full_thesis_primary_archetype") or stage_row.get("primary_archetype"))
                if not archetype_id:
                    continue
                row = accumulators[archetype_id]
                row.runtime_candidate_attempt_count += 1
                row.runtime_full_thesis_row_count += 1
                if _parse_listish(stage_row.get("full_thesis_required_positive_missing_primitives")):
                    row.runtime_full_thesis_row_with_required_positive_missing_count += 1
                if _parse_listish(stage_row.get("full_thesis_green_gap_primitives")):
                    row.runtime_full_thesis_row_with_green_gap_count += 1
                if stage_row.get("symbol") and not is_placeholder_symbol(stage_row.get("symbol")):
                    row.symbols.add(str(stage_row["symbol"]))
                    row.full_thesis_symbols.add(str(stage_row["symbol"]))

    rows = [accumulators[archetype_id].to_row(mandatory=archetype_id in mandatory_ids) for archetype_id in contract_ids]
    full_thesis_row_count = sum(row["runtime_full_thesis_row_count"] for row in rows)
    full_thesis_by_arch = {
        row["archetype_id"]: row["runtime_full_thesis_row_count"]
        for row in rows
        if row["runtime_full_thesis_row_count"]
    }
    full_thesis_candidate_attempts_by_arch = {
        row["archetype_id"]: row["runtime_candidate_attempt_count"]
        for row in rows
        if row["runtime_candidate_attempt_count"]
    }
    distinct_full_thesis_archetype_count = len(full_thesis_by_arch)
    attempted_archetype_ids = [row["archetype_id"] for row in rows if row["source_route_status"] != "RESEARCH_REPLAY_ONLY_NOT_RUNTIME_ATTEMPTED" and row["source_route_status"] != "NOT_ATTEMPTED"]
    mandatory_attempted = [row["archetype_id"] for row in rows if row["mandatory_archetype"] and row["source_route_status"] not in {"RESEARCH_REPLAY_ONLY_NOT_RUNTIME_ATTEMPTED", "NOT_ATTEMPTED"}]
    mandatory_full = [row["archetype_id"] for row in rows if row["mandatory_archetype"] and row["runtime_full_thesis_row_count"]]
    required_positive_missing_rows = sum(row["runtime_full_thesis_row_with_required_positive_missing_count"] for row in rows)
    green_gap_rows = sum(row["runtime_full_thesis_row_with_green_gap_count"] for row in rows)
    c05_id = normalize("C05")
    c05_full_thesis_count = full_thesis_by_arch.get(c05_id, 0) if c05_id else 0
    c05_full_thesis_share = (c05_full_thesis_count / full_thesis_row_count) if full_thesis_row_count else 0.0

    production_audit = _read_json(docs_path / "census_mode_v4_full_thesis_production_audit.json")
    production_score_path_pass = (
        full_thesis_row_count > 0
        and target_unknown_promoted_count == 0
        and source_primary_context_promoted_count == 0
    )
    meaningful_pass = (
        production_score_path_pass
        and distinct_full_thesis_archetype_count >= 3
        and len(mandatory_attempted) >= len(mandatory_ids)
        and len(mandatory_full) >= len(mandatory_ids)
        and c05_full_thesis_share <= 0.50
        and required_positive_missing_rows == 0
        and green_gap_rows == 0
    )
    green_ready_pass = meaningful_pass and green_gap_rows == 0
    archetype_balanced_pass = (
        production_score_path_pass
        and distinct_full_thesis_archetype_count >= 6
        and c05_full_thesis_share <= 0.35
        and len(mandatory_full) >= min(len(mandatory_ids), 4)
    )

    blocker_counter = Counter()
    for row in rows:
        blocker_counter.update(row["blocker_classes"])
    summary_blockers: list[str] = []
    if production_score_path_pass and not meaningful_pass:
        summary_blockers.append("PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS")
    if distinct_full_thesis_archetype_count < 3:
        summary_blockers.append("FULL_THESIS_ARCHETYPE_DIVERSITY_BELOW_MINIMUM")
    if c05_full_thesis_share > 0.50:
        summary_blockers.append("C05_FULL_THESIS_MONOCULTURE")
    if len(mandatory_attempted) < len(mandatory_ids):
        summary_blockers.append("MANDATORY_ARCHETYPE_ATTEMPT_COUNT_BELOW_REQUIRED")
    if len(mandatory_full) < len(mandatory_ids):
        summary_blockers.append("MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING")
    if required_positive_missing_rows:
        summary_blockers.append("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS")
    if green_gap_rows:
        summary_blockers.append("GREEN_GAP_ON_PROMOTED_ROWS")
    if target_unknown_promoted_count:
        summary_blockers.append("TARGET_ARCHETYPE_UNKNOWN_PROMOTED")
    if source_primary_context_promoted_count:
        summary_blockers.append("SOURCE_PRIMARY_CONTEXT_PROMOTED")

    final_status = "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS" if meaningful_pass else "MEANINGFUL_RUNTIME_PARITY_NOT_READY"
    labels = [
        "PRODUCTION_FULL_E2R_SCORE_PATH_PASS" if production_score_path_pass else "PRODUCTION_FULL_E2R_SCORE_PATH_PENDING",
        "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS" if meaningful_pass else "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE",
        "GREEN_READY_FULL_THESIS_PASS" if green_ready_pass else "GREEN_READY_FULL_THESIS_PASS_FALSE",
        "ARCHETYPE_BALANCED_FULL_THESIS_PASS" if archetype_balanced_pass else "ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE",
        final_status,
    ]

    return {
        "schema_version": "e2r_research_to_runtime_parity_matrix_v1",
        "as_of_date": as_of_date or replay_matrix.get("as_of_date"),
        "output_root": str(output_path.relative_to(repo_root) if output_path.is_relative_to(repo_root) else output_path),
        "docs_dir": str(docs_path.relative_to(repo_root) if docs_path.is_relative_to(repo_root) else docs_path),
        "registry_archetype_ids": contract_ids,
        "registry_scope_counts": _contract_scope_counts(contract_ids),
        "registry_archetype_count": len(contract_ids),
        "parity_row_count": len(rows),
        "missing_registry_archetype_ids": [archetype_id for archetype_id in contract_ids if archetype_id not in {row["archetype_id"] for row in rows}],
        "mandatory_archetypes": sorted(mandatory_ids),
        "mandatory_archetype_attempt_count": len(mandatory_attempted),
        "mandatory_archetype_attempt_missing": sorted(mandatory_ids - set(mandatory_attempted)),
        "mandatory_archetype_full_thesis_count": len(mandatory_full),
        "mandatory_archetype_full_thesis_missing": sorted(mandatory_ids - set(mandatory_full)),
        "distinct_runtime_attempted_archetype_count": len(set(attempted_archetype_ids)),
        "distinct_full_thesis_archetype_count": distinct_full_thesis_archetype_count,
        "full_thesis_row_count": full_thesis_row_count,
        "full_thesis_candidate_attempts_by_archetype": full_thesis_candidate_attempts_by_arch,
        "full_thesis_by_archetype": full_thesis_by_arch,
        "full_thesis_production_audit_verdict": production_audit.get("verdict"),
        "full_thesis_production_audit_pass_allowed": production_audit.get("production_pass_allowed"),
        "c05_full_thesis_row_count": c05_full_thesis_count,
        "c05_full_thesis_share": round(c05_full_thesis_share, 6),
        "required_positive_missing_full_thesis_row_count": required_positive_missing_rows,
        "required_positive_missing_full_thesis_row_rate": round(
            required_positive_missing_rows / full_thesis_row_count, 6
        )
        if full_thesis_row_count
        else 0.0,
        "green_gap_full_thesis_row_count": green_gap_rows,
        "green_gap_full_thesis_row_rate": round(green_gap_rows / full_thesis_row_count, 6)
        if full_thesis_row_count
        else 0.0,
        "target_archetype_unknown_promoted_count": target_unknown_promoted_count,
        "source_primary_context_promoted_count": source_primary_context_promoted_count,
        "production_full_e2r_score_path_pass": production_score_path_pass,
        "meaningful_full_thesis_evidence_pass": meaningful_pass,
        "green_ready_full_thesis_pass": green_ready_pass,
        "archetype_balanced_full_thesis_pass": archetype_balanced_pass,
        "final_status": final_status,
        "completion_labels": labels,
        "blockers": sorted(set(summary_blockers)),
        "blocker_counts": dict(sorted(blocker_counter.items())),
        "rows": rows,
    }


def render_research_to_runtime_parity_markdown(audit: Mapping[str, Any]) -> str:
    lines = [
        "# Research To Runtime Parity Matrix - 2026-07-05",
        "",
        "이 문서는 연구 replay가 아니라 실제 Census V4 production runtime에서 각 아키타입이 어디까지 갔는지 전수로 보여준다.",
        "",
        "쉬운 예: 병원 전체 검진에서 36개 진료과가 있는데, 결과지가 C05 진료과 10명만 있으면 전체 진료과 검증이 아니다. 이 matrix는 36개 진료과마다 접수, 검사, 판정, 최종 결과지까지 갔는지 한 줄씩 적은 장부다.",
        "",
        "## Summary",
        "",
        f"- final_status: `{audit['final_status']}`",
        f"- registry_archetype_count: `{audit['registry_archetype_count']}`",
        f"- parity_row_count: `{audit['parity_row_count']}`",
        f"- distinct_runtime_attempted_archetype_count: `{audit['distinct_runtime_attempted_archetype_count']}`",
        f"- distinct_full_thesis_archetype_count: `{audit['distinct_full_thesis_archetype_count']}`",
        f"- full_thesis_row_count: `{audit['full_thesis_row_count']}`",
        f"- c05_full_thesis_share: `{audit['c05_full_thesis_share']}`",
        f"- required_positive_missing_full_thesis_row_rate: `{audit['required_positive_missing_full_thesis_row_rate']}`",
        f"- green_gap_full_thesis_row_rate: `{audit['green_gap_full_thesis_row_rate']}`",
        f"- production_full_e2r_score_path_pass: `{audit['production_full_e2r_score_path_pass']}`",
        f"- meaningful_full_thesis_evidence_pass: `{audit['meaningful_full_thesis_evidence_pass']}`",
        f"- archetype_balanced_full_thesis_pass: `{audit['archetype_balanced_full_thesis_pass']}`",
        "",
        "## Labels",
        "",
    ]
    for label in audit.get("completion_labels", []):
        lines.append(f"- `{label}`")
    lines.extend(["", "## Blockers", ""])
    for blocker in audit.get("blockers", []):
        lines.append(f"- `{blocker}`")
    lines.extend(
        [
            "",
            "## Matrix",
            "",
            "| archetype | runtime status | source route | full rows | accepted claims | planner top1 | source exec | blockers |",
            "|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in audit.get("rows", []):
        blockers = ", ".join(row.get("blocker_classes", [])) or "-"
        lines.append(
            "| {archetype} | {status} | {route} | {full} | {claims} | {planner} | {source_exec} | {blockers} |".format(
                archetype=row["archetype_id"],
                status=row["runtime_parity_status"],
                route=row["source_route_status"],
                full=row["runtime_full_thesis_row_count"],
                claims=row["runtime_accepted_claim_count"] + row["runtime_source_task_accepted_claim_count"],
                planner=row["runtime_planner_top1_count"],
                source_exec=row["runtime_source_task_execution_count"],
                blockers=blockers,
            )
        )
    lines.extend(
        [
            "",
            "## Operator Reading",
            "",
            "`PRODUCTION_FULL_E2R_SCORE_PATH_PASS`는 점수 경로가 닫혔다는 뜻이다. 하지만 현재 promoted 행은 모두 required-positive/Green gap이 남아 있으므로 `MEANINGFUL_FULL_THESIS_EVIDENCE_PASS`가 아니다.",
            "",
            "C06 삼성전자 row처럼 production score path까지 올라온 사례도 smoke 점수와 섞으면 안 된다. production row는 production source-backed claim/gap 장부로 읽고, controlled smoke는 별도 진단으로만 읽는다.",
            "",
        ]
    )
    return "\n".join(lines)


def render_research_to_runtime_root_cause_markdown(audit: Mapping[str, Any]) -> str:
    c05_rows = audit.get("full_thesis_by_archetype", {})
    lines = [
        "# Research To Runtime Root Cause - 2026-07-05",
        "",
        "## Verdict",
        "",
        "`FULL_THESIS_PRODUCTION_PASS`라는 예전 라벨은 너무 넓었다. 현재 정확한 라벨은 `PRODUCTION_FULL_E2R_SCORE_PATH_PASS`이고, `MEANINGFUL_FULL_THESIS_EVIDENCE_PASS=false`다.",
        "",
        "쉬운 예: 예전에는 한 과목(C05) 시험지만 10장 채점된 상태였고, 현재는 7개 과목의 시험지가 채점대에 올라왔다. 하지만 7개 모두 필수 증빙칸이 비어 있어 전체 과목 합격은 아니다.",
        "",
        "## Current Facts",
        "",
        f"- full_thesis_row_count: `{audit['full_thesis_row_count']}`",
        f"- full_thesis_by_archetype: `{json.dumps(c05_rows, ensure_ascii=False, sort_keys=True)}`",
        f"- distinct_full_thesis_archetype_count: `{audit['distinct_full_thesis_archetype_count']}`",
        f"- c05_full_thesis_share: `{audit['c05_full_thesis_share']}`",
        f"- required_positive_missing_full_thesis_row_count: `{audit['required_positive_missing_full_thesis_row_count']}`",
        f"- green_gap_full_thesis_row_count: `{audit['green_gap_full_thesis_row_count']}`",
        f"- target_archetype_unknown_promoted_count: `{audit['target_archetype_unknown_promoted_count']}`",
        f"- source_primary_context_promoted_count: `{audit['source_primary_context_promoted_count']}`",
        "",
        "## Six Audit Questions",
        "",
        "1. 왜 예전 production FULL_THESIS 10개가 전부 C05였고, 현재는 어떻게 바뀌었나?",
        "   - 예전 seed target은 UNKNOWN이었고 source_primary/planner top1 경로가 C05로 쏠렸다. 현재 promoted row는 C01/C03/C05/C06/C08/C17/C28 7개 아키타입으로 분산됐다.",
        "2. target_archetype_counts가 UNKNOWN인데 왜 C05가 되는가?",
        "   - 예전에는 target이 아니라 event-board/refresh queue의 source_primary 문맥과 planner top1이 최종 primary가 됐다. 현재 promoted row의 target_archetype_unknown_promoted_count는 0이다.",
        "3. 27.9998 / 77.9998 점수는 어디서 나오는가?",
        "   - C05 weight profile에 raw component를 clamp 후 재가중한 FULL_E2R_100 score path에서 나온다.",
        "4. C05가 아닌 후보는 왜 0개인가?",
        "   - 이 질문은 예전 C05-only 산출물에 대한 질문이다. 현재는 C01/C03/C06/C08/C17/C28 non-C05 score-path row가 생겼고, C15/C24는 아직 mandatory full-thesis missing이다.",
        "5. required_positive_missing_primitives가 있는데 왜 pass인가?",
        "   - 기존 pass는 score path closed만 봤기 때문이다. meaningful pass는 required-positive gap을 허용하면 안 된다.",
        "6. 삼성전자/하이닉스는 왜 production row가 아닌가?",
        "   - 현재 삼성전자 005930은 C06 production score-path row가 생겼지만 required-positive/Green gap 때문에 meaningful pass가 아니다. 하이닉스 controlled smoke는 여전히 production full-thesis row와 분리해서 본다.",
        "",
        "## Required Direction",
        "",
        "C05 하나가 아니라 C01~C32와 R13 cross-archetype 4개, 총 36개 contract에 대해 attempt, source route, accepted claim, StageCourt, full-thesis 상태를 계속 이 matrix로 증명해야 한다.",
        "",
    ]
    return "\n".join(lines)


def render_research_to_runtime_acceptance_report(
    *,
    parity_audit: Mapping[str, Any],
    research_inventory: Mapping[str, Any],
    memory_cards: Mapping[str, Any],
    source_routes: Mapping[str, Any],
    followup_audit: Mapping[str, Any],
    candidate_selection: Mapping[str, Any],
    planner_bias: Mapping[str, Any],
    all_status_matrix: Mapping[str, Any],
    next_attempt_plan: Mapping[str, Any],
    execution_manifest: Mapping[str, Any],
) -> str:
    quality = research_inventory.get("source_quality_counts", {})
    c06_rows = [
        row
        for row in parity_audit.get("rows", [])
        if str(row.get("archetype_id", "")).startswith("C06_")
    ]
    c06_full_thesis_symbols = sorted(
        {
            symbol
            for row in c06_rows
            for symbol in row.get("full_thesis_symbols", [])
        }
    )
    c06_gap_summary = ", ".join(
        sorted(
            {
                blocker
                for row in c06_rows
                for blocker in row.get("blocker_classes", [])
                if blocker
            }
        )
    ) or "none"
    lines = [
        "# Research To Runtime Acceptance Report - 2026-07-05",
        "",
        "## Verdict",
        "",
        f"- final_status: `{parity_audit['final_status']}`",
        f"- production_full_e2r_score_path_pass: `{parity_audit['production_full_e2r_score_path_pass']}`",
        f"- meaningful_full_thesis_evidence_pass: `{parity_audit['meaningful_full_thesis_evidence_pass']}`",
        f"- archetype_balanced_full_thesis_pass: `{parity_audit['archetype_balanced_full_thesis_pass']}`",
        "",
        "쉬운 예: 이제 C05 한 과목만 채점된 상태는 벗어났고 7개 과목의 score path는 닫혔다. 하지만 7개 모두 필수 증빙칸과 Green 증빙칸이 비어 있어 최종 합격증은 아직 아니다.",
        "",
        "## Required Metrics",
        "",
        f"- research case count: `{research_inventory.get('record_count')}`",
        f"- source quality breakdown: `{json.dumps(quality, ensure_ascii=False, sort_keys=True)}`",
        f"- URL-backed replay count: `{quality.get('A2_URL_BACKED', 0)}`",
        f"- source-proxy-only repair count: `{quality.get('SOURCE_PROXY_ONLY', 0)}`",
        f"- archetype memory card count: `{memory_cards.get('card_count')}`",
        f"- source route pattern count: `{source_routes.get('pattern_count')}`",
        f"- source route gap task count: `{source_routes.get('gap_task_count')}`",
        f"- full-thesis candidate attempts by archetype: `{json.dumps(parity_audit.get('full_thesis_candidate_attempts_by_archetype', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- promoted full-thesis rows by archetype: `{json.dumps(parity_audit.get('full_thesis_by_archetype', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- required positive missing rate: `{parity_audit.get('required_positive_missing_full_thesis_row_rate')}`",
        f"- green gap rate: `{parity_audit.get('green_gap_full_thesis_row_rate')}`",
        f"- distinct archetype count: `{parity_audit.get('distinct_full_thesis_archetype_count')}`",
        f"- C05 share: `{parity_audit.get('c05_full_thesis_share')}`",
        f"- planner C05 top1 share: `{planner_bias.get('c05_top1_share')}`",
        f"- research memory follow-up task count: `{followup_audit.get('task_count')}`",
        f"- research memory follow-up by archetype: `{json.dumps(followup_audit.get('tasks_by_archetype', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- all-archetype runtime status rows: `{all_status_matrix.get('registry_contract_count')}`",
        f"- canonical C contract rows: `{all_status_matrix.get('canonical_c_archetype_count')}`",
        f"- cross-archetype rows: `{all_status_matrix.get('cross_archetype_contract_count')}`",
        f"- registry scope counts: `{json.dumps(all_status_matrix.get('registry_scope_counts', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- exact registry row coverage: `{all_status_matrix.get('all_registered_archetypes_have_exactly_one_runtime_status_row')}`",
        f"- missing parity source rows: `{all_status_matrix.get('missing_parity_source_row_count')}`",
        f"- duplicate parity source rows: `{all_status_matrix.get('duplicate_parity_source_row_count')}`",
        f"- extra parity source rows: `{all_status_matrix.get('extra_parity_source_row_count')}`",
        f"- all contracts have memory card: `{all_status_matrix.get('all_contracts_have_memory_card')}`",
        f"- all contracts have source route patterns: `{all_status_matrix.get('all_contracts_have_source_route_patterns')}`",
        f"- runtime proof counts: `{json.dumps(all_status_matrix.get('runtime_parity_proof_status_counts', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- next runtime attempt plan rows: `{next_attempt_plan.get('plan_row_count')}`",
        f"- next runtime source task shells: `{next_attempt_plan.get('source_task_count')}`",
        f"- next runtime seed events: `{next_attempt_plan.get('seed_event_count')}`",
        f"- next runtime attempt types: `{json.dumps(next_attempt_plan.get('attempt_type_counts', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- runtime execution manifest status: `{execution_manifest.get('execution_status')}`",
        f"- runtime execution seed path: `{execution_manifest.get('seed_event_path')}`",
        f"- runtime execution command target gate: `{(execution_manifest.get('census_v4_config_kwargs') or {}).get('target_gate')}`",
        "",
        "## Production Vs Smoke",
        "",
        f"C06 production score-path symbols: `{', '.join(c06_full_thesis_symbols) if c06_full_thesis_symbols else 'none'}`",
        f"C06 remaining production blockers: `{c06_gap_summary}`",
        "",
        "삼성전자처럼 production score path까지 올라온 row도 controlled smoke와 섞으면 안 된다. production row는 source-backed claim/gap 장부 기준으로 읽고, smoke 점수는 파이프라인 반응을 보는 진단값으로만 본다.",
        "",
        "쉬운 예: 삼성전자 production row는 실제 시험장 답안지이고, controlled smoke는 모의고사 답안지다. 실제 답안지가 있어도 필수 첨부서류가 빠졌으면 합격이 아니고, 모의고사 점수로 합격 처리하면 안 된다.",
        "",
        "## Blockers",
        "",
    ]
    for blocker in parity_audit.get("blockers", []):
        lines.append(f"- `{blocker}`")
    for blocker in candidate_selection.get("blockers", []):
        lines.append(f"- candidate_selection: `{blocker}`")
    for blocker in planner_bias.get("blockers", []):
        lines.append(f"- planner_bias: `{blocker}`")
    lines.append("")
    return "\n".join(lines)


def render_research_to_runtime_readiness_verdict(
    *,
    parity_audit: Mapping[str, Any],
    candidate_selection: Mapping[str, Any],
    planner_bias: Mapping[str, Any],
) -> str:
    labels = ", ".join(f"`{label}`" for label in parity_audit.get("completion_labels", []))
    return "\n".join(
        [
            "# Research To Runtime Readiness Verdict - 2026-07-05",
            "",
            f"- final_verdict: `{parity_audit['final_status']}`",
            f"- labels: {labels}",
            f"- candidate_selection_status: `{candidate_selection.get('status')}`",
            f"- planner_bias_status: `{planner_bias.get('status')}`",
            f"- meaningful_ready: `{parity_audit.get('meaningful_full_thesis_evidence_pass')}`",
            "",
            "현재 상태는 implementation/audit progress이지 goal4 complete가 아니다. C05-only 편중은 완화됐지만, C01~C36 runtime parity와 meaningful full thesis는 아직 required-positive/Green gap 때문에 통과하지 않았다.",
            "",
        ]
    )


def build_meaningful_full_thesis_acceptance_audit(
    *,
    parity_audit: Mapping[str, Any],
    candidate_selection: Mapping[str, Any],
    planner_bias: Mapping[str, Any],
    replay_matrix: Mapping[str, Any],
) -> dict[str, Any]:
    hard_fails: list[str] = []
    if parity_audit.get("distinct_full_thesis_archetype_count", 0) < 3:
        hard_fails.append("distinct_full_thesis_archetype_count_below_3")
    if parity_audit.get("c05_full_thesis_share", 0) > 0.50:
        hard_fails.append("c05_share_above_50_percent")
    if parity_audit.get("mandatory_archetype_full_thesis_missing"):
        hard_fails.append("mandatory_archetype_full_thesis_missing")
    if parity_audit.get("required_positive_missing_full_thesis_row_count", 0) > 0:
        hard_fails.append("required_positive_missing_any_promoted_row")
    if parity_audit.get("green_gap_full_thesis_row_count", 0) > 0:
        hard_fails.append("green_gap_any_promoted_row")
    if parity_audit.get("target_archetype_unknown_promoted_count", 0):
        hard_fails.append("target_archetype_unknown_promoted")
    if parity_audit.get("source_primary_context_promoted_count", 0):
        hard_fails.append("source_primary_context_only_promoted")
    if planner_bias.get("status") != "PLANNER_ARCHETYPE_ROUTING_BIAS_PASS":
        hard_fails.append("planner_bias_audit_not_pass")
    if replay_matrix.get("production_score_leak_count", 0):
        hard_fails.append("research_replay_leaked_to_production_score")
    if not replay_matrix.get("all_source_proxy_cases_planning_only"):
        hard_fails.append("source_proxy_case_not_planning_only")
    if candidate_selection.get("status") != "BALANCED_FULL_THESIS_SELECTION_PASS":
        hard_fails.append("balanced_candidate_selection_not_pass")

    meaningful_pass = not hard_fails
    archetype_balanced_pass = bool(parity_audit.get("archetype_balanced_full_thesis_pass"))
    return {
        "schema_version": "e2r_meaningful_full_thesis_production_acceptance_v1",
        "score_path_status": "PRODUCTION_FULL_E2R_SCORE_PATH_PASS"
        if parity_audit.get("production_full_e2r_score_path_pass")
        else "PRODUCTION_FULL_E2R_SCORE_PATH_PENDING",
        "meaningful_status": "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS"
        if meaningful_pass
        else "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE",
        "archetype_balanced_status": "ARCHETYPE_BALANCED_FULL_THESIS_PASS"
        if archetype_balanced_pass
        else "ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE",
        "candidate_selection_status": candidate_selection.get("status"),
        "meaningful_pass_allowed": meaningful_pass,
        "hard_fails": hard_fails,
        "distinct_full_thesis_archetype_count": parity_audit.get("distinct_full_thesis_archetype_count"),
        "mandatory_archetype_attempt_count": parity_audit.get("mandatory_archetype_attempt_count"),
        "mandatory_archetype_full_thesis_count": parity_audit.get("mandatory_archetype_full_thesis_count"),
        "mandatory_archetype_full_thesis_missing": parity_audit.get("mandatory_archetype_full_thesis_missing", []),
        "c05_full_thesis_share": parity_audit.get("c05_full_thesis_share"),
        "required_positive_missing_row_count": parity_audit.get("required_positive_missing_full_thesis_row_count"),
        "required_positive_missing_rate": parity_audit.get("required_positive_missing_full_thesis_row_rate"),
        "green_gap_row_count": parity_audit.get("green_gap_full_thesis_row_count"),
        "green_gap_rate": parity_audit.get("green_gap_full_thesis_row_rate"),
        "source_primary_context_only_promoted_count": parity_audit.get("source_primary_context_promoted_count"),
        "target_archetype_unknown_promoted_count": parity_audit.get("target_archetype_unknown_promoted_count"),
        "research_replay_production_score_leak_count": replay_matrix.get("production_score_leak_count"),
        "source_proxy_repair_task_count": replay_matrix.get("source_proxy_repair_task_count"),
    }


def write_research_to_runtime_parity_artifacts(
    *,
    repo_root: str | Path = ".",
    output_root: str | Path | None = None,
    docs_dir: str | Path = "docs/operational",
    as_of_date: str | None = None,
    mandatory_archetype_prefixes: Sequence[str] = DEFAULT_MANDATORY_ARCHETYPE_PREFIXES,
) -> dict[str, Any]:
    from e2r.census.all_archetype_next_attempt_planner import write_all_archetype_next_runtime_attempt_plan
    from e2r.census.all_archetype_runtime_execution_manifest import write_all_archetype_runtime_execution_manifest
    from e2r.census.all_archetype_runtime_status_matrix import write_all_archetype_runtime_status_matrix
    from e2r.census.full_thesis_candidate_selector import write_balanced_full_thesis_candidate_selection_audit
    from e2r.census.research_memory_followup_planner import write_research_memory_followup_task_audit
    from e2r.census.research_to_runtime_replay import write_research_to_runtime_replay_reports
    from e2r.research_reverse.reports import write_research_reverse_bundle
    from e2r.research_brain.planner_bias_audit import write_planner_bias_audit
    from e2r.source_routing.research_source_route_recovery import write_source_route_recovery_reports

    repo_root = Path(repo_root).resolve()
    docs_path = Path(docs_dir)
    docs_path = docs_path if docs_path.is_absolute() else repo_root / docs_path
    audit = build_research_to_runtime_parity_audit(
        repo_root=repo_root,
        output_root=output_root,
        docs_dir=docs_path,
        as_of_date=as_of_date,
        mandatory_archetype_prefixes=mandatory_archetype_prefixes,
    )
    matrix_path = docs_path / "research_to_runtime_parity_matrix_2026-07-05.json"
    summary_path = docs_path / "research_to_runtime_parity_matrix_2026-07-05.md"
    root_cause_path = docs_path / "research_to_runtime_root_cause_2026-07-05.md"
    v2_audit_path = docs_path / "census_mode_v4_full_thesis_evidence_completion_audit_v2.json"
    _write_json(matrix_path, audit)
    summary_path.write_text(render_research_to_runtime_parity_markdown(audit), encoding="utf-8")
    root_cause_path.write_text(render_research_to_runtime_root_cause_markdown(audit), encoding="utf-8")
    _write_json(
        v2_audit_path,
        {
            "schema_version": "e2r_census_v4_full_thesis_evidence_completion_audit_v2",
            "score_path_status": "PRODUCTION_FULL_E2R_SCORE_PATH_PASS"
            if audit["production_full_e2r_score_path_pass"]
            else "PRODUCTION_FULL_E2R_SCORE_PATH_PENDING",
            "meaningful_evidence_status": "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS"
            if audit["meaningful_full_thesis_evidence_pass"]
            else "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE",
            "green_ready_status": "GREEN_READY_FULL_THESIS_PASS"
            if audit["green_ready_full_thesis_pass"]
            else "GREEN_READY_FULL_THESIS_PASS_FALSE",
            "archetype_balanced_status": "ARCHETYPE_BALANCED_FULL_THESIS_PASS"
            if audit["archetype_balanced_full_thesis_pass"]
            else "ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE",
            "full_thesis_row_count": audit["full_thesis_row_count"],
            "distinct_full_thesis_archetype_count": audit["distinct_full_thesis_archetype_count"],
            "c05_full_thesis_share": audit["c05_full_thesis_share"],
            "required_positive_missing_full_thesis_row_count": audit[
                "required_positive_missing_full_thesis_row_count"
            ],
            "green_gap_full_thesis_row_count": audit["green_gap_full_thesis_row_count"],
            "blockers": audit["blockers"],
            "matrix_path": str(matrix_path.relative_to(repo_root)),
            "root_cause_path": str(root_cause_path.relative_to(repo_root)),
        },
    )
    research_reverse_bundle = write_research_reverse_bundle(repo_root=repo_root, docs_dir=docs_path)
    source_route_reports = write_source_route_recovery_reports(
        repo_root=repo_root,
        docs_dir=docs_path,
        records=research_reverse_bundle["inventory"]["records"],
    )
    followup_audit = write_research_memory_followup_task_audit(docs_dir=docs_path)
    replay_reports = write_research_to_runtime_replay_reports(
        repo_root=repo_root,
        output_root=output_root,
        docs_dir=docs_path,
    )
    candidate_selection_audit = write_balanced_full_thesis_candidate_selection_audit(
        audit,
        docs_dir=docs_path,
        mandatory_prefixes=mandatory_archetype_prefixes,
    )
    all_status_reports = write_all_archetype_runtime_status_matrix(
        parity_audit=audit,
        memory_cards=research_reverse_bundle["cards"],
        source_routes=source_route_reports["source_route_matrix"],
        candidate_selection=candidate_selection_audit,
        research_inventory=research_reverse_bundle["inventory"],
        docs_dir=docs_path,
    )
    next_attempt_reports = write_all_archetype_next_runtime_attempt_plan(
        status_matrix=all_status_reports["matrix"],
        memory_cards=research_reverse_bundle["cards"],
        docs_dir=docs_path,
    )
    execution_manifest_reports = write_all_archetype_runtime_execution_manifest(
        next_attempt_plan=next_attempt_reports["plan"],
        seed_event_path=next_attempt_reports["seed_event_path"],
        source_task_path=next_attempt_reports["source_task_path"],
        docs_dir=docs_path,
        repo_root=repo_root,
    )
    planner_bias_audit = write_planner_bias_audit(
        repo_root=repo_root,
        output_root=output_root,
        docs_dir=docs_path,
        parity_audit=audit,
    )
    meaningful_acceptance = build_meaningful_full_thesis_acceptance_audit(
        parity_audit=audit,
        candidate_selection=candidate_selection_audit,
        planner_bias=planner_bias_audit,
        replay_matrix=replay_reports["replay_matrix"],
    )
    meaningful_acceptance_path = docs_path / "meaningful_full_thesis_production_acceptance.json"
    meaningful_acceptance_path.write_text(
        json.dumps(meaningful_acceptance, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # Goal4 canonical filenames.  Keep the dated/source-specific files too, but
    # write stable aliases so downstream agents and tests do not need to guess.
    (docs_path / "full_thesis_candidate_selection_audit_v2.json").write_text(
        json.dumps(candidate_selection_audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (docs_path / "planner_bias_and_archetype_routing_audit.json").write_text(
        json.dumps(planner_bias_audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (docs_path / "full_thesis_evidence_completion_audit_v2.json").write_text(
        (docs_path / "census_mode_v4_full_thesis_evidence_completion_audit_v2.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    acceptance_report_path = docs_path / "research_to_runtime_acceptance_report.md"
    readiness_verdict_path = docs_path / "research_to_runtime_readiness_verdict.md"
    acceptance_report_path.write_text(
        render_research_to_runtime_acceptance_report(
            parity_audit=audit,
            research_inventory=research_reverse_bundle["inventory"],
            memory_cards=research_reverse_bundle["cards"],
            source_routes=source_route_reports["source_route_matrix"],
            followup_audit=followup_audit,
            candidate_selection=candidate_selection_audit,
            planner_bias=planner_bias_audit,
            all_status_matrix=all_status_reports["matrix"],
            next_attempt_plan=next_attempt_reports["plan"],
            execution_manifest=execution_manifest_reports["manifest"],
        ),
        encoding="utf-8",
    )
    readiness_verdict_path.write_text(
        render_research_to_runtime_readiness_verdict(
            parity_audit=audit,
            candidate_selection=candidate_selection_audit,
            planner_bias=planner_bias_audit,
        ),
        encoding="utf-8",
    )
    return {
        "audit": audit,
        "matrix_path": matrix_path,
        "summary_path": summary_path,
        "root_cause_path": root_cause_path,
        "v2_audit_path": v2_audit_path,
        "research_reverse_bundle": research_reverse_bundle,
        "source_route_reports": source_route_reports,
        "followup_audit": followup_audit,
        "replay_reports": replay_reports,
        "candidate_selection_audit": candidate_selection_audit,
        "all_status_reports": all_status_reports,
        "next_attempt_reports": next_attempt_reports,
        "execution_manifest_reports": execution_manifest_reports,
        "planner_bias_audit": planner_bias_audit,
        "meaningful_acceptance": meaningful_acceptance,
        "meaningful_acceptance_path": meaningful_acceptance_path,
        "acceptance_report_path": acceptance_report_path,
        "readiness_verdict_path": readiness_verdict_path,
    }


__all__ = [
    "DEFAULT_MANDATORY_ARCHETYPE_PREFIXES",
    "build_research_to_runtime_parity_audit",
    "render_research_to_runtime_parity_markdown",
    "render_research_to_runtime_root_cause_markdown",
    "write_research_to_runtime_parity_artifacts",
]
