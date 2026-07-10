from __future__ import annotations

import json
import unittest
from copy import deepcopy
from dataclasses import replace
from tempfile import TemporaryDirectory

from e2r.research_brain.runtime.known_bad_suite import (
    REQUIRED_KNOWN_BAD_PROBE_IDS,
    KnownBadCategory,
    KnownBadProbeId,
    audit_known_bad_suite,
    write_known_bad_suite,
)
from tests.known_bad_suite_fixture import (
    KNOWN_BAD_PROBE_SPECS,
    build_known_bad_suite_fixture,
)


class UnifiedKnownBadSuiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = build_known_bad_suite_fixture()
        cls.by_probe = {
            item.probe_id: item for item in cls.result.observations
        }

    def test_registry_is_exact_complete_and_splits_c05_boundaries(self) -> None:
        observed = tuple(item.probe_id for item in self.result.observations)
        self.assertEqual(observed, REQUIRED_KNOWN_BAD_PROBE_IDS)
        self.assertEqual(
            tuple(item.probe_id for item in KNOWN_BAD_PROBE_SPECS),
            REQUIRED_KNOWN_BAD_PROBE_IDS,
        )
        self.assertEqual(len(observed), 26)
        self.assertEqual(len(set(observed)), 26)
        self.assertIn(KnownBadProbeId.C05_CONTEXT_COPY_CORPUS.value, observed)
        self.assertIn(KnownBadProbeId.C05_CONTEXT_COPY_CURRENT.value, observed)
        self.assertEqual(self.result.manifest["required_probe_count"], 26)
        self.assertEqual(self.result.manifest["detected_probe_count"], 26)
        self.assertEqual(self.result.manifest["undetected_probe_count"], 0)

    def test_corpus_source_and_planner_mutations_are_detected(self) -> None:
        expected = {
            KnownBadProbeId.FILE_LEVEL_CASE_COLLAPSE.value,
            KnownBadProbeId.FIRST_SYMBOL_EXTRACTION.value,
            KnownBadProbeId.COMPANY_DATE_LOSS.value,
            KnownBadProbeId.ONE_URL_WHOLE_FILE_A2.value,
            KnownBadProbeId.HANDOFF_PROMPT_AS_CASE.value,
            KnownBadProbeId.SOURCE_PROXY_PROMOTED.value,
            KnownBadProbeId.C05_CONTEXT_COPY_CORPUS.value,
            KnownBadProbeId.C05_CONTEXT_COPY_CURRENT.value,
            KnownBadProbeId.SNIPPET_SCORE.value,
            KnownBadProbeId.REPLAY_AS_REAL_FETCH.value,
        }
        self.assertTrue(all(self.by_probe[item].detected for item in expected))
        self.assertTrue(
            all(self.by_probe[item].detector_ids for item in expected)
        )
        self.assertTrue(all(self.by_probe[item].signal_ids for item in expected))
        c05 = self.by_probe[KnownBadProbeId.C05_CONTEXT_COPY_CURRENT.value]
        self.assertTrue(
            any("c05_monoculture" in item for item in c05.detector_ids)
        )

    def test_semantic_and_claim_mutations_are_detected(self) -> None:
        expected = {
            KnownBadProbeId.PRODUCT_PROFILE_AS_ORDER.value,
            KnownBadProbeId.HBM_KEYWORD_POSITIVE.value,
            KnownBadProbeId.SECURITY_KEYWORD_ARR.value,
            KnownBadProbeId.COMMODITY_HEADLINE_MARGIN.value,
            KnownBadProbeId.WRONG_SUBJECT.value,
            KnownBadProbeId.CUSTOMER_CAPA_AS_TARGET_CAPA.value,
            KnownBadProbeId.INDUSTRY_DEMAND_AS_ISSUER_ORDER.value,
            KnownBadProbeId.FINANCIAL_CONTRACT_AS_COMMERCIAL.value,
            KnownBadProbeId.STALE_RISK_PENALTY.value,
            KnownBadProbeId.REROUTED_GAP_CLOSURE.value,
        }
        self.assertTrue(all(self.by_probe[item].detected for item in expected))
        self.assertEqual(
            self.result.manifest["category_counts"][
                KnownBadCategory.SEMANTIC.value
            ],
            4,
        )
        self.assertEqual(
            self.result.manifest["category_counts"][KnownBadCategory.CLAIM.value],
            6,
        )

    def test_score_mode_and_current_mutations_are_detected(self) -> None:
        expected = {
            KnownBadProbeId.PROVIDER_FAILURE_RED.value,
            KnownBadProbeId.EVENT_SCORE_FULL_SCORE.value,
            KnownBadProbeId.STAGE_TRACE_MISMATCH.value,
            KnownBadProbeId.HISTORICAL_OUTCOME_LEAKAGE.value,
            KnownBadProbeId.HISTORICAL_REPLAY_CURRENT_WATCHLIST.value,
            KnownBadProbeId.FORCED_CURRENT_ARCHETYPE_MATERIALIZATION.value,
        }
        self.assertTrue(all(self.by_probe[item].detected for item in expected))
        self.assertFalse(self.result.production_runtime_ready)
        self.assertFalse(self.result.manifest["production_runtime_ready"])
        self.assertTrue(self.result.manifest["test_only"])

    def test_independent_audit_catches_missing_duplicate_tamper_and_overclaim(self) -> None:
        missing = deepcopy(self.result.to_dict())
        missing["observations"].pop()
        missing_audit = audit_known_bad_suite(missing)
        self.assertEqual(
            missing_audit["critical_counts"]["missing_required_probe"],
            1,
        )

        duplicate = deepcopy(self.result.to_dict())
        duplicate["observations"].append(
            deepcopy(duplicate["observations"][0])
        )
        duplicate_audit = audit_known_bad_suite(duplicate)
        self.assertEqual(
            duplicate_audit["critical_counts"]["duplicate_required_probe"],
            1,
        )

        undetected = deepcopy(self.result.to_dict())
        undetected["observations"][0]["detected"] = False
        undetected_audit = audit_known_bad_suite(undetected)
        self.assertEqual(
            undetected_audit["critical_counts"]["undetected_required_probe"],
            1,
        )

        tampered = deepcopy(self.result.to_dict())
        tampered["observations"][0]["mutation_description"] += " tampered"
        tampered_audit = audit_known_bad_suite(tampered)
        self.assertEqual(tampered_audit["critical_counts"]["run_id_mismatch"], 1)
        self.assertEqual(
            tampered_audit["critical_counts"]["manifest_leaf_hash_mismatch"],
            1,
        )

        overclaim = deepcopy(self.result.to_dict())
        overclaim["production_runtime_ready"] = True
        overclaim_audit = audit_known_bad_suite(overclaim)
        self.assertEqual(
            overclaim_audit["critical_counts"][
                "production_runtime_ready_overclaim"
            ],
            1,
        )

        manifest_tamper = deepcopy(self.result.to_dict())
        manifest_tamper["manifest"]["category_counts"] = {}
        manifest_tamper["manifest"]["unique_detector_count"] = 999
        manifest_tamper["manifest"]["test_only"] = False
        manifest_tamper_audit = audit_known_bad_suite(manifest_tamper)
        self.assertEqual(
            manifest_tamper_audit["critical_counts"][
                "manifest_category_count_mismatch"
            ],
            1,
        )
        self.assertEqual(
            manifest_tamper_audit["critical_counts"][
                "manifest_detector_count_mismatch"
            ],
            1,
        )
        self.assertEqual(
            manifest_tamper_audit["critical_counts"][
                "manifest_fixture_boundary_mismatch"
            ],
            1,
        )

        malformed = deepcopy(self.result.to_dict())
        malformed["observations"][0]["detector_ids"] = "not-a-sequence"
        malformed_audit = audit_known_bad_suite(malformed)
        self.assertEqual(
            malformed_audit["critical_counts"]["invalid_observation_contract"],
            1,
        )

        missing_manifest = deepcopy(self.result.to_dict())
        missing_manifest["manifest"] = {}
        missing_manifest_audit = audit_known_bad_suite(missing_manifest)
        self.assertEqual(
            missing_manifest_audit["critical_counts"][
                "manifest_missing_or_invalid"
            ],
            1,
        )
        self.assertTrue(
            all(
                audit["status"] == "UNIFIED_KNOWN_BAD_SUITE_FAIL"
                for audit in (
                    missing_audit,
                    duplicate_audit,
                    undetected_audit,
                    tampered_audit,
                    overclaim_audit,
                    manifest_tamper_audit,
                    malformed_audit,
                    missing_manifest_audit,
                )
            )
        )

    def test_writer_report_and_result_integrity_are_reproducible(self) -> None:
        with TemporaryDirectory() as tmp:
            paths = write_known_bad_suite(self.result, output_root=tmp)
            self.assertTrue(all(path.is_file() for path in paths.values()))
            manifest = json.loads(
                paths["manifest"].read_text(encoding="utf-8")
            )
            audit = json.loads(paths["audit"].read_text(encoding="utf-8"))
            rows = tuple(
                json.loads(line)
                for line in paths["observations"].read_text(
                    encoding="utf-8"
                ).splitlines()
                if line.strip()
            )
            report = paths["report"].read_text(encoding="utf-8")

        self.assertEqual(manifest, self.result.manifest)
        self.assertEqual(audit, self.result.audit)
        self.assertEqual(len(rows), 26)
        self.assertIn("UNIFIED_KNOWN_BAD_SUITE_PASS", report)
        self.assertIn("fixture-only acceptance: true", report)
        self.assertIn("production_runtime_ready: false", report)
        self.assertEqual(self.result.audit["critical_count_sum"], 0)
        self.assertTrue(
            all(value == 0 for value in self.result.audit["critical_counts"].values())
        )
        with self.assertRaisesRegex(ValueError, "integrity mismatch"):
            replace(
                self.result,
                manifest={**self.result.manifest, "leaf_hash": "0" * 64},
            )


if __name__ == "__main__":
    unittest.main()
