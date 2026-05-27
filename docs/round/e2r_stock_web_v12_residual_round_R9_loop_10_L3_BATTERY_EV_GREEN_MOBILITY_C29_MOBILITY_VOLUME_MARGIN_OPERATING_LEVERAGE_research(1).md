# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R9
loop = 10
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE_VS_EV_ADAS_PARTS_FALSE_GREEN
output_file = e2r_stock_web_v12_residual_round_R9_loop_10_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This research file is not a live candidate scan. It is a historical residual calibration study for a mobility archetype after the first Stock-Web calibration. It uses actual `Songdaiki/stock-web` OHLC rows and is designed for later batch ingestion only.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The already-applied global axes are treated as the starting profile, not as new discoveries. This loop tests whether C29 needs a more specific split between OEM-level hybrid/export operating leverage and parts-level EV/ADAS narrative without margin confirmation.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| Round | R9 |
| Sector | 모빌리티·운송·레저, mapped to L3 for auto/hybrid/EV mobility |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE_VS_EV_ADAS_PARTS_FALSE_GREEN |
| loop_objective | counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed calibration ingest summary shows prior coverage across R1-R13 and loops 1-9, with R9 already represented but still appropriate for v12 residual expansion when the case set adds new symbols, trigger families, or counterexamples. The summary also shows a large number of rejected rows caused by invalid price source/basis/status and missing MFE/MAE, so this v12 file keeps explicit `Songdaiki/stock-web`, `tradable_raw`, and `raw_unadjusted_marcap` fields in every machine-readable row. fileciteturn55file0

Duplicate avoidance decision:

```text
selected_gap = R9/C29 OEM hybrid-export margin leverage vs EV/ADAS-parts false Green
avoid_repeating = same R1/R2 HBM/grid/defense cases; same C21/C23/C26 loops from prior v12 outputs
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
reuse_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest reports `FinanceData/marcap` as the upstream source, `raw_unadjusted_marcap` as the price adjustment status, `1995-05-02` to `2026-02-20` as the available date range, 14,354,401 tradable rows, 15,214,118 raw rows, and the calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn57file0 The schema defines tradable shard columns `d,o,h,l,c,v,a,mc,s,m`, raw shard columns with additional `rs`, and MFE/MAE as max-high/min-low from entry through N tradable rows divided by entry close. fileciteturn58file0

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| Symbol | Company | Profile path | Entry window | 180D forward window | Corporate-action window status | Eligibility |
|---|---|---|---|---|---|---|
| 005380 | 현대차 | atlas/symbol_profiles/005/005380.json | 2024-01-26 | Available within Stock-Web max date | Clean 2024 180D window; historical profile has old pre-2000 corporate-action candidates only | usable |
| 000270 | 기아 | atlas/symbol_profiles/000/000270.json | 2024-01-26 | Available within Stock-Web max date | Clean 2024 180D window; historical profile has old pre-2000 corporate-action candidates only | usable |
| 204320 | HL만도 | atlas/symbol_profiles/204/204320.json | 2024-06-05 | Available through 2025 data | Clean 2024-2025 180D window; only corporate-action candidate in 2018 | usable |

Profile validation notes: Hyundai Motor, Kia, and HL Mando all have active-like profiles and current/latest rows through 2026-02-20; their profile files list historical corporate-action candidates outside the 2024-2025 calibration windows used here. fileciteturn59file0turn60file0turn61file0

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM volume/mix/export margin bridge converts into ROE/EPS visibility and price rerating. |
| EV_ADAS_PARTS_FALSE_GREEN | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Parts narrative can look like operating leverage, but lacks confirmed margin/revision bridge. |
| OEM_VALUEUP_PRICE_ONLY_4B_OVERLAY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Strong OEM run-up may create local price peak, but full 4B needs non-price slowdown/valuation evidence. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | Why selected |
|---|---|---|---|---|---|---|---|
| R9L10-C29-HYUNDAI-2024 | 005380 | 현대차 | structural_success | positive | Stage2-Actionable 2024-01-25 -> 2024-01-26 close | current_profile_correct | OEM hybrid/export margin and shareholder-return evidence preceded a large MFE path. |
| R9L10-C29-KIA-2024 | 000270 | 기아 | structural_success | positive | Stage2-Actionable 2024-01-25 -> 2024-01-26 close | current_profile_correct | Similar OEM operating leverage but Green was materially later than Stage2. |
| R9L10-C29-HLMANDO-2024 | 204320 | HL만도 | false_positive_green | counterexample | Stage3-Green-like 2024-06-05 -> 2024-06-05 close | current_profile_false_positive | Parts/ADAS narrative and price breakout lacked durable revision/margin bridge and then produced severe MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 6
representative_trigger_count = 3
```

