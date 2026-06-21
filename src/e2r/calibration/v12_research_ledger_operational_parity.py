"""Compare operational replay output against research-ledger fixture replay."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, timedelta
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


def build_v12_research_ledger_operational_parity_audit(
    *,
    spec_payload: Mapping[str, Any],
    operational_candidates: Sequence[Mapping[str, Any]],
    ledger_candidates: Sequence[Mapping[str, Any]],
    archive_coverage: Sequence[Mapping[str, Any]] = (),
    near_score_tolerance: float = 5.0,
) -> dict[str, Any]:
    """Classify whether research-ledger Green cases reach parity operationally."""

    operational_by_key = _rows_by_symbol_date(
        row for row in operational_candidates if row.get("candidate_source_path") != "runtime_fixture_spec"
    )
    ledger_fixture_rows = [row for row in ledger_candidates if row.get("candidate_source_path") == "runtime_fixture_spec"]
    ledger_exact_by_key_arch = _fixture_rows_by_symbol_date_arch(
        row for row in ledger_fixture_rows if not _is_carried_forward(row)
    )
    ledger_exact_by_key = _rows_by_symbol_date(
        row for row in ledger_fixture_rows if not _is_carried_forward(row)
    )
    ledger_carried_rows = [row for row in ledger_fixture_rows if _is_carried_forward(row)]
    archive_by_key = {
        (str(row.get("symbol") or ""), str(row.get("as_of_date") or "")): row
        for row in archive_coverage
    }

    green_rows: list[dict[str, Any]] = []
    guard_rows: list[dict[str, Any]] = []
    for spec_row in spec_payload.get("rows", []):
        role = str(spec_row.get("role") or "")
        candidate = spec_row.get("candidate") if isinstance(spec_row.get("candidate"), Mapping) else {}
        symbol = str(candidate.get("symbol") or "")
        as_of_date = str(candidate.get("as_of_date") or "")
        archetype = str(spec_row.get("canonical_archetype_id") or "")
        if not symbol or not as_of_date or not archetype:
            continue
        operational_best = _best_score_row(operational_by_key.get((symbol, as_of_date), ()))
        fixture_rows = ledger_exact_by_key_arch.get((symbol, as_of_date, archetype), ())
        fixture_match_mode = "exact_archetype" if fixture_rows else None
        if not fixture_rows and role == "green" and archetype.startswith("R13_"):
            fixture_rows = _source_archetype_fixture_fallback(
                ledger_exact_by_key.get((symbol, as_of_date), ()),
            )
            if fixture_rows:
                fixture_match_mode = "source_archetype_fallback"
        fixture_best = _best_score_row(fixture_rows)
        row = _case_audit_row(
            role=role,
            archetype=archetype,
            symbol=symbol,
            as_of_date=as_of_date,
            operational=operational_best,
            fixture=fixture_best,
            fixture_match_mode=fixture_match_mode,
            archive=archive_by_key.get((symbol, as_of_date)),
            near_score_tolerance=near_score_tolerance,
        )
        if role == "green":
            green_rows.append(row)
        elif role == "guard":
            guard_rows.append(row)

    carried_summary = _carried_summary(ledger_carried_rows, operational_by_key, near_score_tolerance=near_score_tolerance)
    green_bucket_counts = Counter(row["bucket"] for row in green_rows)
    guard_bucket_counts = Counter(row["bucket"] for row in guard_rows)
    green_missing_lane_counts = Counter(
        row["operational_missing_lane"]
        for row in green_rows
        if row["bucket"] == "operational_missing"
    )
    by_archetype: dict[str, dict[str, Any]] = {}
    for row in [*green_rows, *guard_rows]:
        archetype = row["canonical_archetype_id"]
        item = by_archetype.setdefault(
            archetype,
            {
                "canonical_archetype_id": archetype,
                "green_buckets": {},
                "guard_buckets": {},
                "green_case_count": 0,
                "guard_case_count": 0,
            },
        )
        key = "green_buckets" if row["role"] == "green" else "guard_buckets"
        item[key][row["bucket"]] = item[key].get(row["bucket"], 0) + 1
        item[f"{row['role']}_case_count"] += 1

    return {
        "schema_version": "v12_research_ledger_operational_parity_audit_v1",
        "near_score_tolerance": near_score_tolerance,
        "summary": {
            "green_case_count": len(green_rows),
            "guard_case_count": len(guard_rows),
            "green_bucket_counts": dict(sorted(green_bucket_counts.items())),
            "guard_bucket_counts": dict(sorted(guard_bucket_counts.items())),
            "green_missing_lane_counts": dict(sorted(green_missing_lane_counts.items())),
            "carried_fixture_count": len(ledger_carried_rows),
            "carried_fixture_green_count": sum(1 for row in ledger_carried_rows if row.get("stage") == "3-Green"),
        },
        "by_archetype": sorted(by_archetype.values(), key=lambda item: item["canonical_archetype_id"]),
        "green_rows": sorted(green_rows, key=lambda row: (row["bucket"], row["canonical_archetype_id"], row["symbol"])),
        "guard_rows": sorted(guard_rows, key=lambda row: (row["bucket"], row["canonical_archetype_id"], row["symbol"])),
        "carried_summary": carried_summary,
    }


def render_v12_research_ledger_operational_parity_audit(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    lines = [
        "# V12 Research-Ledger Operational Parity Audit",
        "",
        "이 감사는 운영-only replay와 연구-ledger fixture replay를 비교해 차이를 분류한다.",
        "투자 판단 출력이 아니라, candidate funnel / evidence conversion / score gap 중 어디가 막혔는지 찾기 위한 진단이다.",
        "",
        "## Summary",
        "",
        f"- green_case_count: `{summary.get('green_case_count', 0)}`",
        f"- guard_case_count: `{summary.get('guard_case_count', 0)}`",
        f"- green_bucket_counts: `{summary.get('green_bucket_counts', {})}`",
        f"- guard_bucket_counts: `{summary.get('guard_bucket_counts', {})}`",
        f"- green_missing_lane_counts: `{summary.get('green_missing_lane_counts', {})}`",
        f"- carried_fixture_count: `{summary.get('carried_fixture_count', 0)}`",
        f"- carried_fixture_green_count: `{summary.get('carried_fixture_green_count', 0)}`",
        "",
        "## Green Rows",
        "",
        "| bucket | missing lane | archetype | symbol | as-of | operational | ledger fixture | gap |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in payload.get("green_rows", []):
        lines.append(_markdown_case_row(row))
    lines.extend(
        [
            "",
            "## Guard Rows",
            "",
            "| bucket | missing lane | archetype | symbol | as-of | operational | ledger fixture | gap |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload.get("guard_rows", []):
        lines.append(_markdown_case_row(row))
    lines.extend(
        [
            "",
            "## Bucket Meaning",
            "",
            "- `operational_missing`: 운영 replay에서 같은 symbol/as-of 후보가 생성되지 않았다. `missing lane`을 먼저 본다.",
            "- `archive_universe_missing`: 해당 as-of 공식 universe에 종목이 없다.",
            "- `archive_price_missing`: universe에는 있지만 가격 anchor가 부족하다.",
            "- `archive_input_family_missing`: universe에는 있지만 가격/재무/공시 입력 가족이 거의 없다.",
            "- `candidate_funnel_missing`: archive 입력은 있는데 후보 생성에서 빠졌다.",
            "- `operational_archetype_mismatch`: 운영 후보는 있으나 spec 아키타입이 아닌 다른 아키타입으로 채점됐다.",
            "- `ledger_only_green`: 운영 후보는 있지만 연구-ledger fixture를 붙여야 Green이 된다.",
            "- `operational_green_score_gap`: 운영도 Green이나 연구-ledger 점수와 허용 차이보다 크다.",
            "- `near_parity_green`: 운영과 연구-ledger가 둘 다 Green이고 점수 차이가 허용 범위 안이다.",
            "- `guard_pass`: guard fixture가 Green으로 열리지 않았다.",
            "- `guard_fail_false_green`: guard fixture가 Green으로 열렸다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_research_ledger_operational_parity_audit(
    *,
    spec_path: str | Path,
    operational_candidates_path: str | Path,
    ledger_candidates_path: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
    official_root: str | Path | None = None,
    near_score_tolerance: float = 5.0,
) -> dict[str, Path]:
    spec_payload = _read_json(spec_path)
    payload = build_v12_research_ledger_operational_parity_audit(
        spec_payload=spec_payload,
        operational_candidates=_read_json(operational_candidates_path),
        ledger_candidates=_read_json(ledger_candidates_path),
        archive_coverage=build_archive_coverage_from_spec(spec_payload, official_root=official_root) if official_root else (),
        near_score_tolerance=near_score_tolerance,
    )
    json_path = Path(output_json_path)
    markdown_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    markdown_path.write_text(render_v12_research_ledger_operational_parity_audit(payload), encoding="utf-8")
    return {"json": json_path, "markdown": markdown_path}


def build_archive_coverage_from_spec(
    spec_payload: Mapping[str, Any],
    *,
    official_root: str | Path = "data/historical_official",
) -> tuple[dict[str, Any], ...]:
    from e2r.backtest.historical_official_store import HistoricalOfficialStore
    from e2r.models import Market

    store = HistoricalOfficialStore(official_root)
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for spec_row in spec_payload.get("rows", []):
        candidate = spec_row.get("candidate") if isinstance(spec_row.get("candidate"), Mapping) else {}
        symbol = str(candidate.get("symbol") or "")
        as_of_text = str(candidate.get("as_of_date") or "")
        if not symbol or not as_of_text or (symbol, as_of_text) in seen:
            continue
        seen.add((symbol, as_of_text))
        try:
            as_of_date = date.fromisoformat(as_of_text)
        except ValueError:
            continue
        universe = store.load_universe(as_of_date, Market.KR)
        prices = store.load_price_bars(symbol, as_of_date - timedelta(days=370), as_of_date, as_of_date)
        financials = store.load_financial_actuals(symbol, as_of_date)
        disclosures = store.load_disclosures(symbol, as_of_date - timedelta(days=370), as_of_date, as_of_date)
        rows.append(
            {
                "symbol": symbol,
                "as_of_date": as_of_text,
                "universe_present": any(item.symbol == symbol for item in universe),
                "universe_size": len(universe),
                "price_count": len(prices),
                "financial_count": len(financials),
                "disclosure_count": len(disclosures),
            }
        )
    return tuple(rows)


def _case_audit_row(
    *,
    role: str,
    archetype: str,
    symbol: str,
    as_of_date: str,
    operational: Mapping[str, Any] | None,
    fixture: Mapping[str, Any] | None,
    fixture_match_mode: str | None,
    archive: Mapping[str, Any] | None,
    near_score_tolerance: float,
) -> dict[str, Any]:
    operational_stage = _stage(operational)
    fixture_stage = _stage(fixture)
    operational_score = _score(operational)
    fixture_score = _score(fixture)
    score_gap = None
    if operational_score is not None and fixture_score is not None:
        score_gap = round(fixture_score - operational_score, 4)
    if role == "guard":
        bucket = "guard_fail_false_green" if operational_stage == "3-Green" or fixture_stage == "3-Green" else "guard_pass"
    elif operational is None:
        bucket = "operational_missing"
    elif fixture is None:
        bucket = "fixture_missing"
    elif not _operational_archetype_matches(archetype, operational):
        bucket = "operational_archetype_mismatch"
    elif operational_stage == "3-Green" and fixture_stage == "3-Green" and score_gap is not None and abs(score_gap) <= near_score_tolerance:
        bucket = "near_parity_green"
    elif operational_stage == "3-Green" and fixture_stage == "3-Green":
        bucket = "operational_green_score_gap"
    elif fixture_stage == "3-Green":
        bucket = "ledger_only_green"
    else:
        bucket = "both_not_green"
    return {
        "role": role,
        "bucket": bucket,
        "canonical_archetype_id": archetype,
        "symbol": symbol,
        "as_of_date": as_of_date,
        "operational_stage": operational_stage,
        "operational_score": operational_score,
        "operational_candidate_source_path": operational.get("candidate_source_path") if operational else None,
        "operational_matched_archetype": _operational_archetype(operational),
        "operational_archetype_match": _operational_archetype_matches(archetype, operational),
        "operational_contract_coverage_pct": _float_field(operational, "evidence_contract_coverage_pct"),
        "operational_contract_positive_coverage_pct": _float_field(operational, "evidence_contract_positive_coverage_pct"),
        "operational_contract_positive_missing_primitive_count": _float_field(
            operational,
            "evidence_contract_positive_missing_primitive_count",
        ),
        "operational_contract_green_gate_coverage_pct": _float_field(
            operational,
            "evidence_contract_green_gate_coverage_pct",
        ),
        "operational_contract_green_gate_missing_primitive_count": _float_field(
            operational,
            "evidence_contract_green_gate_missing_primitive_count",
        ),
        "operational_contract_guard_present_primitive_count": _float_field(
            operational,
            "evidence_contract_guard_present_primitive_count",
        ),
        "operational_contract_guard_missing_primitive_count": _float_field(
            operational,
            "evidence_contract_guard_missing_primitive_count",
        ),
        "operational_contract_positive_missing_primitives": _text_field(
            operational,
            "evidence_contract_positive_missing_primitives",
        ),
        "operational_contract_green_gate_missing_primitives": _text_field(
            operational,
            "evidence_contract_green_gate_missing_primitives",
        ),
        "operational_contract_guard_present_primitives": _text_field(
            operational,
            "evidence_contract_guard_present_primitives",
        ),
        "operational_contract_guard_missing_primitives": _text_field(
            operational,
            "evidence_contract_guard_missing_primitives",
        ),
        "operational_missing_lane": _operational_missing_lane(operational=operational, archive=archive),
        "archive_universe_present": archive.get("universe_present") if archive else None,
        "archive_price_count": archive.get("price_count") if archive else None,
        "archive_financial_count": archive.get("financial_count") if archive else None,
        "archive_disclosure_count": archive.get("disclosure_count") if archive else None,
        "ledger_stage": fixture_stage,
        "ledger_score": fixture_score,
        "ledger_match_mode": fixture_match_mode,
        "ledger_matched_archetype": _archetype_from_reason_codes(fixture.get("reason_codes", ())) if fixture else None,
        "score_gap": score_gap,
    }


def _operational_archetype(row: Mapping[str, Any] | None) -> str | None:
    if row is None:
        return None
    value = row.get("canonical_archetype_id")
    if value:
        return str(value)
    return None


def _operational_archetype_matches(spec_archetype: str, row: Mapping[str, Any] | None) -> bool:
    operational_archetype = _operational_archetype(row)
    if row is None or not operational_archetype:
        return True
    if spec_archetype.startswith("R13_"):
        return True
    return operational_archetype == spec_archetype


def _carried_summary(
    rows: Sequence[Mapping[str, Any]],
    operational_by_key: Mapping[tuple[str, str], Sequence[Mapping[str, Any]]],
    *,
    near_score_tolerance: float,
) -> list[dict[str, Any]]:
    by_archetype: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        archetype = _archetype_from_reason_codes(row.get("reason_codes", ()))
        best = _best_score_row(operational_by_key.get((str(row.get("symbol") or ""), str(row.get("as_of_date") or "")), ()))
        gap = None
        if best is not None and _score(best) is not None and _score(row) is not None:
            gap = _score(row) - _score(best)
        bucket = by_archetype[archetype]
        bucket["total"] += 1
        if row.get("stage") == "3-Green":
            bucket["fixture_green"] += 1
        if _stage(best) == "3-Green":
            bucket["operational_green"] += 1
        if gap is not None and abs(gap) <= near_score_tolerance:
            bucket["near_score"] += 1
    return [
        {"canonical_archetype_id": archetype, **dict(counts)}
        for archetype, counts in sorted(by_archetype.items())
    ]


def _rows_by_symbol_date(rows: Sequence[Mapping[str, Any]]) -> dict[tuple[str, str], tuple[Mapping[str, Any], ...]]:
    grouped: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("symbol") or ""), str(row.get("as_of_date") or ""))].append(row)
    return {key: tuple(value) for key, value in grouped.items()}


def _fixture_rows_by_symbol_date_arch(rows: Sequence[Mapping[str, Any]]) -> dict[tuple[str, str, str], tuple[Mapping[str, Any], ...]]:
    grouped: dict[tuple[str, str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("symbol") or ""), str(row.get("as_of_date") or ""), _archetype_from_reason_codes(row.get("reason_codes", ())))].append(row)
    return {key: tuple(value) for key, value in grouped.items()}


def _source_archetype_fixture_fallback(rows: Sequence[Mapping[str, Any]]) -> tuple[Mapping[str, Any], ...]:
    green_rows = tuple(
        row
        for row in rows
        if _fixture_role_from_reason_codes(row.get("reason_codes", ())) == "green"
    )
    archetypes = {
        archetype
        for row in green_rows
        if (archetype := _archetype_from_reason_codes(row.get("reason_codes", ())))
    }
    if len(archetypes) != 1:
        return ()
    return green_rows


def _best_score_row(rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    if not rows:
        return None
    return max(rows, key=lambda row: _score(row) if _score(row) is not None else float("-inf"))


def _is_carried_forward(row: Mapping[str, Any]) -> bool:
    return "fixture_carried_forward" in tuple(row.get("reason_codes") or ())


def _archetype_from_reason_codes(reason_codes: Any) -> str:
    for code in tuple(reason_codes or ()):
        text = str(code)
        if text.startswith("C") or text.startswith("R13_"):
            return text
    return ""


def _fixture_role_from_reason_codes(reason_codes: Any) -> str:
    for code in tuple(reason_codes or ()):
        text = str(code)
        if text.startswith("fixture_role:"):
            return text.split(":", 1)[1].strip().lower()
    return ""


def _score(row: Mapping[str, Any] | None) -> float | None:
    if row is None or row.get("score") is None:
        return None
    try:
        return round(float(row["score"]), 4)
    except (TypeError, ValueError):
        return None


def _float_field(row: Mapping[str, Any] | None, key: str) -> float | None:
    if row is None or row.get(key) in (None, ""):
        return None
    try:
        return round(float(row[key]), 4)
    except (TypeError, ValueError):
        return None


def _text_field(row: Mapping[str, Any] | None, key: str) -> str | None:
    if row is None or row.get(key) in (None, ""):
        return None
    return str(row[key])


def _stage(row: Mapping[str, Any] | None) -> str:
    if row is None:
        return "missing"
    return str(row.get("stage") or "missing")


def _markdown_case_row(row: Mapping[str, Any]) -> str:
    operational = f"{row.get('operational_stage')}:{row.get('operational_score')}"
    if row.get("operational_contract_positive_coverage_pct") is not None:
        operational = (
            f"{operational}<br/>pos_cov={row.get('operational_contract_positive_coverage_pct')}"
            f" missing+={row.get('operational_contract_positive_missing_primitive_count')}"
            f" gate_cov={row.get('operational_contract_green_gate_coverage_pct')}"
            f" gate_missing={row.get('operational_contract_green_gate_missing_primitive_count')}"
            f" guard_present={row.get('operational_contract_guard_present_primitive_count')}"
            f" guard_missing={row.get('operational_contract_guard_missing_primitive_count')}"
        )
    fixture = f"{row.get('ledger_stage')}:{row.get('ledger_score')}"
    return (
        f"| {row.get('bucket')} | {row.get('operational_missing_lane') or ''} | "
        f"{row.get('canonical_archetype_id')} | {row.get('symbol')} | "
        f"{row.get('as_of_date')} | {operational} | {fixture} | {row.get('score_gap')} |"
    )


def _operational_missing_lane(*, operational: Mapping[str, Any] | None, archive: Mapping[str, Any] | None) -> str | None:
    if operational is not None:
        return None
    if not archive:
        return "unknown_archive_coverage"
    if not archive.get("universe_present"):
        return "archive_universe_missing"
    if int(archive.get("price_count") or 0) == 0:
        return "archive_price_missing"
    if int(archive.get("financial_count") or 0) == 0 and int(archive.get("disclosure_count") or 0) == 0:
        return "archive_input_family_missing"
    return "candidate_funnel_missing"


def _read_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


__all__ = [
    "build_archive_coverage_from_spec",
    "build_v12_research_ledger_operational_parity_audit",
    "render_v12_research_ledger_operational_parity_audit",
    "write_v12_research_ledger_operational_parity_audit",
]
