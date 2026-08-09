"""Pure collaboration-journal envelope validation for offline receipts."""

from __future__ import annotations

import hashlib
import json
import math
import re
from typing import Any, Mapping, Sequence

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

_REQUEST_ID_RE = re.compile(r"^COLLABREQ-[0-9a-f]{64}$")
_AGENT_ID_RE = re.compile(r"^[A-Za-z0-9._:/-]{1,200}$")
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


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _json_schema_equal(left: Any, right: Any) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return isinstance(left, bool) and isinstance(right, bool) and left == right
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return (
            math.isfinite(float(left))
            and math.isfinite(float(right))
            and left == right
        )
    if isinstance(left, Mapping) or isinstance(right, Mapping):
        return (
            isinstance(left, Mapping)
            and isinstance(right, Mapping)
            and set(left) == set(right)
            and all(_json_schema_equal(left[key], right[key]) for key in left)
        )
    if isinstance(left, list) or isinstance(right, list):
        return (
            isinstance(left, list)
            and isinstance(right, list)
            and len(left) == len(right)
            and all(
                _json_schema_equal(left_item, right_item)
                for left_item, right_item in zip(left, right)
            )
        )
    return type(left) is type(right) and left == right


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


def _expected_provider_identity() -> Mapping[str, Any]:
    return {
        "transport_class": "CollaborationCodexSubagentTransport",
        "bridge_schema_version": COLLABORATION_BRIDGE_SCHEMA_VERSION,
        "provider_route": "COLLABORATION_CODEX_SUBAGENT",
        "provenance_assurance": COLLABORATION_PROVENANCE_ASSURANCE,
        "direct_score_or_stage_authority": False,
    }


def validate_collaboration_request(request: Mapping[str, Any]) -> Mapping[str, Any]:
    if set(request) != _REQUEST_ENVELOPE_KEYS:
        raise ValueError("collaboration request envelope key roster mismatch")
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
        raise ValueError("collaboration request schema name and pass name mismatch")
    if request.get("response_import_required") is not True:
        raise ValueError("collaboration request must require response import")
    prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    output_schema_hash = canonical_hash(output_schema)
    provider_identity = request.get("provider_identity")
    if not isinstance(provider_identity, Mapping):
        raise ValueError("collaboration provider identity is missing")
    if provider_identity != _expected_provider_identity():
        raise ValueError("collaboration request provider identity is invalid")
    provider_identity_hash = canonical_hash(provider_identity)
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
    if request_id != "COLLABREQ-" + canonical_hash(identity):
        raise ValueError("collaboration request id hash mismatch")
    if (
        request.get("score_or_stage_authority") is not False
        or request.get("production_score_authority") is not False
    ):
        raise ValueError("collaboration request cannot have score authority")
    _validate_schema_definition(output_schema, path="$")
    return dict(request)


def _validate_agent_provenance(provenance: Mapping[str, Any]) -> Mapping[str, str]:
    agent_id = str(provenance.get("agent_id") or "").strip()
    task = str(provenance.get("canonical_task_name") or "").strip()
    model = str(provenance.get("agent_model") or "").strip()
    if _AGENT_ID_RE.fullmatch(agent_id) is None:
        raise ValueError("collaboration agent_id is invalid")
    if not task.startswith("/root/") or _AGENT_ID_RE.fullmatch(task) is None:
        raise ValueError("collaboration canonical task name is invalid")
    if not model or len(model) > 200:
        raise ValueError("collaboration agent model is invalid")
    return {
        "agent_id": agent_id,
        "canonical_task_name": task,
        "agent_model": model,
        "agent_surface": "CODEX_COLLABORATION_SUBAGENT",
        "provenance_assurance": COLLABORATION_PROVENANCE_ASSURANCE,
    }


