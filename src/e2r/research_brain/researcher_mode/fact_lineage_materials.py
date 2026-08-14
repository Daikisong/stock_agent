"""Read-only validation for current-v5 fact lineage rematerialization.

This module intentionally does not write checkpoints and does not call a
provider.  It joins two immutable authority planes:

* the Collaboration request/response journal proves what Codex returned; and
* the append-only research-epoch ledger proves which fact ids remain current.

The extractor may consume the validated raw materials in a later phase.  This
module deliberately does *not* claim semantic completeness: the official
extractor response validator and EvidenceFactCompiler must replay these raw
materials before the ledger can issue an exact recovery receipt.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

from .collaboration_provider_bridge import (
    COLLABORATION_PROVIDER_NAME,
    CollaborationCodexSubagentTransport,
)
from .research_epoch import (
    ResearchEpochCheckpoint,
    _checkpoint_from_mapping,
    load_research_epoch_checkpoint,
)


CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION = (
    "e2r_v5_cross_objective_consolidated_actuals_v9"
)
PRE_CROSS_OBJECTIVE_FACT_EXTRACTION_SEMANTICS_VERSION = (
    "e2r_v5_structured_durable_visibility_roles_v8"
)
PRE_DURABLE_VISIBILITY_FACT_EXTRACTION_SEMANTICS_VERSION = (
    "e2r_v5_structured_scenario_input_roles_v7"
)
PRIOR_FACT_EXTRACTION_SEMANTICS_VERSION = (
    "e2r_v5_structured_revision_roles_v6"
)
LEGACY_FACT_EXTRACTION_SEMANTICS_VERSION = (
    "e2r_v5_structured_valuation_roles_v5"
)
AUTHORITY_RECOVERY_FACT_SEMANTICS_VERSIONS = (
    CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION,
    PRE_CROSS_OBJECTIVE_FACT_EXTRACTION_SEMANTICS_VERSION,
    PRE_DURABLE_VISIBILITY_FACT_EXTRACTION_SEMANTICS_VERSION,
    PRIOR_FACT_EXTRACTION_SEMANTICS_VERSION,
    LEGACY_FACT_EXTRACTION_SEMANTICS_VERSION,
)
_STATIC_OBJECTIVE_SCOPE_KEYS = (
    "mode",
    "allowed_objective_relations",
    "material_fact_definition",
    "completion_definition",
    "deterministic_validation_scope",
    "llm_owns_economic_relevance",
)
_HISTORICAL_COMPATIBLE_OBJECTIVE_SCOPE_KEYS = (
    "mode",
    "allowed_objective_relations",
    "llm_owns_economic_relevance",
)
_V9_ISSUER_CONSOLIDATED_TRANSACTION_TYPES = frozenset(
    {
        "CONSOLIDATED_REVENUE_ACTUAL",
        "CONSOLIDATED_OPERATING_PROFIT_ACTUAL",
        "CONSOLIDATED_NET_INCOME_ACTUAL",
        "CONSOLIDATED_OPERATING_CASH_FLOW_ACTUAL",
        "CONSOLIDATED_CAPEX_ACTUAL",
        "CONSOLIDATED_FREE_CASH_FLOW_ACTUAL",
    }
)
_V9_ISSUER_CONSOLIDATED_ECONOMIC_MECHANISMS = frozenset(
    {
        "CONSOLIDATED_EARNINGS_ACTUAL",
        "CONSOLIDATED_CASH_FLOW_ACTUAL",
    }
)
_DOCUMENT_IDENTITY_KEYS = (
    "document_id",
    "canonical_url",
    "title",
    "source_family",
    "published_at",
    "available_at",
    "source_independence_group",
    "full_fetch_performed",
    "snippet_used_as_document",
)


@dataclass(frozen=True)
class CurrentFactLineageRecoveryBinding:
    """Seal one recovery attempt to an exact immutable journal roster.

    ``seed_source_document_ids`` is the exact source-id set named by the
    missing authoritative facts.  The sealed historical calls expand that
    seed to their full current document intersection (for example, 13 fact
    source documents can restore the 52 dispositions from six atomic calls).
    A later valid call that happens to mention one seed cannot silently widen
    the recovery closure because its request/response ids are not sealed here.
    """

    journal_root: Path
    seed_source_document_ids: tuple[str, ...]
    journal_request_ids: tuple[str, ...]
    journal_response_ids: tuple[str, ...]
    expected_recovery_document_ids: tuple[str, ...] = ()
    pending_new_fact_ids: tuple[str, ...] = ()
    pending_new_source_document_ids: tuple[str, ...] = ()
    fact_extraction_semantics_version: str = (
        CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
    )
    schema_version: str = "e2r_v5_current_fact_lineage_recovery_binding_v1"

    def __post_init__(self) -> None:
        object.__setattr__(self, "journal_root", Path(self.journal_root))
        for field_name in (
            "seed_source_document_ids",
            "journal_request_ids",
            "journal_response_ids",
            "expected_recovery_document_ids",
            "pending_new_fact_ids",
            "pending_new_source_document_ids",
        ):
            values = tuple(
                str(value).strip() for value in getattr(self, field_name)
            )
            if any(not value for value in values) or len(values) != len(
                set(values)
            ):
                raise ValueError(
                    f"current fact lineage {field_name} must be unique"
                )
            object.__setattr__(self, field_name, values)
        if not self.seed_source_document_ids:
            raise ValueError(
                "current fact lineage recovery document roster is required"
            )
        if (
            self.fact_extraction_semantics_version
            not in AUTHORITY_RECOVERY_FACT_SEMANTICS_VERSIONS
        ):
            raise ValueError(
                "current fact lineage recovery semantics are unsupported"
            )
        if (
            not self.journal_request_ids
            or len(self.journal_request_ids)
            != len(self.journal_response_ids)
            or any(
                re.fullmatch(r"COLLABREQ-[0-9a-f]{64}", value) is None
                for value in self.journal_request_ids
            )
            or any(
                re.fullmatch(r"COLLABRESP-[0-9a-f]{64}", value) is None
                for value in self.journal_response_ids
            )
        ):
            raise ValueError(
                "current fact lineage journal receipt roster is invalid"
            )

    @property
    def journal_receipt_pairs(self) -> tuple[tuple[str, str], ...]:
        return tuple(zip(self.journal_request_ids, self.journal_response_ids))

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "journal_root": str(self.journal_root),
            "seed_source_document_ids": list(self.seed_source_document_ids),
            "journal_request_ids": list(self.journal_request_ids),
            "journal_response_ids": list(self.journal_response_ids),
            "expected_recovery_document_ids": list(
                self.expected_recovery_document_ids
            ),
            "pending_new_fact_ids": list(self.pending_new_fact_ids),
            "fact_extraction_semantics_version": (
                self.fact_extraction_semantics_version
            ),
            "production_score_authority": False,
        }


@dataclass(frozen=True)
class AuthoritativeResearchEpochFactLedger:
    """Validated append-only fact authority for one target and cutoff."""

    target_id: str
    as_of_date: str
    checkpoint_id: str
    checkpoint_hash: str
    epoch_count: int
    epoch_checkpoint_ids: tuple[str, ...]
    cumulative_fact_ids: tuple[str, ...]
    current_fact_ids: tuple[str, ...]
    retired_fact_ids: tuple[str, ...]
    fact_rows: tuple[Mapping[str, Any], ...]
    schema_version: str = "e2r_v5_authoritative_fact_ledger_v1"

    def recovery_expectation(
        self,
        *,
        persisted_fact_ids: Sequence[str],
        pending_new_fact_ids: Sequence[str] = (),
        pending_retired_fact_ids: Sequence[str] = (),
    ) -> Mapping[str, Any]:
        """Derive the only fact/claim/source set eligible for restoration."""

        persisted = _unique_nonempty_strings(
            persisted_fact_ids,
            label="persisted fact ids",
        )
        current = frozenset(self.current_fact_ids)
        pending_new = frozenset(
            _unique_nonempty_strings(
                pending_new_fact_ids,
                label="pending new fact ids",
            )
        )
        pending_retired = frozenset(
            _unique_nonempty_strings(
                pending_retired_fact_ids,
                label="pending retired fact ids",
            )
        )
        persisted_set = frozenset(persisted)
        outside_current = persisted_set - current
        if (
            pending_new != outside_current
            or pending_new.intersection(current)
            or not pending_retired.issubset(current)
            or pending_retired.intersection(persisted_set)
            or pending_retired.intersection(pending_new)
        ):
            raise ValueError(
                "persisted fact projection requires exact "
                "pending_new_fact_ids and pending_retired_fact_ids attestations"
            )
        fact_by_id = {
            str(row["fact_id"]): dict(row) for row in self.fact_rows
        }
        projected_current = current - pending_retired
        persisted_current = persisted_set.intersection(projected_current)
        missing_ids = tuple(sorted(projected_current - persisted_current))
        missing_rows = tuple(fact_by_id[fact_id] for fact_id in missing_ids)
        claim_ids = _row_string_union(missing_rows, "claim_ids")
        source_document_ids = _row_string_union(missing_rows, "source_ids")
        if missing_ids and pending_retired:
            status = (
                "AUTHORITY_LOSS_RECOVERY_WITH_PENDING_PROJECTION_REQUIRED"
            )
        elif missing_ids and pending_new:
            status = "AUTHORITY_LOSS_RECOVERY_WITH_PENDING_NEW_REQUIRED"
        elif missing_ids:
            status = "AUTHORITY_LOSS_RECOVERY_REQUIRED"
        elif pending_new and pending_retired:
            status = "PENDING_FACT_PROJECTION_EPOCH_COMMIT_REQUIRED"
        elif pending_new:
            status = "PENDING_NEW_FACT_EPOCH_COMMIT_REQUIRED"
        elif pending_retired:
            status = "PENDING_FACT_RETIREMENT_EPOCH_COMMIT_REQUIRED"
        else:
            status = "NO_AUTHORITY_LOSS"
        return {
            "schema_version": (
                "e2r_v5_authoritative_fact_recovery_expectation_v1"
            ),
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "research_epoch_checkpoint_id": self.checkpoint_id,
            "research_epoch_checkpoint_hash": self.checkpoint_hash,
            "status": status,
            "authoritative_current_fact_count": len(self.current_fact_ids),
            "persisted_current_fact_count": len(persisted_current),
            "pending_new_fact_count": len(pending_new),
            "pending_retired_fact_count": len(pending_retired),
            "expected_recovered_fact_count": len(missing_ids),
            "expected_recovered_claim_count": len(claim_ids),
            "expected_recovered_source_document_count": len(
                source_document_ids
            ),
            "persisted_fact_ids": list(sorted(persisted_current)),
            "pending_new_fact_ids": list(sorted(pending_new)),
            "pending_retired_fact_ids": list(sorted(pending_retired)),
            "projected_current_fact_ids": list(sorted(projected_current)),
            "expected_recovered_fact_ids": list(missing_ids),
            "expected_recovered_claim_ids": list(claim_ids),
            "expected_recovered_source_document_ids": list(
                source_document_ids
            ),
            "production_score_authority": False,
        }

    def exact_recovery_receipt(
        self,
        *,
        persisted_fact_ids: Sequence[str],
        recovered_fact_ids: Sequence[str],
        recovered_claim_ids: Sequence[str],
        pending_new_fact_ids: Sequence[str] = (),
        pending_retired_fact_ids: Sequence[str] = (),
    ) -> Mapping[str, Any]:
        """Require exact missing-set intersection before any future merge."""

        expectation = self.recovery_expectation(
            persisted_fact_ids=persisted_fact_ids,
            pending_new_fact_ids=pending_new_fact_ids,
            pending_retired_fact_ids=pending_retired_fact_ids,
        )
        if expectation["status"] not in {
            "AUTHORITY_LOSS_RECOVERY_REQUIRED",
            "AUTHORITY_LOSS_RECOVERY_WITH_PENDING_NEW_REQUIRED",
            "AUTHORITY_LOSS_RECOVERY_WITH_PENDING_PROJECTION_REQUIRED",
        }:
            raise ValueError(
                "fact lineage recovery is allowed only for an authority loss"
            )
        recovered_facts = _unique_nonempty_strings(
            recovered_fact_ids,
            label="recovered fact ids",
        )
        recovered_claims = _unique_nonempty_strings(
            recovered_claim_ids,
            label="recovered claim ids",
        )
        expected_facts = frozenset(
            expectation["expected_recovered_fact_ids"]
        )
        expected_claims = frozenset(
            expectation["expected_recovered_claim_ids"]
        )
        persisted = frozenset(expectation["persisted_fact_ids"])
        pending_new = frozenset(expectation["pending_new_fact_ids"])
        pending_retired = frozenset(
            expectation["pending_retired_fact_ids"]
        )
        if (
            frozenset(recovered_facts) != expected_facts
            or frozenset(recovered_claims) != expected_claims
            or persisted.intersection(recovered_facts)
            or persisted.union(recovered_facts)
            != frozenset(expectation["projected_current_fact_ids"])
            or pending_new.intersection(
                persisted.union(recovered_facts)
            )
        ):
            raise ValueError(
                "recovered fact lineage is not the exact authoritative gap"
            )
        return {
            "schema_version": (
                "e2r_v5_authoritative_fact_recovery_receipt_v1"
            ),
            "status": "EXACT_CURRENT_FACT_INTERSECTION",
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "research_epoch_checkpoint_id": self.checkpoint_id,
            "research_epoch_checkpoint_hash": self.checkpoint_hash,
            "authoritative_current_fact_count": len(self.current_fact_ids),
            "persisted_current_fact_count": len(persisted),
            "recovered_fact_count": len(recovered_facts),
            "recovered_claim_count": len(recovered_claims),
            "pending_new_fact_count": len(pending_new),
            "pending_retired_fact_count": len(pending_retired),
            "recovered_fact_ids": list(sorted(recovered_facts)),
            "recovered_claim_ids": list(sorted(recovered_claims)),
            "pending_new_fact_ids": list(sorted(pending_new)),
            "pending_retired_fact_ids": list(sorted(pending_retired)),
            "merged_current_fact_ids": list(
                sorted(persisted.union(recovered_facts))
            ),
            "merged_fact_ids": list(
                sorted(persisted.union(recovered_facts).union(pending_new))
            ),
            "exact_intersection": True,
            "production_score_authority": False,
        }


def load_authoritative_research_epoch_fact_ledger(
    target_root: str | Path,
    *,
    target_id: str,
    as_of_date: str,
) -> AuthoritativeResearchEpochFactLedger:
    """Validate the entire JSONL chain and its canonical checkpoint head."""

    clean_target = str(target_id).strip()
    clean_as_of = str(as_of_date).strip()
    if not clean_target:
        raise ValueError("authoritative fact ledger target id is required")
    date.fromisoformat(clean_as_of)
    root = Path(target_root)
    ledger_path = root / "research_epochs.jsonl"
    checkpoint_path = root / "research_epoch_checkpoint.json"
    raw_rows = _read_jsonl_objects(ledger_path)
    if not raw_rows:
        raise ValueError("research epoch ledger is empty")
    checkpoints: list[ResearchEpochCheckpoint] = []
    fact_by_id: dict[str, Mapping[str, Any]] = {}
    prior: ResearchEpochCheckpoint | None = None
    for index, raw in enumerate(raw_rows, start=1):
        checkpoint = _checkpoint_from_mapping(raw)
        if checkpoint.to_dict() != raw:
            raise ValueError("research epoch ledger row round-trip mismatch")
        if checkpoint.schema_version != "e2r_research_epoch_checkpoint_v3":
            raise ValueError("authoritative fact ledger requires checkpoint v3")
        if (
            checkpoint.target_id != clean_target
            or checkpoint.as_of_date != clean_as_of
            or checkpoint.epoch != index
        ):
            raise ValueError("research epoch target/date/sequence mismatch")
        expected_parent = prior.checkpoint_id if prior is not None else None
        if checkpoint.resumed_from_checkpoint_id != expected_parent:
            raise ValueError("research epoch checkpoint chain is broken")
        _validate_epoch_fact_delta(
            checkpoint=checkpoint,
            prior=prior,
            fact_by_id=fact_by_id,
        )
        checkpoints.append(checkpoint)
        prior = checkpoint

    head = load_research_epoch_checkpoint(checkpoint_path)
    if head.to_dict() != raw_rows[-1]:
        raise ValueError(
            "research epoch checkpoint is not the canonical JSONL head"
        )
    assert prior is not None
    if head.checkpoint_id != prior.checkpoint_id:
        raise ValueError("research epoch checkpoint head identity mismatch")
    missing_fact_bodies = set(head.cumulative_fact_ids) - set(fact_by_id)
    if missing_fact_bodies:
        raise ValueError("cumulative fact lineage lacks immutable fact bodies")
    current_rows = tuple(
        dict(fact_by_id[fact_id]) for fact_id in head.current_fact_ids
    )
    return AuthoritativeResearchEpochFactLedger(
        target_id=clean_target,
        as_of_date=clean_as_of,
        checkpoint_id=head.checkpoint_id,
        checkpoint_hash=head.checkpoint_hash,
        epoch_count=len(checkpoints),
        epoch_checkpoint_ids=tuple(
            row.checkpoint_id for row in checkpoints
        ),
        cumulative_fact_ids=tuple(head.cumulative_fact_ids),
        current_fact_ids=tuple(head.current_fact_ids),
        retired_fact_ids=tuple(head.retired_fact_ids),
        fact_rows=current_rows,
    )


def current_fact_semantics_contract(
    prompt_payload: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project the stable current-v5 semantics, excluding objective rosters."""

    if (
        prompt_payload.get("fact_extraction_semantics_version")
        != CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
    ):
        raise ValueError("fact lineage prompt does not use current semantics")
    normalization = prompt_payload.get("normalization_contract")
    mechanism = prompt_payload.get(
        "deterministic_mechanism_scope_contract"
    )
    objective_scope = prompt_payload.get("fact_extraction_scope_contract")
    if not all(
        isinstance(value, Mapping)
        for value in (normalization, mechanism, objective_scope)
    ):
        raise ValueError("fact lineage semantics contracts are incomplete")
    assert isinstance(objective_scope, Mapping)
    current_objective_scope_keys = (
        *_STATIC_OBJECTIVE_SCOPE_KEYS,
        "objective_coverage_scope",
    )
    if any(key not in objective_scope for key in current_objective_scope_keys):
        raise ValueError("fact lineage objective scope contract is incomplete")
    projection = {
        "fact_extraction_semantics_version": (
            CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
        ),
        "normalization_contract": dict(normalization),
        "deterministic_mechanism_scope_contract": dict(mechanism),
        "static_production_objective_scope_contract": {
            key: objective_scope[key] for key in current_objective_scope_keys
        },
    }
    return {
        **projection,
        "contract_hash": _canonical_hash(projection),
    }


