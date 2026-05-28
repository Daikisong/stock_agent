# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R12
scheduled_loop: 11
completed_round: R12
completed_loop: 11
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD
output_file: e2r_stock_web_v12_residual_round_R12_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds **4** new independent cases, **2** counterexamples, and **3** residual errors for `R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT`.

## 1. Current Calibrated Profile Assumption

`P0 = e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as existing infrastructure, not new discoveries:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does **not** re-prove those axes. It asks a narrower R12/C31 question: when a life-service, food, or agri event appears, does the event connect to consumption volume, pricing, procurement, subsidy, or repeat-order evidence, or is it only fear-hoarding and price motion?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R12 |
| scheduled_loop | 11 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and under-covered service/agri/misc areas. This file therefore keeps C31 under R12 rather than creating an R13 cross-archetype checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact reviewed: `reports/e2r_calibration/by_round/R12.md`. R12 already has many representative triggers, so this loop avoids adding another generic Stage2-vs-Green proof. It adds a **food/life-service C31 residual split**.

Prior local R12 loop10 cases were `005860`, `057030`, `011150`, and `053290`. This loop uses `008040`, `218150`, `277410`, and `248170`, so no selected representative row reuses the same symbol + trigger_date + entry_date + evidence family from the immediate prior R12 MD.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

All quantitative rows use `tradable_raw`. Raw shards are not used for calibration.

## 5. Historical Eligibility Gate

All representative cases pass:

| gate | status |
|---|---|
| trigger_date is historical | pass |
| entry row exists in tradable shard | pass |
| 180 forward tradable days available by manifest max date | pass |
| OHLCV positive and present | pass |
| 30D/90D/180D MFE and MAE computed | pass |
| corporate-action contaminated 180D window | no selected 180D window overlaps profile candidate dates |

Profile caveat: `008040`, `218150`, and `277410` have historical corporate-action candidates outside the tested windows; `248170` has no candidate dates. This does not block the selected 2022/2023 windows.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | scoring meaning |
|---|---|---|
| GRAIN_WHEAT_FEED_SUPPLY_SECURITY | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | commodity/policy shock with real input-cost and pricing route |
| FUKUSHIMA_SALT_OR_CONDIMENT_HOARDING | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | food-safety fear event; must not promote without repeat-order/margin evidence |
| PRICE_ONLY_FEAR_SPIKE_4B_WATCH | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | overlay-only risk row, not positive Stage2/3 evidence |

## 7. Case Selection Summary

|case_id|symbol|role|trigger_family|why selected|new?|
|---|---|---|---|---|---|
|`R12L11_C31_008040_GRAIN`|`008040`|positive / structural_success|grain_wheat_supply_security|new symbol vs R12 loop10; real flour/feed route|true|
|`R12L11_C31_218150_FEED`|`218150`|positive / high_mae_success|feed_input_supply_security|new symbol; high-MFE/high-MAE route stress|true|
|`R12L11_C31_277410_SALT`|`277410`|counterexample / failed_rerating|fukushima_salt_hoarding|new symbol; food-safety fear spike without durable bridge|true|
|`R12L11_C31_248170_SAUCE`|`248170`|counterexample / failed_rerating|fukushima_condiment_inventory|new symbol; inventory/hoarding false positive guard|true|

## 8. Positive vs Counterexample Balance

| count field | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C/watch case_count | 0 |
| calibration_usable_case_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |

The positive side shows that food-security events can be real when they pass into pricing or volume. The counterexample side shows why the same C31 headline should stay watch-only when the route is merely fear-hoarding.

## 9. Evidence Source Map

| case | evidence source class | allowed for scoring | blocked for scoring |
|---|---|---|---|
| 008040 | war/food-price shock + company route | public event; input shock; flour/feed pricing route; relative strength | later peak outcome |
| 218150 | war/food-price shock + feed input route | public event; input shock; feed/additive relevance | blind Green after price squeeze |
| 277410 | Fukushima treated-water anxiety + salt hoarding | public event as watch-only; price/risk overlay | hoarding fear as durable Stage3 evidence |
| 248170 | Fukushima-related food-safety/inventory fear | public event as watch-only; price/risk overlay | condiment/salt theme without repeat-order or margin bridge |

## 10. Price Data Source Map

| symbol | company | profile_path | representative price shard | window status |
|---:|---|---|---|---|
| 008040 | 사조동아원 | atlas/symbol_profiles/008/008040.json | atlas/ohlcv_tradable_by_symbol_year/008/008040/2022.csv | clean_180D_window |
| 218150 | 미래생명자원 | atlas/symbol_profiles/218/218150.json | atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv | clean_180D_window |
| 277410 | 인산가 | atlas/symbol_profiles/277/277410.json | atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv | clean_180D_window |
| 248170 | 샘표식품 | atlas/symbol_profiles/248/248170.json | atlas/ohlcv_tradable_by_symbol_year/248/248170/2023.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

|trigger_id|case|type|entry|MFE90|MAE90|outcome|dedupe|
|---|---|---|---|---|---|---|---|
|`R12L11_C31_008040_STAGE2A_20220224`|`R12L11_C31_008040_GRAIN`|Stage2-Actionable|2022-02-24 @ 1335|107.12|-9.36|food_security_supply_shock_structural_success|representative|
|`R12L11_C31_008040_GREEN_20220418`|`R12L11_C31_008040_GRAIN`|Stage3-Green|2022-04-18 @ 1870|47.86|-26.47|green_confirmed_but_later_than_stage2|label_comparison_only|
|`R12L11_C31_218150_STAGE2A_20220224`|`R12L11_C31_218150_FEED`|Stage2-Actionable|2022-02-24 @ 8090|59.46|-19.04|feed_input_supply_shock_high_mfe_high_mae_success|representative|
|`R12L11_C31_218150_GREEN_20220322`|`R12L11_C31_218150_FEED`|Stage3-Green|2022-03-22 @ 11750|9.79|-36.6|late_green_high_mae_after_theme_squeeze|label_comparison_only|
|`R12L11_C31_277410_STAGE2WATCH_20230607`|`R12L11_C31_277410_SALT`|Stage2_event_premium_risk_watch|2023-06-07 @ 2550|72.35|-25.1|food_safety_hoarding_spike_failed_rerating|representative|
|`R12L11_C31_277410_4B_20230615`|`R12L11_C31_277410_SALT`|Stage4B|2023-06-15 @ 4055|8.38|-52.9|good_price_risk_overlay_without_full_green|4B_overlay_only|
|`R12L11_C31_248170_STAGE2WATCH_20230607`|`R12L11_C31_248170_SAUCE`|Stage2_event_premium_risk_watch|2023-06-07 @ 29300|67.41|-14.33|food_safety_inventory_spike_failed_rerating|representative|
|`R12L11_C31_248170_4B_20230620`|`R12L11_C31_248170_SAUCE`|Stage4B|2023-06-20 @ 42300|11.11|-40.66|price_only_event_cap_4B_watch|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

|trigger|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|
|R12L11_C31_008040_STAGE2A_20220224|1335|10.86|107.12|107.12|-9.36|-9.36|-25.09|2022-05-20 / 2765|-63.83|
|R12L11_C31_008040_GREEN_20220418|1870|47.86|47.86|47.86|-8.56|-26.47|-46.52|2022-05-20 / 2765|-63.83|
|R12L11_C31_218150_STAGE2A_20220224|8090|53.28|59.46|59.46|-19.04|-19.04|-42.71|2022-04-19 / 12900|-64.07|
|R12L11_C31_218150_GREEN_20220322|11750|9.79|9.79|9.79|-20.85|-36.6|-60.55|2022-04-19 / 12900|-64.07|
|R12L11_C31_277410_STAGE2WATCH_20230607|2550|72.35|72.35|72.35|-25.1|-25.1|-29.73|2023-06-16 / 4395|-59.23|
|R12L11_C31_277410_4B_20230615|4055|8.38|8.38|8.38|-52.9|-52.9|-55.81|2023-06-16 / 4395|-59.23|
|R12L11_C31_248170_STAGE2WATCH_20230607|29300|67.41|67.41|67.41|-1.02|-14.33|-14.33|2023-06-19 / 49050|-48.83|
|R12L11_C31_248170_4B_20230620|42300|11.11|11.11|11.11|-28.72|-40.66|-40.66|2023-06-20 / 47000|-46.6|

## 13. Current Calibrated Profile Stress Test

| question | finding |
|---|---|
| How would current profile judge these cases? | It would correctly allow supply-security Stage2 in 008040/218150 but risks over-promoting 277410/248170 if public event + relative strength are treated as enough. |
| Does judgement align with MFE/MAE? | Mixed. Positives have large MFE, but 218150 also has severe MAE. Counterexamples have large MFE but decay like fear spikes, not durable rerating. |
| Was Stage2 bonus too strong? | Too strong for food-safety hoarding events without volume/margin bridge; acceptable for grain/feed supply shock. |
| Was Yellow 75 too strict/loose? | Loose for hoarding events; acceptable for supply-security route cases. |
| Was Green 87/revision 55 too strict/loose? | Green is too loose if based on event headline and price only; too late if waiting for broad confirmation in fast supply-security shocks. |
| Price-only blowoff guard? | Strengthened. 277410/248170 need price-only blowoff block. |
| Full 4B non-price requirement? | Kept. Price-only local peak is watch/overlay, not a full thesis break. |
| Hard 4C routing? | No hard 4C row proposed here; the evidence is decay/overlay rather than thesis cancellation. |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green comparison | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 008040 | 1335 | 1870 | 0.37 | Green somewhat late; Stage2 route captures more upside. |
| 218150 | 8090 | 11750 | 0.76 | Green captures little remaining upside and much higher MAE. |
| 277410 | 2550 | no valid Green | not_applicable | hoarding/fear spike lacks durable route. |
| 248170 | 29300 | no valid Green | not_applicable | condiment/food-safety spike lacks durable route. |

## 15. 4B Local vs Full-window Timing Audit

| case | 4B trigger | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 277410 | 2023-06-15 close 4055 | 0.82 | 0.82 | good price-risk overlay, but price-only unless non-price 4B evidence appears |
| 248170 | 2023-06-20 close 42300 | 0.66 | 0.66 | useful 4B watch; not full 4B exit without non-price evidence |

## 16. 4C Protection Audit

No hard 4C row is used for weight calibration in this loop. The counterexamples are **failed rerating / 4B watch** cases, not contract cancellation, trial failure, accounting break, or forced-liquidation cases.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`.

