"""Irreversible diagnostic-run freeze with a runtime-only audit receipt."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Mapping

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json
from ..job_store import ProFirstJobStore
from ..multi_pass import ProMultiPassLedger


_DISPOSITIONS = (
    "OLD_V2_REPAIR_HEAVY_DIAGNOSTIC_RUN",
    "SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION",
    "NOT_OPERATIONAL_EFFICIENCY_PROOF",
)


class OldRunFreezeService:
    def __init__(self, store: ProFirstJobStore) -> None:
        self.store = store
        self.ledger = ProMultiPassLedger(store)

    def freeze(
        self,
        *,
        job_id: str,
        run_id: str,
        job_root: str | Path,
        actor: str = "v2.1-fresh-session-transition",
    ) -> Mapping[str, Any]:
        root = Path(job_root)
        if not run_id.strip():
            raise ValueError("run_id is required")
        before = self.store.get_job(job_id)
        passes_before = self.ledger.list_passes(job_id)
        frozen = self.store.freeze_old_diagnostic_job(
            job_id,
            expected_version=before.state_version,
            actor=actor,
            idempotency_key=f"old-run-freeze:{job_id}",
        )
        submitted_followups = tuple(
            row
            for row in passes_before
            if row.pass_name != "INITIAL_FULL_RESEARCH" and row.submit_count == 1
        )
        latest_submitted = submitted_followups[-1] if submitted_followups else None
        latest_snapshot = self.ledger.latest_dossier_snapshot(job_id)
        repair_receipt = _read_optional_json(
            root / "repair/verifier_repair_receipt.json"
        )
        payload: dict[str, Any] = {
            "schema_version": "e2r_pro_old_run_freeze_receipt_v1",
            "job_id": frozen.job_id,
            "run_id": run_id,
            "target_id": frozen.symbol,
            "as_of_date": frozen.as_of_date,
            "archetype_ids": list(frozen.archetype_ids),
            "conversation_id": frozen.conversation_id,
            "old_job_frozen_at": frozen.old_job_frozen_at,
            "superseded_by_fresh_job_id": frozen.superseded_by_fresh_job_id,
            "dispositions": list(_DISPOSITIONS),
            "initial_submit_count_at_freeze": frozen.submit_count,
            "followup_submit_count_at_freeze": len(submitted_followups),
            "new_submit_count_after_freeze": 0,
            "last_in_flight_pass": (
                None
                if latest_submitted is None
                else {
                    "pass_id": latest_submitted.pass_id,
                    "pass_name": latest_submitted.pass_name,
                    "status": latest_submitted.status,
                    "submit_count": latest_submitted.submit_count,
                    "response_hash": latest_submitted.response_hash,
                    "snapshot_id": (
                        latest_snapshot.snapshot_id
                        if latest_snapshot is not None
                        and latest_snapshot.pass_id == latest_submitted.pass_id
                        else None
                    ),
                }
            ),
            "latest_effective_snapshot": (
                None
                if latest_snapshot is None
                else {
                    "snapshot_id": latest_snapshot.snapshot_id,
                    "pass_id": latest_snapshot.pass_id,
                    "dossier_hash": latest_snapshot.dossier_hash,
                    "fact_count": latest_snapshot.fact_count,
                    "question_count": latest_snapshot.question_count,
                    "route_receipt_count": latest_snapshot.route_receipt_count,
                }
            ),
            "latest_repair_receipt_hash": repair_receipt.get("receipt_hash"),
            "latest_unresolved_repair_packet_count": len(
                tuple(repair_receipt.get("unresolved_packet_ids") or ())
            ),
            "runtime_preserved": True,
            "old_facts_allowed_in_fresh_packet": False,
            "old_routes_allowed_as_fresh_answers": False,
            "old_score_stage_allowed_in_fresh_packet": False,
            "score_authority": False,
            "stage_authority": False,
            "publication_withheld": True,
        }
        payload["receipt_hash"] = canonical_hash(payload)
        path = root / "fresh_session/old_run_freeze_receipt.json"
        _write_json_once(path, payload)
        return payload


def _read_optional_json(path: Path) -> Mapping[str, Any]:
    if not path.is_file():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"runtime receipt must be a JSON object: {path}")
    return payload


def _write_json_once(path: Path, payload: Mapping[str, Any]) -> None:
    if path.is_file():
        existing = json.loads(path.read_text(encoding="utf-8"))
        if existing != payload:
            raise RuntimeError("old-run freeze receipt is immutable and already differs")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    data = canonical_json(payload) + "\n"
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        fsync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


__all__ = ["OldRunFreezeService"]
