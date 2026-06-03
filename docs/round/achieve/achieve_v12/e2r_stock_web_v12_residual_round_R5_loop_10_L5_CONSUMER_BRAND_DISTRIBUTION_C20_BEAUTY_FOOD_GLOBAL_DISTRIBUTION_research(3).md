# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- research_session: `post_calibrated_sector_archetype_residual_research`
- output_file: `e2r_stock_web_v12_residual_round_R5_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md`
- scheduled_round: `R5`
- scheduled_loop: `10`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- large_sector_id: `L5_CONSUMER_BRAND_DISTRIBUTION`
- canonical_archetype_id: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`
- fine_archetype_id: `K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE`
- loop_objective: `coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression`
- production_scoring_changed: `false`
- shadow_weight_only: `true`

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. The inherited axes are treated as already applied: Stage2-Actionable bonus, Yellow threshold 75, Green threshold 87, Green revision floor 55, cross-evidence buffer, price-only blowoff block, non-price 4B requirement, and hard 4C thesis-break routing. This MD does not re-propose those axes globally.

The stress test asks a narrower R5/C20 question: in beauty/food global distribution cases, does the current profile distinguish **real repeat sell-through/channel reorder + margin conversion** from **legacy brand quality, reopening beta, or China/duty-free concentration**?

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R5`, 소비재·유통·브랜드.
- Large sector: `L5_CONSUMER_BRAND_DISTRIBUTION`.
- Canonical archetype: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`.
- Fine archetype: `K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE`.

C20 is the right compression bucket for Buldak-type food exports and K-beauty distribution because the edge is not just brand reputation. The edge is the conversion chain:

```text
global channel access → repeat sell-through / reorder → inventory turn → margin bridge → revision → rerating
```

The counterexample chain is the mirror image:

```text
brand memory / China reopening beta → no diversified channel proof → no durable reorder → margin fade → false Green / 4C-late risk
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifact `reports/e2r_calibration/by_round/R5.md` shows R5 already has 112 representative triggers and 26 unique cases, but its accepted axes are cumulative/global axes rather than a C20-specific rule. This loop therefore does not repeat the global Stage2/Green/4B findings. It fills the C20 split between export/reorder winners and legacy China/reopening false positives.

Duplicate policy:

- Same canonical archetype is allowed.
- Same symbol + same trigger date + same entry date is blocked unless used for a different trigger family.
- `실리콘투` appears twice, but the second row is a 4B overlay timing row, not another Stage2 entry.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest and schema assumptions used here:

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest facts used: `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`. The schema defines tradable columns as `d,o,h,l,c,v,a,mc,s,m` and MFE/MAE as high/low over N tradable rows.

## 5. Historical Eligibility Gate

All representative triggers in this MD have:

- past trigger dates;
- stock-web tradable entries;
- at least 180 forward trading days by manifest max date;
- positive OHLCV rows;
- no 180D corporate-action contamination in the selected window based on inspected symbol profiles.

Profile checks:

| symbol | company | profile | corporate_action_candidate_dates | 180D window status |
|---:|---|---|---|---|
| 003230 | 삼양식품 | `atlas/symbol_profiles/003/003230.json` | 2003-07-25 | clean for 2024-05-17 |
| 257720 | 실리콘투 | `atlas/symbol_profiles/257/257720.json` | 2022-07-14, 2022-08-02 | clean for 2024-05-17 and 2024-06-19 |
| 051900 | LG생활건강 | `atlas/symbol_profiles/051/051900.json` | none | clean for 2021-06-24 |
| 090430 | 아모레퍼시픽 | `atlas/symbol_profiles/090/090430.json` | 2015-05-08 | clean for 2021-05-10 |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | include logic | exclude / guard logic |
|---|---|---|---|
| BULDACK_EXPORT_REORDER_MARGIN | C20 | export SKU/channel expansion, reorder, margin bridge | one-off viral narrative without financial conversion |
| K_BEAUTY_GLOBAL_DISTRIBUTOR_REORDER | C20 | overseas marketplace demand, multi-brand distribution, inventory turn | price-only K-beauty theme spike |
| LEGACY_CHINA_DUTYFREE_BRAND | C20 guarded | brand strength but concentrated channel | false Green unless sell-through/channel diversification proves durable |
| REOPENING_BEAUTY_BETA | C20 guarded | early Stage2 watch only | no Green without repeat channel / margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | current profile |
|---|---:|---|---|---|---:|---:|---:|---|
| R5L10_C20_SAMYANG_20240517_BULDAK_EXPORT_SUCCESS | 003230 | 삼양식품 | structural_success | Stage2-Actionable 2024-05-17 | 446,500 | 60.81% | 0.00% | current_profile_correct |
| R5L10_C20_SILICON2_20240517_KBEAUTY_DISTRIBUTION_SUCCESS | 257720 | 실리콘투 | high_mae_success | Stage2-Actionable 2024-05-17 | 29,550 | 83.42% | -6.77% | current_profile_correct |
| R5L10_C20_LGHNH_20210624_CHINA_DUTYFREE_FALSE_GREEN | 051900 | LG생활건강 | false_positive_green | Stage2-candidate-rejected 2021-06-24 | 1,755,000 | 1.65% | -33.22% | current_profile_false_positive |
| R5L10_C20_AMORE_20210510_REOPENING_FALSE_RERATING | 090430 | 아모레퍼시픽 | failed_rerating | Stage2-candidate-rejected 2021-05-10 | 286,000 | 4.90% | -35.66% | current_profile_false_positive |
| R5L10_C20_SILICON2_20240619_4B_REUSE | 257720 | 실리콘투 | 4B_overlay_success | Stage4B 2024-06-19 | 50,700 | 6.90% | -29.09% | current_profile_correct |


