"""Strict runtime configuration for the Pro-first local platform."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from urllib.parse import urlparse


class BrowserConnectionMode(str, Enum):
    CDP_ATTACH = "CDP_ATTACH"
    PERSISTENT_PROFILE = "PERSISTENT_PROFILE"


@dataclass(frozen=True)
class ProBrowserConfig:
    mode: BrowserConnectionMode = BrowserConnectionMode.CDP_ATTACH
    cdp_url: str = "http://127.0.0.1:9222"
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


__all__ = ["BrowserConnectionMode", "ProBrowserConfig"]
