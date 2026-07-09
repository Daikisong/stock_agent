from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from dataclasses import replace
from pathlib import Path

from e2r.cli.compile_e2r_research_intelligence import main as compile_cli_main
from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
    write_case_level_source_verification,
)
from e2r.research_brain.intelligence_schema import (
    HistoricalCaseSourceRelationship,
    HistoricalSnapshotAnchor,
    HistoricalSourceState,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURES = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"
SOURCE_FIXTURES = (
    REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "source_verification"
)


class CaseLevelSourceVerificationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        compilation = compile_research_intelligence(
            [SOURCE_FIXTURES / "golden_source_cases.jsonl"],
            repo_root=REPO_ROOT,
        )
        cls.cases = compilation.cases
        cls.case_by_id = {case.case_id: case for case in cls.cases}
        cls.snapshots = load_historical_provider_snapshots(
            SOURCE_FIXTURES / "provider_snapshots.jsonl"
        )
        cls.links = load_historical_case_source_links(
            SOURCE_FIXTURES / "case_source_links.jsonl"
        )

    def _compile(self, *, snapshots=None, links=None):
        return compile_case_level_source_verification(
            self.cases,
            snapshots=self.snapshots if snapshots is None else snapshots,
            case_source_links=self.links if links is None else links,
            repo_root=REPO_ROOT,
            url_backed_golden_case_ids={
                "PHASE3_C15_HYUNDAI_READY",
                "PHASE3_C15_WRONG_SUBJECT",
                "PHASE3_C15_FUTURE_DATE",
                "PHASE3_URL_STRING_ONLY",
            },
            source_proxy_golden_case_ids={
                "PHASE3_SOURCE_PROXY",
                "PHASE3_EVIDENCE_PENDING",
            },
        )

    def test_canonical_source_state_enum_is_exact(self) -> None:
        self.assertEqual(
            {item.value for item in HistoricalSourceState},
            {
                "SOURCE_PROXY_ONLY",
                "EVIDENCE_URL_PENDING",
                "URL_PRESENT_UNVERIFIED",
                "URL_FETCH_FAILED",
                "URL_FETCHED_NO_ANCHOR",
                "URL_FETCHED_WRONG_SUBJECT",
                "URL_FETCHED_DATE_INVALID",
                "URL_FETCHED_ANCHORED",
                "URL_FETCHED_ANCHORED_CASE_MATCH",
                "HISTORICAL_REPLAY_READY",
            },
        )

    def test_happy_path_and_adversarial_states_are_separated(self) -> None:
        result = self._compile()
        by_case = {row.case_id: row for row in result.verifications}

        ready = by_case["PHASE3_C15_HYUNDAI_READY"]
        self.assertEqual(ready.source_state, "HISTORICAL_REPLAY_READY")
        self.assertTrue(ready.historical_replay_ready)
        self.assertTrue(ready.a2_historical_evidence_eligible)
        self.assertTrue(all(ready.checks.values()))
        self.assertEqual(
            ready.content_sha256,
            "93021bbf3942eb46673eef23497ac0469c188f1dfd273145cb19e2da874b96db",
        )
        self.assertFalse(ready.current_score_eligible)
        self.assertTrue(ready.evaluator_only)

        self.assertEqual(
            by_case["PHASE3_C15_WRONG_SUBJECT"].source_state,
            "URL_FETCHED_WRONG_SUBJECT",
        )
        self.assertEqual(
            by_case["PHASE3_C15_FUTURE_DATE"].source_state,
            "URL_FETCHED_DATE_INVALID",
        )
        self.assertEqual(
            by_case["PHASE3_URL_STRING_ONLY"].source_state,
            "URL_PRESENT_UNVERIFIED",
        )
        self.assertEqual(
            by_case["PHASE3_SOURCE_PROXY"].source_state,
            "SOURCE_PROXY_ONLY",
        )
        self.assertEqual(
            by_case["PHASE3_EVIDENCE_PENDING"].source_state,
            "EVIDENCE_URL_PENDING",
        )
        self.assertEqual(
            result.manifest["status"],
            "CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_PASS",
        )
        self.assertEqual(result.manifest["critical_count_sum"], 0)
        self.assertEqual(result.manifest["historical_replay_ready_count"], 1)
        self.assertTrue(all(task.planning_only for task in result.repair_tasks))
        self.assertTrue(all(not task.current_score_eligible for task in result.repair_tasks))

    def test_content_hash_mismatch_is_fetch_failure(self) -> None:
        bad_snapshot = replace(self.snapshots[0], content_sha256="0" * 64)
        result = self._compile(snapshots=(bad_snapshot,))
        verification = next(
            row for row in result.verifications if row.case_id == "PHASE3_C15_HYUNDAI_READY"
        )
        self.assertEqual(verification.source_state, "URL_FETCH_FAILED")
        self.assertEqual(verification.blocker_code, "CONTENT_HASH_MISMATCH")
        self.assertFalse(verification.historical_replay_ready)

    def test_exact_anchor_and_semantic_link_are_both_required(self) -> None:
        without_link = self._compile(links=())
        verification = next(
            row
            for row in without_link.verifications
            if row.case_id == "PHASE3_C15_HYUNDAI_READY"
        )
        self.assertEqual(verification.source_state, "URL_FETCHED_ANCHORED")
        self.assertEqual(verification.blocker_code, "CASE_SEMANTIC_LINK_MISSING")

        invalid_anchor = HistoricalSnapshotAnchor(
            anchor_id="PHASE3_ANCHOR_C15_PRICE_HIKE",
            locator="text:missing",
            exact_text="This sentence is not in the captured source.",
        )
        bad_snapshot = replace(self.snapshots[0], anchors=(invalid_anchor,))
        without_anchor = self._compile(snapshots=(bad_snapshot,))
        verification = next(
            row
            for row in without_anchor.verifications
            if row.case_id == "PHASE3_C15_HYUNDAI_READY"
        )
        self.assertEqual(verification.source_state, "URL_FETCHED_NO_ANCHOR")
        self.assertEqual(verification.blocker_code, "EXACT_ANCHOR_MISSING_OR_INVALID")

    def test_summary_contradiction_and_unrelated_link_never_become_ready(self) -> None:
        ready_link = next(
            link for link in self.links if link.case_id == "PHASE3_C15_HYUNDAI_READY"
        )
        contradiction = replace(ready_link, summary_consistent=False)
        result = self._compile(links=(contradiction,))
        verification = next(
            row for row in result.verifications if row.case_id == "PHASE3_C15_HYUNDAI_READY"
        )
        self.assertEqual(verification.source_state, "URL_FETCHED_ANCHORED_CASE_MATCH")
        self.assertEqual(verification.blocker_code, "CASE_SUMMARY_SOURCE_CONTRADICTION")

        unrelated = replace(
            ready_link,
            relationship=HistoricalCaseSourceRelationship.UNRELATED.value,
        )
        result = self._compile(links=(unrelated,))
        verification = next(
            row for row in result.verifications if row.case_id == "PHASE3_C15_HYUNDAI_READY"
        )
        self.assertEqual(verification.source_state, "URL_FETCHED_ANCHORED")
        self.assertEqual(verification.blocker_code, "CASE_SEMANTIC_MATCH_FAILED")

    def test_official_document_id_can_replace_url_when_all_other_checks_pass(self) -> None:
        row = {
            "row_type": "case",
            "case_id": "PHASE3_OFFICIAL_DOCUMENT_ID",
            "symbol": "004020",
            "company_name": "Hyundai Steel",
            "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
            "trigger_date": "2021-04-27",
            "document_id": "OFFICIAL-DOC-004020-20210427",
            "evidence_summary": "Product price hikes improved quarterly profit.",
        }
        with tempfile.TemporaryDirectory() as tmp:
            case_path = Path(tmp) / "case.jsonl"
            case_path.write_text(json.dumps(row) + "\n", encoding="utf-8")
            case = compile_research_intelligence([case_path]).cases[0]

        snapshot = replace(
            self.snapshots[0],
            snapshot_id="PHASE3_SNAPSHOT_OFFICIAL_DOCUMENT_ID",
            canonical_url=None,
            official_document_id="OFFICIAL-DOC-004020-20210427",
        )
        link = replace(
            next(link for link in self.links if link.case_id == "PHASE3_C15_HYUNDAI_READY"),
            link_id="PHASE3_LINK_OFFICIAL_DOCUMENT_ID",
            case_id=case.case_id,
            snapshot_id=snapshot.snapshot_id,
        )
        result = compile_case_level_source_verification(
            [case],
            snapshots=[snapshot],
            case_source_links=[link],
            repo_root=REPO_ROOT,
        )
        verification = result.verifications[0]
        self.assertEqual(verification.source_state, "HISTORICAL_REPLAY_READY")
        self.assertIsNone(verification.source_url)
        self.assertEqual(
            verification.official_document_id,
            "OFFICIAL-DOC-004020-20210427",
        )

    def test_mandatory_phase2_golden_cases_are_ready_or_have_exact_blockers(self) -> None:
        compilation = compile_research_intelligence(
            [CORPUS_FIXTURES / "golden_mandatory_cases.md"],
            repo_root=REPO_ROOT,
        )
        by_archetype = {
            case.canonical_archetype_id: case.case_id for case in compilation.cases
        }
        result = compile_case_level_source_verification(
            compilation.cases,
            repo_root=REPO_ROOT,
            url_backed_golden_case_ids={
                by_archetype["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
                by_archetype["C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"],
                by_archetype["C15_MATERIAL_SPREAD_SUPERCYCLE"],
            },
            source_proxy_golden_case_ids={
                by_archetype["C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"],
                by_archetype["C24_BIO_TRIAL_DATA_EVENT_RISK"],
                by_archetype["C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"],
            },
        )

        self.assertEqual(result.manifest["critical_count_sum"], 0)
        self.assertEqual(result.manifest["historical_replay_ready_count"], 0)
        self.assertEqual(len(result.repair_tasks), 6)
        self.assertTrue(
            all(status["exact_blockers"] for status in result.case_statuses)
        )

    def test_writer_and_official_cli_emit_source_verification_outputs(self) -> None:
        result = self._compile()
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_case_level_source_verification(result, output_root=tmp)
            self.assertTrue(paths["manifest"].is_file())
            self.assertTrue(paths["replay_ready"].is_file())
            ready_rows = [
                json.loads(line)
                for line in paths["replay_ready"].read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertEqual(len(ready_rows), 1)

            cli_output = Path(tmp) / "cli"
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = compile_cli_main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--input",
                        str(SOURCE_FIXTURES / "golden_source_cases.jsonl"),
                        "--output-root",
                        str(cli_output),
                        "--snapshot-registry",
                        str(SOURCE_FIXTURES / "provider_snapshots.jsonl"),
                        "--case-source-links",
                        str(SOURCE_FIXTURES / "case_source_links.jsonl"),
                        "--strict",
                        "true",
                    ]
                )
            payload = json.loads(stdout.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(
                payload["source_verification_status"],
                "CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_PASS",
            )
            self.assertEqual(payload["historical_replay_ready_count"], 1)
            self.assertTrue(
                (cli_output / "source_verification" / "source_verification_manifest.json").is_file()
            )


if __name__ == "__main__":
    unittest.main()
