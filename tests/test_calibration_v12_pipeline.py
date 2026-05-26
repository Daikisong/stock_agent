from __future__ import annotations

from datetime import date
import os
from pathlib import Path
import tempfile
import unittest

from e2r.calibration.cli import build_parser, run_v12_calibration_pipeline, run_v12_full_pipeline
from e2r.calibration.dedupe import dedupe_v12_trigger_rows
from e2r.calibration.md_discovery import discover_markdown_documents, v12_result_documents
from e2r.calibration.md_parser import parse_markdown_document
from e2r.calibration.promotion import build_e2r_2_2_candidate_profile
from e2r.calibration.scoring_profile import (
    load_archetype_shadow_profile,
    load_e2r_2_2_candidate_profile,
    load_sector_shadow_profile,
)
from e2r.calibration.transition import build_stage_transition_summary
from e2r.calibration.validation import normalise_trigger_type, validate_v12_trigger_rows
from e2r.calibration.v12_apply import build_v12_rolling_profile_payload
from e2r.calibration.v12_promotion_planner import build_v12_promotion_plan
from e2r.models import Stage
from e2r.red_team import RedTeamAssessment
from e2r.scoring import DeterministicScorer, ScoringPayload
from e2r.staging import StageClassificationInput, StageClassifier


def _v12_md() -> str:
    return """# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R6`
- loop: `41`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C22_INSURANCE_RATE_CYCLE_RESERVE`
- fine_archetype_id: `INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN`
- loop_contribution_label: `canonical_archetype_rule_candidate`
- new_independent_case_count: `2`
- positive_case_count: `1`
- counterexample_count: `1`

Evidence-source exact URLs were not resolved in this run; evidence URL pending.
The non-price evidence is a source-name-level historical public-event proxy.

```jsonl
{"row_type":"case","case_id":"C_POS","symbol":"000810","company_name":"삼성화재","positive_or_counterexample":"positive","case_type":"structural_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"C_NEG","symbol":"088350","company_name":"한화생명","positive_or_counterexample":"counterexample","case_type":"failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web"}
{"row_type":"trigger","trigger_id":"T_POS_S2","case_id":"C_POS","symbol":"000810","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":1000,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":12,"MFE_90D_pct":28,"MFE_180D_pct":40,"MAE_30D_pct":-5,"MAE_90D_pct":-10,"MAE_180D_pct":-12,"forward_window_trading_days":180,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_source":"public report proxy"}
{"row_type":"trigger","trigger_id":"T_POS_GREEN","case_id":"C_POS","symbol":"000810","trigger_type":"Stage3-Green comparison","trigger_date":"2024-05-14","entry_date":"2024-05-16","entry_price":1200,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3,"MFE_90D_pct":6,"MFE_180D_pct":18,"MAE_30D_pct":-8,"MAE_90D_pct":-12,"MAE_180D_pct":-12,"forward_window_trading_days":180,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_source":"public report proxy","current_profile_verdict":"current_profile_too_late"}
{"row_type":"trigger","trigger_id":"T_NEG_S2","case_id":"C_NEG","symbol":"088350","trigger_type":"Stage2 policy-only stress","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":1000,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2,"MFE_90D_pct":3,"MFE_180D_pct":4,"MAE_30D_pct":-12,"MAE_90D_pct":-23,"MAE_180D_pct":-24,"forward_window_trading_days":180,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_source":"policy-only beta","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"trigger","trigger_id":"T_NEG_4B","case_id":"C_NEG","symbol":"088350","trigger_type":"price-only-local-4B-overlay","trigger_date":"2024-03-01","entry_date":"2024-03-04","entry_price":1050,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1,"MFE_90D_pct":1,"MFE_180D_pct":1,"MAE_30D_pct":-20,"MAE_90D_pct":-24,"MAE_180D_pct":-28,"forward_window_trading_days":180,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_source":"price_only","four_b_full_window_peak_proximity":0.4,"current_profile_verdict":"current_profile_4B_too_early"}
```
"""


