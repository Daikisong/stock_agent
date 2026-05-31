# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R2
scheduled_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION
output_file = e2r_stock_web_v12_residual_round_R2_loop_12_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

## 1. Current Calibrated Profile Assumption

Current default proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Applied global axes assumed active:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove the global Stage2 bonus or the global Green threshold. It tests a narrower residual: in C06, HBM headlines can look structurally similar, but the market path diverges sharply depending on whether customer qualification and allocation are confirmed.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R2
loop = 12
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION
loop_objective = coverage_gap_fill | counterexample_mining | green_strictness_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
```

R2 is restricted to AI / semiconductor / electronics. The selected canonical archetype is C06 because previous local R2 loop outputs already covered C08 semi test socket customer quality and C10 memory recovery equipment cycle. This run avoids those repeated canonical routes and focuses on memory producer HBM customer capacity.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check:

- R2 calibration report has `79` representative triggers and `32` unique cases, with accepted cumulative axes for Stage2, Yellow, Green, 4B, and 4C. This implies enough global evidence exists; this loop must add C06-specific residual value rather than repeat global axes.
- Local v12 MDs already include R2 Loop 10 C08 and R2 Loop 11 C10. This loop chooses C06 to avoid rematerializing those case tables.

Duplicate control:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided except Samsung explicit new 4C trigger family
same_symbol_new_trigger_family = allowed_with_reuse_reason
new_symbol_count = 2
new_trigger_family_count = 4
minimum_new_independent_case_ratio = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema basis:

```text
d = date
o = open
h = high
l = low
c = close
v = volume
a = amount
mc = market_cap
s = shares
m = market
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

The file uses tradable shards only for backtest metrics. Raw shards are not used for weight calibration.

## 5. Historical Eligibility Gate

All four representative triggers pass the historical eligibility gate:

```text
trigger_date_past = true
entry_date_exists_in_tradable_shard = true
forward_180_trading_days_available = true
positive_ohlcv = true
MFE_MAE_30_90_180_computed = true
corporate_action_contaminated_180D_window = false
```

For both selected symbols, profile corporate-action candidates are historical and outside the tested 2024 180D windows.

## 6. Canonical Archetype Compression Map

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
  -> HBM capacity expansion
  -> customer qualification / customer allocation visibility
  -> HBM shipment mix and margin bridge
  -> revision confirmation
  -> Green-size-up guard if customer proof is absent
  -> 4C thesis break if qualification failure appears
```

Compression principle: C06 should not be a generic “HBM theme” bucket. It should distinguish three routes:

1. **Confirmed capacity + customer allocation**: actionable positive.
2. **Broad HBM catch-up optimism**: Yellow or Stage2-watch, not Green.
3. **Customer qualification failure**: 4C thesis-break route even if price initially bounces.

## 7. Case Selection Summary

| case_id | symbol | company | role | entry_date | entry_price | MFE90 | MAE90 | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---:|---|
| R2L12_C06_SKHYNIX_20240424_CAPACITY_HBM_STAGE2 | 000660 | SK하이닉스 | structural_success / positive | 2024-04-24 | 179800 | 38.21 | -15.68 | current_profile_correct |
| R2L12_C06_SKHYNIX_20240613_GREEN_HIGH_MAE | 000660 | SK하이닉스 | high_mae_success / positive | 2024-06-13 | 222000 | 11.94 | -31.71 | current_profile_too_late |
| R2L12_C06_SAMSUNG_20240320_HBM_OPTIMISM_FALSE_GREEN | 005930 | 삼성전자 | false_positive_green / counterexample | 2024-03-20 | 76900 | 15.21 | -4.42 | current_profile_false_positive |
| R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C | 005930 | 삼성전자 | 4C_success / counterexample | 2024-05-24 | 75900 | 16.73 | -21.08 | current_profile_4C_too_late |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
```

The positive side is represented by SK hynix’s HBM capacity and customer-allocation route. The counterexample side is represented by Samsung’s HBM catch-up / qualification gap. This is deliberately not a “memory sector always wins” study; it is a discrimination study.

## 9. Evidence Source Map

