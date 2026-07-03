# Census v4 0701 v39 Source Lineage Good Retry Acceptance Chain

작성일: 2026-07-02 KST

## 0. 결론

v39는 v35~v38에서 막은 `source_lineage_unverified_original` 경로의 반대편을 검증한다.

v35~v38이 확인한 것:

```text
일반검색/네이버/업계매체처럼 원문 lineage가 불확실한 source가 탈락했다.
그 뒤 LLM retry가 또 discovery-only source만 내면 실행하지 말고
REJECTED_BY_POLICY leaf row로 남긴다.
```

v39가 추가로 확인한 것:

```text
같은 source-lineage 실패 뒤에도
LLM retry가 DART/IR/회사 뉴스룸/원문 PDF처럼 원문 검증 가능한 source task를 내면
그 task는 버리지 않고 실행한다.
그리고 실제 원문 anchor에서 accepted claim이 나오면
retry planner의 primary archetype으로 watchlist row가 갱신된다.
```

쉬운 예:

```text
1차 시도:
  "한전변압기 고객 배정 일반 뉴스"를 일반검색으로 가져옴
  -> 원문 lineage 미검증
  -> score evidence로 탈락

LLM feedback retry:
  "한전변압기 단일판매 공급계약 원문 계약금액"을 다시 제안
  -> DART 같은 원문 가능 source class 포함

2차 실행:
  DART 원문 anchor에서 계약금액/매출대비/기간 claim 추출
  -> accepted_claim_ids 생김
  -> primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

중요:

```text
이 패치는 FULL_THESIS 운영 Stage가 생겼다고 주장하지 않는다.
이 패치는 source-lineage feedback retry의 양성 경로가
accepted claim까지 연결되는지 고정한 회귀 테스트다.
```

## 1. 왜 필요한가

이전 패치들은 주로 "나쁜 재시도를 막는" 방향이었다.

```text
일반검색 원문 미검증 reject
-> LLM이 다시 NaverSearch/GeneralWeb/IndustryMedia만 제안
-> 실행하지 않음
-> REJECTED_BY_POLICY row로 감사에 남김
```

이것만 있으면 다음 공격이 가능하다.

```text
"그럼 원문 미검증으로 한 번 막히면 좋은 재시도도 다 죽는 것 아니냐?"
"LLM이 DART/IR로 방향을 바꿔도 실제 claim까지 이어지는 증거가 있냐?"
"source-lineage guard가 너무 방어적이라 Research Brain을 살리지 못하는 것 아니냐?"
```

v39는 이 공격을 직접 테스트로 막는다.

```text
나쁜 retry:
  discovery-only -> drop + audit

좋은 retry:
  original-capable source class -> execute -> accepted claim 가능
```

즉 guard의 목표는 "웹을 무조건 막는 것"이 아니다.
목표는 "score source가 아닌 일반검색 결과를 점수에 넣지 말고, LLM에게 더 나은 원문 경로를 찾게 하는 것"이다.

## 2. 코드 변경

수정 파일:

```text
tests/test_research_brain_v4_operational_modes.py
docs/0701/README.md
docs/0701/census_v4_0701_v39_source_lineage_good_retry_acceptance_chain_2026-07-02.md
```

추가된 테스트:

```text
tests/test_research_brain_v4_operational_modes.py:903
  test_source_lineage_feedback_retry_can_execute_original_source_and_accept_claim
```

추가된 테스트 헬퍼:

```text
tests/test_research_brain_v4_operational_modes.py:1890
  _SourceLineageRetryAcceptanceRunner
```

이 헬퍼는 실제 운영 connector가 아니라 unit runner다.
목적은 source-lineage retry 정책의 상태 전이를 고정하는 것이다.

## 3. 검증한 상태 전이

### 3.1 1차 source failure

1차 source runner는 다음을 반환한다.

```text
source_class = TrustedNews
provider_name = NaverFreeSearchProvider
status = NO_EVIDENCE_FOUND
stop_reason = source_lineage_unverified_original
web_rejected_documents.not_eligible_reasons =
  - source_task_provider_error_score_block:general_search_not_score_source
  - source_provider_document_type_mismatch:TrustedNews:general_web_search_provider
  - source_lineage_unverified_original:TrustedNews:general_web_search_provider
