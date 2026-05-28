# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 14
completed_round: R5
completed_loop: 14
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION
output_file: e2r_stock_web_v12_residual_round_R5_loop_14_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
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

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`, with the already-applied global axes treated as baseline: Stage2 actionable evidence bonus, Yellow 75, Green 87, Green revision minimum 55, cross-evidence Green buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing.

This MD does **not** re-propose those global axes. It stress-tests them inside the C20 consumer-beauty/food global distribution archetype.

## 2. Round / Large Sector / Canonical Archetype Scope

- `scheduled_round`: R5
- `scheduled_loop`: 14
- `large_sector_id`: `L5_CONSUMER_BRAND_DISTRIBUTION`
- `canonical_archetype_id`: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`
- `fine_archetype_id`: `K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION`
- `loop_objective`: `coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test`

R5 maps directly to L5, so the round-sector consistency gate passes. The selected canonical archetype stays inside consumer/brand/distribution rather than drifting into R13 cross-archetype red-team work.

## 3. Previous Coverage / Duplicate Avoidance Check

The immediately preceding generated loop ended at `R4 / Loop 14` and declared `next_round = R5`, `next_loop = 14`. Existing accessible registry material showed many earlier non-v12 and v12-like calibration rows, but the current loop is treated as a fresh R5 scheduled round. No `src/e2r` code was read.

Novelty gate:

- New independent cases: 4 / 4 representative cases = 100%.
- New symbols: `257720`, `018290`, `051900`, `090430`.
- Reused cases: 0.
- Same canonical archetype repetition: allowed; same symbol/trigger repetition: not used.
- Positive/counterexample balance: 2 positive, 2 counterexample.

The coverage gap selected here is not “consumer sector in general.” It is the narrower C20 question: when does global beauty/food distribution evidence mean true channel rerating rather than a reopening headline or price beta?

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
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

The manifest states that the atlas is raw/unadjusted, uses tradable OHLCV calibration shards, excludes zero-volume/zero-OHLC rows from calibration shards, and blocks corporate-action-contaminated windows by default. The manifest `max_date` is `2026-02-20`, and all forward windows in this MD sit before that date.

Symbol profile checks:

| symbol | company | profile_path | profile last_date | corporate_action_window_status for trigger window |
| --- | --- | --- | --- | --- |
| 257720 | 실리콘투 | atlas/symbol_profiles/257/257720.json | 2026-02-20 | clean_180D_window; historical corporate-action candidates are 2022 only |
| 018290 | 브이티 | atlas/symbol_profiles/018/018290.json | 2026-02-20 | clean_180D_window; last candidate before test window is 2019-11-08 |
| 051900 | LG생활건강 | atlas/symbol_profiles/051/051900.json | 2026-02-20 | clean_180D_window; no corporate-action candidates |
| 090430 | 아모레퍼시픽 | atlas/symbol_profiles/090/090430.json | 2026-02-20 | clean_180D_window; 2015 candidate outside test window |

## 5. Historical Eligibility Gate

All representative triggers pass:

- Trigger dates are historical.
- Entry dates exist in stock-web tradable shards.
- At least 180 forward trading days are available before manifest max date.
- OHLCV rows include high/low/close/volume.
- 30D/90D/180D MFE and MAE were computed from stock-web raw/unadjusted tradable rows.
- Corporate-action candidate dates do not overlap the tested 180D windows.

## 6. Canonical Archetype Compression Map

C20 can easily sprawl into many fine narratives: K-beauty Amazon/TikTok, Japan drugstore sell-through, China duty-free recovery, ODM/brand export, food export, and global distributor platforms. This loop compresses them into one scoring distinction:

```text
real C20 rerating = verified reorder / sell-through / financial conversion
weak C20 beta     = country reopening / channel headline / price rebound without margin bridge
```

