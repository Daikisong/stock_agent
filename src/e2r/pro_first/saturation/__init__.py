"""Deterministic Pro V2 research-saturation engine."""

from .adjudicator import ResearchSaturationAdjudicator
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
from .question_closure import compile_question_closure_decision
from .route_adequacy import evaluate_route_adequacy

__all__ = [
    "AvailabilityDecision",
    "DeterministicQuestionBound",
    "NONTERMINAL_QUESTION_STATUSES",
    "NoNewRouteConfirmation",
    "QuestionClosureDecision",
    "ResearchSaturationAdjudicator",
    "ResearchSaturationReceipt",
    "RouteAdequacyDecision",
    "SemanticFixpointDecision",
    "TERMINAL_QUESTION_STATUSES",
    "adjudicate_availability",
    "compile_question_closure_decision",
    "compile_saturation_audit",
    "evaluate_route_adequacy",
    "evaluate_semantic_no_new_route_fixpoint",
]