```

의미:

```text
검색 결과나 뉴스 제목이 있어도
원문 lineage가 검증되지 않으면 점수 evidence가 아니다.
```

### 3.2 feedback retry planner

orchestrator는 위 실패를 planner feedback으로 돌려준다.

검증된 feedback:

```text
previous_source_lineage_unverified_original
previous_sources_failed_before_or_after_extraction
```

중요한 점:

```text
feedback에는 score/stage 목표가 들어가지 않는다.
LLM에게 "몇 점 올려라"가 아니라 "이 source가 왜 탈락했는지"만 알려준다.
```

### 3.3 original-capable retry task 유지

retry planner의 2차 output은 `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`로 primary를 바꾸고,
계약금액 primitive를 확인하는 task를 낸다.

테스트에서는 DART source class가 포함된 retry task가 만들어진다.

정책:

```text
source_lineage_unverified_original retry라도
DART / KIND / KRX / IR / CompanyNewsroom / ReportPDF / TrustedNews 같은
원문 또는 원문 검증 가능 source class가 있으면 버리지 않는다.
```

반대로 다음은 버린다.

```text
NaverSearch / GeneralWeb / IndustryMedia / News / Web
```

### 3.4 2차 원문 anchor에서 accepted claim 생성

2차 runner는 DART-like 원문 anchor를 반환한다.

테스트 원문:

```text
한전변압기 단일판매·공급계약체결 계약금액 1500억원 최근매출액 대비 15.0%
계약기간 2026-06-29 ~ 2028-06-29
```

정상 결과:

```text
accepted_claim_ids 존재
adjudicated_claim_to_accepted_claim_count > 0
source_lineage_feedback_retry_dropped_count = 0
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

쉬운 의미:

```text
처음 검색은 틀렸지만,
LLM이 원문 쪽으로 방향을 바꾸면
그 원문에서 실제 계약 claim을 만들 수 있다.
```

## 4. 하드코딩 여부

이 테스트는 종목별 운영 예외를 추가하지 않는다.

하지 않은 것:

```text
if symbol == "005930": pass
if company == "삼성전자": pass
if archetype == "C05": 무조건 claim 생성
```

검증한 것:

```text
source-lineage 실패 feedback
-> retry planner 호출
-> original-capable source task 유지
-> real document / anchor / claim path 실행
-> accepted claim이 있으면 retry primary로 갱신
```

즉 하드코딩된 검색어 생성 패치가 아니라,
이미 LLM이 낸 retry plan을 deterministic policy가 어떻게 처리하는지 고정한 테스트다.

## 5. 테스트 결과

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_feedback_retry_can_execute_original_source_and_accept_claim -v
```

결과:

```text
Ran 1 test in 0.521s
OK
```

운영 모드 테스트 전체:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 47 tests in 2.470s
OK
```

관련 확장 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_provider_failure_pending -v
```

결과:

```text
Ran 137 tests in 40.700s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5071 tests in 219.963s
OK
```

정적 whitespace 검사:

```bash
git diff --check -- tests/test_research_brain_v4_operational_modes.py
```

결과:

```text
OK
```

## 6. 현재 진실표

v39 이후에도 아래 사실은 변하지 않는다.

```text
CENSUS_EVENT_BOARD 상태판 Stage rows:
  exists

operator-admissible FULL_THESIS rows:
  still 0

FULL_E2R_100 verified score rows:
  still 0

Brain/Web readiness:
  source-lineage bad retry drop은 감사 가능
  source-lineage good retry acceptance chain은 unit 수준에서 검증
  그러나 live production full-thesis 승격은 아직 별도 acceptance 필요
