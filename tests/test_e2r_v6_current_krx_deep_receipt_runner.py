from __future__ import annotations

import json
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from e2r.production.metadata import stable_hash
import e2r.production.v6_current_krx_deep_receipt_runner as deep
import e2r.cli.run_e2r_v6_current_krx_deep_receipts_until_pass as deep_cli
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    REQUIRED_TARGET_FILES,
    VERIFICATION_PASS,
    receipt_content_index,
    receipt_content_tree_hash,
)
from tests.test_e2r_v6_canary_compact_receipt import (
    _selection as compact_selection,
    _write_terminal_output,
)


class E2RV6CurrentKrxDeepReceiptRunnerTests(unittest.TestCase):
    AS_OF = "2026-08-09"
    TARGET = "123456"
    ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"

    def _candidate(self, *, target_id: str | None = None, priority: float = 9.0):
        target = target_id or self.TARGET
        lineage = {
            "planner_terminal_status": "COMPLETE",
            "planner_run_id": f"PLANRUN-{target}",
            "blind_input_id": f"BLIND-{target}",
            "plan_hash": "1" * 64,
            "depth_decision_id": f"DEPTH-{target}",
            "depth_decision_hash": "2" * 64,
            "candidate_event_id": f"CAND-{target}",
            "candidate_event_hash": "3" * 64,
            "trigger_signal_ids": [f"TRIG-{target}"],
            "trigger_types": ["OFFICIAL"],
            "trigger_lineage_hash": "4" * 64,
            "source_refs": [f"SRC-{target}"],
            "event_source_refs": [f"SRC-{target}"],
            "event_latest_effective_date": "2026-08-07",
            "event_summary_hash": "6" * 64,
            "leading_archetype_id": self.ARCHETYPE,
            "direct_current_supporting_fact_ids": [f"FACT-{target}"],
            "recipe_ids": [f"RECIPE-{target}"],
            "available_source_families": ["OPENDART"],
            "priority_score": priority,
            "krx_effective_date": "2026-08-07",
            "krx_source_url": "https://data-dbg.krx.co.kr/current",
            "krx_source_hash": "5" * 64,
            "krx_request_id": f"KRXREQ-{target}",
            "natural_selection": True,
            "official_profile_binding": None,
            "phase105_canary_receipt_reused": False,
        }
        return {
            "target_id": target,
            "company_name": f"현재기업-{target}",
            "as_of_date": self.AS_OF,
            "archetype_id": self.ARCHETYPE,
            "latest_trading_snapshot_date": "2026-08-07",
            "natural_lineage": lineage,
            "natural_lineage_hash": stable_hash(lineage),
        }

    def test_projection_requires_complete_natural_depth_and_seals_trigger_lineage(self):
        raw = {
            "depth_decision": {
                "selected_for_deep": True,
                "selected_for_brain": True,
                "acquisition_eligible": True,
                "maximum_depth": "L3_RESEARCH_BRAIN",
                "priority_score": 13.5,
            }
        }
        projected = {
            "planner_terminal_status": "COMPLETE",
            "official_profile_binding": None,
            "target_id": self.TARGET,
            "company_name": "현재기업",
            "planner_run_id": "PLANRUN-current",
            "blind_input_id": "BLIND-current",
            "plan_hash": "1" * 64,
            "depth_decision_id": "DEPTH-current",
            "depth_decision_hash": "2" * 64,
            "candidate_event_id": "CAND-current",
            "candidate_event_hash": "3" * 64,
            "event_trigger_signal_ids": ["TRIG-current"],
            "event_trigger_types": ["OFFICIAL"],
            "event_source_refs": ["SRC-current"],
            "event_latest_effective_date": "2026-08-07",
            "event_summary": "현재기업: OFFICIAL current trigger 1건 검증 필요",
            "source_refs": ["SRC-current"],
            "leading_archetype_id": self.ARCHETYPE,
            "direct_current_supporting_fact_ids": ["FACT-current"],
            "recipe_ids": ["RECIPE-current"],
            "available_source_families": ["OPENDART"],
            "krx_effective_date": "2026-08-07",
            "krx_source_url": "https://data-dbg.krx.co.kr/current",
            "krx_source_hash": "4" * 64,
            "krx_request_id": "KRXREQ-current",
        }
        trigger = {
            "trigger_signal_id": "TRIG-current",
            "target_id": self.TARGET,
            "target_name": "현재기업",
            "trigger_type": "OFFICIAL",
            "effective_date": "2026-08-07",
            "investigation_required": True,
            "source_refs": ["SRC-current"],
        }
        with patch.object(deep, "_candidate_projection", return_value=projected):
            result = deep.project_natural_current_candidate(
                raw,
                trigger_rows=(trigger,),
                as_of_date=self.AS_OF,
            )
        lineage = result["natural_lineage"]
        self.assertEqual(lineage["planner_terminal_status"], "COMPLETE")
        self.assertTrue(lineage["natural_selection"])
        self.assertIsNone(lineage["official_profile_binding"])
        self.assertFalse(lineage["phase105_canary_receipt_reused"])
        self.assertEqual(lineage["priority_score"], 13.5)
        self.assertEqual(lineage["trigger_lineage_hash"], stable_hash([trigger]))

        forced = dict(projected)
        forced["planner_terminal_status"] = "ABSTAINED"
        forced["official_profile_binding"] = {"profile_id": "forced"}
        with patch.object(deep, "_candidate_projection", return_value=forced):
            with self.assertRaisesRegex(ValueError, "not a COMPLETE"):
                deep.project_natural_current_candidate(
                    raw,
                    trigger_rows=(trigger,),
                    as_of_date=self.AS_OF,
                )

    def test_candidate_choice_is_priority_then_identity_without_target_hardcoding(self):
        low = self._candidate(target_id="654321", priority=1.0)
        high_b = self._candidate(target_id="222222", priority=8.0)
        high_a = self._candidate(target_id="111111", priority=8.0)
        raw = ({"id": "low"}, {"id": "high-b"}, {"id": "high-a"})
        with patch.object(
            deep,
            "load_current_live_selection_inputs",
            return_value=(raw, ()),
        ), patch.object(
            deep,
            "project_natural_current_candidate",
            side_effect=(low, high_b, high_a),
        ):
            result = deep.natural_current_candidates(
                live_root="unused",
                as_of_date=self.AS_OF,
            )
        self.assertEqual([row["target_id"] for row in result], ["111111", "222222", "654321"])

    def test_collaboration_wait_returns_immediately_without_score_authority(self):
        candidate = self._candidate()
        calls: list[object] = []

        class PendingRunner:
            def run_checkpoint(inner_self, *, config, target, **kwargs):
                calls.append((config, target, kwargs))
                raise StructuredProviderUnavailable(
                    "COLLABORATION_RESPONSE_PENDING:COLLABREQ-test"
                )

        with tempfile.TemporaryDirectory() as tmp, patch.object(
            deep, "natural_current_candidates", return_value=(candidate,)
        ), patch.object(
            deep, "_pending_request_ids", return_value=("COLLABREQ-test",)
        ):
            root = Path(tmp)
            result = deep.V6CurrentKrxDeepReceiptRunner(
                checkpoint_runner_factory=lambda _row: PendingRunner()
            ).run_checkpoint(
                repo_root=root,
                as_of_date=self.AS_OF,
                live_root=root / "live",
                work_root=root / "work",
                deep_receipt_root=root / "receipts",
                live_materialization_authorized=True,
                checkpoint_resume=True,
            )

        self.assertEqual(result["status"], deep.PHASE107_DEEP_RUN_PENDING)
        self.assertEqual(result["external_wait_marker"], "COLLABORATION_RESPONSE_PENDING")
        self.assertEqual(result["pending_requests"], ["COLLABREQ-test"])
        self.assertFalse(result["score_or_stage_authority"])
        self.assertFalse(result["production_readiness_authority"])
        self.assertEqual(len(calls), 1)
        config, target, kwargs = calls[0]
        self.assertEqual(config.archetype_id, self.ARCHETYPE)
        self.assertEqual(config.as_of_date, self.AS_OF)
        self.assertTrue(config.gold_lane_isolated)
        self.assertEqual(target.symbol, self.TARGET)
        self.assertEqual(kwargs["source_resume_mode"], "REUSE_READY_CHECKPOINT")

    def test_terminal_checkpoint_exports_and_reverifies_one_natural_receipt(self):
        candidate = self._candidate()
        calls: list[object] = []

        class TerminalRunner:
            def run_checkpoint(inner_self, **kwargs):
                calls.append(kwargs)
                return SimpleNamespace(status=deep.PHASE107_TERMINAL_RESEARCH_STATUS)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            receipt_path = root / "receipts" / self.TARGET
            report = {
                "status": VERIFICATION_PASS,
                "critical_count": 0,
                "target_id": self.TARGET,
            }
            with patch.object(
                deep, "natural_current_candidates", return_value=(candidate,)
            ), patch.object(
                deep,
                "export_current_krx_deep_receipt",
                return_value=receipt_path,
            ) as export, patch.object(
                deep,
                "verify_current_krx_deep_receipt",
                return_value=report,
            ):
                result = deep.V6CurrentKrxDeepReceiptRunner(
                    checkpoint_runner_factory=lambda _row: TerminalRunner()
                ).run_checkpoint(
                    repo_root=root,
                    as_of_date=self.AS_OF,
                    live_root=root / "live",
                    work_root=root / "work",
                    deep_receipt_root=root / "receipts",
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                )
        self.assertEqual(result["status"], deep.PHASE107_DEEP_RUN_PASS)
        self.assertEqual(result["selected_target_id"], self.TARGET)
        self.assertEqual(len(calls), 1)
        self.assertEqual(export.call_args.kwargs["candidate"], candidate)
        self.assertFalse(result["score_or_stage_authority"])

    def test_existing_priority_receipt_advances_next_natural_candidate(self):
        first = self._candidate(target_id="111111", priority=9.0)
        second = self._candidate(target_id="222222", priority=8.0)
        invoked_targets: list[str] = []

        class TerminalRunner:
            def run_checkpoint(inner_self, *, target, **_kwargs):
                invoked_targets.append(target.symbol)
                return SimpleNamespace(status=deep.PHASE107_TERMINAL_RESEARCH_STATUS)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first_receipt = root / "receipts/111111"
            first_receipt.mkdir(parents=True)
            second_receipt = root / "receipts/222222"
            report = {
                "status": VERIFICATION_PASS,
                "critical_count": 0,
                "target_id": "111111",
                "metrics": {
                    "canonical_stage_recomputed": "0",
                    "total_score_recomputed": 0.0,
                },
            }
            with patch.object(
                deep, "natural_current_candidates", return_value=(first, second)
            ), patch.object(
                deep,
                "verify_current_krx_deep_receipt",
                return_value=report,
            ), patch.object(
                deep,
                "export_current_krx_deep_receipt",
                return_value=second_receipt,
            ) as export:
                result = deep.V6CurrentKrxDeepReceiptRunner(
                    checkpoint_runner_factory=lambda _row: TerminalRunner()
                ).run_checkpoint(
                    repo_root=root,
                    as_of_date=self.AS_OF,
                    live_root=root / "live",
                    work_root=root / "work",
                    deep_receipt_root=root / "receipts",
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                )
        self.assertEqual(invoked_targets, ["222222"])
        self.assertEqual(export.call_args.kwargs["candidate"], second)
        self.assertEqual(result["selected_target_id"], "222222")

    def test_cli_uses_canonical_live_path_and_preserves_pending_exit(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            live = repo / "output/live_materialization" / self.AS_OF
            live.mkdir(parents=True)
            pending = {
                "schema_version": deep.PHASE107_DEEP_RUN_SCHEMA,
                "status": deep.PHASE107_DEEP_RUN_PENDING,
                "external_wait_marker": "COLLABORATION_RESPONSE_PENDING",
                "blockers": ["COLLABORATION_RESPONSE_PENDING"],
                "score_or_stage_authority": False,
                "production_readiness_authority": False,
            }
            with patch.object(deep_cli, "canonical_repository_root", return_value=repo), patch.object(
                deep_cli, "_repository_identity_is_trusted", return_value=True
            ), patch.object(
                deep_cli.V6CurrentKrxDeepReceiptRunner,
                "run_checkpoint",
                return_value=pending,
            ) as run:
                output = io.StringIO()
                with redirect_stdout(output):
                    code = deep_cli.main(
                        [
                            "--as-of-date",
                            self.AS_OF,
                            "--repo-root",
                            str(repo),
                            "--live-root",
                            str(live),
                            "--work-root",
                            str(repo / "work"),
                            "--deep-receipt-root",
                            str(repo / "receipts"),
                            "--live-materialization-authorized",
                            "true",
                            "--checkpoint-resume",
                            "true",
                            "--research-provider",
                            "codex-collaboration",
                        ]
                    )
        self.assertEqual(code, 3)
        self.assertEqual(json.loads(output.getvalue()), pending)
        self.assertEqual(run.call_count, 1)
        self.assertEqual(run.call_args.kwargs["live_root"], live)
        self.assertTrue(run.call_args.kwargs["live_materialization_authorized"])
        self.assertTrue(run.call_args.kwargs["checkpoint_resume"])

    def test_cli_rejects_symlink_alias_for_canonical_live_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            live = repo / "output/live_materialization" / self.AS_OF
            live.mkdir(parents=True)
            alias = repo / "live-alias"
            alias.symlink_to(live, target_is_directory=True)
            with patch.object(
                deep_cli, "canonical_repository_root", return_value=repo
            ), patch.object(
                deep_cli, "_repository_identity_is_trusted", return_value=True
            ), self.assertRaisesRegex(ValueError, "cannot traverse a symlink"):
                deep_cli.main(
                    [
                        "--as-of-date",
                        self.AS_OF,
                        "--repo-root",
                        str(repo),
                        "--live-root",
                        str(alias),
                        "--work-root",
                        str(repo / "work"),
                        "--deep-receipt-root",
                        str(repo / "receipts"),
                        "--live-materialization-authorized",
                        "true",
                        "--checkpoint-resume",
                        "true",
                        "--research-provider",
                        "codex-collaboration",
                    ]
                )

    def test_actual_tracked_style_projection_exports_and_offline_recomputes(self):
        selection = compact_selection()
        selected = selection["selections"][0]
        assert isinstance(selected, dict)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            source.mkdir()
            target = _write_terminal_output(source, selection)
            provider_audit_path = target / "research_provider_response_cache_audit.json"
            provider_audit = json.loads(provider_audit_path.read_text(encoding="utf-8"))
            provider_audit["transport_call_count"] = provider_audit["logical_call_count"]
            provider_audit_path.write_text(
                json.dumps(provider_audit, sort_keys=True) + "\n", encoding="utf-8"
            )
            target_manifest_path = target / "target_run_manifest.json"
            target_manifest = json.loads(target_manifest_path.read_text(encoding="utf-8"))
            target_manifest["company_name"] = selected["company_name"]
            target_manifest["latest_trading_snapshot_date"] = selected["krx_effective_date"]
            target_manifest["output_tree_hash"] = deep.canary_output_tree_hash(
                target,
                include_post_run_gold=False,
            )
            target_manifest_path.write_text(
                json.dumps(target_manifest, sort_keys=True) + "\n", encoding="utf-8"
            )

            lineage = dict(self._candidate(target_id=str(selected["target_id"]))["natural_lineage"])
            lineage.update(
                {
                    "leading_archetype_id": selected["archetype_id"],
                    "krx_effective_date": selected["krx_effective_date"],
                    "krx_source_url": selected["krx_source_url"],
                    "krx_source_hash": selected["krx_source_hash"],
                    "krx_request_id": selected["krx_request_id"],
                }
            )
            candidate = {
                "target_id": selected["target_id"],
                "company_name": selected["company_name"],
                "as_of_date": selected["selection_as_of_date"],
                "archetype_id": selected["archetype_id"],
                "latest_trading_snapshot_date": selected["krx_effective_date"],
                "natural_lineage": lineage,
                "natural_lineage_hash": stable_hash(lineage),
            }

            original_provider_projection = deep._provider_call_receipts

            def provider_projection(target_root: Path):
                calls = list(original_provider_projection(target_root))
                decisions = deep._decision_rows(target_root)
                components = deep._component_receipts(target_root, decisions)
                facts = deep._fact_receipts(
                    target_root,
                    components,
                    as_of_date=str(selected["selection_as_of_date"]),
                    target_id=str(selected["target_id"]),
                )
                grouped: dict[tuple[str, str, str], list[dict[str, object]]] = {}
                for fact in facts:
                    key = (
                        str(fact["extraction_provider_name"]),
                        str(fact["provider_prompt_hash"]),
                        str(fact["provider_response_hash"]),
                    )
                    grouped.setdefault(key, []).append(dict(fact))
                for index, (lineage_key, lineage_facts) in enumerate(sorted(grouped.items())):
                    provider_name, prompt_hash, response_hash = lineage_key
                    calls.append(
                        {
                            "schema_version": "e2r_v6_provider_call_receipt_v1",
                            "provider_call_id": f"FACTCALL-{index:024d}",
                            "call_scope": "FACT_EXTRACTION",
                            "provider_name": provider_name,
                            "provider_kind": deep._provider_kind(provider_name),
                            "provider_attempt_count": 1,
                            "prompt_hash": prompt_hash,
                            "response_hash": response_hash,
                            "status": "SUCCESS",
                            "score_or_stage_authority": False,
                            "request_id": "COLLABREQ-" + f"{index + 1:064x}",
                            "response_id": "COLLABRESP-" + f"{index + 1:064x}",
                            "request_envelope_hash": f"{index + 2:064x}",
                            "response_envelope_hash": f"{index + 3:064x}",
                            "fact_scope_attestation_hashes": sorted(
                                deep._fact_scope_attestation_hash(fact)
                                for fact in lineage_facts
                            ),
                            "request_envelope_zlib_b64": "eA==",
                            "response_envelope_zlib_b64": "eA==",
                        }
                    )
                return tuple(calls)

            with patch.object(deep, "_provider_call_receipts", side_effect=provider_projection), patch.object(
                deep, "_embedded_fact_journal_call_is_exact", return_value=True
            ):
                receipt = deep.export_current_krx_deep_receipt(
                    repo_root=Path(__file__).resolve().parents[1],
                    target_root=target,
                    destination_root=root / "receipts",
                    candidate=candidate,
                )
                report = deep.verify_current_krx_deep_receipt(
                    receipt,
                    repo_root=Path(__file__).resolve().parents[1],
                    expected_candidate=candidate,
                )
                judge_path = receipt / "judge_decisions.jsonl"
                original_judges = judge_path.read_text(encoding="utf-8")
                judge_rows = [
                    json.loads(line)
                    for line in original_judges.splitlines()
                    if line.strip()
                ]
                judge_rows[0]["provider_route"] = "UNBOUND_ROUTE"
                judge_path.write_text(
                    "".join(
                        json.dumps(row, sort_keys=True, separators=(",", ":"))
                        + "\n"
                        for row in judge_rows
                    ),
                    encoding="utf-8",
                )

                def resign_manifest() -> None:
                    manifest_path = receipt / "receipt_manifest.json"
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    manifest["tracked_receipt_content_index"] = list(
                        receipt_content_index(receipt)
                    )
                    manifest["tracked_receipt_tree_hash"] = receipt_content_tree_hash(
                        receipt
                    )
                    body = {
                        key: value
                        for key, value in manifest.items()
                        if key != "receipt_payload_hash"
                    }
                    manifest["receipt_payload_hash"] = stable_hash(body)
                    manifest_path.write_text(
                        json.dumps(manifest, sort_keys=True) + "\n",
                        encoding="utf-8",
                    )

                resign_manifest()
                route_tampered = deep.verify_current_krx_deep_receipt(
                    receipt,
                    repo_root=Path(__file__).resolve().parents[1],
                    expected_candidate=candidate,
                )

                judge_path.write_text(original_judges, encoding="utf-8")
                fact_path = receipt / "scoring_facts.jsonl"
                fact_rows = [
                    json.loads(line)
                    for line in fact_path.read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
                fact_rows[0]["source_url"] = "https://tamper.invalid/source"
                fact_path.write_text(
                    "".join(
                        json.dumps(row, sort_keys=True, separators=(",", ":"))
                        + "\n"
                        for row in fact_rows
                    ),
                    encoding="utf-8",
                )
                resign_manifest()
                source_tampered = deep.verify_current_krx_deep_receipt(
                    receipt,
                    repo_root=Path(__file__).resolve().parents[1],
                    expected_candidate=candidate,
                )
        self.assertEqual(report["status"], VERIFICATION_PASS)
        self.assertEqual(report["metrics"]["component_count"], 7)
        self.assertEqual(report["metrics"]["judge_decision_count"], 21)
        self.assertGreater(report["metrics"]["scoring_fact_count"], 0)
        self.assertNotEqual(route_tampered["status"], VERIFICATION_PASS)
        self.assertNotEqual(source_tampered["status"], VERIFICATION_PASS)

    def _write_hash_bound_fixture(self, root: Path):
        target = root / self.TARGET
        target.mkdir(parents=True)
        score = {
            "query_count": 1,
            "document_count": 1,
            "fact_count": 2,
            "counterfact_count": 1,
            "material_gap_count": 0,
            "provider_error_count": 0,
            "unauthorized_provider_call_count": 0,
            "local_provider_call_count": 0,
            "score_valid": True,
            "canonical_stage": "2",
        }
        for name in REQUIRED_TARGET_FILES:
            payload = score if name == "score_receipt.json" else {"leaf": name}
            if name.endswith(".jsonl"):
                target.joinpath(name).write_text(
                    json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8"
                )
            else:
                target.joinpath(name).write_text(
                    json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8"
                )
        candidate = self._candidate()
        output_tree_hash = "a" * 64
        receipt_id = "KDXDEEP-" + stable_hash(
            {
                "natural_lineage_hash": candidate["natural_lineage_hash"],
                "output_tree_hash": output_tree_hash,
                "target_id": self.TARGET,
                "as_of_date": self.AS_OF,
            }
        )[:24]
        body = {
            "schema_version": deep.PHASE107_DEEP_RECEIPT_SCHEMA,
            "status": deep.PHASE107_DEEP_RECEIPT_PASS,
            "receipt_id": receipt_id,
            "target_id": self.TARGET,
            "company_name": candidate["company_name"],
            "as_of_date": self.AS_OF,
            "latest_trading_snapshot_date": candidate["latest_trading_snapshot_date"],
            "archetype_id": self.ARCHETYPE,
            "natural_lineage": candidate["natural_lineage"],
            "natural_lineage_hash": candidate["natural_lineage_hash"],
            "output_tree_hash": output_tree_hash,
            "artifact_names": list(REQUIRED_TARGET_FILES),
            "tracked_receipt_content_index": list(receipt_content_index(target)),
            "tracked_receipt_tree_hash": receipt_content_tree_hash(target),
            "component_count": 7,
            "judge_decision_count": 21,
            "scoring_fact_count": 1,
            "source_count": 1,
            "anchor_count": 1,
            "provider_call_count": 1,
            **score,
            "gold_visibility": False,
            "score_or_stage_authority": False,
            "production_readiness_authority": False,
        }
        manifest = {**body, "receipt_payload_hash": stable_hash(body)}
        target.joinpath("receipt_manifest.json").write_text(
            json.dumps(manifest, sort_keys=True) + "\n", encoding="utf-8"
        )
        metrics = {
            "component_count": 7,
            "judge_decision_count": 21,
            "scoring_fact_count": 1,
            "source_count": 1,
            "anchor_count": 1,
            "provider_call_count": 1,
            "total_score_recomputed": 61.0,
            "canonical_stage_recomputed": "2",
        }
        return target, candidate, metrics

    def test_offline_verifier_rejects_raw_hash_tamper_and_forced_relabel(self):
        with tempfile.TemporaryDirectory() as tmp:
            target, candidate, metrics = self._write_hash_bound_fixture(Path(tmp))
            with patch.object(deep, "_validate_artifacts", return_value=metrics):
                passed = deep.verify_current_krx_deep_receipt(
                    target,
                    repo_root=tmp,
                    expected_candidate=candidate,
                )
                self.assertEqual(passed["status"], VERIFICATION_PASS)
                target.joinpath("scoring_facts.jsonl").write_text(
                    '{"tampered":true}\n', encoding="utf-8"
                )
                tampered = deep.verify_current_krx_deep_receipt(
                    target,
                    repo_root=tmp,
                    expected_candidate=candidate,
                )
            self.assertNotEqual(tampered["status"], VERIFICATION_PASS)

        with tempfile.TemporaryDirectory() as tmp:
            target, candidate, metrics = self._write_hash_bound_fixture(Path(tmp))
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["natural_lineage"]["official_profile_binding"] = {
                "profile_id": "forced"
            }
            manifest["natural_lineage_hash"] = stable_hash(manifest["natural_lineage"])
            body = {key: value for key, value in manifest.items() if key != "receipt_payload_hash"}
            manifest["receipt_payload_hash"] = stable_hash(body)
            manifest_path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")
            with patch.object(deep, "_validate_artifacts", return_value=metrics):
                forced = deep.verify_current_krx_deep_receipt(
                    target,
                    repo_root=tmp,
                )
            self.assertNotEqual(forced["status"], VERIFICATION_PASS)
            self.assertEqual(forced["critical_count"], 1)


if __name__ == "__main__":
    unittest.main()
