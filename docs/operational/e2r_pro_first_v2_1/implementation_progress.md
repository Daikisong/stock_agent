# E2R Pro-First V2.1 구현 진행 장부

기준 시각: `2026-08-26 P7 CI 봉인 완료 / P8 독립 C17·C28 실행 경계 검증 완료`

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
P8 실행 전 경계 commit에서 C17/C28 독립 fresh target 생성을 고정
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
P8 C17/C28 fresh canary                   IN_PROGRESS (실행 경계 PASS, live 전송 대기)
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
