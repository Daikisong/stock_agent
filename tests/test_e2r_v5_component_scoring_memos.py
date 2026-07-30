from __future__ import annotations

from dataclasses import replace
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator

from e2r.research_brain.planning.provider_transport import (
    StructuredProviderResponse,
)
from e2r.research_brain.researcher_mode import (
    AnalystJudge,
    CANONICAL_COMPONENT_MAX_POINTS,
    CANONICAL_COMPONENT_ORDER,
    COMPONENT_SCORING_MEMO_OUTPUT_FILES,
    JUDGE_RESPONSE_FIELDS,
    PHASE89_PASS,
    REQUIRED_COMPONENT_JUDGE_ROLES,
    CalibrationJudge,
    CodexResearcherProvider,
    ComponentAnchor,
    ComponentResearchMemo,
    ComponentResearchResult,
    EvidenceFact,
    LLMComponentScoringMemoEngine,
    SkepticJudge,
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
            self.mode == "HONOR_EMPTY_SUPPORT_RULE"
            and not payload["allowed_support_fact_ids"]
        ):
            empty_rule = payload["conditional_judge_rules"]["empty_support_plane"]
            response["proposed_points"] = empty_rule["required_proposed_points"]
            response["allowed_range"] = list(
                empty_rule["required_allowed_range"]
            )
            response["support_fact_ids"] = list(
                empty_rule["required_support_fact_ids"]
            )
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

    def test_large_three_role_judge_projection_stays_below_transport_gate(
        self,
    ) -> None:
        class LargeRosterTransport:
            def __init__(self) -> None:
                self.prompts: list[str] = []
                self.payloads: list[Mapping[str, Any]] = []
                self.output_schemas: list[Mapping[str, Any]] = []

            def provider_identity(self) -> Mapping[str, Any]:
                return {
                    "transport_class": "LargeRosterTransport",
                    "model": "judge-projection-regression",
                }

            def complete(
                self,
                *,
                prompt: str,
                output_schema: Mapping[str, Any],
                schema_name: str,
            ) -> StructuredProviderResponse:
                del schema_name
                payload = json.loads(prompt.rsplit("\n", 1)[-1])
                self.prompts.append(prompt)
                self.payloads.append(payload)
                self.output_schemas.append(output_schema)
                maximum = float(payload["component_max_points"])
                response = {
                    "anchor_comparisons": [
                        "the current fact shape fits the blind ordinal band"
                    ],
                    "proposed_points": maximum * 0.5,
                    "allowed_range": [maximum * 0.4, maximum * 0.6],
                    "rationale": (
                        "every decoded support, counter, and resolution row "
                        "was reviewed"
                    ),
                    "disagreements": [],
                    "support_fact_ids": list(
                        payload["allowed_support_fact_ids"]
                    ),
                    "counter_fact_ids": list(
                        payload["allowed_counter_fact_ids"]
                    ),
                    "nearest_anchor_ids": list(
                        payload["allowed_nearest_anchor_ids"][:1]
                    ),
                    "why_not_higher": "counter rows bound the upper range",
                    "why_not_lower": "support rows establish the lower range",
                }
                Draft202012Validator(output_schema).validate(response)
                return StructuredProviderResponse(
                    payload=response,
                    raw_response=json.dumps(response, ensure_ascii=False),
                    stderr="",
                    returncode=0,
                )

        facts = _large_judge_facts()
        memo = _large_judge_memo(facts)
        transport = LargeRosterTransport()
        provider = CodexResearcherProvider(
            transport=transport  # type: ignore[arg-type]
        )
        judges = (
            AnalystJudge(provider=provider),
            SkepticJudge(provider=provider),
            CalibrationJudge(provider=provider),
        )

        results = tuple(
            judge.judge(
                memo=memo,
                evidence_facts=facts,
                historical_anchors=_anchors(),
            )
            for judge in judges
        )

        expected_fact_ids = {
            *memo.positive_fact_ids,
            *memo.counter_fact_ids,
            *memo.resolution_fact_ids,
        }
        expected_facts_by_id = {
            row.fact_id: row.to_dict() for row in facts
        }
        self.assertEqual(len(expected_fact_ids), 807)
        self.assertGreater(
            len(
                json.dumps(
                    list(expected_facts_by_id.values()),
                    ensure_ascii=False,
                    sort_keys=True,
                )
            ),
            1_000_000,
        )
        self.assertTrue(all(row.status == "COMPLETE" for row in results))
        self.assertEqual(len(transport.prompts), 3)
        self.assertTrue(
            all(len(prompt) < 1_000_000 for prompt in transport.prompts)
        )
        self.assertTrue(
            all(
                "decode every evidence_fact_projection.facts row"
                in prompt.lower()
                for prompt in transport.prompts
            )
        )
        for payload in transport.payloads:
            self.assertNotIn("evidence_facts", payload)
            projection = payload["evidence_fact_projection"]
            self.assertEqual(projection["fact_count"], 807)
            self.assertTrue(projection["every_fact_id_preserved"])
            self.assertTrue(
                projection[
                    "every_fact_lineage_accounted_by_count_and_hash"
                ]
            )
            self.assertFalse(projection["fixed_top_n_used"])
            self.assertFalse(projection["prompt_projection_is_research_cap"])
            decoded_rows = [
                dict(zip(projection["fact_fields"], row))
                for row in projection["facts"]
            ]
            decoded_fact_ids = [row["fact_id"] for row in decoded_rows]
            self.assertEqual(len(decoded_fact_ids), len(expected_fact_ids))
            self.assertEqual(len(decoded_fact_ids), len(set(decoded_fact_ids)))
            self.assertEqual(set(decoded_fact_ids), expected_fact_ids)
            for decoded in decoded_rows:
                source = expected_facts_by_id[decoded["fact_id"]]
                for field in (
                    "subject",
                    "business_segment",
                    "product_family",
                    "economic_mechanism",
                    "predicate",
                    "value",
                    "unit",
                    "period",
                    "direction",
                    "current_lifecycle",
                    "confidence",
                    "structured_evidence_roles",
                ):
                    self.assertEqual(decoded[field], source[field])
                self.assertEqual(
                    projection["source_independence_group_dictionary"][
                        decoded["source_independence_group_index"]
                    ],
                    source["source_independence_group"],
                )
            self.assertFalse(
                {
                    "stage",
                    "total_score",
                    "future_outcome",
                }
                & _recursive_keys(payload)
            )
        for result in results:
            decision = result.decision
            self.assertIsNotNone(decision)
            assert decision is not None
            self.assertEqual(
                set(decision.support_fact_ids),
                set(memo.positive_fact_ids),
            )
            self.assertEqual(
                set(decision.counter_fact_ids),
                set(memo.counter_fact_ids),
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
        payload = provider.calls[0]["payload"]
        self.assertEqual(
            payload["allowed_support_fact_ids"],
            payload["component_research_memo"]["positive_fact_ids"],
        )
        self.assertEqual(
            payload["conditional_judge_rules"]["empty_support_plane"],
            {
                "condition": "allowed_support_fact_ids is empty",
                "required_proposed_points": 0,
                "required_allowed_range": [0, 0],
                "required_support_fact_ids": [],
            },
        )

    def test_empty_support_plane_explicitly_requires_zero_score_contract(self) -> None:
        rows = list(_component_results())
        first = rows[0]
        rows[0] = replace(
            first,
            memo=replace(first.memo, positive_fact_ids=()),
        )
        provider = Phase89JudgeProvider("HONOR_EMPTY_SUPPORT_RULE")

        result = _run(provider, component_results=tuple(rows))

        self.assertEqual(result.status, "COMPONENT_SCORING_MEMOS_COMPLETE")
        first_decisions = [
            row
            for row in result.judge_decisions
            if row.component_id == CANONICAL_COMPONENT_ORDER[0]
        ]
        self.assertEqual(len(first_decisions), 3)
        self.assertTrue(
            all(row.proposed_points == 0 for row in first_decisions)
        )
        self.assertTrue(
            all(row.allowed_range == (0.0, 0.0) for row in first_decisions)
        )
        self.assertTrue(
            all(not row.support_fact_ids for row in first_decisions)
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


def _large_judge_facts() -> tuple[EvidenceFact, ...]:
    shared_source_ids = tuple(
        f"LARGE-SHARED-SOURCE-{index:02d}" for index in range(24)
    )
    shared_claim_ids = tuple(
        f"LARGE-SHARED-CLAIM-{index:02d}" for index in range(24)
    )
    shared_quote_ids = tuple(
        f"LARGE-SHARED-QUOTE-{index:02d}" for index in range(24)
    )
    component_id = CANONICAL_COMPONENT_ORDER[0]
    rows = []
    for index in range(807):
        if index < 400:
            direction = "POSITIVE"
            lifecycle = "CURRENT"
            prefix = "POSITIVE"
        elif index < 800:
            direction = "COUNTER"
            lifecycle = "OPEN"
            prefix = "COUNTER"
        else:
            direction = "RESOLUTION"
            lifecycle = "RESOLVED"
            prefix = "RESOLUTION"
        rows.append(
            EvidenceFact(
                fact_id=f"LARGE-{prefix}-FACT-{index:04d}",
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                subject=f"current target operating observation {index}",
                business_segment=f"segment {index % 5}",
                product_family=f"product family {index % 11}",
                economic_mechanism=(
                    f"distinct economic mechanism {index} links operating "
                    "conditions to component cash economics"
                ),
                predicate=f"LARGE_PREDICATE_{index:04d}",
                value={"observation": index, "confirmed": True},
                unit="index",
                period=f"2026Q{index % 4 + 1}",
                direction=direction,
                source_ids=shared_source_ids,
                claim_ids=shared_claim_ids,
                quote_ids=shared_quote_ids,
                current_lifecycle=lifecycle,
                source_independence_group="ISSUER:CURRENT_TARGET",
                confidence=0.85,
                corroborating_independence_groups=(
                    "ISSUER:CURRENT_TARGET",
                    "INDEPENDENT:CURRENT_TARGET",
                ),
                question_family_tags=(f"QUESTION-{index % 17}",),
                primitive_tags=(f"PRIMITIVE-{index % 13}",),
                allowed_component_ids=(component_id,),
                structured_evidence_roles=("FORWARD_GUIDANCE",),
            )
        )
    return tuple(rows)


def _large_judge_memo(
    facts: tuple[EvidenceFact, ...],
) -> ComponentResearchMemo:
    base = _component_results()[0].memo
    assert base is not None
    return replace(
        base,
        memo_id="PHASE89-LARGE-JUDGE-RESEARCH-MEMO",
        positive_fact_ids=tuple(
            row.fact_id for row in facts if row.direction == "POSITIVE"
        ),
        counter_fact_ids=tuple(
            row.fact_id for row in facts if row.direction == "COUNTER"
        ),
        resolution_fact_ids=tuple(
            row.fact_id for row in facts if row.direction == "RESOLUTION"
        ),
        structured_metrics={
            "current_economic_metric": 1.0,
            "stage": "must be scrubbed before provider transport",
        },
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
