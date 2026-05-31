# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "output_file": "e2r_stock_web_v12_residual_round_R5_loop_12_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md",
  "scheduled_round": "R5",
  "scheduled_loop": 12,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 12,
  "computed_next_round": "R6",
  "computed_next_loop": 12,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE",
  "loop_objective": [
    "coverage_gap_fill",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "stage2_actionable_bonus_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 3,
  "diversity_score_summary": "estimated +50; wrong_round_penalty=0; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0; schema_rematerialization_penalty=0; R5 loop 10/11 were C20, so C18 fills a scheduled-round gap",
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": [
    "C18_verified_reorder_sell_through_bonus",
    "C18_unverified_restock_inventory_guard",
    "C18_post_reorder_peak_4B_overlay"
  ],
  "existing_axis_strengthened": [
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "existing_axis_weakened": null
}
```

This loop adds **3** new independent cases, **1** counterexamples, and **3** residual errors for **R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER**.

No current/live candidate scan was performed. No stock_agent production scoring was changed. This is a standalone historical residual calibration file.

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

This loop does not repeat the global calibration proof. It tests whether R5 consumer/export cases need a narrower channel-reorder and sell-through rule that is not captured by generic consumer beta or C20 beauty/food global distribution logic.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 12
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE
round_schedule_status = valid
round_sector_consistency = pass
```

R5 allows L5 consumer/brand/distribution research. C18 was selected because local loop 10 and loop 11 R5 artifacts were both C20 beauty/food global distribution, leaving apparel/footwear OEM reorder and inventory-cycle evidence under-covered.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result files show:

```text
R5 loop 10 -> C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
R5 loop 11 -> C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
R4 loop 12 -> completed and next_round = R5 / next_loop = 12
```

Therefore this file uses R5 loop 12 and C18 rather than repeating C20 symbols such as 삼양식품, 실리콘투, 코스맥스, or 아모레퍼시픽. The selected symbols are new to the local R5 loop 10/11 C20 sample set.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Price basis is `tradable_raw`. Rows are raw/unadjusted FinanceData/marcap OHLC; corporate-action-contaminated windows are blocked.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | corporate-action candidates | selected window status | forward 180D |
| --- | --- | --- | --- | --- | --- |
| 105630 | 한세실업 | atlas/symbol_profiles/105/105630.json | 2011-11-30 | clean for 2021 selected windows | usable |
| 111770 | 영원무역 | atlas/symbol_profiles/111/111770.json | none | clean for 2023 selected windows | usable |
| 241590 | 화승엔터프라이즈 | atlas/symbol_profiles/241/241590.json | 2018-06-08, 2018-07-02 | clean for 2022 selected windows | usable |

