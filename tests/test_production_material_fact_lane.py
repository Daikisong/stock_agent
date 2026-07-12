from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.research_quality import (
    ProductionMaterialFactLane,
    combine_production_material_fact_lanes,
    compile_production_material_fact_lane,
    write_production_material_fact_lane,
)


class ProductionMaterialFactLaneTests(unittest.TestCase):
    def test_combined_lane_requires_unique_lineage_and_one_as_of_date(self) -> None:
        def lane(target_id: str, fact_id: str, input_id: str):
            return ProductionMaterialFactLane(
                facts=({"fact_id": fact_id},),
                inputs=({"input_id": input_id},),
                manifest={
                    "target_id": target_id,
                    "as_of_date": "2026-07-11",
                },
            )

        combined = combine_production_material_fact_lanes(
            (lane("005930", "P-S", "I-S"), lane("000660", "P-H", "I-H"))
        )
        self.assertEqual(combined.manifest["target_ids"], ["000660", "005930"])
        self.assertEqual(combined.manifest["combined_lane_count"], 2)
        self.assertFalse(combined.manifest["gold_visibility"])
        with self.assertRaisesRegex(ValueError, "fact_id"):
            combine_production_material_fact_lanes(
                (lane("005930", "P-X", "I-S"), lane("000660", "P-X", "I-H"))
            )

    def test_lane_is_compiled_from_scoring_leaves_without_gold_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._jsonl(
                root / "accepted_current_claims.jsonl",
                [
                    {
                        "claim_id": "CLM-1",
                        "temporal_status": "CURRENT",
                        "raw_assertion": {
                            "predicate": "공급 제약이 지속됐다",
                            "object_text": "제한된 공급",
                        },
                    }
                ],
            )
            self._jsonl(
                root / "claim_provenance.jsonl",
                [
                    {
                        "claim_id": "CLM-1",
                        "source_url": "https://dart.fss.or.kr/doc",
                        "exact_quote": "견조한 수요 대비 제한된 공급 환경이 지속됐다.",
                    }
                ],
            )
            self._jsonl(
                root / "claim_impacts_validated.jsonl",
                [
                    {
                        "claim_id": "CLM-1",
                        "mapping_id": "MAP-1",
                        "impact_id": "IMPACT-1",
                        "question_family_id": "capacity_constraint_presold_status",
                        "primitive_id": "hbm_capacity_constraint",
                        "direction": "SUPPORT",
                        "fact_cluster_id": "FACT-1",
                        "source_family": "OFFICIAL_FILING",
                        "scope_validation": {
                            "scope": {
                                "issuer_id": "000660",
                                "business_segment": "MEMORY",
                                "product_family": "HBM",
                                "economic_mechanism": "SUPPLY_CONSTRAINT",
                                "effective_period": "2026Q1",
                            }
                        },
                    },
                    {
                        "claim_id": "CLM-1",
                        "mapping_id": "MAP-1",
                        "impact_id": "IMPACT-2",
                        "question_family_id": "capacity_constraint_presold_status",
                        "primitive_id": "hbm_capacity_constraint",
                        "direction": "COUNTER",
                        "fact_cluster_id": "FACT-2",
                        "source_family": "OFFICIAL_FILING",
                        "scope_validation": {
                            "scope": {
                                "issuer_id": "000660",
                                "business_segment": "MEMORY",
                                "product_family": "HBM",
                                "economic_mechanism": "SUPPLY_CONSTRAINT",
                                "effective_period": "2026Q1",
                            }
                        },
                    },
                ],
            )
            self._jsonl(
                root / "economic_fact_clusters.jsonl",
                [
                    {
                        "fact_cluster_id": "FACT-1",
                        "normalized_subject": "000660 memory hbm",
                        "normalized_predicate": "공급 제약 지속",
                        "normalized_object_value": "제한된 공급",
                        "period": "2026Q1",
                    },
                    {
                        "fact_cluster_id": "FACT-2",
                        "normalized_subject": "000660 memory hbm",
                        "normalized_predicate": "공급 제약 지속",
                        "normalized_object_value": "제한된 공급",
                        "period": "2026Q1",
                    },
                ],
            )
            self._jsonl(
                root / "question_source_tasks.jsonl",
                [
                    {
                        "task_id": "TASK-1",
                        "query_intent": {
                            "literal_queries": ["발행사 HBM 현재 공급 제약 공식 공시"]
                        },
                    }
                ],
            )

            lane = compile_production_material_fact_lane(
                dossier_root=root,
                target_id="000660",
                as_of_date="2026-07-11",
            )
            paths = write_production_material_fact_lane(
                lane,
                output_root=root,
            )

            self.assertEqual(len(lane.facts), 2)
            self.assertEqual(len({row["fact_id"] for row in lane.facts}), 2)
            self.assertEqual(
                {row["fact_role"] for row in lane.facts},
                {"SUPPORT", "COUNTER"},
            )
            self.assertEqual(lane.facts[0]["source_tier"], "REGULATORY_OFFICIAL")
            self.assertEqual(
                lane.facts[0]["mechanism_scope_id"],
                "MEMORY|HBM|SUPPLY_CONSTRAINT",
            )
            self.assertFalse(lane.manifest["gold_visibility"])
            self.assertEqual(lane.manifest["lane_role"], "PRODUCTION")
            self.assertNotIn("GOLD", json.dumps(lane.inputs, ensure_ascii=False))
            self.assertTrue(all(path.is_file() for path in paths.values()))

    @staticmethod
    def _jsonl(path: Path, rows) -> None:
        path.write_text(
            "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
            encoding="utf-8",
        )


if __name__ == "__main__":
    unittest.main()
