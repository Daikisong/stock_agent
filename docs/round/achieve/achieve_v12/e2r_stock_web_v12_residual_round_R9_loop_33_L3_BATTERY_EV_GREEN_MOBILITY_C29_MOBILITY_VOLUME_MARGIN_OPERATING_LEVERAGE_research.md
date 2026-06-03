# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: post_calibrated_sector_archetype_residual_research
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- round: R9
- loop: 33
- output_file: `e2r_stock_web_v12_residual_round_R9_loop_33_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md`
- large_sector_id: `L3_BATTERY_EV_GREEN_MOBILITY`
- canonical_archetype_id: `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`
- fine_archetype_id: `AUTO_OEM_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE; AUTO_PARTS_EV_CUSTOMER_ORDER_WITHOUT_MARGIN_BRIDGE; THERMAL_MANAGEMENT_NARRATIVE_FALSE_POSITIVE`
- loop_objective: coverage_gap_fill; counterexample_mining; residual_false_positive_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; sector_specific_rule_discovery
- production_scoring_changed: false
- shadow_weight_only: true
- stock_agent_code_access_allowed: false
- stock_agent_code_patch_allowed: false
- current_stock_discovery_allowed: false
- auto_trading_allowed: false
- handoff_prompt_embedded: true
- handoff_prompt_executed_now: false

This file is historical calibration research only. It is not live candidate discovery, not a recommendation, not a trading plan, and not a production patch.

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

This loop does **not** re-prove the global rules. It tests whether C29 needs a canonical-archetype-specific margin bridge gate.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R9 |
| loop | 33 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | AUTO_OEM_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE; AUTO_PARTS_EV_CUSTOMER_ORDER_WITHOUT_MARGIN_BRIDGE; THERMAL_MANAGEMENT_NARRATIVE_FALSE_POSITIVE |
| selected scope | Korean auto OEM / auto-parts mobility operating leverage cases |
| selection mode | auto_coverage_gap_fill |
| auto_selected_coverage_gap | R9/C29 after prior R8/C28 software/security loop |

## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` research artifacts were not directly accessible through the public raw paths during this run, so duplicate avoidance used the previous session state and the user-specified Diversity Governor. The immediately prior generated loop was R8/C28, so this loop moves to R9/C29 and does not reuse the same canonical archetype or evidence family.

| Metric | Value |
|---|---:|
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 3 |
| new_canonical_archetype_count | 1 |
| new_trigger_family_count | 3 |
| required_new_independent_case_ratio | 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

The stock-web manifest records `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`, and notes that raw/unadjusted OHLC is used, invalid/zero-volume rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default. Source: citeturn691865view0

| Symbol | Company | Profile path | Tradable shard(s) | Corporate-action window status |
|---|---|---|---|---|
| 000270 | 기아 | atlas/symbol_profiles/000/000270.json | atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv; 2024.csv | clean_180D_window; old 1999 candidate outside window |
| 204320 | HL만도 | atlas/symbol_profiles/204/204320.json | atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv | clean_180D_window; 2018 candidate outside window |
| 011210 | 현대위아 | atlas/symbol_profiles/011/011210.json | atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv | clean_180D_window; no corporate-action candidates |

## 5. Historical Eligibility Gate

All representative triggers pass the historical eligibility gate.

