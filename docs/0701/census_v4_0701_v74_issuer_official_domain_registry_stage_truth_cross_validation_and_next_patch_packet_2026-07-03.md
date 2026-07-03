# Census v4 0701 v74 Issuer Official Domain Registry / Stage Truth Cross Validation / Next Patch Packet

작성일: 2026-07-03

이 문서는 v73 산출물과 v74 최소 패치를 같이 검증한 리뷰 패킷이다. 다음 에이전트는 이 문서를 성공 보고서로 읽으면 안 된다.

한 줄 결론:

```text
Stage처럼 보이는 행은 3391개 있지만 전부 CENSUS_EVENT_BOARD 상태판이다.
운영자가 쓸 수 있는 FULL_THESIS Stage는 여전히 0개다.

v74는 운영 Stage를 만든 패치가 아니라,
진짜 issuer 공식 별도 도메인을 source-backed registry로만 열 수 있게 만든 source-quality 패치다.

v74 bounded live smoke도 NOT_READY이고 FULL_THESIS row는 0개다.
```

쉬운 예:

```text
상태판 Stage:
  "이 종목은 오늘 전체지도에서 Stage1 후보처럼 보인다"
  -> 조사 대상을 정리하는 라벨이다.
  -> 투자 판단용 최종 Stage가 아니다.

운영 FULL_THESIS Stage:
  "검증된 claim -> primitive -> score contribution -> StageCourt까지 닫혔다"
  -> 이때만 운영 Stage다.

현재 v73/v74 기준:
  전자는 있다.
  후자는 없다.
```

## 1. 이 문서를 쓰는 이유

최근 질문은 사실상 두 가지였다.

```text
1. 뭔가 잘못되고 있는 것 맞지?
2. Stage가 있는 애들이 있긴 해?
```

정확한 답:

```text
잘못될 수 있는 지점은 맞다.
다만 "Stage가 하나도 없다"가 아니라,
"상태판 Stage와 운영 Stage가 섞여 보이면 치명적"이다.
```

현재 시스템은 의도적으로 `CENSUS_EVENT_BOARD`와 `FULL_THESIS`를 분리한다.

```text
CENSUS_EVENT_BOARD
  전체 KRX universe에 평가 이벤트를 붙인 상태판.
  예: 아무 공시 없는 종목도 Stage0 / NoCurrentCatalyst로 표시된다.

FULL_THESIS
  source-backed accepted claim이 있고,
  primitive state와 score contribution이 있고,
  StageCourt trace까지 닫힌 운영 thesis.
```

이 구분이 무너지면 다음 사고가 난다.

```text
상태판 Stage2-Watch
  -> 운영 Stage2처럼 오해
  -> "왜 점수와 근거가 없냐" 문제가 발생
```

그래서 v74 문서는 숫자 기준으로 이 구분을 다시 박아둔다.

## 2. v73 산출물 기준 Stage 실체

검증 artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/readiness_verdict.json
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/census_stage_status.jsonl
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/goal_requirement_matrix_audit.json
```

### 2.1 Readiness verdict

```text
verdict = NOT_READY
stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
event_board_non_stage0_count = 85
```

의미:

```text
상태판에서 non-Stage0 후보 85개는 있다.
하지만 운영 full thesis Stage는 0개다.
```

### 2.2 `census_stage_status.jsonl` 분포

```text
total rows = 3391
stage_scope=CENSUS_EVENT_BOARD = 3391
stage_scope=FULL_THESIS = 0
operator_stage_use=NOT_FULL_THESIS_STAGE = 3391
```

base stage 분포:

| base_stage | count | 해석 |
| --- | ---: | --- |
| Stage0 | 3306 | 현재 catalyst 없는 상태판 label |
| Stage1 | 54 | 상태판 후보 label |
| Stage2-Watch | 30 | 상태판 watch label |
| Red | 1 | 상태판 risk-review label |

investigation status 분포:

| investigation_status | count | 해석 |
| --- | ---: | --- |
| NO_CURRENT_CATALYST | 3306 | 현재 점수 재료 없음 |
| PENDING | 48 | 추가 확인 필요 |
| COMPLETE | 36 | 상태판 관점의 처리 완료 |
| RISK_REVIEW | 1 | 상태판 risk 검토 |

중요:

```text
Stage1 54개, Stage2-Watch 30개가 보여도
운영 점수와 운영 Stage가 생성된 것이 아니다.
```

쉬운 예:

```text
학교 출석부에 "발표 후보"라고 적힌 것과
실제 시험지를 채점해서 "90점"이 나온 것은 다르다.

