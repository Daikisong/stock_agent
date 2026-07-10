import ast
import json
import unittest
from pathlib import Path

from e2r.research_brain.canonical import (
    CANONICAL_INTELLIGENCE_NAMESPACE,
    canonical_architecture,
)


class ResearchBrainSingleSourceOfTruthTests(unittest.TestCase):
    def test_canonical_architecture_declares_one_schema_source(self) -> None:
        architecture = canonical_architecture()
        self.assertEqual(architecture.namespace, CANONICAL_INTELLIGENCE_NAMESPACE)
        self.assertEqual(architecture.schema_source_count, 1)
        self.assertFalse(architecture.legacy_imports_allowed)
        self.assertFalse(architecture.scoring_mutation_allowed)
        self.assertFalse(architecture.stage_mutation_allowed)
        self.assertFalse(architecture.historical_outcome_in_runtime_prompt_allowed)
        self.assertEqual(
            set(architecture.capabilities),
            {"corpus", "compiler", "recipes", "retrieval", "planning", "replay", "runtime"},
        )

    def test_canonical_package_tree_exists(self) -> None:
        root = Path("src/e2r/research_brain")
        for package in ("corpus", "compiler", "recipes", "retrieval", "planning", "replay", "runtime"):
            self.assertTrue((root / package / "__init__.py").is_file(), package)

    def test_canonical_cli_surface_is_wired_and_ready_label_is_gated(self) -> None:
        cli_root = Path("src/e2r/cli")
        status_text = Path(
            "src/e2r/research_brain/runtime/command_status.py"
        ).read_text(encoding="utf-8")
        self.assertIn("RECONSTRUCTION_COMPONENT_NOT_READY", status_text)
        compile_text = (cli_root / "compile_e2r_research_intelligence.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("compile_research_intelligence", compile_text)
        self.assertNotIn("MEANINGFUL_E2R_RUNTIME_READY", compile_text)
        replay_text = (cli_root / "run_e2r_historical_replay.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("compile_canonical_frozen_replay", replay_text)
        self.assertIn("build_command_run_manifest", replay_text)
        self.assertNotIn("reconstruction_pending_payload", replay_text)
        self.assertNotIn("MEANINGFUL_E2R_RUNTIME_READY", replay_text)

        current_text = (cli_root / "run_e2r_current_operation.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("run_current_daily_census", current_text)
        self.assertIn("write_current_source_pending_run", current_text)
        self.assertIn("build_command_run_manifest", current_text)
        self.assertNotIn("reconstruction_pending_payload", current_text)
        self.assertNotIn("MEANINGFUL_E2R_RUNTIME_READY", current_text)

        audit_text = (cli_root / "audit_e2r_evidence_intelligence.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("run_independent_review", audit_text)
        self.assertIn("build_command_run_manifest", audit_text)
        self.assertIn('final_status == _READY', audit_text)
        self.assertNotIn("reconstruction_pending_payload", audit_text)

    def test_canonical_modules_never_import_legacy_namespaces(self) -> None:
        root = Path("src/e2r/research_brain")
        forbidden = ("e2r.research_reverse", "e2r.source_routing")
        findings: list[str] = []
        for path in root.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                names: list[str] = []
                if isinstance(node, ast.Import):
                    names.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    names.append(node.module)
                for name in names:
                    if name.startswith(forbidden):
                        findings.append(f"{path}:{node.lineno}:{name}")
        self.assertEqual(findings, [])

    def test_phase1_call_graph_records_hard_acceptance(self) -> None:
        path = Path("docs/operational/e2r_runtime_call_graph_after_phase1.json")
        payload = json.loads(path.read_text(encoding="utf-8"))
        acceptance = payload["acceptance"]
        self.assertEqual(acceptance["duplicate_brain_schema_source_of_truth_count"], 1)
        self.assertEqual(acceptance["production_reachable_legacy_research_reverse_count"], 0)
        self.assertEqual(
            acceptance["production_reachable_primitive_name_route_guesser_count"],
            0,
        )
        self.assertEqual(acceptance["old_cli_canonical_ready_label_capability_count"], 0)
        self.assertEqual(acceptance["status"], "UNIFIED_RESEARCH_BRAIN_ARCHITECTURE_PASS")


if __name__ == "__main__":
    unittest.main()
