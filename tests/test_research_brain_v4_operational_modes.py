import json
import subprocess
import unittest
from dataclasses import replace
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    AppendOnlyEvidenceLedger,
    AnchorType,
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
from e2r.production.source_connectors.source_provider_registry import SourceFetchResult, SourceProviderRegistry
from e2r.research.page_fetcher import PageFetcher
from e2r.research.search_provider import SearchResult
from e2r.production.claim_extraction import CodexCLIExtractorProvider, RuleFallbackExtractorProvider
from e2r.research_brain.schemas import SourceTask
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2, EventMagnitudeV2, LLMPlannerOutputV2
from e2r.research_brain.v4_evidence_extraction_bridge import EvidenceOSExecutionBundleV4
from e2r.research_brain.v4_production_orchestrator import (
    _candidate_seed_events_from_config,
    _claim_extractor_for_config,
    _evidence_context_by_event,
    _bundle_has_direct_source_task_acceptance,
    _deduplicated_feedback_retry_tasks,
    _deduplicated_feedback_retry_tasks_with_rejections,
    _merge_evidence_os_bundles_v4,
    _planner_candidate_order,
    _planner_output_requests_external_web,
    _rejected_claim_feedback_from_bundle,
    _rerouted_claim_feedback_from_bundle,
    _retry_planner_for_rerouted_claim_feedback,
    _retry_planner_for_source_rejection_feedback,
    _retry_planner_for_rejected_mapping_feedback,
    _retry_planner_for_missing_external_web_plan,
    _select_unique_candidate_events,
    _source_rejection_feedback_from_bundle,
    run_research_brain_v4_production_shadow,
)
from e2r.research_brain.v4_planner_runtime import (
    CodexCLIPlannerProviderV4,
    build_v4_planner_prompt_payload,
    run_planner_provider_v4,
    source_tasks_from_planner_output_v4,
    validate_llm_planner_output_v4,
)
from e2r.research_brain.v4_schemas import (
    PlannerRunV4,
    ProductionShadowV4Config,
    SourceAcquisitionModeV4,
    SourceAcquisitionResultV4,
    SourceTaskExecutionV4,
)
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from tests.research_brain_v4_test_helpers import load_v4_cards, load_v4_matrix