For R12 food/life-service/agri-misc events, public event + relative strength should not be enough. A positive Stage2/Yellow promotion needs at least one of:

```text
- direct consumption or reorder signal,
- pricing or margin pass-through route,
- procurement/subsidy/legislation route,
- input-cost shock with clear beneficiary map,
- repeat-order or channel inventory conversion.
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

Proposed C31 rule:

```text
C31_POLICY_EVENT_PROBABILITY_AND_DIRECT_ROUTE_DISCOUNT:
  if public event is real but company route is fear-hoarding / inventory panic only:
      cap positive stage at Stage2_event_premium_risk_watch
      block Stage3-Green unless repeat-order, margin bridge, or procurement evidence appears
      allow 4B overlay when price is near local/full-window blowoff
  if public event has direct consumption/pricing/procurement route:
      allow Stage2-Actionable and Stage3-Yellow path
      require Green confirmation only after non-price evidence, not simply price continuation
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|avg_MFE90|avg_MAE90|false_positive_rate|late_green_count|verdict|
|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|4|76.58|-16.96|0.5|2|mixed; headline events need C31 route split|
|P0b_e2r_2_0_baseline_reference|rollback_reference|4|76.58|-16.96|0.5|2|weaker early route capture|
|P1_sector_specific_candidate_profile|sector_specific|4|83.29|-14.2|0.0|1|better: positive rows selected, hoarding rows watched|
|P2_canonical_archetype_candidate_profile|canonical_archetype_specific|4|83.29|-14.2|0.0|1|best candidate; archetype rule explains price split|
|P3_counterexample_guard_profile|counterexample_guard|2|0.0|0.0|0.0|0|removes false positive promotions; keeps watch/overlay rows|

