from __future__ import annotations

import inspect
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from e2r.cli.run_e2r_researcher_mode_until_pass import (
    _latest_calendar_trading_candidate,
    _semantic_signature,
    build_parser,
)
from e2r.research import EmptySearchProvider, PageFetcher
from e2r.research_brain.researcher_mode import (
    CANONICAL_COMPONENT_ORDER,
    ComponentResearchPlanner,
    CurrentStructuredMaterializationResult,
    CurrentResearcherModeConfig,
    CurrentResearchTarget,
    SourceGraphExplorer,
    OfficialSourceMaterializationResult,
    ResearcherEvidenceFactExtractor,
    ResearcherSourceGraphAcquirer,
    load_current_research_targets,
)
from tests.test_e2r_v5_fact_extraction import FactProvider, _document
from tests.test_e2r_v5_researcher_mode import ScriptedResearchProvider


class Phase94IntegrationProvider:
    provider_name = "PHASE94_INTEGRATION_PROVIDER"

    def __init__(self) -> None:
        self.base = ScriptedResearchProvider()
        self.fact = FactProvider()
        self.calls = []
        self.response_cache_directories = []

    def configure_response_cache(self, directory):
        self.response_cache_directories.append(Path(directory))

    def response_cache_audit(self):
        return {
            "status": "FIXTURE_PROVIDER_CACHE_INTERFACE_ACTIVE",
            "logical_call_count": len(self.calls),
            "transport_call_count": len(self.calls),
            "cache_hit_count": 0,
            "cache_invalid_or_unreadable_count": 0,
        }

    def complete(self, *, pass_name, payload):
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if pass_name == "SOURCE_QUERY_GENERATION":
            return {
                "suggested_queries": [],
                "new_source_directions": [],
                "unresolved_research_notes": ["fixture has only official source"],
            }
        if pass_name == "EVIDENCE_FACT_EXTRACTION":
            return self.fact.complete(pass_name=pass_name, payload=payload)
        if pass_name == "RESEARCH_SUPERVISOR_REVIEW":
            raise RuntimeError("fixture supervisor remains pending")
        response = self.base.complete(pass_name=pass_name, payload=payload)
        if pass_name == "COMPONENT_RESEARCH":
            response = {
                **response,
                "source_coverage": list(payload["source_coverage"])[:1],
            }
        return response


class Phase94IntegrationOfficialMaterializer:
    def materialize(self, **kwargs):
        document = dict(
            _document("DOC-OFFICIAL", "ISSUER_PRESENTATION", "ISSUER:example.com")
        )
        document.update(
            target_id=kwargs["target_id"],
            as_of_date=kwargs["as_of_date"],
        )
        return OfficialSourceMaterializationResult(
            target_id=kwargs["target_id"],
            as_of_date=kwargs["as_of_date"],
            status="OFFICIAL_SOURCE_MATERIALIZED",
            evidence_documents=(document,),
            provider_attempts=({"provider_name": "OpenDART", "status": "FETCHED"},),
            structured_payloads=(
                {
                    "provider_name": "CompanyGuide",
                    "provider_content_hash": "a" * 64,
                    "published_at": "2026-06-27",
                    "available_at": "2026-06-27",
                    "canonical_url": "https://example.com/companyguide",
                    "payload": {
                        "CONSENSUS_AS_OF_DATE": "2026/06/27",
                        "EPS": 1000,
                        "FORWARD_PER": 10,
                        "TARGET_PRC": 100000,
                        "CONSENSUS_PROVIDER_COUNT": 12,
                    },
                },
            ),
            pending_reasons=(),
            audit={
                "status": "OFFICIAL_SOURCE_MATERIALIZATION_PASS",
                "critical_counts": {},
                "critical_count_sum": 0,
            },
        )
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeTargetRunner,
    _historical_anchors,
    _load_prior_research_context,
    _structured_result_from_official,
)


