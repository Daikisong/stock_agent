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

2026-08-24 현재 PR #7의 단계별 구현 상태는 다음과 같다. 이 표의 `완료`는 해당
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
| P9 | 진행 중 | 000660 pass 8 revision 2와 최신 111-fact verifier attempt 4 완료(accepted 49, query/search 0/0). mandatory-linked repair 51개는 15+36 bounded batching, pass 10은 submit 0. repair/saturation/score, C17/C28가 남음 |
| P10 | 부분 완료 | V2 static audit 20/20 zero·critical 0 구현. P9 완료 뒤 full CI·최종 receipt가 남음 |

### 2026-08-24 live P9 진행 기록

`000660 / C06 / as_of_date=2026-08-23`은 최초 승인된 같은 ChatGPT Pro 대화에서
다음 append-only pass를 완료했다.

```text
initial full research                 COMPLETE
public gap closure 1                  COMPLETE
public gap closure 2                  COMPLETE
counter/supersession closure          COMPLETE
effective dossier                     97 facts / 28 questions / 98 routes
source verifier v8                     43 accepted candidates
```

검증 반려 46개를 한 prompt에 넣은 최초 repair 계획은 약 51.8만 자였다. 이 계획은
ChatGPT composer에서 처리되지 않았고 DB상 `submit_count=0`이었으므로 실제 Pro
전송은 없었다. 해당 pass는 삭제하지 않고 `TRANSPORT_PENDING`으로 보존했다.

repair transport는 이제 최대 21만 자의 deterministic prefix batch를 사용한다.
선택되지 않은 packet은 `pending_rejection_packets.jsonl`과 plan receipt의
`deferred_rejection_packet_ids`에 모두 남고, 선택 batch의 Pro 응답을 전체 dossier에
재검증한 뒤 다음 pass에서 다시 계획한다. transport batch는 연구 누락이나
`EVALUATED_ABSENT`로 간주하지 않는다.

쉬운 예로 46개 반려가 한 입력창에 들어가지 않으면 46개를 버리는 것이 아니라
`첫 묶음 → 전체 재검증 → 남은 묶음` 순서로 같은 대화에서 처리한다. 최종 gate는
여전히 verifier repair pending 0을 요구한다.

첫 bounded repair pass `PROPASS-3ef919d661d3bfa39f201c4e`는 46개 중 17개를
담아 정확히 1회 제출됐다. 마지막 assistant turn의 종료 marker 한 글자 누락은 exact
scope marker와 strict JSON parse를 요구하는 bounded normalization으로 복구했고, raw MD와
normalized MD를 서로 다른 hash로 함께 보존했다. pass는 `COMPLETE / submit_count=1`이며
같은 prompt를 다시 제출하지 않았다.

실제 응답에는 material 9, counter 5, resolution 3으로 새 fact 17개와
`NARROWED 13 / REPLACED 4` repair 제안 17개가 있었다. 첫 적용이 0건이 된 원인은 Pro
연구가 아니라 compact dialect adapter가 모든 repair register를 diagnostics로만 옮기고
실행 register를 빈 배열로 만든 것이었다. current `VERIFIER_REPAIR` pass의 exact
candidate/question/category/action/replacement 형식만 보존하도록 교정했고, 실제 capture의
adapter/schema replay는 17 facts, 17 proposals, 10 lineages, 17 routes로 통과했다.

14개 multi-question mismatch는 generic 정책과 회귀시험으로 해결했다. Pro가 선언한 대표
question과 replacement fact의 question은 모두 immutable rejection packet roster의 부분집합이어야
한다. packet 밖 question은 hard fail하고, packet 안이면 원래 전체 roster를 자동 승인 범위가
아닌 deterministic reverification scope로만 복원한다. 원본 Pro response는 수정하지 않는다.

