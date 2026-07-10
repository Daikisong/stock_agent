"""Deterministic claim-backed score and StageCourt atomic decision."""

from __future__ import annotations

import math
import re
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash


ATOMIC_SCORE_STAGE_SCHEMA_VERSION = "e2r_atomic_score_stage_v1"


class AtomicScoreType(str, Enum):
    EVENT_EVIDENCE_PARTIAL = "EVENT_EVIDENCE_PARTIAL"
    FULL_E2R_100 = "FULL_E2R_100"
    NO_SCORE = "NO_SCORE"


class AtomicScoringScope(str, Enum):
    EVENT_EVIDENCE = "EVENT_EVIDENCE"
    FULL_THESIS = "FULL_THESIS"


class AtomicDecisionStatus(str, Enum):
    FINAL = "FINAL"
    EVENT_PARTIAL = "EVENT_PARTIAL"
    PENDING = "PENDING"
    RISK_REVIEW = "RISK_REVIEW"


class AtomicPrimitiveStatus(str, Enum):
    SATISFIED = "SATISFIED"
    MISSING = "MISSING"
    CONTRADICTED = "CONTRADICTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class AtomicClaimPolarity(str, Enum):
    SUPPORT = "SUPPORT"
    COUNTER = "COUNTER"


class CanonicalStage(str, Enum):
    STAGE_0 = "0"
    STAGE_1 = "1"
    STAGE_2 = "2"
    STAGE_3_GREEN = "3-Green"
    STAGE_3_YELLOW = "3-Yellow"
    STAGE_3_RED = "3-Red"
    STAGE_4A = "4A"
    STAGE_4B = "4B"
    STAGE_4C = "4C"
    STAGE_5 = "5"