| case_id | evidence family | stage role | source note |
|---|---|---|---|
| R2L12_C06_SKHYNIX_20240424_CAPACITY_HBM_STAGE2 | HBM capacity expansion tied to demand | Stage2-Actionable | Reuters reported SK hynix DRAM/HBM investment and demand-driven capacity need. |
| R2L12_C06_SKHYNIX_20240613_GREEN_HIGH_MAE | mature HBM relative strength and customer allocation | Stage3-Green / 4B stress | stock-web price path shows Green worked but high-MAE/4B risk emerged quickly. |
| R2L12_C06_SAMSUNG_20240320_HBM_OPTIMISM_FALSE_GREEN | generic HBM catch-up optimism | false-Green counterexample | customer qualification was not yet confirmed. |
| R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C | qualification failure / customer test failure | 4C thesis break | Reuters reported Samsung HBM chips had not passed Nvidia testing; Samsung disputed specific failure claims but described ongoing optimization. |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | profile caveat |
|---:|---|---|---|---|
| 000660 | SK하이닉스 | atlas/symbol_profiles/000/000660.json | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | clean_180D_window; profile corporate-action candidates are historical 1998-2003 only |
| 000660 | SK하이닉스 | atlas/symbol_profiles/000/000660.json | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | clean_180D_window; profile corporate-action candidates are historical 1998-2003 only |
| 005930 | 삼성전자 | atlas/symbol_profiles/005/005930.json | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | clean_180D_window; profile corporate-action candidates 1996/1997/2018 only |
| 005930 | 삼성전자 | atlas/symbol_profiles/005/005930.json | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | clean_180D_window; profile corporate-action candidates 1996/1997/2018 only |


## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TRG_R2L12_C06_SKHYNIX_20240424 | 000660 | Stage2-Actionable | 2024-04-24 | 179800 | 16.24 | 38.21 | 38.21 | -6.01 | -15.68 | -15.68 | 2024-07-11 | 248500 | current_profile_correct |
| TRG_R2L12_C06_SKHYNIX_20240613 | 000660 | Stage3-Green | 2024-06-13 | 222000 | 11.94 | 11.94 | 11.94 | -14.86 | -31.71 | -31.71 | 2024-07-11 | 248500 | current_profile_too_late |
| TRG_R2L12_C06_SAMSUNG_20240320 | 005930 | Stage3-Yellow/Weak-Green | 2024-03-20 | 76900 | 11.83 | 15.21 | 15.21 | -2.34 | -4.42 | -35.11 | 2024-07-08 | 88600 | current_profile_false_positive |
| TRG_R2L12_C06_SAMSUNG_20240524 | 005930 | Stage4C-thesis-break | 2024-05-24 | 75900 | 14.76 | 16.73 | 16.73 | -3.16 | -21.08 | -34.26 | 2024-07-08 | 88600 | current_profile_4C_too_late |


## 12. Trigger-Level OHLC Backtest Tables

