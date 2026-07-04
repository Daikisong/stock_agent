import unittest
from dataclasses import replace
from datetime import date

from e2r.agentic.evidence_os import AnchorType, EvidenceAnchor, EvidenceDocument, SourceType
from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.production.claim_extraction import ExtractorProviderResult, RawAssertionRecord
from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
from e2r.research_brain.schemas import SourceTask, SourceTaskType
from e2r.research_brain.v4_schemas import SourceAcquisitionResultV4, SourceTaskExecutionStatusV4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from tests.research_brain_v4_test_helpers import c06_source_task, sample_v4_event


class _SingleDocumentRunner:
    def __init__(
        self,
        *,
        symbol: str,
        company_name: str,
        published_at: date,
        text: str,
        anchor_type=AnchorType.API_RECORD,
        include_structured_row: bool = True,
        structured_row: dict | None = None,
        canonical_url: str | None = None,
        source_name: str = "unit",
        source_class: str = "TrustedNews",
        source_type=SourceType.NEWS,
        source_lineage_id: str | None = None,
        provider_errors: tuple[str, ...] = (),
        web_fetched_row: bool = False,
        web_title: str = "unit fetched web document",
        query: str = "unit query",
    ) -> None:
        self.symbol = symbol
        self.company_name = company_name
        self.published_at = published_at
        self.text = text
        self.anchor_type = anchor_type
        self.include_structured_row = include_structured_row
        self.structured_row = structured_row
        self.canonical_url = canonical_url
        self.source_name = source_name
        self.source_class = source_class
        self.source_type = source_type
        self.source_lineage_id = source_lineage_id
        self.provider_errors = provider_errors
        self.web_fetched_row = web_fetched_row
        self.web_title = web_title
        self.query = query

    def acquire(self, *, event, task, as_of_date):
        document = EvidenceDocument.from_text(
            text=self.text,
            canonical_url=self.canonical_url or f"snapshot://unit/{self.symbol}",
            source_type=self.source_type,
            source_name=self.source_name,
            published_at=self.published_at,
            available_at=self.published_at,
            fetched_at=as_of_date,
            parser_version="unit",
            source_lineage_id=self.source_lineage_id,
            source_proxy_only=False,
        )
        anchor = EvidenceAnchor.structured(
            document=document,
            anchor_type=self.anchor_type,
            locator="unit:1",
            exact_text=self.text,
            normalized_value={
                "symbol": self.symbol,
                "company_name": self.company_name,
                **(
                    {"row": self.structured_row if self.structured_row is not None else {"EPS_ACTION_TYP_NM": "추정EPS 상향"}}
                    if self.include_structured_row
                    else {}
                ),
            },
            anchor_verified=True,
        )
        web_fetched_documents = ()
        if self.web_fetched_row:
            web_fetched_documents = (
                {
                    "schema_version": "e2r_research_brain_v4_web_fetched_document_v1",
                    "web_fetch_id": f"WEBFETCH-UNIT-{document.document_id}",
                    "web_result_id": f"WEBRESULT-UNIT-{document.document_id}",
                    "web_task_id": f"WEBTASK-UNIT-{task.task_id}",
                    "task_id": task.task_id,
                    "source_task_id": task.task_id,
                    "candidate_event_id": task.candidate_event_id,
                    "symbol": event.symbol,
                    "company_name": event.company_name,
                    "query": self.query,
                    "provider_name": self.source_name,
                    "as_of_date": as_of_date.isoformat(),
                    "status": "FETCHED_FULL_SOURCE",
                    "url": document.canonical_url,
                    "title": self.web_title,
                    "published_at": self.published_at.isoformat(),
                    "document_id": document.document_id,
                    "anchor_id": anchor.anchor_id,
                    "document_hash": document.content_hash,
                    "snippet_score_forbidden": True,
                    "source_origin": "research_brain_v4_attempt",
                    "brain_web_origin": "research_brain_v4_attempt",
                },
            )
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class=self.source_class,
            provider_name=self.source_name,
            status="PARSED",
            documents=(document,),
            anchors=(anchor,),
            document_text_by_id={document.document_id: self.text},
            fetched_document_ids=(document.document_id,),
            document_urls=(document.canonical_url,),
            document_hashes=(document.content_hash,),
            anchor_ids=(anchor.anchor_id,),
            provider_errors=self.provider_errors,
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
            stop_reason="unit",
            web_fetched_documents=web_fetched_documents,
        )


