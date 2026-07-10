import json
import unittest
from dataclasses import replace
from datetime import date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    AppendOnlyEvidenceLedger,
    Directness,
    EvidenceAnchor,
    EvidenceDocument,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    RawAssertion,
    RelationToTarget,
    SemanticStatus,
    SourceType,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
)
from e2r.census.census_runner_v4 import (
    _export_brain_web_bundle_leafs,
    _merge_jsonl_by_key,
    _raw_assertion_rejection_reason_from_mapping_trace,
    _source_task_realness_audit,
    _write_planner_prompt_response_leafs,
)
from e2r.production.source_connectors.source_provider_registry import SourceProviderRegistry
from e2r.research.page_fetcher import PageFetcher
from e2r.research.search_provider import FixtureSearchProvider, SearchResult
from e2r.research_brain.schemas import SourceTask, SourceTaskType
from e2r.research_brain.v4_evidence_extraction_bridge import EvidenceOSExecutionBundleV4, execute_source_tasks_with_evidence_os_v4
from e2r.research_brain.v4_planner_runtime import run_planner_provider_v4
from e2r.research_brain.v4_schemas import DailyWatchlistItemV4, SourceAcquisitionResultV4, SourceTaskExecutionV4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from tests.research_brain_v4_test_helpers import (
    RealStubPlannerProviderV4,
    c06_source_task,
    load_v4_cards,
    research_brain_v4_fixture_root,
    sample_v4_event,
)