Backtest formula:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
```

Interpretation:

- SK hynix 2024-04-24: clean Stage2-Actionable; the 90D MFE/MAE asymmetry supports positive C06 scoring.
- SK hynix 2024-06-13: still positive, but the Green entry was already deep into the move; high 90D MAE argues for a Green-size-up cap near local peaks.
- Samsung 2024-03-20: broad HBM optimism produced limited upside and severe later drawdown; it is a false-Green counterexample.
- Samsung 2024-05-24: explicit qualification failure was a 4C route. The first 30D bounce was noise; 90D/180D path validates thesis-break protection.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected label | actual path | verdict |
|---|---|---|---|
| SKHYNIX_20240424 | Stage2-Actionable / Yellow-high | positive MFE with manageable early MAE | current_profile_correct |
| SKHYNIX_20240613 | Stage3-Green | positive but late/high-MAE | current_profile_too_late |
| SAMSUNG_20240320 | Yellow / weak-Green risk | modest MFE, severe 180D MAE | current_profile_false_positive |
| SAMSUNG_20240524 | 4C thesis-break if routed | bounce then collapse | current_profile_4C_too_late |

Answers to required stress-test questions:

1. Current profile correctly keeps confirmed SK hynix capacity as positive Stage2/Yellow.
2. Current profile is too permissive if Samsung HBM optimism receives Green without customer qualification.
3. Stage2 bonus is appropriate only when capacity/customer evidence is present.
4. Yellow 75 is acceptable for Samsung optimism but should not leak into Green.
5. Green 87 and revision 55 remain necessary but insufficient; C06 needs customer qualification.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate, but C06 should treat supply-allocation exhaustion and customer delay as non-price 4B candidates.
8. Hard 4C routing should be faster when a customer qualification failure appears.

## 14. Stage2 / Yellow / Green Comparison

```text
SKHYNIX Stage2-Actionable entry = 2024-04-24 / 179800
SKHYNIX Stage3-Green comparison entry = 2024-06-13 / 222000
full observed peak after Stage2 = 2024-07-11 / 248500
```

```text
green_lateness_ratio = (222000 - 179800) / (248500 - 179800) = 0.614
```

Interpretation: Green captured only the final third of the Stage2-to-peak move and then suffered high MAE. The Green label is not wrong, but size-up should be capped unless the customer-allocation bridge continues improving.

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| SKHYNIX_20240613 | positioning_overheat + valuation_blowoff | 1.00 | 1.00 | good_full_window_4B_timing_if_non_price_overheat_exists |
| SAMSUNG_20240320 | price_only local peak | 1.00 | 1.00 | price_only_local_4B_without_customer_quality |
| SAMSUNG_20240524 | qualification break | n/a | n/a | not_4B_qualification_break_routes_to_4C |

The useful rule is not “sell every HBM winner near highs.” The useful rule is: if C06 customer allocation is confirmed, a 4B overlay needs non-price overheat evidence; if customer qualification fails, it is not 4B at all—it is 4C.

## 16. 4C Protection Audit

Samsung 2024-05-24 is the clean 4C row:

```text
entry_price = 75900
MFE_30D = +14.76
MAE_90D = -21.08
MAE_180D = -34.26
four_c_protection_label = hard_4c_success_after_noise
```

A first-month bounce did not invalidate the 4C thesis-break signal. The protection worked at 90D/180D horizon.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The residual is not broad enough for all L2 AI/semiconductor. Test sockets, equipment cycles, and memory producers have different evidence bridges. This is narrower than sector level.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
new_axis_proposed = C06_hbm_customer_qualification_green_gate
```

Rule candidate:

```text
For C06, Stage3-Green requires either:
  1. confirmed customer qualification / customer shipment acceptance, or
  2. explicit HBM capacity allocation visibility tied to AI GPU customer demand, or
  3. financial revision that directly names HBM mix, HBM margin, or HBM shipment growth.

Generic HBM catch-up language, capex intent, or broad AI-memory optimism can reach Stage2/Yellow, but cannot reach Green alone.

Qualification failure, customer test failure, or repeated customer shipment delay routes to 4C thesis-break watch even if the first 30D price path bounces.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | current_profile_error_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current default | 4 | 20.78 | -18.22 | 20.78 | -29.21 | 0.25 | 3 | too loose for generic HBM optimism; too slow for qualification break |
| P0b e2r_2_0_baseline_reference | rollback | 4 | 20.78 | -18.22 | 20.78 | -29.21 | 0.50 | 3 | even more likely to over-promote broad HBM headlines |
| P1 sector_specific_candidate_profile | L2 sector | 4 | 20.78 | -18.22 | 20.78 | -29.21 | 0.25 | 2 | useful but too broad; C06-specific gate is cleaner |
| P2 canonical_archetype_candidate_profile | C06 only | 4 | 22.51 | -19.24 | 22.51 | -29.19 | 0.00 | 1 | best alignment: SKH positive retained, Samsung false-Green blocked |
| P3 counterexample_guard_profile | C06 guard | 4 | 16.73 | -27.67 | 16.73 | -34.69 | 0.00 | 1 | best for protection, but may under-rank confirmed SKH capacity |


## 20. Score-Return Alignment Matrix

| case_id | before score | before label | after score | after label | alignment |
|---|---:|---|---:|---|---|
| SKHYNIX_20240424 | 84 | Stage3-Yellow | 86 | Stage3-Yellow-high | retained positive, not forced Green |
| SKHYNIX_20240613 | 89 | Stage3-Green | 84 | Stage3-Yellow-highMAE/Green-size-cap | Green size-up reduced after late entry |
| SAMSUNG_20240320 | 82 | Stage3-Yellow / weak-Green risk | 72 | Stage2-Actionable | false-Green blocked |
| SAMSUNG_20240524 | 58 | Stage2-watch / 4C-watch | 49 | 4C-thesis-break | thesis break strengthened |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION | 2 | 2 | 1 | 1 | 4 | 2 | 4 | 4 | 3 | false | true | C06 now has both positive and qualification-failure counterexample coverage; still needs non-Korean memory holdout later. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 2
reused_case_ids: R2L12_C06_SKHYNIX_20240613_GREEN_HIGH_MAE | R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C
new_symbol_count: 2
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage3_green_revision_min | stage3_cross_evidence_green_buffer | hard_4c_thesis_break_routes_to_4c | price_only_blowoff_blocks_positive_stage
residual_error_types_found: generic_HBM_optimism_false_green | late_4C_customer_qualification_failure | Green_size_up_high_MAE
new_axis_proposed: C06_hbm_customer_qualification_green_gate
existing_axis_strengthened: stage3_green_revision_min | stage3_cross_evidence_green_buffer | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable OHLC rows for 000660 and 005930
- profile corporate-action caveats for selected windows
- 30D / 90D / 180D MFE and MAE
- current calibrated profile stress test
- C06 positive / counterexample balance
- 4B local vs full-window split
- hard 4C thesis-break timing
```

