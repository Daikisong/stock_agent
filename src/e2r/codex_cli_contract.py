"""Immutable Codex-only subprocess contract.

This module is the single launch boundary for Codex subprocesses.  It must not
grow a configurable executable, model-provider switch, endpoint override,
fallback command, or local-model environment passthrough.  In particular,
local LLM runtimes are not an alternative transport for this project.
"""

from __future__ import annotations

import os
from typing import Mapping


CODEX_EXECUTABLE = "codex"
# These flags prevent user-level Codex configuration from silently selecting a
# different provider.  Callers receive this exact tuple and cannot append
# provider, endpoint, profile, model, or fallback arguments.
_CODEX_ISOLATION_ARGS = ("--ignore-user-config", "--ignore-rules")
# Positive allowlist only.  Provider routing variables are intentionally not
# named here: adding an environment variable requires an explicit code review
# of this boundary instead of relying on an ever-growing denylist.
_PASSTHROUGH_ENV_KEYS = frozenset(
    {
        "HOME",
        "LANG",
        "LC_ALL",
        "LC_CTYPE",
        "LOGNAME",
        "OPENAI_API_KEY",
        "OPENAI_ORGANIZATION",
        "OPENAI_ORG_ID",
        "OPENAI_PROJECT",
        "OPENAI_PROJECT_ID",
        "PATH",
        "SHELL",
        "SSL_CERT_DIR",
        "SSL_CERT_FILE",
        "SYSTEMROOT",
        "TEMP",
        "TMP",
        "TMPDIR",
        "USER",
    }
)


def codex_isolation_args() -> tuple[str, ...]:
    """Return fixed flags; callers cannot append provider or endpoint config."""

    return _CODEX_ISOLATION_ARGS


def codex_subprocess_env(environ: Mapping[str, str] | None = None) -> dict[str, str]:
    """Build a minimal environment without endpoint, provider, or proxy routing.

    Authentication may come from ``OPENAI_API_KEY`` or the normal Codex auth
    file under ``HOME``.  Endpoint overrides, model-provider variables, proxy
    variables, and project ``.env`` routing settings are intentionally absent.
    """

    source = os.environ if environ is None else environ
    return {
        key: str(source[key])
        for key in sorted(_PASSTHROUGH_ENV_KEYS)
        if source.get(key) is not None
    }


__all__ = ["CODEX_EXECUTABLE", "codex_isolation_args", "codex_subprocess_env"]
