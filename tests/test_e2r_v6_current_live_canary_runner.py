from __future__ import annotations

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from e2r.production import v6_current_live_canary_runner as phase106_runner_module
from e2r.cli.run_e2r_v6_current_live_canaries_until_pass import (
    _load_inputs,
    main as phase106_cli_main,
)
from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_compact_receipt import (
    RECEIPT_MANIFEST_NAME,
    REQUIRED_ARTIFACT_NAMES,
    REVIEW_DIRECTORY_NAME,
    REVIEW_NAMES,
    build_selection_bound_canary_manifest,
    export_selection_bound_canary_bundle,
)
from e2r.production.v6_current_live_canary_runner import (
    PHASE106_RUN_PASS,
    PHASE106_RUN_PENDING,
    PHASE106_RESUME_BINDING_SCHEMA,
    PHASE106_TERMINAL_RESEARCH_STATUS,
    V6CurrentLiveCanaryRunner,
    _write_phase106_resume_binding,
)
from e2r.production.v6_canary_selection import (
    ISSUER_PROFILE_MANIFEST_NAME,
    compile_cross_archetype_canary_selection,
    seal_cross_archetype_canary_selection,
    seal_current_issuer_business_profile_manifest,
)
from e2r.production.v6_operational_acceptance import _command_attempt
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexSubagentTransport,
)
from tests.test_e2r_v6_canary_compact_receipt import (
    REPO_ROOT,
    _artifacts,
    _reviews,
    _selection,
    _write_terminal_output,
)
from tests import test_e2r_v6_canary_selection as selection_fixtures


class _PendingCheckpointRunner:
    def __init__(self, calls: list[str]) -> None:
        self.calls = calls

    def run_checkpoint(self, *, config, target, repo_root, source_resume_mode):
        self.calls.append(target.target_id)
        target_root = Path(config.output_root) / target.target_id
        transport = CollaborationCodexSubagentTransport()
        transport.configure_journal_root(
            target_root / "collaboration_codex_subagent_provider"
        )
        transport.complete(
            prompt=f"research {target.target_id}",
            output_schema={
                "type": "object",
                "additionalProperties": False,
                "required": ["ok"],
                "properties": {"ok": {"type": "boolean"}},
            },
            schema_name="e2r_v5_phase106_test",
        )
        raise AssertionError("transport must stop on its exact pending request")


class _HistoricalThenActivePendingCheckpointRunner:
    """Leave one immutable old request, then stop on a distinct current one."""

    def __init__(self, calls: list[str]) -> None:
        self.calls = calls
        self.historical_request_id: str | None = None
        self.active_request_id: str | None = None

    def run_checkpoint(self, *, config, target, repo_root, source_resume_mode):
        self.calls.append(target.target_id)
        target_root = Path(config.output_root) / target.target_id
        transport = CollaborationCodexSubagentTransport()
        transport.configure_journal_root(
            target_root / "collaboration_codex_subagent_provider"
        )
        schema = {
            "type": "object",
            "additionalProperties": False,
            "required": ["ok"],
            "properties": {"ok": {"type": "boolean"}},
        }
        try:
            transport.complete(
                prompt=f"historical research {target.target_id}",
                output_schema=schema,
                schema_name="e2r_v5_phase106_historical_test",
            )
        except StructuredProviderUnavailable as exc:
            self.historical_request_id = str(exc).rsplit(":", 1)[-1]
        try:
            transport.complete(
                prompt=f"active research {target.target_id}",
                output_schema=schema,
                schema_name="e2r_v5_phase106_active_test",
            )
        except StructuredProviderUnavailable as exc:
            self.active_request_id = str(exc).rsplit(":", 1)[-1]
            raise
        raise AssertionError("active transport request must remain pending")


