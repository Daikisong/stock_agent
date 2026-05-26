# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 15
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT
loop_objective = holdout_validation / residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a current/live stock scan, not a recommendation, and not a `stock_agent` code patch.

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

This loop does not re-propose those global axes. It stress-tests whether `C19_BRAND_RETAIL_INVENTORY_MARGIN` needs a more specific bridge between brand heat, inventory quality, and gross-margin durability.

## 2. Round / Large Sector / Canonical Archetype Scope

- `large_sector_id`: `L5_CONSUMER_BRAND_DISTRIBUTION`
- `canonical_archetype_id`: `C19_BRAND_RETAIL_INVENTORY_MARGIN`
- `fine_archetype_id`: `BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT`
- Scope: brand-retail and apparel names where sell-through, inventory turn, channel reorder, and gross-margin bridge determine whether a rerating is durable.
- Excluded from scope: pure export channel food/beauty recurrence already covered under C18/C20; platform/content IP; one-off tender/control-premium events.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts checked for context only:

- `reports/e2r_calibration/ingest_summary.md`: existing corpus has R1-R13 coverage, 4,951 raw trigger rows, 1,940 validated rows, and 1,376 aggregate representative rows.
- `reports/e2r_calibration/applied_scoring_diff.md`: global Stock-Web axes already applied. This loop avoids repeating them as new global deltas.

Novelty rule:

```text
required_new_independent_case_ratio >= 0.60
calibration_usable_case_count = 5
new_independent_case_count = 4
reused_case_count = 1
new_independent_case_ratio = 0.80
loop_contribution_label = canonical_archetype_rule_candidate
```

F&F is reused as a known high-quality brand counterexample because it is useful for holdout stress-testing `brand halo != durable Green`.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_data_repo = https://github.com/Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The relevant profile checks show usable 180D windows for the selected entry dates. Corporate-action candidates are either outside the calibrated 180D windows or the trigger is used only as a 4B/4C overlay where the 180D calibration window remains clean.

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
historical_trigger = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180_trading_days_available = true
MFE_30D_90D_180D_computed = true
MAE_30D_90D_180D_computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Values are rounded research-proxy values derived from stock-web visible tradable rows. They are suitable for shadow-weight research, not direct trading use.

## 6. Canonical Archetype Compression Map

```text
fine_archetype: BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT
maps_to: C19_BRAND_RETAIL_INVENTORY_MARGIN
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
```

Compression rule: do not create separate production archetypes for Snow Peak apparel, MLB China brand, outdoor apparel, golf apparel, or OEM/outdoor export apparel. Compress them into C19 when the decisive evidence is inventory turn, sell-through, reorder, and gross-margin bridge.

## 7. Case Selection Summary

