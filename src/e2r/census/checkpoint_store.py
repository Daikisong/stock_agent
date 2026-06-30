"""Checkpoint storage for Census shards."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json


@dataclass(frozen=True)
class CensusCheckpoint:
    run_id: str
    as_of_date: str
    shard_count: int
    shard_index: int
    started_at: str
    completed_at: str | None
    processed_symbols: tuple[str, ...] = ()
    failed_symbols: tuple[str, ...] = ()
    pending_symbols: tuple[str, ...] = ()
    source_corpus_hash: str = ""
    config_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "as_of_date": self.as_of_date,
            "shard_count": self.shard_count,
            "shard_index": self.shard_index,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "processed_symbols": list(self.processed_symbols),
            "failed_symbols": list(self.failed_symbols),
            "pending_symbols": list(self.pending_symbols),
            "source_corpus_hash": self.source_corpus_hash,
            "config_hash": self.config_hash,
        }


class CheckpointStore:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> CensusCheckpoint | None:
        if not self.path.exists():
            return None
        import json

        payload = json.loads(self.path.read_text(encoding="utf-8"))
        return CensusCheckpoint(
            run_id=str(payload["run_id"]),
            as_of_date=str(payload["as_of_date"]),
            shard_count=int(payload["shard_count"]),
            shard_index=int(payload["shard_index"]),
            started_at=str(payload["started_at"]),
            completed_at=payload.get("completed_at"),
            processed_symbols=tuple(payload.get("processed_symbols") or ()),
            failed_symbols=tuple(payload.get("failed_symbols") or ()),
            pending_symbols=tuple(payload.get("pending_symbols") or ()),
            source_corpus_hash=str(payload.get("source_corpus_hash") or ""),
            config_hash=str(payload.get("config_hash") or ""),
        )

    def save(self, checkpoint: CensusCheckpoint) -> None:
        write_json(self.path, checkpoint.to_dict())


def create_checkpoint(
    *,
    run_id: str,
    as_of_date: str,
    shard_count: int,
    shard_index: int,
    processed_symbols: Sequence[str],
    failed_symbols: Sequence[str],
    pending_symbols: Sequence[str],
    source_corpus: Any,
    config: Mapping[str, Any],
    completed: bool = False,
) -> CensusCheckpoint:
    return CensusCheckpoint(
        run_id=run_id,
        as_of_date=as_of_date,
        shard_count=shard_count,
        shard_index=shard_index,
        started_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
        completed_at=(datetime.utcnow().isoformat(timespec="seconds") + "Z") if completed else None,
        processed_symbols=tuple(dict.fromkeys(processed_symbols)),
        failed_symbols=tuple(dict.fromkeys(failed_symbols)),
        pending_symbols=tuple(dict.fromkeys(pending_symbols)),
        source_corpus_hash=stable_hash(source_corpus),
        config_hash=stable_hash(config),
    )


def checkpoint_missing_hash_count(payloads: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for row in payloads if not row.get("source_corpus_hash") or not row.get("config_hash"))


__all__ = ["CensusCheckpoint", "CheckpointStore", "checkpoint_missing_hash_count", "create_checkpoint"]
