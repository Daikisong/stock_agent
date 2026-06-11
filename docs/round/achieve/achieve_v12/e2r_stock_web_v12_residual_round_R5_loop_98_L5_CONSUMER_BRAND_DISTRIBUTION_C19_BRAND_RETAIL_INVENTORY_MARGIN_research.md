# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | retail_inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_98_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. After local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13 supplementation, C19 is the next unsupplemented Priority 0 archetype. Top-covered C19 names are avoided.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
retail_inventory_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 98
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C19 is a brand-retail inventory and margin archetype. Brand heat is the store window; the signal is whether sell-through, reorder, inventory turn, channel quality and OPM are actually moving through the cash register.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN = 24 rows / Priority 0
top covered C19 symbols avoided: 008770, 023530, 031430, 069960, 383220, 020000
recent local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C19 trigger families:

```text
036620 / Stage2-Actionable / 2024-02-21
282330 / Stage2-Actionable / 2024-01-16
366030 / Stage4B / 2024-05-24
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 036620 | atlas/symbol_profiles/036/036620.json | selected 2024 window clean after old 2000/2017/2018 CA candidates |
| 282330 | atlas/symbol_profiles/282/282330.json | no corporate-action candidate |
| 366030 | atlas/symbol_profiles/366/366030.json | selected 2024 window clean after old 2022 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L98_C19_GAMSUNG_2024_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_POSITIVE | 036620 | 2024-02-21 | yes | 180 | yes | yes | true |
| R5L98_C19_BGFRETAIL_2024_CONVENIENCE_RETAIL_INVENTORY_MARGIN_FALSE_STAGE2 | 282330 | 2024-01-16 | yes | 180 | yes | yes | true |
| R5L98_C19_GONGGUWOMEN_2024_SMALL_CAP_APPAREL_EVENT_CAP_4B | 366030 | 2024-05-24 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C19_BRAND_RETAIL_INVENTORY_MARGIN | APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE | Positive Stage2 requires sell-through, reorder cadence, inventory turn, channel quality, OPM and revision bridge. |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2 | Defensive retail watch without SSS/inventory-turn/OPM bridge can become false Stage2. |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | SMALL_CAP_APPAREL_EVENT_CAP_4B | Small-cap apparel event premium should route to 4B when sell-through/reorder/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L98_C19_GAMSUNG_2024_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_POSITIVE | 036620 | 감성코퍼레이션 | positive | Apparel brand sell-through/reorder bridge produced strong 30D/90D MFE with acceptable early MAE. |
| R5L98_C19_BGFRETAIL_2024_CONVENIENCE_RETAIL_INVENTORY_MARGIN_FALSE_STAGE2 | 282330 | BGF리테일 | counterexample | Defensive convenience-retail watch had tiny MFE and persistent MAE without SSS/OPM bridge. |
| R5L98_C19_GONGGUWOMEN_2024_SMALL_CAP_APPAREL_EVENT_CAP_4B | 366030 | 공구우먼 | counterexample / 4B | Small-cap apparel premium capped near the late-May spike and then de-rated sharply. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Gamsung apparel brand sell-through/reorder bridge | historical public/report proxy | true | true | shadow-only positive |
| BGF Retail convenience-retail false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Gonggu Women small-cap apparel event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 036620 | atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv | atlas/symbol_profiles/036/036620.json |
| 282330 | atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv | atlas/symbol_profiles/282/282330.json |
| 366030 | atlas/ohlcv_tradable_by_symbol_year/366/366030/2024.csv | atlas/symbol_profiles/366/366030.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L98_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE | 036620 | Stage2-Actionable | 2024-02-21 | 2840 | positive | brand sell-through/reorder margin bridge worked |
| R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH | 282330 | Stage2-Actionable | 2024-01-16 | 144900 | counterexample | defensive retail false Stage2 |
| R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP | 366030 | Stage4B | 2024-05-24 | 6890 | counterexample/4B | small-cap apparel event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L98_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE | 2840 | 35.74 | -9.51 | 65.14 | -9.51 | 65.14 | -9.51 | 2024-05-24 | 4690 | -18.76 |
| R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH | 144900 | 2.00 | -10.84 | 2.00 | -22.50 | 2.00 | -31.68 | 2024-01-16 | 147800 | -33.02 |
| R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP | 6890 | 14.22 | -15.82 | 14.22 | -44.70 | 14.22 | -44.70 | 2024-05-27 | 7870 | -51.59 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C19 Stage2 needs sell-through / reorder / inventory turn / channel quality / OPM / revision bridge |
| retail_inventory_margin_guardrail | strengthen: retail or brand label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing defensive retail and small-cap apparel premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C19 rows cannot promote without durable sell-through and OPM bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether brand-retail narrative becomes sell-through, reorder, inventory and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 036620 | good_stage2_with_later_watch | Brand/reorder bridge produced strong MFE, but later valuation and channel watch remains necessary. |
| 282330 | bad_stage2 | Defensive retail watch lacked SSS/inventory/OPM bridge and produced tiny MFE with persistent MAE. |
| 366030 | good_4B | Small-cap apparel event premium peaked near the late-May high and later de-rated sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 282330 convenience retail false Stage2 | 0.98 | 0.98 | false Stage2 due missing SSS / inventory turn / OPM bridge |
| 366030 small-cap apparel cap | 0.88 | 0.88 | good full-window 4B timing after apparel-brand event premium |
| 036620 apparel brand bridge | n/a | n/a | positive Stage2, but later channel valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 282330 / 366030
```

