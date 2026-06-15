# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_122_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 122
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_RERATING_4B_WATCH
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

This is the corrected valid run after a duplicate loop121 re-materialization path was discarded. C07 reached the local 30-row stability threshold at loop121, so this loop moves to the next Priority 0 gap: C06.

This loop adds 3 new independent C06 rows and moves C06 from static 21 rows to projected 24 rows. It still needs 6 rows to reach the 30-row stability threshold.

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

C06 is the HBM memory customer/capacity archetype. Memory beta is the tide; the actual edge is whether HBM customer qualification, capacity lock, mix, ASP, margin, revision and FCF arrive together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C06 static rows | 21 |
| C06 need to 30 | 9 |
| C06 need to 50 | 29 |
| C06 investigation point | 고객 CAPA, HBM mix, ASP/FCF 전환, cycle 반례 |
| local previous C06 rows in this session | 0 |
| this loop projected rows | 24 |

Selected symbols avoid local C07/C08/C09/C01 stabilized repetition. The accidentally re-created C07 loop121 materialization path is not counted as new evidence.

| symbol | company | status |
|---|---|---|
| 000660 | SK하이닉스 | new local C06 anchor positive, reduced weight for mega-cap/static-overlap risk |
| 005930 | 삼성전자 | new local C06 large-cap counterexample, reduced weight for mega-cap/static-overlap risk |
| 353200 | 대덕전자 | new local C06 package/substrate counterexample |

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
| 000660 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |
| 005930 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |
| 353200 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- SK하이닉스 has old corporate-action candidates before the selected 2024 window.
- 삼성전자 has old corporate-action candidates before the selected 2024 window.
- 대덕전자 has zero corporate-action candidates.
- Mega-cap memory anchor rows are useful, but they are not allowed to overcount C06 independent evidence.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_RERATING_4B_WATCH | C06 | HBM customer/capacity/mix route can work, but memory-cycle 4B audit is required |
| HBM_MEMORY_CUSTOMER_CAPACITY_LAG_YIELD_MIX_WITHOUT_CONFIRMED_REVISION_BRIDGE | C06 | memory beta without customer/mix/revision bridge is false-positive risk |
| HBM_PACKAGE_SUBSTRATE_CAPACITY_PREMIUM_WITHOUT_CUSTOMER_CAPA_FCF_BRIDGE | C06 | package/substrate capacity premium needs customer lock and FCF bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C06_SKHYNIX_000660_2024_03_06_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_RERATING_4B | 000660 | SK하이닉스 | 4B_overlay_success | positive | HBM customer/mix route produced 52.55% 90D MFE |
| C06_SAMSUNG_005930_2024_03_06_HBM_MEMORY_LAGGING_MIX_CUSTOMER_CAPACITY_FAIL | 005930 | 삼성전자 | failed_rerating | counterexample | memory/HBM narrative had MFE but later severe drawdown without confirmed bridge |
| C06_DAEDUCK_353200_2024_03_06_HBM_PACKAGE_SUBSTRATE_CAPACITY_PREMIUM_FAIL | 353200 | 대덕전자 | failed_rerating | counterexample | HBM package/substrate premium had mid-teens MFE and severe MAE |

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
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 000660 | source_proxy_only | HBM customer capacity / mix / ASP / FCF route | required before promotion |
| 005930 | source_proxy_only | memory/HBM capacity narrative but customer/mix/revision bridge lagged | required; useful as counterexample |
| 353200 | source_proxy_only | package/substrate capacity premium but customer-capa/FCF bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000660 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json |
| 005930 | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | atlas/symbol_profiles/005/005930.json |
| 353200 | atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv | atlas/symbol_profiles/353/353200.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SKHYNIX_000660_2024_03_06_STAGE2A_HBM_MEMORY_CUSTOMER_CAPACITY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 162900 | HBM customer capacity / mix / ASP / FCF |
| SAMSUNG_005930_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_MEMORY_CAPACITY_LAG | Stage2 | 2024-03-06 | 2024-03-06 | 72900 | memory beta without confirmed HBM mix bridge |
| DAEDUCK_353200_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PACKAGE_SUBSTRATE_CAPACITY | Stage2 | 2024-03-06 | 2024-03-06 | 24100 | package/substrate capacity premium without customer/FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 000660 | 2024-03-06 | 162900 | 17.50 | -5.40 | 52.55 | -5.40 | 52.55 | -11.17 | 2024-07-11 | 248500 | -41.77 |
| 005930 | 2024-03-06 | 72900 | 17.28 | -1.65 | 21.81 | -1.65 | 21.81 | -31.55 | 2024-07-11 | 88800 | -43.81 |
| 353200 | 2024-03-06 | 24100 | 16.39 | -7.05 | 16.39 | -13.28 | 16.39 | -40.66 | 2024-04-02 | 28050 | -49.02 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 000660 | Stage2A/Yellow/Green-risk; memory cycle 4B after rerating | high MFE and later drawdown | current_profile_4B_too_late |
| 005930 | Stage2 risk if generic memory beta is over-credited | MFE then large full-window MAE | current_profile_false_positive |
| 353200 | Stage2 risk if package/substrate capacity premium is over-credited | mid-teens MFE and severe MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C06 interpretation:

- Stage2A can work when HBM customer qualification, capacity lock, ASP/mix, revision, margin and FCF align.
- Yellow/Green require non-price customer and mix evidence.
- Generic memory recovery beta or package/substrate capacity premium without bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 000660 | 0.66 | 1.00 | HBM memory mix/capacity rerating | full-window memory-cycle 4B audit required |
| 005930 | 0.82 | 1.00 | memory beta / bridge absent | not Stage3 without HBM customer/mix bridge |
| 353200 | 0.86 | 1.00 | package/substrate capacity premium / bridge absent | not Stage3 without customer-capa/FCF bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 000660 | thesis_break_watch_only | not hard 4C, but 4B cap needed after memory-cycle rerating |
| 005930 | hard_4c_late | customer qualification/mix/revision bridge absence should have capped Stage2 earlier |
| 353200 | hard_4c_late | customer capacity lock and FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, HBM memory capacity should promote Stage2A only when customer qualification, capacity lock, HBM mix, ASP bridge, revision, margin or FCF is visible. Generic memory recovery beta or substrate capacity premium without that bridge should not become Yellow/Green.

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
  AND (customer_qualification OR capacity_lock OR hbm_mix_bridge OR asp_bridge OR confirmed_revision OR fcf_conversion)

if memory_beta_only and customer_mix_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if substrate_capacity_premium and customer_capa_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C06_memory_cycle_4B_audit = true

if MFE_90D > 15 and MAE_180D < -30 and bridge_absent:
    classify_as C06_memory_capacity_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 30.25 | -6.78 | 30.25 | -27.79 | 2 | useful but C06 bridge too loose |
