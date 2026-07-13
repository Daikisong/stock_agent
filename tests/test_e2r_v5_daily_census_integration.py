from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.production.metadata import stable_hash
from e2r.research_brain.researcher_mode.daily_census_integration import (
    DAILY_CENSUS_INTEGRATION_FAIL,
    DAILY_CENSUS_INTEGRATION_PASS,
    DEFAULT_DAILY_CENSUS_INTEGRATION_OUTPUT_PATH,
    DailyDossierEvent,
    DossierComponentState,
    DossierComponentStatus,
    DossierFactLineage,
    FullThesisStatus,
    PersistedResearchDossier,
    ResearchDossierStore,
    ScoreDisplayStatus,
    _audit_fixture_daily,
    _audit_fixture_dossier,
    audit_daily_census_integration,
    build_persisted_research_dossier,
    compile_phase97_daily_census_integration_audit,
    integrate_daily_census_researcher_mode,
    write_daily_census_researcher_integration,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.researcher_mode.saturation import SATURATION_REVIEW_ROLES
from e2r.research_brain.runtime.atomic_score_stage import CanonicalStage
from tests.test_e2r_v5_deterministic_score_aggregator import _aggregation_run


class E2RV5DailyCensusIntegrationTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    AS_OF_DATE = "2026-07-13"

    def setUp(self) -> None:
        self.prior = _audit_fixture_dossier(as_of_date="2026-07-12")
        self.daily = _audit_fixture_daily(
            as_of_date=self.AS_OF_DATE,
            target_id=self.prior.target_id,
        )
        self.fact = DossierFactLineage(
            fact_id="FACT-NEW-VISIBILITY",
            target_id=self.prior.target_id,
            available_date=self.AS_OF_DATE,
            source_ids=("DOC-NEW-VISIBILITY",),
            allowed_component_ids=("earnings_visibility",),
        )
        self.event = DailyDossierEvent(
            event_id="EVENT-NEW-VISIBILITY",
            target_id=self.prior.target_id,
            event_date=self.AS_OF_DATE,
            available_date=self.AS_OF_DATE,
            source_document_ids=("DOC-NEW-VISIBILITY",),
            new_facts=(self.fact,),
            impact_mapping_ids=("IMPACT-NEW-VISIBILITY",),
        )

    def test_committed_phase97_artifact_is_reproducible_and_passes(self) -> None:
        path = self.ROOT / DEFAULT_DAILY_CENSUS_INTEGRATION_OUTPUT_PATH
        committed = json.loads(path.read_text(encoding="utf-8"))
        compiled = compile_phase97_daily_census_integration_audit()

        self.assertEqual(committed, compiled)
        self.assertEqual(committed["status"], DAILY_CENSUS_INTEGRATION_PASS)
        self.assertEqual(committed["critical_count_sum"], 0)

    def test_every_universe_member_gets_assessment_but_deep_is_selective(self) -> None:
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(self.event,),
        )

        self.assertEqual(len(result.rows), len(self.daily["universe"]))
        self.assertEqual(sum(row.researcher_candidate for row in result.rows), 2)
        baseline = next(row for row in result.rows if row.target_id.endswith("B"))
        self.assertFalse(baseline.researcher_candidate)
        self.assertEqual(baseline.full_thesis_status, FullThesisStatus.NOT_OPEN.value)
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_source_backed_delta_reopens_only_impacted_component(self) -> None:
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(self.event,),
        )
        delta = result.delta_plans[0]
        row = next(row for row in result.rows if row.target_id == self.prior.target_id)

        self.assertEqual(delta.reopened_component_ids, ("earnings_visibility",))
        self.assertEqual(len(delta.reused_component_ids), 6)
        self.assertEqual(delta.component_rejudge_ids, delta.reopened_component_ids)
        self.assertTrue(delta.red_team_reopen)
        self.assertTrue(delta.synthesis_reopen)
        self.assertTrue(delta.deterministic_rescore_required)
        self.assertIsNone(delta.new_score_value)
        self.assertIsNone(delta.new_canonical_stage)
        self.assertIsNone(delta.score_delta)
        self.assertEqual(
            row.score_display_status,
            ScoreDisplayStatus.LAST_EFFECTIVE_PENDING_DELTA.value,
        )
        self.assertEqual(row.current_score, self.prior.score_value)
        self.assertEqual(row.current_stage, self.prior.canonical_stage)
        self.assertEqual(
            row.full_thesis_status,
            FullThesisStatus.DELTA_RESEARCH_REQUIRED.value,
        )

    def test_unchanged_full_thesis_is_reused_without_daily_deep_research(self) -> None:
        daily = deepcopy(self.daily)
        daily["depth_decisions"][0]["maximum_depth"] = "L1_BASELINE"
        daily["depth_decisions"][0]["completed_depths"] = [
            "L0_UNIVERSE",
            "L1_BASELINE",
        ]
        daily["depth_decisions"][0]["selected_for_deep"] = False
        daily["stage_statuses"][0]["maximum_depth"] = "L1_BASELINE"
        daily["stage_statuses"][0]["terminal_status"] = "BASELINE_ONLY"

        result = integrate_daily_census_researcher_mode(
            daily,
            persisted_dossiers=(self.prior,),
        )
        row = next(row for row in result.rows if row.target_id == self.prior.target_id)

        self.assertFalse(row.researcher_candidate)
        self.assertEqual(
            row.full_thesis_status,
            FullThesisStatus.FULL_THESIS_REUSED.value,
        )
        self.assertEqual(row.current_score, 70.0)
        self.assertEqual(row.current_stage, CanonicalStage.STAGE_2.value)
        self.assertEqual(row.pending_reasons, ())

    def test_unmapped_fact_does_not_trigger_a_deterministic_fallback_query(self) -> None:
        unmapped = replace(self.fact, allowed_component_ids=())
        event = replace(self.event, new_facts=(unmapped,))
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(event,),
        )
        delta = result.delta_plans[0]

        self.assertEqual(delta.status, "FACT_IMPACT_MAPPING_PENDING")
        self.assertEqual(delta.reopened_component_ids, ())
        self.assertEqual(delta.source_refresh_objectives, ())
        self.assertIn(
            "FACT_COMPONENT_IMPACT_MAPPING_REQUIRED:FACT-NEW-VISIBILITY",
            delta.pending_reasons,
        )
        self.assertFalse(delta.deterministic_query_synthesis)
        self.assertEqual(
            delta.query_generation_authority,
            "LLM_RESEARCH_SUPERVISOR",
        )

    def test_global_business_model_mapping_can_reopen_all_seven_components(self) -> None:
        event = replace(
            self.event,
            global_business_model_impact=True,
        )
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(event,),
        )
        delta = result.delta_plans[0]

        self.assertEqual(delta.reopened_component_ids, CANONICAL_COMPONENT_ORDER)
        self.assertEqual(delta.reused_component_ids, ())
        self.assertEqual(len(delta.source_refresh_objectives), 7)
        self.assertTrue(
            all(row["literal_query"] is None for row in delta.source_refresh_objectives)
        )

    def test_nonmaterial_event_is_recorded_but_does_not_reopen_full_thesis(self) -> None:
        event = replace(
            self.event,
            material=False,
            impact_mapping_ids=(),
        )
        daily = deepcopy(self.daily)
        daily["depth_decisions"][0]["maximum_depth"] = "L1_BASELINE"
        daily["depth_decisions"][0]["completed_depths"] = [
            "L0_UNIVERSE",
            "L1_BASELINE",
        ]
        daily["depth_decisions"][0]["selected_for_deep"] = False
        daily["stage_statuses"][0]["maximum_depth"] = "L1_BASELINE"
        daily["stage_statuses"][0]["terminal_status"] = "BASELINE_ONLY"

        result = integrate_daily_census_researcher_mode(
            daily,
            persisted_dossiers=(self.prior,),
            new_events=(event,),
        )
        row = next(row for row in result.rows if row.target_id == self.prior.target_id)
        self.assertEqual(result.delta_plans, ())
        self.assertEqual(row.daily_assessment_event_ids, (event.event_id,))
        self.assertEqual(
            row.full_thesis_status,
            FullThesisStatus.FULL_THESIS_REUSED.value,
        )

    def test_future_event_and_unknown_prior_fact_fail_closed(self) -> None:
        future = replace(
            self.event,
            event_date="2026-07-14",
            available_date="2026-07-14",
            new_facts=(replace(self.fact, available_date="2026-07-14"),),
        )
        with self.assertRaisesRegex(ValueError, "future event"):
            integrate_daily_census_researcher_mode(
                self.daily,
                persisted_dossiers=(self.prior,),
                new_events=(future,),
            )

        unknown = replace(
            self.event,
            new_facts=(),
            revised_fact_ids=("FACT-DOES-NOT-EXIST",),
        )
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(unknown,),
        )
        self.assertEqual(result.delta_plans[0].status, "FACT_IMPACT_MAPPING_PENDING")
        self.assertIn(
            "UNKNOWN_PRIOR_FACT:FACT-DOES-NOT-EXIST",
            result.delta_plans[0].pending_reasons,
        )

    def test_budget_and_provider_failures_are_pending_not_a_normal_stage0(self) -> None:
        daily = deepcopy(self.daily)
        daily["depth_decisions"][1]["maximum_depth"] = "L4_ACQUISITION"
        daily["depth_decisions"][1]["completed_depths"] = [
            "L0_UNIVERSE",
            "L1_BASELINE",
            "L2_OFFICIAL_LIGHT",
            "L3_RESEARCH_BRAIN",
            "L4_ACQUISITION",
        ]
        daily["depth_decisions"][1]["selected_for_deep"] = True
        daily["stage_statuses"][1].update(
            {
                "maximum_depth": "L4_ACQUISITION",
                "terminal_status": "PROVIDER_PENDING",
                "provider_gaps": ["codex_quota_unavailable"],
                "canonical_stage": "0",
            }
        )
        daily["deep_executions"].append(
            {"target_id": "PHASE97-TARGET-B", "outcome": "PROVIDER_PENDING"}
        )

        result = integrate_daily_census_researcher_mode(daily)
        provider = next(row for row in result.rows if row.target_id.endswith("B"))
        budget = next(row for row in result.rows if row.target_id.endswith("C"))

        self.assertEqual(
            provider.full_thesis_status,
            FullThesisStatus.PROVIDER_PENDING.value,
        )
        self.assertIsNone(provider.current_score)
        self.assertIsNone(provider.current_stage)
        self.assertIn("codex_quota_unavailable", provider.pending_reasons)
        self.assertEqual(
            budget.full_thesis_status,
            FullThesisStatus.BUDGET_CHECKPOINT_PENDING.value,
        )
        self.assertIsNone(budget.current_stage)

    def _completed_update(self) -> PersistedResearchDossier:
        components = []
        for component in self.prior.components:
            if component.component_id == "earnings_visibility":
                components.append(
                    replace(
                        component,
                        memo_id="MEMO-earnings_visibility-V2",
                        memo_hash=stable_hash("earnings_visibility-v2"),
                        decision_id="DECISION-earnings_visibility-V2",
                        fact_ids=(*component.fact_ids, self.fact.fact_id),
                        final_points=11.5,
                        reviewed_event_ids=(self.event.event_id,),
                    )
                )
            else:
                components.append(component)
        return replace(
            self.prior,
            dossier_id="DOSSIER-UPDATED-V2",
            as_of_date=self.AS_OF_DATE,
            version=2,
            previous_dossier_id=self.prior.dossier_id,
            facts=(*self.prior.facts, self.fact),
            components=tuple(components),
            research_epoch_checkpoint_id="REPOCH-PHASE97-V2",
            business_model_memo_hash=stable_hash("business-v2"),
            red_team_memo_hash=stable_hash("red-team-v2"),
            synthesis_memo_hash=stable_hash("synthesis-v2"),
            score_decision_id="SCORE-PHASE97-V2",
            score_value=71.5,
            applied_event_ids=(self.event.event_id,),
        )

    def test_completed_delta_computes_score_change_only_after_deterministic_update(self) -> None:
        updated = self._completed_update()
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(self.event,),
            completed_dossier_updates=(updated,),
        )
        delta = result.delta_plans[0]
        row = next(row for row in result.rows if row.target_id == self.prior.target_id)

        self.assertEqual(delta.status, "DELTA_APPLIED")
        self.assertEqual(delta.new_score_value, 71.5)
        self.assertEqual(delta.score_delta, 1.5)
        self.assertEqual(row.current_score, 71.5)
        self.assertEqual(
            row.score_display_status,
            ScoreDisplayStatus.CURRENT_DETERMINISTIC.value,
        )
        self.assertEqual(
            row.full_thesis_status,
            FullThesisStatus.FULL_THESIS_CURRENT.value,
        )

    def test_completed_delta_cannot_mutate_an_unaffected_component(self) -> None:
        updated = self._completed_update()
        components = list(updated.components)
        unaffected_index = next(
            index
            for index, component in enumerate(components)
            if component.component_id == "capital_allocation"
        )
        components[unaffected_index] = replace(
            components[unaffected_index],
            memo_hash=stable_hash("illicit-unaffected-change"),
        )
        tampered = replace(updated, components=tuple(components))

        with self.assertRaisesRegex(ValueError, "unaffected component changed"):
            integrate_daily_census_researcher_mode(
                self.daily,
                persisted_dossiers=(self.prior,),
                new_events=(self.event,),
                completed_dossier_updates=(tampered,),
            )

    def _canonical_completed_leaves(self):
        score_run, _, memos, facts, _ = _aggregation_run(mode="BASE")
        score_payload = score_run.to_dict()
        target_id = score_run.target_id
        archetype_id = score_run.archetype_id
        as_of_date = score_run.as_of_date
        research = {
            "target_id": target_id,
            "archetype_id": archetype_id,
            "as_of_date": as_of_date,
            "status": "RESEARCH_MEMOS_COMPLETE",
            "business_model_result": {
                "status": "COMPLETE",
                "memo": {
                    "memo_id": "BUSINESS-MEMO-CANONICAL",
                    "target_id": target_id,
                    "archetype_id": archetype_id,
                    "as_of_date": as_of_date,
                    "research_complete": True,
                },
                "pending_reasons": [],
            },
            "component_results": [
                {
                    "component_id": memo.component_id,
                    "status": "COMPLETE",
                    "memo": memo.to_dict(),
                    "pending_reasons": [],
                }
                for memo in memos
            ],
            "red_team_result": {
                "status": "COMPLETE",
                "memo": {
                    "memo_id": "RED-MEMO-CANONICAL",
                    "target_id": target_id,
                    "archetype_id": archetype_id,
                    "review_complete": True,
                    "reviewed_component_ids": list(CANONICAL_COMPONENT_ORDER),
                },
                "pending_reasons": [],
            },
            "synthesis_result": {
                "status": "COMPLETE",
                "memo": {
                    "memo_id": "SYNTHESIS-MEMO-CANONICAL",
                    "target_id": target_id,
                    "archetype_id": archetype_id,
                    "component_memo_ids": [memo.memo_id for memo in memos],
                    "synthesis_complete": True,
                    "unresolved_material_questions": [],
                },
                "pending_reasons": [],
            },
            "pending_reasons": [],
            "production_score_authority": False,
            "final_stage_authority": False,
        }
        review_ids = [f"SATURATION-REVIEW-{index}" for index in range(3)]
        prompt_hashes = [stable_hash(f"saturation-prompt-{index}") for index in range(3)]
        epoch = {
            "checkpoint_id": "REPOCH-CANONICAL-COMPLETE",
            "target_id": target_id,
            "as_of_date": as_of_date,
            "status": "SEMANTIC_SATURATION_CERTIFIED",
            "semantic_saturation_certified": True,
            "gold_critical_fact_miss_count": 0,
            "current_fact_ids": [fact.fact_id for fact in facts],
            "completion_based_on_fixed_rounds": False,
            "zero_search_result_treated_as_saturation": False,
            "transport_budget_treated_as_completion": False,
            "production_score_authority": False,
            "saturation_reviews": [
                {
                    "reviewer_role": role,
                    "status": "COMPLETE",
                    "review": {
                        "review_id": review_ids[index],
                        "prompt_hash": prompt_hashes[index],
                        "approve": True,
                        "provider_backed": True,
                        "checkpoint_id": "REPOCH-CANONICAL-COMPLETE",
                        "reviewer_role": role,
                    },
                }
                for index, role in enumerate(SATURATION_REVIEW_ROLES)
            ],
            "saturation_certificate": {
                "status": "CERTIFIED",
                "semantic_saturation_certified": True,
                "checkpoint_id": "REPOCH-CANONICAL-COMPLETE",
                "provider_backed_reviews_required": True,
                "review_ids": review_ids,
                "provider_prompt_hashes": prompt_hashes,
            },
        }
        total = score_run.total_result.score
        assert total is not None
        stagecourt = {
            "decision": {
                "decision_id": "STAGECOURT-CANONICAL-FINAL",
                "target_id": target_id,
                "archetype_id": archetype_id,
                "as_of_date": as_of_date,
                "status": "FINAL",
                "score_valid": True,
                "research_complete": True,
                "counter_thesis_complete": True,
                "stage_gates_complete": True,
                "llm_stage_authority": False,
                "pending_reasons": [],
                "total_points": total.total_points,
                "component_vector": dict(total.component_points),
                "canonical_stage": CanonicalStage.STAGE_2.value,
            },
            "audit": {"critical_count_sum": 0},
            "llm_stage_authority": False,
        }
        return research, epoch, score_payload, stagecourt, facts

    def test_canonical_phase84_to_95_leaves_materialize_one_l5_dossier(self) -> None:
        research, epoch, score, stagecourt, facts = self._canonical_completed_leaves()
        dossier = build_persisted_research_dossier(
            target_name="Canonical Target",
            research_dossier=research,
            research_epoch_checkpoint=epoch,
            score_aggregation=score,
            stagecourt_run=stagecourt,
            evidence_facts=facts,
        )

        self.assertEqual(dossier.version, 1)
        self.assertTrue(dossier.semantic_saturation_certified)
        self.assertTrue(dossier.score_valid)
        self.assertEqual(dossier.canonical_stage, CanonicalStage.STAGE_2.value)
        self.assertEqual(
            tuple(row.component_id for row in dossier.components),
            CANONICAL_COMPONENT_ORDER,
        )
        self.assertAlmostEqual(
            dossier.score_value or 0.0,
            sum(float(row.final_points or 0.0) for row in dossier.components),
        )

    def test_l5_materializer_rejects_transport_completion_and_vector_tamper(self) -> None:
        research, epoch, score, stagecourt, facts = self._canonical_completed_leaves()
        bad_epoch = deepcopy(epoch)
        bad_epoch["transport_budget_treated_as_completion"] = True
        with self.assertRaisesRegex(ValueError, "saturation checkpoint"):
            build_persisted_research_dossier(
                target_name="Canonical Target",
                research_dossier=research,
                research_epoch_checkpoint=bad_epoch,
                score_aggregation=score,
                stagecourt_run=stagecourt,
                evidence_facts=facts,
            )

        bad_stage = deepcopy(stagecourt)
        bad_stage["decision"]["component_vector"]["earnings_visibility"] += 1.0
        with self.assertRaisesRegex(ValueError, "vector disagree"):
            build_persisted_research_dossier(
                target_name="Canonical Target",
                research_dossier=research,
                research_epoch_checkpoint=epoch,
                score_aggregation=score,
                stagecourt_run=bad_stage,
                evidence_facts=facts,
            )

    def test_versioned_dossier_store_and_integration_writer_round_trip(self) -> None:
        updated = self._completed_update()
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(self.event,),
            completed_dossier_updates=(updated,),
        )
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            store = ResearchDossierStore(root / "store")
            first = store.save(self.prior)
            second = store.save(updated)
            loaded = store.load_latest(self.prior.target_id)
            paths = write_daily_census_researcher_integration(
                result,
                root / "daily",
            )

            self.assertTrue(all(path.is_file() for path in (*first.values(), *second.values())))
            self.assertEqual(loaded, updated)
            self.assertTrue(all(path.is_file() for path in paths.values()))
            manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
            self.assertEqual(manifest["status"], DAILY_CENSUS_INTEGRATION_PASS)

    def test_store_rejects_skipped_version_and_wrong_previous_id(self) -> None:
        with TemporaryDirectory() as tmp:
            store = ResearchDossierStore(tmp)
            store.save(self.prior)
            skipped = replace(
                self.prior,
                dossier_id="DOSSIER-SKIPPED",
                version=3,
                previous_dossier_id="WRONG",
            )
            with self.assertRaisesRegex(ValueError, "non-contiguous"):
                store.save(skipped)

    def test_audit_detects_unbounded_tasks_query_authority_and_advice(self) -> None:
        result = integrate_daily_census_researcher_mode(
            self.daily,
            persisted_dossiers=(self.prior,),
            new_events=(self.event,),
        )
        payload = result.to_leaf_dict()
        payload = deepcopy(payload)
        payload["daily_source_tasks"] = [
            {
                "max_queries": None,
                "max_candidates": 100,
                "max_fetches": 10,
                "stop_condition": "exhaust_all",
            }
        ]
        payload["delta_plans"][0]["deterministic_query_synthesis"] = True
        payload["delta_plans"][0]["source_refresh_objectives"][0][
            "literal_query"
        ] = "hardcoded company-specific query"
        payload["rows"][0]["direct_investment_recommendation"] = True

        audit = audit_daily_census_integration(payload)
        self.assertEqual(audit["status"], "DAILY_CENSUS_INTEGRATION_AUDIT_FAIL")
        self.assertEqual(
            audit["critical_counts"]["source_task_unbounded_or_no_stop_count"],
            1,
        )
        self.assertEqual(
            audit["critical_counts"]["delta_query_or_llm_authority_count"],
            1,
        )
        self.assertEqual(
            audit["critical_counts"]["direct_investment_recommendation_count"],
            1,
        )
        self.assertGreater(audit["critical_count_sum"], 0)

    def test_phase97_failure_label_is_distinct(self) -> None:
        payload = compile_phase97_daily_census_integration_audit()
        payload = deepcopy(payload)
        payload["critical_counts"]["forced_failure"] = 1
        payload["critical_count_sum"] = 1
        payload["status"] = DAILY_CENSUS_INTEGRATION_FAIL
        self.assertNotEqual(payload["status"], DAILY_CENSUS_INTEGRATION_PASS)


if __name__ == "__main__":
    unittest.main()
