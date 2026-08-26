# E2R Pro-First V2.1 구현 진행 장부

기준 시각: `2026-08-26 C17 4차 FAIL 봉인 / subject verifier v11 전체 회귀 PASS`

기준 Goal:
`C:\Users\eorb9\Downloads\e2r_pro_first_v2_1_fresh_session_verifier_ready_master_goal.md`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`

phase commit 계보:

```text
P0 b6c30eb9  기존 repair-heavy Pro 실행을 진단 자료로 봉인
P1 10c7269b  Pro fact 반려 원인을 최초 출력·로컬 결함·의미 결함으로 분해
P2 152db6a7  source 문서와 atomic fact를 분리한 검증 친화 dossier를 도입
P3 d5d62bc2  최초 Pro 조사에서 verifier-ready 증거를 생성하도록 계약 강화
P4 788e14d2  URL 날짜 인용 alias scope의 기계적 결함을 로컬에서 자동 정규화
P5 cad578af  전체 dossier 재출력을 제거하고 의미 오류만 compact delta로 수리
P6 8b0e27bd  기존 대화를 봉인하고 새 Pro 세션의 blind canary 실행 경계를 구현
P7 fdf4ac40  Pro JSON 첨부를 동일 응답 증거로 봉인하고 C06 Gate를 통과
P8 f719b94b  C17/C28 독립 fresh target 생성을 고정
P8 e6ac55b4  C17 1~4차 fresh initial 실행 상태를 순차 봉인
```

PR #7은 계속 Draft/open이며 main 병합, draft 해제, auto-merge를 하지 않는다.

## 현재 판정

```text
P0 old run freeze                         COMPLETE
P1 rejection A/B/C taxonomy              COMPLETE
P2 ResearchDossierV3                      COMPLETE
P3 Initial Prompt V3                      COMPLETE
P4 local preflight                        COMPLETE
P5 compact RepairDeltaV3                  COMPLETE
P6 fresh-session orchestration            COMPLETE
P7 000660 fresh canary                    COMPLETE
P8 C17/C28 fresh canary                   IN_PROGRESS (C17 4차 FAIL 봉인, v11 5차 대기)
P9 final CI/audit                         PENDING
```

아직 선언할 수 있는 최종 verdict는 없다. 특히 old run을 완료한 것으로 간주하거나
`PRO_FIRST_V2_1_OPERATIONAL_RESEARCH_READY`를 선언하지 않는다.

## P7 최종 CI 봉인

`fdf4ac402861db2c12be2eeeafa7c24727e59f3c`를 checkout한 세 GitHub 실행이 모두
완료됐다.

```text
push E2R Pro-first verification
https://github.com/Daikisong/stock_agent/actions/runs/32881804962
SUCCESS / full regression 7,683 tests / failure·error 0

PR E2R Pro-first verification
https://github.com/Daikisong/stock_agent/actions/runs/32881810946
SUCCESS / full regression 7,683 tests / failure·error 0

PR E2R v6 operational cutover verification
https://github.com/Daikisong/stock_agent/actions/runs/32881811183
SUCCESS / Gate 1 receipt·production static audit·7,683 tests PASS
```

따라서 P7은 로컬 영수증만 통과한 상태가 아니라 GitHub의 별도 checkout에서도 전체
회귀를 통과한 상태로 봉인한다.

## P8 독립 cross-archetype fresh 경계

C17 `011170 롯데케미칼`과 C28 `053800 안랩`에는 C06처럼 실제 old repair-heavy job이
없다. 기존 `FreshSessionBoundaryService.start()`를 그대로 쓰면 old job의 종목을 상속하므로,
C06 job을 부모로 넣을 경우 011170을 요청해도 000660 패킷이 만들어지는 잘못된 실행이 된다.

이를 피하려고 다음 경계를 추가했다.

```text
INDEPENDENT_CROSS_ARCHETYPE_CANARY
→ symbol/company/as_of/archetype를 새 candidate와 job에 직접 결박
→ 가짜 frozen old job 생성 0
→ C06 old answer·score·Stage 입력 0
→ 새 runtime/job/run/pass/conversation 요구 유지
→ 기존 대화 화면에는 입력하지 않고 new-chat route로 이동 후 exactly-once submit
```

쉬운 예로 C17 실행은 “C06 문서를 지운 사본”이 아니다. 처음부터 `011170 / 롯데케미칼 /
C17`인 빈 fresh job을 만들고, old-answer deny 목록은 비어 있는 상태로 시작한다.

실행 전 검증:

```text
independent target/boundary regression          PASS
Linux V2.1 non-browser focused                  72/72 PASS
Windows Playwright fresh browser+orchestration  21/21 PASS
Pro-first V2 static audit                       PASS / critical 0
Pro-first production static audit               PASS / critical 0
compileall / git diff --check                    PASS
```

다음 실제 전송 순서는 C17을 별도 새 대화에서 먼저 닫고, 그 결과가 efficiency gate를
통과한 뒤 C28을 또 다른 새 대화에서 실행하는 것이다. 두 실행 모두 점수·Stage 권한은 없다.

## P0 — old repair-heavy run 봉인

봉인 대상:

```text
job              PROJOB-cdd91020f15891533e61431f
run              PRORUN-a7dacadb7088fc23535bfdde
conversation     6a8b09c3-bfcc-83ee-b15b-9f76eca52249
target/as_of     000660 / 2026-08-23
archetype        C06_HBM_MEMORY_CUSTOMER_CAPACITY
frozen_at        2026-08-24T19:28:25.387533Z
```

마지막 in-flight pass15는 새 Goal을 받기 전에 이미 `submit_count=1`이었다. 지시대로 결과를
한 번만 capture하고 deterministic import/receipt까지만 수행했다. 이후 old conversation에
새 입력은 없었다.

```text
last pass          PROPASS-5cafcd69a1577739808ba25b
status             COMPLETE
response hash      570484b5d4d46921c2aa6bf064d768f7d4b3637e4cf6dcc3496302ab38d1e27e
repair candidates  6
withdrawn          2
unresolved         4
effective facts    69
questions/routes   28 / 211
snapshot           PRODOSSIERSNAPSHOT-05656ec8f80ad8d8e58fb94d
dossier hash       6e6fcc84784ba93be41589689e5f0c2d6952078396d016de33ae5ff22f83c675
```

old job의 canonical 의미:

```text
OLD_V2_REPAIR_HEAVY_DIAGNOSTIC_RUN
SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION
NOT_OPERATIONAL_EFFICIENCY_PROOF
```

SQLite `pro_research_jobs`에 다음 immutable transition state를 추가했다.

```text
old_job_frozen_at
superseded_by_fresh_job_id
```

현재 successor는 아직 만들지 않았으므로 `superseded_by_fresh_job_id=null`이다. P6에서 완전히
새 job/conversation이 만들어질 때 same target/as_of를 검사한 뒤 결박한다.

## 권한 차단

freeze 뒤 다음 세 경로를 모두 막는다.

```text
initial job claim_submit
follow-up plan / prepare
follow-up ledger claim_submit
```

실제 old DB에서 재검증한 결과:

```text
freeze 시 initial submit                  1
freeze 시 follow-up submit               10
freeze 이후 새 submit                     0
old follow-up plan             TransportPendingDecision
reason                         SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION
```

쉬운 예로 기존 대화는 삭제한 것이 아니라 “읽기·감사용 보관함”으로 잠갔다. 남은 4개를 같은
대화에 또 묻는 버튼은 코드의 계획 단계와 최종 전송 단계 양쪽에서 모두 잠긴다.

## runtime 보존과 Git 경계

runtime receipt:

```text
C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\live_v2\20260823T145430Z\
jobs\PROJOB-cdd91020f15891533e61431f\fresh_session\old_run_freeze_receipt.json
```

```text
logical receipt hash  2e3daa189aa98b38dacd978cafdb744b1e8e7d6069362f869b0a35cdb0338d3d
file SHA-256          597f0924056d6a3def2b99aa35f7578ff14654859179135a47f4c551468b89ae
runtime_preserved     true
```

원문 Pro 보고서, fetched document, SQLite, screenshot은 runtime에 그대로 보존한다. Git에는
원문을 복제하지 않고 외부 검수에 필요한 ID, hash, 수치, 의미, 테스트만 기록한다.

## 검증

```text
new P0 freeze tests                         3/3 PASS
parser/live/repair/static focused          63/63 PASS
Windows mock browser multi-pass E2E        PASS
freeze CLI idempotent replay               PASS
actual old plan blocked                    PASS
```

Windows 전체 live-runtime 묶음에서 `git rev-parse`가 WSL UNC 경로를 repository로 인식하지
못한 환경 오류는 코드 회귀로 세지 않는다. 같은 테스트는 Linux에서 통과했고 실제 browser
mock test는 Windows 환경에서 성공했다. 최종 판단은 push 뒤 Linux GitHub Actions 결과로 한다.

## P1 — rejection taxonomy

old runtime의 전체 rejection register를 삭제·샘플링하지 않고 읽어 다음을 생성했다.

```text
old_run_rejection_taxonomy.json
old_run_rejection_taxonomy.md
```

append-only snapshot의 register 302행을 `candidate_id + original_candidate_hash`로 결박해
고유 후보 74개로 환원했다. 원문 statement와 quote는 runtime에만 두고 Git 문서에는 식별자,
canonical source document ID, 원인, routing, generic 수정 위치, regression test ID만 넣었다.

```text
고유 rejection                               74
A INITIAL_PROMPT_OUTPUT_DEFECT               50 / 67.57%
B LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT      24 / 32.43%
C GENUINE_SEMANTIC_OR_SOURCE_DEFECT            0 / 0.00%
같은 source가 반복된 후보                    63 / 17 source groups
중복 mechanical rejection                     8
old audit에서 확인된 genuine semantic repair   0
```

가장 큰 원인은 source 부족이 아니라 lifecycle 계약이었다. `UNSUPPORTED_DERIVATION` 38건은
모두 `current_status=UNKNOWN`이어서 old lifecycle bridge가 `UNVERIFIED_PENDING`으로 만든
후보였다. 쉬운 예로 “소송이 해결됐다”는 resolution fact를 가져왔는데 상태 필드가 비어 있으면,
자료를 다시 찾을 문제가 아니라 V3가 `RESOLVED/OPEN/...` 중 하나를 반드시 출력하게 해야 한다.

다음 24건은 Pro에게 다시 물으면 안 되는 로컬 결함이다.

```text
nonissuer subject alias/scope resolver       14
compact repair segment/product 상속           5
same-source quote representation              2
unavailable source representation             3
```

C가 0이라는 수치는 old fact가 전부 의미적으로 정답이라는 뜻이 아니다. old verifier가 A/B에서
먼저 막았기 때문에, P2~P4 수정 뒤 fresh run의 재검문에서 실제 C가 새로 드러날 수 있다.
그때만 compact Pro semantic repair에 보낸다.

검증:

```text
taxonomy unit test                           3/3 PASS
고유 candidate / required field             74/74 PASS
original_candidate_hash binding             74/74 PASS
원문 statement/quote Git 복제                0 PASS
deterministic CLI replay                     PASS
```

## P2 — ResearchDossierV3

source document와 atomic fact를 분리하는 append-only `ResearchDossierV3`를 구현했다.

```text
SourceDocumentV3 1개
├─ AtomicFactV3 N개 (각각 predicate/quote/locator 1개)
└─ SourceLineageV3 1개

