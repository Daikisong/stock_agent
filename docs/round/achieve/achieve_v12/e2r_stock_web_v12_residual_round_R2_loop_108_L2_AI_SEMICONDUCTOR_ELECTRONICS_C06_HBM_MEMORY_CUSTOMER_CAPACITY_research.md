# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R2
selected_loop: 108
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows / C06 rows 17 need-to-30 13
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: mixed_C06_hbm_customer_capacity_allocation_set
loop_objective: coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_residual_round_R2_loop_108_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 3 counterexamples, and 4 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

## 1. Current Calibrated Profile Assumption

Baseline proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. Existing global axes are treated as already applied: `stage2_required_bridge`, `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`. This MD does not propose a global patch; it proposes C06-scoped shadow rules.

## 2. Round / Large Sector / Canonical Archetype Scope

- `C06_HBM_MEMORY_CUSTOMER_CAPACITY` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- Scope: HBM memory customer qualification, capacity allocation, AI-memory mix/ASP, HBM-adjacent substrate/customer narratives.
- Non-scope: pure HBM equipment order conversion should usually be `C07`; pure test socket/customer quality should usually be `C08`; memory equipment beta should usually be `C10`.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index marks C06 as Priority 0 with 17 rows and need-to-30 of 13. Existing top C06 symbols were not used as the core set; this loop uses five symbols not shown in the top-covered C06 list: `000660`, `005930`, `222800`, `353200`, `011070`. Hard duplicate key check uses `canonical_archetype_id + symbol + trigger_type + entry_date`.

```yaml
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_trigger_family_count: 5
minimum_new_independent_case_ratio: 1.00
hard_duplicate_detected: false
```

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
source: Songdaiki/stock-web
source_url: https://github.com/Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
profile_root: atlas/symbol_profiles
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
```

MFE/MAE formula used exactly the stock-web schema convention: `MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100`.

## 5. Historical Eligibility Gate

All five representative trigger rows pass: entry row exists in tradable shard, entry price is the `c` column, forward window has at least 180 trading days, and share-count discontinuity inside entry~D+180 is below the 20% corporate-action contamination threshold.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | compressed canonical | rule meaning |
|---|---|---|
| HBM_SUPPLIER_CUSTOMER_CAPACITY_ALLOCATION_POSITIVE | C06 | signed customer demand + capacity allocation + margin bridge |
| HBM_CUSTOMER_QUALIFICATION_DELAY_4B_COUNTEREXAMPLE | C06 | HBM narrative without qualification is 4B/watch, not Stage3 |
| HBM_DDR5_CUSTOMER_UTILIZATION_PROXY_FALSE_STAGE2 | C06 | memory-utilization proxy is not enough without conversion |
| HBM_ADJACENT_SUBSTRATE_ASP_RECOVERY_FALSE_STAGE2 | C06 | FC-BGA/DDR5 ASP analogy needs customer/revenue bridge |
| HBM_ADJACENT_AI_CHIP_SUBSTRATE_CUSTOMER_QUALIFICATION_HIGH_MAE | C06 | customer qualification can be Stage2-Actionable but needs 4B watch if margin/revision absent |

## 7. Case Selection Summary

|case_id|symbol|company|role|trigger_type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C06_R2L108_000660_HBM3E_CUSTOMER_CAPACITY_SOLDOUT_20240425|000660|SK하이닉스|positive|Stage3-Green|2024-04-25|2024-04-26|177800|39.76|-14.74|39.76|-18.62|current_profile_correct|
|C06_R2L108_005930_HBM3E_NVIDIA_QUALIFICATION_FAIL_20240524|005930|삼성전자|counterexample|Stage4B|2024-05-24|2024-05-27|77200|15.03|-22.93|15.03|-35.36|current_profile_false_positive|
|C06_R2L108_222800_MEMORY_SUBSTRATE_UTILIZATION_RECOVERY_FALSE_STAGE2_20240111|222800|심텍|counterexample|Stage2|2024-01-11|2024-01-12|38100|3.41|-27.3|3.41|-55.64|current_profile_false_positive|
|C06_R2L108_353200_FCBGA_DDR5_ASP_RECOVERY_FALSE_STAGE2_20240111|353200|대덕전자|counterexample|Stage2|2024-01-11|2024-01-12|27550|2.54|-19.96|2.54|-38.62|current_profile_false_positive|
|C06_R2L108_011070_FCBGA_INTEL_NVIDIA_CUSTOMER_QUALIFICATION_HIGH_MAE_20240612|011070|LG이노텍|positive|Stage2-Actionable|2024-06-12|2024-06-13|245000|24.69|-30.12|24.69|-42.98|current_profile_4B_too_late|


## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 3
4B_case_count: 1
4C_case_count: 0
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
current_profile_error_count: 4
```

