from __future__ import annotations

import unittest

from e2r.research_brain.research_quality import (
    select_research_grade_documents,
)


class ResearchGradeDocumentSelectionTests(unittest.TestCase):
    def test_full_source_scope_and_pdf_anchor_control_selection(self) -> None:
        base = {
            "published_at": "2026-06-01",
            "question_family_ids": ["margin_fcf_conversion"],
            "mechanism_scopes": ["HBM/memory margin, FCF, and cash conversion"],
            "source_tier": "REGULATORY_OFFICIAL",
        }
        candidates = [
            {
                **base,
                "document_id": "GOOD-PDF",
                "document_format": "PDF",
                "content_text": "FCF table full text",
                "evidence_anchor": {"page_number": 17, "table_anchor": "T4"},
                "table_extraction": {
                    "value": "120",
                    "unit": "KRW bn",
                    "period": "2026Q1",
                },
            },
            {
                **base,
                "document_id": "BAD-PDF",
                "document_format": "PDF",
                "content_text": "unanchored table",
            },
            {
                **base,
                "document_id": "SNIPPET",
                "content_text": "search result summary",
                "snippet_only": True,
            },
            {
                **base,
                "document_id": "WRONG-SCOPE",
                "content_text": "Foundry margin",
                "mechanism_scopes": ["Foundry economics"],
            },
            {
                **base,
                "document_id": "LOWER-TIER",
                "source_tier": "GENERAL_WEB",
                "content_text": "full original article",
            },
        ]
        selected, rejected = select_research_grade_documents(
            candidates=candidates,
            question_family_id="margin_fcf_conversion",
            as_of_date="2026-07-11",
            mechanism_scope="HBM/memory margin, FCF, and cash conversion",
        )
        self.assertEqual(
            [row["document_id"] for row in selected],
            ["GOOD-PDF", "LOWER-TIER"],
        )
        reasons = {row["document_id"]: row["reason"] for row in rejected}
        self.assertEqual(reasons["BAD-PDF"], "PDF_ANCHOR_INCOMPLETE")
        self.assertEqual(reasons["SNIPPET"], "SNIPPET_ONLY_DISCOVERY")
        self.assertEqual(reasons["WRONG-SCOPE"], "WRONG_MECHANISM_SCOPE")


if __name__ == "__main__":
    unittest.main()