DerivedMetricV3
└─ input_fact_ids로만 원천 fact를 참조
```

old taxonomy의 가장 큰 A 결함 38건을 막기 위해 V3 lifecycle에서 `UNKNOWN`을 제거했다.
`CURRENT|OPEN|RESOLVED|SUPERSEDED|HISTORICAL_ONLY` 중 하나가 아니면 schema 단계에서
거절된다. old B 결함처럼 compact replacement가 segment/product를 잃는 것도 V3에서는
빈 값이 schema를 통과하지 못한다.

추가 deterministic graph gate:

```text
fact 안 source URL 반복                          금지
fact 안 derived metric 혼합                     금지
source/predicate/subject/excerpt 동일 중복       금지
tracking canonical URL / fragment                금지
publication/availability/event 미래누수          금지
source document/fact/lineage roster 불일치        금지
fact_kind/collection 또는 question binding 불일치 금지
failed verifier_preflight                        금지
```

provider failure는 예외적으로 빈 evidence graph + `PROVIDER_PENDING`으로 보존한다. 이는
0점이나 정상 점수 확정이 아니다.

V1/V2 schema·validator는 그대로 등록해 read/verification compatibility를 유지했다. 새 V3
transport binding은 최초 conversation placeholder와 durable pass receipt만 바꾸며 fact,
quote, source document는 바꾸지 않는다.

검증:

```text
V3 schema/evidence graph test                   13/13 PASS
P0/P1 + 기존 V1/V2 focused regression          99/99 PASS
기존 dossier parser/import regression           16/16 PASS
합계                                            128/128 PASS
JSON Schema Draft 2020-12 self-check            PASS
compileall / git diff --check                    PASS
```

상세 계약은 `research_dossier_v3_contract.md`에 기록했다.

## P3 — Initial Prompt V3와 36-contract compiler

master goal의 Initial Full Research Prompt V3를 별도 template으로 추가했다. V2 template과
compiler는 바꾸지 않았으므로 기존 receipt와 snapshot의 의미도 유지된다.

실제 V3 initial prompt는 다음을 동적으로 결합한다.

```text
공통 verifier-ready base prompt
+ target / as_of_date / ResearchPacketV3 context
+ 선택된 primary contract 1~3개
+ 모든 실제 job에 붙는 R13 cross guard 4개
+ mandatory question / source role policy
+ exact ResearchDossierV3 JSON Schema
```

쉬운 예로 C06 한 개를 선택하면 C06 질문과 공통 R13 질문만 들어간다. C17 질문은 들어가지
않는다. C06 전용 검색어나 HBM 전용 규칙은 template/compiler에 없고, C17이나 C28도 같은
코드가 해당 contract를 읽어 prompt를 만든다.

V3 compiler의 강제 경계:

```text
입력 packet schema                  e2r_pro_research_packet_v3만 허용
primary contract                    1~3개
R13 cross guard                     실제 job마다 4개 자동 부착
output                              exact e2r_pro_research_dossier_v3 schema
atomic evidence                     16개 공통 규칙
verifier_preflight                  9 true + derived 혼합 false
score_authority / stage_authority   false
gold/expected/future outcome input  compile 전에 거절
initial prompt hard boundary        100,000 characters
```

36개 canonical contract마다 tracked snapshot을 다시 만들고 deterministic audit JSON/Markdown을
함께 게시했다. primary 32개 snapshot은 실제 one-primary job과 똑같이 R13 4개를 포함하고,
R13 4개 snapshot은 contract 자체의 unit coverage를 확인하는 감사 전용이다.

```text
36/36 compile                        PASS
mandatory question missing           0
atomic contract missing              0
verifier preflight missing           0
derived metric separation missing    0
forced COMPLETE                      0
score/Stage leakage                  0
other-archetype question pollution   0
source role policy missing           0
output V3 schema missing             0
prompt over 100k                     0
prompt size range                    34,909~57,956 chars
```

검증:

```text
P3 전용 regression                   10/10 PASS
P0/P1 + dossier import + V2/V3/P3    64/64 PASS
36 snapshot audit CLI                PASS / critical 0
production static audit              PASS / critical 0
git diff --check                     PASS
```

더 넓은 local Pro-first discovery도 실행했지만 Playwright 사용 묶음은 test body 전에 Linux
`libnspr4.so` 부재로 browser process를 시작하지 못했다. 이는 P2에서 기록한 같은 host 환경
제약이며 P3 코드 실패로 PASS에 포함하지 않았다. push 뒤 의존성을 설치하는 GitHub Actions를
최종 외부 실행 기준으로 확인한다.

이 단계에서는 fresh ChatGPT conversation을 만들거나 Pro에 전송하지 않았다. 따라서 P3
PASS는 “Pro 답변이 좋았다”는 뜻이 아니라 “최초 요청부터 verifier가 읽을 구조를 모든
contract에 동일하게 요구한다”는 뜻이다.

## P4 — Local Evidence Preflight

`ResearchDossierV3`를 source verifier에 바로 넘기지 않고 다음 경계를 강제했다.

```text
V3 사전 정규화
→ URL/source representation/text/alias/scope/date/atomic fact preflight
→ deterministic source verifier
→ rejection root-cause classifier
```

V3의 canonical source/fact 분리는 유지하면서 기존 verifier만 읽는 projection을 별도로 만든다.
preflight가 가져온 원문은 verifier가 다시 fetch하지 않는다. V3가 preflight를 우회해 verifier를
직접 호출하면 명시적으로 실패한다.

로컬에서 닫는 대표 사례:

```text
tracking URL/fragment/query/trailing slash
redirect final URL
CRLF/HTML entity/Unicode quote·dash·whitespace
issuer 및 주입된 publisher alias
V2/V3 field, source ID, lineage ID alias
segment/product closed enum
published date와 HTTP Last-Modified 충돌
동일 official lineage의 alternate representation
```

quote는 byte/Unicode/locator/alternate official representation의 literal exact 순서만 허용한다.
semantic similarity로 검문을 통과시키지 않는다. compound fact도 각 part에 독립 literal quote
span이 있을 때만 쪼갠다.

모든 verifier rejection은 5개 root cause 중 하나로 분류한다.

```text
LOCAL_NORMALIZABLE
SOURCE_REPRESENTATION_RESOLVABLE
INITIAL_PROMPT_OUTPUT_DEFECT
GENUINE_SEMANTIC_OR_SOURCE_DEFECT
NONMATERIAL_AUXILIARY_REJECTION
```

앞의 두 분류는 Pro 전송이 항상 0이다. 현재 P4는 분류·영속 receipt까지만 구현했으며 실제
compact repair 전송은 P5 범위다.

영속 runtime 산출물:

```text
verification/preflight/research_dossier.preflight.json
verification/preflight/verifier_projection.json
verification/preflight/preflight_operations.jsonl
verification/preflight/preflight_issues.jsonl
verification/preflight/preflight_receipt.json
verification/rejection_classifications.jsonl
```

상세 설계와 외부 검수용 경계는 `local_evidence_preflight.md`에 기록했다. 이 단계에서도 fresh
ChatGPT conversation 생성, browser 전송, 새 web search는 하지 않았다.

검증:

```text
P4 local preflight regression                 17/17 PASS
영속 V3 preflight → verifier lifecycle         PASS
P0~P4 + dossier import + source verifier       91/91 PASS
production static audit                        1/1 PASS / critical 0
focused 합계                                  92/92 PASS
compileall / git diff --check                   PASS
실제 Pro·query·search 호출                      0/0/0
```

P3 head `d5d62bc2`의 GitHub Actions는 P4 커밋 직전에도 장시간 `in_progress`였고 실패로
판정되지 않았다. P4 push로 새 head CI를 시작하며 그 결과는 다음 phase 장부에서 head SHA와
run URL로 이어서 기록한다.

## P5 — Compact RepairDeltaV3

기존 V2 old-run repair 경로는 과거 receipt 호환을 위해 그대로 두고, V3 전용 compact repair를
별도 경로로 추가했다. 새 경로는 전체 dossier를 prompt/response에 다시 넣지 않는다.

```text
P4 rejection classifications
→ Pro-repairable material candidate만 선택
→ same source + same root cause + same question scope grouping
→ RepairDeltaV3 prompt
→ CORRECT|REPLACE|NARROW|WITHDRAW
→ V3 graph validation
→ local preflight
→ deterministic source reverification
```

prompt와 output의 강제 경계:

```text
target prompt chars                        <= 60,000
hard max                                   <= 100,000
hard 초과 transport batching 성공 처리        금지
full dossier re-output                     0
accepted fact delete/modify                 0
score/Stage authority                       false/false
repair pass ordinal                         1만 허용
```

`fetched_excerpt`는 반려된 claimed quote가 아니라 실제 fetched source에서 literal locator로
잘라낸 문장이다. locator도 없으면 빈 값이며 semantic similarity로 문장을 만들지 않는다.

`WITHDRAW`는 replacement 없이 public gap을 다시 열고, `CORRECT/NARROW/REPLACE`는 새 atomic
fact와 current-pass route receipt를 요구한다. replacement는 Initial V3 preflight 계약을 그대로
만족해야 하며 full effective dossier graph validation과 source verifier를 모두 다시 통과해야 한다.
repair 전 accepted fact는 hash가 동일해야 하고 재검문에서도 accepted여야 한다.

새 source lineage의 independence group은 publisher + URL host로 보수적으로 생성해 같은
publisher의 여러 문서를 독립 증거로 부풀리지 않는다.

영속 runtime 산출물:

```text
repair_v3/compact_repair_prompt.md
repair_v3/compact_repair_prompt_receipt.json
repair_v3/repair_delta_v3.json
repair_v3/repair_actions.jsonl
repair_v3/reverification_rows.jsonl
repair_v3/research_dossier.repaired.json
repair_v3/compact_repair_receipt.json
```

검증:

```text
P5 compact RepairDeltaV3 regression            13/13 PASS
P5 + legacy V2 repair + P4 + source verifier   77/77 PASS
production static audit                          1/1 PASS / critical 0
focused 합계                                    78/78 PASS
compileall / schema self-check / diff check       PASS
실제 Pro·query·search 호출                        0/0/0
```

상세 설계는 `compact_repair_delta_v3.md`에 기록했다. 현재 P5 서비스는 deterministic
compiler/parser/apply/reverify까지 완성했지만 browser pass에 아직 연결하지 않았다. 따라서
실제 fresh Pro 전송은 여전히 0이다.

## P6 — Fresh-session orchestration

old conversation을 새 prompt의 답안지로 재사용하지 못하도록 runtime/job/run/pass/conversation
identity를 하나의 경계로 묶었다.

```text
frozen old job
→ disjoint fresh runtime root
→ fresh_session_id가 포함된 새 candidate/job
→ ResearchPacketV3 blind leakage audit
→ ChatGPT new-chat route에서 V3 packet/prompt 준비
→ user approval 뒤 exactly-once initial submit
→ old와 다른 conversation ID 확인
→ same-conversation bounded follow-up scope
```

ResearchPacketV3에는 old fact, route, rejection, question answer, score/Stage, expected URL/fact ID를
담는 필드가 없다. 별도 `OldAnswerLeakageManifest`의 exact identity/token도 packet과 initial prompt에서
다시 세어 0이 아니면 browser 준비 전에 실패한다.

새 대화가 아닌 `/c/<old-id>`에서 준비하려 하면 입력 전에 `USER_ATTENTION_REQUIRED`로 돌아간다.
사용자가 new-chat route로 이동한 뒤에는 submit_count 0인 같은 packet/prompt만 재준비할 수 있다.
전송 뒤 old conversation ID가 다시 나오면 그 fresh run을 diagnostic-only로 봉인하고, 새
fresh_session_id/runtime/job/run/pass를 가진 successor만 허용한다.

initial approval이 허용하는 operational tail:

```text
public-gap/counter closure     합쳐서 0~1회
semantic RepairDeltaV3        0~1회
saturation                    1회
```

두 번째 repair/gap/saturation은 같은 conversation을 길게 끌지 않고
`NEW_CONVERSATION_REQUIRED`로 차단한다. compact repair response는 MD attachment가 없어도 화면의
`E2R_REPAIR_DELTA_JSON_BEGIN/END`를 production adapter가 완료 결과로 capture한다.

production adapter mock E2E:

```text
old frozen → fresh V3 initial → local preflight → compact repair → saturation
initial DOM submit                 1
repair DOM submit                  1
saturation DOM submit              1
old conversation submit            0
모든 fresh pass same conversation  true
모든 pass submit_count             1
```

검증:

```text
P6 fresh identity/orchestration regression       13/13 PASS
P6 production adapter browser E2E                 1/1 PASS
large prompt DOM integrity + V2 browser regression 3/3 PASS
P0~P6 phase regression                            60/60 PASS
전체 Pro-first regression                         447/447 PASS
실제 Pro·query·search 호출                         0/0/0
```

상세 설계와 runtime receipt는 `fresh_session_orchestration_v3.md`에 기록했다. P6는 offline
orchestration proof이므로 아직 000660 initial acceptance 80%나 score/Stage를 주장하지 않는다.

## 다음 단계 P7

로그인된 사용자 전용 E2R Chrome/CDP의 ordinary Chat + visible Pro mode에서 완전히 새 conversation을
만들고 000660 / `as_of_date=2026-08-23` / C06+R13 fresh blind packet을 정확히 한 번 전송한다.
initial result에 local preflight와 source verification을 적용해 acceptance ratio를 계산한다. 80%
미만이면 repair로 메워 PASS하지 않고 해당 conversation을 diagnostic-only로 봉인한다.

## P7 live 실행 장부 — fresh initial 1회

마스터 Goal의 사용자 승인 범위에 따라 ordinary Chat + visible Pro mode에서 실제 fresh canary를
시작했다. 기존 대화에 follow-up을 보내지 않았고, 새 conversation을 만든 뒤 initial prompt를
정확히 한 번만 제출했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260824T221229Z
fresh session    FRESH-V2-1-C06-20260824T221229Z
fresh job        PROJOB-ee3f7609d478547f60e3aff8
fresh run        PRORUN-886983514379a2248fe03d3c
initial pass     PROPASS-fe8dc97296863bea30fb5151
durable transient conversation WEB:08326745-1438-42bb-a18b-9355869dab22
visible canonical conversation 6a8cc4ce-095c-83e8-b375-8d40084b818e
old conversation 6a8b09c3-bfcc-83ee-b15b-9f76eca52249
submit count     1
capture count    0 (연구 완료 대기 시점)
current status   RESEARCH_RUNNING
```

blind packet과 prompt 경계:

```text
packet hash                     dcefe680d4f0d079e6af236e7e8744ef21f0afbeac8187935d191fb292bf3712
prompt hash                     a0d4a9a98d255b82fe2db641cfbe1a3c6889226b68d0c6ce837e7e62db981ecc
prompt chars                    58,648
packet old-answer leakage       0
old score/Stage leakage         0
mandatory question families     28
score/stage authority           false/false
```

첫 prepare 시 ChatGPT의 과거 오류 toast 때문에 send-ready 판정이 30초 안에 끝나지 않아
`USER_ATTENTION_REQUIRED`로 안전 정지했다. 이때 `submit_count=0`이었다. 동일 브라우저 draft의
prompt hash와 첨부 File SHA-256을 다시 검증해 새 upload나 composer 입력 없이 복구했고,
그 뒤 제출 횟수는 정확히 1이 됐다. 쉬운 예로 서류가 접수 창구에 이미 놓여 있는지를 hash로
확인한 뒤 접수 버튼만 한 번 누른 것이며, 같은 서류를 두 번 올리지 않았다.

제출 직후 ChatGPT UI가 임시 `WEB:...` 대화 ID를 사용하다 정식 `/c/<id>` URL로 전환하는 것도
live에서 확인했다. 감시 프로세스를 브라우저 연구와 분리해 종료하고, `submit_count=1`을 요구하는
no-submit recovery 경로를 추가했다. 완료 결과 안의 exact job/run marker와 report hash가 모두
맞을 때만 정식 conversation ID로 재결박한 뒤 capture한다. 이 복구 경로에는 upload, composer
입력, DOM send가 없다.

live 실행에 앞서/실행 중 확인한 회귀:

```text
fresh efficiency + orchestration unit tests       19/19 PASS
Windows production adapter browser E2E             2/2 PASS
prepared draft no-mutation recovery browser E2E     1/1 PASS
submitted packet reuse regression                    PASS
transient→canonical conversation rebind regression  PASS
현재 live 새 conversation 확인                       PASS
현재 live exactly-once submit                        PASS (1)
```

이 장부는 중간 상태다. Pro 응답 capture, DossierV3 import, local preflight, source verification과
초기 material acceptance 80% gate가 끝나기 전에는 P7 PASS나 score/Stage를 선언하지 않는다.

## P7 fresh initial 최종 판정 — 1차 conversation은 diagnostic-only

2026-08-25에 첫 fresh initial의 완료 결과를 캡처하고 initial efficiency gate까지 실행했다. 이
conversation은 P7 PASS가 아니다. 마스터 Goal 13~14절에 따라 낮은 acceptance를 repair로 메우지
않고 diagnostic-only로 봉인했다.

```text
visible mode                    ordinary Chat + visible Pro
canonical conversation         6a8cc4ce-095c-83e8-b375-8d40084b818e
submit / capture               1 / 1
additional browser send        0
mandatory questions            28 / 28
serialized source documents    0
serialized material facts      0
accepted material facts        0
initial acceptance             0.0%
source verifier fetch          0
query / search                 0 / 0
score / Stage authority        false / false
score receipt / Stage receipt  없음 / 없음
gate                           FAIL
failure reasons                NO_INITIAL_MATERIAL_CANDIDATES,
                               INITIAL_ACCEPTANCE_RATIO_BELOW_80_PERCENT
publication                    withheld
new conversation required      true
```

Pro가 조사 내용을 전혀 만들지 않은 것은 아니다. 화면 보고서에는 28개 question 판정, 공식 issuer·
경쟁사·시장자료에 대한 서술, 11개 공개/비공개·parser/provider gap, self-audit가 들어 있다. 다만
Pro가 마지막에 exact excerpt 총량을 자체 점검하다 한 단어 초과를 발견했다고 서술한 뒤, 유효한
`E2R_RESEARCH_DOSSIER_JSON_BEGIN/END` 블록과 fact별 excerpt–URL 결박을 출력하지 않았다. 쉬운 예로
조사 메모는 도착했지만 각 주장에 원문 문장과 출처를 붙인 증빙 명세서는 제출되지 않은 상태다.

사람이 읽을 수 있는 모든 보고서 내용은 버리지 않았다.

```text
raw visible report chars                 8,817
normalized report chars                  9,379 (파일 newline 포함 9,380)
visible citation href registry           3
reported material/source/route counts    28 / 18 / 122
serialized usable material facts         0
question results preserved               28
explicit unresolved gaps preserved       11
```

Codex structurer는 새 검색이나 점수 판단 없이 완료 보고서만 읽어 V3 representation을 만들었다.
보고서에 exact excerpt와 explicit URL이 fact 단위로 함께 있지 않은 주장은 material fact로 만들지
않고 question result와 unresolved gap으로 보존했다. 따라서 0개는 “Pro의 모든 설명을 폐기했다”는
뜻이 아니라 “검증 불가능한 설명을 점수 사실로 몰래 승격하지 않았다”는 뜻이다.

live에서 확인된 generic 결함과 조치는
`p7_fresh_initial_failure_taxonomy.md`에 기록했다. 핵심 수정은 다음과 같다.

```text
완료 보고서에 JSON block 없음       → readable report + citation registry를 원문 보존 capture
보고서 representation 복구           → Codex-only structurer, browse/fetch/score/Stage 금지
fact roster 0에서 mapper 예외         → provider 호출 없이 zero-count verification receipt
post-capture verifier 재개             → 브라우저를 다시 열지 않고 immutable capture에서 재개
post-import USER_ATTENTION 재개        → 기존 import ledger 재사용
중단된 중복 import timestamp drift     → evidence 필드 동일할 때 durable ledger timestamp로 복구
```

첫 run의 canonical receipts:

```text
capture source                  DIRECT_REPORT_DOM_NORMALIZED
capture report SHA-256          8ae172543c9a2beba7ec98937efca00c3989a7b73cac3608b1b16dae2c22848c
browser result SHA-256          dd595f8e27c58e22a72e37677adee2b46d231ba81d6080987ba56312a07d2efa
dossier snapshot SHA-256        0c0a4a2fae10db5cea7166ab9db6c20bdfc466fecbcda3f8b5c59b075af5ce9b
efficiency receipt SHA-256      8e751564ceb0f03b0c92015a4ea268c5cffd6a6d0aa129fb40dc2a7927fb4160
source verification semantics  e2r_pro_source_verification_v10
current durable state           GAP_ADJUDICATION + old_job_frozen_at set
```

root-cause prompt patch는 모든 아키타입 공통 Initial Prompt V3에 적용했다. self-audit 오류나 응답
길이 압력이 있어도 dossier 전체를 생략하지 않고, 문제가 있는 fact만 gap으로 내린 뒤 유효한 JSON을
먼저 보장하도록 했다. C06·000660 전용 문구는 추가하지 않았다. 36개 prompt snapshot을 다시 만들었고
compile/오염/누수/길이 critical은 0이다.

다음 P7 시도는 같은 conversation의 repair가 아니다. 새 runtime, fresh_session_id, job, run, pass,
ChatGPT conversation을 사용한 blind fresh rerun이어야 한다. 새 run이 initial acceptance 80%를
통과하기 전에는 C17/C28, 점수, Stage, 운영 준비를 진행하지 않는다.

커밋 전 검증:

```text
fresh/structurer/import/source/prompt 집중 회귀       83/83 PASS
변경된 Windows Playwright browser 회귀                3/3 PASS
Initial Prompt V3 canonical snapshot                 36/36 PASS
Pro-first V2 requirement static audit                PASS / critical 0
Pro-first production static audit                    PASS / critical 0
Python compileall / git diff check                    PASS / PASS
```

WSL 전체 Pro-first discovery에서는 463개 중 browser-dependent 60개가 동일하게 `libnspr4.so` 부재로
시작하지 못했고 나머지 403개는 통과했다. 이는 코드 assertion 실패가 아니라 WSL Chromium 실행환경
문제다. 변경으로 영향을 받은 browser assertion 3개는 Playwright가 설치된 Windows Python에서 다시
실행해 모두 통과했다.

