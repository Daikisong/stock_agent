from __future__ import annotations

from dataclasses import replace
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.researcher_mode import (
    AGGREGATOR_CONFIG,
    CANONICAL_COMPONENT_MAX_POINTS,
    CANONICAL_COMPONENT_ORDER,
    SCORE_AGGREGATION_OUTPUT_FILES,
    ComponentAnchor,
    ComponentResearchMemo,
    ComponentResearchResult,
    DeterministicScoreAggregator,
    EvidenceFact,
    LLMComponentScoringMemoEngine,
    PHASE90_PASS,
    compile_phase90_deterministic_score_aggregator_audit,
    write_deterministic_score_aggregation_run,
)


TARGET = "PHASE90-CURRENT-TARGET"
ARCHETYPE = "PHASE90-CURRENT-ARCHETYPE"
AS_OF_DATE = "2026-06-29"


class Phase90JudgeProvider:
    provider_name = "PHASE90-JUDGE-PROVIDER"

    def __init__(self, mode: str = "BASE") -> None:
        self.mode = mode
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self,
        *,
        pass_name: str,
        payload: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        self.calls.append({"pass_name": pass_name, "payload": payload})
        memo = payload["component_research_memo"]
        maximum = float(payload["component_max_points"])
        fractions = {
            "BASE": {
                "COMPONENT_ANALYST_JUDGE": 0.84,
                "COMPONENT_SKEPTIC_JUDGE": 0.72,
                "CALIBRATION_JUDGE": 0.80,
            },
            "STRONG": {
                "COMPONENT_ANALYST_JUDGE": 0.94,
                "COMPONENT_SKEPTIC_JUDGE": 0.88,
                "CALIBRATION_JUDGE": 0.92,
            },
            "DISAGREE": {
                "COMPONENT_ANALYST_JUDGE": 0.92,
                "COMPONENT_SKEPTIC_JUDGE": 0.20,
                "CALIBRATION_JUDGE": 0.86,
            },
        }[self.mode]
        lower, upper = {
            "BASE": (0.60, 0.94),
            "STRONG": (0.80, 1.00),
            "DISAGREE": (0.10, 0.98),
        }[self.mode]
        return {
            "anchor_comparisons": [
                "current economic strength was placed against blind historical bands"
            ],
            "proposed_points": maximum * fractions[pass_name],
            "allowed_range": [maximum * lower, maximum * upper],
            "rationale": "current support, counterevidence, and anchor scale were reviewed",
            "disagreements": (
                ["material economic-strength disagreement remains"]
                if self.mode == "DISAGREE"
                else []
            ),
            "support_fact_ids": list(memo["positive_fact_ids"]),
            "counter_fact_ids": list(memo["counter_fact_ids"]),
            "nearest_anchor_ids": list(memo["historical_anchor_ids"]),
            "why_not_higher": "open counterevidence constrains the ceiling",
            "why_not_lower": "direct current evidence and anchors establish the floor",
        }


class E2RV5DeterministicScoreAggregatorTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_phase90_audit_is_reproducible_and_complete(self) -> None:
        actual = compile_phase90_deterministic_score_aggregator_audit(self.ROOT)
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_deterministic_score_aggregator_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, committed)
        self.assertEqual(actual["status"], PHASE90_PASS)
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertEqual(actual["canary_counts"]["judge_proposals"], 21)

    def test_complete_run_validates_twenty_one_proposals_and_sums_seven_components(self) -> None:
        run, _, _, _, _ = _aggregation_run()
        self.assertEqual(run.status, "DETERMINISTIC_SCORE_COMPLETE")
        self.assertTrue(run.score_valid)
        self.assertTrue(run.ready_for_stagecourt)
        self.assertEqual(len(run.component_results), 7)
        self.assertEqual(
            sum(len(row.proposal_validations) for row in run.component_results), 21
        )
        self.assertTrue(
            all(validation.valid for row in run.component_results for validation in row.proposal_validations)
        )
        score = run.total_result.score
        self.assertIsNotNone(score)
        self.assertAlmostEqual(score.total_points, 72.0)  # type: ignore[union-attr]
        self.assertAlmostEqual(score.max_points, 100.0)  # type: ignore[union-attr]
        self.assertEqual(len(score.judge_ids), 21)  # type: ignore[union-attr]
        self.assertEqual(len(score.prompt_hashes), 21)  # type: ignore[union-attr]
        self.assertEqual(run.audit["critical_count_sum"], 0)

    def test_component_decision_has_every_required_phase90_lineage(self) -> None:
        run, _, _, _, _ = _aggregation_run()
        for result in run.component_results:
            decision = result.decision
            self.assertIsNotNone(decision)
            self.assertTrue(decision.fact_ids)  # type: ignore[union-attr]
            self.assertTrue(decision.counter_fact_ids)  # type: ignore[union-attr]
            self.assertTrue(decision.anchor_ids)  # type: ignore[union-attr]
            self.assertEqual(len(decision.judge_ids), 3)  # type: ignore[union-attr]
            self.assertEqual(len(decision.prompt_hashes), 3)  # type: ignore[union-attr]
            self.assertEqual(len(decision.config_hash), 64)  # type: ignore[union-attr]
            self.assertAlmostEqual(
                decision.support_points - decision.counter_effect,  # type: ignore[union-attr]
                decision.final_points,  # type: ignore[union-attr]
            )
            self.assertFalse(decision.source_confidence_affects_points)  # type: ignore[union-attr]
            self.assertFalse(decision.production_stage_authority)  # type: ignore[union-attr]

    def test_invalid_extra_proposal_is_removed_and_recorded(self) -> None:
        _, scoring_run, memos, facts, anchors = _aggregation_run()
        decisions = list(scoring_run.component_memos[0].judge_decisions)
        invalid_extra = replace(
            decisions[0],
            component_id=CANONICAL_COMPONENT_ORDER[1],
        )
        result = DeterministicScoreAggregator().aggregate_component(
            memo=memos[0],
            judge_decisions=(*decisions, invalid_extra),
            evidence_facts=facts,
            historical_anchors=anchors,
            expected_as_of_date=AS_OF_DATE,
        )
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(result.invalid_proposal_count, 1)
        self.assertIn(
            "JUDGE_COMPONENT_ID_MISMATCH",
            result.proposal_validations[-1].reason_codes,
        )

    def test_invalid_required_proposal_cannot_become_a_low_score(self) -> None:
        _, scoring_run, memos, facts, anchors = _aggregation_run()
        decisions = list(scoring_run.component_memos[0].judge_decisions)
        decisions[0] = replace(decisions[0], support_fact_ids=("UNKNOWN-FACT",))
        result = DeterministicScoreAggregator().aggregate_component(
            memo=memos[0],
            judge_decisions=decisions,
            evidence_facts=facts,
            historical_anchors=anchors,
            expected_as_of_date=AS_OF_DATE,
        )
        self.assertEqual(result.status, "RESEARCH_REQUIRED")
        self.assertIsNone(result.decision)
        self.assertIn("THREE_VALID_JUDGE_CONSENSUS_MISSING", result.pending_reasons)

    def test_material_disagreement_returns_llm_owned_research_request(self) -> None:
        run, _, _, _, _ = _aggregation_run(mode="DISAGREE")
        self.assertEqual(run.status, "DETERMINISTIC_SCORE_RESEARCH_REQUIRED")
        self.assertFalse(run.score_valid)
        self.assertIsNone(run.total_result.score)
        self.assertEqual(len(run.research_requests), 7)
        for request in run.research_requests:
            self.assertIn(
                "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT",
                request.reason_codes,
            )
            self.assertEqual(
                request.query_generation_authority, "LLM_RESEARCH_SUPERVISOR"
            )
            self.assertFalse(request.deterministic_query_synthesis)

    def test_skeptic_counter_effect_is_applied_once_and_cannot_create_support(self) -> None:
        run, _, _, _, _ = _aggregation_run()
        first = run.component_results[0].decision
        self.assertIsNotNone(first)
        self.assertAlmostEqual(first.support_points, 16.4)  # type: ignore[union-attr]
        self.assertAlmostEqual(first.final_points, 14.4)  # type: ignore[union-attr]
        self.assertAlmostEqual(first.counter_effect, 2.0)  # type: ignore[union-attr]
        self.assertLessEqual(first.final_points, first.support_points)  # type: ignore[union-attr]

    def test_independent_corroboration_changes_confidence_not_economic_points(self) -> None:
        _, scoring_run, memos, _, anchors = _aggregation_run()
        base_facts = _facts(corroborated=False)
        corroborated_facts = _facts(corroborated=True)
        aggregator = DeterministicScoreAggregator()
        kwargs = {
            "memo": memos[0],
            "judge_decisions": scoring_run.component_memos[0].judge_decisions,
            "historical_anchors": anchors,
            "expected_as_of_date": AS_OF_DATE,
        }
        base = aggregator.aggregate_component(
            evidence_facts=base_facts,
            **kwargs,
        )
        corroborated = aggregator.aggregate_component(
            evidence_facts=corroborated_facts,
            **kwargs,
        )
        self.assertEqual(base.status, "COMPLETE")
        self.assertEqual(corroborated.status, "COMPLETE")
        self.assertEqual(base.decision.final_points, corroborated.decision.final_points)  # type: ignore[union-attr]
        self.assertGreater(
            corroborated.decision.confidence,  # type: ignore[union-attr]
            base.decision.confidence,  # type: ignore[union-attr]
        )

    def test_low_source_reliability_holds_finalization_instead_of_multiplying_points(self) -> None:
        _, scoring_run, memos, _, _ = _aggregation_run()
        low_facts = tuple(
            replace(
                row,
                confidence=0.01,
                source_independence_group="ONE-SOURCE",
                corroborating_independence_groups=(),
            )
            for row in _facts(corroborated=False)
        )
        low_anchors = tuple(replace(row, confidence="LOW") for row in _anchors())
        result = DeterministicScoreAggregator().aggregate_component(
            memo=memos[0],
            judge_decisions=scoring_run.component_memos[0].judge_decisions,
            evidence_facts=low_facts,
            historical_anchors=low_anchors,
            expected_as_of_date=AS_OF_DATE,
        )
        self.assertEqual(result.status, "RESEARCH_REQUIRED")
        self.assertIsNone(result.decision)
        self.assertIn(
            "SOURCE_CONFIDENCE_BELOW_FINALIZATION_THRESHOLD",
            result.pending_reasons,
        )

    def test_strong_high_anchor_equivalent_evidence_does_not_collapse_to_one_to_three_points(self) -> None:
        run, _, _, _, _ = _aggregation_run(mode="STRONG")
        first = run.component_results[0].decision
        self.assertIsNotNone(first)
        self.assertGreater(first.final_points, 16.0)  # type: ignore[union-attr]
        self.assertGreater(first.final_points, first.max_points * 0.80)  # type: ignore[union-attr]

    def test_prompt_hashes_are_derived_and_caller_cannot_replace_lineage(self) -> None:
        _, scoring_run, memos, facts, anchors = _aggregation_run()
        result = DeterministicScoreAggregator().aggregate_component(
            memo=memos[0],
            judge_decisions=scoring_run.component_memos[0].judge_decisions,
            evidence_facts=facts,
            historical_anchors=anchors,
            expected_as_of_date=AS_OF_DATE,
            prompt_hashes=("f" * 64, "e" * 64, "d" * 64),
        )
        self.assertEqual(result.status, "RESEARCH_REQUIRED")
        self.assertIn("CALLER_PROMPT_HASH_LINEAGE_MISMATCH", result.pending_reasons)

    def test_cross_component_prompt_reuse_blocks_total(self) -> None:
        run, _, _, _, _ = _aggregation_run()
        decisions = [row.decision for row in run.component_results]
        decisions[1] = replace(
            decisions[1],  # type: ignore[arg-type]
            prompt_hashes=decisions[0].prompt_hashes,  # type: ignore[union-attr]
        )
        total = DeterministicScoreAggregator().aggregate_total(decisions)  # type: ignore[arg-type]
        self.assertEqual(total.status, "RESEARCH_REQUIRED")
        self.assertIn("CROSS_COMPONENT_PROMPT_HASH_REUSE", total.pending_reasons)

    def test_total_requires_exactly_seven_complete_decisions(self) -> None:
        run, _, _, _, _ = _aggregation_run()
        decisions = [row.decision for row in run.component_results]
        missing = DeterministicScoreAggregator().aggregate_total(decisions[:-1])  # type: ignore[arg-type]
        duplicate = DeterministicScoreAggregator().aggregate_total(
            (*decisions, decisions[0])  # type: ignore[arg-type]
        )
        self.assertEqual(missing.status, "RESEARCH_REQUIRED")
        self.assertEqual(duplicate.status, "RESEARCH_REQUIRED")

    def test_run_scope_and_anchor_lineage_fail_closed(self) -> None:
        scoring_run = _scoring_run()
        memos = _memos()
        cross_as_of = tuple(
            replace(row, as_of_date="2026-06-30") if index == 0 else row
            for index, row in enumerate(_facts())
        )
        run = DeterministicScoreAggregator().aggregate_run(
            scoring_memo_run=scoring_run,
            component_research_memos=memos,
            evidence_facts=cross_as_of,
            historical_anchors=_anchors(),
        )
        self.assertFalse(run.score_valid)
        self.assertIn("RUN_EVIDENCE_FACT_AS_OF_MISMATCH", run.pending_reasons)
        direct = DeterministicScoreAggregator().aggregate_component(
            memo=memos[0],
            judge_decisions=scoring_run.component_memos[0].judge_decisions,
            evidence_facts=_facts(),
            historical_anchors=_anchors()[2:],
            expected_as_of_date=AS_OF_DATE,
        )
        self.assertEqual(direct.status, "RESEARCH_REQUIRED")
        self.assertTrue(
            any("UNAVAILABLE_HISTORICAL_ANCHOR" in reason for reason in direct.pending_reasons)
        )

    def test_serialized_anchor_usability_type_tampering_is_rejected(self) -> None:
        _, scoring_run, memos, facts, anchors = _aggregation_run()
        serialized = [row.to_dict() for row in anchors]
        serialized[0]["usable_as_ordinal_anchor"] = 1
        result = DeterministicScoreAggregator().aggregate_component(
            memo=memos[0],
            judge_decisions=scoring_run.component_memos[0].judge_decisions,
            evidence_facts=facts,
            historical_anchors=serialized,
            expected_as_of_date=AS_OF_DATE,
        )
        self.assertEqual(result.status, "RESEARCH_REQUIRED")
        self.assertTrue(
            any(
                "INVALID_HISTORICAL_ANCHOR_USABILITY_TYPE" in reason
                for reason in result.pending_reasons
            )
        )

    def test_total_and_run_config_hash_lineage_must_be_hexadecimal(self) -> None:
        run, _, _, _, _ = _aggregation_run()
        score = run.total_result.score
        self.assertIsNotNone(score)
        with self.assertRaisesRegex(ValueError, "hexadecimal"):
            replace(score, config_hash="z" * 64)  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, "hexadecimal"):
            replace(run, config_hash="z" * 64)

    def test_safeguard_config_cannot_enable_confidence_or_tiny_cap_point_multiplication(self) -> None:
        for key in (
            "source_confidence_affects_points",
            "independent_corroboration_affects_points",
            "tiny_impact_cap_multiplication",
            "stage_authority",
        ):
            config = {**AGGREGATOR_CONFIG, key: True}
            with self.assertRaisesRegex(ValueError, "safeguard"):
                DeterministicScoreAggregator(config=config)

    def test_writer_emits_all_phase90_leaf_artifacts(self) -> None:
        run, _, _, _, _ = _aggregation_run()
        with tempfile.TemporaryDirectory() as directory:
            paths = write_deterministic_score_aggregation_run(run, directory)
            self.assertEqual(set(paths), set(SCORE_AGGREGATION_OUTPUT_FILES))
            self.assertTrue(all(path.is_file() for path in paths.values()))
            component_rows = paths["component_results"].read_text(
                encoding="utf-8"
            ).splitlines()
            validation_rows = paths["proposal_validations"].read_text(
                encoding="utf-8"
            ).splitlines()
            self.assertEqual(len(component_rows), 7)
            self.assertEqual(len(validation_rows), 21)
            self.assertEqual(
                json.loads(paths["audit"].read_text(encoding="utf-8")),
                run.audit,
            )

    def test_output_is_reproducible_and_contains_no_stage_decision(self) -> None:
        first = _aggregation_run()[0].to_dict()
        second = _aggregation_run()[0].to_dict()
        self.assertEqual(first, second)
        keys = _recursive_keys(first)
        self.assertNotIn("stage", keys)
        self.assertNotIn("canonical_stage", keys)
        self.assertNotIn("final_stage", keys)


