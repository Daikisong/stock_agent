# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R12_loop_13_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
scheduled_round = R12
scheduled_loop = 13
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove the global Stage2 bonus. It stress-tests whether a macro food/grain shock should be scored differently when the listed company has a direct feed/input transmission route versus when the same headline is merely downstream input-cost pressure.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R12
loop = 13
round_scheduler_source = previous local v12 output ended at R11 Loop 13 with next_round=R12 / next_loop=13; stock_agent md_registry contains historical R12 entries through loop 8 and R13 entries through loop 8, while the v12 local continuation has advanced beyond repo registry.
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS
```

R12 is treated here as agriculture / life-services / miscellaneous event propagation. The round-sector pair is valid because R12 can use L10 when the work is policy/event/misc rather than a standard consumer-brand R5 study.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were limited to calibration registry / trigger rows. `data/e2r/calibration/trigger_rows_representative.jsonl` was empty in the checked branch, so no symbol+trigger duplicate was found there. `md_registry.jsonl` showed prior R12 historical calibration rounds, but those entries were pre-v12 historical-calibration files rather than this exact v12 residual file pattern.

Diversity gate result:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = none_found_in_allowed_trigger_rows
new_symbol_count = 4
new_trigger_family_count = 4
new_independent_case_ratio = 1.00
minimum_new_independent_case_ratio = 0.60
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest validation:

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

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_basis = tradable_raw
raw_adjustment = none; raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

All representative Stage2 triggers pass the 180D historical eligibility gate:

| symbol | profile path | entry_date | profile last_date | 180D forward available | corporate-action overlap in 180D | calibration_usable |
|---:|---|---:|---:|---:|---:|---:|
| 005860 | atlas/symbol_profiles/005/005860.json | 2022-02-24 | 2026-02-20 | yes | no; listed candidates end 2016-12-22 | true |
| 218150 | atlas/symbol_profiles/218/218150.json | 2022-02-24 | 2026-02-20 | yes | no; listed candidate 2017-12-28 | true |
| 027710 | atlas/symbol_profiles/027/027710.json | 2022-02-24 | 2026-02-20 | yes | no; listed candidates end 2019-12-13 | true |
| 004370 | atlas/symbol_profiles/004/004370.json | 2022-02-24 | 2026-02-20 | yes | no; listed candidates end 2003-07-18 | true |

## 6. Canonical Archetype Compression Map

```text
fine_archetype = GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
compression_reason = A global grain/food shock is a policy/event propagation trigger. It should not be treated as a normal consumer-export or brand-retail archetype unless the research question is channel/reorder/margin in R5.
```

Compression rule:

1. Direct feed/raw-material suppliers can receive Stage2-Actionable credit when the shock changes near-term demand/price negotiation or theme liquidity.
2. Downstream food producers should not receive positive Stage2 credit from the same headline unless pricing power, inventory windfall, export channel, or confirmed margin bridge exists.
3. Price/volume blowoff after the shock is a 4B overlay, not Green confirmation.

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | best trigger | OHLC result | current profile verdict |
|---|---:|---|---|---|---|---|---|
| R12L13_C31_005860_GRAIN_FEED_DIRECT | 005860 | 한일사료 | structural_success | positive | 2022-02-24 close | MFE90 520.35%, MAE90 -18.59%, peak 2022-04-25 15850 | current_profile_correct |
| R12L13_C31_218150_FEED_ADDITIVE_DIRECT | 218150 | 미래생명자원 | structural_success | positive | 2022-02-24 close | MFE90 59.46%, MAE90 -27.07%, peak 2022-04-19 12900 | current_profile_correct |
| R12L13_C31_027710_FEED_THEME_HIGH_MAE | 027710 | 팜스토리 | high_mae_success | counterexample | 2022-02-24 close | MFE90 108.22%, MAE90 -20.89%, peak 2022-04-27 6330 | current_profile_false_positive |
| R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE | 004370 | 농심 | failed_rerating | counterexample | 2022-02-24 close | MFE90 1.69%, MAE90 -19.35%, peak 2022-02-25 331000 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 2
4B_or_4C_case = 3 4B overlays
calibration_usable_case_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The positive set is not interpreted as durable Stage3-Green proof. It is a Stage2/4B calibration set. Think of the grain shock as a flood through a canal: the same water turns the feed-mill wheel, but it drowns the downstream food producer's margin unless that producer has a pump called pricing power.

## 9. Evidence Source Map

| evidence family | trigger date | source note | scoring use |
|---|---:|---|---|
| Russia invasion / Black Sea grain shock | 2022-02-24 | Public historical event. AP/Axios/FAO reporting described 2022 food prices and March 2022 FAO index as record-high, with war-driven disruption. | Stage2 public_event_or_disclosure / policy_or_regulatory_optionality |
| Direct feed/input linkage | 2022-02-24 onward | Listed Korean feed/feed-adjacent names reacted through tradable OHLC rows. | Stage2 directness and relative_strength |
| Downstream food cost pressure | 2022-02-24 onward | Same macro food inflation can pressure margins where inputs rise before pricing power is proven. | Counterexample guard |
| Price/volume blowoff | 2022-03 to 2022-04 | Stock-web OHLC peaks in 005860/218150/027710. | 4B overlay only |

External evidence references used as historical context:

```text
AP: Global food prices in 2022 hit record high amid drought, war.
Axios: Russian invasion of Ukraine fuels record food prices; FAO March 2022 index at 159.3.
Reuters/FAO-context reporting: Ukraine grain storage/export constraints during war.
```

## 10. Price Data Source Map

| symbol | company | shard | entry row checked | peak row checked | profile caveat |
|---:|---|---|---|---|---|
| 005860 | 한일사료 | atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv | 2022-02-24 c=2555 | 2022-04-25 h=15850 | raw/unadjusted; no 2022 corporate action candidate |
| 218150 | 미래생명자원 | atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv | 2022-02-24 c=8090 | 2022-04-19 h=12900 | raw/unadjusted; no 2022 corporate action candidate |
| 027710 | 팜스토리 | atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv | 2022-02-24 c=3040 | 2022-04-27 h=6330 | raw/unadjusted; no 2022 corporate action candidate |
| 004370 | 농심 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2022.csv | 2022-02-24 c=325500 | 2022-02-25 h=331000 | raw/unadjusted; no 2022 corporate action candidate |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | verdict | aggregate |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| R12L13_C31_005860_GRAIN_FEED_DIRECT_T_STAGE2_20220224 | 005860 | Stage2-Actionable | 2022-02-24 | 2555 | 85.52 | -18.59 | 520.35 | -18.59 | 520.35 | -18.59 | 2022-04-25 / 15850 | current_profile_correct | representative |
| R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_STAGE2_20220224 | 218150 | Stage2-Actionable | 2022-02-24 | 8090 | 53.28 | -19.04 | 59.46 | -27.07 | 59.46 | -42.71 | 2022-04-19 / 12900 | current_profile_correct | representative |
| R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224 | 027710 | Stage2-Actionable | 2022-02-24 | 3040 | 15.13 | -20.89 | 108.22 | -20.89 | 108.22 | -38.49 | 2022-04-27 / 6330 | current_profile_false_positive | representative |
| R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224 | 004370 | Stage2-Actionable | 2022-02-24 | 325500 | 1.69 | -13.82 | 1.69 | -19.35 | 1.69 | -19.35 | 2022-02-25 / 331000 | current_profile_false_positive | representative |
| R12L13_C31_005860_GRAIN_FEED_DIRECT_T_4B_20220422 | 005860 | Stage4B-Overlay | 2022-04-22 | 13300 | 19.17 | -44.89 | 19.17 | -62.03 | 19.17 | -62.03 | 2022-04-25 / 15850 | current_profile_4B_too_late | 4B_overlay_only |
| R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_4B_20220322 | 218150 | Stage4B-Overlay | 2022-03-22 | 11750 | 9.79 | -30.13 | 9.79 | -49.79 | 9.79 | -60.55 | 2022-04-19 / 12900 | current_profile_4B_too_early | 4B_overlay_only |
| R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_4B_20220426 | 027710 | Stage4B-Overlay | 2022-04-26 | 5320 | 18.98 | -34.87 | 18.98 | -52.54 | 18.98 | -64.85 | 2022-04-27 / 6330 | current_profile_4B_too_early | 4B_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

Representative Stage2 trigger table:

| symbol | entry_date | entry_price | max high 30D | min low 30D | MFE30 | MAE30 | max high 90D | min low 90D | MFE90 | MAE90 | max high 180D | min low 180D | MFE180 | MAE180 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 005860 | 2022-02-24 | 2555 | 4740 | 2080 | 85.52 | -18.59 | 15850 | 2080 | 520.35 | -18.59 | 15850 | 2080 | 520.35 | -18.59 |
| 218150 | 2022-02-24 | 8090 | 12400 | 6550 | 53.28 | -19.04 | 12900 | 5900 | 59.46 | -27.07 | 12900 | 4635 | 59.46 | -42.71 |
| 027710 | 2022-02-24 | 3040 | 3500 | 2405 | 15.13 | -20.89 | 6330 | 2405 | 108.22 | -20.89 | 6330 | 1870 | 108.22 | -38.49 |
| 004370 | 2022-02-24 | 325500 | 331000 | 280500 | 1.69 | -13.82 | 331000 | 262500 | 1.69 | -19.35 | 331000 | 262500 | 1.69 | -19.35 |

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely action | actual alignment | verdict |
|---:|---|---|---|
| 005860 | Stage2-Actionable allowed, Green blocked without revisions | Massive MFE but event/positioning blowoff, not durable Green | current_profile_correct |
| 218150 | Stage2-Actionable allowed, Green blocked without revisions | Positive MFE, heavy MAE; Green block appropriate | current_profile_correct |
| 027710 | Could be promoted too generously if relative-strength/event headline is overweighted | MFE arrived after high early MAE; no revision bridge | current_profile_false_positive |
| 004370 | Should not promote from grain headline alone | Downstream input-cost pressure, weak MFE, sizable MAE | current_profile_false_positive |

Answers to required stress-test questions:

```text
stage2_actionable_evidence_bonus = useful for 005860/218150, too broad for 027710/004370 unless directness guard is applied.
yellow_threshold_75 = adequate when directness exists; too low for downstream/input-cost-only names.
green_threshold_87_revision_55 = should remain strict; no case here has confirmed Stage3-Green revision evidence.
price_only_blowoff_guard = strengthened; 027710 and 4B overlays show why.
full_4b_non_price_requirement = kept/strengthened; price-only local peaks are not full thesis breaks.
hard_4c_routing = not directly tested; thesis_break_watch_only labels used.
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop. The main audit is Stage2-Actionable versus a too-easy Yellow label. Green lateness is `not_applicable` because the historical event created price motion before company-level revision evidence.