GitHub의 최신 보존 head `05cb9726cfa3f451cf3df8c5be1d097b5c205552`에서도 독립 Linux CI를
확인했다.

```text
E2R Pro-first verification (push)         SUCCESS  run 32793935843
E2R Pro-first verification (PR)           SUCCESS  run 32793940414
E2R v6 operational cutover verification   SUCCESS  run 32793940623
core-unit / browser-mock / full-regression / static-security   모두 SUCCESS
PR #7                                      Draft / OPEN / MERGEABLE
local HEAD == origin branch                true
```

1차 fresh job은 원래 live runtime의 중앙 SQLite 장부에 기록되지만, 그 job의 report와 receipt는
1차 fresh runtime에 있다. 따라서 2차 successor는 서로 다른 두 위치를 함께 써야 한다.

```text
predecessor artifact root  = 1차 fresh runtime
durable state database     = 원래 live runtime/pro_first.sqlite3
successor artifact root    = 완전히 새로운 2차 fresh runtime
```

이를 위해 live runner/CLI에 optional `state_database_path` 경계를 추가했다. 기본값은 기존과 같아
호환성을 유지하고, successor일 때만 중앙 장부를 명시한다. 쉬운 예로 이전 시험 답안지는 1차 서랍에서
읽되, 수험번호 장부는 계속 중앙 금고에서 읽고, 새 답안은 2차 빈 서랍에 쓰는 구조다. 세 위치를
섞거나 복사하지 않는다. 분리 경로 회귀를 포함한 orchestration test는 `18/18 PASS`다.

## P7 최종 — 2차 fresh C06 initial efficiency PASS

1차 diagnostic-only run을 predecessor로 봉인한 뒤 새 runtime/session/job/run/pass/conversation에서
blind fresh initial을 다시 실행했다. 초기 prompt에는 1차 fact, URL, question 답, score, Stage를
넣지 않았으며 submit/capture는 각각 정확히 한 번이다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T150833Z
fresh session    FRESH-V2-1-C06-20260825T150833Z
fresh job        PROJOB-ab48ce7e94097cf9b6846602
fresh run        PRORUN-683f5a5423a6e367f443c6de
initial pass     PROPASS-e49762cc3ad556d6b211d92b
conversation     6a8db0ad-8ed0-83e8-888e-dce26c950343
assistant turn   request-WEB:a63d3897-9bd3-4749-996d-52a56adc7a89-0
submit/capture   1 / 1
```

### visible JSON 산출물 복구

Pro는 응답 본문에 0-fact 실패 결과를 낸 것이 아니었다. 본문에는 응답 길이를 줄인 transport manifest를
두고, 같은 assistant turn에 전체 `ResearchDossierV3` JSON 파일을 visible attachment로 제공했다.
기존 adapter가 `.md/.pdf`만 찾았기 때문에 inline manifest를 전체 dossier로 오인했다.

generic 수정은 종목명이나 파일명을 하드코딩하지 않는다.

```text
inline V3가 expanded_artifact_required_for_verification=true 선언
→ sandbox:/mnt/data/<safe-json-basename> exact reference 검사
→ 같은 conversation + 같은 assistant turn + 같은 filename 1개만 선택
→ visible download control 사용
→ 기존 capture/incoming과 READY는 변경하지 않음
→ capture/supplemental에 별도 JSON + receipt + READY를 written-last로 봉인
→ job/run/target/as_of/conversation/turn/capture receipt/report hash/count 결박
→ browser submit delta=0일 때만 importer가 expanded JSON 선택
```

쉬운 예로 본문은 “전체 명세서는 동봉 파일에 있다”는 운송장이었고, JSON은 실제 명세서였다. 기존
운송장 봉인을 뜯어 바꾸지 않고 동봉 파일에 별도 인수증을 붙였다. 첨부 READY가 없거나 다른 turn,
파일명, hash, 선언 수량이면 0-fact 본문을 import하지 않고 fail-closed한다.

실제 attachment/result:

```text
downloaded bytes                  169,993
expanded source documents         16
expanded facts                    25 (material 18 / counter 5 / resolution 2)
derived metrics                   3
mandatory question results        28
search route receipts             37
unresolved gaps                   12
post-cutoff / duplicate credit    0 / 0
browser submit delta              0
expanded dossier SHA-256          e32c98c78934c2d62c39cbec67d11032948269e62d086a0cdf418dcc7153c1a0
supplemental receipt hash          108ca7596c88bf05c61cbedcf908d73c3db136ca8531339fa07ecf1c8afa48e5
```

Pro가 marker 표기용 `PENDING_NEW_CONVERSATION`과 `NONE`을 JSON identity에 복사한 경우도 initial pass의
top-level/current pass row가 정확히 일치할 때만 로컬에서 canonical placeholder/null로 바꾼다.
follow-up의 `NONE`은 고치지 않고 lineage 오류로 막는다. evidence, quote, URL은 이 정규화가 바꾸지 않는다.

### initial source verification과 efficiency Gate

전체 25개 fact를 source verifier에 넣었고, Initial Gate의 분모인 material candidate는 18개다.
그중 16개가 accepted여서 `16 / 18 = 88.8889%`로 80% 기준을 통과했다. 낮은 비율을 repair로 메운
결과가 아니라 follow-up 전 initial artifact만으로 계산한 값이다.

```text
mandatory question coverage                 28/28
material candidate / accepted               18 / 16
post-preflight acceptance                    88.8889% PASS
all fact terminal                            25/25
accepted all-kind fact                       21
genuine semantic repair candidate            3 <= limit 5
initial prompt output defect                 0
local-normalizable sent to Pro               0
source-representation sent to Pro            0
source-document unbound material             0
question-unbound material                    0
tracking URL                                 0
multi-source atomic fact                     0
derived metric mixed fact                    0
query/search                                 0/0
old conversation new submit                  0
score/Stage authority                        false/false
publication                                  withheld
Gate                                         PASS
```

canonical hashes와 수치는 `p7_c06_fresh_initial_success_receipt.json`에 별도 기록했다. 원문 보고서,
전체 source/fact JSON, fetched document는 Git에 복제하지 않고 보존 runtime의 hash로 결박한다.

검증:

```text
expanded attachment fail-closed unit regression     5/5 PASS
preflight/fresh/import 포함 focused regression      60/60 PASS
Windows MD/PDF/capture browser regression           20/20 PASS
actual visible JSON download                         PASS
actual expanded import                               PASS
actual source verification                           PASS
actual C06 Initial Efficiency Gate                   PASS (88.8889%)
actual Pro extra submit                              0
Linux non-browser Pro-first regression              392/392 PASS
Windows real-browser Pro-first regression            79/79 PASS
split-platform Pro-first total                       471/471 PASS
failure / error                                        0 / 0
Pro-first V2 static audit                         PASS / critical 0
Pro-first production static audit                 PASS / critical 0
E2R v6 production static audit                    PASS / critical 0
Pro-first V2 audit hash                            f0eec38d973de9ae5b5c7b52b505ccdec9b9fd78a1fc749bee7b7ad8998e8acc
E2R v6 static audit hash                           5f4df78b1870afe90511928f88bc76eefc46095e5746b882e80c9f0a068c3b41
compileall / git diff check                        PASS / PASS
```

따라서 P7 verdict는 `PRO_FIRST_V2_1_C06_FRESH_SESSION_PASS`다. 이는 아직 7 component/21 Judge/score/
Stage나 multi-archetype 완료를 뜻하지 않는다. 다음 단계는 각각 새 conversation을 쓰는 P8 C17/C28
fresh initial canary다.

## P8 진행 — 독립 target 경계와 C17 최초 capture

P8은 C06의 종목·conversation·증거를 복사하지 않고 C17과 C28을 각각 완전히 독립된 target으로
시작해야 한다. 이전 구현은 predecessor job이 있는 successor만 만들 수 있었으므로, 과거 진단 job이
없는 target에는 가짜 old job을 만들지 않는 `start_independent` 경계를 추가했다.

쉬운 예로 C06 수험표에 종목명만 롯데케미칼로 바꿔 재사용하지 않는다. 롯데케미칼의 target ID,
아키타입, job, run, pass와 새 ChatGPT conversation을 처음부터 따로 만든다.

```text
boundary commit       f719b94b5bcf99aec6de7e785675ecd16be89b49
target identity test  PASS (old diagnostic job 생성 0)
Linux focused tests   72/72 PASS
GitHub push CI        SUCCESS  run 32884242262
GitHub PR CI          SUCCESS  run 32884248916
GitHub v6 CI          SUCCESS  run 32884248976
```

C17 actual fresh initial은 visible ChatGPT Pro에서 정확히 한 번 전송됐고 새 conversation에서 약 55분간
조사된 뒤 완료됐다. 결과는 inline JSON으로 보존됐으며 자동 재전송은 없었다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T183156Z
fresh session    FRESH-V2-1-C17-20260825T183156Z
fresh job        PROJOB-bd77f3912ada3fdc878330c6
fresh run        PRORUN-6d2c7188521024cf65e94101
initial pass     PROPASS-6de9211605df22e8d1e255ce
conversation     6a8ddfc4-f27c-83e8-829d-919ecb97c815
assistant turn   request-WEB:38f40b92-5b48-45bf-9f26-a853b4009662-0
submit/capture   1 / 1
automatic resend 0
report SHA-256   db1b50f30ee4070e69895b14529dc85abd8cbd288dcb6a55612b996b8a9b2090
dossier SHA-256  517c4af5e78253afda0fcf9b63006bc6329ff50a10c534c4bfde33549613c4a8
```

### C17 local representation 정규화

최초 import는 조사 부족이 아니라 표현 계층의 양방향 연결 불일치에서 fail-closed했다. Pro에 같은 내용을
다시 묻거나 종목별 예외를 넣지 않고, 증거를 절대 늘리지 않는 공통 정규화만 추가했다.

```text
nonissuer source보다 강한 fact issuer scope     true → false  1건
material fact를 counter 칸에서 중복 참조         참조 삭제      1건
fact 쪽 question backlink가 없는 question 참조  참조 삭제      5건
새 fact 생성 / fact kind 승격 / scope 상향       0 / 0 / 0
Pro follow-up / browser submit 증가               0 / 0
```

예를 들어 “공시 가격은 국제 기준가다”라는 중립 fact가 어떤 질문에서는 참고 근거이고 다른 질문에서는
낙관론의 제약처럼 읽힐 수 있다. 그러나 전역 종류가 `MATERIAL`인 fact를 question의 `counter_fact_ids`에
동시에 넣으면 저장 규격이 충돌한다. 로컬 정규화는 그 fact를 `COUNTER`로 바꾸거나 새 사실을 만들지 않고,
잘못된 question 참조만 제거한다. 원문 fact와 closure 설명은 그대로 남는다.

이 규칙은 모든 target에 동일하게 적용하며 알 수 없는 fact ID는 지우지 않는다. 알 수 없는 ID는 기존
strict validator가 계속 오류로 막는다. Initial Prompt V3에도 issuer/source scope 일치, fact kind별
question reference, fact→question backlink 규칙을 공통으로 넣어 36개 snapshot을 다시 만들었다.