No hard 4C candidate is introduced in this C19 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 brand retail inventory-margin cases, Stage2 requires verified sell-through, reorder cadence, inventory turn, channel quality, marketing efficiency, OPM and revision bridge. Retail, brand, convenience, apparel, defensive consumption, DTC or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
rule = C19 should split true sell-through/reorder/inventory-margin positives from defensive retail false Stage2 and small-cap apparel event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 27.12 | -25.57 | 0.67 | mixed; C19 bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 27.12 | -25.57 | 0.67 | weaker C19 bridge split |
| P1 sector_specific_candidate_profile | L5 sell-through/inventory/OPM bridge required | 2 | 33.57 | -16.01 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C19 bridge vs event-cap split | 2 | 33.57 | -16.01 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing brand-retail themes as positive | 1 | 65.14 | -9.51 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 036620 apparel brand bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 65.14 | -9.51 | brand_retail_inventory_margin_positive |
| 282330 convenience retail false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.00 | -22.50 | convenience_retail_false_stage2 |
| 366030 small-cap apparel cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 14.22 | -44.70 | small_cap_apparel_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C19 is the next unsupplemented Priority 0 archetype after local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13 supplementation. This run adds Gamsung Corp, BGF Retail, and Gonggu Women while avoiding top-covered C19 names 008770, 023530, 031430, 069960, 383220 and 020000."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, retail_inventory_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: brand_retail_inventory_margin_positive, convenience_retail_false_stage2, small_cap_apparel_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, retail_inventory_margin_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C19 brand retail inventory-margin bridge vs false Stage2 / event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,configured,C19_requires_sellthrough_reorder_inventory_turn_OPM_revision_bridge,0,"C19 Stage2 should require sell-through, reorder cadence, inventory turn, channel quality, marketing efficiency, OPM and revision bridge, not brand/retail label alone","Gamsung positive worked; BGF Retail and Gonggu Women event/watch rows failed positive-stage promotion","R5L98_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE|R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH|R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,configured,cap_bridge_missing_defensive_retail_and_small_cap_apparel_event_premiums_as_4B_watch,0,"Defensive retail and small-cap apparel premiums can peak before sell-through, inventory turn and OPM bridge is proven","BGF Retail had tiny MFE and persistent drawdown after January high; Gonggu Women showed 4B event-cap behavior after late-May apparel spike","R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH|R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,configured,block_positive_stage_when_retail_brand_theme_has_high_or_persistent_MAE_without_inventory_margin_bridge,0,"High or persistent MAE after bridge-missing C19 entries should block Stage2/Stage3 promotion unless sell-through, inventory turn and OPM evidence survives","BGF Retail MAE180=-31.68 and Gonggu Women MAE90=-44.70","R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH|R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L98_C19_GAMSUNG_2024_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_POSITIVE", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "case_type": "structural_success_with_later_apparel_brand_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L98_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Apparel brand / sell-through / reorder / margin bridge produced strong 30D and 90D MFE after the February brand-retail recovery base with acceptable early MAE. C19 works when brand momentum is tied to sell-through, channel reorder, inventory turn, marketing efficiency, OPM and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C19_positive_requires_sellthrough_reorder_inventory_turn_margin_revision_bridge_not_brand_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2000/2017/2018 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L98_C19_BGFRETAIL_2024_CONVENIENCE_RETAIL_INVENTORY_MARGIN_FALSE_STAGE2", "symbol": "282330", "company_name": "BGF리테일", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "case_type": "failed_rerating_convenience_retail_inventory_margin_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Convenience-retail / defensive consumption watch around the January high had tiny MFE and then persistent MAE. C19 Stage2 should not be awarded without same-store sales, sell-through, inventory turn, franchise economics, OPM and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_defensive_retail_watch_counts_without_SSS_inventory_turn_OPM_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R5L98_C19_GONGGUWOMEN_2024_SMALL_CAP_APPAREL_EVENT_CAP_4B", "symbol": "366030", "company_name": "공구우먼", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-cap apparel brand event premium capped around the late-May spike and then de-rated sharply. C19 should route bridge-missing small-cap brand retail premiums to 4B unless sell-through, reorder cadence, inventory turn, channel quality, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_small_cap_apparel_brand_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L98_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE", "case_id": "R5L98_C19_GAMSUNG_2024_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_POSITIVE", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "sector": "apparel_brand_retail_sellthrough_reorder_margin", "primary_archetype": "sellthrough_reorder_inventory_turn_channel_OPM_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | retail_inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 2840.0, "evidence_available_at_that_date": "apparel brand / DTC-channel sell-through, reorder cadence, inventory-turn normalization, marketing efficiency and OPM/revision bridge proxy after February retail-brand base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["sellthrough_proxy", "channel_reorder_proxy", "inventory_turn_proxy", "marketing_efficiency_proxy", "OPM_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "acceptable_initial_MAE"], "stage4b_evidence_fields": ["later_apparel_brand_valuation_watch", "channel_inventory_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.74, "MFE_90D_pct": 65.14, "MFE_180D_pct": 65.14, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.51, "MAE_90D_pct": -9.51, "MAE_180D_pct": -9.51, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-24", "peak_price": 4690.0, "drawdown_after_peak_pct": -18.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_apparel_brand_channel_valuation_4B_watch_needed", "four_b_evidence_type": ["brand_sellthrough_reorder_bridge", "inventory_turn_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_apparel_brand_sellthrough_reorder_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2000_2017_2018_CA", "same_entry_group_id": "R5L98_C19_036620_2024-02-21_2840", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH", "case_id": "R5L98_C19_BGFRETAIL_2024_CONVENIENCE_RETAIL_INVENTORY_MARGIN_FALSE_STAGE2", "symbol": "282330", "company_name": "BGF리테일", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "sector": "convenience_retail_defensive_consumption_inventory_margin_watch", "primary_archetype": "defensive_retail_watch_without_SSS_inventory_turn_OPM_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | retail_inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-16", "entry_date": "2024-01-16", "entry_price": 144900.0, "evidence_available_at_that_date": "convenience retail / defensive consumption watch after January high without confirmed same-store sales acceleration, inventory-turn improvement, franchise economics, OPM or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["defensive_retail_watch", "brand_retail_theme", "January_relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "persistent_MAE90", "SSS_inventory_OPM_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv", "profile_path": "atlas/symbol_profiles/282/282330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.0, "MFE_90D_pct": 2.0, "MFE_180D_pct": 2.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.84, "MAE_90D_pct": -22.5, "MAE_180D_pct": -31.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 147800.0, "drawdown_after_peak_pct": -33.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "convenience_retail_inventory_margin_watch_was_false_stage2_due_missing_SSS_inventory_turn_OPM_revision_bridge", "four_b_evidence_type": ["defensive_retail_premium", "bridge_missing", "tiny_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_convenience_retail_inventory_margin_watch_without_SSS_OPM_bridge", "current_profile_verdict": "current_profile_false_positive_if_defensive_retail_watch_counts_without_SSS_inventory_turn_OPM_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R5L98_C19_282330_2024-01-16_144900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP", "case_id": "R5L98_C19_GONGGUWOMEN_2024_SMALL_CAP_APPAREL_EVENT_CAP_4B", "symbol": "366030", "company_name": "공구우먼", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "sector": "small_cap_apparel_brand_retail_event_premium", "primary_archetype": "small_cap_apparel_brand_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | retail_inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-24", "entry_date": "2024-05-24", "entry_price": 6890.0, "evidence_available_at_that_date": "small-cap apparel brand event premium without confirmed sell-through, reorder cadence, inventory turn, channel quality, OPM or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["small_cap_apparel_event", "brand_retail_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "sellthrough_reorder_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/366/366030/2024.csv", "profile_path": "atlas/symbol_profiles/366/366030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.22, "MFE_90D_pct": 14.22, "MFE_180D_pct": 14.22, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.82, "MAE_90D_pct": -44.7, "MAE_180D_pct": -44.7, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-27", "peak_price": 7870.0, "drawdown_after_peak_pct": -51.59, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing_small_cap_apparel_brand_event_cap_due_missing_sellthrough_reorder_margin_bridge", "four_b_evidence_type": ["small_cap_apparel_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_small_cap_apparel_brand_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_small_cap_apparel_brand_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R5L98_C19_366030_2024-05-24_6890", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R5L98_C19_GAMSUNG_2024_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R5L98_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE", "symbol": "036620", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "apparel_brand_sellthrough_reorder_positive", "MFE_90D_pct": 65.14, "MAE_90D_pct": -9.51, "score_return_alignment_label": "brand_retail_inventory_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R5L98_C19_BGFRETAIL_2024_CONVENIENCE_RETAIL_INVENTORY_MARGIN_FALSE_STAGE2", "trigger_id": "R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH", "symbol": "282330", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "convenience_retail_inventory_margin_false_stage2", "MFE_90D_pct": 2.0, "MAE_90D_pct": -22.5, "score_return_alignment_label": "convenience_retail_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_defensive_retail_watch_counts_without_SSS_inventory_turn_OPM_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R5L98_C19_GONGGUWOMEN_2024_SMALL_CAP_APPAREL_EVENT_CAP_4B", "trigger_id": "R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP", "symbol": "366030", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "small_cap_apparel_brand_event_cap_4B_guard", "MFE_90D_pct": 14.22, "MAE_90D_pct": -44.7, "score_return_alignment_label": "small_cap_apparel_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_small_cap_apparel_brand_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_CONVENIENCE_RETAIL_INVENTORY_FALSE_STAGE2_AND_SMALL_CAP_APPAREL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "retail_inventory_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["brand_retail_inventory_margin_positive", "convenience_retail_false_stage2", "small_cap_apparel_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C19 rows need explicit sell-through, reorder cadence, inventory turn, channel quality, marketing efficiency, OPM and revision bridge before positive promotion.
- In C19, bridge-missing brand-retail event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C19 brand retail inventory-margin rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R5
completed_loop = 98
completed_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