class ResearchBrainV4EvidenceExtractionFromRealDocumentTests(unittest.TestCase):
    def test_runtime_budget_callback_skips_remaining_source_tasks(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="005930", company_name="삼성전자")
        calls = iter((False, False, True))
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(
                c06_source_task("cash_or_revision_conversion"),
                c06_source_task("customer_preorder_or_allocation"),
            ),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="005930",
                company_name="삼성전자",
                published_at=date(2026, 6, 25),
                text="삼성전자 2026년 2분기 추정EPS 상향 및 HBM 고객 수요 확인",
                source_class="CompanyGuide",
                source_type=SourceType.API,
            ),
            runtime_budget_exhausted=lambda: next(calls),
        )

        self.assertEqual(len(bundle.executions), 2)
        self.assertNotEqual(bundle.executions[0].status, SourceTaskExecutionStatusV4.BUDGET_EXHAUSTED.value)
        self.assertEqual(bundle.executions[1].status, SourceTaskExecutionStatusV4.BUDGET_EXHAUSTED.value)
        self.assertEqual(bundle.executions[1].provider_name, "research_brain_v4_runtime_budget")
        self.assertIn("source_task_skipped_after_runtime_budget_exhausted", bundle.executions[1].provider_errors)
        self.assertEqual(bundle.extraction_audit["runtime_budget_skipped_source_task_count"], 1)

    def test_runtime_budget_callback_stops_document_extraction_inside_source_task(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        calls = iter((False, True))
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(c06_source_task("customer_preorder_or_allocation"),),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text="SK하이닉스 HBM 고객 배정 확인 문서",
                source_class="BrokerReportPublicPDF",
                source_type=SourceType.NEWS,
            ),
            runtime_budget_exhausted=lambda: next(calls),
        )

        self.assertEqual(len(bundle.executions), 1)
        execution = bundle.executions[0]
        self.assertEqual(execution.status, SourceTaskExecutionStatusV4.BUDGET_EXHAUSTED.value)
        self.assertTrue(execution.fetched_document_ids)
        self.assertEqual(execution.budget_used["fetches"], 1)
        self.assertIn(
            "source_task_document_extraction_stopped_after_runtime_budget_exhausted",
            execution.provider_errors,
        )
        self.assertEqual(execution.stop_reason, "source_task_extraction_stopped_after_runtime_budget_exhausted")
        self.assertEqual(bundle.extraction_audit["runtime_budget_stopped_document_extraction_count"], 1)
        self.assertEqual(bundle.extraction_audit["llm_claim_extractor_attempt_count"], 0)

    def test_structured_contract_amount_and_duration_become_source_backed_claims(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C05_EPC_MEGA_CONTRACT_MARGIN_GAP"]
        event = sample_v4_event(symbol="111111", company_name="한전변압기")
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(
                _c05_source_task(event=event, primitive="contract_amount_to_prior_sales"),
                _c05_source_task(event=event, primitive="contract_duration_months"),
            ),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="111111",
                company_name="한전변압기",
                published_at=date(2024, 5, 21),
                text="한전변압기 단일판매·공급계약체결 계약금액 1500억원 최근매출액 대비 15.0% 계약기간 2024-06-01 ~ 2027-05-31",
                structured_row={
                    "report_type": "단일판매·공급계약체결",
                    "contract_amount_to_prior_sales": "0.15",
                    "contract_duration_months": "36",
                },
            ),
        )

        accepted = {claim_id for execution in bundle.executions for claim_id in execution.accepted_claim_ids}
        self.assertTrue(accepted)
        self.assertTrue(all(execution.fetched_document_ids for execution in bundle.executions if execution.accepted_claim_ids))
        accepted_primitives = {
            mapping.primitive_id
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id in accepted and mapping.mapping_status.value == "ACCEPTED"
        }
        self.assertIn("contract_amount_to_prior_sales", accepted_primitives)
        self.assertIn("contract_duration_months", accepted_primitives)
        self.assertTrue(any(claim.effective_end == date(2027, 5, 31) for claim in bundle.ledger.claims.values()))

    def test_companyguide_consensus_numbers_create_revision_visibility_claim_not_cash_conversion(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        task = c06_source_task("cash_or_revision_conversion")
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 7, 1),
                text=(
                    "투자의견 컨센서스 [2026/07/01] "
                    "투자의견 4.0 목표주가 501,458 EPS 45,534 PER 6.9 추정기관수 24"
                ),
                structured_row={
                    "CONSENSUS_AS_OF_DATE": "2026/07/01",
                    "TARGET_PRC": 501458,
                    "EPS": 45534,
                    "CONSENSUS_PROVIDER_COUNT": 24,
                },
                canonical_url="https://wcomp.fnguide.com",
                source_name="CompanyGuide",
                source_class="CompanyGuide",
                source_type=SourceType.API,
            ),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertTrue(execution.accepted_claim_ids)
        self.assertEqual(execution.satisfaction_type, "REROUTED_ACCEPTED_CLAIM")
        self.assertEqual(execution.primitive_gap_unsatisfied_ids, ("cash_or_revision_conversion",))
        accepted_primitives = {
            mapping.primitive_id
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id in set(execution.accepted_claim_ids) and mapping.mapping_status.value == "ACCEPTED"
        }
        self.assertIn("medium_term_revision_visibility", accepted_primitives)
        self.assertNotIn("cash_or_revision_conversion", accepted_primitives)

    def test_repeated_companyguide_consensus_tasks_dedupe_to_one_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(c06_source_task("cash_or_revision_conversion"), c06_source_task("hbm_capacity_pre_sold")),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 7, 1),
                text=(
                    "투자의견 컨센서스 [2026/07/01] "
                    "투자의견 4.0 목표주가 501,458 EPS 45,534 PER 6.9 추정기관수 24"
                ),
                structured_row={
                    "CONSENSUS_AS_OF_DATE": "2026/07/01",
                    "TARGET_PRC": 501458,
                    "EPS": 45534,
                    "CONSENSUS_PROVIDER_COUNT": 24,
                },
                canonical_url="https://wcomp.fnguide.com",
                source_name="CompanyGuide",
                source_class="CompanyGuide",
                source_type=SourceType.API,
            ),
        )

        accepted_refs = [claim_id for execution in bundle.executions for claim_id in execution.accepted_claim_ids]
        self.assertEqual(len(accepted_refs), 2)
        self.assertEqual(len(set(accepted_refs)), 1)
        accepted_mapping_primitives = {
            mapping.primitive_id
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id in set(accepted_refs) and mapping.mapping_status.value == "ACCEPTED"
        }
        self.assertEqual(accepted_mapping_primitives, {"medium_term_revision_visibility"})

    def test_share_buyback_trust_title_alone_is_not_contract_quality_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C05_EPC_MEGA_CONTRACT_MARGIN_GAP"]
        event = sample_v4_event(symbol="473980", company_name="노머스")
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(_c05_source_task(event=event, primitive="contract_quality"),),
            contract=contract,
            as_of_date=date(2026, 6, 24),
            source_runner=_SingleDocumentRunner(
                symbol="473980",
                company_name="노머스",
                published_at=date(2026, 6, 24),
                text="노머스 주요사항보고서(자기주식취득신탁계약체결결정)",
                structured_row={"report_type": "주요사항보고서(자기주식취득신탁계약체결결정)"},
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")

    def test_news_document_cannot_satisfy_broker_report_source_task(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C05_EPC_MEGA_CONTRACT_MARGIN_GAP"]
        event = sample_v4_event(symbol="114450", company_name="그린생명과학")
        task = SourceTask(
            task_id="margin-broker-report",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
            primitive_gap="margin_bridge_visible",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("IndustryMedia",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="114450",
                company_name="그린생명과학",
                published_at=date(2026, 7, 1),
                text="그린생명과학은 공급계약 체결로 고부가 제품 매출과 수익성 개선을 기대한다고 밝혔다.",
                structured_row={"opm_expansion_pctp": "3.0"},
                canonical_url="https://www.digitaltoday.co.kr/news/articleView.html?idxno=665445",
                source_name="https://openapi.naver.com/v1/search/webkr.json",
                source_class="BrokerReportPublicPDF",
                source_type=SourceType.NEWS,
                provider_errors=("trusted_news_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        self.assertIn("source_class_document_type_mismatch:BrokerReportPublicPDF:NEWS", execution.not_eligible_reasons)
        self.assertIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            execution.not_eligible_reasons,
        )
        self.assertIn(
            "source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertEqual(bundle.extraction_audit["source_task_score_admissibility_rejected_count"], 1)

    def test_industry_media_full_news_from_general_search_is_rejected_until_trusted_news_connector_exists(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C05_EPC_MEGA_CONTRACT_MARGIN_GAP"]
        event = sample_v4_event(symbol="114450", company_name="그린생명과학")
        task = SourceTask(
            task_id="margin-industry-media-news",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
            primitive_gap="margin_bridge_visible",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF", "ReportPDF", "TrustedNews", "CompanyNewsroom"),
            fallback_source_classes=("IndustryMedia",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="114450",
                company_name="그린생명과학",
                published_at=date(2026, 7, 1),
                text="그린생명과학은 AI반도체 소재 공급계약으로 고부가 제품 매출과 수익성 개선 가능성을 설명했다.",
                canonical_url="https://www.digitaltoday.co.kr/news/articleView.html?idxno=665445",
                source_name="NaverFreeSearchProvider",
                source_class="IndustryMedia",
                source_type=SourceType.NEWS,
                provider_errors=("trusted_news_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
            ),
        )

        execution = bundle.executions[0]
        self.assertIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            execution.not_eligible_reasons,
        )
        self.assertNotIn(
            "source_task_provider_error_score_block:trusted_news_provider_not_configured",
            execution.not_eligible_reasons,
        )
        self.assertNotIn("source_class_document_type_mismatch:IndustryMedia:NEWS", execution.not_eligible_reasons)
        self.assertIn(
            "source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertIn(
            "source_lineage_unverified_original:IndustryMedia:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertEqual(len(bundle.web_rejected_documents), 1)
        self.assertIn(
            "source_lineage_unverified_original:IndustryMedia:general_web_search_provider",
            bundle.web_rejected_documents[0]["not_eligible_reasons"],
        )
        self.assertEqual(bundle.extraction_audit["source_task_score_admissibility_rejected_count"], 1)

    def test_merged_official_and_web_news_is_checked_as_requested_web_source_not_dart(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C05_EPC_MEGA_CONTRACT_MARGIN_GAP"]
        event = sample_v4_event(symbol="114450", company_name="그린생명과학")
        task = SourceTask(
            task_id="merged-official-web-news",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
            primitive_gap="contract_visibility",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("DART", "KIND", "IssuerOfficial", "IR"),
            fallback_source_classes=("CompanyNewsroom",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="114450",
                company_name="그린생명과학",
                published_at=date(2026, 7, 1),
                text="그린생명과학은 공급계약 체결과 납품 조건을 회사 관계자 설명으로 확인했다고 밝혔다.",
                canonical_url="https://www.digitaltoday.co.kr/news/articleView.html?idxno=665445",
                source_name="live_official_source_provider_registry+NaverFreeSearchProvider",
                source_class="DART",
                source_type=SourceType.NEWS,
                provider_errors=("trusted_news_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
            ),
        )

        execution = bundle.executions[0]
        self.assertIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            execution.not_eligible_reasons,
        )
        self.assertNotIn("source_class_document_type_mismatch:DART:NEWS", execution.not_eligible_reasons)
        self.assertIn(
            "source_provider_document_type_mismatch:CompanyNewsroom:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertIn(
            "source_lineage_unverified_original:CompanyNewsroom:general_web_search_provider",
            execution.not_eligible_reasons,
        )

    def test_web_discovered_kind_full_source_is_not_rejected_as_general_search_provider_error(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE"]
        event = sample_v4_event(symbol="003090", company_name="대웅")
        task = SourceTask(
            task_id="kind-discovered-through-web",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
            primitive_gap="mix_improvement",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("TrustedNews", "BrokerReportPublicPDF", "CompanyNewsroom"),
            fallback_source_classes=("IndustryMedia", "ReportPDF", "NaverSearch"),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="003090",
                company_name="대웅",
                published_at=date(2026, 6, 30),
                text="대웅은 신규시설투자 정정 공시에서 투자기간과 투자목적을 설명했다.",
                canonical_url="https://kind.krx.co.kr/common/disclsviewer.do?method=search&acptno=20260630001612",
                source_name="NaverFreeSearchProvider",
                source_class="KIND",
                source_type=SourceType.FILING,
                provider_errors=("trusted_news_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
            ),
        )

        execution = bundle.executions[0]
        self.assertNotIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            execution.not_eligible_reasons,
        )
        self.assertNotIn(
            "source_task_provider_error_score_block:trusted_news_provider_not_configured",
            execution.not_eligible_reasons,
        )
        self.assertNotIn("source_class_document_type_mismatch:KIND:FILING", execution.not_eligible_reasons)
        self.assertFalse(any(reason.startswith("source_lineage_unverified_original:") for reason in execution.not_eligible_reasons))
        self.assertEqual(bundle.extraction_audit["source_task_score_admissibility_rejected_count"], 0)

    def test_facility_completion_date_becomes_implementation_timeline_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C31_POLICY_SUBSIDY_LEGISLATION_EVENT"]
        event = sample_v4_event(symbol="003090", company_name="대웅")
        task = SourceTask(
            task_id="facility-timeline",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
            primitive_gap="implementation_timeline",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("DART",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-06-30", "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            llm_query_allowed=False,
            general_search_allowed=False,
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="003090",
                company_name="대웅",
                published_at=date(2026, 6, 30),
                text="대웅 신규시설투자 투자금액 1,200억원 완공예정일 2027.12.31",
                structured_row={
                    "report_type": "신규시설투자",
                    "facility_investment_amount": "120000000000",
                    "expected_completion_date": "2027-12-31",
                },
            ),
        )

        accepted = {claim_id for execution in bundle.executions for claim_id in execution.accepted_claim_ids}
        accepted_primitives = {
            mapping.primitive_id
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id in accepted and mapping.mapping_status.value == "ACCEPTED"
        }

        self.assertIn("implementation_timeline", accepted_primitives)

    def test_facility_correction_rejection_keeps_specific_mapping_reason(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE"]
        event = sample_v4_event(symbol="069620", company_name="대웅제약")
        task = SourceTask(
            task_id="facility-volume-growth",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
            primitive_gap="volume_growth_visible",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-06-30", "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            llm_query_allowed=True,
            general_search_allowed=False,
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="069620",
                company_name="대웅제약",
                published_at=date(2026, 6, 30),
                text="대웅제약은 신규시설투자 정정신고를 통해 정정사유가 종료일 연장이라고 밝혔다.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertIn("mapping_not_accepted:REJECTED", execution.not_eligible_reasons)
        self.assertIn(
            "primitive_mapping_rejected:facility_investment_correction_requires_followup_not_positive_capacity",
            execution.not_eligible_reasons,
        )

    def test_web_fetched_document_rejected_after_extraction_gets_document_level_rejection_row(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE"]
        event = sample_v4_event(symbol="069620", company_name="대웅제약")
        task = SourceTask(
            task_id="web-facility-volume-growth",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
            primitive_gap="volume_growth_visible",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=("NaverSearch",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-06-30", "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            llm_query_allowed=True,
            general_search_allowed=False,
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="069620",
                company_name="대웅제약",
                published_at=date(2026, 6, 30),
                text="대웅제약은 신규시설투자 정정신고를 통해 정정사유가 종료일 연장이라고 밝혔다.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://news.example.test/daewoong-facility-correction",
                source_name="https://openapi.naver.com/v1/search/news.json",
                web_fetched_row=True,
                query="대웅제약 신규시설투자 정정 종료일 연장",
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(len(bundle.web_fetched_documents), 1)
        self.assertEqual(len(bundle.web_rejected_documents), 1)
        rejected = bundle.web_rejected_documents[0]
        self.assertEqual(rejected["rejection_phase"], "post_extraction_evidence_os")
        self.assertEqual(rejected["rejection_reason"], "post_extraction_no_score_eligible_claim")
        self.assertEqual(rejected["document_id"], execution.fetched_document_ids[0])
        self.assertEqual(rejected["source_task_id"], task.task_id)
        self.assertEqual(rejected["primitive_gap"], "volume_growth_visible")
        self.assertTrue(rejected["snippet_score_forbidden"])
        self.assertEqual(rejected["accepted_claim_ids"], [])
        self.assertEqual(set(rejected["raw_assertion_ids"]), set(execution.raw_assertion_ids))
        self.assertEqual(set(rejected["rejected_claim_ids"]), set(execution.rejected_claim_ids))
        self.assertIn(
            "primitive_mapping_rejected:facility_investment_correction_requires_followup_not_positive_capacity",
            rejected["not_eligible_reasons"],
        )
        self.assertIn(
            "source_lineage_unverified_original:TrustedNews:general_web_search_provider",
            rejected["not_eligible_reasons"],
        )
        self.assertEqual(bundle.extraction_audit["post_extraction_web_rejected_document_count"], 1)
        self.assertEqual(len(bundle.raw_assertion_rejections), len(execution.rejected_claim_ids))
        raw_rejection = bundle.raw_assertion_rejections[0]
        self.assertIn(raw_rejection["raw_assertion_id"], execution.raw_assertion_ids)
        self.assertIn(raw_rejection["adjudicated_claim_id"], execution.rejected_claim_ids)
        self.assertEqual(raw_rejection["rejection_reason"], "primitive_mapping_rejected")
        self.assertEqual(raw_rejection["mapped_primitive_id"], "volume_growth_visible")
        self.assertEqual(raw_rejection["mapping_status"], "REJECTED")
        self.assertEqual(raw_rejection["target_scope_status"], "DIRECT")
        self.assertEqual(raw_rejection["temporal_status"], "CURRENT")

    def test_real_document_anchor_produces_accepted_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot"),
        )
        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertTrue(execution.fetched_document_ids)
        self.assertTrue(execution.evidence_anchor_ids)
        self.assertTrue(execution.accepted_claim_ids)
        self.assertTrue(bundle.raw_assertions)
        for claim_id in execution.accepted_claim_ids:
            self.assertIn(claim_id, bundle.ledger.claims)

    def test_wrong_subject_document_is_rejected_not_scored(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(symbol="005930", company_name="삼성전자"),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="999999",
                company_name="월덱스",
                published_at=date(2026, 6, 20),
                text="월덱스는 삼성전자를 고객으로 언급했지만 HBM 고객 수요와 추정EPS 상향은 월덱스 문서 주체의 내용이다.",
            ),
        )
        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertIn("target_scope_not_allowed:UNRELATED", execution.not_eligible_reasons)
        self.assertGreater(bundle.extraction_audit["wrong_subject_rejected_count"], 0)

    def test_text_span_keyword_mentions_are_mention_only_not_score_claims(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="005930",
                company_name="삼성전자",
                published_at=date(2026, 6, 20),
                text="삼성전자는 국내 반도체 대표 기업으로 기사 본문에서 언급됐다.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
            ),
        )
        execution = bundle.executions[0]
        self.assertFalse(execution.raw_assertion_ids)
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        self.assertGreater(bundle.extraction_audit["mention_only_count"], 0)

    def test_unstructured_text_span_runs_contract_blind_extractor_and_accepts_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event()
        task = c06_source_task("customer_preorder_or_allocation")
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="005930",
                company_name="삼성전자",
                published_at=date(2026, 6, 20),
                text="삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
            ),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertTrue(execution.raw_assertion_ids)
        self.assertTrue(execution.accepted_claim_ids)
        self.assertEqual(len(bundle.claim_extractor_runs), 1)
        self.assertEqual(bundle.claim_extractor_runs[0]["provider_mode"], "rule_fallback")
        self.assertEqual(bundle.extraction_audit["llm_claim_extractor_attempt_count"], 1)
        self.assertEqual(bundle.extraction_audit["unstructured_text_to_raw_assertion_count"], 1)
        accepted_primitives = {
            mapping.primitive_id
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id in set(execution.accepted_claim_ids) and mapping.mapping_status.value == "ACCEPTED"
        }
        self.assertIn("customer_preorder_or_allocation", accepted_primitives)

    def test_web_title_symbol_alias_maps_english_subject_without_unlocking_general_search_score(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "We maintain our Buy rating on SK Hynix and raise our target price by 12%."
        task = SourceTask(
            task_id="english-broker-report",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="medium_term_revision_visibility",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )
        extractor = _StaticRawAssertionExtractor(
            RawAssertionRecord(
                raw_assertion_id="RAW-SK-HYNIX-REVISION",
                document_id="",
                anchor_id="",
                subject="SK Hynix",
                predicate="revision_claim",
                object_text=quote,
                polarity_proposal="POSITIVE",
                modality="STATED",
                event_date="2026-06-30",
                exact_quote=quote,
                related_entities=("SK Hynix",),
            )
        )

        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=f"{quote} The report discusses HBM demand.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://securities.example.com/research/sk-hynix-000660",
                source_name="NaverFreeSearchProvider",
                source_class="BrokerReportPublicPDF",
                source_type=SourceType.RESEARCH_REPORT,
                provider_errors=("trusted_report_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
                web_title="SK Hynix 000660 - Research Report | Broker",
            ),
            claim_extractor=extractor,
        )

        self.assertIn("SK Hynix", extractor.last_request.target_aliases)
        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        claim = next(iter(bundle.ledger.claims.values()))
        self.assertEqual(claim.target_scope_status.value, "DIRECT")
        self.assertNotIn("target_scope_not_allowed:UNRELATED", execution.not_eligible_reasons)
        self.assertIn(
            "source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )

    def test_verified_broker_report_original_can_score_direct_revision_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "We maintain our Buy rating on SK Hynix and raise our target price by 12%."
        task = SourceTask(
            task_id="recognized-broker-report",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="medium_term_revision_visibility",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=f"{quote} The report discusses HBM demand.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://stock.pstatic.net/stock-research/company/17/20250630_company_000660.pdf",
                source_name="NaverFreeSearchProvider",
                source_class="BrokerReportPublicPDF",
                source_type=SourceType.RESEARCH_REPORT,
                source_lineage_id=(
                    "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                    "verified_report_original:broker_report_domain:stock.pstatic.net"
                ),
                provider_errors=("trusted_report_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
                web_title="SK Hynix 000660 - Research Report | Broker",
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-SK-HYNIX-REVISION-RECOGNIZED-REPORT",
                    document_id="",
                    anchor_id="",
                    subject="SK Hynix",
                    predicate="revision_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK Hynix",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertTrue(execution.accepted_claim_ids)
        self.assertNotIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            execution.not_eligible_reasons,
        )
        self.assertNotIn(
            "source_provider_document_type_mismatch:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertNotIn(
            "source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )

    def test_broker_domain_non_report_pdf_with_forged_lineage_marker_does_not_score(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "We maintain our Buy rating on SK Hynix and raise our target price by 12%."
        task = SourceTask(
            task_id="forged-broker-report-marker",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="medium_term_revision_visibility",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=f"{quote} The report discusses HBM demand.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://www.samsungpop.com/customer/event_terms.pdf",
                source_name="NaverFreeSearchProvider",
                source_class="BrokerReportPublicPDF",
                source_type=SourceType.RESEARCH_REPORT,
                source_lineage_id=(
                    "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                    "verified_report_original:broker_report_domain:samsungpop.com"
                ),
                provider_errors=("trusted_report_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
                web_title="SK Hynix 000660 event terms PDF | SamsungPop",
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-SK-HYNIX-REVISION-FORGED-REPORT-MARKER",
                    document_id="",
                    anchor_id="",
                    subject="SK Hynix",
                    predicate="revision_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK Hynix",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        self.assertIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            execution.not_eligible_reasons,
        )
        self.assertIn(
            "source_provider_document_type_mismatch:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertIn(
            "source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )

    def test_same_host_query_spoofed_report_route_with_forged_lineage_marker_does_not_score(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "We maintain our Buy rating on SK Hynix and raise our target price by 12%."
        spoof_urls = (
            (
                "https://www.samsungpop.com/support/download?"
                "saveKey=research.pdf&fileName=fake.pdf&contentType=application/pdf"
            ),
            "https://www.samsungpop.com/common.do?next=research.pdf&contentType=application/pdf",
            "https://www.samsungpop.com/media/pdfs/fake.pdf",
        )
        for spoof_url in spoof_urls:
            with self.subTest(url=spoof_url):
                task = SourceTask(
                    task_id="same-host-query-spoofed-broker-report",
                    candidate_event_id=event.candidate_event_id,
                    symbol=event.symbol,
                    company_name=event.company_name,
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    primitive_gap="medium_term_revision_visibility",
                    task_type=SourceTaskType.POSITIVE_VERIFY.value,
                    preferred_source_classes=("BrokerReportPublicPDF",),
                    fallback_source_classes=("ReportPDF",),
                    forbidden_source_classes=("unbounded_general_search",),
                    date_window={"end": "2026-07-01", "lookback_days": 90},
                    max_queries=1,
                    max_candidates=5,
                    max_fetches=1,
                    stop_condition={"accepted_claim_count": 1},
                    general_search_allowed=False,
                )
                bundle = execute_source_tasks_with_evidence_os_v4(
                    event=event,
                    tasks=(task,),
                    contract=contract,
                    as_of_date=date(2026, 7, 1),
                    source_runner=_SingleDocumentRunner(
                        symbol="000660",
                        company_name="SK하이닉스",
                        published_at=date(2026, 6, 30),
                        text=f"{quote} The report discusses HBM demand.",
                        anchor_type=AnchorType.TEXT_SPAN,
                        include_structured_row=False,
                        canonical_url=spoof_url,
                        source_name="NaverFreeSearchProvider",
                        source_class="BrokerReportPublicPDF",
                        source_type=SourceType.RESEARCH_REPORT,
                        source_lineage_id=(
                            "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                            "verified_report_original:broker_report_domain:samsungpop.com"
                        ),
                        provider_errors=("trusted_report_provider_not_configured; general search is not a score source",),
                        web_fetched_row=True,
                        web_title="SK Hynix 000660 fake research PDF | SamsungPop",
                    ),
                    claim_extractor=_StaticRawAssertionExtractor(
                        RawAssertionRecord(
                            raw_assertion_id="RAW-SK-HYNIX-REVISION-QUERY-SPOOFED-REPORT",
                            document_id="",
                            anchor_id="",
                            subject="SK Hynix",
                            predicate="revision_claim",
                            object_text=quote,
                            polarity_proposal="POSITIVE",
                            modality="STATED",
                            event_date="2026-06-30",
                            exact_quote=quote,
                            related_entities=("SK Hynix",),
                        )
                    ),
                )

                execution = bundle.executions[0]
                self.assertFalse(execution.accepted_claim_ids)
                self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
                self.assertIn(
                    "source_task_provider_error_score_block:general_search_not_score_source",
                    execution.not_eligible_reasons,
                )
                self.assertIn(
                    "source_provider_document_type_mismatch:BrokerReportPublicPDF:general_web_search_provider",
                    execution.not_eligible_reasons,
                )
                self.assertIn(
                    "source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider",
                    execution.not_eligible_reasons,
                )

    def test_spoofed_broker_report_host_with_forged_lineage_marker_does_not_score(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "We maintain our Buy rating on SK Hynix and raise our target price by 12%."
        task = SourceTask(
            task_id="spoofed-broker-report-host",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="medium_term_revision_visibility",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=f"{quote} The report discusses HBM demand.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://evil.example/samsungpop.com/research/fake-report.pdf",
                source_name="NaverFreeSearchProvider",
                source_class="BrokerReportPublicPDF",
                source_type=SourceType.RESEARCH_REPORT,
                source_lineage_id=(
                    "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                    "verified_report_original:broker_report_domain:evil.example"
                ),
                provider_errors=("trusted_report_provider_not_configured; general search is not a score source",),
                web_fetched_row=True,
                web_title="SK Hynix 000660 fake research PDF",
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-SK-HYNIX-REVISION-SPOOFED-REPORT-HOST",
                    document_id="",
                    anchor_id="",
                    subject="SK Hynix",
                    predicate="revision_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK Hynix",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        self.assertIn(
            "source_task_provider_error_score_block:general_search_not_score_source",
            execution.not_eligible_reasons,
        )
        self.assertIn(
            "source_provider_document_type_mismatch:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertIn(
            "source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider",
            execution.not_eligible_reasons,
        )

    def test_stored_broker_report_snapshot_with_spoofed_url_does_not_score(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "We maintain our Buy rating on SK Hynix and raise our target price by 12%."
        task = SourceTask(
            task_id="stored-spoofed-broker-report",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="medium_term_revision_visibility",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": "2026-07-01", "lookback_days": 90},
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            general_search_allowed=False,
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=f"{quote} The report discusses HBM demand.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://evil.example/samsungpop.com/research/fake-report.pdf",
                source_name="stored_real_source_snapshot_provider",
                source_class="BrokerReportPublicPDF",
                source_type=SourceType.RESEARCH_REPORT,
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-SK-HYNIX-REVISION-STORED-SPOOFED-REPORT",
                    document_id="",
                    anchor_id="",
                    subject="SK Hynix",
                    predicate="revision_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK Hynix",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        self.assertIn(
            "source_lineage_unverified_original:BrokerReportPublicPDF:stored_report_snapshot_provider",
            execution.not_eligible_reasons,
        )

    def test_verified_company_newsroom_original_avoids_general_web_lineage_block_but_profile_claim_still_not_scored(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "SK하이닉스는 GTC 2026에서 AI 메모리 제품 포트폴리오를 공개했다."
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            preferred_source_classes=("CompanyNewsroom",),
            fallback_source_classes=("NaverSearch",),
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=quote,
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://news.skhynix.com/gtc-2026-exhibition-booth/",
                source_name="NaverFreeSearchProvider",
                source_class="CompanyNewsroom",
                source_type=SourceType.NEWS,
                source_lineage_id=(
                    "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                    "verified_issuer_original:issuer_official_domain:skhynix.com:news.skhynix.com"
                ),
                provider_errors=("general search is not a score source",),
                web_fetched_row=True,
                web_title="SK하이닉스, GTC 2026서 엔비디아와 파트너십 재확인 - SK hynix Newsroom",
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-NEWSROOM-PROFILE",
                    document_id="",
                    anchor_id="",
                    subject="SK하이닉스",
                    predicate="product_profile_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK하이닉스",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        self.assertNotIn(
            "source_provider_document_type_mismatch:CompanyNewsroom:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        self.assertNotIn(
            "source_lineage_unverified_original:CompanyNewsroom:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        rejected_primitives = {
            proposal.primitive_id
            for proposal in bundle.ledger.mappings.values()
            if proposal.mapping_status.value == "REJECTED"
        }
        self.assertIn("customer_preorder_or_allocation", rejected_primitives)

    def test_verified_company_newsroom_original_can_score_direct_customer_allocation_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "SK하이닉스는 2026년 HBM 고객 물량 배정이 확정됐다고 밝혔다."
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            preferred_source_classes=("CompanyNewsroom",),
            fallback_source_classes=("NaverSearch",),
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=quote,
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://news.skhynix.com/customer-allocation/",
                source_name="NaverFreeSearchProvider",
                source_class="CompanyNewsroom",
                source_type=SourceType.NEWS,
                source_lineage_id=(
                    "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                    "verified_issuer_original:issuer_official_domain:skhynix.com:news.skhynix.com"
                ),
                provider_errors=("general search is not a score source",),
                web_fetched_row=True,
                web_title="SK하이닉스 HBM 고객 물량 배정 확정 - SK hynix Newsroom",
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-NEWSROOM-CUSTOMER-ALLOCATION",
                    document_id="",
                    anchor_id="",
                    subject="SK하이닉스",
                    predicate="customer_allocation_or_qualification_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK하이닉스",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertTrue(execution.accepted_claim_ids)
        self.assertNotIn(
            "source_provider_document_type_mismatch:CompanyNewsroom:general_web_search_provider",
            execution.not_eligible_reasons,
        )
        accepted_primitives = {
            mapping.primitive_id
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id in set(execution.accepted_claim_ids) and mapping.mapping_status.value == "ACCEPTED"
        }
        self.assertIn("customer_preorder_or_allocation", accepted_primitives)

    def test_verified_company_newsroom_registry_lineage_can_score_alternate_official_domain(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "SK하이닉스는 2026년 HBM 고객 물량 배정이 확정됐다고 밝혔다."
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            preferred_source_classes=("CompanyNewsroom",),
            fallback_source_classes=("NaverSearch",),
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=quote,
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://news.skhynix.co.kr/customer-allocation/",
                source_name="NaverFreeSearchProvider",
                source_class="CompanyNewsroom",
                source_type=SourceType.NEWS,
                source_lineage_id=(
                    "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                    "verified_issuer_original:issuer_official_domain:news.skhynix.co.kr:news.skhynix.co.kr"
                ),
                provider_errors=("general search is not a score source",),
                web_fetched_row=True,
                web_title="SK하이닉스 HBM 고객 물량 배정 확정 - SK hynix Newsroom",
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-NEWSROOM-CUSTOMER-ALLOCATION-REGISTRY",
                    document_id="",
                    anchor_id="",
                    subject="SK하이닉스",
                    predicate="customer_allocation_or_qualification_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK하이닉스",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertTrue(execution.accepted_claim_ids)
        self.assertNotIn(
            "source_lineage_unverified_original:CompanyNewsroom:general_web_search_provider",
            execution.not_eligible_reasons,
        )

    def test_verified_company_newsroom_lineage_requires_homepage_subdomain_match(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        quote = "SK하이닉스는 2026년 HBM 고객 물량 배정이 확정됐다고 밝혔다."
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            preferred_source_classes=("CompanyNewsroom",),
            fallback_source_classes=("NaverSearch",),
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 7, 1),
            source_runner=_SingleDocumentRunner(
                symbol="000660",
                company_name="SK하이닉스",
                published_at=date(2026, 6, 30),
                text=quote,
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
                canonical_url="https://news.skhynix.co.kr/customer-allocation/",
                source_name="NaverFreeSearchProvider",
                source_class="CompanyNewsroom",
                source_type=SourceType.NEWS,
                source_lineage_id=(
                    "NaverFreeSearchProvider:WEBRESULT-UNIT:"
                    "verified_issuer_original:issuer_official_domain:skhynix.com:news.skhynix.co.kr"
                ),
                provider_errors=("general search is not a score source",),
                web_fetched_row=True,
                web_title="SK하이닉스 HBM 고객 물량 배정 확정 - SK hynix Newsroom",
            ),
            claim_extractor=_StaticRawAssertionExtractor(
                RawAssertionRecord(
                    raw_assertion_id="RAW-NEWSROOM-CUSTOMER-ALLOCATION-SPOOF",
                    document_id="",
                    anchor_id="",
                    subject="SK하이닉스",
                    predicate="customer_allocation_or_qualification_claim",
                    object_text=quote,
                    polarity_proposal="POSITIVE",
                    modality="STATED",
                    event_date="2026-06-30",
                    exact_quote=quote,
                    related_entities=("SK하이닉스",),
                )
            ),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "NO_EVIDENCE_FOUND")
        self.assertFalse(execution.accepted_claim_ids)
        self.assertIn(
            "source_lineage_unverified_original:CompanyNewsroom:general_web_search_provider",
            execution.not_eligible_reasons,
        )

    def test_valid_claim_for_other_contract_primitive_is_preserved_as_rerouted(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = sample_v4_event()
        task = c06_source_task("medium_term_revision_visibility")
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(task,),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="005930",
                company_name="삼성전자",
                published_at=date(2026, 6, 20),
                text="삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
            ),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertFalse(execution.satisfies_source_task)
        self.assertEqual(execution.satisfaction_type, "REROUTED_ACCEPTED_CLAIM")
        self.assertTrue(execution.rerouted_accepted_claim_ids)
        self.assertFalse(execution.direct_accepted_claim_ids)
        self.assertEqual(execution.primitive_gap_unsatisfied_ids, ("medium_term_revision_visibility",))
        accepted_primitives = {
            mapping.primitive_id
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id in set(execution.accepted_claim_ids) and mapping.mapping_status.value == "ACCEPTED"
        }
        self.assertIn("customer_preorder_or_allocation", accepted_primitives)

    def test_unstructured_claim_extractor_provider_error_is_provider_failed_not_no_evidence(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task("customer_preorder_or_allocation"),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="005930",
                company_name="삼성전자",
                published_at=date(2026, 6, 20),
                text="삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.",
                anchor_type=AnchorType.TEXT_SPAN,
                include_structured_row=False,
            ),
            claim_extractor=_ProviderErrorExtractor(),
        )

        execution = bundle.executions[0]
        self.assertEqual(execution.status, "PROVIDER_FAILED")
        self.assertFalse(execution.accepted_claim_ids)
        self.assertIn("claim_extractor_provider_error:RuntimeError: unit provider failed", execution.provider_errors)
        self.assertEqual(bundle.claim_extractor_runs[0]["status"], "PROVIDER_FAILED")

    def test_old_positive_document_without_current_confirmation_is_historical_not_scored(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="005930",
                company_name="삼성전자",
                published_at=date(2020, 1, 10),
                text="삼성전자는 HBM 고객 수요와 추정EPS 상향 가능성을 당시 언급했다.",
            ),
        )
        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertIn("temporal_not_allowed:HISTORICAL", execution.not_eligible_reasons)


def _c05_source_task(*, event, primitive: str) -> SourceTask:
    return SourceTask(
        task_id=f"RSTASKV4-C05-TEST-{primitive}",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
        primitive_gap=primitive,
        task_type=SourceTaskType.POSITIVE_VERIFY.value,
        preferred_source_classes=("DART",),
        fallback_source_classes=(),
        forbidden_source_classes=("unbounded_general_search",),
        date_window={"end": event.event_date, "lookback_days": 540},
        max_queries=1,
        max_candidates=10,
        max_fetches=3,
        stop_condition={"accepted_claim_count": 1},
        general_search_allowed=False,
        reason_from_memory="v4 test structured contract primitive",
    )


class _ProviderErrorExtractor:
    def extract_with_metadata(self, request):
        return ExtractorProviderResult(
            provider_name="unit_error_extractor",
            provider_mode="llm",
            model="unit",
            raw_assertions=(),
            provider_error="RuntimeError: unit provider failed",
        )


class _StaticRawAssertionExtractor:
    def __init__(self, *records: RawAssertionRecord) -> None:
        self.records = records
        self.last_request = None

    def extract_with_metadata(self, request):
        self.last_request = request
        records = []
        for record in self.records:
            records.append(
                RawAssertionRecord(
                    raw_assertion_id=record.raw_assertion_id,
                    document_id=request.document_id,
                    anchor_id=request.anchor_id,
                    subject=record.subject,
                    predicate=record.predicate,
                    object_text=record.object_text,
                    polarity_proposal=record.polarity_proposal,
                    modality=record.modality,
                    event_date=record.event_date,
                    exact_quote=record.exact_quote,
                    related_entities=record.related_entities,
                    uncertainty_reason=record.uncertainty_reason,
                )
            )
        return ExtractorProviderResult(
            provider_name="unit_static_extractor",
            provider_mode="llm",
            model="unit",
            raw_assertions=tuple(records),
        )


if __name__ == "__main__":
    unittest.main()