CENSUS_EVENT_BOARD는 출석부다.
FULL_THESIS가 시험 채점 결과다.
```

## 3. Brain/Web readiness 병목

검증 artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/brain_web_readiness_gate_audit.json
```

핵심 숫자:

| 항목 | v73 값 | minimum | 해석 |
| --- | ---: | ---: | --- |
| web_search_task_count | 5 | 20 | 부족 |
| web_search_call_count | 5 | 20 | 부족 |
| web_search_result_count | 41 | - | 검색 결과는 있음 |
| web_fetched_document_count | 1 | 10 | 부족 |
| llm_claim_extractor_attempt_count | 1 | 10 | 부족 |
| llm_claim_extractor_provider_error_count | 0 | - | extractor 장애는 아님 |
| web_or_llm_accepted_claim_count | 0 | 3 | 핵심 차단 |
| official_accepted_claim_count | 1 | - | 공식 source claim은 1개 |
| brain_promoted_stage_row_count | 0 | - | 승격 없음 |

직접 blocker:

```text
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
planner runs 22/30
web search tasks 5/20
web search calls 5/20
fetched documents 1/10
claim extractor attempts 1/10
web/LLM accepted claims 0/3
```

쉬운 예:

```text
검색 결과 41개가 있다는 것
  -> 자료 후보를 봤다는 뜻이다.

accepted claim 0개
  -> 점수 칸에 들어갈 수 있는 검증 문장이 하나도 없다는 뜻이다.
```

따라서 v73은 `검색을 조금 했다`이지 `운영 점수를 만들었다`가 아니다.

## 4. Full thesis seed 상태

검증 artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/full_thesis_seed_materialization_audit.json
```

숫자:

```text
verdict = PASS
seed_event_count = 85
trace_row_count = 85
planner_run_seed_count = 21
real_provider_success_seed_count = 1
accepted_claim_seed_count = 1
stagecourt_trace_seed_count = 1
full_thesis_promoted_seed_count = 0
```

status counts:

```text
PLANNER_NOT_RUN = 64
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 20
STAGECOURT_READY_NOT_PROMOTED = 1
```

해석:

```text
85개 상태판 후보가 full thesis refresh queue로 잡힌 것은 맞다.
하지만 실제 FULL_THESIS row로 승격된 seed는 0개다.
```

여기서 `verdict=PASS`는 "감사 장부가 내부적으로 맞다"는 뜻이다.
목표 완료 PASS가 아니다.

쉬운 예:

```text
대기열 명단이 정확하게 작성됐다.
하지만 실제 면접을 통과한 사람은 아직 0명이다.
```

## 5. 삼성전자 / SK하이닉스 smoke 상태

검증 artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/samsung_hynix_full_thesis_smoke.json
```

숫자:

```text
verdict = PENDING_FULL_THESIS_REFRESH
full_thesis_status = PENDING_FULL_THESIS_REFRESH
smoke_task_count = 14
score_allowed_before_execution = false
daily_event_and_full_thesis_separated = true
hardcoded_query_count = 0
```

해석:

```text
삼성전자와 SK하이닉스도 아직 "운영 점수 몇 점, Stage 몇"으로 말하면 안 된다.
refresh task는 준비돼 있지만 full thesis execution이 끝나지 않았다.
```

