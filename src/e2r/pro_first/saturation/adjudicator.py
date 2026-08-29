"""Whole-dossier deterministic saturation adjudicator."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from ..ids import canonical_hash
from ..research_contracts import select_contract_bundle
from .fixpoint import NoNewRouteConfirmation
from .models import DeterministicQuestionBound, ResearchSaturationReceipt
from .question_closure import compile_question_closure_decision
from .snapshots import compile_verified_research_snapshot


_VERIFIER_INTEGRITY_FAILURE_CODES = frozenset(
    {
        "QUESTION_REFERENCES_UNKNOWN_FACT",
        "QUESTION_REFERENCES_UNVERIFIED_FACT",
        "QUESTION_REFERENCES_NONACTIVE_LINEAGE",
        "QUESTION_FACT_MISSING_SOURCE_LINEAGE",
        "PRO_CLAIMED_SOURCE_ROLE_UNVERIFIED",
        "TERMINAL_EVIDENCE_STATUS_HAS_NO_VERIFIED_FACT",
        "ECONOMIC_BRIDGE_UNVERIFIED",
        "COUNTER_STATUS_HAS_NO_VERIFIED_COUNTERFACT",
        "QUESTION_FACT_NOT_BOUND_TO_ROUTE_RECEIPT",
        "QUESTION_TO_SOURCE_LINKAGE_INCOMPLETE",
    }
)


class ResearchSaturationAdjudicator:
    def adjudicate(
        self,
        *,
        dossier: Mapping[str, Any],
        verified_fact_ids: Sequence[str],
        deterministic_bounds: Mapping[str, DeterministicQuestionBound] | None = None,
        fixpoint_confirmations: Sequence[NoNewRouteConfirmation] = (),
        verifier_repair_pending_ids: Sequence[str] = (),
        lifecycle_hard_break_pending_ids: Sequence[str] = (),
    ) -> ResearchSaturationReceipt:
        schema_version = str(dossier.get("schema_version") or "")
        if schema_version not in {
            "e2r_pro_research_dossier_v2",
            "e2r_pro_research_dossier_v3",
        }:
            raise ValueError("research saturation requires ResearchDossierV2/V3")
        selected = tuple(str(value) for value in dossier.get("selected_archetypes") or ())
        bundle = select_contract_bundle(selected)
        contracts_by_question = {
            str(question["question_family_id"]): (contract, question)
            for contract in bundle.contracts
            for question in contract["question_families"]
        }
        expected_mandatory = tuple(
            question_id
            for question_id, (_contract, question) in contracts_by_question.items()
            if question.get("mandatory_for_full_thesis") is True
        )
        results = tuple(dossier.get("question_family_results") or ())
        result_ids = tuple(
            str(row.get("question_family_id") or "") for row in results
        )
        if len(result_ids) != len(set(result_ids)):
            raise ValueError("duplicate question-family result ids are forbidden")
        unknown = set(result_ids) - set(contracts_by_question)
        if unknown:
            raise ValueError(f"question results escape selected contracts: {sorted(unknown)}")
        results_by_id = {
            str(row.get("question_family_id") or ""): row for row in results
        }
        missing = tuple(
            value for value in expected_mandatory if value not in results_by_id
        )
        fact_rows = tuple(
            row
            for collection in ("material_facts", "counterfacts", "resolution_facts")
            for row in dossier.get(collection) or ()
        )
        facts_by_id = {
            str(row.get("dossier_fact_id") or ""): row for row in fact_rows
        }
        snapshot = compile_verified_research_snapshot(dossier, verified_fact_ids)
        verified = frozenset(snapshot.verified_fact_ids)
        lineages = tuple(dossier.get("source_lineages") or ())
        source_documents = tuple(dossier.get("source_documents") or ())
        routes = tuple(dossier.get("search_route_receipts") or ())
        fact_snapshot_hash = snapshot.fact_snapshot_hash
        lineage_roster_hash = snapshot.accepted_lineage_roster_hash
        bounds = dict(deterministic_bounds or {})
        if set(bounds) - set(contracts_by_question):
            raise ValueError("deterministic bounds contain an unknown contract question")
        decisions_list = []
        for question_id in expected_mandatory:
            if question_id not in results_by_id:
                continue
            result = results_by_id[question_id]
            requested_route_ids = {
                str(value) for value in result.get("search_route_receipt_ids") or ()
            }
            attempted_roles = sorted(
                {
                    str(value)
                    for value in result.get("attempted_source_role_ids") or ()
                }
                | {
                    str(row.get("source_role_id") or "")
                    for row in routes
                    if str(row.get("route_receipt_id") or "")
                    in requested_route_ids
                }
            )
            attempted_roles_hash = canonical_hash(attempted_roles)
            current_confirmations = tuple(
                row
                for row in fixpoint_confirmations
                if row.question_family_id == question_id
                and row.fact_snapshot_hash == fact_snapshot_hash
                and row.accepted_lineage_roster_hash == lineage_roster_hash
                and row.attempted_source_roles_hash == attempted_roles_hash
            )
            decisions_list.append(
                compile_question_closure_decision(
                    question_contract=contracts_by_question[question_id][1],
                    question_result=result,
                    dossier_facts=fact_rows,
                    source_lineages=lineages,
                    source_documents=source_documents,
                    route_receipts=routes,
                    verified_fact_ids=verified,
                    deterministic_bound=bounds.get(question_id),
                    fixpoint_confirmations=current_confirmations,
                )
            )
        decisions = tuple(decisions_list)
        nonterminal = tuple(
            row.question_family_id
            for row in decisions
            if not row.terminal
        )
        public_material = tuple(
            row.question_family_id
            for row in decisions
            if row.deterministic_status
            in {"PUBLIC_SEARCHABLE", "UNKNOWN_ROUTE_NOT_YET_TESTED", "SOURCE_PENDING"}
            and row.materiality not in {"NON_MATERIAL", "MONITORING"}
        )
        # A terminal answer with adequate source search but broken fact/lineage
        # provenance is verifier work, not another public web search.  This
        # includes both fact-backed answers and an adequately searched absence
        # whose append-only audit row still points at a rejected historical
        # candidate.  Missing core source roles remain public acquisition gaps.
        # This ordering prevents an integrity defect from opening an endless
        # sequence of Pro searches that cannot repair the immutable ledger.
        integrity_repair_pending = tuple(
            row.question_family_id
            for row in decisions
            if row.terminal
            and row.route_adequacy.adequate
            and not row.missing_core_source_roles
            and (
                not row.question_to_source_linkage_complete
                or bool(
                    set(row.failure_codes).intersection(
                        _VERIFIER_INTEGRITY_FAILURE_CODES
                    )
                )
            )
        )
        repair_pending = tuple(
            dict.fromkeys(
                [
                    str(value)
                    for value in verifier_repair_pending_ids
                    if not any(
                        row.question_family_id == str(value)
                        and row.terminal
                        and row.deterministic_status
                        == "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH"
                        and row.route_adequacy.semantic_fixpoint
                        for row in decisions
                    )
                ]
                + [
                    row.question_family_id
                    for row in decisions
                    if row.deterministic_status == "VERIFIER_REPAIR_REQUIRED"
                ]
                + list(integrity_repair_pending)
            )
        )
        provider_parser = tuple(
            row.question_family_id
            for row in decisions
            if row.deterministic_status in {"PROVIDER_PENDING", "PARSER_PENDING"}
            or (
                row.gap_class == "CORE_SCORE_BLOCKER"
                and row.availability.availability_class
                in {"PROVIDER_BLOCKED", "PARSER_BLOCKED"}
            )
        )
        lifecycle_pending = tuple(
            dict.fromkeys(
                [str(value) for value in lifecycle_hard_break_pending_ids]
                + [
                    row.question_family_id
                    for row in decisions
                    if row.gap_class == "HARD_BREAK_GAP"
                    and row.deterministic_status == "CONTRADICTED_UNRESOLVED"
                ]
            )
        )
        linkage_incomplete = tuple(
            row.question_family_id
            for row in decisions
            if not row.question_to_source_linkage_complete
        )
        likely_nonpublic = tuple(
            row.question_family_id
            for row in decisions
            if row.status == "LIKELY_NONPUBLIC" and row.terminal
        )
        decisions_not_ready = tuple(
            row.question_family_id for row in decisions if not row.ready
        )
        saturation_valid = not any(
            (
                missing,
                nonterminal,
                public_material,
                repair_pending,
                provider_parser,
                lifecycle_pending,
                linkage_incomplete,
                decisions_not_ready,
            )
        )
        deterministic_status = _research_status(
            missing=missing,
            public_material=public_material,
            repair_pending=repair_pending,
            provider_parser=provider_parser,
            lifecycle_pending=lifecycle_pending,
            nonterminal=nonterminal,
            likely_nonpublic=likely_nonpublic,
            saturation_valid=saturation_valid,
        )
        target = dossier.get("target") or {}
        return ResearchSaturationReceipt(
            job_id=str(dossier.get("job_id") or ""),
            run_id=str(dossier.get("run_id") or ""),
            target_id=str(target.get("target_id") or target.get("symbol") or ""),
            as_of_date=str(dossier.get("as_of_date") or ""),
            conversation_id=str(dossier.get("conversation_id") or ""),
            selected_archetype_ids=selected,
            selected_contract_ids=bundle.contract_ids,
            question_decisions=decisions,
            expected_mandatory_question_ids=expected_mandatory,
            missing_mandatory_question_ids=missing,
            nonterminal_mandatory_question_ids=nonterminal,
            public_material_gap_question_ids=public_material,
            verifier_repair_pending_ids=repair_pending,
            provider_parser_core_pending_question_ids=provider_parser,
            lifecycle_hard_break_pending_ids=lifecycle_pending,
            source_linkage_incomplete_question_ids=linkage_incomplete,
            likely_nonpublic_question_ids=likely_nonpublic,
            deterministic_research_status=deterministic_status,
            pro_claimed_research_status=str(dossier.get("research_status") or ""),
            pro_status_diverged=(
                str(dossier.get("research_status") or "") != deterministic_status
            ),
            fact_snapshot_hash=fact_snapshot_hash,
            accepted_lineage_roster_hash=lineage_roster_hash,
            research_saturation_valid=saturation_valid,
            component_entry_allowed=saturation_valid,
        )


def _research_status(
    *,
    missing: tuple[str, ...],
    public_material: tuple[str, ...],
    repair_pending: tuple[str, ...],
    provider_parser: tuple[str, ...],
    lifecycle_pending: tuple[str, ...],
    nonterminal: tuple[str, ...],
    likely_nonpublic: tuple[str, ...],
    saturation_valid: bool,
) -> str:
    if provider_parser:
        return "PROVIDER_PENDING"
    if repair_pending:
        return "NEEDS_VERIFIER_REPAIR"
    if lifecycle_pending:
        return "NEEDS_COUNTER_SUPERSESSION"
    if missing or public_material or nonterminal:
        return "NEEDS_PUBLIC_GAP_CLOSURE"
    if saturation_valid and likely_nonpublic:
        return "COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER"
    if saturation_valid:
        return "COMPLETE"
    return "NEEDS_PUBLIC_GAP_CLOSURE"


__all__ = ["ResearchSaturationAdjudicator"]
