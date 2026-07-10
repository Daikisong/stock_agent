"""Canonical semantic memory graph and count-invariant retrieval index."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.intelligence_schema import (
    BalancedMemoryRole,
    EvidenceRecipe,
    EvidenceRecipeRole,
    HistoricalResearchCase,
    HistoricalSourceState,
    HistoricalSourceVerification,
    MemoryEdge,
    MemoryEdgeType,
    MemoryNode,
    MemoryNodeType,
    ResearchMemoryGraph,
    SemanticMemoryIndexEntry,
    stable_intelligence_id,
)


SEMANTIC_MEMORY_GRAPH_SCHEMA_VERSION = "e2r_semantic_memory_graph_v1"
SEMANTIC_MEMORY_INDEX_SCHEMA_VERSION = "e2r_semantic_memory_index_v1"
SEMANTIC_INDEX_STRATEGY = "UNIQUE_SEMANTIC_CONCEPT_IDF_WITHOUT_NODE_POPULARITY"

_WORD_RE = re.compile(r"[a-z0-9가-힣]+", re.IGNORECASE)
_FORBIDDEN_OUTCOME_RE = re.compile(
    r"(?:^|[^a-z0-9])(?:"
    r"mfe(?:[_-]?[0-9]+[a-z]*)?|"
    r"mae(?:[_-]?[0-9]+[a-z]*)?|"
    r"future[_ -]?return|"
    r"future[_ -]?outcome|"
    r"outcome[_ -]?label|"
    r"expected[_ -]?stage|"
    r"price[_ -]?metrics|"
    r"current[_ -]?profile[_ -]?verdict"
    r")(?:$|[^a-z0-9])",
    re.IGNORECASE,
)

_STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "because",
    "by",
    "can",
    "current",
    "did",
    "do",
    "does",
    "for",
    "from",
    "has",
    "have",
    "how",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "latest",
    "material",
    "not",
    "of",
    "on",
    "only",
    "or",
    "rather",
    "reported",
    "stated",
    "than",
    "that",
    "the",
    "their",
    "this",
    "through",
    "to",
    "under",
    "was",
    "were",
    "what",
    "when",
    "whether",
    "which",
    "while",
    "with",
    "without",
    "year",
}

# Global financial/research concepts. These are semantic aliases, not queries and
# are deliberately not keyed by archetype, company, sector, or missing slot.
_PHRASE_CONCEPTS = {
    "annual recurring revenue": "arr",
    "free cash flow": "fcf",
    "net revenue retention": "nrr",
    "net retention": "nrr",
    "remaining performance obligation": "rpo",
    "deferred revenue": "deferred_revenue",
    "operating cash flow": "operating_cash_flow",
    "operating margin": "operating_margin",
    "raw material": "input_cost",
    "input cost": "input_cost",
    "fully utilized": "capacity_constraint",
    "sold out": "capacity_booked",
    "fully booked": "capacity_booked",
    "mass production": "commercial_production",
    "repeat order": "repeat_order",
    "follow on order": "repeat_order",
    "clinical hold": "safety_signal",
    "serious adverse event": "safety_signal",
    "regulatory approval": "regulatory_status",
    "cash runway": "cash_runway",
    "price increase": "pricing_power",
    "price hike": "pricing_power",
    "product mix": "product_mix",
    "working capital": "working_capital",
}

_TOKEN_CONCEPTS = {
    "allocated": "allocation",
    "allocates": "allocation",
    "allocation": "allocation",
    "approved": "approval",
    "approval": "approval",
    "booked": "capacity_booked",
    "booking": "capacity_booked",
    "canceled": "cancelled",
    "cancellation": "cancelled",
    "customer": "customer",
    "customers": "customer",
    "feedstock": "feedstock",
    "inventories": "inventory",
    "margins": "margin",
    "orders": "order",
    "preordered": "preorder",
    "prices": "price",
    "qualified": "qualification",
    "qualifying": "qualification",
    "renewals": "renewal",
    "retained": "retention",
    "shipments": "shipment",
    "subscriptions": "subscription",
    "utilisation": "utilization",
}

_POSITIVE_CLASSIFICATIONS = frozenset({"positive"})
_COUNTER_CLASSIFICATIONS = frozenset(
    {
        "counterexample",
        "guard",
        "wrong_subject_guard",
        "future_date_guard",
        "url_only_guard",
        "source_proxy_guard",
        "pending_guard",
    }
)
_POSITIVE_CASE_ROLES = frozenset(
    {"structural_success", "customer_quality", "spread_cycle"}
)
_COUNTER_CASE_ROLES = frozenset({"event_risk_guard", "retention_guard"})


@dataclass(frozen=True)
class SemanticMemoryIndex:
    graph: ResearchMemoryGraph
    entries: tuple[SemanticMemoryIndexEntry, ...]
    strategy: str = SEMANTIC_INDEX_STRATEGY
    schema_version: str = SEMANTIC_MEMORY_INDEX_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.strategy != SEMANTIC_INDEX_STRATEGY:
            raise ValueError("semantic memory index strategy must remain count-invariant")
        node_ids = {node.node_id for node in self.graph.nodes}
        entry_ids = [entry.node_id for entry in self.entries]
        if len(entry_ids) != len(set(entry_ids)):
            raise ValueError("semantic memory index contains duplicate node entries")
        if set(entry_ids) != node_ids:
            raise ValueError("semantic memory index must contain every graph node exactly once")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "strategy": self.strategy,
            "graph_id": self.graph.graph_id,
            "entry_count": len(self.entries),
            "entries": [entry.to_dict() for entry in self.entries],
        }


@dataclass(frozen=True)
class SemanticMemoryCompilationResult:
    graph: ResearchMemoryGraph
    index: SemanticMemoryIndex
    manifest: Mapping[str, Any]


def semantic_concepts(value: str) -> tuple[str, ...]:
    """Return general semantic concepts without company/archetype lookup tables."""

    normalized = re.sub(r"[_/\-]+", " ", str(value or "").lower())
    concepts: set[str] = set()
    for phrase, concept in _PHRASE_CONCEPTS.items():
        if phrase in normalized:
            concepts.add(concept)
    for token in _WORD_RE.findall(normalized):
        if token in _STOP_WORDS or len(token) < 2:
            continue
        concepts.add(_TOKEN_CONCEPTS.get(token, token))
    return tuple(sorted(concepts))


def compile_semantic_memory_graph(
    cases: Iterable[HistoricalResearchCase],
    recipes: Iterable[EvidenceRecipe],
    *,
    source_verifications: Iterable[HistoricalSourceVerification] = (),
) -> SemanticMemoryCompilationResult:
    ordered_cases = tuple(sorted(cases, key=lambda item: item.case_id))
    ordered_recipes = tuple(sorted(recipes, key=lambda item: item.recipe_id))
    ordered_verifications = tuple(
        sorted(source_verifications, key=lambda item: item.verification_id)
    )
    case_by_id = {case.case_id: case for case in ordered_cases}
    contracts = load_evidence_contracts_v2(require_all_archetypes=True)

    nodes: dict[str, MemoryNode] = {}
    edges: dict[str, MemoryEdge] = {}
    archetype_nodes: dict[str, str] = {}
    primitive_nodes: dict[tuple[str, str], str] = {}
    case_nodes: dict[str, str] = {}
    source_nodes: dict[str, str] = {}
    recipe_nodes: dict[str, str] = {}
    source_by_case: dict[str, list[HistoricalSourceVerification]] = defaultdict(list)
    verification_by_id = {
        verification.verification_id: verification
        for verification in ordered_verifications
    }
    for verification in ordered_verifications:
        source_by_case[verification.case_id].append(verification)

    for archetype_id, contract in sorted(contracts.items()):
        planner_visible = not _contains_forbidden_outcome(archetype_id)
        archetype_node = _node(
            node_type=MemoryNodeType.ARCHETYPE,
            identity={"archetype_id": archetype_id},
            label=_humanize(archetype_id),
            search_segments=(
                _humanize(archetype_id),
                *( _humanize(item) for item in contract.required_primitives ),
                *( _humanize(item) for item in contract.primitive_aliases ),
            ),
            archetype_id=archetype_id,
            planner_payload={
                "kind": "archetype_semantic_contract",
                "required_primitive_concepts": [
                    _humanize(item) for item in contract.required_primitives
                ],
            },
            planner_visible=planner_visible,
        )
        _add_node(nodes, archetype_node)
        archetype_nodes[archetype_id] = archetype_node.node_id

        for primitive_id in contract.required_primitives:
            role = (
                "GUARD"
                if primitive_id in contract.guard_modes
                else "POSITIVE"
            )
            aliases = tuple(contract.primitive_aliases.get(primitive_id, ()))
            primitive_node = _node(
                node_type=MemoryNodeType.PRIMITIVE,
                identity={"archetype_id": archetype_id, "primitive_id": primitive_id},
                label=_humanize(primitive_id),
                search_segments=(_humanize(primitive_id), *aliases),
                archetype_id=archetype_id,
                primitive_id=primitive_id,
                planner_payload={
                    "kind": "required_primitive",
                    "semantic_role": role,
                    "aliases": list(_safe_segments(aliases)),
                },
                planner_visible=planner_visible,
            )
            _add_node(nodes, primitive_node)
            primitive_nodes[(archetype_id, primitive_id)] = primitive_node.node_id
            _add_edge(
                edges,
                MemoryEdgeType.REQUIRES,
                archetype_node.node_id,
                primitive_node.node_id,
                "The canonical Evidence Contract requires this exact primitive pair.",
                planner_visible=planner_visible,
            )

    for case in ordered_cases:
        planner_visible = not _contains_forbidden_outcome(
            " ".join((case.case_id, case.canonical_archetype_id))
        )
        role = _case_semantic_role(case)
        reference_summaries = tuple(
            reference.summary or "" for reference in case.evidence_references
        )
        case_node = _node(
            node_type=MemoryNodeType.CASE,
            identity={"case_id": case.case_id},
            label="Historical semantic case",
            search_segments=(
                *case.evidence_families,
                *case.positive_evidence_fields,
                *case.missing_evidence_fields,
                *case.counter_evidence_fields,
                *case.hard_breaks,
                *case.false_positive_patterns,
                *reference_summaries,
            ),
            archetype_id=case.canonical_archetype_id,
            case_id=case.case_id,
            role_slot=BalancedMemoryRole.CONTEXT_CASE,
            available_from_date=case.trigger_date or case.entry_date,
            planner_payload={
                "kind": "historical_case_pattern",
                "semantic_role": role,
                "evidence_families": list(_safe_segments(case.evidence_families)),
                "positive_patterns": list(
                    _safe_segments(case.positive_evidence_fields)
                ),
                "missing_patterns": list(
                    _safe_segments(case.missing_evidence_fields)
                ),
                "counter_patterns": list(
                    _safe_segments(
                        (*case.counter_evidence_fields, *case.false_positive_patterns)
                    )
                ),
                "source_quality_state": case.declared_source_quality,
            },
            planner_visible=planner_visible,
        )
        _add_node(nodes, case_node)
        case_nodes[case.case_id] = case_node.node_id
        archetype_node_id = archetype_nodes.get(case.canonical_archetype_id)
        if archetype_node_id:
            relation = {
                "POSITIVE": MemoryEdgeType.SUPPORTS,
                "COUNTER": MemoryEdgeType.COUNTERS,
                "HARD_BREAK": MemoryEdgeType.CAPS,
            }.get(role, MemoryEdgeType.SAME_MECHANISM)
            _add_edge(
                edges,
                relation,
                case_node.node_id,
                archetype_node_id,
                f"Historical case is linked as {role.lower()} semantic memory.",
                planner_visible=case_node.planner_visible,
            )

    for verification in ordered_verifications:
        case_node_id = case_nodes.get(verification.case_id)
        if not case_node_id:
            continue
        case_node = nodes[case_node_id]
        planner_visible = case_node.planner_visible and not _contains_forbidden_outcome(
            verification.verification_id
        )
        source_node = _node(
            node_type=MemoryNodeType.SOURCE,
            identity={"verification_id": verification.verification_id},
            label="Historical source verification",
            search_segments=(
                verification.source_state,
                verification.blocker_code or "",
                verification.blocker_detail or "",
                verification.target_directness,
                verification.case_relationship or "",
                *verification.exact_quotes,
            ),
            archetype_id=case_node.archetype_id,
            case_id=verification.case_id,
            source_verification_id=verification.verification_id,
            available_from_date=verification.published_date,
            planner_payload={
                "kind": "historical_source_verification",
                "source_state": verification.source_state,
                "blocker_code": verification.blocker_code,
                "blocker_detail": _safe_optional(verification.blocker_detail),
                "target_directness": verification.target_directness,
                "case_relationship": verification.case_relationship,
                "historical_replay_ready": verification.historical_replay_ready,
                "exact_anchors": list(_safe_segments(verification.exact_quotes)),
            },
            planner_visible=planner_visible,
        )
        _add_node(nodes, source_node)
        source_nodes[verification.verification_id] = source_node.node_id
        edge_type = _source_case_edge_type(verification)
        if edge_type == MemoryEdgeType.FAILED_IN:
            source_id, target_id = case_node_id, source_node.node_id
        else:
            source_id, target_id = source_node.node_id, case_node_id
        _add_edge(
            edges,
            edge_type,
            source_id,
            target_id,
            _source_edge_rationale(verification),
            planner_visible=planner_visible,
        )

    recipe_ids_by_archetype: dict[str, list[str]] = defaultdict(list)
    for recipe in ordered_recipes:
        archetype_node_id = archetype_nodes.get(recipe.archetype_id)
        primitive_node_id = primitive_nodes.get(
            (recipe.archetype_id, recipe.primitive_id)
        )
        if archetype_node_id is None or primitive_node_id is None:
            raise ValueError(
                "recipe references a pair outside the canonical Evidence Contract: "
                f"{recipe.archetype_id}/{recipe.primitive_id}"
            )
        planner_visible = nodes[archetype_node_id].planner_visible
        recipe_node = _recipe_node(recipe, planner_visible=planner_visible)
        _add_node(nodes, recipe_node)
        recipe_nodes[recipe.recipe_id] = recipe_node.node_id
        recipe_ids_by_archetype[recipe.archetype_id].append(recipe.recipe_id)
        _add_edge(
            edges,
            MemoryEdgeType.REQUIRES,
            archetype_node_id,
            recipe_node.node_id,
            "The archetype requires this direct evidence question for the exact primitive.",
            planner_visible=planner_visible,
        )
        _add_edge(
            edges,
            MemoryEdgeType.REQUIRES,
            recipe_node.node_id,
            primitive_node_id,
            "The recipe resolves this exact primitive without substring routing.",
            planner_visible=planner_visible,
        )

        role_nodes = _recipe_role_nodes(recipe, planner_visible=planner_visible)
        for role_node in role_nodes:
            _add_node(nodes, role_node)
        role_by_slot = {node.role_slot: node for node in role_nodes}
        positive = role_by_slot[BalancedMemoryRole.POSITIVE.value]
        counter = role_by_slot[BalancedMemoryRole.COUNTEREXAMPLE_GUARD.value]
        source_success = role_by_slot[BalancedMemoryRole.SOURCE_SUCCESS.value]
        source_failure = role_by_slot[BalancedMemoryRole.SOURCE_FAILURE.value]
        semantic_guard = role_by_slot[BalancedMemoryRole.SEMANTIC_GUARD.value]

        positive_relation = (
            MemoryEdgeType.CAPS
            if recipe.role in {
                EvidenceRecipeRole.GUARD.value,
                EvidenceRecipeRole.HARD_BREAK.value,
            }
            else MemoryEdgeType.SUPPORTS
        )
        _add_edge(
            edges,
            positive_relation,
            positive.node_id,
            recipe_node.node_id,
            "Positive evidence for this recipe supports or caps the thesis according to its role.",
            planner_visible=planner_visible,
        )
        _add_edge(
            edges,
            MemoryEdgeType.COUNTERS,
            counter.node_id,
            recipe_node.node_id,
            "Counterevidence prevents one-sided retrieval.",
            planner_visible=planner_visible,
        )
        _add_edge(
            edges,
            MemoryEdgeType.BEST_FOUND_IN,
            source_success.node_id,
            recipe_node.node_id,
            "Verified source-success patterns identify where this question is best resolved.",
            planner_visible=planner_visible,
        )
        _add_edge(
            edges,
            MemoryEdgeType.FAILED_IN,
            recipe_node.node_id,
            source_failure.node_id,
            "Source-failure patterns record where the question remained unresolved.",
            planner_visible=planner_visible,
        )
        _add_edge(
            edges,
            MemoryEdgeType.WRONG_SUBJECT_EXAMPLE,
            semantic_guard.node_id,
            recipe_node.node_id,
            "Wrong-subject and rejection examples are a separate semantic guard.",
            planner_visible=planner_visible,
        )
        _add_edge(
            edges,
            MemoryEdgeType.SUPERSEDES,
            counter.node_id,
            positive.node_id,
            "A current cancellation, reversal, or lifecycle update can supersede old positive evidence.",
            planner_visible=planner_visible,
        )
        if recipe.role == EvidenceRecipeRole.HARD_BREAK.value:
            _add_edge(
                edges,
                MemoryEdgeType.CAPS,
                positive.node_id,
                archetype_node_id,
                "A direct current hard-break can cap the archetype independently of positive score evidence.",
                planner_visible=planner_visible,
            )

        for case_id in recipe.supporting_case_ids:
            case_node_id = case_nodes.get(case_id)
            if not case_node_id:
                continue
            case = case_by_id.get(case_id)
            role = _case_semantic_role(case) if case is not None else "CONTEXT"
            verification_ready = any(
                item.historical_replay_ready for item in source_by_case.get(case_id, ())
            )
            relation = (
                MemoryEdgeType.SUPPORTS
                if role == "POSITIVE" and verification_ready
                else MemoryEdgeType.COUNTERS
                if role in {"COUNTER", "HARD_BREAK"}
                else MemoryEdgeType.SAME_MECHANISM
            )
            _add_edge(
                edges,
                relation,
                case_node_id,
                recipe_node.node_id,
                "Historical case linkage preserves role and source verification state.",
                planner_visible=nodes[case_node_id].planner_visible and planner_visible,
            )
        for case_id in recipe.planning_only_source_proxy_case_ids:
            case_node_id = case_nodes.get(case_id)
            if case_node_id:
                _add_edge(
                    edges,
                    MemoryEdgeType.FAILED_IN,
                    recipe_node.node_id,
                    case_node_id,
                    "Source-proxy case remains planning-only until case-level source repair succeeds.",
                    planner_visible=nodes[case_node_id].planner_visible and planner_visible,
                )
        for verification_id in recipe.supporting_source_verification_ids:
            source_node_id = source_nodes.get(verification_id)
            if source_node_id:
                _add_edge(
                    edges,
                    MemoryEdgeType.BEST_FOUND_IN,
                    recipe_node.node_id,
                    source_node_id,
                    "Replay-ready historical source demonstrates a source-success path.",
                    planner_visible=nodes[source_node_id].planner_visible and planner_visible,
                )
        for verification_id in recipe.supporting_source_failure_verification_ids:
            source_node_id = source_nodes.get(verification_id)
            if source_node_id:
                _add_edge(
                    edges,
                    MemoryEdgeType.FAILED_IN,
                    recipe_node.node_id,
                    source_node_id,
                    "Blocked historical verification demonstrates a source-failure path.",
                    planner_visible=nodes[source_node_id].planner_visible and planner_visible,
                )

    for archetype_id, recipe_ids in sorted(recipe_ids_by_archetype.items()):
        ordered_ids = sorted(recipe_ids)
        for left_index, left_recipe_id in enumerate(ordered_ids):
            for right_recipe_id in ordered_ids[left_index + 1 :]:
                left = recipe_nodes[left_recipe_id]
                right = recipe_nodes[right_recipe_id]
                planner_visible = nodes[left].planner_visible and nodes[right].planner_visible
                _add_edge(
                    edges,
                    MemoryEdgeType.SAME_MECHANISM,
                    left,
                    right,
                    f"Recipes share the reviewed economic mechanism for {archetype_id}.",
                    planner_visible=planner_visible,
                )

    graph = ResearchMemoryGraph(
        graph_id=stable_intelligence_id(
            "memory-graph",
            {
                "node_ids": sorted(nodes),
                "edge_ids": sorted(edges),
                "schema_version": SEMANTIC_MEMORY_GRAPH_SCHEMA_VERSION,
            },
        ),
        nodes=tuple(nodes[node_id] for node_id in sorted(nodes)),
        edges=tuple(edges[edge_id] for edge_id in sorted(edges)),
        schema_version=SEMANTIC_MEMORY_GRAPH_SCHEMA_VERSION,
    )
    index = build_semantic_memory_index(graph)
    manifest = _build_manifest(
        graph=graph,
        index=index,
        cases=ordered_cases,
        recipes=ordered_recipes,
        verifications=ordered_verifications,
        verification_by_id=verification_by_id,
    )
    return SemanticMemoryCompilationResult(graph=graph, index=index, manifest=manifest)


def build_semantic_memory_index(graph: ResearchMemoryGraph) -> SemanticMemoryIndex:
    entries = tuple(
        SemanticMemoryIndexEntry(
            node_id=node.node_id,
            node_type=node.node_type,
            archetype_id=node.archetype_id,
            primitive_id=node.primitive_id,
            recipe_id=node.recipe_id,
            role_slot=node.role_slot,
            concepts=semantic_concepts(node.search_text),
            available_from_date=node.available_from_date,
            planner_visible=node.planner_visible,
            search_text_sha256=hashlib.sha256(
                node.search_text.encode("utf-8")
            ).hexdigest(),
            schema_version=SEMANTIC_MEMORY_INDEX_SCHEMA_VERSION,
        )
        for node in graph.nodes
    )
    return SemanticMemoryIndex(graph=graph, entries=entries)


def write_semantic_memory_graph(
    result: SemanticMemoryCompilationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root) / "retrieval"
    paths = {
        "nodes": root / "research_memory_nodes.jsonl",
        "edges": root / "research_memory_edges.jsonl",
        "index": root / "semantic_memory_index.jsonl",
        "manifest": root / "semantic_memory_manifest.json",
        "report": root / "semantic_memory_report.md",
    }
    write_jsonl(paths["nodes"], (node.to_dict() for node in result.graph.nodes))
    write_jsonl(paths["edges"], (edge.to_dict() for edge in result.graph.edges))
    write_jsonl(paths["index"], (entry.to_dict() for entry in result.index.entries))
    write_json(paths["manifest"], dict(result.manifest))
    write_text(paths["report"], render_semantic_memory_report(result.manifest))
    return paths


def render_semantic_memory_report(manifest: Mapping[str, Any]) -> str:
    lines = [
        "# E2R Semantic Memory Graph",
        "",
        f"- status: {manifest['status']}",
        f"- graph_id: {manifest['graph_id']}",
        f"- node_count: {manifest['node_count']}",
        f"- edge_count: {manifest['edge_count']}",
        f"- planner_visible_node_count: {manifest['planner_visible_node_count']}",
        f"- hidden_outcome_identity_node_count: {manifest['hidden_outcome_identity_node_count']}",
        f"- critical_count_sum: {manifest['critical_count_sum']}",
        "",
        "Retrieval uses unique semantic concepts. Node count, degree, input order,",
        "historical returns, MFE/MAE, and runtime score are not ranking inputs.",
    ]
    return "\n".join(lines) + "\n"


def _recipe_node(recipe: EvidenceRecipe, *, planner_visible: bool) -> MemoryNode:
    predicate_payload = [
        {
            "semantic_test": _safe_optional(predicate.semantic_test),
            "required_subject_relation": _safe_optional(
                predicate.required_subject_relation
            ),
            "required_fields": list(_safe_segments(predicate.required_fields)),
            "allowed_polarities": list(predicate.allowed_polarities),
            "temporal_test": _safe_optional(predicate.temporal_test),
            "lifecycle_test": _safe_optional(predicate.lifecycle_test),
        }
        for predicate in recipe.accepted_claim_predicates
    ]
    search_segments = (
        recipe.economic_mechanism,
        recipe.question_to_answer,
        *(predicate.semantic_test for predicate in recipe.accepted_claim_predicates),
        *recipe.required_entities,
        *recipe.required_values,
        *recipe.required_units,
        *recipe.positive_examples,
        *recipe.counterexamples,
        *recipe.wrong_subject_examples,
        *recipe.source_success_examples,
        *recipe.source_failure_examples,
        *recipe.rejection_conditions,
        *recipe.counter_questions,
        *recipe.supersession_questions,
    )
    return _node(
        node_type=MemoryNodeType.RECIPE,
        identity={"recipe_id": recipe.recipe_id},
        label=recipe.question_to_answer,
        search_segments=search_segments,
        archetype_id=recipe.archetype_id,
        primitive_id=recipe.primitive_id,
        recipe_id=recipe.recipe_id,
        role_slot=BalancedMemoryRole.DIRECT_RECIPE,
        planner_payload={
            "kind": "direct_evidence_recipe",
            "role": recipe.role,
            "economic_mechanism": _safe_optional(recipe.economic_mechanism),
            "question_to_answer": _safe_optional(recipe.question_to_answer),
            "accepted_claim_predicates": predicate_payload,
            "required_entities": list(_safe_segments(recipe.required_entities)),
            "required_values": list(_safe_segments(recipe.required_values)),
            "required_units": list(_safe_segments(recipe.required_units)),
            "required_time_scope": list(
                _safe_segments(recipe.required_time_scope)
            ),
            "required_target_directness": list(
                _safe_segments(recipe.required_target_directness)
            ),
            "required_current_lifecycle": list(
                _safe_segments(recipe.required_current_lifecycle)
            ),
            "preferred_source_families": list(recipe.preferred_source_families),
            "preferred_document_types": list(recipe.preferred_document_types),
            "preferred_sections": list(_safe_segments(recipe.preferred_sections)),
            "discovery_sources": list(recipe.discovery_sources),
            "forbidden_score_sources": list(recipe.forbidden_score_sources),
            "rejection_conditions": list(
                _safe_segments(recipe.rejection_conditions)
            ),
            "counter_questions": list(_safe_segments(recipe.counter_questions)),
            "supersession_questions": list(
                _safe_segments(recipe.supersession_questions)
            ),
            "query_intent_constraints": list(
                _safe_segments(recipe.query_intent_constraints)
            ),
            "stop_conditions": list(_safe_segments(recipe.stop_conditions)),
            "source_exhaustion_conditions": list(
                _safe_segments(recipe.source_exhaustion_conditions)
            ),
        },
        planner_visible=planner_visible,
    )


def _recipe_role_nodes(
    recipe: EvidenceRecipe,
    *,
    planner_visible: bool,
) -> tuple[MemoryNode, ...]:
    positive_type = (
        MemoryNodeType.HARD_BREAK
        if recipe.role == EvidenceRecipeRole.HARD_BREAK.value
        else MemoryNodeType.POSITIVE
    )
    specs = (
        (
            BalancedMemoryRole.POSITIVE,
            positive_type,
            (*recipe.positive_examples, *(p.semantic_test for p in recipe.accepted_claim_predicates)),
            {
                "kind": "positive_or_guard_evidence",
                "recipe_role": recipe.role,
                "examples": list(_safe_segments(recipe.positive_examples)),
                "accepted_predicates": [
                    _safe_optional(predicate.semantic_test)
                    for predicate in recipe.accepted_claim_predicates
                ],
            },
        ),
        (
            BalancedMemoryRole.COUNTEREXAMPLE_GUARD,
            MemoryNodeType.COUNTER,
            (*recipe.counterexamples, *recipe.counter_questions, *recipe.supersession_questions),
            {
                "kind": "counterexample_guard",
                "examples": list(_safe_segments(recipe.counterexamples)),
                "counter_questions": list(_safe_segments(recipe.counter_questions)),
                "supersession_questions": list(
                    _safe_segments(recipe.supersession_questions)
                ),
            },
        ),
        (
            BalancedMemoryRole.SOURCE_SUCCESS,
            MemoryNodeType.SOURCE_SUCCESS,
            (
                *recipe.source_success_examples,
                *recipe.preferred_source_families,
                *recipe.preferred_document_types,
                *recipe.preferred_sections,
            ),
            {
                "kind": "source_success",
                "examples": list(_safe_segments(recipe.source_success_examples)),
                "preferred_source_families": list(recipe.preferred_source_families),
                "preferred_document_types": list(recipe.preferred_document_types),
                "preferred_sections": list(_safe_segments(recipe.preferred_sections)),
                "verified_source_count": len(
                    recipe.supporting_source_verification_ids
                ),
            },
        ),
        (
            BalancedMemoryRole.SOURCE_FAILURE,
            MemoryNodeType.SOURCE_FAILURE,
            (
                *recipe.source_failure_examples,
                *recipe.forbidden_score_sources,
                *recipe.source_exhaustion_conditions,
            ),
            {
                "kind": "source_failure",
                "examples": list(_safe_segments(recipe.source_failure_examples)),
                "forbidden_score_sources": list(recipe.forbidden_score_sources),
                "source_exhaustion_conditions": list(
                    _safe_segments(recipe.source_exhaustion_conditions)
                ),
                "blocked_source_count": len(
                    recipe.supporting_source_failure_verification_ids
                ),
            },
        ),
        (
            BalancedMemoryRole.SEMANTIC_GUARD,
            MemoryNodeType.COUNTER,
            (
                *recipe.wrong_subject_examples,
                *recipe.rejection_conditions,
                *recipe.required_target_directness,
            ),
            {
                "kind": "wrong_subject_semantic_guard",
                "wrong_subject_examples": list(
                    _safe_segments(recipe.wrong_subject_examples)
                ),
                "rejection_conditions": list(
                    _safe_segments(recipe.rejection_conditions)
                ),
                "required_target_directness": list(
                    _safe_segments(recipe.required_target_directness)
                ),
            },
        ),
    )
    return tuple(
        _node(
            node_type=node_type,
            identity={"recipe_id": recipe.recipe_id, "role_slot": role.value},
            label=role.value.replace("_", " ").title(),
            search_segments=search_segments,
            archetype_id=recipe.archetype_id,
            primitive_id=recipe.primitive_id,
            recipe_id=recipe.recipe_id,
            role_slot=role,
            planner_payload=payload,
            planner_visible=planner_visible,
        )
        for role, node_type, search_segments, payload in specs
    )


def _node(
    *,
    node_type: MemoryNodeType,
    identity: Mapping[str, Any],
    label: str,
    search_segments: Iterable[str],
    archetype_id: str | None = None,
    primitive_id: str | None = None,
    case_id: str | None = None,
    recipe_id: str | None = None,
    source_verification_id: str | None = None,
    role_slot: BalancedMemoryRole | None = None,
    available_from_date: str | None = None,
    planner_payload: Mapping[str, Any] | None = None,
    planner_visible: bool = True,
) -> MemoryNode:
    clean_segments = _safe_segments(search_segments)
    clean_label = label if not _contains_forbidden_outcome(label) else node_type.value.title()
    return MemoryNode(
        node_id=stable_intelligence_id(
            "memory-node",
            {"node_type": node_type.value, **dict(identity)},
        ),
        node_type=node_type.value,
        label=clean_label,
        search_text="\n".join(clean_segments),
        archetype_id=archetype_id,
        primitive_id=primitive_id,
        case_id=case_id,
        recipe_id=recipe_id,
        source_verification_id=source_verification_id,
        role_slot=role_slot.value if role_slot else None,
        available_from_date=available_from_date,
        planner_payload=dict(planner_payload or {}),
        planner_visible=planner_visible,
        planning_only=True,
        runtime_score_eligible=False,
        schema_version=SEMANTIC_MEMORY_GRAPH_SCHEMA_VERSION,
    )


def _add_node(nodes: dict[str, MemoryNode], node: MemoryNode) -> None:
    previous = nodes.get(node.node_id)
    if previous is not None and previous != node:
        raise ValueError(f"memory node identity collision: {node.node_id}")
    nodes[node.node_id] = node


def _add_edge(
    edges: dict[str, MemoryEdge],
    edge_type: MemoryEdgeType,
    source_node_id: str,
    target_node_id: str,
    rationale: str,
    *,
    planner_visible: bool,
) -> None:
    edge_id = stable_intelligence_id(
        "memory-edge",
        {
            "edge_type": edge_type.value,
            "source_node_id": source_node_id,
            "target_node_id": target_node_id,
        },
    )
    edge = MemoryEdge(
        edge_id=edge_id,
        edge_type=edge_type.value,
        source_node_id=source_node_id,
        target_node_id=target_node_id,
        rationale=rationale,
        planner_visible=planner_visible,
        planning_only=True,
        runtime_score_eligible=False,
        schema_version=SEMANTIC_MEMORY_GRAPH_SCHEMA_VERSION,
    )
    previous = edges.get(edge_id)
    if previous is not None and previous != edge:
        raise ValueError(f"memory edge identity collision: {edge_id}")
    edges[edge_id] = edge


def _case_semantic_role(case: HistoricalResearchCase | None) -> str:
    if case is None:
        return "CONTEXT"
    classification = str(case.classification or "").strip().lower()
    case_role = str(case.case_role or "").strip().lower()
    if case.hard_breaks:
        return "HARD_BREAK"
    if (
        classification in _COUNTER_CLASSIFICATIONS
        or case_role in _COUNTER_CASE_ROLES
        or case.counter_evidence_fields
        or case.false_positive_patterns
    ):
        return "COUNTER"
    if (
        classification in _POSITIVE_CLASSIFICATIONS
        or case_role in _POSITIVE_CASE_ROLES
        or case.positive_evidence_fields
    ):
        return "POSITIVE"
    return "CONTEXT"


def _source_case_edge_type(
    verification: HistoricalSourceVerification,
) -> MemoryEdgeType:
    if verification.historical_replay_ready:
        return MemoryEdgeType.SUPPORTS
    if (
        verification.source_state
        == HistoricalSourceState.URL_FETCHED_WRONG_SUBJECT.value
    ):
        return MemoryEdgeType.WRONG_SUBJECT_EXAMPLE
    if verification.case_relationship == "COUNTER_CASE_MATCH":
        return MemoryEdgeType.COUNTERS
    return MemoryEdgeType.FAILED_IN


def _source_edge_rationale(verification: HistoricalSourceVerification) -> str:
    if verification.historical_replay_ready:
        return "Fetched content, date, subject, anchor, and case semantics all passed."
    if (
        verification.source_state
        == HistoricalSourceState.URL_FETCHED_WRONG_SUBJECT.value
    ):
        return "Fetched content belongs to a different target and is a wrong-subject example."
    return "Historical source remains blocked and is usable only as source-failure memory."


def _build_manifest(
    *,
    graph: ResearchMemoryGraph,
    index: SemanticMemoryIndex,
    cases: Sequence[HistoricalResearchCase],
    recipes: Sequence[EvidenceRecipe],
    verifications: Sequence[HistoricalSourceVerification],
    verification_by_id: Mapping[str, HistoricalSourceVerification],
) -> Mapping[str, Any]:
    node_by_id = {node.node_id: node for node in graph.nodes}
    node_types = Counter(node.node_type for node in graph.nodes)
    edge_types = Counter(edge.edge_type for edge in graph.edges)
    required_node_types = {item.value for item in MemoryNodeType}
    required_edge_types = {item.value for item in MemoryEdgeType}
    expected_roles = {
        BalancedMemoryRole.DIRECT_RECIPE.value,
        BalancedMemoryRole.POSITIVE.value,
        BalancedMemoryRole.COUNTEREXAMPLE_GUARD.value,
        BalancedMemoryRole.SOURCE_SUCCESS.value,
        BalancedMemoryRole.SOURCE_FAILURE.value,
        BalancedMemoryRole.SEMANTIC_GUARD.value,
    }
    roles_by_recipe: dict[str, set[str]] = defaultdict(set)
    for node in graph.nodes:
        if node.recipe_id and node.role_slot:
            roles_by_recipe[node.recipe_id].add(node.role_slot)
    recipe_role_bundle_missing = sum(
        roles_by_recipe.get(recipe.recipe_id, set()) != expected_roles
        for recipe in recipes
    )
    edge_endpoint_ids = {
        edge.source_node_id for edge in graph.edges
    } | {edge.target_node_id for edge in graph.edges}
    planner_visible_leakage = sum(
        node.planner_visible
        and _contains_forbidden_outcome(
            json.dumps(node.to_dict(), ensure_ascii=False, sort_keys=True)
        )
        for node in graph.nodes
    )
    hidden_outcome_identity = sum(
        not node.planner_visible
        and _contains_forbidden_outcome(
            " ".join(
                item
                for item in (
                    node.archetype_id,
                    node.case_id,
                    node.recipe_id,
                    node.source_verification_id,
                )
                if item
            )
        )
        for node in graph.nodes
    )
    visible_index_leakage = sum(
        entry.planner_visible
        and _contains_forbidden_outcome(" ".join(entry.concepts))
        for entry in index.entries
    )
    critical = {
        "missing_required_node_type": len(required_node_types - set(node_types)),
        "missing_required_edge_type": len(required_edge_types - set(edge_types)),
        "dangling_edge": sum(
            edge.source_node_id not in node_by_id
            or edge.target_node_id not in node_by_id
            for edge in graph.edges
        ),
        "orphan_node": sum(node.node_id not in edge_endpoint_ids for node in graph.nodes),
        "recipe_role_bundle_missing": recipe_role_bundle_missing,
        "planner_visible_future_outcome_node": planner_visible_leakage,
        "planner_visible_future_outcome_index_entry": visible_index_leakage,
        "runtime_score_eligible_node_or_edge": sum(
            node.runtime_score_eligible for node in graph.nodes
        )
        + sum(edge.runtime_score_eligible for edge in graph.edges),
        "source_success_id_not_replay_ready": sum(
            verification_id not in verification_by_id
            or not verification_by_id[verification_id].historical_replay_ready
            for recipe in recipes
            for verification_id in recipe.supporting_source_verification_ids
        ),
        "source_failure_id_marked_ready": sum(
            verification_id in verification_by_id
            and verification_by_id[verification_id].historical_replay_ready
            for recipe in recipes
            for verification_id in recipe.supporting_source_failure_verification_ids
        ),
        "first_n_only_index": 0,
        "popularity_weight_in_index": 0,
    }
    return {
        "schema_version": SEMANTIC_MEMORY_GRAPH_SCHEMA_VERSION,
        "status": (
            "SEMANTIC_MEMORY_GRAPH_COMPILER_PASS"
            if sum(critical.values()) == 0
            else "SEMANTIC_MEMORY_GRAPH_COMPILER_FAIL"
        ),
        "graph_id": graph.graph_id,
        "index_strategy": index.strategy,
        "case_count": len(cases),
        "recipe_count": len(recipes),
        "source_verification_count": len(verifications),
        "node_count": len(graph.nodes),
        "edge_count": len(graph.edges),
        "planner_visible_node_count": sum(node.planner_visible for node in graph.nodes),
        "hidden_outcome_identity_node_count": hidden_outcome_identity,
        "node_count_by_type": dict(sorted(node_types.items())),
        "edge_count_by_type": dict(sorted(edge_types.items())),
        "index_entry_count": len(index.entries),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "node_hash": stable_hash([node.to_dict() for node in graph.nodes]),
        "edge_hash": stable_hash([edge.to_dict() for edge in graph.edges]),
        "index_hash": stable_hash([entry.to_dict() for entry in index.entries]),
        "historical_outcomes_compiled_into_graph": 0,
        "production_runtime_ready": False,
    }


def _safe_segments(values: Iterable[Any]) -> tuple[str, ...]:
    clean: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value or "").strip()
        if not text or _contains_forbidden_outcome(text) or text in seen:
            continue
        seen.add(text)
        clean.append(text)
    return tuple(clean)


def _safe_optional(value: Any) -> str | None:
    clean = str(value or "").strip()
    if not clean or _contains_forbidden_outcome(clean):
        return None
    return clean


def _contains_forbidden_outcome(value: str) -> bool:
    return bool(_FORBIDDEN_OUTCOME_RE.search(str(value or "")))


def _humanize(value: str) -> str:
    parts = str(value or "").strip().split("_")
    if parts and re.fullmatch(r"(?:C|R)[0-9]+", parts[0], re.IGNORECASE):
        parts = parts[1:]
    return " ".join(parts).lower()


__all__ = [
    "SEMANTIC_INDEX_STRATEGY",
    "SEMANTIC_MEMORY_GRAPH_SCHEMA_VERSION",
    "SEMANTIC_MEMORY_INDEX_SCHEMA_VERSION",
    "SemanticMemoryCompilationResult",
    "SemanticMemoryIndex",
    "build_semantic_memory_index",
    "compile_semantic_memory_graph",
    "render_semantic_memory_report",
    "semantic_concepts",
    "write_semantic_memory_graph",
]
