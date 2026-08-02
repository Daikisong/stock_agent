from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest

from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeConfig,
    production_structured_material_fact_rows,
    write_production_lane,
)
from e2r.research_brain.researcher_mode.structured_data_researcher import (
    StructuredMetricRecord,
)


class ProductionStructuredFactLaneTests(unittest.TestCase):
    AS_OF_DATE = "2026-07-12"
    TARGET_ID = "999999"

    def _record(
        self,
        *,
        record_id: str,
        dataset: str,
        metric_id: str,
        value: float,
        source_route: str,
        source_id: str,
    ) -> StructuredMetricRecord:
        return StructuredMetricRecord(
            record_id=record_id,
            target_id=self.TARGET_ID,
            as_of_date=self.AS_OF_DATE,
            metric_id=metric_id,
            value=value,
            unit="MULTIPLE" if "pe" in metric_id else "PRICE",
            period="2026-07-10",
            evidence_roles=("CURRENT_VALUATION",),
            source_ids=(source_id,),
            source_route=source_route,
            observed_at="2026-07-10",
            available_at="2026-07-10",
            record_kind="STRUCTURED_VALUATION_SNAPSHOT",
            confidence=0.99,
            dataset=dataset,
            provenance="STRUCTURED_EXTRACTED",
            metadata={"structured_source": True},
        )

    def _engine(self):
        records = (
            self._record(
                record_id="STRUCTURED-CURRENT-PRICE",
                dataset="VALUATION",
                metric_id="current_price",
                value=123_000.0,
                source_route="KRX_PRICE_MARKET_CAP",
                source_id="STRUCTSRC-KRX",
            ),
            self._record(
                record_id="STRUCTURED-TRAILING-PE",
                dataset="VALUATION",
                metric_id="trailing_pe",
                value=17.25,
                source_route="COMPANYGUIDE",
                source_id="STRUCTSRC-COMPANYGUIDE",
            ),
        )
        return SimpleNamespace(
            target_id=self.TARGET_ID,
            as_of_date=self.AS_OF_DATE,
            records=records,
        )

    def test_source_backed_structured_rows_are_non_scoring_production_facts(self) -> None:
        rows = production_structured_material_fact_rows(self._engine())

        self.assertEqual(len(rows), 2)
        self.assertEqual(len({row["fact_id"] for row in rows}), 2)
        self.assertEqual(
            {row["predicate_family"] for row in rows},
            {"current_price", "trailing_pe"},
        )
        self.assertEqual(
            {row["source_tier"] for row in rows},
            {"FINANCIAL_REVISION"},
        )
        self.assertTrue(all(row["temporal_status"] == "CURRENT" for row in rows))
        self.assertTrue(all(row["score_authority"] is False for row in rows))
        self.assertTrue(all(row["gold_visibility"] is False for row in rows))
        self.assertTrue(all(row["claim_ids"] == [] for row in rows))

    def test_write_production_lane_includes_document_and_structured_facts(self) -> None:
        document_fact = {
            "fact_id": "EFACT-DOCUMENT",
            "target_id": self.TARGET_ID,
            "question_family_id": "cash_conversion",
            "subject_id": self.TARGET_ID,
            "predicate_family": "operating_cash_flow",
            "normalized_object": "source-backed cash flow",
            "period": "FY2026E",
            "mechanism_scope_id": "CORPORATE|CASH|CONVERSION",
            "source_id": "DOC-1",
            "source_ids": ["DOC-1"],
            "source_tier": "TRUSTED_INDEPENDENT",
            "temporal_status": "CURRENT",
            "as_of_date": self.AS_OF_DATE,
            "materiality": "CRITICAL",
            "fact_role": "SUPPORT",
            "economic_mechanism": "CASH_CONVERSION",
            "predicate": "operating_cash_flow",
            "value": 1,
            "confidence": 0.9,
            "claim_ids": ["CLAIM-1"],
            "quote_ids": ["QUOTE-1"],
            "discovery_origin": "CANONICAL_SOURCE_TASK",
            "gold_visibility": False,
        }
        fact_extraction = SimpleNamespace(
            material_claims=(
                {
                    "claim_id": "CLAIM-1",
                    "question_family_id": "cash_conversion",
                    "subject_id": self.TARGET_ID,
                    "predicate_family": "operating_cash_flow",
                    "normalized_object": "source-backed cash flow",
                    "mechanism_scope_id": "CORPORATE|CASH|CONVERSION",
                    "source_tier": "TRUSTED_INDEPENDENT",
                    "materiality": "CRITICAL",
                },
            ),
            facts=(
                SimpleNamespace(
                    fact_id=document_fact["fact_id"],
                    target_id=self.TARGET_ID,
                    period=document_fact["period"],
                    source_ids=("DOC-1",),
                    as_of_date=self.AS_OF_DATE,
                    current_lifecycle="ACTIVE",
                    direction="POSITIVE",
                    economic_mechanism="CASH_CONVERSION",
                    predicate="operating_cash_flow",
                    value=1,
                    confidence=0.9,
                    claim_ids=("CLAIM-1",),
                    quote_ids=("QUOTE-1",),
                ),
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = write_production_lane(
                config=CurrentResearcherModeConfig(
                    as_of_date=self.AS_OF_DATE,
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    output_root=root,
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                    gold_lane_isolated=True,
                    require_researcher_parity=True,
                ),
                target_runs=(
                    SimpleNamespace(
                        status=(
                            "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                        ),
                        target=SimpleNamespace(target_id=self.TARGET_ID),
                        fact_extraction=fact_extraction,
                        structured_result=self._engine(),
                        component_memo_rows=(),
                        production_input_rows=(),
                    ),
                ),
            )
            rows = [
                json.loads(line)
                for line in paths["facts"].read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
        self.assertEqual(len(rows), 3)
        self.assertEqual(
            {row["predicate_family"] for row in rows},
            {"operating_cash_flow", "current_price", "trailing_pe"},
        )


if __name__ == "__main__":
    unittest.main()
