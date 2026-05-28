# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 16
completed_round: R5
completed_loop: 16
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT
output_file: e2r_stock_web_v12_residual_round_R5_loop_16_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
live_candidate_mode: false
current_stock_discovery_allowed: false
```

This loop adds **4** new independent cases, **2** counterexamples, and **3** residual errors for `R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are treated as baseline: Stage2 actionable evidence bonus, Yellow 75, Green 87, Green revision minimum 55, cross-evidence Green buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing.

This file does **not** re-propose those global axes. It stress-tests them inside R5/C20 where a cosmetic brand or ODM can move for two different reasons: verified global reorder/margin conversion, or shallow roadshop/reopening/theme beta.

## 2. Round / Large Sector / Canonical Archetype Scope

- `scheduled_round`: `R5`
- `scheduled_loop`: `16`
- `large_sector_id`: `L5_CONSUMER_BRAND_DISTRIBUTION`
- `canonical_archetype_id`: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`
- `fine_archetype_id`: `K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT`
- `loop_objective`: `coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test`

R5 maps directly to L5, so the round-sector consistency gate passes. The selected canonical archetype remains consumer/brand/distribution and does not drift into R13 cross-archetype red-team work.

## 3. Previous Coverage / Duplicate Avoidance Check

Local round-state inspection shows R5 loop 15 already covered C19. The newly generated R4 loop 16 declared `next_round = R5`, `next_loop = 16`, so this file uses `R5/Loop 16`.

Prior R5 C20 files already used `003230`, `257720`, `051900`, `090430`, `018290`. This loop avoids those repeated representative rows and selects new C20 symbols: `192820`, `161890`, `237880`, `078520`, and `214420`. The fifth symbol is used as a same-loop 4B overlay only and is not counted as a representative new case.

Novelty gate:

```text
new_independent_case_count = 4
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
reused_case_count = 0
minimum_new_independent_case_ratio = 4 / 4 = 100%
```

The coverage gap selected here is the C20 distinction between **ODM/export reorder with margin conversion** and **roadshop/reopening/theme beta**. This is different from the earlier Silicon2/VT/LGHH/Amore loop, which focused on distributor platforms and China/duty-free reopening beta.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields checked:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

The manifest notes that the atlas is raw/unadjusted, excludes zero-volume and zero-OHLC rows from calibration shards, and blocks corporate-action-contaminated windows by default. The `max_date` is `2026-02-20`, and all selected 180D windows end before that boundary.

Symbol profile checks:

| symbol | company | profile_path | last_date | row/corporate-action status for selected window |
| --- | --- | --- | --- | --- |
| 192820 | 코스맥스 | `atlas/symbol_profiles/192/192820.json` | 2026-02-20 | clean; no corporate-action candidates |
| 161890 | 한국콜마 | `atlas/symbol_profiles/161/161890.json` | 2026-02-20 | clean; no corporate-action candidates |
| 237880 | 클리오 | `atlas/symbol_profiles/237/237880.json` | 2026-02-20 | clean; no corporate-action candidates |
| 078520 | 에이블씨엔씨 | `atlas/symbol_profiles/078/078520.json` | 2026-02-20 | clean; old candidates 2007-11-16 and 2018-01-09 outside test window |
| 214420 | 토니모리 | `atlas/symbol_profiles/214/214420.json` | 2026-02-20 | clean; old candidates 2016-12-09 and 2022-01-06 outside test window |

## 5. Historical Eligibility Gate

All four representative triggers pass:

- Trigger dates are historical.
- Entry dates exist in stock-web tradable shards.
- At least 180 forward trading days are available before manifest max date.
- OHLCV rows include high, low, close, and volume.
- 30D/90D/180D MFE and MAE were computed from stock-web raw/unadjusted tradable rows.
- Corporate-action candidate dates do not overlap selected 180D windows.

The `214420` row is 4B overlay-only. It is calibration-usable for risk overlay timing, but not included as a representative positive-stage entry.

## 6. Canonical Archetype Compression Map

C20 can sprawl into many labels: K-beauty, ODM, brand export, Amazon/TikTok, Japan drugstore, US suncare, roadshop recovery, and China/reopening. The compression rule is:

```text
real C20 rerating = reorder/sell-through evidence + margin bridge or revision conversion
weak C20 beta     = country/roadshop/theme/reopening price move without repeat conversion
```

A store sign can attract a crowd, but the calibration cares about the cash register. The share price can jump on foot traffic; the E2R stage should rise only when the receipt shows repeat purchase and margin conversion.

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE90/MAE90 | MFE180/MAE180 | current profile |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5L16_C20_COSMAX_20240513_ODM_EXPORT_MARGIN_BRIDGE | 192820 | 코스맥스 | high_mae_success | 2024-05-13 @ 157,700 | 31.9% / -26.4% | 31.9% / -26.4% | current_profile_correct |
| R5L16_C20_KOLMAR_20240510_US_SUNCARE_ODM_REORDER | 161890 | 한국콜마 | structural_success | 2024-05-10 @ 55,200 | 41.5% / -10.5% | 42.6% / -10.5% | current_profile_too_late |
| R5L16_C20_CLIO_20240513_BRAND_CHANNEL_SELLTHROUGH_REVERSAL | 237880 | 클리오 | 4C_late | 2024-05-13 @ 36,200 | 24.3% / -19.1% | 24.3% / -53.9% | current_profile_4C_too_late |
| R5L16_C20_ABLECNC_20240510_ROADSHOP_REOPENING_THEME_BETA | 078520 | 에이블씨엔씨 | price_moved_without_evidence | 2024-05-10 @ 8,040 | 46.5% / -19.2% | 46.5% / -19.2% | current_profile_false_positive |
| R5L16_C20_TONYMOLY_20240510_PRICE_ONLY_LOCAL_4B | 214420 | 토니모리 | 4B_overlay_success | 2024-06-14 @ 15,700 | 9.5% / -52.2% | 9.5% / -52.2% | current_profile_correct |

## 8. Positive vs Counterexample Balance

The two positive cases are ODM/export conversion cases. `코스맥스` and `한국콜마` were not simply K-beauty theme rows; their useful signal was the bridge from overseas order quality into margin/revision visibility.

The counterexamples are not “bad stocks” in a simple sense. `클리오`, `에이블씨엔씨`, and the `토니모리` overlay show that cosmetic-theme and roadshop-beta signals can create MFE, but they should not automatically become Stage3 without durable channel conversion. This is why this loop strengthens price-only and non-price 4B separation rather than weakening the global profile.

## 9. Evidence Source Map

| evidence family | positive evidence | counterexample evidence | scoring implication |
| --- | --- | --- | --- |
| ODM/export reorder | 코스맥스/한국콜마 had order-quality and margin bridge evidence | roadshop/theme rows had weaker repeat conversion | C20 positive stage should require channel conversion, not just brand/theme visibility |
| Margin bridge | positives converted channel demand into financial visibility | counterexamples had MFE but poor drawdown-adjusted durability | margin/revision should carry more C20 weight than price momentum |
| Relative strength | helpful as timing aid | dangerous when isolated | relative strength is a timing feature, not a thesis feature |
| 4B / 4C | vertical roadshop moves needed overlay discipline | delayed thesis-break watch produced avoidable MAE | keep full 4B non-price requirement; add C20-specific 4C-watch after conversion failure |

## 10. Price Data Source Map

| symbol | company | tradable shard | entry row anchor | profile |
| --- | --- | --- | --- | --- |
| 192820 | 코스맥스 | `atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv` | 2024-05-13 close 157,700 | `atlas/symbol_profiles/192/192820.json` |
| 161890 | 한국콜마 | `atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv` | 2024-05-10 close 55,200 | `atlas/symbol_profiles/161/161890.json` |
| 237880 | 클리오 | `atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv` | 2024-05-13 close 36,200 | `atlas/symbol_profiles/237/237880.json` |
| 078520 | 에이블씨엔씨 | `atlas/ohlcv_tradable_by_symbol_year/078/078520/2024.csv` | 2024-05-10 close 8,040 | `atlas/symbol_profiles/078/078520.json` |
| 214420 | 토니모리 | `atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv` | 2024-06-14 close 15,700 | `atlas/symbol_profiles/214/214420.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | current_profile | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R5L16_C20_COSMAX_T2A_20240513 | Stage2-Actionable | 2024-05-13 / 157,700 | 31.9% | -6.3% | 31.9% | -26.4% | 31.9% | -26.4% | 2024-06-14 / 208,000 | current_profile_correct | representative |
| R5L16_C20_KOLMAR_T2A_20240510 | Stage2-Actionable | 2024-05-10 / 55,200 | 35.9% | -10.5% | 41.5% | -10.5% | 42.6% | -10.5% | 2024-09-30 / 78,700 | current_profile_too_late | representative |
| R5L16_C20_CLIO_T2A_20240513 | Stage2-Actionable | 2024-05-13 / 36,200 | 24.3% | -6.1% | 24.3% | -19.1% | 24.3% | -53.9% | 2024-06-13 / 45,000 | current_profile_4C_too_late | representative |
| R5L16_C20_ABLECNC_T2_REJECT_20240510 | Stage2-candidate-rejected | 2024-05-10 / 8,040 | 46.5% | -9.1% | 46.5% | -19.2% | 46.5% | -19.2% | 2024-05-31 / 11,780 | current_profile_false_positive | representative |
| R5L16_C20_TONYMOLY_T4B_20240614 | Stage4B | 2024-06-14 / 15,700 | 9.5% | -32.8% | 9.5% | -52.2% | 9.5% | -52.2% | 2024-06-14 / 17,190 | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 코스맥스 — ODM/export success with painful high-MAE path

