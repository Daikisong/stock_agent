from __future__ import annotations

from datetime import date
import json
import os
from pathlib import Path
import tempfile
import unittest

from e2r.calibration.cli import build_parser, run_calibration_pipeline
from e2r.calibration.dedupe import dedupe_trigger_rows
from e2r.calibration.md_discovery import discover_markdown_documents, result_documents
from e2r.calibration.md_parser import parse_markdown_document
from e2r.calibration.promotion import promote_calibrated_profile
from e2r.calibration.scoring_profile import get_active_scoring_profile, load_scoring_profile
from e2r.calibration.validation import parse_number, validate_trigger_rows
from e2r.models import ScoreSnapshot, Stage
from e2r.red_team import RedTeamAssessment
from e2r.scoring import DeterministicScorer, ScoringPayload
from e2r.staging import StageClassificationInput, StageClassifier


def _result_md(round_id: int, loop: int, symbol: str = "000001", trigger_type: str = "Stage2") -> str:
    return f"""# E2R Stock-Web Historical Calibration / Backtest Optimization Round

```text
round = R{round_id}
loop = {loop}
sector = 테스트
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

```jsonl
{{"row_type":"price_source_validation","source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","validation_status":"usable_for_historical_calibration"}}
{{"row_type":"case","case_id":"case_{round_id}_{loop}_{symbol}","symbol":"{symbol}","round":"R{round_id}","loop":"{loop}","sector":"테스트","case_type":"structural_success","primary_archetype":"TEST_ARCHETYPE","calibration_usable":true,"price_source":"Songdaiki/stock-web"}}
{{"row_type":"trigger","trigger_id":"trigger_{round_id}_{loop}_{symbol}_{trigger_type}","case_id":"case_{round_id}_{loop}_{symbol}","symbol":"{symbol}","round":"R{round_id}","loop":"{loop}","sector":"테스트","primary_archetype":"TEST_ARCHETYPE","trigger_type":"{trigger_type}","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":1000,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20,"MFE_90D_pct":45,"MFE_180D_pct":70,"MAE_30D_pct":-3,"MAE_90D_pct":-8,"MAE_180D_pct":-12,"forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"group_{round_id}_{symbol}_{trigger_type}","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_source":"public disclosure and report"}}
```
"""


