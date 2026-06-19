# E2R v12 Stock-Web Residual Research — R1 / L1 / C05 EPC Mega Contract Margin Gap

```text
research_session = post_calibrated_sector_archetype_residual_research_v12
selected_round = R1
selected_loop = 206
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4
output_file = e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement + Priority 0 direct evidence/url-quality repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale / novelty check

The current No-Repeat Index says the corpus is no longer short of 30/50/80 rows for C01~C32. The next valuable loops are quality repairs: verified URL repair, source-proxy reduction, missing MFE/MAE repair, and Priority 1 balance reinforcement. C05 is still a Priority 1 target because the index calls for **margin / working-capital failure counterexamples and 4C timing reinforcement**.

This loop therefore stays inside C05 but avoids the latest repeated large-cap EPC set by using smaller or mid-sized construction/EPC issuers with different failure modes:

```text
new independent trigger families:
- FY2024 loss / high cost-rate watch that later reopens
- Q1 2025 profit-turn + backlog/cost-structure bridge
- record order/revenue but operating profit decline due to rising costs
- Saudi EPC order headline with weak margin/cash conversion
- positive operating profit with deep 180D MAE cap
```

Hard duplicate key used for rejection:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No usable trigger below repeats a hard duplicate key from the recent C05 loops in this session.

## 2. Stock-Web price source validation

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
entry_rule = first tradable row on or after evidence_date
MFE/MAE rule = max high / min low from entry row through N tradable rows, against entry close
```

Checked shards:

```text
atlas/ohlcv_tradable_by_symbol_year/005/005960/2025.csv
atlas/ohlcv_tradable_by_symbol_year/005/005960/2026.csv
atlas/ohlcv_tradable_by_symbol_year/002/002990/2025.csv
atlas/ohlcv_tradable_by_symbol_year/002/002990/2026.csv
atlas/ohlcv_tradable_by_symbol_year/013/013580/2025.csv
atlas/ohlcv_tradable_by_symbol_year/013/013580/2026.csv
atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv
atlas/ohlcv_tradable_by_symbol_year/016/016250/2025.csv
```

Profile checks:

```text
005960 Dongbu Construction: corporate_action_candidate_dates are historical only for this window; 180D usable.
002990 Kumho E&C: corporate_action_candidate_dates are historical only for this window; 180D usable.
013580 Kyeryong Construction: corporate_action_candidate_dates are historical only for this window; 180D usable.
016250 SGC E&C: profile has a 2025-06-25 corporate-action candidate, but both usable 2024 entries have 180D windows ending before that date; 180D usable.
```

## 3. Evidence summary

- **Dongbu Construction / 005960**: FY2024 loss and revenue decline created a C05 cost-rate watch, but Q1 2025 then showed operating-profit turnaround, high-profit new orders, debt-ratio improvement, and order backlog around KRW10.3tn. This is the archetypal “do not keep hard 4C sticky after cost-rate reset + backlog bridge” case.
- **Kumho E&C / 002990**: 2024 operating loss was driven by high costs and project delays; later 2025 reporting showed three quarters of operating profit and cost-of-sales ratio improvement. The 2025-02 trigger is therefore a 4B/watch row, not a hard 4C row.
- **Kyeryong Construction / 013580**: revenue and orders were strong and debt ratio improved, but operating profit still declined due to rising costs. The price path was exceptional, but the evidence supports Stage2 cap rather than Stage2-Actionable/Yellow without cash-margin bridge.
- **SGC E&C / 016250**: Q1 2024 turned operating profit positive and Saudi orders were large, but 180D MAE remained deep. The later August 2024 Saudi order headline had almost no forward MFE and severe MAE, showing that EPC order headlines alone do not equal cash/margin conversion.

## 4. Trigger-level backtest table