@dataclass(frozen=True)
class AtomicScoreRule:
    primitive_id: str
    component_key: str
    max_points: float
    material: bool
    green_required: bool = False

    def __post_init__(self) -> None:
        if not self.primitive_id.strip() or not self.component_key.strip():
            raise ValueError("atomic score rule identity is required")
        if not isinstance(self.max_points, (int, float)) or isinstance(
            self.max_points, bool
        ):
            raise ValueError("atomic score rule max_points must be numeric")
        if self.max_points <= 0.0 or self.max_points > 100.0:
            raise ValueError("atomic score rule points must be within 0..100")
        if not math.isfinite(float(self.max_points)):
            raise ValueError("atomic score rule points must be finite")
        if not isinstance(self.material, bool) or not isinstance(
            self.green_required, bool
        ):
            raise ValueError("atomic score rule flags must be boolean")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicScoreClaim:
    claim_id: str
    target_id: str
    primitive_id: str
    observed_date: str
    content_hash: str
    source_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    mapping_ids: tuple[str, ...]
    polarity: str
    target_direct: bool
    current_open: bool
    source_backed: bool
    material: bool
    contradiction_resolved: bool
    historical_replay: bool
    mapping_accepted: bool
    score_eligible: bool

    def __post_init__(self) -> None:
        AtomicClaimPolarity(self.polarity)
        if not all(
            item.strip()
            for item in (
                self.claim_id,
                self.target_id,
                self.primitive_id,
                self.observed_date,
                self.content_hash,
            )
        ):
            raise ValueError("atomic score claim identity is required")
        date.fromisoformat(self.observed_date)
        if re.fullmatch(r"[0-9a-f]{64}", self.content_hash) is None:
            raise ValueError("atomic claim content_hash must be SHA-256")
        _require_unique_text(self.source_ids, context="claim source ids")
        _require_unique_text(self.anchor_ids, context="claim anchor ids")
        _require_unique_text(
            self.mapping_ids,
            context="claim mapping ids",
            required=False,
        )
        for name in (
            "target_direct",
            "current_open",
            "source_backed",
            "material",
            "contradiction_resolved",
            "historical_replay",
            "mapping_accepted",
            "score_eligible",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"atomic claim {name} must be boolean")
        if self.score_eligible and (
            self.polarity != AtomicClaimPolarity.SUPPORT.value
            or not self.target_direct
            or not self.current_open
            or not self.source_backed
            or not self.contradiction_resolved
            or self.historical_replay
            or not self.mapping_accepted
            or not self.mapping_ids
        ):
            raise ValueError("score-eligible atomic claim violates evidence contract")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicPrimitiveAssessment:
    primitive_id: str
    status: str
    evidence_strength: float
    support_claim_ids: tuple[str, ...] = ()
    counter_claim_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        selected_status = AtomicPrimitiveStatus(self.status)
        if not self.primitive_id.strip():
            raise ValueError("atomic primitive assessment identity is required")
        if (
            not isinstance(self.evidence_strength, (int, float))
            or isinstance(self.evidence_strength, bool)
            or not 0.0 <= float(self.evidence_strength) <= 1.0
        ):
            raise ValueError("atomic primitive evidence_strength must be within 0..1")
        _require_unique_text(
            self.support_claim_ids,
            context="primitive support claims",
            required=False,
        )
        _require_unique_text(
            self.counter_claim_ids,
            context="primitive counter claims",
            required=False,
        )
        if selected_status == AtomicPrimitiveStatus.SATISFIED:
            if not self.support_claim_ids or self.evidence_strength <= 0.0:
                raise ValueError("satisfied primitive requires support and strength")
        elif selected_status == AtomicPrimitiveStatus.CONTRADICTED:
            if not self.counter_claim_ids or self.evidence_strength != 0.0:
                raise ValueError("contradicted primitive requires counter claims only")
        elif self.support_claim_ids or self.evidence_strength != 0.0:
            raise ValueError("missing/not-applicable primitive cannot carry score support")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicHardBreakSignal:
    signal_id: str
    claim_id: str
    condition_id: str
    unresolved: bool

    def __post_init__(self) -> None:
        if (
            not self.signal_id.strip()
            or not self.claim_id.strip()
            or not self.condition_id.strip()
        ):
            raise ValueError("atomic hard-break signal identity is required")
        if not isinstance(self.unresolved, bool):
            raise ValueError("atomic hard-break unresolved flag must be boolean")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicStageConfig:
    stage1_threshold: float = 40.0
    stage2_threshold: float = 65.0
    yellow_threshold: float = 80.0
    green_threshold: float = 90.0
    config_version: str = "canonical_stage_thresholds_v1"

    def __post_init__(self) -> None:
        thresholds = (
            self.stage1_threshold,
            self.stage2_threshold,
            self.yellow_threshold,
            self.green_threshold,
        )
        if not all(
            isinstance(item, (int, float)) and not isinstance(item, bool)
            for item in thresholds
        ):
            raise ValueError("atomic stage thresholds must be numeric")
        if not all(math.isfinite(float(item)) for item in thresholds):
            raise ValueError("atomic stage thresholds must be finite")
        if not 0.0 <= thresholds[0] < thresholds[1] < thresholds[2] < thresholds[3] <= 100.0:
            raise ValueError("atomic stage thresholds must be ordered within 0..100")
        if not self.config_version.strip():
            raise ValueError("atomic stage config version is required")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicScoreContribution:
    contribution_id: str
    primitive_id: str
    component_key: str
    points: float
    max_points: float
    support_claim_ids: tuple[str, ...]
    mapping_ids: tuple[str, ...]
    config_fingerprint: str

    def __post_init__(self) -> None:
        if not all(
            item.strip()
            for item in (
                self.contribution_id,
                self.primitive_id,
                self.component_key,
                self.config_fingerprint,
            )
        ):
            raise ValueError("atomic score contribution identity is required")
        if any(
            not isinstance(item, (int, float)) or isinstance(item, bool)
            for item in (self.points, self.max_points)
        ):
            raise ValueError("atomic score contribution points must be numeric")
        if not all(
            math.isfinite(float(item)) for item in (self.points, self.max_points)
        ):
            raise ValueError("atomic score contribution points must be finite")
        if self.max_points <= 0.0:
            raise ValueError("atomic score contribution max_points must be positive")
        if self.points <= 0.0 or self.points > self.max_points:
            raise ValueError("atomic score contribution points are outside rule bounds")
        _require_unique_text(self.support_claim_ids, context="contribution support claims")
        _require_unique_text(self.mapping_ids, context="contribution mapping ids")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicStageCourtTrace:
    trace_id: str
    input_fingerprint: str
    score_fingerprint: str
    config_fingerprint: str
    scoring_scope: str
    score_type: str
    score_value: float | None
    canonical_stage: str
    decision_status: str
    accepted_claim_ids: tuple[str, ...]
    contribution_ids: tuple[str, ...]
    material_gap_ids: tuple[str, ...]
    hard_break_claim_ids: tuple[str, ...]
    reasons: tuple[str, ...]

    def __post_init__(self) -> None:
        AtomicScoringScope(self.scoring_scope)
        AtomicScoreType(self.score_type)
        CanonicalStage(self.canonical_stage)
        AtomicDecisionStatus(self.decision_status)
        if not all(
            item.strip()
            for item in (
                self.trace_id,
                self.input_fingerprint,
                self.score_fingerprint,
                self.config_fingerprint,
            )
        ):
            raise ValueError("atomic StageCourt trace identity is required")
        for value in (
            self.input_fingerprint,
            self.score_fingerprint,
            self.config_fingerprint,
        ):
            if re.fullmatch(r"[0-9a-f]{64}", value) is None:
                raise ValueError("atomic StageCourt trace fingerprints must be SHA-256")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicStageDecision:
    decision_id: str
    target_id: str
    as_of_date: str
    scoring_scope: str
    score_type: str
    score_value: float | None
    raw_reference_score: float | None
    score_valid: bool
    score_finalization_allowed: bool
    canonical_stage: str
    decision_status: str
    scoring_config_version: str
    score_rules: tuple[AtomicScoreRule, ...]
    stage_config: AtomicStageConfig
    provider_pending: bool
    source_pending: bool
    has_prior_live_thesis: bool
    claims: tuple[AtomicScoreClaim, ...]
    primitive_assessments: tuple[AtomicPrimitiveAssessment, ...]
    contributions: tuple[AtomicScoreContribution, ...]
    hard_break_signals: tuple[AtomicHardBreakSignal, ...]
    accepted_claim_ids: tuple[str, ...]
    material_gap_ids: tuple[str, ...]
    missing_conditions: tuple[str, ...]
    hard_break_claim_ids: tuple[str, ...]
    rejected_hard_break_signal_ids: tuple[str, ...]
    input_fingerprint: str
    claim_state_hash: str
    config_fingerprint: str
    score_fingerprint: str
    stage_court_trace: AtomicStageCourtTrace
    schema_version: str = ATOMIC_SCORE_STAGE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        scoring_scope = AtomicScoringScope(self.scoring_scope)
        score_type = AtomicScoreType(self.score_type)
        CanonicalStage(self.canonical_stage)
        decision_status = AtomicDecisionStatus(self.decision_status)
        date.fromisoformat(self.as_of_date)
        if not self.decision_id.strip() or not self.target_id.strip():
            raise ValueError("atomic stage decision identity is required")
        if not self.scoring_config_version.strip() or not self.score_rules:
            raise ValueError("atomic decision scoring config leaf is required")
        for name in (
            "score_valid",
            "score_finalization_allowed",
            "provider_pending",
            "source_pending",
            "has_prior_live_thesis",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"atomic decision {name} must be boolean")
        _require_unique_text(
            self.accepted_claim_ids,
            context="decision accepted claims",
            required=False,
        )
        _require_unique_text(
            self.material_gap_ids,
            context="decision material gaps",
            required=False,
        )
        _require_unique_text(
            self.missing_conditions,
            context="decision missing conditions",
            required=False,
        )
        _require_unique_text(
            self.rejected_hard_break_signal_ids,
            context="decision rejected hard-break signals",
            required=False,
        )
        for name, value in (
            ("score_value", self.score_value),
            ("raw_reference_score", self.raw_reference_score),
        ):
            if value is not None and (
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not math.isfinite(float(value))
                or not 0.0 <= float(value) <= 100.0
            ):
                raise ValueError(f"atomic decision {name} must be within 0..100")
        if score_type == AtomicScoreType.FULL_E2R_100:
            if (
                scoring_scope != AtomicScoringScope.FULL_THESIS
                or self.score_value is None
                or not self.score_valid
                or not self.score_finalization_allowed
                or self.provider_pending
                or self.source_pending
                or not self.accepted_claim_ids
                or not self.contributions
                or self.material_gap_ids
                or self.missing_conditions
                or decision_status
                not in {
                    AtomicDecisionStatus.FINAL,
                    AtomicDecisionStatus.RISK_REVIEW,
                }
            ):
                raise ValueError("full E2R score violates atomic finalization contract")
        elif score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL:
            if (
                scoring_scope != AtomicScoringScope.EVENT_EVIDENCE
                or self.score_value is None
                or not self.score_valid
                or self.score_finalization_allowed
                or self.provider_pending
                or self.source_pending
                or decision_status
                not in {
                    AtomicDecisionStatus.EVENT_PARTIAL,
                    AtomicDecisionStatus.RISK_REVIEW,
                }
            ):
                raise ValueError("event partial score violates scope contract")
        elif (
            self.score_value is not None
            or self.score_valid
            or self.score_finalization_allowed
            or decision_status
            not in {
                AtomicDecisionStatus.PENDING,
                AtomicDecisionStatus.RISK_REVIEW,
            }
        ):
            raise ValueError("NO_SCORE decision cannot expose a valid score")
        contribution_total = round(sum(item.points for item in self.contributions), 6)
        if self.contributions and self.raw_reference_score is None:
            raise ValueError("atomic contribution ledger requires raw reference score")
        if not self.contributions and self.raw_reference_score is not None:
            raise ValueError("atomic raw reference score requires contributions")
        if (
            self.raw_reference_score is not None
            and round(self.raw_reference_score, 6) != contribution_total
        ):
            raise ValueError("atomic raw score differs from contribution ledger")
        if self.score_value is not None and round(self.score_value, 6) != contribution_total:
            raise ValueError("atomic visible score differs from contribution ledger")
        claim_ids = {item.claim_id for item in self.claims}
        if len(claim_ids) != len(self.claims):
            raise ValueError("atomic decision claims contain duplicate ids")
        if not set(self.accepted_claim_ids).issubset(claim_ids):
            raise ValueError("atomic decision references unknown accepted claim")
        if any(
            not set(item.support_claim_ids).issubset(claim_ids)
            for item in self.contributions
        ):
            raise ValueError("atomic contribution references unknown claim")
        claim_by_id = {item.claim_id: item for item in self.claims}
        contribution_claim_ids = {
            claim_id
            for contribution in self.contributions
            for claim_id in contribution.support_claim_ids
        }
        if contribution_claim_ids != set(self.accepted_claim_ids):
            raise ValueError("atomic accepted claims differ from contribution ledger")
        if (
            len({item.contribution_id for item in self.contributions})
            != len(self.contributions)
            or len({item.primitive_id for item in self.contributions})
            != len(self.contributions)
        ):
            raise ValueError("atomic contribution ledger contains duplicates")
        as_of = date.fromisoformat(self.as_of_date)
        rules_by_primitive = {item.primitive_id: item for item in self.score_rules}
        assessments_by_primitive = {
            item.primitive_id: item for item in self.primitive_assessments
        }
        if (
            len(rules_by_primitive) != len(self.score_rules)
            or set(rules_by_primitive) != set(assessments_by_primitive)
            or round(sum(item.max_points for item in self.score_rules), 6) != 100.0
        ):
            raise ValueError("atomic decision score configuration is incomplete")
        if score_type == AtomicScoreType.FULL_E2R_100 and any(
            assessment.status == AtomicPrimitiveStatus.CONTRADICTED.value
            for assessment in self.primitive_assessments
        ):
            raise ValueError("full E2R score cannot carry an open contradiction")
        for contribution in self.contributions:
            support_claims = tuple(
                claim_by_id[claim_id]
                for claim_id in contribution.support_claim_ids
            )
            rule = rules_by_primitive.get(contribution.primitive_id)
            assessment = assessments_by_primitive.get(contribution.primitive_id)
            if (
                rule is None
                or assessment is None
                or rule.component_key != contribution.component_key
                or rule.max_points != contribution.max_points
                or assessment.status != AtomicPrimitiveStatus.SATISFIED.value
                or not set(contribution.support_claim_ids).issubset(
                    assessment.support_claim_ids
                )
                or round(
                    rule.max_points * assessment.evidence_strength,
                    6,
                )
                != round(contribution.points, 6)
            ):
                raise ValueError("atomic contribution differs from scoring rule")
            if contribution.config_fingerprint != self.config_fingerprint:
                raise ValueError("atomic contribution config fingerprint mismatch")
            if any(
                claim.target_id != self.target_id
                or claim.primitive_id != contribution.primitive_id
                or date.fromisoformat(claim.observed_date) > as_of
                or claim.polarity != AtomicClaimPolarity.SUPPORT.value
                or not claim.score_eligible
                or (rule.material and not claim.material)
                for claim in support_claims
            ):
                raise ValueError("atomic contribution contains ineligible support claim")
            expected_mapping_ids = {
                mapping_id
                for claim in support_claims
                for mapping_id in claim.mapping_ids
            }
            if set(contribution.mapping_ids) != expected_mapping_ids:
                raise ValueError("atomic contribution mapping lineage mismatch")
            expected_contribution_payload = {
                "primitive_id": contribution.primitive_id,
                "component_key": contribution.component_key,
                "points": contribution.points,
                "max_points": contribution.max_points,
                "support_claim_ids": list(contribution.support_claim_ids),
                "mapping_ids": list(contribution.mapping_ids),
                "config_fingerprint": contribution.config_fingerprint,
            }
            if contribution.contribution_id != "ACON-" + stable_hash(
                expected_contribution_payload
            )[:24]:
                raise ValueError("atomic contribution id fingerprint mismatch")
        if score_type == AtomicScoreType.FULL_E2R_100:
            contribution_by_primitive = {
                item.primitive_id: item for item in self.contributions
            }
            for assessment in self.primitive_assessments:
                if assessment.status != AtomicPrimitiveStatus.SATISFIED.value:
                    continue
                contribution = contribution_by_primitive.get(assessment.primitive_id)
                if (
                    contribution is None
                    or tuple(contribution.support_claim_ids)
                    != tuple(assessment.support_claim_ids)
                ):
                    raise ValueError(
                        "full E2R score has an unresolved assessment claim"
                    )
        contribution_primitives = {
            item.primitive_id for item in self.contributions
        }
        derived_material_gaps = {
            primitive_id
            for primitive_id, rule in rules_by_primitive.items()
            if rule.material
            and (
                assessments_by_primitive[primitive_id].status
                != AtomicPrimitiveStatus.SATISFIED.value
                or primitive_id not in contribution_primitives
            )
        }
        if set(self.material_gap_ids) != derived_material_gaps:
            raise ValueError("atomic material gaps differ from primitive ledger")
        _require_unique_text(
            self.hard_break_claim_ids,
            context="decision hard-break claims",
            required=False,
        )
        signal_ids = {item.signal_id for item in self.hard_break_signals}
        if len(signal_ids) != len(self.hard_break_signals):
            raise ValueError("atomic decision hard-break signals contain duplicate ids")
        if not set(self.rejected_hard_break_signal_ids).issubset(signal_ids):
            raise ValueError("atomic decision references unknown rejected hard-break signal")
        derived_hard_break_claim_ids: list[str] = []
        derived_rejected_signal_ids: list[str] = []
        for signal in self.hard_break_signals:
            claim = claim_by_id.get(signal.claim_id)
            valid = bool(
                claim
                and claim.target_id == self.target_id
                and date.fromisoformat(claim.observed_date) <= as_of
                and claim.target_direct
                and claim.current_open
                and claim.source_backed
                and claim.material
                and claim.polarity == AtomicClaimPolarity.COUNTER.value
                and not claim.historical_replay
                and signal.unresolved
            )
            if valid:
                if signal.claim_id not in derived_hard_break_claim_ids:
                    derived_hard_break_claim_ids.append(signal.claim_id)
            else:
                derived_rejected_signal_ids.append(signal.signal_id)
        if (
            tuple(derived_hard_break_claim_ids) != self.hard_break_claim_ids
            or tuple(derived_rejected_signal_ids)
            != self.rejected_hard_break_signal_ids
        ):
            raise ValueError("atomic hard break violates current direct OPEN contract")
        if self.hard_break_claim_ids:
            expected_stage = (
                CanonicalStage.STAGE_4C
                if self.has_prior_live_thesis
                else CanonicalStage.STAGE_3_RED
            )
            expected_status = AtomicDecisionStatus.RISK_REVIEW
        elif score_type == AtomicScoreType.NO_SCORE:
            expected_stage = CanonicalStage.STAGE_0
            expected_status = AtomicDecisionStatus.PENDING
        else:
            expected_stage = _stage_for_score(
                float(self.score_value),
                assessments=assessments_by_primitive,
                rules=rules_by_primitive,
                config=self.stage_config,
                event_partial=(
                    score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL
                ),
            )
            expected_status = (
                AtomicDecisionStatus.EVENT_PARTIAL
                if score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL
                else AtomicDecisionStatus.FINAL
            )
        if (
            self.canonical_stage != expected_stage.value
            or self.decision_status != expected_status.value
        ):
            raise ValueError("atomic stage or status differs from deterministic score")
        trace = self.stage_court_trace
        if (
            trace.input_fingerprint != self.input_fingerprint
            or trace.score_fingerprint != self.score_fingerprint
            or trace.config_fingerprint != self.config_fingerprint
            or trace.scoring_scope != self.scoring_scope
            or trace.score_type != self.score_type
            or trace.score_value != self.score_value
            or trace.canonical_stage != self.canonical_stage
            or trace.decision_status != self.decision_status
            or trace.accepted_claim_ids != self.accepted_claim_ids
            or trace.contribution_ids
            != tuple(item.contribution_id for item in self.contributions)
            or trace.material_gap_ids != self.material_gap_ids
            or trace.hard_break_claim_ids != self.hard_break_claim_ids
        ):
            raise ValueError("atomic decision and StageCourt trace mismatch")
        expected_trace_reasons = tuple(
            dict.fromkeys(
                (
                    *self.missing_conditions,
                    *(f"hard_break:{item}" for item in self.hard_break_claim_ids),
                    *(
                        f"hard_break_rejected:{item}"
                        for item in self.rejected_hard_break_signal_ids
                    ),
                )
            )
        )
        if trace.reasons != expected_trace_reasons:
            raise ValueError("atomic decision and StageCourt reasons mismatch")
        expected_claim_hash = stable_hash([item.to_dict() for item in self.claims])
        if expected_claim_hash != self.claim_state_hash:
            raise ValueError("atomic decision claim-state fingerprint mismatch")
        expected_config_hash = stable_hash(
            {
                "scoring_config_version": self.scoring_config_version,
                "rules": [item.to_dict() for item in self.score_rules],
                "stage_config": self.stage_config.to_dict(),
            }
        )
        if expected_config_hash != self.config_fingerprint:
            raise ValueError("atomic decision config fingerprint mismatch")
        expected_input_hash = _input_fingerprint_payload(
            target_id=self.target_id,
            as_of_date=self.as_of_date,
            scoring_scope=self.scoring_scope,
            claims=[item.to_dict() for item in self.claims],
            primitive_assessments=[
                item.to_dict() for item in self.primitive_assessments
            ],
            hard_break_signals=[item.to_dict() for item in self.hard_break_signals],
            provider_pending=self.provider_pending,
            source_pending=self.source_pending,
            has_prior_live_thesis=self.has_prior_live_thesis,
            config_fingerprint=self.config_fingerprint,
        )
        if expected_input_hash != self.input_fingerprint:
            raise ValueError("atomic decision input fingerprint mismatch")
        expected_score_hash = _score_fingerprint_payload(
            scoring_scope=self.scoring_scope,
            score_type=self.score_type,
            score_value=self.score_value,
            raw_reference_score=self.raw_reference_score,
            contribution_payload=[item.to_dict() for item in self.contributions],
            claim_state_hash=self.claim_state_hash,
            config_fingerprint=self.config_fingerprint,
        )
        if expected_score_hash != self.score_fingerprint:
            raise ValueError("atomic decision score fingerprint mismatch")
        expected_decision_id = "ADEC-" + stable_hash(
            {
                "target_id": self.target_id,
                "as_of_date": self.as_of_date,
                "input_fingerprint": self.input_fingerprint,
                "score_fingerprint": self.score_fingerprint,
                "stage": self.canonical_stage,
            }
        )[:24]
        if expected_decision_id != self.decision_id:
            raise ValueError("atomic decision id fingerprint mismatch")
        expected_trace_id = "ACTRACE-" + stable_hash(
            {
                "target_id": self.target_id,
                "input_fingerprint": self.input_fingerprint,
                "score_fingerprint": self.score_fingerprint,
                "stage": self.canonical_stage,
                "status": self.decision_status,
            }
        )[:24]
        if expected_trace_id != trace.trace_id:
            raise ValueError("atomic StageCourt trace id fingerprint mismatch")
        if self.schema_version != ATOMIC_SCORE_STAGE_SCHEMA_VERSION:
            raise ValueError("atomic decision schema version mismatch")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "claims": [item.to_dict() for item in self.claims],
            "score_rules": [item.to_dict() for item in self.score_rules],
            "stage_config": self.stage_config.to_dict(),
            "primitive_assessments": [
                item.to_dict() for item in self.primitive_assessments
            ],
            "contributions": [item.to_dict() for item in self.contributions],
            "hard_break_signals": [item.to_dict() for item in self.hard_break_signals],
            "stage_court_trace": self.stage_court_trace.to_dict(),
        }


