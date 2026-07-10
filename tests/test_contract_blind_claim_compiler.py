from __future__ import annotations

import unittest
from dataclasses import replace
from types import SimpleNamespace

from e2r.agentic.evidence_os import (
    EntityRecord,
    EntityRegistry,
    MappingStatus,
    Polarity,
    RawAssertion,
    SupportDirection,
    TemporalStatus,
)
from e2r.production.claim_extraction import LLMContractBlindRawAssertionExtractor
from e2r.research_brain.runtime.claim_compiler import (
    CanonicalAdjudicationProposal,
    ClaimCompilationInput,
    ClaimCompilationStatus,
    ClaimLifecycleKind,
    ClaimProviderKind,
    ContractBlindClaimCompiler,
    FixtureBlindClaimExtractorProvider,
    FixtureCanonicalClaimAdjudicator,
    FixtureRecipeClaimMapperProvider,
    ProductionLLMRawExtractorAdapter,
    RecipeClaimMappingProposal,
    StrictEntityTemporalAdjudicator,
    adapt_legacy_claim_bundle_for_diagnostics,
    audit_claim_compilation_results,
)
from e2r.research_brain.runtime.source_acquisition import (
    AcquisitionMode,
    AcquisitionStatus,
)
from e2r.research_brain.runtime.task_satisfaction import TaskSatisfactionStatus
from tests import test_source_acquisition_document_selection as phase8_tests


class ContractBlindClaimCompilerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        phase8_tests.SourceAcquisitionDocumentSelectionTest.setUpClass()
        cls.phase8 = phase8_tests.SourceAcquisitionDocumentSelectionTest(
            methodName="test_controlled_smoke_selects_full_hashed_recipe_sections"
        )
        cls.task = phase8_tests.SourceAcquisitionDocumentSelectionTest.task
        cls.recipe = phase8_tests.SourceAcquisitionDocumentSelectionTest.recipe
        cls.recipes = phase8_tests.SourceAcquisitionDocumentSelectionTest.recipes
        cls.reroute_recipe = next(
            recipe
            for recipe in cls.recipes
            if recipe.recipe_id != cls.recipe.recipe_id
            and "POSITIVE"
            in {
                polarity
                for predicate in recipe.accepted_claim_predicates
                for polarity in predicate.allowed_polarities
            }
        )
        cls.registry = EntityRegistry(
            entities={
                cls.task.target_id: EntityRecord(
                    entity_id=cls.task.target_id,
                    legal_name="테스트기업",
                    aliases=("Test Company",),
                    ticker="000660",
                ),
                "TARGET-OTHER": EntityRecord(
                    entity_id="TARGET-OTHER",
                    legal_name="다른기업",
                    aliases=("Other Company",),
                    ticker="999999",
                ),
            }
        )

    def _text(self, *, other_subject: bool = False, old_period: bool = False) -> str:
        if old_period:
            fact = (
                "테스트기업은 2020-01-01 고객 배정 계약을 공개했고 "
                "유효기간은 2020-01-01부터 2020-12-31까지였다."
            )
        elif other_subject:
            fact = (
                "테스트기업은 시장 현황을 설명했다. 다른기업은 2025-03-15 "
                "고객 배정 계약을 공개했고 유효기간은 2025-03-15부터 "
                "2025-12-31까지라고 밝혔다."
            )
        else:
            fact = (
                "테스트기업은 2025-03-15 고객 배정 계약을 공개했고 "
                "유효기간은 2025-03-15부터 2025-12-31까지라고 밝혔다."
            )
        return "\n".join(
            (
                "테스트기업 official filing",
                fact,
                "customer allocation and supply agreement terms were disclosed.",
                "capacity and utilization remained constrained while product ASP increased.",
                "guidance and estimate revisions include cancellation counter checks.",
            )
        )

    def _acquisition(self, *, candidate_id: str, text: str | None = None):
        candidate = self.phase8._candidate(
            candidate_id=candidate_id,
            full_text=text or self._text(),
        )
        return self.phase8._engine(self.phase8._connector(candidate)).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )

    def _source_exhausted_acquisition(self):
        return self.phase8._engine().acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )

    def _provider_failed_acquisition(self):
        connector = self.phase8._connector(
            None,
            family="DART",
            errors=("official provider timeout",),
        )
        return self.phase8._engine(connector).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )

    def _extractor(
        self,
        *,
        subject: str = "테스트기업",
        polarity: Polarity = Polarity.POSITIVE,
        event_date: str = "2025-03-15",
        effective_period: str = "2025-03-15 to 2025-12-31",
        anchor_id: str | None = None,
        empty_quote: bool = False,
        provider_kind: str = ClaimProviderKind.TEST_FIXTURE_LLM.value,
        captured: list | None = None,
    ):
        def callback(inputs):
            if captured is not None:
                captured.append(inputs)
            anchor = inputs.anchors[0]
            return (
                RawAssertion(
                    raw_assertion_id=(
                        f"RAW-{subject}-{polarity.value}-{event_date}-{anchor_id or 'OK'}"
                    ),
                    anchor_id=anchor_id or anchor.anchor_id,
                    subject_text=subject,
                    predicate="customer allocation and supply agreement",
                    object_text=anchor.exact_text,
                    polarity_proposal=polarity,
                    event_date_text=event_date,
                    effective_period_text=effective_period,
                    exact_quote="" if empty_quote else anchor.exact_text,
                ),
            )

        return FixtureBlindClaimExtractorProvider(
            callback=callback,
            provider_name=f"fixture-extractor:{provider_kind}",
            provider_kind=provider_kind,
        )

    def _mapper(
        self,
        *,
        recipe=None,
        direction: SupportDirection = SupportDirection.SUPPORT,
        status: MappingStatus = MappingStatus.ACCEPTED,
        complete_fields: bool = True,
        provider_kind: str = ClaimProviderKind.TEST_FIXTURE_LLM.value,
        empty: bool = False,
        captured: list | None = None,
    ):
        mapping_recipe = recipe or self.recipe

        def callback(inputs):
            if captured is not None:
                captured.append(inputs)
            if empty:
                return ()
            predicate = mapping_recipe.accepted_claim_predicates[0]
            return (
                RecipeClaimMappingProposal.build(
                    claim_id=inputs.claim.claim_id,
                    recipe=mapping_recipe,
                    accepted_predicate_id=predicate.predicate_id,
                    support_direction=direction,
                    mapping_status=status,
                    satisfied_required_fields=(
                        predicate.required_fields if complete_fields else ()
                    ),
                    rationale="fixture semantic recipe mapping",
                ),
            )

        return FixtureRecipeClaimMapperProvider(
            callback=callback,
            provider_name=f"fixture-mapper:{provider_kind}",
            provider_kind=provider_kind,
        )

    def _compile(
        self,
        *,
        acquisition=None,
        extractor=None,
        mapper=None,
        adjudicator=None,
        baseline_events=(),
    ):
        compiler = ContractBlindClaimCompiler(
            extractor=extractor or self._extractor(),
            mapper=mapper or self._mapper(),
            adjudicator=adjudicator or StrictEntityTemporalAdjudicator(),
            test_mode=True,
        )
        return compiler.compile(
            ClaimCompilationInput(
                task=self.task,
                recipe=self.recipe,
                acquisition=acquisition
                or self._acquisition(candidate_id="PHASE9-DEFAULT"),
                target_aliases=("Test Company",),
                entity_registry=self.registry,
                mapping_recipes=self.recipes,
                baseline_events=tuple(baseline_events),
            )
        )

    def test_contract_blind_input_and_direct_task_satisfaction(self) -> None:
        extraction_calls = []
        mapping_calls = []
        result = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-BLIND-DIRECT"),
            extractor=self._extractor(captured=extraction_calls),
            mapper=self._mapper(captured=mapping_calls),
        )
        self.assertEqual(result.status, ClaimCompilationStatus.COMPLETE.value)
        self.assertEqual(
            result.satisfaction.status,
            TaskSatisfactionStatus.DIRECT_TASK_SATISFIED.value,
        )
        self.assertTrue(result.satisfaction.original_gap_closed)
        self.assertEqual(len(result.ledger_events), 1)
        event = result.ledger_events[0]
        self.assertTrue(event.claim_accepted)
        self.assertTrue(event.score_eligible)
        self.assertTrue(event.closes_original_gap)
        self.assertFalse(event.production_score_eligible)

        blind_payload = extraction_calls[0].to_dict()
        forbidden = {
            "recipe_id",
            "primitive_id",
            "primitive_gap",
            "archetype_id",
            "score",
            "stage",
            "historical_outcome",
            "outcome_label",
        }
        self.assertFalse(forbidden & set(blind_payload))
        self.assertFalse(hasattr(extraction_calls[0], "recipe_id"))
        mapping_payload = mapping_calls[0].to_dict()
        self.assertNotIn("task_id", mapping_payload)
        self.assertNotIn("score", mapping_payload)
        self.assertNotIn("stage", mapping_payload)
        self.assertNotIn("historical_outcome", mapping_payload)

    def test_unknown_anchor_and_empty_quote_never_create_claim(self) -> None:
        bad_anchor = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-BAD-ANCHOR"),
            extractor=self._extractor(anchor_id="ANCHOR-NOT-IN-DOCUMENT"),
        )
        self.assertFalse(bad_anchor.adjudicated_claims)
        self.assertFalse(bad_anchor.ledger_events)
        self.assertEqual(bad_anchor.rejections[0].stage, "ANCHOR")

        empty_quote = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-EMPTY-QUOTE"),
            extractor=self._extractor(empty_quote=True),
        )
        self.assertFalse(empty_quote.adjudicated_claims)
        self.assertFalse(empty_quote.ledger_events)
        self.assertTrue(
            any("exact quote is empty" in row.detail for row in empty_quote.rejections)
        )

    def test_wrong_subject_claim_is_ledgered_but_cannot_score(self) -> None:
        result = self._compile(
            acquisition=self._acquisition(
                candidate_id="PHASE9-WRONG-SUBJECT",
                text=self._text(other_subject=True),
            ),
            extractor=self._extractor(subject="다른기업"),
        )
        self.assertEqual(
            result.satisfaction.status,
            TaskSatisfactionStatus.WRONG_SUBJECT.value,
        )
        self.assertEqual(len(result.adjudicated_claims), 1)
        self.assertFalse(result.ledger_events[0].claim_accepted)
        self.assertFalse(result.ledger_events[0].score_eligible)
        self.assertFalse(result.satisfaction.original_gap_closed)

    def test_old_negative_risk_is_stale_not_a_penalty(self) -> None:
        result = self._compile(
            acquisition=self._acquisition(
                candidate_id="PHASE9-OLD-RISK",
                text=self._text(old_period=True),
            ),
            extractor=self._extractor(
                polarity=Polarity.NEGATIVE,
                event_date="2020-01-01",
                effective_period="2020-01-01 to 2020-12-31",
            ),
            mapper=self._mapper(direction=SupportDirection.COUNTER),
        )
        self.assertEqual(
            result.satisfaction.status,
            TaskSatisfactionStatus.STALE_ONLY.value,
        )
        event = result.ledger_events[0]
        self.assertEqual(event.temporal_status, TemporalStatus.EXPIRED.value)
        self.assertFalse(event.score_eligible)
        self.assertFalse(event.closes_original_gap)

    def test_rerouted_claim_is_accepted_without_original_gap_closure(self) -> None:
        result = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-REROUTED"),
            mapper=self._mapper(recipe=self.reroute_recipe),
        )
        self.assertEqual(
            result.satisfaction.status,
            TaskSatisfactionStatus.REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN.value,
        )
        event = result.ledger_events[0]
        self.assertTrue(event.claim_accepted)
        self.assertTrue(event.score_eligible)
        self.assertEqual(event.mapped_recipe_id, self.reroute_recipe.recipe_id)
        self.assertFalse(event.closes_original_gap)
        self.assertFalse(result.satisfaction.original_gap_closed)

    def test_current_source_backed_baseline_can_be_explicitly_reused(self) -> None:
        direct = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-BASELINE-SEED")
        )
        baseline = replace(
            direct.ledger_events[0],
            event_id=f"BASELINE-{direct.ledger_events[0].event_id}",
            baseline=True,
            satisfaction_status=None,
            closes_original_gap=False,
        )
        reused = self._compile(
            acquisition=self._source_exhausted_acquisition(),
            baseline_events=(baseline,),
        )
        self.assertEqual(reused.status, ClaimCompilationStatus.COMPLETE.value)
        self.assertEqual(
            reused.satisfaction.status,
            TaskSatisfactionStatus.BASELINE_CLAIM_REUSED.value,
        )
        self.assertEqual(
            reused.satisfaction.baseline_claim_ids,
            (baseline.claim_id,),
        )
        self.assertTrue(reused.satisfaction.original_gap_closed)
        self.assertFalse(reused.ledger_events)

    def test_lifecycle_refresh_does_not_close_original_gap(self) -> None:
        strict = StrictEntityTemporalAdjudicator()

        def callback(raw, document, anchor, target, registry, as_of):
            proposal = strict.adjudicate(
                raw_assertion=raw,
                document=document,
                anchor=anchor,
                target_entity_id=target,
                entity_registry=registry,
                as_of_date=as_of,
            )
            return replace(
                proposal,
                lifecycle_kind=ClaimLifecycleKind.LIFECYCLE_REFRESH.value,
            )

        result = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-LIFECYCLE"),
            adjudicator=FixtureCanonicalClaimAdjudicator(callback),
        )
        self.assertEqual(
            result.satisfaction.status,
            TaskSatisfactionStatus.LIFECYCLE_REFRESH_ONLY.value,
        )
        self.assertFalse(result.ledger_events[0].score_eligible)
        self.assertFalse(result.satisfaction.original_gap_closed)

    def test_current_counter_claim_is_separate_from_direct_satisfaction(self) -> None:
        result = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-COUNTER"),
            extractor=self._extractor(polarity=Polarity.NEGATIVE),
            mapper=self._mapper(direction=SupportDirection.COUNTER),
        )
        self.assertEqual(
            result.satisfaction.status,
            TaskSatisfactionStatus.COUNTER_CLAIM_FOUND.value,
        )
        self.assertTrue(result.ledger_events[0].score_eligible)
        self.assertFalse(result.ledger_events[0].closes_original_gap)
        self.assertFalse(result.satisfaction.original_gap_closed)

    def test_contradiction_and_supersession_are_resolved_before_eligibility(self) -> None:
        baseline_seed = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-RELATION-SEED")
        )
        baseline = replace(
            baseline_seed.ledger_events[0],
            event_id=f"BASELINE-{baseline_seed.ledger_events[0].event_id}",
            baseline=True,
            satisfaction_status=None,
            closes_original_gap=False,
        )
        strict = StrictEntityTemporalAdjudicator()

        def open_counter(raw, document, anchor, target, registry, as_of):
            proposal = strict.adjudicate(
                raw_assertion=raw,
                document=document,
                anchor=anchor,
                target_entity_id=target,
                entity_registry=registry,
                as_of_date=as_of,
            )
            return replace(
                proposal,
                contradicted_claim_ids=(baseline.claim_id,),
                contradiction_group_id="CONTRADICTION-PHASE9",
                contradiction_resolved=False,
            )

        counter = self._compile(
            acquisition=self._acquisition(
                candidate_id="PHASE9-OPEN-CONTRADICTION",
                text=self._text() + "\nnew counter evidence was published.",
            ),
            extractor=self._extractor(polarity=Polarity.NEGATIVE),
            mapper=self._mapper(direction=SupportDirection.COUNTER),
            adjudicator=FixtureCanonicalClaimAdjudicator(open_counter),
            baseline_events=(baseline,),
        )
        self.assertEqual(
            counter.satisfaction.status,
            TaskSatisfactionStatus.COUNTER_CLAIM_FOUND.value,
        )
        self.assertIn("contradiction_open", counter.ledger_events[0].eligibility_reasons)
        self.assertFalse(counter.ledger_events[0].score_eligible)
        self.assertFalse(counter.satisfaction.original_gap_closed)

        def superseding(raw, document, anchor, target, registry, as_of):
            proposal = strict.adjudicate(
                raw_assertion=raw,
                document=document,
                anchor=anchor,
                target_entity_id=target,
                entity_registry=registry,
                as_of_date=as_of,
            )
            return replace(
                proposal,
                supersedes_claim_ids=(baseline.claim_id,),
            )

        superseded = self._compile(
            acquisition=self._acquisition(
                candidate_id="PHASE9-SUPERSEDES",
                text=self._text() + "\nnew superseding evidence was published.",
            ),
            adjudicator=FixtureCanonicalClaimAdjudicator(superseding),
            baseline_events=(baseline,),
        )
        self.assertEqual(
            superseded.satisfaction.status,
            TaskSatisfactionStatus.DIRECT_TASK_SATISFIED.value,
        )
        self.assertEqual(
            superseded.ledger_events[0].supersedes_claim_ids,
            (baseline.claim_id,),
        )
        self.assertTrue(superseded.ledger_events[0].score_eligible)

        def unknown_relation(raw, document, anchor, target, registry, as_of):
            proposal = strict.adjudicate(
                raw_assertion=raw,
                document=document,
                anchor=anchor,
                target_entity_id=target,
                entity_registry=registry,
                as_of_date=as_of,
            )
            return replace(
                proposal,
                supersedes_claim_ids=("CLAIM-NOT-IN-LEDGER",),
            )

        unknown = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-UNKNOWN-RELATION"),
            adjudicator=FixtureCanonicalClaimAdjudicator(unknown_relation),
        )
        self.assertFalse(unknown.ledger_events[0].score_eligible)
        self.assertTrue(
            any(
                reason.startswith("unknown_claim_relationship")
                for reason in unknown.ledger_events[0].eligibility_reasons
            )
        )

    def test_provider_failure_and_source_exhaustion_remain_distinct(self) -> None:
        provider_failed = self._compile(
            acquisition=self._provider_failed_acquisition()
        )
        self.assertEqual(
            provider_failed.status,
            ClaimCompilationStatus.PROVIDER_FAILED.value,
        )
        self.assertEqual(
            provider_failed.satisfaction.status,
            TaskSatisfactionStatus.PROVIDER_FAILED.value,
        )
        source_exhausted = self._compile(
            acquisition=self._source_exhausted_acquisition()
        )
        self.assertEqual(
            source_exhausted.status,
            ClaimCompilationStatus.SOURCE_EXHAUSTED.value,
        )
        self.assertEqual(
            source_exhausted.satisfaction.status,
            TaskSatisfactionStatus.SOURCE_EXHAUSTED.value,
        )

    def test_rule_fallback_and_parser_signal_cannot_enter_canonical_ledger(self) -> None:
        for kind in (
            ClaimProviderKind.LEGACY_RULE_FALLBACK.value,
            ClaimProviderKind.PARSER_SIGNAL.value,
        ):
            with self.subTest(kind=kind):
                result = self._compile(
                    acquisition=self._acquisition(candidate_id=f"PHASE9-{kind}"),
                    extractor=self._extractor(provider_kind=kind),
                )
                self.assertEqual(
                    result.status,
                    ClaimCompilationStatus.PROVIDER_FAILED.value,
                )
                self.assertFalse(result.adjudicated_claims)
                self.assertFalse(result.ledger_events)
                self.assertFalse(result.satisfaction.original_gap_closed)

        legacy_default = ProductionLLMRawExtractorAdapter(
            LLMContractBlindRawAssertionExtractor()
        )
        legacy_result = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-REAL-LEGACY-ADAPTER"),
            extractor=legacy_default,
        )
        self.assertEqual(
            legacy_result.status,
            ClaimCompilationStatus.PROVIDER_FAILED.value,
        )
        self.assertFalse(legacy_result.ledger_events)

    def test_provider_hash_budget_and_future_baseline_guards(self) -> None:
        valid_extractor = self._extractor()

        class TamperedExtractor:
            def extract(self, inputs):
                return replace(valid_extractor.extract(inputs), input_hash="0" * 64)

        tampered_extraction = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-TAMPERED-EXTRACTOR"),
            extractor=TamperedExtractor(),
        )
        self.assertEqual(
            tampered_extraction.status,
            ClaimCompilationStatus.PROVIDER_FAILED.value,
        )
        self.assertFalse(tampered_extraction.ledger_events)
        self.assertTrue(
            any("input_hash_mismatch" in error for error in tampered_extraction.provider_errors)
        )

        valid_mapper = self._mapper()

        class TamperedMapper:
            def map_claim(self, inputs):
                return replace(valid_mapper.map_claim(inputs), input_hash="f" * 64)

        tampered_mapping = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-TAMPERED-MAPPER"),
            mapper=TamperedMapper(),
        )
        self.assertEqual(
            tampered_mapping.status,
            ClaimCompilationStatus.PARTIAL.value,
        )
        self.assertFalse(tampered_mapping.ledger_events[0].score_eligible)
        self.assertTrue(
            any("input_hash_mismatch" in error for error in tampered_mapping.provider_errors)
        )

        def oversized(inputs):
            anchor = inputs.anchors[0]
            return tuple(
                RawAssertion(
                    raw_assertion_id=f"RAW-OVER-BUDGET-{index}",
                    anchor_id=anchor.anchor_id,
                    subject_text="테스트기업",
                    predicate=f"bounded fact {index}",
                    object_text=anchor.exact_text,
                    polarity_proposal=Polarity.POSITIVE,
                    event_date_text="2025-03-15",
                    effective_period_text="2025-03-15 to 2025-12-31",
                    exact_quote=anchor.exact_text,
                )
                for index in range(21)
            )

        bounded = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-RAW-BUDGET"),
            extractor=FixtureBlindClaimExtractorProvider(oversized),
            mapper=self._mapper(empty=True),
        )
        self.assertEqual(len(bounded.raw_assertions), 20)
        self.assertEqual(
            sum(row.reason == "RAW_ASSERTION_BUDGET_EXCEEDED" for row in bounded.rejections),
            1,
        )

        baseline_seed = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-FUTURE-BASELINE-SEED")
        )
        future_baseline = replace(
            baseline_seed.ledger_events[0],
            event_id=f"FUTURE-{baseline_seed.ledger_events[0].event_id}",
            source_published_at="2025-04-01",
            source_available_at="2025-04-01",
            baseline=True,
            satisfaction_status=None,
            closes_original_gap=False,
        )
        future_reuse = self._compile(
            acquisition=self._source_exhausted_acquisition(),
            baseline_events=(future_baseline,),
        )
        self.assertEqual(
            future_reuse.satisfaction.status,
            TaskSatisfactionStatus.SOURCE_EXHAUSTED.value,
        )
        self.assertFalse(future_reuse.satisfaction.original_gap_closed)

    def test_missing_or_incomplete_recipe_mapping_never_scores(self) -> None:
        no_mapping = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-NO-MAPPING"),
            mapper=self._mapper(empty=True),
        )
        self.assertEqual(
            no_mapping.satisfaction.status,
            TaskSatisfactionStatus.NO_RELEVANT_CLAIM.value,
        )
        self.assertFalse(no_mapping.ledger_events[0].score_eligible)
        self.assertIn(
            "recipe_mapping_missing",
            no_mapping.ledger_events[0].eligibility_reasons,
        )

        incomplete = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-INCOMPLETE-MAPPING"),
            mapper=self._mapper(complete_fields=False),
        )
        self.assertFalse(incomplete.ledger_events[0].score_eligible)
        self.assertTrue(
            any(row.stage == "MAPPING" for row in incomplete.rejections)
        )

    def test_claim_ledger_schema_refuses_proxy_parser_and_mappingless_score(self) -> None:
        direct = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-INVARIANTS")
        )
        event = direct.ledger_events[0]
        with self.assertRaises(ValueError):
            replace(event, source_proxy_only=True)
        with self.assertRaises(ValueError):
            replace(
                event,
                extraction_provider_kind=ClaimProviderKind.PARSER_SIGNAL.value,
            )
        with self.assertRaises(ValueError):
            replace(
                event,
                mapping_id=None,
                mapped_recipe_id=None,
                mapped_archetype_id=None,
                mapped_primitive_id=None,
                accepted_predicate_id=None,
                support_direction=None,
                mapping_status=None,
                mapping_provider_kind=None,
            )

    def test_legacy_claim_bundle_is_preserved_diagnostic_only(self) -> None:
        direct = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-LEGACY-SIDE-BY-SIDE")
        )
        bundle = SimpleNamespace(
            raw_assertions={
                item.raw_assertion_id: item for item in direct.raw_assertions
            },
            ledger=direct.evidence_ledger,
        )
        diagnostic = adapt_legacy_claim_bundle_for_diagnostics(bundle)
        self.assertEqual(diagnostic.status, "LEGACY_CLAIM_DIAGNOSTIC_ONLY")
        self.assertTrue(diagnostic.raw_assertion_ids)
        self.assertTrue(diagnostic.adjudicated_claim_ids)
        self.assertTrue(diagnostic.mapping_ids)
        self.assertEqual(diagnostic.canonical_score_credit_count, 0)
        self.assertEqual(diagnostic.canonical_task_closure_count, 0)
        self.assertFalse(diagnostic.canonical_execution_allowed)

    def test_claim_compiler_audit_has_zero_hard_safety_violations(self) -> None:
        direct = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-AUDIT-DIRECT")
        )
        rerouted = self._compile(
            acquisition=self._acquisition(candidate_id="PHASE9-AUDIT-REROUTED"),
            mapper=self._mapper(recipe=self.reroute_recipe),
        )
        wrong = self._compile(
            acquisition=self._acquisition(
                candidate_id="PHASE9-AUDIT-WRONG",
                text=self._text(other_subject=True),
            ),
            extractor=self._extractor(subject="다른기업"),
        )
        stale = self._compile(
            acquisition=self._acquisition(
                candidate_id="PHASE9-AUDIT-STALE",
                text=self._text(old_period=True),
            ),
            extractor=self._extractor(
                polarity=Polarity.NEGATIVE,
                event_date="2020-01-01",
                effective_period="2020-01-01 to 2020-12-31",
            ),
            mapper=self._mapper(direction=SupportDirection.COUNTER),
        )
        provider_failed = self._compile(
            acquisition=self._provider_failed_acquisition()
        )
        source_exhausted = self._compile(
            acquisition=self._source_exhausted_acquisition()
        )
        audit = audit_claim_compilation_results(
            (direct, rerouted, wrong, stale, provider_failed, source_exhausted)
        )
        self.assertEqual(audit["status"], "CONTRACT_BLIND_CLAIM_COMPILER_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(audit["direct_original_gap_closure_count"], 1)
        self.assertEqual(audit["rerouted_claim_event_count"], 1)
        self.assertEqual(
            audit["result_hash"],
            "dd1f97a90b17c6d35453063d63ecd0a16aa233de7706a9471a86df74f93f8c78",
        )
        self.assertFalse(audit["production_runtime_ready"])


if __name__ == "__main__":
    unittest.main()
