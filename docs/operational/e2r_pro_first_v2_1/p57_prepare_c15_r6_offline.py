"""Prepare, but never submit, the already authorized C15 successor.

Run with Windows Python so existing runtime path identities remain unchanged.
This operational helper uses the repository's durable boundary and packet APIs.
"""

from dataclasses import asdict, fields
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

REPO = Path(r"\\wsl.localhost\Ubuntu-22.04\home\eorb915\projects\stock_agent\.worktrees\e2r-pro-first-browser-platform-20260822")
sys.path.insert(0, str(REPO / "src"))

from e2r.pro_first.canary.live_v2 import LiveCanaryPending
from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.fresh_session.boundary import (
    FreshSessionBoundaryService, OldAnswerLeakageManifest, write_runtime_json_once,
)
from e2r.pro_first.fresh_session.full_thesis_live_v3 import _require_operational_dispatch_history
from e2r.pro_first.fresh_session.live_canary_v3 import (
    build_old_answer_leakage_manifest, _persist_runtime_manifest,
)
from e2r.pro_first.fresh_session.orchestrator_v3 import FreshSessionOrchestratorV3
from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.multi_pass import ProMultiPassLedger

BASE = Path(r"C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime")
OLD_ROOT = BASE / "fresh_v2_1/20260901T124218Z"
FRESH_ROOT = BASE / "fresh_v2_1/20260907T212025Z"
OLD_JOB = "PROJOB-7c02db014fefb06b1258ffe9"
OLD_RUN = "PRORUN-b66fab297a8016c613f2d46a"
OLD_CONVERSATION = "6a96c840-4440-83ee-abe8-c8742eb17741"
SESSION = "FRESH-V2-1-C15-R6-20260907T212025Z"
SOURCE_SHA = "792bb27fd1c47f43231f266fc8c1322f93ae4cce"


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    receipt_path = FRESH_ROOT / "offline_successor_preparation_receipt.json"
    if receipt_path.exists():
        payload = json.loads(receipt_path.read_text(encoding="utf-8"))
        unsigned = {k: v for k, v in payload.items() if k != "receipt_hash"}
        assert canonical_hash(unsigned) == payload["receipt_hash"]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    store = ProFirstJobStore(BASE / "live_v2/20260823T145430Z/pro_first.sqlite3")
    ledger = ProMultiPassLedger(store)
    old = store.get_job(OLD_JOB)
    assert (old.symbol, old.as_of_date, old.conversation_id) == (
        "010950", "2026-08-23", OLD_CONVERSATION,
    )
    existing_boundary_path = FRESH_ROOT / "fresh_session_boundary_receipt.json"
    if old.superseded_by_fresh_job_id is not None:
        existing_boundary = json.loads(existing_boundary_path.read_text(encoding="utf-8"))
        assert existing_boundary["fresh_job_id"] == old.superseded_by_fresh_job_id
        assert existing_boundary["fresh_session_id"] == SESSION
    before_passes = canonical_hash([asdict(row) for row in ledger.list_passes(OLD_JOB)])
    old_job_root = OLD_ROOT / "jobs" / OLD_JOB
    before_files = {
        str(p.relative_to(old_job_root)): file_hash(p)
        for p in old_job_root.rglob("*") if p.is_file()
        and p != old_job_root / "fresh_session/fresh_efficiency_failure_receipt.json"
    }
    try:
        _require_operational_dispatch_history(ledger, job_id=OLD_JOB)
    except LiveCanaryPending as error:
        assert error.status == "OPERATIONAL_EFFICIENCY_GATE_FAILED"
        failure_reason = error.reason
    else:
        raise RuntimeError("R5 history unexpectedly passed; refuse diagnostic seal")

    prior_manifest_payload = json.loads(
        (OLD_ROOT / "old_answer_leakage_manifest.runtime.json").read_text(encoding="utf-8")
    )
    assert canonical_hash({k: v for k, v in prior_manifest_payload.items() if k != "manifest_hash"}) == prior_manifest_payload["manifest_hash"]
    prior_manifest = OldAnswerLeakageManifest(**{
        field.name: prior_manifest_payload[field.name]
        for field in fields(OldAnswerLeakageManifest)
    })
    boundaries = FreshSessionBoundaryService(store)
    old_boundary, _ = boundaries.load_existing(
        fresh_runtime_root=OLD_ROOT, leakage_manifest=prior_manifest,
        allow_frozen_submitted_recovery=True,
    )
    frozen = FreshSessionOrchestratorV3(store, old_boundary).seal_failed_run_for_new_conversation(
        reason=failure_reason,
    )
    assert frozen.old_job_frozen_at is not None

    deny_manifest = build_old_answer_leakage_manifest(
        store, old_job_id=OLD_JOB, old_run_id=OLD_RUN,
        old_conversation_id=OLD_CONVERSATION, old_job_root=old_job_root,
    )
    if existing_boundary_path.exists():
        boundary, fresh = boundaries.load_existing(
            fresh_runtime_root=FRESH_ROOT, leakage_manifest=deny_manifest,
        )
    else:
        boundary, fresh = boundaries.start(
            old_job_id=OLD_JOB, old_run_id=OLD_RUN,
            old_conversation_id=OLD_CONVERSATION,
            fresh_session_id=SESSION, old_runtime_root=OLD_ROOT,
            fresh_runtime_root=FRESH_ROOT, archetype_ids=old.archetype_ids,
            leakage_manifest=deny_manifest,
        )
    _persist_runtime_manifest(FRESH_ROOT, deny_manifest)
    config = load_pro_first_local_config(REPO / "configs/e2r_pro_first_local.yaml")
    built = FreshSessionOrchestratorV3(store, boundary).build_initial_packet(
        commit_sha=SOURCE_SHA, config_hash=config.config_hash,
    )
    fresh = store.get_job(fresh.job_id)
    assert fresh.status == "PACKET_READY"
    assert fresh.submit_count == 0 and fresh.conversation_id is None
    assert fresh.browser_session_id is None
    assert built.packet_leakage_audit.leakage_count == 0
    prompt_leakage_count = (
        built.prompt_leakage_receipt["old_answer_token_count"]
        + built.prompt_leakage_receipt["forbidden_answer_field_token_count"]
    )
    assert prompt_leakage_count == 0
    assert before_passes == canonical_hash([asdict(row) for row in ledger.list_passes(OLD_JOB)])
    assert all(file_hash(old_job_root / p) == digest for p, digest in before_files.items())
    assert store.get_job(OLD_JOB).superseded_by_fresh_job_id == fresh.job_id
    assert fresh.job_id != OLD_JOB and built.packet_payload["run_id"] != OLD_RUN

    unsigned = {
        "schema_version": "e2r_pro_first_v2_1_offline_successor_preparation_v1",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "status": "PACKET_READY_NOT_BROWSER_PREPARED_NOT_SUBMITTED",
        "source_sha": SOURCE_SHA,
        "old_job_id": OLD_JOB,
        "old_job_frozen_at": frozen.old_job_frozen_at,
        "old_history_gate": "OPERATIONAL_EFFICIENCY_GATE_FAILED",
        "old_pass_rows_hash_before_and_after": before_passes,
        "old_pass_rows_unchanged": True,
        "old_artifact_file_count": len(before_files),
        "old_artifact_manifest_hash": canonical_hash(before_files),
        "old_artifacts_preserved": True,
        "fresh_session_id": SESSION,
        "fresh_runtime_root": str(FRESH_ROOT),
        "job_id": fresh.job_id,
        "run_id": built.packet_payload["run_id"],
        "initial_pass_id": built.initial_pass_id,
        "symbol": fresh.symbol,
        "as_of_date": fresh.as_of_date,
        "archetype_ids": list(fresh.archetype_ids),
        "packet_path": str(built.packet_bundle.research_packet_json),
        "packet_hash": built.packet_bundle.packet_hash,
        "prompt_hash": built.prompt.prompt_hash,
        "prompt_char_count": len(built.prompt.prompt_text),
        "packet_old_answer_leakage_count": built.packet_leakage_audit.leakage_count,
        "prompt_old_answer_leakage_count": prompt_leakage_count,
        "new_browser_window_count": 0,
        "new_browser_tab_count": 0,
        "browser_prepared": False,
        "browser_session_id": None,
        "conversation_id": None,
        "submit_count": fresh.submit_count,
        "source_query_count": 0,
        "source_fetch_count": 0,
        "score_authority": False,
        "stage_authority": False,
        "publication_withheld": True,
        "operational_live_pass": False,
    }
    receipt = {**unsigned, "receipt_hash": canonical_hash(unsigned)}
    write_runtime_json_once(receipt_path, receipt)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