원본과 분리한 실제 runtime 전체 복제본에서 pass 6을 무전송 재처리한 결과, 17개 repair
action이 모두 verifier로 전달됐고 5개는 accepted, 12개는 pending으로 남았다. 반려 사유는
`WRONG_SUBJECT 8 / HISTORICAL_ONLY 3 / QUOTE_MISMATCH 1`이다. 즉 adapter가 17건을 0건으로
버리는 결함은 해소했지만 source 검문을 통과하지 않은 12건을 Pro 권위만으로 채택하지 않았다.

same-pass correction은 기존 schema의 `pass_id UNIQUE`를 없애고 `(pass_id,
revision_ordinal)` lineage로 추가한다. legacy row는 revision 1로 보존하고, 새 hash는 별도
`effective_dossier.r{revision}-{hash 앞 24자}.json`과 full hash를 가진 revision 2 DB row로 기록한다. rehearsal에서는
revision 1 no-op snapshot `PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390`과 revision 2
snapshot `PRODOSSIERSNAPSHOT-235d2b608cbda1622f500445`가 함께 남았고
`foreign_key_check=[]`를 확인했다. 이는 당시 rehearsal 기록이며, 이후 원본 runtime에도 같은
snapshot ID/hash의 revision 2가 반영됐다. 최신 상태는 아래 “pass 7 actual capture 통합” 절을
기준으로 한다.

첫 no-op 적용이 만든 pass 6 snapshot과 `resolution 0 / unresolved 17` receipt는 감사
증거이므로 삭제·덮어쓰기하지 않는다. 교정 재처리 경로는 exact parent인 pass 4에서 response
delta를 다시 만들고, 기존 revision 1을 부모로 한 새 append-only revision artifact를 남긴다.
capture 전 관측은
`live_repair_capture_pending_20260824.json`, 복구 후 상태는
`live_repair_capture_recovered_20260824.json`에 고정했다. 나머지 29개 packet은 deferred
roster에 보존돼 있다. 초대형 미전송 pass
`PROPASS-7694a86ac9e996eeabd03394`는 `TRANSPORT_PENDING / submit_count=0`이다.
이 시점에는 full-thesis score·Stage·publication 권한이 아직 없다. 당시 다음 단계였던 원본
revision 2 적용은 완료됐고, 현재는 pass 7 capture의 durable 입고와 최신 verifier 결과에
따른 bounded repair가 남아 있다.

원본 재개에서 추가로 `PUBLIC_GAP_CLOSURE` selector가 모든 non-terminal mandatory
question을 가져가 `VERIFIER_REPAIR_REQUIRED`까지 public search pass에 넣는 순서 결함을
확인했다. public closure는 이제 `missing mandatory + public_material_gap_question_ids`만
후보로 삼고 verifier/provider/lifecycle pending을 각각의 전용 queue에 남긴다. 이미 1회
제출된 pass 7은 취소·재전송하지 않고 durable running pass로 보존하며, 응답 완료 뒤 exact
conversation recovery로 capture한다. routing 규칙이 바뀌어도 submitted/complete이며 아직
snapshot이 없는 pass를 먼저 recovery plan으로 반환하므로, pass 7을 건너뛴 채 새 pass를
동시에 보내는 것도 차단한다.

브라우저 안전 규칙도 함께 고정했다. 실제 ChatGPT 입력은 E2R 전용 Chrome의 exact
conversation DOM/CDP만 사용하며 OS 전역 키보드, clipboard, window focus 자동화는
사용하지 않는다. 중복으로 고착된 탭을 복구할 때도 exact canonical conversation URL과
target id를 확인한 뒤 미전송 composer 탭만 닫고 정상 탭과 로그인 profile은 보존했다.
실행 식별자, pass별 상태, verifier semantics 변화, 테스트와 잔여 작업은
`live_validation_progress_20260824.md`에 계속 누적한다.

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

## P10 정적 판정의 단일 진입점

목표 문서의 P10 정적 카운터는 이제 다음 명령 하나로 다시 계산한다.

```bash
PYTHONPATH=src python -m e2r.cli.audit_e2r_pro_first_v2 --repo-root .
```