The score rule should therefore care less about “해외/글로벌/리오프닝” words and more about whether the business has already converted that visibility into repeat orders, gross margin, operating leverage, or durable customer/channel confirmation.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90/MAE90 | MFE180/MAE180 | profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C20_SILICON2_2024_EXPORT_PLATFORM_EARNINGS | 257720 | 실리콘투 | structural_success | Stage3-Green | 2024-05-10 @ 26250 | 106.5 / -17.9 | 106.5 / -17.9 | current_profile_too_late |
| C20_VT_2024_JAPAN_PRODUCT_SELLTHROUGH | 018290 | 브이티 | high_mae_success | Stage3-Green | 2024-05-10 @ 25400 | 57.5 / -12.6 | 57.5 / -12.6 | current_profile_correct |
| C20_LGHH_2022_CHINA_REOPENING_HEADLINE | 051900 | LG생활건강 | false_positive_green | Stage2-Actionable | 2022-11-11 @ 613000 | 25.9 / -14.0 | 25.9 / -30.3 | current_profile_false_positive |
| C20_AMORE_2022_CHINA_REOPENING_HEADLINE | 090430 | 아모레퍼시픽 | failed_rerating | Stage2-Actionable | 2022-11-11 @ 121500 | 28.2 / -4.5 | 28.2 / -22.7 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

The two positive cases (`실리콘투`, `브이티`) both show a repeat-channel and earnings-conversion bridge. They are not merely “K-beauty theme” rows. The two counterexamples (`LG생활건강`, `아모레퍼시픽`) show that reopening headlines can produce respectable 30D/90D MFE, but the subsequent drawdown punishes premature Stage3 promotion when reorder and margin evidence are missing.

This is the core residual: C20 does not fail because early signals are useless. It fails when the model cannot tell the difference between a product/channel flywheel and a tourist-flow/headline rebound.

## 9. Evidence Source Map

| evidence family | positive evidence | counterexample evidence | scoring implication |
| --- | --- | --- | --- |
| Channel reorder / sell-through | 실리콘투 and 브이티 had visible product-channel conversion and earnings momentum | LG생활건강 and 아모레퍼시픽 had reopening/China beta but weak reorder visibility | require channel-quality confirmation for Stage3 |
| Margin bridge | positives converted sales into operating leverage | counterexamples lacked durable profitability bridge | margin bridge should weigh more in C20 than plain revenue rebound |
| Relative strength | helpful in all four cases | dangerous if not paired with reorder/margin evidence | relative strength is a timing feature, not a C20 thesis feature |
| 4B overlay | 실리콘투 post-rerating valuation/positioning overheat was useful | price-only local peak in reopening names came too early | keep full 4B non-price requirement |

## 10. Price Data Source Map

| symbol | year shards used | entry row anchor | forward window anchor |
| --- | --- | --- | --- |
| 257720 | `257/257720/2024.csv` | 2024-05-10 close 26,250 | 2024-06-19 high 54,200; post-peak lows into Nov 2024 |
| 018290 | `018/018290/2024.csv` | 2024-05-10 close 25,400 | 2024-06-19 high 40,000; Aug 2024 drawdown low 26,000 |
| 051900 | `051/051900/2022.csv`, `051/051900/2023.csv` | 2022-11-11 close 613,000 | 2023-01 high 772,000; July 2023 low near 427,000 |
| 090430 | `090/090430/2022.csv`, `090/090430/2023.csv` | 2022-11-11 close 121,500 | 2023-02 high 155,800; July 2023 low near 93,900 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | profile | dedupe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_C20_SILICON2_2024Q1_STAGE3_GREEN | 257720 | Stage3-Green | 2024-05-10 / 26250 | 106.5 | -17.9 | 106.5 | -17.9 | 106.5 | -17.9 | 2024-06-19 / 54200 | current_profile_too_late | True |
| T_C20_SILICON2_2024_4B_VALUATION_OVERHEAT | 257720 | Stage4B | 2024-06-19 / 50700 | 6.9 | -20.6 | 6.9 | -52.9 | 6.9 | -52.9 | 2024-06-19 / 54200 | current_profile_correct | False |
| T_C20_VT_2024Q1_STAGE3_GREEN | 018290 | Stage3-Green | 2024-05-10 / 25400 | 57.5 | -12.6 | 57.5 | -12.6 | 57.5 | -12.6 | 2024-06-19 / 40000 | current_profile_correct | True |
| T_C20_LGHH_2022_REOPENING_FALSE_POSITIVE | 051900 | Stage2-Actionable | 2022-11-11 / 613000 | 21.7 | -3.3 | 25.9 | -14.0 | 25.9 | -30.3 | 2023-01-20 / 772000 | current_profile_false_positive | True |
| T_C20_AMORE_2022_REOPENING_FALSE_POSITIVE | 090430 | Stage2-Actionable | 2022-11-11 / 121500 | 18.5 | -7.8 | 28.2 | -4.5 | 28.2 | -22.7 | 2023-02-10 / 155800 | current_profile_false_positive | True |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 실리콘투 — verified C20 flywheel but Green lateness remains

