# E2R Reconstruction Phase 13 — Bounded Daily Census

## 판정

`CURRENT_OPERATIONAL_BRAIN_PASS`

전 종목을 같은 깊이로 비싸게 조사하지 않고, 먼저 값싼 공통 검사를 한 뒤 현재 trigger가 있는 일부 종목만 제한적으로 깊게 조사하는 canonical daily 경로를 만들었다.

```text
Universe
→ official / price / risk / existing-ledger baseline
→ SourceTimeline
→ LastEffectiveThesis
→ DepthPolicy
→ selected deep
→ CensusStageStatus
→ Watchlist
```

Phase 12의 `AtomicStageDecision`이 이제 `CensusStageStatus`의 Stage·점수·claim·gap을 한 번에 결정한다. 다만 이번 증거는 deterministic fixture와 manifest round trip이다. 실제 KRX 전 종목, 실제 공시 provider, 실제 Codex 완료를 관측한 것은 아니므로 `production_runtime_ready=false`다.

## 전 종목과 선택적 깊이

깊이는 다음처럼 나뉜다.

| 깊이 | 의미 | 고정 fixture 수 |
|---|---|---:|
| `L0_UNIVERSE` | 오늘 판단할 전체 종목 명부 | 8 |
| `L1_BASELINE` | official, price, risk, existing-ledger 공통 검사 | 8 |
| `L2_OFFICIAL_LIGHT` | 현재 trigger 후보의 공식 출처 얕은 확인 | 8 |
| `L3_RESEARCH_BRAIN` | 우선순위 안에 든 후보의 조사 계획 | 5 |
| `L4_ACQUISITION` | bounded SourceTask로 실제 문서 수집 시도 | 4 |
| `L5_FULL_THESIS` | material gap이 닫혀 완전한 thesis가 된 상태 | 1 |

쉬운 예로 2,000개 종목이 있어도 2,000개 모두에 LLM과 일반 웹 검색을 실행하지 않는다. 2,000개에는 L0/L1을 적용하고, 오늘 공시·실적·위험 변화 같은 trigger가 있는 후보 중 budget 안에 든 종목만 L3 이상으로 올린다.

선정은 sector나 archetype별 할당량을 채우는 방식이 아니다. 현재 trigger의 종류와 수를 deterministic하게 정렬한 뒤 `max_deep_candidates` 안에서 자른다. 따라서 “오늘 반도체를 반드시 3개 뽑는다” 같은 quota가 없다.

## 네 개 baseline lane

eligible 종목마다 다음 네 lane이 정확히 하나씩 있어야 한다.

- `OFFICIAL`: 공시·거래소·회사 IR 같은 공식 정보 상태
- `PRICE`: 가격·거래량 변화 상태
- `RISK`: 현재 위험 신호 상태
- `EXISTING_LEDGER`: 기존 current OPEN claim 상태

baseline은 조사 시작점을 만드는 진단 정보이며 그 자체로 점수가 아니다. 예를 들어 주가가 하루 15% 올랐다는 사실은 `MARKET` trigger를 열 수 있지만, 계약 품질 25점을 자동으로 만들 수는 없다.

provider가 실패한 경우도 0점으로 바꾸지 않는다. `PROVIDER_PENDING` 또는 source gap으로 남겨 “자료를 못 읽음”과 “자료를 읽고 나쁨”을 구분한다.

## Daily trigger와 점수의 경계

현재 daily 경로는 다음 여덟 trigger family를 모두 받는다.

```text
OFFICIAL / EARNINGS / IR / REPORT
NEWS / MARKET / RISK / EXISTING_LEDGER
```

trigger는 “더 조사할 이유”이지 score evidence가 아니다. 특히 뉴스 제목이나 시장 가격은 단독으로 점수를 만들지 않는다.

쉬운 예:

```text
뉴스: 신규 공장 착공 보도
→ NEWS trigger 생성
→ 공식 IR·공시에서 대상 기업 CAPA와 가동 시점을 확인
→ source-backed current claim이 만들어진 경우에만 primitive 점수 재료
```

고정 실행에서는 trigger 8개가 각각 한 번씩 들어왔지만, trigger가 score evidence로 승격된 수는 0이고 MARKET/NEWS 점수 승격도 0이다.

## SourceTask는 합계가 아니라 감사 가능한 leaf다

Production daily의 각 조사 작업은 다음 경계를 직접 가진다.

- `max_queries`
- `max_candidates`
- `max_fetches`
- `max_retries`
- `stop_condition=stop_on_resolution`
- 일반 웹 허용 여부
- official-first 시도 여부와 공식 출처로 해결되지 않은 정확한 이유

고정 실행에는 6개 SourceTask leaf가 있고, 모두 한 deep execution에 정확히 한 번 연결된다. task를 만들고 결과에서 참조하지 않거나, 같은 task를 두 종목 실행에 재사용하면 audit가 실패한다.

쉬운 예로 `DART` 공시에서 장기계약의 당사자·금액·기간이 확인되면 그 claim은 해결된 것이다. `stop_on_resolution`이므로 같은 질문을 풀기 위해 뉴스 100개를 계속 수집하지 않는다. 반대로 공식 출처가 질문을 풀지 못했고 task에 정확한 gap이 남은 경우에만 bounded 일반 웹 fallback을 허용한다.

Test용 task나 fixture provider를 `test_mode=false`에 넣으면 실행 전에 거절한다. bounded Codex provider 계약은 받을 수 있지만, 이번 Phase가 실제 Codex 호출 완료를 증명한 것은 아니다.

