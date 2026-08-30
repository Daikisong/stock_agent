from __future__ import annotations

from argparse import Namespace
from dataclasses import replace
import asyncio
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from e2r.pro_first.atomic_io import fsync_directory
from e2r.pro_first.browser.protocol import ManualLoginRequired
from e2r.pro_first.config import (
    ProAuthorityRuntimeConfig,
    ProDashboardRuntimeConfig,
    ProSupplementRuntimeConfig,
    load_pro_first_local_config,
)
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.operations import (
    build_job_packet,
    create_forced_validation_canary,
    prepare_job_in_logged_in_browser,
)
from e2r.pro_first.runtime import ProFirstLocalStack
from e2r.pro_first.static_audit import (
    audit_python_source,
    compile_pro_first_static_audit,
)
from e2r.cli.run_e2r_pro_first_shadow_check import _run as run_shadow_check


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "configs/e2r_pro_first_local.example.yaml"


class ProFirstOperationalConfigTest(unittest.TestCase):
    def test_windows_directory_fsync_is_a_safe_noop(self) -> None:
        with patch("e2r.pro_first.atomic_io.os.name", "nt"), patch(
            "e2r.pro_first.atomic_io.os.open"
        ) as opener:
            fsync_directory("C:/runtime")
        opener.assert_not_called()

    def test_example_config_is_safe_and_complete(self) -> None:
        config = load_pro_first_local_config(EXAMPLE)
        self.assertEqual(config.scheduler.morning_at, "05:30")
        self.assertEqual(config.scheduler.evening_at, "18:30")
        self.assertTrue(config.browser.require_manual_login)
        self.assertTrue(config.browser.require_user_start_approval)
        self.assertFalse(config.browser.hidden_api_access)
        self.assertFalse(config.authority.pro_score_authority)
        self.assertFalse(config.authority.pro_stage_authority)
        self.assertFalse(config.supplement.full_research_restart)

    def test_non_loopback_dashboard_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "loopback"):
            ProDashboardRuntimeConfig(host="0.0.0.0")

    def test_pro_authority_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot own"):
            ProAuthorityRuntimeConfig(pro_score_authority=True)

    def test_nonblocking_supplement_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "nonblocking"):
            ProSupplementRuntimeConfig(corroboration_cap=True)

    def test_unknown_config_key_rejected(self) -> None:
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / "config.yaml"
            payload = json.loads(EXAMPLE.read_text(encoding="utf-8"))
            payload["browser"]["password"] = "must-not-exist"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unknown"):
                load_pro_first_local_config(path)

    def test_active_port_file_requires_a_path_string(self) -> None:
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / "config.yaml"
            payload = json.loads(EXAMPLE.read_text(encoding="utf-8"))
            payload["browser"]["cdp_active_port_file"] = {"unsafe": "value"}
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "path string"):
                load_pro_first_local_config(path)

    def test_windows_chrome_helper_is_loopback_and_origin_bounded(self) -> None:
        helper = (ROOT / "scripts/start_e2r_pro_chrome.ps1").read_text(
            encoding="utf-8"
        )
        self.assertIn("--remote-debugging-address=127.0.0.1", helper)
        self.assertIn("--remote-allow-origins=http://127.0.0.1", helper)
        self.assertNotIn("--remote-allow-origins=*", helper)


class ProFirstOperationalStackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        base = load_pro_first_local_config(EXAMPLE)
        self.config = replace(base, runtime_root=Path(self.temporary.name) / "runtime")

    def test_stack_check_migrates_db_without_browser_or_login(self) -> None:
        stack = ProFirstLocalStack(self.config, repo_root=ROOT)
        snapshot = stack.readiness_snapshot()
        self.assertTrue(self.config.database_path.is_file())
        self.assertTrue(snapshot["dashboard_loopback_only"])
        self.assertTrue(snapshot["manual_login_required"])
        self.assertFalse(snapshot["hidden_api_access"])

    def test_forced_canary_is_labelled_and_packet_is_blind(self) -> None:
        store = ProFirstJobStore(self.config.database_path)
        job = create_forced_validation_canary(
            store,
            symbol="000000",
            company_name="검증전용회사",
            as_of_date="2026-08-22",
            archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
        )
        prepared, bundle, _prompt = build_job_packet(
            store,
            job_id=job.job_id,
            runtime_root=self.config.runtime_root,
            config_hash=self.config.config_hash,
            repo_root=ROOT,
        )
        payload = json.loads(bundle.research_packet_json.read_text(encoding="utf-8"))
        selection = store.get_candidate(job.candidate_id).selection_receipt
        self.assertEqual(prepared.mode, "FORCED_VALIDATION_CANARY")
        self.assertEqual(selection["selection_mode"], "FORCED_VALIDATION_CANARY")
        self.assertFalse(selection["production_candidate"])
        self.assertFalse(payload["score_authority"])
        self.assertFalse(payload["stage_authority"])
        self.assertNotIn("expected_score", json.dumps(payload).casefold())
        self.assertNotIn("expected_stage", json.dumps(payload).casefold())

    def test_unavailable_cdp_stops_safely_without_submit(self) -> None:
        store = ProFirstJobStore(self.config.database_path)
        job = create_forced_validation_canary(
            store,
            symbol="000001",
            company_name="브라우저부재검증",
            as_of_date="2026-08-22",
        )
        unavailable = replace(
            self.config,
            browser=replace(self.config.browser, cdp_url="http://127.0.0.1:9"),
        )
        with self.assertRaises(Exception):
            asyncio.run(
                prepare_job_in_logged_in_browser(
                    store,
                    job_id=job.job_id,
                    config=unavailable,
                    repo_root=ROOT,
                )
            )
        stopped = store.get_job(job.job_id)
        self.assertEqual(stopped.status, "USER_ATTENTION_REQUIRED")
        self.assertEqual(stopped.submit_count, 0)

    def test_manual_login_pending_is_durable_and_never_submits(self) -> None:
        store = ProFirstJobStore(self.config.database_path)
        job = create_forced_validation_canary(
            store,
            symbol="000002",
            company_name="수동로그인검증",
            as_of_date="2026-08-22",
        )
        observed = {"closed": 0}

        class Adapter:
            async def prepare_without_submit(self, **_kwargs):
                raise ManualLoginRequired("manual login required")

        class Session:
            adapter = Adapter()
            browser_session_id = "BROWSER-manual-login-test"

            async def close(self):
                observed["closed"] += 1

        async def open_session(_worker, *, job_id):
            self.assertEqual(job_id, job.job_id)
            return Session()

        with patch(
            "e2r.pro_first.operations.ProBrowserWorker.open",
            new=open_session,
        ):
            with self.assertRaises(ManualLoginRequired):
                asyncio.run(
                    prepare_job_in_logged_in_browser(
                        store,
                        job_id=job.job_id,
                        config=self.config,
                        repo_root=ROOT,
                    )
                )
        stopped = store.get_job(job.job_id)
        self.assertEqual(stopped.status, "USER_ATTENTION_REQUIRED")
        self.assertEqual(stopped.last_error_class, "ManualLoginRequired")
        self.assertEqual(stopped.submit_count, 0)
        self.assertEqual(observed["closed"], 1)

    def test_shadow_reuses_durable_job_without_creating_duplicate_canary(self) -> None:
        config_path = Path(self.temporary.name) / "config.json"
        config_payload = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        config_payload["runtime"]["root"] = str(self.config.runtime_root)
        config_path.write_text(json.dumps(config_payload), encoding="utf-8")
        store = ProFirstJobStore(self.config.database_path)
        job = create_forced_validation_canary(
            store,
            symbol="000660",
            company_name="SK하이닉스",
            as_of_date="2026-08-22",
            archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
        )
        observed = {}

        class Prepared:
            receipt = {
                "schema_version": "e2r_pro_first_live_shadow_receipt_v1",
                "status": "CHATGPT_WEB_SHADOW_COMPATIBILITY_PASS",
                "submit_count": 0,
            }

            async def close(self) -> None:
                observed["closed"] = True

        async def prepare(store_arg, *, job_id, config, repo_root, screenshot_path):
            observed.update(
                {
                    "job_id": job_id,
                    "runtime_root": config.runtime_root,
                    "screenshot_path": screenshot_path,
                }
            )
            self.assertEqual(store_arg.get_job(job_id).symbol, "000660")
            return Prepared()

        args = Namespace(
            config=str(config_path),
            repo_root=str(ROOT),
            job_id=job.job_id,
            symbol=None,
            company_name=None,
            as_of_date=None,
            archetype_id=[],
            output=None,
        )
        with patch(
            "e2r.cli.run_e2r_pro_first_shadow_check.prepare_job_in_logged_in_browser",
            new=prepare,
        ):
            result = asyncio.run(run_shadow_check(args))
        self.assertEqual(result["status"], "CHATGPT_WEB_SHADOW_COMPATIBILITY_PASS")
        self.assertEqual(observed["job_id"], job.job_id)
        self.assertEqual(observed["runtime_root"], self.config.runtime_root.resolve())
        self.assertTrue(observed["closed"])
        self.assertEqual(len(store.list_jobs(limit=10)), 1)


