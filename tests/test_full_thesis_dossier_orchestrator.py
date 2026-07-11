from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.dossier import (
    DossierRunConfig,
    DossierTarget,
    FullThesisDossierOrchestrator,
    load_question_family_catalog,
)


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "configs/e2r_full_thesis_question_families_v1.json"


class FullThesisDossierOrchestratorTests(unittest.TestCase):
    def test_c06_recipe_has_twelve_semantic_families_and_no_literal_query(self) -> None:
        payload = load_question_family_catalog(CATALOG_PATH)
        families = payload["archetypes"]["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["question_families"]
        self.assertEqual(len(families), 12)
        serialized = json.dumps(payload, ensure_ascii=False).lower()
        self.assertNotIn('"query":', serialized)
        self.assertNotIn('"queries":', serialized)
        self.assertTrue(all(family["budget"]["max_fetches"] <= 20 for family in families))

    def test_arbitrary_target_uses_same_generic_twelve_family_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = self._orchestrator().initialize(
                DossierRunConfig(
                    as_of_date="2026-07-11",
                    canonical_archetype="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    output_root=tmp,
                    materialize_live_input=True,
                    live_materialization_authorized=True,
                ),
                targets=(DossierTarget("999999", "임의회사"),),
            )
            self.assertEqual(result.status, "DOSSIER_ORCHESTRATOR_INITIALIZED")
            target = result.target_results[0]
            self.assertEqual(target["question_family_count"], 12)
            self.assertEqual(target["unbounded_task_count"], 0)
            root = Path(target["output_root"])
            tasks = self._jsonl(root / "question_source_tasks.jsonl")
            closures = self._jsonl(root / "question_closure.jsonl")
            self.assertTrue(all(row["target_id"] == "999999" for row in tasks))
            self.assertTrue(all(row["suggested_queries"] == [] for row in tasks))
            self.assertEqual({row["status"] for row in closures}, {"PROVIDER_PENDING"})
            self.assertNotIn("MISSING", {row["status"] for row in closures})

    def test_live_materialization_requires_explicit_authorization(self) -> None:
        with self.assertRaisesRegex(ValueError, "explicit authorization"):
            DossierRunConfig(
                as_of_date="2026-07-11",
                canonical_archetype="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                output_root="unused",
                materialize_live_input=True,
                live_materialization_authorized=False,
            )

    def test_initializer_never_claims_score_or_readiness(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = self._orchestrator().initialize(
                DossierRunConfig(
                    as_of_date="2026-07-11",
                    canonical_archetype="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    output_root=tmp,
                ),
                targets=(DossierTarget("005930", "삼성전자"),),
            )
            audit = json.loads(
                (
                    Path(result.target_results[0]["output_root"])
                    / "audit_summary.json"
                ).read_text()
            )
            self.assertEqual(audit["status"], "DOSSIER_RESEARCH_PENDING")
            self.assertFalse(audit["readiness_eligible"])
            self.assertEqual(audit["score_type"], "NO_SCORE")
            self.assertFalse(audit["full_score_valid"])

    @staticmethod
    def _orchestrator() -> FullThesisDossierOrchestrator:
        return FullThesisDossierOrchestrator(
            question_family_catalog=load_question_family_catalog(CATALOG_PATH)
        )

    @staticmethod
    def _jsonl(path: Path):
        return [json.loads(line) for line in path.read_text().splitlines() if line]


if __name__ == "__main__":
    unittest.main()