The positive cases are SK hynix and LG Innotek. SK hynix is clean structural success. LG Innotek is positive for customer qualification but mixed because the +24.69% MFE path later became a -42.98% 180D MAE path. Samsung, Simmtech, and Daeduck Electronics are counterexamples showing that HBM/customer/capacity language needs customer sign-off and conversion bridge.

## 9. Evidence Source Map

| symbol | evidence date | source URL | evidence used |
|---|---:|---|---|
| 000660 | 2024-04-25 | https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/ | Q1 profit recovery, HBM/AI demand, Nvidia-linked HBM leadership and capacity signal |
| 005930 | 2024-05-24 | https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/ | HBM3/HBM3E Nvidia test failure due heat/power; customer qualification risk |
| 222800 | 2024-01-11 | https://www.simmtech.com/upload/media/file/638406815140413547.pdf | DRAM utilization expected to recover from HBM/DDR5 demand; proxy not confirmed conversion |
| 353200 | 2024-01-11 | https://www.daeduck.com/file/board/651.do | DDR5 penetration, high-value substrate mix, FC-BGA normalization; proxy not enough |
| 011070 | 2024-06-12 | https://www.businesskorea.co.kr/news/articleView.html?idxno=218911 | FC-BGA supply to Intel/NVIDIA; HBM-adjacent substrate bottleneck narrative |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | years used |
|---|---|---|---|
| 000660 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv + 2025.csv | atlas/symbol_profiles/000/000660.json | 2024-2025 |
| 005930 | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv + 2025.csv | atlas/symbol_profiles/005/005930.json | 2024-2025 |
| 222800 | atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv + 2025.csv | atlas/symbol_profiles/222/222800.json | 2024-2025 |
| 353200 | atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv + 2025.csv | atlas/symbol_profiles/353/353200.json | 2024-2025 |
| 011070 | atlas/ohlcv_tradable_by_symbol_year/011/011070/2024.csv + 2025.csv | atlas/symbol_profiles/011/011070.json | 2024-2025 |

## 11. Case-by-Case Trigger Grid

### 11.1 000660 SK하이닉스 — structural HBM customer/capacity success
Stage2 evidence had public event, customer quality, capacity route, and early revision. Stage3 evidence had confirmed revision, margin bridge, financial visibility, durable HBM customer confirmation and low red-team risk. The 90D MFE of 39.76% validates promotion, although the later peak drawdown argues for a separate 4B overlay after July 2024.

### 11.2 005930 삼성전자 — qualification-delay 4B counterexample
The evidence is not simply weak HBM beta; it is a customer qualification obstacle. A profile that scores Samsung as Stage2/Stage3 on HBM capacity alone would be false positive. The 180D MAE of -35.36% confirms that C06 must gate HBM promotion on customer sign-off and supply allocation.

### 11.3 222800 심텍 — memory-substrate proxy false Stage2
The report evidence described DRAM utilization recovery driven by HBM and DDR5. But this remained a customer-utilization proxy, not confirmed customer allocation or margin conversion. The price path was immediately adverse: 30D MAE -24.28%, 180D MAE -55.64%.

### 11.4 353200 대덕전자 — FC-BGA/DDR5 ASP recovery false Stage2
The substrate narrative had plausible ASP and mix logic, but not enough C06 customer sign-off. The 90D MFE was only 2.54% and the 180D MAE was -38.62%, supporting a C06 proxy decontamination gate.

### 11.5 011070 LG이노텍 — customer qualification positive but high-MAE watch
The Intel/NVIDIA FC-BGA report was stronger than a generic AI/HBM analogy, so Stage2-Actionable is justified. But without margin/revision confirmation, Green should be blocked. The path produced +24.69% MFE and then -42.98% 180D MAE, so C06 needs a local 4B watch for fast MFE with unconfirmed margin bridge.

## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|corp_action|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|000660|2024-04-26|177800|21.48|-4.95|39.76|-14.74|39.76|-18.62|2024-07-11|248500|-41.77|clean_180D_window|
|005930|2024-05-27|77200|14.77|-4.79|15.03|-22.93|15.03|-35.36|2024-07-11|88800|-43.81|clean_180D_window|
|222800|2024-01-12|38100|3.41|-24.28|3.41|-27.3|3.41|-55.64|2024-01-12|39400|-57.11|clean_180D_window|
|353200|2024-01-12|27550|2.54|-18.51|2.54|-19.96|2.54|-38.62|2024-01-12|28250|-40.14|clean_180D_window|
|011070|2024-06-13|245000|24.69|-2.24|24.69|-30.12|24.69|-42.98|2024-07-17|305500|-54.27|clean_180D_window|


## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely action | actual path | verdict |
|---|---|---|---|
| 000660 | Stage3-Green accepted | MFE90 +39.76 / MAE90 -14.74 | current_profile_correct |
| 005930 | HBM beta could be over-promoted unless customer qualification gate dominates | MFE180 +15.03 / MAE180 -35.36 | current_profile_false_positive |
| 222800 | DDR5/HBM utilization proxy could pass Stage2 | MFE180 +3.41 / MAE180 -55.64 | current_profile_false_positive |
| 353200 | FC-BGA/DDR5 ASP recovery could pass Stage2 | MFE180 +2.54 / MAE180 -38.62 | current_profile_false_positive |
| 011070 | Stage2-Actionable correct, but Green/4B timing needs guard | MFE30 +24.69 / MAE180 -42.98 | current_profile_4B_too_late |

Answers to required stress-test questions: Stage2 bonus is useful for SK hynix and LG Innotek, but excessive for Simmtech/Daeduck without conversion evidence. Yellow threshold 75 is not the main issue; the issue is component contamination before the score reaches Yellow. Green threshold/revision guard is appropriate and should remain strict. Price-only blowoff guard is appropriate but C06 needs a specific fast-MFE high-MAE watch. Full 4B non-price requirement is appropriate for Samsung's qualification-delay case. Hard 4C is not proposed because Samsung later had partial HBM progress and the other cases are not hard thesis breaks.

## 14. Stage2 / Yellow / Green Comparison

- SK hynix: Stage3-Green at entry is not late because customer, capacity, and margin bridge were all visible; `green_lateness_ratio = 0.0` in this single-trigger representation.
- LG Innotek: Stage2-Actionable should not become Stage3-Green without margin/revision confirmation despite fast MFE.
- Simmtech/Daeduck: Stage2 should be capped or blocked because the evidence is substrate/memory-utilization proxy rather than customer allocation.
- Samsung: Stage4B/watch should override HBM beta until qualification and supply agreement improve.

## 15. 4B Local vs Full-window Timing Audit

| case | local / full-window observation | timing verdict |
|---|---|---|
| 005930 | event-driven qualification risk at entry; no prior Stage2 pair in this MD | event_driven_4B_watch_no_prior_stage2_pair |
| 011070 | fast +24.69% local MFE, then -42.98% 180D MAE | price_only_local_4B_watch_needed_after_fast_MFE |
| 000660 | peak on 2024-07-11 after strong structural entry, then -41.77% drawdown after peak | 4B overlay needed after peak, not at entry |
| 222800 / 353200 | no meaningful upside before drawdown | Stage2 proxy block, not 4B timing problem |

## 16. 4C Protection Audit

No representative row is promoted to hard Stage4C. Samsung contains qualification-failure evidence, but because later partial HBM approvals existed and the company-wide thesis did not collapse immediately, the safer calibration label is `Stage4B / thesis_break_watch_only`. For Simmtech and Daeduck, the protection mechanism is Stage2 proxy blocking, not hard 4C.

## 17. Sector-Specific Rule Candidate

`L2_C06_HBM_CUSTOMER_QUALIFICATION_CAPACITY_MARGIN_BRIDGE_GATE`

For L2 AI/semiconductor, Stage2-Actionable can be assigned to HBM/customer capacity evidence only if at least one of the following exists: named customer qualification/supply, capacity allocation/backlog, ASP/mix revision, or visible margin bridge. If evidence is only an HBM/DDR5/FC-BGA analogy, cap at Stage1/Watch or low Stage2.

