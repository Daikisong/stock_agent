# Pro-first Browser Platform master goal 완료 감사

## 판정

```text
implementation: PRO_FIRST_PLATFORM_IMPLEMENTATION_READY
browser shadow: CHATGPT_WEB_SHADOW_COMPATIBILITY_PASS
live canary: PRO_FIRST_LIVE_CANARY_PASS
PR: #7 Draft / OPEN / MERGEABLE
```

이 문서는 `e2r_pro_first_browser_platform_master_goal.md` 전체 3,190줄을 구현 코드,
테스트, tracked 영수증, 실제 runtime ledger와 대조한 마감 감사다. 원본 master goal의
SHA-256은 `2b61fc45889c4809b0675dd128aa815b89fd7a5bf2ccdb910f3753d741043098`이다.

판정 범위는 플랫폼 구현과 000660 단일 forced validation canary다. 전체 KRX daily
universe 또는 모든 아키타입의 무인 운영 준비를 뜻하는
`PRO_FIRST_LIVE_OPERATION_READY`는 주장하지 않는다.

쉬운 예로, “브라우저가 보고서를 다운로드했다”만으로 완료가 아니다. 이 canary는
다운로드 뒤 source 검문, gap 판정, 7 component, 21 Judge, deterministic score,
`AtomicStageCourtV2`, publication까지 같은 durable job에서 닫혔기 때문에 live
canary PASS다.

## 30개 구현 목표 대조

| # | master goal | 판정 | 주된 구현·증거 |
|---:|---|---|---|
| 1 | KRX morning/evening scheduler | PASS | `scheduler.py`, scheduler 테스트 |
| 2 | candidate selection/dedupe/queue | PASS | `candidate_selector.py`, durable store |
| 3 | ResearchPacketV1 builder | PASS | `packet.py`, packet schema·blind-safe 검사 |
| 4 | local dashboard | PASS | `dashboard/app.py`, loopback API/UI 테스트 |
| 5 | one-click user approval | PASS | `approval.py`, nonce single-use |
| 6 | logged-in Chrome worker | PASS | `browser/worker.py`, CDP attach |
| 7 | ChatGPT Pro web adapter | PASS | `browser/chatgpt_adapter.py`, production adapter mock E2E |
| 8 | upload/prompt preparation | PASS | `operations.py`, prepare-without-submit |
| 9 | exactly-once submit | PASS | `ExactlyOnceSubmitCoordinator`, 실제 submit 1 |
| 10 | running/clarification/quota/error/completion | PASS | `completion_monitor.py`, stable hash 상태 검사 |
| 11 | MD-first capture | PASS | 새 MD preview/download 테스트 |
| 12 | optional PDF capture | PASS | matching PDF export 테스트 |
| 13 | direct response fallback | PASS | `DIRECT_REPORT_DOM` fallback 테스트 |
| 14 | CAPTURE_COMPLETE event | PASS | dispatcher·ledger·idempotency 테스트 |
| 15 | atomic artifact handoff | PASS | staging→incoming, `READY.json` last |
| 16 | ResearchDossierV1 importer | PASS | parser/dialect/normalizer/validator/importer |
| 17 | URL/date/quote/subject/segment/currentness | PASS | `verification/` 전체와 known-bad 테스트 |
| 18 | EvidenceFact compiler | PASS | verified lineage만 lifecycle bridge로 변환 |
| 19 | materiality-first gap adjudicator | PASS | `gaps/adjudicator.py`, exact gap policy |
| 20 | material-gap-only supplement | PASS | bounded planner/service, corroboration·monitoring 검색 0 |
| 21 | 7 component bridge | PASS | verified fact ID와 allowed edge만 사용 |
| 22 | 21 Judge evidence-only | PASS | 7×3 roster, search 권한 없음 |
| 23 | deterministic score | PASS | 기존 `ResearchCalibratedComponentScorer` 재사용 |
| 24 | deterministic StageCourt | PASS | 기존 `AtomicStageCourtV2` 재사용 |
| 25 | dashboard publication | PASS | `publication.py`, actual `PUBLISHED` |
| 26 | same-input idempotency | PASS | provider/query/fetch 0, score·Stage variance 0 |
| 27 | delta research | PASS | 1 component/3 Judge 재계산, 나머지 재사용 |
| 28 | offline/mock browser E2E | PASS | C06/C17/C28와 restart 4/4 |
| 29 | actual ChatGPT shadow lane | PASS | `live_shadow_receipt.json`, submit 0 |
| 30 | CI/audit/docs/one-command start | PASS | workflow, audit CLI, 문서, PowerShell helper |

## Hard Acceptance Gates

### Gate A — Architecture: PASS

- 기존 KRX scanner, `EvidenceFact`, Gate 1 gap model, scorer,
  `AtomicStageCourtV2`를 재사용한다.
- 새 score engine과 새 Stage engine은 0개다.
- Pro/Codex provider output schema는 score, stage, 방향, source lineage 생성을
  허용하지 않는다. 자유형 Pro MD의 “관련성 제안”은 deterministic allowed-edge와
  source-backed fact 검문을 통과해야만 계산 재료가 된다.

### Gate B — Browser: PASS