def _fact_semantics_compatibility_contract(
    prompt_payload: Mapping[str, Any],
    *,
    expected_semantics_version: str,
) -> Mapping[str, Any]:
    """Project fields that must remain stable across a typed-role upgrade."""

    prompt_semantics_version = prompt_payload.get(
        "fact_extraction_semantics_version"
    )
    if expected_semantics_version not in (
        AUTHORITY_RECOVERY_FACT_SEMANTICS_VERSIONS
    ):
        raise ValueError("fact lineage recovery semantics identity mismatch")
    compatible_prompt_versions = {expected_semantics_version}
    if (
        expected_semantics_version
        != CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
    ):
        # A current prompt may be projected onto a sealed historical request.
        # This is a read-only compatibility comparison; the journal candidate
        # must still carry the exact requested historical semantics version.
        compatible_prompt_versions.add(
            CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
        )
    if prompt_semantics_version not in compatible_prompt_versions:
        raise ValueError("fact lineage recovery semantics identity mismatch")
    normalization = prompt_payload.get("normalization_contract")
    mechanism = prompt_payload.get(
        "deterministic_mechanism_scope_contract"
    )
    objective_scope = prompt_payload.get("fact_extraction_scope_contract")
    if not all(
        isinstance(value, Mapping)
        for value in (normalization, mechanism, objective_scope)
    ):
        raise ValueError("fact lineage semantics contracts are incomplete")
    assert isinstance(objective_scope, Mapping)
    objective_scope_keys = (
        (
            *_STATIC_OBJECTIVE_SCOPE_KEYS,
            "objective_coverage_scope",
        )
        if expected_semantics_version
        == CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
        else _HISTORICAL_COMPATIBLE_OBJECTIVE_SCOPE_KEYS
    )
    if any(key not in objective_scope for key in objective_scope_keys):
        raise ValueError("fact lineage objective scope contract is incomplete")
    mechanism_projection = dict(mechanism)
    if (
        expected_semantics_version
        != CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
    ):
        if (
            prompt_semantics_version
            == CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
            and not isinstance(
                mechanism_projection.get(
                    "issuer_consolidated_actual_fact_encoding"
                ),
                Mapping,
            )
        ):
            raise ValueError(
                "current fact lineage consolidated actual contract is missing"
            )
        mechanism_projection.pop(
            "issuer_consolidated_actual_fact_encoding",
            None,
        )
        mechanism_projection["allowed_transaction_types"] = [
            value
            for value in mechanism_projection.get(
                "allowed_transaction_types", ()
            )
            if value not in _V9_ISSUER_CONSOLIDATED_TRANSACTION_TYPES
        ]
        mechanism_projection["allowed_economic_mechanisms"] = [
            value
            for value in mechanism_projection.get(
                "allowed_economic_mechanisms", ()
            )
            if value not in _V9_ISSUER_CONSOLIDATED_ECONOMIC_MECHANISMS
        ]
    projection = {
        "normalization_contract": dict(normalization),
        "deterministic_mechanism_scope_contract": mechanism_projection,
        "static_production_objective_scope_contract": {
            key: objective_scope[key] for key in objective_scope_keys
        },
    }
    return {
        **projection,
        "contract_hash": _canonical_hash(projection),
    }