## 18. Canonical-Archetype Rule Candidate

`C06_CUSTOMER_QUALIFICATION_AND_CAPACITY_ALLOCATION_GATE`

C06 should split three paths:

1. **Signed/visible HBM customer allocation** → Stage3 eligible when margin/revision bridge exists.
2. **Customer qualification delay** → Stage4B or Stage2 block until qualification improves.
3. **HBM-adjacent substrate/proxy narrative** → Stage2 cap unless revenue/customer conversion is explicit.

## 19. Before / After Backtest Comparison

|profile_id|hypothesis|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|verdict|
|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_proxy|current calibrated profile as-is|5|17.09|-23.01|17.09|-38.24|3/5|mixed; still admits HBM-adjacent proxy false positives|
|P0b e2r_2_0_reference|legacy baseline, weaker bridge guards|5|17.09|-23.01|17.09|-38.24|4/5|too permissive for substrate/proxy narratives|
|P1 sector shadow|L2 AI/HBM customer-signoff and revenue bridge gate|3|26.49|-22.6|26.49|-32.32|1/3|better separates signed HBM capacity from unqualified memory beta|
|P2 canonical C06 shadow|signed customer qualification + capacity allocation + margin bridge required for Stage3|2|32.23|-22.43|32.23|-30.8|0/2, but one high-MAE watch|best precision; LG Innotek remains Stage2+4B watch not Green|
|P3 counterexample guard|block HBM-adjacent proxy rows without customer/revenue confirmation|2|32.23|-22.43|32.23|-30.8|0/2 promoted; 3 blocked|reduces Simmtech/Daeduck/Samsung false positives|


## 20. Score-Return Alignment Matrix

| symbol | score alignment | explanation |
|---|---|---|
| 000660 | aligned | high customer quality + capacity + margin bridge matched high MFE |
| 005930 | misaligned before guard | HBM narrative without qualification led to downside-heavy path |
| 222800 | misaligned | memory-utilization proxy lacked conversion and produced severe MAE |
| 353200 | misaligned | FC-BGA/DDR5 ASP story lacked C06 customer bridge and failed |
| 011070 | mixed | customer qualification produced MFE, but absent margin/revision led to high MAE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed_C06_hbm_customer_capacity_allocation_set | 2 | 3 | 1 | 0 | 5 | 0 | 5 | 5 | 4 | L2_C06_HBM_CUSTOMER_QUALIFICATION_CAPACITY_MARGIN_BRIDGE_GATE | C06_CUSTOMER_QUALIFICATION_AND_CAPACITY_ALLOCATION_GATE | C06 rows 17 -> expected 22 after acceptance; need-to-30 8 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - hbm_customer_qualification_false_positive
  - hbm_adjacent_substrate_proxy_false_stage2
  - fast_mfe_high_mae_local_4b_watch
new_axis_proposed:
  - C06_CUSTOMER_QUALIFICATION_AND_CAPACITY_ALLOCATION_GATE
  - C06_HBM_ADJACENT_SUBSTRATE_PROXY_CAP
  - C06_FAST_MFE_HIGH_MAE_4B_WATCH
