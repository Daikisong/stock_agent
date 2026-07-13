"""Point-in-time structured financial, consensus, and valuation research.

This module deliberately stops before component scoring.  It turns typed
source rows into source-backed metrics, derives only reproducible arithmetic,
and reports unresolved source roles as pending.  A connector failure therefore
cannot silently become a zero component score.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
import hashlib
import math
from pathlib import Path
from statistics import median
from typing import Any, Mapping, Protocol, Sequence

from e2r.models import (
    ConsensusRevision,
    ConsensusSnapshot,
    FinancialActual,
    PriceBar,
    ResearchReport,
)
from e2r.production.metadata import write_jsonl

from .structured_data_researcher import StructuredMetricRecord
from .prompt_projection import project_structured_records


STRUCTURED_FINANCIAL_OUTPUT_FILES: Mapping[str, str] = {
    "FINANCIAL": "structured_financial_records.jsonl",
    "CONSENSUS_REVISION": "consensus_revision_records.jsonl",
    "VALUATION": "valuation_records.jsonl",
}

CANONICAL_STRUCTURED_SOURCE_ROUTES = (
    "COMPANYGUIDE",
    "PUBLIC_BROKER_REPORT",
    "ISSUER_GUIDANCE",
    "DART_ACTUALS_DETERMINISTIC_SCENARIO",
    "KRX_PRICE_MARKET_CAP",
)

STRUCTURED_ROUTE_CAPABILITIES: Mapping[str, tuple[str, ...]] = {
    "COMPANYGUIDE": ("CONSENSUS", "REVISION", "VALUATION"),
    "PUBLIC_BROKER_REPORT": ("CONSENSUS", "REVISION", "VALUATION"),
    "ISSUER_GUIDANCE": ("FINANCIAL", "GUIDANCE"),
    "DART_ACTUALS_DETERMINISTIC_SCENARIO": (
        "FINANCIAL",
        "FCF",
        "VALUATION",
        "SCENARIO",
    ),
    "KRX_PRICE_MARKET_CAP": (
        "PRICE",
        "MARKET_CAP",
        "MARKET_REACTION",
        "VALUATION",
    ),
    "NAVER_FINANCE": ("CONSENSUS", "VALUATION"),
    "CONSENSUS_CSV": ("CONSENSUS", "REVISION", "VALUATION"),
    "PEER_STRUCTURED": ("VALUATION", "PEER_BAND"),
}

PHASE86_REQUIRED_ROLES_BY_COMPONENT: Mapping[str, tuple[str, ...]] = {
    "eps_fcf_explosion": (
        "LATEST_ACTUAL_REVENUE",
        "LATEST_ACTUAL_OPERATING_PROFIT",
        "LATEST_ACTUAL_NET_INCOME",
        "OPERATING_CASH_FLOW",
        "CAPEX",
        "FREE_CASH_FLOW",
        "SEGMENT_CONTRIBUTION",
        "YOY_GROWTH",
        "QOQ_GROWTH",
        "FORWARD_GUIDANCE",
    ),
    "market_mispricing": (
        "CONSENSUS_HISTORY",
        "EPS_REVISION",
        "OPERATING_PROFIT_REVISION",
        "EARNINGS_SURPRISE",
        "PRICE_REACTION",
        "RELATIVE_PERFORMANCE",
    ),
    "valuation_rerating": (
        "CURRENT_PRICE",
        "MARKET_CAP",
        "NET_CASH_DEBT",
        "FORWARD_EPS",
        "FORWARD_FCF",
        "FORWARD_BOOK_VALUE",
        "FORWARD_PE",
        "FORWARD_PB",
        "FORWARD_EV_EBITDA",
        "FORWARD_FCF_YIELD",
        "OWN_HISTORICAL_BAND",
        "PEER_BAND",
        "SCENARIO_SENSITIVITY",
    ),
}

PHASE86_COMPONENT_ROLE_COMPATIBILITY: Mapping[str, tuple[str, ...]] = {
    "ACTUAL_EARNINGS": (
        "LATEST_ACTUAL_REVENUE",
        "LATEST_ACTUAL_OPERATING_PROFIT",
        "LATEST_ACTUAL_NET_INCOME",
    ),
    "FORWARD_REVISION": (
        "CONSENSUS_HISTORY",
        "EPS_REVISION",
        "OPERATING_PROFIT_REVISION",
        "FCF_REVISION",
    ),
    "CASH_CONVERSION": (
        "OPERATING_CASH_FLOW",
        "CAPEX",
        "FREE_CASH_FLOW",
    ),
    "CURRENT_VALUATION": (
        "CURRENT_PRICE",
        "MARKET_CAP",
        "FORWARD_PE",
        "FORWARD_PB",
        "FORWARD_EV_EBITDA",
        "FORWARD_FCF_YIELD",
    ),
    "EARNINGS_REVISION": (
        "EPS_REVISION",
        "OPERATING_PROFIT_REVISION",
        "FCF_REVISION",
    ),
    "CAPEX_SUPPLY_RESPONSE": ("CAPEX",),
    "DURABLE_VISIBILITY": ("FORWARD_GUIDANCE",),
}


@dataclass(frozen=True)
class PeerValuationObservation:
    peer_id: str
    as_of_date: str
    metric_id: str
    value: float
    unit: str
    observed_at: str
    source_ids: tuple[str, ...]
    source_route: str
    confidence: float = 0.9
    metadata: Mapping[str, Any] = field(default_factory=dict)
    schema_version: str = "e2r_peer_valuation_observation_v1"

    def __post_init__(self) -> None:
        if not self.peer_id or not self.metric_id or not self.unit:
            raise ValueError("peer valuation identity is required")
        cutoff = date.fromisoformat(self.as_of_date)
        if date.fromisoformat(self.observed_at[:10]) > cutoff:
            raise ValueError("peer valuation leaks future observations")
        if not math.isfinite(float(self.value)):
            raise ValueError("peer valuation value must be finite")
        if not self.source_ids or len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("peer valuation requires unique source lineage")
        if not 0.0 <= float(self.confidence) <= 1.0:
            raise ValueError("peer valuation confidence is invalid")
        if bool(self.metadata.get("snippet_only")) or bool(
            self.metadata.get("generic_article_claim")
        ):
            raise ValueError("unstructured article data cannot become a peer valuation")
        object.__setattr__(self, "source_ids", tuple(self.source_ids))
        object.__setattr__(self, "metadata", dict(self.metadata))

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SegmentFinancialObservation:
    target_id: str
    as_of_date: str
    segment_id: str
    metric_id: str
    value: float
    unit: str
    period: str
    observed_at: str
    available_at: str
    source_ids: tuple[str, ...]
    source_route: str
    total_company_value: float | None = None
    contribution_pct: float | None = None
    confidence: float = 0.95
    metadata: Mapping[str, Any] = field(default_factory=dict)
    schema_version: str = "e2r_segment_financial_observation_v1"

    def __post_init__(self) -> None:
        if not all(
            str(value).strip()
            for value in (
                self.target_id,
                self.segment_id,
                self.metric_id,
                self.unit,
                self.period,
                self.source_route,
            )
        ):
            raise ValueError("segment financial identity is required")
        cutoff = date.fromisoformat(self.as_of_date)
        observed = date.fromisoformat(self.observed_at[:10])
        available = date.fromisoformat(self.available_at[:10])
        if observed > cutoff or available > cutoff or available < observed:
            raise ValueError("segment financial observation violates as_of_date")
        for value in (self.value, self.total_company_value, self.contribution_pct):
            if value is not None and not math.isfinite(float(value)):
                raise ValueError("segment financial values must be finite")
        if self.contribution_pct is not None and not 0.0 <= self.contribution_pct <= 100.0:
            raise ValueError("segment contribution percent is invalid")
        if not self.source_ids or len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("segment financial observation requires source lineage")
        if bool(self.metadata.get("snippet_only")):
            raise ValueError("snippet cannot become segment financial data")
        object.__setattr__(self, "source_ids", tuple(self.source_ids))
        object.__setattr__(self, "metadata", dict(self.metadata))

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ForwardGuidanceObservation:
    target_id: str
    as_of_date: str
    metric_id: str
    unit: str
    period: str
    observed_at: str
    available_at: str
    source_ids: tuple[str, ...]
    source_route: str
    low_value: float | None = None
    high_value: float | None = None
    midpoint_value: float | None = None
    guidance_status: str = "ISSUER_GUIDANCE"
    confidence: float = 0.95
    metadata: Mapping[str, Any] = field(default_factory=dict)
    schema_version: str = "e2r_forward_guidance_observation_v1"

    def __post_init__(self) -> None:
        if not all(
            str(value).strip()
            for value in (
                self.target_id,
                self.metric_id,
                self.unit,
                self.period,
                self.source_route,
            )
        ):
            raise ValueError("forward guidance identity is required")
        values = (self.low_value, self.high_value, self.midpoint_value)
        if all(value is None for value in values):
            raise ValueError("forward guidance requires a point or range")
        if any(value is not None and not math.isfinite(float(value)) for value in values):
            raise ValueError("forward guidance values must be finite")
        if (
            self.low_value is not None
            and self.high_value is not None
            and self.low_value > self.high_value
        ):
            raise ValueError("forward guidance low cannot exceed high")
        cutoff = date.fromisoformat(self.as_of_date)
        observed = date.fromisoformat(self.observed_at[:10])
        available = date.fromisoformat(self.available_at[:10])
        if observed > cutoff or available > cutoff or available < observed:
            raise ValueError("forward guidance violates as_of_date")
        if self.guidance_status not in {
            "ISSUER_GUIDANCE",
            "ISSUER_OUTLOOK",
            "WITHDRAWN_GUIDANCE",
        }:
            raise ValueError("unknown forward guidance status")
        if not self.source_ids or len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("forward guidance requires source lineage")
        if bool(self.metadata.get("snippet_only")):
            raise ValueError("snippet cannot become forward guidance")
        object.__setattr__(self, "source_ids", tuple(self.source_ids))
        object.__setattr__(self, "metadata", dict(self.metadata))

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StructuredSourcePayload:
    route_name: str
    source_ids: tuple[str, ...] = ()
    financial_actuals: tuple[FinancialActual, ...] = ()
    consensus_snapshots: tuple[ConsensusSnapshot, ...] = ()
    consensus_revisions: tuple[ConsensusRevision, ...] = ()
    research_reports: tuple[ResearchReport, ...] = ()
    price_bars: tuple[PriceBar, ...] = ()
    structured_records: tuple[StructuredMetricRecord, ...] = ()
    peer_valuations: tuple[PeerValuationObservation, ...] = ()
    segment_observations: tuple[SegmentFinancialObservation, ...] = ()
    guidance_observations: tuple[ForwardGuidanceObservation, ...] = ()
    diagnostics: Mapping[str, Any] = field(default_factory=dict)
    schema_version: str = "e2r_structured_source_payload_v1"

    def __post_init__(self) -> None:
        if not self.route_name:
            raise ValueError("structured source route name is required")
        has_rows = any(
            (
                self.financial_actuals,
                self.consensus_snapshots,
                self.consensus_revisions,
                self.research_reports,
                self.price_bars,
                self.structured_records,
                self.peer_valuations,
                self.segment_observations,
                self.guidance_observations,
            )
        )
        if has_rows and not self.source_ids:
            raise ValueError("non-empty structured source payload requires source ids")
        if len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("structured source ids must be unique")
        object.__setattr__(self, "source_ids", tuple(self.source_ids))
        object.__setattr__(self, "financial_actuals", tuple(self.financial_actuals))
        object.__setattr__(self, "consensus_snapshots", tuple(self.consensus_snapshots))
        object.__setattr__(self, "consensus_revisions", tuple(self.consensus_revisions))
        object.__setattr__(self, "research_reports", tuple(self.research_reports))
        object.__setattr__(self, "price_bars", tuple(self.price_bars))
        object.__setattr__(self, "structured_records", tuple(self.structured_records))
        object.__setattr__(self, "peer_valuations", tuple(self.peer_valuations))
        object.__setattr__(self, "segment_observations", tuple(self.segment_observations))
        object.__setattr__(self, "guidance_observations", tuple(self.guidance_observations))
        object.__setattr__(self, "diagnostics", dict(self.diagnostics))

    @property
    def row_count(self) -> int:
        return sum(
            len(value)
            for value in (
                self.financial_actuals,
                self.consensus_snapshots,
                self.consensus_revisions,
                self.research_reports,
                self.price_bars,
                self.structured_records,
                self.peer_valuations,
                self.segment_observations,
                self.guidance_observations,
            )
        )


class StructuredSourceRoute(Protocol):
    route_name: str

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        ...


@dataclass(frozen=True)
class StructuredSourceAttempt:
    route_name: str
    status: str
    capabilities: tuple[str, ...]
    source_ids: tuple[str, ...]
    input_row_count: int
    accepted_record_count: int
    rejection_count: int
    error: str | None = None
    score_authority: bool = False
    schema_version: str = "e2r_structured_source_attempt_v1"

    def __post_init__(self) -> None:
        if self.status not in {
            "FETCHED",
            "NO_RESULT",
            "PARTIAL",
            "REJECTED",
            "PROVIDER_ERROR",
            "NOT_CONFIGURED",
        }:
            raise ValueError("unknown structured source attempt status")
        if self.score_authority:
            raise ValueError("source attempts cannot assign score")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StructuredRecordRejection:
    route_name: str
    row_kind: str
    row_identity: str
    reason: str
    schema_version: str = "e2r_structured_record_rejection_v1"

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StructuredEngineResult:
    target_id: str
    symbol: str
    as_of_date: str
    status: str
    records: tuple[StructuredMetricRecord, ...]
    source_attempts: tuple[StructuredSourceAttempt, ...]
    rejections: tuple[StructuredRecordRejection, ...]
    covered_roles_by_component: Mapping[str, tuple[str, ...]]
    missing_roles_by_component: Mapping[str, tuple[str, ...]]
    component_disposition_by_component: Mapping[str, str]
    deep_researched_canary_valuation_route_not_attempted_count: int
    revision_component_zero_solely_due_connector_gap_count: int
    fcf_component_zero_solely_due_missing_parser_count: int
    score_authority: bool = False
    schema_version: str = "e2r_structured_financial_engine_result_v1"

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "SOURCE_PENDING"}:
            raise ValueError("unknown structured engine status")
        if self.score_authority:
            raise ValueError("structured research cannot directly assign score")
        if self.status == "COMPLETE" and any(self.missing_roles_by_component.values()):
            raise ValueError("complete structured engine result has missing roles")
        if any(value == "ZERO" for value in self.component_disposition_by_component.values()):
            raise ValueError("connector gaps cannot finalize zero components")

    @property
    def financial_records(self) -> tuple[StructuredMetricRecord, ...]:
        return tuple(row for row in self.records if row.dataset == "FINANCIAL")

    @property
    def consensus_revision_records(self) -> tuple[StructuredMetricRecord, ...]:
        return tuple(
            row for row in self.records if row.dataset == "CONSENSUS_REVISION"
        )

    @property
    def valuation_records(self) -> tuple[StructuredMetricRecord, ...]:
        return tuple(row for row in self.records if row.dataset == "VALUATION")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "symbol": self.symbol,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "records": [row.to_dict() for row in self.records],
            "source_attempts": [row.to_dict() for row in self.source_attempts],
            "rejections": [row.to_dict() for row in self.rejections],
            "covered_roles_by_component": {
                key: list(value) for key, value in self.covered_roles_by_component.items()
            },
            "missing_roles_by_component": {
                key: list(value) for key, value in self.missing_roles_by_component.items()
            },
            "component_disposition_by_component": dict(
                self.component_disposition_by_component
            ),
            "deep_researched_canary_valuation_route_not_attempted_count": self.deep_researched_canary_valuation_route_not_attempted_count,
            "revision_component_zero_solely_due_connector_gap_count": self.revision_component_zero_solely_due_connector_gap_count,
            "fcf_component_zero_solely_due_missing_parser_count": self.fcf_component_zero_solely_due_missing_parser_count,
            "score_authority": self.score_authority,
        }

    def to_prompt_projection(self) -> Mapping[str, Any]:
        """Account for every record without duplicating raw time series in prompts."""

        record_projection = project_structured_records(self.records)
        return {
            "schema_version": "e2r_v5_structured_engine_prompt_projection_v1",
            "target_id": self.target_id,
            "symbol": self.symbol,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "record_projection": record_projection,
            "records": [
                {
                    "transport_projection": True,
                    "record_count": record_projection["record_count"],
                    "record_roster_hash": record_projection[
                        "record_roster_hash"
                    ],
                    "full_records_persisted_outside_prompt": True,
                }
            ],
            "source_attempts": [row.to_dict() for row in self.source_attempts],
            "rejections": [row.to_dict() for row in self.rejections],
            "covered_roles_by_component": {
                key: list(value)
                for key, value in self.covered_roles_by_component.items()
            },
            "missing_roles_by_component": {
                key: list(value)
                for key, value in self.missing_roles_by_component.items()
            },
            "component_disposition_by_component": dict(
                self.component_disposition_by_component
            ),
            "deep_researched_canary_valuation_route_not_attempted_count": (
                self.deep_researched_canary_valuation_route_not_attempted_count
            ),
            "revision_component_zero_solely_due_connector_gap_count": (
                self.revision_component_zero_solely_due_connector_gap_count
            ),
            "fcf_component_zero_solely_due_missing_parser_count": (
                self.fcf_component_zero_solely_due_missing_parser_count
            ),
            "full_records_persisted_outside_prompt": True,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }

    def to_component_structured_metrics(
        self,
        requirements_by_component: Mapping[str, Sequence[str]] | None = None,
    ) -> Mapping[str, Mapping[str, Any]]:
        """Expose source-backed records to component researchers without points.

        The compatibility aliases only group evidence.  They never imply that
        a component is strong, complete, or worth any particular score.
        """

        requirements = {
            key: tuple(value)
            for key, value in (
                requirements_by_component or PHASE86_REQUIRED_ROLES_BY_COMPONENT
            ).items()
        }
        payloads: dict[str, dict[str, Any]] = {}
        for component_id, required_roles in requirements.items():
            component_payload: dict[str, Any] = {}
            for required_role in required_roles:
                compatible = {
                    required_role,
                    *PHASE86_COMPONENT_ROLE_COMPATIBILITY.get(required_role, ()),
                }
                matches = [
                    row
                    for row in self.records
                    if compatible & set(row.evidence_roles)
                ]
                if not matches:
                    continue
                component_payload[required_role] = {
                    "evidence_role": required_role,
                    **project_structured_records(matches),
                    "source_pending": False,
                    "score_authority": False,
                }
            payloads[component_id] = component_payload
        return payloads


@dataclass(frozen=True)
class _TaggedRow:
    route_name: str
    source_ids: tuple[str, ...]
    value: Any


class StructuredFinancialConsensusValuationEngine:
    """Compile all attempted structured routes without score mutation."""

    def research(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: str | date,
        routes: Sequence[StructuredSourceRoute],
        required_roles_by_component: Mapping[str, Sequence[str]] | None = None,
        deep_researched_canary: bool = False,
    ) -> StructuredEngineResult:
        cutoff = (
            as_of_date if type(as_of_date) is date else date.fromisoformat(str(as_of_date))
        )
        if not target_id or not symbol or not company_name:
            raise ValueError("structured research target identity is required")
        route_names = [route.route_name for route in routes]
        if len(route_names) != len(set(route_names)):
            raise ValueError("structured source routes must be unique per run")

        records: list[StructuredMetricRecord] = []
        rejections: list[StructuredRecordRejection] = []
        attempts: list[StructuredSourceAttempt] = []
        actuals: list[_TaggedRow] = []
        consensus: list[_TaggedRow] = []
        revisions: list[_TaggedRow] = []
        reports: list[_TaggedRow] = []
        prices: list[_TaggedRow] = []
        peers: list[_TaggedRow] = []

        for route in routes:
            before_records = len(records)
            before_rejections = len(rejections)
            try:
                payload = route.fetch(
                    target_id=target_id,
                    symbol=symbol,
                    company_name=company_name,
                    as_of_date=cutoff,
                )
                if payload.route_name != route.route_name:
                    raise ValueError("structured route returned a mismatched route name")
                self._compile_payload(
                    payload=payload,
                    target_id=target_id,
                    symbol=symbol,
                    cutoff=cutoff,
                    records=records,
                    rejections=rejections,
                    actuals=actuals,
                    consensus=consensus,
                    revisions=revisions,
                    reports=reports,
                    prices=prices,
                    peers=peers,
                )
                accepted = len(records) - before_records
                rejected = len(rejections) - before_rejections
                status = (
                    "PARTIAL"
                    if accepted and rejected
                    else "REJECTED"
                    if rejected
                    else "FETCHED"
                    if accepted or payload.row_count
                    else "NO_RESULT"
                )
                attempts.append(
                    StructuredSourceAttempt(
                        route_name=route.route_name,
                        status=status,
                        capabilities=STRUCTURED_ROUTE_CAPABILITIES.get(
                            route.route_name, ()
                        ),
                        source_ids=payload.source_ids,
                        input_row_count=payload.row_count,
                        accepted_record_count=accepted,
                        rejection_count=rejected,
                    )
                )
            except Exception as exc:
                attempts.append(
                    StructuredSourceAttempt(
                        route_name=route.route_name,
                        status="PROVIDER_ERROR",
                        capabilities=STRUCTURED_ROUTE_CAPABILITIES.get(
                            route.route_name, ()
                        ),
                        source_ids=(),
                        input_row_count=0,
                        accepted_record_count=0,
                        rejection_count=0,
                        error=f"{type(exc).__name__}: {exc}",
                    )
                )

        configured = set(route_names)
        for route_name in CANONICAL_STRUCTURED_SOURCE_ROUTES:
            if route_name not in configured:
                attempts.append(
                    StructuredSourceAttempt(
                        route_name=route_name,
                        status="NOT_CONFIGURED",
                        capabilities=STRUCTURED_ROUTE_CAPABILITIES[route_name],
                        source_ids=(),
                        input_row_count=0,
                        accepted_record_count=0,
                        rejection_count=0,
                        error="structured_route_not_configured",
                    )
                )

        records.extend(_derive_missing_fcf_records(target_id, cutoff, records))
        records.extend(self._derive_growth_records(target_id, cutoff, actuals, records))
        records.extend(
            self._derive_consensus_history_records(target_id, cutoff, consensus, records)
        )
        records.extend(
            self._derive_earnings_surprise_records(
                target_id, cutoff, actuals, consensus, records
            )
        )
        records.extend(
            self._derive_market_reaction_records(
                target_id, symbol, cutoff, actuals, prices, records
            )
        )
        records.extend(
            self._derive_valuation_records(
                target_id=target_id,
                symbol=symbol,
                cutoff=cutoff,
                actuals=actuals,
                consensus=consensus,
                prices=prices,
                peers=peers,
                existing=records,
            )
        )
        compiled = _dedupe_records(records)

        requirements = {
            key: tuple(value)
            for key, value in (
                required_roles_by_component or PHASE86_REQUIRED_ROLES_BY_COMPONENT
            ).items()
        }
        covered_roles = {role for row in compiled for role in row.evidence_roles}
        covered_by_component = {
            component_id: tuple(sorted(set(required) & covered_roles))
            for component_id, required in requirements.items()
        }
        missing_by_component = {
            component_id: tuple(sorted(set(required) - covered_roles))
            for component_id, required in requirements.items()
        }
        pending = any(missing_by_component.values())
        dispositions = {
            component_id: (
                "PROVIDER_SOURCE_PENDING" if missing else "RESEARCH_READY"
            )
            for component_id, missing in missing_by_component.items()
        }
        valuation_attempted = any(
            attempt.status != "NOT_CONFIGURED"
            and "VALUATION" in attempt.capabilities
            for attempt in attempts
        )
        fcf_present = "FREE_CASH_FLOW" in covered_roles
        fcf_derivable_input_present = all(
            role in covered_roles for role in ("OPERATING_CASH_FLOW", "CAPEX")
        )
        revision_missing = not (
            {"EPS_REVISION", "OPERATING_PROFIT_REVISION"} & covered_roles
        )
        revision_connector_gap = any(
            "REVISION" in attempt.capabilities
            and attempt.status
            in {"NO_RESULT", "REJECTED", "PROVIDER_ERROR", "NOT_CONFIGURED"}
            for attempt in attempts
        )
        return StructuredEngineResult(
            target_id=target_id,
            symbol=symbol,
            as_of_date=cutoff.isoformat(),
            status="SOURCE_PENDING" if pending else "COMPLETE",
            records=compiled,
            source_attempts=tuple(attempts),
            rejections=tuple(rejections),
            covered_roles_by_component=covered_by_component,
            missing_roles_by_component=missing_by_component,
            component_disposition_by_component=dispositions,
            deep_researched_canary_valuation_route_not_attempted_count=int(
                deep_researched_canary and not valuation_attempted
            ),
            revision_component_zero_solely_due_connector_gap_count=int(
                revision_missing
                and revision_connector_gap
                and dispositions.get("market_mispricing") == "ZERO"
            ),
            fcf_component_zero_solely_due_missing_parser_count=int(
                fcf_derivable_input_present and not fcf_present
            ),
        )

    def _compile_payload(
        self,
        *,
        payload: StructuredSourcePayload,
        target_id: str,
        symbol: str,
        cutoff: date,
        records: list[StructuredMetricRecord],
        rejections: list[StructuredRecordRejection],
        actuals: list[_TaggedRow],
        consensus: list[_TaggedRow],
        revisions: list[_TaggedRow],
        reports: list[_TaggedRow],
        prices: list[_TaggedRow],
        peers: list[_TaggedRow],
    ) -> None:
        for item in payload.financial_actuals:
            identity = _actual_period(item)
            reason = _financial_actual_rejection(item, symbol=symbol, cutoff=cutoff)
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name, "FinancialActual", identity, reason
                    )
                )
                continue
            tagged = _TaggedRow(payload.route_name, payload.source_ids, item)
            actuals.append(tagged)
            records.extend(
                _records_from_actual(
                    target_id=target_id,
                    cutoff=cutoff,
                    tagged=tagged,
                )
            )

        for item in payload.consensus_snapshots:
            identity = f"{item.fiscal_year}:{item.date.isoformat()}:{item.source}"
            reason = _consensus_rejection(item, symbol=symbol, cutoff=cutoff)
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name, "ConsensusSnapshot", identity, reason
                    )
                )
                continue
            tagged = _TaggedRow(payload.route_name, payload.source_ids, item)
            consensus.append(tagged)
            records.extend(
                _records_from_consensus(
                    target_id=target_id,
                    cutoff=cutoff,
                    tagged=tagged,
                )
            )

        for item in payload.consensus_revisions:
            identity = f"{item.fiscal_year}:{item.date.isoformat()}:{item.source}"
            reason = _revision_rejection(item, symbol=symbol, cutoff=cutoff)
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name, "ConsensusRevision", identity, reason
                    )
                )
                continue
            tagged = _TaggedRow(payload.route_name, payload.source_ids, item)
            revisions.append(tagged)
            records.extend(
                _records_from_revision(
                    target_id=target_id,
                    cutoff=cutoff,
                    tagged=tagged,
                )
            )

        for item in payload.research_reports:
            identity = f"{item.publish_date.isoformat()}:{item.broker}:{item.title}"
            reason = _report_rejection(
                item,
                symbol=symbol,
                cutoff=cutoff,
                route_name=payload.route_name,
            )
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name, "ResearchReport", identity, reason
                    )
                )
                continue
            tagged = _TaggedRow(payload.route_name, payload.source_ids, item)
            reports.append(tagged)
            records.extend(
                _records_from_report(
                    target_id=target_id,
                    cutoff=cutoff,
                    tagged=tagged,
                )
            )

        for item in payload.price_bars:
            identity = f"{item.symbol}:{item.date.isoformat()}"
            reason = _price_rejection(item, cutoff=cutoff)
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name, "PriceBar", identity, reason
                    )
                )
                continue
            prices.append(_TaggedRow(payload.route_name, payload.source_ids, item))

        for item in payload.structured_records:
            reason = _seed_record_rejection(
                item,
                target_id=target_id,
                cutoff=cutoff,
                route_name=payload.route_name,
            )
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name,
                        "StructuredMetricRecord",
                        item.record_id,
                        reason,
                    )
                )
                continue
            records.append(item)

        for item in payload.segment_observations:
            reason = _segment_rejection(
                item,
                target_id=target_id,
                cutoff=cutoff,
                route_name=payload.route_name,
            )
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name,
                        "SegmentFinancialObservation",
                        f"{item.segment_id}:{item.metric_id}:{item.period}",
                        reason,
                    )
                )
                continue
            records.extend(
                _records_from_segment(target_id=target_id, cutoff=cutoff, item=item)
            )

        for item in payload.guidance_observations:
            reason = _guidance_rejection(
                item,
                target_id=target_id,
                cutoff=cutoff,
                route_name=payload.route_name,
            )
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name,
                        "ForwardGuidanceObservation",
                        f"{item.metric_id}:{item.period}",
                        reason,
                    )
                )
                continue
            records.extend(
                _records_from_guidance(target_id=target_id, cutoff=cutoff, item=item)
            )

        for item in payload.peer_valuations:
            reason = _peer_rejection(item, cutoff=cutoff, route_name=payload.route_name)
            if reason:
                rejections.append(
                    StructuredRecordRejection(
                        payload.route_name,
                        "PeerValuationObservation",
                        f"{item.peer_id}:{item.metric_id}",
                        reason,
                    )
                )
                continue
            peers.append(_TaggedRow(payload.route_name, payload.source_ids, item))
            records.append(
                _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id=f"peer_{item.metric_id}",
                    value=item.value,
                    unit=item.unit,
                    period=item.observed_at[:10],
                    roles=("PEER_BAND_INPUT",),
                    source_ids=item.source_ids,
                    source_route=item.source_route,
                    observed_at=item.observed_at,
                    record_kind="PEER_VALUATION_OBSERVATION",
                    confidence=item.confidence,
                    dataset="VALUATION",
                    provenance="STRUCTURED_EXTRACTED",
                    metadata={
                        **dict(item.metadata),
                        "peer_id": item.peer_id,
                        "structured_source": True,
                    },
                )
            )

    def _derive_growth_records(
        self,
        target_id: str,
        cutoff: date,
        actuals: Sequence[_TaggedRow],
        existing: Sequence[StructuredMetricRecord],
    ) -> tuple[StructuredMetricRecord, ...]:
        selected = _best_actuals(actuals)
        derived: list[StructuredMetricRecord] = []
        fields = {
            "revenue": "sales",
            "operating_profit": "operating_profit",
            "net_income": "net_income",
            "operating_cash_flow": "cashflow_from_operations",
            "free_cash_flow": "fcf",
        }
        for key, current in selected.items():
            fiscal_year, quarter = key
            prior_year = selected.get((fiscal_year - 1, quarter))
            prior_quarter = selected.get(_previous_quarter_key(fiscal_year, quarter)) if quarter else None
            for metric_id, attribute in fields.items():
                current_value = _actual_metric_value(current.value, attribute)
                if current_value is None:
                    continue
                for suffix, comparator, role in (
                    ("yoy_pct", prior_year, "YOY_GROWTH"),
                    ("qoq_pct", prior_quarter, "QOQ_GROWTH"),
                ):
                    if comparator is None:
                        continue
                    prior_value = _actual_metric_value(comparator.value, attribute)
                    growth = _percent_change(current_value, prior_value)
                    if growth is None:
                        continue
                    current_period = _actual_period(current.value)
                    prior_period = _actual_period(comparator.value)
                    input_ids = tuple(
                        dict.fromkeys(
                            (
                                *_record_ids(existing, metric_id, current_period),
                                *_record_ids(existing, metric_id, prior_period),
                            )
                        )
                    )
                    if not input_ids:
                        input_ids = (
                            _stable_id("STRUCTURED-INPUT", metric_id, current_period),
                            _stable_id("STRUCTURED-INPUT", metric_id, prior_period),
                        )
                    derived.append(
                        _metric_record(
                            target_id=target_id,
                            cutoff=cutoff,
                            metric_id=f"{metric_id}_{suffix}",
                            value=round(growth, 6),
                            unit="PERCENT",
                            period=current_period,
                            roles=(role,),
                            source_ids=tuple(
                                dict.fromkeys(
                                    (*current.source_ids, *comparator.source_ids)
                                )
                            ),
                            source_route=f"{current.route_name}+{comparator.route_name}",
                            observed_at=max(
                                current.value.reported_at,
                                comparator.value.reported_at,
                            ).isoformat(),
                            record_kind="FINANCIAL_GROWTH",
                            confidence=min(
                                _route_confidence(current.route_name),
                                _route_confidence(comparator.route_name),
                            ),
                            dataset="FINANCIAL",
                            provenance="DERIVED",
                            input_record_ids=input_ids,
                            metadata={
                                "current_period": current_period,
                                "comparison_period": prior_period,
                                "formula": "(current / comparison - 1) * 100",
                            },
                        )
                    )
        return tuple(derived)

    def _derive_consensus_history_records(
        self,
        target_id: str,
        cutoff: date,
        consensus: Sequence[_TaggedRow],
        existing: Sequence[StructuredMetricRecord],
    ) -> tuple[StructuredMetricRecord, ...]:
        grouped: dict[tuple[str, int, str], list[_TaggedRow]] = {}
        for tagged in consensus:
            item: ConsensusSnapshot = tagged.value
            grouped.setdefault((item.source, item.fiscal_year, tagged.route_name), []).append(tagged)
        result: list[StructuredMetricRecord] = []
        fields = {
            "eps": ("eps_e", "EPS_REVISION"),
            "operating_profit": ("op_e", "OPERATING_PROFIT_REVISION"),
            "free_cash_flow": ("fcf_e", "FCF_REVISION"),
        }
        for (_, fiscal_year, route_name), rows in grouped.items():
            ordered = sorted(rows, key=lambda row: row.value.date)
            distinct_dates = sorted({row.value.date for row in ordered})
            if len(distinct_dates) < 2:
                continue
            earliest = next(row for row in ordered if row.value.date == distinct_dates[0])
            latest = next(row for row in reversed(ordered) if row.value.date == distinct_dates[-1])
            source_ids = tuple(dict.fromkeys((*earliest.source_ids, *latest.source_ids)))
            history_inputs = tuple(
                dict.fromkeys(
                    record_id
                    for metric_id in ("consensus_forward_eps", "consensus_forward_operating_profit", "consensus_forward_fcf")
                    for record_id in (
                        *_record_ids(existing, metric_id, f"FY{fiscal_year}E"),
                    )
                )
            ) or (
                _stable_id(
                    "STRUCTURED-INPUT",
                    route_name,
                    fiscal_year,
                    distinct_dates[0],
                    distinct_dates[-1],
                ),
            )
            result.append(
                _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id="consensus_history_span_days",
                    value=(distinct_dates[-1] - distinct_dates[0]).days,
                    unit="DAYS",
                    period=f"FY{fiscal_year}E",
                    roles=("CONSENSUS_HISTORY",),
                    source_ids=source_ids,
                    source_route=route_name,
                    observed_at=distinct_dates[-1].isoformat(),
                    record_kind="CONSENSUS_HISTORY",
                    confidence=min(
                        _route_confidence(earliest.route_name),
                        _route_confidence(latest.route_name),
                    ),
                    dataset="CONSENSUS_REVISION",
                    provenance="DERIVED",
                    input_record_ids=history_inputs,
                    metadata={
                        "observation_count": len(distinct_dates),
                        "first_observation": distinct_dates[0].isoformat(),
                        "last_observation": distinct_dates[-1].isoformat(),
                    },
                )
            )
            for label, (attribute, role) in fields.items():
                before = getattr(earliest.value, attribute)
                after = getattr(latest.value, attribute)
                change = _percent_change(after, before)
                if change is None:
                    continue
                input_ids = tuple(
                    dict.fromkeys(
                        (
                            *_record_ids(
                                existing,
                                f"consensus_forward_{label}",
                                f"FY{fiscal_year}E",
                            ),
                            *history_inputs,
                        )
                    )
                )
                result.append(
                    _metric_record(
                        target_id=target_id,
                        cutoff=cutoff,
                        metric_id=f"{label}_revision_history_pct",
                        value=round(change, 6),
                        unit="PERCENT",
                        period=f"FY{fiscal_year}E",
                        roles=(role, "CONSENSUS_HISTORY"),
                        source_ids=source_ids,
                        source_route=route_name,
                        observed_at=latest.value.date.isoformat(),
                        record_kind="EARNINGS_REVISION",
                        confidence=min(
                            _route_confidence(earliest.route_name),
                            _route_confidence(latest.route_name),
                        ),
                        dataset="CONSENSUS_REVISION",
                        provenance="DERIVED",
                        input_record_ids=input_ids or history_inputs,
                        metadata={
                            "revision_family": "EARNINGS",
                            "target_price_only": False,
                            "before": before,
                            "after": after,
                            "first_date": earliest.value.date.isoformat(),
                            "last_date": latest.value.date.isoformat(),
                        },
                    )
                )
        return tuple(result)

    def _derive_earnings_surprise_records(
        self,
        target_id: str,
        cutoff: date,
        actuals: Sequence[_TaggedRow],
        consensus: Sequence[_TaggedRow],
        existing: Sequence[StructuredMetricRecord],
    ) -> tuple[StructuredMetricRecord, ...]:
        result: list[StructuredMetricRecord] = []
        selected = _best_actuals(actuals)
        fields = {
            "operating_profit": ("operating_profit", "op_e"),
            "net_income": ("net_income", "net_income_e"),
            "eps": ("eps", "eps_e"),
        }
        for actual in selected.values():
            item: FinancialActual = actual.value
            eligible = [
                row
                for row in consensus
                if row.value.fiscal_year == item.fiscal_year
                and row.value.date <= item.reported_at.date()
                and _consensus_quarter_matches(row.value, item.fiscal_quarter)
            ]
            if not eligible:
                continue
            estimate = max(eligible, key=lambda row: row.value.date)
            period = _actual_period(item)
            for label, (actual_attr, estimate_attr) in fields.items():
                actual_value = getattr(item, actual_attr)
                estimate_value = getattr(estimate.value, estimate_attr)
                surprise = _percent_change(actual_value, estimate_value)
                if surprise is None:
                    continue
                input_ids = tuple(
                    dict.fromkeys(
                        (
                            *_record_ids(existing, label, period),
                            *_record_ids(
                                existing,
                                f"consensus_forward_{'operating_profit' if label == 'operating_profit' else label}",
                                f"FY{item.fiscal_year}E",
                            ),
                        )
                    )
                ) or (
                    _stable_id("STRUCTURED-INPUT", "actual", label, period),
                    _stable_id(
                        "STRUCTURED-INPUT",
                        "consensus",
                        label,
                        item.fiscal_year,
                        estimate.value.date,
                    ),
                )
                result.append(
                    _metric_record(
                        target_id=target_id,
                        cutoff=cutoff,
                        metric_id=f"{label}_earnings_surprise_pct",
                        value=round(surprise, 6),
                        unit="PERCENT",
                        period=period,
                        roles=("EARNINGS_SURPRISE",),
                        source_ids=tuple(
                            dict.fromkeys((*actual.source_ids, *estimate.source_ids))
                        ),
                        source_route=f"{actual.route_name}+{estimate.route_name}",
                        observed_at=item.reported_at.isoformat(),
                        record_kind="EARNINGS_SURPRISE",
                        confidence=min(
                            _route_confidence(actual.route_name),
                            _route_confidence(estimate.route_name),
                        ),
                        dataset="CONSENSUS_REVISION",
                        provenance="DERIVED",
                        input_record_ids=input_ids,
                        metadata={
                            "actual_value": actual_value,
                            "consensus_value": estimate_value,
                            "consensus_date": estimate.value.date.isoformat(),
                            "consensus_was_known_before_actual": True,
                        },
                    )
                )
        return tuple(result)

    def _derive_market_reaction_records(
        self,
        target_id: str,
        symbol: str,
        cutoff: date,
        actuals: Sequence[_TaggedRow],
        prices: Sequence[_TaggedRow],
        existing: Sequence[StructuredMetricRecord],
    ) -> tuple[StructuredMetricRecord, ...]:
        target_prices = sorted(
            (row for row in prices if row.value.symbol == symbol),
            key=lambda row: row.value.date,
        )
        if not target_prices:
            return ()
        result: list[StructuredMetricRecord] = []
        latest_price = target_prices[-1]
        price_record = _metric_record(
            target_id=target_id,
            cutoff=cutoff,
            metric_id="current_price",
            value=latest_price.value.close,
            unit=(
                "KRW_PER_SHARE"
                if latest_price.route_name == "KRX_PRICE_MARKET_CAP"
                else "PRICE"
            ),
            period=latest_price.value.date.isoformat(),
            roles=("CURRENT_PRICE",),
            source_ids=latest_price.source_ids,
            source_route=latest_price.route_name,
            observed_at=latest_price.value.date.isoformat(),
            record_kind="MARKET_SNAPSHOT",
            confidence=_route_confidence(latest_price.route_name),
            dataset="VALUATION",
            provenance="OBSERVED",
            metadata={
                "symbol": symbol,
                "price_field": "close",
                "structured_source": True,
            },
        )
        result.append(price_record)
        if latest_price.value.market_cap is not None:
            result.append(
                _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id="market_cap",
                    value=latest_price.value.market_cap,
                    unit=(
                        "KRW"
                        if latest_price.route_name == "KRX_PRICE_MARKET_CAP"
                        else "CURRENCY"
                    ),
                    period=latest_price.value.date.isoformat(),
                    roles=("MARKET_CAP",),
                    source_ids=latest_price.source_ids,
                    source_route=latest_price.route_name,
                    observed_at=latest_price.value.date.isoformat(),
                    record_kind="MARKET_SNAPSHOT",
                    confidence=_route_confidence(latest_price.route_name),
                    dataset="VALUATION",
                    provenance="OBSERVED",
                    metadata={"symbol": symbol, "structured_source": True},
                )
            )

        selected_actuals = sorted(
            _best_actuals(actuals).values(), key=lambda row: row.value.reported_at
        )
        if selected_actuals:
            latest_actual = selected_actuals[-1]
            report_date = latest_actual.value.reported_at.date()
            before = [row for row in target_prices if row.value.date < report_date]
            # A filing can arrive after the close.  Without exchange-session
            # availability metadata, the first strictly later bar is the
            # conservative no-lookahead reaction anchor.
            after = [row for row in target_prices if row.value.date > report_date]
            if before and after:
                anchor = before[-1]
                for label, index in (("1d", 0), ("5d", 4)):
                    if len(after) <= index:
                        continue
                    end = after[index]
                    change = _percent_change(end.value.close, anchor.value.close)
                    if change is None:
                        continue
                    result.append(
                        _metric_record(
                            target_id=target_id,
                            cutoff=cutoff,
                            metric_id=f"price_reaction_{label}_pct",
                            value=round(change, 6),
                            unit="PERCENT",
                            period=report_date.isoformat(),
                            roles=("PRICE_REACTION",),
                            source_ids=tuple(
                                dict.fromkeys(
                                    (
                                        *anchor.source_ids,
                                        *end.source_ids,
                                        *latest_actual.source_ids,
                                    )
                                )
                            ),
                            source_route=f"{latest_actual.route_name}+{end.route_name}",
                            observed_at=end.value.date.isoformat(),
                            record_kind="MARKET_EXPECTATION_REACTION",
                            confidence=min(
                                _route_confidence(latest_actual.route_name),
                                _route_confidence(end.route_name),
                            ),
                            dataset="CONSENSUS_REVISION",
                            provenance="DERIVED",
                            input_record_ids=(
                                _price_bar_input_id(anchor.value),
                                _price_bar_input_id(end.value),
                                _stable_id(
                                    "STRUCTURED-INPUT",
                                    "actual-release",
                                    _actual_period(latest_actual.value),
                                ),
                            ),
                            metadata={
                                "release_date": report_date.isoformat(),
                                "same_day_bar_excluded_without_session_timestamp": True,
                                "start_price_date": anchor.value.date.isoformat(),
                                "end_price_date": end.value.date.isoformat(),
                            },
                        )
                    )

        benchmark_symbols = sorted(
            {row.value.symbol for row in prices if row.value.symbol != symbol}
        )
        if benchmark_symbols:
            lookback_target = _bar_on_or_before(
                target_prices, latest_price.value.date.toordinal() - 28
            )
            if lookback_target is not None:
                for benchmark_symbol in benchmark_symbols:
                    benchmark = sorted(
                        (
                            row
                            for row in prices
                            if row.value.symbol == benchmark_symbol
                        ),
                        key=lambda row: row.value.date,
                    )
                    if not benchmark:
                        continue
                    benchmark_end = _bar_on_or_before(
                        benchmark, latest_price.value.date.toordinal()
                    )
                    benchmark_start = _bar_on_or_before(
                        benchmark, lookback_target.value.date.toordinal()
                    )
                    if benchmark_start is None or benchmark_end is None:
                        continue
                    target_return = _percent_change(
                        latest_price.value.close, lookback_target.value.close
                    )
                    benchmark_return = _percent_change(
                        benchmark_end.value.close, benchmark_start.value.close
                    )
                    if target_return is None or benchmark_return is None:
                        continue
                    result.append(
                        _metric_record(
                            target_id=target_id,
                            cutoff=cutoff,
                            metric_id="relative_performance_1m_pctp",
                            value=round(target_return - benchmark_return, 6),
                            unit="PERCENTAGE_POINT",
                            period=latest_price.value.date.isoformat(),
                            roles=("RELATIVE_PERFORMANCE",),
                            source_ids=tuple(
                                dict.fromkeys(
                                    (
                                        *lookback_target.source_ids,
                                        *latest_price.source_ids,
                                        *benchmark_start.source_ids,
                                        *benchmark_end.source_ids,
                                    )
                                )
                            ),
                            source_route=latest_price.route_name,
                            observed_at=latest_price.value.date.isoformat(),
                            record_kind="RELATIVE_MARKET_PERFORMANCE",
                            confidence=_route_confidence(latest_price.route_name),
                            dataset="CONSENSUS_REVISION",
                            provenance="DERIVED",
                            input_record_ids=(
                                _price_bar_input_id(lookback_target.value),
                                _price_bar_input_id(latest_price.value),
                                _price_bar_input_id(benchmark_start.value),
                                _price_bar_input_id(benchmark_end.value),
                            ),
                            metadata={
                                "benchmark_symbol": benchmark_symbol,
                                "target_return_pct": round(target_return, 6),
                                "benchmark_return_pct": round(
                                    benchmark_return, 6
                                ),
                            },
                        )
                    )
                    break
        return tuple(result)

    def _derive_valuation_records(
        self,
        *,
        target_id: str,
        symbol: str,
        cutoff: date,
        actuals: Sequence[_TaggedRow],
        consensus: Sequence[_TaggedRow],
        prices: Sequence[_TaggedRow],
        peers: Sequence[_TaggedRow],
        existing: Sequence[StructuredMetricRecord],
    ) -> tuple[StructuredMetricRecord, ...]:
        result: list[StructuredMetricRecord] = []
        current_price = _latest_metric(existing, ("current_price",))
        market_cap = _latest_metric(existing, ("market_cap",))
        latest_consensus = _latest_consensus(consensus, cutoff)
        forward_inputs: dict[str, StructuredMetricRecord] = {}
        if latest_consensus is not None:
            snapshot: ConsensusSnapshot = latest_consensus.value
            for metric_id, value, unit, role in (
                ("forward_eps", snapshot.eps_e, "CURRENCY_PER_SHARE", "FORWARD_EPS"),
                (
                    "forward_fcf",
                    snapshot.fcf_e,
                    _consensus_total_currency_unit(snapshot),
                    "FORWARD_FCF",
                ),
                ("forward_book_value", snapshot.bps_e, "CURRENCY_PER_SHARE", "FORWARD_BOOK_VALUE"),
                (
                    "forward_ebitda",
                    _number(snapshot.parsed_fields.get("ebitda_e")),
                    _consensus_total_currency_unit(snapshot),
                    "FORWARD_EBITDA",
                ),
            ):
                if value is None:
                    continue
                inputs = _record_ids(
                    existing,
                    {
                        "forward_eps": "consensus_forward_eps",
                        "forward_fcf": "consensus_forward_fcf",
                        "forward_book_value": "consensus_forward_book_value",
                        "forward_ebitda": "consensus_forward_ebitda",
                    }[metric_id],
                    f"FY{snapshot.fiscal_year}E",
                ) or (
                    _stable_id(
                        "STRUCTURED-INPUT",
                        latest_consensus.route_name,
                        metric_id,
                        snapshot.fiscal_year,
                        snapshot.date,
                    ),
                )
                record = _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id=metric_id,
                    value=value,
                    unit=unit,
                    period=f"FY{snapshot.fiscal_year}E",
                    roles=(role,),
                    source_ids=latest_consensus.source_ids,
                    source_route=latest_consensus.route_name,
                    observed_at=snapshot.date.isoformat(),
                    record_kind="VALUATION_FORWARD_INPUT",
                    confidence=_route_confidence(latest_consensus.route_name),
                    dataset="VALUATION",
                    provenance="DERIVED",
                    input_record_ids=inputs,
                    metadata={
                        "structured_source": True,
                        "consensus_source": snapshot.source,
                    },
                )
                result.append(record)
                forward_inputs[metric_id] = record

        for metric_id, aliases, role, unit in (
            (
                "forward_eps",
                (
                    "forward_eps",
                    "consensus_forward_eps",
                    "issuer_guidance_eps_midpoint",
                ),
                "FORWARD_EPS",
                "CURRENCY_PER_SHARE",
            ),
            (
                "forward_fcf",
                (
                    "forward_fcf",
                    "consensus_forward_fcf",
                    "issuer_guidance_fcf_midpoint",
                    "issuer_guidance_free_cash_flow_midpoint",
                ),
                "FORWARD_FCF",
                "CURRENCY",
            ),
            (
                "forward_book_value",
                (
                    "forward_book_value",
                    "forward_bv",
                    "consensus_forward_book_value",
                    "issuer_guidance_book_value_midpoint",
                ),
                "FORWARD_BOOK_VALUE",
                "CURRENCY_PER_SHARE",
            ),
            (
                "forward_ebitda",
                (
                    "forward_ebitda",
                    "consensus_forward_ebitda",
                    "issuer_guidance_ebitda_midpoint",
                ),
                "FORWARD_EBITDA",
                "CURRENCY",
            ),
        ):
            if metric_id in forward_inputs:
                continue
            source = _latest_metric(existing, aliases)
            if source is None:
                continue
            record = _copy_as_valuation_input(
                source,
                target_id=target_id,
                cutoff=cutoff,
                metric_id=metric_id,
                unit=source.unit or unit,
                role=role,
            )
            result.append(record)
            forward_inputs[metric_id] = record

        # DART actuals can support an explicitly labelled deterministic
        # forward scenario even when no provider publishes forward FCF.  Build
        # the scenarios before valuation multiples so the base-scenario FCF
        # can feed FCF yield instead of being generated too late to be used.
        scenario_records = _scenario_records(
            target_id=target_id,
            cutoff=cutoff,
            actuals=actuals,
            current_price=current_price,
            market_cap=market_cap,
            existing=(*existing, *result),
        )
        result.extend(scenario_records)
        if "forward_fcf" not in forward_inputs:
            scenario_fcf = _latest_metric(
                scenario_records, ("scenario_base_free_cash_flow",)
            )
            if scenario_fcf is not None:
                forward_fcf_record = _copy_as_valuation_input(
                    scenario_fcf,
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id="forward_fcf",
                    unit=scenario_fcf.unit,
                    role="FORWARD_FCF",
                )
                result.append(forward_fcf_record)
                forward_inputs["forward_fcf"] = forward_fcf_record

        net_debt = _latest_metric(existing, ("net_debt",))
        net_cash = _latest_metric(existing, ("net_cash",))
        if net_debt is None and net_cash is not None:
            net_debt = _derived_from_one(
                net_cash,
                target_id=target_id,
                cutoff=cutoff,
                metric_id="net_debt",
                value=-float(net_cash.value),
                unit=net_cash.unit,
                role="NET_CASH_DEBT",
                record_kind="VALUATION_BALANCE_SHEET",
            )
            result.append(net_debt)
        if net_debt is None:
            cash = _latest_metric(
                existing,
                ("cash_and_equivalents", "cash", "cash_equivalents"),
            )
            debt = _latest_metric(existing, ("total_debt", "interest_bearing_debt"))
            if cash is not None and debt is not None:
                net_debt = _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id="net_debt",
                    value=_amount_in_base(debt) - _amount_in_base(cash),
                    unit="BASE_CURRENCY",
                    period=max(cash.period, debt.period),
                    roles=("NET_CASH_DEBT",),
                    source_ids=tuple(dict.fromkeys((*cash.source_ids, *debt.source_ids))),
                    source_route=f"{cash.source_route}+{debt.source_route}",
                    observed_at=max(cash.observed_at, debt.observed_at),
                    record_kind="VALUATION_BALANCE_SHEET",
                    confidence=min(cash.confidence, debt.confidence),
                    dataset="VALUATION",
                    provenance="DERIVED",
                    input_record_ids=(cash.record_id, debt.record_id),
                    metadata={"formula": "total_debt - cash_and_equivalents"},
                )
                result.append(net_debt)
        elif "NET_CASH_DEBT" not in net_debt.evidence_roles:
            result.append(
                _copy_as_valuation_input(
                    net_debt,
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id="net_debt",
                    unit=net_debt.unit,
                    role="NET_CASH_DEBT",
                )
            )

        derived_multiples: dict[str, StructuredMetricRecord] = {}
        for metric_id, numerator, denominator, role, formula in (
            (
                "forward_pe",
                current_price,
                forward_inputs.get("forward_eps"),
                "FORWARD_PE",
                "current_price / forward_eps",
            ),
            (
                "forward_pb",
                current_price,
                forward_inputs.get("forward_book_value"),
                "FORWARD_PB",
                "current_price / forward_book_value",
            ),
        ):
            if numerator is None or denominator is None:
                continue
            value = _safe_divide(float(numerator.value), float(denominator.value))
            if value is None or value <= 0:
                continue
            record = _binary_derived_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id=metric_id,
                value=value,
                unit="MULTIPLE",
                role=role,
                left=numerator,
                right=denominator,
                formula=formula,
                record_kind="VALUATION_MULTIPLE",
            )
            result.append(record)
            derived_multiples[metric_id] = record

        forward_ebitda = forward_inputs.get("forward_ebitda")
        if (
            market_cap is not None
            and forward_ebitda is not None
            and net_debt is not None
        ):
            enterprise_value = _amount_in_base(market_cap) + _amount_in_base(
                net_debt
            )
            ratio = _safe_divide(enterprise_value, _amount_in_base(forward_ebitda))
            if ratio is not None and ratio > 0:
                input_rows = [market_cap, forward_ebitda]
                if net_debt is not None:
                    input_rows.append(net_debt)
                result.append(
                    _nary_derived_record(
                        target_id=target_id,
                        cutoff=cutoff,
                        metric_id="forward_ev_ebitda",
                        value=ratio,
                        unit="MULTIPLE",
                        role="FORWARD_EV_EBITDA",
                        inputs=input_rows,
                        formula="(market_cap + net_debt) / forward_ebitda",
                        record_kind="VALUATION_MULTIPLE",
                    )
                )

        forward_fcf = forward_inputs.get("forward_fcf")
        if market_cap is not None and forward_fcf is not None:
            fcf_yield = _safe_divide(
                _amount_in_base(forward_fcf) * 100.0,
                _amount_in_base(market_cap),
            )
            if fcf_yield is not None:
                result.append(
                    _binary_derived_record(
                        target_id=target_id,
                        cutoff=cutoff,
                        metric_id="forward_fcf_yield_pct",
                        value=fcf_yield,
                        unit="PERCENT",
                        role="FORWARD_FCF_YIELD",
                        left=forward_fcf,
                        right=market_cap,
                        formula="forward_fcf / market_cap * 100",
                        record_kind="VALUATION_MULTIPLE",
                    )
                )

        result.extend(
            _historical_band_records(
                target_id=target_id,
                cutoff=cutoff,
                existing=(*existing, *result),
                current_multiples=derived_multiples,
            )
        )
        result.extend(
            _peer_band_records(
                target_id=target_id,
                cutoff=cutoff,
                peers=peers,
                existing=(*existing, *result),
            )
        )
        return tuple(result)


def write_structured_financial_outputs(
    result: StructuredEngineResult,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    """Write the three canonical Phase 86 JSONL datasets."""

    root = Path(output_directory)
    paths = {
        dataset: root / filename
        for dataset, filename in STRUCTURED_FINANCIAL_OUTPUT_FILES.items()
    }
    rows_by_dataset = {
        "FINANCIAL": result.financial_records,
        "CONSENSUS_REVISION": result.consensus_revision_records,
        "VALUATION": result.valuation_records,
    }
    for dataset, path in paths.items():
        write_jsonl(path, (row.to_dict() for row in rows_by_dataset[dataset]))
    return paths


def _financial_actual_rejection(
    item: FinancialActual, *, symbol: str, cutoff: date
) -> str | None:
    if item.symbol != symbol:
        return "CROSS_TARGET_FINANCIAL_ACTUAL"
    if item.reported_at.date() > cutoff or item.as_of_date > cutoff:
        return "FUTURE_FINANCIAL_ACTUAL"
    if item.period_end > cutoff:
        return "FUTURE_FINANCIAL_PERIOD"
    return None


def _consensus_rejection(
    item: ConsensusSnapshot, *, symbol: str, cutoff: date
) -> str | None:
    if item.symbol != symbol:
        return "CROSS_TARGET_CONSENSUS"
    if item.date > cutoff or item.as_of_date > cutoff:
        return "FUTURE_CONSENSUS"
    return None


def _revision_rejection(
    item: ConsensusRevision, *, symbol: str, cutoff: date
) -> str | None:
    if item.symbol != symbol:
        return "CROSS_TARGET_REVISION"
    if item.date > cutoff or item.as_of_date > cutoff:
        return "FUTURE_REVISION"
    return None


def _report_rejection(
    item: ResearchReport,
    *,
    symbol: str,
    cutoff: date,
    route_name: str,
) -> str | None:
    if item.symbol != symbol:
        return "CROSS_TARGET_BROKER_REPORT"
    if item.publish_date > cutoff or item.as_of_date > cutoff:
        return "FUTURE_BROKER_REPORT"
    if route_name not in {"PUBLIC_BROKER_REPORT", "COMPANYGUIDE"}:
        return "UNTRUSTED_REPORT_ROUTE"
    if not item.raw_text and not any(
        bool(item.parsed_fields.get(key))
        for key in (
            "structured_consensus_source",
            "structured_consensus_revision_source",
            "source_backed_full_document",
            "report_id",
        )
    ):
        return "BROKER_REPORT_WITHOUT_FULL_OR_STRUCTURED_ANCHOR"
    return None


def _price_rejection(item: PriceBar, *, cutoff: date) -> str | None:
    if item.date > cutoff or item.as_of_date > cutoff:
        return "FUTURE_PRICE_BAR"
    return None


def _seed_record_rejection(
    item: StructuredMetricRecord,
    *,
    target_id: str,
    cutoff: date,
    route_name: str,
) -> str | None:
    if item.target_id != target_id:
        return "CROSS_TARGET_STRUCTURED_RECORD"
    if item.as_of_date != cutoff.isoformat():
        return "STRUCTURED_RECORD_AS_OF_MISMATCH"
    if date.fromisoformat(item.observed_at[:10]) > cutoff or date.fromisoformat(
        (item.available_at or item.observed_at)[:10]
    ) > cutoff:
        return "FUTURE_STRUCTURED_RECORD"
    if item.source_route != route_name:
        return "STRUCTURED_RECORD_ROUTE_MISMATCH"
    if item.dataset == "VALUATION":
        capabilities = STRUCTURED_ROUTE_CAPABILITIES.get(route_name, ())
        if "VALUATION" not in capabilities:
            return "NON_VALUATION_ROUTE_VALUATION_RECORD"
        if not bool(item.metadata.get("structured_source")) and item.provenance not in {
            "DERIVED",
            "DETERMINISTIC_SCENARIO",
        }:
            return "VALUATION_WITHOUT_STRUCTURED_SOURCE"
    return None


def _segment_rejection(
    item: SegmentFinancialObservation,
    *,
    target_id: str,
    cutoff: date,
    route_name: str,
) -> str | None:
    if item.target_id != target_id:
        return "CROSS_TARGET_SEGMENT_OBSERVATION"
    if item.as_of_date != cutoff.isoformat():
        return "SEGMENT_OBSERVATION_AS_OF_MISMATCH"
    if item.source_route != route_name:
        return "SEGMENT_OBSERVATION_ROUTE_MISMATCH"
    if date.fromisoformat(item.available_at[:10]) > cutoff:
        return "FUTURE_SEGMENT_OBSERVATION"
    return None


def _guidance_rejection(
    item: ForwardGuidanceObservation,
    *,
    target_id: str,
    cutoff: date,
    route_name: str,
) -> str | None:
    if item.target_id != target_id:
        return "CROSS_TARGET_FORWARD_GUIDANCE"
    if item.as_of_date != cutoff.isoformat():
        return "FORWARD_GUIDANCE_AS_OF_MISMATCH"
    if item.source_route != route_name:
        return "FORWARD_GUIDANCE_ROUTE_MISMATCH"
    if route_name != "ISSUER_GUIDANCE":
        return "FORWARD_GUIDANCE_REQUIRES_ISSUER_ROUTE"
    if date.fromisoformat(item.available_at[:10]) > cutoff:
        return "FUTURE_FORWARD_GUIDANCE"
    return None


def _peer_rejection(
    item: PeerValuationObservation, *, cutoff: date, route_name: str
) -> str | None:
    if item.as_of_date != cutoff.isoformat():
        return "PEER_VALUATION_AS_OF_MISMATCH"
    if date.fromisoformat(item.observed_at[:10]) > cutoff:
        return "FUTURE_PEER_VALUATION"
    if item.source_route != route_name:
        return "PEER_VALUATION_ROUTE_MISMATCH"
    if "VALUATION" not in STRUCTURED_ROUTE_CAPABILITIES.get(route_name, ()):
        return "NON_VALUATION_ROUTE_PEER_RECORD"
    return None


def _records_from_segment(
    *,
    target_id: str,
    cutoff: date,
    item: SegmentFinancialObservation,
) -> tuple[StructuredMetricRecord, ...]:
    base = _metric_record(
        target_id=target_id,
        cutoff=cutoff,
        metric_id=f"segment_{item.segment_id}_{item.metric_id}",
        value=item.value,
        unit=item.unit,
        period=item.period,
        roles=("SEGMENT_CONTRIBUTION",),
        source_ids=item.source_ids,
        source_route=item.source_route,
        observed_at=item.observed_at,
        record_kind="SEGMENT_FINANCIAL",
        confidence=item.confidence,
        dataset="FINANCIAL",
        provenance="STRUCTURED_EXTRACTED",
        metadata={
            **dict(item.metadata),
            "segment_id": item.segment_id,
            "segment_metric_id": item.metric_id,
            "available_at": item.available_at,
            "structured_source": True,
        },
    )
    total_record = None
    if item.total_company_value is not None:
        total_record = _metric_record(
            target_id=target_id,
            cutoff=cutoff,
            metric_id=f"company_total_{item.metric_id}_for_segment",
            value=item.total_company_value,
            unit=item.unit,
            period=item.period,
            roles=("SEGMENT_CONTRIBUTION_INPUT",),
            source_ids=item.source_ids,
            source_route=item.source_route,
            observed_at=item.observed_at,
            record_kind="SEGMENT_COMPANY_TOTAL",
            confidence=item.confidence,
            dataset="FINANCIAL",
            provenance="STRUCTURED_EXTRACTED",
            metadata={
                "segment_metric_id": item.metric_id,
                "structured_source": True,
            },
        )
    contribution = item.contribution_pct
    if contribution is None and item.total_company_value not in (None, 0.0):
        contribution = item.value / float(item.total_company_value) * 100.0
    if contribution is None:
        return (base, *((total_record,) if total_record is not None else ()))
    contribution_provenance = "STRUCTURED_EXTRACTED"
    contribution_inputs: tuple[str, ...] = ()
    if item.contribution_pct is None:
        assert total_record is not None
        contribution_provenance = "DERIVED"
        contribution_inputs = (base.record_id, total_record.record_id)
    percentage = _metric_record(
        target_id=target_id,
        cutoff=cutoff,
        metric_id=f"segment_{item.segment_id}_{item.metric_id}_contribution_pct",
        value=round(float(contribution), 6),
        unit="PERCENT",
        period=item.period,
        roles=("SEGMENT_CONTRIBUTION",),
        source_ids=item.source_ids,
        source_route=item.source_route,
        observed_at=item.observed_at,
        record_kind="SEGMENT_CONTRIBUTION",
        confidence=item.confidence,
        dataset="FINANCIAL",
        provenance=contribution_provenance,
        input_record_ids=contribution_inputs,
        metadata={
            **dict(item.metadata),
            "segment_id": item.segment_id,
            "total_company_value": item.total_company_value,
            "formula": (
                "source_reported_contribution_pct"
                if item.contribution_pct is not None
                else "segment_value / total_company_value * 100"
            ),
            "structured_source": True,
        },
    )
    return (
        base,
        *((total_record,) if total_record is not None else ()),
        percentage,
    )


def _records_from_guidance(
    *,
    target_id: str,
    cutoff: date,
    item: ForwardGuidanceObservation,
) -> tuple[StructuredMetricRecord, ...]:
    rows: list[StructuredMetricRecord] = []
    by_bound: dict[str, StructuredMetricRecord] = {}
    guidance_role = (
        "GUIDANCE_WITHDRAWN"
        if item.guidance_status == "WITHDRAWN_GUIDANCE"
        else "FORWARD_GUIDANCE"
    )
    for bound, value in (
        ("low", item.low_value),
        ("high", item.high_value),
        ("midpoint", item.midpoint_value),
    ):
        if value is None:
            continue
        record = _metric_record(
            target_id=target_id,
            cutoff=cutoff,
            metric_id=f"issuer_guidance_{item.metric_id}_{bound}",
            value=value,
            unit=item.unit,
            period=item.period,
            roles=(guidance_role,),
            source_ids=item.source_ids,
            source_route=item.source_route,
            observed_at=item.observed_at,
            record_kind="ISSUER_FORWARD_GUIDANCE",
            confidence=item.confidence,
            dataset="FINANCIAL",
            provenance="STRUCTURED_EXTRACTED",
            metadata={
                **dict(item.metadata),
                "guidance_status": item.guidance_status,
                "guidance_bound": bound,
                "available_at": item.available_at,
                "structured_source": True,
            },
        )
        rows.append(record)
        by_bound[bound] = record
    if (
        item.midpoint_value is None
        and item.low_value is not None
        and item.high_value is not None
    ):
        low = by_bound["low"]
        high = by_bound["high"]
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id=f"issuer_guidance_{item.metric_id}_midpoint",
                value=(item.low_value + item.high_value) / 2.0,
                unit=item.unit,
                period=item.period,
                roles=(guidance_role,),
                source_ids=item.source_ids,
                source_route=item.source_route,
                observed_at=item.observed_at,
                record_kind="ISSUER_FORWARD_GUIDANCE",
                confidence=item.confidence,
                dataset="FINANCIAL",
                provenance="DERIVED",
                input_record_ids=(low.record_id, high.record_id),
                metadata={
                    **dict(item.metadata),
                    "guidance_status": item.guidance_status,
                    "guidance_bound": "midpoint",
                    "formula": "(guidance_low + guidance_high) / 2",
                    "structured_source": True,
                },
            )
        )
    return tuple(rows)


def _records_from_actual(
    *, target_id: str, cutoff: date, tagged: _TaggedRow
) -> tuple[StructuredMetricRecord, ...]:
    item: FinancialActual = tagged.value
    period = _actual_period(item)
    observed = item.reported_at.isoformat()
    rows: list[StructuredMetricRecord] = []
    definitions = (
        ("revenue", item.sales, "CURRENCY", "LATEST_ACTUAL_REVENUE"),
        (
            "operating_profit",
            item.operating_profit,
            "CURRENCY",
            "LATEST_ACTUAL_OPERATING_PROFIT",
        ),
        ("net_income", item.net_income, "CURRENCY", "LATEST_ACTUAL_NET_INCOME"),
        ("eps", item.eps, "CURRENCY_PER_SHARE", "ACTUAL_EPS"),
        ("book_value", item.bps, "CURRENCY_PER_SHARE", "ACTUAL_BOOK_VALUE"),
        ("equity", item.equity, "CURRENCY", "ACTUAL_EQUITY"),
        ("roe_pct", item.roe, "PERCENT", "ACTUAL_ROE"),
        ("operating_margin_pct", item.opm, "PERCENT", "ACTUAL_MARGIN"),
        (
            "operating_cash_flow",
            item.cashflow_from_operations,
            "CURRENCY",
            "OPERATING_CASH_FLOW",
        ),
        ("capex", abs(item.capex) if item.capex is not None else None, "CURRENCY", "CAPEX"),
        ("free_cash_flow", item.fcf, "CURRENCY", "FREE_CASH_FLOW"),
        ("receivables", item.receivables, "CURRENCY", "WORKING_CAPITAL"),
        ("inventory", item.inventory, "CURRENCY", "WORKING_CAPITAL"),
    )
    by_metric: dict[str, StructuredMetricRecord] = {}
    for metric_id, value, unit, role in definitions:
        if value is None:
            continue
        record = _metric_record(
            target_id=target_id,
            cutoff=cutoff,
            metric_id=metric_id,
            value=value,
            unit=unit,
            period=period,
            roles=(role,),
            source_ids=tagged.source_ids,
            source_route=tagged.route_name,
            observed_at=observed,
            record_kind="FINANCIAL_ACTUAL",
            confidence=_route_confidence(tagged.route_name),
            dataset="FINANCIAL",
            provenance="OBSERVED",
            metadata={
                "symbol": item.symbol,
                "fiscal_year": item.fiscal_year,
                "fiscal_quarter": item.fiscal_quarter,
                "period_end": item.period_end.isoformat(),
                "reported_at": item.reported_at.isoformat(),
                "source_model": item.source,
                "structured_source": True,
            },
        )
        rows.append(record)
        by_metric[metric_id] = record
    if item.fcf is None and item.cashflow_from_operations is not None and item.capex is not None:
        cfo = by_metric["operating_cash_flow"]
        capex = by_metric["capex"]
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id="free_cash_flow",
                value=item.cashflow_from_operations - abs(item.capex),
                unit="CURRENCY",
                period=period,
                roles=("FREE_CASH_FLOW",),
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=observed,
                record_kind="FINANCIAL_DERIVED",
                confidence=_route_confidence(tagged.route_name),
                dataset="FINANCIAL",
                provenance="DERIVED",
                input_record_ids=(cfo.record_id, capex.record_id),
                metadata={
                    "formula": "operating_cash_flow - abs(capex)",
                    "missing_direct_fcf_parser_does_not_finalize_zero": True,
                },
            )
        )
    return tuple(rows)


def _records_from_consensus(
    *, target_id: str, cutoff: date, tagged: _TaggedRow
) -> tuple[StructuredMetricRecord, ...]:
    item: ConsensusSnapshot = tagged.value
    period = f"FY{item.fiscal_year}E"
    total_currency_unit = _consensus_total_currency_unit(item)
    definitions = (
        ("consensus_forward_revenue", item.sales_e, total_currency_unit, ("FORWARD_REVENUE",), "CONSENSUS_REVISION"),
        ("consensus_forward_operating_profit", item.op_e, total_currency_unit, ("FORWARD_OPERATING_PROFIT",), "CONSENSUS_REVISION"),
        ("consensus_forward_net_income", item.net_income_e, total_currency_unit, ("FORWARD_NET_INCOME",), "CONSENSUS_REVISION"),
        ("consensus_forward_eps", item.eps_e, "CURRENCY_PER_SHARE", ("FORWARD_EPS",), "CONSENSUS_REVISION"),
        ("consensus_forward_fcf", item.fcf_e, total_currency_unit, ("FORWARD_FCF",), "CONSENSUS_REVISION"),
        ("consensus_forward_book_value", item.bps_e, "CURRENCY_PER_SHARE", ("FORWARD_BOOK_VALUE",), "CONSENSUS_REVISION"),
        ("consensus_forward_roe_pct", item.roe_e, "PERCENT", ("FORWARD_ROE",), "CONSENSUS_REVISION"),
        ("consensus_forward_pe", item.per_e, "MULTIPLE", ("FORWARD_PE",), "VALUATION"),
        ("consensus_forward_pb", item.pbr_e, "MULTIPLE", ("FORWARD_PB",), "VALUATION"),
        ("consensus_target_price", item.target_price, "PRICE", ("TARGET_PRICE_ONLY",), "CONSENSUS_REVISION"),
        ("consensus_analyst_count", item.analyst_count, "COUNT", ("CONSENSUS_BREADTH",), "CONSENSUS_REVISION"),
    )
    rows = []
    for metric_id, value, unit, roles, dataset in definitions:
        if value is None:
            continue
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id=metric_id,
                value=value,
                unit=unit,
                period=period,
                roles=roles,
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=item.date.isoformat(),
                record_kind="CONSENSUS_SNAPSHOT" if dataset == "CONSENSUS_REVISION" else "STRUCTURED_VALUATION_SNAPSHOT",
                confidence=_route_confidence(tagged.route_name),
                dataset=dataset,
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "symbol": item.symbol,
                    "fiscal_year": item.fiscal_year,
                    "consensus_source": item.source,
                    "structured_source": True,
                    "target_price_only": metric_id == "consensus_target_price",
                    **dict(item.parsed_fields),
                },
            )
        )
    ebitda = _number(item.parsed_fields.get("ebitda_e"))
    if ebitda is not None:
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id="consensus_forward_ebitda",
                value=ebitda,
                unit=total_currency_unit,
                period=period,
                roles=("FORWARD_EBITDA",),
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=item.date.isoformat(),
                record_kind="CONSENSUS_SNAPSHOT",
                confidence=_route_confidence(tagged.route_name),
                dataset="CONSENSUS_REVISION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={"structured_source": True, "consensus_source": item.source},
            )
        )
    return tuple(rows)


def _records_from_revision(
    *, target_id: str, cutoff: date, tagged: _TaggedRow
) -> tuple[StructuredMetricRecord, ...]:
    item: ConsensusRevision = tagged.value
    period = f"FY{item.fiscal_year}E"
    definitions = (
        ("eps_revision_1w_pct", item.eps_revision_1w, "EPS_REVISION", "EARNINGS"),
        ("eps_revision_1m_pct", item.eps_revision_1m, "EPS_REVISION", "EARNINGS"),
        ("eps_revision_3m_pct", item.eps_revision_3m, "EPS_REVISION", "EARNINGS"),
        ("operating_profit_revision_1w_pct", item.op_revision_1w, "OPERATING_PROFIT_REVISION", "EARNINGS"),
        ("operating_profit_revision_1m_pct", item.op_revision_1m, "OPERATING_PROFIT_REVISION", "EARNINGS"),
        ("operating_profit_revision_3m_pct", item.op_revision_3m, "OPERATING_PROFIT_REVISION", "EARNINGS"),
        ("fcf_revision_1m_pct", item.fcf_revision_1m, "FCF_REVISION", "EARNINGS"),
        ("target_price_revision_1m_pct", item.target_price_revision_1m, "TARGET_PRICE_ONLY", "TARGET_PRICE"),
        ("street_high_eps_revision_1m_pct", item.street_high_eps_revision_1m, "EPS_REVISION", "EARNINGS"),
        ("street_low_eps_revision_1m_pct", item.street_low_eps_revision_1m, "EPS_REVISION", "EARNINGS"),
        ("analyst_count_change", item.analyst_count_change, "CONSENSUS_BREADTH", "BREADTH"),
    )
    rows = []
    for metric_id, value, role, family in definitions:
        if value is None:
            continue
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id=metric_id,
                value=value,
                unit="COUNT" if metric_id == "analyst_count_change" else "PERCENT",
                period=period,
                roles=(role,),
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=item.date.isoformat(),
                record_kind=(
                    "TARGET_PRICE_REVISION"
                    if family == "TARGET_PRICE"
                    else "EARNINGS_REVISION"
                ),
                confidence=_route_confidence(tagged.route_name),
                dataset="CONSENSUS_REVISION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "revision_family": family,
                    "target_price_only": family == "TARGET_PRICE",
                    "earnings_revision": family == "EARNINGS",
                    "revision_source": item.source,
                    "structured_source": True,
                    **dict(item.parsed_fields),
                },
            )
        )
    return tuple(rows)


def _records_from_report(
    *, target_id: str, cutoff: date, tagged: _TaggedRow
) -> tuple[StructuredMetricRecord, ...]:
    item: ResearchReport = tagged.value
    fiscal_year = int(item.parsed_fields.get("fy1_fiscal_year") or item.publish_date.year)
    rows: list[StructuredMetricRecord] = []
    for forward_index, values in (
        (1, (item.fy1_sales, item.fy1_op, item.fy1_eps)),
        (2, (item.fy2_sales, item.fy2_op, item.fy2_eps)),
        (3, (item.fy3_sales, item.fy3_op, item.fy3_eps)),
    ):
        period = f"FY{fiscal_year + forward_index - 1}E"
        for metric_id, value, unit, role in (
            ("broker_forward_revenue", values[0], "CURRENCY", "FORWARD_REVENUE"),
            ("broker_forward_operating_profit", values[1], "CURRENCY", "FORWARD_OPERATING_PROFIT"),
            ("broker_forward_eps", values[2], "CURRENCY_PER_SHARE", "FORWARD_EPS"),
        ):
            if value is None:
                continue
            rows.append(
                _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id=metric_id,
                    value=value,
                    unit=unit,
                    period=period,
                    roles=(role, "PUBLIC_BROKER_FORWARD_ESTIMATE"),
                    source_ids=tagged.source_ids,
                    source_route=tagged.route_name,
                    observed_at=item.publish_date.isoformat(),
                    record_kind="PUBLIC_BROKER_STRUCTURED_ESTIMATE",
                    confidence=_route_confidence(tagged.route_name),
                    dataset="CONSENSUS_REVISION",
                    provenance="STRUCTURED_EXTRACTED",
                    metadata={
                        "broker": item.broker,
                        "title": item.title,
                        "structured_source": True,
                        "forward_index": forward_index,
                    },
                )
            )
    for metric_id, value, unit, role in (
        ("broker_forward_pe", item.est_per, "MULTIPLE", "FORWARD_PE"),
        ("broker_forward_pb", item.est_pbr, "MULTIPLE", "FORWARD_PB"),
    ):
        if value is None:
            continue
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id=metric_id,
                value=value,
                unit=unit,
                period=f"FY{fiscal_year}E",
                roles=(role,),
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=item.publish_date.isoformat(),
                record_kind="PUBLIC_BROKER_STRUCTURED_VALUATION",
                confidence=_route_confidence(tagged.route_name),
                dataset="VALUATION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "broker": item.broker,
                    "title": item.title,
                    "structured_source": True,
                    "generic_article_claim": False,
                },
            )
        )
    if item.target_price is not None:
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id="broker_target_price",
                value=item.target_price,
                unit="PRICE",
                period=item.publish_date.isoformat(),
                roles=("TARGET_PRICE_ONLY",),
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=item.publish_date.isoformat(),
                record_kind="TARGET_PRICE_SNAPSHOT",
                confidence=_route_confidence(tagged.route_name),
                dataset="CONSENSUS_REVISION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "broker": item.broker,
                    "target_price_only": True,
                    "earnings_revision": False,
                    "structured_source": True,
                },
            )
        )
    if item.target_revision_pct is not None:
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id="broker_target_price_revision_pct",
                value=item.target_revision_pct,
                unit="PERCENT",
                period=item.publish_date.isoformat(),
                roles=("TARGET_PRICE_ONLY",),
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=item.publish_date.isoformat(),
                record_kind="TARGET_PRICE_REVISION",
                confidence=_route_confidence(tagged.route_name),
                dataset="CONSENSUS_REVISION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "broker": item.broker,
                    "revision_family": "TARGET_PRICE",
                    "target_price_only": True,
                    "earnings_revision": False,
                    "structured_source": True,
                },
            )
        )
    explicit_eps_revision = _number(
        item.parsed_fields.get("eps_revision_pct")
        or item.parsed_fields.get("eps_revision_1m")
    )
    explicit_op_revision = _number(
        item.parsed_fields.get("op_revision_pct")
        or item.parsed_fields.get("op_revision_1m")
    )
    for metric_id, value, role in (
        ("broker_eps_revision_pct", explicit_eps_revision, "EPS_REVISION"),
        (
            "broker_operating_profit_revision_pct",
            explicit_op_revision,
            "OPERATING_PROFIT_REVISION",
        ),
    ):
        if value is None:
            continue
        rows.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id=metric_id,
                value=value,
                unit="PERCENT",
                period=f"FY{fiscal_year}E",
                roles=(role,),
                source_ids=tagged.source_ids,
                source_route=tagged.route_name,
                observed_at=item.publish_date.isoformat(),
                record_kind="EARNINGS_REVISION",
                confidence=_route_confidence(tagged.route_name),
                dataset="CONSENSUS_REVISION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "broker": item.broker,
                    "revision_family": "EARNINGS",
                    "target_price_only": False,
                    "structured_source": True,
                },
            )
        )
    return tuple(rows)


def _metric_record(
    *,
    target_id: str,
    cutoff: date,
    metric_id: str,
    value: float | int | str,
    unit: str,
    period: str,
    roles: Sequence[str],
    source_ids: Sequence[str],
    source_route: str,
    observed_at: str,
    record_kind: str,
    confidence: float,
    dataset: str,
    provenance: str,
    input_record_ids: Sequence[str] = (),
    metadata: Mapping[str, Any] | None = None,
) -> StructuredMetricRecord:
    unique_sources = tuple(dict.fromkeys(str(value) for value in source_ids if value))
    unique_inputs = tuple(
        dict.fromkeys(str(value) for value in input_record_ids if value)
    )
    unique_roles = tuple(dict.fromkeys(str(value) for value in roles if value))
    identity = {
        "target_id": target_id,
        "as_of_date": cutoff.isoformat(),
        "metric_id": metric_id,
        "value": value,
        "unit": unit,
        "period": period,
        "source_ids": unique_sources,
        "source_route": source_route,
        "observed_at": observed_at,
        "record_kind": record_kind,
        "evidence_roles": unique_roles,
        "dataset": dataset,
        "provenance": provenance,
        "input_record_ids": unique_inputs,
        # Two brokers may publish the same estimate on the same date.  Their
        # records are still distinct observations and must not collide merely
        # because the numeric value matches.  Metadata carries the broker,
        # report/document id, scenario, peer id, and other semantic identity.
        "metadata": dict(metadata or {}),
    }
    return StructuredMetricRecord(
        record_id=_stable_id("STRUCTURED", identity),
        target_id=target_id,
        as_of_date=cutoff.isoformat(),
        metric_id=metric_id,
        value=value,
        unit=unit,
        period=period,
        evidence_roles=unique_roles,
        source_ids=unique_sources,
        source_route=source_route,
        observed_at=observed_at,
        available_at=observed_at,
        record_kind=record_kind,
        confidence=round(float(confidence), 6),
        dataset=dataset,
        provenance=provenance,
        input_record_ids=unique_inputs,
        metadata=dict(metadata or {}),
    )


def _derive_missing_fcf_records(
    target_id: str,
    cutoff: date,
    records: Sequence[StructuredMetricRecord],
) -> tuple[StructuredMetricRecord, ...]:
    periods = sorted(
        {
            row.period
            for row in records
            if row.metric_id in {"operating_cash_flow", "capex"}
        }
    )
    output = []
    for period in periods:
        if any(
            row.period == period
            and row.metric_id in {"free_cash_flow", "fcf"}
            for row in records
        ):
            continue
        cfo_rows = [
            row
            for row in records
            if row.period == period and row.metric_id == "operating_cash_flow"
        ]
        capex_rows = [
            row
            for row in records
            if row.period == period and row.metric_id == "capex"
        ]
        if not cfo_rows or not capex_rows:
            continue
        cfo = max(cfo_rows, key=lambda row: (row.confidence, row.observed_at))
        capex = max(capex_rows, key=lambda row: (row.confidence, row.observed_at))
        cfo_value = _number(cfo.value)
        capex_value = _number(capex.value)
        if cfo_value is None or capex_value is None:
            continue
        if cfo.unit == capex.unit:
            fcf_value = cfo_value - abs(capex_value)
            fcf_unit = cfo.unit
        else:
            fcf_value = _amount_in_base(cfo) - abs(_amount_in_base(capex))
            fcf_unit = "BASE_CURRENCY"
        output.append(
            _metric_record(
                target_id=target_id,
                cutoff=cutoff,
                metric_id="free_cash_flow",
                value=fcf_value,
                unit=fcf_unit,
                period=period,
                roles=("FREE_CASH_FLOW",),
                source_ids=tuple(dict.fromkeys((*cfo.source_ids, *capex.source_ids))),
                source_route=f"{cfo.source_route}+{capex.source_route}",
                observed_at=max(cfo.observed_at, capex.observed_at),
                record_kind="FINANCIAL_DERIVED",
                confidence=min(cfo.confidence, capex.confidence),
                dataset="FINANCIAL",
                provenance="DERIVED",
                input_record_ids=(cfo.record_id, capex.record_id),
                metadata={
                    "formula": "operating_cash_flow - abs(capex)",
                    "derived_from_generic_structured_records": True,
                    "missing_direct_fcf_parser_does_not_finalize_zero": True,
                },
            )
        )
    return tuple(output)


def _copy_as_valuation_input(
    source: StructuredMetricRecord,
    *,
    target_id: str,
    cutoff: date,
    metric_id: str,
    unit: str,
    role: str,
) -> StructuredMetricRecord:
    return _metric_record(
        target_id=target_id,
        cutoff=cutoff,
        metric_id=metric_id,
        value=source.value,
        unit=unit,
        period=source.period,
        roles=(role,),
        source_ids=source.source_ids,
        source_route=source.source_route,
        observed_at=source.observed_at,
        record_kind="VALUATION_FORWARD_INPUT",
        confidence=source.confidence,
        dataset="VALUATION",
        provenance="DERIVED",
        input_record_ids=(source.record_id,),
        metadata={
            "structured_source": True,
            "copied_from_metric_id": source.metric_id,
        },
    )


def _derived_from_one(
    source: StructuredMetricRecord,
    *,
    target_id: str,
    cutoff: date,
    metric_id: str,
    value: float,
    unit: str,
    role: str,
    record_kind: str,
) -> StructuredMetricRecord:
    return _metric_record(
        target_id=target_id,
        cutoff=cutoff,
        metric_id=metric_id,
        value=round(value, 6),
        unit=unit,
        period=source.period,
        roles=(role,),
        source_ids=source.source_ids,
        source_route=source.source_route,
        observed_at=source.observed_at,
        record_kind=record_kind,
        confidence=source.confidence,
        dataset="VALUATION",
        provenance="DERIVED",
        input_record_ids=(source.record_id,),
        metadata={"structured_source": True},
    )


def _binary_derived_record(
    *,
    target_id: str,
    cutoff: date,
    metric_id: str,
    value: float,
    unit: str,
    role: str,
    left: StructuredMetricRecord,
    right: StructuredMetricRecord,
    formula: str,
    record_kind: str,
) -> StructuredMetricRecord:
    return _nary_derived_record(
        target_id=target_id,
        cutoff=cutoff,
        metric_id=metric_id,
        value=value,
        unit=unit,
        role=role,
        inputs=(left, right),
        formula=formula,
        record_kind=record_kind,
    )


def _nary_derived_record(
    *,
    target_id: str,
    cutoff: date,
    metric_id: str,
    value: float,
    unit: str,
    role: str,
    inputs: Sequence[StructuredMetricRecord],
    formula: str,
    record_kind: str,
) -> StructuredMetricRecord:
    return _metric_record(
        target_id=target_id,
        cutoff=cutoff,
        metric_id=metric_id,
        value=round(float(value), 6),
        unit=unit,
        period=max(row.period for row in inputs),
        roles=(role,),
        source_ids=tuple(
            dict.fromkeys(source_id for row in inputs for source_id in row.source_ids)
        ),
        source_route="+".join(dict.fromkeys(row.source_route for row in inputs)),
        observed_at=max(row.observed_at for row in inputs),
        record_kind=record_kind,
        confidence=min(row.confidence for row in inputs),
        dataset="VALUATION",
        provenance="DERIVED",
        input_record_ids=tuple(row.record_id for row in inputs),
        metadata={"formula": formula, "structured_source": True},
    )


def _historical_band_records(
    *,
    target_id: str,
    cutoff: date,
    existing: Sequence[StructuredMetricRecord],
    current_multiples: Mapping[str, StructuredMetricRecord],
) -> tuple[StructuredMetricRecord, ...]:
    result: list[StructuredMetricRecord] = []
    definitions = {
        "forward_pe": (
            "historical_forward_pe",
            "consensus_forward_pe",
            "broker_forward_pe",
        ),
        "forward_pb": (
            "historical_forward_pb",
            "consensus_forward_pb",
            "broker_forward_pb",
        ),
        "forward_ev_ebitda": (
            "historical_forward_ev_ebitda",
            "forward_ev_ebitda",
        ),
    }
    for metric_id, aliases in definitions.items():
        observations = [
            row
            for row in existing
            if row.metric_id in aliases
            and _number(row.value) is not None
            and float(row.value) > 0
            and row.record_kind
            not in {"VALUATION_HISTORICAL_BAND", "VALUATION_PEER_BAND"}
        ]
        unique_by_period: dict[tuple[str, str], StructuredMetricRecord] = {}
        for row in sorted(observations, key=lambda value: value.observed_at):
            key = (row.period, row.observed_at[:10])
            current = unique_by_period.get(key)
            if current is None or row.confidence > current.confidence:
                unique_by_period[key] = row
        history = list(unique_by_period.values())
        if len(history) < 3:
            continue
        current = current_multiples.get(metric_id) or _latest_metric(
            existing, (metric_id, *aliases)
        )
        if current is None or _number(current.value) is None:
            continue
        values = sorted(float(row.value) for row in history)
        percentile = (
            sum(value <= float(current.value) for value in values) / len(values) * 100.0
        )
        inputs = tuple(dict.fromkeys((current.record_id, *(row.record_id for row in history))))
        sources = tuple(
            dict.fromkeys(
                source_id
                for row in (current, *history)
                for source_id in row.source_ids
            )
        )
        for suffix, value, unit in (
            ("p25", _quantile(values, 0.25), "MULTIPLE"),
            ("median", median(values), "MULTIPLE"),
            ("p75", _quantile(values, 0.75), "MULTIPLE"),
            ("current_percentile", percentile, "PERCENTILE"),
        ):
            result.append(
                _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id=f"own_{metric_id}_{suffix}",
                    value=round(float(value), 6),
                    unit=unit,
                    period=current.period,
                    roles=("OWN_HISTORICAL_BAND",),
                    source_ids=sources,
                    source_route="STRUCTURED_HISTORICAL_BAND",
                    observed_at=current.observed_at,
                    record_kind="VALUATION_HISTORICAL_BAND",
                    confidence=min(row.confidence for row in (current, *history)),
                    dataset="VALUATION",
                    provenance="DERIVED",
                    input_record_ids=inputs,
                    metadata={
                        "metric_family": metric_id,
                        "history_observation_count": len(history),
                        "formula": "empirical historical distribution",
                        "structured_source": True,
                    },
                )
            )
    return tuple(result)


def _peer_band_records(
    *,
    target_id: str,
    cutoff: date,
    peers: Sequence[_TaggedRow],
    existing: Sequence[StructuredMetricRecord],
) -> tuple[StructuredMetricRecord, ...]:
    grouped: dict[str, list[_TaggedRow]] = {}
    for tagged in peers:
        grouped.setdefault(tagged.value.metric_id, []).append(tagged)
    result: list[StructuredMetricRecord] = []
    for metric_id, rows in grouped.items():
        unique_peers: dict[str, _TaggedRow] = {}
        for row in sorted(rows, key=lambda value: value.value.observed_at):
            unique_peers[row.value.peer_id] = row
        selected = list(unique_peers.values())
        if len(selected) < 2:
            continue
        values = sorted(float(row.value.value) for row in selected)
        input_ids = tuple(
            row.record_id
            for row in existing
            if row.metric_id == f"peer_{metric_id}"
            and row.metadata.get("peer_id") in unique_peers
        ) or tuple(
            _stable_id("STRUCTURED-INPUT", "peer", row.value.peer_id, metric_id)
            for row in selected
        )
        source_ids = tuple(
            dict.fromkeys(
                source_id
                for row in selected
                for source_id in row.value.source_ids
            )
        )
        for suffix, value in (
            ("p25", _quantile(values, 0.25)),
            ("median", median(values)),
            ("p75", _quantile(values, 0.75)),
        ):
            result.append(
                _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id=f"peer_{metric_id}_{suffix}",
                    value=round(float(value), 6),
                    unit=selected[0].value.unit,
                    period=max(row.value.observed_at[:10] for row in selected),
                    roles=("PEER_BAND",),
                    source_ids=source_ids,
                    source_route="STRUCTURED_PEER_BAND",
                    observed_at=max(row.value.observed_at for row in selected),
                    record_kind="VALUATION_PEER_BAND",
                    confidence=min(row.value.confidence for row in selected),
                    dataset="VALUATION",
                    provenance="DERIVED",
                    input_record_ids=input_ids,
                    metadata={
                        "metric_family": metric_id,
                        "peer_ids": sorted(unique_peers),
                        "peer_count": len(selected),
                        "structured_source": True,
                    },
                )
            )
    return tuple(result)


def _scenario_records(
    *,
    target_id: str,
    cutoff: date,
    actuals: Sequence[_TaggedRow],
    current_price: StructuredMetricRecord | None,
    market_cap: StructuredMetricRecord | None,
    existing: Sequence[StructuredMetricRecord],
) -> tuple[StructuredMetricRecord, ...]:
    selected = _best_actuals(actuals)
    if not selected:
        return ()
    latest_key = max(
        selected,
        key=lambda key: (
            selected[key].value.period_end,
            selected[key].value.reported_at,
        ),
    )
    latest = selected[latest_key]
    item: FinancialActual = latest.value
    if item.sales is None or item.sales <= 0:
        return ()
    comparator = selected.get((item.fiscal_year - 1, item.fiscal_quarter))
    base_growth = 0.0
    if comparator is not None and comparator.value.sales:
        observed_growth = _percent_change(item.sales, comparator.value.sales)
        if observed_growth is not None:
            base_growth = _clamp(observed_growth, -30.0, 50.0)
    source_ids = tuple(
        dict.fromkeys(
            (
                *latest.source_ids,
                *(comparator.source_ids if comparator is not None else ()),
                *(current_price.source_ids if current_price is not None else ()),
                *(market_cap.source_ids if market_cap is not None else ()),
            )
        )
    )
    input_ids = tuple(
        dict.fromkeys(
            (
                *_record_ids(existing, "revenue", _actual_period(item)),
                *_record_ids(existing, "operating_profit", _actual_period(item)),
                *_record_ids(existing, "net_income", _actual_period(item)),
                *_record_ids(existing, "free_cash_flow", _actual_period(item)),
                *((current_price.record_id,) if current_price is not None else ()),
                *((market_cap.record_id,) if market_cap is not None else ()),
            )
        )
    ) or (_stable_id("STRUCTURED-INPUT", "scenario", _actual_period(item)),)
    op_margin = _safe_divide(item.operating_profit, item.sales)
    net_margin = _safe_divide(item.net_income, item.sales)
    actual_fcf = _actual_metric_value(item, "fcf")
    fcf_margin = _safe_divide(actual_fcf, item.sales)
    shares = (
        _safe_divide(float(market_cap.value), float(current_price.value))
        if market_cap is not None and current_price is not None
        else None
    )
    output: list[StructuredMetricRecord] = []
    for scenario, adjustment in (("bear", -10.0), ("base", 0.0), ("bull", 10.0)):
        growth = _clamp(base_growth + adjustment, -50.0, 75.0)
        revenue = item.sales * (1.0 + growth / 100.0)
        scenario_values: list[tuple[str, float | None, str, tuple[str, ...]]] = [
            ("revenue", revenue, "CURRENCY", ("SCENARIO_SENSITIVITY",)),
            (
                "operating_profit",
                revenue * op_margin if op_margin is not None else None,
                "CURRENCY",
                ("SCENARIO_SENSITIVITY",),
            ),
            (
                "net_income",
                revenue * net_margin if net_margin is not None else None,
                "CURRENCY",
                ("SCENARIO_SENSITIVITY",),
            ),
            (
                "free_cash_flow",
                revenue * fcf_margin if fcf_margin is not None else None,
                "CURRENCY",
                ("SCENARIO_SENSITIVITY", "FORWARD_FCF"),
            ),
        ]
        projected_net_income = revenue * net_margin if net_margin is not None else None
        projected_eps = (
            _safe_divide(projected_net_income, shares)
            if projected_net_income is not None and shares is not None
            else None
        )
        scenario_values.append(
            (
                "eps",
                projected_eps,
                "CURRENCY_PER_SHARE",
                ("SCENARIO_SENSITIVITY", "FORWARD_EPS"),
            )
        )
        projected_fcf = revenue * fcf_margin if fcf_margin is not None else None
        if current_price is not None and projected_eps is not None and projected_eps > 0:
            scenario_values.append(
                (
                    "forward_pe",
                    float(current_price.value) / projected_eps,
                    "MULTIPLE",
                    ("SCENARIO_SENSITIVITY",),
                )
            )
        if market_cap is not None and projected_fcf is not None:
            scenario_values.append(
                (
                    "forward_fcf_yield_pct",
                    projected_fcf / float(market_cap.value) * 100.0,
                    "PERCENT",
                    ("SCENARIO_SENSITIVITY",),
                )
            )
        for metric_id, value, unit, roles in scenario_values:
            if value is None or not math.isfinite(float(value)):
                continue
            output.append(
                _metric_record(
                    target_id=target_id,
                    cutoff=cutoff,
                    metric_id=f"scenario_{scenario}_{metric_id}",
                    value=round(float(value), 6),
                    unit=unit,
                    period=_next_scenario_period(item),
                    roles=roles,
                    source_ids=source_ids,
                    source_route="DETERMINISTIC_FORWARD_SCENARIO",
                    observed_at=item.reported_at.isoformat(),
                    record_kind="VALUATION_SCENARIO",
                    confidence=0.65,
                    dataset="VALUATION",
                    provenance="DETERMINISTIC_SCENARIO",
                    input_record_ids=input_ids,
                    metadata={
                        "scenario": scenario,
                        "base_growth_pct": round(base_growth, 6),
                        "growth_adjustment_pctp": adjustment,
                        "scenario_growth_pct": round(growth, 6),
                        "margin_hold_constant": True,
                        "formula_version": "dart_actual_trend_scenario_v1",
                        "observed_fact": False,
                        "structured_source": True,
                    },
                )
            )
    return tuple(output)


def _best_actuals(actuals: Sequence[_TaggedRow]) -> Mapping[tuple[int, int | None], _TaggedRow]:
    selected: dict[tuple[int, int | None], _TaggedRow] = {}
    for tagged in actuals:
        item: FinancialActual = tagged.value
        key = (item.fiscal_year, item.fiscal_quarter)
        current = selected.get(key)
        if current is None or _actual_quality_key(tagged) > _actual_quality_key(current):
            selected[key] = tagged
    return selected


def _actual_quality_key(tagged: _TaggedRow) -> tuple[int, int, str]:
    item: FinancialActual = tagged.value
    values = (
        item.sales,
        item.operating_profit,
        item.net_income,
        item.eps,
        item.bps,
        item.equity,
        item.cashflow_from_operations,
        item.capex,
        item.fcf,
    )
    return (
        sum(value is not None for value in values),
        item.reported_at.date().toordinal(),
        tagged.route_name,
    )


def _latest_consensus(
    rows: Sequence[_TaggedRow], cutoff: date
) -> _TaggedRow | None:
    eligible = [row for row in rows if row.value.date <= cutoff]
    if not eligible:
        return None
    future_fiscal = [row for row in eligible if row.value.fiscal_year >= cutoff.year]
    pool = future_fiscal or eligible
    return max(
        pool,
        key=lambda row: (
            row.value.date,
            row.value.fiscal_year,
            _consensus_completeness(row.value),
        ),
    )


def _consensus_completeness(item: ConsensusSnapshot) -> int:
    return sum(
        value is not None
        for value in (
            item.sales_e,
            item.op_e,
            item.net_income_e,
            item.eps_e,
            item.fcf_e,
            item.bps_e,
            item.per_e,
            item.pbr_e,
        )
    )


def _latest_metric(
    records: Sequence[StructuredMetricRecord], aliases: Sequence[str]
) -> StructuredMetricRecord | None:
    accepted = [
        row
        for row in records
        if row.metric_id in set(aliases)
        and _number(row.value) is not None
        and not bool(row.metadata.get("generic_article_claim"))
    ]
    if not accepted:
        return None
    return max(
        accepted,
        key=lambda row: (
            row.observed_at,
            row.period,
            row.confidence,
            row.record_id,
        ),
    )


def _record_ids(
    records: Sequence[StructuredMetricRecord], metric_id: str, period: str
) -> tuple[str, ...]:
    return tuple(
        row.record_id
        for row in records
        if row.metric_id == metric_id and row.period == period
    )


def _actual_period(item: FinancialActual) -> str:
    return (
        f"FY{item.fiscal_year}Q{item.fiscal_quarter}"
        if item.fiscal_quarter is not None
        else f"FY{item.fiscal_year}"
    )


def _next_scenario_period(item: FinancialActual) -> str:
    if item.fiscal_quarter is None:
        return f"FY{item.fiscal_year + 1}E"
    if item.fiscal_quarter == 4:
        return f"FY{item.fiscal_year + 1}Q1E"
    return f"FY{item.fiscal_year}Q{item.fiscal_quarter + 1}E"


def _actual_metric_value(item: FinancialActual, attribute: str) -> float | None:
    if attribute != "fcf":
        return _number(getattr(item, attribute))
    if item.fcf is not None:
        return float(item.fcf)
    if item.cashflow_from_operations is not None and item.capex is not None:
        return float(item.cashflow_from_operations) - abs(float(item.capex))
    return None


def _previous_quarter_key(
    fiscal_year: int, quarter: int | None
) -> tuple[int, int | None]:
    if quarter is None:
        return (fiscal_year - 1, None)
    return (fiscal_year - 1, 4) if quarter == 1 else (fiscal_year, quarter - 1)


def _consensus_quarter_matches(
    item: ConsensusSnapshot, actual_quarter: int | None
) -> bool:
    if actual_quarter is None:
        return item.parsed_fields.get("fiscal_quarter") in (None, "", "ANNUAL")
    raw = item.parsed_fields.get("fiscal_quarter")
    if raw in (None, ""):
        return False
    try:
        return int(raw) == actual_quarter
    except (TypeError, ValueError):
        return False


def _bar_on_or_before(
    rows: Sequence[_TaggedRow], ordinal: int
) -> _TaggedRow | None:
    eligible = [row for row in rows if row.value.date.toordinal() <= ordinal]
    return eligible[-1] if eligible else None


def _price_bar_input_id(item: PriceBar) -> str:
    return _stable_id(
        "STRUCTURED-INPUT",
        "price-bar",
        item.symbol,
        item.date.isoformat(),
        item.close,
        item.source,
    )


def _percent_change(current: Any, previous: Any) -> float | None:
    current_value = _number(current)
    previous_value = _number(previous)
    if current_value is None or previous_value in (None, 0.0):
        return None
    return (current_value / previous_value - 1.0) * 100.0


def _safe_divide(numerator: Any, denominator: Any) -> float | None:
    left = _number(numerator)
    right = _number(denominator)
    if left is None or right in (None, 0.0):
        return None
    value = left / right
    return value if math.isfinite(value) else None


def _consensus_total_currency_unit(item: ConsensusSnapshot) -> str:
    value = str(
        item.parsed_fields.get("financial_statement_unit")
        or item.parsed_fields.get("currency_unit")
        or "CURRENCY"
    ).strip().upper()
    aliases = {
        "KRW_100M": "KRW_100M",
        "KRW_100_MILLION": "KRW_100M",
        "억원": "KRW_100M",
        "KRW_MILLION": "KRW_MILLION",
        "백만원": "KRW_MILLION",
        "KRW": "KRW",
        "원": "KRW",
        "USD_MILLION": "USD_MILLION",
        "USD": "USD",
    }
    return aliases.get(value, value if value else "CURRENCY")


def _amount_in_base(record: StructuredMetricRecord) -> float:
    explicit_scale = _number(record.metadata.get("currency_scale_to_base"))
    if explicit_scale is not None:
        return float(record.value) * explicit_scale
    scale = {
        "KRW": 1.0,
        "KRW_100M": 100_000_000.0,
        "KRW_MILLION": 1_000_000.0,
        "USD": 1.0,
        "USD_MILLION": 1_000_000.0,
        "CURRENCY": 1.0,
    }.get(record.unit, 1.0)
    return float(record.value) * scale


def _number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _quantile(values: Sequence[float], probability: float) -> float:
    ordered = sorted(float(value) for value in values)
    if not ordered:
        raise ValueError("quantile requires observations")
    if len(ordered) == 1:
        return ordered[0]
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def _clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, float(value)))


def _route_confidence(route_name: str) -> float:
    return {
        "DART_ACTUALS_DETERMINISTIC_SCENARIO": 0.98,
        "KRX_PRICE_MARKET_CAP": 0.98,
        "ISSUER_GUIDANCE": 0.95,
        "COMPANYGUIDE": 0.90,
        "NAVER_FINANCE": 0.88,
        "CONSENSUS_CSV": 0.88,
        "PUBLIC_BROKER_REPORT": 0.86,
        "PEER_STRUCTURED": 0.86,
    }.get(route_name, 0.80)


def _dedupe_records(
    records: Sequence[StructuredMetricRecord],
) -> tuple[StructuredMetricRecord, ...]:
    by_id: dict[str, StructuredMetricRecord] = {}
    for row in records:
        existing = by_id.get(row.record_id)
        if existing is not None and existing.to_dict() != row.to_dict():
            raise ValueError("structured record id collision")
        by_id[row.record_id] = row
    return tuple(
        sorted(
            by_id.values(),
            key=lambda row: (
                row.dataset,
                row.metric_id,
                row.period,
                row.observed_at,
                row.record_id,
            ),
        )
    )


def _stable_id(prefix: str, *parts: Any) -> str:
    import json

    payload = json.dumps(parts, ensure_ascii=False, sort_keys=True, default=str)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]
    return f"{prefix}-{digest}"


__all__ = [
    "CANONICAL_STRUCTURED_SOURCE_ROUTES",
    "PHASE86_COMPONENT_ROLE_COMPATIBILITY",
    "PHASE86_REQUIRED_ROLES_BY_COMPONENT",
    "ForwardGuidanceObservation",
    "PeerValuationObservation",
    "SegmentFinancialObservation",
    "STRUCTURED_FINANCIAL_OUTPUT_FILES",
    "STRUCTURED_ROUTE_CAPABILITIES",
    "StructuredEngineResult",
    "StructuredFinancialConsensusValuationEngine",
    "StructuredRecordRejection",
    "StructuredSourceAttempt",
    "StructuredSourcePayload",
    "StructuredSourceRoute",
    "write_structured_financial_outputs",
]