def validate_current_v5_fact_lineage_materials(
    *,
    journal_root: str | Path,
    target_id: str,
    as_of_date: str,
    archetype_id: str,
    current_documents: Sequence[Mapping[str, Any]],
    current_fact_prompt_payload: Mapping[str, Any],
    recovery_projection_document_ids: Sequence[str] | None = None,
    fact_extraction_semantics_version: str = (
        CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
    ),
) -> Mapping[str, Any]:
    """Validate raw journal batches for official semantic replay.

    The returned ``materials`` retain the original full historical batches so
    the extractor can replay every base/continuation response through its
    official ``_validate_response`` path.  This function does not call the
    compiler and never labels response proposals as accepted claims.
    """

    base = {
        "schema_version": "e2r_v5_current_fact_lineage_materials_v1",
        "target_id": str(target_id),
        "as_of_date": str(as_of_date),
        "archetype_id": str(archetype_id),
        "provider_name": COLLABORATION_PROVIDER_NAME,
        "production_score_authority": False,
    }
    try:
        date.fromisoformat(str(as_of_date))
        documents = _validated_current_documents(
            current_documents,
            target_id=str(target_id),
            as_of_date=str(as_of_date),
        )
        document_by_id = {
            str(row["document_id"]): row for row in documents
        }
        projection_ids = (
            tuple(document_by_id)
            if recovery_projection_document_ids is None
            else _unique_nonempty_strings(
                recovery_projection_document_ids,
                label="recovery projection document ids",
            )
        )
        if not projection_ids or not set(projection_ids).issubset(
            document_by_id
        ):
            raise ValueError(
                "fact lineage recovery projection is outside current documents"
            )
        semantics_contract = current_fact_semantics_contract(
            current_fact_prompt_payload
        )
        semantics_compatibility_contract = (
            _fact_semantics_compatibility_contract(
                current_fact_prompt_payload,
                expected_semantics_version=(
                    fact_extraction_semantics_version
                ),
            )
        )
        transport = CollaborationCodexSubagentTransport(
            journal_root=Path(journal_root)
        )
        journal = transport.validated_current_fact_lineage_journal_materials(
            target_id=str(target_id),
            as_of_date=str(as_of_date),
            archetype_id=str(archetype_id),
            document_ids=projection_ids,
            fact_extraction_semantics_version=(
                fact_extraction_semantics_version
            ),
        )
        if not isinstance(journal, Mapping):
            raise ValueError("current fact journal validator unavailable")
        if journal.get("recovery_material_status") == "INVALID":
            raise ValueError("current fact journal contains invalid lineage")
        raw_materials = journal.get("materials")
        if not isinstance(raw_materials, list):
            raise ValueError("current fact journal material roster is malformed")
        if journal.get("recovery_material_status") == "ABSENT":
            return {
                **base,
                "status": "ABSENT",
                "current_semantics_version": (
                    CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
                ),
                "current_semantics_contract_hash": semantics_contract[
                    "contract_hash"
                ],
                "request_count": 0,
                "response_count": 0,
                "lineage_call_group_count": 0,
                "historical_batch_document_count": 0,
                "current_document_count": 0,
                "stale_sibling_document_count": 0,
                "response_fact_proposal_count": 0,
                "current_document_ids": [],
                "current_document_material_occurrence_counts": {},
                "pending_request_ids": list(
                    journal.get("pending_request_ids") or ()
                ),
                "objective_binding_reassessment_pending_count": 0,
                "objective_lineage_reassessment": [],
                "materials": [],
                "atomic_all_or_nothing": True,
                "official_response_semantic_validation_required": True,
                "compiler_exact_intersection_required": True,
                "safe_to_materialize_facts": False,
            }
        candidates = tuple(
            _validate_candidate_material_group(
                material_group,
                target_id=str(target_id),
                as_of_date=str(as_of_date),
                archetype_id=str(archetype_id),
                current_document_by_id=document_by_id,
                recovery_projection_document_ids=frozenset(projection_ids),
                current_semantics_compatibility_contract=(
                    semantics_compatibility_contract
                ),
                recovery_semantics_version=(
                    fact_extraction_semantics_version
                ),
            )
            for material_group in _ordered_journal_material_groups(
                raw_materials
            )
        )
        objective_rows = tuple(
            row
            for candidate in candidates
            for row in candidate["objective_reassessment_rows"]
        )
        objective_by_document: dict[str, Mapping[str, Any]] = {}
        for row in objective_rows:
            document_id = str(row["document_id"])
            prior_row = objective_by_document.get(document_id)
            if prior_row is not None and prior_row != row:
                raise ValueError("objective reassessment metadata conflicts")
            objective_by_document[document_id] = row
        occurrence_count = {
            document_id: sum(
                document_id in candidate["current_document_ids"]
                for candidate in candidates
            )
            for document_id in projection_ids
        }
        if any(not count for count in occurrence_count.values()):
            raise ValueError(
                "journal lineage does not cover every requested current document"
            )
        material_rows = [
            {
                **dict(material),
                "current_document_ids": list(
                    candidate["current_document_ids"]
                ),
                "validated_current_document_ids": list(
                    candidate["validated_current_document_ids"]
                ),
                "already_accounted_sibling_document_ids": list(
                    candidate[
                        "already_accounted_sibling_document_ids"
                    ]
                ),
                "stale_sibling_document_ids": list(
                    candidate["stale_sibling_document_ids"]
                ),
                "lineage_call_group_id": candidate[
                    "lineage_call_group_id"
                ],
            }
            for candidate in candidates
            for material in candidate["materials"]
        ]
        return {
            **base,
            "status": "READY_FOR_OFFICIAL_SEMANTIC_REPLAY",
            "current_semantics_version": (
                CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION
            ),
            "recovery_semantics_version": (
                fact_extraction_semantics_version
            ),
            "current_semantics_contract_hash": semantics_contract[
                "contract_hash"
            ],
            "request_count": len(material_rows),
            "response_count": len(material_rows),
            "lineage_call_group_count": len(candidates),
            "historical_batch_document_count": sum(
                int(row["historical_document_count"])
                for row in candidates
            ),
            "current_document_count": len(projection_ids),
            "validated_current_document_count": len(document_by_id),
            "stale_sibling_document_count": sum(
                len(row["stale_sibling_document_ids"])
                for row in candidates
            ),
            "response_fact_proposal_count": sum(
                int(row["response_fact_proposal_count"])
                for row in candidates
            ),
            "current_document_ids": sorted(document_by_id),
            "current_document_material_occurrence_counts": occurrence_count,
            "pending_request_ids": list(
                journal.get("pending_request_ids") or ()
            ),
            "objective_binding_reassessment_pending_count": len(
                objective_by_document
            ),
            "objective_lineage_reassessment": [
                dict(row)
                for row in sorted(
                    objective_by_document.values(),
                    key=lambda row: str(row["document_id"]),
                )
            ],
            "materials": material_rows,
            "atomic_all_or_nothing": True,
            "official_response_semantic_validation_required": True,
            "compiler_exact_intersection_required": True,
            "safe_to_materialize_facts": False,
        }
    except (
        FileNotFoundError,
        OSError,
        KeyError,
        TypeError,
        ValueError,
        RuntimeError,
        json.JSONDecodeError,
    ) as exc:
        return {
            **base,
            "status": "INVALID",
            "invalid_reason": (
                f"{exc.__class__.__name__}:{' '.join(str(exc).split())}"
            )[:1000],
            "request_count": 0,
            "response_count": 0,
            "lineage_call_group_count": 0,
            "historical_batch_document_count": 0,
            "current_document_count": 0,
            "stale_sibling_document_count": 0,
            "response_fact_proposal_count": 0,
            "current_document_ids": [],
            "current_document_material_occurrence_counts": {},
            "pending_request_ids": [],
            "objective_binding_reassessment_pending_count": 0,
            "objective_lineage_reassessment": [],
            "materials": [],
            "atomic_all_or_nothing": True,
            "official_response_semantic_validation_required": True,
            "compiler_exact_intersection_required": True,
            "safe_to_materialize_facts": False,
        }


