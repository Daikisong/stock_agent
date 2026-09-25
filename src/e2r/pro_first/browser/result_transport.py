"""Audited, bounded normalization for visible ResearchDossier envelopes.

This browser-layer helper has no importer/capture dependencies.  It validates
only transport syntax; dossier semantics remain the responsibility of the
normal parser, validator, verifier, and deterministic engines.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re


BEGIN = "E2R_RESEARCH_DOSSIER_JSON_BEGIN"
END = "E2R_RESEARCH_DOSSIER_JSON_END"
_TERMINAL_SENTINEL = re.compile(
    r"(?m)^(E2R_RESEARCH_DOSSIER_[A-Z_]+_END)[ \t]*$"
)


@dataclass(frozen=True)
class DossierTransportNormalization:
    raw_text: str
    normalized_text: str
    raw_hash: str
    normalized_hash: str
    operations: tuple[str, ...]

    @property
    def applied(self) -> bool:
        return bool(self.operations)


def normalize_visible_dossier_transport(
    text: str,
) -> DossierTransportNormalization:
    """Restore only one deleted terminal-sentinel character.

    The sentinel must be unique and the enclosed object must be strict JSON.
    Arbitrary spelling repairs, JSON edits, fence synthesis, and partial
    payload completion are forbidden.
    """

    if not isinstance(text, str):
        raise TypeError("visible dossier transport must be text")
    raw_hash = _sha256_text(text)
    unchanged = DossierTransportNormalization(
        raw_text=text,
        normalized_text=text,
        raw_hash=raw_hash,
        normalized_hash=raw_hash,
        operations=(),
    )
    if text.count(BEGIN) != 1 or text.count(END) != 0:
        return unchanged
    begin_end = text.index(BEGIN) + len(BEGIN)
    # ChatGPT can append UI-only citation labels after the sentinel.  They are
    # outside the envelope; uniqueness and strict payload parsing still bind
    # the recovered terminator.
    matches = list(_TERMINAL_SENTINEL.finditer(text, begin_end))
    if len(matches) != 1:
        return unchanged
    match = matches[0]
    observed = match.group(1)
    if not _is_exact_single_character_deletion(observed, END):
        return unchanged
    normalized = text[: match.start(1)] + END + text[match.end(1) :]
    if normalized.count(BEGIN) != 1 or normalized.count(END) != 1:
        return unchanged
    block = normalized[
        normalized.index(BEGIN) + len(BEGIN) : normalized.index(END, begin_end)
    ].strip()
    if block.startswith("```"):
        lines = block.splitlines()
        if len(lines) < 3 or not lines[-1].strip().startswith("```"):
            return unchanged
        block = "\n".join(lines[1:-1]).strip()
    lines = block.splitlines()
    if (
        len(lines) >= 2
        and lines[0].strip().casefold() == "json"
        and lines[1].lstrip().startswith("{")
    ):
        block = "\n".join(lines[1:]).strip()
    try:
        payload = json.loads(block)
    except json.JSONDecodeError:
        return unchanged
    if not isinstance(payload, dict):
        return unchanged
    operation = f"RESTORE_SINGLE_DELETED_DOSSIER_END_SENTINEL:{observed}->{END}"
    return DossierTransportNormalization(
        raw_text=text,
        normalized_text=normalized,
        raw_hash=raw_hash,
        normalized_hash=_sha256_text(normalized),
        operations=(operation,),
    )


def _is_exact_single_character_deletion(observed: str, expected: str) -> bool:
    if len(observed) + 1 != len(expected):
        return False
    return any(
        expected[:index] + expected[index + 1 :] == observed
        for index in range(len(expected))
    )


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


__all__ = [
    "DossierTransportNormalization",
    "normalize_visible_dossier_transport",
]
