from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from types import SimpleNamespace
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch

from e2r.cli import resume_e2r_researcher_fact_extraction as cli
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeConfig,
    CurrentResearchTarget,
    resume_current_fact_extraction_checkpoint,
)


class FactExtractionRecoveryCliTest(unittest.TestCase):
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
                ]
            )
        self.assertEqual(status, 2)
        self.assertIn('"provider_route": "COLLABORATION_CODEX_SUBAGENT"', output.getvalue())
        self.assertIn('"score_or_stage_authority": false', output.getvalue())
        self.assertIs(resume.call_args.kwargs["provider"], provider)

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

    def test_cli_does_not_expose_an_ollama_or_qwen_provider_switch(self):
        with (
            self.assertRaises(SystemExit),
            redirect_stdout(StringIO()),
            redirect_stderr(StringIO()),
        ):
            cli.build_parser().parse_args(
                [
                    "--as-of-date",
                    "2026-07-12",
                    "--symbols",
                    "005930",
                    "--archetype",
                    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "--output-root",
                    "output/recovery",
                    "--research-provider",
                    "ollama",
                ]
            )


class FactExtractionRecoveryFunctionTest(unittest.TestCase):
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
