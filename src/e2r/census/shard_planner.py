"""Deterministic shard planning for Census Mode."""

from __future__ import annotations

from typing import Iterable, Mapping, Sequence

from e2r.production.metadata import stable_hash

from .schemas import UniverseInstrument


def shard_for_symbol(symbol: str, shard_count: int) -> int:
    if shard_count <= 0:
        raise ValueError("shard_count must be positive")
    digest = stable_hash({"symbol": str(symbol).zfill(6)})
    return int(digest[:12], 16) % shard_count


def select_shard(
    instruments: Sequence[UniverseInstrument],
    *,
    shard_count: int,
    shard_index: int,
) -> tuple[UniverseInstrument, ...]:
    if shard_index < 0 or shard_index >= shard_count:
        raise ValueError("shard_index must be within shard_count")
    return tuple(item for item in instruments if shard_for_symbol(item.symbol, shard_count) == shard_index)


def merge_stage_maps(stage_rows: Iterable[Mapping[str, object]]) -> tuple[dict[str, object], ...]:
    by_symbol: dict[str, dict[str, object]] = {}
    for row in stage_rows:
        symbol = str(row.get("symbol") or "").zfill(6)
        if symbol and symbol not in by_symbol:
            by_symbol[symbol] = dict(row)
    return tuple(by_symbol[symbol] for symbol in sorted(by_symbol))


def duplicate_symbol_count(rows: Iterable[Mapping[str, object]]) -> int:
    seen: set[str] = set()
    duplicates = 0
    for row in rows:
        symbol = str(row.get("symbol") or "").zfill(6)
        if symbol in seen:
            duplicates += 1
        seen.add(symbol)
    return duplicates


__all__ = ["duplicate_symbol_count", "merge_stage_maps", "select_shard", "shard_for_symbol"]