class ProFirstStaticAuditTest(unittest.TestCase):
    def test_ci_covers_v2_1_inputs_and_enforces_current_test_floor(self) -> None:
        workflow = (
            ROOT / ".github/workflows/e2r_pro_first_verify.yml"
        ).read_text(encoding="utf-8")
        for required_path in (
            '"configs/e2r_archetype_research_*"',
            '"configs/e2r_pro_research_*"',
            '"configs/e2r_pro_repair_*"',
            '"configs/prompts/e2r_pro_*"',
            '"docs/operational/e2r_pro_first_v2_1/**"',
            '"tests/fixtures/pro_first_v2/**"',
            '"tests/research_saturation_fixture.py"',
        ):
            self.assertEqual(workflow.count(required_path), 2)
        self.assertIn('E2R_FULL_UNIT_TEST_FLOOR: "7860"', workflow)
        self.assertIn("countTestCases()", workflow)
        self.assertIn(
            "discovered < E2R_FULL_UNIT_TEST_FLOOR",
            workflow,
        )

    def test_production_surface_has_zero_critical_findings(self) -> None:
        result = compile_pro_first_static_audit(ROOT)
        self.assertEqual(result["critical_count_sum"], 0, result["findings"])
        self.assertEqual(result["guarded_dom_submit_path_count"], 1)

    def test_submit_outside_coordinator_is_detected(self) -> None:
        findings, _ = audit_python_source(
            "async def unsafe(adapter):\n    await adapter.submit_once(None)\n",
            relative_path="src/e2r/pro_first/unsafe.py",
        )
        self.assertEqual([row.key for row in findings], ["submit_without_approval_count"])

    def test_native_locator_click_is_counted_as_the_send_boundary(self) -> None:
        findings, send_dispatches = audit_python_source(
            "async def submit_once(send):\n"
            '    await send.evaluate("element => element.click()")\n',
            relative_path="src/e2r/pro_first/browser/chatgpt_adapter.py",
        )
        self.assertEqual(findings, ())
        self.assertEqual(send_dispatches, (2,))

    def test_coordinate_and_native_send_paths_are_both_counted(self) -> None:
        _findings, send_dispatches = audit_python_source(
            "async def submit_once(send):\n"
            "    await send.click()\n"
            '    await send.evaluate("element => element.click()")\n',
            relative_path="src/e2r/pro_first/browser/chatgpt_adapter.py",
        )
        self.assertEqual(send_dispatches, (2, 3))

    def test_only_exact_intercepted_recovery_coordinator_may_call_submit_once(self) -> None:
        allowed, _ = audit_python_source(
            "class ProMultiPassResearchOrchestrator:\n"
            "    async def resume_intercepted_followup_submit(self, adapter, proof):\n"
            "        await adapter.submit_once(proof)\n",
            relative_path="src/e2r/pro_first/multi_pass/orchestrator.py",
        )
        rejected, _ = audit_python_source(
            "class ProMultiPassResearchOrchestrator:\n"
            "    async def resume_intercepted_followup_submit_unchecked(self, adapter, proof):\n"
            "        await adapter.submit_once(proof)\n",
            relative_path="src/e2r/pro_first/multi_pass/orchestrator.py",
        )
        self.assertEqual(allowed, ())
        self.assertEqual(
            [row.key for row in rejected],
            ["submit_without_approval_count"],
        )

    def test_private_chatgpt_endpoint_is_detected(self) -> None:
        findings, _ = audit_python_source(
            'URL = "https://chatgpt.com/backend-api/conversation"\n',
            relative_path="src/e2r/pro_first/unsafe.py",
        )
        self.assertEqual([row.key for row in findings], ["hidden_chatgpt_api_count"])

    def test_score_and_stage_authority_are_detected(self) -> None:
        findings, _ = audit_python_source(
            'VALUE = {"pro_score_authority": True, "pro_stage_authority": True}\n',
            relative_path="src/e2r/pro_first/unsafe.py",
        )
        self.assertEqual(
            {row.key for row in findings},
            {"pro_score_authority_count", "pro_stage_authority_count"},
        )

    def test_login_automation_is_detected(self) -> None:
        findings, _ = audit_python_source(
            'async def unsafe(page):\n    await page.fill("#password", "secret")\n',
            relative_path="src/e2r/pro_first/unsafe.py",
        )
        self.assertEqual([row.key for row in findings], ["login_automation_count"])


if __name__ == "__main__":
    unittest.main()
