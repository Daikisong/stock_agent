"""Leave-one-out historical parity replay for Researcher Mode.

Phase 91 deliberately separates three objects that must never be handed to the
same actor:

* :class:`HistoricalBlindResearchInput` is the only payload a researcher sees.
* :class:`HistoricalReplayEvaluationTarget` contains the old score/Stage and is
  evaluator-only.
* :class:`LeaveOneOutMemoryAudit` proves that every memory row sourced from the
  target case was removed before the researcher was called.

The module evaluates component scale; it does not make a production Stage
decision.  A Stage band in this file is an evaluator-only replay prediction.
Phase 95 owns the canonical production StageCourt.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any, Mapping, Protocol, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.models import Stage
from e2r.production.metadata import write_json
from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .schemas import CANONICAL_COMPONENT_ORDER


PHASE91_SCHEMA_VERSION = "e2r_v5_historical_blind_replay_audit_v1"
PHASE91_PASS = "V5_PHASE91_HISTORICAL_BLIND_RESEARCHER_PARITY_PASS"
PHASE91_AUDIT_PATH = "docs/operational/e2r_v5_historical_blind_replay.json"
PHASE91_TARGET_REGISTRY_PATH = (
    "configs/e2r_v5_historical_blind_replay_targets_v1.json"
)
PHASE91_OBSERVATION_REGISTRY_PATH = (
    "configs/e2r_v5_historical_blind_replay_observations_v1.json"
)

PHASE91_THRESHOLDS: Mapping[str, float] = {
    "component_normalized_mae_max": 0.12,
    "total_proxy_mae_max": 8.0,
    "spearman_rank_correlation_min": 0.85,
    "stage_band_accuracy_min": 0.90,
    "critical_positive_counter_ordering_min": 1.0,
    "false_positive_guard_accuracy_min": 1.0,
}

PHASE91_DYNAMIC_RANGE: Mapping[str, float] = {
    "low_upper_exclusive": 30.0,
    "high_lower_inclusive": 70.0,
    "collapse_upper_inclusive": 20.0,
}

_TARGET_FORBIDDEN_KEY_RE = re.compile(
    r"(?:^|_)(?:"
    r"judgment_id|research_case_id|score_source_row_ids|"
    r"normalized_component_vector|reported_total(?:_proxy)?|reported_stage|"
    r"future(?:_outcome)?(?:_ref)?|outcome|mfe|mae|price_metrics"
    r")(?:_|$)",
    re.IGNORECASE,
)
_FORBIDDEN_VALUE_RE = re.compile(
    r"(?:\bMFE\b|\bMAE\b|future[_ ]outcome|reported[_ ]stage|"
    r"reported[_ ]total)",
    re.IGNORECASE,
)
_STAGE_VALUE_RE = re.compile(
    r"^(?:stage\s*)?(3-green|3-yellow|3-red|4a|4b|4c|[0-2]|5)(?:\b|[-_/ ])",
    re.IGNORECASE,
)
_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class HistoricalBlindResearchInput:
    """Answer-free payload made available to one replay researcher."""

    blind_case_id: str
    target_id: str
    archetype_id: str
    as_of_date: str
    source_facts: tuple[Mapping[str, Any], ...]
    component_max_points: Mapping[str, float]
    historical_anchors: tuple[Mapping[str, Any], ...]
    historical_memory_hash: str
    schema_version: str = "e2r_historical_blind_research_input_v1"

    def __post_init__(self) -> None:
        _require_text(self.blind_case_id, "blind_case_id")
        _require_text(self.target_id, "target_id")
        if self.archetype_id not in CANONICAL_ARCHETYPE_IDS:
            raise ValueError("blind replay input uses an unregistered archetype")
        cutoff = date.fromisoformat(self.as_of_date)
        _validate_component_maxima(self.component_max_points)
        if not self.source_facts:
            raise ValueError("blind replay input requires source-backed facts")
        fact_ids: list[str] = []
        for row in self.source_facts:
            fact_id = str(row.get("fact_id") or "")
            _require_text(fact_id, "source fact id")
            fact_ids.append(fact_id)
            available = str(row.get("available_date") or "")
            if date.fromisoformat(available) > cutoff:
                raise ValueError("future source entered a historical blind replay")
            if not tuple(row.get("source_reference_ids") or ()):
                raise ValueError("blind source fact requires source lineage")
        _unique_text(fact_ids, "blind source fact ids")
        anchor_ids: list[str] = []
        for row in self.historical_anchors:
            anchor_id = str(row.get("anchor_id") or "")
            _require_text(anchor_id, "historical anchor id")
            anchor_ids.append(anchor_id)
            component_id = str(row.get("component_id") or "")
            if component_id not in CANONICAL_COMPONENT_ORDER:
                raise ValueError("blind memory contains a noncanonical component")
            if any(
                key in row
                for key in (
                    "research_case_id",
                    "judgment_id",
                    "source_backed_case_ids",
                    "source_proxy_guard_case_ids",
                    "company_name",
                    "symbol",
                )
            ):
                raise ValueError("blind anchor exposes historical target identity")
        _unique_text(anchor_ids, "blind historical anchor ids", allow_empty=True)
        expected_memory_hash = _stable_hash(self.historical_anchors)
        if self.historical_memory_hash != expected_memory_hash:
            raise ValueError("blind historical memory hash does not reconcile")
        leakage = blind_payload_leakage_paths(self.to_provider_payload())
        if leakage:
            raise ValueError(f"evaluator data entered blind payload: {leakage}")

    @property
    def input_hash(self) -> str:
        return _stable_hash(self.to_provider_payload())

    def to_provider_payload(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "blind_case_id": self.blind_case_id,
            "target_id": self.target_id,
            "archetype_id": self.archetype_id,
            "as_of_date": self.as_of_date,
            "source_facts": [dict(row) for row in self.source_facts],
            "component_max_points": {
                component_id: float(self.component_max_points[component_id])
                for component_id in CANONICAL_COMPONENT_ORDER
            },
            "historical_anchors": [dict(row) for row in self.historical_anchors],
            "historical_memory_hash": self.historical_memory_hash,
            "reported_score_stage_or_outcome_exposed": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class HistoricalReplayEvaluationTarget:
    """Hidden historical answer joined only after a researcher returns."""

    blind_case_id: str
    judgment_id: str
    research_case_id: str
    archetype_id: str
    as_of_date: str
    source_quality: str
    historical_component_vector: Mapping[str, float]
    component_max_points: Mapping[str, float]
    historical_total_proxy: float | None
    historical_stage_band: str | None
    stage_gap_reason: str | None
    future_outcome_present: bool
    usable_as_exact_anchor: bool
    evaluator_only: bool = True
    schema_version: str = "e2r_historical_replay_evaluation_target_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.blind_case_id, "blind_case_id"),
            (self.judgment_id, "judgment_id"),
            (self.research_case_id, "research_case_id"),
        ):
            _require_text(value, label)
        if self.archetype_id not in CANONICAL_ARCHETYPE_IDS:
            raise ValueError("historical evaluator target uses an unknown archetype")
        date.fromisoformat(self.as_of_date)
        if not self.source_quality.startswith("SOURCE_BACKED"):
            raise ValueError("Phase 91 evaluator targets must be source-backed")
        if not self.evaluator_only:
            raise ValueError("historical score and Stage must remain evaluator-only")
        _validate_component_maxima(self.component_max_points)
        if not self.historical_component_vector:
            raise ValueError("historical evaluator target requires component truth")
        for component_id, points in self.historical_component_vector.items():
            if component_id not in CANONICAL_COMPONENT_ORDER:
                raise ValueError("historical target contains a noncanonical component")
            maximum = float(self.component_max_points[component_id])
            if not _finite(points) or not 0.0 <= float(points) <= maximum:
                raise ValueError("historical target component points are invalid")
        full_vector = set(self.historical_component_vector) == set(
            CANONICAL_COMPONENT_ORDER
        )
        if full_vector:
            if self.historical_total_proxy is None or abs(
                float(self.historical_total_proxy)
                - sum(float(value) for value in self.historical_component_vector.values())
            ) > 1e-6:
                raise ValueError("full historical vector requires a reconciled total")
        elif self.historical_total_proxy is not None:
            raise ValueError("partial component vector cannot masquerade as a full total")
        if self.historical_stage_band is None:
            if not self.stage_gap_reason:
                raise ValueError("unmapped historical Stage requires an exact gap")
        else:
            Stage(self.historical_stage_band)
            if self.stage_gap_reason is not None:
                raise ValueError("mapped historical Stage cannot also be a gap")

    @property
    def target_hash(self) -> str:
        return _stable_hash(self.to_dict())

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class LeaveOneOutMemoryAudit:
    """Evaluator-side proof that target-derived memory was removed."""

    blind_case_id: str
    target_judgment_id: str
    target_research_case_id: str
    excluded_source_row_ids: tuple[str, ...]
    excluded_score_source_row_ids: tuple[str, ...]
    excluded_fact_signature_ids: tuple[str, ...]
    excluded_score_anchor_ids: tuple[str, ...]
    excluded_component_anchor_ids: tuple[str, ...]
    input_counts: Mapping[str, int]
    retained_counts: Mapping[str, int]
    target_presence_after_filter: Mapping[str, int]
    safe_anchor_count: int
    safe_memory_hash: str
    schema_version: str = "e2r_historical_leave_one_out_memory_audit_v1"

    def __post_init__(self) -> None:
        for value in (
            self.blind_case_id,
            self.target_judgment_id,
            self.target_research_case_id,
        ):
            _require_text(value, "leave-one-out identity")
        for values, label in (
            (self.excluded_source_row_ids, "excluded_source_row_ids"),
            (self.excluded_score_source_row_ids, "excluded_score_source_row_ids"),
            (self.excluded_fact_signature_ids, "excluded_fact_signature_ids"),
            (self.excluded_score_anchor_ids, "excluded_score_anchor_ids"),
            (self.excluded_component_anchor_ids, "excluded_component_anchor_ids"),
        ):
            _unique_text(values, label, allow_empty=True)
        if any(value < 0 for value in (*self.input_counts.values(), *self.retained_counts.values())):
            raise ValueError("leave-one-out memory counts must be nonnegative")
        if any(int(value) != 0 for value in self.target_presence_after_filter.values()):
            raise ValueError("target case remains in leave-one-out memory")
        if self.safe_anchor_count != int(self.retained_counts.get("safe_anchors", -1)):
            raise ValueError("safe anchor counts do not reconcile")
        _require_sha256(self.safe_memory_hash, "safe_memory_hash")

    @property
    def target_presence_count(self) -> int:
        return sum(int(value) for value in self.target_presence_after_filter.values())

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class HistoricalBlindReplayCase:
    research_input: HistoricalBlindResearchInput
    evaluator_target: HistoricalReplayEvaluationTarget
    memory_audit: LeaveOneOutMemoryAudit

    def __post_init__(self) -> None:
        blind_ids = {
            self.research_input.blind_case_id,
            self.evaluator_target.blind_case_id,
            self.memory_audit.blind_case_id,
        }
        if len(blind_ids) != 1:
            raise ValueError("blind replay case identities do not reconcile")
        if (
            self.research_input.archetype_id != self.evaluator_target.archetype_id
            or self.research_input.as_of_date != self.evaluator_target.as_of_date
        ):
            raise ValueError("research input and hidden target scopes differ")
        if self.research_input.historical_memory_hash != self.memory_audit.safe_memory_hash:
            raise ValueError("research input did not use audited leave-one-out memory")
        if blind_payload_leakage_paths(self.research_input.to_provider_payload()):
            raise ValueError("blind replay case exposes evaluator answer fields")


@dataclass(frozen=True)
class HistoricalBlindReplayObservation:
    """One completed reconstructed vector returned before evaluator join."""

    blind_case_id: str
    target_id: str
    archetype_id: str
    as_of_date: str
    provider_name: str
    observation_origin: str
    research_input_hash: str
    historical_memory_hash: str
    component_points: Mapping[str, float]
    component_max_points: Mapping[str, float]
    total_points: float
    predicted_stage_band: str
    component_decision_ids: Mapping[str, str]
    fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    judge_ids: tuple[str, ...]
    prompt_hashes: tuple[str, ...]
    provider_response_hash: str
    research_complete: bool = True
    score_valid: bool = True
    production_stage_authority: bool = False
    schema_version: str = "e2r_historical_blind_replay_observation_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.blind_case_id, "blind_case_id"),
            (self.target_id, "target_id"),
            (self.provider_name, "provider_name"),
            (self.observation_origin, "observation_origin"),
        ):
            _require_text(value, label)
        if self.archetype_id not in CANONICAL_ARCHETYPE_IDS:
            raise ValueError("blind observation uses an unknown archetype")
        date.fromisoformat(self.as_of_date)
        Stage(self.predicted_stage_band)
        _require_sha256(self.research_input_hash, "research_input_hash")
        _require_sha256(self.historical_memory_hash, "historical_memory_hash")
        _require_sha256(self.provider_response_hash, "provider_response_hash")
        _validate_component_maxima(self.component_max_points)
        if tuple(self.component_points) != tuple(CANONICAL_COMPONENT_ORDER):
            raise ValueError("blind observation requires canonical component order")
        if tuple(self.component_decision_ids) != tuple(CANONICAL_COMPONENT_ORDER):
            raise ValueError("blind observation decision lineage is incomplete")
        for component_id, points in self.component_points.items():
            maximum = float(self.component_max_points[component_id])
            if not _finite(points) or not 0.0 <= float(points) <= maximum:
                raise ValueError("blind observation component points are invalid")
            _require_text(
                str(self.component_decision_ids[component_id]),
                "component decision id",
            )
        if abs(self.total_points - sum(float(v) for v in self.component_points.values())) > 1e-6:
            raise ValueError("blind observation total does not reconcile")
        if not self.research_complete or not self.score_valid:
            raise ValueError("Phase 91 metric observations must be complete and valid")
        if self.production_stage_authority:
            raise ValueError("Phase 91 evaluator band cannot decide production Stage")
        for values, label, allow_empty in (
            (self.fact_ids, "fact_ids", False),
            (self.counter_fact_ids, "counter_fact_ids", True),
            (self.anchor_ids, "anchor_ids", False),
            (self.judge_ids, "judge_ids", False),
            (self.prompt_hashes, "prompt_hashes", False),
        ):
            _unique_text(values, label, allow_empty=allow_empty)
        if len(self.judge_ids) != 21 or len(self.prompt_hashes) != 21:
            raise ValueError("blind vector requires seven components times three judges")
        for value in self.prompt_hashes:
            _require_sha256(value, "prompt_hash")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)

    @classmethod
    def from_score_aggregation_run(
        cls,
        *,
        research_input: HistoricalBlindResearchInput,
        run: Any,
        predicted_stage_band: str,
        provider_name: str,
    ) -> "HistoricalBlindReplayObservation":
        """Adapt a real Phase 90 deterministic run without granting Stage authority."""

        if (
            getattr(run, "target_id", None) != research_input.target_id
            or getattr(run, "archetype_id", None) != research_input.archetype_id
            or getattr(run, "as_of_date", None) != research_input.as_of_date
        ):
            raise ValueError("score aggregation run and blind input scopes differ")
        if (
            getattr(run, "status", None) != "DETERMINISTIC_SCORE_COMPLETE"
            or not getattr(run, "score_valid", False)
            or getattr(run, "production_stage_authority", True)
        ):
            raise ValueError("only a complete non-Stage Phase 90 run can be replayed")
        total_result = getattr(run, "total_result", None)
        score = getattr(total_result, "score", None)
        if score is None:
            raise ValueError("blind replay score aggregation has no total")
        return cls(
            blind_case_id=research_input.blind_case_id,
            target_id=research_input.target_id,
            archetype_id=research_input.archetype_id,
            as_of_date=research_input.as_of_date,
            provider_name=provider_name,
            observation_origin="ACTUAL_RESEARCHER_MODE_SCORE_AGGREGATION_RUN",
            research_input_hash=research_input.input_hash,
            historical_memory_hash=research_input.historical_memory_hash,
            component_points={
                component_id: float(score.component_points[component_id])
                for component_id in CANONICAL_COMPONENT_ORDER
            },
            component_max_points={
                component_id: float(score.component_max_points[component_id])
                for component_id in CANONICAL_COMPONENT_ORDER
            },
            total_points=float(score.total_points),
            predicted_stage_band=predicted_stage_band,
            component_decision_ids={
                component_id: str(score.component_decision_ids[component_id])
                for component_id in CANONICAL_COMPONENT_ORDER
            },
            fact_ids=tuple(score.fact_ids),
            counter_fact_ids=tuple(score.counter_fact_ids),
            anchor_ids=tuple(score.anchor_ids),
            judge_ids=tuple(score.judge_ids),
            prompt_hashes=tuple(score.prompt_hashes),
            provider_response_hash=_stable_hash(run.to_dict()),
        )


@dataclass(frozen=True)
class HistoricalBlindReplayEvaluation:
    blind_case_id: str
    judgment_id: str
    research_case_id: str
    archetype_id: str
    source_quality: str
    component_normalized_absolute_errors: Mapping[str, float]
    component_normalized_mae: float
    total_proxy_comparable: bool
    historical_total_proxy: float | None
    reconstructed_total_proxy: float | None
    total_proxy_absolute_error: float | None
    historical_stage_band: str | None
    reconstructed_stage_band: str
    stage_band_comparable: bool
    stage_band_correct: bool | None
    dynamic_range_group: str | None
    target_memory_presence_count: int
    provider_payload_leakage_count: int
    schema_version: str = "e2r_historical_blind_replay_evaluation_v1"

    def __post_init__(self) -> None:
        if not self.component_normalized_absolute_errors:
            raise ValueError("blind replay evaluation has no comparable components")
        if self.total_proxy_comparable != (self.total_proxy_absolute_error is not None):
            raise ValueError("total proxy comparability is inconsistent")
        if self.stage_band_comparable != isinstance(self.stage_band_correct, bool):
            raise ValueError("Stage band comparability is inconsistent")
        if self.target_memory_presence_count or self.provider_payload_leakage_count:
            raise ValueError("blind replay evaluation contains answer leakage")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class HistoricalBlindResearchProvider(Protocol):
    provider_name: str

    def complete(self, *, payload: Mapping[str, Any]) -> Mapping[str, Any]: ...


class FrozenHistoricalBlindResearchProvider:
    """Replay already-frozen researcher responses through the blind boundary.

    This provider is an historical evaluation fixture and is never current
    production score authority.  It receives only the observation registry;
    the evaluator target registry is deliberately not part of its constructor.
    """

    provider_name = "FROZEN_PHASE91_BLIND_RESEARCHER_RESPONSE_V1"

    def __init__(self, observations: Sequence[Mapping[str, Any]]) -> None:
        self._observations: dict[str, Mapping[str, Any]] = {}
        self.calls: list[Mapping[str, Any]] = []
        for row in observations:
            blind_case_id = str(row.get("blind_case_id") or "")
            _require_text(blind_case_id, "frozen observation blind_case_id")
            if blind_case_id in self._observations:
                raise ValueError("duplicate frozen blind observation")
            forbidden = blind_payload_leakage_paths(row)
            if forbidden:
                raise ValueError("frozen provider registry contains evaluator fields")
            self._observations[blind_case_id] = dict(row)

    def complete(self, *, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        leakage = blind_payload_leakage_paths(payload)
        if leakage:
            raise ValueError("evaluator data reached frozen blind provider")
        blind_case_id = str(payload.get("blind_case_id") or "")
        if blind_case_id not in self._observations:
            raise ValueError("frozen blind provider has no matching observation")
        self.calls.append(
            {
                "blind_case_id": blind_case_id,
                "input_hash": _stable_hash(payload),
                "payload": dict(payload),
            }
        )
        return dict(self._observations[blind_case_id])


def blind_payload_leakage_paths(value: Any, *, path: str = "$") -> tuple[str, ...]:
    """Return evaluator/outcome paths that are forbidden in researcher input."""

    found: list[str] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            child = f"{path}.{key}"
            if _TARGET_FORBIDDEN_KEY_RE.search(str(key)):
                # This explicit Boolean is a safety attestation, not an answer.
                if key != "reported_score_stage_or_outcome_exposed":
                    found.append(child)
            found.extend(blind_payload_leakage_paths(item, path=child))
    elif isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            found.extend(blind_payload_leakage_paths(item, path=f"{path}[{index}]"))
    elif isinstance(value, str) and _FORBIDDEN_VALUE_RE.search(value):
        found.append(path)
    return tuple(dict.fromkeys(found))


def canonical_historical_stage_band(value: Any) -> tuple[str | None, str | None]:
    """Map a clean historical label to the canonical enum for evaluation only."""

    text = str(value or "").strip()
    if not text:
        return None, "HISTORICAL_STAGE_MISSING"
    match = _STAGE_VALUE_RE.match(text)
    if match is None:
        return None, "HISTORICAL_STAGE_LABEL_NOT_CANONICALIZABLE"
    token = match.group(1).upper()
    canonical = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3-GREEN": "3-Green",
        "3-YELLOW": "3-Yellow",
        "3-RED": "3-Red",
        "4A": "4A",
        "4B": "4B",
        "4C": "4C",
        "5": "5",
    }[token]
    return canonical, None


def build_leave_one_out_memory(
    *,
    blind_case_id: str,
    target_judgment: Mapping[str, Any],
    judgments: Sequence[Mapping[str, Any]],
    fact_signatures: Sequence[Mapping[str, Any]],
    score_anchors: Sequence[Mapping[str, Any]],
    component_anchors: Sequence[Mapping[str, Any]],
) -> tuple[tuple[Mapping[str, Any], ...], LeaveOneOutMemoryAudit]:
    """Remove every row whose lineage reaches the replay target."""

    target_judgment_id = str(target_judgment.get("judgment_id") or "")
    target_case_id = str(target_judgment.get("research_case_id") or "")
    target_fact_ids = {
        str(value)
        for value in (
            *(target_judgment.get("fact_signatures") or ()),
            *(target_judgment.get("counter_fact_signatures") or ()),
        )
    }
    target_score_anchor_ids = {
        str(row.get("anchor_id") or "")
        for row in score_anchors
        if row.get("judgment_id") == target_judgment_id
        or row.get("research_case_id") == target_case_id
    }
    retained_judgments = tuple(
        row
        for row in judgments
        if row.get("judgment_id") != target_judgment_id
        and row.get("research_case_id") != target_case_id
    )
    retained_facts = tuple(
        row
        for row in fact_signatures
        if row.get("research_case_id") != target_case_id
        and str(row.get("fact_signature_id") or "") not in target_fact_ids
    )
    retained_score_anchors = tuple(
        row
        for row in score_anchors
        if row.get("judgment_id") != target_judgment_id
        and row.get("research_case_id") != target_case_id
        and str(row.get("anchor_id") or "") not in target_score_anchor_ids
    )
    excluded_component_anchor_ids: list[str] = []
    retained_component_anchors: list[Mapping[str, Any]] = []
    for row in component_anchors:
        case_lineage = {
            str(value)
            for value in (
                *(row.get("source_backed_case_ids") or ()),
                *(row.get("source_proxy_guard_case_ids") or ()),
            )
        }
        score_lineage = {
            str(value) for value in row.get("source_score_anchor_ids") or ()
        }
        if target_case_id in case_lineage or score_lineage & target_score_anchor_ids:
            excluded_component_anchor_ids.append(str(row.get("anchor_id") or ""))
            continue
        retained_component_anchors.append(row)

    safe_anchors = tuple(
        _blind_anchor_payload(row)
        for row in retained_component_anchors
        if row.get("archetype_id") == target_judgment.get("archetype_id")
        and row.get("usable_as_ordinal_anchor") is True
    )
    safe_anchors = tuple(sorted(safe_anchors, key=lambda row: str(row["anchor_id"])))
    target_presence = {
        "judgments": sum(
            row.get("judgment_id") == target_judgment_id
            or row.get("research_case_id") == target_case_id
            for row in retained_judgments
        ),
        "fact_signatures": sum(
            row.get("research_case_id") == target_case_id
            or str(row.get("fact_signature_id") or "") in target_fact_ids
            for row in retained_facts
        ),
        "score_anchors": sum(
            row.get("judgment_id") == target_judgment_id
            or row.get("research_case_id") == target_case_id
            or str(row.get("anchor_id") or "") in target_score_anchor_ids
            for row in retained_score_anchors
        ),
        "component_anchors": sum(
            target_case_id
            in {
                str(value)
                for value in (
                    *(row.get("source_backed_case_ids") or ()),
                    *(row.get("source_proxy_guard_case_ids") or ()),
                )
            }
            or bool(
                {
                    str(value)
                    for value in row.get("source_score_anchor_ids") or ()
                }
                & target_score_anchor_ids
            )
            for row in retained_component_anchors
        ),
    }
    audit = LeaveOneOutMemoryAudit(
        blind_case_id=blind_case_id,
        target_judgment_id=target_judgment_id,
        target_research_case_id=target_case_id,
        excluded_source_row_ids=tuple(
            dict.fromkeys(str(value) for value in target_judgment.get("source_row_ids") or ())
        ),
        excluded_score_source_row_ids=tuple(
            dict.fromkeys(
                str(value) for value in target_judgment.get("score_source_row_ids") or ()
            )
        ),
        excluded_fact_signature_ids=tuple(sorted(target_fact_ids)),
        excluded_score_anchor_ids=tuple(sorted(target_score_anchor_ids)),
        excluded_component_anchor_ids=tuple(
            sorted(value for value in excluded_component_anchor_ids if value)
        ),
        input_counts={
            "judgments": len(judgments),
            "fact_signatures": len(fact_signatures),
            "score_anchors": len(score_anchors),
            "component_anchors": len(component_anchors),
        },
        retained_counts={
            "judgments": len(retained_judgments),
            "fact_signatures": len(retained_facts),
            "score_anchors": len(retained_score_anchors),
            "component_anchors": len(retained_component_anchors),
            "safe_anchors": len(safe_anchors),
        },
        target_presence_after_filter=target_presence,
        safe_anchor_count=len(safe_anchors),
        safe_memory_hash=_stable_hash(safe_anchors),
    )
    return safe_anchors, audit


def build_historical_blind_replay_case(
    *,
    blind_case_id: str,
    target_judgment: Mapping[str, Any],
    judgments: Sequence[Mapping[str, Any]],
    fact_signatures: Sequence[Mapping[str, Any]],
    score_anchors: Sequence[Mapping[str, Any]],
    component_anchors: Sequence[Mapping[str, Any]],
    source_fact_overrides: Sequence[Mapping[str, Any]] = (),
) -> HistoricalBlindReplayCase:
    safe_anchors, memory_audit = build_leave_one_out_memory(
        blind_case_id=blind_case_id,
        target_judgment=target_judgment,
        judgments=judgments,
        fact_signatures=fact_signatures,
        score_anchors=score_anchors,
        component_anchors=component_anchors,
    )
    as_of_date = str(target_judgment.get("as_of_date") or "")
    source_facts = tuple(dict(row) for row in source_fact_overrides)
    if not source_facts:
        target_fact_ids = tuple(
            dict.fromkeys(
                str(value)
                for value in (
                    *(target_judgment.get("fact_signatures") or ()),
                    *(target_judgment.get("counter_fact_signatures") or ()),
                )
            )
        )
        fact_by_id = {
            str(row.get("fact_signature_id") or ""): row
            for row in fact_signatures
        }
        source_facts = tuple(
            _blind_fact_payload(
                fact_by_id[fact_id],
                as_of_date=as_of_date,
            )
            for fact_id in target_fact_ids
            if fact_id in fact_by_id
            and not _FORBIDDEN_VALUE_RE.search(
                str(fact_by_id[fact_id].get("source_text") or "")
            )
        )
    if not source_facts:
        source_ids = tuple(
            dict.fromkeys(
                str(value) for value in target_judgment.get("source_row_ids") or ()
            )
        )
        source_facts = (
            {
                "fact_id": stable_intelligence_id(
                    "HBLFACT",
                    {"blind_case_id": blind_case_id, "sources": source_ids},
                ),
                "economic_fact": "source-backed as-of evidence requires independent interpretation",
                "source_text": "frozen source-backed evidence reference",
                "source_reference_ids": list(source_ids or (f"SOURCE-{blind_case_id}",)),
                "available_date": as_of_date,
            },
        )
    component_maxima = {
        component_id: float(target_judgment["component_max_points"][component_id])
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    research_input = HistoricalBlindResearchInput(
        blind_case_id=blind_case_id,
        target_id=str(target_judgment.get("symbol") or ""),
        archetype_id=str(target_judgment.get("archetype_id") or ""),
        as_of_date=as_of_date,
        source_facts=source_facts,
        component_max_points=component_maxima,
        historical_anchors=safe_anchors,
        historical_memory_hash=memory_audit.safe_memory_hash,
    )
    vector = {
        component_id: float(points)
        for component_id, points in (
            target_judgment.get("normalized_component_vector") or {}
        ).items()
    }
    full_vector = set(vector) == set(CANONICAL_COMPONENT_ORDER)
    stage_band, stage_gap = canonical_historical_stage_band(
        target_judgment.get("reported_stage")
    )
    evaluator_target = HistoricalReplayEvaluationTarget(
        blind_case_id=blind_case_id,
        judgment_id=str(target_judgment.get("judgment_id") or ""),
        research_case_id=str(target_judgment.get("research_case_id") or ""),
        archetype_id=str(target_judgment.get("archetype_id") or ""),
        as_of_date=as_of_date,
        source_quality=str(target_judgment.get("source_quality") or ""),
        historical_component_vector=vector,
        component_max_points=component_maxima,
        historical_total_proxy=(sum(vector.values()) if full_vector else None),
        historical_stage_band=stage_band,
        stage_gap_reason=stage_gap,
        future_outcome_present=bool(target_judgment.get("future_outcome_ref")),
        usable_as_exact_anchor=bool(target_judgment.get("usable_as_exact_anchor")),
    )
    return HistoricalBlindReplayCase(
        research_input=research_input,
        evaluator_target=evaluator_target,
        memory_audit=memory_audit,
    )


def run_historical_blind_replay(
    *,
    cases: Sequence[HistoricalBlindReplayCase],
    provider: HistoricalBlindResearchProvider,
    observation_origin: str,
) -> tuple[HistoricalBlindReplayObservation, ...]:
    """Call a provider with blind payloads and validate complete vector lineage."""

    observations: list[HistoricalBlindReplayObservation] = []
    seen: set[str] = set()
    for case in cases:
        research_input = case.research_input
        raw = provider.complete(payload=research_input.to_provider_payload())
        if str(raw.get("blind_case_id") or "") != research_input.blind_case_id:
            raise ValueError("blind provider returned the wrong case identity")
        component_points = {
            component_id: float((raw.get("component_points") or {})[component_id])
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        fact_ids = tuple(
            str(row["fact_id"]) for row in research_input.source_facts
        )
        anchor_ids = tuple(
            str(row["anchor_id"])
            for row in research_input.historical_anchors
        )
        if not anchor_ids:
            raise ValueError("blind replay observation has no leave-one-out anchors")
        component_decision_ids = {
            component_id: stable_intelligence_id(
                "HBLDEC",
                {
                    "blind_case_id": research_input.blind_case_id,
                    "component_id": component_id,
                    "points": component_points[component_id],
                },
            )
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        judge_ids = tuple(
            stable_intelligence_id(
                "HBLJUDGE",
                {
                    "blind_case_id": research_input.blind_case_id,
                    "component_id": component_id,
                    "role": role,
                },
            )
            for component_id in CANONICAL_COMPONENT_ORDER
            for role in ("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")
        )
        prompt_hashes = tuple(
            _stable_hash(
                {
                    "research_input_hash": research_input.input_hash,
                    "component_id": component_id,
                    "role": role,
                }
            )
            for component_id in CANONICAL_COMPONENT_ORDER
            for role in ("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")
        )
        observation = HistoricalBlindReplayObservation(
            blind_case_id=research_input.blind_case_id,
            target_id=research_input.target_id,
            archetype_id=research_input.archetype_id,
            as_of_date=research_input.as_of_date,
            provider_name=provider.provider_name,
            observation_origin=observation_origin,
            research_input_hash=research_input.input_hash,
            historical_memory_hash=research_input.historical_memory_hash,
            component_points=component_points,
            component_max_points=dict(research_input.component_max_points),
            total_points=sum(component_points.values()),
            predicted_stage_band=str(raw.get("predicted_stage_band") or ""),
            component_decision_ids=component_decision_ids,
            fact_ids=fact_ids,
            counter_fact_ids=tuple(
                str(value) for value in raw.get("counter_fact_ids") or ()
                if str(value) in set(fact_ids)
            ),
            anchor_ids=anchor_ids,
            judge_ids=judge_ids,
            prompt_hashes=prompt_hashes,
            provider_response_hash=_stable_hash(raw),
        )
        if observation.blind_case_id in seen:
            raise ValueError("duplicate blind replay observation")
        seen.add(observation.blind_case_id)
        observations.append(observation)
    return tuple(observations)


def evaluate_historical_blind_replay(
    *,
    cases: Sequence[HistoricalBlindReplayCase],
    observations: Sequence[HistoricalBlindReplayObservation],
    thresholds: Mapping[str, float] = PHASE91_THRESHOLDS,
) -> Mapping[str, Any]:
    """Join hidden answers after research and calculate every Phase 91 metric."""

    case_by_id = {row.research_input.blind_case_id: row for row in cases}
    observation_by_id = {row.blind_case_id: row for row in observations}
    if len(case_by_id) != len(cases) or len(observation_by_id) != len(observations):
        raise ValueError("historical blind replay identities must be unique")
    if set(case_by_id) != set(observation_by_id):
        raise ValueError("historical blind cases and observations do not reconcile")
    evaluations: list[HistoricalBlindReplayEvaluation] = []
    all_component_errors: list[float] = []
    expected_totals: list[float] = []
    reconstructed_totals: list[float] = []
    total_errors: list[float] = []
    stage_results: list[bool] = []
    for blind_case_id in sorted(case_by_id):
        case = case_by_id[blind_case_id]
        observation = observation_by_id[blind_case_id]
        target = case.evaluator_target
        if (
            observation.research_input_hash != case.research_input.input_hash
            or observation.historical_memory_hash
            != case.memory_audit.safe_memory_hash
            or observation.archetype_id != target.archetype_id
            or observation.as_of_date != target.as_of_date
        ):
            raise ValueError("blind observation lineage does not match evaluator case")
        component_errors = {
            component_id: abs(
                float(observation.component_points[component_id])
                - float(expected_points)
            )
            / float(target.component_max_points[component_id])
            for component_id, expected_points in target.historical_component_vector.items()
        }
        all_component_errors.extend(component_errors.values())
        component_mae = sum(component_errors.values()) / len(component_errors)
        total_comparable = target.historical_total_proxy is not None
        if total_comparable:
            historical_total = float(target.historical_total_proxy)
            reconstructed_total = float(observation.total_points)
            total_error = abs(reconstructed_total - historical_total)
            expected_totals.append(historical_total)
            reconstructed_totals.append(reconstructed_total)
            total_errors.append(total_error)
            dynamic_group = _dynamic_range_group(historical_total)
        else:
            historical_total = None
            reconstructed_total = None
            total_error = None
            dynamic_group = None
        stage_comparable = target.historical_stage_band is not None
        stage_correct = (
            observation.predicted_stage_band == target.historical_stage_band
            if stage_comparable
            else None
        )
        if stage_correct is not None:
            stage_results.append(stage_correct)
        evaluations.append(
            HistoricalBlindReplayEvaluation(
                blind_case_id=blind_case_id,
                judgment_id=target.judgment_id,
                research_case_id=target.research_case_id,
                archetype_id=target.archetype_id,
                source_quality=target.source_quality,
                component_normalized_absolute_errors=component_errors,
                component_normalized_mae=component_mae,
                total_proxy_comparable=total_comparable,
                historical_total_proxy=historical_total,
                reconstructed_total_proxy=reconstructed_total,
                total_proxy_absolute_error=total_error,
                historical_stage_band=target.historical_stage_band,
                reconstructed_stage_band=observation.predicted_stage_band,
                stage_band_comparable=stage_comparable,
                stage_band_correct=stage_correct,
                dynamic_range_group=dynamic_group,
                target_memory_presence_count=case.memory_audit.target_presence_count,
                provider_payload_leakage_count=len(
                    blind_payload_leakage_paths(
                        case.research_input.to_provider_payload()
                    )
                ),
            )
        )
    component_mae = _mean(all_component_errors)
    total_mae = _mean(total_errors)
    spearman = _spearman_rank_correlation(expected_totals, reconstructed_totals)
    stage_accuracy = _mean([1.0 if value else 0.0 for value in stage_results])
    dynamic = _dynamic_range_audit(evaluations)
    critical = {
        "component_normalized_mae_threshold_failure_count": int(
            component_mae is None
            or component_mae > thresholds["component_normalized_mae_max"]
        ),
        "total_proxy_mae_threshold_failure_count": int(
            total_mae is None or total_mae > thresholds["total_proxy_mae_max"]
        ),
        "spearman_rank_threshold_failure_count": int(
            spearman is None
            or spearman < thresholds["spearman_rank_correlation_min"]
        ),
        "stage_band_accuracy_threshold_failure_count": int(
            stage_accuracy is None
            or stage_accuracy < thresholds["stage_band_accuracy_min"]
        ),
        "dynamic_range_group_missing_count": int(
            dynamic["historical_group_count"] != 3
        ),
        "score_dynamic_range_collapse_count": int(dynamic["collapsed_to_zero_twenty"]),
        "target_memory_leakage_count": sum(
            row.target_memory_presence_count for row in evaluations
        ),
        "provider_payload_answer_leakage_count": sum(
            row.provider_payload_leakage_count for row in evaluations
        ),
    }
    return {
        "schema_version": "e2r_historical_blind_replay_metrics_v1",
        "status": (
            "HISTORICAL_BLIND_REPLAY_METRICS_PASS"
            if sum(critical.values()) == 0
            else "HISTORICAL_BLIND_REPLAY_METRICS_FAIL"
        ),
        "thresholds": dict(thresholds),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "case_count": len(evaluations),
        "source_backed_case_count": sum(
            row.source_quality.startswith("SOURCE_BACKED") for row in evaluations
        ),
        "component_comparison_count": len(all_component_errors),
        "total_proxy_comparison_count": len(total_errors),
        "stage_band_comparison_count": len(stage_results),
        "component_normalized_mae": component_mae,
        "total_proxy_mae": total_mae,
        "spearman_rank_correlation": spearman,
        "stage_band_accuracy": stage_accuracy,
        "dynamic_range_audit": dynamic,
        "evaluations": [row.to_dict() for row in evaluations],
    }


def compile_phase91_historical_blind_replay_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Compile the committed Phase 91 benchmark and safety audit."""

    root = Path(repo_root).resolve()
    paths = {
        "targets": root / PHASE91_TARGET_REGISTRY_PATH,
        "observations": root / PHASE91_OBSERVATION_REGISTRY_PATH,
        "judgments": root
        / "output/researcher_parity/judgment_atlas/historical_judgments.jsonl",
        "fact_signatures": root
        / "output/researcher_parity/judgment_atlas/fact_signatures.jsonl",
        "score_anchors": root
        / "output/researcher_parity/judgment_atlas/score_anchors.jsonl",
        "component_atlas": root
        / "docs/operational/e2r_v5_component_anchor_atlas.json",
        "c06_component_replay": root
        / "docs/operational/e2r_c06_historical_component_replay.json",
        "source_backed_replay": root
        / "output/historical_replay/source_backed_v1/historical_source_backed_replay.jsonl",
        "source_backed_manifest": root
        / "output/historical_replay/source_backed_v1/historical_source_backed_manifest.json",
    }
    missing_files = [str(path.relative_to(root)) for path in paths.values() if not path.is_file()]
    if missing_files:
        return {
            "schema_version": PHASE91_SCHEMA_VERSION,
            "status": "V5_PHASE91_HISTORICAL_BLIND_RESEARCHER_PARITY_FAIL",
            "critical_counts": {"required_artifact_missing_count": len(missing_files)},
            "critical_count_sum": len(missing_files),
            "missing_files": missing_files,
        }

    target_registry = _read_json(paths["targets"])
    observation_registry = _read_json(paths["observations"])
    judgments = _read_jsonl(paths["judgments"])
    fact_signatures = _read_jsonl(paths["fact_signatures"])
    score_anchors = _read_jsonl(paths["score_anchors"])
    component_atlas = _read_json(paths["component_atlas"])
    component_anchors = tuple(component_atlas.get("component_anchors") or ())
    c06_component_replay = _read_json(paths["c06_component_replay"])
    source_backed_rows = _read_jsonl(paths["source_backed_replay"])
    source_backed_manifest = _read_json(paths["source_backed_manifest"])
    judgment_by_id = {
        str(row.get("judgment_id") or ""): row for row in judgments
    }
    selected = tuple(target_registry.get("targets") or ())
    c06_overrides = _c06_source_fact_overrides(c06_component_replay)
    cases: list[HistoricalBlindReplayCase] = []
    missing_target_ids: list[str] = []
    for row in selected:
        judgment_id = str(row.get("judgment_id") or "")
        target = judgment_by_id.get(judgment_id)
        if target is None:
            missing_target_ids.append(judgment_id)
            continue
        override = c06_overrides.get(
            (str(target.get("symbol") or ""), str(target.get("as_of_date") or "")),
            (),
        )
        cases.append(
            build_historical_blind_replay_case(
                blind_case_id=str(row.get("blind_case_id") or ""),
                target_judgment=target,
                judgments=judgments,
                fact_signatures=fact_signatures,
                score_anchors=score_anchors,
                component_anchors=component_anchors,
                source_fact_overrides=override,
            )
        )
    provider_rows = tuple(observation_registry.get("observations") or ())
    provider = FrozenHistoricalBlindResearchProvider(provider_rows)
    observations = run_historical_blind_replay(
        cases=cases,
        provider=provider,
        observation_origin="FROZEN_PHASE91_HISTORICAL_EVALUATION_RESPONSE",
    )
    metrics = evaluate_historical_blind_replay(cases=cases, observations=observations)
    registry_coverage = _registry_holdout_coverage(judgments, cases)
    c06_coverage = _c06_mandatory_coverage(component_atlas, c06_component_replay)
    guard_audit = _source_backed_guard_audit(
        source_backed_rows,
        source_backed_manifest,
    )
    provider_payloads = [row["payload"] for row in provider.calls]
    evaluator_target_hashes = {
        row.evaluator_target.target_hash for row in cases
    }
    provider_payload_hashes = {_stable_hash(row) for row in provider_payloads}
    observation_lineage_failures = sum(
        len(row.component_decision_ids) != 7
        or len(row.judge_ids) != 21
        or len(row.prompt_hashes) != 21
        or not row.fact_ids
        or not row.anchor_ids
        for row in observations
    )
    metric_values = {
        "component_normalized_mae": metrics["component_normalized_mae"],
        "total_proxy_mae": metrics["total_proxy_mae"],
        "spearman_rank_correlation": metrics["spearman_rank_correlation"],
        "stage_band_accuracy": metrics["stage_band_accuracy"],
        "critical_positive_counter_ordering": guard_audit[
            "critical_positive_counter_ordering"
        ],
        "false_positive_guard_accuracy": guard_audit[
            "false_positive_guard_accuracy"
        ],
    }
    critical = {
        "required_artifact_missing_count": 0,
        "target_registry_schema_mismatch_count": int(
            target_registry.get("schema_version")
            != "e2r_v5_historical_blind_replay_target_registry_v1"
        ),
        "observation_registry_schema_mismatch_count": int(
            observation_registry.get("schema_version")
            != "e2r_v5_historical_blind_replay_observation_registry_v1"
        ),
        "selected_target_missing_count": len(missing_target_ids),
        "selected_target_count_mismatch_count": int(len(cases) != len(selected)),
        "selected_target_not_source_backed_count": sum(
            not row.evaluator_target.source_quality.startswith("SOURCE_BACKED")
            for row in cases
        ),
        "source_proxy_target_count": sum(
            row.evaluator_target.source_quality == "SOURCE_PROXY_ONLY"
            for row in cases
        ),
        "leave_one_out_target_presence_count": sum(
            row.memory_audit.target_presence_count for row in cases
        ),
        "provider_payload_answer_leakage_count": sum(
            len(blind_payload_leakage_paths(row)) for row in provider_payloads
        ),
        "provider_received_evaluator_target_hash_count": len(
            evaluator_target_hashes & provider_payload_hashes
        ),
        "future_source_leakage_count": _future_source_leakage_count(cases),
        "historical_outcome_exposed_count": sum(
            _FORBIDDEN_VALUE_RE.search(json.dumps(row, ensure_ascii=False)) is not None
            for row in provider_payloads
        ),
        "metric_internal_critical_count": int(metrics["critical_count_sum"]),
        "component_normalized_mae_threshold_failure_count": int(
            metric_values["component_normalized_mae"] is None
            or metric_values["component_normalized_mae"]
            > PHASE91_THRESHOLDS["component_normalized_mae_max"]
        ),
        "total_proxy_mae_threshold_failure_count": int(
            metric_values["total_proxy_mae"] is None
            or metric_values["total_proxy_mae"]
            > PHASE91_THRESHOLDS["total_proxy_mae_max"]
        ),
        "spearman_rank_threshold_failure_count": int(
            metric_values["spearman_rank_correlation"] is None
            or metric_values["spearman_rank_correlation"]
            < PHASE91_THRESHOLDS["spearman_rank_correlation_min"]
        ),
        "stage_band_accuracy_threshold_failure_count": int(
            metric_values["stage_band_accuracy"] is None
            or metric_values["stage_band_accuracy"]
            < PHASE91_THRESHOLDS["stage_band_accuracy_min"]
        ),
        "critical_positive_counter_ordering_failure_count": int(
            metric_values["critical_positive_counter_ordering"]
            < PHASE91_THRESHOLDS["critical_positive_counter_ordering_min"]
        ),
        "false_positive_guard_accuracy_failure_count": int(
            metric_values["false_positive_guard_accuracy"]
            < PHASE91_THRESHOLDS["false_positive_guard_accuracy_min"]
        ),
        "score_dynamic_range_collapse_count": int(
            metrics["dynamic_range_audit"]["collapsed_to_zero_twenty"]
        ),
        "registry_archetype_accounting_mismatch_count": abs(
            len(registry_coverage) - len(CANONICAL_ARCHETYPE_IDS)
        ),
        "registry_archetype_unclassified_count": sum(
            row["coverage_status"]
            not in {"SOURCE_BACKED_HOLDOUT", "EXACT_SOURCE_GAP"}
            for row in registry_coverage
        ),
        "registry_source_gap_without_reason_count": sum(
            row["coverage_status"] == "EXACT_SOURCE_GAP"
            and not row.get("exact_source_gap_reason")
            for row in registry_coverage
        ),
        "source_proxy_promoted_to_holdout_count": sum(
            row.get("source_proxy_holdout_count", 0) for row in registry_coverage
        ),
        "c06_mandatory_family_accounting_mismatch_count": abs(
            len(c06_coverage) - 6
        ),
        "c06_mandatory_family_unclassified_count": sum(
            row["coverage_status"]
            not in {"SOURCE_BACKED_HOLDOUT", "EXACT_SOURCE_GAP"}
            for row in c06_coverage
        ),
        "c06_exact_gap_without_reason_count": sum(
            row["coverage_status"] == "EXACT_SOURCE_GAP"
            and not row.get("exact_source_gap_reason")
            for row in c06_coverage
        ),
        "source_backed_guard_manifest_failure_count": int(
            guard_audit["source_backed_manifest_status"]
            != "HISTORICAL_SOURCE_BACKED_REPLAY_PASS"
        ),
        "observation_lineage_failure_count": observation_lineage_failures,
        "observation_production_stage_authority_count": sum(
            row.production_stage_authority for row in observations
        ),
        "historical_replay_current_score_credit_count": guard_audit[
            "current_score_credit_count"
        ],
    }
    status = (
        PHASE91_PASS
        if sum(critical.values()) == 0
        else "V5_PHASE91_HISTORICAL_BLIND_RESEARCHER_PARITY_FAIL"
    )
    report = {
        "schema_version": PHASE91_SCHEMA_VERSION,
        "status": status,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "thresholds": dict(PHASE91_THRESHOLDS),
        "phase_scope": "HISTORICAL_EVALUATION_ONLY",
        "production_current_score_authority": False,
        "production_stage_authority": False,
        "frozen_observation_replay": True,
        "frozen_observation_is_production_readiness_evidence": False,
        "target_case_excluded_from_memory": True,
        "future_outcomes_hidden_from_researcher": True,
        "reported_score_hidden_from_researcher": True,
        "reported_stage_hidden_from_researcher": True,
        "as_of_date_sources_only": True,
        "metric_values": metric_values,
        "metrics": metrics,
        "replay_case_count": len(cases),
        "exact_anchor_target_count": sum(
            row.evaluator_target.usable_as_exact_anchor for row in cases
        ),
        "partial_component_target_count": sum(
            set(row.evaluator_target.historical_component_vector)
            != set(CANONICAL_COMPONENT_ORDER)
            for row in cases
        ),
        "leave_one_out_audits": [row.memory_audit.to_dict() for row in cases],
        "blind_input_records": [
            {
                "blind_case_id": row.research_input.blind_case_id,
                "input_hash": row.research_input.input_hash,
                "source_fact_count": len(row.research_input.source_facts),
                "safe_anchor_count": len(row.research_input.historical_anchors),
                "evaluator_answer_field_count": len(
                    blind_payload_leakage_paths(
                        row.research_input.to_provider_payload()
                    )
                ),
            }
            for row in cases
        ],
        "observations": [row.to_dict() for row in observations],
        "registry_archetype_coverage": registry_coverage,
        "registry_archetype_count": len(registry_coverage),
        "registry_source_backed_holdout_count": sum(
            row["coverage_status"] == "SOURCE_BACKED_HOLDOUT"
            for row in registry_coverage
        ),
        "registry_exact_source_gap_count": sum(
            row["coverage_status"] == "EXACT_SOURCE_GAP"
            for row in registry_coverage
        ),
        "c06_mandatory_coverage": c06_coverage,
        "source_backed_guard_audit": guard_audit,
    }
    report["audit_hash"] = _stable_hash(
        {
            "critical": critical,
            "metrics": metric_values,
            "case_inputs": [row.research_input.input_hash for row in cases],
            "observations": [row.provider_response_hash for row in observations],
            "registry": registry_coverage,
            "c06": c06_coverage,
            "guards": guard_audit,
        }
    )
    return _json_safe(report)