@dataclass(frozen=True)
class AtomicScoringInput:
    target_id: str
    as_of_date: str
    scope: str
    claims: tuple[AtomicScoreClaim, ...]
    primitive_assessments: tuple[AtomicPrimitiveAssessment, ...]
    rules: tuple[AtomicScoreRule, ...]
    stage_config: AtomicStageConfig = AtomicStageConfig()
    hard_break_signals: tuple[AtomicHardBreakSignal, ...] = ()
    provider_pending: bool = False
    source_pending: bool = False
    has_prior_live_thesis: bool = False
    scoring_config_version: str = "canonical_atomic_scoring_v1"

    def __post_init__(self) -> None:
        AtomicScoringScope(self.scope)
        if not self.target_id.strip() or not self.scoring_config_version.strip():
            raise ValueError("atomic scoring input identity is required")
        date.fromisoformat(self.as_of_date)
        for name in ("provider_pending", "source_pending", "has_prior_live_thesis"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"atomic scoring input {name} must be boolean")
        if not self.rules or not self.primitive_assessments:
            raise ValueError("atomic scoring input requires rules and primitive assessments")
        if len({item.primitive_id for item in self.rules}) != len(self.rules):
            raise ValueError("atomic scoring rules contain duplicate primitives")
        if len({item.primitive_id for item in self.primitive_assessments}) != len(
            self.primitive_assessments
        ):
            raise ValueError("atomic primitive assessments contain duplicates")
        if len({item.signal_id for item in self.hard_break_signals}) != len(
            self.hard_break_signals
        ):
            raise ValueError("atomic hard-break signals contain duplicate ids")
        if {item.primitive_id for item in self.rules} != {
            item.primitive_id for item in self.primitive_assessments
        }:
            raise ValueError("atomic rules and primitive assessments differ")
        if round(sum(item.max_points for item in self.rules), 6) != 100.0:
            raise ValueError("atomic full scoring rules must total 100 points")