def _aggregation_run(*, mode: str = "BASE"):
    facts = _facts()
    anchors = _anchors()
    scoring_run = _scoring_run(mode=mode, facts=facts, anchors=anchors)
    memos = _memos()
    run = DeterministicScoreAggregator().aggregate_run(
        scoring_memo_run=scoring_run,
        component_research_memos=memos,
        evidence_facts=facts,
        historical_anchors=anchors,
    )
    return run, scoring_run, memos, facts, anchors


def _scoring_run(*, mode: str = "BASE", facts=None, anchors=None):
    return LLMComponentScoringMemoEngine(
        analyst_provider=Phase90JudgeProvider(mode)
    ).build(
        target_id=TARGET,
        archetype_id=ARCHETYPE,
        as_of_date=AS_OF_DATE,
        component_results=_component_results(),
        evidence_facts=_facts() if facts is None else facts,
        historical_anchors=_anchors() if anchors is None else anchors,
    )


def _facts(*, corroborated: bool = True) -> tuple[EvidenceFact, ...]:
    common = {
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "subject": "current target operating business",
        "business_segment": "core segment",
        "product_family": "core product",
        "unit": "flag",
        "period": "2026Q2",
        "question_family_tags": (),
        "primitive_tags": (),
    }
    return (
        EvidenceFact(
            fact_id="PHASE90-FACT-SUPPORT",
            economic_mechanism="direct operating strength converts into earnings and cash",
            predicate="current_operating_strength",
            value=True,
            direction="POSITIVE",
            source_ids=("PHASE90-SOURCE-SUPPORT",),
            claim_ids=("PHASE90-CLAIM-SUPPORT",),
            quote_ids=("PHASE90-QUOTE-SUPPORT",),
            current_lifecycle="CURRENT",
            source_independence_group="ISSUER",
            corroborating_independence_groups=(
                ("INDEPENDENT-RESEARCH",) if corroborated else ()
            ),
            confidence=0.86,
            **common,
        ),
        EvidenceFact(
            fact_id="PHASE90-FACT-COUNTER",
            economic_mechanism="open concentration risk constrains durability",
            predicate="concentration_risk",
            value=True,
            direction="COUNTER",
            source_ids=("PHASE90-SOURCE-COUNTER",),
            claim_ids=("PHASE90-CLAIM-COUNTER",),
            quote_ids=("PHASE90-QUOTE-COUNTER",),
            current_lifecycle="OPEN",
            source_independence_group=("INDEPENDENT-RESEARCH" if corroborated else "ISSUER"),
            corroborating_independence_groups=(),
            confidence=0.80,
            **common,
        ),
    )


