"""Bounded source acquisition for Research Brain v3 shadow runs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_os import AnchorType, EvidenceAnchor, EvidenceDocument, SourceType
from e2r.research_brain.schemas import SourceTask
from e2r.research_brain.v2_schemas import CandidateEventV2


@dataclass(frozen=True)
class SourceAcquisitionResultV3:
    status: str
    documents: tuple[EvidenceDocument, ...] = ()
    anchors: tuple[EvidenceAnchor, ...] = ()
    provider_errors: tuple[str, ...] = ()
    not_eligible_reasons: tuple[str, ...] = ()
    budget_used: Mapping[str, int] | None = None
    stop_reason: str = ""
    document_text_by_id: Mapping[str, str] | None = None


class SourceAcquisitionRunnerV3:
    """Source acquisition adapter for frozen/snapshot/live-capable shadow mode.

    The default implementation does not scrape the web. It turns bounded
    official/snapshot event payloads into EvidenceDocument/EvidenceAnchor rows.
    A live provider can be added behind this interface without changing the
    Evidence OS bridge.
    """

    def __init__(self, *, mode: str = "snapshot") -> None:
        self.mode = mode

    def acquire(self, *, event: CandidateEventV2, task: SourceTask, as_of_date: date) -> SourceAcquisitionResultV3:
        policy_rejection = _policy_rejection(task)
        if policy_rejection:
            return SourceAcquisitionResultV3(
                status="REJECTED_BY_POLICY",
                provider_errors=policy_rejection,
                not_eligible_reasons=policy_rejection,
                budget_used={"queries": 0, "candidates": 0, "fetches": 0},
                stop_reason="source_task_rejected_by_v3_policy",
            )
        if self.mode == "live":
            return SourceAcquisitionResultV3(
                status="PROVIDER_FAILED",
                provider_errors=("live_source_acquisition_provider_not_configured",),
                budget_used={"queries": 1, "candidates": 0, "fetches": 0},
                stop_reason="live_provider_missing",
            )
        text = _document_text(event=event, task=task)
        if not text.strip():
            return SourceAcquisitionResultV3(
                status="NO_EVIDENCE_FOUND",
                budget_used={"queries": 1, "candidates": 0, "fetches": 0},
                stop_reason="empty_snapshot_source_payload",
            )
        published = _date_from_text(event.event_date) or as_of_date
        if published > as_of_date:
            return SourceAcquisitionResultV3(
                status="NO_EVIDENCE_FOUND",
                provider_errors=("future_source_rejected",),
                not_eligible_reasons=("future_source_rejected",),
                budget_used={"queries": 1, "candidates": 1, "fetches": 0},
                stop_reason="future_source_rejected",
            )
        source_family = _selected_source_family(event=event, task=task)
        document = EvidenceDocument.from_text(
            text=text,
            canonical_url=_canonical_source_url(event=event, task=task, source_family=source_family),
            source_type=_source_type(source_family),
            source_name=source_family,
            published_at=published,
            available_at=published,
            fetched_at=as_of_date,
            parser_version="research_brain_v3_snapshot_source_acquisition",
            source_lineage_id=f"{source_family}:{event.source_id}",
            source_proxy_only=False,
        )
        anchor = _anchor_for_document(document=document, document_text=text, task=task, source_family=source_family)
        return SourceAcquisitionResultV3(
            status="PARSED",
            documents=(document,),
            anchors=(anchor,),
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
            stop_reason="snapshot_source_anchor_created",
            document_text_by_id={document.document_id: text},
        )


def _policy_rejection(task: SourceTask) -> tuple[str, ...]:
    reasons: list[str] = []
    for field_name in ("max_queries", "max_candidates", "max_fetches"):
        value = getattr(task, field_name)
        if value is None or int(value) <= 0:
            reasons.append(f"unbounded_or_invalid_{field_name}")
    if "unbounded_general_search" not in tuple(task.forbidden_source_classes):
        reasons.append("missing_unbounded_general_search_guard")
    if task.general_search_allowed and _is_official_solvable_gap(task.primitive_gap):
        reasons.append("official_solvable_gap_sent_to_general_web")
    if _is_fcf_gap(task.primitive_gap):
        source_names = {item.lower() for item in (*task.preferred_source_classes, *task.fallback_source_classes)}
        if source_names & {"generalweb", "web", "trustednews", "newsonly"}:
            reasons.append("fcf_gap_sent_to_news_or_general_web")
    return tuple(dict.fromkeys(reasons))


def _document_text(*, event: CandidateEventV2, task: SourceTask) -> str:
    payload = {
        "symbol": event.symbol,
        "company_name": event.company_name,
        "event_date": event.event_date,
        "event_type": event.event_type,
        "primitive_gap": task.primitive_gap,
        "event_summary": event.event_summary,
        "raw_reason_codes": list(event.raw_reason_codes),
        "source_family": event.source_family,
        "source_id": event.source_id,
        "structured_payload": dict(event.structured_payload),
    }
    return (
        f"{payload['company_name']}({payload['symbol']}) {payload['event_date']} "
        f"{payload['event_type']} source evidence for {payload['primitive_gap']}: "
        f"{payload['event_summary']} | reason_codes={payload['raw_reason_codes']} | "
        f"source={payload['source_family']}:{payload['source_id']}"
    )


def _selected_source_family(*, event: CandidateEventV2, task: SourceTask) -> str:
    official = {"DART", "KIND", "KRX", "IR", "Official", "CompanyGuide"}
    for source in task.preferred_source_classes:
        if source in official:
            return source
    return event.source_family or "Snapshot"


def _canonical_source_url(*, event: CandidateEventV2, task: SourceTask, source_family: str) -> str:
    if source_family in {"DART", "KIND", "KRX", "CompanyGuide"}:
        return f"api://{source_family}/{event.source_id}/{task.task_id}"
    if source_family in {"IR", "Official"}:
        return f"snapshot://{source_family}/{event.source_id}/{task.task_id}"
    return f"snapshot://{event.source_family}/{event.source_id}/{task.task_id}"


def _source_type(source_family: str) -> SourceType:
    if source_family in {"DART", "KIND", "KRX"}:
        return SourceType.FILING
    if source_family == "IR":
        return SourceType.IR
    if source_family == "CompanyGuide":
        return SourceType.API
    if "News" in source_family:
        return SourceType.NEWS
    if "Report" in source_family:
        return SourceType.RESEARCH_REPORT
    return SourceType.API


def _anchor_for_document(
    *,
    document: EvidenceDocument,
    document_text: str,
    task: SourceTask,
    source_family: str,
) -> EvidenceAnchor:
    if source_family in {"DART", "KIND", "KRX", "CompanyGuide"}:
        return EvidenceAnchor.structured(
            document=document,
            anchor_type=AnchorType.API_RECORD,
            locator=f"record:{task.primitive_gap}",
            normalized_value={
                "primitive_gap": task.primitive_gap,
                "document_id": document.document_id,
                "source_name": source_family,
            },
            exact_text=document_text[:500],
            anchor_verified=True,
        )
    return EvidenceAnchor.text_span(document=document, document_text=document_text, exact_text=document_text[:500])


def _date_from_text(value: str) -> date | None:
    try:
        return datetime.fromisoformat(str(value)[:10]).date()
    except ValueError:
        return None


def _is_official_solvable_gap(primitive: str) -> bool:
    lower = primitive.lower()
    return any(token in lower for token in ("contract", "backlog", "cash", "fcf", "revision"))


def _is_fcf_gap(primitive: str) -> bool:
    lower = primitive.lower()
    return any(token in lower for token in ("cash", "fcf", "revision"))


__all__ = ["SourceAcquisitionResultV3", "SourceAcquisitionRunnerV3"]
