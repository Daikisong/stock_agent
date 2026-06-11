"""Context checks for one-off demand and shortage evidence."""

from __future__ import annotations

import re


_SENTENCE_RE = re.compile(r"[\n\r.!?。]+")

_EXPLICIT_ONE_OFF_DEMAND_PATTERNS = (
    "일회성 수요",
    "일시적 수요",
    "한시적 수요",
    "일회성 특수",
    "일시적 특수",
    "한시적 특수",
    "코로나 특수",
    "팬데믹 특수",
    "one-off demand",
    "one off demand",
    "temporary demand",
    "temporary shortage",
    "event-driven demand",
    "event demand",
    "pandemic demand",
    "covid demand",
)

_PANDEMIC_EVENT_TOKENS = (
    "팬데믹",
    "코로나",
    "코로나19",
    "진단키트",
    "pandemic",
    "covid",
    "covid-19",
    "test kit",
    "diagnostic kit",
)

_DEMAND_SURGE_TOKENS = (
    "수요",
    "특수",
    "급증",
    "폭발",
    "서프라이즈",
    "매출 증가",
    "매출과 eps",
    "eps",
    "demand",
    "surge",
    "spike",
    "boom",
    "sales growth",
    "revenue growth",
    "eps growth",
)


def has_one_off_shortage_context(text: str) -> bool:
    """Return true only when one-off wording describes demand/shortage risk."""

    if not text:
        return False
    lowered = text.lower()
    if any(pattern in lowered for pattern in _EXPLICIT_ONE_OFF_DEMAND_PATTERNS):
        return True
    for sentence in _sentences(text):
        sentence_lowered = sentence.lower()
        if not any(token in sentence_lowered for token in _PANDEMIC_EVENT_TOKENS):
            continue
        if any(token in sentence_lowered for token in _DEMAND_SURGE_TOKENS):
            return True
    return False


def _sentences(text: str) -> tuple[str, ...]:
    return tuple(part.strip() for part in _SENTENCE_RE.split(text) if part.strip())
