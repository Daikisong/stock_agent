import ast
import csv
import json
import tempfile
from datetime import date
from pathlib import Path
from types import SimpleNamespace
import unittest

from e2r.backtest import asof_research_replay, blind_discovery_replay
from e2r.backtest.e2r_standard_replay import E2RStandardReplayCandidate, _candidate_rows, jsonable
from e2r.backtest.historical_source_adapter import HistoricalSourceCoverage
from e2r.features import FeatureEngineeringInput
from e2r.models import ScoreSnapshot, Stage
from e2r.score_validity import score_state_contract_violations


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_SCORE_STATE_FIELDS = {
    "score_valid",
    "score_blocked_reason",
    "score_fingerprint",
    "research_input_fingerprint",
    "score_variability_drivers",
}


SCORE_OUTPUT_DATACLASSES = {
    "src/e2r/backtest/asof_research_replay.py": {
            "AsOfReplayCandidate": REQUIRED_SCORE_STATE_FIELDS
            | {
                "web_only_score_valid",
                "web_only_score_blocked_reason",
                "web_only_score_fingerprint",
                "web_only_research_input_fingerprint",
                "web_only_score_variability_drivers",
            },
    },
    "src/e2r/backtest/e2r_standard_replay.py": {
        "E2RStandardReplayCandidate": REQUIRED_SCORE_STATE_FIELDS,
    },
    "src/e2r/backtest/blind_discovery_replay.py": {
        "DiscoveredCandidate": REQUIRED_SCORE_STATE_FIELDS,
    },
    "src/e2r/backtest/historical_case_replay.py": {
        "HistoricalCaseReplayResult": REQUIRED_SCORE_STATE_FIELDS,
    },
    "src/e2r/backtest/historical_universe_replay.py": {
        "HistoricalReplayCandidate": REQUIRED_SCORE_STATE_FIELDS,
        "HistoricalReplayDroppedCandidate": REQUIRED_SCORE_STATE_FIELDS,
        "HistoricalReplayStageRecord": REQUIRED_SCORE_STATE_FIELDS,
    },
    "src/e2r/backtest/asof_stage_promotion_autopsy.py": {
        "StagePromotionAutopsyRow": REQUIRED_SCORE_STATE_FIELDS | {"raw_score_before_block"},
    },
}


CRITICAL_OUTPUT_TOKEN_CONTRACTS = {
    "src/e2r/pipeline/daily_scan.py": (
        '"visible_score"',
        '"score_valid"',
        '"score_blocked_reason"',
        '"score_fingerprint"',
        '"research_input_fingerprint"',
        '"score_variability_drivers"',
        '"raw_score_before_block"',
        "normalized_score_state_mapping_if_present",
        "visible_score_total(",
    ),
    "src/e2r/pipeline/korea_live_lite.py": (
        '"visible_score"',
        '"score_valid"',
        '"score_blocked_reason"',
        '"score_fingerprint"',
        '"research_input_fingerprint"',
        '"score_variability_drivers"',
        '"raw_score_before_block"',
        '"score_total": visible_score',
        "normalized_score_state_mapping_if_present",
        "cheap_scan_score",
    ),
    "src/e2r/cli/review_korea_run.py": (
        "targeted_score_states",
        "targeted_score_changes",
        "compare_score_state_rows",
        "serialized_visible_score",
        "visible_score",
        "score_variability_drivers",
        "score_fingerprint",
        "research_input_fingerprint",
    ),
    "src/e2r/backtest/historical_case_replay.py": (
        "normalized_score_state_mapping_if_present",
        "normalized_score_state_payload",
        '"total_score" in payload',
        '"score_valid" in payload',
    ),
    "src/e2r/backtest/historical_universe_replay.py": (
        "normalized_score_state_mapping_if_present",
        "normalized_score_state_payload",
        '"total_score" in payload',
        '"score_valid" in payload',
    ),
    "src/e2r/backtest/monthly_replay_suite.py": (
        "normalized_score_state_mapping_if_present",
        "normalized_score_state_payload",
        '"total_score" in payload',
        '"score_valid" in payload',
        "score_state",
        "score_variability_drivers",
        "score_fingerprint",
        "input_fingerprint",
    ),
    "src/e2r/backtest/asof_stage_promotion_autopsy.py": (
        "normalized_score_state_mapping_if_present",
        "score state",
        "score_variability_drivers",
        "score_fingerprint",
        "raw_score_before_block",
    ),
    "src/e2r/backtest/asof_research_replay.py": (
        "normalized_score_state_mapping_if_present",
        "normalized_score_state_payload",
        "visible_score",
        "web_only_score",
        "web_only_score_valid",
        "web_only_score_blocked_reason",
    ),
    "src/e2r/backtest/e2r_standard_replay.py": (
        "normalized_score_state_mapping_if_present",
        "normalized_score_state_payload",
        "visible_score",
        "score_variability_drivers",
    ),
    "src/e2r/backtest/blind_discovery_replay.py": (
        "normalized_score_state_mapping_if_present",
        "normalized_score_state_payload",
        "visible_score",
        "score_variability_drivers",
    ),
    "src/e2r/briefing.py": (
        "상태 valid fp",
        "상태 pending fp",
        "score_fingerprint",
        "score_variability_drivers",
        "visible_score_total(",
    ),
}


