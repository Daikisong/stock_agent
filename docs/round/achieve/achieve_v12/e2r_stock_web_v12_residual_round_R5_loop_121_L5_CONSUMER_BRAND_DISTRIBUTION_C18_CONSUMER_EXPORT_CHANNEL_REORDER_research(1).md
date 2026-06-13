# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R5
selected_loop = 121
selected_large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
selected_fine_archetype_id = mixed_fine_leaf_set
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
loop_objective = coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test
output_filename = e2r_stock_web_v12_residual_round_R5_loop_121_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C18_consumer_export_channel_reorder_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference
active_profile_context = e2r_2_2 rolling profile exists in repository, but this MD does not patch production scoring.
```

Working assumption: current calibrated Stage2 can recognize export-channel evidence, but C18 needs a more specific gate. Export-channel news is useful only when it carries at least one of the following conversion bridges: repeat/reorder, owned overseas subsidiary sell-through, inventory replenishment with order growth, or margin/revision confirmation. A single global marketing or brand export headline without company-wide conversion should stay Stage2-watch or 4B-watch.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R5 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| primary archetype | consumer export channel reorder / repeat demand |
| allowed scope | consumer export channels, reorder cycles, overseas channel conversion, inventory restocking, repeat demand |
| excluded / compressed away | pure K-brand marketing without reorder bridge, C20 broad beauty/food distribution without repeat-order evidence |
| round consistency | R5/L5/C18 consistent |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index marks C18 as Priority 0 with only 3 representative rows before this loop. Existing top-covered C18 symbols are 003230, 011150, and 383220, so this loop deliberately uses four new symbols: 105630, 005180, 271560, 280360.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicates_found = 0
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_source | Songdaiki/stock-web |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| schema columns | d,o,h,l,c,v,a,mc,s,m |
| MFE/MAE method | max high / min low from entry_date through N tradable rows |
| validation_status | usable_for_historical_calibration |

## 5. Historical Eligibility Gate

All representative trigger rows pass the historical eligibility gate.

| symbol | entry_date | 180 forward rows | corporate action window | calibration_usable |
|---|---:|---:|---|---:|
| 105630 | 2024-02-29 | 180 | clean_180D_window; 2011 profile discontinuity outside window | true |
| 005180 | 2024-07-19 | 180 | clean_180D_window; old 1995/1996/1998 discontinuities outside window | true |
| 271560 | 2024-10-24 | 180 | clean_180D_window; profile has no corporate-action candidates | true |
| 280360 | 2024-10-24 | 180 | clean_180D_window; 2019/2022 profile discontinuities outside window | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | compressed canonical | rationale |
|---|---|---|
| APPAREL_US_INVENTORY_REORDER_CYCLE_MARGIN_BRIDGE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Apparel OEM recovery is a direct export-order/reorder cycle case. |
| FOOD_EXPORT_OVERSEAS_CHANNEL_SKU_DIVERSIFICATION_MARGIN_BRIDGE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Food export-channel expansion is routed to C18 only when SKU/store channel expansion is tested against margin/reorder path. |
| FOOD_OVERSEAS_SUBSIDIARY_REORDER_CAPEX_SEASONAL_DEMAND | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Owned overseas subsidiaries and production expansion convert channel demand into a cleaner reorder/capacity path. |
| SNACK_BRAND_GLOBAL_EXPORT_MARKETING_TO_PRODUCTION_BRIDGE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Single-brand global marketing is accepted as C18 only as a counterexample unless company-wide repeat-order/margin bridge is confirmed. |
| SINGLE_BRAND_EVENT_PREMIUM_WITHOUT_COMPANY_WIDE_REORDER_MARGIN_BRIDGE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 4B overlay leaf for event-premium risk, not a new positive canonical. |

## 7. Case Selection Summary

|symbol|company_name|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|positive|current_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|105630|한세실업|Stage2-Actionable|2024-02-29|20400.0|8.09|-11.27|24.26|-11.27|24.26|-35.59|2024-05-31|25350.0|-48.17|positive|current_profile_4B_too_late|
|005180|빙그레|Stage2-Actionable|2024-07-19|84000.0|9.17|-25.0|9.17|-29.52|19.52|-29.52|2025-04-03|100400.0|-13.15|counterexample|current_profile_false_positive|
|271560|오리온|Stage3-Yellow|2024-10-24|98700.0|7.5|-5.78|12.56|-5.78|28.98|-5.78|2025-05-09|127300.0|-17.52|positive|current_profile_correct|
|280360|롯데웰푸드|Stage2|2024-10-24|131100.0|0.92|-21.43|0.92|-24.1|0.92|-24.1|2024-10-24|132300.0|-24.79|counterexample|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

| bucket | cases | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct |
|---|---:|---:|---:|---:|---:|
| positive | 2 | 18.41 | -8.53 | 26.62 | -20.69 |
| counterexample | 2 | 5.04 | -26.81 | 10.22 | -26.81 |

Interpretation: C18 was not binary. Hansae captured a short/mid-term reorder-cycle move but later failed durability. Orion showed the cleanest structure because overseas channel evidence was tied to subsidiary sales and production expansion. Binggrae and Lotte Wellfood show that export-channel headlines can be bad entries when the bridge is only overseas share, SKU/channel expansion, or a single-brand campaign without repeat-order and margin confirmation.

## 9. Evidence Source Map

| symbol | evidence source | publication timing | source URL | key evidence used |
|---|---|---|---|---|
| 105630 | The Asia Business Daily | 2024-02-29 08:54 KST | https://www.asiae.co.kr/en/article/2024022908255047714 | inventory replenishment cycle, 2H order growth expectation, OP beat, cost-ratio improvement |
| 005180 | The Asia Business Daily | 2024-07-19 08:27 KST | https://www.asiae.co.kr/en/article/2024071908274821007 | overseas sales CAGR, overseas share, SKU/store channel expansion, U.S./China export growth |
| 271560 | The Asia Business Daily | 2024-10-24 07:10 KST | https://www.asiae.co.kr/en/article/2024102316472410538 | overseas sales >60%, China/Vietnam/Russia subsidiary growth, factory expansion, Costco Europe channel |
| 280360 | The Asia Business Daily | 2024-10-24 11:15 KST | https://www.asiae.co.kr/en/print.htm?idxno=2024102311243242649 | Pepero exports +30% YoY, 50+ countries, overseas production-line plan, global marketing campaign |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path |
|---|---|---|
| 105630 | atlas/ohlcv_tradable_by_symbol_year/105/105630/2024.csv | atlas/symbol_profiles/105/105630.json |
| 005180 | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv | atlas/symbol_profiles/005/005180.json |
| 271560 | atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv | atlas/symbol_profiles/271/271560.json |
| 280360 | atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv | atlas/symbol_profiles/280/280360.json |

## 11. Case-by-Case Trigger Grid

### 11.1 105630 한세실업 — positive but durability watch

Stage2-Actionable was justified by the inventory replenishment/order-growth bridge. The 90D MFE reached 24.26%, but 180D MAE reached -35.59%, so the case is useful both as a positive C18 reorder sample and a 4B durability-watch sample.

### 11.2 005180 빙그레 — counterexample / bad entry

Overseas sales expansion and SKU/channel growth were real, but the entry had only 9.17% MFE90 against -29.52% MAE90. This should not be promoted simply because the story says export growth.

### 11.3 271560 오리온 — cleanest positive

Overseas channel evidence was connected to subsidiary sales, production-line expansion, and Q4 seasonal demand. The path showed 28.98% MFE180 with only -5.78% MAE180.

### 11.4 280360 롯데웰푸드 — counterexample plus 4B overlay

Pepero export growth looked strong at the brand level, but the path showed only 0.92% MFE180 and -24.10% MAE180. Treat this as a single-brand event cap unless later company-wide margin/reorder data confirms conversion.

## 12. Trigger-Level OHLC Backtest Tables

|symbol|company_name|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|positive|current_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|105630|한세실업|Stage2-Actionable|2024-02-29|20400.0|8.09|-11.27|24.26|-11.27|24.26|-35.59|2024-05-31|25350.0|-48.17|positive|current_profile_4B_too_late|
|005180|빙그레|Stage2-Actionable|2024-07-19|84000.0|9.17|-25.0|9.17|-29.52|19.52|-29.52|2025-04-03|100400.0|-13.15|counterexample|current_profile_false_positive|
|271560|오리온|Stage3-Yellow|2024-10-24|98700.0|7.5|-5.78|12.56|-5.78|28.98|-5.78|2025-05-09|127300.0|-17.52|positive|current_profile_correct|
|280360|롯데웰푸드|Stage2|2024-10-24|131100.0|0.92|-21.43|0.92|-24.1|0.92|-24.1|2024-10-24|132300.0|-24.79|counterexample|current_profile_false_positive|

## 13. Current Calibrated Profile Stress Test

| symbol | likely current profile action | actual path verdict | stress-test result |
|---|---|---|---|
| 105630 | Stage2-Actionable accepted | MFE90 positive, but 180D drawdown severe | current_profile_4B_too_late |
| 005180 | Stage2-Actionable accepted too easily | high MAE90, delayed recovery | current_profile_false_positive |
| 271560 | Stage3-Yellow accepted | low MAE and good MFE180 | current_profile_correct |
| 280360 | Stage2 accepted too easily | near-zero MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable | Stage3-Yellow | Stage3-Green | green_lateness_ratio |
|---|---|---|---|---|
| 105630 | yes | no | no | not_applicable |
| 005180 | yes | no | no | not_applicable |
| 271560 | implied yes | yes | no | not_applicable |
| 280360 | yes | no | no | not_applicable |

No Stage3-Green trigger is proposed in this loop. The positive result for Orion supports Yellow rather than Green: overseas conversion evidence was strong, but this loop does not include confirmed post-trigger revision sufficient to loosen Green.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | overlay role | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| LOTTEWELLFOOD_280360_20241024_STAGE4B_OVERLAY_SINGLE_BRAND_EVENT_CAP | 4B_overlay_only | null | null | same-entry event-cap overlay; proximity formula is not meaningful because Stage2 and 4B share the same entry. Use as 4B-watch guard, not full positive evidence. |
| HANSAE_105630_20240229_STAGE2_ACTIONABLE_REORDER_CYCLE | durability watch | null | null | MFE90 worked, but 180D drawdown says C18 needs later 4B watch when reorder recovery lacks durable margin/revision follow-through. |

## 16. 4C Protection Audit

No hard Stage4C row is created. There is no explicit contract cancellation, qualification failure, accounting break, forced liquidation, or thesis evidence broken at the trigger dates. High MAE rows are treated as Stage2 false-positive / 4B-watch calibration, not 4C thesis-break evidence.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L5 export-channel evidence should be upgraded only when it includes repeat/reorder or owned-channel conversion plus margin/revision bridge. Marketing-led export headlines without company-wide conversion remain Stage2-watch or 4B-watch.
rule_scope = sector_specific
confidence = medium
production_scoring_changed = false
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C18_reorder_margin_conversion_gate
candidate_gate = repeat_order_or_reorder_cycle OR owned_overseas_channel_sales_conversion OR inventory_replenishment_with_order_growth
plus_required_bridge = margin_bridge OR revision_bridge OR production_capacity_conversion
negative_guard = single_brand_marketing_event OR export_share_small_and_late_entry OR no_company_wide_margin_bridge
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible reps | avg_MFE90 | avg_MAE90 | false-positive reps | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | accepts export-channel Stage2 broadly | 4 | 11.73 | -17.67 | 2 | too broad for C18 |
| P0b e2r_2_0_baseline_reference | less sensitive to channel evidence | 4 | not rerun | not rerun | unknown | baseline only |
| P1 L5 sector candidate | require reorder/margin bridge | 4 | 18.41 positive bucket | -8.53 positive bucket | 1 | better |
| P2 C18 canonical candidate | classify one-brand/export-share-only as watch | 4 | 18.41 positive bucket | -26.81 counter bucket avoided | 0-1 | best shadow hypothesis |
| P3 counterexample guard | demote high-MAE export headlines | 2 counterexamples | 5.04 | -26.81 | 0 if guard applied | useful |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 105630 | 72 | Stage2-Actionable | 70 | Stage2-Actionable | 24.26 | -11.27 | 90D good / 180D durability watch |
| 005180 | 76 | Stage2-Actionable | 64 | Stage2-watch | 9.17 | -29.52 | before too high |
| 271560 | 78 | Stage3-Yellow | 80 | Stage3-Yellow | 12.56 | -5.78 | good |
| 280360 | 72 | Stage2-Actionable | 58 | Stage2-watch | 0.92 | -24.1 | before too high |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | mixed_fine_leaf_set | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 3 | yes | yes | C18 rows 3 -> 7 if accepted; need 23 more to 30, 43 more to 50 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [export_channel_headline_false_positive, single_brand_event_cap_without_company_wide_margin_bridge, late_entry_high_MAE_after_export_rerating, durability_break_after_reorder_cycle]
new_axis_proposed: c18_reorder_margin_conversion_gate
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: yes
canonical_archetype_rule_candidate: yes
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- C18 priority-gap selection.
- New symbol and trigger-family selection.
- Actual stock-web 1D OHLCV entry row, entry close, and 30/90/180D MFE/MAE.
- Corporate-action window status against symbol profile caveats.
- Positive/counterexample balance inside the same canonical archetype.

Not validated:
- No production scoring code was opened or patched.
- No brokerage/live scan/current candidate discovery was performed.
- No investment recommendation is made.
- No 1Y/2Y fields are asserted.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_reorder_margin_conversion_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Require repeat/reorder or owned channel conversion plus margin/revision bridge before Stage2-Actionable/Yellow; marketing-only export headlines stay Stage2-watch/4B-watch","Positive reps avg MFE90=18.41 avg MAE90=-8.53; counter reps avg MFE90=5.04 avg MAE90=-26.81","HANSAE_105630_20240229_STAGE2_ACTIONABLE_REORDER_CYCLE|BINGGRAE_005180_20240719_STAGE2_ACTIONABLE_EXPORT_CHANNEL|ORION_271560_20241024_STAGE3_YELLOW_OVERSEAS_SUBSIDIARY|LOTTEWELLFOOD_280360_20241024_STAGE2_PEPERO_EXPORT_CHANNEL",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","manifest_generated_at":"2026-05-21T16:28:39.421691+00:00"}
{"row_type":"case","case_id":"C18_R5L121_105630_HANSAE_APPAREL_REORDER_20240229","symbol":"105630","company_name":"한세실업","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_US_INVENTORY_REORDER_CYCLE_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"HANSAE_105630_20240229_STAGE2_ACTIONABLE_REORDER_CYCLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_90D_capture_but_durability_guard_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"C18 positive sample for order/reorder recovery; not Green-quality because ASP/FX pressure and later 180D drawdown stayed material."}
{"row_type":"case","case_id":"C18_R5L121_005180_BINGGRAE_EXPORT_CHANNEL_20240719","symbol":"005180","company_name":"빙그레","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"FOOD_EXPORT_OVERSEAS_CHANNEL_SKU_DIVERSIFICATION_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"BINGGRAE_005180_20240719_STAGE2_ACTIONABLE_EXPORT_CHANNEL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"poor_score_return_alignment_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C18 counterexample: overseas channel growth alone did not protect entry risk after a crowded rerating."}
{"row_type":"case","case_id":"C18_R5L121_271560_ORION_OVERSEAS_SUBSIDIARY_20241024","symbol":"271560","company_name":"오리온","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"FOOD_OVERSEAS_SUBSIDIARY_REORDER_CAPEX_SEASONAL_DEMAND","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"ORION_271560_20241024_STAGE3_YELLOW_OVERSEAS_SUBSIDIARY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_alignment_low_MAE_positive_MFE180","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Best positive in this loop: overseas channel evidence is anchored in owned subsidiary sales and capacity, not only marketing."}
{"row_type":"case","case_id":"C18_R5L121_280360_LOTTEWELLFOOD_PEPERO_EXPORT_20241024","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SNACK_BRAND_GLOBAL_EXPORT_MARKETING_TO_PRODUCTION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"LOTTEWELLFOOD_280360_20241024_STAGE2_PEPERO_EXPORT_CHANNEL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"poor_alignment_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"This is the clearest counterexample: a plausible export headline did not become a tradable C18 rerating path."}
{"row_type":"trigger","trigger_id":"HANSAE_105630_20240229_STAGE2_ACTIONABLE_REORDER_CYCLE","case_id":"C18_R5L121_105630_HANSAE_APPAREL_REORDER_20240229","symbol":"105630","company_name":"한세실업","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_US_INVENTORY_REORDER_CYCLE_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":20400.0,"entry_price_basis":"close","evidence_available_at_that_date":"published 2024-02-29 08:54 KST; before KRX open; same-day close entry","evidence_source":"The Asia Business Daily, 2024-02-29, Hansae recovery / inventory replenishment cycle article","evidence_source_url":"https://www.asiae.co.kr/en/article/2024022908255047714","stage2_evidence_fields":["public_broker_report","inventory_replenishment_cycle_expected","2H_orders_expected_up_28pct_yoy","4Q_OP_beat","cost_ratio_improvement"],"stage3_evidence_fields":["partial_margin_bridge","revenue_rebound_expected","fixed_cost_absorption_route"],"stage4b_evidence_fields":["180D_durability_drawdown_watch","ASP_decline_and_FX_pressure"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105630/2024.csv","profile_path":"atlas/symbol_profiles/105/105630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.09,"MFE_90D_pct":24.26,"MFE_180D_pct":24.26,"MAE_30D_pct":-11.27,"MAE_90D_pct":-11.27,"MAE_180D_pct":-35.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":25350.0,"max_drawdown_low":13140.0,"max_drawdown_low_date":"2024-11-21","drawdown_after_peak_pct":-48.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["180D_durability_drawdown_watch","ASP_decline_and_FX_pressure"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"apparel_inventory_reorder_cycle_mfe90_positive_but_180d_durability_break","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates outside selected 180D window or none","same_entry_group_id":"C18_105630_2024-02-29_20400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_note":"Article title translation says Hansae Yes24 Holdings, but the report body describes Hanse Industrial/Hansae operating metrics and Hana target price; routed to 105630 with profile name 한세실업."}
{"row_type":"trigger","trigger_id":"BINGGRAE_005180_20240719_STAGE2_ACTIONABLE_EXPORT_CHANNEL","case_id":"C18_R5L121_005180_BINGGRAE_EXPORT_CHANNEL_20240719","symbol":"005180","company_name":"빙그레","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"FOOD_EXPORT_OVERSEAS_CHANNEL_SKU_DIVERSIFICATION_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-19","entry_date":"2024-07-19","entry_price":84000.0,"entry_price_basis":"close","evidence_available_at_that_date":"published 2024-07-19 08:27 KST; before KRX open; same-day close entry","evidence_source":"The Asia Business Daily, 2024-07-19, Binggrae overseas sales expansion article","evidence_source_url":"https://www.asiae.co.kr/en/article/2024071908274821007","stage2_evidence_fields":["overseas_sales_CAGR_19pct_5y","overseas_sales_share_up_to_10_5pct","US_ice_cream_export_growth","China_refrigerated_products_growth","SKU_and_store_channel_expansion"],"stage3_evidence_fields":["profitability_improvement_expected_but_not_confirmed_as_repeat_reorder","no_company_wide_reorder_confirmation"],"stage4b_evidence_fields":["positioning_overheat","valuation_repricing_overheat","high_MAE_after_entry"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.17,"MFE_90D_pct":9.17,"MFE_180D_pct":19.52,"MAE_30D_pct":-25.0,"MAE_90D_pct":-29.52,"MAE_180D_pct":-29.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-04-03","peak_price":100400.0,"max_drawdown_low":87200.0,"max_drawdown_low_date":"2025-04-09","drawdown_after_peak_pct":-13.15,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["positioning_overheat","valuation_repricing_overheat","high_MAE_after_entry"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"export_channel_headline_bad_entry_high_MAE_without_repeat_order_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates outside selected 180D window or none","same_entry_group_id":"C18_005180_2024-07-19_84000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_note":"Overseas CAGR and channel expansion are real, but overseas share was still 10.5% in 2023 and the entry followed a large prior rerating."}
{"row_type":"trigger","trigger_id":"ORION_271560_20241024_STAGE3_YELLOW_OVERSEAS_SUBSIDIARY","case_id":"C18_R5L121_271560_ORION_OVERSEAS_SUBSIDIARY_20241024","symbol":"271560","company_name":"오리온","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"FOOD_OVERSEAS_SUBSIDIARY_REORDER_CAPEX_SEASONAL_DEMAND","sector":"consumer_brand_distribution","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-10-24","entry_date":"2024-10-24","entry_price":98700.0,"entry_price_basis":"close","evidence_available_at_that_date":"published 2024-10-24 07:10 KST; before KRX open; same-day close entry","evidence_source":"The Asia Business Daily, 2024-10-24, Orion overseas subsidiary sales / 3 trillion won club article","evidence_source_url":"https://www.asiae.co.kr/en/article/2024102316472410538","stage2_evidence_fields":["overseas_sales_ratio_above_60pct","China_Vietnam_Russia_sales_bridge","Costco_Europe_channel_entry","seasonal_Q4_demand"],"stage3_evidence_fields":["multi_country_subsidiary_sales_visibility","China_Vietnam_Russia_growth_forecasts","factory_expansion_and_production_line_evidence","annual_sales_3T_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","profile_path":"atlas/symbol_profiles/271/271560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.5,"MFE_90D_pct":12.56,"MFE_180D_pct":28.98,"MAE_30D_pct":-5.78,"MAE_90D_pct":-5.78,"MAE_180D_pct":-5.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-05-09","peak_price":127300.0,"max_drawdown_low":105000.0,"max_drawdown_low_date":"2025-06-23","drawdown_after_peak_pct":-17.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"overseas_subsidiary_reorder_and_capacity_bridge_positive_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates outside selected 180D window or none","same_entry_group_id":"C18_271560_2024-10-24_98700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_note":"Routed to C18 because the source ties overseas subsidiary channel demand, factory expansion, holiday demand and product exports to sales conversion rather than a pure K-food brand headline."}
{"row_type":"trigger","trigger_id":"LOTTEWELLFOOD_280360_20241024_STAGE2_PEPERO_EXPORT_CHANNEL","case_id":"C18_R5L121_280360_LOTTEWELLFOOD_PEPERO_EXPORT_20241024","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SNACK_BRAND_GLOBAL_EXPORT_MARKETING_TO_PRODUCTION_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-10-24","entry_date":"2024-10-24","entry_price":131100.0,"entry_price_basis":"close","evidence_available_at_that_date":"published 2024-10-24 11:15 KST; during KRX session; same-day close entry","evidence_source":"The Asia Business Daily, 2024-10-24, Lotte Wellfood Pepero global brand / export expansion article","evidence_source_url":"https://www.asiae.co.kr/en/print.htm?idxno=2024102311243242649","stage2_evidence_fields":["Pepero_export_value_1H24_up_30pct_yoy","overseas_brand_sales_surpassed_domestic_brand_sales","sold_in_50_plus_countries","North_America_SE_Asia_export_expansion_plan","India_production_line_plan"],"stage3_evidence_fields":["brand_level_growth_only","company_wide_reorder_margin_bridge_missing","production_bridge_lagged_to_mid_2025"],"stage4b_evidence_fields":["explicit_event_cap","single_brand_event_premium","margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv","profile_path":"atlas/symbol_profiles/280/280360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.92,"MFE_90D_pct":0.92,"MFE_180D_pct":0.92,"MAE_30D_pct":-21.43,"MAE_90D_pct":-24.1,"MAE_180D_pct":-24.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-24","peak_price":132300.0,"max_drawdown_low":99500.0,"max_drawdown_low_date":"2025-02-03","drawdown_after_peak_pct":-24.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["explicit_event_cap","single_brand_event_premium","margin_bridge_missing"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"single_brand_export_event_counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates outside selected 180D window or none","same_entry_group_id":"C18_280360_2024-10-24_131100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_note":"Pepero export data are strong at brand level; C18 counterexample because company-wide repeat-order/margin bridge was not confirmed at entry."}
{"row_type":"trigger","trigger_id":"LOTTEWELLFOOD_280360_20241024_STAGE4B_OVERLAY_SINGLE_BRAND_EVENT_CAP","case_id":"C18_R5L121_280360_LOTTEWELLFOOD_PEPERO_EXPORT_20241024","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SINGLE_BRAND_EVENT_PREMIUM_WITHOUT_COMPANY_WIDE_REORDER_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-10-24","entry_date":"2024-10-24","entry_price":131100.0,"entry_price_basis":"close","evidence_available_at_that_date":"published 2024-10-24 11:15 KST; during KRX session; same-day close entry","evidence_source":"The Asia Business Daily, 2024-10-24, Lotte Wellfood Pepero global brand / export expansion article","evidence_source_url":"https://www.asiae.co.kr/en/print.htm?idxno=2024102311243242649","stage2_evidence_fields":["Pepero_export_value_1H24_up_30pct_yoy","overseas_brand_sales_surpassed_domestic_brand_sales","sold_in_50_plus_countries","North_America_SE_Asia_export_expansion_plan","India_production_line_plan"],"stage3_evidence_fields":["brand_level_growth_only","company_wide_reorder_margin_bridge_missing","production_bridge_lagged_to_mid_2025"],"stage4b_evidence_fields":["explicit_event_cap","single_brand_event_premium","margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv","profile_path":"atlas/symbol_profiles/280/280360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.92,"MFE_90D_pct":0.92,"MFE_180D_pct":0.92,"MAE_30D_pct":-21.43,"MAE_90D_pct":-24.1,"MAE_180D_pct":-24.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-24","peak_price":132300.0,"max_drawdown_low":99500.0,"max_drawdown_low_date":"2025-02-03","drawdown_after_peak_pct":-24.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"same_entry_event_cap_overlay; proximity_formula_not_meaningful; treat_as_4B_watch_not_full_positive","four_b_evidence_type":["explicit_event_cap","single_brand_event_premium","margin_bridge_missing"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"4B_overlay_single_brand_event_cap_should_not_promote_positive_stage","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates outside selected 180D window or none","same_entry_group_id":"C18_280360_2024-10-24_131100","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.4,"do_not_count_as_new_case":true,"source_note":"Pepero export data are strong at brand level; C18 counterexample because company-wide repeat-order/margin bridge was not confirmed at entry."}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L121_105630_HANSAE_APPAREL_REORDER_20240229","trigger_id":"HANSAE_105630_20240229_STAGE2_ACTIONABLE_REORDER_CYCLE","symbol":"105630","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable","changed_components":["durability_guard","4B_watch_after_peak"],"component_delta_explanation":"C18 positive sample for order/reorder recovery; not Green-quality because ASP/FX pressure and later 180D drawdown stayed material.","MFE_90D_pct":24.26,"MAE_90D_pct":-11.27,"score_return_alignment_label":"good_90D_capture_but_durability_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L121_005180_BINGGRAE_EXPORT_CHANNEL_20240719","trigger_id":"BINGGRAE_005180_20240719_STAGE2_ACTIONABLE_EXPORT_CHANNEL","symbol":"005180","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-watch","changed_components":["late_entry_penalty","export_share_floor","reorder_confirmation_required"],"component_delta_explanation":"C18 counterexample: overseas channel growth alone did not protect entry risk after a crowded rerating.","MFE_90D_pct":9.17,"MAE_90D_pct":-29.52,"score_return_alignment_label":"poor_score_return_alignment_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L121_271560_ORION_OVERSEAS_SUBSIDIARY_20241024","trigger_id":"ORION_271560_20241024_STAGE3_YELLOW_OVERSEAS_SUBSIDIARY","symbol":"271560","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":2,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":2,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["owned_subsidiary_channel_bridge","capacity_and_seasonality_confirmed"],"component_delta_explanation":"Best positive in this loop: overseas channel evidence is anchored in owned subsidiary sales and capacity, not only marketing.","MFE_90D_pct":12.56,"MAE_90D_pct":-5.78,"score_return_alignment_label":"good_alignment_low_MAE_positive_MFE180","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L121_280360_LOTTEWELLFOOD_PEPERO_EXPORT_20241024","trigger_id":"LOTTEWELLFOOD_280360_20241024_STAGE2_PEPERO_EXPORT_CHANNEL","symbol":"280360","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-watch","changed_components":["single_brand_event_cap","company_wide_margin_bridge_required"],"component_delta_explanation":"This is the clearest counterexample: a plausible export headline did not become a tradable C18 rerating path.","MFE_90D_pct":0.92,"MAE_90D_pct":-24.1,"score_return_alignment_label":"poor_alignment_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L121_280360_LOTTEWELLFOOD_PEPERO_EXPORT_20241024","trigger_id":"LOTTEWELLFOOD_280360_20241024_STAGE4B_OVERLAY_SINGLE_BRAND_EVENT_CAP","symbol":"280360","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-watch","changed_components":["single_brand_event_cap","company_wide_margin_bridge_required"],"component_delta_explanation":"Overlay only; not aggregate representative. Same entry group as the Lotte Stage2 row.","MFE_90D_pct":0.92,"MAE_90D_pct":-24.1,"score_return_alignment_label":"4B_overlay_guardrail_alignment","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R5","loop":"121","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["export_channel_headline_false_positive","single_brand_event_cap_without_company_wide_margin_bridge","late_entry_high_MAE_after_export_rerating","durability_break_after_reorder_cycle"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"c18_reorder_margin_conversion_gate","sector_specific_rule_candidate":"L5_export_channel_reorder_requires_repeat_order_or_owned_channel_conversion_plus_margin_bridge","canonical_archetype_rule_candidate":"C18 promote only when export channel evidence has repeat/reorder or owned-subsidiary conversion and margin/revision bridge; otherwise Stage2-watch/4B-watch"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
this_loop_selected_round = R5
this_loop_selected_canonical = C18_CONSUMER_EXPORT_CHANNEL_REORDER
coverage_after_if_accepted = C18 representative rows 3 -> 7
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_schedule_status = coverage_index_first_not_sequential
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- 105630 evidence: https://www.asiae.co.kr/en/article/2024022908255047714
- 005180 evidence: https://www.asiae.co.kr/en/article/2024071908274821007
- 271560 evidence: https://www.asiae.co.kr/en/article/2024102316472410538
- 280360 evidence: https://www.asiae.co.kr/en/print.htm?idxno=2024102311243242649