def _anchors() -> tuple[ComponentAnchor, ...]:
    rows = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        for role, suffix, fraction in (
            ("POSITIVE", "P", 0.85),
            ("COUNTER", "C", 0.40),
        ):
            rows.append(
                ComponentAnchor(
                    anchor_id=f"PHASE90-ANCHOR-{component_id}-{suffix}",
                    archetype_id=ARCHETYPE,
                    component_id=component_id,
                    economic_fact_patterns=("blind source-backed economic pattern",),
                    role=role,
                    score_band="HIGH" if role == "POSITIVE" else "LOW",
                    points_lower=maximum * max(0.0, fraction - 0.10),
                    points_mid=maximum * fraction,
                    points_upper=maximum * min(1.0, fraction + 0.10),
                    max_points=maximum,
                    source_backed_case_ids=(
                        f"PHASE90-BLIND-CASE-{component_id}-{suffix}",
                    ),
                    source_proxy_guard_case_ids=(),
                    source_score_anchor_ids=(
                        f"PHASE90-SCORE-LINEAGE-{component_id}-{suffix}",
                    ),
                    confidence="MEDIUM",
                    usable_as_exact_anchor=False,
                    usable_as_ordinal_anchor=True,
                )
            )
    return tuple(rows)


def _memos() -> tuple[ComponentResearchMemo, ...]:
    return tuple(row.memo for row in _component_results())  # type: ignore[misc]