SCORE_MARKDOWN_HEADER_FILES = (
    "src/e2r/backtest/historical_case_replay.py",
    "src/e2r/backtest/historical_universe_replay.py",
    "src/e2r/backtest/asof_stage_promotion_autopsy.py",
    "src/e2r/pipeline/korea_live_lite.py",
    "src/e2r/backtest/monthly_replay_suite.py",
)


SCORE_OUTPUT_SCAN_FILES = tuple(SCORE_OUTPUT_DATACLASSES)
FINAL_SCORE_FIELD_NAMES = {"score", "total_score", "visible_score", "current_score", "merged_score", "score_total"}
SECONDARY_SCORE_FIELD_REQUIREMENTS = {
    "web_only_score": {
        "web_only_score_valid",
        "web_only_score_blocked_reason",
        "web_only_score_fingerprint",
        "web_only_research_input_fingerprint",
        "web_only_score_variability_drivers",
    },
}


class ScoreOutputContractTests(unittest.TestCase):
    def test_replay_score_output_dataclasses_carry_score_state(self):
        for relative_path, classes in SCORE_OUTPUT_DATACLASSES.items():
            tree = ast.parse((ROOT / relative_path).read_text(encoding="utf-8"))
            class_fields = _dataclass_fields_by_name(tree)
            for class_name, required_fields in classes.items():
                with self.subTest(path=relative_path, class_name=class_name):
                    self.assertIn(class_name, class_fields)
                    missing = sorted(required_fields - class_fields[class_name])
                    self.assertEqual(missing, [])

    def test_score_output_dataclasses_with_score_fields_have_state_contract(self):
        for relative_path in SCORE_OUTPUT_SCAN_FILES:
            tree = ast.parse((ROOT / relative_path).read_text(encoding="utf-8"))
            class_fields = _dataclass_fields_by_name(tree)
            for class_name, fields in class_fields.items():
                score_fields = sorted(FINAL_SCORE_FIELD_NAMES & fields)
                if not score_fields:
                    continue
                with self.subTest(path=relative_path, class_name=class_name, score_fields=score_fields):
                    missing = sorted(REQUIRED_SCORE_STATE_FIELDS - fields)
                    self.assertEqual(missing, [])

                for secondary_score_field, required_fields in SECONDARY_SCORE_FIELD_REQUIREMENTS.items():
                    if secondary_score_field not in fields:
                        continue
                    with self.subTest(path=relative_path, class_name=class_name, secondary_score_field=secondary_score_field):
                        missing = sorted(required_fields - fields)
                        self.assertEqual(missing, [])

    def test_critical_json_and_markdown_outputs_do_not_emit_score_without_state(self):
        for relative_path, required_tokens in CRITICAL_OUTPUT_TOKEN_CONTRACTS.items():
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            for token in required_tokens:
                with self.subTest(path=relative_path, token=token):
                    self.assertIn(token, text)

    def test_markdown_tables_do_not_use_bare_score_header(self):
        for relative_path in SCORE_MARKDOWN_HEADER_FILES:
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            for line_number, line in enumerate(text.splitlines(), start=1):
                if not line.lstrip().startswith(("\"", "'")) or "|" not in line:
                    continue
                cells = [cell.strip().strip("\"'") for cell in line.split("|")]
                bare_score_cells = [cell for cell in cells if cell == "score"]
                with self.subTest(path=relative_path, line=line_number):
                    self.assertEqual(bare_score_cells, [])

    def test_briefing_does_not_render_raw_score_total_directly(self):
        text = (ROOT / "src/e2r/briefing.py").read_text(encoding="utf-8")

        self.assertNotIn("score.total_score", text)

    def test_standard_replay_candidate_drivers_include_input_and_expansion_state(self):
        score = ScoreSnapshot(
            symbol="005930",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=10,
            bottleneck_pricing_score=12,
            market_mispricing_score=8,
            valuation_rerating_score=9,
            capital_allocation_score=2,
            information_confidence_score=4,
            risk_penalty=0,
            total_score=65,
            diagnostic_scores={
                "score_valid": 100.0,
                "estimate_missing_fcf_source": 100.0,
                "estimate_missing_revision_source": 100.0,
            },
        )
        feature_input = FeatureEngineeringInput(symbol="005930", as_of_date=date(2026, 6, 12))
        flow_result = SimpleNamespace(
            scores=(score,),
            stages=(SimpleNamespace(symbol="005930", stage=Stage.STAGE_2),),
            evidence=(),
            candidates=(
                SimpleNamespace(
                    symbol="005930",
                    company_name="삼성전자",
                    as_of_date=date(2026, 6, 12),
                    recommended_next_layer=SimpleNamespace(value="deep_research"),
                    cheap_scan_total_score=80.0,
                    reason_codes=("fixture",),
                    candidate_source_path="fixture",
                ),
            ),
            web_results=(
                SimpleNamespace(
                    score=score,
                    feature_input=feature_input,
                    feature_result=SimpleNamespace(payload=SimpleNamespace(canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY")),
                    theme_route_diagnostics={"post_score_gap_expansion_status": "not_attempted", "post_score_gap_expansion_count": 0},
                    expansion_queries_run=(),
                ),
            ),
        )
        coverage = HistoricalSourceCoverage(
            universe_available=True,
            price_available=True,
            disclosure_available=True,
            financial_available=True,
            search_snapshot_available=True,
            report_snapshot_available=True,
        )

        row = _candidate_rows(flow_result, coverage)[0]

        self.assertIn("estimate_source_missing:fcf", row.score_variability_drivers)
        self.assertIn("estimate_source_missing:revision", row.score_variability_drivers)
        self.assertIn("input_missing:research_report", row.score_variability_drivers)
        self.assertIn("input_missing:consensus", row.score_variability_drivers)
        self.assertIn("input_missing:evidence", row.score_variability_drivers)
        self.assertIn("llm_expansion_query_count:0", row.score_variability_drivers)
        self.assertIn("score_gap_expansion_status:not_attempted", row.score_variability_drivers)
        self.assertIsInstance(row.research_input_fingerprint, str)
        self.assertIn(f"research_input_fingerprint:{row.research_input_fingerprint}", row.score_variability_drivers)
        self.assertEqual(jsonable(row)["visible_score"], 65)
        self.assertEqual(score_state_contract_violations(jsonable(row)), ())

    def test_standard_replay_jsonable_does_not_copy_invalid_score_to_visible_score(self):
        row = E2RStandardReplayCandidate(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 12),
            layer="deep_research",
            stage=Stage.STAGE_0,
            rank=1,
            score=83.0,
            evidence_types_seen=("research_report",),
            reason_codes=("score_pending",),
            candidate_source_path="fixture",
            score_valid=False,
            score_blocked_reason="score_gap_unresolved",
            score_fingerprint="blocked-score",
            research_input_fingerprint="input-a",
            score_variability_drivers=("score_invalid:score_gap_unresolved", "raw_score_before_block:83"),
        )

        payload = jsonable(row)

        self.assertIsNone(payload["visible_score"])
        self.assertIsNone(payload["score"])
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_asof_candidate_csv_reconciles_score_aliases_to_visible_score(self):
        row = asof_research_replay.AsOfReplayCandidate(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 12),
            layer="deep_research",
            stage=Stage.STAGE_3_GREEN,
            rank=1,
            score=82.0,
            merged_score=65.0,
            evidence_types_seen=("research_report",),
            reason_codes=("fixture",),
            candidate_source_path="fixture",
            score_valid=True,
            score_blocked_reason=None,
        )

        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "candidates.csv"
            json_path = Path(directory) / "candidates.json"
            asof_research_replay._write_candidates(csv_path, json_path, (row,))

            with csv_path.open(encoding="utf-8") as handle:
                csv_row = next(csv.DictReader(handle))
            json_row = json.loads(json_path.read_text(encoding="utf-8"))[0]

        self.assertEqual(float(csv_row["score"]), 65.0)
        self.assertEqual(float(csv_row["visible_score"]), 65.0)
        self.assertEqual(float(csv_row["merged_score"]), 65.0)
        self.assertEqual(json_row["score"], 65.0)
        self.assertEqual(json_row["visible_score"], 65.0)
        self.assertEqual(json_row["merged_score"], 65.0)
        self.assertEqual(score_state_contract_violations(json_row), ())

    def test_asof_candidate_csv_uses_normalized_validity_when_visible_score_missing(self):
        row = asof_research_replay.AsOfReplayCandidate(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 12),
            layer="deep_research",
            stage=Stage.STAGE_3_YELLOW,
            rank=1,
            score=None,
            merged_score=None,
            evidence_types_seen=("research_report",),
            reason_codes=("fixture",),
            candidate_source_path="fixture",
            score_valid=True,
            score_blocked_reason=None,
            web_only_score=None,
            web_only_score_valid=True,
            web_only_score_blocked_reason=None,
        )

        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "candidates.csv"
            json_path = Path(directory) / "candidates.json"
            asof_research_replay._write_candidates(csv_path, json_path, (row,))

            with csv_path.open(encoding="utf-8") as handle:
                csv_row = next(csv.DictReader(handle))
            json_row = json.loads(json_path.read_text(encoding="utf-8"))[0]

        self.assertEqual(csv_row["score"], "")
        self.assertEqual(csv_row["visible_score"], "")
        self.assertEqual(csv_row["score_valid"], "False")
        self.assertEqual(csv_row["score_blocked_reason"], "visible_score_missing")
        self.assertEqual(csv_row["web_only_score"], "")
        self.assertEqual(csv_row["web_only_score_valid"], "False")
        self.assertEqual(csv_row["web_only_score_blocked_reason"], "visible_score_missing")
        self.assertIsNone(json_row["score"])
        self.assertIsNone(json_row["visible_score"])
        self.assertFalse(json_row["score_valid"])
        self.assertEqual(json_row["score_blocked_reason"], "visible_score_missing")
        self.assertIsNone(json_row["web_only_score"])
        self.assertFalse(json_row["web_only_score_valid"])
        self.assertEqual(json_row["web_only_score_blocked_reason"], "visible_score_missing")
        self.assertEqual(score_state_contract_violations(json_row), ())

    def test_blind_candidate_csv_hides_invalid_compat_score(self):
        row = blind_discovery_replay.DiscoveredCandidate(
            symbol="000660",
            company_name="SK하이닉스",
            as_of_date=date(2026, 6, 12),
            layer="deep_research",
            stage=Stage.STAGE_2,
            rank=1,
            score=83.0,
            evidence_types_seen=("research_report",),
            reason_codes=("score_pending",),
            score_valid=False,
            score_blocked_reason="score_gap_unresolved",
        )

        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "candidates.csv"
            json_path = Path(directory) / "candidates.json"
            blind_discovery_replay._write_candidates(csv_path, json_path, (row,))

            with csv_path.open(encoding="utf-8") as handle:
                csv_row = next(csv.DictReader(handle))
            json_row = json.loads(json_path.read_text(encoding="utf-8"))[0]

        self.assertEqual(csv_row["score"], "")
        self.assertEqual(csv_row["visible_score"], "")
        self.assertIsNone(json_row["score"])
        self.assertIsNone(json_row["visible_score"])
        self.assertEqual(score_state_contract_violations(json_row), ())

    def test_blind_candidate_csv_uses_normalized_validity_when_visible_score_missing(self):
        row = blind_discovery_replay.DiscoveredCandidate(
            symbol="000660",
            company_name="SK하이닉스",
            as_of_date=date(2026, 6, 12),
            layer="deep_research",
            stage=Stage.STAGE_3_YELLOW,
            rank=1,
            score=None,
            evidence_types_seen=("research_report",),
            reason_codes=("fixture",),
            score_valid=True,
            score_blocked_reason=None,
        )

        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "candidates.csv"
            json_path = Path(directory) / "candidates.json"
            blind_discovery_replay._write_candidates(csv_path, json_path, (row,))

            with csv_path.open(encoding="utf-8") as handle:
                csv_row = next(csv.DictReader(handle))
            json_row = json.loads(json_path.read_text(encoding="utf-8"))[0]

        self.assertEqual(csv_row["score"], "")
        self.assertEqual(csv_row["visible_score"], "")
        self.assertEqual(csv_row["score_valid"], "False")
        self.assertEqual(csv_row["score_blocked_reason"], "visible_score_missing")
        self.assertIsNone(json_row["score"])
        self.assertIsNone(json_row["visible_score"])
        self.assertFalse(json_row["score_valid"])
        self.assertEqual(json_row["score_blocked_reason"], "visible_score_missing")
        self.assertEqual(score_state_contract_violations(json_row), ())


def _dataclass_fields_by_name(tree: ast.AST) -> dict[str, set[str]]:
    fields_by_name: dict[str, set[str]] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef) or not _is_dataclass(node):
            continue
        fields: set[str] = set()
        for statement in node.body:
            if isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name):
                fields.add(statement.target.id)
        fields_by_name[node.name] = fields
    return fields_by_name


def _is_dataclass(node: ast.ClassDef) -> bool:
    for decorator in node.decorator_list:
        if isinstance(decorator, ast.Name) and decorator.id == "dataclass":
            return True
        if isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name) and decorator.func.id == "dataclass":
            return True
    return False


if __name__ == "__main__":
    unittest.main()
