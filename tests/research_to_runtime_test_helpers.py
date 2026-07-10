from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

from e2r.census.research_to_runtime_parity import build_research_to_runtime_parity_audit


_REPO_ROOT = Path(__file__).resolve().parents[1]
_TEMP_DIR: tempfile.TemporaryDirectory[str] | None = None
_PARITY_AUDIT: dict[str, Any] | None = None


def runtime_fixture_output_root() -> Path:
    global _TEMP_DIR
    if _TEMP_DIR is None:
        _TEMP_DIR = tempfile.TemporaryDirectory()
        output_root = Path(_TEMP_DIR.name) / "runtime"
        output_root.mkdir(parents=True)
        _write_jsonl(output_root / "planner_runs.jsonl", _planner_rows())
        _write_jsonl(output_root / "source_task_executions.jsonl", _source_task_execution_rows())
        _write_jsonl(output_root / "raw_assertion_rejections.jsonl", _source_lineage_rejection_rows())
        _write_jsonl(output_root / "brain_claim_mapping_trace.jsonl", _claim_mapping_trace_rows())
        shutil.copyfile(
            _REPO_ROOT / "docs/operational/census_mode_v4_full_thesis_seed_materialization_trace.jsonl",
            output_root / "full_thesis_seed_materialization_trace.jsonl",
        )
        _write_mandatory_replay_files(output_root)
    return Path(_TEMP_DIR.name) / "runtime"


def research_to_runtime_fixture_audit() -> dict[str, Any]:
    global _PARITY_AUDIT
    if _PARITY_AUDIT is None:
        _PARITY_AUDIT = build_research_to_runtime_parity_audit(
            repo_root=_REPO_ROOT,
            output_root=runtime_fixture_output_root(),
            docs_dir=_REPO_ROOT / "docs/operational",
            as_of_date="2026-07-05",
        )
    return _PARITY_AUDIT


def _planner_rows() -> list[dict[str, Any]]:
    contracts = json.loads(
        (_REPO_ROOT / "configs/e2r_agentic_evidence_contracts_v2.json").read_text(encoding="utf-8")
    )["contracts"]
    rows: list[dict[str, Any]] = []
    for contract_index, contract in enumerate(contracts):
        archetype_id = str(contract["archetype_id"])
        prefix = archetype_id.split("_", 1)[0]
        for repetition in range(3):
            symbol = "005930" if prefix == "C06" else f"{200000 + contract_index:06d}"
            event_id = f"CE-RUNTIME-FIXTURE-{prefix}-{repetition}"
            rows.append(
                {
                    "planner_run_id": f"PLANNER-RUNTIME-FIXTURE-{prefix}-{repetition}",
                    "real_provider_success": True,
                    "planner_output_score_stage_key_count": 0,
                    "event": {"candidate_event_id": event_id, "symbol": symbol},
                    "output": {"top_k_archetype_hypotheses": [{"archetype_id": archetype_id}]},
                }
            )
    return rows


