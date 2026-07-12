"""Build economic-fact component anchors from the Historical Judgment Atlas."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .schemas import AnchorConfidence, ComponentAnchor


COMPONENT_ANCHOR_SCHEMA_VERSION = "e2r_v5_component_anchor_atlas_v1"
COMPONENT_ANCHOR_PASS = "COMPONENT_ANCHOR_ATLAS_PASS"

C06_ARCHETYPE_ID = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
C06_MANDATORY_ANCHOR_FAMILIES = {
    "C06_DIRECT_SOLD_OUT_CUSTOMER_CAPACITY": {
        "role": "POSITIVE",
        "component_ids": ("earnings_visibility", "bottleneck_pricing"),
        "required_pattern_groups": (
            (r"sold_?out", r"almost_sold_out", r"booked_capacity"),
            (r"capacity", r"customer", r"hbm"),
        ),
    },
    "C06_HBM_REVENUE_MIX_RECORD_PROFIT": {
        "role": "POSITIVE",
        "component_ids": (
            "eps_fcf_explosion",
            "earnings_visibility",
            "bottleneck_pricing",
        ),
        "required_pattern_groups": (
            (r"hbm.*revenue", r"revenue.*mix", r"hbm_mix", r"dram_revenue"),
            (r"profit", r"margin", r"financial_visibility", r"earnings"),
        ),
    },
    "C06_QUALIFICATION_LAG": {
        "role": "COUNTER",
        "component_ids": ("earnings_visibility", "information_confidence"),
        "required_pattern_groups": (
            (r"qualif",),
            (r"lag", r"delay", r"fail", r"uncertainty", r"without_signed"),
        ),
    },
    "C06_REOPEN_CUSTOMER_DEPENDENCY": {
        "role": "COUNTER",
        "component_ids": ("earnings_visibility", "information_confidence"),
        "required_pattern_groups": (
            (
                r"reopen",
                r"customer_depend",
                r"customer_concentr",
                r"customer_lock_missing",
                r"customer.*dependency",
            ),
        ),
    },
    "C06_PROFILE_SUBSTRATE_SYMPATHY": {
        "role": "COUNTER",
        "component_ids": ("earnings_visibility", "bottleneck_pricing"),
        "required_pattern_groups": (
            (r"substrate", r"package", r"socket", r"pcb"),
            (r"proxy", r"absent", r"without", r"false", r"sympathy", r"premium_fail"),
        ),
    },
    "C06_LATE_CYCLE_VALUATION_PRICE_EXTENSION": {
        "role": "COUNTER",
        "component_ids": ("market_mispricing", "valuation_rerating"),
        "required_pattern_groups": (
            (
                r"valuation_blowoff",
                r"valuation.*overheat",
                r"positioning_overheat",
                r"price.*extension",
                r"price_only_local_peak",
                r"late.*cycle",
            ),
        ),
    },
}


def compile_component_anchor_atlas(
    *,
    judgments: Sequence[Mapping[str, Any]],
    fact_signatures: Sequence[Mapping[str, Any]],
    score_anchors: Sequence[Mapping[str, Any]],
    quarantine: Sequence[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    fact_by_id = {
        str(row.get("fact_signature_id") or ""): row
        for row in fact_signatures
        if row.get("fact_signature_id")
    }
    judgment_by_id = {
        str(row.get("judgment_id") or ""): row
        for row in judgments
        if row.get("judgment_id")
    }
    anchors = []
    for row in score_anchors:
        source_quality = str(row.get("source_quality") or "")
        case_id = str(row.get("research_case_id") or "")
        patterns = tuple(
            dict.fromkeys(
                str(fact_by_id.get(str(fact_id), {}).get("economic_fact_pattern") or "")
                for fact_id in row.get("fact_signature_ids") or ()
                if str(fact_by_id.get(str(fact_id), {}).get("economic_fact_pattern") or "")
            )
        )
        if not patterns:
            patterns = ("explicit_component_score_without_fact_signature",)
        maximum = float(row.get("max_points") or 0.0)
        points = float(row.get("points") or 0.0)
        tolerance = maximum * 0.05
        source_backed = source_quality.startswith("SOURCE_BACKED")
        source_proxy = source_quality == "SOURCE_PROXY_ONLY"
        exact = bool(row.get("usable_as_exact_anchor")) and source_backed and not source_proxy
        anchor = ComponentAnchor(
            anchor_id=stable_intelligence_id(
                "CANCH",
                {
                    "score_anchor_id": row.get("anchor_id"),
                    "patterns": patterns,
                },
            ),
            archetype_id=str(row.get("archetype_id") or ""),
            component_id=str(row.get("component_id") or ""),
            economic_fact_patterns=patterns,
            role=str(row.get("role") or "POSITIVE"),
            score_band=str(row.get("score_band") or "ZERO"),
            points_lower=round(max(0.0, points - tolerance), 6),
            points_mid=round(points, 6),
            points_upper=round(min(maximum, points + tolerance), 6),
            max_points=maximum,
            source_backed_case_ids=(case_id,) if source_backed else (),
            source_proxy_guard_case_ids=(case_id,) if source_proxy else (),
            source_score_anchor_ids=(str(row.get("anchor_id") or ""),),
            confidence=(
                AnchorConfidence.HIGH.value
                if exact
                else AnchorConfidence.MEDIUM.value
                if source_backed
                else AnchorConfidence.LOW.value
            ),
            usable_as_exact_anchor=exact,
            usable_as_ordinal_anchor=bool(row.get("usable_as_ordinal_anchor")),
        )
        anchors.append(anchor)
    anchors = sorted(anchors, key=lambda row: row.anchor_id)

    registry_ids = sorted({str(row.get("archetype_id") or "") for row in judgments})
    component_ids = sorted(
        {
            str(component_id)
            for row in judgments
            for component_id in (row.get("component_max_points") or {})
        }
    )
    coverage = _coverage_matrix(anchors, registry_ids, component_ids)
    role_exemplars = _archetype_role_exemplars(
        judgments=judgments,
        fact_by_id=fact_by_id,
        registry_ids=registry_ids,
    )
    mandatory_c06 = _mandatory_c06_anchors(
        judgments=judgments,
        fact_signatures=fact_signatures,
        score_anchors=score_anchors,
    )
    conflict_judgment_ids = {
        str(row.get("judgment_id") or "")
        for row in judgments
        if row.get("score_conflict") is True
    }
    quarantined_conflict_cases = {
        str(row.get("research_case_id") or "")
        for row in quarantine
        if row.get("reason") == "CONFLICTING_SCORE_ROWS"
    }
    conflict_case_ids = {
        str(judgment_by_id[judgment_id].get("research_case_id") or "")
        for judgment_id in conflict_judgment_ids
        if judgment_id in judgment_by_id
    }
    role_counts = Counter(row["role"] for row in role_exemplars if not row["explicit_gap"])
    critical = {
        "component_anchor_without_ordinal_or_gap_count": sum(
            not row["ordinal_anchor_count"] and not row["explicit_gap"]
            for row in coverage
        ),
        "registry_archetype_component_roster_mismatch_count": abs(
            len(coverage) - (len(registry_ids) * len(component_ids))
        ),
        "archetype_positive_exemplar_gap_count": sum(
            row["role"] == "POSITIVE" and row["explicit_gap"] for row in role_exemplars
        ),
        "archetype_counter_exemplar_gap_count": sum(
            row["role"] == "COUNTER" and row["explicit_gap"] for row in role_exemplars
        ),
        "source_backed_high_anchor_missing_count": int(
            not any(row.usable_as_exact_anchor for row in anchors)
        ),
        "counter_anchor_missing_count": int(not any(row.role == "COUNTER" for row in anchors)),
        "source_proxy_exact_anchor_count": sum(
            row.usable_as_exact_anchor and bool(row.source_proxy_guard_case_ids)
            for row in anchors
        ),
        "anchor_conflict_not_quarantined_count": len(
            conflict_case_ids - quarantined_conflict_cases
        ),
        "company_or_symbol_conditioned_anchor_count": sum(
            row.company_name_conditioned or row.target_symbol_conditioned for row in anchors
        ),
        "c06_mandatory_anchor_family_missing_count": sum(
            not row["matched_case_ids"] for row in mandatory_c06
        ),
    }
    return {
        "schema_version": COMPONENT_ANCHOR_SCHEMA_VERSION,
        "status": COMPONENT_ANCHOR_PASS if sum(critical.values()) == 0 else "COMPONENT_ANCHOR_ATLAS_FAIL",
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "registry_archetype_count": len(registry_ids),
        "component_count": len(component_ids),
        "component_anchor_count": len(anchors),
        "exact_anchor_count": sum(row.usable_as_exact_anchor for row in anchors),
        "ordinal_anchor_count": sum(row.usable_as_ordinal_anchor for row in anchors),
        "counter_anchor_count": sum(row.role == "COUNTER" for row in anchors),
        "positive_anchor_count": sum(row.role == "POSITIVE" for row in anchors),
        "archetype_role_exemplar_counts": dict(sorted(role_counts.items())),
        "component_anchors": [row.to_dict() for row in anchors],
        "component_coverage": coverage,
        "archetype_role_exemplars": role_exemplars,
        "c06_mandatory_anchors": mandatory_c06,
        "conflict_quarantine": {
            "conflicting_judgment_count": len(conflict_judgment_ids),
            "conflicting_case_count": len(conflict_case_ids),
            "quarantined_conflicting_case_count": len(
                conflict_case_ids & quarantined_conflict_cases
            ),
        },
        "company_name_scoring_condition_allowed": False,
        "target_symbol_scoring_condition_allowed": False,
        "atlas_hash": stable_hash([row.to_dict() for row in anchors]),
    }


def compile_component_anchor_atlas_from_files(
    *,
    atlas_root: str | Path = "output/researcher_parity/judgment_atlas",
) -> Mapping[str, Any]:
    root = Path(atlas_root)
    return compile_component_anchor_atlas(
        judgments=_read_jsonl(root / "historical_judgments.jsonl"),
        fact_signatures=_read_jsonl(root / "fact_signatures.jsonl"),
        score_anchors=_read_jsonl(root / "score_anchors.jsonl"),
        quarantine=_read_jsonl(root / "quarantine.jsonl"),
    )


def write_component_anchor_atlas(
    atlas: Mapping[str, Any],
    *,
    output_path: str | Path = "docs/operational/e2r_v5_component_anchor_atlas.json",
) -> Path:
    path = Path(output_path)
    write_json(path, atlas)
    return path


def _coverage_matrix(
    anchors: Sequence[ComponentAnchor],
    registry_ids: Sequence[str],
    component_ids: Sequence[str],
) -> list[Mapping[str, Any]]:
    by_key: dict[tuple[str, str], list[ComponentAnchor]] = defaultdict(list)
    for anchor in anchors:
        by_key[(anchor.archetype_id, anchor.component_id)].append(anchor)
    rows = []
    for archetype_id in registry_ids:
        for component_id in component_ids:
            matched = by_key[(archetype_id, component_id)]
            ordinal = sum(row.usable_as_ordinal_anchor for row in matched)
            rows.append(
                {
                    "archetype_id": archetype_id,
                    "component_id": component_id,
                    "anchor_count": len(matched),
                    "exact_anchor_count": sum(row.usable_as_exact_anchor for row in matched),
                    "ordinal_anchor_count": ordinal,
                    "positive_anchor_count": sum(row.role == "POSITIVE" for row in matched),
                    "counter_anchor_count": sum(row.role == "COUNTER" for row in matched),
                    "explicit_gap": not ordinal,
                    "gap_reason": (
                        "NO_COMPONENT_SCORE_ROW_IN_HISTORICAL_CORPUS"
                        if not ordinal
                        else None
                    ),
                }
            )
    return rows


def _archetype_role_exemplars(
    *,
    judgments: Sequence[Mapping[str, Any]],
    fact_by_id: Mapping[str, Mapping[str, Any]],
    registry_ids: Sequence[str],
) -> list[Mapping[str, Any]]:
    result = []
    for archetype_id in registry_ids:
        candidates = [
            row for row in judgments if row.get("archetype_id") == archetype_id
        ]
        for role, key in (
            ("POSITIVE", "fact_signatures"),
            ("COUNTER", "counter_fact_signatures"),
        ):
            ranked = sorted(
                (row for row in candidates if row.get(key)),
                key=lambda row: (
                    row.get("source_quality") == "SOURCE_BACKED_HIGH",
                    row.get("source_quality") == "SOURCE_BACKED_MEDIUM",
                    len(row.get(key) or ()),
                    str(row.get("research_case_id") or ""),
                ),
                reverse=True,
            )
            selected = ranked[0] if ranked else None
            patterns = (
                [
                    fact_by_id[str(fact_id)]["economic_fact_pattern"]
                    for fact_id in selected.get(key) or ()
                    if str(fact_id) in fact_by_id
                ]
                if selected
                else []
            )
            result.append(
                {
                    "archetype_id": archetype_id,
                    "role": role,
                    "research_case_id": (
                        selected.get("research_case_id") if selected else None
                    ),
                    "economic_fact_patterns": patterns,
                    "source_quality": selected.get("source_quality") if selected else None,
                    "reported_stage": selected.get("reported_stage") if selected else None,
                    "explicit_gap": selected is None,
                    "gap_reason": (
                        "NO_ROLE_EXEMPLAR_IN_HISTORICAL_CORPUS"
                        if selected is None
                        else None
                    ),
                    "company_name_conditioned": False,
                    "target_symbol_conditioned": False,
                }
            )
    return result


def _mandatory_c06_anchors(
    *,
    judgments: Sequence[Mapping[str, Any]],
    fact_signatures: Sequence[Mapping[str, Any]],
    score_anchors: Sequence[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    c06_facts: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in fact_signatures:
        if row.get("archetype_id") == C06_ARCHETYPE_ID:
            c06_facts[str(row.get("research_case_id") or "")].append(row)
    anchors_by_case_component: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in score_anchors:
        if row.get("archetype_id") == C06_ARCHETYPE_ID:
            anchors_by_case_component[
                (
                    str(row.get("research_case_id") or ""),
                    str(row.get("component_id") or ""),
                )
            ].append(row)
    judgment_by_case = {
        str(row.get("research_case_id") or ""): row
        for row in judgments
        if row.get("archetype_id") == C06_ARCHETYPE_ID
    }
    result = []
    for family_id, policy in C06_MANDATORY_ANCHOR_FAMILIES.items():
        matched_cases = []
        matched_fact_ids = []
        for case_id, rows in c06_facts.items():
            role_rows = [row for row in rows if row.get("role") == policy["role"]]
            haystack = " ".join(
                str(row.get("economic_fact_pattern") or "") for row in role_rows
            )
            if all(
                any(re.search(pattern, haystack, re.IGNORECASE) for pattern in group)
                for group in policy["required_pattern_groups"]
            ):
                matched_cases.append(case_id)
                matched_fact_ids.extend(
                    str(row.get("fact_signature_id") or "") for row in role_rows
                )
        matched_cases = sorted(set(matched_cases))
        related_score_anchor_ids = sorted(
            {
                str(row.get("anchor_id") or "")
                for case_id in matched_cases
                for component_id in policy["component_ids"]
                for row in anchors_by_case_component[(case_id, component_id)]
            }
        )
        source_backed_cases = sorted(
            case_id
            for case_id in matched_cases
            if str(judgment_by_case.get(case_id, {}).get("source_quality") or "").startswith(
                "SOURCE_BACKED"
            )
        )
        result.append(
            {
                "anchor_family_id": family_id,
                "archetype_id": C06_ARCHETYPE_ID,
                "role": policy["role"],
                "component_ids": list(policy["component_ids"]),
                "economic_pattern_contract": [
                    list(group) for group in policy["required_pattern_groups"]
                ],
                "matched_case_ids": matched_cases,
                "source_backed_case_ids": source_backed_cases,
                "matched_fact_signature_ids": sorted(set(matched_fact_ids)),
                "related_score_anchor_ids": related_score_anchor_ids,
                "usable_as_exact_anchor": bool(
                    source_backed_cases and related_score_anchor_ids
                ),
                "usable_as_ordinal_anchor": bool(matched_cases),
                "company_name_conditioned": False,
                "target_symbol_conditioned": False,
            }
        )
    return result


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


__all__ = [
    "C06_MANDATORY_ANCHOR_FAMILIES",
    "COMPONENT_ANCHOR_PASS",
    "COMPONENT_ANCHOR_SCHEMA_VERSION",
    "compile_component_anchor_atlas",
    "compile_component_anchor_atlas_from_files",
    "write_component_anchor_atlas",
]
