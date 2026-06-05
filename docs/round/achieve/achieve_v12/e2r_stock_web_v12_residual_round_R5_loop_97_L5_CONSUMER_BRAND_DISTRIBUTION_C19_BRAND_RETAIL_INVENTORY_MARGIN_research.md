# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_97_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
```

This file is the corrected final output for this execution. The scheduler state after R4 loop 97 is R5 / loop 97. R5 is the L5 consumer / brand / distribution round, and this run fills C19 brand-retail inventory margin rather than repeating the immediately preceding R5 loop 96 C18 export-channel reorder file, R5 loop 95 C20 beauty/food distribution file, or R4 loop 97 C17 chemical-spread file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
inventory_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 97
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 97
```

C19 is an inventory-to-margin bridge archetype. A brand or retail recovery label is the storefront sign; the signal becomes usable only when inventory turn, channel sell-through, traffic, markdown discipline, margin and revision survive together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN = 38 rows / 13 symbols / good-bad Stage2 8-9 / 4B-4C 3-0
top covered symbols include 282330(9), 004170(4), 007070(4), 093050(4), 337930(4), 139480(3)
previous R5 loop-89 C18 symbols avoided: 018290, 078520, 123690
previous R5 loop-92 C18 symbols avoided: 004370, 007310, 005610
previous R5 loop-94 C18 symbols avoided: 003230, 101530, 011150
previous R5 loop-95 C20 symbols avoided: 002790, 027050, 003350
previous R5 loop-96 C18 symbols avoided: 005180, 222040, 103840
previous R4 loop-97 C17 symbols avoided: 001340, 010060, 006890
previous R3 loop-97 C12 symbols avoided: 011790, 243840, 419050
```

Selected rows avoid hard duplicates and top repeated C19 symbols:

```text
023530 / Stage2-Actionable / 2024-01-22
383220 / Stage2-Actionable / 2024-04-01
008770 / Stage4B / 2024-04-01
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
| 023530 | atlas/symbol_profiles/023/023530.json | no corporate-action candidate |
| 383220 | atlas/symbol_profiles/383/383220.json | selected 2024 window clean after old 2022 CA candidate |
| 008770 | atlas/symbol_profiles/008/008770.json | selected 2024 window clean after old 1999 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L97_C19_LOTTESHOPPING_2024_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_POSITIVE | 023530 | 2024-01-22 | yes | 180 | yes | yes | true |
| R5L97_C19_FNF_2024_APPAREL_CHINA_INVENTORY_FALSE_STAGE2 | 383220 | 2024-04-01 | yes | 180 | yes | yes | true |
| R5L97_C19_HOTELSHILLA_2024_DUTY_FREE_RETAIL_EVENT_CAP_4B | 008770 | 2024-04-01 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C19_BRAND_RETAIL_INVENTORY_MARGIN | DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE | Positive Stage2 requires inventory turn, traffic/category mix, markdown discipline, margin and revision bridge. |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | APPAREL_CHINA_INVENTORY_FALSE_STAGE2 | Apparel/China retail inventory watch without sell-through and margin bridge can become false Stage2. |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | DUTY_FREE_RETAIL_EVENT_CAP_4B | Duty-free/retail recovery event premium should route to 4B when traffic and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L97_C19_LOTTESHOPPING_2024_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_POSITIVE | 023530 | 롯데쇼핑 | positive | Department-store/retail inventory-margin bridge produced strong MFE with controlled early MAE. |
| R5L97_C19_FNF_2024_APPAREL_CHINA_INVENTORY_FALSE_STAGE2 | 383220 | F&F | counterexample | Apparel/China inventory watch produced near-zero durable MFE and high MAE. |
| R5L97_C19_HOTELSHILLA_2024_DUTY_FREE_RETAIL_EVENT_CAP_4B | 008770 | 호텔신라 | counterexample / 4B | Duty-free retail recovery premium capped on the April event spike and then de-rated. |

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
| Lotte Shopping department-store retail inventory margin bridge | historical public/report proxy | true | true | shadow-only positive |
| F&F apparel China inventory false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hotel Shilla duty-free retail event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 023530 | atlas/ohlcv_tradable_by_symbol_year/023/023530/2024.csv | atlas/symbol_profiles/023/023530.json |
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv | atlas/symbol_profiles/383/383220.json |
| 008770 | atlas/ohlcv_tradable_by_symbol_year/008/008770/2024.csv | atlas/symbol_profiles/008/008770.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE | 023530 | Stage2-Actionable | 2024-01-22 | 71800 | positive | department-store retail inventory-margin bridge worked |
| R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH | 383220 | Stage2-Actionable | 2024-04-01 | 76500 | counterexample | apparel China inventory false Stage2 |
| R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP | 008770 | Stage4B | 2024-04-01 | 62900 | counterexample/4B | duty-free retail event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE | 71800 | 28.27 | -5.29 | 28.27 | -11.00 | 28.27 | -14.90 | 2024-02-13 | 92100 | -33.66 |
| R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH | 76500 | 1.18 | -20.13 | 1.18 | -24.58 | 1.18 | -38.37 | 2024-04-01 | 77400 | -39.08 |
| R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP | 62900 | 0.16 | -11.45 | 0.16 | -18.92 | 0.16 | -28.85 | 2024-04-01 | 63000 | -28.97 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C19 Stage2 needs inventory turn / sell-through / traffic / markdown / margin / revision bridge |
| inventory_margin_guardrail | strengthen: recovery labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing apparel and duty-free retail premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE brand/retail rows cannot promote without durable inventory-margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether retail/brand recovery becomes sell-through and inventory-margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 023530 | good_stage2_with_later_watch | Inventory-margin bridge produced solid MFE, but later valuation and inventory watch remains necessary. |
| 383220 | bad_stage2 | Apparel China/inventory watch lacked sell-through and margin bridge, producing near-zero MFE and high MAE. |
| 008770 | good_4B | Duty-free retail event premium peaked immediately and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 383220 apparel inventory false Stage2 | 0.99 | 0.99 | false Stage2 due missing sell-through / markdown / margin bridge |
| 008770 duty-free retail cap | 1.00 | 1.00 | good full-window 4B timing after April duty-free retail event premium |
| 023530 retail inventory bridge | n/a | n/a | positive Stage2, but later retail valuation and inventory watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 383220 / 008770
```

No hard 4C candidate is introduced in this R5 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 brand/retail inventory-margin cases, Stage2 requires verified inventory turn, channel sell-through, traffic/basket recovery, category mix, markdown discipline, margin, or revision bridge. Brand, retail, value-up, China, duty-free, tourist recovery, apparel or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
rule = C19 should split true inventory-turn/sell-through/margin positives from apparel inventory false Stage2 and duty-free retail event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 9.87 | -18.17 | 0.67 | mixed; C19 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 9.87 | -18.17 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L5 inventory/sell-through/margin bridge required | 2 | 14.72 | -17.79 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C19 bridge vs event-cap split | 2 | 14.72 | -17.79 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing brand/retail themes as positive | 1 | 28.27 | -11.00 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 023530 retail inventory bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 28.27 | -11.00 | department_store_retail_inventory_margin_positive |
| 383220 apparel inventory false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.18 | -24.58 | apparel_inventory_false_stage2 |
| 008770 duty-free cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 0.16 | -18.92 | duty_free_retail_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C19 Lotte Shopping department-store/retail inventory-margin positive, F&F apparel China inventory false Stage2, and Hotel Shilla duty-free retail event-cap 4B while avoiding top repeated C19 and previous R5/R4/R3 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, inventory_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: department_store_retail_inventory_margin_positive, apparel_inventory_false_stage2, duty_free_retail_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, inventory_margin_guardrail, high_MAE_guardrail
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
- C19 brand/retail inventory margin bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,configured,C19_requires_inventory_turn_sellthrough_traffic_markdown_margin_revision_bridge,0,"C19 Stage2 should require inventory turn, channel sell-through, traffic/basket recovery, category mix, markdown discipline, margin, or revision bridge, not brand/retail/inventory/value-up label alone","Lotte Shopping positive worked; F&F and Hotel Shilla event/watch rows failed positive-stage promotion","R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE|R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH|R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,configured,cap_bridge_missing_apparel_and_dutyfree_retail_event_premiums_as_4B_watch,0,"Apparel, China retail and duty-free recovery premiums can peak before sell-through, traffic, inventory and margin bridge is proven","F&F had near-zero MFE and deep MAE after inventory watch; Hotel Shilla showed clean 4B event-cap behavior after the April duty-free retail spike","R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH|R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,configured,block_positive_stage_when_brand_retail_theme_has_high_or_persistent_MAE_without_inventory_margin_bridge,0,"High or persistent MAE after bridge-missing C19 entries should block Stage2/Stage3 promotion unless inventory turn, sell-through, traffic and margin evidence survives","F&F MAE180=-38.37 and Hotel Shilla MAE180=-28.85","R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH|R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L97_C19_LOTTESHOPPING_2024_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_POSITIVE", "symbol": "023530", "company_name": "롯데쇼핑", "round": "R5", "loop": "97", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "case_type": "moderate_structural_success_with_later_retail_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Department-store / retail inventory-margin bridge produced a strong 30D MFE and controlled early MAE after the January washout. C19 works when retail/brand narrative maps into inventory normalization, category mix, store traffic, markdown discipline, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C19_positive_requires_inventory_turn_category_mix_traffic_markdown_margin_revision_bridge_not_retail_valueup_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L97_C19_FNF_2024_APPAREL_CHINA_INVENTORY_FALSE_STAGE2", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "97", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "case_type": "failed_rerating_apparel_inventory_margin_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Apparel / China retail inventory rebound watch after the April spike produced almost no durable MFE and then suffered high MAE. C19 Stage2 should not be awarded without confirmed inventory turn, channel sell-through, markdown control, traffic, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_apparel_inventory_watch_counts_without_sellthrough_markdown_inventory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R5L97_C19_HOTELSHILLA_2024_DUTY_FREE_RETAIL_EVENT_CAP_4B", "symbol": "008770", "company_name": "호텔신라", "round": "R5", "loop": "97", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Duty-free / retail recovery event premium capped near the April spike and then de-rated deeply. C19 should route bridge-missing retail recovery premiums to 4B unless traffic, basket size, inventory turn, markdown control, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_duty_free_retail_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "R5L97_C19_LOTTESHOPPING_2024_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_POSITIVE", "symbol": "023530", "company_name": "롯데쇼핑", "round": "R5", "loop": "97", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "sector": "department_store_retail_inventory_margin_valueup", "primary_archetype": "inventory_turn_category_mix_traffic_markdown_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 71800.0, "evidence_available_at_that_date": "department-store / retail value-up and inventory-margin normalization proxy with category mix, store traffic, markdown discipline and margin/revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["inventory_turn_proxy", "category_mix_proxy", "store_traffic_proxy", "markdown_control_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_retail_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023530/2024.csv", "profile_path": "atlas/symbol_profiles/023/023530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.27, "MFE_90D_pct": 28.27, "MFE_180D_pct": 28.27, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.29, "MAE_90D_pct": -11.0, "MAE_180D_pct": -14.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-13", "peak_price": 92100.0, "drawdown_after_peak_pct": -33.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_retail_valuation_and_inventory_4B_watch_needed", "four_b_evidence_type": ["inventory_margin_bridge", "traffic_category_mix", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_department_store_retail_inventory_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R5L97_C19_023530_2024-01-22_71800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH", "case_id": "R5L97_C19_FNF_2024_APPAREL_CHINA_INVENTORY_FALSE_STAGE2", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "97", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "sector": "apparel_brand_China_inventory_recovery_watch", "primary_archetype": "apparel_inventory_watch_without_sellthrough_markdown_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 76500.0, "evidence_available_at_that_date": "apparel brand / China retail inventory recovery watch without confirmed channel sell-through, markdown control, traffic recovery or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["apparel_inventory_watch", "China_retail_recovery_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "deep_MAE90", "sellthrough_markdown_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.18, "MFE_90D_pct": 1.18, "MFE_180D_pct": 1.18, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.13, "MAE_90D_pct": -24.58, "MAE_180D_pct": -38.37, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-01", "peak_price": 77400.0, "drawdown_after_peak_pct": -39.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "apparel_inventory_watch_was_false_stage2_due_missing_sellthrough_markdown_margin_revision_bridge", "four_b_evidence_type": ["apparel_inventory_premium", "bridge_missing", "near_zero_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_apparel_China_inventory_watch_without_sellthrough_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_apparel_inventory_watch_counts_without_sellthrough_markdown_inventory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA_candidate", "same_entry_group_id": "R5L97_C19_383220_2024-04-01_76500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP", "case_id": "R5L97_C19_HOTELSHILLA_2024_DUTY_FREE_RETAIL_EVENT_CAP_4B", "symbol": "008770", "company_name": "호텔신라", "round": "R5", "loop": "97", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "sector": "duty_free_retail_traffic_inventory_event_premium", "primary_archetype": "duty_free_retail_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | inventory_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 62900.0, "evidence_available_at_that_date": "duty-free / retail recovery event premium without confirmed Chinese traffic, basket size, inventory turn, markdown control or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["duty_free_retail_event", "tourist_traffic_recovery_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE90", "deep_MAE180", "traffic_inventory_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008770/2024.csv", "profile_path": "atlas/symbol_profiles/008/008770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.16, "MFE_90D_pct": 0.16, "MFE_180D_pct": 0.16, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.45, "MAE_90D_pct": -18.92, "MAE_180D_pct": -28.85, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-01", "peak_price": 63000.0, "drawdown_after_peak_pct": -28.97, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_duty_free_retail_inventory_event_cap", "four_b_evidence_type": ["duty_free_retail_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_duty_free_retail_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_duty_free_retail_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1999_CA_candidates", "same_entry_group_id": "R5L97_C19_008770_2024-04-01_62900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L97_C19_LOTTESHOPPING_2024_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_POSITIVE", "trigger_id": "R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE", "symbol": "023530", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 55, "policy_or_regulatory_score": 35, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "department_store_retail_inventory_margin_positive", "MFE_90D_pct": 28.27, "MAE_90D_pct": -11.0, "score_return_alignment_label": "department_store_retail_inventory_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L97_C19_FNF_2024_APPAREL_CHINA_INVENTORY_FALSE_STAGE2", "trigger_id": "R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "apparel_China_inventory_false_stage2", "MFE_90D_pct": 1.18, "MAE_90D_pct": -24.58, "score_return_alignment_label": "apparel_inventory_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_apparel_inventory_watch_counts_without_sellthrough_markdown_inventory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L97_C19_HOTELSHILLA_2024_DUTY_FREE_RETAIL_EVENT_CAP_4B", "trigger_id": "R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP", "symbol": "008770", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "duty_free_retail_event_cap_4B_guard", "MFE_90D_pct": 0.16, "MAE_90D_pct": -18.92, "score_return_alignment_label": "duty_free_retail_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_duty_free_retail_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "97", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_CHINA_INVENTORY_FALSE_STAGE2_AND_DUTY_FREE_RETAIL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "inventory_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["department_store_retail_inventory_margin_positive", "apparel_inventory_false_stage2", "duty_free_retail_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C19 rows need explicit inventory turn, channel sell-through, traffic/basket recovery, category mix, markdown discipline, margin or revision bridge before positive promotion.
- In C19, bridge-missing brand/retail event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C19 brand/retail inventory-margin rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 97
next_round = R6
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
