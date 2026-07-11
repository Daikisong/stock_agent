from __future__ import annotations

import hashlib
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from e2r.cli.run_e2r_census_mode import main as census_main
from e2r.cli.run_e2r_current_operation import main as current_main
from e2r.research_brain.runtime.live_materialization import (
    AuthorizationPath,
    LiveOperationalRunEnvelope,
    LiveRunMode,
    load_live_run_profile,
    resolve_live_authorization,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


class LiveAuthorizationContractTests(unittest.TestCase):
    def test_all_goal_run_modes_are_registered(self) -> None:
        self.assertEqual(
            {mode.value for mode in LiveRunMode},
            {
                "MANIFEST_REPLAY",
                "LIVE_BOOTSTRAP",
                "LIVE_DAILY_INCREMENTAL",
                "LIVE_CENSUS_BASELINE",
                "LIVE_CENSUS_SELECTIVE_DEEP",
                "TARGETED_LIVE_SMOKE",
                "TEST_FIXTURE",
            },
        )

    def test_manifest_replay_and_live_materialization_are_separate(self) -> None:
        replay = resolve_live_authorization(
            input_manifest="input.json",
            materialize_live_input=False,
            live_materialization_authorized=False,
            run_profile=None,
            requested_live_mode=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
        )
        live = resolve_live_authorization(
            input_manifest=None,
            materialize_live_input=True,
            live_materialization_authorized=True,
            run_profile="configs/e2r_production_daily_v1.json",
            requested_live_mode=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
        )

        self.assertEqual(replay.path, AuthorizationPath.MANIFEST_REPLAY.value)
        self.assertEqual(replay.run_mode, LiveRunMode.MANIFEST_REPLAY.value)
        self.assertEqual(live.path, AuthorizationPath.LIVE_MATERIALIZATION.value)
        self.assertTrue(live.execution_allowed)

    def test_invalid_live_flag_combinations_are_rejected_with_exact_codes(self) -> None:
        missing_authorization = resolve_live_authorization(
            input_manifest=None,
            materialize_live_input=True,
            live_materialization_authorized=False,
            run_profile="configs/e2r_production_daily_v1.json",
            requested_live_mode=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
        )
        conflict = resolve_live_authorization(
            input_manifest="input.json",
            materialize_live_input=True,
            live_materialization_authorized=True,
            run_profile=None,
            requested_live_mode=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
        )

        self.assertEqual(missing_authorization.path, AuthorizationPath.REJECTED.value)
        self.assertEqual(
            missing_authorization.blocker_codes,
            ("LIVE_MATERIALIZATION_NOT_AUTHORIZED",),
        )
        self.assertIn(
            "INPUT_MANIFEST_AND_LIVE_MATERIALIZATION_CONFLICT",
            conflict.blocker_codes,
        )
        self.assertIn("LIVE_RUN_PROFILE_REQUIRED", conflict.blocker_codes)

    def test_production_profiles_are_bounded_and_official_first(self) -> None:
        expected_modes = {
            "e2r_current_bootstrap_v1.json": LiveRunMode.LIVE_BOOTSTRAP.value,
            "e2r_production_daily_v1.json": LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
            "e2r_census_selective_deep_v1.json": LiveRunMode.LIVE_CENSUS_SELECTIVE_DEEP.value,
        }
        for filename, expected_mode in expected_modes.items():
            profile = load_live_run_profile(REPO_ROOT / "configs" / filename)
            self.assertEqual(profile.run_mode, expected_mode, filename)
            self.assertTrue(profile.live_authorization_required, filename)
            self.assertTrue(profile.official_first, filename)
            self.assertTrue(profile.general_web_requires_official_gap, filename)
            self.assertTrue(all(value > 0 for value in profile.budgets.values()), filename)

    def test_operational_envelope_rejects_readiness_without_live_claim_chain(self) -> None:
        digest = hashlib.sha256(b"fixture").hexdigest()
        with self.assertRaisesRegex(ValueError, "readiness overclaim"):
            LiveOperationalRunEnvelope(
                materialization_run_id="MAT-1",
                evaluator_run_id="EVAL-1",
                as_of_date="2026-07-10",
                run_mode=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
                source_corpus_hash=digest,
                input_manifest_hash=digest,
                evaluator_leaf_hash=digest,
                actual_live_source_count=0,
                fresh_provider_cache_count=0,
                accepted_current_claim_count=0,
                current_atomic_decision_count=0,
                provider_blockers=(),
                critical_counts={},
                production_runtime_ready=True,
            )

    def test_authorized_live_current_does_not_fall_into_manifest_missing_exit_three(self) -> None:
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            output_root = Path(tmp) / "current"
            code = current_main(
                [
                    "--as-of-date",
                    "2026-07-10",
                    "--mode",
                    "production_bounded",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(output_root),
                    "--materialize-live-input",
                    "true",
                    "--live-materialization-authorized",
                    "true",
                    "--run-profile",
                    str(REPO_ROOT / "configs/e2r_production_daily_v1.json"),
                ]
            )
            payload = json.loads(
                (output_root / "current_daily_census_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            envelope = json.loads(
                (output_root / "live_operational_envelope.json").read_text(
                    encoding="utf-8"
                )
            )
            accepted = tuple(
                line
                for line in (output_root / "accepted_claims.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
                if line.strip()
            )

        self.assertEqual(code, 0)
        self.assertEqual(payload["status"], "BOUNDED_DAILY_CENSUS_PASS")
        self.assertEqual(payload["critical_count_sum"], 0)
        self.assertGreater(payload["full_universe_count"], 1000)
        self.assertEqual(payload["claim_provenance_count"], 1)
        self.assertTrue(payload["source_corpus_hash"])
        self.assertEqual(len(accepted), 1)
        self.assertTrue(envelope["production_runtime_ready"])
        self.assertEqual(envelope["accepted_current_claim_count"], 1)

    def test_census_forwards_live_authorization_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            output_root = Path(tmp) / "census"
            code = census_main(
                [
                    "--as-of-date",
                    "2026-07-10",
                    "--mode",
                    "census_selective_deep",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(output_root),
                    "--materialize-live-input",
                    "true",
                    "--live-materialization-authorized",
                    "true",
                    "--run-profile",
                    str(REPO_ROOT / "configs/e2r_census_selective_deep_v1.json"),
                    "--resume",
                    "true",
                ]
            )
            payload = json.loads(
                (output_root / "current_daily_census_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            census = json.loads(
                (output_root / "census_acceptance_audit.json").read_text(
                    encoding="utf-8"
                )
            )

        self.assertEqual(code, 0)
        self.assertEqual(payload["status"], "BOUNDED_DAILY_CENSUS_PASS")
        self.assertEqual(payload["critical_count_sum"], 0)
        self.assertEqual(payload["claim_provenance_count"], 1)
        self.assertEqual(
            payload["source_corpus_hash"], census["census_source_corpus_hash"]
        )
        self.assertEqual(census["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
