from __future__ import annotations

import hashlib
import json
import unittest

from e2r.research_brain.researcher_mode.prompt_projection import (
    project_source_documents,
    project_source_graph_checkpoint,
    project_structured_records,
)
from e2r.research_brain.researcher_mode import StructuredMetricRecord


class E2RV5PromptProjectionTests(unittest.TestCase):
    def test_all_structured_rows_are_hash_accounted_without_fixed_top_n(self):
        rows = tuple(
            StructuredMetricRecord(
                record_id=f"ROW-{index:04d}",
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
                metric_id="daily_close",
                value=float(index),
                unit="KRW",
                period=f"DAY-{index:04d}",
                evidence_roles=("CURRENT_PRICE",),
                source_ids=("SRC-PRICE",),
                source_route="KRX_PRICE_MARKET_CAP",
                observed_at="2026-07-10",
                available_at="2026-07-10",
                record_kind="PRICE_HISTORY",
                confidence=1.0,
                dataset="VALUATION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={"structured_source": True},
            )
            for index in range(1_000)
        )
        first = project_structured_records(rows)
        second = project_structured_records(tuple(reversed(rows)))
        self.assertEqual(first, second)
        self.assertEqual(first["record_count"], 1_000)
        self.assertEqual(first["semantic_series_count"], 1)
        self.assertTrue(first["every_record_accounted_by_hash_and_series_count"])
        self.assertFalse(first["fixed_top_n_used"])
        self.assertFalse(first["prompt_projection_is_research_cap"])
        self.assertNotIn("records", first)
        self.assertLess(len(json.dumps(first, sort_keys=True)), 10_000)

    def test_document_projection_keeps_every_lineage_but_not_duplicate_body(self):
        text = "issuer full report body " * 10_000
        content_hash = hashlib.sha256(text.encode()).hexdigest()
        documents = (
            {
                "document_id": "DOC-1",
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
                "canonical_url": "https://issuer.example/report",
                "title": "Issuer report",
                "source_family": "ISSUER_PRESENTATION",
                "published_at": "2026-07-08",
                "available_at": "2026-07-08",
                "content_hash": content_hash,
                "content_text": text,
                "full_fetch_performed": True,
                "snippet_only": False,
                "evidence_eligible": True,
            },
        )
        projected = project_source_documents(documents)
        self.assertEqual(len(projected), 1)
        self.assertEqual(projected[0]["document_id"], "DOC-1")
        self.assertEqual(projected[0]["content_hash_recomputed"], content_hash)
        self.assertEqual(projected[0]["content_chars"], len(text))
        self.assertNotIn("content_text", projected[0])
        self.assertFalse(projected[0]["prompt_projection_is_research_cap"])

        checkpoint = project_source_graph_checkpoint(
            {"checkpoint_id": "CHECKPOINT", "evidence_documents": list(documents)},
            keys=("checkpoint_id", "evidence_documents"),
        )
        self.assertEqual(checkpoint["evidence_document_count"], 1)
        self.assertTrue(checkpoint["full_document_bodies_omitted_after_fact_extraction"])
        self.assertNotIn("content_text", checkpoint["evidence_documents"][0])


if __name__ == "__main__":
    unittest.main()
