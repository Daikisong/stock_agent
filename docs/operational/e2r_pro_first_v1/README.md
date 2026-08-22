# E2R Pro-first 브라우저 운영 플랫폼

이 디렉터리는 `SCAN → SELECT → PACKET → PREPARE → APPROVAL → SUBMIT → MONITOR → CAPTURE → IMPORT → VERIFY → GAP → COMPONENT → JUDGE → SCORE → STAGECOURT → PUBLISH` 인수 근거를 모은다.

핵심 경계는 단순하다. ChatGPT Pro는 자료를 조사해 dossier를 만들지만 점수와 Stage는 결정하지 않는다. 예를 들어 Pro 보고서가 “Stage 3-Green”이라고 써도 importer가 그 값을 점수 입력으로 사용하지 않고, 검증된 `EvidenceFact`와 기존 deterministic scorer·`AtomicStageCourtV2`만 최종 상태를 만든다.

## 시작

Windows PowerShell:

```powershell
.\scripts\start_e2r_pro_first_stack.ps1
```

Python:

```bash
cp configs/e2r_pro_first_local.example.yaml configs/e2r_pro_first_local.yaml
PYTHONPATH=src python -m e2r.cli.run_e2r_pro_first_stack \
  --config configs/e2r_pro_first_local.yaml
```

한 명령이 SQLite migration, KST 05:30/18:30 scheduler, loopback dashboard, CDP browser worker, capture reconciliation을 시작한다. ChatGPT 로그인은 전용 Chrome에서 사용자가 직접 한다. Dashboard가 승인 nonce를 원자적으로 소비하기 전에는 DOM 전송 경로가 열리지 않는다.

Chrome 151처럼 `/json/version` 대신 `DevToolsActivePort`를 쓰는 환경은 로컬 설정의 `browser.cdp_active_port_file`에 전용 profile의 해당 파일 경로를 지정할 수 있다. worker는 그 파일의 loopback WebSocket capability를 접속 순간 메모리에서만 읽고 config·receipt에는 기록하지 않는다. 기본 Chrome의 profile/cookie를 복사하지 않으며, PowerShell helper는 외부 LAN이 아닌 `127.0.0.1`에만 CDP를 연다.

전용 Chrome이 로그인 화면이면 자동 로그인하지 않고 job을 `USER_ATTENTION_REQUIRED`로 보존한다. 예를 들어 평소 쓰는 Chrome에서 ChatGPT가 로그인되어 있어도 그 cookie를 전용 profile로 복사하지 않는다. 사용자가 전용 창에서 한 번 로그인하면 같은 durable job을 다시 준비하므로 canary가 중복 생성되지 않는다.

## 자동 후반 처리

capture가 끝난 뒤에는 별도 사용자 승인이 없다. runtime이 dossier를 import하고, dossier에 적힌 유한 URL만 원문 검증한 뒤, deterministic gap 판정에서 `CORE_SCORE_BLOCKER`, `STAGE_BOUNDARY_GAP`, `HARD_BREAK_GAP`으로 확인된 공백만 `3 query / 20 candidate / 6 fetch` 이내에서 보충한다. query 문장은 LLM이 만들고 코드는 회사 범위·연도·미래누수·중복만 검증한다. `CORROBORATION_CAP`과 `MONITORING_GAP`은 보충 검색을 열지 않는다.

검증된 fact는 기존 impact validator, 7개 component, evidence-only 21 Judge, `ResearchCalibratedComponentScorer`, `AtomicStageCourtV2`를 차례로 지난다. 예를 들어 Judge provider가 실패하면 해당 job은 pending에 머물며 `0점 Stage 0`을 정상 결과처럼 게시하지 않는다.

현재 canary 최종 handoff는 [live_pilot_handoff.json](live_pilot_handoff.json), 실제
결과와 hash는 [live canary acceptance](live_canary_acceptance_2026-08-22.json), 작업
순서와 실패·수정 이력은 [구현 진행 기록](implementation_progress_2026-08-22.md)에
있다. [live shadow receipt](live_shadow_receipt.json)은 전용 logged-in Chrome에서
packet·prompt·Pro 모드가 전송 직전까지 준비되고 실제 전송은 0회였던 compatibility
PASS를 기록한다. 전용 profile 로그인 전에는 승인 nonce를 발급하거나 send 버튼을
누르지 않는 원칙은 그대로 유지된다.

## 오프라인 검증

```bash
PYTHONPATH=src python scripts/run_e2r_pro_first_offline_ci.py \
  --repo-root . --output /tmp/pro_first_ci.json --full-regression
```

CI는 실제 ChatGPT 계정이나 쿠키를 사용하지 않는다. loopback mock을 같은 `PlaywrightChatGPTWebAdapter`로 조작해 업로드, prompt, 1회 전송, 새 MD 다운로드, capture/import와 후반 deterministic 파이프라인을 검증한다.

관련 문서: [구조](architecture.md), [상태기계](state_machine.md), [보안](security.md),
[최종 readiness](final_readiness.md),
[master goal 완료 감사](master_goal_completion_audit_2026-08-23.md).
