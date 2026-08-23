# Pro-first V2 root cause와 통합 지도

## 현재 판정

기존 `000660` 실행은 브라우저 전송부터 MD capture, import, 검증, component,
Judge, deterministic score, StageCourt까지 한 번 연결됐다는 증거다. 그러나 선택된
아키타입의 필수 질문이 전부 종결됐다는 증거는 아니다.

따라서 기존 JSON은 삭제하거나 바꾸지 않고 다음처럼 의미만 새 receipt와 view에서
교정한다.

```text
PRO_FIRST_END_TO_END_TRANSPORT_CANARY_PASS
FIRST_PASS_PARTIAL_CORPUS_DIAGNOSTIC_ONLY
NOT_A_FULL_THESIS_OPERATIONAL_SCORE

first_pass_diagnostic_score = 23.202275
first_pass_diagnostic_stage = 0
full_thesis_score = null
full_thesis_stage = null
full_thesis_score_valid = false
publication_status = WITHHELD_PENDING_RESEARCH_SATURATION
```

쉬운 예로, 100문항 시험에서 답안지 전송·채점기 연결을 확인한 것과 100문항을 모두
푼 것은 다르다. 기존 canary는 앞의 연결을 증명했지만, 13개 미확인 문항을 남긴 채
뒤의 완료까지 주장했다.

## 1. `COMPLETE`를 강제한 위치

- `configs/e2r_pro_research_prompt_v1.md`는 `research_status`를 반드시
  `COMPLETE`로 쓰라고 지시한다.
- `configs/e2r_pro_research_dossier_v1.schema.json`도 `research_status`를
  `const: COMPLETE`로 제한한다.
- 따라서 Pro가 13개 `unresolved_gaps`를 함께 반환해도 스키마상 상태는 항상
  `COMPLETE`다. 이것은 transport 완료와 research saturation을 혼동한다.

V2 통합 위치는 `ResearchDossierV2.research_status`와 question별 terminal 상태다.
`COMPLETE` 문자열 하나가 아니라 mandatory question roster 전체를 deterministic
saturation engine이 검사해야 한다.

## 2. 질문 계약이 C06에만 있던 범위

`configs/e2r_question_impact_contracts_v1.json`의 모든 row는
`C06_HBM_MEMORY_CUSTOMER_CAPACITY`다. HBM allocation, qualification, ASP,
FCF, valuation 같은 C06 질문은 자세하지만 C01~C05, C07~C32와 R13 guard 네 개의
동등한 질문 계약은 없다.

V2는 `configs/e2r_archetype_research_contracts_v2.json`을 source of truth로 두고
`C01~C32 + R13 4개 = 36개`를 정확히 맞춘다. canonical roster가 늘어나면 contract가
추가되지 않는 한 totality audit가 실패한다.

## 3. one-pass 뒤 바로 scoring으로 간 전이

현재 실제 경로는 다음과 같다.

```text
RESULT_DETECTED
→ CAPTURING_ARTIFACTS
→ CAPTURE_COMPLETE
→ IMPORTING
→ DOSSIER_IMPORTED
→ VERIFYING_SOURCES
→ GAP_ADJUDICATION
→ (supplemental task가 0이면) COMPONENT_RESEARCH
→ JUDGING → SCORING → STAGECOURT → FINAL → PUBLISH
```

`src/e2r/pro_first/post_import.py`의 `advance_once()`는 gap service가
`COMPONENT_RESEARCH`를 반환하면 같은 normalized V1 dossier를 즉시 scoring input으로
넘긴다. `QUESTION_CLOSURE_AUDIT`, `PUBLIC_GAP_CLOSURE`,
`COUNTER_SUPERSESSION_CLOSURE`, `VERIFIER_REPAIR`, `SATURATION_AUDIT` 전이가 없다.

V2는 initial pass 뒤 같은 ChatGPT conversation에서 위 pass들을 수행하고
`FULL_THESIS_READY` receipt가 있을 때만 component 진입을 허용한다.

## 4. component fact count가 adequacy로 오용된 위치

`src/e2r/pro_first/gaps/adjudicator.py`는 검증된 fact를 component별로 세고,
affected component 전부에 fact가 하나 이상 있으면 `range_bounded`로 본다. 이 값은
`EvidenceGapAssessment.from_authority_inputs()`로 전달되어 source role과 gap class를
낮추는 재료가 된다.

예를 들어 EPS component에 회사 소개 fact 하나가 있어도 실제 질문인 “현금흐름표로
FCF 전환이 확인됐는가”에는 답하지 못한다. V2 adequacy 단위는 fact 개수가 아니라
`question + source role + economic bridge + counter/lifecycle + materiality`다.

