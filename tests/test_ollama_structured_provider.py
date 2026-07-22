from __future__ import annotations

import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

from e2r.cli.run_e2r_researcher_mode_until_pass import (
    _build_research_provider,
    _research_provider_manifest,
    build_parser,
)
from e2r.research_brain.planning.provider_transport import (
    OllamaStructuredProviderTransport,
    StructuredProviderRejected,
    StructuredProviderResponse,
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode import (
    CodexResearcherProvider,
    CurrentResearcherModeTargetRunner,
    OllamaResearcherProvider,
)
from e2r.research_brain.researcher_mode.component_researcher import (
    CANDIDATE_RANKING_PAGE_CANDIDATE_LIMIT,
    SOURCE_CANDIDATE_RANKING_SCHEMA,
    _canonicalize_ollama_red_team_fact_set,
    _expected_component_chunk_fact_groundings,
    _loss_accounted_fact_chunk_payloads,
    _provider_output_schema,
    _validate_loss_accounted_chunk_response,
)
from e2r.research_brain.researcher_mode.prompt_projection import (
    project_current_decision_citable_facts,
)


class _FakeHTTPResponse:
    def __init__(self, value=None, *, raw=None, headers=None):
        self.value = value
        self.raw = raw
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self, limit=None):
        raw = self.raw
        if raw is None:
            raw = json.dumps(self.value, ensure_ascii=False).encode("utf-8")
        return raw if limit is None else raw[:limit]


