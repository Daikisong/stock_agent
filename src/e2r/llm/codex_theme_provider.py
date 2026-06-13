"""Codex CLI-backed provider for LLM-assisted theme routing."""

from __future__ import annotations

import json
import os
import re
import signal
import shlex
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping, Sequence

from e2r.env import load_project_env
from e2r.llm.theme_provider import build_theme_route_messages
from e2r.llm.theme_schemas import ThemeRouteInput, ThemeRouteOutput, validate_theme_route_output


THEME_ROUTE_OUTPUT_JSON_SCHEMA: Mapping[str, object] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "status": {
            "type": "string",
            "enum": [
                "no_transition",
                "mixed_route",
                "transition_detected",
                "provider_error",
                "invalid_provider_output",
                "insufficient_evidence",
                "needs_more_evidence",
                "more_evidence_needed",
                "blocked",
                "uncertain",
                "unknown",
            ],
        },
        "transition_detected": {"type": "boolean"},
        "route_confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "emerging_theme_id": {"type": ["string", "null"]},
        "primary_route_id": {"type": ["string", "null"]},
        "large_sector_id": {"type": ["string", "null"]},
        "canonical_archetype_id": {"type": ["string", "null"]},
        "secondary_archetype_ids": {"type": "array", "items": {"type": "string"}},
        "normalized_parsed_fields": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "key": {"type": "string"},
                    "value": {"type": ["boolean", "number", "string"]},
                },
                "required": ["key", "value"],
            },
        },
        "diagnostic_scores": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "key": {"type": "string"},
                    "value": {"type": "number", "minimum": 0, "maximum": 100},
                },
                "required": ["key", "value"],
            },
        },
        "evidence_slots": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "slot": {"type": "string"},
                    "status": {"type": "string", "enum": ["present", "missing", "contradicted", "unknown"]},
                    "evidence_refs": {"type": "array", "items": {"type": "string"}},
                    "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                    "missing_reason": {"type": ["string", "null"]},
                },
                "required": ["slot", "status", "evidence_refs", "confidence", "missing_reason"],
            },
        },
        "missing_information": {"type": "array", "items": {"type": "string"}},
        "suggested_queries": {"type": "array", "items": {"type": "string"}},
        "blocked_reason": {"type": ["string", "null"]},
    },
    "required": [
        "status",
        "transition_detected",
        "route_confidence",
        "emerging_theme_id",
        "primary_route_id",
        "large_sector_id",
        "canonical_archetype_id",
        "secondary_archetype_ids",
        "normalized_parsed_fields",
        "diagnostic_scores",
        "evidence_slots",
        "missing_information",
        "suggested_queries",
        "blocked_reason",
    ],
}


@dataclass(frozen=True)
class CodexCLIThemeRouteProvider:
    """Use ``codex exec`` as a subprocess-based ThemeRouteProvider.

    The repository pipeline cannot call this chat session's sub-agent tool
    directly. This adapter gives the pipeline the same practical behavior by
    asking a non-interactive Codex process for a schema-validated route JSON.
    """

    codex_command: str = "codex"
    model: str | None = None
    profile: str | None = None
    working_directory: str | Path | None = None
    timeout_seconds: float = 180.0
    sandbox: str = "read-only"
    approval_policy: str = "never"
    extra_args: tuple[str, ...] = field(default_factory=tuple)

    def route(self, inputs: ThemeRouteInput) -> ThemeRouteOutput:
        with tempfile.TemporaryDirectory(prefix="e2r_codex_theme_") as tmpdir:
            tmp = Path(tmpdir)
            schema_path = tmp / "theme_route_schema.json"
            output_path = tmp / "theme_route_output.json"
            schema_path.write_text(json.dumps(THEME_ROUTE_OUTPUT_JSON_SCHEMA, ensure_ascii=False), encoding="utf-8")
            command = self._command(schema_path=schema_path, output_path=output_path)
            try:
                completed = _run_codex_command(
                    command,
                    prompt=_codex_theme_prompt(inputs),
                    timeout=self.timeout_seconds,
                )
            except subprocess.TimeoutExpired:
                return ThemeRouteOutput(status="provider_error", blocked_reason="codex_cli_timeout")
            except OSError as exc:
                return ThemeRouteOutput(status="provider_error", blocked_reason=f"codex_cli_os_error:{type(exc).__name__}")
            raw = output_path.read_text(encoding="utf-8") if output_path.exists() else completed.stdout
        data = _json_object_from_text(raw)
        if data is not None:
            return validate_theme_route_output(_normalise_schema_maps(data))
        if completed.returncode != 0:
            reason = _clean_error(completed.stderr or completed.stdout or f"codex_cli_exit_{completed.returncode}")
            return ThemeRouteOutput(status="provider_error", blocked_reason=reason)
        return ThemeRouteOutput(status="invalid_provider_output", blocked_reason="codex_cli_output_not_json")

    def _command(self, *, schema_path: Path, output_path: Path) -> list[str]:
        command = [
            self.codex_command,
            "--sandbox",
            self.sandbox,
            "--ask-for-approval",
            self.approval_policy,
            "exec",
            "--ephemeral",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "--color",
            "never",
        ]
        if self.working_directory is not None:
            command.extend(("-C", str(self.working_directory)))
        if self.model:
            command.extend(("-m", self.model))
        if self.profile:
            command.extend(("-p", self.profile))
        command.extend(self.extra_args)
        command.append("-")
        return command