def _ordered_journal_material_groups(
    materials: Sequence[Any],
) -> tuple[tuple[Mapping[str, Any], ...], ...]:
    """Bind a base request and every ordered continuation page together."""

    grouped: dict[str, list[tuple[int, Mapping[str, Any]]]] = {}
    for raw in materials:
        if not isinstance(raw, Mapping):
            raise ValueError("fact lineage journal material must be an object")
        request_payload = raw.get("request_payload")
        if not isinstance(request_payload, Mapping):
            raise ValueError("fact lineage request payload is missing")
        context = request_payload.get("fact_extraction_continuation_context")
        retry_context = request_payload.get("fact_extraction_retry_context")
        if context is not None and retry_context is not None:
            raise ValueError(
                "fact lineage request has both continuation and retry context"
            )
        if context is None:
            page_number = raw.get("continuation_page_number") or 1
            if (
                isinstance(page_number, bool)
                or not isinstance(page_number, int)
                or page_number < 1
                or (retry_context is None and page_number != 1)
            ):
                raise ValueError("fact lineage material page is invalid")
            base_payload = dict(request_payload)
            base_payload.pop("fact_extraction_retry_context", None)
        else:
            if not isinstance(context, Mapping):
                raise ValueError("fact lineage continuation context is invalid")
            page_number = context.get("page_number")
            if (
                isinstance(page_number, bool)
                or not isinstance(page_number, int)
                or page_number < 2
            ):
                raise ValueError("fact lineage continuation page is invalid")
            base_payload = dict(request_payload)
            base_payload.pop("fact_extraction_continuation_context", None)
            if raw.get("continuation_page_number") != page_number:
                raise ValueError(
                    "fact lineage continuation page metadata drifted"
                )
        group_id = "FACTLINEAGECALL-" + _canonical_hash(base_payload)[:24]
        grouped.setdefault(group_id, []).append((page_number, dict(raw)))
    result: list[tuple[Mapping[str, Any], ...]] = []
    for group_id in sorted(grouped):
        rows = sorted(grouped[group_id], key=lambda item: item[0])
        pages = tuple(page for page, _ in rows)
        if pages != tuple(range(1, len(rows) + 1)):
            raise ValueError("fact lineage continuation pages are not contiguous")
        if len(pages) != len(set(pages)):
            raise ValueError("fact lineage continuation page is duplicated")
        result.append(tuple(row for _, row in rows))
    return tuple(result)