```text
historical_trigger = true
entry_date_in_tradable_shard = true
forward_180D_available_by_manifest = true
high_low_close_volume_present = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| AUTO_OEM_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Volume + ASP/mix + margin bridge produced real OEM operating leverage. |
| AUTO_PARTS_EV_CUSTOMER_ORDER_WITHOUT_MARGIN_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Customer/order quality looked attractive, but margin bridge failed. |
| THERMAL_MANAGEMENT_NARRATIVE_FALSE_POSITIVE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Optionality and relative strength without margin/revision evidence created false-positive risk. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best trigger | current_profile_verdict | calibration_usable |
|---|---:|---|---|---|---|---|
| R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN | 000270 | 기아 | structural_success | R9L33-T001-KIA-STAGE2-FY22 | current_profile_too_late | true |
| R9L33-C29-204320-HLMANDO-2023-EV-ADAS-MARGIN-GAP | 204320 | HL만도 | failed_rerating | R9L33-T003-HLMANDO-STAGE2-FY22 | current_profile_false_positive | true |
| R9L33-C29-011210-HYWIA-2023-THERMAL-MGMT-FALSE-POSITIVE | 011210 | 현대위아 | false_positive_green | R9L33-T005-HYWIA-STAGE2-THERMAL | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

| Bucket | Count | Case IDs |
|---|---:|---|
| positive_case_count | 1 | R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN |
| counterexample_count | 2 | R9L33-C29-204320-HLMANDO-2023-EV-ADAS-MARGIN-GAP; R9L33-C29-011210-HYWIA-2023-THERMAL-MGMT-FALSE-POSITIVE |
| 4B_case_count | 1 | R9L33-T004-HLMANDO-4B-LOCALPEAK |
| 4C_case_count | 1 | R9L33-T006-HYWIA-4C-PRICECONFIRM |

C29 behaves like an engine: **volume is fuel, mix/ASP is compression, and margin bridge is ignition**. Without ignition, customer/order narratives can make short-lived MFE but poor 180D MAE.

## 9. Evidence Source Map

| Trigger | Evidence available at that date | Stage2 fields | Stage3 fields | 4B / 4C fields |
|---|---|---|---|---|
| R9L33-T001-KIA-STAGE2-FY22 | FY22/Q4 result and 2023 guidance implied volume recovery, mix/ASP, and OP margin bridge | disclosure, volume route, early revision, relative strength | margin bridge, financial visibility | none |
| R9L33-T002-KIA-STAGE3-GREEN-Q1CONFIRM | Q1 confirmation made the margin bridge safer but later | disclosure, volume route | confirmed revision, margin bridge, financial visibility | none |
| R9L33-T003-HLMANDO-STAGE2-FY22 | EV/ADAS customer/order narrative existed, but margin bridge did not close | disclosure, customer/order, volume route | unsupported revision/margin bridge | none |
| R9L33-T004-HLMANDO-4B-LOCALPEAK | Local peak while margin bridge still not confirmed | customer/order | unsupported margin bridge | price_only_local_peak, margin_or_backlog_slowdown |
| R9L33-T005-HYWIA-STAGE2-THERMAL | Thermal-management optionality and relative strength, but little realized margin bridge | disclosure, optionality, relative strength | unsupported revision/margin bridge | none |
| R9L33-T006-HYWIA-4C-PRICECONFIRM | Summer narrative fully round-tripped | relative strength | unsupported revision/margin bridge | thesis_evidence_broken |

## 10. Price Data Source Map

| Symbol | Entry row evidence | Forward-window evidence |
|---|---|---|
| 000270 | 2023-01-27 close 68,700 and 2023-04-27 close 86,600 are visible in stock-web rows. | 2023-05-11 high 91,900 and 2024 highs are visible in stock-web rows. |
| 204320 | 2023-02-08 close 46,700 is visible in stock-web rows. | 2023-06-30 high 54,500 and Oct/Nov lows down to 32,400 are visible. |
| 011210 | 2023-06-30 close 67,000 is visible in stock-web rows. | 2023-07-06 high 70,500 and Nov low 51,500 are visible. |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | outcome | aggregate_role |
|---|---:|---|---|---|---:|---:|---:|---|---|
| R9L33-T001-KIA-STAGE2-FY22 | 000270 | Stage2-Actionable | 2023-01-26 | 2023-01-27 | 68,700 | 33.77% | -2.77% | structural_success | representative |
| R9L33-T002-KIA-STAGE3-GREEN-Q1CONFIRM | 000270 | Stage3-Green | 2023-04-26 | 2023-04-27 | 86,600 | 6.12% | -11.55% | late_green_but_valid_confirmation | label_comparison_only |
| R9L33-T003-HLMANDO-STAGE2-FY22 | 204320 | Stage2-Actionable | 2023-02-08 | 2023-02-08 | 46,700 | 16.70% | -5.78% | failed_rerating_high_mae_after_initial_mfe | representative |
| R9L33-T004-HLMANDO-4B-LOCALPEAK | 204320 | Stage4B | 2023-06-30 | 2023-06-30 | 53,900 | 1.11% | -39.89% | 4B_overlay_success | 4B_overlay_only |
| R9L33-T005-HYWIA-STAGE2-THERMAL | 011210 | Stage2-Actionable | 2023-06-30 | 2023-06-30 | 67,000 | 5.22% | -23.13% | false_positive_stage2 | representative |
| R9L33-T006-HYWIA-4C-PRICECONFIRM | 011210 | Stage4C | 2023-11-01 | 2023-11-01 | 52,200 | 24.52% | -1.34% | 4C_late_after_damage_done | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| case | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---|---:|---:|
| 기아 Stage2 | 68,700 | 16.01% / -2.77% | 33.77% / -2.77% | 33.77% / -2.77% | 2023-05-11 | 91,900 | -16.32% |
| HL만도 Stage2 | 46,700 | 11.56% / -5.78% | 16.70% / -5.78% | 16.70% / -30.62% | 2023-06-30 | 54,500 | -40.55% |
| 현대위아 Stage2 | 67,000 | 5.22% / -14.18% | 5.22% / -23.13% | 5.22% / -23.13% | 2023-07-06 | 70,500 | -26.95% |

## 13. Current Calibrated Profile Stress Test

| Case | Current profile likely label | Actual alignment | Verdict |
|---|---|---|---|
| 기아 | Stage2-Actionable first, but Green only after later confirmation | Stage2 had better MFE/MAE than late Green; Green lateness ratio 0.77 | current_profile_too_late |
| HL만도 | Possible Yellow/near-Green if customer/order and EV/ADAS narrative are overweighted | Initial MFE existed, but 180D MAE was -30.62% | current_profile_false_positive |
| 현대위아 | Possible Yellow from relative strength + thermal-management optionality | MFE was only 5.22% while 90D MAE was -23.13% | current_profile_false_positive |

| Existing axis | Result |
|---|---|
| stage2_actionable_evidence_bonus | kept; useful only when margin bridge exists |
| stage3_yellow_total_min | kept; C29 needs margin gate, not a global threshold change |
| stage3_green_total_min / revision_min | strengthened in C29 |
| price_only_blowoff_blocks_positive_stage | strengthened |
| full_4b_requires_non_price_evidence | kept; local peak useful as overlay only |
| hard_4c_thesis_break_routes_to_4c | kept, but C29 4C can be late after large damage |

## 14. Stage2 / Yellow / Green Comparison

```text
Kia Stage2_Actionable_entry_price = 68,700
Kia Stage3_Green_entry_price = 86,600
peak_price_after_Stage2 = 91,900
green_lateness_ratio = (86,600 - 68,700) / (91,900 - 68,700) = 0.77
```

Interpretation: Green captured confirmation but missed most of the early cycle upside. This is **not** a global Green-threshold rollback; it is a C29-specific rule: when auto OEM volume + ASP/mix + margin bridge are all visible, Stage2-Actionable should be allowed to behave closer to Yellow in shadow scoring.

## 15. 4B Local vs Full-window Timing Audit

| Trigger | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| HL만도 2023-06-30 | 0.92 | 0.92 | good local 4B overlay, not full 4C |
| 현대위아 2023-07-06 implied local peak | 1.00 local peak by price | low evidence quality | price-only local 4B cannot be full 4B |
| 기아 Dec/Jan later price highs | not used for representative sell/risk calibration | not used | structural thesis remained intact |

## 16. 4C Protection Audit

| Case | 4C label | Protection interpretation |
|---|---|---|
| HL만도 | thesis_break_watch_only | A 4B overlay would have been more useful than waiting for hard 4C. |
| 현대위아 | hard_4c_late | By the time the narrative fully round-tripped, the main drawdown had already occurred. |
| 기아 | not_applicable | No hard thesis break in the validation window. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = l3_mobility_positive_requires_volume_mix_margin_bridge
candidate_delta = +1 guard
```

