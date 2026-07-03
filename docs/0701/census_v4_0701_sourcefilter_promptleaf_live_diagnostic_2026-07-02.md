# Census v4 0701 Source Filter / Prompt Leaf Live Diagnostic

작성 시점: 2026-07-02 KST  
latest diagnostic: `output/census_v4/2026-07-01-brain-web-diagnostic-sourcefilter-v1`  
previous diagnostic: `output/census_v4/2026-07-01-brain-web-diagnostic-promptleaf-v1`  
canonical output: `output/census_v4/2026-07-01`

> 2026-07-02 추가 주의: 이 문서는 `sourcefilter-v1` 스냅샷이다.
> 최신 Brain/Web 보조 진단은
> `output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6`이며,
> 우선 읽을 문서는
> `docs/0701/census_v4_0701_sourcequality_v6_source_router_patch_result_2026-07-02.md`다.

## 직접 답

```text
운영 FULL_THESIS Stage는 여전히 없다.
Brain/Web accepted score claim도 여전히 0개다.
다만 Planner prompt/response leaf는 실제 live 진단에서 남기기 시작했다.
```

숫자:

```text
verdict = NOT_READY
BRAIN_WEB_PARTIAL row = 0
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0

brain_accepted_claim_count = 0
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0

llm_prompts.jsonl rows = 2
llm_responses.jsonl rows = 2
planner_raw/prompts/*.json = 2
planner_raw/responses/*.json = 2
planner_run_row_count = 22
real_llm_planner_call_count = 2

web_fetched_documents = 10
web_rejected_documents = 13
claim_extractor_runs = 10
raw_assertions = 131
raw_assertion_rejections = 41
```

쉬운 예:

```text
이제 면접 녹취록은 남는다.
  -> LLM에게 무엇을 물었고 무엇을 답했는지 prompt/response leaf로 확인 가능하다.

하지만 합격자는 아직 없다.
  -> web/LLM에서 점수 칸에 들어갈 accepted claim은 0개다.
```

## 이번 패치 의미

### 1. promptleaf-v1 실제 live proof

`promptleaf-v1` 코드 패치 후 새 live diagnostic에서 다음이 확인됐다.

```text
llm_prompts.jsonl = 2 rows
llm_responses.jsonl = 2 rows
planner_runs.jsonl의 real provider row 2개가 prompt_hash/response_hash/raw path를 보유
planner_raw/prompts/*.json = 2 files
planner_raw/responses/*.json = 2 files
```

이제 다음 에이전트는 planner가 실제로 어떤 rejected claim feedback을 받았는지 raw prompt에서 검증할 수 있다.

### 2. stock quote/profile page filter

새 코드 패치:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
```

새 규칙:

```text
finance.naver.com/item/main.naver 같은 종목 시세/프로필 페이지는
대상회사명이 들어 있어도 EvidenceDocument로 넘기지 않는다.
web_rejected_documents에
web_fetch_stock_quote_or_profile_page_not_source_document
로 남긴다.
```

쉬운 예:

```text
대웅 Npay 증권 페이지:
  현재가, 거래량, 시가, 고가, 저가가 있다.

이건 "대웅 신규시설투자가 매출/생산능력으로 연결됐다"는 원문 증거가 아니다.
따라서 LLM extractor까지 보내지 말고 source 단계에서 거절해야 한다.
```

중요:

```text
이건 점수 하드코딩이 아니다.
특정 종목 예외도 아니다.
소스가 뉴스/IR/공시 원문인지, 시세판인지 구분하는 공통 source hygiene 규칙이다.
```

### 3. Census event score-evidence alias counters

새 critical counter:

```text
assessment_event_used_as_score_evidence_count = 0
event_without_accepted_claim_nonzero_score_count = 0
score_contribution_without_accepted_claim_support_count = 0
```

검증:

```text
output/census_v4/2026-07-01 = all 0
output/census_v4/2026-07-01-brain-web-diagnostic-sourcefilter-v1 = all 0
```

쉬운 예:

```text
CensusAssessmentEvent는 출석 도장이다.
출석 도장만으로 점수를 주면 안 된다.

CandidateEvent는 시험지를 열어주는 사건이다.
그 사건도 accepted_claim으로 닫히기 전에는 점수 근거가 아니다.
```

## sourcefilter-v1 진단 해석

이번 sourcefilter-v1은 `003090` 대웅 신규시설투자 정정 이벤트 하나를 bounded Brain/Web으로 본 결과다.

주요 거절:

```text
raw_assertion_rejections = 41
  temporal_status_rejected = 24
  primitive_mapping_rejected = 9
  target_scope_or_directness_rejected = 8

web_rejected_documents = 13
  post_extraction_no_score_eligible_claim = 10
  web_fetch_target_not_in_title_snippet_or_lead = 2
  web_fetch_target_not_found_in_full_text = 1
```

해석:

```text
이 이벤트는 대체로 "신규시설투자 정정 / 기간 연장 / 과거 공시 회고" 성격이다.
운영 leverage, volume growth, cash/revision primitive로 받아들이기에는 부족하다.
따라서 accepted claim 0은 여기서는 안전한 결과다.
```

쉬운 예:

```text
"공장 투자기간이 1년 연장됐다"
  -> 일정/정정 claim일 수는 있다.

"그래서 생산량이 늘고 매출/현금흐름이 확인됐다"
  -> 별도 원문 증거가 있어야 한다.

두 번째 증거가 없는데 점수를 주면 다시 예전처럼 점수가 흔들린다.
```

## 검증

Targeted:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_event_separation \
  tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 19 tests
OK
```

추가 targeted:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_bundle_export -v
```

결과:

```text
Ran 35 tests
OK
```

Full regression:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
test_count = 5009
failed_count = 0
error_count = 0
duration_seconds = 187.7625
artifact_sha256 = 0aa9602e6bc580ea899270ef739b6fe74d22e82e96bdb78c9a87c22ae63215b3
log_sha256 = 49a1d70499ba673ed6d1829cd82ee6822c356df11aa88e9e9155fac72a76b446
```

## 남은 P0

```text
1. web/LLM accepted claim을 0에서 실제 source-backed claim으로 올려야 한다.
2. 단, sourcefilter-v1의 대웅 정정 이벤트처럼 부적합한 이벤트를 억지로 올리면 안 된다.
3. 다음 patch는 LLM planner가 rejected feedback을 보고 더 직접적인 official/IR/source route를 고르도록 해야 한다.
4. BRAIN_WEB_PARTIAL 승격은 web_or_llm_accepted_claim_count >= 3, StageCourt trace, score contribution 연결이 모두 있어야 한다.
5. FULL_THESIS 운영 Stage는 아직 0개이므로 goal 완료가 아니다.
```

한 줄 결론:

```text
감사 가능성은 좋아졌다.
하지만 운영 점수/Stage가 생긴 것은 아니며, accepted source-backed claim을 실제로 만드는 acquisition/planner 품질 패치가 다음 핵심이다.
```