class OllamaStructuredProviderTests(unittest.TestCase):
    def test_long_fact_plane_is_reviewed_in_disjoint_loss_accounted_chunks(
        self,
    ) -> None:
        class ChunkAwareTransport:
            context_length = 65_536
            max_output_tokens = 32_768

            def __init__(self):
                self.payloads = []
                self.output_schemas = []
                self.prompt_lengths = []

            def provider_identity(self):
                return {
                    "transport_class": "ChunkAwareTransport",
                    "model": "test-model",
                    "context_length": 262_144,
                }

            def complete(self, *, prompt, output_schema, schema_name):
                del schema_name
                payload = json.loads(prompt.rsplit("\n", 1)[-1])
                self.payloads.append(payload)
                self.output_schemas.append(output_schema)
                self.prompt_lengths.append(len(prompt))
                chunk = payload.get("loss_accounted_fact_chunk")
                if chunk:
                    row_index = payload["current_evidence_fact_graph"][0][
                        "fact_row_index"
                    ]
                    response = {
                        "business_model_summary": (
                            f"chunk {chunk['chunk_index']} mechanism review"
                        ),
                        "revenue_engines": ["chunk revenue mechanism"],
                        "cost_and_cash_drivers": ["chunk cash mechanism"],
                        "capacity_and_supply_constraints": [
                            "chunk capacity mechanism"
                        ],
                        "customer_and_channel_dependencies": [
                            "chunk customer mechanism"
                        ],
                        "fact_row_indices": [row_index],
                        "uncertainties": ["chunk uncertainty"],
                        "confidence": 0.7,
                        "research_complete": True,
                    }
                else:
                    partials = payload[
                        "loss_accounted_fact_chunk_synthesis"
                    ]["chunk_responses"]
                    response = {
                        "business_model_summary": "all chunks synthesized",
                        "revenue_engines": ["all revenue mechanisms"],
                        "cost_and_cash_drivers": ["all cash mechanisms"],
                        "capacity_and_supply_constraints": [
                            "all capacity mechanisms"
                        ],
                        "customer_and_channel_dependencies": [
                            "all customer mechanisms"
                        ],
                        "fact_row_indices": [
                            row["response"]["fact_row_indices"][0]
                            for row in partials
                        ],
                        "uncertainties": ["cross-chunk uncertainty"],
                        "confidence": 0.8,
                        "research_complete": True,
                    }
                return StructuredProviderResponse(
                    payload=response,
                    raw_response=json.dumps(response),
                    stderr="",
                    returncode=0,
                )

        facts = [
            {
                "fact_id": f"EFACT-{index:04d}",
                "target_id": "TEST",
                "as_of_date": "2026-06-29",
                "subject": "target memory business",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "economic_mechanism": (
                    f"fact {index} " + "긴 경제 메커니즘 " * 500
                ),
                "predicate": f"CURRENT_HBM_MECHANISM_{index}",
                "value": index,
                "unit": "units",
                "period": "2026-06-29",
                "direction": "POSITIVE" if index % 2 == 0 else "COUNTER",
                "current_lifecycle": "CURRENT",
                "confidence": 0.9,
                "structured_evidence_roles": [],
                "claim_ids": [f"CLAIM-{index:04d}"],
                "source_ids": [f"DOC-{index:04d}"],
                "source_independence_group": "issuer:test",
                "corroborating_independence_groups": ["issuer:test"],
                "allowed_component_ids": [],
                "question_family_tags": [],
                "primitive_tags": [],
            }
            for index in range(24)
        ]
        projection = project_current_decision_citable_facts(facts)
        payload = {
            "researcher_role": "BusinessMechanismResearcher",
            "target_id": "TEST",
            "archetype_id": "TEST_ARCHETYPE",
            "as_of_date": "2026-06-29",
            "current_evidence_fact_graph": projection["facts"],
            "current_evidence_fact_projection": {
                key: value
                for key, value in projection.items()
                if key not in {"facts", "fact_id_by_row_index"}
            },
            "source_claims": {},
            "source_documents": {},
            "source_coverage": ["ISSUER"],
        }
        transport = ChunkAwareTransport()
        provider = OllamaResearcherProvider(
            transport=transport,
            fact_document_chunk_chars=10_000,
        )

        response = provider.complete(
            pass_name="BUSINESS_MODEL_RESEARCH",
            payload=payload,
        )

        chunk_payloads = [
            row for row in transport.payloads if row.get("loss_accounted_fact_chunk")
        ]
        self.assertGreater(len(chunk_payloads), 1)
        self.assertLessEqual(len(chunk_payloads), 3)
        self.assertEqual(provider.memo_fact_prompt_chunk_chars, 100_000)
        emitted = [
            global_index
            for chunk in chunk_payloads
            for global_index in chunk["loss_accounted_fact_chunk"][
                "global_fact_row_index_by_chunk_local_index"
            ]
        ]
        self.assertEqual(emitted, list(range(len(facts))))
        self.assertEqual(len(emitted), len(set(emitted)))
        self.assertTrue(
            all(
                len(
                    json.dumps(
                        chunk["current_evidence_fact_projection"],
                        ensure_ascii=False,
                    )
                )
                < 150_000
                for chunk in chunk_payloads
            )
        )
        self.assertEqual(
            set(response["fact_row_indices"]),
            {
                chunk["loss_accounted_fact_chunk"][
                    "global_fact_row_index_by_chunk_local_index"
                ][0]
                for chunk in chunk_payloads
            },
        )
        self.assertTrue(
            transport.payloads[-1].get(
                "loss_accounted_fact_chunk_synthesis"
            )
        )
        self.assertTrue(all(length < 500_000 for length in transport.prompt_lengths))

    def test_fact_chunk_dictionary_remap_preserves_every_decoded_value(
        self,
    ) -> None:
        facts = [
            {
                "fact_id": f"EFACT-{index}",
                "target_id": "TEST",
                "as_of_date": "2026-06-29",
                "subject": f"subject {index}",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "economic_mechanism": f"mechanism {index} " + "x" * 4000,
                "predicate": f"predicate_{index}",
                "value": {"value": index},
                "unit": "units",
                "period": f"2026-Q{index + 1}",
                "direction": "POSITIVE",
                "current_lifecycle": "CURRENT",
                "confidence": 0.8,
                "structured_evidence_roles": [],
                "claim_ids": [f"CLAIM-{index}"],
                "source_ids": [f"DOC-{index}"],
                "source_independence_group": "issuer:test",
                "corroborating_independence_groups": ["issuer:test"],
                "allowed_component_ids": [],
                "question_family_tags": [],
                "primitive_tags": [],
            }
            for index in range(4)
        ]
        projection = project_current_decision_citable_facts(facts)
        payload = {
            "current_evidence_fact_graph": projection["facts"],
            "current_evidence_fact_projection": {
                key: value
                for key, value in projection.items()
                if key not in {"facts", "fact_id_by_row_index"}
            },
            "business_model_validation_retry_context": {
                "validation_error": "final synthesis citation correction"
            },
            "prior_component_memo_context": {
                "available": True,
                "current_fact_rows": [],
                "current_fact_row_count": 0,
                "unavailable_prior_fact_count": 3,
                "unavailable_prior_fact_roster_hash": "a" * 64,
            },
        }
        chunks = _loss_accounted_fact_chunk_payloads(
            payload,
            pass_name="BUSINESS_MODEL_RESEARCH",
            target_projection_chars=10_000,
        )
        self.assertGreater(len(chunks), 1)
        self.assertTrue(
            all(
                "business_model_validation_retry_context" not in chunk
                for chunk in chunks
            )
        )
        original_by_row = {
            row[0]: row for row in projection["facts"]
        }
        fields = projection["fact_fields"]
        for chunk in chunks:
            prior_context = chunk["prior_component_memo_context"]
            self.assertFalse(prior_context["available"])
            self.assertFalse(
                prior_context["prior_fact_dispositions_required"]
            )
            self.assertEqual(
                prior_context["required_prior_fact_disposition_count"], 0
            )
            self.assertTrue(
                prior_context[
                    "unavailable_prior_facts_are_hash_only_not_dispositions"
                ]
            )
            local_projection = chunk["current_evidence_fact_projection"]
            local_dictionaries = local_projection["fact_value_dictionaries"]
            self.assertEqual(
                local_projection["chunk_fact_row_encoding"],
                {
                    "schema_version": "e2r_v5_named_fact_row_encoding_v1",
                    "fact_row_index_field": "fact_row_index",
                    "encoded_fact_values_field": "encoded_fact_values",
                    "encoded_fact_value_fields": fields[1:],
                    "citation_cell_is_not_part_of_encoded_fact_values": True,
                },
            )
            local_to_global = chunk["loss_accounted_fact_chunk"][
                "global_fact_row_index_by_chunk_local_index"
            ]
            for local_row in chunk["current_evidence_fact_graph"]:
                self.assertEqual(
                    set(local_row),
                    {"fact_row_index", "encoded_fact_values"},
                )
                local_index = local_row["fact_row_index"]
                original = original_by_row[local_to_global[local_index]]
                for position, field in enumerate(fields[1:], start=1):
                    name = field[: -len("_dictionary_index")]
                    self.assertEqual(
                        local_dictionaries[name][
                            local_row["encoded_fact_values"][position - 1]
                        ],
                        projection["fact_value_dictionaries"][name][
                            original[position]
                        ],
                    )

    def test_component_chunk_rejects_semantics_copied_from_another_row(
        self,
    ) -> None:
        facts = [
            {
                "fact_id": f"EFACT-{index}",
                "target_id": "TEST",
                "as_of_date": "2026-06-29",
                "subject": "target memory business",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "economic_mechanism": (
                    f"immutable mechanism {index} " + "x" * 40_000
                ),
                "predicate": f"IMMUTABLE_PREDICATE_{index}",
                "value": {"point": index},
                "unit": "units",
                "period": f"2026-Q{index + 1}",
                "direction": "POSITIVE",
                "current_lifecycle": "CURRENT",
                "confidence": 0.8,
                "structured_evidence_roles": [],
                "claim_ids": [f"CLAIM-{index}"],
                "source_ids": [f"DOC-{index}"],
                "source_independence_group": "issuer:test",
                "corroborating_independence_groups": ["issuer:test"],
                "allowed_component_ids": [],
                "question_family_tags": [],
                "primitive_tags": [],
            }
            for index in range(4)
        ]
        projection = project_current_decision_citable_facts(facts)
        chunks = _loss_accounted_fact_chunk_payloads(
            {
                "current_evidence_fact_graph": projection["facts"],
                "current_evidence_fact_projection": {
                    key: value
                    for key, value in projection.items()
                    if key not in {"facts", "fact_id_by_row_index"}
                },
            },
            pass_name="COMPONENT_RESEARCH",
            target_projection_chars=100_000,
        )
        self.assertGreater(len(chunks), 1)
        expected = _expected_component_chunk_fact_groundings(chunks[0])
        selected_index = min(expected)
        other_index = next(index for index in expected if index != selected_index)
        copied_from_other_row = {
            "fact_row_index": selected_index,
            **expected[other_index],
            "component_interpretation": "wrong row semantics",
        }
        response = {
            "selected_fact_row_indices": [selected_index],
            "selected_fact_groundings": [copied_from_other_row],
            "prior_fact_dispositions": [],
        }

        with self.assertRaisesRegex(
            StructuredProviderRejected,
            "loss_accounted_fact_chunk_grounding_source_predicate_mismatch",
        ):
            _validate_loss_accounted_chunk_response(
                pass_name="COMPONENT_RESEARCH",
                response=response,
                allowed_fact_row_indices=set(expected),
                prior_fact_row_indices=set(),
                expected_component_groundings=expected,
            )

        response["selected_fact_groundings"] = [
            {
                "fact_row_index": selected_index,
                **expected[selected_index],
                "component_interpretation": "correct row semantics",
            }
        ]
        _validate_loss_accounted_chunk_response(
            pass_name="COMPONENT_RESEARCH",
            response=response,
            allowed_fact_row_indices=set(expected),
            prior_fact_row_indices=set(),
            expected_component_groundings=expected,
        )

    def test_component_chunk_retry_omits_rejected_semantic_binding(
        self,
    ) -> None:
        class SemanticRetryTransport:
            context_length = 65_536
            max_output_tokens = 32_768

            def __init__(self):
                self.payloads = []
                self.output_schemas = []

            def provider_identity(self):
                return {
                    "transport_class": "SemanticRetryTransport",
                    "model": "test-model",
                    "context_length": 65_536,
                }

            @staticmethod
            def component_response(*, grounding):
                row_index = grounding["fact_row_index"]
                return {
                    "researcher_summary": "component chunk review",
                    "positive_case": "source-backed positive case",
                    "counter_case": "bounded counter case",
                    "selected_fact_row_indices": [row_index],
                    "selected_fact_groundings": [grounding],
                    "structured_metric_row_indices": [],
                    "historical_anchor_ids": [],
                    "nearest_positive_anchor_ids": [],
                    "nearest_counter_anchor_ids": [],
                    "prior_fact_dispositions": [],
                    "proposed_score_lower": 0.0,
                    "proposed_score_mid": 0.0,
                    "proposed_score_upper": 0.0,
                    "why_not_higher": "bounded evidence",
                    "why_not_lower": "one current fact",
                    "source_coverage": ["ISSUER"],
                    "uncertainties": ["test uncertainty"],
                    "confidence": 0.7,
                    "research_complete": True,
                }

            @staticmethod
            def decoded_grounding(payload, row_index):
                projection = payload["current_evidence_fact_projection"]
                fields = projection["chunk_fact_row_encoding"][
                    "encoded_fact_value_fields"
                ]
                dictionaries = projection["fact_value_dictionaries"]
                row = next(
                    item
                    for item in payload["current_evidence_fact_graph"]
                    if item["fact_row_index"] == row_index
                )
                decoded = {
                    field[: -len("_dictionary_index")]: dictionaries[
                        field[: -len("_dictionary_index")]
                    ][dictionary_index]
                    for field, dictionary_index in zip(
                        fields, row["encoded_fact_values"]
                    )
                }
                return {
                    "fact_row_index": row_index,
                    "source_predicate": decoded["predicate"],
                    "source_value_json": json.dumps(
                        decoded["value"],
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                    "source_period_json": json.dumps(
                        decoded["period"],
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                    "source_economic_mechanism": decoded[
                        "economic_mechanism"
                    ],
                    "component_interpretation": "source-bound interpretation",
                }

            def complete(self, *, prompt, output_schema, schema_name):
                del schema_name
                payload = json.loads(prompt.rsplit("\n", 1)[-1])
                self.payloads.append(payload)
                self.output_schemas.append(output_schema)
                chunk = payload.get("loss_accounted_fact_chunk")
                if chunk:
                    retry = payload.get(
                        "loss_accounted_fact_chunk_validation_retry_context"
                    )
                    selected_index = payload["current_evidence_fact_graph"][0][
                        "fact_row_index"
                    ]
                    if retry:
                        grounding = {
                            **retry["expected_selected_fact_groundings"][0],
                            "component_interpretation": (
                                "fresh source-bound interpretation"
                            ),
                        }
                    elif chunk["chunk_index"] == 0:
                        other_index = payload["current_evidence_fact_graph"][1][
                            "fact_row_index"
                        ]
                        grounding = self.decoded_grounding(
                            payload, other_index
                        )
                        grounding["fact_row_index"] = selected_index
                    else:
                        grounding = self.decoded_grounding(
                            payload, selected_index
                        )
                    response = self.component_response(grounding=grounding)
                else:
                    partials = payload[
                        "loss_accounted_fact_chunk_synthesis"
                    ]["chunk_responses"]
                    groundings = [
                        grounding
                        for partial in partials
                        for grounding in partial["response"][
                            "selected_fact_groundings"
                        ]
                    ]
                    response = self.component_response(
                        grounding=groundings[0]
                    )
                    response["selected_fact_row_indices"] = [
                        row["fact_row_index"] for row in groundings
                    ]
                    response["selected_fact_groundings"] = groundings
                return StructuredProviderResponse(
                    payload=response,
                    raw_response=json.dumps(response),
                    stderr="",
                    returncode=0,
                )

        facts = [
            {
                "fact_id": f"EFACT-RETRY-{index}",
                "target_id": "TEST",
                "as_of_date": "2026-06-29",
                "subject": "target memory business",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "economic_mechanism": (
                    f"retry mechanism {index} " + "x" * 40_000
                ),
                "predicate": f"RETRY_PREDICATE_{index}",
                "value": {"point": index},
                "unit": "units",
                "period": f"2026-Q{index + 1}",
                "direction": "POSITIVE",
                "current_lifecycle": "CURRENT",
                "confidence": 0.8,
                "structured_evidence_roles": [],
                "claim_ids": [f"CLAIM-RETRY-{index}"],
                "source_ids": [f"DOC-RETRY-{index}"],
                "source_independence_group": "issuer:test",
                "corroborating_independence_groups": ["issuer:test"],
                "allowed_component_ids": [],
                "question_family_tags": [],
                "primitive_tags": [],
            }
            for index in range(4)
        ]
        projection = project_current_decision_citable_facts(facts)
        transport = SemanticRetryTransport()
        provider = OllamaResearcherProvider(transport=transport)
        response = provider.complete(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "current_evidence_fact_graph": projection["facts"],
                "current_evidence_fact_projection": {
                    key: value
                    for key, value in projection.items()
                    if key not in {"facts", "fact_id_by_row_index"}
                },
            },
        )

        retry_payloads = [
            row
            for row in transport.payloads
            if row.get("loss_accounted_fact_chunk_validation_retry_context")
        ]
        self.assertEqual(len(retry_payloads), 1)
        retry_context = retry_payloads[0][
            "loss_accounted_fact_chunk_validation_retry_context"
        ]
        self.assertNotIn("rejected_response", retry_context)
        base_chunk_payload, base_chunk_schema = next(
            (payload, schema)
            for payload, schema in zip(
                transport.payloads, transport.output_schemas
            )
            if payload.get("loss_accounted_fact_chunk")
            and not payload.get(
                "loss_accounted_fact_chunk_validation_retry_context"
            )
        )
        self.assertEqual(
            len(
                base_chunk_schema["properties"][
                    "selected_fact_groundings"
                ]["items"]["anyOf"]
            ),
            len(base_chunk_payload["current_evidence_fact_graph"]),
        )
        retry_schema = next(
            schema
            for payload, schema in zip(
                transport.payloads, transport.output_schemas
            )
            if payload.get(
                "loss_accounted_fact_chunk_validation_retry_context"
            )
        )
        grounding_variants = retry_schema["properties"][
            "selected_fact_groundings"
        ]["items"]["anyOf"]
        self.assertEqual(len(grounding_variants), 1)
        grounding_properties = grounding_variants[0]["properties"]
        self.assertEqual(
            grounding_properties["fact_row_index"]["enum"],
            [
                retry_context["expected_selected_fact_groundings"][0][
                    "fact_row_index"
                ]
            ],
        )
        self.assertEqual(
            grounding_properties["source_economic_mechanism"]["enum"],
            [
                retry_context["expected_selected_fact_groundings"][0][
                    "source_economic_mechanism"
                ]
            ],
        )
        self.assertEqual(
            retry_context["expected_selected_fact_groundings"][0][
                "source_predicate"
            ],
            "RETRY_PREDICATE_0",
        )
        self.assertEqual(
            response["selected_fact_groundings"][0]["source_predicate"],
            "RETRY_PREDICATE_0",
        )

    def test_component_retry_schema_binds_immutable_fields_by_row(self) -> None:
        expected_rows = [
            {
                "fact_row_index": 7,
                "source_predicate": "PREDICATE_7",
                "source_value_json": '"VALUE_7"',
                "source_period_json": '"PERIOD_7"',
                "source_economic_mechanism": "MECHANISM_7",
            },
            {
                "fact_row_index": 9,
                "source_predicate": "PREDICATE_9",
                "source_value_json": '"VALUE_9"',
                "source_period_json": '"PERIOD_9"',
                "source_economic_mechanism": "MECHANISM_9",
            },
        ]
        schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "loss_accounted_fact_chunk_validation_retry_context": {
                    "expected_selected_fact_groundings": expected_rows,
                }
            },
        )

        variants = schema["properties"]["selected_fact_groundings"][
            "items"
        ]["anyOf"]
        self.assertEqual(len(variants), 2)
        actual = {
            variant["properties"]["fact_row_index"]["enum"][0]: {
                field: variant["properties"][field]["enum"][0]
                for field in (
                    "source_predicate",
                    "source_value_json",
                    "source_period_json",
                    "source_economic_mechanism",
                )
            }
            for variant in variants
        }
        self.assertEqual(
            actual,
            {
                row["fact_row_index"]: {
                    key: value
                    for key, value in row.items()
                    if key != "fact_row_index"
                }
                for row in expected_rows
            },
        )

        synthesis_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "historical_component_anchors": [
                    {"anchor_id": "ANCHOR-P", "role": "POSITIVE"},
                    {"anchor_id": "ANCHOR-C", "role": "COUNTER"},
                ],
                "loss_accounted_fact_chunk_synthesis": {
                    "chunk_responses": [
                        {
                            "response": {
                                "selected_fact_groundings": [
                                    {
                                        **row,
                                        "component_interpretation": (
                                            "chunk interpretation"
                                        ),
                                    }
                                ],
                                "prior_fact_dispositions": [
                                    {
                                        "fact_row_index": row[
                                            "fact_row_index"
                                        ],
                                        "disposition": "RETAIN",
                                        "reason": "chunk disposition",
                                    }
                                ],
                            }
                        }
                        for row in expected_rows
                    ]
                }
            },
        )
        synthesis_variants = synthesis_schema["properties"][
            "selected_fact_groundings"
        ]["items"]["anyOf"]
        self.assertEqual(
            [
                row["properties"]["fact_row_index"]["enum"][0]
                for row in synthesis_variants
            ],
            [7, 9],
        )
        synthesis_properties = synthesis_schema["properties"]
        self.assertEqual(
            [
                row["properties"]["fact_row_index"]["enum"][0]
                for row in synthesis_properties[
                    "prior_fact_dispositions"
                ]["prefixItems"]
            ],
            [7, 9],
        )
        self.assertEqual(
            [
                row["properties"]["fact_row_index"]["enum"][0]
                for row in synthesis_properties[
                    "prior_fact_dispositions"
                ]["items"]["anyOf"]
            ],
            [7, 9],
        )
        self.assertEqual(
            synthesis_properties["prior_fact_dispositions"]["minItems"],
            2,
        )
        self.assertEqual(
            synthesis_properties["prior_fact_dispositions"]["maxItems"],
            2,
        )
        self.assertTrue(
            synthesis_properties["prior_fact_dispositions"][
                "uniqueItems"
            ]
        )
        self.assertEqual(
            synthesis_properties["research_complete"],
            {"type": "boolean", "enum": [True]},
        )
        self.assertEqual(
            synthesis_properties["historical_anchor_ids"],
            {
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": ["ANCHOR-P", "ANCHOR-C"],
                },
                "minItems": 2,
                "maxItems": 2,
                "uniqueItems": True,
            },
        )
        self.assertEqual(
            synthesis_properties["nearest_positive_anchor_ids"]["items"][
                "enum"
            ],
            ["ANCHOR-P"],
        )
        self.assertEqual(
            synthesis_properties["nearest_counter_anchor_ids"]["items"][
                "enum"
            ],
            ["ANCHOR-C"],
        )

    def test_red_team_schema_rejects_duplicate_challenged_fact_rows(self) -> None:
        schema = _provider_output_schema(
            pass_name="RED_TEAM_RESEARCH",
            payload={},
        )

        self.assertTrue(
            schema["properties"]["challenged_fact_row_indices"][
                "uniqueItems"
            ]
        )

        chunk_schema = _provider_output_schema(
            pass_name="RED_TEAM_RESEARCH",
            payload={
                "loss_accounted_fact_chunk": {"chunk_index": 12},
                "current_evidence_fact_graph": [
                    {"fact_row_index": 2},
                    {"fact_row_index": 5},
                ],
            },
        )
        self.assertEqual(
            chunk_schema["properties"]["challenged_fact_row_indices"][
                "items"
            ],
            {"type": "integer", "enum": [2, 5]},
        )

        synthesis_schema = _provider_output_schema(
            pass_name="RED_TEAM_RESEARCH",
            payload={
                "loss_accounted_fact_chunk_synthesis": {
                    "chunk_responses": [
                        {
                            "response": {
                                "challenged_fact_row_indices": [17, 23]
                            }
                        },
                        {
                            "response": {
                                "challenged_fact_row_indices": [23, 31]
                            }
                        },
                    ]
                }
            },
        )
        self.assertEqual(
            synthesis_schema["properties"][
                "challenged_fact_row_indices"
            ]["items"],
            {"type": "integer", "enum": [17, 23, 31]},
        )

    def test_judge_schema_binds_the_role_required_complete_fact_roster(self) -> None:
        analyst_schema = _provider_output_schema(
            pass_name="COMPONENT_ANALYST_JUDGE",
            payload={
                "allowed_support_fact_ids": ["EFACT-P1", "EFACT-P2"],
                "allowed_counter_fact_ids": ["EFACT-C1"],
            },
        )
        self.assertEqual(
            analyst_schema["properties"]["support_fact_ids"],
            {
                "type": "array",
                "enum": [["EFACT-P1", "EFACT-P2"]],
            },
        )
        self.assertNotIn(
            "enum",
            analyst_schema["properties"]["counter_fact_ids"],
        )

        skeptic_schema = _provider_output_schema(
            pass_name="COMPONENT_SKEPTIC_JUDGE",
            payload={
                "allowed_support_fact_ids": ["EFACT-P1"],
                "allowed_counter_fact_ids": ["EFACT-C1", "EFACT-C2"],
            },
        )
        self.assertEqual(
            skeptic_schema["properties"]["counter_fact_ids"],
            {
                "type": "array",
                "enum": [["EFACT-C1", "EFACT-C2"]],
            },
        )
        self.assertEqual(
            skeptic_schema["properties"]["support_fact_ids"],
            {
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": ["EFACT-P1"],
                },
            },
        )

        empty_analyst_schema = _provider_output_schema(
            pass_name="COMPONENT_ANALYST_JUDGE",
            payload={"allowed_support_fact_ids": []},
        )
        self.assertEqual(
            empty_analyst_schema["properties"]["support_fact_ids"]["enum"],
            [[]],
        )

        empty_skeptic_schema = _provider_output_schema(
            pass_name="COMPONENT_SKEPTIC_JUDGE",
            payload={
                "allowed_support_fact_ids": [],
                "allowed_counter_fact_ids": ["EFACT-C1"],
            },
        )
        self.assertEqual(
            empty_skeptic_schema["properties"]["support_fact_ids"],
            {"type": "array", "enum": [[]]},
        )

    def test_ollama_canonicalizes_only_duplicate_red_team_fact_rows(self) -> None:
        response = {
            "challenged_fact_row_indices": [37, 206, 206, 297],
            "review_complete": True,
        }

        self.assertEqual(
            _canonicalize_ollama_red_team_fact_set(
                pass_name="RED_TEAM_RESEARCH",
                response=response,
            ),
            {
                "challenged_fact_row_indices": [37, 206, 297],
                "review_complete": True,
            },
        )
        self.assertIs(
            _canonicalize_ollama_red_team_fact_set(
                pass_name="COMPONENT_RESEARCH",
                response=response,
            ),
            response,
        )

    def test_transport_sends_schema_bound_non_thinking_request(self) -> None:
        schema = {
            "type": "object",
            "additionalProperties": False,
            "required": ["usable"],
            "properties": {"usable": {"type": "boolean"}},
        }
        captured = {}

        def fake_urlopen(request, *, timeout):
            captured["url"] = request.full_url
            captured["body"] = json.loads(request.data.decode("utf-8"))
            captured["timeout"] = timeout
            return _FakeHTTPResponse(
                {
                    "message": {"content": '{"usable":false}'},
                    "done": True,
                    "done_reason": "stop",
                    "prompt_eval_count": 10,
                }
            )

        transport = OllamaStructuredProviderTransport(
            model="test-model",
            context_length=65_536,
            timeout_seconds=123,
        )
        with patch("urllib.request.urlopen", side_effect=fake_urlopen):
            response = transport.complete(
                prompt="Use only as-of-date evidence.",
                output_schema=schema,
                schema_name="e2r_test",
            )

        self.assertEqual(response.payload, {"usable": False})
        self.assertEqual(captured["url"], "http://127.0.0.1:11434/api/chat")
        self.assertEqual(captured["timeout"], 123)
        self.assertEqual(captured["body"]["format"], schema)
        self.assertEqual(captured["body"]["options"]["num_ctx"], 65_536)
        self.assertEqual(captured["body"]["options"]["num_predict"], 32_768)
        self.assertFalse(captured["body"]["think"])
        self.assertFalse(captured["body"]["stream"])

    def test_transport_failure_is_provider_pending_class_not_empty_output(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        with patch(
            "urllib.request.urlopen",
            side_effect=urllib.error.URLError("offline"),
        ):
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "ollama_transport_error",
            ):
                transport.complete(
                    prompt="prompt",
                    output_schema={"type": "object"},
                    schema_name="e2r_test",
                )

    def test_transport_rejects_non_object_model_output(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        response = _FakeHTTPResponse(
            {
                "message": {"content": "[]"},
                "done": True,
                "done_reason": "stop",
                "prompt_eval_count": 10,
            }
        )
        with patch("urllib.request.urlopen", return_value=response):
            with self.assertRaisesRegex(
                StructuredProviderRejected,
                "non-object",
            ):
                transport.complete(
                    prompt="prompt",
                    output_schema={"type": "object"},
                    schema_name="e2r_test",
                )

    def test_provider_cache_is_bound_to_ollama_inference_identity(self) -> None:
        transport = OllamaStructuredProviderTransport(
            base_url="http://127.0.0.1:11434",
            model="model-a",
            context_length=65_536,
            model_digest="a" * 64,
            server_version="0.32.1",
        )
        provider = OllamaResearcherProvider(transport=transport)
        identity = provider._provider_identity()
        self.assertEqual(identity["model"], "model-a")
        self.assertEqual(identity["context_length"], 65_536)
        self.assertEqual(identity["model_digest"], "a" * 64)
        self.assertEqual(identity["base_url"], "http://127.0.0.1:11434")
        with tempfile.TemporaryDirectory() as directory:
            provider.configure_response_cache(Path(directory))
            self.assertEqual(
                provider.response_cache_audit()["provider_name"],
                "OLLAMA_STRUCTURED_RESEARCHER_MODE",
            )

    def test_cli_uses_ollama_only_after_explicit_selection(self) -> None:
        base = [
            "--as-of-date", "2026-06-29",
            "--symbols", "005930",
            "--archetype", "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "--live-materialization-authorized", "true",
            "--checkpoint-resume", "true",
            "--gold-lane-isolated", "true",
            "--require-researcher-parity", "true",
            "--output-root", "output/test",
        ]
        default_args = build_parser().parse_args(base)
        self.assertIsNone(_build_research_provider(default_args))

        local_args = build_parser().parse_args(
            [
                *base,
                "--research-provider", "ollama",
                "--ollama-model", "model-b",
                "--ollama-context-length", "65536",
                "--ollama-fact-document-chunk-chars", "90000",
            ]
        )
        provider = _build_research_provider(local_args)
        self.assertIsInstance(provider, OllamaResearcherProvider)
        self.assertEqual(provider.transport.model, "model-b")
        self.assertEqual(provider.transport.context_length, 65_536)
        self.assertEqual(provider.fact_document_chunk_chars, 90_000)
        self.assertEqual(provider.semantic_prompt_chunk_chars, 10_000)
        self.assertEqual(provider.memo_fact_prompt_chunk_chars, 100_000)
        self.assertEqual(
            provider.candidate_ranking_prompt_chunk_chars,
            100_000,
        )
        self.assertEqual(
            provider.candidate_ranking_page_candidate_limit,
            12,
        )
        self.assertEqual(
            SOURCE_CANDIDATE_RANKING_SCHEMA["properties"]["decisions"][
                "maxItems"
            ],
            CANDIDATE_RANKING_PAGE_CANDIDATE_LIMIT,
        )
        runner = CurrentResearcherModeTargetRunner(provider=provider)
        self.assertEqual(
            runner.fact_extractor.max_document_chars_per_call,
            10_000,
        )
        provider.transport.model_digest = "b" * 64
        provider.transport.server_version = "0.32.1"
        manifest = _research_provider_manifest(provider)
        self.assertTrue(manifest["provider_selected_explicitly"])
        self.assertFalse(manifest["score_or_stage_authority"])
        self.assertEqual(
            manifest["provider_identity"]["model_digest"],
            "b" * 64,
        )
        self.assertEqual(
            manifest["provider_identity"][
                "effective_semantic_prompt_chunk_chars"
            ],
            10_000,
        )

    def test_fact_chunk_size_reserves_room_for_expansion_heavy_json(self) -> None:
        provider = OllamaResearcherProvider.default(
            context_length=262_144,
            max_output_tokens=32_768,
            fact_document_chunk_chars=100_000,
        )

        self.assertEqual(provider.semantic_prompt_chunk_chars, 10_000)
        self.assertEqual(provider.memo_fact_prompt_chunk_chars, 100_000)
        runner = CurrentResearcherModeTargetRunner(provider=provider)
        self.assertEqual(
            runner.fact_extractor.max_document_chars_per_call,
            10_000,
        )
        self.assertEqual(
            provider._provider_identity()[
                "effective_semantic_prompt_chunk_chars"
            ],
            10_000,
        )
        self.assertEqual(
            provider._provider_identity()[
                "effective_memo_fact_prompt_chunk_chars"
            ],
            100_000,
        )

    def test_incomplete_or_unaccounted_response_is_rejected(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        for envelope in (
            {
                "message": {"content": '{}'},
                "done_reason": "stop",
                "prompt_eval_count": 10,
            },
            {
                "message": {"content": '{}'},
                "done": True,
                "done_reason": "length",
                "prompt_eval_count": 10,
            },
            {
                "message": {"content": '{}'},
                "done": True,
                "done_reason": "stop",
            },
        ):
            with self.subTest(envelope=envelope):
                with patch(
                    "urllib.request.urlopen",
                    return_value=_FakeHTTPResponse(envelope),
                ):
                    with self.assertRaises(StructuredProviderRejected):
                        transport.complete(
                            prompt="prompt",
                            output_schema={"type": "object"},
                            schema_name="e2r_test",
                        )

    def test_malformed_utf8_is_rejected_and_response_is_bounded(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        with patch(
            "urllib.request.urlopen",
            return_value=_FakeHTTPResponse(raw=b"\xff\xfe"),
        ):
            with self.assertRaisesRegex(
                StructuredProviderRejected,
                "malformed UTF-8",
            ):
                transport.complete(
                    prompt="prompt",
                    output_schema={"type": "object"},
                    schema_name="e2r_test",
                )

    def test_prompt_cap_and_remote_plaintext_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "loopback"):
            OllamaStructuredProviderTransport(
                base_url="http://192.0.2.10:11434",
                model="test-model",
            )
        transport = OllamaStructuredProviderTransport(
            model="test-model",
            prompt_character_limit=10,
        )
        with self.assertRaisesRegex(
            StructuredProviderRejected,
            "prompt_transport_too_large",
        ):
            transport.complete(
                prompt="x" * 11,
                output_schema={"type": "object"},
                schema_name="e2r_test",
            )

    def test_mutable_model_tag_resolves_to_digest_and_server_version(self) -> None:
        transport = OllamaStructuredProviderTransport(model="model-a")

        def fake_urlopen(request, *, timeout):
            if request.full_url.endswith("/api/tags"):
                return _FakeHTTPResponse(
                    {
                        "models": [
                            {
                                "name": "model-a",
                                "model": "model-a",
                                "digest": "c" * 64,
                            }
                        ]
                    }
                )
            if request.full_url.endswith("/api/version"):
                return _FakeHTTPResponse({"version": "0.32.1"})
            raise AssertionError(request.full_url)

        with patch("urllib.request.urlopen", side_effect=fake_urlopen):
            identity = transport.provider_identity()
        self.assertEqual(identity["model_digest"], "c" * 64)
        self.assertEqual(identity["server_version"], "0.32.1")

    def test_blind_output_violation_is_audited_and_never_cached(self) -> None:
        class ForbiddenOutputTransport:
            model = "test"
            profile = None
            extra_args = ()
            codex_command = None

            def complete(self, **kwargs):
                return StructuredProviderResponse(
                    payload={"total_score": 99},
                    raw_response='{"total_score":99}',
                    stderr="",
                    returncode=0,
                )

        provider = CodexResearcherProvider(
            transport=ForbiddenOutputTransport()
        )
        with tempfile.TemporaryDirectory() as directory:
            provider.configure_response_cache(directory)
            with self.assertRaisesRegex(
                StructuredProviderRejected,
                "blind_output_rejected",
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={"target_id": "TEST", "as_of_date": "2026-06-29"},
                )
            self.assertEqual(
                provider.calls[-1]["status"],
                "PROVIDER_OUTPUT_REJECTED",
            )
            self.assertEqual(
                provider.response_cache_audit()[
                    "provider_output_rejected_count"
                ],
                1,
            )
            self.assertEqual(tuple(Path(directory).glob("*.json")), ())

    def test_codex_selection_rejects_silently_ignored_ollama_option(self) -> None:
        args = build_parser().parse_args(
            [
                "--as-of-date", "2026-06-29",
                "--symbols", "005930",
                "--archetype", "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "--live-materialization-authorized", "true",
                "--checkpoint-resume", "true",
                "--gold-lane-isolated", "true",
                "--require-researcher-parity", "true",
                "--output-root", "output/test",
                "--ollama-model", "model-b",
            ]
        )
        with self.assertRaisesRegex(ValueError, "require"):
            _build_research_provider(args)


if __name__ == "__main__":
    unittest.main()
