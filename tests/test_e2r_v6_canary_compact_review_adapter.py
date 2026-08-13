from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from e2r.production.v6_canary_compact_review_adapter import (
    BLIND_REVIEW_SCHEMA,
    build_blind_compact_review_material,
    consume_blind_compact_review_responses,
    ensure_blind_compact_review_requests,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    COLLABORATION_PROVENANCE_ASSURANCE,
    COLLABORATION_RESPONSE_SCHEMA_VERSION,
    _canonical_hash,
)
from tests.test_e2r_v6_canary_compact_receipt import REPO_ROOT, _bundle


def _write_response(
    journal: Path,
    *,
    request_id: str,
    slot: str,
    blind_artifact_hash: str,
    manifest: dict[str, object],
    agent_id: str,
    task_name: str,
    material_fact_omission_count: int = 0,
) -> None:
    request = json.loads(
        (journal / "requests" / f"{request_id}.json").read_text(encoding="utf-8")
    )
    payload = {
        "schema_version": BLIND_REVIEW_SCHEMA,
        "reviewer_slot": slot,
        "selection_id": manifest["selection_id"],
        "target_id": manifest["target_id"],
        "archetype_id": manifest["archetype_id"],
        "as_of_date": manifest["as_of_date"],
        "blind_artifact_hash": blind_artifact_hash,
        "evidence_lineage_complete": True,
        "component_roster_complete": True,
        "judge_roster_complete": True,
        "fact_source_anchor_linkage_complete": True,
        "critical_findings": (
            [] if material_fact_omission_count == 0 else ["material fact omitted"]
        ),
        "material_fact_omission_count": material_fact_omission_count,
        "counterfact_omission_count": 0,
        "subject_or_segment_mismatch_count": 0,
        "currentness_failure_count": 0,
        "source_quality_failure_count": 0,
        "component_calibration_failure_count": 0,
        "historical_anchor_analogy_failure_count": 0,
        "review_complete": material_fact_omission_count == 0,
        "score_or_stage_authority": False,
    }
    provenance = {
        "agent_id": agent_id,
        "canonical_task_name": task_name,
        "agent_model": "codex-test",
        "agent_surface": "CODEX_COLLABORATION_SUBAGENT",
        "provenance_assurance": COLLABORATION_PROVENANCE_ASSURANCE,
    }
    payload_hash = _canonical_hash(payload)
    response_id = "COLLABRESP-" + _canonical_hash(
        {
            "request_id": request_id,
            "payload_hash": payload_hash,
            "provenance": provenance,
        }
    )
    envelope = {
        "schema_version": COLLABORATION_RESPONSE_SCHEMA_VERSION,
        "response_id": response_id,
        "request_id": request_id,
        "prompt_hash": request["prompt_hash"],
        "output_schema_hash": request["output_schema_hash"],
        "provider_identity_hash": request["provider_identity_hash"],
        "payload_hash": payload_hash,
        "payload": payload,
        "provenance": provenance,
        "validation": {
            "draft202012_schema_valid": True,
            "blind_research_output_valid": True,
            "request_hashes_valid": True,
            "downstream_semantic_validation_required": True,
        },
        "score_or_stage_authority": False,
        "production_score_authority": False,
    }
    (journal / "responses" / f"{request_id}.json").write_text(
        json.dumps(envelope, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


class E2RV6CanaryCompactReviewAdapterTests(unittest.TestCase):
    def test_blind_material_and_two_requests_expose_no_score_or_stage(self) -> None:
        selection, artifacts, manifest, _ = _bundle()
        material = build_blind_compact_review_material(
            selection=selection,
            manifest=manifest,
            artifacts=artifacts,
            repo_root=REPO_ROOT,
        )
        encoded = json.dumps(material, sort_keys=True)
        for forbidden in (
            "component_score_vector",
            "total_score",
            "canonical_stage",
            "final_points",
            "proposed_points",
            "allowed_range",
        ):
            self.assertNotIn(forbidden, encoded)
        with tempfile.TemporaryDirectory() as temporary:
            roster = ensure_blind_compact_review_requests(
                journal_root=temporary,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )
            rows = roster["requests"]
            self.assertEqual([row["status"] for row in rows], ["PENDING", "PENDING"])
            self.assertEqual(len({row["request_id"] for row in rows}), 2)
            self.assertEqual(len({row["prompt_hash"] for row in rows}), 2)

    def test_distinct_validated_agents_produce_two_compact_reviews(self) -> None:
        selection, artifacts, manifest, _ = _bundle()
        with tempfile.TemporaryDirectory() as temporary:
            journal = Path(temporary)
            roster = ensure_blind_compact_review_requests(
                journal_root=journal,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )
            for index, row in enumerate(roster["requests"]):
                _write_response(
                    journal,
                    request_id=str(row["request_id"]),
                    slot=str(row["reviewer_slot"]),
                    blind_artifact_hash=str(roster["blind_artifact_hash"]),
                    manifest=manifest,
                    agent_id=f"agent-{index}",
                    task_name=f"/root/compact_reviewer_{index}",
                )
            reviews = consume_blind_compact_review_responses(
                journal_root=journal,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )
            self.assertEqual(len(reviews), 2)
            self.assertEqual(
                {row["reviewer_id"] for row in reviews},
                {
                    "CODEX_POST_RUN_REVIEWER_A",
                    "CODEX_POST_RUN_REVIEWER_B",
                },
            )
            self.assertTrue(all(row["critical_count_sum"] == 0 for row in reviews))

    def test_same_agent_provenance_is_rejected(self) -> None:
        selection, artifacts, manifest, _ = _bundle()
        with tempfile.TemporaryDirectory() as temporary:
            journal = Path(temporary)
            roster = ensure_blind_compact_review_requests(
                journal_root=journal,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )
            for row in roster["requests"]:
                _write_response(
                    journal,
                    request_id=str(row["request_id"]),
                    slot=str(row["reviewer_slot"]),
                    blind_artifact_hash=str(roster["blind_artifact_hash"]),
                    manifest=manifest,
                    agent_id="same-agent",
                    task_name="/root/same_reviewer",
                )
            with self.assertRaisesRegex(ValueError, "provenance is not distinct"):
                consume_blind_compact_review_responses(
                    journal_root=journal,
                    selection=selection,
                    manifest=manifest,
                    artifacts=artifacts,
                    repo_root=REPO_ROOT,
                )

    def test_distinct_agents_cannot_reuse_one_canonical_reviewer_task(self) -> None:
        selection, artifacts, manifest, _ = _bundle()
        with tempfile.TemporaryDirectory() as temporary:
            journal = Path(temporary)
            roster = ensure_blind_compact_review_requests(
                journal_root=journal,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )
            for index, row in enumerate(roster["requests"]):
                _write_response(
                    journal,
                    request_id=str(row["request_id"]),
                    slot=str(row["reviewer_slot"]),
                    blind_artifact_hash=str(roster["blind_artifact_hash"]),
                    manifest=manifest,
                    agent_id=f"agent-{index}",
                    task_name="/root/reused_reviewer_task",
                )
            with self.assertRaisesRegex(ValueError, "provenance is not distinct"):
                consume_blind_compact_review_responses(
                    journal_root=journal,
                    selection=selection,
                    manifest=manifest,
                    artifacts=artifacts,
                    repo_root=REPO_ROOT,
                )

    def test_nonzero_failure_family_cannot_be_projected_as_pass(self) -> None:
        selection, artifacts, manifest, _ = _bundle()
        with tempfile.TemporaryDirectory() as temporary:
            journal = Path(temporary)
            roster = ensure_blind_compact_review_requests(
                journal_root=journal,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )
            for index, row in enumerate(roster["requests"]):
                _write_response(
                    journal,
                    request_id=str(row["request_id"]),
                    slot=str(row["reviewer_slot"]),
                    blind_artifact_hash=str(roster["blind_artifact_hash"]),
                    manifest=manifest,
                    agent_id=f"agent-{index}",
                    task_name=f"/root/reviewer_{index}",
                    material_fact_omission_count=1 if index == 0 else 0,
                )
            with self.assertRaisesRegex(ValueError, "incomplete or mismatched"):
                consume_blind_compact_review_responses(
                    journal_root=journal,
                    selection=selection,
                    manifest=manifest,
                    artifacts=artifacts,
                    repo_root=REPO_ROOT,
                )


if __name__ == "__main__":
    unittest.main()
