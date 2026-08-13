from __future__ import annotations

import json
import hashlib
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexSubagentTransport,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    _load_fact_checkpoint,
    _load_committed_fact_result_snapshot,
    _upgrade_current_lineage_objective_reassessment_receipts,
)
from e2r.research_brain.researcher_mode.evidence_fact_compiler import (
    EvidenceFactCompiler,
)
from e2r.research_brain.researcher_mode.evidence_fact_extractor import (
    FACT_EXTRACTION_SEMANTICS_VERSION,
    FactExtractionProviderCall,
    ResearcherEvidenceFactExtractor,
    _coerce_provider_call,
    _fact_extraction_continuation_context,
    _replay_current_fact_lineage_group,
    resolve_current_fact_lineage_recovery_binding,
    write_researcher_fact_extraction_result,
)
from e2r.research_brain.researcher_mode.fact_lineage_materials import (
    AUTHORITY_RECOVERY_FACT_SEMANTICS_VERSIONS,
    AuthoritativeResearchEpochFactLedger,
    CurrentFactLineageRecoveryBinding,
    LEGACY_FACT_EXTRACTION_SEMANTICS_VERSION,
    PRIOR_FACT_EXTRACTION_SEMANTICS_VERSION,
    validate_current_v5_fact_lineage_materials,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    load_mechanism_scope_contracts,
)
from tests.test_e2r_v5_fact_lineage_materials import (
    ARCHETYPE,
    AS_OF_DATE,
    OBJECTIVE_COMPONENT,
    TARGET,
    _build_actual_shaped_journal,
    _current_document,
    _official_replay,
    _prompt_document,
    _prompt_payload,
    _proposal,
    _response,
    _write_pair,
)


class _NoCompleteProvider:
    provider_name = "COLLABORATION_CODEX_SUBAGENT"

    def __init__(self) -> None:
        self.complete_call_count = 0

    def complete(self, **_kwargs):
        self.complete_call_count += 1
        raise AssertionError("journal recovery must not call provider.complete")


def _objectives(documents):
    return tuple(
        {
            "objective_id": objective_id,
            "component_id": OBJECTIVE_COMPONENT,
            "question": f"verify {objective_id}",
        }
        for objective_id in sorted(
            {
                str(value)
                for document in documents
                for value in document.get("objective_ids") or ()
            }
        )
    )


def _persisted_claims(template, document, *, count=457):
    rows = []
    objective_ids = list(document["objective_ids"])
    for index in range(count):
        quote = f"Persisted statement {index}."
        identity = {
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "document_id": document["document_id"],
            "question_family_id": f"persisted_question_{index}",
            "subject_id": f"persisted_subject_{index}",
            "predicate_family": f"persisted_predicate_{index}",
            "normalized_object": f"persisted_object_{index}",
            "period": "2026Q2",
            "mechanism_scope_id": f"PERSISTED-SCOPE-{index}",
            "exact_quote": quote,
        }
        row = json.loads(json.dumps(template))
        row.update(
            {
                "claim_id": stable_intelligence_id("RFC", identity),
                "document_id": document["document_id"],
                "source_ids": [document["document_id"]],
                "canonical_url": document["canonical_url"],
                "published_at": document["published_at"],
                "available_at": document["available_at"],
                "source_independence_group": document[
                    "source_independence_group"
                ],
                "source_family": document["source_family"],
                "question_family_id": identity["question_family_id"],
                "question_family_tags": [identity["question_family_id"]],
                "subject_id": identity["subject_id"],
                "subject": f"Persisted mechanism {index}",
                "economic_mechanism": f"persisted mechanism {index}",
                "mechanism_scope_id": identity["mechanism_scope_id"],
                "predicate": f"persisted outcome {index}",
                "predicate_family": identity["predicate_family"],
                "normalized_object": identity["normalized_object"],
                "value": index + 10_000,
                "period": identity["period"],
                "exact_quote": quote,
                "objective_ids": objective_ids,
                "objective_relation": "ADVANCE",
                "provider_prompt_hash": stable_intelligence_id(
                    "FACTPROMPT", {"persisted": index}
                ),
                "provider_response_hash": stable_intelligence_id(
                    "FACTRESP", {"persisted": index}
                ),
            }
        )
        row.pop("supersedes_fact_ids", None)
        row.pop("resolves_fact_ids", None)
        rows.append(row)
    return tuple(rows)


def _ledger(rows):
    fact_rows = tuple(
        sorted(
            (dict(row) for row in rows),
            key=lambda row: str(row["fact_id"]),
        )
    )
    fact_ids = tuple(str(row["fact_id"]) for row in fact_rows)
    return AuthoritativeResearchEpochFactLedger(
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        checkpoint_id="RESEARCH-EPOCH-CHECKPOINT-FIXTURE",
        checkpoint_hash="a" * 64,
        epoch_count=2,
        epoch_checkpoint_ids=("EPOCH-1", "EPOCH-2"),
        cumulative_fact_ids=fact_ids,
        current_fact_ids=fact_ids,
        retired_fact_ids=(),
        fact_rows=fact_rows,
    )


