"""Canonical EvidenceFact graph and terminal claim-utilization orchestration."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .claim_utilization import (
    CLAIM_UTILIZATION_STATUSES,
    ClaimComponentImpactProposal,
    ClaimTerminalDisposition,
    ClaimUtilizationLedgerBuilder,
    ClaimUtilizationLedgerResult,
)
from .evidence_fact_compiler import EvidenceFactCompiler, FactCompilationResult
from .schemas import CANONICAL_COMPONENT_ORDER, EvidenceFact


EVIDENCE_FACT_GRAPH_OUTPUT_FILES: Mapping[str, str] = {
    "facts": "evidence_facts.jsonl",
    "claim_fact_links": "claim_fact_links.jsonl",
    "graph_nodes": "evidence_fact_graph_nodes.jsonl",
    "graph_edges": "evidence_fact_graph_edges.jsonl",
    "validated_impacts": "claim_component_impacts.jsonl",
    "claim_utilization": "claim_utilization.jsonl",
    "audit": "evidence_fact_graph_audit.json",
}


@dataclass(frozen=True)
class EvidenceFactGraphNode:
    node_id: str
    node_type: str
    target_id: str
    as_of_date: str
    payload: Mapping[str, Any]
    production_score_authority: bool = False
    schema_version: str = "e2r_evidence_fact_graph_node_v1"

    def __post_init__(self) -> None:
        if self.node_type not in {
            "CLAIM",
            "FACT",
            "FACT_REFERENCE",
            "SOURCE",
            "QUESTION_FAMILY_TAG",
            "PRIMITIVE_TAG",
            "COMPONENT",
            "IMPACT",
            "UTILIZATION",
        }:
            raise ValueError("unknown EvidenceFact graph node type")
        if not self.node_id.strip() or not self.target_id.strip() or not self.as_of_date:
            raise ValueError("EvidenceFact graph node identity is incomplete")
        if self.production_score_authority:
            raise ValueError("EvidenceFact graph nodes cannot assign production score")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class EvidenceFactGraphEdge:
    edge_id: str
    from_node_id: str
    to_node_id: str
    relationship: str
    metadata: Mapping[str, Any]
    production_score_authority: bool = False
    schema_version: str = "e2r_evidence_fact_graph_edge_v1"

    def __post_init__(self) -> None:
        if not all(
            value.strip()
            for value in (
                self.edge_id,
                self.from_node_id,
                self.to_node_id,
                self.relationship,
            )
        ):
            raise ValueError("EvidenceFact graph edge identity is incomplete")
        if self.production_score_authority:
            raise ValueError("EvidenceFact graph edges cannot assign production score")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class EvidenceFactGraphResult:
    status: str
    target_id: str
    as_of_date: str
    fact_compilation: FactCompilationResult
    claim_utilization: ClaimUtilizationLedgerResult
    nodes: tuple[EvidenceFactGraphNode, ...]
    edges: tuple[EvidenceFactGraphEdge, ...]
    audit: Mapping[str, Any]
    ready_for_component_scoring_memos: bool
    production_score_authority: bool = False
    schema_version: str = "e2r_evidence_fact_graph_result_v1"

    def __post_init__(self) -> None:
        if self.status not in {
            "EVIDENCE_FACT_GRAPH_COMPLETE",
            "EVIDENCE_FACT_GRAPH_PENDING",
        }:
            raise ValueError("unknown EvidenceFact graph status")
        if self.ready_for_component_scoring_memos != (
            self.status == "EVIDENCE_FACT_GRAPH_COMPLETE"
            and int(self.audit.get("critical_count_sum") or 0) == 0
        ):
            raise ValueError("EvidenceFact graph readiness contradicts audit")
        if self.production_score_authority:
            raise ValueError("EvidenceFact graph cannot assign production score")
        node_ids = [row.node_id for row in self.nodes]
        edge_ids = [row.edge_id for row in self.edges]
        if len(node_ids) != len(set(node_ids)):
            raise ValueError("EvidenceFact graph node ids must be unique")
        if len(edge_ids) != len(set(edge_ids)):
            raise ValueError("EvidenceFact graph edge ids must be unique")
        known_nodes = set(node_ids)
        if any(
            row.from_node_id not in known_nodes or row.to_node_id not in known_nodes
            for row in self.edges
        ):
            raise ValueError("EvidenceFact graph edge references an unknown node")

    @property
    def facts(self) -> tuple[EvidenceFact, ...]:
        return self.fact_compilation.facts

    def component_fact_views(self) -> Mapping[str, Mapping[str, Any]]:
        fact_by_id = {row.fact_id: row for row in self.facts}
        result: dict[str, Mapping[str, Any]] = {}
        for component_id in CANONICAL_COMPONENT_ORDER:
            impacts = tuple(
                row
                for row in self.claim_utilization.validated_impacts
                if row.component_id == component_id
            )
            support_ids = tuple(
                sorted({row.fact_id for row in impacts if row.direction == "SUPPORT"})
            )
            counter_ids = tuple(
                sorted({row.fact_id for row in impacts if row.direction == "COUNTER"})
            )
            visible_ids = tuple(sorted(set((*support_ids, *counter_ids))))
            result[component_id] = {
                "component_id": component_id,
                "support_fact_ids": list(support_ids),
                "counter_fact_ids": list(counter_ids),
                "impact_ids": [row.impact_id for row in impacts],
                "validated_credit_units_diagnostic": {
                    row.impact_id: row.validated_credit_units for row in impacts
                },
                "facts": [fact_by_id[fact_id].to_dict() for fact_id in visible_ids],
                "question_family_tags": sorted(
                    {
                        tag
                        for fact_id in visible_ids
                        for tag in fact_by_id[fact_id].question_family_tags
                    }
                ),
                "primitive_tags": sorted(
                    {
                        tag
                        for fact_id in visible_ids
                        for tag in fact_by_id[fact_id].primitive_tags
                    }
                ),
                "question_family_score_gateway": False,
                "primitive_score_gateway": False,
                "production_score_authority": False,
            }
        return result

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "status": self.status,
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "fact_compilation": self.fact_compilation.to_dict(),
            "claim_utilization": self.claim_utilization.to_dict(),
            "nodes": [row.to_dict() for row in self.nodes],
            "edges": [row.to_dict() for row in self.edges],
            "audit": dict(self.audit),
            "ready_for_component_scoring_memos": (
                self.ready_for_component_scoring_memos
            ),
            "production_score_authority": False,
        }


class EvidenceFactGraphEngine:
    """Close claims into facts, utilization rows, impacts, and graph lineage."""

    def compile(
        self,
        *,
        target_id: str,
        as_of_date: str,
        material_claims: Sequence[Mapping[str, Any]],
        impact_proposals: Sequence[ClaimComponentImpactProposal],
        explicit_dispositions: Sequence[ClaimTerminalDisposition] = (),
        claim_total_credit_cap: float = 1.0,
        fact_total_credit_cap: float = 1.0,
        component_fact_credit_cap: float = 1.0,
    ) -> EvidenceFactGraphResult:
        compilation = EvidenceFactCompiler().compile(
            target_id=target_id,
            as_of_date=as_of_date,
            accepted_claims=material_claims,
        )
        return self.build(
            target_id=target_id,
            as_of_date=as_of_date,
            fact_compilation=compilation,
            impact_proposals=impact_proposals,
            explicit_dispositions=explicit_dispositions,
            claim_total_credit_cap=claim_total_credit_cap,
            fact_total_credit_cap=fact_total_credit_cap,
            component_fact_credit_cap=component_fact_credit_cap,
        )

    def build(
        self,
        *,
        target_id: str,
        as_of_date: str,
        fact_compilation: FactCompilationResult,
        impact_proposals: Sequence[ClaimComponentImpactProposal],
        explicit_dispositions: Sequence[ClaimTerminalDisposition] = (),
        claim_total_credit_cap: float = 1.0,
        fact_total_credit_cap: float = 1.0,
        component_fact_credit_cap: float = 1.0,
    ) -> EvidenceFactGraphResult:
        if (
            fact_compilation.target_id != target_id
            or fact_compilation.as_of_date != as_of_date
        ):
            raise ValueError("EvidenceFact graph compilation target/as_of mismatch")
        utilization = ClaimUtilizationLedgerBuilder().build(
            fact_compilation=fact_compilation,
            impact_proposals=impact_proposals,
            explicit_dispositions=explicit_dispositions,
            claim_total_credit_cap=claim_total_credit_cap,
            fact_total_credit_cap=fact_total_credit_cap,
            component_fact_credit_cap=component_fact_credit_cap,
        )
        nodes, edges = _build_graph(
            target_id=target_id,
            as_of_date=as_of_date,
            compilation=fact_compilation,
            utilization=utilization,
        )
        audit = _audit_graph(
            compilation=fact_compilation,
            utilization=utilization,
            nodes=nodes,
            edges=edges,
        )
        status = (
            "EVIDENCE_FACT_GRAPH_COMPLETE"
            if audit["critical_count_sum"] == 0
            else "EVIDENCE_FACT_GRAPH_PENDING"
        )
        return EvidenceFactGraphResult(
            status=status,
            target_id=target_id,
            as_of_date=as_of_date,
            fact_compilation=fact_compilation,
            claim_utilization=utilization,
            nodes=nodes,
            edges=edges,
            audit=audit,
            ready_for_component_scoring_memos=(
                status == "EVIDENCE_FACT_GRAPH_COMPLETE"
            ),
        )


def write_evidence_fact_graph_result(
    result: EvidenceFactGraphResult,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_directory)
    paths = {
        key: root / filename
        for key, filename in EVIDENCE_FACT_GRAPH_OUTPUT_FILES.items()
    }
    write_jsonl(paths["facts"], (row.to_dict() for row in result.facts))
    write_jsonl(
        paths["claim_fact_links"],
        (row.to_dict() for row in result.fact_compilation.claim_fact_links),
    )
    write_jsonl(paths["graph_nodes"], (row.to_dict() for row in result.nodes))
    write_jsonl(paths["graph_edges"], (row.to_dict() for row in result.edges))
    write_jsonl(
        paths["validated_impacts"],
        (row.to_dict() for row in result.claim_utilization.validated_impacts),
    )
    write_jsonl(
        paths["claim_utilization"],
        (row.to_dict() for row in result.claim_utilization.utilization_decisions),
    )
    write_json(paths["audit"], result.audit)
    return paths


def _build_graph(
    *,
    target_id: str,
    as_of_date: str,
    compilation: FactCompilationResult,
    utilization: ClaimUtilizationLedgerResult,
) -> tuple[tuple[EvidenceFactGraphNode, ...], tuple[EvidenceFactGraphEdge, ...]]:
    nodes: dict[str, EvidenceFactGraphNode] = {}
    edges: dict[str, EvidenceFactGraphEdge] = {}

    def add_node(
        node_id: str, node_type: str, payload: Mapping[str, Any]
    ) -> None:
        candidate = EvidenceFactGraphNode(
            node_id=node_id,
            node_type=node_type,
            target_id=target_id,
            as_of_date=as_of_date,
            payload=_json_safe(payload),
        )
        prior = nodes.get(node_id)
        if prior is not None and prior != candidate:
            raise ValueError("EvidenceFact graph node id collision")
        nodes[node_id] = candidate

    def add_edge(
        from_id: str,
        to_id: str,
        relationship: str,
        metadata: Mapping[str, Any] | None = None,
    ) -> None:
        identity = {
            "from": from_id,
            "to": to_id,
            "relationship": relationship,
            "metadata": dict(metadata or {}),
        }
        edge = EvidenceFactGraphEdge(
            edge_id=stable_intelligence_id("EFEDGE", identity),
            from_node_id=from_id,
            to_node_id=to_id,
            relationship=relationship,
            metadata=_json_safe(metadata or {}),
        )
        edges[edge.edge_id] = edge

    fact_by_id = {row.fact_id: row for row in compilation.facts}
    for fact in compilation.facts:
        add_node(fact.fact_id, "FACT", fact.to_dict())
        for source_id in fact.source_ids:
            source_node_id = stable_intelligence_id("EFSOURCE", source_id)
            add_node(source_node_id, "SOURCE", {"source_id": source_id})
            add_edge(source_node_id, fact.fact_id, "SOURCE_SUPPORTS_FACT")
        for tag in fact.question_family_tags:
            tag_node_id = stable_intelligence_id("EFQTAG", tag)
            add_node(
                tag_node_id,
                "QUESTION_FAMILY_TAG",
                {"tag": tag, "score_gateway": False},
            )
            add_edge(fact.fact_id, tag_node_id, "FACT_TAGGED_QUESTION_FAMILY")
        for tag in fact.primitive_tags:
            tag_node_id = stable_intelligence_id("EFPTAG", tag)
            add_node(
                tag_node_id,
                "PRIMITIVE_TAG",
                {"tag": tag, "score_gateway": False},
            )
            add_edge(fact.fact_id, tag_node_id, "FACT_TAGGED_PRIMITIVE")
    for link in compilation.claim_fact_links:
        claim_node_id = stable_intelligence_id("EFCLAIM", link.claim_id)
        add_node(
            claim_node_id,
            "CLAIM",
            {
                "claim_id": link.claim_id,
                "accepted": True,
                "material": link.material_claim,
                "link_role": link.link_role,
            },
        )
        add_edge(
            claim_node_id,
            link.fact_id,
            "CLAIM_MATERIALIZES_FACT",
            {"link_role": link.link_role},
        )
        for related_id, relationship in (
            *((value, "FACT_SUPERSEDES_FACT") for value in link.supersedes_fact_ids),
            *((value, "FACT_RESOLVES_FACT") for value in link.resolves_fact_ids),
        ):
            if related_id not in fact_by_id:
                add_node(
                    related_id,
                    "FACT_REFERENCE",
                    {"fact_id": related_id, "external_reference": True},
                )
            add_edge(link.fact_id, related_id, relationship)
    for rejection in compilation.rejected_claims:
        claim_node_id = stable_intelligence_id(
            "EFCLAIM",
            {"claim_id": rejection.claim_id, "input_index": rejection.input_index},
        )
        add_node(
            claim_node_id,
            "CLAIM",
            {
                "claim_id": rejection.claim_id,
                "accepted": rejection.accepted_claim,
                "material": rejection.material_claim,
                "rejection_reason": rejection.reason,
            },
        )
    impact_by_id = {
        row.impact_id: row for row in utilization.validated_impacts
    }
    for impact in utilization.validated_impacts:
        impact_node_id = stable_intelligence_id("EFIMPACT", impact.impact_id)
        component_node_id = stable_intelligence_id(
            "EFCOMPONENT", impact.component_id
        )
        add_node(impact_node_id, "IMPACT", impact.to_dict())
        add_node(
            component_node_id,
            "COMPONENT",
            {"component_id": impact.component_id},
        )
        add_edge(impact.fact_id, impact_node_id, "FACT_HAS_VALIDATED_IMPACT")
        add_edge(
            impact_node_id,
            component_node_id,
            (
                "FACT_SUPPORTS_COMPONENT"
                if impact.direction == "SUPPORT"
                else "FACT_COUNTERS_COMPONENT"
            ),
            {
                "validated_credit_units": impact.validated_credit_units,
                "production_points_authority": False,
            },
        )
    claim_node_by_claim_id = {
        str(row.payload.get("claim_id") or ""): row.node_id
        for row in nodes.values()
        if row.node_type == "CLAIM"
    }
    for decision in utilization.utilization_decisions:
        utilization_node_id = stable_intelligence_id(
            "EFUTIL", decision.utilization_id
        )
        add_node(utilization_node_id, "UTILIZATION", decision.to_dict())
        claim_node_id = claim_node_by_claim_id.get(decision.claim_id)
        if claim_node_id:
            add_edge(
                claim_node_id,
                utilization_node_id,
                "CLAIM_HAS_TERMINAL_UTILIZATION",
            )
        if decision.fact_id:
            add_edge(
                utilization_node_id,
                decision.fact_id,
                "UTILIZATION_USES_FACT",
            )
        for impact_id in decision.impact_ids:
            if impact_id in impact_by_id:
                add_edge(
                    utilization_node_id,
                    stable_intelligence_id("EFIMPACT", impact_id),
                    "UTILIZATION_CITES_IMPACT",
                )
    return (
        tuple(sorted(nodes.values(), key=lambda row: row.node_id)),
        tuple(sorted(edges.values(), key=lambda row: row.edge_id)),
    )


def _audit_graph(
    *,
    compilation: FactCompilationResult,
    utilization: ClaimUtilizationLedgerResult,
    nodes: Sequence[EvidenceFactGraphNode],
    edges: Sequence[EvidenceFactGraphEdge],
) -> Mapping[str, Any]:
    fact_by_id = {row.fact_id: row for row in compilation.facts}
    link_by_fact: dict[str, list[Any]] = {}
    for link in compilation.claim_fact_links:
        link_by_fact.setdefault(link.fact_id, []).append(link)
    confidence_violations = 0
    for fact_id, links in link_by_fact.items():
        if not any(row.link_role == "INDEPENDENT_CORROBORATION" for row in links):
            continue
        maximum = max(row.claim_confidence for row in links)
        combined = fact_by_id[fact_id].confidence
        confidence_violations += int(
            combined + 1e-12 < maximum
            or (maximum < 1 and combined <= maximum + 1e-12)
        )
    material_claim_ids = {
        row.claim_id
        for row in compilation.claim_fact_links
        if row.material_claim
    } | {
        row.claim_id for row in compilation.rejected_claims if row.material_claim
    }
    utilized_claim_ids = {
        row.claim_id for row in utilization.utilization_decisions
    }
    relationship_counts = {
        relationship: sum(row.relationship == relationship for row in edges)
        for relationship in sorted({row.relationship for row in edges})
    }
    utilization_node_count = sum(
        row.node_type == "UTILIZATION" for row in nodes
    )
    critical = {
        "accepted_claim_without_fact_count": (
            compilation.accepted_claim_without_fact_count
        ),
        "material_claim_without_terminal_utilization_count": len(
            material_claim_ids - utilized_claim_ids
        ),
        "claim_fact_link_missing_count": sum(
            row.link_role == "PRIMARY_FACT_CLAIM"
            and row.fact_id not in fact_by_id
            for row in compilation.claim_fact_links
        ),
        "claim_fact_graph_edge_mismatch_count": abs(
            relationship_counts.get("CLAIM_MATERIALIZES_FACT", 0)
            - len(compilation.claim_fact_links)
        ),
        "terminal_utilization_node_mismatch_count": abs(
            utilization_node_count
            - len(utilization.utilization_decisions)
        ),
        "terminal_utilization_edge_mismatch_count": abs(
            relationship_counts.get("CLAIM_HAS_TERMINAL_UTILIZATION", 0)
            - len(utilization.utilization_decisions)
        ),
        "validated_impact_graph_edge_mismatch_count": abs(
            relationship_counts.get("FACT_HAS_VALIDATED_IMPACT", 0)
            - len(utilization.validated_impacts)
        ),
        "independent_corroboration_confidence_not_improved_count": (
            confidence_violations
        ),
        "utilization_ledger_critical_count": int(
            utilization.audit.get("critical_count_sum") or 0
        ),
        "same_fact_duplicate_credit_count": int(
            utilization.audit["critical_counts"].get(
                "duplicate_or_corroboration_scored_again_count", 0
            )
        ),
        "question_or_primitive_tag_score_gateway_count": sum(
            bool(row.payload.get("score_gateway"))
            for row in nodes
            if row.node_type in {"QUESTION_FAMILY_TAG", "PRIMITIVE_TAG"}
        ),
        "graph_score_authority_count": sum(
            row.production_score_authority for row in nodes
        )
        + sum(row.production_score_authority for row in edges),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_evidence_fact_graph_audit_v1",
        "status": (
            "EVIDENCE_FACT_GRAPH_AUDIT_PASS"
            if critical_sum == 0
            else "EVIDENCE_FACT_GRAPH_AUDIT_FAIL"
        ),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
        "input_claim_count": compilation.input_claim_count,
        "accepted_claim_count": compilation.accepted_claim_count,
        "fact_count": len(compilation.facts),
        "node_count": len(nodes),
        "edge_count": len(edges),
        "relationship_counts": relationship_counts,
        "utilization_status_counts": {
            status: sum(
                row.status == status
                for row in utilization.utilization_decisions
            )
            for status in CLAIM_UTILIZATION_STATUSES
        },
        "same_economic_fact_points_once": True,
        "independent_corroboration_improves_confidence": True,
        "many_to_many_component_impacts_allowed": True,
        "component_mechanism_and_total_credit_validated": True,
        "question_family_score_gateway": False,
        "primitive_score_gateway": False,
        "production_score_authority": False,
    }


def _json_safe(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, sort_keys=True, default=str))


__all__ = [
    "EVIDENCE_FACT_GRAPH_OUTPUT_FILES",
    "EvidenceFactGraphEdge",
    "EvidenceFactGraphEngine",
    "EvidenceFactGraphNode",
    "EvidenceFactGraphResult",
    "write_evidence_fact_graph_result",
]