existing_axis_strengthened:
  - stage2_required_bridge
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_C06_HBM_CUSTOMER_QUALIFICATION_CAPACITY_MARGIN_BRIDGE_GATE
canonical_archetype_rule_candidate: C06_CUSTOMER_QUALIFICATION_AND_CAPACITY_ALLOCATION_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger-level 30D/90D/180D OHLC path, entry close, clean 180D share-count window, positive/counterexample balance, C06 canonical compression. Not validated: production scoring code, live candidates, intraday event timestamps, brokerage API, current investment recommendation, 1Y/2Y windows.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_customer_qualification_capacity_allocation_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Require explicit customer qualification / capacity allocation / margin bridge before C06 Stage3","blocks 3 false positives while preserving SK hynix and LG Innotek as positive/Stage2-actionable signals","C06_R2L108_000660_T1|C06_R2L108_005930_T1|C06_R2L108_222800_T1|C06_R2L108_353200_T1|C06_R2L108_011070_T1",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C06_hbm_adjacent_substrate_proxy_cap,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"HBM/DDR5/FC-BGA analogy alone is capped at Stage2 unless customer/revenue bridge is explicit","Simmtech and Daeduck paths show severe MAE when proxy narrative lacks conversion","C06_R2L108_222800_T1|C06_R2L108_353200_T1",2,2,2,medium,canonical_shadow_only,"proxy decontamination for C06"
shadow_weight,C06_fast_mfe_high_mae_4b_watch,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Fast MFE without margin/revision confirmation should add local 4B watch, not full Green","LG Innotek reached +24.69% MFE but -42.98% MAE in 180D","C06_R2L108_011070_T1",1,1,0,low,guardrail_shadow_only,"4B watch overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C06_R2L108_000660_HBM3E_CUSTOMER_CAPACITY_SOLDOUT_20240425","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_SUPPLIER_CUSTOMER_CAPACITY_ALLOCATION_POSITIVE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C06_R2L108_000660_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM customer/capacity evidence had both non-price customer quality and margin bridge; later drawdown argues for 4B overlay after peak, not for blocking Stage3-Green at entry."}
{"row_type":"trigger","trigger_id":"C06_R2L108_000660_T1","case_id":"C06_R2L108_000660_HBM3E_CUSTOMER_CAPACITY_SOLDOUT_20240425","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_SUPPLIER_CUSTOMER_CAPACITY_ALLOCATION_POSITIVE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage3-Green","trigger_date":"2024-04-25","evidence_available_at_that_date":"Q1 2024 profit recovery, Nvidia-linked HBM leadership, AI HBM capacity sold-out / capacity allocation visibility.","evidence_source":"https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","durable_customer_confirmation","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":177800.0,"MFE_30D_pct":21.48,"MFE_90D_pct":39.76,"MFE_180D_pct":39.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.95,"MAE_90D_pct":-14.74,"MAE_180D_pct":-18.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500.0,"drawdown_after_peak_pct":-41.77,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_customer_capacity_margin_bridge_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|2024-04-26|177800.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L108_000660_HBM3E_CUSTOMER_CAPACITY_SOLDOUT_20240425","trigger_id":"C06_R2L108_000660_T1","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":65,"backlog_visibility_score":82,"margin_bridge_score":90,"revision_score":92,"relative_strength_score":82,"customer_quality_score":95,"policy_or_regulatory_score":5,"valuation_repricing_score":70,"execution_risk_score":20,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":86,"margin_bridge_score":92,"revision_score":92,"relative_strength_score":82,"customer_quality_score":98,"policy_or_regulatory_score":5,"valuation_repricing_score":70,"execution_risk_score":20,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["capacity_or_shipment_score","customer_quality_score","margin_bridge_score"],"component_delta_explanation":"C06 shadow profile separates signed customer qualification/capacity allocation/margin bridge from HBM-adjacent proxy narratives.","MFE_90D_pct":39.76,"MAE_90D_pct":-14.74,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C06_R2L108_005930_HBM3E_NVIDIA_QUALIFICATION_FAIL_20240524","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_DELAY_4B_COUNTEREXAMPLE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_R2L108_005930_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C06 should not promote unqualified HBM capacity narratives to Stage3 without customer qualification and supply allocation; this is an event-driven 4B watch rather than price-only 4B."}
{"row_type":"trigger","trigger_id":"C06_R2L108_005930_T1","case_id":"C06_R2L108_005930_HBM3E_NVIDIA_QUALIFICATION_FAIL_20240524","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_DELAY_4B_COUNTEREXAMPLE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage4B","trigger_date":"2024-05-24","evidence_available_at_that_date":"Reuters-reported HBM3/HBM3E Nvidia test failure from heat/power issues; HBM narrative existed but customer qualification was not signed-off.","evidence_source":"https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","explicit_event_cap","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["qualification_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-27","entry_price":77200.0,"MFE_30D_pct":14.77,"MFE_90D_pct":15.03,"MFE_180D_pct":15.03,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.79,"MAE_90D_pct":-22.93,"MAE_180D_pct":-35.36,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800.0,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"event_driven_4B_watch_no_prior_stage2_pair","four_b_evidence_type":["contract_delay","explicit_event_cap","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"hbm_customer_qualification_delay_4b_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|2024-05-27|77200.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L108_005930_HBM3E_NVIDIA_QUALIFICATION_FAIL_20240524","trigger_id":"C06_R2L108_005930_T1","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":55,"revision_score":65,"relative_strength_score":55,"customer_quality_score":35,"policy_or_regulatory_score":5,"valuation_repricing_score":55,"execution_risk_score":75,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":55,"revision_score":65,"relative_strength_score":55,"customer_quality_score":20,"policy_or_regulatory_score":5,"valuation_repricing_score":55,"execution_risk_score":88,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":53,"stage_label_after":"Stage4B","changed_components":["customer_quality_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C06 shadow profile separates signed customer qualification/capacity allocation/margin bridge from HBM-adjacent proxy narratives.","MFE_90D_pct":15.03,"MAE_90D_pct":-22.93,"score_return_alignment_label":"misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_R2L108_222800_MEMORY_SUBSTRATE_UTILIZATION_RECOVERY_FALSE_STAGE2_20240111","symbol":"222800","company_name":"심텍","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_DDR5_CUSTOMER_UTILIZATION_PROXY_FALSE_STAGE2","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"C06_R2L108_222800_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The 30D/90D/180D path shows that HBM/DDR5 utilization proxy can be a falling-knife false positive when customer order conversion and margin bridge are not explicit."}
{"row_type":"trigger","trigger_id":"C06_R2L108_222800_T1","case_id":"C06_R2L108_222800_MEMORY_SUBSTRATE_UTILIZATION_RECOVERY_FALSE_STAGE2_20240111","symbol":"222800","company_name":"심텍","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_DDR5_CUSTOMER_UTILIZATION_PROXY_FALSE_STAGE2","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage2","trigger_date":"2024-01-11","evidence_available_at_that_date":"Simmtech report expected DRAM capacity utilization recovery from 1Q24 driven by HBM/DDR5, but the evidence was customer-utilization proxy rather than confirmed order/margin bridge.","evidence_source":"https://www.simmtech.com/upload/media/file/638406815140413547.pdf","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv","profile_path":"atlas/symbol_profiles/222/222800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-12","entry_price":38100.0,"MFE_30D_pct":3.41,"MFE_90D_pct":3.41,"MFE_180D_pct":3.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.28,"MAE_90D_pct":-27.3,"MAE_180D_pct":-55.64,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-12","peak_price":39400.0,"drawdown_after_peak_pct":-57.11,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"memory_substrate_utilization_proxy_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|222800|2024-01-12|38100.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L108_222800_MEMORY_SUBSTRATE_UTILIZATION_RECOVERY_FALSE_STAGE2_20240111","trigger_id":"C06_R2L108_222800_T1","symbol":"222800","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":40,"revision_score":60,"relative_strength_score":45,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":70,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":30,"revision_score":60,"relative_strength_score":45,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":80,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":52,"stage_label_after":"Stage1/Watch","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile separates signed customer qualification/capacity allocation/margin bridge from HBM-adjacent proxy narratives.","MFE_90D_pct":3.41,"MAE_90D_pct":-27.3,"score_return_alignment_label":"misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_R2L108_353200_FCBGA_DDR5_ASP_RECOVERY_FALSE_STAGE2_20240111","symbol":"353200","company_name":"대덕전자","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_SUBSTRATE_ASP_RECOVERY_FALSE_STAGE2","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_R2L108_353200_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AI/HBM-adjacent substrate ASP narratives need explicit customer backlog or revenue conversion; otherwise Stage2 should be capped."}
{"row_type":"trigger","trigger_id":"C06_R2L108_353200_T1","case_id":"C06_R2L108_353200_FCBGA_DDR5_ASP_RECOVERY_FALSE_STAGE2_20240111","symbol":"353200","company_name":"대덕전자","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_SUBSTRATE_ASP_RECOVERY_FALSE_STAGE2","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage2","trigger_date":"2024-01-11","evidence_available_at_that_date":"Daeduck Electronics report cited DDR5 penetration, high-value substrate mix and FC-BGA normalization, but HBM-specific customer allocation was not enough to protect the price path.","evidence_source":"https://www.daeduck.com/file/board/651.do","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv","profile_path":"atlas/symbol_profiles/353/353200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-12","entry_price":27550.0,"MFE_30D_pct":2.54,"MFE_90D_pct":2.54,"MFE_180D_pct":2.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.51,"MAE_90D_pct":-19.96,"MAE_180D_pct":-38.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-12","peak_price":28250.0,"drawdown_after_peak_pct":-40.14,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"fcbga_ddr5_asp_recovery_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|353200|2024-01-12|27550.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L108_353200_FCBGA_DDR5_ASP_RECOVERY_FALSE_STAGE2_20240111","trigger_id":"C06_R2L108_353200_T1","symbol":"353200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":40,"margin_bridge_score":45,"revision_score":58,"relative_strength_score":42,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":68,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":65,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":40,"margin_bridge_score":30,"revision_score":58,"relative_strength_score":42,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":80,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":51,"stage_label_after":"Stage1/Watch","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile separates signed customer qualification/capacity allocation/margin bridge from HBM-adjacent proxy narratives.","MFE_90D_pct":2.54,"MAE_90D_pct":-19.96,"score_return_alignment_label":"misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_R2L108_011070_FCBGA_INTEL_NVIDIA_CUSTOMER_QUALIFICATION_HIGH_MAE_20240612","symbol":"011070","company_name":"LG이노텍","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_AI_CHIP_SUBSTRATE_CUSTOMER_QUALIFICATION_HIGH_MAE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C06_R2L108_011070_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_high_mae","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Customer qualification deserved Stage2-Actionable, but not full Stage3 without margin/revision confirmation; fast MFE followed by deep MAE supports a canonical C06 high-MAE 4B watch."}
{"row_type":"trigger","trigger_id":"C06_R2L108_011070_T1","case_id":"C06_R2L108_011070_FCBGA_INTEL_NVIDIA_CUSTOMER_QUALIFICATION_HIGH_MAE_20240612","symbol":"011070","company_name":"LG이노텍","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_AI_CHIP_SUBSTRATE_CUSTOMER_QUALIFICATION_HIGH_MAE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-12","evidence_available_at_that_date":"BusinessKorea reported LG Innotek FC-BGA supply to Intel/NVIDIA; FC-BGA was framed as an HBM-like bottleneck of the substrate market.","evidence_source":"https://www.businesskorea.co.kr/news/articleView.html?idxno=218911","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011070/2024.csv","profile_path":"atlas/symbol_profiles/011/011070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-13","entry_price":245000.0,"MFE_30D_pct":24.69,"MFE_90D_pct":24.69,"MFE_180D_pct":24.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.24,"MAE_90D_pct":-30.12,"MAE_180D_pct":-42.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":305500.0,"drawdown_after_peak_pct":-54.27,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_watch_needed_after_fast_MFE","four_b_evidence_type":["price_only_local_peak","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_adjacent_customer_qualification_high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|011070|2024-06-13|245000.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L108_011070_FCBGA_INTEL_NVIDIA_CUSTOMER_QUALIFICATION_HIGH_MAE_20240612","trigger_id":"C06_R2L108_011070_T1","symbol":"011070","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":45,"margin_bridge_score":50,"revision_score":55,"relative_strength_score":75,"customer_quality_score":80,"policy_or_regulatory_score":5,"valuation_repricing_score":70,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":45,"margin_bridge_score":42,"revision_score":55,"relative_strength_score":75,"customer_quality_score":82,"policy_or_regulatory_score":5,"valuation_repricing_score":62,"execution_risk_score":68,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable + 4B Watch","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile separates signed customer qualification/capacity allocation/margin bridge from HBM-adjacent proxy narratives.","MFE_90D_pct":24.69,"MAE_90D_pct":-30.12,"score_return_alignment_label":"mixed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R2","loop":"108","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["hbm_customer_qualification_false_positive","hbm_adjacent_substrate_proxy_false_stage2","fast_mfe_high_mae_local_4b_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

```yaml
completed_round: R2
completed_loop: 108
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows / C06 rows 17 need-to-30 13
next_recommended_archetypes:
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
  - C11_BATTERY_ORDERBOOK_RERATING
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- Stock-web manifest max date: 2026-02-20.
- Price basis: raw unadjusted marcap OHLC; no adjusted-price repair was applied.
- All price rows are historical calibration rows only and are not live investment recommendations.
- Evidence source URLs are recorded in the evidence source map and in machine-readable trigger rows.

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
