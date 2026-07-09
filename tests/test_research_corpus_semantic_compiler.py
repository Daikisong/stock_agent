from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from e2r.cli.compile_e2r_research_intelligence import main as compile_cli_main
from e2r.research_brain.compiler import compile_research_intelligence
from e2r.research_brain.corpus import parse_historical_research_artifact
from e2r.research_brain.intelligence_schema import ParsedRowKind, QuarantineReason


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"


class ResearchCorpusSemanticCompilerTest(unittest.TestCase):
    def _write(self, directory: str, name: str, text: str) -> Path:
        path = Path(directory) / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_structured_formats_have_explicit_precedence_and_line_ranges(self) -> None:
        markdown = """---
fixture: precedence
---

```json
{"row_type":"case","case_id":"JSON_CASE","symbol":"100001","company_name":"JSON Co","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_date":"2020-01-01"}
```

```jsonl
{"row_type":"case","case_id":"JSONL_CASE","symbol":"100002","company_name":"JSONL Co","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","trigger_date":"2020-01-02"}
```

```csv
row_type,case_id,symbol,company_name,canonical_archetype_id,trigger_date
case,CSV_CASE,100003,CSV Co,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,2020-01-03
```

| row_type | case_id | symbol | company_name | canonical_archetype_id | trigger_date |
|---|---|---|---|---|---|
| case | TABLE_CASE | 100004 | Table Co | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 2020-01-04 |

This narrative paragraph is deliberately long enough to become a parsed narrative row.
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(tmp, "precedence.md", markdown)
            parsed = parse_historical_research_artifact(path)

        by_kind = {row.row_kind: row for row in parsed.rows}
        expected = {
            ParsedRowKind.YAML_FRONT_MATTER.value: 1,
            ParsedRowKind.FENCED_JSON.value: 2,
            ParsedRowKind.FENCED_JSONL.value: 3,
            ParsedRowKind.FENCED_CSV.value: 4,
            ParsedRowKind.MARKDOWN_TABLE.value: 5,
            ParsedRowKind.NARRATIVE.value: 6,
        }
        for kind, precedence in expected.items():
            self.assertIn(kind, by_kind)
            self.assertEqual(by_kind[kind].precedence, precedence)
            self.assertGreaterEqual(by_kind[kind].source_line_range.start, 1)
            self.assertGreaterEqual(
                by_kind[kind].source_line_range.end,
                by_kind[kind].source_line_range.start,
            )

    def test_case_after_24000_bytes_is_not_truncated(self) -> None:
        late_case = {
            "row_type": "case",
            "case_id": "LATE_CASE",
            "symbol": "100005",
            "company_name": "Late Company",
            "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
            "trigger_date": "2020-01-05",
        }
        text = "# Long research\n\n" + ("x" * 30000) + "\n\n```jsonl\n" + json.dumps(late_case) + "\n```\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(tmp, "long.md", text)
            result = compile_research_intelligence([path])

        self.assertEqual([case.case_id for case in result.cases], ["LATE_CASE"])
        self.assertIsNone(result.manifest["quality"]["source_text_truncation_limit"])

    def test_score_rule_and_transition_link_even_when_they_precede_trigger(self) -> None:
        rows = [
            {
                "row_type": "score_simulation",
                "case_id": "ORDER_CASE",
                "trigger_id": "ORDER_T01_FULL",
                "MFE_90D_pct": 12.5,
                "stage_label_after": "Stage2",
            },
            {
                "row_type": "shadow_weight",
                "trigger_ids": "ORDER_T01",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            },
            {
                "row_type": "stage_transition_summary",
                "symbol": "100006",
                "entry_date": "2020-01-06",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            },
            {
                "row_type": "case",
                "case_id": "ORDER_CASE",
                "symbol": "100006",
                "company_name": "Order Company",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_date": "2020-01-06",
                "entry_date": "2020-01-06",
            },
            {
                "row_type": "trigger",
                "case_id": "ORDER_CASE",
                "trigger_id": "ORDER_T01_FULL",
                "symbol": "100006",
                "company_name": "Order Company",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_date": "2020-01-06",
                "entry_date": "2020-01-06",
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(tmp, "order.jsonl", "\n".join(json.dumps(row) for row in rows) + "\n")
            result = compile_research_intelligence([path])

        case = result.cases[0]
        self.assertEqual(len(case.score_simulation_refs), 1)
        self.assertGreaterEqual(len(case.shadow_rule_refs), 1)
        self.assertEqual(len(case.transition_refs), 1)
        self.assertEqual(len(result.linkage_errors), 0)
        self.assertTrue(result.outcomes)
        self.assertTrue(all(outcome.evaluator_only for outcome in result.outcomes))
        self.assertTrue(all(not outcome.runtime_prompt_allowed for outcome in result.outcomes))
        self.assertTrue(all(not outcome.runtime_score_eligible for outcome in result.outcomes))

    def test_trigger_only_rows_create_distinct_cases_without_first_symbol_collapse(self) -> None:
        rows = [
            {
                "row_type": "trigger",
                "symbol": "100061",
                "name": "Trigger Only A",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "entry_date": "2020-06-01",
                "trigger_type": "capacity_signal",
                "evidence_url_pending": True,
            },
            {
                "row_type": "trigger",
                "symbol": "100062",
                "name": "Trigger Only B",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "entry_date": "2020-06-02",
                "trigger_type": "customer_signal",
                "evidence_url_pending": True,
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(
                tmp,
                "trigger_only.jsonl",
                "\n".join(json.dumps(row) for row in rows) + "\n",
            )
            result = compile_research_intelligence([path])

        self.assertEqual(len(result.cases), 2)
        self.assertEqual({case.symbol for case in result.cases}, {"100061", "100062"})
        self.assertTrue(
            all(case.compiler_origin == "STRUCTURED_TRIGGER_SYNTHESIS" for case in result.cases)
        )
        self.assertEqual(result.manifest["quality"]["first_symbol_collapse_count"], 0)

    def test_multiple_trigger_dates_remain_linked_without_false_date_loss(self) -> None:
        rows = [
            {
                "row_type": "case",
                "case_id": "MULTI_DATE_CASE",
                "symbol": "100063",
                "company_name": "Multi Date Company",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_date": "2020-06-03",
            },
            {
                "row_type": "trigger",
                "case_id": "MULTI_DATE_CASE",
                "trigger_id": "MULTI_DATE_T01",
                "symbol": "100063",
                "company_name": "Multi Date Company",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_date": "2020-06-03",
                "entry_date": "2020-06-03",
            },
            {
                "row_type": "trigger",
                "case_id": "MULTI_DATE_CASE",
                "trigger_id": "MULTI_DATE_T02",
                "symbol": "100063",
                "company_name": "Multi Date Company",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_date": "2020-07-03",
                "entry_date": "2020-07-03",
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(
                tmp,
                "multi_date.jsonl",
                "\n".join(json.dumps(row) for row in rows) + "\n",
            )
            result = compile_research_intelligence([path])

        self.assertEqual(result.cases[0].trigger_date, "2020-06-03")
        self.assertEqual(len(result.cases[0].trigger_refs), 2)
        self.assertEqual(result.manifest["quality"]["present_trigger_date_loss_count"], 0)

    def test_malformed_and_conflicting_rows_are_quarantined_without_silent_overwrite(self) -> None:
        valid_a = {
            "row_type": "case",
            "case_id": "DUPLICATE_CASE",
            "symbol": "100007",
            "company_name": "First Company",
            "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
            "trigger_date": "2020-01-07",
        }
        valid_b = dict(valid_a, company_name="Conflicting Company")
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(
                tmp,
                "conflict.jsonl",
                json.dumps(valid_a) + "\n{malformed json\n" + json.dumps(valid_b) + "\n",
            )
            result = compile_research_intelligence([path])

        reasons = {item.reason for item in result.quarantine}
        self.assertIn(QuarantineReason.MALFORMED_STRUCTURED_ROW.value, reasons)
        self.assertIn(QuarantineReason.CONFLICTING_DUPLICATE.value, reasons)
        self.assertTrue(result.linkage_errors)
        self.assertEqual(result.cases[0].company_name, "First Company")
        self.assertEqual(result.manifest["quality"]["silent_duplicate_overwrite_count"], 0)
        self.assertEqual(result.manifest["quality"]["structured_jsonl_row_preservation_rate"], 1.0)

    def test_narrative_fallback_never_promotes_llm_candidate_to_case(self) -> None:
        text = (
            "# Narrative only\n\n"
            "이 문단은 충분히 길지만 machine-readable case row는 없으며 LLM 검토 대상으로만 남아야 합니다.\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(tmp, "narrative.md", text)
            without_provider = compile_research_intelligence([path])
            with_provider = compile_research_intelligence(
                [path],
                narrative_case_provider=lambda artifact, rows: [
                    {
                        "case_id": "LLM_GUESS",
                        "uncertainty": ["no_source"],
                        "score": 99,
                        "stage": "3-Green",
                    }
                ],
            )

        self.assertFalse(without_provider.cases)
        self.assertIn(
            QuarantineReason.NARRATIVE_REQUIRES_LLM.value,
            {item.reason for item in without_provider.quarantine},
        )
        self.assertFalse(with_provider.cases)
        self.assertIn(
            QuarantineReason.LLM_DERIVED_UNVERIFIED.value,
            {item.reason for item in with_provider.quarantine},
        )
        candidate_record = next(
            item
            for item in with_provider.quarantine
            if item.reason == QuarantineReason.LLM_DERIVED_UNVERIFIED.value
        )
        candidate = candidate_record.details["candidate"]
        self.assertFalse(candidate["verified"])
        self.assertFalse(candidate["runtime_score_eligible"])
        self.assertNotIn("score", candidate["payload"])
        self.assertNotIn("stage", candidate["payload"])
        self.assertEqual(
            candidate_record.details["prohibited_output_fields_removed"],
            ["score", "stage"],
        )

    def test_official_compile_cli_writes_canonical_corpus_outputs(self) -> None:
        fixture = FIXTURE_ROOT / "golden_mandatory_cases.md"
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "compiled"
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = compile_cli_main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--input",
                        str(fixture),
                        "--output-root",
                        str(output_root),
                        "--strict",
                        "true",
                    ]
                )
            payload = json.loads(stdout.getvalue())

            self.assertEqual(exit_code, 0)
            self.assertEqual(payload["status"], "RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS")
            self.assertEqual(payload["historical_case_count"], 6)
            self.assertTrue((output_root / "compile_manifest.json").is_file())
            self.assertTrue((output_root / "compile_report.md").is_file())
            self.assertTrue((output_root / "corpus" / "historical_cases.jsonl").is_file())
            self.assertTrue((output_root / "corpus" / "historical_outcomes.jsonl").is_file())
            self.assertTrue((output_root / "corpus" / "historical_rules.jsonl").is_file())
            self.assertTrue((output_root / "corpus" / "quarantine.jsonl").is_file())
            self.assertTrue((output_root / "corpus" / "linkage_errors.jsonl").is_file())


if __name__ == "__main__":
    unittest.main()
