# Census v4 0701 SourceQuality v20 Stage Truth / SourceClass Patch / Next Agent Attack Packet

작성일: 2026-07-02

이 문서는 다음 에이전트가 v20 시점 상태를 빡세게 검증할 수 있게 남기는 중간 감사 패킷이다.

주의:

```text
이 문서는 v20 시점의 중간 감사 패킷이다.
교차검증 후 NEWS guard를 더 보수적으로 조인 최신 문서는 아래다.

docs/0701/census_v4_0701_sourcequality_v21_guardtight_stage_truth_and_next_patch_packet_2026-07-02.md

최신 판단은 v21 문서와 output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21을 우선한다.
```

## 1. 직접 답

질문:

```text
뭔가 잘못되고있는거맞지?
stage가 있는애들이 있긴해?
```

답:

```text
맞다. 아직 운영 Stage로 보면 잘못된 상태다.

Stage row는 있다.
하지만 v20 기준 Stage row 3391개 전부가 CENSUS_EVENT_BOARD다.

운영 FULL_THESIS Stage는 0개다.
FULL_E2R_100 verified score row도 0개다.
web/LLM accepted score claim도 0개다.
```

쉬운 예:

```text
전교생 출석부에는 상태 메모가 붙었다.
  - 3306명: 새 촉매 없음
  - 54명: Stage1 event watch
  - 30명: Stage2-Watch
  - 1명: Red/Risk review

하지만 정식 성적표는 아직 아무도 발급되지 않았다.
  - FULL_THESIS_NOT_RUN = 3391
  - verified score = 0
```

따라서 지금 출력의 `Stage1`, `Stage2-Watch`, `Red`를 운영 추천/운영 thesis Stage처럼 읽으면 안 된다. 이것들은 현재까지는 Census 상태판 Stage다.

## 2. v20 기준 핵심 집계

산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v20
```

Stage 요약:

```text
census_stage_status rows = 3391
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

base_stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use_distribution:
  NOT_FULL_E2R_SCORE = 3391

verified_score_present_count = 0
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
event_board_non_stage0_count = 85
```

Brain/Web readiness:

```text
verdict = BLOCKED

blockers:
  web/LLM accepted claim count is zero
  Brain/Web StageCourt traces are not promoted into census_stage_status
  brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
  planner runs 21/30
  web search tasks 2/20
  web/news search calls 2/20
  fetched documents 1/10
  claim extractor attempts 1/10
  web/LLM accepted claims 0/3
```

Full thesis:

```text
full_thesis_production_audit.verdict = PENDING_FULL_THESIS_PRODUCTION
blocker = production_full_thesis_runner_no_eligible_rows
```

## 3. v17 -> v20 변화

```text
v17:
  BRAIN_WEB_PARTIAL = 0
  FULL_THESIS = 0
  web_search_tasks = 0
  web_fetched_documents = 0
  claim_extractor_runs = 0
  web_or_llm_accepted_claim_count = 0

v18:
  web_search_tasks = 3
  web_search_results = 24
  web_fetched_documents = 1
  claim_extractor_runs = 1
  web_or_llm_accepted_claim_count = 0
  병목 = 뉴스 문서가 BrokerReportPublicPDF source_class로 포장되어 source guard에서 차단

v19:
  web_search_tasks = 13
  web_search_results = 123
  web_fetched_documents = 5
  claim_extractor_runs = 5
  web_or_llm_accepted_claim_count = 0
  병목 = 네이버로 발견한 KIND/기타 문서가 TrustedNews/BrokerReport source_class로 남아 source guard에서 차단

v20:
  web_search_tasks = 2
  web_search_results = 20
  web_fetched_documents = 1
  claim_extractor_runs = 1
  web_or_llm_accepted_claim_count = 0
  source-class guard 병목은 제거됨
  남은 병목 = primitive mapper가 KIND header/정정요구 안내문을 margin bridge로 인정하지 않음
```

v19와 v20의 task 수가 줄어든 것은 LLM planner 출력이 완전히 동일하지 않기 때문이다. 따라서 v19/v20은 정확한 성능 비교가 아니라 병목 위치 비교로만 봐야 한다.

## 4. 이번 패치로 실제로 고친 것

수정 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

고친 문제:

```text
검색 수단과 실제 문서 source class가 섞여 있었다.
```

나쁜 흐름:

```text
SourceTask preferred_source_classes = [BrokerReportPublicPDF, ReportPDF, TrustedNews, CompanyNewsroom]
fallback_source_classes = [IndustryMedia]

Naver가 실제 뉴스/KIND 원문을 발견
  -> result.source_class가 첫 preferred인 BrokerReportPublicPDF 또는 TrustedNews로 남음
  -> NEWS/FILING 문서가 PDF/TrustedNews 문서가 아니라고 차단
  -> general_search_not_score_source / trusted_news_provider_not_configured가 full source까지 자동 차단
