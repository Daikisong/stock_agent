# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round: R2
selected_loop: 205
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5
loop_objective: residual_false_positive_mining | stage2_actionable_bonus_stress_test | sector_specific_rule_discovery | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 6 new independent cases, 3 counterexamples, and 3 residual errors for L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus: +2.0
stage3_yellow_total_min: 75.0
stage3_green_total_min: 87.0
stage3_green_revision_min: 55.0
price_only_blowoff_blocks_positive_stage: true
full_4b_requires_non_price_evidence: true
hard_4c_thesis_break_routes_to_4c: true
```

The purpose is not to loosen Green. The test is whether C10 memory-equipment rows should separate **named supplier order / revenue conversion** from **late beta after customer-capex or product-roadmap headlines**.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| selected_loop | 205 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| fine_archetype_id | C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5 |
| selected sector | AI / semiconductor / electronics |
| round-sector validity | pass |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for selection:

```text
representative rows: 11200
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE: 210 rows / 68 symbols / positives-counter 27-32 / 4B-4C 27-0
top symbols already dense: 240810, 084370, 095610, 036930, 319660, 166090
priority direction: 회복 cycle 초입 false positive와 order conversion 확인
```

Duplicate gate:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
selected symbols: 232140, 253590, 092870
new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_independent_case_ratio: 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest/schema fields checked:

```text
source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
manifest_max_date: 2026-02-20
tradable columns: d,o,h,l,c,v,a,mc,s,m
MFE_N_pct: max high from entry date through N tradable rows / entry_price - 1
MAE_N_pct: min low from entry date through N tradable rows / entry_price - 1
```

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in tradable shard | pass |
| 180 trading-day forward window exists | pass for 6/6 trigger rows |
| required 30/90/180 MFE/MAE present | pass |
| corporate-action 180D contamination | none detected in selected rows |
| row_type=trigger only for usable rows | pass |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5
compressed evidence families:
  1. named customer order / supply contract: YC Corp -> Samsung Electronics
  2. realized tester revenue / OP conversion: Neosem -> SSD/CXL/module tester profit bridge
  3. product-pipeline or future tester optionality without realized order: Exicon -> CXL/SSD tester pipeline
  4. high-MAE true direct-order rows: preserve Stage2-Actionable, block Yellow/Green
  5. late-beta contract-spike rows: cap at Stage2/Actionable, do not promote Green
```

## 7. Case Selection Summary

