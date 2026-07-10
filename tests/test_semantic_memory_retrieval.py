from __future__ import annotations

import io
import json
import re
import tempfile
import unittest
from contextlib import redirect_stdout
from dataclasses import replace
from pathlib import Path

from e2r.cli.compile_e2r_research_intelligence import main as compile_cli_main
from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
)
from e2r.research_brain.intelligence_schema import (
    BalancedMemoryRole,
    BalancedRetrievalRequest,
    HistoricalEvidenceReference,
    HistoricalSourceState,
    MemoryEdgeType,
    MemoryNodeType,
)
from e2r.research_brain.recipes import compile_evidence_recipe_os
from e2r.research_brain.retrieval import (
    compile_semantic_memory_graph,
    evaluate_balanced_retrieval,
    load_blind_retrieval_benchmark,
    retrieve_balanced_memory,
    write_balanced_retrieval_benchmark,
    write_semantic_memory_graph,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURES = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"
SOURCE_FIXTURES = (
    REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "source_verification"
)
OUTCOME_TOKEN_RE = re.compile(
    r"(?:^|[^a-z0-9])(?:mfe|mae|future[_ -]?outcome|outcome[_ -]?label)(?:$|[^a-z0-9])",
    re.IGNORECASE,
)


class SemanticMemoryRetrievalTest(unittest.TestCase):
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
        cls.all_cases = (*mandatory.cases, *source_cases.cases)
        cls.source_result = compile_case_level_source_verification(
            cls.all_cases,
            snapshots=load_historical_provider_snapshots(
                SOURCE_FIXTURES / "provider_snapshots.jsonl"
            ),
            case_source_links=load_historical_case_source_links(
                SOURCE_FIXTURES / "case_source_links.jsonl"
            ),
            repo_root=REPO_ROOT,
        )
        cls.recipe_result = compile_evidence_recipe_os(
            cls.all_cases,
            source_verifications=cls.source_result.verifications,
        )
        cls.memory_result = compile_semantic_memory_graph(
            cls.all_cases,
            cls.recipe_result.recipes,
            source_verifications=cls.source_result.verifications,
        )
        cls.benchmark = load_blind_retrieval_benchmark()
        cls.retrieval_audit = evaluate_balanced_retrieval(
            cls.memory_result.index,
            cls.benchmark,
        )

    def test_graph_has_every_required_node_and_edge_type(self) -> None:
        graph = self.memory_result.graph
        self.assertEqual(
            {node.node_type for node in graph.nodes},
            {item.value for item in MemoryNodeType},
        )
        self.assertEqual(
            {edge.edge_type for edge in graph.edges},
            {item.value for item in MemoryEdgeType},
        )
        self.assertEqual(len({node.node_id for node in graph.nodes}), len(graph.nodes))
        self.assertEqual(len({edge.edge_id for edge in graph.edges}), len(graph.edges))
        node_ids = {node.node_id for node in graph.nodes}
        self.assertTrue(
            all(
                edge.source_node_id in node_ids and edge.target_node_id in node_ids
                for edge in graph.edges
            )
        )
        self.assertEqual(self.memory_result.manifest["critical_count_sum"], 0)

    def test_graph_preserves_all_canonical_identity_layers(self) -> None:
        counts = self.memory_result.manifest["node_count_by_type"]
        self.assertEqual(counts[MemoryNodeType.ARCHETYPE.value], 36)
        self.assertEqual(counts[MemoryNodeType.PRIMITIVE.value], 189)
        self.assertEqual(counts[MemoryNodeType.RECIPE.value], 31)
        self.assertEqual(counts[MemoryNodeType.CASE.value], len(self.all_cases))
        self.assertEqual(
            counts[MemoryNodeType.SOURCE.value],
            len(self.source_result.verifications),
        )
        self.assertGreater(counts[MemoryNodeType.HARD_BREAK.value], 0)

    def test_every_recipe_has_a_complete_balanced_memory_bundle(self) -> None:
        roles_by_recipe: dict[str, set[str]] = {}
        for node in self.memory_result.graph.nodes:
            if node.recipe_id and node.role_slot:
                roles_by_recipe.setdefault(node.recipe_id, set()).add(node.role_slot)
        expected = {
            BalancedMemoryRole.DIRECT_RECIPE.value,
            BalancedMemoryRole.POSITIVE.value,
            BalancedMemoryRole.COUNTEREXAMPLE_GUARD.value,
            BalancedMemoryRole.SOURCE_SUCCESS.value,
            BalancedMemoryRole.SOURCE_FAILURE.value,
            BalancedMemoryRole.SEMANTIC_GUARD.value,
        }
        for recipe in self.recipe_result.recipes:
            self.assertEqual(roles_by_recipe[recipe.recipe_id], expected, recipe.recipe_id)

    def test_verified_source_success_wrong_subject_and_failure_are_distinct_edges(self) -> None:
        graph = self.memory_result.graph
        node_by_verification = {
            node.source_verification_id: node
            for node in graph.nodes
            if node.source_verification_id
        }
        edges_by_source = {}
        for edge in graph.edges:
            edges_by_source.setdefault(edge.source_node_id, set()).add(edge.edge_type)
            edges_by_source.setdefault(edge.target_node_id, set()).add(edge.edge_type)

        ready = next(
            row
            for row in self.source_result.verifications
            if row.historical_replay_ready
        )
        wrong_subject = next(
            row
            for row in self.source_result.verifications
            if row.source_state
            == HistoricalSourceState.URL_FETCHED_WRONG_SUBJECT.value
        )
        proxy = next(
            row
            for row in self.source_result.verifications
            if row.source_state == HistoricalSourceState.SOURCE_PROXY_ONLY.value
        )
        self.assertIn(
            MemoryEdgeType.SUPPORTS.value,
            edges_by_source[node_by_verification[ready.verification_id].node_id],
        )
        self.assertIn(
            MemoryEdgeType.WRONG_SUBJECT_EXAMPLE.value,
            edges_by_source[node_by_verification[wrong_subject.verification_id].node_id],
        )
        self.assertIn(
            MemoryEdgeType.FAILED_IN.value,
            edges_by_source[node_by_verification[proxy.verification_id].node_id],
        )

    def test_planner_visible_graph_and_index_hide_historical_outcomes(self) -> None:
        visible_nodes = [
            node.to_dict()
            for node in self.memory_result.graph.nodes
            if node.planner_visible
        ]
        visible_index = [
            row.to_dict()
            for row in self.memory_result.index.entries
            if row.planner_visible
        ]
        self.assertIsNone(
            OUTCOME_TOKEN_RE.search(
                json.dumps(visible_nodes, ensure_ascii=False, sort_keys=True)
            )
        )
        self.assertIsNone(
            OUTCOME_TOKEN_RE.search(
                json.dumps(visible_index, ensure_ascii=False, sort_keys=True)
            )
        )
        hidden_archetypes = {
            node.archetype_id
            for node in self.memory_result.graph.nodes
            if not node.planner_visible and node.archetype_id
        }
        self.assertIn("R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", hidden_archetypes)
        self.assertEqual(
            self.memory_result.manifest["historical_outcomes_compiled_into_graph"],
            0,
        )

    def test_blind_benchmark_exceeds_every_phase5_threshold(self) -> None:
        manifest = self.retrieval_audit.manifest
        self.assertEqual(manifest["status"], "BALANCED_SEMANTIC_RETRIEVAL_PASS")
        self.assertEqual(manifest["benchmark_count"], 61)
        self.assertEqual(manifest["registry_archetype_coverage_count"], 36)
        self.assertEqual(manifest["archetype_benchmark_count"], 60)
        self.assertEqual(manifest["recipe_benchmark_count"], 31)
        self.assertGreaterEqual(manifest["top3_archetype_hit_rate"], 0.95)
        self.assertGreaterEqual(manifest["required_recipe_hit_rate"], 0.95)
        self.assertGreaterEqual(manifest["positive_guard_pair_rate"], 0.90)
        self.assertEqual(manifest["future_leakage_count"], 0)
        self.assertEqual(manifest["first_n_only_retrieval_count"], 0)
        self.assertEqual(manifest["popularity_bias_critical_count"], 0)
        self.assertTrue(all(row["input_order_invariant"] for row in self.retrieval_audit.rows))
        self.assertTrue(all(row["popularity_invariant"] for row in self.retrieval_audit.rows))
        self.assertTrue(
            all(
                not row["planner_payload_contains_expected_label"]
                for row in self.retrieval_audit.rows
            )
        )

    def test_expected_labels_never_enter_request_and_each_recipe_is_balanced(self) -> None:
        benchmark_case = self.benchmark[0]
        request = benchmark_case.to_request()
        request_payload = request.to_dict()
        self.assertNotIn("expected_archetype_id", request_payload)
        self.assertNotIn("expected_primitive_id", request_payload)
        result = retrieve_balanced_memory(self.memory_result.index, request)
        for recipe_id in result.direct_recipe_ids:
            roles = {
                item.role_slot for item in result.items if item.recipe_id == recipe_id
            }
            self.assertTrue(
                {
                    BalancedMemoryRole.DIRECT_RECIPE.value,
                    BalancedMemoryRole.POSITIVE.value,
                    BalancedMemoryRole.COUNTEREXAMPLE_GUARD.value,
                    BalancedMemoryRole.SOURCE_SUCCESS.value,
                    BalancedMemoryRole.SOURCE_FAILURE.value,
                    BalancedMemoryRole.SEMANTIC_GUARD.value,
                }
                <= roles
            )

    def test_point_in_time_filter_excludes_future_case_memory(self) -> None:
        base = next(
            case
            for case in self.all_cases
            if case.canonical_archetype_id == "C15_MATERIAL_SPREAD_SUPERCYCLE"
        )
        summary = (
            "Blast furnace utilization and steel shipments improved after maintenance "
            "while customer orders absorbed output."
        )
        past = replace(
            base,
            case_id="PHASE5_PIT_PAST_CASE",
            trigger_date="2020-01-01",
            entry_date="2020-01-01",
            evidence_references=(HistoricalEvidenceReference(summary=summary),),
        )
        future = replace(
            base,
            case_id="PHASE5_PIT_FUTURE_CASE",
            trigger_date="2030-01-01",
            entry_date="2030-01-01",
            evidence_references=(HistoricalEvidenceReference(summary=summary),),
        )
        memory = compile_semantic_memory_graph(
            (*self.all_cases, past, future),
            self.recipe_result.recipes,
            source_verifications=self.source_result.verifications,
        )
        result = retrieve_balanced_memory(
            memory.index,
            BalancedRetrievalRequest(
                request_id="PIT_FILTER_TEST",
                current_evidence_text=summary,
                as_of_date="2025-01-01",
                candidate_archetype_ids=("C15_MATERIAL_SPREAD_SUPERCYCLE",),
                top_k_archetypes=1,
                max_recipe_hits=1,
            ),
        )
        node_by_id = {node.node_id: node for node in memory.graph.nodes}
        returned_case_ids = {
            node_by_id[item.node_id].case_id
            for item in result.items
            if item.role_slot == BalancedMemoryRole.CONTEXT_CASE.value
        }
        self.assertIn("PHASE5_PIT_PAST_CASE", returned_case_ids)
        self.assertNotIn("PHASE5_PIT_FUTURE_CASE", returned_case_ids)

    def test_case_search_text_does_not_route_by_historical_company_name(self) -> None:
        case_nodes = [
            node
            for node in self.memory_result.graph.nodes
            if node.node_type == MemoryNodeType.CASE.value
        ]
        serialized = json.dumps(
            [
                {"search_text": node.search_text, "planner_payload": node.planner_payload}
                for node in case_nodes
            ],
            ensure_ascii=False,
        )
        for company_name in ("SK하이닉스", "리노공업", "셀트리온", "안랩"):
            self.assertNotIn(company_name, serialized)

    def test_writers_and_official_cli_emit_phase5_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            memory_paths = write_semantic_memory_graph(
                self.memory_result,
                output_root=tmp,
            )
            benchmark_paths = write_balanced_retrieval_benchmark(
                self.retrieval_audit,
                output_root=tmp,
            )
            self.assertTrue(all(path.is_file() for path in memory_paths.values()))
            self.assertTrue(all(path.is_file() for path in benchmark_paths.values()))

            cli_root = Path(tmp) / "cli"
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = compile_cli_main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--input",
                        str(CORPUS_FIXTURES / "golden_mandatory_cases.md"),
                        "--output-root",
                        str(cli_root),
                        "--strict",
                        "true",
                    ]
                )
            payload = json.loads(stdout.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(
                payload["semantic_memory_status"],
                "SEMANTIC_MEMORY_GRAPH_COMPILER_PASS",
            )
            self.assertEqual(
                payload["balanced_retrieval_status"],
                "BALANCED_SEMANTIC_RETRIEVAL_PASS",
            )
            self.assertTrue(
                (cli_root / "retrieval" / "semantic_memory_manifest.json").is_file()
            )
            self.assertTrue(
                (cli_root / "retrieval" / "balanced_retrieval_acceptance.json").is_file()
            )


if __name__ == "__main__":
    unittest.main()
