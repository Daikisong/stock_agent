"""Canonical two-pass Research Brain execution for selected live candidates."""

from __future__ import annotations

import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.intelligence_schema import (
    MemoryEdge,
    MemoryNode,
    PlannerStatus,
    ResearchMemoryGraph,
    SemanticMemoryIndexEntry,
    TwoPassPlan,
)
from e2r.research_brain.planning import (
    TwoPassPlannerProvider,
    build_codex_two_pass_planner_provider,
    compile_blind_hypothesis_input,
    run_two_pass_planner,
)
from e2r.research_brain.retrieval import SemanticMemoryIndex

from .baseline_materializer import BaselineLaneRecord
from .current_state_store import CurrentStateRecord
from .depth_selector import LiveDepthDecision
from .trigger_fusion import CandidateEvent, TriggerSignal, TriggerType


LIVE_PLANNER_RUN_SCHEMA_VERSION = "e2r_live_planner_run_v1"
_FORBIDDEN_RESPONSE_KEY_RE = re.compile(r"(?:^|_)(?:score|stage)(?:$|_)", re.IGNORECASE)
_FORBIDDEN_PROMPT_LEAK_RE = re.compile(
    r"(?:mfe(?:[_-]?\d+)?|mae(?:[_-]?\d+)?|historical[_ -]?outcome|"
    r"future[_ -]?outcome|outcome[_ -]?label|expected[_ -]?stage)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class BrainPlannerConfig:
    as_of_date: str
    max_brain_candidates: int
    max_llm_calls_per_candidate: int
    memory_root: str = "output/research_intelligence/v1"
    max_parallel_candidates: int = 4
    attempt_id: str = "initial"
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if self.max_brain_candidates <= 0:
            raise ValueError("Brain candidate budget must be bounded and positive")
        if self.max_llm_calls_per_candidate < 2:
            raise ValueError("canonical two-pass planner requires at least two calls per candidate")
        if self.max_parallel_candidates <= 0 or self.max_parallel_candidates > 8:
            raise ValueError("parallel Brain candidate count must be bounded by 8")
        if not self.attempt_id.strip():
            raise ValueError("Brain planner attempt ID is required")


@dataclass(frozen=True)
class LivePlannerRun:
    planner_run_id: str
    target_id: str
    target_name: str
    as_of_date: str
    depth_decision_id: str
    candidate_event_id: str
    trigger_signal_ids: tuple[str, ...]
    source_refs: tuple[str, ...]
    blind_input_id: str
    compiled_fact_count: int
    input_compilation_audit: Mapping[str, int]
    provider_name: str
    provider_real: bool
    provider_fake: bool
    provider_call_count: int
    real_provider_success: bool
    terminal_status: str
    plan: TwoPassPlan
    schema_version: str = LIVE_PLANNER_RUN_SCHEMA_VERSION

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        PlannerStatus(self.terminal_status)
        if not all(
            (
                self.planner_run_id.strip(),
                self.target_id.strip(),
                self.target_name.strip(),
                self.depth_decision_id.strip(),
                self.candidate_event_id.strip(),
                self.blind_input_id.strip(),
                self.provider_name.strip(),
            )
        ):
            raise ValueError("live planner run identity required")
        if not self.trigger_signal_ids or not self.source_refs or self.compiled_fact_count <= 0:
            raise ValueError("live planner run requires current source-backed facts")
        if self.provider_real and self.provider_fake:
            raise ValueError("planner provider cannot be both real and fake")
        if self.provider_call_count < 0:
            raise ValueError("planner call count cannot be negative")
        if self.real_provider_success and (
            not self.provider_real or self.terminal_status == PlannerStatus.PENDING.value
        ):
            raise ValueError("real planner success label is inconsistent")
        if self.plan.blind_input_id != self.blind_input_id:
            raise ValueError("live planner run input/plan mismatch")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "trigger_signal_ids": list(self.trigger_signal_ids),
            "source_refs": list(self.source_refs),
            "input_compilation_audit": dict(self.input_compilation_audit),
            "plan": self.plan.to_dict(),
        }


