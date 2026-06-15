# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
created_at_kst = 2026-06-06
selected_round = R1
selected_loop = 83
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = sequential_round_cycle_selected__coverage_gap_within_scheduled_R1
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not a live watchlist, not investment advice, not a production scoring patch, and not a code implementation request.

## 1. Current Calibrated Profile Assumption

Current profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
active_runtime_profile_context = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Existing applied axes treated as stress-test targets rather than re-proposals:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

C05 is a dangerous archetype because a contract headline is real evidence, but not always sufficient evidence. A mega EPC award is like a very large purchase order written on heavy paper: it looks solid, but the investment machine only receives fuel when margin, execution, working capital, and cash conversion move through the pipe.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R1 |
| selected_loop | 83 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| fine_archetype_id | SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY |
| selected_priority_bucket | Priority 0 |
| round_sector_consistency | pass |

Scope logic:

```text
R1 -> L1_INDUSTRIALS_INFRA_DEFENSE_GRID
C05_EPC_MEGA_CONTRACT_MARGIN_GAP -> R1 / L1
```

This run fills a missing early R1 loop slot while staying inside the scheduled round. No-Repeat Index is used as a duplicate ledger and coverage reference only.

## 3. Previous Coverage / Duplicate Avoidance Check

Latest No-Repeat ledger snapshot used for this run:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP rows = 19
C05 symbols = 12
C05 date range = 2022-01-12 ~ 2024-03-27
top covered symbols include 006360, 047040, 000720, 028050, 375500, 034300
```

Duplicate gate:

| candidate | symbol | canonical | trigger_type | entry_date | duplicate verdict |
|---|---:|---|---|---|---|
| Fadhili / GS건설 | 006360 | C05 | Stage2-Actionable | 2024-04-03 | soft symbol reuse, new trigger date/family |
| Fadhili / 삼성E&A | 028050 | C05 | Stage2 | 2024-04-03 | soft symbol reuse, new trigger date/family |
| Jafurah / 현대건설 | 000720 | C05 | Stage2 | 2024-07-01 | soft symbol reuse, new trigger date/family |

Hard duplicate key rule checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No candidate is counted as a reused case because each uses a new trigger date and entry group. Same-symbol repetition is disclosed and penalized qualitatively, but it is still a useful expansion because the Fadhili/Jafurah gas-project evidence family was not represented in the C05 date range shown by the ledger.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| min_date | 1995-05-02 |
| tradable_row_count | 14,354,401 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |

Schema used:

```text
tradable shard columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| symbol | profile path | entry | 180D forward window | corporate-action overlap | calibration_usable |
|---:|---|---|---|---|---|
| 006360 | atlas/symbol_profiles/006/006360.json | 2024-04-03 | available before manifest max date | no 2024/2025 overlap in profile candidate dates | true |
| 028050 | atlas/symbol_profiles/028/028050.json | 2024-04-03 | available before manifest max date | no 2024/2025 overlap in profile candidate dates | true |
| 000720 | atlas/symbol_profiles/000/000720.json | 2024-07-01 | available using 2024+2025 shards | no 2024/2025 overlap in profile candidate dates | true |

Entry timing rule:

```text
Fadhili Reuters timestamp = 2024-04-02 13:00 UTC = after KRX close.
entry_date = next tradable close = 2024-04-03.

Jafurah Reuters timestamp = 2024-06-30 Sunday.
entry_date = next tradable close = 2024-07-01.
```

## 6. Canonical Archetype Compression Map

| canonical | fine/deep sub-archetype | compression decision |
|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | FADHILI_GAS_PLANT_EPC_AWARD | keep under C05; do not split into separate gas-project canonical |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | JAFURAH_GAS_FIELD_CONSORTIUM_AWARD | keep under C05; consortium share/margin bridge is the key C05 question |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | CONTRACT_SCALE_WITHOUT_MARGIN_BRIDGE | canonical guard candidate |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | HIGH_MAE_AFTER_EPC_HEADLINE | counterexample sub-label |

Canonical compression result:

```text
All cases remain C05. The recurring split is not by geography or customer, but by whether a named EPC award is accompanied by company-specific margin, FCF, backlog-quality, and execution-risk evidence at trigger date.
```

## 7. Case Selection Summary

| case_id | symbol | company | trigger family | trigger_date | entry_date | polarity | outcome |
|---|---:|---|---|---|---|---|---|
| C05_R1L83_CASE_006360_FADHILI_20240402 | 006360 | GS건설 | FADHILI_GAS_PLANT_EPC_AWARD | 2024-04-02 | 2024-04-03 | positive | positive_contract_award_with_followthrough_but_not_green_at_trigger |
| C05_R1L83_CASE_028050_FADHILI_20240402 | 028050 | 삼성E&A | FADHILI_GAS_PLANT_EPC_AWARD | 2024-04-02 | 2024-04-03 | counterexample | contract_award_event_cap_high_MAE_counterexample |
| C05_R1L83_CASE_000720_JAFURAH_20240630 | 000720 | 현대건설 | JAFURAH_GAS_FIELD_CONSORTIUM_AWARD | 2024-06-30 | 2024-07-01 | counterexample | large_project_award_low_MFE_high_MAE_before_late_recovery |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive | 1 | GS건설 / Fadhili |
| counterexample | 2 | 삼성E&A / Fadhili, 현대건설 / Jafurah |
| high-MAE path | 2 | 삼성E&A, 현대건설 |
| clean 180D path | 3 | all three |

Interpretation:

```text
The same Saudi Aramco gas-infra evidence family did not produce one uniform equity path.
GS건설 carried the trigger into a stronger 90D/180D path.
삼성E&A and 현대건설 show that C05 must not treat contract size as margin evidence.
```

## 9. Evidence Source Map

| event | date/time | source-level evidence | affected symbols |
|---|---|---|---|
| Fadhili gas plant expansion | 2024-04-02 13:00 UTC | Reuters reported Aramco awarded $7.7bn Fadhili expansion EPC contracts to Samsung Engineering, GS E&C and Nesma; capacity expansion to 4 bscfd; completion expected Nov 2027. | 006360, 028050 |
| Jafurah gas field / main gas network | 2024-06-30 12:50 UTC | Reuters reported Aramco signed over $25bn of contracts; Jafurah awards included a consortium involving Hyundai E&C. | 000720 |

Evidence limitation:

```text
source_proxy_only = true at the public-source level.
This MD uses Reuters named-party evidence and stock-web OHLC. It does not parse full contract margins, backlog accounting notes, or company filings.
Therefore, the proposed rule is shadow-only and canonical-specific.
```

## 10. Price Data Source Map

| symbol | profile | shard(s) | entry row |
|---:|---|---|---|
| 006360 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv | 2024-04-03 close 15,630 |
| 028050 | atlas/symbol_profiles/028/028050.json | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv | 2024-04-03 close 25,300 |
| 000720 | atlas/symbol_profiles/000/000720.json | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv + 2025.csv | 2024-07-01 close 33,200 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| C05_R1L83_TRG_006360_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403 | 006360 | Stage2-Actionable | 2024-04-03 | 15,630 | 6.97 | -10.17 | 30.52 | -10.17 | 39.16 | -10.17 | 2024-08-27 | 21,750 |
| C05_R1L83_TRG_028050_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403 | 028050 | Stage2 | 2024-04-03 | 25,300 | 6.72 | -5.34 | 15.81 | -14.62 | 15.81 | -35.57 | 2024-07-30 | 29,300 |
| C05_R1L83_TRG_000720_JAFURAH_CONSORTIUM_AWARD_NEXTDAY_CLOSE_20240701 | 000720 | Stage2 | 2024-07-01 | 33,200 | 5.12 | -12.5 | 5.12 | -16.27 | 13.1 | -27.41 | 2025-02-18 | 37,550 |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 006360 / GS건설 / Fadhili