def _bundle(root: Path):
    fixture = _build_actual_shaped_journal(root)
    materials = validate_current_v5_fact_lineage_materials(
        journal_root=fixture["journal"],
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        archetype_id=ARCHETYPE,
        current_documents=fixture["current_documents"],
        current_fact_prompt_payload=fixture["current_prompt_payload"],
    )
    recovered_claims, _recovered_dispositions, recovered_compilation = (
        _official_replay(materials)
    )
    accounted_prompt = _prompt_document(
        "SGDOC-ACCOUNTED",
        "OBJECTIVE-ACCOUNTED",
    )
    accounted_prompt["content_text"] = " ".join(
        f"Persisted statement {index}." for index in range(457)
    )
    accounted_document = _current_document(accounted_prompt)
    accounted_sibling_prompt = next(
        dict(document)
        for payload in fixture["payloads"]
        for document in payload["full_documents"]
        if str(document["document_id"]).startswith("SGDOC-STALE-")
    )
    accounted_sibling_document = _current_document(
        accounted_sibling_prompt
    )
    prior_claims = _persisted_claims(
        recovered_claims[0],
        accounted_document,
    )
    prior_compilation = EvidenceFactCompiler().compile(
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        accepted_claims=prior_claims,
    )
    assert len(prior_compilation.facts) == 457
    authority = _ledger(
        (
            *(row.to_dict() for row in prior_compilation.facts),
            *(row.to_dict() for row in recovered_compilation.facts),
        )
    )
    disposition = {
        "schema_version": "e2r_v5_fact_document_disposition_v1",
        "extraction_semantics_version": FACT_EXTRACTION_SEMANTICS_VERSION,
        "batch_id": "FACTBATCH-PERSISTED",
        "document_id": accounted_document["document_id"],
        "status": "FACTS_EXTRACTED",
        "rationale": "persisted fixture claims were already audited",
        "accepted_fact_count": len(prior_claims),
        "source_absence_proven": False,
        "production_score_authority": False,
    }
    sibling_disposition = {
        **disposition,
        "batch_id": "FACTBATCH-ACCOUNTED-SIBLING",
        "document_id": accounted_sibling_document["document_id"],
        "status": "NO_MATERIAL_FACT",
        "rationale": "already-accounted historical sibling",
        "accepted_fact_count": 0,
    }
    prior_call = FactExtractionProviderCall(
        batch_id="FACTBATCH-PERSISTED",
        status="COMPLETE",
        document_ids=(accounted_document["document_id"],),
        accepted_claim_ids=tuple(row["claim_id"] for row in prior_claims),
        rejected_proposal_count=0,
        document_dispositions=(disposition,),
        pending_reasons=(),
        research_gap_feedback=(),
        provider_name="COLLABORATION_CODEX_SUBAGENT",
        prompt_hash="FACTPROMPT-PERSISTED",
        response_hash="FACTRESP-PERSISTED",
        provider_attempt_count=1,
        accepted_claims=prior_claims,
    )
    sibling_call = FactExtractionProviderCall(
        batch_id="FACTBATCH-ACCOUNTED-SIBLING",
        status="COMPLETE",
        document_ids=(accounted_sibling_document["document_id"],),
        accepted_claim_ids=(),
        rejected_proposal_count=0,
        document_dispositions=(sibling_disposition,),
        pending_reasons=(),
        research_gap_feedback=(),
        provider_name="COLLABORATION_CODEX_SUBAGENT",
        prompt_hash="FACTPROMPT-ACCOUNTED-SIBLING",
        response_hash="FACTRESP-ACCOUNTED-SIBLING",
        provider_attempt_count=1,
        accepted_claims=(),
    )
    documents = tuple(
        (
            *fixture["current_documents"],
            accounted_document,
            accounted_sibling_document,
        )
    )
    objectives = _objectives(documents)
    common = {
        "target_id": TARGET,
        "target_name": "Current Corp",
        "target_aliases": ("Current",),
        "archetype_id": ARCHETYPE,
        "as_of_date": AS_OF_DATE,
        "documents": documents,
        "open_objectives": objectives,
        "current_facts": authority.fact_rows,
        "score_gap_context": {},
        "prior_material_claims": prior_claims,
        "prior_document_dispositions": (
            disposition,
            sibling_disposition,
        ),
        "extraction_mode": "PRODUCTION_OBJECTIVE_LOCAL",
    }
    binding = resolve_current_fact_lineage_recovery_binding(
        authoritative_fact_ledger=authority,
        journal_root=fixture["journal"],
        **common,
    )
    return {
        "fixture": fixture,
        "authority": authority,
        "binding": binding,
        "common": common,
        "prior_calls": (prior_call, sibling_call),
        "prior_compilation": prior_compilation,
        "recovered_claims": recovered_claims,
    }