def validate_collaboration_response_envelope(
    *,
    request: Mapping[str, Any],
    envelope: Mapping[str, Any],
) -> Mapping[str, Any]:
    request = validate_collaboration_request(request)
    if set(envelope) != _RESPONSE_ENVELOPE_KEYS:
        raise ValueError("collaboration response envelope key roster mismatch")
    if envelope.get("schema_version") != COLLABORATION_RESPONSE_SCHEMA_VERSION:
        raise ValueError("unknown collaboration response schema")
    if envelope.get("request_id") != request["request_id"]:
        raise ValueError("collaboration response request id mismatch")
    for key in ("prompt_hash", "output_schema_hash", "provider_identity_hash"):
        if envelope.get(key) != request[key]:
            raise ValueError(f"collaboration response {key} mismatch")
    payload = envelope.get("payload")
    if not isinstance(payload, Mapping):
        raise ValueError("collaboration response payload must be an object")
    payload_hash = canonical_hash(payload)
    if envelope.get("payload_hash") != payload_hash:
        raise ValueError("collaboration response payload hash mismatch")
    provenance = envelope.get("provenance")
    if not isinstance(provenance, Mapping):
        raise ValueError("collaboration response provenance is missing")
    validated_provenance = _validate_agent_provenance(provenance)
    if provenance != validated_provenance:
        raise ValueError("collaboration response provenance mismatch")
    expected_response_id = "COLLABRESP-" + canonical_hash(
        {
            "request_id": request["request_id"],
            "payload_hash": payload_hash,
            "provenance": validated_provenance,
        }
    )
    if envelope.get("response_id") != expected_response_id:
        raise ValueError("collaboration response id hash mismatch")
    if envelope.get("validation") != {
        "draft202012_schema_valid": True,
        "blind_research_output_valid": True,
        "request_hashes_valid": True,
        "downstream_semantic_validation_required": True,
    }:
        raise ValueError("collaboration response validation receipt mismatch")
    if (
        envelope.get("score_or_stage_authority") is not False
        or envelope.get("production_score_authority") is not False
    ):
        raise ValueError("collaboration response cannot have score authority")
    _validate_schema_instance(payload, request["output_schema"], path="$")
    assert_blind_research_output(payload)
    return dict(envelope)


def _validate_schema_definition(schema: Any, *, path: str) -> None:
    if isinstance(schema, bool):
        return
    if not isinstance(schema, Mapping):
        raise ValueError(f"collaboration schema object required:{path}")
    allowed = {
        "type",
        "properties",
        "required",
        "additionalProperties",
        "items",
        "minItems",
        "maxItems",
        "minLength",
        "minimum",
        "maximum",
        "enum",
        "pattern",
        "anyOf",
        "description",
        "$schema",
        "title",
    }
    unknown = set(schema) - allowed
    if unknown:
        raise ValueError(f"unsupported collaboration schema keyword:{path}:{sorted(unknown)}")
    declared_type = schema.get("type")
    allowed_types = {
            "object",
            "array",
            "string",
            "number",
            "integer",
            "boolean",
            "null",
        }
    if "type" in schema:
        if isinstance(declared_type, str):
            declared_types = [declared_type]
        elif (
            isinstance(declared_type, list)
            and declared_type
            and all(isinstance(value, str) for value in declared_type)
            and len(declared_type) == len(set(declared_type))
        ):
            declared_types = declared_type
        else:
            raise ValueError(f"unsupported collaboration schema type:{path}")
        if any(value not in allowed_types for value in declared_types):
            raise ValueError(f"unsupported collaboration schema type:{path}")
    for key in ("description", "title", "$schema"):
        if key in schema and not isinstance(schema[key], str):
            raise ValueError(f"collaboration schema {key} invalid:{path}")
    properties = schema.get("properties")
    if "properties" in schema:
        if not isinstance(properties, Mapping):
            raise ValueError(f"collaboration schema properties invalid:{path}")
        for key, child in properties.items():
            _validate_schema_definition(child, path=f"{path}/{key}")
    required = schema.get("required")
    if "required" in schema and (
        not isinstance(required, Sequence)
        or isinstance(required, (str, bytes))
        or any(not isinstance(value, str) for value in required)
        or len(required) != len(set(required))
    ):
        raise ValueError(f"collaboration schema required invalid:{path}")
    if "items" in schema:
        _validate_schema_definition(schema["items"], path=f"{path}/*")
    additional = schema.get("additionalProperties")
    if "additionalProperties" in schema and not isinstance(
        additional, (bool, Mapping)
    ):
        raise ValueError(f"collaboration schema additionalProperties invalid:{path}")
    if isinstance(additional, Mapping):
        _validate_schema_definition(additional, path=f"{path}/additionalProperties")
    any_of = schema.get("anyOf")
    if "anyOf" in schema:
        if not isinstance(any_of, list) or not any_of:
            raise ValueError(f"collaboration schema anyOf invalid:{path}")
        for index, child in enumerate(any_of):
            _validate_schema_definition(child, path=f"{path}/anyOf/{index}")
    if "pattern" in schema:
        if not isinstance(schema["pattern"], str):
            raise ValueError(f"collaboration schema pattern invalid:{path}")
        try:
            re.compile(schema["pattern"])
        except re.error as exc:
            raise ValueError(f"collaboration schema pattern invalid:{path}") from exc
    enum = schema.get("enum")
    if "enum" in schema:
        if not isinstance(enum, list) or not enum:
            raise ValueError(f"collaboration schema enum invalid:{path}")
        for index, value in enumerate(enum):
            if any(_json_schema_equal(value, prior) for prior in enum[:index]):
                raise ValueError(f"collaboration schema enum duplicates:{path}")
    for key in ("minItems", "maxItems", "minLength"):
        if key in schema and (
            not isinstance(schema[key], int)
            or isinstance(schema[key], bool)
            or schema[key] < 0
        ):
            raise ValueError(f"collaboration schema {key} invalid:{path}")
    for key in ("minimum", "maximum"):
        if key in schema and (
            not isinstance(schema[key], (int, float))
            or isinstance(schema[key], bool)
            or not math.isfinite(float(schema[key]))
        ):
            raise ValueError(f"collaboration schema {key} invalid:{path}")


