from __future__ import annotations

import hashlib
import inspect
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from e2r.cli.run_e2r_researcher_mode_until_pass import (
    _latest_calendar_trading_candidate,
    _load_prior_no_progress_signature,
    _load_prior_source_transport_work_state,
    _result_source_transport_work_state,
    _run_target_until_semantic_terminal,
    _semantic_signature,
    _source_transport_advanced,
    _source_transport_chain_is_valid,
    _source_transport_snapshot,
    _source_transport_work_state,
    _source_transport_work_summary,
    _terminal_source_snapshot_has_pending_fact_extraction,
    build_parser,
    main as run_researcher_mode_until_pass,
)
from e2r.research import EmptySearchProvider, PageFetcher
from e2r.production.metadata import stable_hash
from e2r.research_brain.researcher_mode import (
    CANONICAL_COMPONENT_ORDER,
    PHASE93_POST_RUN_FAIL,
    PHASE93_POST_RUN_PASS,
    ComponentResearchPlanner,
    CurrentStructuredMaterializationResult,
    CurrentResearcherModeConfig,
    CurrentResearchTarget,
    SourceGraphExplorer,
    OfficialSourceMaterializationResult,
    ResearcherEvidenceFactExtractor,
    ResearcherSourceGraphAcquirer,
    SourceGraphAcquisitionConfig,
    write_source_graph_acquisition_run,
    load_current_research_target_registry,
    load_current_research_targets,
)
from tests.test_e2r_v5_fact_extraction import FactProvider, _document
from tests.test_e2r_v5_researcher_mode import ScriptedResearchProvider
from tests.test_e2r_v5_source_graph_acquisition import SourceBrainProvider
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    _official_gap_reasons,
    _score_gap_context_for_supervisor,
    _source_checkpoint_is_ready_for_readonly_replay,
    _source_checkpoint_needs_fact_extraction_recovery,
    _source_checkpoint_needs_downstream_provider_recovery,
    _load_prior_component_memos,
    _reusable_prior_component_memos,
    _same_lane_structured_cache_roots,
)
from e2r.research_brain.researcher_mode.evidence_fact_extractor import (
    FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED,
)
from e2r.research_brain.researcher_mode.source_graph_explorer import (
    _finalize_checkpoint,
    source_graph_acquisition_safety_critical_counts,
    source_graph_checkpoint_audit_binding,
)

AS_OF_DATE = "2026-06-29"


def _phase94_source_checkpoint(
    *,
    epoch: int,
    resumed_from_checkpoint_id: str | None = None,
    generated_queries=(),
    search_candidates=(),
):
    return _finalize_checkpoint(
        {
            "schema_version": "e2r_v5_source_graph_checkpoint_v1",
            "target_id": "CURRENT-TARGET",
            "target_name": "Current Corp",
            "as_of_date": AS_OF_DATE,
            "mode": "TEST",
            "epoch": epoch,
            "status": "CANDIDATE_RANKING_PENDING",
            "resumed_from_checkpoint_id": resumed_from_checkpoint_id,
            "production_score_authority": False,
            "parser_field_direct_score_authority": False,
            "snippet_evidence_allowed": False,
            "transport_budget_can_complete_research": False,
            "generated_queries": list(generated_queries),
            "search_candidates": list(search_candidates),
            "evidence_documents": [],
            "rejected_documents": [],
            "quarantined_documents": [],
        }
    )


def _bound_no_progress_payload(
    signature: str,
    checkpoint,
):
    snapshot = _source_transport_snapshot(checkpoint)
    return {
        "schema_version": "e2r_v5_phase94_semantic_no_progress_v1",
        "status": "RESEARCH_PENDING_NO_NEW_SEMANTIC_STATE",
        "target_id": "CURRENT-TARGET",
        "as_of_date": AS_OF_DATE,
        "source_checkpoint_binding": snapshot["checkpoint_binding"],
        "semantic_signature": signature,
    }


class Phase94IntegrationProvider:
    provider_name = "PHASE94_INTEGRATION_PROVIDER"

    def __init__(self) -> None:
        self.base = ScriptedResearchProvider()
        self.fact = FactProvider()
        self.calls = []
        self.response_cache_directories = []

    def configure_response_cache(self, directory):
        self.response_cache_directories.append(Path(directory))

    def response_cache_audit(self):
        return {
            "status": "FIXTURE_PROVIDER_CACHE_INTERFACE_ACTIVE",
            "logical_call_count": len(self.calls),
            "transport_call_count": len(self.calls),
            "cache_hit_count": 0,
            "cache_invalid_or_unreadable_count": 0,
            "downstream_semantic_invalidation_count": 0,
            "downstream_semantic_cache_delete_count": 0,
            "downstream_semantic_cache_delete_failure_count": 0,
        }

    def complete(self, *, pass_name, payload):
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if pass_name == "SOURCE_QUERY_GENERATION":
            return {
                "suggested_queries": [],
                "new_source_directions": [],
                "unresolved_research_notes": ["fixture has only official source"],
            }
        if pass_name == "EVIDENCE_FACT_EXTRACTION":
            return self.fact.complete(pass_name=pass_name, payload=payload)
        if pass_name == "RESEARCH_SUPERVISOR_REVIEW":
            raise RuntimeError("fixture supervisor remains pending")
        response = self.base.complete(pass_name=pass_name, payload=payload)
        if pass_name == "COMPONENT_RESEARCH":
            response = {
                **response,
                "source_coverage": list(payload["source_coverage"])[:1],
            }
        return response


class Phase94IntegrationOfficialMaterializer:
    def materialize(self, **kwargs):
        document = dict(
            _document("DOC-OFFICIAL", "ISSUER_PRESENTATION", "ISSUER:example.com")
        )
        document.update(
            target_id=kwargs["target_id"],
            as_of_date=kwargs["as_of_date"],
        )
        return OfficialSourceMaterializationResult(
            target_id=kwargs["target_id"],
            as_of_date=kwargs["as_of_date"],
            status="OFFICIAL_SOURCE_MATERIALIZED",
            evidence_documents=(document,),
            provider_attempts=({"provider_name": "OpenDART", "status": "FETCHED"},),
            structured_payloads=(
                {
                    "provider_name": "CompanyGuide",
                    "provider_content_hash": "a" * 64,
                    "published_at": "2026-06-27",
                    "available_at": "2026-06-27",
                    "canonical_url": "https://example.com/companyguide",
                    "payload": {
                        "CONSENSUS_AS_OF_DATE": "2026/06/27",
                        "EPS": 1000,
                        "FORWARD_PER": 10,
                        "TARGET_PRC": 100000,
                        "CONSENSUS_PROVIDER_COUNT": 12,
                    },
                },
            ),
            pending_reasons=(),
            audit={
                "status": "OFFICIAL_SOURCE_MATERIALIZATION_PASS",
                "critical_counts": {},
                "critical_count_sum": 0,
            },
        )
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeTargetRunner,
    _component_supervisor_feedback_by_component,
    _historical_anchors,
    _load_prior_research_context,
    _structured_result_from_official,
)


class Phase94IntegrationStructuredMaterializer:
    def __init__(self):
        self.calls = []

    def materialize(self, **kwargs):
        self.calls.append(kwargs)
        engine = _structured_result_from_official(
            target=CurrentResearchTarget(
                symbol=kwargs["target_id"], company_name=kwargs["target_name"]
            ),
            as_of_date=kwargs["as_of_date"],
            official=kwargs["official"],
        )
        pending = tuple(
            f"STRUCTURED_ROLE_MISSING:{component_id}:{role}"
            for component_id, roles in engine.missing_roles_by_component.items()
            for role in roles
        )
        return CurrentStructuredMaterializationResult(
            target_id=kwargs["target_id"],
            as_of_date=kwargs["as_of_date"],
            latest_trading_snapshot_date=kwargs[
                "latest_trading_snapshot_date"
            ],
            status="SOURCE_PENDING",
            engine_result=engine,
            fetch_attempts=(),
            payload_manifest=(),
            pending_reasons=pending,
            audit={"status": "FIXTURE_SOURCE_PENDING"},
        )