def _source_task_execution_rows() -> list[dict[str, Any]]:
    specs = (
        ("C06_HBM_MEMORY_CUSTOMER_CAPACITY", "005930", "medium_term_revision_visibility", True),
        ("C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "058470", "named_customer_quality", False),
        ("C15_MATERIAL_SPREAD_SUPERCYCLE", "010950", "spread_expansion", True),
        ("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "011170", "spread_expansion", True),
        ("C24_BIO_TRIAL_DATA_EVENT_RISK", "009420", "trial_endpoint_quality", True),
        ("C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "053800", "renewal_retention", False),
        ("C29_TRANSFORMER_GRID_BACKLOG_PRICING", "267260", "backlog_pricing", True),
    )
    rows: list[dict[str, Any]] = []
    for archetype_id, symbol, primitive_gap, accepted in specs:
        prefix = archetype_id.split("_", 1)[0]
        accepted_ids = [f"CLAIM-RUNTIME-FIXTURE-{prefix}"] if accepted else []
        direct_ids = list(accepted_ids) if accepted and prefix != "C24" else []
        not_eligible = []
        unsatisfied = []
        status = "EVIDENCE_OS_ACCEPTED" if accepted else "NO_EVIDENCE_FOUND"
        stop_reason = "accepted_claim" if accepted else "no_score_eligible_real_claim"
        if prefix == "C24":
            unsatisfied = [primitive_gap]
            stop_reason = "accepted_baseline_claim_without_task_primitive"
        if prefix == "C28":
            not_eligible = ["primitive_mapping_rejected:adjudication_not_passed"]
        rows.append(
            {
                "task_id": f"SOURCE-TASK-RUNTIME-FIXTURE-{prefix}",
                "candidate_event_id": f"CE-RUNTIME-FIXTURE-{prefix}-0",
                "archetype_id": archetype_id,
                "symbol": symbol,
                "company_name": f"{prefix} fixture company",
                "primitive_gap": primitive_gap,
                "status": status,
                "stop_reason": stop_reason,
                "source_class": "BrokerReportPublicPDF" if prefix in {"C08", "C28"} else "IssuerOfficial",
                "provider_name": "runtime_fixture_provider",
                "accepted_claim_ids": accepted_ids,
                "direct_accepted_claim_ids": direct_ids,
                "rerouted_accepted_claim_ids": [],
                "rejected_claim_ids": [] if accepted else [f"REJECTED-RUNTIME-FIXTURE-{prefix}"],
                "satisfies_source_task": bool(direct_ids),
                "fetched_document_ids": [f"DOC-RUNTIME-FIXTURE-{prefix}"],
                "document_urls": [f"https://example.test/runtime/{prefix}.pdf"],
                "primitive_gap_unsatisfied_ids": unsatisfied,
                "not_eligible_reasons": not_eligible,
                "provider_errors": [],
            }
        )
    return rows


def _source_lineage_rejection_rows() -> list[dict[str, Any]]:
    common = {
        "mapping_status": "ACCEPTED",
        "semantic_status": "PASS",
        "target_scope_status": "DIRECT",
        "temporal_status": "CURRENT",
        "source_provider": "runtime_fixture_provider",
    }
    return [
        {
            **common,
            "archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            "symbol": "053800",
            "source_task_id": "C28-broker-original-1",
            "primitive_gap": "renewal_retention",
            "source_url": "https://bbn.kiwoom.com/rfCR10848",
            "not_eligible_reasons": [
                "source_lineage_unverified_original:BrokerReportPublicPDF:runtime_fixture_provider"
            ],
        },
        {
            **common,
            "archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            "symbol": "053800",
            "source_task_id": "C28-broker-original-2",
            "primitive_gap": "renewal_retention",
            "source_url": "https://securities.miraeasset.com/bbs/board/message/view.do?categoryId=1521&messageId=2332084",
            "not_eligible_reasons": [
                "source_lineage_unverified_original:BrokerReportPublicPDF:runtime_fixture_provider"
            ],
        },
        {
            **common,
            "archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
            "symbol": "058470",
            "source_task_id": "C08-broker-original",
            "primitive_gap": "named_customer_quality",
            "source_url": "https://www.eugenefn.com/common/files/amail/20250609_058470.pdf",
            "not_eligible_reasons": [
                "source_lineage_unverified_original:BrokerReportPublicPDF:runtime_fixture_provider",
                "semantic_rejected",
                "primitive_mapping_rejected:adjudication_not_passed",
            ],
        },
    ]


def _claim_mapping_trace_rows() -> list[dict[str, Any]]:
    return [
        {
            "archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            "claim_id": "CLAIM-MAPPING-RUNTIME-FIXTURE-C28",
            "source_task_id": "SOURCE-TASK-RUNTIME-FIXTURE-C28",
            "symbol": "053800",
            "primitive_gap": "renewal_retention",
            "trace_status": "REJECTED",
            "accepted": False,
            "mapping_status": "REJECTED",
            "semantic_status": "REJECTED",
            "target_scope_status": "DIRECT",
            "temporal_status": "CURRENT",
            "source_provider": "runtime_fixture_provider",
            "source_url": "https://bbn.kiwoom.com/rfTP/1022/20250618_053800.pdf",
            "eligibility_reasons": ["primitive_mapping_rejected:adjudication_not_passed"],
        }
    ]


def _write_mandatory_replay_files(output_root: Path) -> None:
    specs = (
        ("c06_source_backed_semantic_replay.json", True),
        ("c06_guard_replay_audit.json", True),
        ("c08_source_backed_semantic_replay.json", False),
        ("c15_source_backed_semantic_replay.json", False),
        ("c17_source_backed_semantic_replay.json", False),
        ("c24_source_backed_semantic_replay.json", False),
        ("c28_source_backed_semantic_replay.json", False),
    )
    for filename, c06_guard in specs:
        prefix = filename[:3].upper()
        payload = {
            "positive_replay_pass": True,
            "accepted_claim_count": 1,
            "positive_accepted_claim_ids": [f"REPLAY-CLAIM-RUNTIME-FIXTURE-{prefix}"],
            "positive_accepted_primitive_ids": [f"primitive-{prefix.lower()}"],
            "guard_replay_pass": True,
            "guard_cases_pass": True,
            "guard_accepted_claim_ids": [f"REPLAY-GUARD-RUNTIME-FIXTURE-{prefix}"],
            "production_score_evidence_allowed": False,
        }
        if c06_guard:
            payload["accepted_claim_ids"] = ["REPLAY-GUARD-RUNTIME-FIXTURE-C06"]
        (output_root / filename).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )
