"""Secret-safe project credential preflight for bounded live providers."""

from __future__ import annotations

import os
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Mapping

from e2r.env import load_project_env

from .provider_capabilities import ProviderCapability, provider_capabilities


class CredentialState(str, Enum):
    PRESENT = "PRESENT"
    MISSING = "MISSING"
    INVALID = "INVALID"
    AUTH_FAILED = "AUTH_FAILED"
    NOT_REQUIRED = "NOT_REQUIRED"


@dataclass(frozen=True)
class CredentialAuditRow:
    provider_name: str
    required_env_keys: tuple[str, ...]
    credential_state: str
    present_env_keys: tuple[str, ...]
    missing_env_keys: tuple[str, ...]
    blocker_code: str | None

    def __post_init__(self) -> None:
        CredentialState(self.credential_state)
        if not self.provider_name.strip():
            raise ValueError("credential audit provider required")
        if self.credential_state == CredentialState.PRESENT.value and self.blocker_code:
            raise ValueError("present credential cannot carry blocker")
        if self.credential_state in {CredentialState.MISSING.value, CredentialState.INVALID.value}:
            if not self.blocker_code:
                raise ValueError("missing or invalid credential requires blocker")

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def audit_live_credentials(
    *,
    env_file: str | Path | None = ".env",
    environment: Mapping[str, str] | None = None,
    load_env_file: bool = True,
    capabilities: tuple[ProviderCapability, ...] | None = None,
) -> dict[str, object]:
    loaded_key_names: tuple[str, ...] = ()
    if load_env_file and environment is None:
        loaded = load_project_env(env_file, override=False)
        loaded_key_names = tuple(sorted(loaded))
    env = os.environ if environment is None else environment
    rows = tuple(
        _audit_provider(capability, env=env)
        for capability in (capabilities or provider_capabilities())
    )
    return {
        "schema_version": "e2r_live_credential_audit_v1",
        "env_file_requested": str(env_file) if env_file is not None else None,
        "env_file_loaded_key_names": list(loaded_key_names),
        "secret_values_emitted": False,
        "provider_count": len(rows),
        "credential_state_counts": {
            state.value: sum(row.credential_state == state.value for row in rows)
            for state in CredentialState
        },
        "rows": [row.to_dict() for row in rows],
    }


def _audit_provider(
    capability: ProviderCapability,
    *,
    env: Mapping[str, str],
) -> CredentialAuditRow:
    keys = capability.auth_env_keys
    if not keys:
        return CredentialAuditRow(
            provider_name=capability.provider_name,
            required_env_keys=(),
            credential_state=CredentialState.NOT_REQUIRED.value,
            present_env_keys=(),
            missing_env_keys=(),
            blocker_code=None,
        )
    present = tuple(key for key in keys if str(env.get(key) or "").strip())
    alternatives = capability.provider_name == "OpenDART"
    required_present = bool(present) if alternatives else len(present) == len(keys)
    if not required_present:
        missing = tuple(key for key in keys if key not in present)
        return CredentialAuditRow(
            provider_name=capability.provider_name,
            required_env_keys=keys,
            credential_state=CredentialState.MISSING.value,
            present_env_keys=present,
            missing_env_keys=missing,
            blocker_code="MISSING_CREDENTIAL",
        )
    invalid = tuple(key for key in present if _looks_invalid(str(env.get(key) or "")))
    if invalid:
        return CredentialAuditRow(
            provider_name=capability.provider_name,
            required_env_keys=keys,
            credential_state=CredentialState.INVALID.value,
            present_env_keys=present,
            missing_env_keys=(),
            blocker_code="INVALID_CREDENTIAL",
        )
    return CredentialAuditRow(
        provider_name=capability.provider_name,
        required_env_keys=keys,
        credential_state=CredentialState.PRESENT.value,
        present_env_keys=present,
        missing_env_keys=(),
        blocker_code=None,
    )


def _looks_invalid(value: str) -> bool:
    normalized = value.strip().casefold()
    return len(normalized) < 4 or any(
        token in normalized
        for token in ("changeme", "replace_me", "your_key", "dummy", "example")
    )


__all__ = [
    "CredentialAuditRow",
    "CredentialState",
    "audit_live_credentials",
]
