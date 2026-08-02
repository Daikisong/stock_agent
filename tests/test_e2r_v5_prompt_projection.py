from __future__ import annotations

import hashlib
import json
import unittest

from e2r.research_brain.researcher_mode.prompt_projection import (
    citable_fact_id_by_row_index,
    project_candidate_ranking_evidence_context,
    project_counter_route_proof,
    project_citable_evidence_facts,
    project_current_decision_citable_facts,
    project_evidence_facts,
    project_fact_extraction_evidence_context,
    project_fact_extraction_score_gap_context,
    project_generated_queries,
    project_peer_selection_context,
    project_query_planner_failures,
    project_query_score_gap_context,
    project_research_source_claim_profile,
    project_research_source_document_profile,
    project_research_epoch_checkpoint,
    project_source_documents,
    project_source_document_table,
    project_source_graph_checkpoint,
    project_source_claim_profile,
    project_source_claims,
    project_source_document_profile,
    project_structured_records,
    project_supervisor_evidence_facts,
    project_supervisor_failures,
    project_supervisor_source_graph_checkpoint,
    resolve_citable_fact_row_indices,
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
        self.assertEqual(
            first["metadata_projection"]["metadata_record_count"],
            1_000,
        )
        self.assertNotIn(
            "metadata",
            first["semantic_series"][0]["earliest_record"],
        )
        self.assertLess(len(json.dumps(first, sort_keys=True)), 10_000)

    def test_large_structured_metadata_is_hash_accounted_once(self):
        rows = tuple(
            StructuredMetricRecord(
                record_id=f"ROW-METADATA-{index:04d}",
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
                metric_id="consensus_forward_eps",
                value=float(index),
                unit="KRW",
                period=f"2026Q{index % 4 + 1}",
                evidence_roles=("FORWARD_GUIDANCE",),
                source_ids=("SRC-CONSENSUS",),
                source_route="COMPANYGUIDE",
                observed_at="2026-07-10",
                available_at="2026-07-10",
                record_kind="CONSENSUS",
                confidence=0.9,
                dataset="CONSENSUS_REVISION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "observed_fact": True,
                    "connector_payload": "원본 메타데이터 " * 10_000,
                },
            )
            for index in range(100)
        )

        projected = project_structured_records(rows)
        encoded = json.dumps(projected, ensure_ascii=False, sort_keys=True)
        metadata = projected["metadata_projection"]
        self.assertEqual(metadata["metadata_record_count"], 100)
        self.assertEqual(metadata["metadata_boolean_field_count"], 100)
        self.assertTrue(metadata["full_metadata_persisted_outside_prompt"])
        self.assertNotIn("원본 메타데이터", encoded)
        self.assertLess(len(encoded), 10_000)

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
                    "objective_id": row["objective_id"],
                    "route_kind": (
                        "COUNTER" if index % 2 == 0 else "SUPERSESSION"
                    ),
                    "query_ids": [row["query_id"]],
                    "document_ids": [f"DOC-{index:04d}"],
                    "fact_ids": [f"FACT-{index:04d}"],
                    "parser_extractor_verified": True,
                    "zero_result_only": False,
                }
                for index, row in enumerate(queries)
            )
        )
        self.assertEqual(counter_projection["record_count"], 1_000)
        self.assertEqual(
            sum(
                counter_projection["relation_coverage"]["objective_id"].values()
            ),
            1_000,
        )
        self.assertEqual(counter_projection["semantic_group_count"], 2)
        self.assertTrue(
            all(
                group["relation_coverage"]["query_ids"][
                    "full_relation_values_persisted_outside_prompt"
                ]
                for group in counter_projection["semantic_groups"]
            )
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
        extraction_context = project_fact_extraction_evidence_context(facts)
        reversed_extraction_context = project_fact_extraction_evidence_context(
            tuple(reversed(facts))
        )
        self.assertEqual(extraction_context, reversed_extraction_context)
        self.assertEqual(extraction_context["fact_count"], 1_000)
        self.assertEqual(extraction_context["semantic_state_group_count"], 1)
        self.assertEqual(
            extraction_context["semantic_state_groups"][0][-2],
            1_000,
        )
        self.assertTrue(
            extraction_context[
                "every_fact_accounted_by_hash_and_group_count"
            ]
        )
        self.assertEqual(
            extraction_context["allowed_component_coverage"],
            {"eps_fcf_explosion": 1_000, "visibility_durability": 1_000},
        )
        self.assertEqual(extraction_context["source_id_roster"]["count"], 1_000)
        self.assertEqual(extraction_context["claim_id_roster"]["count"], 1_000)
        self.assertEqual(extraction_context["quote_id_roster"]["count"], 1_000)
        self.assertFalse(extraction_context["fixed_top_n_used"])
        self.assertFalse(extraction_context["score_authority"])
        self.assertNotIn("semantic_observations", extraction_context)
        self.assertLess(
            len(
                json.dumps(
                    extraction_context,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            ),
            20_000,
        )
        citable_projection = project_citable_evidence_facts(facts)
        self.assertEqual(citable_projection["fact_count"], 1_000)
        self.assertEqual(len(citable_projection["facts"]), 1_000)
        self.assertTrue(citable_projection["every_fact_id_preserved"])
        first_fact = dict(
            zip(
                citable_projection["fact_fields"],
                citable_projection["facts"][0],
            )
        )
        self.assertEqual(first_fact["fact_row_index"], 0)
        self.assertEqual(first_fact["fact_id"], "FACT-0000")
        fact_id_by_row_index = citable_fact_id_by_row_index(citable_projection)
        self.assertEqual(
            resolve_citable_fact_row_indices(
                [0, 999],
                fact_id_by_row_index=fact_id_by_row_index,
                label="selected_fact_row_indices",
            ),
            ("FACT-0000", "FACT-0999"),
        )
        with self.assertRaisesRegex(ValueError, "unknown fact row indices"):
            resolve_citable_fact_row_indices(
                [1_000],
                fact_id_by_row_index=fact_id_by_row_index,
                label="selected_fact_row_indices",
            )
        self.assertNotIn(
            "question_family_tags", citable_projection["fact_fields"]
        )
        for repeated_lineage_field in (
            "source_ids",
            "claim_ids",
            "quote_ids",
            "corroborating_independence_groups",
        ):
            self.assertNotIn(
                repeated_lineage_field, citable_projection["fact_fields"]
            )
        self.assertTrue(
            citable_projection[
                "every_fact_lineage_accounted_by_count_and_hash"
            ]
        )
        self.assertEqual(citable_projection["source_id_roster"]["count"], 1_000)
        self.assertEqual(citable_projection["claim_id_roster"]["count"], 1_000)
        self.assertEqual(citable_projection["quote_id_roster"]["count"], 1_000)
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
        claim_profile = project_source_claim_profile(claims)
        self.assertEqual(claim_profile["record_count"], 1_000)
        self.assertTrue(
            claim_profile["every_record_accounted_by_hash_and_group_count"]
        )
        self.assertTrue(
            claim_profile["every_exact_quote_accounted_by_count_and_hash"]
        )
        self.assertNotIn(
            "원문 인용 999",
            json.dumps(claim_profile, ensure_ascii=False, sort_keys=True),
        )

        documents = tuple(
            {
                "document_id": f"DOC-{index:04d}",
                "canonical_url": f"https://example.com/{index}",
                "title": f"공식 문서 {index}",
                "content_hash": hashlib.sha256(str(index).encode()).hexdigest(),
                "source_family": "ISSUER_DISCLOSURE",
                "source_provider": "OFFICIAL",
                "published_at": "2026-07-10",
                "available_at": "2026-07-10",
                "content_type": "application/pdf",
                "evidence_eligible": True,
                "query_ids": (f"QUERY-{index:04d}",),
                "objective_ids": (f"OBJECTIVE-{index % 7}",),
                "content_text": "이미 사실 추출이 끝난 긴 원문 " * 100,
            }
            for index in range(1_000)
        )
        document_profile = project_source_document_profile(documents)
        self.assertEqual(document_profile["record_count"], 1_000)
        self.assertTrue(
            document_profile["every_record_accounted_by_hash_and_group_count"]
        )
        self.assertEqual(document_profile["canonical_url_roster"]["count"], 1_000)
        self.assertNotIn(
            "이미 사실 추출이 끝난 긴 원문",
            json.dumps(document_profile, ensure_ascii=False, sort_keys=True),
        )
        compact_research_context = {
            "facts": citable_projection,
            "claims": claim_profile,
            "documents": document_profile,
        }
        raw_research_context = {
            "facts": facts,
            "claims": claims,
            "documents": documents,
        }
        self.assertLess(
            len(
                json.dumps(
                    compact_research_context,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            ),
            len(
                json.dumps(
                    raw_research_context,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            // 3,
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

    def test_supervisor_and_peer_projections_scale_without_dropping_ledgers(self):
        facts = tuple(
            {
                "fact_id": f"FACT-{index:04d}",
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
                "subject": f"현재 회사 제품군 {index % 9}",
                "business_segment": f"사업부 {index % 4}",
                "product_family": f"제품군 {index % 11}",
                "economic_mechanism": (
                    f"검증된 경제 메커니즘 {index} " + "상세 설명 " * 20
                ),
                "predicate": f"ECONOMIC_PREDICATE_{index:04d}",
                "value": index,
                "unit": "KRW",
                "period": f"2026Q{index % 4 + 1}",
                "direction": "COUNTER" if index % 7 == 0 else "POSITIVE",
                "current_lifecycle": "OPEN" if index % 5 == 0 else "CURRENT",
                "confidence": 0.9,
                "source_ids": (f"SRC-{index:04d}",),
                "claim_ids": (f"CLAIM-{index:04d}",),
                "quote_ids": (f"QUOTE-{index:04d}",),
                "source_independence_group": f"GROUP-{index % 13}",
                "structured_evidence_roles": ("FORWARD_GUIDANCE",),
                "allowed_component_ids": ("earnings_visibility",),
            }
            for index in range(1_000)
        )
        claims = tuple(
            {
                "claim_id": f"CLAIM-{index:04d}",
                "subject": f"현재 회사 제품군 {index % 9}",
                "business_segment": f"사업부 {index % 4}",
                "product_family": f"제품군 {index % 11}",
                "economic_mechanism": (
                    f"검증된 경제 메커니즘 {index} " + "상세 설명 " * 20
                ),
                "predicate": f"ECONOMIC_PREDICATE_{index:04d}",
                "direction": "COUNTER" if index % 7 == 0 else "POSITIVE",
                "source_family": "ISSUER_PRESENTATION",
                "exact_quote": f"원문 인용 {index} " + "직접 근거 " * 20,
            }
            for index in range(1_000)
        )

        supervisor_facts = project_supervisor_evidence_facts(facts)
        peer_context = project_peer_selection_context(facts, claims)
        self.assertEqual(supervisor_facts["record_count"], 1_000)
        self.assertTrue(
            supervisor_facts[
                "every_record_accounted_by_hash_and_group_count"
            ]
        )
        self.assertEqual(supervisor_facts["predicate_roster"]["count"], 1_000)
        self.assertEqual(
            supervisor_facts["source_independence_group_roster"]["count"],
            13,
        )
        self.assertTrue(
            peer_context[
                "every_fact_and_claim_accounted_by_hash_and_group_count"
            ]
        )
        self.assertTrue(
            all(
                group["relation_coverage"]["predicate"]
                for group in peer_context["evidence_business_profile"][
                    "semantic_groups"
                ]
            )
        )
        self.assertFalse(supervisor_facts["fixed_top_n_used"])
        self.assertFalse(peer_context["fixed_top_n_used"])
        supervisor_encoded = json.dumps(
            supervisor_facts, ensure_ascii=False, sort_keys=True
        )
        peer_encoded = json.dumps(peer_context, ensure_ascii=False, sort_keys=True)
        self.assertLess(len(supervisor_encoded), 100_000)
        self.assertLess(len(peer_encoded), 250_000)
        self.assertNotIn("검증된 경제 메커니즘 999", supervisor_encoded)
        self.assertNotIn("원문 인용 999", peer_encoded)

    def test_supervisor_projection_exposes_source_family_independence_coverage(
        self,
    ) -> None:
        facts = (
            {
                "fact_id": "FACT-ISSUER",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "subject": "named technical relationship",
                "economic_mechanism": "technical participation",
                "predicate": "relationship announced",
                "direction": "POSITIVE",
                "current_lifecycle": "CURRENT",
                "confidence": 0.7,
                "source_ids": ("DOC-ISSUER",),
                "claim_ids": ("CLAIM-ISSUER",),
                "quote_ids": ("QUOTE-ISSUER",),
                "source_independence_group": "ISSUER_NEWSROOM:issuer.example",
                "corroborating_independence_groups": (
                    "ISSUER_NEWSROOM:issuer.example",
                ),
                "structured_evidence_roles": (),
                "allowed_component_ids": ("information_confidence",),
            },
            {
                "fact_id": "FACT-CUSTOMER",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "subject": "named technical relationship",
                "economic_mechanism": "independent confirmation",
                "predicate": "relationship corroborated",
                "direction": "POSITIVE",
                "current_lifecycle": "CURRENT",
                "confidence": 0.9,
                "source_ids": ("DOC-CUSTOMER",),
                "claim_ids": ("CLAIM-CUSTOMER",),
                "quote_ids": ("QUOTE-CUSTOMER",),
                "source_independence_group": (
                    "CUSTOMER_OFFICIAL:customer.example"
                ),
                "corroborating_independence_groups": (
                    "ISSUER_NEWSROOM:issuer.example",
                ),
                "structured_evidence_roles": (),
                "allowed_component_ids": ("information_confidence",),
            },
        )

        projection = project_supervisor_evidence_facts(facts)
        review = projection["independent_corroboration_review"]

        self.assertEqual(
            projection["schema_version"],
            "e2r_v5_supervisor_fact_prompt_projection_v4",
        )
        self.assertEqual(
            review["primary_source_family_coverage"],
            {"CUSTOMER_OFFICIAL": 1, "ISSUER_NEWSROOM": 1},
        )
        self.assertEqual(
            review["corroborating_source_family_coverage"],
            {"ISSUER_NEWSROOM": 1},
        )
        self.assertEqual(
            review["fact_without_explicit_corroborating_group_count"],
            1,
        )
        self.assertTrue(review["llm_owns_gap_materiality"])
        self.assertNotIn("issuer.example", json.dumps(review))
        relationship_profiles = review["relationship_profiles"]
        issuer_only = next(
            row
            for row in relationship_profiles
            if row["relationship"]["economic_mechanism"]
            == "technical participation"
        )
        self.assertEqual(
            issuer_only["primary_source_family_coverage"],
            {"ISSUER_NEWSROOM": 1},
        )
        self.assertFalse(issuer_only["independent_corroboration_present"])
        self.assertTrue(
            review[
                "every_information_confidence_fact_accounted_by_hash_and_group_count"
            ]
        )

    def test_supervisor_failure_groups_ignore_literal_transport_detail(self):
        failures = (
            {
                "failure_id": "FAIL-1",
                "failure_kind": "DOCUMENT_REJECTION",
                "failure_stage": "FULL_FETCH",
                "failure_reason": (
                    "UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH:"
                    "query=삼성전자 2026 HBM url=https://example.com/a"
                ),
                "objective_id": "OBJ-1",
                "query_id": "QUERY-1",
                "url": "https://example.com/a",
            },
            {
                "failure_id": "FAIL-2",
                "failure_kind": "DOCUMENT_REJECTION",
                "failure_stage": "FULL_FETCH",
                "failure_reason": (
                    "UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH:"
                    "query=삼성전자 공급계약 url=https://example.com/b"
                ),
                "objective_id": "OBJ-2",
                "query_id": "QUERY-2",
                "url": "https://example.com/b",
            },
            {
                "failure_id": "FAIL-3",
                "failure_kind": "DOCUMENT_REJECTION",
                "failure_stage": "FULL_FETCH",
                "failure_reason": (
                    "FUTURE_DOCUMENT_AFTER_FULL_FETCH:published_at=2026-07-20"
                ),
                "objective_id": "OBJ-3",
                "query_id": "QUERY-3",
                "url": "https://example.com/c",
            },
        )

        projection = project_supervisor_failures(failures)

        self.assertEqual(projection["failure_count"], 3)
        self.assertEqual(projection["failure_group_count"], 2)
        self.assertTrue(projection["every_failure_id_preserved"])
        grouped = {
            row["failure_reason"]: row
            for row in projection["failures"]
        }
        same_class = grouped["UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH"]
        self.assertEqual(same_class["member_failure_count"], 2)
        self.assertEqual(
            same_class["member_failure_ids"],
            ["FAIL-1", "FAIL-2"],
        )
        self.assertEqual(
            {
                failure_id
                for members in projection["failure_group_members"].values()
                for failure_id in members
            },
            {"FAIL-1", "FAIL-2", "FAIL-3"},
        )

    def test_peer_selection_ignores_claim_extraction_transport_lineage(self):
        fact = {
            "fact_id": "FACT-1",
            "subject": "현재 회사 메모리 사업",
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism": "고객 배정이 매출 가시성을 만든다",
            "predicate": "CUSTOMER_ALLOCATION_CONFIRMED",
            "direction": "POSITIVE",
            "current_lifecycle": "CURRENT",
            "confidence": 0.9,
        }
        claim = {
            "claim_id": "CLAIM-1",
            "subject": "현재 회사 메모리 사업",
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism": "고객 배정이 매출 가시성을 만든다",
            "predicate": "CUSTOMER_ALLOCATION_CONFIRMED",
            "direction": "POSITIVE",
            "source_family": "ISSUER_PRESENTATION",
            "exact_quote": "고객 배정 물량을 확보했다",
            "provider_name": "FIRST_EXTRACTOR",
            "provider_prompt_hash": "PROMPT-1",
            "provider_response_hash": "RESPONSE-1",
        }
        reextracted_claim = {
            **claim,
            "provider_name": "SECOND_EXTRACTOR",
            "provider_prompt_hash": "PROMPT-999",
            "provider_response_hash": "RESPONSE-999",
        }
        first = project_peer_selection_context((fact,), (claim,))
        second = project_peer_selection_context((fact,), (reextracted_claim,))
        self.assertEqual(first, second)
        self.assertTrue(
            first["source_claim_business_profile"][
                "extraction_transport_lineage_excluded_from_provider"
            ]
        )

        changed_economics = {
            **reextracted_claim,
            "economic_mechanism": "가격 하락이 매출 가시성을 훼손한다",
            "direction": "COUNTER",
        }
        self.assertNotEqual(
            first,
            project_peer_selection_context((fact,), (changed_economics,)),
        )

    def test_current_research_and_query_contexts_scale_without_evidence_loss(self):
        facts = tuple(
            {
                "fact_id": f"FACT-{index:04d}",
                "subject": "현재 회사",
                "business_segment": f"사업부-{index % 4}",
                "product_family": f"제품군-{index % 9}",
                "economic_mechanism": f"현금 전환 메커니즘-{index % 31}",
                "predicate": f"PREDICATE-{index % 37}",
                "value": index % 101,
                "unit": "KRW",
                "period": f"2026Q{index % 4 + 1}",
                "direction": "COUNTER" if index % 7 == 0 else "POSITIVE",
                "current_lifecycle": (
                    "CURRENT" if index < 900 else "SUPERSEDED"
                ),
                "confidence": 0.9,
                "structured_evidence_roles": ("FORWARD_GUIDANCE",),
                "allowed_component_ids": ("earnings_visibility",),
            }
            for index in range(3_000)
        )
        projection = project_current_decision_citable_facts(facts)
        self.assertEqual(projection["input_fact_count"], 3_000)
        self.assertEqual(projection["fact_count"], 900)
        self.assertEqual(projection["closed_fact_count"], 2_100)
        self.assertTrue(projection["every_input_fact_accounted"])
        self.assertTrue(projection["every_current_fact_individually_citable"])
        self.assertTrue(
            projection["every_closed_fact_accounted_by_hash_and_group_count"]
        )
        self.assertNotIn("fact_id", projection["fact_fields"])
        fact_ids = citable_fact_id_by_row_index(projection)
        self.assertEqual(len(fact_ids), 900)
        self.assertEqual(fact_ids[0], "FACT-0000")
        provider_projection_metadata = {
            key: value
            for key, value in projection.items()
            if key not in {"facts", "fact_id_by_row_index"}
        }
        provider_projection = {
            "current_evidence_fact_projection": provider_projection_metadata,
            "current_evidence_fact_graph": projection["facts"],
        }
        self.assertNotIn("fact_id_by_row_index", provider_projection_metadata)
        self.assertNotIn(
            "FACT-0000",
            json.dumps(provider_projection, ensure_ascii=False, sort_keys=True),
        )
        self.assertLess(
            len(json.dumps(provider_projection, ensure_ascii=False, sort_keys=True)),
            100_000,
        )
        ranking_projection = project_candidate_ranking_evidence_context(facts)
        ranking_encoded = json.dumps(
            ranking_projection, ensure_ascii=False, sort_keys=True
        )
        self.assertEqual(ranking_projection["input_fact_count"], 3_000)
        self.assertEqual(ranking_projection["fact_count"], 900)
        self.assertEqual(ranking_projection["closed_fact_count"], 2_100)
        self.assertTrue(
            ranking_projection["every_current_fact_individually_accounted"]
        )
        self.assertTrue(ranking_projection["every_input_fact_accounted"])
        self.assertNotIn("fact_id_by_row_index", ranking_projection)
        self.assertNotIn("FACT-0000", ranking_encoded)
        self.assertLess(len(ranking_encoded), 100_000)

        failures = tuple(
            {
                "failure_stage": "SEARCH",
                "failure_reason": f"FAILURE-{index % 3}",
                "objective_id": f"OBJ-{index % 7}",
                "query_id": f"QUERY-{index % 19}",
                "alternate_route_required": index % 2 == 0,
                "url": f"https://example.com/{index}",
            }
            for index in range(1_500)
        )
        failure_projection = project_query_planner_failures(failures)
        self.assertEqual(
            failure_projection,
            project_query_planner_failures(tuple(reversed(failures))),
        )
        self.assertEqual(failure_projection["failure_count"], 1_500)
        self.assertEqual(failure_projection["failure_group_count"], 6)
        self.assertTrue(
            failure_projection[
                "every_semantic_failure_accounted_by_group_count_and_hash"
            ]
        )
        gap_projection = project_query_score_gap_context(
            {
                "prior_fact_extraction_feedback": [
                    f"MISSING_FACT:{index}" for index in range(1_000)
                ],
                "prior_supervisor_gap": {
                    "missing_material_facts": ["공식 연간 가이던스"],
                    "unresolved_material_questions": ["현금 전환 귀속"],
                    "failure_assessments": list(failures),
                    "parser_or_extractor_failures": [
                        f"PARSER-{index}" for index in range(1_000)
                    ],
                },
            }
        )
        self.assertEqual(
            gap_projection["prior_fact_extraction_feedback"]["feedback_count"],
            1_000,
        )
        self.assertEqual(
            gap_projection["prior_supervisor_gap"][
                "failure_assessment_projection"
            ]["failure_count"],
            1_500,
        )
        self.assertEqual(
            gap_projection["prior_supervisor_gap"][
                "missing_material_facts"
            ],
            ["공식 연간 가이던스"],
        )
        self.assertLess(
            len(
                json.dumps(
                    {
                        "failures": failure_projection,
                        "gap": gap_projection,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            ),
            100_000,
        )

        checkpoint = {
            "checkpoint_id": "CHECKPOINT",
            "epoch": 200,
            "generated_queries": [
                {
                    "query_id": f"QUERY-{index:04d}",
                    "objective_id": f"OBJECTIVE-{index % 7}",
                    "literal_query": f"현재 회사 원문 탐색 {index} " + "검색어 " * 20,
                    "rationale": f"미충족 경제 사실 탐색 {index}",
                    "source_families": ["ISSUER_PRESENTATION"],
                    "execution_status": "SEARCH_EXECUTED",
                    "search_result_count": 100,
                    "counter_or_supersession_search": index % 2 == 0,
                }
                for index in range(1_000)
            ],
            "search_candidates": [
                {
                    "candidate_id": f"CANDIDATE-{index:04d}",
                    "url": f"https://issuer.example/{index}",
                    "title": f"공식 자료 {index}",
                    "snippet": "발견 메타데이터 " * 20,
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                    "candidate_source_family_hint": "ISSUER_PRESENTATION",
                    "verified_official_domain_candidate": True,
                    "objective_ids": [f"OBJECTIVE-{index % 7}"],
                    "requested_source_families": ["ISSUER_PRESENTATION"],
                    "material_priority": 0.9,
                }
                for index in range(1_000)
            ],
            "evidence_documents": [
                {
                    "document_id": f"DOC-{index:04d}",
                    "canonical_url": f"https://issuer.example/{index}.pdf",
                    "content_hash": hashlib.sha256(str(index).encode()).hexdigest(),
                    "source_family": "ISSUER_PRESENTATION",
                    "source_provider": "PageFetcher",
                    "publication_date_source": "HTTP_LAST_MODIFIED",
                    "published_at": "2026-07-10",
                    "full_fetch_performed": True,
                    "snippet_only": False,
                    "evidence_eligible": True,
                    "objective_ids": [f"OBJECTIVE-{index % 7}"],
                    "query_ids": [f"QUERY-{index:04d}"],
                    "source_independence_group": "ISSUER_PRESENTATION:issuer.example",
                    "verified_official_discovery_urls": [
                        f"https://issuer.example/{index}.pdf"
                    ],
                }
                for index in range(1_000)
            ],
            "transport_budget_can_complete_research": False,
            "semantic_saturation_certified": False,
        }
        supervisor_source = project_supervisor_source_graph_checkpoint(checkpoint)
        source_encoded = json.dumps(
            supervisor_source, ensure_ascii=False, sort_keys=True
        )
        self.assertEqual(
            supervisor_source["generated_queries"]["record_count"], 1_000
        )
        self.assertEqual(
            supervisor_source["search_candidates"]["record_count"], 1_000
        )
        self.assertEqual(
            supervisor_source["evidence_documents"]["record_count"], 1_000
        )
        self.assertNotIn("checkpoint_id", supervisor_source)
        self.assertNotIn("epoch", supervisor_source)
        self.assertTrue(
            supervisor_source["source_graph_prompt_projection"][
                "checkpoint_lineage_excluded_from_provider"
            ]
        )
        self.assertLess(len(source_encoded), 250_000)
        self.assertNotIn("현재 회사 원문 탐색 999", source_encoded)
        self.assertNotIn("https://issuer.example/999.pdf", source_encoded)

    def test_supervisor_source_graph_projection_ignores_checkpoint_lineage(self):
        document = {
            "document_id": "DOC-1",
            "full_source_document_id": "DOC-1",
            "target_id": "CURRENT-TARGET",
            "as_of_date": "2026-07-12",
            "canonical_url": "https://issuer.example/current.pdf",
            "title": "현재 발행사 원문",
            "source_family": "ISSUER_PRESENTATION",
            "source_provider": "FULL_FETCH",
            "publication_date_source": "DOCUMENT_METADATA",
            "published_at": "2026-06-20",
            "available_at": "2026-06-20",
            "content_type": "application/pdf",
            "content_hash": "a" * 64,
            "full_source_content_hash": "a" * 64,
            "full_source_text_chars": 1_000,
            "chunk_index": 0,
            "chunk_count": 1,
            "all_chunks_preserved": True,
            "source_independence_group": "ISSUER:issuer.example",
            "full_fetch_performed": True,
            "full_source_fetch_performed": True,
            "snippet_only": False,
            "snippet_used_as_document": False,
            "evidence_eligible": True,
            "query_ids": ["QUERY-1"],
            "objective_ids": ["OBJECTIVE-1"],
            "discovery_urls": ["https://search.example/first"],
            "verified_official_discovery_urls": [
                "https://official.example/first"
            ],
        }
        checkpoint = {
            "checkpoint_id": "CHECKPOINT-1",
            "epoch": 1,
            "generated_queries": [],
            "search_candidates": [],
            "candidate_materiality_decisions": [],
            "fetch_records": [],
            "rejected_documents": [],
            "query_failures": [],
            "provider_failures": [],
            "evidence_documents": [document],
            "quarantined_documents": [],
            "resolved_objective_ids": [],
            "transport_budget_can_complete_research": False,
            "semantic_saturation_certified": False,
        }
        resumed = {
            **checkpoint,
            "checkpoint_id": "CHECKPOINT-999",
            "epoch": 999,
            "evidence_documents": [
                {
                    **document,
                    "query_ids": ["QUERY-1", "QUERY-999"],
                    "objective_ids": ["OBJECTIVE-1", "OBJECTIVE-999"],
                    "discovery_urls": ["https://search.example/resumed"],
                    "verified_official_discovery_urls": [
                        "https://official.example/resumed"
                    ],
                }
            ],
        }
        self.assertEqual(
            project_supervisor_source_graph_checkpoint(checkpoint),
            project_supervisor_source_graph_checkpoint(resumed),
        )
        changed_content = {
            **resumed,
            "evidence_documents": [
                {
                    **resumed["evidence_documents"][0],
                    "content_hash": "b" * 64,
                    "full_source_content_hash": "b" * 64,
                }
            ],
        }
        self.assertNotEqual(
            project_supervisor_source_graph_checkpoint(checkpoint),
            project_supervisor_source_graph_checkpoint(changed_content),
        )

    def test_supervisor_quarantine_projection_accounts_unbounded_rows(self):
        checkpoint = {
            "generated_queries": [],
            "search_candidates": [],
            "candidate_materiality_decisions": [],
            "fetch_records": [],
            "rejected_documents": [],
            "query_failures": [],
            "provider_failures": [],
            "evidence_documents": [],
            "quarantined_documents": [
                {
                    "document_id": f"DOC-{index:05d}",
                    "candidate_id": f"CAND-{index:05d}",
                    "query_ids": [f"QUERY-{index:05d}"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "url": (
                        f"https://issuer.example/{index}/"
                        + "very-long-discovery-path/" * 100
                    ),
                    "content_hash": f"{index:064x}",
                    "quarantine_reason": (
                        "UNREADABLE_FULL_DOCUMENT_TEXT:"
                        + "connector detail " * 100
                    ),
                    "parser_refetch_required": True,
                    "evidence_eligible": False,
                    "score_authority": False,
                }
                for index in range(1_000)
            ],
            "resolved_objective_ids": [],
            "transport_budget_can_complete_research": False,
            "semantic_saturation_certified": False,
        }

        projected = project_supervisor_source_graph_checkpoint(checkpoint)
        quarantine = projected["quarantined_documents"]
        encoded = json.dumps(projected, ensure_ascii=False, sort_keys=True)
        self.assertEqual(quarantine["record_count"], 1_000)
        self.assertTrue(
            quarantine["every_quarantine_accounted_by_hash_and_group_count"]
        )
        self.assertEqual(quarantine["document_id_roster"]["count"], 1_000)
        self.assertNotIn("very-long-discovery-path", encoded)
        self.assertNotIn("connector detail", encoded)
        self.assertLess(len(encoded), 20_000)

    def test_query_gap_projection_ignores_checkpoint_lineage(self):
        context = {
            "prior_research_epoch": {
                "checkpoint_id": "REPOCH-1",
                "epoch": 1,
                "status": "NEXT_RESEARCH_REQUIRED",
                "unresolved_material_questions": ["제품별 현금 전환"],
                "next_actions": ["새 원천을 탐색한다"],
            },
            "prior_supervisor_gap": {
                "review_id": "REVIEW-1",
                "supervisor_review_id": "REVIEW-1",
                "epoch": 1,
                "status": "NEXT_RESEARCH_REQUIRED",
                "missing_material_facts": ["제품별 FCF"],
                "failure_assessments": [],
                "parser_or_extractor_failures": [],
            },
        }
        resumed = {
            **context,
            "prior_research_epoch": {
                **context["prior_research_epoch"],
                "checkpoint_id": "REPOCH-999",
                "epoch": 999,
            },
            "prior_supervisor_gap": {
                **context["prior_supervisor_gap"],
                "review_id": "REVIEW-999",
                "supervisor_review_id": "REVIEW-999",
                "epoch": 999,
            },
        }
        first = project_query_score_gap_context(context)
        second = project_query_score_gap_context(resumed)
        self.assertEqual(first, second)
        self.assertNotIn("checkpoint_id", first["prior_research_epoch"])
        self.assertNotIn("epoch", first["prior_research_epoch"])
        self.assertNotIn("review_id", first["prior_supervisor_gap"])
        self.assertNotIn("supervisor_review_id", first["prior_supervisor_gap"])
        self.assertNotIn("epoch", first["prior_supervisor_gap"])
        self.assertTrue(
            first["query_score_gap_projection_audit"][
                "checkpoint_lineage_excluded_from_provider"
            ]
        )

    def test_query_prompt_projection_ignores_only_collaboration_transport_waits(
        self,
    ):
        request_a = "COLLABREQ-" + "a" * 64
        request_b = "COLLABREQ-" + "b" * 64
        real_failure = {
            "failure_id": "FAILURE-REAL",
            "failure_stage": "FULL_DOCUMENT_FETCH",
            "failure_reason": "FETCH_TIMEOUT",
            "objective_id": "OBJECTIVE-1",
            "query_id": "QUERY-1",
        }
        wait_failure_a = {
            "failure_reason": (
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_a
            ),
            "objective_id": "MULTI_OBJECTIVE",
            "query_id": "QUERY_GENERATION",
        }
        wait_failure_b = {
            "failure_reason": (
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_b
            ),
            "objective_id": "MULTI_OBJECTIVE",
            "query_id": "QUERY_GENERATION",
        }

        first_failures = project_query_planner_failures(
            (real_failure, wait_failure_a)
        )
        repeated_wait_failures = project_query_planner_failures(
            (
                real_failure,
                wait_failure_a,
                wait_failure_b,
                wait_failure_b,
            )
        )
        self.assertEqual(first_failures, repeated_wait_failures)
        self.assertEqual(first_failures["failure_count"], 1)
        self.assertTrue(
            first_failures[
                "collaboration_transport_waits_excluded_from_semantic_prompt"
            ]
        )

        context_a = {
            "source_graph_pending_reasons": [
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_a,
                "REFERENCE_DISCOVERY_TRANSPORT_BUDGET_CHECKPOINT:2",
            ],
            "prior_fact_extraction_feedback": [
                "UNRESOLVED_RESEARCH_NOTE:peer band source가 필요하다.",
                (
                    "FACT_EXTRACTION_RETRY_CONTEXT:"
                    "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                    "StructuredProviderUnavailable:"
                    "COLLABORATION_RESPONSE_PENDING:"
                    + request_a
                ),
            ],
            "prior_supervisor_gap": {
                "unresolved_material_questions": [
                    (
                        "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        "COLLABORATION_RESPONSE_PENDING:"
                        + request_a
                    ),
                    "PEER_BAND를 확인해야 한다.",
                ],
            },
            "prior_research_epoch": {
                "unresolved_material_questions": [
                    (
                        "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        "COLLABORATION_RESPONSE_PENDING:"
                        + request_a
                    ),
                    "PEER_BAND를 확인해야 한다.",
                ],
            },
        }
        context_b = {
            **context_a,
            "source_graph_pending_reasons": [
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_b,
                "REFERENCE_DISCOVERY_TRANSPORT_BUDGET_CHECKPOINT:2",
            ],
            "prior_fact_extraction_feedback": [
                "UNRESOLVED_RESEARCH_NOTE:peer band source가 필요하다.",
                (
                    "FACT_EXTRACTION_RETRY_CONTEXT:"
                    "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                    "StructuredProviderUnavailable:"
                    "COLLABORATION_RESPONSE_PENDING:"
                    + request_b
                ),
            ],
            "prior_supervisor_gap": {
                "unresolved_material_questions": [
                    (
                        "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        "COLLABORATION_RESPONSE_PENDING:"
                        + request_b
                    ),
                    "PEER_BAND를 확인해야 한다.",
                ],
            },
            "prior_research_epoch": {
                "unresolved_material_questions": [
                    (
                        "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        "COLLABORATION_RESPONSE_PENDING:"
                        + request_b
                    ),
                    "PEER_BAND를 확인해야 한다.",
                ],
            },
        }
        self.assertEqual(
            project_query_score_gap_context(context_a),
            project_query_score_gap_context(context_b),
        )

        changed_real_failure = {
            **real_failure,
            "failure_reason": "HTTP_503",
        }
        self.assertNotEqual(
            first_failures,
            project_query_planner_failures(
                (changed_real_failure, wait_failure_a)
            ),
        )
        mixed_failure = {
            **real_failure,
            "provider_error": (
                "COLLABORATION_RESPONSE_PENDING:" + request_a
            ),
        }
        mixed_projection = project_query_planner_failures((mixed_failure,))
        self.assertEqual(mixed_projection["failure_count"], 1)
        self.assertEqual(
            mixed_projection["failures"][0]["failure_reason"],
            "FETCH_TIMEOUT",
        )
        suffixed_real_error = {
            "failure_reason": (
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_a
                + ":HTTP_503"
            ),
            "objective_id": "OBJECTIVE-1",
        }
        suffixed_projection = project_query_planner_failures(
            (suffixed_real_error,)
        )
        self.assertEqual(suffixed_projection["failure_count"], 1)
        self.assertEqual(
            suffixed_projection["failures"][0]["failure_reason"],
            "QUERY_PROVIDER_ERROR",
        )

    def test_fact_transport_chunk_progress_does_not_change_semantic_prompt(self):
        base_feedback = [
            "UNRESOLVED_RESEARCH_NOTE:peer band source가 필요하다.",
            "FACT_EXTRACTION_RETRY_CONTEXT:UNREADABLE_FULL_DOCUMENT:SGDOC-deadbeef",
        ]
        first = project_query_score_gap_context(
            {
                "prior_fact_extraction_feedback": [
                    *base_feedback,
                    (
                        "FACT_EXTRACTION_RETRY_CONTEXT:"
                        "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                        "SGDOC-2ef3c663d8923972cecc7372:0/3"
                    ),
                ]
            }
        )
        resumed = project_query_score_gap_context(
            {
                "prior_fact_extraction_feedback": [
                    *base_feedback,
                    (
                        "FACT_EXTRACTION_RETRY_CONTEXT:"
                        "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                        "SGDOC-2ef3c663d8923972cecc7372:1/3"
                    ),
                ]
            }
        )
        canonical_refresh = project_query_score_gap_context(
            {
                "prior_fact_extraction_feedback": [
                    *base_feedback,
                    (
                        "FACT_EXTRACTION_RETRY_CONTEXT:"
                        "FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED"
                    ),
                ]
            }
        )

        self.assertEqual(first, resumed)
        self.assertEqual(first, canonical_refresh)
        self.assertEqual(
            project_fact_extraction_score_gap_context(
                {
                    "prior_fact_extraction_feedback": [
                        *base_feedback,
                        (
                            "FACT_EXTRACTION_RETRY_CONTEXT:"
                            "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                            "SGDOC-2ef3c663d8923972cecc7372:0/3"
                        ),
                    ]
                }
            ),
            project_fact_extraction_score_gap_context(
                {
                    "prior_fact_extraction_feedback": [
                        *base_feedback,
                        (
                            "FACT_EXTRACTION_RETRY_CONTEXT:"
                            "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                            "SGDOC-2ef3c663d8923972cecc7372:1/3"
                        ),
                    ]
                }
            ),
        )
        feedback_projection = first["prior_fact_extraction_feedback"]
        self.assertEqual(
            feedback_projection["schema_version"],
            "e2r_v5_fact_gap_feedback_projection_v3",
        )
        self.assertEqual(feedback_projection["feedback_count"], 2)
        self.assertTrue(
            feedback_projection[
                "fact_transport_progress_excluded_from_semantic_prompt"
            ]
        )
        self.assertTrue(
            feedback_projection[
                "fact_transport_progress_persisted_in_fact_checkpoint"
            ]
        )

    def test_fact_transport_progress_filter_preserves_semantic_or_malformed_rows(
        self,
    ):
        baseline = project_query_score_gap_context(
            {"prior_fact_extraction_feedback": []}
        )
        for semantic_row in (
            (
                "FACT_EXTRACTION_RETRY_CONTEXT:"
                "UNREADABLE_FULL_DOCUMENT:SGDOC-deadbeef"
            ),
            (
                "FACT_EXTRACTION_RETRY_CONTEXT:"
                "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                "SGDOC-deadbeef:1/3:SOURCE_ERROR"
            ),
            (
                "FACT_EXTRACTION_RETRY_CONTEXT:"
                "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                "OTHERDOC-deadbeef:3/3"
            ),
            (
                "FACT_EXTRACTION_RETRY_CONTEXT:"
                "FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED:EXTRA"
            ),
        ):
            with self.subTest(semantic_row=semantic_row):
                projected = project_query_score_gap_context(
                    {"prior_fact_extraction_feedback": [semantic_row]}
                )
                self.assertNotEqual(projected, baseline)
                self.assertEqual(
                    projected["prior_fact_extraction_feedback"][
                        "feedback_count"
                    ],
                    1,
                )

    def test_research_source_profiles_ignore_transport_lineage_only_churn(self):
        claim = {
            "claim_id": "CLAIM-1",
            "document_id": "DOC-1",
            "source_ids": ["SOURCE-1"],
            "exact_quote": "현재 원문에 확인된 경제 사실",
            "source_family": "ISSUER_PRESENTATION",
            "source_tier": "TIER1",
            "published_at": "2026-06-20",
            "available_at": "2026-06-20",
            "structured_evidence_roles": ["FORWARD_GUIDANCE"],
            "provider_prompt_hash": "PROMPT-1",
            "provider_response_hash": "RESPONSE-1",
            "materiality_rationale": "첫 추출 설명",
        }
        reextracted_claim = {
            **claim,
            "provider_prompt_hash": "PROMPT-999",
            "provider_response_hash": "RESPONSE-999",
            "materiality_rationale": "재추출 설명",
        }
        self.assertEqual(
            project_research_source_claim_profile((claim,)),
            project_research_source_claim_profile((reextracted_claim,)),
        )
        changed_quote = {
            **reextracted_claim,
            "exact_quote": "경제적으로 다른 원문 사실",
        }
        self.assertNotEqual(
            project_research_source_claim_profile((claim,)),
            project_research_source_claim_profile((changed_quote,)),
        )

        document = {
            "document_id": "DOC-1",
            "full_source_document_id": "DOC-1",
            "target_id": "CURRENT-TARGET",
            "as_of_date": "2026-06-29",
            "canonical_url": "https://issuer.example/current.pdf",
            "title": "현재 발행사 원문",
            "source_family": "ISSUER_PRESENTATION",
            "source_provider": "FULL_FETCH",
            "published_at": "2026-06-20",
            "available_at": "2026-06-20",
            "content_type": "application/pdf",
            "content_hash": "a" * 64,
            "full_source_content_hash": "a" * 64,
            "full_source_text_chars": 1_000,
            "chunk_index": 0,
            "chunk_count": 1,
            "all_chunks_preserved": True,
            "source_independence_group": "ISSUER:issuer.example",
            "full_fetch_performed": True,
            "full_source_fetch_performed": True,
            "snippet_only": False,
            "snippet_used_as_document": False,
            "evidence_eligible": True,
            "query_ids": ["QUERY-1"],
            "objective_ids": ["OBJECTIVE-1"],
            "discovery_urls": ["https://search.example/first"],
            "referenced_urls": ["https://issuer.example/reference-1"],
            "fetched_at": "2026-06-21T00:00:00",
        }
        rediscovered_document = {
            **document,
            "query_ids": ["QUERY-1", "QUERY-999"],
            "objective_ids": ["OBJECTIVE-1", "OBJECTIVE-999"],
            "discovery_urls": [
                "https://search.example/first",
                "https://search.example/resumed",
            ],
            "referenced_urls": ["https://issuer.example/reference-999"],
            "fetched_at": "2026-06-29T00:00:00",
        }
        self.assertEqual(
            project_research_source_document_profile((document,)),
            project_research_source_document_profile((rediscovered_document,)),
        )
        changed_content = {
            **rediscovered_document,
            "content_hash": "b" * 64,
            "full_source_content_hash": "b" * 64,
        }
        self.assertNotEqual(
            project_research_source_document_profile((document,)),
            project_research_source_document_profile((changed_content,)),
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
        self.assertEqual(projected["documents"]["record_count"], 10)
        self.assertEqual(projected["new_facts"]["record_count"], 1)
        self.assertTrue(
            projected["documents"][
                "every_record_accounted_by_exact_count_and_full_hash"
            ]
        )
        self.assertNotIn(text, json.dumps(projected, ensure_ascii=False))
        self.assertNotIn("gold_critical_fact_miss_count", projected)
        self.assertFalse(
            projected["research_epoch_prompt_projection"]["fixed_top_n_used"]
        )
        self.assertLess(len(json.dumps(projected, sort_keys=True)), 30_000)


if __name__ == "__main__":
    unittest.main()
