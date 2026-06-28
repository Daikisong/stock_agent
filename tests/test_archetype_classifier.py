import unittest

from e2r.archetype_classifier import classify_v12_archetype
from e2r.calibration.taxonomy import normalise_canonical_archetype_id, normalise_large_sector_id
from e2r.sector_profiles import SectorProfile


class ArchetypeClassifierTests(unittest.TestCase):
    def test_source_backed_canonical_field_overrides_generic_financial_context(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={
                "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
                "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
                "roe": 12.0,
                "pbr_e": 0.8,
                "pf_exposure_reduced": True,
                "balance_sheet_repair": True,
                "cash_collection_visible": True,
            },
            text="financial ROE PBR PF exposure reduced balance sheet repair cash collection visible",
            price_stage_score=0.0,
            revision_score=70.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK")
        self.assertEqual(classification.large_sector_id, "L9_CONSTRUCTION_REALESTATE_HOUSING")
        self.assertEqual(classification.reason, "source_backed_canonical_archetype")

    def test_price_blowoff_does_not_override_semiconductor_route_context(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={"hbm_demand_mentioned": True},
            text="HBM customer capacity and memory demand are visible",
            price_stage_score=100.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_price_blowoff_without_route_context_stays_cross_archetype_watch(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="",
            price_stage_score=100.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM")

    def test_official_financial_actual_context_routes_to_operating_bridge_not_price_only(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={"financial_actuals_present": True, "actual_op_yoy_pct": 80.0},
            text="financial_actuals_present actual operating profit",
            price_stage_score=100.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C01_ORDER_BACKLOG_MARGIN_BRIDGE")

    def test_routine_governance_report_does_not_override_operating_context(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={"financial_actuals_present": True, "actual_op_yoy_pct": 80.0},
            text="기업지배구조보고서공시 최대주주등소유주식변동신고서 financial_actuals_present actual operating profit",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C01_ORDER_BACKLOG_MARGIN_BRIDGE")

    def test_legacy_accounting_text_does_not_route_without_v2_claim(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={"accounting_or_trust_issue": True},
            text="월덱스 주요 고객사는 삼성전자이며 감사의견은 적정이다.",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertNotEqual(
            classification.canonical_archetype_id,
            "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
        )

    def test_v2_claim_backed_accounting_primitive_routes_to_accounting_archetype(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={
                "accounting_or_trust_issue": True,
                "evidence_os_v2_score_eligible_claim_ids_by_primitive": {
                    "accounting_trust_break": ("CLM-ACCOUNTING",),
                },
            },
            text="Target issuer disclosed that its auditor issued an adverse opinion.",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(
            classification.canonical_archetype_id,
            "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
        )

    def test_control_premium_event_routes_to_governance_archetype(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="공개매수 control premium 경영권 인수",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP")

    def test_financial_inventory_field_alone_does_not_route_to_consumer_retail_inventory(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={"financial_actuals_present": True, "inventory": 1200},
            text="분기 재무 업데이트 actual inventory",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C01_ORDER_BACKLOG_MARGIN_BRIDGE")

    def test_consumer_retail_inventory_context_routes_to_c19(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={"sell_through_confirmed": True, "inventory_spike": True},
            text="브랜드 리테일 채널에서 재고 급증과 셀스루 둔화가 확인된다",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C19_BRAND_RETAIL_INVENTORY_MARGIN")

    def test_consumer_retail_context_without_inventory_risk_does_not_route_to_c19(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="브랜드 리테일 채널 확대와 매장 입점이 진행된다",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertNotEqual(classification.canonical_archetype_id, "C19_BRAND_RETAIL_INVENTORY_MARGIN")

    def test_llm_semiconductor_aliases_normalize_to_canonical_taxonomy(self):
        self.assertEqual(normalise_large_sector_id("semiconductors"), "L2_AI_SEMICONDUCTOR_ELECTRONICS")
        self.assertEqual(
            normalise_canonical_archetype_id("ai_hbm_structural_memory_supplier"),
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )

    def test_memory_manufacturer_order_word_does_not_route_to_equipment(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={},
            text="메모리 수요와 파운드리 수주잔고, 생산설비투자 증가가 영업이익 개선으로 연결된다",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_hbm_customer_contract_context_wins_over_memory_price_cycle(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={
                "minimum_revenue_guarantee": True,
                "multi_year_contract": True,
                "memory_price_increase_mentioned": True,
            },
            text=(
                "HBM 장기공급계약 LTA와 최소 매출 보장으로 고객 CAPA 배정이 확인됐다. "
                "동시에 메모리 가격 상승도 나타난다."
            ),
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_hbm_capacity_constraint_without_customer_lock_routes_to_memory_recovery(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={
                "hbm_demand_mentioned": True,
                "memory_price_increase_mentioned": True,
                "supply_discipline_mentioned": True,
                "hbm_capacity_constraint": True,
                "advanced_packaging_bottleneck": True,
                "cycle_demand_visibility": True,
                "supply_demand_tightness": True,
            },
            text=(
                "HBM 수요 증가와 메모리 가격 상승이 확인된다. "
                "DRAM 가격 상승과 NAND 가격 상승, 공급조절로 업황이 개선된다. "
                "HBM CAPA 제약과 advanced packaging bottleneck이 단기 병목으로 남아 있다."
            ),
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE")

    def test_semiconductor_equipment_supplier_context_routes_to_c07(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={},
            text="반도체 장비 공급사가 HBM 후공정 장비 수주와 고객사 purchase order를 확보했다",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH")

    def test_test_word_in_company_name_does_not_create_socket_route(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            company_name="테스트기업",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={},
            text="DRAM recovery cycle price increase",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE")

    def test_equipment_supplier_with_customer_order_still_routes_to_c07(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={"equipment_order_mentioned": True, "customer_preorder_or_allocation": True},
            text="반도체 장비 공급사가 HBM 후공정 장비 수주와 고객사 purchase order를 확보했다",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH")

    def test_memory_hybrid_solution_does_not_route_to_mobility(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={},
            text="D램과 낸드를 결합한 하이브리드 솔루션으로 메모리 수요와 영업이익 개선이 나타난다",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_vehicle_hybrid_sales_context_still_routes_to_mobility(self):
        classification = classify_v12_archetype(
            symbol="CASE",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="완성차 하이브리드 차량 판매대수와 글로벌 도매 판매가 증가했다",
            price_stage_score=0.0,
            revision_score=0.0,
        )

        self.assertEqual(classification.canonical_archetype_id, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")


if __name__ == "__main__":
    unittest.main()