def adapt_claim_ledger_event_to_atomic_claim(
    event: Any,
    *,
    source_content_hash: str,
    material: bool,
    test_mode: bool = False,
    historical_replay: bool = False,
) -> AtomicScoreClaim:
    """Adapt one canonical Phase 9 claim leaf without granting new eligibility."""

    from e2r.research_brain.runtime.claim_compiler import ClaimLedgerEvent

    if not isinstance(event, ClaimLedgerEvent):
        raise TypeError("atomic claim adapter requires ClaimLedgerEvent")
    if not isinstance(test_mode, bool) or not isinstance(historical_replay, bool):
        raise ValueError("atomic claim adapter mode flags must be boolean")
    mapping_accepted = bool(
        event.mapping_id
        and event.mapped_primitive_id
        and event.mapping_status == "ACCEPTED"
    )
    inherited_eligibility = bool(
        event.production_score_eligible
        or (test_mode and event.score_eligible)
    )
    score_eligible = bool(
        inherited_eligibility
        and mapping_accepted
        and event.directness == "DIRECT"
        and event.temporal_status == "CURRENT"
        and event.support_direction == "SUPPORT"
        and not event.source_proxy_only
        and event.contradiction_resolved
        and not historical_replay
    )
    polarity = (
        AtomicClaimPolarity.SUPPORT.value
        if event.support_direction == "SUPPORT"
        else AtomicClaimPolarity.COUNTER.value
    )
    return AtomicScoreClaim(
        claim_id=event.claim_id,
        target_id=event.target_entity_id,
        primitive_id=event.mapped_primitive_id or event.original_primitive_id,
        observed_date=event.source_available_at,
        content_hash=source_content_hash,
        source_ids=tuple(
            dict.fromkeys((event.source_document_id, event.source_family))
        ),
        anchor_ids=(event.source_anchor_id,),
        mapping_ids=((event.mapping_id,) if event.mapping_id else ()),
        polarity=polarity,
        target_direct=event.directness == "DIRECT",
        current_open=(
            event.temporal_status == "CURRENT" and not event.superseded_by_claim_ids
        ),
        source_backed=not event.source_proxy_only,
        material=material,
        contradiction_resolved=event.contradiction_resolved,
        historical_replay=historical_replay,
        mapping_accepted=mapping_accepted,
        score_eligible=score_eligible,
    )