def _validate_candidate_material_group(
    materials: Sequence[Mapping[str, Any]],
    *,
    target_id: str,
    as_of_date: str,
    archetype_id: str,
    current_document_by_id: Mapping[str, Mapping[str, Any]],
    recovery_projection_document_ids: frozenset[str],
    current_semantics_compatibility_contract: Mapping[str, Any],
    recovery_semantics_version: str,
) -> Mapping[str, Any]:
    if not materials:
        raise ValueError("fact lineage journal call group is empty")
    first_request = materials[0].get("request_payload")
    if not isinstance(first_request, Mapping):
        raise ValueError("fact lineage base request payload is missing")
    request_payload = dict(first_request)
    if "fact_extraction_continuation_context" in request_payload:
        raise ValueError("fact lineage call group lacks its base request")
    request_payload.pop(
        "fact_extraction_retry_context",
        None,
    )
    if (
        request_payload.get("target_id") != target_id
        or request_payload.get("as_of_date") != as_of_date
        or request_payload.get("archetype_hypothesis") != archetype_id
        or _fact_semantics_compatibility_contract(
            request_payload,
            expected_semantics_version=recovery_semantics_version,
        )
        != current_semantics_compatibility_contract
    ):
        raise ValueError("fact lineage current semantics identity mismatch")
    raw_documents = request_payload.get("full_documents")
    if not isinstance(raw_documents, list) or not raw_documents:
        raise ValueError("fact lineage historical batch is missing")
    historical_by_id: dict[str, Mapping[str, Any]] = {}
    for raw in raw_documents:
        historical = _validated_historical_prompt_document(raw)
        document_id = str(historical["document_id"])
        if document_id in historical_by_id:
            raise ValueError("historical fact batch document ids are duplicated")
        historical_by_id[document_id] = historical
    validated_current_ids = tuple(
        sorted(set(historical_by_id).intersection(current_document_by_id))
    )
    current_ids = tuple(
        sorted(
            set(historical_by_id).intersection(
                recovery_projection_document_ids
            )
        )
    )
    if not current_ids:
        raise ValueError("fact lineage material has no recovery intersection")
    objective_rows: list[Mapping[str, Any]] = []
    for document_id in validated_current_ids:
        historical = historical_by_id[document_id]
        current = current_document_by_id[document_id]
        _validate_document_identity(historical=historical, current=current)
        historical_objectives = _mapping_string_tuple(
            historical,
            "objective_ids",
        )
        current_objectives = _mapping_string_tuple(current, "objective_ids")
        if historical_objectives != current_objectives:
            lineage = frozenset(
                (*current_objectives, *_mapping_string_tuple(
                    current,
                    "historical_objective_ids",
                ))
            )
            if not set(historical_objectives).issubset(lineage):
                raise ValueError(
                    "objective drift lacks explicit historical lineage"
                )
            objective_rows.append(
                {
                    "document_id": document_id,
                    "historical_objective_ids": list(
                        historical_objectives
                    ),
                    "current_objective_ids": list(current_objectives),
                    "status": "OBJECTIVE_BINDING_REASSESSMENT_REQUIRED",
                    "preserve_current_fact_lineage": True,
                    "production_score_authority": False,
                }
            )

    _historical_objective_scope(request_payload)
    response_fact_proposal_count = 0
    base_core = dict(request_payload)
    for page_index, material in enumerate(materials, start=1):
        page_request = material.get("request_payload")
        response_payload = material.get("response_payload")
        if not isinstance(page_request, Mapping) or not isinstance(
            response_payload, Mapping
        ):
            raise ValueError("fact lineage request/response payload is missing")
        page_core = dict(page_request)
        context = page_core.pop(
            "fact_extraction_continuation_context",
            None,
        )
        retry_context = page_core.pop(
            "fact_extraction_retry_context",
            None,
        )
        if context is not None and retry_context is not None:
            raise ValueError(
                "fact lineage page has both continuation and retry context"
            )
        if page_core != base_core:
            raise ValueError("fact lineage continuation base payload drifted")
        if page_index == 1:
            if context is not None:
                raise ValueError("fact lineage first page is a continuation")
            if retry_context is not None:
                _validate_retry_context(
                    retry_context,
                    historical_document_ids=frozenset(historical_by_id),
                )
        else:
            if retry_context is not None:
                _validate_retry_context(
                    retry_context,
                    historical_document_ids=frozenset(historical_by_id),
                )
            else:
                _validate_continuation_context(
                    context,
                    page_number=page_index,
                    historical_document_ids=frozenset(historical_by_id),
                )
        facts = response_payload.get("facts")
        dispositions = response_payload.get("document_dispositions")
        unresolved = response_payload.get("unresolved_document_ids")
        notes = response_payload.get("unresolved_research_notes")
        if any(
            not isinstance(value, list)
            for value in (facts, dispositions, unresolved, notes)
        ):
            raise ValueError("fact lineage response arrays are malformed")
        assert isinstance(facts, list)
        assert isinstance(dispositions, list)
        assert isinstance(unresolved, list)
        if any(not isinstance(row, Mapping) for row in facts) or any(
            not isinstance(row, Mapping) for row in dispositions
        ):
            raise ValueError("fact lineage response rows are malformed")
        response_fact_proposal_count += len(facts)
        final_page = page_index == len(materials)
        if final_page:
            if unresolved or response_payload.get("extraction_complete") is not True:
                raise ValueError("fact lineage final page is not terminal")
        else:
            declared_open = (
                response_payload.get("extraction_complete") is False
                and bool(unresolved)
                and set(str(value) for value in unresolved).issubset(
                    historical_by_id
                )
            )
            full_page_requires_confirmation = (
                len(facts) >= 12
                and response_payload.get("extraction_complete") is True
                and not unresolved
            )
            if not declared_open and not full_page_requires_confirmation:
                raise ValueError(
                    "fact lineage non-final page closed incorrectly"
                )
    stale_ids = tuple(
        sorted(set(historical_by_id) - set(validated_current_ids))
    )
    accounted_sibling_ids = tuple(
        sorted(set(validated_current_ids) - set(current_ids))
    )
    return {
        "lineage_call_group_id": (
            "FACTLINEAGECALL-" + _canonical_hash(base_core)[:24]
        ),
        "materials": tuple(dict(row) for row in materials),
        "historical_document_count": len(historical_by_id),
        "current_document_ids": current_ids,
        "validated_current_document_ids": validated_current_ids,
        "already_accounted_sibling_document_ids": accounted_sibling_ids,
        "stale_sibling_document_ids": stale_ids,
        "response_fact_proposal_count": response_fact_proposal_count,
        "objective_reassessment_rows": tuple(objective_rows),
    }