| case_id | symbol | company | trigger | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | role | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| C10-L205-001 | 232140 | YC Corp | Stage2-Actionable | 2024-07-29 | 18260 | 5.37 / -40.69 | 5.37 / -54.71 | 5.37 / -54.71 | counterexample | current_profile_false_positive |
| C10-L205-002 | 232140 | YC Corp | Stage2-Actionable | 2025-03-26 | 12350 | 4.45 / -25.34 | 4.45 / -25.34 | 28.74 / -25.34 | positive | current_profile_correct |
| C10-L205-003 | 253590 | Neosem | Stage2-Actionable | 2024-11-15 | 9650 | 9.22 / -15.13 | 38.55 / -15.13 | 38.55 / -15.96 | positive | current_profile_correct |
| C10-L205-004 | 253590 | Neosem | Stage2-Actionable | 2025-02-07 | 10100 | 32.38 / -6.83 | 32.38 / -18.22 | 32.38 / -24.65 | positive | current_profile_correct |
| C10-L205-005 | 092870 | Exicon | Stage2 | 2024-06-25 | 17500 | 43.71 / -35.71 | 43.71 / -42.86 | 43.71 / -51.94 | counterexample | current_profile_too_early |
| C10-L205-006 | 092870 | Exicon | Stage2 | 2024-10-24 | 11650 | 17.08 / -21.46 | 35.28 / -27.81 | 35.28 / -27.81 | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count: 3
counterexample_count: 3
4B_case_count: 0
4C_case_count: 0
current_profile_error_count: 3
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
```

Positive controls are Neosem and YC follow-on rows where direct supplier revenue/order bridge exists. Counterexamples are YC's 2024 post-spike order row and Exicon pipeline rows where forward MAE shows the danger of converting product optionality into Actionable/Yellow too quickly.

## 9. Evidence Source Map

| case_id | symbol | source | url | evidence summary |
|---|---:|---|---|---|
| C10-L205-001 | 232140 | ZDNet Korea / TheBell / Bloter, 2024-07-29 to 2024-08-06 | https://zdnet.co.kr/view/?no=20240729101422 | Samsung Electronics HBM wafer tester / semiconductor inspection equipment contract, KRW101.7bn, after final qualification; single-customer direct order but entry was already post-spike. |
| C10-L205-002 | 232140 | TheElec Korea / Dealsite, 2025-03-26 to 2025-04-04 | https://www.thelec.kr/news/articleView.html?idxno=34431 | Samsung Electronics semiconductor inspection equipment contract KRW51.15bn, HBM wafer tester follow-on route after prior 2024 KRW101.7bn contract. |
| C10-L205-003 | 253590 | TheElec Global, 2024-11-15 | https://www.thelec.net/news/articleView.html?idxno=5039 | Record third-quarter profit backed by Gen5 SSD tester sales and CXL tester performance; module/component tester route links memory recovery to issuer revenue. |
| C10-L205-004 | 253590 | TheElec Global / KDPress, 2025-02-07 to 2025-02-09 | https://www.thelec.net/news/articleView.html?idxno=5139 | FY2024 revenue and OP increased, with module and component tester businesses driving high profitability; memory module testers were nearly 90% of revenue. |
| C10-L205-005 | 092870 | Mirae Asset Securities / MoneyToday proxy, 2024-06-25 | https://securities.miraeasset.com/bbs/download/2129032.pdf?attachmentId=2129032 | CXL / next-generation tester narrative plus domestic tester commercialization and supply-contract language, but issuer-level memory order conversion remained too thin for Actionable. |
| C10-L205-006 | 092870 | Naver/Mirae company report, 2024-10-24 | https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf | Report highlighted Gen6 SSD / CXL tester demand expectation for 2025, but at trigger date this was product pipeline rather than recognized order/revenue bridge. |

## 10. Price Data Source Map

| symbol | entry_date | entry shard | profile path | 180D corporate-action status |
|---:|---|---|---|---|
| 232140 | 2024-07-29 | atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv | atlas/symbol_profiles/232/232140.json | clean_180D_window |
| 232140 | 2025-03-26 | atlas/ohlcv_tradable_by_symbol_year/232/232140/2025.csv | atlas/symbol_profiles/232/232140.json | clean_180D_window |
| 253590 | 2024-11-15 | atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv | atlas/symbol_profiles/253/253590.json | clean_180D_window |
| 253590 | 2025-02-07 | atlas/ohlcv_tradable_by_symbol_year/253/253590/2025.csv | atlas/symbol_profiles/253/253590.json | clean_180D_window |
| 092870 | 2024-06-25 | atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv | atlas/symbol_profiles/092/092870.json | clean_180D_window |
| 092870 | 2024-10-24 | atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv | atlas/symbol_profiles/092/092870.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### C10-L205-001 / 232140 YC Corp / 2024 Samsung HBM tester contract

- Stage2 evidence: direct Samsung order and HBM wafer tester commercialization.
- Stage3 evidence: customer confirmation exists, but margin/revenue conversion was not yet visible at the entry date.
- Residual: this is not a bad event; it is a **bad entry-quality / late-beta** example. Stage2-Actionable may be allowed, but Yellow/Green should be blocked.

### C10-L205-002 / 232140 YC Corp / 2025 follow-on contract

- Stage2 evidence: repeat Samsung contract after the first HBM tester supply route.
- Residual: repeat order improves evidence quality, but high MAE means Green should still wait for recognized revenue/margin.

### C10-L205-003 / 253590 Neosem / Q3 tester-profit bridge

- Stage2 evidence: Gen5 SSD tester/CXL tester demand was tied to actual record Q3 profitability.
- Stage3 evidence: financial visibility and margin bridge were visible.
- Residual: this is a cleaner C10 direct supplier conversion row.

### C10-L205-004 / 253590 Neosem / FY2024 record results

- Stage2 evidence: full-year revenue/OP bridge, module/component tester sales.
- Stage3 evidence: actual financial conversion exists.
- Residual: valid Actionable, but peak-to-trough drawdown after entry warns against Green without repeat conversion.

### C10-L205-005 / 092870 Exicon / CXL tester and supply-contract narrative

- Stage2 evidence: product route and tester commercialization.
- Stage3 evidence: not enough issuer-level recognized order/revenue bridge at the trigger date.
- Residual: pipeline can be Stage2, but not Actionable/Yellow until the order conversion appears.

### C10-L205-006 / 092870 Exicon / SSD/CXL tester pipeline report

- Stage2 evidence: product roadmap and 2025 CXL/SSD tester demand expectation.
- Residual: product roadmap had real optionality but produced a high-MAE path, so the profile should cap it.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | O/H/L/C/V | peak_date | peak_price | drawdown_after_peak | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE |
|---:|---|---|---|---:|---:|---:|---:|---:|
| 232140 | 2024-07-29 | 15700/19240/15500/18260/31510904 | 2024-07-29 | 19240 | -57.02 | 5.37 / -40.69 | 5.37 / -54.71 | 5.37 / -54.71 |
| 232140 | 2025-03-26 | 11990/12900/11980/12350/1676984 | 2025-10-14 | 15900 | -24.03 | 4.45 / -25.34 | 4.45 / -25.34 | 28.74 / -25.34 |
| 253590 | 2024-11-15 | 9420/9920/9420/9650/1112791 | 2025-02-19 | 13370 | -39.34 | 9.22 / -15.13 | 38.55 / -15.13 | 38.55 / -15.96 |
| 253590 | 2025-02-07 | 9550/10410/9410/10100/1997349 | 2025-02-19 | 13370 | -43.08 | 32.38 / -6.83 | 32.38 / -18.22 | 32.38 / -24.65 |
| 092870 | 2024-06-25 | 17010/17850/16950/17500/190010 | 2024-07-08 | 25150 | -66.56 | 43.71 / -35.71 | 43.71 / -42.86 | 43.71 / -51.94 |
| 092870 | 2024-10-24 | 11430/13380/11360/11650/1914572 | 2025-02-14 | 15760 | -37.88 | 17.08 / -21.46 | 35.28 / -27.81 | 35.28 / -27.81 |

## 13. Current Calibrated Profile Stress Test

| case_id | before score/stage | after shadow score/stage | 180D MFE/MAE | verdict |
|---|---|---|---:|---|
| C10-L205-001 | 28.8 / Stage2 | 22.6 / Stage4B | 5.37 / -54.71 | current_profile_false_positive |
| C10-L205-002 | 39.2 / Stage2 | 47.2 / Stage2 | 28.74 / -25.34 | current_profile_correct |
| C10-L205-003 | 40.8 / Stage2 | 42.8 / Stage2 | 38.55 / -15.96 | current_profile_correct |
| C10-L205-004 | 39.8 / Stage2 | 41.8 / Stage2 | 32.38 / -24.65 | current_profile_correct |
| C10-L205-005 | 0.8 / Stage2 | 0 / Stage4B | 43.71 / -51.94 | current_profile_too_early |
| C10-L205-006 | 0.8 / Stage2 | 0 / Stage4B | 35.28 / -27.81 | current_profile_false_positive |

Stress-test answers:

```text
1. Current profile would reward YC/Neosem direct supplier contracts but risks over-crediting Exicon product pipeline rows.
2. Actual MFE/MAE says direct order rows can still have deep MAE; the profile should block Green before it deletes Stage2.
3. Stage2 bonus is useful for repeat supplier order rows, but too generous for product-roadmap-only rows.
4. Yellow threshold 75 is not too high in C10; it should remain hard to cross without recognized revenue/margin.
5. Green threshold 87 and revision 55 are kept.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is kept.
8. Hard 4C routing is not the main issue here; C10 still needs direct 4C order-cancellation rows in a later loop.
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is proposed. `green_lateness_ratio = not_applicable` for all trigger rows.