The 2024-05-13 entry closed at 157,700. The observed 30D/90D/180D peak was 208,000 on 2024-06-14, or +31.9% MFE. The same path then suffered a deep post-peak drawdown, with observed lows in the 116,000~121,000 area, so this is not a clean low-MAE momentum entry.

Interpretation: C20 should not reject high-MAE winners, but it should label them as Yellow unless reorder/margin confirmation is strong enough to absorb volatility.

### 12.2 한국콜마 — verified ODM/order-quality case where current profile is too late

The 2024-05-10 close was 55,200. The observed high reached 78,700 by 2024-09-30, giving +42.6% MFE over the 180D observed window. The useful residual is timing: the verified ODM/export channel could justify earlier C20 Yellow before generic Green confirmation.

Interpretation: C20 needs an ODM/export-margin bridge gate that can promote earlier than generic beauty-brand heuristics, but not all the way to Green without revision depth.

### 12.3 클리오 — tradeable channel signal, later thesis-break watch needed

The 2024-05-13 entry closed at 36,200 and reached 45,000 on 2024-06-13, a +24.3% MFE. But the later drawdown into the 16,000~18,000 range makes the residual clear: if sell-through and repeat-order evidence fails to persist after the first price peak, C20 should route to 4C-watch earlier.

### 12.4 에이블씨엔씨 — roadshop/theme beta creates MFE but should not promote to durable Stage3

