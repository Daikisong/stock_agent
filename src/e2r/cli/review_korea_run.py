"""Review one Korea live-lite output bundle."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.score_validity import (
    ScoreStateRowChange,
    compare_score_state_rows,
    find_score_state_contract_violations,
    score_state_output_contract_violations,
    serialized_score_block_reason,
    serialized_score_valid,
    serialized_visible_score,
)


@dataclass(frozen=True)
class KoreaRunReviewSummary:
    """Small operational summary for one live-lite run."""

    as_of_date: str
    total_candidates: int
    event_search_count: int
    deep_research_count: int
    stage_distribution: Mapping[str, int] = field(default_factory=dict)
    source_modes: Mapping[str, str] = field(default_factory=dict)
    live_requests_executed: int = 0
    live_requests_failed: int = 0
    cache_hits: int = 0
    cache_writes: int = 0
    missing_credentials: tuple[str, ...] = field(default_factory=tuple)
    top_skipped_candidate_reasons: Mapping[str, int] = field(default_factory=dict)
    top_skipped_query_reasons: Mapping[str, int] = field(default_factory=dict)
    top_dropped_result_reasons: Mapping[str, int] = field(default_factory=dict)
    parser_confidence_low_evidence: tuple[str, ...] = field(default_factory=tuple)
    manual_review_required_items: tuple[str, ...] = field(default_factory=tuple)
    score_state_contract_findings: tuple[str, ...] = field(default_factory=tuple)
    targeted_score_states: tuple[str, ...] = field(default_factory=tuple)
    targeted_score_changes: tuple[str, ...] = field(default_factory=tuple)


def build_review_summary(
    output_directory: str | Path,
    as_of_date: str,
    *,
    previous_output_directory: str | Path | None = None,
    previous_as_of_date: str | None = None,
) -> KoreaRunReviewSummary:
    """Read live-lite output files and return a compact review summary."""

    root = _output_root(output_directory)
    candidates = _read_json(root / f"{as_of_date}_candidates.json")
    evidence = _read_json(root / f"{as_of_date}_evidence.json")
    run_log = _read_json(root / f"{as_of_date}_run_log.json")
    brief = _read_text(root / f"{as_of_date}_brief.md")

    candidate_items = tuple(candidates.get("candidates") or ())
    evidence_items = tuple(evidence.get("evidence") or ())
    audit_findings = tuple(run_log.get("audit_findings") or ())
    targeted_rows = tuple(run_log.get("targeted_smoke_results") or ())
    previous_targeted_rows = _previous_targeted_rows(
        previous_output_directory=previous_output_directory,
        previous_as_of_date=previous_as_of_date or as_of_date,
    )

    return KoreaRunReviewSummary(
        as_of_date=as_of_date,
        total_candidates=len(candidate_items),
        event_search_count=sum(1 for item in candidate_items if item.get("recommended_next_layer") == "event_search"),
        deep_research_count=sum(1 for item in candidate_items if item.get("recommended_next_layer") == "deep_research"),
        stage_distribution=_stage_distribution(brief),
        source_modes=dict(run_log.get("source_modes") or {}),
        live_requests_executed=int(run_log.get("live_requests_executed") or 0),
        live_requests_failed=int(run_log.get("live_requests_failed") or 0),
        cache_hits=int(run_log.get("cache_hits") or 0),
        cache_writes=int(run_log.get("cache_writes") or 0),
        missing_credentials=tuple(run_log.get("missing_credentials") or ()),
        top_skipped_candidate_reasons=_top_reasons(run_log.get("skipped_candidates") or ()),
        top_skipped_query_reasons=_top_reasons(run_log.get("skipped_queries") or ()),
        top_dropped_result_reasons=_top_reasons(run_log.get("dropped_search_results") or ()),
        parser_confidence_low_evidence=_low_confidence_evidence(evidence_items),
        manual_review_required_items=_manual_review_items(audit_findings),
        score_state_contract_findings=tuple(
            dict.fromkeys(
                tuple(run_log.get("score_state_contract_findings") or ())
                + _score_state_contract_findings(candidate_items, targeted_rows)
            )
        ),
        targeted_score_states=_targeted_score_states(targeted_rows),
        targeted_score_changes=_targeted_score_changes(previous_targeted_rows, targeted_rows),
    )


def render_review_summary(summary: KoreaRunReviewSummary) -> str:
    """Render the review summary as plain text for terminal output."""

    lines = [
        f"Korea Live-Lite Run Review / {summary.as_of_date}",
        "",
        f"total candidates: {summary.total_candidates}",
        f"event_search: {summary.event_search_count}",
        f"deep_research: {summary.deep_research_count}",
        f"stage distribution: {_mapping_text(summary.stage_distribution)}",
        f"source modes: {_mapping_text(summary.source_modes)}",
        f"live requests: executed={summary.live_requests_executed}, failed={summary.live_requests_failed}",
        f"cache: hits={summary.cache_hits}, writes={summary.cache_writes}",
        f"missing credentials: {', '.join(summary.missing_credentials) if summary.missing_credentials else 'none'}",
        f"top skipped candidate reasons: {_mapping_text(summary.top_skipped_candidate_reasons)}",
        f"top skipped query reasons: {_mapping_text(summary.top_skipped_query_reasons)}",
        f"top dropped result reasons: {_mapping_text(summary.top_dropped_result_reasons)}",
        f"low confidence evidence: {', '.join(summary.parser_confidence_low_evidence) if summary.parser_confidence_low_evidence else 'none'}",
        f"manual review required: {', '.join(summary.manual_review_required_items) if summary.manual_review_required_items else 'none'}",
        f"score state contract: {' | '.join(summary.score_state_contract_findings) if summary.score_state_contract_findings else 'ok'}",
        f"targeted score states: {' | '.join(summary.targeted_score_states) if summary.targeted_score_states else 'none'}",
        f"targeted score changes: {' | '.join(summary.targeted_score_changes) if summary.targeted_score_changes else 'none'}",
    ]
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Review one Korea live-lite run output bundle.")
    parser.add_argument("as_of_date", help="Run date in YYYY-MM-DD format")
    parser.add_argument("--output-directory", default="output", help="Output root or output/korea_live_lite directory")
    parser.add_argument("--previous-output-directory", help="Previous output root or output/korea_live_lite directory")
    parser.add_argument("--previous-as-of-date", help="Previous run date; defaults to as_of_date when previous output is provided")
    args = parser.parse_args(argv)
    print(
        render_review_summary(
            build_review_summary(
                args.output_directory,
                args.as_of_date,
                previous_output_directory=args.previous_output_directory,
                previous_as_of_date=args.previous_as_of_date,
            )
        ),
        end="",
    )
    return 0


def _output_root(output_directory: str | Path) -> Path:
    root = Path(output_directory)
    if (root / "korea_live_lite").exists():
        return root / "korea_live_lite"
    return root


def _read_json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _stage_distribution(brief: str) -> dict[str, int]:
    counts = Counter(re.findall(r"현재 Stage:\s*([^/\n]+)", brief))
    return dict(sorted((key.strip(), value) for key, value in counts.items()))


def _top_reasons(rows: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    counts = Counter(str(row.get("reason") or "unknown") for row in rows)
    return dict(counts.most_common(5))


def _low_confidence_evidence(rows: Sequence[Mapping[str, Any]]) -> tuple[str, ...]:
    items: list[str] = []
    for row in rows:
        parsed = row.get("parsed_fields") or {}
        confidence = _num(parsed.get("parser_confidence"))
        if confidence is None:
            confidence = _num(parsed.get("confidence"))
        if confidence is None:
            confidence = _num(row.get("confidence"))
        if confidence is not None and confidence < 0.5:
            items.append(str(row.get("evidence_id") or row.get("title") or row.get("symbol") or "unknown"))
    return _limited_items(items)


def _manual_review_items(findings: Sequence[Mapping[str, Any]]) -> tuple[str, ...]:
    items: list[str] = []
    for finding in findings:
        action = str(finding.get("suggested_action") or "")
        if action in {"manual_review", "block_green", "downgrade_to_yellow"}:
            items.append(str(finding.get("finding_id") or finding.get("code") or "audit_finding"))
    return _limited_items(items)


def _score_state_contract_findings(
    candidate_rows: Sequence[Mapping[str, Any]],
    targeted_rows: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    findings = (
        find_score_state_contract_violations(
            candidate_rows,
            path="candidates",
            include_score_only=True,
            require_visible_score_field=True,
        )
        + find_score_state_contract_violations(
            targeted_rows,
            path="targeted_smoke_results",
            include_score_only=True,
            require_visible_score_field=True,
        )
    )
    return _limited_items(tuple(f"{item.path}:{item.violation}" for item in findings))


def _targeted_score_states(rows: Sequence[Mapping[str, Any]]) -> tuple[str, ...]:
    items: list[str] = []
    for row in rows:
        symbol = str(row.get("symbol") or "unknown")
        stage = str(row.get("stage") or "unknown")
        score_text = _score_text(serialized_visible_score(row))
        valid = serialized_score_valid(row)
        reason = serialized_score_block_reason(row) or "valid"
        fingerprint = row.get("score_fingerprint") or "no_fingerprint"
        input_fingerprint = row.get("research_input_fingerprint") or "no_input_fingerprint"
        drivers = tuple(str(item) for item in (row.get("score_variability_drivers") or ()))
        driver_text = ",".join(drivers[:4]) if drivers else "none"
        contract = score_state_output_contract_violations(row)
        contract_text = ",".join(contract[:3]) if contract else "ok"
        items.append(
            f"{symbol} stage={stage} visible_score={score_text} valid={valid} reason={reason} fingerprint={fingerprint} input_fingerprint={input_fingerprint} drivers={driver_text} contract={contract_text}"
        )
    return _limited_items(items, limit=5)


def _previous_targeted_rows(
    *,
    previous_output_directory: str | Path | None,
    previous_as_of_date: str,
) -> tuple[Mapping[str, Any], ...]:
    if previous_output_directory is None:
        return ()
    root = _output_root(previous_output_directory)
    payload = _read_json(root / f"{previous_as_of_date}_run_log.json")
    return tuple(payload.get("targeted_smoke_results") or ())


def _targeted_score_changes(
    before_rows: Sequence[Mapping[str, Any]],
    after_rows: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    if not before_rows:
        return ()
    changes = compare_score_state_rows(before_rows, after_rows, key_fields=("symbol",))
    items = [_score_change_text(change) for change in changes]
    return _limited_items(items, limit=5)


def _score_change_text(change: ScoreStateRowChange) -> str:
    comparison = change.comparison
    drivers = ",".join(comparison.drivers[:4]) if comparison.drivers else "none"
    return (
        f"{change.key} change={comparison.status} "
        f"before={_score_text(comparison.visible_score_before)} "
        f"after={_score_text(comparison.visible_score_after)} "
        f"delta={_score_text(comparison.visible_score_delta)} "
        f"drivers={drivers}"
    )


def _score_text(value: float | None) -> str:
    return "pending" if value is None else f"{value:g}"


def _limited_items(items: Sequence[str], limit: int = 10) -> tuple[str, ...]:
    """Keep terminal review output readable for high-volume live runs."""

    if len(items) <= limit:
        return tuple(items)
    return tuple(items[:limit]) + (f"... +{len(items) - limit} more",)


def _mapping_text(value: Mapping[str, Any]) -> str:
    if not value:
        return "none"
    return ", ".join(f"{key}={item}" for key, item in value.items())


def _num(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["KoreaRunReviewSummary", "build_review_summary", "render_review_summary", "main"]
