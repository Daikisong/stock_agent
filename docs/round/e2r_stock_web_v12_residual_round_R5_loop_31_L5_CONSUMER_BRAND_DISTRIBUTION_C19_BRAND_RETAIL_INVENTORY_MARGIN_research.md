# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
round = R5
loop = 31
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = OUTDOOR_OEM_BRAND_MARGIN_BRIDGE | APPAREL_OEM_INVENTORY_RESTOCK_MARGIN_BRIDGE | BRAND_CHINA_RETAIL_INVENTORY_OVERHANG | OUTDOOR_BRAND_INVENTORY_OVERHANG_COUNTEREXAMPLE
output_file = e2r_stock_web_v12_residual_round_R5_loop_31_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This Markdown is a standalone historical calibration / sector-archetype residual research artifact. It is not a live candidate scan, not a watchlist, not a trading instruction, and not a `stock_agent` code patch. The narrow residual question is whether C19 should distinguish true inventory normalization + margin bridge from brand/retail expansion narratives that still carry inventory overhang.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The current profile is treated as already calibrated. This loop does not re-prove the global Stage2 bonus, Green lateness, or price-only 4B/4C guards. It tests a C19-specific residual: brand retail names can look cheap or popular while the inventory and gross-margin machine is still clogged. In contrast, OEM/apparel exporters can rerate when restocking and margin bridge appear together.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R5 |
| loop | 31 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test |
| primary universe | apparel OEM restocking, outdoor brand margin bridge, China/brand retail inventory overhang, outdoor-brand inventory false positive |

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible research artifacts in the local calibration workspace showed repeated R5/C20 and R5/C18 work, while C19 was explicitly called out as a next gap in prior R5 outputs. A direct GitHub repository search for `C19_BRAND_RETAIL_INVENTORY_MARGIN 383220 111770 105630 298540` returned no matching prior artifact in the accessible search surface. Therefore this loop treats all four representative cases as new independent C19 cases.

```text
auto_selected_coverage_gap = C19_BRAND_RETAIL_INVENTORY_MARGIN lacked positive/counterexample split after R5/C18/C20 work
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_duplicate = false
same_entry_group_rematerialization = false
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

Diversity logic:

```text
new_trigger_families = [
  OUTDOOR_OEM_BRAND_MARGIN_BRIDGE,
  APPAREL_OEM_INVENTORY_RESTOCK_MARGIN_BRIDGE,
  BRAND_CHINA_RETAIL_INVENTORY_OVERHANG,
  OUTDOOR_BRAND_INVENTORY_OVERHANG_COUNTEREXAMPLE
]
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest was checked before case calculation. The atlas uses FinanceData/marcap, records `price_adjustment_status = raw_unadjusted_marcap`, and has `max_date = 2026-02-20`; calibration-safe tradable shards live under `atlas/ohlcv_tradable_by_symbol_year`, while raw rows remain under `atlas/ohlcv_raw_by_symbol_year`. The manifest also records 14,354,401 tradable rows, 15,214,118 raw rows, 5,414 symbols, and KOSPI/KOSDAQ/KOSDAQ GLOBAL/KONEX market coverage. fileciteturn634file0

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Per-symbol profile validation:

| symbol | company_name | profile_path | first_date | last_date | corporate_action_candidate_dates | 180D status |
|---:|---|---|---:|---:|---|---|
| 111770 | 영원무역 | atlas/symbol_profiles/111/111770.json | 2009-07-30 | 2026-02-20 | none | clean for 2023-05-15 trigger |
| 105630 | 한세실업 | atlas/symbol_profiles/105/105630.json | 2009-03-20 | 2026-02-20 | 2011-11-30 | clean for 2023-06-16 trigger |
| 383220 | F&F | atlas/symbol_profiles/383/383220.json | 2021-05-21 | 2026-02-20 | 2022-04-13 | clean for 2023-05-16 trigger |
| 298540 | 더네이쳐홀딩스 | atlas/symbol_profiles/298/298540.json | 2020-07-27 | 2026-02-20 | 2021-08-02; 2021-08-30 | clean for 2023-05-16 trigger |

