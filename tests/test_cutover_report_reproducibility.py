import unittest
import json
import subprocess
import tempfile
from pathlib import Path

from e2r.cli.audit_operational_report_reproducibility import audit_report_reproducibility
from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


def _git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


class CutoverReportReproducibilityTests(unittest.TestCase):
    def test_metadata_contains_required_hashes(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        audit = audit_report_reproducibility(bundle["shadow_latest"], repo_root=".")
        summary = audit["summary"]
        self.assertEqual(summary["missing_command_count"], 0)
        self.assertEqual(summary["missing_config_hash_count"], 0)
        self.assertEqual(summary["missing_planner_hash_count"], 0)

    def test_report_only_artifact_commit_preserves_report_head_alignment(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            _git(repo, "init", "-b", "main")
            _git(repo, "config", "user.email", "test@example.com")
            _git(repo, "config", "user.name", "Test User")
            (repo / "src").mkdir()
            (repo / "src" / "code.py").write_text("print('base')\n", encoding="utf-8")
            _git(repo, "add", "src/code.py")
            _git(repo, "commit", "-m", "base")
            base_sha = _git(repo, "rev-parse", "HEAD")
            report = {
                "production_ready": False,
                "metadata": {
                    "git_head_sha": base_sha,
                    "report_base_commit_sha": base_sha,
                    "command": "unit-test",
                    "config_hash": "config",
                    "source_corpus_hash": "source",
                    "candidate_event_hash": "candidate",
                    "planner_prompt_hash": "prompt",
                    "planner_response_hash": "response",
                },
            }
            report_dir = repo / "docs" / "operational"
            report_dir.mkdir(parents=True)
            (report_dir / "production_cutover_shadow_latest.json").write_text(
                json.dumps(report, indent=2),
                encoding="utf-8",
            )
            _git(repo, "add", "docs/operational/production_cutover_shadow_latest.json")
            _git(repo, "commit", "-m", "report artifacts")

            artifact_audit = audit_report_reproducibility(report, repo_root=repo)
            self.assertEqual(artifact_audit["summary"]["report_head_sha_mismatch_count"], 0)
            self.assertEqual(
                artifact_audit["metadata"]["report_head_alignment"]["mode"],
                "report_artifact_child",
            )

            (repo / "src" / "code.py").write_text("print('changed')\n", encoding="utf-8")
            _git(repo, "add", "src/code.py")
            _git(repo, "commit", "-m", "code change after report")
            stale_audit = audit_report_reproducibility(report, repo_root=repo)
            self.assertEqual(stale_audit["summary"]["report_head_sha_mismatch_count"], 1)


if __name__ == "__main__":
    unittest.main()
