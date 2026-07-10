from __future__ import annotations

import hashlib
import io
import json
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

from e2r.cli.audit_e2r_evidence_intelligence import main as audit_cli_main
from e2r.cli.compile_e2r_research_intelligence import main as compile_cli_main
from e2r.cli.run_e2r_census_mode import main as census_cli_main
from e2r.cli.run_e2r_current_operation import main as current_cli_main
from e2r.cli.run_e2r_historical_replay import main as replay_cli_main
from e2r.production.metadata import stable_hash
from e2r.research_brain.replay import CanonicalFrozenReplayBundle
from e2r.research_brain.runtime import (
    DailyClaimProvenance,
    DailyProviderKind,
    REQUIRED_COMMAND_HASH_CATEGORIES,
    audit_command_run_manifest,
    build_command_run_manifest,
    command_file_hash_entry,
    command_inline_hash_entry,
    run_current_daily_census,
    run_independent_review,
    write_conversion_funnel,
)
from e2r.research_brain.runtime.independent_review import (
    review_corpus_fidelity,
    review_score_stage_integrity,
)
from tests import test_conversion_funnel_observability as funnel_fixture
from tests import test_current_operation_runner as current_fixture_module
from tests import test_historical_current_mode_separation as replay_fixture


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURE = (
    REPO_ROOT
    / "tests"
    / "fixtures"
    / "e2r_reconstruction"
    / "corpus"
    / "golden_mandatory_cases.md"
)
SOURCE_ROOT = (
    REPO_ROOT
    / "tests"
    / "fixtures"
    / "e2r_reconstruction"
    / "source_verification"
)


class CanonicalCommandManifestTest(unittest.TestCase):
    @staticmethod
    def _inline_inputs():
        return {
            category: (
                command_inline_hash_entry(
                    f"{category}-fixture", {"category": category, "value": 1}
                ),
            )
            for category in REQUIRED_COMMAND_HASH_CATEGORIES
        }

    def test_six_hashes_dirty_status_and_tamper_detection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source.json"
            source.write_text('{"source": 1}\n', encoding="utf-8")
            inputs = self._inline_inputs()
            inputs["source"] = (command_file_hash_entry("source-file", source),)
            manifest = build_command_run_manifest(
                command="phase16_test_command",
                semantic_status="PHASE16_COMMAND_PASS",
                exit_code=0,
                argv=("--fixture", "one"),
                output_root=root / "output",
                repo_root=REPO_ROOT,
                hash_inputs=inputs,
            )
            self.assertEqual(
                audit_command_run_manifest(manifest)["critical_count_sum"], 0
            )
            for category in REQUIRED_COMMAND_HASH_CATEGORIES:
                self.assertRegex(manifest[f"{category}_hash"], r"^[0-9a-f]{64}$")
            self.assertEqual(manifest["repo_dirty"], bool(manifest["dirty_paths"]))
            self.assertRegex(manifest["dirty_status_hash"], r"^[0-9a-f]{64}$")

            source.write_text('{"source": 2}\n', encoding="utf-8")
            tampered = audit_command_run_manifest(manifest)
            self.assertGreater(
                tampered["critical_counts"]["hash_entry_content_mismatch"], 0
            )

            overclaim = dict(manifest)
            overclaim["production_runtime_ready"] = True
            overclaim_audit = audit_command_run_manifest(overclaim)
            self.assertEqual(
                overclaim_audit["critical_counts"]["production_readiness_overclaim"],
                1,
            )

    def test_current_repository_state_change_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(
                ["git", "config", "user.email", "phase16@example.test"],
                cwd=repo,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Phase 16"], cwd=repo, check=True
            )
            tracked = repo / "tracked.txt"
            tracked.write_text("frozen\n", encoding="utf-8")
            subprocess.run(["git", "add", "tracked.txt"], cwd=repo, check=True)
            subprocess.run(
                ["git", "commit", "-q", "-m", "fixture"], cwd=repo, check=True
            )
            manifest = build_command_run_manifest(
                command="clean_fixture_command",
                semantic_status="CLEAN_FIXTURE_PASS",
                exit_code=0,
                argv=("--clean",),
                output_root=repo.parent / "outside-output",
                repo_root=repo,
                hash_inputs=self._inline_inputs(),
            )
            self.assertFalse(manifest["repo_dirty"])
            (repo / "untracked.txt").write_text("changed\n", encoding="utf-8")
            audit = audit_command_run_manifest(
                manifest, repo_root=repo, verify_current_repo_state=True
            )
            self.assertEqual(
                audit["critical_counts"]["current_repo_state_mismatch"], 1
            )


class Phase16RuntimeCommandsAndReviewersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls._tmp.name)
        cls.compile_root = cls.root / "compile"
        cls.replay_root = cls.root / "replay"
        cls.current_root = cls.root / "current"
        cls.census_root = cls.root / "census"
        cls.funnel_root = cls.root / "funnel"

        compile_stdout = io.StringIO()
        with redirect_stdout(compile_stdout):
            cls.compile_exit = compile_cli_main(
                [
                    "--repo-root",
                    str(REPO_ROOT),
                    "--output-root",
                    str(cls.compile_root),
                    "--input",
                    str(CORPUS_FIXTURE),
                    "--input",
                    str(SOURCE_ROOT / "golden_source_cases.jsonl"),
                    "--snapshot-registry",
                    str(SOURCE_ROOT / "provider_snapshots.jsonl"),
                    "--case-source-links",
                    str(SOURCE_ROOT / "case_source_links.jsonl"),
                    "--strict",
                    "true",
                ]
            )
        cls.compile_payload = json.loads(compile_stdout.getvalue())

        replay_fixture.HistoricalCurrentModeSeparationTest.setUpClass()
        phase11 = replay_fixture.HistoricalCurrentModeSeparationTest
        fixture_sha = hashlib.sha256(CORPUS_FIXTURE.read_bytes()).hexdigest()
        replay_bundle = CanonicalFrozenReplayBundle(
            result=phase11.historical,
            corpus_manifest={"critical_count_sum": 0, "fixture": "phase16"},
            source_manifest={
                **dict(phase11.phase5.source_result.manifest),
                "critical_count_sum": 0,
            },
            recipe_manifest=dict(phase11.phase5.recipe_result.manifest),
            memory_manifest=dict(phase11.phase5.memory_result.manifest),
            retrieval_manifest=dict(phase11.phase5.retrieval_audit.manifest),
            input_artifact_hashes=(
                {"source_path": str(CORPUS_FIXTURE), "sha256": fixture_sha},
            ),
        )
        replay_stdout = io.StringIO()
        with patch(
            "e2r.cli.run_e2r_historical_replay.compile_canonical_frozen_replay",
            return_value=replay_bundle,
        ), redirect_stdout(replay_stdout):
            cls.replay_exit = replay_cli_main(
                [
                    "--registry",
                    "canonical",
                    "--mode",
                    "blind_frozen_replay",
                    "--output-root",
                    str(cls.replay_root),
                    "--fail-on-critical",
                    "true",
                ]
            )
        cls.replay_payload = json.loads(replay_stdout.getvalue())

        current_fixture_module.CurrentOperationRunnerTest.setUpClass()
        current_fixture = current_fixture_module.CurrentOperationRunnerTest
        hard_break_ids = {
            claim_id
            for decision in current_fixture.decisions
            for claim_id in decision.hard_break_claim_ids
        }
        effective_claim_ids = {
            claim_id
            for decision in current_fixture.decisions
            for claim_id in (
                *decision.accepted_claim_ids,
                *decision.hard_break_claim_ids,
            )
        }
        claims = {item.claim_id: item for item in current_fixture.claims}
        provenance = []
        for claim_id in sorted(effective_claim_ids):
            claim = claims[claim_id]
            hard_break = claim_id in hard_break_ids
            quote = f"source-backed exact quote for {claim_id}"
            document_text = quote + "\nbounded provider fixture body"
            provenance.append(
                DailyClaimProvenance(
                    provenance_id="PROV-" + stable_hash(claim_id)[:24],
                    claim_id=claim_id,
                    target_id=claim.target_id,
                    document_id="DOC-" + stable_hash(claim_id)[:24],
                    source_url=(
                        "https://dart.fss.or.kr/dsaf001/main.do?rcpNo="
                        + stable_hash(claim_id)[:14]
                    ),
                    published_date=claim.observed_date,
                    available_date=claim.observed_date,
                    content_sha256=hashlib.sha256(
                        document_text.encode("utf-8")
                    ).hexdigest(),
                    document_text=document_text,
                    exact_quote=quote,
                    source_ids=claim.source_ids,
                    anchor_ids=claim.anchor_ids,
                    mapping_ids=claim.mapping_ids,
                    extraction_provider_kind=DailyProviderKind.CODEX.value,
                    mapping_provider_kind=DailyProviderKind.CODEX.value,
                    decision_use="HARD_BREAK" if hard_break else "SCORE",
                    mapping_status=(
                        "NOT_REQUIRED_HARD_BREAK" if hard_break else "ACCEPTED"
                    ),
                )
            )
        production_input = replace(
            current_fixture.inputs,
            config=replace(
                current_fixture.config,
                test_mode=False,
                require_claim_provenance=True,
            ),
            source_tasks=tuple(
                replace(item, test_only=False)
                for item in current_fixture.source_tasks
            ),
            deep_executions=tuple(
                replace(
                    item,
                    provider_kind=(
                        DailyProviderKind.CODEX.value
                        if item.llm_calls
                        else DailyProviderKind.NONE.value
                    ),
                )
                for item in current_fixture.executions
            ),
            claim_provenance=tuple(provenance),
        )
        # The direct run proves the input is internally valid before exercising
        # both public facades. It still cannot declare global runtime readiness.
        cls.production_result = run_current_daily_census(production_input)
        cls.input_path = cls.root / "current_input.json"
        cls.input_path.write_text(
            json.dumps(production_input.to_dict(), ensure_ascii=False),
            encoding="utf-8",
        )
        current_stdout = io.StringIO()
        with redirect_stdout(current_stdout):
            cls.current_exit = current_cli_main(
                [
                    "--as-of-date",
                    current_fixture.as_of_date,
                    "--mode",
                    "production_bounded",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(cls.current_root),
                    "--input-manifest",
                    str(cls.input_path),
                    "--fail-on-critical",
                    "true",
                ]
            )
        cls.current_payload = json.loads(current_stdout.getvalue())
        census_stdout = io.StringIO()
        with redirect_stdout(census_stdout):
            cls.census_exit = census_cli_main(
                [
                    "--as-of-date",
                    current_fixture.as_of_date,
                    "--mode",
                    "census_selective_deep",
                    "--brain",
                    "canonical_v1",
                    "--output-root",
                    str(cls.census_root),
                    "--input-manifest",
                    str(cls.input_path),
                    "--fail-on-critical",
                    "true",
                ]
            )
        cls.census_payload = json.loads(census_stdout.getvalue())

        funnel_fixture.ConversionFunnelObservabilityTest.setUpClass()
        write_conversion_funnel(
            funnel_fixture.ConversionFunnelObservabilityTest.result,
            output_root=cls.funnel_root,
        )
        cls.review = run_independent_review(
            compile_root=cls.compile_root,
            replay_root=cls.replay_root,
            current_root=cls.current_root,
            repo_root=REPO_ROOT,
            funnel_root=cls.funnel_root,
            require_live_current=True,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def test_four_canonical_facades_emit_reproducible_command_manifests(self) -> None:
        self.assertEqual(
            (self.compile_exit, self.replay_exit, self.current_exit, self.census_exit),
            (0, 0, 0, 0),
        )
        expected = {
            "compile": (
                self.compile_root,
                "compile_e2r_research_intelligence",
                "COMPILE_RUN_PASS",
            ),
            "replay": (
                self.replay_root,
                "run_e2r_historical_replay",
                "HISTORICAL_REPLAY_PARITY_PASS",
            ),
            "current": (
                self.current_root,
                "run_e2r_current_operation",
                "CURRENT_OPERATIONAL_BRAIN_PASS",
            ),
            "census": (
                self.census_root,
                "run_e2r_census_mode",
                "CURRENT_OPERATIONAL_BRAIN_PASS",
            ),
        }
        for name, (root, command, status) in expected.items():
            with self.subTest(name=name):
                manifest = json.loads(
                    (root / "command_run_manifest.json").read_text(encoding="utf-8")
                )
                self.assertEqual(manifest["command"], command)
                self.assertEqual(manifest["semantic_status"], status)
                self.assertEqual(
                    audit_command_run_manifest(manifest)["critical_count_sum"], 0
                )
                for category in REQUIRED_COMMAND_HASH_CATEGORIES:
                    self.assertRegex(
                        manifest[f"{category}_hash"], r"^[0-9a-f]{64}$"
                    )

    def test_current_and_census_use_same_canonical_leaf_result(self) -> None:
        self.assertTrue(self.production_result.manifest["live_execution_observed"])
        self.assertFalse(self.production_result.production_runtime_ready)
        self.assertEqual(
            self.current_payload["run_id"], self.census_payload["run_id"]
        )
        self.assertEqual(
            self.current_payload["command"], "run_e2r_current_operation"
        )
        self.assertEqual(self.census_payload["command"], "run_e2r_census_mode")
        for filename in (
            "current_daily_universe.jsonl",
            "current_daily_claim_provenance.jsonl",
            "current_daily_source_timelines.jsonl",
            "current_daily_atomic_decisions.jsonl",
            "current_daily_census_stage_statuses.jsonl",
        ):
            self.assertEqual(
                (self.current_root / filename).read_bytes(),
                (self.census_root / filename).read_bytes(),
            )

    def test_reviewers_a_to_e_independently_pass_from_leaf_artifacts(self) -> None:
        self.assertEqual(self.review.status, "INDEPENDENT_E2R_REVIEW_PASS")
        self.assertEqual(self.review.critical_count_sum, 0)
        self.assertEqual(
            tuple(item.reviewer_id for item in self.review.reviewers),
            ("A", "B", "C", "D", "E"),
        )
        self.assertTrue(all(item.verdict == "PASS" for item in self.review.reviewers))
        self.assertEqual(
            len({item.result_hash for item in self.review.reviewers}), 5
        )

    def test_reviewers_ignore_summary_counters_but_fail_on_mutated_leaves(self) -> None:
        compile_manifest = self.compile_root / "compile_manifest.json"
        original_summary = compile_manifest.read_text(encoding="utf-8")
        compile_manifest.write_text(
            json.dumps({"historical_case_count": 999999, "critical_count_sum": 0}),
            encoding="utf-8",
        )
        try:
            self.assertEqual(
                review_corpus_fidelity(
                    compile_root=self.compile_root, repo_root=REPO_ROOT
                ).verdict,
                "PASS",
            )
        finally:
            compile_manifest.write_text(original_summary, encoding="utf-8")

        case_path = self.compile_root / "corpus" / "historical_cases.jsonl"
        original_cases = case_path.read_text(encoding="utf-8")
        rows = [json.loads(line) for line in original_cases.splitlines() if line]
        rows[0]["runtime_score_eligible"] = True
        case_path.write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in rows) + "\n",
            encoding="utf-8",
        )
        try:
            reviewer_a = review_corpus_fidelity(
                compile_root=self.compile_root, repo_root=REPO_ROOT
            )
            self.assertEqual(reviewer_a.verdict, "FAIL")
            self.assertGreater(reviewer_a.critical_counts["case_runtime_score_leak"], 0)
        finally:
            case_path.write_text(original_cases, encoding="utf-8")

        status_path = (
            self.current_root / "current_daily_census_stage_statuses.jsonl"
        )
        original_statuses = status_path.read_text(encoding="utf-8")
        statuses = [
            json.loads(line) for line in original_statuses.splitlines() if line
        ]
        statuses[0]["canonical_stage"] = "FAKE-STAGE"
        status_path.write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in statuses)
            + "\n",
            encoding="utf-8",
        )
        try:
            reviewer_d = review_score_stage_integrity(
                current_root=self.current_root
            )
            self.assertEqual(reviewer_d.verdict, "FAIL")
            self.assertGreater(reviewer_d.critical_counts["noncanonical_stage"], 0)
        finally:
            status_path.write_text(original_statuses, encoding="utf-8")

        watchlist_path = self.current_root / "current_daily_watchlist.jsonl"
        original_watchlist = watchlist_path.read_text(encoding="utf-8")
        watchlist = [
            json.loads(line) for line in original_watchlist.splitlines() if line
        ]
        watchlist[0]["raw_reference_score"] = 999.0
        watchlist_path.write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in watchlist)
            + "\n",
            encoding="utf-8",
        )
        try:
            reviewer_d = review_score_stage_integrity(
                current_root=self.current_root
            )
            self.assertEqual(reviewer_d.verdict, "FAIL")
            self.assertGreater(
                reviewer_d.critical_counts["watchlist_projection_mismatch"], 0
            )
        finally:
            watchlist_path.write_text(original_watchlist, encoding="utf-8")

    def test_production_cli_rejects_tampered_or_nonlive_provenance(self) -> None:
        mutations = {
            "content_tamper": lambda item: item.__setitem__(
                "document_text", item["document_text"] + " tampered"
            ),
            "snapshot_url": lambda item: item.__setitem__(
                "source_url", "snapshot://fixture/document"
            ),
            "available_before_published": lambda item: item.__setitem__(
                "available_date", "1900-01-01"
            ),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                payload = json.loads(self.input_path.read_text(encoding="utf-8"))
                mutate(payload["claim_provenance"][0])
                bad_input = self.root / f"bad_current_input_{name}.json"
                bad_input.write_text(
                    json.dumps(payload, ensure_ascii=False), encoding="utf-8"
                )
                stream = io.StringIO()
                with redirect_stdout(stream):
                    code = current_cli_main(
                        [
                            "--as-of-date",
                            current_fixture_module.CurrentOperationRunnerTest.as_of_date,
                            "--mode",
                            "production_bounded",
                            "--output-root",
                            str(self.root / f"bad-current-{name}"),
                            "--input-manifest",
                            str(bad_input),
                        ]
                    )
                self.assertEqual(code, 2)
                self.assertEqual(
                    json.loads(stream.getvalue())["status"],
                    "CURRENT_OPERATION_INPUT_REJECTED",
                )

    def test_missing_live_input_becomes_external_pending_with_hashes(self) -> None:
        for command, output in (
            (current_cli_main, self.root / "pending-current"),
            (census_cli_main, self.root / "pending-census"),
        ):
            args = [
                "--as-of-date",
                "2099-01-01",
                "--output-root",
                str(output),
            ]
            if command is current_cli_main:
                args.extend(("--mode", "production_bounded"))
            else:
                args.extend(
                    (
                        "--mode",
                        "census_selective_deep",
                        "--brain",
                        "canonical_v1",
                    )
                )
            stream = io.StringIO()
            with redirect_stdout(stream):
                code = command(args)
            payload = json.loads(stream.getvalue())
            self.assertEqual(code, 3)
            self.assertEqual(payload["status"], "EXTERNAL_SOURCE_BLOCKER_NOT_READY")
            manifest = json.loads(
                (output / "command_run_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                audit_command_run_manifest(manifest)["critical_count_sum"], 0
            )

    def test_final_audit_cannot_be_ready_when_live_requirement_is_disabled(self) -> None:
        stream = io.StringIO()
        with redirect_stdout(stream):
            code = audit_cli_main(
                [
                    "--repo-root",
                    str(REPO_ROOT),
                    "--compile-root",
                    str(self.compile_root),
                    "--replay-root",
                    str(self.replay_root),
                    "--current-root",
                    str(self.current_root),
                    "--census-root",
                    str(self.census_root),
                    "--funnel-root",
                    str(self.funnel_root),
                    "--output-root",
                    str(self.root / "final-audit"),
                    "--require-live-current",
                    "false",
                    "--fail-on-critical",
                    "true",
                ]
            )
        payload = json.loads(stream.getvalue())
        self.assertEqual(code, 2)
        self.assertEqual(payload["status"], "INTERNAL_E2R_RUNTIME_NOT_READY")
        self.assertFalse(payload["production_runtime_ready"])
        self.assertEqual(
            payload["critical_counts"]["live_current_requirement_disabled"], 1
        )


if __name__ == "__main__":
    unittest.main()
