"""Gold 조사와 production 조사를 격리한 뒤 material fact recall을 비교한다."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl


GOLD_FACT_FILE = "gold_material_facts.jsonl"
GOLD_SOURCE_FILE = "gold_source_map.jsonl"
GOLD_COVERAGE_FILE = "gold_question_coverage.json"
PRODUCTION_FACT_FILE = "production_material_facts.jsonl"
PRODUCTION_INPUT_FILE = "production_input_manifest.jsonl"
PRODUCTION_LANE_FILE = "production_lane_manifest.json"

REQUIRED_GOLD_ROUTES = {
    "official_filing",
    "issuer_ir_earnings",
    "issuer_newsroom",
    "customer_official",
    "trusted_independent",
    "financial_revision",
    "counter_supersession",
}
SOURCE_TIER_RANK = {
    "REGULATORY_OFFICIAL": 1,
    "ISSUER_OFFICIAL": 1,
    "CUSTOMER_OFFICIAL": 1,
    "TRUSTED_INDEPENDENT": 2,
    "FINANCIAL_REVISION": 2,
    "GENERAL_WEB": 3,
    "DISCOVERY_ONLY": 4,
}


@dataclass(frozen=True)
class MaterialFactComparison:
    question_family_id: str
    gold_fact_id: str
    production_fact_id: str | None
    semantic_match: bool
    source_quality_match: bool
    currentness_match: bool
    mechanism_scope_match: bool
    materiality: str
    miss_reason: str | None
    fact_role: str
    target_id: str

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class BlindResearchBenchmarkResult:
    status: str
    comparisons: tuple[MaterialFactComparison, ...]
    audit: Mapping[str, Any]


class BlindResearchQualityBenchmark:
    """Production 결과 생성이 끝난 뒤에만 gold leaf를 열어 비교한다."""

    def compare(
        self,
        *,
        gold_root: str | Path,
        production_root: str | Path,
    ) -> BlindResearchBenchmarkResult:
        gold = Path(gold_root).resolve()
        production = Path(production_root).resolve()
        _require_isolated_roots(gold, production)
        gold_facts = _read_jsonl(gold / GOLD_FACT_FILE)
        gold_sources = _read_jsonl(gold / GOLD_SOURCE_FILE)
        coverage = _read_json(gold / GOLD_COVERAGE_FILE)
        production_facts = _read_jsonl(production / PRODUCTION_FACT_FILE)
        production_inputs = _read_jsonl(production / PRODUCTION_INPUT_FILE)
        production_lane = _read_json(production / PRODUCTION_LANE_FILE)
        _validate_gold_lane(gold_facts, gold_sources, coverage)
        _validate_production_lane(production_facts, production_lane)

        leakage = _audit_gold_leakage(
            gold_root=gold,
            gold_facts=gold_facts,
            gold_sources=gold_sources,
            production_inputs=production_inputs,
            production_lane=production_lane,
        )
        comparisons = _compare_material_facts(gold_facts, production_facts)
        qualified = {
            row.gold_fact_id
            for row in comparisons
            if row.semantic_match
            and row.source_quality_match
            and row.currentness_match
            and row.mechanism_scope_match
        }
        critical_misses = sum(
            row.materiality == "CRITICAL" and row.gold_fact_id not in qualified
            for row in comparisons
        )
        counter_misses = sum(
            row.fact_role == "COUNTER" and row.gold_fact_id not in qualified
            for row in comparisons
        )
        supersession_misses = sum(
            row.fact_role == "SUPERSESSION"
            and row.gold_fact_id not in qualified
            for row in comparisons
        )
        noncritical = [
            row for row in comparisons if row.materiality == "NONCRITICAL"
        ]
        noncritical_recall = (
            sum(row.gold_fact_id in qualified for row in noncritical)
            / len(noncritical)
            if noncritical
            else 1.0
        )
        routes = {
            str(row.get("research_route") or "") for row in gold_sources
        }
        missing_routes = sorted(REQUIRED_GOLD_ROUTES - routes)
        critical_counts = {
            "critical_material_fact_miss_count": critical_misses,
            "material_counter_fact_miss_count": counter_misses,
            "material_supersession_fact_miss_count": supersession_misses,
            "gold_source_injected_into_production_count": leakage[
                "gold_source_injected_into_production_count"
            ],
            "gold_query_leaked_into_production_count": leakage[
                "gold_query_leaked_into_production_count"
            ],
            "gold_fact_leaked_into_production_prompt_count": leakage[
                "gold_fact_leaked_into_production_prompt_count"
            ],
            "gold_route_missing_count": len(missing_routes),
            "noncritical_recall_below_90_count": int(
                noncritical_recall < 0.9
            ),
        }
        critical_sum = sum(critical_counts.values())
        status = (
            "BLIND_RESEARCH_QUALITY_PASS"
            if critical_sum == 0
            else "BLIND_RESEARCH_QUALITY_FAIL"
        )
        audit = {
            "schema_version": "e2r_research_quality_gold_audit_v1",
            "status": status,
            "benchmark_mode": str(
                coverage.get("benchmark_mode")
                or "UNSPECIFIED_BLIND_BENCHMARK"
            ),
            "gold_lane_role": "PRIVATE_POST_RUN_EVALUATION",
            "production_lane_role": "CANONICAL_BLIND_RUN",
            "gold_fact_count": len(gold_facts),
            "production_fact_count": len(production_facts),
            "qualified_material_fact_match_count": len(qualified),
            "noncritical_fact_count": len(noncritical),
            "noncritical_fact_recall": round(noncritical_recall, 6),
            "required_gold_routes": sorted(REQUIRED_GOLD_ROUTES),
            "observed_gold_routes": sorted(routes),
            "missing_gold_routes": missing_routes,
            "lane_isolation": {
                "gold_root_hash": stable_hash(str(gold)),
                "production_root_hash": stable_hash(str(production)),
                "roots_are_disjoint": True,
                "gold_visibility_during_production": False,
                "comparison_timing": "POST_RUN_ONLY",
            },
            "leakage_audit": leakage,
            "comparisons": [row.to_dict() for row in comparisons],
            "critical_counts": critical_counts,
            "critical_count_sum": critical_sum,
        }
        return BlindResearchBenchmarkResult(
            status=status,
            comparisons=comparisons,
            audit=audit,
        )

    def write(
        self,
        *,
        result: BlindResearchBenchmarkResult,
        comparison_path: str | Path,
        audit_path: str | Path,
    ) -> None:
        write_jsonl(
            Path(comparison_path),
            (row.to_dict() for row in result.comparisons),
        )
        write_json(Path(audit_path), result.audit)


def _compare_material_facts(
    gold_facts: Sequence[Mapping[str, Any]],
    production_facts: Sequence[Mapping[str, Any]],
) -> tuple[MaterialFactComparison, ...]:
    production_by_key: dict[str, list[Mapping[str, Any]]] = {}
    for row in production_facts:
        production_by_key.setdefault(_semantic_fact_key(row), []).append(row)
    used_production_ids: set[str] = set()
    comparisons = []
    for gold in gold_facts:
        candidates = [
            row
            for row in production_by_key.get(_semantic_fact_key(gold), ())
            if str(row["fact_id"]) not in used_production_ids
        ]
        production = min(candidates, key=_candidate_rank) if candidates else None
        if production is not None:
            used_production_ids.add(str(production["fact_id"]))
        semantic_match = production is not None
        source_match = bool(
            production is not None
            and _source_rank(str(production["source_tier"]))
            <= _source_rank(str(gold["source_tier"]))
        )
        currentness_match = bool(
            production is not None
            and production.get("temporal_status") == "CURRENT"
            and production.get("as_of_date") == gold.get("as_of_date")
        )
        mechanism_match = bool(
            production is not None
            and production.get("mechanism_scope_id")
            == gold.get("mechanism_scope_id")
        )
        comparisons.append(
            MaterialFactComparison(
                question_family_id=str(gold["question_family_id"]),
                gold_fact_id=str(gold["fact_id"]),
                production_fact_id=(
                    str(production["fact_id"])
                    if production is not None
                    else None
                ),
                semantic_match=semantic_match,
                source_quality_match=source_match,
                currentness_match=currentness_match,
                mechanism_scope_match=mechanism_match,
                materiality=str(gold["materiality"]),
                miss_reason=_miss_reason(
                    semantic=semantic_match,
                    source=source_match,
                    current=currentness_match,
                    mechanism=mechanism_match,
                ),
                fact_role=str(gold["fact_role"]),
                target_id=str(gold["target_id"]),
            )
        )
    return tuple(comparisons)


def _semantic_fact_key(row: Mapping[str, Any]) -> str:
    return stable_hash(
        {
            "target_id": str(row.get("target_id") or "").casefold(),
            "question_family_id": str(
                row.get("question_family_id") or ""
            ).casefold(),
            "subject_id": str(row.get("subject_id") or "").casefold(),
            "predicate_family": str(
                row.get("predicate_family") or ""
            ).casefold(),
            "normalized_object": str(
                row.get("normalized_object") or ""
            ).casefold(),
            "period": str(row.get("period") or "").casefold(),
        }
    )


def _candidate_rank(row: Mapping[str, Any]) -> tuple[int, int, str]:
    return (
        int(row.get("temporal_status") != "CURRENT"),
        _source_rank(str(row.get("source_tier") or "")),
        str(row.get("fact_id") or ""),
    )


def _source_rank(source_tier: str) -> int:
    if source_tier not in SOURCE_TIER_RANK:
        raise ValueError(f"unknown material fact source tier: {source_tier}")
    return SOURCE_TIER_RANK[source_tier]


def _miss_reason(
    *, semantic: bool, source: bool, current: bool, mechanism: bool
) -> str | None:
    if not semantic:
        return "MATERIAL_SEMANTIC_FACT_NOT_FOUND"
    if not mechanism:
        return "WRONG_BUSINESS_MECHANISM"
    if not current:
        return "STALE_OR_WRONG_AS_OF_DATE"
    if not source:
        return "SOURCE_QUALITY_BELOW_GOLD"
    return None


def _audit_gold_leakage(
    *,
    gold_root: Path,
    gold_facts: Sequence[Mapping[str, Any]],
    gold_sources: Sequence[Mapping[str, Any]],
    production_inputs: Sequence[Mapping[str, Any]],
    production_lane: Mapping[str, Any],
) -> Mapping[str, Any]:
    gold_urls = {
        str(row.get("source_url") or "")
        for row in gold_sources
        if row.get("source_url")
    }
    gold_queries = {
        str(row.get("research_query") or "").strip().casefold()
        for row in gold_sources
        if row.get("research_query")
    }
    gold_fact_ids = {str(row["fact_id"]) for row in gold_facts}
    source_injections = []
    query_leaks = []
    fact_leaks = []
    for row in production_inputs:
        input_type = str(row.get("input_type") or "").upper()
        value = str(row.get("value") or "")
        origin = str(row.get("origin") or "").upper()
        path_value = str(row.get("path") or "")
        path_in_gold = bool(
            path_value
            and _is_relative_to(Path(path_value).resolve(), gold_root)
        )
        if (
            path_in_gold
            or origin.startswith("GOLD")
            or (input_type == "SEED_URL" and value in gold_urls)
        ):
            source_injections.append(str(row.get("input_id") or ""))
        if input_type == "QUERY" and value.strip().casefold() in gold_queries:
            query_leaks.append(str(row.get("input_id") or ""))
        if input_type == "PROMPT_CONTEXT" and any(
            fact_id in value for fact_id in gold_fact_ids
        ):
            fact_leaks.append(str(row.get("input_id") or ""))
    if production_lane.get("gold_visibility") is not False:
        fact_leaks.append("PRODUCTION_LANE_GOLD_VISIBILITY_NOT_FALSE")
    return {
        "gold_source_injected_into_production_count": len(source_injections),
        "gold_query_leaked_into_production_count": len(query_leaks),
        "gold_fact_leaked_into_production_prompt_count": len(fact_leaks),
        "source_injection_input_ids": source_injections,
        "query_leak_input_ids": query_leaks,
        "fact_leak_input_ids": fact_leaks,
    }


def _validate_gold_lane(
    facts: Sequence[Mapping[str, Any]],
    sources: Sequence[Mapping[str, Any]],
    coverage: Mapping[str, Any],
) -> None:
    if not facts or not sources:
        raise ValueError("gold lane requires material facts and source map")
    _require_unique(facts, "fact_id")
    _require_unique(sources, "source_id")
    source_ids = {str(row["source_id"]) for row in sources}
    required = {
        "fact_id",
        "target_id",
        "question_family_id",
        "subject_id",
        "predicate_family",
        "normalized_object",
        "period",
        "mechanism_scope_id",
        "source_id",
        "source_tier",
        "temporal_status",
        "as_of_date",
        "materiality",
        "fact_role",
    }
    for row in facts:
        missing = required - set(row)
        if missing:
            raise ValueError(f"gold material fact fields missing: {sorted(missing)}")
        if str(row["source_id"]) not in source_ids:
            raise ValueError("gold fact source lineage is missing")
        _source_rank(str(row["source_tier"]))
        if row["materiality"] not in {"CRITICAL", "NONCRITICAL"}:
            raise ValueError("unknown materiality")
        if row["fact_role"] not in {"SUPPORT", "COUNTER", "SUPERSESSION"}:
            raise ValueError("unknown material fact role")
    questions = coverage.get("questions") or ()
    if not questions:
        raise ValueError("gold question coverage is empty")
    _require_unique(questions, "question_family_id")


def _validate_production_lane(
    facts: Sequence[Mapping[str, Any]], lane: Mapping[str, Any]
) -> None:
    if lane.get("lane_role") != "PRODUCTION" or lane.get("gold_visibility") is not False:
        raise ValueError("production lane is not contract-blind")
    _require_unique(facts, "fact_id")
    for row in facts:
        _source_rank(str(row.get("source_tier") or ""))
        if row.get("discovery_origin") not in {
            "CANONICAL_PLANNER",
            "CANONICAL_SOURCE_TASK",
        }:
            raise ValueError("production fact lacks independent discovery lineage")


def _require_isolated_roots(gold: Path, production: Path) -> None:
    if gold == production or _is_relative_to(gold, production) or _is_relative_to(
        production, gold
    ):
        raise ValueError("gold and production roots must be disjoint")


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _require_unique(rows: Sequence[Mapping[str, Any]], key: str) -> None:
    values = [str(row.get(key) or "") for row in rows]
    if any(not value for value in values) or len(values) != len(set(values)):
        raise ValueError(f"{key} must be present and unique")


def _read_jsonl(path: Path) -> list[Mapping[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _read_json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


__all__ = [
    "BlindResearchBenchmarkResult",
    "BlindResearchQualityBenchmark",
    "MaterialFactComparison",
]
