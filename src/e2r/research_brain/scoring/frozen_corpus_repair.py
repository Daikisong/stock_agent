"""52f09f3의 고정 corpus를 새 semantic scoring 경로로 재검증한다."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from .business_mechanism_scope import infer_business_mechanism_scope


FROZEN_REPAIR_SCHEMA_VERSION = "e2r_frozen_52f09f3_repair_audit_v1"
FROZEN_REPAIR_PASS = "FROZEN_52F09F3_REPAIR_PASS"
FROZEN_REPAIR_FAIL = "FROZEN_52F09F3_REPAIR_FAIL"

FROZEN_INPUT_LEAVES = (
    "accepted_current_claims.jsonl",
    "adjudicated_claims.jsonl",
    "claim_provenance.jsonl",
    "evidence_anchors.jsonl",
    "evidence_documents.jsonl",
    "executed_question_source_tasks.jsonl",
    "primitive_mappings.jsonl",
    "provider_fetch_results.jsonl",
    "query_change_log.jsonl",
    "question_closure.jsonl",
    "question_source_tasks.jsonl",
    "raw_assertions.jsonl",
    "research_brain_plans.jsonl",
    "research_provider_requests.jsonl",
    "research_web_fetched_documents.jsonl",
    "research_web_rejected_documents.jsonl",
    "research_web_search_results.jsonl",
    "research_web_search_tasks.jsonl",
    "source_timeline.jsonl",
)


def compile_frozen_52f09f3_repair_audit(
    *, config_path: str | Path
) -> Mapping[str, Any]:
    config_file = Path(config_path)
    config = _json(config_file)
    if config.get("schema_version") != "e2r_frozen_52f09f3_repair_config_v1":
        raise ValueError("frozen repair config schema mismatch")
    repo_root = config_file.resolve().parent.parent
    source_root = _resolve(repo_root, str(config["source_root"]))
    output_root = _resolve(repo_root, str(config["output_root"]))
    targets = tuple(
        _evaluate_target(
            source_root=source_root / str(row["target_id"]),
            output_root=output_root / str(row["target_id"]),
            config=dict(row),
            archetype_id=str(config["archetype_id"]),
        )
        for row in config.get("targets") or ()
    )
    critical = {
        "target_roster_missing_count": int(not targets),
        "frozen_input_leaf_mismatch_count": sum(
            row["critical_counts"]["frozen_input_leaf_mismatch_count"]
            for row in targets
        ),
        "new_document_count": sum(
            row["critical_counts"]["new_document_count"] for row in targets
        ),
        "missing_source_document_count": sum(
            row["critical_counts"]["missing_source_document_count"]
            for row in targets
        ),
        "document_payload_mismatch_count": sum(
            row["critical_counts"]["document_payload_mismatch_count"]
            for row in targets
        ),
        "partial_bridge_missing_cap_zero_count": sum(
            row["critical_counts"][
                "partial_bridge_missing_cap_zero_count"
            ]
            for row in targets
        ),
        "legacy_missing_cap_impact_not_repaired_count": sum(
            row["critical_counts"][
                "legacy_missing_cap_impact_not_repaired_count"
            ]
            for row in targets
        ),
        "supported_question_absent_component_count": sum(
            row["critical_counts"][
                "supported_question_absent_component_count"
            ]
            for row in targets
        ),
        "positive_impact_internal_error_count": sum(
            row["critical_counts"][
                "positive_impact_internal_error_count"
            ]
            for row in targets
        ),
        "counter_capacity_impact_ignored_count": sum(
            row["critical_counts"][
                "counter_capacity_impact_ignored_count"
            ]
            for row in targets
        ),
        "required_supported_fact_missing_count": sum(
            row["critical_counts"][
                "required_supported_fact_missing_count"
            ]
            for row in targets
        ),
        "required_bounded_impact_missing_count": sum(
            row["critical_counts"][
                "required_bounded_impact_missing_count"
            ]
            for row in targets
        ),
        "foundry_hbm_scope_violation_count": sum(
            row["critical_counts"][
                "foundry_hbm_scope_violation_count"
            ]
            for row in targets
        ),
        "foundry_reroute_missing_count": sum(
            row["critical_counts"]["foundry_reroute_missing_count"]
            for row in targets
        ),
        "provider_error_count": sum(
            row["critical_counts"]["provider_error_count"]
            for row in targets
        ),
    }
    critical_sum = sum(critical.values())
    payload = {
        "schema_version": FROZEN_REPAIR_SCHEMA_VERSION,
        "status": (
            FROZEN_REPAIR_PASS if critical_sum == 0 else FROZEN_REPAIR_FAIL
        ),
        "as_of_date": str(config["as_of_date"]),
        "source_commit": str(config["source_commit"]),
        "source_root": str(config["source_root"]),
        "output_root": str(config["output_root"]),
        "search_or_fetch_performed": False,
        "new_documents_allowed": False,
        "target_results": targets,
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
        "investment_recommendation_emitted": False,
    }
    return json.loads(json.dumps(payload, ensure_ascii=False))


def _evaluate_target(
    *,
    source_root: Path,
    output_root: Path,
    config: Mapping[str, Any],
    archetype_id: str,
) -> Mapping[str, Any]:
    leaf_hashes = {
        name: {
            "before_sha256": _file_hash(source_root / name),
            "after_sha256": _file_hash(output_root / name),
        }
        for name in FROZEN_INPUT_LEAVES
    }
    input_mismatches = tuple(
        name
        for name, row in leaf_hashes.items()
        if not row["before_sha256"]
        or row["before_sha256"] != row["after_sha256"]
    )
    before_documents = _by_id(
        _jsonl(source_root / "evidence_documents.jsonl"), "document_id"
    )
    after_documents = _by_id(
        _jsonl(output_root / "evidence_documents.jsonl"), "document_id"
    )
    new_document_ids = tuple(sorted(set(after_documents) - set(before_documents)))
    missing_document_ids = tuple(
        sorted(set(before_documents) - set(after_documents))
    )
    document_mismatches = tuple(
        document_id
        for document_id in sorted(set(before_documents) & set(after_documents))
        if _stable_json(before_documents[document_id])
        != _stable_json(after_documents[document_id])
    )
    before_impacts = _jsonl(source_root / "claim_impacts_validated.jsonl")
    after_impacts = _jsonl(output_root / "claim_impacts_validated.jsonl")
    after_rejected = _jsonl(output_root / "claim_impacts_rejected.jsonl")
    after_proposals = _jsonl(output_root / "claim_impacts_proposed.jsonl")
    reconciliations = _jsonl(
        output_root / "question_component_reconciliation.jsonl"
    )
    reconciliation_audit = _json_or_empty(
        output_root / "question_component_reconciliation_audit.json"
    )
    impact_audit = _json_or_empty(output_root / "impact_validation_audit.json")
    subcriteria = _jsonl(output_root / "component_subcriteria.jsonl")
    adjudications = _jsonl(output_root / "impact_adjudications.jsonl")
    dispositions = _jsonl(
        output_root / "impact_mapping_dispositions.jsonl"
    )
    before_cap_zeros = tuple(
        row for row in before_impacts if _legacy_missing_cap_zero(row)
    )
    after_cap_zeros = tuple(
        row
        for row in after_impacts
        if float(row.get("raw_credit_fraction") or 0.0) > 0
        and float(row.get("validated_credit_fraction") or 0.0) <= 0
        and not row.get("duplicate_reason")
        and any(
            float(row.get(name) or 0.0) <= 0
            for name in (
                "causal_cap",
                "source_cap",
                "temporal_cap",
                "support_type_cap",
            )
        )
    )
    after_by_semantic_key: dict[tuple[str, str, str, str], list[Mapping[str, Any]]] = {}
    after_by_claim: dict[str, list[Mapping[str, Any]]] = {}
    for row in after_impacts:
        after_by_semantic_key.setdefault(_impact_semantic_key(row), []).append(row)
        after_by_claim.setdefault(str(row.get("claim_id") or ""), []).append(row)
    rejected_by_claim: dict[str, list[Mapping[str, Any]]] = {}
    for row in after_rejected:
        rejected_by_claim.setdefault(str(row.get("claim_id") or ""), []).append(row)
    adjudication_by_claim = {
        str(row.get("claim_id") or ""): row for row in adjudications
    }
    no_effect_disposition_by_claim: dict[
        str, list[Mapping[str, Any]]
    ] = {}
    for row in dispositions:
        if row.get("status") != (
            "IMPACT_MAPPING_REJECTED_NO_BOUNDED_EFFECT"
        ):
            continue
        no_effect_disposition_by_claim.setdefault(
            str(row.get("claim_id") or ""), []
        ).append(row)
    cap_repair_rows = []
    for row in before_cap_zeros:
        claim_id = str(row.get("claim_id") or "")
        same_edge = after_by_semantic_key.get(_impact_semantic_key(row), ())
        claim_impacts = after_by_claim.get(claim_id, ())
        adjudication = adjudication_by_claim.get(claim_id, {})
        if any(
            float(value.get("validated_credit_fraction") or 0.0) > 0
            or bool(value.get("duplicate_reason"))
            for value in same_edge
        ):
            resolution = "NONZERO_OR_DEDUPED_SAME_EDGE"
        elif claim_impacts:
            resolution = "SEMANTICALLY_RESCOPED_NONZERO"
        elif (
            rejected_by_claim.get(claim_id)
            or no_effect_disposition_by_claim.get(claim_id)
            or adjudication.get("status") == "IMPACT_MAPPING_REJECTED"
        ):
            resolution = "EXPLICIT_SEMANTIC_REJECTION_OR_REROUTE"
        elif adjudication.get("status") in {
            "PROVIDER_ERROR",
            "REVIEW_PENDING",
            "IMPACT_ADJUDICATION_FAIL",
        }:
            resolution = "PROVIDER_OR_REVIEW_PENDING"
        else:
            resolution = "UNRESOLVED_IMPACT_LOSS"
        cap_repair_rows.append(
            {
                "claim_id": str(row.get("claim_id") or ""),
                "primitive_id": str(row.get("primitive_id") or ""),
                "component_id": str(row.get("component_id") or ""),
                "direction": str(row.get("direction") or ""),
                "before_impact_id": str(row.get("impact_id") or ""),
                "before_validated_credit_fraction": float(
                    row.get("validated_credit_fraction") or 0.0
                ),
                "before_support_type_cap": float(
                    row.get("support_type_cap") or 0.0
                ),
                "after_impacts": [
                    _impact_delta(value) for value in same_edge
                ],
                "resolution": resolution,
                "repaired": resolution
                not in {
                    "PROVIDER_OR_REVIEW_PENDING",
                    "UNRESOLVED_IMPACT_LOSS",
                },
            }
        )
    cap_repair_rows = tuple(cap_repair_rows)
    effective_questions = {
        str(row.get("question_family_id") or "")
        for row in reconciliations
        if any(_effective_component_link(link) for link in row.get("component_links") or ())
    }
    required_questions = tuple(
        str(value) for value in config.get("required_supported_questions") or ()
    )
    missing_required_questions = tuple(
        value for value in required_questions if value not in effective_questions
    )
    required_bounded_impact_rows = tuple(
        _required_bounded_impact_result(
            contract=dict(contract), impacts=after_impacts
        )
        for contract in config.get("required_bounded_impacts") or ()
    )
    counter_contract = dict(config.get("required_counter_impact") or {})
    counter_impacts = tuple(
        row
        for row in after_impacts
        if counter_contract
        and str(row.get("primitive_id") or "")
        == str(counter_contract.get("primitive_id") or "")
        and str(row.get("component_id") or "")
        == str(counter_contract.get("component_id") or "")
        and str(row.get("direction") or "") == "COUNTER"
        and float(row.get("counter_effect_fraction") or 0.0) > 0
    )
    accounted_counter_ids = {
        str(impact_id)
        for row in subcriteria
        if float(row.get("counter_effect_points") or 0.0) > 0
        for impact_id in row.get("counter_impact_ids") or ()
    }
    counter_missing = int(bool(counter_contract) and not counter_impacts)
    counter_ignored = sum(
        str(row.get("impact_id") or "") not in accounted_counter_ids
        for row in counter_impacts
    )
    source_claims = _jsonl(source_root / "accepted_current_claims.jsonl")
    source_mappings = _by_id(
        _jsonl(source_root / "primitive_mappings.jsonl"), "mapping_id"
    )
    foundry_claim_ids = _foundry_claim_ids(
        claims=source_claims,
        mappings=source_mappings,
        archetype_id=archetype_id,
    )
    foundry_validated = tuple(
        row
        for row in after_impacts
        if str(row.get("claim_id") or "") in foundry_claim_ids
        and float(row.get("validated_credit_fraction") or 0.0) > 0
    )
    foundry_question_links = tuple(
        {
            "question_family_id": row.get("question_family_id"),
            "claim_id": link.get("claim_id"),
            "impact_id": link.get("impact_id"),
        }
        for row in reconciliations
        if str(row.get("question_family_id") or "")
        in {
            "current_customer_allocation_commitment",
            "customer_concentration_dependency",
        }
        for link in row.get("component_links") or ()
        if str(link.get("claim_id") or "") in foundry_claim_ids
    )
    foundry_reroutes = tuple(
        (
            *(
                row
                for row in after_rejected
                if str(row.get("claim_id") or "") in foundry_claim_ids
                and str(row.get("reason") or "")
                in {
                    "REROUTED_TO_OTHER_MECHANISM",
                    "MECHANISM_SCOPE_REJECTED",
                }
            ),
            *(
                {
                    "claim_id": row.get("claim_id"),
                    "reason": "IMPACT_MAPPING_REJECTED",
                    "review_issues": row.get("review_issues", []),
                }
                for row in adjudications
                if str(row.get("claim_id") or "") in foundry_claim_ids
                and row.get("status") == "IMPACT_MAPPING_REJECTED"
            ),
        )
    )
    require_foundry = bool(config.get("require_foundry_reroute"))
    reconciliation_counts = reconciliation_audit.get("critical_counts") or {}
    impact_counts = impact_audit.get("critical_counts") or {}
    positive_internal_errors = sum(
        int(reconciliation_counts.get(name) or 0)
        for name in (
            "positive_claim_absent_component_count",
            "positive_proposal_absent_component_count",
            "supported_question_zero_credit_count",
            "partially_supported_question_zero_credit_count",
            "supported_non_scoring_component_credit_count",
        )
    ) + int(impact_counts.get("positive_impact_zeroed_by_missing_cap_count") or 0)
    critical = {
        "frozen_input_leaf_mismatch_count": len(input_mismatches),
        "new_document_count": len(new_document_ids),
        "missing_source_document_count": len(missing_document_ids),
        "document_payload_mismatch_count": len(document_mismatches),
        "partial_bridge_missing_cap_zero_count": len(after_cap_zeros),
        "legacy_missing_cap_impact_not_repaired_count": sum(
            row["repaired"] is not True for row in cap_repair_rows
        ),
        "supported_question_absent_component_count": int(
            reconciliation_counts.get(
                "supported_question_absent_component_count"
            )
            or 0
        ),
        "positive_impact_internal_error_count": positive_internal_errors,
        "counter_capacity_impact_ignored_count": counter_missing
        + counter_ignored,
        "required_supported_fact_missing_count": len(
            missing_required_questions
        ),
        "required_bounded_impact_missing_count": sum(
            not row["satisfied"] for row in required_bounded_impact_rows
        ),
        "foundry_hbm_scope_violation_count": len(foundry_validated)
        + len(foundry_question_links)
        + int(require_foundry and not foundry_claim_ids),
        "foundry_reroute_missing_count": int(
            require_foundry and bool(foundry_claim_ids) and not foundry_reroutes
        ),
        "provider_error_count": sum(
            str(row.get("status") or "") == "PROVIDER_ERROR"
            for row in adjudications
        ),
    }
    before_score = _json_or_empty(source_root / "component_score_vector.json")
    after_score = _json_or_empty(output_root / "component_score_vector.json")
    return {
        "target_id": str(config["target_id"]),
        "company_name": str(config["company_name"]),
        "status": "PASS" if sum(critical.values()) == 0 else "FAIL",
        "frozen_input": {
            "leaf_hashes": leaf_hashes,
            "mismatched_leaves": input_mismatches,
            "before_document_count": len(before_documents),
            "after_document_count": len(after_documents),
            "new_document_ids": new_document_ids,
            "missing_document_ids": missing_document_ids,
            "document_payload_mismatch_ids": document_mismatches,
        },
        "required_supported_questions": required_questions,
        "effective_supported_questions": tuple(
            sorted(effective_questions)
        ),
        "missing_required_supported_questions": (
            missing_required_questions
        ),
        "required_bounded_impacts": required_bounded_impact_rows,
        "missing_required_bounded_impact_labels": tuple(
            str(row["label"])
            for row in required_bounded_impact_rows
            if not row["satisfied"]
        ),
        "counter_capacity": {
            "contract": counter_contract,
            "impact_ids": tuple(
                str(row.get("impact_id") or "") for row in counter_impacts
            ),
            "accounted_counter_impact_ids": tuple(
                sorted(accounted_counter_ids)
            ),
        },
        "foundry_scope": {
            "source_claim_ids": tuple(sorted(foundry_claim_ids)),
            "validated_credit_impact_ids": tuple(
                str(row.get("impact_id") or "")
                for row in foundry_validated
            ),
            "forbidden_question_links": foundry_question_links,
            "rerouted_or_rejected_impacts": foundry_reroutes,
        },
        "before_after": {
            "before_verified_supported_score": before_score.get(
                "verified_supported_score"
            ),
            "after_verified_supported_score": after_score.get(
                "verified_supported_score"
            ),
            "before_component_score_vector": before_score.get(
                "component_score_vector", {}
            ),
            "after_component_score_vector": after_score.get(
                "component_score_vector", {}
            ),
            "missing_cap_impact_repairs": cap_repair_rows,
            "after_subcriterion_points": tuple(
                {
                    "subcriterion_id": row.get("subcriterion_id"),
                    "component_id": row.get("component_id"),
                    "points": row.get("points"),
                    "support_impact_ids": row.get("support_impact_ids", []),
                    "counter_impact_ids": row.get("counter_impact_ids", []),
                }
                for row in subcriteria
                if float(row.get("points") or 0.0) > 0
                or float(row.get("counter_effect_points") or 0.0) > 0
            ),
            "after_proposal_count": len(after_proposals),
            "after_validated_impact_count": len(after_impacts),
            "after_rejected_impact_count": len(after_rejected),
            "after_no_bounded_effect_disposition_count": len(
                no_effect_disposition_by_claim
            ),
        },
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


def _legacy_missing_cap_zero(row: Mapping[str, Any]) -> bool:
    if float(row.get("raw_credit_fraction") or 0.0) <= 0:
        return False
    if float(row.get("validated_credit_fraction") or 0.0) > 0:
        return False
    return any(
        float(row.get(name) or 0.0) <= 0
        for name in (
            "causal_cap",
            "source_cap",
            "temporal_cap",
            "support_type_cap",
        )
    )


def _impact_semantic_key(row: Mapping[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(row.get("claim_id") or ""),
        str(row.get("primitive_id") or ""),
        str(row.get("component_id") or ""),
        str(row.get("direction") or ""),
    )


def _impact_delta(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "impact_id": row.get("impact_id"),
        "claim_id": row.get("claim_id"),
        "primitive_id": row.get("primitive_id"),
        "component_id": row.get("component_id"),
        "question_family_id": row.get("question_family_id"),
        "component_subcriterion_id": row.get("component_subcriterion_id"),
        "direction": row.get("direction"),
        "support_type": row.get("support_type"),
        "validated_credit_fraction": row.get("validated_credit_fraction"),
        "support_credit_fraction": row.get("support_credit_fraction"),
        "counter_effect_fraction": row.get("counter_effect_fraction"),
        "support_type_cap": row.get("support_type_cap"),
        "duplicate_reason": row.get("duplicate_reason"),
    }


def _required_bounded_impact_result(
    *, contract: Mapping[str, Any], impacts: Sequence[Mapping[str, Any]]
) -> Mapping[str, Any]:
    allowed_support_types = {
        str(value) for value in contract.get("allowed_support_types") or ()
    }
    matched = tuple(
        row
        for row in impacts
        if float(row.get("validated_credit_fraction") or 0.0) > 0
        and all(
            not str(contract.get(field) or "")
            or str(row.get(field) or "") == str(contract[field])
            for field in (
                "primitive_id",
                "component_id",
                "question_family_id",
                "direction",
            )
        )
        and (
            not allowed_support_types
            or str(row.get("support_type") or "") in allowed_support_types
        )
        and (
            not str(contract.get("scope_product_family") or "")
            or str(
                ((row.get("scope_validation") or {}).get("scope") or {}).get(
                    "product_family"
                )
                or ""
            )
            == str(contract["scope_product_family"])
        )
    )
    return {
        "label": str(contract.get("label") or "UNLABELED_IMPACT"),
        "contract": dict(contract),
        "satisfied": bool(matched),
        "matched_impacts": tuple(_impact_delta(row) for row in matched),
    }


def _effective_component_link(link: Mapping[str, Any]) -> bool:
    return (
        float(link.get("support_credit_fraction") or 0.0) > 0
        or float(link.get("counter_effect_fraction") or 0.0) > 0
        or float(link.get("resolution_effect") or 0.0) > 0
        or bool(link.get("shared_credit_source_impact_id"))
    )


def _foundry_claim_ids(
    *,
    claims: Sequence[Mapping[str, Any]],
    mappings: Mapping[str, Mapping[str, Any]],
    archetype_id: str,
) -> set[str]:
    result = set()
    for claim in claims:
        for mapping_id in claim.get("mapping_ids") or ():
            mapping = mappings.get(str(mapping_id), {})
            scope = infer_business_mechanism_scope(
                claim,
                primitive_id=str(mapping.get("primitive_id") or ""),
                archetype_id=archetype_id,
            )
            if scope.business_segment == "FOUNDRY":
                result.add(str(claim.get("claim_id") or ""))
    return result


def _by_id(
    rows: Sequence[Mapping[str, Any]], key: str
) -> Mapping[str, Mapping[str, Any]]:
    return {
        str(row.get(key) or ""): row
        for row in rows
        if str(row.get(key) or "")
    }


def _file_hash(path: Path) -> str:
    if not path.is_file():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _json_or_empty(path: Path) -> Mapping[str, Any]:
    return _json(path) if path.is_file() else {}


def _jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _stable_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _resolve(repo_root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else repo_root / path


__all__ = [
    "FROZEN_INPUT_LEAVES",
    "FROZEN_REPAIR_FAIL",
    "FROZEN_REPAIR_PASS",
    "FROZEN_REPAIR_SCHEMA_VERSION",
    "compile_frozen_52f09f3_repair_audit",
]