class _HistoricalThenActiveStageCourtPendingCheckpointRunner(
    _HistoricalThenActivePendingCheckpointRunner
):
    """Return a nonterminal run whose exact wait lives in StageCourt."""

    def run_checkpoint(self, *, config, target, repo_root, source_resume_mode):
        self.calls.append(target.target_id)
        target_root = Path(config.output_root) / target.target_id
        transport = CollaborationCodexSubagentTransport()
        transport.configure_journal_root(
            target_root / "collaboration_codex_subagent_provider"
        )
        schema = {
            "type": "object",
            "additionalProperties": False,
            "required": ["ok"],
            "properties": {"ok": {"type": "boolean"}},
        }
        for label in ("historical", "active"):
            try:
                transport.complete(
                    prompt=f"{label} research {target.target_id}",
                    output_schema=schema,
                    schema_name=f"e2r_v5_phase106_{label}_stagecourt_test",
                )
            except StructuredProviderUnavailable as exc:
                request_id = str(exc).rsplit(":", 1)[-1]
                if label == "historical":
                    self.historical_request_id = request_id
                else:
                    self.active_request_id = request_id
        assert self.active_request_id is not None
        return SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            audit={},
            dossier=SimpleNamespace(pending_reasons=()),
            fact_extraction=SimpleNamespace(pending_reasons=()),
            source_graph=SimpleNamespace(checkpoint={"pending_reasons": []}),
            structured_materialization=SimpleNamespace(pending_reasons=()),
            stagecourt=SimpleNamespace(
                decision=SimpleNamespace(
                    pending_reasons=(
                        "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        f"COLLABORATION_RESPONSE_PENDING:{self.active_request_id}",
                    )
                )
            ),
        )


def _write_dummy_strong_bundle(path: Path) -> None:
    path.mkdir(parents=True)
    for name in (RECEIPT_MANIFEST_NAME, *REQUIRED_ARTIFACT_NAMES):
        (path / name).write_text("{}\n", encoding="utf-8")
    reviews = path / REVIEW_DIRECTORY_NAME
    reviews.mkdir()
    for name in REVIEW_NAMES:
        (reviews / name).write_text("{}\n", encoding="utf-8")


