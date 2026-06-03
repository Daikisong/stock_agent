# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| Field | Value |
|---|---|
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| research_session | post_calibrated_sector_archetype_residual_research |
| scheduled_round | R11 |
| scheduled_loop | 14 |
| completed_round | R11 |
| completed_loop | 14 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | IRA_EV_BATTERY_ROUTE_CONGRUENCE |
| output_file | e2r_stock_web_v12_residual_round_R11_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md |
| price_source | Songdaiki/stock-web |
| stock_web_manifest_max_date | 2026-02-20 |
| production_scoring_changed | false |
| shadow_weight_only | true |
| handoff_prompt_embedded | true |
| handoff_prompt_executed_now | false |

This loop adds **3** new independent cases, **1** counterexample, and **2** residual errors for **R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT**.

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied axes tested, not re-proposed as global rules:

- `stage2_actionable_evidence_bonus = +2.0`
- `stage3_yellow_total_min = 75.0`
- `stage3_green_total_min = 87.0`
- `stage3_green_revision_min = 55.0`
- `stage3_cross_evidence_green_buffer = +1.5`
- `price_only_blowoff_blocks_positive_stage = true`
- `full_4b_requires_non_price_evidence = true`
- `hard_4c_thesis_break_routes_to_4c = true`

This MD does not change production scoring. It proposes only C31-scoped shadow rules.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 14 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | IRA_EV_BATTERY_ROUTE_CONGRUENCE |
| loop_objective | residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; coverage_gap_fill |

R11 is treated as a policy/event checkpoint rather than a sector-specific battery or auto round. The same public policy event, the U.S. Inflation Reduction Act, is tested across different Korean listed-company pass-through routes: battery cell, battery material, and finished vehicle exporter.

## 3. Previous Coverage / Duplicate Avoidance Check

The immediate prior chat artifact completed **R10 / Loop 14** and declared `next_round = R11`, `next_loop = 14`. This run therefore uses `scheduled_round = R11`, `scheduled_loop = 14`.

Duplicate avoidance:

| Check | Result |
|---|---|
| stock_agent source code opened | no |
| production scoring inferred from code | no |
| live stock discovery | no |
| same symbol + same trigger_date + same entry_date reused from prior loop | no |
| same canonical archetype allowed | yes |
| new symbols | 373220, 003670, 005380 |
| new trigger families | IRA policy positive route; IRA finished-vehicle headwind; price-only local 4B under policy narrative |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest reports FinanceData/marcap as the source, `raw_unadjusted_marcap` as the adjustment status, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14,354,401`, `raw_row_count = 15,214,118`, and `symbol_count = 5,414`. It also states that calibration shards live under `atlas/ohlcv_tradable_by_symbol_year` and that zero-volume/invalid rows are excluded from calibration shards. fileciteturn1048file0L6-L21 fileciteturn1048file0L30-L45 fileciteturn1048file0L53-L58

The schema confirms that tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs`; MFE/MAE definitions are max-high/min-low over N tradable rows; and calibration requires positive OHLCV, an entry row, at least 180 forward tradable days, and an uncontaminated 180D corporate-action window. fileciteturn1049file0L17-L28 fileciteturn1049file0L45-L68

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| Case | Symbol | Entry date | Entry row exists | >=180 trading days | Corporate-action 180D status | Calibration usable |
|---|---:|---|---|---|---|---|
| LGES IRA positive route | 373220 | 2022-08-17 | yes | yes | clean | true |
| POSCO Future M IRA positive route | 003670 | 2022-08-17 | yes | yes | clean | true |
| Hyundai Motor IRA route mismatch | 005380 | 2022-08-17 | yes | yes | clean | true |
| POSCO Future M 4B overlay | 003670 | 2023-04-19 | yes | yes | clean | true, overlay-only |

LG에너지솔루션 has no corporate-action candidate dates in the profile. fileciteturn1068file0L70-L80  
포스코퓨처엠 has corporate-action candidate dates only in 2015 and 2021, outside the 2022-08-17 and 2023-04-19 windows. fileciteturn1070file0L15-L29  
현대차 has corporate-action candidate dates only in 1998-1999, outside this window. fileciteturn1080file0L3-L11

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| IRA_EV_BATTERY_ROUTE_CONGRUENCE | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | A policy or subsidy event only promotes Stage2/3 if the company has a direct credit-capture, localization, supply-chain qualification, or customer pass-through route. |
| IRA_FINISHED_VEHICLE_ROUTE_MISMATCH | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Same legislation can be negative when final-assembly, local-content, or customer eligibility requirements exclude the firm’s current product path. |
| POLICY_NARRATIVE_PRICE_ONLY_LOCAL_4B | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | A local price peak under policy enthusiasm is 4B-watch only unless non-price deterioration exists. |

## 7. Case Selection Summary

| Case | Symbol | Company | Role | Why selected |
|---|---:|---|---|---|
| R11L14_C31_LGES_IRA_STAGE2 | 373220 | LG에너지솔루션 | structural_success | IRA route congruent for battery cell/local production narrative. |
| R11L14_C31_POSCOFUTUREM_IRA_STAGE2 | 003670 | 포스코퓨처엠 | structural_success + 4B overlay | Battery material localization route produced very high 180D MFE and later local blowoff risk. |
| R11L14_C31_HYUNDAI_IRA_HEADWIND | 005380 | 현대차 | counterexample / false positive | Same policy event was adverse or delayed for finished-vehicle exports not immediately qualifying under local assembly rules. |

## 8. Positive vs Counterexample Balance

| Metric | Count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 1 |
| 4C_case_count | 1 watch-only |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 4 |
| representative_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

## 9. Evidence Source Map

The Inflation Reduction Act was signed into law on August 16, 2022. citeturn735652news0 The clean vehicle credit rules added a North America final-assembly requirement from August 16, 2022, with later battery/mineral sourcing requirements. citeturn444794news1 Hyundai/Kia later accelerated U.S. production partly because the IRA favored domestic EV production, confirming that the immediate route for imported Korean-made EVs was not equivalent to the battery/localization route. citeturn382573news3

| Evidence field | LGES | POSCO Future M | Hyundai Motor |
|---|---|---|---|
| public_event_or_disclosure | IRA signed | IRA signed | IRA signed |
| policy_or_regulatory_optionality | positive | positive | mixed/negative |
| capacity_or_volume_route | U.S. battery production / localization route | battery-material localization/friendshoring | Georgia plant needed, but delayed |
| customer_or_order_quality | automaker/battery customer ecosystem | battery-material customer ecosystem | finished vehicle eligibility not immediate |
| legal_or_contract_risk | low at trigger | low at trigger | elevated due final-assembly eligibility mismatch |
| confirmed_revision | not used at trigger | not used at trigger | not used at trigger |

## 10. Price Data Source Map

| Symbol | Company | Profile path | Tradable shard path(s) used |
|---:|---|---|---|
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv; 2023.csv |
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | atlas/ohlcv_tradable_by_symbol_year/003/003670/2022.csv; 2023.csv |
| 005380 | 현대차 | atlas/symbol_profiles/005/005380.json | atlas/ohlcv_tradable_by_symbol_year/005/005380/2022.csv; 2023.csv |

LGES profile establishes first/last dates and 2022-2026 year files. fileciteturn1068file0L23-L49  
POSCO Future M profile establishes KOSDAQ/KOSPI history and 2022-2026 year files. fileciteturn1069file0L28-L44 fileciteturn1069file0L127-L132  
Hyundai Motor profile establishes long KOSPI history and 2022-2026 year files. fileciteturn1079file0L23-L39 fileciteturn1079file0L133-L139

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | Symbol | Trigger type | Trigger date | Entry date | Entry price | Outcome |
|---|---|---:|---|---|---|---:|---|
| T_R11L14_C31_373220_IRA_SIGNED_STAGE2A | R11L14_C31_LGES_IRA_STAGE2 | 373220 | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 453,500 | structural policy success |
| T_R11L14_C31_003670_IRA_SIGNED_STAGE2A | R11L14_C31_POSCOFUTUREM_IRA_STAGE2 | 003670 | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 158,500 | high-MFE structural success |
| T_R11L14_C31_005380_IRA_SIGNED_HEADWIND | R11L14_C31_HYUNDAI_IRA_HEADWIND | 005380 | Stage2-Watch / Counterexample | 2022-08-16 | 2022-08-17 | 190,000 | false positive if policy route ignored |
| T_R11L14_C31_003670_LOCAL_4B_2023-04-19 | R11L14_C31_POSCOFUTUREM_IRA_STAGE2 | 003670 | 4B-overlay | 2023-04-19 | 2023-04-19 | 414,000 | price-only local 4B too early |

Entry rows are visible in stock-web: LGES 2022-08-17 close 453,500; POSCO Future M 2022-08-17 close 158,500; Hyundai 2022-08-17 close 190,000. fileciteturn1071file0L9-L17 fileciteturn1075file0L27-L35 fileciteturn1081file0L27-L35

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| Symbol | Entry | Entry price | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | Peak date | Peak price | Drawdown after peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 373220 | 2022-08-17 | 453,500 | 13.78% | -5.84% | 38.70% | -8.49% | 38.70% | -8.49% | 2022-11-11 | 629,000 | -33.07% |
| 003670 | 2022-08-17 | 158,500 | 18.93% | -3.47% | 50.79% | -7.26% | 166.56% | -7.26% | 2023-04-19 | 422,500 | -30.89% |
| 005380 | 2022-08-17 | 190,000 | 7.11% | -6.58% | 7.11% | -18.68% | 9.21% | -20.79% | 2023-04-26 | 207,500 | -3.66% |

LGES 30D and 90D/180D extrema are supported by the 2022 rows showing 2022-09-16 high 516,000, 2022-10-04 low 415,000, and 2022-11-11 high 629,000. fileciteturn1071file0L29-L42 fileciteturn1071file0L57-L68

POSCO Future M rows show 2022-09-16 high 188,500, 2022-10-05 low 147,000, November highs up to 239,000, and 2023-04-19 high 422,500. fileciteturn1075file0L45-L60 fileciteturn1076file0L20-L23 fileciteturn1078file0L3-L10

Hyundai rows show 2022-09-02 high 203,500, 2022-12-20 low 154,500, 2022-12-29 low 150,500, and 2023-04-26 high 207,500. fileciteturn1081file0L40-L58 fileciteturn1082file0L47-L55 fileciteturn1084file0L13-L22

### 4B overlay trigger

| Symbol | 4B trigger | Entry price | Local peak price | Full observed peak price | local proximity | full-window proximity | Timing verdict |
|---:|---|---:|---:|---:|---:|---:|---|
| 003670 | 2023-04-19 | 414,000 | 422,500 | 694,000 | 0.968 | 0.477 | price_only_local_4B_too_early |

POSCO Future M continued to a later high of 694,000 on 2023-07-26, so the April 2023 policy-narrative blowoff was only a local peak, not a full-cycle 4B. fileciteturn1085file0L3-L13

## 13. Current Calibrated Profile Stress Test

| Case | P0 probable label | Actual price path | Current profile verdict |
|---|---|---|---|
| LGES | Stage2-Actionable / Yellow border | Strong 90D MFE with manageable MAE | current_profile_correct |
| POSCO Future M | Stage3-Yellow / structural Stage2 | Very strong 180D MFE, but later local blowoff risk | current_profile_correct |
| Hyundai Motor | Could be falsely promoted if policy bonus is generic | Low MFE and high 90D/180D MAE | current_profile_false_positive |
| POSCO Future M 4B overlay | Price-only 4B should be watch-only | April local peak did not capture full-cycle peak | current_profile_4B_too_early_if_price_only_overlay_promoted |

Answers to required stress-test questions:

1. **How would current profile judge this?** It correctly handles battery/localization routes, but can over-score finished-vehicle exporters if policy text is treated generically.
2. **Did that match MFE/MAE?** Yes for battery cell/material; no for Hyundai route mismatch.
3. **Stage2 bonus too high or low?** Correct when the pass-through route is direct; too high when final assembly/local eligibility is adverse.
4. **Yellow 75 too high or low?** Acceptable for LGES/POSCO; too permissive for generic policy-only Hyundai.
5. **Green 87/revision 55 too high or low?** Kept. None of the 2022-08-16 triggers should be Green without revision confirmation.
6. **Price-only blowoff guard?** Strengthened. POSCO April 2023 was local, not full-cycle.
7. **Full 4B non-price requirement?** Strengthened. Without non-price evidence, April 2023 POSCO should not be full 4B.
8. **Hard 4C routing?** Kept. Hyundai is a thesis-break/watch-only route mismatch, not a hard 4C liquidation/crash route.

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2 entry | Yellow entry | Green entry | green_lateness_ratio | Interpretation |
|---|---|---|---|---|---|
| LGES | 2022-08-17 | same evidence cluster | no confirmed Green trigger in this MD | not_applicable | Stage2/Yelow sufficient; Green would require later revisions. |
| POSCO Future M | 2022-08-17 | same evidence cluster | no confirmed Green trigger in this MD | not_applicable | The route was early enough; Green would be outcome-chasing if based on later price. |
| Hyundai | 2022-08-17 watch-only | should not be Yellow | should not be Green | not_applicable | Route mismatch guard prevents policy-only false positive. |

## 15. 4B Local vs Full-window Timing Audit

| Trigger | local peak proximity | full-window proximity | 4B evidence type | Verdict |
|---|---:|---:|---|---|
| T_R11L14_C31_003670_LOCAL_4B_2023-04-19 | 0.968 | 0.477 | price_only; valuation_blowoff; positioning_overheat | price_only_local_4B_too_early |

The audit preserves the calibrated global rule that price-only blowoffs do not become positive stage labels, and strengthens the C31-specific rule that policy-narrative local peaks need full-window context.

## 16. 4C Protection Audit

| Case | 4C label | Reason |
|---|---|---|
| LGES | not_applicable | No hard thesis break at trigger. |
| POSCO Future M | not_applicable | Local 4B only, no hard 4C at 2023-04-19. |
| Hyundai | thesis_break_watch_only | Policy route mismatch reduced positive eligibility, but the company later adapted via U.S. production route; not a hard liquidation/crash 4C. |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = false` for a narrow sector label because this is R11 policy/event, not a battery or auto sector round.

However, within `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`, the policy-event route rule is valid as a cross-sector policy/event shadow rule.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

### Proposed C31 route-congruence rule

For `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`, a policy/subsidy event can promote Stage2/Yellow only when at least one route-congruence condition is true:

1. The company directly captures production, investment, tax-credit, or subsidy economics.
2. The company sells a component/material into the favored domestic/friendshored supply chain.
3. The customer/product eligibility path is already credible at trigger date.
4. The event removes a policy/regulatory bottleneck rather than creating one.

If the company’s immediate product path is excluded or penalized by the policy, the event should be scored as `policy_route_mismatch_watch` or `thesis_break_watch_only`, not as Stage2-Actionable.

## 19. Before / After Backtest Comparison

| Profile | Eligible representative triggers | Avg MFE 90D | Avg MAE 90D | Avg MFE 180D | Avg MAE 180D | False positive rate | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 32.20% | -11.48% | 71.49% | -12.18% | 33.3% | good but policy-route false positive remains |
| P0b e2r_2_0_baseline_reference | 3 | 32.20% | -11.48% | 71.49% | -12.18% | 33.3% | more vulnerable to generic policy promotion |
| P1 policy-route shadow profile | 2 | 44.75% | -7.88% | 102.63% | -7.88% | 0.0% | better score-return alignment |
| P2 C31 canonical route-congruence profile | 2 | 44.75% | -7.88% | 102.63% | -7.88% | 0.0% | preferred shadow |
| P3 4B counterexample guard profile | 4 including overlay | n/a | n/a | n/a | n/a | n/a | keeps local price 4B watch-only |

## 20. Score-Return Alignment Matrix

| Case | P0 score | P0 label | Proposed score | Proposed label | Score-return alignment |
|---|---:|---|---:|---|---|
| LGES | 76 | Stage2-Actionable / Yellow border | 81 | Stage3-Yellow, not Green | aligned_positive |
| POSCO Future M | 79 | Stage3-Yellow | 84 | Stage3-Yellow / structural Stage2 promote | aligned_positive_high_MFE |
| Hyundai | 76 | false Stage2 if generic policy bonus applied | 61 | Stage2-Watch / blocked positive | improved_false_positive_control |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | IRA_EV_BATTERY_ROUTE_CONGRUENCE | 2 | 1 | 1 | 1 watch-only | 3 | 0 | 4 | 3 | 2 | false | true | C31 now has positive battery/cell, positive material, and finished-vehicle counterexample coverage. |

## 22. Residual Contribution Summary

| Field | Value |
|---|---|
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reused_case_ids | [] |
| new_symbol_count | 3 |
| new_canonical_archetype_count | 1 |
| new_fine_archetype_count | 3 compressed to one fine family |
| new_trigger_family_count | 4 |
| tested_existing_calibrated_axes | stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c |
| residual_error_types_found | policy_route_mismatch_false_positive; price_only_local_4B_too_early |
| new_axis_proposed | policy_route_congruence_score; foreign_final_assembly_or_customer_mismatch_penalty |
| existing_axis_strengthened | price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence |
| existing_axis_weakened | null |
| existing_axis_kept | Green revision strictness; hard 4C routing |
| sector_specific_rule_candidate | false |
| canonical_archetype_rule_candidate | true |
| no_new_signal_reason | null |
| loop_contribution_label | canonical_archetype_rule_candidate |
| do_not_propose_new_weight_delta | false |

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-web `tradable_raw` OHLC rows for each entry date.
- 30D/90D/180D MFE/MAE for representative triggers.
- Corporate-action caveat status from symbol profiles.
- C31 policy route-congruence residual against positive and counterexample cases.
- 4B local vs full-window split for POSCO Future M.

Not validated:

- Live 2026 candidates.
- Any stock recommendation.
- Any production scoring code.
- Broker/API trading path.
- Full 1Y/2Y quantitative calibration. 1Y/2Y fields are intentionally left `null` in machine rows for this MD and should not be used for weight updates.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,policy_route_congruence_score,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,2,+2,"C31 policy events need direct credit-capture or localization route, not generic policy enthusiasm",Keeps LGES/POSCOFUTUREM positive while blocking Hyundai false positive,T_R11L14_C31_373220_IRA_SIGNED_STAGE2A|T_R11L14_C31_003670_IRA_SIGNED_STAGE2A|T_R11L14_C31_005380_IRA_SIGNED_HEADWIND,3,3,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,foreign_final_assembly_or_customer_mismatch_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,-6,-6,"When policy eligibility excludes the company's immediate product route, do not promote Stage2/3 solely on policy text",Reduces false positive for finished-vehicle exporter under IRA final assembly mismatch,T_R11L14_C31_005380_IRA_SIGNED_HEADWIND,1,1,1,medium,canonical_shadow_only,not production
shadow_weight,price_only_local_4B_requires_full_window_context,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1.5,+0.5,Local price peak after policy narrative can be too early when full-cycle peak is still ahead,"Keeps Apr-2023 POSCOFUTUREM as watch-only 4B, not full 4B",T_R11L14_C31_003670_LOCAL_4B_2023-04-19,1,0,0,low,4B_overlay_shadow_only,strengthens existing price-only guard
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L14_C31_LGES_IRA_STAGE2","symbol":"373220","company_name":"LG에너지솔루션","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R11L14_C31_373220_IRA_SIGNED_STAGE2A","verdict":"current_profile_correct","notes":"IRA clean-energy/EV policy translated into a plausible battery-cell production-credit and localization route; clean 180D window.","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_EV_BATTERY_ROUTE_CONGRUENCE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive route aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R11L14_C31_POSCOFUTUREM_IRA_STAGE2","symbol":"003670","company_name":"포스코퓨처엠","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R11L14_C31_003670_IRA_SIGNED_STAGE2A","verdict":"current_profile_correct","notes":"Battery-material friendshoring/localization route produced large MFE but also later local blowoff risk.","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_EV_BATTERY_ROUTE_CONGRUENCE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive route aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R11L14_C31_HYUNDAI_IRA_HEADWIND","symbol":"005380","company_name":"현대차","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T_R11L14_C31_005380_IRA_SIGNED_HEADWIND","verdict":"current_profile_false_positive","notes":"Same IRA event had a negative or delayed pass-through for imported/Korea-made EVs because final assembly/localization was not immediately solved.","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_EV_BATTERY_ROUTE_CONGRUENCE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"generic policy score misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_EV_BATTERY_ROUTE_CONGRUENCE","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":["residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"T_R11L14_C31_373220_IRA_SIGNED_STAGE2A","case_id":"R11L14_C31_LGES_IRA_STAGE2","symbol":"373220","company_name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":453500,"evidence_available_at_that_date":"U.S. Inflation Reduction Act signed; battery/clean-energy manufacturing route visible, but quarterly revision confirmation not yet visible.","evidence_source":"IRA enactment and clean vehicle/energy credit public sources","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv","profile_path":"atlas/symbol_profiles/373/373220.json","MFE_30D_pct":13.78,"MFE_90D_pct":38.7,"MFE_180D_pct":38.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.84,"MAE_90D_pct":-8.49,"MAE_180D_pct":-8.49,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-11-11","peak_price":629000,"drawdown_after_peak_pct":-33.07,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_policy_success_with_drawdown","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R11L14_C31_373220_2022-08-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[]}
{"row_type":"trigger","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_EV_BATTERY_ROUTE_CONGRUENCE","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":["residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"T_R11L14_C31_003670_IRA_SIGNED_STAGE2A","case_id":"R11L14_C31_POSCOFUTUREM_IRA_STAGE2","symbol":"003670","company_name":"포스코퓨처엠","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":158500,"evidence_available_at_that_date":"IRA signed; battery-material localization/friendshoring channel visible, with no later EPS confirmation pulled forward into the trigger date.","evidence_source":"IRA enactment and EV/battery supply-chain localization sources","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2022.csv","profile_path":"atlas/symbol_profiles/003/003670.json","MFE_30D_pct":18.93,"MFE_90D_pct":50.79,"MFE_180D_pct":166.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.47,"MAE_90D_pct":-7.26,"MAE_180D_pct":-7.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-19","peak_price":422500,"drawdown_after_peak_pct":-30.89,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_policy_success_high_MFE","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R11L14_C31_003670_2022-08-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[]}
{"row_type":"trigger","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_EV_BATTERY_ROUTE_CONGRUENCE","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":["residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"T_R11L14_C31_005380_IRA_SIGNED_HEADWIND","case_id":"R11L14_C31_HYUNDAI_IRA_HEADWIND","symbol":"005380","company_name":"현대차","trigger_type":"Stage2-Watch / Counterexample","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":190000,"evidence_available_at_that_date":"IRA signed, but final-assembly and North America localization rules made the immediate route negative/delayed for Korean-built EV exports.","evidence_source":"IRA clean-vehicle eligibility / Hyundai-Kia North America production evidence","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2022.csv","profile_path":"atlas/symbol_profiles/005/005380.json","MFE_30D_pct":7.11,"MFE_90D_pct":7.11,"MFE_180D_pct":9.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.58,"MAE_90D_pct":-18.68,"MAE_180D_pct":-20.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-26","peak_price":207500,"drawdown_after_peak_pct":-3.66,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"policy_headwind_not_positive_4B","four_b_evidence_type":["legal_or_regulatory_block","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_event_false_positive_if_route_ignored","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R11L14_C31_005380_2022-08-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[]}
{"row_type":"trigger","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_EV_BATTERY_ROUTE_CONGRUENCE","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":["residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"T_R11L14_C31_003670_LOCAL_4B_2023-04-19","case_id":"R11L14_C31_POSCOFUTUREM_IRA_STAGE2","symbol":"003670","company_name":"포스코퓨처엠","trigger_type":"4B-overlay","trigger_date":"2023-04-19","entry_date":"2023-04-19","entry_price":414000,"evidence_available_at_that_date":"Local price acceleration after policy/friendshoring narrative; treated only as 4B overlay unless non-price deterioration appears.","evidence_source":"stock-web OHLC local peak audit; no production-score change","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","MFE_30D_pct":2.05,"MFE_90D_pct":67.63,"MFE_180D_pct":67.63,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-29.47,"MAE_90D_pct":-29.47,"MAE_180D_pct":-29.47,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-44.52,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.968,"four_b_full_window_peak_proximity":0.477,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"local_4B_too_early_without_non_price_evidence","current_profile_verdict":"current_profile_4B_too_early_if_price_only_overlay_promoted","same_entry_group_id":"R11L14_C31_003670_2023-04-19","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol reused for distinct 4B timing family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[]}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L14_C31_LGES_IRA_STAGE2","trigger_id":"T_R11L14_C31_373220_IRA_SIGNED_STAGE2A","symbol":"373220","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":5,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable / Stage3-Yellow border","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":5,"customer_quality_score":8,"policy_or_regulatory_score":9,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow, not Green","changed_components":["policy_route_congruence_score","+customer_quality_score"],"component_delta_explanation":"IRA route is congruent for cell/battery localization; revision still below Green gate.","MFE_90D_pct":38.7,"MAE_90D_pct":-8.49,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L14_C31_POSCOFUTUREM_IRA_STAGE2","trigger_id":"T_R11L14_C31_003670_IRA_SIGNED_STAGE2A","symbol":"003670","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":5,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow / structural Stage2 promote","changed_components":["policy_route_congruence_score","+customer_quality_score"],"component_delta_explanation":"Battery material localization is congruent, but later local blowoff remains overlay-only without non-price 4B evidence.","MFE_90D_pct":50.79,"MAE_90D_pct":-7.26,"score_return_alignment_label":"aligned_positive_high_MFE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"proposed_c31_route_guard_profile","case_id":"R11L14_C31_HYUNDAI_IRA_HEADWIND","trigger_id":"T_R11L14_C31_005380_IRA_SIGNED_HEADWIND","symbol":"005380","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"false Stage2-Actionable if generic policy bonus applied","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch / blocked positive","changed_components":["policy_route_congruence_score","foreign_final_assembly_mismatch_penalty","legal_or_contract_risk_score"],"component_delta_explanation":"Policy event is real, but immediate credit-capture route is adverse for Korean-built finished EV exports.","MFE_90D_pct":7.11,"MAE_90D_pct":-18.68,"score_return_alignment_label":"generic_policy_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,policy_route_congruence_score,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,2,+2,"C31 policy events need direct credit-capture or localization route, not generic policy enthusiasm",Keeps LGES/POSCOFUTUREM positive while blocking Hyundai false positive,T_R11L14_C31_373220_IRA_SIGNED_STAGE2A|T_R11L14_C31_003670_IRA_SIGNED_STAGE2A|T_R11L14_C31_005380_IRA_SIGNED_HEADWIND,3,3,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,foreign_final_assembly_or_customer_mismatch_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,-6,-6,"When policy eligibility excludes the company's immediate product route, do not promote Stage2/3 solely on policy text",Reduces false positive for finished-vehicle exporter under IRA final assembly mismatch,T_R11L14_C31_005380_IRA_SIGNED_HEADWIND,1,1,1,medium,canonical_shadow_only,not production
shadow_weight,price_only_local_4B_requires_full_window_context,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1.5,+0.5,Local price peak after policy narrative can be too early when full-cycle peak is still ahead,"Keeps Apr-2023 POSCOFUTUREM as watch-only 4B, not full 4B",T_R11L14_C31_003670_LOCAL_4B_2023-04-19,1,0,0,low,4B_overlay_shadow_only,strengthens existing price-only guard
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_route_mismatch_false_positive","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"all selected cases had clean 180D stock-web windows; no narrative-only trigger needed","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R11
completed_loop = 14
next_round = R12
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price rows and profiles are from `Songdaiki/stock-web`, not from live market data.
- Stock-web manifest max date is 2026-02-20; this MD does not fabricate data beyond that date.
- Public event evidence is used only to establish historical trigger timing, not to recommend any current security.
- The IRA signed-date and EV credit eligibility evidence are sourced from public web results cited above.
- All quantitative calibration uses stock-web tradable rows only.
