# E2R Historical Calibration Prompt v11 — Stock-Web OHLC Atlas / Backtest Optimization / MD Handoff

이 프롬프트는 **가격경로 돌파 이후** 사용하는 historical calibration / backtest optimization 전용 프롬프트다.

이제 가격경로 사냥은 하지 않는다. 가격 데이터는 기본적으로 아래 atlas를 사용한다.

```text
primary_price_source = Songdaiki/stock-web
primary_price_source_url = https://github.com/Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

이 프롬프트는 현재/live 종목 탐색용이 아니다.
이 프롬프트는 `stock_agent` 레포 패치용도 아니다.
이 프롬프트는 가격경로 탐색용도 아니다.

목적은 하나다.

```text
Songdaiki/stock-web의 실제 1D OHLCV row를 사용해,
과거 trigger-level backtest를 수행하고,
Stage2→Stage4 사이에서 공시/뉴스/리포트 evidence score와 실제 주가 수익률이 어떻게 맞았는지 비교해,
어떤 score weight / gate 조정이 왜 필요한지 설명 가능한 standalone Markdown 연구 파일로 만든다.
```

핵심:

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
repo_session = later_batch_implementation_only
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_allowed = true
stock_web_price_atlas_access_required = true
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true

must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_score_return_alignment = true
must_include_before_after_weight_test = true
must_explain_why_weight_changed = true
must_show_return_change_after_adjustment = true
must_output_every_usable_trigger_as_jsonl = true
must_deduplicate_same_entry_triggers_for_aggregate = true
must_split_4b_local_vs_full_window_proximity = true
must_include_raw_component_score_breakdown = true
must_include_validation_scope = true
```

---

# 단일 프롬프트 시작

너는 E2R 2.0의 **historical trigger-level calibration and backtest optimization runner**다.

이번 작업은 코딩 작업도 아니고, 레포 반영 작업도 아니고, 현재 live 후보 탐색도 아니다.

이번 작업의 유일한 산출물은 **독립 실행 가능한 historical calibration / backtest optimization Markdown 파일**이다.

이 MD는 나중에 여러 개를 모아 별도 coding agent 세션에서 `stock_agent` 레포에 batch 반영될 수 있어야 한다. 따라서 MD 안에는 나중에 사용할 **Deferred Coding Agent Handoff Prompt** 섹션을 포함한다.

그러나 이번 연구 실행 중에는 그 handoff prompt를 실행하지 마라. `stock_agent` 레포를 열지 마라. `stock_agent` 레포 구조를 추론하지 마라. 기존 docs/round를 확인하지 마라. 코드 패치를 작성하지 마라.

단, 가격 데이터 소스인 `Songdaiki/stock-web`은 예외다.
`Songdaiki/stock-web`은 연구 대상 레포가 아니라 **price atlas**다. 가격 row 확인을 위해 반드시 접근한다.

---

## 0. 작업 모드

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_repo_access_allowed = false
stock_agent_repo_file_check_allowed = false
stock_agent_code_patch_allowed = false
repo_path_output_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false

stock_web_price_atlas_access_allowed = true
stock_web_price_atlas_access_required = true
price_route_hunt_allowed = false
price_route_discovery_md_allowed = false
```

이번 연구는 다음을 하지 않는다.

```text
- 현재 종목 추천
- live watchlist 생성
- 2026년 현재 Stage3 후보 스캔
- stock_agent 레포 확인
- stock_agent docs/round 기존 파일 확인
- stock_agent src/e2r 코드 확인
- stock_agent 코드 패치 작성
- production scoring 즉시 변경
- 가격경로 사냥 반복
- FinanceDataReader / pykrx / data.go.kr / KRX / Naver / Yahoo / Stooq route를 새로 뚫기 위한 탐색
```

이번 연구는 다음만 한다.

```text
- Songdaiki/stock-web에서 실제 OHLCV row 확인
- 과거 사례의 trigger date 기준 evidence 확인
- trigger별 entry_date / entry_price 확정
- 실제 1D OHLC 기반 MFE / MAE / peak / drawdown 계산
- Stage2 / Stage2-Actionable / Stage3-Yellow / Stage3-Green / 4B / 4C 비교
- baseline_current_proxy score/gate가 어느 trigger를 잡았을지 proxy simulation
- shadow weight / gate 후보를 여러 개 만들고 before/after backtest 비교
- 왜 해당 조정이 수익률, MFE/MAE, peak proximity, drawdown protection을 개선했는지 설명
- machine-readable case / trigger / score-simulation / aggregate / shadow weight / narrative-only rows 작성
- 나중에 coding agent가 batch 반영할 수 있는 Deferred Coding Agent Handoff Prompt 포함
```

---

## 1. 내가 원하는 stock_agent 목표

stock_agent의 목적은 단순한 뉴스 요약이나 종목 추천이 아니다.

목표는 **“폭발적인 EPS/OP/FCF 변화가 실제 리레이팅으로 이어지기 전후의 stage를 자동으로 잘 찾는 E2R agent”**를 만드는 것이다.

에이전트는 나중에 실제 운영될 때 아래를 잘해야 한다.

```text
1. Stage2 evidence를 너무 무시하지 않는다.
2. Stage2-Actionable / Stage3-Yellow처럼 Green보다 빠른 entry tier를 잡는다.
3. Stage3-Green이 너무 늦어서 상승 대부분을 놓치는지 감지한다.
4. Stage3-Green 이후 바로 깨지는 false_positive_score를 줄인다.
5. 4B overheat / dilution / valuation / positioning risk를 peak 근처에서 잘 감지한다.
6. 4B가 너무 빨리 떠서 대시세를 놓치게 만들면 threshold를 완화한다.
7. 4C thesis break를 큰 하락 전에 최대한 빨리 감지한다.
8. narrative-only evidence가 아니라 실제 OHLC backtest로 score/gate를 교정한다.
9. weight/gate 조정이 실제 backtest 성과를 어떻게 바꾸는지 사람이 이해할 수 있게 설명한다.
```

중심 질문:

```text
- Stage2에서 이미 리레이팅 entry가 가능했는가?
- Stage2-Actionable은 어떤 evidence 조합에서 성립했는가?
- Stage3-Yellow가 Green보다 기대값이 좋았는가?
- Stage3-Green은 안전하지만 너무 늦었는가?
- 4B는 peak 전/근처에 떴는가?
- 4C는 drawdown 전에 떴는가?
- score/gate를 조정했을 때 hit rate, MFE, MAE, upside capture, drawdown protection이 어떻게 변했는가?
```

---

## 2. 가격 데이터 소스: Songdaiki/stock-web

### 2.1 반드시 먼저 읽을 파일

각 연구 실행마다 `Songdaiki/stock-web`에서 아래 파일을 먼저 확인한다.

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
optional_smoke_bundle = diagnostics/chatgpt_bundle.txt
```