Not validated:

```text
- current live candidates
- investment recommendation
- brokerage execution
- stock_agent production scoring code
- exact analyst-consensus EPS revision import
- future post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,hbm_customer_qualification_green_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,Confirmed customer qualification/capacity allocation separates SK hynix winners from Samsung HBM catch-up false-Green,Blocks false Green and routes qualification failure to 4C,TRG_R2L12_C06_SKHYNIX_20240424|TRG_R2L12_C06_SAMSUNG_20240320|TRG_R2L12_C06_SAMSUNG_20240524,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R2L12_C06_SKHYNIX_20240424_CAPACITY_HBM_STAGE2","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R2L12_C06_SKHYNIX_20240424","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Cleanest C06 positive: capacity expansion plus customer/HBM demand bridge. Stage2 works; Green should wait for customer-allocation visibility."}
{"row_type":"case","case_id":"R2L12_C06_SKHYNIX_20240613_GREEN_HIGH_MAE","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG_R2L12_C06_SKHYNIX_20240613","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family: Stage3-Green lateness and 4B proximity audit, not the 2024-04-24 Stage2 row","independent_evidence_weight":0.5,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Valid C06 winner but Green arrived after roughly 61% of the Stage2-to-peak upside, and the later 90D MAE was severe."}
{"row_type":"case","case_id":"R2L12_C06_SAMSUNG_20240320_HBM_OPTIMISM_FALSE_GREEN","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_R2L12_C06_SAMSUNG_20240320","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"qualification_break_or_false_green_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C06 should not treat broad HBM catch-up optimism as Green without customer qualification. The eventual 180D MAE dominates the modest upside."}
{"row_type":"case","case_id":"R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R2L12_C06_SAMSUNG_20240524","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family: explicit qualification failure after earlier HBM optimism row","independent_evidence_weight":0.5,"score_price_alignment":"qualification_break_or_false_green_alignment","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"This row supports hard 4C routing for customer qualification failure: the 30D bounce did not invalidate the thesis break; 90D/180D protection was valuable."}
{"row_type":"trigger","trigger_id":"TRG_R2L12_C06_SKHYNIX_20240424","case_id":"R2L12_C06_SKHYNIX_20240424_CAPACITY_HBM_STAGE2","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","sector":"AI·반도체·전자부품","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","evidence_available_at_that_date":"SK hynix announced a new DRAM/HBM production-base investment while Reuters described high demand for HBM as a driver of the capacity decision.","evidence_source":"Reuters, 2024-04-24; stock-web OHLC row atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-24","entry_price":179800,"MFE_30D_pct":16.24,"MFE_90D_pct":38.21,"MFE_180D_pct":38.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.01,"MAE_90D_pct":-15.68,"MAE_180D_pct":-15.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-39.0,"green_lateness_ratio":"not_applicable: representative is Stage2-Actionable; Green comparison row is SKHYNIX_20240613","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidates are historical 1998-2003 only","same_entry_group_id":"R2L12_C06_SKHYNIX_20240424_CAPACITY_HBM_STAGE2::2024-04-24::179800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L12_C06_SKHYNIX_20240613","case_id":"R2L12_C06_SKHYNIX_20240613_GREEN_HIGH_MAE","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","sector":"AI·반도체·전자부품","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage3-Green","trigger_date":"2024-06-13","evidence_available_at_that_date":"HBM customer capacity narrative had matured into visible relative strength and capacity allocation; however the stock was already close to a local full-window peak.","evidence_source":"Reuters/market evidence proxy; stock-web OHLC row atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","durable_customer_confirmation","multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-13","entry_price":222000,"MFE_30D_pct":11.94,"MFE_90D_pct":11.94,"MFE_180D_pct":11.94,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.86,"MAE_90D_pct":-31.71,"MAE_180D_pct":-31.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-39.0,"green_lateness_ratio":0.614,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_exists","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidates are historical 1998-2003 only","same_entry_group_id":"R2L12_C06_SKHYNIX_20240613_GREEN_HIGH_MAE::2024-06-13::222000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family: Stage3-Green lateness and 4B proximity audit, not the 2024-04-24 Stage2 row","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L12_C06_SAMSUNG_20240320","case_id":"R2L12_C06_SAMSUNG_20240320_HBM_OPTIMISM_FALSE_GREEN","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","sector":"AI·반도체·전자부품","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage3-Yellow/Weak-Green","trigger_date":"2024-03-20","evidence_available_at_that_date":"Market treated Samsung as an HBM catch-up candidate, but named customer qualification and confirmed high-volume AI GPU supply were not yet proven.","evidence_source":"Reuters/market evidence proxy; later Reuters HBM qualification failure report; stock-web OHLC row atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["qualification_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-20","entry_price":76900,"MFE_30D_pct":11.83,"MFE_90D_pct":15.21,"MFE_180D_pct":15.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.34,"MAE_90D_pct":-4.42,"MAE_180D_pct":-35.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":88600,"drawdown_after_peak_pct":-43.68,"green_lateness_ratio":"not_applicable: no confirmed C06 Green; this row tests false-Green risk","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_without_customer_quality","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_success_if_qualification_failure_routed","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidates 1996/1997/2018 only","same_entry_group_id":"R2L12_C06_SAMSUNG_20240320_HBM_OPTIMISM_FALSE_GREEN::2024-03-20::76900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L12_C06_SAMSUNG_20240524","case_id":"R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_CAPACITY_ALLOCATION","sector":"AI·반도체·전자부품","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4C-thesis-break","trigger_date":"2024-05-24","evidence_available_at_that_date":"Reuters reported Samsung HBM chips had not passed Nvidia tests due to heat/power issues; Samsung disputed details but acknowledged customer-optimization work. That is a C06 qualification-break event, not merely price weakness.","evidence_source":"Reuters, 2024-05-24; stock-web OHLC row atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["qualification_failure","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-24","entry_price":75900,"MFE_30D_pct":14.76,"MFE_90D_pct":16.73,"MFE_180D_pct":16.73,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.16,"MAE_90D_pct":-21.08,"MAE_180D_pct":-34.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":88600,"drawdown_after_peak_pct":-43.68,"green_lateness_ratio":"not_applicable: 4C row","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_qualification_break_routes_to_4C","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_after_noise","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidates 1996/1997/2018 only","same_entry_group_id":"R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C::2024-05-24::75900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family: explicit qualification failure after earlier HBM optimism row","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C06_SKHYNIX_20240424_CAPACITY_HBM_STAGE2","trigger_id":"TRG_R2L12_C06_SKHYNIX_20240424","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":3,"hbm_customer_qualification_score":3},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":3,"hbm_customer_qualification_score":3,"customer_allocation_visibility_score":3,"green_size_up_guard":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["hbm_customer_qualification_score","customer_allocation_visibility_score","green_size_up_guard","qualification_failure_guard"],"component_delta_explanation":"C06 should distinguish confirmed HBM customer qualification/capacity allocation from generic HBM optimism; confirmed customer allocation may promote, qualification failure routes to 4C and Green-size-up is capped.","MFE_90D_pct":38.21,"MAE_90D_pct":-15.68,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C06_SKHYNIX_20240613_GREEN_HIGH_MAE","trigger_id":"TRG_R2L12_C06_SKHYNIX_20240613","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":3,"hbm_customer_qualification_score":3},"weighted_score_before":89,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":3,"hbm_customer_qualification_score":3,"positioning_overheat_score":3,"green_size_up_guard":-2,"customer_allocation_visibility_score":3},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["hbm_customer_qualification_score","customer_allocation_visibility_score","green_size_up_guard","qualification_failure_guard"],"component_delta_explanation":"C06 should distinguish confirmed HBM customer qualification/capacity allocation from generic HBM optimism; confirmed customer allocation may promote, qualification failure routes to 4C and Green-size-up is capped.","MFE_90D_pct":11.94,"MAE_90D_pct":-31.71,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C06_SAMSUNG_20240320_HBM_OPTIMISM_FALSE_GREEN","trigger_id":"TRG_R2L12_C06_SAMSUNG_20240320","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":2,"hbm_customer_qualification_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":2,"hbm_customer_qualification_score":-2,"customer_allocation_visibility_score":-2,"green_size_up_guard":-3},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["hbm_customer_qualification_score","customer_allocation_visibility_score","green_size_up_guard","qualification_failure_guard"],"component_delta_explanation":"C06 should distinguish confirmed HBM customer qualification/capacity allocation from generic HBM optimism; confirmed customer allocation may promote, qualification failure routes to 4C and Green-size-up is capped.","MFE_90D_pct":15.21,"MAE_90D_pct":-4.42,"score_return_alignment_label":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C","trigger_id":"TRG_R2L12_C06_SAMSUNG_20240524","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":1,"hbm_customer_qualification_score":-3},"weighted_score_before":58,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":1,"hbm_customer_qualification_score":-3,"qualification_failure_guard":-5,"hard_4c_route_score":3,"green_size_up_guard":-5},"weighted_score_after":49,"stage_label_after":"Stage2-watch","changed_components":["hbm_customer_qualification_score","customer_allocation_visibility_score","green_size_up_guard","qualification_failure_guard"],"component_delta_explanation":"C06 should distinguish confirmed HBM customer qualification/capacity allocation from generic HBM optimism; confirmed customer allocation may promote, qualification failure routes to 4C and Green-size-up is capped.","MFE_90D_pct":16.73,"MAE_90D_pct":-21.08,"score_return_alignment_label":"counterexample_alignment","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":4,"reused_case_count":2,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","stage3_cross_evidence_green_buffer","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["generic_HBM_optimism_false_green","late_4C_customer_qualification_failure","Green_size_up_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 12
next_round = R3
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source files used:

- `atlas/manifest.json`: max_date, row counts, shard roots, raw/unadjusted notes.
- `atlas/schema.json`: OHLC column definitions, MFE/MAE formula, calibration usable rules.
- `atlas/symbol_profiles/000/000660.json`: SK hynix profile, year availability, row status, corporate-action caveat.
- `atlas/symbol_profiles/005/005930.json`: Samsung Electronics profile, year availability, row status, corporate-action caveat.
- `atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv`: SK hynix representative price rows.
- `atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv`: Samsung representative price rows.

External evidence sources used for event interpretation:

- Reuters, 2024-04-24: SK hynix DRAM/HBM investment and HBM demand context.
- Reuters, 2024-05-24: Samsung HBM chips had not yet passed Nvidia tests due to reported heat/power issues; Samsung disputed the specific failure claims and described ongoing customer optimization.
- Reuters, 2024-11-04: Nvidia request to SK hynix to accelerate HBM4 supply, reinforcing customer-pull interpretation.