def _validate_continuation_context(
    context: Any,
    *,
    page_number: int,
    historical_document_ids: frozenset[str],
) -> None:
    if not isinstance(context, Mapping):
        raise ValueError("fact lineage continuation context is missing")
    required_ids = context.get("required_document_ids")
    prior = context.get("previously_accepted_facts")
    if (
        context.get("page_number") != page_number
        or context.get("page_fact_limit") != 12
        or not isinstance(required_ids, list)
        or frozenset(str(value) for value in required_ids)
        != historical_document_ids
        or len(required_ids) != len(historical_document_ids)
        or not isinstance(prior, list)
    ):
        raise ValueError("fact lineage continuation context is malformed")


def _validate_retry_context(
    context: Any,
    *,
    historical_document_ids: frozenset[str],
) -> None:
    if not isinstance(context, Mapping):
        raise ValueError("fact lineage retry context is missing")
    rewrite_attempt = context.get("rewrite_attempt")
    validation_errors = context.get("validation_errors")
    required_ids = context.get("required_document_ids")
    prior = context.get("previously_accepted_facts")
    if (
        isinstance(rewrite_attempt, bool)
        or rewrite_attempt not in (1, 2)
        or context.get("maximum_rewrite_attempts") != 2
        or not isinstance(validation_errors, list)
        or not validation_errors
        or any(
            not isinstance(reason, str) or not reason.strip()
            for reason in validation_errors
        )
        or not isinstance(required_ids, list)
        or frozenset(str(value) for value in required_ids)
        != historical_document_ids
        or len(required_ids) != len(historical_document_ids)
        or not isinstance(prior, list)
        or any(not isinstance(row, Mapping) for row in prior)
    ):
        raise ValueError("fact lineage retry context is malformed")