def _validate_schema_instance(value: Any, schema: Any, *, path: str) -> None:
    if schema is True:
        return
    if schema is False:
        raise ValueError(f"collaboration response schema violation:{path}:falseSchema")
    if "anyOf" in schema:
        matches = 0
        for child in schema["anyOf"]:
            try:
                _validate_schema_instance(value, child, path=path)
            except (TypeError, ValueError):
                continue
            matches += 1
        if matches == 0:
            raise ValueError(f"collaboration response schema violation:{path}:anyOf")
    kind = schema.get("type")
    kinds = kind if isinstance(kind, list) else [kind]
    valid_type = any(_json_schema_type_matches(value, item) for item in kinds)
    if not valid_type:
        raise ValueError(f"collaboration response schema violation:{path}:type")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"collaboration response schema violation:{path}:nonfinite")
    if "enum" in schema and not any(
        _json_schema_equal(value, candidate) for candidate in schema["enum"]
    ):
        raise ValueError(f"collaboration response schema violation:{path}:enum")
    if isinstance(value, Mapping):
        properties = schema.get("properties") or {}
        required = schema.get("required") or ()
        missing = [key for key in required if key not in value]
        if missing:
            raise ValueError(f"collaboration response schema violation:{path}:required")
        if schema.get("additionalProperties") is False and set(value) - set(properties):
            raise ValueError(
                f"collaboration response schema violation:{path}:additionalProperties"
            )
        additional = schema.get("additionalProperties")
        if isinstance(additional, Mapping):
            for key in set(value) - set(properties):
                _validate_schema_instance(value[key], additional, path=f"{path}/{key}")
        for key, child in properties.items():
            if key in value:
                _validate_schema_instance(value[key], child, path=f"{path}/{key}")
    if isinstance(value, list):
        if len(value) < int(schema.get("minItems", 0)):
            raise ValueError(f"collaboration response schema violation:{path}:minItems")
        if "maxItems" in schema and len(value) > int(schema["maxItems"]):
            raise ValueError(f"collaboration response schema violation:{path}:maxItems")
        if "items" in schema:
            for index, item in enumerate(value):
                _validate_schema_instance(item, schema["items"], path=f"{path}/{index}")
    if isinstance(value, str):
        if len(value) < int(schema.get("minLength", 0)):
            raise ValueError(f"collaboration response schema violation:{path}:minLength")
        if "pattern" in schema and re.search(str(schema["pattern"]), value) is None:
            raise ValueError(f"collaboration response schema violation:{path}:pattern")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            raise ValueError(f"collaboration response schema violation:{path}:minimum")
        if "maximum" in schema and value > schema["maximum"]:
            raise ValueError(f"collaboration response schema violation:{path}:maximum")


def _json_schema_type_matches(value: Any, kind: Any) -> bool:
    return {
        "object": isinstance(value, Mapping),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "integer": (
            isinstance(value, int)
            and not isinstance(value, bool)
        )
        or (
            isinstance(value, float)
            and math.isfinite(value)
            and value.is_integer()
        ),
        "boolean": isinstance(value, bool),
        "null": value is None,
        None: True,
    }.get(kind, False)
