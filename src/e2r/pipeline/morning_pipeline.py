"""Convenience entry point for generating the local morning brief."""

from __future__ import annotations

from e2r.pipeline.daily_scan import DailyScanConfig, DailyScanResult, DailyScanRunner


def run_morning_pipeline(config: DailyScanConfig) -> DailyScanResult:
    """Run the daily scan and write morning briefing outputs."""

    return DailyScanRunner().run(config)
