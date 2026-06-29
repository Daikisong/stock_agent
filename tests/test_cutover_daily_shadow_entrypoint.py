import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CutoverDailyShadowEntrypointTests(unittest.TestCase):
    def test_cli_generates_shadow_outputs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "out"
            docs = Path(tmpdir) / "docs"
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "e2r.cli.run_e2r_production_cutover_shadow",
                    "--as-of-date",
                    "2026-06-30",
                    "--output-dir",
                    str(output),
                    "--docs-dir",
                    str(docs),
                    "--fail-on-critical-audit",
                    "true",
                ],
                env={"PYTHONPATH": "src"},
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            payload = json.loads(completed.stdout)
            self.assertEqual(payload["production_verdict"], "NOT_READY")
            self.assertTrue((output / "audit_summary.json").exists())


if __name__ == "__main__":
    unittest.main()