내부적으로 새 기준을 별도 하드코딩해 기존 audit와 충돌시키는 방식이 아니다. 이미 구현된
contract totality, 36 prompt snapshot, semantic security/authority, scoring publication,
verifier repair, generalization acceptance를 실행한 뒤 목표의 20개 판정 이름으로 합성한다.
추가로 live 상태기계의 순서를 검사해 repair보다 scoring이 먼저 오거나, public material
gap이 corroboration으로 낮아지거나, material gap follow-up 경로가 없어지는 회귀를 잡는다.

현재 워크트리 재계산은 다음과 같다.

```text
required counter roster  20/20
zero counters            20/20
critical_count           0
status                   PASS
mutation detection       PASS
```

쉬운 예로 각 검문소가 따로 `통과`라고 적힌 종이를 외부 검수자가 손으로 맞추는 대신,
마지막 출구에서 20개 도장을 모두 다시 확인하고 하나라도 없으면 종료 코드 2로 실패한다.
GitHub Actions의 `static-security`도 같은 명령을 실행하므로 로컬 보고와 clean runner의
판정 경로가 같다.

이 정적 PASS는 live 연구 완료를 뜻하지 않는다. pass 7은 durable `COMPLETE`가 됐고 pass 8은
동일 conversation에 딱 1회 제출된 `RESEARCH_RUNNING`이다. 다음 resume은 pass 8의 기존
visible 결과 회수만 허용하며 점수·Stage·publication은 계속 막혀 있다.

## completed repair와 descendant capture의 순서

pass 6처럼 Pro 응답 capture는 성공했지만 과거 adapter 결함으로 repair action이 0개 적용된
경우, 동일 pass correction은 기존 snapshot을 덮어쓰지 않고 revision 2로 추가한다. 이때
이미 다음 pass snapshot이 생기면 historical pass revision을 추가할 수 없도록 snapshot
store가 차단한다.

따라서 resume 순서는 다음으로 고정한다.

```text
latest pass가 completed repair revision 1
+ capture에는 proposal 존재
+ durable resolution 0
+ immutable pass_input_hash exact match
→ exact parent에서 무전송 reprocess
→ same-pass revision 2 append
→ 이미 제출된 unsnapshotted descendant capture
→ 신규 repair planning
```

이 gate는 단순히 이름이 `VERIFIER_REPAIR`라는 이유만으로 재실행하지 않는다. proposal이
실제로 capture됐고 적용 결과가 0이며, 해당 pass가 아직 전체 latest이고 revision 1인 경우만
대상이다. 완료된 정상 repair, revision 2가 있는 pass, descendant가 이미 있는 historical
pass는 건드리지 않는다.

쉬운 예로 교정 답안 17개를 받은 기록과 채점표 0개가 동시에 있을 때만 다시 채점한다.
이미 17개 채점표가 있거나 다음 시험 답안까지 제본된 뒤라면 자동으로 과거 장을 바꾸지
않는다. 복제 rehearsal에서는 새 전송 없이 기존과 동일한 `5 accepted / 12 pending`과
revision 2 dossier hash를 재현했다.

Windows runtime의 전체 경로가 긴 경우 full 64자 hash를 파일명에도 반복하면 `.part`를
포함해 260자를 넘을 수 있다. snapshot filename은
`effective_dossier.r{revision}-{hash 앞 24자}.json`을 사용하고, ledger에는 full hash를
계속 저장한다. 파일을 읽거나 기존 파일을 재사용할 때는 언제나 full hash를 검사한다.

repair receipt와 effective repaired artifact 기록 후 snapshot persist 전에 process가
종료되는 crash window도 별도로 판정한다. artifact full hash가 receipt와 같고 normalized
hash가 latest snapshot과 다를 때만 미반영 recovery를 실행한다. 두 hash가 같으면 이미
반영된 정상 repair이므로 재실행하지 않는다.

## pass 7 actual capture 통합: parser가 아니라 evidence ledger adapter

