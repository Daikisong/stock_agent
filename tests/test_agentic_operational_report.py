import json
import tempfile
import unittest
from pathlib import Path

from e2r.calibration.taxonomy import (
    ARCHETYPE_TO_LARGE_SECTOR,
    CANONICAL_ARCHETYPE_IDS,
)
from e2r.cli.run_agentic_operational_report import (
    build_operational_report_bundle,
    run_operational_report,
)


class AgenticOperationalReportTest(unittest.TestCase):
    def test_bundle_marks_ready_and_deprecates_legacy_live_results(self):
        bundle = build_operational_report_bundle(**_sample_inputs())

        self.assertEqual(bundle["summary"]["production_verdict"], "READY")
        self.assertEqual(bundle["source_gap_inventory"]["summary"]["unresolved_source_gap_count"], 0)
        self.assertEqual(
            bundle["legacy_quarantine_audit"]["summary"]["parser_keyword_direct_score_path_count"],
            0,
        )
        self.assertEqual(
            bundle["score_delta_audit"]["summary"]["non_comparable_legacy_comparison_count"],
            2,
        )
        self.assertIn("NON_COMPARABLE", bundle["deprecated_live_results_md"])
        self.assertIn("월덱스", bundle["deprecated_live_results_md"])

        sector_rows = {
            row["large_sector_id"]: row for row in bundle["sector_matrix"]["rows"]
        }
        self.assertEqual(
            sector_rows["L6_FINANCIAL_CAPITAL_RETURN_DIGITAL"][
                "required_bounded_smoke_archetype_count"
            ],
            2,
        )
        self.assertEqual(
            sector_rows["L9_CONSTRUCTION_REALESTATE_HOUSING"][
                "required_bounded_smoke_archetype_count"
            ],
            1,
        )
        self.assertTrue(
            bundle["sector_matrix"]["summary"]["actual_candidate_discovery_path_exercised"]
        )

    def test_cli_writes_required_operational_artifacts(self):
        inputs = _sample_inputs()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_paths = {}
            for name, value in inputs.items():
                if name in {"commit_sha", "generated_at", "test_summary"}:
                    continue
                path = root / f"{name}.json"
                path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
                input_paths[name] = path
            output_dir = root / "docs" / "operational"

            paths = run_operational_report(
                chain_audit_path=input_paths["chain_audit"],
                replay_acceptance_path=input_paths["replay_acceptance"],
                adversarial_acceptance_path=input_paths["adversarial_acceptance"],
                live_smoke_acceptance_path=input_paths["live_smoke_acceptance"],
                frozen_repeatability_acceptance_path=input_paths[
                    "frozen_repeatability_acceptance"
                ],
                source_backed_coverage_path=input_paths["source_backed_coverage"],
                replay_gap_plan_path=input_paths["replay_gap_plan"],
                score_contribution_path=input_paths["score_contributions"],
                score_snapshot_path=input_paths["score_snapshots"],
                stage_court_result_path=input_paths["stage_court_results"],
                discovery_run_log_path=input_paths["discovery_run_log"],
                discovery_candidates_path=input_paths["discovery_candidates"],
                output_directory=output_dir,
                commit_sha="abc123",
                generated_at="2026-06-28",
                test_pass_count=12,
                test_fail_count=0,
                test_skip_count=0,
            )

            expected = {
                "acceptance_report",
                "sector_matrix",
                "archetype_matrix",
                "replay_results",
                "live_smoke_results",
                "source_gap_inventory",
                "score_delta_audit",
                "legacy_quarantine_audit",
                "known_regressions",
                "deprecated_live_results",
            }
            self.assertEqual(set(paths), expected)
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            report = paths["acceptance_report"].read_text(encoding="utf-8")
            self.assertIn("verdict: READY", report)
            self.assertIn("passed: 12", report)


