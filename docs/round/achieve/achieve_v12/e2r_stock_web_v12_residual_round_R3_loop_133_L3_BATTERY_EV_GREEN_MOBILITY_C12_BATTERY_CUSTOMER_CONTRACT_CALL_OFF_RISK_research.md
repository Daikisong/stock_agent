# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_133_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round: R3
selected_loop: 133
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CATHODE_CUSTOMER_CALL_OFF_ASP_MARGIN_FCF_HARD_4C
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_timing_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after the accidental C11 loop132 re-materialization path was discarded. C11 reached the local 30-row stability threshold at loop132, so this run moves to the next Priority 0 gap: C12.

This loop adds 3 new independent C12 rows and moves C12 from static 27 rows to projected 30 rows. The 30-row minimum stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C12:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C12 -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

C12 is the battery customer contract / call-off risk archetype. A contract is a reservation; call-off, utilization, ASP/mix, margin, working capital, and FCF decide whether the reservation turns into cash or evaporates like a booked table with no diner.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C12 static rows | 27 |
| C12 need to 30 | 3 |
| C12 need to 50 | 23 |
| C12 investigation point | 고객 계약과 call-off/demand risk, AMPC/IRA와 분리 |
| local previous C12 rows in this session | 0 |
| this loop projected rows | 30 |

Selected symbols avoid local C14/C11 threshold-completion symbols:

```text
C14 local: 247540, 066970, 373220, 003670, 361610, 006400, 278280, 020150, 011790
C11 local: 137400, 222080, 372170, 299030, 382840, 382480, 104460
```

Selected C12 symbols:

| symbol | company | status |
|---|---|---|
| 005070 | 코스모신소재 | new local C12 hard 4C contract/call-off case |
| 121600 | 나노신소재 | new local C12 4B-to-4C call-off case |
| 078600 | 대주전자재료 | new local C12 overblock counterexample |

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
| 005070 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 121600 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_but_2024_share_count_drift_watch | true, weight 0.85 |
| 078600 / 2024-03-06 | true | true | clean_180D_window | true, weight 1.00 |

Corporate-action notes:

- 코스모신소재 has old corporate-action candidates before the selected 2024 window.
- 나노신소재 has an old corporate-action candidate in 2015 and a 2024 share-count drift watch after April, so its independent evidence weight is reduced.
- 대주전자재료 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| CATHODE_CUSTOMER_CALL_OFF_ASP_MARGIN_FCF_HARD_4C | C12 | customer/backlog narrative should become hard 4C when call-off, ASP/margin and FCF pressure are visible |
| CNT_CUSTOMER_CONTRACT_OPTIONALITY_4B_BOUNCE_THEN_CALL_OFF_4C | C12 | customer optionality can create 4B bounce but must roll into 4C if margin/FCF bridge fails |
| SILICON_ANODE_CUSTOMER_OPTIONALITY_PREMATURE_CALL_OFF_4C_OVERBLOCK | C12 | blanket hard 4C can overblock silicon-anode optionality before confirmed call-off/margin break |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C12_COSMOAM_005070_2024_03_06_CATHODE_CUSTOMER_CALL_OFF_MARGIN_FCF_HARD_4C | 005070 | 코스모신소재 | hard_4c_protection_success | positive_protection | small MFE and severe 180D MAE after contract/call-off risk |
| C12_NANO_121600_2024_03_06_CNT_CUSTOMER_CONTRACT_CALL_OFF_4B_TO_4C | 121600 | 나노신소재 | 4B_to_4C_protection_success | positive_protection | 4B bounce then severe MAE as margin/FCF bridge failed |
| C12_DAEJOO_078600_2024_03_06_SILICON_ANODE_CONTRACT_OPTIONALITY_OVERBLOCK | 078600 | 대주전자재료 | timing_overblock_counterexample | counterexample | huge MFE and shallow entry-MAE, so blanket hard 4C would overblock |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_protection_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| overblock_counterexample_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 005070 | source_proxy_only | customer contract/backlog narrative but call-off, ASP/margin, FCF pressure | required before promotion |
| 121600 | source_proxy_only | CNT/customer optionality but call-off/margin/FCF risk unresolved | required before promotion |
| 078600 | source_proxy_only | silicon-anode customer optionality and qualification route without confirmed call-off break | required; useful as overblock counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 005070 | atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv | atlas/symbol_profiles/005/005070.json |
| 121600 | atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv | atlas/symbol_profiles/121/121600.json |
| 078600 | atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv | atlas/symbol_profiles/078/078600.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| COSMOAM_005070_2024_03_06_STAGE4C_CUSTOMER_CALL_OFF_ASP_MARGIN_RISK | Stage4C | 2024-03-06 | 2024-03-06 | 168400 | customer call-off / ASP / FCF hard 4C |
| NANO_121600_2024_03_06_STAGE4C_CUSTOMER_CONTRACT_OPTIONALITY_CALL_OFF_RISK | Stage4C | 2024-03-06 | 2024-03-06 | 125700 | customer optionality 4B then call-off/margin 4C |
| DAEJOO_078600_2024_03_06_STAGE2_CUSTOMER_OPTIONALITY_OVERBLOCK_COUNTEREXAMPLE | Stage2 | 2024-03-06 | 2024-03-06 | 78100 | silicon-anode customer optionality overblock exception |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 005070 | 2024-03-06 | 168400 | 7.48 | -12.71 | 7.48 | -21.91 | 7.48 | -63.18 | 2024-03-15 | 181000 | -65.75 |
| 121600 | 2024-03-06 | 125700 | 20.60 | -7.72 | 20.60 | -20.29 | 20.60 | -52.82 | 2024-03-19 | 151600 | -60.88 |
| 078600 | 2024-03-06 | 78100 | 30.60 | -2.18 | 109.22 | -2.18 | 109.22 | -5.76 | 2024-06-12 | 163400 | -54.96 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 005070 | Stage2 risk if contract/backlog is over-credited | hard 4C protection worked | current_profile_4C_too_late |
| 121600 | Stage2/4B bounce risk if customer optionality is over-credited | 4B-to-4C protection worked | current_profile_4C_too_late_after_4B_bounce |
| 078600 | hard 4C risk if all customer contract risk is treated as call-off | overblock counterexample | current_profile_overblocks_if_all_customer_contract_risk_treated_as_call_off |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C12 interpretation:

- Contract/backlog language should not become Yellow/Green unless customer call-off adjusted demand, margin, working capital and FCF conversion are visible.
- A 4B bounce can exist inside a bad call-off setup.
- Silicon-anode/customer-qualification optionality needs an overblock exception until call-off or margin break is confirmed.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 005070 | 0.93 | 1.00 | minor rebound / call-off hard 4C | 4B bounce should not override hard 4C |
| 121600 | 0.83 | 1.00 | 4B bounce / call-off risk | 4B must roll into C12 4C after bridge failure |
| 078600 | 0.48 | 1.00 | silicon-anode optionality / large 4B | hard 4C overblocks until call-off break confirmed |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 005070 | hard_4c_success | call-off/ASP/margin pressure protected against later collapse |
| 121600 | hard_4c_success_after_bounce | 4B bounce could not overcome margin/FCF failure |
| 078600 | overblock_counterexample_then_delayed_4c_watch | immediate blanket hard 4C would have been too early |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, customer contract and backlog language should promote Stage2A only when it is connected to customer call-off adjusted demand, margin, working-capital quality, revision and FCF conversion. If call-off/ASP/margin pressure is visible, the name should route to hard 4C even after a temporary 4B bounce. If customer-qualification optionality remains intact and no call-off break is confirmed, apply a Stage2-watch overblock exception.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
confidence = medium
```

Candidate C12 rule:

```text
C12_customer_contract_calloff_hard_4c =
  customer_contract_or_backlog_route
  AND (customer_call_off OR inventory_pressure OR asp_mix_pressure OR margin_revision_down OR working_capital_stress OR fcf_deterioration)

if customer_contract_backlog and C12_customer_contract_calloff_hard_4c:
    cap_stage = Stage4C
    do_not_allow_Stage3_Yellow_or_Green = true

if customer_optionality and qualification_route and not confirmed_call_off_or_margin_break:
    classify_as C12_overblock_counterexample
    cap_stage = Stage2-watch_not_Green
    require delayed_4C_recheck

if MFE_90D > 15 and MAE_180D < -40 and hard_4c_evidence:
    strengthen C12_4B_to_4C_timing_guard

