import os
import unittest
import subprocess
import tempfile
from datetime import date
from pathlib import Path
from unittest.mock import patch

from e2r.llm import (
    CodexCLIThemeRouteProvider,
    ThemeRouteInput,
    build_default_codex_theme_route_provider,
    build_theme_route_messages,
    build_theme_route_provider_from_env,
    validate_theme_route_output,
)
from e2r.llm.codex_theme_provider import _json_object_from_text as _theme_json_object_from_text
from e2r.llm.prompts import E2R_RESEARCH_ANALYST_SYSTEM_PROMPT, E2R_THEME_ROUTE_SYSTEM_PROMPT


class ThemeRouteTests(unittest.TestCase):
    def test_codex_theme_json_repair_reads_first_valid_balanced_object(self):
        payload = 'warning {not json}\\n```json\\n{"status":"needs_more_evidence"}\\n```\\ntrailing {bad'

        parsed = _theme_json_object_from_text(payload)

        self.assertEqual(parsed, {"status": "needs_more_evidence"})

    def test_validate_theme_route_output_strips_stage_override_and_coerces_fields(self):
        output = validate_theme_route_output(
            {
                "status": "transition_detected",
                "transition_detected": "true",
                "confidence": "0.7",
                "emerging_theme_id": "AI_INFRA_PLATFORM_DATACENTER",
                "stage": "3-Green",
                "normalized_parsed_fields": {
                    "gpu_cloud_revenue_visible": "True",
                    "cloud_revenue_growth_pct": "40%",
                    "stage_override": "3-Green",
                },
                "diagnostic_scores": {"bad": "not-a-number", "theme": "80"},
            }
        )

        self.assertTrue(output.transition_detected)
        self.assertEqual(output.route_confidence, 0.7)
        self.assertNotIn("stage_override", output.normalized_parsed_fields)
        self.assertTrue(output.normalized_parsed_fields["gpu_cloud_revenue_visible"])
        self.assertEqual(output.normalized_parsed_fields["cloud_revenue_growth_pct"], 40.0)
        self.assertEqual(output.diagnostic_scores, {"theme": 80.0})

    def test_validate_theme_route_output_rejects_non_finite_numeric_fields(self):
        output = validate_theme_route_output(
            {
                "status": "transition_detected",
                "transition_detected": "nan",
                "route_confidence": "nan",
                "normalized_parsed_fields": {
                    "good_value": "40%",
                    "bad_value": float("nan"),
                },
                "diagnostic_scores": {
                    "bad_nan": "nan",
                    "bad_inf": float("inf"),
                    "good": "80",
                },
            }
        )

        self.assertFalse(output.transition_detected)
        self.assertEqual(output.route_confidence, 0.0)
        self.assertEqual(output.normalized_parsed_fields, {"good_value": 40.0})
        self.assertEqual(output.diagnostic_scores, {"good": 80.0})

    def test_validate_theme_route_output_maps_insufficient_evidence_to_more_research(self):
        output = validate_theme_route_output(
            {
                "status": "insufficient_evidence",
                "route_confidence": 0.3,
                "suggested_queries": ["테스트 매출 연결"],
                "blocked_reason": "source-backed evidence is missing",
            }
        )

        self.assertEqual(output.status, "needs_more_evidence")
        self.assertEqual(output.suggested_queries, ("테스트 매출 연결",))
        self.assertEqual(output.blocked_reason, "source-backed evidence is missing")

    def test_theme_route_prompt_requires_gap_expansion_queries(self):
        self.assertIn("score_gap_context", E2R_THEME_ROUTE_SYSTEM_PROMPT)
        self.assertIn("suggested_queries", E2R_THEME_ROUTE_SYSTEM_PROMPT)
        self.assertIn("do not stop", E2R_THEME_ROUTE_SYSTEM_PROMPT)
        self.assertNotIn("will not synthesize fallback search templates", E2R_THEME_ROUTE_SYSTEM_PROMPT)
        self.assertNotIn("Prefer insufficient_evidence=true", E2R_RESEARCH_ANALYST_SYSTEM_PROMPT)

        messages = build_theme_route_messages(
            ThemeRouteInput(
                company_name="테스트",
                symbol="000000",
                as_of_date=date(2026, 6, 8),
                market="KR",
                score_gap_context=("revision estimate consensus target price EPS OP FCF",),
            )
        )

        self.assertIn("score_gap_context", messages[1]["content"])
        self.assertIn("revision estimate consensus", messages[1]["content"])

    def test_codex_cli_theme_provider_uses_schema_and_validates_output(self):
        provider = CodexCLIThemeRouteProvider(codex_command="codex", working_directory="/repo", timeout_seconds=30)

        def fake_run(command, *, prompt, timeout):
            self.assertIn("codex", command[0])
            self.assertIn("--sandbox", command)
            self.assertIn("read-only", command)
            self.assertIn("--ask-for-approval", command)
            self.assertIn("never", command)
            self.assertIn("--output-schema", command)
            self.assertIn("-C", command)
            self.assertIn("/repo", command)
            self.assertIn("Return exactly one JSON object", prompt)
            output_path = Path(command[command.index("--output-last-message") + 1])
            output_path.write_text(
                """
                {
                  "status": "transition_detected",
                  "transition_detected": true,
                  "route_confidence": 0.72,
                  "emerging_theme_id": "AI_INFRA_PLATFORM_DATACENTER",
                  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                  "evidence_slots": [
                    {"slot": "revenue_bridge", "status": "present", "evidence_refs": ["ev-1"], "confidence": 0.8}
                  ],
                  "missing_information": ["fcf_bridge"],
                  "suggested_queries": ["테스트 클라우드 매출"],
                  "normalized_parsed_fields": {"gpu_cloud_revenue_visible": true, "stage_override": "3-Green"},
                  "diagnostic_scores": {"agent_confidence": 72}
                }
                """,
                encoding="utf-8",
            )
            return subprocess.CompletedProcess(command, 0, "", "")

        with patch("e2r.llm.codex_theme_provider._run_codex_command", side_effect=fake_run):
            output = provider.route(
                ThemeRouteInput(
                    company_name="테스트",
                    symbol="000000",
                    as_of_date=date(2026, 6, 8),
                    market="KR",
                    sector="platform",
                )
            )

        self.assertEqual(output.status, "transition_detected")
        self.assertEqual(output.route_confidence, 0.72)
        self.assertEqual(output.evidence_slots[0].evidence_refs, ("ev-1",))
        self.assertTrue(output.normalized_parsed_fields["gpu_cloud_revenue_visible"])
        self.assertNotIn("stage_override", output.normalized_parsed_fields)

    def test_codex_cli_theme_provider_reports_cli_failure(self):
        provider = CodexCLIThemeRouteProvider(codex_command="codex")
        with patch(
            "e2r.llm.codex_theme_provider._run_codex_command",
            return_value=subprocess.CompletedProcess(["codex"], 1, "", "not logged in"),
        ):
            output = provider.route(
                ThemeRouteInput(company_name="테스트", symbol="000000", as_of_date=date(2026, 6, 8), market="KR")
            )

        self.assertEqual(output.status, "provider_error")
        self.assertIn("not logged in", output.blocked_reason)

    def test_codex_cli_theme_provider_reports_timeout(self):
        provider = CodexCLIThemeRouteProvider(codex_command="codex", timeout_seconds=0.01)
        with patch(
            "e2r.llm.codex_theme_provider._run_codex_command",
            side_effect=subprocess.TimeoutExpired(cmd=["codex"], timeout=0.01),
        ):
            output = provider.route(
                ThemeRouteInput(company_name="테스트", symbol="000000", as_of_date=date(2026, 6, 8), market="KR")
            )

        self.assertEqual(output.status, "provider_error")
        self.assertEqual(output.blocked_reason, "codex_cli_timeout")

    def test_codex_cli_theme_provider_uses_output_json_before_nonzero_exit(self):
        provider = CodexCLIThemeRouteProvider(codex_command="codex", working_directory="/repo", timeout_seconds=30)

        def fake_run(command, *, prompt, timeout):
            output_path = Path(command[command.index("--output-last-message") + 1])
            output_path.write_text(
                """
                {
                  "status": "mixed_route",
                  "transition_detected": true,
                  "route_confidence": 0.81,
                  "emerging_theme_id": "AI_MEMORY_DATACENTER",
                  "primary_route_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                  "canonical_archetype_id": "R2_SEMICONDUCTOR_HBM_MEMORY_SUPERCYCLE",
                  "secondary_archetype_ids": [],
                  "evidence_slots": [],
                  "missing_information": [],
                  "suggested_queries": [],
                  "normalized_parsed_fields": [],
                  "diagnostic_scores": [],
                  "blocked_reason": null
                }
                """,
                encoding="utf-8",
            )
            return subprocess.CompletedProcess(command, 1, "OpenAI Codex banner", "")

        with patch("e2r.llm.codex_theme_provider._run_codex_command", side_effect=fake_run):
            output = provider.route(
                ThemeRouteInput(company_name="테스트", symbol="000000", as_of_date=date(2026, 6, 8), market="KR")
            )

        self.assertEqual(output.status, "mixed_route")
        self.assertEqual(output.route_confidence, 0.81)
        self.assertEqual(output.large_sector_id, "L2_AI_SEMICONDUCTOR_ELECTRONICS")
        self.assertEqual(output.canonical_archetype_id, "R2_SEMICONDUCTOR_HBM_MEMORY_SUPERCYCLE")

    def test_theme_route_provider_env_factory_is_opt_in(self):
        self.assertIsNone(build_theme_route_provider_from_env({}))
        provider = build_theme_route_provider_from_env(
            {
                "E2R_THEME_ROUTE_PROVIDER": "codex",
                "E2R_CODEX_THEME_MODEL": "gpt-test",
                "E2R_CODEX_THEME_TIMEOUT_SECONDS": "45",
            },
            working_directory="/repo",
        )

        self.assertIsInstance(provider, CodexCLIThemeRouteProvider)
        self.assertEqual(provider.model, "gpt-test")
        self.assertEqual(provider.timeout_seconds, 45.0)
        self.assertEqual(str(provider.working_directory), "/repo")

    def test_theme_route_provider_env_factory_loads_project_env_when_not_explicit(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict("os.environ", {}, clear=True):
            env_path = Path(directory) / ".env"
            env_path.write_text(
                "\n".join(
                    (
                        "E2R_THEME_ROUTE_PROVIDER=codex",
                        "E2R_CODEX_THEME_MODEL=gpt-env-file",
                        "E2R_CODEX_THEME_TIMEOUT_SECONDS=77",
                    )
                ),
                encoding="utf-8",
            )
            old_cwd = Path.cwd()
            try:
                os.chdir(directory)
                provider = build_theme_route_provider_from_env(working_directory="/repo")
            finally:
                os.chdir(old_cwd)

        self.assertIsInstance(provider, CodexCLIThemeRouteProvider)
        self.assertEqual(provider.model, "gpt-env-file")
        self.assertEqual(provider.timeout_seconds, 77.0)
        self.assertEqual(str(provider.working_directory), "/repo")

    def test_default_codex_provider_preserves_env_config(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            "os.environ",
            {
                "E2R_CODEX_THEME_MODEL": "gpt-operating",
                "E2R_CODEX_THEME_TIMEOUT_SECONDS": "88",
            },
            clear=True,
        ):
            old_cwd = Path.cwd()
            try:
                os.chdir(directory)
                provider = build_default_codex_theme_route_provider(working_directory="/repo")
            finally:
                os.chdir(old_cwd)

        self.assertIsInstance(provider, CodexCLIThemeRouteProvider)
        self.assertEqual(provider.model, "gpt-operating")
        self.assertEqual(provider.timeout_seconds, 88.0)
        self.assertEqual(str(provider.working_directory), "/repo")


if __name__ == "__main__":
    unittest.main()