- prepare 전송 0, 승인 없는 submit 차단, nonce 1회 소비, 실제 submit/capture 1/1.
- old MD 회피, 새 MD 실다운로드, direct response fallback, optional PDF를 검증했다.
- duplicate submit, auto login, hidden API, cookie export는 모두 0이다.
- actual shadow는 logged-in dedicated Chrome에서 Pro mode와 send-ready까지만 확인하고
  submit 0으로 끝났다.

### Gate C — Downstream: PASS

```text
CAPTURE_COMPLETE → IMPORT → VERIFY → GAP → COMPONENT
→ 21 JUDGE → SCORE → STAGECOURT → PUBLISH
```

위 경로가 production runtime의 `_browser_loop()`와
`ProFirstPostImportCoordinator`에 연결돼 있다. 실제 canary job도 `FINAL / PUBLISHED`다.
승인 뒤 추가 사용자 조작은 요구하지 않는다.

### Gate D — E2E: PASS

- C06: PASS
- C17: PASS, 공백이면 보수적 pending 계약 유지
- C28: PASS
- backend restart after capture: PASS

fixture MD를 importer에 직접 넣는 shortcut이 아니라 loopback ChatGPT page를 실제
`PlaywrightChatGPTWebAdapter`로 조작한다.

### Gate E — Reuse: PASS

- same dossier browser submit 0
- new Pro research 0
- supplemental query/fetch 0/0
- score variance 0, Stage variance 0
- delta는 component 1/7, Judge 3/21만 재계산한다.

### Gate F — Scheduler/Dashboard: PASS

- KST morning 05:30, evening 18:30 simulated run PASS
- missed-window catch-up once와 dedupe PASS
- approval UI와 loopback token security PASS
- READY capture와 post-capture backend restart/resume PASS

### Gate G — Regression: PASS

```text
full unittest: 7,407, process exit 0, failure/error 0
existing conditional skip baseline: 38
new skip/xfail construct: 0
master-goal required test names: 87/87, missing 0
Pro-first core: 191/191
browser mock E2E: 47/47
golden offline E2E: 4/4
performance/reuse audit: 4/4
Phase100: 15/15
Pro-first static audit: critical 0
production static audit: critical 0
compileall / git diff --check: PASS / PASS
```

production static audit hash는
`5e3c32cbf4257235441639291fa720e338d0ce6eef12d23e8b79bcb6518067b1`이다.

## 실제 000660 canary

```text
job/run: PROJOB-70e6a50ae757bd874e602a85 / PRORUN-643c723370681970b5bcc582
target/as_of: 000660 SK하이닉스 / 2026-08-22
archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
submit/capture: 1/1
candidate facts: 35
verified facts: 26 = current 16 + counter 10
rejected facts: 9
credit-validated impacts: 33
component/Judge: 7/7, 21/21
score/interval: 23.202275 / 23.202275~23.202275
score_valid: true
Stage: 0 FINAL
publication: PUBLISHED
scoring query/fetch: 0/0
same snapshot provider calls: impact 0 / Judge 0
investment recommendation: false
```

이 점수는 Gate 1의 별도 996-current-fact snapshot인 `70.2 / Stage 2`와 입력이
다르다. 예를 들어 시험지가 996개 fact인 경우와 이번 Pro 문서에서 검문을 통과한
26개 fact인 경우는 같은 회사여도 점수가 같을 필요가 없다.

## Git·CI·안전성

- base main: `b408b0b6887ea3ca20367a3dc64f543263cd123f`
- branch: `feature/e2r-pro-first-browser-platform-20260822`
- PR: <https://github.com/Daikisong/stock_agent/pull/7>
- Draft/open/mergeable을 유지하며 master goal 지시대로 main에 병합하지 않는다.
- closing 변경 전 head `ffab5f442d96976ca4272365ed43c9b8ff5fe99b`의
  [Pro-first workflow](https://github.com/Daikisong/stock_agent/actions/runs/32582592647)와
  [v6 offline contract](https://github.com/Daikisong/stock_agent/actions/runs/32582592635)는
  SUCCESS다.
- 이 문서를 포함하는 새 PR head는 push 후 같은 workflow의 SUCCESS를 최종 authority로
  삼는다. 문서 안에 자기 commit SHA를 넣어 무한히 SHA가 바뀌는 구조는 만들지 않는다.
- `output/`, `.e2r_cache/`, `data/cache/` 신규 tracked 경로는 0개다.
- 실제 MD, screenshot, SQLite, Chrome profile, cookie는 Git에 넣지 않았다.

## 외부 검수 진입점

1. 이 문서에서 30개 목표와 Gate A~G를 확인한다.
2. `live_shadow_receipt.json`에서 전송 전 compatibility와 submit 0을 확인한다.
3. `live_canary_acceptance_2026-08-22.json`에서 actual hash·score·Stage·재사용 수치를
   확인한다.
4. `implementation_progress_2026-08-22.md`에서 실패 원인과 수정 순서를 확인한다.
5. `offline_e2e_result.json`, `browser_mock_e2e_result.json`,
   `performance_audit.json`, `static_audit.json`을 독립 재실행 영수증으로 확인한다.
6. PR #7 current head의 GitHub Actions가 모두 green인지 확인한다.

## 미해결 blocker

없다. 다만 단일 forced validation canary 밖의 전체 daily universe 운영 확대는 이번
master goal 완료 판정의 범위가 아니며 별도 승인·검증 없이 자동으로 주장하지 않는다.
