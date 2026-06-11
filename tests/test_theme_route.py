import unittest
import subprocess
from datetime import date
from pathlib import Path
from unittest.mock import patch

from e2r.llm import CodexCLIThemeRouteProvider, ThemeRouteInput, build_theme_route_provider_from_env, validate_theme_route_output


class ThemeRouteTests(unittest.TestCase):
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

    def test_validate_theme_route_output_maps_insufficient_evidence_to_no_transition(self):
        output = validate_theme_route_output(
            {
                "status": "insufficient_evidence",
                "route_confidence": 0.3,
                "suggested_queries": ["테스트 매출 연결"],
                "blocked_reason": "source-backed evidence is missing",
            }
        )

        self.assertEqual(output.status, "no_transition")
        self.assertEqual(output.suggested_queries, ("테스트 매출 연결",))
        self.assertEqual(output.blocked_reason, "source-backed evidence is missing")

    def test_codex_cli_theme_provider_uses_schema_and_validates_output(self):
        provider = CodexCLIThemeRouteProvider(codex_command="codex", working_directory="/repo", timeout_seconds=30)

        def fake_run(command, *, input, text, capture_output, timeout, check):
            self.assertIn("codex", command[0])
            self.assertIn("--sandbox", command)
            self.assertIn("read-only", command)
            self.assertIn("--ask-for-approval", command)
            self.assertIn("never", command)
            self.assertIn("--output-schema", command)
            self.assertIn("-C", command)
            self.assertIn("/repo", command)
            self.assertIn("Return exactly one JSON object", input)
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

        with patch("e2r.llm.codex_theme_provider.subprocess.run", side_effect=fake_run):
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
            "e2r.llm.codex_theme_provider.subprocess.run",
            return_value=subprocess.CompletedProcess(["codex"], 1, "", "not logged in"),
        ):
            output = provider.route(
                ThemeRouteInput(company_name="테스트", symbol="000000", as_of_date=date(2026, 6, 8), market="KR")
            )

        self.assertEqual(output.status, "provider_error")
        self.assertIn("not logged in", output.blocked_reason)

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


if __name__ == "__main__":
    unittest.main()