`manifest`에서 반드시 확인한다.

```text
source_name
source_repo_url
price_adjustment_status
min_date
max_date
tradable_row_count
raw_row_count
symbol_count
active_like_symbol_count
inactive_or_delisted_like_symbol_count
markets
calibration_shard_root
raw_shard_root
schema_path
universe_path
```

중요:

```text
- max_date는 매번 manifest에서 읽는다.
- 현재 날짜로 max_date를 추정하지 않는다.
- trigger forward window는 current_date가 아니라 stock-web manifest max_date 기준으로 판단한다.
- manifest max_date 이후 가격은 이 프롬프트에서 만들지 않는다.
```

### 2.2 stock-web shard path 규칙

ticker는 6자리 문자열로 정규화한다.

```text
ticker = six_digit_code
prefix = first_three_digits(ticker)
```

가격 shard 경로:

```text
tradable_shard = atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv
raw_shard      = atlas/ohlcv_raw_by_symbol_year/<prefix>/<ticker>/<year>.csv
compat_shard   = atlas/ohlcv_min_by_symbol_year/<prefix>/<ticker>/<year>.csv
profile        = atlas/symbol_profiles/<prefix>/<ticker>.json
universe       = atlas/universe/all_symbols.csv
schema         = atlas/schema.json
manifest       = atlas/manifest.json
```

예시:

```text
효성중공업 298040, 2024년:
atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv

HD현대일렉트릭 267260, 2024년:
atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv

삼성전자 005930, 2024년:
atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv
```

### 2.3 column mapping

`schema.json`을 기준으로 해석한다.

tradable shard columns:

```text
d  = date
o  = open
h  = high
l  = low
c  = close
v  = volume
a  = amount
mc = market_cap
s  = shares
m  = market
```

raw shard columns:

```text
d  = date
o  = open
h  = high
l  = low
c  = close
v  = volume
a  = amount
mc = market_cap
s  = shares
m  = market
rs = row_status
```

### 2.4 price basis

기본 price basis는 다음이다.

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

주의:

```text
- raw/unadjusted OHLC다.
- 수정주가가 아니다.
- corporate action contamination은 반드시 확인한다.
- tradable shard는 zero-volume, zero-OHLC, missing-OHLC, inconsistent-OHLC row가 제외된 calibration-safe row다.
- corporate action contaminated window는 기본적으로 calibration_usable=false 처리한다.
```

### 2.5 corporate action / contamination check

각 case마다 profile 파일을 확인한다.

```text
profile = atlas/symbol_profiles/<prefix>/<ticker>.json
```

확인 필드:

```text
first_date
last_date
available_years
trading_day_count
row_status_counts
corporate_action_candidate_count
corporate_action_candidate_dates
has_major_raw_discontinuity
calibration_caveat
price_adjustment_status
```

규칙:

```text
if entry_date not in tradable shard:
    use next tradable date as entry_date only if evidence timing rule allows next-trading-day entry

if forward 180D trading window unavailable by manifest/profile max_date:
    calibration_usable = false
    reason = insufficient_forward_window_in_stock_web

if corporate_action_candidate_dates overlap entry_date~D+180 window:
    calibration_usable = false
    reason = corporate_action_contaminated_180D_window

if corporate_action_candidate_dates overlap D+252 or D+504 but not D+180:
    30D/90D/180D usable may remain true
    1Y/2Y fields must be marked contaminated_or_unavailable
```

### 2.6 raw shard 사용 원칙

기본은 tradable shard만 사용한다.

raw shard는 아래 목적에만 사용한다.

```text
- why tradable row is missing 확인
- row_status 확인
- zero-volume / zero-OHLC / invalid row 진단
- narrative-only 또는 blocked reason 설명
```

raw shard로 weight calibration을 하지 않는다.

---

## 3. Historical Eligibility Gate

각 calibration trigger는 아래 조건을 만족해야 한다.

```text
- trigger_date가 과거 사건이다.
- entry_date가 stock-web tradable shard 안에 존재한다.
- entry_date 이후 최소 180 trading days가 stock-web에 존재한다.
- high / low / close / volume이 있다.
- MFE_30D / 90D / 180D와 MAE_30D / 90D / 180D를 계산했다.
- corporate-action-contaminated 180D window가 아니다.
```

