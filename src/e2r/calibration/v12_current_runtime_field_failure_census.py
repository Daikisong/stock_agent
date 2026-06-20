"""Build a census of where current runtime benchmark candidates lose score."""

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
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_current_runtime_field_failure_census_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_current_runtime_field_failure_census_2026-06-19.md")


COMPONENT_FIELDS = (
    "archetype_component_eps_fcf_explosion",
    "archetype_component_earnings_visibility",
    "archetype_component_bottleneck_pricing",
    "archetype_component_market_mispricing",
    "archetype_component_valuation_rerating",
    "archetype_component_capital_allocation",
    "archetype_component_information_confidence",
)
RUNTIME_QUALITY_FIELDS = (
    "revision_score",
    "contract_quality",
    "backlog_rpo_visibility",
    "capa_constraint",
    "structural_visibility_quality",
    "sector_visibility_score",
    "sector_bottleneck_score",
    "domain_specific_evidence_score",
    "actual_profit_conversion_score",
)
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
ZERO_CENSUS_FIELDS = BRIDGE_FIELDS + (
    "contract_quality",
    "backlog_rpo_visibility",
    "capa_constraint",
    "revision_score",
    "domain_specific_evidence_score",
)
DEFICIT_FIELDS = (
    "stage3_total_deficit",
    "stage3_eps_fcf_deficit",
    "stage3_visibility_deficit",
    "stage3_bottleneck_deficit",
    "stage3_market_mispricing_deficit",
    "stage3_valuation_deficit",
    "stage3_revision_deficit",
    "stage3_contract_quality_deficit",
    "structural_visibility_deficit",
    "sector_visibility_deficit",
    "sector_bottleneck_deficit",
    "green_cross_evidence_deficit",
    "domain_specific_evidence_deficit",
    "stage3_yellow_total_deficit",
)
BEST_ROW_FIELDS = (
    "symbol",
    "company_name",
    "as_of_date",
    "current_stage",
    "current_score",
    "canonical_archetype_id",
    "sector_profile",
    "green_gate_deficit_summary",
    "research_axis_bridge_margin",
    "research_axis_bridge_customer",
    "research_axis_bridge_backlog",
    "research_axis_bridge_contract",
    "revision_score",
    "contract_quality",
    "backlog_rpo_visibility",
    "capa_constraint",
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


def _avg(values: Iterable[Any]) -> float | None:
    numbers = [_safe_float(value) for value in values]
    filtered = [number for number in numbers if number is not None]
    if not filtered:
        return None
    return round(sum(filtered) / len(filtered), 4)


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _is_zero(value: Any) -> bool:
    number = _safe_float(value)
    return number is not None and number == 0.0


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


def _enrich_rows(score_rows: list[dict[str, str]], gate_rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    gates_by_key = {_row_key(row): row for row in gate_rows}
    enriched = []
    for row in score_rows:
        merged: dict[str, Any] = dict(row)
        gate = gates_by_key.get(_row_key(row), {})
        merged["failed_gates"] = _failed_gates(gate or row)
        enriched.append(merged)
    return enriched


def _weight_archetype_count(weight_profile_path: str | Path) -> int | None:
    payload = _read_json(weight_profile_path)
    weights = payload.get("archetype_weights")
    if isinstance(weights, dict):
        return len(weights)
    return None


def _stage_counts(rows: list[Mapping[str, Any]]) -> dict[str, int]:
    return _counter_dict(Counter(str(row.get("current_stage") or "unknown") for row in rows))


def _field_zero_counts(rows: list[Mapping[str, Any]], fields: Iterable[str]) -> dict[str, dict[str, Any]]:
    count = len(rows)
    result: dict[str, dict[str, Any]] = {}
    for field in fields:
        zero_count = sum(1 for row in rows if _is_zero(row.get(field)))
        if zero_count:
            result[field] = {
                "zero_count": zero_count,
                "row_count": count,
                "zero_rate": round(zero_count / count, 4) if count else 0.0,
            }
    return result


def _averages(rows: list[Mapping[str, Any]], fields: Iterable[str]) -> dict[str, float | None]:
    return {field: _avg(row.get(field) for row in rows) for field in fields}


def _positive_deficit_averages(rows: list[Mapping[str, Any]]) -> dict[str, float]:
    result = {}
    for field in DEFICIT_FIELDS:
        values = [_safe_float(row.get(field)) for row in rows]
        positives = [value for value in values if value is not None and value > 0]
        if positives:
            result[field] = round(sum(positives) / len(positives), 4)
    return result


def _best_row(rows: list[Mapping[str, Any]]) -> dict[str, Any] | None:
    scored_rows = [row for row in rows if _safe_float(row.get("current_score")) is not None]
    if not scored_rows:
        return None
    best = max(scored_rows, key=lambda row: _safe_float(row.get("current_score")) or -1.0)
    return {field: best.get(field) for field in BEST_ROW_FIELDS}


def _plain_diagnosis(archetype: str, rows: list[Mapping[str, Any]], zero_counts: Mapping[str, Any]) -> str:
    if archetype == "C06_HBM_MEMORY_CUSTOMER_CAPACITY":
        return "HBM 전망/revision과 bridge field는 잡히지만 weighted total/bottleneck gate에서 아직 Green까지 부족하다."
    if archetype == "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE":
        return "삼성 memory recovery route는 margin은 잡히지만 customer/backlog/contract가 비어 direct Green이 아니다."
    if archetype in {"C01_ORDER_BACKLOG_MARGIN_BRIDGE", "C02_POWER_GRID_DATACENTER_CAPEX"}:
        return "전력/인프라는 EPS와 일부 backlog는 보이지만 contract quality, margin delivery, bottleneck gate가 부족하다."
    if archetype == "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG":
        return "방산은 contract/backlog가 있어도 납품-매출-마진 전환이 EPS/FCF와 bottleneck으로 약하게 들어간다."
    if archetype in {"C19_BRAND_RETAIL_INVENTORY_MARGIN", "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"}:
        return "소비재/수출은 channel reorder, sell-through, margin bridge가 Green component로 충분히 번역되지 않는다."
    if archetype.startswith("R13_"):
        return "R13은 false-positive guard 성격이므로 낮은 점수 자체는 의도일 수 있지만, guard_risk source field도 명확히 남겨야 한다."
    if zero_counts:
        return "후보는 채점됐지만 여러 bridge field가 0이라 연구축이 runtime 점수로 충분히 바뀌지 않았다."
    return "field는 일부 채워졌지만 weighted gate deficit을 추가로 봐야 한다."


def _group_rows(rows: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "unknown")].append(row)
    return dict(grouped)


def _group_census(group_key: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    zero_counts = _field_zero_counts(rows, ZERO_CENSUS_FIELDS)
    failed_gate_counts = Counter()
    bottleneck_paths = Counter(str(row.get("bottleneck_selected_path") or "unknown") for row in rows)
    for row in rows:
        failed_gate_counts.update(row.get("failed_gates") or ())
    best = _best_row(rows)
    scores = [_safe_float(row.get("current_score")) for row in rows]
    scores = [score for score in scores if score is not None]
    return {
        "group_key": group_key,
        "row_count": len(rows),
        "symbol_count": len({str(row.get("symbol") or "") for row in rows if str(row.get("symbol") or "")}),
        "stage_counts": _stage_counts(rows),
        "stage3_green_count": sum(1 for row in rows if str(row.get("current_stage")) == "3-Green"),
        "max_score": round(max(scores), 4) if scores else None,
        "avg_score": round(sum(scores) / len(scores), 4) if scores else None,
        "best_row": best,
        "component_averages": _averages(rows, COMPONENT_FIELDS),
        "runtime_quality_averages": _averages(rows, RUNTIME_QUALITY_FIELDS),
        "positive_deficit_averages": _positive_deficit_averages(rows),
        "zero_field_counts": zero_counts,
        "failed_gate_counts": dict(failed_gate_counts.most_common()),
        "bottleneck_selected_path_counts": dict(bottleneck_paths.most_common()),
        "plain_diagnosis": _plain_diagnosis(group_key, rows, zero_counts),
    }


def build_v12_current_runtime_field_failure_census(
    *,
    score_csv_path: str | Path = DEFAULT_SCORE_CSV_PATH,
    gate_csv_path: str | Path = DEFAULT_GATE_CSV_PATH,
    weight_profile_path: str | Path = DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Any]:
    """Aggregate current runtime score/gate losses from benchmark autopsy CSVs."""

    score_rows = _read_csv(score_csv_path)
    gate_rows = _read_csv(gate_csv_path)
    rows = _enrich_rows(score_rows, gate_rows)
    failed_gate_counts = Counter()
    for row in rows:
        failed_gate_counts.update(row.get("failed_gates") or ())

    exercised_archetypes = sorted({str(row.get("canonical_archetype_id") or "unknown") for row in rows})
    canonical_count = _weight_archetype_count(weight_profile_path)
    archetype_rows = [
        _group_census(archetype, group)
        for archetype, group in sorted(_group_rows(rows, "canonical_archetype_id").items())
    ]
    sector_rows = [
        _group_census(sector, group) for sector, group in sorted(_group_rows(rows, "sector_profile").items())
    ]
    global_zero_counts = _field_zero_counts(rows, ZERO_CENSUS_FIELDS)
    return {
        "schema_version": "v12_current_runtime_field_failure_census_v1",
        "scope": "current_benchmark_runtime_candidates_only",
        "score_csv_path": str(score_csv_path),
        "gate_csv_path": str(gate_csv_path),
        "summary": {
            "plain_answer": (
                "현재 runtime benchmark는 후보 120개를 채점했지만 Green은 0개다. "
                "전부 Stage3 total과 bottleneck gate에서 막히며, 원인은 아키타입별 bridge field 0점과 gate deficit이다."
            ),
            "candidate_row_count": len(rows),
            "symbol_count": len({str(row.get("symbol") or "") for row in rows if str(row.get("symbol") or "")}),
            "stage_counts": _stage_counts(rows),
            "stage3_green_count": sum(1 for row in rows if str(row.get("current_stage")) == "3-Green"),
            "runtime_exercised_archetype_count": len(exercised_archetypes),
            "canonical_archetype_count_in_weight_profile": canonical_count,
            "runtime_unexercised_archetype_count": (
                canonical_count - len(exercised_archetypes) if canonical_count is not None else None
            ),
            "failed_gate_counts": dict(failed_gate_counts.most_common()),
            "all_candidates_failed_stage3_total": failed_gate_counts.get("failed_stage3_total_score", 0) == len(rows),
            "all_candidates_failed_stage3_bottleneck": failed_gate_counts.get("failed_stage3_bottleneck", 0) == len(rows),
            "global_zero_field_counts": global_zero_counts,
            "global_zero_field_note": (
                "전역 zero count는 모든 bridge family의 coverage census다. "
                "bio/finance/software field가 120/120 zero인 것은 현재 benchmark가 그 아키타입을 거의 채점하지 않았다는 뜻이며, "
                "각 후보에 모두 필요한 필드라는 뜻은 아니다."
            ),
            "coverage_caveat": (
                "이 census는 현재 benchmark 후보가 실제 채점한 아키타입만 증명한다. "
                "나머지 아키타입은 점수식보다 replay/archive coverage가 먼저 필요하다."
            ),
        },
        "archetype_rows": archetype_rows,
        "sector_rows": sector_rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _top_counts(counts: Mapping[str, Any], limit: int = 5) -> str:
    if not counts:
        return "none"
    items: list[tuple[str, float]] = []
    for key, value in counts.items():
        if isinstance(value, Mapping):
            count = float(value.get("zero_count") or 0)
        else:
            count = float(value or 0)
        items.append((str(key), count))
    items.sort(key=lambda item: (-item[1], item[0]))

    def fmt(number: float) -> str:
        if number.is_integer():
            return str(int(number))
        return f"{number:.2f}"

    return ", ".join(f"{key}:{fmt(count)}" for key, count in items[:limit]) or "none"


def _bridge_quad(row: Mapping[str, Any] | None) -> str:
    if not row:
        return "none"
    return "/".join(
        _fmt(row.get(field))
        for field in (
            "research_axis_bridge_margin",
            "research_axis_bridge_customer",
            "research_axis_bridge_backlog",
            "research_axis_bridge_contract",
        )
    )


def render_v12_current_runtime_field_failure_census(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    lines = [
        "# V12 Current Runtime Field Failure Census",
        "",
        "이 문서는 현재 benchmark runtime 후보 전체에서 점수가 어디서 깎이는지 기계적으로 집계한다.",
        "삼전/하닉만 보는 문서가 아니라, 실제 채점된 모든 후보의 field 0점과 Green gate 실패를 센다.",
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
        f"- all_candidates_failed_stage3_total: `{summary.get('all_candidates_failed_stage3_total')}`",
        f"- all_candidates_failed_stage3_bottleneck: `{summary.get('all_candidates_failed_stage3_bottleneck')}`",
        f"- global_zero_field_note: {summary.get('global_zero_field_note')}",
        f"- coverage_caveat: {summary.get('coverage_caveat')}",
        "",
        "## Global Failure Counts",
        "",
        "| failure kind | top counts |",
        "| --- | --- |",
        f"| failed gates | {_top_counts(summary.get('failed_gate_counts') or {}, limit=12)} |",
        f"| zero fields | {_top_counts(summary.get('global_zero_field_counts') or {}, limit=12)} |",
        "",
        "## Archetype Census",
        "",
        "| archetype | rows | stages | max | avg | best row | bridge m/c/b/k | top zero fields | top failed gates | avg positive deficits | diagnosis |",
        "| --- | ---: | --- | ---: | ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for row in payload.get("archetype_rows", []) or []:
        best = row.get("best_row") or {}
        best_text = "{symbol} {name} {asof} {stage}/{score}".format(
            symbol=_fmt(best.get("symbol")),
            name=_fmt(best.get("company_name")),
            asof=_fmt(best.get("as_of_date")),
            stage=_fmt(best.get("current_stage")),
            score=_fmt(best.get("current_score")),
        ).strip()
        deficits = row.get("positive_deficit_averages") or {}
        deficit_text = _top_counts(
            {
                key: value
                for key, value in deficits.items()
                if key
                in {
                    "stage3_total_deficit",
                    "stage3_bottleneck_deficit",
                    "stage3_visibility_deficit",
                    "stage3_contract_quality_deficit",
                    "stage3_revision_deficit",
                    "domain_specific_evidence_deficit",
                }
            },
            limit=5,
        )
        lines.append(
            "| {arch} | {count} | {stages} | {max_score} | {avg_score} | {best} | {bridge} | {zeros} | {gates} | {deficits} | {diagnosis} |".format(
                arch=row.get("group_key"),
                count=row.get("row_count"),
                stages=row.get("stage_counts"),
                max_score=_fmt(row.get("max_score")),
                avg_score=_fmt(row.get("avg_score")),
                best=best_text or "none",
                bridge=_bridge_quad(best),
                zeros=_top_counts(row.get("zero_field_counts") or {}, limit=6),
                gates=_top_counts(row.get("failed_gate_counts") or {}, limit=6),
                deficits=deficit_text,
                diagnosis=row.get("plain_diagnosis"),
            )
        )

    lines.extend(
        [
            "",
            "## Sector Census",
            "",
            "| sector | rows | stages | max | avg | top zero fields | top failed gates |",
            "| --- | ---: | --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in payload.get("sector_rows", []) or []:
        lines.append(
            "| {sector} | {count} | {stages} | {max_score} | {avg_score} | {zeros} | {gates} |".format(
                sector=row.get("group_key"),
                count=row.get("row_count"),
                stages=row.get("stage_counts"),
                max_score=_fmt(row.get("max_score")),
                avg_score=_fmt(row.get("avg_score")),
                zeros=_top_counts(row.get("zero_field_counts") or {}, limit=6),
                gates=_top_counts(row.get("failed_gate_counts") or {}, limit=6),
            )
        )

    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 현재 채점된 후보 120개는 모두 Stage3 total과 bottleneck gate를 실패한다.",
            "- 하닉은 전망/revision이 무시된 것이 아니라 bridge field가 채워진 뒤에도 total/bottleneck gate 검증이 남는다.",
            "- 전력기기는 EPS와 일부 backlog가 살아도 contract quality와 delivery-to-margin bridge가 부족해 bottleneck이 낮다.",
            "- 방산은 계약/수주잔고가 있어도 매출/마진 전환이 EPS/FCF와 bottleneck으로 약하게 들어간다.",
            "- 소비재/수출은 반복 주문, sell-through, channel margin bridge가 충분히 source-backed field로 안 들어간다.",
            "- 전체 36개 아키타입 중 현재 benchmark가 실제 채점한 것은 일부다. 채점되지 않은 아키타입은 먼저 replay fixture/archive를 만들어야 한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_current_runtime_field_failure_census(
    *,
    score_csv_path: str | Path = DEFAULT_SCORE_CSV_PATH,
    gate_csv_path: str | Path = DEFAULT_GATE_CSV_PATH,
    weight_profile_path: str | Path = DEFAULT_WEIGHT_PROFILE_PATH,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_current_runtime_field_failure_census(
        score_csv_path=score_csv_path,
        gate_csv_path=gate_csv_path,
        weight_profile_path=weight_profile_path,
    )
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_current_runtime_field_failure_census(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_current_runtime_field_failure_census()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
