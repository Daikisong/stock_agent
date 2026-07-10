# E2R Reconstruction Phase 16 — Runtime Commands and Final Audit

## 결론

Phase 16의 내부 명령 연결과 감사 장치는 완료했다.

- compile: `COMPILE_RUN_PASS`
- blind frozen replay: `HISTORICAL_REPLAY_PARITY_PASS`
- full unittest suite: 5,584/5,584 PASS
- current/Census: `EXTERNAL_SOURCE_BLOCKER_NOT_READY`
- 최종 라벨: `EXTERNAL_SOURCE_BLOCKER_NOT_READY`
- `production_runtime_ready=false`

즉, 엔진과 검증 장치는 연결됐지만 실제 2026-07-10 current 입력이 없으므로 `MEANINGFUL_E2R_RUNTIME_READY`는 선언하지 않았다.

쉬운 예로, 자동차의 엔진·브레이크·계기판 테스트는 끝났지만 오늘 도로 상태를 가져오는 센서 입력이 없는 상태다. 이때 “주행 준비 완료”라고 표시하지 않고 “외부 입력 대기”로 남긴다.

## Canonical 명령

```bash
PYTHONPATH=src python -m e2r.cli.compile_e2r_research_intelligence \
  --repo-root . \
  --output-root output/research_intelligence/v1 \
  --strict true

PYTHONPATH=src python -m e2r.cli.run_e2r_historical_replay \
  --registry canonical \
  --mode blind_frozen_replay \
  --output-root output/historical_replay/v1 \
  --fail-on-critical true

PYTHONPATH=src python -m e2r.cli.run_e2r_current_operation \
  --as-of-date 2026-07-10 \
  --mode production_bounded \
  --universe krx \
  --output-root output/current_operation/v1 \
  --fail-on-critical true

PYTHONPATH=src python -m e2r.cli.run_e2r_census_mode \
  --as-of-date 2026-07-10 \
  --mode census_selective_deep \
  --brain canonical_v1 \
  --output-root output/census_v_next \
  --fail-on-critical true
```

모든 명령은 다음 여섯 범주의 hash를 남긴다.

1. config
2. corpus
3. memory
4. recipe
5. prompt
6. source

여기에 commit hash, dirty path 목록, dirty status hash도 함께 기록한다. 예를 들어 실행 뒤 source leaf 한 글자만 바뀌어도 저장된 SHA-256과 현재 파일 hash가 달라져 재현성 감사가 실패한다.

## 실제 compile 결과

- 입력 artifact: 2,260개
- historical case: 10,920개
- historical outcome: 19,031개
- historical rule: 6,255개
- quarantine: 5,549개
- linkage error: 1,036개
- executable recipe: 31개
- explicit unsupported recipe: 158개
- semantic memory: node 25,532개 / edge 44,221개
- blind retrieval: 61개
- top-3 archetype / required recipe / positive-guard pair: 모두 1.0
- critical count: 0

source verification은 10,920개 모두 exact source repair queue에 남았다. URL이나 검증 anchor가 없는데 성공 처리하지 않았다는 뜻이다.

## 실제 blind replay 결과

- frozen as-of: 2026-06-30
- run id: `HREPLAY-ac6559e7c76e820678b48b8f`
- canonical archetype: 36/36
- top-1: 0.916667
- top-3: 1.0
- mapping precision: 1.0
- positive recall: 1.0
- guard accuracy: 1.0
- exact source blocker: 36/36
- 미래 누수: 0
- source proxy 점수 credit: 0
- current watchlist 오염: 0

여기서 exact source blocker 36은 실패를 숨긴 숫자가 아니다. 예를 들어 과거 case가 의미상 C06으로 잘 검색돼도 당시 원문 URL과 exact quote가 없으면 “분류 성공”과 “source 검증 성공”을 분리한다.

## Current/Census가 pending인 이유

정확한 blocker는 다음과 같다.

`CURRENT_KRX_UNIVERSE_AND_LIVE_SOURCE_INPUT_MANIFEST_UNAVAILABLE`

그래서 결과는 다음처럼 고정된다.

- canonical Stage: `0`
- score_valid: `false`
- raw_reference_score: `null`
- exit code: 3

저장소 지침은 별도 요청 전까지 새 live web scraping/API 연결을 추가하지 말라고 한다. 따라서 `.env`에 API key가 있다는 이유만으로 canonical 명령에 자동 live 호출을 붙이지 않았다.

