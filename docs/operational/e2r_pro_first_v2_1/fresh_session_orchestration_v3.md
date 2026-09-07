# Fresh-Session Orchestration V3

## 목적

이 문서는 old repair-heavy ChatGPT Pro 대화를 재사용하지 않고 완전히 새 Chat 대화에서
`ResearchPacketV3`를 최초 한 번만 보내는 P6 경계를 설명한다.

핵심은 새 프롬프트를 만드는 것만이 아니다. 다음 다섯 identity가 모두 달라야 한다.

```text
runtime root
job_id
run_id
research_pass_id
conversation_id
```

쉬운 예로 새 파일 이름만 만들고 브라우저 주소가 여전히
`/c/6a8b09c3-bfcc-83ee-b15b-9f76eca52249`라면 fresh run이 아니다. P6는 준비 단계에서
기존 `/c/<id>`를 거절하고, 전송 뒤 새 `/c/<id>`가 발급됐는지 다시 확인한다.

이 단계는 코드와 offline mock browser E2E까지다. 실제 000660 ChatGPT Pro 전송은 P7이며,
P6 검증 중 live Pro, query, fetch, search를 실행하지 않았다.

## old → fresh identity chain

`FreshSessionBoundaryService.start()`는 다음 순서만 허용한다.

```text
old job의 old_job_frozen_at 확인
→ old/fresh runtime root가 서로 같거나 nested인지 검사
→ fresh_session_id를 포함한 새 candidate fingerprint 생성
→ 새 job_id 생성
→ old job.superseded_by_fresh_job_id 결박
→ immutable boundary receipt 기록
```

runtime root가 이미 다른 파일을 담고 있으면 재사용하지 않는다. 같은
`fresh_session_id + old_job_id`의 immutable boundary receipt가 있는 idempotent 재개만 허용한다.

fresh run 자체가 efficiency gate를 실패하면 `seal_fresh_efficiency_failure()`가 다음 disposition으로
봉인한다.

```text
FRESH_SESSION_DIAGNOSTIC_ONLY
OPERATIONAL_EFFICIENCY_GATE_FAILED
NEW_CONVERSATION_REQUIRED
```

그 job은 더 이상 submit할 수 없다. 새 `fresh_session_id`를 가진 successor job을 만들어야 한다.
즉 실패한 새 대화도 수십 번 repair해서 운영 성공으로 바꿀 수 없다.

## Fresh-blind ResearchPacketV3

새 schema:

```text
configs/e2r_pro_research_packet_v3.schema.json
```

허용 입력:

```text
target metadata
as_of_date / latest trading snapshot date
normal business / financial / revision snapshot
selected primary contract 1~3개
R13 cross guard 4개
research objectives / source role policy / forbidden inferences
```

구조적으로 제거한 입력:

```text
existing_thesis_digest
historical_anchor_digest
known_positive_facts / known_counterfacts
old accepted facts / route receipts / rejection roster
old question terminal answers
Gate 1 / V1 / V2 score와 Stage
expected source URLs / fact IDs
```

`OldAnswerLeakageManifest`는 old job/run/conversation/pass, fact ID, route ID, question answer,
score/Stage, expected URL/fact ID의 exact token을 보관한다. packet과 compiled initial prompt를 각각
감사하고 하나라도 발견되면 파일을 보내기 전에 실패한다.

packet의 `fresh_blind_boundary`는 다음 count를 모두 0으로 고정한다.

```text
old_pro_fact_input_count
old_route_receipt_input_count
old_rejection_input_count
old_question_answer_input_count
old_score_stage_input_count
expected_source_input_count
expected_fact_id_input_count
```

## 브라우저 경계

production `PlaywrightChatGPTWebAdapter`가 사용하는 UI는 ordinary `Chat` composer와 화면에 보이는
`Pro` reasoning mode다. legacy `Deep research` 도구는 명시적으로 거절한다.

초기 준비:

```text
현재 E2R tab이 old conversation 또는 new-chat route인지 확인
→ unrelated ChatGPT conversation이면 입력 없이 실패
→ ChatGPT base new-chat route로 이동
→ conversation_id=None 확인
→ V3 packet upload
→ Initial Prompt V3 입력
→ send-ready 확인
→ submit_count=0 / AWAITING_USER_APPROVAL
```

사용자 approval을 durable nonce로 소비한 뒤에만 DOM send가 한 번 가능하다. send 뒤에는 다음을
검사한다.

```text
submit_count == 1
new conversation_id is not null
new conversation_id != old conversation_id
```

