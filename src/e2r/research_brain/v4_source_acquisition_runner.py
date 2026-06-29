"""Real-source acquisition layer for Research Brain v4 production shadow."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.agentic.evidence_os import AnchorType, EvidenceAnchor, EvidenceDocument, SourceType
from e2r.research_brain.schemas import SourceTask
from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v4_schemas import SourceAcquisitionModeV4, SourceAcquisitionResultV4


@dataclass(frozen=True)
class StoredSourceSnapshot:
    source_class: str
    provider_name: str
    source_path: Path
    symbol: str
    company_name: str
    published_at: date | None
    text: str
    canonical_url: str
    anchor_type: AnchorType
    normalized_value: Mapping[str, Any]


class SourceAcquisitionRunnerV4:
    """Acquire real source snapshots or live official-provider results.

    The default ``frozen_real_source_snapshot`` mode reads already stored source
    snapshots. That is intentionally different from v3: a candidate event
    summary is never converted into a score-eligible document.
    """

    def __init__(
        self,
        *,
        mode: str = SourceAcquisitionModeV4.FROZEN_REAL_SOURCE_SNAPSHOT.value,
        repo_root: str | Path = ".",
    ) -> None:
        self.mode = SourceAcquisitionModeV4(mode)
        self.repo_root = Path(repo_root)

    def acquire(self, *, event: CandidateEventV2, task: SourceTask, as_of_date: date) -> SourceAcquisitionResultV4:
        policy_rejection = _policy_rejection(task)
        if policy_rejection:
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class="policy",
                provider_name="v4_policy_validator",
                status="REJECTED_BY_POLICY",
                provider_errors=policy_rejection,
                budget_used={"queries": 0, "candidates": 0, "fetches": 0},
                stop_reason="source_task_rejected_by_v4_policy",
            )
        if self.mode == SourceAcquisitionModeV4.TEST_FAKE:
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class="test_fake",
                provider_name="test_fake_source_provider",
                status="PROVIDER_FAILED",
                provider_errors=("test_fake_source_not_score_eligible",),
                budget_used={"queries": 1, "candidates": 0, "fetches": 0},
                stop_reason="test_fake_source_never_scores",
            )
        snapshots = tuple(
            sorted(
                self._candidate_snapshots(event=event, task=task, as_of_date=as_of_date),
                key=lambda item: _snapshot_relevance(task.primitive_gap, item.text),
                reverse=True,
            )
        )
        if not snapshots:
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class=_first_source_class(task),
                provider_name=f"{self.mode.value}_provider",
                status="PROVIDER_FAILED" if self.mode != SourceAcquisitionModeV4.FROZEN_REAL_SOURCE_SNAPSHOT else "NO_EVIDENCE_FOUND",
                provider_errors=()
                if self.mode == SourceAcquisitionModeV4.FROZEN_REAL_SOURCE_SNAPSHOT
                else (f"{self.mode.value}_provider_has_no_matching_document",),
                budget_used={"queries": 1, "candidates": 0, "fetches": 0},
                stop_reason="no_matching_real_source_snapshot",
            )
        documents: list[EvidenceDocument] = []
        anchors: list[EvidenceAnchor] = []
        text_by_id: dict[str, str] = {}
        for snapshot in snapshots[: task.max_fetches]:
            document = EvidenceDocument.from_text(
                text=snapshot.text,
                canonical_url=snapshot.canonical_url,
                source_type=_source_type(snapshot.source_class),
                source_name=snapshot.provider_name,
                published_at=snapshot.published_at,
                available_at=snapshot.published_at,
                fetched_at=as_of_date,
                parser_version="research_brain_v4_real_source_snapshot",
                source_lineage_id=f"{snapshot.source_class}:{snapshot.source_path}",
                source_proxy_only=False,
            )
            anchor = _anchor_for_snapshot(document=document, snapshot=snapshot)
            documents.append(document)
            anchors.append(anchor)
            text_by_id[document.document_id] = snapshot.text
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class=_first_source_class(task),
            provider_name="stored_real_source_snapshot_provider",
            status="PARSED",
            documents=tuple(documents),
            anchors=tuple(anchors),
            document_text_by_id=text_by_id,
            fetched_document_ids=tuple(document.document_id for document in documents),
            document_urls=tuple(document.canonical_url or "" for document in documents),
            document_hashes=tuple(document.content_hash for document in documents),
            anchor_ids=tuple(anchor.anchor_id for anchor in anchors),
            budget_used={"queries": 1, "candidates": len(snapshots), "fetches": len(documents)},
            stop_reason="stored_real_source_snapshot_parsed",
        )

    def _candidate_snapshots(
        self,
        *,
        event: CandidateEventV2,
        task: SourceTask,
        as_of_date: date,
    ) -> Iterable[StoredSourceSnapshot]:
        source_classes = tuple(dict.fromkeys((*task.preferred_source_classes, *task.fallback_source_classes)))
        for source_class in source_classes:
            normalized = _normalize_source_class(source_class)
            if normalized == "CompanyGuide":
                yield from _company_guide_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized == "DART":
                yield from _dart_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized in {"KIND", "KRX"}:
                if normalized == "KIND":
                    yield from _kind_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
                else:
                    yield from _krx_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized in {"IR", "IssuerOfficial", "Official"}:
                yield from _issuer_official_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized in {"TrustedNews", "News"}:
                yield from _trusted_news_snapshots(self.repo_root, event=event, as_of_date=as_of_date)


def _company_guide_snapshots(
    repo_root: Path,
    *,
    event: CandidateEventV2,
    as_of_date: date,
) -> Iterable[StoredSourceSnapshot]:
    cache_root = repo_root / "data/cache/company_guide"
    for recent_path in sorted(cache_root.glob(f"*/{event.symbol}_recent_reports.json"), reverse=True):
        payload = _load_json(recent_path)
        if not isinstance(payload, Mapping):
            continue
        for row in payload.get("lists") or ():
            if not isinstance(row, Mapping):
                continue
            row_date = _yy_mm_dd_date(row.get("ANL_DT"), as_of_date)
            if row_date is None or row_date > as_of_date:
                continue
            comment = _strip_html(str(row.get("COMMENT") or row.get("COMMENT2") or ""))
            title = str(row.get("RPT_TITLE") or "")
            company = str(row.get("CMP_NM_KOR") or event.company_name)
            text = "\n".join(
                item
                for item in (
                    f"CompanyGuide report {row.get('RPT_ID')} {row_date.isoformat()}",
                    f"{company}({event.symbol})",
                    title,
                    comment,
                    f"EPS_ACTION_TYP_NM={row.get('EPS_ACTION_TYP_NM')}",
                    f"PRC_ACTION_TYP_NM={row.get('PRC_ACTION_TYP_NM')}",
                    f"TARGET_PRC={row.get('TARGET_PRC')}",
                    f"EPS={row.get('EPS')}",
                    f"BROKER={row.get('BRK_NM_KOR') or row.get('BRK_NM_SHORT_KOR')}",
                )
                if str(item).strip()
            )
            yield StoredSourceSnapshot(
                source_class="CompanyGuide",
                provider_name="CompanyGuideRecentReportsSnapshot",
                source_path=recent_path,
                symbol=event.symbol,
                company_name=company,
                published_at=row_date,
                text=text,
                canonical_url=f"snapshot://company_guide/{recent_path.parent.name}/{event.symbol}/recent_reports#{row.get('RPT_ID')}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={
                    "symbol": event.symbol,
                    "company_name": company,
                    "provider": "CompanyGuide",
                    "row": dict(row),
                    "snapshot_path": str(recent_path),
                },
            )
    for snapshot_path in sorted(cache_root.glob(f"*/{event.symbol}_snapshot.html"), reverse=True):
        text = snapshot_path.read_text(encoding="utf-8", errors="ignore")
        published = _snapshot_date_from_text(text) or _date_from_path(snapshot_path) or as_of_date
        if published > as_of_date:
            continue
        yield StoredSourceSnapshot(
            source_class="CompanyGuide",
            provider_name="CompanyGuideSnapshotHtml",
            source_path=snapshot_path,
            symbol=event.symbol,
            company_name=event.company_name,
            published_at=published,
            text=text[:80_000],
            canonical_url=f"snapshot://company_guide/{snapshot_path.parent.name}/{event.symbol}/snapshot",
            anchor_type=AnchorType.TEXT_SPAN,
            normalized_value={
                "symbol": event.symbol,
                "company_name": event.company_name,
                "provider": "CompanyGuide",
                "snapshot_path": str(snapshot_path),
            },
        )


def _dart_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    paths = (
        *(repo_root / "fixtures/historical").glob("disclosures.csv"),
        *(repo_root / "data/raw/opendart/disclosures").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/opendart/disclosures").glob("*.csv"),
    )
    for path in sorted(paths):
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            published = _date_from_any(row.get("published_at") or row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            raw_text = str(row.get("raw_text") or row.get("title") or "")
            text = _row_text("OpenDART", row, raw_text=raw_text, symbol=event.symbol, company_name=event.company_name)
            yield StoredSourceSnapshot(
                source_class="DART",
                provider_name="OpenDARTStoredDisclosure",
                source_path=path,
                symbol=event.symbol,
                company_name=event.company_name,
                published_at=published,
                text=text,
                canonical_url=f"snapshot://opendart/{event.symbol}/{row.get('rcept_no') or path.name}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "OpenDART", "row": dict(row)},
            )


def _kind_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    paths = (
        *(repo_root / "data/raw/kind/risk_flags").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/kind/risk_flags").glob("*.csv"),
    )
    for path in sorted(paths):
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            published = _date_from_any(row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            text = _row_text("KIND", row, raw_text=str(row.get("title") or ""), symbol=event.symbol, company_name=event.company_name)
            yield StoredSourceSnapshot(
                source_class="KIND",
                provider_name="KINDStoredRiskFlags",
                source_path=path,
                symbol=event.symbol,
                company_name=str(row.get("company_name") or event.company_name),
                published_at=published,
                text=text,
                canonical_url=f"snapshot://kind/{event.symbol}/{published.isoformat()}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "KIND", "row": dict(row)},
            )


def _krx_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    instrument_paths = (
        *(repo_root / "data/raw/krx/instruments").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/krx/instruments").glob("*.csv"),
        repo_root / "fixtures/historical/instruments.csv",
    )
    for path in sorted(path for path in instrument_paths if path.exists()):
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            listed = _date_from_any(row.get("listed_date")) or as_of_date
            if listed > as_of_date:
                continue
            text = _row_text("KRX", row, raw_text=str(row.get("name") or event.company_name), symbol=event.symbol, company_name=event.company_name)
            yield StoredSourceSnapshot(
                source_class="KRX",
                provider_name="KRXStoredInstrumentStatus",
                source_path=path,
                symbol=event.symbol,
                company_name=str(row.get("name") or event.company_name),
                published_at=as_of_date,
                text=text,
                canonical_url=f"snapshot://krx/instruments/{path.name}#{event.symbol}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "KRX", "row": dict(row)},
            )
    price_paths = (
        *(repo_root / "data/raw/krx/prices").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/krx/prices").glob("*.csv"),
        repo_root / "fixtures/historical/prices.csv",
    )
    for path in sorted(path for path in price_paths if path.exists()):
        latest: Mapping[str, Any] | None = None
        latest_date: date | None = None
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            row_date = _date_from_any(row.get("date") or row.get("as_of_date")) or as_of_date
            if row_date > as_of_date:
                continue
            if latest_date is None or row_date > latest_date:
                latest = row
                latest_date = row_date
        if latest is None or latest_date is None:
            continue
        text = _row_text("KRX price", latest, raw_text=f"{event.company_name} KRX trading status", symbol=event.symbol, company_name=event.company_name)
        yield StoredSourceSnapshot(
            source_class="KRX",
            provider_name="KRXStoredPriceStatus",
            source_path=path,
            symbol=event.symbol,
            company_name=event.company_name,
            published_at=latest_date,
            text=text,
            canonical_url=f"snapshot://krx/prices/{path.name}#{latest_date.isoformat()}",
            anchor_type=AnchorType.API_RECORD,
            normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "KRX", "row": dict(latest)},
        )


def _issuer_official_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    text_root = repo_root / "data/raw/search_html/text"
    symbol_or_name = _safe_slug(event.company_name)
    for path in sorted(text_root.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if event.symbol not in text and event.company_name not in text and symbol_or_name not in path.stem:
            continue
        yield StoredSourceSnapshot(
            source_class="IR",
            provider_name="StoredIssuerOfficialOrReportSnapshot",
            source_path=path,
            symbol=event.symbol,
            company_name=event.company_name,
            published_at=as_of_date,
            text=text,
            canonical_url=f"snapshot://issuer_official/{path.name}",
            anchor_type=AnchorType.TEXT_SPAN,
            normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "IssuerOfficial", "snapshot_path": str(path)},
        )


def _trusted_news_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    for path in (repo_root / "fixtures/historical/news.json", repo_root / "data/raw/naver_news/news/news.json"):
        payload = _load_json(path)
        rows = payload if isinstance(payload, Sequence) and not isinstance(payload, (str, bytes, bytearray)) else []
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            text = " ".join(str(row.get(key) or "") for key in ("title", "snippet", "raw_text", "description"))
            if event.symbol not in text and event.company_name not in text:
                continue
            published = _date_from_any(row.get("publish_date") or row.get("published_at") or row.get("date")) or as_of_date
            if published > as_of_date:
                continue
            yield StoredSourceSnapshot(
                source_class="TrustedNews",
                provider_name="StoredTrustedNewsSnapshot",
                source_path=path,
                symbol=event.symbol,
                company_name=event.company_name,
                published_at=published,
                text=text,
                canonical_url=str(row.get("url") or f"snapshot://trusted_news/{event.symbol}/{published.isoformat()}"),
                anchor_type=AnchorType.TEXT_SPAN,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "TrustedNews", "row": dict(row)},
            )


def _anchor_for_snapshot(*, document: EvidenceDocument, snapshot: StoredSourceSnapshot) -> EvidenceAnchor:
    if snapshot.anchor_type != AnchorType.TEXT_SPAN:
        return EvidenceAnchor.structured(
            document=document,
            anchor_type=snapshot.anchor_type,
            locator=f"record:{snapshot.source_class}:{snapshot.symbol}",
            normalized_value=snapshot.normalized_value,
            exact_text=snapshot.text[:500],
            anchor_verified=True,
        )
    quote = _best_quote(snapshot.text)
    return EvidenceAnchor.text_span(document=document, document_text=snapshot.text, exact_text=quote)


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
        if source_names & {"generalweb", "web", "trustednews", "newsonly", "news"}:
            reasons.append("fcf_gap_sent_to_news_or_general_web")
    return tuple(dict.fromkeys(reasons))


def _first_source_class(task: SourceTask) -> str:
    return _normalize_source_class((task.preferred_source_classes or task.fallback_source_classes or ("unknown",))[0])


def _normalize_source_class(value: str) -> str:
    clean = str(value).strip()
    lowered = clean.lower()
    aliases = {
        "opendart": "DART",
        "dart": "DART",
        "kind": "KIND",
        "krx": "KRX",
        "companyguide": "CompanyGuide",
        "company_guide": "CompanyGuide",
        "wisereport": "CompanyGuide",
        "ir": "IR",
        "official": "Official",
        "issuerofficial": "IssuerOfficial",
        "issuer_official": "IssuerOfficial",
        "trustednews": "TrustedNews",
        "news": "News",
    }
    return aliases.get(lowered, clean)


def _source_type(source_class: str) -> SourceType:
    normalized = _normalize_source_class(source_class)
    if normalized in {"DART", "KIND", "KRX"}:
        return SourceType.FILING
    if normalized in {"IR", "IssuerOfficial", "Official"}:
        return SourceType.IR
    if normalized == "CompanyGuide":
        return SourceType.API
    if normalized in {"TrustedNews", "News"}:
        return SourceType.NEWS
    return SourceType.OTHER


def _csv_rows(path: Path) -> tuple[dict[str, str], ...]:
    if not path.exists():
        return ()
    with path.open("r", encoding="utf-8", newline="") as handle:
        return tuple(dict(row) for row in csv.DictReader(handle))


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def _row_text(provider: str, row: Mapping[str, Any], *, raw_text: str, symbol: str, company_name: str) -> str:
    fields = [f"{provider} source record", f"{company_name}({symbol})", raw_text]
    for key, value in row.items():
        if value in (None, "") or key in {"raw_text"}:
            continue
        fields.append(f"{key}={value}")
    return "\n".join(fields)


def _best_quote(text: str) -> str:
    clean = re.sub(r"\s+", " ", _strip_html(text)).strip()
    if not clean:
        return text[:200]
    return clean[:500]


def _strip_html(value: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#39;", "'")
    return re.sub(r"\s+", " ", text).strip()


def _date_from_any(value: Any) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    text = str(value).strip().replace(".", "-")
    if len(text) >= 8 and text[:8].isdigit():
        text = f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    try:
        return datetime.fromisoformat(text[:10]).date()
    except ValueError:
        return None


def _yy_mm_dd_date(value: Any, as_of_date: date) -> date | None:
    text = str(value or "").strip()
    match = re.match(r"(?P<yy>\d{2})[./-](?P<mm>\d{1,2})[./-](?P<dd>\d{1,2})$", text)
    if not match:
        return _date_from_any(value)
    year = 2000 + int(match.group("yy"))
    parsed = date(year, int(match.group("mm")), int(match.group("dd")))
    if parsed > as_of_date and year - 100 >= 1990:
        parsed = date(year - 100, parsed.month, parsed.day)
    return parsed


def _snapshot_date_from_text(text: str) -> date | None:
    match = re.search(r"\[기준\s*:?\s*(\d{4})[.-](\d{2})[.-](\d{2})\]", text)
    if not match:
        return None
    return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))


def _date_from_path(path: Path) -> date | None:
    for part in reversed(path.parts):
        parsed = _date_from_any(part)
        if parsed is not None:
            return parsed
    return None


def _safe_slug(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z가-힣]+", "_", value).strip("_").lower()


def _is_official_solvable_gap(primitive: str) -> bool:
    lower = primitive.lower()
    return any(token in lower for token in ("contract", "backlog", "cash", "fcf", "revision", "rpo"))


def _is_fcf_gap(primitive: str) -> bool:
    lower = primitive.lower()
    return any(token in lower for token in ("cash", "fcf", "revision"))


def _snapshot_relevance(primitive: str, text: str) -> int:
    lower = text.lower()
    primitive_lower = primitive.lower()
    keyword_map = {
        "customer": ("고객", "customer", "엔비디아", "nvidia", "asic", "다변화"),
        "allocation": ("고객", "customer", "allocation", "배정", "다변화"),
        "contract": ("계약", "수주", "long-term", "supply agreement", "backlog", "rpo"),
        "backlog": ("수주잔고", "backlog", "rpo", "order"),
        "capacity": ("공급부족", "공급 부족", "병목", "capacity", "capa", "supply"),
        "price": ("가격", "price", "asp", "상향"),
        "revision": ("추정eps 상향", "목표주가 상향", "revision", "상향"),
        "margin": ("마진", "영업이익", "opm", "margin", "fcf"),
        "fcf": ("fcf", "현금흐름", "cash"),
        "spread": ("spread", "스프레드", "판가", "원재료"),
        "retention": ("renewal", "retention", "churn", "arr", "rpo"),
    }
    score = 0
    for key, needles in keyword_map.items():
        if key in primitive_lower:
            score += sum(5 for needle in needles if needle.lower() in lower)
    score += sum(1 for token in primitive_lower.replace("_", " ").split() if token and token in lower)
    return score


__all__ = ["SourceAcquisitionRunnerV4", "StoredSourceSnapshot"]