The 2024-05-10 entry closed at 8,040 and reached 11,780 on 2024-05-31, +46.5% MFE. However, the subsequent low around 6,500 shows that the move should have been treated as a tradeable beta/overlay rather than a durable C20 rerating without margin/reorder proof.

### 12.5 토니모리 — 4B overlay-only row

The 2024-06-14 4B overlay closed at 15,700 after a vertical theme move. The high of 17,190 was local/full-window proximity, but the post-peak drawdown exceeded -50% in the observed window. This row should calibrate risk overlay timing, not positive-stage promotion.

## 13. Current Calibrated Profile Stress Test

| question | C20 loop-16 finding |
| --- | --- |
| How would current profile judge these? | It likely accepts ODM/export positives after financial visibility, but can still over-score roadshop/theme beta when price and relative strength are strong. |
| Did judgment match MFE/MAE? | Partially. MFE existed in all cases, but drawdown-adjusted alignment separates true ODM/export conversion from beta spikes. |
| Was Stage2 bonus too high/low? | Not globally. In C20, Stage2 bonus is too high for roadshop/theme beta but slightly too low for verified ODM/export channel conversion. |
| Was Yellow 75 too high/low? | Kept globally. C20 needs a gate, not a lower universal threshold. |
| Was Green 87/revision 55 too high/low? | Kept. Green should remain strict, especially after the CLIO and ABLECNC reversal paths. |
| Was price-only blowoff guard appropriate? | Yes, strengthened. Theme-beta spikes should stay overlay-only. |
| Was full 4B non-price requirement appropriate? | Yes. TONYMOLY confirms that price-only peaks are useful as local 4B-watch but need non-price context for full 4B. |
| Was hard 4C routing too late? | In CLIO, yes. C20 needs earlier 4C-watch when repeat conversion fails after an initial peak. |

## 14. Stage2 / Yellow / Green Comparison

C20 is a conversion chain, not a keyword bucket.

```text
positive C20 path:
ODM/export order quality -> repeat sell-through -> margin bridge -> revision visibility -> Stage3-Yellow/Green

false-positive C20 path:
roadshop/reopening/theme beta -> vertical price move -> no durable reorder proof -> drawdown -> 4B/4C-watch
```

The proposed adjustment does not lower the Green threshold. It inserts a C20 gate so that **what** moves the price matters as much as **how much** the price moves.

## 15. 4B Local vs Full-window Timing Audit

`토니모리` is the clearest 4B overlay row. Its 4B entry sits near the full observed cycle peak and later drawdown makes the overlay useful. `에이블씨엔씨` is more subtle: the peak was tradeable, but without non-price evidence it should be marked as price-beta watch rather than full positive stage.

```text
price-only local peak = useful risk watch
price-only local peak + absent channel conversion = no Green promotion
vertical move + valuation/positioning evidence = 4B overlay allowed
```

## 16. 4C Protection Audit

`클리오` supports an earlier 4C-watch label. The correct action is not hard 4C on the first pullback. It is a staged watch:

```text
if first C20 peak appears
and repeat-order / margin evidence fails to arrive
and price breaks below prior channel-confirmation zone:
    route to C20_4C_watch
```

This protects against late recognition while preserving hard 4C for explicit thesis break.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`, but the stronger proposal is canonical rather than broad R5.

R5-wide consumer cases vary too much: food export, apparel inventory, brand retail, cosmetics ODM, and roadshop beta behave differently. The loop therefore proposes only a weak sector rule:

```text
L5_channel_conversion_gate:
    positive stage in consumer distribution should require some conversion proof,
    not just brand recognition or geography/reopening words.
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

