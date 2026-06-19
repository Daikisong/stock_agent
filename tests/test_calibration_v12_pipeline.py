from __future__ import annotations

from datetime import date
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.calibration.archetype_weight_profile import ARCHETYPE_WEIGHT_SEEDS, LARGE_SECTOR_WEIGHT_SEEDS
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
from e2r.calibration.taxonomy import (
    CANONICAL_ARCHETYPE_IDS,
    LARGE_SECTOR_ALIASES,
    LARGE_SECTOR_IDS,
    normalise_canonical_archetype_id,
    normalise_large_sector_id,
)
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


def _v12_no_repeat_standalone_md() -> str:
    return """# E2R Stock-Web V12 No Repeat Standalone Research

## Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- selected_round: `R3`
- large_sector_id: `L3_BATTERY_EV_STORAGE`
- canonical_archetype_id: `C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX`
- fine_archetype_id: `STANDALONE_ALIAS_FIXTURE`
- price_source: `Songdaiki/stock-web`
- shadow_weight_only: `true`

```jsonl
{"schema_version":"v12_no_repeat_standalone_trigger_row_v1","selected_round":"R3","large_sector_id":"L3_BATTERY_EV_STORAGE","canonical_archetype_id":"C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX","fine_archetype_id":"STANDALONE_ALIAS_FIXTURE","trigger_id":"NR-T001","case_id":"NR-C001","symbol":"000001","trigger_type":"4B-local-price-only","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":1000,"MFE_30D_pct":2,"MFE_90D_pct":3,"MFE_180D_pct":4,"MAE_30D_pct":-8,"MAE_90D_pct":-12,"MAE_180D_pct":-18,"forward_window_trading_days":180,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_source":"price_only_local"}
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

    def test_v12_result_filename_wins_over_prompt_title(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = (
                root
                / "e2r_stock_web_v12_residual_round_R6_loop_41_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"
            )
            markdown = _v12_md().replace(
                "# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round",
                "# E2R Historical Calibration Prompt v12",
                1,
            )
            path.write_text(markdown, encoding="utf-8")

            docs = discover_markdown_documents(root)
            v12_docs = v12_result_documents(docs)

            self.assertEqual(len(v12_docs), 1)
            self.assertFalse(v12_docs[0].is_prompt_spec)
            self.assertIsNone(v12_docs[0].exclusion_reason)

    def test_v12_file_discovery_skips_achieve_archive_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_fixture(root)
            suffix_path = (
                root
                / "e2r_stock_web_v12_residual_round_R6_loop_42_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research (1).md"
            )
            suffix_path.write_text(_v12_md(), encoding="utf-8")
            for archive_name in ("achieve", "achieve_v12"):
                archive = root / archive_name
                archive.mkdir()
                archived_path = (
                    archive
                    / "e2r_stock_web_v12_residual_round_R6_loop_43_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"
                )
                archived_path.write_text(_v12_md(), encoding="utf-8")

            docs = v12_result_documents(discover_markdown_documents(root))
            self.assertEqual(len(docs), 2)
            self.assertEqual({doc.path.parent for doc in docs}, {root})
            self.assertIn(suffix_path, {doc.path for doc in docs})

    def test_v12_file_discovery_can_include_achieve_archive_for_cumulative_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_fixture(root)
            archive = root / "achieve" / "achieve_v12"
            archive.mkdir(parents=True)
            archived_path = (
                archive
                / "e2r_stock_web_v12_residual_round_R6_loop_43_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"
            )
            archived_path.write_text(_v12_md(), encoding="utf-8")

            docs = v12_result_documents(discover_markdown_documents(root, include_archive=True))

            self.assertEqual(len(docs), 2)
            self.assertIn(archived_path, {doc.path for doc in docs})

    def test_v12_no_repeat_standalone_discovery_parse_and_normalize(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_STORAGE_C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX_fixture_research.md"
            )
            path.write_text(_v12_no_repeat_standalone_md(), encoding="utf-8")

            docs = v12_result_documents(discover_markdown_documents(tmp))
            self.assertEqual(len(docs), 1)
            self.assertEqual(docs[0].round, "R3")
            self.assertEqual(docs[0].loop, "standalone")
            self.assertEqual(docs[0].large_sector_id, "L3_BATTERY_EV_GREEN_MOBILITY")
            self.assertEqual(docs[0].canonical_archetype_id, "C02_POWER_GRID_DATACENTER_CAPEX")

            parsed = parse_markdown_document(docs[0])
            trigger_rows = parsed.rows_by_type["trigger"]
            self.assertEqual(len(trigger_rows), 1)
            self.assertEqual(trigger_rows[0]["row_type"], "trigger")
            self.assertEqual(trigger_rows[0]["round"], "R3")
            self.assertEqual(trigger_rows[0]["loop"], "standalone")
            self.assertEqual(trigger_rows[0]["large_sector_id"], "L3_BATTERY_EV_GREEN_MOBILITY")
            self.assertEqual(trigger_rows[0]["canonical_archetype_id"], "C02_POWER_GRID_DATACENTER_CAPEX")

            bundle = validate_v12_trigger_rows(trigger_rows)
            self.assertEqual(len(bundle.valid_rows), 1)
            self.assertEqual(bundle.valid_rows[0]["trigger_type"], "Stage4B")

    def test_v12_r13_cross_case_rows_parse_as_guardrail_triggers(self) -> None:
        markdown = """# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R13`
