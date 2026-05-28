# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 12
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD
output_file = e2r_stock_web_v12_residual_round_R5_loop_12_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a historical calibration artifact, not live candidate research and not an investment recommendation.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are not re-proposed: Stage2 actionable evidence bonus, Yellow threshold 75, Green threshold 87, Green revision minimum 55, cross-evidence Green buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing.

The applied calibration summary confirms global adjustments across 13 rounds and 107 parsed result documents, so this loop intentionally searches for sector/canonical residual rather than repeating the global proof. fileciteturn182file0turn183file0

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD
loop_objective = counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test
```

The coverage gap is that K-beauty export/ODM cases can look similar at the headline level, but the price paths split sharply depending on whether the company is an ODM with customer/order-quality and realized margin bridge, or a brand owner still exposed to China/duty-free drag.

## 3. Previous Coverage / Duplicate Avoidance Check

A repository search for `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION K_BEAUTY COSMAX Kolmar Amorepacific calibration` returned no matched calibration artifact in the accessible research index. The general ingest summary shows all R1–R13 sectors were covered, but v12’s purpose is residual gap expansion and not a rerun of the same representative rows. fileciteturn182file0

```text
auto_selected_coverage_gap = L5/C20 K-beauty global channel / ODM reorder with brand-owner China drag guard
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
diversity_score_summary = high_total_61_avg_20.3
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest was read directly. It reports `FinanceData/marcap` as source, `raw_unadjusted_marcap` as price adjustment status, `max_date = 2026-02-20`, `tradable_row_count = 14,354,401`, `raw_row_count = 15,214,118`, `symbol_count = 5,414`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`. fileciteturn186file0

The schema confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m`, raw shard columns with `rs`, and MFE/MAE formulas based on max high and min low from entry date through N tradable rows. fileciteturn187file0

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All three representative cases use 2024 entry dates with at least 180 subsequent stock-web tradable rows before the manifest `max_date = 2026-02-20`.

| symbol | profile status | corporate_action_candidate_dates | 180D window status | usable |
|---:|---|---|---|---|
| 192820 | active_like, no corporate-action candidates | [] | clean_180D_window | true |
| 161890 | active_like, no corporate-action candidates | [] | clean_180D_window | true |
| 090430 | active_like, one old 2015 candidate | [2015-05-08] | clean_180D_window for 2024/2025 case | true |

Profile validation: 코스맥스, 한국콜마, and 아모레퍼시픽 profiles were checked for years, row counts, and corporate-action caveats. fileciteturn188file0turn189file0turn190file0

## 6. Canonical Archetype Compression Map

```text
fine_archetype = K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD
maps_to = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

Compression rule:

```text
ODM/customer-quality cases:
    reorder/channel growth + realized margin bridge + revision confirmation = positive C20 evidence

Brand-owner/channel-drag cases:
    broad K-beauty narrative + relative strength without China/duty-free separation = counterexample guard

4B/4C:
    price-only peak remains watch-only; full 4B or 4C needs non-price margin/channel evidence.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | MFE90 | MAE90 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R5L12-C20-COSMAX-20240514 | 192820 | 코스맥스 | high_mae_success | 2024-05-13 | 2024-05-14 | 160,500 | 29.6% | -27.7% | current_profile_too_early |