class ResearchBrainV4OperationalModesTests(unittest.TestCase):
    def _assert_no_forbidden_planner_context_keys(self, value):
        if isinstance(value, dict):
            for key, item in value.items():
                lowered = str(key).lower()
                self.assertNotIn("score", lowered)
                self.assertNotIn("stage", lowered)
                self.assertNotEqual(lowered, "current_score_eligible")
                self._assert_no_forbidden_planner_context_keys(item)
            return
        if isinstance(value, (list, tuple)):
            for item in value:
                self._assert_no_forbidden_planner_context_keys(item)

    def test_production_defaults_use_live_official_first_and_all_candidates_planned(self):
        config = ProductionShadowV4Config(as_of_date="2026-06-29")
        self.assertEqual(config.source_acquisition, "live_official_first")
        self.assertIsNone(config.candidate_event_seed_path)
        self.assertEqual(config.universe_limit, 30)
        self.assertEqual(config.planner_success_limit, 30)
        self.assertEqual(config.planner_batch_size, 5)
        self.assertEqual(config.max_source_tasks_per_plan, 5)
        self.assertEqual(config.max_fetches_per_task, 3)
        self.assertEqual(config.accepted_claim_target, 0)
        self.assertEqual(config.max_distinct_candidate_attempts, 30)
        self.assertEqual(config.claim_extractor_timeout_seconds, 60.0)

    def test_live_full_bounded_web_fallback_uses_remaining_task_budget_after_official(self):
        event = _planner_event()
        task = SourceTask(
            task_id="TASK-UNIT-TASKWIDE-BUDGET",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="customer_preorder_or_allocation",
            task_type="positive_verify",
            preferred_source_classes=("DART", "TrustedNews"),
            fallback_source_classes=("TrustedNews",),
            query_intents=(
                "삼성전자 HBM 고객 배정 확인",
                "삼성전자 HBM CAPA 확인",
                "삼성전자 HBM 매출 비중 확인",
            ),
            max_queries=3,
            max_candidates=20,
            max_fetches=5,
        )
        search_provider = _BudgetRecordingSearchProvider()
        fetcher = PageFetcher(
            fixture_text_by_url={
                f"https://unit-news.example/samsung-hbm-{index}": "삼성전자는 HBM 고객 배정과 CAPA 관련 내용을 확인했다."
                for index in range(1, 4)
            },
            live_enabled=False,
        )
        runner = SourceAcquisitionRunnerV4(
            mode=SourceAcquisitionModeV4.LIVE_FULL_BOUNDED.value,
            source_provider_registry=SourceProviderRegistry((_OneLiveOfficialConnector(),)),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        )

        result = runner.acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(len(search_provider.calls), 2)
        self.assertTrue(all(call["max_results"] <= 19 for call in search_provider.calls))
        self.assertLessEqual(result.budget_used["queries"], task.max_queries)
        self.assertLessEqual(result.budget_used["candidates"], task.max_candidates)
        self.assertLessEqual(result.budget_used["fetches"], task.max_fetches)
        self.assertLessEqual(result.budget_used["fetch_attempts"], task.max_fetches)
        self.assertEqual(result.budget_used["queries"], 3)

    def test_candidate_event_seed_path_is_prioritized_before_daily_discovery(self):
        discovered = _planner_event_with_id("CE-UNIT-DISCOVERED", symbol="000660", company_name="SK하이닉스")
        with TemporaryDirectory() as tmp:
            seed_path = Path(tmp) / "full_thesis_seed.jsonl"
            seed_path.write_text(
                json.dumps(
                    {
                        "candidate_event_id": "CEV4-FTQUEUE-005930",
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "event_date": "2026-06-29",
                        "detected_at": "2026-06-29",
                        "source_family": "CensusFullThesisQueue",
                        "source_id": str(seed_path),
                        "event_type": "full_thesis_refresh_seed",
                        "event_title": "삼성전자 full thesis refresh queue seed",
                        "event_summary": "planner input only",
                        "raw_reason_codes": ["FULL_THESIS_REFRESH_QUEUE"],
                        "score_evidence_allowed": False,
                        "stage_promotion_allowed_before_execution": False,
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            with patch(
                "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
                return_value=(discovered,),
            ):
                result = run_research_brain_v4_production_shadow(
                    config=ProductionShadowV4Config(
                        as_of_date="2026-06-29",
                        planner_provider="none",
                        source_acquisition="live_official_first",
                        candidate_event_seed_path=str(seed_path),
                        universe_limit=1,
                        planner_success_limit=1,
                    ),
                    v1_archetype_matrix=load_v4_matrix(),
                )

        summary = result["candidate_report"]["summary"]
        planner_runs = result["planner_runs"]
        self.assertEqual(summary["candidate_event_count"], 2)
        self.assertEqual(summary["source_family_breakdown"], {"CensusFullThesisQueue": 1, "DART": 1})
        self.assertEqual(planner_runs[0].event.candidate_event_id, "CEV4-FTQUEUE-005930")
        self.assertEqual(planner_runs[0].event.symbol, "005930")

    def test_candidate_event_seed_path_skips_rows_marked_not_research_brain_eligible(self):
        with TemporaryDirectory() as tmp:
            seed_path = Path(tmp) / "all_archetype_replay_gap_seed_events.jsonl"
            seed_path.write_text(
                json.dumps(
                    {
                        "candidate_event_id": "CEV4-ARREPLAYGAP-C01",
                        "symbol": None,
                        "company_name": None,
                        "event_date": "2026-06-29",
                        "detected_at": "2026-06-29",
                        "source_family": "CensusAllArchetypeReplayGap",
                        "source_id": str(seed_path),
                        "event_type": "all_archetype_source_backed_replay_gap_seed",
                        "event_title": "C01 source-backed replay gap seed",
                        "event_summary": "planner input only; not a production candidate event",
                        "raw_reason_codes": ["ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_GAP"],
                        "research_brain_eligible": False,
                        "score_evidence_allowed": False,
                        "stage_promotion_allowed_before_execution": False,
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            events = _candidate_seed_events_from_config(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    candidate_event_seed_path=str(seed_path),
                ),
                as_of_date=date(2026, 6, 29),
            )

        self.assertEqual(events, ())

    def test_candidate_event_seed_path_resolves_missing_company_name_from_registry_not_archetype(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            universe_dir = root / "data/historical_official/universe"
            universe_dir.mkdir(parents=True)
            (universe_dir / "universe.csv").write_text(
                "symbol,name,market,exchange,sector_custom,listed_date,currency\n"
                "005930,삼성전자,KR,KRX,반도체,1975-06-11,KRW\n",
                encoding="utf-8",
            )
            seed_path = root / "goal4_seed.jsonl"
            seed_path.write_text(
                json.dumps(
                    {
                        "candidate_event_id": "CEV4-GOAL4-C06-005930",
                        "symbol": "005930",
                        "company_name": None,
                        "event_date": "2026-06-29",
                        "detected_at": "2026-06-29",
                        "source_family": "AllArchetypeRuntimeParityFollowUp",
                        "source_id": str(seed_path),
                        "event_type": "all_archetype_runtime_parity_follow_up_seed",
                        "target_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "target_symbol_mode": "SYMBOL_SPECIFIC",
                        "seed_role": "planner_input_only",
                        "structured_payload": {
                            "target_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                            "target_symbol_mode": "SYMBOL_SPECIFIC",
                            "seed_role": "planner_input_only",
                        },
                        "research_brain_eligible": True,
                        "score_evidence_allowed": False,
                        "stage_promotion_allowed_before_execution": False,
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            events = _candidate_seed_events_from_config(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    candidate_event_seed_path=str(seed_path),
                ),
                as_of_date=date(2026, 6, 29),
                repo_root=root,
            )

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].symbol, "005930")
        self.assertEqual(events[0].company_name, "삼성전자")
        self.assertNotEqual(events[0].company_name, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_goal4_operational_seed_file_carries_source_task_failure_feedback_to_planner(self):
        seed_path = Path("docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl")
        events = _candidate_seed_events_from_config(
            config=ProductionShadowV4Config(
                as_of_date="2026-07-05",
                candidate_event_seed_path=str(seed_path),
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            as_of_date=date(2026, 7, 5),
        )
        event = next(
            item
            for item in events
            if item.structured_payload.get("target_archetype") == "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
        )

        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-07-05",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
        )
        full_thesis_context = context[event.candidate_event_id]["full_thesis_queue_context"]

        self.assertEqual(
            full_thesis_context["previous_source_task_primary_failure_axis"],
            "NO_SCORE_ELIGIBLE_REAL_CLAIM",
        )
        self.assertEqual(
            full_thesis_context["previous_source_task_repair_hint"],
            "FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM",
        )
        self.assertTrue(full_thesis_context["previous_source_task_top_source_classes"])
        self.assertTrue(full_thesis_context["previous_source_task_top_primitive_gaps"])
        self.assertTrue(full_thesis_context["source_task_repair_required"])
        self.assertIn(
            "KEEP_RESULT_PENDING_IF_ONLY_NON_ELIGIBLE_CLAIMS_EXIST",
            full_thesis_context["source_task_repair_actions"],
        )
        self.assertEqual(
            full_thesis_context["planner_failure_feedback"]["previous_source_task_primary_failure_axis"],
            "NO_SCORE_ELIGIBLE_REAL_CLAIM",
        )
        self.assertNotIn(
            "score_evidence_allowed_from_previous_source_task_failures",
            full_thesis_context["planner_failure_feedback"],
        )
        self._assert_no_forbidden_planner_context_keys(full_thesis_context)

        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id=context,
        )
        prompt_context = payload["events"][0]["existing_evidence_summary"]["full_thesis_queue_context"]
        self.assertEqual(
            prompt_context["planner_failure_feedback"]["previous_source_task_primary_failure_axis"],
            "NO_SCORE_ELIGIBLE_REAL_CLAIM",
        )
        self.assertTrue(any("previous_source_task_primary_failure_axis" in rule for rule in payload["rules"]))

    def test_goal4_all_archetype_followup_seed_order_is_preserved_in_live_planner_order(self):
        seed_path = Path("docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl")
        events = _candidate_seed_events_from_config(
            config=ProductionShadowV4Config(
                as_of_date="2026-07-05",
                candidate_event_seed_path=str(seed_path),
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            as_of_date=date(2026, 7, 5),
        )

        ordered = _planner_candidate_order(
            events=events,
            config=ProductionShadowV4Config(
                as_of_date="2026-07-05",
                candidate_event_seed_path=str(seed_path),
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            repo_root=".",
            as_of_date=date(2026, 7, 5),
        )

        self.assertEqual(
            [event.candidate_event_id for event in ordered[:30]],
            [event.candidate_event_id for event in events[:30]],
        )
        self.assertEqual(
            ordered[15].structured_payload.get("target_archetype"),
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(
            ordered[21].structured_payload.get("target_archetype"),
            "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        )

    def test_candidate_event_seed_path_skips_missing_or_zero_symbol_rows(self):
        with TemporaryDirectory() as tmp:
            seed_path = Path(tmp) / "bad_seed_rows.jsonl"
            rows = [
                {
                    "candidate_event_id": "CEV4-BAD-NONE",
                    "symbol": None,
                    "event_date": "2026-06-29",
                    "detected_at": "2026-06-29",
                    "source_family": "BadSeed",
                    "source_id": str(seed_path),
                    "research_brain_eligible": True,
                },
                {
                    "candidate_event_id": "CEV4-BAD-ZERO",
                    "symbol": "000000",
                    "event_date": "2026-06-29",
                    "detected_at": "2026-06-29",
                    "source_family": "BadSeed",
                    "source_id": str(seed_path),
                    "research_brain_eligible": True,
                },
                {
                    "candidate_event_id": "CEV4-GOOD",
                    "symbol": "660",
                    "company_name": "SK하이닉스",
                    "event_date": "2026-06-29",
                    "detected_at": "2026-06-29",
                    "source_family": "GoodSeed",
                    "source_id": str(seed_path),
                    "research_brain_eligible": True,
                },
                {
                    "candidate_event_id": "CEV4-GOAL4-ARCHETYPE",
                    "symbol": None,
                    "event_date": "2026-06-29",
                    "detected_at": "2026-06-29",
                    "source_family": "AllArchetypeRuntimeParityFollowUp",
                    "source_id": str(seed_path),
                    "event_type": "all_archetype_runtime_parity_follow_up_seed",
                    "target_archetype": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                    "target_symbol_mode": "ARCHETYPE_LEVEL_DISCOVERY",
                    "seed_role": "planner_input_only",
                    "structured_payload": {
                        "target_archetype": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                        "target_symbol_mode": "ARCHETYPE_LEVEL_DISCOVERY",
                        "seed_role": "planner_input_only",
                    },
                    "research_brain_eligible": True,
                    "score_evidence_allowed": False,
                    "stage_promotion_allowed_before_execution": False,
                },
            ]
            seed_path.write_text(
                "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
                encoding="utf-8",
            )

            events = _candidate_seed_events_from_config(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    candidate_event_seed_path=str(seed_path),
                ),
                as_of_date=date(2026, 6, 29),
            )

        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].candidate_event_id, "CEV4-GOOD")
        self.assertEqual(events[0].symbol, "000660")
        self.assertEqual(events[1].candidate_event_id, "CEV4-GOAL4-ARCHETYPE")
        self.assertEqual(events[1].symbol, "")
        self.assertEqual(events[1].company_name, "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY")
        self.assertEqual(events[1].issuer_directness, "INDUSTRY")

    def test_targetless_archetype_seed_does_not_execute_source_tasks(self):
        with TemporaryDirectory() as tmp:
            seed_path = Path(tmp) / "targetless_goal4_seed.jsonl"
            progress_path = Path(tmp) / "brain_web_runtime_progress.json"
            seed_path.write_text(
                json.dumps(
                    {
                        "candidate_event_id": "CEV4-GOAL4-ARCHETYPE-R13",
                        "symbol": None,
                        "event_date": "2026-06-29",
                        "detected_at": "2026-06-29",
                        "source_family": "AllArchetypeRuntimeParityFollowUp",
                        "source_id": str(seed_path),
                        "event_type": "all_archetype_runtime_parity_follow_up_seed",
                        "target_archetype": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
                        "target_symbol_mode": "ARCHETYPE_LEVEL_DISCOVERY",
                        "seed_role": "planner_input_only",
                        "structured_payload": {
                            "target_archetype": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
                            "target_symbol_mode": "ARCHETYPE_LEVEL_DISCOVERY",
                            "seed_role": "planner_input_only",
                        },
                        "research_brain_eligible": True,
                        "score_evidence_allowed": False,
                        "stage_promotion_allowed_before_execution": False,
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            with patch(
                "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
                return_value=(),
            ):
                result = run_research_brain_v4_production_shadow(
                    config=ProductionShadowV4Config(
                        as_of_date="2026-06-29",
                        planner_provider="fake",
                        source_acquisition="test_fake",
                        candidate_event_seed_path=str(seed_path),
                        universe_limit=1,
                        planner_success_limit=1,
                        planner_batch_size=1,
                        max_distinct_candidate_attempts=1,
                        retry_max=1,
                        runtime_progress_path=str(progress_path),
                        fake_provider_allowed=True,
                    ),
                    v1_archetype_matrix=load_v4_matrix(),
                )
            progress = json.loads(progress_path.read_text(encoding="utf-8"))

        self.assertEqual(result["planner_report"]["summary"]["planner_run_count"], 1)
        self.assertEqual(result["source_acquisition_report"]["summary"]["source_task_executed_count"], 0)
        row = result["watchlist_report"]["rows"][0]
        self.assertEqual(row["symbol"], "")
        self.assertEqual(row["score_valid_status"], "PENDING_EVIDENCE_OS_CLAIMS")
        self.assertIsNone(row["verified_score"])
        phases = [event["phase"] for event in progress["recent_events"]]
        self.assertIn("source_execution_skipped_target_materialization_required", phases)

    def test_runtime_progress_file_records_research_brain_phases(self):
        discovered = _planner_event_with_id("CE-UNIT-DISCOVERED", symbol="000660", company_name="SK하이닉스")
        with TemporaryDirectory() as tmp:
            progress_path = Path(tmp) / "brain_web_runtime_progress.json"
            with patch(
                "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
                return_value=(discovered,),
            ):
                result = run_research_brain_v4_production_shadow(
                    config=ProductionShadowV4Config(
                        as_of_date="2026-06-29",
                        planner_provider="none",
                        source_acquisition="live_official_first",
                        universe_limit=1,
                        planner_success_limit=1,
                        runtime_progress_path=str(progress_path),
                    ),
                    v1_archetype_matrix=load_v4_matrix(),
                )
            progress = json.loads(progress_path.read_text(encoding="utf-8"))

        self.assertEqual(result["planner_report"]["summary"]["planner_run_count"], 1)
        self.assertEqual(progress["schema_version"], "e2r_research_brain_v4_runtime_progress_v1")
        self.assertEqual(progress["status"], "COMPLETED")
        self.assertEqual(progress["latest_phase"], "completed")
        phases = [row["phase"] for row in progress["recent_events"]]
        self.assertIn("events_selected", phases)
        self.assertIn("planner_batch_start", phases)
        self.assertIn("planner_run_processing_end", phases)
        self.assertEqual(progress["config"]["planner_provider"], "none")

    def test_runtime_budget_exhaustion_marks_unplanned_events_pending(self):
        discovered = (
            _planner_event_with_id("CE-UNIT-DISCOVERED-A", symbol="000660", company_name="SK하이닉스"),
            _planner_event_with_id("CE-UNIT-DISCOVERED-B", symbol="005930", company_name="삼성전자"),
        )
        with TemporaryDirectory() as tmp:
            progress_path = Path(tmp) / "brain_web_runtime_progress.json"
            with patch(
                "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
                return_value=discovered,
            ):
                result = run_research_brain_v4_production_shadow(
                    config=ProductionShadowV4Config(
                        as_of_date="2026-06-29",
                        planner_provider="fake",
                        source_acquisition="test_fake",
                        universe_limit=2,
                        planner_success_limit=2,
                        planner_batch_size=1,
                        runtime_progress_path=str(progress_path),
                        runtime_budget_seconds=0.0,
                        fake_provider_allowed=True,
                    ),
                    v1_archetype_matrix=load_v4_matrix(),
                )
            progress = json.loads(progress_path.read_text(encoding="utf-8"))

        planner_runs = result["planner_runs"]
        self.assertEqual(len(planner_runs), 2)
        self.assertTrue(all(run.provider_error == "planner_not_attempted_after_runtime_budget_exhausted" for run in planner_runs))
        self.assertTrue(all(run.provider_name == "not_attempted_after_runtime_budget_exhausted" for run in planner_runs))
        self.assertEqual(result["source_acquisition_report"]["summary"]["source_task_executed_count"], 0)
        phases = [row["phase"] for row in progress["recent_events"]]
        self.assertIn("runtime_budget_exhausted", phases)
        self.assertEqual(progress["latest_phase"], "completed")
        self.assertTrue(progress["latest_event"]["runtime_budget_exhausted"])

    def test_runtime_budget_exhausted_after_source_execution_marks_remaining_events_pending(self):
        discovered = (
            _planner_event_with_id("CE-UNIT-DISCOVERED-A", symbol="000660", company_name="SK하이닉스"),
            _planner_event_with_id("CE-UNIT-DISCOVERED-B", symbol="005930", company_name="삼성전자"),
        )
        with TemporaryDirectory() as tmp:
            progress_path = Path(tmp) / "brain_web_runtime_progress.json"
            budget_check_count = {"value": 0}

            def budget_exhausted_after_source_started(*, config, started_at):
                budget_check_count["value"] += 1
                return budget_check_count["value"] >= 5

            with patch(
                "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
                return_value=discovered,
            ), patch(
                "e2r.research_brain.v4_production_orchestrator._runtime_budget_exhausted_v4",
                side_effect=budget_exhausted_after_source_started,
            ):
                result = run_research_brain_v4_production_shadow(
                    config=ProductionShadowV4Config(
                        as_of_date="2026-06-29",
                        planner_provider="fake",
                        source_acquisition="test_fake",
                        universe_limit=2,
                        planner_success_limit=1,
                        planner_batch_size=1,
                        max_distinct_candidate_attempts=1,
                        retry_max=1,
                        runtime_progress_path=str(progress_path),
                        runtime_budget_seconds=60.0,
                        fake_provider_allowed=True,
                    ),
                    v1_archetype_matrix=load_v4_matrix(),
                )
            progress = json.loads(progress_path.read_text(encoding="utf-8"))

        planner_runs = result["planner_runs"]
        pending_runs = [run for run in planner_runs if run.provider_name == "not_attempted_after_runtime_budget_exhausted"]
        self.assertEqual(len(pending_runs), 1)
        self.assertEqual(pending_runs[0].event.candidate_event_id, "CE-UNIT-DISCOVERED-B")
        self.assertGreater(result["source_acquisition_report"]["summary"]["source_task_executed_count"], 0)
        phases = [row["phase"] for row in progress["recent_events"]]
        self.assertIn("runtime_budget_exhausted_after_source_execution", phases)
        source_start_events = [row for row in progress["recent_events"] if row["phase"] == "source_execution_start"]
        self.assertTrue(source_start_events)
        source_start = source_start_events[0]
        self.assertEqual(
            source_start["source_task_count"],
            source_start["planner_generated_source_task_count"]
            + source_start["event_origin_source_task_count"]
            + source_start["mandatory_official_source_task_count"],
        )
        self.assertEqual(progress["latest_phase"], "completed")
        self.assertTrue(progress["latest_event"]["runtime_budget_exhausted"])

    def test_missing_external_web_plan_retry_preserves_source_execution_budget(self):
        discovered = (
            _planner_event_with_id("CE-UNIT-DISCOVERED-A", symbol="000660", company_name="SK하이닉스"),
        )
        with TemporaryDirectory() as tmp:
            progress_path = Path(tmp) / "brain_web_runtime_progress.json"
            with patch(
                "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
                return_value=discovered,
            ), patch(
                "e2r.research_brain.v4_production_orchestrator._runtime_budget_remaining_seconds_v4",
                return_value=1.0,
            ), patch(
                "e2r.research_brain.v4_production_orchestrator._retry_planner_for_missing_external_web_plan",
                side_effect=AssertionError("optional retry should preserve source execution budget"),
            ):
                result = run_research_brain_v4_production_shadow(
                    config=ProductionShadowV4Config(
                        as_of_date="2026-06-29",
                        planner_provider="fake",
                        source_acquisition="test_fake",
                        universe_limit=1,
                        planner_success_limit=1,
                        planner_batch_size=1,
                        max_distinct_candidate_attempts=1,
                        retry_max=1,
                        runtime_progress_path=str(progress_path),
                        runtime_budget_seconds=600.0,
                        claim_extractor_timeout_seconds=15.0,
                        fake_provider_allowed=True,
                    ),
                    v1_archetype_matrix=load_v4_matrix(),
                )
            progress = json.loads(progress_path.read_text(encoding="utf-8"))

        phases = [row["phase"] for row in progress["recent_events"]]
        self.assertIn("missing_external_web_plan_retry_skipped_insufficient_source_budget", phases)
        self.assertIn("source_execution_start", phases)
        self.assertGreater(result["source_acquisition_report"]["summary"]["source_task_executed_count"], 0)

    def test_cli_passes_candidate_event_seed_path_to_production_shadow_config(self):
        with TemporaryDirectory() as tmp:
            seed_path = Path(tmp) / "full_thesis_blocker_follow_up_seed_events.jsonl"
            output_dir = Path(tmp) / "out"
            seed_path.write_text(
                json.dumps(
                    {
                        "candidate_event_id": "CEV4-FTGAP-000660",
                        "symbol": "000660",
                        "company_name": "SK하이닉스",
                        "event_date": "2026-06-29",
                        "detected_at": "2026-06-29",
                        "source_family": "CensusFullThesisBlockerFollowUp",
                        "event_type": "full_thesis_blocker_follow_up_seed",
                        "structured_payload": {
                            "seed_role": "planner_input_only",
                            "follow_up_task_id": "FTGAP-UNIT",
                            "follow_up_primitive_gap": "hbm_capacity_pre_sold",
                            "follow_up_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        },
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )
            captured = {}

            def fake_run(*, config, v1_archetype_matrix, repo_root):
                captured["config"] = config
                return {
                    "candidate_report": {},
                    "planner_report": {},
                    "source_acquisition_report": {},
                    "evidence_extraction_audit": {},
                    "watchlist_report": {},
                    "static_audit": {},
                    "watchlist_items": (),
                    "planner_runs": (),
                    "executions": (),
                    "bundles": {},
                }

            with patch(
                "e2r.cli.run_research_brain_v4_production_shadow.run_research_brain_v4_production_shadow",
                side_effect=fake_run,
            ), patch(
                "e2r.cli.run_research_brain_v4_production_shadow.build_v4_readiness_verdict",
                return_value={"summary": {"final_status": "NOT_READY"}},
            ), patch(
                "e2r.cli.run_research_brain_v4_production_shadow.build_stability_audit_v4",
                return_value={},
            ), patch(
                "e2r.cli.run_research_brain_v4_production_shadow.build_source_quality_promotion_report_v4",
                return_value={},
            ), patch(
                "e2r.cli.run_research_brain_v4_production_shadow.build_a2_real_replay_claims_sample_v4",
                return_value={},
            ), patch(
                "e2r.cli.run_research_brain_v4_production_shadow.build_url_repair_queue_v4",
                return_value={},
            ), patch(
                "e2r.cli.run_research_brain_v4_production_shadow.build_research_memory_usage_audit_v4",
                return_value={},
            ), patch(
                "e2r.cli.run_research_brain_v4_production_shadow.write_research_brain_v4_report_bundle",
                return_value={"summary": output_dir / "summary.json"},
            ):
                from e2r.cli import run_research_brain_v4_production_shadow as cli

                status = cli.main(
                    [
                        "--as-of-date",
                        "2026-06-29",
                        "--planner-provider",
                        "none",
                        "--source-acquisition",
                        "live_full_bounded",
                        "--candidate-event-seed-path",
                        str(seed_path),
                        "--output-dir",
                        str(output_dir),
                        "--skip-multi-day",
                    ]
                )

        self.assertEqual(status, 0)
        self.assertEqual(captured["config"].candidate_event_seed_path, str(seed_path))

    def test_full_thesis_refresh_queue_consumes_selection_budget_before_daily_fill(self):
        seeds = tuple(
            replace(
                _planner_event_with_id(f"CEV4-FTQUEUE-{idx:06d}", symbol=f"{idx:06d}", company_name=f"큐종목{idx}"),
                source_family="CensusFullThesisQueue",
                source_id="queue://unit",
                event_type="full_thesis_refresh_seed",
                event_title="full thesis refresh seed",
                event_summary="planner input only",
                structured_payload={"seed_role": "planner_input_only"},
            )
            for idx in range(1, 5)
        )
        daily_events = (
            _planner_event_with_id("CE-UNIT-DART", symbol="114450", company_name="그린생명과학"),
            replace(
                _planner_event_with_id("CE-UNIT-CG", symbol="005930", company_name="삼성전자"),
                source_family="CompanyGuide",
                source_id="data/cache/company_guide/005930_recent_reports.json",
                event_type="report_radar",
            ),
        )

        selected = _select_unique_candidate_events((*seeds, *daily_events), limit=3)

        self.assertEqual([event.candidate_event_id for event in selected], [event.candidate_event_id for event in seeds[:3]])
        self.assertTrue(all(event.source_family == "CensusFullThesisQueue" for event in selected))

    def test_goal4_all_archetype_runtime_parity_seeds_consume_selection_budget_before_daily_fill(self):
        seeds = tuple(
            replace(
                _planner_event_with_id(
                    f"CEV4-RTATTEMPT-{idx:06d}",
                    symbol="",
                    company_name=f"C{idx:02d}_ARCHETYPE_DISCOVERY",
                ),
                source_family="AllArchetypeRuntimeParityFollowUp",
                source_id="docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl",
                event_type="all_archetype_runtime_parity_follow_up_seed",
                event_title="planner input only",
                event_summary="source-backed Evidence OS claim required before any production score/stage use",
                issuer_directness="INDUSTRY",
                structured_payload={
                    "seed_role": "planner_input_only",
                    "target_archetype": f"C{idx:02d}_ARCHETYPE_DISCOVERY",
                    "target_symbol_mode": "ARCHETYPE_LEVEL_DISCOVERY",
                },
            )
            for idx in range(1, 5)
        )
        daily_events = (
            _planner_event_with_id("CE-UNIT-DART", symbol="114450", company_name="그린생명과학"),
            replace(
                _planner_event_with_id("CE-UNIT-CG", symbol="005930", company_name="삼성전자"),
                source_family="CompanyGuide",
                source_id="data/cache/company_guide/005930_recent_reports.json",
                event_type="report_radar",
            ),
        )

        selected = _select_unique_candidate_events((*seeds, *daily_events), limit=3)

        self.assertEqual([event.candidate_event_id for event in selected], [event.candidate_event_id for event in seeds[:3]])
        self.assertTrue(all(event.source_family == "AllArchetypeRuntimeParityFollowUp" for event in selected))
        self.assertTrue(all(event.symbol == "" for event in selected))

    def test_full_thesis_seed_context_is_visible_to_planner_without_forcing_target_archetype(self):
        event = replace(
            _planner_event_with_id("CEV4-FTQUEUE-005930", symbol="005930", company_name="삼성전자"),
            source_family="CensusFullThesisQueue",
            source_id="queue://unit",
            event_type="full_thesis_refresh_seed",
            event_title="삼성전자 full thesis refresh seed",
            event_summary=(
                "planner input only. source_stage_signal=OFFICIAL_EVENT_WATCH; "
                "source_stage_decision_status=FINAL; source_base_stage=Stage1; "
                "missing_full_thesis_primitives=source_backed_primitive_coverage_required"
            ),
            structured_payload={
                "seed_role": "planner_input_only",
                "queue_task_id": "FTQUEUE-UNIT-005930",
                "source_stage_scope": "CENSUS_EVENT_BOARD",
                "source_primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                "source_secondary_archetypes": [],
                "source_large_sector_id": "메모리/HBM",
                "source_base_stage": "Stage1",
                "source_stage_signal": "OFFICIAL_EVENT_WATCH",
                "source_stage_decision_status": "FINAL",
                "source_missing_primitives": ["repeat_evidence_family", "cash_or_revision_conversion"],
                "source_material_gap_ids": ["multi_source_confirmation"],
                "source_failed_stage_gates": ["missing_green_bridge"],
                "source_accepted_claim_ids": ["CLM-UNIT"],
                "source_score_contribution_ids": ["SCON-UNIT"],
                "target_archetype_status": "BRAIN_HYPOTHESIS_REQUIRED",
                "target_archetype": None,
                "missing_full_thesis_primitives": [
                    "full_thesis_archetype_hypothesis_required",
                    "source_backed_primitive_coverage_required",
                ],
                "preferred_source_classes": ["DART", "IssuerIR"],
                "fallback_source_classes": ["TrustedNews", "ReportPDF"],
                "forbidden_source_classes": ["snippet_only_score", "unbounded_general_search"],
                "official_first_required": True,
            },
        )

        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
        )

        full_thesis_context = context[event.candidate_event_id]["full_thesis_queue_context"]
        self.assertNotIn("source_stage_signal", context[event.candidate_event_id]["event_summary_preview"])
        self.assertNotIn("source_stage_decision_status", context[event.candidate_event_id]["event_summary_preview"])
        self.assertNotIn("source_base_stage", context[event.candidate_event_id]["event_summary_preview"])
        self.assertNotIn("Stage1", context[event.candidate_event_id]["event_summary_preview"])
        self.assertIn(
            "missing_full_thesis_primitives=source_backed_primitive_coverage_required",
            context[event.candidate_event_id]["event_summary_preview"],
        )
        self.assertEqual(full_thesis_context["source_primary_archetype"], "C05_EPC_MEGA_CONTRACT_MARGIN_GAP")
        self.assertEqual(full_thesis_context["source_large_sector_id"], "메모리/HBM")
        self.assertEqual(full_thesis_context["source_missing_primitives"], ["repeat_evidence_family", "cash_or_revision_conversion"])
        self.assertEqual(full_thesis_context["source_material_gap_ids"], ["multi_source_confirmation"])
        self.assertEqual(full_thesis_context["target_archetype_status"], "BRAIN_HYPOTHESIS_REQUIRED")
        self.assertIsNone(full_thesis_context["target_archetype"])
        self.assertTrue(full_thesis_context["official_first_required"])
        self.assertNotIn("source_base_stage", full_thesis_context)
        self.assertNotIn("source_stage_signal", full_thesis_context)
        self.assertNotIn("source_stage_decision_status", full_thesis_context)
        self.assertNotIn("source_score_contribution_ids", full_thesis_context)
        self._assert_no_forbidden_planner_context_keys(full_thesis_context)

    def test_full_thesis_blocker_follow_up_seed_context_is_visible_without_score_stage_context(self):
        event = replace(
            _planner_event_with_id("CEV4-FTGAP-000660", symbol="000660", company_name="SK하이닉스"),
            source_family="CensusFullThesisBlockerFollowUp",
            source_id="queue://full_thesis_blocker_follow_up_source_tasks.jsonl",
            event_type="full_thesis_blocker_follow_up_seed",
            event_title="SK하이닉스 full thesis primitive follow-up seed",
            event_summary=(
                "planner input only. follow_up_task_id=FTGAP-UNIT; "
                "archetype_id=C06_HBM_MEMORY_CUSTOMER_CAPACITY; "
                "primitive_gap=hbm_capacity_pre_sold; source-backed Evidence OS claim required before promotion"
            ),
            structured_payload={
                "seed_role": "planner_input_only",
                "follow_up_task_id": "FTGAP-UNIT",
                "follow_up_origin": "full_thesis_green_gate_blocker_follow_up",
                "follow_up_primitive_gap": "hbm_capacity_pre_sold",
                "follow_up_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "target_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "target_archetype_status": "GREEN_GATE_BLOCKER_FOLLOW_UP",
                "primitive_gap": "hbm_capacity_pre_sold",
                "present_primitives": ["named_customer_or_customer_quality"],
                "missing_green_primitives": ["hbm_capacity_constraint", "hbm_capacity_pre_sold"],
                "preferred_source_classes": ["DART", "KIND", "KRX", "IssuerIR", "CompanyGuide"],
                "fallback_source_classes": ["TrustedNews", "ReportPDF", "NaverSearch", "GeneralWebSearch"],
                "forbidden_source_classes": ["snippet_only_score", "unbounded_general_search"],
                "official_first_required": True,
                "llm_query_required": True,
                "llm_query_allowed": True,
                "general_search_allowed": True,
                "hardcoded_query_count": 0,
                "hardcoded_queries": [],
                "query_intents": [],
                "success_condition": (
                    "Create at least one accepted Evidence OS claim for primitive `hbm_capacity_pre_sold` "
                    "on symbol `000660`."
                ),
                "expected_claim_schema": {
                    "schema_version": "e2r_expected_runtime_parity_claim_v1",
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "primitive_id": "hbm_capacity_pre_sold",
                    "symbol": "000660",
                    "target_scope_status": "DIRECT",
                    "temporal_status": "CURRENT_OR_AS_OF_VALID",
                    "anchor_status": "VERIFIED_SOURCE_ANCHOR",
                    "mapping_status": "ACCEPTED",
                    "required_claim_status": "ACCEPTED_FOR_SCORE",
                    "score_forbidden_until_claim_accepted": True,
                },
                "fallback_if_not_found": "PENDING_MATERIAL_GAP",
                "date_window": {"end": "2026-06-29", "lookback_days": 365},
                "max_queries": 3,
                "max_candidates": 20,
                "max_fetches": 3,
                "max_queries_per_task": 3,
                "max_candidates_per_query": 20,
                "max_fetches_per_task": 3,
                "stop_condition": {
                    "accepted_claim_count": 1,
                    "counter_claim_check_done": True,
                    "source_budget_exhausted_status": "SOURCE_PENDING",
                },
            },
        )

        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
        )

        full_thesis_context = context[event.candidate_event_id]["full_thesis_queue_context"]
        self.assertEqual(full_thesis_context["follow_up_task_id"], "FTGAP-UNIT")
        self.assertEqual(full_thesis_context["follow_up_primitive_gap"], "hbm_capacity_pre_sold")
        self.assertEqual(full_thesis_context["follow_up_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(full_thesis_context["target_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(full_thesis_context["target_archetype_status"], "GREEN_GATE_BLOCKER_FOLLOW_UP")
        self.assertEqual(full_thesis_context["primitive_gap"], "hbm_capacity_pre_sold")
        self.assertEqual(full_thesis_context["present_primitives"], ["named_customer_or_customer_quality"])
        self.assertEqual(full_thesis_context["missing_green_primitives"], ["hbm_capacity_constraint", "hbm_capacity_pre_sold"])
        self.assertEqual(full_thesis_context["preferred_source_classes"][0], "DART")
        self.assertTrue(full_thesis_context["official_first_required"])
        self.assertTrue(full_thesis_context["llm_query_required"])
        self.assertTrue(full_thesis_context["general_search_allowed"])
        self.assertEqual(full_thesis_context["hardcoded_query_count"], 0)
        self.assertEqual(full_thesis_context["query_intents"], [])
        self.assertIn("accepted Evidence OS claim", full_thesis_context["success_condition"])
        self.assertEqual(full_thesis_context["fallback_if_not_found"], "PENDING_MATERIAL_GAP")
        self.assertEqual(full_thesis_context["expected_claim_schema"]["primitive_id"], "hbm_capacity_pre_sold")
        self.assertEqual(full_thesis_context["expected_claim_schema"]["target_scope_status"], "DIRECT")
        self.assertNotIn("score_forbidden_until_claim_accepted", full_thesis_context["expected_claim_schema"])
        self.assertEqual(full_thesis_context["max_queries"], 3)
        self.assertEqual(full_thesis_context["max_fetches"], 3)
        self.assertNotIn("score_evidence_allowed", full_thesis_context)
        self.assertNotIn("stage_promotion_allowed_before_execution", full_thesis_context)
        self._assert_no_forbidden_planner_context_keys(full_thesis_context)

    def test_goal4_repair_feedback_seed_context_is_visible_to_planner_without_score_context(self):
        event = replace(
            _planner_event_with_id("CEV4-RTATTEMPT-C08", symbol="058470", company_name="리노공업"),
            source_family="AllArchetypeRuntimeParityFollowUp",
            source_id="docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl",
            event_type="all_archetype_runtime_parity_follow_up_seed",
            event_title="C08 runtime parity repair seed",
            event_summary=(
                "planner input only. archetype_id=C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY; "
                "primitive_gap=repeat_order_confirmed; previous_claim_failure_primary_mode="
                "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE"
            ),
            raw_reason_codes=(
                "GOAL4_RUNTIME_PARITY_FOLLOW_UP",
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM",
                "repeat_order_confirmed",
                "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE",
            ),
            structured_payload={
                "seed_role": "planner_input_only",
                "follow_up_task_id": "RTTASK-C08-UNIT",
                "target_archetype": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                "target_archetype_status": "RUNTIME_PARITY_FOLLOW_UP_REQUIRED",
                "primitive_gap": "repeat_order_confirmed",
                "query_intents": [
                    "Ask the LLM planner for bounded official-first queries that verify current direct evidence.",
                    "Previous runtime attempt failed before accepted claim creation.",
                ],
                "success_condition": (
                    "Create at least one accepted Evidence OS claim for primitive `repeat_order_confirmed` "
                    "on symbol `058470`."
                ),
                "expected_claim_schema": {
                    "schema_version": "e2r_expected_runtime_parity_claim_v1",
                    "archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                    "primitive_id": "repeat_order_confirmed",
                    "symbol": "058470",
                    "target_scope_status": "DIRECT",
                    "temporal_status": "CURRENT_OR_AS_OF_VALID",
                    "anchor_status": "VERIFIED_SOURCE_ANCHOR",
                    "mapping_status": "ACCEPTED",
                    "required_claim_status": "ACCEPTED_FOR_SCORE",
                    "score_forbidden_until_claim_accepted": True,
                },
                "fallback_if_not_found": "SOURCE_REPAIR_REQUIRED",
                "previous_claim_failure_primary_mode": "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE",
                "previous_claim_failure_repair_hint": "REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE",
                "previous_claim_failure_top_modes": [
                    {"mode": "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE", "count": 40},
                    {"mode": "PRIMITIVE_MAPPING_REJECTED", "count": 53},
                ],
                "previous_seed_materialization_primary_failure_axis": "PRIMITIVE_GAP_UNSATISFIED",
                "previous_seed_materialization_repair_hint": "FIND_PRIMITIVE_SPECIFIC_CLAIM_NOT_GENERIC_CONTEXT",
                "previous_seed_materialization_top_failure_axes": [
                    {"axis": "PRIMITIVE_GAP_UNSATISFIED", "count": 17},
                    {"axis": "NO_SCORE_ELIGIBLE_REAL_CLAIM", "count": 16},
                ],
                "previous_seed_materialization_status_counts": {
                    "ACCEPTED_CLAIM_NOT_CREATED": 3,
                },
                "seed_materialization_repair_required": True,
                "seed_materialization_repair_actions": [
                    "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_SECTION",
                    "DO_NOT_REUSE_GENERIC_CONTEXT_AS_GAP_CLOSURE",
                ],
                "previous_source_task_primary_failure_axis": "NO_SCORE_ELIGIBLE_REAL_CLAIM",
                "previous_source_task_repair_hint": "FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM",
                "previous_source_task_top_source_classes": [
                    {"source_class": "BrokerReportPDF", "count": 4},
                    {"source_class": "CompanyNewsroom", "count": 2},
                ],
                "previous_source_task_top_primitive_gaps": [
                    {"primitive_gap": "repeat_order_confirmed", "count": 5},
                    {"primitive_gap": "customer_quality", "count": 1},
                ],
                "previous_source_task_failure_sample_refs": [
                    {
                        "task_id": "RSTASK-C08-UNIT",
                        "source_class": "BrokerReportPDF",
                        "primitive_gap": "repeat_order_confirmed",
                        "failure_axes": ["NO_SCORE_ELIGIBLE_REAL_CLAIM"],
                        "not_eligible_reasons": ["no_direct_target_claim"],
                    }
                ],
                "source_task_repair_required": True,
                "source_task_repair_actions": [
                    "FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM",
                    "KEEP_RESULT_PENDING_IF_ONLY_NON_ELIGIBLE_CLAIMS_EXIST",
                ],
                "source_route_repair_required": True,
                "source_route_repair_actions": [
                    "DO_NOT_ACCEPT_GENERIC_DISCLOSURE_PROFILE_AS_PRIMITIVE_EVIDENCE",
                    "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_OR_SECTION_ROUTE",
                    "FETCH_FULL_SOURCE_ANCHOR_BEFORE_MAPPING_RETRY",
                ],
                "planner_failure_feedback": {
                    "previous_claim_failure_primary_mode": "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE",
                    "previous_claim_failure_repair_hint": "REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE",
                    "previous_claim_failure_top_modes": [
                        {"mode": "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE", "count": 40},
                    ],
                    "previous_top_claim_rejection_reasons": [
                        {"reason": "primitive_mapping_rejected", "count": 263},
                    ],
                    "previous_seed_materialization_primary_failure_axis": "PRIMITIVE_GAP_UNSATISFIED",
                    "previous_seed_materialization_repair_hint": "FIND_PRIMITIVE_SPECIFIC_CLAIM_NOT_GENERIC_CONTEXT",
                    "previous_seed_materialization_top_failure_axes": [
                        {"axis": "PRIMITIVE_GAP_UNSATISFIED", "count": 17},
                    ],
                    "previous_seed_materialization_status_counts": {
                        "ACCEPTED_CLAIM_NOT_CREATED": 3,
                    },
                    "previous_seed_materialization_failure_sample_refs": [
                        {
                            "candidate_event_id": "CEV4-RTATTEMPT-UNIT",
                            "target_primitive_gap": "repeat_order_confirmed",
                            "source_task_primary_failure_axis": "PRIMITIVE_GAP_UNSATISFIED",
                        }
                    ],
                    "source_route_repair_actions": [
                        "DO_NOT_ACCEPT_GENERIC_DISCLOSURE_PROFILE_AS_PRIMITIVE_EVIDENCE",
                        "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_OR_SECTION_ROUTE",
                    ],
                    "seed_materialization_repair_actions": [
                        "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_SECTION",
                        "DO_NOT_REUSE_GENERIC_CONTEXT_AS_GAP_CLOSURE",
                    ],
                    "previous_source_task_primary_failure_axis": "NO_SCORE_ELIGIBLE_REAL_CLAIM",
                    "previous_source_task_repair_hint": "FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM",
                    "previous_source_task_top_source_classes": [
                        {"source_class": "BrokerReportPDF", "count": 4},
                    ],
                    "previous_source_task_top_primitive_gaps": [
                        {"primitive_gap": "repeat_order_confirmed", "count": 5},
                    ],
                    "previous_source_task_failure_sample_refs": [
                        {
                            "task_id": "RSTASK-C08-UNIT",
                            "source_class": "BrokerReportPDF",
                            "primitive_gap": "repeat_order_confirmed",
                            "failure_axes": ["NO_SCORE_ELIGIBLE_REAL_CLAIM"],
                        }
                    ],
                    "source_task_repair_actions": [
                        "FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM",
                        "KEEP_RESULT_PENDING_IF_ONLY_NON_ELIGIBLE_CLAIMS_EXIST",
                    ],
                    "score_evidence_allowed_from_previous_rejected_claims": False,
                    "score_evidence_allowed_from_previous_seed_failures": False,
                    "score_evidence_allowed_from_previous_source_task_failures": False,
                    "primitive_gap": "repeat_order_confirmed",
                },
            },
        )

        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
        )

        full_thesis_context = context[event.candidate_event_id]["full_thesis_queue_context"]
        self.assertEqual(
            full_thesis_context["previous_claim_failure_primary_mode"],
            "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE",
        )
        self.assertEqual(
            full_thesis_context["previous_claim_failure_repair_hint"],
            "REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE",
        )
        self.assertTrue(full_thesis_context["source_route_repair_required"])
        self.assertIn(
            "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_OR_SECTION_ROUTE",
            full_thesis_context["source_route_repair_actions"],
        )
        self.assertEqual(
            full_thesis_context["previous_seed_materialization_primary_failure_axis"],
            "PRIMITIVE_GAP_UNSATISFIED",
        )
        self.assertEqual(
            full_thesis_context["previous_seed_materialization_repair_hint"],
            "FIND_PRIMITIVE_SPECIFIC_CLAIM_NOT_GENERIC_CONTEXT",
        )
        self.assertTrue(full_thesis_context["seed_materialization_repair_required"])
        self.assertIn(
            "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_SECTION",
            full_thesis_context["seed_materialization_repair_actions"],
        )
        self.assertEqual(
            full_thesis_context["previous_source_task_primary_failure_axis"],
            "NO_SCORE_ELIGIBLE_REAL_CLAIM",
        )
        self.assertEqual(
            full_thesis_context["previous_source_task_repair_hint"],
            "FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM",
        )
        self.assertTrue(full_thesis_context["source_task_repair_required"])
        self.assertIn(
            "KEEP_RESULT_PENDING_IF_ONLY_NON_ELIGIBLE_CLAIMS_EXIST",
            full_thesis_context["source_task_repair_actions"],
        )
        self.assertEqual(
            full_thesis_context["planner_failure_feedback"]["primitive_gap"],
            "repeat_order_confirmed",
        )
        self.assertEqual(
            full_thesis_context["planner_failure_feedback"]["previous_seed_materialization_primary_failure_axis"],
            "PRIMITIVE_GAP_UNSATISFIED",
        )
        self.assertEqual(
            full_thesis_context["planner_failure_feedback"]["previous_source_task_primary_failure_axis"],
            "NO_SCORE_ELIGIBLE_REAL_CLAIM",
        )
        self.assertIn("accepted Evidence OS claim", full_thesis_context["success_condition"])
        self.assertEqual(full_thesis_context["fallback_if_not_found"], "SOURCE_REPAIR_REQUIRED")
        self.assertEqual(full_thesis_context["expected_claim_schema"]["primitive_id"], "repeat_order_confirmed")
        self.assertEqual(full_thesis_context["expected_claim_schema"]["target_scope_status"], "DIRECT")
        self.assertNotIn("score_forbidden_until_claim_accepted", full_thesis_context["expected_claim_schema"])
        self.assertNotIn(
            "score_evidence_allowed_from_previous_rejected_claims",
            full_thesis_context["planner_failure_feedback"],
        )
        self.assertNotIn(
            "score_evidence_allowed_from_previous_seed_failures",
            full_thesis_context["planner_failure_feedback"],
        )
        self.assertNotIn(
            "score_evidence_allowed_from_previous_source_task_failures",
            full_thesis_context["planner_failure_feedback"],
        )
        self._assert_no_forbidden_planner_context_keys(full_thesis_context)

        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id=context,
        )
        prompt_context = payload["events"][0]["existing_evidence_summary"]["full_thesis_queue_context"]
        self.assertEqual(
            prompt_context["planner_failure_feedback"]["previous_claim_failure_primary_mode"],
            "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE",
        )
        self.assertEqual(
            prompt_context["planner_failure_feedback"]["previous_seed_materialization_primary_failure_axis"],
            "PRIMITIVE_GAP_UNSATISFIED",
        )
        self.assertEqual(
            prompt_context["planner_failure_feedback"]["previous_source_task_primary_failure_axis"],
            "NO_SCORE_ELIGIBLE_REAL_CLAIM",
        )
        self.assertTrue(any("planner_failure_feedback" in rule for rule in payload["rules"]))
        self.assertTrue(any("previous_seed_materialization_primary_failure_axis" in rule for rule in payload["rules"]))
        self.assertTrue(any("previous_source_task_primary_failure_axis" in rule for rule in payload["rules"]))

    def test_existing_evidence_summary_removes_forbidden_score_stage_keys_recursively(self):
        event = replace(
            _planner_event(),
            structured_payload={
                "seed_role": "planner_input_only",
                "queue_task_id": "FTQUEUE-UNIT-005930",
                "source_base_stage": "Stage2-Watch",
                "source_score_contribution_ids": ["SCON-UNIT"],
                "source_missing_primitives": ["cash_or_revision_conversion"],
                "source_material_gap_ids": ["multi_source_confirmation"],
            },
        )
        rerouted_feedback = (
            {
                "requested_primitive_gap": "hbm_capacity_pre_sold",
                "accepted_primitive_ids": ["medium_term_revision_visibility"],
                "primitive_gap_unsatisfied_ids": ["hbm_capacity_pre_sold"],
                "score": 92.0,
                "stage": "3-Green",
                "nested": {
                    "current_score_eligible": True,
                    "target_stage": "3-Green",
                    "safe_reason": "rerouted claim did not close original primitive",
                },
            },
        )
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_official_first",
            ),
            rerouted_claim_feedback_by_event_id={event.candidate_event_id: rerouted_feedback},
        )
        summary = context[event.candidate_event_id]

        self._assert_no_forbidden_planner_context_keys(summary)
        self.assertEqual(
            summary["rerouted_claim_feedback"][0]["requested_primitive_gap"],
            "hbm_capacity_pre_sold",
        )
        self.assertEqual(
            summary["rerouted_claim_feedback"][0]["nested"]["safe_reason"],
            "rerouted claim did not close original primitive",
        )
        self.assertNotIn("source_base_stage", summary["structured_payload_keys"])
        self.assertNotIn("source_score_contribution_ids", summary["structured_payload_keys"])

    def test_prompt_payload_sanitizes_direct_existing_evidence_summary_input(self):
        event = _planner_event()
        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={
                event.candidate_event_id: {
                    "rerouted_claim_feedback": [
                        {
                            "requested_primitive_gap": "hbm_capacity_pre_sold",
                            "stage": "3-Green",
                            "score": 99.0,
                            "nested": {"current_score_eligible": True, "safe_note": "keep"},
                        }
                    ],
                    "full_thesis_queue_context": {
                        "source_base_stage": "Stage1",
                        "source_material_gap_ids": ["multi_source_confirmation"],
                    },
                }
            },
        )
        summary = payload["events"][0]["existing_evidence_summary"]

        self._assert_no_forbidden_planner_context_keys(summary)
        self.assertEqual(
            summary["rerouted_claim_feedback"][0]["requested_primitive_gap"],
            "hbm_capacity_pre_sold",
        )
        self.assertEqual(summary["rerouted_claim_feedback"][0]["nested"]["safe_note"], "keep")
        self.assertEqual(
            summary["full_thesis_queue_context"]["source_material_gap_ids"],
            ["multi_source_confirmation"],
        )

    def test_prompt_payload_sanitizes_candidate_event_score_stage_context(self):
        event = replace(
            _planner_event_with_id("CEV4-FTQUEUE-005930", symbol="005930", company_name="삼성전자"),
            source_family="CensusFullThesisQueue",
            event_summary=(
                "planner input only. source_stage_signal=OFFICIAL_EVENT_WATCH; "
                "source_stage_decision_status=FINAL; source_base_stage=Stage1; "
                "missing_full_thesis_primitives=source_backed_primitive_coverage_required"
            ),
            raw_reason_codes=(
                "FULL_THESIS_REFRESH_QUEUE",
                "event_board_non_stage0_needs_full_thesis_refresh",
                "P2_EVENT_WATCH_REFRESH",
            ),
            structured_payload={
                "queue_task_id": "FTQUEUE-UNIT-005930",
                "source_base_stage": "Stage1",
                "source_stage_signal": "OFFICIAL_EVENT_WATCH",
                "source_stage_decision_status": "FINAL",
                "source_score_contribution_ids": ["SCON-UNIT"],
                "source_missing_primitives": ["cash_or_revision_conversion"],
                "missing_full_thesis_primitives": ["source_backed_primitive_coverage_required"],
            },
        )

        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={event.candidate_event_id: {}},
        )
        candidate = payload["events"][0]["candidate_event"]

        self._assert_no_forbidden_planner_context_keys(candidate)
        self.assertNotIn("source_stage_signal", candidate["event_summary"])
        self.assertNotIn("source_stage_decision_status", candidate["event_summary"])
        self.assertNotIn("source_base_stage", candidate["event_summary"])
        self.assertNotIn("Stage1", candidate["event_summary"])
        self.assertIn(
            "missing_full_thesis_primitives=source_backed_primitive_coverage_required",
            candidate["event_summary"],
        )
        self.assertEqual(candidate["raw_reason_codes"], ["FULL_THESIS_REFRESH_QUEUE", "P2_EVENT_WATCH_REFRESH"])
        self.assertEqual(
            candidate["structured_payload"],
            {
                "queue_task_id": "FTQUEUE-UNIT-005930",
                "source_missing_primitives": ["cash_or_revision_conversion"],
                "missing_full_thesis_primitives": ["source_backed_primitive_coverage_required"],
            },
        )

    def test_fake_provider_is_tests_only_unless_explicitly_allowed(self):
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="fake",
                source_acquisition="frozen_real_source_snapshot",
            ).validate()
        ProductionShadowV4Config(
            as_of_date="2026-06-29",
            planner_provider="fake",
            source_acquisition="frozen_real_source_snapshot",
            fake_provider_allowed=True,
        ).validate()

    def test_unbounded_top_results_and_retry_are_rejected(self):
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", top_results=None).validate()  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", retry_max=None).validate()  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", retry_max=0).validate()
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", max_source_tasks_per_plan=0).validate()
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", accepted_claim_target=-1).validate()
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", max_distinct_candidate_attempts=0).validate()
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", claim_extractor_timeout_seconds=0).validate()

    def test_real_planner_success_limit_skips_failed_attempts_and_continues(self):
        first = _planner_event_with_id("CE-UNIT-FIRST-FAIL", symbol="005930", company_name="삼성전자")
        second = _planner_event_with_id("CE-UNIT-SECOND-SUCCESS", symbol="000660", company_name="SK하이닉스")
        provider = _MissingFirstRealPlannerProvider(success_event_id=second.candidate_event_id)

        with patch(
            "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
            return_value=(first, second),
        ):
            result = run_research_brain_v4_production_shadow(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    planner_provider="real",
                    source_acquisition="frozen_real_source_snapshot",
                    universe_limit=2,
                    planner_success_limit=1,
                    planner_batch_size=1,
                ),
                v1_archetype_matrix=load_v4_matrix(),
                planner_provider=provider,
            )

        planner_runs = result["planner_runs"]
        self.assertEqual([run.event.candidate_event_id for run in planner_runs], [first.candidate_event_id, second.candidate_event_id])
        self.assertFalse(planner_runs[0].real_provider_success)
        self.assertEqual(planner_runs[0].provider_error, "planner_output_missing_for_candidate")
        self.assertTrue(planner_runs[1].real_provider_success)
        self.assertEqual(result["planner_report"]["summary"]["real_provider_success_count"], 1)

    def test_codex_planner_forbidden_self_check_rejects_row_without_aborting_batch(self):
        first = _planner_event_with_id("CE-UNIT-FORBIDDEN", symbol="005930", company_name="삼성전자")
        second = _planner_event_with_id("CE-UNIT-VALID", symbol="000660", company_name="SK하이닉스")
        invalid = _planner_output(query_intents=("삼성전자 HBM 확인",), fallback_source_classes=("TrustedNews",)).to_dict()
        invalid["candidate_event_id"] = first.candidate_event_id
        invalid["planner_self_check"] = {
            "score_keys_present": True,
            "stage_keys_present": False,
            "future_outcome_used": False,
        }
        valid = _planner_output(query_intents=("SK하이닉스 HBM 확인",), fallback_source_classes=("TrustedNews",)).to_dict()
        valid["candidate_event_id"] = second.candidate_event_id
        valid["must_verify_primitives"] = ["customer_preorder_or_allocation"]
        valid["source_task_drafts"][0]["primitive_gap"] = "customer_preorder_or_allocation"

        def fake_codex(command, *, prompt, timeout):
            return subprocess.CompletedProcess(
                list(command),
                0,
                json.dumps({"plans": [invalid, valid]}, ensure_ascii=False),
                "",
            )

        provider = CodexCLIPlannerProviderV4(working_directory=".")
        with patch("e2r.research_brain.v4_planner_runtime._run_codex_command", side_effect=fake_codex):
            runs = run_planner_provider_v4(
                provider=provider,
                events=(first, second),
                memory_cards=load_v4_cards(),
                existing_evidence_by_event_id={},
            )

        self.assertEqual(len(runs), 2)
        self.assertTrue(runs[0].rejected_by_validator)
        self.assertIn("forbidden score/stage keys", runs[0].provider_error or "")
        self.assertFalse(runs[0].real_provider_success)
        self.assertTrue(runs[1].real_provider_success)

    def test_codex_planner_rejects_non_codex_subprocess_configuration(self):
        for kwargs in (
            {"codex_command": "local-provider"},
            {"profile": "local-profile"},
            {"extra_args": ("--config", "model_provider=local")},
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(TypeError):
                CodexCLIPlannerProviderV4(**kwargs)

        provider = CodexCLIPlannerProviderV4()
        command = provider._command(
            schema_path=Path("/tmp/schema.json"),
            output_path=Path("/tmp/output.json"),
        )
        self.assertIn("--ignore-user-config", command)
        self.assertIn("--ignore-rules", command)

    def test_runtime_planner_leaf_flush_survives_source_execution_exception(self):
        event = _planner_event_with_id("CE-UNIT-FLUSH", symbol="005930", company_name="삼성전자")
        provider = _RetryPlannerProvider(
            _planner_output(
                query_intents=("삼성전자 HBM 고객 배정",),
                fallback_source_classes=("TrustedNews",),
            )
        )

        with TemporaryDirectory() as tmpdir:
            output_root = Path(tmpdir) / "out"
            with patch(
                "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
                return_value=(event,),
            ), patch(
                "e2r.research_brain.v4_production_orchestrator.execute_source_tasks_with_evidence_os_v4",
                side_effect=RuntimeError("unit source boom"),
            ):
                with self.assertRaisesRegex(RuntimeError, "unit source boom"):
                    run_research_brain_v4_production_shadow(
                        config=ProductionShadowV4Config(
                            as_of_date="2026-06-29",
                            planner_provider="real",
                            source_acquisition="frozen_real_source_snapshot",
                            universe_limit=1,
                            planner_success_limit=1,
                            planner_batch_size=1,
                            runtime_progress_path=str(output_root / "brain_web_runtime_progress.json"),
                        ),
                        v1_archetype_matrix=load_v4_matrix(),
                        planner_provider=provider,
                    )

            planner_path = output_root / "planner_runs.jsonl"
            self.assertTrue(planner_path.exists())
            rows = [json.loads(line) for line in planner_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["event"]["candidate_event_id"], event.candidate_event_id)
            self.assertTrue(rows[0]["real_provider_success"])

    def test_real_planner_does_not_exceed_distinct_candidate_attempt_cap_when_failures_repeat(self):
        events = tuple(
            _planner_event_with_id(f"CE-UNIT-FAIL-{index}", symbol=f"{index:06d}", company_name=f"실패기업{index}")
            for index in range(5)
        )
        provider = _NoSuccessRealPlannerProvider()

        with patch(
            "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
            return_value=events,
        ):
            result = run_research_brain_v4_production_shadow(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    planner_provider="real",
                    source_acquisition="frozen_real_source_snapshot",
                    universe_limit=5,
                    planner_success_limit=5,
                    planner_batch_size=1,
                    max_distinct_candidate_attempts=2,
                ),
                v1_archetype_matrix=load_v4_matrix(),
                planner_provider=provider,
            )

        planner_runs = result["planner_runs"]
        real_attempts = [run for run in planner_runs if run.provider_name == provider.provider_name]
        not_attempted = [run for run in planner_runs if run.provider_error == "planner_not_attempted_after_real_planner_limit"]
        self.assertEqual([run.event.candidate_event_id for run in real_attempts], ["CE-UNIT-FAIL-0", "CE-UNIT-FAIL-1"])
        self.assertEqual(len(not_attempted), 3)
        self.assertEqual(result["planner_report"]["summary"]["real_provider_attempt_count"], 2)
        self.assertEqual(result["planner_report"]["summary"]["real_provider_success_count"], 0)

    def test_auto_claim_extractor_uses_llm_for_live_full_bounded(self):
        config = ProductionShadowV4Config(
            as_of_date="2026-06-29",
            planner_provider="real",
            source_acquisition="live_full_bounded",
            claim_extractor_provider="auto",
            claim_extractor_timeout_seconds=12.0,
        )
        extractor = _claim_extractor_for_config(config=config, repo_root=".")
        self.assertIsInstance(extractor.provider, CodexCLIExtractorProvider)
        self.assertEqual(extractor.provider.timeout_seconds, 12.0)

    def test_auto_claim_extractor_keeps_replay_on_rule_fallback(self):
        config = ProductionShadowV4Config(
            as_of_date="2026-06-29",
            planner_provider="real",
            source_acquisition="frozen_real_source_snapshot",
            claim_extractor_provider="auto",
        )
        extractor = _claim_extractor_for_config(config=config, repo_root=".")
        self.assertIsInstance(extractor.provider, RuleFallbackExtractorProvider)

    def test_explicit_claim_extractor_provider_is_validated(self):
        ProductionShadowV4Config(
            as_of_date="2026-06-29",
            claim_extractor_provider="codex_cli",
        ).validate()
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(
                as_of_date="2026-06-29",
                claim_extractor_provider="bad_provider",
            ).validate()

    def test_live_full_bounded_retries_planner_when_web_plan_is_missing(self):
        event = _planner_event()
        initial = _planner_output(query_intents=(), fallback_source_classes=("KIND",))
        retry = _planner_output(
            query_intents=("삼성전자 HBM 고객 배정 qualification",),
            fallback_source_classes=("TrustedNews",),
        )
        provider = _RetryPlannerProvider(retry)
        runs = _retry_planner_for_missing_external_web_plan(
            planner_runs=(
                PlannerRunV4(
                    event=event,
                    provider_name="codex_cli_planner",
                    provider_mode="real",
                    real_provider_exercised=True,
                    real_provider_success=True,
                    fake_provider_used=False,
                    output=initial,
                ),
            ),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
        )

        self.assertEqual(provider.call_count, 1)
        self.assertTrue(_planner_output_requests_external_web(runs[0].output))
        self.assertEqual(runs[0].planner_run_role, "initial")

    def test_missing_external_web_plan_retry_does_not_block_executable_official_source_tasks(self):
        event = _planner_event()
        official_first_output = LLMPlannerOutputV2(
            top_k_archetype_hypotheses=(
                {
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "probability_or_score": 0.9,
                    "reason": "unit",
                },
            ),
            positive_thesis="unit positive",
            counter_thesis="unit counter",
            must_verify_primitives=("revenue_visibility_contract",),
            green_blockers_to_close=("source-backed confirmation",),
            red_team_checks=("wrong subject",),
            source_task_drafts=(
                {
                    "task_id": "TASK-OFFICIAL",
                    "primitive_gap": "revenue_visibility_contract",
                    "task_type": "positive_verify",
                    "preferred_source_classes": ["DART", "IssuerIR"],
                    "fallback_source_classes": ["IssuerOfficial"],
                    "forbidden_source_classes": ["unbounded_general_search"],
                    "date_window": {"end": "2026-06-29", "lookback_days": 730},
                    "max_queries": 1,
                    "max_candidates": 5,
                    "max_fetches": 1,
                    "stop_condition": {"accepted_claim_count": 1},
                    "query_intents": ["삼성전자 HBM 매출 가시성 DART IR"],
                    "llm_query_allowed": True,
                    "general_search_allowed": False,
                    "reason_from_memory": "official-first executable source task",
                },
            ),
            query_intents=("삼성전자 HBM 매출 가시성 DART IR",),
            do_not_promote_reasons=("unit",),
            planner_self_check={
                "score_keys_present": False,
                "stage_keys_present": False,
                "future_outcome_used": False,
            },
        )
        provider = _RetryPlannerProvider(_planner_output(query_intents=("retry should not run",), fallback_source_classes=("TrustedNews",)))

        runs = _retry_planner_for_missing_external_web_plan(
            planner_runs=(
                PlannerRunV4(
                    event=event,
                    provider_name="codex_cli_planner",
                    provider_mode="real",
                    real_provider_exercised=True,
                    real_provider_success=True,
                    fake_provider_used=False,
                    output=official_first_output,
                ),
            ),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
        )

        self.assertEqual(provider.call_count, 0)
        self.assertIs(runs[0].output, official_first_output)

    def test_missing_external_web_plan_retry_stops_before_starving_source_budget_mid_loop(self):
        first = _planner_event_with_id("CE-UNIT-005930-A", symbol="005930", company_name="삼성전자")
        second = _planner_event_with_id("CE-UNIT-000660-B", symbol="000660", company_name="SK하이닉스")
        initial = _planner_output(query_intents=(), fallback_source_classes=("KIND",))
        retry = _planner_output(
            query_intents=("삼성전자 HBM 고객 배정 qualification",),
            fallback_source_classes=("TrustedNews",),
        )
        provider = _RetryPlannerProvider(retry)
        progress_events: list[dict] = []

        with TemporaryDirectory() as tmp:
            progress_path = Path(tmp) / "brain_web_runtime_progress.json"
            with patch(
                "e2r.research_brain.v4_production_orchestrator._optional_retry_would_starve_source_execution_v4",
                side_effect=(False, True),
            ), patch(
                "e2r.research_brain.v4_production_orchestrator._runtime_budget_remaining_seconds_v4",
                return_value=10.0,
            ):
                runs = _retry_planner_for_missing_external_web_plan(
                    planner_runs=(
                        PlannerRunV4(
                            event=first,
                            provider_name="codex_cli_planner",
                            provider_mode="real",
                            real_provider_exercised=True,
                            real_provider_success=True,
                            fake_provider_used=False,
                            output=initial,
                        ),
                        PlannerRunV4(
                            event=second,
                            provider_name="codex_cli_planner",
                            provider_mode="real",
                            real_provider_exercised=True,
                            real_provider_success=True,
                            fake_provider_used=False,
                            output=initial,
                        ),
                    ),
                    provider=provider,
                    memory_cards=(),
                    config=ProductionShadowV4Config(
                        as_of_date="2026-06-29",
                        planner_provider="real",
                        source_acquisition="live_full_bounded",
                        planner_batch_size=1,
                        runtime_budget_seconds=600.0,
                        claim_extractor_timeout_seconds=15.0,
                        runtime_progress_path=str(progress_path),
                    ),
                    started_at=0.0,
                    progress_events=progress_events,
                )

        self.assertEqual(provider.call_count, 1)
        self.assertTrue(_planner_output_requests_external_web(runs[0].output))
        self.assertFalse(_planner_output_requests_external_web(runs[1].output))
        phases = [row["phase"] for row in progress_events]
        self.assertIn("missing_external_web_plan_retry_batch_start", phases)
        self.assertIn("missing_external_web_plan_retry_batch_end", phases)
        self.assertIn("missing_external_web_plan_retry_stopped_insufficient_source_budget", phases)

    def test_rejected_claim_feedback_is_added_to_evidence_context(self):
        event = _planner_event()
        feedback = (
            {
                "primitive_gap": "volume_growth_visible",
                "target_scope_status": "DIRECT",
                "mapping_status": "REJECTED",
                "rejection_summary": "mapping_not_accepted:REJECTED",
            },
        )
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            planner_feedback_by_event_id={event.candidate_event_id: ("previous_claims_rejected_before_score",)},
            rejected_claim_feedback_by_event_id={event.candidate_event_id: feedback},
        )

        summary = context[event.candidate_event_id]
        self.assertEqual(summary["planner_feedback"], ["previous_claims_rejected_before_score"])
        self.assertEqual(summary["rejected_claim_feedback"], list(feedback))

    def test_rejected_mapping_feedback_retries_planner_once(self):
        event = _planner_event()
        initial_run = PlannerRunV4(
            event=event,
            provider_name="codex_cli_planner",
            provider_mode="real",
            real_provider_exercised=True,
            real_provider_success=True,
            fake_provider_used=False,
            output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
        )
        retry_output = _planner_output(
            query_intents=("삼성전자 직접 고객 공급 확인 IR",),
            fallback_source_classes=("TrustedNews", "NaverSearch"),
        )
        provider = _RetryPlannerProvider(retry_output)
        bundle = _rejected_bundle(event)

        retry_run = _retry_planner_for_rejected_mapping_feedback(
            planner_run=initial_run,
            bundle=bundle,
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertEqual(retry_run.planner_feedback, ("previous_claims_rejected_before_score",))
        self.assertGreater(retry_run.rejected_claim_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertEqual(feedback_summary["planner_feedback"], ["previous_claims_rejected_before_score"])
        self.assertEqual(feedback_summary["rejected_claim_feedback"][0]["mapping_status"], "REJECTED")
        self.assertNotIn("score", feedback_summary["rejected_claim_feedback"][0])
        self.assertNotIn("stage", feedback_summary["rejected_claim_feedback"][0])

    def test_rerouted_acceptance_does_not_block_rejected_claim_feedback_retry(self):
        event = _planner_event()
        initial_run = PlannerRunV4(
            event=event,
            provider_name="codex_cli_planner",
            provider_mode="real",
            real_provider_exercised=True,
            real_provider_success=True,
            fake_provider_used=False,
            output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
        )
        provider = _RetryPlannerProvider(
            _planner_output(
                query_intents=("삼성전자 직접 원문 IR 고객 공급 확인",),
                fallback_source_classes=("TrustedNews", "NaverSearch"),
            )
        )
        bundle = _bundle_with_rerouted_acceptance_and_rejected_claim(event)

        self.assertFalse(_bundle_has_direct_source_task_acceptance(bundle))
        retry_run = _retry_planner_for_rejected_mapping_feedback(
            planner_run=initial_run,
            bundle=bundle,
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertGreater(retry_run.rejected_claim_feedback_count, 0)
        self.assertGreater(retry_run.rerouted_claim_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertTrue(feedback_summary["rejected_claim_feedback"])
        self.assertTrue(feedback_summary["rerouted_claim_feedback"])
        self.assertEqual(
            feedback_summary["rerouted_claim_feedback"][0]["accepted_primitive_ids"],
            ["medium_term_revision_visibility"],
        )

    def test_official_first_rejected_mapping_feedback_retries_planner(self):
        event = _planner_event()
        initial_run = PlannerRunV4(
            event=event,
            provider_name="codex_cli_planner",
            provider_mode="real",
            real_provider_exercised=True,
            real_provider_success=True,
            fake_provider_used=False,
            output=_planner_output(
                query_intents=("삼성전자 DART HBM capacity 확인",),
                fallback_source_classes=("CompanyGuide",),
            ),
        )
        provider = _RetryPlannerProvider(
            _planner_output(
                query_intents=("삼성전자 IR HBM capacity allocation 원문",),
                fallback_source_classes=("IssuerIR", "CompanyGuide"),
            )
        )
        bundle = _rejected_bundle(event)

        retry_run = _retry_planner_for_rejected_mapping_feedback(
            planner_run=initial_run,
            bundle=bundle,
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_official_first",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertEqual(retry_run.planner_feedback, ("previous_claims_rejected_before_score",))
        self.assertGreater(retry_run.rejected_claim_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertEqual(feedback_summary["planner_feedback"], ["previous_claims_rejected_before_score"])
        self.assertEqual(feedback_summary["rejected_claim_feedback"][0]["mapping_status"], "REJECTED")
        self.assertNotIn("score", feedback_summary["rejected_claim_feedback"][0])
        self.assertNotIn("stage", feedback_summary["rejected_claim_feedback"][0])

    def test_direct_source_task_acceptance_blocks_rejected_claim_feedback_retry(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 직접 원문 IR 고객 공급 확인",), fallback_source_classes=("TrustedNews",))
        )
        bundle = _bundle_with_direct_acceptance_and_rejected_claim(event)

        self.assertTrue(_bundle_has_direct_source_task_acceptance(bundle))
        retry_run = _retry_planner_for_rejected_mapping_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=bundle,
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNone(retry_run)
        self.assertEqual(provider.call_count, 0)

    def test_direct_source_task_acceptance_does_not_block_external_llm_rejected_claim_feedback_retry(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 고객 품질 원문 재확인",), fallback_source_classes=("TrustedNews",))
        )
        bundle = _bundle_with_direct_acceptance_and_external_llm_rejected_claim(event)

        self.assertTrue(_bundle_has_direct_source_task_acceptance(bundle))
        retry_run = _retry_planner_for_rejected_mapping_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=bundle,
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertGreater(retry_run.rejected_claim_feedback_count, 0)

    def test_source_rejection_feedback_is_added_to_evidence_context(self):
        event = _planner_event()
        feedback = (
            {
                "primitive_gap": "named_customer_or_customer_quality",
                "rejected_source_count": 2,
                "rejection_reason_distribution": {
                    "web_result_stock_list_or_channel_page_not_source_document": 2,
                },
            },
        )
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            planner_feedback_by_event_id={event.candidate_event_id: ("previous_sources_rejected_before_extraction",)},
            source_rejection_feedback_by_event_id={event.candidate_event_id: feedback},
        )

        summary = context[event.candidate_event_id]
        self.assertEqual(summary["planner_feedback"], ["previous_sources_rejected_before_extraction"])
        self.assertEqual(summary["source_rejection_feedback"], list(feedback))

    def test_rerouted_claim_feedback_is_added_to_evidence_context(self):
        event = _planner_event()
        feedback = (
            {
                "requested_primitive_gap": "hbm_capacity_pre_sold",
                "accepted_primitive_ids": ["medium_term_revision_visibility"],
                "primitive_gap_unsatisfied_ids": ["hbm_capacity_pre_sold"],
                "satisfaction_type": "REROUTED_ACCEPTED_CLAIM",
            },
        )
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_official_first",
            ),
            planner_feedback_by_event_id={event.candidate_event_id: ("previous_claims_rerouted_original_gap_unsatisfied",)},
            rerouted_claim_feedback_by_event_id={event.candidate_event_id: feedback},
        )

        summary = context[event.candidate_event_id]
        self.assertEqual(summary["planner_feedback"], ["previous_claims_rerouted_original_gap_unsatisfied"])
        self.assertEqual(summary["rerouted_claim_feedback"], list(feedback))

    def test_rerouted_claim_feedback_rows_are_gap_level_not_score_context(self):
        event = _planner_event()
        rows = _rerouted_claim_feedback_from_bundle(_rerouted_only_bundle(event))

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["requested_primitive_gap"], "hbm_capacity_pre_sold")
        self.assertEqual(row["accepted_primitive_ids"], ["medium_term_revision_visibility"])
        self.assertEqual(row["primitive_gap_unsatisfied_ids"], ["hbm_capacity_pre_sold"])
        self.assertEqual(row["satisfaction_type"], "REROUTED_ACCEPTED_CLAIM")
        self.assertNotIn("score", row)
        self.assertNotIn("stage", row)
        self.assertNotIn("current_score_eligible", row)

    def test_rerouted_claim_feedback_retries_planner_once(self):
        event = _planner_event()
        initial_run = PlannerRunV4(
            event=event,
            provider_name="codex_cli_planner",
            provider_mode="real",
            real_provider_exercised=True,
            real_provider_success=True,
            fake_provider_used=False,
            output=_planner_output(query_intents=("삼성전자 CompanyGuide HBM capacity",), fallback_source_classes=("CompanyGuide",)),
        )
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 IR HBM capacity allocation 원문",), fallback_source_classes=("IssuerIR",))
        )

        retry_run = _retry_planner_for_rerouted_claim_feedback(
            planner_run=initial_run,
            bundle=_rerouted_only_bundle(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_official_first",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertEqual(retry_run.planner_feedback, ("previous_claims_rerouted_original_gap_unsatisfied",))
        self.assertGreater(retry_run.rerouted_claim_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertEqual(feedback_summary["planner_feedback"], ["previous_claims_rerouted_original_gap_unsatisfied"])
        self.assertEqual(
            feedback_summary["rerouted_claim_feedback"][0]["accepted_primitive_ids"],
            ["medium_term_revision_visibility"],
        )
        self.assertEqual(
            feedback_summary["rerouted_claim_feedback"][0]["primitive_gap_unsatisfied_ids"],
            ["hbm_capacity_pre_sold"],
        )
        self.assertNotIn("score", feedback_summary["rerouted_claim_feedback"][0])
        self.assertNotIn("stage", feedback_summary["rerouted_claim_feedback"][0])

    def test_direct_source_task_acceptance_blocks_rerouted_claim_feedback_retry(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 IR HBM capacity allocation 원문",), fallback_source_classes=("IssuerIR",))
        )

        retry_run = _retry_planner_for_rerouted_claim_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 CompanyGuide HBM capacity",), fallback_source_classes=("CompanyGuide",)),
            ),
            bundle=_rerouted_bundle_with_direct_acceptance(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_official_first",
                retry_max=2,
            ),
        )

        self.assertIsNone(retry_run)
        self.assertEqual(provider.call_count, 0)

    def test_rerouted_claim_feedback_is_visible_to_planner_prompt_payload(self):
        event = _planner_event()
        rerouted_feedback = _rerouted_claim_feedback_from_bundle(_rerouted_only_bundle(event))
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_official_first",
            ),
            planner_feedback_by_event_id={event.candidate_event_id: ("previous_claims_rerouted_original_gap_unsatisfied",)},
            rerouted_claim_feedback_by_event_id={event.candidate_event_id: rerouted_feedback},
        )

        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id=context,
        )
        summary = payload["events"][0]["existing_evidence_summary"]
        self.assertEqual(summary["planner_feedback"], ["previous_claims_rerouted_original_gap_unsatisfied"])
        self.assertEqual(summary["rerouted_claim_feedback"][0]["requested_primitive_gap"], "hbm_capacity_pre_sold")
        self.assertTrue(any("rerouted_claim_feedback" in rule for rule in payload["rules"]))

    def test_source_rejection_feedback_rows_are_source_level_not_score_context(self):
        event = _planner_event()
        rows = _source_rejection_feedback_from_bundle(_source_rejected_bundle(event))

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["source_task_id"], "TASK-UNIT-SOURCE-REJECTED")
        self.assertEqual(row["primitive_gap"], "named_customer_or_customer_quality")
        self.assertEqual(row["fetched_document_count"], 0)
        self.assertEqual(row["selected_source_count"], 0)
        self.assertIn("web_result_stock_list_or_channel_page_not_source_document", row["rejection_reason_distribution"])
        self.assertNotIn("score", row)
        self.assertNotIn("stage", row)
        self.assertNotIn("current_score_eligible", row)

    def test_policy_rejected_external_task_becomes_source_feedback_without_web_rows(self):
        event = _planner_event()
        rows = _source_rejection_feedback_from_bundle(_policy_rejected_external_task_bundle(event))

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["source_task_id"], "TASK-UNIT-POLICY-REJECTED-EXTERNAL")
        self.assertEqual(row["primitive_gap"], "delivery_schedule")
        self.assertEqual(row["search_result_count"], 0)
        self.assertEqual(row["fetched_document_count"], 0)
        self.assertIn("official_solvable_gap_sent_to_general_web", row["rejection_reason_distribution"])
        self.assertNotIn("score", row)
        self.assertNotIn("stage", row)
        self.assertNotIn("current_score_eligible", row)

    def test_post_extraction_source_rejection_becomes_source_feedback(self):
        event = _planner_event()
        rows = _source_rejection_feedback_from_bundle(_post_extraction_source_rejected_bundle(event))

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["source_task_id"], "TASK-UNIT-POST-EXTRACT-REJECTED")
        self.assertEqual(row["primitive_gap"], "margin_bridge_visible")
        self.assertEqual(row["fetched_document_count"], 1)
        self.assertIn("post_extraction_evidence_os", row["rejection_phase_distribution"])
        self.assertIn("post_extraction_no_score_eligible_claim", row["rejection_reason_distribution"])
        self.assertIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            row["not_eligible_reason_distribution"],
        )
        self.assertEqual(row["sample_rejected_sources"][0]["rejection_phase"], "post_extraction_evidence_os")
        self.assertNotIn("score", row)
        self.assertNotIn("stage", row)
        self.assertNotIn("current_score_eligible", row)
        self.assertNotIn("score", row["sample_rejected_sources"][0])
        self.assertNotIn("stage", row["sample_rejected_sources"][0])
        self.assertNotIn("current_score_eligible", row["sample_rejected_sources"][0])

    def test_direct_acceptance_does_not_block_policy_rejected_external_task_retry(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 마진 현금흐름 원문 확인",), fallback_source_classes=("CompanyNewsroom",))
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=_policy_rejected_external_task_bundle(event, with_direct_acceptance=True),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertGreater(retry_run.source_rejection_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertEqual(feedback_summary["planner_feedback"], ["previous_sources_rejected_before_extraction"])
        self.assertIn(
            "official_solvable_gap_sent_to_general_web",
            feedback_summary["source_rejection_feedback"][0]["rejection_reason_distribution"],
        )

    def test_post_extraction_source_rejection_retries_planner_with_post_tag(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 IR 원문 마진 브리지",), fallback_source_classes=("CompanyNewsroom",))
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=_post_extraction_source_rejected_bundle(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertEqual(retry_run.planner_feedback, ("previous_sources_failed_before_or_after_extraction",))
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertEqual(feedback_summary["planner_feedback"], ["previous_sources_failed_before_or_after_extraction"])
        self.assertIn(
            "post_extraction_evidence_os",
            feedback_summary["source_rejection_feedback"][0]["rejection_phase_distribution"],
        )

    def test_direct_acceptance_does_not_block_post_extraction_source_feedback_retry(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 회사 IR 마진 개선 원문",), fallback_source_classes=("CompanyNewsroom",))
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=_post_extraction_source_rejected_bundle(event, with_direct_acceptance=True),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertGreater(retry_run.source_rejection_feedback_count, 0)

    def test_source_rejection_feedback_is_visible_to_planner_prompt_payload(self):
        event = _planner_event()
        source_feedback = _source_rejection_feedback_from_bundle(_source_rejected_bundle(event))
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            planner_feedback_by_event_id={event.candidate_event_id: ("previous_sources_rejected_before_extraction",)},
            source_rejection_feedback_by_event_id={event.candidate_event_id: source_feedback},
        )
        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=(
                ArchetypeMemoryCard(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    large_sector_id="메모리/HBM",
                ),
            ),
            existing_evidence_by_event_id=context,
        )

        summary = payload["events"][0]["existing_evidence_summary"]
        self.assertEqual(summary["planner_feedback"], ["previous_sources_rejected_before_extraction"])
        self.assertEqual(summary["source_rejection_feedback"][0]["source_task_id"], "TASK-UNIT-SOURCE-REJECTED")
        self.assertTrue(any("source_rejection_feedback" in rule for rule in payload["rules"]))

    def test_low_quality_blog_source_rejection_feedback_is_visible_to_planner_prompt_payload(self):
        event = _planner_event()
        source_feedback = _source_rejection_feedback_from_bundle(_low_quality_blog_source_rejected_bundle(event))
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            planner_feedback_by_event_id={event.candidate_event_id: ("previous_sources_rejected_before_extraction",)},
            source_rejection_feedback_by_event_id={event.candidate_event_id: source_feedback},
        )
        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=(
                ArchetypeMemoryCard(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    large_sector_id="메모리/HBM",
                ),
            ),
            existing_evidence_by_event_id=context,
        )

        summary = payload["events"][0]["existing_evidence_summary"]
        feedback = summary["source_rejection_feedback"][0]
        self.assertEqual(feedback["source_task_id"], "TASK-UNIT-LOW-QUALITY-BLOG")
        self.assertEqual(
            feedback["rejection_reason_distribution"]["web_result_low_quality_blog_or_social_not_score_source"],
            1,
        )
        self.assertNotIn("score", feedback)
        self.assertNotIn("stage", feedback)
        self.assertNotIn("current_score_eligible", feedback)
        self.assertTrue(
            any("issuer IR, DART/KIND detail, report PDF, company newsroom, trusted article original" in rule for rule in payload["rules"])
        )

    def test_source_lineage_unverified_original_feedback_is_visible_to_planner_prompt_payload(self):
        event = _planner_event()
        source_feedback = _source_rejection_feedback_from_bundle(
            _source_lineage_unverified_original_rejected_bundle(event)
        )
        context = _evidence_context_by_event(
            events=(event,),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
            ),
            planner_feedback_by_event_id={event.candidate_event_id: ("previous_source_lineage_unverified_original",)},
            source_rejection_feedback_by_event_id={event.candidate_event_id: source_feedback},
        )
        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=(
                ArchetypeMemoryCard(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    large_sector_id="메모리/HBM",
                ),
            ),
            existing_evidence_by_event_id=context,
        )

        summary = payload["events"][0]["existing_evidence_summary"]
        feedback = summary["source_rejection_feedback"][0]
        self.assertEqual(feedback["source_task_id"], "TASK-UNIT-SOURCE-LINEAGE")
        self.assertEqual(
            feedback["not_eligible_reason_distribution"][
                "source_lineage_unverified_original:TrustedNews:general_web_search_provider"
            ],
            1,
        )
        self.assertIn("source_lineage_unverified_original", feedback["source_rejection_summary"])
        self.assertNotIn("score", feedback)
        self.assertNotIn("stage", feedback)
        self.assertNotIn("current_score_eligible", feedback)
        self.assertTrue(
            any(
                "source_lineage_unverified_original" in rule and "verified original source" in rule
                for rule in payload["rules"]
            )
        )

    def test_source_rejection_feedback_retries_planner_once(self):
        event = _planner_event()
        initial_run = PlannerRunV4(
            event=event,
            provider_name="codex_cli_planner",
            provider_mode="real",
            real_provider_exercised=True,
            real_provider_success=True,
            fake_provider_used=False,
            output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
        )
        provider = _RetryPlannerProvider(
            _planner_output(
                query_intents=("삼성전자 IR 원문 고객 공급 확인",),
                fallback_source_classes=("CompanyNewsroom", "ReportPDF"),
            )
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=initial_run,
            bundle=_source_rejected_bundle(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertEqual(retry_run.planner_feedback, ("previous_sources_rejected_before_extraction",))
        self.assertGreater(retry_run.source_rejection_feedback_count, 0)
        self.assertEqual(retry_run.rejected_claim_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertEqual(feedback_summary["planner_feedback"], ["previous_sources_rejected_before_extraction"])
        self.assertEqual(
            feedback_summary["source_rejection_feedback"][0]["rejection_reason_distribution"][
                "web_result_stock_list_or_channel_page_not_source_document"
            ],
            2,
        )
        self.assertNotIn("score", feedback_summary["source_rejection_feedback"][0])
        self.assertNotIn("stage", feedback_summary["source_rejection_feedback"][0])

    def test_low_quality_blog_source_rejection_feedback_retries_planner_once(self):
        event = _planner_event()
        initial_run = PlannerRunV4(
            event=event,
            provider_name="codex_cli_planner",
            provider_mode="real",
            real_provider_exercised=True,
            real_provider_success=True,
            fake_provider_used=False,
            output=_planner_output(query_intents=("삼성전자 개인 블로그 HBM 정리",), fallback_source_classes=("NaverSearch",)),
        )
        provider = _RetryPlannerProvider(
            _planner_output(
                query_intents=("삼성전자 IR HBM 고객 배정 원문",),
                fallback_source_classes=("CompanyNewsroom", "ReportPDF"),
            )
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=initial_run,
            bundle=_low_quality_blog_source_rejected_bundle(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertEqual(retry_run.planner_feedback, ("previous_sources_rejected_before_extraction",))
        self.assertGreater(retry_run.source_rejection_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        self.assertEqual(
            feedback_summary["source_rejection_feedback"][0]["rejection_reason_distribution"][
                "web_result_low_quality_blog_or_social_not_score_source"
            ],
            1,
        )
        self.assertNotIn("score", feedback_summary["source_rejection_feedback"][0])
        self.assertNotIn("stage", feedback_summary["source_rejection_feedback"][0])

    def test_source_lineage_unverified_original_feedback_retries_planner_once(self):
        event = _planner_event()
        initial_run = PlannerRunV4(
            event=event,
            provider_name="codex_cli_planner",
            provider_mode="real",
            real_provider_exercised=True,
            real_provider_success=True,
            fake_provider_used=False,
            output=_planner_output(query_intents=("삼성전자 HBM 뉴스",), fallback_source_classes=("TrustedNews",)),
        )
        provider = _RetryPlannerProvider(
            _planner_output(
                query_intents=("삼성전자 HBM IR 원문 고객 배정",),
                fallback_source_classes=("CompanyNewsroom", "ReportPDF"),
            )
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=initial_run,
            bundle=_source_lineage_unverified_original_rejected_bundle(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertEqual(
            retry_run.planner_feedback,
            (
                "previous_source_lineage_unverified_original",
                "previous_sources_failed_before_or_after_extraction",
            ),
        )
        self.assertGreater(retry_run.source_rejection_feedback_count, 0)
        feedback_summary = provider.last_existing_evidence_by_event_id[event.candidate_event_id]
        feedback = feedback_summary["source_rejection_feedback"][0]
        self.assertEqual(
            feedback["not_eligible_reason_distribution"][
                "source_lineage_unverified_original:TrustedNews:general_web_search_provider"
            ],
            1,
        )
        self.assertNotIn("score", feedback)
        self.assertNotIn("stage", feedback)

    def test_source_lineage_feedback_retry_drops_discovery_only_source_task(self):
        event = _planner_event()
        original_task = _source_lineage_retry_task(
            event,
            task_id="TASK-ORIGINAL-LINEAGE",
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=("NaverSearch",),
            query_intents=("삼성전자 HBM 고객 배정 뉴스",),
        )
        retry_task = _source_lineage_retry_task(
            event,
            task_id="TASK-RETRY-DISCOVERY-ONLY",
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=("IndustryMedia",),
            query_intents=("삼성전자 HBM 고객 배정 기사",),
        )

        filtered = _deduplicated_feedback_retry_tasks(
            event=event,
            original_tasks=(original_task,),
            retry_tasks=(retry_task,),
            reason_tag="source_lineage_unverified_original",
        )

        self.assertEqual(filtered, ())

    def test_rerouted_feedback_retry_removes_source_that_only_produced_other_primitive(self):
        event = _planner_event()
        retry_task = SourceTask(
            task_id="TASK-REROUTED-SOURCE-RETRY",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="hbm_capacity_pre_sold",
            task_type="positive_verify",
            preferred_source_classes=("CompanyGuide", "IssuerIR", "DART"),
            fallback_source_classes=("KIND", "CompanyGuide"),
            query_intents=("삼성전자 HBM capacity 원문",),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        filtered, rejected = _deduplicated_feedback_retry_tasks_with_rejections(
            event=event,
            original_tasks=(),
            retry_tasks=(retry_task,),
            reason_tag="rerouted_claim_original_gap_unsatisfied",
            rerouted_claim_feedback=_rerouted_claim_feedback_from_bundle(_rerouted_only_bundle(event)),
        )

        self.assertFalse(rejected)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].preferred_source_classes, ("IssuerIR", "DART"))
        self.assertEqual(filtered[0].fallback_source_classes, ("KIND",))
        self.assertIn("feedback_retry:rerouted_claim_original_gap_unsatisfied", filtered[0].reason_from_memory)
        self.assertIn("rerouted_source_removed:CompanyGuide", filtered[0].reason_from_memory)

    def test_rerouted_feedback_retry_drop_is_auditable_when_only_same_source_remains(self):
        event = _planner_event()
        retry_task = SourceTask(
            task_id="TASK-REROUTED-SOURCE-ONLY",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="hbm_capacity_pre_sold",
            task_type="positive_verify",
            preferred_source_classes=("CompanyGuide",),
            fallback_source_classes=(),
            query_intents=("삼성전자 HBM capacity CompanyGuide",),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        filtered, rejected = _deduplicated_feedback_retry_tasks_with_rejections(
            event=event,
            original_tasks=(),
            retry_tasks=(retry_task,),
            reason_tag="rerouted_claim_original_gap_unsatisfied",
            rerouted_claim_feedback=_rerouted_claim_feedback_from_bundle(_rerouted_only_bundle(event)),
        )

        self.assertEqual(filtered, ())
        self.assertEqual(len(rejected), 1)
        self.assertEqual(rejected[0].status, "REJECTED_BY_POLICY")
        self.assertEqual(rejected[0].stop_reason, "rerouted_feedback_removed_all_candidate_source_classes")
        self.assertIn("rerouted_source_removed:CompanyGuide", rejected[0].source_task["reason_from_memory"])

    def test_source_lineage_feedback_retry_drop_has_auditable_execution_row(self):
        event = _planner_event()
        original_task = _source_lineage_retry_task(
            event,
            task_id="TASK-ORIGINAL-LINEAGE",
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=("NaverSearch",),
            query_intents=("삼성전자 HBM 고객 배정 뉴스",),
        )
        retry_task = _source_lineage_retry_task(
            event,
            task_id="TASK-RETRY-DISCOVERY-ONLY",
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=("IndustryMedia",),
            query_intents=("삼성전자 HBM 고객 배정 기사",),
        )

        filtered, rejected = _deduplicated_feedback_retry_tasks_with_rejections(
            event=event,
            original_tasks=(original_task,),
            retry_tasks=(retry_task,),
            reason_tag="source_lineage_unverified_original",
        )

        self.assertEqual(filtered, ())
        self.assertEqual(len(rejected), 1)
        row = rejected[0].to_dict()
        self.assertEqual(row["status"], "REJECTED_BY_POLICY")
        self.assertEqual(row["provider_name"], "research_brain_v4_retry_policy")
        self.assertEqual(row["budget_used"], {"queries": 0, "candidates": 0, "fetches": 0})
        self.assertEqual(row["stop_reason"], "source_lineage_retry_discovery_only_after_unverified_original")
        self.assertIn("source_lineage_retry_discovery_only_after_unverified_original", row["not_eligible_reasons"])
        self.assertIn("feedback_retry:source_lineage_unverified_original", row["source_task"]["reason_from_memory"])
        self.assertIn(
            "dropped:source_lineage_retry_discovery_only_after_unverified_original",
            row["source_task"]["reason_from_memory"],
        )

    def test_source_lineage_feedback_retry_keeps_original_capable_source_task(self):
        event = _planner_event()
        original_task = _source_lineage_retry_task(
            event,
            task_id="TASK-ORIGINAL-LINEAGE",
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=("NaverSearch",),
            query_intents=("삼성전자 HBM 고객 배정 뉴스",),
        )
        retry_task = _source_lineage_retry_task(
            event,
            task_id="TASK-RETRY-ORIGINAL-CAPABLE",
            preferred_source_classes=("CompanyNewsroom",),
            fallback_source_classes=("ReportPDF",),
            query_intents=("삼성전자 HBM 고객 배정 IR 원문",),
        )

        filtered = _deduplicated_feedback_retry_tasks(
            event=event,
            original_tasks=(original_task,),
            retry_tasks=(retry_task,),
            reason_tag="source_lineage_unverified_original",
        )

        self.assertEqual(len(filtered), 1)
        self.assertIn("feedback_retry:source_lineage_unverified_original", filtered[0].reason_from_memory)
        self.assertEqual(filtered[0].preferred_source_classes, ("CompanyNewsroom",))
        self.assertEqual(filtered[0].fallback_source_classes, ("ReportPDF",))

    def test_source_lineage_feedback_retry_can_execute_original_source_and_accept_claim(self):
        event = _planner_event_with_id("CE-UNIT-LINEAGE-ACCEPT", symbol="111111", company_name="한전변압기")
        _SourceLineageRetryAcceptanceRunner.reset()
        provider = _SequentialPlannerProvider(
            outputs=(
                _planner_output_for_archetype(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    primitive="named_customer_or_customer_quality",
                    query="한전변압기 고객 배정 일반 뉴스",
                ),
                _planner_output_for_archetype(
                    archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                    primitive="contract_amount_to_prior_sales",
                    query="한전변압기 단일판매 공급계약 원문 계약금액",
                ),
            )
        )

        with patch(
            "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
            return_value=(event,),
        ), patch(
            "e2r.research_brain.v4_production_orchestrator.SourceAcquisitionRunnerV4",
            _SourceLineageRetryAcceptanceRunner,
        ):
            result = run_research_brain_v4_production_shadow(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    planner_provider="real",
                    source_acquisition="live_full_bounded",
                    universe_limit=1,
                    planner_success_limit=1,
                    planner_batch_size=1,
                    retry_max=2,
                    claim_extractor_provider="rule_fallback",
                ),
                v1_archetype_matrix=load_v4_matrix(),
                planner_provider=provider,
            )

        row = result["watchlist_report"]["rows"][0]
        self.assertEqual(provider.call_count, 2)
        self.assertGreaterEqual(_SourceLineageRetryAcceptanceRunner.call_count, 2)
        self.assertEqual(row["primary_archetype"], "C05_EPC_MEGA_CONTRACT_MARGIN_GAP")
        self.assertTrue(row["accepted_claim_ids"])
        retry_acceptance_rows = [
            execution
            for execution in row["source_task_executions"]
            if execution["status"] == "EVIDENCE_OS_ACCEPTED"
            and "feedback_retry:source_lineage_unverified_original"
            in execution["source_task"]["reason_from_memory"]
        ]
        self.assertTrue(retry_acceptance_rows)
        self.assertTrue(any(execution["source_class"] == "DART" for execution in retry_acceptance_rows))
        self.assertTrue(any(execution["satisfies_source_task"] for execution in retry_acceptance_rows))
        self.assertTrue(any(execution["direct_accepted_claim_ids"] for execution in retry_acceptance_rows))
        self.assertFalse(
            any(
                execution["status"] == "REJECTED_BY_POLICY"
                and execution["stop_reason"] == "source_lineage_retry_discovery_only_after_unverified_original"
                for execution in row["source_task_executions"]
            )
        )
        self.assertGreater(
            result["evidence_extraction_audit"]["summary"]["adjudicated_claim_to_accepted_claim_count"],
            0,
        )
        self.assertEqual(
            result["evidence_extraction_audit"]["summary"].get("source_lineage_feedback_retry_dropped_count", 0),
            0,
        )
        retry_runs = [run for run in result["planner_runs"] if run.planner_run_role == "feedback_retry"]
        self.assertEqual(len(retry_runs), 1)
        self.assertEqual(
            retry_runs[0].planner_feedback,
            (
                "previous_source_lineage_unverified_original",
                "previous_sources_failed_before_or_after_extraction",
            ),
        )

    def test_direct_source_task_acceptance_does_not_block_failed_external_source_feedback_retry(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 IR 원문 고객 공급 확인",), fallback_source_classes=("CompanyNewsroom",))
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=_source_rejected_bundle_with_direct_acceptance(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=2,
            ),
        )

        self.assertIsNotNone(retry_run)
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(retry_run.planner_run_role, "feedback_retry")
        self.assertGreater(retry_run.source_rejection_feedback_count, 0)

    def test_source_rejection_feedback_retry_respects_retry_max_one(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(
            _planner_output(query_intents=("삼성전자 IR 원문",), fallback_source_classes=("CompanyNewsroom",))
        )

        retry_run = _retry_planner_for_source_rejection_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=_source_rejected_bundle(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=1,
            ),
        )

        self.assertIsNone(retry_run)
        self.assertEqual(provider.call_count, 0)

    def test_rejected_mapping_feedback_retry_respects_retry_max_one(self):
        event = _planner_event()
        provider = _RetryPlannerProvider(_planner_output(query_intents=("삼성전자 IR",), fallback_source_classes=("TrustedNews",)))
        retry_run = _retry_planner_for_rejected_mapping_feedback(
            planner_run=PlannerRunV4(
                event=event,
                provider_name="codex_cli_planner",
                provider_mode="real",
                real_provider_exercised=True,
                real_provider_success=True,
                fake_provider_used=False,
                output=_planner_output(query_intents=("삼성전자 기존 검색",), fallback_source_classes=("TrustedNews",)),
            ),
            bundle=_rejected_bundle(event),
            provider=provider,
            memory_cards=(),
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="live_full_bounded",
                retry_max=1,
            ),
        )

        self.assertIsNone(retry_run)
        self.assertEqual(provider.call_count, 0)

    def test_feedback_retry_can_reroute_primary_archetype_and_execute_new_contract(self):
        event = _planner_event_with_id("CE-UNIT-REROUTE", symbol="111111", company_name="한전변압기")
        provider = _SequentialPlannerProvider(
            outputs=(
                _planner_output_for_archetype(
                    archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                    primitive="volume_growth_visible",
                    query="한전변압기 공급계약 volume growth 확인",
                ),
                _planner_output_for_archetype(
                    archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                    primitive="contract_amount_to_prior_sales",
                    query="한전변압기 단일판매 공급계약 계약금액 확인",
                ),
            )
        )

        with patch(
            "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
            return_value=(event,),
        ), patch(
            "e2r.research_brain.v4_production_orchestrator.SourceAcquisitionRunnerV4",
            _RerouteSourceRunner,
        ):
            result = run_research_brain_v4_production_shadow(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    planner_provider="real",
                    source_acquisition="live_full_bounded",
                    universe_limit=1,
                    planner_success_limit=1,
                    planner_batch_size=1,
                    retry_max=2,
                    claim_extractor_provider="rule_fallback",
                ),
                v1_archetype_matrix=load_v4_matrix(),
                planner_provider=provider,
            )

        row = result["watchlist_report"]["rows"][0]
        self.assertEqual(provider.call_count, 2)
        self.assertEqual(row["primary_archetype"], "C05_EPC_MEGA_CONTRACT_MARGIN_GAP")
        self.assertTrue(row["accepted_claim_ids"])
        self.assertGreaterEqual(result["planner_report"]["summary"]["feedback_retry_planner_run_count"], 1)

    def test_feedback_retry_loop_can_chain_post_extraction_feedback_until_retry_max(self):
        event = _planner_event_with_id("CE-UNIT-CHAINED-RETRY", symbol="005930", company_name="삼성전자")
        _ChainedPostExtractionSourceRunner.reset()
        provider = _SequentialPlannerProvider(
            outputs=(
                _planner_output(query_intents=("삼성전자 1차 검색",), fallback_source_classes=("TrustedNews",)),
                _planner_output(query_intents=("삼성전자 2차 IR 검색",), fallback_source_classes=("CompanyNewsroom",)),
                _planner_output(query_intents=("삼성전자 3차 리포트 검색",), fallback_source_classes=("ReportPDF",)),
            )
        )

        with patch(
            "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
            return_value=(event,),
        ), patch(
            "e2r.research_brain.v4_production_orchestrator.SourceAcquisitionRunnerV4",
            _ChainedPostExtractionSourceRunner,
        ):
            result = run_research_brain_v4_production_shadow(
                config=ProductionShadowV4Config(
                    as_of_date="2026-06-29",
                    planner_provider="real",
                    source_acquisition="live_full_bounded",
                    universe_limit=1,
                    planner_success_limit=1,
                    planner_batch_size=1,
                    retry_max=3,
                    claim_extractor_provider="rule_fallback",
                ),
                v1_archetype_matrix=load_v4_matrix(),
                planner_provider=provider,
        )

        self.assertEqual(provider.call_count, 3)
        self.assertGreaterEqual(_ChainedPostExtractionSourceRunner.call_count, 3)
        self.assertEqual(result["planner_report"]["summary"]["feedback_retry_planner_run_count"], 2)
        retry_feedback = [
            run.planner_feedback
            for run in result["planner_runs"]
            if run.planner_run_role == "feedback_retry"
        ]
        self.assertIn(("previous_sources_rejected_before_extraction",), retry_feedback)
        self.assertIn(("previous_sources_failed_before_or_after_extraction",), retry_feedback)

    def test_rejected_claim_feedback_rows_are_claim_level_not_task_only(self):
        event = _planner_event()
        bundle = _rejected_bundle(event)
        rows = _rejected_claim_feedback_from_bundle(bundle)

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["claim_id"], "CLM-UNIT-REJECTED")
        self.assertEqual(row["raw_assertion_id"], "RAW-UNIT-REJECTED")
        self.assertEqual(row["document_id"], "DOC-UNIT-REJECTED")
        self.assertEqual(row["anchor_id"], "ANCH-UNIT-REJECTED")
        self.assertEqual(row["primitive_gap"], "volume_growth_visible")
        self.assertEqual(row["mapping_status"], "REJECTED")
        self.assertIn("mapping_not_accepted:REJECTED", row["eligibility_reasons"])

    def test_rejected_claim_feedback_prefers_raw_assertion_rejection_reason(self):
        event = _planner_event()
        bundle = _rejected_bundle(event)
        raw_rejection = {
            "raw_assertion_rejection_id": "RAWREJECT-UNIT",
            "raw_assertion_id": "RAW-UNIT-REJECTED",
            "adjudicated_claim_id": "CLM-UNIT-REJECTED",
            "claim_id": "CLM-UNIT-REJECTED",
            "rejection_reason": "primitive_mapping_rejected",
            "not_eligible_reasons": (
                "mapping_not_accepted:REJECTED",
                "primitive_mapping_rejected:no_allowed_primitive_for_predicate",
            ),
            "target_scope_status": "DIRECT",
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "semantic_status": "PASS",
            "mapping_status": "REJECTED",
            "mapped_primitive_id": "volume_growth_visible",
            "support_direction": "NEUTRAL",
            "mapping_rationale": "primitive_mapping_rejected:no_allowed_primitive_for_predicate",
        }
        polluted_execution = replace(
            bundle.executions[0],
            not_eligible_reasons=(
                "target_scope_not_allowed:UNRELATED",
                "target_not_direct:NOT_TARGET_SCOPED",
                "temporal_not_allowed:HISTORICAL",
            ),
        )
        bundle = EvidenceOSExecutionBundleV4(
            ledger=bundle.ledger,
            executions=(polluted_execution,),
            documents=bundle.documents,
            anchors=bundle.anchors,
            document_text_by_id=bundle.document_text_by_id,
            extraction_audit=bundle.extraction_audit,
            raw_assertions=bundle.raw_assertions,
            raw_assertion_rejections=(raw_rejection,),
        )

        rows = _rejected_claim_feedback_from_bundle(bundle)

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["raw_assertion_rejection_id"], "RAWREJECT-UNIT")
        self.assertEqual(row["raw_assertion_rejection_reason"], "primitive_mapping_rejected")
        self.assertEqual(row["target_scope_status"], "DIRECT")
        self.assertEqual(row["directness"], "DIRECT")
        self.assertEqual(row["temporal_status"], "CURRENT")
        self.assertIn("primitive_mapping_rejected", row["rejection_summary"])
        self.assertNotIn("target_scope_not_allowed:UNRELATED", row["eligibility_reasons"])

    def test_contract_field_mapping_rejection_requests_contract_compatible_retry_route(self):
        event = _planner_event()
        bundle = _rejected_bundle(event)
        raw_rejection = {
            "raw_assertion_rejection_id": "RAWREJECT-CONTRACT-FIELD",
            "raw_assertion_id": "RAW-UNIT-REJECTED",
            "adjudicated_claim_id": "CLM-UNIT-REJECTED",
            "claim_id": "CLM-UNIT-REJECTED",
            "rejection_reason": "primitive_mapping_rejected",
            "not_eligible_reasons": (
                "mapping_not_accepted:REJECTED",
                "primitive_mapping_rejected:v4_signal:structured_field_contract_quality_revenue_visibility_contract",
            ),
            "target_scope_status": "DIRECT",
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "semantic_status": "PASS",
            "mapping_status": "REJECTED",
            "mapped_primitive_id": "volume_growth_visible",
            "support_direction": "NEUTRAL",
            "mapping_rationale": "primitive_mapping_rejected:v4_signal:structured_field_contract_quality_revenue_visibility_contract",
        }
        bundle = EvidenceOSExecutionBundleV4(
            ledger=bundle.ledger,
            executions=bundle.executions,
            documents=bundle.documents,
            anchors=bundle.anchors,
            document_text_by_id=bundle.document_text_by_id,
            extraction_audit=bundle.extraction_audit,
            raw_assertions=bundle.raw_assertions,
            raw_assertion_rejections=(raw_rejection,),
        )

        rows = _rejected_claim_feedback_from_bundle(bundle)

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertTrue(row["contract_signal_detected"])
        self.assertTrue(row["contract_compatible_route_required"])
        self.assertEqual(row["contract_compatibility_feedback"], "contract_fields_found_but_selected_primitive_incompatible")
        self.assertIn("contract_amount_to_prior_sales", row["contract_compatible_primitive_hints"])

    def test_llm_generated_external_task_is_not_dropped_by_task_cap(self):
        event = _planner_event()
        output = LLMPlannerOutputV2(
            top_k_archetype_hypotheses=(
                {
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "probability_or_score": 0.9,
                    "reason": "unit",
                },
            ),
            positive_thesis="unit positive",
            counter_thesis="unit counter",
            must_verify_primitives=("direct_company_cash_route", "implementation_timeline", "named_customer_or_customer_quality"),
            green_blockers_to_close=("source-backed confirmation",),
            red_team_checks=("wrong subject",),
            source_task_drafts=(
                _source_task_draft_payload("direct_company_cash_route", ("DART",), ("IssuerOfficial",)),
                _source_task_draft_payload("implementation_timeline", ("DART",), ("KIND",)),
                _source_task_draft_payload("named_customer_or_customer_quality", ("DART",), ("TrustedNews", "NaverSearch")),
            ),
            query_intents=("삼성전자 HBM 고객 배정 qualification",),
            do_not_promote_reasons=("unit",),
            planner_self_check={
                "score_keys_present": False,
                "stage_keys_present": False,
                "future_outcome_used": False,
            },
        )

        tasks = source_tasks_from_planner_output_v4(
            event=event,
            planner_output=output,
            card_by_id={
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": ArchetypeMemoryCard(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    large_sector_id="메모리/HBM",
                )
            },
            max_tasks=2,
        )

        self.assertEqual(len(tasks), 2)
        self.assertIn("named_customer_or_customer_quality", {task.primitive_gap for task in tasks})

    def test_source_task_query_intents_are_task_specific_before_global_fallback(self):
        event = _planner_event()
        contract_task = {
            **_source_task_draft_payload("contract_amount_to_prior_sales", ("DART",), ("IssuerOfficial",)),
            "query_intents": ("삼성전자 계약금액 매출액 원문",),
        }
        cost_task = {
            **_source_task_draft_payload("cost_overrun", ("TrustedNews",), ("NaverSearch",)),
            "query_intents": ("삼성전자 비용 초과 원가 상승 원문",),
        }
        fallback_task = _source_task_draft_payload("named_customer_or_customer_quality", ("TrustedNews",), ("NaverSearch",))
        output = LLMPlannerOutputV2(
            top_k_archetype_hypotheses=(
                {
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "probability_or_score": 0.9,
                    "reason": "unit",
                },
            ),
            positive_thesis="unit positive",
            counter_thesis="unit counter",
            must_verify_primitives=("contract_amount_to_prior_sales", "cost_overrun", "named_customer_or_customer_quality"),
            green_blockers_to_close=("source-backed confirmation",),
            red_team_checks=("wrong subject",),
            source_task_drafts=(contract_task, cost_task, fallback_task),
            query_intents=("삼성전자 전체 이벤트 공통 검색",),
            do_not_promote_reasons=("unit",),
            planner_self_check={
                "score_keys_present": False,
                "stage_keys_present": False,
                "future_outcome_used": False,
            },
        )

        tasks = source_tasks_from_planner_output_v4(
            event=event,
            planner_output=output,
            card_by_id={
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": ArchetypeMemoryCard(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    large_sector_id="메모리/HBM",
                )
            },
            max_tasks=3,
        )

        by_primitive = {task.primitive_gap: task for task in tasks}
        self.assertEqual(by_primitive["contract_amount_to_prior_sales"].query_intents, ("삼성전자 계약금액 매출액 원문",))
        self.assertEqual(by_primitive["cost_overrun"].query_intents, ("삼성전자 비용 초과 원가 상승 원문",))
        self.assertEqual(by_primitive["named_customer_or_customer_quality"].query_intents, ("삼성전자 전체 이벤트 공통 검색",))

    def test_fetch_cap_does_not_truncate_planner_source_tasks(self):
        event = _planner_event()
        output = LLMPlannerOutputV2(
            top_k_archetype_hypotheses=(
                {
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "probability_or_score": 0.9,
                    "reason": "unit",
                },
            ),
            positive_thesis="unit positive",
            counter_thesis="unit counter",
            must_verify_primitives=("direct_company_cash_route", "implementation_timeline", "named_customer_or_customer_quality"),
            green_blockers_to_close=("source-backed confirmation",),
            red_team_checks=("wrong subject",),
            source_task_drafts=(
                _source_task_draft_payload("direct_company_cash_route", ("DART",), ("IssuerOfficial",), max_fetches=5),
                _source_task_draft_payload("implementation_timeline", ("DART",), ("KIND",), max_fetches=4),
                _source_task_draft_payload(
                    "named_customer_or_customer_quality",
                    ("TrustedNews",),
                    ("NaverSearch",),
                    max_fetches=3,
                ),
            ),
            query_intents=("삼성전자 HBM 고객 배정 qualification",),
            do_not_promote_reasons=("unit",),
            planner_self_check={
                "score_keys_present": False,
                "stage_keys_present": False,
                "future_outcome_used": False,
            },
        )

        tasks = source_tasks_from_planner_output_v4(
            event=event,
            planner_output=output,
            card_by_id={
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": ArchetypeMemoryCard(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    large_sector_id="메모리/HBM",
                )
            },
            max_tasks=3,
            max_fetches_per_task=1,
        )

        self.assertEqual(len(tasks), 3)
        self.assertEqual({task.max_fetches for task in tasks}, {1})
        self.assertEqual(
            {task.primitive_gap for task in tasks},
            {"direct_company_cash_route", "implementation_timeline", "named_customer_or_customer_quality"},
        )

    def test_planner_candidate_order_prioritizes_claim_likely_live_events_without_dropping_corrections(self):
        correction = replace(
            _planner_event_with_id("CE-UNIT-CORRECTION", symbol="003090", company_name="대웅"),
            event_type="[기재정정]신규시설투자등",
            event_title="[기재정정]신규시설투자등",
            event_summary="신규시설투자 종료일 연장 정정",
            raw_reason_codes=("[기재정정]신규시설투자등",),
        )
        contract = replace(
            _planner_event_with_id("CE-UNIT-CONTRACT", symbol="114450", company_name="그린생명과학"),
            event_type="단일판매ㆍ공급계약체결",
            event_title="단일판매ㆍ공급계약체결",
            event_summary="의약품 원료 공급계약 체결",
            raw_reason_codes=("단일판매ㆍ공급계약체결",),
        )
        report = replace(
            _planner_event_with_id("CE-UNIT-REPORT", symbol="000660", company_name="SK하이닉스"),
            source_family="CompanyGuide",
            source_id="https://comp.fnguide.com/report/unit",
            event_type="report_radar",
            event_title="실적과 멀티플 둘 다 열려 있다",
            event_summary="실적 전망 상향 리포트",
            raw_reason_codes=("REPORT_RADAR",),
        )

        ordered = _planner_candidate_order(
            events=(correction, report, contract),
            config=ProductionShadowV4Config(
                as_of_date="2026-07-01",
                source_acquisition="live_full_bounded",
            ),
            repo_root=".",
            as_of_date=date(2026, 7, 1),
        )

        self.assertEqual({event.candidate_event_id for event in ordered}, {correction.candidate_event_id, report.candidate_event_id, contract.candidate_event_id})
        self.assertLess(ordered.index(contract), ordered.index(correction))
        self.assertLess(ordered.index(report), ordered.index(correction))

    def test_direct_contract_event_prompt_includes_contract_compatible_route_option(self):
        event = replace(
            _planner_event_with_id("CE-UNIT-CONTRACT-PROMPT", symbol="114450", company_name="그린생명과학"),
            event_type="[기재정정]단일판매ㆍ공급계약체결",
            event_title="[기재정정]단일판매ㆍ공급계약체결",
            event_summary="OpenDART 단일판매 공급계약 정정 공시",
            primary_disclosure_type="[기재정정]단일판매ㆍ공급계약체결",
            raw_reason_codes=("[기재정정]단일판매ㆍ공급계약체결",),
            structured_payload={"report_nm": "[기재정정]단일판매ㆍ공급계약체결"},
        )

        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={},
        )

        event_payload = payload["events"][0]
        self.assertTrue(event_payload["event_signal_profile"]["direct_revenue_contract_disclosure"])
        contract_options = [
            option
            for option in event_payload["allowed_archetype_options"]
            if option["contract_compatible"]
        ]
        self.assertEqual(contract_options[0]["archetype_id"], "C05_EPC_MEGA_CONTRACT_MARGIN_GAP")
        self.assertGreater(contract_options[0]["event_signal_fit_score"], contract_options[-1]["event_signal_fit_score"])
        options = {
            option["archetype_id"]: option
            for option in event_payload["allowed_archetype_options"]
        }
        self.assertIn("C05_EPC_MEGA_CONTRACT_MARGIN_GAP", options)
        c05 = options["C05_EPC_MEGA_CONTRACT_MARGIN_GAP"]
        self.assertTrue(c05["contract_compatible"])
        self.assertIn("contract_amount_to_prior_sales", c05["contract_compatible_primitives"])
        self.assertTrue(any("direct_revenue_contract_disclosure" in rule for rule in payload["rules"]))

    def test_non_revenue_contract_event_is_not_marked_as_direct_revenue_contract(self):
        event = replace(
            _planner_event_with_id("CE-UNIT-NON-REVENUE-CONTRACT", symbol="123456", company_name="관리샘플"),
            event_type="주식담보제공계약 체결",
            event_title="주식담보제공계약 체결",
            event_summary="최대주주 주식담보제공계약 체결",
            raw_reason_codes=("주식담보제공계약 체결",),
            structured_payload={"report_nm": "주식담보제공계약 체결"},
        )

        payload = build_v4_planner_prompt_payload(
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={},
        )

        self.assertFalse(payload["events"][0]["event_signal_profile"]["direct_revenue_contract_disclosure"])

    def test_official_solvable_contract_task_drops_web_fallback_instead_of_rejecting_plan(self):
        event = replace(
            _planner_event_with_id("CE-UNIT-CONTRACT-SANITIZE", symbol="114450", company_name="그린생명과학"),
            event_type="단일판매ㆍ공급계약체결",
            event_title="단일판매ㆍ공급계약체결",
            event_summary="OpenDART 공급계약 공시",
            raw_reason_codes=("단일판매ㆍ공급계약체결",),
        )
        payload = {
            "top_k_archetype_hypotheses": [
                {
                    "archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                    "probability_or_score": 0.9,
                    "reason": "contract-compatible route",
                }
            ],
            "positive_thesis": "계약금액과 매출대비 비율을 확인한다.",
            "counter_thesis": "계약 원문 claim 전까지 점수화하지 않는다.",
            "must_verify_primitives": ["contract_quality"],
            "green_blockers_to_close": ["FCF bridge"],
            "red_team_checks": ["wrong subject"],
            "source_task_drafts": [
                {
                    "task_id": "TASK-CONTRACT-QUALITY",
                    "primitive_gap": "contract_quality",
                    "task_type": "positive_verify",
                    "preferred_source_classes": ["DART"],
                    "fallback_source_classes": ["TrustedNews", "IssuerOfficial"],
                    "forbidden_source_classes": ["unbounded_general_search"],
                    "date_window": {"end": "2026-06-29", "lookback_days": 30},
                    "max_queries": 1,
                    "max_candidates": 5,
                    "max_fetches": 1,
                    "stop_condition": {"accepted_claim_count": 1},
                    "llm_query_allowed": True,
                    "general_search_allowed": True,
                    "reason_from_memory": "unit contract route",
                }
            ],
            "query_intents": ["그린생명과학 공급계약 계약금액"],
            "do_not_promote_reasons": ["unit"],
            "planner_self_check": {
                "score_keys_present": False,
                "stage_keys_present": False,
                "future_outcome_used": False,
            },
        }

        output = validate_llm_planner_output_v4(
            payload,
            event=event,
            memory_cards=load_v4_cards(),
        )

        draft = output.source_task_drafts[0]
        self.assertEqual(draft["primitive_gap"], "contract_amount_to_prior_sales")
        self.assertFalse(draft["general_search_allowed"])
        self.assertNotIn("TrustedNews", draft["fallback_source_classes"])
        self.assertIn("IssuerOfficial", draft["fallback_source_classes"])

    def test_contract_visibility_gap_is_sanitized_to_official_first_before_v3_validator(self):
        event = replace(
            _planner_event_with_id("CE-UNIT-CONTRACT-VISIBILITY-SANITIZE", symbol="001470", company_name="삼부토건"),
            event_type="단일판매ㆍ공급계약체결",
            event_title="단일판매ㆍ공급계약체결",
            event_summary="OpenDART 공급계약 공시의 계약 가시성 확인 필요",
            raw_reason_codes=("단일판매ㆍ공급계약체결",),
        )
        payload = {
            "top_k_archetype_hypotheses": [
                {
                    "archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                    "probability_or_score": 0.82,
                    "reason": "contract visibility route",
                }
            ],
            "positive_thesis": "계약기간과 납품 일정이 매출 가시성으로 이어지는지 확인한다.",
            "counter_thesis": "원문 계약기간 claim 전까지 점수화하지 않는다.",
            "must_verify_primitives": ["contract_visibility"],
            "green_blockers_to_close": ["cash bridge"],
            "red_team_checks": ["wrong subject"],
            "source_task_drafts": [
                {
                    "task_id": "TASK-CONTRACT-VISIBILITY",
                    "primitive_gap": "contract_visibility",
                    "task_type": "positive_verify",
                    "preferred_source_classes": ["DART", "NaverSearch"],
                    "fallback_source_classes": ["TrustedNews", "IssuerOfficial"],
                    "forbidden_source_classes": ["unbounded_general_search"],
                    "date_window": {"end": "2026-07-01", "lookback_days": 370},
                    "max_queries": 2,
                    "max_candidates": 10,
                    "max_fetches": 2,
                    "stop_condition": {"accepted_claim_count": 1},
                    "llm_query_allowed": True,
                    "general_search_allowed": True,
                    "query_intents": ["삼부토건 001470 계약기간 매출 가시성 뉴스"],
                    "reason_from_memory": "unit contract visibility route",
                }
            ],
            "query_intents": ["삼부토건 001470 계약기간 매출 가시성"],
            "do_not_promote_reasons": ["unit"],
            "planner_self_check": {
                "score_keys_present": False,
                "stage_keys_present": False,
                "future_outcome_used": False,
            },
        }

        output = validate_llm_planner_output_v4(
            payload,
            event=event,
            memory_cards=load_v4_cards(),
        )

        draft = output.source_task_drafts[0]
        self.assertEqual(draft["primitive_gap"], "contract_visibility")
        self.assertFalse(draft["general_search_allowed"])
        self.assertIn("DART", draft["preferred_source_classes"])
        self.assertNotIn("NaverSearch", draft["preferred_source_classes"])
        self.assertNotIn("TrustedNews", draft["fallback_source_classes"])
        self.assertIn("IssuerOfficial", draft["fallback_source_classes"])

    def test_zero_accepted_claim_first_candidate_continues_to_next_candidate_when_target_is_set(self):
        first = replace(
            _planner_event_with_id("CE-UNIT-A-FIRST-ZERO", symbol="003090", company_name="대웅"),
            event_type="단일판매ㆍ공급계약체결",
            event_title="단일판매ㆍ공급계약체결",
            event_summary="공급계약 원문 확인 필요",
            raw_reason_codes=("단일판매ㆍ공급계약체결",),
        )
        second = replace(
            _planner_event_with_id("CE-UNIT-B-SECOND-ACCEPT", symbol="114450", company_name="그린생명과학"),
            event_type="단일판매ㆍ공급계약체결",
            event_title="단일판매ㆍ공급계약체결",
            event_summary="의약품 원료 공급계약 체결",
            raw_reason_codes=("단일판매ㆍ공급계약체결",),
        )
        provider = _SequentialPlannerProvider(
            outputs=(
                _planner_output(query_intents=("대웅 시설투자 원문",), fallback_source_classes=("TrustedNews",)),
                _planner_output(query_intents=("그린생명과학 공급계약 원문",), fallback_source_classes=("TrustedNews",)),
            )
        )

        def execute_side_effect(*, event, tasks, contract, as_of_date, source_runner, claim_extractor, **_kwargs):
            if event.candidate_event_id == first.candidate_event_id:
                return _rejected_bundle(event)
            return _bundle_with_direct_acceptance_and_rejected_claim(event)

        with patch(
            "e2r.research_brain.v4_production_orchestrator.discover_daily_candidate_events_v4",
            return_value=(first, second),
        ), patch(
            "e2r.research_brain.v4_production_orchestrator.execute_source_tasks_with_evidence_os_v4",
            side_effect=execute_side_effect,
        ):
            result = run_research_brain_v4_production_shadow(
                config=ProductionShadowV4Config(
                    as_of_date="2026-07-01",
                    planner_provider="real",
                    source_acquisition="live_full_bounded",
                    universe_limit=2,
                    planner_success_limit=1,
                    planner_batch_size=1,
                    accepted_claim_target=1,
                    max_distinct_candidate_attempts=2,
                    retry_max=1,
                    claim_extractor_provider="rule_fallback",
                ),
                v1_archetype_matrix=load_v4_matrix(),
                planner_provider=provider,
            )

        self.assertEqual(provider.call_count, 2)
        attempted_ids = [
            run.event.candidate_event_id
            for run in result["planner_runs"]
            if run.real_provider_success
        ]
        self.assertEqual(attempted_ids, [first.candidate_event_id, second.candidate_event_id])
        self.assertEqual(result["candidate_report"]["summary"]["candidate_event_count"], 2)
        accepted_by_event = {
            row["candidate_event_id"]: row["accepted_claim_count"]
            for row in result["candidate_report"]["rows"]
        }
        self.assertEqual(accepted_by_event[first.candidate_event_id], 0)
        self.assertGreaterEqual(accepted_by_event[second.candidate_event_id], 1)

    def test_merge_evidence_bundles_keeps_existing_claim_when_retry_adjudication_collides(self):
        event = _planner_event()
        base = _rejected_bundle(event)
        original_claim = next(iter(base.ledger.claims.values()))
        retry_claim = replace(original_claim, polarity=Polarity.POSITIVE)
        retry_ledger = AppendOnlyEvidenceLedger()
        retry_ledger.append_claim(retry_claim)
        for mapping in base.ledger.mappings.values():
            retry_ledger.append_mapping(mapping)
        retry = EvidenceOSExecutionBundleV4(
            ledger=retry_ledger,
            executions=base.executions,
            documents=base.documents,
            anchors=base.anchors,
            document_text_by_id=base.document_text_by_id,
            extraction_audit=base.extraction_audit,
            raw_assertions=base.raw_assertions,
        )

        merged = _merge_evidence_os_bundles_v4(base, retry)

        self.assertEqual(merged.ledger.claims[original_claim.claim_id].polarity, original_claim.polarity)
        self.assertTrue(
            any(
                event.event_type.value == "UPDATES"
                and event.from_id == original_claim.claim_id
                and event.reason == "claim_id_collision_existing_claim_retained"
                for event in merged.ledger.events
            )
        )