def decide_atomic_score_stage(inputs: AtomicScoringInput) -> AtomicStageDecision:
    as_of = date.fromisoformat(inputs.as_of_date)
    claims_by_id = {item.claim_id: item for item in inputs.claims}
    if len(claims_by_id) != len(inputs.claims):
        raise ValueError("atomic scoring claims contain duplicate ids")
    rules_by_primitive = {item.primitive_id: item for item in inputs.rules}
    config_fingerprint = stable_hash(
        {
            "scoring_config_version": inputs.scoring_config_version,
            "rules": [item.to_dict() for item in inputs.rules],
            "stage_config": inputs.stage_config.to_dict(),
        }
    )
    claim_state_hash = stable_hash([item.to_dict() for item in inputs.claims])
    input_fingerprint = _input_fingerprint_payload(
        target_id=inputs.target_id,
        as_of_date=inputs.as_of_date,
        scoring_scope=inputs.scope,
        claims=[item.to_dict() for item in inputs.claims],
        primitive_assessments=[
            item.to_dict() for item in inputs.primitive_assessments
        ],
        hard_break_signals=[item.to_dict() for item in inputs.hard_break_signals],
        provider_pending=inputs.provider_pending,
        source_pending=inputs.source_pending,
        has_prior_live_thesis=inputs.has_prior_live_thesis,
        config_fingerprint=config_fingerprint,
    )
    eligibility_errors: list[str] = []
    accepted_claim_ids: list[str] = []
    contributions: list[AtomicScoreContribution] = []
    material_gaps: list[str] = []
    missing_conditions: list[str] = []
    assessment_by_primitive = {
        item.primitive_id: item for item in inputs.primitive_assessments
    }
    for primitive_id, rule in rules_by_primitive.items():
        assessment = assessment_by_primitive[primitive_id]
        valid_support: list[str] = []
        for claim_id in assessment.support_claim_ids:
            claim = claims_by_id.get(claim_id)
            if claim is None:
                eligibility_errors.append(f"unknown_support_claim:{claim_id}")
                continue
            if (
                claim.target_id != inputs.target_id
                or claim.primitive_id != primitive_id
                or date.fromisoformat(claim.observed_date) > as_of
                or not claim.score_eligible
                or not claim.mapping_accepted
                or not claim.mapping_ids
                or claim.polarity != AtomicClaimPolarity.SUPPORT.value
                or (rule.material and not claim.material)
            ):
                eligibility_errors.append(f"ineligible_support_claim:{claim_id}")
                continue
            valid_support.append(claim_id)
            if claim_id not in accepted_claim_ids:
                accepted_claim_ids.append(claim_id)
        if assessment.status == AtomicPrimitiveStatus.SATISFIED.value and valid_support:
            points = round(rule.max_points * assessment.evidence_strength, 6)
            contribution_payload = {
                "primitive_id": primitive_id,
                "component_key": rule.component_key,
                "points": points,
                "max_points": rule.max_points,
                "support_claim_ids": valid_support,
                "mapping_ids": list(
                    dict.fromkeys(
                        mapping_id
                        for claim_id in valid_support
                        for mapping_id in claims_by_id[claim_id].mapping_ids
                    )
                ),
                "config_fingerprint": config_fingerprint,
            }
            contributions.append(
                AtomicScoreContribution(
                    contribution_id="ACON-" + stable_hash(contribution_payload)[:24],
                    primitive_id=primitive_id,
                    component_key=rule.component_key,
                    points=points,
                    max_points=rule.max_points,
                    support_claim_ids=tuple(valid_support),
                    mapping_ids=tuple(contribution_payload["mapping_ids"]),
                    config_fingerprint=config_fingerprint,
                )
            )
        elif assessment.status == AtomicPrimitiveStatus.SATISFIED.value:
            missing_conditions.append(f"eligible_claim_missing:{primitive_id}")
        if rule.material and (
            assessment.status != AtomicPrimitiveStatus.SATISFIED.value
            or not valid_support
        ):
            material_gaps.append(primitive_id)
        if assessment.status == AtomicPrimitiveStatus.CONTRADICTED.value:
            missing_conditions.append(f"contradiction_open:{primitive_id}")
    raw_score = round(sum(item.points for item in contributions), 6)
    valid_hard_break_claims: list[str] = []
    rejected_hard_break_signals: list[str] = []
    for signal in inputs.hard_break_signals:
        claim = claims_by_id.get(signal.claim_id)
        valid = bool(
            claim
            and claim.target_id == inputs.target_id
            and date.fromisoformat(claim.observed_date) <= as_of
            and claim.target_direct
            and claim.current_open
            and claim.source_backed
            and claim.material
            and claim.polarity == AtomicClaimPolarity.COUNTER.value
            and not claim.historical_replay
            and signal.unresolved
        )
        if valid:
            valid_hard_break_claims.append(signal.claim_id)
        else:
            rejected_hard_break_signals.append(signal.signal_id)
    blockers = tuple(
        dict.fromkeys(
            (
                *(("provider_pending",) if inputs.provider_pending else ()),
                *(("source_pending",) if inputs.source_pending else ()),
                *(("claimless_score",) if not contributions else ()),
                *(f"material_gap:{item}" for item in material_gaps),
                *eligibility_errors,
                *missing_conditions,
            )
        )
    )
    scope = AtomicScoringScope(inputs.scope)
    if scope == AtomicScoringScope.FULL_THESIS and blockers:
        score_type = AtomicScoreType.NO_SCORE
        score_value = None
        score_valid = False
        finalization_allowed = False
        status = AtomicDecisionStatus.PENDING
    elif scope == AtomicScoringScope.EVENT_EVIDENCE and (
        inputs.provider_pending or inputs.source_pending or not contributions
    ):
        score_type = AtomicScoreType.NO_SCORE
        score_value = None
        score_valid = False
        finalization_allowed = False
        status = AtomicDecisionStatus.PENDING
    elif scope == AtomicScoringScope.EVENT_EVIDENCE:
        score_type = AtomicScoreType.EVENT_EVIDENCE_PARTIAL
        score_value = raw_score
        score_valid = True
        finalization_allowed = False
        status = AtomicDecisionStatus.EVENT_PARTIAL
    else:
        score_type = AtomicScoreType.FULL_E2R_100
        score_value = raw_score
        score_valid = True
        finalization_allowed = True
        status = AtomicDecisionStatus.FINAL

    if valid_hard_break_claims:
        canonical_stage = (
            CanonicalStage.STAGE_4C
            if inputs.has_prior_live_thesis
            else CanonicalStage.STAGE_3_RED
        )
        status = AtomicDecisionStatus.RISK_REVIEW
    elif score_type == AtomicScoreType.NO_SCORE:
        canonical_stage = CanonicalStage.STAGE_0
    else:
        canonical_stage = _stage_for_score(
            float(score_value),
            assessments=assessment_by_primitive,
            rules=rules_by_primitive,
            config=inputs.stage_config,
            event_partial=score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL,
        )
    raw_reference_score = raw_score if contributions else None
    score_fingerprint = _score_fingerprint_payload(
        scoring_scope=inputs.scope,
        score_type=score_type.value,
        score_value=score_value,
        raw_reference_score=raw_reference_score,
        contribution_payload=[item.to_dict() for item in contributions],
        claim_state_hash=claim_state_hash,
        config_fingerprint=config_fingerprint,
    )
    reasons = tuple(
        dict.fromkeys(
            (
                *blockers,
                *(f"hard_break:{item}" for item in valid_hard_break_claims),
                *(
                    f"hard_break_rejected:{item}"
                    for item in rejected_hard_break_signals
                ),
            )
        )
    )
    trace_payload = {
        "target_id": inputs.target_id,
        "input_fingerprint": input_fingerprint,
        "score_fingerprint": score_fingerprint,
        "stage": canonical_stage.value,
        "status": status.value,
    }
    trace = AtomicStageCourtTrace(
        trace_id="ACTRACE-" + stable_hash(trace_payload)[:24],
        input_fingerprint=input_fingerprint,
        score_fingerprint=score_fingerprint,
        config_fingerprint=config_fingerprint,
        scoring_scope=inputs.scope,
        score_type=score_type.value,
        score_value=score_value,
        canonical_stage=canonical_stage.value,
        decision_status=status.value,
        accepted_claim_ids=tuple(accepted_claim_ids),
        contribution_ids=tuple(item.contribution_id for item in contributions),
        material_gap_ids=tuple(material_gaps),
        hard_break_claim_ids=tuple(dict.fromkeys(valid_hard_break_claims)),
        reasons=reasons,
    )
    decision_id = "ADEC-" + stable_hash(
        {
            "target_id": inputs.target_id,
            "as_of_date": inputs.as_of_date,
            "input_fingerprint": input_fingerprint,
            "score_fingerprint": score_fingerprint,
            "stage": canonical_stage.value,
        }
    )[:24]
    return AtomicStageDecision(
        decision_id=decision_id,
        target_id=inputs.target_id,
        as_of_date=inputs.as_of_date,
        scoring_scope=inputs.scope,
        score_type=score_type.value,
        score_value=score_value,
        raw_reference_score=raw_reference_score,
        score_valid=score_valid,
        score_finalization_allowed=finalization_allowed,
        canonical_stage=canonical_stage.value,
        decision_status=status.value,
        scoring_config_version=inputs.scoring_config_version,
        score_rules=inputs.rules,
        stage_config=inputs.stage_config,
        provider_pending=inputs.provider_pending,
        source_pending=inputs.source_pending,
        has_prior_live_thesis=inputs.has_prior_live_thesis,
        claims=inputs.claims,
        primitive_assessments=inputs.primitive_assessments,
        contributions=tuple(contributions),
        hard_break_signals=inputs.hard_break_signals,
        accepted_claim_ids=tuple(accepted_claim_ids),
        material_gap_ids=tuple(material_gaps),
        missing_conditions=tuple(dict.fromkeys((*blockers, *missing_conditions))),
        hard_break_claim_ids=tuple(dict.fromkeys(valid_hard_break_claims)),
        rejected_hard_break_signal_ids=tuple(rejected_hard_break_signals),
        input_fingerprint=input_fingerprint,
        claim_state_hash=claim_state_hash,
        config_fingerprint=config_fingerprint,
        score_fingerprint=score_fingerprint,
        stage_court_trace=trace,
    )