All representative triggers have entry dates in the tradable shard, minimum 180 trading days of forward stock-web rows, high/low/close/volume fields, and clean 180D windows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
| --- | --- | --- |
| APPAREL_OEM_US_REORDER_OPERATING_LEVERAGE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | OEM reorder and export mix are treated as channel-reorder evidence, not contract backlog. |
| PREMIUM_OUTDOOR_OEM_REORDER_MARGIN_QUALITY | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Customer quality plus sell-through/reorder durability compresses into C18. |
| FOOTWEAR_RESTOCK_WITHOUT_SELL_THROUGH | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Restocking narrative without retailer inventory normalization becomes C18 counterexample guard. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
| --- | --- | --- | --- | --- |
| R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208 | 105630 | 한세실업 | structural_success | Apparel OEM reorder/reopening visibility became investable before full reported revision confirmation; the later May 2021 peak shows why C18 also needs 4B inventory/positioning overlay. |
| R5L12_C18_111770_YOUNGONE_PREMIUM_OUTDOOR_REORDER_20230515 | 111770 | 영원무역 | missed_structural | Premium outdoor/apparel OEM reorder plus margin quality acted as a clearer C18 signal than generic consumer beta; current profile would tend to wait for later confirmation. |
| R5L12_C18_241590_HWASEUNG_FOOTWEAR_RESTOCK_FALSE_POSITIVE_20220516 | 241590 | 화승엔터프라이즈 | failed_rerating | Global footwear customer/restocking narrative had price reaction but lacked confirmed sell-through and retailer inventory normalization; the forward path shows large MAE and weak MFE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
calibration_usable_case_count = 3
new_independent_case_ratio = 1.00
```

The construction satisfies the minimum positive/counterexample gate and adds a 4B overlay row without counting that overlay as a new aggregate entry.

## 9. Evidence Source Map

| symbol | evidence family | source status | use |
| --- | --- | --- | --- |
| 105630 | U.S. apparel/OEM channel reorder, operating leverage, relative strength | historical public evidence family; exact URL deferred | positive + 4B overlay timing |
| 111770 | premium outdoor/apparel OEM reorder, customer quality, margin bridge | historical public evidence family; exact URL deferred | missed structural / Green-too-late stress test |
| 241590 | footwear customer restock narrative without sell-through and inventory normalization | historical public evidence family; exact URL deferred | counterexample / false-positive guard |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
| --- | --- | --- | --- | --- |
| 105630 | atlas/ohlcv_tradable_by_symbol_year/105/105630/2021.csv | atlas/symbol_profiles/105/105630.json | 2021-02-08 | usable |
| 105630 | atlas/ohlcv_tradable_by_symbol_year/105/105630/2021.csv | atlas/symbol_profiles/105/105630.json | 2021-05-28 | usable |
| 111770 | atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv | atlas/symbol_profiles/111/111770.json | 2023-05-15 | usable |
| 241590 | atlas/ohlcv_tradable_by_symbol_year/241/241590/2022.csv | atlas/symbol_profiles/241/241590.json | 2022-05-16 | usable |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | Stage2 evidence | Stage3 evidence | 4B/4C evidence | current verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R5L12_T01_HANSAE_20210208_STAGE2_ACTIONABLE_REORDER | R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208 | 105630 | Stage2-Actionable | 2021-02-08 | 2021-02-08 | 17450 | public_event_or_disclosure,customer_or_order_quality,relative_strength,early_revision_signal | margin_bridge,financial_visibility,multiple_public_sources |  | current_profile_correct |
| R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT | R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208 | 105630 | 4B-overlay | 2021-05-28 | 2021-05-28 | 26550 |  | confirmed_revision,margin_bridge,financial_visibility | valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown | current_profile_4B_too_late |
| R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER | R5L12_C18_111770_YOUNGONE_PREMIUM_OUTDOOR_REORDER_20230515 | 111770 | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 47500 | public_event_or_disclosure,customer_or_order_quality,relative_strength,early_revision_signal | margin_bridge,financial_visibility,durable_customer_confirmation |  | current_profile_too_late |
| R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | R5L12_C18_241590_HWASEUNG_FOOTWEAR_RESTOCK_FALSE_POSITIVE_20220516 | 241590 | Stage2-Actionable | 2022-05-16 | 2022-05-16 | 15350 | public_event_or_disclosure,customer_or_order_quality,relative_strength |  | margin_or_backlog_slowdown,positioning_overheat,call_off_or_order_cut,thesis_evidence_broken | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R5L12_T01_HANSAE_20210208_STAGE2_ACTIONABLE_REORDER | 105630 | 2021-02-08 | 17450 | 33.52 | -7.45 | 56.45 | -7.45 | 56.45 | -7.45 | 2021-05-28 | 27300 | structural_success |
| R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT | 105630 | 2021-05-28 | 26550 | 2.82 | -14.69 | 2.82 | -28.81 | 2.82 | -28.81 | 2021-05-28 | 27300 | 4B_overlay_success |
| R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER | 111770 | 2023-05-15 | 47500 | 31.58 | -6.53 | 42.95 | -6.53 | 42.95 | -14.95 | 2023-08-16 | 67900 | missed_structural |
| R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | 241590 | 2022-05-16 | 15350 | 12.05 | -20.85 | 12.05 | -31.27 | 12.05 | -43.32 | 2022-05-17 | 17200 | failed_rerating |

### Stock-Web row snippets used for anchor validation

```text
105630 2021-02-08: o=16250 h=17800 l=16150 c=17450 v=970347
105630 2021-05-28: o=26050 h=27300 l=26000 c=26550 v=710518
111770 2023-05-15: o=44600 h=47700 l=44600 c=47500 v=223149
111770 2023-08-16: o=66600 h=67900 l=59800 c=61400 v=232296
241590 2022-05-16: o=14800 h=15500 l=14650 c=15350 v=221396
241590 2022-05-17: o=15100 h=17200 l=15100 c=16650 v=559323
241590 2022-10-26: o=9690 h=9700 l=8830 c=8930 v=666638
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual alignment | current_profile_verdict | explanation |
| --- | --- | --- | --- | --- |
| R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208 | Stage3-Yellow/Green after confirmation | early Stage2 entry produced high MFE | current_profile_correct | Global Stage2 bonus works, but 4B overlay is needed once reorder evidence is fully priced. |
| R5L12_C18_111770_YOUNGONE_PREMIUM_OUTDOOR_REORDER_20230515 | Stage2-Actionable high but not Green | large 90D MFE arrived before classic revision stack | current_profile_too_late | C18 verified reorder/customer-quality evidence should count more than generic consumer beta. |
| R5L12_C18_241590_HWASEUNG_FOOTWEAR_RESTOCK_FALSE_POSITIVE_20220516 | Stage2/Yellow possible on restocking narrative | low MFE and large MAE | current_profile_false_positive | Restock narrative without sell-through/inventory normalization should be blocked. |

