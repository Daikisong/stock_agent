from __future__ import annotations

import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest

from e2r.cli.compile_e2r_v6_production_static_audit import main as static_cli_main
from e2r.production.v6_production_static_audit import (
    ABSOLUTE_REVIEWER_IDENTITY,
    AUTOMATIC_LOCAL_FALLBACK,
    EXECUTABLE_LOCAL_PROVIDER,
    FIXED_EXPECTED_SCORE,
    FIXED_EXPECTED_STAGE,
    GOLD_PRODUCTION_INPUT,
    OUTPUT_ONLY_READINESS,
    PRODUCTION_STATIC_AUDIT_FAIL,
    PRODUCTION_STATIC_AUDIT_LEAF,
    PRODUCTION_STATIC_AUDIT_PASS,
    REQUIRED_ZERO_COUNT_KEYS,
    SECRET_LITERAL,
    TARGET_CONDITIONED_BRANCH,
    compile_production_static_audit,
    validate_production_static_audit,
)


class E2RV6ProductionStaticAuditTests(unittest.TestCase):
    def _compile_source(self, source: str) -> dict[str, object]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)
        relative = "src/e2r/cli/fixture.py"
        path = repo / relative
        path.parent.mkdir(parents=True)
        path.write_text(source, encoding="utf-8")
        return dict(
            compile_production_static_audit(
                repo_root=repo,
                entrypoint_paths=(relative,),
                config_paths=(),
                auxiliary_paths=(),
                test_mode=True,
            )
        )

    def _compile_config(self, suffix: str, text: str) -> dict[str, object]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)
        entry = repo / "src/e2r/cli/fixture.py"
        entry.parent.mkdir(parents=True)
        entry.write_text("def main():\n    return 0\n", encoding="utf-8")
        relative = f"configs/production.{suffix}"
        config = repo / relative
        config.parent.mkdir(parents=True)
        config.write_text(text, encoding="utf-8")
        return dict(
            compile_production_static_audit(
                repo_root=repo,
                entrypoint_paths=("src/e2r/cli/fixture.py",),
                config_paths=(relative,),
                auxiliary_paths=(),
                test_mode=True,
            )
        )

    def test_clean_positive_recomputes_all_zero_counts_and_exact_hash_roster(self) -> None:
        result = self._compile_source(
            """
from pathlib import Path

PROHIBITED_PROVIDER_DENYLIST = ("QWEN", "OLLAMA", "LOCAL_PROVIDER")
FORBIDDEN_INPUT_KEYS = ("gold_query", "gold_fact", "api_key")

def ready(receipt_valid: bool, output_root: Path) -> bool:
    return receipt_valid and output_root.is_file()
"""
        )

        self.assertEqual(result["status"], PRODUCTION_STATIC_AUDIT_PASS)
        self.assertEqual(result["critical_count_sum"], 0)
        counts = result["critical_counts"]
        self.assertIsInstance(counts, dict)
        self.assertTrue(all(counts[key] == 0 for key in REQUIRED_ZERO_COUNT_KEYS))
        self.assertEqual(result["scanned_file_count"], 1)
        self.assertTrue(validate_production_static_audit(result, allow_test_mode=True))

    def test_known_bad_target_name_or_symbol_conditioned_branch(self) -> None:
        result = self._compile_source(
            'def route(symbol):\n    if symbol == "005930":\n        return "special"\n    return "normal"\n'
        )
        self.assertEqual(result["critical_counts"][TARGET_CONDITIONED_BRANCH], 1)

    def test_known_bad_target_dispatch_map_is_followed_by_dataflow(self) -> None:
        result = self._compile_source(
            "def special():\n    return 1\n\n"
            'routes = {"005930": special}\n\n'
            "def route(symbol):\n    return routes[symbol]()\n"
        )
        self.assertEqual(result["critical_counts"][TARGET_CONDITIONED_BRANCH], 1)

    def test_runtime_package_initializers_are_inside_the_import_scope(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)
        (repo / "src/e2r/cli").mkdir(parents=True)
        (repo / "src/e2r/__init__.py").write_text(
            'def route(symbol):\n    return 1 if symbol == "005930" else 0\n',
            encoding="utf-8",
        )
        (repo / "src/e2r/cli/__init__.py").write_text("", encoding="utf-8")
        (repo / "src/e2r/cli/fixture.py").write_text(
            "def main():\n    return 0\n",
            encoding="utf-8",
        )
        result = compile_production_static_audit(
            repo_root=repo,
            entrypoint_paths=("src/e2r/cli/fixture.py",),
            config_paths=(),
            auxiliary_paths=(),
            test_mode=True,
        )
        roster_paths = {row["path"] for row in result["file_roster"]}
        self.assertIn("src/e2r/__init__.py", roster_paths)
        self.assertIn("src/e2r/cli/__init__.py", roster_paths)
        self.assertEqual(result["critical_counts"][TARGET_CONDITIONED_BRANCH], 1)

    def test_known_bad_fixed_expected_score(self) -> None:
        result = self._compile_source("expected_total_score = 87.5\n")
        self.assertEqual(result["critical_counts"][FIXED_EXPECTED_SCORE], 1)

    def test_known_bad_fixed_expected_stage(self) -> None:
        result = self._compile_source('expected_stage = "3-Green"\n')
        self.assertEqual(result["critical_counts"][FIXED_EXPECTED_STAGE], 1)

    def test_known_bad_gold_path_wired_to_production_input(self) -> None:
        result = self._compile_source(
            'production_input_path = "data/gold/material_facts.jsonl"\n'
        )
        self.assertEqual(result["critical_counts"][GOLD_PRODUCTION_INPUT], 1)

    def test_known_bad_automatic_local_fallback(self) -> None:
        result = self._compile_source("automatic_local_fallback = True\n")
        self.assertEqual(result["critical_counts"][AUTOMATIC_LOCAL_FALLBACK], 1)

    def test_known_bad_executable_local_provider(self) -> None:
        result = self._compile_source(
            "import ollama\n\ndef run():\n    return ollama.Client()\n"
        )
        self.assertGreaterEqual(
            result["critical_counts"][EXECUTABLE_LOCAL_PROVIDER],
            1,
        )

    def test_known_bad_generic_local_provider_route_and_loopback_endpoint(self) -> None:
        result = self._compile_source(
            'provider = "local"\nprovider_endpoint = "http://127.0.0.1:11434/api"\n'
        )
        self.assertEqual(
            result["critical_counts"][EXECUTABLE_LOCAL_PROVIDER],
            2,
        )

    def test_known_bad_absolute_reviewer_path_identity(self) -> None:
        result = self._compile_source('reviewer_id = "/root/phase108_reviewer"\n')
        self.assertEqual(result["critical_counts"][ABSOLUTE_REVIEWER_IDENTITY], 1)

    def test_known_bad_secret_literal(self) -> None:
        result = self._compile_source('api_key = "sk-production-literal"\n')
        self.assertEqual(result["critical_counts"][SECRET_LITERAL], 1)

    def test_known_bad_output_only_readiness_dependency(self) -> None:
        result = self._compile_source(
            "from pathlib import Path\n"
            'output_root = Path("output/run")\n'
            "ready = output_root.exists()\n"
        )
        self.assertEqual(result["critical_counts"][OUTPUT_ONLY_READINESS], 1)

    def test_json_secret_local_fallback_and_gold_input_are_detected(self) -> None:
        result = self._compile_config(
            "json",
            json.dumps(
                {
                    "dart_api_key": "literal-json-secret",
                    "automatic_local_fallback": True,
                    "production": {
                        "inputs": {"path": "data/gold/facts.jsonl"}
                    },
                }
            ),
        )
        counts = result["critical_counts"]
        self.assertEqual(counts[SECRET_LITERAL], 1)
        self.assertEqual(counts[AUTOMATIC_LOCAL_FALLBACK], 1)
        self.assertEqual(counts[GOLD_PRODUCTION_INPUT], 1)

    def test_yaml_secret_local_fallback_and_gold_input_are_detected(self) -> None:
        result = self._compile_config(
            "yml",
            "\n".join(
                (
                    "OPENAI_API_KEY: literal-yaml-secret",
                    "automatic_local_fallback: true",
                    "production_input_path: data/gold/facts.jsonl",
                    "",
                )
            ),
        )
        counts = result["critical_counts"]
        self.assertEqual(counts[SECRET_LITERAL], 1)
        self.assertEqual(counts[AUTOMATIC_LOCAL_FALLBACK], 1)
        self.assertEqual(counts[GOLD_PRODUCTION_INPUT], 1)

    def test_workflow_secret_reference_is_not_a_literal_secret(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)
        entry = repo / "src/e2r/cli/fixture.py"
        entry.parent.mkdir(parents=True)
        entry.write_text("def main():\n    return 0\n", encoding="utf-8")
        relative = ".github/workflows/verify.yml"
        workflow = repo / relative
        workflow.parent.mkdir(parents=True)
        workflow.write_text(
            "jobs:\n  verify:\n    env:\n      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}\n",
            encoding="utf-8",
        )
        result = compile_production_static_audit(
            repo_root=repo,
            entrypoint_paths=("src/e2r/cli/fixture.py",),
            config_paths=(),
            auxiliary_paths=(relative,),
            test_mode=True,
        )
        self.assertEqual(result["critical_counts"][SECRET_LITERAL], 0)
        self.assertEqual(result["status"], PRODUCTION_STATIC_AUDIT_PASS)

    def test_missing_auxiliary_path_is_a_hard_failure(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)
        entry = repo / "src/e2r/cli/fixture.py"
        entry.parent.mkdir(parents=True)
        entry.write_text("def main():\n    return 0\n", encoding="utf-8")
        result = compile_production_static_audit(
            repo_root=repo,
            entrypoint_paths=("src/e2r/cli/fixture.py",),
            config_paths=(),
            auxiliary_paths=(".github/workflows/required_verify.yml",),
            test_mode=True,
        )
        self.assertEqual(result["status"], PRODUCTION_STATIC_AUDIT_FAIL)
        self.assertEqual(result["critical_counts"]["missing_scope_path_count"], 1)

    def test_unresolved_required_local_import_is_a_hard_failure(self) -> None:
        result = self._compile_source(
            "import e2r.production.module_that_does_not_exist\n"
        )
        self.assertEqual(result["status"], PRODUCTION_STATIC_AUDIT_FAIL)
        self.assertEqual(
            result["critical_counts"]["unresolved_local_import_count"],
            1,
        )

    def test_leaf_validation_rejects_self_reported_zero_and_roster_forgery(self) -> None:
        result = self._compile_source("def main():\n    return 0\n")
        forged = json.loads(json.dumps(result))
        forged["file_roster"] = []
        forged["scanned_file_count"] = 0
        self.assertFalse(
            validate_production_static_audit(
                forged,
                recomputed=result,
                allow_test_mode=True,
            )
        )

    def test_file_roster_hash_changes_when_scanned_source_bytes_change(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)
        relative = "src/e2r/cli/fixture.py"
        path = repo / relative
        path.parent.mkdir(parents=True)
        path.write_text("def main():\n    return 0\n", encoding="utf-8")
        first = compile_production_static_audit(
            repo_root=repo,
            entrypoint_paths=(relative,),
            config_paths=(),
            auxiliary_paths=(),
            test_mode=True,
        )
        path.write_text("def main():\n    return 1\n", encoding="utf-8")
        second = compile_production_static_audit(
            repo_root=repo,
            entrypoint_paths=(relative,),
            config_paths=(),
            auxiliary_paths=(),
            test_mode=True,
        )
        self.assertNotEqual(first["file_roster_hash"], second["file_roster_hash"])
        self.assertNotEqual(
            first["file_roster"][0]["sha256"],
            second["file_roster"][0]["sha256"],
        )

    def test_production_scope_cannot_be_replaced(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be replaced"):
            compile_production_static_audit(
                entrypoint_paths=("src/e2r/cli/fixture.py",),
            )

    def test_cli_writes_explicit_check_copy_and_returns_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / PRODUCTION_STATIC_AUDIT_LEAF
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = static_cli_main(
                    [
                        "--repo-root",
                        ".",
                        "--output",
                        str(output),
                    ]
                )
            payload = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(exit_code, 0)
        self.assertEqual(payload["status"], PRODUCTION_STATIC_AUDIT_PASS)
        roster_paths = {row["path"] for row in payload["file_roster"]}
        self.assertIn(
            ".github/workflows/e2r_v6_operational_cutover_verify.yml",
            roster_paths,
        )
        self.assertIn(
            "scripts/run_e2r_v6_clean_clone_reproduction.py",
            roster_paths,
        )
        self.assertIn(
            "requirements/e2r_v6_clean_clone_py310_linux_x86_64.lock",
            roster_paths,
        )
        self.assertIn(PRODUCTION_STATIC_AUDIT_PASS, stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