| case_id | symbol | company | role | current verdict | best trigger | notes |
|---|---:|---|---|---|---|---|
| C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE | 036620 | 감성코퍼레이션 | structural_success / positive | current_profile_missed_structural | T-C19-036620-2023-05-15-S2A | Snow Peak apparel/license-led domestic brand scaling converted into revenue and operating leverage; price path rewarded early channel/margin evidence before a later inventory digestion drawdown. |
| C19-111770-2022-OEM-BRAND-INVENTORY-DISCIPLINE | 111770 | 영원무역 | structural_success / positive | current_profile_too_late | T-C19-111770-2022-08-16-S2A | Apparel export/OEM demand and FX-margin bridge produced steady return with lower false-positive risk because evidence was not just sell-through hype but order/margin visibility. |
| C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP | 383220 | F&F | false_positive_green / counterexample | current_profile_false_positive | T-C19-383220-2023-02-15-GREEN-CAND | Brand quality remained high, but late-Green price entry after a full valuation rerating had poor forward path; inventory/channel normalization and multiple cap mattered more than brand halo. |
| C19-298540-2022-NATIONALGEOGRAPHIC-INVENTORY-SLOWDOWN | 298540 | 더네이쳐홀딩스 | failed_rerating / counterexample | current_profile_false_positive | T-C19-298540-2022-12-12-S2A | Expansion narrative and outdoor/category strength did not translate into durable margin bridge; forward path punished inventory and domestic-channel slowdown. |
| C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY | 110790 | 크리스에프앤씨 | 4B_overlay_success / counterexample | current_profile_4B_too_late | T-C19-110790-2022-05-16-4B | Golf apparel peak carried visible event/sector premium; lack of new channel recurrence and later inventory/margin normalization made it a 4B overlay rather than a positive Stage3 promotion. |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 5
calibration_usable_trigger_count = 8
```

The positive set says C19 can work, but only when brand momentum becomes measurable margin/reorder quality. The counterexample set says brand heat alone is a beautifully painted door with no hinges: it may look like a rerating, but if inventory and margin do not carry the weight, the door falls open into MAE.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE | early revision, apparel/channel volume, relative strength | margin bridge, financial visibility, repeat order/conversion | later local valuation/price-only watch | none in entry window |
| C19-111770-2022-OEM-BRAND-INVENTORY-DISCIPLINE | order/customer quality, relative strength, early revision | margin bridge, low red-team risk | none in entry window | none |
| C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP | brand/customer quality, relative strength | confirmed revision but late valuation | valuation blowoff, positioning, revision slowdown | thesis evidence weakened through normalization |
| C19-298540-2022-NATIONALGEOGRAPHIC-INVENTORY-SLOWDOWN | brand expansion/relative strength | weak margin confirmation | margin/inventory slowdown, price-only local peak | thesis evidence broken |
| C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY | sector/golf apparel heat | weak margin bridge | valuation blowoff, inventory/margin slowdown | later thesis deterioration |

## 10. Price Data Source Map

| symbol | profile_path | selected shard paths | profile caveat |
|---:|---|---|---|
| 036620 | `atlas/symbol_profiles/036/036620.json` | `atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv`, `2024.csv` | CA candidates in 2000/2017/2018 outside selected 180D window |
| 111770 | `atlas/symbol_profiles/111/111770.json` | `atlas/ohlcv_tradable_by_symbol_year/111/111770/2022.csv`, `2023.csv` | no corporate-action candidate |
| 383220 | `atlas/symbol_profiles/383/383220.json` | `atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv`, `2023.csv` | 2022-04-13 candidate avoided by 2023 entry |
| 298540 | `atlas/symbol_profiles/298/298540.json` | `atlas/ohlcv_tradable_by_symbol_year/298/298540/2022.csv`, `2023.csv` | 2021 candidates outside selected 180D window |
| 110790 | `atlas/symbol_profiles/110/110790.json` | `atlas/ohlcv_tradable_by_symbol_year/110/110790/2022.csv` | 2023-10-20 candidate outside selected 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current verdict | aggregate role |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| T-C19-036620-2023-05-15-S2A | Stage2-Actionable | 2023-05-15 | 3150 | 46.0 | -4.9 | 56.8 | -4.9 | 56.8 | -20.3 | current_profile_missed_structural | representative |
| T-C19-036620-2024-02-23-4B | 4B | 2024-02-23 | 3170 | 30.0 | -8.4 | 47.9 | -15.6 | 65.0 | -18.8 | current_profile_4B_too_early | 4B_overlay_only |
| T-C19-111770-2022-08-16-S2A | Stage2-Actionable | 2022-08-16 | 44000 | 14.8 | -6.4 | 19.3 | -6.4 | 24.0 | -8.9 | current_profile_too_late | representative |
| T-C19-383220-2023-02-15-GREEN-CAND | Stage3-Green-candidate | 2023-02-15 | 147700 | 2.7 | -13.3 | 2.7 | -18.4 | 2.7 | -36.5 | current_profile_false_positive | representative |
| T-C19-383220-2023-04-18-4B | 4B | 2023-04-18 | 149400 | 1.4 | -11.6 | 1.4 | -19.3 | 1.4 | -39.2 | current_profile_correct | 4B_overlay_only |
| T-C19-298540-2022-12-12-S2A | Stage2-Actionable | 2022-12-12 | 32900 | 3.3 | -12.6 | 1.4 | -23.1 | 1.4 | -39.7 | current_profile_false_positive | representative |
| T-C19-110790-2022-05-16-4B | 4B | 2022-05-16 | 41850 | 1.3 | -22.9 | 1.3 | -33.3 | 1.3 | -56.3 | current_profile_4B_too_late | representative |
| T-C19-110790-2022-10-13-4C | 4C | 2022-10-13 | 19150 | 10.2 | -4.4 | 12.0 | -12.0 | 16.0 | -25.0 | current_profile_correct | 4C_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

Representative trigger interpretation:

- Gamsung and Youngone show that C19 can identify durable rerating candidates, but only when brand demand is translated into margin or recurring channel evidence.
- F&F, The Nature Holdings, and Cris F&C show that high-quality brands can still become false Greens if the profile rewards brand heat, past growth, or local relative strength after valuation already repriced.
- The core residual is not global Green strictness. It is a C19-specific missing gate: `brand halo` must not substitute for `inventory-turn + gross-margin + channel-reorder evidence`.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile verdict | backtest alignment | residual error |
|---|---|---|---|
| C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE | current_profile_missed_structural | early Stage2 evidence had strong 90D MFE | missed channel/margin bridge |
| C19-111770-2022-OEM-BRAND-INVENTORY-DISCIPLINE | current_profile_too_late | lower drawdown and positive MFE supported earlier Yellow | slow to accept inventory discipline/margin evidence |
| C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP | current_profile_false_positive | 90D and 180D MAE dominated | brand quality over-weighted after valuation rerating |
| C19-298540-2022-NATIONALGEOGRAPHIC-INVENTORY-SLOWDOWN | current_profile_false_positive | severe 180D MAE after local high | expansion narrative lacked inventory/margin confirmation |
| C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY | current_profile_4B_too_late | peak was already local/full-window high | full 4B should fire when sector premium meets inventory/margin slowdown |

## 14. Stage2 / Yellow / Green Comparison

- Stage2-Actionable should fire for C19 only when at least two of three bridges exist:
  1. `channel_reorder_or_sellthrough_evidence`
  2. `gross_margin_or_OP_margin_bridge`
  3. `inventory_turn_or_working_capital_discipline`
- Stage3-Yellow should be allowed when the bridge is visible but not yet confirmed across multiple quarters.
- Stage3-Green should stay stricter than general consumer rerating because brand inventory cycles can reverse quickly.
- Existing `stage3_green_revision_min = 55` is strengthened for C19: revision must be accompanied by inventory/margin evidence, not simply brand revenue growth.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | verdict | reason |
|---|---:|---:|---|---|
| T-C19-036620-2024-02-23-4B | 0.74 | 0.31 | price_only_local_4B_too_early | local rebound was not full-cycle peak without non-price slowdown |
| T-C19-383220-2023-04-18-4B | 0.96 | 0.96 | good_full_window_4B_timing | valuation and revision/normalization evidence aligned with later drawdown |
| T-C19-110790-2022-05-16-4B | 0.97 | 0.97 | good_full_window_4B_timing | local and full-window peaks aligned with later inventory/margin deflation |

## 16. 4C Protection Audit

C19 4C should not wait for a formal business collapse. In brand-retail cases, 4C watch becomes useful when inventory, sell-through, or gross-margin evidence breaks the original demand thesis.

```text
T-C19-110790-2022-10-13-4C = hard_4c_success / protection logic
T-C19-298540-2022-12-12-S2A = later thesis-break watch, not immediate Green
T-C19-383220-2023-04-18-4B = 4B first, 4C only after evidence break
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
axis = l5_brand_or_consumer_rerating_requires_non_price_demand_quality
proposal = When a L5 brand/consumer stock rerates, price and brand awareness alone cannot promote Stage3. Require channel recurrence, margin bridge, or inventory-turn evidence.
confidence = medium
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
new_axis_proposed = c19_inventory_turn_and_gross_margin_bridge_gate
new_axis_proposed = c19_brand_halo_valuation_cap
new_axis_proposed = c19_full_4b_requires_inventory_or_margin_slowdown
```

Mechanism:

```text
if C19 and brand_heat_positive and no inventory_turn_or_margin_bridge:
    cap positive stage at Stage2-watch or Stage3-Red

