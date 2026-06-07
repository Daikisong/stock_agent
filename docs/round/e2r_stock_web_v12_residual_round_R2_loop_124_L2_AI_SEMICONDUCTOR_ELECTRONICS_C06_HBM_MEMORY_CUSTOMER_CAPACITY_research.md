# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_124_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 124
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: FCBGA_HBM_PACKAGE_CAPACITY_CUSTOMER_MIX_RERATING_4B_WATCH
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

This is the corrected valid run after a duplicate loop123 materialization path was discarded. Loop123 already used `222800`, `356860`, and `007810`; this loop uses new C06 symbol/trigger/date combinations only.

This loop adds 3 new independent C06 rows and moves C06 from static 21 rows to local projected 27 after loops 122/123, then to projected 30 after this loop. The 30-row stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

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

C06 is the HBM memory customer/capacity archetype. Capacity is only real when it is wired to customer lock, HBM mix, ASP/margin, revision and FCF. Without those wires, it behaves like a bright panel with no current behind it.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C06 static rows | 21 |
| C06 need to 30 | 9 |
| C06 need to 50 | 29 |
| C06 investigation point | 고객 CAPA, HBM mix, ASP/FCF 전환, cycle 반례 |
| local C06 loop122 projected rows | 24 |
| local C06 loop123 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid local C06 loop122 symbols `000660`, `005930`, `353200` and loop123 symbols `222800`, `356860`, `007810`.

| symbol | company | status |
|---|---|---|
| 009150 | 삼성전기 | new local C06 symbol; FC-BGA/package capacity positive/4B |
| 008060 | 대덕 | new local C06 symbol; package-substrate holdco dead-money counterexample |
| 036710 | 심텍홀딩스 | new local C06 symbol; package-substrate holdco event counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 009150 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |
| 008060 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.80 |
| 036710 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |

Corporate-action notes:

- 삼성전기 has old corporate-action candidates before the selected 2024 window.
- 대덕 has old corporate-action/name split candidates before the selected 2024 window.
- 심텍홀딩스 has old corporate-action/name split candidates before the selected 2024 window.
- Holding-company rows are useful for false-positive guard calibration but should not overcount direct customer-capacity evidence.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| FCBGA_HBM_PACKAGE_CAPACITY_CUSTOMER_MIX_RERATING_4B_WATCH | C06 | FC-BGA/HBM package capacity can support Stage2A, but package-cycle 4B audit is mandatory |
| PACKAGE_SUBSTRATE_HOLDCO_CAPACITY_PREMIUM_WITHOUT_DIRECT_CUSTOMER_FCF_BRIDGE | C06 | holdco capacity premium without direct customer/FCF bridge is dead-money false-positive risk |
| PACKAGE_SUBSTRATE_HOLDCO_EVENT_WITHOUT_CUSTOMER_LOCK_MARGIN_FCF_BRIDGE | C06 | holdco event premium needs customer lock, margin and FCF bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C06_SAMSUNGELECMECH_009150_2024_03_06_FCBGA_HBM_PACKAGE_CAPACITY_RERATING_4B | 009150 | 삼성전기 | 4B_overlay_success | positive | FC-BGA/HBM package-capacity route produced 32.31% MFE and then 4B drawdown |
| C06_DAEDUCK_008060_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_CAPACITY_DEAD_MONEY_FAIL | 008060 | 대덕 | failed_rerating | counterexample | package-substrate holdco premium produced near-zero MFE |
| C06_SIMMTECHHOLDINGS_036710_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_EVENT_PREMIUM_FAIL | 036710 | 심텍홀딩스 | failed_rerating | counterexample | holdco event premium spiked, then collapsed without customer/FCF bridge |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 3 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 009150 | source_proxy_only | FC-BGA/HBM package capacity, customer mix, ASP/margin route | required before promotion |
| 008060 | source_proxy_only | holdco package-substrate capacity narrative but direct customer/FCF bridge absent | required; useful as counterexample |
| 036710 | source_proxy_only | holdco package-substrate event premium but customer lock/margin/FCF bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 009150 | atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv | atlas/symbol_profiles/009/009150.json |
| 008060 | atlas/ohlcv_tradable_by_symbol_year/008/008060/2024.csv | atlas/symbol_profiles/008/008060.json |
| 036710 | atlas/ohlcv_tradable_by_symbol_year/036/036710/2024.csv | atlas/symbol_profiles/036/036710.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SAMSUNGELECMECH_009150_2024_03_06_STAGE2A_FCBGA_HBM_PACKAGE_CAPACITY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 133400 | FC-BGA/HBM package capacity customer-mix route |
| DAEDUCK_008060_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO | Stage2 | 2024-03-06 | 2024-03-06 | 6590 | package-substrate holdco premium without direct bridge |
| SIMMTECHHOLDINGS_036710_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO_EVENT | Stage2 | 2024-03-06 | 2024-03-06 | 2700 | package-substrate holdco event without customer/FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 009150 | 2024-03-06 | 133400 | 20.84 | -1.27 | 32.31 | -1.27 | 32.31 | -20.91 | 2024-07-17 | 176500 | -40.23 |
| 008060 | 2024-03-06 | 6590 | 2.73 | -5.61 | 2.73 | -5.92 | 2.88 | -7.28 | 2024-11-28 | 6780 | -9.88 |
| 036710 | 2024-03-06 | 2700 | 25.93 | -6.48 | 25.93 | -10.74 | 25.93 | -58.67 | 2024-04-02 | 3400 | -67.18 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 009150 | Stage2A possible; 4B after package-capacity rerating | useful MFE and later drawdown | current_profile_4B_too_late |
| 008060 | Stage2 risk if holdco capacity premium is over-credited | near-zero MFE / dead money | current_profile_false_positive |
| 036710 | Stage2 risk if holdco event premium is over-credited | short spike and severe 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C06 interpretation:

- Stage2A can work when FC-BGA/HBM/package capacity is tied to customer mix, ASP/margin, revision and FCF.
- Yellow/Green require non-price customer and mix evidence.
- Holding-company capacity/event premium without direct operating bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 009150 | 0.76 | 1.00 | FC-BGA/HBM package-capacity rerating | full-window 4B audit required |
| 008060 | 0.97 | 1.00 | holdco premium / dead money | not Stage3 without direct customer/FCF bridge |
| 036710 | 0.79 | 1.00 | holdco event premium / bridge absent | not Stage3 without customer lock/FCF bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 009150 | thesis_break_watch_only | not hard 4C, but package/memory cycle 4B cap needed |
| 008060 | hard_4c_dead_money | direct customer capacity and FCF bridge absence should have capped Stage2 earlier |
| 036710 | hard_4c_late | customer lock/margin/FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, HBM/package capacity should promote Stage2A only when direct customer lock, HBM mix, utilization, ASP/margin, revision or FCF conversion is visible. Holding-company capacity/event premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C06_HBM_MEMORY_CUSTOMER_CAPACITY
confidence = medium
```

Candidate C06 rule:

```text
C06_hbm_customer_capacity_mix_bridge_required =
  hbm_memory_or_hbm_package_capacity_route
  AND (customer_qualification OR customer_lock OR capacity_lock OR hbm_mix_bridge OR asp_margin_bridge OR confirmed_revision OR fcf_conversion)

if holdco_capacity_premium and direct_customer_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -35:
    add C06_memory_package_cycle_4B_audit = true

if MFE_90D < 5 and bridge_absent:
    classify_as C06_holdco_dead_money_false_positive_guardrail

if MFE_90D > 20 and MAE_180D < -40 and bridge_absent:
    classify_as C06_holdco_event_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 20.32 | -5.98 | 20.37 | -28.95 | 2 | useful but C06 holdco bridge too loose |
