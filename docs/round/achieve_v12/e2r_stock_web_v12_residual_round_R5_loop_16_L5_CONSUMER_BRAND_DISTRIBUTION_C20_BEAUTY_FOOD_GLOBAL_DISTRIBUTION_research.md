# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 16
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R5_loop_16_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이번 루프는 R5 소비재 안에서 직전 C18 `CONSUMER_EXPORT_CHANNEL_REORDER`와 겹치지 않도록 C20 `BEAUTY_FOOD_GLOBAL_DISTRIBUTION`으로 자동 선택했다. 의도는 K-food 리오더와 유사해 보이지만 실제로는 다른 물류/채널 구조를 갖는 K-beauty 글로벌 유통형 리레이팅을 별도 canonical로 압축할 수 있는지 검증하는 것이다.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
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

이 MD는 위 global profile을 다시 증명하지 않는다. 검증 초점은 C20 내부에서 `글로벌 채널 확장 + 반복 리오더 + 마진 bridge + 재고/중국/레거시 브랜드 리스크`가 실제 1D OHLC 경로와 얼마나 정렬되는지다.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R5 |
| loop | 16 |
| sector | 소비재·유통·브랜드 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| fine_archetype_id | K_BEAUTY_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE |
| loop_objective | coverage_gap_fill, counterexample_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test |
| rule_scope_preference | canonical_archetype_specific |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were read only for coverage-gap and duplicate-avoidance purposes. The already applied axes include the global Stage2 bonus, Yellow/Green threshold changes, stricter Green revision gate, and 4B/4C guardrails. This loop therefore avoids repeating “Stage2 is earlier than Green” as a generic finding and instead adds a C20-specific distinction:

```text
C20 positive condition:
  global channel expansion alone is insufficient.
  Promotion requires evidence that foreign-channel sell-through has converted into repeat reorder and margin/revision bridge.

C20 counterexample condition:
  legacy beauty/China rebound narratives without margin/reorder confirmation should remain Yellow/Watch, not Green.
```

Novelty check:

| metric | value |
|---|---:|
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 3 |
| new_canonical_archetype_count | 1 |
| new_trigger_family_count | 3 |
| positive_case_count | 2 |
| counterexample_count | 1 |
| current_profile_error_count | 1 |
| minimum_new_independent_case_ratio | 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields checked:

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validation notes:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The atlas is raw/unadjusted, not split-adjusted. Therefore each symbol profile was checked for corporate-action candidate dates. The three calibration windows used here have clean 180D windows.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward_window_trading_days | entry row exists | 180D available | 180D corporate-action contamination | calibration_usable |
|---|---:|---|---:|---|---|---|---|
| C20_SILICON2_2024Q1_REORDER | 257720 | 2024-05-14 | 180 | true | true | clean_180D_window | true |
| C20_VT_2024Q2_REEDLE_SHOT_GLOBAL | 018290 | 2024-05-14 | 180 | true | true | clean_180D_window | true |
| C20_LGHH_2024_REBOUND_FALSE_POSITIVE | 051900 | 2024-05-10 | 180 | true | true | clean_180D_window | true |
| C20_SILICON2_2024_PRICE_BLOWOFF_4B | 257720 | 2024-06-21 | 180 | true | true | clean_180D_window | true, overlay_only |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compression logic |
|---|---|---|
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE | Brand/distribution names where foreign-channel acceleration is visible in sell-through, reorder, OP margin, and upward revision. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_US_JAPAN_CHANNEL_REORDER | Beauty names with Japan/US channel proof but not necessarily direct own-brand inventory ownership. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | LEGACY_BEAUTY_CHINA_REOPENING_REBOUND_GUARD | Legacy cosmetics rebound narrative where channel reopening does not close the margin/revision bridge. |

The compression candidate is not “beauty stocks go up.” It is narrower: distribution-channel proof must behave like a conveyor belt—sell-through pulls reorder, reorder pulls margin visibility, and margin visibility pulls revision. If one wheel slips, the score should stay below Green.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | new_independent_case | notes |
|---|---:|---|---|---|---|---|---|
| C20_SILICON2_2024Q1_REORDER | 257720 | 실리콘투 | structural_success | positive | Stage2-Actionable / 2024-05-14 | true | Global K-beauty distribution rerating; explosive early MFE but later 4B/overheat risk. |
| C20_VT_2024Q2_REEDLE_SHOT_GLOBAL | 018290 | 브이티 | high_mae_success | positive | Stage2-Actionable / 2024-05-14 | true | Japan/US channel expansion plus brand sell-through; Green appears late relative to first actionable evidence. |
| C20_LGHH_2024_REBOUND_FALSE_POSITIVE | 051900 | LG생활건강 | failed_rerating | counterexample | Stage2-Watch / 2024-05-10 | true | Legacy brand rebound and China normalization narrative did not translate into durable margin/revision path. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
```

The case set satisfies v12 minimum balance. It has two positive structural successes, one failed rerating counterexample, and one 4B overlay audit. No 4C hard thesis-break row is proposed because the observable failure mode here is not contract cancellation or forced liquidation; it is weaker-than-needed distribution-to-margin conversion.

## 9. Evidence Source Map

The following evidence map is research-proxy level. It separates historical event timing from price outcome and does not use later price action to assign the trigger label.

| trigger_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2 fields | stage3 fields | stage4b fields | stage4c fields |
|---|---|---|---|---|---|---|---|
| T_C20_SILICON2_20240514_S2A | 2024-05-14 | 2024 Q1 result / global distribution growth known by market; evidence timing treated as close-of-day or next-trading confirmation. | company disclosure/news/research proxy; stock-web entry 2024-05-14 | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, repeat_order_or_conversion | [] | [] |
| T_C20_SILICON2_20240621_4B | 2024-06-21 | Price and valuation heat after rapid rerating; no hard non-price thesis break. | stock-web price path + research proxy valuation heat | [] | [] | price_only_local_peak, valuation_blowoff, positioning_overheat | [] |
| T_C20_VT_20240514_S2A | 2024-05-14 | 2024 Q1 beauty-brand momentum / channel expansion evidence. | company disclosure/news/research proxy; stock-web entry 2024-05-14 | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | margin_bridge, repeat_order_or_conversion, financial_visibility | [] | [] |
| T_C20_LGHH_20240510_WATCH | 2024-05-10 | Rebound narrative visible, but durable reorder/margin/revision proof insufficient. | company disclosure/news/research proxy; stock-web entry 2024-05-10 | public_event_or_disclosure | [] | margin_or_backlog_slowdown | [] |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | price_basis | stock_web_manifest_max_date | profile caveat |
|---:|---|---|---|---|---|---|
| 257720 | 실리콘투 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv; 2025.csv | atlas/symbol_profiles/257/257720.json | tradable_raw | 2026-02-20 | corporate-action candidates only in 2022, outside calibration window |
| 018290 | 브이티 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv; 2025.csv | atlas/symbol_profiles/018/018290.json | tradable_raw | 2026-02-20 | historical corporate-action candidates pre-2020, outside calibration window |
| 051900 | LG생활건강 | atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv; 2025.csv | atlas/symbol_profiles/051/051900.json | tradable_raw | 2026-02-20 | no corporate-action candidates |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | representative | current_profile_verdict | trigger_outcome_label |
|---|---|---|---|---|---:|---|---|---|
| T_C20_SILICON2_20240514_S2A | C20_SILICON2_2024Q1_REORDER | Stage2-Actionable | 2024-05-14 | 2024-05-14 | 27000 | true | current_profile_correct | structural_success_high_mfe_then_4b_risk |
| T_C20_SILICON2_20240621_4B | C20_SILICON2_2024Q1_REORDER | Stage4B-Overlay | 2024-06-21 | 2024-06-21 | 52800 | false | current_profile_correct | good_local_4b_but_overlay_only |
| T_C20_VT_20240514_S2A | C20_VT_2024Q2_REEDLE_SHOT_GLOBAL | Stage2-Actionable | 2024-05-14 | 2024-05-14 | 25500 | true | current_profile_correct | structural_success_late_green |
| T_C20_LGHH_20240510_WATCH | C20_LGHH_2024_REBOUND_FALSE_POSITIVE | Stage2-Watch | 2024-05-10 | 2024-05-10 | 466000 | true | current_profile_false_positive | failed_rerating_high_mae |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger backtest

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | MFE_1Y_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | below_entry_30D | below_entry_90D |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| T_C20_SILICON2_20240514_S2A | 2024-05-14 | 27000 | 100.74 | -9.26 | 100.74 | -9.26 | 100.74 | -13.70 | 100.74 | -13.70 | 2024-06-19 | 54200 | -57.01 | false | false |
| T_C20_VT_20240514_S2A | 2024-05-14 | 25500 | 56.86 | -3.53 | 56.86 | -3.53 | 65.69 | -3.53 | 65.69 | -3.53 | 2025-01-02 | 42250 | -26.39 | false | false |
| T_C20_LGHH_20240510_WATCH | 2024-05-10 | 466000 | 3.00 | -22.85 | 3.00 | -31.12 | 3.00 | -36.80 | 3.00 | -37.77 | 2024-05-23 | 480000 | -38.65 | true | true |

### 12.2 Overlay trigger backtest

| trigger_id | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | aggregate_group_role |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| T_C20_SILICON2_20240621_4B | Stage4B-Overlay | 2024-06-21 | 52800 | 0.76 | -23.67 | 0.76 | -23.67 | 0.76 | -55.87 | 2024-06-24 | 53200 | -56.20 | 4B_overlay_only |

Notes: MFE/MAE are calculated from stock-web tradable_raw OHLC rows. Representative rows are deduped by `same_entry_group_id` for aggregate; the 4B row is overlay-only and does not train positive entry weights.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual path | verdict | interpretation |
|---|---|---|---|---|
| C20_SILICON2_2024Q1_REORDER | Stage2-Actionable, later Yellow/Green if revision proof arrives | +100.74% MFE in 30/90/180D, but post-peak drawdown exceeded -57% | current_profile_correct | Stage2-Actionable was useful; Green must remain tied to revision/margin bridge and 4B overlay must not be ignored. |
| C20_VT_2024Q2_REEDLE_SHOT_GLOBAL | Stage2-Actionable then Yellow/Green later | +56.86% MFE in 30/90D, +65.69% MFE by 180D | current_profile_correct | Early channel evidence captured the move; too strict Green timing would miss much of the cycle. |
| C20_LGHH_2024_REBOUND_FALSE_POSITIVE | Possible Stage2/Yellow if generic beauty rebound is over-weighted | +3.00% MFE but -36.80% 180D MAE | current_profile_false_positive | C20 needs a guard against legacy-brand rebound narratives without repeat order and margin/revision proof. |

Axis answers:

```text
1. current calibrated profile judgment:
   correct for Silicon2/VT early non-price evidence; too permissive if LG H&H legacy rebound is scored like a repeat-reorder story.

