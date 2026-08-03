from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderResponse,
)
from e2r.research_brain.researcher_mode import CodexResearcherProvider
from e2r.research_brain.researcher_mode.component_researcher import (
    COMPONENT_RESEARCH_SCHEMA,
    _canonical_json_hash,
    _expected_component_chunk_fact_groundings,
    _loss_accounted_fact_chunk_payloads,
    _loss_accounted_fact_chunk_synthesis_payload,
    _provider_output_schema,
    _validate_loss_accounted_chunk_response,
    _validate_loss_accounted_synthesis_response,
)
from e2r.research_brain.researcher_mode.prompt_projection import (
    project_current_decision_citable_facts,
)


class StructuredResearchProviderTests(unittest.TestCase):
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
        class NarrowCodexResearcherProvider(CodexResearcherProvider):
            @property
            def semantic_prompt_chunk_chars(self) -> int:
                return 10_000

            @property
            def memo_fact_prompt_chunk_chars(self) -> int:
                return 100_000

            @property
            def prompt_transport_max_chars(self) -> int:
                return 500_000

        transport = ChunkAwareTransport()
        provider = NarrowCodexResearcherProvider(
            transport=transport  # type: ignore[arg-type]
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
        synthesis_roster = transport.output_schemas[-1]["properties"][
            "fact_row_indices"
        ]
        synthesis_chunk_responses = transport.payloads[-1][
            "loss_accounted_fact_chunk_synthesis"
        ]["chunk_responses"]
        self.assertEqual(
            [row["enum"] for row in synthesis_roster["prefixItems"]],
            [
                row["response"]["fact_row_indices"]
                for row in synthesis_chunk_responses
                if row["response"]["fact_row_indices"]
            ],
        )
        self.assertEqual(
            synthesis_roster["minItems"],
            len(synthesis_roster["prefixItems"]),
        )
        self.assertTrue(all(length < 500_000 for length in transport.prompt_lengths))

        class BoundedCodexResearcherProvider(CodexResearcherProvider):
            @property
            def memo_fact_prompt_chunk_chars(self) -> int:
                return 100_000

        codex_transport = ChunkAwareTransport()
        codex_provider = BoundedCodexResearcherProvider(
            transport=codex_transport  # type: ignore[arg-type]
        )
        codex_response = codex_provider.complete(
            pass_name="BUSINESS_MODEL_RESEARCH",
            payload=payload,
        )
        codex_chunks = [
            row
            for row in codex_transport.payloads
            if row.get("loss_accounted_fact_chunk")
        ]
        self.assertGreater(len(codex_chunks), 1)
        self.assertEqual(
            [
                global_index
                for chunk in codex_chunks
                for global_index in chunk["loss_accounted_fact_chunk"][
                    "global_fact_row_index_by_chunk_local_index"
                ]
            ],
            list(range(len(facts))),
        )
        self.assertTrue(
            codex_transport.payloads[-1].get(
                "loss_accounted_fact_chunk_synthesis"
            )
        )
        self.assertEqual(
            set(codex_response["fact_row_indices"]),
            {
                chunk["loss_accounted_fact_chunk"][
                    "global_fact_row_index_by_chunk_local_index"
                ][0]
                for chunk in codex_chunks
            },
        )
        self.assertTrue(
            all(
                length < 1_000_000
                for length in codex_transport.prompt_lengths
            )
        )

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
                self.prompt_lengths = []

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
                self.prompt_lengths.append(len(prompt))
                chunk = payload.get("loss_accounted_fact_chunk")
                if chunk:
                    retry = payload.get(
                        "loss_accounted_fact_chunk_validation_retry_context"
                    )
                    selected_index = payload["current_evidence_fact_graph"][0][
                        "fact_row_index"
                    ]
                    if retry:
                        retry_row = (
                            retry["expected_selected_fact_groundings"][-1]
                        )
                        grounding = {
                            **retry_row,
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

        class BoundedCodexResearcherProvider(CodexResearcherProvider):
            @property
            def memo_fact_prompt_chunk_chars(self) -> int:
                return 100_000

        provider = BoundedCodexResearcherProvider(
            transport=transport  # type: ignore[arg-type]
        )
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
        expected_groundings = _expected_component_chunk_fact_groundings(
            retry_payloads[0]
        )
        expected_grounding_rows = [
            {
                "fact_row_index": row_index,
                **expected_groundings[row_index],
            }
            for row_index in sorted(expected_groundings)
        ]
        self.assertEqual(
            retry_context["expected_selected_fact_groundings"],
            expected_grounding_rows,
        )
        retry_row_indices = [
            row["fact_row_index"]
            for row in retry_context["expected_selected_fact_groundings"]
        ]
        self.assertEqual(
            retry_row_indices,
            sorted(
                row["fact_row_index"]
                for row in retry_payloads[0][
                    "current_evidence_fact_graph"
                ]
            ),
        )
        self.assertEqual(
            len(retry_row_indices),
            len(set(retry_row_indices)),
        )
        self.assertEqual(
            retry_context["rejected_selected_fact_row_indices"],
            [
                base_chunk_payload["current_evidence_fact_graph"][0][
                    "fact_row_index"
                ]
            ],
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
        self.assertEqual(
            len(grounding_variants),
            len(expected_grounding_rows),
        )
        grounding_properties = grounding_variants[-1]["properties"]
        self.assertEqual(
            grounding_properties["fact_row_index"]["enum"],
            [
                retry_context["expected_selected_fact_groundings"][-1][
                    "fact_row_index"
                ]
            ],
        )
        self.assertEqual(
            grounding_properties["source_economic_mechanism"]["enum"],
            [
                retry_context["expected_selected_fact_groundings"][-1][
                    "source_economic_mechanism"
                ]
            ],
        )
        self.assertEqual(
            retry_context["expected_selected_fact_groundings"][-1][
                "source_predicate"
            ],
            "RETRY_PREDICATE_1",
        )
        self.assertEqual(
            response["selected_fact_groundings"][0]["source_predicate"],
            "RETRY_PREDICATE_1",
        )
        retry_prompt_length = next(
            prompt_length
            for payload, prompt_length in zip(
                transport.payloads,
                transport.prompt_lengths,
            )
            if payload.get(
                "loss_accounted_fact_chunk_validation_retry_context"
            )
        )
        self.assertLess(retry_prompt_length, 1_000_000)

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
                    if key
                    in {
                        "source_predicate",
                        "source_economic_mechanism",
                    }
                }
                for row in expected_rows
            },
        )
        self.assertTrue(
            all(
                "enum" not in variant["properties"][field]
                for variant in variants
                for field in (
                    "source_value_json",
                    "source_period_json",
                )
            )
        )

        chunk_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "loss_accounted_fact_chunk": {"chunk_index": 0},
                "loss_accounted_fact_chunk_validation_retry_context": {
                    "expected_selected_fact_groundings": expected_rows,
                },
                "prior_component_memo_context": {
                    "current_fact_rows": [
                        {"fact_row_index": row["fact_row_index"]}
                        for row in expected_rows
                    ]
                },
            },
        )
        chunk_dispositions = chunk_schema["properties"][
            "prior_fact_dispositions"
        ]
        self.assertEqual(
            [
                row["properties"]["fact_row_index"]["enum"][0]
                for row in chunk_dispositions["prefixItems"]
            ],
            [7, 9],
        )
        self.assertEqual(
            [
                row["properties"]["fact_row_index"]["enum"][0]
                for row in chunk_dispositions["items"]["anyOf"]
            ],
            [7, 9],
        )
        self.assertEqual(chunk_dispositions["minItems"], 2)
        self.assertEqual(chunk_dispositions["maxItems"], 2)
        self.assertNotIn("uniqueItems", chunk_dispositions)

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
        self.assertNotIn(
            "uniqueItems",
            synthesis_properties["prior_fact_dispositions"],
        )
        consistency_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "component_research_validation_retry_context": {
                    "expected_selected_fact_groundings": expected_rows,
                    "required_model_selected_fact_row_indices": [7],
                },
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
                },
            },
        )
        consistency_properties = consistency_schema["properties"]
        self.assertEqual(
            [
                row["enum"][0]
                for row in consistency_properties[
                    "selected_fact_row_indices"
                ]["prefixItems"]
            ],
            [7],
        )
        self.assertEqual(
            consistency_properties["selected_fact_row_indices"]["items"],
            {"type": "integer", "enum": [7, 9]},
        )
        self.assertEqual(
            [
                row["properties"]["fact_row_index"]["enum"][0]
                for row in consistency_properties[
                    "selected_fact_groundings"
                ]["prefixItems"]
            ],
            [7],
        )
        self.assertEqual(
            [
                row["properties"]["fact_row_index"]["enum"][0]
                for row in consistency_properties[
                    "selected_fact_groundings"
                ]["items"]["anyOf"]
            ],
            [7, 9],
        )
        self.assertEqual(
            [
                row["properties"]["disposition"]["enum"][0]
                for row in consistency_properties[
                    "prior_fact_dispositions"
                ]["prefixItems"]
            ],
            ["RETAIN", "OMIT"],
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

    def test_production_fact_schema_binds_current_objective_roster(self) -> None:
        schema = _provider_output_schema(
            pass_name="EVIDENCE_FACT_EXTRACTION",
            payload={
                "fact_extraction_scope_contract": {
                    "mode": "PRODUCTION_OBJECTIVE_LOCAL",
                    "document_objective_ids": [
                        {
                            "document_id": "DOC-1",
                            "objective_ids": ["OBJECTIVE-A"],
                        },
                        {
                            "document_id": "DOC-2",
                            "objective_ids": ["OBJECTIVE-B"],
                        },
                    ],
                }
            },
        )
        fact_schema = schema["properties"]["facts"]["items"]

        self.assertIn("objective_ids", fact_schema["required"])
        self.assertIn("objective_relation", fact_schema["required"])
        self.assertEqual(
            fact_schema["properties"]["objective_ids"]["items"]["enum"],
            ["OBJECTIVE-A", "OBJECTIVE-B"],
        )
        self.assertEqual(
            fact_schema["properties"]["objective_relation"]["enum"],
            ["ADVANCE", "COUNTER", "SUPERSEDE"],
        )
        other_schema = _provider_output_schema(
            pass_name="EVIDENCE_FACT_EXTRACTION",
            payload={
                "fact_extraction_scope_contract": {
                    "mode": "PRODUCTION_OBJECTIVE_LOCAL",
                    "document_objective_ids": [
                        {
                            "document_id": "DOC-3",
                            "objective_ids": ["OBJECTIVE-C"],
                        }
                    ],
                }
            },
        )
        self.assertNotEqual(
            _canonical_json_hash(schema),
            _canonical_json_hash(other_schema),
        )

    def test_candidate_schema_binds_requested_source_family_roster(self) -> None:
        schema = _provider_output_schema(
            pass_name="SOURCE_CANDIDATE_RANKING",
            payload={
                "discovery_candidates": [
                    {
                        "candidate_id": "CANDIDATE-1",
                        "requested_source_families": [
                            "CUSTOMER_OFFICIAL"
                        ],
                    }
                ]
            },
        )
        matched_schema = schema["properties"]["decisions"]["items"][
            "properties"
        ]["matched_requested_source_family"]
        self.assertEqual(
            matched_schema["enum"],
            ["NONE", "CUSTOMER_OFFICIAL"],
        )
        other_schema = _provider_output_schema(
            pass_name="SOURCE_CANDIDATE_RANKING",
            payload={
                "discovery_candidates": [
                    {
                        "candidate_id": "CANDIDATE-2",
                        "requested_source_families": ["REUTERS"],
                    }
                ]
            },
        )
        self.assertNotEqual(
            _canonical_json_hash(schema),
            _canonical_json_hash(other_schema),
        )

    def test_component_source_coverage_schema_binds_actual_payload_roster(
        self,
    ) -> None:
        coverage_rows = [
            {
                "coverage_id": "TECHTIMES_GENERAL_WEB_DISCOVERY",
                "source_family": "GENERAL_WEB",
            },
            {
                "coverage_id": "COMPANY_IR",
                "source_family": "COMPANY_OFFICIAL",
            },
        ]
        allowed_labels = [
            "COMPANY_IR",
            "TECHTIMES_GENERAL_WEB_DISCOVERY",
        ]

        for component_id in ("INFO_CONFIDENCE", "CONTRACT_QUALITY"):
            with self.subTest(component_id=component_id):
                chunk_schema = _provider_output_schema(
                    pass_name="COMPONENT_RESEARCH",
                    payload={
                        "component_id": component_id,
                        "source_coverage": coverage_rows,
                        "loss_accounted_fact_chunk": {"chunk_index": 0},
                        "current_evidence_fact_graph": [
                            {
                                "fact_row_index": 0,
                                "encoded_fact_values": [0, 0, 0, 0],
                            }
                        ],
                        "current_evidence_fact_projection": {
                            "chunk_fact_row_encoding": {
                                "encoded_fact_value_fields": [
                                    "predicate_dictionary_index",
                                    "value_dictionary_index",
                                    "period_dictionary_index",
                                    "economic_mechanism_dictionary_index",
                                ]
                            },
                            "fact_value_dictionaries": {
                                "predicate": ["PREDICATE"],
                                "value": ["VALUE"],
                                "period": ["PERIOD"],
                                "economic_mechanism": ["MECHANISM"],
                            },
                        },
                    },
                )
                item_schema = chunk_schema["properties"][
                    "source_coverage"
                ]["items"]
                self.assertEqual(item_schema["enum"], allowed_labels)
                self.assertIn(
                    "TECHTIMES_GENERAL_WEB_DISCOVERY",
                    item_schema["enum"],
                )
                self.assertNotIn(
                    "CUSTOMER_OFFICIAL_CONFIRMATION",
                    item_schema["enum"],
                )

        empty_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "component_id": "INFO_CONFIDENCE",
                "source_coverage": [],
            },
        )
        self.assertEqual(
            empty_schema["properties"]["source_coverage"],
            {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
                "maxItems": 0,
            },
        )

        bound_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={"source_coverage": coverage_rows},
        )
        other_roster_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={"source_coverage": ["EXCHANGE_OFFICIAL"]},
        )
        self.assertNotEqual(
            _canonical_json_hash(COMPONENT_RESEARCH_SCHEMA),
            _canonical_json_hash(bound_schema),
        )
        self.assertNotEqual(
            _canonical_json_hash(bound_schema),
            _canonical_json_hash(other_roster_schema),
        )

    def test_component_synthesis_preserves_and_binds_source_coverage(
        self,
    ) -> None:
        coverage_rows = [
            {"coverage_id": "GENERAL_WEB_DISCOVERY"},
            {"route_id": "COMPANY_IR"},
        ]
        original_payload = {
            "component_id": "INFO_CONFIDENCE",
            "source_coverage": coverage_rows,
            "current_evidence_fact_graph": [],
            "current_evidence_fact_projection": {},
        }
        synthesis_payload = _loss_accounted_fact_chunk_synthesis_payload(
            original_payload,
            pass_name="COMPONENT_RESEARCH",
            chunks=[],
            chunk_responses=[],
        )

        self.assertEqual(
            synthesis_payload["source_coverage"],
            coverage_rows,
        )
        synthesis_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload=synthesis_payload,
        )
        item_schema = synthesis_schema["properties"]["source_coverage"][
            "items"
        ]
        self.assertEqual(
            item_schema["enum"],
            ["COMPANY_IR", "GENERAL_WEB_DISCOVERY"],
        )
        self.assertNotIn(
            "CUSTOMER_OFFICIAL_CONFIRMATION",
            item_schema["enum"],
        )

    def test_component_grounding_retry_keeps_source_coverage_binding(
        self,
    ) -> None:
        expected_row = {
            "fact_row_index": 7,
            "source_predicate": "PREDICATE_7",
            "source_value_json": '"VALUE_7"',
            "source_period_json": '"PERIOD_7"',
            "source_economic_mechanism": "MECHANISM_7",
        }
        schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "source_coverage": ["GENERAL_WEB_DISCOVERY"],
                "loss_accounted_fact_chunk_validation_retry_context": {
                    "expected_selected_fact_groundings": [expected_row],
                },
            },
        )

        grounding_variant = schema["properties"][
            "selected_fact_groundings"
        ]["items"]["anyOf"][0]
        self.assertEqual(
            grounding_variant["properties"]["source_predicate"]["enum"],
            ["PREDICATE_7"],
        )
        self.assertEqual(
            schema["properties"]["source_coverage"]["items"]["enum"],
            ["GENERAL_WEB_DISCOVERY"],
        )

    def test_component_schema_requires_every_available_structured_metric_row(
        self,
    ) -> None:
        schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "structured_metric_rows": [
                    {
                        "structured_metric_row_index": 0,
                        "structured_requirement_id": "CURRENT_VALUATION",
                        "immutable_source_backed_value": {"record_count": 3},
                    },
                    {
                        "structured_metric_row_index": 1,
                        "structured_requirement_id": "DURABLE_VISIBILITY",
                        "immutable_source_backed_value": {"record_count": 2},
                    },
                ]
            },
        )

        roster = schema["properties"]["structured_metric_row_indices"]
        self.assertEqual(
            [row["enum"][0] for row in roster["prefixItems"]],
            [0, 1],
        )
        self.assertEqual(roster["minItems"], 2)
        self.assertEqual(roster["maxItems"], 2)
        self.assertEqual(
            roster["items"],
            {"type": "integer", "enum": [0, 1]},
        )
        self.assertNotIn("uniqueItems", roster)

        chunk_schema = _provider_output_schema(
            pass_name="COMPONENT_RESEARCH",
            payload={
                "loss_accounted_fact_chunk": {"chunk_index": 0},
                "loss_accounted_fact_chunk_validation_retry_context": {
                    "expected_selected_fact_groundings": [
                        {
                            "fact_row_index": 0,
                            "source_predicate": "PREDICATE",
                            "source_value_json": '"VALUE"',
                            "source_period_json": '"PERIOD"',
                            "source_economic_mechanism": "MECHANISM",
                        }
                    ]
                },
                "structured_metric_rows": [
                    {"structured_metric_row_index": 0},
                    {"structured_metric_row_index": 1},
                ],
            },
        )
        chunk_roster = chunk_schema["properties"][
            "structured_metric_row_indices"
        ]
        self.assertNotIn("prefixItems", chunk_roster)
        self.assertNotIn("minItems", chunk_roster)
        self.assertNotIn("maxItems", chunk_roster)

    def test_business_model_synthesis_binds_review_completion_not_certainty(
        self,
    ) -> None:
        synthesis_schema = _provider_output_schema(
            pass_name="BUSINESS_MODEL_RESEARCH",
            payload={
                "loss_accounted_fact_chunk_synthesis": {
                    "chunk_responses": [
                        {
                            "chunk_index": 0,
                            "response": {
                                "fact_row_indices": [3, 5],
                                "research_complete": False,
                            }
                        },
                        {
                            "chunk_index": 1,
                            "response": {
                                "fact_row_indices": [11, 13],
                                "research_complete": True,
                            },
                        },
                        {
                            "chunk_index": 2,
                            "response": {
                                "fact_row_indices": [],
                                "research_complete": False,
                            },
                        },
                    ]
                }
            },
        )
        self.assertEqual(
            synthesis_schema["properties"]["research_complete"],
            {"type": "boolean", "enum": [True]},
        )
        fact_roster = synthesis_schema["properties"]["fact_row_indices"]
        self.assertEqual(
            [row["enum"] for row in fact_roster["prefixItems"]],
            [[3, 5], [11, 13]],
        )
        self.assertEqual(
            fact_roster["items"],
            {"type": "integer", "enum": [3, 5, 11, 13]},
        )
        self.assertEqual(fact_roster["minItems"], 2)
        self.assertNotIn("uniqueItems", fact_roster)
        self.assertNotIn("contains", fact_roster)
        self.assertNotIn("allOf", fact_roster)

        chunk_schema = _provider_output_schema(
            pass_name="BUSINESS_MODEL_RESEARCH",
            payload={
                "loss_accounted_fact_chunk": {"chunk_index": 0},
            },
        )
        self.assertEqual(
            chunk_schema["properties"]["research_complete"],
            {"type": "boolean"},
        )

    def test_business_model_synthesis_validator_rejects_first_chunk_copy(
        self,
    ) -> None:
        chunk_responses = [
            {
                "chunk_index": 0,
                "response": {"fact_row_indices": [3, 5]},
            },
            {
                "chunk_index": 1,
                "response": {"fact_row_indices": [11, 13]},
            },
            {
                "chunk_index": 2,
                "response": {"fact_row_indices": []},
            },
        ]

        with self.assertRaisesRegex(
            StructuredProviderRejected,
            (
                "loss_accounted_business_model_synthesis_"
                "chunk_coverage_mismatch:1"
            ),
        ):
            _validate_loss_accounted_synthesis_response(
                pass_name="BUSINESS_MODEL_RESEARCH",
                response={"fact_row_indices": [3, 5]},
                chunk_responses=chunk_responses,
            )

        _validate_loss_accounted_synthesis_response(
            pass_name="BUSINESS_MODEL_RESEARCH",
            response={"fact_row_indices": [5, 13]},
            chunk_responses=chunk_responses,
        )
        with self.assertRaisesRegex(
            StructuredProviderRejected,
            "loss_accounted_fact_response_duplicate_fact_row_indices",
        ):
            _validate_loss_accounted_synthesis_response(
                pass_name="BUSINESS_MODEL_RESEARCH",
                response={"fact_row_indices": [5, 13, 13]},
                chunk_responses=chunk_responses,
            )

    def test_red_team_schema_rejects_duplicate_challenged_fact_rows(self) -> None:
        schema = _provider_output_schema(
            pass_name="RED_TEAM_RESEARCH",
            payload={},
        )

        self.assertNotIn(
            "uniqueItems",
            schema["properties"]["challenged_fact_row_indices"],
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
        with self.assertRaisesRegex(
            StructuredProviderRejected,
            (
                "loss_accounted_fact_response_duplicate_"
                "challenged_fact_row_indices"
            ),
        ):
            _validate_loss_accounted_chunk_response(
                pass_name="RED_TEAM_RESEARCH",
                response={"challenged_fact_row_indices": [2, 2]},
                allowed_fact_row_indices={2, 5},
                prior_fact_row_indices=set(),
                expected_component_groundings={},
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
                "prefixItems": [
                    {"type": "string", "enum": ["EFACT-P1"]},
                    {"type": "string", "enum": ["EFACT-P2"]},
                ],
                "items": {
                    "type": "string",
                    "enum": ["EFACT-P1", "EFACT-P2"],
                },
                "minItems": 2,
                "maxItems": 2,
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
                "prefixItems": [
                    {"type": "string", "enum": ["EFACT-C1"]},
                    {"type": "string", "enum": ["EFACT-C2"]},
                ],
                "items": {
                    "type": "string",
                    "enum": ["EFACT-C1", "EFACT-C2"],
                },
                "minItems": 2,
                "maxItems": 2,
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
            empty_analyst_schema["properties"]["support_fact_ids"],
            {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 0,
            },
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
            {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 0,
            },
        )

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


if __name__ == "__main__":
    unittest.main()