## 5. 13개 gap이 모두 `CORROBORATION_CAP`이 된 call path

실제 `000660` V1 receipt에는 다음이 함께 존재한다.

```text
compiled evidence facts 26
unresolved gaps 13
CORROBORATION_CAP 13
CORE_SCORE_BLOCKER 0
supplemental tasks 0
```

호출 경로는 다음과 같다.

```text
Pro V1 unresolved_gaps
→ compile_conservative_gap_contexts()
→ ProGapAdjudicator.adjudicate()
→ component별 source-backed fact count
→ range_bounded=true
→ EvidenceGapAssessment
→ CORROBORATION_CAP
→ supplemental_allowed=false
→ SupplementalPlanner task 0
→ COMPONENT_RESEARCH
```

V2에서는 primary score source가 실제 mandatory question을 지지하고, 남은 route가
독립 corroboration뿐이며, 공개 가능한 새 predicate가 없고, hard-break polarity를
바꿀 수 없고, adequate-search fixpoint까지 확인된 경우에만 이 cap을 허용한다.

## 6. verifier rejection 뒤 repair가 없는 위치

`ProSourceVerificationService`는 quote/date/subject/segment/currentness 검문 결과를
durable receipt로 남긴다. 그러나 현재 `post_import.py`는 검증 완료 뒤 곧바로 gap
adjudication으로 이동한다. material rejection을 Pro에게 돌려보내
`correct/replace/narrow/withdraw` 중 하나를 받는 pass가 없다.

V2는 rejection을 삭제하지 않고 append-only ledger에 남긴 뒤 같은 conversation의
`VERIFIER_REPAIR` delta를 추가한다. 수정 fact도 다시 deterministic verifier를 통과해야
하며, material rejection pending이 하나라도 남으면 full thesis를 막는다.

## 7. partial score가 `FINAL/PUBLISHED`가 된 위치

- `state_machine.py`의 `STAGECOURT → FINAL` guard는 deterministic StageCourt receipt만
  요구하고 research saturation receipt는 요구하지 않는다.
- `scoring/service.py`는 Judge 21개와 기존 score validity 입력이 갖춰지면 score와
  StageCourt를 만든다.
- `publication.py`는 `FINAL`, 7 component, 21 Judge, score/Stage lineage를 검사하지만
  mandatory question closure, public material gap 0, verifier repair pending 0을 검사하지
  않는다.
- `post_import.py`는 scoring 결과가 `FINAL`이면 즉시 publisher를 호출한다.

그래서 구조적으로 정확한 deterministic 계산이 불완전한 연구 corpus 위에서 실행될 수
있었다. 계산식이 틀린 문제가 아니라 계산 자격 gate가 빠진 문제다.

## 8. 기존 scorer와 StageCourt 재사용 위치

새 점수기나 Stage enum을 만들지 않는다.

- `src/e2r/pro_first/scoring/scorer_bridge.py`가 기존
  `ResearchCalibratedComponentScorer`에 verified component assessment를 전달한다.
- `src/e2r/pro_first/scoring/stagecourt_bridge.py`가 기존
  `AtomicStageCourtV2`를 호출한다.
- canonical Stage enum은 기존 `0`, `1`, `2`, `3-Green`, `3-Yellow`, `3-Red`,
  `4A`, `4B`, `4C`, `5`를 유지한다.

V2가 추가하는 것은 scorer 앞의 `FULL_THESIS_READY` 자격 gate다. 예를 들어 계산기가
정확해도 입력 서류가 덜 모였으면 계산 버튼을 누르지 않는 방식이다.

## 9. 36개 contract를 prompt로 compile할 위치

새 경로는 다음으로 고정한다.

```text
configs/e2r_archetype_research_contracts_v2.json
→ src/e2r/pro_first/research_contracts/loader.py
→ validator.py / totality_audit.py
→ question_planner.py
→ prompt_compiler.py
→ ResearchPacketV2 contract snapshot
→ 같은 conversation의 initial/gap/counter/repair/saturation prompts
```

한 job에는 선택 후보 1~3개 primary contract와 R13 cross guard 네 개만 compile한다.
모든 36개를 한 prompt에 넣지 않는다. CI에서는 반대로 36개 prompt snapshot을 각각
compile하여 누락과 cross-archetype 질문 오염을 검사한다.

## 통합 불변식

