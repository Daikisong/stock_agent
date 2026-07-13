from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.researcher_mode import (
    CANONICAL_COMPONENT_MAX_POINTS,
    CANONICAL_COMPONENT_ORDER,
    COMPONENT_SCORING_MEMO_OUTPUT_FILES,
    JUDGE_RESPONSE_FIELDS,
    PHASE89_PASS,
    REQUIRED_COMPONENT_JUDGE_ROLES,
    ComponentAnchor,
    ComponentResearchMemo,
    ComponentResearchResult,
    EvidenceFact,
    LLMComponentScoringMemoEngine,
    compile_phase89_component_scoring_memos_audit,
    write_component_scoring_memo_run,
)


TARGET = "PHASE89-CURRENT-TARGET"
ARCHETYPE = "PHASE89-CURRENT-ARCHETYPE"
AS_OF_DATE = "2026-06-29"


class Phase89JudgeProvider:
    provider_name = "PHASE89-JUDGE-PROVIDER"

    def __init__(self, mode: str = "COMPLETE") -> None:
        self.mode = mode
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self,
        *,
        pass_name: str,
        payload: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        call: dict[str, Any] = {"pass_name": pass_name, "payload": payload}
        if self.mode == "CONSTANT_PROMPT_HASH":
            call["prompt_hash"] = "a" * 64
        self.calls.append(call)
        if self.mode == "ERROR":
            raise RuntimeError("phase89 provider unavailable")
        memo = payload["component_research_memo"]
        maximum = float(payload["component_max_points"])
        fraction = {
            "COMPONENT_ANALYST_JUDGE": 0.64,
            "COMPONENT_SKEPTIC_JUDGE": 0.50,
            "CALIBRATION_JUDGE": 0.57,
        }[pass_name]
        response: dict[str, Any] = {
            "anchor_comparisons": [
                "current economic shape is between the cited blind anchor bands"
            ],
            "proposed_points": maximum * fraction,
            "allowed_range": [maximum * 0.35, maximum * 0.72],
            "rationale": "current support, counterfacts, and anchor scale were reviewed",
            "disagreements": [],
            "support_fact_ids": list(memo["positive_fact_ids"]),
            "counter_fact_ids": list(memo["counter_fact_ids"]),
            "nearest_anchor_ids": list(memo["historical_anchor_ids"]),
            "why_not_higher": "counterevidence and uncertainty limit the upper bound",
            "why_not_lower": "direct current support and blind anchors support the floor",
        }
        if self.mode == "EXTRA_TOTAL_SCORE":
            response["total_score"] = 90
        if self.mode == "EXTRA_STAGE":
            response["stage"] = "3-Green"
        if self.mode == "MAX_VIOLATION":
            response["proposed_points"] = maximum + 1
            response["allowed_range"] = [0, maximum + 1]
        if self.mode == "BOOL_POINTS":
            response["proposed_points"] = True
        if self.mode == "ANALYST_OMITS_SUPPORT" and pass_name == "COMPONENT_ANALYST_JUDGE":
            response["support_fact_ids"] = []
        if self.mode == "SKEPTIC_OMITS_COUNTER" and pass_name == "COMPONENT_SKEPTIC_JUDGE":
            response["counter_fact_ids"] = []
        if (
            self.mode == "OUTSIDE_FACT_THEN_VALID"
            and "judge_validation_retry_context" not in payload
        ):
            response["support_fact_ids"] = [
                *response["support_fact_ids"],
                "FACT-OUTSIDE-COMPONENT-MEMO",
            ]
        return response