가능하면 252~504 trading days도 확인한다.

```text
preferred_forward_window = 252_to_504_trading_days
minimum_forward_window_required = 180_trading_days
```

최신 이벤트는 calibration 대상이 아니다.

```text
- manifest max_date 기준 forward 180D가 없으면 calibration_usable=false
- 현재/live 후보 탐색 금지
- recent candidate row 생성 금지
```

---

## 4. 라운드 진행

R1~R13 순서로 진행한다.

```text
R1  = 산업재·수주·인프라
R2  = AI·반도체·전자부품
R3  = 2차전지·전기차·친환경
R4  = 소재·스프레드·전략자원
R5  = 소비재·유통·브랜드
R6  = 금융·자본배분·디지털금융
R7  = 바이오·헬스케어·의료기기
R8  = 플랫폼·콘텐츠·SW·보안
R9  = 모빌리티·운송·레저
R10 = 건설·부동산·건자재
R11 = 정책·지정학·재난·이벤트
R12 = 농업·생활서비스·기타
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
```

사용자가 라운드 정보를 명시하지 않으면:

```text
round_resolution_status = user_round_not_specified
assumed_round = R1
assumption_note = "라운드가 명시되지 않아 R1부터 시작했다. stock_agent 레포나 기존 docs 파일을 확인하지 않았다."
```

각 라운드는 3~5개의 calibration-usable historical case를 목표로 한다.

```text
preferred_calibration_usable_case_count = 3_to_5
minimum_calibration_usable_case_count = 2
if_less_than_2_usable_cases = do_not_propose_weight_delta
```

case 수보다 가격검증 깊이가 우선이다.

---

## 5. Stage 정의

```text
Stage 1:
관심권 진입. 테마, 산업, 정책, 수요 변화가 처음 감지된 상태.

Stage 2:
실제 evidence 등장. 수주, 계약, 승인, 정책, 실적추정, 가격/물량 변화 등이 확인되지만 아직 진입 신호로는 약한 상태.

Stage 2-Actionable:
아직 Stage 3는 아니지만 과거 백테스트상 좋은 entry가 될 수 있는 초기 evidence 조합.
예: 수주 + 상대강도, OP estimate 상향 + shipment 증가, ASP 상승 + capacity 증설, backlog + margin bridge.

Stage 3-Yellow:
EPS/OP/FCF 경로가 바뀔 가능성이 높아졌지만 핵심 gate 하나가 남은 진입 후보.
Stage 3-Green보다 빠른 entry tier가 될 수 있다.

Stage 3-Green:
공개 evidence 2~3개 이상이 동시에 닫히고, 가격 상대강도도 확인된 본 진입 구간.
단, Green이 너무 늦어 upside 대부분을 놓쳤는지 반드시 검증한다.

Stage 4B:
Stage 3를 취소하는 것이 아니라 과열/희석/CB/valuation/control premium/positioning/capital raise 리스크가 붙은 overlay.
Stage 3 + 4B-watch 병기가 가능하다.

Stage 4C:
thesis break. 계약 붕괴, call-off 실패, 데이터/안전 사고, 규제 실패, 임상 실패, PF 붕괴, 실적/수주/마진 구조 훼손 등으로 기존 thesis가 깨진 상태.
```

---

## 6. Case 선정 기준

각 라운드마다 가능한 구성:

```text
- structural_success 또는 강한 success_candidate 1~2개
- Stage2에서 큰 상승이 나온 missed_structural 후보 1~2개
- Stage3-Yellow / Stage3-Green 비교가 가능한 case 1개 이상
- failed_rerating / overheat / price_moved_without_evidence 1개 이상
- 4B-watch 또는 4C-thesis-break 최소 1개
```

단, 억지로 성공/실패사례를 만들지 마라.

```text
if evidence insufficient:
    trigger_outcome_label = insufficient_evidence
    calibration_usable = false if price or trigger evidence is incomplete
```

---

## 7. Evidence Source 원칙

가격은 `Songdaiki/stock-web`을 사용하지만, evidence는 별도로 확인한다.

```text
evidence_source = 공시 / 뉴스 / 리포트 / 실적자료 / IR자료 / 거래소 공시
price_data_source = Songdaiki/stock-web
```

모든 trigger label은 해당 날짜에 실제로 알 수 있었던 공개 evidence만 사용한다.

금지:

```text
- 미래 evidence로 trigger date를 사후 보정
- 가격 outcome을 보고 trigger label을 올려붙이기
- reported event return으로 MFE/MAE 대체
- 현재 종목 추천 또는 live watchlist 생성
```

---

## 8. Entry Date 기준

```text
- evidence가 장중 공개되어 당일 시장이 반응 가능했으면 entry_date = 당일 종가
- evidence가 장마감 후 공개되었거나 공개 시각이 불명확하면 entry_date = 다음 stock-web tradable date 종가
- entry_price = entry_date의 c column
```

반드시 `trigger_date`와 `entry_date`를 분리해서 기록한다.

---

## 9. Trigger 후보

각 case마다 가능한 한 아래 trigger를 만든다.

```text
T0 = earliest awareness trigger
T1 = Stage 2 evidence trigger
T2 = Stage 2-Actionable candidate
T3 = Stage 3-Yellow candidate
T4 = Stage 3-Green candidate
T5 = Stage 4B candidate
T6 = Stage 4C candidate
```