| R5L12-C20-KOLMAR-20240514 | 161890 | 한국콜마 | structural_success | 2024-05-13 | 2024-05-14 | 53,600 | 45.7% | -3.2% | current_profile_too_late |
| R5L12-C20-AMORE-20240514 | 090430 | 아모레퍼시픽 | failed_rerating | 2024-05-14 | 2024-05-14 | 169,000 | 18.6% | -31.4% | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
```

The positive set deliberately uses ODM/channel margin-bridge cases. The counterexample is a brand-owner narrative case where global K-beauty strength could look attractive but the China/duty-free drag invalidated durable rerating. Reuters later described Korean brands’ US expansion and noted that many outsource to contract manufacturers such as Cosmax and Kolmar; this supports the distinction between brand-channel demand and ODM production leverage, but is used as sector context rather than a trigger-date promotion source. citeturn463700news0

## 9. Evidence Source Map

| case | trigger evidence | source discipline |
|---|---|---|
| 코스맥스 | Q1 2024 earnings/revision event and ODM global channel recovery | public event / DART-company earnings event; not price-only |
| 한국콜마 | Q1 2024 earnings/revision event and ODM demand-margin bridge | public event / DART-company earnings event; not price-only |
| 아모레퍼시픽 | broad K-beauty narrative failed after Q2 miss and China weakness | FT 2024-08-08 reports Amorepacific’s Q2 miss, share collapse, and China/premium-brand pressure. citeturn456809news2 |

## 10. Price Data Source Map

| symbol | price shard | profile | validation notes |
|---:|---|---|---|
| 192820 | atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv / 2025.csv | atlas/symbol_profiles/192/192820.json | entry/peak/drawdown rows: fileciteturn191file0turn192file0 |
| 161890 | atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv / 2025.csv | atlas/symbol_profiles/161/161890.json | entry/peak/drawdown rows: fileciteturn193file0turn194file0 |
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv / 2025.csv | atlas/symbol_profiles/090/090430.json | entry/peak/Q2-break rows: fileciteturn195file0turn196file0 |

## 11. Case-by-Case Trigger Grid

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current profile verdict |
|---|---|---|---|---|---|
| 코스맥스 | public event, customer/order quality, early revision | revision + margin bridge but high MAE | price-only local watch | none | current_profile_too_early |
| 한국콜마 | public event, customer/order quality, early revision | revision + margin bridge + low red-team risk | positioning/revision watch near peak | none | current_profile_too_late |
| 아모레퍼시픽 | narrative + relative strength | unsupported for Green | price-only/valuation peak | Q2 miss, channel thesis break | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R5L12-C20-COSMAX-S2A-20240513 | 160,500 | 29.6% | 29.6% | 29.6% | -3.9% | -27.7% | -27.7% | 2024-06-14 | 208,000 | -44.2% |
| R5L12-C20-KOLMAR-S2A-20240513 | 53,600 | 39.9% | 45.7% | 46.8% | -3.2% | -3.2% | -3.2% | 2024-09-30 | 78,700 | -34.1% |
| R5L12-C20-AMORE-S2-NARR-20240514 | 169,000 | 18.6% | 18.6% | 18.6% | -1.0% | -31.4% | -39.9% | 2024-05-31 | 200,500 | -50.3% |


### OHLC anchor notes

- 코스맥스 entry row `2024-05-14 c=160,500`, peak row `2024-06-14 h=208,000`, and later drawdown lows were read from the stock-web tradable shard. fileciteturn191file0turn192file0
- 한국콜마 entry row `2024-05-14 c=53,600`, peak row `2024-09-30 h=78,700`, and subsequent drawdown rows were read from stock-web tradable shards. fileciteturn193file0turn194file0
- 아모레퍼시픽 entry row `2024-05-14 c=169,000`, May peak row `2024-05-31 h=200,500`, 2024-08-07 break row `c=124,500`, and 2025 continuation lows were read from stock-web tradable shards. fileciteturn195file0turn196file0

## 13. Current Calibrated Profile Stress Test

| case | current calibrated proxy verdict | actual alignment | stress result |
|---|---|---|---|
| 코스맥스 | Stage3-Yellow too early if one-quarter beat overweights revision | +29.6% MFE but -27.7% MAE | keep Yellow; require durable margin/channel split before Green |
| 한국콜마 | Stage3-Green too late if revision proof waits for September | +45.7% MFE90 / shallow early MAE | allow C20 ODM margin bridge to cross Green with confirmation |
| 아모레퍼시픽 | false-positive risk if global K-beauty narrative ignores China/duty-free drag | +18.6% early MFE but -39.9% 180D MAE | add brand-owner China/duty-free drag guard |


Answering the required stress questions:

```text
1. Current profile judgment:
   - ODMs: likely Stage2/Yellow early, with Green only after revision proof.
   - Brand owner: may over-score if broad K-beauty narrative and relative strength are not channel-split.