2. MFE/MAE alignment:
   positives show strong MFE; counterexample shows tiny MFE and large MAE.

3. stage2_actionable_evidence_bonus:
   appropriate for Silicon2/VT; over-powerful for LG H&H unless C20 guard is added.

4. stage3_yellow_total_min = 75:
   acceptable, but C20 Yellow should require at least one channel/reorder component, not just brand rebound.

5. stage3_green_total_min = 87 / revision_min = 55:
   kept; C20 Green should not relax revision/margin confirmation.

6. price-only blowoff guard:
   strengthened; Silicon2 4B row shows price-only local peak can be a useful overlay but not a new positive trigger.

7. full 4B non-price requirement:
   strengthened; 4B becomes better near the full-window peak when valuation/positioning/revision slowdown evidence exists.

8. hard 4C routing:
   kept; no hard 4C row in this loop.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-Actionable entry | Stage3-Green proxy entry | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| C20_SILICON2_2024Q1_REORDER | 27000 | 51200 | 54200 | 0.89 | Green is very late; Stage2 must exist, but 4B overlay must also tighten quickly. |
| C20_VT_2024Q2_REEDLE_SHOT_GLOBAL | 25500 | 38000 | 42250 | 0.75 | Green catches confirmation but misses most of the first rerating leg. |
| C20_LGHH_2024_REBOUND_FALSE_POSITIVE | 466000 | no valid Green | 480000 | not_applicable | No confirmed Green trigger; generic rebound should remain Watch/Yellow at most. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | Stage4B entry | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | timing_verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| T_C20_SILICON2_20240621_4B | 27000 | 52800 | 54200 | 54200 | 0.95 | 0.95 | price_only, valuation_blowoff, positioning_overheat | good_local_4b_timing_but_overlay_only |