class CurrentFactLineageRecoveryTests(unittest.TestCase):
    def test_authority_recovery_keeps_known_v5_journal_semantics(self):
        self.assertIn(
            LEGACY_FACT_EXTRACTION_SEMANTICS_VERSION,
            AUTHORITY_RECOVERY_FACT_SEMANTICS_VERSIONS,
        )
        binding = CurrentFactLineageRecoveryBinding(
            journal_root=".",
            seed_source_document_ids=("SGDOC-HISTORICAL",),
            journal_request_ids=("COLLABREQ-" + "a" * 64,),
            journal_response_ids=("COLLABRESP-" + "b" * 64,),
            fact_extraction_semantics_version=(
                LEGACY_FACT_EXTRACTION_SEMANTICS_VERSION
            ),
        )
        self.assertEqual(
            binding.fact_extraction_semantics_version,
            LEGACY_FACT_EXTRACTION_SEMANTICS_VERSION,
        )
        with self.assertRaisesRegex(
            ValueError,
            "current fact lineage recovery semantics are unsupported",
        ):
            CurrentFactLineageRecoveryBinding(
                journal_root=".",
                seed_source_document_ids=("SGDOC-HISTORICAL",),
                journal_request_ids=("COLLABREQ-" + "a" * 64,),
                journal_response_ids=("COLLABRESP-" + "b" * 64,),
                fact_extraction_semantics_version="UNKNOWN-HISTORICAL-VERSION",
            )

    def test_committed_known_historical_recovery_receipt_remains_readable(self):
        historical = {
            "batch_id": "FACTBATCH-HISTORICAL",
            "status": "COMPLETE",
            "document_ids": ["SGDOC-HISTORICAL"],
            "accepted_claim_ids": [],
            "rejected_proposal_count": 0,
            "document_dispositions": [],
            "pending_reasons": [],
            "research_gap_feedback": [],
            "provider_name": "COLLABORATION_CODEX_SUBAGENT",
            "prompt_hash": "FACTPROMPT-HISTORICAL",
            "response_hash": "FACTRESP-HISTORICAL",
            "provider_attempt_count": 0,
            "current_lineage_request_ids": ["COLLABREQ-" + "a" * 64],
            "current_lineage_response_ids": ["COLLABRESP-" + "b" * 64],
            "current_lineage_original_batch_document_ids": [
                "SGDOC-HISTORICAL"
            ],
            "extraction_semantics_version": (
                "e2r_v5_structured_valuation_roles_v5"
            ),
        }

        restored = _coerce_provider_call(historical)

        self.assertEqual(restored.provider_attempt_count, 0)
        self.assertEqual(
            restored.extraction_semantics_version,
            "e2r_v5_structured_valuation_roles_v5",
        )
        with self.assertRaisesRegex(
            ValueError,
            "current fact lineage recovery receipts are invalid",
        ):
            _coerce_provider_call(
                {
                    **historical,
                    "extraction_semantics_version": "UNKNOWN-HISTORICAL-VERSION",
                }
            )

    def test_authority_recovery_selects_exact_prior_semantics_without_unneeded_rewrite(
        self,
    ):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal = root / "collaboration_codex_subagent_provider"
            transport = CollaborationCodexSubagentTransport()
            transport.configure_journal_root(journal)
            prompt_document = _prompt_document(
                "SGDOC-SEMANTICS-UPGRADE",
                "OBJECTIVE-SEMANTICS-UPGRADE",
            )
            prompt_document.update(
                {
                    "canonical_url": (
                        "https://broker.example/semantics-upgrade.pdf"
                    ),
                    "source_family": "PUBLIC_BROKER_PDF",
                    "source_independence_group": (
                        "PUBLIC_BROKER_PDF:broker.example"
                    ),
                }
            )
            current_document = _current_document(prompt_document)
            old_response = _response(
                [prompt_document],
                [
                    _proposal(
                        prompt_document,
                        claim_index=700,
                        quote_index=0,
                    ),
                    _proposal(
                        prompt_document,
                        claim_index=701,
                        quote_index=1,
                    ),
                ],
            )
            old_payload = _prompt_payload(
                [prompt_document],
                marker="prior-semantics-authority",
                semantics_version=(
                    PRIOR_FACT_EXTRACTION_SEMANTICS_VERSION
                ),
            )
            _write_pair(
                transport,
                journal,
                payload=old_payload,
                response=old_response,
                agent_model="codex-collaboration",
            )
            old_request = next(
                json.loads(path.read_text(encoding="utf-8"))
                for path in (journal / "requests").glob("COLLABREQ-*.json")
            )
            old_roles = old_request["output_schema"]["properties"]["facts"][
                "items"
            ]["properties"]["structured_evidence_roles"]["items"]["enum"]
            self.assertIn("FORWARD_PB", old_roles)
            self.assertIn("EPS_REVISION", old_roles)
            self.assertIn("OPERATING_PROFIT_REVISION", old_roles)
            self.assertNotIn(
                "LATEST_ACTUAL_DEPRECIATION_AMORTIZATION",
                old_roles,
            )
            current_payload = _prompt_payload(
                [prompt_document],
                marker="current-semantics-rewrite",
            )
            _write_pair(
                transport,
                journal,
                payload=current_payload,
                response=_response(
                    [prompt_document],
                    [
                        _proposal(
                            prompt_document,
                            claim_index=799,
                            quote_index=2,
                        )
                    ],
                ),
                agent_model="codex-collaboration",
            )
            prior_materials = validate_current_v5_fact_lineage_materials(
                journal_root=journal,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=(current_document,),
                current_fact_prompt_payload=current_payload,
                fact_extraction_semantics_version=(
                    PRIOR_FACT_EXTRACTION_SEMANTICS_VERSION
                ),
            )
            old_claims, _dispositions, old_compilation = _official_replay(
                prior_materials
            )
            authority = _ledger(
                tuple(row.to_dict() for row in old_compilation.facts)
            )
            common = {
                "target_id": TARGET,
                "target_name": "Current Corp",
                "target_aliases": ("Current",),
                "archetype_id": ARCHETYPE,
                "as_of_date": AS_OF_DATE,
                "documents": (current_document,),
                "open_objectives": _objectives((current_document,)),
                "current_facts": authority.fact_rows,
                "score_gap_context": {},
                "prior_material_claims": (),
                "prior_document_dispositions": (),
                "extraction_mode": "PRODUCTION_OBJECTIVE_LOCAL",
            }
            binding = resolve_current_fact_lineage_recovery_binding(
                authoritative_fact_ledger=authority,
                journal_root=journal,
                **common,
            )
            provider = _NoCompleteProvider()
            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **common,
                authoritative_fact_ledger=authority,
                current_fact_lineage_recovery_binding=binding,
            )

        self.assertEqual(
            binding.fact_extraction_semantics_version,
            PRIOR_FACT_EXTRACTION_SEMANTICS_VERSION,
        )
        self.assertEqual(
            {
                row.extraction_semantics_version
                for row in result.provider_calls
                if row.current_lineage_request_ids
            },
            {PRIOR_FACT_EXTRACTION_SEMANTICS_VERSION},
        )
        self.assertEqual(provider.complete_call_count, 0)
        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(result.pending_reasons, ())
        self.assertEqual(
            {row["claim_id"] for row in old_claims},
            {row["claim_id"] for row in result.material_claims},
        )
        self.assertEqual(
            {row.fact_id for row in old_compilation.facts},
            {row.fact_id for row in result.facts},
        )
        self.assertEqual(
            result.audit["current_fact_lineage_recovery_status"],
            "COMPLETE",
        )
        self.assertEqual(
            result.audit["boundary_context_invalidated_prior_claim_count"],
            0,
        )

    def test_actual_shaped_13_seed_restores_52_dispositions_and_42_facts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = _bundle(root)
            binding = bundle["binding"]
            provider = _NoCompleteProvider()

            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **bundle["common"],
                prior_provider_calls=bundle["prior_calls"],
                authoritative_fact_ledger=bundle["authority"],
                current_fact_lineage_recovery_binding=binding,
            )

            self.assertEqual(len(binding.seed_source_document_ids), 13)
            self.assertEqual(len(binding.expected_recovery_document_ids), 52)
            self.assertEqual(len(binding.journal_request_ids), 6)
            self.assertEqual(provider.complete_call_count, 0)
            self.assertEqual(len(result.material_claims), 499)
            self.assertEqual(len(result.facts), 499)
            self.assertEqual(len(result.document_dispositions), 54)
            recovery_calls = [
                row for row in result.provider_calls
                if row.current_lineage_request_ids
            ]
            self.assertEqual(len(recovery_calls), 6)
            self.assertEqual(
                sum(len(row.document_ids) for row in recovery_calls),
                52,
            )
            self.assertEqual(
                sum(len(row.accepted_claim_ids) for row in recovery_calls),
                42,
            )
            accounted_sibling_id = "SGDOC-STALE-000"
            self.assertTrue(
                any(
                    accounted_sibling_id
                    in row.current_lineage_original_batch_document_ids
                    for row in recovery_calls
                )
            )
            self.assertTrue(
                all(
                    accounted_sibling_id not in row.document_ids
                    for row in recovery_calls
                )
            )
            self.assertTrue(
                all(row.provider_attempt_count == 0 for row in recovery_calls)
            )
            self.assertTrue(
                all(not row.semantics_migration_request_ids for row in recovery_calls)
            )
            self.assertEqual(
                {
                    document_id
                    for row in recovery_calls
                    for document_id in (
                        row.current_lineage_objective_reassessment_document_ids
                    )
                },
                {"SGDOC-CURRENT-000"},
            )
            tampered_call = dict(recovery_calls[0].to_dict())
            tampered_call[
                "current_lineage_objective_reassessment_document_ids"
            ] = ["SGDOC-OUTSIDE-CALL"]
            with self.assertRaisesRegex(
                ValueError,
                "current fact lineage recovery receipts are invalid",
            ):
                _coerce_provider_call(tampered_call)
            self.assertEqual(
                result.audit["current_fact_lineage_recovery_status"],
                "COMPLETE",
            )
            self.assertEqual(
                result.audit["current_fact_lineage_recovered_fact_count"],
                42,
            )
            self.assertEqual(
                result.audit[
                    "current_fact_lineage_provider_complete_call_count"
                ],
                0,
            )
            self.assertEqual(
                result.audit["critical_counts"]["unaccounted_document_count"],
                0,
            )
            drift_ids = result.audit[
                "current_fact_lineage_objective_reassessment_document_ids"
            ]
            self.assertEqual(drift_ids, ["SGDOC-CURRENT-000"])
            self.assertIn(
                "SGDOC-CURRENT-000",
                result.audit["pending_coverage_refresh_document_ids"],
            )

            output = root / "checkpoint"
            write_researcher_fact_extraction_result(result, output)
            committed = _load_committed_fact_result_snapshot(
                output,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
            )
            self.assertTrue(committed["leaf_commit_complete"])
            self.assertFalse(committed["atomic_snapshot_repair_required"])
            self.assertEqual(committed["leaf_mismatch_names"], ())
            self.assertEqual(len(committed["facts"]), 499)
            self.assertEqual(len(committed["provider_calls"]), 8)
            source_graph = SimpleNamespace(
                evidence_documents=bundle["common"]["documents"],
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
            )
            reloaded = _load_fact_checkpoint(output, source_graph=source_graph)
            self.assertIn(
                "SGDOC-CURRENT-000",
                reloaded["prior_coverage_refresh_document_ids"],
            )
            self.assertEqual(
                reloaded[
                    "prior_current_lineage_objective_reassessment_document_ids"
                ],
                ("SGDOC-CURRENT-000",),
            )
            current_lineage_rows = [
                row
                for row in reloaded["prior_provider_calls"]
                if row.get("current_lineage_request_ids")
            ]
            self.assertEqual(len(current_lineage_rows), 6)
            self.assertTrue(
                all(
                    _coerce_provider_call(row).provider_attempt_count == 0
                    for row in current_lineage_rows
                )
            )

    def test_legacy_calls_migrate_only_embedded_claim_objective_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = _bundle(Path(directory))
            result = ResearcherEvidenceFactExtractor(
                provider=_NoCompleteProvider()
            ).extract(
                **bundle["common"],
                prior_provider_calls=bundle["prior_calls"],
                authoritative_fact_ledger=bundle["authority"],
                current_fact_lineage_recovery_binding=bundle["binding"],
            )
            serialized = dict(result.to_dict())
            legacy_calls = []
            for raw_call in serialized["provider_calls"]:
                call = dict(raw_call)
                if call.get("current_lineage_request_ids"):
                    call.pop(
                        "current_lineage_objective_reassessment_document_ids",
                        None,
                    )
                legacy_calls.append(call)
            legacy_audit = dict(serialized["audit"])
            legacy_audit[
                "current_fact_lineage_objective_reassessment_document_ids"
            ] = []
            legacy_audit["pending_coverage_refresh_document_ids"] = []
            legacy_result = {
                **serialized,
                "provider_calls": legacy_calls,
                "audit": legacy_audit,
            }
            tampered_legacy_call = next(
                dict(row)
                for row in legacy_calls
                if row.get("current_lineage_request_ids")
                and row.get("accepted_claims")
            )
            tampered_claims = [
                dict(row)
                for row in tampered_legacy_call["accepted_claims"]
            ]
            tampered_claims[0]["objective_ids"] = [
                "OBJECTIVE-NOT-IN-HISTORICAL-LINEAGE"
            ]
            tampered_legacy_call["accepted_claims"] = tampered_claims
            with self.assertRaisesRegex(
                ValueError,
                "lacks explicit historical lineage",
            ):
                _upgrade_current_lineage_objective_reassessment_receipts(
                    [tampered_legacy_call],
                    document_by_id={
                        row["document_id"]: row
                        for row in bundle["common"]["documents"]
                    },
                )
            current_documents = []
            for raw_document in bundle["common"]["documents"]:
                document = dict(raw_document)
                if document["document_id"] == "SGDOC-ACCOUNTED":
                    document["historical_objective_ids"] = list(
                        document["objective_ids"]
                    )
                    document["objective_ids"] = [
                        "OBJECTIVE-ACCOUNTED-CURRENT"
                    ]
                current_documents.append(document)
            checkpoint = _load_fact_checkpoint(
                Path(directory) / "unused",
                source_graph=SimpleNamespace(
                    target_id=TARGET,
                    as_of_date=AS_OF_DATE,
                    evidence_documents=tuple(current_documents),
                ),
                committed_fact_snapshot={
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "accepted_claims": serialized["material_claims"],
                    "document_dispositions": serialized[
                        "document_dispositions"
                    ],
                    "provider_calls": legacy_calls,
                    "rejections": serialized["rejections"],
                    "result": legacy_result,
                },
            )

        self.assertEqual(
            checkpoint[
                "prior_current_lineage_objective_reassessment_document_ids"
            ],
            ("SGDOC-CURRENT-000",),
        )
        self.assertIn(
            "SGDOC-CURRENT-000",
            checkpoint["prior_coverage_refresh_document_ids"],
        )
        self.assertNotIn(
            "SGDOC-ACCOUNTED",
            checkpoint[
                "prior_current_lineage_objective_reassessment_document_ids"
            ],
        )
        self.assertEqual(
            {
                document_id
                for row in checkpoint["prior_provider_calls"]
                if row.get("current_lineage_request_ids")
                for document_id in row.get(
                    "current_lineage_objective_reassessment_document_ids"
                )
                or ()
            },
            {"SGDOC-CURRENT-000"},
        )

    def test_partial_sealed_group_merges_zero_recovered_facts(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = _bundle(Path(directory))
            original = bundle["binding"]
            partial = CurrentFactLineageRecoveryBinding(
                journal_root=original.journal_root,
                seed_source_document_ids=original.seed_source_document_ids,
                journal_request_ids=original.journal_request_ids[:-1],
                journal_response_ids=original.journal_response_ids[:-1],
                expected_recovery_document_ids=(
                    original.expected_recovery_document_ids
                ),
            )
            provider = _NoCompleteProvider()

            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **bundle["common"],
                prior_provider_calls=bundle["prior_calls"],
                authoritative_fact_ledger=bundle["authority"],
                current_fact_lineage_recovery_binding=partial,
            )

            self.assertEqual(provider.complete_call_count, 0)
            self.assertEqual(
                result.audit["current_fact_lineage_recovery_status"],
                "PENDING",
            )
            self.assertEqual(
                result.audit["current_fact_lineage_recovered_fact_count"],
                0,
            )
            self.assertFalse(
                any(row.current_lineage_request_ids for row in result.provider_calls)
            )

    def test_ambiguous_second_valid_group_fails_binding_resolution(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = _bundle(root)
            fixture = bundle["fixture"]
            transport = CollaborationCodexSubagentTransport()
            transport.configure_journal_root(fixture["journal"])
            duplicate_payload = _prompt_payload(
                fixture["payloads"][0]["full_documents"],
                marker="ambiguous-second-valid-group",
            )
            _write_pair(
                transport,
                fixture["journal"],
                payload=duplicate_payload,
                response=fixture["responses"][0],
                agent_model="codex-collaboration",
            )

            with self.assertRaisesRegex(ValueError, "ambiguous"):
                resolve_current_fact_lineage_recovery_binding(
                    authoritative_fact_ledger=bundle["authority"],
                    journal_root=fixture["journal"],
                    **bundle["common"],
                )

    def test_redundant_partial_overlap_keeps_unique_atomic_cover(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = _bundle(root)
            fixture = bundle["fixture"]
            original = bundle["binding"]
            seed_document_id = original.seed_source_document_ids[0]
            seed_prompt_document = next(
                dict(document)
                for payload in fixture["payloads"]
                for document in payload["full_documents"]
                if document["document_id"] == seed_document_id
            )
            transport = CollaborationCodexSubagentTransport()
            transport.configure_journal_root(fixture["journal"])
            overlap_payload = _prompt_payload(
                [seed_prompt_document],
                marker="redundant-partial-overlap",
            )
            overlap_request_id = _write_pair(
                transport,
                fixture["journal"],
                payload=overlap_payload,
                response=_response(
                    [seed_prompt_document],
                    [
                        _proposal(
                            seed_prompt_document,
                            claim_index=990,
                            quote_index=10,
                        )
                    ],
                ),
                agent_model="codex-collaboration",
            )

            binding = resolve_current_fact_lineage_recovery_binding(
                authoritative_fact_ledger=bundle["authority"],
                journal_root=fixture["journal"],
                **bundle["common"],
            )

            self.assertEqual(
                binding.journal_request_ids,
                original.journal_request_ids,
            )
            self.assertNotIn(overlap_request_id, binding.journal_request_ids)
            self.assertEqual(
                binding.expected_recovery_document_ids,
                original.expected_recovery_document_ids,
            )

    def test_authority_gap_preserves_attested_persisted_enrichment(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = _bundle(Path(directory))
            claims = list(bundle["common"]["prior_material_claims"])
            corroborating_claim = dict(claims[0])
            corroborating_claim["exact_quote"] = (
                "Persisted statement 0. Persisted statement 1."
            )
            corroborating_claim["claim_id"] = stable_intelligence_id(
                "RFC",
                {
                    key: corroborating_claim[key]
                    for key in (
                        "target_id",
                        "as_of_date",
                        "document_id",
                        "question_family_id",
                        "subject_id",
                        "predicate_family",
                        "normalized_object",
                        "period",
                        "mechanism_scope_id",
                        "exact_quote",
                    )
                },
            )
            corroborating_claim["provider_prompt_hash"] = (
                stable_intelligence_id("FACTPROMPT", {"enrichment": 1})
            )
            corroborating_claim["provider_response_hash"] = (
                stable_intelligence_id("FACTRESP", {"enrichment": 1})
            )
            claims.append(corroborating_claim)
            enriched_compilation = EvidenceFactCompiler().compile(
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                accepted_claims=claims,
            )
            prior_rows = {
                row.fact_id: row.to_dict()
                for row in enriched_compilation.facts
            }
            current_rows = {
                str(row["fact_id"]): dict(row)
                for row in bundle["authority"].fact_rows
            }
            current_rows.update(prior_rows)
            common = {
                **bundle["common"],
                "current_facts": tuple(
                    current_rows[fact_id]
                    for fact_id in sorted(current_rows)
                ),
                "prior_material_claims": tuple(claims),
            }

            binding = resolve_current_fact_lineage_recovery_binding(
                authoritative_fact_ledger=bundle["authority"],
                journal_root=bundle["fixture"]["journal"],
                **common,
            )
            provider = _NoCompleteProvider()
            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **common,
                prior_provider_calls=bundle["prior_calls"],
                authoritative_fact_ledger=bundle["authority"],
                current_fact_lineage_recovery_binding=binding,
            )

            self.assertEqual(provider.complete_call_count, 0)
            self.assertEqual(
                result.audit["current_fact_lineage_recovery_status"],
                "COMPLETE",
            )
            self.assertEqual(
                {row.fact_id: row.to_dict() for row in result.facts},
                current_rows,
            )

    def test_recovery_closes_before_scheduling_new_documents(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = _bundle(root)
            documents = []
            for raw_document in bundle["common"]["documents"]:
                document = dict(raw_document)
                if document["document_id"] == "SGDOC-CURRENT-000":
                    document["objective_ids"] = list(
                        document["historical_objective_ids"]
                    )
                documents.append(document)
            documents.extend(
                _current_document(
                    _prompt_document(
                        f"SGDOC-NEW-{index}",
                        f"OBJECTIVE-NEW-{index}",
                    )
                )
                for index in range(2)
            )
            common = {
                **bundle["common"],
                "documents": tuple(documents),
                "open_objectives": _objectives(documents),
            }
            binding = resolve_current_fact_lineage_recovery_binding(
                authoritative_fact_ledger=bundle["authority"],
                journal_root=bundle["fixture"]["journal"],
                **common,
            )
            provider = _NoCompleteProvider()

            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **common,
                prior_provider_calls=bundle["prior_calls"],
                authoritative_fact_ledger=bundle["authority"],
                current_fact_lineage_recovery_binding=binding,
            )

            self.assertEqual(provider.complete_call_count, 0)
            self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
            self.assertEqual(
                result.pending_reasons,
                ("FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED",),
            )
            self.assertEqual(
                result.audit["current_fact_lineage_recovery_status"],
                "COMPLETE",
            )
            self.assertEqual(
                result.audit["current_fact_lineage_recovered_fact_count"],
                42,
            )
            self.assertEqual(result.audit["new_unprocessed_document_count"], 2)
            self.assertEqual(
                result.audit["critical_counts"]["unaccounted_document_count"],
                2,
            )
            output = root / "recovery-boundary-checkpoint"
            write_researcher_fact_extraction_result(result, output)
            persisted = json.loads(
                (output / "fact_extraction_result.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                persisted["pending_reasons"],
                ["FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED"],
            )

    def test_content_tamper_fails_closed_before_replay(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = _bundle(Path(directory))
            common = dict(bundle["common"])
            documents = [dict(row) for row in common["documents"]]
            documents[0]["content_text"] += " tampered"
            # Keeping the old content_hash proves exact content identity fails.
            common["documents"] = documents

            with self.assertRaisesRegex(ValueError, "content/hash"):
                resolve_current_fact_lineage_recovery_binding(
                    authoritative_fact_ledger=bundle["authority"],
                    journal_root=bundle["fixture"]["journal"],
                    **common,
                )

    def test_pending_new_fact_without_union_projection_blocks_recovery(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = _bundle(Path(directory))
            extra_claim = dict(bundle["common"]["prior_material_claims"][0])
            extra_claim.update(
                {
                    "claim_id": "RFC-PENDING-NEW",
                    "subject_id": "pending-new-subject",
                    "subject": "pending new subject",
                    "predicate": "pending new predicate",
                    "predicate_family": "pending_new_predicate",
                    "normalized_object": "pending_new_object",
                    "mechanism_scope_id": "PENDING-NEW-SCOPE",
                    "exact_quote": "Persisted statement 0.",
                }
            )
            claims = (*bundle["common"]["prior_material_claims"], extra_claim)
            pending_compilation = EvidenceFactCompiler().compile(
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                accepted_claims=claims,
            )
            pending_fact_ids = set(
                row.fact_id for row in pending_compilation.facts
            ) - set(bundle["authority"].current_fact_ids)
            self.assertEqual(len(pending_fact_ids), 1)
            original = bundle["binding"]
            binding = CurrentFactLineageRecoveryBinding(
                journal_root=original.journal_root,
                seed_source_document_ids=original.seed_source_document_ids,
                journal_request_ids=original.journal_request_ids,
                journal_response_ids=original.journal_response_ids,
                expected_recovery_document_ids=(
                    original.expected_recovery_document_ids
                ),
                pending_new_fact_ids=tuple(pending_fact_ids),
            )
            provider = _NoCompleteProvider()
            common = {**bundle["common"], "prior_material_claims": claims}

            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **common,
                prior_provider_calls=bundle["prior_calls"],
                authoritative_fact_ledger=bundle["authority"],
                current_fact_lineage_recovery_binding=binding,
            )

            self.assertEqual(provider.complete_call_count, 0)
            self.assertEqual(
                result.audit["current_fact_lineage_recovery_status"],
                "PENDING",
            )
            self.assertIn(
                "CURRENT_FACT_LINEAGE_AUTHORITY_PROJECTION_MISMATCH",
                "|".join(result.pending_reasons),
            )
            self.assertEqual(
                result.audit["current_fact_lineage_recovered_fact_count"],
                0,
            )

    def test_attested_pending_new_fact_merges_with_exact_authority_recovery(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = _bundle(Path(directory))
            extra_claim = dict(bundle["recovered_claims"][0])
            extra_claim.update(
                {
                    "claim_id": "RFC-PENDING-NEW-MIXED-RECOVERY",
                    "subject_id": "pending-new-mixed-recovery",
                    "subject": "pending new mixed recovery subject",
                    "predicate": "pending new mixed recovery predicate",
                    "predicate_family": "pending_new_mixed_recovery",
                    "normalized_object": "pending_new_mixed_recovery",
                    "mechanism_scope_id": "PENDING-NEW-MIXED-RECOVERY",
                    "exact_quote": "Current statement 0.",
                    "extraction_semantics_version": (
                        FACT_EXTRACTION_SEMANTICS_VERSION
                    ),
                }
            )
            claims = (*bundle["common"]["prior_material_claims"], extra_claim)
            pending_compilation = EvidenceFactCompiler().compile(
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                accepted_claims=claims,
            )
            pending_rows = {
                row.fact_id: row.to_dict()
                for row in pending_compilation.facts
                if row.fact_id not in bundle["authority"].current_fact_ids
            }
            self.assertEqual(len(pending_rows), 1)
            pending_fact_id = next(iter(pending_rows))
            current_rows = {
                str(row["fact_id"]): dict(row)
                for row in bundle["authority"].fact_rows
            }
            current_rows.update(pending_rows)
            pending_document_id = str(extra_claim["document_id"])
            pending_disposition = {
                **bundle["common"]["prior_document_dispositions"][0],
                "batch_id": "FACTBATCH-PENDING-NEW-MIXED-RECOVERY",
                "document_id": pending_document_id,
                "accepted_fact_count": 1,
                "rationale": "new semantics fact already committed",
                "extraction_semantics_version": (
                    FACT_EXTRACTION_SEMANTICS_VERSION
                ),
            }
            common = {
                **bundle["common"],
                "current_facts": tuple(
                    current_rows[fact_id] for fact_id in sorted(current_rows)
                ),
                "prior_material_claims": claims,
                "prior_document_dispositions": (
                    *bundle["common"]["prior_document_dispositions"],
                    pending_disposition,
                ),
            }

            binding = resolve_current_fact_lineage_recovery_binding(
                authoritative_fact_ledger=bundle["authority"],
                journal_root=bundle["fixture"]["journal"],
                pending_new_fact_ids=(pending_fact_id,),
                **common,
            )
            provider = _NoCompleteProvider()
            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **common,
                prior_provider_calls=bundle["prior_calls"],
                authoritative_fact_ledger=bundle["authority"],
                current_fact_lineage_recovery_binding=binding,
            )

            self.assertEqual(provider.complete_call_count, 0)
            self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
            self.assertIn(
                "FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED",
                result.pending_reasons,
            )
            self.assertEqual(
                result.audit["current_fact_lineage_recovery_status"],
                "COMPLETE",
            )
            self.assertEqual(
                result.audit["current_fact_lineage_expectation_status"],
                "AUTHORITY_LOSS_RECOVERY_WITH_PENDING_NEW_REQUIRED",
            )
            self.assertEqual(len(result.facts), 500)
            self.assertIn(pending_fact_id, {row.fact_id for row in result.facts})
            disposition_ids = [
                str(row["document_id"])
                for row in result.document_dispositions
            ]
            self.assertEqual(len(disposition_ids), len(set(disposition_ids)))
            self.assertEqual(disposition_ids.count(pending_document_id), 1)
            self.assertEqual(
                next(
                    row["rationale"]
                    for row in result.document_dispositions
                    if row["document_id"] == pending_document_id
                ),
                "new semantics fact already committed",
            )

    def test_self_and_cycle_in_persisted_claims_block_before_journal(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = _bundle(Path(directory))
            baseline = list(bundle["common"]["prior_material_claims"])
            compiled = EvidenceFactCompiler().compile(
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                accepted_claims=baseline[:2],
            )
            fact_id_by_claim = {
                row.claim_id: row.fact_id for row in compiled.claim_fact_links
            }
            first_fact_id = fact_id_by_claim[baseline[0]["claim_id"]]
            second_fact_id = fact_id_by_claim[baseline[1]["claim_id"]]
            cases = {
                "self": (
                    {**baseline[0], "supersedes_fact_ids": [first_fact_id]},
                    baseline[1],
                ),
                "cycle": (
                    {**baseline[0], "supersedes_fact_ids": [second_fact_id]},
                    {**baseline[1], "supersedes_fact_ids": [first_fact_id]},
                ),
            }
            for label, replacements in cases.items():
                with self.subTest(label=label):
                    claims = (
                        *replacements,
                        *baseline[2:],
                    )
                    provider = _NoCompleteProvider()
                    result = ResearcherEvidenceFactExtractor(
                        provider=provider
                    ).extract(
                        **{
                            **bundle["common"],
                            "prior_material_claims": claims,
                        },
                        prior_provider_calls=bundle["prior_calls"],
                        authoritative_fact_ledger=bundle["authority"],
                        current_fact_lineage_recovery_binding=bundle["binding"],
                    )
                    self.assertEqual(provider.complete_call_count, 0)
                    self.assertEqual(
                        result.audit["current_fact_lineage_recovery_status"],
                        "PENDING",
                    )
                    self.assertEqual(
                        result.audit[
                            "current_fact_lineage_recovered_fact_count"
                        ],
                        0,
                    )

    def test_split_document_with_ordered_continuation_replays_atomically(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal = root / "collaboration_codex_subagent_provider"
            transport = CollaborationCodexSubagentTransport()
            transport.configure_journal_root(journal)
            prompt_document = _prompt_document(
                "SGDOC-SPLIT",
                "OBJECTIVE-SPLIT",
            )
            current = _current_document(prompt_document)
            content = str(current["content_text"])
            split_at = content.index("SGDOC-SPLIT material statement 6.")

            def chunk(index, start, end):
                row = dict(current)
                chunk_text = content[start:end]
                row.update(
                    {
                        "content_text": chunk_text,
                        "transport_chunk_id": f"FACTCHUNK-SPLIT-{index}",
                        "transport_chunk_index": index,
                        "transport_chunk_count": 2,
                        "transport_chunk_start": start,
                        "transport_chunk_end": end,
                        "transport_chunk_content_hash": hashlib.sha256(
                            chunk_text.encode("utf-8")
                        ).hexdigest(),
                        "full_document_text_chars": len(content),
                    }
                )
                return row

            first_chunk = chunk(0, 0, split_at)
            second_chunk = chunk(1, split_at, len(content))
            first_base = _prompt_payload([first_chunk], marker="split-page-1")
            first_prompt = first_base["full_documents"][0]
            first_proposal = _proposal(
                first_prompt,
                claim_index=900,
                quote_index=0,
            )
            second_proposal = _proposal(
                first_prompt,
                claim_index=901,
                quote_index=1,
            )
            _write_pair(
                transport,
                journal,
                payload=first_base,
                response=_response(
                    [first_prompt],
                    [first_proposal],
                    complete=False,
                ),
                agent_model="codex-gpt-5.4",
            )
            continuation = {
                **first_base,
                "fact_extraction_continuation_context": {
                    "page_number": 2,
                    "page_fact_limit": 12,
                    "required_document_ids": ["SGDOC-SPLIT"],
                    "previously_accepted_facts": [
                        {
                            "document_id": first_proposal["document_id"],
                            "question_family_id": first_proposal[
                                "question_family_id"
                            ],
                            "subject_id": first_proposal["subject_id"],
                            "predicate_family": first_proposal[
                                "predicate_family"
                            ],
                            "normalized_object": first_proposal[
                                "normalized_object"
                            ],
                            "period": first_proposal["period"],
                            "direction": first_proposal["direction"],
                            "current_lifecycle": first_proposal[
                                "current_lifecycle"
                            ],
                            "objective_ids": first_proposal["objective_ids"],
                            "objective_relation": first_proposal[
                                "objective_relation"
                            ],
                            "exact_quote": first_proposal["exact_quote"],
                        }
                    ],
                    "instruction": _fact_extraction_continuation_context(
                        page_number=2,
                        required_document_ids=("SGDOC-SPLIT",),
                        accepted_claims=(first_proposal,),
                    )["instruction"],
                },
            }
            _write_pair(
                transport,
                journal,
                payload=continuation,
                response=_response(
                    [first_prompt],
                    [second_proposal],
                    complete=True,
                ),
                agent_model="codex-collaboration",
            )
            second_base = _prompt_payload(
                [second_chunk],
                marker="split-chunk-2",
            )
            second_prompt = second_base["full_documents"][0]
            third_proposal = _proposal(
                second_prompt,
                claim_index=902,
                quote_index=7,
            )
            _write_pair(
                transport,
                journal,
                payload=second_base,
                response=_response([second_prompt], [third_proposal]),
                agent_model="codex-collaboration",
            )
            current_prompt = _prompt_payload([current], marker="current")
            materials = validate_current_v5_fact_lineage_materials(
                journal_root=journal,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=[current],
                current_fact_prompt_payload=current_prompt,
                recovery_projection_document_ids=["SGDOC-SPLIT"],
            )
            self.assertEqual(
                materials["status"],
                "READY_FOR_OFFICIAL_SEMANTIC_REPLAY",
                materials,
            )
            grouped = {}
            for row in materials["materials"]:
                grouped.setdefault(row["lineage_call_group_id"], []).append(row)
            replayed = [
                _replay_current_fact_lineage_group(
                    group_id=group_id,
                    materials=rows,
                    target_id=TARGET,
                    as_of_date=AS_OF_DATE,
                    scope_contract=load_mechanism_scope_contracts()[ARCHETYPE],
                    provider_name=materials["provider_name"],
                    recovery_document_ids=frozenset({"SGDOC-SPLIT"}),
                )
                for group_id, rows in grouped.items()
            ]
            recovered_claims = tuple(
                claim for row in replayed for claim in row["material_claims"]
            )
            compilation = EvidenceFactCompiler().compile(
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                accepted_claims=recovered_claims,
            )
            self.assertEqual(len(recovered_claims), 3)
            self.assertEqual(len(compilation.facts), 3)
            authority = _ledger(row.to_dict() for row in compilation.facts)
            common = {
                "target_id": TARGET,
                "target_name": "Current Corp",
                "target_aliases": ("Current",),
                "archetype_id": ARCHETYPE,
                "as_of_date": AS_OF_DATE,
                "documents": (current,),
                "open_objectives": _objectives((current,)),
                "current_facts": authority.fact_rows,
                "score_gap_context": {},
                "prior_material_claims": (),
                "prior_document_dispositions": (),
                "extraction_mode": "PRODUCTION_OBJECTIVE_LOCAL",
            }
            binding = resolve_current_fact_lineage_recovery_binding(
                authoritative_fact_ledger=authority,
                journal_root=journal,
                **common,
            )
            provider = _NoCompleteProvider()
            result = ResearcherEvidenceFactExtractor(provider=provider).extract(
                **common,
                authoritative_fact_ledger=authority,
                current_fact_lineage_recovery_binding=binding,
            )

            self.assertEqual(provider.complete_call_count, 0)
            self.assertEqual(len(binding.seed_source_document_ids), 1)
            self.assertEqual(len(binding.expected_recovery_document_ids), 1)
            self.assertEqual(len(binding.journal_request_ids), 3)
            self.assertEqual(
                len(result.facts),
                3,
                (result.pending_reasons, result.audit),
            )
            self.assertEqual(len(result.document_dispositions), 1)
            self.assertEqual(len(result.provider_calls), 2)
            self.assertEqual(
                sorted(len(row.current_lineage_request_ids) for row in result.provider_calls),
                [1, 2],
            )
            self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")


if __name__ == "__main__":
    unittest.main()
