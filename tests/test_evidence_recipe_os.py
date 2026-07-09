from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.cli.compile_e2r_research_intelligence import main as compile_cli_main
from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
)
from e2r.research_brain.recipes import (
    compile_evidence_recipe_os,
    load_evidence_recipe_semantics,
    write_evidence_recipe_os,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURES = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"
SOURCE_FIXTURES = (
    REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "source_verification"
)


class EvidenceRecipeOSTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mandatory = compile_research_intelligence(
            [CORPUS_FIXTURES / "golden_mandatory_cases.md"],
            repo_root=REPO_ROOT,
        )
        source_cases = compile_research_intelligence(
            [SOURCE_FIXTURES / "golden_source_cases.jsonl"],
            repo_root=REPO_ROOT,
        )
        cls.mandatory_cases = mandatory.cases
        cls.all_cases = (*mandatory.cases, *source_cases.cases)
        snapshots = load_historical_provider_snapshots(
            SOURCE_FIXTURES / "provider_snapshots.jsonl"
        )
        links = load_historical_case_source_links(
            SOURCE_FIXTURES / "case_source_links.jsonl"
        )
        cls.source_result = compile_case_level_source_verification(
            cls.all_cases,
            snapshots=snapshots,
            case_source_links=links,
            repo_root=REPO_ROOT,
        )
        by_archetype = {
            case.canonical_archetype_id: case.case_id for case in mandatory.cases
        }
        cls.url_case_ids = {
            by_archetype["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
            by_archetype["C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"],
            by_archetype["C15_MATERIAL_SPREAD_SUPERCYCLE"],
        }
        cls.proxy_case_ids = {
            by_archetype["C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"],
            by_archetype["C24_BIO_TRIAL_DATA_EVENT_RISK"],
            by_archetype["C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"],
        }
        cls.result = compile_evidence_recipe_os(
            cls.all_cases,
            source_verifications=cls.source_result.verifications,
            required_url_backed_case_ids=cls.url_case_ids,
            required_source_proxy_case_ids=cls.proxy_case_ids,
        )

    def test_every_contract_pair_has_recipe_or_exact_unsupported_reason(self) -> None:
        contracts = load_evidence_contracts_v2(require_all_archetypes=True)
        required_pairs = {
            (archetype_id, primitive_id)
            for archetype_id, contract in contracts.items()
            for primitive_id in contract.required_primitives
        }
        recipe_pairs = {
            (recipe.archetype_id, recipe.primitive_id) for recipe in self.result.recipes
        }
        unsupported_pairs = {
            (item.archetype_id, item.primitive_id) for item in self.result.unsupported
        }

        self.assertEqual(len(required_pairs), 189)
        self.assertEqual(len(self.result.recipes), 31)
        self.assertEqual(len(self.result.unsupported), 158)
        self.assertEqual(recipe_pairs | unsupported_pairs, required_pairs)
        self.assertFalse(recipe_pairs & unsupported_pairs)
        self.assertTrue(all(item.reason_code for item in self.result.unsupported))
        self.assertTrue(all(item.planning_only for item in self.result.unsupported))
        self.assertTrue(
            all(not item.runtime_route_available for item in self.result.unsupported)
        )

    def test_six_required_archetypes_have_detailed_executable_recipes(self) -> None:
        self.assertEqual(
            self.result.manifest["recipe_count_by_archetype"],
            {
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 6,
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": 5,
                "C15_MATERIAL_SPREAD_SUPERCYCLE": 5,
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 5,
                "C24_BIO_TRIAL_DATA_EVENT_RISK": 5,
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION": 5,
            },
        )
        for recipe in self.result.recipes:
            self.assertTrue(recipe.executable)
            self.assertFalse(recipe.runtime_score_eligible)
            self.assertFalse(recipe.literal_queries)
            self.assertTrue(recipe.economic_mechanism)
            self.assertTrue(recipe.question_to_answer)
            self.assertTrue(recipe.accepted_claim_predicates)
            self.assertTrue(recipe.required_entities)
            self.assertTrue(recipe.required_values)
            self.assertTrue(recipe.required_units)
            self.assertTrue(recipe.required_time_scope)
            self.assertTrue(recipe.required_current_lifecycle)
            self.assertTrue(recipe.preferred_source_families)
            self.assertTrue(recipe.preferred_document_types)
            self.assertTrue(recipe.preferred_sections)
            self.assertTrue(recipe.discovery_sources)
            self.assertTrue(recipe.forbidden_score_sources)
            self.assertTrue(recipe.positive_examples)
            self.assertTrue(recipe.counterexamples)
            self.assertTrue(recipe.wrong_subject_examples)
            self.assertTrue(recipe.source_success_examples)
            self.assertTrue(recipe.source_failure_examples)
            self.assertTrue(recipe.rejection_conditions)
            self.assertTrue(recipe.counter_questions)
            self.assertTrue(recipe.supersession_questions)
            self.assertTrue(recipe.query_intent_constraints)
            self.assertTrue(recipe.stop_conditions)
            self.assertTrue(recipe.source_exhaustion_conditions)
            self.assertTrue(recipe.supporting_case_ids)

    def test_recipe_roles_and_semantics_preserve_positive_and_guard_logic(self) -> None:
        by_pair = {
            (recipe.archetype_id, recipe.primitive_id): recipe
            for recipe in self.result.recipes
        }
        c06 = by_pair[
            ("C06_HBM_MEMORY_CUSTOMER_CAPACITY", "customer_preorder_or_allocation")
        ]
        self.assertEqual(c06.role, "POSITIVE")
        self.assertIn("customer", c06.question_to_answer.lower())
        self.assertIn("allocation", c06.question_to_answer.lower())
        self.assertTrue(any("cancell" in question.lower() for question in c06.counter_questions))

        c17_guard = by_pair[
            ("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_material_cost_risk")
        ]
        self.assertEqual(c17_guard.role, "GUARD")
        self.assertIn("margin", c17_guard.question_to_answer.lower())

        c24_break = by_pair[
            ("C24_BIO_TRIAL_DATA_EVENT_RISK", "binary_event_unresolved")
        ]
        self.assertEqual(c24_break.role, "HARD_BREAK")
        self.assertTrue(c24_break.required_current_lifecycle)

    def test_verified_sources_and_source_proxy_cases_keep_separate_roles(self) -> None:
        c15_recipes = [
            recipe
            for recipe in self.result.recipes
            if recipe.archetype_id == "C15_MATERIAL_SPREAD_SUPERCYCLE"
        ]
        self.assertTrue(
            all(recipe.supporting_source_verification_ids for recipe in c15_recipes)
        )
        self.assertTrue(
            any(
                "PHASE3_C15_HYUNDAI_READY" in recipe.supporting_case_ids
                for recipe in c15_recipes
            )
        )

        for case_id in self.proxy_case_ids:
            self.assertTrue(
                any(
                    case_id in recipe.planning_only_source_proxy_case_ids
                    for recipe in self.result.recipes
                ),
                case_id,
            )
        self.assertEqual(
            self.result.manifest["critical_counts"][
                "source_proxy_example_not_planning_only"
            ],
            0,
        )

    def test_no_generic_query_or_primitive_substring_routing(self) -> None:
        compiler_path = (
            REPO_ROOT
            / "src"
            / "e2r"
            / "research_brain"
            / "recipes"
            / "evidence_recipe_compiler.py"
        )
        source = compiler_path.read_text(encoding="utf-8")
        self.assertIn(
            'RECIPE_ROUTING_STRATEGY = "EXACT_ARCHETYPE_PRIMITIVE_SEMANTIC_DEFINITION_LOOKUP"',
            source,
        )
        self.assertNotIn("primitive_id.lower", source)
        self.assertNotIn("primitive_id.startswith", source)
        self.assertNotIn("literal_queries=(primitive_id", source)
        self.assertEqual(
            self.result.manifest["critical_counts"]["generic_query_only_recipe"],
            0,
        )
        self.assertEqual(
            self.result.manifest["critical_counts"][
                "primitive_substring_production_routing"
            ],
            0,
        )
        self.assertEqual(
            self.result.manifest["critical_counts"]["literal_query_in_recipe"],
            0,
        )

    def test_semantic_registry_matches_exact_required_pairs(self) -> None:
        semantics = load_evidence_recipe_semantics()
        definitions = semantics["primitive_definitions"]
        self.assertEqual(len(semantics["profiles"]), 6)
        self.assertEqual(len(definitions), 31)
        self.assertEqual(
            len(
                {
                    (row["archetype_id"], row["primitive_id"])
                    for row in definitions
                }
            ),
            31,
        )

    def test_manifest_and_writer_are_honest_about_partial_executable_coverage(self) -> None:
        manifest = self.result.manifest
        self.assertEqual(manifest["status"], "EVIDENCE_RECIPE_OS_COMPILER_PASS")
        self.assertEqual(manifest["pair_coverage_rate"], 1.0)
        self.assertEqual(manifest["executable_recipe_coverage_rate"], 0.164021)
        self.assertFalse(manifest["production_runtime_ready"])
        self.assertEqual(manifest["critical_count_sum"], 0)

        with tempfile.TemporaryDirectory() as tmp:
            paths = write_evidence_recipe_os(self.result, output_root=tmp)
            self.assertTrue(paths["recipes"].is_file())
            self.assertTrue(paths["unsupported"].is_file())
            self.assertTrue(paths["manifest"].is_file())
            self.assertEqual(
                len(paths["recipes"].read_text(encoding="utf-8").splitlines()),
                31,
            )

    def test_official_compile_cli_emits_recipe_os_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "compile"
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = compile_cli_main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--input",
                        str(CORPUS_FIXTURES / "golden_mandatory_cases.md"),
                        "--output-root",
                        str(output),
                        "--strict",
                        "true",
                    ]
                )
            payload = json.loads(stdout.getvalue())

            self.assertEqual(exit_code, 0)
            self.assertEqual(
                payload["evidence_recipe_status"],
                "EVIDENCE_RECIPE_OS_COMPILER_PASS",
            )
            self.assertEqual(payload["executable_recipe_count"], 31)
            self.assertEqual(payload["explicit_unsupported_recipe_count"], 158)
            self.assertTrue(
                (output / "recipes" / "evidence_recipe_manifest.json").is_file()
            )


if __name__ == "__main__":
    unittest.main()
