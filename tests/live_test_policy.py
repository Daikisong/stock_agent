"""Explicit opt-in policy for tests that call real external providers."""

from __future__ import annotations

import os
import unittest


LIVE_TESTS_ENABLED = os.environ.get("E2R_RUN_LIVE_TESTS", "").strip().lower() in {
    "1",
    "true",
    "yes",
}

requires_live_test = unittest.skipUnless(
    LIVE_TESTS_ENABLED,
    "real-provider integration test requires E2R_RUN_LIVE_TESTS=1",
)

