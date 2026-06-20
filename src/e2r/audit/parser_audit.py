"""Parser sanity checks for live-lite research evidence."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from e2r.models import Evidence, ScoreSnapshot, Stage, StageSnapshot
from e2r.sources.opendart import DISCLOSURE_SIGNAL_ROUTINE


@dataclass(frozen=True)
class AuditFinding:
    """One parser or evidence-quality issue that may require review."""

    finding_id: str
    symbol: str
    severity: str
    code: str
    message: str
    suggested_action: str
    evidence_id: str | None = None
    field_name: str | None = None
    observed_value: float | str | None = None


def audit_parser_outputs(
    *,
    evidence: Sequence[Evidence] = (),
    scores: Sequence[ScoreSnapshot] = (),
    stages: Sequence[StageSnapshot] = (),
) -> tuple[AuditFinding, ...]:
    """Audit parsed evidence fields before live-lite output is trusted."""

    findings: list[AuditFinding] = []
    evidence_by_symbol: dict[str, list[Evidence]] = {}
    evidence_by_id: dict[str, Evidence] = {}
    for item in evidence:
        evidence_by_symbol.setdefault(item.symbol, []).append(item)
        evidence_by_id[item.evidence_id] = item
        findings.extend(_audit_evidence(item))

    for score in scores:
        findings.extend(_audit_contract_score_inputs(score, evidence_by_symbol.get(score.symbol, ())))

    for stage in stages:
        findings.extend(_audit_stage_confidence(stage, evidence_by_symbol.get(stage.symbol, ()), evidence_by_id))

    return tuple(_dedupe(findings))


def _audit_evidence(evidence: Evidence) -> tuple[AuditFinding, ...]:
    fields = evidence.parsed_fields
    findings: list[AuditFinding] = []
    if fields.get("search_snippet_only"):
        findings.append(
            _finding(
                evidence,
                "warning",
                "search_snippet_only_evidence",
                "evidence was built from a search snippet without fetched document text",
                "manual_review",
                "search_snippet_only",
                1.0,
            )
        )
    if fields.get("search_snippet_date_unverified"):
        findings.append(
            _finding(
                evidence,
                "hard",
                "search_snippet_date_unverified",
                "search snippet date was not verified and cannot support Stage 3-Green",
                "block_green",
                "search_snippet_date_unverified",
                1.0,
            )
        )
    checks: tuple[tuple[str, str, float, str, str, str], ...] = (
        ("contract_amount_to_prior_sales", "contract_ratio_too_high", 5.0, "hard", "block_green", "contract amount to prior sales is above 500%"),
        ("contract_duration_months", "contract_duration_too_long", 120.0, "warning", "manual_review", "contract duration is above 120 months"),
        ("opm", "opm_too_high", 80.0, "warning", "manual_review", "OPM is above 80%"),
        ("est_per", "est_per_too_high", 300.0, "warning", "manual_review", "estimated PER is above 300"),
        ("est_pbr", "est_pbr_too_high", 50.0, "warning", "manual_review", "estimated PBR is above 50"),
        ("target_revision_pct", "target_revision_too_high", 300.0, "warning", "manual_review", "target price revision is above 300%"),
        ("target_price_revision_1m", "target_price_revision_too_high", 300.0, "hard", "score_exclude", "target price revision is above 300%"),
        ("eps_revision_1m", "eps_revision_too_high", 300.0, "warning", "score_exclude", "EPS revision is above 300%"),
        ("op_revision_1m", "op_revision_too_high", 300.0, "warning", "score_exclude", "OP revision is above 300%"),
    )
    for field_name, code, threshold, severity, action, message in checks:
        value = _num(fields.get(field_name))
        if value is not None and value > threshold:
            findings.append(_finding(evidence, severity, code, message, action, field_name, value))

    est_per = _num(fields.get("est_per"))
    if est_per is not None and est_per < 1.0:
        findings.append(_finding(evidence, "warning", "est_per_too_low", "estimated PER is below 1", "manual_review", "est_per", est_per))
    est_pbr = _num(fields.get("est_pbr"))
    if est_pbr is not None and est_pbr < 0.1:
        findings.append(_finding(evidence, "warning", "est_pbr_too_low", "estimated PBR is below 0.1", "manual_review", "est_pbr", est_pbr))

    low = _num(fields.get("fifty_two_week_low"))
    current = _num(fields.get("current_price"))
    if low is not None and current is not None and low > current:
        findings.append(
            _finding(
                evidence,
                "hard",
                "fifty_two_week_low_above_current_price",
                "52-week low is above current price",
                "block_green",
                "fifty_two_week_low",
                low,
            )
        )

    confidence = _confidence(evidence)
    if confidence < 0.5 and not fields.get("search_snippet_only") and not _skip_low_confidence_noise(evidence):
        findings.append(
            _finding(
                evidence,
                "warning",
                "low_parser_confidence",
                "parser confidence is below 0.5",
                "manual_review",
                "parser_confidence",
                confidence,
            )
        )
    return tuple(findings)


def _skip_low_confidence_noise(evidence: Evidence) -> bool:
    fields = evidence.parsed_fields
    if fields.get("detail_fetched"):
        return False
    if fields.get("signal_class") == DISCLOSURE_SIGNAL_ROUTINE:
        return True
    return evidence.source_type == "disclosure" and evidence.source_name == "OpenDART" and fields.get("signal_class") == DISCLOSURE_SIGNAL_ROUTINE


def _audit_contract_score_inputs(score: ScoreSnapshot, evidence: Sequence[Evidence]) -> tuple[AuditFinding, ...]:
    contract_score = _num(score.diagnostic_scores.get("contract_quality")) or 0.0
    if contract_score <= 0.0:
        return ()
    has_amount = any(_has_field(item.parsed_fields, "contract_amount", "contract_amount_to_prior_sales", "contract_to_sales") for item in evidence)
    has_duration = any(_has_field(item.parsed_fields, "contract_duration_months", "lta_duration_months") for item in evidence)
    if has_amount and has_duration:
        return ()
    if _has_source_backed_contract_proxy(score, evidence):
        return ()
    severity = "hard" if contract_score >= 45.0 else "warning"
    action = "block_green" if severity == "hard" else "manual_review"
    missing = "amount and duration"
    if has_amount:
        missing = "duration"
    elif has_duration:
        missing = "amount"
    return (
        AuditFinding(
            finding_id=f"parser-audit:{score.symbol}:contract_score_missing_fields",
            symbol=score.symbol,
            severity=severity,
            code="contract_score_missing_fields",
            message=f"contract_quality score exists but contract {missing} field is missing",
            suggested_action=action,
            field_name="contract_quality",
            observed_value=contract_score,
        ),
    )


def _has_source_backed_contract_proxy(score: ScoreSnapshot, evidence: Sequence[Evidence]) -> bool:
    bridge_raw = _num(score.diagnostic_scores.get("source_backed_green_bridge_raw")) or 0.0
    guard_risk = _num(score.diagnostic_scores.get("research_axis_bridge_guard_risk")) or 0.0
    contract_required = _num(score.diagnostic_scores.get("contract_required_for_green")) or 0.0
    if bridge_raw >= 80.0 and guard_risk <= 0.0 and contract_required <= 0.0:
        return True
    for item in evidence:
        fields = item.parsed_fields
        has_customer_or_capacity = any(
            _has_field(fields, key)
            for key in (
                "customer_preorder_or_allocation",
                "capacity_precommitted",
                "booked_out_capacity",
                "order_slot_locked",
                "revenue_visibility_contract",
                "customer_contract_visible",
                "named_customer_quality",
            )
        )
        has_delivery_or_backlog = any(
            _has_field(fields, key)
            for key in (
                "delivery_schedule",
                "order_to_revenue_bridge",
                "revenue_recognition_path",
                "record_backlog",
                "backlog_visibility",
                "order_backlog_to_sales",
            )
        )
        if has_customer_or_capacity and has_delivery_or_backlog:
            return True
    return False


def _audit_stage_confidence(
    stage: StageSnapshot,
    symbol_evidence: Sequence[Evidence],
    evidence_by_id: Mapping[str, Evidence],
) -> tuple[AuditFinding, ...]:
    if stage.stage != Stage.STAGE_3_GREEN:
        return ()
    linked = tuple(evidence_by_id[item] for item in stage.evidence_ids if item in evidence_by_id)
    if not linked:
        linked = tuple(symbol_evidence)
    if not linked:
        return (
            AuditFinding(
                finding_id=f"parser-audit:{stage.symbol}:stage3_green_no_evidence",
                symbol=stage.symbol,
                severity="hard",
                code="stage3_green_no_evidence",
                message="Stage 3-Green has no linked evidence",
                suggested_action="block_green",
            ),
        )
    if any(item.parsed_fields.get("search_snippet_only") for item in linked) and not any(
        item.source_type != "news" or not item.parsed_fields.get("search_snippet_only") for item in linked
    ):
        return (
            AuditFinding(
                finding_id=f"parser-audit:{stage.symbol}:stage3_green_snippet_only",
                symbol=stage.symbol,
                severity="hard",
                code="stage3_green_snippet_only",
                message="Stage 3-Green is supported only by search-snippet evidence",
                suggested_action="block_green",
            ),
        )
    if all(_confidence(item) < 0.5 for item in linked):
        return (
            AuditFinding(
                finding_id=f"parser-audit:{stage.symbol}:stage3_green_low_confidence_only",
                symbol=stage.symbol,
                severity="hard",
                code="stage3_green_low_confidence_only",
                message="Stage 3-Green is supported only by low-confidence evidence",
                suggested_action="block_green",
            ),
        )
    if any(item.parsed_fields.get("green_allowed_by_date", True) is False for item in linked):
        return (
            AuditFinding(
                finding_id=f"parser-audit:{stage.symbol}:stage3_green_date_unverified_snippet",
                symbol=stage.symbol,
                severity="hard",
                code="stage3_green_date_unverified_snippet",
                message="Stage 3-Green has date-unverified snippet evidence",
                suggested_action="block_green",
            ),
        )
    return ()


def _finding(
    evidence: Evidence,
    severity: str,
    code: str,
    message: str,
    action: str,
    field_name: str,
    value: float,
) -> AuditFinding:
    return AuditFinding(
        finding_id=f"parser-audit:{evidence.symbol}:{evidence.evidence_id}:{code}",
        symbol=evidence.symbol,
        severity=severity,
        code=code,
        message=message,
        suggested_action=action,
        evidence_id=evidence.evidence_id,
        field_name=field_name,
        observed_value=round(value, 6),
    )


def _confidence(evidence: Evidence) -> float:
    fields = evidence.parsed_fields
    value = _num(fields.get("parser_confidence"))
    if value is None:
        value = _num(fields.get("confidence"))
    if value is None:
        value = evidence.confidence
    return float(value)


def _has_field(fields: Mapping[str, Any], *names: str) -> bool:
    return any(fields.get(name) not in (None, "") for name in names)


def _num(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _dedupe(findings: Sequence[AuditFinding]) -> tuple[AuditFinding, ...]:
    unique: dict[str, AuditFinding] = {}
    for finding in findings:
        unique.setdefault(finding.finding_id, finding)
    return tuple(unique.values())


__all__ = ["AuditFinding", "audit_parser_outputs"]
