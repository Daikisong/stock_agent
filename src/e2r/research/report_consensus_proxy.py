"""Create consensus/revision proxy rows from parsed broker reports.

These proxies are intentionally narrow: they only convert numbers explicitly
present in a parsed research report. Missing EPS/OP/FCF revisions remain
missing.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.models import ConsensusRevision, ConsensusSnapshot, ResearchReport

_MIN_PROXY_PARSER_CONFIDENCE = 0.35
_MIN_FULL_TEXT_CHARS = 80
_REVISION_OUTLIER_ABS_PCT = 300.0


@dataclass(frozen=True)
class ReportConsensusProxyResult:
    """Consensus proxy rows and reports annotated with proxy metadata."""

    consensus: tuple[ConsensusSnapshot, ...]
    consensus_revisions: tuple[ConsensusRevision, ...]
    reports: tuple[ResearchReport, ...]


def build_report_consensus_proxy(
    reports: Sequence[ResearchReport],
    *,
    as_of_date: date | None = None,
) -> ReportConsensusProxyResult:
    """Convert explicit report estimate fields into consensus proxy objects."""

    consensus: list[ConsensusSnapshot] = []
    revisions: list[ConsensusRevision] = []
    annotated_reports: list[ResearchReport] = []

    for report in reports:
        report_as_of = as_of_date or report.as_of_date
        proxy_allowed, proxy_metadata = _report_proxy_metadata(report, report_as_of)
        report_consensus = _consensus_from_report(report, report_as_of, proxy_metadata) if proxy_allowed else ()
        report_revision = _revision_from_report(report, report_as_of, proxy_metadata) if proxy_allowed else None
        proxy_created = bool(report_consensus or report_revision)
        parsed_fields = dict(report.parsed_fields)
        if proxy_created:
            parsed_fields.update(proxy_metadata)
            if report_revision is not None:
                parsed_fields.update(
                    {
                        key: value
                        for key, value in report_revision.parsed_fields.items()
                        if key in {"target_price_revision_outlier", "consensus_proxy_weak_reasons"}
                    }
                )
        consensus.extend(report_consensus)
        if report_revision is not None:
            revisions.append(report_revision)
        annotated_reports.append(replace(report, parsed_fields=parsed_fields))

    return ReportConsensusProxyResult(
        consensus=tuple(consensus),
        consensus_revisions=tuple(revisions),
        reports=tuple(annotated_reports),
    )


def _consensus_from_report(
    report: ResearchReport,
    as_of_date: date,
    proxy_metadata: Mapping[str, Any],
) -> tuple[ConsensusSnapshot, ...]:
    fiscal_year = _fiscal_year(report)
    rows: list[ConsensusSnapshot] = []
    for offset, prefix in enumerate(("fy1", "fy2", "fy3")):
        values = {
            "sales_e": getattr(report, f"{prefix}_sales"),
            "op_e": getattr(report, f"{prefix}_op"),
            "eps_e": getattr(report, f"{prefix}_eps"),
        }
        if offset == 0:
            values["per_e"] = report.est_per
            values["pbr_e"] = report.est_pbr
            values["roe_e"] = report.roe
            values["target_price"] = report.target_price
        if not any(value is not None for value in values.values()):
            continue
        rows.append(
            ConsensusSnapshot(
                symbol=report.symbol,
                date=report.publish_date,
                fiscal_year=fiscal_year + offset,
                as_of_date=as_of_date,
                source="report_proxy",
                parsed_fields=proxy_metadata,
                **values,
            )
        )
    return tuple(rows)


def _revision_from_report(
    report: ResearchReport,
    as_of_date: date,
    proxy_metadata: Mapping[str, Any],
) -> ConsensusRevision | None:
    fields = report.parsed_fields
    values = {
        "eps_revision_1m": _first_number(fields, "eps_revision_pct", "eps_revision_1m_pct", "eps_revision_1m"),
        "op_revision_1m": _first_number(fields, "op_revision_pct", "op_revision_1m_pct", "op_revision_1m"),
        "fcf_revision_1m": _first_number(fields, "fcf_revision_pct", "fcf_revision_1m_pct", "fcf_revision_1m"),
        "target_price_revision_1m": _first_number(
            fields,
            "target_price_revision_pct",
            "target_revision_pct",
            "target_price_revision_1m",
        ),
    }
    if report.target_revision_pct is not None:
        values["target_price_revision_1m"] = report.target_revision_pct
    if not any(value is not None for value in values.values()):
        return None
    parsed_fields = dict(proxy_metadata)
    parsed_fields["explicit_revision_proxy"] = True
    for key, value in values.items():
        if value is not None:
            parsed_fields[key] = value
    if _source_backed_revision_values_are_usable(report, parsed_fields):
        parsed_fields["consensus_proxy_quality"] = "source_backed_revision"
        parsed_fields["consensus_proxy_score_eligible"] = True
    for key, value in values.items():
        if value is not None and abs(value) > _REVISION_OUTLIER_ABS_PCT:
            parsed_fields[f"{key}_outlier"] = True
            if key == "target_price_revision_1m":
                parsed_fields["target_price_revision_outlier"] = True
    return ConsensusRevision(
        symbol=report.symbol,
        date=report.publish_date,
        fiscal_year=_fiscal_year(report),
        as_of_date=as_of_date,
        source="report_proxy",
        parsed_fields=parsed_fields,
        **values,
    )


def _source_backed_revision_values_are_usable(report: ResearchReport, fields: Mapping[str, Any]) -> bool:
    if report.parsed_fields.get("search_snippet_only"):
        return False
    if not (report.parsed_fields.get("source_url") or report.parsed_fields.get("url")):
        return False
    parser_confidence = _first_number(fields, "parser_confidence")
    if parser_confidence is not None and parser_confidence < _MIN_PROXY_PARSER_CONFIDENCE:
        return False
    return True


def _report_proxy_metadata(report: ResearchReport, as_of_date: date) -> tuple[bool, dict[str, Any]]:
    fields = report.parsed_fields
    if report.publish_date > as_of_date:
        return False, {}
    if fields.get("search_snippet_only"):
        return False, {}
    if fields.get("search_snippet_date_unverified") or fields.get("date_unverified_document"):
        return False, {}
    if fields.get("green_allowed_by_date") is False:
        return False, {}
    parser_confidence = _first_number(fields, "parser_confidence")
    weak_reasons: list[str] = []
    if parser_confidence is not None and parser_confidence < _MIN_PROXY_PARSER_CONFIDENCE:
        weak_reasons.append("low_parser_confidence")
    raw_text = (report.raw_text or "").strip()
    if not raw_text:
        weak_reasons.append("missing_raw_text")
    elif len(raw_text) < _MIN_FULL_TEXT_CHARS:
        weak_reasons.append("short_raw_text")
    if not fields.get("source_url") and not fields.get("url"):
        weak_reasons.append("missing_source_url")
    quality = "weak" if weak_reasons else "full_text_report"
    return True, {
        "consensus_proxy_created": True,
        "consensus_proxy_source": "research_report",
        "derived_from_source_type": "research_report",
        "consensus_proxy_quality": quality,
        "consensus_proxy_score_eligible": quality == "full_text_report",
        "consensus_proxy_weak_reasons": tuple(weak_reasons),
        **({"parser_confidence": parser_confidence} if parser_confidence is not None else {}),
    }


def _fiscal_year(report: ResearchReport) -> int:
    value = _first_number(report.parsed_fields, "fy1_fiscal_year", "fiscal_year")
    if value is not None and value >= 1900:
        return int(value)
    return report.publish_date.year


def _first_number(fields: Mapping[str, Any], *keys: str) -> float | None:
    for key in keys:
        value = fields.get(key)
        if value in (None, ""):
            continue
        try:
            return float(value)
        except (TypeError, ValueError):
            continue
    return None


__all__ = ["ReportConsensusProxyResult", "build_report_consensus_proxy"]
