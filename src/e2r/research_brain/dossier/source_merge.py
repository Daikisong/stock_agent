"""Merge multiple real source runs without losing SourceTask lineage."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl


MERGED_SOURCE_SCHEMA_VERSION = "e2r_dossier_merged_source_run_v1"


def merge_dossier_source_runs(
    *,
    source_roots: Sequence[str | Path],
    output_root: str | Path,
    target_id: str,
) -> Mapping[str, Any]:
    roots = tuple(Path(value) for value in source_roots)
    if len(roots) < 2 or any(not root.is_dir() for root in roots):
        raise ValueError("source merge requires at least two existing source roots")
    task_rows = _merge_unique_rows(
        roots=roots,
        names=("question_source_tasks.jsonl",),
        identity_keys=("task_id", "source_task_id"),
        target_id=target_id,
    )
    fetch_rows = _merge_unique_rows(
        roots=roots,
        names=("provider_fetch_results.jsonl",),
        identity_keys=(
            "provider_fetch_result_id",
            "fetch_id",
            "requested_url",
            "canonical_url",
        ),
        target_id=target_id,
    )
    documents_by_id: dict[str, dict[str, Any]] = {}
    for root in roots:
        selected = root / "claim_selected_documents.jsonl"
        paths = (selected,) if selected.is_file() else (root / "evidence_documents.jsonl",)
        for path in paths:
            if not path.is_file():
                continue
            for row in _read_jsonl(path):
                if str(row.get("target_id") or "") != target_id:
                    continue
                document_id = str(row.get("document_id") or "")
                if not document_id:
                    continue
                prior = documents_by_id.get(document_id)
                if prior is None:
                    documents_by_id[document_id] = dict(row)
                    continue
                if str(prior.get("content_hash") or "") != str(
                    row.get("content_hash") or ""
                ):
                    raise ValueError("same document id has conflicting content hashes")
                prior["source_task_ids"] = list(
                    dict.fromkeys(
                        (
                            *(prior.get("source_task_ids") or ()),
                            *(row.get("source_task_ids") or ()),
                        )
                    )
                )
    documents = tuple(documents_by_id[key] for key in sorted(documents_by_id))
    referenced_task_ids = {
        str(task_id)
        for row in documents
        for task_id in row.get("source_task_ids") or ()
    }
    task_ids = {
        str(row.get("task_id") or row.get("source_task_id") or "")
        for row in task_rows
    }
    unresolved_task_ids = referenced_task_ids - task_ids
    critical = {
        "document_missing_count": int(not documents),
        "source_task_lineage_missing_count": len(unresolved_task_ids),
        "target_contamination_count": sum(
            str(row.get("target_id") or "") != target_id for row in documents
        ),
    }
    output = Path(output_root)
    output.mkdir(parents=True, exist_ok=True)
    write_jsonl(output / "question_source_tasks.jsonl", task_rows)
    write_jsonl(output / "provider_fetch_results.jsonl", fetch_rows)
    write_jsonl(output / "evidence_documents.jsonl", documents)
    audit = {
        "schema_version": MERGED_SOURCE_SCHEMA_VERSION,
        "status": (
            "DOSSIER_SOURCE_MERGE_PASS"
            if sum(critical.values()) == 0
            else "DOSSIER_SOURCE_MERGE_FAIL"
        ),
        "target_id": target_id,
        "source_roots": [str(root) for root in roots],
        "source_task_count": len(task_rows),
        "fetch_result_count": len(fetch_rows),
        "full_document_count": len(documents),
        "referenced_source_task_count": len(referenced_task_ids),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }
    write_json(output / "source_merge_audit.json", audit)
    return audit


def _merge_unique_rows(
    *,
    roots: Sequence[Path],
    names: Sequence[str],
    identity_keys: Sequence[str],
    target_id: str,
) -> tuple[Mapping[str, Any], ...]:
    result: dict[str, Mapping[str, Any]] = {}
    for root in roots:
        for name in names:
            path = root / name
            if not path.is_file():
                continue
            for row in _read_jsonl(path):
                if str(row.get("target_id") or "") != target_id:
                    continue
                identity = next(
                    (
                        str(row.get(key) or "")
                        for key in identity_keys
                        if str(row.get(key) or "")
                    ),
                    "",
                )
                if not identity:
                    identity = json.dumps(row, ensure_ascii=False, sort_keys=True)
                result.setdefault(identity, row)
    return tuple(result[key] for key in sorted(result))


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = ["MERGED_SOURCE_SCHEMA_VERSION", "merge_dossier_source_runs"]
