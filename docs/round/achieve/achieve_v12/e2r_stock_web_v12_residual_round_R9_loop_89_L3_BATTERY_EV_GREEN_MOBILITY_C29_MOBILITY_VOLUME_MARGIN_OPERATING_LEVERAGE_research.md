# E2R Stock-Web v12 Residual Research — R9 Loop 89 — L3 / C29

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R9
scheduled_loop: 89
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: TIRE_AND_AUTO_COMPONENT_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA_FADE
output_file: e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year

completed_round: R9
completed_loop: 89
next_round: R10
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

직전 산출물은 `R8 / loop 89` 완료 상태였으므로 이번 실행은 순환 규칙상 `R9 / loop 89`다.

R9는 mobility / transport 성격이면 `L3_BATTERY_EV_GREEN_MOBILITY`, 건설·부동산 transport-adjacent 성격이면 `L9_CONSTRUCTION_REALESTATE_HOUSING`를 허용한다. 이번 연구는 자동차 부품·타이어의 volume / margin operating leverage 문제이므로 `L3 / C29`로 분류한다.

```text
R8 loop 89 completed
-> scheduled_round = R9
-> scheduled_loop = 89
-> selected_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
-> selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

---

## 2. No-Repeat / novelty check

No-Repeat Index 기준 C29는 이미 꽤 많이 쌓인 archetype이다.

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rows: 60
symbols: 27
date_range: 2021-01-08~2024-08-26
positive/counterexample: 26/13
4B/4C: 6/0
top_repeat_symbols:
  - 011210
  - 000270
  - 005380
  - 005850
  - 010690
  - 018880
```

이번 실행에서는 위 반복 상위 종목과 직전 R9 loop88에서 사용한 `002350`, `009900`, `012860`을 피했다. 또한 최근 다른 round에서 이미 다룬 `204320`, `012330`도 피했다.

선정 종목:

```text
025540 한국단자
073240 금호타이어
033530 SJG세종
```

Hard duplicate 기준인 `canonical_archetype_id + symbol + trigger_type + entry_date` 관점에서 모두 신규 row로 취급 가능하다.

```yaml
new_independent_case_count: 3
same_archetype_new_symbol_count: 3
reused_case_count: 0
do_not_count_as_new_case_count: 0
```

---

## 3. Research question

C29의 잔여 오류는 단순하다.

자동차·타이어·EV 부품주는 시장 전체가 “mobility beta”로 묶는 순간이 많다. 그러나 실제 re-rating은 타이어 가격/원재료 스프레드, OE/RE replacement volume, mix, 고객사 증산, 부품 ASP, 전장화 penetration, margin bridge가 붙을 때만 오래 간다.

따라서 이번 fine-archetype은 다음 질문으로 둔다.

```text
When a tire / auto-component stock moves on mobility-cycle beta,
does the trigger contain company-specific volume, margin, mix, and earnings conversion evidence,
or is it only a sector headline / liquidity spike?
```

핵심 구분선:

```text
generic_mobility_beta_only -> Watch / Stage2-FalsePositive-Candidate
volume + margin + EPS bridge -> Stage2-Actionable or Stage3-Yellow
repeatable margin/volume conversion + controlled MAE -> Stage3-Green candidate
large MFE without bridge + high MAE -> local 4B watch, not full Green
```

---

## 4. Price atlas validation

사용한 가격 데이터는 모두 `Songdaiki/stock-web`의 tradable shard다.

```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
row_count: 14,354,401
tradable_row_count: 14,354,401
max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

Corporate-action contamination check:

```text
025540 한국단자:
  corporate_action_candidate_dates: 1997-01-03, 1999-04-26
  entry~D+180 overlap: none
  calibration_usable: true

073240 금호타이어:
  corporate_action_candidate_dates: 2010-11-02, 2010-12-14, 2018-07-20
  entry~D+180 overlap: none
  calibration_usable: true

033530 SJG세종:
  corporate_action_candidate_dates: 1999-11-29
  entry~D+180 overlap: none
  calibration_usable: true
