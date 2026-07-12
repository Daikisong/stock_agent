from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.researcher_mode import (
    ATLAS_PASS,
    HistoricalScoreSchemaType,
    compile_historical_judgment_atlas,
)


class E2RV5HistoricalJudgmentAtlasTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def _compile(self, rows: list[dict]) -> object:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "research.jsonl"
            research.write_text(
                "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
                encoding="utf-8",
            )
            registry = root / "registry.json"
            registry.write_text(
                json.dumps(
                    {
                        "contract_count": 1,
                        "contracts": [
                            {"archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY"}
                        ],
                    }
                ),
                encoding="utf-8",
            )
            return compile_historical_judgment_atlas(
                [research],
                repo_root=self.ROOT,
                registry_contract_path=registry,
            )

    def test_direct_component_points_preserve_points_and_aliases(self) -> None:
        result = self._compile(
            [
                {
                    "row_type": "case",
                    "case_id": "DIRECT_CASE",
                    "symbol": "100001",
                    "company_name": "Direct Memory",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "trigger_date": "2024-01-01",
                    "declared_source_quality": "official_direct",
                    "source_url": "https://example.com/official",
                    "positive_evidence_fields": ["sold out capacity", "record profit"],
                    "raw_component_score_breakdown": {
                        "eps_fcf_explosion": 20,
                        "visibility_quality": 18,
                        "bottleneck_pricing_power": 15,
                        "market_mispricing": 10,
                        "valuation_rerating_runway": 8,
                        "capital_allocation": 3,
                        "information_confidence": 5,
                        "total": 79,
                    },
                }
            ]
        )
        self.assertEqual(result.audit["status"], ATLAS_PASS)
        judgment = result.judgments[0]
        self.assertEqual(
            judgment.score_schema_type,
            HistoricalScoreSchemaType.DIRECT_COMPONENT_POINTS.value,
        )
        self.assertEqual(judgment.normalized_component_vector["earnings_visibility"], 18)
        self.assertEqual(judgment.normalized_component_vector["bottleneck_pricing"], 15)
        self.assertEqual(judgment.reported_total_proxy, 79)
        self.assertTrue(judgment.usable_as_exact_anchor)

    def test_normalized_component_ratings_convert_to_archetype_maxima(self) -> None:
        result = self._compile(
            [
                {
                    "row_type": "case",
                    "case_id": "RATING_CASE",
                    "symbol": "100002",
                    "company_name": "Rating Memory",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "trigger_date": "2024-01-02",
                    "declared_source_quality": "issuer_official_direct",
                    "source_url": "https://example.com/ir",
                    "normalized_component_ratings": {
                        "eps_fcf_explosion": 75,
                        "visibility_quality": 80,
                        "bottleneck_pricing_power": 50,
                    },
                }
            ]
        )
        judgment = result.judgments[0]
        self.assertEqual(
            judgment.score_schema_type,
            HistoricalScoreSchemaType.NORMALIZED_COMPONENT_RATINGS.value,
        )
        self.assertEqual(judgment.normalized_component_vector["eps_fcf_explosion"], 18)
        self.assertEqual(judgment.normalized_component_vector["earnings_visibility"], 16.8)
        self.assertEqual(judgment.normalized_component_vector["bottleneck_pricing"], 9.5)

    def test_source_proxy_is_ordinal_only_and_future_outcome_stays_hidden(self) -> None:
        result = self._compile(
            [
                {
                    "row_type": "case",
                    "case_id": "PROXY_CASE",
                    "symbol": "100003",
                    "company_name": "Proxy Memory",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "trigger_date": "2024-01-03",
                    "source_proxy_only": True,
                    "raw_component_score_breakdown": {
                        "eps_fcf_explosion": 12,
                        "visibility_quality": 10,
                        "total": 22,
                    },
                    "MFE_90D_pct": 88,
                }
            ]
        )
        judgment = result.judgments[0]
        self.assertEqual(judgment.source_quality, "SOURCE_PROXY_ONLY")
        self.assertFalse(judgment.usable_as_exact_anchor)
        self.assertTrue(judgment.usable_as_ordinal_anchor)
        runtime_text = json.dumps(judgment.to_runtime_anchor(), sort_keys=True)
        self.assertNotIn("future_outcome_ref", runtime_text)
        self.assertNotIn("MFE", runtime_text)

    def test_every_structured_row_is_semantically_accounted(self) -> None:
        result = self._compile(
            [
                {
                    "row_type": "case",
                    "case_id": "ACCOUNT_CASE",
                    "symbol": "100004",
                    "company_name": "Account Memory",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "trigger_date": "2024-01-04",
                },
                {
                    "row_type": "shadow_weight",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "weight": 1.2,
                },
                {
                    "row_type": "research_metadata",
                    "note": "preserve this row",
                },
            ]
        )
        accounting = result.audit["structured_row_accounting"]
        self.assertEqual(accounting["structured_row_preservation_rate"], 1.0)
        self.assertEqual(
            accounting["structured_row_count"],
            accounting["accounted_structured_row_count"],
        )
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_operational_full_corpus_atlas_is_committed_pass(self) -> None:
        path = self.ROOT / "docs/operational/e2r_v5_historical_judgment_atlas_audit.json"
        self.assertTrue(path.is_file())
        audit = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit["status"], ATLAS_PASS)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(audit["registry_archetype_coverage_rate"], 1.0)
        self.assertEqual(
            audit["structured_row_accounting"]["structured_row_preservation_rate"],
            1.0,
        )
        self.assertEqual(
            audit["critical_counts"]["source_proxy_exact_anchor_promotion_count"],
            0,
        )
        self.assertEqual(
            audit["critical_counts"]["future_outcome_current_prompt_exposure_count"],
            0,
        )


if __name__ == "__main__":
    unittest.main()
