import json
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.census.census_runner_v4 import (
    CensusV4RunConfig,
    _apply_production_full_thesis_from_brain,
    _brain_stage_promotion_audit,
    _claim_to_stage_forensic_audit,
    _export_brain_web_bundle_leafs,
    _full_thesis_production_audit,
    _primitive_state_chain_audit,
    _promote_brain_stage_rows,
    _source_connector_capability_audit,
    _sync_brain_trace_promotion_markers,
    run_census_mode_v4,
)
from e2r.production.metadata import write_jsonl
from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
from e2r.research_brain.v4_schemas import DailyWatchlistItemV4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from tests.census_v4_test_helpers import census_v4_artifacts, read_json
from tests.research_brain_v4_test_helpers import c06_source_task, sample_v4_event


class CensusV4BrainStagePromotionGateTests(unittest.TestCase):
    def test_canonical_disabled_run_records_no_brain_stage_promotion(self):
        artifacts = census_v4_artifacts()
        audit = read_json(artifacts["output_root"] / "brain_stage_promotion_audit.json")

        self.assertEqual(audit["verdict"], "NOT_REQUESTED")
        self.assertEqual(audit["brain_stage_trace_count"], 0)
        self.assertEqual(audit["brain_promoted_stage_row_count"], 0)
        self.assertEqual(audit["unsafe_promoted_stage_row_count"], 0)
        self.assertEqual(audit["brain_stage_promotion_mode"], "disabled")

    def test_brain_snapshot_stage_trace_is_exported_but_not_promoted(self):
        event = sample_v4_event()
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot"),
        )
        self.assertTrue(bundle.executions[0].accepted_claim_ids)

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            watchlist_item = DailyWatchlistItemV4(
                symbol=event.symbol,
                company_name=event.company_name,
                candidate_event_id=event.candidate_event_id,
                event_type=event.event_type,
                event_summary=event.event_summary,
                event_source=event.source_id,
                primary_archetype="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                accepted_claim_ids=tuple(bundle.executions[0].accepted_claim_ids),
            )
            counts = _export_brain_web_bundle_leafs(
                result={
                    "config": {"as_of_date": "2026-06-29"},
                    "bundles": {event.candidate_event_id: bundle},
                    "planner_runs": (),
                    "watchlist_items": (watchlist_item,),
                },
                output_root=root,
            )
            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-06-29",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="frozen_real_source_snapshot",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": counts["accepted_claim_exported_count"],
                },
                stage_rows=[],
            )
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            accepted = _read_jsonl(root / "accepted_claims.jsonl")

        self.assertGreater(counts["stagecourt_trace_exported_count"], 0)
        self.assertTrue(accepted)
        self.assertTrue(all(row["score_eligible"] is False for row in accepted))
        self.assertTrue(all("snapshot_source_not_score_eligible" in row["eligibility_reasons"] for row in accepted))
        self.assertGreater(audit["brain_stage_trace_count"], 0)
        self.assertEqual(audit["brain_promoted_stage_row_count"], 0)
        self.assertEqual(audit["unsafe_promoted_stage_row_count"], 0)
        self.assertEqual(audit["verdict"], "BLOCKED")
        self.assertIn("source acquisition is not production-live: frozen_real_source_snapshot", audit["blockers"])
        self.assertTrue(all(row["census_stage_status_id"] is None for row in traces))
        self.assertTrue(all(row["trace_status"].endswith("STAGE_NOT_PROMOTED") for row in traces))

    def test_promoted_brain_row_with_blockers_is_unsafe(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="none",
                    brain_stage_promotion_mode="disabled",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 0, "source_task_execution_count": 0, "accepted_claim_count": 0},
                stage_rows=[{"symbol": "005930", "stagecourt_trace_id": "SCT-BRAIN-unsafe", "stage_source": "research_brain_v4_attempt"}],
            )

        self.assertEqual(audit["verdict"], "FAIL_UNSAFE_PROMOTION")
        self.assertEqual(audit["brain_promoted_stage_row_count"], 1)
        self.assertEqual(audit["unsafe_promoted_stage_row_count"], 1)

    def test_strict_live_connected_promoted_brain_row_is_promotion_applied(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(root / "planner_runs.jsonl", [{"provider_mode": "real", "real_provider_success": True}])
            write_jsonl(
                root / "source_task_executions.jsonl",
                [
                    {
                        "task_id": "TASK-A",
                        "source_origin": "research_brain_v4_attempt",
                        "fetched_document_ids": ["DOC-A"],
                    }
                ],
            )
            write_jsonl(root / "evidence_documents.jsonl", [{"document_id": "DOC-A", "source_origin": "research_brain_v4_attempt", "canonical_url": "https://example.com/doc"}])
            write_jsonl(root / "evidence_anchors.jsonl", [{"anchor_id": "ANCH-A", "document_id": "DOC-A", "source_origin": "research_brain_v4_attempt"}])
            write_jsonl(
                root / "claim_extractor_runs.jsonl",
                [
                    {
                        "provider_mode": "llm",
                        "provider_name": "codex_cli_contract_blind_extractor",
                        "raw_assertion_ids": ["RAWLLM-A"],
                    }
                ],
            )
            write_jsonl(
                root / "accepted_claims.jsonl",
                [
                    {
                        "claim_id": "CLM-A",
                        "brain_web_claim": True,
                        "source_origin": "research_brain_v4_attempt",
                        "document_id": "DOC-A",
                        "anchor_id": "ANCH-A",
                        "event_date": "2026-06-30",
                        "target_scope_status": "DIRECT",
                        "temporal_status": "CURRENT",
                        "score_eligible": True,
                        "raw_assertion_id": "RAWLLM-A",
                    }
                ],
            )
            write_jsonl(root / "score_contributions.jsonl", [{"score_contribution_id": "SCON-A", "source_origin": "research_brain_v4_attempt", "support_claim_ids": ["CLM-A"]}])
            write_jsonl(
                root / "brain_to_claim_trace.jsonl",
                [
                    {
                        "accepted_claim_id": "CLM-A",
                        "score_contribution_id": "SCON-A",
                        "primitive_state_ids": ["PRIM-A"],
                        "stagecourt_trace_id": "SCT-BRAIN-A",
                    }
                ],
            )
            write_jsonl(
                root / "stagecourt_traces.jsonl",
                [
                    {
                        "stagecourt_trace_id": "SCT-BRAIN-A",
                        "source_origin": "research_brain_v4_attempt",
                        "accepted_claim_ids": ["CLM-A"],
                        "score_contribution_ids": ["SCON-A"],
                        "primitive_state_ids": ["PRIM-A"],
                        "not_promoted_to_census_stage_status": True,
                    }
                ],
            )
            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "stagecourt_trace_id": "SCT-BRAIN-A",
                        "accepted_claim_ids": ["CLM-A"],
                        "score_contribution_ids": ["SCON-A"],
                        "primitive_state_ids": ["PRIM-A"],
                    }
                ],
            )

        self.assertEqual(audit["verdict"], "PROMOTION_APPLIED")
        self.assertEqual(audit["brain_promoted_stage_row_count"], 1)
        self.assertEqual(audit["unsafe_promoted_stage_row_count"], 0)
        self.assertEqual(audit["web_or_llm_accepted_claim_count"], 1)
        self.assertEqual(audit["llm_extracted_accepted_claim_count"], 1)
        self.assertEqual(audit["blockers"], [])

    def test_nonrepresentative_score_ineligible_claim_does_not_make_clean_promotion_unsafe(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            accepted.append(
                {
                    "claim_id": "CLM-DIAG",
                    "brain_web_claim": True,
                    "source_origin": "research_brain_v4_attempt",
                    "document_id": "DOC-A",
                    "anchor_id": "ANCH-A",
                    "event_date": "2026-06-30",
                    "target_scope_status": "DIRECT",
                    "temporal_status": "CURRENT",
                    "score_eligible": False,
                    "eligibility_reasons": ["source_task_not_satisfied_rerouted_claim"],
                    "primitive_id": "adjacent_context_only",
                    "mapping_status": "REJECTED",
                    "raw_assertion_id": "RAWLLM-A",
                }
            )
            write_jsonl(root / "accepted_claims.jsonl", accepted)

            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 2},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "stagecourt_trace_id": "SCT-BRAIN-A",
                        "stage_source": "research_brain_v4_attempt",
                        "accepted_claim_ids": ["CLM-A"],
                        "score_contribution_ids": ["SCON-A"],
                        "primitive_state_ids": ["PRIM-A"],
                    }
                ],
            )

        self.assertEqual(audit["verdict"], "PROMOTION_APPLIED")
        self.assertEqual(audit["unsafe_promoted_stage_row_count"], 0)
        self.assertEqual(audit["brain_claim_score_ineligible_count"], 1)
        self.assertEqual(audit["promoted_brain_claim_score_ineligible_count"], 0)
        self.assertEqual(audit["diagnostic_brain_claim_score_ineligible_count"], 1)
        self.assertEqual(audit["blockers"], [])

    def test_score_ineligible_trace_claim_is_not_promoted_as_representative_stage(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            accepted[0]["score_eligible"] = False
            accepted[0]["eligibility_reasons"] = ["source_task_not_satisfied_rerouted_claim"]
            write_jsonl(root / "accepted_claims.jsonl", accepted)

            stage_rows, export = _promote_brain_stage_rows(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "census_stage_status_id": "CSS-BASE",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "stage_source": "event_board",
                    }
                ],
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
            )

        self.assertEqual(export["promoted_stage_row_count"], 0)
        self.assertEqual(export["skipped_unsupported_trace_count"], 1)
        self.assertEqual(stage_rows[0]["stage_scope"], "CENSUS_EVENT_BOARD")
        self.assertEqual(stage_rows[0]["stage_source"], "event_board")

    def test_official_only_brain_claim_promotes_as_official_partial_not_brain_web(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            accepted[0].pop("raw_assertion_id", None)
            accepted[0]["source_provider"] = "OpenDART"
            accepted[0]["source_url"] = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260701999999"
            write_jsonl(root / "accepted_claims.jsonl", accepted)
            write_jsonl(root / "claim_extractor_runs.jsonl", [])

            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
            )
            audit = _brain_stage_promotion_audit(
                config=config,
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=[],
            )
            stage_rows, export = _promote_brain_stage_rows(
                config=config,
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scope": "NO_SCORE",
                    }
                ],
            )

        self.assertEqual(audit["verdict"], "ELIGIBLE_NOT_PROMOTED")
        self.assertEqual(audit["official_accepted_claim_count"], 1)
        self.assertEqual(audit["web_or_llm_accepted_claim_count"], 0)
        self.assertEqual(audit["brain_stage_trace_without_web_or_llm_claim_count"], 1)
        self.assertEqual(audit["brain_stage_trace_with_official_claim_count"], 1)
        self.assertEqual(audit["brain_stage_trace_without_supported_claim_count"], 0)
        self.assertEqual(audit["blockers"], [])
        self.assertEqual(export["promoted_stage_row_count"], 1)
        self.assertEqual(export["promoted_web_llm_stage_row_count"], 0)
        self.assertEqual(export["promoted_official_stage_row_count"], 1)
        self.assertEqual(stage_rows[0]["stage_scope"], "BRAIN_OFFICIAL_PARTIAL")
        self.assertEqual(stage_rows[0]["score_scope"], "BRAIN_OFFICIAL_CLAIM_BACKED_PARTIAL")
        self.assertEqual(stage_rows[0]["brain_partial_evidence_lane"], "official")
        self.assertEqual(stage_rows[0]["operator_stage_use"], "NOT_FULL_THESIS_STAGE")
        self.assertEqual(stage_rows[0]["operator_score_use"], "NOT_FULL_E2R_SCORE")
        self.assertEqual(stage_rows[0]["operator_scope_note"], "brain_official_claim_backed_partial_not_full_thesis")
        self.assertTrue(stage_rows[0]["base_stage_display"].startswith("BRAIN_OFFICIAL_PARTIAL_"))
        self.assertEqual(stage_rows[0]["full_thesis_stage"], "FULL_THESIS_NOT_RUN")
        self.assertEqual(stage_rows[0]["official_source_task_count"], 1)
        self.assertEqual(stage_rows[0]["official_evidence_document_count"], 1)
        self.assertEqual(stage_rows[0]["official_source_task_ids"], ["TASK-A"])
        self.assertEqual(stage_rows[0]["official_evidence_document_ids"], ["DOC-A"])

    def test_unpromoted_snapshot_document_does_not_make_live_promoted_row_unsafe(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            docs = _read_jsonl(root / "evidence_documents.jsonl")
            docs.append(
                {
                    "document_id": "DOC-SNAP",
                    "source_origin": "research_brain_v4_attempt",
                    "canonical_url": "snapshot://issuer_official/unpromoted_report.txt",
                }
            )
            write_jsonl(root / "evidence_documents.jsonl", docs)
            source_tasks = _read_jsonl(root / "source_task_executions.jsonl")
            source_tasks.append(
                {
                    "task_id": "TASK-SNAP",
                    "source_origin": "research_brain_v4_attempt",
                    "fetched_document_ids": ["DOC-SNAP"],
                    "accepted_claim_ids": [],
                }
            )
            write_jsonl(root / "source_task_executions.jsonl", source_tasks)

            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 2, "accepted_claim_count": 1},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "stagecourt_trace_id": "SCT-BRAIN-A",
                        "accepted_claim_ids": ["CLM-A"],
                        "score_contribution_ids": ["SCON-A"],
                        "primitive_state_ids": ["PRIM-A"],
                    }
                ],
            )

        self.assertEqual(audit["brain_snapshot_document_count"], 1)
        self.assertEqual(audit["brain_promoted_snapshot_document_count"], 0)
        self.assertEqual(audit["unsafe_promoted_stage_row_count"], 0)
        self.assertEqual(audit["verdict"], "PROMOTION_APPLIED")
        self.assertNotIn("promoted brain evidence documents include snapshot:// URLs", audit["blockers"])

    def test_mixed_web_and_official_brain_traces_promote_per_trace_without_global_blocker(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            write_jsonl(
                root / "source_task_executions.jsonl",
                [
                    {
                        "task_id": "TASK-A",
                        "source_origin": "research_brain_v4_attempt",
                        "fetched_document_ids": ["DOC-A"],
                        "accepted_claim_ids": ["CLM-A"],
                    },
                    {
                        "task_id": "TASK-B",
                        "source_origin": "research_brain_v4_attempt",
                        "fetched_document_ids": ["DOC-B"],
                        "accepted_claim_ids": ["CLM-B"],
                    },
                ],
            )
            docs = _read_jsonl(root / "evidence_documents.jsonl")
            docs.append(
                {
                    "document_id": "DOC-B",
                    "source_origin": "research_brain_v4_attempt",
                    "canonical_url": "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260701999999",
                }
            )
            write_jsonl(root / "evidence_documents.jsonl", docs)
            anchors = _read_jsonl(root / "evidence_anchors.jsonl")
            anchors.append({"anchor_id": "ANCH-B", "document_id": "DOC-B", "source_origin": "research_brain_v4_attempt"})
            write_jsonl(root / "evidence_anchors.jsonl", anchors)
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            accepted.append(
                {
                    "claim_id": "CLM-B",
                    "brain_web_claim": True,
                    "source_origin": "research_brain_v4_attempt",
                    "document_id": "DOC-B",
                    "anchor_id": "ANCH-B",
                    "event_date": "2026-06-30",
                    "target_scope_status": "DIRECT",
                    "temporal_status": "CURRENT",
                    "score_eligible": True,
                    "primitive_id": "delivery_schedule",
                    "source_provider": "OpenDART",
                    "source_url": "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260701999999",
                }
            )
            write_jsonl(root / "accepted_claims.jsonl", accepted)
            states = _read_jsonl(root / "primitive_states.jsonl")
            states.append(
                {
                    "primitive_state_id": "PRIM-B",
                    "source_origin": "research_brain_v4_attempt",
                    "primitive_id": "delivery_schedule",
                    "support_claim_ids": ["CLM-B"],
                    "counter_claim_ids": [],
                }
            )
            write_jsonl(root / "primitive_states.jsonl", states)
            write_jsonl(
                root / "score_contributions.jsonl",
                _read_jsonl(root / "score_contributions.jsonl")
                + [
                    {
                        "score_contribution_id": "SCON-B",
                        "source_origin": "research_brain_v4_attempt",
                        "support_claim_ids": ["CLM-B"],
                        "mapping_ids": ["MAP-B"],
                    }
                ],
            )
            write_jsonl(
                root / "brain_to_claim_trace.jsonl",
                _read_jsonl(root / "brain_to_claim_trace.jsonl")
                + [
                    {
                        "accepted_claim_id": "CLM-B",
                        "score_contribution_id": "SCON-B",
                        "primitive_state_ids": ["PRIM-B"],
                        "stagecourt_trace_id": "SCT-BRAIN-B",
                    }
                ],
            )
            write_jsonl(
                root / "stagecourt_traces.jsonl",
                _read_jsonl(root / "stagecourt_traces.jsonl")
                + [
                    {
                        "stagecourt_trace_id": "SCT-BRAIN-B",
                        "trace_id": "SCT-BRAIN-B",
                        "symbol": "000660",
                        "source_origin": "research_brain_v4_attempt",
                        "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                        "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                        "accepted_claim_ids": ["CLM-B"],
                        "score_contribution_ids": ["SCON-B"],
                        "primitive_state_ids": ["PRIM-B"],
                        "score_interval": {"lower": 24.0, "upper": 24.0},
                        "score_status": "FINAL",
                        "base_stage": "Stage1",
                        "transition_overlay": "NONE",
                        "investigation_status": "FINAL",
                        "missing_green_primitives": ["margin_bridge_visible"],
                        "missing_yellow_primitives": [],
                        "not_promoted_to_census_stage_status": True,
                    }
                ],
            )

            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
            )
            stage_rows, export = _promote_brain_stage_rows(
                config=config,
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 2, "accepted_claim_count": 2},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scope": "NO_SCORE",
                    },
                    {
                        "symbol": "000660",
                        "company_name": "SK하이닉스",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scope": "NO_SCORE",
                    },
                ],
            )
            audit = _brain_stage_promotion_audit(
                config=config,
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 2, "accepted_claim_count": 2},
                stage_rows=stage_rows,
            )

        rows_by_symbol = {row["symbol"]: row for row in stage_rows}
        self.assertEqual(export["promoted_stage_row_count"], 2)
        self.assertEqual(export["promoted_web_llm_stage_row_count"], 1)
        self.assertEqual(export["promoted_official_stage_row_count"], 1)
        self.assertEqual(rows_by_symbol["005930"]["stage_scope"], "BRAIN_WEB_PARTIAL")
        self.assertEqual(rows_by_symbol["000660"]["stage_scope"], "BRAIN_OFFICIAL_PARTIAL")
        self.assertEqual(rows_by_symbol["000660"]["operator_stage_use"], "NOT_FULL_THESIS_STAGE")
        self.assertEqual(rows_by_symbol["000660"]["full_thesis_stage"], "FULL_THESIS_NOT_RUN")
        self.assertEqual(rows_by_symbol["000660"]["official_source_task_count"], 1)
        self.assertEqual(rows_by_symbol["000660"]["official_evidence_document_count"], 1)
        self.assertEqual(rows_by_symbol["000660"]["official_source_task_ids"], ["TASK-B"])
        self.assertEqual(rows_by_symbol["000660"]["official_evidence_document_ids"], ["DOC-B"])
        self.assertEqual(audit["verdict"], "PROMOTION_APPLIED")
        self.assertEqual(audit["brain_stage_trace_with_web_or_llm_claim_count"], 1)
        self.assertEqual(audit["brain_stage_trace_with_official_claim_count"], 1)
        self.assertEqual(audit["brain_stage_trace_without_supported_claim_count"], 0)
        self.assertEqual(audit["unsafe_promoted_stage_row_count"], 0)

    def test_promoted_brain_trace_reference_mismatch_is_unsafe(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            traces[0]["census_stage_status_id"] = "CSS-BAD"
            write_jsonl(root / "brain_to_claim_trace.jsonl", traces)

            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=[
                    {
                        "census_stage_status_id": "CSS-BAD",
                        "symbol": "005930",
                        "stage_source": "research_brain_v4_attempt",
                        "stagecourt_trace_id": "SCT-BRAIN-A",
                        "accepted_claim_ids": ["CLM-A"],
                        "score_contribution_ids": ["SCON-OTHER"],
                        "primitive_state_ids": ["PRIM-A"],
                    }
                ],
            )

        self.assertEqual(audit["verdict"], "FAIL_UNSAFE_PROMOTION")
        self.assertEqual(audit["brain_trace_promoted_reference_error_count"], 1)
        self.assertIn("brain_to_claim_trace promoted references are dangling or mismatched: 1", audit["blockers"])

    def test_strict_live_connected_brain_trace_promotes_representative_row_and_updates_trace_refs(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            stage_rows, export = _promote_brain_stage_rows(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            stagecourt = _read_jsonl(root / "stagecourt_traces.jsonl")

        self.assertEqual(export["promoted_stage_row_count"], 1)
        self.assertEqual(stage_rows[0]["stage_source"], "research_brain_v4_attempt")
        self.assertEqual(stage_rows[0]["stage_scope"], "BRAIN_WEB_PARTIAL")
        self.assertEqual(stage_rows[0]["score_scope"], "BRAIN_WEB_CLAIM_BACKED_PARTIAL")
        self.assertEqual(stage_rows[0]["operator_stage_use"], "NOT_FULL_THESIS_STAGE")
        self.assertEqual(stage_rows[0]["operator_score_use"], "NOT_FULL_E2R_SCORE")
        self.assertEqual(stage_rows[0]["operator_scope_note"], "brain_web_claim_backed_partial_not_full_thesis")
        self.assertTrue(stage_rows[0]["base_stage_display"].startswith("BRAIN_WEB_PARTIAL_"))
        self.assertTrue(stage_rows[0]["stage_decision_status_display"].startswith("BRAIN_WEB_PARTIAL_"))
        self.assertEqual(stage_rows[0]["candidate_event_id"], "CE-BRAIN-A")
        self.assertIn("CE-BRAIN-A", stage_rows[0]["candidate_event_ids"])
        self.assertEqual(stage_rows[0]["candidate_event_count"], 1)
        self.assertIn("CE-BRAIN-A", stage_rows[0]["investigation_only_candidate_event_ids"])
        self.assertEqual(stage_rows[0]["candidate_event_scope"], "CANDIDATE_EVENTS_PRESENT")
        self.assertEqual(stage_rows[0]["full_thesis_stage"], "FULL_THESIS_NOT_RUN")
        self.assertEqual(stage_rows[0]["accepted_claim_ids"], ["CLM-A"])
        self.assertEqual(stage_rows[0]["score_contribution_ids"], ["SCON-A"])
        self.assertEqual(stage_rows[0]["primitive_state_ids"], ["PRIM-A"])
        self.assertEqual(stage_rows[0]["stagecourt_trace_id"], "SCT-BRAIN-A")
        self.assertTrue(stage_rows[0]["census_stage_status_id"])
        self.assertEqual(traces[0]["census_stage_status_id"], stage_rows[0]["census_stage_status_id"])
        self.assertEqual(traces[0]["trace_status"], "CLAIM_SCORE_TRACE_PROMOTED_TO_CENSUS_STAGE_STATUS")
        self.assertIs(stagecourt[0]["not_promoted_to_census_stage_status"], False)
        self.assertIs(stagecourt[0]["promoted_to_census_stage_status"], True)

    def test_final_stage_row_sync_clears_stale_brain_promotion_refs(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            stagecourt = _read_jsonl(root / "stagecourt_traces.jsonl")
            stale_trace = {
                **stagecourt[0],
                "stagecourt_trace_id": "SCT-BRAIN-STALE",
                "trace_id": "SCT-BRAIN-STALE",
                "not_promoted_to_census_stage_status": False,
                "promoted_to_census_stage_status": True,
                "census_stage_status_id": "CSS-BRAIN-STALE",
            }
            stagecourt[0]["not_promoted_to_census_stage_status"] = False
            stagecourt[0]["promoted_to_census_stage_status"] = True
            stagecourt[0]["census_stage_status_id"] = "CSS-BRAIN-OLD"
            write_jsonl(root / "stagecourt_traces.jsonl", [stagecourt[0], stale_trace])
            brain_traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            brain_traces[0]["census_stage_status_id"] = "CSS-BRAIN-OLD"
            brain_traces[0]["trace_status"] = "CLAIM_SCORE_TRACE_PROMOTED_TO_CENSUS_STAGE_STATUS"
            brain_traces.append(
                {
                    **brain_traces[0],
                    "stagecourt_trace_id": "SCT-BRAIN-STALE",
                    "census_stage_status_id": "CSS-BRAIN-STALE",
                }
            )
            write_jsonl(root / "brain_to_claim_trace.jsonl", brain_traces)

            final_stage_rows = [
                {
                    "symbol": "005930",
                    "stagecourt_trace_id": "SCT-BRAIN-A",
                    "census_stage_status_id": "CSS-BRAIN-FINAL",
                    "stage_source": "research_brain_v4_attempt",
                    "accepted_claim_ids": ["CLM-A"],
                    "score_contribution_ids": ["SCON-A"],
                    "primitive_state_ids": ["PRIM-A"],
                }
            ]
            _sync_brain_trace_promotion_markers(output_root=root, stage_rows=final_stage_rows)
            updated_stagecourt = {
                row["stagecourt_trace_id"]: row
                for row in _read_jsonl(root / "stagecourt_traces.jsonl")
            }
            updated_traces = {
                row["stagecourt_trace_id"]: row
                for row in _read_jsonl(root / "brain_to_claim_trace.jsonl")
            }
            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=final_stage_rows,
            )

        self.assertEqual(updated_stagecourt["SCT-BRAIN-A"]["census_stage_status_id"], "CSS-BRAIN-FINAL")
        self.assertIs(updated_stagecourt["SCT-BRAIN-A"]["not_promoted_to_census_stage_status"], False)
        self.assertIs(updated_stagecourt["SCT-BRAIN-STALE"]["not_promoted_to_census_stage_status"], True)
        self.assertIsNone(updated_stagecourt["SCT-BRAIN-STALE"]["census_stage_status_id"])
        self.assertEqual(updated_traces["SCT-BRAIN-A"]["census_stage_status_id"], "CSS-BRAIN-FINAL")
        self.assertIsNone(updated_traces["SCT-BRAIN-STALE"]["census_stage_status_id"])
        self.assertEqual(updated_traces["SCT-BRAIN-STALE"]["not_promoted_reason"], "stagecourt_trace_not_in_final_census_stage_status")
        self.assertEqual(audit["brain_stage_trace_not_promoted_marker_missing_count"], 0)
        self.assertEqual(audit["brain_trace_promoted_reference_error_count"], 0)
        self.assertEqual(audit["verdict"], "PROMOTION_APPLIED")

    def test_non_score_brain_claim_is_not_promoted_as_representative_stage_claim(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            accepted.append({**accepted[0], "claim_id": "CLM-B", "primitive_id": "medium_term_revision_visibility"})
            write_jsonl(root / "accepted_claims.jsonl", accepted)
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            traces.append(
                {
                    **traces[0],
                    "accepted_claim_id": "CLM-B",
                    "score_contribution_id": None,
                    "score_contribution_ids": [],
                    "primitive_state_id": None,
                    "primitive_state_ids": [],
                    "score_support_status": "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING",
                    "representative_score_claim": False,
                    "trace_status": "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING",
                }
            )
            write_jsonl(root / "brain_to_claim_trace.jsonl", traces)

            stage_rows, export = _promote_brain_stage_rows(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 2},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            updated_traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            promotion_audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 2},
                stage_rows=stage_rows,
            )

        self.assertEqual(export["promoted_stage_row_count"], 1)
        self.assertEqual(stage_rows[0]["accepted_claim_ids"], ["CLM-A"])
        self.assertEqual(stage_rows[0]["primitive_state_ids"], ["PRIM-A"])
        self.assertIsNotNone(updated_traces[0]["census_stage_status_id"])
        self.assertIsNone(updated_traces[1]["census_stage_status_id"])
        self.assertEqual(updated_traces[1]["not_promoted_reason"], "accepted_claim_not_in_representative_score_claim_ids")
        self.assertEqual(promotion_audit["verdict"], "PROMOTION_APPLIED")
        self.assertEqual(promotion_audit["brain_trace_promoted_reference_error_count"], 0)

    def test_pending_material_gap_brain_stage_is_not_production_full_thesis_without_green_gate_coverage(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="meaningful",
            )
            stage_rows, _ = _promote_brain_stage_rows(
                config=config,
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=stage_rows,
            )
            follow_up_tasks = _read_jsonl(root / "full_thesis_blocker_follow_up_source_tasks.jsonl")
            follow_up_seed_events = _read_jsonl(root / "full_thesis_blocker_follow_up_seed_events.jsonl")
            connector_audit = _source_connector_capability_audit(config=config, output_root=root)

        self.assertEqual(stage_rows[0]["stage_scope"], "BRAIN_WEB_PARTIAL")
        self.assertEqual(stage_rows[0]["operator_stage_use"], "NOT_FULL_THESIS_STAGE")
        self.assertEqual(audit["candidate_row_count"], 1)
        self.assertEqual(audit["promoted_full_thesis_row_count"], 0)
        self.assertEqual(audit["verdict"], "PENDING_PRODUCTION_FULL_THESIS")
        self.assertEqual(audit["blocked_candidates"][0]["blockers"], ["score_status_not_final"])
        self.assertEqual(audit["blocked_candidate_blocker_counts"]["score_status_not_final"], 1)
        self.assertNotIn("missing_green_gate_primitives", audit["blocked_candidate_blocker_counts"])
        self.assertEqual(audit["blocked_candidate_archetype_counts"]["C06_HBM_MEMORY_CUSTOMER_CAPACITY"], 1)
        self.assertEqual(
            audit["blocked_candidate_missing_green_primitive_counts"],
            {
                "customer_preorder_or_allocation": 1,
                "hbm_capacity_constraint": 1,
                "hbm_capacity_pre_sold": 1,
                "revenue_visibility_contract": 1,
            },
        )
        self.assertEqual(
            audit["blocked_candidate_missing_green_primitive_counts_by_archetype"],
            {
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": {
                    "customer_preorder_or_allocation": 1,
                    "hbm_capacity_constraint": 1,
                    "hbm_capacity_pre_sold": 1,
                    "revenue_visibility_contract": 1,
                }
            },
        )
        self.assertEqual(audit["blocked_candidate_follow_up_source_task_count"], 4)
        self.assertEqual(audit["blocked_candidate_follow_up_seed_event_count"], 4)
        self.assertEqual(len(follow_up_tasks), 4)
        self.assertEqual(len(follow_up_seed_events), 4)
        self.assertEqual(
            {task["primitive_gap"] for task in follow_up_tasks},
            {
                "customer_preorder_or_allocation",
                "hbm_capacity_constraint",
                "hbm_capacity_pre_sold",
                "revenue_visibility_contract",
            },
        )
        for task in follow_up_tasks:
            self.assertEqual(task["source_task_origin"], "full_thesis_green_gate_blocker_follow_up")
            self.assertEqual(task["task_type"], "green_closure")
            self.assertEqual(task["task_status"], "PLANNING_REQUIRED")
            self.assertTrue(task["planner_required"])
            self.assertTrue(task["llm_query_required"])
            self.assertTrue(task["llm_query_allowed"])
            self.assertTrue(task["general_search_allowed"])
            self.assertTrue(task["official_first_required"])
            self.assertEqual(task["follow_up_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
            self.assertEqual(task["follow_up_primitive_gap"], task["primitive_gap"])
            self.assertFalse(task["score_allowed_before_execution"])
            self.assertFalse(task["stage_promotion_allowed_before_execution"])
            self.assertEqual(task["hardcoded_query_count"], 0)
            self.assertEqual(task["hardcoded_queries"], [])
            self.assertEqual(task["query_intents"], [])
            self.assertGreater(task["max_queries"], 0)
            self.assertGreater(task["max_candidates"], 0)
            self.assertGreater(task["max_fetches"], 0)
            self.assertIn("unbounded_general_search", task["forbidden_source_classes"])
        seed_payloads_by_gap = {
            seed["structured_payload"]["follow_up_primitive_gap"]: seed["structured_payload"]
            for seed in follow_up_seed_events
        }
        self.assertEqual(set(seed_payloads_by_gap), {task["primitive_gap"] for task in follow_up_tasks})
        for seed in follow_up_seed_events:
            self.assertEqual(seed["source_family"], "CensusFullThesisBlockerFollowUp")
            self.assertEqual(seed["event_type"], "full_thesis_blocker_follow_up_seed")
            self.assertEqual(seed["target_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
            self.assertEqual(seed["target_archetype_status"], "GREEN_GATE_BLOCKER_FOLLOW_UP")
            self.assertEqual(seed["primitive_gap"], seed["follow_up_primitive_gap"])
            self.assertIn(seed["follow_up_primitive_gap"], {task["primitive_gap"] for task in follow_up_tasks})
            self.assertEqual(seed["follow_up_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
            self.assertTrue(str(seed["follow_up_task_id"]).startswith("FTGAP-"))
            self.assertTrue(seed["research_brain_eligible"])
            self.assertFalse(seed["score_evidence_allowed"])
            self.assertFalse(seed["stage_promotion_allowed_before_execution"])
            payload = seed["structured_payload"]
            _assert_no_forbidden_brain_payload_keys(payload)
            self.assertEqual(payload["seed_role"], "planner_input_only")
            self.assertEqual(seed["follow_up_task_id"], payload["follow_up_task_id"])
            self.assertEqual(seed["follow_up_archetype_id"], payload["follow_up_archetype_id"])
            self.assertEqual(seed["follow_up_primitive_gap"], payload["follow_up_primitive_gap"])
            self.assertEqual(payload["target_archetype"], seed["target_archetype"])
            self.assertEqual(payload["target_archetype_status"], seed["target_archetype_status"])
            self.assertEqual(payload["primitive_gap"], seed["primitive_gap"])
            self.assertEqual(payload["follow_up_origin"], "full_thesis_green_gate_blocker_follow_up")
            self.assertTrue(payload["llm_query_required"])
            self.assertTrue(payload["llm_query_allowed"])
            self.assertTrue(payload["general_search_allowed"])
            self.assertEqual(payload["hardcoded_query_count"], 0)
            self.assertEqual(payload["hardcoded_queries"], [])
            self.assertEqual(payload["query_intents"], [])
            self.assertEqual(payload["max_queries"], 3)
            self.assertEqual(payload["max_candidates"], 20)
            self.assertEqual(payload["max_fetches"], 3)
        self.assertEqual(connector_audit["blocking_full_thesis_task_count"], 0)
        self.assertEqual(connector_audit["full_thesis_task_with_blocking_source_class_count"], len(follow_up_tasks))
        self.assertTrue(connector_audit["full_thesis_task_executable_source_path_pass_allowed"])
        self.assertEqual(connector_audit["verdict"], "SOURCE_CONNECTOR_CAPABILITY_PASS")
        self.assertTrue(connector_audit["source_connector_capability_pass_allowed"])
        self.assertEqual(connector_audit["blocking_full_thesis_source_classes"], [])
        self.assertIn("IssuerIR", connector_audit["non_executable_full_thesis_source_classes"])
        self.assertNotIn("TrustedNews", connector_audit["non_executable_full_thesis_source_classes"])
        self.assertIn("TrustedNews", connector_audit["bounded_web_acquisition_source_classes"])
        follow_up_task_ids = {task["task_id"] for task in follow_up_tasks}
        audited_task_ids = {
            task_id
            for row in connector_audit["source_classes"]
            for task_id in row.get("full_thesis_task_ids") or []
        }
        self.assertTrue(follow_up_task_ids <= audited_task_ids)

    def test_final_brain_stage_with_green_gap_is_production_full_thesis_but_not_green_complete(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            traces = _read_jsonl(root / "stagecourt_traces.jsonl")
            traces[0]["score_status"] = "FINAL"
            traces[0]["base_stage"] = "Stage2-Watch"
            traces[0]["investigation_status"] = "COMPLETE"
            traces[0]["missing_green_primitives"] = [
                "customer_preorder_or_allocation",
                "hbm_capacity_constraint",
                "hbm_capacity_pre_sold",
                "revenue_visibility_contract",
            ]
            write_jsonl(root / "stagecourt_traces.jsonl", traces)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="meaningful",
            )
            stage_rows, _ = _promote_brain_stage_rows(
                config=config,
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 1, "accepted_claim_count": 1},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=stage_rows,
            )
            production_audit = _full_thesis_production_audit(config=config, stage_rows=stage_rows)
            follow_up_tasks = _read_jsonl(root / "full_thesis_blocker_follow_up_source_tasks.jsonl")

        row = stage_rows[0]
        self.assertEqual(audit["verdict"], "PRODUCTION_FULL_THESIS_PROMOTED")
        self.assertEqual(audit["promoted_full_thesis_row_count"], 1)
        self.assertEqual(audit["blocked_candidate_count"], 0)
        self.assertEqual(audit["blocked_candidate_blocker_counts"], {})
        self.assertEqual(len(follow_up_tasks), 0)
        self.assertEqual(row["stage_scope"], "FULL_THESIS")
        self.assertEqual(row["score_scale"], "FULL_E2R_100")
        self.assertEqual(row["full_thesis_stage"], "Stage2-Watch")
        self.assertEqual(row["full_thesis_missing_primitives"], [])
        self.assertEqual(
            row["full_thesis_green_gap_primitives"],
            [
                "customer_preorder_or_allocation",
                "hbm_capacity_constraint",
                "hbm_capacity_pre_sold",
                "revenue_visibility_contract",
            ],
        )
        self.assertFalse(row["full_thesis_green_gate_complete"])
        self.assertFalse(production_audit["production_pass_allowed"])
        self.assertEqual(production_audit["production_full_thesis_row_count"], 1)
        self.assertIn(
            "production_full_thesis_rows_with_required_positive_missing_primitives",
            production_audit["blockers"],
        )

    def test_provider_failed_green_gap_blocks_production_full_thesis_final_score(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            traces = _read_jsonl(root / "stagecourt_traces.jsonl")
            traces[0]["accepted_claim_ids"] = ["CLM-1", "CLM-2", "CLM-4"]
            traces[0]["score_contribution_ids"] = ["SCON-1", "SCON-2", "SCON-4"]
            traces[0]["primitive_state_ids"] = ["PRIM-1", "PRIM-2", "PRIM-4"]
            traces[0]["score_interval"] = {"lower": 63.0, "upper": 88.0}
            traces[0]["score_status"] = "FINAL"
            traces[0]["base_stage"] = "Stage2-Watch"
            write_jsonl(root / "stagecourt_traces.jsonl", traces)
            executions = _read_jsonl(root / "source_task_executions.jsonl")
            executions[2].update(
                {
                    "status": "PROVIDER_FAILED",
                    "accepted_claim_ids": [],
                    "fetched_document_ids": [],
                    "primitive_gap": "hbm_capacity_constraint",
                    "primitive_gap_unsatisfied_ids": ["hbm_capacity_constraint"],
                    "provider_errors": ["trusted_news_provider_not_configured; general search is not a score source"],
                    "stop_reason": "live_official_provider_failed_web_no_evidence_found",
                    "source_task": {
                        "task_id": "TASK-3",
                        "candidate_event_id": "CE-BRAIN-FULL",
                        "symbol": "005930",
                        "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "primitive_gap": "hbm_capacity_constraint",
                    },
                }
            )
            write_jsonl(root / "source_task_executions.jsonl", executions)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="full_thesis",
            )

            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            production_audit = _full_thesis_production_audit(config=config, stage_rows=stage_rows)
            follow_up_tasks = _read_jsonl(root / "full_thesis_blocker_follow_up_source_tasks.jsonl")

        self.assertEqual(audit["promoted_full_thesis_row_count"], 0)
        self.assertEqual(audit["blocked_candidate_count"], 1)
        self.assertIn("source_pending_required_or_green_primitives", audit["blocked_candidate_blocker_counts"])
        self.assertEqual(
            audit["blocked_candidate_source_pending_gap_primitive_counts"],
            {"hbm_capacity_constraint": 1},
        )
        blocked = audit["blocked_candidates"][0]
        self.assertEqual(blocked["source_pending_green_primitives"], ["hbm_capacity_constraint"])
        self.assertEqual(blocked["source_pending_required_primitives"], ["hbm_capacity_constraint"])
        self.assertEqual(blocked["source_pending_gap_proof"][0]["status"], "PROVIDER_FAILED")
        self.assertEqual(stage_rows[0]["stage_scope"], "CENSUS_EVENT_BOARD")
        self.assertEqual(stage_rows[0]["full_thesis_stage"], "FULL_THESIS_NOT_RUN")
        self.assertEqual(production_audit["production_full_thesis_row_count"], 0)
        self.assertIn("production_full_thesis_runner_no_eligible_rows", production_audit["blockers"])
        self.assertEqual({task["primitive_gap"] for task in follow_up_tasks}, {"hbm_capacity_constraint"})

    def test_provider_failed_guard_gap_does_not_count_as_positive_required_source_pending(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            primitives = (
                "contract_amount_to_prior_sales",
                "contract_duration_months",
                "margin_bridge_visible",
                "delivery_schedule",
            )
            write_jsonl(root / "planner_runs.jsonl", [{"provider_mode": "real", "real_provider_success": True}])
            write_jsonl(root / "claim_extractor_runs.jsonl", [{"provider_mode": "llm", "provider_name": "codex_cli_contract_blind_extractor"}])
            write_jsonl(
                root / "source_task_executions.jsonl",
                [
                    {
                        "task_id": f"TASK-C05-{idx}",
                        "source_origin": "research_brain_v4_attempt",
                        "candidate_event_id": "CE-BRAIN-C05",
                        "primitive_gap": primitive,
                        "status": "EVIDENCE_OS_ACCEPTED",
                        "fetched_document_ids": [f"DOC-C05-{idx}"],
                        "accepted_claim_ids": [f"CLM-C05-{idx}"],
                    }
                    for idx, primitive in enumerate(primitives, 1)
                ]
                + [
                    {
                        "task_id": "TASK-C05-GUARD",
                        "source_origin": "research_brain_v4_attempt",
                        "candidate_event_id": "CE-BRAIN-C05",
                        "primitive_gap": "cost_overrun",
                        "primitive_gap_unsatisfied_ids": ["cost_overrun"],
                        "status": "PROVIDER_FAILED",
                        "fetched_document_ids": [],
                        "accepted_claim_ids": [],
                        "provider_errors": ["issuer_ir_discovery_not_configured; guard follow-up pending"],
                    }
                ],
            )
            write_jsonl(
                root / "evidence_documents.jsonl",
                [
                    {
                        "document_id": f"DOC-C05-{idx}",
                        "source_origin": "research_brain_v4_attempt",
                        "canonical_url": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260701{idx:06d}",
                    }
                    for idx, _ in enumerate(primitives, 1)
                ],
            )
            write_jsonl(
                root / "evidence_anchors.jsonl",
                [
                    {
                        "anchor_id": f"ANCH-C05-{idx}",
                        "document_id": f"DOC-C05-{idx}",
                        "source_origin": "research_brain_v4_attempt",
                    }
                    for idx, _ in enumerate(primitives, 1)
                ],
            )
            write_jsonl(
                root / "accepted_claims.jsonl",
                [
                    {
                        "claim_id": f"CLM-C05-{idx}",
                        "brain_web_claim": True,
                        "source_origin": "research_brain_v4_attempt",
                        "document_id": f"DOC-C05-{idx}",
                        "anchor_id": f"ANCH-C05-{idx}",
                        "event_date": "2026-06-30",
                        "target_scope_status": "DIRECT",
                        "temporal_status": "CURRENT",
                        "score_eligible": True,
                        "primitive_id": primitive,
                        "mapping_status": "ACCEPTED",
                        "support_direction": "SUPPORT",
                    }
                    for idx, primitive in enumerate(primitives, 1)
                ],
            )
            write_jsonl(
                root / "primitive_states.jsonl",
                [
                    {
                        "primitive_state_id": f"PRIM-C05-{idx}",
                        "source_origin": "research_brain_v4_attempt",
                        "primitive_id": primitive,
                        "support_claim_ids": [f"CLM-C05-{idx}"],
                        "counter_claim_ids": [],
                    }
                    for idx, primitive in enumerate(primitives, 1)
                ],
            )
            write_jsonl(
                root / "score_contributions.jsonl",
                [
                    {
                        "score_contribution_id": f"SCON-C05-{idx}",
                        "source_origin": "research_brain_v4_attempt",
                        "support_claim_ids": [f"CLM-C05-{idx}"],
                        "mapping_ids": [f"MAP-C05-{idx}"],
                    }
                    for idx, _ in enumerate(primitives, 1)
                ],
            )
            write_jsonl(
                root / "brain_to_claim_trace.jsonl",
                [
                    {
                        "accepted_claim_id": f"CLM-C05-{idx}",
                        "score_contribution_id": f"SCON-C05-{idx}",
                        "primitive_state_ids": [f"PRIM-C05-{idx}"],
                        "stagecourt_trace_id": "SCT-BRAIN-C05",
                    }
                    for idx, _ in enumerate(primitives, 1)
                ],
            )
            write_jsonl(
                root / "stagecourt_traces.jsonl",
                [
                    {
                        "stagecourt_trace_id": "SCT-BRAIN-C05",
                        "trace_id": "SCT-BRAIN-C05",
                        "symbol": "047040",
                        "company_name": "대우건설",
                        "candidate_event_id": "CE-BRAIN-C05",
                        "source_origin": "research_brain_v4_attempt",
                        "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                        "accepted_claim_ids": [f"CLM-C05-{idx}" for idx, _ in enumerate(primitives, 1)],
                        "score_contribution_ids": [f"SCON-C05-{idx}" for idx, _ in enumerate(primitives, 1)],
                        "primitive_state_ids": [f"PRIM-C05-{idx}" for idx, _ in enumerate(primitives, 1)],
                        "score_interval": {"lower": 74.0, "upper": 74.0},
                        "score_status": "FINAL",
                        "base_stage": "Stage3-Yellow",
                    }
                ],
            )

            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="full_thesis",
            )
            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "047040",
                        "company_name": "대우건설",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )

        row = stage_rows[0]
        self.assertEqual(audit["promoted_full_thesis_row_count"], 1)
        self.assertEqual(audit["blocked_candidate_count"], 0)
        self.assertEqual(row["stage_scope"], "FULL_THESIS")
        self.assertEqual(row["full_thesis_source_pending_gap_primitives"], [])
        self.assertEqual(row["full_thesis_source_pending_required_gap_primitives"], [])
        self.assertEqual(row["full_thesis_required_gap_primitives"], [])
        self.assertEqual(row["full_thesis_required_positive_missing_primitives"], [])
        self.assertTrue(row["full_thesis_green_gate_complete"])

    def test_production_audit_blocks_full_thesis_row_with_source_pending_gap(self):
        config = CensusV4RunConfig(as_of_date="2026-07-01", target_gate="full_thesis")

        production_audit = _full_thesis_production_audit(
            config=config,
            stage_rows=[
                {
                    "symbol": "005930",
                    "stage_scope": "FULL_THESIS",
                    "score_scale": "FULL_E2R_100",
                    "full_thesis_score_valid_status": "FINAL",
                    "full_thesis_accepted_claim_ids": ["CLM-1"],
                    "full_thesis_score_contribution_ids": ["SCON-1"],
                    "full_thesis_stagecourt_trace_ids": ["SCT-1"],
                    "full_thesis_source_pending_gap_primitives": ["hbm_capacity_constraint"],
                    "full_thesis_source_pending_green_gap_primitives": ["hbm_capacity_constraint"],
                }
            ],
        )

        self.assertFalse(production_audit["production_pass_allowed"])
        self.assertEqual(production_audit["production_full_thesis_final_with_source_pending_gap_count"], 1)
        self.assertEqual(production_audit["provider_failed_green_gap_final_score_count"], 1)
        self.assertIn(
            "production_full_thesis_rows_with_source_pending_required_or_green_gap",
            production_audit["blockers"],
        )

    def test_production_audit_blocks_required_positive_missing_primitives(self):
        config = CensusV4RunConfig(as_of_date="2026-07-01", target_gate="full_thesis")

        production_audit = _full_thesis_production_audit(
            config=config,
            stage_rows=[
                {
                    "symbol": "047040",
                    "stage_scope": "FULL_THESIS",
                    "score_scale": "FULL_E2R_100",
                    "full_thesis_score_valid_status": "FINAL",
                    "full_thesis_accepted_claim_ids": ["CLM-1"],
                    "full_thesis_score_contribution_ids": ["SCON-1"],
                    "full_thesis_stagecourt_trace_ids": ["SCT-1"],
                    "full_thesis_required_gap_primitives": [],
                    "full_thesis_required_positive_missing_primitives": [
                        "contract_duration_months",
                        "margin_bridge_visible",
                    ],
                }
            ],
        )

        self.assertFalse(production_audit["production_pass_allowed"])
        self.assertIn(
            "production_full_thesis_rows_with_required_positive_missing_primitives",
            production_audit["blockers"],
        )
        self.assertEqual(production_audit["production_full_thesis_row_count"], 1)
        self.assertEqual(production_audit["production_full_thesis_row_with_missing_required_primitives_count"], 0)
        self.assertEqual(production_audit["production_full_thesis_row_with_blocking_required_gap_primitives_count"], 0)
        self.assertEqual(production_audit["production_full_thesis_row_with_required_positive_missing_primitives_count"], 1)
        self.assertEqual(production_audit["production_symbols_without_missing_required_primitives"], ["047040"])
        self.assertEqual(production_audit["production_symbols_without_required_positive_missing_primitives"], [])

    def test_green_gap_follow_up_trace_does_not_replace_representative_full_thesis_row(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            traces = _read_jsonl(root / "stagecourt_traces.jsonl")
            traces.append(
                {
                    "stagecourt_trace_id": "SCT-BRAIN-FTGAP",
                    "trace_id": "SCT-BRAIN-FTGAP",
                    "symbol": "005930",
                    "candidate_event_id": "CEV4-FTGAP-005930-GREEN-GAP",
                    "source_origin": "research_brain_v4_attempt",
                    "primary_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "accepted_claim_ids": ["CLM-1"],
                    "score_contribution_ids": ["SCON-1"],
                    "primitive_state_ids": ["PRIM-1"],
                    "score_interval": {"lower": 4.0, "upper": 4.0},
                    "score_status": "FINAL",
                    "base_stage": "Stage0",
                    "transition_overlay": "NONE",
                    "investigation_status": "COMPLETE",
                    "missing_green_primitives": [
                        "customer_preorder_or_allocation",
                        "revenue_visibility_contract",
                        "hbm_capacity_constraint",
                        "hbm_capacity_pre_sold",
                    ],
                }
            )
            write_jsonl(root / "stagecourt_traces.jsonl", traces)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="meaningful",
            )
            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            atomic_rows = {item["atomic_stage_decision_id"]: item for item in _read_jsonl(root / "atomic_stage_decisions.jsonl")}
            event_rows = {item["event_id"]: item for item in _read_jsonl(root / "census_events.jsonl")}

        row = stage_rows[0]
        self.assertEqual(audit["candidate_row_count"], 1)
        self.assertEqual(audit["promoted_full_thesis_trace_count"], 1)
        self.assertEqual(audit["promoted_stagecourt_trace_ids"], ["SCT-BRAIN-FULL"])
        self.assertEqual(row["full_thesis_stagecourt_trace_ids"], ["SCT-BRAIN-FULL"])
        self.assertEqual(row["full_thesis_candidate_event_id"], "CE-BRAIN-FULL")
        self.assertIn("CE-BRAIN-FULL", row["candidate_event_ids"])
        self.assertIn("CE-BRAIN-FULL", row["score_eligible_candidate_event_ids"])
        self.assertEqual(row["full_e2r_verified_score"], 84.0)
        self.assertTrue(row["atomic_stage_decision_id"].startswith("ATOMIC-FTPROD-"))
        atomic = atomic_rows[row["atomic_stage_decision_id"]]
        self.assertEqual(atomic["stage_scope"], "FULL_THESIS")
        self.assertEqual(atomic["accepted_claim_ids"], row["accepted_claim_ids"])
        self.assertEqual(atomic["score_contribution_ids"], row["score_contribution_ids"])
        self.assertEqual(atomic["primitive_state_ids"], row["primitive_state_ids"])
        event = event_rows[row["full_thesis_candidate_event_id"]]
        self.assertEqual(event["event_category"], "FullThesisProductionEvent")
        self.assertEqual(event["atomic_stage_decision_id"], row["atomic_stage_decision_id"])

    def test_full_green_gate_brain_stage_can_be_promoted_to_production_full_thesis(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="meaningful",
            )
            stage_rows, _ = _promote_brain_stage_rows(
                config=config,
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 4, "accepted_claim_count": 4},
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=stage_rows,
            )
            production_audit = _full_thesis_production_audit(config=config, stage_rows=stage_rows)
            atomic_rows = {item["atomic_stage_decision_id"]: item for item in _read_jsonl(root / "atomic_stage_decisions.jsonl")}
            event_rows = {item["event_id"]: item for item in _read_jsonl(root / "census_events.jsonl")}
            write_jsonl(root / "census_stage_status.jsonl", stage_rows)
            primitive_chain = _primitive_state_chain_audit(root)

        row = stage_rows[0]
        self.assertEqual(audit["verdict"], "PRODUCTION_FULL_THESIS_PROMOTED")
        self.assertEqual(audit["candidate_source_counts"], {"brain_web_partial_stage_row": 1})
        self.assertEqual(audit["promoted_full_thesis_row_count"], 1)
        self.assertEqual(row["stage_scope"], "FULL_THESIS")
        self.assertEqual(row["score_scale"], "FULL_E2R_100")
        self.assertEqual(row["score_scope"], "FULL_E2R_100")
        self.assertEqual(row["operator_stage_use"], "FULL_THESIS_STAGE")
        self.assertEqual(row["operator_score_use"], "FULL_E2R_SCORE")
        self.assertEqual(row["primary_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(row["canonical_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(row["archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(row["full_thesis_primary_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(row["full_thesis_production_mode"], "research_brain_v4_production")
        self.assertEqual(row["full_thesis_missing_primitives"], [])
        self.assertIn("CE-BRAIN-FULL", row["candidate_event_ids"])
        self.assertIn("CE-BRAIN-FULL", row["score_eligible_candidate_event_ids"])
        self.assertEqual(row["full_e2r_verified_score"], 84.0)
        self.assertFalse(production_audit["production_pass_allowed"])
        self.assertEqual(production_audit["production_full_thesis_row_count"], 1)
        self.assertEqual(production_audit["controlled_smoke_full_thesis_row_count"], 0)
        self.assertIn(
            "production_full_thesis_rows_with_required_positive_missing_primitives",
            production_audit["blockers"],
        )
        self.assertEqual(row["full_thesis_source_task_ids"], ["TASK-1", "TASK-2", "TASK-3", "TASK-4"])
        self.assertTrue(all(proof["linked"] for proof in row["full_thesis_source_linkage_proof"]))
        self.assertTrue(row["atomic_stage_decision_id"].startswith("ATOMIC-FTPROD-"))
        atomic = atomic_rows[row["atomic_stage_decision_id"]]
        self.assertTrue(atomic["is_representative"])
        self.assertEqual(atomic["stagecourt_trace_id"], row["stagecourt_trace_id"])
        self.assertEqual(atomic["accepted_claim_ids"], row["accepted_claim_ids"])
        self.assertEqual(atomic["score_contribution_ids"], row["score_contribution_ids"])
        self.assertEqual(atomic["primitive_state_ids"], row["primitive_state_ids"])
        event = event_rows[row["full_thesis_candidate_event_id"]]
        self.assertEqual(event["event_category"], "FullThesisProductionEvent")
        self.assertEqual(event["atomic_stage_decision_id"], row["atomic_stage_decision_id"])
        self.assertEqual(primitive_chain["verdict"], "PASS")
        self.assertEqual(primitive_chain["critical_counts"]["atomic_decision_primitive_set_mismatch_count"], 0)

    def test_full_thesis_blocks_claim_not_linked_to_same_live_source_document(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            executions = _read_jsonl(root / "source_task_executions.jsonl")
            executions[0]["fetched_document_ids"] = ["DOC-OTHER"]
            write_jsonl(root / "source_task_executions.jsonl", executions)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="meaningful",
            )

            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )

        self.assertEqual(stage_rows[0]["stage_scope"], "CENSUS_EVENT_BOARD")
        self.assertEqual(audit["verdict"], "PENDING_PRODUCTION_FULL_THESIS")
        blockers = audit["blocked_candidates"][0]["blockers"]
        self.assertIn("claim_not_linked_to_live_source_task_document", blockers)
        proof = audit["blocked_candidates"][0]["source_linkage_proof"]
        self.assertFalse(next(row for row in proof if row["claim_id"] == "CLM-1")["linked"])

    def test_full_thesis_blocks_missing_score_interval_upper(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            traces = _read_jsonl(root / "stagecourt_traces.jsonl")
            traces[0]["score_interval"] = {"lower": 84.0}
            write_jsonl(root / "stagecourt_traces.jsonl", traces)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="meaningful",
            )

            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )

        self.assertEqual(stage_rows[0]["stage_scope"], "CENSUS_EVENT_BOARD")
        self.assertEqual(audit["verdict"], "PENDING_PRODUCTION_FULL_THESIS")
        self.assertIn("missing_verified_score_interval_upper", audit["blocked_candidates"][0]["blockers"])

    def test_official_only_complete_trace_can_be_full_thesis_candidate_without_brain_web_partial(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            for row in accepted:
                row.pop("raw_assertion_id", None)
                row["brain_web_claim"] = False
                row["source_provider"] = "OpenDART"
                row["source_url"] = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260701999999"
            write_jsonl(root / "accepted_claims.jsonl", accepted)
            write_jsonl(root / "claim_extractor_runs.jsonl", [])
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="meaningful",
            )

            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )

        self.assertEqual(audit["candidate_row_count"], 1)
        self.assertEqual(audit["candidate_source_counts"], {"stagecourt_trace_direct_scan": 1})
        self.assertEqual(audit["promoted_full_thesis_row_count"], 1)
        self.assertEqual(stage_rows[0]["stage_scope"], "FULL_THESIS")
        self.assertEqual(stage_rows[0]["operator_stage_use"], "FULL_THESIS_STAGE")
        self.assertEqual(stage_rows[0]["full_thesis_primary_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(stage_rows[0]["canonical_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(stage_rows[0]["archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(audit["blocked_candidates"], [])
        self.assertIn("separate Brain/Web evidence gate", audit["rule"])

    def test_production_full_thesis_writes_matching_claim_to_stage_trace(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="full_thesis",
            )

            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            trace_rows = {item["trace_id"]: item for item in _read_jsonl(root / "claim_to_stage_trace.jsonl")}
            row = stage_rows[0]
            trace = trace_rows[row["claim_to_stage_trace_id"]]
            forensic = _claim_to_stage_forensic_audit(output_root=root, stage_rows=stage_rows)

        self.assertEqual(audit["promoted_full_thesis_row_count"], 1)
        self.assertTrue(row["claim_to_stage_trace_id"].startswith("CSTTRACE-FTPROD-"))
        self.assertEqual(set(row["accepted_claim_ids"]), set(trace["accepted_claim_ids"]))
        self.assertEqual(set(row["score_contribution_ids"]), set(trace["score_contribution_ids"]))
        self.assertEqual(set(row["full_thesis_stagecourt_trace_ids"]), set(trace["stagecourt_trace_ids"]))
        self.assertEqual(forensic["critical_counts"]["claim_to_stage_claim_set_mismatch_count"], 0)
        self.assertEqual(forensic["critical_counts"]["claim_to_stage_score_contribution_set_mismatch_count"], 0)
        self.assertEqual(forensic["critical_counts"]["claim_to_stage_stagecourt_set_mismatch_count"], 0)

    def test_green_stage_with_green_gap_is_downgraded_before_full_thesis_promotion(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_full_thesis_fixture(root)
            traces = _read_jsonl(root / "stagecourt_traces.jsonl")
            traces[0]["base_stage"] = "Stage3-Green"
            traces[0]["primitive_state_ids"] = [
                item for item in traces[0]["primitive_state_ids"] if item != "PRIM-3"
            ]
            write_jsonl(root / "stagecourt_traces.jsonl", traces)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="full_thesis",
            )

            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "base_stage": "Stage1",
                        "canonical_stage": "1",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "score_scale": "NO_SCORE",
                        "score_scope": "NO_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    }
                ],
            )
            production = _full_thesis_production_audit(config=config, stage_rows=stage_rows)

        self.assertEqual(audit["promoted_full_thesis_row_count"], 1)
        self.assertEqual(stage_rows[0]["full_thesis_source_stage"], "Stage3-Green")
        self.assertEqual(stage_rows[0]["full_thesis_stage"], "Stage3-Yellow")
        self.assertEqual(stage_rows[0]["canonical_stage"], "3-Yellow")
        self.assertTrue(stage_rows[0]["full_thesis_green_stage_downgraded_by_gap"])
        self.assertEqual(stage_rows[0]["full_thesis_missing_primitives"], [])
        self.assertIn("hbm_capacity_constraint", stage_rows[0]["full_thesis_green_gap_primitives"])
        self.assertEqual(production["production_green_stage_row_with_green_gap_count"], 0)
        self.assertEqual(
            production["blockers"],
            ["production_full_thesis_rows_with_required_positive_missing_primitives"],
        )

    def test_provider_failed_non_claim_task_does_not_block_brain_stage_promotion(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            executions = _read_jsonl(root / "source_task_executions.jsonl")
            executions.append(
                {
                    "task_id": "TASK-IR-PENDING",
                    "source_origin": "research_brain_v4_attempt",
                    "status": "PROVIDER_FAILED",
                    "accepted_claim_ids": [],
                    "fetched_document_ids": [],
                    "stop_reason": "live_official_no_fetchable_document",
                }
            )
            write_jsonl(root / "source_task_executions.jsonl", executions)

            audit = _brain_stage_promotion_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_source_acquisition="live_official_first",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={"real_provider_success_count": 1, "source_task_execution_count": 2, "accepted_claim_count": 1},
                stage_rows=[],
            )

        self.assertEqual(audit["verdict"], "ELIGIBLE_NOT_PROMOTED")
        self.assertEqual(audit["brain_source_task_without_document_ref_count"], 0)
        self.assertNotIn("Brain source task rows missing fetched document refs: 1", audit["blockers"])

    def test_full_thesis_refresh_queue_without_stagecourt_trace_is_explicitly_unmaterialized(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_source_acquisition="live_official_first",
                brain_stage_promotion_mode="strict",
                target_gate="full_thesis",
            )
            stage_rows, audit = _apply_production_full_thesis_from_brain(
                config=config,
                output_root=root,
                stage_rows=[
                    {
                        "symbol": "005930",
                        "company_name": "삼성전자",
                        "as_of_date": "2026-07-01",
                        "base_stage": "Stage2-Watch",
                        "canonical_stage": "2",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "stage_signal": "MATERIAL_CLAIM_WATCH",
                        "stage_decision_status": "PENDING_MATERIAL_GAPS",
                        "operator_stage_use": "NOT_FULL_THESIS_STAGE",
                        "score_scale": "EVENT_WEIGHTED_PARTIAL",
                        "score_scope": "EVENT_WEIGHTED_PARTIAL",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                        "full_thesis_missing_primitives": ["full_thesis_refresh_task_not_run"],
                    }
                ],
            )

        self.assertEqual(stage_rows[0]["stage_scope"], "CENSUS_EVENT_BOARD")
        self.assertEqual(audit["verdict"], "PENDING_PRODUCTION_FULL_THESIS")
        self.assertEqual(audit["full_thesis_refresh_queue_candidate_count"], 1)
        self.assertEqual(audit["candidate_row_count"], 0)
        self.assertEqual(audit["candidate_source_counts"], {})
        self.assertEqual(audit["refresh_queue_materialized_candidate_count"], 0)
        self.assertEqual(audit["refresh_queue_unmaterialized_candidate_count"], 1)
        self.assertEqual(audit["refresh_queue_unmaterialized_sample"][0]["symbol"], "005930")
        self.assertEqual(
            audit["refresh_queue_unmaterialized_sample"][0]["materialization_blocker"],
            "full_thesis_refresh_task_has_no_research_brain_stagecourt_trace",
        )
        self.assertIn("full_thesis_refresh_queue_has_no_brain_stagecourt_trace_candidates", audit["blockers"])

    def test_brain_partial_stage_without_atomic_id_uses_stage_primitive_chain(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_live_brain_promotion_fixture(root)
            write_jsonl(
                root / "census_stage_status.jsonl",
                [
                    {
                        "symbol": "005930",
                        "stage_scope": "BRAIN_WEB_PARTIAL",
                        "accepted_claim_ids": ["CLM-A"],
                        "score_contribution_ids": ["SCON-A"],
                        "primitive_state_ids": ["PRIM-A"],
                        "atomic_stage_decision_id": None,
                    }
                ],
            )

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "PASS")
        self.assertEqual(audit["critical_counts"]["atomic_decision_primitive_set_mismatch_count"], 0)

    def test_max_iterations_feeds_full_thesis_follow_up_seed_to_second_brain_attempt(self):
        calls = []

        def fake_brain_attempt(*, config, output_root, full_thesis_seed_path, full_thesis_seed_event_count, full_thesis_seed_source, full_thesis_seed_original_path):
            calls.append(
                {
                    "seed_path": str(full_thesis_seed_path),
                    "seed_event_count": full_thesis_seed_event_count,
                    "seed_source": full_thesis_seed_source,
                    "seed_original_path": full_thesis_seed_original_path,
                }
            )
            if len(calls) == 1:
                _write_live_brain_promotion_fixture(output_root)
            return {
                "schema_version": "e2r_census_v4_brain_web_attempt_audit_v1",
                "attempt_mode": "research_brain_v4_production_shadow_attempt",
                "verdict": "ATTEMPTED_NOT_CUTOVER_READY",
                "full_thesis_seed_event_path": str(full_thesis_seed_path),
                "full_thesis_seed_source": full_thesis_seed_source,
                "full_thesis_seed_original_path": full_thesis_seed_original_path,
                "full_thesis_seed_event_count": full_thesis_seed_event_count,
                "full_thesis_seed_consumed_by_research_brain": True,
                "full_thesis_seed_planner_attempted_event_count": full_thesis_seed_event_count,
                "full_thesis_seed_planner_run_row_count": full_thesis_seed_event_count,
                "full_thesis_seed_planner_run_count": full_thesis_seed_event_count,
                "full_thesis_seed_real_provider_success_count": full_thesis_seed_event_count,
                "full_thesis_seed_source_task_execution_count": 1,
                "full_thesis_seed_accepted_claim_count": 1,
                "full_thesis_seed_stagecourt_trace_count": 1,
                "full_thesis_seed_materialized_to_stagecourt": True,
                "planner_provider": config.brain_planner_provider,
                "source_acquisition": config.brain_source_acquisition,
                "planner_run_count": max(1, full_thesis_seed_event_count),
                "real_provider_success_count": 1,
                "source_task_execution_count": 1,
                "real_document_fetched_count": 1,
                "unique_real_document_fetched_count": 1,
                "accepted_claim_count": 1,
                "unique_accepted_claim_count": 1,
                "brain_to_census_claim_exported_count": 1,
                "brain_stagecourt_trace_exported_count": 1,
                "brain_to_census_stage_exported_count": 0,
                "brain_source_task_exported_count": 1,
                "brain_source_task_execution_exported_count": 1,
                "brain_evidence_document_exported_count": 1,
                "brain_evidence_anchor_exported_count": 1,
                "brain_score_contribution_exported_count": 1,
                "brain_to_claim_trace_count": 1,
                "brain_raw_assertion_exported_count": 1,
                "claim_acceptance_ready": True,
                "stagecourt_trace_ready": True,
                "cutover_export_ready": False,
                "blockers": ["Research Brain StageCourt traces are not promoted into census_stage_status rows"],
            }

        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            with patch("e2r.census.census_runner_v4._run_brain_web_attempt", side_effect=fake_brain_attempt):
                run_census_mode_v4(
                    CensusV4RunConfig(
                        as_of_date="2026-07-01",
                        output_root=str(output_root),
                        v3_output_root="output/census_v3/2026-07-01",
                        run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                        brain_web_mode="enabled",
                        brain_planner_provider="real",
                        brain_source_acquisition="live_official_first",
                        brain_stage_promotion_mode="strict",
                        max_iterations=2,
                        fail_on_critical_audit=False,
                        write_operational_docs=False,
                    )
                )
            audit = read_json(output_root / "full_thesis_follow_up_iterations_audit.json")
            trace = _read_jsonl(output_root / "full_thesis_seed_materialization_trace.jsonl")

        self.assertEqual(len(calls), 2)
        self.assertEqual(audit["follow_up_iteration_count"], 1)
        self.assertEqual(audit["iterations"][1]["seed_event_count"], 4)
        self.assertIn("full_thesis_follow_up_iteration_2_seed_events.jsonl", calls[1]["seed_path"])
        iteration_seed_paths = {row["seed_source_path"] for row in trace if str(row.get("seed_source_path") or "").endswith("full_thesis_follow_up_iteration_2_seed_events.jsonl")}
        self.assertEqual(len(iteration_seed_paths), 1)


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _assert_no_forbidden_brain_payload_keys(value) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            lowered = str(key).lower()
            assert "score" not in lowered
            assert "stage" not in lowered
            assert lowered != "current_score_eligible"
            _assert_no_forbidden_brain_payload_keys(item)
        return
    if isinstance(value, (list, tuple)):
        for item in value:
            _assert_no_forbidden_brain_payload_keys(item)


def _write_live_brain_promotion_fixture(root: Path) -> None:
    write_jsonl(root / "planner_runs.jsonl", [{"provider_mode": "real", "real_provider_success": True}])
    write_jsonl(
        root / "claim_extractor_runs.jsonl",
        [
            {
                "provider_mode": "llm",
                "provider_name": "codex_cli_contract_blind_extractor",
                "raw_assertion_ids": ["RAWLLM-A"],
            }
        ],
    )
    write_jsonl(
        root / "source_task_executions.jsonl",
        [
            {
                "task_id": "TASK-A",
                "source_origin": "research_brain_v4_attempt",
                "fetched_document_ids": ["DOC-A"],
                "accepted_claim_ids": ["CLM-A"],
            }
        ],
    )
    write_jsonl(root / "evidence_documents.jsonl", [{"document_id": "DOC-A", "source_origin": "research_brain_v4_attempt", "canonical_url": "https://example.com/doc"}])
    write_jsonl(root / "evidence_anchors.jsonl", [{"anchor_id": "ANCH-A", "document_id": "DOC-A", "source_origin": "research_brain_v4_attempt"}])
    write_jsonl(
        root / "accepted_claims.jsonl",
        [
            {
                "claim_id": "CLM-A",
                "brain_web_claim": True,
                "source_origin": "research_brain_v4_attempt",
                "document_id": "DOC-A",
                "anchor_id": "ANCH-A",
                "event_date": "2026-06-30",
                "target_scope_status": "DIRECT",
                "temporal_status": "CURRENT",
                "score_eligible": True,
                "primitive_id": "named_customer_or_customer_quality",
                "mapping_status": "ACCEPTED",
                "support_direction": "SUPPORT",
                "raw_assertion_id": "RAWLLM-A",
            }
        ],
    )
    write_jsonl(
        root / "primitive_states.jsonl",
        [
            {
                "primitive_state_id": "PRIM-A",
                "source_origin": "research_brain_v4_attempt",
                "primitive_id": "named_customer_or_customer_quality",
                "support_claim_ids": ["CLM-A"],
                "counter_claim_ids": [],
            }
        ],
    )
    write_jsonl(
        root / "primitive_mappings.jsonl",
        [
            {
                "mapping_id": "MAP-A",
                "source_origin": "research_brain_v4_attempt",
                "accepted_claim_ids": ["CLM-A"],
                "primitive_state_ids": ["PRIM-A"],
                "score_contribution_ids": ["SCON-A"],
                "primitive_ids": ["named_customer_or_customer_quality"],
            }
        ],
    )
    write_jsonl(
        root / "score_contributions.jsonl",
        [
            {
                "score_contribution_id": "SCON-A",
                "source_origin": "research_brain_v4_attempt",
                "support_claim_ids": ["CLM-A"],
                "mapping_ids": ["MAP-A"],
            }
        ],
    )
    write_jsonl(
        root / "brain_to_claim_trace.jsonl",
        [
            {
                "accepted_claim_id": "CLM-A",
                "score_contribution_id": "SCON-A",
                "primitive_state_ids": ["PRIM-A"],
                "stagecourt_trace_id": "SCT-BRAIN-A",
            }
        ],
    )
    write_jsonl(
        root / "brain_claim_mapping_trace.jsonl",
        [
            {
                "brain_claim_mapping_trace_id": "BRAINMAP-A",
                "claim_id": "CLM-A",
                "accepted": True,
                "score_eligible": True,
                "symbol": "005930",
                "mapping_id": "MAP-A",
                "mapping_status": "ACCEPTED",
                "primitive_id": "named_customer_or_customer_quality",
                "support_direction": "SUPPORT",
                "primitive_state_ids": ["PRIM-A"],
                "score_contribution_ids": ["SCON-A"],
                "stagecourt_trace_id": "SCT-BRAIN-A",
                "source_origin": "research_brain_v4_attempt",
            }
        ],
    )
    write_jsonl(
        root / "stagecourt_traces.jsonl",
        [
            {
                "stagecourt_trace_id": "SCT-BRAIN-A",
                "trace_id": "SCT-BRAIN-A",
                "symbol": "005930",
                "candidate_event_id": "CE-BRAIN-A",
                "source_origin": "research_brain_v4_attempt",
                "primary_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "accepted_claim_ids": ["CLM-A"],
                "score_contribution_ids": ["SCON-A"],
                "primitive_state_ids": ["PRIM-A"],
                "score_interval": {"lower": 77.5, "upper": 82.0},
                "score_status": "PENDING_MATERIAL_GAPS",
                "base_stage": "Stage2-Watch",
                "transition_overlay": "NONE",
                "investigation_status": "PENDING",
                "missing_green_primitives": ["cash_or_revision_conversion"],
                "missing_yellow_primitives": [],
                "not_promoted_to_census_stage_status": True,
            }
        ],
    )


def _write_live_brain_full_thesis_fixture(root: Path) -> None:
    primitives = [
        "customer_preorder_or_allocation",
        "revenue_visibility_contract",
        "hbm_capacity_constraint",
        "hbm_capacity_pre_sold",
    ]
    write_jsonl(root / "planner_runs.jsonl", [{"provider_mode": "real", "real_provider_success": True}])
    write_jsonl(
        root / "claim_extractor_runs.jsonl",
        [
            {
                "provider_mode": "llm",
                "provider_name": "codex_cli_contract_blind_extractor",
                "raw_assertion_ids": [f"RAWLLM-{idx}" for idx, _ in enumerate(primitives, 1)],
            }
        ],
    )
    write_jsonl(
        root / "source_task_executions.jsonl",
        [
            {
                "task_id": f"TASK-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "candidate_event_id": "CE-BRAIN-FULL",
                "fetched_document_ids": [f"DOC-{idx}"],
                "accepted_claim_ids": [f"CLM-{idx}"],
            }
            for idx, _ in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "evidence_documents.jsonl",
        [
            {
                "document_id": f"DOC-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "canonical_url": f"https://example.com/full-thesis-{idx}",
            }
            for idx, _ in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "evidence_anchors.jsonl",
        [
            {
                "anchor_id": f"ANCH-{idx}",
                "document_id": f"DOC-{idx}",
                "source_origin": "research_brain_v4_attempt",
            }
            for idx, _ in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "accepted_claims.jsonl",
        [
            {
                "claim_id": f"CLM-{idx}",
                "brain_web_claim": True,
                "source_origin": "research_brain_v4_attempt",
                "document_id": f"DOC-{idx}",
                "anchor_id": f"ANCH-{idx}",
                "event_date": "2026-06-30",
                "target_scope_status": "DIRECT",
                "temporal_status": "CURRENT",
                "score_eligible": True,
                "primitive_id": primitive,
                "mapping_status": "ACCEPTED",
                "support_direction": "SUPPORT",
                "raw_assertion_id": f"RAWLLM-{idx}",
            }
            for idx, primitive in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "primitive_states.jsonl",
        [
            {
                "primitive_state_id": f"PRIM-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "primitive_id": primitive,
                "support_claim_ids": [f"CLM-{idx}"],
                "counter_claim_ids": [],
            }
            for idx, primitive in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "primitive_mappings.jsonl",
        [
            {
                "mapping_id": f"MAP-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "accepted_claim_ids": [f"CLM-{idx}"],
                "primitive_state_ids": [f"PRIM-{idx}"],
                "score_contribution_ids": [f"SCON-{idx}"],
                "primitive_ids": [primitive],
            }
            for idx, primitive in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "score_contributions.jsonl",
        [
            {
                "score_contribution_id": f"SCON-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "support_claim_ids": [f"CLM-{idx}"],
                "mapping_ids": [f"MAP-{idx}"],
                "raw_points": 21.0,
            }
            for idx, _ in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "brain_to_claim_trace.jsonl",
        [
            {
                "accepted_claim_id": f"CLM-{idx}",
                "score_contribution_id": f"SCON-{idx}",
                "primitive_state_ids": [f"PRIM-{idx}"],
                "stagecourt_trace_id": "SCT-BRAIN-FULL",
            }
            for idx, _ in enumerate(primitives, 1)
        ],
    )
    write_jsonl(
        root / "stagecourt_traces.jsonl",
        [
            {
                "stagecourt_trace_id": "SCT-BRAIN-FULL",
                "trace_id": "SCT-BRAIN-FULL",
                "symbol": "005930",
                "candidate_event_id": "CE-BRAIN-FULL",
                "source_origin": "research_brain_v4_attempt",
                "primary_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "accepted_claim_ids": [f"CLM-{idx}" for idx, _ in enumerate(primitives, 1)],
                "score_contribution_ids": [f"SCON-{idx}" for idx, _ in enumerate(primitives, 1)],
                "primitive_state_ids": [f"PRIM-{idx}" for idx, _ in enumerate(primitives, 1)],
                "score_interval": {"lower": 84.0, "upper": 84.0},
                "score_status": "FINAL",
                "base_stage": "Stage3-Yellow",
                "transition_overlay": "NONE",
                "investigation_status": "COMPLETE",
                "missing_green_primitives": [],
                "missing_yellow_primitives": [],
                "not_promoted_to_census_stage_status": True,
            }
        ],
    )


if __name__ == "__main__":
    unittest.main()
