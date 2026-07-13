from __future__ import annotations

import hashlib
import json
import unittest

from e2r.research_brain.researcher_mode.prompt_projection import (
    project_counter_route_proof,
    project_citable_evidence_facts,
    project_evidence_facts,
    project_generated_queries,
    project_research_epoch_checkpoint,
    project_source_documents,
    project_source_document_table,
    project_source_graph_checkpoint,
    project_source_claims,
    project_structured_records,
    project_supervisor_failures,
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

    def test_derived_structured_lineage_is_roster_projected_once(self):
        input_ids = tuple(f"INPUT-{index:05d}" for index in range(5_000))
        row = StructuredMetricRecord(
            record_id="ROW-DERIVED",
            target_id="CURRENT-TARGET",
            as_of_date="2026-07-12",
            metric_id="eps_revision_history_pct",
            value=25.0,
            unit="PERCENT",
            period="HISTORY",
            evidence_roles=("FORWARD_GUIDANCE",),
            source_ids=("SRC-CONSENSUS",),
            source_route="POINT_IN_TIME_CONSENSUS",
            observed_at="2026-07-10",
            available_at="2026-07-10",
            record_kind="DERIVED_CONSENSUS",
            confidence=1.0,
            dataset="CONSENSUS_REVISION",
            provenance="DERIVED",
            input_record_ids=input_ids,
            metadata={"window": "90D"},
        )
        projected = project_structured_records((row,))
        series = projected["semantic_series"][0]
        snapshot = series["earliest_record"]
        self.assertEqual(snapshot["input_record_id_roster"]["count"], 5_000)
        self.assertNotIn("input_record_ids", snapshot)
        self.assertTrue(series["latest_record_same_as_earliest"])
        self.assertNotIn("latest_record", series)
        self.assertLess(len(json.dumps(projected, sort_keys=True)), 5_000)

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
        table = project_source_document_table(documents)
        self.assertEqual(table["document_count"], 1)
        self.assertTrue(table["every_document_id_preserved"])
        self.assertNotIn(
            "content_text", table["document_fields"]
        )

        checkpoint = project_source_graph_checkpoint(
            {"checkpoint_id": "CHECKPOINT", "evidence_documents": list(documents)},
            keys=("checkpoint_id", "evidence_documents"),
        )
        self.assertEqual(checkpoint["evidence_document_count"], 1)
        self.assertTrue(checkpoint["full_document_bodies_omitted_after_fact_extraction"])
        self.assertNotIn("content_text", checkpoint["evidence_documents"][0])

    def test_large_source_graph_state_is_grouped_without_fixed_top_n(self):
        candidates = tuple(
            {
                "candidate_id": f"CAND-{index:05d}",
                "ranking_status": "MATERIAL" if index % 3 else "NOT_MATERIAL",
                "fetch_status": (
                    "FULL_DOCUMENT_FETCHED"
                    if index % 5
                    else "FETCH_REJECTED"
                ),
                "source": "NAVER",
                "query_lineage_valid": True,
                "is_disclosure": index % 2 == 0,
                "is_news": index % 2 == 1,
                "is_pdf": index % 7 == 0,
                "is_report_domain": index % 11 == 0,
                "objective_ids": (f"OBJ-{index % 7}",),
                "query_ids": (f"QUERY-{index % 101}",),
                "material_priority": float(index % 10) / 10,
                "rank": index + 1,
                "snippet": "discovery text " * 100,
                "url": f"https://example.com/{index}",
            }
            for index in range(5_000)
        )
        checkpoint = {
            "checkpoint_id": "CHECKPOINT",
            "search_candidates": list(candidates),
        }
        first = project_source_graph_checkpoint(
            checkpoint,
            keys=("checkpoint_id", "search_candidates"),
        )
        second = project_source_graph_checkpoint(
            {**checkpoint, "search_candidates": list(reversed(candidates))},
            keys=("checkpoint_id", "search_candidates"),
        )
        self.assertEqual(first, second)
        projected = first["search_candidates"]
        self.assertEqual(projected["record_count"], 5_000)
        self.assertTrue(
            projected["every_record_accounted_by_hash_and_group_count"]
        )
        self.assertFalse(projected["fixed_top_n_used"])
        self.assertFalse(projected["prompt_projection_is_research_cap"])
        self.assertEqual(
            sum(projected["relation_coverage"]["objective_ids"].values()),
            5_000,
        )
        self.assertLess(len(json.dumps(first, sort_keys=True)), 100_000)

    def test_query_fact_and_failure_projections_preserve_complete_rosters(self):
        queries = tuple(
            {
                "query_id": f"QUERY-{index:04d}",
                "objective_id": f"OBJ-{index % 7}",
                "literal_query": f"회사 공시 사실 확인 {index}",
                "rationale": "현재 사실 공백을 확인한다.",
                "source_families": ("ISSUER_DISCLOSURE",),
                "execution_status": "EXECUTED",
                "prompt_hash": "x" * 64,
                "response_hash": "y" * 64,
            }
            for index in range(1_000)
        )
        query_projection = project_generated_queries(queries)
        self.assertEqual(query_projection["query_count"], 1_000)
        self.assertEqual(len(query_projection["queries"]), 1_000)
        self.assertTrue(query_projection["every_literal_query_preserved"])
        self.assertNotIn("prompt_hash", query_projection["query_fields"])
        counter_projection = project_counter_route_proof(
            tuple(
                {
                    **row,
                    "counter_or_supersession_search": True,
                    "search_result_count": index % 5,
                }
                for index, row in enumerate(queries)
            )
        )
        self.assertEqual(counter_projection["record_count"], 1_000)
        self.assertEqual(
            sum(
                counter_projection["relation_coverage"]["query_id"].values()
            ),
            1_000,
        )
        self.assertFalse(counter_projection["fixed_top_n_used"])

        facts = tuple(
            {
                "fact_id": f"FACT-{index:04d}",
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
                "subject": "현재 회사",
                "business_segment": "메모리",
                "product_family": "고대역폭 메모리",
                "economic_mechanism": f"장기 계약과 현금 전환 근거 {index}",
                "predicate": "지속 가능한 공급 가시성",
                "value": index,
                "unit": "KRW",
                "period": "2026Q2",
                "direction": "POSITIVE",
                "source_ids": (f"SRC-{index:04d}",),
                "claim_ids": (f"CLAIM-{index:04d}",),
                "quote_ids": (f"QUOTE-{index:04d}",),
                "current_lifecycle": "CURRENT",
                "source_independence_group": f"GROUP-{index % 11}",
                "confidence": 0.9,
                "question_family_tags": (f"QUESTION-{index:04d}",),
                "primitive_tags": (f"PRIMITIVE-{index:04d}",),
                "allowed_component_ids": (
                    "eps_fcf_explosion",
                    "visibility_durability",
                ),
                "structured_evidence_roles": ("FORWARD_GUIDANCE",),
            }
            for index in range(1_000)
        )
        fact_projection = project_evidence_facts(facts)
        self.assertEqual(fact_projection["fact_count"], 1_000)
        self.assertEqual(fact_projection["semantic_group_count"], 1)
        group = fact_projection["semantic_fact_groups"][0]
        self.assertEqual(group["fact_count"], 1_000)
        self.assertEqual(group["semantic_observation_count"], 1_000)
        self.assertEqual(
            group["allowed_component_coverage"],
            {"eps_fcf_explosion": 1_000, "visibility_durability": 1_000},
        )
        self.assertNotIn(
            "question_family_tags",
            fact_projection["semantic_observation_fields"],
        )
        self.assertEqual(
            len(fact_projection["question_family_tag_coverage"]), 1_000
        )
        citable_projection = project_citable_evidence_facts(facts)
        self.assertEqual(citable_projection["fact_count"], 1_000)
        self.assertEqual(len(citable_projection["facts"]), 1_000)
        self.assertTrue(citable_projection["every_fact_id_preserved"])
        self.assertEqual(citable_projection["facts"][0]["fact_id"], "FACT-0000")
        self.assertNotIn(
            "question_family_tags", citable_projection["facts"][0]
        )
        self.assertLess(
            len(json.dumps(citable_projection, ensure_ascii=False, sort_keys=True)),
            len(json.dumps(facts, ensure_ascii=False, sort_keys=True)),
        )

        claims = tuple(
            {
                "claim_id": f"CLAIM-{index:04d}",
                "document_id": f"DOC-{index:04d}",
                "source_ids": (f"SRC-{index:04d}",),
                "canonical_url": f"https://example.com/{index}",
                "exact_quote": f"원문 인용 {index}",
                "source_family": "ISSUER_DISCLOSURE",
                "source_tier": "PRIMARY",
                "published_at": "2026-07-10",
                "available_at": "2026-07-10",
                "materiality": "MATERIAL",
                "materiality_rationale": "현재 경제 사실을 직접 확인한다.",
                "accepted": True,
                "accepted_by_evidence_os": True,
                "economic_mechanism": "fact graph와 중복되는 긴 설명 " * 20,
                "provider_prompt_hash": "p" * 64,
                "provider_response_hash": "r" * 64,
            }
            for index in range(1_000)
        )
        claim_projection = project_source_claims(claims)
        self.assertEqual(claim_projection["claim_count"], 1_000)
        self.assertEqual(len(claim_projection["claims"]), 1_000)
        self.assertTrue(
            claim_projection["every_claim_id_and_exact_quote_preserved"]
        )
        self.assertNotIn(
            "economic_mechanism", claim_projection["claim_fields"]
        )
        self.assertLess(
            len(json.dumps(claim_projection, ensure_ascii=False, sort_keys=True)),
            len(json.dumps(claims, ensure_ascii=False, sort_keys=True)) // 2,
        )

        failures = tuple(
            {
                "failure_id": f"FAIL-{index:04d}",
                "failure_kind": "QUERY_FAILURE",
                "failure_stage": "SEARCH",
                "failure_reason": "PROVIDER_TIMEOUT",
                "objective_id": f"OBJ-{index % 7}",
                "query_id": f"QUERY-{index:04d}",
                "url": f"https://example.com/{index}",
                "content_hash": "z" * 64,
                "absence_eligible": False,
                "zero_result_only": False,
            }
            for index in range(1_000)
        )
        failure_projection = project_supervisor_failures(failures)
        self.assertEqual(failure_projection["failure_count"], 1_000)
        self.assertEqual(failure_projection["failure_group_count"], 1)
        self.assertEqual(len(failure_projection["failures"]), 1)
        self.assertEqual(
            failure_projection["failures"][0]["member_failure_count"],
            1_000,
        )
        self.assertTrue(failure_projection["every_failure_id_preserved"])
        self.assertNotIn("content_hash", failure_projection["failures"][0])
        self.assertLess(
            len(
                json.dumps(
                    {
                        "queries": query_projection,
                        "facts": fact_projection,
                        "failures": failure_projection,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            ),
            1_000_000,
        )

    def test_research_epoch_projection_keeps_delta_lineage_without_bodies(self):
        text = "full fetched source body " * 20_000
        documents = tuple(
            {
                "document_id": f"DOC-{index}",
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
                "canonical_url": f"https://issuer.example/{index}",
                "content_hash": hashlib.sha256(text.encode()).hexdigest(),
                "content_text": text,
                "full_fetch_performed": True,
                "snippet_only": False,
                "evidence_eligible": True,
            }
            for index in range(10)
        )
        projected = project_research_epoch_checkpoint(
            {
                "checkpoint_id": "REPOCH",
                "documents": list(documents),
                "new_facts": [{"fact_id": "FACT-1"}],
            }
        )
        self.assertEqual(projected["checkpoint_id"], "REPOCH")
        self.assertEqual(projected["document_delta_count"], 10)
        self.assertEqual(len(projected["documents"]), 10)
        self.assertTrue(
            projected["full_document_bodies_omitted_after_fact_extraction"]
        )
        self.assertNotIn("content_text", projected["documents"][0])
        self.assertFalse(
            projected["research_epoch_prompt_projection"]["fixed_top_n_used"]
        )
        self.assertLess(len(json.dumps(projected, sort_keys=True)), 30_000)


if __name__ == "__main__":
    unittest.main()