Existing applied axes are kept, but narrowed for C18. Stage2 bonus is useful only when channel reorder and sell-through are both supported. Price-only blowoff remains blocked; 4B requires non-price evidence such as inventory exhaustion, margin slowdown, or positioning overheat.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green/proxy entry | peak after Stage2 | green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- | --- |
| Hansae | 2021-02-08 @17450 | 2021-05-28 @26550 | 27300 | 0.924 | Green/confirmation near peak; use 4B overlay. |
| Youngone | 2023-05-15 @47500 | not confirmed in this MD | 67900 | not_applicable | C18 candidate rule would promote earlier. |
| Hwaseung | 2022-05-16 @15350 | blocked | 17200 | not_applicable | False positive; block without sell-through/inventory evidence. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | entry | Stage2 base | local peak | full-window peak | local proximity | full proximity | evidence type | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT | 26550 | 17450 | 27300 | 27300 | 0.924 | 0.924 | valuation_blowoff|positioning_overheat|margin_or_backlog_slowdown | good_full_window_4B_timing |
| R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | 15350 | 15350 | 17200 | 17200 | not_applicable | not_applicable | margin_or_backlog_slowdown|thesis_evidence_broken | positive-stage block, not 4B profit-taking |

## 16. 4C Protection Audit

| case_id | 4C/protection trigger | label | protection read |
| --- | --- | --- | --- |
| Hansae | none hard; 4B overlay only | thesis_break_watch_only | Peak proximity warning mattered, but hard 4C evidence was not required. |
| Youngone | none | not_applicable | Positive C18 case; later drawdown does not invalidate early reorder signal. |
| Hwaseung | sell-through/inventory failure after May 2022 | hard_4c_late | The system should route unverified restocking narrative to watch/guard earlier. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
candidate_axis = L5_C18_verified_reorder_sell_through_bonus
candidate_delta = +2 shadow-only
condition = channel_reorder_score + export_mix_score + customer_quality_score + sell_through_score supported by non-price evidence
```

The sector rule says C18 is not just “consumer demand up.” It must be channel reorder that turns into production/order cadence, margin bridge, or verified sell-through. This is why Hansae and Youngone work while Hwaseung fails.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
candidate_axis_1 = C18_verified_reorder_sell_through_bonus
candidate_axis_2 = C18_unverified_restock_inventory_guard
candidate_axis_3 = C18_post_reorder_peak_4B_overlay
```

