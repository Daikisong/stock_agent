"""Compatibility-era case inventory compiler owned by Research Brain."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.compiler.legacy_source_quality import (
    extract_urls,
    infer_source_families,
    infer_source_quality,
    source_quality_flags,
)
from e2r.research_brain.corpus.legacy_file_scanner import scan_research_files


ARCHETYPE_SHORT_RE = re.compile(r"\b(C\d{2}|R13)\b")
SYMBOL_RE = re.compile(r"\b\d{6}\b")


@dataclass(frozen=True)
class ResearchCaseRecord:
    research_case_id: str
    source_file: str
    canonical_archetype_id: str
    large_sector_id: str | None
    symbol: str | None
    company_name: str | None
    trigger_type: str
    trigger_date: str | None
    case_role: str
    evidence_family: str
    source_urls: list[str]
    source_quality: str
    source_proxy_only: bool
    evidence_url_pending: bool
    production_scoring_changed: bool
    shadow_weight_only: bool
    runtime_score_eligible: bool
    primitive_bridge_positive: list[str]
    primitive_bridge_missing: list[str]
    green_blockers: list[str]
    false_positive_patterns: list[str]
    stage_cap_rules: list[str]
    runtime_source_route_hints: list[str]
    price_path_metrics: dict[str, Any]
    do_not_promote_reason: str | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _load_contracts(repo_root: Path) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    v12 = json.loads((repo_root / "configs" / "e2r_archetype_evidence_contracts_v12.json").read_text(encoding="utf-8"))
    contracts: dict[str, dict[str, Any]] = {}
    by_short: dict[str, str] = {}
    for row in v12.get("contracts", []):
        archetype_id = row.get("canonical_archetype_id") or row.get("archetype_id")
        if not archetype_id:
            continue
        contracts[archetype_id] = row
        by_short[archetype_id.split("_", 1)[0]] = archetype_id
    return contracts, by_short


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def _detect_archetypes(path: Path, text: str, by_short: Mapping[str, str]) -> list[str]:
    haystack = f"{path.name}\n{text[:20000]}"
    found: list[str] = []
    for short, full in by_short.items():
        if full in haystack or short in path.name or re.search(rf"\b{re.escape(short)}\b", haystack):
            found.append(full)
    if found:
        return sorted(set(found))
    match = ARCHETYPE_SHORT_RE.search(path.name)
    if match and match.group(1) in by_short:
        return [by_short[match.group(1)]]
    return []


def _case_role(text: str) -> str:
    lower = text.lower()
    if "4c" in lower or "hard break" in lower:
        return "4C"
    if "4b" in lower or "watch" in lower:
        return "4B"
    if "false positive" in lower or "guard" in lower or "반례" in lower:
        return "guard"
    if "counterexample" in lower:
        return "counterexample"
    if "profile" in lower or "stage2 cap" in lower:
        return "profile_cap"
    if "green" in lower:
        return "stage3_green"
    if "yellow" in lower:
        return "stage3_yellow"
    if "stage2" in lower or "actionable" in lower:
        return "stage2_actionable"
    return "positive"


def _trigger_type(text: str) -> str:
    lower = text.lower()
    if "contract" in lower or "수주" in lower or "공급계약" in lower:
        return "contract_or_order"
    if "hbm" in lower or "capacity" in lower or "capa" in lower:
        return "capacity_or_shortage"
    if "clinical" in lower or "endpoint" in lower or "임상" in lower:
        return "clinical_or_regulatory"
    if "arr" in lower or "rpo" in lower or "retention" in lower:
        return "software_recurring_revenue"
    if "spread" in lower or "commodity" in lower or "원자재" in lower:
        return "spread_or_commodity"
    if "audit" in lower or "accounting" in lower or "감사" in lower:
        return "risk_or_accounting"
    return "research_case"


def _patterns(text: str, needles: list[str]) -> list[str]:
    lower = text.lower()
    return [needle for needle in needles if needle.lower() in lower]


def _price_metrics(text: str) -> dict[str, Any]:
    lower = text.lower()
    metrics: dict[str, Any] = {}
    for key in ("mfe", "mae", "price_path", "return", "수익률"):
        if key in lower:
            metrics[key] = "mentioned_in_research_only"
    return metrics


def _record_id(path: Path, archetype_id: str, text: str) -> str:
    digest = hashlib.sha1(f"{path.as_posix()}::{archetype_id}::{text[:2000]}".encode("utf-8")).hexdigest()[:20]
    return f"RCASE-{digest}"


def extract_research_cases(
    *,
    repo_root: str | Path = ".",
    max_chars_per_file: int = 24000,
) -> list[ResearchCaseRecord]:
    root = Path(repo_root)
    contracts, by_short = _load_contracts(root)
    records: list[ResearchCaseRecord] = []
    for path in scan_research_files(root):
        text = _read_text(path)
        if not text:
            continue
        sample = text[:max_chars_per_file]
        archetype_ids = _detect_archetypes(path.relative_to(root), sample, by_short)
        if not archetype_ids:
            continue
        urls = extract_urls(sample)
        source_quality = infer_source_quality(sample, urls)
        flags = source_quality_flags(source_quality)
        source_families = infer_source_families(urls, sample)
        symbol_match = SYMBOL_RE.search(path.name) or SYMBOL_RE.search(sample[:2000])
        case_role = _case_role(sample)
        for archetype_id in archetype_ids:
            contract = contracts[archetype_id]
            required = list(contract.get("required_primitives") or [])
            positive = _patterns(sample, required + list(contract.get("positive_primitives") or []))
            missing = [primitive for primitive in required if primitive not in positive]
            green_blockers = _patterns(sample, ["green_blocker", "green gap", "green_gate", "required_positive_missing"])
            false_positive = _patterns(sample, ["false_positive", "false positive", "profile only", "sympathy", "keyword only"])
            stage_caps = _patterns(sample, ["stage2 cap", "stage cap", "yellow gate", "green gate", "4b", "4c"])
            evidence_family = source_families[0] if source_families else "ResearchMemory"
            rel = path.relative_to(root).as_posix()
            records.append(
                ResearchCaseRecord(
                    research_case_id=_record_id(path.relative_to(root), archetype_id, sample),
                    source_file=rel,
                    canonical_archetype_id=archetype_id,
                    large_sector_id=contract.get("large_sector_id"),
                    symbol=symbol_match.group(0) if symbol_match else None,
                    company_name=None,
                    trigger_type=_trigger_type(sample),
                    trigger_date=None,
                    case_role=case_role,
                    evidence_family=evidence_family,
                    source_urls=urls[:20],
                    source_quality=source_quality,
                    source_proxy_only=flags["source_proxy_only"],
                    evidence_url_pending=flags["evidence_url_pending"],
                    production_scoring_changed=False,
                    shadow_weight_only=flags["shadow_weight_only"],
                    runtime_score_eligible=False,
                    primitive_bridge_positive=sorted(set(positive)),
                    primitive_bridge_missing=missing,
                    green_blockers=green_blockers,
                    false_positive_patterns=false_positive,
                    stage_cap_rules=stage_caps,
                    runtime_source_route_hints=source_families,
                    price_path_metrics=_price_metrics(sample),
                    do_not_promote_reason="source_proxy_only_planning_only"
                    if flags["source_proxy_only"]
                    else ("price_path_outcome_not_runtime_prompt" if flags["shadow_weight_only"] else None),
                )
            )
    return records


__all__ = ["ResearchCaseRecord", "extract_research_cases"]