def _planner_event() -> CandidateEventV2:
    return _planner_event_with_id("CE-UNIT-005930")


def _planner_event_with_id(candidate_event_id: str, *, symbol: str = "005930", company_name: str = "삼성전자") -> CandidateEventV2:
    return CandidateEventV2(
        candidate_event_id=candidate_event_id,
        symbol=symbol,
        company_name=company_name,
        event_date="2026-06-29",
        detected_at="2026-06-29",
        source_family="DART",
        source_id=f"https://dart.example/{symbol}",
        event_type="unit_event",
        event_summary=f"{company_name} HBM 고객 배정 확인 필요",
        magnitude=EventMagnitudeV2(),
    )


def _planner_output(*, query_intents, fallback_source_classes) -> LLMPlannerOutputV2:
    return LLMPlannerOutputV2(
        top_k_archetype_hypotheses=(
            {
                "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "probability_or_score": 0.9,
                "reason": "unit",
            },
        ),
        positive_thesis="unit positive",
        counter_thesis="unit counter",
        must_verify_primitives=("named_customer_or_customer_quality",),
        green_blockers_to_close=("source-backed confirmation",),
        red_team_checks=("wrong subject",),
        source_task_drafts=(
            {
                "task_id": "TASK-UNIT",
                "primitive_gap": "named_customer_or_customer_quality",
                "task_type": "positive_verify",
                "preferred_source_classes": ["DART"],
                "fallback_source_classes": list(fallback_source_classes),
                "forbidden_source_classes": ["unbounded_general_search"],
                "date_window": {"end": "2026-06-29", "lookback_days": 30},
                "max_queries": 1,
                "max_candidates": 5,
                "max_fetches": 1,
                "stop_condition": {"accepted_claim_count": 1},
                "llm_query_allowed": True,
                "general_search_allowed": False,
                "reason_from_memory": "unit",
            },
        ),
        query_intents=tuple(query_intents),
        do_not_promote_reasons=("unit",),
        planner_self_check={
            "score_keys_present": False,
            "stage_keys_present": False,
            "future_outcome_used": False,
        },
    )


