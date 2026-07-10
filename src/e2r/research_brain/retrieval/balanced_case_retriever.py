"""Balanced semantic retrieval for recipes, cases, guards, and source outcomes."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.intelligence_schema import (
    ArchetypeRetrievalHit,
    BalancedMemoryRole,
    BalancedRetrievalItem,
    BalancedRetrievalRequest,
    BalancedRetrievalResult,
    MemoryNode,
    MemoryNodeType,
    SemanticMemoryIndexEntry,
)
from e2r.research_brain.retrieval.semantic_memory_index import (
    SemanticMemoryIndex,
    semantic_concepts,
)


BALANCED_RETRIEVAL_SCHEMA_VERSION = "e2r_balanced_semantic_retrieval_v1"
BLIND_RETRIEVAL_BENCHMARK_SCHEMA_VERSION = "e2r_blind_retrieval_benchmark_v1"
DEFAULT_BLIND_RETRIEVAL_BENCHMARK_PATH = (
    Path(__file__).resolve().parents[4]
    / "configs"
    / "e2r_semantic_retrieval_blind_benchmark_v1.jsonl"
)
_REQUIRED_BALANCED_ROLES = (
    BalancedMemoryRole.DIRECT_RECIPE.value,
    BalancedMemoryRole.POSITIVE.value,
    BalancedMemoryRole.COUNTEREXAMPLE_GUARD.value,
    BalancedMemoryRole.SOURCE_SUCCESS.value,
    BalancedMemoryRole.SOURCE_FAILURE.value,
    BalancedMemoryRole.SEMANTIC_GUARD.value,
)
_FORBIDDEN_RESULT_TOKENS = (
    "mfe_",
    "mae_",
    "future_return",
    "future_outcome",
    "outcome_label",
    "expected_stage",
    "price_metrics",
    "current_profile_verdict",
)


@dataclass(frozen=True)
class BlindRetrievalBenchmarkCase:
    benchmark_id: str
    current_evidence: str
    as_of_date: str
    expected_archetype_id: str
    expected_primitive_id: str
    archetype_retrieval_expected: bool = True
    required_recipe_expected: bool = True
    exclusion_reason: str | None = None
    evaluator_only: bool = True

    def __post_init__(self) -> None:
        required = (
            self.benchmark_id,
            self.current_evidence,
            self.as_of_date,
            self.expected_archetype_id,
            self.expected_primitive_id,
        )
        if not all(item.strip() for item in required):
            raise ValueError("blind retrieval benchmark fields must be non-empty")
        if not self.evaluator_only:
            raise ValueError("blind retrieval expected labels must remain evaluator-only")
        if self.expected_archetype_id in self.current_evidence:
            raise ValueError("raw benchmark evidence contains the expected archetype id")
        if self.expected_primitive_id in self.current_evidence:
            raise ValueError("raw benchmark evidence contains the expected primitive id")
        if (
            not self.archetype_retrieval_expected
            or not self.required_recipe_expected
        ) and not str(self.exclusion_reason or "").strip():
            raise ValueError("benchmark exclusions require an exact reason")

    def to_request(self) -> BalancedRetrievalRequest:
        return BalancedRetrievalRequest(
            request_id=self.benchmark_id,
            current_evidence_text=self.current_evidence,
            as_of_date=self.as_of_date,
            top_k_archetypes=3,
            max_recipe_hits=3,
        )


@dataclass(frozen=True)
class BalancedRetrievalBenchmarkAudit:
    rows: tuple[Mapping[str, Any], ...]
    manifest: Mapping[str, Any]


def retrieve_balanced_memory(
    index: SemanticMemoryIndex,
    request: BalancedRetrievalRequest,
) -> BalancedRetrievalResult:
    return _retrieve_from_entries(index, request, index.entries)


def _retrieve_from_entries(
    index: SemanticMemoryIndex,
    request: BalancedRetrievalRequest,
    entries: Sequence[SemanticMemoryIndexEntry],
) -> BalancedRetrievalResult:
    node_by_id = {node.node_id: node for node in index.graph.nodes}
    # Node identity, not sequence or occurrence count, is authoritative. This is
    # what makes reversed input and duplicated popularity probes invariant.
    unique_entries = {
        entry.node_id: entry
        for entry in entries
        if entry.node_id in node_by_id
    }
    eligible = tuple(
        entry
        for entry in unique_entries.values()
        if _entry_is_eligible(entry, node_by_id[entry.node_id], request)
    )
    query_concepts = set(semantic_concepts(request.current_evidence_text))
    for primitive_id in request.required_primitive_ids:
        query_concepts.update(semantic_concepts(primitive_id))
    if not query_concepts:
        query_concepts.add("unresolved_evidence")

    entries_by_archetype: dict[str, list[SemanticMemoryIndexEntry]] = defaultdict(list)
    for entry in eligible:
        if entry.archetype_id:
            entries_by_archetype[entry.archetype_id].append(entry)
    if request.candidate_archetype_ids:
        allowed = set(request.candidate_archetype_ids)
        entries_by_archetype = {
            archetype_id: values
            for archetype_id, values in entries_by_archetype.items()
            if archetype_id in allowed
        }
    if not entries_by_archetype:
        raise ValueError("balanced retrieval has no eligible archetype memory")

    idf = _concept_idf(entries_by_archetype)
    archetype_rows: list[
        tuple[float, str, tuple[str, ...], tuple[str, ...]]
    ] = []
    for archetype_id, archetype_entries in entries_by_archetype.items():
        unique_archetype_concepts = {
            concept
            for entry in archetype_entries
            for concept in entry.concepts
        }
        aggregate_score, aggregate_matches = _semantic_similarity(
            query_concepts,
            unique_archetype_concepts,
            idf,
        )
        node_scores = [
            (
                *_semantic_similarity(query_concepts, set(entry.concepts), idf),
                entry.node_id,
            )
            for entry in archetype_entries
        ]
        node_scores.sort(
            key=lambda row: (-row[0], _stable_tie(request.request_id, row[2]))
        )
        best_node_score = node_scores[0][0] if node_scores else 0.0
        structured_boost = 0.0
        if request.required_primitive_ids and any(
            entry.primitive_id in request.required_primitive_ids
            for entry in archetype_entries
        ):
            structured_boost = 0.2
        score = round(
            min(1.0, best_node_score * 0.75 + aggregate_score * 0.25 + structured_boost),
            8,
        )
        matched = tuple(
            sorted(
                set(aggregate_matches)
                | set(node_scores[0][1] if node_scores else ())
            )
        )
        supporting = tuple(
            row[2]
            for row in node_scores
            if row[0] > 0
        )[:3]
        archetype_rows.append((score, archetype_id, matched, supporting))
    archetype_rows.sort(
        key=lambda row: (-row[0], _stable_tie(request.request_id, row[1]))
    )
    selected_archetypes = archetype_rows[: request.top_k_archetypes]
    archetype_hits = tuple(
        ArchetypeRetrievalHit(
            archetype_id=archetype_id,
            semantic_score=score,
            matched_concepts=matched,
            supporting_node_ids=supporting,
        )
        for score, archetype_id, matched, supporting in selected_archetypes
    )
    selected_archetype_ids = {hit.archetype_id for hit in archetype_hits}
    archetype_score = {
        hit.archetype_id: hit.semantic_score for hit in archetype_hits
    }

    recipe_rows: list[
        tuple[float, SemanticMemoryIndexEntry, tuple[str, ...]]
    ] = []
    for entry in eligible:
        if (
            entry.node_type != MemoryNodeType.RECIPE.value
            or entry.archetype_id not in selected_archetype_ids
        ):
            continue
        score, matched = _semantic_similarity(query_concepts, set(entry.concepts), idf)
        if (
            request.required_primitive_ids
            and entry.primitive_id in request.required_primitive_ids
        ):
            score = min(1.0, score + 0.25)
        score = min(
            1.0,
            score * 0.9 + archetype_score.get(entry.archetype_id or "", 0.0) * 0.1,
        )
        recipe_rows.append((round(score, 8), entry, matched))
    recipe_rows.sort(
        key=lambda row: (
            -row[0],
            _stable_tie(request.request_id, row[1].node_id),
        )
    )
    selected_recipes = recipe_rows[: request.max_recipe_hits]

    items: list[BalancedRetrievalItem] = []
    for recipe_score, recipe_entry, recipe_matches in selected_recipes:
        recipe_id = recipe_entry.recipe_id
        if not recipe_id or not recipe_entry.archetype_id:
            continue
        bundle_entries = {
            entry.role_slot: entry
            for entry in eligible
            if entry.recipe_id == recipe_id and entry.role_slot
        }
        for role in _REQUIRED_BALANCED_ROLES:
            entry = bundle_entries.get(role)
            if entry is None:
                continue
            node = node_by_id[entry.node_id]
            role_score, role_matches = _semantic_similarity(
                query_concepts,
                set(entry.concepts),
                idf,
            )
            combined_score = (
                recipe_score
                if role == BalancedMemoryRole.DIRECT_RECIPE.value
                else recipe_score * 0.8 + role_score * 0.2
            )
            items.append(
                BalancedRetrievalItem(
                    node_id=node.node_id,
                    node_type=node.node_type,
                    role_slot=role,
                    archetype_id=node.archetype_id or recipe_entry.archetype_id,
                    primitive_id=node.primitive_id,
                    recipe_id=node.recipe_id,
                    semantic_score=round(combined_score, 8),
                    matched_concepts=tuple(
                        sorted(set(recipe_matches) | set(role_matches))
                    ),
                    planner_payload=node.planner_payload,
                    available_from_date=node.available_from_date,
                )
            )

    context_rows: list[
        tuple[float, SemanticMemoryIndexEntry, tuple[str, ...]]
    ] = []
    for entry in eligible:
        if (
            entry.node_type != MemoryNodeType.CASE.value
            or entry.archetype_id not in selected_archetype_ids
        ):
            continue
        score, matched = _semantic_similarity(query_concepts, set(entry.concepts), idf)
        if score > 0:
            context_rows.append((score, entry, matched))
    context_rows.sort(
        key=lambda row: (
            -row[0],
            _stable_tie(request.request_id, row[1].node_id),
        )
    )
    seen_context_archetypes: set[str] = set()
    for context_score, entry, matched in context_rows:
        if not entry.archetype_id or entry.archetype_id in seen_context_archetypes:
            continue
        node = node_by_id[entry.node_id]
        items.append(
            BalancedRetrievalItem(
                node_id=node.node_id,
                node_type=node.node_type,
                role_slot=BalancedMemoryRole.CONTEXT_CASE.value,
                archetype_id=entry.archetype_id,
                primitive_id=node.primitive_id,
                recipe_id=node.recipe_id,
                semantic_score=round(context_score, 8),
                matched_concepts=matched,
                planner_payload=node.planner_payload,
                available_from_date=node.available_from_date,
            )
        )
        seen_context_archetypes.add(entry.archetype_id)
        if len(seen_context_archetypes) >= request.top_k_archetypes:
            break

    covered_roles = tuple(
        role for role in _REQUIRED_BALANCED_ROLES if any(item.role_slot == role for item in items)
    )
    missing_roles = tuple(
        role for role in _REQUIRED_BALANCED_ROLES if role not in covered_roles
    )
    direct_recipe_ids = tuple(
        dict.fromkeys(
            item.recipe_id
            for item in items
            if item.role_slot == BalancedMemoryRole.DIRECT_RECIPE.value
            and item.recipe_id
        )
    )
    result_payload = {
        "request_id": request.request_id,
        "archetype_hits": [hit.to_dict() for hit in archetype_hits],
        "items": [item.to_dict() for item in items],
    }
    future_leakage_count = _forbidden_token_count(result_payload)
    return BalancedRetrievalResult(
        request_id=request.request_id,
        archetype_hits=archetype_hits,
        items=tuple(items),
        covered_roles=covered_roles,
        missing_roles=missing_roles,
        direct_recipe_ids=direct_recipe_ids,
        first_n_only=False,
        popularity_weight_used=False,
        future_leakage_count=future_leakage_count,
    )


def load_blind_retrieval_benchmark(
    path: str | Path | None = None,
) -> tuple[BlindRetrievalBenchmarkCase, ...]:
    benchmark_path = Path(path or DEFAULT_BLIND_RETRIEVAL_BENCHMARK_PATH)
    rows: list[BlindRetrievalBenchmarkCase] = []
    seen: set[str] = set()
    with benchmark_path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            raw = json.loads(line)
            if raw.get("schema_version") != BLIND_RETRIEVAL_BENCHMARK_SCHEMA_VERSION:
                raise ValueError(
                    f"unsupported blind retrieval benchmark schema at line {line_number}"
                )
            row = BlindRetrievalBenchmarkCase(
                benchmark_id=str(raw["benchmark_id"]),
                current_evidence=str(raw["current_evidence"]),
                as_of_date=str(raw["as_of_date"]),
                expected_archetype_id=str(raw["expected_archetype_id"]),
                expected_primitive_id=str(raw["expected_primitive_id"]),
                archetype_retrieval_expected=bool(
                    raw.get("archetype_retrieval_expected", True)
                ),
                required_recipe_expected=bool(
                    raw.get("required_recipe_expected", True)
                ),
                exclusion_reason=(
                    str(raw["exclusion_reason"])
                    if raw.get("exclusion_reason")
                    else None
                ),
                evaluator_only=bool(raw.get("evaluator_only", True)),
            )
            if row.benchmark_id in seen:
                raise ValueError(f"duplicate retrieval benchmark id: {row.benchmark_id}")
            seen.add(row.benchmark_id)
            rows.append(row)
    if not rows:
        raise ValueError("blind retrieval benchmark is empty")
    return tuple(rows)


def evaluate_balanced_retrieval(
    index: SemanticMemoryIndex,
    benchmark_cases: Iterable[BlindRetrievalBenchmarkCase],
) -> BalancedRetrievalBenchmarkAudit:
    cases = tuple(benchmark_cases)
    node_by_id = {node.node_id: node for node in index.graph.nodes}
    expected_recipe_by_pair = {
        (node.archetype_id, node.primitive_id): node.recipe_id
        for node in index.graph.nodes
        if node.node_type == MemoryNodeType.RECIPE.value
        and node.archetype_id
        and node.primitive_id
        and node.recipe_id
    }
    entry_counts = Counter(
        entry.archetype_id
        for entry in index.entries
        if entry.planner_visible and entry.archetype_id
    )
    rows: list[Mapping[str, Any]] = []
    for case in cases:
        request = case.to_request()
        result = retrieve_balanced_memory(index, request)
        reversed_result = _retrieve_from_entries(
            index,
            request,
            tuple(reversed(index.entries)),
        )
        decoy_archetype = next(
            (
                archetype_id
                for archetype_id, _ in entry_counts.most_common()
                if archetype_id != case.expected_archetype_id
            ),
            None,
        )
        repeated_decoy = tuple(
            entry
            for entry in index.entries
            if entry.archetype_id == decoy_archetype
        )
        popularity_result = _retrieve_from_entries(
            index,
            request,
            (*index.entries, *repeated_decoy, *repeated_decoy, *repeated_decoy),
        )
        expected_recipe_id = expected_recipe_by_pair.get(
            (case.expected_archetype_id, case.expected_primitive_id)
        )
        recipe_evaluated = bool(
            case.required_recipe_expected and expected_recipe_id
        )
        effective_exclusion_reason = case.exclusion_reason
        if case.required_recipe_expected and not expected_recipe_id:
            effective_exclusion_reason = (
                "EXPECTED_RECIPE_NOT_COMPILED_FOR_PARTIAL_INPUT_SCOPE"
            )
        top_archetypes = tuple(hit.archetype_id for hit in result.archetype_hits)
        top3_hit = (
            case.expected_archetype_id in top_archetypes[:3]
            if case.archetype_retrieval_expected
            else None
        )
        recipe_hit = (
            bool(expected_recipe_id and expected_recipe_id in result.direct_recipe_ids)
            if recipe_evaluated
            else None
        )
        expected_recipe_roles = {
            item.role_slot
            for item in result.items
            if item.recipe_id == expected_recipe_id
        }
        positive_guard_pair = (
            {
                BalancedMemoryRole.POSITIVE.value,
                BalancedMemoryRole.COUNTEREXAMPLE_GUARD.value,
            }
            <= expected_recipe_roles
            if recipe_evaluated
            else None
        )
        normal_signature = (
            top_archetypes,
            result.direct_recipe_ids,
        )
        reversed_signature = (
            tuple(hit.archetype_id for hit in reversed_result.archetype_hits),
            reversed_result.direct_recipe_ids,
        )
        popularity_signature = (
            tuple(hit.archetype_id for hit in popularity_result.archetype_hits),
            popularity_result.direct_recipe_ids,
        )
        result_leakage = _forbidden_token_count(result.to_dict())
        rows.append(
            {
                "schema_version": BALANCED_RETRIEVAL_SCHEMA_VERSION,
                "benchmark_id": case.benchmark_id,
                "expected_archetype_id": case.expected_archetype_id,
                "expected_primitive_id": case.expected_primitive_id,
                "expected_recipe_id": expected_recipe_id,
                "archetype_retrieval_expected": case.archetype_retrieval_expected,
                "required_recipe_expected": recipe_evaluated,
                "benchmark_declared_recipe_expected": case.required_recipe_expected,
                "exclusion_reason": effective_exclusion_reason,
                "top_archetype_ids": list(top_archetypes),
                "direct_recipe_ids": list(result.direct_recipe_ids),
                "top3_archetype_hit": top3_hit,
                "required_recipe_hit": recipe_hit,
                "positive_guard_pair": positive_guard_pair,
                "future_leakage_count": result_leakage,
                "input_order_invariant": normal_signature == reversed_signature,
                "popularity_probe_archetype_id": decoy_archetype,
                "popularity_invariant": normal_signature == popularity_signature,
                "balanced_roles": list(result.covered_roles),
                "missing_roles": list(result.missing_roles),
                "planner_payload_contains_expected_label": any(
                    case.expected_archetype_id
                    in json.dumps(item.planner_payload, ensure_ascii=False)
                    for item in result.items
                ),
                "graph_node_count": len(node_by_id),
            }
        )

    benchmark_count = len(rows)
    archetype_rows = [row for row in rows if row["archetype_retrieval_expected"]]
    recipe_rows = [row for row in rows if row["required_recipe_expected"]]
    top3_rate = _rate(archetype_rows, "top3_archetype_hit")
    recipe_rate = _rate(recipe_rows, "required_recipe_hit")
    pair_rate = _rate(recipe_rows, "positive_guard_pair")
    future_leakage_count = sum(int(row["future_leakage_count"]) for row in rows)
    first_n_only_count = sum(not row["input_order_invariant"] for row in rows)
    popularity_bias_critical_count = sum(
        not row["popularity_invariant"] for row in rows
    )
    critical = {
        "top3_archetype_hit_rate_below_0_95": int(top3_rate < 0.95),
        "required_recipe_hit_rate_below_0_95": int(recipe_rate < 0.95),
        "positive_guard_pair_rate_below_0_90": int(pair_rate < 0.90),
        "future_leakage": future_leakage_count,
        "first_n_only_retrieval": first_n_only_count,
        "popularity_bias_critical": popularity_bias_critical_count,
        "unjustified_benchmark_exclusion": sum(
            (
                not row["archetype_retrieval_expected"]
                or not row["required_recipe_expected"]
            )
            and not row["exclusion_reason"]
            for row in rows
        ),
    }
    manifest = {
        "schema_version": BALANCED_RETRIEVAL_SCHEMA_VERSION,
        "status": (
            "BALANCED_SEMANTIC_RETRIEVAL_PASS"
            if benchmark_count and sum(critical.values()) == 0
            else "BALANCED_SEMANTIC_RETRIEVAL_FAIL"
        ),
        "benchmark_count": benchmark_count,
        "registry_archetype_coverage_count": len(
            {row["expected_archetype_id"] for row in rows}
        ),
        "archetype_benchmark_count": len(archetype_rows),
        "recipe_benchmark_count": len(recipe_rows),
        "explicit_exclusion_count": sum(
            not row["archetype_retrieval_expected"]
            or not row["required_recipe_expected"]
            for row in rows
        ),
        "archetype_exclusion_count": sum(
            not row["archetype_retrieval_expected"] for row in rows
        ),
        "recipe_exclusion_count": sum(
            not row["required_recipe_expected"] for row in rows
        ),
        "top3_archetype_hit_count": sum(
            bool(row["top3_archetype_hit"]) for row in archetype_rows
        ),
        "top3_archetype_hit_rate": top3_rate,
        "required_recipe_hit_count": sum(
            bool(row["required_recipe_hit"]) for row in recipe_rows
        ),
        "required_recipe_hit_rate": recipe_rate,
        "positive_guard_pair_count": sum(
            bool(row["positive_guard_pair"]) for row in recipe_rows
        ),
        "positive_guard_pair_rate": pair_rate,
        "future_leakage_count": future_leakage_count,
        "first_n_only_retrieval_count": first_n_only_count,
        "popularity_bias_critical_count": popularity_bias_critical_count,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": stable_hash(rows),
        "production_runtime_ready": False,
    }
    return BalancedRetrievalBenchmarkAudit(rows=tuple(rows), manifest=manifest)


def write_balanced_retrieval_benchmark(
    audit: BalancedRetrievalBenchmarkAudit,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root) / "retrieval"
    paths = {
        "benchmark_results": root / "blind_retrieval_results.jsonl",
        "acceptance": root / "balanced_retrieval_acceptance.json",
        "benchmark_report": root / "balanced_retrieval_report.md",
    }
    write_jsonl(paths["benchmark_results"], audit.rows)
    write_json(paths["acceptance"], dict(audit.manifest))
    write_text(paths["benchmark_report"], render_balanced_retrieval_report(audit.manifest))
    return paths


def render_balanced_retrieval_report(manifest: Mapping[str, Any]) -> str:
    lines = [
        "# E2R Balanced Semantic Retrieval Acceptance",
        "",
        f"- status: {manifest['status']}",
        f"- benchmark_count: {manifest['benchmark_count']}",
        f"- registry_archetype_coverage_count: {manifest['registry_archetype_coverage_count']}",
        f"- archetype_benchmark_count: {manifest['archetype_benchmark_count']}",
        f"- recipe_benchmark_count: {manifest['recipe_benchmark_count']}",
        f"- top3_archetype_hit_rate: {manifest['top3_archetype_hit_rate']:.4f}",
        f"- required_recipe_hit_rate: {manifest['required_recipe_hit_rate']:.4f}",
        f"- positive_guard_pair_rate: {manifest['positive_guard_pair_rate']:.4f}",
        f"- future_leakage_count: {manifest['future_leakage_count']}",
        f"- first_n_only_retrieval_count: {manifest['first_n_only_retrieval_count']}",
        f"- popularity_bias_critical_count: {manifest['popularity_bias_critical_count']}",
        "",
        "Every selected recipe is returned with positive, counterexample,",
        "source-success, source-failure, and wrong-subject semantic-guard memory.",
    ]
    return "\n".join(lines) + "\n"


def _entry_is_eligible(
    entry: SemanticMemoryIndexEntry,
    node: MemoryNode,
    request: BalancedRetrievalRequest,
) -> bool:
    if not entry.planner_visible or not node.planner_visible:
        return False
    if entry.available_from_date and entry.available_from_date > request.as_of_date:
        return False
    if node.case_id and node.case_id in request.excluded_case_ids:
        return False
    return True


def _concept_idf(
    entries_by_archetype: Mapping[str, Sequence[SemanticMemoryIndexEntry]],
) -> Mapping[str, float]:
    document_frequency: Counter[str] = Counter()
    for entries in entries_by_archetype.values():
        document_frequency.update(
            {
                concept
                for entry in entries
                for concept in entry.concepts
            }
        )
    archetype_count = len(entries_by_archetype)
    return {
        concept: math.log((archetype_count + 1) / (frequency + 1)) + 1.0
        for concept, frequency in document_frequency.items()
    }


def _semantic_similarity(
    query_concepts: set[str],
    target_concepts: set[str],
    idf: Mapping[str, float],
) -> tuple[float, tuple[str, ...]]:
    matched = query_concepts & target_concepts
    if not matched:
        return 0.0, ()
    query_weight = sum(idf.get(concept, 1.0) for concept in query_concepts)
    target_weight = sum(idf.get(concept, 1.0) for concept in target_concepts)
    matched_weight = sum(idf.get(concept, 1.0) for concept in matched)
    recall = matched_weight / query_weight if query_weight else 0.0
    precision = matched_weight / target_weight if target_weight else 0.0
    score = min(1.0, recall * 0.88 + math.sqrt(precision) * 0.12)
    return round(score, 8), tuple(sorted(matched))


def _stable_tie(request_id: str, identity: str) -> str:
    return hashlib.sha256(f"{request_id}\0{identity}".encode("utf-8")).hexdigest()


def _forbidden_token_count(value: Any) -> int:
    serialized = json.dumps(value, ensure_ascii=False, sort_keys=True).lower()
    return sum(serialized.count(token) for token in _FORBIDDEN_RESULT_TOKENS)


def _rate(rows: Sequence[Mapping[str, Any]], key: str) -> float:
    if not rows:
        return 0.0
    return round(sum(bool(row[key]) for row in rows) / len(rows), 6)


__all__ = [
    "BALANCED_RETRIEVAL_SCHEMA_VERSION",
    "BLIND_RETRIEVAL_BENCHMARK_SCHEMA_VERSION",
    "DEFAULT_BLIND_RETRIEVAL_BENCHMARK_PATH",
    "BalancedRetrievalBenchmarkAudit",
    "BlindRetrievalBenchmarkCase",
    "evaluate_balanced_retrieval",
    "load_blind_retrieval_benchmark",
    "render_balanced_retrieval_report",
    "retrieve_balanced_memory",
    "write_balanced_retrieval_benchmark",
]
