"""Test-only detector registry for the Phase 15 known-bad suite."""

from __future__ import annotations

import io
import json
import unittest
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.research_brain.planner_bias_audit import build_planner_bias_audit
from e2r.research_brain.runtime.known_bad_suite import (
    KnownBadCategory,
    KnownBadProbeId,
    KnownBadProbeObservation,
    KnownBadSuiteResult,
    compile_known_bad_suite,
)


CORPUS_GOLDEN = (
    "tests.test_research_corpus_golden.ResearchCorpusGoldenTest."
    "test_mandatory_golden_cases_are_preserved_one_for_one"
)
CORPUS_REGISTRY = (
    "tests.test_research_corpus_golden.ResearchCorpusGoldenTest."
    "test_registry_golden_has_every_canonical_archetype_exactly_once"
)
FIRST_SYMBOL = (
    "tests.test_research_corpus_semantic_compiler."
    "ResearchCorpusSemanticCompilerTest."
    "test_trigger_only_rows_create_distinct_cases_without_first_symbol_collapse"
)
MULTIPLE_DATES = (
    "tests.test_research_corpus_semantic_compiler."
    "ResearchCorpusSemanticCompilerTest."
    "test_multiple_trigger_dates_remain_linked_without_false_date_loss"
)
CASE_SOURCE = (
    "tests.test_case_level_source_verification."
    "CaseLevelSourceVerificationTest."
    "test_happy_path_and_adversarial_states_are_separated"
)
CLAIM_INVARIANTS = (
    "tests.test_contract_blind_claim_compiler.ContractBlindClaimCompilerTest."
    "test_claim_ledger_schema_refuses_proxy_parser_and_mappingless_score"
)
BLIND_INPUT = (
    "tests.test_two_pass_brain_planner.TwoPassBrainPlannerTest."
    "test_blind_input_drops_future_outcome_and_preassigned_fields"
)
PLANNER_INJECTION = (
    "tests.test_two_pass_brain_planner.TwoPassBrainPlannerTest."
    "test_score_stage_source_primary_and_archetype_injection_are_pending"
)
C05_MONOCULTURE = (
    "tests.known_bad_suite_fixture.KnownBadMutationDetectors."
    "test_c05_monoculture_is_rejected_by_bias_audit"
)
PRODUCT_PROFILE = (
    "tests.test_research_brain_v4_evidence_extraction_from_real_document."
    "ResearchBrainV4EvidenceExtractionFromRealDocumentTests."
    "test_verified_company_newsroom_original_avoids_general_web_lineage_block_"
    "but_profile_claim_still_not_scored"
)
HBM_KEYWORD = (
    "tests.test_research_brain_v4_evidence_extraction_from_real_document."
    "ResearchBrainV4EvidenceExtractionFromRealDocumentTests."
    "test_hbm_mix_quote_does_not_satisfy_customer_allocation_task"
)
SECURITY_KEYWORD = (
    "tests.test_census_v4_all_archetype_replay_matrix."
    "CensusV4AllArchetypeReplayMatrixTests."
    "test_c28_source_backed_semantic_replay_passes_security_keyword_guard"
)
COMMODITY_HEADLINE = (
    "tests.test_census_v4_all_archetype_replay_matrix."
    "CensusV4AllArchetypeReplayMatrixTests."
    "test_c15_source_backed_semantic_replay_passes_raw_commodity_guard"
)
SOURCE_REJECTIONS = (
    "tests.test_source_acquisition_document_selection."
    "SourceAcquisitionDocumentSelectionTest."
    "test_unknown_future_snippet_hash_and_wrong_subject_are_rejected"
)
WRONG_SUBJECT = (
    "tests.test_contract_blind_claim_compiler.ContractBlindClaimCompilerTest."
    "test_wrong_subject_claim_is_ledgered_but_cannot_score"
)
TARGET_SCOPE = (
    "tests.test_agentic_evidence_os.AgenticEvidenceOSTests."
    "test_customer_supplier_and_industry_claims_do_not_become_issuer_capacity_"
    "or_order_support"
)
FINANCIAL_TRUST = (
    "tests.test_contract_semantic_classifier.ContractSemanticClassifierTests."
    "test_share_buyback_trust_is_not_customer_contract"
)
FINANCIAL_PLEDGE = (
    "tests.test_contract_semantic_classifier.ContractSemanticClassifierTests."
    "test_pledge_contract_is_not_customer_contract"
)
STALE_RISK = (
    "tests.test_contract_blind_claim_compiler.ContractBlindClaimCompilerTest."
    "test_old_negative_risk_is_stale_not_a_penalty"
)
REROUTED_GAP = (
    "tests.test_contract_blind_claim_compiler.ContractBlindClaimCompilerTest."
    "test_rerouted_claim_is_accepted_without_original_gap_closure"
)
PROVIDER_NOT_RED = (
    "tests.test_census_provider_pending_not_red."
    "CensusProviderPendingNotRedTests."
    "test_provider_pending_never_red_or_reject"
)
REPLAY_FETCH = (
    "tests.test_source_acquisition_document_selection."
    "SourceAcquisitionDocumentSelectionTest."
    "test_snapshot_and_report_replay_never_count_as_production_fetch"
)
EVENT_PARTIAL = (
    "tests.test_atomic_score_stage_integrity.AtomicScoreStageIntegrityTest."
    "test_material_gap_blocks_full_but_event_partial_stays_explicit"
)
STAGE_TRACE = (
    "tests.test_atomic_score_stage_integrity.AtomicScoreStageIntegrityTest."
    "test_joint_stage_and_trace_forgery_is_recomputed_from_score"
)
HISTORICAL_BOUNDARY = (
    "tests.test_historical_current_mode_separation."
    "HistoricalCurrentModeSeparationTest."
    "test_historical_prompt_is_blind_and_source_proxy_never_scores"
)
CURRENT_REJECTIONS = (
    "tests.test_historical_current_mode_separation."
    "HistoricalCurrentModeSeparationTest."
    "test_current_operation_rejects_future_history_quota_and_missing_outcome"
)
CURRENT_SELECTIVE = (
    "tests.test_historical_current_mode_separation."
    "HistoricalCurrentModeSeparationTest."
    "test_current_operation_is_full_baseline_and_bounded_selective_deep"
)


