from datetime import date, datetime
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.agentic import (
    DEFAULT_EVIDENCE_CONTRACT_PATH,
    claim_backed_parsed_fields,
    claim_metadata_from_claims,
    compile_claims_from_primitives,
    evidence_contract_gap_context,
    evidence_contract_for_archetype,
    load_evidence_contracts,
)
from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput
from e2r.models import FinancialActual, Market, ResearchReport
from e2r.pipeline.evidence_builder import evidence_from_feature_domains


class EvidenceClaimTests(unittest.TestCase):
    def test_evidence_contract_config_covers_canonical_archetypes(self):
        contracts = load_evidence_contracts()

        self.assertEqual(len(contracts), 36)
        self.assertEqual(set(contracts), set(CANONICAL_ARCHETYPE_IDS))
        c06 = evidence_contract_for_archetype("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertIsNotNone(c06)
        self.assertIn("customer_preorder_or_allocation", c06.required_primitives)
        self.assertIn("customer_preorder_or_allocation", c06.positive_primitives)
        self.assertIn("hbm_capacity_pre_sold", c06.green_gate_primitives)
        self.assertNotIn("medium_term_revision_visibility", c06.green_gate_primitives)
        self.assertEqual(c06.guard_primitives, ())
        self.assertIn("customer", c06.required_bridge_axes)
        c11 = evidence_contract_for_archetype("C11_BATTERY_ORDERBOOK_RERATING")
        self.assertIn("customer_contract", c11.positive_primitives)
        self.assertIn("customer_contract", c11.green_gate_primitives)
        self.assertIn("call_off_risk", c11.guard_primitives)
        c14 = evidence_contract_for_archetype("C14_EV_DEMAND_SLOWDOWN_4B_4C")
        self.assertEqual(c14.positive_primitives, ())
        self.assertIn("ev_demand_slowdown", c14.guard_primitives)

    def test_guard_only_contract_gap_context_does_not_frame_guards_as_positive_missing(self):
        context = evidence_contract_gap_context("C14_EV_DEMAND_SLOWDOWN_4B_4C")[0]

        self.assertIn("positive_primitives=none", context)
        self.assertIn("missing_positive_primitives=none", context)
        self.assertIn("missing_required_primitives=ev_demand_slowdown", context)
        self.assertIn("guard_primitives_to_check=ev_demand_slowdown", context)
        self.assertIn("missing_guard_primitives=ev_demand_slowdown", context)
        self.assertIn("where applicable and verify guard primitives", context)

        c14 = evidence_contract_for_archetype("C14_EV_DEMAND_SLOWDOWN_4B_4C")
        present_context = evidence_contract_gap_context(
            "C14_EV_DEMAND_SLOWDOWN_4B_4C",
            present_primitives=c14.guard_primitives,
        )[0]
        self.assertIn("present_guard_primitives=ev_demand_slowdown", present_context)
        self.assertIn("missing_guard_primitives=none", present_context)

    def test_positive_contract_gap_context_lists_positive_and_missing_positive_separately(self):
        context = evidence_contract_gap_context(
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            present_primitives=("hbm_capacity_pre_sold",),
        )[0]

        self.assertIn("positive_primitives=customer_preorder_or_allocation", context)
        self.assertIn("hbm_capacity_pre_sold", context)
        missing_positive = context.split("missing_positive_primitives=", 1)[1].split(
            "; missing_green_gate_primitives",
            1,
        )[0]
        self.assertIn("customer_preorder_or_allocation", missing_positive)
        self.assertNotIn("hbm_capacity_pre_sold", missing_positive)

    def test_evidence_contract_config_rejects_duplicate_or_count_mismatch(self):
        payload = json.loads(DEFAULT_EVIDENCE_CONTRACT_PATH.read_text())
        with TemporaryDirectory() as tmp:
            duplicate_path = Path(tmp) / "duplicate_contracts.json"
            duplicate_payload = {
                **payload,
                "contract_count": payload["contract_count"] + 1,
                "contracts": payload["contracts"] + [payload["contracts"][0]],
            }
            duplicate_path.write_text(json.dumps(duplicate_payload), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "duplicate evidence contract"):
                load_evidence_contracts(path=duplicate_path)

            count_mismatch_path = Path(tmp) / "count_mismatch_contracts.json"
            count_mismatch_payload = {**payload, "contract_count": payload["contract_count"] + 1}
            count_mismatch_path.write_text(json.dumps(count_mismatch_payload), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "contract_count mismatch"):
                load_evidence_contracts(path=count_mismatch_path)

    def test_compile_claims_from_primitives_builds_stable_claim_metadata(self):
        claims = compile_claims_from_primitives(
            evidence_id="evidence:000660:2024-04-25:C06",
            symbol="000660",
            as_of_date=date(2024, 4, 25),
            primitive_ids=("hbm_capacity_pre_sold", "hbm_capacity_pre_sold", "customer_preorder_or_allocation"),
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            subject="SK Hynix",
            quote_text="HBM capacity was sold out and customer allocation was visible.",
            source_url="https://example.com/hbm",
            source_tier=1,
            confidence=0.92,
        )

        claims_again = compile_claims_from_primitives(
            evidence_id="evidence:000660:2024-04-25:C06",
            symbol="000660",
            as_of_date=date(2024, 4, 25),
            primitive_ids=("hbm_capacity_pre_sold", "customer_preorder_or_allocation"),
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            subject="SK Hynix",
            quote_text="HBM capacity was sold out and customer allocation was visible.",
            source_url="https://example.com/hbm",
            source_tier=1,
            confidence=0.92,
        )

        self.assertEqual(tuple(item.claim_id for item in claims), tuple(item.claim_id for item in claims_again))
        self.assertEqual(len(claims), 2)

        metadata = claim_metadata_from_claims(claims, as_of_date=date(2024, 4, 25))

        self.assertEqual(metadata["claim_ledger_version"], "e2r-claim-ledger-v1")
        self.assertEqual(metadata["compiled_claim_count"], 2)
        self.assertIn("hbm_capacity_pre_sold", metadata["compiled_claim_ids_by_primitive"])
        self.assertEqual(metadata["compiled_primitive_states"]["hbm_capacity_pre_sold"]["status"], "PRESENT")
        self.assertTrue(metadata["compiled_primitive_states"]["hbm_capacity_pre_sold"]["support_claim_ids"])

    def test_evidence_builder_attaches_claim_ledger_to_report_fields(self):
        report = ResearchReport(
            symbol="000660",
            publish_date=date(2024, 4, 25),
            broker="FixtureBroker",
            title="SK Hynix HBM sold-out report",
            as_of_date=date(2024, 4, 25),
            raw_text="HBM capacity was sold out and customer allocation was visible.",
            parsed_fields={
                "hbm_capacity_pre_sold": True,
                "customer_preorder_or_allocation": True,
                "parser_confidence": 0.9,
            },
        )

        evidence = evidence_from_feature_domains(
            market=Market.KR,
            fallback_symbol="000660",
            research_reports=(report,),
        )[0]

        fields = evidence.parsed_fields
        self.assertEqual(fields["claim_ledger_version"], "e2r-claim-ledger-v1")
        self.assertIn("hbm_capacity_pre_sold", fields["compiled_claim_ids_by_primitive"])
        self.assertIn("customer_preorder_or_allocation", fields["compiled_claim_ids_by_primitive"])
        self.assertNotIn("parser_confidence", fields["compiled_claim_ids_by_primitive"])

    def test_claim_compiler_excludes_runtime_bookkeeping_fields(self):
        fields = claim_backed_parsed_fields(
            evidence_id="research:000660:2024-04-25:FixtureBroker",
            symbol="000660",
            as_of_date=date(2024, 4, 25),
            parsed_fields={
                "hbm_capacity_pre_sold": True,
                "date_verified": True,
                "green_allowed_by_date": True,
                "runtime_fixture_source_backed": True,
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "evidence_contract_coverage_pct": 100.0,
            },
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            subject="SK Hynix",
            quote_text="HBM capacity was sold out.",
            source_tier=1,
            confidence=0.9,
        )

        primitives = fields["compiled_claim_ids_by_primitive"]

        self.assertEqual(set(primitives), {"hbm_capacity_pre_sold"})

    def test_feature_engineer_passes_claim_ids_to_score_contribution_audit(self):
        parsed_fields = claim_backed_parsed_fields(
            evidence_id="research:000660:2024-04-25:FixtureBroker",
            symbol="000660",
            as_of_date=date(2024, 4, 25),
            parsed_fields={
                "hbm_capacity_pre_sold": True,
                "customer_preorder_or_allocation": True,
                "hbm_capacity_constraint": True,
                "parser_confidence": 0.9,
            },
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            subject="SK Hynix",
            quote_text="HBM capacity was sold out and customer allocation was visible.",
            source_tier=1,
            confidence=0.9,
        )
        report = ResearchReport(
            symbol="000660",
            publish_date=date(2024, 4, 25),
            broker="FixtureBroker",
            title="SK Hynix HBM sold-out report",
            as_of_date=date(2024, 4, 25),
            raw_text="HBM capacity was sold out and customer allocation was visible.",
            parsed_fields=parsed_fields,
        )

        result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="000660",
                as_of_date=date(2024, 4, 25),
                company_name="SK Hynix",
                sector_context="semiconductor",
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                research_reports=(report,),
            )
        )
        score = result.score()

        self.assertGreaterEqual(score.diagnostic_scores["claim_backed_claim_count_capped"], 3.0)
        self.assertGreater(score.diagnostic_scores["score_claim_backed_component_count_capped"], 0.0)
        self.assertEqual(score.diagnostic_scores["orphan_score_component_count_capped"], 0.0)
        self.assertEqual(score.diagnostic_scores["evidence_contract_required_primitive_count_capped"], 6.0)
        self.assertEqual(score.diagnostic_scores["evidence_contract_present_primitive_count_capped"], 3.0)
        self.assertEqual(score.diagnostic_scores["evidence_contract_positive_present_primitive_count_capped"], 3.0)
        self.assertEqual(score.diagnostic_scores["evidence_contract_positive_coverage_pct"], 50.0)
        self.assertEqual(score.diagnostic_scores["evidence_contract_green_gate_present_primitive_count_capped"], 3.0)
        self.assertEqual(score.diagnostic_scores["evidence_contract_green_gate_coverage_pct"], 75.0)
        self.assertEqual(score.diagnostic_scores["evidence_contract_guard_required_primitive_count_capped"], 0.0)
        self.assertIn("medium_term_revision_visibility", result.source_fields["evidence_contract_missing_primitives"])

    def test_guard_only_contract_has_no_positive_coverage(self):
        class FieldStub:
            def score_claim_ids_by_primitive(self):
                return {"ev_demand_slowdown": ("CLM-EV",)}

        coverage = DeterministicFeatureEngineer._evidence_contract_coverage(
            "C14_EV_DEMAND_SLOWDOWN_4B_4C",
            FieldStub(),
        )

        diagnostics = coverage["diagnostics"]
        source_fields = coverage["source_fields"]
        self.assertEqual(diagnostics["evidence_contract_positive_required_primitive_count_capped"], 0.0)
        self.assertEqual(diagnostics["evidence_contract_positive_coverage_pct"], 0.0)
        self.assertEqual(diagnostics["evidence_contract_guard_only_contract"], 100.0)
        self.assertEqual(diagnostics["evidence_contract_guard_present_primitive_count_capped"], 1.0)
        self.assertIn("ev_demand_slowdown", source_fields["evidence_contract_guard_present_primitives"])

    def test_guard_counter_claim_clears_missing_without_marking_guard_present(self):
        claims = compile_claims_from_primitives(
            evidence_id="evidence:267260:2023-07-27:C03",
            symbol="267260",
            as_of_date=date(2023, 7, 27),
            primitive_ids=("cost_overrun",),
            archetype_id="C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
            subject="Fixture Company",
            quote_text="Cost overrun risk was checked and not found as of the report date.",
            source_tier=1,
            polarity="negative",
        )
        metadata = claim_metadata_from_claims(claims, as_of_date=date(2023, 7, 27))

        class FieldStub:
            def score_claim_ids_by_primitive(self):
                return {
                    primitive: tuple(claim_ids)
                    for primitive, claim_ids in metadata["compiled_claim_ids_by_primitive"].items()
                }

            def score_support_claim_ids_by_primitive(self):
                return {
                    primitive: tuple(state["support_claim_ids"])
                    for primitive, state in metadata["compiled_primitive_states"].items()
                    if state["support_claim_ids"]
                }

            def score_counter_claim_ids_by_primitive(self):
                return {
                    primitive: tuple(state["counter_claim_ids"])
                    for primitive, state in metadata["compiled_primitive_states"].items()
                    if state["counter_claim_ids"]
                }

        coverage = DeterministicFeatureEngineer._evidence_contract_coverage(
            "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
            FieldStub(),
        )

        diagnostics = coverage["diagnostics"]
        source_fields = coverage["source_fields"]
        self.assertEqual(diagnostics["evidence_contract_guard_present_primitive_count_capped"], 0.0)
        self.assertEqual(diagnostics["evidence_contract_guard_cleared_primitive_count_capped"], 1.0)
        self.assertEqual(diagnostics["evidence_contract_guard_missing_primitive_count_capped"], 0.0)
        self.assertIn("cost_overrun", source_fields["evidence_contract_guard_cleared_primitives"])
        self.assertNotIn("cost_overrun", source_fields["evidence_contract_guard_present_primitives"])

    def test_capacity_numeric_claim_alias_counts_for_capacity_constraint_gate(self):
        parsed_fields = claim_backed_parsed_fields(
            evidence_id="research:267260:2023-07-27:FixtureBroker",
            symbol="267260",
            as_of_date=date(2023, 7, 27),
            parsed_fields={
                "order_backlog_to_sales": 1.55,
                "capa_utilization_pct": 96,
                "pricing_power_confirmed": True,
            },
            archetype_id="C02_POWER_GRID_DATACENTER_CAPEX",
            subject="HD Hyundai Electric",
            quote_text="Backlog, high utilization, and pricing power were reported.",
            source_tier=1,
            confidence=0.9,
        )
        report = ResearchReport(
            symbol="267260",
            publish_date=date(2023, 7, 27),
            broker="FixtureBroker",
            title="Power equipment report",
            as_of_date=date(2023, 7, 27),
            raw_text="Backlog, high utilization, and pricing power were reported.",
            parsed_fields=parsed_fields,
        )

        result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="267260",
                as_of_date=date(2023, 7, 27),
                company_name="HD Hyundai Electric",
                sector_context="power_equipment",
                canonical_archetype_id="C02_POWER_GRID_DATACENTER_CAPEX",
                research_reports=(report,),
            )
        )

        self.assertIn("capacity_constraint", result.source_fields["evidence_contract_green_gate_present_primitives"])
        self.assertEqual(result.payload.diagnostic_scores["evidence_contract_green_gate_coverage_pct"], 100.0)

    def test_score_contribution_claim_mapping_is_component_specific(self):
        class FieldStub:
            def score_claim_ids_by_primitive(self):
                return {"hbm_capacity_pre_sold": ("CLM-HBM",)}

        mapping = DeterministicFeatureEngineer._score_contribution_claim_ids(
            FieldStub(),
            {
                "eps_fcf_explosion": 1.0,
                "earnings_visibility": 1.0,
                "bottleneck_pricing": 1.0,
                "market_mispricing": 1.0,
                "valuation_rerating": 1.0,
                "capital_allocation": 1.0,
                "information_confidence": 1.0,
            },
        )

        self.assertNotIn("eps_fcf_explosion", mapping)
        self.assertNotIn("capital_allocation", mapping)
        self.assertEqual(mapping["bottleneck_pricing"], ("CLM-HBM",))
        self.assertEqual(mapping["information_confidence"], ("CLM-HBM",))

    def test_feature_engineer_claim_backs_official_actual_contributions(self):
        prior = FinancialActual(
            symbol="000660",
            fiscal_year=2023,
            fiscal_quarter=1,
            period_end=date(2023, 3, 31),
            reported_at=datetime(2023, 4, 25),
            as_of_date=date(2024, 4, 25),
            source="official",
            sales=1_000.0,
            operating_profit=100.0,
            net_income=80.0,
            eps=100.0,
            cashflow_from_operations=90.0,
            fcf=70.0,
            opm=10.0,
        )
        latest = FinancialActual(
            symbol="000660",
            fiscal_year=2024,
            fiscal_quarter=1,
            period_end=date(2024, 3, 31),
            reported_at=datetime(2024, 4, 25),
            as_of_date=date(2024, 4, 25),
            source="official",
            sales=2_000.0,
            operating_profit=500.0,
            net_income=420.0,
            eps=520.0,
            cashflow_from_operations=430.0,
            fcf=360.0,
            opm=25.0,
        )

        result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="000660",
                as_of_date=date(2024, 4, 25),
                company_name="SK Hynix",
                financial_actuals=(prior, latest),
            )
        )

        self.assertGreater(result.payload.components["eps_fcf_explosion"], 0.0)
        self.assertIn("eps_fcf_explosion", result.payload.score_contribution_claim_ids)
        self.assertGreater(result.payload.diagnostic_scores["claim_backed_claim_count_capped"], 0.0)


if __name__ == "__main__":
    unittest.main()