Profile rows confirm active-like stock-web coverage and no corporate-action candidate date inside the selected 2023 180D windows for all representative cases. fileciteturn660file0 fileciteturn663file0 fileciteturn659file0 fileciteturn668file0

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | 180 trading days available? | clean 180D corporate-action window? | calibration_usable | block_reason |
|---|---:|---:|---:|---:|---:|---:|---|
| R5L31_C19_YOUNGONE_20230515_OEM_BRAND_MARGIN_SUCCESS | 111770 | 2023-05-15 | 47,500 | true | true | true | none |
| R5L31_C19_HANSAE_20230616_OEM_INVENTORY_RESTOCK_SUCCESS | 105630 | 2023-06-16 | 17,880 | true | true | true | none |
| R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN | 383220 | 2023-05-16 | 137,900 | true | true | true | none |
| R5L31_C19_NATURE_20230516_OUTDOOR_INVENTORY_COUNTER | 298540 | 2023-05-16 | 25,850 | true | true | true | none |

The entry rows and key peak/low rows are visible in the stock-web tradable shards: 영원무역 2023 rows show the 2023-05-15 entry and the subsequent 2023-08-16 high; 한세실업 rows show the 2023-06-16 entry and 2023-10-31 high, with the 2024 row showing the post-peak 2024-01-16 low; F&F rows show the 2023-05-16 entry, 2023-06-20 high, and 2023-10-27 low; 더네이쳐홀딩스 rows show the 2023-05-16 entry, 2023-06-09 high, and 2023-07-26 low. fileciteturn662file0 fileciteturn665file0 fileciteturn664file0 fileciteturn661file0 fileciteturn669file0

## 6. Canonical Archetype Compression Map

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
  ├── OUTDOOR_OEM_BRAND_MARGIN_BRIDGE
  ├── APPAREL_OEM_INVENTORY_RESTOCK_MARGIN_BRIDGE
  ├── BRAND_CHINA_RETAIL_INVENTORY_OVERHANG
  └── OUTDOOR_BRAND_INVENTORY_OVERHANG_COUNTEREXAMPLE
```

Compression rule: C19 should not be just “brand popularity.” It is the stock-market version of a warehouse: sell-through, inventory aging, gross margin, and reorder rhythm are the shelves. A clean store-front without clean shelves is a false signal.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | entry date | entry price | 180D MFE | 180D MAE | current profile verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| R5L31_C19_YOUNGONE_20230515_OEM_BRAND_MARGIN_SUCCESS | 111770 | 영원무역 | structural_success | outdoor OEM/brand margin bridge | 2023-05-15 | 47,500 | +42.95% | -6.11% | current_profile_correct |
| R5L31_C19_HANSAE_20230616_OEM_INVENTORY_RESTOCK_SUCCESS | 105630 | 한세실업 | high_mae_success | apparel OEM restock + inventory normalization | 2023-06-16 | 17,880 | +33.11% | -3.08% | current_profile_correct; 4B late |
| R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN | 383220 | F&F | false_positive_green | brand/China narrative with inventory risk | 2023-05-16 | 137,900 | +2.76% | -37.20% | current_profile_false_positive |
| R5L31_C19_NATURE_20230516_OUTDOOR_INVENTORY_COUNTER | 298540 | 더네이쳐홀딩스 | failed_rerating | outdoor brand expansion without cleared inventory bridge | 2023-05-16 | 25,850 | +7.16% | -23.29% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
representative_trigger_count = 4
new_independent_case_count = 4
reused_case_count = 0
current_profile_error_count = 3
```

The positive side is not “consumer beta.” It is inventory/restocking/margin mechanism. The counterexample side is not “bad stock chart.” It is a broken shelf: brand expansion narratives kept moving while the inventory and margin bridge failed to close.

## 9. Evidence Source Map

| evidence family | source basis | scoring use |
|---|---|---|
| inventory normalization | quarterly earnings, DART/KIND filing family, management commentary family | Stage2/Stage3 positive only when margin bridge also appears |
| margin bridge | gross margin/operating-margin direction and revision family | Stage3 confirmation |
| brand expansion narrative | press/research narrative, overseas/channel expansion stories | Stage2 only if inventory and margin evidence confirm |
| inventory overhang | earnings notes, margin pressure, stock-web post-trigger MAE validation | counterexample guard / 4C watch |
| stock-web OHLC | tradable_raw shards | outcome validation, MFE/MAE, 4B/4C timing only |

## 10. Price Data Source Map

