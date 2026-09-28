"""Requirement-level totality audit against the existing canonical roster."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
from typing import Any, Mapping

from .loader import CROSS_GUARD_IDS, default_contract_path
from .validator import ContractValidationError, validate_contract_catalog


def compile_contract_totality_audit(
    repo_root: str | Path,
    *,
    contract_path: str | Path | None = None,
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    canonical_payload = json.loads(
        (root / "configs/e2r_archetype_evidence_contracts_v12.json").read_text(
            encoding="utf-8"
        )
    )
    research_path = Path(contract_path) if contract_path else default_contract_path()
    research_payload = json.loads(research_path.read_text(encoding="utf-8"))
    validation_error = None
    try:
        validate_contract_catalog(research_payload)
    except ContractValidationError as error:
        validation_error = str(error)
    canonical_ids = {
        str(row["canonical_archetype_id"])
        for row in canonical_payload.get("contracts") or ()
    }
    research = tuple(research_payload.get("contracts") or ())
    research_ids = {str(row.get("archetype_id") or "") for row in research}
    missing = sorted(canonical_ids - research_ids)
    extra = sorted(research_ids - canonical_ids)
    required_unmapped = 0
    green_unmapped = 0
    guard_unmapped = 0
    question_without_scope = 0
    question_without_source = 0
    contract_without_counter = 0
    contract_without_adequacy = 0
    question_text_signatures = Counter()
    for contract in research:
        questions = tuple(contract.get("question_families") or ())
        mapped = {
            str(value)
            for question in questions
            for value in question.get("required_primitives") or ()
        }
        counter_mapped = {
            str(value)
            for question in questions
            if set(
                question.get("question_roles")
                or (question.get("question_role"),)
            ).intersection(
                {"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION", "GUARD_ONLY"}
            )
            or question.get("could_change_hard_break") is True
            for value in question.get("required_primitives") or ()
        }
        required_unmapped += len(set(contract.get("required_primitives") or ()) - mapped)
        green_unmapped += len(set(contract.get("green_gate_primitives") or ()) - mapped)
        guard_unmapped += len(set(contract.get("guard_primitives") or ()) - counter_mapped)
        question_without_scope += sum(
            not question.get("affected_component_ids")
            and "GUARD_ONLY"
            not in set(
                question.get("question_roles")
                or (question.get("question_role"),)
            )
            for question in questions
        )
        question_without_source += sum(
            not question.get("required_source_roles") for question in questions
        )
        contract_without_counter += not any(
            set(
                question.get("question_roles")
                or (question.get("question_role"),)
            ).intersection(
                {"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION", "GUARD_ONLY"}
            )
            for question in questions
        )
        contract_without_adequacy += not bool(contract.get("adequate_search_policy"))
        signature = tuple(
            "".join(
                character.casefold()
                for character in str(question.get("question_text") or "")
                if character.isalnum()
            )
            for question in questions
        )
        question_text_signatures[signature] += 1
    generic = sum(count - 1 for count in question_text_signatures.values() if count > 1)
    counters = {
        "canonical_contract_count": len(canonical_ids),
        "research_contract_count": len(research_ids),
        "missing_contract_count": len(missing),
        "extra_unknown_contract_count": len(extra),
        "required_primitive_unmapped_count": required_unmapped,
        "green_gate_primitive_unmapped_count": green_unmapped,
        "guard_primitive_unmapped_count": guard_unmapped,
        "question_without_scope_count": question_without_scope,
        "question_without_source_role_count": question_without_source,
        "contract_without_counter_hard_break_count": int(contract_without_counter),
        "contract_without_adequate_search_count": int(contract_without_adequacy),
        "generic_filler_contract_count": generic,
        "cross_guard_count": len(set(CROSS_GUARD_IDS).intersection(research_ids)),
    }
    critical_count = sum(
        value
        for key, value in counters.items()
        if key.endswith("_count")
        and key
        not in {
            "canonical_contract_count",
            "research_contract_count",
            "cross_guard_count",
        }
    ) + int(validation_error is not None)
    return {
        "schema_version": "e2r_pro_first_v2_contract_totality_audit_v1",
        "status": "PASS" if critical_count == 0 else "FAIL",
        "critical_count": critical_count,
        "counters": counters,
        "missing_contract_ids": missing,
        "extra_contract_ids": extra,
        "validation_error": validation_error,
        "cross_guard_ids": list(CROSS_GUARD_IDS),
    }


__all__ = ["compile_contract_totality_audit"]
