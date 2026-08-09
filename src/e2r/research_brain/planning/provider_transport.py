"""Codex-only structured transport for canonical Research Brain planners."""

from __future__ import annotations

import json
import os
import re
import signal
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.codex_cli_contract import (
    CODEX_EXECUTABLE,
    codex_isolation_args,
    codex_subprocess_env,
)


class StructuredProviderUnavailable(RuntimeError):
    """Provider process could not return a usable response."""


class StructuredProviderRejected(RuntimeError):
    """Provider response was returned but violated the structured contract."""


@dataclass(frozen=True)
class StructuredProviderResponse:
    payload: Mapping[str, Any]
    raw_response: str
    stderr: str
    returncode: int


@dataclass
class CodexStructuredProviderTransport:
    working_directory: str | Path | None = None
    timeout_seconds: float = 180.0
    sandbox: str = "read-only"
    approval_policy: str = "never"

    def __post_init__(self) -> None:
        if self.timeout_seconds <= 0:
            raise ValueError("structured provider timeout must be positive")
        if not self.sandbox.strip() or not self.approval_policy.strip():
            raise ValueError("structured provider sandbox and approval policy are required")

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
        schema_name: str,
    ) -> StructuredProviderResponse:
        if not prompt.strip() or not schema_name.strip():
            raise ValueError("structured provider requires prompt and schema name")
        if re.fullmatch(r"[A-Za-z0-9_.-]+", schema_name) is None:
            raise ValueError("structured provider schema name contains unsafe characters")
        with tempfile.TemporaryDirectory(prefix="e2r_structured_provider_") as tmpdir:
            root = Path(tmpdir)
            schema_path = root / f"{schema_name}.schema.json"
            output_path = root / f"{schema_name}.output.json"
            schema_path.write_text(
                json.dumps(output_schema, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )
            command = self.command(
                schema_path=schema_path,
                output_path=output_path,
            )
            try:
                completed = run_codex_command(
                    command,
                    prompt=prompt,
                    timeout=self.timeout_seconds,
                )
            except subprocess.TimeoutExpired as exc:
                raise StructuredProviderUnavailable("codex_cli_timeout") from exc
            except OSError as exc:
                raise StructuredProviderUnavailable(
                    f"codex_cli_os_error:{type(exc).__name__}"
                ) from exc
            raw = (
                output_path.read_text(encoding="utf-8")
                if output_path.exists()
                else completed.stdout
            )
        payload = json_object_from_text(raw)
        if payload is None:
            if completed.returncode != 0:
                detail = clean_provider_error(completed.stderr or completed.stdout)
                raise StructuredProviderUnavailable(detail)
            raise StructuredProviderRejected("provider returned non-json output")
        if completed.returncode != 0:
            raise StructuredProviderUnavailable(
                clean_provider_error(completed.stderr or completed.stdout)
            )
        return StructuredProviderResponse(
            payload=payload,
            raw_response=raw,
            stderr=completed.stderr,
            returncode=completed.returncode,
        )

    def command(self, *, schema_path: Path, output_path: Path) -> list[str]:
        command = [
            CODEX_EXECUTABLE,
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
        command.extend(codex_isolation_args())
        command.append("-")
        return command


def run_codex_command(
    command: Sequence[str],
    *,
    prompt: str,
    timeout: float,
) -> subprocess.CompletedProcess[str]:
    process = subprocess.Popen(
        list(command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=(os.name == "posix"),
        env=codex_subprocess_env(),
    )
    try:
        stdout, stderr = process.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        terminate_process_tree(process)
        raise
    return subprocess.CompletedProcess(
        list(command),
        process.returncode,
        stdout,
        stderr,
    )


def terminate_process_tree(process: subprocess.Popen[str]) -> None:
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


def json_object_from_text(text: str) -> Mapping[str, Any] | None:
    clean = text.strip()
    if not clean:
        return None
    try:
        parsed = json.loads(clean)
        return parsed if isinstance(parsed, Mapping) else None
    except json.JSONDecodeError:
        pass
    decoder = json.JSONDecoder()
    for match in re.finditer(r"\{", clean):
        try:
            parsed, _ = decoder.raw_decode(clean[match.start() :])
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, Mapping):
            return parsed
    return None


def clean_provider_error(text: str) -> str:
    clean = re.sub(r"\s+", " ", str(text or "")).strip()
    return clean[-2000:] or "structured_provider_error"


__all__ = [
    "CodexStructuredProviderTransport",
    "StructuredProviderRejected",
    "StructuredProviderResponse",
    "StructuredProviderUnavailable",
    "clean_provider_error",
    "codex_isolation_args",
    "json_object_from_text",
    "run_codex_command",
    "terminate_process_tree",
]