The positive side is two OEM cases; the counterexample side is a component supplier case. The distinction is intentionally inside the same canonical C29 cell. This avoids making C29 too broad: OEM operating leverage with confirmed margin/revision behaves differently from supplier narrative momentum without margin closure.

## 9. Evidence Source Map

| case_id | trigger_type | trigger_date | evidence_available_at_that_date | stage2_evidence_fields | stage3_evidence_fields | 4B/4C evidence |
|---|---|---|---|---|---|---|
| HYUNDAI | Stage2-Actionable | 2024-01-25 | 2023/4Q earnings, high operating profit base, hybrid/export mix, shareholder-return/value-up attention | public_event_or_disclosure; relative_strength; capacity_or_volume_route; early_revision_signal | margin_bridge; financial_visibility; multiple_public_sources | later 4B overlay: price_only_local_peak + positioning_overheat |
| KIA | Stage2-Actionable | 2024-01-25 | 2023 earnings/dividend surprise and margin resilience | public_event_or_disclosure; relative_strength; capacity_or_volume_route; early_revision_signal | confirmed_revision; margin_bridge; financial_visibility | later 4B watch only; no hard thesis break |
| HLMANDO | False Green candidate | 2024-06-05 | Parts/ADAS/EV narrative and price breakout; insufficient durable margin/revision confirmation | relative_strength; customer_or_order_quality | weak/unsupported confirmed_revision; incomplete margin_bridge | downside became thesis-break watch, not hard 4C |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | entry_price | Source rows used |
|---|---|---|---:|---:|---|
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json | 2024-01-26 | 187300 | 2024 rows show entry close, June peak, and post-peak drawdown. fileciteturn62file0turn63file0 |
| 000270 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | atlas/symbol_profiles/000/000270.json | 2024-01-26 | 94400 | 2024 rows show entry close, June peak, and post-peak drawdown. fileciteturn64file0turn65file0 |
| 204320 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | atlas/symbol_profiles/204/204320.json | 2024-06-05 | 49600 | 2024-2025 rows show breakout entry, 90D/180D downside, and partial recovery. fileciteturn66file0turn67file0turn68file0 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | Representative? | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|
| R9L10-C29-HYUNDAI-S2-20240125 | HYUNDAI | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 187300 | true | current_profile_correct |
| R9L10-C29-HYUNDAI-4B-20240628 | HYUNDAI | Stage4B-watch | 2024-06-28 | 2024-06-28 | 295000 | false | current_profile_4B_too_early_if_price_only |
| R9L10-C29-KIA-S2-20240125 | KIA | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 94400 | true | current_profile_correct |
| R9L10-C29-KIA-GREEN-20240229 | KIA | Stage3-Green | 2024-02-29 | 2024-02-29 | 124500 | false | current_profile_too_late |
| R9L10-C29-HLMANDO-FALSEGREEN-20240605 | HLMANDO | Stage3-Green-like | 2024-06-05 | 2024-06-05 | 49600 | true | current_profile_false_positive |
| R9L10-C29-HLMANDO-4C-WATCH-20240909 | HLMANDO | 4C-watch | 2024-09-09 | 2024-09-09 | 32050 | false | current_profile_4C_too_late_if_not_flagged |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger backtest

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| HYUNDAI-S2 | 187300 | 39.35 | -0.43 | 50.03 | -0.43 | 59.90 | -0.43 | 2024-06-28 | 299500 | -33.26 | false | false |
| KIA-S2 | 94400 | 39.51 | -1.80 | 43.01 | -1.80 | 43.01 | -5.19 | 2024-06-19 | 135000 | -33.70 | false | false |
| HLMANDO-FALSEGREEN | 49600 | 0.81 | -17.64 | 0.81 | -37.80 | 0.81 | -37.80 | 2024-06-05 | 50000 | -38.30 | true | true |

