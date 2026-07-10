"""Recipe-aware document type, freshness, and section selection."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date
from typing import Mapping

from e2r.research_brain.intelligence_schema import EvidenceRecipe
from e2r.research_brain.planning.source_task import QuestionSourceTask
from e2r.research_brain.runtime.source_acquisition import (
    AcquiredDocument,
    AcquisitionMode,
    DocumentCandidate,
    DocumentRejectionReason,
    DocumentSelection,
    SelectedDocumentSection,
)


DOCUMENT_SELECTOR_VERSION = "e2r_recipe_document_selector_v1"


_SOURCE_FAMILY_ALIASES = {
    "IR": "IssuerIR",
    "BrokerPDF": "ResearchReport",
    "BrokerReport": "ResearchReport",
    "News": "TrustedNews",
    "OfficialDisclosure": "DART",
}
_DISCOVERY_ONLY_SOURCE_FAMILIES = frozenset(
    {
        "Naver",
        "NaverNews",
        "NaverSearch",
        "GeneralWeb",
        "GeneralWebSearch",
        "TrustedNewsSearch",
        "WebSearch",
    }
)
_DOCUMENT_TYPES_BY_SOURCE_FAMILY = {
    "DART": {"filing", "earnings_release", "structured_record"},
    "KIND": {"filing", "structured_record"},
    "KRX": {"filing", "structured_record"},
    "IssuerIR": {
        "investor_presentation",
        "earnings_release",
        "filing",
        "structured_record",
    },
    "IssuerNewsroom": {"full_article", "press_release"},
    "CompanyEarningsCall": {
        "earnings_call_transcript",
        "transcript",
    },
    "CompanyGuide": {"structured_record", "financial_statement"},
    "SEC": {"filing", "structured_record"},
    "Regulator": {"filing", "registry_record", "structured_record"},
    "ClinicalTrialRegistry": {"registry_record", "structured_record"},
    "CustomerOfficial": {"press_release", "full_article", "filing"},
    "CustomerNewsroom": {"press_release", "full_article"},
    "PeerReviewedPublication": {"peer_reviewed_article", "full_article"},
    "IndustryData": {"industry_dataset", "structured_record"},
    "TrustedNews": {"full_article"},
    "ResearchReport": {"research_report"},
}
_TOKEN_RE = re.compile(r"[0-9A-Za-z가-힣]+")
_STOPWORDS = {
    "and",
    "the",
    "with",
    "from",
    "for",
    "및",
    "관련",
    "현황",
}


@dataclass(frozen=True)
class RecipeDocumentSelector:
    recipes_by_id: Mapping[str, EvidenceRecipe]
    selector_version: str = DOCUMENT_SELECTOR_VERSION

    def __post_init__(self) -> None:
        if not self.recipes_by_id:
            raise ValueError("recipe document selector requires recipes")
        if any(
            recipe_id != recipe.recipe_id
            for recipe_id, recipe in self.recipes_by_id.items()
        ):
            raise ValueError("recipe document selector mapping identity mismatch")

    def select(
        self,
        *,
        task: QuestionSourceTask,
        candidate: DocumentCandidate,
        mode: AcquisitionMode,
        as_of_date: date,
    ) -> DocumentSelection:
        recipe = self.recipes_by_id.get(task.recipe_id)
        if recipe is None or recipe.recipe_id != candidate.recipe_id:
            return _rejected(
                DocumentRejectionReason.TASK_RECIPE_LINK_MISMATCH,
                "selector has no matching executable recipe",
            )
        source_family = _normalize_source_family(candidate.source_family)
        if source_family in _DISCOVERY_ONLY_SOURCE_FAMILIES:
            return _rejected(
                DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH,
                "search/discovery provider family is not an original document source",
            )
        allowed_sources = {
            *task.source_route.preferred_source_families,
            *task.source_route.fallback_source_families,
            *recipe.preferred_source_families,
            *recipe.discovery_sources,
        }
        normalized_allowed_sources = {
            _normalize_source_family(item) for item in allowed_sources
        }
        if source_family not in normalized_allowed_sources:
            return _rejected(
                DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH,
                f"source family {source_family} is outside task/recipe route",
            )
        task_document_types = set(task.source_route.preferred_document_types)
        recipe_document_types = set(recipe.preferred_document_types)
        if candidate.document_type not in task_document_types:
            return _rejected(
                DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH,
                (
                    f"document type {candidate.document_type} is outside the "
                    "QuestionSourceTask document contract"
                ),
            )
        if candidate.document_type not in recipe_document_types:
            return _rejected(
                DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH,
                (
                    f"document type {candidate.document_type} is not one of "
                    f"{sorted(recipe.preferred_document_types)}"
                ),
            )
        compatible_types = _DOCUMENT_TYPES_BY_SOURCE_FAMILY.get(source_family)
        if compatible_types is not None and candidate.document_type not in compatible_types:
            return _rejected(
                DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH,
                f"{source_family} cannot produce {candidate.document_type}",
            )
        published_at = date.fromisoformat(str(candidate.published_at))
        if (
            recipe.freshness_max_age_days is not None
            and (as_of_date - published_at).days > recipe.freshness_max_age_days
        ):
            return _rejected(
                DocumentRejectionReason.STALE_DOCUMENT,
                (
                    f"document age {(as_of_date - published_at).days}d exceeds "
                    f"recipe maximum {recipe.freshness_max_age_days}d"
                ),
            )
        linked_sections = tuple(
            section
            for section in task.source_route.preferred_sections
            if section in set(recipe.preferred_sections)
        )
        if not linked_sections:
            return _rejected(
                DocumentRejectionReason.TASK_RECIPE_LINK_MISMATCH,
                "QuestionSourceTask sections do not intersect the linked recipe",
            )
        selected_sections = select_recipe_sections(
            text=str(candidate.full_text),
            preferred_sections=linked_sections,
        )
        if not selected_sections:
            return _rejected(
                DocumentRejectionReason.RECIPE_SECTION_MISSING,
                "fetched full text contains no recipe-relevant section",
            )
        full_text = str(candidate.full_text)
        content_hash = hashlib.sha256(full_text.encode("utf-8")).hexdigest()
        document_id = _stable_id(
            "ADOC",
            {
                "task_id": task.task_id,
                "recipe_id": task.recipe_id,
                "candidate_id": candidate.candidate_id,
                "content_hash": content_hash,
                "selected_section_ids": [
                    section.section_id for section in selected_sections
                ],
            },
        )
        document = AcquiredDocument(
            document_id=document_id,
            candidate_id=candidate.candidate_id,
            task_id=task.task_id,
            recipe_id=task.recipe_id,
            mode=mode.value,
            provider_name=candidate.provider_name,
            source_family=source_family,
            document_type=candidate.document_type,
            title=candidate.title,
            canonical_url=candidate.canonical_url,
            original_source_url=str(candidate.original_source_url),
            published_at=str(candidate.published_at),
            available_at=str(candidate.available_at),
            fetched_at=candidate.fetched_at,
            full_text=full_text,
            content_hash=content_hash,
            content_type=candidate.content_type,
            discovery_source_family=candidate.discovery_source_family,
            selected_sections=selected_sections,
            counts_as_live=candidate.counts_as_live,
            historical_replay=mode == AcquisitionMode.HISTORICAL_REPLAY,
            source_repair_only=mode == AcquisitionMode.SOURCE_REPAIR_BACKFILL,
            controlled_smoke=mode == AcquisitionMode.CONTROLLED_SMOKE,
            original_source_verified=candidate.original_source_verified,
            source_document_compatible=True,
            target_relation=candidate.target_relation,
            source_lineage_id=(
                f"{candidate.source_lineage_id}|selector:{self.selector_version}"
            ),
        )
        return DocumentSelection(
            document=document,
            rejection_reason=None,
            rejection_detail=None,
        )


def select_recipe_sections(
    *,
    text: str,
    preferred_sections: tuple[str, ...],
) -> tuple[SelectedDocumentSection, ...]:
    clean_text = str(text or "").strip()
    if not clean_text or not preferred_sections:
        return ()
    selected: list[SelectedDocumentSection] = []
    seen_hashes: dict[str, int] = {}
    for recipe_section in preferred_sections:
        match = _section_match(clean_text, recipe_section)
        if match is None:
            continue
        section_text = _window_around(clean_text, match)
        content_hash = hashlib.sha256(section_text.encode("utf-8")).hexdigest()
        existing_index = seen_hashes.get(content_hash)
        if existing_index is not None:
            existing = selected[existing_index]
            selected[existing_index] = SelectedDocumentSection(
                section_id=existing.section_id,
                section_name=existing.section_name,
                text=existing.text,
                content_hash=existing.content_hash,
                matched_recipe_sections=tuple(
                    dict.fromkeys(
                        (*existing.matched_recipe_sections, recipe_section)
                    )
                ),
            )
            continue
        section_id = _stable_id(
            "DSEC",
            {
                "recipe_section": recipe_section,
                "content_hash": content_hash,
            },
        )
        seen_hashes[content_hash] = len(selected)
        selected.append(
            SelectedDocumentSection(
                section_id=section_id,
                section_name=recipe_section,
                text=section_text,
                content_hash=content_hash,
                matched_recipe_sections=(recipe_section,),
            )
        )
    return tuple(selected)


def _section_match(text: str, recipe_section: str) -> tuple[int, int] | None:
    lowered = text.casefold()
    phrase = recipe_section.casefold().strip()
    direct = lowered.find(phrase)
    if direct >= 0:
        return direct, direct + len(phrase)
    tokens = [
        token.casefold()
        for token in _TOKEN_RE.findall(recipe_section)
        if len(token) >= 2 and token.casefold() not in _STOPWORDS
    ]
    if not tokens:
        return None
    positions = [lowered.find(token) for token in tokens]
    present = [position for position in positions if position >= 0]
    required_hits = 1 if len(tokens) == 1 else max(2, (len(tokens) + 1) // 2)
    if len(present) < required_hits:
        return None
    start = min(present)
    end = max(
        position + len(token)
        for position, token in zip(positions, tokens)
        if position >= 0
    )
    return start, end


def _window_around(text: str, match: tuple[int, int], radius: int = 700) -> str:
    start, end = match
    window_start = max(0, start - radius)
    window_end = min(len(text), end + radius)
    prefix_break = text.rfind("\n", window_start, start)
    suffix_break = text.find("\n", end, window_end)
    if prefix_break >= 0:
        window_start = prefix_break + 1
    if suffix_break >= 0:
        window_end = suffix_break
    return text[window_start:window_end].strip()


def _normalize_source_family(value: str) -> str:
    clean = str(value).strip()
    return _SOURCE_FAMILY_ALIASES.get(clean, clean)


def _rejected(
    reason: DocumentRejectionReason,
    detail: str,
) -> DocumentSelection:
    return DocumentSelection(
        document=None,
        rejection_reason=reason.value,
        rejection_detail=detail,
    )


def _stable_id(prefix: str, payload: Mapping[str, object]) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    digest = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
    return f"{prefix}-{digest[:24]}"


__all__ = [
    "DOCUMENT_SELECTOR_VERSION",
    "RecipeDocumentSelector",
    "select_recipe_sections",
]