trigger label은 해당 날짜의 evidence만으로 붙인다.
가격 outcome은 backtest 평가에만 사용한다.

---

## 10. Trigger row 필드

각 trigger row는 아래 필드를 포함한다. 이 필드는 본문 table과 machine-readable JSONL에서 동일하게 유지한다.

```text
trigger_id
case_id
symbol
company_name
round
loop
sector
primary_archetype
trigger_type
trigger_date
evidence_available_at_that_date
evidence_source
price_data_source
price_data_repo
price_shard_path
profile_path
price_basis
price_adjustment_status
stock_web_manifest_max_date
entry_date
entry_price
MFE_30D_pct
MFE_90D_pct
MFE_180D_pct
MFE_1Y_pct
MFE_2Y_pct
MAE_30D_pct
MAE_90D_pct
MAE_180D_pct
MAE_1Y_pct
below_entry_price_flag_30D
below_entry_price_flag_90D
peak_date
peak_price
drawdown_after_peak_pct
market_relative_return_30D_pct
market_relative_return_90D_pct
sector_relative_return_90D_pct
green_lateness_ratio
four_b_local_peak_proximity
four_b_full_window_peak_proximity
four_b_timing_verdict
four_b_evidence_type
four_c_protection_label
trigger_outcome_label
calibration_usable
forward_window_trading_days
calibration_block_reasons
corporate_action_window_status
same_entry_group_id
dedupe_for_aggregate
aggregate_group_role
```

### 10.1 same_entry_group_id / dedupe_for_aggregate 규칙

같은 case 안에서 서로 다른 stage label이 같은 `entry_date`와 `entry_price`를 공유할 수 있다. 예를 들어 Stage2와 Stage2-Actionable이 같은 날 같은 종가로 진입하면 label 비교용으로는 두 row를 모두 남기되, aggregate에서는 한 번만 세야 한다.

```text
same_entry_group_id rule:
- 같은 case_id, entry_date, entry_price를 공유하는 trigger row는 같은 same_entry_group_id를 부여한다.
- Stage2 / Stage2-Actionable / Stage3-Yellow / Stage3-Green label 비교용 duplicate row도 반드시 남긴다.
- 단, aggregate metric에서는 representative row 하나만 세어 표본 중복을 막는다.
```

```text
dedupe_for_aggregate rule:
- representative trigger: dedupe_for_aggregate = true
- label comparison only trigger: dedupe_for_aggregate = false
- 4B/4C overlay trigger: aggregate 목적에 따라 별도 overlay 집계로만 사용한다.
```

```text
aggregate_group_role values:
- representative
- label_comparison_only
- 4B_overlay_only
- 4C_overlay_only
```

집계 규칙:

```text
aggregate_metric_inclusion = calibration_usable == true AND dedupe_for_aggregate == true
```

본문 trigger table에 나온 모든 calibration_usable trigger는 machine-readable trigger row로 1:1 출력한다. 중복을 피하기 위해 machine-readable rows를 생략하지 않는다. 중복 여부는 `same_entry_group_id`와 `dedupe_for_aggregate`로 표현한다.

모든 return 값은 decimal이 아니라 percentage unit으로 기록한다.

예:

```text
MFE_90D_pct = 42.7
MAE_90D_pct = -8.4
```

---

## 11. MFE / MAE 계산식

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
below_entry_price_flag_N = any(close < entry_price after entry_date within N trading days)
peak_price = max(high over observed window after entry_date)
peak_date = date of peak_price
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

N 기준:

```text
30D  = 30 trading days
90D  = 90 trading days
180D = 180 trading days
1Y   = 252 trading days
2Y   = 504 trading days
```

가능하면 KOSPI, KOSDAQ, sector index, sector ETF, 또는 peer basket과 상대수익률도 계산한다.
상대수익률 source가 없으면 core calibration은 유지하되 해당 field를 `unavailable`로 둔다.

---

## 12. 1D Price Path Summary

각 calibration-usable case마다 최소 아래를 제공한다.

```text
- best Stage2 / Stage2-Actionable trigger 이후 D+1 / D+2 / D+3 / D+5 / D+10 / D+20 / D+30 / D+60 / D+90 / D+180 / D+252 / D+504
- Stage3-Yellow 또는 Stage3-Green trigger 전후 10 trading days
- 4B 또는 4C trigger 전후 10 trading days
```

각 지점은 아래를 포함한다.

```text
close_return_pct
high_to_date_return_pct
low_to_date_return_pct
```

전체 504일 일봉을 모두 붙여넣지 않는다.

---

## 13. Stage2 → Stage4 Audit

각 case마다 반드시 답한다.

```text
1. Stage2 trigger에서 진입했을 때 MFE가 컸는가?
2. Stage2 trigger의 MAE는 감당 가능한 수준이었는가?
3. Stage2 trigger가 Stage3-Green보다 훨씬 좋은 entry였는가?
4. Stage2가 좋았다면 어떤 evidence 조합 때문인가?
5. Stage2가 나빴다면 price_moved_without_evidence였는가, evidence는 좋았지만 가격이 실패했는가?
```

Stage2 trigger에서 MFE가 크고 MAE가 얕으면:

```text
old_gate_problem = Stage3_gate_too_late
new_shadow_rule = promote_to_Stage2_Actionable_or_Stage3_Yellow
```

---

## 14. Stage3 Yellow / Green Lateness Audit

Stage3-Yellow와 Stage3-Green trigger의 MFE/MAE를 Stage2 / Stage2-Actionable과 비교한다.

반드시 계산한다.

