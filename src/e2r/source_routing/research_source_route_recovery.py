"""Recover runtime source-route patterns from research memory and contracts."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping


OFFICIAL_SOURCE_FAMILIES = ("DART", "KIND", "KRX", "IssuerIR", "CompanyGuide")


def _load_contracts(repo_root: Path) -> list[dict[str, Any]]:
    return json.loads(
        (repo_root / "configs" / "e2r_archetype_evidence_contracts_v12.json").read_text(encoding="utf-8")
    )["contracts"]


def _route_families_for_primitive(primitive_id: str, research_families: list[str]) -> list[tuple[str, str]]:
    primitive = primitive_id.lower()
    official = [("DART", "PRIMARY"), ("IssuerIR", "PRIMARY"), ("CompanyGuide", "SECONDARY")]
    if any(key in primitive for key in ("contract", "backlog", "order", "delivery", "customer")):
        official = [("DART", "PRIMARY"), ("KIND", "PRIMARY"), ("IssuerIR", "SECONDARY"), ("CompanyGuide", "SECONDARY")]
    elif any(key in primitive for key in ("fcf", "cash", "eps", "revision", "opm", "margin", "spread")):
        official = [("DART", "PRIMARY"), ("CompanyGuide", "PRIMARY"), ("IssuerIR", "SECONDARY"), ("BrokerReportPDF", "FALLBACK")]
    elif any(key in primitive for key in ("hbm", "capacity", "qualification", "allocation", "pre_sold")):
        official = [("IssuerIR", "PRIMARY"), ("CompanyGuide", "SECONDARY"), ("TrustedNews", "FALLBACK"), ("BrokerReportPDF", "FALLBACK")]
    elif any(key in primitive for key in ("clinical", "endpoint", "regulatory", "trial", "partner", "runway")):
        official = [("DART", "PRIMARY"), ("IssuerIR", "PRIMARY"), ("TrustedNews", "FALLBACK"), ("IndustryMedia", "FALLBACK")]
    elif any(key in primitive for key in ("arr", "rpo", "renewal", "retention", "churn", "software")):
        official = [("DART", "PRIMARY"), ("IssuerIR", "PRIMARY"), ("CompanyGuide", "SECONDARY"), ("BrokerReportPDF", "FALLBACK")]
    discovery_only = {"NaverSearch", "GeneralWebSearch", "ResearchMemory"}
    research_routes = [
        (family, "DISCOVERY_ONLY" if family in discovery_only else "FALLBACK")
        for family in research_families
    ]
    merged: list[tuple[str, str]] = []
    seen: set[str] = set()
    for family, role in official + research_routes:
        if family in seen:
            continue
        seen.add(family)
        merged.append((family, role))
    for family in ("NaverSearch", "GeneralWebSearch", "ResearchMemory"):
        if family not in seen:
            seen.add(family)
            merged.append((family, "DISCOVERY_ONLY"))
    merged.append(("Snippet", "FORBIDDEN_FOR_SCORE"))
    return merged


def build_source_route_patterns(
    *,
    repo_root: str | Path = ".",
    records: Iterable[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    root = Path(repo_root)
    contracts = _load_contracts(root)
    research_families_by_arch: dict[str, set[str]] = defaultdict(set)
    for record in records:
        archetype_id = str(record.get("canonical_archetype_id"))
        for family in record.get("runtime_source_route_hints", []):
            research_families_by_arch[archetype_id].add(str(family))

    patterns: list[dict[str, Any]] = []
    gap_tasks: list[dict[str, Any]] = []
    for contract in contracts:
        archetype_id = contract["canonical_archetype_id"]
        primitives = list(contract.get("required_primitives") or [])
        for primitive in primitives:
            families = _route_families_for_primitive(primitive, sorted(research_families_by_arch.get(archetype_id, [])))
            for family, role in families:
                pattern = {
                    "schema_version": "e2r_source_route_pattern_v1",
                    "archetype_id": archetype_id,
                    "primitive_id": primitive,
                    "source_family": family,
                    "route_role": role,
                    "examples": [],
                    "requires_full_source": role != "DISCOVERY_ONLY",
                    "requires_quote_anchor": role not in {"DISCOVERY_ONLY", "FORBIDDEN_FOR_SCORE"},
                    "requires_current_lifecycle_check": role not in {"DISCOVERY_ONLY", "FORBIDDEN_FOR_SCORE"},
                    "official_first_required": family in OFFICIAL_SOURCE_FAMILIES or role in {"PRIMARY", "SECONDARY"},
                    "query_intent_examples": [
                        f"verify current source-backed {primitive} with target-company scope",
                    ]
                    if role not in {"FORBIDDEN_FOR_SCORE"}
                    else [],
                    "bad_query_patterns": ["snippet-only", "price-only", "source-proxy-only"],
                    "known_false_positive_sources": ["ResearchMemory score reuse", "search snippet without full source"],
                }
                patterns.append(pattern)
            if not research_families_by_arch.get(archetype_id):
                gap_tasks.append(
                    {
                        "task_id": f"SROUTE-GAP-{archetype_id}-{primitive}",
                        "archetype_id": archetype_id,
                        "primitive_id": primitive,
                        "status": "SOURCE_ROUTE_MEMORY_GAP",
                        "next_action": "use_official_first_route_and_record_source_blocker_if_no_current_anchor",
                    }
                )
    return {
        "schema_version": "e2r_research_source_route_recovery_matrix_v1",
        "pattern_count": len(patterns),
        "archetype_count": len(contracts),
        "patterns": patterns,
        "gap_task_count": len(gap_tasks),
        "gap_tasks": gap_tasks,
        "snippet_score_allowed": False,
        "research_memory_score_allowed": False,
    }


def write_source_route_recovery_reports(
    *,
    repo_root: str | Path = ".",
    docs_dir: str | Path = "docs/operational",
    records: Iterable[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    root = Path(repo_root)
    docs = Path(docs_dir)
    docs = docs if docs.is_absolute() else root / docs
    payload = build_source_route_patterns(repo_root=root, records=records)
    matrix_path = docs / "research_source_route_recovery_matrix.json"
    tasks_path = docs / "research_source_route_gap_tasks.json"
    docs.mkdir(parents=True, exist_ok=True)
    matrix_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tasks_path.write_text(
        json.dumps(
            {
                "schema_version": "e2r_research_source_route_gap_tasks_v1",
                "gap_task_count": payload["gap_task_count"],
                "tasks": payload["gap_tasks"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return {"source_route_matrix": payload, "matrix_path": matrix_path, "gap_tasks_path": tasks_path}


__all__ = ["OFFICIAL_SOURCE_FAMILIES", "build_source_route_patterns", "write_source_route_recovery_reports"]