현재 C17 exact capture의 parser→dialect adapter→pre-schema→identity binding→strict validator 결과:

```text
source documents             8
material/counter/resolution  9 / 8 / 3
all facts                    20
mandatory questions          26
search route receipts        26
strict graph validation      PASS
focused regression           72/72 PASS
Initial Prompt V3 snapshots  36/36 PASS / critical 0
Pro-first static audit       PASS / critical 0
Pro-first V2 static audit    PASS / critical 0
E2R v6 production audit      PASS / critical 0
compileall / diff check      PASS / PASS
```

이 시점은 C17의 **capture·import 전 검문 PASS**이지 Initial Efficiency Gate PASS가 아니다. 다음 재개는
같은 submitted job과 immutable capture를 사용하며 browser upload·composer 입력·DOM send를 실행하지
않는다. source verification과 initial acceptance를 마친 뒤에만 C17 Gate 판정을 기록한다. C17이 끝나기
전에는 C28이나 P8 최종 verdict를 선언하지 않는다. 상세 수치와 hash는
`p8_c17_fresh_initial_preflight_receipt.json`에 기록했다.

첫 post-capture 재개는 브라우저를 열기 전에 fail-closed했다. 원인은 resume 경로가 이미 제출된 prompt를
영수증에서 복원하지 않고 최신 공통 template로 다시 compile한 뒤 immutable prompt receipt와 비교했기
때문이다. C17 제출 뒤 scope/reference 규칙 3개가 공통 template에 추가됐으므로 두 hash가 다른 것은
정상이다. 이 실패에서 browser submit과 runtime artifact 변경은 모두 0이다.

resume 경로를 다음처럼 분리했다.

```text
새 제출 전 경로       현재 template로 compile → prepare/upload/send 가능
submit_count=1 재개   기존 packet + manifest + prompt receipts만 exact-load
                     → current template compile 금지
                     → browser prepare/upload/send 금지
```

recovery loader는 당시 packet의 commit/config/hash, durable job의 packet/prompt hash, run/pass identity,
blind packet audit, prompt leakage receipt, mandatory question roster와 score/Stage authority false를 모두
검사한다. prompt 본문은 복원·전송하지 않고 영수증의 글자 수만 보존한다. compile이 호출되면 즉시
실패하도록 만든 회귀를 포함해 fresh orchestration `20/20 PASS`를 확인했다.

### C17 Initial Efficiency Gate — diagnostic-only FAIL

receipt-only recovery로 동일 capture를 import한 뒤 8개 source를 각 1회 full fetch하고 전체 20개 fact를
검증했다. query/search와 Pro follow-up은 모두 0이다. 결과는 9개 material candidate 중 3개 accepted로
80% Gate를 통과하지 못했다. 같은 conversation에서 repair로 비율을 올리지 않고 즉시 봉인했다.

```text
material candidate / accepted        9 / 3
post-preflight acceptance             33.3333% FAIL
mandatory question coverage           26 / 26
all fact terminal                      20 / 20
genuine repair candidate / limit       9 / 5
initial prompt output defect           1
local/representation sent to Pro       0 / 0
query/search                            0 / 0
same-conversation repair               0
score/Stage authority                  false / false
publication                            withheld
durable state                          GAP_ADJUDICATION + frozen_at
new conversation required              true
```

불변 Gate failure 수치와 runtime 파일 hash는 `p8_c17_fresh_initial_failure_receipt.json`에 기록했다.
이 33.3333%를 이후 verifier 개선으로 소급 변경하지 않는다.

거절 10건을 원문과 대조한 결과, 실제 output defect와 generic verifier 오탐이 섞여 있었다.

```text
원문 표 cell이 newline, excerpt가 vertical `|` delimiter  오탐 3건
본문 회사채 만기일 2028-01-31을 게시일로 오인          오탐 1건
exact excerpt에 target이 있는데 subject 띄어쓰기로 거절  오탐 1건
중간 문구를 생략한 비연속 quote                         실제 defect
떨어진 표 header/value를 한 excerpt로 합성               실제 defect
target도 subject도 exact excerpt에 없는 project label     실제 defect
```

표 delimiter 수정은 셀의 값과 순서가 실제 문서에 연속할 때만 punctuation-normalized exact match로
인정한다. 중간에 다른 셀이 끼면 계속 거절한다. 날짜 수정은 `재무제표 작성기준`, `발행일 만기일`처럼
본문/표 header에 포함된 단어를 게시일 label로 보지 않고, 줄 시작의 실제 `게시일 2026-...` 같은
metadata만 읽는다. subject 수정도 exact excerpt 자체에 target alias가 있을 때만 nonissuer subject의
띄어쓰기 차이를 허용한다.

sealed source page를 사용한 read-only projection 결과는 다음과 같다. 이것은 과거 Gate 재채점이 아니라
새 verifier 규칙의 단위 확인이다.

```text
vertical table quote exact match       3/3 PASS
synthetic header/value quote reject    2/2 PASS
SK filing publication date             2026-08-13 PASS
MOTIR target-specific subject scope    PASS
source/quote/publication regression    212/212 PASS
```

새 Initial Prompt V3에는 표 cell 합성 금지, publication date와 본문 미래일 분리, 최신 predicate와
HISTORICAL_ONLY 분리를 모든 아키타입 공통 규칙으로 추가했다. C17 종목명·질문명·검색어를 코드에
하드코딩하지 않았다. 다음 C17은 새 runtime/session/job/run/pass/conversation에서 blind fresh initial로
다시 시작한다.

### C17 두 번째 fresh initial — lifecycle 분모 결함 봉인

첫 실패에서 확인한 공통 prompt/verifier 결함을 고친 뒤, 첫 C17 job을 predecessor로 동결하고 완전히
새 runtime/job/run/pass/ChatGPT conversation에서 두 번째 actual Pro 조사를 정확히 한 번 실행했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T200105Z
fresh session    FRESH-V2-1-C17-R2-20260825T200105Z
fresh job        PROJOB-2136f20fb124e6b76760230b
fresh run        PRORUN-e53f79d5009fb8a7248a71ac
initial pass     PROPASS-68c4c79b446b0c16bdb9ff40
conversation     6a8df4a7-1690-83ee-bd01-036d058c979f
submit/capture   1 / 1
automatic resend 0
prompt/response  58,327 / 138,146 chars
research/total   3,076.970388 / 3,132.240946 seconds
report SHA-256   e353b051332af43ab60af225b7b535a3d8fb93e5d87f2f99edcede76ec48c19e
```

26개 mandatory question/route가 모두 채워졌고 8개 dossier source를 full fetch했다. 전체 21개 fact는
모두 terminal이었으며 query/search와 same-conversation repair는 0이었다. 그러나 당시 Gate 구현은
`material_facts` 배열의 12개를 lifecycle과 무관하게 모두 현재 acceptance 분모로 세어 `6/12=50%`로
FAIL을 봉인했다.

```text
당시 immutable Gate                         6 / 12 = 50.0000% FAIL
mandatory question                          26 / 26
all fact terminal                            21 / 21
initial prompt output defect                  0
genuine repair candidate / limit              4 / 5
query/search                                  0 / 0
same-conversation repair                      0
score/Stage authority                        false / false
publication                                  withheld
```

원인은 evidence 부족이 아니라 현재성 분모 오염이었다. 12개 중 Q1 과거 비교 fact 5개는 Pro가 명시적으로
`HISTORICAL_ONLY`로 보존했고, Q2/current material은 7개였다. 과거 사실을 삭제하거나 CURRENT로 승격하지
않고, `EvidenceLifecycleBridge.compile_as_evidence`가 true인 material만 현재 Gate 후보와 repair roster에
포함하도록 공통 계산을 고쳤다.

쉬운 예로 2026년 2분기 현재 성적을 평가하면서 2026년 1분기 비교표 5줄까지 새 답안의 분모에 넣으면 안
된다. 비교표는 이력으로 그대로 남기되 현재 답안은 `6/7=85.7143%`로 계산해야 한다.

```text
serialized material facts                    12 (모두 보존)
excluded HISTORICAL_ONLY                       5
current material candidate / accepted          7 / 6
read-only fixed-rule projection                85.7143% PASS
current genuine repair candidate               1 <= limit 5
```

과거 immutable FAIL receipt를 새 규칙으로 덮어쓰지 않았다. 위 PASS는 계산 수리 검증용 read-only projection
이라 operational Gate 권한이 없고, 실제 PASS는 새 conversation에서만 얻는다. 두 번째 실패의 전체 ID,
hash, 수치와 projection hash는 `p8_c17_fresh_initial_failure_receipt_r2.json`에 별도 봉인했다.

범용 회귀는 `현재 7개 중 6개 accepted + HISTORICAL_ONLY 5개 + 과거 rejection 5개`를 입력해 다음을
동시에 확인한다.

```text
과거 fact/ID 보존                              PASS
현재 분모                                      7
accepted                                       6
acceptance                                     85.7143% PASS
현재 genuine repair roster                     1
focused lifecycle/fresh/verifier regression   94/94 PASS
Pro-first static audit                        PASS / critical 0
Pro-first V2 static audit                     PASS / critical 0
E2R v6 production static audit                PASS / critical 0
compileall / diff check                       PASS / PASS
```

이 수정도 target, 종목명, C17 질문명으로 분기하지 않는다. 다음 단계는 이 commit을 push한 뒤 새
runtime/session/job/run/pass/conversation에서 C17 initial을 한 번 더 실행하는 것이다. 두 번째 실패 job은
감사용으로 동결하며 같은 conversation에는 어떤 추가 질문도 보내지 않는다.

### C17 세 번째 fresh initial — 전 후보 일괄 withholding 봉인

current-material Gate 수리를 push하고 CI green을 확인한 뒤, 두 번째 C17 job을 predecessor로 봉인하고
세 번째 actual Pro 조사를 새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T210303Z
fresh session    FRESH-V2-1-C17-R3-20260825T210303Z
fresh job        PROJOB-8d0471204d7de2826e879f2e
fresh run        PRORUN-69358af2127fa7984988fb83
initial pass     PROPASS-cc762a119f46a3f109bf08e6
conversation     6a8e0320-0f28-83ee-9a1e-5c0bc2d148c7
submit/capture   1 / 1
automatic resend 0
prompt/response  58,327 / 59,779 chars
research elapsed 4,946.447733 seconds
report SHA-256   8891d29aba3eb0c6c6f8e0a3aeca595c93932aad3d0cb550fba5c0aaea4368e5
```

Pro는 11개 source document와 26개 mandatory question result를 만들었지만, 조사 마지막에 fact-question
양방향 binding과 전체 schema 검증을 끝내지 못했다는 이유로 후보 50개 전부를 accepted candidate
배열에서 제거했다. 조사 부족과 구분하면 다음과 같다.

```text
opened source documents                 11
mandatory question results              26 / 26
self-reported candidate facts           50
serialized material/counter/resolution   0 / 0 / 0
search route receipts                     0
terminal/nonterminal questions            0 / 26
complete claimed                          false
```

최초 import는 `conversation_id=PENDING_NEW_CONVERSATION`, top-level/pass `parent_pass_id=null` 조합에서
fail-closed했다. 기존 transport normalizer가 같은 placeholder를 parent 문자열 `NONE`과 함께 쓴 경우만
처리하고 더 정확한 JSON null 조합을 놓쳤기 때문이다. exact initial pass와 명시적 parent field를 모두
확인한 뒤 null 또는 `NONE`만 허용하도록 공통 수정했다. parent field 누락과 follow-up pass는 계속
정규화하지 않는다.