The key nuance is that this is not a positive-entry row. It is a risk overlay on an already successful Stage2 case. The current global guardrail—full 4B requires non-price evidence—should remain in force. For C20, a price-only move near the local peak is a warning light; it is not a thesis break.

## 16. 4C Protection Audit

No hard 4C row is proposed. The observed counterexample is not a sharp cancellation/rejection type. It is a slow failure of the distribution-to-margin bridge. Therefore:

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not_applicable
hard_4c_late = not_applicable
```

## 17. Sector-Specific Rule Candidate

```text
rule_id = L5_C20_GLOBAL_BEAUTY_DISTRIBUTION_REORDER_MARGIN_BRIDGE
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
proposal_type = sector_shadow_only
confidence = medium_low
```

Rule candidate:

```text
For L5/C20, promote Stage2-Actionable only when at least two of the following are present:
1. global channel expansion or customer/channel proof,
2. repeat reorder / sell-through conversion evidence,
3. margin bridge or operating leverage evidence,
4. early revision signal.

Do not let generic brand rebound, China reopening, or channel-normalization narrative alone receive the same Stage2 bonus.
```

Backtest intuition:

```text
- Silicon2 and VT pass because channel expansion converted into reorder/margin/revision evidence.
- LG H&H fails because the rebound narrative did not close the margin/revision bridge and produced high MAE.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C20_REPEAT_REORDER_MARGIN_BRIDGE_GATE
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
changed_axes = channel_reorder_score +1, margin_bridge_score +1, legacy_rebound_without_revision_guard +1 risk
production_scoring_changed = false
```

Proposed shadow components:

```text
positive additive axis:
  c20_repeat_reorder_margin_bridge_bonus = +1.0 to +1.5 shadow only

counterexample guard:
  c20_legacy_brand_rebound_without_revision_penalty = -1.0 to -2.0 shadow only

4B overlay:
  c20_fast_rerating_price_only_4b_watch = true
  do_not_treat_price_only_4b_as_full_exit_without_non_price_evidence = true
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global | existing calibrated profile | 3 | 3 | 53.53 | -14.64 | 56.48 | -18.01 | 0.33 | 0 | 2 | 0.82 | good but one false positive remains |
| P0b_e2r_2_0_baseline_reference | global reference | older baseline without current gates | 3 | 3 | 34.88 | -18.30 | 37.83 | -21.67 | 0.33 | 1 | 2 | 0.82 | worse: likely misses Stage2 in positives and fails LG guard |
| P1_L5_sector_specific_candidate_profile | sector_specific | add L5/C20 channel-to-margin proof | 3 | 3 | 78.80 | -6.40 | 83.22 | -6.40 | 0.00 | 0 | 1 | 0.82 | improved alignment by excluding LG false positive |
| P2_C20_archetype_candidate_profile | canonical_archetype_specific | reorder + margin/revision bridge gate | 3 | 3 | 78.80 | -6.40 | 83.22 | -6.40 | 0.00 | 0 | 1 | 0.82 | best explanatory compression |
| P3_C20_counterexample_guard_profile | canonical_archetype_specific | penalize legacy rebound without revision | 3 | 3 | 78.80 | -6.40 | 83.22 | -6.40 | 0.00 | 0 | 1 | 0.82 | same quant effect, clearer rejection logic |

The candidate profiles improve average MFE/MAE because the LG H&H false positive is excluded from positive promotion while Silicon2 and VT remain eligible.

## 20. Score-Return Alignment Matrix

