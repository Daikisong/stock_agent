from __future__ import annotations

from dataclasses import replace
import json
import unittest
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode import (
    AnalystJudge,
    CalibrationJudge,
    ComponentAnchor,
    ComponentResearchMemo,
    DeterministicScoreAggregator,
    EvidenceFact,
    SkepticJudge,
)
from e2r.research_brain.researcher_mode.capability_regression import (
    KNOWN_BAD_CASES,
    PHASE98_CASES,
    PHASE98_PASS,
    POSITIVE_CAPABILITY_CASES,
    compile_phase98_capability_regression_audit,
)


TARGET = "PHASE98-GENERIC-CURRENT-TARGET"
ARCHETYPE = "PHASE98-GENERIC-ARCHETYPE"
AS_OF_DATE = "2026-06-29"


class Phase98JudgeProvider:
    provider_name = "PHASE98-TEST-MODE-JUDGE"

    def complete(
        self,
        *,
        pass_name: str,
        payload: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        memo = payload["component_research_memo"]
        maximum = float(payload["component_max_points"])
        has_counter = bool(memo["counter_fact_ids"])
        fraction = (
            {
                "COMPONENT_ANALYST_JUDGE": 0.85,
                "COMPONENT_SKEPTIC_JUDGE": 0.72,
                "CALIBRATION_JUDGE": 0.83,
            }[pass_name]
            if has_counter
            else 0.82
        )
        return {
            "anchor_comparisons": [
                "source-backed current economics were compared with the blind ordinal anchor"
            ],
            "proposed_points": maximum * fraction,
            "allowed_range": [maximum * 0.55, maximum * 0.95],
            "rationale": (
                f"{pass_name} independently finds that material current evidence "
                "supports a reproducible component range"
            ),
            "disagreements": [],
            "support_fact_ids": list(memo["positive_fact_ids"]),
            "counter_fact_ids": list(memo["counter_fact_ids"]),
            "nearest_anchor_ids": list(memo["historical_anchor_ids"]),
            "why_not_higher": "the test keeps a bounded ceiling",
            "why_not_lower": "direct source-backed material economics establish the floor",
        }


class E2RV5Phase98PositiveCapabilityTests(unittest.TestCase):
    def test_hbm_sold_out_mix_and_record_profit_score_three_material_components(
        self,
    ) -> None:
        sold_out = _fact(
            "SOLD-OUT",
            mechanism="customer allocations lock current HBM capacity",
            predicate="hbm_capacity_sold_out",
            allowed=("earnings_visibility", "bottleneck_pricing"),
        )
        revenue_mix = _fact(
            "REVENUE-MIX",
            mechanism="higher HBM revenue mix expands earnings conversion",
            predicate="hbm_revenue_mix_expansion",
            value=42.0,
            unit="percent",
            allowed=("eps_fcf_explosion", "earnings_visibility"),
        )
        record_profit = _fact(
            "RECORD-PROFIT",
            mechanism="record operating profit validates earnings conversion",
            predicate="record_operating_profit",
            value=8_000.0,
            unit="KRW_bn",
            allowed=("eps_fcf_explosion",),
        )
        facts = (sold_out, revenue_mix, record_profit)

        eps = _score_component(
            "eps_fcf_explosion", facts, (revenue_mix.fact_id, record_profit.fact_id)
        )
        visibility = _score_component(
            "earnings_visibility", facts, (sold_out.fact_id, revenue_mix.fact_id)
        )
        bottleneck = _score_component(
            "bottleneck_pricing", facts, (sold_out.fact_id,)
        )

        for result in (eps, visibility, bottleneck):
            self.assertEqual(result.status, "COMPLETE")
            self.assertGreaterEqual(
                result.decision.final_points,
                result.decision.max_points * 0.75,
            )

    def test_official_asp_and_actual_profit_score_pricing_and_eps(self) -> None:
        asp = _fact(
            "OFFICIAL-ASP",
            mechanism="issuer-reported HBM ASP increase realizes pricing power",
            predicate="official_hbm_asp_change",
            value=18.0,
            unit="percent",
            allowed=("bottleneck_pricing",),
        )
        actual_profit = _fact(
            "ACTUAL-PROFIT",
            mechanism="filed actual operating profit converts demand into earnings",
            predicate="actual_operating_profit",
            value=7_500.0,
            unit="KRW_bn",
            allowed=("eps_fcf_explosion",),
        )

        pricing = _score_component(
            "bottleneck_pricing", (asp, actual_profit), (asp.fact_id,)
        )
        eps = _score_component(
            "eps_fcf_explosion", (asp, actual_profit), (actual_profit.fact_id,)
        )
        self.assertGreater(pricing.decision.final_points, 0)
        self.assertGreater(eps.decision.final_points, 0)
        self.assertEqual(pricing.decision.fact_ids, (asp.fact_id,))
        self.assertEqual(eps.decision.fact_ids, (actual_profit.fact_id,))

    def test_named_customer_order_scores_visibility_and_information_quality(
        self,
    ) -> None:
        order = _fact(
            "NAMED-CUSTOMER-ORDER",
            mechanism="named hyperscaler order locks issuer shipment visibility",
            predicate="named_customer_purchase_order",
            value="binding order",
            unit=None,
            allowed=("earnings_visibility", "information_confidence"),
        )
        visibility = _score_component(
            "earnings_visibility", (order,), (order.fact_id,)
        )
        information = _score_component(
            "information_confidence", (order,), (order.fact_id,)
        )
        self.assertGreater(visibility.decision.final_points, 0)
        self.assertGreater(information.decision.final_points, 0)
        self.assertIn(order.fact_id, visibility.decision.fact_ids)
        self.assertIn(order.fact_id, information.decision.fact_ids)

    def test_public_valuation_and_forward_eps_score_valuation(self) -> None:
        public_valuation = _fact(
            "PUBLIC-VALUATION",
            mechanism="public market price and share count establish current valuation",
            predicate="public_forward_pe",
            value=9.2,
            unit="multiple",
            allowed=("valuation_rerating",),
        )
        forward_eps = _fact(
            "FORWARD-EPS",
            mechanism="dated public consensus forward EPS supplies the valuation denominator",
            predicate="public_forward_eps",
            value=8_900.0,
            unit="KRW_per_share",
            allowed=("valuation_rerating",),
        )
        result = _score_component(
            "valuation_rerating",
            (public_valuation, forward_eps),
            (public_valuation.fact_id, forward_eps.fact_id),
            structured_metrics={"FORWARD_PE": 9.2, "FORWARD_EPS": 8_900.0},
        )
        self.assertGreater(result.decision.final_points, 0)
        self.assertEqual(
            set(result.decision.fact_ids),
            {public_valuation.fact_id, forward_eps.fact_id},
        )

    def test_upward_consensus_revision_scores_mispricing_and_visibility(self) -> None:
        revision = _fact(
            "UPWARD-REVISION",
            mechanism="point-in-time consensus EPS revision raises expected earnings path",
            predicate="consensus_eps_revision",
            value=14.0,
            unit="percent",
            allowed=("market_mispricing", "earnings_visibility"),
        )
        mispricing = _score_component(
            "market_mispricing", (revision,), (revision.fact_id,)
        )
        visibility = _score_component(
            "earnings_visibility", (revision,), (revision.fact_id,)
        )
        self.assertGreater(mispricing.decision.final_points, 0)
        self.assertGreater(visibility.decision.final_points, 0)

    def test_capacity_expansion_counter_reduces_net_bottleneck_score(self) -> None:
        scarcity = _fact(
            "CAPACITY-SCARCITY",
            mechanism="sold-out constrained capacity supports scarcity economics",
            predicate="capacity_scarcity",
            allowed=("bottleneck_pricing",),
        )
        expansion = _fact(
            "CAPACITY-EXPANSION",
            mechanism="issuer capacity expansion increases supply and can relax the bottleneck",
            predicate="issuer_capacity_expansion",
            value=35.0,
            unit="percent",
            direction="COUNTER",
            lifecycle="OPEN",
            allowed=("bottleneck_pricing",),
        )
        without_counter = _score_component(
            "bottleneck_pricing", (scarcity,), (scarcity.fact_id,)
        )
        with_counter = _score_component(
            "bottleneck_pricing",
            (scarcity, expansion),
            (scarcity.fact_id,),
            counter_fact_ids=(expansion.fact_id,),
        )
        self.assertEqual(without_counter.decision.counter_effect, 0)
        self.assertGreater(with_counter.decision.counter_effect, 0)
        self.assertLess(
            with_counter.decision.final_points,
            without_counter.decision.final_points,
        )

    def test_independent_corroboration_raises_confidence_not_points(self) -> None:
        base = _fact(
            "CORROBORATED-ECONOMIC-FACT",
            mechanism="binding allocation establishes forward shipment visibility",
            predicate="binding_allocation",
            allowed=("earnings_visibility",),
            confidence=0.72,
        )
        corroborated = replace(
            base,
            corroborating_independence_groups=("INDEPENDENT-RESEARCH",),
        )
        base_result = _score_component(
            "earnings_visibility", (base,), (base.fact_id,)
        )
        corroborated_result = _score_component(
            "earnings_visibility", (corroborated,), (corroborated.fact_id,)
        )
        self.assertEqual(
            base_result.decision.final_points,
            corroborated_result.decision.final_points,
        )
        self.assertGreater(
            corroborated_result.decision.confidence,
            base_result.decision.confidence,
        )


class E2RV5Phase98CapabilityRegressionAuditTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_phase98_registry_is_exact_and_every_detector_passes(self) -> None:
        audit = compile_phase98_capability_regression_audit()
        self.assertEqual(len(POSITIVE_CAPABILITY_CASES), 7)
        self.assertEqual(len(KNOWN_BAD_CASES), 20)
        self.assertEqual(len(PHASE98_CASES), 27)
        self.assertEqual(
            tuple(case.case_id for case in POSITIVE_CAPABILITY_CASES),
            tuple(f"POS-{index:02d}" for index in range(1, 8)),
        )
        self.assertEqual(
            tuple(case.case_id for case in KNOWN_BAD_CASES),
            tuple(f"BAD-{index:02d}" for index in range(1, 21)),
        )
        self.assertEqual(audit["status"], PHASE98_PASS)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(audit["test_mode_only"])
        self.assertFalse(audit["production_readiness_authority"])

    def test_committed_phase98_audit_is_reproducible(self) -> None:
        expected = compile_phase98_capability_regression_audit()
        actual = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_capability_known_bad_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)