class E2RV6CurrentLiveCanaryRunnerTests(unittest.TestCase):
    def test_phase106_resume_binding_seals_current_source_and_research_epoch(
        self,
    ) -> None:
        selection = _selection()
        row = selection["selections"][0]
        assert isinstance(row, dict)
        source = {
            "target_id": row["target_id"],
            "as_of_date": selection["selection_as_of_date"],
            "checkpoint_id": "SGCHECK-" + "3" * 24,
            "checkpoint_hash": "3" * 64,
            "epoch": 8,
            "resumed_from_checkpoint_id": "SGCHECK-" + "2" * 24,
        }
        epoch = SimpleNamespace(
            target_id=row["target_id"],
            as_of_date=selection["selection_as_of_date"],
            checkpoint_id="REPOCH-" + "4" * 24,
            checkpoint_hash="4" * 64,
            epoch=7,
            source_graph_checkpoint_id="SGCHECK-" + "1" * 24,
        )
        with tempfile.TemporaryDirectory() as temporary:
            target_root = Path(temporary)
            (target_root / "source_graph_checkpoint.json").write_text(
                "{}\n", encoding="utf-8"
            )
            (target_root / "research_epoch_checkpoint.json").write_text(
                "{}\n", encoding="utf-8"
            )
            with (
                patch(
                    "e2r.production.v6_current_live_canary_runner."
                    "load_source_graph_checkpoint",
                    return_value=source,
                ),
                patch(
                    "e2r.production.v6_current_live_canary_runner."
                    "validate_source_graph_checkpoint",
                    return_value=source,
                ),
                patch(
                    "e2r.production.v6_current_live_canary_runner."
                    "load_research_epoch_checkpoint",
                    return_value=epoch,
                ),
                patch(
                    "e2r.production.v6_current_live_canary_runner."
                    "refresh_canary_target_manifest_hash",
                    return_value=False,
                ),
            ):
                written = _write_phase106_resume_binding(
                    target_root=target_root,
                    selection=selection,
                    row=row,
                )

            self.assertTrue(written)
            receipt = json.loads(
                (target_root / "until_pass_progress.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                receipt["schema_version"], PHASE106_RESUME_BINDING_SCHEMA
            )
            self.assertEqual(
                receipt["phase106_source_checkpoint_binding"], source
            )
            self.assertEqual(
                receipt["research_epoch_checkpoint_binding"]["checkpoint_id"],
                epoch.checkpoint_id,
            )
            self.assertFalse(receipt["production_score_authority"])
            self.assertFalse(receipt["production_stage_authority"])
            self.assertEqual(
                receipt["resume_binding_hash"],
                stable_hash(
                    {
                        key: value
                        for key, value in receipt.items()
                        if key != "resume_binding_hash"
                    }
                ),
            )

    def test_forced_selection_loads_profile_from_canonical_cutover_sibling(
        self,
    ) -> None:
        fixture = selection_fixtures.E2RV6CanarySelectionTests(
            methodName=(
                "test_forced_exact_five_require_complete_official_profile_and_abstention"
            )
        )
        candidates = fixture._abstained_candidates()
        profile = fixture._forced_profile_manifest(candidates)
        selection = compile_cross_archetype_canary_selection(
            selection_as_of_date=fixture.AS_OF_DATE,
            candidates=candidates,
            trigger_events=fixture._signals(candidates),
            issuer_business_profile_manifest=profile,
        )
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            cutover = repo / "docs/operational/e2r_v6_operational_cutover"
            profile_path = cutover / ISSUER_PROFILE_MANIFEST_NAME
            selection_path = cutover / "cross_archetype_canary_selection.json"
            seal_current_issuer_business_profile_manifest(profile_path, profile)
            seal_cross_archetype_canary_selection(
                selection_path,
                selection,
                issuer_business_profile_manifest=profile,
            )

            loaded_selection, loaded_profile = _load_inputs(
                repo_root=repo,
                selection_path=selection_path,
            )

            self.assertFalse((repo / "output").exists())
            self.assertEqual(stable_hash(loaded_selection), stable_hash(selection))
            self.assertEqual(stable_hash(loaded_profile), stable_hash(profile))
            with (
                patch(
                    "e2r.cli.run_e2r_v6_current_live_canaries_until_pass.canonical_repository_root",
                    return_value=repo.resolve(),
                ),
                patch(
                    "e2r.cli.run_e2r_v6_current_live_canaries_until_pass._repository_identity_is_trusted",
                    return_value=True,
                ),
                patch(
                    "e2r.cli.run_e2r_v6_current_live_canaries_until_pass.V6CurrentLiveCanaryRunner.run_checkpoint",
                    return_value={
                        "status": PHASE106_RUN_PENDING,
                        "blockers": ["COLLABORATION_RESPONSE_PENDING"],
                    },
                ) as run,
                redirect_stdout(io.StringIO()),
            ):
                exit_code = phase106_cli_main(
                    [
                        "--repo-root",
                        str(repo),
                        "--live-materialization-authorized",
                        "true",
                        "--checkpoint-resume",
                        "true",
                        "--research-provider",
                        "codex-collaboration",
                    ]
                )
            self.assertEqual(exit_code, 3)
            self.assertEqual(
                stable_hash(run.call_args.kwargs["issuer_business_profile_manifest"]),
                stable_hash(profile),
            )

    def test_cli_accepts_only_collaboration_and_preserves_pending_exit(self) -> None:
        with self.assertRaises(SystemExit):
            phase106_cli_main(
                [
                    "--live-materialization-authorized",
                    "true",
                    "--checkpoint-resume",
                    "true",
                    "--research-provider",
                    "local",
                ]
            )
        selection = _selection()
        pending = {
            "status": PHASE106_RUN_PENDING,
            "pending_requests": [{"request_id": "COLLABREQ-test"}],
        }
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary).resolve()
            with (
                patch(
                    "e2r.cli.run_e2r_v6_current_live_canaries_until_pass.canonical_repository_root",
                    return_value=repo,
                ),
                patch(
                    "e2r.cli.run_e2r_v6_current_live_canaries_until_pass._repository_identity_is_trusted",
                    return_value=True,
                ),
                patch(
                    "e2r.cli.run_e2r_v6_current_live_canaries_until_pass._load_inputs",
                    return_value=(selection, None),
                ),
                patch(
                    "e2r.cli.run_e2r_v6_current_live_canaries_until_pass.V6CurrentLiveCanaryRunner.run_checkpoint",
                    return_value=pending,
                ) as run,
                redirect_stdout(io.StringIO()) as stdout,
            ):
                exit_code = phase106_cli_main(
                    [
                        "--repo-root",
                        str(repo),
                        "--live-materialization-authorized",
                        "true",
                        "--checkpoint-resume",
                        "true",
                        "--research-provider",
                        "codex-collaboration",
                    ]
                )
            self.assertEqual(exit_code, 3)
            self.assertEqual(json.loads(stdout.getvalue())["status"], PHASE106_RUN_PENDING)
            self.assertTrue(run.call_args.kwargs["live_materialization_authorized"])
            self.assertTrue(run.call_args.kwargs["checkpoint_resume"])

    def test_research_collaboration_pending_returns_immediately(self) -> None:
        selection = _selection()
        calls: list[str] = []
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result = V6CurrentLiveCanaryRunner(
                checkpoint_runner_factory=lambda _row: _PendingCheckpointRunner(
                    calls
                )
            ).run_checkpoint(
                repo_root=REPO_ROOT,
                selection=selection,
                work_root=root / "work",
                cutover_root=root / "cutover",
                live_materialization_authorized=True,
                checkpoint_resume=True,
            )
            self.assertEqual(result["status"], PHASE106_RUN_PENDING)
            self.assertEqual(calls, ["000001"])
            self.assertEqual(len(result["pending_requests"]), 1)
            self.assertEqual(
                result["blockers"], ["COLLABORATION_RESPONSE_PENDING"]
            )
            self.assertEqual(
                result["external_wait_marker"],
                "COLLABORATION_RESPONSE_PENDING",
            )
            attempt = _command_attempt(
                step_id="current_live_canary_runs",
                argv=["python", "-m", "phase106"],
                completed=subprocess.CompletedProcess(
                    args=[],
                    returncode=3,
                    stdout=json.dumps(result),
                    stderr="",
                ),
            )
            self.assertEqual(
                attempt["pending_markers"],
                ["COLLABORATION_RESPONSE_PENDING"],
            )
            self.assertTrue(
                result["pending_requests"][0]["request_id"].startswith(
                    "COLLABREQ-"
                )
            )
            self.assertEqual(
                result["pending_requests"][0]["request_scope"],
                "FULL_RESEARCHER_MODE",
            )
            self.assertEqual(
                result["pending_requests"][0]["pass_name"],
                "PHASE106_TEST",
            )
            self.assertEqual(
                result["pending_requests"][0]["schema_name"],
                "e2r_v5_phase106_test",
            )
            self.assertFalse((root / "cutover" / "current_live_canaries").exists())
            self.assertEqual(result["gold_call_count"], 0)
            self.assertEqual(result["local_provider_call_count"], 0)

    def test_pending_output_exposes_only_the_current_typed_request(self) -> None:
        """An unanswered superseded journal row must not become active again."""

        selection = _selection()
        calls: list[str] = []
        checkpoint_runner = _HistoricalThenActivePendingCheckpointRunner(calls)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result = V6CurrentLiveCanaryRunner(
                checkpoint_runner_factory=lambda _row: checkpoint_runner
            ).run_checkpoint(
                repo_root=REPO_ROOT,
                selection=selection,
                work_root=root / "work",
                cutover_root=root / "cutover",
                live_materialization_authorized=True,
                checkpoint_resume=True,
            )

            self.assertEqual(result["status"], PHASE106_RUN_PENDING)
            self.assertEqual(calls, ["000001"])
            self.assertIsNotNone(checkpoint_runner.historical_request_id)
            self.assertIsNotNone(checkpoint_runner.active_request_id)
            self.assertNotEqual(
                checkpoint_runner.historical_request_id,
                checkpoint_runner.active_request_id,
            )
            self.assertEqual(
                [row["request_id"] for row in result["pending_requests"]],
                [checkpoint_runner.active_request_id],
            )
            journal = (
                root
                / "work"
                / "research"
                / str(selection["selections"][0]["archetype_id"])
                / "000001"
                / "collaboration_codex_subagent_provider"
                / "requests"
            )
            self.assertEqual(len(tuple(journal.glob("*.json"))), 2)

    def test_stagecourt_wait_exposes_current_supervisor_not_history(self) -> None:
        """Supervisor waits are born after dossier construction in StageCourt."""

        selection = _selection()
        calls: list[str] = []
        checkpoint_runner = (
            _HistoricalThenActiveStageCourtPendingCheckpointRunner(calls)
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result = V6CurrentLiveCanaryRunner(
                checkpoint_runner_factory=lambda _row: checkpoint_runner
            ).run_checkpoint(
                repo_root=REPO_ROOT,
                selection=selection,
                work_root=root / "work",
                cutover_root=root / "cutover",
                live_materialization_authorized=True,
                checkpoint_resume=True,
            )

            self.assertEqual(result["status"], PHASE106_RUN_PENDING)
            self.assertEqual(result["pending_kind"], "RESEARCH_COLLABORATION_RESPONSE")
            self.assertEqual(result["blockers"], ["COLLABORATION_RESPONSE_PENDING"])
            self.assertEqual(
                [row["request_id"] for row in result["pending_requests"]],
                [checkpoint_runner.active_request_id],
            )
            self.assertNotEqual(
                checkpoint_runner.historical_request_id,
                checkpoint_runner.active_request_id,
            )

    def test_terminal_target_opens_exact_distinct_blind_reviews_before_next_target(
        self,
    ) -> None:
        selection = _selection()
        selected = selection["selections"][0]
        assert isinstance(selected, dict)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            research_parent = (
                root / "work" / "research" / str(selected["archetype_id"])
            )
            research_parent.mkdir(parents=True)
            target_root = _write_terminal_output(research_parent, selection)
            manifest_path = target_root / "target_run_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["status"] = PHASE106_TERMINAL_RESEARCH_STATUS
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            factory = Mock(side_effect=AssertionError("terminal output must resume at review"))
            result = V6CurrentLiveCanaryRunner(
                checkpoint_runner_factory=factory
            ).run_checkpoint(
                repo_root=REPO_ROOT,
                selection=selection,
                work_root=root / "work",
                cutover_root=root / "cutover",
                live_materialization_authorized=True,
                checkpoint_resume=True,
            )
            self.assertEqual(result["status"], PHASE106_RUN_PENDING)
            self.assertEqual(result["pending_kind"], "INDEPENDENT_CODEX_REVIEWS")
            self.assertEqual(
                result["blockers"], ["COLLABORATION_RESPONSE_PENDING"]
            )
            self.assertEqual(
                [row["reviewer_slot"] for row in result["pending_requests"]],
                ["A", "B"],
            )
            self.assertEqual(
                len({row["request_id"] for row in result["pending_requests"]}), 2
            )
            factory.assert_not_called()
            self.assertFalse((root / "cutover" / "current_live_canaries").exists())

    def test_all_five_are_staged_then_atomically_published(self) -> None:
        selection = _selection()
        rows = selection["selections"]
        assert isinstance(rows, list)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            work = root / "work"
            cutover = root / "cutover"
            for index, row in enumerate(rows):
                assert isinstance(row, dict)
                artifacts = _artifacts(selection, index)
                manifest = build_selection_bound_canary_manifest(
                    selection=selection,
                    selection_id=str(row["selection_id"]),
                    artifacts=artifacts,
                    repo_root=REPO_ROOT,
                )
                export_selection_bound_canary_bundle(
                    output_directory=(
                        work
                        / "prepared"
                        / f"{row['archetype_id']}_{row['target_id']}"
                    ),
                    selection=selection,
                    manifest=manifest,
                    artifacts=artifacts,
                    reviews=_reviews(manifest, artifacts),
                    repo_root=REPO_ROOT,
                )
            result = V6CurrentLiveCanaryRunner().run_checkpoint(
                repo_root=REPO_ROOT,
                selection=selection,
                work_root=work,
                cutover_root=cutover,
                live_materialization_authorized=True,
                checkpoint_resume=True,
            )
            self.assertEqual(result["status"], PHASE106_RUN_PASS)
            live = cutover / "current_live_canaries"
            self.assertTrue(live.is_dir())
            self.assertTrue((cutover / "cross_archetype_canary_summary.json").is_file())
            self.assertFalse(any(path.name.endswith(".tmp") for path in cutover.iterdir()))
            for directory in live.iterdir():
                self.assertEqual(
                    {path.name for path in directory.iterdir()},
                    {
                        RECEIPT_MANIFEST_NAME,
                        *REQUIRED_ARTIFACT_NAMES,
                        REVIEW_DIRECTORY_NAME,
                    },
                )
            resumed = V6CurrentLiveCanaryRunner().run_checkpoint(
                repo_root=REPO_ROOT,
                selection=selection,
                work_root=work,
                cutover_root=cutover,
                live_materialization_authorized=True,
                checkpoint_resume=True,
            )
            self.assertEqual(resumed["status"], PHASE106_RUN_PASS)
            self.assertEqual(resumed["summary_id"], result["summary_id"])

    def test_failed_offline_verification_publishes_nothing(self) -> None:
        selection = _selection()
        rows = selection["selections"]
        assert isinstance(rows, list)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            work = root / "work"
            for row in rows:
                assert isinstance(row, dict)
                _write_dummy_strong_bundle(
                    work
                    / "prepared"
                    / f"{row['archetype_id']}_{row['target_id']}"
                )
            with patch(
                "e2r.production.v6_current_live_canary_runner._verify_prepared_bundle",
                side_effect=[{}, {}, {}, {}, ValueError("fifth canary invalid")],
            ):
                with self.assertRaisesRegex(ValueError, "fifth canary invalid"):
                    V6CurrentLiveCanaryRunner().run_checkpoint(
                        repo_root=REPO_ROOT,
                        selection=selection,
                        work_root=work,
                        cutover_root=root / "cutover",
                        live_materialization_authorized=True,
                        checkpoint_resume=True,
                    )
            self.assertFalse((root / "cutover" / "current_live_canaries").exists())

    def test_cutover_parent_symlink_swap_fails_before_atomic_publish(self) -> None:
        selection = _selection()
        rows = selection["selections"]
        assert isinstance(rows, list)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            work = root / "work"
            cutover = root / "cutover"
            displaced = root / "cutover-original"
            victim = root / "outside"
            victim.mkdir()
            for index, row in enumerate(rows):
                assert isinstance(row, dict)
                artifacts = _artifacts(selection, index)
                manifest = build_selection_bound_canary_manifest(
                    selection=selection,
                    selection_id=str(row["selection_id"]),
                    artifacts=artifacts,
                    repo_root=REPO_ROOT,
                )
                export_selection_bound_canary_bundle(
                    output_directory=(
                        work
                        / "prepared"
                        / f"{row['archetype_id']}_{row['target_id']}"
                    ),
                    selection=selection,
                    manifest=manifest,
                    artifacts=artifacts,
                    reviews=_reviews(manifest, artifacts),
                    repo_root=REPO_ROOT,
                )

            original_fsync_tree = phase106_runner_module._fsync_tree

            def swap_parent_after_staging_fsync(staging: Path) -> None:
                original_fsync_tree(staging)
                cutover.rename(displaced)
                cutover.symlink_to(victim, target_is_directory=True)

            with patch(
                "e2r.production.v6_current_live_canary_runner._fsync_tree",
                side_effect=swap_parent_after_staging_fsync,
            ), self.assertRaises((OSError, ValueError)):
                V6CurrentLiveCanaryRunner().run_checkpoint(
                    repo_root=REPO_ROOT,
                    selection=selection,
                    work_root=work,
                    cutover_root=cutover,
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                )

            self.assertFalse((victim / "current_live_canaries").exists())
            self.assertFalse((displaced / "current_live_canaries").exists())
            self.assertFalse(
                (victim / "cross_archetype_canary_summary.json").exists()
            )


if __name__ == "__main__":
    unittest.main()
