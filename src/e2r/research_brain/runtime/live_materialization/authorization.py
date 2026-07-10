"""Fail-closed authorization routing for manifest replay and bounded live runs."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path


class LiveRunMode(str, Enum):
    MANIFEST_REPLAY = "MANIFEST_REPLAY"
    LIVE_BOOTSTRAP = "LIVE_BOOTSTRAP"
    LIVE_DAILY_INCREMENTAL = "LIVE_DAILY_INCREMENTAL"
    LIVE_CENSUS_BASELINE = "LIVE_CENSUS_BASELINE"
    LIVE_CENSUS_SELECTIVE_DEEP = "LIVE_CENSUS_SELECTIVE_DEEP"
    TARGETED_LIVE_SMOKE = "TARGETED_LIVE_SMOKE"
    TEST_FIXTURE = "TEST_FIXTURE"


class AuthorizationPath(str, Enum):
    MANIFEST_REPLAY = "MANIFEST_REPLAY"
    LIVE_MATERIALIZATION = "LIVE_MATERIALIZATION"
    FAIL_CLOSED = "FAIL_CLOSED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class LiveAuthorizationDecision:
    path: str
    run_mode: str
    input_manifest: str | None
    run_profile: str | None
    materialize_live_input: bool
    live_materialization_authorized: bool
    blocker_codes: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        AuthorizationPath(self.path)
        LiveRunMode(self.run_mode)
        if self.path == AuthorizationPath.REJECTED.value and not self.blocker_codes:
            raise ValueError("rejected live authorization requires exact blockers")
        if self.path != AuthorizationPath.REJECTED.value and self.blocker_codes:
            raise ValueError("only rejected authorization may carry blockers")
        if self.path == AuthorizationPath.MANIFEST_REPLAY.value:
            if not self.input_manifest or self.materialize_live_input:
                raise ValueError("manifest replay requires only an input manifest")
        if self.path == AuthorizationPath.LIVE_MATERIALIZATION.value:
            if not (
                self.materialize_live_input
                and self.live_materialization_authorized
                and self.run_profile
            ):
                raise ValueError("live materialization requires authorization and run profile")

    @property
    def execution_allowed(self) -> bool:
        return self.path in {
            AuthorizationPath.MANIFEST_REPLAY.value,
            AuthorizationPath.LIVE_MATERIALIZATION.value,
        }

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def resolve_live_authorization(
    *,
    input_manifest: str | Path | None,
    materialize_live_input: bool,
    live_materialization_authorized: bool,
    run_profile: str | Path | None,
    requested_live_mode: str,
) -> LiveAuthorizationDecision:
    """Resolve one CLI request without performing I/O or weakening fail-closed behavior."""

    live_mode = LiveRunMode(requested_live_mode)
    manifest = str(input_manifest) if input_manifest else None
    profile = str(run_profile) if run_profile else None
    blockers: list[str] = []
    if manifest and materialize_live_input:
        blockers.append("INPUT_MANIFEST_AND_LIVE_MATERIALIZATION_CONFLICT")
    if materialize_live_input and not live_materialization_authorized:
        blockers.append("LIVE_MATERIALIZATION_NOT_AUTHORIZED")
    if live_materialization_authorized and not materialize_live_input:
        blockers.append("LIVE_AUTHORIZATION_WITHOUT_MATERIALIZATION_REQUEST")
    if materialize_live_input and not profile:
        blockers.append("LIVE_RUN_PROFILE_REQUIRED")
    if live_mode == LiveRunMode.TEST_FIXTURE and live_materialization_authorized:
        blockers.append("TEST_FIXTURE_CANNOT_RECEIVE_LIVE_AUTHORIZATION")
    if blockers:
        return LiveAuthorizationDecision(
            path=AuthorizationPath.REJECTED.value,
            run_mode=live_mode.value,
            input_manifest=manifest,
            run_profile=profile,
            materialize_live_input=materialize_live_input,
            live_materialization_authorized=live_materialization_authorized,
            blocker_codes=tuple(dict.fromkeys(blockers)),
        )
    if manifest:
        return LiveAuthorizationDecision(
            path=AuthorizationPath.MANIFEST_REPLAY.value,
            run_mode=LiveRunMode.MANIFEST_REPLAY.value,
            input_manifest=manifest,
            run_profile=None,
            materialize_live_input=False,
            live_materialization_authorized=False,
        )
    if materialize_live_input:
        return LiveAuthorizationDecision(
            path=AuthorizationPath.LIVE_MATERIALIZATION.value,
            run_mode=live_mode.value,
            input_manifest=None,
            run_profile=profile,
            materialize_live_input=True,
            live_materialization_authorized=True,
        )
    return LiveAuthorizationDecision(
        path=AuthorizationPath.FAIL_CLOSED.value,
        run_mode=live_mode.value,
        input_manifest=None,
        run_profile=None,
        materialize_live_input=False,
        live_materialization_authorized=False,
    )


__all__ = [
    "AuthorizationPath",
    "LiveAuthorizationDecision",
    "LiveRunMode",
    "resolve_live_authorization",
]
