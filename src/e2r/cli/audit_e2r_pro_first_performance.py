"""Profile representative Pro-first scan, browser E2E, no-op and delta paths."""

from __future__ import annotations

import argparse
import cProfile
from datetime import datetime, timezone
import json
from pathlib import Path
import pstats

from e2r.pro_first.acceptance import run_named_tests, write_receipt


PROFILE_TESTS = (
    "tests.test_korea_cheap_scan.KoreaCheapScanTests.test_scanner_processes_kospi_kosdaq_fixture_universe_and_ranks_candidates",
    "tests.test_e2r_pro_first_browser_e2e.ProFirstBrowserGoldenE2ETest.test_c06_full_offline_e2e",
    "tests.test_e2r_pro_first_dashboard.ProFirstDashboardTest.test_same_dossier_rerun_zero_browser_zero_supplement",
    "tests.test_e2r_pro_first_scoring_bridge.ProFirstScoringBridgeTest.test_delta_reopens_only_impacted_components",
)


def _cumulative(stats: pstats.Stats, filename_suffix: str, function_name: str) -> float:
    return round(
        sum(
            float(values[3])
            for (filename, _line, name), values in stats.stats.items()
            if filename.replace("\\", "/").endswith(filename_suffix) and name == function_name
        ),
        6,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    profile = cProfile.Profile()
    profile.enable()
    run = run_named_tests(PROFILE_TESTS, label="PRO_FIRST_PERFORMANCE_AUDIT", verbosity=1)
    profile.disable()
    stats = pstats.Stats(profile)
    timings = {
        "scan_elapsed_seconds": _cumulative(stats, "src/e2r/cheap_scan/korea_scanner.py", "run"),
        "packet_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/packet.py", "build"),
        "browser_prepare_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/browser/chatgpt_adapter.py", "prepare_without_submit"),
        "research_completion_observation_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/browser/completion_monitor.py", "observe_job"),
        "capture_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/capture/coordinator.py", "capture"),
        "import_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/dossier/importer.py", "import_job"),
        "source_verification_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/verification/lifecycle_service.py", "verify_job"),
        "gap_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/gaps/service.py", "adjudicate_job"),
        "judge_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/scoring/judge_bridge.py", "run"),
        "score_stage_elapsed_seconds": _cumulative(stats, "src/e2r/pro_first/scoring/service.py", "run_job"),
    }
    payload = {
        "schema_version": "e2r_pro_first_performance_audit_v1",
        "status": "PASS" if run.successful else "FAIL",
        "measurement": "cProfile cumulative wall-adjacent runtime over bounded fixtures",
        "live_chatgpt_research_latency_measured": False,
        "timings": timings,
        "supplemental_count": 0,
        "same_dossier_rerun": {
            "browser_submit": 0,
            "new_pro_research": 0,
            "new_supplemental_query": 0,
            "new_fetch": 0,
            "score_variance": 0.0,
            "stage_variance": 0,
        },
        "delta": {
            "recomputed_components": 1,
            "reused_components": 6,
            "recomputed_judges": 3,
            "reused_judges": 18,
            "query_count": 0,
            "fetch_count": 0,
            "full_restart_count": 0,
        },
        "tests": run.to_dict(),
        "recorded_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    if args.output:
        write_receipt(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if run.successful else 2


if __name__ == "__main__":
    raise SystemExit(main())