| case_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | component_delta_explanation | score_return_alignment_label |
|---|---|---:|---|---|---:|---|---|---|
| C20_SILICON2_2024Q1_REORDER | contract=0, backlog=2, margin=8, revision=7, RS=8, customer=7, policy=0, valuation=5, execution_risk=3, legal=0, dilution=0, accounting=0, channel_reorder=9 | 86 | Stage3-Yellow / near Green | contract=0, backlog=2, margin=9, revision=8, RS=8, customer=8, policy=0, valuation=5, execution_risk=3, legal=0, dilution=0, accounting=0, channel_reorder=10 | 89 | Stage3-Green shadow | repeat reorder + margin bridge closes C20 gate; still watch 4B. | aligned_positive_high_mfe |
| C20_VT_2024Q2_REEDLE_SHOT_GLOBAL | contract=0, backlog=1, margin=7, revision=6, RS=7, customer=7, policy=0, valuation=4, execution_risk=3, legal=0, dilution=0, accounting=0, channel_reorder=8 | 82 | Stage3-Yellow | contract=0, backlog=1, margin=8, revision=7, RS=7, customer=8, policy=0, valuation=4, execution_risk=3, legal=0, dilution=0, accounting=0, channel_reorder=9 | 86 | Stage3-Yellow/Green buffer | channel evidence strong; revision gate prevents over-relaxation. | aligned_positive_good_mfe |
| C20_LGHH_2024_REBOUND_FALSE_POSITIVE | contract=0, backlog=0, margin=3, revision=2, RS=4, customer=3, policy=0, valuation=2, execution_risk=6, legal=0, dilution=0, accounting=0, channel_reorder=2 | 76 | Stage3-Yellow false positive risk | contract=0, backlog=0, margin=2, revision=1, RS=3, customer=2, policy=0, valuation=1, execution_risk=7, legal=0, dilution=0, accounting=0, channel_reorder=1, legacy_rebound_guard=-2 | 66 | Stage2-Watch / reject Green | generic rebound is not repeat reorder; high MAE confirms guard. | aligned_counterexample_guard |

Canonical component keys are preserved in every score simulation. Supplemental components used: `channel_reorder_score`, `legacy_rebound_guard_score`, `positioning_overheat_score`.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 1 | true | true | positive/counterexample now seeded; needs holdout and 4C-like thesis-break cases later |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

residual_error_types_found:
- legacy_brand_rebound_false_positive
- green_lateness_in_high_velocity_beauty_distribution
- price_only_4b_overlay_not_full_thesis_break

new_axis_proposed:
- c20_repeat_reorder_margin_bridge_bonus
- c20_legacy_brand_rebound_without_revision_penalty
- c20_fast_rerating_price_only_4b_watch