The 2024-05-10 confirmed earnings trigger worked strongly: entry close 26,250, 30D/90D high 54,200, and +106.5% MFE. But the price path also shows that the pure Green confirmation came after an earlier channel-traction move. Using the earlier 2024-02-21 shock row as a Stage2/Yellow comparison, the Green lateness ratio is about `0.36`, which is “somewhat late” but not a full failure.

The June 2024 4B overlay is clean as a risk overlay: non-price thesis was not broken, but valuation/positioning overheat after a rapid rerating was enough to mark a full-window 4B risk zone.

### 12.2 브이티 — high-MAE success, not a false positive

The 2024-05-10 entry at 25,400 reached a 40,000 high by 2024-06-19. MAE was still meaningful because the entry-day low and subsequent volatility were large. This is a “high MAE success,” useful for C20 because beauty-product sell-through can be volatile even when the channel thesis is real.

### 12.3 LG생활건강 — reopening beta produced MFE but failed rerating durability

The 2022-11-11 entry at 613,000 reached a 772,000 high, so a naive trigger-level study might call it a win. The later 180D drawdown to the 427,000 area shows the residual issue: reopening headlines and relative strength produced tradeable MFE, but did not create durable Stage3 evidence.

### 12.4 아모레퍼시픽 — similar reopening false positive pattern

The 2022-11-11 entry at 121,500 reached a 155,800 high, but later dropped toward the 93,900 area. This reinforces that reopening/country beta should be capped until reorder and margin evidence confirm the channel.

## 13. Current Calibrated Profile Stress Test

| question | C20 finding |
| --- | --- |
| How would current profile judge these? | It would likely accept 실리콘투/브이티 after confirmed revisions, but could over-score LG생활건강/아모레퍼시픽 if relative strength and reopening headlines were treated as sufficient cross evidence. |
| Did judgment match MFE/MAE? | Mixed. Positive cases aligned; counterexamples had MFE but poor drawdown-adjusted alignment. |
| Was Stage2 bonus too high/low? | Not globally. In C20, Stage2 should be useful only when channel evidence is not merely thematic. |
| Was Yellow 75 too high/low? | Kept. But C20 headline-only beta should be capped below Yellow unless reorder/margin evidence appears. |
| Was Green 87/revision 55 too high/low? | Kept globally. C20 may need an earlier Yellow exception for verified sell-through before full revision consensus. |
| Was price-only blowoff guard appropriate? | Yes, strengthened. Reopening false positives show why price alone is insufficient. |
| Was full 4B non-price requirement appropriate? | Yes. Silicon2 4B worked because valuation/positioning evidence existed; reopening local peaks alone were too early. |
| Was hard 4C routing too late? | In counterexamples, 4C would have been late if it waited for explicit thesis break; C20 should add earlier thesis-break watch when reorder/margin evidence fails to arrive. |

## 14. Stage2 / Yellow / Green Comparison

C20 has a special timing shape. The true winners often begin as sell-through/order-quality stories before full financial confirmation. But the losers also begin as plausible macro/channel stories. The difference is not the presence of global/reopening language; it is the conversion chain.

```text
C20 early positive chain:
product/channel traction -> repeat order / distributor evidence -> margin bridge -> revision confirmation

C20 false positive chain:
country reopening / duty-free headline -> price rebound -> no reorder proof -> no margin bridge -> drawdown
```

The proposed C20 shadow rule does not lower the Green threshold. It inserts a verification gate so that channel-quality and margin conversion must be visible before Stage3 promotion.

## 15. 4B Local vs Full-window Timing Audit