이전 90점대 / 60점대 논란과 연결하면:

```text
현재 정답은 "몇 점"이 아니라 "아직 운영 점수 산출 금지"다.
```

## 6. Goal matrix 기준 완료/미완료

검증 artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/goal_requirement_matrix_audit.json
```

요약:

```text
required_goal_completion_count = 19
required_goal_completion_pass_count = 14
required_goal_completion_pending_count = 5
required_goal_completion_fail_count = 0
goal_completion_minimum_pass = false
```

남은 pending gate:

| gate | 상태 | blocker |
| --- | --- | --- |
| FULL_THESIS_SMOKE_PASS | PENDING | full_thesis_smoke_pending |
| FULL_THESIS_PRODUCTION_PASS | PENDING | full_thesis_production_pass_false |
| FULL_THESIS_SEED_PROMOTION_PASS | PENDING | full_thesis_seed_promotion_pass_false |
| BRAIN_WEB_EVIDENCE_PASS | PENDING | brain_web_evidence_pass_false |
| ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS | PENDING | source_backed_replay_parity_all_archetypes_pending |

현재 의미:

```text
가짜 성공을 막는 장치는 많이 통과했다.
하지만 운영 full thesis 점수와 Stage를 만드는 핵심 경로는 아직 미완성이다.
```

## 7. v74 코드 패치: issuer official domain registry

패치 목적:

```text
v73은 CompanyGuide homepage의 동일 host 또는 하위 도메인만 자동 verified issuer original로 허용했다.
이건 안전하지만, 실제 회사가 별도 공식 도메인을 쓰면 너무 보수적으로 막는다.

v74는 별도 공식 도메인을 source-backed registry로만 열 수 있게 한다.
```

변경 파일:

```text
configs/e2r_issuer_official_domains_v1.json
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

### 7.1 새 registry

추가 파일:

```text
configs/e2r_issuer_official_domains_v1.json
```

현재 seed entry:

```text
000660 SK하이닉스
  news.skhynix.com
  news.skhynix.co.kr
```

주의:

```text
valid_from = 2026-07-03
verified_as_of = 2026-07-03
```

즉 이 registry는 `as_of_date=2026-07-01` live smoke에는 적용되면 안 된다.

쉬운 예:

```text
2026-07-03에 "이 도메인은 공식 뉴스룸"이라고 확인했다.
그러면 2026-07-01에 판단하던 사람이 그 장부를 알고 있었다고 보면 미래누수다.
그래서 2026-07-01 run에서는 이 registry row를 무시해야 한다.
```

### 7.2 source runner 변경

핵심 함수:

```text
_issuer_official_domain_authorities()
_issuer_official_domain_authorities_from_companyguide()
_issuer_official_domain_authorities_from_registry()
_issuer_official_domain_authority_from_registry_entry()
```

인정 조건:

```text
status = ACTIVE
symbol == event.symbol
host 존재
source_url 존재
source_anchor_text 존재
valid_from <= as_of_date
verified_as_of <= as_of_date
valid_to가 있으면 valid_to >= as_of_date
```

금지한 것:

```text
종목명 하드코딩
brand stem 자동 허용
검색 결과 title/snippet만 보고 official domain 생성
source_url/anchor 없는 registry row 허용
as_of_date 이후 verified row 허용
```

쉬운 예:

```text
허용:
  registry에 000660 / news.skhynix.co.kr / source_url / KOR anchor / valid_from<=as_of_date가 있다.
  검색 결과 URL도 news.skhynix.co.kr이다.
  title/snippet에 SK하이닉스 alias가 있다.
  -> verified issuer original 후보 가능.

차단:
  news-skhynix.co.kr
  skhynix-investor.co.kr
  skhynix.com.fake-domain.com
  -> 이름이 비슷해도 registry host와 다르므로 차단.
```

