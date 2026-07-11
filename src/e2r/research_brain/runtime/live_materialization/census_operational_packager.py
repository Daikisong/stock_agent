"""Write deterministic full-universe Census leaves from the current evaluator."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.runtime.current_operation_runner import (
    AtomicScoreType,
    CanonicalStage,
    CurrentOperationRunnerResult,
    DailyBaselineLaneStatus,
    DailyTerminalStatus,
    compute_current_source_corpus_hash,
)


CENSUS_OPERATIONAL_SCHEMA_VERSION = "e2r_live_census_operational_v1"


def package_live_census_operation(
    *,
    result: CurrentOperationRunnerResult,
    output_root: str | Path,
    shard_count: int,
    resume: bool,
) -> Mapping[str, Path]:
    """Package one complete Census and deterministically materialize every shard.

    ``shard_count`` is an orchestration partition count, not a row filter.  One
    canonical invocation writes/checks every partition and then merges all of
    them, so the public Census map always represents the full eligible universe.
    """

    if isinstance(shard_count, bool) or not isinstance(shard_count, int) or shard_count <= 0:
        raise ValueError("Census shard_count must be a positive integer")
    if not isinstance(resume, bool):
        raise ValueError("Census resume must be boolean")

    root = Path(output_root)
    eligible = tuple(item for item in result.universe if item.eligible)
    member_by_target = {item.target_id: item for item in eligible}
    timeline_by_target = {item.target_id: item for item in result.source_timelines}
    lane_by_target: dict[str, list[Any]] = defaultdict(list)
    for lane in result.baseline_lanes:
        lane_by_target[lane.target_id].append(lane)

    stage_rows = tuple(
        _census_stage_row(
            status=status,
            market=member_by_target[status.target_id].market,
            source_attempted=bool(
                timeline_by_target.get(status.target_id)
                and timeline_by_target[status.target_id].events
            ),
        )
        for status in sorted(result.stage_statuses, key=lambda item: item.target_id)
        if status.target_id in member_by_target
    )
    shard_rows = _partition_rows(stage_rows, shard_count=shard_count)
    shard_paths, checkpoint_paths, reused_shards = _write_or_resume_shards(
        root=root,
        shard_rows=shard_rows,
        as_of_date=result.as_of_date,
        resume=resume,
    )
    merged_rows = tuple(
        row
        for shard_index in range(shard_count)
        for row in _read_jsonl(shard_paths[shard_index])
    )
    merged_rows = tuple(sorted(merged_rows, key=lambda item: str(item["target_id"])))

    current_source_corpus_hash = str(
        result.manifest.get("source_corpus_hash") or ""
    )
    census_source_corpus_hash = compute_current_source_corpus_hash(
        as_of_date=result.as_of_date,
        universe=result.universe,
        baseline_lanes=result.baseline_lanes,
        triggers=result.triggers,
        claims=result.claims,
        claim_provenance=result.claim_provenance,
        source_tasks=result.source_tasks,
        deep_executions=result.deep_executions,
    )
    source_corpus_audit = audit_current_census_source_corpus_hash(
        current_source_corpus_hash=current_source_corpus_hash,
        census_source_corpus_hash=census_source_corpus_hash,
    )

    hard_counts = {
        **_hard_acceptance_counts(
            result=result,
            eligible_target_ids=tuple(member_by_target),
            stage_rows=merged_rows,
            lane_by_target=lane_by_target,
        ),
        **source_corpus_audit["critical_counts"],
    }
    if any(hard_counts.values()):
        raise ValueError(f"Census hard acceptance failed: {hard_counts}")

    paths: dict[str, Path] = {}
    paths["census_stage_map_jsonl"] = root / "census_stage_map.jsonl"
    write_jsonl(paths["census_stage_map_jsonl"], merged_rows)
    paths["census_stage_map_csv"] = root / "census_stage_map.csv"
    _write_stage_csv(paths["census_stage_map_csv"], merged_rows)

    stage_counts = Counter(str(row["canonical_stage"]) for row in merged_rows)
    terminal_counts = Counter(str(row["terminal_status"]) for row in merged_rows)
    paths["stage_distribution"] = root / "stage_distribution.json"
    write_json(
        paths["stage_distribution"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "as_of_date": result.as_of_date,
            "eligible_count": len(eligible),
            "stage_counts": dict(sorted(stage_counts.items())),
            "terminal_status_counts": dict(sorted(terminal_counts.items())),
        },
    )

    # Current KRX universe has an exchange-market field but no trustworthy
    # sector taxonomy.  Preserve that distinction instead of inventing sectors.
    market_rows: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in merged_rows:
        market_rows[str(row["market"])].append(row)
    paths["sector_distribution"] = root / "sector_distribution.json"
    write_json(
        paths["sector_distribution"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "as_of_date": result.as_of_date,
            "classification_basis": "KRX_MARKET_FALLBACK_SECTOR_FIELD_UNAVAILABLE",
            "rows": [
                {
                    "sector": "UNCLASSIFIED",
                    "market": market,
                    "symbol_count": len(rows),
                    "stage_counts": dict(
                        sorted(Counter(str(row["canonical_stage"]) for row in rows).items())
                    ),
                }
                for market, rows in sorted(market_rows.items())
            ],
        },
    )

    depth_counts = Counter(item.maximum_depth for item in result.depth_decisions)
    paths["depth_distribution"] = root / "depth_distribution.json"
    write_json(
        paths["depth_distribution"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "as_of_date": result.as_of_date,
            "maximum_depth_counts": dict(sorted(depth_counts.items())),
            "selected_for_deep_count": sum(
                item.selected_for_deep for item in result.depth_decisions
            ),
            "not_selected_for_deep_count": sum(
                not item.selected_for_deep for item in result.depth_decisions
            ),
        },
    )

    provider_rows = _provider_gap_rows(result, lane_by_target=lane_by_target)
    paths["provider_gap_report"] = root / "provider_gap_report.json"
    write_json(
        paths["provider_gap_report"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "as_of_date": result.as_of_date,
            "provider_gap_target_count": len(provider_rows),
            "rows": provider_rows,
        },
    )
    source_rows = _source_gap_rows(result)
    paths["source_gap_report"] = root / "source_gap_report.json"
    write_json(
        paths["source_gap_report"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "as_of_date": result.as_of_date,
            "source_gap_target_count": len(source_rows),
            "rows": source_rows,
        },
    )

    paths["watchlist_seed"] = root / "watchlist_seed.json"
    write_json(
        paths["watchlist_seed"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "as_of_date": result.as_of_date,
            "monitoring_only": True,
            "rows": [item.to_dict() for item in result.watchlist],
        },
    )
    paths["deep_backfill_queue"] = root / "deep_backfill_queue.json"
    write_json(
        paths["deep_backfill_queue"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "as_of_date": result.as_of_date,
            "rows": _deep_backfill_rows(merged_rows),
        },
    )

    paths["census_acceptance_audit"] = root / "census_acceptance_audit.json"
    write_json(
        paths["census_acceptance_audit"],
        {
            "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
            "status": "CENSUS_SELECTIVE_DEEP_PASS",
            "as_of_date": result.as_of_date,
            "eligible_count": len(eligible),
            "stage_map_count": len(merged_rows),
            "source_timeline_count": len(result.source_timelines),
            "baseline_lane_count": len(result.baseline_lanes),
            "selected_deep_count": sum(
                item.selected_for_deep for item in result.depth_decisions
            ),
            "shard_count": shard_count,
            "checkpoint_count": len(checkpoint_paths),
            "reused_shard_count": reused_shards,
            "merged_stage_map_hash": stable_hash(merged_rows),
            "source_corpus_hash": census_source_corpus_hash,
            "current_source_corpus_hash": current_source_corpus_hash,
            "census_source_corpus_hash": census_source_corpus_hash,
            "source_corpus_hash_audit": source_corpus_audit,
            "hard_acceptance_counts": hard_counts,
            "critical_count_sum": 0,
            "production_runtime_ready": False,
        },
    )
    paths["operator_digest"] = root / "operator_digest.md"
    write_text(
        paths["operator_digest"],
        _render_operator_digest(
            result=result,
            eligible_count=len(eligible),
            stage_counts=stage_counts,
            terminal_counts=terminal_counts,
            shard_count=shard_count,
            reused_shards=reused_shards,
        ),
    )
    for index, path in enumerate(shard_paths):
        paths[f"census_shard_{index:04d}"] = path
    for index, path in enumerate(checkpoint_paths):
        paths[f"census_checkpoint_{index:04d}"] = path
    return paths


def audit_current_census_source_corpus_hash(
    *,
    current_source_corpus_hash: str,
    census_source_corpus_hash: str,
) -> Mapping[str, Any]:
    """Fail closed when current and Census did not use the same source corpus."""

    def valid(value: str) -> bool:
        return len(value) == 64 and all(
            character in "0123456789abcdef" for character in value
        )

    current_valid = valid(current_source_corpus_hash)
    census_valid = valid(census_source_corpus_hash)
    critical = {
        "current_source_corpus_hash_missing_or_invalid": int(not current_valid),
        "census_source_corpus_hash_missing_or_invalid": int(not census_valid),
        "current_census_source_corpus_hash_mismatch": int(
            current_valid
            and census_valid
            and current_source_corpus_hash != census_source_corpus_hash
        ),
    }
    total = sum(critical.values())
    return {
        "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
        "status": (
            "CURRENT_CENSUS_SOURCE_CORPUS_HASH_PASS"
            if total == 0
            else "CURRENT_CENSUS_SOURCE_CORPUS_HASH_FAIL"
        ),
        "current_source_corpus_hash": current_source_corpus_hash,
        "census_source_corpus_hash": census_source_corpus_hash,
        "critical_counts": critical,
        "critical_count_sum": total,
    }


def _census_stage_row(
    *,
    status: Any,
    market: str,
    source_attempted: bool,
) -> Mapping[str, Any]:
    return {
        **status.to_dict(),
        "market": market,
        "source_attempted": source_attempted,
    }


def _partition_rows(
    rows: Sequence[Mapping[str, Any]], *, shard_count: int
) -> tuple[tuple[Mapping[str, Any], ...], ...]:
    buckets: list[list[Mapping[str, Any]]] = [[] for _ in range(shard_count)]
    for row in rows:
        shard_index = int(
            stable_hash({"target_id": str(row["target_id"])})[:16], 16
        ) % shard_count
        buckets[shard_index].append(row)
    return tuple(
        tuple(sorted(bucket, key=lambda item: str(item["target_id"])))
        for bucket in buckets
    )


def _write_or_resume_shards(
    *,
    root: Path,
    shard_rows: Sequence[Sequence[Mapping[str, Any]]],
    as_of_date: str,
    resume: bool,
) -> tuple[tuple[Path, ...], tuple[Path, ...], int]:
    shard_root = root / "shards"
    checkpoint_root = root / "checkpoints"
    shard_paths: list[Path] = []
    checkpoint_paths: list[Path] = []
    reused = 0
    for index, rows in enumerate(shard_rows):
        shard_path = shard_root / f"census_stage_map.shard-{index:04d}.jsonl"
        checkpoint_path = checkpoint_root / f"checkpoint.shard-{index:04d}.json"
        rows_tuple = tuple(rows)
        expected_hash = stable_hash(rows_tuple)
        reusable = False
        if resume and shard_path.exists() and checkpoint_path.exists():
            try:
                existing_rows = _read_jsonl(shard_path)
                checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
                reusable = (
                    stable_hash(existing_rows) == expected_hash
                    and checkpoint.get("status") == "COMPLETE"
                    and checkpoint.get("row_count") == len(rows_tuple)
                    and checkpoint.get("content_hash") == expected_hash
                )
            except (OSError, ValueError, TypeError, json.JSONDecodeError):
                reusable = False
        if reusable:
            reused += 1
        else:
            write_jsonl(shard_path, rows_tuple)
            write_json(
                checkpoint_path,
                {
                    "schema_version": CENSUS_OPERATIONAL_SCHEMA_VERSION,
                    "status": "COMPLETE",
                    "as_of_date": as_of_date,
                    "shard_index": index,
                    "shard_count": len(shard_rows),
                    "row_count": len(rows_tuple),
                    "content_hash": expected_hash,
                },
            )
        shard_paths.append(shard_path)
        checkpoint_paths.append(checkpoint_path)
    return tuple(shard_paths), tuple(checkpoint_paths), reused


def _hard_acceptance_counts(
    *,
    result: CurrentOperationRunnerResult,
    eligible_target_ids: Sequence[str],
    stage_rows: Sequence[Mapping[str, Any]],
    lane_by_target: Mapping[str, Sequence[Any]],
) -> Mapping[str, int]:
    eligible_ids = set(eligible_target_ids)
    row_ids = tuple(str(row.get("target_id") or "") for row in stage_rows)
    timeline_ids = tuple(
        item.target_id
        for item in result.source_timelines
        if item.target_id in eligible_ids
    )
    claim_references = tuple(
        str(claim_id)
        for row in stage_rows
        for claim_id in row.get("accepted_claim_ids") or ()
    )
    provider_failed_targets = {
        target_id
        for target_id, lanes in lane_by_target.items()
        if any(
            lane.lane_status == DailyBaselineLaneStatus.PROVIDER_FAILED.value
            and lane.provider_error
            for lane in lanes
        )
    }
    return {
        "missing_symbol_count": len(eligible_ids - set(row_ids)),
        "duplicate_symbol_count": len(row_ids) - len(set(row_ids)),
        "symbol_outside_eligible_count": len(set(row_ids) - eligible_ids),
        "source_timeline_count_mismatch": abs(len(timeline_ids) - len(eligible_ids)),
        "baseline_lane_count_mismatch": abs(
            len(result.baseline_lanes) - len(eligible_ids) * 4
        ),
        "unknown_default_count": sum(
            not str(row.get("canonical_stage") or "").strip()
            or not str(row.get("terminal_status") or "").strip()
            for row in stage_rows
        ),
        "provider_pending_without_failure_count": sum(
            row.get("terminal_status") == DailyTerminalStatus.PROVIDER_PENDING.value
            and not row.get("provider_gaps")
            and str(row.get("target_id") or "") not in provider_failed_targets
            for row in stage_rows
        ),
        "stage0_without_source_attempt_count": sum(
            row.get("canonical_stage") == CanonicalStage.STAGE_0.value
            and row.get("source_attempted") is not True
            for row in stage_rows
        ),
        "claimless_nonzero_score_count": sum(
            row.get("score_type") != AtomicScoreType.NO_SCORE.value
            and row.get("score_value") is not None
            and not row.get("accepted_claim_ids")
            for row in stage_rows
        ),
        "duplicate_claim_reference_count": len(claim_references)
        - len(set(claim_references)),
    }


def _provider_gap_rows(
    result: CurrentOperationRunnerResult,
    *,
    lane_by_target: Mapping[str, Sequence[Any]],
) -> list[Mapping[str, Any]]:
    rows: list[Mapping[str, Any]] = []
    status_by_target = {item.target_id: item for item in result.stage_statuses}
    for target_id in sorted(status_by_target):
        status = status_by_target[target_id]
        lane_errors = sorted(
            {
                str(lane.provider_error)
                for lane in lane_by_target.get(target_id, ())
                if lane.provider_error
            }
        )
        gaps = sorted(set(status.provider_gaps))
        if gaps or lane_errors:
            rows.append(
                {
                    "target_id": target_id,
                    "target_name": status.target_name,
                    "terminal_status": status.terminal_status,
                    "provider_gaps": gaps,
                    "provider_errors": lane_errors,
                }
            )
    return rows


def _source_gap_rows(result: CurrentOperationRunnerResult) -> list[Mapping[str, Any]]:
    return [
        {
            "target_id": status.target_id,
            "target_name": status.target_name,
            "terminal_status": status.terminal_status,
            "source_gaps": list(status.source_gaps),
            "material_gap_ids": list(status.material_gap_ids),
            "missing_conditions": list(status.missing_conditions),
        }
        for status in sorted(result.stage_statuses, key=lambda item: item.target_id)
        if status.source_gaps or status.material_gap_ids or status.missing_conditions
    ]


def _deep_backfill_rows(
    stage_rows: Sequence[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    pending = {
        DailyTerminalStatus.SOURCE_PENDING.value,
        DailyTerminalStatus.PROVIDER_PENDING.value,
        DailyTerminalStatus.BUDGET_PENDING.value,
        DailyTerminalStatus.NOT_SELECTED_BUDGET.value,
    }
    return [
        {
            "target_id": row["target_id"],
            "target_name": row["target_name"],
            "terminal_status": row["terminal_status"],
            "maximum_depth": row["maximum_depth"],
            "provider_gaps": row.get("provider_gaps") or [],
            "source_gaps": row.get("source_gaps") or [],
            "material_gap_ids": row.get("material_gap_ids") or [],
            "next_action": row["next_action"],
        }
        for row in stage_rows
        if row.get("terminal_status") in pending
    ]


def _write_stage_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = tuple(rows[0]) if rows else (
        "target_id",
        "target_name",
        "canonical_stage",
        "terminal_status",
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: json.dumps(value, ensure_ascii=False, sort_keys=True)
                    if isinstance(value, (list, tuple, dict))
                    else value
                    for key, value in row.items()
                }
            )


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        rows = tuple(json.loads(line) for line in handle if line.strip())
    if any(not isinstance(row, Mapping) for row in rows):
        raise ValueError("Census shard contains a non-object row")
    return rows


def _render_operator_digest(
    *,
    result: CurrentOperationRunnerResult,
    eligible_count: int,
    stage_counts: Mapping[str, int],
    terminal_counts: Mapping[str, int],
    shard_count: int,
    reused_shards: int,
) -> str:
    return "\n".join(
        (
            "# E2R 전체 Census 운영 요약",
            "",
            f"- 기준일: {result.as_of_date}",
            f"- 전체 적격 종목: {eligible_count}",
            f"- Stage 분포: {dict(sorted(stage_counts.items()))}",
            f"- terminal status 분포: {dict(sorted(terminal_counts.items()))}",
            f"- selective-deep 선택: {sum(item.selected_for_deep for item in result.depth_decisions)}",
            f"- deterministic shard: {shard_count}",
            f"- resume 재사용 shard: {reused_shards}",
            "- Stage 0/Pending은 근거 부족 또는 provider/source 상태를 그대로 표시합니다.",
            "- 직접적인 투자 권고: 없음",
            "",
        )
    )


__all__ = [
    "CENSUS_OPERATIONAL_SCHEMA_VERSION",
    "audit_current_census_source_corpus_hash",
    "package_live_census_operation",
]
