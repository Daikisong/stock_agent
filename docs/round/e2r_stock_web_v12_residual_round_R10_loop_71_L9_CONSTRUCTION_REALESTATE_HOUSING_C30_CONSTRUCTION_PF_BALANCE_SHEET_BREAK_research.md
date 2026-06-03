# E2R Stock-Web v12 Residual Research — R10 Loop 71 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 71
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_LIQUIDITY_BREAK_VS_REPAIR_CAPITAL_BRIDGE_AND_SUSPENSION_CONTAMINATION
sector: 건설·부동산·주택·PF
output_file: e2r_stock_web_v12_residual_round_R10_loop_71_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the sequential v12 scheduler after the prior R9/L3 mobility research. The scheduled target is therefore:

```text
scheduled_round = R10
scheduled_loop = 71
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

This is not a live candidate scan, not a recommendation file, and not a `stock_agent` patch. It is a standalone historical calibration note using `Songdaiki/stock-web` 1D tradable raw OHLC rows.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","notes":"Manifest confirms raw/unadjusted OHLC, tradable shard root, full atlas committed, and corporate-action-contaminated windows blocked by default."}
```

Ticker profile checks used in this run:

```jsonl
{"row_type":"price_source_validation","symbol":"009410","name":"태영건설","profile_path":"atlas/symbol_profiles/009/009410.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7576,"corporate_action_candidate_dates":["2007-05-03","2020-09-22","2024-10-31"],"calibration_caveat":"Corporate-action candidate windows are blocked by default.","status_inferred":"active_like"}
{"row_type":"price_source_validation","symbol":"034300","name":"신세계건설","profile_path":"atlas/symbol_profiles/034/034300.json","first_date":"1999-06-25","last_date":"2025-01-24","trading_day_count":6312,"corporate_action_candidate_dates":["1999-11-16","2024-02-06"],"calibration_caveat":"Corporate-action candidate windows are blocked by default.","status_inferred":"inactive_or_delisted_like"}
{"row_type":"price_source_validation","symbol":"002990","name":"금호건설","profile_path":"atlas/symbol_profiles/002/002990.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7708,"corporate_action_candidate_dates":["1999-03-22","2000-01-11","2010-04-29","2010-11-24","2012-03-22","2013-03-28","2013-11-07"],"calibration_caveat":"Corporate-action candidate windows are blocked by default.","status_inferred":"active_like"}
{"row_type":"price_source_validation","symbol":"014790","name":"HL D&I","profile_path":"atlas/symbol_profiles/014/014790.json","first_date":"1995-05-03","last_date":"2026-02-20","trading_day_count":7728,"corporate_action_candidate_dates":["1996-01-03","1997-11-03","1997-12-27","1999-12-21","2010-04-28","2012-02-06"],"calibration_caveat":"Corporate-action candidate windows are blocked by default.","status_inferred":"active_like"}
```

## 3. No-repeat and novelty check

