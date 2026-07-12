from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.research_quality import (
    audit_search_adequacy,
    compile_dossier_search_adequacy,
)
from e2r.research_brain.scoring.question_impact_contract import (
    load_question_impact_contracts,
)


class AbsenceRequiresAdequateSearchTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    FIXTURE = ROOT / "tests/fixtures/semantic_scoring_v2/search_adequacy"

    def test_absence_provider_pending_and_evidence_found_are_distinct(self) -> None:
        rows = self._compile()
        by_family = {row.question_family_id: row for row in rows}
        absent = by_family["qualification_pass_lag_reopen"]
        provider = by_family["medium_term_revision_consensus"]
        found = by_family["shipment_mass_production_generation"]
        self.assertEqual(absent.saturation_status, "ADEQUATE_ABSENCE")
        self.assertTrue(absent.adequate_absence_allowed)
        self.assertEqual(provider.saturation_status, "PROVIDER_PENDING")
        self.assertFalse(provider.adequate_absence_allowed)
        self.assertEqual(found.saturation_status, "EVIDENCE_FOUND")
        self.assertFalse(found.adequate_absence_allowed)

    def test_missing_counter_route_makes_observed_absence_a_hard_failure(self) -> None:
        tasks = list(self._jsonl("executed_question_source_tasks.jsonl"))
        first = dict(tasks[0])
        first["adequacy_route_attempts"] = [
            row
            for row in first["adequacy_route_attempts"]
            if row["route_category"] != "COUNTER"
        ]
        tasks[0] = first
        rows = self._compile(executed_tasks=tasks)
        row = rows[0]
        self.assertEqual(row.saturation_status, "INADEQUATE_SEARCH")
        self.assertIn("COUNTER", row.missing_route_categories)
        audit = audit_search_adequacy(rows)
        self.assertEqual(
            audit["critical_counts"][
                "inadequate_question_closure_absence_count"
            ],
            1,
        )

    def test_budget_exhaustion_is_pending_never_absence(self) -> None:
        fetches = list(self._jsonl("provider_fetch_results.jsonl"))
        fetches[0] = {
            **fetches[0],
            "acquisition_class": "BUDGET_EXHAUSTED",
            "provider_error": None,
            "budget_exhausted": True,
        }
        rows = self._compile(provider_fetch_results=fetches)
        row = {
            item.question_family_id: item for item in rows
        }["medium_term_revision_consensus"]
        self.assertEqual(row.saturation_status, "BUDGET_PENDING")
        self.assertFalse(row.adequate_absence_allowed)

    def test_later_same_route_document_resolves_earlier_provider_failure(self) -> None:
        documents = list(self._jsonl("evidence_documents.jsonl"))
        documents.append(
            {
                "document_id": "DOC-REVISION-RECOVERY",
                "source_task_ids": ["TASK-PROVIDER"],
                "canonical_url": "https://financial.example/revision",
                "source_class": "CompanyGuide",
                "published_at": "2026-07-01",
                "content_text": "The current revision source was fetched and investigated.",
                "snippet_only": False,
            }
        )
        rows = compile_dossier_search_adequacy(
            question_tasks=self._jsonl("question_source_tasks.jsonl"),
            executed_tasks=self._jsonl("executed_question_source_tasks.jsonl"),
            provider_requests=self._jsonl("provider_requests.jsonl"),
            provider_fetch_results=self._jsonl("provider_fetch_results.jsonl"),
            web_search_tasks=self._jsonl("web_search_tasks.jsonl"),
            documents=documents,
            claims=self._jsonl("accepted_current_claims.jsonl"),
            primitive_mappings=self._jsonl("primitive_mappings.jsonl"),
            question_closures=self._jsonl("question_closure.jsonl"),
            question_contracts=load_question_impact_contracts(
                self.ROOT / "configs/e2r_question_impact_contracts_v1.json"
            ),
        )
        recovered = {
            row.question_family_id: row for row in rows
        }["medium_term_revision_consensus"]
        self.assertEqual(recovered.provider_failures, 0)
        self.assertEqual(recovered.saturation_status, "ADEQUATE_ABSENCE")
        self.assertTrue(recovered.adequate_absence_allowed)

    def test_controlled_fixture_search_adequacy_has_zero_critical(self) -> None:
        actual = audit_search_adequacy(self._compile())
        self.assertEqual(actual["critical_count_sum"], 0)

    def test_operational_audit_is_live_samsung_hynix_not_fixture(self) -> None:
        controlled = audit_search_adequacy(self._compile())
        operational = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_evidence_search_adequacy_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(operational["critical_count_sum"], 0)
        self.assertEqual(operational["question_count"], 26)
        self.assertEqual(
            {row["target_id"] for row in operational["rows"]},
            {"005930", "000660"},
        )
        self.assertEqual(operational["saturation_counts"]["PROVIDER_PENDING"], 0)
        self.assertEqual(operational["saturation_counts"]["SOURCE_PENDING"], 0)
        self.assertEqual(operational["saturation_counts"]["BUDGET_PENDING"], 0)
        self.assertNotEqual(operational, controlled)

    def _compile(self, *, executed_tasks=None, provider_fetch_results=None):
        return compile_dossier_search_adequacy(
            question_tasks=self._jsonl("question_source_tasks.jsonl"),
            executed_tasks=(
                executed_tasks
                if executed_tasks is not None
                else self._jsonl("executed_question_source_tasks.jsonl")
            ),
            provider_requests=self._jsonl("provider_requests.jsonl"),
            provider_fetch_results=(
                provider_fetch_results
                if provider_fetch_results is not None
                else self._jsonl("provider_fetch_results.jsonl")
            ),
            web_search_tasks=self._jsonl("web_search_tasks.jsonl"),
            documents=self._jsonl("evidence_documents.jsonl"),
            claims=self._jsonl("accepted_current_claims.jsonl"),
            primitive_mappings=self._jsonl("primitive_mappings.jsonl"),
            question_closures=self._jsonl("question_closure.jsonl"),
            question_contracts=load_question_impact_contracts(
                self.ROOT / "configs/e2r_question_impact_contracts_v1.json"
            ),
            claim_eligibility_decisions=self._jsonl(
                "claim_eligibility_decisions.jsonl"
            ),
            proposed_impacts=self._jsonl("claim_impacts_proposed.jsonl"),
            validated_impacts=self._jsonl("claim_impacts_validated.jsonl"),
            material_fact_comparisons=self._jsonl(
                "material_fact_comparison.jsonl"
            ),
        )

    def _jsonl(self, name: str):
        path = self.FIXTURE / name
        return tuple(
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )


if __name__ == "__main__":
    unittest.main()
