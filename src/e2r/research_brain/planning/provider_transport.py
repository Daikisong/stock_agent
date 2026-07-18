"""Structured provider transports for canonical Research Brain planners."""

from __future__ import annotations

import http.client
import ipaddress
import json
import os
import re
import signal
import subprocess
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence


_OLLAMA_MAX_RESPONSE_BYTES = 32 * 1024 * 1024
_OLLAMA_MAX_IDENTITY_RESPONSE_BYTES = 2 * 1024 * 1024


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
    codex_command: str = "codex"
    model: str | None = None
    profile: str | None = None
    working_directory: str | Path | None = None
    timeout_seconds: float = 180.0
    sandbox: str = "read-only"
    approval_policy: str = "never"
    extra_args: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.codex_command.strip():
            raise ValueError("structured provider command must be non-empty")
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
        if self.model and self.model != "codex-cli-default":
            command.extend(("-m", self.model))
        if self.profile:
            command.extend(("-p", self.profile))
        command.extend(self.extra_args)
        command.append("-")
        return command


@dataclass
class OllamaStructuredProviderTransport:
    """Schema-constrained Ollama chat transport for an explicit local route."""

    base_url: str = "http://127.0.0.1:11434"
    model: str = "qwen3.5:27b"
    timeout_seconds: float = 900.0
    context_length: int = 262_144
    max_output_tokens: int = 32_768
    prompt_character_limit: int = 500_000
    temperature: float = 0.0
    seed: int = 42
    think: bool = False
    keep_alive: int | str = -1
    model_digest: str | None = None
    server_version: str | None = None

    def __post_init__(self) -> None:
        self.base_url = self.base_url.rstrip("/")
        parsed = urllib.parse.urlparse(self.base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Ollama base URL must be an absolute HTTP(S) URL")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("Ollama base URL must not contain credentials")
        if (
            parsed.path not in {"", "/"}
            or parsed.params
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("Ollama base URL must not contain a path, query, or fragment")
        hostname = str(parsed.hostname or "").casefold()
        try:
            loopback = ipaddress.ip_address(hostname).is_loopback
        except ValueError:
            loopback = hostname == "localhost"
        if not loopback:
            raise ValueError("Ollama base URL must use a loopback host")
        if not self.model.strip():
            raise ValueError("Ollama model must be non-empty")
        if self.timeout_seconds <= 0:
            raise ValueError("Ollama timeout must be positive")
        if isinstance(self.context_length, bool) or self.context_length < 8_192:
            raise ValueError("Ollama context length must be at least 8192")
        if (
            isinstance(self.max_output_tokens, bool)
            or self.max_output_tokens <= 0
            or self.max_output_tokens >= self.context_length
        ):
            raise ValueError("Ollama output token reserve is invalid")
        if (
            isinstance(self.prompt_character_limit, bool)
            or self.prompt_character_limit <= 0
        ):
            raise ValueError("Ollama prompt character limit must be positive")
        if not 0 <= self.temperature <= 2:
            raise ValueError("Ollama temperature must be between 0 and 2")
        if isinstance(self.seed, bool):
            raise ValueError("Ollama seed must be an integer")
        if self.model_digest is not None and re.fullmatch(
            r"[0-9a-f]{64}", self.model_digest
        ) is None:
            raise ValueError("Ollama model digest must be a SHA-256 hex digest")
        if self.server_version is not None and not self.server_version.strip():
            raise ValueError("Ollama server version must be non-empty")

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
        if len(prompt) > self.prompt_character_limit:
            raise StructuredProviderRejected(
                f"ollama_prompt_transport_too_large:{len(prompt)}:"
                f"max={self.prompt_character_limit}"
            )
        request_body = {
            "model": self.model,
            "stream": False,
            "think": self.think,
            "format": dict(output_schema),
            "messages": [{"role": "user", "content": prompt}],
            "options": {
                "temperature": self.temperature,
                "seed": self.seed,
                "num_ctx": self.context_length,
                "num_predict": self.max_output_tokens,
            },
            "keep_alive": self.keep_alive,
        }
        request = urllib.request.Request(
            f"{self.base_url}/api/chat",
            data=json.dumps(request_body, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(
                request,
                timeout=self.timeout_seconds,
            ) as response:
                raw_envelope = _bounded_response_text(
                    response,
                    max_bytes=_OLLAMA_MAX_RESPONSE_BYTES,
                    response_name="Ollama chat",
                )
        except urllib.error.HTTPError as exc:
            try:
                detail = exc.read(_OLLAMA_MAX_IDENTITY_RESPONSE_BYTES + 1).decode(
                    "utf-8", errors="replace"
                )
            except OSError:
                detail = str(exc)
            raise StructuredProviderUnavailable(
                f"ollama_http_error:{exc.code}:{clean_provider_error(detail)}"
            ) from exc
        except UnicodeError as exc:
            raise StructuredProviderRejected(
                "Ollama returned malformed UTF-8"
            ) from exc
        except (
            urllib.error.URLError,
            TimeoutError,
            OSError,
            http.client.HTTPException,
        ) as exc:
            raise StructuredProviderUnavailable(
                f"ollama_transport_error:{type(exc).__name__}:"
                f"{clean_provider_error(str(exc))}"
            ) from exc
        try:
            envelope = json.loads(raw_envelope)
        except json.JSONDecodeError as exc:
            raise StructuredProviderRejected(
                "Ollama returned a non-JSON response envelope"
            ) from exc
        if not isinstance(envelope, Mapping):
            raise StructuredProviderRejected(
                "Ollama response envelope must be an object"
            )
        if envelope.get("error"):
            raise StructuredProviderUnavailable(
                f"ollama_provider_error:{clean_provider_error(str(envelope['error']))}"
            )
        message = envelope.get("message")
        content = message.get("content") if isinstance(message, Mapping) else None
        if not isinstance(content, str):
            raise StructuredProviderRejected(
                "Ollama response is missing message.content"
            )
        if (
            envelope.get("done") is not True
            or envelope.get("done_reason") != "stop"
        ):
            raise StructuredProviderRejected(
                "Ollama response did not finish with stop"
            )
        prompt_eval_count = envelope.get("prompt_eval_count")
        if (
            isinstance(prompt_eval_count, bool)
            or not isinstance(prompt_eval_count, int)
            or prompt_eval_count <= 0
        ):
            raise StructuredProviderRejected(
                "Ollama response is missing prompt token accounting"
            )
        if prompt_eval_count >= self.context_length - self.max_output_tokens:
            raise StructuredProviderRejected(
                "Ollama prompt reached the reserved context boundary"
            )
        payload = json_object_from_text(content)
        if payload is None:
            raise StructuredProviderRejected(
                "Ollama returned non-object structured output"
            )
        return StructuredProviderResponse(
            payload=payload,
            raw_response=content,
            stderr="",
            returncode=0,
        )

    def provider_identity(self) -> Mapping[str, Any]:
        """Return every inference setting that can change a cached response."""

        self.resolve_provider_identity()
        return {
            "transport_class": self.__class__.__qualname__,
            "base_url": self.base_url,
            "model": self.model,
            "model_digest": self.model_digest,
            "server_version": self.server_version,
            "context_length": self.context_length,
            "max_output_tokens": self.max_output_tokens,
            "prompt_character_limit": self.prompt_character_limit,
            "temperature": self.temperature,
            "seed": self.seed,
            "think": self.think,
            "keep_alive": self.keep_alive,
        }

    def resolve_provider_identity(self) -> None:
        """Freeze the mutable model tag to a digest before cache lookup."""

        if self.model_digest is not None and self.server_version is not None:
            return
        tags = self._get_json("/api/tags")
        models = tags.get("models")
        if not isinstance(models, list):
            raise StructuredProviderUnavailable(
                "ollama_identity_error:model list is missing"
            )
        matching = next(
            (
                row
                for row in models
                if isinstance(row, Mapping)
                and self.model
                in {
                    str(row.get("name") or ""),
                    str(row.get("model") or ""),
                }
            ),
            None,
        )
        digest = str(matching.get("digest") or "") if matching is not None else ""
        if re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            raise StructuredProviderUnavailable(
                f"ollama_identity_error:model digest unavailable:{self.model}"
            )
        version_payload = self._get_json("/api/version")
        version = str(version_payload.get("version") or "").strip()
        if not version:
            raise StructuredProviderUnavailable(
                "ollama_identity_error:server version unavailable"
            )
        self.model_digest = digest
        self.server_version = version

    def _get_json(self, path: str) -> Mapping[str, Any]:
        request = urllib.request.Request(f"{self.base_url}{path}", method="GET")
        try:
            with urllib.request.urlopen(
                request,
                timeout=min(self.timeout_seconds, 30.0),
            ) as response:
                raw = _bounded_response_text(
                    response,
                    max_bytes=_OLLAMA_MAX_IDENTITY_RESPONSE_BYTES,
                    response_name="Ollama identity",
                )
        except UnicodeError as exc:
            raise StructuredProviderRejected(
                "Ollama identity response contains malformed UTF-8"
            ) from exc
        except (
            urllib.error.URLError,
            urllib.error.HTTPError,
            TimeoutError,
            OSError,
            http.client.HTTPException,
        ) as exc:
            raise StructuredProviderUnavailable(
                f"ollama_identity_error:{type(exc).__name__}:"
                f"{clean_provider_error(str(exc))}"
            ) from exc
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise StructuredProviderRejected(
                "Ollama identity response is not JSON"
            ) from exc
        if not isinstance(value, Mapping):
            raise StructuredProviderRejected(
                "Ollama identity response must be an object"
            )
        return value


def _bounded_response_text(
    response: Any,
    *,
    max_bytes: int,
    response_name: str,
) -> str:
    content_length = (
        response.headers.get("Content-Length") if response.headers else None
    )
    if content_length is not None:
        try:
            if int(content_length) > max_bytes:
                raise StructuredProviderRejected(
                    f"{response_name} response exceeds {max_bytes} bytes"
                )
        except ValueError:
            raise StructuredProviderRejected(
                f"{response_name} response has invalid Content-Length"
            )
    raw = response.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise StructuredProviderRejected(
            f"{response_name} response exceeds {max_bytes} bytes"
        )
    return raw.decode("utf-8")


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
    "OllamaStructuredProviderTransport",
    "StructuredProviderRejected",
    "StructuredProviderResponse",
    "StructuredProviderUnavailable",
    "clean_provider_error",
    "json_object_from_text",
    "run_codex_command",
    "terminate_process_tree",
]