def _validated_current_documents(
    documents: Sequence[Mapping[str, Any]],
    *,
    target_id: str,
    as_of_date: str,
) -> tuple[Mapping[str, Any], ...]:
    if isinstance(documents, (str, bytes)) or not isinstance(
        documents, Sequence
    ):
        raise TypeError("current fact lineage documents must be a sequence")
    rows = tuple(dict(row) for row in documents)
    ids = tuple(str(row.get("document_id") or "").strip() for row in rows)
    if (
        not rows
        or any(not value for value in ids)
        or len(ids) != len(set(ids))
    ):
        raise ValueError("current fact lineage document ids must be unique")
    for row in rows:
        if (
            row.get("target_id") != target_id
            or row.get("as_of_date") != as_of_date
            or row.get("full_fetch_performed") is not True
            or row.get("snippet_only") is True
            or row.get("snippet_used_as_document") is True
            or row.get("evidence_eligible") is not True
        ):
            raise ValueError("current fact lineage document scope is invalid")
        _validated_content_hash(row)
    return rows


def _validated_historical_prompt_document(
    value: Any,
) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError("historical fact prompt document must be an object")
    row = dict(value)
    if any(key not in row for key in _DOCUMENT_IDENTITY_KEYS):
        raise ValueError("historical fact prompt identity is incomplete")
    if (
        not str(row.get("document_id") or "").strip()
        or row.get("full_fetch_performed") is not True
        or row.get("snippet_used_as_document") is not False
    ):
        raise ValueError("historical fact prompt document is not full evidence")
    content = str(row.get("content_text") or "")
    if not content.strip():
        raise ValueError("historical fact prompt document content is empty")
    row["_validated_content_hash"] = hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()
    return row


def _validated_content_hash(row: Mapping[str, Any]) -> str:
    content = str(row.get("content_text") or "")
    actual = hashlib.sha256(content.encode("utf-8")).hexdigest()
    expected = (
        row.get("transport_chunk_content_hash")
        if int(row.get("transport_chunk_count") or 1) > 1
        else row.get("content_hash")
    )
    if not content.strip() or str(expected or "") != actual:
        raise ValueError("current fact lineage document content/hash mismatch")
    return actual


def _validate_document_identity(
    *,
    historical: Mapping[str, Any],
    current: Mapping[str, Any],
) -> None:
    for key in _DOCUMENT_IDENTITY_KEYS:
        if historical.get(key) != current.get(key):
            raise ValueError(f"fact lineage document identity mismatch:{key}")
    transport = historical.get("transport_chunk")
    if transport:
        if not isinstance(transport, Mapping):
            raise ValueError("fact lineage historical transport chunk invalid")
        current_content = str(current.get("content_text") or "")
        current_content_hash = _validated_content_hash(current)
        start = int(transport.get("start_char") or 0)
        end = int(transport.get("end_char") or 0)
        raw_chunk_index = transport.get("chunk_index")
        raw_chunk_count = transport.get("chunk_count")
        expected = {
            "start_char": start,
            "end_char": end,
            "chunk_content_hash": historical.get(
                "_validated_content_hash"
            ),
            "full_document_content_hash": current_content_hash,
            "full_document_text_chars": len(current_content),
        }
        if (
            start < 0
            or end <= start
            or end > len(current_content)
            or current_content[start:end]
            != str(historical.get("content_text") or "")
            or any(
                transport.get(key) != value
                for key, value in expected.items()
            )
            or not str(transport.get("transport_chunk_id") or "")
            or isinstance(raw_chunk_index, bool)
            or not isinstance(raw_chunk_index, int)
            or isinstance(raw_chunk_count, bool)
            or not isinstance(raw_chunk_count, int)
            or raw_chunk_count <= 1
            or raw_chunk_index < 0
            or raw_chunk_index >= raw_chunk_count
        ):
            raise ValueError("fact lineage transport chunk fields mismatch")
    elif historical.get("_validated_content_hash") != _validated_content_hash(
        current
    ):
        raise ValueError("fact lineage historical/current content hash mismatch")