if MFE_90D > 50 and MAE_90D > -10 and optionality_route:
    add C12_customer_optionality_overblock_exception

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / overblock | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 45.77 | -14.79 | 45.77 | -40.59 | 1 overblock | useful but C12 timing/exception rule needed |
| P0b calibrated rollback | rollback | 3 | 45.77 | -14.79 | 45.77 | -40.59 | 1 overblock | over-credits contract beta or overblocks optionality |
| P1 sector_specific_candidate_profile | L3 | 2 hard 4C + 1 overblock exception | 14.04 | -21.1 | 14.04 | -58.0 | 0 | better after call-off/margin bridge gate |
| P2 canonical_archetype_candidate_profile | C12 | 2 hard 4C + 1 overblock exception | 14.04 | -21.1 | 14.04 | -58.0 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C12 guard | 2 hard 4C + 1 overblock exception | 14.04 | -21.1 | 14.04 | -58.0 | 0 | adds optionality overblock guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 005070 | hard 4C aligned; contract/backlog beta failed | current_profile_4C_too_late |
| 121600 | hard 4C aligned after 4B bounce | current_profile_4C_too_late_after_4B_bounce |
| 078600 | hard 4C overblock if optionality treated as call-off | current_profile_overblocks_if_all_customer_contract_risk_treated_as_call_off |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive protection | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | mixed C12 fine ids | 2 | 1 | 2 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 27 -> projected 30; reaches minimum stability threshold |

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
  - current_profile_4C_too_late
  - current_profile_overblocks_if_all_customer_contract_risk_treated_as_call_off