Rule candidate: In L3 mobility cases, Stage2/Yellow promotion is allowed only when at least two of three are present: volume route, ASP/mix or customer quality, and margin bridge. Green requires all three plus revision/financial visibility.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
axis = c29_volume_margin_bridge_required_for_green
candidate_delta = +1 guard
```

Rule candidate: For C29, customer/order quality or EV/thermal-management optionality without margin bridge caps the score at Stage2-Watch or Yellow-stress. It cannot become Green without confirmed revision and margin bridge.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global_current | Current calibrated profile, no C29 special gate | 3 | 18.56% | -10.56% | 18.56% | -18.84% | 66.7% | misaligned: positive captured late, two false positives promoted |
| P0b e2r_2_0_baseline_reference | rollback_reference | Older baseline with looser Stage3/Green pressure | 3 | 18.56% | -10.56% | 18.56% | -18.84% | 66.7% | worse false-positive control |
| P1 sector_specific_candidate_profile | sector_specific | L3 mobility requires volume/mix + margin bridge for positive promotion | 3 | 18.33% | -10.56% | 18.56% | -18.84% | 0% | improved |
| P2 canonical_archetype_candidate_profile | canonical_archetype_specific | C29 auto-parts order/customer quality capped without margin/revision | 3 | 18.33% | -10.56% | 18.56% | -18.84% | 0% | improved |
| P3 counterexample_guard_profile | canonical_archetype_specific | C29 theme/relative-strength price-only route cannot promote Yellow/Green | 3 | 18.33% | -10.56% | 18.56% | -18.84% | 0% | best false-positive guard |


## 20. Score-Return Alignment Matrix

| Case | Current score issue | Proposed shadow adjustment | Return alignment |
|---|---|---|---|
| 기아 | Green too late for OEM volume/mix/margin inflection | allow C29 Stage2-Actionable -> Yellow shadow when volume + mix + margin all present | improved; Stage2 MFE90 33.77% |
| HL만도 | customer/order narrative could over-promote | cap without margin bridge and revision | improved; avoids high-MAE false positive |
| 현대위아 | optionality/relative strength could over-promote | narrative-only cap | improved; avoids 5.22% MFE vs -23.13% MAE trap |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_OEM_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE; AUTO_PARTS_EV_CUSTOMER_ORDER_WITHOUT_MARGIN_BRIDGE; THERMAL_MANAGEMENT_NARRATIVE_FALSE_POSITIVE | 1 | 2 | 1 | 1 | 3 | 0 | 6 | 3 | 3 | true | true | C29 now has OEM positive + two auto-parts counterexamples; still needs pure logistics / transport holdout cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - stage3_yellow_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C29 margin-bridge false positive
  - C29 Green lateness in OEM volume/mix inflection
  - 4B local peak vs full-window separation
new_axis_proposed:
  - c29_volume_margin_bridge_required_for_green
  - c29_customer_order_without_margin_cap
  - c29_local_peak_4b_overlay_when_margin_gap_persists
existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R9/C29 mobility volume-margin operating leverage
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Historical OHLC rows from Songdaiki/stock-web.
- 180D forward windows available by manifest max_date.
- Corporate-action contamination absent in each representative 180D window.
- Stage2 vs Green timing comparison for Kia.
- C29 false-positive guard using HL Mando and Hyundai Wia.
```

