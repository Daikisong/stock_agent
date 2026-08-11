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

        The allowed files contain denylist tombstones only.  They inspect
        persisted lineage and reject it; none of these files constructs a provider or
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
            source_root / "production" / "v6_provider_runtime_audit.py",
            source_root / "production" / "v6_production_static_audit.py",
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

    def test_fact_only_resume_routes_authority_gap_to_exact_journal_replay(self):
        target = CurrentResearchTarget("005930", "삼성전자", ("Samsung",))
        as_of_date = "2026-07-12"
        document_id = "SGDOC-" + "a" * 24
        source_checkpoint = {
            "target_id": target.target_id,
            "target_name": target.company_name,
            "as_of_date": as_of_date,
            "checkpoint_id": "SGCHECK-CURRENT",
            "checkpoint_hash": "s" * 64,
            "resumed_from_checkpoint_id": "SGCHECK-AUTHORITY",
            "production_downstream_document_ids": [document_id],
            "evidence_documents": [{"document_id": document_id}],
        }
        authority_facts = (
            {
                "fact_id": "EFACT-AUTHORITY",
                "target_id": target.target_id,
                "as_of_date": as_of_date,
                "source_ids": [document_id],
            },
        )
        ledger = object()
        binding = SimpleNamespace(
            seed_source_document_ids=(document_id,),
            pending_new_fact_ids=(),
        )
        authority_context = {
            "target_id": target.target_id,
            "as_of_date": as_of_date,
            "facts": authority_facts,
            "authoritative_fact_ledger_available": True,
            "authoritative_fact_lineage_recovery_required": True,
            "pending_new_fact_epoch_commit_required": False,
            "pending_new_fact_ids": (),
            "authoritative_fact_ledger": ledger,
            "authoritative_recovery_expectation": {
                "status": "AUTHORITY_LOSS_RECOVERY_REQUIRED",
                "expected_recovered_source_document_ids": [document_id],
            },
            "source_graph_checkpoint_id": "SGCHECK-CURRENT",
            "source_graph_checkpoint_hash": "s" * 64,
        }
        prior_context = {
            "facts": authority_facts,
            "research_gap_feedback": (),
            "structured_gap_context": {},
            "score_gap_context": {},
            "supervisor_source_gap_context": {},
        }
        prior_fact = {
            "prior_material_claims": (),
            "prior_document_dispositions": (),
            "prior_provider_calls": (),
            "prior_rejections": (),
        }
        source_graph = SimpleNamespace(
            status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
            evidence_documents=(
                {
                    "document_id": document_id,
                    "target_id": target.target_id,
                    "as_of_date": as_of_date,
                },
            ),
            checkpoint={**source_checkpoint, "pending_reasons": []},
            audit={"critical_count_sum": 0},
        )
        result = SimpleNamespace(
            status="FACT_EXTRACTION_COMPLETE",
            facts=(),
        )
        extractor = Mock()
        extractor.extract.return_value = result
        provider = Mock()
        provider.semantic_prompt_chunk_chars = 220_000
        events = []

        with TemporaryDirectory() as directory:
            target_root = Path(directory) / target.target_id
            target_root.mkdir(parents=True)
            (target_root / "source_graph_checkpoint.json").write_text(
                "{}\n", encoding="utf-8"
            )
            config = CurrentResearcherModeConfig(
                as_of_date=as_of_date,
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                output_root=directory,
                live_materialization_authorized=True,
                checkpoint_resume=True,
                gold_lane_isolated=True,
                require_researcher_parity=True,
            )
            module = (
                "e2r.research_brain.researcher_mode.current_researcher_mode."
            )
            with (
                patch(module + "load_source_graph_checkpoint", return_value=source_checkpoint),
                patch(
                    module + "validate_source_graph_checkpoint",
                    return_value=source_checkpoint,
                ),
                patch(
                    module + "_load_authoritative_prior_fact_context",
                    side_effect=lambda *args, **kwargs: (
                        events.append("authority_loaded") or authority_context
                    ),
                ),
                patch(
                    module + "_hydrate_readonly_source_graph_run",
                    side_effect=lambda **kwargs: (
                        events.append("source_replayed") or source_graph
                    ),
                ) as hydrate,
                patch(
                    module + "_load_prior_research_context",
                    return_value=prior_context,
                ),
                patch(module + "_load_fact_checkpoint", return_value=prior_fact),
                patch(
                    module + "resolve_current_fact_lineage_recovery_binding",
                    return_value=binding,
                ) as resolve_binding,
                patch(
                    module + "ResearcherEvidenceFactExtractor",
                    return_value=extractor,
                ),
                patch(module + "write_researcher_fact_extraction_result"),
                patch(module + "write_jsonl"),
            ):
                recovered = resume_current_fact_extraction_checkpoint(
                    config=config,
                    target=target,
                    provider=provider,
                )

            self.assertIs(recovered, result)
            self.assertEqual(events, ["authority_loaded", "source_replayed"])
            self.assertTrue(
                hydrate.call_args.kwargs[
                    "authoritative_fact_lineage_recovery"
                ]["authoritative_fact_lineage_recovery_required"]
            )
            resolve_binding.assert_called_once()
            self.assertEqual(
                resolve_binding.call_args.kwargs["journal_root"],
                target_root / "collaboration_codex_subagent_provider",
            )

        provider.complete.assert_not_called()
        extraction_kwargs = extractor.extract.call_args.kwargs
        self.assertIs(extraction_kwargs["authoritative_fact_ledger"], ledger)
        self.assertIs(
            extraction_kwargs["current_fact_lineage_recovery_binding"],
            binding,
        )
        self.assertEqual(extraction_kwargs["current_facts"], authority_facts)


if __name__ == "__main__":
    unittest.main()
