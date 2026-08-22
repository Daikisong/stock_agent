"""Publish a FINAL deterministic result without investment directives."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
from typing import Any, Mapping

from .ids import canonical_hash, canonical_json, stable_id
from .job_store import ProFirstJobStore
from .models import JobStatus, ProResearchJob


_DIRECTIVE_PATTERN = re.compile(
    r"(?:매수|매도|비중\s*(?:확대|축소)|\b(?:buy|sell|overweight|underweight)\b)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ProPublishedResult:
    job: ProResearchJob
    result: Mapping[str, Any]
    publication_receipt: Mapping[str, Any]
    publication_root: Path


class ProResultPublisher:
    """Bind the dashboard result to durable scorer and StageCourt receipts."""

    def __init__(self, store: ProFirstJobStore) -> None:
        self.store = store

    def publish(
        self,
        job_id: str,
        *,
        job_root: str | Path,
    ) -> ProPublishedResult:
        root = Path(job_root).resolve()
        publication_root = root / "publication"
        result_path = publication_root / "result.json"
        receipt_path = publication_root / "publication_receipt.json"
        job = self.store.get_job(job_id)
        existing = self.store.get_publication(job_id)
        if existing is not None:
            if not result_path.is_file() or not receipt_path.is_file():
                raise ValueError("published database row lacks local result artifacts")
            durable_file = _read_json(receipt_path)
            result_file = _read_json(result_path)
            if (
                canonical_json(durable_file) != canonical_json(existing)
                or canonical_json(result_file)
                != canonical_json(existing.get("result") or {})
            ):
                raise ValueError("published files differ from the durable ledger")
            return ProPublishedResult(
                job=job,
                result=result_file,
                publication_receipt=durable_file,
                publication_root=publication_root,
            )
        if job.status != JobStatus.FINAL.value:
            raise ValueError("result publication requires FINAL job status")
        score_receipt = self.store.get_score_receipt(job_id)
        stage_receipt = self.store.get_stagecourt_receipt(job_id)
        verification_receipt = self.store.get_source_verification_receipt(job_id)
        if score_receipt is None or stage_receipt is None or verification_receipt is None:
            raise ValueError(
                "publication requires source verification, score, and StageCourt receipts"
            )
        if (
            job.score_receipt_id != score_receipt.get("score_receipt_id")
            or job.stagecourt_receipt_id
            != stage_receipt.get("stagecourt_receipt_id")
            or stage_receipt.get("score_receipt_id") != job.score_receipt_id
        ):
            raise ValueError("FINAL result receipt lineage is inconsistent")
        score = score_receipt.get("score") or {}
        stage = stage_receipt.get("decision") or {}
        component_vector = score.get("component_score_vector") or {}
        if not isinstance(component_vector, Mapping) or len(component_vector) != 7:
            raise ValueError("publication requires the canonical seven-component vector")
        component_rows = _read_jsonl(root / "scoring/component_memos.jsonl")
        judge_rows = _read_jsonl(root / "scoring/judge_decisions.jsonl")
        if len(component_rows) != 7 or len(judge_rows) != 21:
            raise ValueError("publication requires 7 component memos and 21 Judges")
        component_ids = {str(row.get("component_id") or "") for row in component_rows}
        judge_roster = {
            (str(row.get("component_id") or ""), str(row.get("role") or ""))
            for row in judge_rows
        }
        expected_judge_roster = {
            (component_id, role)
            for component_id in component_ids
            for role in ("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")
        }
        assessment_ids = {
            str(row.get("assessment_id") or "")
            for row in score_receipt.get("component_assessments") or ()
        }
        if (
            component_ids != set(component_vector)
            or judge_roster != expected_judge_roster
            or len(assessment_ids) != 7
            or set(stage.get("component_assessment_ids") or ()) != assessment_ids
            or score_receipt.get("judge_decision_count") != 21
            or stage.get("full_e2r_score") != score.get("full_e2r_score")
            or (stage.get("full_score_valid") is True)
            != (score.get("full_score_valid") is True)
        ):
            raise ValueError("publication component/Judge/score/Stage lineage is inconsistent")
        gap_decisions = self.store.get_gap_decisions(job_id)
        candidate = self.store.get_candidate(job.candidate_id)
        source_rows = _read_optional_jsonl(
            root / "verification/source_verifications.jsonl"
        )
        accepted_source_ids = {
            str(row.get("source_id") or "")
            for row in source_rows
            if str(row.get("status") or "").startswith("ACCEPTED_")
            and str(row.get("source_id") or "")
        }
        candidate_count = int(verification_receipt.get("candidate_fact_count") or 0)
        accepted_count = int(
            verification_receipt.get("accepted_fact_candidate_count") or 0
        )
        monitoring_conditions = _monitoring_conditions(
            gap_decisions=gap_decisions,
            stage=stage,
        )
        stage_cap_reasons = tuple(
            dict.fromkeys(
                str((row.get("materiality") or {}).get("stage_cap_reason") or "")
                for row in gap_decisions
                if str((row.get("materiality") or {}).get("stage_cap_reason") or "")
            )
        )
        selection = candidate.selection_receipt
        result = _canonical_mapping(
            {
                "schema_version": "e2r_pro_published_result_v1",
                "job_id": job_id,
                "symbol": job.symbol,
                "company": job.company_name,
                "as_of_date": job.as_of_date,
                "research_mode": job.mode,
                "trigger_summary": {
                    "trigger_ids": list(selection.get("trigger_ids") or ()),
                    "reason_codes": list(selection.get("reason_codes") or ()),
                },
                "candidate_archetypes": list(job.archetype_ids),
                "selected_archetype": score_receipt.get("selected_archetype_id"),
                "verified_source_count": (
                    len(accepted_source_ids)
                    if accepted_source_ids
                    else int(verification_receipt.get("source_document_count") or 0)
                ),
                "accepted_fact_count": accepted_count,
                "rejected_fact_count": max(0, candidate_count - accepted_count),
                "compiled_evidence_fact_count": int(
                    verification_receipt.get("compiled_evidence_fact_count") or 0
                ),
                "unresolved_gap_count": len(gap_decisions),
                "component_coverage": "7/7",
                "judge_coverage": "21/21",
                "component_vector": dict(component_vector),
                "score_interval": {
                    "lower": score.get("provisional_score_lower"),
                    "upper": score.get("provisional_score_upper"),
                },
                "full_score": score.get("full_e2r_score"),
                "score_valid": score.get("full_score_valid") is True,
                "score_type": score.get("score_type"),
                "canonical_stage": stage.get("canonical_stage"),
                "stage_status": stage.get("decision_status"),
                "stage_signal": stage.get("stage_signal"),
                "stage_cap_reasons": list(stage_cap_reasons),
                "risk_overlay": dict(stage.get("risk_overlay") or {}),
                "monitoring_conditions": list(monitoring_conditions),
                "score_receipt_id": job.score_receipt_id,
                "stagecourt_receipt_id": job.stagecourt_receipt_id,
                "score_authority": "ResearchCalibratedComponentScorer",
                "stage_authority": "AtomicStageCourtV2",
                "pro_score_ignored": True,
                "pro_stage_ignored": True,
                "investment_recommendation": False,
            }
        )
        _assert_no_investment_directive(result)
        result_hash = canonical_hash(result)
        publication_id = stable_id(
            "PROPUBLICATION",
            {"job_id": job_id, "result_hash": result_hash},
        )
        receipt_base = {
            "schema_version": "e2r_pro_result_publication_receipt_v1",
            "status": "PUBLISHED",
            "job_id": job_id,
            "result_hash": result_hash,
            "result": result,
            "score_receipt_id": job.score_receipt_id,
            "stagecourt_receipt_id": job.stagecourt_receipt_id,
            "score_authority": "ResearchCalibratedComponentScorer",
            "stage_authority": "AtomicStageCourtV2",
            "investment_recommendation_count": 0,
        }
        publication_hash = canonical_hash(receipt_base)
        receipt = _canonical_mapping(
            {
                **receipt_base,
                "publication_id": publication_id,
                "publication_hash": publication_hash,
            }
        )
        _write_or_verify_json(result_path, result)
        _write_or_verify_json(receipt_path, receipt)
        published_job = self.store.record_publication(
            job_id,
            expected_version=job.state_version,
            publication_id=publication_id,
            publication_hash=publication_hash,
            receipt=receipt,
        )
        return ProPublishedResult(
            job=published_job,
            result=result,
            publication_receipt=receipt,
            publication_root=publication_root,
        )


def _monitoring_conditions(
    *,
    gap_decisions: tuple[Mapping[str, Any], ...],
    stage: Mapping[str, Any],
) -> tuple[str, ...]:
    conditions = []
    for row in gap_decisions:
        label = str(row.get("planner_label") or "UNCLASSIFIED_GAP")
        components = tuple(
            str(value)
            for value in ((row.get("assessment") or {}).get("affected_component_ids"))
            or ()
        )
        conditions.append(f"{label}:{','.join(components) or 'UNSCOPED'}")
    hard_breaks = tuple(
        str(value)
        for value in (stage.get("risk_overlay") or {}).get("hard_break_claim_ids")
        or ()
    )
    if hard_breaks:
        conditions.append("OPEN_HARD_BREAK_REVIEW:" + ",".join(hard_breaks))
    if stage.get("decision_status") != "FINAL":
        conditions.append("STAGE_STATUS:" + str(stage.get("decision_status") or "PENDING"))
    return tuple(dict.fromkeys(conditions))


def _assert_no_investment_directive(payload: Mapping[str, Any]) -> None:
    rendered = canonical_json(payload)
    if _DIRECTIVE_PATTERN.search(rendered):
        raise ValueError("published result contains a prohibited investment directive")


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return payload


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    rows = _read_optional_jsonl(path)
    if not path.is_file():
        raise ValueError(f"required JSONL artifact is missing: {path}")
    return rows


def _read_optional_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    rows = tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )
    if not all(isinstance(row, Mapping) for row in rows):
        raise ValueError(f"expected JSONL objects: {path}")
    return rows


def _canonical_mapping(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    normalized = json.loads(canonical_json(payload))
    if not isinstance(normalized, Mapping):
        raise ValueError("canonical result must be a JSON object")
    return normalized


def _write_or_verify_json(path: Path, payload: Mapping[str, Any]) -> None:
    if path.is_file():
        if canonical_json(_read_json(path)) != canonical_json(payload):
            raise ValueError(f"published artifact changed: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".part")
    with part.open("w", encoding="utf-8") as stream:
        stream.write(canonical_json(payload) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    descriptor = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


__all__ = ["ProPublishedResult", "ProResultPublisher"]
