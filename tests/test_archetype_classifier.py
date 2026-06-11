import unittest

from e2r.archetype_classifier import classify_v12_archetype
from e2r.calibration.taxonomy import normalise_canonical_archetype_id, normalise_large_sector_id
from e2r.sector_profiles import SectorProfile


class ArchetypeClassifierTests(unittest.TestCase):
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
