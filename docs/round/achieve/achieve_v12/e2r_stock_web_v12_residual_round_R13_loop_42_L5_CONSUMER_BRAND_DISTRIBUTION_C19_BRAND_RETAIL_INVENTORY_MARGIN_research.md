# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 42
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = SNOWPEAK_APPAREL_DOMESTIC_REORDER_GROSS_MARGIN | ATHLEISURE_CHANNEL_REORDER_MARGIN_EXPANSION | CHINA_MLB_CHANNEL_INVENTORY_REORDER_RISK | LIFESTYLE_APPAREL_INVENTORY_MARGIN_OVERHANG
loop_objective = holdout_validation, residual_false_positive_mining, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
```

This file is historical calibration research only. It is not live candidate discovery, not investment recommendation language, and not a repository patch.

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

The residual question here is not whether Stage2 is generally earlier than Green. The question is narrower: in consumer-brand retail, when does brand heat become a true reorder/margin engine, and when is it just a shiny storefront with inventory stacked behind the curtain?

## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L5_CONSUMER_BRAND_DISTRIBUTION`
- canonical_archetype_id: `C19_BRAND_RETAIL_INVENTORY_MARGIN`
- sector: 소비재·유통·브랜드
- primary_archetype: brand retail inventory margin
- case roles: 2 positive structural/reorder cases, 2 counterexample/4C cases.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact access was limited to calibration summaries and registry-like files. The ingest summary already covers R1~R13 and loops 1~9, with 107 parsed result MDs, 4,951 raw trigger rows, 1,940 validated trigger rows, and 1,376 aggregate representative rows. Direct search for `C19_BRAND_RETAIL_INVENTORY_MARGIN` returned no exact previous canonical-id hit in the accessible artifacts. Therefore this loop is treated as new canonical residual coverage rather than schema rematerialization.

```text
required_new_independent_case_ratio = 0.60
calibration_usable_case_count = 4
new_independent_case_count = 4
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was read before trigger calculation.

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Relevant manifest fields:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The schema confirms that tradable shards use `d,o,h,l,c,v,a,mc,s,m`, and that calibration requires positive OHLC/volume, 180 forward tradable rows, computed 30D/90D/180D MFE/MAE, and no corporate-action-contaminated 180D window.

## 5. Historical Eligibility Gate

All four representative cases satisfy the historical gate.

| symbol | profile_path | entry_year | profile_status | corporate_action_overlap_180D | forward_window | calibration_usable |
| --- | --- | --- | --- | --- | --- | --- |
| 036620 | atlas/symbol_profiles/036/036620.json | 2023/2024 | active_like | none in tested window | >=180 trading days | true |
| 337930 | atlas/symbol_profiles/337/337930.json | 2023/2024 | active_like | none in tested window | >=180 trading days | true |
| 383220 | atlas/symbol_profiles/383/383220.json | 2023/2024 | active_like | none in tested window | >=180 trading days | true |
| 298540 | atlas/symbol_profiles/298/298540.json | 2023/2024 | active_like | none in tested window | >=180 trading days | true |


Corporate-action candidate dates in profiles were outside the tested windows:
- 036620: 2000-05-24, 2000-06-16, 2017-05-26, 2018-12-21.
- 337930: 2021-09-23.
- 383220: 2022-04-13.
- 298540: 2021-08-02, 2021-08-30.

## 6. Canonical Archetype Compression Map

```text
SNOWPEAK_APPAREL_DOMESTIC_REORDER_GROSS_MARGIN -> C19_BRAND_RETAIL_INVENTORY_MARGIN
ATHLEISURE_CHANNEL_REORDER_MARGIN_EXPANSION -> C19_BRAND_RETAIL_INVENTORY_MARGIN
CHINA_MLB_CHANNEL_INVENTORY_REORDER_RISK -> C19_BRAND_RETAIL_INVENTORY_MARGIN
LIFESTYLE_APPAREL_INVENTORY_MARGIN_OVERHANG -> C19_BRAND_RETAIL_INVENTORY_MARGIN
```

Compression logic: C19 is not just “consumer brand.” It requires brand demand to convert into sell-through, clean inventory, and gross-margin stability. When those links are missing, brand heat behaves like a bright shop window with the warehouse quietly flooding behind it.

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | current_profile_verdict | new? |
| --- | --- | --- | --- | --- | --- | --- |
| R13L42-C19-036620-GAMSUNG-2024-REORDER-MARGIN | 036620 | 감성코퍼레이션 | positive | TRG-R13L42-036620-S2A-20240222 | current_profile_too_late | true |
| R13L42-C19-337930-BRANDX-2024-ATHLEISURE-REORDER | 337930 | 브랜드엑스코퍼레이션/젝시믹스 | positive | TRG-R13L42-337930-S2A-20240529 | current_profile_too_late | true |
| R13L42-C19-383220-FNF-2023-CHINA-INVENTORY-COUNTER | 383220 | F&F | counterexample | TRG-R13L42-383220-S2-20230906 | current_profile_false_positive | true |
| R13L42-C19-298540-NATURE-2024-INVENTORY-COUNTER | 298540 | 더네이쳐홀딩스 | counterexample | TRG-R13L42-298540-S2-20240215 | current_profile_4C_too_late | true |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 2
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
counterexample_search_incomplete = false
```