class E2RV5Phase94RunnerContractTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_issuer_ir_failure_is_preserved_as_official_gap(self):
        official = OfficialSourceMaterializationResult(
            target_id="CURRENT-TARGET",
            as_of_date=AS_OF_DATE,
            status="OFFICIAL_SOURCE_MATERIALIZED",
            evidence_documents=(),
            provider_attempts=(
                {
                    "provider_name": "GenericIssuerProvider",
                    "source_class": "IR",
                    "status": "PROVIDER_FAILED",
                    "counts_as_symbol_evidence": False,
                    "provider_error": "issuer discovery unavailable",
                },
            ),
            structured_payloads=(),
            pending_reasons=(),
            audit={"status": "OFFICIAL_SOURCE_MATERIALIZATION_PASS"},
        )

        reasons = _official_gap_reasons(official)

        self.assertEqual(
            reasons,
            (
                "OFFICIAL_PROVIDER_PENDING:GenericIssuerProvider:"
                "PROVIDER_FAILED:issuer discovery unavailable",
            ),
        )
        self.assertFalse(any("official sources fetched" in row for row in reasons))

    def test_same_lane_cache_roots_require_matching_target_manifest_and_date(self):
        with tempfile.TemporaryDirectory() as directory:
            lane = Path(directory)
            valid = lane / "VALID"
            wrong_date = lane / "WRONG-DATE"
            missing_manifest = lane / "NO-MANIFEST"
            current = lane / "CURRENT"
            for root in (valid, wrong_date, missing_manifest, current):
                (root / "structured_source_cache").mkdir(parents=True)
            (valid / "target_run_manifest.json").write_text(
                json.dumps(
                    {"target_id": "VALID", "as_of_date": "2026-07-12"}
                ),
                encoding="utf-8",
            )
            (wrong_date / "target_run_manifest.json").write_text(
                json.dumps(
                    {
                        "target_id": "WRONG-DATE",
                        "as_of_date": "2026-07-13",
                    }
                ),
                encoding="utf-8",
            )
            (current / "target_run_manifest.json").write_text(
                json.dumps(
                    {"target_id": "CURRENT", "as_of_date": "2026-07-12"}
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                _same_lane_structured_cache_roots(
                    lane,
                    target_id="CURRENT",
                    as_of_date="2026-07-12",
                ),
                (valid / "structured_source_cache",),
            )

    def test_resumed_no_progress_runs_once_then_reuses_semantic_stop(self) -> None:
        signature = "a" * 64
        checkpoint = _phase94_source_checkpoint(epoch=1)
        snapshot = _source_transport_snapshot(checkpoint)
        result = SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            completion_gates={"source_graph_checkpoint_ready": False},
        )

        class Runner:
            def __init__(self) -> None:
                self.calls = 0

            def run_checkpoint(self, **_kwargs):
                self.calls += 1
                return result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_root = root / "CURRENT-TARGET"
            target_root.mkdir(parents=True)
            no_progress_path = (
                target_root / "semantic_no_progress_checkpoint.json"
            )
            no_progress_path.write_text(
                json.dumps(_bound_no_progress_payload(signature, checkpoint)),
                encoding="utf-8",
            )
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    return_value=signature,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

            self.assertIs(returned, result)
            self.assertEqual(runner.calls, 1)
            self.assertEqual(
                json.loads(no_progress_path.read_text(encoding="utf-8"))[
                    "semantic_signature"
                ],
                signature,
            )

    def test_prior_no_progress_signature_requires_exact_source_binding(self) -> None:
        checkpoint = _phase94_source_checkpoint(epoch=1)
        binding = _source_transport_snapshot(checkpoint)["checkpoint_binding"]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "semantic_no_progress_checkpoint.json"
            valid = _bound_no_progress_payload("b" * 64, checkpoint)
            path.write_text(json.dumps(valid), encoding="utf-8")
            self.assertEqual(
                _load_prior_no_progress_signature(
                    path=path,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                    source_checkpoint_binding=binding,
                ),
                "b" * 64,
            )
            self.assertIsNone(
                _load_prior_no_progress_signature(
                    path=path,
                    target_id="OTHER-TARGET",
                    as_of_date=AS_OF_DATE,
                    source_checkpoint_binding=binding,
                )
            )
            self.assertIsNone(
                _load_prior_no_progress_signature(
                    path=path,
                    target_id="CURRENT-TARGET",
                    as_of_date="2026-06-28",
                    source_checkpoint_binding=binding,
                )
            )
            self.assertIsNone(
                _load_prior_no_progress_signature(
                    path=path,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                    source_checkpoint_binding={
                        **binding,
                        "epoch": binding["epoch"] + 1,
                    },
                )
            )
            legacy = {
                key: value
                for key, value in valid.items()
                if key not in {"as_of_date", "source_checkpoint_binding"}
            }
            path.write_text(json.dumps(legacy), encoding="utf-8")
            self.assertIsNone(
                _load_prior_no_progress_signature(
                    path=path,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                    source_checkpoint_binding=binding,
                )
            )
            path.write_text(
                json.dumps({**valid, "semantic_signature": "not-a-sha"}),
                encoding="utf-8",
            )
            self.assertIsNone(
                _load_prior_no_progress_signature(
                    path=path,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                    source_checkpoint_binding=binding,
                )
            )

    def test_resumed_no_progress_allows_recovery_before_new_stop(self) -> None:
        old_signature = "c" * 64
        recovered_signature = "d" * 64
        checkpoint = _phase94_source_checkpoint(epoch=1)
        snapshot = _source_transport_snapshot(checkpoint)
        result = SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            completion_gates={"source_graph_checkpoint_ready": False},
        )

        class Runner:
            def __init__(self) -> None:
                self.calls = 0

            def run_checkpoint(self, **_kwargs):
                self.calls += 1
                return result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_root = root / "CURRENT-TARGET"
            target_root.mkdir(parents=True)
            no_progress_path = (
                target_root / "semantic_no_progress_checkpoint.json"
            )
            no_progress_path.write_text(
                json.dumps(
                    _bound_no_progress_payload(old_signature, checkpoint)
                ),
                encoding="utf-8",
            )
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    side_effect=(recovered_signature, recovered_signature),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

            self.assertEqual(runner.calls, 2)
            self.assertEqual(
                json.loads(no_progress_path.read_text(encoding="utf-8"))[
                    "semantic_signature"
                ],
                recovered_signature,
            )

    def test_readonly_source_replay_allows_one_advance_before_stale_stop(
        self,
    ) -> None:
        signature = "f" * 64
        checkpoint = _phase94_source_checkpoint(epoch=1)
        advanced_checkpoint = _phase94_source_checkpoint(
            epoch=2,
            resumed_from_checkpoint_id=checkpoint["checkpoint_id"],
        )
        snapshot = _source_transport_snapshot(checkpoint)
        advanced_snapshot = _source_transport_snapshot(advanced_checkpoint)
        replayed = SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            completion_gates={"source_graph_checkpoint_ready": True},
            audit={"source_checkpoint_readonly_replayed": True},
        )
        advanced = SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            completion_gates={"source_graph_checkpoint_ready": True},
            audit={"source_checkpoint_readonly_replayed": False},
        )

        class Runner:
            def __init__(self) -> None:
                self.modes = []

            def run_checkpoint(self, **kwargs):
                self.modes.append(kwargs["source_resume_mode"])
                return replayed if len(self.modes) == 1 else advanced

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_root = root / "CURRENT-TARGET"
            target_root.mkdir(parents=True)
            (target_root / "semantic_no_progress_checkpoint.json").write_text(
                json.dumps(_bound_no_progress_payload(signature, checkpoint)),
                encoding="utf-8",
            )
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    return_value=signature,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    side_effect=(snapshot, advanced_snapshot),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

        self.assertIs(returned, advanced)
        self.assertEqual(
            runner.modes,
            ["REUSE_READY_CHECKPOINT", "ADVANCE"],
        )

    def test_until_pass_reuses_terminal_source_until_fact_queue_drains(
        self,
    ) -> None:
        checkpoint = _phase94_source_checkpoint(epoch=1)
        advanced_checkpoint = _phase94_source_checkpoint(
            epoch=2,
            resumed_from_checkpoint_id=checkpoint["checkpoint_id"],
        )
        snapshot = _source_transport_snapshot(checkpoint)
        advanced_snapshot = _source_transport_snapshot(advanced_checkpoint)

        def result(
            *,
            fact_status: str,
            source_status: str,
            fact_recovery_replayed: bool = False,
            complete: bool = False,
        ):
            return SimpleNamespace(
                status=(
                    "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                    if complete
                    else "RESEARCH_CHECKPOINT_PENDING"
                ),
                completion_gates={"source_graph_checkpoint_ready": True},
                source_graph=SimpleNamespace(
                    status=source_status,
                ),
                fact_extraction=SimpleNamespace(
                    status=fact_status,
                    pending_reasons=(
                        (
                            "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                            "StructuredProviderUnavailable:"
                            "COLLABORATION_RESPONSE_PENDING:COLLABREQ-"
                            + "e" * 64,
                        )
                        if fact_status == "FACT_EXTRACTION_PENDING"
                        else ()
                    ),
                ),
                audit={
                    "source_checkpoint_readonly_replayed": not complete,
                    "source_checkpoint_fact_extraction_recovery_replayed": (
                        fact_recovery_replayed
                    ),
                },
            )

        results = (
            result(
                fact_status="FACT_EXTRACTION_PENDING",
                source_status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
            ),
            result(
                fact_status="FACT_EXTRACTION_PENDING",
                source_status="QUERY_GENERATION_PENDING",
                fact_recovery_replayed=True,
            ),
            result(
                fact_status="FACT_EXTRACTION_COMPLETE",
                source_status="QUERY_GENERATION_PENDING",
                fact_recovery_replayed=True,
            ),
            result(
                fact_status="FACT_EXTRACTION_COMPLETE",
                source_status="QUERY_GENERATION_PENDING",
                complete=True,
            ),
        )

        class Runner:
            def __init__(self) -> None:
                self.modes = []

            def run_checkpoint(self, **kwargs):
                self.modes.append(kwargs["source_resume_mode"])
                return results[len(self.modes) - 1]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    side_effect=(
                        "a" * 64,
                        "b" * 64,
                        "c" * 64,
                        "d" * 64,
                    ),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    side_effect=(
                        snapshot,
                        snapshot,
                        snapshot,
                        advanced_snapshot,
                    ),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

        self.assertIs(returned, results[-1])
        self.assertEqual(
            runner.modes,
            [
                "REUSE_READY_CHECKPOINT",
                "REUSE_READY_CHECKPOINT",
                "REUSE_READY_CHECKPOINT",
                "ADVANCE",
            ],
        )
        self.assertTrue(
            _terminal_source_snapshot_has_pending_fact_extraction(
                results[0],
                snapshot["work_state"],
            )
        )
        self.assertTrue(
            _terminal_source_snapshot_has_pending_fact_extraction(
                results[1],
                snapshot["work_state"],
            )
        )
        self.assertFalse(
            _terminal_source_snapshot_has_pending_fact_extraction(
                results[2],
                snapshot["work_state"],
            )
        )
        canonical_refresh = result(
            fact_status="FACT_EXTRACTION_PENDING",
            source_status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
        )
        canonical_refresh.fact_extraction.pending_reasons = (
            FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED,
        )
        self.assertTrue(
            _terminal_source_snapshot_has_pending_fact_extraction(
                canonical_refresh,
                snapshot["work_state"],
            )
        )

    def test_terminal_fact_wait_stops_on_same_semantic_signature(
        self,
    ) -> None:
        checkpoint = _phase94_source_checkpoint(epoch=1)
        snapshot = _source_transport_snapshot(checkpoint)
        pending_result = SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            completion_gates={"source_graph_checkpoint_ready": True},
            source_graph=SimpleNamespace(
                status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
            ),
            fact_extraction=SimpleNamespace(
                status="FACT_EXTRACTION_PENDING",
                pending_reasons=(
                    "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                    "StructuredProviderUnavailable:"
                    "COLLABORATION_RESPONSE_PENDING:COLLABREQ-"
                    + "f" * 64,
                ),
            ),
            audit={
                "source_checkpoint_readonly_replayed": True,
                "source_checkpoint_fact_extraction_recovery_replayed": False,
            },
        )

        class Runner:
            def __init__(self) -> None:
                self.modes = []

            def run_checkpoint(self, **kwargs):
                self.modes.append(kwargs["source_resume_mode"])
                return pending_result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    return_value="a" * 64,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )
        self.assertIs(returned, pending_result)
        self.assertEqual(
            runner.modes,
            ["REUSE_READY_CHECKPOINT", "REUSE_READY_CHECKPOINT"],
        )

    def test_fact_recovery_keeps_non_drained_source_snapshot_frozen(
        self,
    ) -> None:
        checkpoint = _phase94_source_checkpoint(
            epoch=1,
            search_candidates=(
                {
                    "candidate_id": "CANDIDATE-PENDING",
                    "ranking_status": "PENDING",
                    "fetch_status": "NOT_STARTED",
                },
            ),
        )
        snapshot = _source_transport_snapshot(checkpoint)
        pending = SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            completion_gates={"source_graph_checkpoint_ready": False},
            source_graph=SimpleNamespace(
                status="CANDIDATE_RANKING_PENDING",
            ),
            fact_extraction=SimpleNamespace(
                status="FACT_EXTRACTION_PENDING",
                pending_reasons=(
                    "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                    "StructuredProviderUnavailable:"
                    "COLLABORATION_RESPONSE_PENDING:COLLABREQ-"
                    + "f" * 64,
                ),
            ),
            audit={
                "source_checkpoint_readonly_replayed": True,
                "source_checkpoint_fact_extraction_recovery_replayed": True,
            },
        )
        complete = SimpleNamespace(
            status="PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD",
            completion_gates={"source_graph_checkpoint_ready": True},
            source_graph=SimpleNamespace(
                status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
            ),
            fact_extraction=SimpleNamespace(
                status="FACT_EXTRACTION_COMPLETE",
                pending_reasons=(),
            ),
            audit={
                "source_checkpoint_readonly_replayed": True,
                "source_checkpoint_fact_extraction_recovery_replayed": True,
            },
        )

        class Runner:
            def __init__(self) -> None:
                self.modes = []

            def run_checkpoint(self, **kwargs):
                self.modes.append(kwargs["source_resume_mode"])
                return (pending, complete)[len(self.modes) - 1]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    side_effect=("a" * 64, "b" * 64),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    side_effect=(snapshot, snapshot),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

        self.assertIs(returned, complete)
        self.assertEqual(
            runner.modes,
            ["REUSE_READY_CHECKPOINT", "REUSE_READY_CHECKPOINT"],
        )
        self.assertEqual(
            _source_transport_work_summary(snapshot["work_state"])[
                "pending_ranking_count"
            ],
            1,
        )
        self.assertTrue(
            _terminal_source_snapshot_has_pending_fact_extraction(
                pending,
                snapshot["work_state"],
            )
        )

    def test_terminal_fact_wait_does_not_replay_persisted_deferred_audit(
        self,
    ) -> None:
        checkpoint = _phase94_source_checkpoint(epoch=1)
        snapshot = _source_transport_snapshot(checkpoint)
        pending_result = SimpleNamespace(
            status="RESEARCH_CHECKPOINT_PENDING",
            completion_gates={"source_graph_checkpoint_ready": True},
            source_graph=SimpleNamespace(
                status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                audit={
                    "query_generation_deferred_by_candidate_work": True,
                },
            ),
            fact_extraction=SimpleNamespace(
                status="FACT_EXTRACTION_PENDING",
                pending_reasons=(
                    "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                    "StructuredProviderUnavailable:"
                    "COLLABORATION_RESPONSE_PENDING:COLLABREQ-"
                    + "d" * 64,
                ),
            ),
            research_epoch=SimpleNamespace(
                supervisor_review=SimpleNamespace(
                    status="NEXT_RESEARCH_REQUIRED",
                    reasonable_positive_routes_remaining=True,
                    query_direction_briefs=({"objective_id": "OBJ"},),
                    new_source_family_directions=(),
                ),
            ),
            audit={
                "source_checkpoint_readonly_replayed": True,
                "source_checkpoint_fact_extraction_recovery_replayed": False,
            },
        )

        class Runner:
            def __init__(self) -> None:
                self.modes = []

            def run_checkpoint(self, **kwargs):
                self.modes.append(kwargs["source_resume_mode"])
                if len(self.modes) > 2:
                    raise AssertionError(
                        "persisted deferred audit replayed the same checkpoint"
                    )
                return pending_result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    return_value="d" * 64,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )
            no_progress = json.loads(
                (
                    root
                    / "CURRENT-TARGET"
                    / "semantic_no_progress_checkpoint.json"
                ).read_text(encoding="utf-8")
            )

        self.assertIs(returned, pending_result)
        self.assertEqual(
            runner.modes,
            ["REUSE_READY_CHECKPOINT", "REUSE_READY_CHECKPOINT"],
        )
        self.assertEqual(
            no_progress["status"],
            "RESEARCH_PENDING_NO_NEW_SEMANTIC_STATE",
        )

    def test_readonly_source_replay_requires_terminal_source_work(self) -> None:
        ready = {
            "status": "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
            "generated_queries": [
                {"execution_status": "SEARCH_EXECUTED"}
            ],
            "search_candidates": [
                {
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                }
            ],
        }
        self.assertTrue(
            _source_checkpoint_is_ready_for_readonly_replay(ready)
        )
        for mutation in (
            {
                "status": "CANDIDATE_RANKING_PENDING",
            },
            {
                "generated_queries": [{"execution_status": "PENDING"}],
            },
            {
                "search_candidates": [
                    {
                        "ranking_status": "PENDING",
                        "fetch_status": "NOT_STARTED",
                    }
                ],
            },
            {
                "search_candidates": [
                    {
                        "ranking_status": "MATERIAL",
                        "fetch_status": "MATERIAL_PENDING_FETCH",
                    }
                ],
            },
        ):
            candidate = {**ready, **mutation}
            self.assertFalse(
                _source_checkpoint_is_ready_for_readonly_replay(candidate)
            )

    def test_fact_extraction_recovery_freezes_pending_source_snapshot(
        self,
    ) -> None:
        request_id = "COLLABREQ-" + "a" * 64
        checkpoint = {
            "target_id": "CURRENT-TARGET",
            "as_of_date": AS_OF_DATE,
            "status": "QUERY_GENERATION_PENDING",
            "pending_reasons": [
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_id
            ],
            "generated_queries": [
                {"execution_status": "SEARCH_EXECUTED"}
            ],
            "search_candidates": [
                {
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                }
            ],
            "evidence_documents": [
                {"document_id": "DOC-1"},
                {"document_id": "BACKFILL-NOT-DOWNSTREAM"},
            ],
            "production_downstream_document_ids": ["DOC-1"],
        }
        fact_result = {
            "target_id": "CURRENT-TARGET",
            "as_of_date": AS_OF_DATE,
            "status": "FACT_EXTRACTION_PENDING",
            "pending_reasons": [
                "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:"
                "COLLABORATION_RESPONSE_PENDING:COLLABREQ-" + "b" * 64,
                "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                "SGDOC-" + "c" * 24 + ":0/3",
            ],
            "audit": {"input_document_count": 1},
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fact_path = root / "fact_extraction_result.json"
            fact_path.write_text(json.dumps(fact_result), encoding="utf-8")
            self.assertTrue(
                _source_checkpoint_needs_fact_extraction_recovery(
                    root=root,
                    checkpoint=checkpoint,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                )
            )

            recoverable_pending_checkpoints = []
            for pending_reason in (
                checkpoint["pending_reasons"][0] + ":SUFFIX",
                "LLM_RETURNED_NO_NEW_VALID_QUERY",
                "QUERY_PROVIDER_ERROR:SEARCH_PROVIDER_ERROR",
            ):
                recoverable_pending_checkpoints.append(
                    {
                        **checkpoint,
                        "pending_reasons": [pending_reason],
                    }
                )
            recoverable_pending_checkpoints.extend(
                (
                    {
                        **checkpoint,
                        "generated_queries": [
                            {"execution_status": "PENDING"}
                        ],
                    },
                    {
                        **checkpoint,
                        "status": "CANDIDATE_RANKING_PENDING",
                        "search_candidates": [
                            {
                                "ranking_status": "PENDING",
                                "fetch_status": "NOT_STARTED",
                            }
                        ],
                    },
                    {
                        **checkpoint,
                        "search_candidates": [
                            {
                                "ranking_status": "MATERIAL",
                                "fetch_status": "MATERIAL_PENDING_FETCH",
                            }
                        ],
                    },
                )
            )
            for recoverable in recoverable_pending_checkpoints:
                self.assertTrue(
                    _source_checkpoint_needs_fact_extraction_recovery(
                        root=root,
                        checkpoint=recoverable,
                        target_id="CURRENT-TARGET",
                        as_of_date=AS_OF_DATE,
                    )
                )

            invalid_checkpoints = (
                {
                    **checkpoint,
                    "production_downstream_document_ids": [
                        "DOC-1",
                        "DOC-MISSING",
                    ],
                },
                {**checkpoint, "evidence_documents": []},
                {
                    **checkpoint,
                    "status": "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                },
            )
            for invalid in invalid_checkpoints:
                self.assertFalse(
                    _source_checkpoint_needs_fact_extraction_recovery(
                        root=root,
                        checkpoint=invalid,
                        target_id="CURRENT-TARGET",
                        as_of_date=AS_OF_DATE,
                    )
                )

            for key, value in (
                ("status", "FACT_EXTRACTION_COMPLETE"),
                ("target_id", "OTHER-TARGET"),
                ("as_of_date", "2026-06-28"),
            ):
                invalid_fact = {**fact_result, key: value}
                fact_path.write_text(
                    json.dumps(invalid_fact),
                    encoding="utf-8",
                )
                self.assertFalse(
                    _source_checkpoint_needs_fact_extraction_recovery(
                        root=root,
                        checkpoint=checkpoint,
                        target_id="CURRENT-TARGET",
                        as_of_date=AS_OF_DATE,
                    )
                )

            mismatched_roster_fact = {
                **fact_result,
                "audit": {"input_document_count": 2},
            }
            fact_path.write_text(
                json.dumps(mismatched_roster_fact),
                encoding="utf-8",
            )
            self.assertFalse(
                _source_checkpoint_needs_fact_extraction_recovery(
                    root=root,
                    checkpoint=checkpoint,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                )
            )

            for invalid_reason in (
                "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:INVALID_PROVIDER_OUTPUT",
                fact_result["pending_reasons"][0] + ":SUFFIX",
                "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                "SGDOC-" + "c" * 24 + ":0/3",
            ):
                invalid_fact = {
                    **fact_result,
                    "pending_reasons": [invalid_reason],
                }
                fact_path.write_text(
                    json.dumps(invalid_fact),
                    encoding="utf-8",
                )
                self.assertFalse(
                    _source_checkpoint_needs_fact_extraction_recovery(
                        root=root,
                        checkpoint=checkpoint,
                        target_id="CURRENT-TARGET",
                        as_of_date=AS_OF_DATE,
                    )
                )

    def test_pending_source_snapshot_recovers_downstream_provider_before_fetch(
        self,
    ) -> None:
        checkpoint = {
            "status": "CANDIDATE_RANKING_PENDING",
            "generated_queries": [
                {"execution_status": "SEARCH_EXECUTED"}
            ],
            "search_candidates": [
                {
                    "ranking_status": "MATERIAL",
                    "fetch_status": "MATERIAL_PENDING_FETCH",
                }
            ],
            "evidence_documents": [
                {
                    "document_id": "DOC-1",
                    "canonical_url": "https://example.com/report.pdf",
                    "content_type": "application/pdf",
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fact_result = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": AS_OF_DATE,
                "status": "FACT_EXTRACTION_COMPLETE",
                "document_dispositions": [
                    {
                        "document_id": "DOC-1",
                        "status": "FACTS_EXTRACTED",
                    }
                ],
                "audit": {
                    "critical_count_sum": 0,
                    "input_document_count": 1,
                },
            }
            dossier = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": AS_OF_DATE,
                "business_model_result": {
                    "status": "PENDING",
                    "pending_reasons": [
                        "PROVIDER_ERROR:CUDA error"
                    ],
                },
                "component_results": [],
                "red_team_result": None,
            }
            (root / "fact_extraction_result.json").write_text(
                json.dumps(fact_result),
                encoding="utf-8",
            )
            (root / "researcher_mode_dossier.json").write_text(
                json.dumps(dossier),
                encoding="utf-8",
            )
            self.assertTrue(
                _source_checkpoint_needs_downstream_provider_recovery(
                    root=root,
                    checkpoint=checkpoint,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                )
            )

            dossier["business_model_result"]["pending_reasons"] = [
                "MATERIAL_FACT_GAP_REMAINS"
            ]
            (root / "researcher_mode_dossier.json").write_text(
                json.dumps(dossier),
                encoding="utf-8",
            )
            self.assertFalse(
                _source_checkpoint_needs_downstream_provider_recovery(
                    root=root,
                    checkpoint=checkpoint,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                )
            )

            dossier["business_model_result"]["pending_reasons"] = [
                "PROVIDER_ERROR:CUDA error"
            ]
            fact_result["document_dispositions"][0]["status"] = "UNREADABLE"
            (root / "researcher_mode_dossier.json").write_text(
                json.dumps(dossier),
                encoding="utf-8",
            )
            (root / "fact_extraction_result.json").write_text(
                json.dumps(fact_result),
                encoding="utf-8",
            )
            self.assertFalse(
                _source_checkpoint_needs_downstream_provider_recovery(
                    root=root,
                    checkpoint=checkpoint,
                    target_id="CURRENT-TARGET",
                    as_of_date=AS_OF_DATE,
                )
            )

    def test_completed_resume_removes_stale_no_progress_leaf(self) -> None:
        signature = "e" * 64
        checkpoint = _phase94_source_checkpoint(epoch=1)
        snapshot = _source_transport_snapshot(checkpoint)
        result = SimpleNamespace(
            status="PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD",
            completion_gates={"source_graph_checkpoint_ready": True},
        )

        class Runner:
            def run_checkpoint(self, **_kwargs):
                return result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_root = root / "CURRENT-TARGET"
            target_root.mkdir(parents=True)
            no_progress_path = (
                target_root / "semantic_no_progress_checkpoint.json"
            )
            no_progress_path.write_text(
                json.dumps(_bound_no_progress_payload(signature, checkpoint)),
                encoding="utf-8",
            )
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    return_value=signature,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_prior_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_result_source_transport_work_state",
                    return_value=snapshot,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                _run_target_until_semantic_terminal(
                    runner=Runner(),
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

            self.assertFalse(no_progress_path.exists())

    def test_supervisor_feedback_routes_only_to_its_component_rewrite(self) -> None:
        routed = _component_supervisor_feedback_by_component(
            {
                "review_id": "SUPERVISOR-150",
                "epoch": 150,
                "status": "NEXT_RESEARCH_REQUIRED",
                "component_status": {
                    component_id: "COMPLETE"
                    for component_id in CANONICAL_COMPONENT_ORDER
                },
                "component_findings": [
                    {
                        "component_id": "market_mispricing",
                        "memo_sufficient": False,
                        "rationale": "사실 방향과 서술이 모순된다",
                    },
                    {
                        "component_id": "capital_allocation",
                        "memo_sufficient": True,
                        "rationale": "현재 메모는 충분하다",
                    },
                ],
                "missing_material_facts": [
                    {
                        "component_id": "eps_fcf_explosion",
                        "fact_need": "동일 기간 FCF",
                    }
                ],
                "failure_assessments": [
                    {"failure_type": "GLOBAL_PROVIDER_DIAGNOSTIC"}
                ],
            }
        )

        self.assertEqual(
            set(routed), {"market_mispricing", "eps_fcf_explosion"}
        )
        self.assertEqual(
            routed["market_mispricing"]["component_findings"][0][
                "memo_sufficient"
            ],
            False,
        )
        self.assertEqual(
            routed["eps_fcf_explosion"]["missing_material_facts"][0][
                "fact_need"
            ],
            "동일 기간 FCF",
        )
        self.assertNotIn("failure_assessments", routed["market_mispricing"])
        self.assertNotIn("review_id", routed["market_mispricing"])
        self.assertNotIn("epoch", routed["market_mispricing"])

    def test_component_feedback_projection_ignores_checkpoint_only_churn(self) -> None:
        semantic_context = {
            "status": "NEXT_RESEARCH_REQUIRED",
            "component_status": {
                component_id: "COMPLETE"
                for component_id in CANONICAL_COMPONENT_ORDER
            },
            "component_findings": [
                {
                    "component_id": "market_mispricing",
                    "memo_sufficient": False,
                    "rationale": "같은 사실 방향 모순을 다시 검토한다",
                }
            ],
            "missing_material_facts": [],
        }
        first = _component_supervisor_feedback_by_component(
            {
                **semantic_context,
                "review_id": "SUPERVISOR-206",
                "epoch": 206,
            }
        )
        second = _component_supervisor_feedback_by_component(
            {
                **semantic_context,
                "review_id": "SUPERVISOR-207",
                "epoch": 207,
            }
        )

        self.assertEqual(first, second)
        self.assertEqual(set(first), {"market_mispricing"})

    def test_pending_supervisor_transport_placeholder_does_not_reopen_components(
        self,
    ) -> None:
        routed = _component_supervisor_feedback_by_component(
            {
                "review_id": "RSUP-PENDING-1",
                "status": "NEXT_RESEARCH_REQUIRED",
                "component_status": {
                    component_id: "PENDING"
                    for component_id in CANONICAL_COMPONENT_ORDER
                },
                "component_findings": [],
                "missing_material_facts": [],
                "unresolved_material_questions": [
                    "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                    "COLLABORATION_RESPONSE_PENDING:COLLABREQ-1"
                ],
                "component_memos_sufficient": False,
            }
        )

        self.assertEqual(routed, {})

    def test_complete_prior_memo_reuse_requires_stable_semantic_inputs(
        self,
    ) -> None:
        prior_memos = {
            component_id: {
                "component_id": component_id,
                "research_complete": True,
            }
            for component_id in (
                "eps_fcf_explosion",
                "bottleneck_pricing",
                "capital_allocation",
            )
        }
        facts = (
            {
                "fact_id": "FACT-1",
                "predicate": "free_cash_flow",
                "value": 100,
            },
        )
        structured_records = (
            {
                "record_id": "STRUCT-1",
                "evidence_roles": ["ACTUAL_EARNINGS"],
                "value": 100,
            },
        )
        requirements = {
            component_id: (
                ("ACTUAL_EARNINGS",)
                if component_id == "eps_fcf_explosion"
                else ()
            )
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        actionable = {
            "bottleneck_pricing": {"component_findings": [{}]},
            "capital_allocation": {"component_findings": [{}]},
        }

        reusable = _reusable_prior_component_memos(
            prior_component_memos=prior_memos,
            actionable_feedback_by_component=actionable,
            prior_facts=facts,
            current_facts=facts,
            prior_fact_snapshot_available=True,
            prior_structured_result={
                "records": list(structured_records)
            },
            current_structured_result=SimpleNamespace(
                records=structured_records
            ),
            required_roles_by_component=requirements,
        )
        self.assertEqual(set(reusable), {"eps_fcf_explosion"})

        fact_drift = _reusable_prior_component_memos(
            prior_component_memos=prior_memos,
            actionable_feedback_by_component={},
            prior_facts=facts,
            current_facts=(
                *facts,
                {
                    "fact_id": "FACT-2",
                    "predicate": "capacity",
                    "value": 2,
                },
            ),
            prior_fact_snapshot_available=True,
            prior_structured_result={
                "records": list(structured_records)
            },
            current_structured_result=SimpleNamespace(
                records=structured_records
            ),
            required_roles_by_component=requirements,
        )
        self.assertEqual(fact_drift, {})

        structured_drift = _reusable_prior_component_memos(
            prior_component_memos=prior_memos,
            actionable_feedback_by_component={},
            prior_facts=facts,
            current_facts=facts,
            prior_fact_snapshot_available=True,
            prior_structured_result={
                "records": list(structured_records)
            },
            current_structured_result=SimpleNamespace(
                records=(
                    {
                        **structured_records[0],
                        "value": 200,
                    },
                )
            ),
            required_roles_by_component=requirements,
        )
        self.assertNotIn("eps_fcf_explosion", structured_drift)

    def test_prior_memo_citing_retired_fact_is_not_reused_after_snapshot_stabilizes(
        self,
    ) -> None:
        facts = (
            {
                "fact_id": "FACT-CURRENT",
                "predicate": "free_cash_flow",
                "value": 100,
            },
        )
        prior_memos = {
            "eps_fcf_explosion": {
                "component_id": "eps_fcf_explosion",
                "research_complete": True,
                "positive_fact_ids": ["FACT-RETIRED"],
            },
            "bottleneck_pricing": {
                "component_id": "bottleneck_pricing",
                "research_complete": True,
                "positive_fact_ids": ["FACT-CURRENT"],
                "context_fact_ids": ["FACT-RETIRED-CONTEXT"],
            },
        }
        requirements = {
            component_id: () for component_id in CANONICAL_COMPONENT_ORDER
        }

        reusable = _reusable_prior_component_memos(
            prior_component_memos=prior_memos,
            actionable_feedback_by_component={},
            prior_facts=facts,
            current_facts=facts,
            prior_fact_snapshot_available=True,
            prior_structured_result={"records": []},
            current_structured_result=SimpleNamespace(records=()),
            required_roles_by_component=requirements,
        )

        self.assertNotIn("eps_fcf_explosion", reusable)
        self.assertIn("bottleneck_pricing", reusable)

    def test_query_direction_and_retryable_source_failure_reopen_component(
        self,
    ) -> None:
        routed = _component_supervisor_feedback_by_component(
            {
                "status": "NEXT_RESEARCH_REQUIRED",
                "component_status": {},
                "component_findings": [],
                "missing_material_facts": [],
                "query_direction_briefs": [
                    {
                        "objective_id": "OBJ-BOTTLENECK",
                        "query_brief": "패키징 처리량을 재확인",
                    }
                ],
                "new_source_family_directions": [
                    {
                        "objective_id": "OBJ-EPS",
                        "source_family": "ISSUER_EARNINGS_RELEASE",
                    }
                ],
                "failure_assessments": [
                    {
                        "failure_id": "FAIL-CAPITAL",
                        "objective_id": "OBJ-CAPITAL",
                        "classification": "FETCH_FAILURE",
                        "retryable": True,
                    },
                    {
                        "failure_id": "FAIL-GLOBAL",
                        "classification": "FETCH_FAILURE",
                        "retryable": True,
                    },
                ],
            },
            objective_component_by_id={
                "OBJ-EPS": "eps_fcf_explosion",
                "OBJ-BOTTLENECK": "bottleneck_pricing",
                "OBJ-CAPITAL": "capital_allocation",
            },
        )

        self.assertEqual(
            set(routed),
            {
                "eps_fcf_explosion",
                "bottleneck_pricing",
                "capital_allocation",
            },
        )
        self.assertEqual(
            routed["eps_fcf_explosion"][
                "new_source_family_directions"
            ][0]["objective_id"],
            "OBJ-EPS",
        )
        self.assertEqual(
            routed["bottleneck_pricing"]["query_direction_briefs"][0][
                "objective_id"
            ],
            "OBJ-BOTTLENECK",
        )
        self.assertEqual(
            routed["capital_allocation"]["failure_assessments"][0][
                "failure_id"
            ],
            "FAIL-CAPITAL",
        )

    def test_provider_outage_recovers_only_hash_bound_prior_memo_body(self) -> None:
        memo = {
            "target_id": "CURRENT-TARGET",
            "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "component_id": "eps_fcf_explosion",
            "researcher_role": "EPSFCFResearcher",
            "positive_fact_ids": ["FACT-POS"],
            "counter_fact_ids": ["FACT-COUNTER"],
            "resolution_fact_ids": [],
            "context_fact_ids": [],
            "research_complete": True,
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "research_epoch_checkpoint.json").write_text(
                json.dumps(
                    {
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-06-29",
                        "component_memo_hashes": {
                            "eps_fcf_explosion": stable_hash(memo)
                        },
                    }
                ),
                encoding="utf-8",
            )
            (root / "research_epochs.jsonl").write_text(
                json.dumps(
                    {
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-06-29",
                        "changed_component_memos": [memo],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "component_research_memos.jsonl").write_text(
                json.dumps(
                    {
                        "component_id": "eps_fcf_explosion",
                        "research_status": "PENDING",
                        "pending_reasons": ["PROVIDER_ERROR:usage limit"],
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            recovered = _load_prior_component_memos(
                root=root,
                target_id="CURRENT-TARGET",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                as_of_date="2026-06-29",
            )
            self.assertEqual(recovered, {"eps_fcf_explosion": memo})

            tampered = {**memo, "positive_fact_ids": ["FACT-INVENTED"]}
            (root / "research_epochs.jsonl").write_text(
                json.dumps(
                    {
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-06-29",
                        "changed_component_memos": [tampered],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            self.assertEqual(
                _load_prior_component_memos(
                    root=root,
                    target_id="CURRENT-TARGET",
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    as_of_date="2026-06-29",
                ),
                {},
            )

    def test_master_command_contract_exists_without_low_completion_options(self) -> None:
        parser = build_parser()
        option_strings = {
            option
            for action in parser._actions
            for option in action.option_strings
        }
        self.assertTrue(
            {
                "--as-of-date",
                "--symbols",
                "--archetype",
                "--live-materialization-authorized",
                "--checkpoint-resume",
                "--gold-lane-isolated",
                "--require-researcher-parity",
                "--output-root",
            }.issubset(option_strings)
        )
        self.assertFalse(
            any(
                value in option_strings
                for value in (
                    "--max-rounds",
                    "--max-research-iterations",
                    "--max-documents",
                    "--top-results",
                )
            )
        )

    def test_phase94_requires_live_checkpoint_gold_isolation_and_parity(self) -> None:
        base = {
            "as_of_date": "2026-07-12",
            "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "output_root": "/tmp/phase94-contract",
            "live_materialization_authorized": True,
            "checkpoint_resume": True,
            "gold_lane_isolated": True,
            "require_researcher_parity": True,
        }
        config = CurrentResearcherModeConfig(**base)
        self.assertEqual(
            config.source_acquisition_mode,
            "PRODUCTION_DAILY",
        )
        CurrentResearcherModeConfig(
            **base,
            source_acquisition_mode="TEST",
        )
        with self.assertRaisesRegex(ValueError, "backfill"):
            CurrentResearcherModeConfig(
                **base,
                source_acquisition_mode="RESEARCH_BACKFILL",
            )
        for key in (
            "live_materialization_authorized",
            "checkpoint_resume",
            "gold_lane_isolated",
            "require_researcher_parity",
        ):
            invalid = {**base, key: False}
            with self.assertRaises(ValueError):
                CurrentResearcherModeConfig(**invalid)

    def test_target_registry_resolves_master_canaries_without_runner_branch(self) -> None:
        targets = load_current_research_targets(
            symbols=("005930", "000660"),
            as_of_date="2026-07-12",
        )
        self.assertEqual(
            [(row.symbol, row.company_name) for row in targets],
            [("005930", "삼성전자"), ("000660", "SK하이닉스")],
        )
        self.assertEqual(
            targets[0].official_domains,
            (
                "news.samsung.com",
                "samsung.com",
                "irsvc.teletogether.com",
            ),
        )
        self.assertEqual(
            targets[1].official_domains,
            (
                "news.skhynix.com",
                "skhynix.com",
                "news.skhynix.co.kr",
            ),
        )
        before_delegated_service_verification = load_current_research_targets(
            symbols=("005930",),
            as_of_date="2026-07-11",
        )[0]
        self.assertNotIn(
            "irsvc.teletogether.com",
            before_delegated_service_verification.official_domains,
        )
        runner_source = inspect.getsource(CurrentResearcherModeTargetRunner)
        self.assertNotIn("005930", runner_source)
        self.assertNotIn("000660", runner_source)
        self.assertNotIn("삼성전자", runner_source)
        self.assertNotIn("SK하이닉스", runner_source)

        with tempfile.TemporaryDirectory() as directory:
            legacy_registry = Path(directory) / "legacy_targets.json"
            legacy_registry.write_text(
                json.dumps(
                    {
                        "targets": [
                            {
                                "target_id": "CURRENT-LEGACY",
                                "company_name": "Current Legacy",
                                "aliases": ["Legacy Current"],
                                "official_domains": ["current.example"],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            registry_rows = load_current_research_target_registry(
                legacy_registry
            )
            legacy = load_current_research_targets(
                symbols=("CURRENT-LEGACY",),
                registry_path=legacy_registry,
                registry_rows=registry_rows,
            )
            self.assertEqual(
                tuple(
                    row.get("target_id") for row in registry_rows
                ),
                ("CURRENT-LEGACY",),
            )
            self.assertEqual(legacy[0].target_id, "CURRENT-LEGACY")
            self.assertEqual(legacy[0].company_name, "Current Legacy")

    def test_source_graph_has_one_full_thesis_objective_per_component(self) -> None:
        plans = ComponentResearchPlanner().plan(
            target_id="CURRENT",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            evidence_facts=(),
            historical_anchors=(),
        )
        graph = SourceGraphExplorer().explore(
            target_id="CURRENT",
            as_of_date="2026-07-12",
            documents=(),
            research_plans=plans,
            source_coverage=(),
        )
        self.assertEqual(len(graph.open_objectives), 7)
        self.assertEqual(
            {row.component_id for row in graph.open_objectives},
            set(CANONICAL_COMPONENT_ORDER),
        )
        self.assertTrue(all(row.literal_query is None for row in graph.open_objectives))
        self.assertTrue(
            all(row.query_must_be_generated_by_llm for row in graph.open_objectives)
        )

    def test_production_runner_cannot_import_or_read_private_gold(self) -> None:
        source = (
            self.ROOT
            / "src/e2r/research_brain/researcher_mode/current_researcher_mode.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("full_thesis_gold_benchmark", source)
        self.assertNotIn("compare_phase93_gold_post_run", source)
        self.assertNotIn("load_phase93_gold_corpus", source)
        self.assertIn('"gold_visibility": False', source)

    def test_phase94_gold_comparison_runs_only_after_every_production_target_closes(
        self,
    ) -> None:
        targets = tuple(
            SimpleNamespace(target_id=value)
            for value in ("CURRENT-A", "CURRENT-B")
        )

        def execute(
            *,
            second_status: str,
            selected_target_ids: tuple[str, ...] = (
                "CURRENT-A",
                "CURRENT-B",
            ),
        ):
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry_path = root / "target_registry.json"
                registry_path.write_text(
                    json.dumps(
                        {
                            "mandatory_targets": [
                                {
                                    "symbol": target.target_id,
                                    "company_name": target.target_id,
                                }
                                for target in targets
                            ]
                        }
                    ),
                    encoding="utf-8",
                )
                statuses = {
                    "CURRENT-A": (
                        "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                    ),
                    "CURRENT-B": second_status,
                }
                selected_targets = tuple(
                    target
                    for target in targets
                    if target.target_id in selected_target_ids
                )
                runs = tuple(
                    SimpleNamespace(
                        status=statuses[target.target_id],
                        target=target,
                        output_root=root / target.target_id,
                        completion_gates={},
                        score_aggregation=object(),
                        stagecourt=object(),
                    )
                    for target in selected_targets
                )
                order = []
                run_by_id = {
                    run.target.target_id: run for run in runs
                }

                def run_target(**kwargs):
                    target_id = kwargs["target"].target_id
                    order.append(f"production:{target_id}")
                    return run_by_id[target_id]

                def write_lane(**_kwargs):
                    order.append("production_lane_closed")
                    return {"lane": root / "production_lane_manifest.json"}

                def compare(**_kwargs):
                    order.append("post_run_gold_opened")
                    return SimpleNamespace(
                        status=PHASE93_POST_RUN_FAIL,
                        comparisons=(),
                        audit={
                            "critical_counts": {
                                "critical_material_fact_recall_below_threshold_count": 1
                            }
                        },
                    )

                compare_mock = Mock(side_effect=compare)
                with (
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "load_current_research_targets",
                        return_value=selected_targets,
                    ),
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "_build_research_provider",
                        return_value=object(),
                    ),
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "CurrentResearcherModeTargetRunner",
                        return_value=SimpleNamespace(provider=object()),
                    ),
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "_research_provider_manifest",
                        return_value={"provider_name": "TEST"},
                    ),
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "_run_target_until_semantic_terminal",
                        side_effect=run_target,
                    ),
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "write_production_lane",
                        side_effect=write_lane,
                    ),
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "_load_post_run_gold_tools",
                        return_value=(
                            PHASE93_POST_RUN_PASS,
                            compare_mock,
                            Mock(),
                        ),
                    ) as gold_tools_mock,
                    patch(
                        "e2r.cli.run_e2r_researcher_mode_until_pass."
                        "write_canary_post_run_gold_comparison"
                    ),
                    patch("builtins.print"),
                ):
                    exit_code = run_researcher_mode_until_pass(
                        [
                            "--as-of-date",
                            AS_OF_DATE,
                            "--symbols",
                            ",".join(selected_target_ids),
                            "--archetype",
                            "CURRENT-ARCHETYPE",
                            "--live-materialization-authorized",
                            "true",
                            "--checkpoint-resume",
                            "true",
                            "--gold-lane-isolated",
                            "true",
                            "--require-researcher-parity",
                            "true",
                            "--output-root",
                            str(root),
                            "--target-registry",
                            str(registry_path),
                        ]
                    )
                summary = json.loads(
                    (root / "phase94_run_summary.json").read_text(
                        encoding="utf-8"
                    )
                )
                audit_path = root / "post_run_gold_recall_audit.json"
                audit = (
                    json.loads(
                        audit_path.read_text(
                            encoding="utf-8"
                        )
                    )
                    if audit_path.is_file()
                    else None
                )
                return (
                    exit_code,
                    order,
                    compare_mock.call_count,
                    summary,
                    runs,
                    audit,
                    gold_tools_mock.call_count,
                )

        pending = execute(second_status="RESEARCH_CHECKPOINT_PENDING")
        self.assertEqual(pending[0], 2)
        self.assertEqual(pending[2], 0)
        self.assertNotIn("post_run_gold_opened", pending[1])
        self.assertFalse(pending[3]["production_research_complete"])

        partial_complete = execute(
            second_status=(
                "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
            ),
            selected_target_ids=("CURRENT-A",),
        )
        self.assertEqual(partial_complete[0], 2)
        self.assertEqual(partial_complete[2], 0)
        self.assertEqual(partial_complete[6], 0)
        self.assertNotIn("post_run_gold_opened", partial_complete[1])
        self.assertTrue(
            partial_complete[3]["production_research_complete"]
        )
        self.assertFalse(partial_complete[3]["comparison_executed"])
        self.assertEqual(
            partial_complete[3]["post_run_gold_status"],
            "PENDING_FULL_MANDATORY_TARGET_ROSTER",
        )
        self.assertEqual(
            partial_complete[3]["missing_mandatory_target_ids"],
            ["CURRENT-B"],
        )
        self.assertEqual(
            partial_complete[3]["target_statuses"],
            {
                "CURRENT-A": (
                    "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                )
            },
        )
        self.assertFalse(partial_complete[5]["comparison_executed"])
        self.assertEqual(
            partial_complete[5]["missing_target_ids"],
            ["CURRENT-B"],
        )
        self.assertIn(
            "mandatory_targets roster",
            partial_complete[5]["reason"],
        )

        post_run_fail = execute(
            second_status=(
                "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
            )
        )
        self.assertEqual(post_run_fail[0], 2)
        self.assertEqual(post_run_fail[2], 1)
        self.assertEqual(post_run_fail[6], 1)
        self.assertEqual(
            post_run_fail[1],
            [
                "production:CURRENT-A",
                "production:CURRENT-B",
                "production_lane_closed",
                "post_run_gold_opened",
            ],
        )
        self.assertTrue(post_run_fail[3]["production_research_complete"])
        self.assertTrue(post_run_fail[3]["comparison_executed"])
        self.assertTrue(
            post_run_fail[3]["full_mandatory_target_roster_selected"]
        )
        self.assertEqual(
            post_run_fail[3]["post_run_gold_status"],
            PHASE93_POST_RUN_FAIL,
        )
        self.assertTrue(
            all(
                run.status
                == "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                for run in post_run_fail[4]
            )
        )

    def test_partial_subprocess_never_loads_or_reads_gold(self) -> None:
        script = textwrap.dedent(
            """
            import json
            import sys
            import tempfile
            from pathlib import Path
            from types import SimpleNamespace
            from unittest.mock import patch

            gold_module = (
                "e2r.research_brain.researcher_mode."
                "full_thesis_gold_benchmark"
            )
            assert gold_module not in sys.modules
            import e2r.cli.run_e2r_researcher_mode_until_pass as cli
            assert gold_module not in sys.modules

            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = root / "targets.json"
                registry.write_text(
                    json.dumps(
                        {
                            "mandatory_targets": [
                                {
                                    "symbol": "CURRENT-A",
                                    "company_name": "Current A",
                                },
                                {
                                    "symbol": "CURRENT-B",
                                    "company_name": "Current B",
                                },
                            ]
                        }
                    ),
                    encoding="utf-8",
                )
                output_root = root / "output"
                target_root = output_root / "CURRENT-A"
                target_root.mkdir(parents=True)
                stale_gold = target_root / "gold_fact_comparison.jsonl"
                stale_gold.write_text(
                    "{malformed stale Gold",
                    encoding="utf-8",
                )
                original_read_text = Path.read_text
                original_read_bytes = Path.read_bytes

                def guarded_read_text(path, *args, **kwargs):
                    if path == stale_gold:
                        raise AssertionError("partial main read stale Gold")
                    return original_read_text(path, *args, **kwargs)

                def guarded_read_bytes(path, *args, **kwargs):
                    if path == stale_gold:
                        raise AssertionError("partial main hashed stale Gold")
                    return original_read_bytes(path, *args, **kwargs)

                def completed_run(**kwargs):
                    target = kwargs["target"]
                    return SimpleNamespace(
                        status=(
                            "PRODUCTION_RESEARCH_COMPLETE_"
                            "PENDING_POST_RUN_GOLD"
                        ),
                        target=target,
                        output_root=target_root,
                        completion_gates={},
                    )

                with (
                    patch.object(Path, "read_text", guarded_read_text),
                    patch.object(Path, "read_bytes", guarded_read_bytes),
                    patch.object(
                        cli,
                        "_build_research_provider",
                        return_value=object(),
                    ),
                    patch.object(
                        cli,
                        "CurrentResearcherModeTargetRunner",
                        return_value=SimpleNamespace(provider=object()),
                    ),
                    patch.object(
                        cli,
                        "_research_provider_manifest",
                        return_value={"provider_name": "TEST"},
                    ),
                    patch.object(
                        cli,
                        "_run_target_until_semantic_terminal",
                        side_effect=completed_run,
                    ),
                    patch.object(
                        cli,
                        "write_production_lane",
                        return_value={
                            "lane": output_root
                            / "production_lane_manifest.json"
                        },
                    ),
                    patch("builtins.print"),
                ):
                    exit_code = cli.main(
                        [
                            "--as-of-date",
                            "2026-06-29",
                            "--symbols",
                            "CURRENT-A",
                            "--archetype",
                            "CURRENT-ARCHETYPE",
                            "--live-materialization-authorized",
                            "true",
                            "--checkpoint-resume",
                            "true",
                            "--gold-lane-isolated",
                            "true",
                            "--require-researcher-parity",
                            "true",
                            "--output-root",
                            str(output_root),
                            "--target-registry",
                            str(registry),
                        ]
                    )
                assert exit_code == 2
                assert gold_module not in sys.modules
                summary = json.loads(
                    (output_root / "phase94_run_summary.json").read_text(
                        encoding="utf-8"
                    )
                )
                assert summary["production_research_complete"] is True
                assert summary["comparison_executed"] is False
                assert summary["missing_mandatory_target_ids"] == [
                    "CURRENT-B"
                ]
            """
        )
        result = subprocess.run(
            [sys.executable, "-c", script],
            cwd=self.ROOT,
            env={**os.environ, "PYTHONPATH": "src"},
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            result.stdout + result.stderr,
        )

    def test_phase94_output_contract_names_are_present(self) -> None:
        source = (
            self.ROOT
            / "src/e2r/research_brain/researcher_mode/current_researcher_mode.py"
        ).read_text(encoding="utf-8")
        for leaf in (
            "business_model_memo.json",
            "source_graph_checkpoint.json",
            "counterfacts.jsonl",
            "component_research_memos.jsonl",
            "structured_engine_result.json",
            "stagecourt.json",
        ):
            self.assertIn(leaf, source)
        self.assertEqual(
            _latest_calendar_trading_candidate("2026-07-12"),
            "2026-07-10",
        )

    def test_no_progress_signature_ignores_prose_and_source_transport_churn(
        self,
    ) -> None:
        def result(*, question: str, failure_reason: str):
            supervisor = SimpleNamespace(
                status="NEXT_RESEARCH_REQUIRED",
                unresolved_material_questions=(question,),
                next_actions=(f"action for {question}",),
            )
            return SimpleNamespace(
                source_graph=SimpleNamespace(
                    status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                    checkpoint={
                        "generated_queries": [],
                        "search_candidates": [],
                        "query_failures": [
                            {
                                "query_id": "Q1",
                                "candidate_id": "C1",
                                "failure_stage": "FULL_DOCUMENT_FETCH",
                                "failure_reason": failure_reason,
                                "alternate_route_required": True,
                            }
                        ],
                    },
                    evidence_documents=(),
                ),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_COMPLETE",
                    pending_reasons=(),
                    facts=(),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(status="SOURCE_PENDING", records=()),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING", pending_reasons=("SOURCE_PENDING",)
                ),
                research_epoch=SimpleNamespace(supervisor_review=supervisor),
            )

        first = result(question="첫 번째 표현", failure_reason="TLS_FAILURE")
        rephrased = result(question="같은 뜻의 두 번째 표현", failure_reason="TLS_FAILURE")
        changed_failure = result(
            question="같은 뜻의 세 번째 표현",
            failure_reason="HTTP_503_FAILURE",
        )
        parser_noise_first = result(
            question="파서 손상 첫 번째 표현",
            failure_reason=(
                "SNIPPET_ONLY_FULL_FETCH_REQUIRED:live_fetch_unreadable_text:"
                "excessive_control_characters:10/100"
            ),
        )
        parser_noise_second = result(
            question="파서 손상 두 번째 표현",
            failure_reason=(
                "SNIPPET_ONLY_FULL_FETCH_REQUIRED:live_fetch_unreadable_text:"
                "excessive_control_characters:200/2000"
            ),
        )
        self.assertEqual(_semantic_signature(first), _semantic_signature(rephrased))
        self.assertEqual(
            _semantic_signature(parser_noise_first),
            _semantic_signature(parser_noise_second),
        )
        self.assertEqual(
            _semantic_signature(first), _semantic_signature(changed_failure)
        )

    def test_source_transport_progress_recognizes_navigation_backlog_drain(
        self,
    ) -> None:
        before_checkpoint = {
            "generated_queries": [],
            "search_candidates": [
                *[
                    {
                        "candidate_id": f"RANK-{index}",
                        "ranking_status": "PENDING",
                        "fetch_status": "NOT_STARTED",
                    }
                    for index in range(38)
                ],
                *[
                    {
                        "candidate_id": f"FETCH-{index}",
                        "ranking_status": "MATERIAL",
                        "fetch_status": "MATERIAL_PENDING_FETCH",
                    }
                    for index in range(563)
                ],
            ],
        }
        after_checkpoint = {
            "generated_queries": [],
            "search_candidates": [
                *[
                    {
                        "candidate_id": f"RANK-{index}",
                        "ranking_status": (
                            "NOT_MATERIAL" if index < 22 else "PENDING"
                        ),
                        "fetch_status": (
                            "REFERENCE_DISCOVERY_REJECTED_NAVIGATION_ONLY"
                            if index < 22
                            else "NOT_STARTED"
                        ),
                    }
                    for index in range(38)
                ],
                *[
                    {
                        "candidate_id": f"FETCH-{index}",
                        "ranking_status": (
                            "NOT_MATERIAL" if index < 252 else "MATERIAL"
                        ),
                        "fetch_status": (
                            "REFERENCE_DISCOVERY_REJECTED_NAVIGATION_ONLY"
                            if index < 252
                            else "MATERIAL_PENDING_FETCH"
                        ),
                    }
                    for index in range(563)
                ],
            ],
        }
        before = _source_transport_work_state(before_checkpoint)
        after = _source_transport_work_state(after_checkpoint)
        bound_before_checkpoint = _phase94_source_checkpoint(
            epoch=1,
            search_candidates=before_checkpoint["search_candidates"],
        )
        bound_after_checkpoint = _phase94_source_checkpoint(
            epoch=2,
            resumed_from_checkpoint_id=(
                bound_before_checkpoint["checkpoint_id"]
            ),
            search_candidates=after_checkpoint["search_candidates"],
        )
        bound_before = _source_transport_snapshot(bound_before_checkpoint)
        bound_after = _source_transport_snapshot(bound_after_checkpoint)

        self.assertEqual(
            _source_transport_work_summary(before),
            {
                "pending_query_count": 0,
                "pending_ranking_count": 38,
                "pending_fetch_count": 563,
                "state_hash": stable_hash(before),
            },
        )
        self.assertEqual(
            _source_transport_work_summary(after),
            {
                "pending_query_count": 0,
                "pending_ranking_count": 16,
                "pending_fetch_count": 311,
                "state_hash": stable_hash(after),
            },
        )
        self.assertTrue(_source_transport_advanced(before, after))
        self.assertTrue(
            _source_transport_chain_is_valid(
                bound_before,
                bound_after,
                readonly_replayed=False,
            )
        )
        self.assertTrue(
            _source_transport_advanced(
                bound_before["work_state"],
                bound_after["work_state"],
            )
        )

    def test_source_transport_progress_recognizes_each_forward_transition(
        self,
    ) -> None:
        transitions = (
            (
                {
                    "generated_queries": [
                        {"query_id": "QUERY", "execution_status": "PENDING"}
                    ]
                },
                {
                    "generated_queries": [
                        {
                            "query_id": "QUERY",
                            "execution_status": "SEARCH_EXECUTED",
                        }
                    ]
                },
            ),
            (
                {
                    "search_candidates": [
                        {
                            "candidate_id": "CANDIDATE",
                            "ranking_status": "PENDING",
                            "fetch_status": "NOT_STARTED",
                        }
                    ]
                },
                {
                    "search_candidates": [
                        {
                            "candidate_id": "CANDIDATE",
                            "ranking_status": "MATERIAL",
                            "fetch_status": "MATERIAL_PENDING_FETCH",
                        }
                    ]
                },
            ),
            (
                {
                    "search_candidates": [
                        {
                            "candidate_id": "CANDIDATE",
                            "ranking_status": "MATERIAL",
                            "fetch_status": "FETCH_RETRY_PENDING",
                        }
                    ]
                },
                {
                    "search_candidates": [
                        {
                            "candidate_id": "CANDIDATE",
                            "ranking_status": "MATERIAL",
                            "fetch_status": "FULL_DOCUMENT_FETCHED",
                        }
                    ]
                },
            ),
        )
        for before_checkpoint, after_checkpoint in transitions:
            with self.subTest(before=before_checkpoint):
                self.assertTrue(
                    _source_transport_advanced(
                        _source_transport_work_state(before_checkpoint),
                        _source_transport_work_state(after_checkpoint),
                    )
                )

    def test_source_transport_progress_ignores_attempt_failure_and_document_churn(
        self,
    ) -> None:
        before = _source_transport_work_state(
            {
                "generated_queries": [
                    {
                        "query_id": "QUERY",
                        "execution_status": "PENDING",
                        "attempt_id": "ATTEMPT-1",
                    }
                ],
                "search_candidates": [
                    {
                        "candidate_id": "CANDIDATE",
                        "ranking_status": "MATERIAL",
                        "fetch_status": "FETCH_RETRY_PENDING",
                        "full_fetch_attempt_count": 1,
                    }
                ],
                "query_failures": [{"failure_id": "FAILURE-1"}],
                "evidence_documents": [{"document_id": "DOCUMENT-1"}],
            }
        )
        after = _source_transport_work_state(
            {
                "generated_queries": [
                    {
                        "query_id": "QUERY",
                        "execution_status": "PENDING",
                        "attempt_id": "ATTEMPT-2",
                    }
                ],
                "search_candidates": [
                    {
                        "candidate_id": "CANDIDATE",
                        "ranking_status": "MATERIAL",
                        "fetch_status": "FETCH_RETRY_PENDING",
                        "full_fetch_attempt_count": 99,
                    }
                ],
                "query_failures": [{"failure_id": "FAILURE-2"}],
                "evidence_documents": [{"document_id": "DOCUMENT-2"}],
            }
        )
        self.assertEqual(before, after)
        self.assertFalse(_source_transport_advanced(before, after))

    def test_source_transport_progress_rejects_fresh_ids_without_transition(
        self,
    ) -> None:
        before = _source_transport_work_state(
            {
                "generated_queries": [],
                "search_candidates": [
                    {
                        "candidate_id": "EXISTING",
                        "ranking_status": "MATERIAL",
                        "fetch_status": "FULL_DOCUMENT_FETCHED",
                    }
                ],
            }
        )
        after = _source_transport_work_state(
            {
                "generated_queries": [
                    {"query_id": "FRESH-QUERY", "execution_status": "PENDING"}
                ],
                "search_candidates": [
                    {
                        "candidate_id": "EXISTING",
                        "ranking_status": "MATERIAL",
                        "fetch_status": "FULL_DOCUMENT_FETCHED",
                    },
                    {
                        "candidate_id": "FRESH-CANDIDATE",
                        "ranking_status": "PENDING",
                        "fetch_status": "NOT_STARTED",
                    },
                ],
            }
        )
        self.assertFalse(_source_transport_advanced(before, after))

    def test_source_transport_progress_rejects_deleted_pending_rows(self) -> None:
        before = _source_transport_work_state(
            {
                "generated_queries": [
                    {"query_id": "DELETED-QUERY", "execution_status": "PENDING"}
                ],
                "search_candidates": [
                    {
                        "candidate_id": "DELETED-CANDIDATE",
                        "ranking_status": "PENDING",
                        "fetch_status": "NOT_STARTED",
                    }
                ],
            }
        )
        after = _source_transport_work_state(
            {"generated_queries": [], "search_candidates": []}
        )
        self.assertFalse(_source_transport_advanced(before, after))

    def test_source_transport_chain_rejects_wrong_parent_and_allows_replay(
        self,
    ) -> None:
        prior_checkpoint = _phase94_source_checkpoint(epoch=7)
        wrong_parent_checkpoint = _phase94_source_checkpoint(
            epoch=8,
            resumed_from_checkpoint_id="SGCHECK-WRONG-PARENT",
        )
        prior = _source_transport_snapshot(prior_checkpoint)
        wrong_parent = _source_transport_snapshot(wrong_parent_checkpoint)

        self.assertFalse(
            _source_transport_chain_is_valid(
                prior,
                wrong_parent,
                readonly_replayed=False,
            )
        )
        self.assertTrue(
            _source_transport_chain_is_valid(
                prior,
                prior,
                readonly_replayed=True,
            )
        )
        self.assertFalse(
            _source_transport_chain_is_valid(
                prior,
                wrong_parent,
                readonly_replayed=True,
            )
        )

    def test_result_source_transport_requires_target_date_and_hash(self) -> None:
        checkpoint = _phase94_source_checkpoint(epoch=1)
        result = SimpleNamespace(
            source_graph=SimpleNamespace(checkpoint=checkpoint)
        )
        self.assertEqual(
            _result_source_transport_work_state(
                result,
                target_id="CURRENT-TARGET",
                as_of_date=AS_OF_DATE,
            )["checkpoint_binding"]["checkpoint_id"],
            checkpoint["checkpoint_id"],
        )
        with self.assertRaises(ValueError):
            _result_source_transport_work_state(
                result,
                target_id="CURRENT-TARGET",
                as_of_date="2026-06-28",
            )
        tampered = dict(checkpoint)
        tampered["epoch"] = 99
        with self.assertRaises(ValueError):
            _result_source_transport_work_state(
                SimpleNamespace(
                    source_graph=SimpleNamespace(checkpoint=tampered)
                ),
                target_id="CURRENT-TARGET",
                as_of_date=AS_OF_DATE,
            )

    def test_source_transport_baseline_requires_valid_target_bound_checkpoint(
        self,
    ) -> None:
        checkpoint = _finalize_checkpoint(
            {
                "schema_version": "e2r_v5_source_graph_checkpoint_v1",
                "target_id": "CURRENT-TARGET",
                "target_name": "Current Corp",
                "as_of_date": "2026-06-29",
                "mode": "TEST",
                "epoch": 1,
                "status": "CANDIDATE_RANKING_PENDING",
                "production_score_authority": False,
                "parser_field_direct_score_authority": False,
                "snippet_evidence_allowed": False,
                "transport_budget_can_complete_research": False,
                "generated_queries": [
                    {"query_id": "QUERY", "execution_status": "PENDING"}
                ],
                "search_candidates": [],
                "evidence_documents": [],
                "rejected_documents": [],
                "quarantined_documents": [],
            }
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source_graph_checkpoint.json"
            path.write_text(json.dumps(checkpoint), encoding="utf-8")
            state = _load_prior_source_transport_work_state(
                path=path,
                target_id="CURRENT-TARGET",
                as_of_date="2026-06-29",
            )
            self.assertEqual(
                _source_transport_work_summary(state["work_state"]),
                {
                    "pending_query_count": 1,
                    "pending_ranking_count": 0,
                    "pending_fetch_count": 0,
                    "state_hash": stable_hash(state["work_state"]),
                },
            )
            self.assertIsNone(
                _load_prior_source_transport_work_state(
                    path=path,
                    target_id="OTHER-TARGET",
                    as_of_date="2026-06-29",
                )
            )
            self.assertIsNone(
                _load_prior_source_transport_work_state(
                    path=path,
                    target_id="CURRENT-TARGET",
                    as_of_date="2026-06-28",
                )
            )
            tampered = dict(checkpoint)
            tampered["status"] = "STOPPED_ON_RESOLUTION"
            path.write_text(json.dumps(tampered), encoding="utf-8")
            self.assertIsNone(
                _load_prior_source_transport_work_state(
                    path=path,
                    target_id="CURRENT-TARGET",
                    as_of_date="2026-06-29",
                )
            )

    def test_repeated_semantics_continue_only_for_existing_work_transition(
        self,
    ) -> None:
        signature = "9" * 64

        def result(checkpoint):
            return SimpleNamespace(
                status="RESEARCH_CHECKPOINT_PENDING",
                completion_gates={"source_graph_checkpoint_ready": False},
                audit={"source_checkpoint_readonly_replayed": False},
                source_graph=SimpleNamespace(checkpoint=checkpoint),
            )

        baseline_checkpoint = _phase94_source_checkpoint(
            epoch=1,
            search_candidates=(
                {
                    "candidate_id": "EXISTING",
                    "ranking_status": "PENDING",
                    "fetch_status": "NOT_STARTED",
                },
            ),
        )
        fetch_checkpoint = _phase94_source_checkpoint(
            epoch=2,
            resumed_from_checkpoint_id=baseline_checkpoint["checkpoint_id"],
            search_candidates=(
                {
                    "candidate_id": "EXISTING",
                    "ranking_status": "MATERIAL",
                    "fetch_status": "MATERIAL_PENDING_FETCH",
                },
            ),
        )
        terminal_checkpoint = _phase94_source_checkpoint(
            epoch=3,
            resumed_from_checkpoint_id=fetch_checkpoint["checkpoint_id"],
            search_candidates=(
                {
                    "candidate_id": "EXISTING",
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                },
            ),
        )
        fresh_only_checkpoint = _phase94_source_checkpoint(
            epoch=4,
            resumed_from_checkpoint_id=terminal_checkpoint["checkpoint_id"],
            generated_queries=(
                {
                    "query_id": "FRESH-QUERY",
                    "execution_status": "PENDING",
                },
            ),
            search_candidates=(
                {
                    "candidate_id": "EXISTING",
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                },
            ),
        )
        results = tuple(
            result(checkpoint)
            for checkpoint in (
                fetch_checkpoint,
                terminal_checkpoint,
                fresh_only_checkpoint,
            )
        )

        class Runner:
            def __init__(self) -> None:
                self.calls = []

            def run_checkpoint(self, **kwargs):
                self.calls.append(kwargs["source_resume_mode"])
                return results[len(self.calls) - 1]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_root = root / "CURRENT-TARGET"
            target_root.mkdir(parents=True)
            no_progress_path = (
                target_root / "semantic_no_progress_checkpoint.json"
            )
            (target_root / "source_graph_checkpoint.json").write_text(
                json.dumps(baseline_checkpoint),
                encoding="utf-8",
            )
            no_progress_path.write_text(
                json.dumps(
                    _bound_no_progress_payload(
                        signature,
                        baseline_checkpoint,
                    )
                ),
                encoding="utf-8",
            )
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    return_value=signature,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

            self.assertIs(returned, results[-1])
            self.assertEqual(
                runner.calls,
                ["REUSE_READY_CHECKPOINT", "ADVANCE", "ADVANCE"],
            )
            progress = json.loads(
                (target_root / "until_pass_progress.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertFalse(progress["source_transport_advanced"])
            self.assertTrue(progress["source_transport_chain_valid"])
            self.assertEqual(
                progress["source_checkpoint_binding"]["checkpoint_id"],
                fresh_only_checkpoint["checkpoint_id"],
            )
            self.assertEqual(
                set(progress["source_transport_work"]),
                {
                    "pending_query_count",
                    "pending_ranking_count",
                    "pending_fetch_count",
                    "state_hash",
                },
            )
            self.assertNotIn("FRESH-QUERY", json.dumps(progress))
            self.assertEqual(
                json.loads(no_progress_path.read_text(encoding="utf-8"))[
                    "semantic_signature"
                ],
                signature,
            )

    def test_repeated_semantics_grant_deferred_query_planner_one_turn(
        self,
    ) -> None:
        signature = "8" * 64

        def result(checkpoint, *, deferred: bool):
            return SimpleNamespace(
                status="RESEARCH_CHECKPOINT_PENDING",
                completion_gates={"source_graph_checkpoint_ready": True},
                audit={"source_checkpoint_readonly_replayed": False},
                source_graph=SimpleNamespace(
                    checkpoint=checkpoint,
                    audit={
                        "query_generation_deferred_by_candidate_work": deferred
                    },
                ),
                research_epoch=SimpleNamespace(
                    supervisor_review=SimpleNamespace(
                        status="NEXT_RESEARCH_REQUIRED",
                        reasonable_positive_routes_remaining=True,
                        query_direction_briefs=({"objective_id": "OBJ"},),
                        new_source_family_directions=(),
                    )
                ),
            )

        baseline = _phase94_source_checkpoint(epoch=1)
        reference_drained = _phase94_source_checkpoint(
            epoch=2,
            resumed_from_checkpoint_id=baseline["checkpoint_id"],
        )
        planner_attempted = _phase94_source_checkpoint(
            epoch=3,
            resumed_from_checkpoint_id=reference_drained["checkpoint_id"],
        )
        results = (
            result(reference_drained, deferred=True),
            result(planner_attempted, deferred=False),
        )

        class Runner:
            def __init__(self) -> None:
                self.calls = []

            def run_checkpoint(self, **kwargs):
                self.calls.append(kwargs["source_resume_mode"])
                return results[len(self.calls) - 1]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_root = root / "CURRENT-TARGET"
            target_root.mkdir(parents=True)
            (target_root / "source_graph_checkpoint.json").write_text(
                json.dumps(baseline),
                encoding="utf-8",
            )
            (
                target_root / "semantic_no_progress_checkpoint.json"
            ).write_text(
                json.dumps(_bound_no_progress_payload(signature, baseline)),
                encoding="utf-8",
            )
            runner = Runner()
            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_signature",
                    return_value=signature,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_semantic_state",
                    return_value={},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "refresh_canary_target_manifest_hash"
                ),
            ):
                returned = _run_target_until_semantic_terminal(
                    runner=runner,
                    config=SimpleNamespace(
                        output_root=str(root),
                        as_of_date=AS_OF_DATE,
                    ),
                    target=SimpleNamespace(target_id="CURRENT-TARGET"),
                )

            self.assertIs(returned, results[-1])
            self.assertEqual(runner.calls, ["REUSE_READY_CHECKPOINT", "ADVANCE"])
            pending = json.loads(
                (
                    target_root / "semantic_no_progress_checkpoint.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(pending["semantic_signature"], signature)

    def test_no_progress_signature_ignores_attempt_ids_without_new_facts(
        self,
    ) -> None:
        def result(
            *,
            literal_query: str,
            query_id: str,
            candidate_id: str,
            document_id: str,
            fact_ids: tuple[str, ...] = (),
            failure_count: int = 1,
        ):
            supervisor = SimpleNamespace(status="NEXT_RESEARCH_REQUIRED")
            return SimpleNamespace(
                source_graph=SimpleNamespace(
                    status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                    checkpoint={
                        "generated_queries": [
                            {
                                "query_id": query_id,
                                "literal_query": literal_query,
                                "execution_status": "EXECUTED",
                            }
                        ],
                        "search_candidates": [
                            {
                                "candidate_id": candidate_id,
                                "ranking_status": "SELECTED",
                                "fetch_status": "FAILED",
                            }
                        ],
                        "query_failures": [
                            {
                                "query_id": f"{query_id}-{index}",
                                "candidate_id": f"{candidate_id}-{index}",
                                "failure_stage": "FULL_DOCUMENT_FETCH",
                                "failure_reason": "TLS_FAILURE",
                                "alternate_route_required": True,
                            }
                            for index in range(failure_count)
                        ],
                    },
                    evidence_documents=(
                        SimpleNamespace(document_id=document_id),
                    ),
                ),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_COMPLETE",
                    pending_reasons=(),
                    facts=tuple(
                        SimpleNamespace(fact_id=fact_id) for fact_id in fact_ids
                    ),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(
                    status="SOURCE_PENDING",
                    records=(),
                ),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING",
                    pending_reasons=("SOURCE_PENDING",),
                ),
                research_epoch=SimpleNamespace(supervisor_review=supervisor),
            )

        first = result(
            literal_query="첫 번째 표현의 동일 연구 질문",
            query_id="Q1",
            candidate_id="C1",
            document_id="D1",
        )
        repeated_attempt = result(
            literal_query="두 번째 표현의 동일 연구 질문",
            query_id="Q2",
            candidate_id="C2",
            document_id="D2",
            failure_count=2,
        )
        material_progress = result(
            literal_query="세 번째 표현의 동일 연구 질문",
            query_id="Q3",
            candidate_id="C3",
            document_id="D3",
            fact_ids=("FACT-NEW",),
        )

        self.assertEqual(
            _semantic_signature(first),
            _semantic_signature(repeated_attempt),
        )
        self.assertNotEqual(
            _semantic_signature(first),
            _semantic_signature(material_progress),
        )

    def test_no_progress_signature_tracks_supervisor_validation_failure_class(
        self,
    ) -> None:
        def result(*, validation_error: str, prose: str):
            return SimpleNamespace(
                source_graph=SimpleNamespace(
                    status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                    checkpoint={
                        "generated_queries": [],
                        "search_candidates": [],
                        "query_failures": [],
                    },
                    evidence_documents=(),
                ),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_COMPLETE",
                    pending_reasons=(),
                    facts=(),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(status="SOURCE_PENDING", records=()),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING", pending_reasons=("SOURCE_PENDING",)
                ),
                research_epoch=SimpleNamespace(
                    supervisor_review=SimpleNamespace(
                        status="NEXT_RESEARCH_REQUIRED",
                        unresolved_material_questions=(
                            "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                            f"StructuredProviderRejected:{validation_error}",
                            prose,
                        ),
                        next_actions=(f"action for {prose}",),
                    )
                ),
            )

        first = result(
            validation_error="component sufficiency contradicts current memos",
            prose="첫 번째 설명",
        )
        rephrased = result(
            validation_error="component sufficiency contradicts current memos",
            prose="표현만 바꾼 두 번째 설명",
        )
        changed_validation = result(
            validation_error="counter supersession completion lacks route proof",
            prose="표현만 바꾼 세 번째 설명",
        )
        self.assertEqual(_semantic_signature(first), _semantic_signature(rephrased))
        self.assertNotEqual(
            _semantic_signature(first),
            _semantic_signature(changed_validation),
        )

    def test_no_progress_signature_normalizes_supervisor_wait_request_id(
        self,
    ) -> None:
        def result(request_id: str):
            wait = (
                "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:"
                "COLLABORATION_RESPONSE_PENDING:"
                f"{request_id}"
            )
            return SimpleNamespace(
                source_graph=SimpleNamespace(
                    status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                    checkpoint={
                        "generated_queries": [],
                        "search_candidates": [],
                        "query_failures": [],
                    },
                    evidence_documents=(),
                ),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_COMPLETE",
                    pending_reasons=(),
                    facts=(),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(status="COMPLETE", records=()),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING",
                    pending_reasons=(wait,),
                ),
                research_epoch=SimpleNamespace(
                    supervisor_review=SimpleNamespace(
                        status="NEXT_RESEARCH_REQUIRED",
                        unresolved_material_questions=(wait,),
                        failure_assessments=(),
                    )
                ),
            )

        first = result("COLLABREQ-" + ("a" * 64))
        second = result("COLLABREQ-" + ("b" * 64))
        self.assertEqual(_semantic_signature(first), _semantic_signature(second))

    def test_no_progress_signature_ignores_duplicate_supervisor_failures(
        self,
    ) -> None:
        def result(*, failure_class: str, failure_count: int):
            failure = {
                "classification": failure_class,
                "retryable": True,
                "source_absence_claim_allowed": False,
            }
            supervisor = SimpleNamespace(
                status="NEXT_RESEARCH_REQUIRED",
                failure_assessments=tuple(
                    dict(failure) for _ in range(failure_count)
                ),
            )
            return SimpleNamespace(
                source_graph=SimpleNamespace(
                    status="EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                    checkpoint={
                        "generated_queries": [],
                        "search_candidates": [],
                        "query_failures": [],
                    },
                    evidence_documents=(),
                ),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_COMPLETE",
                    pending_reasons=(),
                    facts=(),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(
                    status="SOURCE_PENDING",
                    records=(),
                ),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING",
                    pending_reasons=("SOURCE_PENDING",),
                ),
                research_epoch=SimpleNamespace(supervisor_review=supervisor),
            )

        first = result(failure_class="FETCH_FAILURE", failure_count=1)
        repeated = result(failure_class="FETCH_FAILURE", failure_count=20)
        changed = result(failure_class="PARSER_EXTRACTOR_FAILURE", failure_count=1)

        self.assertEqual(
            _semantic_signature(first),
            _semantic_signature(repeated),
        )
        self.assertNotEqual(
            _semantic_signature(first),
            _semantic_signature(changed),
        )

    def test_no_progress_signature_normalizes_usage_limit_transport_noise(self) -> None:
        def result(*, reset_time: str, temp_name: str):
            usage_error = (
                "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:command used "
                f"/tmp/e2r_structured_provider_{temp_name}/output.json; "
                "ERROR: You've hit your usage limit. "
                f"try again at {reset_time}"
            )
            return SimpleNamespace(
                source_graph=SimpleNamespace(
                    status="CANDIDATE_RANKING_PENDING",
                    checkpoint={
                        "generated_queries": [],
                        "search_candidates": [],
                        "query_failures": [],
                    },
                    evidence_documents=(),
                ),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_PENDING",
                    pending_reasons=(usage_error,),
                    facts=(),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(status="SOURCE_PENDING", records=()),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING",
                    pending_reasons=(usage_error,),
                ),
                research_epoch=SimpleNamespace(
                    supervisor_review=SimpleNamespace(status="PROVIDER_PENDING")
                ),
            )

        first = result(
            reset_time="Jul 20th, 2026 3:58 AM",
            temp_name="abc123",
        )
        second = result(
            reset_time="Jul 21st, 2026 4:59 AM",
            temp_name="different456",
        )
        self.assertEqual(_semantic_signature(first), _semantic_signature(second))

    def test_no_progress_signature_normalizes_prompt_size_and_context_noise(
        self,
    ) -> None:
        def result(*, prompt_size: int, context_detail: str):
            pending = (
                "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderRejected:prompt_transport_too_large:"
                f"{prompt_size}:max=1000000",
                "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:"
                f"{context_detail} ERROR: Codex ran out of room in the "
                "model's context window. tokens used 0",
            )
            return SimpleNamespace(
                source_graph=SimpleNamespace(status="SOURCE_PENDING"),
                fact_extraction=SimpleNamespace(
                    status="FACT_EXTRACTION_PENDING",
                    pending_reasons=pending,
                    facts=(),
                ),
                dossier=SimpleNamespace(component_results=()),
                structured_result=SimpleNamespace(
                    status="SOURCE_PENDING",
                    records=(),
                ),
                score_aggregation=SimpleNamespace(
                    status="SCORE_PENDING",
                    pending_reasons=pending,
                ),
                research_epoch=SimpleNamespace(
                    supervisor_review=SimpleNamespace(status="PROVIDER_PENDING")
                ),
            )

        first = result(prompt_size=1092391, context_detail="first prompt body")
        second = result(prompt_size=1178622, context_detail="different prompt body")
        self.assertEqual(_semantic_signature(first), _semantic_signature(second))

    def test_unstructured_roles_are_not_misclassified_as_structured_metrics(self) -> None:
        plans = ComponentResearchPlanner().plan(
            target_id="CURRENT",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            evidence_facts=(),
            historical_anchors=(),
            research_seeds=(),
        )
        by_component = {row.component_id: row for row in plans}
        self.assertNotIn(
            "CUSTOMER_COMMITMENT",
            by_component["earnings_visibility"].structured_metric_requirements,
        )
        self.assertEqual(
            by_component["information_confidence"].structured_metric_requirements,
            (),
        )
        self.assertIn(
            "CURRENT_VALUATION",
            by_component["valuation_rerating"].structured_metric_requirements,
        )

    def test_missing_exact_archetype_anchors_use_generic_ordinal_guards(self) -> None:
        anchors = _historical_anchors(
            repo_root=self.ROOT,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(
            {row["component_id"] for row in anchors},
            set(CANONICAL_COMPONENT_ORDER),
        )
        transfers = [row for row in anchors if row.get("ordinal_transfer_only")]
        self.assertTrue(transfers)
        self.assertTrue(all(row["usable_as_ordinal_anchor"] for row in transfers))
        self.assertTrue(all(not row["usable_as_exact_anchor"] for row in transfers))
        self.assertTrue(all(row["source_proxy_guard_case_ids"] for row in transfers))
        self.assertTrue(all(not row["company_name_conditioned"] for row in transfers))

    def test_pending_checkpoint_writes_honest_full_dossier_without_gold(self) -> None:
        provider = Phase94IntegrationProvider()
        acquirer = ResearcherSourceGraphAcquirer(
            query_provider=provider,
            search_provider=EmptySearchProvider(),
            page_fetcher=PageFetcher(fixture_text_by_url={}),
        )
        structured_materializer = Phase94IntegrationStructuredMaterializer()
        runner = CurrentResearcherModeTargetRunner(
            provider=provider,
            official_materializer=Phase94IntegrationOfficialMaterializer(),
            structured_materializer=structured_materializer,
            source_acquirer=acquirer,
            fact_extractor=ResearcherEvidenceFactExtractor(
                provider=provider,
                documents_per_call=1,
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            config = CurrentResearcherModeConfig(
                as_of_date="2026-06-29",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                output_root=directory,
                live_materialization_authorized=True,
                checkpoint_resume=True,
                gold_lane_isolated=True,
                require_researcher_parity=True,
                latest_trading_snapshot_date="2026-06-29",
                source_acquisition_mode="TEST",
            )
            result = runner.run_checkpoint(
                config=config,
                target=CurrentResearchTarget(
                    symbol="CURRENT-TARGET",
                    company_name="Current Corp",
                    official_domains=("example.com",),
                ),
                repo_root=self.ROOT,
            )
            self.assertEqual(result.status, "RESEARCH_CHECKPOINT_PENDING")
            self.assertEqual(len(result.fact_extraction.facts), 1)
            self.assertFalse(result.score_aggregation.score_valid)
            self.assertEqual(result.structured_result.status, "SOURCE_PENDING")
            expected = {
                "business_model_memo.json",
                "source_graph.json",
                "generated_queries.jsonl",
                "source_graph_evidence_documents.jsonl",
                "evidence_facts.jsonl",
                "counterfacts.jsonl",
                "component_research_memos.jsonl",
                "component_scoring_memos.jsonl",
                "judge_decisions.jsonl",
                "anchor_comparisons.jsonl",
                "component_decisions.jsonl",
                "total_score.json",
                "stagecourt.json",
                "current_researcher_mode_audit.json",
                "research_epochs.jsonl",
                "query_ledger.jsonl",
                "source_graph.jsonl",
                "documents.jsonl",
                "component_judge_decisions.jsonl",
                "historical_anchor_comparisons.jsonl",
                "final_component_decisions.jsonl",
                "score_vector.json",
                "atomic_stage_decision.json",
                "stagecourt_trace.json",
                "canary_leaf_contract_audit.json",
            }
            files = {path.name for path in result.output_root.iterdir() if path.is_file()}
            self.assertTrue(expected.issubset(files))
            audit = json.loads(
                (result.output_root / "current_researcher_mode_audit.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertFalse(audit["gold_visibility"])
            self.assertFalse(audit["completion_based_on_fixed_rounds"])
            self.assertIn(
                "source_graph_checkpoint_ready", audit["completion_gates"]
            )
            self.assertIn("fact_extraction_complete", audit["completion_gates"])
            self.assertFalse(
                audit["completion_gates"]["source_graph_checkpoint_ready"]
            )
            component_payload = next(
                row["payload"]
                for row in provider.calls
                if row["pass_name"] == "COMPONENT_RESEARCH"
            )
            self.assertIn("COMPANYGUIDE", component_payload["source_coverage"])
            query_payload = next(
                row["payload"]
                for row in provider.calls
                if row["pass_name"] == "SOURCE_QUERY_GENERATION"
            )
            self.assertEqual(
                query_payload["score_gap_context"][
                    "verified_official_domain_allowlist"
                ],
                ["example.com"],
            )
            self.assertFalse((result.output_root / "gold_fact_comparison.jsonl").exists())
            leaf_audit = json.loads(
                (result.output_root / "canary_leaf_contract_audit.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(leaf_audit["critical_count_sum"], 0)
            self.assertTrue(result.completion_gates["master_canary_leaf_contract"])
            score_vector = json.loads(
                (result.output_root / "score_vector.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertFalse(score_vector["score_valid"])
            self.assertIsNone(score_vector["component_score_vector"])
            structured_requirements = structured_materializer.calls[-1][
                "required_roles_by_component"
            ]
            self.assertIn(
                "FORWARD_GUIDANCE",
                structured_requirements["eps_fcf_explosion"],
            )
            self.assertIn(
                "DURABLE_VISIBILITY",
                structured_requirements["valuation_rerating"],
            )
            self.assertEqual(
                provider.response_cache_directories[-1],
                result.output_root / "research_provider_response_cache",
            )
            self.assertTrue(
                (
                    result.output_root
                    / "research_provider_response_cache_audit.json"
                ).is_file()
            )

            provider_call_count_before_resume = len(provider.calls)
            runner.run_checkpoint(
                config=config,
                target=CurrentResearchTarget(
                    symbol="CURRENT-TARGET",
                    company_name="Current Corp",
                    official_domains=("example.com",),
                ),
                repo_root=self.ROOT,
            )
            resumed_component_payloads = [
                row["payload"]
                for row in provider.calls[provider_call_count_before_resume:]
                if row["pass_name"] == "COMPONENT_RESEARCH"
            ]
            self.assertEqual(resumed_component_payloads, [])
            resumed_query_payload = [
                row["payload"]
                for row in provider.calls
                if row["pass_name"] == "SOURCE_QUERY_GENERATION"
            ][-1]
            self.assertTrue(
                resumed_query_payload["score_gap_context"][
                    "prior_structured_source_gap"
                ]["missing_roles_by_component"]
            )
            self.assertEqual(
                resumed_query_payload["score_gap_context"][
                    "prior_structured_source_gap"
                ]["query_generation_owner"],
                "LLM",
            )

    def test_query_wait_snapshot_replays_only_to_recover_pending_facts(
        self,
    ) -> None:
        target = CurrentResearchTarget(
            symbol="CURRENT-TARGET",
            company_name="Current Corp",
            official_domains=("example.com",),
        )
        as_of_date = "2026-06-29"
        plans = ComponentResearchPlanner().plan(
            target_id=target.target_id,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            evidence_facts=(),
            historical_anchors=(),
        )
        graph = SourceGraphExplorer().explore(
            target_id=target.target_id,
            as_of_date=as_of_date,
            documents=(),
            research_plans=plans,
            source_coverage=(),
        )
        document = dict(
            _document(
                "DOC-FACT-RECOVERY",
                "ISSUER_PRESENTATION",
                "ISSUER:example.com",
            )
        )
        document.update(
            target_id=target.target_id,
            as_of_date=as_of_date,
            objective_ids=[graph.open_objectives[0].objective_id],
        )
        acquisition_config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_results_per_query=100,
            max_queries_per_checkpoint=10,
            max_candidates_per_checkpoint=100,
            max_fetches_per_checkpoint=20,
        )
        source_run = ResearcherSourceGraphAcquirer(
            query_provider=SourceBrainProvider(),
            search_provider=EmptySearchProvider(),
            page_fetcher=PageFetcher(fixture_text_by_url={}),
        ).acquire(
            config=acquisition_config,
            target_id=target.target_id,
            target_name=target.company_name,
            target_aliases=(),
            as_of_date=as_of_date,
            open_objectives=graph.open_objectives,
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
            official_documents=(document,),
        )
        self.assertEqual(len(source_run.evidence_documents), 1)
        terminal_checkpoint_id = source_run.checkpoint["checkpoint_id"]
        pending_state = json.loads(json.dumps(source_run.checkpoint))
        pending_state.pop("checkpoint_id")
        pending_state.pop("checkpoint_hash")
        pending_state.update(
            epoch=int(pending_state["epoch"]) + 1,
            status="QUERY_GENERATION_PENDING",
            resumed_from_checkpoint_id=terminal_checkpoint_id,
            pending_reasons=[
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                "COLLABREQ-" + "d" * 64
            ],
            production_downstream_document_ids=["DOC-FACT-RECOVERY"],
        )
        pending_checkpoint = _finalize_checkpoint(pending_state)

        class ForbiddenSourceAcquirer:
            def acquire(self, **_kwargs):
                raise AssertionError(
                    "fact recovery replay called source acquisition"
                )

        with tempfile.TemporaryDirectory() as directory:
            target_root = Path(directory) / target.target_id
            target_root.mkdir(parents=True)
            paths = write_source_graph_acquisition_run(
                source_run,
                output_root=target_root,
            )
            paths["checkpoint"].write_text(
                json.dumps(pending_checkpoint),
                encoding="utf-8",
            )
            audit = json.loads(paths["audit"].read_text(encoding="utf-8"))
            critical = source_graph_acquisition_safety_critical_counts(
                config=acquisition_config,
                checkpoint=pending_checkpoint,
            )
            audit.update(
                checkpoint_binding=dict(
                    source_graph_checkpoint_audit_binding(
                        pending_checkpoint
                    )
                ),
                critical_counts=dict(critical),
                critical_count_sum=sum(critical.values()),
            )
            paths["audit"].write_text(
                json.dumps(audit),
                encoding="utf-8",
            )
            (target_root / "fact_extraction_result.json").write_text(
                json.dumps(
                    {
                        "target_id": target.target_id,
                        "as_of_date": as_of_date,
                        "status": "FACT_EXTRACTION_PENDING",
                        "pending_reasons": [
                            FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED
                        ],
                        "audit": {"input_document_count": 1},
                    }
                ),
                encoding="utf-8",
            )
            provider = Phase94IntegrationProvider()
            runner = CurrentResearcherModeTargetRunner(
                provider=provider,
                official_materializer=Phase94IntegrationOfficialMaterializer(),
                structured_materializer=(
                    Phase94IntegrationStructuredMaterializer()
                ),
                source_acquirer=ForbiddenSourceAcquirer(),
                fact_extractor=ResearcherEvidenceFactExtractor(
                    provider=provider,
                    documents_per_call=1,
                ),
            )
            result = runner.run_checkpoint(
                config=CurrentResearcherModeConfig(
                    as_of_date=as_of_date,
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    output_root=directory,
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                    gold_lane_isolated=True,
                    require_researcher_parity=True,
                    latest_trading_snapshot_date=as_of_date,
                    source_acquisition_mode="TEST",
                ),
                target=target,
                repo_root=self.ROOT,
                source_resume_mode="REUSE_READY_CHECKPOINT",
            )

            self.assertTrue(
                result.audit["source_checkpoint_readonly_replayed"]
            )
            self.assertTrue(
                result.audit[
                    "source_checkpoint_fact_extraction_recovery_replayed"
                ]
            )
            self.assertFalse(
                result.audit[
                    "source_checkpoint_downstream_recovery_replayed"
                ]
            )
            self.assertTrue(
                result.source_graph.audit[
                    "fact_extraction_recovery_replay"
                ]
            )
            self.assertEqual(
                result.source_graph.checkpoint["checkpoint_id"],
                pending_checkpoint["checkpoint_id"],
            )
            self.assertTrue(
                any(
                    row["pass_name"] == "EVIDENCE_FACT_EXTRACTION"
                    for row in provider.calls
                )
            )

    def test_ready_source_checkpoint_replays_without_acquisition_mutation(
        self,
    ) -> None:
        target = CurrentResearchTarget(
            symbol="CURRENT-TARGET",
            company_name="Current Corp",
            official_domains=("example.com",),
        )
        as_of_date = "2026-06-29"
        plans = ComponentResearchPlanner().plan(
            target_id=target.target_id,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            evidence_facts=(),
            historical_anchors=(),
        )
        graph = SourceGraphExplorer().explore(
            target_id=target.target_id,
            as_of_date=as_of_date,
            documents=(),
            research_plans=plans,
            source_coverage=(),
        )
        source_provider = SourceBrainProvider()
        source_run = ResearcherSourceGraphAcquirer(
            query_provider=source_provider,
            search_provider=EmptySearchProvider(),
            page_fetcher=PageFetcher(fixture_text_by_url={}),
        ).acquire(
            config=SourceGraphAcquisitionConfig(
                mode="TEST",
                max_queries_per_checkpoint=1,
                max_candidates_per_checkpoint=10,
                max_fetches_per_checkpoint=1,
            ),
            target_id=target.target_id,
            target_name=target.company_name,
            target_aliases=(),
            as_of_date=as_of_date,
            open_objectives=graph.open_objectives,
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
        )
        self.assertEqual(
            source_run.status,
            "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
        )
        self.assertEqual(
            source_run.audit["checkpoint_binding"],
            {
                "target_id": source_run.checkpoint["target_id"],
                "as_of_date": source_run.checkpoint["as_of_date"],
                "checkpoint_id": source_run.checkpoint["checkpoint_id"],
                "checkpoint_hash": source_run.checkpoint["checkpoint_hash"],
                "epoch": source_run.checkpoint["epoch"],
            },
        )

        class ForbiddenSourceAcquirer:
            def acquire(self, **_kwargs):
                raise AssertionError("readonly replay called source acquisition")

        with tempfile.TemporaryDirectory() as directory:
            target_root = Path(directory) / target.target_id
            target_root.mkdir(parents=True)
            paths = write_source_graph_acquisition_run(
                source_run,
                output_root=target_root,
            )
            legacy_audit = json.loads(
                paths["audit"].read_text(encoding="utf-8")
            )
            legacy_audit.pop("checkpoint_binding", None)
            legacy_audit["critical_counts"] = {
                "stale_same_count_external_pass_must_not_be_trusted": 0
            }
            paths["audit"].write_text(
                json.dumps(legacy_audit),
                encoding="utf-8",
            )
            before = {
                name: (path.read_bytes(), path.stat().st_mtime_ns)
                for name, path in paths.items()
            }
            provider = Phase94IntegrationProvider()
            runner = CurrentResearcherModeTargetRunner(
                provider=provider,
                official_materializer=Phase94IntegrationOfficialMaterializer(),
                structured_materializer=(
                    Phase94IntegrationStructuredMaterializer()
                ),
                source_acquirer=ForbiddenSourceAcquirer(),
                fact_extractor=ResearcherEvidenceFactExtractor(
                    provider=provider,
                    documents_per_call=1,
                ),
            )
            result = runner.run_checkpoint(
                config=CurrentResearcherModeConfig(
                    as_of_date=as_of_date,
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    output_root=directory,
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                    gold_lane_isolated=True,
                    require_researcher_parity=True,
                    latest_trading_snapshot_date=as_of_date,
                    source_acquisition_mode="TEST",
                ),
                target=target,
                repo_root=self.ROOT,
                source_resume_mode="REUSE_READY_CHECKPOINT",
            )

            self.assertTrue(
                result.audit["source_checkpoint_readonly_replayed"]
            )
            self.assertEqual(
                result.source_graph.audit["checkpoint_binding_status"],
                "LEGACY_AUDIT_REBOUND_FROM_EXACT_CHECKPOINT_IN_MEMORY",
            )
            self.assertNotIn(
                "stale_same_count_external_pass_must_not_be_trusted",
                result.source_graph.audit["critical_counts"],
            )
            self.assertTrue(
                any(
                    row["pass_name"] == "BUSINESS_MODEL_RESEARCH"
                    for row in provider.calls
                )
            )
            self.assertEqual(
                source_run.checkpoint["checkpoint_id"],
                result.source_graph.checkpoint["checkpoint_id"],
            )
            self.assertEqual(
                source_run.checkpoint["checkpoint_hash"],
                result.source_graph.checkpoint["checkpoint_hash"],
            )
            self.assertEqual(
                source_run.checkpoint["epoch"],
                result.source_graph.checkpoint["epoch"],
            )
            self.assertEqual(
                before,
                {
                    name: (path.read_bytes(), path.stat().st_mtime_ns)
                    for name, path in paths.items()
                },
            )

            other_target = CurrentResearchTarget(
                symbol="OTHER-TARGET",
                company_name="Other Corp",
                official_domains=("example.com",),
            )
            other_root = Path(directory) / other_target.target_id
            other_root.mkdir()
            (other_root / "source_graph_checkpoint.json").write_bytes(
                paths["checkpoint"].read_bytes()
            )
            with self.assertRaisesRegex(ValueError, "target mismatch"):
                runner.run_checkpoint(
                    config=CurrentResearcherModeConfig(
                        as_of_date=as_of_date,
                        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        output_root=directory,
                        live_materialization_authorized=True,
                        checkpoint_resume=True,
                        gold_lane_isolated=True,
                        require_researcher_parity=True,
                        source_acquisition_mode="TEST",
                    ),
                    target=other_target,
                    repo_root=self.ROOT,
                    source_resume_mode="REUSE_READY_CHECKPOINT",
                )

            stale_bound_audit = dict(legacy_audit)
            stale_bound_audit["critical_counts"] = dict(
                result.source_graph.audit["critical_counts"]
            )
            stale_bound_audit["checkpoint_binding"] = {
                **result.source_graph.audit["checkpoint_binding"],
                "epoch": source_run.checkpoint["epoch"] + 1,
            }
            paths["audit"].write_text(
                json.dumps(stale_bound_audit),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "binding mismatch"):
                runner.run_checkpoint(
                    config=CurrentResearcherModeConfig(
                        as_of_date=as_of_date,
                        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        output_root=directory,
                        live_materialization_authorized=True,
                        checkpoint_resume=True,
                        gold_lane_isolated=True,
                        require_researcher_parity=True,
                        source_acquisition_mode="TEST",
                    ),
                    target=target,
                    repo_root=self.ROOT,
                    source_resume_mode="REUSE_READY_CHECKPOINT",
                )

            tampered = json.loads(
                paths["checkpoint"].read_text(encoding="utf-8")
            )
            tampered["status"] = "STOPPED_ON_RESOLUTION"
            paths["checkpoint"].write_text(
                json.dumps(tampered),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                runner.run_checkpoint(
                    config=CurrentResearcherModeConfig(
                        as_of_date=as_of_date,
                        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        output_root=directory,
                        live_materialization_authorized=True,
                        checkpoint_resume=True,
                        gold_lane_isolated=True,
                        require_researcher_parity=True,
                        source_acquisition_mode="TEST",
                    ),
                    target=target,
                    repo_root=self.ROOT,
                    source_resume_mode="REUSE_READY_CHECKPOINT",
                )

    def test_structured_role_gap_keeps_component_objective_open_for_llm_search(
        self,
    ) -> None:
        target_id = "CURRENT-TARGET"
        as_of_date = "2026-06-29"
        objectives = tuple(
            {
                "objective_id": f"OBJECTIVE-{component_id}",
                "component_id": component_id,
            }
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "component_research_memos.jsonl").write_text(
                "\n".join(
                    json.dumps(
                        {
                            "component_id": component_id,
                            "research_complete": True,
                        }
                    )
                    for component_id in CANONICAL_COMPONENT_ORDER
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "structured_engine_result.json").write_text(
                json.dumps(
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "status": "SOURCE_PENDING",
                        "missing_roles_by_component": {
                            "eps_fcf_explosion": ["FORWARD_GUIDANCE"],
                            "market_mispricing": [],
                            "valuation_rerating": ["DURABLE_VISIBILITY"],
                        },
                        "covered_roles_by_component": {
                            "eps_fcf_explosion": ["FREE_CASH_FLOW"]
                        },
                        "component_disposition_by_component": {
                            "eps_fcf_explosion": "PROVIDER_SOURCE_PENDING"
                        },
                    }
                ),
                encoding="utf-8",
            )
            (root / "current_structured_materialization.json").write_text(
                json.dumps(
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "pending_reasons": [
                            "STRUCTURED_ROLE_MISSING:eps_fcf_explosion:FORWARD_GUIDANCE"
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (root / "current_structured_materialization_audit.json").write_text(
                json.dumps(
                    {
                        "issuer_fact_materialization": {
                            "guidance_observation_count": 0,
                            "issuer_source_required_for_segment_and_guidance": True,
                        }
                    }
                ),
                encoding="utf-8",
            )
            (root / "research_epoch_checkpoint.json").write_text(
                json.dumps(
                    {
                        "checkpoint_id": "EPOCH-1",
                        "epoch": 1,
                        "status": "NEXT_RESEARCH_REQUIRED",
                        "unresolved_material_questions": [
                            "issuer forward guidance source is missing"
                        ],
                        "next_actions": ["generate a new source query with the LLM"],
                        "supervisor_review": {
                            "review_id": "SUPERVISOR-1",
                            "epoch": 1,
                            "status": "NEXT_RESEARCH_REQUIRED",
                            "structured_data_complete": False,
                            "query_direction_briefs": [
                                {
                                    "objective_id": "OBJECTIVE-eps_fcf_explosion",
                                    "research_need": "numeric issuer outlook",
                                    "avoid_repeating": [],
                                    "counter_or_supersession": False,
                                }
                            ],
                        },
                    }
                ),
                encoding="utf-8",
            )

            context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=objectives,
            )

        self.assertNotIn(
            "OBJECTIVE-eps_fcf_explosion", context["resolved_objective_ids"]
        )
        self.assertNotIn(
            "OBJECTIVE-valuation_rerating", context["resolved_objective_ids"]
        )
        self.assertEqual(
            set(context["resolved_objective_ids"]),
            {
                f"OBJECTIVE-{component_id}"
                for component_id in CANONICAL_COMPONENT_ORDER
                if component_id
                not in {"eps_fcf_explosion", "valuation_rerating"}
            },
        )
        structured_gap = context["structured_gap_context"]
        self.assertEqual(
            structured_gap["missing_roles_by_component"],
            {
                "eps_fcf_explosion": ["FORWARD_GUIDANCE"],
                "valuation_rerating": ["DURABLE_VISIBILITY"],
            },
        )
        resolution = structured_gap["missing_role_resolution_contracts"]
        guidance = resolution["eps_fcf_explosion"]["FORWARD_GUIDANCE"]
        durable = resolution["valuation_rerating"]["DURABLE_VISIBILITY"]
        self.assertEqual(
            guidance["llm_fact_extractable_roles"], ["FORWARD_GUIDANCE"]
        )
        self.assertEqual(
            durable["accepted_engine_evidence_roles"],
            ["DURABLE_VISIBILITY", "FORWARD_GUIDANCE"],
        )
        self.assertEqual(
            durable["llm_fact_extractable_roles"], ["FORWARD_GUIDANCE"]
        )
        allowed = durable["fact_materialization_contracts"][
            "FORWARD_GUIDANCE"
        ]["allowed_source_families"]
        self.assertIn("ISSUER_EARNINGS_RELEASE", allowed)
        self.assertNotIn("PUBLIC_BROKER_PDF", allowed)
        self.assertTrue(
            durable["fact_materialization_contracts"]["FORWARD_GUIDANCE"]
            ["third_party_estimate_is_not_substitutable"]
        )
        self.assertEqual(structured_gap["query_generation_owner"], "LLM")
        self.assertFalse(structured_gap["deterministic_fallback_query_allowed"])
        self.assertEqual(
            context["supervisor_gap_context"]["query_direction_briefs"][0][
                "research_need"
            ],
            "numeric issuer outlook",
        )

    def test_pending_supervisor_transport_placeholder_does_not_reopen_objectives(
        self,
    ) -> None:
        target_id = "CURRENT-TARGET"
        as_of_date = "2026-06-29"
        objectives = tuple(
            {
                "objective_id": f"OBJECTIVE-{component_id}",
                "component_id": component_id,
            }
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "component_research_memos.jsonl").write_text(
                "\n".join(
                    json.dumps(
                        {
                            "component_id": component_id,
                            "research_complete": True,
                        }
                    )
                    for component_id in CANONICAL_COMPONENT_ORDER
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "research_epoch_checkpoint.json").write_text(
                json.dumps(
                    {
                        "checkpoint_id": "EPOCH-PENDING",
                        "epoch": 9,
                        "status": "NEXT_RESEARCH_REQUIRED",
                        "supervisor_review": {
                            "review_id": "RSUP-PENDING-1",
                            "status": "NEXT_RESEARCH_REQUIRED",
                            "component_status": {
                                component_id: "PENDING"
                                for component_id in CANONICAL_COMPONENT_ORDER
                            },
                            "component_findings": [],
                            "missing_material_facts": [],
                            "unresolved_material_questions": [
                                "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                                "COLLABORATION_RESPONSE_PENDING:COLLABREQ-1"
                            ],
                            "component_memos_sufficient": False,
                        },
                    }
                ),
                encoding="utf-8",
            )

            context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=objectives,
            )

        self.assertEqual(
            set(context["resolved_objective_ids"]),
            {
                f"OBJECTIVE-{component_id}"
                for component_id in CANONICAL_COMPONENT_ORDER
            },
        )

    def test_hash_bound_complete_memo_survives_transport_pending_and_semantic_rewrite_does_not_reopen_source(
        self,
    ) -> None:
        target_id = "CURRENT-TARGET"
        as_of_date = "2026-06-29"
        archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        component_id = "bottleneck_pricing"
        objective_id = "OBJECTIVE-bottleneck_pricing"
        memo = {
            "target_id": target_id,
            "archetype_id": archetype_id,
            "component_id": component_id,
            "researcher_role": "BottleneckPricingResearcher",
            "positive_fact_ids": ["FACT-POS"],
            "counter_fact_ids": ["FACT-COUNTER"],
            "resolution_fact_ids": [],
            "context_fact_ids": [],
            "research_complete": True,
        }
        memo_hash = hashlib.sha256(
            json.dumps(
                memo,
                ensure_ascii=False,
                sort_keys=True,
                default=str,
            ).encode("utf-8")
        ).hexdigest()

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "component_research_memos.jsonl").write_text(
                json.dumps(
                    {
                        "component_id": component_id,
                        "research_complete": False,
                        "pending_reasons": [
                            "PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING"
                        ],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "research_epochs.jsonl").write_text(
                json.dumps(
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "changed_component_memos": [memo],
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            def write_checkpoint(supervisor_review):
                (root / "research_epoch_checkpoint.json").write_text(
                    json.dumps(
                        {
                            "checkpoint_id": "EPOCH-HASH-BOUND",
                            "target_id": target_id,
                            "as_of_date": as_of_date,
                            "epoch": 10,
                            "status": "NEXT_RESEARCH_REQUIRED",
                            "component_memo_hashes": {
                                component_id: memo_hash
                            },
                            "supervisor_review": supervisor_review,
                        }
                    ),
                    encoding="utf-8",
                )

            semantic_rewrite = {
                "review_id": "SUPERVISOR-SEMANTIC-REWRITE",
                "status": "NEXT_RESEARCH_REQUIRED",
                "component_status": {component_id: "PENDING"},
                "component_findings": [
                    {
                        "component_id": component_id,
                        "memo_sufficient": False,
                        "missing_fact_needs": [],
                        "rationale": (
                            "심판 허용구간 불일치 설명을 memo에서 다시 쓴다."
                        ),
                    }
                ],
                "missing_material_facts": [],
                "new_source_family_directions": [],
                "query_direction_briefs": [],
                "source_family_gaps": [],
                "failure_assessments": [],
                "parser_or_extractor_failures": [],
                "unresolved_material_questions": [
                    "semantic component rewrite required"
                ],
                "next_actions": ["rewrite bottleneck memo"],
            }
            write_checkpoint(semantic_rewrite)
            semantic_context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=(
                    {
                        "objective_id": objective_id,
                        "component_id": component_id,
                    },
                ),
                archetype_id=archetype_id,
            )

            self.assertEqual(
                semantic_context["resolved_objective_ids"],
                (objective_id,),
            )
            self.assertEqual(
                semantic_context["supervisor_source_gap_context"], {}
            )
            routed = _component_supervisor_feedback_by_component(
                semantic_context["supervisor_gap_context"],
                objective_component_by_id={
                    objective_id: component_id
                },
            )
            self.assertEqual(set(routed), {component_id})

            write_checkpoint(
                {
                    "review_id": "SUPERVISOR-TRANSPORT-PENDING",
                    "status": "NEXT_RESEARCH_REQUIRED",
                    "component_status": {component_id: "PENDING"},
                    "component_findings": [],
                    "missing_material_facts": [],
                    "new_source_family_directions": [],
                    "query_direction_briefs": [],
                    "source_family_gaps": [],
                    "failure_assessments": [],
                    "parser_or_extractor_failures": [],
                    "unresolved_material_questions": [
                        "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                        "COLLABORATION_RESPONSE_PENDING:COLLABREQ-1"
                    ],
                    "next_actions": ["retry supervisor transport"],
                }
            )
            transport_context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=(
                    {
                        "objective_id": objective_id,
                        "component_id": component_id,
                    },
                ),
                archetype_id=archetype_id,
            )

        self.assertEqual(
            transport_context["resolved_objective_ids"],
            (objective_id,),
        )
        self.assertEqual(
            transport_context["supervisor_source_gap_context"], {}
        )
        self.assertEqual(
            _component_supervisor_feedback_by_component(
                transport_context["supervisor_gap_context"],
                objective_component_by_id={objective_id: component_id},
            ),
            {},
        )

    def test_score_disagreement_stays_supervisor_owned_while_fact_gaps_reopen_sources(
        self,
    ) -> None:
        target_id = "CURRENT-TARGET"
        as_of_date = "2026-06-29"
        score_unresolved = {"market_mispricing", "valuation_rerating"}
        source_unresolved = {
            "market_mispricing",
            "valuation_rerating",
        }
        objectives = tuple(
            {
                "objective_id": f"OBJECTIVE-{component_id}",
                "component_id": component_id,
            }
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        requests = [
            {
                "request_id": f"REQUEST-{component_id}",
                "component_id": component_id,
                "reason_codes": ["UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"],
                "query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
                "deterministic_query_synthesis": False,
            }
            for component_id in sorted(score_unresolved)
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "component_research_memos.jsonl").write_text(
                "\n".join(
                    json.dumps(
                        {
                            "component_id": component_id,
                            "research_complete": True,
                        }
                    )
                    for component_id in CANONICAL_COMPONENT_ORDER
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "deterministic_score_aggregation_run.json").write_text(
                json.dumps(
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "status": "DETERMINISTIC_SCORE_RESEARCH_REQUIRED",
                        "score_valid": False,
                        "pending_reasons": [
                            "EXACT_SEVEN_COMPONENT_DECISIONS_REQUIRED"
                        ],
                        "research_requests": requests,
                        "component_results": [
                            {
                                "component_id": component_id,
                                "status": (
                                    "RESEARCH_REQUIRED"
                                    if component_id in score_unresolved
                                    else "COMPLETE"
                                ),
                                "pending_reasons": (
                                    ["UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"]
                                    if component_id in score_unresolved
                                    else []
                                ),
                            }
                            for component_id in CANONICAL_COMPONENT_ORDER
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (root / "research_epoch_checkpoint.json").write_text(
                json.dumps(
                    {
                        "checkpoint_id": "EPOCH-2",
                        "epoch": 2,
                        "status": "NEXT_RESEARCH_REQUIRED",
                        "supervisor_review": {
                            "status": "NEXT_RESEARCH_REQUIRED",
                            "component_status": {
                                component_id: "COMPLETE"
                                for component_id in CANONICAL_COMPONENT_ORDER
                            },
                            "missing_material_facts": [
                                {
                                    "component_id": "market_mispricing",
                                    "direction": "COUNTER",
                                }
                            ],
                            "query_direction_briefs": [
                                {
                                    "objective_id": "OBJECTIVE-valuation_rerating",
                                    "counter_or_supersession": True,
                                }
                            ],
                        },
                    }
                ),
                encoding="utf-8",
            )

            context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=objectives,
            )

        self.assertEqual(
            set(context["resolved_objective_ids"]),
            {
                f"OBJECTIVE-{component_id}"
                for component_id in CANONICAL_COMPONENT_ORDER
                if component_id not in source_unresolved
            },
        )
        # Raw judge disagreement itself stays Supervisor-owned.  Market opens
        # because it has a concrete fact gap; valuation opens because the
        # persisted Supervisor review contains an objective-bound query
        # direction.  Status and next_actions text alone have no authority.
        self.assertEqual(context["score_gap_context"], {})
        source_gap = context["supervisor_source_gap_context"]
        self.assertEqual(
            {
                row["component_id"]
                for row in source_gap["missing_material_facts"]
            },
            {"market_mispricing"},
        )
        self.assertEqual(
            [
                row["objective_id"]
                for row in source_gap["query_direction_briefs"]
            ],
            ["OBJECTIVE-valuation_rerating"],
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "component_research_memos.jsonl").write_text(
                "\n".join(
                    json.dumps(
                        {
                            "component_id": component_id,
                            "research_complete": True,
                        }
                    )
                    for component_id in CANONICAL_COMPONENT_ORDER
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "deterministic_score_aggregation_run.json").write_text(
                json.dumps(
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "status": "DETERMINISTIC_SCORE_RESEARCH_REQUIRED",
                        "score_valid": False,
                        "pending_reasons": [
                            "EXACT_SEVEN_COMPONENT_DECISIONS_REQUIRED"
                        ],
                        "research_requests": requests,
                        "component_results": [],
                    }
                ),
                encoding="utf-8",
            )
            score_only_context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=objectives,
            )

        self.assertEqual(
            set(score_only_context["resolved_objective_ids"]),
            {row["objective_id"] for row in objectives},
        )
        self.assertEqual(score_only_context["score_gap_context"], {})
        self.assertEqual(
            score_only_context["supervisor_source_gap_context"], {}
        )

    def test_only_retryable_parser_or_fetch_failures_reopen_source_path(
        self,
    ) -> None:
        target_id = "CURRENT-TARGET"
        as_of_date = "2026-06-29"
        objectives = tuple(
            {
                "objective_id": f"OBJECTIVE-{component_id}",
                "component_id": component_id,
            }
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "component_research_memos.jsonl").write_text(
                "\n".join(
                    json.dumps(
                        {
                            "component_id": component_id,
                            "research_complete": True,
                        }
                    )
                    for component_id in CANONICAL_COMPONENT_ORDER
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "research_epoch_checkpoint.json").write_text(
                json.dumps(
                    {
                        "checkpoint_id": "EPOCH-FAILURE-ROUTING",
                        "epoch": 3,
                        "status": "NEXT_RESEARCH_REQUIRED",
                        "supervisor_review": {
                            "status": "NEXT_RESEARCH_REQUIRED",
                            "missing_material_facts": [],
                            "failure_assessments": [
                                {
                                    "failure_id": "PROVIDER-RETRYABLE",
                                    "classification": "PROVIDER_FAILURE",
                                    "retryable": True,
                                },
                                {
                                    "failure_id": "PARSER-NONRETRYABLE",
                                    "classification": "PARSER_EXTRACTOR_FAILURE",
                                    "retryable": False,
                                },
                                {
                                    "failure_id": "PARSER-RETRYABLE",
                                    "classification": "PARSER_EXTRACTOR_FAILURE",
                                    "retryable": True,
                                },
                                {
                                    "failure_id": "FETCH-RETRYABLE",
                                    "classification": "FETCH_FAILURE",
                                    "retryable": True,
                                },
                            ],
                            "parser_or_extractor_failures": [
                                "PARSER-NONRETRYABLE",
                                "PARSER-RETRYABLE",
                            ],
                        },
                    }
                ),
                encoding="utf-8",
            )
            (root / "source_graph_checkpoint.json").write_text(
                json.dumps(
                    {
                        "resolved_objective_ids": [],
                        "query_failures": [
                            {
                                "failure_id": "PARSER-RETRYABLE",
                                "objective_id": (
                                    "OBJECTIVE-bottleneck_pricing"
                                ),
                            },
                            {
                                "failure_id": "FETCH-RETRYABLE",
                                "objective_id": (
                                    "OBJECTIVE-capital_allocation"
                                ),
                            },
                        ],
                        "provider_failures": [],
                        "rejected_documents": [],
                    }
                ),
                encoding="utf-8",
            )

            context = _load_prior_research_context(
                root,
                target_id=target_id,
                as_of_date=as_of_date,
                objectives=objectives,
            )

        source_gap = context["supervisor_source_gap_context"]
        self.assertEqual(
            {
                row["failure_id"]
                for row in source_gap["failure_assessments"]
            },
            {"PARSER-RETRYABLE", "FETCH-RETRYABLE"},
        )
        self.assertEqual(
            source_gap["parser_or_extractor_failures"],
            ["PARSER-RETRYABLE"],
        )
        self.assertNotIn(
            "OBJECTIVE-bottleneck_pricing",
            context["resolved_objective_ids"],
        )
        self.assertNotIn(
            "OBJECTIVE-capital_allocation",
            context["resolved_objective_ids"],
        )

    def test_score_supervisor_projection_keeps_all_three_exact_judge_ranges(
        self,
    ) -> None:
        component_id = "bottleneck_pricing"
        decisions = tuple(
            SimpleNamespace(
                role=role,
                proposed_points=points,
                allowed_range=allowed_range,
                rationale=f"{role} rationale",
                disagreements=(f"{role} disagreement",),
                why_not_higher=f"{role} upper bound",
                why_not_lower=f"{role} lower bound",
            )
            for role, points, allowed_range in (
                ("ANALYST", 16.5, (14.9, 18.0)),
                ("SKEPTIC", 15.5, (14.5, 17.0)),
                ("CALIBRATION_JUDGE", 18.35, (18.05, 18.75)),
            )
        )
        aggregation = SimpleNamespace(
            to_score_gap_context=lambda: {
                "component_research_requests": [
                    {
                        "component_id": component_id,
                        "reason_codes": [
                            "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"
                        ],
                    }
                ]
            },
            component_results=(
                SimpleNamespace(
                    component_id=component_id,
                    material_disagreement=True,
                    pending_reasons=(
                        "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT",
                    ),
                ),
            ),
        )
        scoring_memos = SimpleNamespace(
            component_memos=(
                SimpleNamespace(
                    component_id=component_id,
                    judge_decisions=decisions,
                ),
            )
        )

        context = _score_gap_context_for_supervisor(
            aggregation=aggregation,
            scoring_memos=scoring_memos,
            structured_report_candidates=(
                {
                    "candidate_id": "STRUCTCAND-report-1",
                    "provider_name": "CompanyGuide",
                    "source_family_hint": "PUBLIC_BROKER_PDF",
                    "research_route": "PUBLIC_BROKER_REPORT",
                    "published_at": "2026-04-06",
                    "broker": "Example Securities",
                    "title": "Target quarterly preview",
                    "provider_file_name": "report.pdf",
                    "structured_fields": {"fy1_eps": 1234.0},
                    "url_resolution_required": True,
                    "full_document_owner": "LLM_SOURCE_GRAPH",
                    "evidence_eligible": False,
                    "snippet_only": True,
                    "deterministic_url_synthesis": False,
                    "deterministic_query_synthesis": False,
                    "production_score_authority": False,
                    "canonical_url": "https://must-not-project.example/report",
                },
            ),
        )

        self.assertEqual(
            context["material_disagreement_component_ids"], [component_id]
        )
        reviews = context["material_disagreement_judge_reviews"][0][
            "judge_reviews"
        ]
        self.assertEqual(
            [row["role"] for row in reviews],
            ["ANALYST", "SKEPTIC", "CALIBRATION_JUDGE"],
        )
        self.assertEqual(
            [row["allowed_range"] for row in reviews],
            [[14.9, 18.0], [14.5, 17.0], [18.05, 18.75]],
        )
        report_candidates = context[
            "structured_report_source_candidates"
        ]
        self.assertEqual(len(report_candidates), 1)
        self.assertEqual(
            report_candidates[0]["source_family_hint"],
            "PUBLIC_BROKER_PDF",
        )
        self.assertNotIn("canonical_url", report_candidates[0])
        contract = context[
            "structured_report_source_candidate_contract"
        ]
        self.assertEqual(contract["bounded_candidate_count"], 1)
        self.assertTrue(contract["metadata_is_discovery_hint_not_evidence"])
        self.assertEqual(
            contract["literal_query_generation_owner"],
            "SOURCE_QUERY_GENERATION_LLM",
        )
        self.assertFalse(
            contract["deterministic_url_or_query_synthesis_allowed"]
        )


if __name__ == "__main__":
    unittest.main()
