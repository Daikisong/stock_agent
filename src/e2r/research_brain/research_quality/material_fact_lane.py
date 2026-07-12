"""Build the canonical production side of the blind material-fact benchmark."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import stable_hash, write_json, write_jsonl


PRODUCTION_MATERIAL_FACT_SCHEMA_VERSION = "e2r_production_material_fact_lane_v1"


@dataclass(frozen=True)
class ProductionMaterialFactLane:
    facts: tuple[Mapping[str, Any], ...]
    inputs: tuple[Mapping[str, Any], ...]
    manifest: Mapping[str, Any]


def combine_production_material_fact_lanes(
    lanes: tuple[ProductionMaterialFactLane, ...],
) -> ProductionMaterialFactLane:
    if not lanes:
        raise ValueError("at least one production material-fact lane is required")
    as_of_dates = {
        str(lane.manifest.get("as_of_date") or "") for lane in lanes
    }
    if len(as_of_dates) != 1 or not next(iter(as_of_dates)):
        raise ValueError("combined production lanes must share one as_of_date")
    facts = tuple(row for lane in lanes for row in lane.facts)
    inputs = tuple(row for lane in lanes for row in lane.inputs)
    _require_unique(facts, "fact_id")
    _require_unique(inputs, "input_id")
    target_ids = sorted(
        {str(lane.manifest.get("target_id") or "") for lane in lanes}
    )
    if any(not target_id for target_id in target_ids):
        raise ValueError("combined production lane target_id is missing")
    manifest = {
        "schema_version": PRODUCTION_MATERIAL_FACT_SCHEMA_VERSION,
        "lane_role": "PRODUCTION",
        "target_ids": target_ids,
        "as_of_date": next(iter(as_of_dates)),
        "gold_visibility": False,
        "production_fact_count": len(facts),
        "production_input_count": len(inputs),
        "planner_input_classes": [
            "QUESTION_CONTRACT",
            "CURRENT_PRODUCTION_EVIDENCE",
            "SCORE_GAP_CONTEXT",
        ],
        "forbidden_input_classes": [
            "GOLD_URL",
            "GOLD_QUERY",
            "GOLD_FACT",
            "EXPECTED_COMPONENT",
            "EXPECTED_SCORE",
        ],
        "post_run_fact_compilation": True,
        "combined_lane_count": len(lanes),
    }
    return ProductionMaterialFactLane(
        facts=facts,
        inputs=inputs,
        manifest=manifest,
    )


def compile_production_material_fact_lane(
    *,
    dossier_root: str | Path,
    target_id: str,
    as_of_date: str,
) -> ProductionMaterialFactLane:
    root = Path(dossier_root)
    claims = {
        str(row.get("claim_id") or ""): row
        for row in _read_jsonl(root / "accepted_current_claims.jsonl")
    }
    provenance = {
        str(row.get("claim_id") or ""): row
        for row in _read_jsonl(root / "claim_provenance.jsonl")
    }
    clusters = {
        str(row.get("fact_cluster_id") or ""): row
        for row in _read_jsonl(root / "economic_fact_clusters.jsonl")
    }
    impacts = _read_jsonl(root / "claim_impacts_validated.jsonl")
    if not claims or not provenance or not impacts:
        raise ValueError(
            "production material-fact lane requires accepted claims, provenance, and validated impacts"
        )
    grouped: dict[tuple[str, ...], list[Mapping[str, Any]]] = {}
    for impact in impacts:
        claim_id = str(impact.get("claim_id") or "")
        if claim_id not in claims or claim_id not in provenance:
            raise ValueError("validated impact lacks current claim or provenance")
        key = (
            claim_id,
            str(impact.get("question_family_id") or ""),
            str(impact.get("primitive_id") or ""),
            str(impact.get("direction") or ""),
            str(impact.get("fact_cluster_id") or ""),
        )
        grouped.setdefault(key, []).append(impact)
    facts = tuple(
        _material_fact(
            target_id=target_id,
            as_of_date=as_of_date,
            key=key,
            impacts=rows,
            claim=claims[key[0]],
            provenance=provenance[key[0]],
            cluster=clusters.get(key[4], {}),
        )
        for key, rows in sorted(grouped.items())
    )
    inputs = _production_inputs(root=root, target_id=target_id)
    manifest = {
        "schema_version": PRODUCTION_MATERIAL_FACT_SCHEMA_VERSION,
        "lane_role": "PRODUCTION",
        "target_id": target_id,
        "as_of_date": as_of_date,
        "gold_visibility": False,
        "production_fact_count": len(facts),
        "production_input_count": len(inputs),
        "planner_input_classes": [
            "QUESTION_CONTRACT",
            "CURRENT_PRODUCTION_EVIDENCE",
            "SCORE_GAP_CONTEXT",
        ],
        "forbidden_input_classes": [
            "GOLD_URL",
            "GOLD_QUERY",
            "GOLD_FACT",
            "EXPECTED_COMPONENT",
            "EXPECTED_SCORE",
        ],
        "post_run_fact_compilation": True,
    }
    return ProductionMaterialFactLane(facts=facts, inputs=inputs, manifest=manifest)


def write_production_material_fact_lane(
    lane: ProductionMaterialFactLane,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "facts": root / "production_material_facts.jsonl",
        "inputs": root / "production_input_manifest.jsonl",
        "manifest": root / "production_lane_manifest.json",
    }
    write_jsonl(paths["facts"], lane.facts)
    write_jsonl(paths["inputs"], lane.inputs)
    write_json(paths["manifest"], lane.manifest)
    return paths


def _material_fact(
    *,
    target_id: str,
    as_of_date: str,
    key: tuple[str, ...],
    impacts: list[Mapping[str, Any]],
    claim: Mapping[str, Any],
    provenance: Mapping[str, Any],
    cluster: Mapping[str, Any],
) -> Mapping[str, Any]:
    claim_id, question_family_id, primitive_id, direction, fact_cluster_id = key
    first = impacts[0]
    scope = ((first.get("scope_validation") or {}).get("scope") or {})
    raw = claim.get("raw_assertion") or {}
    subject = str(
        cluster.get("normalized_subject")
        or "/".join(
            value
            for value in (
                str(scope.get("issuer_id") or target_id),
                str(scope.get("business_segment") or "UNSPECIFIED"),
                str(scope.get("product_family") or "UNSPECIFIED"),
            )
            if value
        )
    )
    predicate = str(
        cluster.get("normalized_predicate")
        or raw.get("predicate")
        or primitive_id
    )
    normalized_object = str(
        cluster.get("normalized_object_value")
        or raw.get("object_text")
        or raw.get("value")
        or primitive_id
    )
    period = str(
        cluster.get("period")
        or scope.get("effective_period")
        or claim.get("effective_start")
        or claim.get("event_date")
        or as_of_date
    )
    mechanism_scope_id = "|".join(
        str(scope.get(field) or "UNSPECIFIED").upper()
        for field in (
            "business_segment",
            "product_family",
            "economic_mechanism",
        )
    )
    semantic_payload = {
        "target_id": target_id,
        "question_family_id": question_family_id,
        "subject_id": _normalize(subject),
        "predicate_family": _normalize(predicate),
        "normalized_object": _normalize(normalized_object),
        "period": _normalize(period),
        "mechanism_scope_id": mechanism_scope_id,
    }
    return {
        "fact_id": "PFACT-" + stable_hash(
            {
                **semantic_payload,
                "claim_id": claim_id,
                "primitive_id": primitive_id,
                "direction": direction,
                "fact_cluster_id": fact_cluster_id,
            }
        )[:24],
        **semantic_payload,
        "claim_id": claim_id,
        "primitive_id": primitive_id,
        "mapping_ids": sorted(
            {
                str(row.get("mapping_id") or "")
                for row in impacts
                if str(row.get("mapping_id") or "")
            }
        ),
        "impact_ids": sorted(
            {
                str(row.get("impact_id") or "")
                for row in impacts
                if str(row.get("impact_id") or "")
            }
        ),
        "fact_cluster_id": fact_cluster_id,
        "source_tier": _source_tier(first, provenance),
        "temporal_status": str(claim.get("temporal_status") or ""),
        "as_of_date": as_of_date,
        "fact_role": _fact_role(direction),
        "source_url": str(provenance.get("source_url") or ""),
        "exact_quote": str(provenance.get("exact_quote") or ""),
        "discovery_origin": "CANONICAL_SOURCE_TASK",
    }


def _production_inputs(*, root: Path, target_id: str) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = [
        {
            "input_id": "PINPUT-" + stable_hash(
                {"target_id": target_id, "type": "CONFIG"}
            )[:24],
            "input_type": "CONFIG",
            "value": "C06 canonical production question and scoring contracts",
            "origin": "CANONICAL_CONFIG",
        }
    ]
    seen_queries: set[str] = set()
    task_rows = tuple(
        (
            *_read_jsonl(root / "question_source_tasks.jsonl"),
            *_read_jsonl(root / "executed_question_source_tasks.jsonl"),
        )
    )
    for task in task_rows:
        for query in (task.get("query_intent") or {}).get("literal_queries") or ():
            value = str(query).strip()
            if not value or value.casefold() in seen_queries:
                continue
            seen_queries.add(value.casefold())
            rows.append(
                {
                    "input_id": "PINPUT-" + stable_hash(
                        {
                            "target_id": target_id,
                            "task_id": task.get("task_id"),
                            "query": value,
                        }
                    )[:24],
                    "input_type": "QUERY",
                    "value": value,
                    "origin": "LLM_PLANNER",
                }
            )
    rows.append(
        {
            "input_id": "PINPUT-" + stable_hash(
                {"target_id": target_id, "type": "PROMPT_CONTEXT"}
            )[:24],
            "input_type": "PROMPT_CONTEXT",
            "value": "question contracts, current production evidence, and score-gap context only",
            "origin": "CANONICAL_PIPELINE",
        }
    )
    return tuple(rows)


def _source_tier(
    impact: Mapping[str, Any], provenance: Mapping[str, Any]
) -> str:
    source_family = str(impact.get("source_family") or "").upper()
    url = str(provenance.get("source_url") or "").casefold()
    if source_family == "OFFICIAL_FILING" or any(
        host in url for host in ("dart.fss.or.kr", "kind.krx.co.kr")
    ):
        return "REGULATORY_OFFICIAL"
    if source_family in {"ISSUER_OFFICIAL", "ISSUER_IR"}:
        return "ISSUER_OFFICIAL"
    if source_family == "CUSTOMER_OFFICIAL":
        return "CUSTOMER_OFFICIAL"
    if source_family in {"FINANCIAL_REVISION", "COMPANYGUIDE"}:
        return "FINANCIAL_REVISION"
    return "TRUSTED_INDEPENDENT"


def _fact_role(direction: str) -> str:
    normalized = str(direction or "").upper()
    if normalized in {"COUNTER", "NEGATIVE", "RISK_OPEN"}:
        return "COUNTER"
    if normalized in {"RESOLUTION", "RISK_RESOLVED", "SUPERSESSION"}:
        return "SUPERSESSION"
    return "SUPPORT"


def _normalize(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().casefold())


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _require_unique(rows: tuple[Mapping[str, Any], ...], key: str) -> None:
    values = [str(row.get(key) or "") for row in rows]
    if any(not value for value in values) or len(values) != len(set(values)):
        raise ValueError(f"combined production lane {key} must be present and unique")


__all__ = [
    "PRODUCTION_MATERIAL_FACT_SCHEMA_VERSION",
    "ProductionMaterialFactLane",
    "combine_production_material_fact_lanes",
    "compile_production_material_fact_lane",
    "write_production_material_fact_lane",
]