### Label comparison / overlay triggers

| trigger_id | entry_price | MFE_to_representative_peak_pct | MAE_to_180D_pct | role | verdict |
|---|---:|---:|---:|---|---|
| HYUNDAI-4B-20240628 | 295000 | 1.53 vs same-day high 299500 | -32.24 to post-peak trough | 4B_overlay_only | good local top, but price-only unless backed by non-price fatigue |
| KIA-GREEN-20240229 | 124500 | 8.43 to 135000 | -28.11 to late-year trough | label_comparison_only | Green caught confirmation but gave up most Stage2 upside |
| HLMANDO-4C-WATCH-20240909 | 32050 | 55.99 if measured back to prior 50000 peak; not positive entry | continued thesis-watch | 4C_overlay_only | downside happened before hard 4C evidence was cleanly separable |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_expected_stage | actual price path | verdict | Residual lesson |
|---|---|---|---|---|
| HYUNDAI | Stage2-Actionable, later Green | Strong positive MFE with almost no early MAE | current_profile_correct | Stage2 bonus works for OEM margin/revision bridge. |
| KIA | Stage2-Actionable, Green after revision confirmation | Stage2 captured most upside; Green was still useful but late | current_profile_correct with late_green_warning | C29 OEM Green should not wait too long when margin bridge and capital return are already public. |
| HLMANDO | Could be over-promoted to Yellow/Green if relative strength and EV/ADAS narrative are over-weighted | False Green: 0.81% MFE vs -37.80% MAE | current_profile_false_positive | C29 supplier narrative needs realized margin/revision gate, not just customer/ADAS optionality. |

Questions required by v12:

1. Stage2 bonus was appropriate for OEM cases, but too generous if applied to supplier narrative without margin closure.
2. Yellow threshold 75 is acceptable but needs C29 supplier cap when margin/revision fields are unsupported.
3. Green threshold 87/revision 55 is directionally correct; C29 supplier Green should require realized margin or guidance revision, not just price breakout.
4. Price-only blowoff guard remains appropriate; Hyundai 2024-06-28 is a good local price peak but should not become full 4B without non-price fatigue.
5. Full 4B non-price requirement is strengthened, not weakened.
6. Hard 4C routing is kept; HLMando is a 4C-watch/downside-protection example rather than a clean hard 4C row.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3/Green entry | peak after Stage2 | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| HYUNDAI | 187300 | 250000 | 299500 | 0.56 | Green was moderately late but still before full-window peak. |
| KIA | 94400 | 124500 | 135000 | 0.74 | Green captured confirmation after much of the upside had already occurred. |
| HLMANDO | not reliable | 49600 false Green | 50000 | not_applicable | Green-like label was outcome-misaligned; evidence did not close margin/revision bridge. |

C29 residual implication: Stage2-Actionable is useful for OEM margin operating leverage, but Stage3-Green needs a different rule for supplier narratives.

## 15. 4B Local vs Full-window Timing Audit

| case_id | Stage2 price | 4B watch price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| HYUNDAI | 187300 | 295000 | 299500 | 299500 | 0.96 | 0.96 | price_only; positioning_overheat | local timing good, but full 4B requires non-price fatigue. |
| KIA | 94400 | 124500 | 135000 | 135000 | 0.74 | 0.74 | valuation_blowoff_watch; price_only | usable as watch, not automatic full 4B. |
| HLMANDO | 49600 | 32050 downside watch | 50000 prior peak | 50000 prior peak | not_applicable | not_applicable | thesis_break_watch_only | not a 4B, a false-positive/protection case. |

## 16. 4C Protection Audit

HLMando provides a 4C-watch example: after the 2024-06-05 false Green-like trigger, downside exceeded -37% within the forward window. The file does not label a clean hard 4C because the research does not establish a single public contract cancellation, qualification failure, or accounting break date. For ingestion, this should be used as `thesis_break_watch_only`, not hard 4C.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = false
hard_4c_late = possible_but_not_proven
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = c29_oem_vs_supplier_margin_bridge_split
proposal_type = sector_shadow_only
```

Rule candidate:

> In L3/C29, OEM hybrid/export volume operating leverage can receive Stage2-Actionable credit from public earnings, capital return, relative strength, and margin bridge evidence. Supplier EV/ADAS narratives must be capped below Stage3-Green unless realized margin/revision or order-to-margin conversion is present.

This is not a production scoring change. It is a sector shadow rule for later batch ledgering.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
new_axis_proposed = c29_supplier_green_requires_realized_margin_revision
```