```

좋은 흐름:

```text
Naver는 발견 수단이다.
실제 점수 근거 source class는 fetched document를 보고 다시 정한다.

kind.krx.co.kr URL이면 KIND
dart.fss.or.kr URL이면 DART
뉴스 full text이고 IndustryMedia fallback이 있으면 IndustryMedia
뉴스 full text이고 CompanyNewsroom이 허용되면 CompanyNewsroom
```

쉬운 예:

```text
구글로 DART 공시를 찾았다.
  -> 점수 근거는 구글이 아니라 DART 공시다.

네이버로 KIND 공시를 찾았다.
  -> 점수 근거는 네이버 검색결과가 아니라 KIND 원문이다.

네이버로 뉴스 full text를 찾았다.
  -> 점수 근거는 네이버 snippet이 아니라 fetched news article이다.
```

v20 확인:

```text
source_task_executions 중 Naver 경유 row:
  symbol = 114450
  source_class = KIND
  provider_name = live_official_source_provider_registry+NaverFreeSearchProvider
  document_url = https://kind.krx.co.kr/common/disclsviewer.do?method=search&acptno=20260630001605

not_eligible_reasons:
  mapping_not_accepted:REJECTED
  primitive_mapping_rejected:no_allowed_primitive_for_predicate

사라진 source-related rejection:
  source_task_provider_error_score_block:general_search_not_score_source
  source_task_provider_error_score_block:trusted_news_provider_not_configured
  source_class_document_type_mismatch:...
  source_provider_document_type_mismatch:...
```

즉 source routing/source admissibility 문제 하나는 고쳤다. 하지만 accepted web/LLM claim은 아직 0개다.

## 5. 왜 아직 Stage가 운영용이 아닌가

v20의 web fetched document:

```text
url = https://kind.krx.co.kr/common/disclsviewer.do?method=search&acptno=20260630001605
title = [그린생명과학] [정정]단일판매ㆍ공급계약체결
source_path = data/cache/research_brain_v4_web_fetch/2026-07-01/4c0ece09f273bbff5cfba9f0fd9f666c9c8fe89e.txt
```

실제 fetch 본문 핵심:

```text
대한민국 대표 기업공시채널 KIND
[그린생명과학] [정정]단일판매ㆍ공급계약체결
본 문서는 최종문서가 아니므로, 최종 정정문서를 반드시 확인하시기 바랍니다.
본 공지사항은 공시내용 기재 불충분 등의 사유로 한국거래소 정정요구를 받은 사항입니다.
```

이 문서는 상세 계약 본문이 아니다. 계약금액, 납품 기간, 마진 bridge, 현금흐름 bridge가 있는 최종 상세 문서가 아니다.

따라서 LLM raw assertion도 다음처럼만 나왔다.

```text
official_document_fact
contract_or_order_claim
정정문서 확인 필요
공시내용 기재 불충분 / 정정요구
```

이걸 `margin_bridge_visible`로 점수화하지 않은 것은 맞다. 여기서 점수를 주면 다시 예전처럼 "공시 제목을 보고 마진 bridge까지 줬다"는 오류가 된다.

## 6. 현재 114450 그린생명과학 사례의 실제 상태

OpenDART 공식 원문에서는 claim이 꽤 많이 accepted됐다.

```text
symbol = 114450
accepted_claims = 19
source_provider = OpenDART

accepted primitives:
  contract_quality
  contract_amount_to_prior_sales
  contract_duration_months
  delivery_schedule
```

대표 accepted quote에는 다음이 들어 있다.

```text
계약금액 총액 = 10,238,670,000원
최근 매출액 = 24,860,636,227원
매출액 대비 = 41.18%
계약상대방 = UPL Limited
판매공급지역 = 브라질
```

하지만 이것은 아직 C05 전체 thesis가 아니다.

```text
확인된 것:
  계약 규모
  계약 기간/일정 계열
  상대방/지역 일부

아직 확인되지 않은 것:
  margin_bridge_visible
  cash_or_revision_conversion
  repeat evidence family
  multi-source confirmation
  FULL_THESIS score interval
```

쉬운 예:

```text
"큰 계약을 했다"는 영수증은 있다.
하지만 "이 계약이 이익률을 얼마나 올리고 현금흐름으로 언제 바뀌는지"는 아직 없다.
그래서 Stage2-Watch까지는 가능해도 Yellow/Green thesis로 확정하면 안 된다.
```

## 7. 다음 병목

P0 병목:

```text
KIND/DART 상세 본문 해상도와 primitive mapper feedback loop
```

세부:

```text
1. web search가 KIND viewer/listing URL을 가져오면 상세 본문인지 검사해야 한다.
   - "본 문서는 최종문서가 아니므로" 같은 안내문만 있으면 score source가 아니라 follow-up source다.