| symbol | shard path | profile path | entry row | relevant peak/low rows |
|---:|---|---|---|---|
| 111770 | atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv | atlas/symbol_profiles/111/111770.json | 2023-05-15 c=47,500 | 2023-08-16 h=67,900; 2023-05-15 l=44,600; post-peak low near 46,950 |
| 105630 | atlas/ohlcv_tradable_by_symbol_year/105/105630/2023.csv | atlas/symbol_profiles/105/105630.json | 2023-06-16 c=17,880 | 2023-10-31 h=23,800; 2023-07-26 l=17,330; 2024-01-16 l=19,080 |
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv | atlas/symbol_profiles/383/383220.json | 2023-05-16 c=137,900 | 2023-06-20 h=141,700; 2023-10-27 l=86,600 |
| 298540 | atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv | atlas/symbol_profiles/298/298540.json | 2023-05-16 c=25,850 | 2023-06-09 h=27,700; 2023-07-26 l=19,830 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B/4C fields | aggregate role |
|---|---:|---|---:|---:|---:|---|---|---|---|
| R5L31_T01_YOUNGONE_STAGE2_MARGIN_BRIDGE_20230515 | 111770 | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 47,500 | margin_bridge; relative_strength; early_revision_signal; inventory_normalization | confirmed_revision; margin_bridge; financial_visibility | - | representative |
| R5L31_T02_HANSAE_STAGE2_RESTOCK_20230616 | 105630 | Stage2-Actionable | 2023-06-16 | 2023-06-16 | 17,880 | margin_bridge; relative_strength; inventory_normalization; early_revision_signal | confirmed_revision; margin_bridge; financial_visibility | - | representative |
| R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516 | 383220 | Stage2-Watch / false positive guard | 2023-05-16 | 2023-05-16 | 137,900 | brand_global_narrative; relative_strength_decay | - | thesis_evidence_broken | representative |
| R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516 | 298540 | Stage2-Watch / false positive guard | 2023-05-16 | 2023-05-16 | 25,850 | brand_expansion_narrative; relative_strength_decay | - | thesis_evidence_broken | representative |
| R5L31_T05_HANSAE_4B_INVENTORY_RERATING_OVERHEAT_20231031 | 105630 | Stage4B | 2023-10-31 | 2023-10-31 | 22,850 | - | confirmed_revision; margin_bridge | valuation_blowoff; positioning_overheat; margin_or_backlog_slowdown | 4B_overlay_only |
| R5L31_T06_FNF_4C_INVENTORY_THESIS_BREAK_20230719 | 383220 | Stage4C | 2023-07-19 | 2023-07-19 | 105,300 | - | - | thesis_evidence_broken; margin_or_backlog_slowdown | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| trigger_id | entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L31_T01_YOUNGONE_STAGE2_MARGIN_BRIDGE_20230515 | 47,500 | +36.84% | -6.11% | +42.95% | -6.11% | +42.95% | -6.11% | 2023-08-16 | 67,900 | -30.85% |
| R5L31_T02_HANSAE_STAGE2_RESTOCK_20230616 | 17,880 | +22.48% | -3.08% | +23.60% | -3.08% | +33.11% | -3.08% | 2023-10-31 | 23,800 | -19.83% |
| R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516 | 137,900 | +2.76% | -12.62% | +2.76% | -31.04% | +2.76% | -37.20% | 2023-06-20 | 141,700 | -38.88% |
| R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516 | 25,850 | +7.16% | -9.86% | +7.16% | -23.29% | +7.16% | -23.29% | 2023-06-09 | 27,700 | -28.41% |

### Overlay / comparison triggers

| trigger_id | entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | local/full proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| R5L31_T05_HANSAE_4B_INVENTORY_RERATING_OVERHEAT_20231031 | 22,850 | +4.16% | -7.00% | +4.16% | -16.50% | 0.84 / 0.84 | good_full_window_4B_timing |
| R5L31_T06_FNF_4C_INVENTORY_THESIS_BREAK_20230719 | 105,300 | +6.55% | -7.74% | +13.87% | -17.76% | n/a | hard_4c_success_if_routed_by_inventory_break |

## 13. Current Calibrated Profile Stress Test