```text
Pro는 질문·검색·fact·repair를 제안할 수 있다.
Pro는 score 또는 Stage 권한을 갖지 않는다.

mandatory question nonterminal > 0
또는 PUBLIC_SEARCHABLE material gap > 0
또는 verifier repair pending > 0
또는 core provider/parser pending > 0
→ score_valid=false
→ canonical Stage=null / RESEARCH_INCOMPLETE
→ WITHHELD_PENDING_RESEARCH_SATURATION
```

기존 V1 파일은 append-only 감사 증거로 보존한다. 새 의미는
`canary_reclassification_receipt.json`과 `readiness_view.py`가 제공한다.

## 구현 진행 장부

2026-08-23 현재 PR #7의 단계별 구현 상태는 다음과 같다. 이 표의 `완료`는 해당
phase의 코드·지정 회귀시험·한글 커밋이 branch에 존재한다는 뜻이며, 전체 V2 운영
완료를 뜻하지 않는다.

| Phase | 상태 | 현재 증거 |
| --- | --- | --- |
| P0 | 완료 | 기존 one-pass canary를 partial diagnostic으로 재분류 |
| P1 | 완료 | 36/36 contract, 233 question family, critical 0 |
| P2 | 완료 | 6종 동적 prompt template와 36 snapshot audit |
| P3 | 완료 | ResearchDossierV2, question/route/status 장부, V1 read-only 호환 |
| P4 | 완료 | 동일 conversation follow-up, 최초 승인 scope, pass별 exactly-once, parent lineage |
| P5 | 완료 | question/source-role 단위 adequacy, semantic fixpoint, cap/monitoring/core blocker 분리 |
| P6 | 완료 | 11종 verifier rejection packet, 동일 대화 repair/withdraw, deterministic re-verification |
| P7 | 완료 | saturation 선행 gate, diagnostic/full score 분리, Stage/publication withheld, 기존 scorer/StageCourt 재사용 |
| P8 | 완료 | 36 prompt snapshot, 13 mechanism golden, known-bad 30종·detector 29개 |
| P9~P10 | 미완료 | frozen MD replay/live canary와 CI·최종 receipt가 남음 |

P4의 최초 전송과 후속 전송은 브라우저 send 버튼을 두 군데서 누르지 않는다. DOM에는
기존 `submit_once()` 한 경로만 있고, 최초 pass는 기존 job의 `submit_count`, 후속
pass는 `pro_research_passes.submit_count`를 각각 DB에서 먼저 `0→1`로 원자 청구한다.

쉬운 예로 같은 채팅에서 두 번째 질문을 보내더라도 첫 질문을 다시 보낸 것으로 세지
않는다. 첫 전송 장부는 계속 1이고, 두 번째 질문은 별도 pass 장부에서 1이다. 대상,
기준일, 선택 contract 또는 conversation이 바뀌면 기존 승인을 재사용할 수 없다.

P4 leaf receipt는 `multi_pass_orchestration_audit.json`, P5 leaf receipt는
`saturation_semantics_audit.json`, P6 leaf receipt는 `verifier_repair_audit.json`, P7
leaf receipt는 `scoring_publication_gate_audit.json`이다. P7의 지정 scoring 시험
36개와 Pro-first 전체 시험 278개가 통과했고 production static audit의 critical
finding은 0이다.

P7부터 component/Judge 수가 7/7·21/21이라는 사실만으로는 게시할 수 없다. 예를 들어
C17 fixture는 component와 Judge를 모두 만들었지만 deterministic score validity가
pending이므로 기존처럼 `Stage 0`을 FINAL로 내보내지 않는다. 대신 진단 component
vector와 부분점수만 별도 보존하고 `canonical_stage=null`, `score_valid=false`,
`publication_status=WITHHELD_PENDING_RESEARCH_SATURATION`으로 남긴다.

P8 leaf receipt는 `generalization_acceptance.json`이다. 저장소의 36개 prompt snapshot과
13개 필수 mechanism family golden replay가 모두 통과했고, master goal에 열거된 known-bad
30개는 실제 회귀시험 29개와 연결되어 전부 실행·통과했다. P8 추가 수용시험은 8/8,
관련 핵심 시험은 81/81, Pro-first 전체 시험은 288/288이며 production static audit의
critical finding은 0이다. golden replay는 live query/fetch를 하지 않아 0/0이고 Pro의
score·Stage 권한도 모두 false다.

쉬운 예로 C28 software golden은 보안이라는 단어 하나를 ARR로 간주하지 않는다.
ARR·RPO와 GRR/NRR·renewal 질문, source role, positive/counter fact 연결이 모두 닫혀야
통과한다. 첫 공개 material 질문을 다시 `PUBLIC_SEARCHABLE`로 열면 같은 fixture도 즉시
saturation invalid가 되는 것까지 함께 검증한다.