def _planner_output_for_archetype(*, archetype_id: str, primitive: str, query: str) -> LLMPlannerOutputV2:
    return LLMPlannerOutputV2(
        top_k_archetype_hypotheses=(
            {
                "archetype_id": archetype_id,
                "probability_or_score": 0.9,
                "reason": "unit reroute",
            },
        ),
        positive_thesis="unit positive",
        counter_thesis="unit counter",
        must_verify_primitives=(primitive,),
        green_blockers_to_close=("source-backed confirmation",),
        red_team_checks=("wrong subject",),
        source_task_drafts=(
            {
                "task_id": f"TASK-{primitive}",
                "primitive_gap": primitive,
                "task_type": "positive_verify",
                "preferred_source_classes": ["DART"],
                "fallback_source_classes": ["TrustedNews"],
                "forbidden_source_classes": ["unbounded_general_search"],
                "date_window": {"end": "2026-06-29", "lookback_days": 30},
                "max_queries": 1,
                "max_candidates": 5,
                "max_fetches": 1,
                "stop_condition": {"accepted_claim_count": 1},
                "llm_query_allowed": True,
                "general_search_allowed": True,
                "reason_from_memory": "unit reroute task",
            },
        ),
        query_intents=(query,),
        do_not_promote_reasons=("unit",),
        planner_self_check={
            "score_keys_present": False,
            "stage_keys_present": False,
            "future_outcome_used": False,
        },
    )