@dataclass(frozen=True)
class BrainPlannerRunResult:
    as_of_date: str
    status: str
    planner_runs: tuple[LivePlannerRun, ...]
    prompt_rows: tuple[Mapping[str, Any], ...]
    response_rows: tuple[Mapping[str, Any], ...]
    memory_metadata: Mapping[str, Any]
    audit: Mapping[str, Any]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)


@dataclass
class RecordingTwoPassPlannerProvider(TwoPassPlannerProvider):
    base: TwoPassPlannerProvider
    target_id: str
    attempt_id: str
    prompt_rows: list[Mapping[str, Any]]
    response_rows: list[Mapping[str, Any]]

    @property
    def provider_name(self) -> str:
        return self.base.provider_name

    @property
    def real_provider(self) -> bool:
        return bool(self.base.real_provider)

    @property
    def fake_provider(self) -> bool:
        return bool(self.base.fake_provider)

    def complete(
        self,
        *,
        planner_pass: str,
        prompt: str,
        output_schema: Mapping[str, Any],
    ):
        prompt_hash = _sha256_text(prompt)
        call_id = "LLMCALL-" + stable_hash(
            {
                "target": self.target_id,
                "attempt_id": self.attempt_id,
                "planner_pass": planner_pass,
                "prompt_hash": prompt_hash,
            }
        )[:24]
        self.prompt_rows.append(
            {
                "schema_version": "e2r_live_llm_prompt_v1",
                "call_id": call_id,
                "target_id": self.target_id,
                "attempt_id": self.attempt_id,
                "planner_pass": planner_pass,
                "provider_name": self.provider_name,
                "prompt_hash": prompt_hash,
                "prompt_text": prompt,
            }
        )
        try:
            completion = self.base.complete(
                planner_pass=planner_pass,
                prompt=prompt,
                output_schema=output_schema,
            )
        except Exception as exc:
            self.response_rows.append(
                {
                    "schema_version": "e2r_live_llm_response_v1",
                    "call_id": call_id,
                    "target_id": self.target_id,
                    "attempt_id": self.attempt_id,
                    "planner_pass": planner_pass,
                    "provider_name": self.provider_name,
                    "status": "PROVIDER_ERROR",
                    "response_hash": _sha256_text(type(exc).__name__),
                    "response_payload": {},
                    "error_category": type(exc).__name__,
                }
            )
            raise
        self.response_rows.append(
            {
                "schema_version": "e2r_live_llm_response_v1",
                "call_id": call_id,
                "target_id": self.target_id,
                "attempt_id": self.attempt_id,
                "planner_pass": planner_pass,
                "provider_name": self.provider_name,
                "status": "COMPLETED",
                "response_hash": _sha256_text(completion.raw_response),
                "response_payload": dict(completion.payload),
                "raw_response": completion.raw_response,
                "error_category": None,
            }
        )
        return completion