The no-repeat index snapshot lists `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` as already covered by 113 rows, 34 symbols, and date range `2021-03-11~2024-09-30`; the top repeated symbols are `006360`, `UNKNOWN_SYMBOL`, `294870`, `047040`, `000720`, and `375500`. This run deliberately avoids reusing those top-covered C30 keys and focuses on `009410`, `034300`, `002990`, and `014790`.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novel keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"009410","trigger_type":"Stage4C-PF-liquidity-workout-break","entry_date":"2023-12-28","duplicate_status":"not_found_in_top_covered_symbols; allowed as new/under-covered hard-4C liquidity break key"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"034300","trigger_type":"DataQuality-Repair-CapitalInjection-ShareCountBreak","entry_date":"2024-01-18","duplicate_status":"not_found_in_top_covered_symbols; allowed as data-quality repair / corporate-action contamination key"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","trigger_type":"Stage2-FalsePositive-PF-Overhang-NoRepairBridge","entry_date":"2024-01-31","duplicate_status":"new symbol expansion against C30 top list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","trigger_type":"Stage2-RepairBridge-Counterexample","entry_date":"2024-01-31","duplicate_status":"new symbol expansion against C30 top list"}
```

## 4. Case thesis

C30 is not a normal cyclical construction recovery archetype. It behaves more like a bridge inspection after an earthquake: visible valuation cheapness can be real, but if the bridge piers are PF debt, guarantee exposure, refinancing, project-quality defect, or capital support, the first task is not to admire the low multiple; it is to check whether the structure can carry traffic.

The residual question for this loop:

```text
Can the calibrated E2R profile distinguish:
1. hard liquidity-break / workout / suspension paths,
2. corporate-action-contaminated capital repair paths,
3. low-PBR/PF-overhang false-positive drift paths,
4. genuine repair-bridge counterexamples where the price path recovers without hard 4C?
```

## 5. Trigger-level Stock-Web rows

### 5.1 009410 태영건설 — workout/liquidity break, price path contaminated after suspension/restructuring

Stock-Web rows confirm a hard price break into 2023-12-28 and then a high-volatility January rebound before a tradable-row gap until 2024-10-31. The profile lists `2024-10-31` as a corporate-action candidate, so 90D/180D calibration must be blocked even though the short-term path produced a large MFE.

Key rows observed:

```text
2023-12-27: o=2780 h=2960 l=2380 c=2405 v=3935359
2023-12-28: o=1940 h=3005 l=1935 c=2315 v=34856588
2024-01-02: o=2280 h=2780 l=2275 c=2620
2024-01-03: o=3100 h=3405 l=2800 c=3245
2024-01-11: o=3475 h=4110 l=3400 c=3765
2024-03-13: o=2305 h=2325 l=2290 c=2310
2024-10-31: o=4700 h=6110 l=4275 c=4435, shares jump to 287905337; corporate_action_candidate_date
```

```jsonl
{"row_type":"trigger","case_id":"C30_R10L71_009410_TAEYOUNG_WORKOUT_BREAK","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_WORKOUT_SUSPENSION_CONTAMINATION","symbol":"009410","company_name":"태영건설","trigger_type":"Stage4C-PF-liquidity-workout-break","trigger_date":"2023-12-28","entry_date":"2023-12-28","entry_price":2315.0,"entry_price_basis":"close","price_basis":"tradable_raw","entry_row_exists":true,"MFE_30D_pct":77.54,"MAE_30D_pct":-16.41,"MFE_90D_pct":null,"MAE_90D_pct":null,"MFE_180D_pct":null,"MAE_180D_pct":null,"peak_date_30D":"2024-01-11","peak_price_30D":4110.0,"max_drawdown_low_30D_date":"2023-12-28","max_drawdown_low_30D":1935.0,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":true,"window_180D_corporate_action_contaminated":true,"calibration_usable":false,"blocked_reason":"corporate_action_or_restructuring_contaminated_forward_window_after_2024-10-31_plus_tradable_gap","evidence_url_pending":true,"source_proxy_only":true,"current_profile_residual":"Short-term rebound can look like 4B/mean-reversion if price-only; must be hard-routed to 4C/liquidity-break until post-restructuring capital structure is separated."}
```

### 5.2 034300 신세계건설 — capital-support/repair path, share-count break contaminates clean calibration

The 2024-02-06 Stock-Web profile and shard rows show a share-count/marcap break: shares move from 4,000,000 to 7,760,554. The local path around January/February is therefore useful as a data-quality repair and rule-design case, but it must not be used as a clean positive/negative weight-calibration row.

Key rows observed:

```text
2024-01-18: o=11190 h=13920 l=10730 c=12600 v=831111
2024-01-31: o=10690 h=11210 l=10650 c=11170 shares=4000000
2024-02-05: o=11380 h=12100 l=11270 c=11880 shares=4000000
2024-02-06: o=11870 h=11870 l=11310 c=11310 shares=7760554, profile corporate-action candidate
2024-02-16: o=12270 h=12750 l=11980 c=12670 shares=7760554
```

```jsonl
{"row_type":"trigger","case_id":"C30_R10L71_034300_SHINSEGAE_CONSTRUCTION_CAPITAL_REPAIR_BLOCKED","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CAPITAL_SUPPORT_REPAIR_WITH_SHARECOUNT_BREAK","symbol":"034300","company_name":"신세계건설","trigger_type":"DataQuality-Repair-CapitalInjection-ShareCountBreak","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":12600.0,"entry_price_basis":"close","price_basis":"tradable_raw","entry_row_exists":true,"MFE_30D_pct":10.48,"MAE_30D_pct":-16.67,"MFE_90D_pct":null,"MAE_90D_pct":null,"MFE_180D_pct":null,"MAE_180D_pct":null,"peak_date_30D":"2024-02-16","peak_price_30D":12750.0,"max_drawdown_low_30D_date":"2024-01-29","max_drawdown_low_30D":10100.0,"window_30D_corporate_action_contaminated":true,"window_90D_corporate_action_contaminated":true,"window_180D_corporate_action_contaminated":true,"calibration_usable":false,"blocked_reason":"profile_corporate_action_candidate_2024-02-06_inside_forward_window_share_count_break","evidence_url_pending":true,"source_proxy_only":true,"current_profile_residual":"Capital repair may be valid evidence, but raw-unadjusted OHLC requires blocking the trigger from weight calibration and routing it to data-repair/capital-structure-note."}
```

### 5.3 002990 금호건설 — low-multiple/PF-overhang false positive without repair bridge

This case is a clean tradable-path stress test. The price starts near 5,210 at the 2024-01-31 trigger and then bleeds almost continuously. Any C30 logic that rewards construction cheapness or late-stage low P/B without a visible balance-sheet repair bridge would have generated a false Stage2/Yellow impression.

Key rows observed:

```text
2024-01-31: o=5200 h=5210 l=5100 c=5210
2024-02-01: h=5280
2024-03-15: l=4615
2024-06-13: l=3645
2024-08-05: l=3205
2024-10-25: l=2850
```

```jsonl
{"row_type":"trigger","case_id":"C30_R10L71_002990_KUMHO_FALSE_POSITIVE_PF_OVERHANG","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LOW_MULTIPLE_PF_OVERHANG_WITHOUT_REPAIR_BRIDGE","symbol":"002990","company_name":"금호건설","trigger_type":"Stage2-FalsePositive-PF-Overhang-NoRepairBridge","trigger_date":"2024-01-31","entry_date":"2024-01-31","entry_price":5210.0,"entry_price_basis":"close","price_basis":"tradable_raw","entry_row_exists":true,"MFE_30D_pct":1.34,"MAE_30D_pct":-11.42,"MFE_90D_pct":1.34,"MAE_90D_pct":-30.04,"MFE_180D_pct":1.34,"MAE_180D_pct":-45.30,"peak_date_180D":"2024-02-01","peak_price_180D":5280.0,"max_drawdown_low_180D_date":"2024-10-25","max_drawdown_low_180D":2850.0,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"data_quality_label":"clean_tradable_path","evidence_url_pending":true,"source_proxy_only":true,"current_profile_residual":"C30 false positive if valuation/cheapness is allowed to substitute for non-price balance-sheet repair evidence."}
```

### 5.4 014790 HL D&I — repair-bridge counterexample / not every PF-overhang name is hard 4C

HL D&I provides the counterweight. The initial C30 surface condition can look similar—small construction balance sheet, PF sensitivity, low base—but the path did not behave like a hard liquidity break. From 2024-01-31, drawdown was contained and the stock later staged a sizable local recovery.

Key rows observed:

```text
2024-01-31: o=2045 h=2090 l=2035 c=2075
2024-02-01: h=2230
2024-04-17: l=1928
2024-06-20: h=2660
2024-08-23: h=2880
```

```jsonl
{"row_type":"trigger","case_id":"C30_R10L71_014790_HLDNI_REPAIR_BRIDGE_COUNTEREXAMPLE","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_REPAIR_BRIDGE_COUNTEREXAMPLE","symbol":"014790","company_name":"HL D&I","trigger_type":"Stage2-RepairBridge-Counterexample","trigger_date":"2024-01-31","entry_date":"2024-01-31","entry_price":2075.0,"entry_price_basis":"close","price_basis":"tradable_raw","entry_row_exists":true,"MFE_30D_pct":7.47,"MAE_30D_pct":-4.53,"MFE_90D_pct":28.19,"MAE_90D_pct":-7.08,"MFE_180D_pct":38.80,"MAE_180D_pct":-7.08,"peak_date_180D":"2024-08-23","peak_price_180D":2880.0,"max_drawdown_low_180D_date":"2024-04-17","max_drawdown_low_180D":1928.0,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"data_quality_label":"clean_tradable_path","evidence_url_pending":true,"source_proxy_only":true,"current_profile_residual":"C30 should not hard-4C every small construction name. Need a repair/no-acute-liquidity-breach bridge to allow Stage2 or local 4B watch."}
```

## 6. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L71_009410_TAEYOUNG_WORKOUT_BREAK","case_role":"hard_4c_liquidity_break_blocked_by_restructuring_contamination","symbol":"009410","company_name":"태영건설","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_count":1,"usable_trigger_count":0,"blocked_trigger_count":1,"classification":"hard_4C_not_weight_calibration","lesson":"When workout/liquidity break is visible, price-only rebound must not unlock 4B/Stage2; post-restructuring share-count discontinuity must be separated."}
{"row_type":"case","case_id":"C30_R10L71_034300_SHINSEGAE_CONSTRUCTION_CAPITAL_REPAIR_BLOCKED","case_role":"capital_repair_data_quality_block","symbol":"034300","company_name":"신세계건설","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_count":1,"usable_trigger_count":0,"blocked_trigger_count":1,"classification":"data_quality_repair_required","lesson":"Capital-support events can be the right non-price bridge, but raw OHLC with share-count break is not usable for clean return calibration."}
{"row_type":"case","case_id":"C30_R10L71_002990_KUMHO_FALSE_POSITIVE_PF_OVERHANG","case_role":"false_positive_guardrail","symbol":"002990","company_name":"금호건설","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_count":1,"usable_trigger_count":1,"blocked_trigger_count":0,"classification":"bad_stage2_false_positive","lesson":"Low valuation and construction-cycle cheapness are not enough when PF repair bridge is absent; the 180D path had almost no upside and -45% MAE."}
{"row_type":"case","case_id":"C30_R10L71_014790_HLDNI_REPAIR_BRIDGE_COUNTEREXAMPLE","case_role":"counterexample_positive_repair_bridge","symbol":"014790","company_name":"HL D&I","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_count":1,"usable_trigger_count":1,"blocked_trigger_count":0,"classification":"good_stage2_or_local_repair_watch","lesson":"C30 guardrail must distinguish acute liquidity break from repairable overhang; this clean path shows low MAE and strong 180D MFE."}
```

## 7. Score simulation rows

These component scores are shadow diagnostics, not production scores. They model how a sector-specific C30 overlay should respond.

```jsonl
{"row_type":"score_simulation","case_id":"C30_R10L71_009410_TAEYOUNG_WORKOUT_BREAK","symbol":"009410","profile_proxy":"e2r_2_1_stock_web_calibrated","eps_fcf_explosion":5,"earnings_visibility":10,"bottleneck_pricing":0,"market_mispricing":15,"valuation_rerating":5,"capital_allocation":0,"information_confidence":70,"c30_pf_liquidity_break_penalty":-45,"c30_repair_bridge_bonus":0,"price_only_blowoff_block":true,"simulated_total_after_c30_overlay":60,"stage_before_overlay":"Stage2/4B-confused-if-price-only","stage_after_overlay":"Stage4C-watch/blocked","stress_result":"positive_stage_blocked"}
{"row_type":"score_simulation","case_id":"C30_R10L71_034300_SHINSEGAE_CONSTRUCTION_CAPITAL_REPAIR_BLOCKED","symbol":"034300","profile_proxy":"e2r_2_1_stock_web_calibrated","eps_fcf_explosion":10,"earnings_visibility":15,"bottleneck_pricing":0,"market_mispricing":20,"valuation_rerating":10,"capital_allocation":25,"information_confidence":55,"c30_pf_liquidity_break_penalty":-15,"c30_repair_bridge_bonus":20,"corporate_action_contamination_block":true,"simulated_total_after_c30_overlay":null,"stage_before_overlay":"Stage2/repair-watch","stage_after_overlay":"data_quality_blocked_not_weight","stress_result":"blocked_by_share_count_break"}
{"row_type":"score_simulation","case_id":"C30_R10L71_002990_KUMHO_FALSE_POSITIVE_PF_OVERHANG","symbol":"002990","profile_proxy":"e2r_2_1_stock_web_calibrated","eps_fcf_explosion":5,"earnings_visibility":20,"bottleneck_pricing":0,"market_mispricing":35,"valuation_rerating":20,"capital_allocation":10,"information_confidence":45,"c30_pf_liquidity_break_penalty":-25,"c30_repair_bridge_bonus":0,"simulated_total_before_c30_overlay":65,"simulated_total_after_c30_overlay":40,"stage_before_overlay":"Stage2-Yellow-risk","stage_after_overlay":"Stage1/Red-watch","stress_result":"bad_stage2_blocked"}
{"row_type":"score_simulation","case_id":"C30_R10L71_014790_HLDNI_REPAIR_BRIDGE_COUNTEREXAMPLE","symbol":"014790","profile_proxy":"e2r_2_1_stock_web_calibrated","eps_fcf_explosion":10,"earnings_visibility":35,"bottleneck_pricing":0,"market_mispricing":35,"valuation_rerating":25,"capital_allocation":20,"information_confidence":60,"c30_pf_liquidity_break_penalty":0,"c30_repair_bridge_bonus":20,"simulated_total_before_c30_overlay":65,"simulated_total_after_c30_overlay":80,"stage_before_overlay":"Stage2-Yellow-borderline","stage_after_overlay":"Stage2-Actionable/local-4B-watch","stress_result":"repairable_overhang_allowed_without_green_loosen"}
```

## 8. Aggregate summary

```jsonl
{"row_type":"aggregate","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_rows":4,"usable_trigger_rows":2,"blocked_trigger_rows":2,"positive_or_repair_counterexamples":1,"false_positive_or_hard_break_cases":2,"data_quality_repair_cases":1,"median_usable_MFE_180D_pct":20.07,"median_usable_MAE_180D_pct":-26.19,"interpretation":"C30 residual is not simply bearish or bullish. The overlay needs two gates: hard liquidity-break blocks positive stages; repair/no-acute-liquidity bridge can allow local Stage2 watch if raw OHLC is clean."}
```

The clean usable pair is deliberately asymmetric:

| Symbol | Role | 180D MFE | 180D MAE | Interpretation |
|---|---:|---:|---:|---|
| 002990 | false positive | +1.34% | -45.30% | Cheapness without repair bridge failed. |
| 014790 | repair counterexample | +38.80% | -7.08% | Repairable overhang behaved much better. |

## 9. Residual contribution

```jsonl
{"row_type":"residual_contribution","axis":"stage2_required_bridge","scope":"canonical_archetype","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","candidate_rule":"Require at least one verified non-price balance-sheet repair bridge before C30 can receive Stage2-Actionable or Yellow credit: debt maturity extension, sponsor capital support, credible covenant/refinancing clarity, PF guarantee reduction, or project-loss cap. Valuation cheapness alone is not a bridge.","supporting_cases":["002990","014790"],"counter_cases":["009410","034300"],"promotion_readiness":"hold_for_verified_evidence_urls","why_not_apply_now":"This run uses stock-web price rows cleanly, but several non-price evidence labels remain source_proxy_only/evidence_url_pending; promote only after URL/filing repair."}
{"row_type":"residual_contribution","axis":"hard_4c_confirmation","scope":"canonical_archetype","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","candidate_rule":"If workout/liquidity-break/trading-suspension/capital-structure discontinuity appears, route to 4C or data-quality block even if 30D price MFE is large. Do not let price-only rebound unlock 4B or Stage2.","supporting_cases":["009410","034300"],"promotion_readiness":"apply_after_verified_event_url_repair","why_not_apply_now":"Stock-web confirms price/structure discontinuities; event URLs still pending in this standalone pass."}
```

## 10. Shadow weight suggestion

```jsonl
{"row_type":"shadow_weight","target":"canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","weight_name":"c30_pf_repair_bridge_required","suggested_delta":1.0,"direction":"tighten_positive_stage_entry","applies_to":["Stage2-Actionable","Stage3-Yellow","Stage3-Green"],"rule":"C30 positive stage requires non-price repair bridge; valuation, oversold price, low PBR, or construction-cycle rebound cannot substitute.","expected_effect":"Reduce 002990-like false positives without blocking 014790-like repair counterexamples."}
{"row_type":"shadow_weight","target":"canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","weight_name":"c30_liquidity_break_hard_4c_guard","suggested_delta":1.0,"direction":"strengthen_4c_routing","applies_to":["Stage4C","data_quality_block"],"rule":"Workout, suspension, emergency capital action, or share-count discontinuity routes to 4C/data-quality block before any 4B/Stage2 interpretation.","expected_effect":"Prevents 009410/034300 rebound or recapitalization artifacts from entering positive calibration."}
{"row_type":"shadow_weight","target":"canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","weight_name":"c30_repair_counterexample_local_watch","suggested_delta":0.5,"direction":"allow_selective_repairable_overhang","applies_to":["Stage2","local_4B_watch"],"rule":"If no acute liquidity break and clean Stock-Web path shows contained MAE with repair evidence, allow local watch without loosening Green thresholds.","expected_effect":"Preserves 014790-like counterexamples; avoids turning C30 into a one-way bearish archetype."}
```

## 11. Coverage matrix row

```jsonl
{"row_type":"coverage_matrix","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_BREAK_VS_REPAIR_CAPITAL_BRIDGE_AND_SUSPENSION_CONTAMINATION","symbols_added":["009410","034300","002990","014790"],"new_symbol_count_vs_top_covered_list":4,"case_balance":"1 hard 4C blocked, 1 data-quality capital repair blocked, 1 false positive, 1 repair counterexample","coverage_contribution":"Adds under-covered C30 paths outside the dominant 006360/294870/047040/000720/375500 cluster."}
```

## 12. Validation scope

```text
Validation scope: historical calibration only.
Stock-Web rows used: tradable_raw 1D OHLCV.
Forward-window basis: manifest max_date 2026-02-20.
Clean calibration rows: 002990, 014790.
Blocked rows: 009410 due restructuring/tradable gap/corporate-action candidate; 034300 due 2024-02-06 share-count break.
Non-price evidence status: source_proxy_only/evidence_url_pending in this standalone pass.
Production scoring change: none.
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

When batching v12 MD outputs into stock_agent, ingest this file as a C30 canonical residual candidate.

Tasks:
1. Parse trigger/case/score_simulation/aggregate/shadow_weight/residual_contribution rows.
2. Treat 002990 and 014790 as clean Stock-Web calibration rows.
3. Treat 009410 and 034300 as blocked/data-quality rows, not weight-calibration positives.
4. Add or update C30 rule candidate:
   - C30 positive Stage2/Yellow requires non-price repair bridge.
   - workout/liquidity-break/trading-suspension/share-count discontinuity routes to 4C or data-quality block.
   - repairable overhang can allow local watch but must not loosen Stage3-Green thresholds.
5. Keep source_proxy_only/evidence_url_pending as promotion blockers until event URLs/disclosures are repaired.
6. Do not change production scoring from this file alone.
```

## 14. Next round state

```text
completed_round = R10
completed_loop = 71
next_round = R11
next_loop = 71
```
