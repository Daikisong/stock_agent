from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash
from e2r.research_brain.research_quality import (
    BlindResearchQualityBenchmark,
    POST_RUN_SEMANTIC_MATCH_CONTRACT,
    build_post_run_reviewer_identity,
)


class PostRunSemanticEconomicEventContractTests(unittest.TestCase):
    """Post-run reviewers compare economic events, not literal Gold pages."""

    ROOT = Path(__file__).resolve().parents[1]
    FIXTURE = ROOT / "tests/fixtures/semantic_scoring_v2/blind_benchmark"

    @staticmethod
    def _reviewer_identity(role_id: str) -> Mapping[str, str]:
        return build_post_run_reviewer_identity(
            role_id=role_id,
            provider_call_id="COLLABCALL-" + role_id,
            prompt_hash=stable_hash(("prompt", role_id)),
            response_hash=stable_hash(("response", role_id)),
        )

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, Any]]:
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    @staticmethod
    def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
        path.write_text(
            "".join(
                json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                for row in rows
            ),
            encoding="utf-8",
        )

    def _copy_fixture(
        self, temporary_root: str
    ) -> tuple[Path, Path, Path]:
        fixture = Path(temporary_root) / "benchmark"
        shutil.copytree(self.FIXTURE, fixture)
        return fixture, fixture / "gold", fixture / "production"

    @staticmethod
    def _baseline_mapping(
        *, gold_root: Path, production_root: Path
    ) -> dict[str, str]:
        result = BlindResearchQualityBenchmark().compare(
            gold_root=gold_root,
            production_root=production_root,
        )
        return {
            row.gold_fact_id: str(row.production_fact_id)
            for row in result.comparisons
        }

    def _write_adjudication(
        self,
        *,
        gold_root: Path,
        production_root: Path,
        default_mapping: Mapping[str, str],
        mapping_overrides: Mapping[str, Sequence[str]],
        review_approval_overrides: Mapping[str, bool] | None = None,
    ) -> None:
        gold_facts = self._read_jsonl(
            gold_root / "gold_material_facts.jsonl"
        )
        production_facts = self._read_jsonl(
            production_root / "production_material_facts.jsonl"
        )
        primary_rows = []
        for gold in gold_facts:
            gold_fact_id = str(gold["fact_id"])
            production_fact_ids = list(
                mapping_overrides.get(
                    gold_fact_id,
                    (str(default_mapping[gold_fact_id]),),
                )
            )
            primary_rows.append(
                {
                    "gold_fact_id": gold_fact_id,
                    "production_fact_ids": production_fact_ids,
                    "semantic_match": bool(production_fact_ids),
                    "mechanism_scope_match": bool(production_fact_ids),
                    "rationale": (
                        "독립 reviewer가 literal 페이지나 row shape가 아니라 "
                        "target-bound core economic event와 mechanism을 판정한다."
                    ),
                }
            )
        primary = {
            "schema_version": "e2r_v6_post_run_gold_semantic_primary_v2",
            "reviewer_identity": self._reviewer_identity(
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
            "rows": primary_rows,
        }
        (production_root / "post_run_gold_semantic_primary.json").write_text(
            json.dumps(primary, ensure_ascii=False, sort_keys=True),
            encoding="utf-8",
        )
        review_root = production_root / "post_run_gold_semantic_reviews"
        review_root.mkdir()
        approval_overrides = dict(review_approval_overrides or {})
        for reviewer in ("reviewer_a", "reviewer_b"):
            review = {
                "schema_version": "e2r_v6_post_run_gold_semantic_review_v2",
                "reviewer_identity": self._reviewer_identity(
                    "CODEX_POST_RUN_REVIEWER_"
                    + reviewer.removeprefix("reviewer_").upper()
                ),
                "primary_payload_hash": stable_hash(primary),
                "gold_visible_only_post_run": True,
                "score_or_stage_authority": False,
                "production_score_authority": False,
                "rows": [
                    {
                        "gold_fact_id": str(gold["fact_id"]),
                        "approve": approval_overrides.get(
                            str(gold["fact_id"]), True
                        ),
                        "rationale": (
                            "core event boundaries가 맞으면 승인하고 industry "
                            "general, cross-target, wrong-segment이면 거절한다."
                        ),
                    }
                    for gold in gold_facts
                ],
            }
            (review_root / f"{reviewer}.json").write_text(
                json.dumps(review, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )

    def test_customer_official_compound_event_does_not_require_same_named_page(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, gold_root, production_root = self._copy_fixture(tmp)
            default_mapping = self._baseline_mapping(
                gold_root=gold_root,
                production_root=production_root,
            )
            gold_path = gold_root / "gold_material_facts.jsonl"
            gold_facts = self._read_jsonl(gold_path)
            gold_id = "G-B-CAPACITY"
            for row in gold_facts:
                if row["fact_id"] == gold_id:
                    row.update(
                        {
                            "question_family_id": (
                                "customer_technical_participation_corroboration"
                            ),
                            "subject_id": "TARGET-B/HBM4/CUSTOMER-ECOSYSTEM",
                            "predicate_family": (
                                "CUSTOMER_OFFICIAL_TECHNICAL_PARTICIPATION"
                            ),
                            "normalized_object": (
                                "CUSTOMER_CORROBORATED_HBM4_CO_DESIGN"
                            ),
                            "period": "2026",
                            "mechanism_scope_id": (
                                "HBM_CUSTOMER_ECOSYSTEM_CORROBORATION"
                            ),
                        }
                    )
            self._write_jsonl(gold_path, gold_facts)

            facts_path = production_root / "production_material_facts.jsonl"
            production_facts = [
                row
                for row in self._read_jsonl(facts_path)
                if row["fact_id"] != default_mapping[gold_id]
            ]
            compound_ids = (
                "P-CUSTOMER-TECHNICAL-PARTICIPATION",
                "P-CUSTOMER-DIRECT-CORROBORATION",
            )
            production_facts.extend(
                [
                    {
                        "fact_id": compound_ids[0],
                        "target_id": "TARGET-B",
                        "question_family_id": "customer_event_agenda",
                        "subject_id": "TARGET-B/HBM4/SESSION-A",
                        "predicate_family": "ENGINEER_TECHNICAL_PARTICIPATION",
                        "normalized_object": "HBM4_INTEGRATION_SESSION_LISTED",
                        "period": "2026",
                        "mechanism_scope_id": (
                            "HBM_CUSTOMER_ECOSYSTEM_CORROBORATION"
                        ),
                        "source_tier": "CUSTOMER_OFFICIAL",
                        "temporal_status": "CURRENT",
                        "as_of_date": "2026-07-11",
                        "discovery_origin": "CANONICAL_SOURCE_TASK",
                    },
                    {
                        "fact_id": compound_ids[1],
                        "target_id": "TARGET-B",
                        "question_family_id": "customer_technical_profile",
                        "subject_id": "TARGET-B/HBM4/PROFILE-B",
                        "predicate_family": "CUSTOMER_ATTRIBUTED_CO_DESIGN",
                        "normalized_object": "HBM4_CO_DESIGN_ATTRIBUTED_TO_TARGET",
                        "period": "2026",
                        "mechanism_scope_id": (
                            "HBM_CUSTOMER_ECOSYSTEM_CORROBORATION"
                        ),
                        "source_tier": "CUSTOMER_OFFICIAL",
                        "temporal_status": "CURRENT",
                        "as_of_date": "2026-07-11",
                        "discovery_origin": "CANONICAL_SOURCE_TASK",
                    },
                ]
            )
            self._write_jsonl(facts_path, production_facts)
            self._write_adjudication(
                gold_root=gold_root,
                production_root=production_root,
                default_mapping=default_mapping,
                mapping_overrides={gold_id: compound_ids},
            )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=gold_root,
                production_root=production_root,
                post_run_semantic_adjudication_root=production_root,
            )

        comparison = next(
            row for row in result.comparisons if row.gold_fact_id == gold_id
        )
        self.assertTrue(comparison.semantic_match)
        self.assertEqual(comparison.production_fact_ids, compound_ids)
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_PASS")
        contract = result.audit["post_run_semantic_adjudication"][
            "semantic_match_contract"
        ]
        self.assertEqual(contract, POST_RUN_SEMANTIC_MATCH_CONTRACT)
        self.assertFalse(contract["literal_page_identity_required"])
        self.assertTrue(contract["compound_atomic_fact_sets_allowed"])

    def test_component_context_counter_can_match_same_dividend_support_event(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, gold_root, production_root = self._copy_fixture(tmp)
            default_mapping = self._baseline_mapping(
                gold_root=gold_root,
                production_root=production_root,
            )
            gold_id = "G-A-ALLOCATION"
            gold_path = gold_root / "gold_material_facts.jsonl"
            gold_facts = self._read_jsonl(gold_path)
            for row in gold_facts:
                if row["fact_id"] == gold_id:
                    row.update(
                        {
                            "question_family_id": "quarterly_dividend_actual",
                            "subject_id": "TARGET-A/SHAREHOLDERS",
                            "predicate_family": "DIVIDEND_APPROVED_AND_PAYABLE",
                            "normalized_object": (
                                "Q1_DIVIDEND_KRW_2_453_316_MILLION"
                            ),
                            "period": "2026Q1",
                            "mechanism_scope_id": (
                                "SHAREHOLDER_RETURN_DIVIDEND"
                            ),
                            "fact_role": "SUPPORT",
                        }
                    )
            self._write_jsonl(gold_path, gold_facts)

            facts_path = production_root / "production_material_facts.jsonl"
            production_facts = self._read_jsonl(facts_path)
            replacement_id = "P-DIVIDEND-COMPONENT-COUNTER"
            for row in production_facts:
                if row["fact_id"] == default_mapping[gold_id]:
                    row.update(
                        {
                            "fact_id": replacement_id,
                            "question_family_id": "capital_allocation_burden",
                            "subject_id": "TARGET-A/CAPITAL-ALLOCATION",
                            "predicate_family": "DIVIDEND_PAYABLE_RECOGNIZED",
                            "normalized_object": (
                                "KRW_2_453_316_000_000_DIVIDEND_PAYABLE"
                            ),
                            "period": "2026Q1",
                            "mechanism_scope_id": (
                                "SHAREHOLDER_RETURN_DIVIDEND"
                            ),
                            "fact_role": "COUNTER",
                        }
                    )
            self._write_jsonl(facts_path, production_facts)
            self._write_adjudication(
                gold_root=gold_root,
                production_root=production_root,
                default_mapping=default_mapping,
                mapping_overrides={gold_id: (replacement_id,)},
            )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=gold_root,
                production_root=production_root,
                post_run_semantic_adjudication_root=production_root,
            )

        comparison = next(
            row for row in result.comparisons if row.gold_fact_id == gold_id
        )
        self.assertTrue(comparison.semantic_match)
        self.assertEqual(comparison.production_fact_id, replacement_id)
        self.assertFalse(
            POST_RUN_SEMANTIC_MATCH_CONTRACT[
                "component_context_fact_role_identity_required"
            ]
        )
        self.assertTrue(
            POST_RUN_SEMANTIC_MATCH_CONTRACT[
                "canonical_numeric_meaning_required"
            ]
        )

    def test_independent_reviews_reject_industry_general_and_wrong_segment(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, gold_root, production_root = self._copy_fixture(tmp)
            default_mapping = self._baseline_mapping(
                gold_root=gold_root,
                production_root=production_root,
            )
            facts_path = production_root / "production_material_facts.jsonl"
            production_facts = self._read_jsonl(facts_path)
            replacements = {
                "G-A-ALLOCATION": "P-WRONG-FOUNDRY-SEGMENT",
                "G-A-ASP": "P-INDUSTRY-GENERAL-NO-ATTRIBUTION",
            }
            replaced_ids = {
                default_mapping[gold_id] for gold_id in replacements
            }
            production_facts = [
                row
                for row in production_facts
                if row["fact_id"] not in replaced_ids
            ]
            production_facts.extend(
                [
                    {
                        "fact_id": replacements["G-A-ALLOCATION"],
                        "target_id": "TARGET-A",
                        "question_family_id": "foundry_capacity",
                        "subject_id": "TARGET-A/FOUNDRY",
                        "predicate_family": "FOUNDRY_CAPACITY_EXPANDED",
                        "normalized_object": "FOUNDRY_WAFER_CAPACITY_UP",
                        "period": "2026",
                        "mechanism_scope_id": "FOUNDRY_SUPPLY_RESPONSE",
                        "source_tier": "ISSUER_OFFICIAL",
                        "temporal_status": "CURRENT",
                        "as_of_date": "2026-07-11",
                        "discovery_origin": "CANONICAL_SOURCE_TASK",
                    },
                    {
                        "fact_id": replacements["G-A-ASP"],
                        "target_id": "TARGET-A",
                        "question_family_id": "industry_memory_pricing",
                        "subject_id": "INDUSTRY/MEMORY",
                        "predicate_family": "INDUSTRY_ASP_INCREASED",
                        "normalized_object": "INDUSTRY_MEMORY_ASP_UP",
                        "period": "2026Q1",
                        "mechanism_scope_id": "INDUSTRY_MEMORY_PRICING",
                        "source_tier": "REGULATORY_OFFICIAL",
                        "temporal_status": "CURRENT",
                        "as_of_date": "2026-07-11",
                        "discovery_origin": "CANONICAL_SOURCE_TASK",
                    },
                ]
            )
            self._write_jsonl(facts_path, production_facts)
            self._write_adjudication(
                gold_root=gold_root,
                production_root=production_root,
                default_mapping=default_mapping,
                mapping_overrides={
                    gold_id: (production_id,)
                    for gold_id, production_id in replacements.items()
                },
                review_approval_overrides={
                    gold_id: False for gold_id in replacements
                },
            )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=gold_root,
                production_root=production_root,
                post_run_semantic_adjudication_root=production_root,
            )

        comparison_by_id = {
            row.gold_fact_id: row for row in result.comparisons
        }
        self.assertFalse(
            comparison_by_id["G-A-ALLOCATION"].semantic_match
        )
        self.assertFalse(comparison_by_id["G-A-ASP"].semantic_match)
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_FAIL")
        self.assertIn(
            "WRONG_SEGMENT",
            POST_RUN_SEMANTIC_MATCH_CONTRACT["prohibited_substitutions"],
        )
        self.assertIn(
            "INDUSTRY_GENERAL_WITHOUT_TARGET_ATTRIBUTION",
            POST_RUN_SEMANTIC_MATCH_CONTRACT["prohibited_substitutions"],
        )

    def test_cross_target_mapping_remains_a_hard_validation_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, gold_root, production_root = self._copy_fixture(tmp)
            default_mapping = self._baseline_mapping(
                gold_root=gold_root,
                production_root=production_root,
            )
            self._write_adjudication(
                gold_root=gold_root,
                production_root=production_root,
                default_mapping=default_mapping,
                mapping_overrides={"G-A-ALLOCATION": ("P-201",)},
            )
            with self.assertRaisesRegex(
                ValueError, "crosses target boundaries"
            ):
                BlindResearchQualityBenchmark().compare(
                    gold_root=gold_root,
                    production_root=production_root,
                    post_run_semantic_adjudication_root=production_root,
                )

    def test_production_fact_id_reuse_remains_a_hard_validation_error(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, gold_root, production_root = self._copy_fixture(tmp)
            default_mapping = self._baseline_mapping(
                gold_root=gold_root,
                production_root=production_root,
            )
            self._write_adjudication(
                gold_root=gold_root,
                production_root=production_root,
                default_mapping=default_mapping,
                mapping_overrides={
                    "G-A-ALLOCATION": ("P-101",),
                    "G-A-SHIPMENT": ("P-101",),
                },
            )
            with self.assertRaisesRegex(
                ValueError, "reuses a production fact"
            ):
                BlindResearchQualityBenchmark().compare(
                    gold_root=gold_root,
                    production_root=production_root,
                    post_run_semantic_adjudication_root=production_root,
                )

    def test_filesystem_reviewer_identity_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, gold_root, production_root = self._copy_fixture(tmp)
            default_mapping = self._baseline_mapping(
                gold_root=gold_root,
                production_root=production_root,
            )
            self._write_adjudication(
                gold_root=gold_root,
                production_root=production_root,
                default_mapping=default_mapping,
                mapping_overrides={},
            )
            primary_path = (
                production_root / "post_run_gold_semantic_primary.json"
            )
            primary = json.loads(primary_path.read_text(encoding="utf-8"))
            primary["reviewer_identity"]["provider_call_id"] = (
                "/root/primary_reviewer"
            )
            primary_path.write_text(
                json.dumps(primary, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                ValueError, "reviewer identity is invalid"
            ):
                BlindResearchQualityBenchmark().compare(
                    gold_root=gold_root,
                    production_root=production_root,
                    post_run_semantic_adjudication_root=production_root,
                )


if __name__ == "__main__":
    unittest.main()