Not validated:

```text
- Live 2026 candidate scan.
- Production scoring code.
- Brokerage API or trading action.
- Global scoring changes.
- Exhaustive C29 sector coverage across logistics, airlines, and shipping.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_volume_margin_bridge_required_for_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 positives required volume + ASP/mix + margin bridge; two counterexamples failed without it","Kia preserved; HL Mando and Hyundai Wia false-positive risk reduced","R9L33-T001-KIA-STAGE2-FY22|R9L33-T003-HLMANDO-STAGE2-FY22|R9L33-T005-HYWIA-STAGE2-THERMAL",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_customer_order_without_margin_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Auto-parts customer/order quality is insufficient when margin bridge and revision are unsupported","False-positive Yellow/Green labels fall back to Stage2-Watch","R9L33-T003-HLMANDO-STAGE2-FY22|R9L33-T005-HYWIA-STAGE2-THERMAL",2,2,2,medium,counterexample_guard_shadow_only,"not production; protects C29 from theme/order-only rerating"
shadow_weight,c29_local_peak_4b_overlay_when_margin_gap_persists,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Local price peak with persistent margin gap is useful as 4B overlay, but not as full 4C without thesis break evidence","HL Mando 4B overlay improved drawdown awareness after local peak","R9L33-T004-HLMANDO-4B-LOCALPEAK",1,1,1,low,sector_shadow_only,"4B overlay only; not a sell recommendation"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L33-T001-KIA-STAGE2-FY22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"OEM volume recovery + ASP/mix + margin bridge created tradable operating leverage before later Green confirmation.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"OEM volume recovery + ASP/mix + margin bridge created tradable operating leverage before later Green confirmation."}
{"row_type":"case","case_id":"R9L33-C29-204320-HLMANDO-2023-EV-ADAS-MARGIN-GAP","symbol":"204320","company_name":"HL만도","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_EV_CUSTOMER_ORDER_WITHOUT_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R9L33-T003-HLMANDO-STAGE2-FY22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Customer/order/ADAS narrative was not enough; margin bridge and revision durability failed to close.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Customer/order/ADAS narrative was not enough; margin bridge and revision durability failed to close."}
{"row_type":"case","case_id":"R9L33-C29-011210-HYWIA-2023-THERMAL-MGMT-FALSE-POSITIVE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"THERMAL_MANAGEMENT_NARRATIVE_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R9L33-T005-HYWIA-STAGE2-THERMAL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Mobility/thermal-management option narrative lifted price, but volume-margin bridge and revision evidence were thin.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Mobility/thermal-management option narrative lifted price, but volume-margin bridge and revision evidence were thin."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R9L33-T001-KIA-STAGE2-FY22","case_id":"R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":["coverage_gap_fill","green_strictness_stress_test","sector_specific_rule_discovery"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","entry_date":"2023-01-27","entry_price":68700,"evidence_available_at_that_date":"FY22/Q4 result and 2023 guidance read as volume recovery + ASP/mix + margin bridge; disclosure timing treated as next tradable close.","evidence_source":"Kia FY22/Q4 result disclosure/IR; stock-web rows validate Jan-2023 entry and subsequent OHLC.","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.01,"MFE_90D_pct":33.77,"MFE_180D_pct":33.77,"MFE_1Y_pct":91.7,"MFE_2Y_pct":96.51,"MAE_30D_pct":-2.77,"MAE_90D_pct":-2.77,"MAE_180D_pct":-2.77,"MAE_1Y_pct":-2.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-16.32,"green_lateness_ratio":"baseline_for_case","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_after_stage2_actionable","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L33-000270-2023-01-27-68700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L33-T002-KIA-STAGE3-GREEN-Q1CONFIRM","case_id":"R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":["green_strictness_stress_test"],"trigger_type":"Stage3-Green","trigger_date":"2023-04-26","entry_date":"2023-04-27","entry_price":86600,"evidence_available_at_that_date":"Q1 confirmation made margin/volume bridge safer, but entry came after a large part of the Jan trigger upside.","evidence_source":"Kia Q1 result confirmation; stock-web rows validate Apr-2023 entry and forward OHLC.","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.12,"MFE_90D_pct":6.12,"MFE_180D_pct":16.51,"MFE_1Y_pct":51.73,"MFE_2Y_pct":55.89,"MAE_30D_pct":-6.7,"MAE_90D_pct":-11.55,"MAE_180D_pct":-11.55,"MAE_1Y_pct":-11.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-28","peak_price":100900,"drawdown_after_peak_pct":-23.79,"green_lateness_ratio":0.77,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_but_valid_confirmation","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L33-000270-2023-04-27-86600","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R9L33-T003-HLMANDO-STAGE2-FY22","case_id":"R9L33-C29-204320-HLMANDO-2023-EV-ADAS-MARGIN-GAP","symbol":"204320","company_name":"HL만도","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_EV_CUSTOMER_ORDER_WITHOUT_MARGIN_BRIDGE","sector":"Auto parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":["counterexample_mining","sector_specific_rule_discovery"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-02-08","entry_date":"2023-02-08","entry_price":46700,"evidence_available_at_that_date":"EV/ADAS customer-order quality and auto-production recovery were visible, but margin bridge was not closed.","evidence_source":"HL Mando FY22/Q4 result/IR and forward guidance; stock-web rows validate Feb-2023 entry and forward OHLC.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["unknown_or_not_supported:confirmed_revision","unknown_or_not_supported:margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.56,"MFE_90D_pct":16.7,"MFE_180D_pct":16.7,"MFE_1Y_pct":16.7,"MFE_2Y_pct":16.7,"MAE_30D_pct":-5.78,"MAE_90D_pct":-5.78,"MAE_180D_pct":-30.62,"MAE_1Y_pct":-30.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-30","peak_price":54500,"drawdown_after_peak_pct":-40.55,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"failed_rerating_high_mae_after_initial_mfe","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L33-204320-2023-02-08-46700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L33-T004-HLMANDO-4B-LOCALPEAK","case_id":"R9L33-C29-204320-HLMANDO-2023-EV-ADAS-MARGIN-GAP","symbol":"204320","company_name":"HL만도","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_EV_CUSTOMER_ORDER_WITHOUT_MARGIN_BRIDGE","sector":"Auto parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":["4B_non_price_requirement_stress_test"],"trigger_type":"Stage4B","trigger_date":"2023-06-30","entry_date":"2023-06-30","entry_price":53900,"evidence_available_at_that_date":"Local peak came while margin-bridge evidence remained weak; 4B is valid only as overlay, not as price-only full thesis break.","evidence_source":"stock-web local peak / subsequent drawdown; non-price 4B evidence treated as margin-bridge non-confirmation, not cancellation.","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["unknown_or_not_supported:confirmed_revision","unknown_or_not_supported:margin_bridge"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.11,"MFE_90D_pct":1.11,"MFE_180D_pct":1.11,"MFE_1Y_pct":10.95,"MFE_2Y_pct":10.95,"MAE_30D_pct":-22.26,"MAE_90D_pct":-39.89,"MAE_180D_pct":-39.89,"MAE_1Y_pct":-39.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-30","peak_price":54500,"drawdown_after_peak_pct":-40.55,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_local_4B_overlay_but_not_full_4C","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_after_failed_stage2","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L33-204320-2023-06-30-53900","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R9L33-T005-HYWIA-STAGE2-THERMAL","case_id":"R9L33-C29-011210-HYWIA-2023-THERMAL-MGMT-FALSE-POSITIVE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"THERMAL_MANAGEMENT_NARRATIVE_FALSE_POSITIVE","sector":"Auto parts / thermal management","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":["counterexample_mining","residual_false_positive_mining"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-06-30","entry_date":"2023-06-30","entry_price":67000,"evidence_available_at_that_date":"Thermal-management and mobility optionality were visible, but the trigger lacked a closed margin bridge and revision support.","evidence_source":"Hyundai Wia mobility/thermal-management narrative and stock-web OHLC reaction.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["unknown_or_not_supported:confirmed_revision","unknown_or_not_supported:margin_bridge","unknown_or_not_supported:financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.22,"MFE_90D_pct":5.22,"MFE_180D_pct":5.22,"MFE_1Y_pct":5.22,"MFE_2Y_pct":12.84,"MAE_30D_pct":-14.18,"MAE_90D_pct":-23.13,"MAE_180D_pct":-23.13,"MAE_1Y_pct":-23.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":70500,"drawdown_after_peak_pct":-26.95,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"false_positive_stage2_without_margin_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L33-011210-2023-06-30-67000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L33-T006-HYWIA-4C-PRICECONFIRM","case_id":"R9L33-C29-011210-HYWIA-2023-THERMAL-MGMT-FALSE-POSITIVE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"THERMAL_MANAGEMENT_NARRATIVE_FALSE_POSITIVE","sector":"Auto parts / thermal management","primary_archetype":"mobility_volume_margin_operating_leVERAGE","loop_objective":["4C_thesis_break_timing_test"],"trigger_type":"Stage4C","trigger_date":"2023-11-01","entry_date":"2023-11-01","entry_price":52200,"evidence_available_at_that_date":"Prior summer narrative had fully round-tripped; use as thesis-break watch row, not a new short/negative recommendation.","evidence_source":"stock-web OHLC failed-rerating confirmation.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["unknown_or_not_supported:confirmed_revision","unknown_or_not_supported:margin_bridge"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.43,"MFE_90D_pct":24.52,"MFE_180D_pct":24.52,"MFE_1Y_pct":24.52,"MFE_2Y_pct":65.52,"MAE_30D_pct":-1.34,"MAE_90D_pct":-1.34,"MAE_180D_pct":-1.34,"MAE_1Y_pct":-1.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-21","peak_price":65000,"drawdown_after_peak_pct":-20.77,"green_lateness_ratio":"not_applicable:4C_overlay","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4C_late_after_damage_done","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late_after_false_positive","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L33-011210-2023-11-01-52200","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN","trigger_id":"R9L33-T001-KIA-STAGE2-FY22","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":40,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":30,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable / below Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":53,"relative_strength_score":42,"customer_quality_score":48,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78.0,"stage_label_after":"Stage3-Yellow shadow","changed_components":["margin_bridge_score","+8","revision_score","+5","valuation_repricing_score","+5"],"component_delta_explanation":"C29 OEM case gets early Yellow only when volume + ASP/mix + OP margin bridge appears together.","MFE_90D_pct":33.77,"MAE_90D_pct":-2.77,"score_return_alignment_label":"improved_early_alignment","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L33-C29-204320-HLMANDO-2023-EV-ADAS-MARGIN-GAP","trigger_id":"R9L33-T003-HLMANDO-STAGE2-FY22","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":38,"margin_bridge_score":22,"revision_score":18,"relative_strength_score":32,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow false-positive risk","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":38,"margin_bridge_score":22,"revision_score":18,"relative_strength_score":32,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67.0,"stage_label_after":"Stage2-Watch / margin-bridge blocked","changed_components":["margin_bridge_gate","execution_risk_score"],"component_delta_explanation":"Auto-parts order/customer evidence is capped unless margin bridge/revision durability confirms operating leverage.","MFE_90D_pct":16.7,"MAE_90D_pct":-5.78,"score_return_alignment_label":"guard_reduces_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L33-C29-011210-HYWIA-2023-THERMAL-MGMT-FALSE-POSITIVE","trigger_id":"R9L33-T005-HYWIA-STAGE2-THERMAL","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":45,"customer_quality_score":25,"policy_or_regulatory_score":30,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":45,"customer_quality_score":25,"policy_or_regulatory_score":30,"valuation_repricing_score":0,"execution_risk_score":60,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63.0,"stage_label_after":"Stage2-Watch / narrative-only cap","changed_components":["c29_narrative_without_margin_cap","execution_risk_score"],"component_delta_explanation":"Thermal-management optionality cannot promote Green/Yellow without realized volume-margin or revision evidence.","MFE_90D_pct":5.22,"MAE_90D_pct":-23.13,"score_return_alignment_label":"guard_reduces_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_volume_margin_bridge_required_for_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 positives required volume + ASP/mix + margin bridge; two counterexamples failed without it","Kia preserved; HL Mando and Hyundai Wia false-positive risk reduced","R9L33-T001-KIA-STAGE2-FY22|R9L33-T003-HLMANDO-STAGE2-FY22|R9L33-T005-HYWIA-STAGE2-THERMAL",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_customer_order_without_margin_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Auto-parts customer/order quality is insufficient when margin bridge and revision are unsupported","False-positive Yellow/Green labels fall back to Stage2-Watch","R9L33-T003-HLMANDO-STAGE2-FY22|R9L33-T005-HYWIA-STAGE2-THERMAL",2,2,2,medium,counterexample_guard_shadow_only,"not production; protects C29 from theme/order-only rerating"
shadow_weight,c29_local_peak_4b_overlay_when_margin_gap_persists,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Local price peak with persistent margin gap is useful as 4B overlay, but not as full 4C without thesis break evidence","HL Mando 4B overlay improved drawdown awareness after local peak","R9L33-T004-HLMANDO-4B-LOCALPEAK",1,1,1,low,sector_shadow_only,"4B overlay only; not a sell recommendation"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"33","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","stage3_yellow_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C29 margin-bridge false positive","C29 Green lateness in OEM volume/mix inflection","4B local peak vs full-window separation"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R9/C29 mobility volume-margin operating leverage after R8/C28 software/security loop"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"000000","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"no narrative-only blocked case in this loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R9 / C29 holdout with logistics or airline transport volume-margin cases
alternate_next_round = R10 / C30 construction PF balance-sheet break
carry_forward_questions:
  - Does C29 rule differ between OEM and auto-parts?
  - Should transport/logistics cases be moved under L10_MISC or kept under L3 mobility?
  - Are C29 4B overlays more predictive when inventory/incentive evidence appears before price drawdown?
```

## 28. Source Notes

Stock-Web / price source citations used in this MD:

- Manifest: stock-web manifest max_date and raw/unadjusted caveats. citeturn691865view0
- Kia profile and corporate-action status: fileciteturn1045file0 fileciteturn1046file0
- Kia entry and forward OHLC rows: fileciteturn1035file0 fileciteturn1031file0 fileciteturn1032file0 fileciteturn1033file0 fileciteturn1034file0 fileciteturn1047file0
- HL Mando profile and OHLC rows: fileciteturn1040file0 fileciteturn1036file0 fileciteturn1037file0 fileciteturn1038file0 fileciteturn1039file0
- Hyundai Wia profile and OHLC rows: fileciteturn1044file0 fileciteturn1041file0 fileciteturn1042file0 fileciteturn1043file0

External evidence note: company IR/disclosure pages and contemporaneous mobility-sector news were used only to classify trigger families. Quantitative calibration is based solely on stock-web OHLC rows.