실제 immutable capture를 browser 재개 없이 parser→dialect→pre-schema→identity binding→strict V3
validator에 다시 넣은 결과는 `0 facts / 11 sources / 26 questions` graph로 PASS했다. 동일 submitted job을
receipt-only recovery한 뒤 Gate를 실행했고 추가 upload/composer/send는 0이었다.

```text
Initial Gate material / accepted          0 / 0
acceptance                                0.0% FAIL
failure reasons                           NO_INITIAL_MATERIAL_CANDIDATES,
                                          INITIAL_ACCEPTANCE_RATIO_BELOW_80_PERCENT
full source fetch                         11
query/search                              0 / 0
same-conversation repair                  0
score/Stage authority                     false / false
publication                               withheld
durable state                             GAP_ADJUDICATION + frozen_at
```

과거 Gate receipt는 당시 코드대로 output defect 0을 보존한다. 새 공통 Gate는 dossier가 명시한
`candidate_fact_count_withheld > 0`인데 current material이 0이면 synthetic fact를 만들지 않고
`INITIAL_PROMPT_OUTPUT_DEFECT` 하나를 추가 기록한다. sealed dossier의 read-only projection은 withheld
50, output defect 1이며 operational PASS 권한은 없다.

근본 prompt 수정은 마지막 일괄 직렬화를 금지한다.

```text
조사 시작        mandatory question skeleton 생성
source를 열 때   SourceDocument + route 즉시 append
quote 확인 때    AtomicFact + 양방향 question binding 즉시 append
후속 조사        이미 검증된 core subset 보존 후 한 건씩 추가
후보 실패        해당 후보만 gap, 기존 valid fact는 유지
도구 시간 감소   새 탐색 중지 → 현재 graph를 JSON-first로 봉인
```

source와 후보를 찾았는데 마지막 일괄 schema 검사를 못 끝냈다는 이유로 세 fact 배열을 모두 비우는 행동을
모든 36개 아키타입에서 명시적으로 금지했다. JSON을 최종 응답의 첫 번째 주 산출물로 두고 Markdown은
그 뒤 짧게만 허용한다. 특정 target·C17·롯데케미칼·후보 개수로 분기하지 않는다.

검증:

```text
exact captured V3 transport recovery             PASS
focused prompt/preflight/gate/orchestration     65/65 PASS
Initial Prompt V3 snapshots                     36/36 PASS / critical 0
Pro-first static audit                          PASS / critical 0
Pro-first V2 static audit                       PASS / critical 0
E2R v6 production static audit                  PASS / critical 0
compileall / diff check                         PASS / PASS
```

세 번째 immutable failure의 전체 hash와 old/new Gate 의미는
`p8_c17_fresh_initial_failure_receipt_r3.json`에 기록했다. 다음 C17은 이 수정 commit을 packet에 결박한
새 runtime/session/job/run/pass/conversation에서 다시 시작한다. 세 번째 conversation에는 추가 질문을
보내지 않는다.

### C17 네 번째 fresh initial — analyst subject verifier 과잉반려 봉인

전 후보 일괄 withholding 방지 수정 commit과 독립 CI green을 확인한 뒤, 세 번째 C17 job을 predecessor로
봉인하고 네 번째 actual Pro 조사를 새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T223036Z
fresh session    FRESH-V2-1-C17-R4-20260825T223036Z
fresh job        PROJOB-2ceb6e7eccad3ab6e4a8446b
fresh run        PRORUN-609870c1cb8f7e5c4de98c97
initial pass     PROPASS-db2ed0ab0d2b0d93bb84b5ee
commit binding   14d0c7f24f082b19d99f2e5df508965fa3c4fdcf
conversation     6a8e17a3-44a8-83ee-92a9-e941133c33a3
submit/capture   1 / 1
automatic resend 0
prompt/response  59,254 / 122,693 chars
research elapsed 5,997.813202 seconds
report SHA-256   c36b18248c1a7db2229aca6f97d2e5ecb8f1d5649a9d453f6db3f836f253f9ea
```

Pro는 이전 실행처럼 후보 전부를 버리지 않고 `10 material / 9 counter / 7 resolution`, source 7개,
question 26개, route receipt 26개를 실제 JSON graph에 보존했다. 26개 질문 중 23개가 terminal이고 3개
`PUBLIC_SEARCHABLE`이 남아 `NEEDS_PUBLIC_GAP_CLOSURE`로 정직하게 끝났다.

```text
serialized material                         10
excluded HISTORICAL_ONLY                     4
current material / accepted                6 / 4
acceptance                              66.6667% FAIL
output contract defect                        0
query/search                               0 / 0
score/Stage authority              false / false
publication                          withheld
```

두 current material과 counter 하나는 source fetch, date, exact quote까지 통과했지만 subject가
`KB증권의 롯데케미칼 추정`, `iM증권의 롯데케미칼 가치평가`처럼 구조화된 관계 라벨이라는 이유로
`REJECTED_WRONG_SUBJECT`가 됐다. 원문에는 대상명·종목코드와 quote가 실제로 존재하지만 그 합성 라벨
전체가 글자 그대로 나오지 않아 생긴 verifier 과잉반려다.

공통 verifier는 non-issuer structured subject가 target alias를 포함하고, 이미 literal 검증된 quote의 앞뒤
2,000자 bounded context에도 같은 target alias가 있을 때만 target analyst fact를 인정하도록 고쳤다.
target 언급이 멀리 떨어진 다중 회사 문서는 계속 `WRONG_SUBJECT`로 막는다. 쉬운 예로 문서 첫머리에
`롯데케미칼(011170) 주가전망`이 있고 바로 뒤에 `2026년 EPS 추정치 +15%`가 있으면 같은 대상 분석이다.
반대로 5,000자 앞에 롯데케미칼이 한 번 나오고 quote는 비교기업 얘기면 통과하지 않는다.

네 번째 immutable capture와 내려받은 7개 원문을 `/tmp` projection에서 재검증한 결과는 다음과 같다.

```text
all fact candidates / accepted                26 / 20
current material / accepted                     6 / 6
acceptance                                     100% PASS
genuine semantic repair                           0
query/search                                   0 / 0
read-only Gate projection                       PASS
projection receipt b1524db518f1d5d50d71acdd2a3339c84c22684ab73b922cff9c92d761aaba7b
```

과거 FAIL receipt는 덮어쓰지 않았고 projection에는 operational 권한이 없다. 전체 ID, hash, old/new Gate와
과잉반려 근거는 `p8_c17_fresh_initial_failure_receipt_r4.json`에 봉인했다. source verification semantics는
`e2r_pro_source_verification_v11`로 올린다. 회귀·정적 감사·CI green 뒤 새 conversation에서 실제 C17
initial PASS를 다시 증명하며 네 번째 conversation에는 어떤 추가 입력도 보내지 않는다.

코드 변경 후 로컬 검증은 다음과 같이 닫혔다.

```text
source/local-preflight/Gate/known-bad focused   72/72 PASS
Playwright 직접 실행 6 modules              79/79 PASS
전체 unittest                                 7,698 PASS
failure / error / skipped                        0 / 0 / 38
Pro-first static audit                         PASS / critical 0
Pro-first V2 static audit                      PASS / critical 0
E2R v6 production static audit                 PASS / critical 0
compileall / git diff check                     PASS / PASS
```

첫 전체 실행의 browser 60 ERROR는 assertion 실패가 아니라 WSL에
`libnspr4.so`, `libnss3.so`, `libasound.so.2`가 없어 Chromium이 시작 전 종료된 환경 실패였다.
관리자 인증이 필요한 시스템 설치 대신 공개 Ubuntu 패키지를 `/tmp/e2r-playwright-deps`에만 풀고
`LD_LIBRARY_PATH`로 테스트 Chromium에 연결했다. 그 후 browser 79개와 전체 7,698개가 모두
통과했다. Windows ChatGPT 로그인 프로필과 봉인된 C17 대화는 변경하지 않았다.

## 2026-08-26 — C17 다섯 번째 fresh initial은 짧은 인용의 dossier 일괄 반려를 드러냄

네 번째 C17 실패 원인의 공통 verifier 수정과 독립 CI green을 확인한 뒤, 다섯 번째 actual Pro 조사를
새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T010453Z
fresh session    FRESH-V2-1-C17-R5-20260826T010453Z
fresh job        PROJOB-6ed24292874ceae06e5e7f27
fresh run        PRORUN-10f8b5284f7fe8bd52ca12d8
initial pass     PROPASS-25f410895f717db11ff4fe5a
commit binding   e8f0b25c8d6858bd6bf0b5d0b998f3b540c20c43
conversation     6a8e3c60-3b58-83ee-ad02-e81700c63463
submit/capture   1 / 1
automatic resend 0
prompt/response  59,254 / 148,393 chars
research elapsed 3,812.572911 seconds
report SHA-256   c9fe840b8923d5b8f210608abaed306943a78a02cb8db4ec9fffeb9e48700fd3
```

Pro 응답 캡처와 canonical conversation 복구는 성공했다. 그러나 import schema가 첫 counterfact의
`supporting_excerpt="정기보수 영향"`을 8자 미만이라는 이유만으로 거절해 initial efficiency Gate까지
도달하지 못했다. 이때 실제 응답에는 source 9개와 fact 33개가 있었다.

```text
source documents                       9
material / counter / resolution    12 / 15 / 6
all facts                              33
derived metrics                         1
questions / routes                 26 / 26
short nonempty excerpt                  1
actual import verdict                FAIL
```

이 실패는 Pro 자료 부족이나 파싱 누락이 아니라 pre-downstream schema의 일괄 반려다. 쉬운 예로 33개
후보 중 `정기보수 영향` 한 줄이 7자라는 이유로 33개 전체를 버린 셈이다. initial dossier와 compact
repair schema는 이제 `supporting_excerpt`가 비어 있지 않으면 후보 graph를 보존한다. 빈 문자열은 계속
거절한다. 1~7자 후보는 자동 증거 승격되지 않으며 기존 literal source verifier가 fact 단위로 보류·거절한다.
따라서 나머지 dossier를 살리면서 점수 안전성은 유지한다.

R5 immutable capture를 새 schema로 읽기 전용 projection한 결과는 다음과 같다.

```text
schema projection                      PASS
source / all facts                   9 / 33
material / counter / resolution    12 / 15 / 6
questions / routes                 26 / 26
query / fetch                         0 / 0
operational Gate authority              false
projection hash       1809818ec02bdf546e2741e1275ae33e1305fd1218e6c55a03ea10eccf39fc5f
```

이 projection으로 R5를 소급 PASS 처리하지 않았다. R5 job은
`FRESH_SESSION_DIAGNOSTIC_ONLY / NEW_CONVERSATION_REQUIRED`로 봉인했고 같은 conversation에는 어떤
추가 입력도 보내지 않는다. 전체 ID, hash와 immutable 실패는
`p8_c17_fresh_initial_failure_receipt_r5.json`에 기록했다.

공통 schema와 36개 prompt snapshot을 갱신한 뒤 로컬 검증은 다음과 같이 닫혔다.