pass 7은 ChatGPT Pro가 자료를 못 가져온 사례가 아니다. 실제 capture에는 source-backed
material 4개, counter 5개, resolution 5개와 route 18개가 있다. 문제는 자연어를 점수로
바꾸는 parser가 아니라, 같은 대화의 후속 출력이 기존 immutable dossier 장부에 안전하게
append되는 transport dialect 경계였다.

```text
raw capture                    14 facts / 5 lineages / 18 routes / 18 questions
read-only append delta         14 facts / 2 new lineages / 18 new routes
effective dossier             111 facts / 21 lineages / 133 routes / 28 questions
deterministic research status COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER
score authority               false
Stage authority               false
new submit                    0
```

다음 다섯 규칙을 generic하게 통합했다.

- canonical V2 여부는 `PROFACT-` ID 하나가 아니라 schema의 fact 필수 필드 전체로 판정한다.
- follow-up이 R13 cross guard를 selected roster에 반복해도 prior primary contract scope를
  바꾸지 않고 diagnostics로 남긴다.
- 반복된 source lineage는 prior identity를 유지하고 URL/fact/publisher/current-state만
  append한다. raw capture의 표현은 수정하지 않는다.
- durable SQL 핵심 필드가 모두 같은 prior pass row는 보조 감사 필드까지 byte-for-byte
  보존한다. 한 필드라도 다르면 hard fail한다.
- top-level `research_status`는 Pro 문구를 직접 채택하지 않고 merged mandatory question
  roster에서 다시 계산한다. Pro 문구는 saturation diagnostics에 남긴다.

쉬운 예: Pro MD는 사람이 읽을 수 있는 조사 보고서이고, effective dossier는 주민등록번호가
있는 장부다. 보고서가 기존 출처를 “2Q 실적”이라고 줄여 써도 장부의 기존 lineage identity를
새 사람으로 바꾸지 않는다. 대신 새 공시 URL과 새 사실만 기존 사람의 최신 기록으로 붙인다.

`subject`·segment·product를 코드가 종목별 문구로 발명하지 않는다. compact direct-source
fact에 subject가 빠졌을 때만 응답 자체의 exact target 또는 publisher를 구조 식별자로 쓰고,
segment/product 부재는 `null`로 명시한다. statement, URL, publisher, date, quote는 raw
payload에서 가져온 값을 유지하고 이후 deterministic source verifier가 진위를 판정한다.

실제 pass 7 capture를 DB write 없이 parser → adapter → identity binding → append-only merge
→ schema validator → normalizer에 통과시켰고 focused regression은 `56/56 PASS`다. 그 뒤
기존 READY bundle을 `REUSE_CAPTURE`로 입고해 pass 7은 durable `COMPLETE`, 누적 snapshot은
`111 facts / 21 lineages / 133 routes / 28 questions`가 됐다. 이 단계에서도 full-thesis
score와 canonical Stage는 없다.

## 공유 fact의 acquisition provenance와 질문 route ownership 분리

pass 7 뒤 public-gap 판정이 28개 mandatory question 전부를 다시 열었다. raw Pro 자료가
비어서가 아니라 질문 closure가 “이 질문이 fact를 쓴다”와 “이 질문 소유 route가 fact를
처음 취득했다”를 같은 조건으로 묶었기 때문이다.

```text
기존 조건
Q2가 F1을 사용
→ Q2 소유 route.accepted_fact_ids에도 F1이 있어야 함

수정 조건
F1이 durable route history 어디선가 실제 accepted됨
+ F1이 현재 verified됨
→ Q2도 F1을 사용할 수 있음
→ 원래 route ownership은 Q1으로 그대로 보존
```

이 분리는 route를 다른 질문으로 재라벨하는 완화가 아니다. route adequacy와 source-role
coverage는 계속 현재 질문이 요청한 route만 본다. 오직 fact의 acquisition provenance만
전체 immutable accepted-route history에서 확인한다.

derived counter/resolution relationship은 직접 URL을 가진 새 원문 fact가 아닐 수 있다.
따라서 현재 verified relationship이 선언한 `source_anchor_fact_ids` 전부가 immutable
acquisition history에 있을 때만 계보를 상속한다. anchor가 후속 snapshot에서 superseded되어
현재 verified roster에서 빠졌더라도 과거 accepted 영수증은 지우지 않는다. 반면 route와
anchor가 없는 direct fact는 계속 차단한다.

