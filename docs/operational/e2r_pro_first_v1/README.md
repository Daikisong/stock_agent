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

## 오프라인 검증

```bash
PYTHONPATH=src python scripts/run_e2r_pro_first_offline_ci.py \
  --repo-root . --output /tmp/pro_first_ci.json --full-regression
```

CI는 실제 ChatGPT 계정이나 쿠키를 사용하지 않는다. loopback mock을 같은 `PlaywrightChatGPTWebAdapter`로 조작해 업로드, prompt, 1회 전송, 새 MD 다운로드, capture/import와 후반 deterministic 파이프라인을 검증한다.

관련 문서: [구조](architecture.md), [상태기계](state_machine.md), [보안](security.md), [최종 readiness](final_readiness.md).