```text
Stage2-Actionable: supported for 005860 and 218150 if direct feed/input route is present.
Stage3-Yellow: only tentative; requires directness plus early financial visibility.
Stage3-Green: blocked; no confirmed revision / durable customer / margin bridge.
green_lateness_ratio = not_applicable:no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B trigger | 4B entry | local proximity | full-window proximity | verdict |
|---:|---:|---:|---:|---:|---|
| 005860 | 2022-04-22 | 13300 | 0.808 | 0.808 | good_full_window_4B_timing |
| 218150 | 2022-03-22 | 11750 | 0.849 | 0.761 | good_local_but_early_full_window_4B |
| 027710 | 2022-04-26 | 5320 | 0.693 | 0.693 | price_only_local_4B_too_early |
| 004370 | none | null | null | null | no_4B_trigger |

The split matters: price-only peaks can look like a 4B mirror, but without non-price evidence the mirror is only reflecting crowd heat, not thesis decay.

## 16. 4C Protection Audit

No hard 4C thesis-break trigger is accepted. The proper label is `thesis_break_watch_only` for direct feed themes once prices lose momentum and no financial revision follows. For 004370, the better route is not 4C; it is pre-promotion blocking.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_name = L10_R12_EVENT_DIRECTNESS_GATE
candidate = true
```