## 오래된 current OPEN claim 보존

최근 N일 lookback은 수집 우선순위에 쓸 수 있어도 Stage를 삭제하는 cutoff가 아니다.

고정 fixture의 기존 원장 claim은 `2024-01-15`에 관측됐고 daily 기준일은 `2026-06-30`이다. 이 claim은 오래됐지만 여전히 current OPEN이므로 `LastEffectiveThesis`에 남는다.

```text
오래됨 + 아직 OPEN
→ 자동 삭제하지 않음
→ NEEDS_REFRESH로 표시
→ 현재 반증이나 종료 claim이 확인될 때 lifecycle 변경
```

`current_open_claim_dropped_by_lookback=0`, `recent_lookback_stage_cutoff=0`으로 독립 감사했다.

## 다섯 종료 상태와 atomic score

선택된 5개 후보는 반드시 하나의 terminal outcome으로 끝난다.

| outcome | 수 | 의미 |
|---|---:|---|
| `FULL_THESIS` | 1 | material 조건이 모두 source-backed claim으로 닫힘 |
| `DISPROVED` | 1 | current direct hard break로 기존 논리가 훼손됨 |
| `SOURCE_PENDING` | 1 | 필요한 공식/source 근거가 아직 없음 |
| `PROVIDER_PENDING` | 1 | provider 실패로 판단을 확정할 수 없음 |
| `BUDGET_PENDING` | 1 | 오늘의 bounded budget 안에서 조사가 끝나지 않음 |

`FULL_THESIS` 한 건만 `FULL_E2R_100`, 100점, `3-Green`으로 확정됐다. current hard break가 있는 한 건은 raw 참고점수 75를 보존하되 표시 점수는 `NO_SCORE`, Stage는 `4C`다. pending 세 건도 낮은 점수를 정상 점수처럼 확정하지 않는다.

## CensusStageStatus와 Watchlist

전 종목은 정확히 하나의 `CensusStageStatus`를 가진다. Watchlist에는 다음 필드를 노출한다.

- score type과 표시 점수·raw reference 구분
- confidence
- accepted claim IDs
- missing conditions
- material/provider/source gaps
- 다음 monitoring action

직접적인 매수·매도·비중 지시는 허용하지 않는다. 예를 들어 `Stage 4C 논리 훼손 감시`, `근거 보완 후 Stage 재검증`, `다음 실적과 수주잔고 확인`처럼 확인할 다음 행동만 표시한다.

고정 fixture는 trigger가 모든 종목에 있어 Watchlist도 8행이다. `watchlist_projection_mismatch=0`, 투자 권고 문구 수는 0이다.

## Legacy Census와의 경계

기존 Census의 `UniverseInstrument`, `BaselineScanResult`, `SourceTimeline`, `LastEffectiveThesisState`는 one-way adapter로 canonical current 입력에 옮길 수 있다.

다만 legacy `base_stage_hint=Stage3-Green`을 canonical Stage에 복사하지 않는다. Stage와 score는 오직 current atomic decision에서 와야 한다. adapter fixture는 baseline 4개와 MARKET/EXISTING_LEDGER trigger 2개를 보존했지만 최종 Stage는 atomic decision이 없으므로 `0 / NO_SCORE`였다.

기존 `run_e2r_census_mode`는 계속 legacy 진단 경로로 잠겨 있고 production ready를 주장할 수 없다.

## 독립 감사와 known-bad

leaf artifact에서 61개 critical 조건을 다시 계산했다. 다음 변이를 실제로 넣어 모두 탐지했다.

- 전 종목 상태 중 한 행 삭제
- MARKET trigger를 score evidence로 위조
- recent cutoff 적용
- current OPEN claim을 현재 thesis에서 삭제
- pending 상태에 full score 삽입
- Watchlist 상태 행 삭제
- Watchlist에 직접 매수 문구 삽입
- daily config 또는 SourceTask cap을 `None`으로 변경
- `stop_on_resolution` 제거
- SourceTask 참조 삭제
- official-first 근거 없이 일반 웹 허용
- sector quota 추가
- 모든 종목에 LLM 실행 위조

정상 leaf hash와 audit hash는 모두 `bb7ed7dccbd9e68ed56d8b9ad04ff469f9b16b2b80c770634ec611357419b27e`이고 critical 합은 0이다.

## 주요 파일

- `runtime/current_operation_runner.py`: bounded daily runner, SourceTask leaf, timeline/thesis/depth/status/watchlist, 독립 audit
- `census/canonical_current_adapter.py`: 기존 Census leaf의 one-way canonical adapter
- `cli/run_e2r_current_operation.py`: current input manifest 실행과 산출물 기록
- `tests/test_current_operation_runner.py`: full-universe·depth·pending·known-bad·CLI·adapter 검사
- `e2r_reconstruction_phase13_acceptance.json`: 고정 Phase 13 acceptance

## 검증 경계와 다음 단계

Phase 13은 daily Census의 의미와 bounded 계약을 완성했다. 아직 실제 KRX universe와 실제 provider 완료를 관측하지 않았으므로 이 결과만으로 운영 준비 완료를 선언하지 않는다.

다음 Phase 14에서는 `candidate → hypothesis → retrieval → recipe → SourceTask → query → result → fetched/relevant document → assertion → claim → primitive → score → terminal outcome` 전환을 leaf artifact에서 독립 재계산해야 한다. 단순히 task shell 수가 늘어난 것을 진척으로 세지 않고, 원래 gap이 직접 닫혔는지를 우선 측정한다.
