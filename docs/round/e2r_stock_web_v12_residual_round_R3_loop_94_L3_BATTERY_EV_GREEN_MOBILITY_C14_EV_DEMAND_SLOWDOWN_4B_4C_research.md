---
schema_family: v12_sector_archetype_residual
research_round: R3
research_loop: 94
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_HARD_4C_VS_FALSE_4C_RECOVERY
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - high_MAE_guardrail
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
evidence_status: source_proxy_only
evidence_url_pending: true
created_at: 2026-06-06
---

# E2R Stock-Web v12 Residual Research — R3 loop 94 / L3 / C14

## 0. Executive summary

이번 loop는 **C14_EV_DEMAND_SLOWDOWN_4B_4C**의 coverage gap을 채우기 위한 residual research다. C14는 EV/battery chain에서 가장 쉽게 착시가 생기는 영역이다. 가격이 크게 빠졌다는 사실만으로 hard 4C를 확정하면 LG에너지솔루션처럼 회복하는 셀 대표주를 놓치고, 반대로 초기 반등만 보고 4C를 늦추면 에코프로비엠·엘앤에프·SK아이이테크놀로지처럼 깊은 MAE를 허용한다.

핵심 분리축은 다음이다.

```text
EV demand slowdown headline
  ≠ automatic hard 4C

hard 4C requires:
  customer call-off / utilization drop / margin guidance break / order cut / capex delay / thesis break confirmation

local 4B or false 4C recovery requires:
  no durable non-price thesis break + price recovery with cleaner demand/revision signal
```

## 1. Selection and novelty check

```text
selected_round = R3
selected_loop = 94
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_HARD_4C_VS_FALSE_4C_RECOVERY
selected_priority_bucket = Priority 0
```

Novelty checks:

```text
C14 current index rows = 21
need_to_30 = 9
selected purpose = EV demand slowdown / utilization / call-off / hard 4C timing test
prior C14 registry max observed = R3 loop 93
this output loop = R3 loop 94
hard duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date
```

This file intentionally uses **fresh trigger family framing** rather than re-proving generic "price-only blowoff should be blocked." The trigger family is: EV demand slowdown + utilization/call-off/margin break vs false 4C recovery.

## 2. Price source validation

Stock-Web validation basis:

```text
price_atlas_repo = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Usable symbols:

| symbol | name | profile status | 2024 shard | CA caveat |
|---|---|---|---|---|
| 373220 | LG에너지솔루션 | active_like | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | clean, no CA candidate in profile |
| 247540 | 에코프로비엠 | active_like | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | old CA candidates only, outside 2024 window |
| 066970 | 엘앤에프 | active_like | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | old CA candidates only, outside 2024 window |
| 361610 | SK아이이테크놀로지 | active_like | atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv | clean, no CA candidate in profile |

## 3. Trigger table

| case_id | symbol | name | entry_date | entry_price | trigger_type | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | residual label |
|---|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| C14-LGES-2024-01-22-EV_DEMAND_SLOWDOWN_HARD_4C_STRESS | 373220 | LG에너지솔루션 | 2024-01-22 | 372,000 | EV_DEMAND_SLOWDOWN_MARGIN_UTILIZATION_WARNING | 10.89% | -2.69% | 12.90% | -12.63% | 19.35% | -16.40% | false_hard_4c / local 4B recovery after demand-slowdown scare |
| C14-ECOPROBM-2024-01-22-CATHODE_CALL_OFF_DECAY | 247540 | 에코프로비엠 | 2024-01-22 | 248,000 | CATHODE_EV_DEMAND_SLOWDOWN_CALL_OFF_RISK | 10.08% | -14.92% | 19.56% | -25.00% | 19.56% | -40.04% | true_4C_after_transient_rebound |
| C14-LNF-2024-01-29-MATERIAL_DEMAND_BREAK | 066970 | 엘앤에프 | 2024-01-29 | 145,100 | CATHODE_MATERIAL_DEMAND_SLOWDOWN_MARGIN_BREAK | 20.81% | -8.96% | 37.15% | -22.61% | 37.15% | -42.87% | true_4C_with_high_MFE_trap |
| C14-SKIET-2024-01-22-SEPARATOR_UTILIZATION_BREAK | 361610 | SK아이이테크놀로지 | 2024-01-22 | 72,100 | SEPARATOR_EV_DEMAND_SLOWDOWN_UTILIZATION_BREAK | 10.96% | -9.71% | 10.96% | -47.57% | 10.96% | -58.32% | clean_hard_4C |

## 4. Case notes

### C14-LGES-2024-01-22-EV_DEMAND_SLOWDOWN_HARD_4C_STRESS

```text
symbol = 373220
name = LG에너지솔루션
entry_date = 2024-01-22
entry_price = 372000
trigger_type = EV_DEMAND_SLOWDOWN_MARGIN_UTILIZATION_WARNING
max_high_window_marker = 444000 on 2024-10-08
min_low_window_marker = 311000 on 2024-08-05
residual_label = false_hard_4c / local 4B recovery after demand-slowdown scare
```

Interpretation:

셀 대표주는 EV 수요둔화 헤드라인에도 2024년 하반기 반등 창을 만들었다. C14에서 hard 4C는 price drawdown alone이 아니라 utilization/order-cut/margin break confirm이 필요.

### C14-ECOPROBM-2024-01-22-CATHODE_CALL_OFF_DECAY

```text
symbol = 247540
name = 에코프로비엠
entry_date = 2024-01-22
entry_price = 248000
trigger_type = CATHODE_EV_DEMAND_SLOWDOWN_CALL_OFF_RISK
max_high_window_marker = 296500 on 2024-03-25
min_low_window_marker = 148700 on 2024-09-10
residual_label = true_4C_after_transient_rebound
```

Interpretation:

초기 반등은 강했지만 180D 창에서 -40% MAE가 열렸다. orderbook headline보다 customer call-off/utilization/margin confirmation이 우선이라는 반례.

### C14-LNF-2024-01-29-MATERIAL_DEMAND_BREAK

```text
symbol = 066970
name = 엘앤에프
entry_date = 2024-01-29
entry_price = 145100
trigger_type = CATHODE_MATERIAL_DEMAND_SLOWDOWN_MARGIN_BREAK
max_high_window_marker = 199000 on 2024-03-25
min_low_window_marker = 82900 on 2024-09-10
residual_label = true_4C_with_high_MFE_trap
```

Interpretation:

중간 MFE가 컸으나 이후 180D MAE가 심했다. C14에서는 MFE만 보고 false 4C로 풀면 안 되고, peak 이후 utilization/guidance break를 다시 물어야 한다.

### C14-SKIET-2024-01-22-SEPARATOR_UTILIZATION_BREAK

```text
symbol = 361610
name = SK아이이테크놀로지
entry_date = 2024-01-22
entry_price = 72100
trigger_type = SEPARATOR_EV_DEMAND_SLOWDOWN_UTILIZATION_BREAK
max_high_window_marker = 80000 on 2024-01-26
min_low_window_marker = 30050 on 2024-09-10
residual_label = clean_hard_4C
```

Interpretation:

분리막 utilization break가 붙는 순간 단순 price-only 4B가 아니라 hard 4C로 빨리 보내야 하는 대표 반례.

## 5. Current calibrated profile stress-test

The current calibrated profile should not collapse C14 into one rule. The correct behavior is a fork.

### Fork A — hard 4C should be accelerated

Applies when:

```text
EV demand slowdown headline
+ customer call-off or utilization break
+ margin/guidance revision pressure
+ no confirmed order/revenue bridge
+ persistent lower-low price path
```

Observed examples:

```text
247540 에코프로비엠
066970 엘앤에프
361610 SK아이이테크놀로지
```

### Fork B — hard 4C should be delayed until non-price confirmation

Applies when:

```text
EV demand slowdown headline
+ local price drawdown
but no durable customer/order/margin thesis break confirmation
and price/revision path stabilizes
```

Observed example:

```text
373220 LG에너지솔루션
```

This distinction matters because a crude C14 rule would either over-protect and miss the rebound, or under-protect and allow a high-MAE trap.

## 6. Shadow rule candidate

```json
{
  "patch_axis": "hard_4c_confirmation",
  "scope": {
    "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
    "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C"
  },
  "candidate_rule": "Within C14, upgrade to hard 4C only when EV-demand-slowdown vocabulary is paired with at least two non-price break signals: customer call-off/order cut, utilization drop, margin/guidance cut, capex delay, or failure of orderbook-to-revenue bridge. If only price drawdown and generic EV slowdown headline exist, route to local_4B_watch or Stage3-Red watch rather than hard 4C.",
  "why_not_global": "EV slowdown language is too broad. Cell makers, cathode makers, separators, and equipment/material suppliers exhibit different recovery and drawdown profiles.",
  "production_ready": false,
  "blocking_reason": "source_proxy_only; evidence_url_pending; requires exact non-price URL verification before promotion"
}
```

## 7. Every usable trigger as JSONL

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_round": "R3", "research_loop": 94, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_CELL_EV_DEMAND_SLOWDOWN_RECOVERY_VS_TRUE_4C", "symbol": "373220", "name": "LG에너지솔루션", "trigger_type": "EV_DEMAND_SLOWDOWN_MARGIN_UTILIZATION_WARNING", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 372000, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 10.89, "MAE_30D_pct": -2.69, "MFE_90D_pct": 12.9, "MAE_90D_pct": -12.63, "MFE_180D_pct": 19.35, "MAE_180D_pct": -16.4, "current_profile_stage": "Stage2-Yellow/4B-watch", "residual_label": "false_hard_4c / local 4B recovery after demand-slowdown scare", "evidence_status": "source_proxy_only", "evidence_url_pending": true, "do_not_count_for_production_promotion": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_round": "R3", "research_loop": 94, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_ORDERBOOK_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_REBOUND_SPIKE", "symbol": "247540", "name": "에코프로비엠", "trigger_type": "CATHODE_EV_DEMAND_SLOWDOWN_CALL_OFF_RISK", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 248000, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 10.08, "MAE_30D_pct": -14.92, "MFE_90D_pct": 19.56, "MAE_90D_pct": -25.0, "MFE_180D_pct": 19.56, "MAE_180D_pct": -40.04, "current_profile_stage": "Stage3-Red/4C-watch", "residual_label": "true_4C_after_transient_rebound", "evidence_status": "source_proxy_only", "evidence_url_pending": true, "do_not_count_for_production_promotion": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_round": "R3", "research_loop": 94, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_MATERIAL_EV_DEMAND_SLOWDOWN_TRUE_4C_WITH_VOLATILE_REBOUND", "symbol": "066970", "name": "엘앤에프", "trigger_type": "CATHODE_MATERIAL_DEMAND_SLOWDOWN_MARGIN_BREAK", "trigger_date": "2024-01-29", "entry_date": "2024-01-29", "entry_price": 145100, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 20.81, "MAE_30D_pct": -8.96, "MFE_90D_pct": 37.15, "MAE_90D_pct": -22.61, "MFE_180D_pct": 37.15, "MAE_180D_pct": -42.87, "current_profile_stage": "Stage3-Red/4C-confirm", "residual_label": "true_4C_with_high_MFE_trap", "evidence_status": "source_proxy_only", "evidence_url_pending": true, "do_not_count_for_production_promotion": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_round": "R3", "research_loop": 94, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_UTILIZATION_EV_DEMAND_SLOWDOWN_HARD_4C", "symbol": "361610", "name": "SK아이이테크놀로지", "trigger_type": "SEPARATOR_EV_DEMAND_SLOWDOWN_UTILIZATION_BREAK", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 72100, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 10.96, "MAE_30D_pct": -9.71, "MFE_90D_pct": 10.96, "MAE_90D_pct": -47.57, "MFE_180D_pct": 10.96, "MAE_180D_pct": -58.32, "current_profile_stage": "4C-confirm", "residual_label": "clean_hard_4C", "evidence_status": "source_proxy_only", "evidence_url_pending": true, "do_not_count_for_production_promotion": true}
```

## 8. Residual contribution summary

```text
positive_or_recovery_case_count = 1
hard_4c_case_count = 3
counterexample_balance = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
evidence_status = source_proxy_only
promotion_ready = false
production_scoring_changed = false
```

Residual lesson:

```text
C14 is not simply "EV down = 4C".
C14 should behave like a circuit breaker with a fuse:
- price decline is heat,
- non-price thesis break is the fuse melting.
Without the fuse, keep it as local 4B/Stage3-Red watch.
With the fuse, move to hard 4C earlier.
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not treat this MD as an immediately applicable production patch.

Task:
1. Ingest this MD as v12 residual research.
2. Parse trigger JSONL rows.
3. Keep rows as source_proxy_only / evidence_url_pending.
4. Do not promote the proposed hard_4c_confirmation rule until exact non-price evidence URLs are verified.
5. If verified, consider a C14-scoped rule that requires at least two non-price thesis-break signals before hard 4C.
6. Preserve the false-hard-4C recovery case separately from true hard-4C cases.
```

## 10. Next research state

```text
completed_round = R3
completed_loop = 94
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