def _source_task_draft_payload(primitive: str, preferred, fallback, *, max_fetches: int = 1):
    return {
        "task_id": f"TASK-{primitive}",
        "primitive_gap": primitive,
        "task_type": "positive_verify",
        "preferred_source_classes": list(preferred),
        "fallback_source_classes": list(fallback),
        "forbidden_source_classes": ["unbounded_general_search"],
        "date_window": {"end": "2026-06-29", "lookback_days": 30},
        "max_queries": 1,
        "max_candidates": 5,
        "max_fetches": max_fetches,
        "stop_condition": {"accepted_claim_count": 1},
        "llm_query_allowed": True,
        "general_search_allowed": False,
        "reason_from_memory": "unit",
    }


class _OneLiveOfficialConnector:
    provider_name = "OpenDARTUnit"
    source_class = "DART"

    def fetch(self, *, symbol, company_name, as_of_date, mode):
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="FETCHED",
            canonical_url=f"https://dart.example/{symbol}/official",
            official_document_id=f"OFFICIAL-{symbol}",
            published_at=as_of_date.isoformat(),
            available_at=as_of_date.isoformat(),
            fetched_at=as_of_date.isoformat(),
            content_hash=f"HASH-{symbol}",
            raw_text=f"{company_name} 공식 보고서 HBM 현재 상태 확인.",
            structured_payload={"symbol": symbol, "company_name": company_name},
            provider_request_id=f"REQ-{symbol}",
        )