class E2RV5ComponentScoringMemoTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_phase89_audit_is_reproducible_and_complete(self) -> None:
        actual = compile_phase89_component_scoring_memos_audit(self.ROOT)
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_component_scoring_memos_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, committed)
        self.assertEqual(actual["status"], PHASE89_PASS)
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertEqual(actual["canary_counts"]["judge_memos"], 21)

    def test_all_seven_components_receive_three_independent_judge_memos(self) -> None:
        provider = Phase89JudgeProvider()
        result = _run(provider)
        self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_COMPLETE")
        self.assertTrue(result.ready_for_deterministic_aggregation)
        self.assertEqual(len(result.component_memos), 7)
        self.assertEqual(len(result.judge_decisions), 21)
        self.assertEqual(result.audit["critical_count_sum"], 0)
        self.assertEqual(len(provider.calls), 21)
        for memo in result.component_memos:
            self.assertEqual(
                {row.role for row in memo.judge_results},
                set(REQUIRED_COMPONENT_JUDGE_ROLES),
            )
            self.assertEqual(len(set(memo.prompt_hashes)), 3)
            self.assertEqual(
                len({row.judge_call_id for row in memo.judge_results}),
                3,
            )

    def test_each_judge_memo_has_exact_phase89_output_and_lineage(self) -> None:
        result = _run(Phase89JudgeProvider())
        for decision in result.judge_decisions:
            self.assertEqual(len(decision.prompt_hash), 64)
            self.assertEqual(len(decision.response_hash), 64)
            self.assertTrue(decision.judge_call_id)
            self.assertTrue(decision.support_fact_ids)
            self.assertTrue(decision.counter_fact_ids)
            self.assertTrue(decision.nearest_anchor_ids)
            self.assertTrue(decision.why_not_higher)
            self.assertTrue(decision.why_not_lower)
            self.assertLessEqual(
                decision.allowed_range[1], decision.component_max_points
            )
            self.assertFalse(decision.production_total_score_authority)
            self.assertFalse(decision.production_stage_authority)

    def test_judges_do_not_see_prior_researcher_score_band(self) -> None:
        provider = Phase89JudgeProvider()
        _run(provider)
        for call in provider.calls:
            memo = call["payload"]["component_research_memo"]
            self.assertFalse(
                {
                    "proposed_score_lower",
                    "proposed_score_mid",
                    "proposed_score_upper",
                    "why_not_higher",
                    "why_not_lower",
                    "confidence",
                }
                & set(memo)
            )

    def test_role_prompts_expose_distinct_generic_review_dimensions(self) -> None:
        provider = Phase89JudgeProvider()
        _run(provider)
        by_pass = {
            row["pass_name"]: set(row["payload"]["independent_role_mandate"])
            for row in provider.calls[:3]
        }
        self.assertIn("POSITIVE_THESIS", by_pass["COMPONENT_ANALYST_JUDGE"])
        self.assertTrue(
            {
                "COUNTEREVIDENCE",
                "BUSINESS_PHASE",
                "VALUATION",
                "CONCENTRATION",
                "UNCERTAINTY",
            }.issubset(by_pass["COMPONENT_SKEPTIC_JUDGE"])
        )
        self.assertIn(
            "HISTORICAL_ANCHOR_COMPARABILITY",
            by_pass["CALIBRATION_JUDGE"],
        )

    def test_total_score_or_stage_attempt_is_pending_not_ignored(self) -> None:
        for mode in ("EXTRA_TOTAL_SCORE", "EXTRA_STAGE"):
            result = _run(Phase89JudgeProvider(mode))
            self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_PENDING")
            self.assertFalse(result.ready_for_deterministic_aggregation)
            self.assertGreater(
                result.audit["critical_counts"]["pending_judge_result_count"],
                0,
            )
            self.assertTrue(
                any(
                    "INVALID_PROVIDER_OUTPUT" in reason
                    for memo in result.component_memos
                    for reason in memo.pending_reasons
                )
            )

    def test_missing_or_incompatible_anchor_blocks_calibration(self) -> None:
        anchors = _anchors()[2:]
        result = _run(Phase89JudgeProvider(), anchors=anchors)
        first = result.component_memos[0]
        self.assertEqual(first.status, "PENDING")
        self.assertTrue(
            all(
                "INVALID_JUDGE_INPUT_LINEAGE" in row.pending_reasons[0]
                for row in first.judge_results
            )
        )

    def test_provider_failure_and_unconfigured_provider_remain_pending(self) -> None:
        failed = _run(Phase89JudgeProvider("ERROR"))
        unconfigured = LLMComponentScoringMemoEngine(
            analyst_provider=None
        ).build(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            component_results=_component_results(),
            evidence_facts=_facts(),
            historical_anchors=_anchors(),
        )
        for result in (failed, unconfigured):
            self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_PENDING")
            self.assertFalse(result.ready_for_deterministic_aggregation)
            self.assertIsNone(result.to_dict().get("score"))

    def test_invalid_numeric_types_or_component_max_are_pending(self) -> None:
        for mode in ("MAX_VIOLATION", "BOOL_POINTS"):
            result = _run(Phase89JudgeProvider(mode))
            self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_PENDING")
            self.assertGreater(
                result.audit["critical_counts"]["pending_judge_result_count"],
                0,
            )

    def test_analyst_and_skeptic_must_account_for_their_fact_planes(self) -> None:
        for mode, role in (
            ("ANALYST_OMITS_SUPPORT", "ANALYST"),
            ("SKEPTIC_OMITS_COUNTER", "SKEPTIC"),
        ):
            result = _run(Phase89JudgeProvider(mode))
            self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_PENDING")
            self.assertTrue(
                any(
                    row.role == role and row.status == "PENDING"
                    for memo in result.component_memos
                    for row in memo.judge_results
                )
            )

    def test_invalid_judge_citation_is_returned_to_llm_for_one_clean_rewrite(
        self,
    ) -> None:
        provider = Phase89JudgeProvider("OUTSIDE_FACT_THEN_VALID")
        result = _run(provider)

        self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_COMPLETE")
        self.assertEqual(len(result.judge_decisions), 21)
        self.assertEqual(len(provider.calls), 42)
        retry_calls = [
            row
            for row in provider.calls
            if "judge_validation_retry_context" in row["payload"]
        ]
        self.assertEqual(len(retry_calls), 21)
        for call in retry_calls:
            context = call["payload"]["judge_validation_retry_context"]
            memo = call["payload"]["component_research_memo"]
            self.assertIn("outside the component memo", context["validation_error"])
            self.assertEqual(
                context["allowed_support_fact_ids"],
                memo["positive_fact_ids"],
            )
            self.assertEqual(
                context["allowed_counter_fact_ids"],
                memo["counter_fact_ids"],
            )
            self.assertEqual(
                context["allowed_nearest_anchor_ids"],
                memo["historical_anchor_ids"],
            )

    def test_reused_prompt_hash_cannot_prove_three_judge_independence(self) -> None:
        result = _run(Phase89JudgeProvider("CONSTANT_PROMPT_HASH"))
        self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_PENDING")
        self.assertEqual(
            result.audit["critical_counts"][
                "within_component_duplicate_prompt_hash_count"
            ],
            14,
        )
        self.assertTrue(
            all(
                "THREE_JUDGE_PROMPT_INDEPENDENCE_NOT_PROVEN"
                in memo.pending_reasons
                for memo in result.component_memos
            )
        )

    def test_writer_emits_component_judge_run_and_audit_leaves(self) -> None:
        result = _run(Phase89JudgeProvider())
        with tempfile.TemporaryDirectory() as directory:
            paths = write_component_scoring_memo_run(result, directory)
            self.assertEqual(set(paths), set(COMPONENT_SCORING_MEMO_OUTPUT_FILES))
            self.assertTrue(all(path.is_file() for path in paths.values()))
            judge_rows = [
                json.loads(line)
                for line in paths["judge_memos"]
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            self.assertEqual(len(judge_rows), 21)
            self.assertEqual(
                json.loads(paths["audit"].read_text(encoding="utf-8")),
                result.audit,
            )

    def test_run_is_reproducible_and_carries_no_total_or_stage_output(self) -> None:
        first = _run(Phase89JudgeProvider()).to_dict()
        second = _run(Phase89JudgeProvider()).to_dict()
        self.assertEqual(first, second)
        keys = _recursive_keys(first)
        self.assertNotIn("total_score", keys)
        self.assertNotIn("total_points", keys)
        self.assertNotIn("stage", keys)
        self.assertNotIn("canonical_stage", keys)

    def test_fact_scope_and_complete_seven_component_roster_are_fail_closed(self) -> None:
        cross_target = (
            EvidenceFact(**{**_facts()[0].to_dict(), "target_id": "OTHER"}),
            _facts()[1],
        )
        with self.assertRaisesRegex(ValueError, "target/as_of mismatch"):
            _run(Phase89JudgeProvider(), facts=cross_target)
        result = _run(
            Phase89JudgeProvider(),
            component_results=_component_results()[:-1],
        )
        self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_PENDING")
        self.assertEqual(
            result.audit["critical_counts"][
                "missing_component_research_result_count"
            ],
            1,
        )
        rows = list(_component_results())
        rows[0] = ComponentResearchResult(
            component_id=rows[0].component_id,
            researcher_role=rows[1].researcher_role,
            status="COMPLETE",
            memo=rows[1].memo,
            pending_reasons=(),
            provider_name="PHASE89-MISMATCH-FIXTURE",
            prompt_hash="PHASE89-MISMATCH-PROMPT",
        )
        mismatch = _run(Phase89JudgeProvider(), component_results=tuple(rows))
        self.assertEqual(mismatch.status, "COMPONENT_SCORING_MEMOS_PENDING")
        self.assertIn(
            "COMPONENT_RESEARCH_MEMO_SCOPE_MISMATCH",
            mismatch.component_memos[0].pending_reasons,
        )

    def test_provider_receives_closed_required_output_contract(self) -> None:
        provider = Phase89JudgeProvider()
        _run(provider)
        self.assertEqual(
            set(provider.calls[0]["payload"]["required_judge_output_fields"]),
            set(JUDGE_RESPONSE_FIELDS),
        )


def _run(
    provider: Phase89JudgeProvider,
    *,
    component_results=None,
    facts=None,
    anchors=None,
):
    return LLMComponentScoringMemoEngine(
        analyst_provider=provider
    ).build(
        target_id=TARGET,
        archetype_id=ARCHETYPE,
        as_of_date=AS_OF_DATE,
        component_results=(
            _component_results() if component_results is None else component_results
        ),
        evidence_facts=_facts() if facts is None else facts,
        historical_anchors=_anchors() if anchors is None else anchors,
    )


def _facts() -> tuple[EvidenceFact, ...]:
    common = {
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "subject": "current target operating business",
        "business_segment": "core segment",
        "product_family": "core product",
        "unit": "flag",
        "period": "2026Q2",
        "source_independence_group": "ISSUER",
        "confidence": 0.85,
        "question_family_tags": (),
        "primitive_tags": (),
    }
    return (
        EvidenceFact(
            fact_id="PHASE89-FACT-SUPPORT",
            economic_mechanism="current operating strength converts into earnings and cash",
            predicate="current_operating_strength",
            value=True,
            direction="POSITIVE",
            source_ids=("PHASE89-SOURCE-SUPPORT",),
            claim_ids=("PHASE89-CLAIM-SUPPORT",),
            quote_ids=("PHASE89-QUOTE-SUPPORT",),
            current_lifecycle="CURRENT",
            **common,
        ),
        EvidenceFact(
            fact_id="PHASE89-FACT-COUNTER",
            economic_mechanism="customer concentration can reduce earnings durability",
            predicate="customer_concentration_risk",
            value=True,
            direction="COUNTER",
            source_ids=("PHASE89-SOURCE-COUNTER",),
            claim_ids=("PHASE89-CLAIM-COUNTER",),
            quote_ids=("PHASE89-QUOTE-COUNTER",),
            current_lifecycle="OPEN",
            **common,
        ),
    )


def _anchors() -> tuple[ComponentAnchor, ...]:
    rows = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        for role, suffix, fraction in (
            ("POSITIVE", "P", 0.65),
            ("COUNTER", "C", 0.35),
        ):
            rows.append(
                ComponentAnchor(
                    anchor_id=f"PHASE89-ANCHOR-{component_id}-{suffix}",
                    archetype_id=ARCHETYPE,
                    component_id=component_id,
                    economic_fact_patterns=(
                        "source-backed current economic pattern",
                    ),
                    role=role,
                    score_band="HIGH" if role == "POSITIVE" else "LOW",
                    points_lower=maximum * max(0.0, fraction - 0.1),
                    points_mid=maximum * fraction,
                    points_upper=maximum * min(1.0, fraction + 0.1),
                    max_points=maximum,
                    source_backed_case_ids=(
                        f"PHASE89-BLIND-CASE-{component_id}-{suffix}",
                    ),
                    source_proxy_guard_case_ids=(),
                    source_score_anchor_ids=(
                        f"PHASE89-SCORE-LINEAGE-{component_id}-{suffix}",
                    ),
                    confidence="MEDIUM",
                    usable_as_exact_anchor=False,
                    usable_as_ordinal_anchor=True,
                )
            )
    return tuple(rows)


def _component_results() -> tuple[ComponentResearchResult, ...]:
    rows = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        memo = ComponentResearchMemo(
            memo_id=f"PHASE89-RESEARCH-MEMO-{component_id}",
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            component_id=component_id,
            component_max_points=maximum,
            positive_fact_ids=("PHASE89-FACT-SUPPORT",),
            counter_fact_ids=("PHASE89-FACT-COUNTER",),
            resolution_fact_ids=(),
            structured_metrics={
                "current_economic_metric": 1.0,
                "concentration_metric": 0.4,
            },
            historical_anchor_ids=(
                f"PHASE89-ANCHOR-{component_id}-P",
                f"PHASE89-ANCHOR-{component_id}-C",
            ),
            researcher_summary="current facts were researched before independent judging",
            positive_case="current source-backed operating strength supports the component",
            counter_case="concentration and uncertainty limit the component ceiling",
            uncertainties=("duration remains to be confirmed",),
            source_coverage=("ISSUER_OFFICIAL", "INDEPENDENT_REPORT"),
            proposed_score_lower=maximum * 0.41,
            proposed_score_mid=maximum * 0.53,
            proposed_score_upper=maximum * 0.69,
            confidence=0.78,
            research_complete=True,
            nearest_positive_anchor_ids=(
                f"PHASE89-ANCHOR-{component_id}-P",
            ),
            nearest_counter_anchor_ids=(
                f"PHASE89-ANCHOR-{component_id}-C",
            ),
            why_not_higher="counterevidence remains",
            why_not_lower="current direct support exists",
            researcher_role=f"PHASE89-{component_id}-RESEARCHER",
        )
        rows.append(
            ComponentResearchResult(
                component_id=component_id,
                researcher_role=memo.researcher_role,
                status="COMPLETE",
                memo=memo,
                pending_reasons=(),
                provider_name="PHASE89-RESEARCH-FIXTURE",
                prompt_hash=f"PHASE89-RESEARCH-PROMPT-{component_id}",
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
