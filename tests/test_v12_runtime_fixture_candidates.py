import unittest

from e2r.calibration.v12_runtime_fixture_candidates import (
    ARCHETYPE_RUNTIME_BRIDGE_SPECS,
    build_v12_green_runtime_fixture_candidates,
    render_v12_green_runtime_fixture_candidates_report,
)


class V12RuntimeFixtureCandidateTests(unittest.TestCase):
    def test_bridge_specs_keep_gate_required_axes_explicit(self) -> None:
        c06_primitives = ARCHETYPE_RUNTIME_BRIDGE_SPECS["C06_HBM_MEMORY_CUSTOMER_CAPACITY"][
            "expected_runtime_primitives"
        ]
        c10_spec = ARCHETYPE_RUNTIME_BRIDGE_SPECS["C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"]
        c10_primitives = c10_spec["expected_runtime_primitives"]
        c20_primitives = ARCHETYPE_RUNTIME_BRIDGE_SPECS["C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"][
            "expected_runtime_primitives"
        ]

        self.assertIn("customer_preorder_or_allocation", c06_primitives)
        self.assertIn("revenue_visibility_contract", c06_primitives)
        self.assertEqual(c10_spec["runtime_bridge_group"], "semiconductor_memory_recovery_bridge")
        self.assertIn("cycle_demand_visibility", c10_primitives)
        self.assertIn("supply_demand_tightness", c10_primitives)
        self.assertNotIn("customer_contract_visible", c10_primitives)
        self.assertIn("platform_distribution_scale", c20_primitives)

    def test_green_candidates_require_clean_green_and_guard_pair(self) -> None:
        rows = [
            {
                "case_id": "GREEN_C06",
                "trigger_id": "T1",
                "symbol": "000660 SK하이닉스",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-04-25",
                "MFE_180D_pct": 70,
                "evidence_available_at_that_date": "HBM capacity booked and customer allocation visible.",
                "source_proxy_only": False,
                "evidence_url_pending": False,
                "usable_for_weight_calibration": True,
            },
            {
                "case_id": "GREEN_C06_HIGH_MFE_BUT_WEAK_SEMANTIC_MATCH",
                "trigger_id": "T1B",
                "symbol": "007660 이수페타시스",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2023-01-19",
                "MFE_180D_pct": 500,
                "evidence_available_at_that_date": "Server MLB customer expansion and capex response were visible.",
                "source_proxy_only": False,
                "evidence_url_pending": False,
                "usable_for_weight_calibration": True,
            },
            {
                "case_id": "C06_FALSE_GREEN_MARKER",
                "trigger_id": "T1C",
                "symbol": "005930 삼성전자",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-04-05",
                "MFE_180D_pct": 900,
                "evidence_available_at_that_date": "false_green HBM catch-up headline without direct qualification.",
                "source_proxy_only": False,
                "evidence_url_pending": False,
                "usable_for_weight_calibration": True,
            },
            {
                "case_id": "GUARD_C06",
                "trigger_id": "T2",
                "symbol": "005930 삼성전자",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage2-FalsePositive-FoundryMemoryBetaSpike",
                "trigger_date": "2024-05-01",
                "evidence_available_at_that_date": "HBM catch-up headline without direct qualification.",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "GUARD_C06_STAGE4B_LATE",
                "trigger_id": "T2B",
                "symbol": "000660 SK하이닉스",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage4B",
                "trigger_date": "2024-07-11",
                "MAE_180D_pct": 40,
                "evidence_available_at_that_date": "HBM capacity customer evidence stayed valid, but valuation was already late.",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "GREEN_C21_PROXY",
                "trigger_id": "T3",
                "symbol": "000001 금융",
                "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-02-01",
                "source_proxy_only": True,
                "evidence_url_pending": False,
            },
            {
                "case_id": "GREEN_C23",
                "trigger_id": "T4",
                "symbol": "000100 유한양행",
                "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
                "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-09-20",
                "evidence_source": "Reuters approval report",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
        ]

        payload = build_v12_green_runtime_fixture_candidates(rows)
        by_arch = {row["canonical_archetype_id"]: row for row in payload["archetypes"]}

        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["fixture_status"], "ready_for_runtime_replay_fixture")
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["runtime_bridge_group"],
            "semiconductor_customer_capacity_bridge",
        )
        self.assertIn(
            "customer_preorder_or_allocation",
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["expected_runtime_primitives"],
        )
        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["raw_stage3_green_row_count"], 3)
        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["green_row_count"], 2)
        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["green_guard_marker_row_count"], 1)
        self.assertEqual(
            by_arch["C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY"]["fixture_status"],
            "needs_green_row",
        )
        self.assertEqual(by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["fixture_status"], "needs_verified_green_source")
        self.assertEqual(by_arch["C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION"]["fixture_status"], "needs_guard_pair")
        self.assertEqual(payload["ready_archetype_count"], 1)
        self.assertEqual(payload["archetype_count"], 36)
        self.assertEqual(payload["schema_version"], "v12_green_runtime_fixture_candidates_v2")
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["green_fixture_candidate"]["case_id"],
            "GREEN_C06",
        )
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["guard_fixture_candidate"]["case_id"],
            "GUARD_C06",
        )

        report = render_v12_green_runtime_fixture_candidates_report(payload)
        self.assertIn("C06_HBM_MEMORY_CUSTOMER_CAPACITY", report)
        self.assertIn("ready_for_runtime_replay_fixture", report)
        self.assertIn("Replay Fixture Matrix", report)

    def test_proxy_text_overrides_false_flags_for_fixture_cleanliness(self) -> None:
        rows = [
            {
                "case_id": "GREEN_C02",
                "trigger_id": "T1",
                "symbol": "000001",
                "large_sector_id": "L1_CAPEX_BACKLOG_CONTRACTING",
                "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-04-01",
                "evidence_source": "verified exchange disclosure",
                "evidence_available_at_that_date": "Grid order backlog and datacenter customer demand visible.",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "GUARD_C02_PROXY",
                "trigger_id": "T2",
                "symbol": "000002",
                "large_sector_id": "L1_CAPEX_BACKLOG_CONTRACTING",
                "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                "trigger_type": "Stage2-FalsePositive-CapexTheme",
                "trigger_date": "2024-04-02",
                "evidence_source": "source_proxy_only_not_price_only",
                "evidence_available_at_that_date": "source_proxy_only: grid beta visible, but direct backlog absent; verified URL repair pending",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
        ]

        payload = build_v12_green_runtime_fixture_candidates(rows)
        c02 = {row["canonical_archetype_id"]: row for row in payload["archetypes"]}[
            "C02_POWER_GRID_DATACENTER_CAPEX"
        ]

        self.assertEqual(c02["fixture_status"], "needs_guard_pair")
        self.assertEqual(c02["clean_green_row_count"], 1)
        self.assertEqual(c02["clean_guard_row_count"], 0)
        self.assertEqual(c02["source_proxy_only_count"], 1)
        self.assertEqual(c02["evidence_url_pending_count"], 1)
        self.assertTrue(c02["guard_fixture_candidate"]["source_proxy_only"])
        self.assertTrue(c02["guard_fixture_candidate"]["evidence_url_pending"])

    def test_source_backed_structural_success_can_be_green_equivalent_but_local_4b_is_blocked(self) -> None:
        rows = [
            {
                "case_id": "C07_SUCCESS",
                "trigger_id": "C07_T1",
                "symbol": "042700",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
                "trigger_type": "Stage3-Yellow",
                "trigger_date": "2024-02-05",
                "MFE_180D_pct": 233.67,
                "MAE_180D_pct": -0.68,
                "positive_or_counterexample": "positive",
                "case_type": "structural_success",
                "trigger_outcome_label": "named_SK_Hynix_TC_bonder_order_and_capacity_route_unlocked_large_MFE",
                "current_profile_verdict": "current_profile_correct_but_late_4B_overlay_needed_after_peak",
                "stage3_evidence_fields": ["named_customer_order", "backlog_visibility", "financial_visibility"],
                "stage4b_evidence_fields": ["post_peak_drawdown_after_large_MFE"],
                "evidence_available_at_that_date": "TheBell reported named SK Hynix HBM TC-bonder order and capacity route.",
                "evidence_source": "https://example.com/source",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "C07_GUARD",
                "trigger_id": "C07_T2",
                "symbol": "031980",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
                "trigger_type": "Stage4B",
                "trigger_date": "2024-06-14",
                "MAE_180D_pct": -65.38,
                "evidence_available_at_that_date": "HBM packaging premium without direct order-to-revenue bridge.",
                "evidence_source": "https://example.com/guard",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "C12_YELLOW_LOCAL_4B",
                "trigger_id": "C12_T1",
                "symbol": "002710",
                "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
                "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
                "trigger_type": "Stage3-Yellow",
                "trigger_date": "2023-03-09",
                "MFE_180D_pct": 340.35,
                "positive_or_counterexample": "positive",
                "case_type": "battery_can_material_customer_conversion_positive",
                "current_profile_verdict": "current_profile_correct_but_needs_local_4b_exit",
                "stage3_evidence_fields": ["delivery_or_revenue_conversion", "durable_customer_confirmation"],
                "stage4b_evidence_fields": ["contract_delay_or_calloff_risk", "local_4b_watch_guard"],
                "evidence_available_at_that_date": "The row supports Stage3-Yellow, not Stage3-Green, while requiring local 4B watch.",
                "evidence_source": "https://example.com/c12",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "C12_ENCHEM_CUSTOMER_SUPPLY",
                "trigger_id": "C12_T2",
                "symbol": "348370",
                "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
                "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
                "trigger_type": "Stage3-Yellow",
                "trigger_date": "2024-01-25",
                "MFE_180D_pct": 247.27,
                "MAE_180D_pct": -5.55,
                "positive_or_counterexample": "positive",
                "case_type": "structural_success",
                "trigger_outcome_label": "north_america_customer_supply_positive_with_4b_exit_guard",
                "current_profile_verdict": "current_profile_missed_structural_then_needs_local_4b_overlay",
                "stage2_evidence_fields": ["named_cell_customers", "north_america_supply_chain"],
                "stage3_evidence_fields": ["customer_supply_conversion", "shipment_and_capacity_bridge"],
                "stage4b_evidence_fields": ["post_peak_drawdown_watch_after_fast_rerating"],
                "evidence_available_at_that_date": (
                    "North America electrolyte supply: Georgia plant capacity expansion and shipments to "
                    "LGES, SK On, Ultium Cells and BlueOvalSK customers."
                ),
                "evidence_source": "https://example.com/enchem",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "C14_DAEJOO_SURVIVOR",
                "trigger_id": "C14_T1",
                "symbol": "078600",
                "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
                "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
                "trigger_type": "Stage2-Actionable",
                "trigger_date": "2024-04-02",
                "MFE_180D_pct": 80.75,
                "MAE_180D_pct": -18.58,
                "case_type": "structural_success / positive",
                "trigger_outcome_label": "survivor_reopen_positive_silicon_anode",
                "current_profile_verdict": "current_profile_missed_structural_if_generic_ev_slowdown_blocks_survivor",
                "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route"],
                "stage3_evidence_fields": ["financial_visibility", "durable_customer_confirmation"],
                "stage4b_evidence_fields": [],
                "stage4c_evidence_fields": [],
                "evidence_available_at_that_date": (
                    "Silicon-anode sales were expected to exceed the prior full year; coverage expanded "
                    "from two vehicle models to nine and SK On adoption was referenced."
                ),
                "evidence_source": "EV_C14_FU123_DAEJOO_20240402_ETNEWS",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "C24_FALSE_GREEN",
                "trigger_id": "C24_FALSE_GREEN_T1",
                "symbol": "028300",
                "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
                "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-05-16",
                "MFE_180D_pct": 11.59,
                "MAE_180D_pct": -52.87,
                "case_type": "counterexample",
                "trigger_outcome_label": "false_positive_green",
                "current_profile_verdict": "current_profile_false_positive",
                "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"],
                "evidence_available_at_that_date": "Pre-event anticipation existed, but endpoint confirmation was absent.",
                "evidence_source": "https://example.com/c24",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "case_id": "R13_HDHE_CONTROL",
                "trigger_id": "R13_T1",
                "symbol": "267260",
                "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
                "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2025-04-22",
                "MFE_180D_pct": 228.07,
                "MAE_180D_pct": -2.02,
                "trigger_outcome_label": "positive_control_order_backlog_earnings_conversion",
                "current_profile_verdict": "current_profile_should_accept",
                "stage2_evidence_fields": ["official/direct source", "accounting-to-cash bridge"],
                "stage3_evidence_fields": ["multi-field evidence bridge", "forward price validation"],
                "evidence_available_at_that_date": "HD Hyundai Electric Q1 sales, OP, orders and backlog.",
                "evidence_source": "https://example.com/hdhe",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
        ]

        payload = build_v12_green_runtime_fixture_candidates(rows)
        by_arch = {row["canonical_archetype_id"]: row for row in payload["archetypes"]}

        c07 = by_arch["C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"]
        self.assertEqual(c07["fixture_status"], "ready_for_runtime_replay_fixture")
        self.assertEqual(c07["raw_stage3_green_row_count"], 0)
        self.assertEqual(c07["green_row_count"], 1)
        self.assertIn(
            "hbm_customer_order",
            c07["green_fixture_candidate"]["source_expected_runtime_primitives"],
        )

        c12 = by_arch["C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"]
        self.assertEqual(c12["green_row_count"], 1)
        self.assertEqual(c12["fixture_status"], "needs_guard_pair")
        self.assertEqual(c12["green_fixture_candidate"]["case_id"], "C12_ENCHEM_CUSTOMER_SUPPLY")
        self.assertIn(
            "shipment_and_capacity_bridge",
            c12["green_fixture_candidate"]["source_expected_runtime_primitives"],
        )

        c14 = by_arch["C14_EV_DEMAND_SLOWDOWN_4B_4C"]
        self.assertEqual(c14["green_row_count"], 1)
        self.assertEqual(c14["fixture_status"], "needs_guard_pair")
        self.assertIn(
            "survivor_reopen_positive",
            c14["green_fixture_candidate"]["source_expected_runtime_primitives"],
        )

        c24 = by_arch["C24_BIO_TRIAL_DATA_EVENT_RISK"]
        self.assertEqual(c24["green_row_count"], 0)
        self.assertGreaterEqual(c24["guard_row_count"], 1)

        r13 = by_arch["R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION"]
        self.assertEqual(r13["green_row_count"], 1)
        self.assertEqual(
            r13["green_fixture_candidate"]["source_canonical_archetype_id"],
            "C02_POWER_GRID_DATACENTER_CAPEX",
        )

    def test_r13_green_candidate_preserves_source_archetype_primitives(self) -> None:
        rows = [
            {
                "case_id": "R13_C23_YUHAN",
                "trigger_id": "R13_T_C23",
                "symbol": "000100",
                "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
                "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
                "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
                "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-08-20",
                "MFE_180D_pct": 77.55,
                "MAE_180D_pct": -2.66,
                "trigger_outcome_label": "direct_approval_commercialization_bridge",
                "current_profile_verdict": "current_profile_too_late",
                "stage2_evidence_fields": ["FDA approval", "direct economics"],
                "stage3_evidence_fields": ["commercialization", "partner economics", "royalty route"],
                "evidence_available_at_that_date": "FDA approval of Lazcluze/Rybrevant based on MARIPOSA created direct economics commercialization evidence.",
                "evidence_source": "FDA/J&J/Yuhan public approval source",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            }
        ]

        payload = build_v12_green_runtime_fixture_candidates(rows)
        r13 = {
            row["canonical_archetype_id"]: row
            for row in payload["archetypes"]
        }["R13_CROSS_ARCHETYPE_4B_4C_REDTEAM"]

        self.assertEqual(
            r13["green_fixture_candidate"]["source_canonical_archetype_id"],
            "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
        )
        self.assertIn(
            "royalty_route",
            r13["green_fixture_candidate"]["source_expected_runtime_primitives"],
        )
        self.assertIn(
            "partner_economics_visible",
            r13["green_fixture_candidate"]["source_expected_runtime_primitives"],
        )


if __name__ == "__main__":
    unittest.main()