Rule candidate:

> In R12/L10 agriculture-life-misc event shocks, Stage2-Actionable promotion requires a direct transmission route: feed/input sales exposure, inventory/pricing windfall, or explicit order/volume evidence. If the same macro event is merely downstream input-cost pressure, demote to Stage2-Watch or block positive promotion.

Expected effect:

```text
positive retained = 005860, 218150
counterexample blocked = 027710 if only theme-beta/high-MAE, 004370 if only downstream cost pressure
scope = sector_specific / R12-L10 event propagation
confidence = medium-low; 4 cases, balanced but still small sample
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule_name = C31_EVENT_TRANSMISSION_QUALITY_GATE
candidate = true
```

Canonical rule candidate:

> C31 event shocks must classify the direction of economic transmission before scoring. Positive event score is allowed only when the event creates a plausible revenue/margin/volume tailwind for the listed entity. If the event is cost inflation, supply squeeze without pricing power, or pure theme liquidity, reduce policy_or_regulatory_score and add execution/input-cost risk.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible trigger count | selected entry trigger per case | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | missed structural count | score-return alignment |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 4 | 4 | 172.43 | -21.48 | 172.43 | -29.79 | 0.50 | 0 | mixed; direct cases pass but downstream/theme cases leak |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | 4 | 172.43 | -21.48 | 172.43 | -29.79 | 0.75 | 0 | weaker guard; too much event/RS promotion |
| P1 sector_specific_candidate_profile | R12/L10 | 3 | 3 direct/theme names | 229.34 | -22.18 | 229.34 | -33.26 | 0.33 | 0 | better but 027710 still risky |
| P2 canonical_archetype_candidate_profile | C31 directness gate | 2 | 2 direct names only | 289.90 | -22.83 | 289.90 | -30.65 | 0.00 | 0 | best alignment in this loop |
| P3 counterexample_guard_profile | guard | 4 | 2 accepted / 2 blocked | 289.90 accepted | -22.83 accepted | 289.90 accepted | -30.65 accepted | 0.00 | 0 | strongest counterexample control |