The two positive cases show that early C19 Stage2 can work when reorder/sell-through quality is visible before formal Green. The two counterexamples show that the same “brand/channel” language becomes dangerous when inventory and margin bridge are not clean.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|
| 036620 | apparel brand reorder | relative strength, sell-through/reorder proxy, early revision | later margin/revision confirmation | price-only/local overheat after May 2024 peak |
| 337930 | athleisure channel expansion | channel reorder, brand traction, margin bridge | later confirmed operating leverage | valuation/positioning blowoff in Oct 2024 |
| 383220 | China/MLB channel risk | brand/channel narrative, but weak inventory proof | unsupported for positive Green | thesis-break/margin slowdown after Nov 2023 |
| 298540 | lifestyle apparel inventory overhang | brand presence, but weak margin proof | unsupported for positive Green | inventory/margin thesis break by mid-2024 |

Evidence source labels are research proxies using public disclosure/quarterly result timing plus verified stock-web OHLC entry rows. This MD does not claim to have parsed production scoring code or live source collectors.

## 10. Price Data Source Map

| symbol | tradable_shard | profile | basis | manifest_max_date |
| --- | --- | --- | --- | --- |
| 036620 | atlas/ohlcv_tradable_by_symbol_year/036/036620/<year>.csv | atlas/symbol_profiles/036/036620.json | tradable_raw | 2026-02-20 |
| 337930 | atlas/ohlcv_tradable_by_symbol_year/337/337930/<year>.csv | atlas/symbol_profiles/337/337930.json | tradable_raw | 2026-02-20 |
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/<year>.csv | atlas/symbol_profiles/383/383220.json | tradable_raw | 2026-02-20 |
| 298540 | atlas/ohlcv_tradable_by_symbol_year/298/298540/<year>.csv | atlas/symbol_profiles/298/298540.json | tradable_raw | 2026-02-20 |


## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG-R13L42-036620-S2A-20240222 | 036620 | Stage2-Actionable | 2024-02-22 | 3025 | 55.04 | -6.28 | 55.04 | -6.28 | current_profile_too_late | representative |
| TRG-R13L42-036620-GREEN-20240523 | 036620 | Stage3-Green | 2024-05-23 | 4505 | 4.11 | -35.18 | 4.11 | -37.85 | current_profile_too_late | label_comparison_only |
| TRG-R13L42-337930-S2A-20240529 | 337930 | Stage2-Actionable | 2024-05-29 | 5750 | 132.7 | -8.7 | 132.7 | -12.17 | current_profile_too_late | representative |
| TRG-R13L42-337930-4B-20241002 | 337930 | Stage4B | 2024-10-02 | 12540 | 6.7 | -59.73 | 6.7 | -59.73 | current_profile_4B_too_late | 4B_overlay_only |
| TRG-R13L42-383220-S2-20230906 | 383220 | Stage2 | 2023-09-06 | 112400 | 6.67 | -37.46 | 6.67 | -45.64 | current_profile_false_positive | representative |
| TRG-R13L42-383220-4C-20231115 | 383220 | Stage4C | 2023-11-15 | 91500 | 2.08 | -27.1 | 2.08 | -37.38 | current_profile_4C_too_late | 4C_overlay_only |
| TRG-R13L42-298540-S2-20240215 | 298540 | Stage2 | 2024-02-15 | 15550 | 3.79 | -21.8 | 3.79 | -42.77 | current_profile_false_positive | representative |
| TRG-R13L42-298540-4C-20240614 | 298540 | Stage4C | 2024-06-14 | 13580 | 0.22 | -29.6 | 0.22 | -36.67 | current_profile_4C_too_late | 4C_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate triggers:

| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 036620 | 2024-02-22 | 3025 | 27.44 | -6.28 | 55.04 | -6.28 | 55.04 | -6.28 | 2024-05-24 | 4690 | -46.91 |
| 337930 | 2024-05-29 | 5750 | 58.96 | -8.7 | 132.7 | -8.7 | 132.7 | -12.17 | 2024-10-07 | 13380 | -62.26 |
| 383220 | 2023-09-06 | 112400 | 6.67 | -13.61 | 6.67 | -37.46 | 6.67 | -45.64 | 2023-09-18 | 119900 | -49.04 |
| 298540 | 2024-02-15 | 15550 | 3.79 | -10.03 | 3.79 | -21.8 | 3.79 | -42.77 | 2024-02-19 | 16140 | -44.86 |


Interpretation:
- 036620 and 337930 prove the constructive side of C19: when inventory/sell-through quality and margin bridge are clean enough, early Stage2 captures materially more upside than confirmed Green.
- 383220 and 298540 prove the guard side: brand heat without inventory/margin proof produces low MFE and severe MAE.

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely behavior | actual path | verdict |
|---|---|---|---|
| 036620 | Waits for confirmed revision/Green; Stage2 signal exists but under-credited as C19-specific. | Stage2 entry +55.04% MFE90, Green entry only +4.11% MFE90 with much worse drawdown. | current_profile_too_late |
| 337930 | Accepts after visible strength but 4B overlay may lag until price damage begins. | Stage2 entry +132.70% MFE90; 4B proximity 0.89 near full-window peak. | current_profile_too_late |
| 383220 | Can overread brand/channel recovery without inventory proof. | MFE180 +6.67%, MAE180 -45.64%. | current_profile_false_positive |
| 298540 | Can treat brand retail presence as watchlist even when inventory/margin bridge is absent. | MFE180 +3.79%, MAE180 -42.77%. | current_profile_false_positive / current_profile_4C_too_late |

Answers to required stress-test questions:
1. Current profile is directionally better than E2R 2.0, but C19 needs separate sell-through/inventory fields.
2. Positive cases match MFE/MAE only when entry is allowed before confirmed Green.
3. Stage2 bonus is not globally too high; it is too blunt for C19.
4. Yellow 75 is okay as a global floor but misses the difference between clean reorder and brand heat.
5. Green 87/revision 55 is too late for early C19 reorder cases and still too permissive for brand-only false positives if inventory is unscored.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate.
8. Hard 4C routing is too late when inventory/margin evidence is already broken.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green/late entry | peak after Stage2 | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- | --- |
| 036620 | 3025 | 4505 | 4690 | 0.889 | Green captures almost none of the early upside. |
| 337930 | 5750 | 8350 | 13380 | 0.341 | Green is somewhat late but still before most upside; 4B overlay matters more. |
| 383220 | 112400 | n/a | 119900 | not_applicable | No supported positive Green; brand heat should be blocked. |
| 298540 | 15550 | n/a | 16140 | not_applicable | No supported positive Green; margin/inventory guard dominates. |


## 15. 4B Local vs Full-window Timing Audit

| trigger | stage2_entry | 4B_entry | local_peak | full_peak | local_proximity | full_proximity | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TRG-R13L42-337930-4B-20241002 | 5750 | 12540 | 13380 | 13380 | 0.89 | 0.89 | good_full_window_4B_timing |
| TRG-R13L42-036620-GREEN-20240523 / implicit local overheat | 3025 | 4595 | 4690 | 4690 | 0.94 | 0.94 | price-only local 4B useful as overlay, not positive-stage promotion |


