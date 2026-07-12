from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.researcher_mode import (
    QUESTION_AUTHORITY_PASS,
    audit_research_question_seed_authority,
    load_research_question_seed_catalog,
)
from e2r.research_brain.scoring.question_impact_contract import (
    compile_question_closures_v2,
    load_question_impact_contracts,
)


class E2RV5QuestionSeedAuthorityTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_legacy_contracts_and_new_seeds_have_no_score_or_stage_authority(self) -> None:
        path = self.ROOT / "configs/e2r_question_impact_contracts_v1.json"
        contracts = load_question_impact_contracts(path)
        catalog = load_research_question_seed_catalog(path)
        self.assertEqual(len(contracts), len(catalog.seeds))
        for row in (*contracts.values(), *catalog.seeds):
            self.assertFalse(row.production_score_authority)
            self.assertFalse(row.component_completion_authority)
            self.assertFalse(row.absence_authority)
            self.assertFalse(row.final_stage_authority)

    def test_catalog_exposes_hints_but_no_claim_closure_method(self) -> None:
        catalog = load_research_question_seed_catalog(
            self.ROOT / "configs/e2r_question_impact_contracts_v1.json"
        )
        seed = catalog.seeds[0]
        self.assertTrue(seed.retrieval_keyword_hints)
        self.assertTrue(seed.source_route_hints)
        self.assertTrue(seed.false_positive_guard_hints)
        self.assertFalse(hasattr(catalog, "compile_closures"))
        self.assertFalse(hasattr(catalog, "evaluate_absence"))
        self.assertFalse(hasattr(catalog, "score"))

    def test_legacy_closure_row_explicitly_declares_compatibility_only(self) -> None:
        contract = load_question_impact_contracts(
            self.ROOT / "configs/e2r_question_impact_contracts_v1.json"
        )["shipment_mass_production_generation"]
        row = compile_question_closures_v2(
            contracts={contract.question_family_id: contract},
            claims=[],
            primitive_mappings=[],
            eligibility_decisions=[],
        )[0]
        self.assertTrue(row["compatibility_adapter"])
        self.assertFalse(row["production_score_authority"])
        self.assertFalse(row["component_completion_authority"])
        self.assertFalse(row["absence_authority"])
        self.assertFalse(row["final_stage_authority"])

    def test_canonical_researcher_namespace_never_calls_question_closure(self) -> None:
        audit = audit_research_question_seed_authority(repo_root=self.ROOT)
        self.assertEqual(audit["status"], QUESTION_AUTHORITY_PASS)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(audit["future_namespace_question_closure_imports"], [])
        self.assertEqual(audit["future_namespace_question_closure_calls"], [])

    def test_operational_authority_audit_is_committed_pass(self) -> None:
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_question_seed_authority_audit.json"
            ).read_text(encoding="utf-8")
        )
        actual = audit_research_question_seed_authority(repo_root=self.ROOT)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["status"], QUESTION_AUTHORITY_PASS)


if __name__ == "__main__":
    unittest.main()