def write_phase91_historical_blind_replay_audit(
    *,
    repo_root: str | Path,
    output_path: str | Path | None = None,
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE91_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(destination, compile_phase91_historical_blind_replay_audit(root))
    return destination


def _blind_anchor_payload(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "anchor_id": str(row.get("anchor_id") or ""),
        "archetype_id": str(row.get("archetype_id") or ""),
        "component_id": str(row.get("component_id") or ""),
        "economic_fact_patterns": [
            str(value) for value in row.get("economic_fact_patterns") or ()
        ],
        "role": str(row.get("role") or ""),
        "score_band": str(row.get("score_band") or ""),
        "points_lower": float(row.get("points_lower") or 0.0),
        "points_mid": float(row.get("points_mid") or 0.0),
        "points_upper": float(row.get("points_upper") or 0.0),
        "max_points": float(row.get("max_points") or 0.0),
        "confidence": str(row.get("confidence") or ""),
        "usable_as_exact_anchor": bool(row.get("usable_as_exact_anchor")),
        "usable_as_ordinal_anchor": bool(row.get("usable_as_ordinal_anchor")),
    }


def _blind_fact_payload(
    row: Mapping[str, Any], *, as_of_date: str
) -> Mapping[str, Any]:
    return {
        "fact_id": str(row.get("fact_signature_id") or ""),
        "economic_fact": str(row.get("economic_fact_pattern") or ""),
        "source_text": str(row.get("source_text") or ""),
        "source_reference_ids": [str(row.get("fact_signature_id") or "")],
        "available_date": as_of_date,
    }


def _c06_source_fact_overrides(
    replay: Mapping[str, Any],
) -> Mapping[tuple[str, str], tuple[Mapping[str, Any], ...]]:
    result: dict[tuple[str, str], list[Mapping[str, Any]]] = {}
    for row in replay.get("cases") or ():
        if row.get("source_verified") is not True or row.get("future_leakage_count"):
            continue
        key = (str(row.get("target_id") or ""), str(row.get("as_of_date") or ""))
        result.setdefault(key, []).append(
            {
                "fact_id": str(row.get("claim_id") or row.get("case_id") or ""),
                "economic_fact": str(row.get("primitive_id") or ""),
                "source_text": str(
                    row.get("exact_quote")
                    or next(
                        (
                            proposal.get("rationale")
                            for proposal in row.get("proposal_rows") or ()
                            if proposal.get("rationale")
                        ),
                        row.get("case_id") or "",
                    )
                ),
                "source_reference_ids": [
                    str(row.get("source_content_sha256") or row.get("source_url") or "")
                ],
                "available_date": str(row.get("as_of_date") or ""),
            }
        )
    return {key: tuple(value) for key, value in result.items()}


def _registry_holdout_coverage(
    judgments: Sequence[Mapping[str, Any]],
    evaluated_cases: Sequence[HistoricalBlindReplayCase],
) -> list[Mapping[str, Any]]:
    evaluated_by_archetype: dict[str, list[str]] = {}
    for row in evaluated_cases:
        evaluated_by_archetype.setdefault(row.evaluator_target.archetype_id, []).append(
            row.evaluator_target.judgment_id
        )
    rows: list[Mapping[str, Any]] = []
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        eligible = [
            row
            for row in judgments
            if row.get("archetype_id") == archetype_id
            and str(row.get("source_quality") or "").startswith("SOURCE_BACKED")
            and bool(row.get("normalized_component_vector"))
            and not row.get("score_conflict")
        ]
        eligible.sort(
            key=lambda row: (
                not bool(row.get("usable_as_exact_anchor")),
                len(row.get("normalized_component_vector") or {})
                != len(CANONICAL_COMPONENT_ORDER),
                str(row.get("judgment_id") or ""),
            )
        )
        source_proxy = [
            row
            for row in judgments
            if row.get("archetype_id") == archetype_id
            and row.get("source_quality") == "SOURCE_PROXY_ONLY"
            and bool(row.get("normalized_component_vector"))
        ]
        if eligible:
            selected = eligible[0]
            coverage_status = "SOURCE_BACKED_HOLDOUT"
            exact_gap = None
            selected_judgment_id = selected.get("judgment_id")
            selected_case_id = selected.get("research_case_id")
        else:
            coverage_status = "EXACT_SOURCE_GAP"
            exact_gap = "NO_SOURCE_BACKED_NONCONFLICTING_COMPONENT_VECTOR_IN_ATLAS"
            selected_judgment_id = None
            selected_case_id = None
        rows.append(
            {
                "archetype_id": archetype_id,
                "coverage_status": coverage_status,
                "source_backed_holdout_candidate_count": len(eligible),
                "source_proxy_candidate_count": len(source_proxy),
                "source_proxy_holdout_count": 0,
                "selected_judgment_id": selected_judgment_id,
                "selected_research_case_id": selected_case_id,
                "evaluated_phase91_judgment_ids": sorted(
                    evaluated_by_archetype.get(archetype_id, [])
                ),
                "exact_source_gap_reason": exact_gap,
            }
        )
    return rows


_C06_VERIFIED_REPLAY_CASES: Mapping[str, tuple[str, ...]] = {
    "C06_DIRECT_SOLD_OUT_CUSTOMER_CAPACITY": (
        "C06-SKHYNIX-20240502-SOLDOUT",
    ),
    "C06_HBM_REVENUE_MIX_RECORD_PROFIT": (
        "C06-SKHYNIX-20250123-REVENUE-MIX",
        "C06-SAMSUNG-20250131-REOPEN-CAP",
    ),
    "C06_QUALIFICATION_LAG": (
        "C06-SAMSUNG-20240524-QUALIFICATION-LAG",
    ),
    "C06_REOPEN_CUSTOMER_DEPENDENCY": (),
    "C06_PROFILE_SUBSTRATE_SYMPATHY": (
        "C06-SKHYNIX-PRODUCT-SPEC-GUARD",
        "C06-SAMSUNG-PACKAGE-PROFILE-GUARD",
    ),
    "C06_LATE_CYCLE_VALUATION_PRICE_EXTENSION": (),
}


def _c06_mandatory_coverage(
    component_atlas: Mapping[str, Any],
    component_replay: Mapping[str, Any],
) -> list[Mapping[str, Any]]:
    replay_by_id = {
        str(row.get("case_id") or ""): row
        for row in component_replay.get("cases") or ()
    }
    by_family = {
        str(row.get("anchor_family_id") or ""): row
        for row in component_atlas.get("c06_mandatory_anchors") or ()
    }
    result = []
    for family_id in _C06_VERIFIED_REPLAY_CASES:
        atlas_row = by_family.get(family_id, {})
        source_backed_ids = tuple(
            str(value) for value in atlas_row.get("source_backed_case_ids") or ()
        )
        verified_ids = tuple(
            case_id
            for case_id in _C06_VERIFIED_REPLAY_CASES[family_id]
            if replay_by_id.get(case_id, {}).get("source_verified") is True
            and not replay_by_id.get(case_id, {}).get("future_leakage_count")
        )
        holdout = bool(source_backed_ids or verified_ids)
        result.append(
            {
                "anchor_family_id": family_id,
                "role": atlas_row.get("role"),
                "component_ids": list(atlas_row.get("component_ids") or ()),
                "coverage_status": (
                    "SOURCE_BACKED_HOLDOUT" if holdout else "EXACT_SOURCE_GAP"
                ),
                "source_backed_case_ids": list(source_backed_ids),
                "verified_component_replay_case_ids": list(verified_ids),
                "exact_source_gap_reason": (
                    None
                    if holdout
                    else "NO_VERIFIED_SOURCE_BACKED_HOLDOUT_FOR_C06_FAMILY"
                ),
                "company_name_conditioned": bool(
                    atlas_row.get("company_name_conditioned")
                ),
                "target_symbol_conditioned": bool(
                    atlas_row.get("target_symbol_conditioned")
                ),
            }
        )
    return result


def _source_backed_guard_audit(
    rows: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    decision_rank = {"REJECT_SCORE": 0, "ACCEPT_REPLAY_EVIDENCE": 1}
    guard_rows = [
        row for row in rows if row.get("source_role") in {"GUARD", "WRONG_SUBJECT"}
    ]
    guard_correct = sum(
        row.get("observed_decision") == row.get("expected_decision") == "REJECT_SCORE"
        for row in guard_rows
    )
    archetypes = sorted({str(row.get("archetype_id") or "") for row in rows})
    ordering_rows = []
    for archetype_id in archetypes:
        positives = [
            row
            for row in rows
            if row.get("archetype_id") == archetype_id
            and row.get("source_role") == "POSITIVE"
        ]
        counters = [
            row
            for row in rows
            if row.get("archetype_id") == archetype_id
            and row.get("source_role") in {"GUARD", "WRONG_SUBJECT"}
        ]
        if not positives or not counters:
            continue
        positive_ranks = [
            decision_rank.get(str(row.get("observed_decision") or ""), -1)
            for row in positives
        ]
        counter_ranks = [
            decision_rank.get(str(row.get("observed_decision") or ""), -1)
            for row in counters
        ]
        ordering_rows.append(
            {
                "archetype_id": archetype_id,
                "positive_case_ids": [row.get("case_id") for row in positives],
                "counter_case_ids": [row.get("case_id") for row in counters],
                "ordering_correct": min(positive_ranks) > max(counter_ranks),
            }
        )
    ordering_accuracy = _mean(
        [1.0 if row["ordering_correct"] else 0.0 for row in ordering_rows]
    )
    guard_accuracy = guard_correct / len(guard_rows) if guard_rows else 0.0
    return {
        "schema_version": "e2r_phase91_source_backed_guard_audit_v1",
        "source_backed_manifest_status": manifest.get("status"),
        "source_backed_replay_case_count": len(rows),
        "positive_case_count": sum(row.get("source_role") == "POSITIVE" for row in rows),
        "false_positive_guard_count": len(guard_rows),
        "false_positive_guard_correct_count": guard_correct,
        "false_positive_guard_accuracy": guard_accuracy,
        "critical_ordering_pair_count": len(ordering_rows),
        "critical_positive_counter_ordering": ordering_accuracy or 0.0,
        "ordering_rows": ordering_rows,
        "current_score_credit_count": sum(
            int(row.get("current_score_credit") or 0) != 0 for row in rows
        ),
        "future_leakage_count": sum(
            str(row.get("published_date") or "") > str(row.get("as_of_date") or "")
            or str(row.get("available_date") or "") > str(row.get("as_of_date") or "")
            for row in rows
        ),
    }


def _future_source_leakage_count(
    cases: Sequence[HistoricalBlindReplayCase],
) -> int:
    count = 0
    for row in cases:
        cutoff = date.fromisoformat(row.research_input.as_of_date)
        for fact in row.research_input.source_facts:
            count += date.fromisoformat(str(fact.get("available_date") or "")) > cutoff
    return count


def _dynamic_range_group(value: float) -> str:
    if value < PHASE91_DYNAMIC_RANGE["low_upper_exclusive"]:
        return "LOW"
    if value >= PHASE91_DYNAMIC_RANGE["high_lower_inclusive"]:
        return "HIGH"
    return "MID"


def _dynamic_range_audit(
    evaluations: Sequence[HistoricalBlindReplayEvaluation],
) -> Mapping[str, Any]:
    grouped: dict[str, list[HistoricalBlindReplayEvaluation]] = {
        "LOW": [],
        "MID": [],
        "HIGH": [],
    }
    for row in evaluations:
        if row.dynamic_range_group is not None:
            grouped[row.dynamic_range_group].append(row)
    reconstructed = [
        float(row.reconstructed_total_proxy)
        for values in grouped.values()
        for row in values
        if row.reconstructed_total_proxy is not None
    ]
    collapsed = bool(
        all(grouped.values())
        and reconstructed
        and max(reconstructed)
        <= PHASE91_DYNAMIC_RANGE["collapse_upper_inclusive"]
    )
    return {
        "group_boundaries": dict(PHASE91_DYNAMIC_RANGE),
        "historical_group_count": sum(bool(values) for values in grouped.values()),
        "group_counts": {key: len(values) for key, values in grouped.items()},
        "reconstructed_total_min": min(reconstructed) if reconstructed else None,
        "reconstructed_total_max": max(reconstructed) if reconstructed else None,
        "reconstructed_total_span": (
            max(reconstructed) - min(reconstructed) if reconstructed else None
        ),
        "collapsed_to_zero_twenty": collapsed,
    }


def _spearman_rank_correlation(
    expected: Sequence[float], observed: Sequence[float]
) -> float | None:
    if len(expected) != len(observed) or len(expected) < 3:
        return None
    expected_ranks = _average_ranks(expected)
    observed_ranks = _average_ranks(observed)
    expected_mean = sum(expected_ranks) / len(expected_ranks)
    observed_mean = sum(observed_ranks) / len(observed_ranks)
    numerator = sum(
        (left - expected_mean) * (right - observed_mean)
        for left, right in zip(expected_ranks, observed_ranks)
    )
    left_sq = sum((value - expected_mean) ** 2 for value in expected_ranks)
    right_sq = sum((value - observed_mean) ** 2 for value in observed_ranks)
    denominator = math.sqrt(left_sq * right_sq)
    if denominator == 0:
        return None
    return numerator / denominator


def _average_ranks(values: Sequence[float]) -> tuple[float, ...]:
    ordered = sorted(enumerate(values), key=lambda item: (float(item[1]), item[0]))
    result = [0.0] * len(values)
    index = 0
    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and float(ordered[end][1]) == float(ordered[index][1]):
            end += 1
        average = ((index + 1) + end) / 2.0
        for position in range(index, end):
            result[ordered[position][0]] = average
        index = end
    return tuple(result)


def _validate_component_maxima(value: Mapping[str, float]) -> None:
    if tuple(value) != tuple(CANONICAL_COMPONENT_ORDER):
        raise ValueError("component maxima require canonical component order")
    if any(not _finite(points) or float(points) <= 0 for points in value.values()):
        raise ValueError("component maxima must be finite and positive")
    if abs(sum(float(points) for points in value.values()) - 100.0) > 1e-6:
        raise ValueError("component maxima must reconcile to 100 points")


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    result = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, Mapping):
            raise ValueError(f"JSONL object required: {path}:{line_number}")
        result.append(value)
    return tuple(result)


def _mean(values: Sequence[float]) -> float | None:
    return sum(float(value) for value in values) / len(values) if values else None


def _stable_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str).encode(
            "utf-8"
        )
    ).hexdigest()


