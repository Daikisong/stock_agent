from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import re
from types import SimpleNamespace
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch

from e2r.codex_cli_contract import codex_subprocess_env
from e2r.cli import resume_e2r_researcher_fact_extraction as cli
from e2r.cli import run_agentic_adjudication as adjudication_cli
from e2r.cli import run_agentic_asof_snapshot_verifier as asof_verifier_cli
from e2r.cli import run_agentic_claim_extraction as claim_extraction_cli
from e2r.cli import run_agentic_primitive_mapping as primitive_mapping_cli
from e2r.cli import run_agentic_replacement_snapshot_verifier as replacement_verifier_cli
from e2r.cli import run_agentic_same_event_replacement_planner as replacement_planner_cli
from e2r.cli import run_e2r_researcher_mode_until_pass as full_cli
from e2r.production.claim_extraction.extractor_provider import CodexCLIExtractorProvider
from e2r.research_brain.planning import provider_transport
from e2r.research_brain.researcher_mode import component_researcher
import e2r.research_brain.researcher_mode as researcher_mode
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeConfig,
    CurrentResearchTarget,
    resume_current_fact_extraction_checkpoint,
)


class FactExtractionRecoveryCliTest(unittest.TestCase):
    def test_local_model_names_exist_only_in_audit_only_source_files(self):
        """Static guard: production source cannot regain a local LLM route.

        The two allowed files contain denylist tombstones only.  They inspect
        persisted lineage and reject it; neither file constructs a provider or
        opens a model endpoint.
        """

        source_root = Path(__file__).resolve().parents[1] / "src" / "e2r"
        allowed_audit_only_files = {
            source_root
            / "research_brain"
            / "researcher_mode"
            / "source_graph_explorer.py",
            source_root
            / "research_brain"
            / "researcher_mode"
            / "tracked_receipts.py",
        }
        forbidden_runtime_pattern = re.compile(
            r"(?i)(?:\bollama\b|\bqwen(?:\d+(?:\.\d+)?)?\b|"
            r"llama\.cpp|\blm[ _-]?studio\b|11434)"
        )
        matching_files = {
            path
            for path in source_root.rglob("*.py")
            if forbidden_runtime_pattern.search(path.read_text(encoding="utf-8"))
        }

        self.assertEqual(matching_files, allowed_audit_only_files)

    def test_codex_subprocess_environment_drops_every_routing_override(self):
        # Pure dictionary test: this does not open a socket or start a provider.
        # The values are deliberately inert and prove that even named routing
        # variables cannot cross the Codex subprocess boundary.
        sanitized = codex_subprocess_env(
            {
                "PATH": "/usr/bin",
                "HOME": "/home/test",
                "OPENAI_API_KEY": "secret",
                "OPENAI_BASE_URL": "https://forbidden.invalid/v1",
                "OPENAI_API_BASE": "https://forbidden.invalid/v1",
                "OLLAMA_HOST": "https://forbidden.invalid",
                "HTTP_PROXY": "https://forbidden.invalid",
                "HTTPS_PROXY": "https://forbidden.invalid",
                "CODEX_HOME": "/tmp/redirected-config",
                "E2R_CODEX_PLANNER_COMMAND": "local-provider",
            }
        )

        self.assertEqual(sanitized["PATH"], "/usr/bin")
        self.assertEqual(sanitized["HOME"], "/home/test")
        self.assertEqual(sanitized["OPENAI_API_KEY"], "secret")
        self.assertNotIn("OPENAI_BASE_URL", sanitized)
        self.assertNotIn("OPENAI_API_BASE", sanitized)
        self.assertNotIn("OLLAMA_HOST", sanitized)
        self.assertNotIn("HTTP_PROXY", sanitized)
        self.assertNotIn("HTTPS_PROXY", sanitized)
        self.assertNotIn("CODEX_HOME", sanitized)
        self.assertNotIn("E2R_CODEX_PLANNER_COMMAND", sanitized)

    def test_local_llm_runtime_types_are_not_importable_or_exported(self):
        # Denylist regression only.  Importing these production modules must
        # never expose a constructible local-model runtime.
        self.assertFalse(
            hasattr(provider_transport, "OllamaStructuredProviderTransport")
        )
        self.assertFalse(
            hasattr(component_researcher, "OllamaResearcherProvider")
        )
        self.assertFalse(
            hasattr(researcher_mode, "OllamaResearcherProvider")
        )

    def test_cli_uses_only_collaboration_provider_and_reports_pending(self):
        target = CurrentResearchTarget("005930", "삼성전자", ("Samsung",))
        result = SimpleNamespace(
            status="FACT_EXTRACTION_PENDING",
            facts=(),
            material_claims=(),
            provider_calls=(object(),),
            pending_reasons=(
                "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:"
                "COLLABORATION_RESPONSE_PENDING:COLLABREQ-"
                + "a" * 64,
            ),
        )
        provider = object()
        output = StringIO()
        with (
            patch.object(cli, "load_current_research_target_registry", return_value=({},)),
            patch.object(cli, "load_current_research_targets", return_value=(target,)),
            patch.object(
                cli.CollaborationCodexResearcherProvider,
                "default",
                return_value=provider,
            ),
            patch.object(
                cli,
                "resume_current_fact_extraction_checkpoint",
                return_value=result,
            ) as resume,
            redirect_stdout(output),
        ):
            status = cli.main(
                [
                    "--as-of-date",
                    "2026-07-12",
                    "--symbols",
                    "005930",
                    "--archetype",
                    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "--output-root",
                    "output/recovery",
                    "--fact-documents-per-call",
                    "2",
                ]
            )
        self.assertEqual(status, 2)
        self.assertIn('"provider_route": "COLLABORATION_CODEX_SUBAGENT"', output.getvalue())
        self.assertIn('"score_or_stage_authority": false', output.getvalue())
        self.assertIs(resume.call_args.kwargs["provider"], provider)
        self.assertEqual(
            resume.call_args.kwargs["config"].fact_documents_per_call,
            2,
        )

    def test_cli_returns_zero_only_when_every_target_fact_leaf_is_complete(self):
        targets = (
            CurrentResearchTarget("005930", "삼성전자"),
            CurrentResearchTarget("000660", "SK하이닉스"),
        )
        complete = SimpleNamespace(
            status="FACT_EXTRACTION_COMPLETE",
            facts=(object(),),
            material_claims=(object(),),
            provider_calls=(object(),),
            pending_reasons=(),
        )
        with (
            patch.object(cli, "load_current_research_target_registry", return_value=({},)),
            patch.object(cli, "load_current_research_targets", return_value=targets),
            patch.object(
                cli.CollaborationCodexResearcherProvider,
                "default",
                return_value=object(),
            ),
            patch.object(
                cli,
                "resume_current_fact_extraction_checkpoint",
                side_effect=(complete, complete),
            ),
            redirect_stdout(StringIO()),
        ):
            status = cli.main(
                [
                    "--as-of-date",
                    "2026-07-12",
                    "--symbols",
                    "005930,000660",
                    "--archetype",
                    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "--output-root",
                    "output/recovery",
                ]
            )
        self.assertEqual(status, 0)

    def test_clis_do_not_expose_a_local_llm_provider_or_option(self):
        # Parser-only regression.  Inspect the parser schema without supplying
        # an endpoint value or starting any provider process.
        full_parser = full_cli.build_parser()
        full_provider_action = next(
            action
            for action in full_parser._actions
            if action.dest == "research_provider"
        )
        self.assertEqual(
            tuple(full_provider_action.choices or ()),
            ("codex", "codex-subagent", "codex-collaboration"),
        )
        self.assertFalse(
            any(
                action.dest == "research_provider"
                for action in cli.build_parser()._actions
            )
        )
        agentic_parsers = (
            adjudication_cli.build_arg_parser(),
            asof_verifier_cli.build_arg_parser(),
            claim_extraction_cli.build_arg_parser(),
            primitive_mapping_cli.build_arg_parser(),
            replacement_verifier_cli.build_arg_parser(),
            replacement_planner_cli.build_arg_parser(),
        )
        for parser in (cli.build_parser(), full_parser, *agentic_parsers):
            option_names = {
                option
                for action in parser._actions
                for option in action.option_strings
            }
            self.assertFalse(
                any(
                    forbidden in option.casefold()
                    for option in option_names
                    for forbidden in ("ollama", "qwen")
                )
            )
            self.assertNotIn("--reasoning-effort", option_names)

        with self.assertRaises(TypeError):
            CodexCLIExtractorProvider(model="custom-model")

    def test_full_and_recovery_clis_share_the_fact_transport_batch_option(self):
        recovery = cli.build_parser().parse_args(
            [
                "--as-of-date",
                "2026-07-12",
                "--symbols",
                "005930",
                "--archetype",
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "--output-root",
                "output/recovery",
                "--fact-documents-per-call",
                "2",
            ]
        )
        full = full_cli.build_parser().parse_args(
            [
                "--as-of-date",
                "2026-07-12",
                "--symbols",
                "005930",
                "--archetype",
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "--live-materialization-authorized",
                "true",
                "--checkpoint-resume",
                "true",
                "--gold-lane-isolated",
                "true",
                "--require-researcher-parity",
                "true",
                "--output-root",
                "output/recovery",
                "--fact-documents-per-call",
                "2",
            ]
        )
        self.assertEqual(recovery.fact_documents_per_call, 2)
        self.assertEqual(full.fact_documents_per_call, 2)


