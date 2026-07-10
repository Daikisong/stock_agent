from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    BaselineLane,
    BaselineLaneRecord,
    BaselineLaneStatus,
    CandidateEvent,
    CurrentDepthSelector,
    DepthSelectionConfig,
    LiveDepth,
    LiveUniverseRow,
    TriggerSignal,
    TriggerType,
    load_depth_decisions,
    load_live_run_profile,
    write_depth_selection,
)


def _universe(symbol: str) -> LiveUniverseRow:
    return LiveUniverseRow(
        symbol=symbol,
        company_name=f"회사{symbol}",
        market="KOSPI",
        security_group="주권",
        stock_certificate_type="보통주",
        sector_type="",
        listing_date="2020-01-01",
        listing_status="LISTED",
        source_effective_date="2026-07-09",
        source_url="https://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info",
        source_document_id=f"KRX-UNIVERSE-{symbol}",
        source_content_hash="a" * 64,
        source_request_id="KRX-REQUEST",
        source_mode="LIVE_OFFICIAL_API",
        eligible=True,
        exclusion_reason=None,
        raw_fields={},
    )


def _signal(symbol: str, trigger_type: TriggerType, *, lifecycle: str = "CURRENT"):
    signal_id = f"TRIG-{symbol}-{trigger_type.value}"
    return TriggerSignal(
        trigger_signal_id=signal_id,
        target_id=symbol,
        target_name=f"회사{symbol}",
        trigger_type=trigger_type.value,
        source_event_id=f"EVENT-{symbol}-{trigger_type.value}",
        effective_date="2026-07-10",
        detected_at="2026-07-10",
        source_refs=(f"SOURCE-{symbol}",),
        provider_names=("OpenDART",),
        subject_direct=True,
        lifecycle_status=lifecycle,
        investigation_required=True,
        score_evidence_eligible=False,
        headline_or_snippet_only=False,
        payload={},
    )


def _candidate(signal: TriggerSignal) -> CandidateEvent:
    return CandidateEvent(
        candidate_event_id=f"CAND-{signal.target_id}",
        target_id=signal.target_id,
        target_name=signal.target_name,
        as_of_date="2026-07-10",
        latest_effective_date=signal.effective_date,
        trigger_types=(signal.trigger_type,),
        trigger_signal_ids=(signal.trigger_signal_id,),
        source_refs=signal.source_refs,
        investigation_required=True,
        active_thesis_present=False,
        score_evidence_eligible=False,
        summary="검증 필요",
    )


def _baseline(symbol: str) -> BaselineLaneRecord:
    return BaselineLaneRecord(
        lane_id=f"LANE-{symbol}",
        target_id=symbol,
        target_name=f"회사{symbol}",
        market="KOSPI",
        lane=BaselineLane.OFFICIAL.value,
        status=BaselineLaneStatus.NO_RESULT.value,
        observed_date="2026-07-10",
        provider_names=("OpenDART",),
        source_ids=(f"BASESRC-{symbol}",),
        values={},
    )