| horizon | max high | min low | MFE_pct | MAE_pct | verdict |
|---|---:|---:|---:|---:|---|
| 30D | 16,720 | 14,040 | 6.97 | -10.17 | early evidence not enough for Green |
| 90D | 20,400 | 14,040 | 30.52 | -10.17 | Stage2-Actionable positive |
| 180D | 21,750 | 14,040 | 39.16 | -10.17 | positive, but 4B later requires non-price evidence |

### 12.2 028050 / 삼성E&A / Fadhili

| horizon | max high | min low | MFE_pct | MAE_pct | verdict |
|---|---:|---:|---:|---:|---|
| 30D | 27,000 | 23,950 | 6.72 | -5.34 | initial contract pop only |
| 90D | 29,300 | 21,600 | 15.81 | -14.62 | moderate MFE, high risk |
| 180D | 29,300 | 16,300 | 15.81 | -35.57 | counterexample; contract scale lacked durable margin bridge |

### 12.3 000720 / 현대건설 / Jafurah

| horizon | max high | min low | MFE_pct | MAE_pct | verdict |
|---|---:|---:|---:|---:|---|
| 30D | 34,900 | 29,050 | 5.12 | -12.50 | weak early follow-through |
| 90D | 34,900 | 27,800 | 5.12 | -16.27 | high-MAE event-cap path |
| 180D | 37,550 | 24,100 | 13.10 | -27.41 | late recovery does not validate early Stage2-Actionable |

## 13. Current Calibrated Profile Stress Test

| symbol | P0 score before | P0 label before | P2 score after | P2 label after | current profile verdict |
|---:|---:|---|---:|---|---|
| 006360 | 71.0 | Stage2-Actionable | 73.0 | Stage2-Actionable | current_profile_correct_if_capped_below_Green_until_margin_bridge |
| 028050 | 70.0 | Stage2-Actionable | 62.0 | Stage2-watch | current_profile_false_positive_if_promoted_above_Stage2_watch_without_margin_bridge |
| 000720 | 64.0 | Stage2 | 57.0 | Stage1/weak-watch | current_profile_false_positive_if_contract_headline_promotes_without_project_cashflow_bridge |

Stress-test result:

```text
C05 residual error = contract headline too easily receives Stage2-Actionable credit when margin bridge is not visible.
The global Stage2 evidence bonus remains useful, but C05 needs a canonical guard that asks: "is this contract profitable and cash-converting, or just large?"
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Yellow or Stage3-Green trigger is asserted in this MD.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Stage2 result:

| bucket | symbol | conclusion |
|---|---:|---|
| good Stage2-Actionable | 006360 | named award + strong subsequent price path; still not Green at trigger |
| bad Stage2 if over-promoted | 028050 | named award but high 180D MAE |
| bad Stage2 if over-promoted | 000720 | consortium headline and weak early MFE/high MAE |

## 15. 4B Local vs Full-window Timing Audit

| symbol | possible 4B context | local peak proximity | full-window proximity | verdict |
|---:|---|---|---|---|
| 006360 | Aug 2024 overheat after strong run | not_triggered_as_4B | not_triggered_as_4B | price-only local peak should not be full 4B without margin/revision slowdown |
| 028050 | Jul/Aug peak followed by deep drawdown | not_triggered_as_4B | not_triggered_as_4B | would require non-price margin/backlog slowdown evidence |
| 000720 | early weak MFE, later recovery | not_triggered_as_4B | not_triggered_as_4B | high-MAE guard is more relevant than 4B timing |

4B evidence type:

```text
four_b_evidence_type = price_only_watch | margin_or_backlog_slowdown_needed
do_not_treat_as_full_4B = true
```

## 16. 4C Protection Audit

No hard 4C is asserted because this MD does not establish a company-specific thesis break from filings or contract economics.

| symbol | price-path warning | 4C label |
|---:|---|---|
| 028050 | -44.37% drawdown after peak; -35.57% MAE180 from entry | thesis_break_watch_only |
| 000720 | -27.41% MAE180 before late recovery | high_MAE_guardrail_watch |
| 006360 | drawdown after peak but entry MAE controlled | no_4C |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate = l1_named_contract_requires_backlog_margin_cash_bridge
```

Rule wording:

```text
In L1 industrials/infra/EPC, a named global customer contract can justify Stage2,
but Stage2-Actionable requires at least one of:
1. company-specific margin guidance or margin bridge,
2. backlog conversion schedule with contribution visibility,
3. FCF/working-capital improvement evidence,
4. post-award revision confirmation.
```

This is sector-specific but not global. It is supported by three C05 cases in one L1 scope, not by multiple large sectors.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate = c05_margin_cash_bridge_required_for_stage2_actionable
```

Canonical rule:

```text
For C05, contract_score and backlog_visibility_score can open Stage2 watch.
Stage2-Actionable requires margin_bridge_score >= 6 and execution_risk_score <= 4, or equivalent explicit evidence.
If contract evidence is named but margin/FCF/revision bridge is missing, cap at Stage2-watch and tag high_MAE_guardrail_watch.
```

Expected effect:

```text
- Keep GS건설 as Stage2-Actionable positive because its path validates a useful Stage2 trigger.
- Cap 삼성E&A to Stage2-watch because 180D MAE and post-peak drawdown expose missing margin bridge.
- Cap 현대건설 to Stage1/weak-watch or Stage2-watch because consortium headline lacked company-specific economics and had weak 30D/90D MFE.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | alignment |
|---|---|---:|---:|---:|---:|---:|---|---|
| P0 | current_calibrated_proxy | 3 | 17.15 | -13.69 | 22.69 | -24.38 | 2/3 if all contract events are promoted to Stage2-Actionable | mixed; contract evidence alone is too coarse |
| P0b | baseline_reference | 3 | 17.15 | -13.69 | 22.69 | -24.38 | not_scored_for_production | too blunt for C05 |
| P1 | sector_specific_candidate_profile | 3 | 17.15 | -13.69 | 22.69 | -24.38 | 1/3 | better but still too broad |
| P2 | canonical_archetype_candidate_profile | 3 | 17.15 | -13.69 | 22.69 | -24.38 | 0/3 after Samsung/Hyundai capped | best local alignment |
| P3 | counterexample_guard_profile | 3 | 17.15 | -13.69 | 22.69 | -24.38 | 0/3 but may under-promote GS | safe but too conservative |

## 20. Score-Return Alignment Matrix

| symbol | evidence strength | price path | alignment verdict |
|---:|---|---|---|
| 006360 | named EPC award + customer quality + good price path | MFE90 30.52 / MAE90 -10.17 | aligned with Stage2-Actionable |
| 028050 | named EPC award but margin bridge not confirmed | MFE90 15.81 / MAE180 -35.57 | over-promotion risk |
| 000720 | named consortium award but company share/margin unclear | MFE90 5.12 / MAE180 -27.41 | over-promotion risk |

Mechanism:

```text
The award headline is the ignition spark.
The margin/FCF bridge is the engine.
C05 should not treat the spark as if the engine already turned over.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY | 1 | 2 | 0 | 0 | 3 | 0 | 3 | 3 | 2 | true | true | C05 still Priority 0 until 30-row minimum |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
residual_error_types_found: contract_headline_without_margin_bridge_false_positive | high_MAE_after_mega_EPC_award | late_recovery_does_not_validate_early_promotion
new_axis_proposed: c05_margin_cash_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: null
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest and schema basis
- 006360 / 028050 / 000720 symbol profile availability
- tradable_raw OHLC entry rows
- 30D / 90D / 180D MFE/MAE using observed 1D high/low paths
- no 2024/2025 corporate-action candidate overlap in symbol profiles
```

Not validated:

```text
- exact contract value allocated to each company
- project-level gross margin
- working-capital/cash-conversion details
- company filing-level backlog accounting
- intraday event-time price reaction
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c05_margin_cash_bridge_required_for_stage2_actionable,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"Mega EPC awards need margin/FCF/revision bridge before Stage2-Actionable; contract scale alone created high-MAE counterexamples.","1 positive GS case kept; Samsung E&A and Hyundai E&C capped to Stage2-watch/weak-watch because 90D/180D MAE overwhelmed headline evidence.","C05_R1L83_TRG_006360_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403|C05_R1L83_TRG_028050_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403|C05_R1L83_TRG_000720_JAFURAH_CONSORTIUM_AWARD_NEXTDAY_CLOSE_20240701",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C05_R1L83_CASE_006360_FADHILI_20240402","symbol":"006360","company_name":"GS건설","round":"R1","loop":"83","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C05_R1L83_TRG_006360_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2-Actionable entry had strong 90D/180D upside with controlled entry MAE; Green still needs margin/FCF bridge.","current_profile_verdict":"current_profile_correct_if_capped_below_Green_until_margin_bridge","price_source":"Songdaiki/stock-web","notes":"Same symbol is already covered in C05 ledger, but this uses a new post-2024-03-27 Fadhili trigger date and same-day-after-close next-trading-day entry."}
{"row_type":"case","case_id":"C05_R1L83_CASE_028050_FADHILI_20240402","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"83","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY","case_type":"high_mae_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C05_R1L83_TRG_028050_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Contract scale produced only moderate MFE and later deep MAE; C05 should demand margin/FCF/revision bridge before Stage2-Actionable.","current_profile_verdict":"current_profile_false_positive_if_promoted_above_Stage2_watch_without_margin_bridge","price_source":"Songdaiki/stock-web","notes":"Same symbol is already covered in C05 ledger, but this trigger uses the new Fadhili 2024-04-02 evidence family and next-trading-day entry."}
{"row_type":"case","case_id":"C05_R1L83_CASE_000720_JAFURAH_20240630","symbol":"000720","company_name":"현대건설","round":"R1","loop":"83","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY","case_type":"high_mae_late_recovery_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C05_R1L83_TRG_000720_JAFURAH_CONSORTIUM_AWARD_NEXTDAY_CLOSE_20240701","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Project headline alone had weak 30D/90D MFE and large 180D MAE; later recovery does not validate early Stage2-Actionable promotion.","current_profile_verdict":"current_profile_false_positive_if_contract_headline_promotes_without_project_cashflow_bridge","price_source":"Songdaiki/stock-web","notes":"Same symbol appears in C05 coverage, but this Jafurah consortium trigger family and 2024-07-01 entry are outside the cited C05 ledger date range."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C05_R1L83_TRG_006360_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403","case_id":"C05_R1L83_CASE_006360_FADHILI_20240402","symbol":"006360","company_name":"GS건설","round":"R1","loop":"83","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-02","entry_date":"2024-04-03","entry_price":15630,"evidence_available_at_that_date":"Reuters, 2024-04-02 13:00 UTC, Aramco awards $7.7bn Fadhili gas expansion EPC contracts to Samsung Engineering, GS E&C and Nesma.","evidence_source":"Reuters, 2024-04-02 13:00 UTC, Aramco awards $7.7bn Fadhili gas expansion EPC contracts to Samsung Engineering, GS E&C and Nesma.","stage2_evidence_fields":["named_EPC_award","Saudi_Aramco_customer","gas_plant_capacity_expansion","project_completion_schedule"],"stage3_evidence_fields":["not_confirmed_margin_bridge_at_trigger","not_confirmed_FCF_conversion_at_trigger"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.97,"MFE_90D_pct":30.52,"MFE_180D_pct":39.16,"MAE_30D_pct":-10.17,"MAE_90D_pct":-10.17,"MAE_180D_pct":-10.17,"MFE_1Y_pct":"not_computed_not_needed_for_180D_delta","MFE_2Y_pct":"not_computed_not_needed_for_180D_delta","MAE_1Y_pct":"not_computed_not_needed_for_180D_delta","MAE_2Y_pct":"not_computed_not_needed_for_180D_delta","peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-22.48,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"positive_contract_award_with_followthrough_but_not_green_at_trigger","current_profile_verdict":"current_profile_correct_if_capped_below_Green_until_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_2025_profile_candidate_overlap","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|2024-04-03|15630","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L83_TRG_028050_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403","case_id":"C05_R1L83_CASE_028050_FADHILI_20240402","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"83","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-02","entry_date":"2024-04-03","entry_price":25300,"evidence_available_at_that_date":"Reuters, 2024-04-02 13:00 UTC, Aramco awards $7.7bn Fadhili gas expansion EPC contracts to Samsung Engineering, GS E&C and Nesma.","evidence_source":"Reuters, 2024-04-02 13:00 UTC, Aramco awards $7.7bn Fadhili gas expansion EPC contracts to Samsung Engineering, GS E&C and Nesma.","stage2_evidence_fields":["named_EPC_award","Saudi_Aramco_customer","gas_plant_capacity_expansion"],"stage3_evidence_fields":["margin_bridge_missing_at_trigger","revision_followthrough_not_confirmed"],"stage4b_evidence_fields":["valuation_or_event_cap_watch_after_July_peak"],"stage4c_evidence_fields":["180D_high_MAE_without_price_path_support"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.72,"MFE_90D_pct":15.81,"MFE_180D_pct":15.81,"MAE_30D_pct":-5.34,"MAE_90D_pct":-14.62,"MAE_180D_pct":-35.57,"MFE_1Y_pct":"not_computed_not_needed_for_180D_delta","MFE_2Y_pct":"not_computed_not_needed_for_180D_delta","MAE_1Y_pct":"not_computed_not_needed_for_180D_delta","MAE_2Y_pct":"not_computed_not_needed_for_180D_delta","peak_date":"2024-07-30","peak_price":29300,"drawdown_after_peak_pct":-44.37,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"contract_award_event_cap_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_promoted_above_Stage2_watch_without_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_2025_profile_candidate_overlap","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|2024-04-03|25300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L83_TRG_000720_JAFURAH_CONSORTIUM_AWARD_NEXTDAY_CLOSE_20240701","case_id":"C05_R1L83_CASE_000720_JAFURAH_20240630","symbol":"000720","company_name":"현대건설","round":"R1","loop":"83","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SAUDI_GAS_EPC_AWARD_MARGIN_BRIDGE_VS_MEGA_CONTRACT_PRICE_SPIKE_AND_BACKLOG_QUALITY","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-06-30","entry_date":"2024-07-01","entry_price":33200,"evidence_available_at_that_date":"Reuters, 2024-06-30 12:50 UTC, Aramco signs over $25bn contracts for Jafurah gas field and main gas network expansion; Jafurah awards included a consortium involving Hyundai E&C.","evidence_source":"Reuters, 2024-06-30 12:50 UTC, Aramco signs over $25bn contracts for Jafurah gas field and main gas network expansion; Jafurah awards included a consortium involving Hyundai E&C.","stage2_evidence_fields":["named_consortium_award","Saudi_Aramco_customer","large_gas_field_project"],"stage3_evidence_fields":["consortium_share_unknown","company_specific_margin_bridge_missing","FCF_conversion_not_confirmed"],"stage4b_evidence_fields":["event_premium_cap_watch"],"stage4c_evidence_fields":["high_MAE_before_late_recovery"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MFE_90D_pct":5.12,"MFE_180D_pct":13.1,"MAE_30D_pct":-12.5,"MAE_90D_pct":-16.27,"MAE_180D_pct":-27.41,"MFE_1Y_pct":"not_computed_not_needed_for_180D_delta","MFE_2Y_pct":"not_computed_not_needed_for_180D_delta","MAE_1Y_pct":"not_computed_not_needed_for_180D_delta","MAE_2Y_pct":"not_computed_not_needed_for_180D_delta","peak_date":"2025-02-18","peak_price":37550,"drawdown_after_peak_pct":-14.11,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"large_project_award_low_MFE_high_MAE_before_late_recovery","current_profile_verdict":"current_profile_false_positive_if_contract_headline_promotes_without_project_cashflow_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_2025_profile_candidate_overlap","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|2024-07-01|33200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P2_c05_margin_cash_bridge_guard_shadow","case_id":"C05_R1L83_CASE_006360_FADHILI_20240402","trigger_id":"C05_R1L83_TRG_006360_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":14,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":71.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":15,"margin_bridge_score":7,"revision_score":4,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":73.0,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C05 shadow profile keeps contract credit but caps Stage2-Actionable unless margin/FCF/revision bridge is visible at trigger date.","MFE_90D_pct":30.52,"MAE_90D_pct":-10.17,"score_return_alignment_label":"Stage2-Actionable entry had strong 90D/180D upside with controlled entry MAE; Green still needs margin/FCF bridge.","current_profile_verdict":"current_profile_correct_if_capped_below_Green_until_margin_bridge"}
{"row_type":"score_simulation","profile_id":"P2_c05_margin_cash_bridge_guard_shadow","case_id":"C05_R1L83_CASE_028050_FADHILI_20240402","trigger_id":"C05_R1L83_TRG_028050_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":14,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":70.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":14,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":8,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":62.0,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C05 shadow profile keeps contract credit but caps Stage2-Actionable unless margin/FCF/revision bridge is visible at trigger date.","MFE_90D_pct":15.81,"MAE_90D_pct":-14.62,"score_return_alignment_label":"Contract scale produced only moderate MFE and later deep MAE; C05 should demand margin/FCF/revision bridge before Stage2-Actionable.","current_profile_verdict":"current_profile_false_positive_if_promoted_above_Stage2_watch_without_margin_bridge"}
{"row_type":"score_simulation","profile_id":"P2_c05_margin_cash_bridge_guard_shadow","case_id":"C05_R1L83_CASE_000720_JAFURAH_20240630","trigger_id":"C05_R1L83_TRG_000720_JAFURAH_CONSORTIUM_AWARD_NEXTDAY_CLOSE_20240701","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":11,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":64.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":10,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":57.0,"stage_label_after":"Stage1/weak-watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C05 shadow profile keeps contract credit but caps Stage2-Actionable unless margin/FCF/revision bridge is visible at trigger date.","MFE_90D_pct":5.12,"MAE_90D_pct":-16.27,"score_return_alignment_label":"Project headline alone had weak 30D/90D MFE and large 180D MAE; later recovery does not validate early Stage2-Actionable promotion.","current_profile_verdict":"current_profile_false_positive_if_contract_headline_promotes_without_project_cashflow_bridge"}
```