class _BudgetRecordingSearchProvider:
    def __init__(self) -> None:
        self.calls = []

    def search(self, query, as_of_date, max_results=100):
        call_index = len(self.calls) + 1
        self.calls.append({"query": query, "max_results": max_results})
        return (
            SearchResult(
                title=f"삼성전자 HBM 고객 배정 보도 {call_index}",
                url=f"https://unit-news.example/samsung-hbm-{call_index}",
                snippet="삼성전자 HBM 고객 배정 확인",
                source="UnitNews",
                rank=call_index,
                is_news=True,
            ),
        )


class _MissingFirstRealPlannerProvider:
    provider_name = "unit_real_planner_missing_first"
    provider_mode = "real"
    real_provider = True
    fake_provider = False
    model = "unit"
    endpoint = "unit"

    def __init__(self, *, success_event_id: str) -> None:
        self.success_event_id = success_event_id

    def plan_many(self, *, events, memory_cards, existing_evidence_by_event_id=None):
        return {
            event.candidate_event_id: _planner_output(
                query_intents=(),
                fallback_source_classes=("IssuerOfficial",),
            )
            for event in events
            if event.candidate_event_id == self.success_event_id
        }


class _NoSuccessRealPlannerProvider:
    provider_name = "unit_real_planner_no_success"
    provider_mode = "real"
    real_provider = True
    fake_provider = False
    model = "unit"
    endpoint = "unit"

    def plan_many(self, *, events, memory_cards, existing_evidence_by_event_id=None):
        return {}


