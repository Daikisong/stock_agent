# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R2
selected_loop = 128
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = mixed_c10_memory_recovery_equipment_cycle_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|memory_beta_vs_order_revenue_bridge_rule_discovery
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds **5 new independent C10 cases**, **5 usable trigger rows**, **2 positive cases**, **3 counterexamples**, and **4 current-profile residual errors**. The selected branch is not a generic HBM-equipment rerating branch. It is the memory-cycle recovery equipment branch: DRAM/NAND capex recovery, conversion investment, utilization recovery, CMP/strip/clean/transfer-tool exposure, and the boundary between actionable order/revenue bridge and late-cycle memory-beta price extension.

## 1. Current Calibrated Profile Assumption

The working proxy remains `e2r_2_1_stock_web_calibrated_proxy` with strict Green gates, Stage2 actionable bonus only when evidence quality is high, price-only blowoff blocking positive-stage promotion, full 4B requiring non-price evidence, and hard 4C requiring thesis-break evidence. This MD does not modify production scoring. It only proposes a C10-specific shadow rule candidate for later batch ingestion.

## 2. Round / Large Sector / Canonical Archetype Scope

C10 belongs to **R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS**. The selected scope is **C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE**, not C06 memory customer-capacity, not C07 HBM equipment order relative strength, not C08 test/socket customer-quality, and not C09 advanced-equipment valuation blowoff. The canonical compression rule for this loop is simple: memory-cycle recovery vocabulary is useful only when it can be wired into equipment orders, revenue recognition, margin/revision bridge, or utilization-driven consumable recovery.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index marks C10 as Priority 0 with **13 rows**, **13 symbols**, **0 positive / 13 counterexample balance**, and visible top covered symbols `036810`, `036930`, `067310`, `079370`, `084370`, `095610`. This loop avoids that visible top-symbol cluster and uses `319660`, `281820`, `240810`, `036200`, and `160980`. These are same-canonical but new-symbol rows relative to the visible top C10 set.

```text
coverage_before = C10 rows 13
coverage_after_if_accepted = C10 rows 18
need_to_30_after_if_accepted = 12
need_to_50_after_if_accepted = 32
same_archetype_new_symbol_count = 5
reused_case_count = 0
hard_duplicate_check = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields checked: source_name `FinanceData/marcap`, price_adjustment_status `raw_unadjusted_marcap`, max_date `2026-02-20`, calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`, raw_shard_root `atlas/ohlcv_raw_by_symbol_year`, schema_path `atlas/schema.json`, universe_path `atlas/universe/all_symbols.csv`. MFE/MAE is calculated as entry close versus the maximum high / minimum low in the next 30/90/180 tradable rows, using stock-web tradable shards.

## 5. Historical Eligibility Gate

All representative trigger rows have an entry date inside a stock-web tradable shard, an entry close, at least 180 forward trading rows, and complete `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`. All usable rows are clean for 180D corporate-action contamination. GST (`083450`) was examined as a possible C10 narrative row, but it is excluded from calibration because the raw-unadjusted 180D window contains stock-split/close-ratio contamination.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| MEMORY_DRY_STRIP_ETCH_CLEAN_TURNAROUND_BRIDGE | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Memory recovery plus PSK dry-process equipment exposure can be actionable when recovery maps to shipment/revenue bridge. |
| CMP_STEP_MEMORY_CAPEX_SLURRY_MARGIN_BRIDGE | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | CMP process-step increase and high-margin slurry recovery are a clean memory capex operating-leverage bridge. |
| EARLY_MEMORY_CONVERSION_REVENUE_BRIDGE_WITH_LOSS_CONTINUATION | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Revenue recovery without OP/revision conversion is only watch, not actionable rerating. |
| HBM_SCRUBBER_CHILLER_PRICE_EXTENSION_WITHOUT_NAMED_ORDER_BRIDGE | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | HBM/chiller vocabulary after price extension needs named order or revision bridge; otherwise 4B watch. |
| HBM_WAFER_TRANSFER_SECOND_VENDOR_BETA_WITHOUT_MARGIN_BRIDGE | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Second-vendor HBM beta without margin/order conversion is a high-MAE false-positive risk. |

## 7. Case Selection Summary