def _sample_inputs():
    replay_rows = []
    source_rows = []
    stage_rows = []
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        replay_rows.append(
            {
                "archetype_id": archetype_id,
                "contract_present": True,
                "coverage_status": "stage_preview_ready",
                "stage_court_ready_count": 1,
                "production_score_fixture": False,
                "production_stage_fixture": False,
            }
        )
        source_rows.append(
            {
                "archetype_id": archetype_id,
                "coverage_status": "source_backed_candidate_available",
                "source_backed_candidate_count": 3,
                "source_proxy_or_pending_count": 1,
                "unverified_research_row_count": 0,
            }
        )
        stage_rows.append(
            {
                "archetype_id": archetype_id,
                "stage_court_ready": True,
                "result_status": "stage_court_ready",
                "large_sector_id": ARCHETYPE_TO_LARGE_SECTOR[archetype_id],
            }
        )
    return {
        "chain_audit": {
            "schema_version": "chain",
            "summary": {
                "evidence_os_chain_ready": True,
                "score_contribution_ready_count": 36,
                "score_interval_ready_count": 36,
                "stage_court_ready_count": 36,
            },
        },
        "replay_acceptance": {
            "schema_version": "replay",
            "summary": {
                "production_cutover_ready": True,
                "replay_acceptance_ready": True,
                "archetype_count": 36,
                "stage_preview_ready_count": 36,
                "unsupported_source_gap_count": 0,
            },
            "rows": replay_rows,
        },
        "adversarial_acceptance": {
            "schema_version": "adversarial",
            "summary": {
                "production_cutover_ready": True,
                "adversarial_acceptance_ready": True,
                "case_count": 24,
                "missing_representative_test_count": 0,
            },
        },
        "live_smoke_acceptance": {
            "schema_version": "live",
            "summary": {
                "production_cutover_ready": True,
                "live_smoke_acceptance_ready": True,
                "accepted_operational_stage_count": 2,
                "deprecated_legacy_result_not_accepted_count": 2,
                "legacy_parser_score_claim_without_v2_current_row_count": 0,
                "legacy_parser_score_audit_missing_count": 0,
                "legacy_parser_score_claim_without_v2_quarantined_row_count": 2,
                "legacy_parser_score_claim_without_v2_quarantined_total_count": 200,
                "post_score_gap_append_only_violation_count": 0,
            },
            "rows": [
                {
                    "symbol": "005930",
                    "company_name": "삼성전자",
                    "stage": "3-Green",
                    "verified_score": 97.5,
                    "score_status": "FINAL",
                    "agentic_evidence_claim_count": 96,
                    "agentic_evidence_accepted_mapping_count": 24,
                    "legacy_parser_score_claim_without_v2_count": 0,
                },
                {
                    "symbol": "000660",
                    "company_name": "SK하이닉스",
                    "stage": "3-Green",
                    "verified_score": 97.5,
                    "score_status": "FINAL",
                    "agentic_evidence_claim_count": 73,
                    "agentic_evidence_accepted_mapping_count": 22,
                    "legacy_parser_score_claim_without_v2_count": 0,
                },
            ],
            "deprecated_rows": [
                {
                    "symbol": "005930",
                    "company": "삼성전자",
                    "visible_score": 63.2499,
                    "stage": "4C",
                    "red_team_status": "hard_break",
                    "rejection_reason": "legacy 63-point result is not accepted",
                },
                {
                    "symbol": "000660",
                    "company": "SK하이닉스",
                    "visible_score": 63.8662,
                    "stage": "3-Red",
                    "red_team_status": "moderate",
                    "rejection_reason": "legacy 63-point result is not accepted",
                },
            ],
        },
        "frozen_repeatability_acceptance": {
            "schema_version": "frozen",
            "summary": {
                "production_cutover_ready": True,
                "frozen_repeatability_acceptance_ready": True,
                "score_stage_repeatability_ready_count": 1,
            },
        },
        "source_backed_coverage": {
            "schema_version": "coverage",
            "summary": {
                "contract_count": 36,
                "source_backed_candidate_archetype_count": 36,
                "source_backed_candidate_row_count": 108,
                "source_gap_no_rows_archetype_count": 0,
                "source_gap_with_rows_archetype_count": 0,
                "source_proxy_or_pending_row_count": 0,
            },
            "rows": source_rows,
        },
        "replay_gap_plan": {
            "schema_version": "gap",
            "summary": {
                "gap_task_count": 0,
                "unsupported_source_gap_task_count": 0,
                "production_cutover_ready": True,
            },
            "tasks": [],
        },
        "score_contributions": {
            "schema_version": "contrib",
            "summary": {
                "nonzero_score_contribution_count": 155,
                "orphan_score_blocked_count": 0,
                "score_contribution_ready_count": 322,
            },
        },
        "score_snapshots": {
            "schema_version": "snapshot",
            "summary": {
                "score_interval_ready_count": 46,
                "invalid_score_snapshot_output_count": 0,
            },
        },
        "stage_court_results": {
            "schema_version": "stage",
            "summary": {"stage_court_ready_count": 46},
            "results": stage_rows,
        },
        "discovery_run_log": {
            "schema_version": "run",
            "source_call_counts": {"opendart_disclosure_date_range": 1},
        },
        "discovery_candidates": {
            "schema_version": "candidates",
            "candidates": [
                {
                    "symbol": "111111",
                    "company_name": "한전변압기",
                    "production_candidate": True,
                    "test_injected": False,
                    "candidate_source_path": "official_cheap_scan",
                }
            ],
        },
        "commit_sha": "abc123",
        "generated_at": "2026-06-28",
        "test_summary": {
            "command": "PYTHONPATH=src python -m unittest discover -s tests -v",
            "passed": 12,
            "failed": 0,
            "skipped": 0,
        },
    }


if __name__ == "__main__":
    unittest.main()