```

---

## 5. Trigger-level case table

| case_id | symbol | name | trigger_date | entry_date | entry_close | trigger_type | classification |
|---|---:|---|---:|---:|---:|---|---|
| C29-R9L89-001 | 025540 | 한국단자 | 2024-07-26 | 2024-07-26 | 58,700 | Stage2-Actionable / tire-auto connector margin-volume bridge | positive_with_local_4B |
| C29-R9L89-002 | 073240 | 금호타이어 | 2024-01-25 | 2024-01-25 | 5,900 | Stage2-FalsePositive-Candidate / tire margin beta without durable bridge | counterexample_high_MAE |
| C29-R9L89-003 | 033530 | SJG세종 | 2024-02-02 | 2024-02-02 | 6,320 | Stage2-FalsePositive-Candidate / auto-parts mobility beta without conversion | counterexample_hard_4C_candidate |

---

## 6. Backtest result — actual 1D OHLC path

### 6.1 025540 한국단자 — positive with local 4B

Trigger thesis:

```text
auto connector / component content growth + mobility volume/mix beta
```

Observed path:

```text
entry_date: 2024-07-26
entry_close: 58,700
D+30 high: 81,400 on 2024-08-14
D+30 low: 53,500 on 2024-08-05
D+180 high: 86,200 on 2025-02-06
D+180 low: 53,500 on 2024-08-05

MFE_30D: +38.7%
MAE_30D: -8.9%
MFE_90D: +38.7%
MAE_90D: -8.9%
MFE_180D: +46.8%
MAE_180D: -8.9%
```

Interpretation:

한국단자는 단순 자동차 부품 beta보다 더 좋은 표본이다. entry 이후 8월 초 market shock를 견딘 뒤 8월 14일에 큰 MFE가 발생했고, 2025년 2월에는 86,200원까지 추가 MFE가 확장됐다. 다만 spike 구간은 짧고 변동성이 크므로 full Green보다는 `Stage2-Actionable -> Stage3-Yellow candidate + local 4B watch`가 더 안전하다.

E2R route:

```text
baseline_route: Stage2-Actionable
post_path_label: positive_with_local_4B
preferred_route: Stage2-Actionable / Stage3-Yellow candidate, not unconditional Green
```

---

### 6.2 073240 금호타이어 — high-MAE counterexample

Trigger thesis:

```text
tire cycle / margin recovery / replacement demand beta
```

Observed path:

```text
entry_date: 2024-01-25
entry_close: 5,900
near_term_high: 6,880 on 2024-02-19
summer_low: 4,280 on 2024-08-05
later_low_in_window: 4,190 on 2024-09-04

MFE_30D: +16.6%
MAE_30D: about -0.8% to -6.8% depending window endpoint
MFE_90D: about +17.5%
MAE_90D: -29.0%
MFE_180D: about +17.5%
MAE_180D: -29.0%
```

Interpretation:

금호타이어는 tire margin beta가 30D MFE를 만들 수는 있지만, company-specific margin bridge가 약하면 90D/180D에서 high-MAE로 꺾일 수 있다는 반례다. 같은 tire label이라고 해도 한국단자처럼 volume/mix/order conversion이 붙은 부품주와 동일하게 scoring하면 안 된다.

E2R route:

```text
baseline_route: Stage2-FalsePositive-Candidate
post_path_label: counterexample_high_MAE
preferred_route: Watch / Yellow blocked unless margin-earnings bridge appears
```

---

### 6.3 033530 SJG세종 — hard 4C candidate

Trigger thesis:

```text
auto-parts mobility beta / component recovery / hydrogen-mobility optionality
```

Observed path:

```text
entry_date: 2024-02-02
entry_close: 6,320
near_term_high: 6,840 on 2024-03-06
summer_low: 4,085 on 2024-08-05

MFE_30D: +8.2%
MAE_30D: about -8.4%
MFE_90D: +8.2%
MAE_90D: about -19.8%
MFE_180D: +8.2%
MAE_180D: -35.4%
```

Interpretation:

SJG세종은 C29가 가장 조심해야 하는 “mobility label but no conversion” 반례다. 단순 자동차부품 회복 기대, hydrogen/mobility optionality, sector beta만으로는 Stage2-Actionable을 열기 어렵다. 가격경로도 30D MFE가 미약하고 180D MAE가 깊다.

E2R route:

```text
baseline_route: Stage2-FalsePositive-Candidate
post_path_label: hard_4C_candidate
preferred_route: Watch / blocked Stage2 unless actual order-volume-margin bridge is present
```

---

## 7. Score-return alignment

### 7.1 Existing calibrated profile stress test

현재 e2r_2_1_stock_web_calibrated profile은 다음 원칙을 이미 갖는다.

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75
stage3_green_total_min = 87
stage3_green_revision_min = 55
cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4B_requires_non_price_evidence = true
hard_4C_routes_to_4C = true
```

