"""Stable component catalog shared by every archetype scoring contract."""

from e2r.calibration.archetype_weight_profile import SCORE_COMPONENT_KEYS


CANONICAL_COMPONENT_IDS = tuple(SCORE_COMPONENT_KEYS)


def component_ids() -> tuple[str, ...]:
    return CANONICAL_COMPONENT_IDS


__all__ = ["CANONICAL_COMPONENT_IDS", "component_ids"]