| symbol | trigger | evidence_date | entry_date | entry OHLCV | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak/trough | role |
|---|---|---:|---:|---|---:|---:|---:|---|---|
| 005960 Dongbu Construction | Stage4B | 2025-02-04 | 2025-02-04 | O 3,430 / H 3,450 / L 3,400 / C 3,415 / V 25,798 | 6.73 / -0.73 | 62.52 / -1.17 | 101.76 / -1.17 | 2025-09-11 / 2025-04-07 | 4B_reopen_control |
| 005960 Dongbu Construction | Stage2-Actionable | 2025-05-15 | 2025-05-15 | O 4,145 / H 4,245 / L 3,960 / C 4,215 / V 45,727 | 31.91 / -6.05 | 63.46 / -6.05 | 63.46 / -6.05 | 2025-09-11 / 2025-05-15 | positive_reopen |
| 002990 Kumho E&C | Stage4B | 2025-02-17 | 2025-02-17 | O 2,650 / H 2,675 / L 2,600 / C 2,625 / V 66,321 | 8.57 / -6.86 | 36.19 / -8.57 | 65.33 / -8.57 | 2025-09-08 / 2025-04-09 | 4B_not_4C_control |
| 013580 Kyeryong Construction Industrial | Stage2 | 2025-03-13 | 2025-03-13 | O 13,460 / H 13,610 / L 13,300 / C 13,400 / V 20,259 | 136.94 / -5.22 | 136.94 / -5.22 | 136.94 / -5.22 | 2025-04-23 / 2025-04-03 | stage2_cap_high_mfe_control |
| 016250 SGC E&C | Stage2-Actionable | 2024-04-23 | 2024-04-23 | O 15,300 / H 15,580 / L 15,200 / C 15,450 / V 4,538 | 8.74 / -1.62 | 21.29 / -9.39 | 21.29 / -23.82 | 2024-08-05 / 2024-12-09 | positive_with_high_mae_cap |
| 016250 SGC E&C | Stage4B | 2024-08-29 | 2024-08-29 | O 16,760 / H 16,760 / L 16,250 / C 16,600 / V 13,285 | 1.45 / -8.73 | 1.45 / -29.10 | 5.12 / -29.10 | 2025-05-23 / 2024-12-09 | order_without_conversion_counterexample |


## 5. Current calibrated profile stress test

| symbol | trigger | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | total | profile stress |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 005960 | Stage4B | 8 | 12 | 6 | 10 | 8 | 5 | 12 | 61.0 | Green blocked by MAE/bridge gap |
| 005960 | Stage2-Actionable | 16 | 18 | 9 | 11 | 10 | 6 | 9 | 79.0 | Stage2/Actionable preserved |
| 002990 | Stage4B | 7 | 10 | 5 | 11 | 8 | 5 | 11 | 57.0 | Green blocked by MAE/bridge gap |
| 013580 | Stage2 | 12 | 16 | 8 | 12 | 9 | 6 | 9 | 72.0 | Stage2/Actionable preserved |
| 016250 | Stage2-Actionable | 13 | 17 | 13 | 10 | 8 | 5 | 10 | 76.0 | Green blocked by MAE/bridge gap |
| 016250 | Stage4B | 11 | 15 | 10 | 10 | 7 | 4 | 9 | 66.0 | Green blocked by MAE/bridge gap |


Interpretation:

```text
current_profile_error_count = 4
positive_or_reopen_case_count = 3
counterexample_or_guardrail_case_count = 3
stage2_like_count = 3
stage4b_count = 3
stage4c_count = 0
calibration_usable_trigger_count = 6
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
```

The residual error is not that C05 should be more bullish. It is narrower:

```text
- hard 4C can be too sticky after a cost-rate reset if backlog/order and debt/cost structure recover.
- Stage2-Actionable needs a second bridge, not merely a large EPC/order headline.
- a high-MFE row can still remain Stage2-capped when evidence lacks cashflow/working-capital conversion.
- deep MAE on an otherwise valid order/profit bridge should block Yellow/Green first, not delete Stage2.
```

## 6. Residual contribution summary

```text
rule_candidate = C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4
sector_rule_candidate = L1_EPC_COST_RATE_RESET_AND_CASHFLOW_REOPEN_GATE
new_axis_proposed = false
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, hard_4c_confirmation
existing_axis_refined = C05 hard_4C requires trust/liquidity/backlog break; cost-rate loss alone is 4B unless offset quality is absent
existing_axis_weakened = none_global
production_scoring_changed = false
shadow_weight_only = true
```

Proposed C05-specific shadow rule:

```text
C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4:
  - EPC order/backlog/revenue headline alone cannot create Stage2-Actionable, Yellow, or Green.
  - Stage2-Actionable requires at least one direct second bridge:
      cost-rate recovery,
      operating-profit conversion,
      working-capital release,
      debt/net-cash improvement,
      backlog-to-revenue conversion,
      high-profit new order mix,
      or cashflow visibility.
  - FY loss, cost-rate shock, project delay, or debt-ratio stress routes first to Stage4B/watch.
  - hard Stage4C requires confirmed non-price thesis break:
      liquidity stress,
      accounting/trust break,
      backlog/order collapse,
      license/regulatory damage,
      or weak offset quality.
  - after a trust/cost-rate break, Stage2-Actionable reopen is allowed only when direct cost/debt/order/cash bridge appears.
  - high MFE after ugly earnings is a warning against hard-4C stickiness;
    high MAE on valid bridge rows blocks Yellow/Green first.
```

## 7. Machine-readable JSONL trigger rows

```jsonl
{"row_type":"trigger","research_version":"v12_stock_web_residual","selected_round":"R1","selected_loop":206,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4","symbol":"005960","company_name":"Dongbu Construction","case_id":"C05_005960_2025_02_04_4B_COST_RATE_LOSS","trigger_type":"Stage4B","evidence_date":"2025-02-04","entry_date":"2025-02-04","entry_price":3415,"entry_ohlcv":{"o":3430,"h":3450,"l":3400,"c":3415,"v":25798},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","actual_stock_web_row_used":true,"forward_180d_last_date":"2025-10-29","corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"mfe_30d_pct":6.73,"mae_30d_pct":-0.73,"mfe_90d_pct":62.52,"mae_90d_pct":-1.17,"mfe_180d_pct":101.76,"mae_180d_pct":-1.17,"peak_180d_date":"2025-09-11","trough_180d_date":"2025-04-07"},"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":12,"bottleneck_pricing":6,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":5,"information_confidence":12},"score_simulation":{"current_profile_total":61.0,"green_blocked":true,"production_scoring_changed":false},"case_role":"4B_reopen_control","evidence_summary":"FY2024 operating loss and revenue decline created cost-rate/working-capital watch, but price path says hard 4C would have been too sticky.","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|005960|Stage4B|2025-02-04","representative_for_aggregate":true}
{"row_type":"trigger","research_version":"v12_stock_web_residual","selected_round":"R1","selected_loop":206,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4","symbol":"005960","company_name":"Dongbu Construction","case_id":"C05_005960_2025_05_15_STAGE2A_TURNAROUND_ORDER_BACKLOG","trigger_type":"Stage2-Actionable","evidence_date":"2025-05-15","entry_date":"2025-05-15","entry_price":4215,"entry_ohlcv":{"o":4145,"h":4245,"l":3960,"c":4215,"v":45727},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","actual_stock_web_row_used":true,"forward_180d_last_date":"2026-02-05","corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"mfe_30d_pct":31.91,"mae_30d_pct":-6.05,"mfe_90d_pct":63.46,"mae_90d_pct":-6.05,"mfe_180d_pct":63.46,"mae_180d_pct":-6.05,"peak_180d_date":"2025-09-11","trough_180d_date":"2025-05-15"},"raw_component_score_breakdown":{"eps_fcf_explosion":16,"earnings_visibility":18,"bottleneck_pricing":9,"market_mispricing":11,"valuation_rerating":10,"capital_allocation":6,"information_confidence":9},"score_simulation":{"current_profile_total":79.0,"green_blocked":false,"production_scoring_changed":false},"case_role":"positive_reopen","evidence_summary":"Q1 2025 consolidated operating profit turned positive; high-profit new orders, reduced borrowings, lower debt ratio, order backlog around KRW10.3tn.","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|005960|Stage2-Actionable|2025-05-15","representative_for_aggregate":true}
{"row_type":"trigger","research_version":"v12_stock_web_residual","selected_round":"R1","selected_loop":206,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4","symbol":"002990","company_name":"Kumho E&C","case_id":"C05_002990_2025_02_17_4B_HIGH_COST_RATIO_DEFICIT","trigger_type":"Stage4B","evidence_date":"2025-02-17","entry_date":"2025-02-17","entry_price":2625,"entry_ohlcv":{"o":2650,"h":2675,"l":2600,"c":2625,"v":66321},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","actual_stock_web_row_used":true,"forward_180d_last_date":"2025-11-11","corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"mfe_30d_pct":8.57,"mae_30d_pct":-6.86,"mfe_90d_pct":36.19,"mae_90d_pct":-8.57,"mfe_180d_pct":65.33,"mae_180d_pct":-8.57,"peak_180d_date":"2025-09-08","trough_180d_date":"2025-04-09"},"raw_component_score_breakdown":{"eps_fcf_explosion":7,"earnings_visibility":10,"bottleneck_pricing":5,"market_mispricing":11,"valuation_rerating":8,"capital_allocation":5,"information_confidence":11},"score_simulation":{"current_profile_total":57.0,"green_blocked":true,"production_scoring_changed":false},"case_role":"4B_not_4C_control","evidence_summary":"FY2024 operating deficit/cost burden was a watch signal; later cost-ratio improvement means hard 4C should require confirmed liquidity/accounting break.","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|002990|Stage4B|2025-02-17","representative_for_aggregate":true}
{"row_type":"trigger","research_version":"v12_stock_web_residual","selected_round":"R1","selected_loop":206,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4","symbol":"013580","company_name":"Kyeryong Construction Industrial","case_id":"C05_013580_2025_03_13_STAGE2_RECORD_ORDER_COST_PRESSURE","trigger_type":"Stage2","evidence_date":"2025-03-13","entry_date":"2025-03-13","entry_price":13400,"entry_ohlcv":{"o":13460,"h":13610,"l":13300,"c":13400,"v":20259},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","actual_stock_web_row_used":true,"forward_180d_last_date":"2025-12-05","corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"mfe_30d_pct":136.94,"mae_30d_pct":-5.22,"mfe_90d_pct":136.94,"mae_90d_pct":-5.22,"mfe_180d_pct":136.94,"mae_180d_pct":-5.22,"peak_180d_date":"2025-04-23","trough_180d_date":"2025-04-03"},"raw_component_score_breakdown":{"eps_fcf_explosion":12,"earnings_visibility":16,"bottleneck_pricing":8,"market_mispricing":12,"valuation_rerating":9,"capital_allocation":6,"information_confidence":9},"score_simulation":{"current_profile_total":72.0,"green_blocked":false,"production_scoring_changed":false},"case_role":"stage2_cap_high_mfe_control","evidence_summary":"Revenue and orders were strong, debt ratio improved, but operating profit declined due to rising costs; this is Stage2, not Actionable/Yellow without cash-margin bridge.","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|013580|Stage2|2025-03-13","representative_for_aggregate":true}
{"row_type":"trigger","research_version":"v12_stock_web_residual","selected_round":"R1","selected_loop":206,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4","symbol":"016250","company_name":"SGC E&C","case_id":"C05_016250_2024_04_23_STAGE2A_ORDER_BACKLOG_PROFIT_TURN","trigger_type":"Stage2-Actionable","evidence_date":"2024-04-23","entry_date":"2024-04-23","entry_price":15450,"entry_ohlcv":{"o":15300,"h":15580,"l":15200,"c":15450,"v":4538},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","actual_stock_web_row_used":true,"forward_180d_last_date":"2025-01-17","corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"mfe_30d_pct":8.74,"mae_30d_pct":-1.62,"mfe_90d_pct":21.29,"mae_90d_pct":-9.39,"mfe_180d_pct":21.29,"mae_180d_pct":-23.82,"peak_180d_date":"2024-08-05","trough_180d_date":"2024-12-09"},"raw_component_score_breakdown":{"eps_fcf_explosion":13,"earnings_visibility":17,"bottleneck_pricing":13,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":5,"information_confidence":10},"score_simulation":{"current_profile_total":76.0,"green_blocked":true,"production_scoring_changed":false},"case_role":"positive_with_high_mae_cap","evidence_summary":"Q1 operating profit was positive, Saudi orders exceeded KRW1tn and PF/cost overhang was claimed to be easing; MAE still argues against Yellow/Green.","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|016250|Stage2-Actionable|2024-04-23","representative_for_aggregate":true}
{"row_type":"trigger","research_version":"v12_stock_web_residual","selected_round":"R1","selected_loop":206,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4","symbol":"016250","company_name":"SGC E&C","case_id":"C05_016250_2024_08_29_4B_SAUDI_ORDER_CONVERSION_GAP","trigger_type":"Stage4B","evidence_date":"2024-08-29","entry_date":"2024-08-29","entry_price":16600,"entry_ohlcv":{"o":16760,"h":16760,"l":16250,"c":16600,"v":13285},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","actual_stock_web_row_used":true,"forward_180d_last_date":"2025-05-30","corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"mfe_30d_pct":1.45,"mae_30d_pct":-8.73,"mfe_90d_pct":1.45,"mae_90d_pct":-29.1,"mfe_180d_pct":5.12,"mae_180d_pct":-29.1,"peak_180d_date":"2025-05-23","trough_180d_date":"2024-12-09"},"raw_component_score_breakdown":{"eps_fcf_explosion":11,"earnings_visibility":15,"bottleneck_pricing":10,"market_mispricing":10,"valuation_rerating":7,"capital_allocation":4,"information_confidence":9},"score_simulation":{"current_profile_total":66.0,"green_blocked":true,"production_scoring_changed":false},"case_role":"order_without_conversion_counterexample","evidence_summary":"KRW490bn Saudi chemical-facility contracts added backlog, but forward path shows order headline alone did not create margin/cash conversion; local 4B/watch.","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|016250|Stage4B|2024-08-29","representative_for_aggregate":true}
```

