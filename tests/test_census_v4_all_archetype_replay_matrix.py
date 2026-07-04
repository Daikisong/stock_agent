import unittest

from tests.census_v4_test_helpers import census_v4_artifacts, read_json, read_jsonl


class CensusV4AllArchetypeReplayMatrixTests(unittest.TestCase):
    def test_matrix_covers_all_contracts_and_closes_source_backed_replay_gate(self):
        artifacts = census_v4_artifacts()
        root = artifacts["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        readiness = artifacts["readiness"]
        goal_completion = read_json(root / "goal_completion_audit.json")

        self.assertEqual(matrix["schema_version"], "e2r_census_v4_all_archetype_replay_matrix_v1")
        self.assertEqual(matrix["archetype_count"], 36)
        self.assertEqual(len(matrix["archetypes"]), 36)
        self.assertTrue(matrix["all_archetype_replay_pass"])
        self.assertEqual(matrix["source_backed_ready_count"], 36)
        self.assertEqual(matrix["guard_replay_ready_count"], 36)
        self.assertEqual(matrix["controlled_wiring_smoke_ready_count"], 1)
        self.assertEqual(matrix["missing_required_archetype_count"], 0)
        self.assertEqual(matrix["missing_required_archetype_ids"], [])
        self.assertEqual(matrix["blockers"], [])
        self.assertTrue(matrix["external_replay_acceptance_pass"])
        self.assertEqual(matrix["external_source_backed_seed_ready_count"], 30)
        self.assertTrue(matrix["external_global_guard_ready"])
        external = matrix["external_replay_acceptance"]
        self.assertTrue(external["external_source_backed_manifest_ready"])
        self.assertTrue(external["external_replay_acceptance_ready"])
        self.assertTrue(external["external_adversarial_acceptance_ready"])
        self.assertEqual(external["manifest_production_score_fixture_count"], 0)
        self.assertFalse(external["production_score_fixture_allowed"])
        self.assertFalse(external["production_stage_fixture_allowed"])

        self.assertTrue(readiness["all_archetype_replay_pass"])
        self.assertEqual(readiness["all_archetype_replay_matrix"]["archetype_count"], 36)
        self.assertEqual(readiness["all_archetype_replay_matrix"]["source_backed_ready_count"], 36)
        self.assertEqual(readiness["all_archetype_replay_matrix"]["guard_replay_ready_count"], 36)
        self.assertEqual(readiness["all_archetype_replay_matrix"]["controlled_wiring_smoke_ready_count"], 1)
        self.assertEqual(readiness["all_archetype_replay_matrix"]["replay_gap_source_task_count"], 0)
        self.assertEqual(readiness["all_archetype_replay_matrix"]["replay_gap_seed_event_count"], 0)
        self.assertEqual(readiness["all_archetype_replay_matrix"]["replay_gap_plan_task_count"], 0)
        self.assertTrue(goal_completion["all_archetype_replay_pass_allowed"])
        self.assertEqual(goal_completion["all_archetype_replay_matrix_summary"]["archetype_count"], 36)
        self.assertEqual(goal_completion["all_archetype_replay_matrix_summary"]["missing_required_archetype_count"], 0)
        self.assertEqual(goal_completion["all_archetype_replay_matrix_summary"]["replay_gap_source_task_count"], 0)
        self.assertEqual(goal_completion["all_archetype_replay_matrix_summary"]["replay_gap_seed_event_count"], 0)
        self.assertEqual(goal_completion["all_archetype_replay_matrix_summary"]["replay_gap_plan_task_count"], 0)
        self.assertNotIn("source_backed_replay_parity_all_archetypes_pending", goal_completion["blockers"])

        self.assertEqual(matrix["replay_gap_source_task_count"], matrix["missing_required_archetype_count"])
        self.assertEqual(matrix["replay_gap_seed_event_count"], matrix["replay_gap_source_task_count"])
        self.assertEqual(matrix["replay_gap_plan_task_count"], matrix["missing_required_archetype_count"])

    def test_all_archetype_replay_matrix_exports_existing_replay_gap_plan_manifest(self):
        root = census_v4_artifacts()["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        acceptance = read_json(root / "all_archetype_replay_acceptance_manifest.json")
        gap_plan = read_json(root / "all_archetype_replay_gap_plan.json")

        self.assertEqual(acceptance["schema_version"], "e2r_replay_acceptance_manifest_v1")
        self.assertEqual(acceptance["source"], "census_v4_all_archetype_replay_matrix")
        self.assertEqual(acceptance["summary"]["archetype_count"], matrix["required_archetype_count"])
        self.assertEqual(acceptance["summary"]["stage_preview_ready_count"], matrix["required_archetype_count"])
        self.assertEqual(acceptance["summary"]["unsupported_source_gap_count"], 0)
        self.assertTrue(acceptance["summary"]["replay_acceptance_ready"])
        self.assertFalse(acceptance["summary"]["production_cutover_ready"])

        self.assertEqual(gap_plan["schema_version"], "e2r_replay_gap_plan_manifest_v1")
        self.assertEqual(gap_plan["summary"]["gap_task_count"], 0)
        self.assertEqual(gap_plan["summary"]["unsupported_source_gap_task_count"], 0)
        self.assertTrue(gap_plan["summary"]["production_cutover_ready"])
        by_archetype = {task["archetype_id"]: task for task in gap_plan["tasks"]}
        self.assertEqual(by_archetype, {})

    def test_all_source_backed_replay_gaps_are_closed_by_0621_acceptance_artifacts(self):
        root = census_v4_artifacts()["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        tasks = read_jsonl(root / "all_archetype_replay_gap_source_tasks.jsonl")
        seeds = read_jsonl(root / "all_archetype_replay_gap_seed_events.jsonl")

        self.assertTrue(matrix["all_archetype_replay_pass"])
        self.assertEqual(matrix["missing_required_archetype_count"], 0)
        self.assertEqual(tasks, [])
        self.assertEqual(seeds, [])

        by_id = {row["archetype_id"]: row for row in matrix["archetypes"]}
        c01 = by_id["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]
        self.assertTrue(c01["positive_replay_pass"])
        self.assertTrue(c01["guard_replay_pass"])
        self.assertEqual(c01["positive_replay_basis"], "0621_c01_c36_source_backed_replay_acceptance")
        self.assertEqual(c01["guard_replay_basis"], "0621_global_adversarial_acceptance")
        self.assertEqual(c01["external_source_backed_seed_candidate_count"], 3)
        self.assertEqual(c01["source_backed_fixture_count"], 3)
        self.assertFalse(c01["controlled_wiring_smoke_pass"])
        self.assertFalse(c01["production_score_fixture_allowed"])
        self.assertFalse(c01["production_stage_fixture_allowed"])

    def test_c06_source_backed_semantic_replay_passes_without_treating_smoke_as_production(self):
        matrix = read_json(census_v4_artifacts()["output_root"] / "all_archetype_replay_matrix.json")
        by_id = {row["archetype_id"]: row for row in matrix["archetypes"]}
        c06 = by_id["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]

        self.assertEqual(c06["replay_status"], "SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY")
        self.assertEqual(c06["replay_scope"], "source_backed_semantic_replay")
        self.assertEqual(c06["url_backed_wiring_fixture_count"], 2)
        self.assertEqual(c06["source_backed_fixture_count"], 1)
        self.assertEqual(set(c06["full_thesis_symbols"]), {"005930", "000660"})
        self.assertTrue(c06["controlled_wiring_smoke_pass"])
        self.assertTrue(c06["positive_replay_pass"])
        self.assertTrue(c06["guard_replay_pass"])
        self.assertEqual(c06["guard_case_count"], 3)
        self.assertEqual(c06["guard_case_pass_count"], 3)
        self.assertEqual(c06["source_backed_replay_symbols"], ["000660"])
        self.assertIn("controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted", c06["semantic_blockers"])
        self.assertIn("samsung_positive_smoke_reuses_c06_guard_urls", c06["semantic_blockers"])

        source_gap_ids = {
            row["archetype_id"]
            for row in matrix["archetypes"]
            if row["replay_status"] == "SOURCE_GAP_PENDING"
        }
        self.assertNotIn("C01_ORDER_BACKLOG_MARGIN_BRIDGE", source_gap_ids)
        self.assertNotIn("C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", source_gap_ids)

    def test_c08_source_backed_semantic_replay_passes_profile_only_guard(self):
        root = census_v4_artifacts()["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        replay = read_json(root / "c08_source_backed_semantic_replay.json")
        by_id = {row["archetype_id"]: row for row in matrix["archetypes"]}
        c08 = by_id["C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"]

        self.assertEqual(c08["replay_status"], "SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY")
        self.assertTrue(c08["positive_replay_pass"])
        self.assertTrue(c08["guard_replay_pass"])
        self.assertEqual(c08["source_backed_fixture_count"], 4)
        self.assertEqual(c08["source_backed_replay_symbols"], ["405100"])
        self.assertEqual(c08["score_contribution_count"], 0)

        self.assertEqual(replay["schema_version"], "e2r_census_v4_c08_source_backed_semantic_replay_v1")
        self.assertTrue(replay["positive_replay_pass"])
        self.assertTrue(replay["guard_replay_pass"])
        self.assertEqual(set(replay["positive_accepted_primitive_ids"]), {"socket_or_test_demand_visible", "named_customer_quality"})
        self.assertEqual(replay["guard_accepted_primitive_ids"], ["socket_or_test_demand_visible"])
        self.assertEqual(replay["profile_only_guard_leaked_primitives"], [])
        self.assertEqual(replay["accepted_claim_count"], 4)
        self.assertEqual(replay["document_urls"], ["https://ssl.pstatic.net/imgstock/upload/research/company/1704669223541.pdf"])
        self.assertEqual(replay["blockers"], [])

    def test_c15_source_backed_semantic_replay_passes_raw_commodity_guard(self):
        root = census_v4_artifacts()["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        replay = read_json(root / "c15_source_backed_semantic_replay.json")
        by_id = {row["archetype_id"]: row for row in matrix["archetypes"]}
        c15 = by_id["C15_MATERIAL_SPREAD_SUPERCYCLE"]

        self.assertEqual(c15["replay_status"], "SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY")
        self.assertTrue(c15["positive_replay_pass"])
        self.assertTrue(c15["guard_replay_pass"])
        self.assertEqual(c15["source_backed_fixture_count"], 6)
        self.assertEqual(c15["accepted_claim_count"], 6)
        self.assertEqual(c15["guard_case_count"], 1)
        self.assertEqual(c15["guard_case_pass_count"], 1)
        self.assertEqual(c15["source_backed_replay_symbols"], ["004020", "005490"])
        self.assertEqual(c15["score_contribution_count"], 0)

        self.assertEqual(replay["schema_version"], "e2r_census_v4_c15_source_backed_semantic_replay_v1")
        self.assertTrue(replay["positive_replay_pass"])
        self.assertTrue(replay["guard_replay_pass"])
        self.assertEqual(
            set(replay["positive_accepted_primitive_ids"]),
            {"spread_expansion", "pricing_power_confirmed", "fcf_quality_score"},
        )
        self.assertEqual(replay["guard_accepted_primitive_ids"], [])
        self.assertEqual(replay["raw_commodity_guard_leaked_primitives"], [])
        self.assertEqual(replay["accepted_claim_count"], 6)
        self.assertEqual(
            replay["document_urls"],
            [
                "https://en.yna.co.kr/view/AEN20210427007052320",
                "https://www.posco.co.kr/homepage/servlet/FileDownLoad?fileCategory=irDataFd&fileNum=407",
                "https://www.businesskorea.co.kr/news/articleView.html?idxno=60900",
            ],
        )
        self.assertEqual(replay["blockers"], [])
        self.assertFalse(replay["production_score_evidence_allowed"])

    def test_c17_source_backed_semantic_replay_passes_spread_only_guard(self):
        root = census_v4_artifacts()["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        replay = read_json(root / "c17_source_backed_semantic_replay.json")
        by_id = {row["archetype_id"]: row for row in matrix["archetypes"]}
        c17 = by_id["C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"]

        self.assertEqual(c17["replay_status"], "SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY")
        self.assertTrue(c17["positive_replay_pass"])
        self.assertTrue(c17["guard_replay_pass"])
        self.assertEqual(c17["source_backed_fixture_count"], 10)
        self.assertEqual(c17["accepted_claim_count"], 10)
        self.assertEqual(c17["guard_case_count"], 1)
        self.assertEqual(c17["guard_case_pass_count"], 1)
        self.assertEqual(c17["source_backed_replay_symbols"], ["010950"])
        self.assertEqual(c17["score_contribution_count"], 0)

        self.assertEqual(replay["schema_version"], "e2r_census_v4_c17_source_backed_semantic_replay_v1")
        self.assertTrue(replay["positive_replay_pass"])
        self.assertTrue(replay["guard_replay_pass"])
        self.assertEqual(
            set(replay["positive_support_primitive_ids"]),
            {"spread_expansion", "opm_expansion_pctp", "utilization_rate"},
        )
        self.assertEqual(replay["guard_support_primitive_ids"], ["spread_expansion"])
        self.assertEqual(replay["spread_only_guard_leaked_support_primitives"], [])
        self.assertEqual(replay["accepted_claim_count"], 10)
        self.assertEqual(
            replay["document_urls"],
            [
                "https://www.s-oil.com/common/page/FileDownload.aspx?FileName=638977732335971792.pdf&PIndex=4&PathType=BOARD&TFileName=3Q+2025+S-OIL+Earnings+Release.pdf",
                "https://www.s-oil.com/common/page/FileDownload.aspx?FileName=638917284006185071.pdf&PIndex=4&PathType=BOARD&TFileName=2Q25++Earnings+Release+FN.pdf",
            ],
        )
        self.assertEqual(replay["blockers"], [])
        self.assertFalse(replay["production_score_evidence_allowed"])

    def test_c24_source_backed_semantic_replay_passes_binary_event_guard(self):
        root = census_v4_artifacts()["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        replay = read_json(root / "c24_source_backed_semantic_replay.json")
        by_id = {row["archetype_id"]: row for row in matrix["archetypes"]}
        c24 = by_id["C24_BIO_TRIAL_DATA_EVENT_RISK"]

        self.assertEqual(c24["replay_status"], "SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY")
        self.assertTrue(c24["positive_replay_pass"])
        self.assertTrue(c24["guard_replay_pass"])
        self.assertEqual(c24["source_backed_fixture_count"], 5)
        self.assertEqual(c24["accepted_claim_count"], 5)
        self.assertEqual(c24["guard_case_count"], 1)
        self.assertEqual(c24["guard_case_pass_count"], 1)
        self.assertEqual(c24["source_backed_replay_symbols"], ["009420", "215600"])
        self.assertEqual(c24["score_contribution_count"], 0)

        self.assertEqual(replay["schema_version"], "e2r_census_v4_c24_source_backed_semantic_replay_v1")
        self.assertTrue(replay["positive_replay_pass"])
        self.assertTrue(replay["guard_replay_pass"])
        self.assertEqual(replay["positive_support_primitive_ids"], ["trial_quality_visible"])
        self.assertEqual(replay["guard_counter_primitive_ids"], ["binary_event_unresolved"])
        self.assertEqual(replay["binary_event_guard_leaked_support_primitives"], [])
        self.assertEqual(replay["accepted_claim_count"], 5)
        self.assertEqual(
            replay["document_urls"],
            [
                "https://www.prnewswire.com/news-releases/hanall-biopharma-reports-full-year-2023-financial-results-and-provides-business-update-302095695.html",
                "https://www.prnewswire.com/news-releases/sillajen-announces-conclusions-from-interim-futility-analysis-of-phase-3-phocus-trial-in-hcc-300895539.html",
            ],
        )
        self.assertEqual(replay["blockers"], [])
        self.assertFalse(replay["production_score_evidence_allowed"])

    def test_c28_source_backed_semantic_replay_passes_security_keyword_guard(self):
        root = census_v4_artifacts()["output_root"]
        matrix = read_json(root / "all_archetype_replay_matrix.json")
        replay = read_json(root / "c28_source_backed_semantic_replay.json")
        by_id = {row["archetype_id"]: row for row in matrix["archetypes"]}
        c28 = by_id["C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"]

        self.assertEqual(c28["replay_status"], "SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY")
        self.assertTrue(c28["positive_replay_pass"])
        self.assertTrue(c28["guard_replay_pass"])
        self.assertEqual(c28["source_backed_fixture_count"], 7)
        self.assertEqual(c28["accepted_claim_count"], 7)
        self.assertEqual(c28["guard_case_count"], 1)
        self.assertEqual(c28["guard_case_pass_count"], 1)
        self.assertEqual(c28["source_backed_replay_symbols"], ["00CRWD"])
        self.assertEqual(c28["score_contribution_count"], 0)

        self.assertEqual(replay["schema_version"], "e2r_census_v4_c28_source_backed_semantic_replay_v1")
        self.assertTrue(replay["positive_replay_pass"])
        self.assertTrue(replay["guard_replay_pass"])
        self.assertEqual(
            set(replay["positive_support_primitive_ids"]),
            {"arr_growth_visible", "nrr", "retention_or_renewal", "rpo_to_sales", "recurring_margin_leverage"},
        )
        self.assertEqual(replay["guard_support_primitive_ids"], [])
        self.assertEqual(replay["guard_accepted_claim_ids"], [])
        self.assertEqual(replay["keyword_only_guard_leaked_support_primitives"], [])
        self.assertEqual(replay["accepted_claim_count"], 7)
        self.assertEqual(
            replay["document_urls"],
            [
                "https://www.sec.gov/Archives/edgar/data/1535527/000153552725000009/crwd-20250131.htm",
                "https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-announces-falcon-next-gen-siem-isv-ecosystem-open",
            ],
        )
        self.assertEqual(replay["blockers"], [])
        self.assertFalse(replay["production_score_evidence_allowed"])

    def test_matrix_has_no_source_proxy_score_leak(self):
        matrix = read_json(census_v4_artifacts()["output_root"] / "all_archetype_replay_matrix.json")
        self.assertEqual(matrix["source_proxy_leak_count"], 0)
        self.assertEqual(matrix["source_proxy_leak_claim_ids"], [])
        self.assertTrue(all(row["source_proxy_leak_count"] == 0 for row in matrix["archetypes"]))

    def test_c06_guard_replay_blocks_qualification_lag_false_positive(self):
        root = census_v4_artifacts()["output_root"]
        audit = read_json(root / "c06_guard_replay_audit.json")

        self.assertEqual(audit["schema_version"], "e2r_census_v4_c06_guard_replay_audit_v1")
        self.assertTrue(audit["positive_wiring_smoke_ready"])
        self.assertTrue(audit["positive_replay_ready"])
        self.assertTrue(audit["source_backed_positive_replay_ready"])
        self.assertTrue(audit["positive_semantic_replay_ready"])
        self.assertTrue(audit["guard_replay_pass"])
        self.assertTrue(audit["guard_cases_pass"])
        self.assertEqual(audit["guard_case_count"], 3)
        self.assertEqual(audit["guard_case_pass_count"], 3)
        self.assertEqual(audit["positive_guard_url_reuse_count"], 3)
        self.assertNotIn("c06_positive_semantic_replay_required_before_guard_pass", audit["blockers"])
        replay = audit["source_backed_semantic_replay"]
        self.assertTrue(replay["positive_replay_pass"])
        self.assertEqual(replay["accepted_primitive_ids"], ["customer_preorder_or_allocation"])
        self.assertEqual(replay["accepted_claim_count"], 1)
        self.assertEqual(replay["document_urls"], ["https://ssl.pstatic.net/imgstock/upload/research/company/sk_hynix_memory_20240401.pdf"])
        self.assertEqual(replay["blockers"], [])
        self.assertIn("controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted", audit["semantic_blockers"])
        self.assertIn("samsung_positive_smoke_reuses_c06_guard_urls", audit["semantic_blockers"])
        self.assertEqual(audit["score_contribution_leak_count"], 0)
        self.assertEqual(audit["hard_break_false_positive_count"], 0)
        self.assertEqual(audit["green_unlock_false_positive_count"], 0)
        by_id = {row["guard_case_id"]: row for row in audit["cases"]}
        self.assertIn("C06-GUARD-SAMSUNG-QUALIFICATION-LAG-NOT-4C", by_id)
        lag = by_id["C06-GUARD-SAMSUNG-QUALIFICATION-LAG-NOT-4C"]
        self.assertFalse(lag["expected_hard_break_allowed"])
        self.assertFalse(lag["expected_current_score_eligible"])
        self.assertEqual(lag["score_contribution_ids"], [])
        self.assertFalse(lag["source_proxy_only"])
        self.assertFalse(lag["evidence_url_pending"])


if __name__ == "__main__":
    unittest.main()