class _SequentialPlannerProvider:
    provider_name = "unit_sequential_planner"
    provider_mode = "real"
    fake_provider = False
    real_provider = True
    model = "unit"
    endpoint = "unit"

    def __init__(self, *, outputs):
        self.outputs = tuple(outputs)
        self.call_count = 0

    def plan_many(self, *, events, memory_cards, existing_evidence_by_event_id=None):
        output = self.outputs[min(self.call_count, len(self.outputs) - 1)]
        self.call_count += 1
        return {event.candidate_event_id: output for event in events}


class _RerouteSourceRunner:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def acquire(self, *, event, task, as_of_date):
        if task.archetype_id == "C05_EPC_MEGA_CONTRACT_MARGIN_GAP":
            text = "한전변압기 단일판매·공급계약체결 계약금액 1500억원 최근매출액 대비 15.0% 계약기간 2026-06-29 ~ 2028-06-29"
            anchor_type = AnchorType.API_RECORD
            normalized_value = {
                "symbol": event.symbol,
                "company_name": event.company_name,
                "row": {
                    "report_type": "단일판매·공급계약체결",
                    "contract_amount_to_prior_sales": "0.15",
                    "contract_duration_months": "24",
                },
            }
        else:
            text = "한전변압기는 UPL과 2026.06.29 공급계약을 체결했다."
            anchor_type = AnchorType.TEXT_SPAN
            normalized_value = {"symbol": event.symbol, "company_name": event.company_name}
        document = EvidenceDocument.from_text(
            text=text,
            canonical_url=f"https://dart.example/{event.symbol}/{task.archetype_id}",
            source_type=SourceType.FILING,
            source_name="OpenDARTUnit",
            published_at=date(2026, 6, 29),
            available_at=date(2026, 6, 29),
            fetched_at=as_of_date,
            parser_version="unit",
            source_proxy_only=False,
        )
        anchor = EvidenceAnchor.structured(
            document=document,
            anchor_type=anchor_type,
            locator=f"unit:{task.task_id}",
            exact_text=text,
            normalized_value=normalized_value,
            anchor_verified=True,
        )
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class="DART",
            provider_name="OpenDARTUnit",
            status="PARSED",
            documents=(document,),
            anchors=(anchor,),
            document_text_by_id={document.document_id: text},
            fetched_document_ids=(document.document_id,),
            document_urls=(document.canonical_url or "",),
            document_hashes=(document.content_hash,),
            anchor_ids=(anchor.anchor_id,),
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
            stop_reason="unit",
        )


class _SourceLineageRetryAcceptanceRunner:
    call_count = 0

    @classmethod
    def reset(cls) -> None:
        cls.call_count = 0

    def __init__(self, *args, **kwargs) -> None:
        pass

    def acquire(self, *, event, task, as_of_date):
        type(self).call_count += 1
        is_feedback_retry_task = "feedback_retry:source_lineage_unverified_original" in str(
            getattr(task, "reason_from_memory", "") or ""
        )
        if not is_feedback_retry_task:
            web_task_id = "WEBTASK-LINEAGE-ACCEPT-PRE"
            web_result_id = "WEBRESULT-LINEAGE-ACCEPT-PRE"
            web_fetch_id = "WEBFETCH-LINEAGE-ACCEPT-PRE"
            web_task = {
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "한전변압기 고객 배정 일반 뉴스",
                "primitive_gap": task.primitive_gap,
                "provider_name": "NaverFreeSearchProvider",
                "status": "SEARCH_EXECUTED",
                "result_count": 1,
                "fetched_document_count": 1,
                "rejected_document_count": 1,
            }
            web_result = {
                "web_result_id": web_result_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": web_task["query"],
                "provider_name": "NaverFreeSearchProvider",
                "url": "https://news.example.test/transformer-customer-allocation",
                "title": "한전변압기 고객 배정 보도",
                "selection_status": "SELECTED_FOR_FETCH",
                "selected_for_fetch": True,
            }
            web_fetched = {
                "web_fetch_id": web_fetch_id,
                "web_result_id": web_result_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": web_task["query"],
                "provider_name": "NaverFreeSearchProvider",
                "url": web_result["url"],
                "title": web_result["title"],
                "document_id": "DOC-LINEAGE-ACCEPT-PRE",
                "snippet_score_forbidden": True,
            }
            web_rejected = {
                "web_rejected_id": "WEBREJECT-LINEAGE-ACCEPT-PRE",
                "web_result_id": web_result_id,
                "web_fetch_id": web_fetch_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": web_task["query"],
                "provider_name": "NaverFreeSearchProvider",
                "status": "REJECTED",
                "url": web_result["url"],
                "title": web_result["title"],
                "rejection_phase": "post_extraction_evidence_os",
                "rejection_reason": "post_extraction_no_score_eligible_claim",
                "not_eligible_reasons": [
                    "source_task_provider_error_score_block:general_search_not_score_source",
                    "source_provider_document_type_mismatch:TrustedNews:general_web_search_provider",
                    "source_lineage_unverified_original:TrustedNews:general_web_search_provider",
                ],
                "provider_errors": ["trusted_news_provider_not_configured; general search is not a score source"],
                "raw_assertion_ids": [],
                "rejected_claim_ids": [],
                "accepted_claim_ids": [],
                "snippet_score_forbidden": True,
            }
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class="TrustedNews",
                provider_name="NaverFreeSearchProvider",
                status="NO_EVIDENCE_FOUND",
                fetched_document_ids=("DOC-LINEAGE-ACCEPT-PRE",),
                document_urls=(web_result["url"],),
                document_hashes=("hash-lineage-accept-pre",),
                provider_errors=tuple(web_rejected["provider_errors"]),
                budget_used={"queries": 1, "candidates": 1, "fetches": 1},
                stop_reason="source_lineage_unverified_original",
                web_search_tasks=(web_task,),
                web_search_results=(web_result,),
                web_fetched_documents=(web_fetched,),
                web_rejected_documents=(web_rejected,),
            )

        text = (
            "한전변압기 단일판매·공급계약체결 계약금액 1500억원 최근매출액 대비 15.0% "
            "계약기간 2026-06-29 ~ 2028-06-29"
        )
        normalized_value = {
            "symbol": event.symbol,
            "company_name": event.company_name,
            "row": {
                "report_type": "단일판매·공급계약체결",
                "contract_amount_to_prior_sales": "0.15",
                "contract_duration_months": "24",
            },
        }
        document = EvidenceDocument.from_text(
            text=text,
            canonical_url=f"https://dart.example/{event.symbol}/retry-contract",
            source_type=SourceType.FILING,
            source_name="OpenDARTUnit",
            published_at=date(2026, 6, 29),
            available_at=date(2026, 6, 29),
            fetched_at=as_of_date,
            parser_version="unit",
            source_proxy_only=False,
        )
        anchor = EvidenceAnchor.structured(
            document=document,
            anchor_type=AnchorType.API_RECORD,
            locator=f"unit:{task.task_id}",
            exact_text=text,
            normalized_value=normalized_value,
            anchor_verified=True,
        )
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class="DART",
            provider_name="OpenDARTUnit",
            status="PARSED",
            documents=(document,),
            anchors=(anchor,),
            document_text_by_id={document.document_id: text},
            fetched_document_ids=(document.document_id,),
            document_urls=(document.canonical_url or "",),
            document_hashes=(document.content_hash,),
            anchor_ids=(anchor.anchor_id,),
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
            stop_reason="unit_source_lineage_retry_accepted",
        )


class _ChainedPostExtractionSourceRunner:
    call_count = 0
    post_extraction_emitted = False

    @classmethod
    def reset(cls) -> None:
        cls.call_count = 0
        cls.post_extraction_emitted = False

    def __init__(self, *args, **kwargs) -> None:
        pass

    def acquire(self, *, event, task, as_of_date):
        type(self).call_count += 1
        is_feedback_retry_task = "feedback_retry" in str(getattr(task, "reason_from_memory", "") or "")
        if not is_feedback_retry_task:
            web_task_id = "WEBTASK-CHAINED-PRE"
            web_result_id = "WEBRESULT-CHAINED-PRE"
            web_task = {
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "삼성전자 1차 검색",
                "primitive_gap": task.primitive_gap,
            }
            web_result = {
                "web_result_id": web_result_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "삼성전자 1차 검색",
                "provider_name": "NaverFreeSearchProvider",
                "url": "https://example.test/tag/samsung",
                "title": "주식 태그 목록",
                "selection_status": "REJECTED_NON_EVIDENCE_RESULT_METADATA",
            }
            web_rejected = {
                "web_rejected_id": "WEBREJECT-CHAINED-PRE",
                "web_result_id": web_result_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "삼성전자 1차 검색",
                "provider_name": "NaverFreeSearchProvider",
                "url": "https://example.test/tag/samsung",
                "title": "주식 태그 목록",
                "rejection_reason": "web_result_stock_list_or_channel_page_not_source_document",
                "snippet_score_forbidden": True,
            }
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class="IndustryMedia",
                provider_name="NaverFreeSearchProvider",
                status="NO_EVIDENCE_FOUND",
                provider_errors=("general search is not a score source",),
                budget_used={"queries": 1, "candidates": 1, "fetches": 0},
                stop_reason="unit_pre_extraction_rejected",
                web_search_tasks=(web_task,),
                web_search_results=(web_result,),
                web_rejected_documents=(web_rejected,),
            )
        if not type(self).post_extraction_emitted:
            type(self).post_extraction_emitted = True
            web_task_id = "WEBTASK-CHAINED-POST"
            web_result_id = "WEBRESULT-CHAINED-POST"
            web_fetch_id = "WEBFETCH-CHAINED-POST"
            web_task = {
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "삼성전자 2차 IR 검색",
                "primitive_gap": task.primitive_gap,
            }
            web_result = {
                "web_result_id": web_result_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "삼성전자 2차 IR 검색",
                "provider_name": "NaverFreeSearchProvider",
                "url": "https://news.example/unrelated",
                "title": "업계 소식 모음",
                "selection_status": "SELECTED_FOR_FETCH",
            }
            web_fetched = {
                "web_fetch_id": web_fetch_id,
                "web_result_id": web_result_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "삼성전자 2차 IR 검색",
                "provider_name": "NaverFreeSearchProvider",
                "url": "https://news.example/unrelated",
                "title": "업계 소식 모음",
                "document_id": "DOC-CHAINED-POST",
            }
            web_rejected = {
                "web_rejected_id": "WEBREJECT-CHAINED-POST",
                "web_result_id": web_result_id,
                "web_fetch_id": web_fetch_id,
                "web_task_id": web_task_id,
                "task_id": task.task_id,
                "source_task_id": task.task_id,
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "query": "삼성전자 2차 IR 검색",
                "provider_name": "NaverFreeSearchProvider",
                "status": "REJECTED",
                "url": "https://news.example/unrelated",
                "title": "업계 소식 모음",
                "rejection_phase": "post_extraction_evidence_os",
                "rejection_reason": "post_extraction_no_score_eligible_claim",
                "not_eligible_reasons": [
                    "source_task_provider_error_score_block:general_search_not_score_source",
                    "target_scope_not_allowed:UNRELATED",
                    "target_not_direct:NOT_TARGET_SCOPED",
                ],
                "raw_assertion_ids": ["RAWLLM-CHAINED-POST"],
                "rejected_claim_ids": ["CLM-CHAINED-POST"],
                "accepted_claim_ids": [],
                "snippet_score_forbidden": True,
            }
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class="IndustryMedia",
                provider_name="NaverFreeSearchProvider",
                status="NO_EVIDENCE_FOUND",
                fetched_document_ids=("DOC-CHAINED-POST",),
                document_urls=("https://news.example/unrelated",),
                document_hashes=("hash-chained-post",),
                provider_errors=("general search is not a score source",),
                budget_used={"queries": 1, "candidates": 1, "fetches": 1},
                stop_reason="unit_post_extraction_rejected",
                web_search_tasks=(web_task,),
                web_search_results=(web_result,),
                web_fetched_documents=(web_fetched,),
                web_rejected_documents=(web_rejected,),
            )
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class="ReportPDF",
            provider_name="UnitReportProvider",
            status="NO_EVIDENCE_FOUND",
            provider_errors=("unit_no_matching_report_after_chained_retry",),
            budget_used={"queries": 1, "candidates": 0, "fetches": 0},
            stop_reason="unit_no_more_evidence",
        )


def _rejected_bundle(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    document = EvidenceDocument(
        document_id="DOC-UNIT-REJECTED",
        canonical_url="https://dart.example/rejected",
        source_type=SourceType.FILING,
        source_name="OpenDART",
        content_hash="hash-unit-rejected",
        published_at=date(2026, 6, 29),
    )
    anchor = EvidenceAnchor(
        anchor_id="ANCH-UNIT-REJECTED",
        document_id=document.document_id,
        anchor_type=AnchorType.TEXT_SPAN,
        locator="char:0:20",
        exact_text="삼성전자 시설투자 종료일 연장 정정",
        anchor_verified=True,
    )
    raw = RawAssertion(
        raw_assertion_id="RAW-UNIT-REJECTED",
        anchor_id=anchor.anchor_id,
        subject_text="삼성전자",
        predicate="시설투자 종료일 연장 정정",
        object_text="volume growth 직접 증거 아님",
        value="volume growth 직접 증거 아님",
        polarity_proposal=Polarity.NORMAL,
        exact_quote=anchor.exact_text,
    )
    claim = AdjudicatedClaim(
        claim_id="CLM-UNIT-REJECTED",
        raw_assertion_id=raw.raw_assertion_id,
        subject_entity_id="TICKER:005930",
        target_entity_id="TICKER:005930",
        relation_to_target=RelationToTarget.SELF,
        directness=Directness.DIRECT,
        verification_status=VerificationStatus.SEMANTIC_VERIFIED,
        target_scope_status=TargetScopeStatus.DIRECT,
        polarity=Polarity.NORMAL,
        temporal_status=TemporalStatus.CURRENT,
        semantic_status=SemanticStatus.PASS_,
        investigation_status=InvestigationStatus.COMPLETE,
        event_date=date(2026, 6, 29),
        adjudication_rationale="direct current claim but not score primitive",
        source_document_id=document.document_id,
        source_anchor_id=anchor.anchor_id,
        source_assertion_id="SRCASSERT-UNIT-REJECTED",
    )
    mapping = PrimitiveMappingProposal.build(
        claim_id=claim.claim_id,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_id="volume_growth_visible",
        support_direction=SupportDirection.NEUTRAL,
        mapping_status=MappingStatus.REJECTED,
        rationale="mapping_not_accepted:REJECTED",
        contract_rule_id="volume_growth_visible",
    )
    ledger = AppendOnlyEvidenceLedger()
    ledger.append_claim(claim)
    ledger.append_mapping(mapping)
    task = SourceTask(
        task_id="TASK-UNIT-REJECTED",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_gap="volume_growth_visible",
        task_type="positive_verify",
        preferred_source_classes=("DART",),
        fallback_source_classes=("TrustedNews",),
        max_queries=1,
        max_candidates=5,
        max_fetches=1,
    )
    execution = SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status="NO_EVIDENCE_FOUND",
        fetched_document_ids=(document.document_id,),
        document_urls=(document.canonical_url or "",),
        document_hashes=(document.content_hash,),
        evidence_anchor_ids=(anchor.anchor_id,),
        raw_assertion_ids=(raw.raw_assertion_id,),
        adjudicated_claim_ids=(claim.claim_id,),
        rejected_claim_ids=(claim.claim_id,),
        not_eligible_reasons=("mapping_not_accepted:REJECTED",),
        budget_used={"queries": 1, "candidates": 1, "fetches": 1},
        stop_reason="no_score_eligible_real_claim",
    )
    return EvidenceOSExecutionBundleV4(
        ledger=ledger,
        executions=(execution,),
        documents={document.document_id: document},
        anchors={anchor.anchor_id: anchor},
        document_text_by_id={document.document_id: anchor.exact_text},
        extraction_audit={},
        raw_assertions={raw.raw_assertion_id: raw},
    )


