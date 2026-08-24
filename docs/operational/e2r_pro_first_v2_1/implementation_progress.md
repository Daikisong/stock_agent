# E2R Pro-First V2.1 구현 진행 장부

기준 시각: `2026-08-25 P4 완료 검증 시점`

기준 Goal:
`C:\Users\eorb9\Downloads\e2r_pro_first_v2_1_fresh_session_verifier_ready_master_goal.md`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`

phase commit 계보:

```text
P0 b6c30eb9  기존 repair-heavy Pro 실행을 진단 자료로 봉인
P1 10c7269b  Pro fact 반려 원인을 최초 출력·로컬 결함·의미 결함으로 분해
P2 152db6a7  source 문서와 atomic fact를 분리한 검증 친화 dossier를 도입
P3 d5d62bc2  최초 Pro 조사에서 verifier-ready 증거를 생성하도록 계약 강화
P4 이 문서와 함께 local evidence preflight phase commit으로 고정
```

PR #7은 계속 Draft/open이며 main 병합, draft 해제, auto-merge를 하지 않는다.

## 현재 판정

```text
P0 old run freeze                         COMPLETE
P1 rejection A/B/C taxonomy              COMPLETE
P2 ResearchDossierV3                      COMPLETE
P3 Initial Prompt V3                      COMPLETE
P4 local preflight                        COMPLETE
P5 compact RepairDeltaV3                  PENDING
P6 fresh-session orchestration            PENDING
P7 000660 fresh canary                    PENDING
P8 C17/C28 fresh canary                   PENDING
P9 final CI/audit                         PENDING
```

아직 선언할 수 있는 최종 verdict는 없다. 특히 old run을 완료한 것으로 간주하거나
`PRO_FIRST_V2_1_OPERATIONAL_RESEARCH_READY`를 선언하지 않는다.

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

## 다음 단계 P5

전체 dossier를 다시 출력시키는 기존 repair 계약을 제거하고, P4가
`INITIAL_PROMPT_OUTPUT_DEFECT` 또는 `GENUINE_SEMANTIC_OR_SOURCE_DEFECT`로 분류한 material
candidate만 source별로 묶은 `RepairDeltaV3`로 수리한다. 로컬/representation 결함은 repair
payload에 들어가지 않으며 아직 실제 fresh Pro 전송은 하지 않는다.