쉬운 예: 한 실적 공시에서 “매출 증가”와 “CAPA 잠김”을 동시에 읽었다면 공시 다운로드
영수증은 한 장이면 된다. 두 번째 체크리스트 칸에 같은 공시를 사용한다고 영수증을 다시
발급할 필요는 없다. 다만 영수증 없이 보고서에 새로 적힌 숫자는 여전히 근거로 인정하지
않는다.

실제 pass 7 provisional saturation을 동일 snapshot binding으로 재실행한 결과 잘못 열린
public question은 `28→10`으로 줄었다. 남은 10개 가운데 9개는 실제 direct/anchor route 결박이
없고 1개는 linked verified fact가 없어 그대로 보류했다. 이 경계는 공유 fact, archived
anchor relationship, unrouted direct fact의 세 회귀시험으로 고정했고 saturation 시험은
`26/26 PASS`다.

Windows mock 종료 시 발견된 multi-pass SQLite read connection 7곳도
`contextlib.closing`으로 명시적으로 닫았다. 기능 assertion 뒤 임시 DB 삭제만 실패하던
`WinError 32`가 사라졌고 동일 Windows Chromium mock은 `1/1 PASS`다. production static
audit는 `20/20 zero / critical_count=0 / PASS`를 유지한다.

## 공개자료 취득과 verifier 무결성 수리의 전이 분리

Pass 8은 28개 질문별 공개 경로를 실제 조사하고 새 route 영수증 28개를 남겼지만 새 material
fact는 0개였다. 이 상태에서 남은 질문을 availability 문자열만 보고 또 공개검색으로 보내면
route만 계속 늘어나는 무한 반복이 된다. 공개 웹은 immutable ledger의 누락된 fact ID나 잘못
연결된 subject를 고칠 수 없기 때문이다.

그래서 terminal fact-backed 질문을 다음 두 갈래로 나눴다.

```text
route 부족 또는 core source role 부족
→ PUBLIC_GAP_CLOSURE

route 충분 + core source role 충족 + fact/lineage 결박 실패
→ VERIFIER_REPAIR
```

Pass 8 read-only 재판정에서는 신규 공개 route queue가 `0`, verifier repair가 `5`다. 즉
`새 자료를 못 믿으니 또 찾아라`가 아니라 `찾은 자료의 장부 연결을 승인·철회·교체하라`로
전이가 바뀌었다. score와 Stage는 이 5건이 다시 deterministic verification을 통과하고
saturation이 true가 된 뒤에만 계산한다.

같은 pass에서 정상 route가 verified direct fact의 exact source URL을 열었으나
`accepted_fact_ids`만 빠뜨린 경우에는 다음 불변식을 모두 확인해 acquisition provenance를
복구한다.

- fact `research_pass_id == route.pass_id`
- provider/parser `SUCCESS`
- exact opened source URL 일치
- 현재 verified direct fact이며 derived relationship이 아님

다른 pass의 같은 URL은 쓸 수 없다. derived relationship은 exact URL 지름길을 쓰지 않고
모든 declared source anchor가 immutable accepted-route history에 있어야 한다.

또 compact Pro dialect의 `NOT_APPLICABLE_WITH_REASON`은 raw 사유를 유지한 채 canonical
availability `NOT_APPLICABLE`로만 정규화한다. 이를 `PUBLIC_SEARCHABLE`로 기본 변환하면
원래 적용 불가능하다고 설명한 질문이 공개검색 queue로 되돌아가는 의미 손실이 생긴다.

Pass 8 revision 1과 수정 adapter의 read-only 결과는 이 availability 한 leaf만 다르고 fact,
statement, source, route count는 모두 같다. 기존 revision 1을 고치지 않고 same-pass revision 2를
append해 두 의미를 모두 감사할 수 있게 한다. 관련 saturation focused test는 `28/28`, dossier
status test는 `14/14`, Windows Chromium browser mock은 `1/1`, production static audit는
`20/20 zero / critical_count=0 / PASS`다.

