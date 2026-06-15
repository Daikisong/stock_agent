# E2R Stock-Web v12 Residual Research
## C01_ORDER_BACKLOG_MARGIN_BRIDGE — transformer / power-equipment backlog-to-margin bridge

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 114
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: TRANSFORMER_POWER_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_GRID_THEME_LABEL_FADE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
created_at_utc: 2026-06-07T04:43:35.086404+00:00
```

## 1. Selection rationale

The latest no-repeat ledger marks `C01_ORDER_BACKLOG_MARGIN_BRIDGE` as Priority 0 with only 16 rows, needing 14 more rows to reach the 30-row minimum stability band and 34 more rows to reach the 50-row practical calibration band.

This loop therefore selected C01 rather than continuing the already-run C08/C09 thin semiconductor routes. The new case set avoids the C01 top-covered symbols shown in the ledger (`082740`, `267270`, `010660`, `044450`, `054540`, `064820`) and uses a new transformer / power-equipment order-backlog bridge cluster:

- `267260` HD Hyundai Electric
- `298040` Hyosung Heavy Industries
- `103590` Iljin Electric

The purpose is not to re-prove a generic “grid CAPEX is bullish” rule. The C01 question is narrower:

> Does the visible order/backlog theme actually convert into company-level revenue, margin, and revision durability, or is it merely a power-equipment label rally?

## 2. Price-source validation

Source manifest:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year"
}
```

Corporate-action rule applied:

```text
if corporate_action_candidate_dates overlap entry_date~D+180:
    calibration_usable = false
else:
    calibration_usable = true
```

All three selected case windows are usable for the local C01 calibration window. Iljin Electric has a profile-level corporate-action candidate on 2024-02-13, so its entry is deliberately placed after that date.

## 3. External evidence / source-proxy spine

This run uses source-proxy evidence rather than repaired exchange filings. Therefore all three cases are marked `source_proxy_only_url_repair_required=true`.

- HD Hyundai Electric is a manufacturer of power transformers and other electrical equipment and had already supplied transformers to many countries before the 2024 order/backlog rerating cycle.
- Hyosung Heavy Industries specializes in power transmission/distribution solutions, transformers, extra-high voltage equipment, and power systems.
- Iljin Electric is connected to high-voltage electrical transmission equipment and high-voltage underground cable / global project exposure through the Iljin group source-proxy.

The research question is whether these business exposures behaved like true C01 backlog-to-margin conversion, not merely whether the companies had power-equipment vocabulary.

## 4. Case table

| case_id | symbol | name | trigger_family | entry_date | entry_close | peak_date | peak_high | max_favorable_excursion | max_adverse_excursion | classification |
|---|---:|---|---|---|---:|---|---:|---:|---:|---|
| C01-114-001 | 267260 | HD현대일렉트릭 | transformer_backlog_margin_bridge | 2024-01-19 | 98,700 | 2024-11-12 | 413,500 | +318.95% | -2.74% | clean_positive |
| C01-114-002 | 298040 | 효성중공업 | power_equipment_backlog_margin_bridge | 2024-01-19 | 177,500 | 2024-11-12 | 518,000 | +191.83% | -12.06% | positive_high_mae_watch |
| C01-114-003 | 103590 | 일진전기 | high_voltage_cable_transformer_order_bridge | 2024-03-04 | 11,960 | 2024-05-29 | 30,250 | +152.93% | local -11.37% / full -35.54% | high_mfe_full_fade_counterexample |

## 5. Case notes

### 5.1 HD Hyundai Electric — clean positive

`267260` is the cleanest C01 example in this loop.

- Profile check: active-like KOSPI, no 2024 corporate-action contamination.
- Entry row: 2024-01-19 close 98,700.
- Local adverse move: 2024-01-24 low 96,000.
- Peak row: 2024-11-12 high 413,500.
- MFE: +318.95%.
- MAE: -2.74%.

Interpretation:

This is the C01 version of a clean bridge: transformer exposure, backlog acceptance, and market confidence in margin conversion all lined up. The price path is not just a one-day theme candle; it sustained the thesis across the year.

Profile stress-test result:

```text
current calibrated profile should allow Stage2-Actionable quickly
Stage3-Green only after non-price backlog/margin/revision evidence
price path supports positive classification
full_4b_requires_non_price_evidence still remains valid
```

### 5.2 Hyosung Heavy Industries — positive, but high-MAE watch

`298040` also worked as a backlog/margin route, but it had a deeper early adverse excursion.

- Profile check: active-like KOSPI, no corporate-action contamination.
- Entry row: 2024-01-19 close 177,500.
- Adverse low: 2024-02-06 low 156,100.
- Peak row: 2024-11-12 high 518,000.
- MFE: +191.83%.
- MAE: -12.06%.

Interpretation:

This is still a C01 positive, but the early drawdown means a naive “order backlog label = Green” rule would be too loose. It should pass Stage2-Actionable with bridge evidence, but Green should require confirmation that backlog quality is passing into gross margin / operating margin rather than simply riding the transformer shortage theme.

Profile stress-test result:

```text
Stage2-Actionable: yes, with backlog and margin bridge
Stage3-Yellow: possible after sustained price + evidence alignment
Stage3-Green: require revision / OPM confirmation
4B local: not primary
high-MAE guardrail: active
```

### 5.3 Iljin Electric — high-MFE but full-window fade

`103590` is the key guardrail case.

- Profile check: active-like KOSPI, corporate-action candidate on 2024-02-13.
- Entry deliberately shifted after the candidate date: 2024-03-04 close 11,960.
- Peak row: 2024-05-29 high 30,250.
- Full-window adverse low: 2024-12-09 low 7,710.
- MFE: +152.93%.
- Full-window MAE: -35.54%.

Interpretation:

Iljin Electric shows that a real high-voltage equipment / cable label can generate a large C01-style move, but the full-window fade is too large to treat as clean Green without company-level order quality and margin conversion. This is not a “bad company” statement; it is a profile guardrail. C01 needs to distinguish:

```text
category backlog tailwind
    vs
company-specific backlog quality
    vs
margin/revision conversion
```

Profile stress-test result:

```text
Stage2 may be allowed locally
Stage3-Green should be blocked without margin/revision confirmation
full 4B watch is appropriate
classification: high-MFE/full-fade counterexample to loose Green
```

## 6. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"TRANSFORMER_POWER_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_GRID_THEME_LABEL_FADE","symbol":"267260","name":"HD현대일렉트릭","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":98700,"peak_date":"2024-11-12","peak_high":413500,"mfe_pct":318.95,"mae_pct":-2.74,"classification":"clean_positive","calibration_usable":true,"source_proxy_only_url_repair_required":true,"duplicate_check":"new_symbol_for_C01_not_in_top_covered_set"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"TRANSFORMER_POWER_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_GRID_THEME_LABEL_FADE","symbol":"298040","name":"효성중공업","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":177500,"peak_date":"2024-11-12","peak_high":518000,"mfe_pct":191.83,"mae_pct":-12.06,"classification":"positive_high_mae_watch","calibration_usable":true,"source_proxy_only_url_repair_required":true,"duplicate_check":"new_symbol_for_C01_not_in_top_covered_set"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"TRANSFORMER_POWER_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_GRID_THEME_LABEL_FADE","symbol":"103590","name":"일진전기","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":11960,"peak_date":"2024-05-29","peak_high":30250,"mfe_pct":152.93,"mae_pct":-35.54,"classification":"high_mfe_full_fade_counterexample","calibration_usable":true,"source_proxy_only_url_repair_required":true,"duplicate_check":"new_symbol_for_C01_not_in_top_covered_set","corporate_action_note":"profile candidate 2024-02-13; entry selected after candidate date"}
```

## 7. Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","symbol":"267260","baseline_proxy":"e2r_2_2_rolling_calibrated","stage2_actionable_evidence_bonus":2.0,"stage3_green_revision_min":55.0,"price_only_blowoff_blocks_positive_stage":true,"expected_stage":"Stage3-Yellow_to_Green_if_revision_confirmed","residual_error":"under-recognition risk if C01 backlog-to-margin bridge is compressed into generic C02 grid capex"}
{"row_type":"score_simulation","symbol":"298040","baseline_proxy":"e2r_2_2_rolling_calibrated","stage2_actionable_evidence_bonus":2.0,"stage3_green_revision_min":55.0,"price_only_blowoff_blocks_positive_stage":true,"expected_stage":"Stage2-Actionable_to_Stage3-Yellow","residual_error":"Green too early if early MAE and margin evidence are ignored"}
{"row_type":"score_simulation","symbol":"103590","baseline_proxy":"e2r_2_2_rolling_calibrated","stage2_actionable_evidence_bonus":2.0,"stage3_green_revision_min":55.0,"price_only_blowoff_blocks_positive_stage":true,"expected_stage":"Stage2_local_or_4B_watch","residual_error":"loose Green if high-MFE theme path is not separated from full-window fade"}
```

