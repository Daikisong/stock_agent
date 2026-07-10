from __future__ import annotations

import io
import json
import unittest
from contextlib import redirect_stdout
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.canonical_current_adapter import (
    adapt_census_snapshot_to_current_input,
)
from e2r.census.last_effective_thesis import LastEffectiveThesisState
from e2r.census.schemas import BaselineScanResult, UniverseInstrument
from e2r.census.source_timeline import SourceTimeline, SourceTimelineEvent
from e2r.cli.run_e2r_current_operation import main as current_cli_main
from e2r.production.metadata import stable_hash
from e2r.research_brain.runtime import (
    AtomicClaimPolarity,
    AtomicHardBreakSignal,
    AtomicPrimitiveAssessment,
    AtomicPrimitiveStatus,
    AtomicScoreClaim,
    AtomicScoreRule,
    AtomicScoreType,
    AtomicScoringInput,
    AtomicScoringScope,
    CanonicalStage,
    CensusDepthLevel,
    CurrentDeepOutcome,
    CurrentOperationRunnerConfig,
    CurrentOperationRunnerInput,
    CurrentTriggerSignal,
    CurrentTriggerType,
    DailyBaselineLane,
    DailyBaselineLaneStatus,
    DailyBaselineLaneType,
    DailyDeepExecution,
    DailyNextAction,
    DailyProviderKind,
    DailySourceTaskRecord,
    DailyTerminalStatus,
    DailyThesisLifecycle,
    DailyUniverseMember,
    audit_current_daily_census,
    current_operation_runner_input_from_mapping,
    decide_atomic_score_stage,
    run_current_daily_census,
    write_current_daily_census,
)


class CurrentOperationRunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.as_of_date = "2026-06-30"
        cls.targets = (
            ("T-RISK", "위험기업", CurrentTriggerType.RISK.value),
            ("T-OFFICIAL", "공시기업", CurrentTriggerType.OFFICIAL.value),
            ("T-EARN", "실적기업", CurrentTriggerType.EARNINGS.value),
            ("T-IR", "IR기업", CurrentTriggerType.IR.value),
            (
                "T-LEDGER",
                "기존원장기업",
                CurrentTriggerType.EXISTING_LEDGER.value,
            ),
            ("T-REPORT", "리포트기업", CurrentTriggerType.REPORT.value),
            ("T-NEWS", "뉴스기업", CurrentTriggerType.NEWS.value),
            ("T-MARKET", "시장기업", CurrentTriggerType.MARKET.value),
        )
        cls.universe = tuple(
            DailyUniverseMember(
                target_id=target_id,
                target_name=name,
                market="KOSPI",
                as_of_date=cls.as_of_date,
            )
            for target_id, name, _ in cls.targets
        )
        cls.baseline_lanes = tuple(
            DailyBaselineLane(
                target_id=target_id,
                as_of_date=cls.as_of_date,
                lane_type=lane.value,
                lane_status=DailyBaselineLaneStatus.OBSERVED.value,
                source_ids=(f"BASE-{target_id}-{lane.value}",),
                observed_date=cls.as_of_date,
            )
            for target_id, _, _ in cls.targets
            for lane in DailyBaselineLaneType
        )
        cls.triggers = tuple(
            CurrentTriggerSignal(
                signal_id=f"TRIGGER-{target_id}",
                target_id=target_id,
                observed_date=(
                    "2024-01-15"
                    if trigger_type == CurrentTriggerType.EXISTING_LEDGER.value
                    else cls.as_of_date
                ),
                trigger_type=trigger_type,
                source_id=f"TRIGGER-SOURCE-{target_id}",
            )
            for target_id, _, trigger_type in cls.targets
        )
        cls.full = cls._decision("T-OFFICIAL")
        cls.risk = cls._decision("T-RISK", risk=True)
        cls.source_pending = cls._decision("T-EARN", source_pending=True)
        cls.provider_pending = cls._decision("T-IR", provider_pending=True)
        cls.budget_pending = cls._decision(
            "T-LEDGER",
            sparse=True,
            observed_date="2024-01-15",
        )
        cls.decisions = (
            cls.risk,
            cls.full,
            cls.source_pending,
            cls.provider_pending,
            cls.budget_pending,
        )
        claim_by_id = {
            claim.claim_id: claim
            for decision in cls.decisions
            for claim in decision.claims
        }
        cls.claims = tuple(claim_by_id.values())
        source_task_specs = (
            ("T-RISK", 1, "DART", False),
            ("T-OFFICIAL", 1, "DART", False),
            ("T-OFFICIAL", 2, "COMPANY_IR", False),
            ("T-EARN", 1, "DART", False),
            ("T-EARN", 2, "GENERAL_WEB", True),
            ("T-IR", 1, "COMPANY_IR", False),
        )
        cls.source_tasks = tuple(
            DailySourceTaskRecord(
                task_id=f"TASK-{target_id}-{sequence}",
                target_id=target_id,
                question_task_id=f"QUESTION-{target_id}-{sequence}",
                source_class=source_class,
                max_queries=2,
                max_candidates=10,
                max_fetches=2,
                max_retries=1,
                allows_general_web=allows_general_web,
                official_gap_reasons=(
                    ("official_source_did_not_resolve_claim",)
                    if allows_general_web
                    else ()
                ),
                test_only=True,
            )
            for target_id, sequence, source_class, allows_general_web in (
                source_task_specs
            )
        )
        task_ids_by_target = {
            target_id: tuple(
                item.task_id
                for item in cls.source_tasks
                if item.target_id == target_id
            )
            for target_id, _, _ in cls.targets
        }
        trigger_by_target = {item.target_id: item for item in cls.triggers}
        cls.executions = (
            cls._execution(
                target_id="T-RISK",
                outcome=CurrentDeepOutcome.DISPROVED,
                decision=cls.risk,
                trigger=trigger_by_target["T-RISK"],
                llm_calls=1,
                source_task_ids=task_ids_by_target["T-RISK"],
                fetches=1,
            ),
            cls._execution(
                target_id="T-OFFICIAL",
                outcome=CurrentDeepOutcome.FULL_THESIS,
                decision=cls.full,
                trigger=trigger_by_target["T-OFFICIAL"],
                llm_calls=1,
                source_task_ids=task_ids_by_target["T-OFFICIAL"],
                fetches=2,
            ),
            cls._execution(
                target_id="T-EARN",
                outcome=CurrentDeepOutcome.SOURCE_PENDING,
                decision=cls.source_pending,
                trigger=trigger_by_target["T-EARN"],
                llm_calls=1,
                source_task_ids=task_ids_by_target["T-EARN"],
                fetches=1,
                general_web_fetches=1,
                official_gap_reasons=("official_source_did_not_resolve_claim",),
            ),
            cls._execution(
                target_id="T-IR",
                outcome=CurrentDeepOutcome.PROVIDER_PENDING,
                decision=cls.provider_pending,
                trigger=trigger_by_target["T-IR"],
                llm_calls=1,
                source_task_ids=task_ids_by_target["T-IR"],
                fetches=0,
            ),
            cls._execution(
                target_id="T-LEDGER",
                outcome=CurrentDeepOutcome.BUDGET_PENDING,
                decision=cls.budget_pending,
                trigger=trigger_by_target["T-LEDGER"],
                llm_calls=0,
                source_task_ids=(),
                fetches=0,
            ),
        )
        cls.config = CurrentOperationRunnerConfig(
            max_official_light_targets=8,
            max_deep_candidates=5,
            max_brain_candidates=5,
            max_acquisition_candidates=5,
            max_llm_calls_per_candidate=2,
            max_source_tasks_per_candidate=3,
            max_fetches_per_candidate=3,
            max_retries_per_candidate=1,
            max_general_web_fetches_per_candidate=1,
            max_runtime_seconds=120.0,
            test_mode=True,
        )
        cls.inputs = CurrentOperationRunnerInput(
            as_of_date=cls.as_of_date,
            universe=cls.universe,
            baseline_lanes=cls.baseline_lanes,
            triggers=cls.triggers,
            claims=cls.claims,
            source_tasks=cls.source_tasks,
            atomic_decisions=cls.decisions,
            deep_executions=cls.executions,
            config=cls.config,
        )
        cls.result = run_current_daily_census(cls.inputs)

    @classmethod
    def _rules(cls) -> tuple[AtomicScoreRule, ...]:
        primitive_ids = (
            "revision_direction",
            "fcf_quality",
            "contract_quality",
            "capacity_lock",
        )
        return tuple(
            AtomicScoreRule(
                primitive_id=primitive_id,
                component_key=f"component:{primitive_id}",
                max_points=25.0,
                material=primitive_id != "capacity_lock",
                green_required=primitive_id
                in {"contract_quality", "capacity_lock"},
            )
            for primitive_id in primitive_ids
        )

    @classmethod
    def _support_claim(
        cls,
        target_id: str,
        primitive_id: str,
        *,
        observed_date: str,
    ) -> AtomicScoreClaim:
        return AtomicScoreClaim(
            claim_id=f"CLAIM-{target_id}-{primitive_id}",
            target_id=target_id,
            primitive_id=primitive_id,
            observed_date=observed_date,
            content_hash=stable_hash(
                {"target_id": target_id, "primitive_id": primitive_id}
            ),
            source_ids=(f"SOURCE-{target_id}-{primitive_id}",),
            anchor_ids=(f"ANCHOR-{target_id}-{primitive_id}",),
            mapping_ids=(f"MAPPING-{target_id}-{primitive_id}",),
            polarity=AtomicClaimPolarity.SUPPORT.value,
            target_direct=True,
            current_open=True,
            source_backed=True,
            material=primitive_id != "capacity_lock",
            contradiction_resolved=True,
            historical_replay=False,
            mapping_accepted=True,
            score_eligible=True,
        )

    @classmethod
    def _decision(
        cls,
        target_id: str,
        *,
        risk: bool = False,
        source_pending: bool = False,
        provider_pending: bool = False,
        sparse: bool = False,
        observed_date: str | None = None,
    ):
        observed = observed_date or cls.as_of_date
        rules = cls._rules()
        claims = tuple(
            cls._support_claim(
                target_id,
                rule.primitive_id,
                observed_date=observed,
            )
            for rule in rules
            if not sparse or rule.primitive_id == "revision_direction"
        )
        claim_by_primitive = {item.primitive_id: item for item in claims}
        assessments = []
        for rule in rules:
            claim = claim_by_primitive.get(rule.primitive_id)
            missing = claim is None or (
                risk and rule.primitive_id == "contract_quality"
            )
            assessments.append(
                AtomicPrimitiveAssessment(
                    primitive_id=rule.primitive_id,
                    status=(
                        AtomicPrimitiveStatus.MISSING.value
                        if missing
                        else AtomicPrimitiveStatus.SATISFIED.value
                    ),
                    evidence_strength=0.0 if missing else 1.0,
                    support_claim_ids=() if missing else (claim.claim_id,),
                )
            )
        hard_break_signals = ()
        if risk:
            counter = AtomicScoreClaim(
                claim_id=f"CLAIM-{target_id}-HARD-BREAK",
                target_id=target_id,
                primitive_id="contract_cancelled",
                observed_date=cls.as_of_date,
                content_hash=stable_hash({"target_id": target_id, "risk": True}),
                source_ids=(f"SOURCE-{target_id}-HARD-BREAK",),
                anchor_ids=(f"ANCHOR-{target_id}-HARD-BREAK",),
                mapping_ids=(),
                polarity=AtomicClaimPolarity.COUNTER.value,
                target_direct=True,
                current_open=True,
                source_backed=True,
                material=True,
                contradiction_resolved=False,
                historical_replay=False,
                mapping_accepted=False,
                score_eligible=False,
            )
            claims = (*claims, counter)
            hard_break_signals = (
                AtomicHardBreakSignal(
                    signal_id=f"HARD-BREAK-{target_id}",
                    claim_id=counter.claim_id,
                    condition_id="material_contract_cancelled",
                    unresolved=True,
                ),
            )
        return decide_atomic_score_stage(
            AtomicScoringInput(
                target_id=target_id,
                as_of_date=cls.as_of_date,
                scope=AtomicScoringScope.FULL_THESIS.value,
                claims=claims,
                primitive_assessments=tuple(assessments),
                rules=rules,
                hard_break_signals=hard_break_signals,
                source_pending=source_pending,
                provider_pending=provider_pending,
                has_prior_live_thesis=risk,
            )
        )

    @classmethod
    def _execution(
        cls,
        *,
        target_id: str,
        outcome: CurrentDeepOutcome,
        decision,
        trigger: CurrentTriggerSignal,
        llm_calls: int,
        source_task_ids: tuple[str, ...],
        fetches: int,
        general_web_fetches: int = 0,
        official_gap_reasons: tuple[str, ...] = (),
    ) -> DailyDeepExecution:
        provider = (
            DailyProviderKind.FIXTURE.value
            if llm_calls
            else DailyProviderKind.NONE.value
        )
        return DailyDeepExecution(
            execution_id=f"EXEC-{target_id}",
            target_id=target_id,
            outcome=outcome.value,
            trigger_signal_ids=(trigger.signal_id,),
            terminal_reason=f"terminal:{outcome.value.lower()}",
            atomic_decision_id=decision.decision_id,
            source_task_ids=source_task_ids,
            provider_kind=provider,
            provider_trace_id=(f"PROVIDER-TRACE-{target_id}" if llm_calls else None),
            llm_calls=llm_calls,
            source_tasks=len(source_task_ids),
            fetches=fetches,
            retries=0,
            general_web_fetches=general_web_fetches,
            official_first_attempted=True,
            official_gap_reasons=official_gap_reasons,
            runtime_seconds=5.0,
        )

    def test_full_universe_has_baseline_timeline_thesis_depth_and_one_status(self) -> None:
        result = self.result
        self.assertEqual(len(result.universe), 8)
        self.assertEqual(len(result.baseline_lanes), 32)
        self.assertEqual(len(result.source_timelines), 8)
        self.assertEqual(len(result.thesis_states), 8)
        self.assertEqual(len(result.depth_decisions), 8)
        self.assertEqual(len(result.stage_statuses), 8)
        self.assertEqual(
            {item.target_id for item in result.stage_statuses},
            {item.target_id for item in result.universe},
        )
        self.assertEqual(result.audit["critical_count_sum"], 0)
        self.assertEqual(result.manifest["status"], "BOUNDED_DAILY_CENSUS_PASS")
        self.assertFalse(result.production_runtime_ready)

    def test_selective_depth_is_bounded_and_each_selected_candidate_terminates(self) -> None:
        selected = tuple(
            item for item in self.result.depth_decisions if item.selected_for_deep
        )
        self.assertEqual(len(selected), 5)
        self.assertEqual(len(self.result.deep_executions), 5)
        self.assertEqual(
            {item.outcome for item in self.result.deep_executions},
            {item.value for item in CurrentDeepOutcome},
        )
        for depth in self.result.depth_decisions:
            self.assertIn(CensusDepthLevel.L0_UNIVERSE.value, depth.completed_depths)
            self.assertIn(CensusDepthLevel.L1_BASELINE.value, depth.completed_depths)
        self.assertEqual(
            sum(
                CensusDepthLevel.L5_FULL_THESIS.value in item.completed_depths
                for item in self.result.depth_decisions
            ),
            1,
        )
        llm_targets = {
            item.target_id for item in self.result.deep_executions if item.llm_calls
        }
        self.assertTrue(
            llm_targets.issubset({item.target_id for item in selected})
        )
        self.assertLess(len(llm_targets), len(self.result.universe))
        self.assertEqual(len(self.result.source_tasks), 6)
        self.assertTrue(
            all(
                item.stop_condition == "stop_on_resolution"
                and item.max_queries > 0
                and item.max_candidates > 0
                and item.max_fetches > 0
                for item in self.result.source_tasks
            )
        )
        referenced_task_ids = tuple(
            task_id
            for execution in self.result.deep_executions
            for task_id in execution.source_task_ids
        )
        self.assertCountEqual(
            referenced_task_ids,
            (item.task_id for item in self.result.source_tasks),
        )

    def test_all_trigger_families_are_investigation_only(self) -> None:
        self.assertEqual(
            {item.trigger_type for item in self.result.triggers},
            {item.value for item in CurrentTriggerType},
        )
        trigger_events = tuple(
            event
            for timeline in self.result.source_timelines
            for event in timeline.events
            if event.role == "TRIGGER"
        )
        self.assertEqual(len(trigger_events), 8)
        self.assertTrue(all(item.candidate_event_eligible for item in trigger_events))
        self.assertTrue(
            all(not item.score_evidence_eligible for item in trigger_events)
        )
        self.assertEqual(
            self.result.audit["critical_counts"][
                "market_news_used_as_score_evidence"
            ],
            0,
        )

    def test_atomic_decisions_drive_full_risk_and_pending_statuses(self) -> None:
        by_target = {item.target_id: item for item in self.result.stage_statuses}
        full = by_target["T-OFFICIAL"]
        self.assertEqual(full.score_type, AtomicScoreType.FULL_E2R_100.value)
        self.assertEqual(full.score_value, 100.0)
        self.assertEqual(full.canonical_stage, CanonicalStage.STAGE_3_GREEN.value)
        self.assertTrue(full.score_finalization_allowed)
        self.assertEqual(full.terminal_status, DailyTerminalStatus.FULL_THESIS.value)

        risk = by_target["T-RISK"]
        self.assertEqual(risk.score_type, AtomicScoreType.NO_SCORE.value)
        self.assertIsNone(risk.score_value)
        self.assertEqual(risk.raw_reference_score, 75.0)
        self.assertEqual(risk.canonical_stage, CanonicalStage.STAGE_4C.value)
        self.assertEqual(risk.terminal_status, DailyTerminalStatus.DISPROVED.value)

        for target_id, terminal in (
            ("T-EARN", DailyTerminalStatus.SOURCE_PENDING.value),
            ("T-IR", DailyTerminalStatus.PROVIDER_PENDING.value),
            ("T-LEDGER", DailyTerminalStatus.BUDGET_PENDING.value),
        ):
            with self.subTest(target_id=target_id):
                status = by_target[target_id]
                self.assertEqual(status.terminal_status, terminal)
                self.assertNotEqual(status.score_type, AtomicScoreType.FULL_E2R_100.value)
                self.assertFalse(status.score_finalization_allowed)

    def test_old_but_open_claim_survives_without_recent_stage_cutoff(self) -> None:
        thesis = next(
            item
            for item in self.result.thesis_states
            if item.target_id == "T-LEDGER"
        )
        old_claim = next(
            item for item in self.claims if item.target_id == "T-LEDGER"
        )
        self.assertEqual(old_claim.observed_date, "2024-01-15")
        self.assertIn(old_claim.claim_id, thesis.current_open_claim_ids)
        self.assertEqual(thesis.lifecycle_status, DailyThesisLifecycle.NEEDS_REFRESH.value)
        self.assertFalse(thesis.recent_cutoff_applied)
        self.assertEqual(
            self.result.audit["critical_counts"][
                "current_open_claim_dropped_by_lookback"
            ],
            0,
        )

    def test_watchlist_exposes_score_confidence_claims_gaps_and_safe_action(self) -> None:
        self.assertEqual(len(self.result.watchlist), 8)
        for item in self.result.watchlist:
            payload = item.to_dict()
            for key in (
                "score_type",
                "confidence",
                "claim_ids",
                "missing_conditions",
                "gap_ids",
                "next_action",
            ):
                self.assertIn(key, payload)
            self.assertNotIn("매수", item.monitoring_label)
            self.assertNotIn("매도", item.monitoring_label)
        full = next(
            item for item in self.result.watchlist if item.target_id == "T-OFFICIAL"
        )
        self.assertEqual(
            full.next_action,
            DailyNextAction.MONITOR_NEXT_EARNINGS_AND_BACKLOG.value,
        )
        self.assertTrue(full.claim_ids)

    def test_independent_audit_catches_named_known_bad_mutations(self) -> None:
        payload = self.result.to_dict()

        missing_status = deepcopy(payload)
        missing_status["stage_statuses"].pop()
        audit = audit_current_daily_census(missing_status)
        self.assertEqual(
            audit["critical_counts"]["eligible_symbol_without_status"],
            1,
        )

        trigger_score = deepcopy(payload)
        market_timeline = next(
            item
            for item in trigger_score["source_timelines"]
            if item["target_id"] == "T-MARKET"
        )
        market_event = next(
            item for item in market_timeline["events"] if item["role"] == "TRIGGER"
        )
        market_event["score_evidence_eligible"] = True
        audit = audit_current_daily_census(trigger_score)
        self.assertEqual(
            audit["critical_counts"]["market_news_used_as_score_evidence"],
            1,
        )

        cutoff = deepcopy(payload)
        cutoff["thesis_states"][0]["recent_cutoff_applied"] = True
        audit = audit_current_daily_census(cutoff)
        self.assertEqual(
            audit["critical_counts"]["recent_lookback_stage_cutoff"],
            1,
        )

        dropped_open_claim = deepcopy(payload)
        ledger_thesis = next(
            item
            for item in dropped_open_claim["thesis_states"]
            if item["target_id"] == "T-LEDGER"
        )
        ledger_thesis["current_open_claim_ids"] = []
        audit = audit_current_daily_census(dropped_open_claim)
        self.assertEqual(
            audit["critical_counts"][
                "current_open_claim_dropped_by_lookback"
            ],
            1,
        )

        pending_score = deepcopy(payload)
        provider_status = next(
            item
            for item in pending_score["stage_statuses"]
            if item["target_id"] == "T-IR"
        )
        provider_status["score_type"] = AtomicScoreType.FULL_E2R_100.value
        provider_status["score_value"] = 10.0
        provider_status["score_finalization_allowed"] = True
        audit = audit_current_daily_census(pending_score)
        self.assertEqual(audit["critical_counts"]["pending_final_score"], 1)

        unsafe = deepcopy(payload)
        unsafe["watchlist"][0]["monitoring_label"] = "즉시 매수"
        audit = audit_current_daily_census(unsafe)
        self.assertEqual(
            audit["critical_counts"]["watchlist_recommendation_language"],
            1,
        )

        missing_watchlist = deepcopy(payload)
        missing_watchlist["watchlist"].pop()
        audit = audit_current_daily_census(missing_watchlist)
        self.assertEqual(audit["critical_counts"]["watchlist_coverage_gap"], 1)

        unbounded = deepcopy(payload)
        unbounded["config"]["max_deep_candidates"] = None
        audit = audit_current_daily_census(unbounded)
        self.assertEqual(
            audit["critical_counts"]["unbounded_production_config"],
            1,
        )

        unbounded_task = deepcopy(payload)
        unbounded_task["source_tasks"][0]["max_fetches"] = None
        audit = audit_current_daily_census(unbounded_task)
        self.assertEqual(
            audit["critical_counts"]["source_task_unbounded_or_no_stop"],
            1,
        )

        no_stop = deepcopy(payload)
        no_stop["source_tasks"][0]["stop_condition"] = "exhaust_all_results"
        audit = audit_current_daily_census(no_stop)
        self.assertEqual(
            audit["critical_counts"]["source_task_unbounded_or_no_stop"],
            1,
        )

        unreferenced_task = deepcopy(payload)
        risk_execution = next(
            item
            for item in unreferenced_task["deep_executions"]
            if item["target_id"] == "T-RISK"
        )
        risk_execution["source_task_ids"] = []
        audit = audit_current_daily_census(unreferenced_task)
        self.assertEqual(
            audit["critical_counts"]["source_task_unreferenced_or_duplicate"],
            1,
        )
        self.assertEqual(
            audit["critical_counts"][
                "execution_source_task_reference_mismatch"
            ],
            1,
        )

        unauthorized_web = deepcopy(payload)
        for task in unauthorized_web["source_tasks"]:
            if task["target_id"] == "T-EARN":
                task["allows_general_web"] = False
                task["official_gap_reasons"] = []
        audit = audit_current_daily_census(unauthorized_web)
        self.assertEqual(
            audit["critical_counts"]["general_web_without_official_gap"],
            1,
        )

        forbidden_quota = deepcopy(payload)
        forbidden_quota["config"]["sector_sample_quota"] = 1
        audit = audit_current_daily_census(forbidden_quota)
        self.assertEqual(
            audit["critical_counts"][
                "forbidden_quota_or_recent_cutoff_config"
            ],
            1,
        )

        all_symbol_llm = deepcopy(payload)
        for execution in all_symbol_llm["deep_executions"]:
            execution["llm_calls"] = 1
        for target_id in ("T-REPORT", "T-NEWS", "T-MARKET"):
            all_symbol_llm["deep_executions"].append(
                {
                    "execution_id": f"FORGED-{target_id}",
                    "target_id": target_id,
                    "outcome": CurrentDeepOutcome.BUDGET_PENDING.value,
                    "trigger_signal_ids": [f"TRIGGER-{target_id}"],
                    "terminal_reason": "forged_all_symbol_llm",
                    "atomic_decision_id": None,
                    "source_task_ids": [],
                    "provider_kind": DailyProviderKind.FIXTURE.value,
                    "provider_trace_id": f"FORGED-TRACE-{target_id}",
                    "llm_calls": 1,
                    "source_tasks": 0,
                    "fetches": 0,
                    "retries": 0,
                    "general_web_fetches": 0,
                    "official_first_attempted": True,
                    "official_gap_reasons": [],
                    "runtime_seconds": 1.0,
                }
            )
        audit = audit_current_daily_census(all_symbol_llm)
        self.assertEqual(
            audit["critical_counts"]["all_symbol_llm_execution"],
            1,
        )

    def test_production_bounded_contract_rejects_fixture_provider_but_accepts_codex(self) -> None:
        production_config = replace(self.config, test_mode=False)
        with self.assertRaisesRegex(ValueError, "test-only SourceTask"):
            run_current_daily_census(replace(self.inputs, config=production_config))
        production_source_tasks = tuple(
            replace(item, test_only=False) for item in self.source_tasks
        )
        with self.assertRaisesRegex(ValueError, "fixture provider"):
            run_current_daily_census(
                replace(
                    self.inputs,
                    config=production_config,
                    source_tasks=production_source_tasks,
                )
            )
        production_executions = tuple(
            replace(
                item,
                provider_kind=(
                    DailyProviderKind.CODEX.value
                    if item.llm_calls
                    else DailyProviderKind.NONE.value
                ),
            )
            for item in self.executions
        )
        result = run_current_daily_census(
            replace(
                self.inputs,
                config=production_config,
                source_tasks=production_source_tasks,
                deep_executions=production_executions,
            )
        )
        self.assertTrue(result.manifest["production_bounded_contract_ready"])
        self.assertFalse(result.manifest["live_execution_observed"])
        self.assertFalse(result.production_runtime_ready)

    def test_manifest_loader_writer_and_cli_round_trip(self) -> None:
        decoded = current_operation_runner_input_from_mapping(self.inputs.to_dict())
        rerun = run_current_daily_census(decoded)
        self.assertEqual(rerun.run_id, self.result.run_id)
        self.assertEqual(
            rerun.audit["result_hash"],
            self.result.audit["result_hash"],
        )
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            direct_paths = write_current_daily_census(
                self.result,
                output_root=root / "direct",
            )
            self.assertTrue(all(path.exists() for path in direct_paths.values()))
            input_path = root / "input.json"
            input_path.write_text(
                json.dumps(self.inputs.to_dict(), ensure_ascii=False),
                encoding="utf-8",
            )
            stream = io.StringIO()
            with redirect_stdout(stream):
                exit_code = current_cli_main(
                    [
                        "--as-of-date",
                        self.as_of_date,
                        "--mode",
                        "test",
                        "--output-root",
                        str(root / "cli"),
                        "--input-manifest",
                        str(input_path),
                    ]
                )
            self.assertEqual(exit_code, 0)
            cli_payload = json.loads(stream.getvalue())
            self.assertEqual(cli_payload["status"], "BOUNDED_DAILY_CENSUS_PASS")
            self.assertFalse(cli_payload["production_runtime_ready"])

        wrong_schema = self.inputs.to_dict()
        wrong_schema["schema_version"] = "legacy_or_unknown"
        with self.assertRaisesRegex(ValueError, "schema version mismatch"):
            current_operation_runner_input_from_mapping(wrong_schema)

    def test_legacy_census_adapter_preserves_leaves_but_not_stage_hint(self) -> None:
        instrument = UniverseInstrument(
            symbol="005930",
            company_name="어댑터기업",
            market="KOSPI",
        )
        scan = BaselineScanResult(
            symbol=instrument.symbol,
            as_of_date=self.as_of_date,
            price_anomaly_count=1,
            trigger_priority_score=5.0,
        )
        event = SourceTimelineEvent(
            event_id="LEGACY-MARKET-EVENT",
            symbol=instrument.symbol,
            event_type="MarketAnomaly",
            source_family="KRXPrice",
            event_date=self.as_of_date,
            candidate_event_eligible=True,
            score_evidence_eligible=False,
            reason="market trigger only",
        )
        timeline = SourceTimeline(
            symbol=instrument.symbol,
            company_name=instrument.company_name,
            as_of_date=self.as_of_date,
            events=(event,),
        )
        legacy_thesis = LastEffectiveThesisState(
            symbol=instrument.symbol,
            company_name=instrument.company_name,
            as_of_date=self.as_of_date,
            thesis_status="NEEDS_REFRESH",
            base_stage_hint="Stage3-Green",
            last_effective_event_id=event.event_id,
            followup_required=True,
            reason_codes=("legacy_stage_hint_must_not_copy",),
        )
        config = replace(
            self.config,
            max_official_light_targets=1,
            max_deep_candidates=1,
            max_brain_candidates=1,
            max_acquisition_candidates=1,
        )
        adapted = adapt_census_snapshot_to_current_input(
            as_of_date=self.as_of_date,
            instruments=(instrument,),
            scans=(scan,),
            source_timelines=(timeline,),
            thesis_states=(legacy_thesis,),
            config=config,
        )
        execution = DailyDeepExecution(
            execution_id="ADAPTER-BUDGET-PENDING",
            target_id=instrument.symbol,
            outcome=CurrentDeepOutcome.BUDGET_PENDING.value,
            trigger_signal_ids=tuple(item.signal_id for item in adapted.triggers),
            terminal_reason="adapter_budget_boundary",
            provider_kind=DailyProviderKind.NONE.value,
            official_first_attempted=True,
        )
        result = run_current_daily_census(
            replace(adapted, deep_executions=(execution,))
        )
        self.assertEqual(len(result.baseline_lanes), 4)
        self.assertEqual(
            {item.trigger_type for item in result.triggers},
            {
                CurrentTriggerType.MARKET.value,
                CurrentTriggerType.EXISTING_LEDGER.value,
            },
        )
        self.assertEqual(
            result.stage_statuses[0].canonical_stage,
            CanonicalStage.STAGE_0.value,
        )
        self.assertEqual(
            result.stage_statuses[0].score_type,
            AtomicScoreType.NO_SCORE.value,
        )
        self.assertNotEqual(
            result.stage_statuses[0].canonical_stage,
            legacy_thesis.base_stage_hint,
        )


if __name__ == "__main__":
    unittest.main()
