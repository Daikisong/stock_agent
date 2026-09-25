"""Same-input no-op and bounded delta reuse contracts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER

from .ids import canonical_hash
from .job_store import ProFirstJobStore
from .models import JobStatus


@dataclass(frozen=True)
class DeltaScoringReuseContext:
    prior_job_id: str
    prior_job_root: Path
    components_to_revisit: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.prior_job_id.strip():
            raise ValueError("delta reuse requires a prior job id")
        components = tuple(
            dict.fromkeys(str(value) for value in self.components_to_revisit)
        )
        if not components:
            raise ValueError("no-delta input must stop before a DELTA_RESEARCH job")
        if not set(components).issubset(CANONICAL_COMPONENT_ORDER):
            raise ValueError("delta revisit roster contains an unknown component")
        object.__setattr__(self, "components_to_revisit", components)
        object.__setattr__(
            self,
            "prior_job_root",
            Path(self.prior_job_root).resolve(),
        )


@dataclass(frozen=True)
class SameInputNoopResult:
    prior_job_id: str
    result: Mapping[str, Any]
    receipt: Mapping[str, Any]


class ProSameInputReuseGate:
    """Return the prior publication before creating or submitting a new job."""

    def __init__(self, store: ProFirstJobStore) -> None:
        self.store = store

    def evaluate(
        self,
        *,
        prior_job_id: str,
        current_trigger_fingerprint: str,
        prior_source_delta_hash: str | None,
        current_source_delta_hash: str | None,
        expected_dossier_hash: str | None = None,
    ) -> SameInputNoopResult | None:
        prior = self.store.get_job(prior_job_id)
        same_trigger = (
            bool(current_trigger_fingerprint)
            and prior.trigger_fingerprint == current_trigger_fingerprint
        )
        same_source_delta = bool(
            prior_source_delta_hash
            and current_source_delta_hash
            and prior_source_delta_hash == current_source_delta_hash
        )
        if not (same_trigger or same_source_delta):
            return None
        if prior.status != JobStatus.FINAL.value or not prior.published_at:
            raise ValueError("same-input reuse requires a published FINAL prior job")
        publication = self.store.get_publication(prior_job_id)
        import_receipt = self.store.get_dossier_import_receipt(prior_job_id)
        score_receipt = self.store.get_score_receipt(prior_job_id)
        stage_receipt = self.store.get_stagecourt_receipt(prior_job_id)
        if not all((publication, import_receipt, score_receipt, stage_receipt)):
            raise ValueError("same-input prior job lacks canonical durable receipts")
        dossier_hash = str(import_receipt.get("normalized_dossier_hash") or "")
        if expected_dossier_hash is not None and expected_dossier_hash != dossier_hash:
            return None
        result = dict(publication.get("result") or {})
        receipt = {
            "schema_version": "e2r_pro_same_input_noop_receipt_v1",
            "status": "SAME_DOSSIER_NOOP",
            "prior_job_id": prior_job_id,
            "dossier_hash": dossier_hash,
            "same_trigger_fingerprint": same_trigger,
            "same_source_delta_hash": same_source_delta,
            "browser_submit_count": 0,
            "new_pro_research_count": 0,
            "supplemental_query_count": 0,
            "supplemental_fetch_count": 0,
            "source_fetch_count": 0,
            "recomputed_component_count": 0,
            "recomputed_judge_count": 0,
            "score_variance": 0.0,
            "stage_variance": 0,
            "reused_score_receipt_id": score_receipt.get("score_receipt_id"),
            "reused_stagecourt_receipt_id": stage_receipt.get(
                "stagecourt_receipt_id"
            ),
            "reused_publication_id": publication.get("publication_id"),
            "no_new_job_created": True,
            "receipt_hash": "",
        }
        receipt["receipt_hash"] = canonical_hash(
            {key: value for key, value in receipt.items() if key != "receipt_hash"}
        )
        return SameInputNoopResult(
            prior_job_id=prior_job_id,
            result=result,
            receipt=receipt,
        )


__all__ = [
    "DeltaScoringReuseContext",
    "ProSameInputReuseGate",
    "SameInputNoopResult",
]