if C19 and channel_reorder + margin_bridge + low execution risk:
    allow Stage2-Actionable / Stage3-Yellow earlier, even before generic Green threshold

if C19 and local/full peak proximity high and inventory/margin slowdown exists:
    promote 4B overlay to full 4B-elevated
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | avg MFE90 | avg MAE90 | false positive | missed structural | alignment |
|---|---|---|---:|---:|---|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Current calibrated profile with global guards only | 16.3 | -17.22 | 2/5 | 2 | mixed_residual_errors |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Older baseline without Stock-Web global guards | 16.3 | -17.22 | 3/5 | 2 | worse_than_current |
| P1_L5_brand_inventory_margin_sector_shadow | sector_specific | Require inventory-turn/gross-margin/channel-reorder bridge before L5 brand retail Green | 19.7 | -16.93 | 1/4 | 1 | improved |
| P2_C19_brand_retail_inventory_margin_shadow | canonical_archetype_specific | Promote C19 only when brand demand converts into repeat channel reorder and margin bridge; cap brand-halo valuation rerating | 38.05 | -5.65 | 0/2 selected | 0 | best_small_sample |
| P3_C19_inventory_counterexample_guard | counterexample_guard | If inventory/gross-margin deterioration appears after brand rerating, route to Stage3-Red/4B-watch not Green | 1.8 | -24.93 | blocked | 0 | risk_guard_improved |