이번 C29 표본을 대입하면:

| symbol | raw path | naive risk | calibrated profile expectation | result |
|---:|---|---|---|---|
| 025540 | high MFE, controlled MAE | local spike over-read | Stage2/Yellow, local 4B watch | aligned |
| 073240 | early MFE then high MAE | tire beta over-read | Watch / false-positive candidate | aligned if bridge gate exists |
| 033530 | low MFE, deep MAE | mobility theme over-read | blocked Stage2 / 4C candidate | aligned |

### 7.2 Residual error

Residual error는 “C29 mobility beta를 너무 넓게 주는 경우”다.

```text
if trigger contains only:
  - tire/auto-parts sector rally
  - mobility/EV component label
  - short-term volume spike
  - generic recovery language
and lacks:
  - OE/RE volume evidence
  - customer production / order bridge
  - ASP / mix / utilization bridge
  - OP/EPS/FCF revision bridge
then:
  block Stage3-Green
  cap at Watch or Stage2-FalsePositive-Candidate
```

---

## 8. Raw component score breakdown

### 8.1 025540 한국단자

```yaml
symbol: "025540"
name: "한국단자"
entry_date: "2024-07-26"
entry_price: 58700
classification: positive_with_local_4B

raw_component_score_breakdown:
  revision_or_earnings_visibility: 16
  revenue_or_order_volume_bridge: 18
  margin_or_mix_bridge: 18
  customer_or_supply_chain_specificity: 14
  balance_sheet_or_fcf_support: 8
  technical_price_quality: 12
  risk_penalty: -6
  price_only_blowoff_penalty: -3
  total_shadow_score: 77

stage_interpretation:
  stage2_actionable: true
  stage3_yellow_candidate: true
  stage3_green_candidate: false
  local_4b_watch: true
```

### 8.2 073240 금호타이어

```yaml
symbol: "073240"
name: "금호타이어"
entry_date: "2024-01-25"
entry_price: 5900
classification: counterexample_high_MAE

raw_component_score_breakdown:
  revision_or_earnings_visibility: 8
  revenue_or_order_volume_bridge: 8
  margin_or_mix_bridge: 10
  customer_or_supply_chain_specificity: 4
  balance_sheet_or_fcf_support: 4
  technical_price_quality: 5
  risk_penalty: -14
  price_only_blowoff_penalty: -4
  total_shadow_score: 21

stage_interpretation:
  stage2_actionable: false
  stage3_yellow_candidate: false
  stage3_green_candidate: false
  local_4b_watch: false
  high_mae_counterexample: true
```

### 8.3 033530 SJG세종

```yaml
symbol: "033530"
name: "SJG세종"
entry_date: "2024-02-02"
entry_price: 6320
classification: hard_4C_candidate

raw_component_score_breakdown:
  revision_or_earnings_visibility: 5
  revenue_or_order_volume_bridge: 5
  margin_or_mix_bridge: 5
  customer_or_supply_chain_specificity: 4
  balance_sheet_or_fcf_support: 3
  technical_price_quality: 2
  risk_penalty: -18
  price_only_blowoff_penalty: -3
  total_shadow_score: 3

stage_interpretation:
  stage2_actionable: false
  stage3_yellow_candidate: false
  stage3_green_candidate: false
  hard_4c_candidate: true
```

---

## 9. Proposed shadow rule candidate