class CensusV4BrainBundleExportTests(unittest.TestCase):
    def test_planner_prompt_response_leafs_are_exported_with_hashes(self):
        event = sample_v4_event()
        runs = run_planner_provider_v4(
            provider=RealStubPlannerProviderV4(),
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={event.candidate_event_id: {}},
        )

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_planner_prompt_response_leafs(output_root=root, planner_runs=runs)
            prompts = _read_jsonl(root / "llm_prompts.jsonl")
            responses = _read_jsonl(root / "llm_responses.jsonl")
            prompt_artifact = json.loads((root / prompts[0]["raw_prompt_path"]).read_text(encoding="utf-8"))
            response_artifact = json.loads((root / responses[0]["raw_response_path"]).read_text(encoding="utf-8"))

        self.assertEqual(len(prompts), 1)
        self.assertEqual(len(responses), 1)
        self.assertEqual(prompts[0]["planner_run_id"], runs[0].planner_run_id)
        self.assertEqual(responses[0]["planner_run_id"], runs[0].planner_run_id)
        self.assertEqual(prompts[0]["prompt_hash"], runs[0].prompt_hash)
        self.assertEqual(responses[0]["response_hash"], runs[0].response_hash)
        self.assertEqual(prompt_artifact["prompt_hash"], runs[0].prompt_hash)
        self.assertEqual(response_artifact["response_hash"], runs[0].response_hash)
        self.assertIn("research_brain_v4_planner_prompt", json.dumps(prompt_artifact, ensure_ascii=False))
        self.assertIn("candidate_event_id", json.dumps(response_artifact, ensure_ascii=False))

    def test_planner_prompt_response_leafs_merge_across_attempts(self):
        first_event = sample_v4_event("005930", "삼성전자")
        second_event = sample_v4_event("000660", "SK하이닉스")
        first_runs = run_planner_provider_v4(
            provider=RealStubPlannerProviderV4(),
            events=(first_event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={first_event.candidate_event_id: {}},
        )
        second_runs = run_planner_provider_v4(
            provider=RealStubPlannerProviderV4(),
            events=(second_event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={second_event.candidate_event_id: {}},
        )

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_planner_prompt_response_leafs(output_root=root, planner_runs=first_runs)
            _write_planner_prompt_response_leafs(output_root=root, planner_runs=second_runs)
            prompts = _read_jsonl(root / "llm_prompts.jsonl")
            responses = _read_jsonl(root / "llm_responses.jsonl")

        self.assertEqual({row["candidate_event_id"] for row in prompts}, {first_event.candidate_event_id, second_event.candidate_event_id})
        self.assertEqual({row["candidate_event_id"] for row in responses}, {first_event.candidate_event_id, second_event.candidate_event_id})

    def test_brain_bundle_exports_claim_leafs_without_stage_promotion(self):
        event = sample_v4_event()
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV4(
                mode="frozen_real_source_snapshot",
                repo_root=research_brain_v4_fixture_root(),
            ),
        )
        self.assertTrue(bundle.executions[0].accepted_claim_ids)
        self.assertTrue(bundle.raw_assertions)

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            watchlist_item = DailyWatchlistItemV4(
                symbol=event.symbol,
                company_name=event.company_name,
                candidate_event_id=event.candidate_event_id,
                event_type=event.event_type,
                event_summary=event.event_summary,
                event_source=event.source_id,
                primary_archetype="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                accepted_claim_ids=tuple(bundle.executions[0].accepted_claim_ids),
            )
            counts = _export_brain_web_bundle_leafs(
                result={
                    "config": {"as_of_date": "2026-06-29"},
                    "bundles": {event.candidate_event_id: bundle},
                    "planner_runs": (),
                    "watchlist_items": (watchlist_item,),
                },
                output_root=root,
            )
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            documents = _read_jsonl(root / "evidence_documents.jsonl")
            anchors = _read_jsonl(root / "evidence_anchors.jsonl")
            raw = _read_jsonl(root / "raw_assertions.jsonl")
            adjudicated = _read_jsonl(root / "adjudicated_claims.jsonl")
            primitives = _read_jsonl(root / "primitive_states.jsonl")
            contributions = _read_jsonl(root / "score_contributions.jsonl")
            stagecourt = _read_jsonl(root / "stagecourt_traces.jsonl")
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            mapping_trace = _read_jsonl(root / "brain_claim_mapping_trace.jsonl")

        self.assertGreater(counts["stagecourt_trace_exported_count"], 0)
        self.assertGreater(counts["brain_claim_mapping_trace_exported_count"], 0)
        self.assertEqual(counts["accepted_claim_exported_count"], len({row["claim_id"] for row in accepted}))
        self.assertTrue(documents)
        self.assertTrue(anchors)
        self.assertTrue(raw)
        self.assertTrue(adjudicated)
        self.assertTrue(accepted)
        self.assertTrue(primitives)
        self.assertTrue(contributions)
        self.assertTrue(stagecourt)
        self.assertEqual({row["accepted_claim_id"] for row in traces}, {row["claim_id"] for row in accepted})
        accepted_by_id = {row["claim_id"]: row for row in accepted}
        self.assertTrue(all(row["score_contribution_id"] for row in contributions))
        self.assertTrue(all(row["stagecourt_trace_id"] for row in stagecourt))
        self.assertTrue(all(row["stagecourt_trace_id"] for row in traces))
        self.assertTrue(all("score_eligible" in row for row in traces))
        self.assertTrue(all(row["score_eligible"] == accepted_by_id[row["accepted_claim_id"]]["score_eligible"] for row in traces))
        self.assertTrue(all(row["score_contribution_id"] for row in traces))
        self.assertTrue(all(row["score_contribution_ids"] for row in traces))
        self.assertTrue(all(row["score_contribution_id"] in row["score_contribution_ids"] for row in traces))
        self.assertTrue(all(row["primitive_state_id"] for row in traces))
        self.assertTrue(all(row["primitive_state_ids"] for row in traces))
        self.assertTrue(all(row["primitive_state_id"] in row["primitive_state_ids"] for row in traces))
        self.assertTrue(all(row["brain_web_claim"] is True for row in accepted))
        self.assertTrue(all(row["source_origin"] == "research_brain_v4_attempt" for row in accepted))
        self.assertTrue(all(row["trace_status"] == "CLAIM_SCORE_TRACE_EXPORTED_STAGE_NOT_PROMOTED" for row in traces))
        self.assertTrue(mapping_trace)
        self.assertTrue(any(row["accepted"] is True for row in mapping_trace))
        self.assertEqual({row["claim_id"] for row in mapping_trace if row["accepted"] is True}, {row["claim_id"] for row in accepted})
        self.assertTrue(all(row["source_document_id"] for row in mapping_trace))
        self.assertTrue(all(row["source_anchor_id"] for row in mapping_trace))

    def test_rerouted_claim_is_planner_feedback_not_score_export(self):
        event = sample_v4_event()
        task = c06_source_task("medium_term_revision_visibility")
        text = "삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다."
        document = EvidenceDocument.from_text(
            text=text,
            canonical_url="https://unit.example.com/rerouted",
            source_type=SourceType.NEWS,
            source_name="unit",
            published_at=date(2026, 6, 20),
            available_at=date(2026, 6, 20),
            fetched_at=date(2026, 6, 29),
            parser_version="unit",
            source_proxy_only=False,
        )
        anchor = EvidenceAnchor.text_span(document=document, document_text=text, exact_text=text)
        raw = RawAssertion(
            raw_assertion_id="RAW-REROUTED",
            anchor_id=anchor.anchor_id,
            subject_text="삼성전자",
            predicate="customer_allocation_or_qualification_claim",
            object_text=anchor.exact_text or "",
            value=anchor.exact_text or "",
            polarity_proposal=Polarity.POSITIVE,
            exact_quote=anchor.exact_text or "",
        )
        claim = AdjudicatedClaim(
            claim_id="CLM-REROUTED",
            raw_assertion_id=raw.raw_assertion_id,
            subject_entity_id="TICKER:005930",
            target_entity_id="TICKER:005930",
            relation_to_target=RelationToTarget.SELF,
            directness=Directness.DIRECT,
            verification_status=VerificationStatus.SEMANTIC_VERIFIED,
            target_scope_status=TargetScopeStatus.DIRECT,
            polarity=Polarity.POSITIVE,
            temporal_status=TemporalStatus.CURRENT,
            semantic_status=SemanticStatus.PASS_,
            investigation_status=InvestigationStatus.COMPLETE,
            event_date=date(2026, 6, 20),
            adjudication_rationale="unit valid claim for a different primitive",
            source_document_id=document.document_id,
            source_anchor_id=anchor.anchor_id,
            source_assertion_id="SRCASSERT-REROUTED",
        )
        mapping = PrimitiveMappingProposal.build(
            claim_id=claim.claim_id,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_id="customer_preorder_or_allocation",
            support_direction=SupportDirection.SUPPORT,
            mapping_status=MappingStatus.ACCEPTED,
            rationale="unit valid rerouted claim",
            contract_rule_id="customer_preorder_or_allocation",
        )
        ledger = AppendOnlyEvidenceLedger()
        ledger.append_claim(claim)
        ledger.append_mapping(mapping)
        execution = SourceTaskExecutionV4(
            task_id="TASK-REROUTED",
            source_task=task.to_dict(),
            status="EVIDENCE_OS_ACCEPTED",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=task.archetype_id,
            primitive_gap=task.primitive_gap,
            source_class="TrustedNews",
            provider_name="unit",
            fetched_document_ids=(document.document_id,),
            document_urls=(document.canonical_url or "",),
            document_hashes=(document.content_hash,),
            evidence_anchor_ids=(anchor.anchor_id,),
            raw_assertion_ids=(raw.raw_assertion_id,),
            adjudicated_claim_ids=(claim.claim_id,),
            accepted_claim_ids=(claim.claim_id,),
            direct_accepted_claim_ids=(),
            rerouted_accepted_claim_ids=(claim.claim_id,),
            accepted_primitive_ids=(mapping.primitive_id,),
            primitive_gap_unsatisfied_ids=(task.primitive_gap,),
            satisfies_source_task=False,
            satisfaction_type="REROUTED_ACCEPTED_CLAIM",
            stop_reason="rerouted_claim_accepted_original_gap_unsatisfied",
        )
        bundle = EvidenceOSExecutionBundleV4(
            ledger=ledger,
            executions=(execution,),
            documents={document.document_id: document},
            anchors={anchor.anchor_id: anchor},
            document_text_by_id={document.document_id: text},
            extraction_audit={},
            raw_assertions={raw.raw_assertion_id: raw},
        )
        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertFalse(execution.satisfies_source_task)
        self.assertEqual(execution.satisfaction_type, "REROUTED_ACCEPTED_CLAIM")

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            watchlist_item = DailyWatchlistItemV4(
                symbol=event.symbol,
                company_name=event.company_name,
                candidate_event_id=event.candidate_event_id,
                event_type=event.event_type,
                event_summary=event.event_summary,
                event_source=event.source_id,
                primary_archetype="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                accepted_claim_ids=tuple(execution.accepted_claim_ids),
            )
            counts = _export_brain_web_bundle_leafs(
                result={
                    "config": {"as_of_date": "2026-06-29"},
                    "bundles": {event.candidate_event_id: bundle},
                    "planner_runs": (),
                    "watchlist_items": (watchlist_item,),
                },
                output_root=root,
            )
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            contributions = _read_jsonl(root / "score_contributions.jsonl")
            stagecourt = _read_jsonl(root / "stagecourt_traces.jsonl")
            source_executions = _read_jsonl(root / "source_task_executions.jsonl")
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            mapping_trace = _read_jsonl(root / "brain_claim_mapping_trace.jsonl")

        self.assertGreater(counts["accepted_claim_exported_count"], 0)
        self.assertEqual(counts["score_contribution_exported_count"], 0)
        self.assertEqual(counts["stagecourt_trace_exported_count"], 0)
        self.assertTrue(accepted)
        self.assertTrue(all(row["score_eligible"] is False for row in accepted))
        self.assertTrue(all(row["satisfies_source_task"] is False for row in accepted))
        self.assertTrue(all("source_task_not_satisfied_rerouted_claim" in row["eligibility_reasons"] for row in accepted))
        self.assertFalse(contributions)
        self.assertFalse(stagecourt)
        self.assertEqual(source_executions[0]["score_claim_ids"], [])
        self.assertEqual(source_executions[0]["score_claim_count"], 0)
        self.assertEqual(traces[0]["score_support_status"], "NO_SCORE_CONTRIBUTION")
        accepted_mapping_rows = [row for row in mapping_trace if row.get("accepted") is True]
        self.assertTrue(accepted_mapping_rows)
        self.assertTrue(all(row["score_eligible"] is False for row in accepted_mapping_rows))
        self.assertTrue(all(row["trace_status"] == "ACCEPTED_NOT_SCORE_ELIGIBLE" for row in accepted_mapping_rows))
        self.assertTrue(all("source_task_not_satisfied_rerouted_claim" in row["eligibility_reasons"] for row in accepted_mapping_rows))

    def test_brain_bundle_exports_web_search_leafs(self):
        event = sample_v4_event()
        query = "삼성전자 HBM 고객 배정 qualification"
        url = "https://news.example.com/samsung-hbm"
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV4(
                mode="live_full_bounded",
                source_provider_registry=SourceProviderRegistry(connectors=()),
                web_search_provider=FixtureSearchProvider(
                    results_by_query={
                        query: (
                            SearchResult(
                                title="삼성전자 HBM 고객 배정 확인",
                                url=url,
                                snippet="삼성전자 HBM 고객 배정 관련 기사",
                                source="NaverSearch",
                                published_at=datetime(2026, 6, 20, 9, 0),
                                query=query,
                                rank=1,
                                is_news=True,
                            ),
                        )
                    }
                ),
                web_page_fetcher=PageFetcher(
                    fixture_text_by_url={
                        url: "삼성전자(005930)는 HBM 고객 배정과 qualification 진행 상황을 설명했다. 원문 전문이다."
                    }
                ),
            ),
        )

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            counts = _export_brain_web_bundle_leafs(
                result={
                    "config": {"as_of_date": "2026-06-29"},
                    "bundles": {event.candidate_event_id: bundle},
                    "planner_runs": (),
                    "watchlist_items": (),
                },
                output_root=root,
            )
            web_tasks = _read_jsonl(root / "web_search_tasks.jsonl")
            web_results = _read_jsonl(root / "web_search_results.jsonl")
            web_fetched = _read_jsonl(root / "web_fetched_documents.jsonl")
            extractor_runs = _read_jsonl(root / "claim_extractor_runs.jsonl")
            source_executions = _read_jsonl(root / "source_task_executions.jsonl")
            raw_rows = _read_jsonl(root / "raw_assertions.jsonl")
            adjudicated = _read_jsonl(root / "adjudicated_claims.jsonl")
            mapping_trace = _read_jsonl(root / "brain_claim_mapping_trace.jsonl")

        self.assertEqual(counts["web_search_task_exported_count"], 1)
        self.assertEqual(counts["web_search_result_exported_count"], 1)
        self.assertEqual(counts["web_fetched_document_exported_count"], 1)
        self.assertEqual(counts["claim_extractor_run_exported_count"], 1)
        self.assertGreater(counts["brain_claim_mapping_trace_exported_count"], 0)
        self.assertEqual(web_tasks[0]["status"], "SEARCH_EXECUTED")
        self.assertEqual(web_results[0]["selection_status"], "SELECTED_FOR_FETCH")
        self.assertEqual(web_fetched[0]["url"], url)
        self.assertEqual(web_fetched[0]["source_origin"], "research_brain_v4_attempt")
        self.assertEqual(source_executions[0]["symbol"], event.symbol)
        self.assertEqual(source_executions[0]["company_name"], event.company_name)
        self.assertEqual(source_executions[0]["archetype_id"], task.archetype_id)
        self.assertEqual(source_executions[0]["primitive_gap"], task.primitive_gap)
        self.assertEqual(source_executions[0]["source_class"], "NaverSearch")
        self.assertTrue(source_executions[0]["provider_name"])
        self.assertEqual(source_executions[0]["preferred_source_classes"], ["NaverSearch"])
        self.assertEqual(source_executions[0]["requested_source_classes"], ["NaverSearch"])
        self.assertEqual(source_executions[0]["source_task_origin"], "research_brain_v4_attempt")
        self.assertEqual(extractor_runs[0]["document_id"], web_fetched[0]["document_id"])
        self.assertEqual(extractor_runs[0]["source_origin"], "research_brain_v4_attempt")
        self.assertTrue(raw_rows)
        self.assertTrue(adjudicated)
        self.assertEqual(raw_rows[0]["document_id"], web_fetched[0]["document_id"])
        self.assertEqual(raw_rows[0]["source_document_id"], web_fetched[0]["document_id"])
        self.assertEqual(raw_rows[0]["source_anchor_id"], web_fetched[0]["anchor_id"])
        self.assertTrue(raw_rows[0]["exact_quote"])
        self.assertTrue(raw_rows[0]["anchor_verified"])
        self.assertEqual(adjudicated[0]["source_document_id"], web_fetched[0]["document_id"])
        self.assertEqual(adjudicated[0]["document_id"], web_fetched[0]["document_id"])
        self.assertEqual(adjudicated[0]["anchor_id"], web_fetched[0]["anchor_id"])
        self.assertEqual(adjudicated[0]["quote_text"], raw_rows[0]["exact_quote"])
        self.assertEqual(mapping_trace[0]["source_document_id"], web_fetched[0]["document_id"])
        self.assertEqual(mapping_trace[0]["source_anchor_id"], web_fetched[0]["anchor_id"])
        self.assertEqual(mapping_trace[0]["quote_text"], raw_rows[0]["exact_quote"])
        self.assertEqual(mapping_trace[0]["source_task_id"], task.task_id)
        self.assertEqual(mapping_trace[0]["primitive_gap"], task.primitive_gap)
        self.assertIn(mapping_trace[0]["trace_status"], {"ACCEPTED_FOR_SCORE", "ACCEPTED_NOT_SCORE_ELIGIBLE", "REJECTED_BEFORE_SCORE"})
        if mapping_trace[0]["accepted"] is False:
            self.assertTrue(mapping_trace[0]["rejection_reason"])

    def test_brain_bundle_exports_source_lineage_retry_drop_execution(self):
        event = sample_v4_event()
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            task_id="TASK-RETRY-DISCOVERY-ONLY",
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=("IndustryMedia",),
            query_intents=("삼성전자 HBM 고객 배정 기사",),
            reason_from_memory=(
                "unit source lineage retry;"
                "feedback_retry:source_lineage_unverified_original;"
                "dropped:source_lineage_retry_discovery_only_after_unverified_original"
            ),
        )
        execution = SourceTaskExecutionV4(
            task_id="RSTASKV4RETRYDROP-UNIT",
            source_task=task.to_dict(),
            status="REJECTED_BY_POLICY",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=task.archetype_id,
            primitive_gap=task.primitive_gap,
            source_class="policy",
            provider_name="research_brain_v4_retry_policy",
            source_task_origin="feedback_retry",
            preferred_source_classes=task.preferred_source_classes,
            fallback_source_classes=task.fallback_source_classes,
            requested_source_classes=(*task.preferred_source_classes, *task.fallback_source_classes),
            not_eligible_reasons=("source_lineage_retry_discovery_only_after_unverified_original",),
            provider_errors=("source_lineage_retry_discovery_only_after_unverified_original",),
            budget_used={"queries": 0, "candidates": 0, "fetches": 0},
            stop_reason="source_lineage_retry_discovery_only_after_unverified_original",
        )
        bundle = EvidenceOSExecutionBundleV4(
            ledger=AppendOnlyEvidenceLedger(),
            executions=(execution,),
            documents={},
            anchors={},
            document_text_by_id={},
            extraction_audit={"source_lineage_feedback_retry_dropped_count": 1},
        )

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            counts = _export_brain_web_bundle_leafs(
                result={
                    "config": {"as_of_date": "2026-06-29"},
                    "bundles": {event.candidate_event_id: bundle},
                    "planner_runs": (),
                    "watchlist_items": (),
                },
                output_root=root,
            )
            source_executions = _read_jsonl(root / "source_task_executions.jsonl")
            source_tasks = _read_jsonl(root / "source_tasks.jsonl")

        self.assertEqual(counts["source_task_execution_exported_count"], 1)
        self.assertEqual(counts["source_task_exported_count"], 1)
        self.assertEqual(source_executions[0]["status"], "REJECTED_BY_POLICY")
        self.assertEqual(source_executions[0]["provider_name"], "research_brain_v4_retry_policy")
        self.assertEqual(
            source_executions[0]["stop_reason"],
            "source_lineage_retry_discovery_only_after_unverified_original",
        )
        self.assertEqual(source_executions[0]["budget_used"], {"queries": 0, "candidates": 0, "fetches": 0})
        self.assertEqual(source_tasks[0]["task_id"], "TASK-RETRY-DISCOVERY-ONLY")
        self.assertIn(
            "dropped:source_lineage_retry_discovery_only_after_unverified_original",
            source_tasks[0]["reason_from_memory"],
        )

    def test_source_task_execution_merge_backfills_existing_leaf_identity(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "source_task_executions.jsonl"
            path.write_text(
                json.dumps(
                    {
                        "task_id": "SRC-OLD",
                        "symbol": "005930",
                        "source_task": {
                            "task_id": "SRC-OLD",
                            "candidate_event_id": "CE-1",
                            "symbol": "005930",
                            "company_name": "삼성전자",
                            "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                            "primitive_gap": "named_customer_or_customer_quality",
                            "preferred_source_classes": ["DART", "IssuerOfficial"],
                            "fallback_source_classes": ["TrustedNews"],
                            "forbidden_source_classes": ["unbounded_general_search"],
                        },
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )
            _merge_jsonl_by_key(path, [{"task_id": "SRC-NEW", "source_task": {"preferred_source_classes": ["KIND"]}}], "task_id")
            rows = _read_jsonl(path)

        old = next(row for row in rows if row["task_id"] == "SRC-OLD")
        self.assertEqual(old["candidate_event_id"], "CE-1")
        self.assertEqual(old["company_name"], "삼성전자")
        self.assertEqual(old["archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(old["primitive_gap"], "named_customer_or_customer_quality")
        self.assertEqual(old["source_class"], "DART")
        self.assertEqual(old["provider_name"], "OpenDART")
        self.assertEqual(old["requested_source_classes"], ["DART", "IssuerOfficial", "TrustedNews"])
        self.assertTrue(old["source_task_origin"])

    def test_source_task_realness_audit_checks_execution_identity_fields(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            task = {
                "task_id": "SRC-OLD",
                "candidate_event_id": "CE-1",
                "symbol": "005930",
                "company_name": "삼성전자",
                "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "primitive_gap": "named_customer_or_customer_quality",
                "preferred_source_classes": ["DART"],
                "fallback_source_classes": ["IssuerOfficial"],
                "forbidden_source_classes": ["unbounded_general_search"],
            }
            (root / "source_tasks.jsonl").write_text(json.dumps(task, ensure_ascii=False) + "\n", encoding="utf-8")
            (root / "source_task_executions.jsonl").write_text(
                json.dumps(
                    {
                        "task_id": "SRC-OLD",
                        "status": "NO_EVIDENCE_FOUND",
                        "source_task": task,
                        "accepted_claim_ids": [],
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )
            audit = _source_task_realness_audit(output_root=root)

        self.assertEqual(audit["critical_counts"]["source_task_execution_missing_source_class_count"], 0)
        self.assertEqual(audit["critical_counts"]["source_task_execution_missing_provider_name_count"], 0)
        self.assertEqual(audit["critical_counts"]["source_task_execution_missing_source_task_origin_count"], 0)
        self.assertEqual(audit["critical_counts"]["source_task_execution_missing_requested_source_classes_count"], 0)

    def test_brain_mapping_trace_merges_source_task_rejection_detail(self):
        event = sample_v4_event(symbol="069620", company_name="대웅제약")
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE"]
        task = SourceTask(
            task_id="facility-volume-growth",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
            primitive_gap="volume_growth_visible",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-06-30", "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            llm_query_allowed=True,
            general_search_allowed=False,
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleTextDocumentRunner(
                symbol="069620",
                company_name="대웅제약",
                text="대웅제약은 신규시설투자 정정신고를 통해 정정사유가 종료일 연장이라고 밝혔다.",
            ),
        )

        self.assertFalse(bundle.executions[0].accepted_claim_ids)
        self.assertTrue(bundle.executions[0].rejected_claim_ids)
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            counts = _export_brain_web_bundle_leafs(
                result={
                    "config": {"as_of_date": "2026-07-01"},
                    "bundles": {event.candidate_event_id: bundle},
                    "planner_runs": (),
                    "watchlist_items": (),
                },
                output_root=root,
            )
            mapping_trace = _read_jsonl(root / "brain_claim_mapping_trace.jsonl")
            raw_rejections = _read_jsonl(root / "raw_assertion_rejections.jsonl")

        self.assertTrue(mapping_trace)
        self.assertGreater(counts["raw_assertion_rejection_exported_count"], 0)
        self.assertTrue(raw_rejections)
        self.assertFalse(mapping_trace[0]["accepted"])
        self.assertFalse(mapping_trace[0]["score_eligible"])
        self.assertIn("mapping_not_accepted:REJECTED", mapping_trace[0]["eligibility_reasons"])
        self.assertIn(
            "primitive_mapping_rejected:facility_investment_correction_requires_followup_not_positive_capacity",
            mapping_trace[0]["eligibility_reasons"],
        )
        self.assertEqual(raw_rejections[0]["raw_assertion_id"], mapping_trace[0]["raw_assertion_id"])
        self.assertEqual(raw_rejections[0]["adjudicated_claim_id"], mapping_trace[0]["claim_id"])
        self.assertEqual(raw_rejections[0]["rejection_reason"], "primitive_mapping_rejected")
        self.assertEqual(raw_rejections[0]["source_task_id"], task.task_id)
        self.assertEqual(raw_rejections[0]["primitive_gap"], "volume_growth_visible")

    def test_raw_assertion_rejection_reason_prefers_row_axes_over_polluted_task_reasons(self):
        reason = _raw_assertion_rejection_reason_from_mapping_trace(
            row={
                "target_scope_status": "DIRECT",
                "directness": "DIRECT",
                "temporal_status": "CURRENT",
                "semantic_status": "PASS",
                "mapping_status": "REJECTED",
            },
            eligibility_reasons=[
                "mapping_not_accepted:REJECTED",
                "primitive_mapping_rejected:no_allowed_primitive_for_predicate",
                "target_scope_not_allowed:UNRELATED",
                "target_not_direct:NOT_TARGET_SCOPED",
                "temporal_not_allowed:HISTORICAL",
            ],
        )

        self.assertEqual(reason, "primitive_mapping_rejected")


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class _SingleTextDocumentRunner:
    def __init__(self, *, symbol: str, company_name: str, text: str) -> None:
        self.symbol = symbol
        self.company_name = company_name
        self.text = text

    def acquire(self, *, event, task, as_of_date):
        document = EvidenceDocument.from_text(
            text=self.text,
            canonical_url=f"https://unit.example.com/{self.symbol}",
            source_type=SourceType.NEWS,
            source_name="unit",
            published_at=date(2026, 6, 30),
            available_at=date(2026, 6, 30),
            fetched_at=as_of_date,
            parser_version="unit",
            source_proxy_only=False,
        )
        anchor = EvidenceAnchor.text_span(document=document, document_text=self.text, exact_text=self.text)
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class="TrustedNews",
            provider_name="unit",
            status="PARSED",
            documents=(document,),
            anchors=(anchor,),
            document_text_by_id={document.document_id: self.text},
            fetched_document_ids=(document.document_id,),
            document_urls=(document.canonical_url,),
            document_hashes=(document.content_hash,),
            anchor_ids=(anchor.anchor_id,),
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
            stop_reason="unit",
        )


if __name__ == "__main__":
    unittest.main()