def _bundle_with_rerouted_acceptance_and_rejected_claim(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    bundle = _rejected_bundle(event)
    accepted_execution = SourceTaskExecutionV4(
        task_id="TASK-UNIT-REROUTED",
        source_task={
            "task_id": "TASK-UNIT-REROUTED",
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "primitive_gap": "official_disclosure_status_current",
        },
        status="EVIDENCE_OS_ACCEPTED",
        fetched_document_ids=("DOC-UNIT-REJECTED",),
        document_urls=("https://dart.example/rejected",),
        document_hashes=("hash-unit-rejected",),
        evidence_anchor_ids=("ANCH-UNIT-REJECTED",),
        accepted_claim_ids=("CLM-UNIT-REROUTED",),
        direct_accepted_claim_ids=(),
        rerouted_accepted_claim_ids=("CLM-UNIT-REROUTED",),
        accepted_primitive_ids=("medium_term_revision_visibility",),
        primitive_gap_unsatisfied_ids=("official_disclosure_status_current",),
        satisfies_source_task=False,
        satisfaction_type="REROUTED_ACCEPTED_CLAIM",
        stop_reason="rerouted_claim_accepted_original_gap_unsatisfied",
    )
    return EvidenceOSExecutionBundleV4(
        ledger=bundle.ledger,
        executions=(*bundle.executions, accepted_execution),
        documents=bundle.documents,
        anchors=bundle.anchors,
        document_text_by_id=bundle.document_text_by_id,
        extraction_audit=bundle.extraction_audit,
        raw_assertions=bundle.raw_assertions,
    )


def _rerouted_only_bundle(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    execution = SourceTaskExecutionV4(
        task_id="TASK-UNIT-REROUTED-ONLY",
        source_task={
            "task_id": "TASK-UNIT-REROUTED-ONLY",
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "primitive_gap": "hbm_capacity_pre_sold",
            "preferred_source_classes": ("CompanyGuide",),
            "fallback_source_classes": ("IssuerIR",),
        },
        status="EVIDENCE_OS_ACCEPTED",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_gap="hbm_capacity_pre_sold",
        source_class="CompanyGuide",
        provider_name="CompanyGuide",
        preferred_source_classes=("CompanyGuide",),
        fallback_source_classes=("IssuerIR",),
        fetched_document_ids=("DOC-UNIT-CG-CONSENSUS",),
        document_urls=("https://wcomp.fnguide.com",),
        document_hashes=("hash-unit-cg-consensus",),
        evidence_anchor_ids=("ANCH-UNIT-CG-CONSENSUS",),
        accepted_claim_ids=("CLM-UNIT-CG-CONSENSUS",),
        direct_accepted_claim_ids=(),
        rerouted_accepted_claim_ids=("CLM-UNIT-CG-CONSENSUS",),
        accepted_primitive_ids=("medium_term_revision_visibility",),
        primitive_gap_unsatisfied_ids=("hbm_capacity_pre_sold",),
        satisfies_source_task=False,
        satisfaction_type="REROUTED_ACCEPTED_CLAIM",
        budget_used={"queries": 1, "candidates": 1, "fetches": 1},
        stop_reason="rerouted_claim_accepted_original_gap_unsatisfied",
    )
    return EvidenceOSExecutionBundleV4(
        ledger=AppendOnlyEvidenceLedger(),
        executions=(execution,),
        documents={},
        anchors={},
        document_text_by_id={},
        extraction_audit={},
    )


def _rerouted_bundle_with_direct_acceptance(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    bundle = _rerouted_only_bundle(event)
    direct = SourceTaskExecutionV4(
        task_id="TASK-UNIT-REROUTED-DIRECT",
        source_task={
            "task_id": "TASK-UNIT-REROUTED-DIRECT",
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "primitive_gap": "hbm_capacity_pre_sold",
        },
        status="EVIDENCE_OS_ACCEPTED",
        fetched_document_ids=("DOC-UNIT-IR-CAPACITY",),
        document_urls=("https://ir.example/capacity",),
        document_hashes=("hash-unit-ir-capacity",),
        evidence_anchor_ids=("ANCH-UNIT-IR-CAPACITY",),
        accepted_claim_ids=("CLM-UNIT-IR-CAPACITY",),
        direct_accepted_claim_ids=("CLM-UNIT-IR-CAPACITY",),
        accepted_primitive_ids=("hbm_capacity_pre_sold",),
        primitive_gap_satisfied_ids=("hbm_capacity_pre_sold",),
        satisfies_source_task=True,
        satisfaction_type="DIRECT_ACCEPTED_CLAIM",
        stop_reason="accepted_direct_source_task_claim",
    )
    return EvidenceOSExecutionBundleV4(
        ledger=bundle.ledger,
        executions=(*bundle.executions, direct),
        documents=bundle.documents,
        anchors=bundle.anchors,
        document_text_by_id=bundle.document_text_by_id,
        extraction_audit=bundle.extraction_audit,
    )


def _bundle_with_direct_acceptance_and_rejected_claim(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    bundle = _rejected_bundle(event)
    accepted_execution = SourceTaskExecutionV4(
        task_id="TASK-UNIT-DIRECT",
        source_task={
            "task_id": "TASK-UNIT-DIRECT",
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "primitive_gap": "volume_growth_visible",
        },
        status="EVIDENCE_OS_ACCEPTED",
        fetched_document_ids=("DOC-UNIT-REJECTED",),
        document_urls=("https://dart.example/rejected",),
        document_hashes=("hash-unit-rejected",),
        evidence_anchor_ids=("ANCH-UNIT-REJECTED",),
        accepted_claim_ids=("CLM-UNIT-DIRECT",),
        direct_accepted_claim_ids=("CLM-UNIT-DIRECT",),
        satisfies_source_task=True,
        satisfaction_type="DIRECT_ACCEPTED_CLAIM",
        stop_reason="accepted_direct_source_task_claim",
    )
    return EvidenceOSExecutionBundleV4(
        ledger=bundle.ledger,
        executions=(*bundle.executions, accepted_execution),
        documents=bundle.documents,
        anchors=bundle.anchors,
        document_text_by_id=bundle.document_text_by_id,
        extraction_audit=bundle.extraction_audit,
        raw_assertions=bundle.raw_assertions,
    )


def _bundle_with_direct_acceptance_and_external_llm_rejected_claim(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    bundle = _bundle_with_direct_acceptance_and_rejected_claim(event)
    rejected_execution = replace(
        bundle.executions[0],
        source_class="TrustedNews",
        provider_name="NaverFreeSearchProvider",
    )
    raw_rejection = {
        "raw_assertion_rejection_id": "RAWREJ-UNIT-EXTERNAL-LLM",
        "source_task_id": rejected_execution.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "raw_assertion_id": "RAWLLM-UNIT-REJECTED",
        "claim_id": "CLM-UNIT-REJECTED",
        "adjudicated_claim_id": "CLM-UNIT-REJECTED",
        "rejection_stage": "score_eligibility",
        "rejection_reason": "mapping_not_accepted:REJECTED",
        "not_eligible_reasons": ("mapping_not_accepted:REJECTED",),
        "mapping_rationale": "external LLM claim reached Evidence OS but did not satisfy the source task primitive",
        "mapping_status": "REJECTED",
        "mapped_primitive_id": "volume_growth_visible",
        "support_direction": "NEUTRAL",
        "target_scope_status": "DIRECT",
        "directness": "DIRECT",
        "semantic_status": "PASS",
        "temporal_status": "CURRENT",
        "polarity": "NORMAL",
    }
    web_fetched = {
        "web_fetched_id": "WEBFETCH-UNIT-EXTERNAL-LLM",
        "task_id": rejected_execution.task_id,
        "source_task_id": rejected_execution.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "provider_name": "NaverFreeSearchProvider",
        "source_class": "TrustedNews",
        "document_id": "DOC-UNIT-REJECTED",
        "status": "FETCHED_FULL_SOURCE",
        "url": "https://news.example/direct-source",
    }
    return EvidenceOSExecutionBundleV4(
        ledger=bundle.ledger,
        executions=(rejected_execution, bundle.executions[1]),
        documents=bundle.documents,
        anchors=bundle.anchors,
        document_text_by_id=bundle.document_text_by_id,
        extraction_audit=bundle.extraction_audit,
        raw_assertions=bundle.raw_assertions,
        web_fetched_documents=(web_fetched,),
        raw_assertion_rejections=(raw_rejection,),
    )


def _source_rejected_bundle(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    task = SourceTask(
        task_id="TASK-UNIT-SOURCE-REJECTED",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_gap="named_customer_or_customer_quality",
        task_type="positive_verify",
        preferred_source_classes=("TrustedNews",),
        fallback_source_classes=("CompanyNewsroom", "ReportPDF"),
        query_intents=("삼성전자 기존 검색",),
        max_queries=1,
        max_candidates=5,
        max_fetches=1,
    )
    execution = SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status="NO_EVIDENCE_FOUND",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id=task.archetype_id,
        primitive_gap=task.primitive_gap,
        source_class="TrustedNews",
        provider_name="NaverFreeSearchProvider",
        preferred_source_classes=task.preferred_source_classes,
        fallback_source_classes=task.fallback_source_classes,
        forbidden_source_classes=task.forbidden_source_classes,
        requested_source_classes=(*task.preferred_source_classes, *task.fallback_source_classes),
        budget_used={"queries": 1, "candidates": 2, "fetches": 0},
        stop_reason="all_web_results_rejected_before_fetch",
    )
    web_task = {
        "web_task_id": "WEBTASK-UNIT-SOURCE-REJECTED",
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "primitive_gap": task.primitive_gap,
        "query": "삼성전자 기존 검색",
        "provider_name": "NaverFreeSearchProvider",
        "status": "SEARCH_EXECUTED",
        "result_count": 2,
        "fetched_document_count": 0,
        "rejected_document_count": 2,
    }
    web_results = (
        {
            "web_result_id": "WEBRESULT-UNIT-1",
            "web_task_id": web_task["web_task_id"],
            "task_id": task.task_id,
            "source_task_id": task.task_id,
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "query": "삼성전자 기존 검색",
            "provider_name": "NaverFreeSearchProvider",
            "url": "https://example.test/tag/samsung",
            "title": "주식 태그 목록",
            "selected_for_fetch": False,
            "selection_status": "REJECTED_NON_EVIDENCE_RESULT_METADATA",
        },
        {
            "web_result_id": "WEBRESULT-UNIT-2",
            "web_task_id": web_task["web_task_id"],
            "task_id": task.task_id,
            "source_task_id": task.task_id,
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "query": "삼성전자 기존 검색",
            "provider_name": "NaverFreeSearchProvider",
            "url": "https://example.test/channel/market",
            "title": "시장 채널",
            "selected_for_fetch": False,
            "selection_status": "REJECTED_NON_EVIDENCE_RESULT_METADATA",
        },
    )
    web_rejected = tuple(
        {
            "web_rejected_id": f"WEBREJECT-UNIT-{index}",
            "web_result_id": result["web_result_id"],
            "task_id": task.task_id,
            "source_task_id": task.task_id,
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "query": result["query"],
            "provider_name": result["provider_name"],
            "status": "REJECTED",
            "url": result["url"],
            "title": result["title"],
            "rejection_reason": "web_result_stock_list_or_channel_page_not_source_document",
            "snippet_score_forbidden": True,
        }
        for index, result in enumerate(web_results, start=1)
    )
    return EvidenceOSExecutionBundleV4(
        ledger=AppendOnlyEvidenceLedger(),
        executions=(execution,),
        documents={},
        anchors={},
        document_text_by_id={},
        extraction_audit={},
        web_search_tasks=(web_task,),
        web_search_results=web_results,
        web_rejected_documents=web_rejected,
    )


def _low_quality_blog_source_rejected_bundle(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    task = SourceTask(
        task_id="TASK-UNIT-LOW-QUALITY-BLOG",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_gap="named_customer_or_customer_quality",
        task_type="positive_verify",
        preferred_source_classes=("NaverSearch",),
        fallback_source_classes=("CompanyNewsroom", "ReportPDF"),
        query_intents=("삼성전자 HBM 고객 배정 개인 블로그",),
        max_queries=1,
        max_candidates=5,
        max_fetches=1,
    )
    execution = SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status="NO_EVIDENCE_FOUND",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id=task.archetype_id,
        primitive_gap=task.primitive_gap,
        source_class="NaverSearch",
        provider_name="NaverFreeSearchProvider",
        preferred_source_classes=task.preferred_source_classes,
        fallback_source_classes=task.fallback_source_classes,
        forbidden_source_classes=task.forbidden_source_classes,
        requested_source_classes=(*task.preferred_source_classes, *task.fallback_source_classes),
        budget_used={"queries": 1, "candidates": 1, "fetches": 0, "fetch_attempts": 0},
        stop_reason="low_quality_blog_rejected_before_fetch",
    )
    web_task = {
        "web_task_id": "WEBTASK-UNIT-LOW-QUALITY-BLOG",
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "primitive_gap": task.primitive_gap,
        "query": "삼성전자 HBM 고객 배정 개인 블로그",
        "provider_name": "NaverFreeSearchProvider",
        "status": "SEARCH_EXECUTED",
        "result_count": 1,
        "fetched_document_count": 0,
        "rejected_document_count": 1,
    }
    web_result = {
        "web_result_id": "WEBRESULT-UNIT-LOW-QUALITY-BLOG",
        "web_task_id": web_task["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": "삼성전자 HBM 고객 배정 개인 블로그",
        "provider_name": "NaverFreeSearchProvider",
        "url": "https://some-personal-blog.tistory.com/1234",
        "title": "삼성전자 HBM 고객 배정 개인 블로그 정리",
        "selected_for_fetch": False,
        "selection_status": "REJECTED_NON_EVIDENCE_RESULT_METADATA",
    }
    web_rejected = {
        "web_rejected_id": "WEBREJECT-UNIT-LOW-QUALITY-BLOG",
        "web_result_id": web_result["web_result_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": web_result["query"],
        "provider_name": web_result["provider_name"],
        "status": "REJECTED",
        "url": web_result["url"],
        "title": web_result["title"],
        "rejection_reason": "web_result_low_quality_blog_or_social_not_score_source",
        "snippet_score_forbidden": True,
    }
    return EvidenceOSExecutionBundleV4(
        ledger=AppendOnlyEvidenceLedger(),
        executions=(execution,),
        documents={},
        anchors={},
        document_text_by_id={},
        extraction_audit={},
        web_search_tasks=(web_task,),
        web_search_results=(web_result,),
        web_rejected_documents=(web_rejected,),
    )


def _source_lineage_unverified_original_rejected_bundle(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    task = SourceTask(
        task_id="TASK-UNIT-SOURCE-LINEAGE",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_gap="named_customer_or_customer_quality",
        task_type="positive_verify",
        preferred_source_classes=("TrustedNews",),
        fallback_source_classes=("CompanyNewsroom", "ReportPDF"),
        query_intents=("삼성전자 HBM 고객 배정 뉴스",),
        max_queries=1,
        max_candidates=5,
        max_fetches=1,
    )
    web_task = {
        "web_task_id": "WEBTASK-UNIT-SOURCE-LINEAGE",
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "primitive_gap": task.primitive_gap,
        "query": "삼성전자 HBM 고객 배정 뉴스",
        "provider_name": "NaverFreeSearchProvider",
        "status": "SEARCH_EXECUTED",
        "result_count": 1,
        "fetched_document_count": 1,
        "rejected_document_count": 1,
    }
    web_result = {
        "web_result_id": "WEBRESULT-UNIT-SOURCE-LINEAGE",
        "web_task_id": web_task["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": "삼성전자 HBM 고객 배정 뉴스",
        "provider_name": "NaverFreeSearchProvider",
        "url": "https://news.example.test/samsung-hbm-customer",
        "title": "삼성전자 HBM 고객 배정 보도",
        "selected_for_fetch": True,
        "selection_status": "SELECTED_FOR_FETCH",
    }
    web_fetched = {
        "web_fetch_id": "WEBFETCH-UNIT-SOURCE-LINEAGE",
        "web_result_id": web_result["web_result_id"],
        "web_task_id": web_task["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": web_result["query"],
        "provider_name": web_result["provider_name"],
        "url": web_result["url"],
        "title": web_result["title"],
        "document_id": "DOC-UNIT-SOURCE-LINEAGE",
        "snippet_score_forbidden": True,
    }
    web_rejected = {
        "web_rejected_id": "WEBREJECT-UNIT-SOURCE-LINEAGE",
        "web_result_id": web_result["web_result_id"],
        "web_fetch_id": web_fetched["web_fetch_id"],
        "web_task_id": web_task["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": web_result["query"],
        "provider_name": web_result["provider_name"],
        "status": "REJECTED",
        "url": web_result["url"],
        "title": web_result["title"],
        "rejection_phase": "post_extraction_evidence_os",
        "rejection_reason": "post_extraction_no_score_eligible_claim",
        "not_eligible_reasons": [
            "source_task_provider_error_score_block:general_search_not_score_source",
            "source_provider_document_type_mismatch:TrustedNews:general_web_search_provider",
            "source_lineage_unverified_original:TrustedNews:general_web_search_provider",
        ],
        "provider_errors": ["trusted_news_provider_not_configured; general search is not a score source"],
        "raw_assertion_ids": [],
        "rejected_claim_ids": [],
        "accepted_claim_ids": [],
        "snippet_score_forbidden": True,
    }
    execution = SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status="NO_EVIDENCE_FOUND",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id=task.archetype_id,
        primitive_gap=task.primitive_gap,
        source_class="TrustedNews",
        provider_name="NaverFreeSearchProvider",
        preferred_source_classes=task.preferred_source_classes,
        fallback_source_classes=task.fallback_source_classes,
        requested_source_classes=(*task.preferred_source_classes, *task.fallback_source_classes),
        fetched_document_ids=("DOC-UNIT-SOURCE-LINEAGE",),
        document_urls=("https://news.example.test/samsung-hbm-customer",),
        document_hashes=("hash-unit-source-lineage",),
        not_eligible_reasons=tuple(web_rejected["not_eligible_reasons"]),
        provider_errors=tuple(web_rejected["provider_errors"]),
        budget_used={"queries": 1, "candidates": 1, "fetches": 1},
        stop_reason="source_lineage_unverified_original",
    )
    return EvidenceOSExecutionBundleV4(
        ledger=AppendOnlyEvidenceLedger(),
        executions=(execution,),
        documents={},
        anchors={},
        document_text_by_id={},
        extraction_audit={},
        web_search_tasks=(web_task,),
        web_search_results=(web_result,),
        web_fetched_documents=(web_fetched,),
        web_rejected_documents=(web_rejected,),
    )


def _source_lineage_retry_task(
    event: CandidateEventV2,
    *,
    task_id: str,
    preferred_source_classes: tuple[str, ...],
    fallback_source_classes: tuple[str, ...],
    query_intents: tuple[str, ...],
) -> SourceTask:
    return SourceTask(
        task_id=task_id,
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_gap="named_customer_or_customer_quality",
        task_type="positive_verify",
        preferred_source_classes=preferred_source_classes,
        fallback_source_classes=fallback_source_classes,
        query_intents=query_intents,
        max_queries=1,
        max_candidates=5,
        max_fetches=1,
        reason_from_memory="unit source lineage retry",
    )


def _source_rejected_bundle_with_direct_acceptance(event: CandidateEventV2) -> EvidenceOSExecutionBundleV4:
    bundle = _source_rejected_bundle(event)
    accepted_execution = SourceTaskExecutionV4(
        task_id="TASK-UNIT-SOURCE-DIRECT",
        source_task={
            "task_id": "TASK-UNIT-SOURCE-DIRECT",
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "company_name": event.company_name,
            "primitive_gap": "named_customer_or_customer_quality",
        },
        status="EVIDENCE_OS_ACCEPTED",
        fetched_document_ids=("DOC-UNIT-SOURCE-DIRECT",),
        document_urls=("https://ir.example/direct",),
        document_hashes=("hash-unit-source-direct",),
        evidence_anchor_ids=("ANCH-UNIT-SOURCE-DIRECT",),
        accepted_claim_ids=("CLM-UNIT-SOURCE-DIRECT",),
        direct_accepted_claim_ids=("CLM-UNIT-SOURCE-DIRECT",),
        satisfies_source_task=True,
        satisfaction_type="DIRECT_ACCEPTED_CLAIM",
        stop_reason="accepted_direct_source_task_claim",
    )
    return EvidenceOSExecutionBundleV4(
        ledger=bundle.ledger,
        executions=(*bundle.executions, accepted_execution),
        documents=bundle.documents,
        anchors=bundle.anchors,
        document_text_by_id=bundle.document_text_by_id,
        extraction_audit=bundle.extraction_audit,
        web_search_tasks=bundle.web_search_tasks,
        web_search_results=bundle.web_search_results,
        web_rejected_documents=bundle.web_rejected_documents,
    )


def _post_extraction_source_rejected_bundle(
    event: CandidateEventV2,
    *,
    with_direct_acceptance: bool = False,
) -> EvidenceOSExecutionBundleV4:
    task = SourceTask(
        task_id="TASK-UNIT-POST-EXTRACT-REJECTED",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
        primitive_gap="margin_bridge_visible",
        task_type="positive_verify",
        preferred_source_classes=("IndustryMedia",),
        fallback_source_classes=("TrustedNews",),
        query_intents=("삼성전자 마진 브리지 원문",),
        max_queries=1,
        max_candidates=5,
        max_fetches=1,
    )
    web_task = {
        "web_task_id": "WEBTASK-UNIT-POST-EXTRACT",
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "primitive_gap": task.primitive_gap,
        "query": "삼성전자 마진 브리지 원문",
        "search_provider": "NaverSearch",
    }
    web_result = {
        "web_result_id": "WEBRESULT-UNIT-POST-EXTRACT",
        "web_task_id": web_task["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": "삼성전자 마진 브리지 원문",
        "provider_name": "NaverFreeSearchProvider",
        "url": "https://blog.example/post",
        "title": "삼성전자 마진 브리지 블로그 글",
        "selected_for_fetch": True,
        "selection_status": "SELECTED_FOR_FETCH",
    }
    web_fetched = {
        "web_fetch_id": "WEBFETCH-UNIT-POST-EXTRACT",
        "web_result_id": web_result["web_result_id"],
        "web_task_id": web_task["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": web_result["query"],
        "provider_name": web_result["provider_name"],
        "url": web_result["url"],
        "title": web_result["title"],
        "document_id": "DOC-UNIT-POST-EXTRACT",
    }
    web_rejected = {
        "web_rejected_id": "WEBREJECT-UNIT-POST-EXTRACT",
        "web_result_id": web_result["web_result_id"],
        "web_fetch_id": web_fetched["web_fetch_id"],
        "web_task_id": web_task["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": web_result["query"],
        "provider_name": web_result["provider_name"],
        "status": "REJECTED",
        "url": web_result["url"],
        "title": web_result["title"],
        "rejection_phase": "post_extraction_evidence_os",
        "rejection_reason": "post_extraction_no_score_eligible_claim",
        "not_eligible_reasons": [
            "source_task_provider_error_score_block:general_search_not_score_source",
            "source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider",
            "primitive_mapping_rejected:no_allowed_primitive_for_predicate",
        ],
        "provider_errors": ["trusted_news_provider_not_configured; general search is not a score source"],
        "raw_assertion_ids": ["RAWLLM-UNIT-POST"],
        "rejected_claim_ids": ["CLM-UNIT-POST"],
        "accepted_claim_ids": [],
        "snippet_score_forbidden": True,
    }
    execution = SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status="NO_EVIDENCE_FOUND",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id=task.archetype_id,
        primitive_gap=task.primitive_gap,
        source_class="IndustryMedia",
        provider_name="NaverFreeSearchProvider",
        preferred_source_classes=task.preferred_source_classes,
        fallback_source_classes=task.fallback_source_classes,
        requested_source_classes=(*task.preferred_source_classes, *task.fallback_source_classes),
        fetched_document_ids=("DOC-UNIT-POST-EXTRACT",),
        document_urls=("https://blog.example/post",),
        document_hashes=("hash-unit-post-extract",),
        raw_assertion_ids=("RAWLLM-UNIT-POST",),
        rejected_claim_ids=("CLM-UNIT-POST",),
        not_eligible_reasons=tuple(web_rejected["not_eligible_reasons"]),
        provider_errors=tuple(web_rejected["provider_errors"]),
        budget_used={"queries": 1, "candidates": 1, "fetches": 1},
        stop_reason="no_score_eligible_real_claim",
    )
    executions = [execution]
    if with_direct_acceptance:
        executions.append(
            SourceTaskExecutionV4(
                task_id="TASK-UNIT-POST-DIRECT",
                source_task={
                    "task_id": "TASK-UNIT-POST-DIRECT",
                    "candidate_event_id": event.candidate_event_id,
                    "symbol": event.symbol,
                    "company_name": event.company_name,
                    "primitive_gap": "contract_amount_to_prior_sales",
                },
                status="EVIDENCE_OS_ACCEPTED",
                fetched_document_ids=("DOC-UNIT-POST-DIRECT",),
                document_urls=("https://dart.example/direct",),
                document_hashes=("hash-unit-post-direct",),
                evidence_anchor_ids=("ANCH-UNIT-POST-DIRECT",),
                accepted_claim_ids=("CLM-UNIT-POST-DIRECT",),
                direct_accepted_claim_ids=("CLM-UNIT-POST-DIRECT",),
                satisfies_source_task=True,
                satisfaction_type="DIRECT_ACCEPTED_CLAIM",
                stop_reason="accepted_direct_source_task_claim",
            )
        )
    return EvidenceOSExecutionBundleV4(
        ledger=AppendOnlyEvidenceLedger(),
        executions=tuple(executions),
        documents={},
        anchors={},
        document_text_by_id={},
        extraction_audit={},
        web_search_tasks=(web_task,),
        web_search_results=(web_result,),
        web_fetched_documents=(web_fetched,),
        web_rejected_documents=(web_rejected,),
    )


def _policy_rejected_external_task_bundle(
    event: CandidateEventV2,
    *,
    with_direct_acceptance: bool = False,
) -> EvidenceOSExecutionBundleV4:
    task = SourceTask(
        task_id="TASK-UNIT-POLICY-REJECTED-EXTERNAL",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
        primitive_gap="delivery_schedule",
        task_type="positive_verify",
        preferred_source_classes=("CompanyNewsroom", "ReportPDF"),
        fallback_source_classes=("IndustryMedia",),
        query_intents=("삼성전자 공급계약 납품 일정 확인",),
        max_queries=1,
        max_candidates=5,
        max_fetches=1,
    )
    policy_rejected = SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status="REJECTED_BY_POLICY",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id=task.archetype_id,
        primitive_gap=task.primitive_gap,
        source_class="policy",
        provider_name="v4_policy_validator",
        preferred_source_classes=task.preferred_source_classes,
        fallback_source_classes=task.fallback_source_classes,
        forbidden_source_classes=task.forbidden_source_classes,
        requested_source_classes=(*task.preferred_source_classes, *task.fallback_source_classes),
        provider_errors=("official_solvable_gap_sent_to_general_web",),
        budget_used={"queries": 0, "candidates": 0, "fetches": 0},
        stop_reason="source_task_rejected_by_v4_policy",
    )
    executions = [policy_rejected]
    if with_direct_acceptance:
        executions.append(
            SourceTaskExecutionV4(
                task_id="TASK-UNIT-POLICY-DIRECT",
                source_task={
                    "task_id": "TASK-UNIT-POLICY-DIRECT",
                    "candidate_event_id": event.candidate_event_id,
                    "symbol": event.symbol,
                    "company_name": event.company_name,
                    "primitive_gap": "contract_amount_to_prior_sales",
                },
                status="EVIDENCE_OS_ACCEPTED",
                fetched_document_ids=("DOC-UNIT-POLICY-DIRECT",),
                document_urls=("https://dart.example/direct",),
                document_hashes=("hash-unit-policy-direct",),
                evidence_anchor_ids=("ANCH-UNIT-POLICY-DIRECT",),
                accepted_claim_ids=("CLM-UNIT-POLICY-DIRECT",),
                direct_accepted_claim_ids=("CLM-UNIT-POLICY-DIRECT",),
                satisfies_source_task=True,
                satisfaction_type="DIRECT_ACCEPTED_CLAIM",
                stop_reason="accepted_direct_source_task_claim",
            )
        )
    return EvidenceOSExecutionBundleV4(
        ledger=AppendOnlyEvidenceLedger(),
        executions=tuple(executions),
        documents={},
        anchors={},
        document_text_by_id={},
        extraction_audit={},
    )


class _RetryPlannerProvider:
    provider_name = "unit_retry_planner"
    provider_mode = "real"
    fake_provider = False
    real_provider = True
    model = "unit"
    endpoint = "unit"

    def __init__(self, output: LLMPlannerOutputV2) -> None:
        self.output = output
        self.call_count = 0
        self.last_existing_evidence_by_event_id = {}

    def plan_many(self, *, events, memory_cards, existing_evidence_by_event_id=None):
        self.call_count += 1
        self.last_existing_evidence_by_event_id = dict(existing_evidence_by_event_id or {})
        return {event.candidate_event_id: self.output for event in events}


if __name__ == "__main__":
    unittest.main()
