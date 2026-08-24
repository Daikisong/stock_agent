"""Bounded V2 transport-identity binding without touching research evidence."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Mapping

from ..ids import canonical_hash


INITIAL_CONVERSATION_PLACEHOLDER = "PENDING_INITIAL_CONVERSATION"


class DossierIdentityBindingError(ValueError):
    """A dossier cannot be bound to the captured browser/pass identity safely."""


@dataclass(frozen=True)
class BoundDossierIdentity:
    payload: Mapping[str, Any]
    before_hash: str
    after_hash: str
    operations: tuple[str, ...]


def bind_dossier_transport_identity(
    payload: Mapping[str, Any],
    *,
    conversation_id: str,
    research_pass_id: str | None,
    parent_pass_id: str | None,
    allow_initial_conversation_placeholder: bool,
    pass_name: str | None = None,
    prompt_hash: str | None = None,
    response_hash: str | None = None,
) -> BoundDossierIdentity:
    """Bind only the unknowable initial conversation id to capture identity.

    ChatGPT creates ``/c/<conversation_id>`` only after the first visible send,
    so the initial prompt cannot contain that value.  The raw capture stays
    immutable; this function replaces the one exact top-level placeholder only
    after capture has proved the actual conversation.  Facts, excerpts, URLs,
    question results, and pass identities are never rewritten.
    """

    before_hash = canonical_hash(payload)
    if payload.get("schema_version") != "e2r_pro_research_dossier_v2":
        return BoundDossierIdentity(
            payload=dict(payload),
            before_hash=before_hash,
            after_hash=before_hash,
            operations=("NON_V2_IDENTITY_BINDING_NOT_APPLICABLE",),
        )
    if not conversation_id.strip():
        raise DossierIdentityBindingError("captured V2 conversation id is required")
    actual_pass_id = str(payload.get("research_pass_id") or "")
    if research_pass_id is None or actual_pass_id != research_pass_id:
        raise DossierIdentityBindingError("V2 research pass id differs from durable pass")
    actual_parent = payload.get("parent_pass_id")
    if actual_parent != parent_pass_id:
        raise DossierIdentityBindingError("V2 parent pass id differs from durable lineage")

    current = str(payload.get("conversation_id") or "")
    bound = deepcopy(dict(payload))
    operations: list[str] = []
    if current == conversation_id:
        operations.append("CONVERSATION_ID_ALREADY_CAPTURE_BOUND")
    else:
        if not (
            allow_initial_conversation_placeholder
            and parent_pass_id is None
            and current == INITIAL_CONVERSATION_PLACEHOLDER
        ):
            raise DossierIdentityBindingError(
                "V2 conversation id is neither capture-bound nor the exact initial placeholder"
            )
        if _count_exact_string(payload, INITIAL_CONVERSATION_PLACEHOLDER) != 1:
            raise DossierIdentityBindingError(
                "initial conversation placeholder must occur only at the top level"
            )
        bound["conversation_id"] = conversation_id
        operations.append("BIND_INITIAL_CONVERSATION_ID_FROM_CAPTURE_RECEIPT")
    pass_values = (pass_name, prompt_hash, response_hash)
    if any(value is not None for value in pass_values):
        if not all(isinstance(value, str) and value for value in pass_values):
            raise DossierIdentityBindingError(
                "pass name, prompt hash, and response hash must be bound together"
            )
        if len(str(prompt_hash)) != 64 or len(str(response_hash)) != 64:
            raise DossierIdentityBindingError("durable pass hashes must be sha256")
        rows = list(bound.get("research_passes") or ())
        matching_indexes = [
            index
            for index, row in enumerate(rows)
            if str((row or {}).get("pass_id") or "") == research_pass_id
        ]
        if len(matching_indexes) > 1:
            raise DossierIdentityBindingError("current research pass occurs more than once")
        durable_row = {
            "pass_id": research_pass_id,
            "parent_pass_id": parent_pass_id,
            "pass_name": pass_name,
            "status": "COMPLETE",
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
        }
        if matching_indexes:
            rows[matching_indexes[0]] = durable_row
        else:
            rows.append(durable_row)
        bound["research_passes"] = rows
        operations.append("BIND_CURRENT_PASS_RECEIPT_FROM_DURABLE_CAPTURE")
    return BoundDossierIdentity(
        payload=bound,
        before_hash=before_hash,
        after_hash=canonical_hash(bound),
        operations=tuple(operations),
    )


def _count_exact_string(value: Any, needle: str) -> int:
    if isinstance(value, Mapping):
        return sum(_count_exact_string(child, needle) for child in value.values())
    if isinstance(value, (list, tuple)):
        return sum(_count_exact_string(child, needle) for child in value)
    return int(value == needle)


__all__ = [
    "BoundDossierIdentity",
    "DossierIdentityBindingError",
    "INITIAL_CONVERSATION_PLACEHOLDER",
    "bind_dossier_transport_identity",
]
