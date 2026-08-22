from __future__ import annotations

from dataclasses import replace
import asyncio
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

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


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "configs/e2r_pro_first_local.example.yaml"


class ProFirstOperationalConfigTest(unittest.TestCase):
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


class ProFirstStaticAuditTest(unittest.TestCase):
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