나쁜 예는 “FCF source가 없지만 raw 68점이니 Stage 2”라고 내보내는 것이다. 현재 구현은 같은 상황을 “Stage 0 / Source Pending”으로 남긴다.

## Production claim provenance

production 점수나 hard break에 쓰이는 claim은 다음을 모두 가져야 한다.

- 실제 문서 URL
- 원문 전체 text와 그 SHA-256
- 원문 안에 실제로 존재하는 exact quote
- source / anchor / mapping id lineage
- published date와 available date
- CODEX extraction / mapping provider trace
- direct, current, non-proxy 상태

`snapshot://`, `example.test`, `localhost` 같은 테스트 URL은 production provenance로 거절한다. `available_date`가 `published_date`보다 빠르거나 claim 관측일보다 늦어도 거절한다.

## 독립 Reviewer A–E

- A — Corpus Fidelity: artifact 원본 hash, row/case/outcome lineage를 leaf에서 다시 계산한다.
- B — Recipe/Retrieval: recipe/unsupported 경계, memory graph, blind retrieval rate를 leaf에서 다시 계산한다.
- C — Source/Claim Realness: source blocker와 current 문서·quote·hash·fetch 경로를 직접 검사한다.
- D — Score/Stage Integrity: atomic score, canonical Stage, pending score 금지, watchlist projection을 다시 대조한다.
- E — Historical/Current Separation: planner/evaluator 분리, 미래 누수, quota/forced archetype, current 오염을 검사한다.

compile summary의 숫자를 `999999`로 바꿔도 Reviewer A는 summary를 믿지 않고 leaf를 다시 읽는다. 반대로 case leaf의 `runtime_score_eligible=false`를 `true`로 바꾸면 실패한다.

## 최종 READY 조건

`MEANINGFUL_E2R_RUNTIME_READY`는 다음이 동시에 참일 때만 가능하다.

1. Reviewer A–E가 모두 leaf 기준 PASS
2. compile/replay/current/Census 명령이 같은 현재 commit에서 PASS
3. current와 Census가 실제 fetched document와 provenance를 가짐
4. current/Census canonical leaf가 동일함
5. worktree가 clean
6. critical count와 blocker가 0

`--require-live-current false`로 검사를 끄는 것 자체가 critical이다. 검사를 껐다고 READY가 되지는 않는다.

main worktree는 사용자 변경 때문에 dirty이고, 별도 clean 검증에서도 실제 current source input은 없었다. 따라서 최종 상태를 정직하게 `EXTERNAL_SOURCE_BLOCKER_NOT_READY`로 유지한다.

### 사용자 dirty 상태와 코드 clean 검증 분리

main worktree에는 사용자가 수정·삭제한 `docs/core/goal*.md` 4개가 있어 이를 임의로 되돌리지 않았다. 대신 같은 commit을 별도 clean worktree에서 다시 실행했다.

- clean worktree `repo_dirty=false`
- compile component: PASS
- replay component: PASS
- component commit mismatch: 0
- working-tree critical: 0
- clean final audit critical sum: 30
- clean final audit status: `EXTERNAL_SOURCE_BLOCKER_NOT_READY`

즉 main의 dirty 표시는 코드 변경 때문이 아니다. clean 환경에서도 남는 blocker는 실제 current/Census input leaf 부재다.

## Phase 0 기준선 18개 실패 해소

Phase 0부터 추적하던 18개 실패는 같은 stale expectation 묶음이었다. authoritative operational leaf는 production full-thesis가 0건인데, 과거 테스트가 C17 score-path-only 1건을 계속 기대했다.

이를 C17을 억지로 다시 PASS시키는 방식으로 고치지 않았다. 대신 다음 현재 사실을 검증하도록 테스트를 바꿨다.

- C15/C17/C24: accepted claim은 있지만 full-thesis score path는 닫히지 않음
- C06: material gap으로 blocked
- C08/C28: source task는 실행됐지만 accepted claim이 없음
- production full-thesis: 0건
- score-path status: `PRODUCTION_FULL_E2R_SCORE_PATH_PENDING`
- promoted row가 0건이므로 required-positive/green-gap promoted-row 숫자도 0

쉬운 예로, 계약서 초안이 있다는 사실을 계약 체결로 세지 않는 것과 같다. accepted claim이 있어도 score contribution과 StageCourt까지 연결되지 않았다면 full thesis가 아니다.