| case_id | symbol | company | trigger | role | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| C10_R2L128_319660_20240319 | 319660 | 피에스케이 | Stage2-Actionable | positive | 2024-03-19 | 26,850 | 45.62 | -2.42 | 45.62 | -42.09 | current_profile_stage2_good_but_4b_overlay_too_late |
| C10_R2L128_281820_20240524 | 281820 | 케이씨텍 | Stage2-Actionable | positive | 2024-05-24 | 37,150 | 58.82 | -20.73 | 58.82 | -32.30 | current_profile_positive_but_missing_high_mae_decay_guard |
| C10_R2L128_240810_20240809 | 240810 | 원익IPS | Stage2-Watch | counterexample | 2024-08-09 | 34,600 | 11.27 | -38.87 | 11.27 | -39.88 | current_profile_false_positive_if_stage2_actionable |
| C10_R2L128_036200_20240624 | 036200 | 유니셈 | Stage4B-Watch | counterexample | 2024-06-24 | 10,050 | 24.18 | -39.60 | 24.18 | -48.16 | current_profile_false_positive_if_hbm_vocabulary_promotes_stage2 |
| C10_R2L128_160980_20240417 | 160980 | 싸이맥스 | Stage4B-Watch | counterexample | 2024-04-17 | 19,480 | 21.92 | -40.20 | 21.92 | -61.96 | current_profile_false_positive_if_second_vendor_beta_promotes_stage2 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_watch_or_overlay_count = 4
4C_case_count = 0
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
representative_trigger_count = 5
current_profile_error_count = 5
```

C10 is a mixed branch: it can produce real Stage2-Actionable samples when memory recovery is tied to equipment steps, customer capex, and margin/revision conversion; it also creates many false positives because “memory recovery” is a broad beta wave. This loop intentionally pairs two positive rows with three counterexamples so the archetype can learn the difference between bridge and mist.

## 9. Evidence Source Map

| symbol | trigger_date | source | URL | evidence interpretation |
|---:|---:|---|---|---|
| 319660 | 2024-03-19 | Shinhan Securities company report PDF, 2024-03-19 | https://ssl.pstatic.net/imgstock/upload/research/company/1710804567070.pdf | Memory DRAM/NAND recovery plus PR-strip/dry-clean/dry-etch exposure gives a cleaner order/revenue bridge than generic memory-beta language. |
| 281820 | 2024-05-24 | NewsPim / DS Investment report briefing, 2024-05-24 | https://www.newspim.com/news/view/20240524000219 | CMP process-step increase, HBM stacking layer count, memory-customer CMP supply, and high-margin slurry recovery link memory capex to operating leverage. |
| 240810 | 2024-08-09 | The Value News, 2024-08-09 | https://www.thevaluenews.co.kr/news/184815 | Revenue recovery and DRAM/NAND conversion-investment vocabulary existed, but 2Q24 operating loss continuation meant the order/revenue bridge had not converted to earnings quality. |
| 036200 | 2024-06-24 | Daum / ZDNet Korea, 2024-06-24 | https://v.daum.net/v/20240624162722203 | HBM scrubbing/chiller and NAND cryogenic chiller narrative was real, but the trigger came after a sharp price extension and lacked a fresh named-order/revision bridge. |
| 160980 | 2024-04-17 | Daum / iNews24, 2024-04-17 | https://v.daum.net/v/20240417083011557 | HBM wafer-transfer and second-vendor narrative created memory-cycle beta, but it was not enough without shipment, margin, or customer-order conversion. |

## 10. Price Data Source Map

| symbol | profile_path | entry shard | forward shard coverage | 180D corporate-action status |
|---:|---|---|---|---|
| 319660 | atlas/symbol_profiles/319/319660.json | atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv | 2024-2025 where needed | clean_180D_window |
| 281820 | atlas/symbol_profiles/281/281820.json | atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv | 2024-2025 where needed | clean_180D_window |
| 240810 | atlas/symbol_profiles/240/240810.json | atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv | 2024-2025 where needed | clean_180D_window |
| 036200 | atlas/symbol_profiles/036/036200.json | atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv | 2024-2025 where needed | clean_180D_window |
| 160980 | atlas/symbol_profiles/160/160980.json | atlas/ohlcv_tradable_by_symbol_year/160/160980/2024.csv | 2024-2025 where needed | clean_180D_window |

## 11. Case-by-Case Trigger Notes

### Case 1 — PSK / 319660 / dry strip-clean memory recovery positive with 4B overlay

The source report describes PSK as a semiconductor equipment maker with PR strip as the main revenue pillar and additional dry cleaner / dry etcher / bevel etcher exposure. The investment point is a second-half memory-turnaround bridge, not just a theme tag. The stock-web path supports Stage2-Actionable: +24.77% MFE in 30D and +45.62% in 90D/180D. However, the same path later printed -42.09% 180D MAE and -60.23% drawdown after the 180D peak. The lesson is not to reject the positive; it is to attach a post-peak 4B guard after the order/revenue bridge rally has already played out.

### Case 2 — KCTech / 281820 / CMP step and slurry margin bridge positive

The evidence is cleaner than generic memory beta: CMP process-step growth, HBM stack layer count, memory-customer CMP equipment supply, and high-margin slurry recovery. The path delivered +34.59% MFE in 30D and +58.82% MFE in 90D/180D. The drawdown after the 180D peak was severe (-57.37%), so this is a Stage2/Yellow candidate with Green blocked until revision and high-MAE guard pass.

### Case 3 — Wonik IPS / 240810 / early conversion investment watch, not actionable

Wonik IPS had revenue recovery and DRAM/NAND conversion-investment language, but operating loss continued in 2Q24. That is the missing gear. The price path gave only +11.27% MFE across all windows while 90D/180D MAE reached -38.87%/-39.88%. C10 should not upgrade this to Stage2-Actionable until OP or revision confirms that equipment revenue is converting into earnings.

### Case 4 — Unisem / 036200 / HBM scrubber and chiller vocabulary after price extension

Unisem had real HBM-process scrubber and chiller narrative, with major memory customers and NAND cryogenic chiller optionality. But the trigger row came after a sharp run, and there was no fresh named-order or estimate-revision bridge at the trigger. The path gave some local upside (+24.18% MFE), then -48.16% 180D MAE and -58.25% post-peak drawdown. This belongs to local 4B watch, not actionable positive rerating.

### Case 5 — Cymechs / 160980 / HBM wafer-transfer second-vendor beta false positive

Cymechs had HBM wafer-transfer equipment and second-vendor narrative. This is exactly the kind of memory-cycle equipment beta that can seduce a Stage2 engine. The price path says the evidence was not yet enough: +21.92% MFE but -61.96% 180D MAE and -68.80% post-peak drawdown. The missing pieces were shipment confirmation, customer order size, and margin/revision bridge.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | clean window |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TRG_C10_R2L128_319660_20240319 | 2024-03-19 | 26,850 | 24.77 | -2.42 | 45.62 | -2.42 | 45.62 | -42.09 | 2024-07-11 | 39,100 | -60.23 | clean_180D_window |
| TRG_C10_R2L128_281820_20240524 | 2024-05-24 | 37,150 | 34.59 | -1.75 | 58.82 | -20.73 | 58.82 | -32.30 | 2024-07-11 | 59,000 | -57.37 | clean_180D_window |
| TRG_C10_R2L128_240810_20240809 | 2024-08-09 | 34,600 | 11.27 | -20.09 | 11.27 | -38.87 | 11.27 | -39.88 | 2024-08-21 | 38,500 | -45.97 | clean_180D_window |
| TRG_C10_R2L128_036200_20240624 | 2024-06-24 | 10,050 | 24.18 | -21.69 | 24.18 | -39.60 | 24.18 | -48.16 | 2024-07-04 | 12,480 | -58.25 | clean_180D_window |
| TRG_C10_R2L128_160980_20240417 | 2024-04-17 | 19,480 | 21.92 | -10.32 | 21.92 | -40.20 | 21.92 | -61.96 | 2024-05-29 | 23,750 | -68.80 | clean_180D_window |

## 13. Current Calibrated Profile Stress Test

| case_id | likely current judgement | proposed judgement | current_profile_verdict | residual diagnosis |
|---|---|---|---|---|
| C10_R2L128_319660_20240319 | Stage2-Actionable | Stage2-Actionable + 4B local watch | current_profile_stage2_good_but_4b_overlay_too_late | Stage2-Actionable with mandatory 4B-after-peak guard |
| C10_R2L128_281820_20240524 | Stage2-Actionable | Stage2-Actionable + high-MAE guard | current_profile_positive_but_missing_high_mae_decay_guard | Stage2-Actionable; Green blocked until margin/revision and post-peak MAE guard pass |
| C10_R2L128_240810_20240809 | Stage2-Actionable candidate | Stage2-Watch / counterexample | current_profile_false_positive_if_stage2_actionable | Stage2-Watch only until OP/revision bridge confirms |
| C10_R2L128_036200_20240624 | Stage2-Actionable candidate | Stage4B-Watch / price-extension block | current_profile_false_positive_if_hbm_vocabulary_promotes_stage2 | local 4B watch; require order/revision bridge for Stage2-Actionable |
| C10_R2L128_160980_20240417 | Stage2-Actionable candidate | Stage4B-Watch / bridge-missing block | current_profile_false_positive_if_second_vendor_beta_promotes_stage2 | Stage4B-Watch; block actionable until named order/revenue bridge exists |

## 14. Stage2 / Yellow / Green Comparison

This loop does **not** propose a Stage3-Green loosening. PSK and KCTech can be Stage2/Yellow because the evidence connects memory recovery to specific process equipment and revenue/margin bridge. Even there, Green should be blocked by high post-peak drawdown and the need for revision confirmation. Wonik IPS, Unisem, and Cymechs show that memory recovery vocabulary without OP/revision/order confirmation creates high-MAE false positives.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B/4C timing verdict | local/full interpretation |
|---|---|---|
| PSK | positive_then_4B_overlay | Positive early path was valid, but full 180D window requires a post-peak 4B guard. |
| KCTech | positive_with_high_mae_guard | Strong MFE validates Stage2, while -32.30% 180D MAE blocks Green and requires decay guard. |
| Wonik IPS | false_stage2_watch_only | OP-loss continuation plus weak MFE and large MAE argue against actionable promotion. |
| Unisem | local_4B_watch | HBM/chiller vocabulary produced local upside, but full-window drawdown was too large. |
| Cymechs | local_4B_or_false_positive | Second-vendor beta is insufficient without shipment/margin bridge. |

## 16. 4C Protection Audit

No hard 4C row is proposed in this loop. C10 is usually a Stage2/Yellow/4B boundary archetype. The hard 4C route should require a thesis break such as order cancellation, utilization collapse, margin break, or funding/going-concern stress. Large MAE alone should not be promoted to 4C unless non-price evidence confirms business deterioration.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L2_MEMORY_RECOVERY_EQUIPMENT_BRIDGE_GATE_V1
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
rule = In L2 memory-cycle equipment names, memory capex recovery or HBM vocabulary can open Stage2-Watch. Stage2-Actionable requires at least one bridge: named customer/order, explicit equipment step increase, revenue-recognition path, margin/revision confirmation, or utilization/consumable recovery. If evidence is only beta vocabulary after a price extension, route to local 4B watch.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C10_MEMORY_RECOVERY_ORDER_REVENUE_BRIDGE_V1
scope = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
positive examples = 319660_20240319, 281820_20240524
counterexamples = 240810_20240809, 036200_20240624, 160980_20240417
new_axis_proposed = c10_order_revenue_margin_bridge_vs_memory_beta_gate
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|green_not_loosened_by_v12
existing_axis_weakened = none
```