| question | finding |
|---|---|
| How would current calibrated profile judge 영원무역? | Correct if it recognizes explicit margin bridge + inventory normalization; not just retail beta. |
| Did that judgment match MFE/MAE? | Yes. +42.95% MFE_180D with -6.11% MAE supports promotion. |
| How would current calibrated profile judge 한세실업? | Correct for Stage2, but 4B overlay was late after rerating approached the full observed peak. |
| Did F&F reveal a residual false positive? | Yes. A brand/China narrative without inventory normalization produced only +2.76% MFE_180D and -37.20% MAE_180D. |
| Did 더네이쳐홀딩스 reveal a residual false positive? | Yes. Outdoor-brand expansion without a clean inventory/margin bridge delivered +7.16% MFE_180D and -23.29% MAE_180D. |
| Was Stage2 bonus excessive? | Not globally. It was useful for positive restock/margin cases, but too permissive if applied to brand narrative alone. |
| Was Yellow 75 too loose? | In C19, Yellow can be too loose unless inventory normalization and margin bridge are both present. |
| Was Green 87 / revision 55 too strict or loose? | Kept, but C19 should require `inventory_normalization_score` as a companion gate. |
| Was price-only blowoff guard appropriate? | Strengthened. Price-only rebound in C19 cannot promote Stage2/3. |
| Was full 4B non-price requirement appropriate? | Strengthened. 한세실업 4B needed valuation/positioning/margin fatigue, not just a local high. |
| Was hard 4C routing late? | F&F indicates 4C can be late if inventory thesis-break evidence is ignored until after deep drawdown. |

```text
current_profile_error_count = 3
error_1 = current_profile_false_positive for F&F if brand/global narrative is promoted without inventory bridge
error_2 = current_profile_false_positive for 더네이쳐홀딩스 if outdoor expansion narrative is promoted without inventory bridge
error_3 = current_profile_4B_too_late for 한세실업 after inventory restock rerating was mostly reflected
```

## 14. Stage2 / Yellow / Green Comparison

The useful lateness audit is not a classic “Green is always late” argument. It is a C19 component-quality argument. For positive C19 cases, Stage2 can be valid when inventory normalization and margin bridge appear together. For counterexamples, even a Yellow-like total score should not promote if the inventory shelf remains broken.

```text
Youngone Stage2 entry = 47,500
Youngone full observed 180D peak = 67,900
Hansae Stage2 entry = 17,880
Hansae full observed 180D peak = 23,800
F&F counterexample entry = 137,900
F&F full observed 180D peak = 141,700
```

The C19 lesson is: Stage2 should be allowed to breathe when restocking/margin evidence is alive; Yellow/Green should be choked when the score is built on brand narrative but inventory bridge is missing.

## 15. 4B Local vs Full-window Timing Audit

| trigger | stage2 entry | 4B entry | full-window peak | local peak proximity | full-window proximity | non-price 4B evidence | verdict |
|---|---:|---:|---:|---:|---:|---|---|
| 한세실업 2023-10-31 | 17,880 | 22,850 | 23,800 | 0.84 | 0.84 | valuation_blowoff; positioning_overheat; margin/backlog slowdown risk | good_full_window_4B_timing |

For C19, 4B should fire when the inventory-normalization rerating is mostly reflected and incremental evidence begins to flatten. It should not fire merely because a local price peak occurred.

## 16. 4C Protection Audit

F&F is the guard case.

```text
prior_stage_entry = 2023-05-16 close 137,900
observed peak after entry = 2023-06-20 high 141,700
thesis-break watch trigger = 2023-07-19 close 105,300
180D low = 2023-10-27 low 86,600
max_drawdown_after_peak_from_prior_stage = -38.88%
four_c_protection_label = hard_4c_success_if_routed_by_inventory_break
```

The exact 4C trigger date is research-proxy, not production logic. The point is that inventory thesis-break should be allowed to block or downgrade before the full drawdown is visible.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Candidate sector rule:

```text
l5_inventory_margin_bridge_before_brand_narrative_bonus = +1 shadow
l5_brand_expansion_without_inventory_normalization_guard = +1 guard
```

