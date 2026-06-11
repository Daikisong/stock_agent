# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 98
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: AI_SERVER_HBM_PCB_CUSTOMER_CAPACITY_ORDER_CYCLE_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent C06 rows and moves C06 from static 21 rows to local projected 24 after loop77, 27 after loop97, and 30 after this loop. The minimum 30-row stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C06:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C06 -> C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

C06 is the HBM/customer-capacity archetype. The important bridge is:

```text
AI/HBM demand -> customer capacity allocation -> ASP/mix -> margin/revision -> FCF
```

A label alone is smoke. The order, customer, mix, and cash conversion are the engine.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C06 rows | 21 |
| static C06 symbols | 16 |
| static C06 good/bad Stage2 | 6 / 4 |
| static C06 4B/4C | 2 / 2 |
| static C06 URL pending/proxy | 18 / 12 |
| static top covered symbols | 005290, 036540, 080220, 222800, 353200, 000660 |
| local C06 loop77 projected rows | 24 |
| local C06 loop97 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid the static C06 top-covered symbols, local loop77 symbols `000660`, `005930`, `000990`, and local loop97 symbols `042700`, `089030`, `095340`.

| symbol | company | status |
|---|---|---|
| 007660 | 이수페타시스 | new C06 symbol versus static top-covered and local C06 loops |
| 064760 | 티씨케이 | new C06 symbol; reduced weight due to C06/C10 boundary |
| 356860 | 티엘비 | new C06 symbol; HBM-PCB capacity premium false-positive |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C06 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 007660 / 2024-03-05 | true | true | clean_180D_window | true |
| 064760 / 2024-03-22 | true | true | clean_180D_window | true |
| 356860 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 이수페타시스 has a corporate-action candidate in 2021 only; selected 2024 window is clean.
- 티씨케이 has zero corporate-action candidates.
- 티엘비 has corporate-action candidates in 2022 only; selected 2024 window is clean.
- 삼성전자, 한미반도체, 테크윙, ISC were not reused because they already appeared in local C06 loops.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| AI_SERVER_HBM_PCB_CUSTOMER_CAPACITY_ORDER_CYCLE_4B_WATCH | C06 | AI/HBM customer capacity and PCB order route can support Stage2A, but needs 4B audit |
| MEMORY_CUSTOMER_CAPACITY_PROCESS_PARTS_MARGIN_4B_WATCH | C06 | memory process-parts customer capacity route is C06/C10 boundary; reduced weight |
| HBM_PCB_CUSTOMER_CAPACITY_PREMIUM_WITHOUT_ORDER_MARGIN_BRIDGE | C06 | HBM-adjacent premium without order/margin bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C06_ISUPETASYS_007660_2024_03_05_AI_SERVER_HBM_PCB_CUSTOMER_CAPA_RERATING | 007660 | 이수페타시스 | 4B_overlay_success | positive | AI/HBM customer capacity route produced 50%+ MFE and then cycle drawdown |
| C06_TCK_064760_2024_03_22_MEMORY_CUSTOMER_CAPACITY_PARTS_RERATING | 064760 | 티씨케이 | 4B_overlay_success | positive | memory customer capacity/process-parts route worked but later drew down |
| C06_TLB_356860_2024_03_06_HBM_PCB_CAPACITY_PREMIUM_FALSE_POSITIVE | 356860 | 티엘비 | failed_rerating | counterexample | HBM-PCB premium lacked order/ASP/margin/FCF bridge and had severe 180D MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 3 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 007660 | source_proxy_only | AI/HBM PCB customer-capacity and order-cycle route | required before promotion |
| 064760 | source_proxy_only | memory customer-capacity/process-parts utilization route | required before promotion |
| 356860 | source_proxy_only | HBM-PCB capacity premium but order/margin bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 007660 | atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv | atlas/symbol_profiles/007/007660.json |
| 064760 | atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv | atlas/symbol_profiles/064/064760.json |
| 356860 | atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv | atlas/symbol_profiles/356/356860.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| ISUPETASYS_007660_2024_03_05_STAGE2A_AI_SERVER_HBM_PCB_CUSTOMER_CAPA | Stage2-Actionable | 2024-03-05 | 2024-03-05 | 38500 | AI/HBM PCB customer capacity and order cycle |
| TCK_064760_2024_03_22_STAGE2A_MEMORY_CUSTOMER_CAPACITY_PARTS | Stage2-Actionable | 2024-03-22 | 2024-03-22 | 110700 | memory customer capacity and process-parts utilization |
| TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PCB_CAPA_PREMIUM | Stage2 | 2024-03-06 | 2024-03-06 | 28200 | HBM-PCB capacity premium without order/margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 007660 | 2024-03-05 | 38500 | 16.88 | -15.71 | 54.55 | -15.71 | 54.55 | -19.74 | 2024-06-28 | 59500 | -48.07 |
| 064760 | 2024-03-22 | 110700 | 25.66 | -5.15 | 35.41 | -5.15 | 35.41 | -37.31 | 2024-06-14 | 149900 | -53.70 |
| 356860 | 2024-03-06 | 28200 | 12.59 | -11.35 | 12.59 | -23.40 | 12.59 | -60.04 | 2024-04-05 | 31750 | -64.50 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 007660 | Stage2A possible; 4B after customer-capacity rerating | useful MFE and later cycle drawdown | current_profile_4B_too_late |
| 064760 | Stage2A possible but C06/C10 boundary | useful MFE and later deep drawdown | current_profile_4B_too_late |
| 356860 | Stage2 risk if HBM-PCB premium is over-credited | low MFE and severe MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C06 interpretation:

- Stage2A can work when customer capacity, HBM/AI-server route, or memory capacity bottleneck evidence appears before the full price rerating.
- Yellow/Green require customer conversion, ASP/mix realization, margin bridge, revision, and FCF.
- HBM-adjacent PCB premium without order/margin bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 007660 | 1.00 | 1.00 | valuation rerating / cycle peak | 4B audit required after HBM/AI PCB rerating |
| 064760 | 1.00 | 1.00 | memory process-parts cycle | 4B audit required after memory capacity rerating |
| 356860 | 1.00 | 1.00 | event premium / weak follow-through | not Stage3 without order/margin bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 007660 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 064760 | thesis_break_watch_only | not hard 4C, but memory-cycle drawdown requires C06/C10 audit |
| 356860 | hard_4c_late | order/ASP/margin/FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 AI/semiconductor names, HBM or AI-server capacity evidence can support Stage2A only when customer conversion, capacity allocation, ASP/mix, margin bridge, revision, or FCF are visible. HBM-adjacent PCB/process labels without order/margin bridge should be capped at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C06_HBM_MEMORY_CUSTOMER_CAPACITY
confidence = medium
```

Candidate C06 rule:

```text
C06_hbm_customer_capacity_bridge_required =
  hbm_or_ai_server_customer_capacity_route
  AND (customer_conversion OR capacity_slot_lock OR asp_mix_bridge OR margin_bridge OR confirmed_revision OR fcf_conversion)

if hbm_adjacent_premium and order_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C06_peak_proximity_4B_audit = true

if MFE_90D < 20 and MAE_90D < -20:
    classify_as C06_hbm_bridge_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 34.18 | -14.75 | 34.18 | -39.03 | 1 | useful but C06 bridge still loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 34.18 | -14.75 | 34.18 | -39.03 | 1 | over-credits HBM-adjacent premiums |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 44.98 | -10.43 | 44.98 | -28.52 | 0 | better after customer-capacity bridge gate |
