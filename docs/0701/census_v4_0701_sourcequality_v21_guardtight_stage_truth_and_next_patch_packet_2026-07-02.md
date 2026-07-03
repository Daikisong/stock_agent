# Census v4 0701 SourceQuality v21 Guard-Tight Stage Truth / Next Patch Packet

작성일: 2026-07-02

이 문서는 `sourcequality-v20` 문서를 교차검증한 뒤, guard를 더 보수적으로 조인 최신 감사 패킷이다.

## 1. 최종 직접 답

```text
Stage row는 있다.
하지만 운영 FULL_THESIS Stage는 아직 0개다.

v21 기준:
  CENSUS_EVENT_BOARD row = 3391
  FULL_THESIS row = 0
  FULL_E2R_100 verified score row = 0
  verified_score_present_count = 0
  web/LLM accepted score claim = 0
```

쉬운 예:

```text
출석부에는 "관찰 필요" 같은 상태 메모가 붙었다.
하지만 정식 성적표는 아직 한 명도 발급되지 않았다.

따라서 Stage1/Stage2-Watch/Red가 보인다고 해서
운영용 Green/Yellow/Red thesis가 완성된 것은 아니다.
```

## 2. v21 산출물

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21
```

Stage summary:

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

## 3. 교차검증 반영 사항

두 개의 읽기 전용 교차검증을 받았다.

### 문서/숫자 검증

결론:

```text
치명 이슈 없음.
Stage row는 있지만 운영 FULL_THESIS Stage는 0개라는 결론은 artifact와 일치.
```

지적:

```text
README 안에 v20 최신 포인터와 v17 historical 포인터가 섞여 있었다.
```

반영:

```text
README 상단 최신 기준을 v21/5042로 교체.
v17/5036 기록은 historical baseline으로 명시.
```

### 코드 안전성 검증

결론:

```text
치명 이슈 없음.
BrokerReportPublicPDF가 NEWS를 그대로 먹는 길은 막혀 있음.
```

중간 지적:

```text
1. v20은 general_search_not_score_source 예외가 NEWS까지 너무 넓게 열릴 수 있었다.
2. official URL 판정이 substring 기반이라 fake path에 kind.krx 문자열이 있으면 위험했다.
3. source_class가 execution 단위라 여러 문서가 섞이면 문서별 source_class가 필요하다.
```

v21 반영:

```text
1. NEWS는 trusted connector/domain allowlist가 생기기 전까지 general search provider 경유 점수 금지.
2. DART/KIND/KRX/CompanyGuide 판정은 exact hostname allowlist로 좁힘.
3. fake path example.com/.../kind.krx.co.kr/...가 KIND로 승격되지 않는 테스트 추가.
4. 문서별 source_class는 구조 변경 범위가 커서 다음 P1로 남김.
```

쉬운 예:

```text
네이버로 DART 공시를 찾았다.
  -> 점수 근거는 DART 공시다.

네이버로 일반 뉴스 전문을 찾았다.
  -> 지금은 아직 점수 근거가 아니다.
  -> trusted news connector나 domain allowlist가 붙기 전까지는 diagnostics/follow-up 재료다.

example.com/kind.krx.co.kr/fake 를 찾았다.
  -> KIND가 아니다.
  -> hostname이 정확히 kind.krx.co.kr일 때만 KIND다.