class CurrentBrainPlannerRunner:
    def run(
        self,
        config: BrainPlannerConfig,
        *,
        depth_decisions: Sequence[LiveDepthDecision],
        candidate_events: Sequence[CandidateEvent],
        trigger_signals: Sequence[TriggerSignal],
        baseline_lanes: Sequence[BaselineLaneRecord],
        current_state: Sequence[CurrentStateRecord],
        provider: TwoPassPlannerProvider | None = None,
        memory_index: SemanticMemoryIndex | None = None,
    ) -> BrainPlannerRunResult:
        selected = tuple(
            sorted(
                (item for item in depth_decisions if item.selected_for_brain),
                key=lambda item: (-item.priority_score, item.target_id),
            )
        )
        if len(selected) > config.max_brain_candidates:
            raise ValueError("selected Brain targets exceed configured budget")
        candidates = _unique_by_target(candidate_events, "candidate event")
        signals_by_id = _unique_by_id(
            trigger_signals,
            key="trigger_signal_id",
            context="trigger signal",
        )
        lanes_by_target: dict[str, list[BaselineLaneRecord]] = {}
        for lane in baseline_lanes:
            lanes_by_target.setdefault(lane.target_id, []).append(lane)
        state_by_target = _unique_by_target(current_state, "current state")
        effective_memory, memory_metadata = (
            (memory_index, _in_memory_metadata(memory_index))
            if memory_index is not None
            else load_canonical_semantic_memory_index(config.memory_root)
        )
        effective_provider = provider or build_codex_two_pass_planner_provider(
            working_directory=Path.cwd(),
        )
        jobs: list[
            tuple[
                LiveDepthDecision,
                CandidateEvent,
                tuple[TriggerSignal, ...],
            ]
        ] = []
        for decision in selected:
            candidate = candidates.get(decision.target_id)
            if candidate is None or candidate.candidate_event_id != decision.candidate_event_id:
                raise ValueError("selected Brain target lacks its exact candidate event")
            target_signals = tuple(
                signals_by_id[signal_id]
                for signal_id in candidate.trigger_signal_ids
                if signal_id in signals_by_id
            )
            if len(target_signals) != len(candidate.trigger_signal_ids):
                raise ValueError("selected Brain candidate has missing trigger lineage")
            jobs.append((decision, candidate, target_signals))

        def execute(job):
            decision, candidate, target_signals = job
            return _execute_planner_candidate(
                config=config,
                decision=decision,
                candidate=candidate,
                signals=target_signals,
                lanes=lanes_by_target.get(decision.target_id, ()),
                current_state=state_by_target.get(decision.target_id),
                memory_index=effective_memory,
                provider=effective_provider,
            )

        if len(jobs) <= 1 or config.max_parallel_candidates == 1:
            completed = tuple(execute(job) for job in jobs)
        else:
            with ThreadPoolExecutor(
                max_workers=min(config.max_parallel_candidates, len(jobs)),
                thread_name_prefix="e2r-brain",
            ) as executor:
                completed = tuple(executor.map(execute, jobs))
        runs = [item[0] for item in completed]
        prompt_rows = [row for item in completed for row in item[1]]
        response_rows = [row for item in completed for row in item[2]]
        audit = _audit_brain_planner(
            as_of_date=config.as_of_date,
            selected=selected,
            runs=tuple(runs),
            prompt_rows=tuple(prompt_rows),
            response_rows=tuple(response_rows),
        )
        return BrainPlannerRunResult(
            as_of_date=config.as_of_date,
            status=(
                "CURRENT_BRAIN_PLANNER_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_BRAIN_PLANNER_FAIL"
            ),
            planner_runs=tuple(runs),
            prompt_rows=tuple(prompt_rows),
            response_rows=tuple(response_rows),
            memory_metadata=memory_metadata,
            audit=audit,
        )


