"""Schemas shared by bounded live materializers and operational envelopes."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from .authorization import LiveRunMode


LIVE_RUN_PROFILE_SCHEMA_VERSION = "e2r_live_run_profile_v1"
LIVE_OPERATIONAL_ENVELOPE_SCHEMA_VERSION = "e2r_live_operational_run_envelope_v1"
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_REQUIRED_BUDGETS = (
    "max_official_light_targets",
    "max_deep_candidates",
    "max_brain_candidates",
    "max_acquisition_candidates",
    "max_llm_calls_per_candidate",
    "max_source_tasks_per_candidate",
    "max_fetches_per_candidate",
    "max_retries_per_candidate",
    "max_general_web_fetches_per_candidate",
    "max_runtime_seconds",
)


@dataclass(frozen=True)
class LiveRunProfile:
    profile_id: str
    run_mode: str
    live_authorization_required: bool
    allowed_providers: tuple[str, ...]
    universe_policy: Mapping[str, Any]
    baseline_policy: Mapping[str, Any]
    budgets: Mapping[str, int]
    checkpoint_resume: bool
    final_label_ceiling: str
    official_first: bool = True
    general_web_requires_official_gap: bool = True
    schema_version: str = LIVE_RUN_PROFILE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != LIVE_RUN_PROFILE_SCHEMA_VERSION:
            raise ValueError("live run profile schema version mismatch")
        mode = LiveRunMode(self.run_mode)
        if not self.profile_id.strip() or not self.allowed_providers:
            raise ValueError("live run profile identity and providers are required")
        if len(set(self.allowed_providers)) != len(self.allowed_providers):
            raise ValueError("live run profile providers must be unique")
        if mode not in {LiveRunMode.MANIFEST_REPLAY, LiveRunMode.TEST_FIXTURE}:
            if not self.live_authorization_required:
                raise ValueError("live run profile must require explicit authorization")
            if not self.official_first or not self.general_web_requires_official_gap:
                raise ValueError("production live profile must remain official-first")
        missing = [key for key in _REQUIRED_BUDGETS if key not in self.budgets]
        if missing:
            raise ValueError(f"live run profile budgets missing: {missing}")
        for key in _REQUIRED_BUDGETS:
            value = self.budgets[key]
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"live run profile budget must be bounded and positive: {key}")
        if not self.universe_policy or not self.baseline_policy:
            raise ValueError("live run profile universe and baseline policy required")
        if not self.final_label_ceiling.strip():
            raise ValueError("live run profile final label ceiling required")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class LiveOperationalRunEnvelope:
    materialization_run_id: str
    evaluator_run_id: str
    as_of_date: str
    run_mode: str
    source_corpus_hash: str
    input_manifest_hash: str
    evaluator_leaf_hash: str
    actual_live_source_count: int
    fresh_provider_cache_count: int
    accepted_current_claim_count: int
    current_atomic_decision_count: int
    provider_blockers: tuple[str, ...]
    critical_counts: Mapping[str, int]
    production_runtime_ready: bool
    schema_version: str = LIVE_OPERATIONAL_ENVELOPE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != LIVE_OPERATIONAL_ENVELOPE_SCHEMA_VERSION:
            raise ValueError("live operational envelope schema version mismatch")
        LiveRunMode(self.run_mode)
        if not all(
            value.strip()
            for value in (
                self.materialization_run_id,
                self.evaluator_run_id,
                self.as_of_date,
            )
        ):
            raise ValueError("live operational envelope identity required")
        for digest in (
            self.source_corpus_hash,
            self.input_manifest_hash,
            self.evaluator_leaf_hash,
        ):
            if not _SHA256_RE.fullmatch(digest):
                raise ValueError("live operational envelope hashes must be SHA-256")
        counts = (
            self.actual_live_source_count,
            self.fresh_provider_cache_count,
            self.accepted_current_claim_count,
            self.current_atomic_decision_count,
        )
        if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in counts):
            raise ValueError("live operational envelope counts must be non-negative integers")
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in self.critical_counts.values()
        ):
            raise ValueError("live operational envelope critical counts invalid")
        if self.production_runtime_ready and (
            self.run_mode == LiveRunMode.TEST_FIXTURE.value
            or self.provider_blockers
            or sum(self.critical_counts.values())
            or self.actual_live_source_count <= 0
            or self.accepted_current_claim_count <= 0
            or self.current_atomic_decision_count <= 0
        ):
            raise ValueError("live operational readiness overclaim")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_live_run_profile(path: str | Path) -> LiveRunProfile:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("live run profile must be an object")
    return LiveRunProfile(
        profile_id=str(payload.get("profile_id") or ""),
        run_mode=str(payload.get("run_mode") or ""),
        live_authorization_required=payload.get("live_authorization_required") is True,
        allowed_providers=tuple(payload.get("allowed_providers") or ()),
        universe_policy=dict(payload.get("universe_policy") or {}),
        baseline_policy=dict(payload.get("baseline_policy") or {}),
        budgets=dict(payload.get("budgets") or {}),
        checkpoint_resume=payload.get("checkpoint_resume") is True,
        final_label_ceiling=str(payload.get("final_label_ceiling") or ""),
        official_first=payload.get("official_first") is True,
        general_web_requires_official_gap=(
            payload.get("general_web_requires_official_gap") is True
        ),
        schema_version=str(payload.get("schema_version") or ""),
    )


__all__ = [
    "LIVE_OPERATIONAL_ENVELOPE_SCHEMA_VERSION",
    "LIVE_RUN_PROFILE_SCHEMA_VERSION",
    "LiveOperationalRunEnvelope",
    "LiveRunProfile",
    "load_live_run_profile",
]
