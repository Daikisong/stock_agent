from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from e2r.production.metadata import stable_hash
from e2r.production.v6_current_krx_census import (
    CURRENT_KRX_CENSUS_FAIL,
    CURRENT_KRX_CENSUS_TEST_PASS,
    compile_current_krx_census_cutover,
)
from e2r.research_brain.runtime.live_materialization import (
    LiveDepthDecision,
    LiveUniverseRow,
    TriggerSignal,
)
from e2r.research_brain.researcher_mode.tracked_receipts import VERIFICATION_PASS


class E2RV6CurrentKrxCensusTests(unittest.TestCase):
    AS_OF = "2026-08-09"
    EFFECTIVE = "2026-08-07"
    TARGET = "123456"

    def _write_json(self, path: Path, payload: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def _write_jsonl(self, path: Path, rows: list[dict[str, object]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "".join(
                json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                for row in rows
            ),
            encoding="utf-8",
        )

    def _fixture(self, root: Path, *, stage: str = "2") -> tuple[Path, Path]:
        live = root / "live"
        receipts = root / "receipts"
        live.mkdir(parents=True)
        receipts.mkdir(parents=True)
        source_hash = hashlib.sha256(b"current krx").hexdigest()
        universe = LiveUniverseRow(
            symbol=self.TARGET,
            company_name="현재검증기업",
            market="KOSPI",
            security_group="STOCK",
            stock_certificate_type="COMMON",
            sector_type="GENERAL",
            listing_date="2020-01-01",
            listing_status="LISTED",
            source_effective_date=self.EFFECTIVE,
            source_url=(
                "https://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info"
            ),
            source_document_id="KRXDOC-CURRENT",
            source_content_hash=source_hash,
            source_request_id="KRXREQ-CURRENT",
            source_mode="LIVE",
            eligible=True,
            exclusion_reason=None,
            raw_fields={"ISU_SRT_CD": self.TARGET},
        )
        self._write_jsonl(live / "universe_eligible.jsonl", [universe.to_dict()])
        self._write_jsonl(live / "universe_raw.jsonl", [universe.to_dict()])
        self._write_jsonl(live / "universe_excluded.jsonl", [])
        universe_payload = [universe.to_dict()]
        self._write_json(
            live / "universe_provenance.json",
            {
                "schema_version": "e2r_live_krx_universe_provenance_v1",
                "status": "CURRENT_UNIVERSE_MATERIALIZATION_PASS",
                "as_of_date": self.AS_OF,
                "source_effective_date": self.EFFECTIVE,
                "raw_universe_hash": stable_hash(universe_payload),
                "eligible_universe_hash": stable_hash(universe_payload),
                "request_attempts": [
                    {
                        "market": "KOSPI",
                        "effective_date": self.EFFECTIVE,
                        "status": "FETCHED",
                        "row_count": 1,
                        "fetched_at": "2026-08-09T00:10:00+00:00",
                    }
                ],
            },
        )

        trigger_rows: list[dict[str, object]] = []
        trigger_ids: list[str] = []
        for index, trigger_type in enumerate(("OFFICIAL", "MARKET", "RISK")):
            payload = {"index": index, "trigger_type": trigger_type}
            trigger_id = "TRIG-" + stable_hash(
                {
                    "target": self.TARGET,
                    "source_event": f"EVENT-{index}",
                    "effective_date": self.EFFECTIVE,
                    "trigger_type": trigger_type,
                    "lifecycle_status": "OPEN",
                    "providers": ("KRX",),
                    "payload": payload,
                }
            )[:24]
            signal = TriggerSignal(
                trigger_signal_id=trigger_id,
                target_id=self.TARGET,
                target_name="현재검증기업",
                trigger_type=trigger_type,
                source_event_id=f"EVENT-{index}",
                effective_date=self.EFFECTIVE,
                detected_at=self.AS_OF,
                source_refs=(f"SRC-{index}",),
                provider_names=("KRX",),
                subject_direct=True,
                lifecycle_status="OPEN",
                investigation_required=True,
                score_evidence_eligible=False,
                headline_or_snippet_only=False,
                payload=payload,
            )
            trigger_ids.append(trigger_id)
            trigger_rows.append(signal.to_dict())
        self._write_jsonl(live / "trigger_signals.jsonl", trigger_rows)
        self._write_jsonl(live / "candidate_events.jsonl", [])
        decision = LiveDepthDecision(
            depth_decision_id="DEPTH-CURRENT",
            target_id=self.TARGET,
            target_name="현재검증기업",
            as_of_date=self.AS_OF,
            completed_depths=(
                "L0_UNIVERSE",
                "L1_BASELINE",
                "L2_OFFICIAL_LIGHT",
                "L3_RESEARCH_BRAIN",
            ),
            maximum_depth="L3_RESEARCH_BRAIN",
            candidate_event_id="CAND-CURRENT",
            trigger_signal_ids=tuple(trigger_ids),
            priority_score=10.0,
            selected_for_official_light=True,
            selected_for_deep=True,
            selected_for_brain=True,
            acquisition_eligible=True,
            selection_reasons=("current source-backed trigger",),
            not_selected_reason=None,
            source_task_budget={"max_source_tasks": 8, "max_fetches": 12},
            llm_budget={"max_llm_calls": 3, "max_retries": 3},
            general_web_budget={"max_general_web_fetches": 3},
        )
        self._write_jsonl(live / "depth_decisions.jsonl", [decision.to_dict()])

        empty_jsonl = (
            "baseline_lanes.jsonl",
            "planner_runs.jsonl",
            "llm_prompts.jsonl",
            "llm_responses.jsonl",
            "question_source_tasks.jsonl",
            "provider_requests.jsonl",
            "provider_fetch_results.jsonl",
            "source_task_satisfaction.jsonl",
            "current_claim_ledger.jsonl",
            "gap_closure_status.jsonl",
            "primitive_states.jsonl",
            "atomic_stage_decisions.jsonl",
        )
        for name in empty_jsonl:
            self._write_jsonl(live / name, [])
        self._write_jsonl(
            live / "source_tasks.jsonl",
            [{"task_id": "TASK-CURRENT", "target_id": self.TARGET}],
        )
        self._write_jsonl(
            live / "evidence_documents.jsonl",
            [{"document_id": "DOC-CURRENT", "target_id": self.TARGET}],
        )
        self._write_jsonl(
            live / "adjudicated_claims.jsonl",
            [
                {
                    "claim_id": "CLAIM-CURRENT",
                    "target_id": self.TARGET,
                    "investigation_status": "ACCEPTED",
                }
            ],
        )
        audit_contracts = {
            "universe_audit.json": ("e2r_live_universe_audit_v1", None),
            "baseline_lane_audit.json": (
                "e2r_live_baseline_lane_audit_v1",
                "CURRENT_BASELINE_LANES_PASS",
            ),
            "trigger_fusion_audit.json": (
                "e2r_live_trigger_fusion_audit_v1",
                "CURRENT_TRIGGER_FUSION_PASS",
            ),
            "candidate_selection_audit.json": (
                "e2r_live_depth_selection_audit_v1",
                "CURRENT_DEPTH_SELECTION_PASS",
            ),
            "planner_validation.json": (
                "e2r_live_brain_planner_audit_v1",
                "CURRENT_BRAIN_PLANNER_PASS",
            ),
            "source_task_audit.json": (
                "e2r_live_source_task_audit_v1",
                "CURRENT_SOURCE_TASK_PASS",
            ),
            "provider_call_report.json": (
                "e2r_live_source_acquisition_audit_v1",
                "CURRENT_SOURCE_ACQUISITION_PASS",
            ),
            "claim_compiler_audit.json": (
                "e2r_live_current_claim_audit_v1",
                "CURRENT_CLAIM_COMPILER_PASS",
            ),
            "adaptive_gap_audit.json": (
                "e2r_live_adaptive_gap_audit_v1",
                "ADAPTIVE_GAP_CLOSURE_PASS",
            ),
            "atomic_score_audit.json": (
                "e2r_live_current_atomic_score_audit_v1",
                "CURRENT_ATOMIC_DECISION_PASS",
            ),
        }
        for name, (schema, status) in audit_contracts.items():
            payload = {
                "schema_version": schema,
                "as_of_date": self.AS_OF,
                "critical_count_sum": 0,
                "hard_acceptance_pass": True,
            }
            if status is not None:
                payload["status"] = status
            if name == "universe_audit.json":
                payload.update(
                    {
                        "source_effective_date": self.EFFECTIVE,
                        "raw_universe_count": 1,
                        "eligible_universe_count": 1,
                        "excluded_universe_count": 0,
                        "duplicate_eligible_symbol_count": 0,
                        "missing_symbol_count": 0,
                        "provider_request_count": 1,
                    }
                )
            self._write_json(
                live / name,
                payload,
            )

        target = receipts / self.TARGET
        target.mkdir()
        self._write_json(
            target / "receipt_manifest.json",
            {
                "receipt_id": "RECEIPT-CURRENT",
                "target_id": self.TARGET,
                "as_of_date": self.AS_OF,
            },
        )
        self._write_json(
            target / "score_receipt.json",
            {
                "target_id": self.TARGET,
                "score_valid": True,
                "research_complete": True,
                "semantic_saturation_certified": True,
                "material_gap_count": 0,
                "provider_error_count": 0,
                "total_score": 61.0,
                "component_score_vector": {"component": 61.0},
                "canonical_stage": stage,
            },
        )
        self._write_json(
            target / "stagecourt_receipt.json",
            {
                "target_id": self.TARGET,
                "decision_status": "FINAL",
                "score_valid": True,
                "canonical_stage": stage,
            },
        )
        self._write_jsonl(
            target / "scoring_facts.jsonl",
            [
                {
                    "fact_id": "FACT-CURRENT",
                    "source_tier": "ISSUER_OFFICIAL",
                    "quote_excerpt": "현재 공식 원문에 결박된 점수 fact",
                }
            ],
        )
        self._write_jsonl(
            target / "provider_calls.jsonl",
            [{"provider_call_id": "CALL-CURRENT", "status": "SUCCESS"}],
        )
        return live, receipts

    @staticmethod
    def _verification(path: str | Path) -> dict[str, object]:
        return {
            "target_id": Path(path).name,
            "status": VERIFICATION_PASS,
            "critical_count": 0,
        }

    def _compile(
        self,
        live: Path,
        receipts: Path,
        *,
        selection_candidates: tuple[dict[str, object], ...] | None = None,
    ) -> tuple[dict[str, object], tuple[dict[str, object], ...]]:
        candidate = {"target_id": self.TARGET}
        candidates = (
            (candidate,)
            if selection_candidates is None
            else selection_candidates
        )
        with patch(
            "e2r.production.v6_current_krx_census.load_current_live_selection_inputs",
            return_value=(candidates, ()),
        ):
            summary, rows = compile_current_krx_census_cutover(
                assessment_as_of_date=self.AS_OF,
                live_root=live,
                deep_receipt_root=receipts,
                receipt_verifier=self._verification,
                test_mode=True,
                execution_date_kst=self.AS_OF,
            )
        return dict(summary), tuple(dict(row) for row in rows)

    def test_selected_depth_without_complete_planner_cannot_inflate_natural_count(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            live, receipts = self._fixture(Path(tmp))
            summary, _rows = self._compile(
                live,
                receipts,
                selection_candidates=(),
            )

        self.assertEqual(summary["natural_candidate_count"], 0)
        self.assertEqual(summary["natural_l5_completed_count"], 0)
        self.assertEqual(
            summary["critical_counts"]["natural_candidate_missing_count"],
            1,
        )
        self.assertFalse(summary["production_runtime_ready"])

    def test_natural_l5_verified_receipt_contract_passes_without_production_claim(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            live, receipts = self._fixture(Path(tmp))
            summary, rows = self._compile(live, receipts)

        self.assertEqual(summary["status"], CURRENT_KRX_CENSUS_TEST_PASS)
        self.assertFalse(summary["production_runtime_ready"])
        self.assertEqual(summary["natural_trigger_lane_count"], 3)
        self.assertEqual(summary["natural_l5_completed_count"], 1)
        self.assertEqual(summary["score_valid_deep_row_count"], 1)
        self.assertEqual(summary["nonzero_score_contribution_count"], 1)
        self.assertEqual(summary["execution_date_kst"], self.AS_OF)
        self.assertEqual(
            summary["source_available_at"], "2026-08-09T00:10:00+00:00"
        )
        self.assertEqual(rows[0]["maximum_depth"], "L5")
        self.assertEqual(rows[0]["current_score"], 61.0)
        self.assertEqual(rows[0]["canonical_stage"], "2")

    def test_l5_zero_and_all_pending_cannot_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            live, receipts = self._fixture(Path(tmp))
            for child in receipts.iterdir():
                for leaf in child.iterdir():
                    leaf.unlink()
                child.rmdir()
            summary, rows = self._compile(live, receipts)

        self.assertEqual(summary["status"], CURRENT_KRX_CENSUS_FAIL)
        self.assertGreater(summary["critical_counts"]["l5_completed_missing_count"], 0)
        self.assertGreater(
            summary["critical_counts"]["score_valid_deep_row_missing_count"], 0
        )
        self.assertEqual(rows[0]["current_score_status"], "RESEARCH_IN_PROGRESS")
        self.assertIsNone(rows[0]["current_score"])

    def test_provider_failure_and_snippet_scoring_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            live, receipts = self._fixture(Path(tmp))
            target = receipts / self.TARGET
            self._write_jsonl(
                target / "provider_calls.jsonl",
                [{"provider_call_id": "CALL-CURRENT", "status": "PROVIDER_ERROR"}],
            )
            self._write_jsonl(
                target / "scoring_facts.jsonl",
                [
                    {
                        "fact_id": "FACT-CURRENT",
                        "source_tier": "SEARCH_SNIPPET",
                        "quote_excerpt": "snippet",
                        "headline_or_snippet_only": True,
                    }
                ],
            )
            summary, _ = self._compile(live, receipts)

        self.assertEqual(summary["status"], CURRENT_KRX_CENSUS_FAIL)
        self.assertEqual(
            summary["critical_counts"]["provider_failed_final_score_count"], 1
        )
        self.assertEqual(summary["critical_counts"]["snippet_score_count"], 1)

    def test_all_stage_zero_cannot_claim_census_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            live, receipts = self._fixture(Path(tmp), stage="0")
            summary, _ = self._compile(live, receipts)

        self.assertEqual(summary["status"], CURRENT_KRX_CENSUS_FAIL)
        self.assertEqual(
            summary["critical_counts"]["all_zero_or_all_pending_false_pass_count"],
            1,
        )

    def test_production_cannot_replace_receipt_verifier(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            live, receipts = self._fixture(Path(tmp))
            with self.assertRaisesRegex(ValueError, "cannot replace"):
                compile_current_krx_census_cutover(
                    assessment_as_of_date=self.AS_OF,
                    live_root=live,
                    deep_receipt_root=receipts,
                    receipt_verifier=self._verification,
                    test_mode=False,
                )

    def test_universe_partition_and_audit_schema_are_not_self_attested(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            live, receipts = self._fixture(Path(tmp))
            self._write_jsonl(live / "universe_raw.jsonl", [])
            self._write_json(
                live / "planner_validation.json",
                {
                    "schema_version": "placeholder",
                    "status": "CURRENT_BRAIN_PLANNER_PASS",
                    "as_of_date": self.AS_OF,
                    "critical_count_sum": 0,
                    "hard_acceptance_pass": True,
                },
            )
            summary, _ = self._compile(live, receipts)

        self.assertEqual(summary["status"], CURRENT_KRX_CENSUS_FAIL)
        self.assertGreater(summary["critical_count_sum"], 0)
        self.assertGreater(
            summary["critical_counts"]["live_stage_audit_failure_count"], 0
        )


if __name__ == "__main__":
    unittest.main()
