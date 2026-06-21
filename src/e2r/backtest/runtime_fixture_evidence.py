"""Source-backed V12 runtime fixture evidence for diagnostic replays.

The fixture spec is not a production data source. It is an explicit replay aid
that turns existing research MD trigger rows into point-in-time evidence so the
runtime pipeline can be tested against the accumulated research ledger.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import claim_metadata_from_claims, compile_claims_from_parsed_fields, compile_claims_from_primitives
from e2r.agentic.evidence_contract import evidence_contract_for_archetype
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.models import Evidence, Instrument, Market, ResearchReport, SourceTier


@dataclass(frozen=True)
class RuntimeFixtureEvidenceRow:
    """One source-backed fixture row converted from the V12 replay spec."""

    symbol: str
    company_name: str
    market: Market
    as_of_date: date
    role: str
    canonical_archetype_id: str
    large_sector_id: str | None
    source_file: str
    trigger_id: str | None
    case_id: str | None
    report: ResearchReport
    evidence: Evidence


DEFAULT_CARRY_FORWARD_DAYS = 180


class RuntimeFixtureEvidenceStore:
    """Load explicit V12 fixture specs and expose as-of evidence rows."""

    def __init__(self, spec_paths: Sequence[str | Path] = (), *, project_root: str | Path | None = None) -> None:
        self.project_root = Path(project_root or Path.cwd())
        self.rows = tuple(
            row
            for spec_path in spec_paths
            for row in _rows_from_spec_path(Path(spec_path), project_root=self.project_root)
        )

    def instruments(self, *, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        by_symbol: dict[str, RuntimeFixtureEvidenceRow] = {}
        for row in self.rows:
            if row.market != market or row.as_of_date > as_of_date:
                continue
            by_symbol.setdefault(row.symbol, row)
        return tuple(
            Instrument(
                symbol=row.symbol,
                name=row.company_name,
                market=row.market,
                exchange="KRX" if row.market == Market.KR else row.market.value,
                currency="KRW" if row.market == Market.KR else "USD",
            )
            for row in sorted(by_symbol.values(), key=lambda item: item.symbol)
        )

    def candidates(
        self,
        *,
        market: Market,
        as_of_date: date,
        carry_forward_symbols: Sequence[str] = (),
        carry_forward_days: int = DEFAULT_CARRY_FORWARD_DAYS,
    ) -> tuple[CheapScanCandidate, ...]:
        exact_rows = [row for row in self.rows if row.market == market and row.as_of_date == as_of_date]
        carry_forward_set = {str(symbol) for symbol in carry_forward_symbols}
        carry_forward_cutoff = as_of_date - timedelta(days=max(carry_forward_days, 0))
        carried_rows = [
            row
            for row in self.rows
            if row.market == market
            and row.role == "green"
            and row.symbol in carry_forward_set
            and carry_forward_cutoff <= row.as_of_date < as_of_date
        ]
        candidate_rows = _dedupe_fixture_candidate_rows((*exact_rows, *carried_rows))
        return tuple(
            CheapScanCandidate(
                symbol=row.symbol,
                company_name=row.company_name,
                market=row.market,
                as_of_date=as_of_date,
                reason_codes=_candidate_reason_codes(row, replay_date=as_of_date),
                cheap_scan_total_score=80.0,
                evidence_ids=(row.evidence.evidence_id,),
                recommended_next_layer=RecommendedNextLayer.DEEP_RESEARCH,
                candidate_source_path="runtime_fixture_spec",
                test_injected=True,
                production_candidate=False,
            )
            for row in sorted(candidate_rows, key=lambda item: (item.symbol, item.canonical_archetype_id, item.role, item.as_of_date))
        )

    def reports_for(
        self,
        *,
        symbol: str,
        as_of_date: date,
        canonical_archetype_id: str | None = None,
        role: str | None = None,
    ) -> tuple[ResearchReport, ...]:
        return tuple(
            row.report
            for row in self._matching_rows(
                symbol=symbol,
                as_of_date=as_of_date,
                canonical_archetype_id=canonical_archetype_id,
                role=role,
            )
        )

    def evidence_for(
        self,
        *,
        symbol: str,
        as_of_date: date,
        canonical_archetype_id: str | None = None,
        role: str | None = None,
    ) -> tuple[Evidence, ...]:
        return tuple(
            row.evidence
            for row in self._matching_rows(
                symbol=symbol,
                as_of_date=as_of_date,
                canonical_archetype_id=canonical_archetype_id,
                role=role,
            )
        )

    def reports_for_candidate(self, candidate: CheapScanCandidate) -> tuple[ResearchReport, ...]:
        scope = _fixture_scope_from_candidate(candidate)
        if scope is None:
            return ()
        canonical_archetype_id, role = scope
        return self.reports_for(
            symbol=candidate.symbol,
            as_of_date=candidate.as_of_date,
            canonical_archetype_id=canonical_archetype_id,
            role=role,
        )

    def evidence_for_candidate(self, candidate: CheapScanCandidate) -> tuple[Evidence, ...]:
        scope = _fixture_scope_from_candidate(candidate)
        if scope is None:
            return ()
        canonical_archetype_id, role = scope
        return self.evidence_for(
            symbol=candidate.symbol,
            as_of_date=candidate.as_of_date,
            canonical_archetype_id=canonical_archetype_id,
            role=role,
        )

    def _matching_rows(
        self,
        *,
        symbol: str,
        as_of_date: date,
        canonical_archetype_id: str | None,
        role: str | None,
    ) -> tuple[RuntimeFixtureEvidenceRow, ...]:
        return tuple(
            row
            for row in self.rows
            if row.symbol == symbol
            and row.as_of_date <= as_of_date
            and (not canonical_archetype_id or row.canonical_archetype_id == canonical_archetype_id)
            and (not role or row.role == role)
        )


def _dedupe_fixture_candidate_rows(rows: Sequence[RuntimeFixtureEvidenceRow]) -> tuple[RuntimeFixtureEvidenceRow, ...]:
    by_key: dict[tuple[str, str, str, str], RuntimeFixtureEvidenceRow] = {}
    for row in rows:
        key = (row.symbol, row.canonical_archetype_id, row.role, row.evidence.evidence_id)
        by_key.setdefault(key, row)
    return tuple(by_key.values())


def _candidate_reason_codes(row: RuntimeFixtureEvidenceRow, *, replay_date: date) -> tuple[str, ...]:
    codes = [
        "V12_RUNTIME_FIXTURE_SPEC",
        row.canonical_archetype_id,
        f"fixture_role:{row.role}",
        f"fixture_source_date:{row.as_of_date.isoformat()}",
    ]
    if row.as_of_date != replay_date:
        codes.append("fixture_carried_forward")
    return tuple(codes)


def _rows_from_spec_path(path: Path, *, project_root: Path) -> tuple[RuntimeFixtureEvidenceRow, ...]:
    raw_rows = _load_spec_rows(path)
    rows: list[RuntimeFixtureEvidenceRow] = []
    for raw in raw_rows:
        row = _fixture_row_from_spec(raw, project_root=project_root)
        if row is not None:
            rows.append(row)
    return tuple(rows)


def _load_spec_rows(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.suffix.lower() == ".jsonl":
        rows = []
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    rows.append(json.loads(line))
        return tuple(row for row in rows if isinstance(row, Mapping))
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return tuple(row for row in payload if isinstance(row, Mapping))
    if isinstance(payload, Mapping):
        rows = payload.get("rows")
        if isinstance(rows, list):
            return tuple(row for row in rows if isinstance(row, Mapping))
    return ()


def _fixture_row_from_spec(raw: Mapping[str, Any], *, project_root: Path) -> RuntimeFixtureEvidenceRow | None:
    role = str(raw.get("role") or "").strip().lower() or "fixture"
    is_ready_pair = raw.get("fixture_status") == "ready_for_runtime_replay_fixture"
    if not is_ready_pair and role != "guard":
        return None
    candidate = raw.get("candidate")
    if not isinstance(candidate, Mapping):
        return None
    if candidate.get("source_proxy_only") or candidate.get("evidence_url_pending"):
        return None
    symbol = str(candidate.get("symbol") or "").strip()
    if not symbol:
        return None
    row_date = _row_date(candidate)
    if row_date is None:
        return None
    source_file = str(candidate.get("source_file") or "").strip()
    if not source_file:
        return None
    source_path = project_root / source_file
    if not source_path.exists():
        return None
    trigger = _source_trigger_row(source_path, trigger_id=candidate.get("trigger_id"), case_id=candidate.get("case_id"))
    company_name = str(
        trigger.get("company_name")
        or trigger.get("company_name_kr")
        or candidate.get("company_name")
        or symbol
    ).strip()
    canonical_archetype_id, large_sector_id = _fixture_taxonomy(raw, trigger, role=role)
    if not canonical_archetype_id:
        return None
    market = _market_value(trigger.get("market") or candidate.get("market"))
    parsed_fields = _runtime_fields_from_fixture_row(raw, trigger, canonical_archetype_id=canonical_archetype_id)
    text = _fixture_text(raw, trigger)
    published_at = datetime(row_date.year, row_date.month, row_date.day, 8, 0)
    source_url = _source_identifier(candidate, trigger, source_file)
    evidence_id = _evidence_id(symbol, row_date, canonical_archetype_id, role, candidate.get("trigger_id") or candidate.get("case_id"))
    runtime_primitives, cleared_guard_primitives = _claim_primitives_from_fixture(
        raw,
        trigger,
        parsed_fields,
        canonical_archetype_id=canonical_archetype_id,
    )
    primitive_claims = compile_claims_from_primitives(
        evidence_id=evidence_id,
        symbol=symbol,
        as_of_date=row_date,
        primitive_ids=runtime_primitives,
        archetype_id=canonical_archetype_id,
        subject=company_name,
        quote_text=text[:1_000],
        source_url=source_url,
        source_tier=int(SourceTier.TIER_1),
        confidence=0.92,
        verified=True,
    )
    cleared_guard_claims = compile_claims_from_primitives(
        evidence_id=evidence_id,
        symbol=symbol,
        as_of_date=row_date,
        primitive_ids=cleared_guard_primitives,
        archetype_id=canonical_archetype_id,
        subject=company_name,
        quote_text=text[:1_000],
        source_url=source_url,
        source_tier=int(SourceTier.TIER_1),
        confidence=0.92,
        verified=True,
        polarity="negative",
    )
    field_claims = compile_claims_from_parsed_fields(
        evidence_id=evidence_id,
        symbol=symbol,
        as_of_date=row_date,
        parsed_fields=parsed_fields,
        archetype_id=canonical_archetype_id,
        subject=company_name,
        quote_text=text[:1_000],
        source_url=source_url,
        source_tier=int(SourceTier.TIER_1),
        confidence=0.92,
        max_claims=160,
    )
    compiled_claims = tuple(
        {
            claim.claim_id: claim
            for claim in (*primitive_claims, *cleared_guard_claims, *field_claims)
        }.values()
    )
    parsed_fields.update(
        {
            "source_url": source_url,
            "source_file": source_file,
            "source_trigger_id": candidate.get("trigger_id") or trigger.get("trigger_id"),
            "source_case_id": candidate.get("case_id") or trigger.get("case_id"),
            "source_runtime_primitives": list(runtime_primitives),
            "source_cleared_guard_primitives": list(cleared_guard_primitives),
            "date_verified": True,
            "green_allowed_by_date": True,
            "runtime_fixture_source_backed": True,
            "canonical_archetype_id": canonical_archetype_id,
        }
    )
    if compiled_claims:
        parsed_fields.update(claim_metadata_from_claims(compiled_claims, as_of_date=row_date))
    if large_sector_id:
        parsed_fields["large_sector_id"] = large_sector_id
    report = ResearchReport(
        symbol=symbol,
        publish_date=row_date,
        broker="V12RuntimeFixture",
        title=f"{canonical_archetype_id} {role} fixture",
        as_of_date=row_date,
        target_revision_pct=parsed_fields.get("target_revision_pct"),
        fy1_sales=parsed_fields.get("fy1_sales"),
        fy1_op=parsed_fields.get("fy1_op"),
        fy1_eps=parsed_fields.get("fy1_eps"),
        fy2_sales=parsed_fields.get("fy2_sales"),
        fy2_op=parsed_fields.get("fy2_op"),
        fy2_eps=parsed_fields.get("fy2_eps"),
        order_backlog_to_sales=parsed_fields.get("order_backlog_to_sales"),
        export_ratio=parsed_fields.get("export_ratio"),
        us_revenue_ratio=parsed_fields.get("us_revenue_ratio"),
        asp_increase_mentioned=bool(parsed_fields.get("asp_increase_mentioned")),
        lead_time_mentioned=bool(parsed_fields.get("lead_time_mentioned")),
        shortage_mentioned=bool(parsed_fields.get("shortage_mentioned")),
        raw_text=text,
        parsed_fields=parsed_fields,
    )
    evidence = Evidence(
        evidence_id=evidence_id,
        source_type="research_report",
        source_name="V12RuntimeFixture",
        source_tier=SourceTier.TIER_1,
        published_at=published_at,
        observed_at=published_at,
        available_at=published_at,
        as_of_date=row_date,
        market=market,
        symbol=symbol,
        title=report.title,
        url_or_identifier=source_url,
        excerpt_or_value=text[:240],
        parsed_fields=parsed_fields,
        confidence=0.92,
    )
    return RuntimeFixtureEvidenceRow(
        symbol=symbol,
        company_name=company_name,
        market=market,
        as_of_date=row_date,
        role=role,
        canonical_archetype_id=canonical_archetype_id,
        large_sector_id=large_sector_id,
        source_file=source_file,
        trigger_id=str(candidate.get("trigger_id") or trigger.get("trigger_id") or "") or None,
        case_id=str(candidate.get("case_id") or trigger.get("case_id") or "") or None,
        report=report,
        evidence=evidence,
    )


def _fixture_scope_from_candidate(candidate: CheapScanCandidate) -> tuple[str, str] | None:
    if candidate.candidate_source_path != "runtime_fixture_spec":
        return None
    canonical_archetype_id = ""
    role = ""
    for code in candidate.reason_codes:
        text = str(code)
        if text.startswith("fixture_role:"):
            role = text.split(":", 1)[1].strip().lower()
        elif text and text != "V12_RUNTIME_FIXTURE_SPEC" and not text.startswith("fixture_"):
            canonical_archetype_id = text
    if not canonical_archetype_id:
        return None
    return canonical_archetype_id, role


def _fixture_taxonomy(raw: Mapping[str, Any], trigger: Mapping[str, Any], *, role: str) -> tuple[str, str | None]:
    canonical_archetype_id = str(raw.get("canonical_archetype_id") or trigger.get("canonical_archetype_id") or "").strip()
    large_sector_id = str(raw.get("large_sector_id") or trigger.get("large_sector_id") or "").strip() or None
    if role == "green" and canonical_archetype_id.startswith("R13_"):
        source_canonical, source_large = _fixture_source_taxonomy(raw, trigger)
        if source_canonical and not source_canonical.startswith("R13_"):
            return source_canonical, source_large or large_sector_id
    return canonical_archetype_id, large_sector_id


def _fixture_source_taxonomy(raw: Mapping[str, Any], trigger: Mapping[str, Any]) -> tuple[str, str | None]:
    candidate = raw.get("candidate") if isinstance(raw.get("candidate"), Mapping) else {}
    for container in (candidate, raw, trigger):
        source_canonical = str(container.get("source_canonical_archetype_id") or "").strip()
        if source_canonical:
            source_large = str(container.get("source_large_sector_id") or "").strip() or None
            return source_canonical, source_large
    return "", None


def _row_date(candidate: Mapping[str, Any]) -> date | None:
    for key in ("as_of_date", "trigger_date", "entry_date", "date"):
        value = candidate.get(key)
        if not value:
            continue
        try:
            return date.fromisoformat(str(value)[:10])
        except ValueError:
            continue
    return None


def _source_trigger_row(path: Path, *, trigger_id: Any, case_id: Any) -> dict[str, Any]:
    wanted_trigger_id = str(trigger_id or "").strip()
    wanted_case_id = str(case_id or "").strip()
    fallback: dict[str, Any] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        if not stripped.startswith("{"):
            continue
        try:
            row = json.loads(stripped)
        except json.JSONDecodeError:
            continue
        if row.get("row_type") != "trigger":
            continue
        if not fallback:
            fallback = dict(row)
        if wanted_trigger_id and row.get("trigger_id") == wanted_trigger_id:
            return dict(row)
        if wanted_case_id and row.get("case_id") == wanted_case_id:
            return dict(row)
    return fallback


def _runtime_fields_from_fixture_row(
    raw: Mapping[str, Any],
    trigger: Mapping[str, Any],
    *,
    canonical_archetype_id: str | None = None,
) -> dict[str, Any]:
    role = str(raw.get("role") or "").strip().lower()
    fields: dict[str, Any] = {}
    if role == "green":
        _apply_green_fixture_baseline(fields)
        positive_primitives, _ = _fixture_runtime_primitive_groups(
            raw,
            trigger,
            canonical_archetype_id=canonical_archetype_id,
            role=role,
        )
        for primitive in positive_primitives:
            _apply_research_primitive(fields, str(primitive), positive=True)
    for phrase in _evidence_phrases(raw, trigger):
        _apply_research_evidence_phrase(fields, phrase)
    if role != "green":
        _apply_guard_fixture_fields(fields, raw, trigger)
    return fields


def _claim_primitives_from_fixture(
    raw: Mapping[str, Any],
    trigger: Mapping[str, Any],
    parsed_fields: Mapping[str, Any],
    *,
    canonical_archetype_id: str | None,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    role = str(raw.get("role") or "").strip().lower()
    primitives, cleared_guard_primitives = _fixture_runtime_primitive_groups(
        raw,
        trigger,
        canonical_archetype_id=canonical_archetype_id,
        role=role,
    )
    primitive_list = list(primitives)
    if role != "green":
        primitive_list.extend(
            key
            for key in (
                "missing_cashflow_bridge",
                "price_only_blowoff",
                "valuation_overheat",
                "theme_hype_without_revenue",
                "source_quality_conflict",
                "receivables_inventory_spike",
                "contract_cancelled_or_delayed",
            )
            if parsed_fields.get(key)
        )
    return (
        tuple(dict.fromkeys(str(item).strip() for item in primitive_list if str(item).strip())),
        tuple(dict.fromkeys(str(item).strip() for item in cleared_guard_primitives if str(item).strip())),
    )


def _fixture_runtime_primitive_groups(
    raw: Mapping[str, Any],
    trigger: Mapping[str, Any],
    *,
    canonical_archetype_id: str | None,
    role: str,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    primitives = list(_source_expected_runtime_primitives(raw))
    if not primitives and (role != "green" or not _green_fixture_uses_source_taxonomy(raw, trigger)):
        value = raw.get("expected_runtime_primitives")
        if isinstance(value, list):
            primitives.extend(str(item) for item in value)
    clean_primitives = tuple(dict.fromkeys(str(item).strip() for item in primitives if str(item).strip()))
    if role != "green":
        return clean_primitives, ()
    guard_primitives: set[str] = set()
    if canonical_archetype_id:
        contract = evidence_contract_for_archetype(canonical_archetype_id)
        if contract is not None:
            guard_primitives = set(contract.guard_primitives)
    positive_primitives = tuple(item for item in clean_primitives if item not in guard_primitives)
    cleared_guard_primitives = tuple(item for item in clean_primitives if item in guard_primitives)
    return positive_primitives, cleared_guard_primitives


def _source_expected_runtime_primitives(raw: Mapping[str, Any]) -> tuple[Any, ...]:
    candidate = raw.get("candidate") if isinstance(raw.get("candidate"), Mapping) else {}
    for container in (candidate, raw):
        value = container.get("source_expected_runtime_primitives")
        if isinstance(value, list):
            return tuple(value)
    return ()


def _green_fixture_uses_source_taxonomy(raw: Mapping[str, Any], trigger: Mapping[str, Any]) -> bool:
    canonical_archetype_id = str(raw.get("canonical_archetype_id") or trigger.get("canonical_archetype_id") or "")
    source_canonical, _source_large = _fixture_source_taxonomy(raw, trigger)
    return bool(canonical_archetype_id.startswith("R13_") and source_canonical and not source_canonical.startswith("R13_"))


def _apply_green_fixture_baseline(fields: dict[str, Any]) -> None:
    fields.setdefault("financial_actuals_present", True)
    fields.setdefault("actual_op_yoy_pct", 120.0)
    fields.setdefault("actual_eps_yoy_pct", 120.0)
    fields.setdefault("actual_sales_yoy_pct", 70.0)
    fields.setdefault("actual_fcf_yoy_pct", 60.0)
    fields.setdefault("opm_expansion_pctp", 10.0)
    fields.setdefault("fcf_growth_pct", 60.0)
    fields.setdefault("eps_revision_pct", 45.0)
    fields.setdefault("op_revision_pct", 45.0)
    fields.setdefault("fcf_revision_pct", 35.0)
    fields.setdefault("target_price_revision_pct", 40.0)
    fields.setdefault("target_revision_pct", 40.0)
    fields.setdefault("target_multiple_delta", 5.0)
    fields.setdefault("target_multiple_before", 8.0)
    fields.setdefault("target_multiple_after", 13.0)
    fields.setdefault("est_per", 8.0)
    fields.setdefault("est_pbr", 1.0)
    fields.setdefault("market_frame_shift", True)
    fields.setdefault("capa_expansion_pct", 50.0)
    fields.setdefault("capex_to_sales", 0.20)
    fields.setdefault("disciplined_capex", True)
    fields.setdefault("capacity_precommitted", True)
    fields.setdefault("fy1_sales", 100.0)
    fields.setdefault("fy2_sales", 145.0)
    fields.setdefault("fy1_op", 100.0)
    fields.setdefault("fy2_op", 185.0)
    fields.setdefault("fy1_eps", 100.0)
    fields.setdefault("fy2_eps", 180.0)
    fields.setdefault("estimate_upgrade_mentioned", True)
    fields.setdefault("forward_estimate_present", True)


def _apply_research_primitive(fields: dict[str, Any], primitive: str, *, positive: bool) -> None:
    lowered = primitive.lower()
    if positive and primitive in {
        "cost_overrun",
        "binary_event_unresolved",
        "approval_not_confirmed",
        "safety_signal",
        "cash_runway_risk",
        "policy_reversal_risk",
        "funding_cost_risk",
        "event_spread_risk",
        "capex_cycle_risk",
        "call_off_risk",
        "raw_material_cost_risk",
        "regulatory_risk",
        "token_or_theme_hype_risk",
        "inventory_spike",
        "policy_headline_only",
        "valuation_overheat",
        "price_only_blowoff",
        "high_mae_history",
        "execution_risk_score",
        "positioning_reversal_risk",
    }:
        fields[f"{primitive}_monitored"] = True
        if primitive == "cost_overrun":
            fields["cost_rate_improvement"] = True
            fields["margin_bridge_visible"] = True
            fields["high_margin_mix_improvement"] = True
        return
    numeric_defaults = {
        "order_backlog_to_sales": 1.4,
        "contract_amount_to_prior_sales": 0.6,
        "contract_duration_months": 36.0,
        "export_growth_pct": 80.0,
        "volume_growth_pct": 35.0,
        "arr_growth_pct": 45.0,
        "nrr": 125.0,
        "roe": 12.0,
        "pbr_e": 0.8,
        "k_ics_ratio": 190.0,
        "spread_expansion_pct": 25.0,
    }
    if primitive in numeric_defaults:
        fields[primitive] = numeric_defaults[primitive]
    else:
        fields[primitive] = True
    _apply_primitive_semantic_aliases(fields, primitive, lowered)


def _apply_primitive_semantic_aliases(fields: dict[str, Any], primitive: str, lowered: str) -> None:
    if any(token in lowered for token in ("order", "backlog", "book", "contract", "award", "project")):
        fields["record_backlog"] = True
        fields["backlog_visibility"] = True
        fields.setdefault("order_backlog_to_sales", 1.0)
        fields["delivery_schedule"] = True
        fields["order_to_revenue_bridge"] = True
    if any(token in lowered for token in ("customer", "partner", "platform", "distribution", "channel", "volume")):
        fields["named_customer_quality"] = True
        fields["customer_quality_visible"] = True
    if any(token in lowered for token in ("margin", "profit", "spread", "mix", "leverage", "cash", "collection")):
        fields["margin_bridge_visible"] = True
        fields["high_margin_mix_improvement"] = True
        fields["pricing_power_confirmed"] = True
    if any(token in lowered for token in ("capacity", "utilization", "capa", "slot", "jv")):
        fields["capacity_constraint"] = True
        fields["capacity_precommitted"] = True
        fields["booked_out_capacity"] = True
    if any(token in lowered for token in ("pricing", "price", "asp", "spread")):
        fields["pricing_power_mentioned"] = True
        fields["pricing_power_confirmed"] = True
        fields["asp_increase_mentioned"] = True
    if any(token in lowered for token in ("export", "global", "overseas")):
        fields["export_channel_expansion"] = True
        fields["overseas_channel_expansion"] = True
        fields["channel_expansion"] = True
        fields["export_growth_mentioned"] = True
    if any(token in lowered for token in ("repeat", "reorder", "sell_through", "retention", "renewal", "recurring")):
        fields["repeat_order_confirmed"] = True
        fields["channel_reorder_confirmed"] = True
        fields["recurring_consumer_demand"] = True
        fields["retention_or_renewal"] = True
    if any(token in lowered for token in ("approval", "regulatory", "reimbursement", "royalty")):
        fields["regulatory_approval_confirmed"] = True
        fields["approval_to_revenue_bridge"] = True
        fields["reimbursement_confirmed"] = True
        fields["royalty_route"] = True
        fields["partner_economics_visible"] = True
    if any(token in lowered for token in ("capital", "dividend", "buyback", "roe", "pbr", "treasury")):
        fields["capital_return_execution"] = True
        fields["shareholder_return_execution"] = True
        fields["treasury_share_cancellation"] = True
    if any(token in lowered for token in ("reserve", "loss_ratio", "k_ics", "csm")):
        fields["reserve_quality_visible"] = True
        fields["loss_ratio_quality"] = True
        fields["csm_growth_visible"] = True
    if any(token in lowered for token in ("arr", "nrr", "software", "seat", "ad_revenue", "arpu", "ip_monetization")):
        fields["arr_growth_visible"] = True
        fields["retention_or_renewal"] = True
        fields["contract_renewal_visible"] = True
        fields["seat_expansion_visible"] = True
        fields["recurring_margin_leverage"] = True
    if any(token in lowered for token in ("policy", "subsidy", "ampc", "ira")):
        fields["policy_or_regulatory_confirmed"] = True
        fields["subsidy_capture_visible"] = True
        fields["direct_company_cash_route"] = True
    if primitive in {"order_backlog_to_sales", "record_backlog", "backlog_visibility"}:
        fields["record_backlog"] = True
        fields["backlog_visibility"] = True
    if primitive in {"fcf_quality_score", "cash_collection_visible"}:
        fields["actual_fcf_yoy_pct"] = max(float(fields.get("actual_fcf_yoy_pct", 0.0)), 60.0)
        fields["fcf_growth_pct"] = max(float(fields.get("fcf_growth_pct", 0.0)), 60.0)
    if primitive in {"medium_term_revision_visibility", "confirmed_revision"}:
        fields["estimate_upgrade_mentioned"] = True
        fields["op_revision_pct"] = max(float(fields.get("op_revision_pct", 0.0)), 45.0)
        fields["eps_revision_pct"] = max(float(fields.get("eps_revision_pct", 0.0)), 45.0)
        fields["fcf_revision_pct"] = max(float(fields.get("fcf_revision_pct", 0.0)), 35.0)
    if primitive in {"pricing_power_confirmed", "asp_increase_mentioned"}:
        fields["pricing_power_mentioned"] = True
        fields["asp_increase_mentioned"] = True
    if primitive in {"lead_time_extended", "capacity_constraint", "hbm_capacity_constraint"}:
        fields["capacity_constraint"] = True
        fields["lead_time_mentioned"] = True
    if primitive in {"datacenter_customer", "hyperscaler_customer"}:
        fields["datacenter_customer"] = True
        fields["customer_quality_visible"] = True
    if primitive in {"customer_contract", "customer_contract_visible", "revenue_visibility_contract"}:
        fields["customer_contract_visible"] = True
        fields["revenue_visibility_contract"] = True
    if primitive in {
        "contract_quality",
        "official_contract",
        "export_contract",
        "offtake_contract",
        "project_award_confirmed",
    }:
        fields["customer_contract_visible"] = True
        fields["revenue_visibility_contract"] = True
        fields["official_contract"] = True
    if primitive in {"government_customer", "sovereign_customer"}:
        fields["government_customer"] = True
        fields["named_customer_quality"] = True
        fields["customer_quality_visible"] = True
        fields["multi_year_contract"] = True
    if primitive in {
        "advanced_packaging_bottleneck",
        "equipment_order_backlog",
        "hbm_customer_order",
        "customer_preorder_or_allocation",
    }:
        fields["advanced_packaging_bottleneck"] = True
        fields["capacity_constraint"] = True
        fields["capacity_precommitted"] = True
        fields["booked_out_capacity"] = True
        fields["customer_preorder_or_allocation"] = True
    if primitive in {
        "named_cell_customers",
        "sk_on_customer",
        "silicon_anode_customer_adoption",
        "customer_supply_conversion",
        "regional_proximity_advantage",
    }:
        fields["named_customer_quality"] = True
        fields["customer_quality_visible"] = True
        fields["customer_contract_visible"] = True
        fields["revenue_visibility_contract"] = True
    if primitive in {
        "shipment_and_capacity_bridge",
        "shipment_visibility",
        "capacity_or_volume_route",
        "vehicle_model_coverage_expansion",
        "volume_visibility",
    }:
        fields["delivery_schedule"] = True
        fields["order_to_revenue_bridge"] = True
        fields["revenue_recognition_path"] = True
        fields["capacity_constraint"] = True
        fields["capacity_precommitted"] = True
        fields["volume_visibility"] = True
        fields["volume_growth_visible"] = True
        fields.setdefault("volume_growth_pct", 35.0)
    if primitive in {"survivor_reopen_positive", "silicon_anode_customer_adoption"}:
        fields["market_frame_shift"] = True
        fields["customer_quality_visible"] = True
        fields["capacity_precommitted"] = True
        fields["volume_visibility"] = True
    if primitive in {"cash_collection_visible", "accounting_to_cash_bridge", "multi_field_evidence_bridge"}:
        fields["cash_collection_visible"] = True
        fields["margin_bridge_visible"] = True
        fields["high_margin_mix_improvement"] = True
        fields["actual_fcf_yoy_pct"] = max(float(fields.get("actual_fcf_yoy_pct", 0.0)), 60.0)
    if primitive in {
        "direct_revenue_route",
        "implementation_timeline",
        "legal_overhang_removed",
        "project_export_route_reopened",
        "project_award_confirmed",
        "policy_or_regulatory_confirmed",
    }:
        fields["policy_or_regulatory_confirmed"] = True
        fields["project_award_confirmed"] = True
        fields["direct_company_cash_route"] = True
        fields["direct_revenue_route"] = True
        fields["implementation_timeline"] = True
    if primitive in {
        "supply_shortage",
        "zinc_concentrate_supply_tightness",
        "named_counterparty_TC_benchmark",
        "direct_smelter_economics",
        "pricing_power_confirmed",
    }:
        fields["supply_shortage_mentioned"] = True
        fields["structural_shortage_mentioned"] = True
        fields["pricing_power_confirmed"] = True
        fields["margin_bridge_visible"] = True
        fields["high_margin_mix_improvement"] = True
    if primitive in {"repeat_order_confirmed", "channel_reorder_confirmed"}:
        fields["repeat_order_confirmed"] = True
        fields["channel_reorder_confirmed"] = True
        fields["recurring_consumer_demand"] = True
    if primitive in {"high_margin_mix_improvement", "mix_improvement", "margin_bridge_visible"}:
        fields["margin_bridge_visible"] = True
        fields["high_margin_mix_improvement"] = True
    if primitive in {"partner_economics_visible", "low_red_team_risk"}:
        fields["partner_economics_visible"] = True
        fields["source_quality_conflict"] = False


def _evidence_phrases(raw: Mapping[str, Any], trigger: Mapping[str, Any]) -> tuple[str, ...]:
    phrases: list[str] = []
    for container in (trigger, raw.get("candidate") if isinstance(raw.get("candidate"), Mapping) else {}):
        for key in (
            "stage2_evidence_fields",
            "stage3_evidence_fields",
            "stage4b_evidence_fields",
            "stage4c_evidence_fields",
        ):
            value = container.get(key)
            if isinstance(value, list):
                phrases.extend(str(item) for item in value)
            elif value:
                phrases.append(str(value))
        for key in (
            "evidence_available_at_that_date",
            "evidence_source",
            "evidence_source_url",
            "evidence_summary",
            "notes",
            "trigger_rationale",
            "current_profile_verdict",
            "trigger_type",
        ):
            value = container.get(key)
            if isinstance(value, list):
                phrases.extend(str(item) for item in value)
            elif value not in (None, ""):
                phrases.append(str(value))
    return tuple(phrases)


def _apply_research_evidence_phrase(fields: dict[str, Any], phrase: str) -> None:
    lowered = phrase.lower()
    if any(token in lowered for token in ("backlog", "order/backlog", "named backlog")) or "수주잔고" in phrase:
        fields["record_backlog"] = True
        fields["backlog_visibility"] = True
        fields.setdefault("order_backlog_to_sales", 1.0)
    if any(token in lowered for token in ("delivery", "revenue", "order-to-revenue", "book-to-bill")) or "매출 전환" in phrase:
        fields["delivery_schedule"] = True
        fields["order_to_revenue_bridge"] = True
        fields["revenue_recognition_path"] = True
    if any(token in lowered for token in ("margin", "profit", "operating-profit", "profitability")) or any(
        token in phrase for token in ("마진", "이익", "수익성")
    ):
        fields["margin_bridge_visible"] = True
        fields["high_margin_mix_improvement"] = True
        fields["pricing_power_confirmed"] = True
    if any(token in lowered for token in ("customer", "nvidia", "global customers", "anchor customer")) or "고객" in phrase:
        fields["named_customer_quality"] = True
        fields["customer_quality_visible"] = True
    if any(token in lowered for token in ("datacenter", "data center", "server power")) or "데이터센터" in phrase:
        fields["datacenter_customer"] = True
        fields["data_center_contract"] = True
        fields["power_capacity_constraint"] = True
    if any(token in lowered for token in ("capacity", "allocation", "sold-out", "sold out", "pre-sold")) or "완판" in phrase:
        fields["capacity_constraint"] = True
        fields["capacity_precommitted"] = True
        fields["booked_out_capacity"] = True
        fields["customer_preorder_or_allocation"] = True
    if "hbm" in lowered:
        fields["hbm_context_mentioned"] = True
        fields["hbm_demand_mentioned"] = True
        fields["hbm_capacity_constraint"] = True
    if any(token in lowered for token in ("revision", "confirmed_revision", "earnings expansion", "target price")):
        fields["estimate_upgrade_mentioned"] = True
        fields.setdefault("target_price_revision_pct", 35.0)
    if any(token in lowered for token in ("sellthrough", "sell-through", "reorder", "repeat order")) or "리오더" in phrase:
        fields["sell_through_confirmed"] = True
        fields["repeat_order_confirmed"] = True
        fields["channel_reorder_confirmed"] = True
    if any(token in lowered for token in ("distribution", "channel", "global launch")) or any(token in phrase for token in ("유통", "해외")):
        fields["platform_distribution_scale"] = True
        fields["export_channel_expansion"] = True
        fields["overseas_channel_expansion"] = True
        fields["channel_expansion"] = True
    if any(token in lowered for token in ("brand", "indie")):
        fields["brand_customer_diversification"] = True
    if "equipment order recovery" in lowered or "수주 회복" in phrase:
        fields["equipment_order_recovery"] = True
        fields["equipment_order_backlog"] = True
        fields["order_to_revenue_bridge"] = True
    if any(token in lowered for token in ("approval", "reimbursement", "royalty", "partner economics")):
        fields["regulatory_approval_confirmed"] = True
        fields["approval_to_revenue_bridge"] = True
        fields["reimbursement_confirmed"] = True
    if any(token in lowered for token in ("capital return", "dividend", "cancellation", "roe", "pbr")):
        fields["capital_return_execution"] = True
        fields["shareholder_return_execution"] = True
    if any(token in lowered for token in ("reserve", "k-ics", "loss ratio")):
        fields["reserve_release_quality"] = True
        fields["insurance_margin_quality"] = True
    if any(token in lowered for token in ("subsidy", "policy", "award", "project")):
        fields["policy_or_regulatory_confirmed"] = True
        fields["project_award_confirmed"] = True
        fields["direct_company_cash_route"] = True


def _apply_guard_fixture_fields(fields: dict[str, Any], raw: Mapping[str, Any], trigger: Mapping[str, Any]) -> None:
    haystack = " ".join(_evidence_phrases(raw, trigger)).lower()
    fields["missing_cashflow_bridge"] = True
    if any(token in haystack for token in ("quadrupled", "blowoff", "overhang", "late", "valuation", "price")):
        fields["price_only_blowoff"] = True
        fields["valuation_overheat"] = True
    if any(token in haystack for token in ("theme", "narrative", "headline")):
        fields["theme_hype_without_revenue"] = True
    if any(token in haystack for token in ("qualification lag", "not enough", "absent", "false", "weak", "caution")):
        fields["source_quality_conflict"] = True
    if any(token in haystack for token in ("inventory", "overhang")):
        fields["receivables_inventory_spike"] = True
    if any(token in haystack for token in ("cancel", "delay", "call-off")):
        fields["contract_cancelled_or_delayed"] = True


def _fixture_text(raw: Mapping[str, Any], trigger: Mapping[str, Any]) -> str:
    primitive_text = ", ".join(str(item) for item in raw.get("expected_runtime_primitives") or ())
    phrase_text = "\n".join(_evidence_phrases(raw, trigger))
    return "\n".join(part for part in (primitive_text, phrase_text) if part)


def _source_identifier(candidate: Mapping[str, Any], trigger: Mapping[str, Any], source_file: str) -> str:
    for container in (candidate, trigger):
        for key in ("evidence_source", "evidence_source_url", "evidence_url", "url"):
            value = container.get(key)
            if isinstance(value, list) and value:
                return str(value[0])
            if value not in (None, ""):
                return str(value)
    return source_file


def _market_value(value: Any) -> Market:
    try:
        return Market(str(value or "KR"))
    except ValueError:
        return Market.KR


def _evidence_id(symbol: str, row_date: date, canonical: str, role: str, unique: Any) -> str:
    raw = f"{symbol}:{row_date.isoformat()}:{canonical}:{role}:{unique or ''}"
    return f"runtime-fixture:{hashlib.sha1(raw.encode('utf-8')).hexdigest()[:16]}"


__all__ = ["RuntimeFixtureEvidenceRow", "RuntimeFixtureEvidenceStore"]