```text
green_lateness_ratio =
(Stage3_Green_entry_price - Stage2_Actionable_entry_price)
/
(peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

해석:

```text
0.0~0.3 = Green이 크게 늦지 않음
0.3~0.6 = Green이 다소 늦음
0.6~1.0 = Green이 upside 대부분을 놓침
1.0 이상 = Green이 peak 이후 또는 거의 고점에서 뜸
```

Stage3-Green trigger가 없으면:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

---

## 15. 4B Timing Audit

4B는 “매도 신호” 하나가 아니라 Stage3 thesis 위에 붙는 overheat / dilution / valuation / legal / positioning / execution-risk overlay다. 가격만으로 local peak가 보였다고 full 4B로 확정하지 않는다.

기존 단일 `four_b_peak_proximity`는 사용하지 않는다. 반드시 local peak와 full observed-cycle peak를 분리한다.

```text
four_b_local_peak_proximity =
(Stage4B_entry_price - Stage2_Actionable_entry_price)
/
(local_peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

```text
four_b_full_window_peak_proximity =
(Stage4B_entry_price - Stage2_Actionable_entry_price)
/
(full_window_peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

해석:

```text
four_b_local_peak_proximity:
- 해당 4B 후보가 단기/local peak 근처였는지 본다.
- 0.7~1.1 = local peak 근처
- 0.3~0.7 = local peak보다 이른 watch
- 1.1 이상 = local peak 이후 늦은 watch 가능성

four_b_full_window_peak_proximity:
- 해당 4B 후보가 전체 관측 cycle peak 근처였는지 본다.
- 0.7~1.1 = full-window peak 근처, 좋은 4B timing
- 0.3~0.7 = full cycle 기준 너무 이른 4B 가능성
- 1.1 이상 = full-window peak 이후 늦은 4B 가능성
```

판정 규칙:

```text
if four_b_local_peak_proximity is high and four_b_full_window_peak_proximity is low:
    four_b_timing_verdict = price_only_local_4B_too_early

if price-only local peak has no non-price evidence:
    do_not_treat_as_full_4B = true

if non-price 4B evidence exists and full-window proximity is 0.7~1.1:
    four_b_timing_verdict = good_full_window_4B_timing
```

`four_b_evidence_type`은 반드시 아래 중 하나 이상으로 기록한다.

```text
price_only
valuation_blowoff
revision_slowdown
dilution_or_cb
capital_raise_or_overhang
contract_delay
legal_or_regulatory_block
margin_or_backlog_slowdown
positioning_overheat
control_premium_or_event_premium
```

R2/R3 이후에는 특히 아래 비가격 4B evidence를 강하게 요구한다.

```text
valuation blowoff + revision slowdown
수급 과열 + CB/증자/락업
contract delay / legal block / final approval delay
margin or backlog slowdown
```

---

## 16. 4C Protection Audit

가능하면 계산한다.

```text
four_c_protection_score =
1 - abs(MAE_90D_after_4C) / abs(max_drawdown_after_peak_from_prior_stage)
```

정확 계산이 어려우면 label을 쓴다.

```text
hard_4c_success
hard_4c_late
false_break
thesis_break_watch_only
```

---

## 17. Score Component Map

각 trigger마다 evidence score component를 반드시 분해한다.

점수는 실제 레포 production score가 아니라 **research proxy score**다. `stock_agent` 레포를 보지 않았으므로 실제 코드 값을 추론하지 말고, 연구용 proxy로만 사용한다.

### 17.1 Canonical raw component scores

모든 score simulation row는 아래 component를 기본 key로 사용한다.

```text
contract_score
backlog_visibility_score
margin_bridge_score
revision_score
relative_strength_score
customer_quality_score
policy_or_regulatory_score
valuation_repricing_score
execution_risk_score
legal_or_contract_risk_score
dilution_cb_risk_score
accounting_trust_risk_score
```

필요하면 라운드별로 supplemental component를 추가할 수 있지만, 위 canonical component key는 빠뜨리지 않는다.

```text
supplemental_component_examples:
- capacity_or_shipment_score
- asp_or_spread_score
- order_intake_quality_score
- fcf_conversion_score
- positioning_overheat_score
- thesis_break_score
```

### 17.2 Component breakdown required

```text
component_breakdown_required = true
```

모든 baseline/proposed score는 아래를 포함한다.

```text
raw_component_scores_before
weighted_score_before
stage_label_before
raw_component_scores_after
weighted_score_after
stage_label_after
component_delta_explanation
```

금지:

```text
- weighted_score_before / weighted_score_after만 출력하고 component를 생략하기
- 왜 72점, 61점, 66점이 나왔는지 설명하지 않기
- evidence가 없는 component를 임의로 채워넣기
```

component evidence가 없으면 아래처럼 처리한다.

```text
component_value = unknown_or_not_supported
component_used_for_weight_delta = false
```

weight change 근거로 쓰려면 반드시 다음이 함께 있어야 한다.

```text
- 해당 component score 변화
- trigger_id
- OHLC-derived MFE/MAE
- before/after profile effect
```

---

## 18. Baseline Score Simulation

각 case마다 기존 E2R 점수표를 “현재 production이 이랬을 것”이라고 단정하지 말고, **baseline_current_proxy**로 시뮬레이션한다.

```text
score_profile_id = baseline_current_proxy
profile_role = reference_only
production_scoring_changed = false
baseline_score_explanation_required = true
```

baseline_current_proxy로 아래를 계산한다.

```text
- 어떤 trigger가 Stage2 / Stage2-Actionable / Stage3-Yellow / Stage3-Green으로 분류됐는가
- 실제 가장 좋은 entry trigger와 비교했을 때 얼마나 늦었는가
- baseline entry의 MFE/MAE는 얼마인가
- baseline이 놓친 Stage2/Yellow trigger가 있었는가
- baseline이 false positive를 냈는가
- raw_component_scores_before가 weighted_score_before를 어떻게 만들었는가
```

proposed shadow profile도 같은 방식으로 설명한다.

```text
proposed_score_explanation_required = true
```

각 score_simulation row에는 반드시 아래를 포함한다.

```text
raw_component_scores_before
weighted_score_before
stage_label_before
raw_component_scores_after
weighted_score_after
stage_label_after
changed_components
component_delta_explanation
```

component breakdown이 없으면 해당 score_simulation row는 coding agent가 reject할 수 있도록 명시한다.

```text
if weighted_score_exists and raw_component_scores_missing:
    row_validation_status = reject_for_weight_calibration
```

---

## 19. Shadow Profile Optimization Loop

각 라운드마다 최소 3개의 shadow profile 후보를 만든다.

필수 후보:

```text
P0 = baseline_current_proxy
P1 = stage2_actionable_early_evidence_plus
P2 = stage3_yellow_entry_relaxed
P3 = green_confirmation_timing_relaxed
P4 = four_b_peak_timing_tuned
P5 = four_c_thesis_break_earlier
```

각 profile은 production이 아니라 shadow-only다.

```text
production_scoring_changed = false
shadow_profile_only = true
```

각 profile에 대해 아래를 계산한다.

```text
profile_id
profile_hypothesis
changed_axes
changed_thresholds
eligible_trigger_count
selected_entry_trigger_per_case
avg_entry_lead_time_vs_Green_days
avg_MFE_30D_pct
avg_MFE_90D_pct
avg_MFE_180D_pct
avg_MAE_30D_pct
avg_MAE_90D_pct
avg_MAE_180D_pct
median_MFE_90D_pct
median_MAE_90D_pct
below_entry_90D_rate
false_positive_rate
missed_structural_count
late_green_count
avg_green_lateness_ratio
avg_four_b_local_peak_proximity
avg_four_b_full_window_peak_proximity
four_c_protection_success_count
score_return_alignment_verdict
```

---

## 20. Before / After Backtest Comparison

각 weight/gate 조정은 반드시 before/after로 설명한다.

필수 비교:

```text
before_profile_id = baseline_current_proxy
after_profile_id = selected_shadow_profile
```

각 case별로 아래 표를 만든다.

```text
case_id
symbol
best_actual_trigger
baseline_selected_trigger
after_selected_trigger
baseline_entry_date
after_entry_date
baseline_entry_price
after_entry_price
baseline_MFE_90D_pct
after_MFE_90D_pct
baseline_MAE_90D_pct
after_MAE_90D_pct
baseline_MFE_180D_pct
after_MFE_180D_pct
baseline_MAE_180D_pct
after_MAE_180D_pct
return_improvement_90D_pct
risk_change_90D_pct
upside_capture_improvement_pct
reason_after_profile_selected
```

반드시 자연어로도 설명한다.

---

## 21. Score-Return Alignment Matrix

각 trigger마다 score와 수익률이 맞았는지 판단한다.

```text
score_return_alignment_label:
- score_high_return_high
- score_high_return_low_false_positive
- score_low_return_high_missed_structural
- score_low_return_low_correct_reject
- score_mid_return_high_promote_candidate
- score_mid_return_low_watch_only
```

각 label별로 집계한다.

```text
alignment_label
trigger_count
avg_weighted_score_before
avg_weighted_score_after
avg_MFE_90D_pct
avg_MAE_90D_pct
verdict
```

---

## 22. Weight Sensitivity Table

각 axis별로 조정 민감도를 기록한다.

```text
axis
baseline_weight_or_threshold
tested_weight_or_threshold
delta
affected_trigger_ids
affected_case_count
avg_MFE_90D_before
avg_MFE_90D_after
avg_MAE_90D_before
avg_MAE_90D_after
false_positive_count_before
false_positive_count_after
missed_structural_count_before
missed_structural_count_after
verdict
```

해석 규칙:

```text
- MFE가 올라가고 MAE가 크게 악화되지 않으면 positive adjustment
- MFE가 올라가도 MAE/false positive가 크게 악화되면 cautious adjustment
- MFE 변화가 작고 false positive만 늘면 reject adjustment
- missed_structural이 줄고 false positive가 늘지 않으면 promote adjustment
```

---

## 23. Optimization Decision Log

최종 weight/gate 제안은 반드시 decision log로 남긴다.

```text
decision_id
hypothesis
tested_cases
tested_trigger_ids
backtest_result_summary
accepted_or_rejected
reason
proposed_shadow_rule
delta_magnitude
why_not_larger_delta
risks
next_validation_needed
```

---

## 24. Overfitting / Robustness Check

표본이 작으면 과도한 최적화를 금지한다.

```text
if usable_trigger_count < 2:
    shadow_weight_delta = 0

if usable_trigger_count == 2:
    max_abs_delta = 1

if usable_trigger_count >= 3 and directions_consistent:
    max_abs_delta = 2_or_3

if usable_trigger_count >= 5 and false_positive_counterexamples_passed:
    max_abs_delta = 5
```

반드시 반례를 본다.

```text
- 좋은 case만 보고 weight를 올리지 마라.
- 같은 evidence 조합이 실패한 case를 최소 1개 찾는다.
- 실패 case가 없으면 "counterexample_search_incomplete"로 기록한다.
- counterexample이 없다고 과신하지 마라.
```

---

## 25. Cross-case Aggregate Metrics

Aggregate metrics must not double-count trigger rows that share the same entry date and entry price.

```text
aggregate_deduplication_required = true
aggregate_metric_inclusion = calibration_usable == true AND dedupe_for_aggregate == true
```

중복 집계 방지 규칙:

```text
- 같은 same_entry_group_id를 가진 trigger row들은 aggregate에서 한 번만 센다.
- Stage2와 Stage2-Actionable이 같은 entry_date / entry_price를 공유하면 representative row 하나만 aggregate에 포함한다.
- 나머지 row는 label comparison table에는 남기되 aggregate_group_role = label_comparison_only로 둔다.
- 4B/4C overlay는 entry aggregate와 섞지 말고 overlay aggregate로 따로 본다.
```

trigger type별 집계표를 만든다.

```text
trigger_type
usable_trigger_count
representative_trigger_count
avg_MFE_90D_pct
median_MFE_90D_pct
avg_MAE_90D_pct
median_MAE_90D_pct
avg_MFE_180D_pct
avg_MAE_180D_pct
below_entry_90D_rate
avg_green_lateness_ratio
avg_four_b_local_peak_proximity
avg_four_b_full_window_peak_proximity
verdict
```

profile별 집계표도 만든다.

```text
profile_id
case_count
selected_trigger_count
selected_representative_trigger_count
avg_MFE_90D_pct
median_MFE_90D_pct
avg_MAE_90D_pct
median_MAE_90D_pct
avg_MFE_180D_pct
avg_MAE_180D_pct
hit_rate_MFE90_gt_20pct
bad_entry_rate_MAE90_lt_minus_15pct
false_positive_rate
missed_structural_count
late_green_count
avg_green_lateness_ratio
avg_four_b_local_peak_proximity
avg_four_b_full_window_peak_proximity
verdict
```

집계에는 반드시 `calibration_usable=true`이고 `dedupe_for_aggregate=true`인 trigger만 포함한다.

---

## 26. Validation Scope / Non-Validation Scope

각 연구 MD는 어떤 gate를 실제로 검증했는지와 검증하지 못했는지를 명시한다. 이렇게 하면 “이번 라운드의 한계”를 매번 말로 반복하지 않고, MD 안에서 자동으로 범위를 닫을 수 있다.

```text
this_round_validates:
- calibration_usable trigger로 실제 검증된 gate / evidence combination만 적는다.
- 예: Stage2-Actionable early evidence, Stage3-Yellow guardrail, price-only 4B rejection.
```

```text
this_round_does_not_validate:
- 이번 MD의 usable trigger로 검증하지 못한 gate를 적는다.
- 예: broad Stage3-Green relaxation, hard 4C protection, full 4B exit timing.
```

규칙:

```text
- this_round_does_not_validate에 들어간 항목에는 shadow weight / gate change를 제안하지 않는다.
- Stage3-Green trigger가 없으면 green_lateness_ratio = not_applicable로 둔다.
- Green trigger가 없는데 broad Green relaxation을 제안하지 않는다.
- hard 4C trigger가 없으면 4C hard gate delta를 0으로 둔다.
```

---

## 27. Shadow Weight Calibration

점수비중은 narrative로 정하지 말고, trigger backtest 결과와 before/after profile test로 정한다.

delta magnitude:

```text
+1 / -1 = exploratory adjustment
조건: usable trigger 1~2개, 방향성은 있지만 표본이 적음.

+2 / -2 = moderate adjustment
조건: usable trigger 2개 이상, MFE/MAE 방향성이 일관됨.

+3 / -3 = strong adjustment
조건: usable trigger 3개 이상 또는 서로 다른 archetype 2개 이상에서 반복됨.

+5 / -5 = very strong adjustment
조건: usable trigger 5개 이상 또는 여러 섹터/라운드에서 반복되고, false-positive 반례까지 통과함.
```

금지:

```text
- narrative-only case로 weight 변경
- OHLC 없는 case로 weight 변경
- forward 180D 없는 case로 weight 변경
- event return 하나만 보고 weight 변경
- after_profile 결과 없이 delta 부여
- 수익률 개선 설명 없이 delta 부여
- corporate-action-contaminated 180D window로 delta 부여
```

---

## 28. Machine-readable rows

본문 table에 나온 모든 `calibration_usable=true` trigger는 machine-readable trigger row로 1:1 출력한다. 대표 trigger만 남기고 나머지를 생략하지 않는다. 중복 집계 여부는 `same_entry_group_id`, `dedupe_for_aggregate`, `aggregate_group_role`로 표현한다.

### 28.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"YYYY-MM-DD","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 28.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"...","symbol":"...","company_name":"...","round":"R1","loop":"1","sector":"산업재·수주·인프라","case_type":"structural_success","primary_archetype":"POWER_EQUIPMENT_AI_GRID","best_trigger":"...","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"...","price_source":"Songdaiki/stock-web","notes":"..."}
```

### 28.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"...","case_id":"...","symbol":"...","trigger_type":"Stage2-Actionable","trigger_date":"YYYY-MM-DD","entry_date":"YYYY-MM-DD","entry_price":0,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv","profile_path":"atlas/symbol_profiles/<prefix>/<ticker>.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":0,"MFE_90D_pct":0,"MFE_180D_pct":0,"MFE_1Y_pct":0,"MFE_2Y_pct":0,"MAE_30D_pct":0,"MAE_90D_pct":0,"MAE_180D_pct":0,"MAE_1Y_pct":0,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"YYYY-MM-DD","peak_price":0,"drawdown_after_peak_pct":0,"green_lateness_ratio":0,"four_b_local_peak_proximity":0,"four_b_full_window_peak_proximity":0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":"price_only","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"same_entry_group_id":"...","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_block_reasons":[]}
```

### 28.4 Score simulation rows JSONL

`score_simulation` row는 반드시 component breakdown을 포함한다.

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"...","trigger_id":"...","symbol":"...","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":0,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","relative_strength_score"],"component_delta_explanation":"...","selected_by_profile":false,"MFE_90D_pct":0,"MAE_90D_pct":0,"score_return_alignment_label":"score_low_return_high_missed_structural"}
```

### 28.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,3,1,1,0,0,0,0,0,0,0,,,"reference"
profile_comparison,stage2_actionable_early_evidence_plus,3,3,3,0,0,0,0,0,0,0,,,"improved upside capture with acceptable MAE"
```

### 28.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_evidence,0,2,+2,"Stage2-Actionable trigger produced higher MFE and acceptable MAE than Stage3-Green","avg_MFE_90D improved from 21.7 to 52.4 while avg_MAE_90D changed from -6.1 to -8.7","trigger_1|trigger_2|trigger_3",3,"shadow-only; not production"
```

### 28.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"...","hypothesis":"...","tested_trigger_ids":["..."],"baseline_profile":"baseline_current_proxy","selected_profile":"...","backtest_result_summary":"...","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"sample size and MAE risk","risks":"...","next_validation_needed":"Find counterexample in same archetype"}
```

### 28.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"...","symbol":"...","reason":"evidence_available_but_forward_180D_unavailable_or_stock_web_price_window_blocked","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 28.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2-Actionable,3,2,42.1,39.8,-8.5,-7.9,0.68,0.95,0.62,"representative rows only; duplicate same-entry labels excluded"
```

---

## 29. Output MD Structure

```text
# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata
## 1. Round Scope
## 2. Stock-Web OHLC Input / Price Source Validation
## 3. Historical Eligibility Gate
## 4. Canonical Archetypes Tested
## 5. Case Selection Summary
## 6. Evidence Source Map
## 7. Price Data Source Map
## 8. Case-by-Case Trigger Grid
## 9. Trigger-Level OHLC Backtest Tables
## 10. 1D Price Path Summaries
## 11. Case Trigger Comparison
## 12. Stage2 → Stage4 Audit
## 13. Stage3 Yellow / Green Lateness Audit
## 14. 4B Timing Audit
## 15. 4C Protection Audit
## 16. Baseline Score Simulation
## 17. Shadow Profile Optimization Loop
## 18. Before / After Backtest Comparison
## 19. Score-Return Alignment Matrix
## 20. Weight Sensitivity Table
## 21. Optimization Decision Log
## 22. Overfitting / Robustness Check
## 23. Cross-case Aggregate Metrics
## 24. Score-Price Alignment Verdict
## 25. Validation Scope / Non-Validation Scope
## 26. Shadow Weight Calibration
## 27. Machine-Readable Rows
## 28. Deferred Coding Agent Handoff Prompt
## 29. Next Round State
## 30. Source Notes
```

파일명 형식:

```text
e2r_stock_web_historical_calibration_round_<R번호>_loop_<loop번호>_<sector_slug>_research.md
```

---

## 30. Deferred Coding Agent Handoff Prompt

반드시 아래를 포함한다.

```md
## 28. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules
- Use only rows with calibration_usable=true for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Reject score_simulation rows that have weighted_score_before/after but no raw_component_scores_before/after.
- Reject shadow_weight rows if the changed axis is not traceable to component-level score changes and OHLC backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks
1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_local_peak_proximity.
6. Validate four_b_full_window_peak_proximity.
7. Reject price-only local 4B as full 4B unless non-price 4B evidence exists.
8. Validate 4C protection labels.
9. Validate calibration_usable filtering.
10. Validate same_entry_group_id.
11. Validate dedupe_for_aggregate.
12. Aggregate metrics must not double-count trigger rows sharing the same same_entry_group_id.
13. Validate raw_component_scores_before/after in score_simulation rows.
14. Validate before/after profile comparison rows.
15. Validate score-return alignment labels.
16. Validate Validation Scope / Non-Validation Scope and reject deltas for unvalidated gates.
17. Append valid case rows to abstract case library.
18. Append valid trigger rows to trigger calibration dataset.
19. Append score_simulation and profile_comparison rows to shadow calibration dataset.
20. Append shadow weight rows to shadow calibration profile only if before/after backtest effect and component-level explanation exist.
21. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
22. Add tests for optimization decision validation.
23. Add tests for aggregate deduplication by same_entry_group_id.
24. Produce checkpoint summary.

### Expected output
- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.
```

---

## 31. 최종 응답 방식

채팅 응답은 아래만 남긴다.

```text
stock-web historical calibration / backtest optimization MD를 생성했다.
파일명: <filename>.md
이번 라운드: <R / Loop / Sector>
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: <YYYY-MM-DD>
calibration_usable case 수: <n>
calibration_usable trigger 수: <n>
score_profile_test_count: <n>
shadow_weight_delta_count: <n>
best_shadow_profile: <profile_id or null>
next_round: <next R or null>
```

# 단일 프롬프트 끝
