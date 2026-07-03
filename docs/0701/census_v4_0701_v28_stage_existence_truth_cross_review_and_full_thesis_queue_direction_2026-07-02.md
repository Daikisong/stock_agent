# Census v4 0701 v28 Stage Existence Truth Cross Review

작성일: 2026-07-02 KST

기준 산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v28
```

## 0. 결론

질문에 대한 답은 둘로 나눠야 한다.

```text
Stage가 있는 애들이 있나?
  있다. 전 종목 3,391개에 CENSUS_EVENT_BOARD 상태판 Stage가 붙어 있다.

운영에서 써도 되는 FULL_THESIS 점수/Stage가 있나?
  없다. 0개다.
```

현재 `Stage1`, `Stage2-Watch`, `Red`가 보이는 것은 사실이다. 하지만 이 Stage는 전부:

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
```

이다.

쉬운 예:

```text
병원 접수표에는 "진료 필요", "검사 필요" 같은 상태가 찍혀 있다.
하지만 의사가 진단서를 발급한 것은 아니다.

CENSUS_EVENT_BOARD Stage = 접수표 상태
FULL_THESIS Stage = 진단서
```

따라서 지금 결과를 이렇게 말하면 틀린다.

```text
삼성전자 Stage1이니까 운영 Stage1이다.
```

정확한 말은 이것이다.

```text
삼성전자는 Census 상태판에서 Stage1로 표시됐지만,
FULL_THESIS refresh는 아직 실행되지 않았고,
운영용 verified score/Stage는 없다.
```

## 1. Stage 존재 교차검증

`census_stage_summary.json` 기준:

```text
event_board_stage_row_count = 3391
event_board_non_stage0_count = 85

base_stage_distribution:
  Stage0       = 3306
  Stage1       = 54
  Stage2-Watch = 30
  Red          = 1

canonical_stage_distribution:
  0     = 3306
  1     = 54
  2     = 30
  3-Red = 1
```

즉 Stage 라벨 자체는 있다.

하지만 같은 파일이 동시에 이렇게 말한다.

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN = 3391

full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
verified_score_present_count = 0
```

이게 핵심이다.

```text
상태판 Stage는 3,391개.
운영 FULL_THESIS Stage는 0개.
```

## 2. 비 Stage0 85개도 운영 Stage가 아니다

`census_stage_status.jsonl`에서 `base_stage != Stage0`인 행은 85개다.

분포:

```text
Stage1       = 54
Stage2-Watch = 30
Red          = 1
```

하지만 이 85개 전부가:

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_not_run = true
full_thesis_score_valid_status = NOT_SCORED
full_thesis_primary_archetype = None
full_thesis_missing_primitives = full_thesis_refresh_task_not_run
```

상태다.

쉬운 예:

```text
DART 공시가 있어서 "뭔가 볼 게 있다"는 표시는 붙었다.
하지만 아직 아키타입별 논리, 점수 primitive, Green gate, score contribution까지 닫은 것은 아니다.
```

샘플:

```text
000660 SK하이닉스:
  base_stage = Stage1
  accepted_official_claim_count = 1
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_thesis_verified_score = None

005930 삼성전자:
  base_stage = Stage1
  accepted_official_claim_count = 1
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_thesis_verified_score = None

001470 삼부토건:
  base_stage = Stage2-Watch
  accepted_official_claim_count = 1
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_thesis_verified_score = None
```

따라서 "Stage가 있는 애들이 있긴 하다"는 말은 맞지만, "운영 Stage가 완성됐다"는 말은 틀리다.

## 3. FULL_THESIS production runner 교차검증

`full_thesis_production_runner_audit.json` 기준:

```text
verdict = PENDING_PRODUCTION_FULL_THESIS
candidate_row_count = 1
blocked_candidate_count = 1
promoted_full_thesis_row_count = 0
promoted_symbols = []
```

유일한 FULL_THESIS 후보:

```text
symbol = 114450
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP

present_primitives:
  contract_amount_to_prior_sales
  contract_duration_months
  delivery_schedule

missing_green_primitives:
  margin_bridge_visible

blocker:
  missing_green_gate_primitives
```

쉬운 예:

```text
계약 금액, 계약 기간, 납품 일정은 닫혔다.
하지만 "이 계약이 마진 개선으로 이어지는가"는 아직 닫히지 않았다.

C05에서 마진 bridge가 없으면 FULL_THESIS로 승격하면 안 된다.
```

따라서 114450도 운영 Stage로 올리지 않는 것이 맞다.

## 4. Brain/Web 경로 교차검증

`brain_stage_promotion_audit.json` 기준:

```text
verdict = BLOCKED
real_provider_success_count = 3
source_task_execution_count = 23
official_accepted_claim_count = 48
web_or_llm_accepted_claim_count = 0
llm_extracted_accepted_claim_count = 0
web_news_accepted_claim_count = 0
brain_promoted_stage_row_count = 0
unsafe_promoted_stage_row_count = 0
```

blockers:

```text
web/LLM accepted brain claim count is zero for BRAIN_WEB_PARTIAL promotion
brain StageCourt traces have no web/LLM accepted claim support: 1
```

해석:

```text
공식 OpenDART claim은 48개 닫혔다.
하지만 Brain/Web이 찾아서 LLM evidence path로 accepted 된 claim은 0개다.
```

쉬운 예:

```text
DART 공시는 접수했고 일부 claim도 닫혔다.
하지만 "웹/리포트/IR을 LLM이 읽고 점수칸에 들어갈 증거를 만든 경로"는 아직 0이다.
```

여기서 공식 claim 48개를 web/LLM claim처럼 세면 다시 거짓 진척이 된다.

## 5. 왜 아직 잘못되고 있다고 봐야 하나

현재 guard가 false positive를 막는 것은 맞다.

```text
Tistory/블로그/급등종목 정리 글을 점수 source로 인정하지 않는다.
FULL_THESIS primitive가 안 닫히면 승격하지 않는다.
web/LLM accepted claim이 0이면 Brain/Web ready로 표시하지 않는다.
```

하지만 운영 목표 기준으로는 아직 잘못되고 있는 부분도 분명하다.

```text
1. 비 Stage0 85개가 전부 full_thesis_refresh_task_not_run이다.
2. FULL_THESIS runner는 유일 후보 1개만 심사했다.
3. 그 1개도 margin_bridge_visible 부족으로 막혔다.
4. Brain/Web은 retry loop는 돌지만 accepted claim을 아직 만들지 못한다.
5. web fetch는 아직 Tistory/블로그/시황성 문서로 새는 비중이 크다.
```

쉬운 예:

```text
현재 시스템은 "허술한 자료로 점수 주지 않는 브레이크"는 생겼다.
하지만 "좋은 자료를 찾아서 실제 진단서까지 발급하는 엔진"은 아직 약하다.
```

즉 지금 상태는:

```text
과거처럼 아무 자료나 점수로 넣는 문제는 막는 중.
하지만 실제 운영 Stage를 충분히 만들어내는 능력은 아직 부족.
```

## 6. 다음 패치 방향

다음 패치는 점수 gate를 느슨하게 하는 것이 아니다.

### P0-H. FULL_THESIS refresh queue

문제:

```text
비 Stage0 85개가 전부 full_thesis_refresh_task_not_run이다.
```

해야 할 일:

```text
CENSUS_EVENT_BOARD 비 Stage0 행
-> material candidate만 bounded queue에 넣기
-> 아키타입 hypothesis와 missing primitive 생성
-> official-first source task 실행
-> accepted claim / score contribution / StageCourt trace가 닫힌 경우만 FULL_THESIS 후보로 승격
```

주의:

```text
Stage1/Stage2-Watch를 그대로 FULL_THESIS로 복사하면 안 된다.
queue에 올리는 것과 점수/Stage 확정은 다르다.
```

쉬운 예:

```text
나쁜 패치:
  삼성전자가 Stage1로 보이니 운영 Stage1로 출력.

좋은 패치:
  삼성전자를 FULL_THESIS refresh queue에 올림.
  C06/Cxx 가설을 세우고, 필수 primitive를 source-backed claim으로 닫은 뒤에만 운영 Stage 출력.
```

### P0-G. Source route quality

문제:

```text
retry는 더 돌지만 source가 Tistory/블로그/급등종목 정리 글로 새면 accepted claim은 0이다.
```

해야 할 일:

```text
1. Tistory/블로그/텔레그램/급등종목/시황 모음은 더 빨리 reject
2. DART detail / KIND / 회사 IR / company newsroom / public report PDF / 신뢰 뉴스 원문을 우선 route
3. Naver result가 공식/리포트 원문이면 resolver로 승격
4. 일반 웹 provider 문서를 score source로 직접 허용하지 않음
5. post-extraction rejection을 다음 retry prompt에 계속 반영
```

쉬운 예:

```text
나쁜 패치:
  블로그에 "마진 개선 기대"가 있으니 margin_bridge_visible 인정.

좋은 패치:
  블로그는 source failure로 기록.
  회사 IR, 공시 본문, 리포트 PDF, 신뢰 뉴스 원문에서
  마진 개선의 수치/근거/기간을 다시 찾게 함.
```

### P0-I. FULL_THESIS score validity

해야 할 일:

```text
verified_score_lower_bound / potential_score_upper_bound를 유지한다.
material gap이 Stage 경계를 바꿀 수 있으면 PENDING으로 둔다.
provider failure를 낮은 점수로 확정하지 않는다.
```

쉬운 예:

```text
검증 점수 63점, 남은 gap 최대 +1점:
  Stage 경계가 안 바뀌므로 FINAL_WITH_NONMATERIAL_GAPS 가능.

검증 점수 84점, 남은 Green primitive 최대 +8점:
  Yellow/Green 경계가 열려 있으므로 PENDING_MATERIAL_GAPS.
```

## 7. 다음 에이전트 공격 질문

다음 에이전트는 아래 질문으로 문서를 공격해야 한다.

```text
1. Stage row 3,391개를 운영 Stage로 오해하는 문구가 남아 있는가?
2. non-Stage0 85개가 모두 full_thesis_not_run임을 숨기고 있지 않은가?
3. official_accepted_claim_count 48개를 web/LLM accepted claim처럼 포장하지 않는가?
4. FULL_THESIS candidate 114450 하나가 막힌 이유를 margin_bridge_visible로 정확히 적었는가?
5. Tistory/블로그/급등종목 문서를 score source로 인정하자는 방향으로 새지 않는가?
6. P0-H queue가 Stage1/2를 그대로 운영 Stage로 복사하는 위험을 막고 있는가?
7. provider/source pending을 낮은 점수 확정으로 바꾸지 않는가?
8. full unittest 5055개 통과를 운영 ready로 과장하지 않는가?
9. leaf artifact PASS를 FULL_THESIS ready와 혼동하지 않는가?
10. 삼성전자/하이닉스 Stage1 샘플을 운영 점수 산출로 오해하지 않게 적었는가?
```

## 8. 현재 판정

```text
Artifact integrity:
  PASS

Event-board Stage existence:
  PRESENT
  rows = 3391
  non-Stage0 rows = 85

Operator-admissible FULL_THESIS Stage:
  ABSENT
  rows = 0

Verified FULL_E2R_100 score:
  ABSENT
  rows = 0

Brain/Web accepted evidence:
  ABSENT
  web_or_llm_accepted_claim_count = 0

Correct final verdict:
  NOT_READY
```

한 줄 결론:

```text
Stage처럼 보이는 것은 있다.
하지만 지금 운영에 써도 되는 점수/Stage는 아직 없다.
다음 패치는 FULL_THESIS refresh queue와 source route quality를 동시에 잡아야 한다.
```