Silicon2’s 2024-06-19 overlay has both high local and full-window proximity because it sits near the full observed cycle peak. Its later drawdown makes the 4B overlay useful. The LG생활건강 and 아모레퍼시픽 local peaks are different: they had price-only reopening peaks but not enough non-price evidence to treat them as full 4B thesis overlays at the time. They should be marked as `price_only_local_4B_too_early` unless accompanied by valuation, positioning, revision slowdown, or channel evidence.

## 16. 4C Protection Audit

Hard 4C should remain thesis-break based. But C20 needs an earlier watch label:

```text
if global/reopening/channel headline exists
and 1~2 reporting cycles pass without reorder, sell-through, margin bridge, or revision confirmation:
    four_c_protection_label = thesis_break_watch_only
```

This does not make a sell signal by itself. It prevents a stale Stage2/Stage3 label from lingering after the promised channel recovery fails to become visible.

## 17. Sector-Specific Rule Candidate

No broad L5 sector-specific rule is proposed yet. C18 consumer export, C19 retail inventory/margin, and C20 global distribution are similar but not identical. This loop supports a **canonical** C20 rule, not a whole L5 rule.

## 18. Canonical-Archetype Rule Candidate

Proposed C20 canonical shadow rules:

```text
C20_channel_reorder_margin_confirmation_gate:
  For Stage3-Yellow/Green in beauty/food global distribution, require at least one of:
    - repeat order or sell-through confirmation,
    - distributor/customer quality evidence,
    - gross margin / operating margin bridge,
    - confirmed revision tied to overseas channel conversion.
  Reopening/country/duty-free headline alone cannot promote beyond Stage2-Actionable.
```

```text
C20_price_only_reopening_beta_discount:
  If the only evidence is reopening, tourist-flow, duty-free, or channel headline plus price strength,
  cap positive score and require follow-up financial visibility before Green.
```