new_axis_proposed: C12_customer_contract_calloff_hard_4c|C12_4B_to_4C_timing_guard|C12_customer_optionality_overblock_exception|share_count_drift_independent_weight_reduction
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
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
- Uses C12 Priority 0 coverage gap.
- Avoids local C14/C11 threshold-completion symbols.
- Keeps 121600 with reduced weight because of 2024 share-count drift watch.
- Treats 078600 as overblock counterexample, not Green promotion.
- Discards the accidental duplicate C11 loop132 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated C11 loop132 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C12_customer_contract_calloff_hard_4c,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"005070/121600 show customer contract/backlog optionality can fail when call-off, ASP/margin and FCF pressure persist","caps Stage2/Yellow after weak or temporary bounce and preserves hard 4C protection","COSMOAM_005070_2024_03_06_STAGE4C_CUSTOMER_CALL_OFF_ASP_MARGIN_RISK|NANO_121600_2024_03_06_STAGE4C_CUSTOMER_CONTRACT_OPTIONALITY_CALL_OFF_RISK",2,2,0,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C12_4B_to_4C_timing_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"121600 had a 20.60% MFE before -52.82% 180D MAE, so 4B bounce must roll into 4C if margin/FCF bridge fails","prevents 4B bounces from becoming Green without call-off-adjusted margin and FCF proof","NANO_121600_2024_03_06_STAGE4C_CUSTOMER_CONTRACT_OPTIONALITY_CALL_OFF_RISK",1,1,0,medium,canonical_shadow_only,"4B/4C timing calibration"
shadow_weight,C12_customer_optionality_overblock_exception,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"078600 shows blanket call-off hard 4C can overblock silicon-anode customer optionality when no confirmed call-off/margin break exists","keeps 078600 as Stage2-watch with delayed 4C recheck rather than immediate hard 4C","DAEJOO_078600_2024_03_06_STAGE2_CUSTOMER_OPTIONALITY_OVERBLOCK_COUNTEREXAMPLE",1,1,1,medium,canonical_shadow_only,"overblock guardrail"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"121600 has 2024 share-count drift during the validation window","keeps row usable but lowers independent evidence weight","NANO_121600_2024_03_06_STAGE4C_CUSTOMER_CONTRACT_OPTIONALITY_CALL_OFF_RISK",1,1,0,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C12_COSMOAM_005070_2024_03_06_CATHODE_CUSTOMER_CALL_OFF_MARGIN_FCF_HARD_4C","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"133","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CALL_OFF_ASP_MARGIN_FCF_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"COSMOAM_005070_2024_03_06_STAGE4C_CUSTOMER_CALL_OFF_ASP_MARGIN_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window","independent_evidence_weight":0.95,"score_price_alignment":"cathode/customer call-off and ASP/margin risk allowed only a 7.48% MFE before -63.18% 180D MAE, so hard 4C protection was directionally correct","current_profile_verdict":"current_profile_4C_too_late_if_contract_backlog_overcredited","price_source":"Songdaiki/stock-web","notes":"new local C12 symbol after C11 threshold completion; old profile caveat outside 2024 window"}
{"row_type":"case","case_id":"C12_NANO_121600_2024_03_06_CNT_CUSTOMER_CONTRACT_CALL_OFF_4B_TO_4C","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"133","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CNT_CUSTOMER_CONTRACT_OPTIONALITY_4B_BOUNCE_THEN_CALL_OFF_4C","case_type":"4B_to_4C_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"NANO_121600_2024_03_06_STAGE4C_CUSTOMER_CONTRACT_OPTIONALITY_CALL_OFF_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate in 2015 only; 2024 share-count drift watch visible after April, independent weight reduced","independent_evidence_weight":0.85,"score_price_alignment":"CNT/customer optionality produced a 20.60% bounce, then -52.82% 180D MAE; 4B timing had to roll into C12 hard 4C when margin/FCF bridge failed","current_profile_verdict":"current_profile_4C_too_late_after_4B_bounce","price_source":"Songdaiki/stock-web","notes":"new local C12 symbol; share-count drift watch from April row count change lowers evidence weight"}
{"row_type":"case","case_id":"C12_DAEJOO_078600_2024_03_06_SILICON_ANODE_CONTRACT_OPTIONALITY_OVERBLOCK","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"133","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SILICON_ANODE_CUSTOMER_OPTIONALITY_PREMATURE_CALL_OFF_4C_OVERBLOCK","case_type":"timing_overblock_counterexample","positive_or_counterexample":"counterexample","best_trigger":"DAEJOO_078600_2024_03_06_STAGE2_CUSTOMER_OPTIONALITY_OVERBLOCK_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"silicon-anode/customer optionality had a 109.22% MFE and only -5.76% 180D MAE from entry, so blanket C12 hard 4C would overblock without confirmed call-off/margin break","current_profile_verdict":"current_profile_overblocks_if_all_customer_contract_risk_treated_as_call_off","price_source":"Songdaiki/stock-web","notes":"clean profile with zero corporate-action candidates; overblock guard"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"COSMOAM_005070_2024_03_06_STAGE4C_CUSTOMER_CALL_OFF_ASP_MARGIN_RISK","case_id":"C12_COSMOAM_005070_2024_03_06_CATHODE_CUSTOMER_CALL_OFF_MARGIN_FCF_HARD_4C","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"133","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CALL_OFF_ASP_MARGIN_FCF_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":168400.0,"evidence_available_at_that_date":"source_proxy_only: battery material customer contract risk, call-off/inventory pressure, ASP/mix pressure and FCF risk visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["customer_contract_backlog_narrative","cathode_recovery_beta"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["minor_bounce","valuation_peak_watch"],"stage4c_evidence_fields":["customer_call_off_risk","asp_mix_pressure","inventory_pressure","margin_fcf_pressure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.48,"MFE_90D_pct":7.48,"MFE_180D_pct":7.48,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-12.71,"MAE_90D_pct":-21.91,"MAE_180D_pct":-63.18,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":181000.0,"drawdown_after_peak_pct":-65.75,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"minor 4B bounce should not override customer call-off / ASP / FCF hard 4C","four_b_evidence_type":["minor_rebound","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protection_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late_if_contract_backlog_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C12_005070_2024_03_06_168400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"NANO_121600_2024_03_06_STAGE4C_CUSTOMER_CONTRACT_OPTIONALITY_CALL_OFF_RISK","case_id":"C12_NANO_121600_2024_03_06_CNT_CUSTOMER_CONTRACT_CALL_OFF_4B_TO_4C","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"133","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CNT_CUSTOMER_CONTRACT_OPTIONALITY_4B_BOUNCE_THEN_CALL_OFF_4C","sector":"battery / EV / green mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":125700.0,"evidence_available_at_that_date":"source_proxy_only: CNT/customer contract optionality and EV battery material growth visible, but customer call-off/margin/FCF risk not resolved; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["customer_contract_optionality","CNT_growth_beta","relative_strength_bounce"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["4b_bounce_after_contract_optionality","valuation_peak_watch"],"stage4c_evidence_fields":["customer_call_off_risk","margin_bridge_absent","fcf_bridge_absent","share_count_drift_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv","profile_path":"atlas/symbol_profiles/121/121600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.6,"MFE_90D_pct":20.6,"MFE_180D_pct":20.6,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.72,"MAE_90D_pct":-20.29,"MAE_180D_pct":-52.82,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-19","peak_price":151600.0,"drawdown_after_peak_pct":-60.88,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.83,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"4B bounce was real but should have rolled into C12 call-off/margin/FCF 4C when bridge failed","four_b_evidence_type":["4b_bounce","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success_after_bounce","trigger_outcome_label":"positive_protection_mfe_then_high_mae","current_profile_verdict":"current_profile_4C_too_late_after_4B_bounce","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_watch_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_but_2024_share_count_drift_watch","same_entry_group_id":"C12_121600_2024_03_06_125700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window; 2024 share-count drift watch","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DAEJOO_078600_2024_03_06_STAGE2_CUSTOMER_OPTIONALITY_OVERBLOCK_COUNTEREXAMPLE","case_id":"C12_DAEJOO_078600_2024_03_06_SILICON_ANODE_CONTRACT_OPTIONALITY_OVERBLOCK","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"133","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SILICON_ANODE_CUSTOMER_OPTIONALITY_PREMATURE_CALL_OFF_4C_OVERBLOCK","sector":"battery / EV / green mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":78100.0,"evidence_available_at_that_date":"source_proxy_only: silicon-anode customer optionality and customer qualification route visible; no confirmed call-off/margin break yet; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["silicon_anode_customer_optionality","customer_qualification_route","relative_strength_reversal"],"stage3_evidence_fields":["customer_optional_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["large_4b_timing_rally","valuation_peak_watch"],"stage4c_evidence_fields":["call_off_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv","profile_path":"atlas/symbol_profiles/078/078600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.6,"MFE_90D_pct":109.22,"MFE_180D_pct":109.22,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.18,"MAE_90D_pct":-2.18,"MAE_180D_pct":-5.76,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":163400.0,"drawdown_after_peak_pct":-54.96,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.48,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"blanket C12 hard 4C would overblock silicon-anode customer optionality; delayed 4C/4B blowoff audit still required","four_b_evidence_type":["large_4b_rally","customer_optionality"],"four_c_protection_label":"overblock_counterexample_then_delayed_4c_watch","trigger_outcome_label":"counterexample_overbroad_calloff_4c","current_profile_verdict":"current_profile_overblocks_if_all_customer_contract_risk_treated_as_call_off","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_078600_2024_03_06_78100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C12_COSMOAM_005070_2024_03_06_CATHODE_CUSTOMER_CALL_OFF_MARGIN_FCF_HARD_4C","trigger_id":"COSMOAM_005070_2024_03_06_STAGE4C_CUSTOMER_CALL_OFF_ASP_MARGIN_RISK","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":59,"stage_label_before":"Stage2 bounce risk / late C12 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":41,"stage_label_after":"Stage4C hard customer call-off / margin risk","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Contract/backlog narrative lacked call-off-adjusted margin and FCF bridge.","MFE_90D_pct":7.48,"MAE_90D_pct":-21.91,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_4C_too_late_if_contract_backlog_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C12_NANO_121600_2024_03_06_CNT_CUSTOMER_CONTRACT_CALL_OFF_4B_TO_4C","trigger_id":"NANO_121600_2024_03_06_STAGE4C_CUSTOMER_CONTRACT_OPTIONALITY_CALL_OFF_RISK","symbol":"121600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 bounce risk / late C12 4C","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Stage4C call-off/margin watch after 4B bounce","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Customer optionality produced bounce, but margin/FCF and share-count quality failed to sustain rerating.","MFE_90D_pct":20.6,"MAE_90D_pct":-20.29,"score_return_alignment_label":"hard_4c_after_4b_bounce","current_profile_verdict":"current_profile_4C_too_late_after_4B_bounce"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C12_DAEJOO_078600_2024_03_06_SILICON_ANODE_CONTRACT_OPTIONALITY_OVERBLOCK","trigger_id":"DAEJOO_078600_2024_03_06_STAGE2_CUSTOMER_OPTIONALITY_OVERBLOCK_COUNTEREXAMPLE","symbol":"078600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-watch / customer optionality 4B window","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-watch with C12 overblock exception and 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Hard 4C should wait for confirmed call-off or margin break when customer optionality and qualification route remain intact.","MFE_90D_pct":109.22,"MAE_90D_pct":-2.18,"score_return_alignment_label":"overblock_counterexample_then_delayed_4b_audit","current_profile_verdict":"current_profile_overblocks_if_all_customer_contract_risk_treated_as_call_off"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"133","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overblocks_if_all_customer_contract_risk_treated_as_call_off"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R3
completed_loop = 133
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C02_POWER_GRID_DATACENTER_CAPEX, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted, C12 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C12 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/005/005070.json
  - atlas/symbol_profiles/121/121600.json
  - atlas/symbol_profiles/078/078600.json
- Rejected duplicate materialization path:
  - e2r_stock_web_v12_residual_round_R3_loop_132_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
