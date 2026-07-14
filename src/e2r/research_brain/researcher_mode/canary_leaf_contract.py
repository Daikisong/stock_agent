"""Materialize the exact per-canary leaf contract required by the v5 goal.

The Researcher Mode internals keep richer module-specific filenames.  This
module publishes deterministic, score-safe projections under the final
acceptance filenames without changing the underlying score or Stage authority.
Gold comparison remains a separate post-run-only operation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl


CANARY_LEAF_CONTRACT_SCHEMA_VERSION = "e2r_v5_canary_leaf_contract_v1"
CANARY_MASTER_LEAF_FILES: Mapping[str, str] = {
    "research_epochs": "research_epochs.jsonl",
    "query_ledger": "query_ledger.jsonl",
    "source_graph": "source_graph.jsonl",
    "documents": "documents.jsonl",
    "evidence_facts": "evidence_facts.jsonl",
    "counterfacts": "counterfacts.jsonl",
    "component_research_memos": "component_research_memos.jsonl",
    "component_judge_decisions": "component_judge_decisions.jsonl",
    "historical_anchor_comparisons": "historical_anchor_comparisons.jsonl",
    "final_component_decisions": "final_component_decisions.jsonl",
    "score_vector": "score_vector.json",
    "atomic_stage_decision": "atomic_stage_decision.json",
    "stagecourt_trace": "stagecourt_trace.json",
    "gold_fact_comparison": "gold_fact_comparison.jsonl",
}

_JSONL_MIRRORS: Mapping[str, str] = {
    "query_ledger.jsonl": "generated_queries.jsonl",
    "documents.jsonl": "source_graph_evidence_documents.jsonl",
    "component_judge_decisions.jsonl": "judge_decisions.jsonl",
    "historical_anchor_comparisons.jsonl": "anchor_comparisons.jsonl",
    "final_component_decisions.jsonl": "component_decisions.jsonl",
}
_CHECKPOINT_REQUIRED = tuple(
    name
    for key, name in CANARY_MASTER_LEAF_FILES.items()
    if key != "gold_fact_comparison"
)


def materialize_canary_checkpoint_leaves(
    output_root: str | Path,
    *,
    target_id: str,
    as_of_date: str,
    production_research_complete: bool,
    refresh_target_manifest: bool = False,
) -> Mapping[str, Any]:
    """Write exact checkpoint leaves from canonical internal artifacts."""

    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)
    for destination, source in _JSONL_MIRRORS.items():
        source_path = root / source
        if source_path.is_file():
            write_jsonl(root / destination, _read_jsonl(source_path))

    _write_research_epochs(root, target_id=target_id, as_of_date=as_of_date)
    _write_source_graph_rows(root, target_id=target_id, as_of_date=as_of_date)
    _write_score_vector(root, target_id=target_id, as_of_date=as_of_date)

    audit = audit_canary_leaf_contract(
        root,
        target_id=target_id,
        as_of_date=as_of_date,
        production_research_complete=production_research_complete,
        post_run_gold_required=False,
    )
    write_json(root / "canary_leaf_contract_audit.json", audit)
    if refresh_target_manifest:
        _refresh_target_manifest(root, audit)
    return audit


def write_canary_post_run_gold_comparison(
    output_root: str | Path,
    *,
    target_id: str,
    as_of_date: str,
    comparison_rows: Sequence[Mapping[str, Any]],
    refresh_target_manifest: bool = True,
) -> Mapping[str, Any]:
    """Publish target-scoped Gold comparison only after production is closed."""

    root = Path(output_root)
    rows = tuple(dict(row) for row in comparison_rows)
    if any(str(row.get("target_id") or "") != target_id for row in rows):
        raise ValueError("post-run Gold comparison crosses canary target scope")
    write_jsonl(root / CANARY_MASTER_LEAF_FILES["gold_fact_comparison"], rows)
    audit = audit_canary_leaf_contract(
        root,
        target_id=target_id,
        as_of_date=as_of_date,
        production_research_complete=True,
        post_run_gold_required=True,
    )
    write_json(root / "canary_leaf_contract_audit.json", audit)
    if refresh_target_manifest:
        _refresh_target_manifest(root, audit)
    return audit


def audit_canary_leaf_contract(
    output_root: str | Path,
    *,
    target_id: str,
    as_of_date: str,
    production_research_complete: bool,
    post_run_gold_required: bool,
) -> Mapping[str, Any]:
    root = Path(output_root)
    leaf_rows = {
        key: _leaf_row(root, filename)
        for key, filename in CANARY_MASTER_LEAF_FILES.items()
    }
    mirror_mismatches = {
        destination: int(
            not _jsonl_equal(root / destination, root / source)
        )
        for destination, source in _JSONL_MIRRORS.items()
    }
    epochs = _read_jsonl(root / CANARY_MASTER_LEAF_FILES["research_epochs"])
    checkpoint = _read_json(root / "research_epoch_checkpoint.json")
    epoch_lineage_valid = bool(
        checkpoint
        and epochs
        and len(
            {
                str(row.get("checkpoint_id") or "")
                for row in epochs
                if str(row.get("checkpoint_id") or "")
            }
        )
        == len(epochs)
        and all(
            row.get("target_id") == target_id
            and row.get("as_of_date") == as_of_date
            for row in epochs
        )
        and any(
            row.get("checkpoint_id") == checkpoint.get("checkpoint_id")
            and row.get("target_id") == target_id
            and row.get("as_of_date") == as_of_date
            for row in epochs
        )
    )
    source_graph_valid = _source_graph_projection_valid(
        root,
        target_id=target_id,
        as_of_date=as_of_date,
    )
    score_vector_valid = _score_projection_valid(
        root,
        target_id=target_id,
        as_of_date=as_of_date,
    )
    gold_present = leaf_rows["gold_fact_comparison"]["exists"]
    gold_rows = _read_jsonl(
        root / CANARY_MASTER_LEAF_FILES["gold_fact_comparison"]
    )
    critical_counts = {
        "checkpoint_leaf_missing_count": sum(
            not (root / filename).is_file() for filename in _CHECKPOINT_REQUIRED
        ),
        "mirror_content_mismatch_count": sum(mirror_mismatches.values()),
        "research_epoch_lineage_failure_count": int(not epoch_lineage_valid),
        "source_graph_projection_failure_count": int(not source_graph_valid),
        "score_vector_projection_failure_count": int(not score_vector_valid),
        "premature_gold_comparison_count": int(
            gold_present and not production_research_complete
        ),
        "post_run_gold_missing_count": int(
            post_run_gold_required and not gold_present
        ),
        "post_run_gold_empty_count": int(
            post_run_gold_required and not gold_rows
        ),
        "post_run_gold_scope_mismatch_count": sum(
            str(row.get("target_id") or "") != target_id for row in gold_rows
        ),
    }
    critical_sum = sum(critical_counts.values())
    return {
        "schema_version": CANARY_LEAF_CONTRACT_SCHEMA_VERSION,
        "status": (
            "CANARY_LEAF_CONTRACT_PASS"
            if critical_sum == 0
            else "CANARY_LEAF_CONTRACT_PENDING"
        ),
        "target_id": target_id,
        "as_of_date": as_of_date,
        "production_research_complete": production_research_complete,
        "post_run_gold_required": post_run_gold_required,
        "leaf_rows": leaf_rows,
        "mirror_mismatch_by_leaf": mirror_mismatches,
        "research_epoch_lineage_valid": epoch_lineage_valid,
        "source_graph_projection_valid": source_graph_valid,
        "score_vector_projection_valid": score_vector_valid,
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
    }


def canary_output_tree_hash(output_root: str | Path) -> str:
    root = Path(output_root)
    return stable_hash(
        [
            {
                "path": str(path.relative_to(root)),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
            for path in sorted(root.rglob("*"))
            if path.is_file() and path.name != "target_run_manifest.json"
        ]
    )


def _write_research_epochs(root: Path, *, target_id: str, as_of_date: str) -> None:
    checkpoint = _read_json(root / "research_epoch_checkpoint.json")
    if not checkpoint:
        return
    if (
        str(checkpoint.get("target_id") or "") != target_id
        or str(checkpoint.get("as_of_date") or "") != as_of_date
    ):
        raise ValueError("research epoch checkpoint target or date mismatch")
    path = root / CANARY_MASTER_LEAF_FILES["research_epochs"]
    by_id = {
        str(row.get("checkpoint_id") or ""): dict(row)
        for row in _read_jsonl(path)
        if str(row.get("checkpoint_id") or "")
    }
    by_id[str(checkpoint["checkpoint_id"])] = dict(checkpoint)
    rows = sorted(
        by_id.values(),
        key=lambda row: (int(row.get("epoch") or 0), str(row.get("checkpoint_id") or "")),
    )
    write_jsonl(path, rows)


def _write_source_graph_rows(root: Path, *, target_id: str, as_of_date: str) -> None:
    graph = _read_json(root / "source_graph.json")
    if not graph:
        return
    write_jsonl(
        root / CANARY_MASTER_LEAF_FILES["source_graph"],
        _source_graph_rows(graph, target_id=target_id, as_of_date=as_of_date),
    )


def _source_graph_rows(
    graph: Mapping[str, Any], *, target_id: str, as_of_date: str
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = [
        {
            "schema_version": CANARY_LEAF_CONTRACT_SCHEMA_VERSION,
            "record_type": "GRAPH_STATE",
            "target_id": target_id,
            "as_of_date": as_of_date,
            "checkpoint_required": graph.get("checkpoint_required"),
            "covered_source_families": list(graph.get("covered_source_families") or ()),
            "open_objectives": list(graph.get("open_objectives") or ()),
            "score_authority": bool(graph.get("score_authority", False)),
        }
    ]
    rows.extend(
        {
            **dict(row),
            "schema_version": CANARY_LEAF_CONTRACT_SCHEMA_VERSION,
            "record_type": "NODE",
            "target_id": target_id,
            "as_of_date": as_of_date,
        }
        for row in graph.get("nodes") or ()
    )
    rows.extend(
        {
            **dict(row),
            "schema_version": CANARY_LEAF_CONTRACT_SCHEMA_VERSION,
            "record_type": "EDGE",
            "target_id": target_id,
            "as_of_date": as_of_date,
        }
        for row in graph.get("edges") or ()
    )
    return tuple(rows)


def _write_score_vector(root: Path, *, target_id: str, as_of_date: str) -> None:
    source_path = root / "deterministic_total_score.json"
    total = _read_json(source_path)
    if not total:
        return
    raw_score = total.get("score")
    score = raw_score if isinstance(raw_score, Mapping) else {}
    score_valid = bool(
        total.get("status") == "COMPLETE" and score.get("score_valid") is True
    )
    write_json(
        root / CANARY_MASTER_LEAF_FILES["score_vector"],
        {
            "schema_version": "e2r_v5_canary_score_vector_v1",
            "target_id": target_id,
            "as_of_date": as_of_date,
            "status": "COMPLETE" if score_valid else "RESEARCH_REQUIRED",
            "score_valid": score_valid,
            "component_score_vector": (
                dict(score.get("component_points") or {}) if score_valid else None
            ),
            "total_points": score.get("total_points") if score_valid else None,
            "max_points": score.get("max_points") if score_valid else None,
            "pending_reasons": list(total.get("pending_reasons") or ()),
            "production_stage_authority": False,
            "source_artifact": "deterministic_total_score.json",
            "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        },
    )


def _source_graph_projection_valid(
    root: Path, *, target_id: str, as_of_date: str
) -> bool:
    source = _read_json(root / "source_graph.json")
    rows = _read_jsonl(root / CANARY_MASTER_LEAF_FILES["source_graph"])
    if not source or not rows:
        return False
    return rows == _source_graph_rows(
        source,
        target_id=target_id,
        as_of_date=as_of_date,
    )


def _score_projection_valid(
    root: Path, *, target_id: str, as_of_date: str
) -> bool:
    source_path = root / "deterministic_total_score.json"
    score = _read_json(root / CANARY_MASTER_LEAF_FILES["score_vector"])
    if not source_path.is_file() or not score:
        return False
    if (
        score.get("target_id") != target_id
        or score.get("as_of_date") != as_of_date
        or score.get("source_sha256")
        != hashlib.sha256(source_path.read_bytes()).hexdigest()
    ):
        return False
    source = _read_json(source_path)
    raw = source.get("score")
    source_score = raw if isinstance(raw, Mapping) else {}
    source_valid = bool(
        source.get("status") == "COMPLETE"
        and source_score.get("score_valid") is True
    )
    if score.get("score_valid") is not source_valid:
        return False
    if not source_valid:
        return bool(
            score.get("component_score_vector") is None
            and score.get("total_points") is None
        )
    return bool(
        score.get("component_score_vector")
        == source_score.get("component_points")
        and score.get("total_points") == source_score.get("total_points")
    )


def _jsonl_equal(left: Path, right: Path) -> bool:
    return bool(left.is_file() and right.is_file() and _read_jsonl(left) == _read_jsonl(right))


def _refresh_target_manifest(root: Path, audit: Mapping[str, Any]) -> None:
    path = root / "target_run_manifest.json"
    manifest = _read_json(path)
    if not manifest:
        return
    manifest = {
        **manifest,
        "canary_leaf_contract": {
            "status": audit["status"],
            "critical_count_sum": audit["critical_count_sum"],
            "audit_path": "canary_leaf_contract_audit.json",
        },
        "output_tree_hash": canary_output_tree_hash(root),
    }
    write_json(path, manifest)


def _leaf_row(root: Path, filename: str) -> Mapping[str, Any]:
    path = root / filename
    if not path.is_file():
        return {"path": filename, "exists": False, "sha256": None, "row_count": None}
    return {
        "path": filename,
        "exists": True,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "row_count": len(_read_jsonl(path)) if path.suffix == ".jsonl" else None,
    }


def _read_json(path: Path) -> Mapping[str, Any]:
    if not path.is_file():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, Mapping) else {}


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    rows = []
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, Mapping):
                return ()
            rows.append(dict(value))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return ()
    return tuple(rows)


__all__ = [
    "CANARY_LEAF_CONTRACT_SCHEMA_VERSION",
    "CANARY_MASTER_LEAF_FILES",
    "audit_canary_leaf_contract",
    "canary_output_tree_hash",
    "materialize_canary_checkpoint_leaves",
    "write_canary_post_run_gold_comparison",
]