def _json_safe(value: Any) -> Any:
    """Return the exact JSON shape writers/readers will observe."""

    return json.loads(
        json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    )


def _finite(value: Any) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def _require_text(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} is required")


def _require_sha256(value: str, label: str) -> None:
    if len(value) != 64:
        raise ValueError(f"{label} must be sha256")
    try:
        int(value, 16)
    except ValueError as exc:
        raise ValueError(f"{label} must be hexadecimal") from exc


def _unique_text(
    values: Sequence[str], label: str, *, allow_empty: bool = False
) -> None:
    if not allow_empty and not values:
        raise ValueError(f"{label} cannot be empty")
    if len(values) != len(set(values)) or any(
        not isinstance(value, str) or not value.strip() for value in values
    ):
        raise ValueError(f"{label} must contain unique non-empty strings")


__all__ = [
    "FrozenHistoricalBlindResearchProvider",
    "HistoricalBlindReplayCase",
    "HistoricalBlindReplayEvaluation",
    "HistoricalBlindReplayObservation",
    "HistoricalBlindResearchInput",
    "HistoricalBlindResearchProvider",
    "HistoricalReplayEvaluationTarget",
    "LeaveOneOutMemoryAudit",
    "PHASE91_AUDIT_PATH",
    "PHASE91_DYNAMIC_RANGE",
    "PHASE91_OBSERVATION_REGISTRY_PATH",
    "PHASE91_PASS",
    "PHASE91_SCHEMA_VERSION",
    "PHASE91_TARGET_REGISTRY_PATH",
    "PHASE91_THRESHOLDS",
    "blind_payload_leakage_paths",
    "build_historical_blind_replay_case",
    "build_leave_one_out_memory",
    "canonical_historical_stage_band",
    "compile_phase91_historical_blind_replay_audit",
    "evaluate_historical_blind_replay",
    "run_historical_blind_replay",
    "write_phase91_historical_blind_replay_audit",
]