### recovered dossier는 같은 hash의 verifier roster만 사용할 수 있다

Live process를 재시작하면 latest dossier snapshot은 pass 8 revision 2인데 source verification
receipt는 pass 4에 머물 수 있다. pass 6 repair가 fact를 철회·교체했기 때문에 두 roster의
개수가 우연히 비슷해도 identity는 같지 않다. 실제로 old 97-row verifier receipt에는 최신
111-fact dossier에 없는 rejection candidate 8개가 남아 있었다.

따라서 repair packet을 만들기 전 다음 hash gate가 필요하다.

```text
receipt effective/normalized dossier hash == latest dossier hash
→ durable verifier artifact 재사용 가능

두 hash가 다름
→ latest effective snapshot을 bounded deterministic reverify
→ 새 verification roster만 repair compiler에 전달
```

쉬운 예로, 반품·교환 뒤의 최신 재고표에 지난달 불량품 목록을 그대로 붙이면 존재하지 않는
상품 번호가 나온다. 불량 판정 규칙을 바꾼 것이 아니라 최신 재고표를 같은 검사기로 다시
검사해야 한다. 이 경계는 recovered durable result, current durable result, just-computed result
세 경우의 회귀시험으로 고정했고 live-runtime `26/26`, source-verifier `29/29`, static audit
critical `0`을 통과했다.

### accounting cap의 미전송 영수증과 실제 transport failure를 구분한다

최신 verifier는 111개 candidate 중 49개를 승인했고, mandatory question에 연결된 rejection
51개를 repair packet으로 만들었다. 첫 15개는 199,646자로 composer 예산 210,000자 안이며,
나머지 36개는 다음 batch에 그대로 보존된다. 첫 계획 pass 10은 점검용 follow-up 상한 6에서
`TRANSPORT_PENDING / submit_count=0`으로 멈췄다.

이 상한은 실제 UI 오류가 아니라 accounting policy다. 사용자가 뒤에 더 큰 상한을 명시해도
기존 코드는 같은 pending row만 반환해 재개가 불가능했다. 반대로 모든 pending을 자동 재시도하면
composer 초과나 UI incompatibility까지 중복 전송할 수 있다.

수정 후에는 사유 문자열이 정확히 bounded pass limit이고 submit이 0이며 새 상한에 여유가
있을 때만 새 pass를 append한다. 기존 pending row는 그대로 보존하고 새 pass detail에
`resumed_from_transport_pending_pass_id`, original logical input hash, 새 transport-resume input을
함께 저장한다. 실제 transport failure는 상한을 올려도 pending 그대로다. 같은 호출의 반복은
새 pass를 만들지 않는다. Windows Chromium을 포함한 multi-pass `19/19`, verifier-repair
`18/18`로 이 경계를 고정했다.

### DOM click 완료와 navigation wait timeout은 재전송 사유가 아니다

첫 15개 repair batch의 pass 11은 visible send button click action이 완료된 뒤 Playwright가
scheduled navigation을 기다리다 timeout됐다. exactly-once claim은 이미 소비돼
`submit_count=1`이므로 다시 composer를 채우거나 click하면 안 된다.

`TRANSPORT_PENDING / submit_count=1`은 recovery-only 상태로 다룬다. 같은 conversation에서
exact pass/parent marker가 있는 visible result를 확인할 때만 RESEARCH_RUNNING으로 복구하고
COMPLETE로 전이한다. marker가 없으면 pending을 유지하며 자동 submit은 없다. Post-click
inspection이 이미 RESEARCH_RUNNING을 증명하면 최초 submit 호출 자체를 성공 처리하지만,
그 inspection도 단 한 번의 click 이후에만 실행한다. 이 경계는 Windows Chromium multi-pass
`20/20`, live-runtime `27/27`, static critical `0`으로 고정했다.
