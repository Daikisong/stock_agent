from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.research_brain.replay import (
    FrozenReplaySourceStatus,
    HistoricalAttemptStatus,
    HistoricalGuardDecision,
    HistoricalGuardKind,
    HistoricalGuardProbe,
    HistoricalSourceResolution,
    compile_historical_replay_parity,
    write_historical_replay_parity,
)
from e2r.research_brain.runtime import (
    CanonicalRunMode,
    CurrentClaimReference,
    CurrentDeepCandidate,
    CurrentDeepDisposition,
    CurrentDeepOutcome,
    CurrentOperationInput,
    CurrentTriggerSignal,
    CurrentUniverseBaseline,
    audit_historical_current_separation,
    claim_mode_output_root,
    compile_current_operation,
    forbidden_planner_context_paths,
    write_current_operation,
)
from tests import test_semantic_memory_retrieval as phase5_tests


class HistoricalCurrentModeSeparationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        phase5_tests.SemanticMemoryRetrievalTest.setUpClass()
        cls.phase5 = phase5_tests.SemanticMemoryRetrievalTest
        ready = next(
            item
            for item in cls.phase5.source_result.verifications
            if item.historical_replay_ready
        )
        wrong_subject = next(
            item
            for item in cls.phase5.source_result.verifications
            if item.source_state == "URL_FETCHED_WRONG_SUBJECT"
        )
        cls.guard_probes = (
            HistoricalGuardProbe(
                probe_id="HGUARD-POSITIVE",
                guard_kind=HistoricalGuardKind.POSITIVE.value,
                frozen_as_of_date="2026-06-30",
                evidence_reference_id="BR-C06-01",
                observed_decision=HistoricalGuardDecision.ACCEPT_EVALUATOR_HIT.value,
            ),
            HistoricalGuardProbe(
                probe_id="HGUARD-COUNTER",
                guard_kind=HistoricalGuardKind.COUNTER_GUARD.value,
                frozen_as_of_date="2026-06-30",
                evidence_reference_id="BALANCED-MEMORY-COUNTER-GUARD",
                observed_decision=HistoricalGuardDecision.REJECT_SCORE.value,
            ),
            HistoricalGuardProbe(
                probe_id="HGUARD-WRONG-SUBJECT",
                guard_kind=HistoricalGuardKind.WRONG_SUBJECT.value,
                frozen_as_of_date="2026-06-30",
                evidence_reference_id=wrong_subject.verification_id,
                observed_decision=HistoricalGuardDecision.REJECT_SCORE.value,
            ),
            HistoricalGuardProbe(
                probe_id="HGUARD-OLD-RISK",
                guard_kind=HistoricalGuardKind.OLD_RISK.value,
                frozen_as_of_date="2026-06-30",
                evidence_reference_id="PHASE9-STALE-LIFECYCLE-FIXTURE",
                observed_decision=HistoricalGuardDecision.NO_CURRENT_PENALTY.value,
            ),
            HistoricalGuardProbe(
                probe_id="HGUARD-SOURCE-MISSING",
                guard_kind=HistoricalGuardKind.SOURCE_MISSING.value,
                frozen_as_of_date="2026-06-30",
                evidence_reference_id="NO-URL-BACKED-FROZEN-SOURCE",
                observed_decision=HistoricalGuardDecision.SOURCE_PENDING.value,
            ),
        )
        cls.historical = compile_historical_replay_parity(
            retrieval_audit=cls.phase5.retrieval_audit,
            benchmark_cases=cls.phase5.benchmark,
            frozen_as_of_date="2026-06-30",
            guard_probes=cls.guard_probes,
            source_statuses=(
                FrozenReplaySourceStatus(
                    archetype_id="C15_MATERIAL_SPREAD_SUPERCYCLE",
                    resolution=HistoricalSourceResolution.URL_BACKED_REPLAY.value,
                    replay_source_reference_ids=(ready.verification_id,),
                ),
                FrozenReplaySourceStatus(
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    resolution=HistoricalSourceResolution.EXACT_BLOCKER.value,
                    blocker_reason="SOURCE_PROXY_ONLY_REQUIRES_CASE_LEVEL_URL",
                    source_proxy_reference_ids=("SOURCE-PROXY-C06",),
                ),
            ),
        )
        cls.current_input = cls._build_current_input()
        cls.current = compile_current_operation(cls.current_input)

    @staticmethod
    def _build_current_input() -> CurrentOperationInput:
        as_of_date = "2026-06-30"
        universe = tuple(
            CurrentUniverseBaseline(
                target_id=f"TARGET-{index}",
                target_name=f"테스트기업{index}",
                as_of_date=as_of_date,
                baseline_source_ids=(f"BASELINE-{index}",),
            )
            for index in range(1, 7)
        )
        trigger_types = (
            "OFFICIAL",
            "MARKET",
            "NEWS",
            "RISK",
            "EXISTING_LEDGER",
        )
        signals = tuple(
            CurrentTriggerSignal(
                signal_id=f"SIGNAL-{index}",
                target_id=f"TARGET-{index}",
                observed_date=as_of_date,
                trigger_type=trigger_type,
                source_id=f"TRIGGER-SOURCE-{index}",
            )
            for index, trigger_type in enumerate(trigger_types, start=1)
        )
        claims = (
            CurrentClaimReference(
                claim_id="CURRENT-CLAIM-POSITIVE",
                target_id="TARGET-1",
                observed_date=as_of_date,
                source_id="DIRECT-OFFICIAL-DOC",
                source_backed=True,
                current_open=True,
                historical_replay=False,
                score_eligible=True,
            ),
            CurrentClaimReference(
                claim_id="CURRENT-CLAIM-COUNTER",
                target_id="TARGET-2",
                observed_date=as_of_date,
                source_id="DIRECT-COUNTER-DOC",
                source_backed=True,
                current_open=True,
                historical_replay=False,
                score_eligible=False,
            ),
        )
        candidates = tuple(
            CurrentDeepCandidate(
                candidate_id=f"CANDIDATE-{index}",
                target_id=f"TARGET-{index}",
                trigger_signal_ids=(f"SIGNAL-{index}",),
                current_claim_ids=(
                    ("CURRENT-CLAIM-POSITIVE",)
                    if index == 1
                    else ("CURRENT-CLAIM-COUNTER",)
                    if index == 2
                    else ()
                ),
                inferred_archetype_ids=(
                    ("C06_HBM_MEMORY_CUSTOMER_CAPACITY",)
                    if index == 1
                    else ("C15_MATERIAL_SPREAD_SUPERCYCLE",)
                    if index == 2
                    else ()
                ),
                selected_for_deep=True,
                selection_reason="current dated trigger selected within deep budget",
            )
            for index in range(1, 6)
        )
        dispositions = (
            CurrentDeepDisposition(
                candidate_id="CANDIDATE-1",
                target_id="TARGET-1",
                outcome=CurrentDeepOutcome.FULL_THESIS.value,
                supporting_claim_ids=("CURRENT-CLAIM-POSITIVE",),
                score_claim_ids=("CURRENT-CLAIM-POSITIVE",),
                missing_conditions=(),
            ),
            CurrentDeepDisposition(
                candidate_id="CANDIDATE-2",
                target_id="TARGET-2",
                outcome=CurrentDeepOutcome.DISPROVED.value,
                supporting_claim_ids=("CURRENT-CLAIM-COUNTER",),
                score_claim_ids=(),
                missing_conditions=(),
            ),
            CurrentDeepDisposition(
                candidate_id="CANDIDATE-3",
                target_id="TARGET-3",
                outcome=CurrentDeepOutcome.SOURCE_PENDING.value,
                supporting_claim_ids=(),
                score_claim_ids=(),
                missing_conditions=("target-direct official source",),
                pending_reason="official source gap remains open",
            ),
            CurrentDeepDisposition(
                candidate_id="CANDIDATE-4",
                target_id="TARGET-4",
                outcome=CurrentDeepOutcome.PROVIDER_PENDING.value,
                supporting_claim_ids=(),
                score_claim_ids=(),
                missing_conditions=("provider completion",),
                pending_reason="bounded provider failed",
            ),
            CurrentDeepDisposition(
                candidate_id="CANDIDATE-5",
                target_id="TARGET-5",
                outcome=CurrentDeepOutcome.BUDGET_PENDING.value,
                supporting_claim_ids=(),
                score_claim_ids=(),
                missing_conditions=("next bounded investigation round",),
                pending_reason="selective deep budget exhausted",
            ),
        )
        return CurrentOperationInput(
            as_of_date=as_of_date,
            universe=universe,
            signals=signals,
            claims=claims,
            candidates=candidates,
            deep_dispositions=dispositions,
            max_deep_candidates=5,
            test_only=True,
        )

    def test_historical_replay_covers_registry_and_thresholds(self) -> None:
        manifest = self.historical.manifest
        self.assertEqual(manifest["status"], "HISTORICAL_REPLAY_PARITY_PASS")
        self.assertEqual(manifest["registry_archetype_count"], 36)
        self.assertEqual(manifest["registry_covered_archetype_count"], 36)
        self.assertEqual(manifest["archetype_parity_row_count"], 36)
        self.assertEqual(
            {item.archetype_id for item in self.historical.archetype_rows},
            set(CANONICAL_ARCHETYPE_IDS),
        )
        self.assertGreaterEqual(manifest["top3_accuracy"], 0.95)
        self.assertGreaterEqual(manifest["top1_accuracy"], 0.85)
        self.assertGreaterEqual(manifest["mapping_precision"], 0.95)
        self.assertGreaterEqual(manifest["positive_recall"], 0.90)
        self.assertGreaterEqual(manifest["guard_accuracy"], 0.95)
        self.assertEqual(manifest["critical_count_sum"], 0)
        self.assertEqual(manifest["guard_probe_count"], 5)
        self.assertEqual(manifest["guard_probe_kind_count"], 5)
        self.assertEqual(manifest["guard_probe_pass_rate"], 1.0)
        self.assertEqual(
            set(manifest["guard_probe_counts"]),
            {item.value for item in HistoricalGuardKind},
        )
        self.assertEqual(
            manifest["leaf_hash"],
            "236ae82327e773a2062a18ab0a409a0dc2688a476818f60154d404ddc08b899d",
        )

    def test_historical_prompt_is_blind_and_source_proxy_never_scores(self) -> None:
        self.assertTrue(
            all(not item.planner_forbidden_context_paths for item in self.historical.benchmark_leaves)
        )
        self.assertEqual(self.historical.manifest["future_leakage_count"], 0)
        self.assertEqual(self.historical.manifest["source_proxy_score_credit_count"], 0)
        self.assertEqual(self.historical.manifest["url_backed_archetype_count"], 1)
        self.assertEqual(self.historical.manifest["exact_source_blocker_archetype_count"], 35)
        self.assertTrue(
            all(
                item.source_resolution == HistoricalSourceResolution.URL_BACKED_REPLAY.value
                or item.source_blocker_reason
                for item in self.historical.archetype_rows
            )
        )
        self.assertTrue(
            all(
                item.attempt_status != HistoricalAttemptStatus.NOT_ATTEMPTED.value
                or item.attempt_reason
                for item in self.historical.archetype_rows
            )
        )
        self.assertEqual(self.historical.manifest["current_watchlist_eligible_count"], 0)
        self.assertTrue(
            forbidden_planner_context_paths(
                {"current_evidence": "expected_stage=3-Green"}
            )
        )

    def test_historical_replay_rejects_unfrozen_or_fake_source_credit(self) -> None:
        with self.assertRaisesRegex(ValueError, "not frozen"):
            compile_historical_replay_parity(
                retrieval_audit=self.phase5.retrieval_audit,
                benchmark_cases=self.phase5.benchmark,
                frozen_as_of_date="2026-06-29",
                guard_probes=self.guard_probes,
            )
        with self.assertRaisesRegex(ValueError, "source proxy"):
            FrozenReplaySourceStatus(
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                resolution=HistoricalSourceResolution.EXACT_BLOCKER.value,
                blocker_reason="SOURCE_PROXY_ONLY",
                source_proxy_score_credit=1,
            )

    def test_current_operation_is_full_baseline_and_bounded_selective_deep(self) -> None:
        manifest = self.current.manifest
        self.assertEqual(
            manifest["status"],
            "CURRENT_OPERATION_MODE_SEPARATION_PASS",
        )
        self.assertEqual(manifest["full_universe_baseline_count"], 6)
        self.assertEqual(manifest["real_trigger_candidate_count"], 5)
        self.assertEqual(manifest["selected_deep_candidate_count"], 5)
        self.assertEqual(manifest["deep_terminal_outcome_count"], 5)
        self.assertEqual(
            set(manifest["deep_outcome_counts"]),
            {item.value for item in CurrentDeepOutcome},
        )
        self.assertTrue(all(manifest["deep_outcome_counts"].values()))
        self.assertEqual(manifest["materialized_current_archetype_count"], 2)
        self.assertEqual(manifest["missing_current_archetype_row_critical_count"], 0)
        self.assertEqual(manifest["archetype_quota_count"], 0)
        self.assertEqual(manifest["trigger_score_evidence_count"], 0)
        self.assertEqual(manifest["critical_count_sum"], 0)
        self.assertEqual(
            manifest["leaf_hash"],
            "e6142d30f5360fb61b3fa519123e64539cd0cb4b0051ceac8c7ac4f80ed72fd1",
        )

    def test_current_operation_rejects_future_history_quota_and_missing_outcome(self) -> None:
        with self.assertRaisesRegex(ValueError, "future signal"):
            compile_current_operation(
                replace(
                    self.current_input,
                    signals=(
                        replace(self.current_input.signals[0], observed_date="2026-07-01"),
                        *self.current_input.signals[1:],
                    ),
                )
            )
        with self.assertRaisesRegex(ValueError, "historical replay claim"):
            compile_current_operation(
                replace(
                    self.current_input,
                    claims=(
                        replace(
                            self.current_input.claims[0],
                            historical_replay=True,
                            score_eligible=False,
                        ),
                        self.current_input.claims[1],
                    ),
                )
            )
        with self.assertRaisesRegex(ValueError, "forbids archetype quotas"):
            replace(
                self.current_input,
                archetype_quota={"C06_HBM_MEMORY_CUSTOMER_CAPACITY": 1},
            )
        with self.assertRaisesRegex(ValueError, "terminal outcome"):
            compile_current_operation(
                replace(
                    self.current_input,
                    deep_dispositions=self.current_input.deep_dispositions[:-1],
                )
            )
        with self.assertRaisesRegex(ValueError, "not direct score evidence"):
            replace(self.current_input.signals[0], counts_as_score_evidence=True)

    def test_mode_output_roots_are_physically_separate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            historical_paths = write_historical_replay_parity(
                self.historical,
                output_root=root / "historical",
            )
            current_paths = write_current_operation(
                self.current,
                output_root=root / "current",
            )
            historical_marker = json.loads(
                historical_paths["mode_marker"].read_text(encoding="utf-8")
            )
            current_marker = json.loads(
                current_paths["mode_marker"].read_text(encoding="utf-8")
            )
            self.assertEqual(
                historical_marker["mode"],
                CanonicalRunMode.HISTORICAL_REPLAY.value,
            )
            self.assertEqual(
                current_marker["mode"],
                CanonicalRunMode.CURRENT_OPERATION.value,
            )
            self.assertTrue(historical_paths["planner_inputs"].is_file())
            self.assertTrue(historical_paths["evaluator_leaves"].is_file())
            self.assertTrue(historical_paths["guard_probes"].is_file())
            planner_row = json.loads(
                historical_paths["planner_inputs"]
                .read_text(encoding="utf-8")
                .splitlines()[0]
            )
            evaluator_row = json.loads(
                historical_paths["evaluator_leaves"]
                .read_text(encoding="utf-8")
                .splitlines()[0]
            )
            self.assertNotIn("archetype_id", planner_row)
            self.assertNotIn("expected_primitive_id", planner_row)
            self.assertTrue(planner_row["planner_input"]["request_id"].startswith("BLIND-"))
            self.assertNotIn("C06", planner_row["planner_input"]["request_id"])
            self.assertNotIn("planner_input", evaluator_row)
            self.assertIn("archetype_id", evaluator_row)
            self.assertTrue(current_paths["dispositions"].is_file())
            with self.assertRaisesRegex(ValueError, "cannot share output root"):
                claim_mode_output_root(
                    root / "historical",
                    mode=CanonicalRunMode.CURRENT_OPERATION,
                    run_id=self.current.run_id,
                )

    def test_independent_mode_separation_audit_has_zero_critical_count(self) -> None:
        audit = audit_historical_current_separation(
            historical_manifest=self.historical.manifest,
            current_manifest=self.current.manifest,
        )
        self.assertEqual(
            audit["status"],
            "HISTORICAL_CURRENT_MODE_SEPARATION_PASS",
        )
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(
            audit["result_hash"],
            "702400d8e940a96ba194bb930fbb5409b11ad273693d1f584288c4d97cbc4836",
        )
        self.assertFalse(audit["production_runtime_ready"])
        tampered_current = dict(self.current.manifest)
        tampered_current.pop("leaf_hash")
        tampered = audit_historical_current_separation(
            historical_manifest=self.historical.manifest,
            current_manifest=tampered_current,
        )
        self.assertEqual(
            tampered["status"],
            "HISTORICAL_CURRENT_MODE_SEPARATION_FAIL",
        )
        self.assertEqual(tampered["critical_counts"]["current_manifest_field_missing"], 1)


if __name__ == "__main__":
    unittest.main()