둘째 또는 셋째 조건이 실패하면 `DIAGNOSTIC_ONLY_NEW_CONVERSATION_REQUIRED`다. 같은 adapter의
재클릭과 자동 resubmit은 불가능하다.

큰 V3 prompt는 OS keyboard/clipboard를 쓰지 않고 정확히 찾은 contenteditable DOM 안에서만
입력한다. rendered `innerText`가 JSON 들여쓰기를 접어 길이가 짧아 보여도 실제 editor text node와
`br`를 재구성해 원문 prompt가 그대로 남았는지 검사한다.

## initial approval이 허용하는 bounded tail

새 conversation이 확인되고 initial result hash가 생긴 뒤에만 approval scope를 만든다.

```text
INITIAL_FULL_RESEARCH              정확히 1회
PUBLIC_GAP/COUNTER closure         합쳐서 최대 1회
VERIFIER_REPAIR                    최대 1회
SATURATION_AUDIT                   최대 1회
```

모든 follow-up은 같은 target/as_of/contracts/browser session/conversation에 묶인다. 다른 대화로
이동하면 준비와 전송 양쪽에서 실패한다.

compact repair는 P5 compiler를 그대로 사용하지만 job/run/pass/parent marker를 추가했다.
`BrowserResultSnapshot`과 direct DOM capture도 `RepairDeltaV3` sentinel을 정식 완료 결과로 인식한다.
따라서 ChatGPT가 별도 MD attachment 대신 화면 본문에 delta를 반환해도 parser로 넘길 수 있다.

두 번째 semantic repair, 두 번째 public-gap closure, 두 번째 saturation은 operational success로
이어지지 않는다. generic prompt/schema/normalizer/verifier를 고치고 다른 새 conversation에서
재실행해야 한다.

## runtime receipt

Git에 raw 실행물을 넣지 않고 fresh runtime 아래에 다음 hash-bound receipt를 쓴다.

```text
fresh_session_boundary_receipt.json
jobs/<job>/fresh_session/fresh_blind_packet_audit.json
jobs/<job>/fresh_session/fresh_initial_prompt_leakage_audit.json
jobs/<job>/fresh_session/initial_prompt_v3_receipt.json
jobs/<job>/fresh_session/fresh_v3_prepare_receipt.json
jobs/<job>/fresh_session/fresh_initial_submit_receipt.json
jobs/<job>/fresh_session/fresh_initial_submit_failure_receipt.json   # 실패 시
jobs/<job>/fresh_session/fresh_efficiency_failure_receipt.json       # 봉인 시
```

receipt는 같은 경로의 내용이 달라지면 덮어쓰지 않는다.

## 테스트 증거

P6 unit/integration test가 확인한 항목:

```text
새 runtime/job/run/pass ID
old fact/route/answer/score/Stage/expected URL leakage 0
old conversation follow-up 차단
new-chat route가 아니면 USER_ATTENTION_REQUIRED
manual new-chat 이동 뒤 submit_count=0으로 재준비 가능
initial exactly-once submit
새 conversation identity 확인
initial approval scope의 bounded follow-up
compact repair plan idempotency
repair 두 번째 pass 차단
실패한 fresh run 봉인 → 새 successor runtime/job/run/pass
```

production adapter mock E2E:

```text
old conversation frozen
→ new Chat route
→ ResearchPacketV3 upload
→ Initial Prompt V3 submit 1회
→ LocalEvidencePreflight
→ RepairDeltaV3 submit/capture 1회
→ Saturation Audit submit 1회

DOM submit count       3
conversation count     1 fresh / 0 old reuse
각 pass submit_count   1
```

P0~P6 phase regression은 60/60, 기존 V1/V2/browser/scoring/source-verifier를 포함한 전체
Pro-first regression은 447/447 통과했다.

로컬 Ubuntu host에는 `libnspr4/libnss3/libasound2`가 system install되어 있지 않아, test 전용
package를 `/tmp`에 추출하고 `LD_LIBRARY_PATH`로만 연결했다. 저장소와 사용자 runtime에는 이
라이브러리를 복사하지 않았다. 같은 production adapter test는 GitHub Actions의 browser dependency
step에서도 실행된다.

## P7로 넘기는 경계

P6 완료가 의미하는 것은 “fresh 경로를 안전하게 실행할 수 있다”는 것이다. 다음은 아직 증명하지
않았다.

```text
실제 000660 새 Pro conversation 결과
initial candidate / accepted fact 수
post-preflight verifier acceptance >= 80%
genuine semantic repair <= max(5, 10%)
mandatory question terminal closure
7 component / 21 Judge / deterministic score / StageCourt
```

위 수치는 P7 live canary receipt가 있어야만 판정한다.