```text
C20_verified_channel_traction_stage2_exception:
  If repeat sell-through and early margin conversion are visible before formal revision consensus,
  allow earlier Yellow/Actionable scoring, but do not lower global Green thresholds.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 54.5 | -12.2 | 2/4 | mixed; positives survive but reopening false positives remain. |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback | 54.5 | -12.6 | 2/4+ | worse; headline and price beta would be over-promoted. |
| P1_L5_sector_specific_candidate | sector_specific | C20_channel_reorder_margin_confirmation_gate | 54.5 | -12.6 | 1/4 or lower when gate enforced | better but should remain canonical rather than whole-sector until C18/C19 are tested. |
| P2_C20_canonical_candidate | canonical_archetype_specific | C20_channel_reorder_margin_confirmation_gate|C20_price_only_reopening_beta_discount | 54.5 | -12.6 | 0/2 for reopening-headline counterexamples under proposed guard | best explanatory fit for this loop. |
| P3_C20_counterexample_guard | canonical_archetype_specific | Stage3 promotion guard only | 27.1 | -9.3 | guarded | avoids confusing transient reopening MFE with durable rerating. |

## 20. Score-Return Alignment Matrix

| bucket | trigger_ids | return alignment | interpretation |
| --- | --- | --- | --- |
| Verified channel conversion | Silicon2, VT | strong MFE, tolerable but real MAE | C20 should reward channel proof plus margin bridge |
| Reopening headline beta | LG생활건강, 아모레퍼시픽 | temporary MFE, poor drawdown-adjusted durability | C20 should cap headline-only promotion |
| 4B overlay | Silicon2 June 2024 | full-window peak proximity good | non-price 4B rule is strengthened |
| 4C watch | LG생활건강, 아모레퍼시픽 | thesis deterioration arrived after failed conversion | add watch-only protection label, not automatic hard 4C |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION | 2 | 2 | 1 | 2 watch-only | 4 | 0 | 5 | 4 | 3 | false | true | C20 now has balanced positive/counterexample seed; C18/C19 still need separate loop coverage. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - reopening_headline_false_positive
  - green_lateness_in_verified_channel_conversion
  - price_only_local_4B_too_early
new_axis_proposed:
  - C20_channel_reorder_margin_confirmation_gate
  - C20_price_only_reopening_beta_discount
  - C20_verified_channel_traction_stage2_exception
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Historical C20 trigger-level OHLC behavior using stock-web tradable raw rows.
- Positive and counterexample balance.
- C20-specific channel/reorder/margin gate as a shadow-only candidate.
- Local vs full-window 4B distinction.

Not validated:

- Current/live stock selection.
- `stock_agent` production scoring code.
- Broker/API integration.
- Any investment recommendation.
- Global rule promotion across multiple large sectors.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_margin_confirmation_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,Reopening/global-channel headline should not promote to Stage3 without confirmed reorder or margin bridge,False-positive pressure reduced in LG생활건강/아모레퍼시픽 while preserving 실리콘투/브이티 positives,T_C20_SILICON2_2024Q1_STAGE3_GREEN|T_C20_VT_2024Q1_STAGE3_GREEN|T_C20_LGHH_2022_REOPENING_FALSE_POSITIVE|T_C20_AMORE_2022_REOPENING_FALSE_POSITIVE,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C20_verified_channel_traction_stage2_exception,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,When repeat sell-through plus early margin conversion exists before full Street revision C20 can allow earlier Yellow,Green lateness reduced for 실리콘투 without weakening Green threshold globally,T_C20_SILICON2_2024Q1_STAGE3_GREEN|T_C20_VT_2024Q1_STAGE3_GREEN,2,2,0,low,canonical_shadow_only,requires additional holdout before production promotion
shadow_weight,C20_price_only_reopening_beta_discount,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,Price-only local peak after reopening headlines should be watch/4B overlay not positive rerating evidence,Separates transient MFE from durable score-return alignment,T_C20_LGHH_2022_REOPENING_FALSE_POSITIVE|T_C20_AMORE_2022_REOPENING_FALSE_POSITIVE,2,2,2,medium,canonical_shadow_only,not production; reinforces existing price-only guard
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C20_SILICON2_2024_EXPORT_PLATFORM_EARNINGS","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C20_SILICON2_2024Q1_STAGE3_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage3 confirmation worked, but C20 verified channel traction was already actionable before the Q1 earnings gap.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"K-beauty cross-border distribution platform; Q1 2024 earnings conversion made channel reorder and operating leverage visible."}
{"row_type":"case","case_id":"C20_VT_2024_JAPAN_PRODUCT_SELLTHROUGH","symbol":"018290","company_name":"브이티","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T_C20_VT_2024Q1_STAGE3_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Confirmed product sell-through plus earnings conversion aligned with high 90D MFE despite a noisy entry drawdown.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Beauty brand/product channel case; Japan/global product traction became investable only after repeated sell-through and margin evidence."}
{"row_type":"case","case_id":"C20_LGHH_2022_CHINA_REOPENING_HEADLINE","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T_C20_LGHH_2022_REOPENING_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Reopening headline and price rebound produced temporary MFE, but no durable channel reorder/margin bridge; 180D MAE and drawdown dominated.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Large incumbent beauty brand; China reopening beta was not enough without reorder proof and financial revision follow-through."}
{"row_type":"case","case_id":"C20_AMORE_2022_CHINA_REOPENING_HEADLINE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_C20_AMORE_2022_REOPENING_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"The reopening rally generated 90D MFE, but subsequent price path showed that channel recovery without confirmed reorder and margin bridge was not a durable rerating.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Beauty incumbent China-reopening proxy; outcome argues for a C20-specific reorder/margin confirmation gate."}
{"trigger_id":"T_C20_SILICON2_2024Q1_STAGE3_GREEN","case_id":"C20_SILICON2_2024_EXPORT_PLATFORM_EARNINGS","symbol":"257720","company_name":"실리콘투","trigger_type":"Stage3-Green","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":26250,"evidence_available_at_that_date":"Q1 2024 earnings conversion made cross-border K-beauty distribution operating leverage public.","evidence_source":"company quarterly earnings / public market disclosure; stock-web 2024 shard entry row","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":106.5,"MFE_90D_pct":106.5,"MFE_180D_pct":106.5,"MFE_1Y_pct":106.5,"MFE_2Y_pct":null,"MAE_30D_pct":-17.9,"MAE_90D_pct":-17.9,"MAE_180D_pct":-17.9,"MAE_1Y_pct":-17.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-55.9,"green_lateness_ratio":0.36,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_after_confirmed_channel_conversion","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C20_SILICON2_2024Q1_GREEN","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"T_C20_SILICON2_2024_4B_VALUATION_OVERHEAT","case_id":"C20_SILICON2_2024_EXPORT_PLATFORM_EARNINGS","symbol":"257720","company_name":"실리콘투","trigger_type":"Stage4B","trigger_date":"2024-06-19","entry_date":"2024-06-19","entry_price":50700,"evidence_available_at_that_date":"Price and positioning overheat after a rapid earnings-confirmation rerating; not a thesis break.","evidence_source":"stock-web OHLC peak/proximity check; non-price 4B evidence is valuation/positioning, not cancellation.","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":6.9,"MFE_90D_pct":6.9,"MFE_180D_pct":6.9,"MFE_1Y_pct":6.9,"MFE_2Y_pct":null,"MAE_30D_pct":-20.6,"MAE_90D_pct":-52.9,"MAE_180D_pct":-52.9,"MAE_1Y_pct":-52.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-55.9,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.02,"four_b_full_window_peak_proximity":1.02,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C20_SILICON2_2024_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol as representative; different 4B overlay trigger family","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"T_C20_VT_2024Q1_STAGE3_GREEN","case_id":"C20_VT_2024_JAPAN_PRODUCT_SELLTHROUGH","symbol":"018290","company_name":"브이티","trigger_type":"Stage3-Green","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":25400,"evidence_available_at_that_date":"Product sell-through and quarterly earnings conversion confirmed the brand-channel path.","evidence_source":"company quarterly earnings / product-channel public evidence; stock-web 2024 shard entry row","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":57.5,"MFE_90D_pct":57.5,"MFE_180D_pct":57.5,"MFE_1Y_pct":57.5,"MFE_2Y_pct":null,"MAE_30D_pct":-12.6,"MAE_90D_pct":-12.6,"MAE_180D_pct":-12.6,"MAE_1Y_pct":-12.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":40000,"drawdown_after_peak_pct":-35.0,"green_lateness_ratio":0.18,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C20_VT_2024Q1_GREEN","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"T_C20_LGHH_2022_REOPENING_FALSE_POSITIVE","case_id":"C20_LGHH_2022_CHINA_REOPENING_HEADLINE","symbol":"051900","company_name":"LG생활건강","trigger_type":"Stage2-Actionable","trigger_date":"2022-11-11","entry_date":"2022-11-11","entry_price":613000,"evidence_available_at_that_date":"China reopening / duty-free beta headline and price rebound; reorder and margin bridge were not confirmed.","evidence_source":"public reopening headline family; stock-web 2022/2023 shard entry and forward rows","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":21.7,"MFE_90D_pct":25.9,"MFE_180D_pct":25.9,"MFE_1Y_pct":25.9,"MFE_2Y_pct":null,"MAE_30D_pct":-3.3,"MAE_90D_pct":-14.0,"MAE_180D_pct":-30.3,"MAE_1Y_pct":-30.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-01-20","peak_price":772000,"drawdown_after_peak_pct":-44.7,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":0.75,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C20_LGHH_2022_REOPENING","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"T_C20_AMORE_2022_REOPENING_FALSE_POSITIVE","case_id":"C20_AMORE_2022_CHINA_REOPENING_HEADLINE","symbol":"090430","company_name":"아모레퍼시픽","trigger_type":"Stage2-Actionable","trigger_date":"2022-11-11","entry_date":"2022-11-11","entry_price":121500,"evidence_available_at_that_date":"China reopening / cosmetics recovery headline; reorder, profitability and channel recovery were not yet verified.","evidence_source":"public reopening headline family; stock-web 2022/2023 shard entry and forward rows","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":18.5,"MFE_90D_pct":28.2,"MFE_180D_pct":28.2,"MFE_1Y_pct":28.2,"MFE_2Y_pct":null,"MAE_30D_pct":-7.8,"MAE_90D_pct":-4.5,"MAE_180D_pct":-22.7,"MAE_1Y_pct":-22.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-10","peak_price":155800,"drawdown_after_peak_pct":-39.7,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":0.7,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C20_AMORE_2022_REOPENING","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_CONFIRMATION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2022.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"C20_SILICON2_2024_EXPORT_PLATFORM_EARNINGS","trigger_id":"T_C20_SILICON2_2024Q1_STAGE3_GREEN","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":89,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":21,"revision_score":22,"relative_strength_score":18,"customer_quality_score":22,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":97,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates real reorder/margin confirmation from reopening/headline beta; 4B overlay converts valuation/positioning excess into risk, not positive stage evidence.","MFE_90D_pct":106.5,"MAE_90D_pct":-17.9,"score_return_alignment_label":"residual_error_or_lateness","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"C20_SILICON2_2024_EXPORT_PLATFORM_EARNINGS","trigger_id":"T_C20_SILICON2_2024_4B_VALUATION_OVERHEAT","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":20,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":22,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":98,"stage_label_before":"Stage4B-Overlay","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":20,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":-10,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates real reorder/margin confirmation from reopening/headline beta; 4B overlay converts valuation/positioning excess into risk, not positive stage evidence.","MFE_90D_pct":6.9,"MAE_90D_pct":-52.9,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"C20_VT_2024_JAPAN_PRODUCT_SELLTHROUGH","trigger_id":"T_C20_VT_2024Q1_STAGE3_GREEN","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":89,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":21,"revision_score":22,"relative_strength_score":18,"customer_quality_score":22,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":97,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates real reorder/margin confirmation from reopening/headline beta; 4B overlay converts valuation/positioning excess into risk, not positive stage evidence.","MFE_90D_pct":57.5,"MAE_90D_pct":-12.6,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"C20_LGHH_2022_CHINA_REOPENING_HEADLINE","trigger_id":"T_C20_LGHH_2022_REOPENING_FALSE_POSITIVE","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":20,"customer_quality_score":8,"policy_or_regulatory_score":18,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":20,"customer_quality_score":2,"policy_or_regulatory_score":18,"valuation_repricing_score":6,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":39,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates real reorder/margin confirmation from reopening/headline beta; 4B overlay converts valuation/positioning excess into risk, not positive stage evidence.","MFE_90D_pct":25.9,"MAE_90D_pct":-14.0,"score_return_alignment_label":"residual_error_or_lateness","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"C20_AMORE_2022_CHINA_REOPENING_HEADLINE","trigger_id":"T_C20_AMORE_2022_REOPENING_FALSE_POSITIVE","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":20,"customer_quality_score":8,"policy_or_regulatory_score":18,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":20,"customer_quality_score":2,"policy_or_regulatory_score":18,"valuation_repricing_score":6,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":39,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates real reorder/margin confirmation from reopening/headline beta; 4B overlay converts valuation/positioning excess into risk, not positive stage evidence.","MFE_90D_pct":28.2,"MAE_90D_pct":-4.5,"score_return_alignment_label":"residual_error_or_lateness","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"14","scheduled_round":"R5","scheduled_loop":"14","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["reopening_headline_false_positive","green_lateness_in_channel_conversion","price_only_local_4B_too_early"],"diversity_score_summary":"4 new symbols; 4 new trigger families; C20 positive/counterexample balance; no reused case.","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 14
next_round = R6
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files consulted:

- `atlas/manifest.json` — source name, row counts, max date, raw/unadjusted status, shard roots.
- `atlas/symbol_profiles/257/257720.json` — Silicon2 availability, candidate corporate-action dates, profile caveat.
- `atlas/symbol_profiles/018/018290.json` — VT availability and corporate-action candidate list.
- `atlas/symbol_profiles/051/051900.json` — LG생활건강 availability and clean corporate-action status.
- `atlas/symbol_profiles/090/090430.json` — 아모레퍼시픽 availability and 2015-only corporate-action candidate.
- `atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv` — Silicon2 entry, peak and drawdown rows.
- `atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv` — VT entry, peak and drawdown rows.
- `atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv` and `2023.csv` — reopening entry, peak and drawdown rows.
- `atlas/ohlcv_tradable_by_symbol_year/090/090430/2022.csv` and `2023.csv` — reopening entry, peak and drawdown rows.

The quantitative rows use stock-web raw/unadjusted tradable OHLC. 2Y fields are left null because the selected forward windows are not needed for this loop’s 180D calibration claim.

