from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.research_quality import (
    FAILURE_NEXT_ACTIONS,
    RESEARCH_REPAIR_FAILURE_CLASSES,
    audit_adaptive_repair_contract,
    canonical_research_failure_class,
    compile_research_repair_directive,
)
from e2r.research_brain.runtime.live_materialization.adaptive_gap_closure import (
    AdaptiveGapAttempt,
    _audit_adaptive_gap,
)


class AdaptiveResearchRepairLoopTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_every_semantic_failure_returns_context_to_llm_without_query_template(self) -> None:
        self.assertEqual(
            RESEARCH_REPAIR_FAILURE_CLASSES,
            set(FAILURE_NEXT_ACTIONS),
        )
        for failure_class in RESEARCH_REPAIR_FAILURE_CLASSES:
            directive = compile_research_repair_directive(
                failure_class=failure_class,
                question_family_id="arbitrary_question",
                original_question="What current material fact resolves this question?",
                failure_reason="failure evidence",
            )
            self.assertEqual(directive.query_generation_owner, "LLM")
            self.assertFalse(directive.deterministic_fallback_query_allowed)
            self.assertTrue(directive.require_novel_query)
            self.assertNotIn("suggested_queries", directive.to_dict())
            self.assertNotIn("HBM", directive.next_action)
            self.assertNotIn("contract_quality", directive.next_action)

    def test_rerouted_and_counter_evidence_are_preserved_while_gap_stays_open(self) -> None:
        rerouted = compile_research_repair_directive(
            failure_class="REROUTED_MECHANISM",
            question_family_id="question-a",
            original_question="What resolves the original mechanism?",
            failure_reason="claim belongs to another mechanism",
            preserved_evidence_ids=("IMPACT-OTHER",),
        )
        counter = compile_research_repair_directive(
            failure_class="COUNTER_ONLY",
            question_family_id="question-b",
            original_question="Is positive support also present?",
            failure_reason="only a counter claim was validated",
            preserved_evidence_ids=("COUNTER-1",),
        )
        self.assertTrue(rerouted.preserve_rerouted_impacts)
        self.assertTrue(rerouted.original_gap_open)
        self.assertEqual(
            rerouted.score_gap_context["preserved_evidence_ids"],
            ("IMPACT-OTHER",),
        )
        self.assertTrue(counter.preserve_counter_evidence)
        self.assertTrue(counter.original_gap_open)

    def test_gold_miss_returns_only_failure_reason_not_gold_answer(self) -> None:
        directive = compile_research_repair_directive(
            failure_class="GOLD_MATERIAL_FACT_MISSED",
            question_family_id="question-a",
            original_question="What material fact is missing?",
            failure_reason="miss found at https://gold.private/fact",
            preserved_evidence_ids=("GOLD-FACT-SECRET",),
            validation_feedback=("use https://gold.private/source",),
        )
        context = directive.score_gap_context
        self.assertEqual(context["preserved_evidence_ids"], ())
        self.assertEqual(context["validation_feedback"], ())
        self.assertNotIn("https://", context["failure_reason"])
        self.assertEqual(
            directive.next_action,
            "REPLAN_WITHOUT_GOLD_SOURCE_OR_FACT",
        )

    def test_duplicate_query_is_a_hard_repair_failure(self) -> None:
        attempt = AdaptiveGapAttempt(
            attempt_id="A1",
            source_task_id="T1",
            target_id="X",
            failure_reason_code="GENERIC_CONTEXT_ONLY",
            next_action="PRIORITIZE_TARGET_DIRECT_QUANTIFIED_SOURCE",
            previous_queries=("X 2026 filing",),
            suggested_queries=("X 2026 filing",),
            planning_status="COMPLETE",
            terminal_status="SOURCE_PENDING",
            provider_name="fixture",
            prompt_hash="a" * 64,
            response_hash="b" * 64,
            identical_query=True,
        )
        audit = _audit_adaptive_gap(
            ledger=(),
            attempts=(attempt,),
            gaps=(),
        )
        self.assertFalse(audit["hard_acceptance_pass"])
        self.assertEqual(audit["critical_counts"]["identical_retry"], 1)

    def test_aliases_map_to_canonical_failure_classes(self) -> None:
        self.assertEqual(
            canonical_research_failure_class("SOURCE_EXHAUSTED"),
            "NO_DOCUMENT_FOUND",
        )
        self.assertEqual(
            canonical_research_failure_class(
                "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN"
            ),
            "REROUTED_MECHANISM",
        )
        with self.assertRaisesRegex(ValueError, "unknown adaptive"):
            canonical_research_failure_class("UNDECLARED_FAILURE")

    def test_operational_contract_audit_is_replayable(self) -> None:
        actual = audit_adaptive_repair_contract()
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_adaptive_research_repair_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