```text
focused dossier/preflight/repair tests          56/56 PASS
Initial Prompt V3 snapshots                     36/36 PASS / critical 0
전체 unittest                                   7,701 PASS
failure / error                                   0 / 0
Pro-first static audit                           PASS / critical 0
Pro-first V2 static audit                        PASS / critical 0
E2R v6 production static audit                  PASS / critical 0
compileall / git diff check                      PASS / PASS
```

다음 실제 C17 검문은 이 schema hash가 반영된 commit과 CI green을 먼저 확인한 뒤, 여섯 번째 새
conversation에서 수행한다. R5 raw capture와 중앙 ledger는 수정하지 않는다.

## 2026-08-26 — C17 R6 전송 전 predecessor denylist 경계를 보완

짧은 인용 일괄 반려 수정 commit `953eede0ae6b81dddce19277aa4661f4b4c6ef2f`를 push한 뒤 같은
head의 독립 CI 세 개가 모두 성공했다.

```text
push Pro-first CI       32923567286 SUCCESS
PR Pro-first CI         32923570626 SUCCESS
E2R v6 offline CI       32923570621 SUCCESS
PR #7 state             Draft / Open / Mergeable
```

그 뒤 C17 R6을 위한 새 runtime/session을 준비했지만 ChatGPT 전송보다 앞선 old-answer leakage
manifest 단계에서 멈췄다. R5는 schema import 전에 캡처는 완료했지만
`research_passes/effective_dossier.latest.json`은 만들지 못한 diagnostic predecessor다. 기존 manifest
builder가 verifier-complete predecessor만 가정해 이 파일을 무조건 열었다.

```text
intended runtime     C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T025720Z
intended session     FRESH-V2-1-C17-R6-20260826T025720Z
fresh runtime/job/run/pass/conversation created   0 / 0 / 0 / 0 / 0
upload/composer fill/submit/capture                0 / 0 / 0 / 0
automatic resend                                      0
R5 ledger mutation                                     0
actual Pro initial attempt                              0
```

따라서 이 사건은 C17 initial efficiency Gate 실패가 아니라 전송 전 boundary 진단이다. 위 intended
identity는 감사용으로 폐기하고 실제 R6에는 새 timestamp를 사용한다.

공통 manifest builder는 verifier-complete predecessor에서는 기존 effective dossier를 계속 우선한다.
그 파일이 없는 schema-failed predecessor에서만 `READY.json`, capture receipt identity와 전체 capture
bundle SHA-256을 모두 확인한 뒤 기존 bounded `ResearchDossierParser`로 캡처 JSON을 읽는다. 여기서
읽은 값은 오직 이전 answer token denylist에만 들어가며 source verification, score, Stage 권한은 없다.
쉬운 예로 R5의 `PROFACT-C01`이라는 이름이 새 packet에 우연히 복사되는지는 막지만, 그 fact를 새
증거 또는 점수로 인정하지는 않는다. 캡처 JSON을 한 글자라도 바꾸면 hash mismatch로 실패한다.

실제 R5 캡처에 대한 읽기 전용 manifest projection은 다음과 같다.

```text
old fact ids              33
old route receipt ids     26
old research pass ids      1
old question answers      26
expected source URLs      14
expected fact ids         33
score / Stage authority  false / false
```

수정 후 검증:

```text
focused fresh orchestration                    21/21 PASS
tampered capture rejection                         PASS
전체 unittest                                  7,702 PASS
failure / error / skipped                    0 / 0 / 38
Pro-first static audit                    PASS / critical 0
Pro-first V2 static audit                 PASS / critical 0
E2R v6 production static audit            PASS / critical 0
compileall / git diff check                PASS / PASS
```

전체 identity와 zero-submit 증거는
`p8_c17_fresh_pre_submit_boundary_failure_receipt_r6.json`에 기록했다. 다음 actual R6은 이 수정 commit과
독립 CI green을 확인한 뒤 새 runtime/session/job/run/pass/conversation에서 정확히 한 번만 보낸다.

## 2026-08-26 — C17 여섯 번째 actual fresh initial 100% PASS

전송 전 boundary 수정 commit `b4493b26e9f1aadbc3789ff0bda70b14122f6895`와 독립 CI 세 개가 모두
SUCCESS인 것을 확인한 뒤, 폐기한 pre-submit identity와 다른 새 runtime/session에서 C17 actual Pro
조사를 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T033612Z
fresh session    FRESH-V2-1-C17-R6-20260826T033612Z
fresh job        PROJOB-41ec024bdbc0c9c8d56c9d05
fresh run        PRORUN-b9e5878d77b712aa7a378561
initial pass     PROPASS-6a68e3062040f1f73f6d9487
commit binding   b4493b26e9f1aadbc3789ff0bda70b14122f6895
conversation     6a8e5f55-a7f8-83e8-bd89-82c1e4529916
submit/capture   1 / 1
automatic resend 0
prompt/response  59,254 / 120,503 chars
research elapsed 3,665.403214 seconds
total elapsed    3,732.263675 seconds
report SHA-256   e71dabb85fba62901fbe8ad6089cd5782f7de7b6d826b774e70d0c30f7bf0364
```

ChatGPT 결과 카드의 JSON을 실제 capture bundle에 저장했고 importer는
`parser_source=DOWNLOADED_JSON`으로 읽었다. 보고서 MD는 visible report를 보존하는 별도 감사 산출물이고,
선택 PDF는 요청하지 않아 `null`이며 오류도 없다. 쉬운 예로 JSON은 계산기에 넣는 구조화 입력이고 MD는
사람이 당시 답변을 다시 읽는 영수증이다. 둘 중 하나를 예전 대화 파일과 혼동해 선택하지 않았다.

Pro dossier는 source 8개와 fact 26개를 만들었다. material 15개 중 7개는 `as_of_date` 현재 판단이 아닌
historical-only 자료라 efficiency 분모에서 제외했다. 남은 current material 8개는 preflight와 source
verification 후 8개 모두 승인됐다.

```text
source documents                               8
material / counter / resolution          15 / 8 / 3
all facts                                     26
historical-only material excluded              7
current material / accepted                8 / 8
post-preflight acceptance                    100% PASS
mandatory question coverage               26 / 26
search route receipts                          34
genuine semantic repair                         0
repair pass / deferred batch                 0 / 0
output contract defect                          0
query / search                               0 / 0
source fetch                                    8
score / Stage authority              false / false
publication                          withheld
```

여기서 `100% PASS`는 C17 초기 조사 효율 검문 통과이며 점수나 Stage 확정이 아니다. 예를 들어 질문 26개가
모두 dossier에 답을 갖고 current material 8개가 검증됐어도, 남은 public/parser gap을 닫고 7 component와
21 Judge를 계산하기 전에는 운영 점수를 게시하지 않는다. 그래서 job은 `GAP_ADJUDICATION`, publication은
withheld, score/Stage authority는 false를 유지한다.

DB와 파일을 교차 확인한 결과 job은 `submit_count=1`, `capture_count=1`, `last_error=null`이고 initial pass는
`COMPLETE`다. capture receipt, downloaded JSON, normalized dossier, source verification, efficiency receipt의
identity와 hash는 `p8_c17_fresh_initial_success_receipt_r6.json`에 기록했다. raw 보고서, source page, 중앙
ledger는 Git에 넣지 않는다. 다음 단계는 완전히 다른 새 conversation에서 C28 initial canary를 실행하는
것이다.

## 2026-08-26 — C28 첫 fresh initial은 비공개 종결 근거 1개 누락으로 봉인

C17 R6의 100% PASS와 commit `dca86ae95f1356bcbd95c7e6202ca1b0e622b162`의 독립 CI green을 확인한
뒤, C17과 다른 종목·아키타입인 안랩 C28 actual Pro 조사를 새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T050004Z
fresh session    FRESH-V2-1-C28-R1-20260826T050004Z
fresh job        PROJOB-8df8121eb03759d7f8a883ac
fresh run        PRORUN-584b325f46a1fc5d02249a1a
initial pass     PROPASS-df09bfe4987bc857a1a42780
commit binding   dca86ae95f1356bcbd95c7e6202ca1b0e622b162
conversation     6a8e72fe-b6fc-83e8-9c03-b760986e7d78
submit/capture   1 / 1
automatic resend 0
prompt/response  60,479 / 129,708 chars
```

ChatGPT 결과 카드에서 JSON을 실제로 내려받아 `parser_source=DOWNLOADED_JSON` 경로로 연결했다. MD는
사람이 읽는 감사용 보고서이고 선택 PDF는 요청하지 않았다. 즉 이번 실패는 다운로드 버튼이나 MD/JSON
선택 문제가 아니다. JSON에는 source 6개, fact 37개, mandatory question 27개, route receipt 32개가
보존됐다.

strict schema가 멈춘 곳은 C28 Q02 하나다. Pro는 이 질문을 `LIKELY_NONPUBLIC`으로 표시하고 성공한
검색 경로 2개를 연결했지만, 그중 한 경로의 `no_new_route_reason`이 비어 있었다.

```text
failing question                         C28...Q02
claimed status                    LIKELY_NONPUBLIC
linked routes / SUCCESS                    2 / 2
route missing no-new-route reason              1
actual import                                 FAIL
initial efficiency Gate reached             false
score / Stage authority             false / false
publication                           withheld
```

쉬운 예로 “공개자료에서 못 찾았다”는 기록만 있고 “공식 공시 범위상 왜 더 볼 경로가 없는가”가 한 경로에
없으므로 `비공개로 종결`할 수 없다. 그렇다고 없는 이유를 코드가 만들어 넣어서도 안 된다. 공통
pre-schema normalizer는 이런 terminal absence/nonpublic 주장을 `PUBLIC_SEARCHABLE`,
`adequate_search_proven=false`로 한 방향 하향하고, mandatory question이면 dossier 상태도 우선순위에 맞춰
`NEEDS_PUBLIC_GAP_CLOSURE`로 되돌리도록 수정했다. 이미 모든 경로에 이유가 있는 정상
`LIKELY_NONPUBLIC`은 그대로 보존한다. 종목명·C28·질문 ID 조건은 사용하지 않았다.

R1 immutable JSON을 수정 코드에 읽기 전용으로 투영한 결과는 source 6개와 fact 37개를 그대로 보존한 채
strict V3 schema를 통과했다. 이 projection에는 initial efficiency Gate, score, Stage, publication 권한이
없으며 R1을 소급 PASS 처리하지 않는다. R1 job은 state version 15에서 다음 disposition으로 봉인했다.

```text
FRESH_SESSION_DIAGNOSTIC_ONLY
OPERATIONAL_EFFICIENCY_GATE_FAILED
NEW_CONVERSATION_REQUIRED
same-conversation follow-up / automatic resend   0 / 0
```

회귀검사는 근거 없는 `LIKELY_NONPUBLIC` 하향, 정상 종결 보존, 근거 없는 evaluated absence 하향,
이유 미생성을 함께 확인했다. local preflight 31개와 dossier/status/saturation/prompt focused 72개가 모두
통과했다. 전체 ID, hash, raw/projection 경계와 봉인 증거는
`p8_c28_fresh_initial_failure_receipt_r1.json`에 기록했다. 전체 테스트·정적 감사·독립 CI green을 먼저
확인한 뒤에만 두 번째 완전 새 C28 conversation을 시작한다.