| P2 canonical_archetype_candidate_profile | C06 | 2 promoted + 1 guard | 44.98 | -10.43 | 44.98 | -28.52 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C06 guard | 2 promoted + 1 guard | 44.98 | -10.43 | 44.98 | -28.52 | 0 | adds HBM-adjacent bridge false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 007660 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 064760 | Stage2A aligned but boundary; 4B audit late | current_profile_4B_too_late |
| 356860 | Stage2 false positive if order/margin bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed C06 fine ids | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 24 -> local 27 -> projected 30; reaches minimum stability threshold |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C06_hbm_customer_capacity_bridge_required|C06_peak_proximity_4B_audit|C06_hbm_bridge_false_positive_guardrail
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses clean 180D windows.
- Uses C06 Priority 0 coverage gap.
- Avoids static C06 top-covered symbols and local loop77/97 symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_hbm_customer_capacity_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"356860 shows HBM-adjacent PCB capacity premium can fail without order/margin bridge while 007660/064760 work only as Stage2A with 4B audit","blocks 356860 false positive while preserving 007660/064760 Stage2A","ISUPETASYS_007660_2024_03_05_STAGE2A_AI_SERVER_HBM_PCB_CUSTOMER_CAPA|TCK_064760_2024_03_22_STAGE2A_MEMORY_CUSTOMER_CAPACITY_PARTS|TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PCB_CAPA_PREMIUM",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C06_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"007660/064760 HBM or memory customer-capacity reratings needed 4B audit after MFE and drawdown","adds 4B audit after large C06 MFE without converting price-only peaks into Green","ISUPETASYS_007660_2024_03_05_STAGE2A_AI_SERVER_HBM_PCB_CUSTOMER_CAPA|TCK_064760_2024_03_22_STAGE2A_MEMORY_CUSTOMER_CAPACITY_PARTS",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C06_hbm_bridge_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"356860 had low MFE and severe 180D MAE after HBM-PCB customer-capacity premium","requires order/ASP/margin/FCF bridge before C06 Stage2/Yellow promotion","TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PCB_CAPA_PREMIUM",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C06_ISUPETASYS_007660_2024_03_05_AI_SERVER_HBM_PCB_CUSTOMER_CAPA_RERATING","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SERVER_HBM_PCB_CUSTOMER_CAPACITY_ORDER_CYCLE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"ISUPETASYS_007660_2024_03_05_STAGE2A_AI_SERVER_HBM_PCB_CUSTOMER_CAPA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"AI-server/HBM PCB customer-capacity route captured 50%+ MFE, but later cycle drawdown required a C06 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C06 symbol versus static top-covered and local C06 loop77/97 symbols; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C06_TCK_064760_2024_03_22_MEMORY_CUSTOMER_CAPACITY_PARTS_RERATING","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_CUSTOMER_CAPACITY_PROCESS_PARTS_MARGIN_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TCK_064760_2024_03_22_STAGE2A_MEMORY_CUSTOMER_CAPACITY_PARTS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"memory customer capacity / process-parts route captured 35% MFE, but later memory-cycle drawdown required C06/C10 boundary 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"borderline C06/C10 case; counted with reduced weight because it is a memory-customer-capacity bridge rather than pure HBM device capacity"}
{"row_type":"case","case_id":"C06_TLB_356860_2024_03_06_HBM_PCB_CAPACITY_PREMIUM_FALSE_POSITIVE","symbol":"356860","company_name":"티엘비","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PCB_CUSTOMER_CAPACITY_PREMIUM_WITHOUT_ORDER_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PCB_CAPA_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"HBM/PCB customer-capacity premium had only low-teens MFE and then severe MAE without order, ASP, margin, or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C06 symbol; clean 2024 corporate-action window; useful as HBM-adjacent capacity false-positive guardrail"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"ISUPETASYS_007660_2024_03_05_STAGE2A_AI_SERVER_HBM_PCB_CUSTOMER_CAPA","case_id":"C06_ISUPETASYS_007660_2024_03_05_AI_SERVER_HBM_PCB_CUSTOMER_CAPA_RERATING","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SERVER_HBM_PCB_CUSTOMER_CAPACITY_ORDER_CYCLE_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":38500.0,"evidence_available_at_that_date":"source_proxy_only: AI server/HBM PCB customer capacity route, order cycle, ASP/mix expectation, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["ai_server_pcb_route","hbm_customer_capacity_route","order_cycle","relative_strength"],"stage3_evidence_fields":["customer_conversion_partial","asp_mix_bridge_pending","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv","profile_path":"atlas/symbol_profiles/007/007660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.88,"MFE_90D_pct":54.55,"MFE_180D_pct":54.55,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.71,"MAE_90D_pct":-15.71,"MAE_180D_pct":-19.74,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":59500.0,"drawdown_after_peak_pct":-48.07,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"stage2a_customer_capacity_route_worked_but_C06_4B_audit_required_after_cycle_peak","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_007660_2024_03_05_38500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TCK_064760_2024_03_22_STAGE2A_MEMORY_CUSTOMER_CAPACITY_PARTS","case_id":"C06_TCK_064760_2024_03_22_MEMORY_CUSTOMER_CAPACITY_PARTS_RERATING","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_CUSTOMER_CAPACITY_PROCESS_PARTS_MARGIN_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":110700.0,"evidence_available_at_that_date":"source_proxy_only: memory customer capacity recovery, process-parts utilization route, HBM/advanced memory process exposure, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_customer_capacity_route","process_parts_utilization_route","hbm_advanced_memory_exposure","relative_strength"],"stage3_evidence_fields":["customer_capacity_bridge_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv","profile_path":"atlas/symbol_profiles/064/064760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.66,"MFE_90D_pct":35.41,"MFE_180D_pct":35.41,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.15,"MAE_90D_pct":-5.15,"MAE_180D_pct":-37.31,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":149900.0,"drawdown_after_peak_pct":-53.7,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_customer_capacity_rerating_worked_but_later_cycle_drawdown_requires_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_4b_cycle_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_064760_2024_03_22_110700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"borderline C06/C10 bridge case; counted with reduced weight","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PCB_CAPA_PREMIUM","case_id":"C06_TLB_356860_2024_03_06_HBM_PCB_CAPACITY_PREMIUM_FALSE_POSITIVE","symbol":"356860","company_name":"티엘비","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PCB_CUSTOMER_CAPACITY_PREMIUM_WITHOUT_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":28200.0,"evidence_available_at_that_date":"source_proxy_only: HBM PCB/customer-capacity premium and event spike visible, but order conversion, ASP/mix, margin, and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_pcb_premium","customer_capacity_expectation","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["order_conversion_absent","asp_mix_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv","profile_path":"atlas/symbol_profiles/356/356860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.59,"MFE_90D_pct":12.59,"MFE_180D_pct":12.59,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.35,"MAE_90D_pct":-23.4,"MAE_180D_pct":-60.04,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":31750.0,"drawdown_after_peak_pct":-64.5,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_pcb_capacity_premium_not_C06_stage3_without_order_margin_bridge","four_b_evidence_type":["event_spike","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_customer_capacity_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_356860_2024_03_06_28200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_ISUPETASYS_007660_2024_03_05_AI_SERVER_HBM_PCB_CUSTOMER_CAPA_RERATING","trigger_id":"ISUPETASYS_007660_2024_03_05_STAGE2A_AI_SERVER_HBM_PCB_CUSTOMER_CAPA","symbol":"007660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Actionable with C06 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"AI/HBM PCB customer capacity route worked, but Green requires ASP/mix, margin, revision, and FCF conversion.","MFE_90D_pct":54.55,"MAE_90D_pct":-15.71,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_TCK_064760_2024_03_22_MEMORY_CUSTOMER_CAPACITY_PARTS_RERATING","trigger_id":"TCK_064760_2024_03_22_STAGE2A_MEMORY_CUSTOMER_CAPACITY_PARTS","symbol":"064760","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable / C06-C10 boundary","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-watch with C06/C10 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory customer-capacity parts rerating worked, but C06 promotion should remain capped without customer/FCF conversion proof.","MFE_90D_pct":35.41,"MAE_90D_pct":-5.15,"score_return_alignment_label":"positive_but_boundary_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_TLB_356860_2024_03_06_HBM_PCB_CAPACITY_PREMIUM_FALSE_POSITIVE","trigger_id":"TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PCB_CAPA_PREMIUM","symbol":"356860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C06 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM PCB/customer capacity premium without order, ASP, margin, or FCF bridge should not receive C06 promotion.","MFE_90D_pct":12.59,"MAE_90D_pct":-23.4,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 98
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

If this loop is accepted together with local loop77 and loop97, C06 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C06 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/007/007660.json
  - atlas/symbol_profiles/064/064760.json
  - atlas/symbol_profiles/356/356860.json
- Considered but not reused:
  - atlas/symbol_profiles/005/005930.json
  - atlas/symbol_profiles/042/042700.json
  - atlas/symbol_profiles/089/089030.json
  - atlas/symbol_profiles/095/095340.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