def audit_atomic_stage_decisions(
    decisions: Sequence[AtomicStageDecision | Mapping[str, Any]],
) -> Mapping[str, Any]:
    payloads = [
        item.to_dict() if isinstance(item, AtomicStageDecision) else dict(item)
        for item in decisions
    ]
    critical = {
        "claimless_score": 0,
        "material_gap_full_score": 0,
        "event_score_as_full": 0,
        "stage_score_trace_mismatch": 0,
        "pending_final_low_score": 0,
        "hard_break_without_current_direct_open": 0,
        "score_contribution_without_claim": 0,
        "score_contribution_without_mapping": 0,
        "fingerprint_mismatch_concealed": 0,
    }
    for payload in payloads:
        score_type = str(payload.get("score_type") or "")
        score_value = payload.get("score_value")
        claims = tuple(payload.get("claims") or ())
        claim_by_id = {
            str(item.get("claim_id")): item
            for item in claims
            if isinstance(item, Mapping) and item.get("claim_id")
        }
        accepted = tuple(str(item) for item in payload.get("accepted_claim_ids") or ())
        contributions = tuple(payload.get("contributions") or ())
        material_gaps = tuple(payload.get("material_gap_ids") or ())
        if score_type != AtomicScoreType.NO_SCORE.value and (
            not accepted or any(claim_id not in claim_by_id for claim_id in accepted)
        ):
            critical["claimless_score"] += 1
        derived_material_gaps = _payload_material_gap_ids(payload)
        if score_type == AtomicScoreType.FULL_E2R_100.value and (
            material_gaps
            or derived_material_gaps is None
            or derived_material_gaps
        ):
            critical["material_gap_full_score"] += 1
        if score_type == AtomicScoreType.FULL_E2R_100.value and str(
            payload.get("scoring_scope")
        ) == AtomicScoringScope.EVENT_EVIDENCE.value:
            critical["event_score_as_full"] += 1
        trace = payload.get("stage_court_trace")
        expected_trace_reasons = tuple(
            dict.fromkeys(
                (
                    *(str(item) for item in payload.get("missing_conditions") or ()),
                    *(
                        f"hard_break:{item}"
                        for item in payload.get("hard_break_claim_ids") or ()
                    ),
                    *(
                        f"hard_break_rejected:{item}"
                        for item in payload.get("rejected_hard_break_signal_ids")
                        or ()
                    ),
                )
            )
        )
        if not isinstance(trace, Mapping) or any(
            trace.get(key) != payload.get(payload_key)
            for key, payload_key in (
                ("score_type", "score_type"),
                ("scoring_scope", "scoring_scope"),
                ("score_value", "score_value"),
                ("canonical_stage", "canonical_stage"),
                ("decision_status", "decision_status"),
                ("input_fingerprint", "input_fingerprint"),
                ("score_fingerprint", "score_fingerprint"),
                ("config_fingerprint", "config_fingerprint"),
            )
        ):
            critical["stage_score_trace_mismatch"] += 1
        elif (
            tuple(trace.get("accepted_claim_ids") or ()) != accepted
            or tuple(trace.get("contribution_ids") or ())
            != tuple(
                str(item.get("contribution_id"))
                for item in contributions
                if isinstance(item, Mapping)
            )
            or tuple(trace.get("material_gap_ids") or ()) != material_gaps
            or tuple(trace.get("hard_break_claim_ids") or ())
            != tuple(payload.get("hard_break_claim_ids") or ())
            or tuple(trace.get("reasons") or ()) != expected_trace_reasons
            or not _payload_has_expected_stage_and_status(payload)
        ):
            critical["stage_score_trace_mismatch"] += 1
        if score_value is not None and (
            str(payload.get("decision_status"))
            == AtomicDecisionStatus.PENDING.value
            or score_type == AtomicScoreType.NO_SCORE.value
            or payload.get("provider_pending") is True
            or payload.get("source_pending") is True
        ):
            critical["pending_final_low_score"] += 1
        expected_hard_break_state = _payload_expected_hard_break_state(payload)
        if expected_hard_break_state is None or (
            tuple(payload.get("hard_break_claim_ids") or ())
            != expected_hard_break_state[0]
            or tuple(payload.get("rejected_hard_break_signal_ids") or ())
            != expected_hard_break_state[1]
        ):
            critical["hard_break_without_current_direct_open"] += 1
        for contribution in contributions:
            support_claim_ids = (
                tuple(str(item) for item in contribution.get("support_claim_ids") or ())
                if isinstance(contribution, Mapping)
                else ()
            )
            support_claims = tuple(
                claim_by_id.get(claim_id) for claim_id in support_claim_ids
            )
            if (
                not support_claim_ids
                or any(claim is None for claim in support_claims)
                or any(claim_id not in accepted for claim_id in support_claim_ids)
                or any(
                    claim is not None
                    and (
                        claim.get("score_eligible") is not True
                        or claim.get("target_direct") is not True
                        or claim.get("current_open") is not True
                        or claim.get("source_backed") is not True
                        or claim.get("contradiction_resolved") is not True
                    )
                    for claim in support_claims
                )
            ):
                critical["score_contribution_without_claim"] += 1
            mapping_ids = (
                tuple(str(item) for item in contribution.get("mapping_ids") or ())
                if isinstance(contribution, Mapping)
                else ()
            )
            expected_mapping_ids = {
                str(mapping_id)
                for claim in support_claims
                if claim is not None
                for mapping_id in claim.get("mapping_ids") or ()
            }
            if (
                not mapping_ids
                or set(mapping_ids) != expected_mapping_ids
                or any(
                    claim is not None and claim.get("mapping_accepted") is not True
                    for claim in support_claims
                )
            ):
                critical["score_contribution_without_mapping"] += 1
        expected_claim_hash = stable_hash(list(claims))
        expected_config_hash = stable_hash(
            {
                "scoring_config_version": payload.get("scoring_config_version"),
                "rules": list(payload.get("score_rules") or ()),
                "stage_config": payload.get("stage_config"),
            }
        )
        expected_input_hash = _input_fingerprint_payload(
            target_id=str(payload.get("target_id") or ""),
            as_of_date=str(payload.get("as_of_date") or ""),
            scoring_scope=str(payload.get("scoring_scope") or ""),
            claims=list(claims),
            primitive_assessments=list(payload.get("primitive_assessments") or ()),
            hard_break_signals=list(payload.get("hard_break_signals") or ()),
            provider_pending=bool(payload.get("provider_pending")),
            source_pending=bool(payload.get("source_pending")),
            has_prior_live_thesis=bool(payload.get("has_prior_live_thesis")),
            config_fingerprint=str(payload.get("config_fingerprint") or ""),
        )
        expected_score_hash = _score_fingerprint_payload(
            scoring_scope=str(payload.get("scoring_scope") or ""),
            score_type=score_type,
            score_value=score_value,
            raw_reference_score=payload.get("raw_reference_score"),
            contribution_payload=list(contributions),
            claim_state_hash=expected_claim_hash,
            config_fingerprint=str(payload.get("config_fingerprint") or ""),
        )
        expected_decision_id = "ADEC-" + stable_hash(
            {
                "target_id": str(payload.get("target_id") or ""),
                "as_of_date": str(payload.get("as_of_date") or ""),
                "input_fingerprint": str(payload.get("input_fingerprint") or ""),
                "score_fingerprint": str(payload.get("score_fingerprint") or ""),
                "stage": str(payload.get("canonical_stage") or ""),
            }
        )[:24]
        expected_trace_id = "ACTRACE-" + stable_hash(
            {
                "target_id": str(payload.get("target_id") or ""),
                "input_fingerprint": str(payload.get("input_fingerprint") or ""),
                "score_fingerprint": str(payload.get("score_fingerprint") or ""),
                "stage": str(payload.get("canonical_stage") or ""),
                "status": str(payload.get("decision_status") or ""),
            }
        )[:24]
        if (
            payload.get("claim_state_hash") != expected_claim_hash
            or payload.get("config_fingerprint") != expected_config_hash
            or payload.get("input_fingerprint") != expected_input_hash
            or payload.get("score_fingerprint") != expected_score_hash
            or payload.get("decision_id") != expected_decision_id
            or not isinstance(trace, Mapping)
            or trace.get("trace_id") != expected_trace_id
            or payload.get("schema_version") != ATOMIC_SCORE_STAGE_SCHEMA_VERSION
        ):
            critical["fingerprint_mismatch_concealed"] += 1
    return {
        "schema_version": "e2r_atomic_score_stage_audit_v1",
        "status": (
            "DETERMINISTIC_SCORE_STAGE_INTEGRITY_PASS"
            if payloads and sum(critical.values()) == 0
            else "DETERMINISTIC_SCORE_STAGE_INTEGRITY_FAIL"
        ),
        "decision_count": len(payloads),
        "score_type_counts": {
            item.value: sum(payload.get("score_type") == item.value for payload in payloads)
            for item in AtomicScoreType
        },
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": stable_hash(payloads),
        "production_runtime_ready": False,
    }