```yaml
rule_id: C29_MOBILITY_VOLUME_MARGIN_BRIDGE_REQUIRED
scope:
  large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
  canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE

rule_type: shadow_rule_only
production_scoring_changed: false
do_not_propose_new_weight_delta: true

positive_gate:
  require_at_least_two:
    - company_specific_order_or_customer_volume_bridge
    - OE_or_RE_replacement_volume_or_utilization_evidence
    - ASP_mix_margin_expansion_evidence
    - OP_EPS_revision_or_FCF_bridge
    - customer_program_award_or_platform_expansion

negative_gate:
  if_only_generic_mobility_beta_or_auto_parts_label:
    max_stage: Watch
  if_price_spike_without_non_price_bridge:
    max_stage: Stage2-FalsePositive-Candidate
  if_MFE_lt_10_and_MAE_gt_25_with_no_bridge:
    route_to: hard_4C_candidate

local_4b_rule:
  if_MFE_30D_or_90D_gt_30_percent:
    require_non_price_bridge_for_full_4B
    otherwise_label: local_4B_watch_only
```

---

## 10. JSONL trigger rows

```jsonl
{"case_id":"C29-R9L89-001","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_COMPONENT_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA_FADE","symbol":"025540","name":"한국단자","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":58700,"trigger_type":"Stage2-Actionable","classification":"positive_with_local_4B","mfe_30d_pct":38.7,"mae_30d_pct":-8.9,"mfe_90d_pct":38.7,"mae_90d_pct":-8.9,"mfe_180d_pct":46.8,"mae_180d_pct":-8.9,"calibration_usable":true,"corporate_action_contaminated_180d":false,"score_alignment":"aligned_if_local_4b_not_full_green","independent_evidence_weight":1.0}
{"case_id":"C29-R9L89-002","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_COMPONENT_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA_FADE","symbol":"073240","name":"금호타이어","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":5900,"trigger_type":"Stage2-FalsePositive-Candidate","classification":"counterexample_high_MAE","mfe_30d_pct":16.6,"mae_30d_pct":-6.8,"mfe_90d_pct":17.5,"mae_90d_pct":-29.0,"mfe_180d_pct":17.5,"mae_180d_pct":-29.0,"calibration_usable":true,"corporate_action_contaminated_180d":false,"score_alignment":"needs_mobility_bridge_gate","independent_evidence_weight":1.0}
{"case_id":"C29-R9L89-003","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_COMPONENT_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA_FADE","symbol":"033530","name":"SJG세종","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":6320,"trigger_type":"Stage2-FalsePositive-Candidate","classification":"hard_4c_candidate","mfe_30d_pct":8.2,"mae_30d_pct":-8.4,"mfe_90d_pct":8.2,"mae_90d_pct":-19.8,"mfe_180d_pct":8.2,"mae_180d_pct":-35.4,"calibration_usable":true,"corporate_action_contaminated_180d":false,"score_alignment":"stage2_should_be_blocked_without_bridge","independent_evidence_weight":1.0}
```

---

## 11. Residual contribution summary

```yaml
new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true
```

C29의 실전 guardrail은 “mobility라는 자동차 큰 단어”가 아니라 “차량당 콘텐츠 / 고객 생산 / OE·RE volume / ASP·mix / OP·EPS 전환”이다. 타이어·자동차부품은 같은 라벨이어도 conversion bridge가 있는 종목과 없는 종목의 90D/180D price path가 크게 갈린다.

---

## 12. Validation scope

```yaml
validation_scope:
  price_data:
    source: Songdaiki/stock-web
    shard_type: tradable_by_symbol_year
    symbols_checked:
      - 025540
      - 073240
      - 033530
    years_checked:
      - 2024
      - 2025
  no_repeat_index_checked: true
  current_live_scan: false
  production_code_patch: false
  production_scoring_change: false
  handoff_prompt_executed_now: false
```

---

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not treat this MD as a production scoring mandate.
This MD is a historical calibration residual artifact.

Input artifact:
e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse the JSONL trigger rows.
2. Add them to the v12 residual research corpus only if they do not violate the No-Repeat hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Preserve do_not_propose_new_weight_delta=true.
4. Consider a shadow-only C29 guard:
   - block Stage3-Green on generic mobility / auto-parts / tire beta without volume-margin-EPS bridge.
   - route weak-MFE/high-MAE cases to Stage2-FalsePositive-Candidate or 4C candidate.
   - mark large MFE without non-price bridge as local_4B_watch_only, not full 4B.
5. Do not patch production scoring unless a separate batch calibration instruction explicitly authorizes it.
```