def _execute_planner_candidate(
    *,
    config: BrainPlannerConfig,
    decision: LiveDepthDecision,
    candidate: CandidateEvent,
    signals: Sequence[TriggerSignal],
    lanes: Sequence[BaselineLaneRecord],
    current_state: CurrentStateRecord | None,
    memory_index: SemanticMemoryIndex,
    provider: TwoPassPlannerProvider,
) -> tuple[
    LivePlannerRun,
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
]:
    evidence_rows = _planner_evidence_rows(
        candidate=candidate,
        signals=signals,
        lanes=lanes,
        current_state=current_state,
    )
    compiled = compile_blind_hypothesis_input(
        target_id=decision.target_id,
        target_name=decision.target_name,
        target_aliases=(),
        as_of_date=config.as_of_date,
        evidence_rows=evidence_rows,
        sector_context=(),
    )
    prompt_rows: list[Mapping[str, Any]] = []
    response_rows: list[Mapping[str, Any]] = []
    recording = RecordingTwoPassPlannerProvider(
        base=provider,
        target_id=decision.target_id,
        attempt_id=config.attempt_id,
        prompt_rows=prompt_rows,
        response_rows=response_rows,
    )
    plan = run_two_pass_planner(
        blind_input=compiled.blind_input,
        memory_index=memory_index,
        provider=recording,
        test_mode=config.test_mode,
    )
    call_count = len(response_rows)
    if call_count > config.max_llm_calls_per_candidate:
        raise ValueError("planner exceeded per-candidate LLM call budget")
    run = LivePlannerRun(
        planner_run_id="LIVEPLAN-"
        + stable_hash(
            {
                "target": decision.target_id,
                "blind_input": compiled.blind_input.input_id,
                "plan": plan.plan_id,
            }
        )[:24],
        target_id=decision.target_id,
        target_name=decision.target_name,
        as_of_date=config.as_of_date,
        depth_decision_id=decision.depth_decision_id,
        candidate_event_id=candidate.candidate_event_id,
        trigger_signal_ids=tuple(candidate.trigger_signal_ids),
        source_refs=tuple(candidate.source_refs),
        blind_input_id=compiled.blind_input.input_id,
        compiled_fact_count=len(compiled.blind_input.current_facts),
        input_compilation_audit=compiled.audit,
        provider_name=recording.provider_name,
        provider_real=recording.real_provider,
        provider_fake=recording.fake_provider,
        provider_call_count=call_count,
        real_provider_success=(
            recording.real_provider and plan.status != PlannerStatus.PENDING.value
        ),
        terminal_status=plan.status,
        plan=plan,
    )
    return run, tuple(prompt_rows), tuple(response_rows)


