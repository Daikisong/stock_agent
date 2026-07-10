"""Systemic failure clusters and code-repair history, separate from runtime retry."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.runtime.adaptive_investigation_controller import (
    InvestigationFailureReason,
    InvestigationRound,
    InvestigationRoundStatus,
)


SYSTEMIC_FAILURE_SCHEMA_VERSION = "e2r_systemic_failure_cluster_v1"


class SystemicClusterStatus(str, Enum):
    OPEN = "OPEN"
    REPAIR_IN_PROGRESS = "REPAIR_IN_PROGRESS"
    VERIFIED_REPAIRED = "VERIFIED_REPAIRED"
    NOT_SYSTEMIC = "NOT_SYSTEMIC"


class CodeRepairResult(str, Enum):
    VERIFIED = "VERIFIED"
    FAILED = "FAILED"
    PENDING = "PENDING"


@dataclass(frozen=True)
class SystemicFailureCluster:
    cluster_id: str
    failure_reason: str
    failure_signature: str
    status: str
    occurrence_count: int
    distinct_task_count: int
    task_ids: tuple[str, ...]
    round_ids: tuple[str, ...]
    source_families: tuple[str, ...]
    rejection_ids: tuple[str, ...]
    systemic_code_repair_candidate: bool
    runtime_query_retry_is_code_repair: bool = False
    schema_version: str = SYSTEMIC_FAILURE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        InvestigationFailureReason(self.failure_reason)
        SystemicClusterStatus(self.status)
        if not isinstance(self.systemic_code_repair_candidate, bool) or not isinstance(
            self.runtime_query_retry_is_code_repair, bool
        ):
            raise ValueError("systemic failure cluster flags must be boolean")
        if not all(
            item.strip()
            for item in (self.cluster_id, self.failure_signature)
        ):
            raise ValueError("systemic failure cluster identity is required")
        if self.occurrence_count <= 0 or self.distinct_task_count <= 0:
            raise ValueError("systemic failure cluster counts must be positive")
        if self.distinct_task_count != len(set(self.task_ids)):
            raise ValueError("systemic failure distinct-task count mismatch")
        if self.occurrence_count != len(self.round_ids):
            raise ValueError("systemic failure occurrence count mismatch")
        if self.systemic_code_repair_candidate != (
            self.distinct_task_count >= 2
        ):
            raise ValueError("systemic repair candidacy requires multiple tasks")
        if self.runtime_query_retry_is_code_repair:
            raise ValueError("runtime query retry cannot be labeled code repair")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CodeRepairHistoryEntry:
    repair_id: str
    cluster_id: str
    commit_sha: str
    changed_files: tuple[str, ...]
    verification_tests: tuple[str, ...]
    result: str
    result_detail: str
    repaired_by: str
    runtime_round_ids: tuple[str, ...]
    test_only: bool
    runtime_investigation_action: bool = False

    def __post_init__(self) -> None:
        CodeRepairResult(self.result)
        required = (
            self.repair_id,
            self.cluster_id,
            self.commit_sha,
            self.result_detail,
            self.repaired_by,
        )
        if not all(item.strip() for item in required):
            raise ValueError("code repair history provenance is required")
        if not isinstance(self.test_only, bool):
            raise ValueError("code repair history test_only must be boolean")
        if (
            not self.test_only
            and re.fullmatch(r"[0-9a-f]{7,40}", self.commit_sha) is None
        ):
            raise ValueError("production code repair history requires a git commit SHA")
        for values in (
            self.changed_files,
            self.verification_tests,
            self.runtime_round_ids,
        ):
            if not values or any(not str(item).strip() for item in values):
                raise ValueError("code repair history requires non-empty leaf references")
        if self.runtime_investigation_action:
            raise ValueError("code repair history cannot be a runtime investigation action")

    @classmethod
    def build(
        cls,
        *,
        cluster: SystemicFailureCluster,
        commit_sha: str,
        changed_files: Sequence[str],
        verification_tests: Sequence[str],
        result: CodeRepairResult | str,
        result_detail: str,
        repaired_by: str,
        test_only: bool,
    ) -> "CodeRepairHistoryEntry":
        result_value = CodeRepairResult(result)
        payload = {
            "cluster_id": cluster.cluster_id,
            "commit_sha": commit_sha,
            "changed_files": list(changed_files),
            "tests": list(verification_tests),
            "result": result_value.value,
        }
        return cls(
            repair_id=_stable_id("CODEREPAIR", payload),
            cluster_id=cluster.cluster_id,
            commit_sha=commit_sha,
            changed_files=tuple(dict.fromkeys(changed_files)),
            verification_tests=tuple(dict.fromkeys(verification_tests)),
            result=result_value.value,
            result_detail=result_detail,
            repaired_by=repaired_by,
            runtime_round_ids=cluster.round_ids,
            test_only=test_only,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SystemicRepairLedger:
    ledger_id: str
    clusters: tuple[SystemicFailureCluster, ...]
    code_repair_history: tuple[CodeRepairHistoryEntry, ...]
    runtime_round_count: int
    production_runtime_ready: bool = False
    schema_version: str = SYSTEMIC_FAILURE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not isinstance(self.production_runtime_ready, bool):
            raise ValueError("systemic repair readiness flag must be boolean")
        if not self.ledger_id.strip():
            raise ValueError("systemic repair ledger identity is required")
        cluster_ids = {cluster.cluster_id for cluster in self.clusters}
        if len(cluster_ids) != len(self.clusters):
            raise ValueError("systemic repair ledger contains duplicate clusters")
        if any(
            entry.cluster_id not in cluster_ids for entry in self.code_repair_history
        ):
            raise ValueError("code repair history references unknown cluster")
        if self.runtime_round_count < 0:
            raise ValueError("systemic repair runtime round count cannot be negative")
        if self.production_runtime_ready:
            raise ValueError("systemic repair schema cannot declare runtime ready")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def build_systemic_failure_clusters(
    rounds: Sequence[InvestigationRound],
    *,
    min_distinct_tasks: int = 2,
) -> tuple[SystemicFailureCluster, ...]:
    if min_distinct_tasks < 2:
        raise ValueError("systemic cluster requires at least two distinct tasks")
    grouped: dict[tuple[str, str], list[InvestigationRound]] = {}
    for round_ in rounds:
        if round_.status == InvestigationRoundStatus.RESOLVED.value:
            continue
        if round_.failure is None:
            continue
        signature = _failure_signature(round_)
        grouped.setdefault((round_.failure.reason, signature), []).append(round_)
    clusters: list[SystemicFailureCluster] = []
    for (reason, signature), items in sorted(grouped.items()):
        task_ids = tuple(dict.fromkeys(item.task_id for item in items))
        if len(task_ids) < min_distinct_tasks:
            continue
        round_ids = tuple(item.round_id for item in items)
        source_families = tuple(
            dict.fromkeys(
                source
                for item in items
                for source in item.failure.failed_source_families
            )
        )
        rejection_ids = tuple(
            dict.fromkeys(
                rejection_id
                for item in items
                for rejection_id in item.failure.rejection_ids
            )
        )
        cluster_id = _stable_id(
            "SYSFAIL",
            {
                "reason": reason,
                "signature": signature,
                "task_ids": list(task_ids),
            },
        )
        clusters.append(
            SystemicFailureCluster(
                cluster_id=cluster_id,
                failure_reason=reason,
                failure_signature=signature,
                status=SystemicClusterStatus.OPEN.value,
                occurrence_count=len(items),
                distinct_task_count=len(task_ids),
                task_ids=task_ids,
                round_ids=round_ids,
                source_families=source_families,
                rejection_ids=rejection_ids,
                systemic_code_repair_candidate=True,
            )
        )
    return tuple(clusters)


def build_systemic_repair_ledger(
    *,
    rounds: Sequence[InvestigationRound],
    code_repair_history: Sequence[CodeRepairHistoryEntry] = (),
    min_distinct_tasks: int = 2,
) -> SystemicRepairLedger:
    clusters = build_systemic_failure_clusters(
        rounds,
        min_distinct_tasks=min_distinct_tasks,
    )
    payload = {
        "round_ids": [item.round_id for item in rounds],
        "cluster_ids": [item.cluster_id for item in clusters],
        "repair_ids": [item.repair_id for item in code_repair_history],
    }
    return SystemicRepairLedger(
        ledger_id=_stable_id("SYSLEDGER", payload),
        clusters=clusters,
        code_repair_history=tuple(code_repair_history),
        runtime_round_count=len(rounds),
    )


def with_code_repair_history(
    ledger: SystemicRepairLedger,
    entries: Sequence[CodeRepairHistoryEntry],
) -> SystemicRepairLedger:
    history = tuple(dict.fromkeys((*ledger.code_repair_history, *entries)))
    payload = {
        "cluster_ids": [item.cluster_id for item in ledger.clusters],
        "repair_ids": [item.repair_id for item in history],
        "runtime_round_count": ledger.runtime_round_count,
    }
    return SystemicRepairLedger(
        ledger_id=_stable_id("SYSLEDGER", payload),
        clusters=ledger.clusters,
        code_repair_history=history,
        runtime_round_count=ledger.runtime_round_count,
    )


def write_systemic_repair_ledger(
    path: str | Path,
    ledger: SystemicRepairLedger,
) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(ledger.to_dict(), ensure_ascii=False, sort_keys=True, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return output


def audit_systemic_repair_ledger(
    ledger: SystemicRepairLedger,
) -> Mapping[str, Any]:
    critical = {
        "runtime_retry_labeled_code_repair": sum(
            cluster.runtime_query_retry_is_code_repair for cluster in ledger.clusters
        ),
        "cluster_without_multiple_tasks": sum(
            cluster.distinct_task_count < 2 for cluster in ledger.clusters
        ),
        "history_unknown_cluster": sum(
            entry.cluster_id not in {item.cluster_id for item in ledger.clusters}
            for entry in ledger.code_repair_history
        ),
        "history_without_changed_file_or_test": sum(
            not entry.changed_files or not entry.verification_tests
            for entry in ledger.code_repair_history
        ),
        "history_marked_runtime_action": sum(
            entry.runtime_investigation_action for entry in ledger.code_repair_history
        ),
    }
    return {
        "schema_version": "e2r_systemic_repair_audit_v1",
        "status": (
            "SYSTEMIC_REPAIR_SEPARATION_PASS"
            if ledger.clusters
            and ledger.code_repair_history
            and sum(critical.values()) == 0
            else "SYSTEMIC_REPAIR_SEPARATION_FAIL"
        ),
        "cluster_count": len(ledger.clusters),
        "code_repair_history_count": len(ledger.code_repair_history),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": _sha256(_stable_json(ledger.to_dict())),
        "production_runtime_ready": False,
    }


def _failure_signature(round_: InvestigationRound) -> str:
    assert round_.failure is not None
    detail = re.sub(r"[^0-9a-z가-힣]+", " ", round_.failure.detail.casefold()).strip()
    sources = ",".join(sorted(round_.failure.failed_source_families))
    return _sha256(f"{round_.failure.reason}|{detail}|{sources}")


def _stable_id(prefix: str, payload: Mapping[str, Any]) -> str:
    return f"{prefix}-{_sha256(_stable_json(payload))[:24]}"


def _stable_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


__all__ = [
    "SYSTEMIC_FAILURE_SCHEMA_VERSION",
    "CodeRepairHistoryEntry",
    "CodeRepairResult",
    "SystemicClusterStatus",
    "SystemicFailureCluster",
    "SystemicRepairLedger",
    "audit_systemic_repair_ledger",
    "build_systemic_failure_clusters",
    "build_systemic_repair_ledger",
    "with_code_repair_history",
    "write_systemic_repair_ledger",
]