```

쉬운 예:

```text
이번 패치는 배관 테스트다.
물이 한 번 막혔을 때 다른 배관으로 다시 흘러갈 수 있는지 확인했다.
하지만 아직 실제 도시 전체에 물이 안정적으로 공급된다고 선언한 것은 아니다.
```

운영 언어로 바꾸면:

```text
원문 미검증 웹 실패 -> LLM feedback -> 원문 source retry -> accepted claim
```

이 체인이 테스트로 고정됐다.

하지만:

```text
accepted claim -> score contribution -> StageCourt -> FULL_THESIS promoted row
```

이 전체 운영 row가 canonical output에 대량으로 존재한다는 증명은 아직 아니다.

## 7. 다음 에이전트가 공격해야 할 지점

다음 리뷰어는 아래를 빡세게 봐야 한다.

### 7.1 unit runner 한계

v39의 accepted claim은 unit runner가 DART-like 원문 anchor를 만든 것이다.

공격 질문:

```text
실제 OpenDART/KIND/IR connector에서 같은 source-lineage retry가 발생했을 때도
web_rejected -> planner feedback -> retry task -> accepted claim leaf가 이어지는가?
```

다음 패치 방향:

```text
frozen live snapshot 또는 실제 connector fixture로
source-lineage retry acceptance chain을 한 단계 더 재현한다.
```

### 7.2 retry primary 갱신의 안전성

v39는 retry에서 C06 -> C05로 primary archetype이 바뀌는 것을 허용한다.
이것은 필요한 기능이지만 위험도 있다.

공격 질문:

```text
retry claim 하나가 우연히 다른 archetype primitive에 매핑됐을 때
primary archetype을 너무 쉽게 바꾸는가?
source task satisfaction / accepted primitive / source quorum이 충분한가?
```

다음 패치 방향:

```text
retry primary 갱신 조건을 source task satisfaction + accepted claim + mapping status + contract compatibility로 감사한다.
```

### 7.3 drop count와 good retry count의 비율

v38은 dropped retry count를 readiness에 노출했다.
v39는 good retry acceptance를 테스트했다.

공격 질문:

```text
실제 output에서는 source_lineage_feedback_retry_dropped_count만 있고
source_lineage_feedback_retry_accepted_count는 없는가?
있다면 readiness가 편향된 상태를 숨기지 않는가?
```

다음 패치 방향:

```text
readiness audit에 source_lineage_feedback_retry_executed_count,
source_lineage_feedback_retry_accepted_count,
source_lineage_feedback_retry_no_evidence_count를 추가한다.
```

### 7.4 FULL_THESIS 승격까지의 끊김

v39는 accepted claim까지만 확인한다.

공격 질문:

```text
accepted claim이 생겼는데 score contribution과 StageCourt에 연결되지 않는 row가 있는가?
accepted claim은 있지만 representative row가 아니어서 점수에 안 들어가는 경우가 설명되는가?
```

다음 패치 방향:

```text
source-lineage good retry accepted claim이
score_contributions.jsonl, primitive_states.jsonl, atomic_stage_decisions.jsonl까지 이어지는
leaf-chain 테스트를 추가한다.
```

### 7.5 live daily에서 unbounded fallback 재발 여부

v39는 bounded config로 실행된다.

공격 질문:

```text
source-lineage feedback retry가 live daily에서 무제한 web fetch를 다시 열지 않는가?
retry_max, max_queries, max_candidates, max_fetches가 유지되는가?
```

다음 패치 방향:

```text
feedback retry task도 original task와 동일하게 budget leaf를 남기고,
production daily preset에서 unbounded retry config를 static audit한다.
```

## 8. 최종 판단

v39 기준으로 방향은 맞다.

확실히 좋아진 점:

```text
나쁜 source-lineage retry는 실행하지 않고 감사에 남긴다.
좋은 source-lineage retry는 막지 않고 accepted claim까지 갈 수 있다.
그 차이가 테스트로 고정됐다.
```

아직 완료가 아닌 점:

```text
canonical FULL_THESIS 운영 Stage row는 아직 0이다.
FULL_E2R_100 verified score row도 아직 0이다.
v39는 production complete가 아니라 source retry acceptance chain 회귀 보강이다.
```

다음 최우선 방향:

```text
source-lineage good retry accepted claim
-> score contribution
-> primitive state
-> StageCourt
-> promoted FULL_THESIS row
```

이 전체 leaf chain을 실제 connector 또는 frozen live snapshot으로 검증해야 한다.
