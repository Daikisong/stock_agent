"""Deterministic Pro V2 research-saturation engine."""

from .adjudicator import ResearchSaturationAdjudicator
from .confirmation_compiler import (
    FixpointConfirmationCompilation,
    RouteSnapshotBindingCompilation,
    compile_fixpoint_confirmations,
    compile_route_snapshot_bindings,
)
from .audit import compile_saturation_audit
from .availability import adjudicate_availability
from .fixpoint import (
    NoNewRouteConfirmation,
    SemanticFixpointDecision,
    evaluate_semantic_no_new_route_fixpoint,
)
from .models import (
    AvailabilityDecision,
    DeterministicQuestionBound,
    NONTERMINAL_QUESTION_STATUSES,
    QuestionClosureDecision,
    ResearchSaturationReceipt,
    RouteAdequacyDecision,
    TERMINAL_QUESTION_STATUSES,
)
from .snapshots import VerifiedResearchSnapshot, compile_verified_research_snapshot
from .question_closure import compile_question_closure_decision
from .route_adequacy import evaluate_route_adequacy

__all__ = [
    "FixpointConfirmationCompilation",
    "AvailabilityDecision",
    "DeterministicQuestionBound",
    "NONTERMINAL_QUESTION_STATUSES",
    "NoNewRouteConfirmation",
    "QuestionClosureDecision",
    "ResearchSaturationAdjudicator",
    "ResearchSaturationReceipt",
    "RouteSnapshotBindingCompilation",
    "VerifiedResearchSnapshot",
    "RouteAdequacyDecision",
    "SemanticFixpointDecision",
    "TERMINAL_QUESTION_STATUSES",
    "adjudicate_availability",
    "compile_question_closure_decision",
    "compile_fixpoint_confirmations",
    "compile_route_snapshot_bindings",
    "compile_saturation_audit",
    "compile_verified_research_snapshot",
    "evaluate_route_adequacy",
    "evaluate_semantic_no_new_route_fixpoint",
]