2. MFE/MAE alignment:
   - 한국콜마 aligns strongly.
   - 코스맥스 succeeds but with high MAE; Green should remain guarded.
   - 아모레퍼시픽 is a residual false positive unless China/duty-free drag is penalized.

3. Stage2 bonus:
   - Useful for ODMs; too generous for brand-owner narrative without channel split.

4. Yellow 75:
   - Adequate; should remain a watch state for C20 brand owners.

5. Green 87 / revision 55:
   - Correct globally; C20 needs realized margin bridge and channel split as an additional condition.

6. Price-only blowoff guard:
   - Strengthened. May peaks alone did not identify durable 4B.

7. Full 4B non-price requirement:
   - Strengthened for C20; price-only local/full peaks become watch overlays only.

8. Hard 4C routing:
   - Appropriate; 아모레퍼시픽 post-Q2 miss is a thesis-break/protection case, not positive calibration.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable entry | Green proxy date | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| 코스맥스 | 2024-05-14 at 160,500 | 2024-06-13/14 around 184,100~184,900 | 0.50 | Green is moderately late; high MAE says do not relax globally |
| 한국콜마 | 2024-05-14 at 53,600 | 2024-09-10/30 around 76,200~78,700 | 0.90 | Green captures too much of upside after revision confirmation; C20 ODM exception candidate |
| 아모레퍼시픽 | 2024-05-14 at 169,000 | no confirmed Green | not_applicable | broad K-beauty narrative lacked channel-drag separation |

## 15. 4B Local vs Full-window Timing Audit

| case | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| 코스맥스 | 2024-06-14 price peak watch | 0.51 | 0.51 | price_only, positioning_overheat | watch only; not full 4B |
| 한국콜마 | 2024-09-10/30 peak/revision watch | 0.90 | 0.90 | price_only, positioning_overheat, revision_slowdown | good 4B watch, but full 4B requires non-price |
| 아모레퍼시픽 | 2024-05-31 price peak | 1.00 | 1.00 | price_only, valuation_blowoff | price-only peak was insufficient; 4C arrived after Q2 evidence |

## 16. 4C Protection Audit

아모레퍼시픽 is the 4C stress case. The 2024-08-07 break row occurred after the earlier May price peak and after broad global K-beauty narrative had already failed to protect the stock. The post-peak drawdown was about `-50.3%`, while the 4C row’s following 90D MAE was about `-16.3%`, giving a rough protection label:

```text
four_c_protection_label = hard_4c_success
four_c_protection_score_proxy = 1 - 16.3 / 50.3 = 0.68
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c20_china_dutyfree_drag_guard
candidate_delta = +1 guard
```

Rule:

```text
For L5 consumer/brand-distribution cases, broad K-beauty/global-channel narrative cannot promote to Stage3-Green unless China/duty-free drag is explicitly separated or proven immaterial.
```

Reason:

```text
아모레퍼시픽 shows that the same K-beauty headline can hide opposite channel economics.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c20_green_requires_realized_channel_margin_bridge
candidate_delta = +1 guard
```

Rule:

```text
For C20, Green requires at least two of:
1. realized margin bridge,
2. confirmed revision,
3. channel reorder evidence outside a single geography,
4. low channel-drag red-team risk.

Relative strength plus K-beauty narrative is capped at Stage2/Yellow.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 3 | 31.3% | -20.8% | 31.7% | -23.6% | 33.3% | works for ODMs but leaks Amore-style brand-owner drag |
| P0b e2r_2_0_baseline_reference | rollback reference | 3 | 31.3% | -20.8% | 31.7% | -23.6% | 33.3% | less strict Green; not preferred |
| P1 sector_specific_candidate_profile | L5 | 3 | 37.7% | -15.5% | 38.2% | -15.5% | 0.0% | blocks brand-owner channel-drag false positive |
| P2 canonical_archetype_candidate_profile | C20 | 3 | 37.7% | -15.5% | 38.2% | -15.5% | 0.0% | rewards ODM margin bridge but caps weak channel split |
| P3 counterexample_guard_profile | C20 guard | 3 | 37.7% | -15.5% | 38.2% | -15.5% | 0.0% | most conservative; no global delta |


## 20. Score-Return Alignment Matrix

| case | before score / label | after score / label | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| 코스맥스 | 82 / Stage3-Yellow | 78 / Stage3-Yellow_guarded | 29.6% | -27.7% | success but high-MAE; guard improves risk labeling |
| 한국콜마 | 86 / Stage3-Yellow | 88 / Stage3-Green_C20_confirmed | 45.7% | -3.2% | best score-return alignment |
| 아모레퍼시픽 | 78 / Stage3-Yellow_false_positive_risk | 66 / Stage2_watch_or_4C_blocked | 18.6% | -31.4% | guard removes false-positive promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD | 2 | 1 | 2 | 1 | 3 | 0 | 5 | 3 | 1 | true | true | still needs food/export-channel and platform-commerce holdouts |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - brand_owner_china_drag_false_positive
  - ODM_high_MAE_success
  - late_green_after_revision_confirmation
new_axis_proposed:
  - c20_green_requires_realized_channel_margin_bridge
  - c20_china_dutyfree_drag_guard
  - c20_price_only_4b_watch_not_exit
existing_axis_strengthened:
  - stage3_green_revision_min in C20 only
  - full_4b_requires_non_price_evidence in C20 only
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high_total_61_avg_20.3
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L5/C20 K-beauty global channel / ODM reorder with brand-owner China drag guard
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest and schema
- symbol profiles for 192820, 161890, 090430
- 2024/2025 tradable OHLC rows around representative entries, peaks, and 180D windows
- MFE/MAE based on raw unadjusted tradable OHLC
- positive/counterexample balance
- same-entry-group dedupe
- 4B local vs full-window split
- 4C protection label for the Amorepacific thesis-break case
```

Not validated:

```text
- production scoring code
- live candidates
- brokerage data
- adjusted-price reconciliation
- exact DART rcpNo URL mapping for each earnings disclosure
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_green_requires_realized_channel_margin_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Block Green if K-beauty/global-channel narrative lacks realized margin bridge and channel split.","Reduced Amore-style false positive; kept Kolmar success.",R5L12-C20-KOLMAR-S2A-20240513|R5L12-C20-AMORE-S2-NARR-20240514,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_dutyfree_drag_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Consumer brand rerating must separate US/Japan/Amazon growth from China/duty-free drag.","Lower false-positive yellow/green in brand owners; ODMs with customer-quality still pass.",R5L12-C20-AMORE-S2-NARR-20240514,3,3,1,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_price_only_4b_watch_not_exit,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Price-only local/full peaks are watch overlays until revision slowdown or channel evidence appears.","Preserves existing full_4b_requires_non_price_evidence and makes C20-specific overlay explicit.",R5L12-C20-AMORE-4B-PRICE-20240531|R5L12-C20-KOLMAR-S2A-20240513,5,3,1,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L12-C20-COSMAX-20240514","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L12-C20-COSMAX-S2A-20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early_positive_but_high_MAE_success","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"2024-05-13/14 Q1 earnings/revision event: ODM global channel recovery and non-China order quality were visible, but subsequent drawdown shows C20 needs channel/revision durability, not a one-quarter beat alone."}
{"row_type":"case","case_id":"R5L12-C20-KOLMAR-20240514","symbol":"161890","company_name":"한국콜마","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L12-C20-KOLMAR-S2A-20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_with_late_green","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2024-05-13/14 Q1 earnings/revision event: ODM demand and margin recovery appeared in earnings before the later September peak. Green confirmation arrived late versus the May actionable trigger."}
{"row_type":"case","case_id":"R5L12-C20-AMORE-20240514","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L12-C20-AMORE-S2-NARR-20240514","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_green_if_channel_drag_ignored","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The global K-beauty narrative and May price strength did not isolate China/duty-free drag. The later 2024-08-07 Q2 miss and China weakness routed this to thesis-break/4C rather than positive promotion."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R5L12-C20-COSMAX-S2A-20240513","case_id":"R5L12-C20-COSMAX-20240514","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / ODM reorder","loop_objective":["counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","coverage_gap_fill","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","entry_date":"2024-05-14","entry_price":160500,"evidence_available_at_that_date":"2024-05-13/14 Q1 earnings/revision event: ODM global channel recovery and non-China order quality were visible, but subsequent drawdown shows C20 needs channel/revision durability, not a one-quarter beat alone.","evidence_source":"DART/company Q1 2024 earnings event; sector context cross-checked with Reuters K-beauty exporter/ODM discussion.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.6,"MFE_90D_pct":29.6,"MFE_180D_pct":29.6,"MFE_1Y_pct":29.6,"MFE_2Y_pct":null,"MAE_30D_pct":-3.9,"MAE_90D_pct":-27.7,"MAE_180D_pct":-27.7,"MAE_1Y_pct":-27.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":208000,"drawdown_after_peak_pct":-44.2,"green_lateness_ratio":0.5,"four_b_local_peak_proximity":0.51,"four_b_full_window_peak_proximity":0.51,"four_b_timing_verdict":"price_only_local_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"early_positive_but_high_MAE_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12-C20-COSMAX-20240514::2024-05-14::160500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L12-C20-KOLMAR-S2A-20240513","case_id":"R5L12-C20-KOLMAR-20240514","symbol":"161890","company_name":"한국콜마","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / ODM reorder","loop_objective":["counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","coverage_gap_fill","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","entry_date":"2024-05-14","entry_price":53600,"evidence_available_at_that_date":"2024-05-13/14 Q1 earnings/revision event: ODM demand and margin recovery appeared in earnings before the later September peak. Green confirmation arrived late versus the May actionable trigger.","evidence_source":"DART/company Q1 2024 earnings event; sector context cross-checked with Reuters K-beauty exporter/ODM discussion.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["positioning_overheat","revision_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv","profile_path":"atlas/symbol_profiles/161/161890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.9,"MFE_90D_pct":45.7,"MFE_180D_pct":46.8,"MFE_1Y_pct":46.8,"MFE_2Y_pct":null,"MAE_30D_pct":-3.2,"MAE_90D_pct":-3.2,"MAE_180D_pct":-3.2,"MAE_1Y_pct":-3.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":78700,"drawdown_after_peak_pct":-34.1,"green_lateness_ratio":0.9,"four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"late_but_good_full_window_4B_watch","four_b_evidence_type":["price_only","positioning_overheat","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_with_late_green","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12-C20-KOLMAR-20240514::2024-05-14::53600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L12-C20-AMORE-S2-NARR-20240514","case_id":"R5L12-C20-AMORE-20240514","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / ODM reorder","loop_objective":["counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","coverage_gap_fill","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Narrative","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":169000,"evidence_available_at_that_date":"The global K-beauty narrative and May price strength did not isolate China/duty-free drag. The later 2024-08-07 Q2 miss and China weakness routed this to thesis-break/4C rather than positive promotion.","evidence_source":"FT 2024-08-08 noted Amorepacific's Q2 miss, one-day share collapse, and China/premium-brand weakness; Reuters/FT sector context confirms broad China weakness in beauty.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken","margin_or_backlog_slowdown"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.6,"MFE_90D_pct":18.6,"MFE_180D_pct":18.6,"MFE_1Y_pct":18.6,"MFE_2Y_pct":null,"MAE_30D_pct":-1.0,"MAE_90D_pct":-31.4,"MAE_180D_pct":-39.9,"MAE_1Y_pct":-41.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500,"drawdown_after_peak_pct":-50.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_enough_then_4C","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_green_if_channel_drag_ignored","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12-C20-AMORE-20240514::2024-05-14::169000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L12-C20-AMORE-4B-PRICE-20240531","case_id":"R5L12-C20-AMORE-20240514","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / ODM reorder","loop_objective":["4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"trigger_type":"Stage4B-Watch","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":194200,"evidence_available_at_that_date":"Overlay trigger for timing audit; not used as positive promotion.","evidence_source":"Stock-web OHLC + FT/sector evidence for Amorepacific Q2 miss and China drag.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.7,"MAE_90D_pct":-40.3,"MAE_180D_pct":-48.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500,"drawdown_after_peak_pct":-50.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_peak_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12-C20-AMORE-20240514::2024-05-31::194200","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"overlay_trigger_not_representative","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L12-C20-AMORE-4C-20240807","case_id":"R5L12-C20-AMORE-20240514","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_ODM_REORDER_WITH_CHINA_DRAG_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / ODM reorder","loop_objective":["4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"trigger_type":"Stage4C","trigger_date":"2024-08-07","entry_date":"2024-08-07","entry_price":124500,"evidence_available_at_that_date":"Overlay trigger for timing audit; not used as positive promotion.","evidence_source":"Stock-web OHLC + FT/sector evidence for Amorepacific Q2 miss and China drag.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.4,"MFE_90D_pct":26.9,"MFE_180D_pct":26.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.9,"MAE_90D_pct":-16.3,"MAE_180D_pct":-19.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-27","peak_price":158000,"drawdown_after_peak_pct":-36.9,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_4C","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_overlay_only","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12-C20-AMORE-20240514::2024-08-07::124500","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"overlay_trigger_not_representative","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L12-C20-COSMAX-20240514","trigger_id":"R5L12-C20-COSMAX-S2A-20240513","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow guard subtracts for high MAE/positioning risk unless realized margin bridge persists beyond one quarter.","MFE_90D_pct":29.6,"MAE_90D_pct":-27.7,"score_return_alignment_label":"early_positive_but_high_MAE_success","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_0_baseline_reference","case_id":"R5L12-C20-COSMAX-20240514","trigger_id":"R5L12-C20-COSMAX-S2A-20240513","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow guard subtracts for high MAE/positioning risk unless realized margin bridge persists beyond one quarter.","MFE_90D_pct":29.6,"MAE_90D_pct":-27.7,"score_return_alignment_label":"early_positive_but_high_MAE_success","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"sector_specific_candidate_profile","case_id":"R5L12-C20-COSMAX-20240514","trigger_id":"R5L12-C20-COSMAX-S2A-20240513","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":12,"revision_score":16,"relative_strength_score":12,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_guarded","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow guard subtracts for high MAE/positioning risk unless realized margin bridge persists beyond one quarter.","MFE_90D_pct":29.6,"MAE_90D_pct":-27.7,"score_return_alignment_label":"early_positive_but_high_MAE_success","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R5L12-C20-COSMAX-20240514","trigger_id":"R5L12-C20-COSMAX-S2A-20240513","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":12,"revision_score":16,"relative_strength_score":12,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_guarded","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow guard subtracts for high MAE/positioning risk unless realized margin bridge persists beyond one quarter.","MFE_90D_pct":29.6,"MAE_90D_pct":-27.7,"score_return_alignment_label":"early_positive_but_high_MAE_success","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R5L12-C20-COSMAX-20240514","trigger_id":"R5L12-C20-COSMAX-S2A-20240513","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":12,"revision_score":16,"relative_strength_score":12,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_guarded","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow guard subtracts for high MAE/positioning risk unless realized margin bridge persists beyond one quarter.","MFE_90D_pct":29.6,"MAE_90D_pct":-27.7,"score_return_alignment_label":"early_positive_but_high_MAE_success","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L12-C20-KOLMAR-20240514","trigger_id":"R5L12-C20-KOLMAR-S2A-20240513","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow rule rewards realized ODM margin bridge plus multi-channel reorder, not only broad K-beauty narrative.","MFE_90D_pct":45.7,"MAE_90D_pct":-3.2,"score_return_alignment_label":"structural_success_with_late_green","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_0_baseline_reference","case_id":"R5L12-C20-KOLMAR-20240514","trigger_id":"R5L12-C20-KOLMAR-S2A-20240513","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow rule rewards realized ODM margin bridge plus multi-channel reorder, not only broad K-beauty narrative.","MFE_90D_pct":45.7,"MAE_90D_pct":-3.2,"score_return_alignment_label":"structural_success_with_late_green","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"sector_specific_candidate_profile","case_id":"R5L12-C20-KOLMAR-20240514","trigger_id":"R5L12-C20-KOLMAR-S2A-20240513","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":20,"revision_score":22,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":17},"weighted_score_after":88,"stage_label_after":"Stage3-Green_C20_confirmed","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow rule rewards realized ODM margin bridge plus multi-channel reorder, not only broad K-beauty narrative.","MFE_90D_pct":45.7,"MAE_90D_pct":-3.2,"score_return_alignment_label":"structural_success_with_late_green","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R5L12-C20-KOLMAR-20240514","trigger_id":"R5L12-C20-KOLMAR-S2A-20240513","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":20,"revision_score":22,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":17},"weighted_score_after":88,"stage_label_after":"Stage3-Green_C20_confirmed","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow rule rewards realized ODM margin bridge plus multi-channel reorder, not only broad K-beauty narrative.","MFE_90D_pct":45.7,"MAE_90D_pct":-3.2,"score_return_alignment_label":"structural_success_with_late_green","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R5L12-C20-KOLMAR-20240514","trigger_id":"R5L12-C20-KOLMAR-S2A-20240513","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":20,"revision_score":22,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":17},"weighted_score_after":88,"stage_label_after":"Stage3-Green_C20_confirmed","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 shadow rule rewards realized ODM margin bridge plus multi-channel reorder, not only broad K-beauty narrative.","MFE_90D_pct":45.7,"MAE_90D_pct":-3.2,"score_return_alignment_label":"structural_success_with_late_green","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L12-C20-AMORE-20240514","trigger_id":"R5L12-C20-AMORE-S2-NARR-20240514","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_false_positive_risk","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"New C20 counterexample guard blocks K-beauty narrative promotion unless China/duty-free drag is separated and confirmed margin bridge remains positive.","MFE_90D_pct":18.6,"MAE_90D_pct":-31.4,"score_return_alignment_label":"false_positive_green_if_channel_drag_ignored","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_0_baseline_reference","case_id":"R5L12-C20-AMORE-20240514","trigger_id":"R5L12-C20-AMORE-S2-NARR-20240514","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_false_positive_risk","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"New C20 counterexample guard blocks K-beauty narrative promotion unless China/duty-free drag is separated and confirmed margin bridge remains positive.","MFE_90D_pct":18.6,"MAE_90D_pct":-31.4,"score_return_alignment_label":"false_positive_green_if_channel_drag_ignored","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"sector_specific_candidate_profile","case_id":"R5L12-C20-AMORE-20240514","trigger_id":"R5L12-C20-AMORE-S2-NARR-20240514","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7,"china_or_dutyfree_drag_penalty":-12},"weighted_score_after":66,"stage_label_after":"Stage2_watch_or_4C_blocked","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"New C20 counterexample guard blocks K-beauty narrative promotion unless China/duty-free drag is separated and confirmed margin bridge remains positive.","MFE_90D_pct":18.6,"MAE_90D_pct":-31.4,"score_return_alignment_label":"false_positive_green_if_channel_drag_ignored","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R5L12-C20-AMORE-20240514","trigger_id":"R5L12-C20-AMORE-S2-NARR-20240514","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7,"china_or_dutyfree_drag_penalty":-12},"weighted_score_after":66,"stage_label_after":"Stage2_watch_or_4C_blocked","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"New C20 counterexample guard blocks K-beauty narrative promotion unless China/duty-free drag is separated and confirmed margin bridge remains positive.","MFE_90D_pct":18.6,"MAE_90D_pct":-31.4,"score_return_alignment_label":"false_positive_green_if_channel_drag_ignored","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R5L12-C20-AMORE-20240514","trigger_id":"R5L12-C20-AMORE-S2-NARR-20240514","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7,"china_or_dutyfree_drag_penalty":-12},"weighted_score_after":66,"stage_label_after":"Stage2_watch_or_4C_blocked","changed_components":["margin_bridge_score","revision_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"New C20 counterexample guard blocks K-beauty narrative promotion unless China/duty-free drag is separated and confirmed margin bridge remains positive.","MFE_90D_pct":18.6,"MAE_90D_pct":-31.4,"score_return_alignment_label":"false_positive_green_if_channel_drag_ignored","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_green_requires_realized_channel_margin_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Block Green if K-beauty/global-channel narrative lacks realized margin bridge and channel split.","Reduced Amore-style false positive; kept Kolmar success.",R5L12-C20-KOLMAR-S2A-20240513|R5L12-C20-AMORE-S2-NARR-20240514,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_dutyfree_drag_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Consumer brand rerating must separate US/Japan/Amazon growth from China/duty-free drag.","Lower false-positive yellow/green in brand owners; ODMs with customer-quality still pass.",R5L12-C20-AMORE-S2-NARR-20240514,3,3,1,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_price_only_4b_watch_not_exit,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Price-only local/full peaks are watch overlays until revision slowdown or channel evidence appears.","Preserves existing full_4b_requires_non_price_evidence and makes C20-specific overlay explicit.",R5L12-C20-AMORE-4B-PRICE-20240531|R5L12-C20-KOLMAR-S2A-20240513,5,3,1,low,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["brand_owner_china_drag_false_positive","ODM_high_MAE_success","late_green_after_revision_confirmation"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R5L12-C20-NONE","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"no narrative-only case retained; all selected cases have usable 180D stock-web windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied `e2r_2_1_stock_web_calibrated` profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple `large_sector_id` values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
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
next_round = R5_loop13_or_L5_C18_holdout
recommended_next_scope = C18_CONSUMER_EXPORT_CHANNEL_REORDER or C19_BRAND_RETAIL_INVENTORY_MARGIN
avoid_repeating = 192820/161890/090430 same 2024-05-14 trigger family
priority = add food/export-channel and retail-inventory counterexamples
```

## 28. Source Notes

- Stock-web manifest and schema were used as the price source authority. fileciteturn186file0turn187file0
- Stock-agent calibration artifacts were used only for duplicate avoidance and already-applied global axis awareness. fileciteturn182file0turn183file0
- Sector context: Reuters described 2024/2025 K-beauty export expansion, US e-commerce strength, and Cosmax/Kolmar as contract manufacturers in the beauty supply chain. citeturn463700news0
- Counterexample context: FT described Amorepacific’s 2024 Q2 miss and China/premium-brand weakness as part of a broader Asian beauty pressure pattern. citeturn456809news2
- The quantitative backtest does not rely on live quotes; it uses stock-web raw unadjusted tradable OHLC only.