### 7.3 lineage 재검증 강화

source runner의 `_document_has_verified_issuer_original_lineage()`도 marker 문자열만 믿지 않도록 맞췄다.

이제 필요 조건:

```text
source_lineage_id에 verified_issuer_original marker 존재
authority host 존재
result host 존재
canonical_url host 존재
canonical_url host == result host
result host == authority host 또는 result host가 authority host의 하위 도메인
```

쉬운 예:

```text
lineage에 verified_issuer_original이라고 적혀 있어도
canonical_url이 다른 host면 CompanyNewsroom으로 승급되지 않는다.
```

## 8. v74가 해결한 것과 해결하지 못한 것

해결한 것:

```text
1. 공식 별도 도메인을 열 방법이 생겼다.
2. 그 방법은 source-backed registry를 거쳐야 한다.
3. 2026-07-03에 확인한 registry row가 2026-07-01 run에 들어가지 않도록 as-of gate가 있다.
4. spoof host는 계속 막힌다.
5. registry lineage가 bridge에서 다시 검증될 수 있다.
```

해결하지 못한 것:

```text
1. v73 live artifact의 web_or_llm_accepted_claim_count=0은 그대로다.
2. FULL_THESIS row=0도 그대로다.
3. 삼성전자/하이닉스 운영 점수는 아직 산출 금지다.
4. 모든 아키타입 source-backed replay는 아직 32/32가 아니다.
5. stop-on-resolution은 아직 accepted direct claim 기준으로 완전히 닫히지 않았다.
```

중요:

```text
v74 registry 패치는 "문서 원문성을 안전하게 열 수 있는 길"을 만든 것이다.
그 자체가 점수나 Stage를 만들지는 않는다.
```

## 9. 검증 결과

### 9.1 Targeted registry / lineage tests

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_live_full_bounded_marks_company_homepage_subdomain_as_verified_newsroom_original \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_live_full_bounded_does_not_mark_issuer_domain_spoof_hosts_as_verified_original \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_live_full_bounded_marks_registry_backed_alternate_official_domain \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_live_full_bounded_ignores_future_registry_official_domain \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_verified_company_newsroom_original_can_score_direct_customer_allocation_claim \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_verified_company_newsroom_registry_lineage_can_score_alternate_official_domain \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_verified_company_newsroom_lineage_requires_homepage_subdomain_match \
  -v
```

결과:

```text
Ran 7 tests
OK
```

검증된 케이스:

| 테스트 | 의미 |
| --- | --- |
| homepage subdomain accepted | `news.skhynix.com`은 `skhynix.com` 하위 도메인으로 인정 |
| spoof hosts rejected | 비슷한 host는 자동 official 금지 |
| registry alternate domain accepted | registry가 있으면 `news.skhynix.co.kr` 허용 |
| future registry ignored | valid_from/verified_as_of가 as-of 이후면 무시 |
| bridge direct claim accepted | verified newsroom direct claim은 score path 가능 |
| bridge registry lineage accepted | registry lineage도 host 일치 시 score path 가능 |
| bridge mismatched lineage rejected | `skhynix.com:news.skhynix.co.kr` 같은 불일치 lineage는 거부 |

### 9.2 Related regression

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  -v
```

결과:

```text
Ran 91 tests in 9.125s
OK
```

### 9.3 Full suite

실행:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5109 tests in 220.472s
OK
```

### 9.4 v74 bounded live smoke

실행:

```bash
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 E2R_CODEX_EXTRACTOR_TIMEOUT_SECONDS=120 PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v74 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-timeout-seconds 120 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

결과:

```text
stdout = NOT_READY
exit code = 1
```

Readiness:

```text
verdict = NOT_READY
stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
event_board_non_stage0_count = 85
```

Stage status:

```text
rows = 3391
stage_scope=CENSUS_EVENT_BOARD = 3391
operator_stage_use=NOT_FULL_THESIS_STAGE = 3391
FULL_THESIS row = 0
```

base stage:

```text
Stage0 = 3306
Stage1 = 54
Stage2-Watch = 30
Red = 1
```

Brain/Web gate:

| 항목 | v74 값 | minimum | 해석 |
| --- | ---: | ---: | --- |
| web_search_task_count | 6 | 20 | 부족 |
| web_search_call_count | 6 | 20 | 부족 |
| web_search_result_count | 65 | - | 검색 결과는 늘어남 |
| web_fetched_document_count | 2 | 10 | 부족 |
| llm_claim_extractor_attempt_count | 2 | 10 | 부족 |
| llm_claim_extractor_provider_error_count | 0 | - | extractor 장애는 아님 |
| web_or_llm_accepted_claim_count | 0 | 3 | 핵심 차단 유지 |
| official_accepted_claim_count | 1 | - | 공식 source claim 1개 |
| brain_promoted_stage_row_count | 0 | - | 승격 없음 |

web fetched documents:

```text
rows = 2
verified_issuer_original = false for both rows
verified_issuer_authority_source_kind = null for both rows
```

해석:

```text
v74 registry row는 valid_from=2026-07-03이라
as_of_date=2026-07-01 live smoke에 적용되지 않았다.

즉 이 패치가 0701 판단에 미래 확인 도메인을 끌어와 READY를 만든 흔적은 없다.
```

v73 대비:

| 항목 | v73 | v74 | 해석 |
| --- | ---: | ---: | --- |
| web_search_task_count | 5 | 6 | 소폭 증가 |
| web_search_call_count | 5 | 6 | 소폭 증가 |
| web_search_result_count | 41 | 65 | 증가 |
| web_fetched_document_count | 1 | 2 | 증가 |
| llm_claim_extractor_attempt_count | 1 | 2 | 증가 |
| web_or_llm_accepted_claim_count | 0 | 0 | 미해결 |
| FULL_THESIS row | 0 | 0 | 미해결 |

중요:

```text
v74 smoke는 registry 패치가 미래누수를 만들지 않는다는 확인에 가깝다.
운영 Stage 성공 증거가 아니다.
```

## 10. 교차검증 관점의 공격 포인트

다음 에이전트는 아래를 먼저 공격해야 한다.

### 10.1 상태판 Stage를 운영 Stage로 오해하는지

질문:

```text
census_stage_status.jsonl에 Stage1/Stage2-Watch가 있으니 Stage가 있는 것 아닌가?
```

답:

```text
아니다.
stage_scope=CENSUS_EVENT_BOARD이고 operator_stage_use=NOT_FULL_THESIS_STAGE다.
FULL_THESIS row는 0개다.
```

검증 명령:

```bash
python - <<'PY'
import json, collections, pathlib
p=pathlib.Path('output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/census_stage_status.jsonl')
rows=[json.loads(l) for l in p.read_text().splitlines() if l.strip()]
print(collections.Counter(r.get('stage_scope') for r in rows))
print(collections.Counter(r.get('operator_stage_use') for r in rows))
print(collections.Counter(r.get('base_stage') for r in rows))
PY
```

### 10.2 registry가 brand-stem 하드코딩인지

질문:

```text
결국 SK하이닉스 예외처리 아닌가?
```

답:

```text
아니다.
code path는 symbol/host/source_url/anchor/date/status가 있는 registry row를 읽는다.
종목명 조건문이나 archetype 조건문으로 허용하지 않는다.
```

공격해야 할 부분:

```text
registry entry가 충분히 source-backed인지
source_url/anchor가 실제 공식 페이지에서 온 것인지
registry 갱신 audit가 필요한지
```

### 10.3 registry가 미래누수를 만들지 않는지

질문:

```text
2026-07-03에 확인한 news.skhynix.co.kr을 2026-07-01 판단에 쓰는가?
```