## 20. Score-Return Alignment Matrix

| axis | existing axis status | observation | outcome |
|---|---|---|---|
| stage2_actionable_evidence_bonus | existing_axis_tested | Works for direct feed/input names | kept with directness gate |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened | 027710 / 4B overlay shows high peak but poor risk path | strengthen |
| full_4b_requires_non_price_evidence | existing_axis_strengthened | Price-only local peaks should not become thesis breaks | strengthen |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept | No hard 4C tested | keep |
| C31_EVENT_TRANSMISSION_QUALITY_GATE | new_axis_proposed | Differentiates direct feed tailwind from downstream cost pressure | propose shadow-only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS | 2 | 2 | 3 | 0 | 4 | 0 | 7 | 4 | 2 | true | true | Still needs non-Ukraine agri event holdout and commodity-price-downside cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: theme_beta_high_MAE, downstream_input_cost_false_positive, price_only_4B_too_early
new_axis_proposed: C31_EVENT_TRANSMISSION_QUALITY_GATE
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: none
existing_axis_kept: stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Songdaiki/stock-web manifest and schema assumptions.
- 2022 1D OHLC rows for 005860, 218150, 027710, 004370.
- 30D/90D/180D MFE/MAE for representative Stage2 triggers.
- Local/full-window 4B proximity for 005860, 218150, 027710.
- Corporate-action window status using symbol profile candidate dates.
```

Not validated:

```text
- No live/current candidate discovery.
- No production scoring patch.
- No stock_agent src/e2r access.
- No brokerage or auto-trading action.
- 1Y/2Y fields are present but left null because the active calibration scope of this loop is 30D/90D/180D residual scoring.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_EVENT_TRANSMISSION_QUALITY_GATE,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require direct revenue/margin/volume route before event shock can promote positive Stage2","Blocks 004370 and weakens 027710 while retaining 005860/218150","R12L13_C31_005860_GRAIN_FEED_DIRECT_T_STAGE2_20220224|R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_STAGE2_20220224|R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224|R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224",4,4,2,medium_low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L10_R12_DOWNSTREAM_INPUT_COST_BLOCK,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Food/grain headline can be negative for downstream margin if pricing power is unproven","Reduces false positive on 004370",R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224,1,1,1,medium_low,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,PRICE_ONLY_LOCAL_4B_NOT_FULL_4B,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Existing axis strengthened, not changed globally","027710 local 4B is too price-only to count as full 4B",R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_4B_20220426,3,3,1,medium_low,axis_stress_test,"existing axis strengthened"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L13_C31_005860_GRAIN_FEED_DIRECT_T_STAGE2_20220224", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Direct feed-cost / feed-price beta transmitted quickly; still high-volatility event beta rather than durable Green."}
{"row_type": "case", "case_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT", "symbol": "218150", "company_name": "미래생명자원", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_STAGE2_20220224", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Direct animal-feed / additive adjacency captured the grain shock but did not justify Stage3-Green without revision evidence."}
{"row_type": "case", "case_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_high_MAE_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Theme beta eventually rallied, but early Stage2 had poor MAE and no confirmed revision bridge; Green promotion would be false positive."}
{"row_type": "case", "case_id": "R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE", "symbol": "004370", "company_name": "농심", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_high_MAE_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Same food-inflation event acted as input-cost pressure for downstream food producer; headline food inflation must not be promoted as positive without pricing-power evidence."}
{"row_type": "trigger", "trigger_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT_T_STAGE2_20220224", "case_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "sector": "agriculture_life_services_other / policy_event_misc", "primary_archetype": "global grain/feed cost shock", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Russia invaded Ukraine; global grain/feed supply shock became public before/through the KRX session; event evidence existed but company-specific revision evidence did not.", "evidence_source": "FAO/AP/Axios/Reuters-style public historical event sources; stock-web OHLC row for entry.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility_watch_only"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 2555, "MFE_30D_pct": 85.52, "MFE_90D_pct": 520.35, "MFE_180D_pct": 520.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.59, "MAE_90D_pct": -18.59, "MAE_180D_pct": -18.59, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -68.14, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT_20220224_C2555", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_STAGE2_20220224", "case_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT", "symbol": "218150", "company_name": "미래생명자원", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "sector": "agriculture_life_services_other / policy_event_misc", "primary_archetype": "global grain/feed cost shock", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Russia invaded Ukraine; global grain/feed supply shock became public before/through the KRX session; event evidence existed but company-specific revision evidence did not.", "evidence_source": "FAO/AP/Axios/Reuters-style public historical event sources; stock-web OHLC row for entry.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility_watch_only"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv", "profile_path": "atlas/symbol_profiles/218/218150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 8090, "MFE_30D_pct": 53.28, "MFE_90D_pct": 59.46, "MFE_180D_pct": 59.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.04, "MAE_90D_pct": -27.07, "MAE_180D_pct": -42.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-19", "peak_price": 12900, "drawdown_after_peak_pct": -64.07, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT_20220224_C8090", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224", "case_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "sector": "agriculture_life_services_other / policy_event_misc", "primary_archetype": "global grain/feed cost shock", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Russia invaded Ukraine; global grain/feed supply shock became public before/through the KRX session; event evidence existed but company-specific revision evidence did not.", "evidence_source": "FAO/AP/Axios/Reuters-style public historical event sources; stock-web OHLC row for entry.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv", "profile_path": "atlas/symbol_profiles/027/027710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 3040, "MFE_30D_pct": 15.13, "MFE_90D_pct": 108.22, "MFE_180D_pct": 108.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.89, "MAE_90D_pct": -20.89, "MAE_180D_pct": -38.49, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-27", "peak_price": 6330, "drawdown_after_peak_pct": -70.46, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE_20220224_C3040", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224", "case_id": "R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE", "symbol": "004370", "company_name": "농심", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "sector": "agriculture_life_services_other / policy_event_misc", "primary_archetype": "global grain/feed cost shock", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Russia invaded Ukraine; global grain/feed supply shock became public before/through the KRX session; event evidence existed but company-specific revision evidence did not.", "evidence_source": "FAO/AP/Axios/Reuters-style public historical event sources; stock-web OHLC row for entry.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "input_cost_pressure_flag"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004370/2022.csv", "profile_path": "atlas/symbol_profiles/004/004370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 325500, "MFE_30D_pct": 1.69, "MFE_90D_pct": 1.69, "MFE_180D_pct": 1.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.82, "MAE_90D_pct": -19.35, "MAE_180D_pct": -19.35, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-02-25", "peak_price": 331000, "drawdown_after_peak_pct": -20.69, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_20220224_C325500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT_T_4B_20220422", "case_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "sector": "agriculture_life_services_other / policy_event_misc", "primary_archetype": "global grain/feed cost shock 4B overlay", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2022-04-22", "evidence_available_at_that_date": "Post-Stage2 price/volume blowoff with no confirmed company-level revision; 4B is an overlay, not an automatic exit instruction.", "evidence_source": "stock-web OHLC row plus public food/grain shock context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-22", "entry_price": 13300, "MFE_30D_pct": 19.17, "MFE_90D_pct": 19.17, "MFE_180D_pct": 19.17, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -44.89, "MAE_90D_pct": -62.03, "MAE_180D_pct": -62.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -68.14, "green_lateness_ratio": "not_applicable:4B_overlay_only", "four_b_local_peak_proximity": 0.808, "four_b_full_window_peak_proximity": 0.808, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT_2022-04-22_C13300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_4B_20220322", "case_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT", "symbol": "218150", "company_name": "미래생명자원", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "sector": "agriculture_life_services_other / policy_event_misc", "primary_archetype": "global grain/feed cost shock 4B overlay", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2022-03-22", "evidence_available_at_that_date": "Post-Stage2 price/volume blowoff with no confirmed company-level revision; 4B is an overlay, not an automatic exit instruction.", "evidence_source": "stock-web OHLC row plus public food/grain shock context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv", "profile_path": "atlas/symbol_profiles/218/218150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-22", "entry_price": 11750, "MFE_30D_pct": 9.79, "MFE_90D_pct": 9.79, "MFE_180D_pct": 9.79, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.13, "MAE_90D_pct": -49.79, "MAE_180D_pct": -60.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-19", "peak_price": 12900, "drawdown_after_peak_pct": -64.07, "green_lateness_ratio": "not_applicable:4B_overlay_only", "four_b_local_peak_proximity": 0.849, "four_b_full_window_peak_proximity": 0.761, "four_b_timing_verdict": "good_local_but_early_full_window_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT_2022-03-22_C11750", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_4B_20220426", "case_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GLOBAL_GRAIN_FEED_COST_SHOCK_DIRECTNESS", "sector": "agriculture_life_services_other / policy_event_misc", "primary_archetype": "global grain/feed cost shock 4B overlay", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2022-04-26", "evidence_available_at_that_date": "Post-Stage2 price/volume blowoff with no confirmed company-level revision; 4B is an overlay, not an automatic exit instruction.", "evidence_source": "stock-web OHLC row plus public food/grain shock context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv", "profile_path": "atlas/symbol_profiles/027/027710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-26", "entry_price": 5320, "MFE_30D_pct": 18.98, "MFE_90D_pct": 18.98, "MFE_180D_pct": 18.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -34.87, "MAE_90D_pct": -52.54, "MAE_180D_pct": -64.85, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-27", "peak_price": 6330, "drawdown_after_peak_pct": -70.46, "green_lateness_ratio": "not_applicable:4B_overlay_only", "four_b_local_peak_proximity": 0.693, "four_b_full_window_peak_proximity": 0.693, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE_2022-04-26_C5320", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT", "trigger_id": "R12L13_C31_005860_GRAIN_FEED_DIRECT_T_STAGE2_20220224", "symbol": "005860", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 20, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 20, "valuation_repricing_score": 12, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "margin_bridge_score", "direct_feed_input_transmission_score"], "component_delta_explanation": "Direct feed/input linkage receives shadow credit, but absence of confirmed revision keeps the label below Stage3-Green.", "MFE_90D_pct": 520.35, "MAE_90D_pct": -18.59, "score_return_alignment_label": "score_return_alignment_positive_but_not_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT", "trigger_id": "R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_STAGE2_20220224", "symbol": "218150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 20, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 20, "valuation_repricing_score": 12, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "margin_bridge_score", "direct_feed_input_transmission_score"], "component_delta_explanation": "Direct feed/input linkage receives shadow credit, but absence of confirmed revision keeps the label below Stage3-Green.", "MFE_90D_pct": 59.46, "MAE_90D_pct": -27.07, "score_return_alignment_label": "score_return_alignment_positive_but_not_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE", "trigger_id": "R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224", "symbol": "027710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -8, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 20, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -10, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 12, "valuation_repricing_score": 0, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["margin_bridge_score", "execution_risk_score", "downstream_cost_pressure_guard"], "component_delta_explanation": "Headline grain/food shock is demoted when there is no direct volume/repricing route or when the shock is mainly input-cost pressure.", "MFE_90D_pct": 108.22, "MAE_90D_pct": -20.89, "score_return_alignment_label": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE", "trigger_id": "R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224", "symbol": "004370", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -8, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 2, "policy_or_regulatory_score": 20, "valuation_repricing_score": 0, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -10, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 1, "policy_or_regulatory_score": 12, "valuation_repricing_score": 0, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["margin_bridge_score", "execution_risk_score", "downstream_cost_pressure_guard"], "component_delta_explanation": "Headline grain/food shock is demoted when there is no direct volume/repricing route or when the shock is mainly input-cost pressure.", "MFE_90D_pct": 1.69, "MAE_90D_pct": -19.35, "score_return_alignment_label": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["theme_beta_high_MAE", "downstream_input_cost_false_positive", "price_only_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R12
completed_loop = 13
next_round = R13
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web repository files checked:

```text
Songdaiki/stock-web atlas/manifest.json
Songdaiki/stock-web atlas/schema.json
Songdaiki/stock-web atlas/symbol_profiles/005/005860.json
Songdaiki/stock-web atlas/symbol_profiles/218/218150.json
Songdaiki/stock-web atlas/symbol_profiles/027/027710.json
Songdaiki/stock-web atlas/symbol_profiles/004/004370.json
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/004/004370/2022.csv
```

External historical-event context used only to anchor trigger_date/evidence timing:

```text
AP: Global food prices in 2022 hit record high amid drought, war.
Axios: Russian invasion of Ukraine fuels record food prices.
FAO/UN-food-price-index context as cited by AP/Axios search results.
```

No investment recommendation language is intended or implied.