@dataclass(frozen=True)
class KnownBadProbeSpec:
    probe_id: str
    category: str
    source_phase: int
    detector_ids: tuple[str, ...]
    mutation_description: str


KNOWN_BAD_PROBE_SPECS = (
    KnownBadProbeSpec(
        KnownBadProbeId.FILE_LEVEL_CASE_COLLAPSE.value,
        KnownBadCategory.CORPUS.value,
        2,
        (CORPUS_GOLDEN,),
        "Multiple semantic cases in one artifact collapse into one file-level case.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.FIRST_SYMBOL_EXTRACTION.value,
        KnownBadCategory.CORPUS.value,
        2,
        (FIRST_SYMBOL,),
        "Every trigger row inherits the first symbol found in the artifact.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.COMPANY_DATE_LOSS.value,
        KnownBadCategory.CORPUS.value,
        2,
        (CORPUS_REGISTRY, MULTIPLE_DATES),
        "Present company names or distinct trigger dates disappear during compilation.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.ONE_URL_WHOLE_FILE_A2.value,
        KnownBadCategory.SOURCE.value,
        3,
        (CASE_SOURCE,),
        "One good URL upgrades every case in the same file to A2 evidence.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.HANDOFF_PROMPT_AS_CASE.value,
        KnownBadCategory.CORPUS.value,
        2,
        (CORPUS_GOLDEN,),
        "A deferred coding handoff prompt is parsed as a research case.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.SOURCE_PROXY_PROMOTED.value,
        KnownBadCategory.SOURCE.value,
        9,
        (CLAIM_INVARIANTS, HISTORICAL_BOUNDARY),
        "A source-proxy or parser signal is promoted into score-bearing evidence.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.C05_CONTEXT_COPY_CORPUS.value,
        KnownBadCategory.PLANNER.value,
        5,
        (BLIND_INPUT, PLANNER_INJECTION),
        "Historical source-primary or archetype answer keys are copied into planner context.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.C05_CONTEXT_COPY_CURRENT.value,
        KnownBadCategory.PLANNER.value,
        5,
        (C05_MONOCULTURE,),
        "Copied C05 context makes unrelated current candidates route to C05 by default.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.PRODUCT_PROFILE_AS_ORDER.value,
        KnownBadCategory.SEMANTIC.value,
        9,
        (PRODUCT_PROFILE,),
        "A product portfolio or partnership profile is treated as a customer order.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.HBM_KEYWORD_POSITIVE.value,
        KnownBadCategory.SEMANTIC.value,
        9,
        (HBM_KEYWORD,),
        "An HBM keyword or mix statement alone becomes positive allocation evidence.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.SECURITY_KEYWORD_ARR.value,
        KnownBadCategory.SEMANTIC.value,
        6,
        (SECURITY_KEYWORD,),
        "A security keyword alone becomes ARR or retention evidence.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.COMMODITY_HEADLINE_MARGIN.value,
        KnownBadCategory.SEMANTIC.value,
        6,
        (COMMODITY_HEADLINE,),
        "A commodity-price headline alone becomes issuer margin evidence.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.SNIPPET_SCORE.value,
        KnownBadCategory.SOURCE.value,
        7,
        (SOURCE_REJECTIONS,),
        "A search snippet without a full fetch receives score credit.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.WRONG_SUBJECT.value,
        KnownBadCategory.CLAIM.value,
        9,
        (WRONG_SUBJECT,),
        "A fact about another company closes the target company's gap.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.CUSTOMER_CAPA_AS_TARGET_CAPA.value,
        KnownBadCategory.CLAIM.value,
        9,
        (TARGET_SCOPE,),
        "A customer's capacity expansion becomes the issuer's capacity evidence.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.INDUSTRY_DEMAND_AS_ISSUER_ORDER.value,
        KnownBadCategory.CLAIM.value,
        9,
        (TARGET_SCOPE,),
        "Industry-wide demand becomes an issuer-specific order or allocation.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.FINANCIAL_CONTRACT_AS_COMMERCIAL.value,
        KnownBadCategory.CLAIM.value,
        9,
        (FINANCIAL_TRUST, FINANCIAL_PLEDGE),
        "A buyback trust or collateral agreement becomes a revenue contract.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.STALE_RISK_PENALTY.value,
        KnownBadCategory.CLAIM.value,
        9,
        (STALE_RISK,),
        "An expired negative event is applied as a current score penalty.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.REROUTED_GAP_CLOSURE.value,
        KnownBadCategory.CLAIM.value,
        10,
        (REROUTED_GAP,),
        "A useful claim rerouted to another recipe closes the original gap.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.PROVIDER_FAILURE_RED.value,
        KnownBadCategory.SCORE_STAGE.value,
        13,
        (PROVIDER_NOT_RED,),
        "A provider outage is interpreted as Red or thesis rejection.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.REPLAY_AS_REAL_FETCH.value,
        KnownBadCategory.SOURCE.value,
        7,
        (REPLAY_FETCH,),
        "A historical snapshot or report replay is counted as a live production fetch.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.EVENT_SCORE_FULL_SCORE.value,
        KnownBadCategory.SCORE_STAGE.value,
        12,
        (EVENT_PARTIAL,),
        "An event-only partial score is finalized as a full E2R score.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.STAGE_TRACE_MISMATCH.value,
        KnownBadCategory.SCORE_STAGE.value,
        12,
        (STAGE_TRACE,),
        "A forged Stage and trace disagree with the deterministic score input.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.HISTORICAL_OUTCOME_LEAKAGE.value,
        KnownBadCategory.MODE.value,
        11,
        (BLIND_INPUT, HISTORICAL_BOUNDARY),
        "Future price outcomes or expected stages leak into historical planner input.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.HISTORICAL_REPLAY_CURRENT_WATCHLIST.value,
        KnownBadCategory.MODE.value,
        11,
        (HISTORICAL_BOUNDARY, CURRENT_REJECTIONS),
        "A historical replay claim contaminates the current watchlist.",
    ),
    KnownBadProbeSpec(
        KnownBadProbeId.FORCED_CURRENT_ARCHETYPE_MATERIALIZATION.value,
        KnownBadCategory.CURRENT.value,
        11,
        (CURRENT_SELECTIVE, CURRENT_REJECTIONS),
        "Current operation forces an archetype quota without a real trigger.",
    ),
)