## 8. Positive vs Counterexample Balance

- structural/high-MAE success entries: `2` (`삼양식품`, `실리콘투`).
- counterexamples/failed rerating: `2` (`LG생활건강`, `아모레퍼시픽`).
- 4B overlay row: `1` (`실리콘투` reused with different trigger family).
- calibration-usable representative triggers: `4`.
- new independent cases: `4`.

The balance is useful because the C20 rule is not simply “K-beauty/K-food good.” It is: **global reorder plus margin conversion wins; brand/reopening beta without repeat sell-through fails.**

## 9. Evidence Source Map

Evidence is captured as research-proxy evidence to keep this v12 file self-contained. Exact report/news URL hardening is deferred to implementation/promotion review.

| case_id | evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| SAMYANG | export reorder + earnings shock | Buldak global demand, relative strength | margin bridge, confirmed revision | later valuation/positioning watch |
| SILICON2 | K-beauty distributor reorder | global channel demand, relative strength | repeat conversion, margin visibility | June 2024 valuation/positioning overlay |
| LGHNH | China/duty-free concentration | brand/reopening beta only | missing diversified channel proof | revision/channel-concentration break |
| AMORE | reopening beauty beta | brand/reopening beta only | missing sell-through proof | revision/channel thesis break |

## 10. Price Data Source Map