## 8. Aggregate row

```json
{
  "row_type": "aggregate",
  "research_version": "v12_stock_web_residual",
  "selected_round": "R1",
  "selected_loop": 206,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4",
  "new_independent_case_count": 6,
  "new_independent_trigger_count": 6,
  "unique_symbol_count": 4,
  "stage2_count": 1,
  "stage2_actionable_count": 2,
  "stage4b_count": 3,
  "stage4c_count": 0,
  "positive_or_reopen_case_count": 3,
  "counterexample_or_guardrail_case_count": 3,
  "calibration_usable_trigger_count": 6,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "corporate_action_contaminated_180D_count": 0,
  "insufficient_forward_window_180D_count": 0,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "ready_for_batch_ingest": true
}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session.

```text
You are the coding agent for Songdaiki/stock_agent. Read this MD only as one v12 residual research artifact. Do not treat it as a production scoring change by itself.

Task:
1. Ingest the JSONL trigger rows only if the standard v12 parser validates the filename, selected_round, selected_loop, large_sector_id, canonical_archetype_id, trigger_type, entry_date, entry_price, 30/90/180D MFE/MAE, and price_source_validation fields.
2. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
3. Keep production_scoring_changed=false for this artifact.
4. Treat the proposed rule C05_WORKING_CAPITAL_CASHFLOW_REOPEN_AND_HARD4C_GATE_V4 as a shadow candidate only.
5. Promote only if multiple future C05 artifacts support the same narrow condition: hard 4C should require trust/liquidity/backlog break, while cost-rate loss with debt/order/cost offset should remain 4B/watch or Stage2 reopen.
```

## 10. Batch Ingest Self-Audit

```text
standard_v12_filename = pass
filename_round_matches_metadata = pass
filename_loop_matches_metadata = pass
round_sector_pair = pass
canonical_archetype_id_valid = pass
trigger_type_canonical_stage_label = pass
actual_stock_web_1D_ohlcv_used = pass
entry_price_present_for_all_usable_triggers = pass
entry_ohlcv_present_for_all_usable_triggers = pass
complete_30_90_180_mfe_mae_present = pass
corporate_action_180D_screen = pass
insufficient_forward_window_screen = pass
source_proxy_only_count = 0
evidence_url_pending_count = 0
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 11. Source URLs checked

```text
MAIN_EXECUTION_PROMPT:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO_REPEAT_INDEX:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

STOCK_WEB_MANIFEST:
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json

STOCK_WEB_PROFILES:
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/005/005960.json
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/002/002990.json
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/013/013580.json
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/016/016250.json

EVIDENCE_URLS:
https://biz.chosun.com/en/en-realestate/2025/02/04/J2HOCTXA25E35DAUZ3ANDFS5QU/
https://www.mk.co.kr/en/realestate/11317872
https://en.topdaily.kr/articles/8280
https://pulse.mk.co.kr/news/english/10997339
https://www.koreawho.com/news_view.jsp?idxno=7532
https://pulse.mk.co.kr/news/english/11103763
```

## 12. Next Research State

```text
completed_round = R1
completed_loop = 206
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement / C05 margin-working-capital failure + 4C timing repair
next_recommended_archetypes = [
  C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR,
  C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR,
  C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR,
  C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR,
  R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
]
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