class KnownBadMutationDetectors(unittest.TestCase):
    """Direct mutation probes that did not already have a strong isolated test."""

    def test_c05_monoculture_is_rejected_by_bias_audit(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "runtime"
            output_root.mkdir(parents=True)
            rows = []
            for index in range(10):
                rows.append(
                    {
                        "real_provider_success": True,
                        "event": {"symbol": f"{index:06d}"},
                        "output": {
                            "top_k_archetype_hypotheses": [
                                {"archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP"}
                            ]
                        },
                    }
                )
            (output_root / "planner_runs.jsonl").write_text(
                "".join(
                    json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                    for row in rows
                ),
                encoding="utf-8",
            )
            audit = build_planner_bias_audit(
                repo_root=root,
                output_root=output_root,
                docs_dir=root / "docs",
            )

        self.assertEqual(audit["c05_top1_share"], 1.0)
        self.assertEqual(
            audit["status"],
            "PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY",
        )
        self.assertIn("planner_top1_c05_share_over_limit", audit["blockers"])
        self.assertIn(
            "planner_top1_distinct_archetype_count_below_minimum",
            audit["blockers"],
        )


class _RecordingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.passed_test_ids: set[str] = set()

    def addSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802
        super().addSuccess(test)
        self.passed_test_ids.add(test.id())


@lru_cache(maxsize=1)
def build_known_bad_suite_fixture() -> KnownBadSuiteResult:
    detector_ids = tuple(
        sorted(
            {
                detector_id
                for spec in KNOWN_BAD_PROBE_SPECS
                for detector_id in spec.detector_ids
            }
        )
    )
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(loader.loadTestsFromName(item) for item in detector_ids)
    stream = io.StringIO()
    runner = unittest.TextTestRunner(
        stream=stream,
        verbosity=0,
        resultclass=_RecordingResult,
    )
    run = runner.run(suite)
    failed_ids = tuple(
        detector_id
        for detector_id in detector_ids
        if detector_id not in run.passed_test_ids
    )
    if failed_ids or run.testsRun != len(detector_ids):
        raise AssertionError(
            "known-bad detector execution failed: "
            f"failed={failed_ids}; tests_run={run.testsRun}; "
            f"expected={len(detector_ids)}; output={stream.getvalue()}"
        )

    observations = tuple(
        KnownBadProbeObservation(
            probe_id=spec.probe_id,
            category=spec.category,
            source_phase=spec.source_phase,
            detector_ids=spec.detector_ids,
            mutation_description=spec.mutation_description,
            detected=all(item in run.passed_test_ids for item in spec.detector_ids),
            signal_ids=tuple(
                f"unittest_pass:{detector_id}" for detector_id in spec.detector_ids
            ),
        )
        for spec in KNOWN_BAD_PROBE_SPECS
    )
    return compile_known_bad_suite(observations)


__all__ = [
    "KNOWN_BAD_PROBE_SPECS",
    "KnownBadMutationDetectors",
    "KnownBadProbeSpec",
    "build_known_bad_suite_fixture",
]
