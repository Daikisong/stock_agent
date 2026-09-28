from __future__ import annotations

import unittest
from dataclasses import replace

from e2r.production.metadata import stable_hash
from e2r.research_brain.runtime import (
    AtomicClaimPolarity,
    AtomicDecisionStatus,
    AtomicHardBreakSignal,
    AtomicPrimitiveAssessment,
    AtomicPrimitiveStatus,
    AtomicScoreClaim,
    AtomicScoreRule,
    AtomicScoreType,
    AtomicScoringInput,
    AtomicScoringScope,
    AtomicStageConfig,
    CanonicalStage,
    adapt_claim_ledger_event_to_atomic_claim,
    audit_atomic_score_delta,
    audit_atomic_stage_decisions,
    decide_atomic_score_stage,
)
from tests import test_contract_blind_claim_compiler as phase9_tests


class AtomicScoreStageIntegrityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.as_of_date = "2026-06-30"
        cls.target_id = "ATOMIC-TARGET"
        cls.primitive_ids = (
            "revision_direction",
            "fcf_quality",
            "contract_quality",
            "capacity_lock",
        )
        cls.rules = tuple(
            AtomicScoreRule(
                primitive_id=primitive_id,
                component_key=f"component:{primitive_id}",
                max_points=25.0,
                material=primitive_id != "capacity_lock",
                green_required=primitive_id in {"contract_quality", "capacity_lock"},
            )
            for primitive_id in cls.primitive_ids
        )
        cls.claims = tuple(
            AtomicScoreClaim(
                claim_id=f"CLAIM-{primitive_id}",
                target_id=cls.target_id,
                primitive_id=primitive_id,
                observed_date=cls.as_of_date,
                content_hash=stable_hash({"primitive": primitive_id, "version": 1}),
                source_ids=(f"SOURCE-{primitive_id}",),
                anchor_ids=(f"ANCHOR-{primitive_id}",),
                mapping_ids=(f"MAPPING-{primitive_id}",),
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
            for primitive_id in cls.primitive_ids
        )
        cls.assessments = tuple(
            AtomicPrimitiveAssessment(
                primitive_id=primitive_id,
                status=AtomicPrimitiveStatus.SATISFIED.value,
                evidence_strength=1.0,
                support_claim_ids=(f"CLAIM-{primitive_id}",),
            )
            for primitive_id in cls.primitive_ids
        )
        cls.full = decide_atomic_score_stage(cls._input())

    @classmethod
    def _input(cls, **overrides) -> AtomicScoringInput:
        payload = {
            "target_id": cls.target_id,
            "as_of_date": cls.as_of_date,
            "scope": AtomicScoringScope.FULL_THESIS.value,
            "claims": cls.claims,
            "primitive_assessments": cls.assessments,
            "rules": cls.rules,
        }
        payload.update(overrides)
        return AtomicScoringInput(**payload)

    def test_full_score_is_one_atomic_claim_contribution_stage_trace(self) -> None:
        decision = self.full
        self.assertEqual(decision.score_type, AtomicScoreType.FULL_E2R_100.value)
        self.assertEqual(decision.score_value, 100.0)
        self.assertTrue(decision.score_valid)
        self.assertTrue(decision.score_finalization_allowed)
        self.assertEqual(decision.canonical_stage, CanonicalStage.STAGE_3_GREEN.value)
        self.assertEqual(decision.decision_status, AtomicDecisionStatus.FINAL.value)
        self.assertEqual(len(decision.accepted_claim_ids), 4)
        self.assertEqual(len(decision.contributions), 4)
        self.assertFalse(decision.material_gap_ids)
        self.assertEqual(
            decision.stage_court_trace.contribution_ids,
            tuple(item.contribution_id for item in decision.contributions),
        )
        self.assertEqual(
            {item.value for item in CanonicalStage},
            {
                "0",
                "1",
                "2",
                "3-Green",
                "3-Yellow",
                "3-Red",
                "4A",
                "4B",
                "4C",
                "5",
            },
        )

    def test_phase9_acquired_document_claim_leaf_reaches_atomic_score(self) -> None:
        phase9_tests.ContractBlindClaimCompilerTest.setUpClass()
        phase9 = phase9_tests.ContractBlindClaimCompilerTest(
            "test_contract_blind_input_and_direct_task_satisfaction"
        )
        acquisition = phase9._acquisition(candidate_id="PHASE12-RAW-TO-SCORE")
        compilation = phase9._compile(acquisition=acquisition)
        event = next(item for item in compilation.ledger_events if item.score_eligible)
        document = acquisition.documents[0]
        claim = adapt_claim_ledger_event_to_atomic_claim(
            event,
            source_content_hash=document.content_hash,
            material=True,
            test_mode=True,
        )
        rule = AtomicScoreRule(
            primitive_id=claim.primitive_id,
            component_key="customer_contract_visibility",
            max_points=100.0,
            material=True,
            green_required=True,
        )
        assessment = AtomicPrimitiveAssessment(
            primitive_id=claim.primitive_id,
            status=AtomicPrimitiveStatus.SATISFIED.value,
            evidence_strength=1.0,
            support_claim_ids=(claim.claim_id,),
        )
        decision = decide_atomic_score_stage(
            AtomicScoringInput(
                target_id=claim.target_id,
                as_of_date=self.as_of_date,
                scope=AtomicScoringScope.FULL_THESIS.value,
                claims=(claim,),
                primitive_assessments=(assessment,),
                rules=(rule,),
            )
        )
        self.assertEqual(decision.score_type, AtomicScoreType.FULL_E2R_100.value)
        self.assertEqual(decision.score_value, 100.0)
        self.assertEqual(decision.accepted_claim_ids, (event.claim_id,))
        self.assertEqual(decision.contributions[0].mapping_ids, (event.mapping_id,))
        self.assertEqual(decision.claims[0].content_hash, document.content_hash)

        production_boundary = adapt_claim_ledger_event_to_atomic_claim(
            event,
            source_content_hash=document.content_hash,
            material=True,
            test_mode=False,
        )
        self.assertFalse(production_boundary.score_eligible)
        historical_boundary = adapt_claim_ledger_event_to_atomic_claim(
            event,
            source_content_hash=document.content_hash,
            material=True,
            test_mode=True,
            historical_replay=True,
        )
        self.assertTrue(historical_boundary.historical_replay)
        self.assertFalse(historical_boundary.score_eligible)

    def test_superseded_risk_removed_from_current_penalty(self) -> None:
        phase9_tests.ContractBlindClaimCompilerTest.setUpClass()
        phase9 = phase9_tests.ContractBlindClaimCompilerTest(
            "test_contract_blind_input_and_direct_task_satisfaction"
        )
        acquisition = phase9._acquisition(candidate_id="SUPERSEDED-RISK")
        compilation = phase9._compile(acquisition=acquisition)
        event = next(item for item in compilation.ledger_events if item.score_eligible)
        superseded_event = replace(
            event,
            claim_id="CLAIM-SUPERSEDED-RISK",
            raw_assertion_id="RAW-SUPERSEDED-RISK",
            subject_entity_id=self.target_id,
            target_entity_id=self.target_id,
            original_primitive_id="contract_cancelled",
            mapped_primitive_id="contract_cancelled",
            polarity="NEGATIVE",
            support_direction="COUNTER",
            score_eligible=False,
            production_score_eligible=False,
            superseded_by_claim_ids=("CLAIM-RESOLUTION",),
            contradiction_resolved=False,
            closes_original_gap=False,
        )
        risk_claim = adapt_claim_ledger_event_to_atomic_claim(
            superseded_event,
            source_content_hash=acquisition.documents[0].content_hash,
            material=True,
            test_mode=True,
        )
        self.assertFalse(risk_claim.current_open)
        self.assertFalse(risk_claim.score_eligible)
        signal = AtomicHardBreakSignal(
            signal_id="HARD-BREAK-SUPERSEDED",
            claim_id=risk_claim.claim_id,
            condition_id="contract_cancelled",
            unresolved=True,
        )

        decision = decide_atomic_score_stage(
            self._input(
                claims=(*self.claims, risk_claim),
                hard_break_signals=(signal,),
                has_prior_live_thesis=True,
            )
        )

        self.assertFalse(decision.hard_break_claim_ids)
        self.assertEqual(
            decision.rejected_hard_break_signal_ids,
            (signal.signal_id,),
        )
        self.assertEqual(decision.canonical_stage, CanonicalStage.STAGE_3_GREEN.value)

    def test_claimless_full_request_becomes_no_score(self) -> None:
        decision = decide_atomic_score_stage(self._input(claims=()))
        self.assertEqual(decision.score_type, AtomicScoreType.NO_SCORE.value)
        self.assertIsNone(decision.score_value)
        self.assertFalse(decision.score_valid)
        self.assertFalse(decision.score_finalization_allowed)
        self.assertEqual(decision.canonical_stage, CanonicalStage.STAGE_0.value)
        self.assertEqual(decision.decision_status, AtomicDecisionStatus.PENDING.value)
        self.assertIn("claimless_score", decision.missing_conditions)
        with self.assertRaisesRegex(ValueError, "requires contributions"):
            replace(decision, raw_reference_score=0.0)

    def test_material_gap_blocks_full_but_event_partial_stays_explicit(self) -> None:
        assessments = tuple(
            replace(
                item,
                status=AtomicPrimitiveStatus.MISSING.value,
                evidence_strength=0.0,
                support_claim_ids=(),
            )
            if item.primitive_id == "contract_quality"
            else item
            for item in self.assessments
        )
        blocked = decide_atomic_score_stage(
            self._input(primitive_assessments=assessments)
        )
        self.assertEqual(blocked.score_type, AtomicScoreType.NO_SCORE.value)
        self.assertIsNone(blocked.score_value)
        self.assertEqual(blocked.raw_reference_score, 75.0)
        self.assertIn("contract_quality", blocked.material_gap_ids)
        self.assertFalse(blocked.score_valid)

        event = decide_atomic_score_stage(
            self._input(
                scope=AtomicScoringScope.EVENT_EVIDENCE.value,
                primitive_assessments=assessments,
            )
        )
        self.assertEqual(
            event.score_type,
            AtomicScoreType.EVENT_EVIDENCE_PARTIAL.value,
        )
        self.assertEqual(event.score_value, 75.0)
        self.assertTrue(event.score_valid)
        self.assertFalse(event.score_finalization_allowed)
        self.assertEqual(event.canonical_stage, CanonicalStage.STAGE_2.value)
        self.assertEqual(event.decision_status, AtomicDecisionStatus.EVENT_PARTIAL.value)

        unmapped_claims = tuple(
            replace(
                item,
                mapping_ids=(),
                mapping_accepted=False,
                score_eligible=False,
            )
            if item.primitive_id == "contract_quality"
            else item
            for item in self.claims
        )
        unmapped = decide_atomic_score_stage(self._input(claims=unmapped_claims))
        self.assertEqual(unmapped.score_type, AtomicScoreType.NO_SCORE.value)
        self.assertIn(
            "ineligible_support_claim:CLAIM-contract_quality",
            unmapped.missing_conditions,
        )

    def test_provider_or_source_pending_never_becomes_final_low_score(self) -> None:
        for field in ("provider_pending", "source_pending"):
            with self.subTest(field=field):
                decision = decide_atomic_score_stage(self._input(**{field: True}))
                self.assertEqual(decision.score_type, AtomicScoreType.NO_SCORE.value)
                self.assertIsNone(decision.score_value)
                self.assertEqual(decision.raw_reference_score, 100.0)
                self.assertFalse(decision.score_valid)
                self.assertEqual(
                    decision.decision_status,
                    AtomicDecisionStatus.PENDING.value,
                )
                self.assertIn(field, decision.missing_conditions)

    def test_hard_break_requires_current_direct_open_source_backed_material_claim(self) -> None:
        risk_claim = AtomicScoreClaim(
            claim_id="CLAIM-HARD-BREAK",
            target_id=self.target_id,
            primitive_id="contract_cancelled",
            observed_date=self.as_of_date,
            content_hash=stable_hash("hard-break-current-direct"),
            source_ids=("SOURCE-HARD-BREAK",),
            anchor_ids=("ANCHOR-HARD-BREAK",),
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
        signal = AtomicHardBreakSignal(
            signal_id="HARD-BREAK-SIGNAL",
            claim_id=risk_claim.claim_id,
            condition_id="contract_cancelled_or_delayed",
            unresolved=True,
        )
        risk = decide_atomic_score_stage(
            self._input(
                claims=(*self.claims, risk_claim),
                hard_break_signals=(signal,),
                has_prior_live_thesis=True,
            )
        )
        self.assertEqual(risk.canonical_stage, CanonicalStage.STAGE_4C.value)
        self.assertEqual(risk.decision_status, AtomicDecisionStatus.RISK_REVIEW.value)
        self.assertEqual(risk.hard_break_claim_ids, (risk_claim.claim_id,))
        with self.assertRaisesRegex(ValueError, "hard break violates"):
            replace(
                risk,
                hard_break_claim_ids=(),
                stage_court_trace=replace(
                    risk.stage_court_trace,
                    hard_break_claim_ids=(),
                ),
            )
        omitted = risk.to_dict()
        omitted["hard_break_claim_ids"] = []
        omitted["stage_court_trace"]["hard_break_claim_ids"] = []
        omitted_audit = audit_atomic_stage_decisions((omitted,))
        self.assertEqual(
            omitted_audit["critical_counts"][
                "hard_break_without_current_direct_open"
            ],
            1,
        )

        wrong_subject = replace(
            risk_claim,
            claim_id="CLAIM-WRONG-SUBJECT-RISK",
            target_direct=False,
        )
        rejected_signal = replace(
            signal,
            signal_id="HARD-BREAK-WRONG-SUBJECT",
            claim_id=wrong_subject.claim_id,
        )
        safe = decide_atomic_score_stage(
            self._input(
                claims=(*self.claims, wrong_subject),
                hard_break_signals=(rejected_signal,),
                has_prior_live_thesis=True,
            )
        )
        self.assertEqual(safe.canonical_stage, CanonicalStage.STAGE_3_GREEN.value)
        self.assertFalse(safe.hard_break_claim_ids)
        self.assertEqual(
            safe.rejected_hard_break_signal_ids,
            (rejected_signal.signal_id,),
        )

        invalid_variants = {
            "not_current_open": replace(
                risk_claim,
                claim_id="CLAIM-NOT-CURRENT-OPEN",
                current_open=False,
            ),
            "not_source_backed": replace(
                risk_claim,
                claim_id="CLAIM-NOT-SOURCE-BACKED",
                source_backed=False,
            ),
            "not_material": replace(
                risk_claim,
                claim_id="CLAIM-NOT-MATERIAL",
                material=False,
            ),
            "historical_replay": replace(
                risk_claim,
                claim_id="CLAIM-HISTORICAL-RISK",
                historical_replay=True,
            ),
            "future_observed": replace(
                risk_claim,
                claim_id="CLAIM-FUTURE-RISK",
                observed_date="2026-07-01",
            ),
        }
        for label, invalid_claim in invalid_variants.items():
            with self.subTest(hard_break_condition=label):
                invalid_signal = replace(
                    signal,
                    signal_id=f"HARD-BREAK-{label}",
                    claim_id=invalid_claim.claim_id,
                )
                invalid_decision = decide_atomic_score_stage(
                    self._input(
                        claims=(*self.claims, invalid_claim),
                        hard_break_signals=(invalid_signal,),
                        has_prior_live_thesis=True,
                    )
                )
                self.assertFalse(invalid_decision.hard_break_claim_ids)
                self.assertEqual(
                    invalid_decision.rejected_hard_break_signal_ids,
                    (invalid_signal.signal_id,),
                )

        resolved_signal = replace(
            signal,
            signal_id="HARD-BREAK-RESOLVED",
            unresolved=False,
        )
        resolved_decision = decide_atomic_score_stage(
            self._input(
                claims=(*self.claims, risk_claim),
                hard_break_signals=(resolved_signal,),
                has_prior_live_thesis=True,
            )
        )
        self.assertFalse(resolved_decision.hard_break_claim_ids)

        wrong_polarity = replace(
            risk_claim,
            claim_id="CLAIM-SUPPORT-CANNOT-HARD-BREAK",
            polarity=AtomicClaimPolarity.SUPPORT.value,
        )
        wrong_polarity_signal = replace(
            signal,
            signal_id="HARD-BREAK-SUPPORT-POLARITY",
            claim_id=wrong_polarity.claim_id,
        )
        polarity_rejected = decide_atomic_score_stage(
            self._input(
                claims=(*self.claims, wrong_polarity),
                hard_break_signals=(wrong_polarity_signal,),
                has_prior_live_thesis=True,
            )
        )
        self.assertFalse(polarity_rejected.hard_break_claim_ids)
        self.assertEqual(
            polarity_rejected.rejected_hard_break_signal_ids,
            (wrong_polarity_signal.signal_id,),
        )

    def test_atomic_constructor_rejects_stage_trace_and_fingerprint_tampering(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "stage or status differs from deterministic score",
        ):
            replace(self.full, canonical_stage=CanonicalStage.STAGE_2.value)
        with self.assertRaisesRegex(ValueError, "StageCourt trace mismatch"):
            replace(
                self.full,
                stage_court_trace=replace(
                    self.full.stage_court_trace,
                    canonical_stage=CanonicalStage.STAGE_2.value,
                ),
            )
        with self.assertRaisesRegex(ValueError, "StageCourt reasons mismatch"):
            replace(
                self.full,
                stage_court_trace=replace(
                    self.full.stage_court_trace,
                    reasons=("forged_reason",),
                ),
            )
        with self.assertRaisesRegex(ValueError, "score fingerprint mismatch"):
            replace(
                self.full,
                score_fingerprint="0" * 64,
                stage_court_trace=replace(
                    self.full.stage_court_trace,
                    score_fingerprint="0" * 64,
                ),
            )

    def test_atomic_constructor_rejects_numeric_status_and_raw_score_loopholes(self) -> None:
        with self.assertRaisesRegex(ValueError, "thresholds must be numeric"):
            AtomicStageConfig(stage1_threshold=True)
        with self.assertRaisesRegex(ValueError, "thresholds must be finite"):
            AtomicStageConfig(stage1_threshold=float("nan"))
        with self.assertRaisesRegex(ValueError, "points must be finite"):
            replace(self.full.contributions[0], points=float("nan"))
        with self.assertRaisesRegex(ValueError, "requires raw reference score"):
            replace(self.full, raw_reference_score=None)
        with self.assertRaisesRegex(ValueError, "finalization contract"):
            replace(self.full, provider_pending=True)
        with self.assertRaisesRegex(ValueError, "finalization contract"):
            replace(
                self.full,
                decision_status=AtomicDecisionStatus.PENDING.value,
            )
        with self.assertRaisesRegex(ValueError, "evidence contract"):
            replace(
                self.claims[0],
                polarity=AtomicClaimPolarity.COUNTER.value,
            )
        with self.assertRaisesRegex(ValueError, "evidence contract"):
            replace(self.claims[0], contradiction_resolved=False)

    def test_joint_stage_and_trace_forgery_is_recomputed_from_score(self) -> None:
        forged = self.full.to_dict()
        forged["canonical_stage"] = CanonicalStage.STAGE_2.value
        forged["stage_court_trace"]["canonical_stage"] = (
            CanonicalStage.STAGE_2.value
        )
        audit = audit_atomic_stage_decisions((forged,))
        self.assertEqual(
            audit["critical_counts"]["stage_score_trace_mismatch"],
            1,
        )
        with self.assertRaisesRegex(ValueError, "input fingerprint mismatch"):
            replace(
                self.full,
                input_fingerprint="0" * 64,
                stage_court_trace=replace(
                    self.full.stage_court_trace,
                    input_fingerprint="0" * 64,
                ),
            )

    def test_score_delta_requires_claim_config_or_contribution_change(self) -> None:
        changed_claims = tuple(
            replace(
                item,
                content_hash=stable_hash(
                    {"claim_id": item.claim_id, "version": 2}
                ),
            )
            if item.primitive_id == "revision_direction"
            else item
            for item in self.claims
        )
        changed_assessments = tuple(
            replace(item, evidence_strength=0.8)
            if item.primitive_id == "revision_direction"
            else item
            for item in self.assessments
        )
        changed = decide_atomic_score_stage(
            self._input(
                claims=changed_claims,
                primitive_assessments=changed_assessments,
            )
        )
        explained = audit_atomic_score_delta(self.full, changed)
        self.assertEqual(explained["status"], "ATOMIC_SCORE_DELTA_EXPLAINED")
        self.assertEqual(explained["score_delta"], -5.0)
        self.assertTrue(explained["claim_state_changed"])
        self.assertTrue(explained["contribution_changed"])

        assessment_only = decide_atomic_score_stage(
            self._input(primitive_assessments=changed_assessments)
        )
        assessment_only_audit = audit_atomic_score_delta(self.full, assessment_only)
        self.assertEqual(
            assessment_only_audit["status"],
            "ATOMIC_SCORE_DELTA_UNEXPLAINED",
        )
        self.assertFalse(assessment_only_audit["claim_state_changed"])
        self.assertFalse(assessment_only_audit["config_changed"])
        self.assertTrue(assessment_only_audit["contribution_changed"])

        tampered = self.full.to_dict()
        tampered["decision_id"] = "TAMPERED-SCORE-WITHOUT-LEAF-CHANGE"
        tampered["score_value"] = 99.0
        unexplained = audit_atomic_score_delta(self.full, tampered)
        self.assertEqual(
            unexplained["status"],
            "ATOMIC_SCORE_DELTA_UNEXPLAINED",
        )
        self.assertEqual(unexplained["unexplained_score_delta_count"], 1)

        invalid_numeric = self.full.to_dict()
        invalid_numeric["score_value"] = "not-a-score"
        invalid_numeric_audit = audit_atomic_score_delta(
            self.full,
            invalid_numeric,
        )
        self.assertEqual(
            invalid_numeric_audit["status"],
            "ATOMIC_SCORE_DELTA_UNEXPLAINED",
        )
        self.assertEqual(
            invalid_numeric_audit["unexplained_score_delta_count"],
            1,
        )

    def test_atomic_audit_passes_valid_types_and_catches_known_bad_payloads(self) -> None:
        material_missing = tuple(
            replace(
                item,
                status=AtomicPrimitiveStatus.MISSING.value,
                evidence_strength=0.0,
                support_claim_ids=(),
            )
            if item.primitive_id == "contract_quality"
            else item
            for item in self.assessments
        )
        event = decide_atomic_score_stage(
            self._input(
                scope=AtomicScoringScope.EVENT_EVIDENCE.value,
                primitive_assessments=material_missing,
            )
        )
        pending = decide_atomic_score_stage(
            self._input(primitive_assessments=material_missing)
        )
        audit = audit_atomic_stage_decisions((self.full, event, pending))
        self.assertEqual(
            audit["status"],
            "DETERMINISTIC_SCORE_STAGE_INTEGRITY_PASS",
        )
        self.assertEqual(audit["decision_count"], 3)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(
            audit["score_type_counts"],
            {
                "EVENT_EVIDENCE_PARTIAL": 1,
                "FULL_E2R_100": 1,
                "NO_SCORE": 1,
            },
        )
        self.assertEqual(
            audit["result_hash"],
            "be5c0d66b45bee42d0e37285f5a96161672a4daf7c0e867c7d658090c3bf9dbe",
        )

        bad = self.full.to_dict()
        bad["score_value"] = 99.0
        bad_audit = audit_atomic_stage_decisions((bad,))
        self.assertEqual(
            bad_audit["status"],
            "DETERMINISTIC_SCORE_STAGE_INTEGRITY_FAIL",
        )
        self.assertEqual(
            bad_audit["critical_counts"]["stage_score_trace_mismatch"],
            1,
        )
        self.assertEqual(
            bad_audit["critical_counts"]["fingerprint_mismatch_concealed"],
            1,
        )

        material_gap_forged = self.full.to_dict()
        for assessment in material_gap_forged["primitive_assessments"]:
            if assessment["primitive_id"] == "contract_quality":
                assessment["status"] = AtomicPrimitiveStatus.MISSING.value
                assessment["evidence_strength"] = 0.0
                assessment["support_claim_ids"] = []
        material_gap_audit = audit_atomic_stage_decisions((material_gap_forged,))
        self.assertEqual(
            material_gap_audit["critical_counts"]["material_gap_full_score"],
            1,
        )

        claimless_forged = self.full.to_dict()
        claimless_forged["claims"] = []
        claimless_audit = audit_atomic_stage_decisions((claimless_forged,))
        self.assertEqual(claimless_audit["critical_counts"]["claimless_score"], 1)
        self.assertGreater(
            claimless_audit["critical_counts"]["score_contribution_without_claim"],
            0,
        )

        pending_low = pending.to_dict()
        pending_low["score_value"] = 25.0
        pending_low_audit = audit_atomic_stage_decisions((pending_low,))
        self.assertEqual(
            pending_low_audit["critical_counts"]["pending_final_low_score"],
            1,
        )


if __name__ == "__main__":
    unittest.main()
