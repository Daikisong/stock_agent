"""Audited Codex collaboration-subagent fallback for Researcher Mode.

The repository process cannot invoke the surrounding Codex collaboration
tool.  This module therefore implements a deliberately asynchronous bridge:

1. an exact prompt and its dynamic JSON Schema are written to an immutable
   request journal;
2. an orchestrator delegates that request to a Codex collaboration subagent;
3. a dedicated importer validates and records the response in a separate
   namespace; and
4. a resumed Researcher Mode call consumes the validated response through the
   ordinary ``StructuredResearchProvider`` contract.

The journal is not a score or Stage authority and must never be populated by
writing the normal Codex CLI response cache directly.
"""

from __future__ import annotations

from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderResponse,
    StructuredProviderUnavailable,
)

from .component_researcher import (
    CANDIDATE_RANKING_PAGE_CANDIDATE_LIMIT,
    CodexResearcherProvider,
    _single_payload_request_material,
)
from .schemas import assert_blind_research_output


COLLABORATION_BRIDGE_SCHEMA_VERSION = (
    "e2r_v5_collaboration_codex_subagent_bridge_v1"
)
COLLABORATION_REQUEST_SCHEMA_VERSION = (
    "e2r_v5_collaboration_codex_subagent_request_v1"
)
COLLABORATION_RESPONSE_SCHEMA_VERSION = (
    "e2r_v5_collaboration_codex_subagent_response_v1"
)
COLLABORATION_PROVENANCE_ASSURANCE = (
    "ORCHESTRATOR_ATTESTED_NOT_CRYPTOGRAPHIC"
)
COLLABORATION_PROVIDER_NAME = (
    "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE"
)
CODEX_SUBAGENT_FALLBACK_PROVIDER_NAME = (
    "CODEX_STRUCTURED_RESEARCHER_WITH_COLLABORATION_SUBAGENT_FALLBACK"
)
_REQUEST_ID_RE = re.compile(r"^COLLABREQ-[0-9a-f]{64}$")
_RESPONSE_ID_RE = re.compile(r"^COLLABRESP-[0-9a-f]{64}$")
_AGENT_ID_RE = re.compile(r"^[A-Za-z0-9._:/-]{1,200}$")
_USAGE_LIMIT_RE = re.compile(r"\busage\s+limit\b", re.IGNORECASE)
_REQUEST_ENVELOPE_KEYS = frozenset(
    {
        "schema_version",
        "request_id",
        "request_identity",
        "provider_identity",
        "provider_identity_hash",
        "schema_name",
        "pass_name",
        "prompt",
        "prompt_hash",
        "output_schema",
        "output_schema_hash",
        "score_or_stage_authority",
        "production_score_authority",
        "response_import_required",
    }
)
_RESPONSE_ENVELOPE_KEYS = frozenset(
    {
        "schema_version",
        "response_id",
        "request_id",
        "prompt_hash",
        "output_schema_hash",
        "provider_identity_hash",
        "payload_hash",
        "payload",
        "provenance",
        "validation",
        "score_or_stage_authority",
        "production_score_authority",
    }
)


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(
        path,
        os.O_RDONLY | getattr(os, "O_DIRECTORY", 0),
    )
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _atomic_create_json(path: Path, value: Mapping[str, Any]) -> bool:
    """Durably create one immutable JSON object without overwriting a peer.

    The temporary file is complete and fsynced before the hard-link CAS.  A
    hard link is an atomic create-if-absent operation on the destination:
    exactly one concurrent writer can win and ``FileExistsError`` tells every
    loser to compare against that winner.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    temporary = Path(temporary_name)
    created = False
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            return False
        created = True
        _fsync_directory(path.parent)
        return True
    finally:
        temporary.unlink(missing_ok=True)
        if created:
            _fsync_directory(path.parent)


def _create_or_read_identical_json(
    path: Path,
    value: Mapping[str, Any],
) -> tuple[Mapping[str, Any], bool]:
    created = _atomic_create_json(path, value)
    if created:
        return dict(value), True
    existing = _read_json_object(path)
    return existing, False


@contextmanager
def _request_journal_lock(root: Path, request_id: str):
    if _REQUEST_ID_RE.fullmatch(str(request_id)) is None:
        raise ValueError("collaboration journal lock request id is invalid")
    lock_root = root / "locks"
    lock_root.mkdir(parents=True, exist_ok=True)
    lock_path = lock_root / f"{request_id}.lock"
    descriptor = os.open(
        lock_path,
        os.O_RDWR | os.O_CREAT,
        0o600,
    )
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


def _read_json_object(path: Path) -> Mapping[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid JSON object: {path}") from exc
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return dict(value)


def _draft202012_validate(
    *,
    payload: Mapping[str, Any],
    output_schema: Mapping[str, Any],
) -> None:
    try:
        from jsonschema import Draft202012Validator
        from jsonschema.exceptions import SchemaError
    except (ImportError, AttributeError) as exc:
        raise RuntimeError(
            "jsonschema>=4 with Draft202012Validator is required for "
            "collaboration response validation"
        ) from exc
    try:
        Draft202012Validator.check_schema(output_schema)
        errors = sorted(
            Draft202012Validator(output_schema).iter_errors(payload),
            key=lambda row: tuple(str(part) for part in row.absolute_path),
        )
    except SchemaError as exc:
        raise ValueError(
            "collaboration request contains an invalid Draft 2020-12 schema"
        ) from exc
    if errors:
        first = errors[0]
        location = "/".join(str(part) for part in first.absolute_path) or "$"
        raise ValueError(
            "collaboration response schema violation:"
            f"{location}:{' '.join(first.message.split())[:500]}"
        )


def _pass_name_from_schema_name(schema_name: str) -> str:
    prefix = "e2r_v5_"
    if not schema_name.startswith(prefix):
        raise ValueError("collaboration schema name is not an E2R v5 pass")
    pass_name = schema_name[len(prefix) :].upper()
    if not pass_name or re.fullmatch(r"[A-Z0-9_]+", pass_name) is None:
        raise ValueError("collaboration pass name is invalid")
    return pass_name


def _request_identity(
    *,
    pass_name: str,
    prompt_hash: str,
    output_schema_hash: str,
    provider_identity_hash: str,
) -> Mapping[str, str]:
    return {
        "pass_name": pass_name,
        "prompt_hash": prompt_hash,
        "output_schema_hash": output_schema_hash,
        "provider_identity_hash": provider_identity_hash,
    }


def _request_id(identity: Mapping[str, str]) -> str:
    return "COLLABREQ-" + _canonical_hash(identity)


def _validate_agent_provenance(
    *,
    agent_id: str,
    canonical_task_name: str,
    agent_model: str,
) -> Mapping[str, str]:
    clean_agent_id = str(agent_id).strip()
    clean_task = str(canonical_task_name).strip()
    clean_model = str(agent_model).strip()
    if _AGENT_ID_RE.fullmatch(clean_agent_id) is None:
        raise ValueError("collaboration agent_id is invalid")
    if (
        not clean_task.startswith("/root/")
        or _AGENT_ID_RE.fullmatch(clean_task) is None
    ):
        raise ValueError("collaboration canonical task name is invalid")
    if not clean_model or len(clean_model) > 200:
        raise ValueError("collaboration agent model is invalid")
    return {
        "agent_id": clean_agent_id,
        "canonical_task_name": clean_task,
        "agent_model": clean_model,
        "agent_surface": "CODEX_COLLABORATION_SUBAGENT",
        "provenance_assurance": COLLABORATION_PROVENANCE_ASSURANCE,
    }


@dataclass
class CollaborationCodexSubagentTransport:
    """Filesystem journal transport consumed only after strict import."""

    journal_root: Path | None = None
    _last_request_id: str | None = field(default=None, init=False)
    _last_response_id: str | None = field(default=None, init=False)

    def provider_identity(self) -> Mapping[str, Any]:
        return {
            "transport_class": self.__class__.__qualname__,
            "bridge_schema_version": COLLABORATION_BRIDGE_SCHEMA_VERSION,
            "provider_route": "COLLABORATION_CODEX_SUBAGENT",
            "provenance_assurance": COLLABORATION_PROVENANCE_ASSURANCE,
            "direct_score_or_stage_authority": False,
        }

    def configure_journal_root(self, root: str | Path) -> None:
        journal_root = Path(root)
        for name in ("requests", "responses", "quarantine", "locks"):
            (journal_root / name).mkdir(parents=True, exist_ok=True)
        self.journal_root = journal_root
        self._last_request_id = None
        self._last_response_id = None

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
        schema_name: str,
    ) -> StructuredProviderResponse:
        root = self.journal_root
        if root is None:
            raise StructuredProviderUnavailable(
                "COLLABORATION_BRIDGE_NOT_CONFIGURED"
            )
        pass_name = _pass_name_from_schema_name(schema_name)
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        output_schema_hash = _canonical_hash(output_schema)
        provider_identity = dict(self.provider_identity())
        provider_identity_hash = _canonical_hash(provider_identity)
        identity = _request_identity(
            pass_name=pass_name,
            prompt_hash=prompt_hash,
            output_schema_hash=output_schema_hash,
            provider_identity_hash=provider_identity_hash,
        )
        request_id = _request_id(identity)
        request = {
            "schema_version": COLLABORATION_REQUEST_SCHEMA_VERSION,
            "request_id": request_id,
            "request_identity": dict(identity),
            "provider_identity": provider_identity,
            "provider_identity_hash": provider_identity_hash,
            "schema_name": schema_name,
            "pass_name": pass_name,
            "prompt": prompt,
            "prompt_hash": prompt_hash,
            "output_schema": dict(output_schema),
            "output_schema_hash": output_schema_hash,
            "score_or_stage_authority": False,
            "production_score_authority": False,
            "response_import_required": True,
        }
        request_path = root / "requests" / f"{request_id}.json"
        existing_request, _ = _create_or_read_identical_json(
            request_path,
            request,
        )
        if existing_request != request:
            raise StructuredProviderRejected(
                "collaboration request journal identity collision"
            )
        self._last_request_id = request_id
        self._last_response_id = None
        response_path = root / "responses" / f"{request_id}.json"
        if not response_path.is_file():
            raise StructuredProviderUnavailable(
                f"COLLABORATION_RESPONSE_PENDING:{request_id}"
            )
        try:
            with _request_journal_lock(root, request_id):
                envelope = _validate_response_envelope(
                    request=request,
                    envelope=_read_json_object(response_path),
                )
                quarantine_path = (
                    root
                    / "quarantine"
                    / request_id
                    / f"{envelope['response_id']}.json"
                )
                if quarantine_path.is_file():
                    response_path.unlink(missing_ok=True)
                    _fsync_directory(response_path.parent)
                    raise ValueError(
                        "collaboration response was previously quarantined"
                    )
        except (TypeError, ValueError, RuntimeError) as exc:
            self._quarantine_response(
                request_id=request_id,
                reason=f"{exc.__class__.__name__}:{' '.join(str(exc).split())}",
            )
            raise StructuredProviderRejected(
                f"COLLABORATION_RESPONSE_REJECTED:{request_id}:"
                f"{' '.join(str(exc).split())[-500:]}"
            ) from exc
        payload = dict(envelope["payload"])
        self._last_response_id = str(envelope["response_id"])
        return StructuredProviderResponse(
            payload=payload,
            raw_response=json.dumps(
                payload,
                ensure_ascii=False,
                sort_keys=True,
            ),
            stderr="",
            returncode=0,
        )

    def validated_response_identity(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
        schema_name: str,
        response_payload: Mapping[str, Any],
        provider_name: str,
    ) -> Mapping[str, Any] | None:
        """Read and validate one exact active journal response without writes."""

        root = self.journal_root
        if root is None:
            return None
        pass_name = _pass_name_from_schema_name(schema_name)
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        output_schema_hash = _canonical_hash(output_schema)
        provider_identity = dict(self.provider_identity())
        provider_identity_hash = _canonical_hash(provider_identity)
        identity = _request_identity(
            pass_name=pass_name,
            prompt_hash=prompt_hash,
            output_schema_hash=output_schema_hash,
            provider_identity_hash=provider_identity_hash,
        )
        request_id = _request_id(identity)
        request_path = root / "requests" / f"{request_id}.json"
        response_path = root / "responses" / f"{request_id}.json"
        try:
            request = _validate_request(_read_json_object(request_path))
            envelope = _validate_response_envelope(
                request=request,
                envelope=_read_json_object(response_path),
            )
        except (
            FileNotFoundError,
            OSError,
            TypeError,
            ValueError,
            RuntimeError,
        ):
            return None
        if (
            request["request_id"] != request_id
            or request["prompt"] != prompt
            or request["output_schema"] != output_schema
            or envelope["payload"] != response_payload
            or (
                root
                / "quarantine"
                / request_id
                / f"{envelope['response_id']}.json"
            ).is_file()
        ):
            return None
        response_hash = hashlib.sha256(
            json.dumps(
                response_payload,
                ensure_ascii=False,
                sort_keys=True,
                default=str,
            ).encode("utf-8")
        ).hexdigest()
        return {
            "schema_version": (
                "e2r_v5_validated_provider_response_identity_v1"
            ),
            "provider_route": "COLLABORATION_VALIDATED_RESPONSE_JOURNAL",
            "provider_name": provider_name,
            "pass_name": pass_name,
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
            "request_locator_id": request_id,
            "response_locator_id": str(envelope["response_id"]),
            "provenance_hash": _canonical_hash(envelope["provenance"]),
        }

    def validated_request_material_for_prompt_hash(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        """Recover one exact active request/response pair without journal writes."""

        root = self.journal_root
        clean_pass_name = str(pass_name).strip()
        clean_prompt_hash = str(prompt_hash).strip()
        if (
            root is None
            or re.fullmatch(r"[A-Z0-9_]+", clean_pass_name) is None
            or re.fullmatch(r"[0-9a-f]{64}", clean_prompt_hash) is None
        ):
            return None
        candidates: list[tuple[Mapping[str, Any], Mapping[str, Any]]] = []
        try:
            request_paths = tuple(
                (root / "requests").glob("COLLABREQ-*.json")
            )
        except OSError:
            return None
        for request_path in request_paths:
            try:
                request = _validate_request(
                    _read_json_object(request_path)
                )
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
                RuntimeError,
            ):
                continue
            if (
                request["pass_name"] != clean_pass_name
                or request["prompt_hash"] != clean_prompt_hash
            ):
                continue
            request_id = str(request["request_id"])
            response_path = root / "responses" / f"{request_id}.json"
            try:
                envelope = _validate_response_envelope(
                    request=request,
                    envelope=_read_json_object(response_path),
                )
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
                RuntimeError,
            ):
                continue
            quarantine_path = (
                root
                / "quarantine"
                / request_id
                / f"{envelope['response_id']}.json"
            )
            if quarantine_path.is_file():
                continue
            candidates.append((request, envelope))
        if len(candidates) != 1:
            return None
        request, envelope = candidates[0]
        return {
            "request": dict(request),
            "response": dict(envelope),
        }

    def validated_request_for_prompt_hash(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        """Recover one exact active request, including a still-pending one.

        A SourceGraph transport-only resume can advance its checkpoint lineage
        while an already-written collaboration request is waiting for a
        response.  Request recovery therefore cannot require a response file,
        but any response that does exist must still pass the full envelope and
        quarantine checks.
        """

        root = self.journal_root
        clean_pass_name = str(pass_name).strip()
        clean_prompt_hash = str(prompt_hash).strip()
        if (
            root is None
            or re.fullmatch(r"[A-Z0-9_]+", clean_pass_name) is None
            or re.fullmatch(r"[0-9a-f]{64}", clean_prompt_hash) is None
        ):
            return None
        candidates: list[Mapping[str, Any]] = []
        try:
            request_paths = tuple(
                (root / "requests").glob("COLLABREQ-*.json")
            )
        except OSError:
            return None
        for request_path in request_paths:
            try:
                request = _validate_request(
                    _read_json_object(request_path)
                )
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
                RuntimeError,
            ):
                continue
            if (
                request["pass_name"] != clean_pass_name
                or request["prompt_hash"] != clean_prompt_hash
            ):
                continue
            request_id = str(request["request_id"])
            quarantine_root = root / "quarantine" / request_id
            try:
                if any(quarantine_root.glob("COLLABRESP-*.json")):
                    continue
            except OSError:
                continue
            response_path = root / "responses" / f"{request_id}.json"
            if response_path.is_file():
                try:
                    envelope = _validate_response_envelope(
                        request=request,
                        envelope=_read_json_object(response_path),
                    )
                except (
                    FileNotFoundError,
                    OSError,
                    TypeError,
                    ValueError,
                    RuntimeError,
                ):
                    continue
                if (
                    root
                    / "quarantine"
                    / request_id
                    / f"{envelope['response_id']}.json"
                ).is_file():
                    continue
            candidates.append(request)
        if len(candidates) != 1:
            return None
        return dict(candidates[0])

    def validated_fact_extraction_retry_material(
        self,
        *,
        primary_prompt: str,
        output_schema: Mapping[str, Any],
        schema_name: str,
    ) -> Mapping[str, Any] | None:
        """Recover one exact corrected retry for a quarantined primary.

        The quarantined primary payload is deliberately never read.  Its
        immutable request and semantic-validation receipt only establish why
        an exact retry request may be resumed.
        """

        root = self.journal_root
        if root is None:
            return None
        pass_name = _pass_name_from_schema_name(schema_name)
        if pass_name != "EVIDENCE_FACT_EXTRACTION":
            return None
        primary_prompt_hash = hashlib.sha256(
            primary_prompt.encode("utf-8")
        ).hexdigest()
        output_schema_hash = _canonical_hash(output_schema)
        provider_identity = dict(self.provider_identity())
        provider_identity_hash = _canonical_hash(provider_identity)
        primary_identity = _request_identity(
            pass_name=pass_name,
            prompt_hash=primary_prompt_hash,
            output_schema_hash=output_schema_hash,
            provider_identity_hash=provider_identity_hash,
        )
        primary_request_id = _request_id(primary_identity)
        try:
            primary_request = _validate_request(
                _read_json_object(
                    root
                    / "requests"
                    / f"{primary_request_id}.json"
                )
            )
            primary_payload = json.loads(
                primary_prompt.rsplit("\n", 1)[-1]
            )
        except (
            FileNotFoundError,
            OSError,
            TypeError,
            ValueError,
            RuntimeError,
            json.JSONDecodeError,
        ):
            return None
        if (
            not isinstance(primary_payload, Mapping)
            or primary_request.get("request_id") != primary_request_id
            or primary_request.get("prompt") != primary_prompt
            or primary_request.get("output_schema") != output_schema
            or primary_request.get("schema_name") != schema_name
            or (
                root
                / "responses"
                / f"{primary_request_id}.json"
            ).is_file()
        ):
            return None

        semantic_reasons: set[str] = set()
        quarantine_root = root / "quarantine" / primary_request_id
        try:
            reason_paths = tuple(
                quarantine_root.glob(
                    "COLLABRESP-*.json.*.reason.json"
                )
            )
        except OSError:
            return None
        for reason_path in reason_paths:
            try:
                receipt = _read_json_object(reason_path)
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
            ):
                continue
            response_id = str(receipt.get("response_id") or "")
            reason = str(receipt.get("reason") or "")
            if (
                receipt.get("schema_version")
                != "e2r_v5_collaboration_response_quarantine_v1"
                or receipt.get("request_id") != primary_request_id
                or _RESPONSE_ID_RE.fullmatch(response_id) is None
                or not reason_path.name.startswith(
                    f"{response_id}.json."
                )
                or not (
                    quarantine_root / f"{response_id}.json"
                ).is_file()
                or receipt.get("production_score_authority") is not False
                or receipt.get("reusable_provider_response") is not False
                or not reason.startswith(
                    "FACT_EXTRACTION_SEMANTIC_VALIDATION:"
                )
            ):
                continue
            semantic_reasons.add(reason)
        if not semantic_reasons:
            return None

        candidates: list[
            tuple[Mapping[str, Any], Mapping[str, Any], Mapping[str, Any]]
        ] = []
        try:
            request_paths = tuple(
                (root / "requests").glob("COLLABREQ-*.json")
            )
        except OSError:
            return None
        for request_path in request_paths:
            try:
                retry_request = _validate_request(
                    _read_json_object(request_path)
                )
                retry_payload = json.loads(
                    str(retry_request["prompt"]).rsplit("\n", 1)[-1]
                )
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
                RuntimeError,
                json.JSONDecodeError,
            ):
                continue
            if (
                retry_request.get("request_id") == primary_request_id
                or retry_request.get("pass_name") != pass_name
                or retry_request.get("schema_name") != schema_name
                or retry_request.get("output_schema") != output_schema
                or not isinstance(retry_payload, Mapping)
            ):
                continue
            retry_context = retry_payload.get(
                "fact_extraction_retry_context"
            )
            if not isinstance(retry_context, Mapping):
                continue
            retry_base_payload = dict(retry_payload)
            retry_base_payload.pop("fact_extraction_retry_context", None)
            if retry_base_payload != primary_payload:
                continue
            validation_errors = retry_context.get("validation_errors")
            if (
                not isinstance(validation_errors, list)
                or not validation_errors
                or any(
                    not isinstance(reason, str) or not reason.strip()
                    for reason in validation_errors
                )
            ):
                continue
            expected_reason = " ".join(
                (
                    "FACT_EXTRACTION_SEMANTIC_VALIDATION:"
                    + " | ".join(validation_errors)
                ).split()
            )[-1000:]
            if expected_reason not in semantic_reasons:
                continue
            request_id = str(retry_request["request_id"])
            try:
                retry_response = _validate_response_envelope(
                    request=retry_request,
                    envelope=_read_json_object(
                        root / "responses" / f"{request_id}.json"
                    ),
                )
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
                RuntimeError,
            ):
                continue
            if (
                root
                / "quarantine"
                / request_id
                / f"{retry_response['response_id']}.json"
            ).is_file():
                continue
            candidates.append(
                (retry_request, retry_response, retry_payload)
            )
        if len(candidates) != 1:
            return None
        retry_request, retry_response, retry_payload = candidates[0]
        return {
            "primary_request": dict(primary_request),
            "retry_request": dict(retry_request),
            "retry_response": dict(retry_response),
            "retry_payload": dict(retry_payload),
        }

    def validated_peer_selection_retry_material(
        self,
        *,
        primary_prompt: str,
        output_schema: Mapping[str, Any],
        schema_name: str,
    ) -> Mapping[str, Any] | None:
        """Recover one exact peer retry after its primary was quarantined.

        A clean process starts the peer route from the immutable primary
        payload.  If that response was quarantined, the ordinary call stops at
        the missing primary response before it can reach the already imported
        retry.  Bind that retry to the primary payload and quarantine receipt
        so resume can consume it without treating the rejected response as a
        cache hit.
        """

        root = self.journal_root
        if root is None:
            return None
        pass_name = _pass_name_from_schema_name(schema_name)
        if pass_name != "STRUCTURED_PEER_SELECTION":
            return None
        primary_prompt_hash = hashlib.sha256(
            primary_prompt.encode("utf-8")
        ).hexdigest()
        output_schema_hash = _canonical_hash(output_schema)
        provider_identity_hash = _canonical_hash(self.provider_identity())
        primary_request_id = _request_id(
            _request_identity(
                pass_name=pass_name,
                prompt_hash=primary_prompt_hash,
                output_schema_hash=output_schema_hash,
                provider_identity_hash=provider_identity_hash,
            )
        )
        try:
            primary_request = _validate_request(
                _read_json_object(
                    root / "requests" / f"{primary_request_id}.json"
                )
            )
            primary_payload = json.loads(
                primary_prompt.rsplit("\n", 1)[-1]
            )
        except (
            FileNotFoundError,
            OSError,
            TypeError,
            ValueError,
            RuntimeError,
            json.JSONDecodeError,
        ):
            return None
        if (
            not isinstance(primary_payload, Mapping)
            or primary_request.get("request_id") != primary_request_id
            or primary_request.get("prompt") != primary_prompt
            or primary_request.get("output_schema") != output_schema
            or primary_request.get("schema_name") != schema_name
            or (root / "responses" / f"{primary_request_id}.json").is_file()
        ):
            return None

        quarantine_reasons: set[str] = set()
        quarantine_root = root / "quarantine" / primary_request_id
        try:
            reason_paths = tuple(
                quarantine_root.glob("COLLABRESP-*.json.*.reason.json")
            )
        except OSError:
            return None
        for reason_path in reason_paths:
            try:
                receipt = _read_json_object(reason_path)
            except (FileNotFoundError, OSError, TypeError, ValueError):
                continue
            response_id = str(receipt.get("response_id") or "")
            reason = str(receipt.get("reason") or "")
            if (
                receipt.get("schema_version")
                != "e2r_v5_collaboration_response_quarantine_v1"
                or receipt.get("request_id") != primary_request_id
                or _RESPONSE_ID_RE.fullmatch(response_id) is None
                or not reason_path.name.startswith(f"{response_id}.json.")
                or not (quarantine_root / f"{response_id}.json").is_file()
                or receipt.get("production_score_authority") is not False
                or receipt.get("reusable_provider_response") is not False
                or not reason.startswith(
                    "STRUCTURED_PEER_RESPONSE_VALIDATION_REJECTED:"
                    "FRESH_SELECTION_RESPONSE_ATTEMPT_1:"
                )
            ):
                continue
            quarantine_reasons.add(reason)
        if not quarantine_reasons:
            return None

        candidates: list[
            tuple[Mapping[str, Any], Mapping[str, Any], Mapping[str, Any]]
        ] = []
        try:
            request_paths = tuple((root / "requests").glob("COLLABREQ-*.json"))
        except OSError:
            return None
        for request_path in request_paths:
            try:
                retry_request = _validate_request(
                    _read_json_object(request_path)
                )
                retry_payload = json.loads(
                    str(retry_request["prompt"]).rsplit("\n", 1)[-1]
                )
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
                RuntimeError,
                json.JSONDecodeError,
            ):
                continue
            if (
                retry_request.get("request_id") == primary_request_id
                or retry_request.get("pass_name") != pass_name
                or retry_request.get("schema_name") != schema_name
                or retry_request.get("output_schema") != output_schema
                or not isinstance(retry_payload, Mapping)
            ):
                continue
            retry_context = retry_payload.get("peer_selection_retry_context")
            if (
                not isinstance(retry_context, Mapping)
                or set(retry_context) != {"validation_error", "instruction"}
            ):
                continue
            retry_base_payload = dict(retry_payload)
            retry_base_payload.pop("peer_selection_retry_context", None)
            if retry_base_payload != primary_payload:
                continue
            validation_error = retry_context.get("validation_error")
            if not isinstance(validation_error, str) or not validation_error.strip():
                continue
            if retry_context.get("instruction") != (
                "Rewrite the complete peer selection under the original "
                "two-to-five peer contract; do not invent any valuation values."
            ):
                continue
            expected_reason = " ".join(
                (
                    "STRUCTURED_PEER_RESPONSE_VALIDATION_REJECTED:"
                    "FRESH_SELECTION_RESPONSE_ATTEMPT_1:"
                    + validation_error
                ).split()
            )[-500:]
            if expected_reason not in quarantine_reasons:
                continue
            request_id = str(retry_request["request_id"])
            try:
                retry_response = _validate_response_envelope(
                    request=retry_request,
                    envelope=_read_json_object(
                        root / "responses" / f"{request_id}.json"
                    ),
                )
            except (
                FileNotFoundError,
                OSError,
                TypeError,
                ValueError,
                RuntimeError,
            ):
                continue
            if (
                root
                / "quarantine"
                / request_id
                / f"{retry_response['response_id']}.json"
            ).is_file():
                continue
            candidates.append(
                (retry_request, retry_response, retry_payload)
            )
        if len(candidates) != 1:
            return None
        retry_request, retry_response, retry_payload = candidates[0]
        return {
            "primary_request": dict(primary_request),
            "retry_request": dict(retry_request),
            "retry_response": dict(retry_response),
            "retry_payload": dict(retry_payload),
        }

    def invalidate_last_response(self, reason: str) -> Mapping[str, Any]:
        request_id = self._last_request_id
        if request_id is None:
            return {
                "status": "NO_COLLABORATION_RESPONSE",
                "reason": str(reason),
            }
        return self._quarantine_response(
            request_id=request_id,
            reason=str(reason),
            use_last_validated_response_id=True,
        )

    def _quarantine_response(
        self,
        *,
        request_id: str,
        reason: str,
        use_last_validated_response_id: bool = False,
    ) -> Mapping[str, Any]:
        root = self.journal_root
        if root is None:
            return {
                "status": "COLLABORATION_BRIDGE_NOT_CONFIGURED",
                "request_id": request_id,
                "reason": reason,
            }
        if _REQUEST_ID_RE.fullmatch(str(request_id)) is None:
            raise ValueError("collaboration quarantine request id is invalid")
        with _request_journal_lock(root, request_id):
            return self._quarantine_response_locked(
                root=root,
                request_id=request_id,
                reason=reason,
                use_last_validated_response_id=(
                    use_last_validated_response_id
                ),
            )

    def _quarantine_response_locked(
        self,
        *,
        root: Path,
        request_id: str,
        reason: str,
        use_last_validated_response_id: bool,
    ) -> Mapping[str, Any]:
        response_path = root / "responses" / f"{request_id}.json"
        try:
            response_bytes = response_path.read_bytes()
        except FileNotFoundError:
            return {
                "status": "COLLABORATION_RESPONSE_ALREADY_ABSENT",
                "request_id": request_id,
                "reason": reason,
            }
        trusted_response_id = (
            self._last_response_id
            if use_last_validated_response_id
            and request_id == self._last_request_id
            and isinstance(self._last_response_id, str)
            and _RESPONSE_ID_RE.fullmatch(self._last_response_id) is not None
            else None
        )
        response_id = (
            trusted_response_id
            if trusted_response_id is not None
            else "COLLABRESP-" + hashlib.sha256(response_bytes).hexdigest()
        )
        quarantine_root = root / "quarantine" / request_id
        quarantine_root.mkdir(parents=True, exist_ok=True)
        quarantine_path = quarantine_root / f"{response_id}.json"
        try:
            os.link(response_path, quarantine_path)
            _fsync_directory(quarantine_root)
        except FileExistsError:
            if quarantine_path.read_bytes() != response_bytes:
                raise ValueError(
                    "collaboration quarantine response identity collision"
                )
        except FileNotFoundError:
            if not quarantine_path.is_file():
                return {
                    "status": "COLLABORATION_RESPONSE_ALREADY_ABSENT",
                    "request_id": request_id,
                    "reason": reason,
                }
            if quarantine_path.read_bytes() != response_bytes:
                raise ValueError(
                    "collaboration quarantine response identity collision"
                )
        response_path.unlink(missing_ok=True)
        _fsync_directory(response_path.parent)
        clean_reason = " ".join(str(reason).split())[-1000:]
        reason_hash = hashlib.sha256(clean_reason.encode("utf-8")).hexdigest()
        reason_path = quarantine_path.with_name(
            f"{quarantine_path.name}.{reason_hash}.reason.json"
        )
        reason_receipt = {
            "schema_version": (
                "e2r_v5_collaboration_response_quarantine_v1"
            ),
            "request_id": request_id,
            "response_id": response_id,
            "reason": clean_reason,
            "quarantined_response_path": str(quarantine_path),
            "production_score_authority": False,
            "reusable_provider_response": False,
        }
        existing_reason, _ = _create_or_read_identical_json(
            reason_path,
            reason_receipt,
        )
        if existing_reason != reason_receipt:
            raise ValueError(
                "collaboration quarantine reason identity collision"
            )
        self._last_response_id = None
        return {
            "status": "COLLABORATION_RESPONSE_QUARANTINED",
            "request_id": request_id,
            "response_id": response_id,
            "quarantined_response_path": str(quarantine_path),
            "reason_path": str(reason_path),
        }

    def journal_audit(self) -> Mapping[str, Any]:
        root = self.journal_root
        if root is None:
            return {
                "schema_version": (
                    "e2r_v5_collaboration_provider_journal_audit_v1"
                ),
                "status": "COLLABORATION_JOURNAL_DISABLED",
                "request_count": 0,
                "validated_request_count": 0,
                "invalid_request_count": 0,
                "response_file_count": 0,
                "validated_response_count": 0,
                "invalid_response_count": 0,
                "orphan_response_count": 0,
                "pending_response_count": 0,
                "quarantined_response_count": 0,
                "provenance_assurance": (
                    COLLABORATION_PROVENANCE_ASSURANCE
                ),
                "score_or_stage_authority": False,
            }
        requests = tuple((root / "requests").glob("*.json"))
        responses = tuple((root / "responses").glob("*.json"))
        valid_requests: dict[str, Mapping[str, Any]] = {}
        invalid_request_count = 0
        for request_path in requests:
            try:
                request = _validate_request(
                    _read_json_object(request_path)
                )
                request_id = str(request["request_id"])
                if request_path.name != f"{request_id}.json":
                    raise ValueError(
                        "collaboration request path and payload disagree"
                    )
            except (TypeError, ValueError, RuntimeError):
                invalid_request_count += 1
                continue
            valid_requests[request_id] = request
        validated_response_request_ids: set[str] = set()
        invalid_response_count = 0
        orphan_response_count = 0
        for response_path in responses:
            request = valid_requests.get(response_path.stem)
            if request is None:
                orphan_response_count += 1
                continue
            try:
                envelope = _validate_response_envelope(
                    request=request,
                    envelope=_read_json_object(response_path),
                )
                if (
                    root
                    / "quarantine"
                    / response_path.stem
                    / f"{envelope['response_id']}.json"
                ).is_file():
                    raise ValueError(
                        "active response has a quarantine tombstone"
                    )
            except (TypeError, ValueError, RuntimeError):
                invalid_response_count += 1
                continue
            validated_response_request_ids.add(response_path.stem)
        quarantined = tuple(
            path
            for path in (root / "quarantine").rglob("COLLABRESP-*.json")
            if not path.name.endswith(".reason.json")
        )
        return {
            "schema_version": (
                "e2r_v5_collaboration_provider_journal_audit_v1"
            ),
            "status": "COLLABORATION_JOURNAL_ACTIVE",
            "journal_root": str(root),
            "request_count": len(requests),
            "validated_request_count": len(valid_requests),
            "invalid_request_count": invalid_request_count,
            "response_file_count": len(responses),
            "validated_response_count": len(
                validated_response_request_ids
            ),
            "invalid_response_count": invalid_response_count,
            "orphan_response_count": orphan_response_count,
            "pending_response_count": len(
                set(valid_requests) - validated_response_request_ids
            ),
            "quarantined_response_count": len(quarantined),
            "last_request_id": self._last_request_id,
            "last_response_id": self._last_response_id,
            "provenance_assurance": COLLABORATION_PROVENANCE_ASSURANCE,
            "score_or_stage_authority": False,
            "normal_codex_cli_cache_namespace": False,
        }


def _validate_request(request: Mapping[str, Any]) -> Mapping[str, Any]:
    if set(request) != _REQUEST_ENVELOPE_KEYS:
        raise ValueError(
            "collaboration request envelope key roster mismatch"
        )
    if request.get("schema_version") != COLLABORATION_REQUEST_SCHEMA_VERSION:
        raise ValueError("unknown collaboration request schema")
    request_id = str(request.get("request_id") or "")
    if _REQUEST_ID_RE.fullmatch(request_id) is None:
        raise ValueError("collaboration request id is invalid")
    prompt = request.get("prompt")
    output_schema = request.get("output_schema")
    if not isinstance(prompt, str) or not prompt:
        raise ValueError("collaboration request prompt is missing")
    if not isinstance(output_schema, Mapping):
        raise ValueError("collaboration request output schema is missing")
    schema_name = request.get("schema_name")
    pass_name = str(request.get("pass_name") or "")
    if not isinstance(schema_name, str) or not schema_name:
        raise ValueError("collaboration request schema name is missing")
    if _pass_name_from_schema_name(schema_name) != pass_name:
        raise ValueError(
            "collaboration request schema name and pass name mismatch"
        )
    if request.get("response_import_required") is not True:
        raise ValueError(
            "collaboration request must require response import"
        )
    prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    output_schema_hash = _canonical_hash(output_schema)
    provider_identity = request.get("provider_identity")
    if not isinstance(provider_identity, Mapping):
        raise ValueError("collaboration provider identity is missing")
    expected_provider_identity = (
        CollaborationCodexSubagentTransport().provider_identity()
    )
    if provider_identity != expected_provider_identity:
        raise ValueError(
            "collaboration request provider identity is invalid"
        )
    provider_identity_hash = _canonical_hash(provider_identity)
    if (
        request.get("prompt_hash") != prompt_hash
        or request.get("output_schema_hash") != output_schema_hash
        or request.get("provider_identity_hash") != provider_identity_hash
    ):
        raise ValueError("collaboration request content hash mismatch")
    identity = _request_identity(
        pass_name=pass_name,
        prompt_hash=prompt_hash,
        output_schema_hash=output_schema_hash,
        provider_identity_hash=provider_identity_hash,
    )
    if request.get("request_identity") != identity:
        raise ValueError("collaboration request identity mismatch")
    if request_id != _request_id(identity):
        raise ValueError("collaboration request id hash mismatch")
    if (
        request.get("score_or_stage_authority") is not False
        or request.get("production_score_authority") is not False
    ):
        raise ValueError("collaboration request cannot have score authority")
    return dict(request)


def _validate_response_envelope(
    *,
    request: Mapping[str, Any],
    envelope: Mapping[str, Any],
) -> Mapping[str, Any]:
    request = _validate_request(request)
    if set(envelope) != _RESPONSE_ENVELOPE_KEYS:
        raise ValueError(
            "collaboration response envelope key roster mismatch"
        )
    if envelope.get("schema_version") != COLLABORATION_RESPONSE_SCHEMA_VERSION:
        raise ValueError("unknown collaboration response schema")
    if envelope.get("request_id") != request["request_id"]:
        raise ValueError("collaboration response request id mismatch")
    for key in (
        "prompt_hash",
        "output_schema_hash",
        "provider_identity_hash",
    ):
        if envelope.get(key) != request[key]:
            raise ValueError(f"collaboration response {key} mismatch")
    payload = envelope.get("payload")
    if not isinstance(payload, Mapping):
        raise ValueError("collaboration response payload must be an object")
    payload_hash = _canonical_hash(payload)
    if envelope.get("payload_hash") != payload_hash:
        raise ValueError("collaboration response payload hash mismatch")
    provenance = envelope.get("provenance")
    if not isinstance(provenance, Mapping):
        raise ValueError("collaboration response provenance is missing")
    validated_provenance = _validate_agent_provenance(
        agent_id=str(provenance.get("agent_id") or ""),
        canonical_task_name=str(
            provenance.get("canonical_task_name") or ""
        ),
        agent_model=str(provenance.get("agent_model") or ""),
    )
    if provenance != validated_provenance:
        raise ValueError("collaboration response provenance mismatch")
    expected_response_id = "COLLABRESP-" + _canonical_hash(
        {
            "request_id": request["request_id"],
            "payload_hash": payload_hash,
            "provenance": validated_provenance,
        }
    )
    if envelope.get("response_id") != expected_response_id:
        raise ValueError("collaboration response id hash mismatch")
    validation = envelope.get("validation")
    expected_validation = {
        "draft202012_schema_valid": True,
        "blind_research_output_valid": True,
        "request_hashes_valid": True,
        "downstream_semantic_validation_required": True,
    }
    if validation != expected_validation:
        raise ValueError("collaboration response validation receipt mismatch")
    if (
        envelope.get("score_or_stage_authority") is not False
        or envelope.get("production_score_authority") is not False
    ):
        raise ValueError("collaboration response cannot have score authority")
    _draft202012_validate(
        payload=payload,
        output_schema=request["output_schema"],
    )
    assert_blind_research_output(payload)
    return dict(envelope)


def import_collaboration_response(
    *,
    journal_root: str | Path,
    request_id: str,
    response_payload: Mapping[str, Any],
    agent_id: str,
    canonical_task_name: str,
    agent_model: str,
) -> Mapping[str, Any]:
    """Validate and atomically import one collaboration-subagent response."""

    if _REQUEST_ID_RE.fullmatch(str(request_id)) is None:
        raise ValueError("collaboration request id is invalid")
    root = Path(journal_root)
    request_path = root / "requests" / f"{request_id}.json"
    request = _validate_request(_read_json_object(request_path))
    if request["request_id"] != request_id:
        raise ValueError("collaboration request path and payload disagree")
    payload = dict(response_payload)
    _draft202012_validate(
        payload=payload,
        output_schema=request["output_schema"],
    )
    assert_blind_research_output(payload)
    provenance = _validate_agent_provenance(
        agent_id=agent_id,
        canonical_task_name=canonical_task_name,
        agent_model=agent_model,
    )
    payload_hash = _canonical_hash(payload)
    response_id = "COLLABRESP-" + _canonical_hash(
        {
            "request_id": request_id,
            "payload_hash": payload_hash,
            "provenance": provenance,
        }
    )
    envelope = {
        "schema_version": COLLABORATION_RESPONSE_SCHEMA_VERSION,
        "response_id": response_id,
        "request_id": request_id,
        "prompt_hash": request["prompt_hash"],
        "output_schema_hash": request["output_schema_hash"],
        "provider_identity_hash": request["provider_identity_hash"],
        "payload_hash": payload_hash,
        "payload": payload,
        "provenance": provenance,
        "validation": {
            "draft202012_schema_valid": True,
            "blind_research_output_valid": True,
            "request_hashes_valid": True,
            "downstream_semantic_validation_required": True,
        },
        "score_or_stage_authority": False,
        "production_score_authority": False,
    }
    _validate_response_envelope(request=request, envelope=envelope)
    with _request_journal_lock(root, request_id):
        quarantine_path = (
            root
            / "quarantine"
            / request_id
            / f"{response_id}.json"
        )
        if quarantine_path.is_file():
            raise ValueError(
                "the same collaboration response was previously quarantined"
            )
        response_path = root / "responses" / f"{request_id}.json"
        existing, created = _create_or_read_identical_json(
            response_path,
            envelope,
        )
        if not created and existing != envelope:
            raise ValueError(
                "a different collaboration response is already imported"
            )
        return existing


@dataclass
class CollaborationCodexResearcherProvider(CodexResearcherProvider):
    """Codex researcher backed only by the validated collaboration journal."""

    transport: CollaborationCodexSubagentTransport
    provider_name: str = COLLABORATION_PROVIDER_NAME

    @classmethod
    def default(cls) -> "CollaborationCodexResearcherProvider":
        return cls(transport=CollaborationCodexSubagentTransport())

    def configure_response_cache(self, directory: str | Path) -> None:
        # The ordinary Codex CLI cache is intentionally not used here.  The
        # validated response journal carries the response-specific provenance.
        cache_root = Path(directory)
        self.response_cache_directory = None
        self._response_cache_call_start_index = len(self.calls)
        self._response_cache_invalidation_start_index = len(
            self.cache_invalidations
        )
        self.transport.configure_journal_root(
            cache_root.parent / "collaboration_codex_subagent_provider"
        )

    def invalidate_last_response_cache(self, reason: str) -> Mapping[str, Any]:
        cache_event = dict(super().invalidate_last_response_cache(reason))
        journal_event = dict(self.transport.invalidate_last_response(reason))
        combined = {
            **cache_event,
            "collaboration_journal_invalidation": journal_event,
        }
        if self.cache_invalidations:
            self.cache_invalidations[-1] = combined
        return combined

    def validated_response_identity(
        self,
        *,
        pass_name: str,
        payload: Mapping[str, Any],
        response_payload: Mapping[str, Any],
    ) -> Mapping[str, Any] | None:
        """Bind reuse to the exact validated collaboration response envelope."""

        (
            _safe_payload,
            output_schema,
            prompt,
            _prompt_hash,
            _schema_hash,
        ) = _single_payload_request_material(
            pass_name=pass_name,
            payload=payload,
        )
        return self.transport.validated_response_identity(
            prompt=prompt,
            output_schema=output_schema,
            schema_name=f"e2r_v5_{pass_name.lower()}",
            response_payload=response_payload,
            provider_name=self.provider_name,
        )

    def validated_request_payload(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        """Recover only a request backed by one validated active response."""

        material = self.transport.validated_request_material_for_prompt_hash(
            pass_name=pass_name,
            prompt_hash=prompt_hash,
        )
        if not isinstance(material, Mapping):
            return None
        request = material.get("request")
        return self._validated_payload_from_request(
            request=request,
            pass_name=pass_name,
            prompt_hash=prompt_hash,
        )

    def validated_pending_request_payload(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        """Recover request-only material for a pending saturation replay."""

        request = self.transport.validated_request_for_prompt_hash(
            pass_name=pass_name,
            prompt_hash=prompt_hash,
        )
        return self._validated_payload_from_request(
            request=request,
            pass_name=pass_name,
            prompt_hash=prompt_hash,
        )

    def validated_fact_extraction_retry_payload(
        self,
        *,
        primary_payload: Mapping[str, Any],
    ) -> Mapping[str, Any] | None:
        """Recover only the exact active retry bound to this primary."""

        try:
            (
                safe_primary_payload,
                output_schema,
                primary_prompt,
                _primary_prompt_hash,
                _schema_hash,
            ) = _single_payload_request_material(
                pass_name="EVIDENCE_FACT_EXTRACTION",
                payload=primary_payload,
            )
        except (KeyError, TypeError, ValueError):
            return None
        material = self.transport.validated_fact_extraction_retry_material(
            primary_prompt=primary_prompt,
            output_schema=output_schema,
            schema_name="e2r_v5_evidence_fact_extraction",
        )
        if not isinstance(material, Mapping):
            return None
        request = material.get("retry_request")
        if not isinstance(request, Mapping):
            return None
        retry_payload = self._validated_payload_from_request(
            request=request,
            pass_name="EVIDENCE_FACT_EXTRACTION",
            prompt_hash=str(request.get("prompt_hash") or ""),
        )
        if not isinstance(retry_payload, Mapping):
            return None
        retry_base_payload = dict(retry_payload)
        retry_base_payload.pop("fact_extraction_retry_context", None)
        if retry_base_payload != safe_primary_payload:
            return None
        return dict(retry_payload)

    def validated_peer_selection_retry_payload(
        self,
        *,
        primary_payload: Mapping[str, Any],
    ) -> Mapping[str, Any] | None:
        """Recover only the exact active peer retry bound to this primary."""

        try:
            (
                safe_primary_payload,
                output_schema,
                primary_prompt,
                _primary_prompt_hash,
                _schema_hash,
            ) = _single_payload_request_material(
                pass_name="STRUCTURED_PEER_SELECTION",
                payload=primary_payload,
            )
        except (KeyError, TypeError, ValueError):
            return None
        material = self.transport.validated_peer_selection_retry_material(
            primary_prompt=primary_prompt,
            output_schema=output_schema,
            schema_name="e2r_v5_structured_peer_selection",
        )
        if not isinstance(material, Mapping):
            return None
        request = material.get("retry_request")
        if not isinstance(request, Mapping):
            return None
        retry_payload = self._validated_payload_from_request(
            request=request,
            pass_name="STRUCTURED_PEER_SELECTION",
            prompt_hash=str(request.get("prompt_hash") or ""),
        )
        if not isinstance(retry_payload, Mapping):
            return None
        retry_base_payload = dict(retry_payload)
        retry_base_payload.pop("peer_selection_retry_context", None)
        if retry_base_payload != safe_primary_payload:
            return None
        return dict(retry_payload)

    @staticmethod
    def _validated_payload_from_request(
        *,
        request: Any,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        if not isinstance(request, Mapping):
            return None
        prompt = request.get("prompt")
        if not isinstance(prompt, str) or "\n" not in prompt:
            return None
        try:
            payload = json.loads(prompt.rsplit("\n", 1)[-1])
        except (TypeError, json.JSONDecodeError):
            return None
        if not isinstance(payload, Mapping):
            return None
        try:
            (
                safe_payload,
                output_schema,
                rebuilt_prompt,
                rebuilt_prompt_hash,
                rebuilt_schema_hash,
            ) = _single_payload_request_material(
                pass_name=pass_name,
                payload=payload,
            )
        except (KeyError, TypeError, ValueError):
            return None
        if (
            rebuilt_prompt_hash != prompt_hash
            or request.get("prompt_hash") != rebuilt_prompt_hash
            or request.get("prompt") != rebuilt_prompt
            or request.get("output_schema") != output_schema
            or request.get("output_schema_hash") != rebuilt_schema_hash
            or request.get("schema_name")
            != f"e2r_v5_{pass_name.lower()}"
        ):
            return None
        return dict(safe_payload)

    def response_cache_audit(self) -> Mapping[str, Any]:
        return {
            **super().response_cache_audit(),
            "status": "COLLABORATION_PROVIDER_JOURNAL_ACTIVE",
            "collaboration_journal": dict(self.transport.journal_audit()),
        }


class CodexSubagentFallbackResearchProvider(CodexResearcherProvider):
    """Route only the exact usage-limited leaf to collaboration Codex.

    ``CodexResearcherProvider.complete`` owns the loss-accounted chunk and
    synthesis orchestration.  Keeping that method intact is important: a
    usage-limit miss on chunk 2 must not replay chunk 1 through a different
    provider.  This subclass therefore switches providers only inside
    ``_complete_single_payload``, the smallest independently cached leaf.
    """

    def __init__(
        self,
        *,
        primary: CodexResearcherProvider,
        collaboration: CollaborationCodexResearcherProvider,
    ) -> None:
        super().__init__(
            transport=primary.transport,
            provider_name=CODEX_SUBAGENT_FALLBACK_PROVIDER_NAME,
        )
        self.primary = primary
        self.collaboration = collaboration
        self._call_start_index = 0
        self._last_provider: CodexResearcherProvider | None = None

    @classmethod
    def default(
        cls,
        *,
        working_directory: str | Path | None = None,
        timeout_seconds: float = 300.0,
    ) -> "CodexSubagentFallbackResearchProvider":
        return cls(
            primary=CodexResearcherProvider.default(
                working_directory=working_directory,
                timeout_seconds=timeout_seconds,
            ),
            collaboration=CollaborationCodexResearcherProvider.default(),
        )

    @property
    def candidate_ranking_page_candidate_limit(self) -> int:
        return CANDIDATE_RANKING_PAGE_CANDIDATE_LIMIT

    @property
    def memo_fact_prompt_chunk_chars(self) -> int:
        return self.primary.memo_fact_prompt_chunk_chars

    def _complete_single_payload(
        self,
        *,
        pass_name: str,
        payload: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        primary_call_start = len(self.primary.calls)
        try:
            response = self.primary._complete_single_payload(
                pass_name=pass_name,
                payload=payload,
            )
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            if not self._primary_usage_limit_failure(
                exc,
                call_start_index=primary_call_start,
            ):
                self._last_provider = self.primary
                self._mirror_latest_call(self.primary, route="CODEX_CLI")
                raise
            try:
                response = self.collaboration._complete_single_payload(
                    pass_name=pass_name,
                    payload=payload,
                )
            except (
                StructuredProviderUnavailable,
                StructuredProviderRejected,
                TimeoutError,
                OSError,
                RuntimeError,
            ):
                self._last_provider = self.collaboration
                self._mirror_latest_call(
                    self.collaboration,
                    route="COLLABORATION_CODEX_SUBAGENT",
                )
                raise
            self._last_provider = self.collaboration
            self._mirror_latest_call(
                self.collaboration,
                route="COLLABORATION_CODEX_SUBAGENT",
            )
            return response
        self._last_provider = self.primary
        self._mirror_latest_call(self.primary, route="CODEX_CLI")
        return response

    def configure_response_cache(self, directory: str | Path) -> None:
        self.primary.configure_response_cache(directory)
        self.collaboration.configure_response_cache(directory)
        self._call_start_index = len(self.calls)
        self._last_provider = None

    def validated_request_payload(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        """Delegate legacy request recovery only to the validated journal."""

        return self.collaboration.validated_request_payload(
            pass_name=pass_name,
            prompt_hash=prompt_hash,
        )

    def validated_pending_request_payload(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        """Delegate request-only recovery solely to collaboration pending."""

        return self.collaboration.validated_pending_request_payload(
            pass_name=pass_name,
            prompt_hash=prompt_hash,
        )

    def validated_fact_extraction_retry_payload(
        self,
        *,
        primary_payload: Mapping[str, Any],
    ) -> Mapping[str, Any] | None:
        """Delegate exact semantic-retry recovery to collaboration only."""

        return self.collaboration.validated_fact_extraction_retry_payload(
            primary_payload=primary_payload,
        )

    def validated_peer_selection_retry_payload(
        self,
        *,
        primary_payload: Mapping[str, Any],
    ) -> Mapping[str, Any] | None:
        """Delegate exact peer-retry recovery to collaboration only."""

        return self.collaboration.validated_peer_selection_retry_payload(
            primary_payload=primary_payload,
        )

    def invalidate_last_response_cache(self, reason: str) -> Mapping[str, Any]:
        if self._last_provider is None:
            event = {
                "status": "NO_ELIGIBLE_RESPONSE",
                "reason": str(reason),
            }
        else:
            event = dict(
                self._last_provider.invalidate_last_response_cache(reason)
            )
        self.cache_invalidations.append(event)
        return event

    def response_cache_audit(self) -> Mapping[str, Any]:
        primary = dict(self.primary.response_cache_audit())
        collaboration = dict(self.collaboration.response_cache_audit())
        events = tuple(self.calls[self._call_start_index :])
        bridge = dict(
            collaboration.get("collaboration_journal") or {}
        )
        return {
            "schema_version": (
                "e2r_v5_codex_subagent_fallback_provider_audit_v1"
            ),
            "status": "CODEX_SUBAGENT_FALLBACK_PROVIDER_ACTIVE",
            "provider_name": self.provider_name,
            "logical_call_count": len(events),
            "successful_call_count": sum(
                row.get("status") == "COMPLETE" for row in events
            ),
            "provider_error_count": sum(
                row.get("status") == "PROVIDER_ERROR" for row in events
            ),
            "provider_output_rejected_count": sum(
                row.get("status") == "PROVIDER_OUTPUT_REJECTED"
                for row in events
            ),
            "prompt_transport_rejected_count": sum(
                row.get("status") == "PROMPT_TRANSPORT_REJECTED"
                for row in events
            ),
            "transport_call_count": int(
                primary.get("transport_call_count") or 0
            ),
            "provider_usage_limit_detected": bool(
                primary.get("provider_usage_limit_detected")
            ),
            "provider_usage_limit_reset_hints": list(
                primary.get("provider_usage_limit_reset_hints") or ()
            ),
            "provider_usage_limit_transport_error_count": int(
                primary.get(
                    "provider_usage_limit_transport_error_count"
                )
                or 0
            ),
            "provider_usage_limit_short_circuit_count": int(
                primary.get(
                    "provider_usage_limit_short_circuit_count"
                )
                or 0
            ),
            "cache_hit_count": int(primary.get("cache_hit_count") or 0),
            "cache_invalid_or_unreadable_count": int(
                primary.get("cache_invalid_or_unreadable_count") or 0
            ),
            "downstream_semantic_invalidation_count": len(
                self.cache_invalidations
            ),
            "downstream_semantic_cache_delete_count": sum(
                row.get("status") == "INVALID_RESPONSE_CACHE_DELETED"
                for row in self.cache_invalidations
            ),
            "downstream_semantic_cache_delete_failure_count": sum(
                row.get("status") == "CACHE_DELETE_FAILED"
                for row in self.cache_invalidations
            ),
            "failed_provider_response_cached": False,
            "normal_codex_cli_cache": primary,
            "collaboration_provider": collaboration,
            "collaboration_journal": bridge,
            "collaboration_response_score_or_stage_authority": False,
        }

    def _provider_identity(self) -> Mapping[str, Any]:
        return {
            "provider_class": self.__class__.__qualname__,
            "provider_name": self.provider_name,
            "primary_provider_identity": dict(
                self.primary._provider_identity()
            ),
            "collaboration_provider_identity": dict(
                self.collaboration._provider_identity()
            ),
            "fallback_condition": "CODEX_CLI_USAGE_LIMIT_CACHE_MISS_ONLY",
            "provenance_assurance": COLLABORATION_PROVENANCE_ASSURANCE,
            "direct_score_or_stage_authority": False,
        }

    def _primary_usage_limit_failure(
        self,
        error: Exception,
        *,
        call_start_index: int,
    ) -> bool:
        latest = (
            self.primary.calls[-1]
            if len(self.primary.calls) > call_start_index
            else {}
        )
        return bool(
            latest.get("provider_failure_class") == "USAGE_LIMIT"
            and _USAGE_LIMIT_RE.search(str(error))
        )

    def _mirror_latest_call(
        self,
        provider: CodexResearcherProvider,
        *,
        route: str,
    ) -> None:
        latest = dict(provider.calls[-1]) if provider.calls else {}
        self.calls.append(
            {
                **latest,
                "provider_route": route,
                "composite_provider_name": self.provider_name,
            }
        )


__all__ = [
    "CODEX_SUBAGENT_FALLBACK_PROVIDER_NAME",
    "COLLABORATION_BRIDGE_SCHEMA_VERSION",
    "COLLABORATION_PROVIDER_NAME",
    "COLLABORATION_PROVENANCE_ASSURANCE",
    "CodexSubagentFallbackResearchProvider",
    "CollaborationCodexResearcherProvider",
    "CollaborationCodexSubagentTransport",
    "import_collaboration_response",
]
