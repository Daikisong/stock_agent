"""Blind-safe ResearchPacketV1 builder and deterministic packet bundle writer."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

from e2r.research_brain.researcher_mode.schemas import (
    ComponentAnchor,
    HistoricalResearchJudgment,
)

from .ids import canonical_hash, canonical_json, stable_id
from .models import ResearchMode


PACKET_SCHEMA_VERSION = "e2r_pro_research_packet_v1"
DOSSIER_SCHEMA_VERSION = "e2r_pro_research_dossier_v1"


@dataclass(frozen=True)
class DeltaResearchContext:
    prior_receipt: Mapping[str, Any] | None
    new_events: tuple[Mapping[str, Any], ...]
    new_or_superseding_facts: tuple[Mapping[str, Any], ...]
    components_to_revisit: tuple[str, ...]

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "prior_receipt": _json_copy(self.prior_receipt),
            "new_events": _json_copy(self.new_events),
            "new_or_superseding_facts": _json_copy(self.new_or_superseding_facts),
            "components_to_revisit": sorted(set(self.components_to_revisit)),
            "prior_receipt_is_current_authority": False,
        }


@dataclass(frozen=True)
class PacketBuildInput:
    job_id: str
    symbol: str
    company_name: str
    as_of_date: str
    latest_trading_snapshot_date: str
    research_mode: str | ResearchMode
    aliases: tuple[str, ...] = ()
    run_id: str | None = None
    trigger_summary: tuple[Mapping[str, Any], ...] = ()
    candidate_archetypes: tuple[str, ...] = ()
    business_snapshot: Mapping[str, Any] = field(default_factory=dict)
    structured_financial_snapshot: Mapping[str, Any] = field(default_factory=dict)
    revision_valuation_snapshot: Mapping[str, Any] = field(default_factory=dict)
    existing_thesis_digest: Mapping[str, Any] | None = None
    historical_judgments: tuple[HistoricalResearchJudgment | Mapping[str, Any], ...] = ()
    component_anchors: tuple[ComponentAnchor | Mapping[str, Any], ...] = ()
    known_positive_facts: tuple[Mapping[str, Any], ...] = ()
    known_counterfacts: tuple[Mapping[str, Any], ...] = ()
    research_objectives: tuple[str, ...] = ()
    source_preferences: tuple[str, ...] = ()
    forbidden_inferences: tuple[str, ...] = ()
    delta_context: DeltaResearchContext | None = None


@dataclass(frozen=True)
class ResearchPacketV1:
    payload: Mapping[str, Any]
    packet_hash: str

    def to_json(self) -> str:
        return json.dumps(
            self.payload,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        ) + "\n"

    def to_markdown(self) -> str:
        target = self.payload["target"]
        return (
            "# E2R Pro Research Packet\n\n"
            f"- job_id: `{self.payload['job_id']}`\n"
            f"- run_id: `{self.payload['run_id']}`\n"
            f"- target: `{target['symbol']} {target['company_name']}`\n"
            f"- as_of_date: `{self.payload['as_of_date']}`\n"
            f"- research_mode: `{self.payload['research_mode']}`\n"
            "- score_authority: `false`\n"
            "- stage_authority: `false`\n\n"
            "```json\n"
            f"{self.to_json()}```\n"
        )


@dataclass(frozen=True)
class PacketBundleReceipt:
    packet_directory: Path
    research_packet_json: Path
    research_packet_markdown: Path
    packet_manifest: Path
    packet_hash: str
    manifest_hash: str


class ResearchPacketBuilder:
    def __init__(self, schema_path: str | Path | None = None) -> None:
        default = Path(__file__).resolve().parents[3] / "configs" / "e2r_pro_research_packet_v1.schema.json"
        self.schema_path = Path(schema_path) if schema_path else default
        self.schema = json.loads(self.schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(self.schema)
        self.validator = Draft202012Validator(self.schema, format_checker=FormatChecker())

    def build(self, request: PacketBuildInput) -> ResearchPacketV1:
        cutoff = date.fromisoformat(request.as_of_date)
        trading_date = date.fromisoformat(request.latest_trading_snapshot_date)
        if trading_date > cutoff:
            raise ValueError("latest trading snapshot date exceeds as_of_date")
        mode = ResearchMode(request.research_mode)
        run_id = request.run_id or stable_id(
            "PRORUN",
            {
                "job_id": request.job_id,
                "as_of_date": request.as_of_date,
                "research_mode": mode.value,
                "trigger_summary": request.trigger_summary,
            },
        )
        if mode is ResearchMode.DELTA_RESEARCH:
            if request.existing_thesis_digest is None or request.delta_context is None:
                raise ValueError("DELTA_RESEARCH requires an existing thesis and delta context")
            delta_context = request.delta_context.to_dict()
            business_snapshot: Mapping[str, Any] = {}
            financial_snapshot: Mapping[str, Any] = {}
            revision_snapshot: Mapping[str, Any] = {}
            historical_digest: Sequence[Mapping[str, Any]] = ()
            positives: Sequence[Mapping[str, Any]] = ()
            counters: Sequence[Mapping[str, Any]] = ()
            objectives: Sequence[str] = ()
            triggers = delta_context["new_events"]
        else:
            if request.delta_context is not None:
                raise ValueError("delta context is only valid for DELTA_RESEARCH")
            delta_context = None
            business_snapshot = request.business_snapshot
            financial_snapshot = request.structured_financial_snapshot
            revision_snapshot = request.revision_valuation_snapshot
            historical_digest = build_blind_historical_anchor_digest(
                request.historical_judgments,
                request.component_anchors,
            )
            positives = request.known_positive_facts
            counters = request.known_counterfacts
            objectives = request.research_objectives
            triggers = request.trigger_summary

        payload: Mapping[str, Any] = {
            "schema_version": PACKET_SCHEMA_VERSION,
            "job_id": request.job_id,
            "run_id": run_id,
            "target": {
                "symbol": request.symbol,
                "company_name": request.company_name,
                "aliases": sorted(set(request.aliases)),
            },
            "as_of_date": request.as_of_date,
            "latest_trading_snapshot_date": request.latest_trading_snapshot_date,
            "research_mode": mode.value,
            "trigger_summary": _json_copy(triggers),
            "candidate_archetypes": sorted(set(request.candidate_archetypes)),
            "business_snapshot": _json_copy(business_snapshot),
            "structured_financial_snapshot": _json_copy(financial_snapshot),
            "revision_valuation_snapshot": _json_copy(revision_snapshot),
            "existing_thesis_digest": _json_copy(request.existing_thesis_digest),
            "historical_anchor_digest": _json_copy(historical_digest),
            "known_positive_facts": _json_copy(positives),
            "known_counterfacts": _json_copy(counters),
            "research_objectives": sorted(set(objectives)),
            "source_preferences": tuple(dict.fromkeys(request.source_preferences)),
            "forbidden_inferences": tuple(dict.fromkeys(request.forbidden_inferences)),
            "delta_context": _json_copy(delta_context),
            "output_contract": DOSSIER_SCHEMA_VERSION,
            "score_authority": False,
            "stage_authority": False,
        }
        payload = _json_copy(payload)
        _assert_no_forbidden_answer_fields(payload)
        _assert_as_of_dates(payload, cutoff)
        errors = sorted(self.validator.iter_errors(payload), key=lambda row: tuple(row.path))
        if errors:
            details = "; ".join(
                f"{'/'.join(str(item) for item in error.path) or '$'}: {error.message}"
                for error in errors
            )
            raise ValueError(f"ResearchPacketV1 schema validation failed: {details}")
        return ResearchPacketV1(payload=payload, packet_hash=canonical_hash(payload))


def build_blind_historical_anchor_digest(
    judgments: Sequence[HistoricalResearchJudgment | Mapping[str, Any]],
    component_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    digest: list[Mapping[str, Any]] = []
    for judgment in judgments:
        if isinstance(judgment, HistoricalResearchJudgment):
            runtime = judgment.to_runtime_anchor()
        else:
            runtime = dict(judgment)
        if runtime.get("company_name_conditioned") or runtime.get("target_symbol_conditioned"):
            raise ValueError("target-conditioned historical judgment is forbidden")
        digest.append(
            {
                "digest_kind": "HISTORICAL_JUDGMENT",
                "judgment_id": runtime.get("judgment_id"),
                "archetype_id": runtime.get("archetype_id"),
                "as_of_date": runtime.get("as_of_date"),
                "source_quality": runtime.get("source_quality"),
                "fact_signatures": list(runtime.get("fact_signatures") or ())[:3],
                "counter_fact_signatures": list(
                    runtime.get("counter_fact_signatures") or ()
                )[:3],
                "usable_as_ordinal_anchor": bool(
                    runtime.get("usable_as_ordinal_anchor", False)
                ),
                "anchor_confidence": runtime.get("anchor_confidence"),
                "historical_score_or_stage_exposed": False,
            }
        )

    counts: dict[tuple[str, str], int] = {}
    for anchor in component_anchors:
        value = anchor.to_dict() if isinstance(anchor, ComponentAnchor) else dict(anchor)
        if value.get("company_name_conditioned") or value.get("target_symbol_conditioned"):
            raise ValueError("target-conditioned component anchor is forbidden")
        component_id = str(value.get("component_id") or "")
        if not component_id:
            raise ValueError("component anchor requires component_id")
        role = str(value.get("role") or "POSITIVE").upper()
        direction = "COUNTER" if any(token in role for token in ("COUNTER", "RISK", "NEGATIVE")) else "POSITIVE"
        count_key = (component_id, direction)
        if counts.get(count_key, 0) >= 3:
            continue
        counts[count_key] = counts.get(count_key, 0) + 1
        proxy_guard = bool(value.get("source_proxy_guard_case_ids")) or not bool(
            value.get("source_backed_case_ids")
        )
        row: dict[str, Any] = {
            "digest_kind": "COMPONENT_ANCHOR",
            "anchor_id": value.get("anchor_id"),
            "archetype_id": value.get("archetype_id"),
            "component_id": component_id,
            "direction": direction,
            "economic_fact_patterns": list(value.get("economic_fact_patterns") or ()),
            "role": value.get("role"),
            "confidence": value.get("confidence"),
            "usable_as_exact_anchor": bool(value.get("usable_as_exact_anchor"))
            and not proxy_guard,
            "usable_as_ordinal_anchor": bool(value.get("usable_as_ordinal_anchor")),
            "guard_only": proxy_guard,
        }
        if not proxy_guard:
            row.update(
                {
                    "score_band": value.get("score_band"),
                    "points_lower": value.get("points_lower"),
                    "points_mid": value.get("points_mid"),
                    "points_upper": value.get("points_upper"),
                    "max_points": value.get("max_points"),
                }
            )
        digest.append(row)
    return tuple(_json_copy(digest))


def write_packet_bundle(
    packet: ResearchPacketV1,
    packet_directory: str | Path,
    *,
    commit_sha: str,
    config_hash: str,
) -> PacketBundleReceipt:
    destination = Path(packet_directory)
    destination.mkdir(parents=True, exist_ok=True)
    json_path = destination / "research_packet.json"
    markdown_path = destination / "research_packet.md"
    manifest_path = destination / "packet_manifest.json"
    manifest = {
        "job_id": packet.payload["job_id"],
        "run_id": packet.payload["run_id"],
        "packet_hash": packet.packet_hash,
        "commit_sha": commit_sha,
        "config_hash": config_hash,
        "as_of_date": packet.payload["as_of_date"],
        "target": packet.payload["target"],
    }
    _atomic_write_text(json_path, packet.to_json())
    _atomic_write_text(markdown_path, packet.to_markdown())
    _atomic_write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
    )
    return PacketBundleReceipt(
        packet_directory=destination,
        research_packet_json=json_path,
        research_packet_markdown=markdown_path,
        packet_manifest=manifest_path,
        packet_hash=packet.packet_hash,
        manifest_hash=canonical_hash(manifest),
    )


def _assert_no_forbidden_answer_fields(value: Any, path: tuple[str, ...] = ()) -> None:
    forbidden = {
        "expected_score",
        "expected_final_score",
        "expected_stage",
        "expected_final_stage",
        "final_score",
        "final_stage",
        "gold_answer",
        "gold_score",
        "gold_stage",
        "future_outcome",
        "future_outcome_ref",
        "past_price_outcome",
        "forward_return",
        "hidden_answer",
    }
    forbidden_compact = {key.replace("_", "") for key in forbidden}
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).strip().lower()
            compact = "".join(character for character in normalized if character.isalnum())
            if normalized in forbidden or compact in forbidden_compact:
                raise ValueError(
                    f"forbidden answer field in ResearchPacketV1: {'/'.join(path + (str(key),))}"
                )
            _assert_no_forbidden_answer_fields(child, path + (str(key),))
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _assert_no_forbidden_answer_fields(child, path + (str(index),))


def _assert_as_of_dates(value: Any, cutoff: date, path: tuple[str, ...] = ()) -> None:
    date_keys = {
        "as_of_date",
        "publication_date",
        "published_date",
        "filing_date",
        "event_date",
        "source_date",
        "snapshot_date",
        "latest_trading_snapshot_date",
        "receipt_as_of_date",
    }
    timestamp_keys = {"published_at", "filed_at", "event_at", "source_timestamp"}
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).strip().lower()
            if isinstance(child, str) and normalized in date_keys:
                candidate_date = date.fromisoformat(child)
                if candidate_date > cutoff:
                    raise ValueError(
                        f"future source date exceeds as_of_date: {'/'.join(path + (str(key),))}"
                    )
            elif isinstance(child, str) and normalized in timestamp_keys:
                candidate_datetime = datetime.fromisoformat(child.replace("Z", "+00:00"))
                if candidate_datetime.date() > cutoff:
                    raise ValueError(
                        f"future source timestamp exceeds as_of_date: {'/'.join(path + (str(key),))}"
                    )
            _assert_as_of_dates(child, cutoff, path + (str(key),))
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _assert_as_of_dates(child, cutoff, path + (str(index),))


def _json_copy(value: Any) -> Any:
    return json.loads(canonical_json(value))


def _atomic_write_text(path: Path, content: str) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(content, encoding="utf-8")
    os.replace(temporary, path)


__all__ = [
    "DOSSIER_SCHEMA_VERSION",
    "DeltaResearchContext",
    "PACKET_SCHEMA_VERSION",
    "PacketBuildInput",
    "PacketBundleReceipt",
    "ResearchPacketBuilder",
    "ResearchPacketV1",
    "build_blind_historical_anchor_digest",
    "write_packet_bundle",
]