def load_canonical_semantic_memory_index(
    memory_root: str | Path,
) -> tuple[SemanticMemoryIndex, Mapping[str, Any]]:
    root = Path(memory_root) / "retrieval"
    paths = {
        "manifest": root / "semantic_memory_manifest.json",
        "nodes": root / "research_memory_nodes.jsonl",
        "edges": root / "research_memory_edges.jsonl",
        "index": root / "semantic_memory_index.jsonl",
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError("canonical semantic memory artifacts missing: " + ",".join(missing))
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    nodes = tuple(MemoryNode(**row) for row in _read_jsonl(paths["nodes"]))
    edges = tuple(MemoryEdge(**row) for row in _read_jsonl(paths["edges"]))
    graph = ResearchMemoryGraph(
        graph_id=str(manifest.get("graph_id") or ""),
        nodes=nodes,
        edges=edges,
        schema_version=str(manifest.get("schema_version") or ""),
    )
    entries = tuple(
        SemanticMemoryIndexEntry(
            **{**row, "concepts": tuple(row.get("concepts") or ())}
        )
        for row in _read_jsonl(paths["index"])
    )
    memory = SemanticMemoryIndex(graph=graph, entries=entries)
    metadata = {
        "schema_version": "e2r_live_memory_load_v1",
        "graph_id": graph.graph_id,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "index_entry_count": len(entries),
        "manifest_status": manifest.get("status"),
        "critical_count_sum": manifest.get("critical_count_sum"),
        "file_hashes": {
            name: _sha256_file(path) for name, path in paths.items()
        },
    }
    return memory, metadata


def write_brain_planner_run(
    result: BrainPlannerRunResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "runs": root / "planner_runs.jsonl",
        "prompts": root / "llm_prompts.jsonl",
        "responses": root / "llm_responses.jsonl",
        "validation": root / "planner_validation.json",
        "memory": root / "planner_memory_metadata.json",
    }
    write_jsonl(paths["runs"], (item.to_dict() for item in result.planner_runs))
    write_jsonl(paths["prompts"], result.prompt_rows)
    write_jsonl(paths["responses"], result.response_rows)
    write_json(paths["validation"], {**dict(result.audit), "status": result.status})
    write_json(paths["memory"], result.memory_metadata)
    return paths


def load_planner_run_rows(path: str | Path) -> tuple[Mapping[str, Any], ...]:
    return tuple(_read_jsonl(Path(path)))


def _planner_evidence_rows(
    *,
    candidate: CandidateEvent,
    signals: Sequence[TriggerSignal],
    lanes: Sequence[BaselineLaneRecord],
    current_state: CurrentStateRecord | None,
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    for signal in signals:
        text = _fact_text(signal)
        rows.append(
            {
                "fact_id": "CURRENT-" + signal.trigger_signal_id,
                "text": text,
                "observed_date": signal.effective_date,
                "target_relation": "DIRECT",
                "current_status": (
                    "RESOLVED"
                    if "RESOLVED" in signal.lifecycle_status
                    else "ACTIVE"
                    if "OPEN" in signal.lifecycle_status
                    else "CURRENT"
                ),
                "source_refs": list(signal.source_refs),
            }
        )
    if current_state and not current_state.material_events:
        rows.append(
            {
                "fact_id": "CURRENT-HISTORY-" + candidate.target_id,
                "text": (
                    f"{candidate.target_name}의 과거 공식 사건 이력은 아직 완전한 backfill이 "
                    "아니므로 현재 관측만으로 장기 논리를 확정할 수 없다."
                ),
                "observed_date": candidate.as_of_date,
                "target_relation": "DIRECT",
                "current_status": "CURRENT",
                "source_refs": list(candidate.source_refs),
            }
        )
    for lane in lanes:
        if lane.provider_error_category:
            rows.append(
                {
                    "fact_id": "CURRENT-GAP-" + lane.lane_id,
                    "text": (
                        f"{candidate.target_name}의 {lane.lane} 공식 자료 확인은 provider 오류로 "
                        "완료되지 않아 추가 확인이 필요하다."
                    ),
                    "observed_date": lane.observed_date,
                    "target_relation": "DIRECT",
                    "current_status": "UNKNOWN",
                    "source_refs": list(lane.source_ids or candidate.source_refs),
                }
            )
    return tuple(rows)


def _fact_text(signal: TriggerSignal) -> str:
    report_name = str(signal.payload.get("report_name") or "").strip()
    if report_name:
        return (
            f"{signal.target_name}은 {signal.effective_date}에 '{report_name}' 공식 공시가 "
            f"접수되었고 확인 상태는 {signal.lifecycle_status}이다."
        )
    if signal.trigger_type == TriggerType.MARKET.value:
        return (
            f"{signal.target_name}의 {signal.effective_date} 일간 주가 변동률은 "
            f"{signal.payload.get('return_pct')}%이고 거래대금은 "
            f"{signal.payload.get('trading_value')}원이다. 이 관측은 조사 우선순위 신호다."
        )
    if signal.trigger_type == TriggerType.RISK.value and signal.payload.get("krx_segment"):
        return (
            f"{signal.target_name}은 {signal.effective_date} KRX에서 "
            f"'{signal.payload.get('krx_segment')}' 상태로 직접 관측되었고, "
            "원인과 해제 여부를 공식 자료로 재확인해야 한다."
        )
    if signal.trigger_type == TriggerType.EXISTING_LEDGER.value:
        return (
            f"{signal.target_name}의 기존 current claim 또는 OPEN 사건은 "
            f"{signal.effective_date} 기준 lifecycle 재확인이 필요하다."
        )
    return (
        f"{signal.target_name}에 {signal.effective_date} 현재 "
        f"{signal.trigger_type} 직접 관측이 있으며 상태는 {signal.lifecycle_status}이다."
    )


def _audit_brain_planner(
    *,
    as_of_date: str,
    selected: Sequence[LiveDepthDecision],
    runs: Sequence[LivePlannerRun],
    prompt_rows: Sequence[Mapping[str, Any]],
    response_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    real_success = sum(item.real_provider_success for item in runs)
    pending = sum(item.terminal_status == PlannerStatus.PENDING.value for item in runs)
    exact_blockers = sum(
        item.plan.pending is not None
        and bool(item.plan.pending.reason_code)
        and bool(item.plan.pending.reason_detail)
        for item in runs
    )
    score_stage_keys = sum(
        _forbidden_response_key_count(row.get("response_payload") or {})
        for row in response_rows
    )
    future_leaks = sum(
        bool(_FORBIDDEN_PROMPT_LEAK_RE.search(str(row.get("prompt_text") or "")))
        for row in prompt_rows
    )
    source_primary = sum(
        "source_primary" in str(row.get("prompt_text") or "").lower()
        for row in prompt_rows
    )
    future_input_drop = sum(
        int(item.input_compilation_audit.get("future_evidence_dropped_count", 0))
        for item in runs
    )
    status_counts: dict[str, int] = {}
    for item in runs:
        status_counts[item.terminal_status] = status_counts.get(item.terminal_status, 0) + 1
    critical = {
        "selected_l3_empty": int(len(selected) <= 0),
        "selected_planner_run_count_mismatch": abs(len(selected) - len(runs)),
        "planner_call_empty": int(len(response_rows) <= 0),
        "real_success_or_exact_blocker_missing": int(
            real_success <= 0 and exact_blockers != len(runs)
        ),
        "planner_score_stage_key": score_stage_keys,
        "future_outcome_prompt_leak": future_leaks,
        "source_primary_copy_without_reason": source_primary,
        "provider_failure_final_score": 0,
        "future_input_fact_used": future_input_drop,
    }
    return {
        "schema_version": "e2r_live_brain_planner_audit_v1",
        "as_of_date": as_of_date,
        "selected_L3_count": len(selected),
        "planner_run_count": len(runs),
        "planner_call_count": len(response_rows),
        "real_planner_success_count": real_success,
        "planner_pending_count": pending,
        "exact_llm_blocker_count": exact_blockers,
        "planner_status_counts": dict(sorted(status_counts.items())),
        "planner_score_stage_key_count": score_stage_keys,
        "future_outcome_prompt_leak_count": future_leaks,
        "source_primary_copy_without_reason_count": source_primary,
        "provider_failure_final_score_count": 0,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
    }


def _forbidden_response_key_count(value: Any) -> int:
    if isinstance(value, Mapping):
        return sum(
            int(bool(_FORBIDDEN_RESPONSE_KEY_RE.search(str(key))))
            + _forbidden_response_key_count(item)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return sum(_forbidden_response_key_count(item) for item in value)
    return 0


def _unique_by_target(rows: Sequence[Any], context: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for row in rows:
        target_id = str(row.target_id)
        if target_id in result:
            raise ValueError(f"duplicate target in {context}")
        result[target_id] = row
    return result


def _unique_by_id(rows: Sequence[Any], *, key: str, context: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for row in rows:
        identity = str(getattr(row, key))
        if identity in result:
            raise ValueError(f"duplicate identity in {context}")
        result[identity] = row
    return result


def _read_jsonl(path: Path) -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return tuple(rows)


def _in_memory_metadata(index: SemanticMemoryIndex) -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_live_memory_load_v1",
        "graph_id": index.graph.graph_id,
        "node_count": len(index.graph.nodes),
        "edge_count": len(index.graph.edges),
        "index_entry_count": len(index.entries),
        "manifest_status": "IN_MEMORY_TEST_OR_CALLER_SUPPLIED",
        "critical_count_sum": 0,
        "file_hashes": {},
    }


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


__all__ = [
    "LIVE_PLANNER_RUN_SCHEMA_VERSION",
    "BrainPlannerConfig",
    "BrainPlannerRunResult",
    "CurrentBrainPlannerRunner",
    "LivePlannerRun",
    "RecordingTwoPassPlannerProvider",
    "load_canonical_semantic_memory_index",
    "load_planner_run_rows",
    "write_brain_planner_run",
]
