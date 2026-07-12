from __future__ import annotations

import json
import os
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
)
from e2r.research_brain.intelligence_schema import PlannerStatus
from e2r.research_brain.planning import (
    CodexStructuredProviderTransport,
    FixtureTwoPassPlannerProvider,
    build_pass_a_prompt,
    build_codex_two_pass_planner_provider,
    compile_blind_hypothesis_input,
    evaluate_two_pass_planner_benchmark,
    run_two_pass_planner,
    write_two_pass_plan,
    write_two_pass_planner_benchmark,
)
from e2r.research_brain.recipes import compile_evidence_recipe_os
from e2r.research_brain.retrieval import (
    compile_semantic_memory_graph,
    load_blind_retrieval_benchmark,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURES = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"
SOURCE_FIXTURES = (
    REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "source_verification"
)


class TwoPassBrainPlannerTest(unittest.TestCase):
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
        cases = (*mandatory.cases, *source_cases.cases)
        source_result = compile_case_level_source_verification(
            cases,
            snapshots=load_historical_provider_snapshots(
                SOURCE_FIXTURES / "provider_snapshots.jsonl"
            ),
            case_source_links=load_historical_case_source_links(
                SOURCE_FIXTURES / "case_source_links.jsonl"
            ),
            repo_root=REPO_ROOT,
        )
        recipes = compile_evidence_recipe_os(
            cases,
            source_verifications=source_result.verifications,
        )
        cls.memory = compile_semantic_memory_graph(
            cases,
            recipes.recipes,
            source_verifications=source_result.verifications,
        )
        cls.benchmark = load_blind_retrieval_benchmark()

    def _input_for_benchmark(self, benchmark_id: str):
        row = next(item for item in self.benchmark if item.benchmark_id == benchmark_id)
        return compile_blind_hypothesis_input(
            target_id="BLIND-TEST-TARGET",
            target_name="Blind target",
            target_aliases=(),
            as_of_date=row.as_of_date,
            evidence_rows=(
                {
                    "fact_id": "CURRENT-FACT-1",
                    "text": row.current_evidence,
                    "observed_date": row.as_of_date,
                    "target_relation": "DIRECT",
                    "current_status": "CURRENT",
                },
            ),
        ).blind_input

    def _provider(self, *, mutate_a=None, mutate_b=None, capture=None):
        def pass_a(payload):
            if capture is not None:
                capture.append(("A", deepcopy(payload)))
            source = payload["input"]
            fact = source["current_facts"][0]
            result = {
                "input_id": source["input_id"],
                "hypotheses": [
                    {
                        "hypothesis_id": "H1",
                        "rank": 1,
                        "mechanism_summary": fact["text"],
                        "strength": "MEDIUM",
                        "supporting_fact_ids": [fact["fact_id"]],
                        "contradicting_fact_ids": [],
                        "must_verify_questions": [
                            "Which direct current fact closes this mechanism?"
                        ],
                    }
                ],
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }
            return mutate_a(result) if mutate_a else result

        def pass_b(payload):
            if capture is not None:
                capture.append(("B", deepcopy(payload)))
            source = payload["input"]
            fact = source["current_facts"][0]
            memory = source["balanced_memory"]
            ranked = memory["ranked_archetypes"][:3]
            direct = [
                item
                for item in memory["memory_items"]
                if item["role"] == "DIRECT_RECIPE"
            ]
            hypotheses = []
            for rank, candidate in enumerate(ranked, start=1):
                recipe_ids = [
                    item["recipe_id"]
                    for item in direct
                    if item["archetype_id"] == candidate["archetype_id"]
                ][:1]
                hypotheses.append(
                    {
                        "archetype_id": candidate["archetype_id"],
                        "rank": rank,
                        "reason": "Balanced semantic memory matches current evidence.",
                        "supporting_fact_ids": [fact["fact_id"]],
                        "contradicting_fact_ids": [],
                        "recipe_ids": recipe_ids,
                    }
                )
            direct_recipe = next(
                (
                    item
                    for item in direct
                    if hypotheses and item["recipe_id"] in hypotheses[0]["recipe_ids"]
                ),
                None,
            )
            abstain = direct_recipe is None
            drafts = []
            if direct_recipe is not None:
                content = direct_recipe["content"]
                drafts.append(
                    {
                        "draft_id": "D1",
                        "recipe_id": direct_recipe["recipe_id"],
                        "question_to_answer": content["question_to_answer"],
                        "why_material": "The leading mechanism requires direct current evidence.",
                        "query_intent": (
                            "Find a target-specific authoritative fact that answers the "
                            "unresolved question."
                        ),
                        "preferred_source_families": content[
                            "preferred_source_families"
                        ],
                        "fallback_source_families": content["discovery_sources"],
                        "max_queries": 3,
                        "max_candidates": 20,
                        "max_fetches": 5,
                        "stop_condition": "Stop after a direct anchored claim and its counter check.",
                    }
                )
            result = {
                "input_id": source["input_id"],
                "top_k_archetypes": hypotheses,
                "supporting_current_fact_ids": [fact["fact_id"]],
                "contradicting_current_fact_ids": [],
                "positive_thesis": "Current facts may support the leading mechanism.",
                "counter_thesis": "Wrong subject, stale lifecycle, or missing conversion may defeat it.",
                "must_verify_questions": [
                    "Does a direct current source satisfy the reviewed question?"
                ],
                "red_team_questions": [
                    "Is the fact stale, cancelled, superseded, or about another subject?"
                ],
                "source_task_drafts": drafts,
                "do_not_promote_reasons": [
                    "Direct evidence and counter checks remain open."
                ],
                "ambiguity_reasons": (
                    ["The leading option has no reviewed executable recipe."]
                    if abstain
                    else []
                ),
                "abstain": abstain,
                "abstention_reason": (
                    "No reviewed executable recipe is available." if abstain else ""
                ),
            }
            return mutate_b(result) if mutate_b else result

        return FixtureTwoPassPlannerProvider(pass_a=pass_a, pass_b=pass_b)

    def test_blind_input_drops_future_outcome_and_preassigned_fields(self) -> None:
        compiled = compile_blind_hypothesis_input(
            target_id="T1",
            target_name="Target",
            target_aliases=(),
            as_of_date="2025-01-01",
            evidence_rows=(
                {
                    "fact_id": "F1",
                    "text": "Customer allocation is current; score=88; Stage=3-Green;",
                    "observed_date": "2024-12-31",
                    "source_primary": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "expected_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                },
                {
                    "fact_id": "F2",
                    "text": "MFE_180D_pct was high.",
                    "observed_date": "2024-12-31",
                },
                {
                    "fact_id": "F3",
                    "text": "A later report should not be visible.",
                    "observed_date": "2025-01-02",
                },
                {
                    "fact_id": "F4",
                    "text": "The source primary field was copied into this row.",
                    "observed_date": "2024-12-31",
                },
                {
                    "fact_id": "F5",
                    "text": "This row has an invalid date.",
                    "observed_date": "2024-99-99",
                },
                {
                    "fact_id": "F6",
                    "text": "The clinical program entered stage 2 enrollment.",
                    "observed_date": "2024-12-31",
                },
                {
                    "fact_id": "F7",
                    "text": "The E2R stage 2 classification was preassigned.",
                    "observed_date": "2024-12-31",
                },
            ),
        )
        payload = json.dumps(compiled.blind_input.to_dict(), ensure_ascii=False)
        self.assertEqual(len(compiled.blind_input.current_facts), 2)
        self.assertIn("clinical program entered stage 2", payload)
        self.assertNotIn("C06_HBM", payload)
        self.assertNotIn("score=", payload.lower())
        self.assertNotIn("stage=", payload.lower())
        self.assertEqual(compiled.audit["outcome_evidence_dropped_count"], 1)
        self.assertEqual(compiled.audit["future_evidence_dropped_count"], 1)
        self.assertEqual(compiled.audit["forbidden_context_evidence_dropped_count"], 2)
        self.assertEqual(compiled.audit["invalid_date_evidence_dropped_count"], 1)
        self.assertEqual(compiled.audit["source_primary_field_forwarded_count"], 0)

    def test_pass_a_prompt_contains_only_blind_current_input(self) -> None:
        blind_input = self._input_for_benchmark("BR-C06-01")
        benchmark = next(
            item for item in self.benchmark if item.benchmark_id == "BR-C06-01"
        )
        captured = []
        run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(capture=captured),
            test_mode=True,
        )
        pass_a_payload = next(payload for label, payload in captured if label == "A")
        prompt = build_pass_a_prompt(pass_a_payload)
        lower = prompt.lower()
        self.assertNotIn("source_primary", lower)
        self.assertNotIn("expected_archetype", lower)
        self.assertNotIn("canonical_archetype", lower)
        self.assertNotIn("mfe", lower)
        self.assertNotIn("mae", lower)
        self.assertNotIn("score=", lower)
        self.assertNotIn("sector_context", lower)
        self.assertNotIn(benchmark.benchmark_id.lower(), lower)
        self.assertNotIn(benchmark.expected_archetype_id.lower(), lower)
        self.assertNotIn(benchmark.expected_primitive_id.lower(), lower)

    def test_pass_b_prompt_uses_balanced_memory_without_semantic_scores(self) -> None:
        captured = []
        plan = run_two_pass_planner(
            blind_input=self._input_for_benchmark("BR-C06-01"),
            memory_index=self.memory.index,
            provider=self._provider(capture=captured),
            test_mode=True,
        )
        self.assertEqual(plan.status, PlannerStatus.COMPLETE.value)
        pass_b = next(payload for label, payload in captured if label == "B")
        serialized = json.dumps(pass_b, ensure_ascii=False, sort_keys=True).lower()
        self.assertNotIn("semantic_score", serialized)
        self.assertNotIn("source_primary", serialized)
        self.assertNotIn("mfe_", serialized)
        self.assertNotIn("mae_", serialized)
        roles = {
            item["role"]
            for item in pass_b["input"]["balanced_memory"]["memory_items"]
        }
        self.assertTrue(
            {
                "DIRECT_RECIPE",
                "POSITIVE",
                "COUNTEREXAMPLE_GUARD",
                "SOURCE_SUCCESS",
                "SOURCE_FAILURE",
                "SEMANTIC_GUARD",
            }
            <= roles
        )

    def test_full_blind_benchmark_exceeds_phase6_thresholds(self) -> None:
        audit = evaluate_two_pass_planner_benchmark(
            memory_index=self.memory.index,
            benchmark_cases=self.benchmark,
            provider=self._provider(),
            test_mode=True,
        )
        manifest = audit.manifest
        self.assertEqual(manifest["status"], "TWO_PASS_PLANNER_TEST_BENCHMARK_PASS")
        self.assertEqual(manifest["benchmark_count"], 61)
        self.assertEqual(manifest["archetype_benchmark_count"], 60)
        self.assertGreaterEqual(manifest["top3_hit_rate"], 0.95)
        self.assertGreaterEqual(manifest["top1_hit_rate"], 0.85)
        self.assertGreater(manifest["abstention_count"], 0)
        self.assertEqual(manifest["critical_guard_misroute_count"], 0)
        self.assertEqual(manifest["impossible_archetype_assignment_count"], 0)
        self.assertEqual(manifest["planner_score_stage_mutation_count"], 0)
        self.assertEqual(manifest["source_primary_copy_without_reason_count"], 0)
        self.assertEqual(manifest["prompt_response_hash_missing_count"], 0)
        self.assertEqual(
            manifest["result_hash"],
            "963912be8e09f4251e71f630168c8f702612033bb9034927e3f431f5450b18b2",
        )
        self.assertFalse(manifest["production_runtime_ready"])

    def test_unsupported_leading_archetype_abstains(self) -> None:
        plan = run_two_pass_planner(
            blind_input=self._input_for_benchmark("BR-REG-C01"),
            memory_index=self.memory.index,
            provider=self._provider(),
            test_mode=True,
        )
        self.assertEqual(plan.status, PlannerStatus.ABSTAINED.value)
        self.assertTrue(plan.critique_output.abstain)
        self.assertTrue(plan.critique_output.ambiguity_reasons)
        self.assertFalse(plan.critique_output.source_task_drafts)

    def test_provider_failure_and_missing_provider_become_pending(self) -> None:
        blind_input = self._input_for_benchmark("BR-C06-01")
        missing = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=None,
        )
        self.assertEqual(missing.status, PlannerStatus.PENDING.value)
        self.assertEqual(missing.pending.reason_code, "PLANNER_PROVIDER_NOT_CONFIGURED")
        self.assertTrue(missing.pending.prompt_hash)
        self.assertTrue(missing.pending.response_hash)

        def fail(_payload):
            raise RuntimeError("provider down")

        failed = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=FixtureTwoPassPlannerProvider(fail, fail),
            test_mode=True,
        )
        self.assertEqual(failed.status, PlannerStatus.PENDING.value)
        self.assertEqual(failed.pending.reason_code, "PROVIDER_OR_OUTPUT_ERROR")

    def test_fake_provider_is_rejected_outside_test_mode(self) -> None:
        plan = run_two_pass_planner(
            blind_input=self._input_for_benchmark("BR-C06-01"),
            memory_index=self.memory.index,
            provider=self._provider(),
            test_mode=False,
        )
        self.assertEqual(plan.status, PlannerStatus.PENDING.value)
        self.assertEqual(plan.pending.reason_code, "FAKE_PROVIDER_NOT_ALLOWED")

    def test_score_stage_source_primary_and_archetype_injection_are_pending(self) -> None:
        blind_input = self._input_for_benchmark("BR-C06-01")

        def inject_archetype(row):
            row["hypotheses"][0]["mechanism_summary"] = (
                "Use c06_hbm_memory_customer_capacity directly."
            )
            return row

        pass_a_injection = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(mutate_a=inject_archetype),
            test_mode=True,
        )
        self.assertEqual(pass_a_injection.status, PlannerStatus.PENDING.value)
        self.assertEqual(len(pass_a_injection.provider_traces), 1)
        self.assertEqual(
            pass_a_injection.pending.response_hash,
            pass_a_injection.provider_traces[-1].response_hash,
        )

        def inject_source_primary(row):
            row["top_k_archetypes"][0]["reason"] = "source_primary copied"
            return row

        pass_b_injection = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(mutate_b=inject_source_primary),
            test_mode=True,
        )
        self.assertEqual(pass_b_injection.status, PlannerStatus.PENDING.value)
        self.assertEqual(len(pass_b_injection.provider_traces), 2)
        self.assertEqual(
            pass_b_injection.pending.response_hash,
            pass_b_injection.provider_traces[-1].response_hash,
        )

        def inject_score_key(row):
            row["score"] = 99
            return row

        score_injection = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(mutate_b=inject_score_key),
            test_mode=True,
        )
        self.assertEqual(score_injection.status, PlannerStatus.PENDING.value)

    def test_decoder_rejects_json_type_coercion(self) -> None:
        blind_input = self._input_for_benchmark("BR-C06-01")

        def string_boolean(row):
            row["abstain"] = "false"
            return row

        plan = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(mutate_b=string_boolean),
            test_mode=True,
        )
        self.assertEqual(plan.status, PlannerStatus.PENDING.value)
        self.assertIn("must be a boolean", plan.pending.reason_detail)

        def string_rank(row):
            row["hypotheses"][0]["rank"] = "1"
            return row

        rank_plan = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(mutate_a=string_rank),
            test_mode=True,
        )
        self.assertEqual(rank_plan.status, PlannerStatus.PENDING.value)
        self.assertIn("must be an integer", rank_plan.pending.reason_detail)

    def test_target_and_sector_plausibility_require_abstention(self) -> None:
        benchmark = next(
            item for item in self.benchmark if item.benchmark_id == "BR-C06-01"
        )
        direct_input = self._input_for_benchmark("BR-C06-01")
        peer_only = compile_blind_hypothesis_input(
            target_id="BLIND-TEST-TARGET",
            target_name="Blind target",
            target_aliases=(),
            as_of_date=benchmark.as_of_date,
            evidence_rows=(
                {
                    "fact_id": "CURRENT-FACT-1",
                    "text": benchmark.current_evidence,
                    "observed_date": benchmark.as_of_date,
                    "target_relation": "PEER",
                    "current_status": "CURRENT",
                },
            ),
        ).blind_input
        self.assertNotEqual(peer_only.input_id, direct_input.input_id)
        peer_plan = run_two_pass_planner(
            blind_input=peer_only,
            memory_index=self.memory.index,
            provider=self._provider(),
            test_mode=True,
        )
        self.assertEqual(peer_plan.status, PlannerStatus.PENDING.value)
        self.assertIn("direct current target evidence", peer_plan.pending.reason_detail)

        wrong_sector = compile_blind_hypothesis_input(
            target_id="BLIND-TEST-TARGET",
            target_name="Blind target",
            target_aliases=(),
            as_of_date=benchmark.as_of_date,
            evidence_rows=(
                {
                    "fact_id": "CURRENT-FACT-1",
                    "text": benchmark.current_evidence,
                    "observed_date": benchmark.as_of_date,
                    "target_relation": "DIRECT",
                    "current_status": "CURRENT",
                },
            ),
            sector_context=("L99_IMPOSSIBLE_SECTOR",),
        ).blind_input
        self.assertNotEqual(wrong_sector.input_id, direct_input.input_id)
        sector_plan = run_two_pass_planner(
            blind_input=wrong_sector,
            memory_index=self.memory.index,
            provider=self._provider(),
            test_mode=True,
        )
        self.assertEqual(sector_plan.status, PlannerStatus.PENDING.value)
        self.assertIn("sector context", sector_plan.pending.reason_detail)

    def test_impossible_assignment_and_nonofficial_first_draft_are_pending(self) -> None:
        blind_input = self._input_for_benchmark("BR-C06-01")

        def impossible(row):
            row["top_k_archetypes"][0]["archetype_id"] = "C99_IMPOSSIBLE"
            return row

        impossible_plan = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(mutate_b=impossible),
            test_mode=True,
        )
        self.assertEqual(impossible_plan.status, PlannerStatus.PENDING.value)

        def naver_first(row):
            row["source_task_drafts"][0]["preferred_source_families"] = [
                "NaverSearch",
                "DART",
            ]
            return row

        bad_source_plan = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(mutate_b=naver_first),
            test_mode=True,
        )
        self.assertEqual(bad_source_plan.status, PlannerStatus.PENDING.value)

    def test_prompt_response_hashes_are_stable_and_plan_writes(self) -> None:
        blind_input = self._input_for_benchmark("BR-C06-01")
        first = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(),
            test_mode=True,
        )
        second = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(),
            test_mode=True,
        )
        self.assertEqual(first.plan_id, second.plan_id)
        self.assertEqual(first.provider_traces, second.provider_traces)
        self.assertTrue(
            all(trace.prompt_hash and trace.response_hash for trace in first.provider_traces)
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = write_two_pass_plan(first, output_path=Path(tmp) / "plan.json")
            self.assertTrue(path.is_file())
            self.assertEqual(json.loads(path.read_text())["status"], "COMPLETE")

    def test_critique_identity_changes_when_blind_hypothesis_changes(self) -> None:
        blind_input = self._input_for_benchmark("BR-C06-01")
        first_capture = []
        second_capture = []

        def alter_hypothesis(row):
            row["hypotheses"][0]["mechanism_summary"] += " A distinct mechanism detail."
            return row

        first = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(capture=first_capture),
            test_mode=True,
        )
        second = run_two_pass_planner(
            blind_input=blind_input,
            memory_index=self.memory.index,
            provider=self._provider(
                mutate_a=alter_hypothesis,
                capture=second_capture,
            ),
            test_mode=True,
        )
        first_critique_id = next(
            payload["input"]["input_id"]
            for label, payload in first_capture
            if label == "B"
        )
        second_critique_id = next(
            payload["input"]["input_id"]
            for label, payload in second_capture
            if label == "B"
        )
        self.assertEqual(first.plan_id, second.plan_id)
        self.assertNotEqual(first_critique_id, second_critique_id)
        self.assertNotEqual(
            first.provider_traces[-1].prompt_hash,
            second.provider_traces[-1].prompt_hash,
        )

    def test_benchmark_writer_and_transport_command(self) -> None:
        audit = evaluate_two_pass_planner_benchmark(
            memory_index=self.memory.index,
            benchmark_cases=self.benchmark,
            provider=self._provider(),
            test_mode=True,
        )
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_two_pass_planner_benchmark(audit, output_root=tmp)
            self.assertTrue(all(path.is_file() for path in paths.values()))
            transport = CodexStructuredProviderTransport(working_directory=REPO_ROOT)
            command = transport.command(
                schema_path=Path(tmp) / "schema.json",
                output_path=Path(tmp) / "output.json",
            )
            self.assertIn("--output-schema", command)
            self.assertIn("--output-last-message", command)
            self.assertEqual(command[-1], "-")

    def test_default_real_provider_loads_project_env_and_validates_transport(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env_path = Path(tmp) / ".env"
            env_path.write_text(
                "\n".join(
                    (
                        "E2R_CODEX_PLANNER_COMMAND=codex-from-dotenv",
                        "E2R_CODEX_PLANNER_MODEL=test-model",
                        "E2R_CODEX_PLANNER_TIMEOUT_SECONDS=42",
                        "E2R_CODEX_PLANNER_EXTRA_ARGS=--config test.value=true",
                    )
                ),
                encoding="utf-8",
            )
            with patch.dict(os.environ, {}, clear=True):
                provider = build_codex_two_pass_planner_provider(
                    working_directory=REPO_ROOT,
                    env_file=env_path,
                )
                self.assertEqual(provider.transport.codex_command, "codex-from-dotenv")
                self.assertEqual(provider.transport.model, "test-model")
                self.assertEqual(provider.transport.timeout_seconds, 42.0)
                self.assertEqual(
                    provider.transport.extra_args,
                    ("--config", "test.value=true"),
                )
                self.assertEqual(provider.transport.working_directory, REPO_ROOT)

            with patch.dict(
                os.environ,
                {"E2R_CODEX_PLANNER_COMMAND": "process-command"},
                clear=True,
            ):
                provider = build_codex_two_pass_planner_provider(env_file=env_path)
                self.assertEqual(provider.transport.codex_command, "process-command")

        with self.assertRaisesRegex(ValueError, "unsafe characters"):
            CodexStructuredProviderTransport().complete(
                prompt="test",
                output_schema={"type": "object"},
                schema_name="../../escape",
            )
        with self.assertRaisesRegex(ValueError, "timeout"):
            CodexStructuredProviderTransport(timeout_seconds=0)


if __name__ == "__main__":
    unittest.main()