수정 후 로컬 검증은 다음과 같이 닫혔다.

```text
local preflight focused                              31/31 PASS
dossier/status/saturation/prompt focused             72/72 PASS
실제 C28 R1 JSON read-only strict projection             PASS
전체 unittest                                       7,705 PASS
failure / error / skipped                         0 / 0 / 38
Phase100                                             15/15 PASS
Pro-first static audit                        PASS / critical 0
Pro-first V2 static audit                     PASS / critical 0
E2R v6 production static audit                 PASS / critical 0
compileall / git diff check                          PASS / PASS
```

첫 전체 실행에서 브라우저 테스트가 낸 ERROR는 코드 실패가 아니라 `/tmp`에 풀어 둔 Chromium 공유
라이브러리의 상위 경로를 잘못 지정한 실행 환경 오류였다. 실제 경로
`/tmp/e2r-playwright-deps/root/usr/lib/x86_64-linux-gnu`로 브라우저 어댑터 25개를 먼저 통과시킨 뒤,
전체 7,705개를 처음부터 새로 실행해 failure/error 0을 확인했다. 중단한 환경 오류 실행은 위 최종 수치에
합산하지 않았다.

## 2026-08-26 — C28 두 번째 fresh initial은 다른 질문 route 오결박으로 봉인

C28 R1 수정 commit `b136f02bdae86587bef4eb65159ff8011bee8423`의 독립 CI 세 개가 모두
SUCCESS인 것을 확인한 뒤, R1과 다른 runtime/session/conversation에서 C28 actual Pro 조사를 정확히 한
번 전송했다. 일반 Chat의 Pro 모드이며 legacy Deep Research 전송은 사용하지 않았다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T073534Z
fresh session    FRESH-V2-1-C28-R2-20260826T073534Z
fresh job        PROJOB-92a788cb99d245f007457792
fresh run        PRORUN-7c3e60dacd5b3ea2e022d1df
initial pass     PROPASS-fbc13f5eb3f4c9e20d8af44c
commit binding   b136f02bdae86587bef4eb65159ff8011bee8423
conversation     6a8e975e-fd30-83ee-9f62-cfaf58836274
submit/capture   1 / 1
automatic resend 0
```

ChatGPT 결과 카드의 JSON을 실제로 내려받아 `parser_source=DOWNLOADED_JSON`으로 읽었다. visible DOM의
원본에는 JSON 문자열 안 raw control character 35개가 있었고, 기존 bounded parser가 의미를 바꾸지 않고
JSON escape만 적용했다. MD 실다운로드·새 JSON·선택 PDF 경계도 유지됐고 PDF는 요청하지 않아 `null`이다.
즉 이번에도 예전 MD를 잘못 집어온 문제가 아니다.

다운로드 JSON에는 source 6개, fact 11개, mandatory question 27개와 route receipt 17개가 있었다. strict
schema는 question row 15개가 자기 질문이 아닌 route receipt ID를 참조해 Gate 전에 멈췄다. 주로 공통 R13
cross-guard 질문에서 C28 본 질문 또는 이웃 질문의 route를 재사용한 경우였다.

```text
source documents                               6
material / counter / resolution          7 / 4 / 0
all facts                                     11
mandatory questions / route receipts      27 / 17
derived metrics / unresolved gaps          3 / 11
research status          NEEDS_PUBLIC_GAP_CLOSURE
actual import                              FAIL
initial efficiency Gate reached            false
score / Stage authority            false / false
publication                          withheld
```

쉬운 예로 Q02가 “Q03 검색에서 이 URL을 봤다”는 영수증을 자기 영수증처럼 연결한 상태다. URL과 자료를
삭제할 이유는 없지만, 그 영수증으로 Q02 검색이 충분했다고 증명할 수는 없다. 공통 pre-schema normalizer는
각 question이 정확히 같은 `archetype_id × question_family_id` 소유 route만 보존하도록 수정했다. unknown,
foreign, duplicate link는 해당 question에서만 제거하고 `adequate_search_proven=false`로 되돌린다. 전역
route receipt와 모든 fact는 그대로 보존한다. 종목·C28·질문 ID 하드코딩은 없다.

R2 immutable JSON을 parser → 공개 dialect adapter → pre-schema normalizer → transport identity binding →
strict V3 validator 순서로 읽기 전용 투영한 결과는 PASS다.

```text
initial placeholder alias normalization          1
source / route URL canonicalization           2 / 3
foreign question route links removed             15
source / facts / questions / global routes  6 / 11 / 27 / 17
research status          NEEDS_PUBLIC_GAP_CLOSURE
Gate / score / Stage authority      false / false / false
```

이 projection으로 R2를 소급 PASS 처리하지 않았다. R2 job은 state version 15에서
`FRESH_SESSION_DIAGNOSTIC_ONLY / OPERATIONAL_EFFICIENCY_GATE_FAILED / NEW_CONVERSATION_REQUIRED`로 봉인했고,
같은 conversation에는 후속 입력이나 자동 재전송을 하지 않는다. 전체 실행 identity, artifact hash, 오류와
봉인 증거는 `p8_c28_fresh_initial_failure_receipt_r2.json`에 기록했다.

수정 후 검증은 다음과 같이 닫혔다.

```text
focused dossier/preflight/fresh tests              182/182 PASS
전체 unittest                                      7,707 PASS
failure / error / skipped                        0 / 0 / 38
Phase100                                            15/15 PASS
Pro-first static audit                       PASS / critical 0
Pro-first V2 static audit                    PASS / critical 0
E2R v6 production static audit                PASS / critical 0
compileall / git diff check                         PASS / PASS
```

다음 단계는 이 범용 수정을 한글 commit으로 push하고 독립 CI green을 확인한 뒤, 세 번째 완전 새 C28
conversation에서 actual initial canary를 한 번만 전송하는 것이다. R2 raw capture와 중앙 ledger는 수정하지
않는다.

## 2026-08-26 — C28 R3와 P9 다중 아키타입 fresh-session 검문 통과

C28 R2 범용 수정 commit `fdac32990ba8d29fb6b596c6f5bbb8d5a372538e`의 독립 CI 세 개가 모두
SUCCESS인 것을 확인한 뒤, R1/R2와 다른 runtime/session/conversation에서 안랩 C28 actual Pro 조사를
정확히 한 번 전송했다. 일반 Chat의 Pro 모드이며 legacy Deep Research를 사용하지 않았다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T091553Z
fresh session    FRESH-V2-1-C28-R3-20260826T091553Z
fresh job        PROJOB-e3d57e985cd3a1617b717ccd
fresh run        PRORUN-d0f7e7834ed81f0c9bb324a1
initial pass     PROPASS-13e168efd50ba39ed8e94102
conversation     6a8eaee3-d670-83ee-9c01-6f7d438db2f0
submit/capture   1 / 1
automatic resend 0
prompt/response  60,479 / 116,288 chars
research elapsed 3,678.863673 seconds
total elapsed    3,738.385957 seconds
```

ChatGPT 결과 카드에서 새 JSON을 실제로 다운로드해 `parser_source=DOWNLOADED_JSON`으로 import했다.
JSON 문자열 안 raw control character 84개는 bounded parser가 escape만 적용했고, source/fact 의미는
바꾸지 않았다. 예전 MD를 잘못 고른 것이 아니며 선택 PDF는 요청하지 않아 `null`이다.

```text
source documents                              9
all facts                                    22
initial current material candidate/accepted 10 / 10
post-preflight acceptance ratio             100%
mandatory question coverage                 27 / 27
verified/compiled facts                         17
genuine repair candidate / actual pass       0 / 0
query / search / fetch                       0 / 0 / 9
score / Stage authority                      false / false
publication                                  withheld
initial efficiency Gate                      PASS
```

R3 job은 `GAP_ADJUDICATION`, dossier는 `NEEDS_PUBLIC_GAP_CLOSURE`다. 이 PASS는 C28 초기 조사 효율
통과이지 최종 점수나 Stage가 아니다. 전체 identity, artifact hash, parser operation, source verification과
Gate 수치는 `p8_c28_fresh_initial_success_receipt_r3.json`에 고정했다. raw report, downloaded JSON,
source page와 중앙 ledger는 Git에 넣지 않는다.

P9에서는 동결 구 실행과 세 fresh 실행을 `fresh_session_comparison.json/.md`로 비교했다. 새 독립 감사기는
비교표의 자기주장을 믿지 않고 다섯 source receipt를 다시 읽어 합계와 hard-zero counter를 계산한다.

```text
fresh archetypes / conversations            3 / 3
initial material candidate/accepted        36 / 34
aggregate acceptance ratio                94.4444%
mandatory question coverage                81 / 81
verified facts                                    56
actual Pro repair pass                              0
required hard-zero counters                    13/13
fresh efficiency audit               PASS / critical 0
audit hash       47d96d1f3b602ef0b963ce3772ffc70cbacdb655fb399aefdcf0a61fb9b87b6a
```

동결 구 실행은 11 pass, prompt defect 50개, local/verifier defect 24개였고 마지막 source verification은
53 fact를 accepted/compiled했다. 다만 구 pipeline은 initial acceptance 경계와 11 pass 전체 문자 telemetry를
보존하지 않았으므로 comparison에는 `null`과 이유를 남겼다. 서로 source corpus가 달라 score parity도
금지했다.

현재 verdict는 verifier-ready pipeline, C06, C17, C28, multi-archetype fresh session까지 PASS다. 세 live
canary에는 공개자료/parser gap 합계 41개가 남아 있고 score/Stage publication 권한도 없으므로
`operational_research_readiness=WITHHELD_FULL_THESIS_PENDING`을 유지한다. 즉 초기 효율 검문을 최종 thesis
완료로 과장하지 않는다.

P9 코드·영수증·문서 작성 후 로컬 검증은 다음과 같이 닫혔다.

```text
P9 fresh efficiency focused tests                   5/5 PASS
Linux headless browser tests                       79/79 PASS
전체 unittest                                     7,712 PASS
failure / error / skipped                       0 / 0 / 38
Phase100                                           15/15 PASS
Gate 1 tracked receipt                               4/4 PASS
Pro-first static audit                     PASS / critical 0
Pro-first V2 static audit                  PASS / critical 0
Pro-first V2 static audit hash 0928a78b0411df4e885760d24be84d6a53edad45613963c0b53146aafad07b9a
E2R v6 production static audit             PASS / critical 0
E2R v6 static audit hash       ff981d5bed53ebaec938dbcc3049c4e31a854766cd6517ac306376609c94a27a
compileall / git diff check                       PASS / PASS
```

첫 전체 실행에서 난 브라우저 ERROR 60개는 Playwright가 `libnspr4.so`를 찾지 못한 실행환경 오류였다.
`/tmp/e2r-playwright-deps/root/usr/lib/x86_64-linux-gnu`를 `LD_LIBRARY_PATH`에 연결해 브라우저 79개를
독립 통과시킨 뒤 전체 7,712개를 처음부터 다시 실행했다. 최종 실행은 failure/error 0이며 앞선 환경 오류
실행은 PASS 수치에 포함하지 않았다.

```text
final full unittest elapsed       655.522 seconds
final full unittest log sha256    9bccf1f209803306de93029cdab105aa762253c5915d594183dcc88c094eba91
```