def audit_atomic_score_delta(
    before: AtomicStageDecision | Mapping[str, Any],
    after: AtomicStageDecision | Mapping[str, Any],
) -> Mapping[str, Any]:
    before_payload = before.to_dict() if isinstance(before, AtomicStageDecision) else dict(before)
    after_payload = after.to_dict() if isinstance(after, AtomicStageDecision) else dict(after)
    before_score = before_payload.get("score_value")
    after_score = after_payload.get("score_value")
    invalid_score_value = False
    if before_score is not None and after_score is not None:
        if any(
            not isinstance(item, (int, float))
            or isinstance(item, bool)
            or not math.isfinite(float(item))
            for item in (before_score, after_score)
        ):
            delta = None
            invalid_score_value = True
        else:
            delta = round(float(after_score) - float(before_score), 6)
    else:
        delta = None
    before_claim_state = stable_hash(list(before_payload.get("claims") or ()))
    after_claim_state = stable_hash(list(after_payload.get("claims") or ()))
    claim_changed = before_claim_state != after_claim_state
    before_config_state = stable_hash(
        {
            "scoring_config_version": before_payload.get("scoring_config_version"),
            "rules": list(before_payload.get("score_rules") or ()),
            "stage_config": before_payload.get("stage_config"),
        }
    )
    after_config_state = stable_hash(
        {
            "scoring_config_version": after_payload.get("scoring_config_version"),
            "rules": list(after_payload.get("score_rules") or ()),
            "stage_config": after_payload.get("stage_config"),
        }
    )
    config_changed = before_config_state != after_config_state
    contribution_changed = before_payload.get("contributions") != after_payload.get(
        "contributions"
    )
    unexplained = int(
        invalid_score_value
        or (
            delta not in (None, 0.0)
            and not claim_changed
            and not config_changed
        )
    )
    payload = {
        "before_decision_id": before_payload.get("decision_id"),
        "after_decision_id": after_payload.get("decision_id"),
        "score_delta": delta,
        "claim_state_changed": claim_changed,
        "config_changed": config_changed,
        "contribution_changed": contribution_changed,
        "unexplained_score_delta_count": unexplained,
    }
    return {
        "schema_version": "e2r_atomic_score_delta_audit_v1",
        "status": (
            "ATOMIC_SCORE_DELTA_EXPLAINED"
            if unexplained == 0
            else "ATOMIC_SCORE_DELTA_UNEXPLAINED"
        ),
        **payload,
        "result_hash": stable_hash(payload),
    }


def _payload_has_expected_stage_and_status(payload: Mapping[str, Any]) -> bool:
    try:
        score_type = AtomicScoreType(str(payload.get("score_type") or ""))
        scoring_scope = AtomicScoringScope(
            str(payload.get("scoring_scope") or "")
        )
        hard_break_state = _payload_expected_hard_break_state(payload)
        if hard_break_state is None:
            return False
        hard_break_claim_ids = hard_break_state[0]
        score_value = payload.get("score_value")
        raw_reference_score = payload.get("raw_reference_score")
        contributions = tuple(payload.get("contributions") or ())
        contribution_total = round(
            sum(
                float(item.get("points"))
                for item in contributions
                if isinstance(item, Mapping)
            ),
            6,
        )
        if len(contributions) != sum(
            isinstance(item, Mapping) for item in contributions
        ):
            return False
        if contributions and raw_reference_score is None:
            return False
        if not contributions and raw_reference_score is not None:
            return False
        if raw_reference_score is not None and round(
            float(raw_reference_score), 6
        ) != contribution_total:
            return False
        if score_value is not None and round(
            float(score_value), 6
        ) != contribution_total:
            return False
        if score_type == AtomicScoreType.FULL_E2R_100 and (
            scoring_scope != AtomicScoringScope.FULL_THESIS
            or payload.get("score_valid") is not True
            or payload.get("score_finalization_allowed") is not True
            or payload.get("provider_pending") is True
            or payload.get("source_pending") is True
            or payload.get("missing_conditions")
        ):
            return False
        if score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL and (
            scoring_scope != AtomicScoringScope.EVENT_EVIDENCE
            or payload.get("score_valid") is not True
            or payload.get("score_finalization_allowed") is not False
            or payload.get("provider_pending") is True
            or payload.get("source_pending") is True
        ):
            return False
        if score_type == AtomicScoreType.NO_SCORE and (
            score_value is not None
            or payload.get("score_valid") is not False
            or payload.get("score_finalization_allowed") is not False
        ):
            return False
        if hard_break_claim_ids:
            expected_stage = (
                CanonicalStage.STAGE_4C
                if payload.get("has_prior_live_thesis") is True
                else CanonicalStage.STAGE_3_RED
            )
            expected_status = AtomicDecisionStatus.RISK_REVIEW
        elif score_type == AtomicScoreType.NO_SCORE:
            expected_stage = CanonicalStage.STAGE_0
            expected_status = AtomicDecisionStatus.PENDING
        else:
            if (
                not isinstance(score_value, (int, float))
                or isinstance(score_value, bool)
            ):
                return False
            rules = tuple(
                AtomicScoreRule(**dict(item))
                for item in payload.get("score_rules") or ()
                if isinstance(item, Mapping)
            )
            assessments = tuple(
                AtomicPrimitiveAssessment(**dict(item))
                for item in payload.get("primitive_assessments") or ()
                if isinstance(item, Mapping)
            )
            rules_by_primitive = {item.primitive_id: item for item in rules}
            assessments_by_primitive = {
                item.primitive_id: item for item in assessments
            }
            if (
                not rules
                or len(rules_by_primitive) != len(rules)
                or set(rules_by_primitive) != set(assessments_by_primitive)
            ):
                return False
            stage_config_payload = payload.get("stage_config")
            if not isinstance(stage_config_payload, Mapping):
                return False
            expected_stage = _stage_for_score(
                float(score_value),
                assessments=assessments_by_primitive,
                rules=rules_by_primitive,
                config=AtomicStageConfig(**dict(stage_config_payload)),
                event_partial=(
                    score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL
                ),
            )
            expected_status = (
                AtomicDecisionStatus.EVENT_PARTIAL
                if score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL
                else AtomicDecisionStatus.FINAL
            )
        return (
            payload.get("canonical_stage") == expected_stage.value
            and payload.get("decision_status") == expected_status.value
        )
    except (TypeError, ValueError):
        return False


