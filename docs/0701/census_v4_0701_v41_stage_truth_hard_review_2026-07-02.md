# Census v4 0701 v41 Stage Truth Hard Review

작성일: 2026-07-02 KST

## 0. 결론

질문:

```text
뭔가 잘못되고 있는 거 맞지?
Stage가 있는 애들이 있긴 해?
```

현재 산출물 기준 답:

```text
Stage처럼 보이는 행은 있다.
하지만 운영에 쓸 FULL_THESIS Stage 행은 없다.
```

정확히 나누면:

```text
CENSUS_EVENT_BOARD Stage:
  있음
  전 종목/후보의 현재 상태판이다.
  예: 공식 이벤트가 하나 있어서 Stage1 watch로 표시.

FULL_THESIS operating Stage:
  없음
  아키타입별 Evidence OS가 claim -> primitive -> score -> StageCourt까지 닫은 운영 Stage다.
  현재 row 수 0.

FULL_E2R_100 verified score:
  없음
  운영 점수 100점 scale로 확정된 row 수 0.
```

쉬운 예:

```text
SK하이닉스 행에 Stage1이 보일 수 있다.
하지만 그건 "DART 공식 이벤트가 있으니 상태판에서 watch"라는 뜻이다.
"C06 HBM thesis를 FULL_THESIS로 돌려서 87점 Yellow/Green"이라는 뜻이 아니다.
```

따라서 UI나 리포트가 이 둘을 섞어 보여 주면 잘못된 것이다.

## 1. 확인한 산출물

확인 대상:

```text
docs/operational/census_mode_v4_readiness_verdict.md.json
docs/operational/census_mode_v4_sample_leaf_bundle.jsonl
docs/operational/census_mode_v4_full_thesis_production_audit.json
docs/operational/census_mode_v4_full_thesis_production_runner_audit.json
docs/operational/census_mode_v4_brain_web_readiness_gate_audit.json
docs/operational/census_mode_v4_stage_signal_audit.json
docs/operational/census_mode_v4_score_scale_audit.json
```

주의:

```text
현재 docs/operational artifact는 v40 readiness-count 패치 전 생성물로 보인다.
그래서 operational artifact 자체에는 v40 신규 count가 아직 보이지 않는다.
v40 신규 count는 단위/관련/전체 테스트로 검증했다.
```

## 2. 교차검증 결과

### 2.1 readiness verdict

명령:

```bash
python - <<'PY'
import json
from pathlib import Path
p=Path('docs/operational/census_mode_v4_readiness_verdict.md.json')
data=json.loads(p.read_text())
for key in ['stage_scope_notice','brain_web_readiness_gate']:
    print(key, data.get(key))
PY
```

결과 요약:

```text
stage_scope_notice =
  NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST

brain_web_readiness_gate.verdict =
  NOT_REQUESTED

brain_web_readiness_gate.source_task_execution_count =
  0

brain_web_readiness_gate.web_or_llm_accepted_claim_count =
  0
```

해석:

```text
상태판 Stage row는 있지만 FULL_THESIS row는 없다는 것을 artifact가 직접 말한다.
Brain/Web 운영 증거 수집 gate도 이 산출물에서는 실행 요청 자체가 없다.
```

### 2.2 sample leaf bundle

명령:

```bash
python - <<'PY'
import json
from collections import Counter
from pathlib import Path
p=Path('docs/operational/census_mode_v4_sample_leaf_bundle.jsonl')
rows=[json.loads(line) for line in p.read_text().splitlines() if line.strip()]
print('rows', len(rows))
print('stage_scope', dict(Counter(str(r.get('stage_scope')) for r in rows if 'stage_scope' in r)))
print('score_scale', dict(Counter(str(r.get('score_scale')) for r in rows if 'score_scale' in r)))
print('operator_stage_use', dict(Counter(str(r.get('operator_stage_use')) for r in rows if 'operator_stage_use' in r)))
PY
```

결과:

```text
rows 67
stage_scope {'CENSUS_EVENT_BOARD': 67}
score_scale {'EVENT_WEIGHTED_PARTIAL': 67}
operator_stage_use {'NOT_FULL_THESIS_STAGE': 67}
```

해석:

```text
67개 샘플 leaf row 전부 상태판 Stage다.
운영 Stage로 써도 되는 row는 0개다.
```

### 2.3 FULL_THESIS marker 검색

명령:

```bash
rg -n '"stage_scope": "FULL_THESIS"|"operator_stage_use": "FULL_THESIS_STAGE"|"score_scale": "FULL_E2R_100"|"is_full_thesis_stage": true|"is_full_e2r_score": true' \
  docs/operational/census_mode_v4_*.json \
  docs/operational/census_mode_v4_*.jsonl
```