def _component_results() -> tuple[ComponentResearchResult, ...]:
    rows = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        memo = ComponentResearchMemo(
            memo_id=f"PHASE90-RESEARCH-MEMO-{component_id}",
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            component_id=component_id,
            component_max_points=maximum,
            positive_fact_ids=("PHASE90-FACT-SUPPORT",),
            counter_fact_ids=("PHASE90-FACT-COUNTER",),
            resolution_fact_ids=(),
            structured_metrics={"current_strength": 1.0, "concentration": 0.4},
            historical_anchor_ids=(
                f"PHASE90-ANCHOR-{component_id}-P",
                f"PHASE90-ANCHOR-{component_id}-C",
            ),
            researcher_summary="current source-backed economics were fully researched",
            positive_case="direct current evidence supports a high economic range",
            counter_case="open concentration risk constrains the upper range",
            uncertainties=("duration still requires monitoring",),
            source_coverage=("ISSUER_OFFICIAL", "INDEPENDENT_REPORT"),
            proposed_score_lower=maximum * 0.50,
            proposed_score_mid=maximum * 0.72,
            proposed_score_upper=maximum * 0.92,
            confidence=0.82,
            research_complete=True,
            nearest_positive_anchor_ids=(
                f"PHASE90-ANCHOR-{component_id}-P",
            ),
            nearest_counter_anchor_ids=(
                f"PHASE90-ANCHOR-{component_id}-C",
            ),
            why_not_higher="open counterevidence remains",
            why_not_lower="direct source-backed economic strength exists",
            researcher_role=f"PHASE90-{component_id}-RESEARCHER",
        )
        rows.append(
            ComponentResearchResult(
                component_id=component_id,
                researcher_role=memo.researcher_role,
                status="COMPLETE",
                memo=memo,
                pending_reasons=(),
                provider_name="PHASE90-RESEARCH-FIXTURE",
                prompt_hash=f"PHASE90-RESEARCH-PROMPT-{component_id}",
            )
        )
    return tuple(rows)


def _recursive_keys(value: Any) -> set[str]:
    if isinstance(value, Mapping):
        return set(value) | {
            nested
            for item in value.values()
            for nested in _recursive_keys(item)
        }
    if isinstance(value, (list, tuple)):
        return {
            nested for item in value for nested in _recursive_keys(item)
        }
    return set()


if __name__ == "__main__":
    unittest.main()