This should not become a global rule yet. It is strongest inside consumer/brand/distribution names where inventory and gross margin are not side notes but the engine itself.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
rule_scope = canonical_archetype_specific
```

### Proposed C19 shadow rules

1. `c19_inventory_normalization_margin_bridge_bonus`
   - Promote only when inventory normalization and margin bridge appear together.
   - Supported by 영원무역 and 한세실업.

2. `c19_brand_narrative_inventory_overhang_guard`
   - Block Stage2/Stage3 promotion when brand/channel narrative exists but inventory and margin bridge remain weak.
   - Supported by F&F and 더네이쳐홀딩스.

3. `c19_rerating_4b_margin_fatigue_overlay`
   - Use 4B overlay after a successful inventory/margin rerating approaches the full observed peak and non-price fatigue appears.
   - Supported by 한세실업 overlay row.

## 19. Before / After Backtest Comparison

| profile | scope | selected representative triggers | avg MFE 90D | avg MAE 90D | avg MFE 180D | avg MAE 180D | false positive rate | missed structural count | score-return alignment verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | all 4 if brand narrative not guarded | +19.62% | -15.88% | +21.50% | -17.42% | 50.0% | 0 | mixed; positives diluted by two severe counterexamples |
| P0b e2r_2_0_baseline_reference | rollback | later/less component-aware | not primary | not primary | not primary | not primary | unknown | unknown | reference only |
| P1 sector_specific_candidate_profile | L5 | promote margin+inventory; block narrative-only | +33.28% promoted | -4.60% promoted | +38.03% promoted | -4.60% promoted | 0.0% among promoted | 0 | improved |
| P2 canonical_archetype_candidate_profile | C19 | same as P1 but limited to C19 | +33.28% promoted | -4.60% promoted | +38.03% promoted | -4.60% promoted | 0.0% among promoted | 0 | best alignment |
| P3 counterexample_guard_profile | C19 guard | F&F/Nature blocked | +4.96% blocked | -27.17% avoided | +4.96% blocked | -30.25% avoided | reduced | 0 | useful guard |

## 20. Score-Return Alignment Matrix

| case | raw component diagnosis | P0 verdict | actual return path | after C19 shadow profile |
|---|---|---|---|---|
| 영원무역 | margin bridge + inventory normalization + RS | correct | high upside / low MAE | promote |
| 한세실업 | restock + margin bridge + RS; later 4B fatigue | correct but 4B late | high upside then drawdown sensitivity | promote then 4B overlay |
| F&F | brand narrative with inventory overhang | false positive risk | weak MFE / severe MAE | block promotion; 4C watch |
| 더네이쳐홀딩스 | outdoor brand expansion without clean margin/inventory proof | false positive risk | weak MFE / high MAE | block promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | OUTDOOR_OEM_BRAND_MARGIN_BRIDGE / APPAREL_OEM_INVENTORY_RESTOCK_MARGIN_BRIDGE / BRAND_CHINA_RETAIL_INVENTORY_OVERHANG / OUTDOOR_BRAND_INVENTORY_OVERHANG_COUNTEREXAMPLE | 2 | 2 | 1 | 1 | 4 | 0 | 6 | 4 | 3 | true | true | C19 has first balanced positive/counterexample seed; needs additional holdout beyond apparel/outdoor. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes: [stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [current_profile_false_positive, current_profile_4B_too_late, current_profile_4C_too_late]
new_axis_proposed: c19_inventory_normalization_margin_bridge_bonus; c19_brand_narrative_inventory_overhang_guard; c19_rerating_4b_margin_fatigue_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R5/C19 brand retail inventory margin gap after R5/C18 and R5/C20 coverage
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- symbol profile availability and corporate-action candidate windows
- trigger entry rows inside tradable shards
- 30D/90D/180D MFE/MAE proxy calculations from stock-web tradable_raw rows
- positive/counterexample balance
- Stage2/Stage3/4B/4C evidence separation
- same_entry_group dedupe fields
- machine-readable rows for later ingestion
```

Not validated:

```text
- production scoring code behavior
- live current candidate status
- brokerage/API routing
- complete DART filing text extraction
- whether these shadow rows should be promoted globally
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c19_inventory_normalization_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Promote C19 only when inventory normalization and margin bridge are both present.","Promoted cases average +38.03% MFE_180D with -4.60% MAE_180D.","R5L31_T01_YOUNGONE_STAGE2_MARGIN_BRIDGE_20230515|R5L31_T02_HANSAE_STAGE2_RESTOCK_20230616",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_brand_narrative_inventory_overhang_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Block brand/global/outdoor expansion narrative when inventory and margin bridge are not closed.","Blocked counterexamples average -30.25% MAE_180D with only +4.96% MFE_180D.","R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516|R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516",2,2,2,medium,canonical_guard_only,"not production; post-calibrated residual"
shadow_weight,c19_rerating_4b_margin_fatigue_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"After inventory/margin rerating approaches peak and fatigue appears, use 4B overlay.","Hansae 4B overlay was near 0.84 full-window proximity and later drawdown sensitivity rose.","R5L31_T05_HANSAE_4B_INVENTORY_RERATING_OVERHEAT_20231031",1,1,0,low,overlay_shadow_only,"requires more 4B holdout"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L31_C19_YOUNGONE_20230515_OEM_BRAND_MARGIN_SUCCESS", "symbol": "111770", "company_name": "영원무역", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "OUTDOOR_OEM_BRAND_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L31_T01_YOUNGONE_STAGE2_MARGIN_BRIDGE_20230515", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "score_return_aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "영원무역 C19 structural_success case using clean 180D tradable_raw window."}
{"row_type": "case", "case_id": "R5L31_C19_HANSAE_20230616_OEM_INVENTORY_RESTOCK_SUCCESS", "symbol": "105630", "company_name": "한세실업", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_OEM_INVENTORY_RESTOCK_MARGIN_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R5L31_T02_HANSAE_STAGE2_RESTOCK_20230616", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "score_return_aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "한세실업 C19 high_mae_success case using clean 180D tradable_raw window."}
{"row_type": "case", "case_id": "R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_CHINA_RETAIL_INVENTORY_OVERHANG", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "F&F C19 false_positive_green case using clean 180D tradable_raw window."}
{"row_type": "case", "case_id": "R5L31_C19_NATURE_20230516_OUTDOOR_INVENTORY_COUNTER", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "OUTDOOR_BRAND_INVENTORY_OVERHANG_COUNTEREXAMPLE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "더네이쳐홀딩스 C19 failed_rerating case using clean 180D tradable_raw window."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L31_T01_YOUNGONE_STAGE2_MARGIN_BRIDGE_20230515", "case_id": "R5L31_C19_YOUNGONE_20230515_OEM_BRAND_MARGIN_SUCCESS", "symbol": "111770", "company_name": "영원무역", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "OUTDOOR_OEM_BRAND_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "entry_date": "2023-05-15", "entry_price": 47500, "evidence_available_at_that_date": "quarterly earnings / brand retail inventory and margin bridge signal available by trigger date; price not used for promotion", "evidence_source": "company/DART/KIND earnings-disclosure family; analyst/public reporting family; stock-web OHLC for outcome validation only", "stage2_evidence_fields": ["margin_bridge", "relative_strength", "early_revision_signal", "inventory_normalization"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv", "profile_path": "atlas/symbol_profiles/111/111770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.84, "MFE_90D_pct": 42.95, "MFE_180D_pct": 42.95, "MFE_1Y_pct": 42.95, "MFE_2Y_pct": null, "MAE_30D_pct": -6.11, "MAE_90D_pct": -6.11, "MAE_180D_pct": -6.11, "MAE_1Y_pct": -6.11, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-16", "peak_price": 67900, "drawdown_after_peak_pct": -30.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L31_C19_YOUNGONE_20230515_OEM_BRAND_MARGIN_SUCCESS_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L31_T02_HANSAE_STAGE2_RESTOCK_20230616", "case_id": "R5L31_C19_HANSAE_20230616_OEM_INVENTORY_RESTOCK_SUCCESS", "symbol": "105630", "company_name": "한세실업", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_OEM_INVENTORY_RESTOCK_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-16", "entry_date": "2023-06-16", "entry_price": 17880, "evidence_available_at_that_date": "quarterly earnings / brand retail inventory and margin bridge signal available by trigger date; price not used for promotion", "evidence_source": "company/DART/KIND earnings-disclosure family; analyst/public reporting family; stock-web OHLC for outcome validation only", "stage2_evidence_fields": ["margin_bridge", "relative_strength", "inventory_normalization", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105630/2023.csv", "profile_path": "atlas/symbol_profiles/105/105630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.48, "MFE_90D_pct": 23.6, "MFE_180D_pct": 33.11, "MFE_1Y_pct": 33.11, "MFE_2Y_pct": null, "MAE_30D_pct": -3.08, "MAE_90D_pct": -3.08, "MAE_180D_pct": -3.08, "MAE_1Y_pct": -3.08, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-31", "peak_price": 23800, "drawdown_after_peak_pct": -19.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L31_C19_HANSAE_20230616_OEM_INVENTORY_RESTOCK_SUCCESS_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516", "case_id": "R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_CHINA_RETAIL_INVENTORY_OVERHANG", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-16", "entry_date": "2023-05-16", "entry_price": 137900, "evidence_available_at_that_date": "quarterly earnings / brand retail inventory and margin bridge signal available by trigger date; price not used for promotion", "evidence_source": "company/DART/KIND earnings-disclosure family; analyst/public reporting family; stock-web OHLC for outcome validation only", "stage2_evidence_fields": ["brand_global_narrative", "relative_strength_decay"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.76, "MFE_90D_pct": 2.76, "MFE_180D_pct": 2.76, "MFE_1Y_pct": 2.76, "MFE_2Y_pct": null, "MAE_30D_pct": -12.62, "MAE_90D_pct": -31.04, "MAE_180D_pct": -37.2, "MAE_1Y_pct": -37.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-20", "peak_price": 141700, "drawdown_after_peak_pct": -38.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516", "case_id": "R5L31_C19_NATURE_20230516_OUTDOOR_INVENTORY_COUNTER", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "OUTDOOR_BRAND_INVENTORY_OVERHANG_COUNTEREXAMPLE", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-16", "entry_date": "2023-05-16", "entry_price": 25850, "evidence_available_at_that_date": "quarterly earnings / brand retail inventory and margin bridge signal available by trigger date; price not used for promotion", "evidence_source": "company/DART/KIND earnings-disclosure family; analyst/public reporting family; stock-web OHLC for outcome validation only", "stage2_evidence_fields": ["brand_expansion_narrative", "relative_strength_decay"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv", "profile_path": "atlas/symbol_profiles/298/298540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.16, "MFE_90D_pct": 7.16, "MFE_180D_pct": 7.16, "MFE_1Y_pct": 7.16, "MFE_2Y_pct": null, "MAE_30D_pct": -9.86, "MAE_90D_pct": -23.29, "MAE_180D_pct": -23.29, "MAE_1Y_pct": -23.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-09", "peak_price": 27700, "drawdown_after_peak_pct": -28.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L31_C19_NATURE_20230516_OUTDOOR_INVENTORY_COUNTER_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L31_T05_HANSAE_4B_INVENTORY_RERATING_OVERHEAT_20231031", "case_id": "R5L31_C19_HANSAE_20230616_OEM_INVENTORY_RESTOCK_SUCCESS", "symbol": "105630", "company_name": "한세실업", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_OEM_INVENTORY_RESTOCK_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2023-10-31", "entry_date": "2023-10-31", "entry_price": 22850, "evidence_available_at_that_date": "post-rerating valuation and positioning heat after inventory restock/margin bridge was mostly reflected", "evidence_source": "stock-web OHLC plus non-price valuation/positioning overlay family", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105630/2023.csv", "profile_path": "atlas/symbol_profiles/105/105630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.16, "MFE_90D_pct": 4.16, "MFE_180D_pct": 4.16, "MFE_1Y_pct": 4.16, "MFE_2Y_pct": null, "MAE_30D_pct": -7.0, "MAE_90D_pct": -16.5, "MAE_180D_pct": -19.83, "MAE_1Y_pct": -19.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-31", "peak_price": 23800, "drawdown_after_peak_pct": -19.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.84, "four_b_full_window_peak_proximity": 0.84, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L31_C19_HANSAE_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L31_T06_FNF_4C_INVENTORY_THESIS_BREAK_20230719", "case_id": "R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_CHINA_RETAIL_INVENTORY_OVERHANG", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2023-07-19", "entry_date": "2023-07-19", "entry_price": 105300, "evidence_available_at_that_date": "inventory/margin thesis failed to close and trend had moved from watch to thesis-break protection", "evidence_source": "inventory/margin evidence family plus stock-web OHLC outcome validation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken", "accounting_or_trust_break"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.55, "MFE_90D_pct": 13.87, "MFE_180D_pct": 13.87, "MFE_1Y_pct": 13.87, "MFE_2Y_pct": null, "MAE_30D_pct": -7.74, "MAE_90D_pct": -17.76, "MAE_180D_pct": -17.76, "MAE_1Y_pct": -17.76, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-18", "peak_price": 119900, "drawdown_after_peak_pct": -27.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success_if_routed_by_inventory_break", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L31_C19_FNF_4C", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L31_C19_YOUNGONE_20230515_OEM_BRAND_MARGIN_SUCCESS", "trigger_id": "R5L31_T01_YOUNGONE_STAGE2_MARGIN_BRIDGE_20230515", "symbol": "111770", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 72, "revision_score": 62, "relative_strength_score": 68, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 70, "channel_sellthrough_score": 65}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 72, "revision_score": 62, "relative_strength_score": 68, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 70, "channel_sellthrough_score": 65}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow", "changed_components": ["inventory_normalization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C19 shadow profile promotes explicit margin+inventory normalization and blocks brand/global narrative when inventory/margin bridge is not closed.", "MFE_90D_pct": 42.95, "MAE_90D_pct": -6.11, "score_return_alignment_label": "score_return_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L31_C19_HANSAE_20230616_OEM_INVENTORY_RESTOCK_SUCCESS", "trigger_id": "R5L31_T02_HANSAE_STAGE2_RESTOCK_20230616", "symbol": "105630", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 72, "revision_score": 62, "relative_strength_score": 68, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 70, "channel_sellthrough_score": 65}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 72, "revision_score": 62, "relative_strength_score": 68, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 70, "channel_sellthrough_score": 65}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow", "changed_components": ["inventory_normalization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C19 shadow profile promotes explicit margin+inventory normalization and blocks brand/global narrative when inventory/margin bridge is not closed.", "MFE_90D_pct": 23.6, "MAE_90D_pct": -3.08, "score_return_alignment_label": "score_return_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN", "trigger_id": "R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 28, "relative_strength_score": 35, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 72, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 20, "channel_sellthrough_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 28, "relative_strength_score": 35, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 72, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 20, "channel_sellthrough_score": 25}, "weighted_score_after": 62, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["inventory_normalization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C19 shadow profile promotes explicit margin+inventory normalization and blocks brand/global narrative when inventory/margin bridge is not closed.", "MFE_90D_pct": 2.76, "MAE_90D_pct": -31.04, "score_return_alignment_label": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L31_C19_NATURE_20230516_OUTDOOR_INVENTORY_COUNTER", "trigger_id": "R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516", "symbol": "298540", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 28, "relative_strength_score": 35, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 72, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 20, "channel_sellthrough_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 28, "relative_strength_score": 35, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 72, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "inventory_normalization_score": 20, "channel_sellthrough_score": 25}, "weighted_score_after": 62, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["inventory_normalization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C19 shadow profile promotes explicit margin+inventory normalization and blocks brand/global narrative when inventory/margin bridge is not closed.", "MFE_90D_pct": 7.16, "MAE_90D_pct": -23.29, "score_return_alignment_label": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c19_inventory_normalization_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Promote C19 only when inventory normalization and margin bridge are both present.","Promoted cases average +38.03% MFE_180D with -4.60% MAE_180D.","R5L31_T01_YOUNGONE_STAGE2_MARGIN_BRIDGE_20230515|R5L31_T02_HANSAE_STAGE2_RESTOCK_20230616",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_brand_narrative_inventory_overhang_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Block brand/global/outdoor expansion narrative when inventory and margin bridge are not closed.","Blocked counterexamples average -30.25% MAE_180D with only +4.96% MFE_180D.","R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516|R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516",2,2,2,medium,canonical_guard_only,"not production; post-calibrated residual"
shadow_weight,c19_rerating_4b_margin_fatigue_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"After inventory/margin rerating approaches peak and fatigue appears, use 4B overlay.","Hansae 4B overlay was near 0.84 full-window proximity and later drawdown sensitivity rose.","R5L31_T05_HANSAE_4B_INVENTORY_RERATING_OVERHEAT_20231031",1,1,0,low,overlay_shadow_only,"requires more 4B holdout"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "31", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_false_positive", "current_profile_4B_too_late", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl

```

No narrative-only row is emitted because all representative cases are 180D calibration-usable and have clean selected windows.

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
recommended_next_round = R5 / C19 holdout or R5 / C18-C20 cross-consumer guard validation
recommended_next_objective = holdout_validation; counterexample_mining; 4B_non_price_requirement_stress_test
avoid_next_duplicate = do not reuse 111770 2023-05-15, 105630 2023-06-16, 383220 2023-05-16, 298540 2023-05-16 unless new trigger family or correction
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json` under Songdaiki/stock-web, checked for max_date, shard roots, row counts, and raw/unadjusted caveat. fileciteturn634file0
- Symbol profile sources: 영원무역, 한세실업, F&F, 더네이쳐홀딩스 stock-web profile JSONs. fileciteturn660file0 fileciteturn663file0 fileciteturn659file0 fileciteturn668file0
- OHLC row sources: 111770/2023, 105630/2023 and 2024, 383220/2023, 298540/2023 stock-web tradable shards. fileciteturn662file0 fileciteturn665file0 fileciteturn664file0 fileciteturn661file0 fileciteturn669file0
- This file uses research proxy component scores only. It does not assert actual production scoring behavior.
