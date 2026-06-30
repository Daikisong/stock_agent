"""CompanyGuide/report radar Census v3 source family attempt rows."""

from __future__ import annotations

from . import attempt_row


def collect_companyguide_report_attempt(symbol: str, *, has_report_event: bool = False) -> dict:
    return attempt_row(
        symbol=symbol,
        source_family="CompanyGuide/ReportRadar",
        status="REPORT_EVENT_PRESENT" if has_report_event else "NO_ACCEPTED_REPORT_CLAIM",
    )


__all__ = ["collect_companyguide_report_attempt"]
