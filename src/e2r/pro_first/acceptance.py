"""Deterministic local acceptance runners and machine-readable receipts."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import time
import unittest
from typing import Any, Iterable, Mapping


CORE_TEST_MODULES = (
    "tests.test_e2r_pro_first_state_machine",
    "tests.test_e2r_pro_first_scheduler",
    "tests.test_e2r_pro_first_candidate_selector",
    "tests.test_e2r_pro_first_packet",
    "tests.test_e2r_pro_first_browser_adapter",
    "tests.test_e2r_pro_first_approval_submit",
    "tests.test_e2r_pro_first_completion_capture",
    "tests.test_e2r_pro_first_dossier_import",
    "tests.test_e2r_pro_first_source_verification",
    "tests.test_e2r_pro_first_gap_adjudication",
    "tests.test_e2r_pro_first_scoring_bridge",
    "tests.test_e2r_pro_first_dashboard",
    "tests.test_e2r_pro_first_submit_static_guard",
    "tests.test_e2r_pro_first_operational_acceptance",
)

BROWSER_MOCK_TEST_MODULES = (
    "tests.test_e2r_pro_first_browser_adapter",
    "tests.test_e2r_pro_first_approval_submit",
    "tests.test_e2r_pro_first_completion_capture",
    "tests.test_e2r_pro_first_browser_e2e",
)

OFFLINE_E2E_TEST_NAMES = (
    "tests.test_e2r_pro_first_browser_e2e.ProFirstBrowserGoldenE2ETest.test_c06_full_offline_e2e",
    "tests.test_e2r_pro_first_browser_e2e.ProFirstBrowserGoldenE2ETest.test_c17_full_offline_e2e",
    "tests.test_e2r_pro_first_browser_e2e.ProFirstBrowserGoldenE2ETest.test_c24_or_c28_full_offline_e2e",
    "tests.test_e2r_pro_first_browser_e2e.ProFirstBrowserGoldenE2ETest.test_backend_restart_after_capture",
)


@dataclass(frozen=True)
class AcceptanceRun:
    label: str
    tests_run: int
    failure_count: int
    error_count: int
    skip_count: int
    elapsed_seconds: float
    successful: bool
    output_tail: str

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_first_test_receipt_v1",
            "label": self.label,
            "status": "PASS" if self.successful else "FAIL",
            "tests_run": self.tests_run,
            "failure_count": self.failure_count,
            "error_count": self.error_count,
            "skip_count": self.skip_count,
            "elapsed_seconds": round(self.elapsed_seconds, 6),
            "output_tail": self.output_tail,
            "recorded_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        }


def run_named_tests(names: Iterable[str], *, label: str, verbosity: int = 2) -> AcceptanceRun:
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromNames(tuple(names))
    started = time.monotonic()
    result = unittest.TextTestRunner(stream=stream, verbosity=verbosity).run(suite)
    elapsed = time.monotonic() - started
    output = stream.getvalue()
    return AcceptanceRun(
        label=label,
        tests_run=result.testsRun,
        failure_count=len(result.failures),
        error_count=len(result.errors),
        skip_count=len(result.skipped),
        elapsed_seconds=elapsed,
        successful=result.wasSuccessful() and not result.skipped,
        output_tail=output[-8_000:],
    )


def write_receipt(path: str | Path, payload: Mapping[str, Any]) -> Path:
    destination = Path(path).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    temporary = destination.with_name(f".{destination.name}.tmp")
    temporary.write_text(encoded, encoding="utf-8")
    temporary.replace(destination)
    return destination


__all__ = [
    "AcceptanceRun",
    "BROWSER_MOCK_TEST_MODULES",
    "CORE_TEST_MODULES",
    "OFFLINE_E2E_TEST_NAMES",
    "run_named_tests",
    "write_receipt",
]