결과:

```text
match 없음
```

해석:

```text
현재 v4 operational artifact 묶음 안에서 FULL_THESIS/FULL_E2R marker는 발견되지 않았다.
```

### 2.4 FULL_THESIS production audit

확인 결과:

```text
docs/operational/census_mode_v4_full_thesis_production_audit.json
  status  = PENDING_FULL_THESIS_PRODUCTION
  verdict = PENDING_FULL_THESIS_PRODUCTION

docs/operational/census_mode_v4_full_thesis_production_runner_audit.json
  verdict = NOT_REQUESTED
  promoted_full_thesis_row_count = 0
  candidate_row_count = 0
  blocked_candidate_count = 0
```

해석:

```text
production FULL_THESIS runner가 이 산출물에서는 실제 승격을 만들지 않았다.
```

### 2.5 stage/score audit

확인 결과:

```text
docs/operational/census_mode_v4_stage_signal_audit.json
  verdict = PASS

docs/operational/census_mode_v4_score_scale_audit.json
  verdict = PASS
```

이 PASS의 의미:

```text
상태판 Stage와 score scale의 표기 분리는 통과했다.
하지만 FULL_THESIS 운영 Stage가 존재한다는 뜻은 아니다.
```

## 3. 왜 헷갈렸나

현재 row에는 이런 필드가 같이 들어 있다.

```text
base_stage = Stage1 또는 Stage2-Watch
canonical_stage = 1 또는 2
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
score_scale = EVENT_WEIGHTED_PARTIAL
full_thesis_stage = FULL_THESIS_NOT_RUN
full_e2r_verified_score = null
```

사람이 앞의 `Stage1`, `Stage2-Watch`만 보면 Stage가 있다고 느낀다.

하지만 뒤의 필드가 실제 의미를 제한한다.

```text
stage_scope = CENSUS_EVENT_BOARD
```

는 "전체지도 상태판"이다.

```text
operator_stage_use = NOT_FULL_THESIS_STAGE
```

는 "운영 Stage로 쓰지 말라"는 표시다.

```text
full_thesis_stage = FULL_THESIS_NOT_RUN
```

는 "아직 진짜 thesis 평가를 돌리지 않았다"는 표시다.

쉬운 예:

```text
건강검진 접수표에 "혈압 재검"이라고 적힌 것과
심장 전문의가 정밀검사 후 "수술 필요"라고 판정한 것은 다르다.

CENSUS_EVENT_BOARD Stage는 접수표에 가깝다.
FULL_THESIS Stage는 정밀 판정에 가깝다.
```

## 4. 현재 구조가 맞는 부분

좋은 점:

```text
1. CensusAssessmentEvent가 score evidence로 들어가지 않는다.
2. 상태판 Stage와 운영 Stage를 stage_scope로 분리하려고 한다.
3. EVENT_WEIGHTED_PARTIAL과 FULL_E2R_100을 score_scale로 분리하려고 한다.
4. operator_stage_use = NOT_FULL_THESIS_STAGE가 있어 운영 오용을 막으려 한다.
5. FULL_THESIS_NOT_RUN을 명시해서 "아직 정밀 thesis 미실행"을 숨기지 않는다.
```

이 방향은 맞다.

전 종목 Census에서 모든 종목에 억지 점수를 주면 안 된다.

올바른 흐름:

```text
전 종목에 CensusAssessmentEvent 부여
-> 실제 CandidateEvent가 있는지 확인
-> source-backed claim이 있으면 상태판 Stage 부여
-> FULL_THESIS refresh 대상이면 별도 정밀 평가
-> claim/primitive/score/StageCourt가 닫힐 때만 운영 Stage 부여
```

## 5. 현재 구조가 부족한 부분

문제:

```text
상태판 Stage는 있는데 FULL_THESIS 운영 Stage로 이어지는 leaf chain이 아직 닫히지 않았다.
```

필요한 실제 chain:

```text
source task execution
-> EvidenceDocument
-> EvidenceAnchor
-> accepted EvidenceClaim
-> PrimitiveState
-> ScoreContribution
-> StageCourt trace
-> census_stage_status row with stage_scope=FULL_THESIS
-> score_scale=FULL_E2R_100
-> operator_stage_use=FULL_THESIS_STAGE
```

현재 확인된 chain:

```text
official event / partial claim
-> CENSUS_EVENT_BOARD row
-> EVENT_WEIGHTED_PARTIAL
-> NOT_FULL_THESIS_STAGE
```

즉 지금은 "지도에 핀을 꽂는 단계"까지는 있다.
하지만 "핀을 꽂은 종목을 실제 운영 thesis로 정밀 채점하는 단계"는 아직 0개다.