```text
Stage2 cap: Exicon product-pipeline rows
Stage2-Actionable: named customer order or actual tester revenue/profit conversion
Stage3-Yellow candidate: Neosem-style actual revenue/OP bridge only, but high MAE still blocks Green
Stage3-Green: no row promoted
```

## 15. 4B Local vs Full-window Timing Audit

No full Stage4B trigger row is proposed. However, YC 2024 and Exicon rows behave like **late-beta / post-spike local-overheat warnings**.

```text
four_b_local_peak_proximity: not_applicable_no_full_4B_trigger
four_b_full_window_peak_proximity: not_applicable_no_full_4B_trigger
four_b_evidence_type: positioning_overheat / valuation_blowoff / margin_or_backlog_slowdown where applicable
four_b_timing_verdict: use as Actionable cap, not as full 4B without non-price deterioration
```

## 16. 4C Protection Audit

No Stage4C trigger row is proposed.

```text
four_c_protection_label: not_applicable_no_4C_trigger
hard_4c_note: C10 still needs future direct order-cancel / capex-pushout / customer-loss 4C rows.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope: sector_specific
sector_specific_rule_candidate: L2_MEMORY_EQUIPMENT_SUPPLIER_ORDER_CONVERSION_GATE_V5
rule:
  In L2 memory-equipment recovery, customer-level memory capex, HBM growth, or product roadmap language can create Stage2 watch.
  Stage2-Actionable requires a named customer order, supply contract, shipment, customer qualification, revenue conversion, or margin conversion at issuer level.
  If the entry occurs after a contract-driven spike and 30/90D MAE is already severe, cap the row at Actionable and block Yellow/Green.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_LATE_BETA_GREEN_BLOCKER_GATE_V5
rule:
  Direct supplier bridge preserves Stage2/Actionable.
  Product-pipeline or future tester optionality without order/revenue conversion remains Stage2.
  High-MAE direct-order winners block Yellow/Green first; they do not erase Stage2.
  Repeat order + realized margin/revenue bridge is required before Stage3-Yellow.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false-positive rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | direct order and product pipeline both get partial credit | 6 | 26.62 | -30.68 | 30.67 | -33.4 | 0.50 | over-credits product-pipeline rows |
| P0b e2r_2_0_baseline_reference | rollback | slower Stage2; less explicit bridge bonus | 6 | 26.62 | -30.68 | 30.67 | -33.4 | 0.33 | misses direct order speed |
| P1 sector_specific_candidate_profile | L2 | supplier-level order/revenue bridge required | 6 | 26.62 | -30.68 | 30.67 | -33.4 | 0.17 | best alignment |
| P2 canonical_archetype_candidate_profile | C10 | C10 late-beta high-MAE Green blocker | 6 | 26.62 | -30.68 | 30.67 | -33.4 | 0.17 | best alignment |
| P3 counterexample_guard_profile | C10 guard | product-roadmap-only rows capped at Stage2 | 6 | 26.62 | -30.68 | 30.67 | -33.4 | 0.00 | too conservative for direct follow-on orders |

## 20. Score-Return Alignment Matrix

```text
best aligned:
  - Neosem actual tester profit bridge -> Stage2-Actionable / possible Yellow watch
  - YC 2025 repeat Samsung order -> Stage2-Actionable but Green blocked