def _payload_expected_hard_break_state(
    payload: Mapping[str, Any],
) -> tuple[tuple[str, ...], tuple[str, ...]] | None:
    try:
        as_of = date.fromisoformat(str(payload.get("as_of_date") or ""))
        claim_by_id = {
            str(item.get("claim_id")): item
            for item in payload.get("claims") or ()
            if isinstance(item, Mapping) and item.get("claim_id")
        }
        accepted_claim_ids: list[str] = []
        rejected_signal_ids: list[str] = []
        signal_ids: set[str] = set()
        for signal in payload.get("hard_break_signals") or ():
            if not isinstance(signal, Mapping):
                return None
            signal_id = str(signal.get("signal_id") or "")
            claim_id = str(signal.get("claim_id") or "")
            if not signal_id or signal_id in signal_ids:
                return None
            signal_ids.add(signal_id)
            claim = claim_by_id.get(claim_id)
            observed_date = (
                date.fromisoformat(str(claim.get("observed_date") or ""))
                if claim is not None
                else None
            )
            valid = bool(
                claim
                and claim.get("target_id") == payload.get("target_id")
                and observed_date is not None
                and observed_date <= as_of
                and claim.get("target_direct") is True
                and claim.get("current_open") is True
                and claim.get("source_backed") is True
                and claim.get("material") is True
                and claim.get("polarity") == AtomicClaimPolarity.COUNTER.value
                and claim.get("historical_replay") is False
                and signal.get("unresolved") is True
            )
            if valid:
                if claim_id not in accepted_claim_ids:
                    accepted_claim_ids.append(claim_id)
            else:
                rejected_signal_ids.append(signal_id)
        return tuple(accepted_claim_ids), tuple(rejected_signal_ids)
    except (TypeError, ValueError):
        return None


def _payload_material_gap_ids(
    payload: Mapping[str, Any],
) -> set[str] | None:
    try:
        rules = tuple(
            AtomicScoreRule(**dict(item))
            for item in payload.get("score_rules") or ()
            if isinstance(item, Mapping)
        )
        assessments = tuple(
            AtomicPrimitiveAssessment(**dict(item))
            for item in payload.get("primitive_assessments") or ()
            if isinstance(item, Mapping)
        )
        rules_by_primitive = {item.primitive_id: item for item in rules}
        assessments_by_primitive = {
            item.primitive_id: item for item in assessments
        }
        if (
            not rules
            or len(rules_by_primitive) != len(rules)
            or set(rules_by_primitive) != set(assessments_by_primitive)
        ):
            return None
        contribution_primitives = {
            str(item.get("primitive_id"))
            for item in payload.get("contributions") or ()
            if isinstance(item, Mapping) and item.get("primitive_id")
        }
        return {
            primitive_id
            for primitive_id, rule in rules_by_primitive.items()
            if rule.material
            and (
                assessments_by_primitive[primitive_id].status
                != AtomicPrimitiveStatus.SATISFIED.value
                or primitive_id not in contribution_primitives
            )
        }
    except (TypeError, ValueError):
        return None


def _stage_for_score(
    score: float,
    *,
    assessments: Mapping[str, AtomicPrimitiveAssessment],
    rules: Mapping[str, AtomicScoreRule],
    config: AtomicStageConfig,
    event_partial: bool,
) -> CanonicalStage:
    if event_partial and score >= config.stage2_threshold:
        return CanonicalStage.STAGE_2
    if event_partial and score >= config.stage1_threshold:
        return CanonicalStage.STAGE_1
    if event_partial:
        return CanonicalStage.STAGE_0
    green_satisfied = all(
        not rule.green_required
        or assessments[primitive_id].status == AtomicPrimitiveStatus.SATISFIED.value
        for primitive_id, rule in rules.items()
    )
    if score >= config.green_threshold:
        return (
            CanonicalStage.STAGE_3_GREEN
            if green_satisfied
            else CanonicalStage.STAGE_3_YELLOW
        )
    if score >= config.yellow_threshold:
        return CanonicalStage.STAGE_3_YELLOW
    if score >= config.stage2_threshold:
        return CanonicalStage.STAGE_2
    if score >= config.stage1_threshold:
        return CanonicalStage.STAGE_1
    return CanonicalStage.STAGE_0


def _input_fingerprint_payload(
    *,
    target_id: str,
    as_of_date: str,
    scoring_scope: str,
    claims: Sequence[Mapping[str, Any]],
    primitive_assessments: Sequence[Mapping[str, Any]],
    hard_break_signals: Sequence[Mapping[str, Any]],
    provider_pending: bool,
    source_pending: bool,
    has_prior_live_thesis: bool,
    config_fingerprint: str,
) -> str:
    return stable_hash(
        {
            "target_id": target_id,
            "as_of_date": as_of_date,
            "scope": scoring_scope,
            "claims": list(claims),
            "primitive_assessments": list(primitive_assessments),
            "hard_break_signals": list(hard_break_signals),
            "provider_pending": provider_pending,
            "source_pending": source_pending,
            "has_prior_live_thesis": has_prior_live_thesis,
            "config_fingerprint": config_fingerprint,
        }
    )


def _score_fingerprint_payload(
    *,
    scoring_scope: str,
    score_type: str,
    score_value: float | None,
    raw_reference_score: float | None,
    contribution_payload: Sequence[Mapping[str, Any]],
    claim_state_hash: str,
    config_fingerprint: str,
) -> str:
    return stable_hash(
        {
            "scoring_scope": scoring_scope,
            "score_type": score_type,
            "score_value": score_value,
            "raw_reference_score": raw_reference_score,
            "contributions": list(contribution_payload),
            "claim_state_hash": claim_state_hash,
            "config_fingerprint": config_fingerprint,
        }
    )


def _require_unique_text(
    values: Sequence[str],
    *,
    context: str,
    required: bool = True,
) -> None:
    if required and not values:
        raise ValueError(f"{context} cannot be empty")
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains empty text")
    if len(values) != len(set(values)):
        raise ValueError(f"{context} contains duplicate values")


__all__ = [
    "ATOMIC_SCORE_STAGE_SCHEMA_VERSION",
    "AtomicClaimPolarity",
    "AtomicDecisionStatus",
    "AtomicHardBreakSignal",
    "AtomicPrimitiveAssessment",
    "AtomicPrimitiveStatus",
    "AtomicScoreClaim",
    "AtomicScoreContribution",
    "AtomicScoreRule",
    "AtomicScoreType",
    "AtomicScoringInput",
    "AtomicScoringScope",
    "AtomicStageConfig",
    "AtomicStageCourtTrace",
    "AtomicStageDecision",
    "CanonicalStage",
    "adapt_claim_ledger_event_to_atomic_claim",
    "audit_atomic_score_delta",
    "audit_atomic_stage_decisions",
    "decide_atomic_score_stage",
]
