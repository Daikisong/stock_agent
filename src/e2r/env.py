"""Project-local environment loading helpers."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Mapping


def load_project_env(env_path: str | Path | None = ".env", *, override: bool = False) -> dict[str, str]:
    """Load simple KEY=VALUE pairs from a project .env file.

    Existing process environment values are preserved unless ``override`` is
    explicitly true. The parser intentionally supports only the common .env
    shape used by this project and ignores comments or malformed lines.
    """

    if env_path is None:
        return {}
    path = _resolve_env_path(env_path)
    if path is None or not path.exists():
        return {}

    loaded: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not key or key.startswith("#"):
            continue
        value = _clean_env_value(value)
        if override or key not in os.environ:
            os.environ[key] = value
            loaded[key] = value
    return loaded


def env_presence(keys: tuple[str, ...], *, env: Mapping[str, str] | None = None) -> dict[str, bool]:
    source = os.environ if env is None else env
    return {key: bool(source.get(key)) for key in keys}


def _resolve_env_path(env_path: str | Path) -> Path | None:
    path = Path(env_path)
    if path.is_absolute():
        return path
    cwd_path = Path.cwd() / path
    if cwd_path.exists():
        return cwd_path
    for parent in Path(__file__).resolve().parents:
        candidate = parent / path
        if candidate.exists():
            return candidate
    return cwd_path


def _clean_env_value(value: str) -> str:
    cleaned = value.strip()
    if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {"'", '"'}:
        return cleaned[1:-1]
    return cleaned


__all__ = ["env_presence", "load_project_env"]