misaligned without new guard:
  - YC 2024 post-spike contract row -> Actionable too easy, Green must be blocked
  - Exicon CXL/SSD product pipeline rows -> Stage2 only until order/revenue conversion
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5 | 3 | 3 | 0 | 0 | 6 | 0 | 6 | 6 | 3 | L2_MEMORY_EQUIPMENT_SUPPLIER_ORDER_CONVERSION_GATE_V5 | C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_LATE_BETA_GREEN_BLOCKER_GATE_V5 | direct 4C order-cancel / capex-pushout rows still missing |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, full_4b_requires_non_price_evidence
residual_error_types_found: late_beta_after_contract_spike, product_pipeline_without_supplier_order_conversion, high_MAE_true_direct_order_green_blocker
new_axis_proposed: no_global_axis
existing_axis_strengthened: stage2_required_bridge; stage3_green_not_loosened
existing_axis_weakened: none
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_MEMORY_EQUIPMENT_SUPPLIER_ORDER_CONVERSION_GATE_V5
canonical_archetype_rule_candidate: C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_LATE_BETA_GREEN_BLOCKER_GATE_V5
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web tradable_raw OHLC row exists for every entry_date.
- 30/90/180D MFE/MAE exists for every trigger row.
- Trigger type uses canonical stage label.
- Each trigger row has same_entry_group_id, dedupe_for_aggregate, aggregate_group_role.
- No production scoring change is made.
```

Not validated in this MD:

```text
- live candidate status
- brokerage/API execution
- production stock_agent code behavior
- post-2026-02-20 price path
- exact future revenue recognition beyond public evidence available at trigger date
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,supplier_order_conversion_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"C10 product-pipeline rows had deep MAE without direct order/revenue bridge","caps Exicon-style product optionality at Stage2","TRG-L205-001|TRG-L205-002|TRG-L205-003|TRG-L205-004|TRG-L205-005|TRG-L205-006",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,late_beta_high_MAE_green_blocker,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"direct order rows can still suffer deep MAE after spike; Green must wait for realized margin/revenue","preserves Stage2/Actionable but blocks Yellow/Green","TRG-L205-001|TRG-L205-002|TRG-L205-003|TRG-L205-004|TRG-L205-005|TRG-L205-006",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10-L205-001","symbol":"232140","company_name":"YC Corp","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hbm_wafer_tester_contract_late_beta_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Samsung Electronics HBM wafer tester / semiconductor inspection equipment contract, KRW101.7bn, after final qualification; single-customer direct order but entry was already post-spike."}
{"row_type":"trigger","trigger_id":"TRG-L205-001","case_id":"C10-L205-001","symbol":"232140","company_name":"YC Corp","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","sector":"AI/Semiconductor/Electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-29","evidence_available_at_that_date":"Samsung Electronics HBM wafer tester / semiconductor inspection equipment contract, KRW101.7bn, after final qualification; single-customer direct order but entry was already post-spike.","evidence_source":"ZDNet Korea / TheBell / Bloter, 2024-07-29 to 2024-08-06","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-29","entry_price":18260.0,"entry_ohlcv":{"o":15700.0,"h":19240.0,"l":15500.0,"c":18260.0,"v":31510904},"MFE_30D_pct":5.37,"MFE_90D_pct":5.37,"MFE_180D_pct":5.37,"MFE_1Y_pct":5.37,"MFE_2Y_pct":null,"MAE_30D_pct":-40.69,"MAE_90D_pct":-54.71,"MAE_180D_pct":-54.71,"MAE_1Y_pct":-54.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-29","peak_price":19240.0,"drawdown_after_peak_pct":-57.02,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_full_4B_trigger","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"not_applicable_no_4C_trigger","trigger_outcome_label":"hbm_wafer_tester_contract_late_beta_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:232140:Stage2-Actionable:2024-07-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10-L205-001","trigger_id":"TRG-L205-001","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":28.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":22,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":22.6,"stage_label_after":"Stage4B","changed_components":["supplier_order_conversion_required","late_beta_high_MAE_green_blocker"],"component_delta_explanation":"Direct order/revenue bridge is preserved, but product-pipeline or post-spike entries are capped; high-MAE rows block Yellow/Green rather than deleting Stage2.","MFE_90D_pct":5.37,"MAE_90D_pct":-54.71,"score_return_alignment_label":"hbm_wafer_tester_contract_late_beta_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10-L205-002","symbol":"232140","company_name":"YC Corp","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"repeat_samsung_memory_tester_order_reopen","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Samsung Electronics semiconductor inspection equipment contract KRW51.15bn, HBM wafer tester follow-on route after prior 2024 KRW101.7bn contract."}
{"row_type":"trigger","trigger_id":"TRG-L205-002","case_id":"C10-L205-002","symbol":"232140","company_name":"YC Corp","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","sector":"AI/Semiconductor/Electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-26","evidence_available_at_that_date":"Samsung Electronics semiconductor inspection equipment contract KRW51.15bn, HBM wafer tester follow-on route after prior 2024 KRW101.7bn contract.","evidence_source":"TheElec Korea / Dealsite, 2025-03-26 to 2025-04-04","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","repeat_order_or_conversion"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2025.csv","profile_path":"atlas/symbol_profiles/232/232140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-26","entry_price":12350.0,"entry_ohlcv":{"o":11990.0,"h":12900.0,"l":11980.0,"c":12350.0,"v":1676984},"MFE_30D_pct":4.45,"MFE_90D_pct":4.45,"MFE_180D_pct":28.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.34,"MAE_90D_pct":-25.34,"MAE_180D_pct":-25.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-14","peak_price":15900.0,"drawdown_after_peak_pct":-24.03,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_full_4B_trigger","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable_no_4C_trigger","trigger_outcome_label":"repeat_samsung_memory_tester_order_reopen","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:232140:Stage2-Actionable:2025-03-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10-L205-002","trigger_id":"TRG-L205-002","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":12,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":39.2,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":12,"margin_bridge_score":8,"revision_score":0,"relative_strength_score":5,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":47.2,"stage_label_after":"Stage2","changed_components":["supplier_order_conversion_required","late_beta_high_MAE_green_blocker"],"component_delta_explanation":"Direct order/revenue bridge is preserved, but product-pipeline or post-spike entries are capped; high-MAE rows block Yellow/Green rather than deleting Stage2.","MFE_90D_pct":4.45,"MAE_90D_pct":-25.34,"score_return_alignment_label":"repeat_samsung_memory_tester_order_reopen","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10-L205-003","symbol":"253590","company_name":"Neosem","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"gen5_ssd_cxl_tester_record_q3_bridge","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Record third-quarter profit backed by Gen5 SSD tester sales and CXL tester performance; module/component tester route links memory recovery to issuer revenue."}
{"row_type":"trigger","trigger_id":"TRG-L205-003","case_id":"C10-L205-003","symbol":"253590","company_name":"Neosem","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","sector":"AI/Semiconductor/Electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-15","evidence_available_at_that_date":"Record third-quarter profit backed by Gen5 SSD tester sales and CXL tester performance; module/component tester route links memory recovery to issuer revenue.","evidence_source":"TheElec Global, 2024-11-15","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv","profile_path":"atlas/symbol_profiles/253/253590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-15","entry_price":9650.0,"entry_ohlcv":{"o":9420.0,"h":9920.0,"l":9420.0,"c":9650.0,"v":1112791},"MFE_30D_pct":9.22,"MFE_90D_pct":38.55,"MFE_180D_pct":38.55,"MFE_1Y_pct":38.55,"MFE_2Y_pct":null,"MAE_30D_pct":-15.13,"MAE_90D_pct":-15.13,"MAE_180D_pct":-15.96,"MAE_1Y_pct":-21.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":13370.0,"drawdown_after_peak_pct":-39.34,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_full_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_4C_trigger","trigger_outcome_label":"gen5_ssd_cxl_tester_record_q3_bridge","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:253590:Stage2-Actionable:2024-11-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10-L205-003","trigger_id":"TRG-L205-003","symbol":"253590","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":40.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":17,"revision_score":12,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":42.8,"stage_label_after":"Stage2","changed_components":["supplier_order_conversion_required","late_beta_high_MAE_green_blocker"],"component_delta_explanation":"Direct order/revenue bridge is preserved, but product-pipeline or post-spike entries are capped; high-MAE rows block Yellow/Green rather than deleting Stage2.","MFE_90D_pct":38.55,"MAE_90D_pct":-15.13,"score_return_alignment_label":"gen5_ssd_cxl_tester_record_q3_bridge","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10-L205-004","symbol":"253590","company_name":"Neosem","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"fy2024_record_revenue_op_memory_module_tester_bridge","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FY2024 revenue and OP increased, with module and component tester businesses driving high profitability; memory module testers were nearly 90% of revenue."}
{"row_type":"trigger","trigger_id":"TRG-L205-004","case_id":"C10-L205-004","symbol":"253590","company_name":"Neosem","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","sector":"AI/Semiconductor/Electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-07","evidence_available_at_that_date":"FY2024 revenue and OP increased, with module and component tester businesses driving high profitability; memory module testers were nearly 90% of revenue.","evidence_source":"TheElec Global / KDPress, 2025-02-07 to 2025-02-09","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253590/2025.csv","profile_path":"atlas/symbol_profiles/253/253590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-07","entry_price":10100.0,"entry_ohlcv":{"o":9550.0,"h":10410.0,"l":9410.0,"c":10100.0,"v":1997349},"MFE_30D_pct":32.38,"MFE_90D_pct":32.38,"MFE_180D_pct":32.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.83,"MAE_90D_pct":-18.22,"MAE_180D_pct":-24.65,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":13370.0,"drawdown_after_peak_pct":-43.08,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_full_4B_trigger","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable_no_4C_trigger","trigger_outcome_label":"fy2024_record_revenue_op_memory_module_tester_bridge","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:253590:Stage2-Actionable:2025-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10-L205-004","trigger_id":"TRG-L205-004","symbol":"253590","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":39.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":17,"revision_score":12,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":41.8,"stage_label_after":"Stage2","changed_components":["supplier_order_conversion_required","late_beta_high_MAE_green_blocker"],"component_delta_explanation":"Direct order/revenue bridge is preserved, but product-pipeline or post-spike entries are capped; high-MAE rows block Yellow/Green rather than deleting Stage2.","MFE_90D_pct":32.38,"MAE_90D_pct":-18.22,"score_return_alignment_label":"fy2024_record_revenue_op_memory_module_tester_bridge","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10-L205-005","symbol":"092870","company_name":"Exicon","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"cxl_nonmemory_tester_contract_high_mae_cap","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"CXL / next-generation tester narrative plus domestic tester commercialization and supply-contract language, but issuer-level memory order conversion remained too thin for Actionable."}
{"row_type":"trigger","trigger_id":"TRG-L205-005","case_id":"C10-L205-005","symbol":"092870","company_name":"Exicon","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","sector":"AI/Semiconductor/Electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-06-25","evidence_available_at_that_date":"CXL / next-generation tester narrative plus domestic tester commercialization and supply-contract language, but issuer-level memory order conversion remained too thin for Actionable.","evidence_source":"Mirae Asset Securities / MoneyToday proxy, 2024-06-25","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-25","entry_price":17500.0,"entry_ohlcv":{"o":17010.0,"h":17850.0,"l":16950.0,"c":17500.0,"v":190010},"MFE_30D_pct":43.71,"MFE_90D_pct":43.71,"MFE_180D_pct":43.71,"MFE_1Y_pct":43.71,"MFE_2Y_pct":null,"MAE_30D_pct":-35.71,"MAE_90D_pct":-42.86,"MAE_180D_pct":-51.94,"MAE_1Y_pct":-51.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":25150.0,"drawdown_after_peak_pct":-66.56,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_full_4B_trigger","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable_no_4C_trigger","trigger_outcome_label":"cxl_nonmemory_tester_contract_high_mae_cap","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:Stage2:2024-06-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10-L205-005","trigger_id":"TRG-L205-005","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":0.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":22,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":0,"stage_label_after":"Stage4B","changed_components":["supplier_order_conversion_required","late_beta_high_MAE_green_blocker"],"component_delta_explanation":"Direct order/revenue bridge is preserved, but product-pipeline or post-spike entries are capped; high-MAE rows block Yellow/Green rather than deleting Stage2.","MFE_90D_pct":43.71,"MAE_90D_pct":-42.86,"score_return_alignment_label":"cxl_nonmemory_tester_contract_high_mae_cap","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"C10-L205-006","symbol":"092870","company_name":"Exicon","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ssd_cxl_tester_pipeline_without_supplier_order_conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Report highlighted Gen6 SSD / CXL tester demand expectation for 2025, but at trigger date this was product pipeline rather than recognized order/revenue bridge."}
{"row_type":"trigger","trigger_id":"TRG-L205-006","case_id":"C10-L205-006","symbol":"092870","company_name":"Exicon","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_SUPPLIER_ORDER_AND_LATE_BETA_COUNTEREXAMPLE_REPAIR_V5","sector":"AI/Semiconductor/Electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-10-24","evidence_available_at_that_date":"Report highlighted Gen6 SSD / CXL tester demand expectation for 2025, but at trigger date this was product pipeline rather than recognized order/revenue bridge.","evidence_source":"Naver/Mirae company report, 2024-10-24","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-24","entry_price":11650.0,"entry_ohlcv":{"o":11430.0,"h":13380.0,"l":11360.0,"c":11650.0,"v":1914572},"MFE_30D_pct":17.08,"MFE_90D_pct":35.28,"MFE_180D_pct":35.28,"MFE_1Y_pct":58.54,"MFE_2Y_pct":null,"MAE_30D_pct":-21.46,"MAE_90D_pct":-27.81,"MAE_180D_pct":-27.81,"MAE_1Y_pct":-27.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":15760.0,"drawdown_after_peak_pct":-37.88,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_full_4B_trigger","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable_no_4C_trigger","trigger_outcome_label":"ssd_cxl_tester_pipeline_without_supplier_order_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:Stage2:2024-10-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10-L205-006","trigger_id":"TRG-L205-006","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":0.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":22,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":0,"stage_label_after":"Stage4B","changed_components":["supplier_order_conversion_required","late_beta_high_MAE_green_blocker"],"component_delta_explanation":"Direct order/revenue bridge is preserved, but product-pipeline or post-spike entries are capped; high-MAE rows block Yellow/Green rather than deleting Stage2.","MFE_90D_pct":35.28,"MAE_90D_pct":-27.81,"score_return_alignment_label":"ssd_cxl_tester_pipeline_without_supplier_order_conversion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"205","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence"],"residual_error_types_found":["late_beta_after_contract_spike","product_pipeline_without_supplier_order_conversion","high_MAE_true_direct_order_green_blocker"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round: R2
completed_loop: 205
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```

## 28. Source Notes

```text
main_execution_prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
stock_web_manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
stock_web_schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
YC 2024 contract: https://zdnet.co.kr/view/?no=20240729101422
YC 2025 follow-on: https://www.thelec.kr/news/articleView.html?idxno=34431
Neosem Q3/FY2024: https://www.thelec.net/news/articleView.html?idxno=5039 ; https://www.thelec.net/news/articleView.html?idxno=5139
Exicon 2024 reports: https://securities.miraeasset.com/bbs/download/2129032.pdf?attachmentId=2129032 ; https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
