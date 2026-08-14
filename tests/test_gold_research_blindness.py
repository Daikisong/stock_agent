from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from e2r.production.metadata import stable_hash
from e2r.research_brain.research_quality import (
    BlindResearchQualityBenchmark,
    build_post_run_reviewer_identity,
)


def _portable_reviewer_identity(role_id: str):
    return build_post_run_reviewer_identity(
        role_id=role_id,
        provider_call_id="COLLABCALL-" + role_id,
        prompt_hash=stable_hash(("prompt", role_id)),
        response_hash=stable_hash(("response", role_id)),
    )


class GoldResearchBlindnessTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    FIXTURE = (
        ROOT / "tests/fixtures/semantic_scoring_v2/blind_benchmark"
    )

    def test_isolated_lanes_pass_without_gold_input_leakage(self) -> None:
        result = BlindResearchQualityBenchmark().compare(
            gold_root=self.FIXTURE / "gold",
            production_root=self.FIXTURE / "production",
        )
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_PASS")
        self.assertEqual(result.audit["critical_count_sum"], 0)
        self.assertEqual(result.audit["noncritical_fact_recall"], 1.0)
        self.assertEqual(
            result.audit["critical_counts"][
                "gold_source_injected_into_production_count"
            ],
            0,
        )
        self.assertTrue(
            all(row.semantic_match for row in result.comparisons)
        )

    def test_same_source_may_be_rediscovered_but_cannot_be_a_seed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "benchmark"
            shutil.copytree(self.FIXTURE, fixture)
            source = json.loads(
                (fixture / "gold/gold_source_map.jsonl")
                .read_text()
                .splitlines()[0]
            )
            with (fixture / "production/production_input_manifest.jsonl").open(
                "a", encoding="utf-8"
            ) as handle:
                handle.write(
                    json.dumps(
                        {
                            "input_id": "LEAKED-SEED",
                            "input_type": "SEED_URL",
                            "value": source["source_url"],
                            "origin": "CANONICAL_CONFIG",
                        }
                    )
                    + "\n"
                )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=fixture / "gold",
                production_root=fixture / "production",
            )
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_FAIL")
        self.assertEqual(
            result.audit["critical_counts"][
                "gold_source_injected_into_production_count"
            ],
            1,
        )

    def test_critical_gold_miss_cannot_pass_on_raw_source_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "benchmark"
            shutil.copytree(self.FIXTURE, fixture)
            path = fixture / "production/production_material_facts.jsonl"
            rows = [
                json.loads(line) for line in path.read_text().splitlines()
            ]
            rows = [row for row in rows if row["fact_id"] != "P-203"]
            path.write_text(
                "".join(json.dumps(row) + "\n" for row in rows),
                encoding="utf-8",
            )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=fixture / "gold",
                production_root=fixture / "production",
            )
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_FAIL")
        self.assertEqual(
            result.audit["critical_counts"][
                "material_counter_fact_miss_count"
            ],
            1,
        )

    def test_gold_and_production_directories_cannot_nest(self) -> None:
        with self.assertRaisesRegex(ValueError, "disjoint"):
            BlindResearchQualityBenchmark().compare(
                gold_root=self.FIXTURE,
                production_root=self.FIXTURE / "production",
            )

    def test_post_run_reviewed_adjudication_supports_paraphrase_and_compound_facts(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "benchmark"
            shutil.copytree(self.FIXTURE, fixture)
            gold_root = fixture / "gold"
            production_root = fixture / "production"
            baseline = BlindResearchQualityBenchmark().compare(
                gold_root=gold_root,
                production_root=production_root,
            )
            facts_path = production_root / "production_material_facts.jsonl"
            facts = [
                json.loads(line)
                for line in facts_path.read_text(encoding="utf-8").splitlines()
            ]
            first = baseline.comparisons[0]
            original = next(
                row for row in facts if row["fact_id"] == first.production_fact_id
            )
            facts = [
                row for row in facts if row["fact_id"] != first.production_fact_id
            ]
            compound_ids = ("P-COMPOUND-A", "P-COMPOUND-B")
            for index, fact_id in enumerate(compound_ids):
                facts.append(
                    {
                        **original,
                        "fact_id": fact_id,
                        "question_family_id": (
                            f"independent_customer_booking_semantics_{index}"
                        ),
                        "subject_id": f"{original['target_id']}:commercial-booking",
                        "predicate_family": (
                            "volume alignment"
                            if index == 0
                            else "commercial commitment"
                        ),
                        "normalized_object": (
                            "current customer allocation"
                            if index == 0
                            else "booked supply visibility"
                        ),
                        "period": "FY2026 current",
                        "mechanism_scope_id": "CUSTOMER_BOOKING_VISIBILITY",
                    }
                )
            facts_path.write_text(
                "".join(
                    json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                    for row in facts
                ),
                encoding="utf-8",
            )
            gold_facts = [
                json.loads(line)
                for line in (
                    gold_root / "gold_material_facts.jsonl"
                ).read_text(encoding="utf-8").splitlines()
            ]
            baseline_id_by_gold = {
                row.gold_fact_id: row.production_fact_id
                for row in baseline.comparisons
            }
            primary_rows = []
            for gold in gold_facts:
                gold_fact_id = str(gold["fact_id"])
                production_fact_ids = (
                    list(compound_ids)
                    if gold_fact_id == first.gold_fact_id
                    else [str(baseline_id_by_gold[gold_fact_id])]
                )
                primary_rows.append(
                    {
                        "gold_fact_id": gold_fact_id,
                        "production_fact_ids": production_fact_ids,
                        "semantic_match": True,
                        "mechanism_scope_match": True,
                        "rationale": (
                            "독립 생성된 source-backed atomic fact set이 "
                            "동일한 경제 사실과 메커니즘을 구성한다."
                        ),
                    }
                )
            primary = {
                "schema_version": (
                    "e2r_v6_post_run_gold_semantic_primary_v2"
                ),
                "reviewer_identity": _portable_reviewer_identity(
                    "CODEX_POST_RUN_PRIMARY"
                ),
                "gold_visible_only_post_run": True,
                "score_or_stage_authority": False,
                "production_score_authority": False,
                "gold_fact_roster_hash": stable_hash(
                    sorted(str(row["fact_id"]) for row in gold_facts)
                ),
                "production_fact_roster_hash": stable_hash(
                    sorted(str(row["fact_id"]) for row in facts)
                ),
                "rows": primary_rows,
            }
            primary_path = (
                production_root / "post_run_gold_semantic_primary.json"
            )
            primary_path.write_text(
                json.dumps(primary, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )
            review_root = (
                production_root / "post_run_gold_semantic_reviews"
            )
            review_root.mkdir()
            primary_hash = stable_hash(primary)
            for reviewer in ("reviewer_a", "reviewer_b"):
                review = {
                    "schema_version": (
                        "e2r_v6_post_run_gold_semantic_review_v2"
                    ),
                    "reviewer_identity": _portable_reviewer_identity(
                        "CODEX_POST_RUN_REVIEWER_"
                        + reviewer.removeprefix("reviewer_").upper()
                    ),
                    "primary_payload_hash": primary_hash,
                    "gold_visible_only_post_run": True,
                    "score_or_stage_authority": False,
                    "production_score_authority": False,
                    "rows": [
                        {
                            "gold_fact_id": str(gold["fact_id"]),
                            "approve": True,
                            "rationale": (
                                "Gold와 production을 post-run에서만 대조했고 "
                                "source-backed 의미와 메커니즘이 일치한다."
                            ),
                        }
                        for gold in gold_facts
                    ],
                }
                (review_root / f"{reviewer}.json").write_text(
                    json.dumps(review, ensure_ascii=False, sort_keys=True),
                    encoding="utf-8",
                )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=gold_root,
                production_root=production_root,
                post_run_semantic_adjudication_root=production_root,
            )
            dissent_path = review_root / "reviewer_b.json"
            dissent = json.loads(
                dissent_path.read_text(encoding="utf-8")
            )
            dissent["rows"][0]["approve"] = False
            dissent["rows"][0]["rationale"] = (
                "독립 검토에서 이 의미 매핑은 충분하지 않다고 판단했다."
            )
            dissent_path.write_text(
                json.dumps(dissent, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )
            dissent_result = BlindResearchQualityBenchmark().compare(
                gold_root=gold_root,
                production_root=production_root,
                post_run_semantic_adjudication_root=production_root,
            )
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_PASS")
        self.assertEqual(
            dissent_result.status,
            "BLIND_RESEARCH_QUALITY_FAIL",
        )
        self.assertFalse(
            next(
                row
                for row in dissent_result.comparisons
                if row.gold_fact_id == first.gold_fact_id
            ).semantic_match
        )
        comparison = next(
            row
            for row in result.comparisons
            if row.gold_fact_id == first.gold_fact_id
        )
        self.assertEqual(comparison.production_fact_ids, compound_ids)
        self.assertEqual(
            comparison.semantic_match_method,
            "POST_RUN_INDEPENDENT_SEMANTIC_ADJUDICATION",
        )
        self.assertEqual(
            result.audit["post_run_semantic_adjudication"][
                "independent_review_count"
            ],
            2,
        )

    def test_post_run_adjudication_rejects_cross_target_fact_mapping(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "benchmark"
            shutil.copytree(self.FIXTURE, fixture)
            gold_root = fixture / "gold"
            production_root = fixture / "production"
            gold_facts = [
                json.loads(line)
                for line in (
                    gold_root / "gold_material_facts.jsonl"
                ).read_text(encoding="utf-8").splitlines()
            ]
            production_facts = [
                json.loads(line)
                for line in (
                    production_root / "production_material_facts.jsonl"
                ).read_text(encoding="utf-8").splitlines()
            ]
            wrong = next(
                row
                for row in production_facts
                if row["target_id"] != gold_facts[0]["target_id"]
            )
            primary = {
                "schema_version": (
                    "e2r_v6_post_run_gold_semantic_primary_v2"
                ),
                "reviewer_identity": _portable_reviewer_identity(
                    "CODEX_POST_RUN_PRIMARY"
                ),
                "gold_visible_only_post_run": True,
                "score_or_stage_authority": False,
                "production_score_authority": False,
                "gold_fact_roster_hash": stable_hash(
                    sorted(str(row["fact_id"]) for row in gold_facts)
                ),
                "production_fact_roster_hash": stable_hash(
                    sorted(str(row["fact_id"]) for row in production_facts)
                ),
                "rows": [
                    {
                        "gold_fact_id": str(gold["fact_id"]),
                        "production_fact_ids": (
                            [str(wrong["fact_id"])]
                            if index == 0
                            else []
                        ),
                        "semantic_match": index == 0,
                        "mechanism_scope_match": index == 0,
                        "rationale": "교차 target은 반드시 거절돼야 한다.",
                    }
                    for index, gold in enumerate(gold_facts)
                ],
            }
            (
                production_root / "post_run_gold_semantic_primary.json"
            ).write_text(
                json.dumps(primary, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )
            review_root = (
                production_root / "post_run_gold_semantic_reviews"
            )
            review_root.mkdir()
            with self.assertRaisesRegex(
                ValueError, "crosses target boundaries"
            ):
                BlindResearchQualityBenchmark().compare(
                    gold_root=gold_root,
                    production_root=production_root,
                    post_run_semantic_adjudication_root=production_root,
                )


if __name__ == "__main__":
    unittest.main()