2. KIND viewer URL에서 실제 상세 공시/DART 원문으로 resolve하는 adapter가 필요하다.
   - 현재는 OpenDART가 이미 상세를 갖고 있는데, web fallback은 KIND 껍데기를 다시 가져오는 중이다.

3. primitive mapper가 rejected claim을 planner feedback으로 더 강하게 돌려야 한다.
   - 지금 v20의 남은 rejection은 source 문제가 아니라 no_allowed_primitive_for_predicate다.
   - 같은 KIND header를 반복 검색하지 말고 "마진/수익성 bridge 원문이 없다"는 feedback으로 다음 task를 바꿔야 한다.

4. accepted official claim만으로 Brain/Web promotion하면 안 된다.
   - v20은 official accepted claim이 많아도 web/LLM accepted claim 0개라 promotion을 막았다.
   - 이 차단은 맞다.
```

## 8. 다음 에이전트 공격 질문

다음 에이전트는 아래 질문부터 공격해야 한다.

```text
1. v20의 Stage1/Stage2-Watch/Red 85개는 모두 CENSUS_EVENT_BOARD인가?
   기대 답: 예. FULL_THESIS row는 0개여야 한다.

2. v20에서 web/LLM accepted score claim이 0개인가?
   기대 답: 예. web fetch/LLM extraction은 돌았지만 accepted score claim은 없다.

3. Naver로 찾은 KIND 공시가 더 이상 TrustedNews/BrokerReport로 포장되지 않는가?
   기대 답: 예. source_class=KIND로 찍힌다.

4. source-class mismatch가 사라졌는데도 왜 accepted가 0개인가?
   기대 답: fetched KIND 문서가 상세 계약본문이 아니라 header/정정요구 안내문이고,
   primitive mapper가 margin_bridge_visible로 인정하지 않았기 때문이다.

5. OpenDART accepted claim 19개가 왜 FULL_THESIS가 아닌가?
   기대 답: 계약 규모/기간/납품일정은 확인됐지만 margin/cash/revision/repeat evidence가 없어서
   C05 full thesis gate가 열리지 않는다.

6. 지금 당장 Green/Yellow를 내보내도 되는가?
   기대 답: 아니다. verified_score_present_count=0, full_thesis_stage_row_count=0이다.
```

## 9. 검증

좁은 source-class regression:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_contract_visibility_external_context_can_use_bounded_web \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_news_fallback_uses_news_source_class_when_report_pdf_is_first_preference \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_web_discovered_kind_document_keeps_official_kind_source_class \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_news_document_cannot_satisfy_broker_report_source_task \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_industry_media_full_news_is_not_rejected_as_general_search_when_report_task_has_news_fallback \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_web_discovered_kind_full_source_is_not_rejected_as_general_search_provider_error -v

result = Ran 6 tests / OK
```

전체 테스트:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_after_sourceclass_v20_artifact.json \
  --log output/test_full_repo_0701/full_unittest_after_sourceclass_v20.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 5041
failed_count = 0
error_count = 0
duration_seconds = 198.1864
artifact_sha256 = baea8ef9fd81b059b3551bcb450111302ed8be2d194679c244082f3032700af6
log_sha256 = 70a500d7710e147edb58089611c0b0ead51098a0d0f0ad7cfc58723a51fbcf38
```

v20 diagnostic:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v20 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 5 \
  --brain-max-fetches-per-task 1 \
  --brain-accepted-claim-target 1 \
  --brain-max-distinct-candidate-attempts 4 \
  --brain-claim-extractor-provider codex_cli \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate brain_web \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --write-operational-docs false

result = NOT_READY
```

## 10. 최종 판단

```text
이번 패치로 source-class false rejection은 한 단계 줄었다.

하지만 아직 운영 가능 상태는 아니다.
Stage label은 있지만 운영 FULL_THESIS Stage는 0개다.
web/LLM accepted score claim도 0개다.

현재 핵심 병목은:
  1. KIND/DART 상세 본문 resolve
  2. primitive mapper가 rejected claim을 planner feedback으로 제대로 되돌리는 루프
  3. margin/cash/revision/repeat evidence가 실제 accepted claim으로 닫힐 때까지 FULL_THESIS를 열지 않는 gate 유지
```

다음 에이전트가 이 문서를 보고 "Stage가 있으니 운영 가능"이라고 말하면 틀린 것이다.

정확한 표현은 다음이다.

```text
Census 상태판 Stage는 있다.
운영 FULL_THESIS Stage는 아직 없다.
source-class 버그 하나는 고쳤고,
다음 병목은 상세 원문 해상도와 primitive feedback loop다.
```