```text
C20_ODM_EXPORT_MARGIN_BRIDGE_GATE:
    if ODM/export reorder evidence + margin/revision conversion exists,
    allow Stage3-Yellow even if generic consumer profile is still waiting.

C20_ROADSHOP_THEME_BETA_GUARD:
    if evidence is only roadshop/reopening/theme beta + relative strength,
    cap at Stage2-Watch or 4B-watch until repeat conversion appears.

C20_FAST_4C_WATCH_AFTER_CHANNEL_REVERSAL:
    after first C20 price peak, if repeat-order/margin evidence fails,
    route to 4C-watch before hard thesis break.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| P0 / e2r_2_1_stock_web_calibrated_proxy | current | global calibrated profile as-is | none | 4 | COSMAX/KOLMAR/CLIO/ABLECNC | 36.0 | -18.8 | 36.3 | -27.5 | 50% | 1 | 1 | mixed: ODM winners survive, but roadshop/theme beta still risks false positive labels |
| P0b / e2r_2_0_baseline_reference | rollback | pre-calibrated baseline | lower guard pressure | 4 | same | 36.0 | -18.8 | 36.3 | -27.5 | 75% | 1 | 2 | worse: price-beta and reopening signals over-promote |
| P1 / L5_sector_specific_candidate | sector | R5 positive stage needs channel conversion, not brand/geography headline | L5_channel_conversion_gate | 3 | COSMAX/KOLMAR/CLIO | 32.6 | -18.7 | 32.6 | -30.3 | 33% | 0 | 1 | better, but still too broad for roadshop beta |
| P2 / C20_archetype_candidate | canonical | C20 ODM/export reorder plus margin bridge may promote; roadshop/theme beta capped | C20_ODM_export_margin_gate, C20_roadshop_theme_beta_guard | 2 | COSMAX/KOLMAR | 36.7 | -18.5 | 37.3 | -18.5 | 0% | 0 | 1 | best explanatory alignment |
| P3 / counterexample_guard_profile | guard | reject price-only cosmetic beta unless reorder/margin proof appears | C20_price_beta_4B_only_guard | 2 | CLIO/ABLECNC rejected or 4C-watch | 35.4 | -19.2 | 35.4 | -36.6 | 0% | 1 | 0 | protects against false positives while retaining watch labels |

## 20. Score-Return Alignment Matrix

| case | before label | after label | price result | alignment verdict |
| --- | --- | --- | --- | --- |
| 코스맥스 | Stage3-Yellow | Stage3-Yellow with high-MAE caution | +31.9% MFE / -26.4% MAE | aligned but volatile |
| 한국콜마 | Stage2-Actionable | Stage3-Yellow | +42.6% MFE / -10.5% MAE | improved; current profile too late |
| 클리오 | Stage3-Yellow false-positive risk | Stage2-Watch / 4C-watch | +24.3% MFE / -53.9% MAE | improved protection |
| 에이블씨엔씨 | Stage2-Actionable false-positive risk | Stage2-Watch-Rejected | +46.5% MFE / -19.2% MAE | better drawdown-adjusted guard |
| 토니모리 | Stage2/Yellow edge | 4B overlay only | +9.5% MFE / -52.2% MAE after 4B | risk overlay aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT | 2 | 2 | 1 | 2 | 4 | 0 | 5 | 4 | 3 | true | true | C20 now has ODM/export-vs-roadshop beta split; more food-export and non-China DTC holdouts remain |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: roadshop_theme_beta_false_positive, sellthrough_reversal_4c_late, verified_odm_export_yellow_too_late, price_only_local_4b_needed
new_axis_proposed: C20_ODM_EXPORT_MARGIN_BRIDGE_GATE, C20_ROADSHOP_THEME_BETA_GUARD, C20_FAST_4C_WATCH_AFTER_CHANNEL_REVERSAL
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- R5/Loop16 schedule and round-sector consistency.
- Stock-web manifest max date and raw/unadjusted price basis.
- Symbol profile availability and corporate-action window cleanliness.
- 2024 stock-web tradable OHLC entry rows and observed forward MFE/MAE paths.
- Positive/counterexample balance inside C20.
- C20-specific shadow rule candidates.

Not validated:

- Live 2026 candidate status.
- Any current recommendation or watchlist.
- Production scoring implementation.
- `stock_agent/src/e2r` code structure.
- Broker/API execution.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_ODM_EXPORT_MARGIN_BRIDGE_GATE,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,Promote only when ODM/export reorder is paired with margin or revision conversion,Retained COSMAX/KOLMAR but blocked roadshop/theme beta promotion,R5L16_C20_COSMAX_T2A_20240513|R5L16_C20_KOLMAR_T2A_20240510|R5L16_C20_CLIO_T2A_20240513|R5L16_C20_ABLECNC_T2_REJECT_20240510,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C20_ROADSHOP_THEME_BETA_GUARD,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,Roadshop/reopening/theme beta may create MFE but should not become Green without durable channel proof,Reduced false positive labels for ABLECNC and CLIO,R5L16_C20_CLIO_T2A_20240513|R5L16_C20_ABLECNC_T2_REJECT_20240510|R5L16_C20_TONYMOLY_T4B_20240614,3,2,2,medium,canonical_shadow_only,not production; overlay rows only calibrate risk
shadow_weight,C20_FAST_4C_WATCH_AFTER_CHANNEL_REVERSAL,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,If sell-through/channel evidence fails to repeat after first price peak route to 4C-watch earlier,Improved CLIO protection after June peak,R5L16_C20_CLIO_T2A_20240513,1,1,1,low,canonical_shadow_only,requires more holdout cases before production promotion
```

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "R5L16_C20_COSMAX_T2A_20240513", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_COSMAX_20240513_ODM_EXPORT_MARGIN_BRIDGE", "case_type": "high_mae_success", "company_name": "코스맥스", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "notes": "ODM/export order quality and margin bridge appeared before broad cosmetic beta fully settled; the price path rewarded the thesis but punished late confirmation after the June spike.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "high_mae_structural_success", "symbol": "192820"}
{"best_trigger": "R5L16_C20_KOLMAR_T2A_20240510", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_KOLMAR_20240510_US_SUNCARE_ODM_REORDER", "case_type": "structural_success", "company_name": "한국콜마", "current_profile_verdict": "current_profile_too_late", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "notes": "US/suncare and ODM channel conversion moved before the model would normally see enough revision confirmation; this is a C20 case where sell-through plus margin bridge should allow earlier Yellow.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "structural_success_green_late", "symbol": "161890"}
{"best_trigger": "R5L16_C20_CLIO_T2A_20240513", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_CLIO_20240513_BRAND_CHANNEL_SELLTHROUGH_REVERSAL", "case_type": "4C_late", "company_name": "클리오", "current_profile_verdict": "current_profile_4C_too_late", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "notes": "The early brand/channel signal was tradeable but did not sustain through the later margin/reorder confirmation window. C20 needs a faster thesis-break watch when repeat conversion fails after the first peak.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "sellthrough_watch_but_thesis_break_late", "symbol": "237880"}
{"best_trigger": "R5L16_C20_ABLECNC_T2_REJECT_20240510", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_ABLECNC_20240510_ROADSHOP_REOPENING_THEME_BETA", "case_type": "price_moved_without_evidence", "company_name": "에이블씨엔씨", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "notes": "Roadshop/reopening and cosmetic-theme beta generated MFE, but repeat-order and margin evidence were too weak to treat the move as a durable C20 rerating.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "price_beta_without_durable_channel_conversion", "symbol": "078520"}
{"best_trigger": "R5L16_C20_TONYMOLY_T4B_20240614", "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_TONYMOLY_20240510_PRICE_ONLY_LOCAL_4B", "case_type": "4B_overlay_success", "company_name": "토니모리", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "independent_evidence_weight": 0.0, "is_new_independent_case": false, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "notes": "This is not a positive-stage case. It is a risk overlay: after a vertical roadshop/theme move, valuation/positioning plus absent durable channel proof should mark 4B overlay rather than Green confirmation.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "overlay trigger for same-loop theme-beta 4B timing; not counted as representative new case", "round": "R5", "row_type": "case", "score_price_alignment": "good_4B_overlay_after_price_beta", "symbol": "214420"}
{"MAE_180D_pct": -26.4, "MAE_1Y_pct": null, "MAE_30D_pct": -6.3, "MAE_90D_pct": -26.4, "MFE_180D_pct": 31.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 31.9, "MFE_90D_pct": 31.9, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_COSMAX_20240513_ODM_EXPORT_MARGIN_BRIDGE", "company_name": "코스맥스", "corporate_action_window_status": "clean_180D_window; profile shows no corporate-action candidates", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.9, "entry_date": "2024-05-13", "entry_price": 157700, "evidence_available_at_that_date": "ODM/export order quality and margin bridge appeared before broad cosmetic beta fully settled; the price path rewarded the thesis but punished late confirmation after the June spike.", "evidence_source": "historical public earnings/channel evidence proxy; price rows from Songdaiki/stock-web", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "forward_window_trading_days": 180, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_c_protection_label": null, "green_lateness_ratio": 0.48, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "peak_date": "2024-06-14", "peak_price": 208000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "primary_archetype": "beauty_food_global_distribution", "profile_path": "atlas/symbol_profiles/192/192820.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "SEG_192820_2024-05-13", "sector": "consumer_brand_distribution", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "192820", "trigger_date": "2024-05-13", "trigger_id": "R5L16_C20_COSMAX_T2A_20240513", "trigger_outcome_label": "high_mae_structural_success", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -10.5, "MAE_1Y_pct": null, "MAE_30D_pct": -10.5, "MAE_90D_pct": -10.5, "MFE_180D_pct": 42.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 35.9, "MFE_90D_pct": 41.5, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_KOLMAR_20240510_US_SUNCARE_ODM_REORDER", "company_name": "한국콜마", "corporate_action_window_status": "clean_180D_window; profile shows no corporate-action candidates", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.0, "entry_date": "2024-05-10", "entry_price": 55200, "evidence_available_at_that_date": "US/suncare and ODM channel conversion moved before the model would normally see enough revision confirmation; this is a C20 case where sell-through plus margin bridge should allow earlier Yellow.", "evidence_source": "historical public earnings/channel evidence proxy; price rows from Songdaiki/stock-web", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "forward_window_trading_days": 180, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_c_protection_label": null, "green_lateness_ratio": 0.38, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "peak_date": "2024-09-30", "peak_price": 78700, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "primary_archetype": "beauty_food_global_distribution", "profile_path": "atlas/symbol_profiles/161/161890.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "SEG_161890_2024-05-10", "sector": "consumer_brand_distribution", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "161890", "trigger_date": "2024-05-10", "trigger_id": "R5L16_C20_KOLMAR_T2A_20240510", "trigger_outcome_label": "structural_success_green_late", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -53.9, "MAE_1Y_pct": null, "MAE_30D_pct": -6.1, "MAE_90D_pct": -19.1, "MFE_180D_pct": 24.3, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 24.3, "MFE_90D_pct": 24.3, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_CLIO_20240513_BRAND_CHANNEL_SELLTHROUGH_REVERSAL", "company_name": "클리오", "corporate_action_window_status": "clean_180D_window; profile shows no corporate-action candidates", "current_profile_verdict": "current_profile_4C_too_late", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -62.9, "entry_date": "2024-05-13", "entry_price": 36200, "evidence_available_at_that_date": "The early brand/channel signal was tradeable but did not sustain through the later margin/reorder confirmation window. C20 needs a faster thesis-break watch when repeat conversion fails after the first peak.", "evidence_source": "historical public earnings/channel evidence proxy; price rows from Songdaiki/stock-web", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "peak_date": "2024-06-13", "peak_price": 45000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "primary_archetype": "beauty_food_global_distribution", "profile_path": "atlas/symbol_profiles/237/237880.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "SEG_237880_2024-05-13", "sector": "consumer_brand_distribution", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["repeat_order_or_conversion"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "237880", "trigger_date": "2024-05-13", "trigger_id": "R5L16_C20_CLIO_T2A_20240513", "trigger_outcome_label": "sellthrough_watch_but_thesis_break_late", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -19.2, "MAE_1Y_pct": null, "MAE_30D_pct": -9.1, "MAE_90D_pct": -19.2, "MFE_180D_pct": 46.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 46.5, "MFE_90D_pct": 46.5, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_ABLECNC_20240510_ROADSHOP_REOPENING_THEME_BETA", "company_name": "에이블씨엔씨", "corporate_action_window_status": "clean_180D_window; profile has 2007-11-16 and 2018-01-09 candidates outside selected window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.8, "entry_date": "2024-05-10", "entry_price": 8040, "evidence_available_at_that_date": "Roadshop/reopening and cosmetic-theme beta generated MFE, but repeat-order and margin evidence were too weak to treat the move as a durable C20 rerating.", "evidence_source": "historical public earnings/channel evidence proxy; price rows from Songdaiki/stock-web", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "peak_date": "2024-05-31", "peak_price": 11780, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078520/2024.csv", "primary_archetype": "beauty_food_global_distribution", "profile_path": "atlas/symbol_profiles/078/078520.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "SEG_078520_2024-05-10", "sector": "consumer_brand_distribution", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "078520", "trigger_date": "2024-05-10", "trigger_id": "R5L16_C20_ABLECNC_T2_REJECT_20240510", "trigger_outcome_label": "price_beta_without_durable_channel_conversion", "trigger_type": "Stage2-candidate-rejected"}
{"MAE_180D_pct": -52.2, "MAE_1Y_pct": null, "MAE_30D_pct": -32.8, "MAE_90D_pct": -52.2, "MFE_180D_pct": 9.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 9.5, "MFE_90D_pct": 9.5, "aggregate_group_role": "4B_overlay_only", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_TONYMOLY_20240510_PRICE_ONLY_LOCAL_4B", "company_name": "토니모리", "corporate_action_window_status": "clean_180D_window; profile has 2016-12-09 and 2022-01-06 candidates outside selected window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": false, "do_not_count_as_new_case": true, "drawdown_after_peak_pct": -56.4, "entry_date": "2024-06-14", "entry_price": 15700, "evidence_available_at_that_date": "This is not a positive-stage case. It is a risk overlay: after a vertical roadshop/theme move, valuation/positioning plus absent durable channel proof should mark 4B overlay rather than Green confirmation.", "evidence_source": "historical public earnings/channel evidence proxy; price rows from Songdaiki/stock-web", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_EXPORT_ROADSHOP_BETA_SPLIT", "forward_window_trading_days": 180, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_b_full_window_peak_proximity": 1.0, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable", "independent_evidence_weight": 0.0, "is_new_independent_case": false, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "peak_date": "2024-06-14", "peak_price": 17190, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv", "primary_archetype": "beauty_food_global_distribution", "profile_path": "atlas/symbol_profiles/214/214420.json", "reuse_reason": "same-loop 4B overlay only; not counted in aggregate", "round": "R5", "row_type": "trigger", "same_entry_group_id": "SEG_214420_2024-06-14", "sector": "consumer_brand_distribution", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "214420", "trigger_date": "2024-06-14", "trigger_id": "R5L16_C20_TONYMOLY_T4B_20240614", "trigger_outcome_label": "good_4B_overlay_after_price_beta", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -26.4, "MFE_90D_pct": 31.9, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_COSMAX_20240513_ODM_EXPORT_MARGIN_BRIDGE", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "inventory_turn_score"], "component_delta_explanation": "C20 shadow profile separates ODM/export reorder and margin conversion from roadshop/reopening/theme beta; price-only spikes remain overlay-only.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 13, "contract_score": 0, "customer_quality_score": 15, "dilution_cb_risk_score": 0, "execution_risk_score": -6, "inventory_turn_score": 9, "legal_or_contract_risk_score": 0, "margin_bridge_score": 18, "policy_or_regulatory_score": 0, "relative_strength_score": 12, "revision_score": 17, "valuation_repricing_score": 9}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 11, "contract_score": 0, "customer_quality_score": 14, "dilution_cb_risk_score": 0, "execution_risk_score": -4, "inventory_turn_score": 8, "legal_or_contract_risk_score": 0, "margin_bridge_score": 15, "policy_or_regulatory_score": 0, "relative_strength_score": 13, "revision_score": 16, "valuation_repricing_score": 10}, "row_type": "score_simulation", "score_return_alignment_label": "high_mae_structural_success", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "192820", "trigger_id": "R5L16_C20_COSMAX_T2A_20240513", "weighted_score_after": 84, "weighted_score_before": 80}
{"MAE_90D_pct": -10.5, "MFE_90D_pct": 41.5, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_KOLMAR_20240510_US_SUNCARE_ODM_REORDER", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "inventory_turn_score"], "component_delta_explanation": "C20 shadow profile separates ODM/export reorder and margin conversion from roadshop/reopening/theme beta; price-only spikes remain overlay-only.", "current_profile_verdict": "current_profile_too_late", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 13, "contract_score": 0, "customer_quality_score": 15, "dilution_cb_risk_score": 0, "execution_risk_score": -4, "inventory_turn_score": 9, "legal_or_contract_risk_score": 0, "margin_bridge_score": 17, "policy_or_regulatory_score": 0, "relative_strength_score": 13, "revision_score": 16, "valuation_repricing_score": 8}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 10, "contract_score": 0, "customer_quality_score": 13, "dilution_cb_risk_score": 0, "execution_risk_score": -4, "inventory_turn_score": 7, "legal_or_contract_risk_score": 0, "margin_bridge_score": 13, "policy_or_regulatory_score": 0, "relative_strength_score": 14, "revision_score": 14, "valuation_repricing_score": 8}, "row_type": "score_simulation", "score_return_alignment_label": "structural_success_green_late", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage2-Actionable", "symbol": "161890", "trigger_id": "R5L16_C20_KOLMAR_T2A_20240510", "weighted_score_after": 81, "weighted_score_before": 74}
{"MAE_90D_pct": -19.1, "MFE_90D_pct": 24.3, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_CLIO_20240513_BRAND_CHANNEL_SELLTHROUGH_REVERSAL", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "inventory_turn_score"], "component_delta_explanation": "C20 shadow profile separates ODM/export reorder and margin conversion from roadshop/reopening/theme beta; price-only spikes remain overlay-only.", "current_profile_verdict": "current_profile_4C_too_late", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 4, "contract_score": 0, "customer_quality_score": 10, "dilution_cb_risk_score": 0, "execution_risk_score": -13, "inventory_turn_score": 2, "legal_or_contract_risk_score": 0, "margin_bridge_score": 6, "policy_or_regulatory_score": 0, "relative_strength_score": 8, "revision_score": 6, "valuation_repricing_score": 6}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 8, "contract_score": 0, "customer_quality_score": 13, "dilution_cb_risk_score": 0, "execution_risk_score": -2, "inventory_turn_score": 5, "legal_or_contract_risk_score": 0, "margin_bridge_score": 10, "policy_or_regulatory_score": 0, "relative_strength_score": 16, "revision_score": 12, "valuation_repricing_score": 11}, "row_type": "score_simulation", "score_return_alignment_label": "sellthrough_watch_but_thesis_break_late", "stage_label_after": "Stage2-Watch / 4C-watch", "stage_label_before": "Stage3-Yellow_false_positive_risk", "symbol": "237880", "trigger_id": "R5L16_C20_CLIO_T2A_20240513", "weighted_score_after": 62, "weighted_score_before": 76}
{"MAE_90D_pct": -19.2, "MFE_90D_pct": 46.5, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_ABLECNC_20240510_ROADSHOP_REOPENING_THEME_BETA", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "inventory_turn_score"], "component_delta_explanation": "C20 shadow profile separates ODM/export reorder and margin conversion from roadshop/reopening/theme beta; price-only spikes remain overlay-only.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 1, "contract_score": 0, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": -12, "inventory_turn_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 3, "policy_or_regulatory_score": 0, "relative_strength_score": 8, "revision_score": 4, "valuation_repricing_score": 6}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 3, "contract_score": 0, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": -1, "inventory_turn_score": 2, "legal_or_contract_risk_score": 0, "margin_bridge_score": 7, "policy_or_regulatory_score": 0, "relative_strength_score": 18, "revision_score": 8, "valuation_repricing_score": 13}, "row_type": "score_simulation", "score_return_alignment_label": "price_beta_without_durable_channel_conversion", "stage_label_after": "Stage2-Watch-Rejected", "stage_label_before": "Stage2-Actionable_false_positive_risk", "symbol": "078520", "trigger_id": "R5L16_C20_ABLECNC_T2_REJECT_20240510", "weighted_score_after": 56, "weighted_score_before": 73}
{"MAE_90D_pct": -52.2, "MFE_90D_pct": 9.5, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "R5L16_C20_TONYMOLY_20240510_PRICE_ONLY_LOCAL_4B", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "inventory_turn_score"], "component_delta_explanation": "C20 shadow profile separates ODM/export reorder and margin conversion from roadshop/reopening/theme beta; price-only spikes remain overlay-only.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 0, "contract_score": 0, "customer_quality_score": 4, "dilution_cb_risk_score": 0, "execution_risk_score": -18, "inventory_turn_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 2, "policy_or_regulatory_score": 0, "relative_strength_score": 7, "revision_score": 3, "valuation_repricing_score": 8}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "channel_reorder_score": 2, "contract_score": 0, "customer_quality_score": 6, "dilution_cb_risk_score": 0, "execution_risk_score": -1, "inventory_turn_score": 1, "legal_or_contract_risk_score": 0, "margin_bridge_score": 6, "policy_or_regulatory_score": 0, "relative_strength_score": 18, "revision_score": 8, "valuation_repricing_score": 17}, "row_type": "score_simulation", "score_return_alignment_label": "good_4B_overlay_after_price_beta", "stage_label_after": "4B overlay only / no positive stage", "stage_label_before": "Stage2-Actionable/Yellow edge", "symbol": "214420", "trigger_id": "R5L16_C20_TONYMOLY_T4B_20240614", "weighted_score_after": 52, "weighted_score_before": 72}
{"canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "5 new R5/C20 symbols; ODM/export positives balanced against roadshop/theme beta counterexamples; no repeated 실리콘투/브이티/LG생활건강/아모레퍼시픽 rows.", "do_not_propose_new_weight_delta": false, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "16", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 4, "new_symbol_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "residual_error_types_found": ["roadshop_theme_beta_false_positive", "sellthrough_reversal_4c_late", "verified_odm_export_yellow_too_late", "price_only_local_4b_needed"], "reused_case_count": 0, "round": "R5", "round_schedule_status": "valid", "round_sector_consistency": "pass", "row_type": "residual_contribution", "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "scheduled_loop": "16", "scheduled_round": "R5", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"]}
{"canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "NONE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "price_source": "Songdaiki/stock-web", "reason": "all selected representative cases have usable 180D windows; TONYMOLY is 4B overlay only and not aggregate representative", "row_type": "narrative_only", "symbol": null, "usage": "not_weight_calibration"}
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
completed_loop = 16
next_round = R6
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest inspected: `atlas/manifest.json`; manifest max date `2026-02-20`.
- Symbol profiles inspected: `192/192820`, `161/161890`, `237/237880`, `078/078520`, `214/214420`.
- Tradable shards inspected for entry rows and observed forward windows: `192820/2024.csv`, `161890/2024.csv`, `237880/2024.csv`, `078520/2024.csv`, `214420/2024.csv`.
- No `stock_agent/src/e2r` files were opened.
- This MD contains shadow-only research rows and no investment recommendation.