C18 should compress apparel OEM, outdoor OEM, and footwear OEM into one canonical rule: reorder is positive only when verified by sell-through/inventory normalization or durable customer quality. A customer restock headline alone is not enough.

## 19. Before / After Backtest Comparison

| profile_key | profile_id | profile_hypothesis | changed_axes | eligible_triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current calibrated proxy, no C18 scoped rule | none | 3 | 37.15 | -15.08 | 37.15 | -21.91 | 1/3 | 1 | 1 | mixed; misses Youngone and over-scores Hwaseung |
| P0b | e2r_2_0_baseline_reference | rollback reference | pre-calibrated thresholds | 3 | 37.15 | -15.08 | 37.15 | -21.91 | 1/3 | 1 | 1 | weaker false-positive guard |
| P1 | sector_specific_candidate_profile | L5 export-channel reorder quality bonus plus restock guard | C18/L5 scoped axes | 3 | 49.7 | -6.99 | 49.7 | -11.2 | 0/3 | 0 | 0 | aligned after blocking unverified restock |
| P2 | canonical_archetype_candidate_profile | C18 verified reorder/sell-through compression | canonical C18 axes | 3 | 49.7 | -6.99 | 49.7 | -11.2 | 0/3 | 0 | 0 | best score-return alignment |
| P3 | counterexample_guard_profile | restocking without inventory/sell-through proof blocked | guard only | 1 | 12.05 | -31.27 | 12.05 | -43.32 | 0/1 | 0 | 0 | false positive removed |

## 20. Score-Return Alignment Matrix

| case_id | trigger_id | score_before | stage_before | score_after | stage_after | MFE_90D | MAE_90D | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208 | R5L12_T01_HANSAE_20210208_STAGE2_ACTIONABLE_REORDER | 83.0 | Stage3-Yellow | 88.0 | Stage3-Green_C18_reorder_quality | 56.45 | -7.45 | aligned_positive |
| R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208 | R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT | 89.0 | Stage3-Green | 79.0 | 4B-overlay-on-Stage3 | 2.82 | -28.81 | overlay_aligned |
| R5L12_C18_111770_YOUNGONE_PREMIUM_OUTDOOR_REORDER_20230515 | R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER | 74.0 | Stage2-Actionable_high | 87.5 | Stage3-Green_C18_reorder_quality | 42.95 | -6.53 | aligned_positive |
| R5L12_C18_241590_HWASEUNG_FOOTWEAR_RESTOCK_FALSE_POSITIVE_20220516 | R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | 76.0 | Stage3-Yellow_false_positive_risk | 57.0 | Stage2-Watch_or_4C_watch | 12.05 | -31.27 | false_positive_removed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE | 2 | 1 | 1 | 1 | 3 | 0 | 4 | 3 | 3 | True | True | C18 now has positive + counterexample + 4B coverage; still needs C19 separate loop |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - premium_apparel_oem_reorder_green_too_late
  - footwear_restocking_without_sell_through_false_positive
  - post_reorder_peak_requires_4B_overlay
new_axis_proposed:
  - C18_verified_reorder_sell_through_bonus
  - C18_unverified_restock_inventory_guard
  - C18_post_reorder_peak_4B_overlay
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

```text
- scheduled_round / scheduled_loop consistency
- R5 / L5 round-sector consistency
- stock-web manifest max_date = 2026-02-20
- selected symbol profiles and corporate-action windows
- actual tradable OHLC anchor rows for entry/peak/drawdown calculations
- 30D / 90D / 180D MFE/MAE calculations
- positive/counterexample balance
- same_entry_group dedupe logic
- score component decomposition
```

Not validated:

```text
- live/current candidates
- stock_agent source code
- broker/API execution
- production scoring changes
- exact final source URLs for every evidence item; these are deferred for implementation intake before any promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_verified_reorder_sell_through_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+2,+2,"confirmed channel reorder plus export mix and sell-through quality should bridge Stage2 to Green earlier than generic consumer beta","Hansae and Youngone positives improve score-return alignment without reusing C20 beauty/food cases",R5L12_T01_HANSAE_20210208_STAGE2_ACTIONABLE_REORDER|R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER,2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_unverified_restock_inventory_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+1,+1,"restocking narrative without sell-through or retailer inventory normalization should not promote Stage2/Yellow","Hwaseung counterexample blocks false positive caused by customer/restocking narrative",R5L12_T04_HWASEUNG_20220516_FALSE_REORDER,1,1,1,medium,canonical_shadow_only,"guard only; not production"
shadow_weight,C18_post_reorder_peak_4B_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+1,+1,"post-reorder repricing near full-window peak with weakening incremental evidence should become 4B overlay","Hansae May 2021 row shows very low forward MFE and large MAE after peak",R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT,1,0,1,medium,canonical_shadow_only,"4B overlay only; not a sell recommendation"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208","symbol":"105630","company_name":"한세실업","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L12_T01_HANSAE_20210208_STAGE2_ACTIONABLE_REORDER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"early_export_reorder_signal_aligned_with_high_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Apparel OEM reorder/reopening visibility became investable before full reported revision confirmation; the later May 2021 peak shows why C18 also needs 4B inventory/positioning overlay."}
{"row_type":"case","case_id":"R5L12_C18_111770_YOUNGONE_PREMIUM_OUTDOOR_REORDER_20230515","symbol":"111770","company_name":"영원무역","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"reorder_quality_signal_preceded_large_90D_MFE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Premium outdoor/apparel OEM reorder plus margin quality acted as a clearer C18 signal than generic consumer beta; current profile would tend to wait for later confirmation."}
{"row_type":"case","case_id":"R5L12_C18_241590_HWASEUNG_FOOTWEAR_RESTOCK_FALSE_POSITIVE_20220516","symbol":"241590","company_name":"화승엔터프라이즈","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L12_T04_HWASEUNG_20220516_FALSE_REORDER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"inventory_destocking_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Global footwear customer/restocking narrative had price reaction but lacked confirmed sell-through and retailer inventory normalization; the forward path shows large MAE and weak MFE."}
{"row_type":"trigger","trigger_id":"R5L12_T01_HANSAE_20210208_STAGE2_ACTIONABLE_REORDER","case_id":"R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208","symbol":"105630","company_name":"한세실업","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE","sector":"소비재·유통·브랜드","primary_archetype":"CONSUMER_EXPORT_CHANNEL_REORDER","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test","stage2_actionable_bonus_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2021-02-08","evidence_available_at_that_date":"U.S. apparel reorder/reopening visibility and OEM operating leverage were visible as a non-price evidence family; price reaction confirmed that the market had begun to price channel reorder recovery.","evidence_source":"historical public earnings/reorder evidence family plus stock-web OHLC row 2021-02-08; exact source URL not promoted to production here","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105630/2021.csv","profile_path":"atlas/symbol_profiles/105/105630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-08","entry_price":17450,"MFE_30D_pct":33.52,"MFE_90D_pct":56.45,"MFE_180D_pct":56.45,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.45,"MAE_90D_pct":-7.45,"MAE_180D_pct":-7.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-05-28","peak_price":27300,"drawdown_after_peak_pct":-30.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12_105630_20210208_17450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT","case_id":"R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208","symbol":"105630","company_name":"한세실업","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE","sector":"소비재·유통·브랜드","primary_archetype":"CONSUMER_EXPORT_CHANNEL_REORDER","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test","stage2_actionable_bonus_stress_test"],"trigger_type":"4B-overlay","trigger_date":"2021-05-28","evidence_available_at_that_date":"After the reorder thesis repriced rapidly, price was near the observed cycle high and incremental evidence was no longer improving enough to justify fresh positive-stage promotion.","evidence_source":"stock-web OHLC row 2021-05-28 plus non-price watch items: reorder cadence and retailer inventory exhaustion risk; production handoff should verify company/analyst source URLs before code promotion","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105630/2021.csv","profile_path":"atlas/symbol_profiles/105/105630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-28","entry_price":26550,"MFE_30D_pct":2.82,"MFE_90D_pct":2.82,"MFE_180D_pct":2.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.69,"MAE_90D_pct":-28.81,"MAE_180D_pct":-28.81,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-28","peak_price":27300,"drawdown_after_peak_pct":-30.77,"green_lateness_ratio":0.924,"four_b_local_peak_proximity":0.924,"four_b_full_window_peak_proximity":0.924,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12_105630_20210528_26550","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same Hansae structural case; separate 4B overlay timing audit, not a new aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER","case_id":"R5L12_C18_111770_YOUNGONE_PREMIUM_OUTDOOR_REORDER_20230515","symbol":"111770","company_name":"영원무역","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE","sector":"소비재·유통·브랜드","primary_archetype":"CONSUMER_EXPORT_CHANNEL_REORDER","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test","stage2_actionable_bonus_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","evidence_available_at_that_date":"Premium outdoor/apparel OEM reorder and margin-quality signal was visible before the June-August price acceleration; the signal was not a generic consumer beta.","evidence_source":"historical public earnings/reorder evidence family plus stock-web OHLC row 2023-05-15; exact source URL not promoted to production here","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv","profile_path":"atlas/symbol_profiles/111/111770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-15","entry_price":47500,"MFE_30D_pct":31.58,"MFE_90D_pct":42.95,"MFE_180D_pct":42.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.53,"MAE_90D_pct":-6.53,"MAE_180D_pct":-14.95,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-16","peak_price":67900,"drawdown_after_peak_pct":-40.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12_111770_20230515_47500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L12_T04_HWASEUNG_20220516_FALSE_REORDER","case_id":"R5L12_C18_241590_HWASEUNG_FOOTWEAR_RESTOCK_FALSE_POSITIVE_20220516","symbol":"241590","company_name":"화승엔터프라이즈","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_FOOTWEAR_OEM_EXPORT_CHANNEL_REORDER_INVENTORY_CYCLE","sector":"소비재·유통·브랜드","primary_archetype":"CONSUMER_EXPORT_CHANNEL_REORDER","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test","stage2_actionable_bonus_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2022-05-16","evidence_available_at_that_date":"Footwear customer/restocking narrative looked actionable, but sell-through and retailer inventory normalization were not confirmed. The price path makes this a C18 counterexample.","evidence_source":"historical public customer/restocking narrative plus stock-web OHLC row 2022-05-16; exact URL verification deferred to coding handoff if promoted","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241590/2022.csv","profile_path":"atlas/symbol_profiles/241/241590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-05-16","entry_price":15350,"MFE_30D_pct":12.05,"MFE_90D_pct":12.05,"MFE_180D_pct":12.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.85,"MAE_90D_pct":-31.27,"MAE_180D_pct":-43.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-05-17","peak_price":17200,"drawdown_after_peak_pct":-49.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_positive_block","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L12_241590_20220516_15350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208","trigger_id":"R5L12_T01_HANSAE_20210208_STAGE2_ACTIONABLE_REORDER","symbol":"105630","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":54,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":66,"export_mix_score":64,"retailer_inventory_score":54,"sell_through_score":58,"brand_customer_diversification_score":66,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":66,"revision_score":58,"relative_strength_score":74,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":84,"export_mix_score":82,"retailer_inventory_score":66,"sell_through_score":66,"brand_customer_diversification_score":72,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green_C18_reorder_quality","changed_components":["channel_reorder_score","export_mix_score","retailer_inventory_score","sell_through_score","customer_quality_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"C18 adds channel-reorder/export-mix quality when retailer reorder and operating leverage are visible before full EPS revision confirmation.","MFE_90D_pct":56.45,"MAE_90D_pct":-7.45,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L12_C18_105630_HANSAE_US_APPAREL_REORDER_20210208","trigger_id":"R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT","symbol":"105630","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":72,"revision_score":70,"relative_strength_score":82,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":76,"execution_risk_score":42,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":84,"export_mix_score":82,"retailer_inventory_score":58,"sell_through_score":66,"brand_customer_diversification_score":0,"positioning_overheat_score":-2,"thesis_break_score":0},"weighted_score_before":89.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":72,"revision_score":70,"relative_strength_score":82,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":74,"export_mix_score":78,"retailer_inventory_score":50,"sell_through_score":60,"brand_customer_diversification_score":0,"positioning_overheat_score":-12,"thesis_break_score":0},"weighted_score_after":79.0,"stage_label_after":"4B-overlay-on-Stage3","changed_components":["channel_reorder_score","export_mix_score","retailer_inventory_score","sell_through_score","customer_quality_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"Near-peak channel-reorder confirmation should convert to 4B overlay when fresh sell-through/reorder acceleration weakens.","MFE_90D_pct":2.82,"MAE_90D_pct":-28.81,"score_return_alignment_label":"overlay_aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L12_C18_111770_YOUNGONE_PREMIUM_OUTDOOR_REORDER_20230515","trigger_id":"R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER","symbol":"111770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":60,"revision_score":50,"relative_strength_score":58,"customer_quality_score":68,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":34,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":58,"export_mix_score":70,"retailer_inventory_score":62,"sell_through_score":64,"brand_customer_diversification_score":72,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable_high","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":70,"revision_score":58,"relative_strength_score":66,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":82,"export_mix_score":84,"retailer_inventory_score":72,"sell_through_score":72,"brand_customer_diversification_score":78,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green_C18_reorder_quality","changed_components":["channel_reorder_score","export_mix_score","retailer_inventory_score","sell_through_score","customer_quality_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"Premium channel reorder plus customer-quality evidence should bridge from Stage2-Actionable to Green even when classic revision score is not yet dominant.","MFE_90D_pct":42.95,"MAE_90D_pct":-6.53,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L12_C18_241590_HWASEUNG_FOOTWEAR_RESTOCK_FALSE_POSITIVE_20220516","trigger_id":"R5L12_T04_HWASEUNG_20220516_FALSE_REORDER","symbol":"241590","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":42,"revision_score":42,"relative_strength_score":58,"customer_quality_score":58,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":46,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":62,"export_mix_score":58,"retailer_inventory_score":38,"sell_through_score":32,"brand_customer_diversification_score":44,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":34,"revision_score":32,"relative_strength_score":42,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":38,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":34,"export_mix_score":44,"retailer_inventory_score":18,"sell_through_score":16,"brand_customer_diversification_score":34,"positioning_overheat_score":0,"thesis_break_score":-8},"weighted_score_after":57.0,"stage_label_after":"Stage2-Watch_or_4C_watch","changed_components":["channel_reorder_score","export_mix_score","retailer_inventory_score","sell_through_score","customer_quality_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"C18 should not promote restocking narratives unless retailer inventory and sell-through evidence are verified; this counterexample blocks false Yellow/Green.","MFE_90D_pct":12.05,"MAE_90D_pct":-31.27,"score_return_alignment_label":"false_positive_removed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":12,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["premium_apparel_oem_reorder_green_too_late","footwear_restocking_without_sell_through_false_positive","post_reorder_peak_requires_4B_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R5
completed_loop = 12
next_round = R6
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Stock-web manifest checked: atlas/manifest.json
Schema path checked by manifest: atlas/schema.json
Universe path checked by manifest: atlas/universe/all_symbols.csv
Profiles checked:
- atlas/symbol_profiles/105/105630.json
- atlas/symbol_profiles/111/111770.json
- atlas/symbol_profiles/241/241590.json
OHLC shards checked:
- atlas/ohlcv_tradable_by_symbol_year/105/105630/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/241/241590/2022.csv
```

This file contains historical calibration research only. It is not an investment recommendation, not a live watchlist, and not a production scoring patch.
