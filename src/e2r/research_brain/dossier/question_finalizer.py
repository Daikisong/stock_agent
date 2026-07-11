"""Finalize dossier question states from real bounded source-attempt leaves."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl


QUESTION_FINALIZER_SCHEMA_VERSION = "e2r_dossier_question_finalizer_v1"
_RESOLVED_WEB_STATUSES = {"SEARCH_EXECUTED", "RESOLVED_STOPPED"}


def finalize_dossier_question_closures(
    *,
    dossier_root: str | Path,
    source_research_roots: Sequence[str | Path],
) -> Mapping[str, Any]:
    root = Path(dossier_root)
    tasks = _read_jsonl(root / "question_source_tasks.jsonl")
    closures = _read_jsonl(root / "question_closure.jsonl")
    if not tasks or not closures:
        raise ValueError("question finalization requires dossier tasks and closures")
    research_roots = tuple(Path(value) for value in source_research_roots)
    executed_tasks = tuple(
        row
        for research_root in research_roots
        for row in _read_jsonl(research_root / "question_source_tasks.jsonl")
    )
    fetch_rows = tuple(
        row
        for research_root in research_roots
        for row in _read_jsonl(research_root / "provider_fetch_results.jsonl")
    )
    request_rows = tuple(
        row
        for research_root in research_roots
        for row in _read_jsonl(research_root / "provider_requests.jsonl")
    )
    web_tasks = tuple(
        row
        for research_root in research_roots
        for row in _read_jsonl(research_root / "web_search_tasks.jsonl")
    )
    task_by_family = {
        str(row.get("question_family_id") or ""): row for row in tasks
    }
    closure_by_family = {
        str(row.get("question_family_id") or ""): row for row in closures
    }
    if set(task_by_family) != set(closure_by_family):
        raise ValueError("question task and closure family identities differ")
    finalized = []
    researched_family_count = 0
    evaluated_absent_count = 0
    for family_id, task in task_by_family.items():
        closure = dict(closure_by_family[family_id])
        matching_tasks = tuple(
            row
            for row in executed_tasks
            if str(row.get("target_id") or "") == str(task.get("target_id") or "")
            and str(row.get("question_to_answer") or "")
            == str(task.get("question_to_answer") or "")
        )
        task_ids = {str(row.get("task_id") or "") for row in matching_tasks}
        matching_fetches = tuple(
            row for row in fetch_rows if str(row.get("source_task_id") or "") in task_ids
        )
        matching_requests = tuple(
            row for row in request_rows if str(row.get("source_task_id") or "") in task_ids
        )
        matching_web = tuple(
            row for row in web_tasks if str(row.get("source_task_id") or "") in task_ids
        )
        real_query = bool(matching_tasks) and all(
            (row.get("query_intent") or {}).get("generator_kind") == "REAL_LLM"
            and (row.get("query_intent") or {}).get("literal_queries")
            for row in matching_tasks
        )
        bounded = bool(matching_tasks) and all(
            0 < int((row.get("budget") or {}).get(name) or 0) <= maximum
            for row in matching_tasks
            for name, maximum in (
                ("max_queries", 10),
                ("max_candidates", 100),
                ("max_fetches", 20),
            )
        )
        official_attempted = any(
            row.get("actual_provider_call") is True for row in matching_requests
        ) or any(
            str(row.get("acquisition_class") or "")
            in {"SOURCE_EXHAUSTED", "PROVIDER_FAILED", "REAL_PROVIDER_FETCH", "FRESH_PROVIDER_CACHE"}
            for row in matching_fetches
        )
        web_completed = any(
            row.get("official_first_attempted") is True
            and row.get("search_call_executed") is True
            and str(row.get("status") or "") in _RESOLVED_WEB_STATUSES
            for row in matching_web
        )
        researched = real_query and bounded and official_attempted
        proof = [
            str(row.get("provider_request_record_id") or "")
            for row in matching_requests
            if str(row.get("provider_request_record_id") or "")
        ]
        proof.extend(
            str(row.get("web_task_id") or "")
            for row in matching_web
            if str(row.get("web_task_id") or "")
        )
        if researched:
            researched_family_count += 1
        pending = closure.get("status") in {
            "PROVIDER_PENDING",
            "SOURCE_PENDING",
            "BUDGET_PENDING",
        }
        if pending and researched and web_completed and proof:
            closure.update(
                {
                    "status": "EVALUATED_ABSENT",
                    "failure_class": "SOURCE_EXHAUSTED",
                    "search_exhaustion_proof": list(dict.fromkeys(proof)),
                    "next_action": "QUESTION_TERMINAL_NO_QUALIFYING_CURRENT_CLAIM",
                }
            )
            evaluated_absent_count += 1
        closure["research_execution"] = {
            "real_llm_query": real_query,
            "bounded": bounded,
            "official_attempted": official_attempted,
            "web_fallback_completed": web_completed,
            "executed_source_task_ids": sorted(task_ids),
        }
        finalized.append(closure)
    nonterminal = tuple(
        row["question_family_id"]
        for row in finalized
        if row.get("status")
        in {"PROVIDER_PENDING", "SOURCE_PENDING", "BUDGET_PENDING"}
    )
    critical = {
        "pending_marked_absent_without_proof_count": sum(
            row.get("status") == "EVALUATED_ABSENT"
            and not row.get("search_exhaustion_proof")
            for row in finalized
        ),
        "unbounded_research_count": sum(
            bool((row.get("research_execution") or {}).get("executed_source_task_ids"))
            and not (row.get("research_execution") or {}).get("bounded")
            for row in finalized
        ),
        "nonterminal_question_count": len(nonterminal),
    }
    audit = {
        "schema_version": QUESTION_FINALIZER_SCHEMA_VERSION,
        "status": (
            "DOSSIER_QUESTION_CLOSURE_PASS"
            if sum(critical.values()) == 0
            else "DOSSIER_QUESTION_CLOSURE_PENDING"
        ),
        "target_id": tasks[0].get("target_id"),
        "question_family_count": len(tasks),
        "researched_family_count": researched_family_count,
        "evaluated_absent_count": sum(
            row.get("status") == "EVALUATED_ABSENT" for row in finalized
        ),
        "nonterminal_question_family_ids": list(nonterminal),
        "source_research_roots": [str(value) for value in research_roots],
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }
    _write_research_attempt_leaves(
        root=root,
        research_roots=research_roots,
        executed_tasks=executed_tasks,
        request_rows=request_rows,
        web_tasks=web_tasks,
    )
    write_jsonl(root / "question_closure.jsonl", finalized)
    write_json(root / "question_closure_audit.json", audit)
    return audit


def _write_research_attempt_leaves(
    *,
    root: Path,
    research_roots: Sequence[Path],
    executed_tasks: Sequence[Mapping[str, Any]],
    request_rows: Sequence[Mapping[str, Any]],
    web_tasks: Sequence[Mapping[str, Any]],
) -> None:
    write_jsonl(
        root / "executed_question_source_tasks.jsonl",
        _dedupe_rows(executed_tasks, ("task_id",)),
    )
    write_jsonl(
        root / "research_provider_requests.jsonl",
        _dedupe_rows(request_rows, ("provider_request_record_id",)),
    )
    write_jsonl(
        root / "research_web_search_tasks.jsonl",
        _dedupe_rows(web_tasks, ("web_task_id",)),
    )
    for name in (
        "web_search_results.jsonl",
        "web_rejected_documents.jsonl",
        "web_fetched_documents.jsonl",
    ):
        rows = tuple(
            row
            for research_root in research_roots
            for row in _read_jsonl(research_root / name)
        )
        write_jsonl(root / f"research_{name}", _dedupe_rows(rows, ("web_result_id", "web_fetch_id")))


def _dedupe_rows(
    rows: Sequence[Mapping[str, Any]], identity_keys: Sequence[str]
) -> tuple[Mapping[str, Any], ...]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = next(
            (str(row.get(key) or "") for key in identity_keys if str(row.get(key) or "")),
            json.dumps(row, ensure_ascii=False, sort_keys=True),
        )
        result.setdefault(identity, row)
    return tuple(result[key] for key in sorted(result))


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = ["QUESTION_FINALIZER_SCHEMA_VERSION", "finalize_dossier_question_closures"]