def _score_component(
    component_id: str,
    evidence_facts: Sequence[EvidenceFact],
    positive_fact_ids: tuple[str, ...],
    *,
    counter_fact_ids: tuple[str, ...] = (),
    structured_metrics: Mapping[str, Any] | None = None,
):
    maximum = 15.0 if component_id in {"market_mispricing", "valuation_rerating"} else 20.0
    if component_id in {"capital_allocation", "information_confidence"}:
        maximum = 5.0
    anchor = ComponentAnchor(
        anchor_id=f"PHASE98-ANCHOR-{component_id}",
        archetype_id=ARCHETYPE,
        component_id=component_id,
        economic_fact_patterns=("blind material source-backed economic pattern",),
        role="POSITIVE",
        score_band="HIGH",
        points_lower=maximum * 0.60,
        points_mid=maximum * 0.80,
        points_upper=maximum * 0.95,
        max_points=maximum,
        source_backed_case_ids=(f"PHASE98-BLIND-CASE-{component_id}",),
        source_proxy_guard_case_ids=(),
        source_score_anchor_ids=(f"PHASE98-BLIND-SCORE-{component_id}",),
        confidence="MEDIUM",
        usable_as_exact_anchor=False,
        usable_as_ordinal_anchor=True,
    )
    memo = ComponentResearchMemo(
        memo_id=f"PHASE98-MEMO-{component_id}",
        target_id=TARGET,
        archetype_id=ARCHETYPE,
        component_id=component_id,
        component_max_points=maximum,
        positive_fact_ids=positive_fact_ids,
        counter_fact_ids=counter_fact_ids,
        resolution_fact_ids=(),
        structured_metrics=dict(structured_metrics or {}),
        historical_anchor_ids=(anchor.anchor_id,),
        researcher_summary="the test-mode researcher reviewed material facts and counterfacts",
        positive_case="direct current facts support material component economics",
        counter_case=(
            "the open supply response constrains the net score"
            if counter_fact_ids
            else "no open material counterfact was established in this bounded fixture"
        ),
        uncertainties=("duration remains a monitoring item",),
        source_coverage=("ISSUER_OFFICIAL", "INDEPENDENT_PUBLIC"),
        proposed_score_lower=maximum * 0.55,
        proposed_score_mid=maximum * 0.82,
        proposed_score_upper=maximum * 0.95,
        confidence=0.82,
        research_complete=True,
        nearest_positive_anchor_ids=(anchor.anchor_id,),
        nearest_counter_anchor_ids=(),
        why_not_higher="the bounded fixture does not prove an absolute ceiling",
        why_not_lower="source-backed material economics establish a high floor",
        researcher_role=f"PHASE98-{component_id}-RESEARCHER",
    )
    provider = Phase98JudgeProvider()
    judge_results = (
        AnalystJudge(provider=provider).judge(
            memo=memo,
            evidence_facts=evidence_facts,
            historical_anchors=(anchor,),
        ),
        SkepticJudge(provider=provider).judge(
            memo=memo,
            evidence_facts=evidence_facts,
            historical_anchors=(anchor,),
        ),
        CalibrationJudge(provider=provider).judge(
            memo=memo,
            evidence_facts=evidence_facts,
            historical_anchors=(anchor,),
        ),
    )
    for row in judge_results:
        if row.status != "COMPLETE" or row.decision is None:
            raise AssertionError(row.pending_reasons)
    result = DeterministicScoreAggregator().aggregate_component(
        memo=memo,
        judge_decisions=tuple(row.decision for row in judge_results if row.decision),
        evidence_facts=evidence_facts,
        historical_anchors=(anchor,),
        expected_as_of_date=AS_OF_DATE,
    )
    if result.status != "COMPLETE" or result.decision is None:
        raise AssertionError(
            {
                "pending_reasons": result.pending_reasons,
                "proposal_reasons": [
                    row.reason_codes for row in result.proposal_validations
                ],
            }
        )
    return result


def _fact(
    suffix: str,
    *,
    mechanism: str,
    predicate: str,
    allowed: tuple[str, ...],
    value: Any = True,
    unit: str | None = "flag",
    direction: str = "POSITIVE",
    lifecycle: str = "CURRENT",
    confidence: float = 0.90,
) -> EvidenceFact:
    return EvidenceFact(
        fact_id=f"PHASE98-FACT-{suffix}",
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        subject="current target operating business",
        business_segment="current relevant segment",
        product_family="current relevant product",
        economic_mechanism=mechanism,
        predicate=predicate,
        value=value,
        unit=unit,
        period="2026Q2",
        direction=direction,
        source_ids=(f"PHASE98-SOURCE-{suffix}",),
        claim_ids=(f"PHASE98-CLAIM-{suffix}",),
        quote_ids=(f"PHASE98-QUOTE-{suffix}",),
        current_lifecycle=lifecycle,
        source_independence_group="ISSUER-OFFICIAL",
        corroborating_independence_groups=(),
        confidence=confidence,
        allowed_component_ids=allowed,
    )


if __name__ == "__main__":
    unittest.main()
