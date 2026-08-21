from __future__ import annotations

import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from typing import Any, Mapping

from e2r.research_brain.researcher_mode import (
    CANONICAL_COMPONENT_ORDER,
    FrozenHistoricalBlindResearchProvider,
    HistoricalBlindReplayCase,
    HistoricalBlindReplayObservation,
    HistoricalBlindResearchInput,
    HistoricalReplayEvaluationTarget,
    LeaveOneOutMemoryAudit,
    PHASE91_PASS,
    PHASE91_THRESHOLDS,
    blind_payload_leakage_paths,
    build_historical_blind_replay_case,
    canonical_historical_stage_band,
    compile_phase91_historical_blind_replay_audit,
    evaluate_historical_blind_replay,
    run_historical_blind_replay,
    write_phase91_historical_blind_replay_audit,
)


class E2RV5HistoricalBlindReplayTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.recompiled_audit = compile_phase91_historical_blind_replay_audit(
            cls.ROOT
        )
        cls.committed_audit = json.loads(
            (
                cls.ROOT
                / "docs/operational/e2r_v5_historical_blind_replay.json"
            ).read_text(encoding="utf-8")
        )
        cls.raw_replay_inputs_available = not bool(
            cls.recompiled_audit.get("missing_files")
        )
        # The clean repository intentionally excludes two output/** replay
        # inputs.  In that checkout, tests below inspect the committed receipt
        # while the compiler result must fail closed and name both omissions.
        cls.audit = (
            cls.recompiled_audit
            if cls.raw_replay_inputs_available
            else cls.committed_audit
        )

    def test_phase91_audit_is_reproducible_and_passes_every_threshold(self) -> None:
        if self.raw_replay_inputs_available:
            self.assertEqual(self.recompiled_audit, self.committed_audit)
        else:
            missing = self.recompiled_audit["missing_files"]
            self.assertEqual(
                self.recompiled_audit["status"],
                "V5_PHASE91_HISTORICAL_BLIND_RESEARCHER_PARITY_FAIL",
            )
            self.assertEqual(
                self.recompiled_audit["critical_count_sum"],
                len(missing),
            )
            self.assertEqual(
                set(missing),
                {
                    "output/historical_replay/source_backed_v1/"
                    "historical_source_backed_replay.jsonl",
                    "output/historical_replay/source_backed_v1/"
                    "historical_source_backed_manifest.json",
                },
            )
            self.assertTrue(
                all(not (self.ROOT / path).exists() for path in missing)
            )

        # This validates the tracked historical receipt.  It is not a claim
        # that omitted output/** inputs were rebuilt in a clean clone.
        self.assertEqual(self.committed_audit["status"], PHASE91_PASS)
        self.assertEqual(self.committed_audit["critical_count_sum"], 0)
        metrics = self.committed_audit["metric_values"]
        self.assertLessEqual(
            metrics["component_normalized_mae"],
            PHASE91_THRESHOLDS["component_normalized_mae_max"],
        )
        self.assertLessEqual(
            metrics["total_proxy_mae"],
            PHASE91_THRESHOLDS["total_proxy_mae_max"],
        )
        self.assertGreaterEqual(
            metrics["spearman_rank_correlation"],
            PHASE91_THRESHOLDS["spearman_rank_correlation_min"],
        )
        self.assertGreaterEqual(
            metrics["stage_band_accuracy"],
            PHASE91_THRESHOLDS["stage_band_accuracy_min"],
        )

    def test_target_case_is_removed_from_every_memory_layer(self) -> None:
        case = self._actual_case("HBR-001", "HJDG-fb4a0b4ba531cb52e178f25b")
        audit = case.memory_audit
        self.assertEqual(audit.target_presence_count, 0)
        self.assertTrue(audit.excluded_source_row_ids)
        self.assertTrue(audit.excluded_score_source_row_ids)
        self.assertTrue(audit.excluded_fact_signature_ids)
        self.assertTrue(audit.excluded_score_anchor_ids)
        self.assertTrue(audit.excluded_component_anchor_ids)
        payload_text = json.dumps(
            case.research_input.to_provider_payload(),
            ensure_ascii=False,
            sort_keys=True,
        )
        self.assertNotIn(case.evaluator_target.judgment_id, payload_text)
        self.assertNotIn(case.evaluator_target.research_case_id, payload_text)

    def test_provider_receives_no_historical_score_stage_or_outcome(self) -> None:
        case = self._actual_case("HBR-001", "HJDG-fb4a0b4ba531cb52e178f25b")
        observation_row = self._observation_row("HBR-001")
        provider = FrozenHistoricalBlindResearchProvider((observation_row,))
        observations = run_historical_blind_replay(
            cases=(case,),
            provider=provider,
            observation_origin="TEST_FROZEN_BLIND_RESPONSE",
        )
        self.assertEqual(len(observations), 1)
        self.assertEqual(len(provider.calls), 1)
        payload = provider.calls[0]["payload"]
        self.assertEqual(blind_payload_leakage_paths(payload), ())
        serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        self.assertNotIn("normalized_component_vector", serialized)
        self.assertNotIn("reported_total_proxy", serialized)
        self.assertNotIn("reported_stage", serialized)
        self.assertNotIn("future_outcome_ref", serialized)

    def test_future_source_is_rejected_at_blind_input_boundary(self) -> None:
        maxima = _maxima()
        anchors = _safe_anchors()
        with self.assertRaisesRegex(ValueError, "future source"):
            HistoricalBlindResearchInput(
                blind_case_id="FUTURE-CASE",
                target_id="TARGET",
                archetype_id="C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                as_of_date="2023-07-27",
                source_facts=(
                    {
                        "fact_id": "FACT-FUTURE",
                        "economic_fact": "future report",
                        "source_text": "published one day too late",
                        "source_reference_ids": ["SOURCE-FUTURE"],
                        "available_date": "2023-07-28",
                    },
                ),
                component_max_points=maxima,
                historical_anchors=anchors,
                historical_memory_hash=_stable_hash(anchors),
            )

    def test_answer_key_field_is_rejected_even_when_nested_in_source_fact(self) -> None:
        maxima = _maxima()
        anchors = _safe_anchors()
        with self.assertRaisesRegex(ValueError, "evaluator data"):
            HistoricalBlindResearchInput(
                blind_case_id="LEAK-CASE",
                target_id="TARGET",
                archetype_id="C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                as_of_date="2024-01-01",
                source_facts=(
                    {
                        "fact_id": "FACT-LEAK",
                        "economic_fact": "order backlog",
                        "source_text": "source-backed evidence",
                        "source_reference_ids": ["SOURCE-LEAK"],
                        "available_date": "2024-01-01",
                        "reported_stage": "3-Green",
                    },
                ),
                component_max_points=maxima,
                historical_anchors=anchors,
                historical_memory_hash=_stable_hash(anchors),
            )

    def test_partial_historical_vector_is_not_used_as_total_proxy(self) -> None:
        case = self._actual_case("HBR-013", "HJDG-380865d3e21c5a353dfc262e")
        self.assertEqual(len(case.evaluator_target.historical_component_vector), 2)
        self.assertIsNone(case.evaluator_target.historical_total_proxy)
        full_count = self.audit["metrics"]["total_proxy_comparison_count"]
        component_count = self.audit["metrics"]["component_comparison_count"]
        self.assertEqual(full_count, 12)
        self.assertEqual(component_count, 92)

    def test_canonical_historical_stage_mapping_preserves_e2r_enum(self) -> None:
        examples = {
            "Stage2-Actionable": "2",
            "Stage3-Green": "3-Green",
            "Stage3-Yellow": "3-Yellow",
            "Stage3-Red": "3-Red",
            "Stage4B-Watch": "4B",
            "4C": "4C",
        }
        for historical, expected in examples.items():
            with self.subTest(historical=historical):
                value, gap = canonical_historical_stage_band(historical)
                self.assertEqual(value, expected)
                self.assertIsNone(gap)
        value, gap = canonical_historical_stage_band("narrative label only")
        self.assertIsNone(value)
        self.assertEqual(gap, "HISTORICAL_STAGE_LABEL_NOT_CANONICALIZABLE")

    def test_dynamic_range_audit_fails_when_high_mid_low_all_collapse_to_twenty(self) -> None:
        cases = (
            _synthetic_case("DYN-HIGH", 80.0),
            _synthetic_case("DYN-MID", 50.0),
            _synthetic_case("DYN-LOW", 10.0),
        )
        provider = FrozenHistoricalBlindResearchProvider(
            (
                _synthetic_observation("DYN-HIGH", 20.0),
                _synthetic_observation("DYN-MID", 15.0),
                _synthetic_observation("DYN-LOW", 10.0),
            )
        )
        observations = run_historical_blind_replay(
            cases=cases,
            provider=provider,
            observation_origin="TEST_DYNAMIC_COLLAPSE",
        )
        report = evaluate_historical_blind_replay(
            cases=cases,
            observations=observations,
        )
        self.assertTrue(report["dynamic_range_audit"]["collapsed_to_zero_twenty"])
        self.assertEqual(
            report["critical_counts"]["score_dynamic_range_collapse_count"],
            1,
        )
        self.assertEqual(report["status"], "HISTORICAL_BLIND_REPLAY_METRICS_FAIL")

    def test_dynamic_range_canary_contains_historical_high_mid_and_low(self) -> None:
        dynamic = self.audit["metrics"]["dynamic_range_audit"]
        self.assertEqual(dynamic["historical_group_count"], 3)
        self.assertTrue(all(dynamic["group_counts"].values()))
        self.assertFalse(dynamic["collapsed_to_zero_twenty"])
        self.assertGreater(dynamic["reconstructed_total_max"], 20.0)

    def test_critical_positive_counter_ordering_and_guards_are_perfect(self) -> None:
        guard = self.audit["source_backed_guard_audit"]
        self.assertEqual(guard["critical_ordering_pair_count"], 6)
        self.assertEqual(guard["critical_positive_counter_ordering"], 1.0)
        self.assertEqual(guard["false_positive_guard_count"], 7)
        self.assertEqual(guard["false_positive_guard_accuracy"], 1.0)
        self.assertTrue(all(row["ordering_correct"] for row in guard["ordering_rows"]))
        self.assertEqual(guard["current_score_credit_count"], 0)
        self.assertEqual(guard["future_leakage_count"], 0)

    def test_every_registry_archetype_has_holdout_or_exact_source_gap(self) -> None:
        rows = self.audit["registry_archetype_coverage"]
        self.assertEqual(len(rows), 36)
        self.assertEqual(
            {row["coverage_status"] for row in rows},
            {"SOURCE_BACKED_HOLDOUT", "EXACT_SOURCE_GAP"},
        )
        gaps = {
            row["archetype_id"]: row["exact_source_gap_reason"]
            for row in rows
            if row["coverage_status"] == "EXACT_SOURCE_GAP"
        }
        self.assertEqual(
            set(gaps),
            {
                "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
                "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
            },
        )
        self.assertTrue(all(gaps.values()))
        self.assertTrue(all(row["source_proxy_holdout_count"] == 0 for row in rows))

    def test_c06_six_mandatory_families_have_holdout_or_exact_gap(self) -> None:
        rows = self.audit["c06_mandatory_coverage"]
        self.assertEqual(len(rows), 6)
        by_id = {row["anchor_family_id"]: row for row in rows}
        self.assertEqual(
            by_id["C06_REOPEN_CUSTOMER_DEPENDENCY"]["coverage_status"],
            "EXACT_SOURCE_GAP",
        )
        self.assertTrue(
            by_id["C06_REOPEN_CUSTOMER_DEPENDENCY"]["exact_source_gap_reason"]
        )
        for family_id, row in by_id.items():
            with self.subTest(family_id=family_id):
                self.assertIn(
                    row["coverage_status"],
                    {"SOURCE_BACKED_HOLDOUT", "EXACT_SOURCE_GAP"},
                )
                self.assertFalse(row["company_name_conditioned"])
                self.assertFalse(row["target_symbol_conditioned"])

    def test_observation_has_seven_decisions_and_twenty_one_judges(self) -> None:
        for row in self.audit["observations"]:
            with self.subTest(blind_case_id=row["blind_case_id"]):
                self.assertEqual(
                    set(row["component_points"]), set(CANONICAL_COMPONENT_ORDER)
                )
                self.assertEqual(
                    set(row["component_decision_ids"]),
                    set(CANONICAL_COMPONENT_ORDER),
                )
                self.assertEqual(len(row["judge_ids"]), 21)
                self.assertEqual(len(row["prompt_hashes"]), 21)
                self.assertFalse(row["production_stage_authority"])

    def test_real_score_aggregation_adapter_requires_complete_non_stage_run(self) -> None:
        case = self._actual_case("HBR-001", "HJDG-fb4a0b4ba531cb52e178f25b")
        incomplete = SimpleNamespace(
            target_id=case.research_input.target_id,
            archetype_id=case.research_input.archetype_id,
            as_of_date=case.research_input.as_of_date,
            status="DETERMINISTIC_SCORE_RESEARCH_REQUIRED",
            score_valid=False,
            production_stage_authority=False,
        )
        with self.assertRaisesRegex(ValueError, "complete non-Stage"):
            HistoricalBlindReplayObservation.from_score_aggregation_run(
                research_input=case.research_input,
                run=incomplete,
                predicted_stage_band="2",
                provider_name="TEST",
            )

    def test_complete_phase90_run_adapts_without_copying_a_stage_decision(self) -> None:
        case = self._actual_case("HBR-001", "HJDG-fb4a0b4ba531cb52e178f25b")
        maxima = case.research_input.component_max_points
        component_points = {
            component_id: float(maxima[component_id]) * 0.6
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        judge_ids = tuple(
            f"JUDGE-{component_id}-{role}"
            for component_id in CANONICAL_COMPONENT_ORDER
            for role in ("ANALYST", "SKEPTIC", "CALIBRATION")
        )
        prompt_hashes = tuple(
            hashlib.sha256(value.encode("utf-8")).hexdigest()
            for value in judge_ids
        )
        score = SimpleNamespace(
            component_points=component_points,
            component_max_points=dict(maxima),
            total_points=sum(component_points.values()),
            component_decision_ids={
                component_id: f"DECISION-{component_id}"
                for component_id in CANONICAL_COMPONENT_ORDER
            },
            fact_ids=("FACT-A",),
            counter_fact_ids=("FACT-B",),
            anchor_ids=("ANCHOR-A",),
            judge_ids=judge_ids,
            prompt_hashes=prompt_hashes,
        )
        run = SimpleNamespace(
            target_id=case.research_input.target_id,
            archetype_id=case.research_input.archetype_id,
            as_of_date=case.research_input.as_of_date,
            status="DETERMINISTIC_SCORE_COMPLETE",
            score_valid=True,
            production_stage_authority=False,
            total_result=SimpleNamespace(score=score),
            to_dict=lambda: {
                "status": "DETERMINISTIC_SCORE_COMPLETE",
                "component_points": component_points,
            },
        )
        observation = HistoricalBlindReplayObservation.from_score_aggregation_run(
            research_input=case.research_input,
            run=run,
            predicted_stage_band="2",
            provider_name="ACTUAL-TEST-PROVIDER",
        )
        self.assertEqual(
            observation.observation_origin,
            "ACTUAL_RESEARCHER_MODE_SCORE_AGGREGATION_RUN",
        )
        self.assertAlmostEqual(observation.total_points, 60.0)
        self.assertFalse(observation.production_stage_authority)
        self.assertEqual(len(observation.judge_ids), 21)

    def test_observation_registry_never_contains_evaluator_target_identifiers(self) -> None:
        observations = json.loads(
            (
                self.ROOT
                / "configs/e2r_v5_historical_blind_replay_observations_v1.json"
            ).read_text(encoding="utf-8")
        )["observations"]
        targets = json.loads(
            (
                self.ROOT
                / "configs/e2r_v5_historical_blind_replay_targets_v1.json"
            ).read_text(encoding="utf-8")
        )["targets"]
        observation_text = json.dumps(observations, sort_keys=True)
        self.assertEqual(blind_payload_leakage_paths(observations), ())
        for target in targets:
            self.assertNotIn(target["judgment_id"], observation_text)

    def test_writer_emits_same_leaf_backed_audit(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = write_phase91_historical_blind_replay_audit(
                repo_root=self.ROOT,
                output_path=Path(tmpdir) / "phase91.json",
            )
            written = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(written, self.recompiled_audit)

    def _actual_case(
        self, blind_case_id: str, judgment_id: str
    ) -> HistoricalBlindReplayCase:
        judgments = _read_jsonl(
            self.ROOT
            / "output/researcher_parity/judgment_atlas/historical_judgments.jsonl"
        )
        fact_signatures = _read_jsonl(
            self.ROOT
            / "output/researcher_parity/judgment_atlas/fact_signatures.jsonl"
        )
        score_anchors = _read_jsonl(
            self.ROOT
            / "output/researcher_parity/judgment_atlas/score_anchors.jsonl"
        )
        component_atlas = json.loads(
            (
                self.ROOT / "docs/operational/e2r_v5_component_anchor_atlas.json"
            ).read_text(encoding="utf-8")
        )
        target = next(row for row in judgments if row["judgment_id"] == judgment_id)
        return build_historical_blind_replay_case(
            blind_case_id=blind_case_id,
            target_judgment=target,
            judgments=judgments,
            fact_signatures=fact_signatures,
            score_anchors=score_anchors,
            component_anchors=tuple(component_atlas["component_anchors"]),
        )

    def _observation_row(self, blind_case_id: str) -> Mapping[str, Any]:
        rows = json.loads(
            (
                self.ROOT
                / "configs/e2r_v5_historical_blind_replay_observations_v1.json"
            ).read_text(encoding="utf-8")
        )["observations"]
        return next(row for row in rows if row["blind_case_id"] == blind_case_id)


def _maxima() -> Mapping[str, float]:
    return {
        "eps_fcf_explosion": 20.0,
        "earnings_visibility": 20.0,
        "bottleneck_pricing": 20.0,
        "market_mispricing": 15.0,
        "valuation_rerating": 15.0,
        "capital_allocation": 5.0,
        "information_confidence": 5.0,
    }


def _safe_anchors() -> tuple[Mapping[str, Any], ...]:
    maxima = _maxima()
    return tuple(
        {
            "anchor_id": f"ANCHOR-{component_id}",
            "archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
            "component_id": component_id,
            "economic_fact_patterns": ["blind source-backed pattern"],
            "role": "POSITIVE",
            "score_band": "MEDIUM",
            "points_lower": maximum * 0.4,
            "points_mid": maximum * 0.5,
            "points_upper": maximum * 0.6,
            "max_points": maximum,
            "confidence": "MEDIUM",
            "usable_as_exact_anchor": False,
            "usable_as_ordinal_anchor": True,
        }
        for component_id, maximum in maxima.items()
    )


def _synthetic_case(blind_case_id: str, historical_total: float) -> HistoricalBlindReplayCase:
    maxima = _maxima()
    anchors = _safe_anchors()
    fraction = historical_total / 100.0
    vector = {
        component_id: maximum * fraction
        for component_id, maximum in maxima.items()
    }
    research_input = HistoricalBlindResearchInput(
        blind_case_id=blind_case_id,
        target_id=f"TARGET-{blind_case_id}",
        archetype_id="C01_ORDER_BACKLOG_MARGIN_BRIDGE",
        as_of_date="2024-01-01",
        source_facts=(
            {
                "fact_id": f"FACT-{blind_case_id}",
                "economic_fact": "order backlog and margin bridge",
                "source_text": "source-backed as-of evidence",
                "source_reference_ids": [f"SOURCE-{blind_case_id}"],
                "available_date": "2024-01-01",
            },
        ),
        component_max_points=maxima,
        historical_anchors=anchors,
        historical_memory_hash=_stable_hash(anchors),
    )
    target = HistoricalReplayEvaluationTarget(
        blind_case_id=blind_case_id,
        judgment_id=f"JUDGMENT-{blind_case_id}",
        research_case_id=f"CASE-{blind_case_id}",
        archetype_id="C01_ORDER_BACKLOG_MARGIN_BRIDGE",
        as_of_date="2024-01-01",
        source_quality="SOURCE_BACKED_HIGH",
        historical_component_vector=vector,
        component_max_points=maxima,
        historical_total_proxy=historical_total,
        historical_stage_band="2",
        stage_gap_reason=None,
        future_outcome_present=True,
        usable_as_exact_anchor=True,
    )
    memory = LeaveOneOutMemoryAudit(
        blind_case_id=blind_case_id,
        target_judgment_id=target.judgment_id,
        target_research_case_id=target.research_case_id,
        excluded_source_row_ids=(f"SOURCE-ROW-{blind_case_id}",),
        excluded_score_source_row_ids=(f"SCORE-ROW-{blind_case_id}",),
        excluded_fact_signature_ids=(f"HFACT-{blind_case_id}",),
        excluded_score_anchor_ids=(f"HANCH-{blind_case_id}",),
        excluded_component_anchor_ids=(f"CANCH-{blind_case_id}",),
        input_counts={
            "judgments": 2,
            "fact_signatures": 2,
            "score_anchors": 2,
            "component_anchors": 8,
        },
        retained_counts={
            "judgments": 1,
            "fact_signatures": 1,
            "score_anchors": 1,
            "component_anchors": 7,
            "safe_anchors": 7,
        },
        target_presence_after_filter={
            "judgments": 0,
            "fact_signatures": 0,
            "score_anchors": 0,
            "component_anchors": 0,
        },
        safe_anchor_count=7,
        safe_memory_hash=_stable_hash(anchors),
    )
    return HistoricalBlindReplayCase(research_input, target, memory)


def _synthetic_observation(blind_case_id: str, total: float) -> Mapping[str, Any]:
    return {
        "blind_case_id": blind_case_id,
        "component_points": {
            component_id: maximum * (total / 100.0)
            for component_id, maximum in _maxima().items()
        },
        "predicted_stage_band": "2",
        "counter_fact_ids": [],
    }


def _stable_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")
    ).hexdigest()


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


if __name__ == "__main__":
    unittest.main()