## 20. Score-Return Alignment Matrix

| bucket | trigger count | avg MFE90 | avg MAE90 | interpretation |
|---|---:|---:|---:|---|
| recurring channel + margin bridge | 2 | 38.05 | -5.65 | positive C19 signal |
| brand halo / expansion without inventory bridge | 2 | 2.05 | -20.75 | false Green/Stage2 risk |
| 4B inventory/margin slowdown overlay | 2 | 1.35 | -26.3 | full 4B needs non-price evidence |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT | 2 | 3 | 3 | 1 | 4 | 1 | 8 | 5 | 5 | true | true | C19 still needs larger non-Korea holdout; Korea sample now has positive/counterexample balance. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: [C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP]
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_green_revision_min]
residual_error_types_found: [brand_halo_false_green, inventory_margin_missed_4B, channel_reorder_missed_structural]
new_axis_proposed: [c19_inventory_turn_and_gross_margin_bridge_gate, c19_brand_halo_valuation_cap, c19_full_4b_requires_inventory_or_margin_slowdown]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_green_revision_min]
existing_axis_weakened: null
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_cross_evidence_green_buffer, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Stock-Web OHLC path and profile-path presence.
- Trigger-level entry/forward MFE/MAE estimates.
- Representative-trigger dedupe.
- C19-specific residual logic.

Non-validation scope:

- No production code patch.
- No current/live candidate scan.
- No broker/API work.
- No investment recommendation.
- No claim that this small holdout alone is enough for a global rule.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c19_inventory_turn_and_gross_margin_bridge_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,C19 winners had channel recurrence + margin bridge; brand-halo entries without it had poor MFE/MAE,blocks F&F/TheNature/CrisFNC false promotion while retaining Gamsung/Youngone as Stage2/Y actionable,T-C19-036620-2023-05-15-S2A|T-C19-036620-2024-02-23-4B|T-C19-111770-2022-08-16-S2A|T-C19-383220-2023-02-15-GREEN-CAND|T-C19-383220-2023-04-18-4B|T-C19-298540-2022-12-12-S2A|T-C19-110790-2022-05-16-4B|T-C19-110790-2022-10-13-4C,8,4,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c19_brand_halo_valuation_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,High brand recognition and relative strength cannot substitute for inventory turn and gross-margin confirmation,reduces false-positive Green on brand retail rerating peaks,T-C19-383220-2023-02-15-GREEN-CAND|T-C19-298540-2022-12-12-S2A|T-C19-110790-2022-05-16-4B,5,3,3,medium,counterexample_guard_shadow_only,keeps global price-only guard but adds C19-specific evidence condition
shadow_weight,c19_full_4b_requires_inventory_or_margin_slowdown,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,C19 local peaks become full 4B only when inventory/gross-margin/channel slowdown evidence appears,separates Gamsung local volatility from F&F/CrisFNC full risk overlay,T-C19-036620-2024-02-23-4B|T-C19-383220-2023-04-18-4B|T-C19-110790-2022-05-16-4B,3,2,2,medium,4B_overlay_shadow_only,not a sell rule; overlay/risk calibration only
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T-C19-036620-2023-05-15-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_missed_structural", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Snow Peak apparel/license-led domestic brand scaling converted into revenue and operating leverage; price path rewarded early channel/margin evidence before a later inventory digestion drawdown."}
{"row_type": "case", "case_id": "C19-111770-2022-OEM-BRAND-INVENTORY-DISCIPLINE", "symbol": "111770", "company_name": "영원무역", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T-C19-111770-2022-08-16-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_too_late", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Apparel export/OEM demand and FX-margin bridge produced steady return with lower false-positive risk because evidence was not just sell-through hype but order/margin visibility."}
{"row_type": "case", "case_id": "C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T-C19-383220-2023-02-15-GREEN-CAND", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "holdout/reused high-quality brand false-positive archetype", "independent_evidence_weight": 0.5, "score_price_alignment": "current_profile_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Brand quality remained high, but late-Green price entry after a full valuation rerating had poor forward path; inventory/channel normalization and multiple cap mattered more than brand halo."}
{"row_type": "case", "case_id": "C19-298540-2022-NATIONALGEOGRAPHIC-INVENTORY-SLOWDOWN", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T-C19-298540-2022-12-12-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Expansion narrative and outdoor/category strength did not translate into durable margin bridge; forward path punished inventory and domestic-channel slowdown."}
{"row_type": "case", "case_id": "C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY", "symbol": "110790", "company_name": "크리스에프앤씨", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "T-C19-110790-2022-05-16-4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_4B_too_late", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Golf apparel peak carried visible event/sector premium; lack of new channel recurrence and later inventory/margin normalization made it a 4B overlay rather than a positive Stage3 promotion."}
{"row_type": "trigger", "trigger_id": "T-C19-036620-2023-05-15-S2A", "case_id": "C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "entry_date": "2023-05-15", "entry_price": 3150, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.0, "MFE_90D_pct": 56.8, "MFE_180D_pct": 56.8, "MFE_1Y_pct": 56.8, "MFE_2Y_pct": 113.0, "MAE_30D_pct": -4.9, "MAE_90D_pct": -4.9, "MAE_180D_pct": -20.3, "MAE_1Y_pct": -20.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-11", "peak_price": 4940, "drawdown_after_peak_pct": -49.2, "green_lateness_ratio": "0.42", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE::2023-05-15::3150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C19-036620-2024-02-23-4B", "case_id": "C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "4B", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 3170, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 30.0, "MFE_90D_pct": 47.9, "MFE_180D_pct": 65.0, "MFE_1Y_pct": 128.0, "MFE_2Y_pct": null, "MAE_30D_pct": -8.4, "MAE_90D_pct": -15.6, "MAE_180D_pct": -18.8, "MAE_1Y_pct": -18.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-09", "peak_price": 7210, "drawdown_after_peak_pct": -36.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.74, "four_b_full_window_peak_proximity": 0.31, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["valuation_blowoff", "price_only_local_peak"], "four_c_protection_label": null, "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE::2024-02-23::3170", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C19-111770-2022-08-16-S2A", "case_id": "C19-111770-2022-OEM-BRAND-INVENTORY-DISCIPLINE", "symbol": "111770", "company_name": "영원무역", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-16", "entry_date": "2022-08-16", "entry_price": 44000, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/111/111770/2022.csv", "profile_path": "atlas/symbol_profiles/111/111770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.8, "MFE_90D_pct": 19.3, "MFE_180D_pct": 24.0, "MFE_1Y_pct": 32.0, "MFE_2Y_pct": 66.0, "MAE_30D_pct": -6.4, "MAE_90D_pct": -6.4, "MAE_180D_pct": -8.9, "MAE_1Y_pct": -8.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-18", "peak_price": 58100, "drawdown_after_peak_pct": -24.0, "green_lateness_ratio": "0.36", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-111770-2022-OEM-BRAND-INVENTORY-DISCIPLINE::2022-08-16::44000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C19-383220-2023-02-15-GREEN-CAND", "case_id": "C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Green-candidate", "trigger_date": "2023-02-15", "entry_date": "2023-02-15", "entry_price": 147700, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.7, "MFE_90D_pct": 2.7, "MFE_180D_pct": 2.7, "MFE_1Y_pct": 2.7, "MFE_2Y_pct": 3.0, "MAE_30D_pct": -13.3, "MAE_90D_pct": -18.4, "MAE_180D_pct": -36.5, "MAE_1Y_pct": -41.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-18", "peak_price": 151500, "drawdown_after_peak_pct": -46.0, "green_lateness_ratio": "1.08", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": null, "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP::2023-02-15::147700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "R13 holdout includes F&F as a known high-quality brand overvaluation counterexample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T-C19-383220-2023-04-18-4B", "case_id": "C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "4B", "trigger_date": "2023-04-18", "entry_date": "2023-04-18", "entry_price": 149400, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "revision_slowdown", "margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.4, "MFE_90D_pct": 1.4, "MFE_180D_pct": 1.4, "MFE_1Y_pct": 1.4, "MFE_2Y_pct": 1.7, "MAE_30D_pct": -11.6, "MAE_90D_pct": -19.3, "MAE_180D_pct": -39.2, "MAE_1Y_pct": -43.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-18", "peak_price": 151500, "drawdown_after_peak_pct": -46.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "revision_slowdown", "margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP::2023-04-18::149400", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "R13 holdout includes F&F as a known high-quality brand overvaluation counterexample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T-C19-298540-2022-12-12-S2A", "case_id": "C19-298540-2022-NATIONALGEOGRAPHIC-INVENTORY-SLOWDOWN", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-12-12", "entry_date": "2022-12-12", "entry_price": 32900, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298540/2022.csv", "profile_path": "atlas/symbol_profiles/298/298540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.3, "MFE_90D_pct": 1.4, "MFE_180D_pct": 1.4, "MFE_1Y_pct": 1.4, "MFE_2Y_pct": 1.4, "MAE_30D_pct": -12.6, "MAE_90D_pct": -23.1, "MAE_180D_pct": -39.7, "MAE_1Y_pct": -50.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-12-22", "peak_price": 34000, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak"], "four_c_protection_label": null, "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-298540-2022-NATIONALGEOGRAPHIC-INVENTORY-SLOWDOWN::2022-12-12::32900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C19-110790-2022-05-16-4B", "case_id": "C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY", "symbol": "110790", "company_name": "크리스에프앤씨", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "4B", "trigger_date": "2022-05-16", "entry_date": "2022-05-16", "entry_price": 41850, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["margin_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/110/110790/2022.csv", "profile_path": "atlas/symbol_profiles/110/110790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.3, "MFE_90D_pct": 1.3, "MFE_180D_pct": 1.3, "MFE_1Y_pct": 1.3, "MFE_2Y_pct": 1.3, "MAE_30D_pct": -22.9, "MAE_90D_pct": -33.3, "MAE_180D_pct": -56.3, "MAE_1Y_pct": -62.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-18", "peak_price": 42400, "drawdown_after_peak_pct": -60.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY::2022-05-16::41850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C19-110790-2022-10-13-4C", "case_id": "C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY", "symbol": "110790", "company_name": "크리스에프앤씨", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_MARGIN_HOLDOUT", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "4C", "trigger_date": "2022-10-13", "entry_date": "2022-10-13", "entry_price": 19150, "evidence_available_at_that_date": "historical public earnings/brand-channel/inventory evidence available as of trigger date; no later outcome used for label assignment", "evidence_source": "quarterly results, company disclosure/news/consensus summaries; price path verified via stock-web tradable shards", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "margin_or_backlog_slowdown", "accounting_or_trust_break"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/110/110790/2022.csv", "profile_path": "atlas/symbol_profiles/110/110790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.2, "MFE_90D_pct": 12.0, "MFE_180D_pct": 16.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.4, "MAE_90D_pct": -12.0, "MAE_180D_pct": -25.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-12-01", "peak_price": 21450, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY::2022-10-13::19150", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE", "trigger_id": "T-C19-036620-2023-05-15-S2A", "symbol": "036620", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 8, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 73, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 9, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 77, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "C19 rewards channel recurrence plus margin bridge; not a pure price/brand halo adjustment.", "MFE_90D_pct": 56.8, "MAE_90D_pct": -4.9, "score_return_alignment_label": "residual_error_found", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-036620-2023-SNOWPEAK-MARGIN-BRIDGE", "trigger_id": "T-C19-036620-2024-02-23-4B", "symbol": "036620", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 82, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 80, "stage_label_after": "4B-watch", "changed_components": ["margin_bridge_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "C19 rewards channel recurrence plus margin bridge; not a pure price/brand halo adjustment.", "MFE_90D_pct": 47.9, "MAE_90D_pct": -15.6, "score_return_alignment_label": "residual_error_found", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-111770-2022-OEM-BRAND-INVENTORY-DISCIPLINE", "trigger_id": "T-C19-111770-2022-08-16-S2A", "symbol": "111770", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 8, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 9, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "C19 rewards channel recurrence plus margin bridge; not a pure price/brand halo adjustment.", "MFE_90D_pct": 19.3, "MAE_90D_pct": -6.4, "score_return_alignment_label": "residual_error_found", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP", "trigger_id": "T-C19-383220-2023-02-15-GREEN-CAND", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 3, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 5, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 3, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 5, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 81, "stage_label_after": "Stage3-Red", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C19 discounts brand halo and valuation rerating when no inventory turn or gross-margin bridge confirms sell-through.", "MFE_90D_pct": 2.7, "MAE_90D_pct": -18.4, "score_return_alignment_label": "residual_error_found", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-383220-2023-FNF-CHINA-GROWTH-MULTIPLE-CAP", "trigger_id": "T-C19-383220-2023-04-18-4B", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 86, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 84, "stage_label_after": "4B-elevated", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C19 discounts brand halo and valuation rerating when no inventory turn or gross-margin bridge confirms sell-through.", "MFE_90D_pct": 1.4, "MAE_90D_pct": -19.3, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-298540-2022-NATIONALGEOGRAPHIC-INVENTORY-SLOWDOWN", "trigger_id": "T-C19-298540-2022-12-12-S2A", "symbol": "298540", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 5, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 5, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 69, "stage_label_after": "Stage2-watch", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C19 discounts brand halo and valuation rerating when no inventory turn or gross-margin bridge confirms sell-through.", "MFE_90D_pct": 1.4, "MAE_90D_pct": -23.1, "score_return_alignment_label": "residual_error_found", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY", "trigger_id": "T-C19-110790-2022-05-16-4B", "symbol": "110790", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 75, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 70, "stage_label_after": "4B-elevated", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C19 discounts brand halo and valuation rerating when no inventory turn or gross-margin bridge confirms sell-through.", "MFE_90D_pct": 1.3, "MAE_90D_pct": -33.3, "score_return_alignment_label": "residual_error_found", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19-110790-2022-GOLF-APPAREL-PEAK-INVENTORY", "trigger_id": "T-C19-110790-2022-10-13-4C", "symbol": "110790", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 1, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 9, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 44, "stage_label_before": "4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 1, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 10, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 40, "stage_label_after": "4C", "changed_components": ["execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C19 thesis-break/brand-inventory deterioration remains 4C protection logic, not positive weight.", "MFE_90D_pct": 12.0, "MAE_90D_pct": -12.0, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R13", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage3_green_revision_min"], "residual_error_types_found": ["brand_halo_false_green", "inventory_margin_missed_4B", "channel_reorder_missed_structural"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = batch_implementation_prompt_or_R13_loop_16_final_cross_archetype_review
candidate_next_scope = aggregate all v12 MD machine-readable rows into promotion/acceptance ledger
```

## 28. Source Notes

Stock-Web files directly checked in this loop:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/036/036620.json`
- `atlas/symbol_profiles/111/111770.json`
- `atlas/symbol_profiles/383/383220.json`
- `atlas/symbol_profiles/298/298540.json`
- `atlas/symbol_profiles/110/110790.json`
- `atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/111/111770/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/298/298540/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/110/110790/2022.csv`

The numerical MFE/MAE fields are rounded research proxies based on these visible shard rows and should be revalidated by a batch parser before promotion.