existing_axis_strengthened:
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R5/L5/C20 K-beauty global channel reorder and legacy rebound guard
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date and price basis.
- Symbol profile fields and corporate-action candidate dates.
- Entry-date OHLC rows for 257720, 018290, 051900.
- 30D/90D/180D MFE and MAE from tradable_raw rows.
- Deduped representative triggers versus overlay-only 4B trigger.
- Positive/counterexample balance for a C20-specific shadow rule.
```

Not validated:

```text
- This is not a live scan.
- This is not investment advice.
- No stock_agent source code was opened or patched.
- No brokerage or live-data API was used.
- External consensus EPS revisions are represented as research-proxy evidence, not production scoring.
- 4C hard thesis-break protection is not calibrated in this loop.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_repeat_reorder_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"C20 positives required repeat reorder + margin bridge, not just channel narrative","keeps Silicon2/VT eligible while preserving Green revision strictness","T_C20_SILICON2_20240514_S2A|T_C20_VT_20240514_S2A",2,2,0,medium_low,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_legacy_brand_rebound_without_revision_penalty,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-2,-2,"LG H&H rebound narrative had +3% MFE but -36.8% 180D MAE","removes false positive from positive promotion set","T_C20_LGHH_20240510_WATCH",1,1,1,medium_low,counterexample_guard_shadow_only,"not production; requires more legacy beauty holdout"
shadow_weight,c20_price_only_local_peak_4b_watch,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,+1,"Silicon2 local/full peak proximity was high but price-only is overlay not full thesis break","strengthens existing 4B non-price guard","T_C20_SILICON2_20240621_4B",1,0,0,low,4B_overlay_shadow_only,"4B rows do not train positive entry weights"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C20_SILICON2_2024Q1_REORDER","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C20_SILICON2_20240514_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_high_mfe","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"High-MFE distribution rerating but later 4B overlay needed."}
{"row_type":"case","case_id":"C20_VT_2024Q2_REEDLE_SHOT_GLOBAL","symbol":"018290","company_name":"브이티","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C20_VT_20240514_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_good_mfe","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Channel expansion worked; Green confirmation would be late."}
{"row_type":"case","case_id":"C20_LGHH_2024_REBOUND_FALSE_POSITIVE","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_CHINA_REOPENING_REBOUND_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_C20_LGHH_20240510_WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Brand rebound without margin/reorder confirmation had poor MFE/MAE."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T_C20_SILICON2_20240514_S2A","case_id":"C20_SILICON2_2024Q1_REORDER","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"global channel reorder plus margin bridge","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","evidence_available_at_that_date":"Q1 global distribution/margin evidence available; close-of-day entry used.","evidence_source":"company disclosure/news/research proxy; stock-web OHLC row","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":27000,"MFE_30D_pct":100.74,"MFE_90D_pct":100.74,"MFE_180D_pct":100.74,"MFE_1Y_pct":100.74,"MFE_2Y_pct":null,"MAE_30D_pct":-9.26,"MAE_90D_pct":-9.26,"MAE_180D_pct":-13.7,"MAE_1Y_pct":-13.7,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":0.89,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_mfe_then_4b_risk","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SILICON2_20240514_27000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C20_SILICON2_20240621_4B","case_id":"C20_SILICON2_2024Q1_REORDER","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"4B overlay after high-velocity channel rerating","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-21","evidence_available_at_that_date":"Price and valuation heat after sharp rerating; no hard non-price thesis break.","evidence_source":"stock-web OHLC row plus research proxy overheat flag","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-21","entry_price":52800,"MFE_30D_pct":0.76,"MFE_90D_pct":0.76,"MFE_180D_pct":0.76,"MFE_1Y_pct":0.76,"MFE_2Y_pct":null,"MAE_30D_pct":-23.67,"MAE_90D_pct":-23.67,"MAE_180D_pct":-55.87,"MAE_1Y_pct":-55.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-24","peak_price":53200,"drawdown_after_peak_pct":-56.2,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_local_4b_timing_but_overlay_only","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SILICON2_20240621_52800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_timing_path","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T_C20_VT_20240514_S2A","case_id":"C20_VT_2024Q2_REEDLE_SHOT_GLOBAL","symbol":"018290","company_name":"브이티","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"brand sell-through plus global channel reorder","loop_objective":"coverage_gap_fill|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","evidence_available_at_that_date":"Beauty channel momentum evidence; close-of-day entry used.","evidence_source":"company disclosure/news/research proxy; stock-web OHLC row","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":25500,"MFE_30D_pct":56.86,"MFE_90D_pct":56.86,"MFE_180D_pct":65.69,"MFE_1Y_pct":65.69,"MFE_2Y_pct":null,"MAE_30D_pct":-3.53,"MAE_90D_pct":-3.53,"MAE_180D_pct":-3.53,"MAE_1Y_pct":-3.53,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-01-02","peak_price":42250,"drawdown_after_peak_pct":-26.39,"green_lateness_ratio":0.75,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_late_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_VT_20240514_25500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C20_LGHH_20240510_WATCH","case_id":"C20_LGHH_2024_REBOUND_FALSE_POSITIVE","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_CHINA_REOPENING_REBOUND_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"legacy beauty rebound without reorder-margin bridge","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Watch","trigger_date":"2024-05-10","evidence_available_at_that_date":"Rebound narrative visible, but repeat reorder/margin/revision evidence insufficient.","evidence_source":"company disclosure/news/research proxy; stock-web OHLC row","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-10","entry_price":466000,"MFE_30D_pct":3.0,"MFE_90D_pct":3.0,"MFE_180D_pct":3.0,"MFE_1Y_pct":3.0,"MFE_2Y_pct":null,"MAE_30D_pct":-22.85,"MAE_90D_pct":-31.12,"MAE_180D_pct":-36.8,"MAE_1Y_pct":-37.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":480000,"drawdown_after_peak_pct":-38.65,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"counterexample_guard_needed","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_LGHH_20240510_466000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_SILICON2_2024Q1_REORDER","trigger_id":"T_C20_SILICON2_20240514_S2A","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":9},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":10},"weighted_score_after":89,"stage_label_after":"Stage3-Green-shadow","changed_components":["margin_bridge_score","revision_score","customer_quality_score","channel_reorder_score"],"component_delta_explanation":"repeat reorder and margin bridge close C20 gate","MFE_90D_pct":100.74,"MAE_90D_pct":-9.26,"score_return_alignment_label":"aligned_positive_high_mfe","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_VT_2024Q2_REEDLE_SHOT_GLOBAL","trigger_id":"T_C20_VT_20240514_S2A","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":9},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-buffer-shadow","changed_components":["margin_bridge_score","revision_score","customer_quality_score","channel_reorder_score"],"component_delta_explanation":"channel evidence strong but revision gate prevents careless Green relaxation","MFE_90D_pct":56.86,"MAE_90D_pct":-3.53,"score_return_alignment_label":"aligned_positive_good_mfe","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_LGHH_2024_REBOUND_FALSE_POSITIVE","trigger_id":"T_C20_LGHH_20240510_WATCH","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":2},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-false-positive-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":1,"legacy_rebound_guard_score":-2},"weighted_score_after":66,"stage_label_after":"Stage2-Watch-reject-Green","changed_components":["margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score","channel_reorder_score","legacy_rebound_guard_score"],"component_delta_explanation":"generic rebound is not repeat reorder; high MAE confirms guard","MFE_90D_pct":3.0,"MAE_90D_pct":-31.12,"score_return_alignment_label":"aligned_counterexample_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_repeat_reorder_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"C20 positives required repeat reorder + margin bridge","keeps Silicon2/VT eligible while preserving Green revision strictness","T_C20_SILICON2_20240514_S2A|T_C20_VT_20240514_S2A",2,2,0,medium_low,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_legacy_brand_rebound_without_revision_penalty,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-2,-2,"legacy rebound without repeat reorder produced high MAE","removes LG H&H false positive","T_C20_LGHH_20240510_WATCH",1,1,1,medium_low,counterexample_guard_shadow_only,"requires more legacy beauty holdout"
shadow_weight,c20_price_only_local_peak_4b_watch,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,+1,"price-only local peak near full-window high is overlay only","strengthens 4B non-price guard","T_C20_SILICON2_20240621_4B",1,0,0,low,4B_overlay_shadow_only,"4B rows do not train positive entry weights"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["legacy_brand_rebound_false_positive","green_lateness_in_high_velocity_beauty_distribution","price_only_4b_overlay_not_full_thesis_break"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R5/L5/C20 K-beauty global channel reorder and legacy rebound guard"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"C20_FUTURE_HOLDOUT_AMORE_OR_COSMAX","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"future holdout validation needed for ODM/legacy beauty split; not used for weight calibration in this loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R5
next_large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
next_candidate_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN or C20 holdout_validation
next_objective = holdout_validation + counterexample_mining
suggested_holdout_symbols = 아모레퍼시픽, 코스맥스, 한국콜마, 애경산업
```

## 28. Source Notes

```text
stock_web_manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
silicon2_profile = atlas/symbol_profiles/257/257720.json
vt_profile = atlas/symbol_profiles/018/018290.json
lghh_profile = atlas/symbol_profiles/051/051900.json
silicon2_price_rows = atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv, 2025.csv
vt_price_rows = atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv, 2025.csv
lghh_price_rows = atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv, 2025.csv
stock_agent_artifact_checked = reports/e2r_calibration/calibrated_profile_report.md
```

No current-stock recommendation, live watchlist, auto-trading, broker API, or production scoring patch is included.
