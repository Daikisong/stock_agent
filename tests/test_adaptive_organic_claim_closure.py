from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from e2r.research_brain.dossier import (
    DossierRunConfig,
    DossierTarget,
    FullThesisDossierOrchestrator,
    load_question_family_catalog,
    next_action_for_failure,
    run_organic_claim_closure,
)


ROOT = Path(__file__).resolve().parents[1]


class AdaptiveOrganicClaimClosureTests(unittest.TestCase):
    def test_failure_actions_change_by_failure_class_without_query_template(self) -> None:
        self.assertNotEqual(
            next_action_for_failure("STALE_ONLY"),
            next_action_for_failure("REROUTED_PRIMITIVE"),
        )
        self.assertNotIn("HBM", next_action_for_failure("PROVIDER_FAILED"))

    def test_source_backed_claim_is_written_as_organic_with_target_isolation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = base / "source"
            output = base / "output" / "123456"
            source.mkdir()
            target = DossierTarget("123456", "임의회사")
            catalog = load_question_family_catalog(
                ROOT / "configs/e2r_full_thesis_question_families_v1.json"
            )
            FullThesisDossierOrchestrator(
                question_family_catalog=catalog
            ).initialize(
                DossierRunConfig(
                    as_of_date="2026-07-11",
                    canonical_archetype="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    output_root=output,
                ),
                targets=(target,),
            )
            document = self._document()
            self._jsonl(source / "claim_selected_documents.jsonl", [document])
            self._jsonl(
                source / "question_source_tasks.jsonl",
                [
                    {
                        "task_id": "OLD-TASK",
                        "target_id": "123456",
                        "company_name": "임의회사",
                        "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "primitive_id": "shipment_or_revenue_mix",
                    }
                ],
            )
            self._jsonl(source / "provider_fetch_results.jsonl", [])
            self._jsonl(source / "web_search_results.jsonl", [])
            result = run_organic_claim_closure(
                target=target,
                as_of_date="2026-07-11",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                source_root=(source,),
                output_root=output,
                compiler=_FakeCompiler(),
            )
            self.assertEqual(result.status, "ORGANIC_CLAIM_CLOSURE_PASS")
            claims = self._read_jsonl(output / "accepted_current_claims.jsonl")
            self.assertEqual(claims[0]["target_id"], "123456")
            self.assertEqual(claims[0]["evidence_origin"], "ORGANIC_LIVE")
            self.assertTrue(claims[0]["fetched"])
            self.assertFalse(claims[0]["source_proxy_only"])
            self.assertTrue((output / "query_change_log.jsonl").is_file())
            self.assertTrue((output / "component_delta_log.jsonl").is_file())

    @staticmethod
    def _document():
        text = "임의회사는 HBM 제품을 양산하고 상업 출하했다."
        content_hash = hashlib.sha256(text.encode()).hexdigest()
        return {
            "document_id": "DOC-1",
            "target_id": "123456",
            "source_task_ids": ["OLD-TASK"],
            "acquisition_class": "ACTUAL_LIVE_FULL_DOCUMENT",
            "canonical_url": "https://issuer.example/document",
            "published_at": "2026-07-10",
            "available_at": "2026-07-10",
            "fetched_at": "2026-07-10T10:00:00Z",
            "content_text": text,
            "content_hash": content_hash,
        }

    @staticmethod
    def _jsonl(path: Path, rows):
        path.write_text("".join(json.dumps(row) + "\n" for row in rows))

    @staticmethod
    def _read_jsonl(path: Path):
        return [json.loads(line) for line in path.read_text().splitlines() if line]


class _FakeProvenance:
    def to_dict(self):
        return {
            "claim_id": "CLM-1",
            "target_id": "123456",
            "fetched": True,
            "source_proxy_only": False,
            "source_url": "https://issuer.example/document",
            "published_date": "2026-07-10",
            "content_sha256": "a" * 64,
            "exact_quote": "임의회사는 HBM 제품을 양산하고 상업 출하했다.",
            "mapping_ids": ["MAP-1"],
        }


class _FakeCompiler:
    def compile(self, *args, **kwargs):
        return SimpleNamespace(
            evidence_anchors=(),
            raw_assertions=({"raw_assertion_id": "RA-1"},),
            adjudicated_claims=({"claim_id": "CLM-1"},),
            primitive_mappings=(
                {
                    "mapping_id": "MAP-1",
                    "claim_id": "CLM-1",
                    "primitive_id": "shipment_or_revenue_mix",
                    "support_direction": "SUPPORT",
                    "accepted_by_evidence_os": True,
                },
            ),
            accepted_current_claims=(
                {
                    "claim_id": "CLM-1",
                    "target_id": "123456",
                    "mapping_ids": ["MAP-1"],
                    "accepted": True,
                },
            ),
            daily_claim_provenance=(_FakeProvenance(),),
            source_task_satisfaction=(),
            compilation_pending=(),
            audit={"critical_count_sum": 0},
        )


if __name__ == "__main__":
    unittest.main()