class FactExtractionRecoveryFunctionTest(unittest.TestCase):
    def test_config_rejects_invalid_fact_transport_batch(self):
        for value in (True, 0, -1, 1.5, "2"):
            with self.subTest(value=value), self.assertRaisesRegex(
                ValueError,
                "positive transport batch",
            ):
                CurrentResearcherModeConfig(
                    as_of_date="2026-07-12",
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    output_root="output/recovery",
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                    gold_lane_isolated=True,
                    require_researcher_parity=True,
                    fact_documents_per_call=value,
                )

    def test_recovery_function_rejects_nonproduction_source_semantics(self):
        with TemporaryDirectory() as directory:
            config = CurrentResearcherModeConfig(
                as_of_date="2026-07-12",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                output_root=directory,
                live_materialization_authorized=True,
                checkpoint_resume=True,
                gold_lane_isolated=True,
                require_researcher_parity=True,
                source_acquisition_mode="TEST",
            )
            with self.assertRaisesRegex(
                ValueError,
                "restricted to production daily checkpoints",
            ):
                resume_current_fact_extraction_checkpoint(
                    config=config,
                    target=CurrentResearchTarget("005930", "삼성전자"),
                    provider=Mock(),
                )

    def test_missing_source_checkpoint_fails_before_provider_configuration(self):
        with TemporaryDirectory() as directory:
            config = CurrentResearcherModeConfig(
                as_of_date="2026-07-12",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                output_root=directory,
                live_materialization_authorized=True,
                checkpoint_resume=True,
                gold_lane_isolated=True,
                require_researcher_parity=True,
            )
            provider = Mock()
            with self.assertRaisesRegex(
                ValueError,
                "requires a source graph checkpoint",
            ):
                resume_current_fact_extraction_checkpoint(
                    config=config,
                    target=CurrentResearchTarget("005930", "삼성전자"),
                    provider=provider,
                )
            provider.configure_response_cache.assert_not_called()


if __name__ == "__main__":
    unittest.main()
