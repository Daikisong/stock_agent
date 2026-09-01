"""Strict runtime configuration for the Pro-first local platform.

The tracked ``.yaml`` example is deliberately JSON-compatible YAML.  Keeping
the accepted runtime format to this safe subset avoids a second configuration
parser and, more importantly, prevents executable YAML tags from entering the
local control plane.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlparse

from .ids import canonical_hash


class BrowserConnectionMode(str, Enum):
    CDP_ATTACH = "CDP_ATTACH"
    PERSISTENT_PROFILE = "PERSISTENT_PROFILE"


@dataclass(frozen=True)
class ProBrowserConfig:
    mode: BrowserConnectionMode = BrowserConnectionMode.CDP_ATTACH
    cdp_url: str = "http://127.0.0.1:9222"
    cdp_active_port_file: Path | None = None
    chatgpt_url: str = "https://chatgpt.com/"
    require_manual_login: bool = True
    require_user_start_approval: bool = True
    auto_capture_after_completion: bool = True
    hidden_api_access: bool = False
    persistent_profile_path: Path | None = None
    poll_interval_seconds: float = 5.0
    required_stable_observations: int = 3
    mock_origin_allowed: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.mode, BrowserConnectionMode):
            object.__setattr__(self, "mode", BrowserConnectionMode(self.mode))
        if self.cdp_active_port_file is not None:
            object.__setattr__(
                self,
                "cdp_active_port_file",
                Path(self.cdp_active_port_file).expanduser().resolve(),
            )
        if not self.require_manual_login:
            raise ValueError("ChatGPT login automation is forbidden")
        if not self.require_user_start_approval:
            raise ValueError("live Pro submit requires explicit user approval")
        if self.hidden_api_access:
            raise ValueError("hidden/private ChatGPT API access is forbidden")
        if self.poll_interval_seconds <= 0:
            raise ValueError("poll_interval_seconds must be positive")
        if self.required_stable_observations < 2:
            raise ValueError("completion requires at least two stable observations")
        self._validate_chatgpt_url()
        if self.mode is BrowserConnectionMode.CDP_ATTACH:
            parsed = urlparse(self.cdp_url)
            if parsed.scheme not in {"http", "https"} or parsed.hostname not in {
                "127.0.0.1",
                "localhost",
                "::1",
            }:
                raise ValueError("CDP attach endpoint must be loopback-only")
        elif self.persistent_profile_path is None:
            raise ValueError("PERSISTENT_PROFILE requires a dedicated profile path")

    def _validate_chatgpt_url(self) -> None:
        parsed = urlparse(self.chatgpt_url)
        if parsed.scheme == "https" and parsed.hostname in {"chatgpt.com", "www.chatgpt.com"}:
            return
        if (
            self.mock_origin_allowed
            and parsed.scheme == "http"
            and parsed.hostname in {"127.0.0.1", "localhost", "::1"}
        ):
            return
        raise ValueError("chatgpt_url must be official HTTPS or an explicit loopback mock")


@dataclass(frozen=True)
class ProDashboardRuntimeConfig:
    host: str = "127.0.0.1"
    port: int = 8765

    def __post_init__(self) -> None:
        parsed = urlparse(f"http://{self.host}:{self.port}")
        if parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError("dashboard must remain loopback-only")
        if not 1 <= int(self.port) <= 65_535:
            raise ValueError("dashboard port is outside the TCP range")


@dataclass(frozen=True)
class ProScheduleRuntimeConfig:
    timezone: str = "Asia/Seoul"
    morning_enabled: bool = True
    morning_at: str = "05:30"
    evening_enabled: bool = True
    evening_at: str = "18:30"
    maximum_idle_poll_seconds: float = 60.0

    def __post_init__(self) -> None:
        if self.timezone != "Asia/Seoul":
            raise ValueError("production scheduler timezone must remain Asia/Seoul")
        for value in (self.morning_at, self.evening_at):
            pieces = value.split(":")
            if len(pieces) != 2 or not all(piece.isdigit() for piece in pieces):
                raise ValueError("scheduler times must use HH:MM")
            hour, minute = (int(piece) for piece in pieces)
            if not 0 <= hour <= 23 or not 0 <= minute <= 59:
                raise ValueError("scheduler time is outside the local clock range")
        if self.maximum_idle_poll_seconds <= 0:
            raise ValueError("scheduler poll interval must be positive")


@dataclass(frozen=True)
class ProScanRuntimeConfig:
    production_deep_only: bool = True
    universe_limit: int | None = None
    top_n: int | None = None
    deep_research_min_score: float = 45.0

    def __post_init__(self) -> None:
        if not self.production_deep_only:
            raise ValueError("Pro queue accepts production DEEP_RESEARCH candidates only")
        for label, value in (("universe_limit", self.universe_limit), ("top_n", self.top_n)):
            if value is not None and int(value) <= 0:
                raise ValueError(f"{label} must be positive when configured")
        if not 0 <= float(self.deep_research_min_score) <= 100:
            raise ValueError("deep research threshold must be between 0 and 100")


@dataclass(frozen=True)
class ProSupplementRuntimeConfig:
    core_score_blocker: bool = True
    stage_boundary_gap: bool = True
    hard_break_gap: bool = True
    corroboration_cap: bool = False
    monitoring_gap: bool = False
    full_research_restart: bool = False

    def __post_init__(self) -> None:
        if self.corroboration_cap or self.monitoring_gap:
            raise ValueError("nonblocking gaps may not open supplemental research")
        if self.full_research_restart:
            raise ValueError("a dossier may not restart full Pro research")


@dataclass(frozen=True)
class ProAuthorityRuntimeConfig:
    pro_score_authority: bool = False
    pro_stage_authority: bool = False
    deterministic_score_required: bool = True
    deterministic_stagecourt_required: bool = True

    def __post_init__(self) -> None:
        if self.pro_score_authority or self.pro_stage_authority:
            raise ValueError("Pro output cannot own production score or Stage")
        if not self.deterministic_score_required or not self.deterministic_stagecourt_required:
            raise ValueError("deterministic scorer and StageCourt are mandatory")


@dataclass(frozen=True)
class ProFirstLocalConfig:
    runtime_root: Path
    dashboard: ProDashboardRuntimeConfig
    scheduler: ProScheduleRuntimeConfig
    browser: ProBrowserConfig
    scan: ProScanRuntimeConfig
    supplement: ProSupplementRuntimeConfig
    authority: ProAuthorityRuntimeConfig
    reconciliation_poll_seconds: float = 5.0

    def __post_init__(self) -> None:
        object.__setattr__(self, "runtime_root", Path(self.runtime_root).expanduser().resolve())
        if self.reconciliation_poll_seconds <= 0:
            raise ValueError("reconciliation poll interval must be positive")

    @property
    def database_path(self) -> Path:
        return self.runtime_root / "pro_first.sqlite3"

    @property
    def config_hash(self) -> str:
        return canonical_hash(self.to_dict())

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "runtime": {
                "root": str(self.runtime_root),
                "reconciliation_poll_seconds": self.reconciliation_poll_seconds,
            },
            "dashboard": {
                "host": self.dashboard.host,
                "port": self.dashboard.port,
            },
            "scheduler": {
                "timezone": self.scheduler.timezone,
                "morning": {
                    "enabled": self.scheduler.morning_enabled,
                    "at": self.scheduler.morning_at,
                },
                "evening": {
                    "enabled": self.scheduler.evening_enabled,
                    "at": self.scheduler.evening_at,
                },
                "maximum_idle_poll_seconds": self.scheduler.maximum_idle_poll_seconds,
            },
            "browser": {
                "mode": self.browser.mode.value,
                "cdp_url": self.browser.cdp_url,
                "cdp_active_port_file": (
                    str(self.browser.cdp_active_port_file)
                    if self.browser.cdp_active_port_file is not None
                    else None
                ),
                "chatgpt_url": self.browser.chatgpt_url,
                "require_manual_login": self.browser.require_manual_login,
                "require_user_start_approval": self.browser.require_user_start_approval,
                "auto_capture_after_completion": self.browser.auto_capture_after_completion,
                "hidden_api_access": self.browser.hidden_api_access,
                "poll_interval_seconds": self.browser.poll_interval_seconds,
                "required_stable_observations": self.browser.required_stable_observations,
            },
            "scan": self.scan.__dict__,
            "supplement": self.supplement.__dict__,
            "authority": self.authority.__dict__,
        }


def load_pro_first_local_config(path: str | Path) -> ProFirstLocalConfig:
    """Load and strictly validate the safe JSON-compatible YAML subset."""

    source = Path(path).expanduser().resolve()
    try:
        payload = json.loads(source.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(
            "Pro-first config must use the tracked JSON-compatible YAML format"
        ) from error
    if not isinstance(payload, Mapping):
        raise ValueError("Pro-first config root must be an object")
    _require_exact_keys(
        payload,
        {"runtime", "dashboard", "scheduler", "browser", "scan", "supplement", "authority"},
        "config",
    )
    runtime = _mapping(payload, "runtime")
    dashboard = _mapping(payload, "dashboard")
    scheduler = _mapping(payload, "scheduler")
    morning = _mapping(scheduler, "morning")
    evening = _mapping(scheduler, "evening")
    browser = _mapping(payload, "browser")
    scan = _mapping(payload, "scan")
    supplement = _mapping(payload, "supplement")
    authority = _mapping(payload, "authority")
    _require_exact_keys(runtime, {"root", "reconciliation_poll_seconds"}, "runtime")
    _require_exact_keys(dashboard, {"host", "port"}, "dashboard")
    _require_exact_keys(
        scheduler,
        {"timezone", "morning", "evening", "maximum_idle_poll_seconds"},
        "scheduler",
    )
    _require_exact_keys(morning, {"enabled", "at"}, "scheduler.morning")
    _require_exact_keys(evening, {"enabled", "at"}, "scheduler.evening")
    _require_exact_keys(
        browser,
        {
            "mode",
            "cdp_url",
            "cdp_active_port_file",
            "chatgpt_url",
            "require_manual_login",
            "require_user_start_approval",
            "auto_capture_after_completion",
            "hidden_api_access",
            "poll_interval_seconds",
            "required_stable_observations",
        },
        "browser",
    )
    _require_exact_keys(
        scan,
        {"production_deep_only", "universe_limit", "top_n", "deep_research_min_score"},
        "scan",
    )
    _require_exact_keys(
        supplement,
        {
            "core_score_blocker",
            "stage_boundary_gap",
            "hard_break_gap",
            "corroboration_cap",
            "monitoring_gap",
            "full_research_restart",
        },
        "supplement",
    )
    _require_exact_keys(
        authority,
        {
            "pro_score_authority",
            "pro_stage_authority",
            "deterministic_score_required",
            "deterministic_stagecourt_required",
        },
        "authority",
    )
    return ProFirstLocalConfig(
        runtime_root=Path(str(runtime["root"])),
        reconciliation_poll_seconds=float(runtime["reconciliation_poll_seconds"]),
        dashboard=ProDashboardRuntimeConfig(
            host=str(dashboard["host"]), port=int(dashboard["port"])
        ),
        scheduler=ProScheduleRuntimeConfig(
            timezone=str(scheduler["timezone"]),
            morning_enabled=_strict_bool(morning["enabled"], "scheduler.morning.enabled"),
            morning_at=str(morning["at"]),
            evening_enabled=_strict_bool(evening["enabled"], "scheduler.evening.enabled"),
            evening_at=str(evening["at"]),
            maximum_idle_poll_seconds=float(scheduler["maximum_idle_poll_seconds"]),
        ),
        browser=ProBrowserConfig(
            mode=BrowserConnectionMode(str(browser["mode"])),
            cdp_url=str(browser["cdp_url"]),
            cdp_active_port_file=(
                _optional_path(
                    browser["cdp_active_port_file"],
                    "browser.cdp_active_port_file",
                )
            ),
            chatgpt_url=str(browser["chatgpt_url"]),
            require_manual_login=_strict_bool(browser["require_manual_login"], "browser.require_manual_login"),
            require_user_start_approval=_strict_bool(browser["require_user_start_approval"], "browser.require_user_start_approval"),
            auto_capture_after_completion=_strict_bool(browser["auto_capture_after_completion"], "browser.auto_capture_after_completion"),
            hidden_api_access=_strict_bool(browser["hidden_api_access"], "browser.hidden_api_access"),
            poll_interval_seconds=float(browser["poll_interval_seconds"]),
            required_stable_observations=int(browser["required_stable_observations"]),
        ),
        scan=ProScanRuntimeConfig(
            production_deep_only=_strict_bool(scan["production_deep_only"], "scan.production_deep_only"),
            universe_limit=_optional_int(scan["universe_limit"], "scan.universe_limit"),
            top_n=_optional_int(scan["top_n"], "scan.top_n"),
            deep_research_min_score=float(scan["deep_research_min_score"]),
        ),
        supplement=ProSupplementRuntimeConfig(
            **{
                key: _strict_bool(supplement[key], f"supplement.{key}")
                for key in supplement
            }
        ),
        authority=ProAuthorityRuntimeConfig(
            **{
                key: _strict_bool(authority[key], f"authority.{key}")
                for key in authority
            }
        ),
    )


def _mapping(parent: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = parent.get(key)
    if not isinstance(value, Mapping):
        raise ValueError(f"{key} must be an object")
    return value


def _require_exact_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        raise ValueError(
            f"{label} keys differ: missing={sorted(expected - actual)}, "
            f"unknown={sorted(actual - expected)}"
        )


def _strict_bool(value: Any, label: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{label} must be boolean")
    return value


def _optional_int(value: Any, label: str) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{label} must be an integer or null")
    return value


def _optional_path(value: Any, label: str) -> Path | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty path string or null")
    return Path(value)


__all__ = [
    "BrowserConnectionMode",
    "ProAuthorityRuntimeConfig",
    "ProBrowserConfig",
    "ProDashboardRuntimeConfig",
    "ProFirstLocalConfig",
    "ProScanRuntimeConfig",
    "ProScheduleRuntimeConfig",
    "ProSupplementRuntimeConfig",
    "load_pro_first_local_config",
]
