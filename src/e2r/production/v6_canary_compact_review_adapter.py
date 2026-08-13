"""Blind Collaboration review adapter for compact Phase-106 receipts.

Reviewers see evidence lineage, never the production score vector, total, or
Stage.  After two distinct validated Collaboration responses attest that the
lineage is complete, deterministic code replays the compact receipt and fills
the review projection from that replay.  Reviewers therefore have no direct
score or Stage authority.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import hashlib
import json
from pathlib import Path
from typing import Any

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_compact_receipt import (
    COMPACT_REVIEW_PASS,
    COMPACT_REVIEW_SCHEMA,
    validate_selection_bound_canary_artifacts,
    validate_selection_bound_canary_bundle,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.collaboration_envelope_contract import (
    validate_collaboration_request,
    validate_collaboration_response_envelope,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexSubagentTransport,
)


BLIND_REVIEW_SCHEMA = "e2r_v6_compact_blind_review_response_v1"
BLIND_REVIEW_PASS_NAME = "COMPACT_CANARY_BLIND_REVIEW"
BLIND_REVIEW_OUTPUT_SCHEMA_NAME = "e2r_v5_compact_canary_blind_review"
REVIEWER_SLOTS = ("A", "B")
PORTABLE_REVIEWER_ROLE_IDS = {
    "A": "CODEX_POST_RUN_REVIEWER_A",
    "B": "CODEX_POST_RUN_REVIEWER_B",
}

_RESPONSE_KEYS = frozenset(
    {
        "schema_version",
        "reviewer_slot",
        "selection_id",
        "target_id",
        "archetype_id",
        "as_of_date",
        "blind_artifact_hash",
        "evidence_lineage_complete",
        "component_roster_complete",
        "judge_roster_complete",
        "fact_source_anchor_linkage_complete",
        "critical_findings",
        "material_fact_omission_count",
        "counterfact_omission_count",
        "subject_or_segment_mismatch_count",
        "currentness_failure_count",
        "source_quality_failure_count",
        "component_calibration_failure_count",
        "historical_anchor_analogy_failure_count",
        "review_complete",
        "score_or_stage_authority",
    }
)


def _mapping(value: object, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def compact_blind_review_output_schema() -> Mapping[str, Any]:
    """Return the exact response schema shared by both independent slots."""

    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": sorted(_RESPONSE_KEYS),
        "properties": {
            "schema_version": {"enum": [BLIND_REVIEW_SCHEMA]},
            "reviewer_slot": {"enum": list(REVIEWER_SLOTS)},
            "selection_id": {"type": "string", "minLength": 1},
            "target_id": {"type": "string", "pattern": "^[0-9A-Z]{6}$"},
            "archetype_id": {"type": "string", "minLength": 1},
            "as_of_date": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
            "blind_artifact_hash": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "evidence_lineage_complete": {"type": "boolean"},
            "component_roster_complete": {"type": "boolean"},
            "judge_roster_complete": {"type": "boolean"},
            "fact_source_anchor_linkage_complete": {"type": "boolean"},
            "critical_findings": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
                "maxItems": 100,
            },
            "material_fact_omission_count": {"type": "integer", "minimum": 0},
            "counterfact_omission_count": {"type": "integer", "minimum": 0},
            "subject_or_segment_mismatch_count": {"type": "integer", "minimum": 0},
            "currentness_failure_count": {"type": "integer", "minimum": 0},
            "source_quality_failure_count": {"type": "integer", "minimum": 0},
            "component_calibration_failure_count": {"type": "integer", "minimum": 0},
            "historical_anchor_analogy_failure_count": {"type": "integer", "minimum": 0},
            "review_complete": {"type": "boolean"},
            "score_or_stage_authority": {"enum": [False]},
        },
    }


def _blind_projection(
    *,
    manifest: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> Mapping[str, Any]:
    components = tuple(artifacts["component_decisions.jsonl"])
    judges = tuple(artifacts["judge_decisions.jsonl"])
    score_receipt = _mapping(
        artifacts["score_receipt.json"], context="compact score receipt"
    )
    return {
        "selection_binding": {
            "selection_id": manifest["selection_id"],
            "selection_roster_hash": manifest["selection_roster_hash"],
            "target_id": manifest["target_id"],
            "archetype_id": manifest["archetype_id"],
            "as_of_date": manifest["as_of_date"],
            "receipt_id": manifest["receipt_id"],
            "receipt_payload_hash": manifest["receipt_payload_hash"],
        },
        "components": [
            {
                "component_id": row["component_id"],
                "support_fact_ids": list(row["support_fact_ids"]),
                "counter_fact_ids": list(row["counter_fact_ids"]),
                "resolution_fact_ids": list(row["resolution_fact_ids"]),
                "anchor_ids": list(row["anchor_ids"]),
                "judge_decision_ids": list(row["judge_decision_ids"]),
            }
            for row in components
        ],
        "judges": [
            {
                "judge_decision_id": row["judge_decision_id"],
                "component_id": row["component_id"],
                "role": row["role"],
                "support_fact_ids": list(row["support_fact_ids"]),
                "counter_fact_ids": list(row["counter_fact_ids"]),
                "anchor_ids": list(row["anchor_ids"]),
                "provider_call_id": row["provider_call_id"],
                "prompt_hash": row["prompt_hash"],
                "response_hash": row["response_hash"],
            }
            for row in judges
        ],
        "facts": list(artifacts["scoring_facts.jsonl"]),
        "accepted_fact_inventory": list(score_receipt["blind_review_inventory"]),
        "sources": list(artifacts["source_manifest.jsonl"]),
        "anchors": list(artifacts["anchor_manifest.jsonl"]),
        "provider_calls": list(artifacts["provider_calls.jsonl"]),
        "score_or_stage_authority": False,
    }


def build_blind_compact_review_material(
    *,
    selection: Mapping[str, Any],
    manifest: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Validate the score lineage, then project only non-score review material."""

    validate_selection_bound_canary_artifacts(
        selection=selection,
        selection_id=str(manifest.get("selection_id") or ""),
        artifacts=artifacts,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    projection = _blind_projection(manifest=manifest, artifacts=artifacts)
    encoded = json.dumps(
        projection,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    forbidden_keys = (
        "component_score_vector",
        "component_max_vector",
        "total_score",
        "canonical_stage",
        "final_points",
        "proposed_points",
        "allowed_range",
        "classification_input",
        "canary_result",
        "production_receipt",
    )
    if any(f'"{key}"' in encoded for key in forbidden_keys):
        raise ValueError("blind review projection exposes production score or Stage")
    return {
        "schema_version": "e2r_v6_compact_blind_review_material_v1",
        "blind_artifact_hash": stable_hash(projection),
        "projection": projection,
        "score_or_stage_authority": False,
    }


def _prompt(*, slot: str, material: Mapping[str, Any]) -> str:
    payload = {
        "reviewer_slot": slot,
        "review_objective": (
            "Independently verify exact seven-component/twenty-one-judge evidence "
            "lineage and seven failure families: material-fact omission, counterfact "
            "omission, wrong subject/segment, stale currentness, weak source quality, "
            "component under/over calibration, and non-analogous historical anchors. "
            "Use the complete relative receipt inventory below. Do not infer or output "
            "a score or Stage."
        ),
        "blind_review_material": material,
    }
    return (
        "You are an independent blind E2R compact-receipt lineage reviewer.\n"
        "Return only the requested JSON object. A failed or incomplete lineage "
        "must be reported in critical_findings and must not be marked complete.\n"
        + json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    )


def ensure_blind_compact_review_requests(
    *,
    journal_root: str | Path,
    selection: Mapping[str, Any],
    manifest: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Create/read the exact A/B journal requests and report pending identities."""

    material = build_blind_compact_review_material(
        selection=selection,
        manifest=manifest,
        artifacts=artifacts,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    schema = compact_blind_review_output_schema()
    transport = CollaborationCodexSubagentTransport()
    transport.configure_journal_root(journal_root)
    rows = []
    for slot in REVIEWER_SLOTS:
        prompt = _prompt(slot=slot, material=material)
        status = "COMPLETE"
        try:
            response = transport.complete(
                prompt=prompt,
                output_schema=schema,
                schema_name=BLIND_REVIEW_OUTPUT_SCHEMA_NAME,
            )
            payload = dict(response.payload)
        except StructuredProviderUnavailable as exc:
            if not str(exc).startswith("COLLABORATION_RESPONSE_PENDING:"):
                raise
            status = "PENDING"
            payload = None
        request_id = str(transport.journal_audit().get("last_request_id") or "")
        rows.append(
            {
                "reviewer_slot": slot,
                "request_id": request_id,
                "prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                "status": status,
                "payload": payload,
            }
        )
    if len({row["request_id"] for row in rows}) != 2 or len({row["prompt_hash"] for row in rows}) != 2:
        raise ValueError("reviewer A/B requests are not distinct")
    return {
        "schema_version": "e2r_v6_compact_blind_review_request_roster_v1",
        "blind_artifact_hash": material["blind_artifact_hash"],
        "requests": rows,
        "score_or_stage_authority": False,
    }


def _validated_envelopes(
    *, journal_root: Path, request_rows: Sequence[Mapping[str, Any]]
) -> tuple[tuple[Mapping[str, Any], Mapping[str, Any]], ...]:
    result = []
    for row in request_rows:
        request_id = str(row["request_id"])
        request = validate_collaboration_request(
            _mapping(
                json.loads((journal_root / "requests" / f"{request_id}.json").read_text(encoding="utf-8")),
                context="review request",
            )
        )
        envelope = validate_collaboration_response_envelope(
            request=request,
            envelope=_mapping(
                json.loads((journal_root / "responses" / f"{request_id}.json").read_text(encoding="utf-8")),
                context="review response",
            ),
        )
        result.append((request, envelope))
    return tuple(result)


def consume_blind_compact_review_responses(
    *,
    journal_root: str | Path,
    selection: Mapping[str, Any],
    manifest: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
    """Consume two exact journal responses and construct deterministic reviews."""

    roster = ensure_blind_compact_review_requests(
        journal_root=journal_root,
        selection=selection,
        manifest=manifest,
        artifacts=artifacts,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    request_rows = tuple(_mapping(row, context="request roster row") for row in roster["requests"])
    if any(row["status"] != "COMPLETE" for row in request_rows):
        raise StructuredProviderUnavailable("COMPACT_BLIND_REVIEWS_PENDING")
    envelope_pairs = _validated_envelopes(
        journal_root=Path(journal_root), request_rows=request_rows
    )
    agent_ids = {
        str(envelope["provenance"]["agent_id"])
        for _, envelope in envelope_pairs
    }
    task_names = {
        str(envelope["provenance"]["canonical_task_name"])
        for _, envelope in envelope_pairs
    }
    if len(agent_ids) != 2 or len(task_names) != 2:
        raise ValueError("reviewer A/B agent provenance is not distinct")
    verified = validate_selection_bound_canary_artifacts(
        selection=selection,
        selection_id=str(manifest["selection_id"]),
        artifacts=artifacts,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    reviews = []
    for roster_row, (request, envelope) in zip(request_rows, envelope_pairs):
        payload = _mapping(envelope["payload"], context="blind review response payload")
        slot = str(roster_row["reviewer_slot"])
        if (
            set(payload) != _RESPONSE_KEYS
            or payload.get("schema_version") != BLIND_REVIEW_SCHEMA
            or payload.get("reviewer_slot") != slot
            or payload.get("selection_id") != manifest["selection_id"]
            or payload.get("target_id") != manifest["target_id"]
            or payload.get("archetype_id") != manifest["archetype_id"]
            or payload.get("as_of_date") != manifest["as_of_date"]
            or payload.get("blind_artifact_hash") != roster["blind_artifact_hash"]
            or payload.get("evidence_lineage_complete") is not True
            or payload.get("component_roster_complete") is not True
            or payload.get("judge_roster_complete") is not True
            or payload.get("fact_source_anchor_linkage_complete") is not True
            or any(
                isinstance(payload.get(field), bool)
                or not isinstance(payload.get(field), int)
                or payload.get(field) != 0
                for field in (
                    "material_fact_omission_count",
                    "counterfact_omission_count",
                    "subject_or_segment_mismatch_count",
                    "currentness_failure_count",
                    "source_quality_failure_count",
                    "component_calibration_failure_count",
                    "historical_anchor_analogy_failure_count",
                )
            )
            or payload.get("critical_findings") != []
            or payload.get("review_complete") is not True
            or payload.get("score_or_stage_authority") is not False
        ):
            raise ValueError("blind compact review response is incomplete or mismatched")
        # The task name proves that two distinct agents performed the reviews,
        # but it is a runtime path (for example ``/root/worker_a``), not a
        # portable reviewer identity.  The tracked artifact exposes the
        # sealed slot as a stable role id; provider call and prompt/response
        # hashes retain the exact review lineage.
        reviewer_id = PORTABLE_REVIEWER_ROLE_IDS[slot]
        prompt_hash = str(request["prompt_hash"])
        response_hash = str(envelope["payload_hash"])
        identity = {
            "reviewer_id": reviewer_id,
            "provider_call_id": request["request_id"],
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
            "receipt_payload_hash": manifest["receipt_payload_hash"],
        }
        reviews.append(
            {
                "schema_version": COMPACT_REVIEW_SCHEMA,
                "status": COMPACT_REVIEW_PASS,
                "review_id": "CANREVIEW-" + stable_hash(identity)[:24],
                "reviewer_id": reviewer_id,
                "provider_name": "COLLABORATION_CODEX",
                "provider_call_id": request["request_id"],
                "prompt_hash": prompt_hash,
                "response_hash": response_hash,
                "selection_id": manifest["selection_id"],
                "selection_roster_hash": manifest["selection_roster_hash"],
                "receipt_id": manifest["receipt_id"],
                "receipt_payload_hash": manifest["receipt_payload_hash"],
                "target_id": manifest["target_id"],
                "archetype_id": manifest["archetype_id"],
                "as_of_date": manifest["as_of_date"],
                "recomputed_component_score_vector": verified["component_score_vector"],
                "recomputed_total_score": verified["total_score"],
                "recomputed_canonical_stage": verified["canonical_stage"],
                "all_eight_artifacts_verified": True,
                "full_score_lineage_verified": True,
                "independent_review": True,
                "review_complete": True,
                "critical_findings": [],
                "critical_count_sum": 0,
                "material_fact_omission_count": 0,
                "counterfact_omission_count": 0,
                "subject_or_segment_mismatch_count": 0,
                "currentness_failure_count": 0,
                "source_quality_failure_count": 0,
                "component_calibration_failure_count": 0,
                "historical_anchor_analogy_failure_count": 0,
                "score_or_stage_authority": False,
            }
        )
    validate_selection_bound_canary_bundle(
        selection=selection,
        manifest=manifest,
        artifacts=artifacts,
        reviews=reviews,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    return reviews[0], reviews[1]


__all__ = [
    "BLIND_REVIEW_SCHEMA",
    "PORTABLE_REVIEWER_ROLE_IDS",
    "build_blind_compact_review_material",
    "compact_blind_review_output_schema",
    "consume_blind_compact_review_responses",
    "ensure_blind_compact_review_requests",
]
