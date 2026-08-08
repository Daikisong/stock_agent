"""Source-backed structured financial/consensus/valuation record boundary."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
import math
import re
from typing import Any, Mapping, Sequence


BROKER_VALUATION_FACT_RECORD_CONTRACTS: Mapping[str, Mapping[str, str]] = {
    "FORWARD_BOOK_VALUE": {
        "metric_id": "broker_forward_book_value",
        "unit": "KRW_PER_SHARE",
    },
    "FORWARD_PB": {
        "metric_id": "broker_forward_pb",
        "unit": "MULTIPLE",
    },
    "FORWARD_EV_EBITDA": {
        "metric_id": "broker_forward_ev_ebitda",
        "unit": "MULTIPLE",
    },
}
BROKER_VALUATION_QUOTE_METRIC_PATTERNS: Mapping[str, re.Pattern[str]] = {
    "FORWARD_BOOK_VALUE": re.compile(
        r"(?:\bBPS\b|book\s+value\s+per\s+share|주당\s*(?:순자산|장부가))",
        re.IGNORECASE,
    ),
    "FORWARD_PB": re.compile(
        r"(?:\bPBR\b|\bP\s*/\s*B\b|주가\s*순자산)",
        re.IGNORECASE,
    ),
    "FORWARD_EV_EBITDA": re.compile(
        r"(?:\bEV\s*/\s*EBITDA\b|enterprise\s+value\s*/?\s*EBITDA)",
        re.IGNORECASE,
    ),
}


def broker_valuation_forward_period_end(period: str) -> date | None:
    normalized = str(period or "").strip().upper().replace(" ", "")
    quarter = re.match(
        r"^(?:FY)?(20\d{2})(?:Q([1-4])|([1-4])Q|([1-4])분기)",
        normalized,
    )
    if quarter:
        year = int(quarter.group(1))
        value = int(next(item for item in quarter.groups()[1:] if item))
        month = value * 3
        day = 31 if month in {3, 12} else 30
        return date(year, month, day)
    annual = re.match(
        r"^(?:FY)?(20\d{2})(?:년|[EF])(?:\b|\(|;|,|$)",
        normalized,
    )
    if annual:
        return date(int(annual.group(1)), 12, 31)
    return None


def broker_valuation_quote_matches_claim(
    *,
    role: str,
    exact_quote: str,
    period: str,
    value: float,
) -> bool:
    """Bind a broker metric/value to its exact quote row and period column."""

    pattern = BROKER_VALUATION_QUOTE_METRIC_PATTERNS.get(role)
    period_end = broker_valuation_forward_period_end(period)
    if pattern is None or period_end is None or not exact_quote.strip():
        return False
    year = period_end.year
    marker_match = re.search(rf"(?<!\d){year}\s*([EF])\b", period, re.I)
    expected_marker = marker_match.group(1).upper() if marker_match else ""
    lines = [line.strip() for line in exact_quote.splitlines() if line.strip()]
    for index, line in enumerate(lines):
        if not pattern.search(line):
            continue
        if _broker_line_binds_period_and_value(
            line,
            year=year,
            expected_marker=expected_marker,
            value=value,
        ):
            return True
        for header in reversed(lines[max(0, index - 12) : index]):
            columns = _broker_period_columns(header)
            if not columns:
                continue
            matching_indices = [
                column_index
                for column_index, (column_year, column_marker) in enumerate(columns)
                if column_year == year
                and (
                    not expected_marker
                    or not column_marker
                    or column_marker == expected_marker
                )
            ]
            if not matching_indices:
                continue
            row_values = _broker_reported_numbers(line)
            if len(row_values) < len(columns):
                continue
            aligned_values = row_values[-len(columns) :]
            if any(
                _same_broker_reported_number(
                    aligned_values[column_index], value
                )
                for column_index in matching_indices
            ):
                return True
    return False


def _broker_line_binds_period_and_value(
    line: str,
    *,
    year: int,
    expected_marker: str,
    value: float,
) -> bool:
    period_tokens = _broker_period_columns(line)
    matched_metric_count = sum(
        bool(pattern.search(line))
        for pattern in BROKER_VALUATION_QUOTE_METRIC_PATTERNS.values()
    )
    if len(period_tokens) != 1 or matched_metric_count != 1:
        return False
    token_year, token_marker = period_tokens[0]
    if token_year != year or (
        expected_marker
        and token_marker
        and token_marker != expected_marker
    ):
        return False
    return any(
        not (1900 <= abs(number) <= 2100 and number.is_integer())
        and _same_broker_reported_number(number, value)
        for number in _broker_reported_numbers(line)
    )


def _broker_period_columns(text: str) -> tuple[tuple[int, str], ...]:
    return tuple(
        (int(match.group(1)), (match.group(2) or "").upper())
        for match in re.finditer(
            r"(?<!\d)(20\d{2})\s*([EF]?)(?!\d)",
            text,
            re.IGNORECASE,
        )
    )


def _broker_reported_numbers(text: str) -> tuple[float, ...]:
    return tuple(
        float(token.replace(",", ""))
        for token in re.findall(r"[-+]?\d[\d,]*(?:\.\d+)?", text)
    )


def _same_broker_reported_number(left: float, right: float) -> bool:
    tolerance = max(1e-9, abs(float(right)) * 1e-9)
    return abs(float(left) - float(right)) <= tolerance


@dataclass(frozen=True)
class StructuredMetricRecord:
    record_id: str
    target_id: str
    as_of_date: str
    metric_id: str
    value: float | int | str
    unit: str
    period: str
    evidence_roles: tuple[str, ...]
    source_ids: tuple[str, ...]
    source_route: str
    observed_at: str
    record_kind: str
    confidence: float
    available_at: str | None = None
    dataset: str = "GENERIC"
    provenance: str = "OBSERVED"
    input_record_ids: tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)
    score_authority: bool = False
    schema_version: str = "e2r_structured_metric_record_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.record_id, "record_id"),
            (self.target_id, "target_id"),
            (self.metric_id, "metric_id"),
            (self.unit, "unit"),
            (self.period, "period"),
            (self.source_route, "source_route"),
            (self.record_kind, "record_kind"),
        ):
            if not str(value).strip():
                raise ValueError(f"{label} is required")
        cutoff = date.fromisoformat(self.as_of_date)
        observed = date.fromisoformat(self.observed_at[:10])
        if observed > cutoff:
            raise ValueError("structured metric leaks future observations")
        available = date.fromisoformat((self.available_at or self.observed_at)[:10])
        if available < observed:
            raise ValueError("structured metric available_at cannot precede observed_at")
        if available > cutoff:
            raise ValueError("structured metric leaks future availability")
        if not self.source_ids:
            raise ValueError("structured metric requires source lineage")
        if len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("structured metric source ids must be unique")
        if not self.evidence_roles:
            raise ValueError("structured metric requires evidence roles")
        if not 0 <= float(self.confidence) <= 1:
            raise ValueError("structured metric confidence is invalid")
        if isinstance(self.value, float) and not math.isfinite(self.value):
            raise ValueError("structured metric value must be finite")
        if self.dataset not in {
            "GENERIC",
            "FINANCIAL",
            "CONSENSUS_REVISION",
            "VALUATION",
        }:
            raise ValueError("unknown structured metric dataset")
        if self.provenance not in {
            "OBSERVED",
            "STRUCTURED_EXTRACTED",
            "DERIVED",
            "DETERMINISTIC_SCENARIO",
        }:
            raise ValueError("unknown structured metric provenance")
        if len(self.input_record_ids) != len(set(self.input_record_ids)):
            raise ValueError("structured metric input record ids must be unique")
        if self.provenance in {"DERIVED", "DETERMINISTIC_SCENARIO"} and not self.input_record_ids:
            raise ValueError("derived structured metric requires input lineage")
        if self.score_authority:
            raise ValueError("structured metric records cannot directly assign score")
        if bool(self.metadata.get("snippet_only")):
            raise ValueError("snippet-only data cannot become a structured metric")
        if self.dataset == "VALUATION" and bool(
            self.metadata.get("generic_article_claim")
        ):
            raise ValueError("generic article claims cannot become valuation records")
        object.__setattr__(self, "available_at", self.available_at or self.observed_at)
        object.__setattr__(self, "input_record_ids", tuple(self.input_record_ids))
        object.__setattr__(self, "metadata", dict(self.metadata))

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StructuredResearchResult:
    status: str
    records: tuple[StructuredMetricRecord, ...]
    covered_roles_by_component: Mapping[str, tuple[str, ...]]
    missing_roles_by_component: Mapping[str, tuple[str, ...]]
    fallback_routes_required: tuple[str, ...]
    score_authority: bool = False

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "SOURCE_PENDING"}:
            raise ValueError("unknown structured research status")
        if self.status == "COMPLETE" and any(self.missing_roles_by_component.values()):
            raise ValueError("complete structured research cannot have missing roles")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "records": [row.to_dict() for row in self.records],
            "covered_roles_by_component": {
                key: list(value)
                for key, value in self.covered_roles_by_component.items()
            },
            "missing_roles_by_component": {
                key: list(value)
                for key, value in self.missing_roles_by_component.items()
            },
            "fallback_routes_required": list(self.fallback_routes_required),
            "score_authority": self.score_authority,
        }


class StructuredDataResearcher:
    """Validates records and reports gaps; a connector gap never means 0 points."""

    def assess(
        self,
        *,
        target_id: str,
        as_of_date: str,
        records: Sequence[StructuredMetricRecord | Mapping[str, Any]],
        required_roles_by_component: Mapping[str, Sequence[str]],
        fallback_routes: Sequence[str] = (
            "COMPANYGUIDE",
            "PUBLIC_BROKER_REPORT",
            "ISSUER_GUIDANCE",
            "DART_ACTUALS_DETERMINISTIC_SCENARIO",
            "KRX_PRICE_MARKET_CAP",
        ),
    ) -> StructuredResearchResult:
        compiled = tuple(_coerce_record(row) for row in records)
        ids = [row.record_id for row in compiled]
        if len(ids) != len(set(ids)):
            raise ValueError("structured record ids must be unique")
        if any(row.target_id != target_id for row in compiled):
            raise ValueError("structured researcher received cross-target data")
        if any(row.as_of_date != as_of_date for row in compiled):
            raise ValueError("structured record as_of_date mismatch")
        covered_roles = {
            role for row in compiled for role in row.evidence_roles
        }
        covered_by_component = {}
        missing_by_component = {}
        for component_id, required in required_roles_by_component.items():
            required_set = set(required)
            covered_by_component[component_id] = tuple(
                sorted(required_set & covered_roles)
            )
            missing_by_component[component_id] = tuple(
                sorted(required_set - covered_roles)
            )
        any_missing = any(missing_by_component.values())
        return StructuredResearchResult(
            status="SOURCE_PENDING" if any_missing else "COMPLETE",
            records=compiled,
            covered_roles_by_component=covered_by_component,
            missing_roles_by_component=missing_by_component,
            fallback_routes_required=(
                tuple(dict.fromkeys(fallback_routes)) if any_missing else ()
            ),
        )


def _coerce_record(
    row: StructuredMetricRecord | Mapping[str, Any],
) -> StructuredMetricRecord:
    if isinstance(row, StructuredMetricRecord):
        return row
    payload = dict(row)
    payload["evidence_roles"] = tuple(payload.get("evidence_roles") or ())
    payload["source_ids"] = tuple(payload.get("source_ids") or ())
    return StructuredMetricRecord(**payload)


__all__ = [
    "BROKER_VALUATION_FACT_RECORD_CONTRACTS",
    "BROKER_VALUATION_QUOTE_METRIC_PATTERNS",
    "StructuredDataResearcher",
    "StructuredMetricRecord",
    "StructuredResearchResult",
    "broker_valuation_forward_period_end",
    "broker_valuation_quote_matches_claim",
]