답:

```text
쓰면 안 된다.
테스트가 future registry ignored를 검증한다.
```

### 10.4 registry lineage가 bridge에서 재검증되는지

질문:

```text
source_lineage_id 문자열에 marker만 있으면 score path가 열리는가?
```

답:

```text
아니다.
bridge는 canonical_url host와 lineage result host를 다시 비교한다.
```

### 10.5 이 패치로 web/LLM accepted claim이 생기는지

질문:

```text
v74로 web_or_llm_accepted_claim_count=0이 해결됐나?
```

답:

```text
아직 아니다.
이 패치는 accepted claim을 만들 수 있는 공식 도메인 경로를 연 것이다.
실제 live run에서 verified issuer document fetch -> LLM claim extraction -> accepted mapping까지 통과해야 count가 오른다.
```

## 11. 다음 패치 방향

우선순위:

```text
P0. live Brain/Web에서 verified issuer official-domain 문서를 실제로 fetch하고 accepted claim까지 닫기
P1. accepted direct claim 기준 stop-on-resolution 구현
P2. `web_or_llm_accepted_claim_count >= 3`을 가짜 count 없이 충족
P3. SK하이닉스/Samsung full thesis refresh가 score_allowed_before_execution=false에서 실제 StageCourt trace로 넘어가는지 검증
P4. C01~C32 all-archetype source-backed replay parity 확장
```

### 11.1 P0 상세

목표:

```text
verified issuer official-domain document
  -> EvidenceDocument
  -> EvidenceAnchor
  -> LLM/raw assertion
  -> target/temporal adjudication
  -> primitive mapping
  -> accepted claim
  -> score contribution
```

현재 v73:

```text
web_fetched_document_count = 1
web_or_llm_accepted_claim_count = 0
```

원하는 다음 상태:

```text
web_fetched_document_count >= 10
web_or_llm_accepted_claim_count >= 3
단, source_lineage_unverified_original이나 snippet-only claim으로 count를 채우면 실패
```

### 11.2 P1 상세

현재 문제:

```text
official fetch가 있어도 그 문서가 primitive를 만족하는 accepted direct claim인지 acquisition 단계에서는 모른다.
그래서 stop-on-resolution을 단순 fetch 기준으로 닫으면 안 된다.
```

올바른 기준:

```text
source task primitive에 대응하는 accepted direct claim이 생겼다
  -> 같은 task의 web fallback 종료

coverage-only official 문서만 있다
  -> 필요한 follow-up은 계속 가능
```

쉬운 예:

```text
DART 회사개황만 가져왔다.
  -> 회사가 존재한다는 coverage일 뿐 HBM 고객 배정 claim은 아니다.
  -> stop하면 안 된다.

회사 뉴스룸에서 "HBM 고객 물량 배정 확정" claim이 accepted됐다.
  -> customer_preorder_or_allocation primitive가 닫혔다.
  -> 해당 task는 stop 가능.
```

## 12. 외부 리뷰어에게 넘길 결론

외부 리뷰어가 공격해야 할 핵심 문장:

```text
v74는 NOT_READY를 READY로 바꾸지 않았다.
v74는 FULL_THESIS Stage를 만들지 않았다.
v74는 상태판 Stage와 운영 Stage의 혼동을 줄이면서,
공식 별도 도메인을 안전하게 열 registry 기반 source-quality 경로만 추가했다.
```

현재 최종 상태:

```text
readiness = NOT_READY
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
web/LLM accepted claim = 0 in v74 artifact
registry patch targeted tests = PASS
related regression = PASS
full suite = PASS, 5109 tests
v74 bounded live smoke = NOT_READY, no FULL_THESIS row
```

운영자에게 말할 수 있는 답:

```text
지금 stage가 있긴 하다.
하지만 그것은 전체지도 상태판 stage다.
실제 운영 stage는 아직 없다.
```