## 8. Aggregate metric JSONL

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","case_count":3,"trigger_count":3,"positive_case_count":2,"counterexample_count":1,"high_mae_watch_count":2,"clean_positive_count":1,"source_proxy_only_count":3,"verified_url_repair_needed_count":3,"median_mfe_pct":191.83,"median_mae_pct":-12.06}
```

## 9. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","scope":"canonical_archetype","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"c01_backlog_to_margin_revision_bridge_required","direction":"tighten_green_allow_stage2","suggested_delta":"+0.25 only when backlog/revenue/margin bridge is explicit; -0.35 when only sector theme or orderbook label exists","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight","scope":"large_sector","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","axis":"grid_power_equipment_backlog_bridge_not_same_as_generic_grid_capex","direction":"separate_C01_from_C02","suggested_delta":"route power-equipment companies to C01 only when order backlog and margin/revision are explicit; otherwise leave in C02/C31 theme bucket","production_scoring_changed":false,"shadow_weight_only":true}
```

Rule language:

> C01 should reward companies where order backlog is visible and plausibly margin-accretive. It should not blindly reward every grid/transformer/cable label. For Green, require at least one non-price bridge: contract/order disclosure, backlog mix, capacity lock, ASP/margin improvement, or earnings revision. Without that bridge, strong MFE should remain 4B watch or Stage2-only.

## 10. Residual contribution summary

```text
completed_round = R1
completed_loop = 114
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 2
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 3
verified_url_repair_needed_count = 3

diversity_score_summary = C01 Priority 0 보강 + HD현대일렉트릭 clean backlog/margin positive + 효성중공업 positive/high-MAE watch + 일진전기 high-MFE/full-fade counterexample
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C01 rows 16, 30-row target까지 14 부족, 50-row target까지 34 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c01_backlog_to_margin_revision_bridge_required
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C01 order-backlog/power-equipment rallies
existing_axis_weakened = null
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session.

```text
You are a coding agent implementing accumulated E2R v12 research MDs.

Read this MD as a deferred handoff artifact only. Do not treat it as a live stock recommendation.

Task:
- Parse trigger, aggregate_metric, score_simulation, shadow_weight rows.
- Add the C01-specific shadow rule candidate:
  c01_backlog_to_margin_revision_bridge_required
- Ensure no production scoring is changed unless batch review explicitly approves it.
- Keep C01 separated from generic C02 grid capex:
  C01 = order backlog + margin/revision conversion bridge.
  C02 = power grid/datacenter capex exposure and capacity-lock theme.
- Preserve the high-MFE/full-fade counterexample behavior for Iljin Electric-like paths.
- Do not re-ingest duplicate keys:
  canonical_archetype_id + symbol + trigger_type + entry_date.
```