## 6. v40 패치와 이 문서의 관계

v40 패치가 한 일:

```text
source-lineage feedback retry 결과를 readiness에 분리 count로 노출
```

새 count:

```text
source_lineage_feedback_retry_execution_count
source_lineage_feedback_retry_accepted_execution_count
source_lineage_feedback_retry_no_evidence_execution_count
source_lineage_feedback_retry_dropped_count
discovery_only_retry_after_unverified_original_count
```

왜 중요한가:

```text
LLM retry가 원문 미검증 문제를 실제로 복구했는지,
아니면 또 discovery-only로 헛돌았는지,
readiness에서 숫자로 분리해서 봐야 하기 때문이다.
```

하지만 v40도 아직 FULL_THESIS를 만들지는 않는다.

v40은 이런 질문에 답한다.

```text
LLM source-lineage retry가 accepted claim까지 갈 수 있는가?
그 결과가 readiness에 숨지 않고 보이는가?
```

v40은 아직 이런 질문에는 답하지 못한다.

```text
accepted retry claim이 FULL_THESIS Stage row까지 이어지는가?
```

## 7. 다음 패치 방향

다음 에이전트가 공격해야 할 순서:

```text
1. operational artifact를 v40 이후 코드로 재생성한다.
2. brain_web_readiness_gate_audit.json에 v40 신규 count가 실제로 쓰이는지 확인한다.
3. source_lineage_feedback_retry_accepted_execution_count > 0인 사례를 만든다.
4. 그 accepted claim id가 accepted_claims artifact에 존재하는지 확인한다.
5. 같은 claim id가 ScoreContribution support_claim_ids로 이어지는지 확인한다.
6. 해당 contribution이 PrimitiveState와 StageCourt trace까지 이어지는지 확인한다.
7. 마지막으로 census_stage_status row가 stage_scope=FULL_THESIS로 생성되는지 확인한다.
```

완료 기준:

```text
source-lineage retry accepted claim
-> score contribution
-> primitive state
-> StageCourt trace
-> FULL_THESIS row
```

이 chain을 fixture가 아니라 실제 connector 또는 frozen live snapshot으로 닫아야 한다.

## 8. 다음 리뷰어가 바로 찔러야 할 질문

```text
1. 지금 Stage1/Stage2-Watch row를 운영 Stage라고 표시하는 UI/리포트가 있는가?
2. FULL_THESIS_NOT_RUN인데도 score/stage를 투자 판단용처럼 출력하는 경로가 있는가?
3. EVENT_WEIGHTED_PARTIAL 점수를 FULL_E2R_100처럼 정규화해 보여 주는 경로가 있는가?
4. v40 신규 readiness count가 실제 operational artifact에 생성되는가?
5. Brain/Web gate가 NOT_REQUESTED인 상태를 READY처럼 표시하는 경로가 있는가?
6. source-lineage retry accepted claim이 score contribution으로 이어지지 못해도 PASS가 되는가?
7. sample bundle 67개가 모두 상태판인데 README나 report가 "Stage 있는 종목 67개"처럼 오해시키는가?
```

## 9. 검증 명령 기록

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v > /tmp/census_v40_full_unittest.log 2>&1
```

결과:

```text
Ran 5072 tests in 222.590s
OK
```

형식 검사:

```bash
git diff --check -- src/e2r/census/census_runner_v4.py tests/test_census_v4_brain_web_readiness_gate.py docs/0701/README.md docs/0701/census_v4_0701_v40_source_lineage_retry_outcome_readiness_counts_2026-07-02.md
```

결과:

```text
출력 없음, exit 0
```

후행 공백 검사:

```bash
rg -n "[ \t]$" \
  docs/0701/census_v4_0701_v40_source_lineage_retry_outcome_readiness_counts_2026-07-02.md \
  docs/0701/README.md \
  src/e2r/census/census_runner_v4.py \
  tests/test_census_v4_brain_web_readiness_gate.py
```

결과:

```text
match 없음
```

## 10. 최종 판단

현재 시스템은 완전히 망가진 상태라기보다, 두 층이 섞이면 위험한 중간 상태다.

맞는 층:

```text
Census 상태판은 존재한다.
source-backed partial event를 Stage1/Stage2-Watch로 표시할 수 있다.
```

아직 없는 층:

```text
FULL_THESIS 운영 Stage는 없다.
FULL_E2R_100 운영 점수도 없다.
```

따라서 다음 구현 목표는 점수표를 다시 만지는 것이 아니다.

목표:

```text
상태판 Stage를 운영 Stage처럼 보이지 않게 계속 막고,
accepted claim이 FULL_THESIS leaf chain 끝까지 닫히는 실제 경로를 만든다.
```