## 20. Score-Return Alignment Matrix

| matrix cell | observation |
|---|---|
| high score + high MFE + acceptable route | 008040, 218150 Stage2 entries pass as C31 supply-security positives. |
| high score + high MFE + high MAE | 218150 shows positive route but needs high-MAE sizing guard. |
| high score + high MFE + no durable route | 277410/248170 are false-positive risks if promoted beyond watch. |
| late Green + lower residual upside | 008040 and especially 218150 show Green lateness inside fast event shocks. |
| 4B overlay useful | 277410/248170 blowoff rows improve risk labeling without turning into hard 4C. |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD|2|2|2|0|4|0|8|4|3|true|true|C31 has route-vs-hoarding split; still needs more non-food service/agri holdouts|

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - food_safety_hoarding_false_positive
  - late_green_high_mae
  - event_route_positive_vs_theme_counterexample_split
new_axis_proposed:
  - C31_event_to_consumption_or_procurement_route_bonus
  - C31_food_safety_hoarding_without_repeat_order_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- historical trigger rows only
- Songdaiki/stock-web tradable_raw OHLC rows
- 30D/90D/180D MFE and MAE
- C31 route-vs-hoarding residual split
- Stage2/Green timing and 4B overlay behavior
```

Not validated:

```text
- live 2026 candidates
- production scoring changes
- broker/API execution
- current recommendation/watchlist
- global axis promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_event_to_consumption_or_procurement_route_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"reward supply-security events only when pricing/volume/procurement route exists","selected positives retained; fear-hoarding false positives blocked",R12L11_C31_008040_STAGE2A_20220224|R12L11_C31_218150_STAGE2A_20220224,4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_food_safety_hoarding_without_repeat_order_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"fear/hoarding spikes require 4B watch rather than Green unless repeat-order or margin evidence appears","277410/248170 false-positive promotions blocked",R12L11_C31_277410_STAGE2WATCH_20230607|R12L11_C31_248170_STAGE2WATCH_20230607,4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L11_C31_008040_GRAIN", "symbol": "008040", "company_name": "사조동아원", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L11_C31_008040_STAGE2A_20220224", "current_profile_verdict": "current_profile_correct", "notes": "Wheat/flour/feed supply shock passed through to a plausible pricing route; Green confirmation was later and lower quality than Stage2-Actionable.", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R12L11_C31_218150_FEED", "symbol": "218150", "company_name": "미래생명자원", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R12L11_C31_218150_STAGE2A_20220224", "current_profile_verdict": "current_profile_too_late", "notes": "Large MFE but severe MAE; confirms event-to-input route while requiring position/risk guard for C31.", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R12L11_C31_277410_SALT", "symbol": "277410", "company_name": "인산가", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L11_C31_277410_STAGE2WATCH_20230607", "current_profile_verdict": "current_profile_false_positive", "notes": "Fukushima salt-hoarding event created a spike without durable repeat-order or margin bridge.", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_guard_needed", "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R12L11_C31_248170_SAUCE", "symbol": "248170", "company_name": "샘표식품", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L11_C31_248170_STAGE2WATCH_20230607", "current_profile_verdict": "current_profile_false_positive", "notes": "Condiment/food-safety fear repricing lacked a policy procurement or recurring volume route; 4B overlay was more useful than Green.", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_guard_needed", "price_source": "Songdaiki/stock-web"}
{"row_type": "trigger", "trigger_id": "R12L11_C31_008040_STAGE2A_20220224", "case_id": "R12L11_C31_008040_GRAIN", "symbol": "008040", "company_name": "사조동아원", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Russia/Ukraine war exposed wheat/flour supply-security shock; Korean flour/feed names had visible pricing-volume route rather than pure theme-only price action.", "evidence_source": "FAO food-price shock context; stock-web atlas/ohlcv_tradable_by_symbol_year/008/008040/2022.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008040/2022.csv", "profile_path": "atlas/symbol_profiles/008/008040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 1335, "MFE_30D_pct": 10.86, "MFE_90D_pct": 107.12, "MFE_180D_pct": 107.12, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.36, "MAE_90D_pct": -9.36, "MAE_180D_pct": -25.09, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-20", "peak_price": 2765, "drawdown_after_peak_pct": -63.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "food_security_supply_shock_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_008040_GRAIN_2022-02-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L11_C31_008040_GREEN_20220418", "case_id": "R12L11_C31_008040_GRAIN", "symbol": "008040", "company_name": "사조동아원", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2022-04-18", "evidence_available_at_that_date": "By mid-April the price shock and feed/flour route were obvious, but entry was already far above the Stage2 anchor.", "evidence_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/008/008040/2022.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008040/2022.csv", "profile_path": "atlas/symbol_profiles/008/008040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-18", "entry_price": 1870, "MFE_30D_pct": 47.86, "MFE_90D_pct": 47.86, "MFE_180D_pct": 47.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.56, "MAE_90D_pct": -26.47, "MAE_180D_pct": -46.52, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-20", "peak_price": 2765, "drawdown_after_peak_pct": -63.83, "green_lateness_ratio": 0.37, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "green_confirmed_but_later_than_stage2", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_008040_GRAIN_20220224", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L11_C31_218150_STAGE2A_20220224", "case_id": "R12L11_C31_218150_FEED", "symbol": "218150", "company_name": "미래생명자원", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Feed/additive supply-security route moved with the grain shock, but high MAE shows C31 needs risk sizing and not a blind Green promotion.", "evidence_source": "FAO food-price shock context; stock-web atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv", "profile_path": "atlas/symbol_profiles/218/218150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 8090, "MFE_30D_pct": 53.28, "MFE_90D_pct": 59.46, "MFE_180D_pct": 59.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.04, "MAE_90D_pct": -19.04, "MAE_180D_pct": -42.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-19", "peak_price": 12900, "drawdown_after_peak_pct": -64.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "feed_input_supply_shock_high_mfe_high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_218150_FEED_2022-02-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L11_C31_218150_GREEN_20220322", "case_id": "R12L11_C31_218150_FEED", "symbol": "218150", "company_name": "미래생명자원", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2022-03-22", "evidence_available_at_that_date": "A later Green-like confirmation entered after much of the event repricing; the forward path retained severe drawdown risk.", "evidence_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv", "profile_path": "atlas/symbol_profiles/218/218150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-22", "entry_price": 11750, "MFE_30D_pct": 9.79, "MFE_90D_pct": 9.79, "MFE_180D_pct": 9.79, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.85, "MAE_90D_pct": -36.6, "MAE_180D_pct": -60.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-19", "peak_price": 12900, "drawdown_after_peak_pct": -64.07, "green_lateness_ratio": 0.76, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "late_green_high_mae_after_theme_squeeze", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_218150_FEED_20220224", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L11_C31_277410_STAGE2WATCH_20230607", "case_id": "R12L11_C31_277410_SALT", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2023-06-07", "evidence_available_at_that_date": "Fukushima treated-water anxiety and salt hoarding created a demand spike, but durable repeat-order and margin bridge were not visible at the trigger date.", "evidence_source": "AP/IAEA Fukushima discharge context; stock-web atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-07", "entry_price": 2550, "MFE_30D_pct": 72.35, "MFE_90D_pct": 72.35, "MFE_180D_pct": 72.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -25.1, "MAE_90D_pct": -25.1, "MAE_180D_pct": -29.73, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -59.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "food_safety_hoarding_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_277410_SALT_2023-06-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L11_C31_277410_4B_20230615", "case_id": "R12L11_C31_277410_SALT", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2023-06-15", "evidence_available_at_that_date": "Price entered the local blowoff zone before a durable cash-flow bridge appeared; this is 4B overlay/risk calibration only.", "evidence_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-15", "entry_price": 4055, "MFE_30D_pct": 8.38, "MFE_90D_pct": 8.38, "MFE_180D_pct": 8.38, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -52.9, "MAE_90D_pct": -52.9, "MAE_180D_pct": -55.81, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -59.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.82, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "good_price_risk_overlay_without_full_green", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_277410_SALT_20230607", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L11_C31_248170_STAGE2WATCH_20230607", "case_id": "R12L11_C31_248170_SAUCE", "symbol": "248170", "company_name": "샘표식품", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2023-06-07", "evidence_available_at_that_date": "Food-safety fear around salt/condiment inventory produced a sharp spike but the evidence was hoarding-led, not repeat-order or subsidy/legislation-led.", "evidence_source": "AP/IAEA Fukushima discharge context; stock-web atlas/ohlcv_tradable_by_symbol_year/248/248170/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/248/248170/2023.csv", "profile_path": "atlas/symbol_profiles/248/248170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-07", "entry_price": 29300, "MFE_30D_pct": 67.41, "MFE_90D_pct": 67.41, "MFE_180D_pct": 67.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.02, "MAE_90D_pct": -14.33, "MAE_180D_pct": -14.33, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-19", "peak_price": 49050, "drawdown_after_peak_pct": -48.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "food_safety_inventory_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_248170_SAUCE_2023-06-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L11_C31_248170_4B_20230620", "case_id": "R12L11_C31_248170_SAUCE", "symbol": "248170", "company_name": "샘표식품", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_GRAIN_AND_FUKUSHIMA_HOARDING_EVENT_BRIDGE_GUARD", "sector": "food_security_life_service_policy_event", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2023-06-20", "evidence_available_at_that_date": "After the blowoff day, upside was capped and downside widened; without non-price 4B evidence this remains overlay rather than full thesis break.", "evidence_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/248/248170/2023.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/248/248170/2023.csv", "profile_path": "atlas/symbol_profiles/248/248170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-20", "entry_price": 42300, "MFE_30D_pct": 11.11, "MFE_90D_pct": 11.11, "MFE_180D_pct": 11.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -28.72, "MAE_90D_pct": -40.66, "MAE_180D_pct": -40.66, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-20", "peak_price": 47000, "drawdown_after_peak_pct": -46.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.66, "four_b_full_window_peak_proximity": 0.66, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_exit", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_event_cap_4B_watch", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L11_C31_248170_SAUCE_20230607", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_008040_GRAIN", "trigger_id": "R12L11_C31_008040_STAGE2A_20220224", "symbol": "008040", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 16, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable_with_C31_route_bonus", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 107.12, "MAE_90D_pct": -9.36, "score_return_alignment_label": "positive_route_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_008040_GRAIN", "trigger_id": "R12L11_C31_008040_GREEN_20220418", "symbol": "008040", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 5, "relative_strength_score": 16, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 5, "relative_strength_score": 16, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 13, "execution_risk_score": 16, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow_high_MAE_watch", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 47.86, "MAE_90D_pct": -26.47, "score_return_alignment_label": "green_lateness_or_high_mae_guard", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_218150_FEED", "trigger_id": "R12L11_C31_218150_STAGE2A_20220224", "symbol": "218150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 5, "relative_strength_score": 16, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 16, "revision_score": 5, "relative_strength_score": 16, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable_with_C31_route_bonus", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 59.46, "MAE_90D_pct": -19.04, "score_return_alignment_label": "positive_route_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_218150_FEED", "trigger_id": "R12L11_C31_218150_GREEN_20220322", "symbol": "218150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 15, "valuation_repricing_score": 13, "execution_risk_score": 16, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow_high_MAE_watch", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 9.79, "MAE_90D_pct": -36.6, "score_return_alignment_label": "green_lateness_or_high_mae_guard", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_277410_SALT", "trigger_id": "R12L11_C31_277410_STAGE2WATCH_20230607", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 14, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable_false_positive_if_unguarded", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 26, "execution_risk_score": 24, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2_event_premium_risk_watch", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 72.35, "MAE_90D_pct": -25.1, "score_return_alignment_label": "false_positive_guarded", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_277410_SALT", "trigger_id": "R12L11_C31_277410_4B_20230615", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 14, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow_or_Green_if_price_only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 28, "execution_risk_score": 24, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B_overlay", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 8.38, "MAE_90D_pct": -52.9, "score_return_alignment_label": "4B_overlay_alignment_improved", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_248170_SAUCE", "trigger_id": "R12L11_C31_248170_STAGE2WATCH_20230607", "symbol": "248170", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 14, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable_false_positive_if_unguarded", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 26, "execution_risk_score": 24, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2_event_premium_risk_watch", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 67.41, "MAE_90D_pct": -14.33, "score_return_alignment_label": "false_positive_guarded", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L11_C31_248170_SAUCE", "trigger_id": "R12L11_C31_248170_4B_20230620", "symbol": "248170", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 14, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow_or_Green_if_price_only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 15, "valuation_repricing_score": 28, "execution_risk_score": 24, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B_overlay", "changed_components": ["margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31 shadow profile rewards event-to-consumption/procurement route and discounts hoarding/fear spikes without repeat-order, pricing, or margin bridge evidence.", "MFE_90D_pct": 11.11, "MAE_90D_pct": -40.66, "score_return_alignment_label": "4B_overlay_alignment_improved", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R12", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["food_safety_hoarding_false_positive", "late_green_high_mae", "event_route_positive_vs_theme_counterexample_split"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R12
completed_loop = 11
next_round = R13
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, max date `2026-02-20`.
- Stock-Web schema: `atlas/schema.json`; MFE/MAE definitions follow tradable-row high/low windows.
- Price shards inspected: `008040/2022.csv`, `218150/2022.csv`, `277410/2023.csv`, `248170/2023.csv`, and `248170/2024.csv` for forward window check.
- Profiles inspected: `008040`, `218150`, `277410`, `248170`.
- Historical event context: Russia/Ukraine food-price shock and Fukushima treated-water/salt-hoarding food-safety event.

