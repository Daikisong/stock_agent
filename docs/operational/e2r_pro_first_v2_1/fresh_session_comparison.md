# E2R Pro-first V2.1 fresh-session 최종 비교

## 최종 판정

```text
verifier-ready pipeline             PASS
C06 fresh initial                   PASS
C17 fresh initial                   PASS
C28 fresh initial                   PASS
multi-archetype fresh session       PASS
operational research readiness      WITHHELD_FULL_THESIS_PENDING
```

이 문서가 확정하는 범위는 **서로 다른 세 아키타입의 새 Pro 대화에서 초기 조사 효율 검문을 통과했다**는
것이다. 세 실행 모두 점수·Stage 권한은 없고 publication은 withheld다. 따라서 이 결과를 “세 종목의 최종
점수와 Stage까지 산출 완료”라고 해석하면 안 된다.

쉬운 예로, 시험 답안 81칸을 모두 채우고 출처가 붙은 핵심 답안 34개를 검문에 통과시킨 상태다. 하지만
남은 공개자료/parser gap 41개를 종결하고 deterministic scorer에 넘기는 기말 채점까지 끝난 상태는 아니다.

## 실제 새 대화 결과

| 아키타입 | 종목 | initial 후보 | 통과 | 비율 | 질문 coverage | 검증 fact | Pro 수리 pass | 판정 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| C06 | SK하이닉스 | 18 | 16 | 88.8889% | 28/28 | 21 | 0 | PASS |
| C17 | 롯데케미칼 | 8 | 8 | 100% | 26/26 | 18 | 0 | PASS |
| C28 | 안랩 | 10 | 10 | 100% | 27/27 | 17 | 0 | PASS |
| 합계 | 3개 독립 대화 | 36 | 34 | 94.4444% | 81/81 | 56 | 0 | PASS |

각 실행은 다른 `fresh_session_id`, job, run, pass, conversation을 쓴다. 모두 submit/capture `1/1`, 자동
재전송 `0`, query/search `0/0`이다. 실제 공개 source fetch는 각각 16, 8, 9로 합계 33이다.

C28 R3는 ChatGPT 결과 카드에서 새 JSON을 실제 다운로드해 `parser_source=DOWNLOADED_JSON`으로
import했다. 화면에 보였던 JSON이 바로 이 산출물이다. MD는 사람이 읽는 보조 보고서일 뿐이므로 JSON이
정상 연결된 뒤 MD를 다시 내려받을 필요가 없다. 선택 PDF는 요청하지 않아 `null`이고, 이 또한 정상이다.

## 동결 구 실행과 fresh 실행 비교

| 항목 | 동결 구 실행 | fresh 3개 실행 |
| --- | ---: | ---: |
| 아키타입 수 | 1 | 3 |
| 독립 conversation | 1개를 반복 사용 | 3 |
| initial material 후보/통과 | 구 pipeline 미보존 | 36/34 |
| verifier acceptance ratio | 계산 불가 | 94.4444% |
| initial prompt defect rejection | 50 | 0 |
| local/verifier defect rejection | 24 | 0 |
| genuine semantic repair 후보 | 0 | 3 |
| Pro repair submit | 10 | 0 |
| 전체 Pro pass | 11 | 3 |
| 전체 prompt 문자 | 11 pass 합계 미보존, initial 141,982 | 179,064 |
| 전체 output 문자 | 11 pass 합계 미보존, initial 136,604 | 272,253 |
| 경과시간 | durable 102,273.792271초 | initial research 합계 14,910.411287초 |
| 최종 검증 fact | 53 | 56 |
| 질문 row coverage | 28/28 | 81/81 |
| terminal closure | 미증명 | 미증명, gap 41 |
| 점수/Stage 권한 | false/false | false/false |

구 실행은 initial candidate/accepted 경계를 저장하지 않았으므로 그 비율을 나중에 추정하지 않았다. 또한
11 pass 전체 prompt/output 문자 수도 영속화되지 않아 initial 수치와 telemetry 공백을 그대로 표시했다.

