from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import asyncio
import json
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from e2r.pro_first.dossier import (
    DossierDeltaMergeError,
    DossierValidationContext,
    DossierIdentityBindingError,
    ResearchDossierNormalizer,
    apply_research_dossier_delta,
    bind_dossier_transport_identity,
)
from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.packet import DeltaResearchContext
from e2r.pro_first.browser.protocol import (
    BrowserInspection,
    BrowserResultSnapshot,
    BrowserUIState,
    PreparedBrowserJob,
    RecoveredBrowserConversation,
)
from e2r.pro_first.config import (
    ProAuthorityRuntimeConfig,
    ProBrowserConfig,
    ProDashboardRuntimeConfig,
    ProFirstLocalConfig,
    ProScanRuntimeConfig,
    ProScheduleRuntimeConfig,
    ProSupplementRuntimeConfig,
)
from e2r.pro_first.job_store import (
    ProFirstJobStore,
    _ensure_dossier_snapshot_revision_schema,
)
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.multi_pass import (
    ProMultiPassDossierStore,
    ProMultiPassResearchOrchestrator,
    load_effective_research_dossier,
)
from e2r.pro_first.operations import (
    _git_head,
    build_delta_job_packet_v2,
    build_job_packet_v2,
    create_forced_validation_canary,
    prepare_v2_job_in_logged_in_browser,
    recover_submitted_v2_job_in_logged_in_browser,
)
from e2r.pro_first.canary.live_v2 import (
    _accepted_dossier_fact_ids,
    _compile_question_bounds,
    _completed_current_repair_reprocess_pass_id,
    _durable_pass_rows,
    _followup_execution_mode,
    _has_exact_followup_markers,
    _has_snapshotted_completed_pass,
    _load_recovered_snapshot_state,
    _normalize_followup_dossier_pre_schema,
    _public_gap_followup_question_ids,
    _quarantine_misbound_followup_capture,
    _submitted_unsnapshotted_followup_plan,
    _verification_artifact_rows,
    _verification_needs_effective_dossier_reverification,
)
from e2r.pro_first.capture.receipt import (
    CAPTURE_EVENT_TYPE,
    CAPTURE_RECEIPT_SCHEMA,
    CaptureReceipt,
    file_sha256,
)
from e2r.cli.run_e2r_pro_first_v2_live_canaries import _parse_spec
from tests.test_e2r_pro_first_v2_saturation import _complete_dossier
from tests.test_e2r_pro_first_v2_dossier_status import _base_v2


ARCHETYPE = "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"


