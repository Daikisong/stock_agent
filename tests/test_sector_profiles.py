from dataclasses import replace
from datetime import date, datetime
import unittest

from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput
from e2r.archetype_classifier import classify_v12_archetype
from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.models import ConsensusRevision, ConsensusSnapshot, FinancialActual, PriceBar, ResearchReport, Stage
from e2r.red_team import RedTeamEngine
from e2r.sector_profiles import SectorProfile, infer_sector_profile, profile_for_archetype, profile_name_from_diagnostic
from e2r.stage_gate_diagnostics import promotion_band
from e2r.staging import StageClassificationInput, StageClassifier


def _bar(day: int, low: float, high: float, close: float) -> PriceBar:
    as_of_date = date(2024, 5, day)
    return PriceBar(
        symbol="CASE",
        date=as_of_date,
        open=close,
        high=high,
        low=low,
        close=close,
        adj_close=close,
        volume=1000,
        trading_value=close * 1000,
        market_cap=1_000_000_000,
        source="test",
        as_of_date=as_of_date,
    )


def _rich_input(title: str, parsed_fields: dict) -> FeatureEngineeringInput:
    as_of_date = date(2024, 5, 16)
    return FeatureEngineeringInput(
        symbol="CASE",
        as_of_date=as_of_date,
        price_bars=(_bar(1, 80, 100, 90), _bar(16, 120, 150, 145)),
        financial_actuals=(
            FinancialActual(
                symbol="CASE",
                fiscal_year=2023,
                fiscal_quarter=4,
                period_end=date(2023, 12, 31),
                reported_at=datetime(2024, 2, 15, 8, 0),
                as_of_date=as_of_date,
                source="test",
                sales=1000,
                operating_profit=100,
                net_income=80,
                eps=100,
                fcf=80,
            ),
        ),
        consensus=(
            ConsensusSnapshot(
                symbol="CASE",
                date=as_of_date,
                fiscal_year=2024,
                as_of_date=as_of_date,
                source="test",
                sales_e=1700,
                op_e=420,
                eps_e=420,
                per_e=12,
                pbr_e=2,
                analyst_count=4,
            ),
        ),
        consensus_revisions=(
            ConsensusRevision(
                symbol="CASE",
                date=as_of_date,
                fiscal_year=2024,
                as_of_date=as_of_date,
                eps_revision_1m=35,
                op_revision_1m=35,
                target_price_revision_1m=40,
            ),
        ),
        research_reports=(
            ResearchReport(
                symbol="CASE",
                publish_date=as_of_date,
                broker="Test",
                title=title,
                as_of_date=as_of_date,
                target_revision_pct=40,
                fy1_op=420,
                fy1_eps=420,
                fy2_op=570,
                fy2_eps=560,
                est_per=12,
                parsed_fields=parsed_fields,
                raw_text=title,
            ),
        ),
    )