```

## 4. v21의 Naver 실행 결과

v21에서 Naver 경유 execution은 1건이다.

```text
symbol = 114450
provider_name = live_official_source_provider_registry+NaverFreeSearchProvider
source_class = IndustryMedia
primitive_gap = cost_overrun
document_url = https://www.digitaltoday.co.kr/news/articleView.html?idxno=665445
status = NO_EVIDENCE_FOUND
accepted_claim_ids = []
```

차단 사유:

```text
source_task_provider_error_score_block:general_search_not_score_source
source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider
primitive_mapping_rejected:no_allowed_primitive_for_predicate
target_scope_not_allowed:UNRELATED
target_not_direct:NOT_TARGET_SCOPED
```

해석:

```text
v20에서는 source-class 문제를 고치며 NEWS까지 넓게 열릴 여지가 있었다.
v21에서는 NEWS를 다시 점수 금지로 잠갔다.
따라서 web/LLM accepted score claim은 여전히 0개이고, 이 차단은 의도된 보수성이다.
```

## 5. 현재 114450 공식 DART 상태

OpenDART 공식 원문 accepted claim은 존재한다.

```text
accepted_claims rows = 116
source_provider = OpenDART 116
symbol 114450 accepted_claims = 25
```

114450에서 확인된 대표 primitive:

```text
contract_quality
contract_amount_to_prior_sales
contract_duration_months
delivery_schedule
```

하지만 FULL_THESIS가 아닌 이유:

```text
margin_bridge_visible 미충족
cash_or_revision_conversion 미충족
repeat evidence family 미충족
multi-source confirmation 미충족
web/LLM accepted score claim 0개
```

쉬운 예:

```text
"계약금액이 최근 매출의 41.18%"라는 계약 영수증은 있다.
하지만 "이 계약이 이익률을 얼마나 올리고 현금흐름으로 언제 바뀌는가"는 아직 없다.
그래서 운영 Yellow/Green thesis를 열면 안 된다.
```

## 6. 검증

좁은 regression:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_news_fallback_uses_news_source_class_when_report_pdf_is_first_preference \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_web_discovered_kind_document_keeps_official_kind_source_class \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_web_discovered_fake_kind_path_does_not_become_official_kind_source_class \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_news_document_cannot_satisfy_broker_report_source_task \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_industry_media_full_news_from_general_search_is_rejected_until_trusted_news_connector_exists \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_web_discovered_kind_full_source_is_not_rejected_as_general_search_provider_error -v

result = Ran 6 tests / OK
```

전체 테스트:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_after_sourceclass_v21_guardtight_artifact.json \
  --log output/test_full_repo_0701/full_unittest_after_sourceclass_v21_guardtight.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 5042
failed_count = 0
error_count = 0
duration_seconds = 199.1275
artifact_sha256 = e259f571feb672804c739628d93929844b08cc91ccf3a3325ab6a3712bc3ca71
log_sha256 = 1e96b0edee72f47e6c93280e5338c7547dd6e331f5f035d0e74c1c8180739be9
```

v21 diagnostic:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21 \
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
  --test-result-artifact output/test_full_repo_0701/full_unittest_after_sourceclass_v20_artifact.json \
  --write-operational-docs false

result = NOT_READY
```

주의:

```text
v21 diagnostic 실행에는 v20 full-test artifact를 입력했다.
그 뒤 최신 코드 기준 full unittest를 다시 돌려 5042 OK artifact를 만들었다.
따라서 readiness 결과는 NOT_READY이고,
최신 repo test 증거는 full_unittest_after_sourceclass_v21_guardtight_artifact.json이다.
```

## 7. 다음 패치 방향

P0:

```text
KIND/DART 상세 본문 resolver
```

현재 web/KIND fetch는 header나 안내문만 잡는 경우가 있다. 상세 계약본문, 첨부 본문, DART 원문으로 resolve해야 한다.

P0:

```text
primitive mapper feedback loop
```

`primitive_mapping_rejected:no_allowed_primitive_for_predicate`가 나오면 같은 종류의 header/roundup/news를 반복하지 말고, planner feedback에 다음처럼 돌려야 한다.

```text
현재 문서는 margin_bridge_visible을 채우지 못했다.
계약금액/기간은 이미 DART에서 확인됐다.
다음 검색/소스 task는 OPM, 매출총이익, 원가, 판가, cash/revision bridge만 겨냥해야 한다.
```

P1:

```text
document_id -> source_class mapping
```

현재 `SourceAcquisitionResultV4.source_class`는 execution 단위다. 여러 문서가 섞이면 문서별 source_class가 필요하다.

P1:

```text
trusted news connector/domain allowlist
```

NEWS를 운영 점수로 쓰려면 단순 Naver general search가 아니라 trusted connector 또는 domain/source-family allowlist가 필요하다.

## 8. 최종 판단

```text
v21 기준으로 Stage가 있는 애들은 있다.
하지만 전부 CENSUS_EVENT_BOARD 상태판 Stage다.

운영 FULL_THESIS Stage는 없다.
web/LLM accepted score claim도 없다.

source-class false rejection은 줄였고,
NEWS score leakage 위험은 다시 잠갔다.

다음 핵심은 상세 원문 resolver와 mapper feedback loop다.
```
