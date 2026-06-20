"""Audit whether v12 Green/guard fixture rows have exact replay inputs."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
import csv
import json
import re

from .v12_runtime_replay_spec import build_v12_runtime_replay_spec


LOOKBACK_DAYS = 370
RECENT_PRICE_DAYS = 45
DISCLOSURE_LOOKBACK_DAYS = 45


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    path_obj = Path(path)
    if not path_obj.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path_obj.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _read_csv(path: str | Path) -> list[dict[str, Any]]:
    path_obj = Path(path)
    if not path_obj.exists():
        return []
    with path_obj.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _parse_date(value: Any) -> date | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def _parse_datetime_date(value: Any) -> date | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text).date()
    except ValueError:
        return _parse_date(text)


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _symbol(row: dict[str, Any]) -> str:
    return str(row.get("symbol") or "").strip()


def _date_key(row: dict[str, Any], *keys: str) -> date | None:
    for key in keys:
        if key in row and row.get(key):
            return _parse_datetime_date(row.get(key))
    return None


def _asof_visible(row: dict[str, Any], as_of_date: date, *keys: str) -> bool:
    row_date = _date_key(row, *keys)
    return row_date is not None and row_date <= as_of_date


def _rows_by_symbol(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        symbol = _symbol(row)
        if symbol:
            grouped[symbol].append(row)
    return grouped


def _candidate(row: dict[str, Any]) -> dict[str, Any]:
    candidate = row.get("candidate") or {}
    return {
        "case_id": candidate.get("case_id"),
        "trigger_id": candidate.get("trigger_id"),
        "symbol": str(candidate.get("symbol") or "").strip(),
        "as_of_date": str(candidate.get("as_of_date") or "").strip(),
        "trigger_type": candidate.get("trigger_type"),
        "MFE_180D_pct": candidate.get("MFE_180D_pct"),
        "MAE_180D_pct": candidate.get("MAE_180D_pct"),
        "evidence_source": candidate.get("evidence_source"),
        "source_file": candidate.get("source_file"),
        "source_proxy_only": bool(candidate.get("source_proxy_only")),
        "evidence_url_pending": bool(candidate.get("evidence_url_pending")),
    }


def _normalise_url(value: Any) -> str:
    text = str(value or "").strip().strip("[](){}<>,.;\"'")
    if not text:
        return ""
    return text.rstrip("/").lower()


def _extract_urls(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        urls: list[str] = []
        for item in value:
            urls.extend(_extract_urls(item))
        return list(dict.fromkeys(urls))
    text = str(value)
    urls = [_normalise_url(match) for match in re.findall(r"https?://[^\s\]\)\},;]+", text)]
    return [url for url in dict.fromkeys(urls) if url]


def _urls_match(row: dict[str, Any], target_urls: set[str]) -> bool:
    row_url = _normalise_url(row.get("url") or row.get("source_url"))
    return bool(row_url and row_url in target_urls)


def _matching_source_rows(rows: list[dict[str, Any]], target_urls: set[str]) -> list[dict[str, Any]]:
    if not target_urls:
        return list(rows)
    return [row for row in rows if _urls_match(row, target_urls)]


def _spec_rows(spec_payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows = list(spec_payload.get("rows") or [])
    if rows:
        return rows
    if spec_payload.get("archetypes"):
        replay_spec = build_v12_runtime_replay_spec(fixture_payload=spec_payload, coverage_payload={})
        return list(replay_spec.get("rows") or [])
    return []


def _universe_present(universe_rows: list[dict[str, Any]], symbol: str, as_of_date: date) -> bool:
    for row in universe_rows:
        if _symbol(row) != symbol:
            continue
        listed_date = _parse_date(row.get("listed_date"))
        if listed_date is None or listed_date <= as_of_date:
            return True
    return False


def _price_rows(rows: list[dict[str, Any]], symbol: str, as_of_date: date) -> list[dict[str, Any]]:
    start = as_of_date - timedelta(days=LOOKBACK_DAYS)
    result: list[dict[str, Any]] = []
    for row in rows:
        if _symbol(row) != symbol:
            continue
        row_date = _date_key(row, "date", "basDt")
        visible_date = _date_key(row, "as_of_date", "date", "basDt")
        if row_date is None or visible_date is None:
            continue
        if start <= row_date <= as_of_date and visible_date <= as_of_date:
            result.append(row)
    return sorted(result, key=lambda item: str(item.get("date") or item.get("basDt")))


def _financial_rows(rows: list[dict[str, Any]], symbol: str, as_of_date: date) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for row in rows:
        if _symbol(row) != symbol:
            continue
        reported_at = _date_key(row, "reported_at")
        visible_date = _date_key(row, "as_of_date", "reported_at")
        if reported_at is not None and visible_date is not None and reported_at <= as_of_date and visible_date <= as_of_date:
            result.append(row)
    return sorted(result, key=lambda item: str(item.get("reported_at")))


def _disclosure_rows(rows: list[dict[str, Any]], symbol: str, as_of_date: date, *, days: int) -> list[dict[str, Any]]:
    start = as_of_date - timedelta(days=days)
    result: list[dict[str, Any]] = []
    for row in rows:
        if _symbol(row) != symbol:
            continue
        published_at = _date_key(row, "published_at", "observed_at")
        available_at = _date_key(row, "available_at", "as_of_date", "published_at")
        if published_at is None or available_at is None:
            continue
        if start <= published_at <= as_of_date and available_at <= as_of_date:
            result.append(row)
    return sorted(result, key=lambda item: str(item.get("published_at")))


def _latest_date(rows: list[dict[str, Any]], *keys: str) -> str | None:
    dates = [value for value in (_date_key(row, *keys) for row in rows) if value is not None]
    if not dates:
        return None
    return max(dates).isoformat()


def _days_since_latest(rows: list[dict[str, Any]], as_of_date: date, *keys: str) -> int | None:
    latest = _latest_date(rows, *keys)
    if latest is None:
        return None
    return (as_of_date - date.fromisoformat(latest)).days


def _retrospective_missing(
    *,
    universe_present: bool,
    price_count: int,
    recent_price_count: int,
    search_count: int,
    report_count: int,
    requires_source_url_match: bool = False,
) -> list[str]:
    missing: list[str] = []
    if not universe_present:
        missing.append("official_universe")
    if price_count <= 0:
        missing.append("price_history_370d")
    elif recent_price_count <= 0:
        missing.append("recent_price_history_45d")
    if search_count <= 0:
        if requires_source_url_match:
            missing.append("evidence_source_search_snapshot")
        else:
            missing.append("retrospective_search_snapshot")
    if report_count <= 0:
        if requires_source_url_match:
            missing.append("evidence_source_report_text_snapshot")
        else:
            missing.append("report_text_snapshot")
    return missing


def _strict_missing(
    *,
    universe_present: bool,
    price_count: int,
    recent_price_count: int,
    pit_search_count: int,
    pit_report_count: int,
    requires_source_url_match: bool = False,
) -> list[str]:
    missing: list[str] = []
    if not universe_present:
        missing.append("official_universe")
    if price_count <= 0:
        missing.append("price_history_370d")
    elif recent_price_count <= 0:
        missing.append("recent_price_history_45d")
    if pit_search_count <= 0:
        if requires_source_url_match:
            missing.append("pit_evidence_source_search_snapshot")
        else:
            missing.append("pit_search_snapshot")
    if pit_report_count <= 0:
        if requires_source_url_match:
            missing.append("pit_evidence_source_report_text_snapshot")
        else:
            missing.append("pit_report_text_snapshot")
    return missing


def _readiness_status(missing: list[str], *, strict: bool) -> str:
    if not missing:
        return "ready_strict_pit_exact_replay" if strict else "ready_retrospective_exact_replay"
    official_missing = any(
        item in {"official_universe", "price_history_370d", "recent_price_history_45d"} for item in missing
    )
    research_missing = any("snapshot" in item for item in missing)
    if official_missing and research_missing:
        return "missing_official_and_research_inputs"
    if official_missing:
        return "missing_candidate_generation_inputs"
    return "missing_research_snapshot_inputs"


def _root_cause(retrospective_missing: list[str], strict_missing: list[str]) -> str:
    if not retrospective_missing and not strict_missing:
        return "exact_fixture_inputs_archived"
    if not retrospective_missing:
        return "retrospective_replay_possible_but_strict_pit_discovery_not_proven"
    if any(item in {"official_universe", "price_history_370d", "recent_price_history_45d"} for item in retrospective_missing):
        if any("snapshot" in item for item in retrospective_missing):
            return "fixture_official_archive_or_research_snapshots_missing"
        return "fixture_symbol_or_price_history_missing_from_official_archive"
    return "fixture_research_snapshot_not_archived"


def build_v12_exact_fixture_replay_readiness(
    *,
    spec_payload: dict[str, Any],
    universe_rows: list[dict[str, Any]],
    price_rows: list[dict[str, Any]],
    financial_rows: list[dict[str, Any]],
    disclosure_rows: list[dict[str, Any]],
    search_snapshots: list[dict[str, Any]],
    report_snapshots: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build a row-level exact replay input readiness matrix."""

    search_by_symbol = _rows_by_symbol(search_snapshots)
    report_by_symbol = _rows_by_symbol(report_snapshots)
    rows: list[dict[str, Any]] = []
    for spec_row in _spec_rows(spec_payload):
        candidate = _candidate(spec_row)
        symbol = candidate["symbol"]
        as_of_date = _parse_date(candidate["as_of_date"])
        if not symbol or as_of_date is None:
            continue

        prices = _price_rows(price_rows, symbol, as_of_date)
        recent_prices = [
            row
            for row in prices
            if (_date_key(row, "date", "basDt") or date.min) >= as_of_date - timedelta(days=RECENT_PRICE_DAYS)
        ]
        financials = _financial_rows(financial_rows, symbol, as_of_date)
        disclosures_45d = _disclosure_rows(disclosure_rows, symbol, as_of_date, days=DISCLOSURE_LOOKBACK_DAYS)
        disclosures_370d = _disclosure_rows(disclosure_rows, symbol, as_of_date, days=LOOKBACK_DAYS)
        candidate_evidence_urls = set(_extract_urls(candidate.get("evidence_source")))
        symbol_searches = list(search_by_symbol.get(symbol, []))
        symbol_reports = list(report_by_symbol.get(symbol, []))
        retrospective_searches = _matching_source_rows(symbol_searches, candidate_evidence_urls)
        retrospective_reports = _matching_source_rows(symbol_reports, candidate_evidence_urls)
        pit_searches = [
            row for row in retrospective_searches if _asof_visible(row, as_of_date, "search_date", "published_at")
        ]
        pit_reports = [row for row in retrospective_reports if _asof_visible(row, as_of_date, "as_of_date")]
        universe_ok = _universe_present(universe_rows, symbol, as_of_date)

        retrospective_missing = _retrospective_missing(
            universe_present=universe_ok,
            price_count=len(prices),
            recent_price_count=len(recent_prices),
            search_count=len(retrospective_searches),
            report_count=len(retrospective_reports),
            requires_source_url_match=bool(candidate_evidence_urls),
        )
        strict_missing = _strict_missing(
            universe_present=universe_ok,
            price_count=len(prices),
            recent_price_count=len(recent_prices),
            pit_search_count=len(pit_searches),
            pit_report_count=len(pit_reports),
            requires_source_url_match=bool(candidate_evidence_urls),
        )
        rows.append(
            {
                "role": spec_row.get("role"),
                "canonical_archetype_id": spec_row.get("canonical_archetype_id"),
                "large_sector_id": spec_row.get("large_sector_id"),
                "runtime_bridge_group": spec_row.get("runtime_bridge_group"),
                "current_runtime_gap_status": spec_row.get("current_runtime_gap_status"),
                "required_bridge_axes": list(spec_row.get("required_bridge_axes") or ()),
                "current_missing_required_bridge_axes": list(spec_row.get("current_missing_required_bridge_axes") or ()),
                "expected_outcome": spec_row.get("expected_outcome"),
                "candidate": candidate,
                "retrospective_readiness_status": _readiness_status(retrospective_missing, strict=False),
                "strict_pit_readiness_status": _readiness_status(strict_missing, strict=True),
                "retrospective_missing_inputs": retrospective_missing,
                "strict_pit_missing_inputs": strict_missing,
                "root_cause": _root_cause(retrospective_missing, strict_missing),
                "input_counts": {
                    "official_universe_present": universe_ok,
                    "price_bars_370d": len(prices),
                    "recent_price_bars_45d": len(recent_prices),
                    "financial_actuals": len(financials),
                    "disclosures_45d": len(disclosures_45d),
                    "disclosures_370d": len(disclosures_370d),
                    "candidate_evidence_urls": len(candidate_evidence_urls),
                    "symbol_search_snapshots": len(symbol_searches),
                    "symbol_report_snapshots": len(symbol_reports),
                    "retrospective_search_snapshots": len(retrospective_searches),
                    "retrospective_report_snapshots": len(retrospective_reports),
                    "pit_search_snapshots": len(pit_searches),
                    "pit_report_snapshots": len(pit_reports),
                },
                "latest_input_dates": {
                    "latest_price_date": _latest_date(prices, "date", "basDt"),
                    "latest_price_gap_days": _days_since_latest(prices, as_of_date, "date", "basDt"),
                    "latest_financial_reported_at": _latest_date(financials, "reported_at"),
                    "latest_disclosure_published_at": _latest_date(disclosures_370d, "published_at", "observed_at"),
                    "latest_search_date": _latest_date(retrospective_searches, "search_date"),
                    "latest_report_as_of_date": _latest_date(retrospective_reports, "as_of_date"),
                },
            }
        )

    retrospective_status_counts = Counter(str(row["retrospective_readiness_status"]) for row in rows)
    strict_status_counts = Counter(str(row["strict_pit_readiness_status"]) for row in rows)
    root_cause_counts = Counter(str(row["root_cause"]) for row in rows)
    missing_input_counts: Counter[str] = Counter()
    strict_missing_input_counts: Counter[str] = Counter()
    role_status_counts = Counter(f"{row.get('role')}:{row['retrospective_readiness_status']}" for row in rows)
    for row in rows:
        missing_input_counts.update(row["retrospective_missing_inputs"])
        strict_missing_input_counts.update(row["strict_pit_missing_inputs"])

    by_archetype: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_archetype[str(row.get("canonical_archetype_id") or "")].append(row)
    pair_rows: list[dict[str, Any]] = []
    for archetype, archetype_rows in sorted(by_archetype.items()):
        green_rows = [row for row in archetype_rows if row.get("role") == "green"]
        guard_rows = [row for row in archetype_rows if row.get("role") == "guard"]
        green_ready = any(row["retrospective_readiness_status"] == "ready_retrospective_exact_replay" for row in green_rows)
        guard_ready = any(row["retrospective_readiness_status"] == "ready_retrospective_exact_replay" for row in guard_rows)
        green_strict = any(row["strict_pit_readiness_status"] == "ready_strict_pit_exact_replay" for row in green_rows)
        guard_strict = any(row["strict_pit_readiness_status"] == "ready_strict_pit_exact_replay" for row in guard_rows)
        pair_rows.append(
            {
                "canonical_archetype_id": archetype,
                "green_retrospective_ready": green_ready,
                "guard_retrospective_ready": guard_ready,
                "pair_retrospective_ready": green_ready and guard_ready,
                "green_strict_pit_ready": green_strict,
                "guard_strict_pit_ready": guard_strict,
                "pair_strict_pit_ready": green_strict and guard_strict,
                "green_statuses": sorted({row["retrospective_readiness_status"] for row in green_rows}),
                "guard_statuses": sorted({row["retrospective_readiness_status"] for row in guard_rows}),
            }
        )

    return {
        "schema_version": "v12_exact_fixture_replay_readiness_v1",
        "scope": "v12_runtime_replay_spec_rows_vs_local_historical_official_search_report_inputs",
        "spec_row_count": len(rows),
        "fixture_symbol_count": len({row["candidate"]["symbol"] for row in rows}),
        "official_universe_symbol_count": len({_symbol(row) for row in universe_rows if _symbol(row)}),
        "retrospective_ready_count": sum(
            1 for row in rows if row["retrospective_readiness_status"] == "ready_retrospective_exact_replay"
        ),
        "strict_pit_ready_count": sum(1 for row in rows if row["strict_pit_readiness_status"] == "ready_strict_pit_exact_replay"),
        "retrospective_readiness_status_counts": _counter_dict(retrospective_status_counts),
        "strict_pit_readiness_status_counts": _counter_dict(strict_status_counts),
        "root_cause_counts": _counter_dict(root_cause_counts),
        "retrospective_missing_input_counts": _counter_dict(missing_input_counts),
        "strict_pit_missing_input_counts": _counter_dict(strict_missing_input_counts),
        "role_retrospective_status_counts": _counter_dict(role_status_counts),
        "archetype_pair_summary": {
            "archetype_count": len(pair_rows),
            "green_retrospective_ready_count": sum(1 for row in pair_rows if row["green_retrospective_ready"]),
            "guard_retrospective_ready_count": sum(1 for row in pair_rows if row["guard_retrospective_ready"]),
            "pair_retrospective_ready_count": sum(1 for row in pair_rows if row["pair_retrospective_ready"]),
            "green_strict_pit_ready_count": sum(1 for row in pair_rows if row["green_strict_pit_ready"]),
            "guard_strict_pit_ready_count": sum(1 for row in pair_rows if row["guard_strict_pit_ready"]),
            "pair_strict_pit_ready_count": sum(1 for row in pair_rows if row["pair_strict_pit_ready"]),
        },
        "archetype_pair_rows": pair_rows,
        "rows": rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _candidate_text(candidate: dict[str, Any]) -> str:
    return " ".join(
        part
        for part in (
            str(candidate.get("symbol") or "").strip(),
            str(candidate.get("as_of_date") or "").strip(),
            str(candidate.get("case_id") or "").strip(),
        )
        if part
    )


def _counts_text(counts: dict[str, Any]) -> str:
    keys = (
        "price_bars_370d",
        "recent_price_bars_45d",
        "financial_actuals",
        "disclosures_45d",
        "candidate_evidence_urls",
        "symbol_search_snapshots",
        "symbol_report_snapshots",
        "retrospective_search_snapshots",
        "retrospective_report_snapshots",
        "pit_search_snapshots",
        "pit_report_snapshots",
    )
    return ", ".join(f"{key}={counts.get(key, 0)}" for key in keys)


def render_v12_exact_fixture_replay_readiness(payload: dict[str, Any]) -> str:
    rows = list(payload.get("rows", []))
    pair_summary = payload.get("archetype_pair_summary") or {}
    lines = [
        "# V12 Exact Fixture Replay Readiness",
        "",
        "이 문서는 Green/guard fixture 62개가 현재 로컬 historical official/search/report archive로 exact replay 가능한지 점검한다.",
        "HBM 전용 보정이 아니라 전 아키타입에서 입력 아카이브, 후보 funnel, evidence bridge 문제를 분리하기 위한 장부다.",
        "",
        "## Summary",
        "",
        f"- spec_row_count: `{payload.get('spec_row_count', 0)}`",
        f"- fixture_symbol_count: `{payload.get('fixture_symbol_count', 0)}`",
        f"- official_universe_symbol_count: `{payload.get('official_universe_symbol_count', 0)}`",
        f"- retrospective_ready_count: `{payload.get('retrospective_ready_count', 0)}`",
        f"- strict_pit_ready_count: `{payload.get('strict_pit_ready_count', 0)}`",
        f"- retrospective_readiness_status_counts: `{payload.get('retrospective_readiness_status_counts', {})}`",
        f"- strict_pit_readiness_status_counts: `{payload.get('strict_pit_readiness_status_counts', {})}`",
        f"- root_cause_counts: `{payload.get('root_cause_counts', {})}`",
        f"- retrospective_missing_input_counts: `{payload.get('retrospective_missing_input_counts', {})}`",
        f"- strict_pit_missing_input_counts: `{payload.get('strict_pit_missing_input_counts', {})}`",
        f"- role_retrospective_status_counts: `{payload.get('role_retrospective_status_counts', {})}`",
        f"- archetype_pair_summary: `{pair_summary}`",
        "",
        "## Fixture Rows",
        "",
        "| role | archetype | fixture candidate | retrospective status | strict PIT status | input counts | missing inputs | root cause |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(
        rows,
        key=lambda item: (
            str(item.get("retrospective_readiness_status")),
            str(item.get("strict_pit_readiness_status")),
            str(item.get("canonical_archetype_id")),
            str(item.get("role")),
        ),
    ):
        lines.append(
            "| {role} | {arch} | {candidate} | {retro} | {strict} | {counts} | {missing} | {cause} |".format(
                role=row.get("role"),
                arch=row.get("canonical_archetype_id"),
                candidate=_candidate_text(row.get("candidate") or {}),
                retro=row.get("retrospective_readiness_status"),
                strict=row.get("strict_pit_readiness_status"),
                counts=_counts_text(row.get("input_counts") or {}),
                missing=_join(row.get("retrospective_missing_inputs") or []),
                cause=row.get("root_cause"),
            )
        )
    lines.extend(
        [
            "",
            "## Pair Readiness",
            "",
            "| archetype | green retro | guard retro | pair retro | green strict | guard strict | pair strict |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload.get("archetype_pair_rows", []):
        lines.append(
            "| {arch} | {green_retro} | {guard_retro} | {pair_retro} | {green_strict} | {guard_strict} | {pair_strict} |".format(
                arch=row.get("canonical_archetype_id"),
                green_retro=row.get("green_retrospective_ready"),
                guard_retro=row.get("guard_retrospective_ready"),
                pair_retro=row.get("pair_retrospective_ready"),
                green_strict=row.get("green_strict_pit_ready"),
                guard_strict=row.get("guard_strict_pit_ready"),
                pair_strict=row.get("pair_strict_pit_ready"),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- `ready_retrospective_exact_replay`: 현재 replay 방식처럼 저장된 옛 문서 후보를 symbol로 가져오고 문서 날짜를 필터링하면 돌릴 입력이 있다.",
            "- `ready_strict_pit_exact_replay`: 검색 snapshot과 report text snapshot도 as-of date 이전에 저장된 것으로 증명된다.",
            "- 쉬운 예: 하닉 `000660 2024-04-25`는 retrospective 입력은 있지만 search snapshot의 `search_date`가 2026-05-14라 strict PIT discovery까지는 증명되지 않는다.",
            "- 쉬운 예: C21/C23/C28 다수 fixture는 종목이 historical official universe 13개 안에 없어서 점수식 이전에 입력 아카이브가 비어 있다.",
            "- 중요한 점: Green 기준을 낮추는 문제가 아니라, 전 아키타입 fixture를 replay 입력으로 고정하고 각 아키타입의 evidence bridge를 붙여야 한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_exact_fixture_replay_readiness(
    *,
    spec_path: str | Path,
    official_root: str | Path,
    search_snapshot_root: str | Path,
    report_snapshot_root: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    official = Path(official_root)
    search_root = Path(search_snapshot_root)
    report_root = Path(report_snapshot_root)
    payload = build_v12_exact_fixture_replay_readiness(
        spec_payload=_read_json(spec_path),
        universe_rows=_read_csv(official / "universe" / "universe.csv"),
        price_rows=_read_csv(official / "prices" / "prices.csv"),
        financial_rows=_read_csv(official / "financials" / "financials.csv"),
        disclosure_rows=_read_csv(official / "disclosures" / "disclosures.csv"),
        search_snapshots=_read_jsonl(search_root / "search_snapshots.jsonl"),
        report_snapshots=_read_jsonl(report_root / "report_snapshots.jsonl"),
    )
    json_path = Path(output_json_path)
    markdown_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    markdown_path.write_text(render_v12_exact_fixture_replay_readiness(payload), encoding="utf-8")
    return {"json": json_path, "markdown": markdown_path}