| P0b calibrated rollback | rollback | 3 | 30.25 | -6.78 | 30.25 | -27.79 | 2 | over-credits memory beta/capacity premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 52.55 | -5.4 | 52.55 | -11.17 | 0 | better after customer/mix bridge gate |
| P2 canonical_archetype_candidate_profile | C06 | 1 promoted + 2 guard | 52.55 | -5.4 | 52.55 | -11.17 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C06 guard | 1 promoted + 2 guard | 52.55 | -5.4 | 52.55 | -11.17 | 0 | adds memory beta/capacity false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 000660 | Stage2A aligned; 4B cycle audit needed | current_profile_4B_too_late |
| 005930 | Stage2 false positive if customer/mix bridge not enforced | current_profile_false_positive |
| 353200 | Stage2 false positive if customer-capa/FCF bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed C06 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> projected 24; still need 6 to reach 30 |

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
new_axis_proposed: C06_hbm_customer_capacity_mix_bridge_required|C06_memory_cycle_4B_audit|C06_memory_capacity_false_positive_guardrail
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
- Avoids local C07/C08/C09 stabilized repetition.
- Keeps 000660/005930 with reduced weights because they are mega-cap memory anchors and may overlap static corpus.
- Keeps 353200 as clean package/substrate counterexample.
- Discards the accidental duplicate loop121 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop121 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_hbm_customer_capacity_mix_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"005930/353200 show memory beta or package capacity premium can fail without customer/mix/FCF bridge while 000660 works only as Stage2A with 4B audit","blocks two false positives while preserving 000660 Stage2A","SKHYNIX_000660_2024_03_06_STAGE2A_HBM_MEMORY_CUSTOMER_CAPACITY|SAMSUNG_005930_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_MEMORY_CAPACITY_LAG|DAEDUCK_353200_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PACKAGE_SUBSTRATE_CAPACITY",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C06_memory_cycle_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"000660 HBM memory mix rerating needed full-window 4B audit after MFE and drawdown","adds 4B audit after C06 memory-cycle MFE without converting price-only peaks into Green","SKHYNIX_000660_2024_03_06_STAGE2A_HBM_MEMORY_CUSTOMER_CAPACITY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C06_memory_capacity_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"005930/353200 had MFE but high MAE after memory beta/capacity premium without customer/mix/FCF bridge","requires confirmed customer capacity, HBM mix, ASP/revision, margin and FCF bridge before Stage2/Yellow promotion","SAMSUNG_005930_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_MEMORY_CAPACITY_LAG|DAEDUCK_353200_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PACKAGE_SUBSTRATE_CAPACITY",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C06_SKHYNIX_000660_2024_03_06_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_RERATING_4B","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"122","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"SKHYNIX_000660_2024_03_06_STAGE2A_HBM_MEMORY_CUSTOMER_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; HBM memory anchor may overlap static corpus, independent weight reduced","independent_evidence_weight":0.9,"score_price_alignment":"HBM customer capacity, mix, ASP and memory FCF route captured 50%+ MFE, but later peak-to-drawdown required C06 4B cycle audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol; core memory anchor positive"}
{"row_type":"case","case_id":"C06_SAMSUNG_005930_2024_03_06_HBM_MEMORY_LAGGING_MIX_CUSTOMER_CAPACITY_FAIL","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"122","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_LAG_YIELD_MIX_WITHOUT_CONFIRMED_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"SAMSUNG_005930_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_MEMORY_CAPACITY_LAG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; mega-cap memory anchor, independent weight reduced","independent_evidence_weight":0.9,"score_price_alignment":"generic memory/HBM capacity narrative produced a tradable MFE but later severe MAE when customer qualification, HBM mix, and revision bridge lagged","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol; useful large-cap counterexample separating memory beta from confirmed HBM mix/customer bridge"}
{"row_type":"case","case_id":"C06_DAEDUCK_353200_2024_03_06_HBM_PACKAGE_SUBSTRATE_CAPACITY_PREMIUM_FAIL","symbol":"353200","company_name":"대덕전자","round":"R2","loop":"122","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PACKAGE_SUBSTRATE_CAPACITY_PREMIUM_WITHOUT_CUSTOMER_CAPA_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DAEDUCK_353200_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PACKAGE_SUBSTRATE_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"package/substrate HBM capacity premium produced only mid-teens MFE and then severe full-window MAE without customer/capa/FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol; clean profile with zero corporate-action candidates"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SKHYNIX_000660_2024_03_06_STAGE2A_HBM_MEMORY_CUSTOMER_CAPACITY","case_id":"C06_SKHYNIX_000660_2024_03_06_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_RERATING_4B","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"122","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_RERATING_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":162900.0,"evidence_available_at_that_date":"source_proxy_only: HBM customer capacity, high-value memory mix, ASP/revision expectation, AI accelerator demand and FCF route visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_customer_capacity","hbm_mix","asp_bridge","ai_memory_demand","relative_strength"],"stage3_evidence_fields":["customer_capacity_bridge_partial","revision_bridge_partial","margin_bridge_partial","fcf_conversion_pending"],"stage4b_evidence_fields":["memory_cycle_peak_watch","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.5,"MFE_90D_pct":52.55,"MFE_180D_pct":52.55,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.4,"MAE_90D_pct":-5.4,"MAE_180D_pct":-11.17,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500.0,"drawdown_after_peak_pct":-41.77,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.66,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_memory_customer_capacity_rerating_worked_but_full_window_memory_cycle_peak_requires_C06_4B_audit","four_b_evidence_type":["valuation_rerating","memory_cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["mega_cap_anchor_overlap_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_000660_2024_03_06_162900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; memory anchor overlap","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SAMSUNG_005930_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_MEMORY_CAPACITY_LAG","case_id":"C06_SAMSUNG_005930_2024_03_06_HBM_MEMORY_LAGGING_MIX_CUSTOMER_CAPACITY_FAIL","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"122","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_LAG_YIELD_MIX_WITHOUT_CONFIRMED_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":72900.0,"evidence_available_at_that_date":"source_proxy_only: memory recovery and HBM capacity narrative visible, but confirmed HBM customer qualification, mix/ASP bridge, revision and FCF conversion lagged; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_recovery_beta","hbm_capacity_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["memory_beta_peak","customer_mix_bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["hbm_customer_qualification_lag","mix_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.28,"MFE_90D_pct":21.81,"MFE_180D_pct":21.81,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-31.55,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800.0,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_beta_not_C06_stage3_without_confirmed_hbm_customer_mix_revision_bridge","four_b_evidence_type":["memory_beta_peak","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mfe_then_high_mae_hbm_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["mega_cap_anchor_overlap_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_005930_2024_03_06_72900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; memory anchor overlap","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DAEDUCK_353200_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PACKAGE_SUBSTRATE_CAPACITY","case_id":"C06_DAEDUCK_353200_2024_03_06_HBM_PACKAGE_SUBSTRATE_CAPACITY_PREMIUM_FAIL","symbol":"353200","company_name":"대덕전자","round":"R2","loop":"122","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PACKAGE_SUBSTRATE_CAPACITY_PREMIUM_WITHOUT_CUSTOMER_CAPA_FCF_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":24100.0,"evidence_available_at_that_date":"source_proxy_only: HBM/package substrate capacity premium visible, but confirmed customer capacity lock, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_package_substrate_capacity_premium","memory_cycle_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","customer_capacity_bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["customer_capa_lock_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv","profile_path":"atlas/symbol_profiles/353/353200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.39,"MFE_90D_pct":16.39,"MFE_180D_pct":16.39,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.05,"MAE_90D_pct":-13.28,"MAE_180D_pct":-40.66,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":28050.0,"drawdown_after_peak_pct":-49.02,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_package_substrate_capacity_premium_not_C06_stage3_without_customer_capa_margin_fcf_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_customer_capacity_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_353200_2024_03_06_24100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_SKHYNIX_000660_2024_03_06_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_RERATING_4B","trigger_id":"SKHYNIX_000660_2024_03_06_STAGE2A_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":9,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow/Green-risk with memory-cycle 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":9,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable with mandatory C06 4B cycle audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM customer/mix route worked, but full Green needs realized customer capacity, ASP/margin, revision and FCF conversion plus cycle audit.","MFE_90D_pct":52.55,"MAE_90D_pct":-5.4,"score_return_alignment_label":"positive_high_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_SAMSUNG_005930_2024_03_06_HBM_MEMORY_LAGGING_MIX_CUSTOMER_CAPACITY_FAIL","trigger_id":"SAMSUNG_005930_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_MEMORY_CAPACITY_LAG","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive / memory beta risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage1/4C-watch, not C06 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Generic memory beta without confirmed HBM customer/mix/revision bridge produced MFE but high full-window MAE.","MFE_90D_pct":21.81,"MAE_90D_pct":-1.65,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_DAEDUCK_353200_2024_03_06_HBM_PACKAGE_SUBSTRATE_CAPACITY_PREMIUM_FAIL","trigger_id":"DAEDUCK_353200_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PACKAGE_SUBSTRATE_CAPACITY","symbol":"353200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / substrate capacity premium risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage1/4C-watch, not C06 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM substrate/capacity premium without customer capacity lock, margin and FCF bridge produced mid-teens MFE and severe MAE.","MFE_90D_pct":16.39,"MAE_90D_pct":-13.28,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"122","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 122
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX
```

If this loop is accepted, C06 moves to projected 24 rows and still needs 6 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C06 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/000/000660.json
  - atlas/symbol_profiles/005/005930.json
  - atlas/symbol_profiles/353/353200.json
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R2_loop_121_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
