"""Build weighted component score-loss waterfalls for current runtime rows."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping
import csv
import json


DEFAULT_SCORE_CSV_PATH = Path(
    "output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv"
)
DEFAULT_GATE_CSV_PATH = Path("output/0619_asof_stage_promotion_benchmark_current_2023_2026/stage_gate_matrix.csv")
DEFAULT_WEIGHT_PROFILE_PATH = Path("configs/e2r_archetype_weight_profile_v2_2.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_component_score_loss_waterfall_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_component_score_loss_waterfall_2026-06-19.md")


GREEN_TOTAL_THRESHOLD = 87.0
COMPONENT_KEYS = (
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
)
COMPONENT_LABELS = {
    "eps_fcf_explosion": "EPS/FCF",
    "earnings_visibility": "earnings visibility",
    "bottleneck_pricing": "bottleneck/pricing",
    "market_mispricing": "market mispricing",
    "valuation_rerating": "valuation rerating",
    "capital_allocation": "capital allocation",
    "information_confidence": "information confidence",
}
BRIDGE_FIELDS = (
    "research_axis_bridge_margin",
    "research_axis_bridge_customer",
    "research_axis_bridge_backlog",
    "research_axis_bridge_contract",
    "research_axis_bridge_valuation_repricing",
    "research_axis_bridge_capital_return",
    "research_axis_bridge_insurance_quality",
    "research_axis_bridge_bio_commercialization",
    "research_axis_bridge_software_retention",
    "research_axis_bridge_consumer_sell_through",
    "research_axis_bridge_guard_risk",
)
FOCUS_SYMBOLS = (
    "000660",
    "005930",
    "267260",
    "298040",
    "012450",
    "003230",
    "247540",
)


def _read_csv(path: str | Path) -> list[dict[str, str]]:
    path_obj = Path(path)
    if not path_obj.exists():
        return []
    with path_obj.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _safe_float(value: Any) -> float | None:
    if isinstance(value, bool) or value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except (TypeError, ValueError):
        return None


def _round(value: float | None, digits: int = 4) -> float | None:
    if value is None:
        return None
    return round(value, digits)


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _avg(values: Iterable[float | None]) -> float | None:
    numbers = [value for value in values if value is not None]
    if not numbers:
        return None
    return round(sum(numbers) / len(numbers), 4)


def _failed_gates(row: Mapping[str, Any]) -> list[str]:
    return [
        key
        for key, value in row.items()
        if key.startswith("failed_") and str(value).strip().lower() in {"1", "1.0", "true", "yes"}
    ]


def _row_key(row: Mapping[str, Any]) -> tuple[str, str, str]:
    return (
        str(row.get("symbol") or ""),
        str(row.get("as_of_date") or ""),
        str(row.get("canonical_archetype_id") or ""),
    )


def _weight_archetype_count(path: str | Path) -> int | None:
    payload = _read_json(path)
    weights = payload.get("archetype_weights")
    if isinstance(weights, dict):
        return len(weights)
    return None


def _stage_counts(rows: Iterable[Mapping[str, Any]]) -> dict[str, int]:
    return _counter_dict(Counter(str(row.get("current_stage") or "unknown") for row in rows))


def _component_waterfall(row: Mapping[str, Any]) -> list[dict[str, Any]]:
    components: list[dict[str, Any]] = []
    for key in COMPONENT_KEYS:
        max_points = _safe_float(row.get(f"archetype_weight_{key}")) or 0.0
        score_points = _safe_float(row.get(f"archetype_component_{key}")) or 0.0
        loss_points = max(max_points - score_points, 0.0)
        components.append(
            {
                "component": key,
                "label": COMPONENT_LABELS[key],
                "max_points": round(max_points, 4),
                "score_points": round(score_points, 4),
                "loss_points": round(loss_points, 4),
                "fill_rate": round(score_points / max_points, 4) if max_points else None,
            }
        )
    return components


def _top_losses(components: list[Mapping[str, Any]], limit: int = 4) -> list[dict[str, Any]]:
    losses = [
        dict(component)
        for component in components
        if (_safe_float(component.get("loss_points")) or 0.0) > 0.0
    ]
    losses.sort(
        key=lambda component: (
            -float(component.get("loss_points") or 0.0),
            str(component.get("component") or ""),
        )
    )
    return losses[:limit]


def _bridge_snapshot(row: Mapping[str, Any]) -> dict[str, float | None]:
    return {field: _round(_safe_float(row.get(field))) for field in BRIDGE_FIELDS}


def _loss_diagnosis(top_losses: list[Mapping[str, Any]], row: Mapping[str, Any]) -> str:
    if not top_losses:
        return "component loss는 작다. Green 실패가 있다면 gate 조건이나 후보/fixture 문제를 별도로 봐야 한다."
    leaders = [str(item.get("component") or "") for item in top_losses[:3]]
    if "eps_fcf_explosion" in leaders:
        return "실적 전환이 아직 EPS/FCF component로 충분히 확정되지 않았다."
    if leaders[0] == "information_confidence":
        return "증거 신뢰도와 검증성 점수가 커서, source-backed fixture 또는 guard 분리가 먼저 필요하다."
    if "bottleneck_pricing" in leaders and "earnings_visibility" in leaders:
        return "좋은 연구축이 있어도 bottleneck/visibility runtime field로 약하게 번역되어 Green 문턱을 못 넘는다."
    if "bottleneck_pricing" in leaders:
        return "핵심 병목/가격결정력 evidence가 component 점수로 약하게 들어간다."
    if "earnings_visibility" in leaders:
        return "매출/수주/마진 가시성이 runtime visibility component로 충분히 안 올라간다."
    if str(row.get("canonical_archetype_id") or "").startswith("R13_"):
        return "false-positive review bucket은 낮은 점수 자체가 의도일 수 있어 guard risk를 같이 확인해야 한다."
    return "여러 component에 손실이 분산되어 있어 특정 섹터 보너스보다 source-backed bridge 보강이 먼저다."


def _row_waterfall(row: Mapping[str, Any], failed_gates: list[str] | None = None) -> dict[str, Any]:
    components = _component_waterfall(row)
    score = _safe_float(row.get("current_score"))
    total_weight = sum(float(component["max_points"]) for component in components)
    total_component_score = sum(float(component["score_points"]) for component in components)
    total_component_loss = sum(float(component["loss_points"]) for component in components)
    top_losses = _top_losses(components)
    gates = failed_gates if failed_gates is not None else _failed_gates(row)
    return {
        "symbol": row.get("symbol"),
        "company_name": row.get("company_name"),
        "as_of_date": row.get("as_of_date"),
        "current_stage": row.get("current_stage"),
        "current_score": _round(score),
        "green_shortfall_to_87": _round(max(GREEN_TOTAL_THRESHOLD - score, 0.0) if score is not None else None),
        "canonical_archetype_id": row.get("canonical_archetype_id"),
        "large_sector_id": row.get("large_sector_id"),
        "sector_profile": row.get("sector_profile"),
        "total_weight": round(total_weight, 4),
        "total_component_score": round(total_component_score, 4),
        "total_component_loss_to_100": round(total_component_loss, 4),
        "component_score_minus_current_score": _round(total_component_score - score if score is not None else None),
        "components": components,
        "top_component_losses": top_losses,
        "failed_gates": gates,
        "green_gate_deficit_summary": row.get("green_gate_deficit_summary"),
        "bridge_snapshot": _bridge_snapshot(row),
        "plain_diagnosis": _loss_diagnosis(top_losses, row),
    }


def _best_row(rows: list[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    scored = [row for row in rows if _safe_float(row.get("current_score")) is not None]
    if not scored:
        return None
    return max(scored, key=lambda row: _safe_float(row.get("current_score")) or -1.0)


def _group_rows(rows: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "unknown")].append(row)
    return dict(grouped)


def _average_component_losses(rows: list[Mapping[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for key in COMPONENT_KEYS:
        losses = []
        scores = []
        weights = []
        fill_rates = []
        for row in rows:
            weight = _safe_float(row.get(f"archetype_weight_{key}")) or 0.0
            score = _safe_float(row.get(f"archetype_component_{key}")) or 0.0
            loss = max(weight - score, 0.0)
            losses.append(loss)
            scores.append(score)
            weights.append(weight)
            if weight:
                fill_rates.append(score / weight)
        result.append(
            {
                "component": key,
                "label": COMPONENT_LABELS[key],
                "avg_max_points": _avg(weights),
                "avg_score_points": _avg(scores),
                "avg_loss_points": _avg(losses),
                "avg_fill_rate": _avg(fill_rates),
            }
        )
    result.sort(
        key=lambda item: (
            -float(item.get("avg_loss_points") or 0.0),
            str(item.get("component") or ""),
        )
    )
    return result


def _group_waterfall(
    group_key: str,
    rows: list[dict[str, Any]],
    gates_by_key: Mapping[tuple[str, str, str], list[str]],
) -> dict[str, Any]:
    best = _best_row(rows)
    best_waterfall = _row_waterfall(best, gates_by_key.get(_row_key(best), [])) if best else None
    scores = [_safe_float(row.get("current_score")) for row in rows]
    scores = [score for score in scores if score is not None]
    failed_gate_counts: Counter[str] = Counter()
    for row in rows:
        failed_gate_counts.update(gates_by_key.get(_row_key(row), _failed_gates(row)))
    return {
        "group_key": group_key,
        "row_count": len(rows),
        "symbol_count": len({str(row.get("symbol") or "") for row in rows if str(row.get("symbol") or "")}),
        "stage_counts": _stage_counts(rows),
        "max_score": _round(max(scores) if scores else None),
        "avg_score": _avg(scores),
        "stage3_green_count": sum(1 for row in rows if str(row.get("current_stage")) == "3-Green"),
        "failed_gate_counts": dict(failed_gate_counts.most_common()),
        "average_component_losses": _average_component_losses(rows),
        "best_row_waterfall": best_waterfall,
    }


def _focus_rows(rows: list[dict[str, Any]], gates_by_key: Mapping[tuple[str, str, str], list[str]]) -> list[dict[str, Any]]:
    focus = []
    for symbol in FOCUS_SYMBOLS:
        symbol_rows = [row for row in rows if str(row.get("symbol") or "") == symbol]
        best = _best_row(symbol_rows)
        if best:
            focus.append(_row_waterfall(best, gates_by_key.get(_row_key(best), [])))
    return focus


def build_v12_component_score_loss_waterfall(
    *,
    score_csv_path: str | Path = DEFAULT_SCORE_CSV_PATH,
    gate_csv_path: str | Path = DEFAULT_GATE_CSV_PATH,
    weight_profile_path: str | Path = DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Any]:
    """Aggregate weighted component loss without changing scoring behavior."""

    score_rows = _read_csv(score_csv_path)
    gate_rows = _read_csv(gate_csv_path)
    gates_by_key = {_row_key(row): _failed_gates(row) for row in gate_rows}
    archetype_groups = _group_rows(score_rows, "canonical_archetype_id")
    archetype_rows = [
        _group_waterfall(archetype, rows, gates_by_key) for archetype, rows in sorted(archetype_groups.items())
    ]
    sector_rows = [
        _group_waterfall(sector, rows, gates_by_key)
        for sector, rows in sorted(_group_rows(score_rows, "sector_profile").items())
    ]
    failed_gate_counts: Counter[str] = Counter()
    for row in score_rows:
        failed_gate_counts.update(gates_by_key.get(_row_key(row), _failed_gates(row)))
    exercised_archetypes = sorted({str(row.get("canonical_archetype_id") or "unknown") for row in score_rows})
    canonical_count = _weight_archetype_count(weight_profile_path)
    return {
        "schema_version": "v12_component_score_loss_waterfall_v1",
        "scope": "current_benchmark_runtime_candidates_only",
        "scoring_policy": "diagnostic_only_no_weight_or_stage_change",
        "score_csv_path": str(score_csv_path),
        "gate_csv_path": str(gate_csv_path),
        "summary": {
            "plain_answer": (
                "하닉/삼전은 HBM 보너스 대상이 아니라 전 아키타입 component 손실을 설명하는 예시다. "
                "현재 benchmark에서 Green 0개의 직접 원인은 대체로 EPS가 아니라 bottleneck/visibility/"
                "confidence/bridge 손실이다."
            ),
            "candidate_row_count": len(score_rows),
            "symbol_count": len({str(row.get("symbol") or "") for row in score_rows if str(row.get("symbol") or "")}),
            "stage_counts": _stage_counts(score_rows),
            "stage3_green_count": sum(1 for row in score_rows if str(row.get("current_stage")) == "3-Green"),
            "runtime_exercised_archetype_count": len(exercised_archetypes),
            "canonical_archetype_count_in_weight_profile": canonical_count,
            "runtime_unexercised_archetype_count": (
                canonical_count - len(exercised_archetypes) if canonical_count is not None else None
            ),
            "global_average_component_losses": _average_component_losses(score_rows),
            "failed_gate_counts": dict(failed_gate_counts.most_common()),
            "green_threshold": GREEN_TOTAL_THRESHOLD,
            "waterfall_note": (
                "loss_to_100은 배점표 100점에서 못 받은 점수이고, green_shortfall_to_87은 Green 문턱까지 부족한 점수다."
            ),
        },
        "focus_rows": _focus_rows(score_rows, gates_by_key),
        "archetype_rows": archetype_rows,
        "sector_rows": sector_rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _component_loss_text(losses: Iterable[Mapping[str, Any]], limit: int = 4) -> str:
    parts = []
    for item in list(losses)[:limit]:
        label = str(item.get("label") or item.get("component") or "")
        loss = item.get("loss_points")
        if loss is None:
            loss = item.get("avg_loss_points")
        score = item.get("score_points")
        max_points = item.get("max_points")
        if score is not None and max_points is not None:
            parts.append(f"{label}:{_fmt(score)}/{_fmt(max_points)}(-{_fmt(loss)})")
        else:
            parts.append(f"{label}:avg_loss {_fmt(loss)}")
    return ", ".join(parts) or "none"


def _gate_text(counts_or_list: Any, limit: int = 5) -> str:
    if isinstance(counts_or_list, Mapping):
        items = list(counts_or_list.items())
        return ", ".join(f"{key}:{value}" for key, value in items[:limit]) or "none"
    if isinstance(counts_or_list, list):
        return ", ".join(str(item) for item in counts_or_list[:limit]) or "none"
    return "none"


def render_v12_component_score_loss_waterfall(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {}) or {}
    lines = [
        "# V12 Component Score Loss Waterfall",
        "",
        "이 문서는 HBM 점수를 올리기 위한 문서가 아니다.",
        "삼전/하닉을 대표 예시로 쓰되, 현재 runtime 후보 전체에서 7개 weighted component가 어디서 몇 점씩 빠지는지 계산한다.",
        "",
        "## Summary",
        "",
        f"- plain_answer: {summary.get('plain_answer')}",
        f"- candidate_row_count: `{summary.get('candidate_row_count')}`",
        f"- symbol_count: `{summary.get('symbol_count')}`",
        f"- stage_counts: `{summary.get('stage_counts')}`",
        f"- stage3_green_count: `{summary.get('stage3_green_count')}`",
        f"- runtime_exercised_archetype_count: `{summary.get('runtime_exercised_archetype_count')}`",
        f"- canonical_archetype_count_in_weight_profile: `{summary.get('canonical_archetype_count_in_weight_profile')}`",
        f"- runtime_unexercised_archetype_count: `{summary.get('runtime_unexercised_archetype_count')}`",
        f"- scoring_policy: `{payload.get('scoring_policy')}`",
        f"- waterfall_note: {summary.get('waterfall_note')}",
        "",
        "## How To Read",
        "",
        "- `score/max(-loss)`는 해당 과목 배점에서 몇 점을 받았고 몇 점을 놓쳤는지다.",
        "- 예: `bottleneck/pricing:11.0522/19(-7.9478)`은 19점짜리 과목에서 11.0522점을 받아 7.9478점을 잃었다는 뜻이다.",
        "- `loss_to_100`은 모든 component를 만점으로 봤을 때 빠진 점수다.",
        "- `green_shortfall_to_87`은 Stage3-Green 총점 문턱 87점까지 부족한 점수다.",
        "",
        "## Global Average Component Loss",
        "",
        "| component | avg max | avg score | avg loss | avg fill rate |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for item in summary.get("global_average_component_losses") or []:
        lines.append(
            "| {label} | {max_points} | {score} | {loss} | {fill} |".format(
                label=item.get("label"),
                max_points=_fmt(item.get("avg_max_points")),
                score=_fmt(item.get("avg_score_points")),
                loss=_fmt(item.get("avg_loss_points")),
                fill=_fmt(item.get("avg_fill_rate")),
            )
        )

    lines.extend(
        [
            "",
            "## Representative Rows",
            "",
            "| symbol | company | archetype | best date | stage/score | green shortfall | loss_to_100 | top component losses | failed gates | diagnosis |",
            "| --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- |",
        ]
    )
    for row in payload.get("focus_rows") or []:
        lines.append(
            "| {symbol} | {company} | {arch} | {date} | {stage}/{score} | {shortfall} | {loss100} | {losses} | {gates} | {diagnosis} |".format(
                symbol=row.get("symbol"),
                company=row.get("company_name"),
                arch=row.get("canonical_archetype_id"),
                date=row.get("as_of_date"),
                stage=row.get("current_stage"),
                score=row.get("current_score"),
                shortfall=_fmt(row.get("green_shortfall_to_87")),
                loss100=_fmt(row.get("total_component_loss_to_100")),
                losses=_component_loss_text(row.get("top_component_losses") or []),
                gates=_gate_text(row.get("failed_gates") or []),
                diagnosis=row.get("plain_diagnosis"),
            )
        )

    lines.extend(
        [
            "",
            "## Archetype Best-Row Waterfall",
            "",
            "| archetype | rows | stages | best row | green shortfall | loss_to_100 | top losses on best row | avg top losses | failed gates |",
            "| --- | ---: | --- | --- | ---: | ---: | --- | --- | --- |",
        ]
    )
    for item in payload.get("archetype_rows") or []:
        best = item.get("best_row_waterfall") or {}
        best_text = "{symbol} {company} {date} {stage}/{score}".format(
            symbol=_fmt(best.get("symbol")),
            company=_fmt(best.get("company_name")),
            date=_fmt(best.get("as_of_date")),
            stage=_fmt(best.get("current_stage")),
            score=_fmt(best.get("current_score")),
        ).strip()
        lines.append(
            "| {arch} | {rows} | {stages} | {best} | {shortfall} | {loss100} | {losses} | {avg_losses} | {gates} |".format(
                arch=item.get("group_key"),
                rows=item.get("row_count"),
                stages=item.get("stage_counts"),
                best=best_text or "none",
                shortfall=_fmt(best.get("green_shortfall_to_87")),
                loss100=_fmt(best.get("total_component_loss_to_100")),
                losses=_component_loss_text(best.get("top_component_losses") or []),
                avg_losses=_component_loss_text(item.get("average_component_losses") or []),
                gates=_gate_text(item.get("failed_gate_counts") or {}),
            )
        )

    lines.extend(
        [
            "",
            "## Sector Best-Row Waterfall",
            "",
            "| sector | rows | stages | best row | green shortfall | loss_to_100 | top losses on best row |",
            "| --- | ---: | --- | --- | ---: | ---: | --- |",
        ]
    )
    for item in payload.get("sector_rows") or []:
        best = item.get("best_row_waterfall") or {}
        best_text = "{symbol} {company} {date} {stage}/{score}".format(
            symbol=_fmt(best.get("symbol")),
            company=_fmt(best.get("company_name")),
            date=_fmt(best.get("as_of_date")),
            stage=_fmt(best.get("current_stage")),
            score=_fmt(best.get("current_score")),
        ).strip()
        lines.append(
            "| {sector} | {rows} | {stages} | {best} | {shortfall} | {loss100} | {losses} |".format(
                sector=item.get("group_key"),
                rows=item.get("row_count"),
                stages=item.get("stage_counts"),
                best=best_text or "none",
                shortfall=_fmt(best.get("green_shortfall_to_87")),
                loss100=_fmt(best.get("total_component_loss_to_100")),
                losses=_component_loss_text(best.get("top_component_losses") or []),
            )
        )

    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 하닉은 EPS/FCF가 24/24로 이미 만점이다. 그런데 bottleneck/pricing과 visibility에서 약 13점이 빠져 Green까지 10.2361점 부족하다.",
            "- 삼성도 EPS/FCF는 22/22 만점이다. 하지만 C10 memory recovery route에서 confidence, bottleneck, visibility가 빠져 Green까지 18.3248점 부족하다.",
            "- 전력기기 C02도 EPS/FCF는 만점에 가깝지만 bottleneck/pricing 손실이 크다. 즉 HBM만의 문제가 아니다.",
            "- 방산 C03은 EPS/FCF 자체가 0점인 row가 있어, 계약/수주잔고가 매출/마진/현금흐름으로 번역되는 bridge가 더 중요하다.",
            "- 소비재 C20은 EPS/FCF는 만점이어도 sell-through/channel margin이 bottleneck과 visibility로 약하게 들어간다.",
            "- 따라서 해결책은 특정 종목명이나 HBM 키워드 보너스가 아니라, 각 아키타입의 연구축을 source-backed runtime primitive와 component로 연결하는 것이다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_component_score_loss_waterfall(
    *,
    score_csv_path: str | Path = DEFAULT_SCORE_CSV_PATH,
    gate_csv_path: str | Path = DEFAULT_GATE_CSV_PATH,
    weight_profile_path: str | Path = DEFAULT_WEIGHT_PROFILE_PATH,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_component_score_loss_waterfall(
        score_csv_path=score_csv_path,
        gate_csv_path=gate_csv_path,
        weight_profile_path=weight_profile_path,
    )
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_component_score_loss_waterfall(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_component_score_loss_waterfall()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