### 25.5 shadow_weight row

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c05_margin_cash_bridge_required_for_stage2_actionable,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"Mega EPC awards need margin/FCF/revision bridge before Stage2-Actionable; contract scale alone created high-MAE counterexamples.","1 positive GS case kept; Samsung E&A and Hyundai E&C capped to Stage2-watch/weak-watch because 90D/180D MAE overwhelmed headline evidence.","C05_R1L83_TRG_006360_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403|C05_R1L83_TRG_028050_FADHILI_EPC_AWARD_NEXTDAY_CLOSE_20240403|C05_R1L83_TRG_000720_JAFURAH_CONSORTIUM_AWARD_NEXTDAY_CLOSE_20240701",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"83","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":0,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["contract_headline_without_margin_bridge_false_positive","high_MAE_after_mega_EPC_award","late_recovery_does_not_validate_early_promotion"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C05_R1L83_SOURCE_NOTE_REUTERS_AND_STOCKWEB","symbol":"MULTI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reason":"Human-readable evidence and price-source notes; machine calibration rows above carry the usable trigger data.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R1
completed_loop = 83
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = sequential_round_cycle_selected__coverage_gap_within_scheduled_R1
round_sector_consistency = pass
next_scheduled_round = R2
next_scheduled_loop = 83
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP until 30-row minimum; then C01_ORDER_BACKLOG_MARGIN_BRIDGE; if cross-checkpoint is required, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```

## 28. Source Notes

Primary execution and duplicate ledgers:

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md
```

Stock-Web files inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/006/006360.json
atlas/symbol_profiles/028/028050.json
atlas/symbol_profiles/000/000720.json
atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv
```

Public evidence source notes:

```text
Reuters, 2024-04-02, Aramco awards $7.7bn in contracts for Fadhili gas expansion.
Reuters, 2024-06-30, Aramco signs over $25bn of deals for main gas network and Jafurah gas field.
```
