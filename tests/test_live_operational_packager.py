from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.runtime import (
    CurrentDeepOutcome,
    CurrentOperationRunnerConfig,
    CurrentOperationRunnerInput,
    CurrentTriggerSignal,
    CurrentTriggerType,
    DailyBaselineLane,
    DailyBaselineLaneStatus,
    DailyBaselineLaneType,
    DailyClaimProvenance,
    DailyDeepExecution,
    DailyProviderKind,
    DailySourceTaskRecord,
    DailyUniverseMember,
    run_current_daily_census,
)
from e2r.research_brain.runtime.live_materialization import (
    CurrentAtomicDecisionBuilder,
    LiveRunMode,
    package_live_current_operation,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


class LiveOperationalPackagerArtifactTest(unittest.TestCase):
    def test_phase32_audit_records_executed_but_pending_live_operation(self) -> None:
        audit = json.loads(
            (
                REPO_ROOT
                / "docs/operational/e2r_live_current_operation_audit.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(audit["official_cli_exit_code"], 0)
        self.assertGreater(audit["full_universe_count"], 1000)
        self.assertGreater(audit["actual_live_source_count"], 0)
        self.assertEqual(audit["evaluator_critical_count_sum"], 0)
        self.assertFalse(audit["production_runtime_ready"])
        self.assertTrue(audit["safety"]["actual_live_execution_performed"])
        self.assertFalse(audit["safety"]["claimless_nonzero_score"])


class LiveOperationalPackagerTests(unittest.TestCase):
    as_of_date = "2026-07-10"
    target_id = "005930"

    def test_claimless_result_stays_pending_without_hardcoded_ready(self) -> None:
        result, inputs, document = self._build_result(with_claim=False)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            live = root / "live"
            output = root / "output"
            manifest = root / "input.json"
            self._write_live_leaves(live, document=document)
            write_json(manifest, inputs.to_dict())

            paths = package_live_current_operation(
                result=result,
                live_root=live,
                input_manifest=manifest,
                output_root=output,
                run_mode=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
            )

            self.assertEqual(self._read_jsonl(paths["accepted_claims"]), [])
            self.assertEqual(self._read_jsonl(paths["claim_provenance"]), [])
            self.assertEqual(self._read_jsonl(paths["score_contributions"]), [])
            self.assertEqual(len(self._read_jsonl(paths["atomic_decisions"])), 1)
            envelope = self._read_json(paths["live_operational_envelope"])
            audit = self._read_json(paths["audit_summary"])
            self.assertFalse(envelope["production_runtime_ready"])
            self.assertIn(
                "NO_ACCEPTED_CURRENT_CLAIM", envelope["provider_blockers"]
            )
            self.assertEqual(envelope["actual_live_source_count"], 1)
            self.assertEqual(
                audit["status"],
                "LIVE_OPERATION_EXECUTED_PENDING_ACCEPTED_CURRENT_CLAIM",
            )
            self.assertEqual(audit["accepted_current_claim_count"], 0)
            self.assertFalse(audit["production_runtime_ready"])

    def test_result_claim_provenance_atomic_and_contribution_override_stale_live_leaves(
        self,
    ) -> None:
        result, inputs, document = self._build_result(with_claim=True)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            live = root / "live"
            output = root / "output"
            manifest = root / "input.json"
            self._write_live_leaves(live, document=document, stale_canonical=True)
            write_json(manifest, inputs.to_dict())

            paths = package_live_current_operation(
                result=result,
                live_root=live,
                input_manifest=manifest,
                output_root=output,
                run_mode=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
            )

            claims = self._read_jsonl(paths["accepted_claims"])
            provenance = self._read_jsonl(paths["claim_provenance"])
            decisions = self._read_jsonl(paths["atomic_decisions"])
            contributions = self._read_jsonl(paths["score_contributions"])
            primitive_states = self._read_jsonl(paths["primitive_states"])
            documents = self._read_jsonl(paths["evidence_documents"])
            anchors = self._read_jsonl(paths["evidence_anchors"])
            raw_assertions = self._read_jsonl(paths["raw_assertions"])
            adjudicated = self._read_jsonl(paths["adjudicated_claims"])
            satisfaction = self._read_jsonl(paths["source_task_executions"])
            self.assertEqual([row["claim_id"] for row in claims], ["CLM-LIVE"])
            self.assertEqual(
                [row["claim_id"] for row in provenance], ["CLM-LIVE"]
            )
            self.assertEqual(len(decisions), 1)
            self.assertEqual(decisions[0]["accepted_claim_ids"], ["CLM-LIVE"])
            self.assertEqual(len(contributions), 1)
            self.assertEqual(contributions[0]["support_claim_ids"], ["CLM-LIVE"])
            self.assertEqual(contributions[0]["target_id"], self.target_id)
            self.assertTrue(
                any(
                    row["primitive_id"] == "memory_price_increase_mentioned"
                    and row["state"] == "PRESENT_CURRENT"
                    for row in primitive_states
                )
            )
            self.assertNotIn(
                "STALE-CLAIM", {row["claim_id"] for row in claims}
            )
            document = next(
                row for row in documents if row["document_id"] == "DOC-LIVE"
            )
            self.assertEqual(document["content_hash"], provenance[0]["content_sha256"])
            self.assertEqual(
                hashlib.sha256(document["content_text"].encode("utf-8")).hexdigest(),
                provenance[0]["content_sha256"],
            )
            anchor = next(row for row in anchors if row["anchor_id"] == "ANCH-LIVE")
            self.assertEqual(anchor["document_id"], document["document_id"])
            self.assertEqual(anchor["content_hash"], document["content_hash"])
            adjudication = next(
                row for row in adjudicated if row["claim_id"] == "CLM-LIVE"
            )
            self.assertEqual(adjudication["source_document_id"], "DOC-LIVE")
            self.assertEqual(adjudication["source_anchor_id"], "ANCH-LIVE")
            self.assertIn(
                adjudication["raw_assertion_id"],
                {row["raw_assertion_id"] for row in raw_assertions},
            )
            task_execution = next(
                row
                for row in satisfaction
                if "CLM-LIVE" in row.get("accepted_claim_ids", [])
            )
            self.assertEqual(task_execution["status"], "DIRECT_TASK_SATISFIED")
            self.assertIn(
                task_execution.get("source_task_id"),
                {"SOURCE-TASK-LIVE", "QUESTION-LIVE"},
            )

            envelope = self._read_json(paths["live_operational_envelope"])
            audit = self._read_json(paths["audit_summary"])
            digest = paths["operator_digest"].read_text(encoding="utf-8")
            self.assertTrue(envelope["production_runtime_ready"])
            self.assertEqual(envelope["provider_blockers"], [])
            self.assertEqual(envelope["accepted_current_claim_count"], 1)
            self.assertEqual(envelope["actual_live_source_count"], 1)
            self.assertEqual(audit["status"], "LIVE_OPERATIONAL_BRAIN_READY")
            self.assertEqual(audit["claim_provenance_count"], 1)
            self.assertEqual(audit["score_contribution_count"], 1)
            self.assertEqual(
                audit["canonical_claim_chain_counts"]["evidence_documents"], 1
            )
            self.assertEqual(audit["operational_critical_count_sum"], 0)
            self.assertTrue(audit["production_runtime_ready"])
            self.assertIn("accepted current claims: 1", digest)
            self.assertIn("status: Operational Runtime Ready", digest)

    def _build_result(self, *, with_claim: bool):
        text = "삼성전자는 메모리 평균판매가격 상승을 공식 발표했다."
        content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        satisfaction = (
            {
                "source_task_id": "TASK-LIVE",
                "target_id": self.target_id,
                "primitive_id": "memory_price_increase_mentioned",
                "status": (
                    "DIRECT_TASK_SATISFIED" if with_claim else "SOURCE_EXHAUSTED"
                ),
                "original_gap_open": not with_claim,
                "accepted_claim_ids": ["CLM-LIVE"] if with_claim else [],
                "accepted_mapping_ids": ["MAP-LIVE"] if with_claim else [],
            },
            {
                "source_task_id": "TASK-GAP",
                "target_id": self.target_id,
                "primitive_id": "revenue_visibility_contract",
                "status": "SOURCE_EXHAUSTED",
                "original_gap_open": True,
                "accepted_claim_ids": [],
                "accepted_mapping_ids": [],
            },
        )
        bridge_provenance = (
            {
                "claim_id": "CLM-LIVE",
                "target_id": self.target_id,
                "available_date": "2026-04-30",
                "content_sha256": content_hash,
                "source_ids": ["FETCH-LIVE", "issuer-newsroom:live"],
                "anchor_ids": ["ANCH-LIVE"],
                "mapping_ids": ["MAP-LIVE"],
                "directness": "DIRECT",
                "temporal_status": "CURRENT",
                "mapping_status": "ACCEPTED",
                "fetched": True,
                "anchor_verified": True,
                "source_proxy_only": False,
            },
        ) if with_claim else ()
        accepted = (
            {
                "claim_id": "CLM-LIVE",
                "target_id": self.target_id,
                "accepted": True,
                "directness": "DIRECT",
                "temporal_status": "CURRENT",
                "semantic_status": "PASS",
                "mapping_ids": ["MAP-LIVE"],
            },
        ) if with_claim else ()
        atomic = CurrentAtomicDecisionBuilder().build(
            as_of_date=self.as_of_date,
            source_task_satisfaction=satisfaction,
            gap_status_rows=(
                {
                    "source_task_id": "TASK-GAP",
                    "terminal_status": "SOURCE_PENDING",
                },
            ),
            accepted_current_claims=accepted,
            claim_provenance=bridge_provenance,
        )
        decision = atomic.decisions[0]
        claim_provenance = ()
        if with_claim:
            claim_provenance = (
                DailyClaimProvenance(
                    provenance_id="PROV-LIVE",
                    claim_id="CLM-LIVE",
                    target_id=self.target_id,
                    document_id="DOC-LIVE",
                    source_url=(
                        "https://news.samsung.com/global/"
                        "samsung-electronics-announces-first-quarter-2026-results"
                    ),
                    published_date="2026-04-30",
                    available_date="2026-04-30",
                    content_sha256=content_hash,
                    document_text=text,
                    exact_quote=text,
                    source_ids=atomic.claims[0].source_ids,
                    anchor_ids=atomic.claims[0].anchor_ids,
                    mapping_ids=atomic.claims[0].mapping_ids,
                    extraction_provider_kind=DailyProviderKind.CODEX.value,
                    mapping_provider_kind=DailyProviderKind.CODEX.value,
                ),
            )

        universe = (
            DailyUniverseMember(
                target_id=self.target_id,
                target_name="삼성전자",
                market="KOSPI",
                as_of_date=self.as_of_date,
            ),
            DailyUniverseMember(
                target_id="000660",
                target_name="SK하이닉스",
                market="KOSPI",
                as_of_date=self.as_of_date,
            ),
        )
        baseline = tuple(
            DailyBaselineLane(
                target_id=member.target_id,
                as_of_date=self.as_of_date,
                lane_type=lane.value,
                lane_status=DailyBaselineLaneStatus.OBSERVED.value,
                source_ids=(f"BASE-{member.target_id}-{lane.value}",),
                observed_date=self.as_of_date,
            )
            for member in universe
            for lane in DailyBaselineLaneType
        )
        trigger = CurrentTriggerSignal(
            signal_id="TRIGGER-LIVE",
            target_id=self.target_id,
            observed_date=self.as_of_date,
            trigger_type=CurrentTriggerType.OFFICIAL.value,
            source_id="OFFICIAL-LIVE",
        )
        source_task = DailySourceTaskRecord(
            task_id="SOURCE-TASK-LIVE",
            target_id=self.target_id,
            question_task_id="QUESTION-LIVE",
            source_class="IssuerIR",
            max_queries=1,
            max_candidates=2,
            max_fetches=1,
            max_retries=0,
        )
        execution = DailyDeepExecution(
            execution_id="EXEC-LIVE",
            target_id=self.target_id,
            outcome=CurrentDeepOutcome.SOURCE_PENDING.value,
            trigger_signal_ids=(trigger.signal_id,),
            terminal_reason="one material source gap remains open",
            atomic_decision_id=decision.decision_id,
            source_task_ids=(source_task.task_id,),
            provider_kind=DailyProviderKind.CODEX.value,
            provider_trace_id="TRACE-LIVE",
            llm_calls=1,
            source_tasks=1,
            fetches=1,
            official_first_attempted=True,
            runtime_seconds=1.0,
        )
        config = CurrentOperationRunnerConfig(
            max_official_light_targets=1,
            max_deep_candidates=1,
            max_brain_candidates=1,
            max_acquisition_candidates=1,
            max_llm_calls_per_candidate=2,
            max_source_tasks_per_candidate=2,
            max_fetches_per_candidate=2,
            max_retries_per_candidate=1,
            max_general_web_fetches_per_candidate=0,
            max_runtime_seconds=30.0,
            test_mode=False,
            require_claim_provenance=True,
        )
        inputs = CurrentOperationRunnerInput(
            as_of_date=self.as_of_date,
            universe=universe,
            baseline_lanes=baseline,
            triggers=(trigger,),
            claims=atomic.claims,
            claim_provenance=claim_provenance,
            source_tasks=(source_task,),
            atomic_decisions=(decision,),
            deep_executions=(execution,),
            config=config,
        )
        return run_current_daily_census(inputs), inputs, {
            "schema_version": "e2r_live_source_acquisition_v1",
            "acquisition_class": "REAL_PROVIDER_FETCH",
            "document_id": "DOC-LIVE",
            "content_hash": content_hash,
            "content_text": text,
            "canonical_url": (
                "https://news.samsung.com/global/"
                "samsung-electronics-announces-first-quarter-2026-results"
            ),
            "target_id": self.target_id,
        }

    @staticmethod
    def _write_live_leaves(
        root: Path,
        *,
        document: dict[str, object],
        stale_canonical: bool = False,
    ) -> None:
        for name in (
            "planner_runs.jsonl",
            "source_task_satisfaction.jsonl",
            "evidence_anchors.jsonl",
            "raw_assertions.jsonl",
            "adjudicated_claims.jsonl",
        ):
            write_jsonl(root / name, ())
        write_jsonl(root / "evidence_documents.jsonl", (document,))
        write_jsonl(
            root / "provider_fetch_results.jsonl",
            (
                {
                    "acquisition_class": "REAL_PROVIDER_FETCH",
                    "cache_hit": False,
                    "document_id": document["document_id"],
                    "content_hash": document["content_hash"],
                    "provider_name": "IssuerNewsroom",
                    "provider_error": None,
                },
            ),
        )
        stale = ({"claim_id": "STALE-CLAIM"},) if stale_canonical else ()
        write_jsonl(root / "accepted_current_claims.jsonl", stale)
        write_jsonl(root / "daily_claim_provenance.jsonl", stale)
        write_jsonl(root / "atomic_stage_decisions.jsonl", stale)
        write_jsonl(root / "primitive_states.jsonl", stale)
        write_jsonl(root / "universe_eligible.jsonl", ())
        write_jsonl(root / "baseline_lanes.jsonl", ())
        write_jsonl(root / "trigger_signals.jsonl", ())
        write_jsonl(root / "source_tasks.jsonl", ())

    @staticmethod
    def _read_json(path: Path) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, object]]:
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]


if __name__ == "__main__":
    unittest.main()