class ProFirstV2LiveRuntimeTest(unittest.TestCase):
    now = datetime(2026, 8, 23, 1, 2, 3, tzinfo=timezone.utc)

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.runtime = self.root / "runtime"
        self.store = ProFirstJobStore(
            self.root / "pro-first.sqlite3",
            now=lambda: self.now,
        )

    def test_windows_cmd_preserved_outer_quotes_are_removed_from_canary_spec(self) -> None:
        spec = _parse_spec(
            '"000660|SK하이닉스|C06_HBM_MEMORY_CUSTOMER_CAPACITY"',
            as_of_date="2026-08-23",
        )
        self.assertEqual(spec.symbol, "000660")
        self.assertEqual(spec.company_name, "SK하이닉스")
        self.assertEqual(
            spec.archetype_id,
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )

    def test_running_submitted_followup_recovers_result_without_resubmit(self) -> None:
        pass_root = self.root / "submitted-followup"
        research_pass = SimpleNamespace(
            status="RESEARCH_RUNNING",
            submit_count=1,
        )
        self.assertEqual(
            _followup_execution_mode(research_pass, pass_root=pass_root),
            "RECOVER_SUBMITTED_RESULT",
        )

    def test_claimed_transport_timeout_recovers_result_without_resubmit(self) -> None:
        pass_root = self.root / "claimed-transport-timeout"
        research_pass = SimpleNamespace(
            status="TRANSPORT_PENDING",
            submit_count=1,
        )

        self.assertEqual(
            _followup_execution_mode(research_pass, pass_root=pass_root),
            "RECOVER_SUBMITTED_RESULT",
        )

    def test_provider_failed_pass_accepts_only_late_capture_recovery_mode(self) -> None:
        pass_root = self.root / "provider-failed-late-result"
        research_pass = SimpleNamespace(
            status="FAILED_HARD",
            submit_count=1,
            detail={
                "failure_domain": "PROVIDER",
                "automatic_resubmit_allowed": False,
            },
        )

        self.assertEqual(
            _followup_execution_mode(research_pass, pass_root=pass_root),
            "RECOVER_FAILED_LATE_RESULT",
        )
        incoming = pass_root / "capture/incoming"
        incoming.mkdir(parents=True)
        (incoming / "READY.json").write_text("{}", encoding="utf-8")
        (incoming / "browser_capture_receipt.json").write_text(
            "{}", encoding="utf-8"
        )
        self.assertEqual(
            _followup_execution_mode(research_pass, pass_root=pass_root),
            "REUSE_FAILED_LATE_CAPTURE",
        )

        with self.assertRaisesRegex(RuntimeError, "unambiguous"):
            _followup_execution_mode(
                SimpleNamespace(
                    status="FAILED_HARD",
                    submit_count=1,
                    detail={
                        "failure_domain": "TRANSPORT",
                        "automatic_resubmit_allowed": False,
                    },
                ),
                pass_root=self.root / "transport-failed",
            )

    def test_stale_verifier_roster_is_refreshed_before_repair_packets(self) -> None:
        dossier = _base_v2()
        current_hash = canonical_hash(dossier)
        stale = SimpleNamespace(
            result=None,
            receipt={"effective_dossier_hash": "a" * 64},
        )
        current = SimpleNamespace(
            result=None,
            receipt={"effective_dossier_hash": current_hash},
        )
        just_verified = SimpleNamespace(
            result=object(),
            receipt={"effective_dossier_hash": "a" * 64},
        )

        self.assertTrue(
            _verification_needs_effective_dossier_reverification(
                stale,
                dossier=dossier,
            )
        )
        self.assertFalse(
            _verification_needs_effective_dossier_reverification(
                current,
                dossier=dossier,
            )
        )
        self.assertFalse(
            _verification_needs_effective_dossier_reverification(
                just_verified,
                dossier=dossier,
            )
        )

    def test_public_gap_followup_never_steals_verifier_repair_questions(self) -> None:
        saturation = SimpleNamespace(
            missing_mandatory_question_ids=("Q-MISSING",),
            nonterminal_mandatory_question_ids=(
                "Q-MISSING",
                "Q-PUBLIC",
                "Q-REPAIR",
                "Q-PROVIDER",
                "Q-LIFECYCLE",
            ),
            public_material_gap_question_ids=("Q-PUBLIC", "Q-REPAIR"),
            verifier_repair_pending_ids=("Q-REPAIR",),
            provider_parser_core_pending_question_ids=("Q-PROVIDER",),
            lifecycle_hard_break_pending_ids=("Q-LIFECYCLE",),
        )

        self.assertEqual(
            _public_gap_followup_question_ids(saturation),
            ("Q-MISSING", "Q-PUBLIC"),
        )

    def test_submitted_public_gap_is_recovered_before_routing_rules_change(self) -> None:
        scope = SimpleNamespace(job_id="PROJOB-RECOVERY")
        research_pass = SimpleNamespace(
            pass_id="PROPASS-RUNNING",
            pass_name="PUBLIC_GAP_CLOSURE",
            submit_count=1,
            status="RESEARCH_RUNNING",
            prompt_hash="a" * 64,
        )
        ledger = SimpleNamespace(
            list_passes=lambda _job_id: (research_pass,),
            latest_dossier_snapshot_for_pass=lambda **_kwargs: None,
            get_scope=lambda _job_id: scope,
        )
        orchestrator = SimpleNamespace(ledger=ledger)

        recovered = _submitted_unsnapshotted_followup_plan(
            orchestrator,
            job_id="PROJOB-RECOVERY",
            pass_name="PUBLIC_GAP_CLOSURE",
        )

        self.assertIsNotNone(recovered)
        self.assertIs(recovered.scope, scope)
        self.assertIs(recovered.research_pass, research_pass)
        self.assertEqual(recovered.prompt_text, "")
        self.assertEqual(recovered.prompt_hash, "a" * 64)

        ledger.latest_dossier_snapshot_for_pass = lambda **_kwargs: object()
        self.assertIsNone(
            _submitted_unsnapshotted_followup_plan(
                orchestrator,
                job_id="PROJOB-RECOVERY",
                pass_name="PUBLIC_GAP_CLOSURE",
            )
        )

    def test_completed_noop_repair_is_reprocessed_before_descendant_snapshot(
        self,
    ) -> None:
        job_id = "PROJOB-REPAIR-REPROCESS"
        pass_id = "PROPASS-REPAIR-REPROCESS"
        job_root = self.root / "job"
        pass_root = job_root / f"research_passes/06_{pass_id}"
        incoming = pass_root / "capture/incoming"
        incoming.mkdir(parents=True)
        (incoming / "research_dossier.json").write_text(
            json.dumps(
                {
                    "verification_repair_register": [
                        {
                            "candidate_id": "PROFACT-OLD",
                            "status": "REPLACED",
                            "dossier_fact_id": "PROFACT-NEW",
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        receipt_root = job_root / "repair"
        receipt_root.mkdir(parents=True)
        receipt_path = receipt_root / "verifier_repair_receipt.json"
        receipt_path.write_text(
            json.dumps(
                {
                    "research_pass_id": pass_id,
                    "resolutions": [],
                    "unresolved_packet_ids": ["PACKET-1"],
                }
            ),
            encoding="utf-8",
        )
        research_pass = SimpleNamespace(
            job_id=job_id,
            pass_id=pass_id,
            pass_name="VERIFIER_REPAIR",
            pass_ordinal=6,
            status="COMPLETE",
            submit_count=1,
            response_hash="a" * 64,
        )
        snapshot = SimpleNamespace(
            snapshot_id="SNAPSHOT-REPAIR-1",
            revision_ordinal=1,
            dossier_hash=canonical_hash({"research_pass_id": pass_id}),
        )
        ledger = SimpleNamespace(
            get_pass=lambda _pass_id: research_pass,
            latest_dossier_snapshot_for_pass=lambda **_kwargs: snapshot,
            latest_dossier_snapshot=lambda _job_id: snapshot,
        )

        self.assertEqual(
            _completed_current_repair_reprocess_pass_id(
                ledger,
                job_id=job_id,
                dossier={"research_pass_id": pass_id},
                job_root=job_root,
            ),
            pass_id,
        )

        repaired = {
            "research_pass_id": pass_id,
            "verification_repair_register": [
                {
                    "packet_id": "PACKET-1",
                    "status": "REVERIFIED_ACCEPTED",
                }
            ],
        }
        (receipt_root / "effective_repaired_dossier.json").write_text(
            json.dumps(repaired),
            encoding="utf-8",
        )
        receipt_path.write_text(
            json.dumps(
                {
                    "research_pass_id": pass_id,
                    "resolutions": [
                        {
                            "packet_id": "PACKET-1",
                            "status": "REVERIFIED_ACCEPTED",
                        }
                    ],
                    "effective_dossier_hash": canonical_hash(repaired),
                }
            ),
            encoding="utf-8",
        )
        self.assertEqual(
            _completed_current_repair_reprocess_pass_id(
                ledger,
                job_id=job_id,
                dossier={"research_pass_id": pass_id},
                job_root=job_root,
            ),
            pass_id,
        )

        snapshot.dossier_hash = canonical_hash(
            ResearchDossierNormalizer().normalize(repaired).payload
        )
        self.assertIsNone(
            _completed_current_repair_reprocess_pass_id(
                ledger,
                job_id=job_id,
                dossier={"research_pass_id": pass_id},
                job_root=job_root,
            )
        )

        snapshot.revision_ordinal = 2
        self.assertIsNone(
            _completed_current_repair_reprocess_pass_id(
                ledger,
                job_id=job_id,
                dossier={"research_pass_id": pass_id},
                job_root=job_root,
            )
        )

    def test_followup_execution_modes_distinguish_submit_capture_and_partial_bundle(self) -> None:
        pass_root = self.root / "followup-modes"
        planned = SimpleNamespace(status="PLANNED", submit_count=0)
        self.assertEqual(
            _followup_execution_mode(planned, pass_root=pass_root),
            "PREPARE_AND_SUBMIT",
        )
        incoming = pass_root / "capture/incoming"
        incoming.mkdir(parents=True)
        (incoming / "READY.json").write_text("{}", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "partially committed"):
            _followup_execution_mode(
                SimpleNamespace(status="RESEARCH_RUNNING", submit_count=1),
                pass_root=pass_root,
            )
        (incoming / "browser_capture_receipt.json").write_text(
            "{}", encoding="utf-8"
        )
        self.assertEqual(
            _followup_execution_mode(
                SimpleNamespace(status="RESEARCH_RUNNING", submit_count=1),
                pass_root=pass_root,
            ),
            "REUSE_CAPTURE",
        )
        self.assertEqual(
            _followup_execution_mode(
                SimpleNamespace(status="COMPLETE", submit_count=1),
                pass_root=pass_root,
            ),
            "REUSE_CAPTURE",
        )

    def test_wrong_previous_turn_capture_is_preserved_and_never_imported(self) -> None:
        pass_root = self.root / "misbound-followup"
        incoming = pass_root / "capture/incoming"
        incoming.mkdir(parents=True)
        expected_pass = "PROPASS-CURRENT"
        expected_parent = "PROPASS-PARENT"
        report_text = (
            "[[E2R_PRO_PASS_ID:PROPASS-PREVIOUS]]\n"
            "[[E2R_PRO_PARENT_PASS_ID:PROPASS-OLDER]]\n"
        )
        report = incoming / "pro_report.md"
        dossier = incoming / "research_dossier.json"
        report.write_text(report_text, encoding="utf-8")
        dossier.write_text("{}\n", encoding="utf-8")
        receipt = CaptureReceipt(
            schema_version=CAPTURE_RECEIPT_SCHEMA,
            event_type=CAPTURE_EVENT_TYPE,
            job_id="PROJOB-MISBOUND",
            run_id="PRORUN-MISBOUND",
            target_id="000660",
            as_of_date="2026-08-23",
            packet_hash="a" * 64,
            prompt_hash="b" * 64,
            conversation_id="conversation-misbound",
            assistant_turn_id="assistant-previous",
            report_md_hash=file_sha256(report),
            report_pdf_hash=None,
            dossier_json_hash=file_sha256(dossier),
            submit_count=1,
            capture_count=1,
            captured_at="2026-08-27T00:00:00Z",
            capture_mode="DIRECT_VISIBLE_RESPONSE",
            capture_source="VISIBLE_REPORT",
            optional_pdf_error=None,
        )

        self.assertFalse(
            _has_exact_followup_markers(
                report_text,
                pass_id=expected_pass,
                parent_pass_id=expected_parent,
            )
        )
        quarantine = _quarantine_misbound_followup_capture(
            pass_root=pass_root,
            capture_receipt=receipt,
            report_text=report_text,
            expected_pass_id=expected_pass,
            expected_parent_pass_id=expected_parent,
        )

        preserved = pass_root / quarantine["quarantine_relative_path"]
        self.assertFalse(incoming.exists())
        self.assertEqual(
            (preserved / "pro_report.md").read_text(encoding="utf-8"),
            report_text,
        )
        self.assertEqual(quarantine["status"], "PRESERVED_NOT_IMPORTED")
        self.assertFalse(quarantine["fact_import_allowed"])
        self.assertFalse(quarantine["automatic_resubmit_allowed"])

    def test_followup_v3_runs_initial_pre_schema_before_delta_merge(self) -> None:
        question_a = "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
        question_b = "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02"
        payload = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": "PROJOB-FOLLOWUP-PREFLIGHT",
            "source_documents": [],
            "material_facts": [
                {
                    "dossier_fact_id": "PROFACT-FOLLOWUP-ONE",
                    "fact_kind": "MATERIAL",
                    "question_family_ids": [question_a],
                }
            ],
            "counterfacts": [],
            "resolution_facts": [],
            "question_family_results": [
                {
                    "question_family_id": question_b,
                    "support_fact_ids": ["PROFACT-FOLLOWUP-ONE"],
                    "counter_fact_ids": [],
                    "resolution_fact_ids": [],
                }
            ],
            "source_lineages": [],
            "search_route_receipts": [],
        }

        normalized = _normalize_followup_dossier_pre_schema(
            payload,
            archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
        )

        self.assertEqual(
            normalized.payload["question_family_results"][0][
                "support_fact_ids"
            ],
            [],
        )
        self.assertEqual(
            normalized.payload["material_facts"][0]["question_family_ids"],
            [question_a],
        )
        self.assertIn(
            "DROP_UNBOUND_QUESTION_FACT_REFERENCE",
            {row.operation_code for row in normalized.operations},
        )

    def test_followup_delta_keeps_exact_prior_route_reference_during_preflight(self) -> None:
        question_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
        archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        payload = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": "PROJOB-FOLLOWUP-PRIOR-ROUTE",
            "source_documents": [],
            "material_facts": [],
            "counterfacts": [],
            "resolution_facts": [],
            "source_lineages": [],
            "derived_metrics": [],
            "search_route_receipts": [],
            "question_family_results": [
                {
                    "archetype_id": archetype_id,
                    "question_family_id": question_id,
                    "status": "PUBLIC_SEARCHABLE",
                    "search_route_receipt_ids": ["ROUTE-PRIOR-EXACT"],
                    "adequate_search_proven": False,
                }
            ],
        }
        prior = {
            "search_route_receipts": [
                {
                    "route_receipt_id": "ROUTE-PRIOR-EXACT",
                    "pass_id": "PROPASS-PRIOR",
                    "archetype_id": archetype_id,
                    "question_family_id": question_id,
                }
            ]
        }

        normalized = _normalize_followup_dossier_pre_schema(
            payload,
            archetype_ids=(archetype_id,),
            prior_dossier=prior,
        )

        self.assertEqual(
            normalized.payload["question_family_results"][0][
                "search_route_receipt_ids"
            ],
            ["ROUTE-PRIOR-EXACT"],
        )
        self.assertEqual(normalized.payload["search_route_receipts"], [])
        self.assertNotIn(
            "DROP_INVALID_QUESTION_ROUTE_REFERENCE",
            {row.operation_code for row in normalized.operations},
        )

    def test_durable_dossier_pass_rows_skip_only_unsubmitted_transport_plan(self) -> None:
        rows = (
            SimpleNamespace(
                pass_ordinal=1,
                pass_id="PASS-1",
                parent_pass_id=None,
                pass_name="INITIAL_FULL_RESEARCH",
                status="COMPLETE",
                submit_count=1,
                prompt_hash="a" * 64,
                response_hash="b" * 64,
            ),
            SimpleNamespace(
                pass_ordinal=2,
                pass_id="PASS-UNSENT",
                parent_pass_id="PASS-1",
                pass_name="VERIFIER_REPAIR",
                status="TRANSPORT_PENDING",
                submit_count=0,
                prompt_hash="c" * 64,
                response_hash=None,
            ),
            SimpleNamespace(
                pass_ordinal=3,
                pass_id="PASS-UNPERSISTED",
                parent_pass_id="PASS-1",
                pass_name="VERIFIER_REPAIR",
                status="FAILED_HARD",
                submit_count=1,
                prompt_hash="f" * 64,
                response_hash=None,
                pass_input_hash="9" * 64,
                detail={
                    "failure_domain": "TRANSPORT",
                    "failure_class": (
                        "CHATGPT_SUBMITTED_TURN_NOT_SERVER_PERSISTED"
                    ),
                    "server_persistence_confirmed": False,
                    "server_persistence_absence_confirmation_count": 2,
                    "server_persistence_failure_evidence_hash": "7" * 64,
                    "transport_failure_root_input_hash": "9" * 64,
                    "replacement_pass_allowed": True,
                },
            ),
            SimpleNamespace(
                pass_ordinal=4,
                pass_id="PASS-CURRENT",
                parent_pass_id="PASS-1",
                pass_name="VERIFIER_REPAIR",
                status="RESEARCH_RUNNING",
                submit_count=1,
                prompt_hash="d" * 64,
                response_hash=None,
                pass_input_hash="8" * 64,
                detail={
                    "supersedes_unpersisted_pass_id": "PASS-UNPERSISTED",
                    "transport_replacement_root_input_hash": "9" * 64,
                },
            ),
        )

        class FakeLedger:
            def list_passes(self, _job_id):
                return rows

            def get_pass(self, pass_id):
                return next(row for row in rows if row.pass_id == pass_id)

        compiled = _durable_pass_rows(
            FakeLedger(),  # type: ignore[arg-type]
            "JOB-1",
            current_pass_id="PASS-CURRENT",
            current_response_hash="e" * 64,
            prior_dossier={
                "research_passes": [
                    {
                        "pass_id": "PASS-1",
                        "parent_pass_id": None,
                        "pass_name": "INITIAL_FULL_RESEARCH",
                        "status": "COMPLETE",
                        "prompt_hash": "a" * 64,
                        "response_hash": "b" * 64,
                        "conversation_id": "CONVERSATION-1",
                    }
                ]
            },
        )
        self.assertEqual(
            [row["pass_id"] for row in compiled],
            ["PASS-1", "PASS-CURRENT"],
        )
        self.assertEqual(compiled[0]["conversation_id"], "CONVERSATION-1")

        mismatched_prior = {
            "research_passes": [
                {
                    **dict(compiled[0]),
                    "response_hash": "f" * 64,
                }
            ]
        }
        with self.assertRaisesRegex(
            ValueError,
            "effective dossier pass row differs from durable ledger",
        ):
            _durable_pass_rows(
                FakeLedger(),  # type: ignore[arg-type]
                "JOB-1",
                current_pass_id="PASS-CURRENT",
                current_response_hash="e" * 64,
                prior_dossier=mismatched_prior,
            )

    def test_durable_pass_rows_skip_sealed_unpersisted_different_context(self) -> None:
        failed = SimpleNamespace(
            pass_ordinal=1,
            pass_id="PASS-FAILED-OLD-CONTEXT",
            parent_pass_id=None,
            pass_name="SATURATION_AUDIT",
            status="FAILED_HARD",
            submit_count=1,
            prompt_hash="a" * 64,
            response_hash=None,
            pass_input_hash="b" * 64,
            detail={
                "failure_domain": "TRANSPORT",
                "failure_class": (
                    "CHATGPT_SUBMITTED_TURN_NOT_SERVER_PERSISTED"
                ),
                "server_persistence_confirmed": False,
                "server_persistence_absence_confirmation_count": 2,
                "server_persistence_failure_evidence_hash": "c" * 64,
                "transport_failure_root_input_hash": "b" * 64,
                "replacement_pass_allowed": True,
            },
        )
        current = SimpleNamespace(
            pass_ordinal=2,
            pass_id="PASS-CURRENT-NEW-CONTEXT",
            parent_pass_id=None,
            pass_name="SATURATION_AUDIT",
            status="RESEARCH_RUNNING",
            submit_count=1,
            prompt_hash="d" * 64,
            response_hash=None,
            pass_input_hash="e" * 64,
            detail={},
        )

        class FakeLedger:
            def list_passes(self, _job_id):
                return (failed, current)

            def get_pass(self, pass_id):
                return next(
                    row for row in (failed, current) if row.pass_id == pass_id
                )

        rows = _durable_pass_rows(
            FakeLedger(),  # type: ignore[arg-type]
            "JOB-1",
            current_pass_id=current.pass_id,
            current_response_hash="f" * 64,
        )

        self.assertEqual(
            [row["pass_id"] for row in rows],
            ["PASS-CURRENT-NEW-CONTEXT"],
        )

    def test_durable_pass_rows_keep_artifact_reexport_only_in_transport_ledger(self) -> None:
        initial = SimpleNamespace(
            pass_ordinal=1,
            pass_id="PASS-INITIAL",
            parent_pass_id=None,
            pass_name="INITIAL_FULL_RESEARCH",
            status="COMPLETE",
            submit_count=1,
            prompt_hash="a" * 64,
            response_hash="b" * 64,
            detail={},
        )
        artifact = SimpleNamespace(
            pass_ordinal=2,
            pass_id="PASS-ARTIFACT",
            parent_pass_id="PASS-INITIAL",
            pass_name="ARTIFACT_REEXPORT",
            status="COMPLETE",
            submit_count=1,
            prompt_hash="c" * 64,
            response_hash="d" * 64,
            detail={"transport_only": True},
        )
        current = SimpleNamespace(
            pass_ordinal=3,
            pass_id="PASS-CURRENT",
            parent_pass_id="PASS-INITIAL",
            pass_name="PUBLIC_GAP_CLOSURE",
            status="RESEARCH_RUNNING",
            submit_count=1,
            prompt_hash="e" * 64,
            response_hash=None,
            detail={},
        )

        class FakeLedger:
            def list_passes(self, _job_id):
                return (initial, artifact, current)

            def get_pass(self, pass_id):
                return next(
                    row
                    for row in (initial, artifact, current)
                    if row.pass_id == pass_id
                )

        rows = _durable_pass_rows(
            FakeLedger(),  # type: ignore[arg-type]
            "JOB-1",
            current_pass_id=current.pass_id,
            current_response_hash="f" * 64,
            prior_dossier={
                "research_passes": [
                    {
                        "pass_id": initial.pass_id,
                        "parent_pass_id": initial.parent_pass_id,
                        "pass_name": initial.pass_name,
                        "status": "COMPLETE",
                        "prompt_hash": initial.prompt_hash,
                        "response_hash": initial.response_hash,
                    }
                ]
            },
        )

        self.assertEqual(
            [row["pass_id"] for row in rows],
            ["PASS-INITIAL", "PASS-CURRENT"],
        )

    def test_durable_pass_rows_reject_unbound_or_mismatched_failed_pass(self) -> None:
        failed = SimpleNamespace(
            pass_ordinal=1,
            pass_id="PASS-FAILED",
            parent_pass_id=None,
            pass_name="SATURATION_AUDIT",
            status="FAILED_HARD",
            submit_count=1,
            prompt_hash="a" * 64,
            response_hash=None,
            pass_input_hash="b" * 64,
            detail={"server_persistence_confirmed": False},
        )
        current = SimpleNamespace(
            pass_ordinal=2,
            pass_id="PASS-CURRENT",
            parent_pass_id=None,
            pass_name="SATURATION_AUDIT",
            status="RESEARCH_RUNNING",
            submit_count=1,
            prompt_hash="c" * 64,
            response_hash=None,
            pass_input_hash="d" * 64,
            detail={},
        )

        class FakeLedger:
            def __init__(self, rows):
                self.rows = rows

            def list_passes(self, _job_id):
                return self.rows

            def get_pass(self, pass_id):
                return next(row for row in self.rows if row.pass_id == pass_id)

        with self.assertRaisesRegex(
            ValueError,
            "durable prior pass is missing its response hash",
        ):
            _durable_pass_rows(
                FakeLedger((failed, current)),  # type: ignore[arg-type]
                "JOB-1",
                current_pass_id="PASS-CURRENT",
                current_response_hash="e" * 64,
            )

        mismatched_current = SimpleNamespace(
            **{
                **current.__dict__,
                "detail": {
                    "supersedes_unpersisted_pass_id": "PASS-FAILED",
                    "transport_replacement_root_input_hash": "f" * 64,
                },
            }
        )
        with self.assertRaisesRegex(
            ValueError,
            "differs from replacement lineage",
        ):
            _durable_pass_rows(
                FakeLedger((failed, mismatched_current)),  # type: ignore[arg-type]
                "JOB-1",
                current_pass_id="PASS-CURRENT",
                current_response_hash="e" * 64,
            )

    def test_superseded_unpersisted_pass_stays_excluded_for_descendants(self) -> None:
        failed = SimpleNamespace(
            pass_ordinal=1,
            pass_id="PASS-FAILED",
            parent_pass_id=None,
            pass_name="SATURATION_AUDIT",
            status="FAILED_HARD",
            submit_count=1,
            prompt_hash="a" * 64,
            response_hash=None,
            pass_input_hash="b" * 64,
            detail={
                "failure_domain": "TRANSPORT",
                "failure_class": (
                    "CHATGPT_SUBMITTED_TURN_NOT_SERVER_PERSISTED"
                ),
                "server_persistence_confirmed": False,
                "server_persistence_absence_confirmation_count": 2,
                "server_persistence_failure_evidence_hash": "3" * 64,
                "transport_failure_root_input_hash": "b" * 64,
                "replacement_pass_allowed": True,
            },
        )
        replacement = SimpleNamespace(
            pass_ordinal=2,
            pass_id="PASS-REPLACEMENT",
            parent_pass_id=None,
            pass_name="SATURATION_AUDIT",
            status="COMPLETE",
            submit_count=1,
            prompt_hash="c" * 64,
            response_hash="d" * 64,
            pass_input_hash="e" * 64,
            detail={
                "supersedes_unpersisted_pass_id": "PASS-FAILED",
                "transport_replacement_root_input_hash": "b" * 64,
            },
        )
        descendant = SimpleNamespace(
            pass_ordinal=3,
            pass_id="PASS-DESCENDANT",
            parent_pass_id="PASS-REPLACEMENT",
            pass_name="PUBLIC_GAP_CLOSURE",
            status="RESEARCH_RUNNING",
            submit_count=1,
            prompt_hash="f" * 64,
            response_hash=None,
            pass_input_hash="1" * 64,
            detail={},
        )

        class FakeLedger:
            def list_passes(self, _job_id):
                return (failed, replacement, descendant)

            def get_pass(self, pass_id):
                return next(
                    row
                    for row in (failed, replacement, descendant)
                    if row.pass_id == pass_id
                )

        rows = _durable_pass_rows(
            FakeLedger(),  # type: ignore[arg-type]
            "JOB-1",
            current_pass_id="PASS-DESCENDANT",
            current_response_hash="2" * 64,
        )

        self.assertEqual(
            [row["pass_id"] for row in rows],
            ["PASS-REPLACEMENT", "PASS-DESCENDANT"],
        )

    def test_explicit_source_commit_supports_cross_runtime_packet_build(self) -> None:
        source_commit = "a" * 40
        with patch.dict("os.environ", {"E2R_SOURCE_COMMIT_SHA": source_commit}):
            self.assertEqual(_git_head(self.root / "not-a-git-repo"), source_commit)
        with patch.dict("os.environ", {"E2R_SOURCE_COMMIT_SHA": "HEAD;bad"}):
            with self.assertRaisesRegex(ValueError, "full hexadecimal"):
                _git_head(self.root)

    def _build(self):
        job = create_forced_validation_canary(
            self.store,
            symbol="TEST28",
            company_name="검증기업",
            as_of_date="2026-08-23",
            archetype_ids=(ARCHETYPE,),
        )
        return build_job_packet_v2(
            self.store,
            job_id=job.job_id,
            runtime_root=self.runtime,
            config_hash="c" * 64,
            repo_root=Path(__file__).resolve().parents[1],
        )

    def _build_delta(self):
        candidate = self.store.create_candidate(
            symbol="TEST28D",
            company_name="델타검증기업",
            as_of_date="2026-08-23",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="f" * 64,
            research_mode=ResearchMode.DELTA_RESEARCH,
            selection_receipt={
                "trigger_ids": ["TRIGGER-DELTA-1"],
                "reason_codes": ["MATERIAL_NEW_EVENT"],
            },
        )
        job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=(ARCHETYPE,),
        )
        question_id = f"{ARCHETYPE}_Q03"
        q03_closure = {"status": "SUPPORTED_SCORING"}
        q05_closure = {"status": "SUPPORTED_SCORING"}
        delta = DeltaResearchContext(
            prior_receipt={
                "prior_job_id": "PROJOB-PRIOR",
                "dossier_hash": "d" * 64,
            },
            new_events=(
                {
                    "event_id": "EVENT-DELTA-1",
                    "event_date": "2026-08-23",
                    "statement": "새 계약 갱신 공시",
                },
            ),
            new_or_superseding_facts=(),
            components_to_revisit=(
                "earnings_visibility",
                "information_confidence",
            ),
            question_families_to_revisit=(question_id,),
            prior_question_closure_map={
                question_id: {
                    **q03_closure,
                    "closure_hash": canonical_hash(q03_closure),
                },
                f"{ARCHETYPE}_Q05": {
                    **q05_closure,
                    "closure_hash": canonical_hash(q05_closure),
                },
            },
            stale_primitive_ids=("retention_or_renewal",),
            monitoring_question_family_ids=(question_id,),
        )
        thesis = {
            "prior_job_id": "PROJOB-PRIOR",
            "prior_dossier_hash": "d" * 64,
            "prior_as_of_date": "2026-08-22",
        }
        built = build_delta_job_packet_v2(
            self.store,
            job_id=job.job_id,
            runtime_root=self.runtime,
            config_hash="c" * 64,
            repo_root=Path(__file__).resolve().parents[1],
            existing_thesis_digest=thesis,
            delta_context=delta,
        )
        return built, thesis, delta

    def test_v2_packet_attaches_hash_bound_contracts_and_initial_pass(self) -> None:
        built = self._build()
        payload = built.packet_payload
        snapshot = payload["research_contract_snapshot"]
        unsigned = {
            key: value for key, value in snapshot.items() if key != "snapshot_hash"
        }
        self.assertEqual(payload["schema_version"], "e2r_pro_research_packet_v2")
        self.assertEqual(payload["output_contract"], "e2r_pro_research_dossier_v2")
        self.assertEqual(len(snapshot["contracts"]), 5)
        self.assertEqual(snapshot["snapshot_hash"], canonical_hash(unsigned))
        self.assertIn(f"[[E2R_PRO_PASS_ID:{built.initial_pass_id}]]", built.prompt.prompt_text)
        self.assertIn("PENDING_INITIAL_CONVERSATION", built.prompt.prompt_text)
        self.assertNotIn("expected_score", built.prompt.prompt_text.casefold())
        self.assertNotIn("expected_stage", built.prompt.prompt_text.casefold())

    def test_v2_packet_and_initial_pass_are_idempotent(self) -> None:
        first = self._build()
        second = build_job_packet_v2(
            self.store,
            job_id=first.job.job_id,
            runtime_root=self.runtime,
            config_hash="c" * 64,
            repo_root=Path(__file__).resolve().parents[1],
        )
        self.assertEqual(first.packet_bundle.packet_hash, second.packet_bundle.packet_hash)
        self.assertEqual(first.initial_pass_id, second.initial_pass_id)
        self.assertEqual(first.prompt.prompt_hash, second.prompt.prompt_hash)

    def test_delta_operational_path_reopens_only_impacted_questions(self) -> None:
        built, thesis, delta = self._build_delta()

        self.assertEqual(built.prompt.pass_name, ResearchMode.DELTA_RESEARCH.value)
        self.assertEqual(
            built.prompt.mandatory_question_ids,
            (f"{ARCHETYPE}_Q03",),
        )
        self.assertTrue(built.output_filename.endswith("_DELTA.md"))
        self.assertEqual(built.packet_payload["existing_thesis_digest"], thesis)
        self.assertEqual(
            built.packet_payload["delta_context"],
            delta.to_dict(),
        )
        self.assertIn("새 계약 갱신 공시", built.prompt.prompt_text)
        self.assertIn(f"{ARCHETYPE}_Q03", built.prompt.prompt_text)
        self.assertNotIn(f"1. `{ARCHETYPE}_Q05`", built.prompt.prompt_text)
        self.assertIn(
            f'"reused_question_family_ids": [\n        "{ARCHETYPE}_Q05"',
            built.prompt.prompt_text,
        )

    def test_delta_operational_path_is_idempotent_and_context_bound(self) -> None:
        first, thesis, delta = self._build_delta()
        second = build_delta_job_packet_v2(
            self.store,
            job_id=first.job.job_id,
            runtime_root=self.runtime,
            config_hash="c" * 64,
            repo_root=Path(__file__).resolve().parents[1],
            existing_thesis_digest=thesis,
            delta_context=delta,
        )
        self.assertEqual(first.packet_bundle.packet_hash, second.packet_bundle.packet_hash)
        self.assertEqual(first.initial_pass_id, second.initial_pass_id)
        changed_thesis = {**thesis, "prior_dossier_hash": "e" * 64}
        with self.assertRaisesRegex(ValueError, "differs from requested"):
            build_delta_job_packet_v2(
                self.store,
                job_id=first.job.job_id,
                runtime_root=self.runtime,
                config_hash="c" * 64,
                repo_root=Path(__file__).resolve().parents[1],
                existing_thesis_digest=changed_thesis,
                delta_context=delta,
            )

    def test_initial_conversation_binding_changes_only_transport_identity(self) -> None:
        built = self._build()
        payload = {
            "schema_version": "e2r_pro_research_dossier_v2",
            "conversation_id": "PENDING_INITIAL_CONVERSATION",
            "research_pass_id": built.initial_pass_id,
            "parent_pass_id": None,
            "material_facts": [
                {
                    "dossier_fact_id": "PROFACT-1",
                    "statement": "변경되면 안 되는 사실",
                    "source_url": "https://example.com/source",
                    "supporting_excerpt": "변경되면 안 되는 인용문",
                }
            ],
        }
        facts_before = deepcopy(payload["material_facts"])
        bound = bind_dossier_transport_identity(
            payload,
            conversation_id="CONVERSATION-LIVE-1",
            research_pass_id=built.initial_pass_id,
            parent_pass_id=None,
            allow_initial_conversation_placeholder=True,
        )
        self.assertEqual(bound.payload["conversation_id"], "CONVERSATION-LIVE-1")
        self.assertEqual(bound.payload["material_facts"], facts_before)
        self.assertEqual(
            bound.operations[0],
            "BIND_INITIAL_CONVERSATION_ID_FROM_CAPTURE_RECEIPT",
        )

    def test_initial_transport_aliases_bind_without_embedded_pass_row(self) -> None:
        built = self._build()
        payload = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "conversation_id": "PENDING_NEW_CONVERSATION",
            "research_pass_id": built.initial_pass_id,
            "parent_pass_id": "NONE",
            "research_passes": [],
            "material_facts": [
                {
                    "dossier_fact_id": "PROFACT-1",
                    "statement": "The source reported NONE as literal text.",
                }
            ],
        }

        bound = bind_dossier_transport_identity(
            payload,
            conversation_id="CONVERSATION-LIVE-1",
            research_pass_id=built.initial_pass_id,
            parent_pass_id=None,
            allow_initial_conversation_placeholder=True,
            pass_name="INITIAL_FULL_RESEARCH",
            prompt_hash="c" * 64,
            response_hash="d" * 64,
        )

        self.assertIsNone(bound.payload["parent_pass_id"])
        self.assertEqual(bound.payload["conversation_id"], "CONVERSATION-LIVE-1")
        self.assertEqual(
            bound.payload["material_facts"], payload["material_facts"]
        )
        self.assertEqual(len(bound.payload["research_passes"]), 1)
        self.assertEqual(
            bound.payload["research_passes"][0]["pass_id"],
            built.initial_pass_id,
        )
        self.assertIn("BIND_INITIAL_PARENT_PASS_NULL_ALIAS", bound.operations)
        self.assertIn(
            "BIND_INITIAL_CONVERSATION_ID_FROM_CAPTURE_RECEIPT",
            bound.operations,
        )

    def test_initial_null_alias_is_rejected_outside_exact_initial_scope(self) -> None:
        built = self._build()
        payload = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "conversation_id": "PENDING_NEW_CONVERSATION",
            "research_pass_id": built.initial_pass_id,
            "parent_pass_id": "NONE",
            "research_passes": [],
        }

        with self.assertRaisesRegex(
            DossierIdentityBindingError,
            "parent pass id differs",
        ):
            bind_dossier_transport_identity(
                payload,
                conversation_id="CONVERSATION-LIVE-1",
                research_pass_id=built.initial_pass_id,
                parent_pass_id=None,
                allow_initial_conversation_placeholder=True,
                pass_name="VERIFIER_REPAIR",
                prompt_hash="c" * 64,
                response_hash="d" * 64,
            )

    def test_identity_binding_rejects_arbitrary_or_nested_placeholder(self) -> None:
        built = self._build()
        base = {
            "schema_version": "e2r_pro_research_dossier_v2",
            "conversation_id": "UNRELATED-CONVERSATION",
            "research_pass_id": built.initial_pass_id,
            "parent_pass_id": None,
        }
        with self.assertRaises(DossierIdentityBindingError):
            bind_dossier_transport_identity(
                base,
                conversation_id="CONVERSATION-LIVE-1",
                research_pass_id=built.initial_pass_id,
                parent_pass_id=None,
                allow_initial_conversation_placeholder=True,
            )
        nested = {
            **base,
            "conversation_id": "PENDING_INITIAL_CONVERSATION",
            "business_model": {"note": "PENDING_INITIAL_CONVERSATION"},
        }
        with self.assertRaises(DossierIdentityBindingError):
            bind_dossier_transport_identity(
                nested,
                conversation_id="CONVERSATION-LIVE-1",
                research_pass_id=built.initial_pass_id,
                parent_pass_id=None,
                allow_initial_conversation_placeholder=True,
            )

    def test_precomputed_initial_pass_id_is_preserved_in_approval_scope(self) -> None:
        built = self._build()
        job = self._approve_and_mark_running(built)
        scope = ProMultiPassResearchOrchestrator(self.store).record_completed_initial_pass(
            job.job_id,
            primary_archetype_ids=(ARCHETYPE,),
            response_hash="d" * 64,
            initial_pass_id=built.initial_pass_id,
        )
        self.assertEqual(scope.initial_pass_id, built.initial_pass_id)

    def test_submitted_v2_recovery_reuses_packet_and_never_resubmits(self) -> None:
        built = self._build()
        running = self._approve_and_mark_running(
            built,
            conversation_id="WEB:transient-conversation",
        )
        report_text = "\n".join(
            (
                f"[[E2R_PRO_JOB_ID:{running.job_id}]]",
                f"[[E2R_PRO_RUN_ID:{built.packet_payload['run_id']}]]",
                "E2R_RESEARCH_DOSSIER_JSON_BEGIN",
                "{}",
                "E2R_RESEARCH_DOSSIER_JSON_END",
            )
        )
        snapshot = BrowserResultSnapshot(
            conversation_id="canonical-conversation-1234",
            assistant_turn_id="assistant-final",
            report_text=report_text,
            report_hash="a" * 64,
            has_citations=False,
            has_dossier_marker=True,
            job_marker_matches=True,
            run_marker_matches=True,
            new_attachment_keys=(),
        )

        class FakeAdapter:
            recovery_count = 0
            submit_count = 0

            async def recover_conversation_without_submit(self, **kwargs):
                self.recovery_count += 1
                if kwargs["job_id"] != running.job_id:
                    raise AssertionError("wrong recovery job")
                return RecoveredBrowserConversation(
                    conversation_id="canonical-conversation-1234",
                    inspection=BrowserInspection(
                        state=BrowserUIState.READY_FOR_INPUT,
                        conversation_id="canonical-conversation-1234",
                        editor_ready=True,
                        deep_research_ready=True,
                        packet_uploaded=False,
                        prompt_ready=False,
                        send_ready=False,
                        stop_visible=False,
                    ),
                    result=snapshot,
                    search_query="검증기업",
                    result_href="/c/canonical-conversation-1234",
                )

        adapter = FakeAdapter()

        class FakePage:
            async def screenshot(self, **_kwargs):
                raise TimeoutError("optional screenshot renderer timeout")

        class FakeSession:
            def __init__(self):
                self.adapter = adapter
                self.page = FakePage()

            async def close(self):
                return None

        class FakeWorker:
            def __init__(self, _config):
                pass

            async def open(self, *, job_id):
                if job_id != running.job_id:
                    raise AssertionError("wrong worker job")
                return FakeSession()

        config = ProFirstLocalConfig(
            runtime_root=self.runtime,
            dashboard=ProDashboardRuntimeConfig(),
            scheduler=ProScheduleRuntimeConfig(),
            browser=ProBrowserConfig(),
            scan=ProScanRuntimeConfig(),
            supplement=ProSupplementRuntimeConfig(),
            authority=ProAuthorityRuntimeConfig(),
        )
        with patch("e2r.pro_first.operations.ProBrowserWorker", FakeWorker):
            recovered = asyncio.run(
                recover_submitted_v2_job_in_logged_in_browser(
                    self.store,
                    job_id=running.job_id,
                    config=config,
                    repo_root=self.root,
                    search_terms=("검증기업",),
                )
            )

        self.assertEqual(adapter.recovery_count, 1)
        self.assertEqual(adapter.submit_count, 0)
        self.assertEqual(recovered.receipt["recovery_submit_count"], 0)
        self.assertEqual(recovered.job.submit_count, 1)
        self.assertEqual(recovered.job.status, JobStatus.RESEARCH_RUNNING.value)
        self.assertEqual(
            recovered.job.conversation_id,
            "canonical-conversation-1234",
        )
        self.assertEqual(
            recovered.prompt.prompt_hash,
            built.prompt.prompt_hash,
        )

        attention = self.store.transition(
            recovered.job.job_id,
            expected_version=recovered.job.state_version,
            to_status=JobStatus.USER_ATTENTION_REQUIRED,
            actor="test-import-failure",
            idempotency_key="captured-import-failure",
            updates={
                "capture_count": 1,
                "last_error_class": "DOSSIER_INVALID",
                "last_error_message": "compact dialect retry fixture",
            },
        )
        with patch("e2r.pro_first.operations.ProBrowserWorker", FakeWorker):
            captured_retry = asyncio.run(
                recover_submitted_v2_job_in_logged_in_browser(
                    self.store,
                    job_id=attention.job_id,
                    config=config,
                    repo_root=self.root,
                    search_terms=("검증기업",),
                    screenshot_path=self.root / "private/recovery.png",
                )
            )
        self.assertEqual(adapter.recovery_count, 2)
        self.assertEqual(captured_retry.job.status, JobStatus.USER_ATTENTION_REQUIRED.value)
        self.assertEqual(captured_retry.job.submit_count, 1)
        self.assertEqual(captured_retry.job.capture_count, 1)
        self.assertTrue(captured_retry.receipt["capture_reused"])
        self.assertEqual(captured_retry.receipt["recovery_submit_count"], 0)
        self.assertTrue(captured_retry.receipt["screenshot_runtime_only"])
        self.assertEqual(
            captured_retry.receipt["screenshot_status"],
            "OPTIONAL_CAPTURE_FAILED",
        )
        self.assertEqual(
            captured_retry.receipt["screenshot_error_class"],
            "TimeoutError",
        )

    def test_initial_v2_prepare_returns_runtime_without_submitting(self) -> None:
        built = self._build()

        class FakePage:
            url = "https://chatgpt.com/"

            async def goto(self, *_args, **_kwargs):
                raise AssertionError("already-open ChatGPT page must be reused")

        class FakeAdapter:
            submit_count = 0

            async def prepare_without_submit(inner_self, **kwargs):
                self.assertEqual(
                    Path(kwargs["packet_path"]),
                    built.packet_bundle.research_packet_json,
                )
                self.assertEqual(kwargs["prompt_hash"], built.prompt.prompt_hash)
                return PreparedBrowserJob(
                    browser_session_id=kwargs["browser_session_id"],
                    conversation_id="WEB:prepared-v2",
                    state=BrowserUIState.AWAITING_USER_APPROVAL,
                    packet_path=Path(kwargs["packet_path"]),
                    packet_hash=kwargs["packet_hash"],
                    prompt_hash=kwargs["prompt_hash"],
                    uploaded_filename=Path(kwargs["packet_path"]).name,
                    prompt_preview=kwargs["prompt"][:120],
                    deep_research_ready=True,
                    send_ready=True,
                    preexisting_attachment_keys=(),
                )

        adapter = FakeAdapter()

        class FakeSession:
            browser_session_id = "BROWSER-PREPARE-V2"
            page = FakePage()

            def __init__(inner_self):
                inner_self.adapter = adapter

            async def close(inner_self):
                return None

        class FakeWorker:
            def __init__(inner_self, _config):
                pass

            async def open(inner_self, *, job_id):
                self.assertEqual(job_id, built.job.job_id)
                return FakeSession()

        config = ProFirstLocalConfig(
            runtime_root=self.runtime,
            dashboard=ProDashboardRuntimeConfig(),
            scheduler=ProScheduleRuntimeConfig(),
            browser=ProBrowserConfig(),
            scan=ProScanRuntimeConfig(),
            supplement=ProSupplementRuntimeConfig(),
            authority=ProAuthorityRuntimeConfig(),
        )
        with patch("e2r.pro_first.operations.ProBrowserWorker", FakeWorker):
            prepared = asyncio.run(
                prepare_v2_job_in_logged_in_browser(
                    self.store,
                    job_id=built.job.job_id,
                    config=config,
                    repo_root=self.root,
                )
            )

        self.assertEqual(prepared.job.status, JobStatus.AWAITING_USER_APPROVAL.value)
        self.assertEqual(prepared.job.submit_count, 0)
        self.assertEqual(adapter.submit_count, 0)
        self.assertEqual(
            prepared.receipt["status"],
            "CHATGPT_PRO_V2_PREPARED_AWAITING_APPROVAL",
        )

    def test_effective_dossier_snapshot_is_hash_bound_and_reusable(self) -> None:
        built = self._build()
        job = self._approve_and_mark_running(built)
        orchestrator = ProMultiPassResearchOrchestrator(self.store)
        orchestrator.record_completed_initial_pass(
            job.job_id,
            primary_archetype_ids=(ARCHETYPE,),
            response_hash="d" * 64,
            initial_pass_id=built.initial_pass_id,
        )
        dossier = {
            "job_id": job.job_id,
            "research_pass_id": built.initial_pass_id,
            "material_facts": [],
            "counterfacts": [],
            "resolution_facts": [],
            "question_family_results": [],
            "search_route_receipts": [],
        }
        snapshot_store = ProMultiPassDossierStore(orchestrator.ledger)
        first = snapshot_store.persist(
            job_id=job.job_id,
            pass_id=built.initial_pass_id,
            dossier=dossier,
            job_root=self.runtime / "jobs" / job.job_id,
        )
        second = snapshot_store.persist(
            job_id=job.job_id,
            pass_id=built.initial_pass_id,
            dossier=dossier,
            job_root=self.runtime / "jobs" / job.job_id,
        )
        self.assertEqual(first.record.snapshot_id, second.record.snapshot_id)
        self.assertEqual(first.record.revision_ordinal, 1)
        self.assertEqual(
            load_effective_research_dossier(self.runtime / "jobs" / job.job_id),
            dossier,
        )
        revision_dossier = deepcopy(dossier)
        revision_dossier["material_facts"] = [
            {"dossier_fact_id": "PROFACT-APPEND-ONLY-REVISION"}
        ]
        revision = snapshot_store.persist(
            job_id=job.job_id,
            pass_id=built.initial_pass_id,
            dossier=revision_dossier,
            job_root=self.runtime / "jobs" / job.job_id,
        )
        revision_again = snapshot_store.persist(
            job_id=job.job_id,
            pass_id=built.initial_pass_id,
            dossier=revision_dossier,
            job_root=self.runtime / "jobs" / job.job_id,
        )
        self.assertEqual(revision.record.revision_ordinal, 2)
        self.assertEqual(revision.record.parent_snapshot_id, first.record.snapshot_id)
        self.assertEqual(revision_again.record.snapshot_id, revision.record.snapshot_id)
        self.assertNotEqual(first.path, revision.path)
        self.assertEqual(
            revision.path.name,
            (
                "effective_dossier.r2-"
                f"{revision.record.dossier_hash[:24]}.json"
            ),
        )
        self.assertLess(len(revision.path.name), 64)
        self.assertEqual(
            json.loads(first.path.read_text(encoding="utf-8")),
            dossier,
        )
        self.assertEqual(
            load_effective_research_dossier(self.runtime / "jobs" / job.job_id),
            revision_dossier,
        )
        snapshots = orchestrator.ledger.list_dossier_snapshots(job.job_id)
        self.assertEqual(
            [row.revision_ordinal for row in snapshots],
            [1, 2],
        )
        recovered = _load_recovered_snapshot_state(
            orchestrator.ledger,
            job_id=job.job_id,
            job_root=self.runtime / "jobs" / job.job_id,
        )
        self.assertIsNotNone(recovered)
        recovered_dossier, outcomes = recovered
        self.assertEqual(recovered_dossier, revision_dossier)
        self.assertEqual(len(outcomes), 2)
        self.assertTrue(all(row["recovered_from_durable_snapshot"] for row in outcomes))
        self.assertTrue(
            _has_snapshotted_completed_pass(
                orchestrator.ledger,
                job_id=job.job_id,
                pass_name="INITIAL_FULL_RESEARCH",
            )
        )

    def test_legacy_snapshot_table_migrates_without_rewriting_existing_row(
        self,
    ) -> None:
        path = self.root / "legacy-snapshot.sqlite3"
        connection = sqlite3.connect(path)
        self.addCleanup(connection.close)
        connection.execute("PRAGMA foreign_keys=ON")
        connection.executescript(
            """
            CREATE TABLE pro_research_jobs (job_id TEXT PRIMARY KEY);
            CREATE TABLE pro_research_passes (
                pass_id TEXT PRIMARY KEY,
                job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id)
            );
            CREATE TABLE pro_research_dossier_snapshots (
                snapshot_id TEXT PRIMARY KEY,
                job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
                pass_id TEXT NOT NULL UNIQUE
                    REFERENCES pro_research_passes(pass_id),
                parent_snapshot_id TEXT
                    REFERENCES pro_research_dossier_snapshots(snapshot_id),
                dossier_hash TEXT NOT NULL,
                relative_path TEXT NOT NULL,
                fact_count INTEGER NOT NULL,
                question_count INTEGER NOT NULL,
                route_receipt_count INTEGER NOT NULL,
                created_at TEXT NOT NULL,
                UNIQUE(job_id, dossier_hash)
            );
            CREATE INDEX idx_pro_dossier_snapshots_job_created
                ON pro_research_dossier_snapshots(
                    job_id, created_at, snapshot_id
                );
            INSERT INTO pro_research_jobs VALUES ('JOB-LEGACY');
            INSERT INTO pro_research_passes VALUES ('PASS-LEGACY', 'JOB-LEGACY');
            INSERT INTO pro_research_dossier_snapshots VALUES (
                'SNAPSHOT-LEGACY', 'JOB-LEGACY', 'PASS-LEGACY', NULL,
                'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                'research_passes/01/effective_dossier.json', 97, 28, 98,
                '2026-08-24T00:00:00Z'
            );
            """
        )

        _ensure_dossier_snapshot_revision_schema(connection)

        columns = {
            str(row[1])
            for row in connection.execute(
                "PRAGMA table_info(pro_research_dossier_snapshots)"
            )
        }
        migrated = connection.execute(
            "SELECT * FROM pro_research_dossier_snapshots"
        ).fetchone()
        self.assertIn("revision_ordinal", columns)
        self.assertEqual(migrated[0], "SNAPSHOT-LEGACY")
        self.assertEqual(migrated[3], 1)
        connection.execute(
            """
            INSERT INTO pro_research_dossier_snapshots (
                snapshot_id, job_id, pass_id, revision_ordinal,
                parent_snapshot_id, dossier_hash, relative_path,
                fact_count, question_count, route_receipt_count, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "SNAPSHOT-REVISION-2",
                "JOB-LEGACY",
                "PASS-LEGACY",
                2,
                "SNAPSHOT-LEGACY",
                "b" * 64,
                "research_passes/01/effective_dossier.revision-b.json",
                114,
                28,
                115,
                "2026-08-24T01:00:00Z",
            ),
        )
        self.assertEqual(
            connection.execute(
                "SELECT COUNT(*) FROM pro_research_dossier_snapshots"
            ).fetchone()[0],
            2,
        )
        self.assertEqual(connection.execute("PRAGMA foreign_key_check").fetchall(), [])

    def test_dossier_schema_accepts_canonical_initial_pass_name(self) -> None:
        schema = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "configs/e2r_pro_research_dossier_v2.schema.json"
            ).read_text(encoding="utf-8")
        )
        values = schema["$defs"]["researchPass"]["properties"]["pass_name"]["enum"]
        self.assertIn("INITIAL_FULL_RESEARCH", values)
        self.assertIn("COUNTER_SUPERSESSION_CLOSURE", values)

    def test_recovered_verification_rows_are_hash_bound_to_receipt(self) -> None:
        root = self.root / "verification"
        root.mkdir(parents=True)
        rows = ({"dossier_fact_id": "PROFACT-1", "status": "ACCEPTED_CURRENT"},)
        links = ({"claim_id": "CLAIM-1", "fact_id": "FACT-1"},)
        rejection_classifications: tuple[dict, ...] = ()
        rejections: tuple[dict, ...] = ()
        compilation = {"facts": [], "claim_fact_links": list(links)}
        for name, values in (
            ("source_verifications.jsonl", rows),
            ("rejection_classifications.jsonl", rejection_classifications),
            ("claim_fact_links.jsonl", links),
            ("fact_compilation_rejections.jsonl", rejections),
        ):
            (root / name).write_text(
                "".join(json.dumps(value, sort_keys=True) + "\n" for value in values),
                encoding="utf-8",
            )
        (root / "fact_compilation_receipt.json").write_text(
            json.dumps(compilation),
            encoding="utf-8",
        )
        receipt = {
            "job_id": "JOB-1",
            "dossier_id": "DOSSIER-1",
            "verification_semantics_version": "v7",
            "preflight_receipt_hash": "a" * 64,
        }
        receipt["verification_hash"] = canonical_hash(
            {
                "job_id": receipt["job_id"],
                "dossier_id": receipt["dossier_id"],
                "verification_semantics_version": receipt[
                    "verification_semantics_version"
                ],
                "preflight_receipt_hash": receipt[
                    "preflight_receipt_hash"
                ],
                "verifications": rows,
                "rejection_classifications": rejection_classifications,
                "fact_compilation": compilation,
            }
        )
        recovered = _verification_artifact_rows(
            SimpleNamespace(
                result=None,
                receipt=receipt,
                verification_root=root,
            )
        )
        self.assertEqual(recovered, (rows, links, rejections))

    def test_followup_delta_merges_append_only_into_full_dossier(self) -> None:
        original = _base_v2()
        original["question_family_results"][0]["attempted_source_role_ids"] = [
            "ISSUER_OFFICIAL"
        ]
        response = deepcopy(original)
        response["research_pass_id"] = "PASS-2"
        response["parent_pass_id"] = "PASS-1"
        response["candidate_archetypes"] = []
        response["selected_archetypes"] = []
        response["research_status"] = "NEEDS_VERIFIER_REPAIR"
        changed = deepcopy(original["question_family_results"][0])
        changed["closure_reason"] = "두 번째 pass에서 공개 경로를 추가 확인했다."
        changed["attempted_source_role_ids"] = ["CUSTOMER_PARTNER_OFFICIAL"]
        response["question_family_results"] = [changed]
        response["research_passes"] = [
            {
                "pass_id": "PASS-2",
                "parent_pass_id": "PASS-1",
                "pass_name": "PUBLIC_GAP_CLOSURE",
                "status": "COMPLETE",
                "prompt_hash": "a" * 64,
                "response_hash": "b" * 64,
            }
        ]
        result = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=response,
            validation_context=DossierValidationContext(
                job_id="JOB-V2",
                run_id="RUN-V2",
                target_id="000660",
                as_of_date="2026-08-22",
                conversation_id="CONVERSATION-V2",
                candidate_archetype_ids=(
                    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                ),
                research_pass_id="PASS-2",
                parent_pass_id="PASS-1",
                enforce_parent_pass_id=True,
            ),
        )
        self.assertEqual(len(result.effective_dossier["research_passes"]), 2)
        self.assertEqual(result.updated_question_family_ids, (changed["question_family_id"],))
        self.assertEqual(result.effective_dossier["research_pass_id"], "PASS-2")
        self.assertEqual(
            result.effective_dossier["selected_archetypes"],
            original["selected_archetypes"],
        )
        self.assertEqual(
            result.effective_dossier["research_status"],
            "NEEDS_PUBLIC_GAP_CLOSURE",
        )
        self.assertEqual(
            result.effective_dossier["research_saturation"][
                "pro_reported_followup_research_status"
            ],
            "NEEDS_VERIFIER_REPAIR",
        )
        self.assertEqual(
            result.effective_dossier["question_family_results"][0][
                "attempted_source_role_ids"
            ],
            ["ISSUER_OFFICIAL", "CUSTOMER_PARTNER_OFFICIAL"],
        )

    def test_followup_delta_cannot_rewrite_prior_route_receipt(self) -> None:
        original = _base_v2()
        question = original["question_family_results"][0]
        route = {
            "route_receipt_id": "ROUTE-IMMUTABLE",
            "pass_id": "PASS-1",
            "archetype_id": question["archetype_id"],
            "question_family_id": question["question_family_id"],
            "gap_id": "GAP-1",
            "source_role_id": "ISSUER_OFFICIAL",
            "query_or_navigation_objective": "최초 공식 경로",
            "query_text": "최초 질의",
            "result_count_seen": 0,
            "opened_source_urls": [],
            "accepted_fact_ids": [],
            "rejected_candidate_ids": [],
            "provider_status": "SUCCESS",
            "no_new_route_reason": "결과 없음",
            "performed_at": "2026-08-22T01:00:00Z",
        }
        original["search_route_receipts"] = [route]
        question["search_route_receipt_ids"] = [route["route_receipt_id"]]
        question["attempted_source_role_ids"] = ["ISSUER_OFFICIAL"]
        response = deepcopy(original)
        response["research_pass_id"] = "PASS-2"
        response["parent_pass_id"] = "PASS-1"
        response["research_passes"].append(
            {
                "pass_id": "PASS-2",
                "parent_pass_id": "PASS-1",
                "pass_name": "PUBLIC_GAP_CLOSURE",
                "status": "COMPLETE",
                "prompt_hash": "a" * 64,
                "response_hash": "b" * 64,
            }
        )
        response["search_route_receipts"][0]["query_text"] = "조용히 바꾼 질의"
        with self.assertRaises(DossierDeltaMergeError):
            apply_research_dossier_delta(
                original_dossier=original,
                response_dossier=response,
                validation_context=DossierValidationContext(
                    job_id="JOB-V2",
                    run_id="RUN-V2",
                    target_id="000660",
                    as_of_date="2026-08-22",
                    conversation_id="CONVERSATION-V2",
                    candidate_archetype_ids=(
                        "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    ),
                    research_pass_id="PASS-2",
                    parent_pass_id="PASS-1",
                    enforce_parent_pass_id=True,
                ),
            )

    def test_followup_delta_extends_existing_source_lineage_append_only(self) -> None:
        original = _base_v2()
        original["source_lineages"] = [
            {
                "source_lineage_id": "LINEAGE-1",
                "source_urls": ["https://example.com/old"],
                "canonical_source_urls": ["https://example.com/old"],
                "fact_ids": [],
                "independence_group_id": "ISSUER-1",
                "lineage_subject": "동일 실적 발표 계보",
                "publisher_roster": ["검증대상"],
                "same_fact_reprints_collapsed": ["기존 전재"],
                "lineage_status": "OPEN",
                "status": "ACTIVE",
            }
        ]
        response = deepcopy(original)
        response["research_pass_id"] = "PASS-2"
        response["parent_pass_id"] = "PASS-1"
        response["candidate_archetypes"] = []
        response["selected_archetypes"] = []
        response["source_lineages"] = [
            {
                "source_lineage_id": "LINEAGE-1",
                "source_urls": ["https://example.com/new"],
                "canonical_source_urls": ["https://example.com/new"],
                "fact_ids": [],
                "independence_group_id": "ISSUER-1",
                "lineage_subject": "동일 실적 발표 계보",
                "publisher_roster": ["검증대상"],
                "same_fact_reprints_collapsed": ["새 전재"],
                "lineage_status": "RESOLVED",
                "lineage_operation": "APPEND_UPDATE",
                "status": "ACTIVE",
            }
        ]
        response["research_passes"] = [
            {
                "pass_id": "PASS-2",
                "parent_pass_id": "PASS-1",
                "pass_name": "PUBLIC_GAP_CLOSURE",
                "status": "COMPLETE",
                "prompt_hash": "a" * 64,
                "response_hash": "b" * 64,
            }
        ]

        result = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=response,
            validation_context=DossierValidationContext(
                job_id="JOB-V2",
                run_id="RUN-V2",
                target_id="000660",
                as_of_date="2026-08-22",
                conversation_id="CONVERSATION-V2",
                candidate_archetype_ids=(
                    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                ),
                research_pass_id="PASS-2",
                parent_pass_id="PASS-1",
                enforce_parent_pass_id=True,
            ),
        )
        lineage = result.effective_dossier["source_lineages"][0]
        self.assertEqual(
            lineage["source_urls"],
            ["https://example.com/old", "https://example.com/new"],
        )
        self.assertEqual(lineage["lineage_status"], "RESOLVED")
        self.assertEqual(lineage["lineage_status_history"], ["OPEN", "RESOLVED"])
        self.assertEqual(result.new_source_lineage_ids, ())

    def test_followup_delta_cannot_rebind_existing_source_lineage(self) -> None:
        original = _base_v2()
        original["source_lineages"] = [
            {
                "source_lineage_id": "LINEAGE-1",
                "source_urls": ["https://example.com/old"],
                "fact_ids": [],
                "independence_group_id": "ISSUER-1",
                "lineage_subject": "동일 실적 발표 계보",
                "status": "ACTIVE",
            }
        ]
        response = deepcopy(original)
        response["research_pass_id"] = "PASS-2"
        response["parent_pass_id"] = "PASS-1"
        response["source_lineages"][0]["independence_group_id"] = "OTHER"
        response["research_passes"].append(
            {
                "pass_id": "PASS-2",
                "parent_pass_id": "PASS-1",
                "pass_name": "PUBLIC_GAP_CLOSURE",
                "status": "COMPLETE",
                "prompt_hash": "a" * 64,
                "response_hash": "b" * 64,
            }
        )
        with self.assertRaisesRegex(
            DossierDeltaMergeError,
            "rewrote source lineage identity",
        ):
            apply_research_dossier_delta(
                original_dossier=original,
                response_dossier=response,
                validation_context=DossierValidationContext(
                    job_id="JOB-V2",
                    run_id="RUN-V2",
                    target_id="000660",
                    as_of_date="2026-08-22",
                    conversation_id="CONVERSATION-V2",
                    candidate_archetype_ids=(
                        "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    ),
                    research_pass_id="PASS-2",
                    parent_pass_id="PASS-1",
                    enforce_parent_pass_id=True,
                ),
            )

    def test_live_bound_compiler_is_target_blind_and_source_role_aware(self) -> None:
        dossier, verified = _complete_dossier()
        first = _compile_question_bounds(
            dossier,
            verified_fact_ids=verified,
        )
        changed_target = deepcopy(dossier)
        changed_target["target"] = {
            "target_id": "UNRELATED-TARGET",
            "company_name": "다른 검증기업",
        }
        second = _compile_question_bounds(
            changed_target,
            verified_fact_ids=verified,
        )
        self.assertEqual(first, second)
        self.assertEqual(
            set(first),
            {
                row["question_family_id"]
                for row in dossier["question_family_results"]
            },
        )

    def test_accepted_candidate_roster_requires_compiled_claim_link(self) -> None:
        rows = (
            {
                "dossier_fact_id": "PROFACT-ACCEPTED",
                "status": "ACCEPTED_CURRENT",
                "compiled_claim_id": "CLAIM-ACCEPTED",
            },
            {
                "dossier_fact_id": "PROFACT-COMPILER-REJECTED",
                "status": "ACCEPTED_CURRENT",
                "compiled_claim_id": "CLAIM-REJECTED",
            },
            {
                "dossier_fact_id": "PROFACT-QUOTE-REJECTED",
                "status": "REJECTED_QUOTE_MISMATCH",
                "compiled_claim_id": None,
            },
        )
        accepted = _accepted_dossier_fact_ids(
            rows,
            ({"claim_id": "CLAIM-ACCEPTED", "fact_id": "FACT-1"},),
        )
        self.assertEqual(accepted, ("PROFACT-ACCEPTED",))

    def _approve_and_mark_running(
        self,
        built,
        *,
        conversation_id: str = "CONVERSATION-LIVE-V2",
    ):
        job = self.store.get_job(built.job.job_id)
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="test",
            idempotency_key="browser-preparing",
        )
        job = self.store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id="BROWSER-LIVE-V2",
            conversation_id=conversation_id,
            adapter_name="FakeV2Adapter",
            packet_hash=built.packet_bundle.packet_hash,
            prompt_hash=built.prompt.prompt_hash,
            state={"state": "AWAITING_USER_APPROVAL", "initial_pass_id": built.initial_pass_id},
            actor="test",
            idempotency_key="browser-prepared",
        )
        job, nonce = self.store.issue_approval_nonce(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="approval-issued",
            prompt_hash=built.prompt.prompt_hash,
            expires_at="2026-08-24T01:02:03Z",
        )
        job = self.store.consume_approval_nonce(
            job.job_id,
            nonce,
            expected_version=job.state_version,
            actor="user-approved-in-thread",
            idempotency_key="approval-consumed",
            prompt_hash=built.prompt.prompt_hash,
        )
        job = self.store.claim_submit(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="initial-submit",
        )
        return self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.RESEARCH_RUNNING,
            actor="test",
            idempotency_key="initial-running",
        )


if __name__ == "__main__":
    unittest.main()