class Phase94IntegrationStructuredMaterializer:
    def materialize(self, **kwargs):
        engine = _structured_result_from_official(
            target=CurrentResearchTarget(
                symbol=kwargs["target_id"], company_name=kwargs["target_name"]
            ),
            as_of_date=kwargs["as_of_date"],
            official=kwargs["official"],
        )
        pending = tuple(
            f"STRUCTURED_ROLE_MISSING:{component_id}:{role}"
            for component_id, roles in engine.missing_roles_by_component.items()
            for role in roles
        )
        return CurrentStructuredMaterializationResult(
            target_id=kwargs["target_id"],
            as_of_date=kwargs["as_of_date"],
            latest_trading_snapshot_date=kwargs[
                "latest_trading_snapshot_date"
            ],
            status="SOURCE_PENDING",
            engine_result=engine,
            fetch_attempts=(),
            payload_manifest=(),
            pending_reasons=pending,
            audit={"status": "FIXTURE_SOURCE_PENDING"},
        )


class E2RV5Phase94RunnerContractTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_master_command_contract_exists_without_low_completion_options(self) -> None:
        parser = build_parser()
        option_strings = {
            option
            for action in parser._actions
            for option in action.option_strings
        }
        self.assertTrue(
            {
                "--as-of-date",
                "--symbols",
                "--archetype",
                "--live-materialization-authorized",
                "--checkpoint-resume",
                "--gold-lane-isolated",
                "--require-researcher-parity",
                "--output-root",
            }.issubset(option_strings)
        )
        self.assertFalse(
            any(
                value in option_strings
                for value in (
                    "--max-rounds",
                    "--max-research-iterations",
                    "--max-documents",
                    "--top-results",
                )
            )
        )

    def test_phase94_requires_live_checkpoint_gold_isolation_and_parity(self) -> None:
        base = {
            "as_of_date": "2026-07-12",
            "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "output_root": "/tmp/phase94-contract",
            "live_materialization_authorized": True,
            "checkpoint_resume": True,
            "gold_lane_isolated": True,
            "require_researcher_parity": True,
        }
        CurrentResearcherModeConfig(**base)
        for key in (
            "live_materialization_authorized",
            "checkpoint_resume",
            "gold_lane_isolated",
            "require_researcher_parity",
        ):
            invalid = {**base, key: False}
            with self.assertRaises(ValueError):
                CurrentResearcherModeConfig(**invalid)

    def test_target_registry_resolves_master_canaries_without_runner_branch(self) -> None:
        targets = load_current_research_targets(symbols=("005930", "000660"))
        self.assertEqual(
            [(row.symbol, row.company_name) for row in targets],
            [("005930", "삼성전자"), ("000660", "SK하이닉스")],
        )
        runner_source = inspect.getsource(CurrentResearcherModeTargetRunner)
        self.assertNotIn("005930", runner_source)
        self.assertNotIn("000660", runner_source)
        self.assertNotIn("삼성전자", runner_source)
        self.assertNotIn("SK하이닉스", runner_source)

    def test_source_graph_has_one_full_thesis_objective_per_component(self) -> None:
        plans = ComponentResearchPlanner().plan(
            target_id="CURRENT",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            evidence_facts=(),
            historical_anchors=(),
        )
        graph = SourceGraphExplorer().explore(
            target_id="CURRENT",
            as_of_date="2026-07-12",
            documents=(),
            research_plans=plans,
            source_coverage=(),
        )
        self.assertEqual(len(graph.open_objectives), 7)
        self.assertEqual(
            {row.component_id for row in graph.open_objectives},
            set(CANONICAL_COMPONENT_ORDER),
        )
        self.assertTrue(all(row.literal_query is None for row in graph.open_objectives))
        self.assertTrue(
            all(row.query_must_be_generated_by_llm for row in graph.open_objectives)
        )

    def test_production_runner_cannot_import_or_read_private_gold(self) -> None:
        source = (
            self.ROOT
            / "src/e2r/research_brain/researcher_mode/current_researcher_mode.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("full_thesis_gold_benchmark", source)
        self.assertNotIn("compare_phase93_gold_post_run", source)
        self.assertNotIn("load_phase93_gold_corpus", source)
        self.assertIn('"gold_visibility": False', source)

    def test_phase94_output_contract_names_are_present(self) -> None:
        source = (
            self.ROOT
            / "src/e2r/research_brain/researcher_mode/current_researcher_mode.py"
        ).read_text(encoding="utf-8")
        for leaf in (
            "business_model_memo.json",
            "source_graph_checkpoint.json",
            "counterfacts.jsonl",
            "component_research_memos.jsonl",
            "structured_engine_result.json",
            "stagecourt.json",
        ):
            self.assertIn(leaf, source)
        self.assertEqual(
            _latest_calendar_trading_candidate("2026-07-12"),
            "2026-07-10",
        )

    def test_no_progress_signature_ignores_supervisor_prose_churn(self) -> None:
        def result(*, question: str, failure_reason: str):
            supervisor = SimpleNamespace(
                status="NEXT_RESEARCH_REQUIRED",
                unresolved_material_questions=(question,),
                next_actions=(f"action for {question}",),
            )
            return SimpleNamespace(
                source_graph=SimpleNamespace(
                    status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                    checkpoint={
                        "generated_queries": [],
                        "search_candidates": [],
                        "query_failures": [
                            {
                                "query_id": "Q1",
                                "candidate_id": "C1",
                                "failure_stage": "FULL_DOCUMENT_FETCH",
                                "failure_reason": failure_reason,
                                "alternate_route_required": True,
                            }
                        ],
                    },
                    evidence_documents=(),
                ),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_COMPLETE",
                    pending_reasons=(),
                    facts=(),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(status="SOURCE_PENDING", records=()),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING", pending_reasons=("SOURCE_PENDING",)
                ),
                research_epoch=SimpleNamespace(supervisor_review=supervisor),
            )

        first = result(question="첫 번째 표현", failure_reason="TLS_FAILURE")
        rephrased = result(question="같은 뜻의 두 번째 표현", failure_reason="TLS_FAILURE")
        changed_failure = result(
            question="같은 뜻의 세 번째 표현",
            failure_reason="HTTP_503_FAILURE",
        )
        self.assertEqual(_semantic_signature(first), _semantic_signature(rephrased))
        self.assertNotEqual(
            _semantic_signature(first), _semantic_signature(changed_failure)
        )

    def test_unstructured_roles_are_not_misclassified_as_structured_metrics(self) -> None:
        plans = ComponentResearchPlanner().plan(
            target_id="CURRENT",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            evidence_facts=(),
            historical_anchors=(),
            research_seeds=(),
        )
        by_component = {row.component_id: row for row in plans}
        self.assertNotIn(
            "CUSTOMER_COMMITMENT",
            by_component["earnings_visibility"].structured_metric_requirements,
        )
        self.assertEqual(
            by_component["information_confidence"].structured_metric_requirements,
            (),
        )
        self.assertIn(
            "CURRENT_VALUATION",
            by_component["valuation_rerating"].structured_metric_requirements,
        )

    def test_missing_exact_archetype_anchors_use_generic_ordinal_guards(self) -> None:
        anchors = _historical_anchors(
            repo_root=self.ROOT,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(
            {row["component_id"] for row in anchors},
            set(CANONICAL_COMPONENT_ORDER),
        )
        transfers = [row for row in anchors if row.get("ordinal_transfer_only")]
        self.assertTrue(transfers)
        self.assertTrue(all(row["usable_as_ordinal_anchor"] for row in transfers))
        self.assertTrue(all(not row["usable_as_exact_anchor"] for row in transfers))
        self.assertTrue(all(row["source_proxy_guard_case_ids"] for row in transfers))
        self.assertTrue(all(not row["company_name_conditioned"] for row in transfers))

    def test_pending_checkpoint_writes_honest_full_dossier_without_gold(self) -> None:
        provider = Phase94IntegrationProvider()
        acquirer = ResearcherSourceGraphAcquirer(
            query_provider=provider,
            search_provider=EmptySearchProvider(),
            page_fetcher=PageFetcher(fixture_text_by_url={}),
        )
        runner = CurrentResearcherModeTargetRunner(
            provider=provider,
            official_materializer=Phase94IntegrationOfficialMaterializer(),
            structured_materializer=Phase94IntegrationStructuredMaterializer(),
            source_acquirer=acquirer,
            fact_extractor=ResearcherEvidenceFactExtractor(
                provider=provider,
                documents_per_call=1,
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            config = CurrentResearcherModeConfig(
                as_of_date="2026-06-29",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                output_root=directory,
                live_materialization_authorized=True,
                checkpoint_resume=True,
                gold_lane_isolated=True,
                require_researcher_parity=True,
                latest_trading_snapshot_date="2026-06-29",
            )
            result = runner.run_checkpoint(
                config=config,
                target=CurrentResearchTarget(
                    symbol="CURRENT-TARGET",
                    company_name="Current Corp",
                    official_domains=("example.com",),
                ),
                repo_root=self.ROOT,
            )
            self.assertEqual(result.status, "RESEARCH_CHECKPOINT_PENDING")
            self.assertEqual(len(result.fact_extraction.facts), 1)
            self.assertFalse(result.score_aggregation.score_valid)
            self.assertEqual(result.structured_result.status, "SOURCE_PENDING")
            expected = {
                "business_model_memo.json",
                "source_graph.json",
                "generated_queries.jsonl",
                "source_graph_evidence_documents.jsonl",
                "evidence_facts.jsonl",
                "counterfacts.jsonl",
                "component_research_memos.jsonl",
                "component_scoring_memos.jsonl",
                "judge_decisions.jsonl",
                "anchor_comparisons.jsonl",
                "component_decisions.jsonl",
                "total_score.json",
                "stagecourt.json",
                "current_researcher_mode_audit.json",
            }
            files = {path.name for path in result.output_root.iterdir() if path.is_file()}
            self.assertTrue(expected.issubset(files))
            audit = json.loads(
                (result.output_root / "current_researcher_mode_audit.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertFalse(audit["gold_visibility"])
            self.assertFalse(audit["completion_based_on_fixed_rounds"])
            self.assertIn(
                "source_graph_checkpoint_ready", audit["completion_gates"]
            )
            self.assertIn("fact_extraction_complete", audit["completion_gates"])
            self.assertFalse(
                audit["completion_gates"]["source_graph_checkpoint_ready"]
            )
            component_payload = next(
                row["payload"]
                for row in provider.calls
                if row["pass_name"] == "COMPONENT_RESEARCH"
            )
            self.assertIn("COMPANYGUIDE", component_payload["source_coverage"])
            query_payload = next(
                row["payload"]
                for row in provider.calls
                if row["pass_name"] == "SOURCE_QUERY_GENERATION"
            )
            self.assertEqual(
                query_payload["score_gap_context"][
                    "verified_official_domain_allowlist"
                ],
                ["example.com"],
            )
            self.assertFalse((result.output_root / "gold_fact_comparison.jsonl").exists())
            self.assertEqual(
                provider.response_cache_directories[-1],
                result.output_root / "research_provider_response_cache",
            )
            self.assertTrue(
                (
                    result.output_root
                    / "research_provider_response_cache_audit.json"
                ).is_file()
            )

            runner.run_checkpoint(
                config=config,
                target=CurrentResearchTarget(
                    symbol="CURRENT-TARGET",
                    company_name="Current Corp",
                    official_domains=("example.com",),
                ),
                repo_root=self.ROOT,
            )
            resumed_query_payload = [
                row["payload"]
                for row in provider.calls
                if row["pass_name"] == "SOURCE_QUERY_GENERATION"
            ][-1]
            self.assertTrue(
                resumed_query_payload["score_gap_context"][
                    "prior_structured_source_gap"
                ]["missing_roles_by_component"]
            )
            self.assertEqual(
                resumed_query_payload["score_gap_context"][
                    "prior_structured_source_gap"
                ]["query_generation_owner"],
                "LLM",
            )

    def test_structured_role_gap_keeps_component_objective_open_for_llm_search(
        self,
    ) -> None:
        target_id = "CURRENT-TARGET"
        as_of_date = "2026-06-29"
        objectives = tuple(
            {
                "objective_id": f"OBJECTIVE-{component_id}",
                "component_id": component_id,
            }
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "component_research_memos.jsonl").write_text(
                "\n".join(
                    json.dumps(
                        {
                            "component_id": component_id,
                            "research_complete": True,
                        }
                    )
                    for component_id in CANONICAL_COMPONENT_ORDER
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "structured_engine_result.json").write_text(
                json.dumps(
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "status": "SOURCE_PENDING",
                        "missing_roles_by_component": {
                            "eps_fcf_explosion": ["FORWARD_GUIDANCE"],
                            "market_mispricing": [],
                            "valuation_rerating": [],
                        },
                        "covered_roles_by_component": {
                            "eps_fcf_explosion": ["FREE_CASH_FLOW"]
                        },
                        "component_disposition_by_component": {
                            "eps_fcf_explosion": "PROVIDER_SOURCE_PENDING"
                        },
                    }
                ),
                encoding="utf-8",
            )
            (root / "current_structured_materialization.json").write_text(
                json.dumps(
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "pending_reasons": [
                            "STRUCTURED_ROLE_MISSING:eps_fcf_explosion:FORWARD_GUIDANCE"
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (root / "current_structured_materialization_audit.json").write_text(
                json.dumps(
                    {
                        "issuer_fact_materialization": {
                            "guidance_observation_count": 0,
                            "issuer_source_required_for_segment_and_guidance": True,
                        }
                    }
                ),
                encoding="utf-8",
            )
            (root / "research_epoch_checkpoint.json").write_text(
                json.dumps(
                    {
                        "checkpoint_id": "EPOCH-1",
                        "epoch": 1,
                        "status": "NEXT_RESEARCH_REQUIRED",
                        "unresolved_material_questions": [
                            "issuer forward guidance source is missing"
                        ],
                        "next_actions": ["generate a new source query with the LLM"],
                        "supervisor_review": {
                            "review_id": "SUPERVISOR-1",
                            "epoch": 1,
                            "status": "NEXT_RESEARCH_REQUIRED",
                            "structured_data_complete": False,
                            "query_direction_briefs": [
                                {
                                    "objective_id": "OBJECTIVE-eps_fcf_explosion",
                                    "research_need": "numeric issuer outlook",
                                    "avoid_repeating": [],
                                    "counter_or_supersession": False,
                                }
                            ],
                        },
                    }
                ),
                encoding="utf-8",
            )

            context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=objectives,
            )

        self.assertNotIn(
            "OBJECTIVE-eps_fcf_explosion", context["resolved_objective_ids"]
        )
        self.assertEqual(
            set(context["resolved_objective_ids"]),
            {
                f"OBJECTIVE-{component_id}"
                for component_id in CANONICAL_COMPONENT_ORDER
                if component_id != "eps_fcf_explosion"
            },
        )
        structured_gap = context["structured_gap_context"]
        self.assertEqual(
            structured_gap["missing_roles_by_component"],
            {"eps_fcf_explosion": ["FORWARD_GUIDANCE"]},
        )
        self.assertEqual(structured_gap["query_generation_owner"], "LLM")
        self.assertFalse(structured_gap["deterministic_fallback_query_allowed"])
        self.assertEqual(
            context["supervisor_gap_context"]["query_direction_briefs"][0][
                "research_need"
            ],
            "numeric issuer outlook",
        )


if __name__ == "__main__":
    unittest.main()
