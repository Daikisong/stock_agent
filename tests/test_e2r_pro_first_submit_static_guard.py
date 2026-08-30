from __future__ import annotations

from pathlib import Path
import unittest

from e2r.pro_first.static_audit import audit_python_source


ROOT = Path(__file__).resolve().parents[1]


class ProFirstSubmitStaticGuardTest(unittest.TestCase):
    def test_all_dom_click_submit_paths_require_consumed_ledger_proof(self) -> None:
        adapter_path = ROOT / "src/e2r/pro_first/browser/chatgpt_adapter.py"
        source = adapter_path.read_text(encoding="utf-8")
        findings, send_dispatch_lines = audit_python_source(
            source,
            relative_path="src/e2r/pro_first/browser/chatgpt_adapter.py",
        )
        self.assertEqual(findings, ())
        self.assertEqual(len(send_dispatch_lines), 1)
        submit_source = source[
            source.index("    async def submit_once") : source.index("    async def inspect_state")
        ]
        dispatch = 'await send.evaluate("element => element.click()")'
        click_offset = submit_source.index(dispatch)
        prefix = submit_source[:click_offset]
        self.assertIn("ledger_verified", prefix)
        self.assertIn("_prepared_binding", prefix)
        self.assertIn("_submit_attempted", prefix)
        self.assertIn("E2R_PRO_JOB_ID", prefix)

    def test_submit_coordinator_claims_database_before_dom_action(self) -> None:
        source = (ROOT / "src/e2r/pro_first/approval.py").read_text(encoding="utf-8")
        submit = source[source.index("    async def submit(") : source.index("    @staticmethod")]
        self.assertLess(submit.index("self.store.claim_submit"), submit.index("adapter.submit_once"))
        self.assertIn("automatic_resubmit_allowed\": False", submit)

    def test_enter_key_submit_bypass_is_absent(self) -> None:
        browser_root = ROOT / "src/e2r/pro_first/browser"
        joined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(browser_root.glob("*.py"))
        )
        self.assertNotIn('press("Enter")', joined)
        self.assertNotIn("press('Enter')", joined)
        self.assertNotIn("keyboard.press", joined)


if __name__ == "__main__":
    unittest.main()
