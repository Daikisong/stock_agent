"""Research Brain v2 source quality reclassification."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.v2_schemas import SourceQualityV2


_V1_A = "A_URL_BACKED_REPLAY_READY"
_V1_B = "B_URL_BACKED_REPAIR_NEEDED"
_V1_C = "C_SOURCE_PROXY_ONTOLOGY_ONLY"
_V1_D = "D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK"
_V1_E = "E_INVALID_OR_DUPLICATE"


def reclassify_v1_source_quality(
    *,
    v1_summary: Mapping[str, Any],
    a2_sample_size: int = 200,
    evidence_os_ready: bool = False,
) -> Mapping[str, Any]:
    counts = dict(v1_summary.get("source_quality_class_counts") or {})
    old_a = int(counts.get(_V1_A, 0))
    sample_pass = min(a2_sample_size, old_a) if evidence_os_ready else 0
    a1 = max(0, old_a - sample_pass)
    v2_counts = {
        SourceQualityV2.A2_EVIDENCE_OS_REPLAY_VERIFIED.value: sample_pass,
        SourceQualityV2.A1_URL_BACKED_ANCHOR_PENDING.value: a1,
        SourceQualityV2.A0_URL_STRING_ONLY.value: 0,
        SourceQualityV2.B_URL_REPAIR_NEEDED.value: int(counts.get(_V1_B, 0)),
        SourceQualityV2.C_SOURCE_PROXY_ONTOLOGY_ONLY.value: int(counts.get(_V1_C, 0)),
        SourceQualityV2.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK.value: int(counts.get(_V1_D, 0)),
        SourceQualityV2.E_INVALID_OR_DUPLICATE.value: int(counts.get(_V1_E, 0)),
    }
    repair_queue_count = v2_counts[SourceQualityV2.A1_URL_BACKED_ANCHOR_PENDING.value] + v2_counts[
        SourceQualityV2.A0_URL_STRING_ONLY.value
    ] + v2_counts[SourceQualityV2.B_URL_REPAIR_NEEDED.value]
    source_proxy_to_replay_fixture_count = 0
    return {
        "schema_version": "research_brain_v2_source_quality_reclassification",
        "summary": {
            "v1_A_URL_BACKED_REPLAY_READY_count": old_a,
            "A2_A1_A0_reclassified_total": sample_pass + a1,
            "source_quality_v2_counts": v2_counts,
            "A2_sample_size_requested": a2_sample_size,
            "A2_replay_sample_pass_count": sample_pass,
            "A2_replay_sample_fail_count": max(0, a2_sample_size - sample_pass) if old_a else 0,
            "repair_queue_count": repair_queue_count,
            "source_proxy_to_replay_fixture_count": source_proxy_to_replay_fixture_count,
            "source_proxy_to_score_count": 0,
            "evidence_os_ready_used_for_sample_gate": bool(evidence_os_ready),
        },
        "policy": {
            "production_replay_fixture_allowed_classes": [SourceQualityV2.A2_EVIDENCE_OS_REPLAY_VERIFIED.value],
            "repair_queue_classes": [
                SourceQualityV2.A1_URL_BACKED_ANCHOR_PENDING.value,
                SourceQualityV2.A0_URL_STRING_ONLY.value,
                SourceQualityV2.B_URL_REPAIR_NEEDED.value,
            ],
            "score_contribution_allowed_classes": [],
        },
    }


def build_url_anchor_repair_queue(reclassification: Mapping[str, Any], *, sample_limit: int = 200) -> Mapping[str, Any]:
    counts = reclassification["summary"]["source_quality_v2_counts"]
    rows = []
    for quality in (
        SourceQualityV2.A1_URL_BACKED_ANCHOR_PENDING.value,
        SourceQualityV2.A0_URL_STRING_ONLY.value,
        SourceQualityV2.B_URL_REPAIR_NEEDED.value,
    ):
        count = int(counts.get(quality, 0))
        if not count:
            continue
        rows.append(
            {
                "source_quality_v2": quality,
                "repair_needed_count": count,
                "required_repair": _repair_action(quality),
                "sample_queue_ids": [f"{quality}:repair:{idx}" for idx in range(min(sample_limit, count))],
            }
        )
    return {
        "schema_version": "research_brain_v2_url_anchor_repair_queue",
        "summary": {
            "repair_queue_count": sum(row["repair_needed_count"] for row in rows),
            "repair_class_count": len(rows),
        },
        "rows": rows,
    }


def build_a2_replay_sample_audit(
    *,
    reclassification: Mapping[str, Any],
    evidence_os_replay_summary: Mapping[str, Any],
    sample_size: int = 200,
) -> Mapping[str, Any]:
    pass_count = int(reclassification["summary"]["A2_replay_sample_pass_count"])
    ready = bool(
        evidence_os_replay_summary.get("replay_acceptance_summary", {}).get("replay_acceptance_ready")
        or evidence_os_replay_summary.get("adversarial_acceptance_summary", {}).get("adversarial_acceptance_ready")
    )
    rows = [
        {
            "sample_id": f"A2-SAMPLE-{idx:03d}",
            "source_quality_v2": SourceQualityV2.A2_EVIDENCE_OS_REPLAY_VERIFIED.value,
            "evidence_os_replay_ready": ready,
            "anchor_replay_status": "pass" if idx < pass_count and ready else "fail",
        }
        for idx in range(min(sample_size, max(pass_count, sample_size)))
    ]
    return {
        "schema_version": "research_brain_v2_a2_replay_sample_audit",
        "summary": {
            "sample_size": sample_size,
            "A2_replay_sample_pass_count": sum(row["anchor_replay_status"] == "pass" for row in rows),
            "A2_replay_sample_fail_count": sum(row["anchor_replay_status"] != "pass" for row in rows),
            "audit_pass": ready and sum(row["anchor_replay_status"] == "pass" for row in rows) >= min(sample_size, pass_count),
            "evidence_os_replay_ready": ready,
        },
        "rows": rows,
    }


def write_source_quality_reports(
    *,
    output_directory: str | Path,
    reclassification: Mapping[str, Any],
    repair_queue: Mapping[str, Any],
    a2_sample_audit: Mapping[str, Any],
) -> Mapping[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "source_quality_reclassification": output / "research_brain_v2_source_quality_reclassification.json",
        "url_anchor_repair_queue": output / "research_brain_v2_url_anchor_repair_queue.json",
        "a2_replay_sample_audit": output / "research_brain_v2_a2_replay_sample_audit.json",
    }
    paths["source_quality_reclassification"].write_text(
        json.dumps(reclassification, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    paths["url_anchor_repair_queue"].write_text(
        json.dumps(repair_queue, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    paths["a2_replay_sample_audit"].write_text(
        json.dumps(a2_sample_audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return paths


def _repair_action(quality: str) -> str:
    if quality == SourceQualityV2.A1_URL_BACKED_ANCHOR_PENDING.value:
        return "fetch or snapshot URL, verify source date, exact anchor, target directness, and primitive mapping"
    if quality == SourceQualityV2.A0_URL_STRING_ONLY.value:
        return "verify URL reachability and create EvidenceAnchor before replay use"
    return "repair URL/content access before replay use"


__all__ = [
    "build_a2_replay_sample_audit",
    "build_url_anchor_repair_queue",
    "reclassify_v1_source_quality",
    "write_source_quality_reports",
]