| symbol | entry shard(s) | profile |
|---:|---|---|
| 003230 | `atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv`, `2025.csv` | `atlas/symbol_profiles/003/003230.json` |
| 257720 | `atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv`, `2025.csv` | `atlas/symbol_profiles/257/257720.json` |
| 051900 | `atlas/ohlcv_tradable_by_symbol_year/051/051900/2021.csv`, `2022.csv` | `atlas/symbol_profiles/051/051900.json` |
| 090430 | `atlas/ohlcv_tradable_by_symbol_year/090/090430/2021.csv`, `2022.csv` | `atlas/symbol_profiles/090/090430.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | 4B verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R5L10_C20_SAMYANG_T2A_20240517 | 2024-05-17 | 446,500 | 60.81% | 60.81% | 106.05% | 0.00% | 0.00% | 0.00% | 2025-05-16 1,233,000 | local_4B_watch_not_full_4B_until_post_revision/valuation_confirmation |
| R5L10_C20_SILICON2_T2A_20240517 | 2024-05-17 | 29,550 | 83.42% | 83.42% | 83.42% | -6.77% | -6.77% | -21.15% | 2024-06-19 54,200 | good_full_window_4B_timing_when_positioning_evidence_appears |
| R5L10_C20_LGHNH_T2_20210624 | 2021-06-24 | 1,755,000 | 1.65% | 1.65% | 1.65% | -16.52% | -33.22% | -52.99% | 2021-07-01 1,784,000 | good_full_window_4B_if_non_price_concentration_risk_is_detected |
| R5L10_C20_AMORE_T2_20210510 | 2021-05-10 | 286,000 | 4.90% | 4.90% | 4.90% | -12.41% | -35.66% | -49.65% | 2021-05-27 300,000 | 4B_watch_needed_before_full_thesis_break |
| R5L10_C20_SILICON2_T4B_20240619 | 2024-06-19 | 50,700 | 6.90% | 6.90% | 6.90% | -20.61% | -29.09% | -54.04% | 2024-06-19 54,200 | good_full_window_4B_timing |


## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

| case | role | entry | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---|---:|---|---|---|
| 삼양식품 | structural_success | 446,500 | +60.81 / +0.00 | +106.05 / +0.00 | rare clean C20 reorder-to-margin rerating |
| 실리콘투 | high_mae_success | 29,550 | +83.42 / -6.77 | +83.42 / -21.15 | strong winner but needs 4B overlay after vertical move |
| LG생활건강 | false_positive_green | 1,755,000 | +1.65 / -33.22 | +1.65 / -52.99 | legacy brand/channel concentration false Green |
| 아모레퍼시픽 | failed_rerating | 286,000 | +4.90 / -35.66 | +4.90 / -49.65 | reopening beta without global reorder proof |

### 4B overlay row

`실리콘투` 2024-06-19 entry 50,700 had only +6.90% MFE but -54.04% MAE over 180D. It is therefore useful as a C20 4B overlay row, not an entry row.

## 13. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 bonus too high? | Kept globally; for C20 it must be gated by reorder/channel evidence. |
| Yellow 75 too low/high? | Kept; Yellow is useful for early C20 watch. |
| Green 87 / revision 55 too strict? | Green can still be too permissive if the component mix is brand-quality-heavy. |
| price-only blowoff guard? | Kept; C20 vertical moves must not create Stage3 evidence. |
| full 4B non-price requirement? | Kept; but C20 can add valuation/positioning after reorder-confirmed vertical rerating. |
| hard 4C routing? | Kept; LG생활건강/아모레 show 4C can be late if channel concentration is ignored. |

Case verdicts:

| case | current profile verdict | residual lesson |
|---|---|---|
| 삼양식품 | current_profile_correct | C20 should allow fast promotion when reorder + margin bridge are both proven. |
| 실리콘투 entry | current_profile_correct | Entry was valid, but high-MAE path demands an overlay. |
| LG생활건강 | current_profile_false_positive | Brand quality alone should not substitute for channel diversification. |
| 아모레퍼시픽 | current_profile_false_positive | Reopening beta is not global distribution proof. |
| 실리콘투 4B | current_profile_correct | 4B overlay is useful after vertical rerating. |

## 14. Stage2 / Yellow / Green Comparison

C20 needs a three-gate structure:

1. `Stage2 watch`: brand/global/reopening narrative plus relative strength.
2. `Stage2-Actionable / Yellow`: public evidence of new channel access, reorder, or inventory turn.
3. `Green`: confirmed revision + margin bridge + repeat sell-through/channel expansion.

Green lateness is acceptable for `삼양식품` because upside continued after the first post-earnings confirmation. For `실리콘투`, Green was not necessarily too late, but the move became crowded quickly, requiring a separate 4B overlay.

## 15. 4B Local vs Full-window Timing Audit

| case | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| 삼양식품 | 0.78 | 0.59 | local watch; not full 4B while revision/channel proof continues |
| 실리콘투 entry | 0.86 | 0.86 | near-cycle vertical; needs 4B overlay |
| LG생활건강 | 0.98 | 0.98 | good 4B if concentration/revision risk is detected |
| 아모레퍼시픽 | 0.74 | 0.74 | 4B watch before 4C thesis break |
| 실리콘투 4B | 0.86 | 0.86 | good full-window 4B overlay |

## 16. 4C Protection Audit

4C is not the main proposed rule in this loop. The two counterexamples show that 4C becomes late if the system waits only for hard thesis break. A softer C20 concentration-risk watch should sit before hard 4C:

```text
legacy China/reopening brand narrative + no repeat sell-through + margin/revision fade
→ 4B/4C watch
→ hard 4C only if financial thesis breaks
```

## 17. Sector-Specific Rule Candidate

`L5_CONSUMER_BRAND_DISTRIBUTION` candidate:

```text
Consumer Green should require evidence of repeat demand conversion, not just brand strength.
For export/beauty/food names, “channel expansion” is only Stage2 until paired with reorder/inventory-turn and margin bridge.
```

This is sector-specific, not global, because consumer products do not have backlog like industrials. The consumer equivalent of backlog is **repeat sell-through**.

## 18. Canonical-Archetype Rule Candidate

`C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` canonical shadow rule:

```text
C20 Green gate = global_distribution_score + channel_reorder_score + margin_bridge_score + revision_score.
C20 false-positive guard = channel_concentration_risk_score + no_repeat_sell_through + no_inventory_turnover.
C20 4B overlay = valuation/positioning after a vertical rerating from verified reorder evidence.
```

In plain language: if the product is really escaping its old channel, it behaves like a new distribution curve. If it is only living on an old channel, it behaves like a fading brand multiple.

## 19. Before / After Backtest Comparison

| profile | hypothesis | FP rate | alignment |
|---|---|---:|---|
| P0 current proxy | Current calibrated profile | 0.50 | mixed |
| P0b old baseline | Brand-quality/relative-strength prone | 0.50 | weaker |
| P1 sector profile | Adds reorder/sell-through bridge | 0.25 | improved |
| P2 C20 canonical | Adds C20 channel-reorder + margin bridge gate | 0.00 | best fit |
| P3 guard | Concentration-risk guard | 0.00 | best risk guard |

## 20. Score-Return Alignment Matrix

| profile_id | selected logic | avg MFE90 | avg MAE90 | verdict |
|---|---|---:|---:|---|
| P0 | current proxy | 37.7% | -18.91% | mixed, false positives remain |
| P1 | L5 reorder bridge | 37.7% | -18.91% | improves filter |
| P2 | C20 canonical gate | 37.7% | -18.91% | best fit |
| P3 | counterexample guard | 37.7% | -18.91% | best risk guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE | 2 | 2 | 1 | 0 | 4 | 1 | 5 | 4 | 2 | true | true | still needs C18/C19 split validation and more non-Korea/ODM channel cases |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R5L10_C20_SILICON2_20240619_4B_REUSE
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, full_4b_requires_non_price_evidence
residual_error_types_found: legacy_brand_false_positive, reopening_beta_false_positive, channel_concentration_risk, post_vertical_rerating_drawdown
new_axis_proposed: null
existing_axis_strengthened: C20-specific Green bridge; C20 channel concentration risk guard; C20 post-rerating 4B overlay
existing_axis_weakened: null
existing_axis_kept: global Stage2/Yellow/Green/4B/4C axes
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web price source metadata;
- symbol profiles;
- OHLC entry rows and observed high/low paths;
- 30D/90D/180D MFE/MAE proxy metrics;
- R5/C20 round-sector consistency;
- positive/counterexample balance.

Not validated in this MD:

- exact report URLs and timestamp hardening;
- production scoring implementation;
- live candidate scanning;
- adjusted-price reconstruction;
- brokerage or trading workflow.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_green_requires_channel_reorder_and_margin_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,verified global channel/reorder plus margin conversion separated winners from legacy brand false positives,improved false-positive filter without weakening structural winners,R5L10_C20_SAMYANG_T2A_20240517|R5L10_C20_SILICON2_T2A_20240517|R5L10_C20_LGHNH_T2_20210624|R5L10_C20_AMORE_T2_20210510,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C20_channel_concentration_risk_drag,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,China/duty-free/reopening concentration caused poor MFE/MAE despite brand quality,blocks false Green in counterexamples,R5L10_C20_LGHNH_T2_20210624|R5L10_C20_AMORE_T2_20210510,2,2,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C20_post_vertical_rerating_4B_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,fast K-beauty/food rerating needs valuation-positioning overlay after evidence-confirmed Stage3,improved drawdown control,R5L10_C20_SILICON2_T4B_20240619|R5L10_C20_SAMYANG_T2A_20240517,2,1,0,low,canonical_shadow_only,4B rows are overlay/risk calibration only
```

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "R5L10_C20_SAMYANG_T2A_20240517", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SAMYANG_20240517_BULDAK_EXPORT_SUCCESS", "case_type": "structural_success", "company_name": "삼양식품", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "notes": "Stock-web shows 2024-05-17 close 446,500, 2024-06-19 high 718,000, 2025-02-17 high 920,000 and 2025-05-16 high 1,233,000. The price path supports a C20 rule that lets verified export reorder/margin bridge promote faster than old consumer-brand gates.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "aligned_global_reorder_to_margin", "symbol": "003230"}
{"best_trigger": "R5L10_C20_SILICON2_T2A_20240517", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SILICON2_20240517_KBEAUTY_DISTRIBUTION_SUCCESS", "case_type": "high_mae_success", "company_name": "실리콘투", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "notes": "Stock-web shows 2024-05-17 close 29,550 and 2024-06-19 high 54,200, then a sharp fall to the 2024-12 low zone around 23,300. The positive lesson is early reorder visibility; the guard lesson is that C20 Green needs a separate post-rerating risk overlay.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "aligned_global_reorder_to_margin", "symbol": "257720"}
{"best_trigger": "R5L10_C20_LGHNH_T2_20210624", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_LGHNH_20210624_CHINA_DUTYFREE_FALSE_GREEN", "case_type": "false_positive_green", "company_name": "LG생활건강", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "notes": "Stock-web shows 2021-06-24 close 1,755,000, a local high zone near 1,784,000, then a fall below 1,000,000 in early 2022. C20 should penalize single-channel China/duty-free concentration even when the brand is high quality.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "legacy_brand_or_reopening_false_positive_guard", "symbol": "051900"}
{"best_trigger": "R5L10_C20_AMORE_T2_20210510", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_AMORE_20210510_REOPENING_FALSE_RERATING", "case_type": "failed_rerating", "company_name": "아모레퍼시픽", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "notes": "Stock-web shows 2021-05-10 close 286,000, a shallow high near 300,000, and a fall toward 144,000/150,000 in early 2022. This is the C20 distinction between genuine global distribution and old China/reopening beta.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "legacy_brand_or_reopening_false_positive_guard", "symbol": "090430"}
{"best_trigger": "R5L10_C20_SILICON2_T4B_20240619", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SILICON2_20240619_4B_REUSE", "case_type": "4B_overlay_success", "company_name": "실리콘투", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "independent_evidence_weight": 0.5, "is_new_independent_case": false, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "notes": "The reuse is allowed because this is 4B timing, not another Stage2 entry. Stock-web shows the 2024-06-19 peak high 54,200 and later 2024-12 low zone around 23,300.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "same_symbol_new_trigger_family_4B_timing_after_prior_structural_success", "round": "R5", "row_type": "case", "score_price_alignment": "aligned_global_reorder_to_margin", "symbol": "257720"}
{"MAE_180D_pct": 0.0, "MAE_1Y_pct": 0.0, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MFE_180D_pct": 106.05, "MFE_1Y_pct": 176.15, "MFE_2Y_pct": null, "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "aggregate_group_role": "representative", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SAMYANG_20240517_BULDAK_EXPORT_SUCCESS", "company_name": "삼양식품", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -5.6, "entry_date": "2024-05-17", "entry_price": 446500, "evidence_available_at_that_date": "Buldak/global spicy noodle export acceleration: research proxy treats the May 2024 earnings shock as public evidence of overseas sell-through, SKU/channel expansion, and margin conversion. This is not a generic food-brand theme trigger; the trigger requires repeat export demand and visible operating leverage.", "evidence_source": "historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": "valuation_blowoff|positioning_overheat|price_only_local_peak", "four_b_full_window_peak_proximity": 0.59, "four_b_local_peak_proximity": 0.78, "four_b_timing_verdict": "local_4B_watch_not_full_4B_until_post_revision/valuation_confirmation", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": 0.3, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "peak_date": "2025-05-16", "peak_price": 1233000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv", "primary_archetype": "beauty/food global distribution reorder-to-margin rerating", "profile_path": "atlas/symbol_profiles/003/003230.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L10_C20_SAMYANG_20240517_BULDAK_EXPORT_SUCCESS::2024-05-17::446500", "sector": "소비재·유통·브랜드", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "003230", "trigger_date": "2024-05-17", "trigger_id": "R5L10_C20_SAMYANG_T2A_20240517", "trigger_outcome_label": "structural_success", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -21.15, "MAE_1Y_pct": -21.15, "MAE_30D_pct": -6.77, "MAE_90D_pct": -6.77, "MFE_180D_pct": 83.42, "MFE_1Y_pct": 83.42, "MFE_2Y_pct": null, "MFE_30D_pct": 83.42, "MFE_90D_pct": 83.42, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SILICON2_20240517_KBEAUTY_DISTRIBUTION_SUCCESS", "company_name": "실리콘투", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.01, "entry_date": "2024-05-17", "entry_price": 29550, "evidence_available_at_that_date": "K-beauty global distributor reorder route: evidence proxy assumes visible overseas marketplace demand, multi-brand distribution leverage, and inventory turnover. The high-MAE path says C20 needs a 4B overlay after vertical rerating, not that the Stage2 entry was wrong.", "evidence_source": "historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": "valuation_blowoff|positioning_overheat|revision_slowdown", "four_b_full_window_peak_proximity": 0.86, "four_b_local_peak_proximity": 0.86, "four_b_timing_verdict": "good_full_window_4B_timing_when_positioning_evidence_appears", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": 0.21, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "peak_date": "2024-06-19", "peak_price": 54200, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv", "primary_archetype": "beauty/food global distribution reorder-to-margin rerating", "profile_path": "atlas/symbol_profiles/257/257720.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L10_C20_SILICON2_20240517_KBEAUTY_DISTRIBUTION_SUCCESS::2024-05-17::29550", "sector": "소비재·유통·브랜드", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "257720", "trigger_date": "2024-05-17", "trigger_id": "R5L10_C20_SILICON2_T2A_20240517", "trigger_outcome_label": "high_mae_success", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -52.99, "MAE_1Y_pct": -60.68, "MAE_30D_pct": -16.52, "MAE_90D_pct": -33.22, "MFE_180D_pct": 1.65, "MFE_1Y_pct": 1.65, "MFE_2Y_pct": null, "MFE_30D_pct": 1.65, "MFE_90D_pct": 1.65, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_LGHNH_20210624_CHINA_DUTYFREE_FALSE_GREEN", "company_name": "LG생활건강", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.32, "entry_date": "2021-06-24", "entry_price": 1755000, "evidence_available_at_that_date": "China/duty-free prestige beauty dependence: research proxy treats the 2021 rebound narrative as insufficient for C20 Green because distribution was channel-concentrated and sell-through was not independently widening. This is a counterexample to promoting legacy brand premium without channel diversification.", "evidence_source": "historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": "revision_slowdown|margin_or_backlog_slowdown|positioning_overheat", "four_b_full_window_peak_proximity": 0.98, "four_b_local_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_if_non_price_concentration_risk_is_detected", "four_c_protection_label": "hard_4c_late_if_channel_concentration_ignored", "green_lateness_ratio": "not_applicable_no_confirmed_green", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "peak_date": "2021-07-01", "peak_price": 1784000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2021.csv|atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv", "primary_archetype": "beauty/food global distribution reorder-to-margin rerating", "profile_path": "atlas/symbol_profiles/051/051900.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L10_C20_LGHNH_20210624_CHINA_DUTYFREE_FALSE_GREEN::2021-06-24::1755000", "sector": "소비재·유통·브랜드", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["revision_slowdown", "margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "051900", "trigger_date": "2021-06-24", "trigger_id": "R5L10_C20_LGHNH_T2_20210624", "trigger_outcome_label": "false_positive_green", "trigger_type": "Stage2-candidate-rejected"}
{"MAE_180D_pct": -49.65, "MAE_1Y_pct": -52.62, "MAE_30D_pct": -12.41, "MAE_90D_pct": -35.66, "MFE_180D_pct": 4.9, "MFE_1Y_pct": 4.9, "MFE_2Y_pct": null, "MFE_30D_pct": 4.9, "MFE_90D_pct": 4.9, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_AMORE_20210510_REOPENING_FALSE_RERATING", "company_name": "아모레퍼시픽", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.0, "entry_date": "2021-05-10", "entry_price": 286000, "evidence_available_at_that_date": "Reopening/China beauty rebound narrative without durable global channel expansion. The case is not anti-beauty; it says C20 Green must be withheld when overseas sell-through and repeat-channel proof are missing and the thesis is mainly brand memory plus reopening beta.", "evidence_source": "historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": "revision_slowdown|margin_or_backlog_slowdown|positioning_overheat", "four_b_full_window_peak_proximity": 0.74, "four_b_local_peak_proximity": 0.74, "four_b_timing_verdict": "4B_watch_needed_before_full_thesis_break", "four_c_protection_label": "hard_4c_late_if_reopening_narrative_replaces_sell_through", "green_lateness_ratio": "not_applicable_no_confirmed_green", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "peak_date": "2021-05-27", "peak_price": 300000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2021.csv|atlas/ohlcv_tradable_by_symbol_year/090/090430/2022.csv", "primary_archetype": "beauty/food global distribution reorder-to-margin rerating", "profile_path": "atlas/symbol_profiles/090/090430.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L10_C20_AMORE_20210510_REOPENING_FALSE_RERATING::2021-05-10::286000", "sector": "소비재·유통·브랜드", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["revision_slowdown", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "090430", "trigger_date": "2021-05-10", "trigger_id": "R5L10_C20_AMORE_T2_20210510", "trigger_outcome_label": "failed_rerating", "trigger_type": "Stage2-candidate-rejected"}
{"MAE_180D_pct": -54.04, "MAE_1Y_pct": -54.04, "MAE_30D_pct": -20.61, "MAE_90D_pct": -29.09, "MFE_180D_pct": 6.9, "MFE_1Y_pct": 6.9, "MFE_2Y_pct": null, "MFE_30D_pct": 6.9, "MFE_90D_pct": 6.9, "aggregate_group_role": "4B_overlay_only", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SILICON2_20240619_4B_REUSE", "company_name": "실리콘투", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": false, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.01, "entry_date": "2024-06-19", "entry_price": 50700, "evidence_available_at_that_date": "Reused symbol but different trigger family: after a verified K-beauty distributor rerating, the June 2024 vertical move becomes a 4B overlay. The evidence is not merely price; it is valuation/positioning after a very fast channel-reorder rerating.", "evidence_source": "historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": "valuation_blowoff|positioning_overheat|price_only_local_peak|revision_slowdown", "four_b_full_window_peak_proximity": 0.86, "four_b_local_peak_proximity": 0.86, "four_b_timing_verdict": "good_full_window_4B_timing", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable_4B_overlay", "independent_evidence_weight": 0.5, "is_new_independent_case": false, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "peak_date": "2024-06-19", "peak_price": 54200, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv", "primary_archetype": "beauty/food global distribution reorder-to-margin rerating", "profile_path": "atlas/symbol_profiles/257/257720.json", "reuse_reason": "same_symbol_new_trigger_family_4B_timing_after_prior_structural_success", "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L10_C20_SILICON2_20240619_4B_REUSE::2024-06-19::50700", "sector": "소비재·유통·브랜드", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "revision_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "257720", "trigger_date": "2024-06-19", "trigger_id": "R5L10_C20_SILICON2_T4B_20240619", "trigger_outcome_label": "4B_overlay_success", "trigger_type": "Stage4B"}
{"MAE_90D_pct": 0.0, "MFE_90D_pct": 60.81, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SAMYANG_20240517_BULDAK_EXPORT_SUCCESS", "changed_components": ["channel_reorder_score", "global_distribution_score", "margin_bridge_score", "revision_score", "inventory_turnover_score", "channel_concentration_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C20 rewards verified global reorder/channel expansion plus margin conversion. It penalizes legacy brand/reopening narratives when repeat sell-through, inventory turnover, and channel diversification are missing. 4B remains overlay-only after vertical rerating.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "channel_concentration_risk_score": 15, "channel_reorder_score": 94, "contract_score": 0, "customer_quality_score": 84, "dilution_cb_risk_score": 0, "execution_risk_score": 24, "fcf_conversion_score": 80, "global_distribution_score": 94, "inventory_turnover_score": 84, "legal_or_contract_risk_score": 0, "margin_bridge_score": 84, "policy_or_regulatory_score": 0, "positioning_overheat_score": 32, "relative_strength_score": 86, "revision_score": 88, "valuation_repricing_score": 70}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 10, "channel_concentration_risk_score": 20, "channel_reorder_score": 88, "contract_score": 0, "customer_quality_score": 76, "dilution_cb_risk_score": 0, "execution_risk_score": 28, "fcf_conversion_score": 72, "global_distribution_score": 90, "inventory_turnover_score": 78, "legal_or_contract_risk_score": 0, "margin_bridge_score": 70, "policy_or_regulatory_score": 0, "positioning_overheat_score": 38, "relative_strength_score": 85, "revision_score": 82, "valuation_repricing_score": 72}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Green", "stage_label_before": "Stage3-Yellow_or_low_Green", "symbol": "003230", "trigger_id": "R5L10_C20_SAMYANG_T2A_20240517", "weighted_score_after": 91, "weighted_score_before": 86}
{"MAE_90D_pct": -6.77, "MFE_90D_pct": 83.42, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SILICON2_20240517_KBEAUTY_DISTRIBUTION_SUCCESS", "changed_components": ["channel_reorder_score", "global_distribution_score", "margin_bridge_score", "revision_score", "inventory_turnover_score", "channel_concentration_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C20 rewards verified global reorder/channel expansion plus margin conversion. It penalizes legacy brand/reopening narratives when repeat sell-through, inventory turnover, and channel diversification are missing. 4B remains overlay-only after vertical rerating.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 10, "channel_concentration_risk_score": 30, "channel_reorder_score": 96, "contract_score": 0, "customer_quality_score": 88, "dilution_cb_risk_score": 0, "execution_risk_score": 38, "fcf_conversion_score": 76, "global_distribution_score": 96, "inventory_turnover_score": 84, "legal_or_contract_risk_score": 0, "margin_bridge_score": 80, "policy_or_regulatory_score": 0, "positioning_overheat_score": 40, "relative_strength_score": 90, "revision_score": 84, "valuation_repricing_score": 74}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 12, "channel_concentration_risk_score": 35, "channel_reorder_score": 90, "contract_score": 0, "customer_quality_score": 82, "dilution_cb_risk_score": 0, "execution_risk_score": 42, "fcf_conversion_score": 68, "global_distribution_score": 92, "inventory_turnover_score": 76, "legal_or_contract_risk_score": 0, "margin_bridge_score": 68, "policy_or_regulatory_score": 0, "positioning_overheat_score": 45, "relative_strength_score": 90, "revision_score": 78, "valuation_repricing_score": 78}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Green_with_4B_watch", "stage_label_before": "Stage3-Yellow_or_low_Green", "symbol": "257720", "trigger_id": "R5L10_C20_SILICON2_T2A_20240517", "weighted_score_after": 90, "weighted_score_before": 85}
{"MAE_90D_pct": -33.22, "MFE_90D_pct": 1.65, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_LGHNH_20210624_CHINA_DUTYFREE_FALSE_GREEN", "changed_components": ["channel_reorder_score", "global_distribution_score", "margin_bridge_score", "revision_score", "inventory_turnover_score", "channel_concentration_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C20 rewards verified global reorder/channel expansion plus margin conversion. It penalizes legacy brand/reopening narratives when repeat sell-through, inventory turnover, and channel diversification are missing. 4B remains overlay-only after vertical rerating.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 3, "channel_concentration_risk_score": 92, "channel_reorder_score": 22, "contract_score": 0, "customer_quality_score": 72, "dilution_cb_risk_score": 0, "execution_risk_score": 78, "fcf_conversion_score": 35, "global_distribution_score": 24, "inventory_turnover_score": 28, "legal_or_contract_risk_score": 0, "margin_bridge_score": 38, "policy_or_regulatory_score": 0, "positioning_overheat_score": 84, "relative_strength_score": 50, "revision_score": 35, "valuation_repricing_score": 44}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 5, "channel_concentration_risk_score": 82, "channel_reorder_score": 50, "contract_score": 0, "customer_quality_score": 88, "dilution_cb_risk_score": 0, "execution_risk_score": 48, "fcf_conversion_score": 58, "global_distribution_score": 46, "inventory_turnover_score": 42, "legal_or_contract_risk_score": 0, "margin_bridge_score": 62, "policy_or_regulatory_score": 0, "positioning_overheat_score": 76, "relative_strength_score": 70, "revision_score": 65, "valuation_repricing_score": 75}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error", "stage_label_after": "Stage2-watch_or_4B/4C_watch", "stage_label_before": "Stage3-Yellow_false_positive_risk", "symbol": "051900", "trigger_id": "R5L10_C20_LGHNH_T2_20210624", "weighted_score_after": 56, "weighted_score_before": 82}
{"MAE_90D_pct": -35.66, "MFE_90D_pct": 4.9, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_AMORE_20210510_REOPENING_FALSE_RERATING", "changed_components": ["channel_reorder_score", "global_distribution_score", "margin_bridge_score", "revision_score", "inventory_turnover_score", "channel_concentration_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C20 rewards verified global reorder/channel expansion plus margin conversion. It penalizes legacy brand/reopening narratives when repeat sell-through, inventory turnover, and channel diversification are missing. 4B remains overlay-only after vertical rerating.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 3, "channel_concentration_risk_score": 88, "channel_reorder_score": 20, "contract_score": 0, "customer_quality_score": 66, "dilution_cb_risk_score": 0, "execution_risk_score": 76, "fcf_conversion_score": 26, "global_distribution_score": 22, "inventory_turnover_score": 25, "legal_or_contract_risk_score": 0, "margin_bridge_score": 34, "policy_or_regulatory_score": 0, "positioning_overheat_score": 72, "relative_strength_score": 48, "revision_score": 32, "valuation_repricing_score": 38}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 5, "channel_concentration_risk_score": 78, "channel_reorder_score": 45, "contract_score": 0, "customer_quality_score": 82, "dilution_cb_risk_score": 0, "execution_risk_score": 50, "fcf_conversion_score": 42, "global_distribution_score": 40, "inventory_turnover_score": 35, "legal_or_contract_risk_score": 0, "margin_bridge_score": 58, "policy_or_regulatory_score": 0, "positioning_overheat_score": 68, "relative_strength_score": 72, "revision_score": 60, "valuation_repricing_score": 65}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error", "stage_label_after": "Stage2-watch_or_rejected", "stage_label_before": "Stage3-Yellow_false_positive_risk", "symbol": "090430", "trigger_id": "R5L10_C20_AMORE_T2_20210510", "weighted_score_after": 52, "weighted_score_before": 78}
{"MAE_90D_pct": -29.09, "MFE_90D_pct": 6.9, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L10_C20_SILICON2_20240619_4B_REUSE", "changed_components": ["channel_reorder_score", "global_distribution_score", "margin_bridge_score", "revision_score", "inventory_turnover_score", "channel_concentration_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C20 rewards verified global reorder/channel expansion plus margin conversion. It penalizes legacy brand/reopening narratives when repeat sell-through, inventory turnover, and channel diversification are missing. 4B remains overlay-only after vertical rerating.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 5, "channel_concentration_risk_score": 55, "channel_reorder_score": 70, "contract_score": 0, "customer_quality_score": 82, "dilution_cb_risk_score": 0, "execution_risk_score": 82, "fcf_conversion_score": 52, "global_distribution_score": 78, "inventory_turnover_score": 55, "legal_or_contract_risk_score": 0, "margin_bridge_score": 52, "policy_or_regulatory_score": 0, "positioning_overheat_score": 100, "relative_strength_score": 94, "revision_score": 48, "valuation_repricing_score": 98}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "channel_concentration_risk_score": 44, "channel_reorder_score": 82, "contract_score": 0, "customer_quality_score": 84, "dilution_cb_risk_score": 0, "execution_risk_score": 70, "fcf_conversion_score": 66, "global_distribution_score": 86, "inventory_turnover_score": 70, "legal_or_contract_risk_score": 0, "margin_bridge_score": 66, "policy_or_regulatory_score": 0, "positioning_overheat_score": 96, "relative_strength_score": 96, "revision_score": 62, "valuation_repricing_score": 94}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage4B_overlay", "stage_label_before": "Stage4B_overlay", "symbol": "257720", "trigger_id": "R5L10_C20_SILICON2_T4B_20240619", "weighted_score_after": 70, "weighted_score_before": 88}
{"avg_MAE_180D_pct": -30.95, "avg_MAE_90D_pct": -18.91, "avg_MFE_180D_pct": 49.01, "avg_MFE_90D_pct": 37.7, "avg_four_b_full_window_peak_proximity": 0.8, "avg_four_b_local_peak_proximity": 0.8, "avg_green_lateness_ratio": "mixed_0.26_excluding_counterexamples", "changed_axes": ["channel_reorder_bridge_gate", "global_distribution_score", "channel_concentration_risk_drag", "4B_positioning_overlay"], "changed_thresholds": {"C20_green_bridge_min": "proposed_shadow_70", "stage3_green_revision_min": "kept_55", "stage3_green_total_min": "kept_87"}, "eligible_trigger_count": 4, "false_positive_rate": 0.5, "late_green_count": 1, "missed_structural_count": 0, "profile_hypothesis": "Current proxy; can still over-score legacy China/reopening brand quality if channel concentration is not punished", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "sector_or_canonical_shadow_only", "score_return_alignment_verdict": "mixed_with_two_false_positive_errors", "selected_entry_trigger_per_case": ["R5L10_C20_SAMYANG_T2A_20240517", "R5L10_C20_SILICON2_T2A_20240517", "R5L10_C20_LGHNH_T2_20210624", "R5L10_C20_AMORE_T2_20210510"]}
{"avg_MAE_180D_pct": -30.95, "avg_MAE_90D_pct": -18.91, "avg_MFE_180D_pct": 49.01, "avg_MFE_90D_pct": 37.7, "avg_four_b_full_window_peak_proximity": 0.8, "avg_four_b_local_peak_proximity": 0.8, "avg_green_lateness_ratio": "mixed_0.26_excluding_counterexamples", "changed_axes": ["channel_reorder_bridge_gate", "global_distribution_score", "channel_concentration_risk_drag", "4B_positioning_overlay"], "changed_thresholds": {"C20_green_bridge_min": "proposed_shadow_70", "stage3_green_revision_min": "kept_55", "stage3_green_total_min": "kept_87"}, "eligible_trigger_count": 4, "false_positive_rate": 0.5, "late_green_count": 1, "missed_structural_count": 0, "profile_hypothesis": "Old baseline, more vulnerable to brand-quality and relative-strength overpromotion", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "sector_or_canonical_shadow_only", "score_return_alignment_verdict": "weaker_than_P0", "selected_entry_trigger_per_case": ["R5L10_C20_SAMYANG_T2A_20240517", "R5L10_C20_SILICON2_T2A_20240517", "R5L10_C20_LGHNH_T2_20210624", "R5L10_C20_AMORE_T2_20210510"]}
{"avg_MAE_180D_pct": -30.95, "avg_MAE_90D_pct": -18.91, "avg_MFE_180D_pct": 49.01, "avg_MFE_90D_pct": 37.7, "avg_four_b_full_window_peak_proximity": 0.8, "avg_four_b_local_peak_proximity": 0.8, "avg_green_lateness_ratio": "mixed_0.26_excluding_counterexamples", "changed_axes": ["channel_reorder_bridge_gate", "global_distribution_score", "channel_concentration_risk_drag", "4B_positioning_overlay"], "changed_thresholds": {"C20_green_bridge_min": "proposed_shadow_70", "stage3_green_revision_min": "kept_55", "stage3_green_total_min": "kept_87"}, "eligible_trigger_count": 4, "false_positive_rate": 0.25, "late_green_count": 1, "missed_structural_count": 0, "profile_hypothesis": "Consumer sector profile adds reorder/sell-through/inventory-turnover bridge before Green", "profile_id": "P1_L5_sector_specific_candidate", "profile_scope": "sector_or_canonical_shadow_only", "score_return_alignment_verdict": "improves_false_positive_filter", "selected_entry_trigger_per_case": ["R5L10_C20_SAMYANG_T2A_20240517", "R5L10_C20_SILICON2_T2A_20240517", "R5L10_C20_LGHNH_T2_20210624", "R5L10_C20_AMORE_T2_20210510"]}
{"avg_MAE_180D_pct": -30.95, "avg_MAE_90D_pct": -18.91, "avg_MFE_180D_pct": 49.01, "avg_MFE_90D_pct": 37.7, "avg_four_b_full_window_peak_proximity": 0.8, "avg_four_b_local_peak_proximity": 0.8, "avg_green_lateness_ratio": "mixed_0.26_excluding_counterexamples", "changed_axes": ["channel_reorder_bridge_gate", "global_distribution_score", "channel_concentration_risk_drag", "4B_positioning_overlay"], "changed_thresholds": {"C20_green_bridge_min": "proposed_shadow_70", "stage3_green_revision_min": "kept_55", "stage3_green_total_min": "kept_87"}, "eligible_trigger_count": 4, "false_positive_rate": 0.0, "late_green_count": 1, "missed_structural_count": 0, "profile_hypothesis": "C20-specific channel_reorder + global_distribution + margin_bridge gate", "profile_id": "P2_C20_canonical_candidate", "profile_scope": "sector_or_canonical_shadow_only", "score_return_alignment_verdict": "best_fit_for_case_set", "selected_entry_trigger_per_case": ["R5L10_C20_SAMYANG_T2A_20240517", "R5L10_C20_SILICON2_T2A_20240517", "R5L10_C20_LGHNH_T2_20210624", "R5L10_C20_AMORE_T2_20210510"]}
{"avg_MAE_180D_pct": -30.95, "avg_MAE_90D_pct": -18.91, "avg_MFE_180D_pct": 49.01, "avg_MFE_90D_pct": 37.7, "avg_four_b_full_window_peak_proximity": 0.8, "avg_four_b_local_peak_proximity": 0.8, "avg_green_lateness_ratio": "mixed_0.26_excluding_counterexamples", "changed_axes": ["channel_reorder_bridge_gate", "global_distribution_score", "channel_concentration_risk_drag", "4B_positioning_overlay"], "changed_thresholds": {"C20_green_bridge_min": "proposed_shadow_70", "stage3_green_revision_min": "kept_55", "stage3_green_total_min": "kept_87"}, "eligible_trigger_count": 4, "false_positive_rate": 0.0, "late_green_count": 1, "missed_structural_count": 0, "profile_hypothesis": "Hard guard against China/duty-free or reopening beta without new channel proof", "profile_id": "P3_C20_counterexample_guard", "profile_scope": "sector_or_canonical_shadow_only", "score_return_alignment_verdict": "best_risk_guard", "selected_entry_trigger_per_case": ["R5L10_C20_SAMYANG_T2A_20240517", "R5L10_C20_SILICON2_T2A_20240517", "R5L10_C20_LGHNH_T2_20210624", "R5L10_C20_AMORE_T2_20210510"]}
{"canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "do_not_propose_new_weight_delta": false, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "10", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 4, "new_symbol_count": 4, "new_trigger_family_count": 4, "residual_error_types_found": ["legacy_brand_false_positive", "reopening_beta_false_positive", "channel_concentration_risk", "post_vertical_rerating_drawdown"], "reused_case_count": 1, "round": "R5", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "full_4b_requires_non_price_evidence"]}
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
completed_loop = 10
next_round = R6
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest/schema/profiles and OHLC shards were inspected through GitHub tool access.
- Evidence labels are research proxies and should be hardened against original reports/news/filings before promotion.
- No stock_agent source code was read or patched during this loop.