class LiveDepthPolicyTests(unittest.TestCase):
    def setUp(self):
        self.symbols = ("000001", "000002", "000003", "000004", "000005")
        self.universe = tuple(_universe(symbol) for symbol in self.symbols)
        types = (
            TriggerType.RISK,
            TriggerType.EARNINGS,
            TriggerType.OFFICIAL,
            TriggerType.REPORT,
            TriggerType.MARKET,
        )
        self.signals = tuple(
            _signal(
                symbol,
                trigger_type,
                lifecycle="OPEN" if trigger_type == TriggerType.RISK else "CURRENT",
            )
            for symbol, trigger_type in zip(self.symbols, types)
        )
        self.candidates = tuple(_candidate(signal) for signal in self.signals)
        self.lanes = tuple(_baseline(symbol) for symbol in self.symbols)
        self.config = DepthSelectionConfig(
            as_of_date="2026-07-10",
            max_official_light_targets=4,
            max_deep_candidates=3,
            max_brain_candidates=2,
            max_acquisition_candidates=1,
            max_llm_calls_per_candidate=2,
            max_source_tasks_per_candidate=4,
            max_fetches_per_candidate=6,
            max_retries_per_candidate=1,
            max_general_web_fetches_per_candidate=2,
            max_runtime_seconds=600,
            test_mode=True,
        )

    def _select(self, *, universe=None, candidates=None, signals=None, lanes=None):
        return CurrentDepthSelector().select(
            self.config,
            universe=self.universe if universe is None else universe,
            baseline_lanes=self.lanes if lanes is None else lanes,
            candidate_events=self.candidates if candidates is None else candidates,
            trigger_signals=self.signals if signals is None else signals,
        )

    def test_live_operational_audit_records_every_symbol_and_bounded_deep(self):
        audit = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "docs/operational/e2r_live_depth_selection_audit.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(audit["status"], "CURRENT_DEPTH_SELECTION_PASS")
        self.assertGreater(audit["eligible_universe_count"], 1000)
        self.assertEqual(
            audit["depth_decision_count"], audit["eligible_universe_count"]
        )
        self.assertGreater(audit["selected_deep_count"], 0)
        self.assertLessEqual(
            audit["selected_deep_count"], audit["budget_limits"]["max_deep_candidates"]
        )
        self.assertEqual(audit["unbounded_candidate_count"], 0)
        self.assertEqual(audit["forced_archetype_quota_count"], 0)
        self.assertEqual(audit["not_selected_without_reason_count"], 0)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(audit["hard_acceptance_pass"])

    def test_every_symbol_gets_decision_and_nested_budgets_are_respected(self):
        result = self._select()

        self.assertEqual(result.status, "CURRENT_DEPTH_SELECTION_PASS")
        self.assertEqual(len(result.decisions), len(self.universe))
        self.assertEqual(result.audit["selected_official_light_count"], 4)
        self.assertEqual(result.audit["selected_deep_count"], 2)
        self.assertEqual(result.audit["selected_brain_count"], 2)
        self.assertEqual(result.audit["acquisition_eligible_count"], 1)
        self.assertEqual(result.audit["unbounded_candidate_count"], 0)
        self.assertEqual(result.audit["forced_archetype_quota_count"], 0)
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_selected_brain_targets_stop_at_l3_until_acquisition_executes(self):
        result = self._select()
        selected = [decision for decision in result.decisions if decision.selected_for_brain]

        self.assertEqual(len(selected), 2)
        self.assertTrue(
            all(decision.maximum_depth == LiveDepth.L3_RESEARCH_BRAIN.value for decision in selected)
        )
        self.assertTrue(
            all(
                decision.completed_depths
                == (
                    LiveDepth.L0_UNIVERSE.value,
                    LiveDepth.L1_BASELINE.value,
                    LiveDepth.L2_OFFICIAL_LIGHT.value,
                    LiveDepth.L3_RESEARCH_BRAIN.value,
                )
                for decision in selected
            )
        )

    def test_nonselected_targets_have_exact_budget_reason(self):
        result = self._select()
        not_selected = [decision for decision in result.decisions if not decision.selected_for_deep]

        self.assertEqual(len(not_selected), 3)
        self.assertTrue(all(decision.not_selected_reason for decision in not_selected))
        self.assertEqual(result.audit["not_selected_without_reason_count"], 0)
        self.assertEqual(len(result.not_selected_budget), 3)

    def test_current_selection_is_deterministic_and_has_no_archetype_quota(self):
        first = self._select()
        second = self._select(
            universe=tuple(reversed(self.universe)),
            candidates=tuple(reversed(self.candidates)),
            signals=tuple(reversed(self.signals)),
            lanes=tuple(reversed(self.lanes)),
        )

        self.assertEqual(
            [decision.to_dict() for decision in first.decisions],
            [decision.to_dict() for decision in second.decisions],
        )
        self.assertTrue(all(not decision.forced_archetype_quota for decision in first.decisions))

    def test_no_signal_run_fails_selected_deep_gate_instead_of_fake_pass(self):
        result = self._select(candidates=(), signals=())

        self.assertEqual(result.status, "CURRENT_DEPTH_SELECTION_FAIL")
        self.assertEqual(result.audit["selected_deep_count"], 0)
        self.assertEqual(result.audit["critical_counts"]["selected_deep_empty"], 1)

    def test_production_profile_builds_finite_nested_config(self):
        profile = load_live_run_profile("configs/e2r_production_daily_v1.json")
        config = DepthSelectionConfig.from_run_profile(
            as_of_date="2026-07-10",
            profile=profile,
        )

        self.assertEqual(config.max_deep_candidates, 60)
        self.assertEqual(config.max_brain_candidates, 40)
        self.assertEqual(config.max_acquisition_candidates, 40)
        self.assertGreater(config.max_runtime_seconds, 0)

    def test_writer_and_loader_preserve_all_depth_leaf_rows(self):
        result = self._select()
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_depth_selection(result, output_root=tmp)
            loaded = load_depth_decisions(paths["decisions"])
            self.assertEqual(
                [decision.to_dict() for decision in loaded],
                [decision.to_dict() for decision in result.decisions],
            )
            self.assertTrue(all(Path(path).is_file() for path in paths.values()))


if __name__ == "__main__":
    unittest.main()
