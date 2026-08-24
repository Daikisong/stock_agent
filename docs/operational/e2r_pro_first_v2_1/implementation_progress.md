# E2R Pro-First V2.1 구현 진행 장부

기준 시각: `2026-08-25 04:30 KST`

기준 Goal:
`C:\Users\eorb9\Downloads\e2r_pro_first_v2_1_fresh_session_verifier_ready_master_goal.md`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`

부모 HEAD: `49adcb4056821d7e6a24b58e9c068dbf2092e542`

PR #7은 계속 Draft/open이며 main 병합, draft 해제, auto-merge를 하지 않는다.

## 현재 판정

```text
P0 old run freeze                         COMPLETE
P1 rejection A/B/C taxonomy              PENDING
P2 ResearchDossierV3                      PENDING
P3 Initial Prompt V3                      PENDING
P4 local preflight                        PENDING
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

## 다음 단계 P1

old runtime의 전체 rejection packet을 삭제·샘플링하지 않고 읽어 다음을 생성한다.

```text
old_run_rejection_taxonomy.json
old_run_rejection_taxonomy.md
```

각 candidate를 A `INITIAL_PROMPT_OUTPUT_DEFECT`, B `LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT`,
C `GENUINE_SEMANTIC_OR_SOURCE_DEFECT`로 분류하고, 같은 source/중복 mechanical rejection과
실제 Pro semantic repair 수를 따로 집계한다. 이 taxonomy가 끝나기 전 fresh conversation은
만들지 않는다.