def _historical_objective_scope(
    request_payload: Mapping[str, Any],
) -> Mapping[str, frozenset[str]] | None:
    scope = request_payload.get("fact_extraction_scope_contract")
    if scope is None:
        return None
    if not isinstance(scope, Mapping):
        raise ValueError("fact lineage objective scope must be an object")
    rows = scope.get("document_objective_ids")
    if not isinstance(rows, list):
        raise ValueError("fact lineage document objective scope is missing")
    result: dict[str, frozenset[str]] = {}
    for raw in rows:
        if not isinstance(raw, Mapping):
            raise ValueError("fact lineage objective scope row is invalid")
        document_id = str(raw.get("document_id") or "").strip()
        objective_ids = frozenset(
            _mapping_string_tuple(raw, "objective_ids")
        )
        if not document_id or not objective_ids or document_id in result:
            raise ValueError("fact lineage objective scope row is incomplete")
        result[document_id] = objective_ids
    prompt_ids = {
        str(row.get("document_id") or ""): frozenset(
            _mapping_string_tuple(row, "objective_ids")
        )
        for row in request_payload.get("full_documents") or ()
        if isinstance(row, Mapping)
    }
    if scope.get("objective_coverage_scope") == (
        "TARGET_WIDE_CURRENT_OPEN_OBJECTIVES"
    ):
        discovery_rows = scope.get("document_discovery_objective_ids")
        if not isinstance(discovery_rows, list):
            raise ValueError(
                "fact lineage discovery objective provenance is missing"
            )
        discovery_ids = {
            str(row.get("document_id") or ""): frozenset(
                _mapping_string_tuple(row, "objective_ids")
            )
            for row in discovery_rows
            if isinstance(row, Mapping)
        }
        if (
            discovery_ids != prompt_ids
            or set(result) != set(prompt_ids)
            or any(
                not discovery_ids[document_id].issubset(
                    result[document_id]
                )
                for document_id in result
            )
        ):
            raise ValueError(
                "fact lineage target-wide/discovery objective scope mismatch"
            )
    elif result != prompt_ids:
        raise ValueError("fact lineage prompt/objective scope mismatch")
    return result


def _validate_epoch_fact_delta(
    *,
    checkpoint: ResearchEpochCheckpoint,
    prior: ResearchEpochCheckpoint | None,
    fact_by_id: dict[str, Mapping[str, Any]],
) -> None:
    cumulative = tuple(checkpoint.cumulative_fact_ids)
    current = frozenset(checkpoint.current_fact_ids)
    retired = frozenset(checkpoint.retired_fact_ids)
    if (
        cumulative != tuple(sorted(cumulative))
        or tuple(checkpoint.current_fact_ids)
        != tuple(sorted(checkpoint.current_fact_ids))
        or tuple(checkpoint.retired_fact_ids)
        != tuple(sorted(checkpoint.retired_fact_ids))
    ):
        raise ValueError("research epoch fact ids are not canonical-sorted")
    new_rows = tuple(dict(row) for row in checkpoint.new_facts)
    new_ids = tuple(str(row.get("fact_id") or "").strip() for row in new_rows)
    if any(not value for value in new_ids) or len(new_ids) != len(
        set(new_ids)
    ):
        raise ValueError("research epoch new fact ids are invalid")
    prior_cumulative = frozenset(
        prior.cumulative_fact_ids if prior is not None else ()
    )
    if set(new_ids) != set(cumulative) - prior_cumulative:
        raise ValueError("research epoch new fact delta is not exact")
    if frozenset(cumulative) != prior_cumulative.union(new_ids):
        raise ValueError("research epoch cumulative facts are not append-only")
    for row, fact_id in zip(new_rows, new_ids):
        if (
            row.get("target_id") != checkpoint.target_id
            or row.get("as_of_date") != checkpoint.as_of_date
            or fact_id in fact_by_id
        ):
            raise ValueError("research epoch fact body identity is invalid")
        fact_by_id[fact_id] = row
    prior_current = frozenset(
        prior.current_fact_ids if prior is not None else ()
    )
    prior_retired = frozenset(
        prior.retired_fact_ids if prior is not None else ()
    )
    expected_retired_delta = prior_current - current
    retired_rows = tuple(checkpoint.retired_facts)
    retired_delta_ids = tuple(
        str(row.get("fact_id") or "").strip() for row in retired_rows
    )
    if (
        frozenset(retired_delta_ids) != expected_retired_delta
        or retired != (prior_retired.union(expected_retired_delta) - current)
    ):
        raise ValueError("research epoch retired fact delta is not exact")


def _read_jsonl_objects(path: Path) -> tuple[Mapping[str, Any], ...]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read append-only research epochs: {path}") from exc
    if any(not line.strip() for line in lines):
        raise ValueError("research epoch ledger contains a blank record")
    rows: list[Mapping[str, Any]] = []
    for line in lines:
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError("research epoch ledger contains invalid JSON") from exc
        if not isinstance(value, Mapping):
            raise ValueError("research epoch ledger record must be an object")
        rows.append(dict(value))
    return tuple(rows)


def _unique_nonempty_strings(
    values: Sequence[str],
    *,
    label: str,
) -> tuple[str, ...]:
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
        raise TypeError(f"{label} must be a sequence")
    result = tuple(str(value).strip() for value in values)
    if any(not value for value in result) or len(result) != len(set(result)):
        raise ValueError(f"{label} must be unique and nonempty")
    return result


def _row_string_union(
    rows: Sequence[Mapping[str, Any]],
    key: str,
) -> tuple[str, ...]:
    values: list[str] = []
    for row in rows:
        current = _mapping_string_tuple(row, key)
        if not current:
            raise ValueError(f"authoritative fact row lacks {key}")
        values.extend(current)
    return tuple(sorted(set(values)))


def _mapping_string_tuple(
    value: Mapping[str, Any],
    key: str,
) -> tuple[str, ...]:
    raw = value.get(key)
    if isinstance(raw, (str, bytes)) or not isinstance(raw, Sequence):
        return ()
    result = tuple(str(item).strip() for item in raw)
    if any(not item for item in result) or len(result) != len(set(result)):
        return ()
    return result


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


__all__ = [
    "AuthoritativeResearchEpochFactLedger",
    "CURRENT_FACT_EXTRACTION_SEMANTICS_VERSION",
    "CurrentFactLineageRecoveryBinding",
    "current_fact_semantics_contract",
    "load_authoritative_research_epoch_fact_ledger",
    "validate_current_v5_fact_lineage_materials",
]