C10 behaves like a factory power switch. The memory cycle can turn the lights on across the building, but only machines connected to a working belt—orders, shipments, revenue recognition, or margin—should be treated as productive output. Unconnected bulbs still glow for a while; then the heat becomes drawdown.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_count | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | Memory recovery beta can over-promote generic equipment names | 5 | 32.36 | -28.36 | 32.36 | -44.88 | 3 | 1 | mixed; captures PSK/KCTech but over-trusts beta vocabulary |
| P1_L2_sector_specific_candidate_profile | sector shadow | Require order/revenue/margin bridge before actionable Stage2 | 5 | 32.36 | -28.36 | 32.36 | -44.88 | 1 | 0 | better false-positive suppression |
| P2_C10_canonical_candidate_profile | canonical shadow | Separate C10 bridge positives from C10 memory-beta extensions | 5 | 32.36 | -28.36 | 32.36 | -44.88 | 0 | 0 | best alignment in this sample |
| P3_counterexample_guard_profile | guard shadow | Any high-MAE risk blocks Stage2 until confirmation | 5 | 32.36 | -28.36 | 32.36 | -44.88 | 0 | 1 | too conservative for PSK/KCTech |

## 20. Raw Component Score Proxy

| case_id | baseline_score_proxy | candidate_score_proxy | delta | role | MFE_180D_pct | MAE_180D_pct |
|---|---:|---:|---:|---|---:|---:|
| C10_R2L128_319660_20240319 | 67 | 75 | +8 | positive | 45.62 | -42.09 |
| C10_R2L128_281820_20240524 | 69 | 77 | +8 | positive | 58.82 | -32.30 |
| C10_R2L128_240810_20240809 | 65 | 57 | -8 | counterexample | 11.27 | -39.88 |
| C10_R2L128_036200_20240624 | 68 | 55 | -13 | counterexample | 24.18 | -48.16 |
| C10_R2L128_160980_20240417 | 66 | 54 | -12 | counterexample | 21.92 | -61.96 |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_watch_or_overlay_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed_c10_memory_recovery_equipment_cycle_leaf_set | 2 | 3 | 4 | 0 | 5 | 0 | 5 | 5 | 5 | L2_MEMORY_RECOVERY_EQUIPMENT_BRIDGE_GATE_V1 | C10_MEMORY_RECOVERY_ORDER_REVENUE_BRIDGE_V1 | C10 rows 13 -> 18 if accepted; need 12 to 30, 32 to 50 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 3
current_profile_error_count: 5
coverage_before: C10 rows 13
coverage_after_if_accepted: C10 rows 18
need_to_30_after_if_accepted: 12
need_to_50_after_if_accepted: 32
do_not_propose_new_weight_delta: false
production_scoring_changed: false
shadow_weight_only: true
```

## 23. Shadow Weight Recommendation

```jsonl
{"row_type":"shadow_weight_recommendation","scope":"L2_AI_SEMICONDUCTOR_ELECTRONICS","candidate_rule":"L2_MEMORY_RECOVERY_EQUIPMENT_BRIDGE_GATE_V1","proposed_change":"Increase Stage2 evidence quality only when order/revenue/margin bridge exists; add high-MAE local 4B guard for memory beta extensions.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight_recommendation","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_rule":"C10_MEMORY_RECOVERY_ORDER_REVENUE_BRIDGE_V1","positive_anchor_cases":["C10_R2L128_319660_20240319","C10_R2L128_281820_20240524"],"counterexample_anchor_cases":["C10_R2L128_240810_20240809","C10_R2L128_036200_20240624","C10_R2L128_160980_20240417"],"production_scoring_changed":false,"shadow_weight_only":true}
```

## 24. Machine-Readable Case JSONL

```jsonl
{"row_type": "case_summary", "case_id": "C10_R2L128_319660_20240319", "symbol": "319660", "company": "피에스케이", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_DRY_STRIP_ETCH_CLEAN_TURNAROUND_BRIDGE", "role": "positive", "trigger_family": "Stage2-Actionable", "evidence_summary": "Memory DRAM/NAND recovery plus PR-strip/dry-clean/dry-etch exposure gives a cleaner order/revenue bridge than generic memory-beta language.", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1710804567070.pdf", "representative_trigger_id": "TRG_C10_R2L128_319660_20240319"}
{"row_type": "case_summary", "case_id": "C10_R2L128_281820_20240524", "symbol": "281820", "company": "케이씨텍", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "CMP_STEP_MEMORY_CAPEX_SLURRY_MARGIN_BRIDGE", "role": "positive", "trigger_family": "Stage2-Actionable", "evidence_summary": "CMP process-step increase, HBM stacking layer count, memory-customer CMP supply, and high-margin slurry recovery link memory capex to operating leverage.", "source_url": "https://www.newspim.com/news/view/20240524000219", "representative_trigger_id": "TRG_C10_R2L128_281820_20240524"}
{"row_type": "case_summary", "case_id": "C10_R2L128_240810_20240809", "symbol": "240810", "company": "원익IPS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "EARLY_MEMORY_CONVERSION_REVENUE_BRIDGE_WITH_LOSS_CONTINUATION", "role": "counterexample", "trigger_family": "Stage2-Watch", "evidence_summary": "Revenue recovery and DRAM/NAND conversion-investment vocabulary existed, but 2Q24 operating loss continuation meant the order/revenue bridge had not converted to earnings quality.", "source_url": "https://www.thevaluenews.co.kr/news/184815", "representative_trigger_id": "TRG_C10_R2L128_240810_20240809"}
{"row_type": "case_summary", "case_id": "C10_R2L128_036200_20240624", "symbol": "036200", "company": "유니셈", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_SCRUBBER_CHILLER_PRICE_EXTENSION_WITHOUT_NAMED_ORDER_BRIDGE", "role": "counterexample", "trigger_family": "Stage4B-Watch", "evidence_summary": "HBM scrubbing/chiller and NAND cryogenic chiller narrative was real, but the trigger came after a sharp price extension and lacked a fresh named-order/revision bridge.", "source_url": "https://v.daum.net/v/20240624162722203", "representative_trigger_id": "TRG_C10_R2L128_036200_20240624"}
{"row_type": "case_summary", "case_id": "C10_R2L128_160980_20240417", "symbol": "160980", "company": "싸이맥스", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_WAFER_TRANSFER_SECOND_VENDOR_BETA_WITHOUT_MARGIN_BRIDGE", "role": "counterexample", "trigger_family": "Stage4B-Watch", "evidence_summary": "HBM wafer-transfer and second-vendor narrative created memory-cycle beta, but it was not enough without shipment, margin, or customer-order conversion.", "source_url": "https://v.daum.net/v/20240417083011557", "representative_trigger_id": "TRG_C10_R2L128_160980_20240417"}
```

## 25. Machine-Readable Trigger JSONL

```jsonl
{"row_type": "trigger_row", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_DRY_STRIP_ETCH_CLEAN_TURNAROUND_BRIDGE", "case_id": "C10_R2L128_319660_20240319", "trigger_id": "TRG_C10_R2L128_319660_20240319", "symbol": "319660", "company": "피에스케이", "trigger_date": "2024-03-19", "entry_date": "2024-03-19", "entry_price": 26850, "trigger_type": "Stage2-Actionable", "role": "positive", "MFE_30D_pct": 24.77, "MAE_30D_pct": -2.42, "MFE_90D_pct": 45.62, "MAE_90D_pct": -2.42, "MFE_180D_pct": 45.62, "MAE_180D_pct": -42.09, "peak_180D_date": "2024-07-11", "peak_180D_price": 39100, "drawdown_after_peak_180D_pct": -60.23, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv", "corporate_action_status": "clean_180D_window", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1710804567070.pdf", "current_profile_verdict": "current_profile_stage2_good_but_4b_overlay_too_late", "proposed_profile_verdict": "Stage2-Actionable with mandatory 4B-after-peak guard"}
{"row_type": "trigger_row", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "CMP_STEP_MEMORY_CAPEX_SLURRY_MARGIN_BRIDGE", "case_id": "C10_R2L128_281820_20240524", "trigger_id": "TRG_C10_R2L128_281820_20240524", "symbol": "281820", "company": "케이씨텍", "trigger_date": "2024-05-24", "entry_date": "2024-05-24", "entry_price": 37150, "trigger_type": "Stage2-Actionable", "role": "positive", "MFE_30D_pct": 34.59, "MAE_30D_pct": -1.75, "MFE_90D_pct": 58.82, "MAE_90D_pct": -20.73, "MFE_180D_pct": 58.82, "MAE_180D_pct": -32.3, "peak_180D_date": "2024-07-11", "peak_180D_price": 59000, "drawdown_after_peak_180D_pct": -57.37, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv", "corporate_action_status": "clean_180D_window", "source_url": "https://www.newspim.com/news/view/20240524000219", "current_profile_verdict": "current_profile_positive_but_missing_high_mae_decay_guard", "proposed_profile_verdict": "Stage2-Actionable; Green blocked until margin/revision and post-peak MAE guard pass"}
{"row_type": "trigger_row", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "EARLY_MEMORY_CONVERSION_REVENUE_BRIDGE_WITH_LOSS_CONTINUATION", "case_id": "C10_R2L128_240810_20240809", "trigger_id": "TRG_C10_R2L128_240810_20240809", "symbol": "240810", "company": "원익IPS", "trigger_date": "2024-08-09", "entry_date": "2024-08-09", "entry_price": 34600, "trigger_type": "Stage2-Watch", "role": "counterexample", "MFE_30D_pct": 11.27, "MAE_30D_pct": -20.09, "MFE_90D_pct": 11.27, "MAE_90D_pct": -38.87, "MFE_180D_pct": 11.27, "MAE_180D_pct": -39.88, "peak_180D_date": "2024-08-21", "peak_180D_price": 38500, "drawdown_after_peak_180D_pct": -45.97, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "corporate_action_status": "clean_180D_window", "source_url": "https://www.thevaluenews.co.kr/news/184815", "current_profile_verdict": "current_profile_false_positive_if_stage2_actionable", "proposed_profile_verdict": "Stage2-Watch only until OP/revision bridge confirms"}
{"row_type": "trigger_row", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_SCRUBBER_CHILLER_PRICE_EXTENSION_WITHOUT_NAMED_ORDER_BRIDGE", "case_id": "C10_R2L128_036200_20240624", "trigger_id": "TRG_C10_R2L128_036200_20240624", "symbol": "036200", "company": "유니셈", "trigger_date": "2024-06-24", "entry_date": "2024-06-24", "entry_price": 10050, "trigger_type": "Stage4B-Watch", "role": "counterexample", "MFE_30D_pct": 24.18, "MAE_30D_pct": -21.69, "MFE_90D_pct": 24.18, "MAE_90D_pct": -39.6, "MFE_180D_pct": 24.18, "MAE_180D_pct": -48.16, "peak_180D_date": "2024-07-04", "peak_180D_price": 12480, "drawdown_after_peak_180D_pct": -58.25, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv", "corporate_action_status": "clean_180D_window", "source_url": "https://v.daum.net/v/20240624162722203", "current_profile_verdict": "current_profile_false_positive_if_hbm_vocabulary_promotes_stage2", "proposed_profile_verdict": "local 4B watch; require order/revision bridge for Stage2-Actionable"}
{"row_type": "trigger_row", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_WAFER_TRANSFER_SECOND_VENDOR_BETA_WITHOUT_MARGIN_BRIDGE", "case_id": "C10_R2L128_160980_20240417", "trigger_id": "TRG_C10_R2L128_160980_20240417", "symbol": "160980", "company": "싸이맥스", "trigger_date": "2024-04-17", "entry_date": "2024-04-17", "entry_price": 19480, "trigger_type": "Stage4B-Watch", "role": "counterexample", "MFE_30D_pct": 21.92, "MAE_30D_pct": -10.32, "MFE_90D_pct": 21.92, "MAE_90D_pct": -40.2, "MFE_180D_pct": 21.92, "MAE_180D_pct": -61.96, "peak_180D_date": "2024-05-29", "peak_180D_price": 23750, "drawdown_after_peak_180D_pct": -68.8, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/160/160980/2024.csv", "corporate_action_status": "clean_180D_window", "source_url": "https://v.daum.net/v/20240417083011557", "current_profile_verdict": "current_profile_false_positive_if_second_vendor_beta_promotes_stage2", "proposed_profile_verdict": "Stage4B-Watch; block actionable until named order/revenue bridge exists"}
```

## 26. Score Simulation JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C10_R2L128_319660_20240319", "profile_id": "P2_C10_canonical_candidate_profile", "baseline_score_proxy": 67, "candidate_score_proxy": 75, "score_delta_proxy": 8, "stage_before_proxy": "Stage2-Actionable", "stage_after_proxy": "Stage2-Actionable + 4B local watch", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C10_R2L128_281820_20240524", "profile_id": "P2_C10_canonical_candidate_profile", "baseline_score_proxy": 69, "candidate_score_proxy": 77, "score_delta_proxy": 8, "stage_before_proxy": "Stage2-Actionable", "stage_after_proxy": "Stage2-Actionable + high-MAE guard", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C10_R2L128_240810_20240809", "profile_id": "P2_C10_canonical_candidate_profile", "baseline_score_proxy": 65, "candidate_score_proxy": 57, "score_delta_proxy": -8, "stage_before_proxy": "Stage2-Actionable candidate", "stage_after_proxy": "Stage2-Watch / counterexample", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C10_R2L128_036200_20240624", "profile_id": "P2_C10_canonical_candidate_profile", "baseline_score_proxy": 68, "candidate_score_proxy": 55, "score_delta_proxy": -13, "stage_before_proxy": "Stage2-Actionable candidate", "stage_after_proxy": "Stage4B-Watch / price-extension block", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C10_R2L128_160980_20240417", "profile_id": "P2_C10_canonical_candidate_profile", "baseline_score_proxy": 66, "candidate_score_proxy": 54, "score_delta_proxy": -12, "stage_before_proxy": "Stage2-Actionable candidate", "stage_after_proxy": "Stage4B-Watch / bridge-missing block", "production_scoring_changed": false, "shadow_weight_only": true}
```

## 27. Aggregate JSONL

```jsonl
{"row_type":"aggregate_summary","selected_round":"R2","selected_loop":128,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","coverage_before":13,"coverage_after_if_accepted":18,"new_independent_case_count":5,"usable_trigger_row_count":5,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":4,"avg_MFE_90D_pct":32.36,"avg_MAE_90D_pct":-28.36,"avg_MFE_180D_pct":32.36,"avg_MAE_180D_pct":-44.88,"sector_rule_candidate":"L2_MEMORY_RECOVERY_EQUIPMENT_BRIDGE_GATE_V1","canonical_rule_candidate":"C10_MEMORY_RECOVERY_ORDER_REVENUE_BRIDGE_V1","production_scoring_changed":false,"shadow_weight_only":true}
```

## 28. Narrative-Only / Blocked Rows

```jsonl
{"row_type": "narrative_only_blocked_price_row", "symbol": "083450", "company": "GST", "requested_trigger_date": "2024-04-01", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "reason": "corporate_action_contaminated_180D_window", "blocked_from_calibration": true, "observed_corporate_action_candidates": [{"d": "2024-06-26", "type": "close_ratio", "prev_c": 43300.0, "c": 21600.0, "ratio": 0.4988}, {"d": "2024-07-24", "type": "shares_change", "prev_s": 9317745, "s": 18618260, "ratio": 1.9982}], "note": "Potential HBM/scrubber/chiller narrative row, but excluded from usable trigger rows because stock-web raw-unadjusted window has split/close-ratio contamination."}
```

GST is explicitly not counted as a usable trigger row. It is kept here only to prevent the future research loop from accidentally using a contaminated raw-unadjusted price window as calibration evidence.

## 29. Deferred Coding-Agent Handoff Prompt

```text
DO NOT EXECUTE IN THIS RESEARCH LOOP.
When converting this MD into code changes, run the existing v12 calibration ingest first. If the C10 rows validate, add a shadow candidate for C10_MEMORY_RECOVERY_ORDER_REVENUE_BRIDGE_V1. The implementation should not loosen Stage3-Green. It should add an archetype-scoped Stage2 quality gate: memory recovery vocabulary alone = Stage2-Watch; actionable Stage2 requires named order/customer, revenue-recognition bridge, margin/revision confirmation, or utilization/consumable recovery. Add high-MAE local 4B guard for price extensions without order/revision bridge.
```

## 30. Next Research State

```text
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
avoid_next_due_recent_session = C18|C26|C29|C30|C02|C09|C14|C10
coverage_index_first = true
sequential_round_cycle_required = false
```

## 31. Validation Self-Check

```text
standard_filename = pass
round_large_sector_archetype_consistency = pass
actual_stock_web_1D_OHLC_used = pass
price_basis_tradable_raw = pass
price_adjustment_status_raw_unadjusted_marcap = pass
manifest_max_date_respected = pass
MFE_MAE_30_90_180_present_for_all_usable_rows = pass
at_least_one_positive_and_one_counterexample = pass
no_live_candidate_discovery = pass
no_code_patch = pass
no_production_scoring_change = pass
shadow_weight_only = pass
no_repeat_hard_duplicate_check = pass
```