C19 needs 4B as an overlay: after a consumer brand rerates, the same store traffic that created the thesis can turn into a crowded narrative. The price is no longer a receipt; it becomes a queue.

## 16. 4C Protection Audit

| trigger | prior_stage_peak | 4C_entry | MAE90_after_4C | max_drawdown_after_prior_peak | protection_label |
| --- | --- | --- | --- | --- | --- |
| TRG-R13L42-383220-4C-20231115 | 119900 | 91500 | -27.1 | -49.04 | hard_4c_success |
| TRG-R13L42-298540-4C-20240614 | 16140 | 13580 | -29.6 | -44.86 | hard_4c_success |


A precise four_c_protection_score is not promoted here because prior-stage peak windows and disclosure timing are research-proxy level. The label is still useful: both 4C triggers would have reduced exposure before the deepest drawdowns.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_brand_retail_valuation_4B_overlay
candidate_delta = +1 overlay sensitivity
condition = brand retail rerating >70% of observed full-window upside AND valuation/positioning evidence exists
effect = convert late-stage positive label to 4B overlay, not hard sell signal
```

This is sector-scoped because consumer brand narratives often rerate sharply on channel stories before the next revision print. The rule should not become global without multi-sector evidence.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN

positive promotion rule:
+2 C19_sell_through_inventory_quality_bonus
applies when:
- reorder/sell-through quality is visible,
- inventory quality is not deteriorating,
- gross-margin bridge is plausible,
- brand heat is supported by channel conversion rather than only traffic/search/price.

counterexample guard:
-3 C19_inventory_margin_absence_guard
applies when:
- brand/channel narrative exists,
- but inventory, markdown, gross margin, or channel stock evidence is weak/broken,
- and revision quality is not confirmed.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | selected_entries | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | late_green_count | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | global proxy | 4 | 4 representative | 49.55 | -18.48 | 49.55 | -26.72 | 50% | 2 | brand heat still overpromotes F&F/Nature and Green can be late |
| P0b e2r_2_0_baseline_reference | rollback | 4 | 4 representative | 49.55 | -18.48 | 49.55 | -26.72 | 50%+ | 2 | worse: no stock-web guards and weaker 4C separation |
| P1 sector_specific_candidate_profile | L5 | 4 | 036620,337930 + 4B overlay | 93.87 | -7.49 | 93.87 | -9.23 | 0% | 1 | best risk-adjusted fit for L5 consumer brand retail |
| P2 canonical_archetype_candidate_profile | C19 | 4 | 036620,337930 only | 93.87 | -7.49 | 93.87 | -9.23 | 0% | 1 | canonical rule candidate |
| P3 counterexample_guard_profile | C19 guard | 4 | reject F&F/Nature, watch positives until sell-through proof | 93.87 | -7.49 | 93.87 | -9.23 | 0% | 1 | safer but may delay early positives |


## 20. Score-Return Alignment Matrix

| case | before_stage | after_stage | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 036620 | Stage3-Yellow | Stage2-Actionable/C19-promote | 55.04 | -6.28 | aligned |
| 337930 | Stage3-Yellow | Stage2-Actionable/C19-promote | 132.7 | -8.7 | aligned |
| 383220 | Stage2/Yellow-risk | Rejected-positive/4C-watch | 6.67 | -37.46 | false_positive_removed |
| 298540 | Stage2-watch | 4C-watch/rejected-positive | 3.79 | -21.8 | false_positive_removed |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | SNOWPEAK_APPAREL / ATHLEISURE / CHINA_INVENTORY / LIFESTYLE_APPAREL | 2 | 2 | 1 | 2 | 4 | 0 | 8 | 4 | 4 | true | true | Need C19 holdout for footwear/sports OEM and offline-store-heavy retailers. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - late_green_after_brand_rerating
  - brand_heat_false_positive
  - inventory_margin_4C_late
  - valuation_4B_overlay_needed
new_axis_proposed:
  - C19_sell_through_inventory_quality_bonus
  - C19_inventory_margin_absence_guard
  - L5_brand_retail_valuation_4B_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web manifest and schema basis.
- symbol profiles for all four cases.
- stock-web tradable OHLC rows for trigger entry windows.
- MFE/MAE proxy calculations from actual tradable OHLC rows.
- 180D forward window availability by manifest/profile max date.

Not validated:
- production `stock_agent` scoring code.
- live scanner output.
- broker/API data.
- current candidate suitability.
- adjusted-price return series.
- exact analyst-consensus revision timestamps.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_sell_through_inventory_quality_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+2,+2,"Positive cases rerated when reorder/sell-through and gross-margin stability were visible before confirmed Green.","Improves positive alignment: 036620/337930 selected before late Green.","TRG-R13L42-036620-S2A-20240222|TRG-R13L42-337930-S2A-20240529",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C19_inventory_margin_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,-3,-3,"Brand heat/channel presence without inventory-quality and margin bridge produced false positives.","Rejects F&F and TheNature positive promotion.","TRG-R13L42-383220-S2-20230906|TRG-R13L42-298540-S2-20240215",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L5_brand_retail_valuation_4B_overlay,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+1,+1,"After consumer-brand rerating, valuation/positioning overlay captured drawdown protection better than price-only exits.","BrandX 4B full-window proximity 0.89 and post-peak drawdown -62.26%.","TRG-R13L42-337930-4B-20241002",4,4,2,low,sector_shadow_only,"overlay only; not a positive-stage promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L42-C19-036620-GAMSUNG-2024-REORDER-MARGIN", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "SNOWPEAK_APPAREL_DOMESTIC_REORDER_GROSS_MARGIN", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R13L42-036620-S2A-20240222", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Apparel brand sell-through/reorder thesis moved early, while stricter confirmed revision/Green evidence came after much of the upside."}
{"row_type": "case", "case_id": "R13L42-C19-337930-BRANDX-2024-ATHLEISURE-REORDER", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션/젝시믹스", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_CHANNEL_REORDER_MARGIN_EXPANSION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R13L42-337930-S2A-20240529", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Brand/channel traction with inventory-light sell-through characteristics; 4B overlay becomes important after valuation/positioning acceleration."}
{"row_type": "case", "case_id": "R13L42-C19-383220-FNF-2023-CHINA-INVENTORY-COUNTER", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CHINA_MLB_CHANNEL_INVENTORY_REORDER_RISK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R13L42-383220-S2-20230906", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Brand/channel narrative looked reusable, but inventory/channel quality and revision durability were not confirmed; subsequent 4C-style downside was large."}
{"row_type": "case", "case_id": "R13L42-C19-298540-NATURE-2024-INVENTORY-COUNTER", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "LIFESTYLE_APPAREL_INVENTORY_MARGIN_OVERHANG", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R13L42-298540-S2-20240215", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample aligned", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Brand retail channel existed, but inventory/margin overhang made rerating attempts fail; 4C thesis-break routing should fire earlier when margin bridge is absent."}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-036620-S2A-20240222", "case_id": "R13L42-C19-036620-GAMSUNG-2024-REORDER-MARGIN", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "SNOWPEAK_APPAREL_DOMESTIC_REORDER_GROSS_MARGIN", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "evidence_available_at_that_date": "Snow Peak apparel reorder/brand sell-through signal; price row confirms next-day tradable entry close.", "evidence_source": "DART/quarterly-result narrative proxy + stock-web OHLC; not a live recommendation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-22", "entry_price": 3025, "MFE_30D_pct": 27.44, "MFE_90D_pct": 55.04, "MFE_180D_pct": 55.04, "MFE_1Y_pct": 121.82, "MFE_2Y_pct": null, "MAE_30D_pct": -6.28, "MAE_90D_pct": -6.28, "MAE_180D_pct": -6.28, "MAE_1Y_pct": -17.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-24", "peak_price": 4690, "drawdown_after_peak_pct": -46.91, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G036620-20240222-3025", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-036620-GREEN-20240523", "case_id": "R13L42-C19-036620-GAMSUNG-2024-REORDER-MARGIN", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "SNOWPEAK_APPAREL_DOMESTIC_REORDER_GROSS_MARGIN", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-23", "evidence_available_at_that_date": "Later confirmed operating momentum/revision confidence after price already repriced.", "evidence_source": "DART/quarterly-result narrative proxy + stock-web OHLC", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-23", "entry_price": 4505, "MFE_30D_pct": 4.11, "MFE_90D_pct": 4.11, "MFE_180D_pct": 4.11, "MFE_1Y_pct": 48.95, "MFE_2Y_pct": null, "MAE_30D_pct": -17.2, "MAE_90D_pct": -35.18, "MAE_180D_pct": -37.85, "MAE_1Y_pct": -44.73, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-24", "peak_price": 4690, "drawdown_after_peak_pct": -46.91, "green_lateness_ratio": 0.889, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "late_green_high_drawdown", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G036620-20240523-4505", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-337930-S2A-20240529", "case_id": "R13L42-C19-337930-BRANDX-2024-ATHLEISURE-REORDER", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션/젝시믹스", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_CHANNEL_REORDER_MARGIN_EXPANSION", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-29", "evidence_available_at_that_date": "Athleisure brand channel traction and reorder narrative began before the full valuation blowoff.", "evidence_source": "DART/quarterly-result narrative proxy + stock-web OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv", "profile_path": "atlas/symbol_profiles/337/337930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-29", "entry_price": 5750, "MFE_30D_pct": 58.96, "MFE_90D_pct": 132.7, "MFE_180D_pct": 132.7, "MFE_1Y_pct": 132.7, "MFE_2Y_pct": null, "MAE_30D_pct": -8.7, "MAE_90D_pct": -8.7, "MAE_180D_pct": -12.17, "MAE_1Y_pct": -12.17, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 13380, "drawdown_after_peak_pct": -62.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_with_4B_overlay", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G337930-20240529-5750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-337930-4B-20241002", "case_id": "R13L42-C19-337930-BRANDX-2024-ATHLEISURE-REORDER", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션/젝시믹스", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_CHANNEL_REORDER_MARGIN_EXPANSION", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2024-10-02", "evidence_available_at_that_date": "After rapid re-rating, local valuation/positioning overheat was visible before the subsequent drawdown.", "evidence_source": "stock-web OHLC + valuation/positioning overlay proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv", "profile_path": "atlas/symbol_profiles/337/337930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-02", "entry_price": 12540, "MFE_30D_pct": 6.7, "MFE_90D_pct": 6.7, "MFE_180D_pct": 6.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.38, "MAE_90D_pct": -59.73, "MAE_180D_pct": -59.73, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 13380, "drawdown_after_peak_pct": -62.26, "green_lateness_ratio": 0.341, "four_b_local_peak_proximity": 0.89, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G337930-20241002-12540", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-383220-S2-20230906", "case_id": "R13L42-C19-383220-FNF-2023-CHINA-INVENTORY-COUNTER", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CHINA_MLB_CHANNEL_INVENTORY_REORDER_RISK", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2", "trigger_date": "2023-09-06", "evidence_available_at_that_date": "Brand/channel recovery narrative without sufficient sell-through and inventory-quality confirmation.", "evidence_source": "DART/quarterly-result narrative proxy + stock-web OHLC", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-06", "entry_price": 112400, "MFE_30D_pct": 6.67, "MFE_90D_pct": 6.67, "MFE_180D_pct": 6.67, "MFE_1Y_pct": 6.67, "MFE_2Y_pct": null, "MAE_30D_pct": -13.61, "MAE_90D_pct": -37.46, "MAE_180D_pct": -45.64, "MAE_1Y_pct": -47.06, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-18", "peak_price": 119900, "drawdown_after_peak_pct": -49.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G383220-20230906-112400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-383220-4C-20231115", "case_id": "R13L42-C19-383220-FNF-2023-CHINA-INVENTORY-COUNTER", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CHINA_MLB_CHANNEL_INVENTORY_REORDER_RISK", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C", "trigger_date": "2023-11-15", "evidence_available_at_that_date": "Margin/channel pressure became explicit enough to route thesis-break rather than wait for price-only confirmation.", "evidence_source": "DART/quarterly-result narrative proxy + stock-web OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-15", "entry_price": 91500, "MFE_30D_pct": 2.08, "MFE_90D_pct": 2.08, "MFE_180D_pct": 2.08, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.44, "MAE_90D_pct": -27.1, "MAE_180D_pct": -37.38, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-16", "peak_price": 93400, "drawdown_after_peak_pct": -34.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G383220-20231115-91500", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-298540-S2-20240215", "case_id": "R13L42-C19-298540-NATURE-2024-INVENTORY-COUNTER", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "LIFESTYLE_APPAREL_INVENTORY_MARGIN_OVERHANG", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2", "trigger_date": "2024-02-15", "evidence_available_at_that_date": "Lifestyle/outdoor apparel brand had channel presence, but inventory/margin bridge was not proven.", "evidence_source": "DART/quarterly-result narrative proxy + stock-web OHLC", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv", "profile_path": "atlas/symbol_profiles/298/298540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-15", "entry_price": 15550, "MFE_30D_pct": 3.79, "MFE_90D_pct": 3.79, "MFE_180D_pct": 3.79, "MFE_1Y_pct": 3.79, "MFE_2Y_pct": null, "MAE_30D_pct": -10.03, "MAE_90D_pct": -21.8, "MAE_180D_pct": -42.77, "MAE_1Y_pct": -50.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 16140, "drawdown_after_peak_pct": -44.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G298540-20240215-15550", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R13L42-298540-4C-20240614", "case_id": "R13L42-C19-298540-NATURE-2024-INVENTORY-COUNTER", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "LIFESTYLE_APPAREL_INVENTORY_MARGIN_OVERHANG", "sector": "소비재·유통·브랜드", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C", "trigger_date": "2024-06-14", "evidence_available_at_that_date": "Inventory/margin break was no longer just a valuation issue; thesis evidence was broken.", "evidence_source": "DART/quarterly-result narrative proxy + stock-web OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv", "profile_path": "atlas/symbol_profiles/298/298540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-14", "entry_price": 13580, "MFE_30D_pct": 0.22, "MFE_90D_pct": 0.22, "MFE_180D_pct": 0.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.46, "MAE_90D_pct": -29.6, "MAE_180D_pct": -36.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-17", "peak_price": 13610, "drawdown_after_peak_pct": -36.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G298540-20240614-13580", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L42-C19-036620-GAMSUNG-2024-REORDER-MARGIN", "trigger_id": "TRG-R13L42-036620-S2A-20240222", "symbol": "036620", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 6, "sell_through_score": 7, "brand_heat_score": 7, "store_expansion_quality_score": 0, "gross_margin_stability_score": 7}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 8, "sell_through_score": 9, "brand_heat_score": 8, "store_expansion_quality_score": 0, "gross_margin_stability_score": 8}, "weighted_score_after": 83.5, "stage_label_after": "Stage2-Actionable/C19-promote", "changed_components": ["inventory_quality_score", "sell_through_score", "gross_margin_stability_score", "execution_risk_score"], "component_delta_explanation": "C19 candidate adds sell-through and inventory-quality bonus; no Green promotion without later revision.", "MFE_90D_pct": 55.04, "MAE_90D_pct": -6.28, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L42-C19-337930-BRANDX-2024-ATHLEISURE-REORDER", "trigger_id": "TRG-R13L42-337930-S2A-20240529", "symbol": "337930", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 7, "sell_through_score": 8, "brand_heat_score": 8, "store_expansion_quality_score": 0, "gross_margin_stability_score": 7}, "weighted_score_before": 79.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 8, "sell_through_score": 9, "brand_heat_score": 8, "store_expansion_quality_score": 0, "gross_margin_stability_score": 8}, "weighted_score_after": 86.0, "stage_label_after": "Stage2-Actionable/C19-promote", "changed_components": ["inventory_quality_score", "sell_through_score", "gross_margin_stability_score", "execution_risk_score"], "component_delta_explanation": "Reorder quality and margin bridge separate the case from simple brand heat; 4B overlay still required after valuation expansion.", "MFE_90D_pct": 132.7, "MAE_90D_pct": -8.7, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L42-C19-383220-FNF-2023-CHINA-INVENTORY-COUNTER", "trigger_id": "TRG-R13L42-383220-S2-20230906", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 7, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 3, "sell_through_score": 3, "brand_heat_score": 7, "store_expansion_quality_score": 0, "gross_margin_stability_score": 4}, "weighted_score_before": 73.5, "stage_label_before": "Stage2/Yellow-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 5, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 2, "sell_through_score": 2, "brand_heat_score": 7, "store_expansion_quality_score": 0, "gross_margin_stability_score": 3}, "weighted_score_after": 61.0, "stage_label_after": "Rejected-positive/4C-watch", "changed_components": ["inventory_quality_score", "sell_through_score", "gross_margin_stability_score", "execution_risk_score"], "component_delta_explanation": "C19 guard penalizes channel narrative without inventory/sell-through proof.", "MFE_90D_pct": 6.67, "MAE_90D_pct": -37.46, "score_return_alignment_label": "false_positive_removed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L42-C19-298540-NATURE-2024-INVENTORY-COUNTER", "trigger_id": "TRG-R13L42-298540-S2-20240215", "symbol": "298540", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 3, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 2, "sell_through_score": 2, "brand_heat_score": 6, "store_expansion_quality_score": 0, "gross_margin_stability_score": 2}, "weighted_score_before": 65.0, "stage_label_before": "Stage2-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_quality_score": 1, "sell_through_score": 1, "brand_heat_score": 6, "store_expansion_quality_score": 0, "gross_margin_stability_score": 1}, "weighted_score_after": 52.0, "stage_label_after": "4C-watch/rejected-positive", "changed_components": ["inventory_quality_score", "sell_through_score", "gross_margin_stability_score", "execution_risk_score"], "component_delta_explanation": "Inventory and margin bridge absence blocks brand retail positive promotion.", "MFE_90D_pct": 3.79, "MAE_90D_pct": -21.8, "score_return_alignment_label": "false_positive_removed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "42", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["late_green_after_brand_rerating", "brand_heat_false_positive", "inventory_margin_4C_late", "valuation_4B_overlay_needed"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_sell_through_inventory_quality_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+2,+2,"Positive cases rerated when reorder/sell-through and gross-margin stability were visible before confirmed Green.","Improves positive alignment: 036620/337930 selected before late Green.","TRG-R13L42-036620-S2A-20240222|TRG-R13L42-337930-S2A-20240529",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C19_inventory_margin_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,-3,-3,"Brand heat/channel presence without inventory-quality and margin bridge produced false positives.","Rejects F&F and TheNature positive promotion.","TRG-R13L42-383220-S2-20230906|TRG-R13L42-298540-S2-20240215",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L5_brand_retail_valuation_4B_overlay,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+1,+1,"After consumer-brand rerating, valuation/positioning overlay captured drawdown protection better than price-only exits.","BrandX 4B full-window proximity 0.89 and post-peak drawdown -62.26%.","TRG-R13L42-337930-4B-20241002",4,4,2,low,sector_shadow_only,"overlay only; not a positive-stage promotion"
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
next_round = R13_loop_43
next_large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
next_canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
reason = C19 now has positive/counterexample balance; L5 coverage should next test global distribution rerating versus inventory/channel risk in beauty/food.
```

## 28. Source Notes

Primary paths accessed or referenced:
- `Songdaiki/stock-web/atlas/manifest.json`
- `Songdaiki/stock-web/atlas/schema.json`
- `Songdaiki/stock-web/atlas/symbol_profiles/036/036620.json`
- `Songdaiki/stock-web/atlas/symbol_profiles/337/337930.json`
- `Songdaiki/stock-web/atlas/symbol_profiles/383/383220.json`
- `Songdaiki/stock-web/atlas/symbol_profiles/298/298540.json`
- `Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv`
- `Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv`
- `Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/337/337930/2025.csv`
- `Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv`
- `Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv`
- `Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv`
- `Songdaiki/stock_agent/reports/e2r_calibration/ingest_summary.md`

All price rows are based on `tradable_raw` stock-web OHLC and are not adjusted-price returns.