| P0b calibrated rollback | rollback | 3 | 20.32 | -5.98 | 20.37 | -28.95 | 2 | over-credits package/holdco capacity premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 32.31 | -1.27 | 32.31 | -20.91 | 0 | better after customer-capa/FCF gate |
| P2 canonical_archetype_candidate_profile | C06 | 1 promoted + 2 guard | 32.31 | -1.27 | 32.31 | -20.91 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C06 guard | 1 promoted + 2 guard | 32.31 | -1.27 | 32.31 | -20.91 | 0 | adds holdco false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 009150 | Stage2A aligned; 4B cycle audit needed | current_profile_4B_too_late |
| 008060 | Stage2 false positive / dead-money if direct bridge not enforced | current_profile_false_positive |
| 036710 | Stage2 false positive if holdco event bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed C06 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 27 -> projected 30; reaches minimum stability threshold |

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
new_axis_proposed: C06_hbm_customer_capacity_mix_bridge_required|C06_memory_package_cycle_4B_audit|C06_holdco_dead_money_false_positive_guardrail|C06_holdco_event_false_positive_guardrail
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
- Uses C06 Priority 0 coverage gap.
- Avoids local C06 loop122 and loop123 symbols.
- Keeps 009150 with reduced weight because it is a large-cap package-substrate boundary name.
- Keeps 008060/036710 with reduced weights because they are holding-company structures.
- Discards the accidental duplicate loop123 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop123 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_hbm_customer_capacity_mix_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"008060/036710 show package-substrate holdco premiums can fail without direct customer-capa/margin/FCF bridge while 009150 works only as Stage2A with 4B audit","blocks two false positives while preserving 009150 Stage2A","SAMSUNGELECMECH_009150_2024_03_06_STAGE2A_FCBGA_HBM_PACKAGE_CAPACITY|DAEDUCK_008060_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO|SIMMTECHHOLDINGS_036710_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO_EVENT",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C06_memory_package_cycle_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"009150 package-capacity rerating needed full-window 4B audit after MFE and drawdown","adds 4B audit after C06 package/memory-cycle MFE without converting price-only peaks into Green","SAMSUNGELECMECH_009150_2024_03_06_STAGE2A_FCBGA_HBM_PACKAGE_CAPACITY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C06_holdco_dead_money_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"008060 had near-zero MFE after package-substrate holdco premium without direct bridge","requires direct customer capacity, HBM mix, margin/revision and FCF bridge before Stage2/Yellow promotion","DAEDUCK_008060_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO",1,1,1,medium,canonical_shadow_only,"dead-money false-positive guardrail"
shadow_weight,C06_holdco_event_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"036710 had event MFE and severe 180D MAE after package-substrate holdco premium without customer/FCF bridge","requires confirmed customer lock, margin/revision and FCF bridge before Stage2/Yellow promotion","SIMMTECHHOLDINGS_036710_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO_EVENT",1,1,1,medium,canonical_shadow_only,"event false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C06_SAMSUNGELECMECH_009150_2024_03_06_FCBGA_HBM_PACKAGE_CAPACITY_RERATING_4B","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"124","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"FCBGA_HBM_PACKAGE_CAPACITY_CUSTOMER_MIX_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"SAMSUNGELECMECH_009150_2024_03_06_STAGE2A_FCBGA_HBM_PACKAGE_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; large-cap package substrate boundary, independent weight reduced","independent_evidence_weight":0.9,"score_price_alignment":"FC-BGA/HBM package-capacity customer-mix route captured 32% MFE, but post-peak drawdown required C06 4B cycle audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol versus loops 122/123; package/FC-BGA bridge positive/4B watch"}
{"row_type":"case","case_id":"C06_DAEDUCK_008060_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_CAPACITY_DEAD_MONEY_FAIL","symbol":"008060","company_name":"대덕","round":"R2","loop":"124","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PACKAGE_SUBSTRATE_HOLDCO_CAPACITY_PREMIUM_WITHOUT_DIRECT_CUSTOMER_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DAEDUCK_008060_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action/name split candidates before selected 2024 window; holdco boundary case, independent weight reduced","independent_evidence_weight":0.8,"score_price_alignment":"package-substrate holdco capacity premium produced near-zero MFE and weak follow-through without direct customer capacity or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol; holdco structure prevents direct C06 promotion without customer/FCF bridge"}
{"row_type":"case","case_id":"C06_SIMMTECHHOLDINGS_036710_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_EVENT_PREMIUM_FAIL","symbol":"036710","company_name":"심텍홀딩스","round":"R2","loop":"124","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PACKAGE_SUBSTRATE_HOLDCO_EVENT_WITHOUT_CUSTOMER_LOCK_MARGIN_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"SIMMTECHHOLDINGS_036710_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO_EVENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action/name split candidates only before selected 2024 window","independent_evidence_weight":0.9,"score_price_alignment":"package-substrate holdco event premium produced a short spike but then severe MAE without customer lock, margin and FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol; high-beta holdco/event false-positive guard"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SAMSUNGELECMECH_009150_2024_03_06_STAGE2A_FCBGA_HBM_PACKAGE_CAPACITY","case_id":"C06_SAMSUNGELECMECH_009150_2024_03_06_FCBGA_HBM_PACKAGE_CAPACITY_RERATING_4B","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"124","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"FCBGA_HBM_PACKAGE_CAPACITY_CUSTOMER_MIX_RERATING_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":133400.0,"evidence_available_at_that_date":"source_proxy_only: FC-BGA/HBM package capacity, customer mix route, AI server substrate demand and revision expectation visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["fc_bga_hbm_package_capacity","customer_mix_route","ai_server_substrate_demand","relative_strength"],"stage3_evidence_fields":["customer_capacity_bridge_partial","margin_bridge_partial","revision_bridge_partial","fcf_conversion_pending"],"stage4b_evidence_fields":["memory_package_cycle_peak_watch","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv","profile_path":"atlas/symbol_profiles/009/009150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.84,"MFE_90D_pct":32.31,"MFE_180D_pct":32.31,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-1.27,"MAE_90D_pct":-1.27,"MAE_180D_pct":-20.91,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":176500.0,"drawdown_after_peak_pct":-40.23,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.76,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fc_bga_hbm_package_capacity_rerating_worked_but_full_window_cycle_peak_requires_C06_4B_audit","four_b_evidence_type":["valuation_rerating","package_cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["large_cap_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_009150_2024_03_06_133400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; large-cap package substrate boundary","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DAEDUCK_008060_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO","case_id":"C06_DAEDUCK_008060_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_CAPACITY_DEAD_MONEY_FAIL","symbol":"008060","company_name":"대덕","round":"R2","loop":"124","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PACKAGE_SUBSTRATE_HOLDCO_CAPACITY_PREMIUM_WITHOUT_DIRECT_CUSTOMER_FCF_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":6590.0,"evidence_available_at_that_date":"source_proxy_only: package-substrate holding-company capacity premium visible, but direct customer capacity lock, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["package_substrate_holdco_premium","memory_recovery_narrative"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["dead_money_follow_through","direct_bridge_absent"],"stage4c_evidence_fields":["direct_customer_capacity_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008060/2024.csv","profile_path":"atlas/symbol_profiles/008/008060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.73,"MFE_90D_pct":2.73,"MFE_180D_pct":2.88,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.61,"MAE_90D_pct":-5.92,"MAE_180D_pct":-7.28,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-28","peak_price":6780.0,"drawdown_after_peak_pct":-9.88,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"package_substrate_holdco_premium_not_C06_stage3_without_direct_customer_capa_fcf_bridge","four_b_evidence_type":["dead_money_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_dead_money","trigger_outcome_label":"counterexample_low_mfe_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["holdco_structure_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_008060_2024_03_06_6590","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action/name split candidates before selected 2024 window; holdco boundary","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SIMMTECHHOLDINGS_036710_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO_EVENT","case_id":"C06_SIMMTECHHOLDINGS_036710_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_EVENT_PREMIUM_FAIL","symbol":"036710","company_name":"심텍홀딩스","round":"R2","loop":"124","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PACKAGE_SUBSTRATE_HOLDCO_EVENT_WITHOUT_CUSTOMER_LOCK_MARGIN_FCF_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":2700.0,"evidence_available_at_that_date":"source_proxy_only: package-substrate holdco event premium and memory substrate recovery narrative visible, but customer lock, margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["package_substrate_holdco_event","memory_substrate_recovery_narrative","relative_strength_event"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","holdco_bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["customer_lock_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036710/2024.csv","profile_path":"atlas/symbol_profiles/036/036710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.93,"MFE_90D_pct":25.93,"MFE_180D_pct":25.93,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.48,"MAE_90D_pct":-10.74,"MAE_180D_pct":-58.67,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":3400.0,"drawdown_after_peak_pct":-67.18,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"package_substrate_holdco_event_not_C06_stage3_without_customer_lock_margin_fcf_bridge","four_b_evidence_type":["event_spike","bridge_absent","full_window_drawdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_event_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["holdco_structure_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_036710_2024_03_06_2700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action/name split candidates before selected 2024 window","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_SAMSUNGELECMECH_009150_2024_03_06_FCBGA_HBM_PACKAGE_CAPACITY_RERATING_4B","trigger_id":"SAMSUNGELECMECH_009150_2024_03_06_STAGE2A_FCBGA_HBM_PACKAGE_CAPACITY","symbol":"009150","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-watch with C06 4B cycle audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"FC-BGA/HBM package-capacity route worked, but Green needs customer mix, ASP/margin, revision and FCF conversion.","MFE_90D_pct":32.31,"MAE_90D_pct":-1.27,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_DAEDUCK_008060_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_CAPACITY_DEAD_MONEY_FAIL","trigger_id":"DAEDUCK_008060_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO","symbol":"008060","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":56,"stage_label_before":"Stage2 false-positive / holdco capacity risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":43,"stage_label_after":"Stage1/dead-money watch, not C06 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Package-substrate holdco premium without direct customer-capa or FCF bridge produced near-zero upside.","MFE_90D_pct":2.73,"MAE_90D_pct":-5.92,"score_return_alignment_label":"false_positive_dead_money_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_SIMMTECHHOLDINGS_036710_2024_03_06_PACKAGE_SUBSTRATE_HOLDCO_EVENT_PREMIUM_FAIL","trigger_id":"SIMMTECHHOLDINGS_036710_2024_03_06_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_HOLDCO_EVENT","symbol":"036710","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / package substrate holdco event risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage1/4C-watch, not C06 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Package-substrate holdco event premium without customer lock/margin/FCF bridge produced a spike and then severe MAE.","MFE_90D_pct":25.93,"MAE_90D_pct":-10.74,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"124","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

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
completed_loop = 124
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C06_HBM_MEMORY_CUSTOMER_CAPACITY_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with local C06 loops 122 and 123, C06 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C06 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/008/008060/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/036/036710/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/009/009150.json
  - atlas/symbol_profiles/008/008060.json
  - atlas/symbol_profiles/036/036710.json
- Rejected local duplicate C06 symbols:
  - 000660, 005930, 353200
  - 222800, 356860, 007810
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R2_loop_123_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