class V12CalibrationPipelineTests(unittest.TestCase):
    def _write_fixture(self, root: Path) -> Path:
        path = root / "e2r_stock_web_v12_residual_round_R6_loop_41_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"
        path.write_text(_v12_md(), encoding="utf-8")
        return path

    def test_v12_file_discovery_extracts_sector_and_archetype(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self._write_fixture(Path(tmp))
            docs = v12_result_documents(discover_markdown_documents(tmp))
            self.assertEqual(len(docs), 1)
            self.assertEqual(docs[0].round, "R6")
            self.assertEqual(docs[0].loop, "41")
            self.assertEqual(docs[0].large_sector_id, "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL")
            self.assertEqual(docs[0].canonical_archetype_id, "C22_INSURANCE_RATE_CYCLE_RESERVE")

    def test_v12_metadata_and_residual_contribution_parse(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_fixture(Path(tmp))
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            self.assertEqual(parsed.registry_row["schema_family"], "v12_sector_archetype_residual")
            self.assertEqual(parsed.registry_row["large_sector_id"], "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL")
            self.assertEqual(parsed.rows_by_type["residual_contribution"][0]["loop_contribution_label"], "canonical_archetype_rule_candidate")
            self.assertTrue(parsed.rows_by_type["trigger"][0]["evidence_url_pending"])

    def test_v12_trigger_aliases_normalize(self) -> None:
        self.assertEqual(normalise_trigger_type("Stage3-Green comparison"), "Stage3-Green")
        self.assertEqual(normalise_trigger_type("price-only-local-4B-overlay"), "Stage4B")
        self.assertEqual(normalise_trigger_type("Stage2 policy-only stress"), "Stage2")

    def test_v12_validation_shadow_flags_and_promotion_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_fixture(Path(tmp))
            parsed = parse_markdown_document(v12_result_documents(discover_markdown_documents(path.parent))[0])
            triggers = parsed.rows_by_type["trigger"]
            cases = {row["case_id"]: row for row in parsed.rows_by_type["case"]}
            for row in triggers:
                case = cases.get(row["case_id"])
                if case:
                    row["positive_or_counterexample"] = case["positive_or_counterexample"]
            bundle = validate_v12_trigger_rows(triggers)
            self.assertGreaterEqual(len(bundle.valid_rows), 4)
            self.assertTrue(all(row["usable_for_global_promotion"] is False for row in bundle.valid_rows))
            self.assertTrue(any(row["evidence_url_pending"] for row in bundle.valid_rows))
            self.assertTrue(any(row["source_proxy_only"] for row in bundle.valid_rows))
            self.assertTrue(any(row["v12_stage2_quality"] == "good_stage2" for row in bundle.valid_rows))
            self.assertTrue(any(row["v12_stage2_quality"] == "bad_stage2" for row in bundle.valid_rows))

    def test_same_archetype_new_symbol_is_not_duplicate_but_same_symbol_entry_is(self) -> None:
        base = {
            "trigger_id": "a",
            "symbol": "000810",
            "canonical_archetype_id": "C22",
            "trigger_type": "Stage2-Actionable",
            "trigger_date": "2024-02-22",
            "entry_date": "2024-02-23",
            "entry_price": 1000,
        }
        new_symbol = {**base, "trigger_id": "b", "symbol": "005830"}
        duplicate = {**base, "trigger_id": "c"}
        reps, _ = dedupe_v12_trigger_rows([base, new_symbol, duplicate])
        self.assertEqual(len(reps), 2)
        self.assertEqual({row["symbol"] for row in reps}, {"000810", "005830"})

    def test_stage_transition_summary_generated(self) -> None:
        rows = [
            {"case_id": "case", "symbol": "000810", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-23", "entry_price": 1000, "MFE_180D_pct": 40},
            {"case_id": "case", "symbol": "000810", "trigger_type": "Stage3-Yellow", "entry_date": "2024-04-01", "entry_price": 1100, "MFE_180D_pct": 25},
            {"case_id": "case", "symbol": "000810", "trigger_type": "Stage3-Green", "entry_date": "2024-05-16", "entry_price": 1200, "MFE_180D_pct": 5, "current_profile_too_late": True},
            {"case_id": "case", "symbol": "000810", "trigger_type": "Stage4B", "entry_date": "2024-08-22", "entry_price": 1350, "MFE_180D_pct": 1, "MAE_90D_pct": -12, "v12_4b_quality": "good_4b_timing"},
        ]
        summary = build_stage_transition_summary(rows)
        self.assertEqual(len(summary), 1)
        self.assertEqual(summary[0]["stage2_to_yellow_return_pct"], 10.0)
        self.assertEqual(summary[0]["stage2_to_green_return_pct"], 20.0)
        self.assertEqual(summary[0]["green_upside_capture_pct"], 50.0)
        self.assertEqual(summary[0]["stage4b_peak_capture_pct"], 87.5)
        self.assertEqual(summary[0]["stage4b_to_90d_low_return_pct"], -12)
        self.assertEqual(summary[0]["transition_verdict"], "4b_good_peak_capture")

    def test_v12_full_run_writes_rolling_ledger_outputs_and_preserves_active_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "md"
            data_dir = Path(tmp) / "data"
            report_dir = Path(tmp) / "reports"
            root.mkdir()
            self._write_fixture(root)
            active_before = Path("configs/e2r_scoring_profile_active.yaml").read_text(encoding="utf-8")
            result = run_v12_full_pipeline(md_input_root=root, data_directory=data_dir, report_directory=report_dir)
            active_after = Path("configs/e2r_scoring_profile_active.yaml").read_text(encoding="utf-8")
            self.assertEqual(active_before, active_after)
            self.assertFalse(result["summary"]["production_default_scoring_changed"])
            for path in (
                data_dir / "v12_md_registry.jsonl",
                data_dir / "v12_trigger_rows_representative.jsonl",
                data_dir / "stage_transition_summary.jsonl",
                data_dir / "sector_shadow_profile.json",
                data_dir / "archetype_shadow_profile.json",
                data_dir / "e2r_2_2_candidate_profile.json",
                data_dir / "v12_archetype_evidence_state.json",
                data_dir / "v12_promotion_decisions.jsonl",
                data_dir / "v12_patch_specs.jsonl",
                report_dir / "rolling_calibration_state.md",
                report_dir / "apply_next_patch_plan.md",
                report_dir / "blocked_axes_report.md",
                report_dir / "promotion_readiness_report.md",
            ):
                self.assertTrue(path.exists(), path)
            self.assertEqual(load_sector_shadow_profile(data_dir / "sector_shadow_profile.json")["profile_status"], "rolling_calibration_ledger")
            self.assertEqual(load_archetype_shadow_profile(data_dir / "archetype_shadow_profile.json")["profile_status"], "rolling_calibration_ledger")
            candidate = load_e2r_2_2_candidate_profile(data_dir / "e2r_2_2_candidate_profile.json")
            self.assertFalse(candidate["production_default_scoring_changed"])
            self.assertIn("promotion_decision_counts", candidate)
            decisions = (data_dir / "v12_promotion_decisions.jsonl").read_text(encoding="utf-8")
            self.assertIn("apply_next_patch", decisions)
            readiness_report = (report_dir / "promotion_readiness_report.md").read_text(encoding="utf-8")
            self.assertIn("source_proxy", readiness_report)
            self.assertIn("rolling calibration", readiness_report)
            self.assertIn("live discovery", readiness_report)
            self.assertIn("safe patch", readiness_report)

    def test_v12_promotion_planner_creates_apply_next_patch_for_clean_guardrail(self) -> None:
        rows = [
            {
                "trigger_id": "T1",
                "case_id": "C1",
                "symbol": "A",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_PRICE_ONLY_THEME",
                "positive_or_counterexample": "counterexample",
                "case_type": "overheat",
                "trigger_type": "Stage4B",
                "v12_4b_quality": "price_only_4b",
                "evidence_source": "price_only",
            },
            {
                "trigger_id": "T2",
                "case_id": "C2",
                "symbol": "B",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_PRICE_ONLY_THEME",
                "positive_or_counterexample": "counterexample",
                "case_type": "overheat",
                "trigger_type": "Stage2",
                "v12_stage2_quality": "bad_stage2",
                "MFE_90D_pct": 2,
                "MAE_90D_pct": -28,
                "evidence_source": "theme_overheat_report",
            },
            {
                "trigger_id": "T3",
                "case_id": "C3",
                "symbol": "C",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_PRICE_ONLY_THEME",
                "positive_or_counterexample": "counterexample",
                "case_type": "failed_rerating",
                "trigger_type": "Stage4C",
                "v12_4c_quality": "late_4c",
                "evidence_source": "thesis_break_disclosure",
            },
        ]
        candidates = [
            {
                "axis": "local_4b_watch_guard",
                "scope": "canonical_archetype",
                "large_sector_id": None,
                "canonical_archetype_id": "C99_PRICE_ONLY_THEME",
                "row_count": 3,
                "unique_symbol_count": 3,
                "positive_case_count": 0,
                "counterexample_count": 3,
                "good_stage2_count": 0,
                "bad_stage2_count": 1,
                "stage2_high_mae_count": 1,
                "good_4b_timing_count": 0,
                "too_early_4b_count": 0,
                "price_only_4b_count": 1,
                "4c_late_count": 1,
                "hard_4c_count": 0,
                "source_proxy_only_count": 0,
                "evidence_url_pending_count": 0,
                "confidence": "low_medium",
                "reason": "Price-only rows should stay watch-only.",
            }
        ]
        plan = build_v12_promotion_plan(rows, [], [], candidates)
        self.assertEqual(plan["promotion_decisions"][0]["decision"], "apply_next_patch")
        self.assertEqual(plan["promotion_decisions"][0]["promotion_type"], "Type1_safety_guardrail")
        self.assertEqual(len(plan["patch_specs"]), 1)
        self.assertEqual(plan["patch_specs"][0]["new_value"], "price_only_4b_watch_only_not_full_4b")
        self.assertEqual(plan["patch_specs"][0]["counterexample_guard_ids"], ["C3", "C2", "C1"])

    def test_large_sector_apply_patch_specs_include_support_case_ids(self) -> None:
        rows = [
            {
                "case_id": "P1",
                "symbol": "A",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C98_TEST_A",
                "positive_or_counterexample": "positive",
                "case_type": "structural_success",
                "trigger_type": "Stage2",
                "trigger_date": "2024-01-01",
            },
            {
                "case_id": "N1",
                "symbol": "B",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_TEST_B",
                "positive_or_counterexample": "counterexample",
                "case_type": "overheat",
                "trigger_type": "Stage2",
                "trigger_date": "2024-02-01",
            },
            {
                "case_id": "N2",
                "symbol": "C",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_TEST_B",
                "positive_or_counterexample": "counterexample",
                "case_type": "failed_rerating",
                "trigger_type": "Stage4C",
                "trigger_date": "2024-03-01",
            },
        ]
        candidates = [
            {
                "axis": "stage2_required_bridge",
                "scope": "large_sector",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": None,
                "row_count": 3,
                "unique_symbol_count": 3,
                "positive_case_count": 1,
                "counterexample_count": 2,
                "bad_stage2_count": 1,
                "stage2_high_mae_count": 1,
                "source_proxy_only_count": 0,
                "evidence_url_pending_count": 0,
            }
        ]
        plan = build_v12_promotion_plan(rows, [], [], candidates)
        self.assertEqual(plan["promotion_decisions"][0]["decision"], "apply_next_patch")
        self.assertEqual(plan["patch_specs"][0]["evidence_support_ids"], ["P1"])
        self.assertEqual(plan["patch_specs"][0]["counterexample_guard_ids"], ["N2", "N1"])

    def test_defensive_patch_specs_fallback_to_raw_support_case_ids(self) -> None:
        rows = [
            {
                "case_id": "RAW_GUARD_1",
                "symbol": "A",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C19_TEST",
                "trigger_type": "Stage4B",
                "trigger_date": "2024-01-01",
                "trigger_outcome_label": "4B_too_early",
            },
            {
                "case_id": "RAW_GUARD_2",
                "symbol": "B",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C19_TEST",
                "trigger_type": "Stage4C",
                "trigger_date": "2024-02-01",
                "trigger_outcome_label": "4C_success",
            },
        ]
        candidates = [
            {
                "axis": "local_4b_watch_guard",
                "scope": "canonical_archetype",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C19_TEST",
                "row_count": 2,
                "unique_symbol_count": 2,
                "counterexample_count": 2,
                "good_4b_timing_count": 0,
                "price_only_4b_count": 1,
                "4c_late_count": 1,
                "source_proxy_only_count": 0,
                "evidence_url_pending_count": 0,
            }
        ]
        plan = build_v12_promotion_plan(rows, [], [], candidates)
        self.assertEqual(plan["promotion_decisions"][0]["decision"], "apply_next_patch")
        self.assertEqual(plan["patch_specs"][0]["evidence_support_ids"], ["RAW_GUARD_2", "RAW_GUARD_1"])
        self.assertEqual(plan["patch_specs"][0]["counterexample_guard_ids"], ["RAW_GUARD_2", "RAW_GUARD_1"])

    def test_v12_promotion_planner_blocks_positive_patch_with_proxy_data(self) -> None:
        candidates = [
            {
                "axis": "stage2_bonus_candidate_delta",
                "scope": "canonical_archetype",
                "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
                "row_count": 8,
                "unique_symbol_count": 5,
                "positive_case_count": 3,
                "counterexample_count": 2,
                "good_stage2_count": 4,
                "bad_stage2_count": 0,
                "stage2_high_mae_count": 0,
                "source_proxy_only_count": 3,
                "evidence_url_pending_count": 0,
            }
        ]
        transitions = [
            {"canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "A"},
            {"canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "B"},
            {"canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "C"},
        ]
        plan = build_v12_promotion_plan([], [], transitions, candidates)
        self.assertEqual(plan["promotion_decisions"][0]["decision"], "blocked_by_data_quality")
        self.assertEqual(plan["patch_specs"], [])

    def test_direct_e2r_2_2_candidate_profile_helper_includes_promotion_decisions(self) -> None:
        rows = [
            {
                "trigger_id": "T1",
                "case_id": "C1",
                "symbol": "A",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_PRICE_ONLY_THEME",
                "positive_or_counterexample": "counterexample",
                "case_type": "overheat",
                "trigger_type": "Stage4B",
                "v12_4b_quality": "price_only_4b",
            },
            {
                "trigger_id": "T2",
                "case_id": "C2",
                "symbol": "B",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_PRICE_ONLY_THEME",
                "positive_or_counterexample": "counterexample",
                "case_type": "overheat",
                "trigger_type": "Stage2",
                "v12_stage2_quality": "bad_stage2",
                "MAE_90D_pct": -30,
            },
            {
                "trigger_id": "T3",
                "case_id": "C3",
                "symbol": "C",
                "large_sector_id": "L0_TEST",
                "canonical_archetype_id": "C99_PRICE_ONLY_THEME",
                "positive_or_counterexample": "counterexample",
                "case_type": "failed_rerating",
                "trigger_type": "Stage4C",
                "v12_4c_quality": "late_4c",
            },
        ]
        aggregate_metrics = [
            {
                "group_name": "canonical_archetype_id",
                "group_value": "C99_PRICE_ONLY_THEME",
                "row_count": 3,
                "unique_symbol_count": 3,
                "positive_case_count": 0,
                "counterexample_count": 3,
                "good_stage2_count": 0,
                "bad_stage2_count": 1,
                "stage2_high_mae_count": 1,
                "good_4b_timing_count": 0,
                "too_early_4b_count": 0,
                "price_only_4b_count": 1,
                "4c_late_count": 1,
                "hard_4c_count": 0,
                "source_proxy_only_count": 0,
                "evidence_url_pending_count": 0,
            }
        ]
        profile = build_e2r_2_2_candidate_profile(rows, aggregate_metrics, [])
        self.assertFalse(profile["production_default_scoring_changed"])
        self.assertIn("promotion_decision_counts", profile)
        self.assertEqual(profile["apply_next_patch_count"], 3)

    def test_v12_rolling_profile_payload_turns_patch_specs_into_scoped_guards(self) -> None:
        patch_specs = [
            {
                "axis": "stage2_bonus_candidate_delta",
                "scope": "canonical_archetype:C22_INSURANCE_RATE_CYCLE_RESERVE",
                "new_value": 1.0,
            },
            {
                "axis": "stage2_required_bridge",
                "scope": "large_sector:L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                "new_value": "require_non_price_bridge",
            },
            {
                "axis": "local_4b_watch_guard",
                "scope": "canonical_archetype:C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                "new_value": "price_only_4b_watch_only_not_full_4b",
            },
            {
                "axis": "stage2_bonus_candidate_delta",
                "scope": "canonical_archetype:C_BAD",
                "new_value": 99,
            },
        ]
        profile = build_v12_rolling_profile_payload(patch_specs=patch_specs)
        self.assertEqual(profile["profile_id"], "e2r_2_2_rolling_calibrated")
        self.assertEqual(profile["adjustments"]["v12_stage2_archetype_bonus"], 1.0)
        self.assertIn("canonical_archetype:C22_INSURANCE_RATE_CYCLE_RESERVE", profile["guardrails"]["v12_stage2_bonus_scopes"])
        self.assertNotIn("C_BAD", profile["guardrails"].get("v12_stage2_bonus_scopes", ""))
        self.assertEqual(profile["thresholds"]["stage3_green_total_min"], 87.0)
        self.assertTrue(profile["guardrails"]["stage3_green_not_loosened_by_v12"])

    def test_v12_scoped_stage2_bonus_applies_only_with_non_price_bridge(self) -> None:
        old = os.environ.get("E2R_SCORING_PROFILE")
        components = {
            "eps_fcf_explosion": 12,
            "earnings_visibility": 13,
            "bottleneck_pricing": 11,
            "market_mispricing": 12,
            "valuation_rerating": 8,
            "capital_allocation": 3,
            "information_confidence": 4,
        }
        try:
            os.environ["E2R_SCORING_PROFILE"] = "calibrated"
            baseline = DeterministicScorer().score(
                ScoringPayload(
                    symbol="000810",
                    as_of_date=date(2024, 2, 23),
                    components=components,
                    diagnostic_scores={"credible_order_or_policy_evidence": 1},
                    canonical_archetype_id="C22_INSURANCE_RATE_CYCLE_RESERVE",
                )
            )
            os.environ["E2R_SCORING_PROFILE"] = "e2r_2_2"
            rolling = DeterministicScorer().score(
                ScoringPayload(
                    symbol="000810",
                    as_of_date=date(2024, 2, 23),
                    components=components,
                    diagnostic_scores={"credible_order_or_policy_evidence": 1},
                    canonical_archetype_id="C22_INSURANCE_RATE_CYCLE_RESERVE",
                )
            )
            unscoped = DeterministicScorer().score(
                ScoringPayload(
                    symbol="000810",
                    as_of_date=date(2024, 2, 23),
                    components=components,
                    diagnostic_scores={"credible_order_or_policy_evidence": 1},
                    canonical_archetype_id="C00_UNKNOWN",
                )
            )
        finally:
            if old is None:
                os.environ.pop("E2R_SCORING_PROFILE", None)
            else:
                os.environ["E2R_SCORING_PROFILE"] = old
        self.assertGreater(rolling.total_score, baseline.total_score)
        self.assertEqual(unscoped.total_score, baseline.total_score)
        self.assertEqual(rolling.diagnostic_scores["v12_stage2_scope_bonus_applied"], 1.0)
        self.assertEqual(rolling.diagnostic_scores["archetype_weight_profile_applied"], 1.0)

    def test_v12_required_bridge_blocks_scoped_price_only_stage2(self) -> None:
        old = os.environ.get("E2R_SCORING_PROFILE")
        try:
            os.environ["E2R_SCORING_PROFILE"] = "e2r_2_2"
            score = DeterministicScorer().score(
                ScoringPayload(
                    symbol="POLICY",
                    as_of_date=date(2024, 2, 23),
                    components={
                        "eps_fcf_explosion": 14,
                        "earnings_visibility": 15,
                        "bottleneck_pricing": 13,
                        "market_mispricing": 12,
                        "valuation_rerating": 9,
                        "capital_allocation": 3,
                        "information_confidence": 4,
                    },
                    diagnostic_scores={"evidence_family_price": 1, "cross_evidence_family_count": 1},
                    large_sector_id="L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
                )
            )
            stage = StageClassifier().classify(
                StageClassificationInput(score=score, red_team=RedTeamAssessment.empty("POLICY", date(2024, 2, 23)))
            )
        finally:
            if old is None:
                os.environ.pop("E2R_SCORING_PROFILE", None)
            else:
                os.environ["E2R_SCORING_PROFILE"] = old
        self.assertGreaterEqual(score.total_score, 65)
        self.assertEqual(score.diagnostic_scores["v12_scope_stage2_required_bridge_match"], 1.0)
        self.assertNotEqual(stage.stage, Stage.STAGE_2)

    def test_v12_calibration_pipeline_can_apply_profile_when_requested(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "md"
            data_dir = Path(tmp) / "data"
            report_dir = Path(tmp) / "reports"
            active_path = Path("configs/e2r_scoring_profile_active.yaml")
            profile_path = Path("configs/e2r_scoring_profile_v2_2.yaml")
            active_before = active_path.read_text(encoding="utf-8")
            profile_before = profile_path.read_text(encoding="utf-8") if profile_path.exists() else None
            root.mkdir()
            self._write_fixture(root)
            try:
                result = run_v12_calibration_pipeline(
                    md_input_root=root,
                    data_directory=data_dir,
                    report_directory=report_dir,
                    activate_profile=True,
                )
                self.assertTrue(result["summary"]["production_default_scoring_changed"])
                self.assertTrue((report_dir / "rolling_calibration_apply_report.md").exists())
                self.assertEqual(
                    Path("configs/e2r_scoring_profile_active.yaml").read_text(encoding="utf-8"),
                    "active_profile: e2r_2_2\nrollback_profile: calibrated\n",
                )
            finally:
                active_path.write_text(active_before, encoding="utf-8")
                if profile_before is None:
                    profile_path.unlink(missing_ok=True)
                else:
                    profile_path.write_text(profile_before, encoding="utf-8")

    def test_v12_cli_argument_parsing(self) -> None:
        args = build_parser().parse_args(
            [
                "run-v12-calibration",
                "--md-input-root",
                "docs/example",
                "--data-directory",
                "data/e2r/calibration/v12",
                "--report-directory",
                "reports/e2r_calibration/v12",
            ]
        )
        self.assertEqual(args.command, "run-v12-calibration")
        self.assertEqual(args.md_input_root, "docs/example")


if __name__ == "__main__":
    unittest.main()