class CalibrationPipelineTests(unittest.TestCase):
    def test_real_generated_md_files_are_discovered_and_prompt_sections_do_not_exclude_results(self) -> None:
        docs = discover_markdown_documents("docs/round")
        results = result_documents(docs)
        self.assertGreaterEqual(len(results), 100)
        self.assertTrue({f"R{i}" for i in range(1, 14)}.issubset({doc.round for doc in results}))

    def test_prompt_spec_filename_is_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "e2r_historical_calibration_prompt.md").write_text("# E2R Historical Calibration Prompt\n", encoding="utf-8")
            docs = discover_markdown_documents(root)
            self.assertEqual(docs[0].exclusion_reason, "prompt_spec_file_excluded")

    def test_parser_extracts_jsonl_csv_table_and_preserves_symbol(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "e2r_stock_web_historical_calibration_round_R1_loop_1_test_research.md"
            path.write_text(
                _result_md(1, 1, "005930")
                + """
```csv
row_type,profile_id,case_count,avg_MFE_90D_pct,avg_MAE_90D_pct
profile_comparison,baseline_current_proxy,1,10,-5
```

|row_type|axis|baseline_value|tested_value|delta|reason|backtest_effect|trigger_ids|calibration_usable_count|notes|
|---|---|---:|---:|---:|---|---|---|---:|---|
|shadow_weight|stage2_axis|0|1|+1|reason|MFE90 45; MAE90 -8|trigger_1_1_005930_Stage2|1|note|
""",
                encoding="utf-8",
            )
            doc = result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            self.assertEqual(parsed.rows_by_type["trigger"][0]["symbol"], "005930")
            self.assertEqual(len(parsed.rows_by_type["price_source_validation"]), 1)
            self.assertEqual(len(parsed.rows_by_type["profile_comparison"]), 1)
            self.assertEqual(len(parsed.rows_by_type["shadow_weight"]), 1)

    def test_numeric_parser_handles_unavailable_markers(self) -> None:
        for value in ("unavailable", "n/a", "None", "not_applicable", "insufficient_forward_window_in_stock_web"):
            self.assertIsNone(parse_number(value))
        self.assertEqual(parse_number("1,234.5%"), 1234.5)

    def test_validation_rejects_bad_rows_and_keeps_stage2_positive_rows(self) -> None:
        good = {
            "row_type": "trigger",
            "trigger_id": "good",
            "case_id": "case",
            "symbol": "000001",
            "round": "R1",
            "trigger_type": "Stage2-Actionable",
            "entry_date": "2024-01-03",
            "entry_price": 1000,
            "price_data_source": "Songdaiki/stock-web",
            "price_basis": "tradable_raw",
            "price_adjustment_status": "raw_unadjusted_marcap",
            "MFE_30D_pct": 20,
            "MFE_90D_pct": 45,
            "MFE_180D_pct": 70,
            "MAE_30D_pct": -3,
            "MAE_90D_pct": -8,
            "MAE_180D_pct": -12,
            "forward_window_trading_days": 180,
            "calibration_usable": True,
            "aggregate_group_role": "representative",
            "dedupe_for_aggregate": True,
            "evidence_source": "public report",
        }
        narrative = {**good, "trigger_id": "narrative", "trigger_type": "Stage2", "MFE_180D_pct": "n/a"}
        price_only = {**good, "trigger_id": "price_only", "evidence_source": "price_only"}
        four_b = {**good, "trigger_id": "four_b", "trigger_type": "Stage4B"}
        four_c = {**good, "trigger_id": "four_c", "trigger_type": "Stage4C"}
        contaminated = {**good, "trigger_id": "corp", "corporate_action_window_status": "contaminated"}
        bundle = validate_trigger_rows([good, narrative, price_only, four_b, four_c, contaminated])
        valid_by_id = {row["trigger_id"]: row for row in bundle.valid_rows}
        self.assertTrue(valid_by_id["good"]["usable_for_weight_calibration"])
        self.assertFalse(valid_by_id["price_only"]["usable_for_weight_calibration"])
        self.assertTrue(valid_by_id["four_b"]["guardrail_usable"])
        self.assertTrue(valid_by_id["four_c"]["guardrail_usable"])
        rejected_reasons = {reason for row in bundle.rejected_rows for reason in row.get("rejection_reasons", [])}
        self.assertIn("missing_required_mfe_mae", rejected_reasons)
        self.assertIn("corporate_action_contaminated", rejected_reasons)
        self.assertIn("price_only_no_evidence", rejected_reasons)

    def test_dedupe_repeated_loop_rows_into_one_representative(self) -> None:
        base = {
            "trigger_id": "old",
            "same_entry_group_id": "same",
            "loop": "1",
            "parse_method": "markdown_table",
            "MFE_30D_pct": 1,
        }
        richer = {**base, "trigger_id": "new", "loop": "3", "parse_method": "jsonl", "MFE_90D_pct": 2}
        reps, dedupe_map = dedupe_trigger_rows([base, richer])
        self.assertEqual(len(reps), 1)
        self.assertEqual(reps[0]["trigger_id"], "new")
        self.assertEqual(len(dedupe_map), 2)

    def test_promotion_applies_when_coverage_and_rows_are_strong(self) -> None:
        rows = []
        for index in range(1, 6):
            rows.append(
                {
                    "trigger_id": f"s2_{index}",
                    "case_id": f"case_s2_{index}",
                    "round": f"R{index}",
                    "trigger_type": "Stage2-Actionable",
                    "usable_for_weight_calibration": True,
                    "MFE_90D_pct": 45,
                    "MAE_90D_pct": -8,
                }
            )
            rows.append(
                {
                    "trigger_id": f"yellow_{index}",
                    "case_id": f"case_y_{index}",
                    "round": f"R{index}",
                    "trigger_type": "Stage3-Yellow",
                    "usable_for_weight_calibration": True,
                    "MFE_90D_pct": 40,
                    "MAE_90D_pct": -9,
                }
            )
            rows.append(
                {
                    "trigger_id": f"green_{index}",
                    "case_id": f"case_g_{index}",
                    "round": f"R{index}",
                    "trigger_type": "Stage3-Green",
                    "usable_for_weight_calibration": True,
                    "MFE_90D_pct": 10,
                    "MAE_90D_pct": -25,
                }
            )
        for index in range(4):
            rows.append({"trigger_id": f"b{index}", "case_id": f"case_b{index}", "round": "R1", "trigger_type": "Stage4B", "guardrail_class": "price_only_4b_rejection"})
            rows.append({"trigger_id": f"c{index}", "case_id": f"case_c{index}", "round": "R2", "trigger_type": "Stage4C"})
        with tempfile.TemporaryDirectory() as tmp:
            result = promote_calibrated_profile(rows, coverage_passed=True, output_directory=tmp, write_runtime_profiles=False)
            self.assertEqual(result.promotion_status, "applied")
            self.assertTrue(result.production_default_scoring_changed)
            self.assertGreaterEqual(len(result.applied_axes), 5)

    def test_promotion_blocks_on_coverage_failure_without_claiming_default_change(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = promote_calibrated_profile([], coverage_passed=False, output_directory=tmp, write_runtime_profiles=False)
            self.assertEqual(result.promotion_status, "blocked_by_coverage_failure")
            self.assertFalse(result.production_default_scoring_changed)

    def test_full_pipeline_fixture_writes_json_and_reports(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "rounds"
            root.mkdir()
            for index in range(107):
                round_id = index % 13 + 1
                loop = index // 13 + 1
                symbol = f"{index + 1:06d}"
                trigger_type = "Stage3-Yellow" if index % 3 == 1 else "Stage3-Green" if index % 3 == 2 else "Stage2-Actionable"
                (root / f"e2r_stock_web_historical_calibration_round_R{round_id}_loop_{loop}_test_research.md").write_text(
                    _result_md(round_id, loop, symbol, trigger_type),
                    encoding="utf-8",
                )
            data_dir = Path(tmp) / "data"
            report_dir = Path(tmp) / "reports"
            result = run_calibration_pipeline(
                md_input_root=root,
                data_directory=data_dir,
                report_directory=report_dir,
                write_runtime_profiles=False,
            )
            self.assertEqual(result["summary"]["discovered_result_md_count"], 107)
            self.assertEqual(result["summary"]["promotion_status"], "applied")
            for path in (
                data_dir / "md_registry.jsonl",
                data_dir / "trigger_rows_representative.jsonl",
                data_dir / "applied_weight_changes.json",
                report_dir / "ingest_summary.md",
                report_dir / "applied_scoring_diff.md",
                report_dir / "by_round" / "R1.md",
            ):
                self.assertTrue(path.exists(), path)
            for line in (data_dir / "trigger_rows_representative.jsonl").read_text(encoding="utf-8").splitlines():
                payload = json.loads(line)
                self.assertNotIn(float("inf"), payload.values())

    def test_active_profile_is_v2_2_and_rollbacks_are_loadable(self) -> None:
        old = os.environ.get("E2R_SCORING_PROFILE")
        try:
            os.environ.pop("E2R_SCORING_PROFILE", None)
            self.assertEqual(get_active_scoring_profile().profile_id, "e2r_2_2_rolling_calibrated")
            os.environ["E2R_SCORING_PROFILE"] = "baseline"
            self.assertEqual(get_active_scoring_profile().profile_id, "e2r_2_0_baseline")
            os.environ["E2R_SCORING_PROFILE"] = "calibrated"
            self.assertEqual(get_active_scoring_profile().profile_id, "e2r_2_1_stock_web_calibrated")
        finally:
            if old is None:
                os.environ.pop("E2R_SCORING_PROFILE", None)
            else:
                os.environ["E2R_SCORING_PROFILE"] = old

    def test_default_scoring_changes_intentionally_but_baseline_can_compare(self) -> None:
        payload = ScoringPayload(
            symbol="000001",
            as_of_date=date(2024, 1, 3),
            components={
                "eps_fcf_explosion": 12,
                "earnings_visibility": 16,
                "bottleneck_pricing": 12,
                "market_mispricing": 12,
                "valuation_rerating": 9,
                "capital_allocation": 2,
                "information_confidence": 4,
            },
            diagnostic_scores={"calibration_stage2_actionable_evidence": 1},
        )
        old = os.environ.get("E2R_SCORING_PROFILE")
        try:
            os.environ["E2R_SCORING_PROFILE"] = "baseline"
            baseline = DeterministicScorer().score(payload)
            os.environ["E2R_SCORING_PROFILE"] = "calibrated"
            calibrated = DeterministicScorer().score(payload)
        finally:
            if old is None:
                os.environ.pop("E2R_SCORING_PROFILE", None)
            else:
                os.environ["E2R_SCORING_PROFILE"] = old
        self.assertGreater(calibrated.total_score, baseline.total_score)
        stage = StageClassifier().classify(
            StageClassificationInput(score=calibrated, red_team=RedTeamAssessment.empty("000001", date(2024, 1, 3)))
        )
        self.assertEqual(stage.stage, Stage.STAGE_2)
        self.assertIn("Stage2-Actionable", " ".join(stage.stage_reason))

    def test_calibrated_green_is_stricter_and_price_only_does_not_promote(self) -> None:
        score = ScoreSnapshot(
            symbol="000002",
            as_of_date=date(2024, 1, 3),
            eps_fcf_explosion_score=18,
            earnings_visibility_score=16,
            bottleneck_pricing_score=16,
            market_mispricing_score=11,
            valuation_rerating_score=11,
            capital_allocation_score=3,
            information_confidence_score=5,
            risk_penalty=0,
            total_score=86,
            diagnostic_scores={"revision_score": 52, "structural_visibility_quality": 60, "one_off_shortage_risk": 0},
        )
        old = os.environ.get("E2R_SCORING_PROFILE")
        try:
            os.environ["E2R_SCORING_PROFILE"] = "baseline"
            baseline_stage = StageClassifier().classify(
                StageClassificationInput(score=score, red_team=RedTeamAssessment.empty("000002", date(2024, 1, 3)))
            )
            os.environ["E2R_SCORING_PROFILE"] = "calibrated"
            calibrated_stage = StageClassifier().classify(
                StageClassificationInput(score=score, red_team=RedTeamAssessment.empty("000002", date(2024, 1, 3)))
            )
            price_only_score = ScoreSnapshot(
                **{**score.__dict__, "diagnostic_scores": {"price_only_blowoff_score": 90, "revision_score": 100}}
            )
            price_only_stage = StageClassifier().classify(
                StageClassificationInput(
                    score=price_only_score,
                    red_team=RedTeamAssessment.empty("000002", date(2024, 1, 3)),
                    company_event_score=80,
                )
            )
        finally:
            if old is None:
                os.environ.pop("E2R_SCORING_PROFILE", None)
            else:
                os.environ["E2R_SCORING_PROFILE"] = old
        self.assertEqual(baseline_stage.stage, Stage.STAGE_3_GREEN)
        self.assertNotEqual(calibrated_stage.stage, Stage.STAGE_3_GREEN)
        self.assertNotIn(price_only_stage.stage, {Stage.STAGE_2, Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW})

    def test_runtime_profile_sample_behaviors_are_explicit(self) -> None:
        old = os.environ.get("E2R_SCORING_PROFILE")
        try:
            near_stage2_payload = ScoringPayload(
                symbol="000011",
                as_of_date=date(2024, 2, 1),
                components={
                    "eps_fcf_explosion": 12,
                    "earnings_visibility": 13,
                    "bottleneck_pricing": 11,
                    "market_mispricing": 12,
                    "valuation_rerating": 8,
                    "capital_allocation": 4,
                    "information_confidence": 4,
                },
                diagnostic_scores={"credible_order_or_policy_evidence": 1},
            )
            os.environ["E2R_SCORING_PROFILE"] = "baseline"
            baseline_stage2_score = DeterministicScorer().score(near_stage2_payload)
            baseline_stage2 = StageClassifier().classify(
                StageClassificationInput(
                    score=baseline_stage2_score,
                    red_team=RedTeamAssessment.empty("000011", date(2024, 2, 1)),
                )
            )
            os.environ["E2R_SCORING_PROFILE"] = "calibrated"
            calibrated_stage2_score = DeterministicScorer().score(near_stage2_payload)
            calibrated_stage2 = StageClassifier().classify(
                StageClassificationInput(
                    score=calibrated_stage2_score,
                    red_team=RedTeamAssessment.empty("000011", date(2024, 2, 1)),
                )
            )
            self.assertLess(baseline_stage2_score.total_score, 65)
            self.assertGreaterEqual(calibrated_stage2_score.total_score, 65)
            self.assertNotEqual(baseline_stage2.stage, Stage.STAGE_2)
            self.assertEqual(calibrated_stage2.stage, Stage.STAGE_2)
            self.assertIn("Stage2-Actionable", " ".join(calibrated_stage2.stage_reason))

            yellow_payload = ScoringPayload(
                symbol="000012",
                as_of_date=date(2024, 2, 1),
                components={
                    "eps_fcf_explosion": 17,
                    "earnings_visibility": 15,
                    "bottleneck_pricing": 15,
                    "market_mispricing": 11,
                    "valuation_rerating": 10,
                    "capital_allocation": 5,
                    "information_confidence": 5,
                },
            )
            os.environ["E2R_SCORING_PROFILE"] = "baseline"
            baseline_yellow_score = DeterministicScorer().score(yellow_payload)
            baseline_yellow = StageClassifier().classify(
                StageClassificationInput(
                    score=baseline_yellow_score,
                    red_team=RedTeamAssessment.empty("000012", date(2024, 2, 1)),
                )
            )
            os.environ["E2R_SCORING_PROFILE"] = "calibrated"
            calibrated_yellow_score = DeterministicScorer().score(yellow_payload)
            calibrated_yellow = StageClassifier().classify(
                StageClassificationInput(
                    score=calibrated_yellow_score,
                    red_team=RedTeamAssessment.empty("000012", date(2024, 2, 1)),
                )
            )
            self.assertEqual(baseline_yellow_score.total_score, 78)
            self.assertEqual(calibrated_yellow_score.total_score, 78)
            self.assertEqual(baseline_yellow.stage, Stage.STAGE_2)
            self.assertEqual(calibrated_yellow.stage, Stage.STAGE_3_YELLOW)

            revision_gate_score = ScoreSnapshot(
                symbol="000013",
                as_of_date=date(2024, 2, 1),
                eps_fcf_explosion_score=18,
                earnings_visibility_score=16,
                bottleneck_pricing_score=16,
                market_mispricing_score=11,
                valuation_rerating_score=11,
                capital_allocation_score=5,
                information_confidence_score=5,
                risk_penalty=0,
                total_score=88,
                diagnostic_scores={"revision_score": 52, "structural_visibility_quality": 70, "one_off_shortage_risk": 0},
            )
            os.environ["E2R_SCORING_PROFILE"] = "baseline"
            baseline_revision = StageClassifier().classify(
                StageClassificationInput(
                    score=revision_gate_score,
                    red_team=RedTeamAssessment.empty("000013", date(2024, 2, 1)),
                )
            )
            os.environ["E2R_SCORING_PROFILE"] = "calibrated"
            calibrated_revision = StageClassifier().classify(
                StageClassificationInput(
                    score=revision_gate_score,
                    red_team=RedTeamAssessment.empty("000013", date(2024, 2, 1)),
                )
            )
            self.assertEqual(baseline_revision.stage, Stage.STAGE_3_GREEN)
            self.assertEqual(calibrated_revision.stage, Stage.STAGE_3_YELLOW)

            price_only_score = ScoreSnapshot(
                **{
                    **revision_gate_score.__dict__,
                    "diagnostic_scores": {"price_only_blowoff_score": 90, "revision_score": 100},
                }
            )
            price_only_stage = StageClassifier().classify(
                StageClassificationInput(
                    score=price_only_score,
                    red_team=RedTeamAssessment.empty("000013", date(2024, 2, 1)),
                    company_event_score=80,
                )
            )
            self.assertNotIn(price_only_stage.stage, {Stage.STAGE_2, Stage.STAGE_3_YELLOW, Stage.STAGE_3_GREEN})

            hard_4c_score = ScoreSnapshot(
                **{
                    **revision_gate_score.__dict__,
                    "diagnostic_scores": {
                        "hard_4c_thesis_break_score": 80,
                        "revision_score": 100,
                        "structural_visibility_quality": 70,
                    },
                }
            )
            hard_4c_stage = StageClassifier().classify(
                StageClassificationInput(
                    score=hard_4c_score,
                    red_team=RedTeamAssessment.empty("000013", date(2024, 2, 1)),
                )
            )
            self.assertEqual(hard_4c_stage.stage, Stage.STAGE_4C)
        finally:
            if old is None:
                os.environ.pop("E2R_SCORING_PROFILE", None)
            else:
                os.environ["E2R_SCORING_PROFILE"] = old

    def test_cli_argument_parsing(self) -> None:
        args = build_parser().parse_args(["--md-input-root", "docs/round", "--data-directory", "x", "--report-directory", "y"])
        self.assertEqual(args.md_input_root, "docs/round")
        self.assertEqual(load_scoring_profile("configs/e2r_scoring_profile_baseline.yaml").profile_id, "e2r_2_0_baseline")


if __name__ == "__main__":
    unittest.main()