- loop: `71`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM`

```jsonl
{"row_type":"r13_cross_case","source_round":"R12","source_loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_trigger_id":"SRC-T1","case_id":"R12L71-C32-003920","symbol":"003920","trigger_type":"Stage4B-GovernanceExecutionRisk","entry_date":"2021-05-28","entry_price":570000,"mfe_30_pct":42.63,"mae_30_pct":-5.26,"mfe_90_pct":42.63,"mae_90_pct":-20.14,"mfe_180_pct":42.63,"mae_180_pct":-34.91,"calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"aggregate","axis":"stage2_required_bridge","row_count":1}
{"row_type":"r13_cross_summary","selected_cross_case_count":1,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_candidate","axis":"local_4b_watch","decision":"hold_for_more_evidence"}
```
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_residual_round_R13_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md"
            )
            path.write_text(markdown, encoding="utf-8")
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            trigger_rows = parsed.rows_by_type["trigger"]

            self.assertEqual(len(trigger_rows), 1)
            self.assertEqual(len(parsed.rows_by_type["aggregate_metric"]), 1)
            self.assertEqual(len(parsed.rows_by_type["shadow_weight"]), 1)
            self.assertEqual(trigger_rows[0]["row_type"], "trigger")
            self.assertEqual(trigger_rows[0]["source_row_type"], "r13_cross_case")
            self.assertEqual(trigger_rows[0]["round"], "R12")
            self.assertEqual(trigger_rows[0]["loop"], "71")
            self.assertEqual(trigger_rows[0]["trigger_id"], "SRC-T1")
            self.assertEqual(trigger_rows[0]["MFE_30D_pct"], 42.63)
            self.assertEqual(trigger_rows[0]["MAE_180D_pct"], -34.91)
            self.assertTrue(trigger_rows[0]["do_not_count_as_new_case"])

            bundle = validate_v12_trigger_rows(trigger_rows)
            self.assertEqual(len(bundle.valid_rows), 1)
            self.assertEqual(bundle.valid_rows[0]["trigger_type"], "Stage4B")
            self.assertTrue(bundle.valid_rows[0]["guardrail_usable"])
            self.assertFalse(bundle.valid_rows[0]["usable_for_new_weight_evidence"])

    def test_v12_r13_review_trigger_rows_parse_as_guardrail_triggers(self) -> None:
        markdown = """# E2R Stock-Web v12 Residual Research — R13 Loop 71

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R13`
- loop: `71`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`

```jsonl
{"row_type":"r13_review_trigger","research_id":"R13L71_HIGH_MAE_GUARDRAIL","round":"R13","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","trigger_type":"Stage2-FalsePositive-PF-Overhang-NoRepairBridge","entry_date":"2024-01-31","entry_price":5210.0,"mfe_180d_pct":1.34,"mae_180d_pct":-45.30,"calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","do_not_count_as_new_sector_case":true}
{"row_type":"r13_cross_archetype_rule_candidate","rule_name":"R13_high_mfe_high_mae_bridge_governor","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL"}
```
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_residual_round_R13_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md"
            )
            path.write_text(markdown, encoding="utf-8")
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            trigger_rows = parsed.rows_by_type["trigger"]

            self.assertEqual(len(trigger_rows), 1)
            self.assertEqual(trigger_rows[0]["row_type"], "trigger")
            self.assertEqual(trigger_rows[0]["source_row_type"], "r13_review_trigger")
            self.assertEqual(trigger_rows[0]["MFE_180D_pct"], 1.34)
            self.assertEqual(trigger_rows[0]["MAE_180D_pct"], -45.30)
            self.assertTrue(trigger_rows[0]["do_not_count_as_new_case"])
            self.assertEqual(len(parsed.rows_by_type["canonical_archetype_rule_candidate"]), 1)

            bundle = validate_v12_trigger_rows(trigger_rows)
            self.assertEqual(len(bundle.valid_rows), 0)
            self.assertEqual(len(bundle.rejected_rows), 1)
            self.assertIn("missing_required_mfe_mae", bundle.rejected_rows[0]["validation_reasons"])

    def test_v12_compact_case_rows_synthesise_trigger_rows(self) -> None:
        markdown = """# E2R v12 compact case fixture

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R7`
- loop: `89`
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`

```jsonl
{"row_type":"case","case_id":"POS","symbol":"326030","entry_date":"2024-07-12","entry_close":83000,"trigger_type":"approved_drug_sales_bridge","classification":"positive_with_local_4b_overlay","mfe_30d_pct":34.58,"mae_30d_pct":-12.53,"mfe_90d_pct":43.98,"mae_90d_pct":-12.53,"mfe_180d_pct":56.39,"mae_180d_pct":-12.53,"calibration_usable":true}
{"row_type":"case","case_id":"NEG","symbol":"128940","entry_date":"2024-03-25","entry_close":347000,"trigger_type":"pipeline_headline_without_revenue_bridge","classification":"counterexample_high_mae","mfe_30d_pct":0.86,"mae_30d_pct":-14.55,"mfe_90d_pct":0.86,"mae_90d_pct":-25.65,"mfe_180d_pct":0.86,"mae_180d_pct":-25.65,"calibration_usable":true}
```
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md"
            )
            path.write_text(markdown, encoding="utf-8")
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            trigger_rows = parsed.rows_by_type["trigger"]

            self.assertEqual(len(trigger_rows), 2)
            self.assertTrue(all(row["source_row_type"] == "v12_compact_case" for row in trigger_rows))
            positive = next(row for row in trigger_rows if row["case_id"] == "POS")
            counter = next(row for row in trigger_rows if row["case_id"] == "NEG")
            self.assertEqual(positive["entry_price"], 83000)
            self.assertEqual(positive["trigger_type"], "Stage2-Actionable")
            self.assertEqual(positive["positive_or_counterexample"], "positive")
            self.assertEqual(counter["trigger_type"], "Stage2")
            self.assertEqual(counter["positive_or_counterexample"], "counterexample")

            bundle = validate_v12_trigger_rows(trigger_rows)
            self.assertEqual(len(bundle.valid_rows), 2)
            by_case = {row["case_id"]: row for row in bundle.valid_rows}
            self.assertTrue(by_case["POS"]["usable_for_new_weight_evidence"])
            self.assertFalse(by_case["NEG"]["usable_for_new_weight_evidence"])

    def test_v12_trigger_case_and_cross_review_aliases_parse_as_triggers(self) -> None:
        markdown = """# E2R v12 trigger aliases

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R13`
- loop: `84`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`

```jsonl
{"row_type":"trigger_case","case_id":"C16_POS","ticker":"036460","trigger_type":"east_sea_policy_cashflow_bridge","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":39400,"mfe_pct":63.71,"mae_pct":-4.19,"classification":"positive_with_local_4B_watch","calibration_usable":true}
{"row_type":"cross_review_trigger","review_id":"R13_REVIEW_NEG","original_trigger_type":"Stage2-FalsePositive-NoBridge","symbol":"004090","entry_date":"2024-06-04","entry_price":23300,"MFE_90D_pct":20.60,"MAE_90D_pct":-33.30,"polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","calibration_usable":true}
```
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_residual_round_R13_loop_84_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md"
            )
            path.write_text(markdown, encoding="utf-8")
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            trigger_rows = parsed.rows_by_type["trigger"]

            self.assertEqual(len(trigger_rows), 2)
            by_source = {row["source_row_type"]: row for row in trigger_rows}
            self.assertEqual(by_source["trigger_case"]["symbol"], "036460")
            self.assertEqual(by_source["trigger_case"]["MFE_180D_pct"], 63.71)
            self.assertEqual(by_source["trigger_case"]["trigger_type"], "Stage2-Actionable")
            self.assertEqual(by_source["cross_review_trigger"]["trigger_id"], "R13_REVIEW_NEG")
            self.assertEqual(by_source["cross_review_trigger"]["trigger_type"], "Stage2")

            bundle = validate_v12_trigger_rows(trigger_rows)
            self.assertEqual(len(bundle.valid_rows), 0)
            self.assertEqual(len(bundle.rejected_rows), 2)
            self.assertTrue(
                all("missing_required_mfe_mae" in row["validation_reasons"] for row in bundle.rejected_rows)
            )

    def test_v12_review_only_file_gets_rejected_audit_trigger(self) -> None:
        markdown = """# E2R v12 review-only fixture

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R13`
- loop: `97`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM`

```jsonl
{"row_type":"shadow_weight","axis":"stage2_required_bridge","counterexample_count":12,"new_independent_case_count":0}
{"row_type":"residual_contribution","new_independent_case_count":0,"loop_contribution_label":"axis_stress_test_passed","do_not_propose_new_weight_delta":true}
```
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_residual_round_R13_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md"
            )
            path.write_text(markdown, encoding="utf-8")
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            trigger_rows = parsed.rows_by_type["trigger"]

            self.assertEqual(len(trigger_rows), 1)
            self.assertEqual(trigger_rows[0]["source_row_type"], "v12_review_only_audit")
            bundle = validate_v12_trigger_rows(trigger_rows)
            self.assertEqual(len(bundle.valid_rows), 0)
            self.assertEqual(len(bundle.rejected_rows), 1)
            self.assertIn("missing_entry_price", bundle.rejected_rows[0]["validation_reasons"])

    def test_v12_metadata_only_result_gets_rejected_audit_trigger(self) -> None:
        markdown = """---
research_mode: stock_web_v12_sector_archetype_residual_calibration
selected_round: R8
selected_loop: 104
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
---

# C26 narrative-only residual note

This file records a C26 split, but it has no structured MFE/MAE trigger rows.
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_residual_round_R8_loop_104_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md"
            )
            path.write_text(markdown, encoding="utf-8")
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            trigger_rows = parsed.rows_by_type["trigger"]

            self.assertEqual(len(trigger_rows), 1)
            self.assertEqual(trigger_rows[0]["source_row_type"], "v12_review_only_audit")
            self.assertEqual(parsed.registry_row["parsed_trigger_row_count"], 1)

            bundle = validate_v12_trigger_rows(trigger_rows)
            self.assertEqual(len(bundle.valid_rows), 0)
            self.assertEqual(len(bundle.rejected_rows), 1)
            self.assertIn("missing_entry_price", bundle.rejected_rows[0]["validation_reasons"])

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
        self.assertEqual(normalise_trigger_type("Stage3-Green-comparison"), "Stage3-Green")
        self.assertEqual(normalise_trigger_type("Stage4B-overlay"), "Stage4B")
        self.assertEqual(normalise_trigger_type("4C-watch"), "Stage4C")
        self.assertEqual(normalise_trigger_type("price-only-local-4B-overlay"), "Stage4B")
        self.assertEqual(normalise_trigger_type("4B-local-price-only"), "Stage4B")
        self.assertEqual(normalise_trigger_type("Stage2 policy-only stress"), "Stage2")
        self.assertEqual(normalise_trigger_type("Stage2-Actionable-GovernanceOverhangRelease"), "Stage2-Actionable")
        self.assertEqual(normalise_trigger_type("Stage4B-GovernanceExecutionRisk"), "Stage4B")
        self.assertEqual(normalise_trigger_type("4C-thesis-break"), "Stage4C")

    def test_v12_runtime_weight_seed_covers_canonical_taxonomy(self) -> None:
        self.assertTrue(all(key in ARCHETYPE_WEIGHT_SEEDS for key in CANONICAL_ARCHETYPE_IDS))
        self.assertTrue(all(key in LARGE_SECTOR_WEIGHT_SEEDS for key in LARGE_SECTOR_IDS))
        self.assertEqual(normalise_large_sector_id("L3_BATTERY_EV_STORAGE"), "L3_BATTERY_EV_GREEN_MOBILITY")
        self.assertEqual(normalise_large_sector_id("L9_CONSTRUCTION_REAL_ESTATE"), "L9_CONSTRUCTION_REALESTATE_HOUSING")
        self.assertEqual(
            normalise_canonical_archetype_id("C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX"),
            "C02_POWER_GRID_DATACENTER_CAPEX",
        )
        self.assertTrue(all(normalise_large_sector_id(alias) in LARGE_SECTOR_WEIGHT_SEEDS for alias in LARGE_SECTOR_ALIASES))

    def test_v12_ohlc_table_inherits_trigger_grid_stage_metadata(self) -> None:
        markdown = """# Split trigger grid fixture

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R7`
- loop: `27`
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C24_BIO_TRIAL_DATA_EVENT_RISK`

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | trigger_outcome_label | current_profile_verdict | aggregate role |
|---|---|---|---:|---:|---:|---|---|---|
| R7L27-T001 | CASE-A | Stage2-Actionable | 2023-10-23 | 2023-10-24 | 58000 | structural_success | current_profile_too_late | representative |

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L27-T001 | 000100 | 2023-10-24 | 58000 | 10.69 | -5.34 | 23.45 | -5.34 | 73.10 | -5.34 |
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = (
                Path(tmp)
                / "e2r_stock_web_v12_residual_round_R7_loop_27_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md"
            )
            path.write_text(markdown, encoding="utf-8")
            doc = v12_result_documents(discover_markdown_documents(path.parent))[0]
            parsed = parse_markdown_document(doc)
            ohlc_rows = [row for row in parsed.rows_by_type["trigger"] if row.get("MFE_90D_pct")]

            self.assertEqual(len(ohlc_rows), 1)
            self.assertEqual(ohlc_rows[0]["trigger_type"], "Stage2-Actionable")
            self.assertEqual(ohlc_rows[0]["case_id"], "CASE-A")
            self.assertEqual(ohlc_rows[0]["current_profile_verdict"], "current_profile_too_late")

            bundle = validate_v12_trigger_rows(parsed.rows_by_type["trigger"])
            self.assertTrue(any(row.get("trigger_type") == "Stage2-Actionable" for row in bundle.valid_rows))
            self.assertFalse(any(row.get("trigger_type") == "" for row in bundle.valid_rows))

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

    def test_v12_dedupe_accepts_list_evidence_family(self) -> None:
        base = {
            "trigger_id": "a",
            "symbol": "000810",
            "canonical_archetype_id": "C22",
            "trigger_type": "Stage2-Actionable",
            "trigger_date": "2024-02-22",
            "entry_date": "2024-02-23",
            "entry_price": 1000,
            "evidence_family": ["orderbook", "margin_bridge"],
        }
        duplicate = {**base, "trigger_id": "b", "evidence_family": ["orderbook", "margin_bridge"]}
        reordered_duplicate = {**base, "trigger_id": "c", "evidence_family": ["margin_bridge", "orderbook"]}
        independent_family = {**base, "trigger_id": "d", "evidence_family": ["orderbook", "margin_bridge", "fcf"]}

        reps, dedupe_map = dedupe_v12_trigger_rows([base, duplicate, reordered_duplicate, independent_family])

        self.assertEqual(len(reps), 2)
        self.assertEqual(len(dedupe_map), 4)
        self.assertTrue(any(row["dedupe_member_count"] == 3 for row in reps))

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
                data_dir / "v12_raw_aggregate_metric_rows.jsonl",
                data_dir / "v12_raw_shadow_weight_rows.jsonl",
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
            with tempfile.TemporaryDirectory() as tmp:
                profile_payload = build_v12_rolling_profile_payload(
                    patch_specs=[
                        {
                            "axis": "stage2_bonus_candidate_delta",
                            "scope": "canonical_archetype:C22_INSURANCE_RATE_CYCLE_RESERVE",
                            "new_value": 1.0,
                        }
                    ]
                )
                profile_path = Path(tmp) / "e2r_scoring_profile_v2_2.yaml"
                profile_path.write_text(
                    "\n".join(
                        [
                            f"profile_id: {profile_payload['profile_id']}",
                            f"profile_status: {profile_payload['profile_status']}",
                            f"previous_default_profile: {profile_payload['previous_default_profile']}",
                            f"profile_basis: {profile_payload['profile_basis']}",
                            "thresholds:",
                            *[f"  {key}: {value}" for key, value in profile_payload["thresholds"].items()],
                            "adjustments:",
                            *[f"  {key}: {value}" for key, value in profile_payload["adjustments"].items()],
                            "guardrails:",
                            *[f"  {key}: {value}" for key, value in profile_payload["guardrails"].items()],
                        ]
                    )
                    + "\n",
                    encoding="utf-8",
                )
                os.environ["E2R_SCORING_PROFILE"] = "calibrated"
                baseline = DeterministicScorer().score(
                    ScoringPayload(
                        symbol="000810",
                        as_of_date=date(2024, 2, 23),
                        components=components,
                        diagnostic_scores={"credible_order_or_policy_evidence": 1},
                        large_sector_id="L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                        canonical_archetype_id="C22_INSURANCE_RATE_CYCLE_RESERVE",
                    )
                )
                os.environ["E2R_SCORING_PROFILE"] = "e2r_2_2"
                with patch("e2r.calibration.scoring_profile.V2_2_PROFILE_PATH", profile_path):
                    rolling = DeterministicScorer().score(
                        ScoringPayload(
                            symbol="000810",
                            as_of_date=date(2024, 2, 23),
                            components=components,
                            diagnostic_scores={"credible_order_or_policy_evidence": 1},
                            large_sector_id="L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                            canonical_archetype_id="C22_INSURANCE_RATE_CYCLE_RESERVE",
                        )
                    )
                    with self.assertRaisesRegex(ValueError, "unknown canonical_archetype_id"):
                        DeterministicScorer().score(
                            ScoringPayload(
                                symbol="000810",
                                as_of_date=date(2024, 2, 23),
                                components=components,
                                diagnostic_scores={"credible_order_or_policy_evidence": 1},
                                large_sector_id="L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                                canonical_archetype_id="C00_UNKNOWN",
                            )
                        )
        finally:
            if old is None:
                os.environ.pop("E2R_SCORING_PROFILE", None)
            else:
                os.environ["E2R_SCORING_PROFILE"] = old
        self.assertGreater(rolling.total_score, baseline.total_score)
        self.assertEqual(rolling.diagnostic_scores["v12_stage2_scope_bonus_applied"], 1.0)
        self.assertEqual(rolling.diagnostic_scores["archetype_weight_profile_applied"], 1.0)

    def test_v12_required_bridge_blocks_scoped_price_only_stage2(self) -> None:
        old = os.environ.get("E2R_SCORING_PROFILE")
        try:
            os.environ["E2R_SCORING_PROFILE"] = "e2r_2_2"
            score = DeterministicScorer().score(
                ScoringPayload(
                    symbol="GRID",
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
                    large_sector_id="L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
                    canonical_archetype_id="C02_POWER_GRID_DATACENTER_CAPEX",
                )
            )
            stage = StageClassifier().classify(
                StageClassificationInput(score=score, red_team=RedTeamAssessment.empty("GRID", date(2024, 2, 23)))
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
            weight_profile_path = Path("configs/e2r_archetype_weight_profile_v2_2.json")
            active_before = active_path.read_text(encoding="utf-8")
            profile_before = profile_path.read_text(encoding="utf-8") if profile_path.exists() else None
            weight_profile_before = (
                weight_profile_path.read_text(encoding="utf-8") if weight_profile_path.exists() else None
            )
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
                if weight_profile_before is None:
                    weight_profile_path.unlink(missing_ok=True)
                else:
                    weight_profile_path.write_text(weight_profile_before, encoding="utf-8")

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