class SectorProfileTests(unittest.TestCase):
    def test_canonical_archetypes_have_profile_mapping(self):
        missing = [item for item in CANONICAL_ARCHETYPE_IDS if profile_for_archetype(item) is None]

        self.assertEqual(missing, [])
        self.assertEqual(profile_for_archetype("C06_HBM_MEMORY_CUSTOMER_CAPACITY"), SectorProfile.MEMORY_HBM)
        self.assertEqual(profile_for_archetype("C01_ORDER_BACKLOG_MARGIN_BRIDGE"), SectorProfile.GENERIC)
        self.assertEqual(profile_for_archetype("C18_CONSUMER_EXPORT_CHANNEL_REORDER"), SectorProfile.K_FOOD_EXPORT)
        self.assertEqual(profile_for_archetype("C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"), SectorProfile.K_BEAUTY_EXPORT)
        self.assertEqual(profile_for_archetype("C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"), SectorProfile.FINANCIAL_CAPITAL_RETURN)
        self.assertEqual(profile_for_archetype("C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION"), SectorProfile.BIO_COMMERCIALIZATION)
        self.assertEqual(profile_for_archetype("C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"), SectorProfile.SOFTWARE_SECURITY)

    def test_profile_inference_from_keywords(self):
        self.assertEqual(infer_sector_profile(text="초고압 변압기 리드타임 장기화"), SectorProfile.POWER_EQUIPMENT)
        self.assertEqual(infer_sector_profile(text="방산 K9 폴란드 정부 고객"), SectorProfile.DEFENSE)
        self.assertEqual(infer_sector_profile(text="불닭 수출 비중 확대"), SectorProfile.K_FOOD_EXPORT)
        self.assertEqual(infer_sector_profile(text="실리콘투 K-뷰티 해외 채널 확장"), SectorProfile.K_BEAUTY_EXPORT)
        self.assertEqual(infer_sector_profile(text="HBM 수요 증가 메모리 가격 상승"), SectorProfile.MEMORY_HBM)
        self.assertEqual(infer_sector_profile(text="AI 데이터센터 GPU 클라우드 매출 확대"), SectorProfile.AI_INFRA_PLATFORM)
        self.assertEqual(infer_sector_profile(text="저PBR 은행 자사주 소각 주주환원"), SectorProfile.FINANCIAL_CAPITAL_RETURN)
        self.assertEqual(infer_sector_profile(text="보험 CSM 증가 K-ICS 손해율 개선"), SectorProfile.INSURANCE_RESERVE)
        self.assertEqual(infer_sector_profile(text="FDA 승인 이후 상업화 로열티"), SectorProfile.BIO_COMMERCIALIZATION)
        self.assertEqual(infer_sector_profile(text="SaaS ARR NRR renewal retention"), SectorProfile.SOFTWARE_SECURITY)

    def test_hbm_supplier_profile_is_not_stolen_by_nvidia_datacenter_terms(self):
        profile = infer_sector_profile(
            company_name="SK하이닉스",
            sector_custom="semiconductor",
            text="AI 데이터센터 HBM D램 엔비디아 메모리 공급부족과 가격 상승",
        )
        routed = classify_v12_archetype(
            symbol="000660",
            company_name="SK하이닉스",
            sector_context="semiconductor",
            sector_profile=profile,
            parsed_fields={"hbm_demand_mentioned": True, "memory_price_increase_mentioned": True},
            text="AI 데이터센터 HBM D램 엔비디아 메모리 공급부족과 가격 상승",
        )

        self.assertEqual(profile, SectorProfile.MEMORY_HBM)
        self.assertNotEqual(routed.canonical_archetype_id, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG")
        self.assertTrue(routed.canonical_archetype_id.startswith(("C06", "C10")))

    def test_hbm_capacity_and_backlog_fields_do_not_force_power_equipment_profile(self):
        profile = infer_sector_profile(
            company_name="테스트메모리",
            sector_custom="semiconductor memory",
            text="HBM D램 고객 물량 배정과 CAPA 제약, 수주잔고 가시성이 같이 확인된다.",
            parsed_fields={
                "hbm_demand_mentioned": True,
                "hbm_capacity_constraint": True,
                "customer_preorder_or_allocation": True,
                "capa_utilization_pct": 100,
                "order_backlog_to_sales": 1.5,
            },
        )

        self.assertEqual(profile, SectorProfile.MEMORY_HBM)

    def test_structured_hbm_supplier_evidence_beats_gpu_cloud_noise_without_sector_metadata(self):
        profile = infer_sector_profile(
            company_name="테스트메모리",
            sector_custom=None,
            text=(
                "HBM D램 수요 증가와 메모리 가격 상승이 실적 중심축이다. "
                "엔비디아 GPU와 빅테크 클라우드 매출 성장도 시장 수요 배경으로 언급됐다."
            ),
            parsed_fields={
                "hbm_demand_mentioned": True,
                "memory_price_increase_mentioned": True,
                "gpu_cloud_revenue_visible": True,
                "cloud_revenue_growth_visible": True,
                "nvidia_momentum_mentioned": True,
            },
        )
        routed = classify_v12_archetype(
            symbol="MEMORY",
            company_name="테스트메모리",
            sector_context=None,
            sector_profile=profile,
            parsed_fields={"hbm_demand_mentioned": True, "memory_price_increase_mentioned": True},
            text="HBM D램 수요 증가와 메모리 가격 상승, 엔비디아 GPU 클라우드 매출 성장",
        )

        self.assertEqual(profile, SectorProfile.MEMORY_HBM)
        self.assertNotEqual(routed.canonical_archetype_id, "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE")

    def test_hbm_memory_manufacturer_is_not_routed_to_test_socket_from_equipment_noise(self):
        routed = classify_v12_archetype(
            symbol="MEMORY",
            company_name="테스트메모리",
            sector_context=None,
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={"hbm_demand_mentioned": True, "memory_price_increase_mentioned": True},
            text=(
                "HBM D램 수요 증가와 메모리 가격 상승으로 실적 중심축이 바뀌었다. "
                "관련 문장에는 검사장비 테스트와 장비 발주 이슈도 언급됐다."
            ),
        )

        self.assertIn(
            routed.canonical_archetype_id,
            {"C06_HBM_MEMORY_CUSTOMER_CAPACITY", "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"},
        )

    def test_semiconductor_test_socket_supplier_still_routes_to_c08(self):
        routed = classify_v12_archetype(
            symbol="SOCKET",
            company_name="테스트소켓",
            sector_context="semiconductor",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={},
            text="HBM 테스트 소켓 고객 qualification 통과와 반복 매출 전환",
        )

        self.assertEqual(routed.canonical_archetype_id, "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY")

    def test_platform_metadata_still_wins_when_hbm_is_related_news_noise(self):
        profile = infer_sector_profile(
            company_name="플랫폼테스트",
            sector_custom="platform internet",
            text=(
                "AI 데이터센터 GPU 클라우드 매출과 검색 광고 플랫폼 매출이 확대된다. "
                "관련 시장 문장에는 HBM과 메모리 가격 상승도 언급됐다."
            ),
            parsed_fields={
                "gpu_cloud_revenue_visible": True,
                "cloud_revenue_growth_visible": True,
                "hbm_demand_mentioned": True,
                "memory_price_increase_mentioned": True,
            },
        )

        self.assertEqual(profile, SectorProfile.AI_INFRA_PLATFORM)

    def test_power_equipment_profile_is_not_stolen_by_datacenter_ai_terms(self):
        profile = infer_sector_profile(
            company_name="전력기기 테스트",
            sector_custom="power_equipment",
            text="AI 데이터센터 전력망 변압기 수주와 리드타임 장기화",
        )

        self.assertEqual(profile, SectorProfile.POWER_EQUIPMENT)

    def test_site_search_ad_words_do_not_create_ai_platform_profile(self):
        profile = infer_sector_profile(
            company_name="현대차",
            sector_custom="auto",
            text="현대차는 하이브리드 마진 개선이 기대된다. 기사검색 검색버튼 광고문의.",
        )

        self.assertNotEqual(profile, SectorProfile.AI_INFRA_PLATFORM)

    def test_non_semiconductor_metadata_blocks_marketwide_hbm_noise(self):
        auto_profile = infer_sector_profile(
            company_name="현대차",
            sector_custom="auto",
            text="현대차 마진 개선 기사. 시장 관련기사: 삼성전자 SK하이닉스 HBM 메모리 급등.",
        )
        bio_profile = infer_sector_profile(
            company_name="알테오젠",
            sector_custom="biotech",
            text="알테오젠 기술이전 기사. 시장 관련기사: SK하이닉스 HBM 메모리 가격 상승.",
        )

        self.assertNotEqual(auto_profile, SectorProfile.MEMORY_HBM)
        self.assertNotEqual(bio_profile, SectorProfile.MEMORY_HBM)

    def test_sector_metadata_blocks_marketwide_power_noise(self):
        semi_profile = infer_sector_profile(
            company_name="SK하이닉스",
            sector_custom="semiconductor",
            text="SK하이닉스 HBM 메모리 수요 증가. 관련기사: AI 데이터센터 전력망 투자 확대.",
        )
        auto_profile = infer_sector_profile(
            company_name="현대차",
            sector_custom="auto",
            text="현대차 하이브리드 마진 개선. 관련기사: AI 데이터센터 전력망 투자 확대.",
        )

        self.assertEqual(semi_profile, SectorProfile.MEMORY_HBM)
        self.assertNotEqual(auto_profile, SectorProfile.POWER_EQUIPMENT)

    def test_generic_food_word_does_not_route_biotech_to_k_food(self):
        profile = infer_sector_profile(
            company_name="알테오젠",
            sector_custom="biotech",
            text="알테오젠 기술이전과 식품의약품안전처 허가 일정이 언급됐다.",
        )

        self.assertNotEqual(profile, SectorProfile.K_FOOD_EXPORT)

    def test_consumer_and_defense_related_news_do_not_override_blocked_metadata(self):
        bio_profile = infer_sector_profile(
            company_name="알테오젠",
            sector_custom="biotech",
            text="알테오젠 기술이전 기사. 관련기사: K-뷰티 수출과 K-방산 수출 증가.",
        )
        auto_profile = infer_sector_profile(
            company_name="현대모비스",
            sector_custom="auto parts",
            text="현대모비스 수익성 개선 기사. 관련기사: K-방산 수출 계약.",
        )

        self.assertNotEqual(bio_profile, SectorProfile.K_BEAUTY_EXPORT)
        self.assertNotEqual(auto_profile, SectorProfile.DEFENSE)

    def test_mobility_and_holding_contexts_win_before_battery_or_hbm_fallback(self):
        auto_route = classify_v12_archetype(
            symbol="005380",
            company_name="현대차",
            sector_context="auto",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="현대차 하이브리드 마진 개선. 관련기사: 배터리 JV AMPC.",
        )
        holding_route = classify_v12_archetype(
            symbol="402340",
            company_name="SK스퀘어",
            sector_context="holding",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="SK스퀘어 자회사 SK하이닉스 HBM 실적과 지분법 이익 확대.",
        )

        self.assertEqual(auto_route.canonical_archetype_id, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(holding_route.canonical_archetype_id, "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN")

    def test_holding_metadata_blocks_direct_memory_manufacturer_profile(self):
        profile = infer_sector_profile(
            company_name="테스트스퀘어",
            sector_custom="지주 투자회사 반도체 ICT",
            text="테스트스퀘어는 자회사 HBM 반도체 지분가치와 순자산가치가 부각됐다.",
        )
        routed = classify_v12_archetype(
            symbol="HOLD",
            company_name="테스트스퀘어",
            sector_context="지주 투자회사 반도체 ICT",
            sector_profile=profile,
            parsed_fields={},
            text="자회사 HBM 반도체 지분가치와 순자산가치가 부각됐다.",
        )

        self.assertEqual(profile, SectorProfile.GENERIC)
        self.assertEqual(routed.canonical_archetype_id, "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN")

    def test_mobility_business_context_blocks_battery_noise_without_metadata(self):
        profile = infer_sector_profile(
            company_name="테스트완성차",
            sector_custom=None,
            text="테스트완성차 글로벌 도매 판매와 하이브리드 마진 개선. 관련기사: 배터리 JV AMPC.",
        )
        routed = classify_v12_archetype(
            symbol="AUTO",
            company_name="테스트완성차",
            sector_context=None,
            sector_profile=profile,
            parsed_fields={},
            text="글로벌 도매 판매와 하이브리드 마진 개선. 관련기사: 배터리 JV AMPC.",
        )

        self.assertNotEqual(profile, SectorProfile.BATTERY_OVERHEAT)
        self.assertEqual(routed.canonical_archetype_id, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")

    def test_memory_word_alone_does_not_create_generic_hbm_route(self):
        routed = classify_v12_archetype(
            symbol="GENERIC",
            company_name="일반기업",
            sector_context=None,
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="일반기업 실적 회복 기사. 시장 관련기사: 메모리 업황 코멘트.",
        )

        self.assertNotEqual(routed.canonical_archetype_id, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_power_grid_context_wins_over_loose_nuclear_word(self):
        routed = classify_v12_archetype(
            symbol="POWER",
            company_name="전력기기",
            sector_context="power_equipment",
            sector_profile=SectorProfile.POWER_EQUIPMENT,
            parsed_fields={"record_backlog": True},
            text="AI 데이터센터 전력망 변압기 수주잔고 증가. 관련 문단에 원전 정책도 언급됐다.",
        )

        self.assertEqual(routed.canonical_archetype_id, "C02_POWER_GRID_DATACENTER_CAPEX")

    def test_holding_context_wins_over_marketwide_defense_rotation_noise(self):
        routed = classify_v12_archetype(
            symbol="HOLD",
            company_name="테스트지주",
            sector_context="holding",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="테스트지주는 자회사 지분가치가 부각됐다. 관련 시장문장: 방산업은 중장기 수주잔고가 늘었다.",
        )

        self.assertEqual(routed.canonical_archetype_id, "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN")

    def test_naver_url_does_not_count_as_financial_nav_token(self):
        routed = classify_v12_archetype(
            symbol="BIO",
            company_name="테스트바이오",
            sector_context="biotech",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="테스트바이오 임상 데이터 이벤트 기사 https://news.example.com/?division=NAVER",
        )

        self.assertNotEqual(routed.canonical_archetype_id, "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN")

    def test_bio_approval_context_wins_over_health_insurance_word(self):
        routed = classify_v12_archetype(
            symbol="BIO",
            company_name="테스트바이오",
            sector_context="biotech",
            sector_profile=SectorProfile.GENERIC,
            parsed_fields={},
            text="테스트바이오 바이오시밀러 품목허가 승인. 의료보험시스템 재정부담 감소가 기대된다.",
        )

        self.assertEqual(routed.canonical_archetype_id, "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION")

    def test_loose_ai_parts_phrase_does_not_create_memory_profile(self):
        profile = infer_sector_profile(
            company_name="전자부품테스트",
            sector_custom="electronics",
            text="전자부품테스트는 AI 모빌리티 핵심 부품 수요와 로봇 밸류체인 편입을 언급했다.",
        )

        self.assertNotEqual(profile, SectorProfile.MEMORY_HBM)

    def test_ai_component_supplier_is_semiconductor_not_platform(self):
        profile = infer_sector_profile(
            company_name="삼성전기",
            sector_custom="electronics",
            text="AI 서버용 MLCC와 FC-BGA 반도체 기판 수요가 증가하고 장기공급계약이 확대된다.",
        )

        self.assertEqual(profile, SectorProfile.MEMORY_HBM)

    def test_loose_defense_footer_keyword_does_not_route_to_c03(self):
        routed = classify_v12_archetype(
            symbol="000660",
            company_name="SK하이닉스",
            sector_context="semiconductor",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={"hbm_demand_mentioned": True},
            text="SK하이닉스 HBM 수요 증가와 메모리 공급부족. 하단 메뉴: 중공업·방산.",
        )

        self.assertNotEqual(routed.canonical_archetype_id, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG")

    def test_memory_profile_is_not_overridden_by_unrelated_defense_export_footer(self):
        routed = classify_v12_archetype(
            symbol="000660",
            company_name="SK하이닉스",
            sector_context="semiconductor",
            sector_profile=SectorProfile.MEMORY_HBM,
            parsed_fields={"hbm_demand_mentioned": True},
            text=(
                "SK하이닉스 HBM 수요 증가와 메모리 공급부족. "
                "관련기사: K-방산 수출 운명의 분수령, 폴란드 훈련서 K2·K9 전개."
            ),
        )

        self.assertNotEqual(routed.canonical_archetype_id, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG")

    def test_ai_infra_profile_routes_to_existing_runtime_archetype(self):
        platform = classify_v12_archetype(
            symbol="035420",
            company_name="NAVER",
            sector_context="platform",
            sector_profile=SectorProfile.AI_INFRA_PLATFORM,
            parsed_fields={"gpu_cloud_revenue_visible": True},
            text="AI 클라우드 매출 성장",
        )
        datacenter_capex = classify_v12_archetype(
            symbol="TEST",
            company_name="데이터센터",
            sector_context=None,
            sector_profile=SectorProfile.AI_INFRA_PLATFORM,
            parsed_fields={"datacenter_capacity_constraint": True},
            text="데이터센터 CAPEX 전력 용량 제약",
        )

        self.assertEqual(platform.canonical_archetype_id, "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE")
        self.assertEqual(datacenter_capex.canonical_archetype_id, "C02_POWER_GRID_DATACENTER_CAPEX")

    def test_ai_infra_platform_route_is_not_stolen_by_memory_news_tokens(self):
        result = classify_v12_archetype(
            symbol="035420",
            company_name="NAVER",
            sector_context="platform",
            sector_profile=SectorProfile.AI_INFRA_PLATFORM,
            parsed_fields={
                "theme_business_link_mentioned": True,
                "ai_infra_capacity_or_gpu_mentioned": True,
                "nvidia_momentum_mentioned": True,
            },
            text=(
                "NAVER AI 데이터센터 엔비디아 GPU 클라우드 매출 반도체 SK하이닉스 "
                "장비 order 검색 광고 플랫폼"
            ),
        )

        self.assertEqual(result.large_sector_id, "L8_PLATFORM_CONTENT_SW_SECURITY")
        self.assertEqual(result.canonical_archetype_id, "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE")

    def test_feature_engineering_keeps_ai_platform_route_with_semiconductor_mentions(self):
        feature_input = replace(
            _rich_input(
                (
                    "NAVER AI 데이터센터 엔비디아 GPU 클라우드 매출 반도체 SK하이닉스 "
                    "장비 order 검색 광고 플랫폼"
                ),
                {
                    "theme_business_link_mentioned": True,
                    "ai_infra_capacity_or_gpu_mentioned": True,
                    "nvidia_momentum_mentioned": True,
                    "gpu_cloud_revenue_visible": True,
                },
            ),
            company_name="NAVER",
            sector_context="platform",
        )
        result = DeterministicFeatureEngineer().engineer(feature_input)

        self.assertEqual(result.source_fields["sector_profile"], "AI_INFRA_PLATFORM")
        self.assertEqual(result.source_fields["large_sector_id"], "L8_PLATFORM_CONTENT_SW_SECURITY")
        self.assertEqual(result.source_fields["canonical_archetype_id"], "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE")

    def test_cross_archetype_domain_profiles_feed_existing_canonical_routes(self):
        cases = (
            (
                "저PBR 은행 자사주 소각 주주환원 신용비용 안정",
                {
                    "roe": 12,
                    "pbr_e": 0.45,
                    "capital_return_execution": True,
                    "treasury_share_cancellation": True,
                    "credit_cost_quality": True,
                },
                "FINANCIAL_CAPITAL_RETURN",
                "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
            ),
            (
                "보험 CSM 증가 K-ICS 245% 준비금 안정 손해율 개선",
                {
                    "csm_growth_visible": True,
                    "k_ics_ratio": 245,
                    "reserve_quality_visible": True,
                    "loss_ratio_quality": True,
                },
                "INSURANCE_RESERVE",
                "C22_INSURANCE_RATE_CYCLE_RESERVE",
            ),
            (
                "FDA 승인 이후 상업화 매출 전환 로열티",
                {
                    "regulatory_approval_confirmed": True,
                    "approval_to_revenue_bridge": True,
                    "royalty_route": True,
                    "partner_economics_visible": True,
                },
                "BIO_COMMERCIALIZATION",
                "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
            ),
            (
                "SaaS ARR growth NRR renewal retention recurring margin",
                {
                    "arr_growth_pct": 35,
                    "nrr": 125,
                    "arr_growth_visible": True,
                    "retention_or_renewal": True,
                    "contract_renewal_visible": True,
                    "recurring_margin_leverage": True,
                },
                "SOFTWARE_SECURITY",
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            ),
        )
        for title, parsed_fields, expected_profile, expected_archetype in cases:
            with self.subTest(expected_profile=expected_profile):
                result = DeterministicFeatureEngineer().engineer(_rich_input(title, parsed_fields))
                score = result.score()

                self.assertEqual(result.source_fields["sector_profile"], expected_profile)
                self.assertEqual(result.source_fields["canonical_archetype_id"], expected_archetype)
                self.assertGreater(score.diagnostic_scores["domain_specific_evidence_score"], 0)
                self.assertGreater(score.diagnostic_scores["sector_visibility_score"], 0)

    def test_k_food_visibility_does_not_require_contract_quality(self):
        result = DeterministicFeatureEngineer().engineer(
            _rich_input(
                "삼양식품 불닭 수출 비중 확대 해외 채널 확장 ASP 상승",
                {
                    "export_ratio": 78,
                    "export_channel_expansion": True,
                    "overseas_channel_expansion": True,
                    "recurring_consumer_demand": True,
                    "high_margin_mix_improvement": True,
                    "pricing_power_mentioned": True,
                    "opm_expansion_pctp": 8,
                    "target_revision_pct": 40,
                },
            )
        )
        score = result.score()

        self.assertEqual(profile_name_from_diagnostic(score.diagnostic_scores["sector_profile_id"]), "K_FOOD_EXPORT")
        self.assertLess(score.diagnostic_scores["contract_quality"], 45)
        self.assertGreaterEqual(score.diagnostic_scores["structural_visibility_quality"], 45)

    def test_memory_hbm_evidence_improves_visibility_without_generic_contract(self):
        result = DeterministicFeatureEngineer().engineer(
            _rich_input(
                "삼성전자 메모리 HBM 수요 증가 메모리 가격 상승 공급조절",
                {
                    "hbm_demand_mentioned": True,
                    "memory_price_increase_mentioned": True,
                    "supply_discipline_mentioned": True,
                    "pricing_power_mentioned": True,
                    "target_revision_pct": 35,
                },
            )
        )
        score = result.score()

        self.assertEqual(profile_name_from_diagnostic(score.diagnostic_scores["sector_profile_id"]), "MEMORY_HBM")
        self.assertLess(score.diagnostic_scores["contract_quality"], 45)
        self.assertGreater(score.diagnostic_scores["sector_visibility_score"], 35)

    def test_generic_financial_inventory_field_does_not_create_consumer_retail_archetype(self):
        as_of_date = date(2026, 5, 1)
        result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="000660",
                company_name="SK하이닉스",
                sector_context="반도체",
                as_of_date=as_of_date,
                financial_actuals=(
                    FinancialActual(
                        symbol="000660",
                        fiscal_year=2025,
                        fiscal_quarter=4,
                        period_end=date(2025, 12, 31),
                        reported_at=datetime(2026, 2, 15, 8),
                        as_of_date=as_of_date,
                        source="test",
                        sales=1000,
                        operating_profit=100,
                        inventory=500,
                    ),
                ),
            )
        )

        self.assertNotEqual(result.source_fields["canonical_archetype_id"], "C19_BRAND_RETAIL_INVENTORY_MARGIN")

    def test_qualitative_evidence_is_bounded_and_cannot_create_green_alone(self):
        as_of_date = date(2024, 5, 16)
        feature_input = FeatureEngineeringInput(
            symbol="CASE",
            as_of_date=as_of_date,
            research_reports=(
                ResearchReport(
                    symbol="CASE",
                    publish_date=as_of_date,
                    broker="Test",
                    title="삼양식품 불닭 수출 비중 확대 해외 채널 확장 ASP 상승",
                    as_of_date=as_of_date,
                    parsed_fields={
                        "export_channel_expansion": True,
                        "overseas_channel_expansion": True,
                        "recurring_consumer_demand": True,
                        "pricing_power_mentioned": True,
                    },
                    raw_text="삼양식품 불닭 수출 비중 확대 해외 채널 확장 ASP 상승",
                ),
            ),
        )
        result = DeterministicFeatureEngineer().engineer(feature_input)
        score = result.score()
        stage = StageClassifier().classify(
            StageClassificationInput(score=score, red_team=RedTeamEngine().assess(result.red_team_signals))
        )

        self.assertGreater(score.diagnostic_scores["structural_visibility_quality"], 0)
        self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)

    def test_promotion_band_is_diagnostic_only(self):
        result = DeterministicFeatureEngineer().engineer(
            _rich_input(
                "일진전기 초고압 전력기기 수주잔고 리드타임 장기화",
                {
                    "contract_duration_months": 12,
                    "contract_amount_to_prior_sales": 0.12,
                    "order_backlog_to_sales": 1.2,
                    "lead_time_extended": True,
                    "pricing_power_mentioned": True,
                    "target_revision_pct": 35,
                },
            )
        )
        score = result.score()
        stage = StageClassifier().classify(
            StageClassificationInput(score=score, red_team=RedTeamEngine().assess(result.red_team_signals))
        )

        self.assertIn(promotion_band(score, stage.stage), {"Stage 1", "Stage 2", "Stage 2-High", "Stage 3-Watch"})
        self.assertNotEqual(stage.stage.value, promotion_band(score, stage.stage))


if __name__ == "__main__":
    unittest.main()