def _run_codex_command(command: Sequence[str], *, prompt: str, timeout: float) -> subprocess.CompletedProcess[str]:
    process = subprocess.Popen(
        list(command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=(os.name == "posix"),
    )
    try:
        stdout, stderr = process.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        _terminate_process_tree(process)
        raise
    return subprocess.CompletedProcess(list(command), process.returncode, stdout, stderr)


def _terminate_process_tree(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    if os.name == "posix":
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        try:
            process.wait(timeout=5)
            return
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                return
            process.wait(timeout=5)
            return
    process.kill()
    process.wait(timeout=5)


def build_theme_route_provider_from_env(
    environ: Mapping[str, str] | None = None,
    *,
    working_directory: str | Path | None = None,
) -> CodexCLIThemeRouteProvider | None:
    """Build the optional route provider selected by environment variables."""

    if environ is None:
        load_project_env()
        env = os.environ
    else:
        env = environ
    mode = (env.get("E2R_THEME_ROUTE_PROVIDER") or "").strip().lower()
    if mode not in {"codex", "codex-cli", "codex_cli"}:
        return None
    return CodexCLIThemeRouteProvider(
        codex_command=(env.get("E2R_CODEX_THEME_COMMAND") or "codex").strip() or "codex",
        model=_optional_env(env, "E2R_CODEX_THEME_MODEL"),
        profile=_optional_env(env, "E2R_CODEX_THEME_PROFILE"),
        working_directory=_optional_env(env, "E2R_CODEX_THEME_WORKDIR") or working_directory,
        timeout_seconds=_float_env(env, "E2R_CODEX_THEME_TIMEOUT_SECONDS", 180.0),
        sandbox=(env.get("E2R_CODEX_THEME_SANDBOX") or "read-only").strip() or "read-only",
        approval_policy=(env.get("E2R_CODEX_THEME_APPROVAL_POLICY") or "never").strip() or "never",
        extra_args=tuple(shlex.split(env.get("E2R_CODEX_THEME_EXTRA_ARGS") or "")),
    )


def build_default_codex_theme_route_provider(
    *,
    working_directory: str | Path | None = None,
) -> CodexCLIThemeRouteProvider | None:
    """Build the operational Codex route provider while preserving env config."""

    load_project_env()
    env = dict(os.environ)
    env["E2R_THEME_ROUTE_PROVIDER"] = "codex"
    return build_theme_route_provider_from_env(env, working_directory=working_directory)


def _codex_theme_prompt(inputs: ThemeRouteInput) -> str:
    system, user = build_theme_route_messages(inputs)
    return "\n\n".join(
        (
            str(system["content"]),
            "Return exactly one JSON object matching the provided schema. Do not include markdown.",
            "For normalized_parsed_fields and diagnostic_scores, output arrays of {key, value} objects; use [] when empty.",
            str(user["content"]),
        )
    )


def _json_object_from_text(text: str) -> Mapping[str, object] | None:
    clean = text.strip()
    if not clean:
        return None
    try:
        parsed = json.loads(clean)
        return parsed if isinstance(parsed, Mapping) else None
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{.*\}", clean, re.DOTALL)
    if not match:
        return None
    try:
        parsed = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, Mapping) else None


def _normalise_schema_maps(data: Mapping[str, object]) -> Mapping[str, object]:
    normalized = dict(data)
    for field_name in ("normalized_parsed_fields", "diagnostic_scores"):
        value = normalized.get(field_name)
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
            mapped: dict[str, object] = {}
            for item in value:
                if not isinstance(item, Mapping):
                    continue
                key = str(item.get("key") or "").strip()
                if not key:
                    continue
                mapped[key] = item.get("value")
            normalized[field_name] = mapped
    return normalized


def _clean_error(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()[:240] or "codex_cli_failed"


def _optional_env(env: Mapping[str, str], key: str) -> str | None:
    value = (env.get(key) or "").strip()
    return value or None


def _float_env(env: Mapping[str, str], key: str, default: float) -> float:
    try:
        return float(env.get(key) or default)
    except (TypeError, ValueError):
        return default


__all__ = [
    "CodexCLIThemeRouteProvider",
    "THEME_ROUTE_OUTPUT_JSON_SCHEMA",
    "build_default_codex_theme_route_provider",
    "build_theme_route_provider_from_env",
]
