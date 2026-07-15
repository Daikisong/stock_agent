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
    project_generated_queries,
    project_peer_selection_context,
    project_query_planner_failures,
    project_query_score_gap_context,
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
        self.assertTrue(
            all(
                group["relation_coverage"]["predicate"]
                for group in supervisor_facts["semantic_groups"]
            )
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
        self.assertLess(len(supervisor_encoded), 250_000)
        self.assertLess(len(peer_encoded), 250_000)
        self.assertNotIn("검증된 경제 메커니즘 999", supervisor_encoded)
        self.assertNotIn("원문 인용 999", peer_encoded)

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
                "every_failure_accounted_by_group_count_and_hash"
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
        self.assertLess(len(source_encoded), 250_000)
        self.assertNotIn("현재 회사 원문 탐색 999", source_encoded)
        self.assertNotIn("https://issuer.example/999.pdf", source_encoded)

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