C06의 `initial_research_elapsed_seconds=7566.1444`는 앞선 durable browser 연구 구간을 포함하지만,
`total_elapsed_seconds=94.565768`은 재개된 capture recovery 프로세스만 센다. 서로 다른 시계 범위이므로 두
값을 같은 의미로 비교하지 않는다. 이 차이를 숨기지 않고 comparison JSON에 함께 기록했다.

## P9 독립 감사

다음 명령은 comparison JSON의 합계를 믿지 않고 C06·C17·C28 성공 영수증, old freeze 영수증, rejection
taxonomy를 직접 다시 읽는다.

```bash
PYTHONPATH=src python -m e2r.cli.audit_e2r_pro_first_v2_1_fresh_efficiency \
  --repo-root . \
  --output /tmp/e2r_pro_v2_1_fresh_efficiency_audit.json
```

현재 재계산 결과는 다음과 같다.

```text
status             PASS
critical_count     0
fresh archetypes   3
accepted/candidate 34/36
verified facts     56
mandatory coverage 81/81
audit hash         47d96d1f3b602ef0b963ce3772ffc70cbacdb655fb399aefdcf0a61fb9b87b6a
comparison hash    b1778795d32c4b434ac9537c430d4b24898e7e36a518367ae83615c0ed5c8e01
```

감사기는 아래 13개 카운터가 모두 0인지 검사한다.

```text
old_conversation_new_submit_count
old_fact_in_fresh_packet_count
old_score_stage_in_fresh_packet_count
local_normalizable_sent_to_pro_count
source_representation_sent_to_pro_count
full_dossier_repair_response_required_count
multi_source_atomic_fact_count
derived_metric_mixed_fact_count
tracking_url_fact_count
question_unbound_material_fact_count
repair_deferred_batch_count
second_repair_pass_count
partial_score_published_count
```

예를 들어 comparison JSON만 `36/36`으로 고쳐도 개별 영수증 합은 `34/36`이므로 CI가 실패한다. C28
영수증에서 `partial_score_published_count`를 1로 바꾸거나 동결 구 job의 새 submit을 1로 바꿔도 실패하는
회귀 테스트를 넣었다. GitHub Actions의 Pro-first static-security job도 같은 CLI를 매번 실행한다.

## 비교 금지와 다음 경계

구 C06 실행과 fresh C06/C17/C28 실행은 source corpus와 아키타입 구성이 다르다. 따라서 점수 parity,
점수 향상률, 같은 thesis 품질이라는 주장은 금지한다.

현재 확정된 것은 **fresh-session 초기 효율과 다중 아키타입 일반화**다. 운영 연구 준비 완료를 선언하려면
각 live canary의 남은 public/parser gap을 종결하고 source-backed component 7/7, Judge 21/21,
deterministic score/Stage와 publication gate를 별도 영수증으로 증명해야 한다.

## 최종 로컬 검증

```text
P9 fresh efficiency audit                  PASS / critical 0
focused P9 audit tests                              5/5 PASS
Linux headless browser tests                       79/79 PASS
전체 unittest                                     7,712 PASS
failure / error / skipped                       0 / 0 / 38
Phase100                                           15/15 PASS
Gate 1 tracked receipt                               4/4 PASS
Pro-first static audit                     PASS / critical 0
Pro-first V2 static audit                  PASS / critical 0
E2R v6 production static audit             PASS / critical 0
compileall / git diff check                       PASS / PASS
```

첫 전체 실행에서 브라우저 60개가 `libnspr4.so`를 찾지 못해 ERROR가 났다. 이는 코드 assertion 실패가
아니라 Playwright 공유 라이브러리 경로 누락이었다. 실제 dependency 경로를 연결해 브라우저 모듈 79개를
먼저 모두 통과시킨 뒤, 전체 7,712개를 처음부터 다시 실행해 failure/error 0을 확인했다. 환경 오류 실행은
최종 수치에 합산하지 않았다.