C29 is too broad if OEMs and suppliers are scored with identical relative-strength/customer-quality gates. The archetype should split:

- OEM branch: volume/mix/export margin bridge + shareholder/capital-return credibility.
- Supplier branch: customer narrative + ADAS/EV optionality must be validated by margin, backlog-to-revenue, or revision confirmation.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_triggers | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 3 | HYUNDAI-S2, KIA-S2, HLMANDO-FALSEGREEN | 31.28 | -13.34 | 34.57 | -14.47 | 0.33 | mixed: OEM correct, supplier false Green |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | later Green labels | 20.38 | -22.11 | 22.72 | -23.70 | 0.33 | weaker early capture, still vulnerable to supplier false Green |
| P1_L3_sector_candidate | sector_specific | 3 | OEM Stage2; supplier capped to Yellow/watch | 31.28 | -13.34 | 34.57 | -14.47 | 0.00 for positive promotion | improved by blocking supplier Green |
| P2_C29_archetype_candidate | canonical_archetype_specific | 3 | branch split by OEM/supplier margin bridge | 31.28 | -13.34 | 34.57 | -14.47 | 0.00 for positive promotion | best evidence-price alignment |
| P3_counterexample_guard_profile | guard | 3 | requires realized margin/revision for supplier Green | 31.28 | -13.34 | 34.57 | -14.47 | 0.00 | keeps current global axes, adds C29 guard |

## 20. Score-Return Alignment Matrix

| case_id | contract_score | backlog_visibility_score | margin_bridge_score | revision_score | relative_strength_score | customer_quality_score | valuation_repricing_score | execution_risk_score | weighted_score_before | stage_before | weighted_score_after | stage_after | score_return_alignment_label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| HYUNDAI | 0 | 2 | 9 | 8 | 8 | 7 | 8 | 2 | 82 | Stage2-Actionable/Yellow | 84 | Stage2-Actionable strong | aligned_positive |
| KIA | 0 | 2 | 9 | 8 | 8 | 7 | 8 | 2 | 83 | Stage2-Actionable/Yellow | 85 | Stage2-Actionable strong | aligned_positive_green_late |
| HLMANDO | 0 | 3 | 3 | 2 | 8 | 7 | 5 | 7 | 78 | Stage3-Yellow/false Green risk | 69 | Watch/Yellow cap | aligned_after_guard |

Canonical component keys required by v12 are present in the machine-readable rows. Components with no direct evidence, such as contract score for OEMs, are set to zero rather than inferred.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE_VS_EV_ADAS_PARTS_FALSE_GREEN | 2 | 1 | 1 | 0 | 3 | 0 | 6 | 3 | 1 | true | true | Needs more non-OEM supplier counterexamples and one clean hard 4C date. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [supplier_false_green, green_late_for_oem, price_only_4b_watch]
new_axis_proposed: [c29_supplier_green_requires_realized_margin_revision, c29_oem_vs_supplier_margin_bridge_split]
existing_axis_strengthened: [stage3_green_revision_min in C29 supplier branch, full_4b_requires_non_price_evidence]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual `Songdaiki/stock-web` 2024 and 2025 tradable OHLC rows for selected entries.
- 30D/90D/180D MFE/MAE using raw unadjusted tradable shards.
- Corporate-action candidate windows from symbol profiles.
- Positive/counterexample balance at the case level.

Not validated:

- Live/current 2026 candidate status.
- Production scoring code behavior.
- Brokerage/trading execution.
- Full 2Y MFE/MAE for all triggers. 1Y/2Y fields are included in JSON rows as null when not used in this v12 weight delta.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_supplier_green_requires_realized_margin_revision,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"HL Mando false Green had 0.81% MFE and -37.80% MAE after supplier narrative without confirmed margin/revision","blocks supplier false Green while preserving OEM Stage2 positives","R9L10-C29-HLMANDO-FALSEGREEN-20240605",3,3,1,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_oem_stage2_operating_leverage_credit,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Hyundai and Kia Stage2 entries captured 43-60% 180D MFE with shallow early MAE","keeps OEM Stage2 bonus when margin/revision and capital-return evidence align","R9L10-C29-HYUNDAI-S2-20240125|R9L10-C29-KIA-S2-20240125",3,3,1,low,sector_shadow_only,"not production; use with counterexample guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R9L10-C29-HYUNDAI-2024","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L10-C29-HYUNDAI-S2-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM margin/revision/capital-return bridge captured strong MFE with shallow early MAE."}
{"row_type":"case","case_id":"R9L10-C29-KIA-2024","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L10-C29-KIA-S2-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_green_late","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 captured most upside; Green confirmation was materially later."}
{"row_type":"case","case_id":"R9L10-C29-HLMANDO-2024","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_ADAS_PARTS_FALSE_GREEN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R9L10-C29-HLMANDO-FALSEGREEN-20240605","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_before_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Supplier narrative and price breakout lacked realized margin/revision; severe MAE followed."}
{"row_type":"trigger","trigger_id":"R9L10-C29-HYUNDAI-S2-20240125","case_id":"R9L10-C29-HYUNDAI-2024","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE","sector":"모빌리티·운송·레저","primary_archetype":"OEM hybrid/export margin operating leverage","loop_objective":"counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":187300,"evidence_available_at_that_date":"2023/4Q earnings, margin resilience, hybrid/export mix, shareholder-return/value-up attention","evidence_source":"public earnings/disclosure/news/research narrative; price via stock-web","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.35,"MFE_90D_pct":50.03,"MFE_180D_pct":59.90,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.43,"MAE_90D_pct":-0.43,"MAE_180D_pct":-0.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-33.26,"green_lateness_ratio":0.56,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"005380_2024-01-26_187300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L10-C29-HYUNDAI-4B-20240628","case_id":"R9L10-C29-HYUNDAI-2024","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_PRICE_ONLY_4B_OVERLAY","trigger_type":"Stage4B-watch","trigger_date":"2024-06-28","entry_date":"2024-06-28","entry_price":295000,"evidence_available_at_that_date":"Local price peak after OEM value-up rerating; non-price fatigue not established","evidence_source":"stock-web price path plus qualitative 4B watch narrative","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.53,"MFE_90D_pct":1.53,"MFE_180D_pct":1.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.59,"MAE_90D_pct":-27.12,"MAE_180D_pct":-32.24,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-33.26,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_local_price_peak_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success_watch_only","current_profile_verdict":"current_profile_4B_too_early_if_price_only","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"005380_2024-06-28_295000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L10-C29-KIA-S2-20240125","case_id":"R9L10-C29-KIA-2024","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":94400,"evidence_available_at_that_date":"2023 earnings and dividend/shareholder-return surprise with margin resilience","evidence_source":"public earnings/disclosure/news/research narrative; price via stock-web","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.51,"MFE_90D_pct":43.01,"MFE_180D_pct":43.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.80,"MAE_90D_pct":-1.80,"MAE_180D_pct":-5.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-33.70,"green_lateness_ratio":0.74,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000270_2024-01-26_94400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L10-C29-KIA-GREEN-20240229","case_id":"R9L10-C29-KIA-2024","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_HYBRID_EXPORT_MARGIN_LEVERAGE","trigger_type":"Stage3-Green","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":124500,"evidence_available_at_that_date":"post-earnings rerating confirmation and revision/margin validation","evidence_source":"public price path and research proxy evidence","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.78,"MFE_90D_pct":8.43,"MFE_180D_pct":8.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.47,"MAE_90D_pct":-18.23,"MAE_180D_pct":-28.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-33.70,"green_lateness_ratio":0.74,"four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"green_late_but_not_full_4B","four_b_evidence_type":["valuation_blowoff","price_only"],"four_c_protection_label":null,"trigger_outcome_label":"late_green_label_comparison","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000270_2024-02-29_124500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L10-C29-HLMANDO-FALSEGREEN-20240605","case_id":"R9L10-C29-HLMANDO-2024","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_ADAS_PARTS_FALSE_GREEN","trigger_type":"Stage3-Green-like","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":49600,"evidence_available_at_that_date":"EV/ADAS parts narrative and price breakout, but margin/revision confirmation insufficient","evidence_source":"public narrative proxy and stock-web price path","stage2_evidence_fields":["relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["weak_margin_bridge","unsupported_confirmed_revision"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.81,"MFE_90D_pct":0.81,"MFE_180D_pct":0.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.64,"MAE_90D_pct":-37.80,"MAE_180D_pct":-37.80,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":50000,"drawdown_after_peak_pct":-38.30,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"false_green_not_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"204320_2024-06-05_49600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L10-C29-HLMANDO-4C-WATCH-20240909","case_id":"R9L10-C29-HLMANDO-2024","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_ADAS_PARTS_FALSE_GREEN","trigger_type":"4C-watch","trigger_date":"2024-09-09","entry_date":"2024-09-09","entry_price":32050,"evidence_available_at_that_date":"price path confirmed prior false Green downside; no single hard 4C evidence date isolated","evidence_source":"stock-web price path only for protection audit","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.80,"MFE_90D_pct":38.07,"MFE_180D_pct":46.65,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.74,"MAE_90D_pct":-3.74,"MAE_180D_pct":-3.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-02-13","peak_price":47000,"drawdown_after_peak_pct":-30.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4C_watch_not_positive_entry","current_profile_verdict":"current_profile_4C_too_late_if_not_flagged","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"204320_2024-09-09_32050","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10-C29-HYUNDAI-2024","trigger_id":"R9L10-C29-HYUNDAI-S2-20240125","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":7},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable/Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":8},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable strong","changed_components":["roe_pbr_capital_return_score"],"component_delta_explanation":"OEM margin bridge plus capital-return credibility should preserve Stage2 credit.","MFE_90D_pct":50.03,"MAE_90D_pct":-0.43,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10-C29-KIA-2024","trigger_id":"R9L10-C29-KIA-S2-20240125","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":8},"weighted_score_before":83,"stage_label_before":"Stage2-Actionable/Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":9},"weighted_score_after":85,"stage_label_after":"Stage2-Actionable strong","changed_components":["roe_pbr_capital_return_score"],"component_delta_explanation":"Stage2 remains correct; Green confirmation is late but not false.","MFE_90D_pct":43.01,"MAE_90D_pct":-1.80,"score_return_alignment_label":"aligned_positive_green_late","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10-C29-HLMANDO-2024","trigger_id":"R9L10-C29-HLMANDO-FALSEGREEN-20240605","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow/false Green risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0},"weighted_score_after":69,"stage_label_after":"Watch/Yellow cap","changed_components":["margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Supplier narrative without realized margin/revision should cap Green despite relative strength.","MFE_90D_pct":0.81,"MAE_90D_pct":-37.80,"score_return_alignment_label":"aligned_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"same_archetype_new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["supplier_false_green","green_late_for_oem","price_only_4b_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R9/C29 OEM hybrid-export margin leverage vs supplier EV/ADAS false Green"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_supplier_green_requires_realized_margin_revision,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Supplier false Green had severe MAE without confirmed margin/revision","Reduces false positive Green risk","R9L10-C29-HLMANDO-FALSEGREEN-20240605",3,3,1,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_oem_stage2_operating_leverage_credit,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"OEM Stage2 entries aligned with large 180D MFE and shallow early MAE","Preserves Stage2 credit for OEM margin bridge","R9L10-C29-HYUNDAI-S2-20240125|R9L10-C29-KIA-S2-20240125",3,3,1,low,sector_shadow_only,"not production; use only with supplier guard"
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
next_round = R10 or R9 holdout
suggested_next_gap = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK or additional C29 supplier hard-4C case
carry_forward_state = C29 now has 2 OEM positives, 1 supplier false Green, 1 price-only 4B watch
```

## 28. Source Notes

- Stock-Web manifest and schema were validated for this loop. fileciteturn57file0turn58file0
- Hyundai, Kia, and HL Mando profile files were checked for available years, latest date, and corporate-action candidate caveats. fileciteturn59file0turn60file0turn61file0
- Hyundai 2024 OHLC rows validate the 2024-01-26 entry, June peak, and post-peak drawdown. fileciteturn62file0turn63file0
- Kia 2024 OHLC rows validate the 2024-01-26 entry, June peak, and late-year drawdown. fileciteturn64file0turn65file0
- HL Mando 2024-2025 OHLC rows validate the false Green entry and forward downside/recovery path. fileciteturn66file0turn67file0turn68file0
