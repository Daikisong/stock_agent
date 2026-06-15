# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
selected_round: R8
selected_loop: 92
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_BLOCKCHAIN_IP_GLOBAL_MONETIZATION_EVENT_RERATING_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent C27 rows and, after local loop 83, moves C27 from projected 27 rows to projected 30 rows.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C27:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R8 -> L8_PLATFORM_CONTENT_SW_SECURITY
C27 -> C27_CONTENT_IP_GLOBAL_MONETIZATION
```

C27 is not “well-known IP exists.” It is the monetization bridge from content/game/fandom visibility into bookings, ARPU, live-service retention, recurring monetization, global distribution, operating leverage, and cash conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C27 rows | 24 |
| static C27 symbols | 17 |
| static C27 good/bad Stage2 | 6 / 7 |
| static C27 4B/4C | 3 / 3 |
| static C27 URL pending/proxy | 24 / 15 |
| static top covered symbols | 035760, 251270, 035900, 194480, 419530, 036420 |
| local C27 loop 83 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid both the static top-covered C27 list and local loop 83 C27 symbols `259960`, `263750`, and `352820`.

| symbol | company | status |
|---|---|---|
| 112040 | 위메이드 | new C27 symbol versus static top-covered and local C27 loop |
| 293490 | 카카오게임즈 | new C27 symbol versus static top-covered and local C27 loop |
| 122870 | 와이지엔터테인먼트 | new C27 symbol versus static top-covered and local C27 loop |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated loop memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 112040 / 2024-03-11 | true | true | clean_180D_window | true |
| 293490 / 2024-01-11 | true | true | clean_180D_window | true |
| 122870 / 2024-03-11 | true | true | clean_180D_window | true |

Corporate-action notes:

- 위메이드 has corporate-action candidates only in 2012 and 2021; selected 2024 window is clean.
- 카카오게임즈 has zero corporate-action candidates.
- 와이지엔터테인먼트 has corporate-action candidates only in 2012 and 2014; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GAME_BLOCKCHAIN_IP_GLOBAL_MONETIZATION_EVENT_RERATING_4B_WATCH | C27 | game/platform IP can rerate violently, but bookings/recurring monetization must follow |
| GAME_IP_LINEUP_EVENT_PREMIUM_WITHOUT_BOOKINGS_BRIDGE | C27 | game lineup premium without bookings/live-service retention is false-positive risk |
| MUSIC_FANDOM_IP_LINEUP_WITHOUT_OPERATING_LEVERAGE_BRIDGE | C27 | fandom/music IP narrative needs revenue revision and operating leverage |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C27_WEMADE_112040_2024_03_11_GAME_BLOCKCHAIN_IP_MONETIZATION_RERATING | 112040 | 위메이드 | 4B_overlay_success | positive | high MFE, then event-crowding drawdown; requires 4B audit |
| C27_KAKAOGAMES_293490_2024_01_11_GAME_IP_LINEUP_PREMIUM_FALSE_POSITIVE | 293490 | 카카오게임즈 | failed_rerating | counterexample | lineup premium had almost no MFE and persistent MAE |
| C27_YG_122870_2024_03_11_MUSIC_FANDOM_IP_LINEUP_REVISION_LAG | 122870 | 와이지엔터테인먼트 | failed_rerating | counterexample | fandom/IP lineup premium had single-digit MFE and later high MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 112040 | source_proxy_only | game/blockchain IP and monetization-event rerating; bookings bridge pending | required before promotion |
| 293490 | source_proxy_only | game IP lineup premium but bookings/live-service bridge absent | required; useful as counterexample |
| 122870 | source_proxy_only | music/fandom IP lineup narrative but revenue-revision bridge lagged | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 112040 | atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv | atlas/symbol_profiles/112/112040.json |
| 293490 | atlas/ohlcv_tradable_by_symbol_year/293/293490/2024.csv | atlas/symbol_profiles/293/293490.json |
| 122870 | atlas/ohlcv_tradable_by_symbol_year/122/122870/2024.csv | atlas/symbol_profiles/122/122870.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| WEMADE_112040_2024_03_11_STAGE2A_GAME_BLOCKCHAIN_IP_MONETIZATION | Stage2-Actionable | 2024-03-11 | 2024-03-11 | 55000 | game/blockchain IP monetization event |
| KAKAOGAMES_293490_2024_01_11_STAGE2_FALSE_POSITIVE_GAME_IP_LINEUP | Stage2 | 2024-01-11 | 2024-01-11 | 27200 | game lineup premium without bookings bridge |
| YG_122870_2024_03_11_STAGE2_FALSE_POSITIVE_FANDOM_IP_LINEUP | Stage2 | 2024-03-11 | 2024-03-11 | 43800 | fandom/music IP lineup without revenue revision bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 112040 | 2024-03-11 | 55000 | 46.36 | -17.45 | 46.36 | -28.18 | 46.36 | -46.91 | 2024-03-20 | 80500 | -63.73 |
| 293490 | 2024-01-11 | 27200 | 1.84 | -11.40 | 1.84 | -26.62 | 1.84 | -39.67 | 2024-01-12 | 27700 | -45.85 |
| 122870 | 2024-03-11 | 43800 | 9.47 | -4.57 | 9.47 | -13.13 | 9.47 | -31.62 | 2024-04-01 | 47950 | -37.54 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 112040 | Stage2A/Yellow possible; 4B after event rerating | high MFE but high MAE and deep peak drawdown | current_profile_4B_too_late |
| 293490 | Stage2 risk if IP lineup premium is over-credited | near-zero MFE and persistent MAE | current_profile_false_positive |
| 122870 | Stage2 risk if fandom lineup narrative is over-credited | single-digit MFE and high 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C27 interpretation:

- Stage2A can work when IP monetization is attached to bookings, ARPU, live-service retention, recurring monetization, or global distribution conversion.
- Yellow/Green require monetization and operating-leverage evidence.
- IP lineup, launch event, or fandom recovery without that bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 112040 | 1.00 | 1.00 | event crowding / valuation | high-MFE event rerating requires 4B audit |
| 293490 | 1.00 | 1.00 | lineup event premium / weak follow-through | not Stage3 without bookings bridge |
| 122870 | 1.00 | 1.00 | fandom lineup event premium / revision lag | not Stage3 without revenue revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 112040 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 293490 | hard_4c_late | bookings/live-service bridge absence should have capped Stage2 earlier |
| 122870 | hard_4c_late | revenue-revision/operating leverage bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L8_PLATFORM_CONTENT_SW_SECURITY
confidence = medium
```

Candidate:

> In L8 content/platform names, content IP, game lineup, or fandom visibility can open a research route, but Stage2A requires monetization evidence: bookings, ARPU, live-service retention, recurring revenue, distribution conversion, or operating leverage. Without that bridge, event premiums should be capped at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C27_CONTENT_IP_GLOBAL_MONETIZATION
confidence = medium
```

Candidate C27 rule:

```text
C27_monetization_bridge_required =
  content_or_game_or_fandom_ip
  AND (bookings_growth OR arpu_bridge OR live_service_retention OR recurring_monetization OR distribution_expansion OR operating_leverage)

if ip_lineup_or_launch_event_premium and monetization_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 40 and drawdown_after_peak < -35:
    add C27_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_90D < -10:
    classify_as C27_ip_monetization_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 19.22 | -22.64 | 19.22 | -39.4 | 2 | useful but C27 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 19.22 | -22.64 | 19.22 | -39.4 | 2 | over-credits IP/lineup/event narratives |
| P1 sector_specific_candidate_profile | L8 | 1 promoted + 2 guard | 46.36 | -28.18 | 46.36 | -46.91 | 0 | better after monetization bridge gate |
| P2 canonical_archetype_candidate_profile | C27 | 1 promoted + 2 guard | 46.36 | -28.18 | 46.36 | -46.91 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C27 guard | 1 promoted + 2 guard | 46.36 | -28.18 | 46.36 | -46.91 | 0 | adds IP monetization false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 112040 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 293490 | Stage2 false positive if bookings bridge not enforced | current_profile_false_positive |
| 122870 | Stage2 false positive if operating-leverage bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | mixed C27 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 24 -> local projected 27 -> projected 30; reaches minimum stability threshold |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C27_monetization_bridge_required|C27_peak_proximity_4B_audit|C27_ip_monetization_false_positive_guardrail
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses clean 180D windows.
- Uses C27 Priority 0 coverage gap.
- Avoids static C27 top-covered symbols and local loop 83 C27 symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_monetization_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"293490/122870 show game/music IP lineup premiums fail without bookings/revenue-revision bridge while 112040 works only as Stage2A with 4B audit","blocks two false positives while preserving 112040 Stage2A","WEMADE_112040_2024_03_11_STAGE2A_GAME_BLOCKCHAIN_IP_MONETIZATION|KAKAOGAMES_293490_2024_01_11_STAGE2_FALSE_POSITIVE_GAME_IP_LINEUP|YG_122870_2024_03_11_STAGE2_FALSE_POSITIVE_FANDOM_IP_LINEUP",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C27_peak_proximity_4B_audit,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"112040 high-MFE game/blockchain IP rerating still needed 4B audit after event crowding","adds 4B audit after large C27 MFE without converting price-only event crowding into Green","WEMADE_112040_2024_03_11_STAGE2A_GAME_BLOCKCHAIN_IP_MONETIZATION",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C27_ip_monetization_false_positive_guardrail,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"293490/122870 had low MFE and high MAE after IP lineup/fandom premium","requires bookings/ARPU/live-service/revenue-revision bridge before Stage2/Yellow promotion","KAKAOGAMES_293490_2024_01_11_STAGE2_FALSE_POSITIVE_GAME_IP_LINEUP|YG_122870_2024_03_11_STAGE2_FALSE_POSITIVE_FANDOM_IP_LINEUP",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C27_WEMADE_112040_2024_03_11_GAME_BLOCKCHAIN_IP_MONETIZATION_RERATING","symbol":"112040","company_name":"위메이드","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_BLOCKCHAIN_IP_GLOBAL_MONETIZATION_EVENT_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"WEMADE_112040_2024_03_11_STAGE2A_GAME_BLOCKCHAIN_IP_MONETIZATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"game/blockchain IP monetization and event rerating captured 46% MFE, but later peak-to-drawdown exceeded 60%, requiring C27 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C27 symbol versus static top-covered list and local C27 loop 83; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C27_KAKAOGAMES_293490_2024_01_11_GAME_IP_LINEUP_PREMIUM_FALSE_POSITIVE","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_LINEUP_EVENT_PREMIUM_WITHOUT_BOOKINGS_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"KAKAOGAMES_293490_2024_01_11_STAGE2_FALSE_POSITIVE_GAME_IP_LINEUP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"game IP/lineup event premium produced almost no MFE and then persistent MAE because bookings/live-service monetization bridge was absent","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C27 symbol; counterexample for lineup/event premium without ARPU, bookings, live-service retention, or operating-leverage proof"}
{"row_type":"case","case_id":"C27_YG_122870_2024_03_11_MUSIC_FANDOM_IP_LINEUP_REVISION_LAG","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MUSIC_FANDOM_IP_LINEUP_WITHOUT_OPERATING_LEVERAGE_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"YG_122870_2024_03_11_STAGE2_FALSE_POSITIVE_FANDOM_IP_LINEUP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"music/fandom IP lineup premium had only single-digit MFE before 30%+ MAE because operating-leverage and revenue-revision bridge lagged","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C27 symbol; selected 2024 window is clear of older corporate-action candidates"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"WEMADE_112040_2024_03_11_STAGE2A_GAME_BLOCKCHAIN_IP_MONETIZATION","case_id":"C27_WEMADE_112040_2024_03_11_GAME_BLOCKCHAIN_IP_MONETIZATION_RERATING","symbol":"112040","company_name":"위메이드","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_BLOCKCHAIN_IP_GLOBAL_MONETIZATION_EVENT_RERATING_4B_WATCH","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-11","entry_date":"2024-03-11","entry_price":55000.0,"evidence_available_at_that_date":"source_proxy_only: game IP, blockchain/platform monetization event, global distribution expectation, and sharp relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["game_ip_route","blockchain_platform_monetization_route","global_distribution_expectation","relative_strength"],"stage3_evidence_fields":["bookings_bridge_pending","recurring_monetization_pending","margin_bridge_pending"],"stage4b_evidence_fields":["event_crowding","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":46.36,"MFE_90D_pct":46.36,"MFE_180D_pct":46.36,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-17.45,"MAE_90D_pct":-28.18,"MAE_180D_pct":-46.91,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-20","peak_price":80500.0,"drawdown_after_peak_pct":-63.73,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_Stage2A_but_extreme_event_rerating_requires_C27_4B_audit","four_b_evidence_type":["event_crowding","valuation_rerating"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_112040_2024_03_11_55000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KAKAOGAMES_293490_2024_01_11_STAGE2_FALSE_POSITIVE_GAME_IP_LINEUP","case_id":"C27_KAKAOGAMES_293490_2024_01_11_GAME_IP_LINEUP_PREMIUM_FALSE_POSITIVE","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_LINEUP_EVENT_PREMIUM_WITHOUT_BOOKINGS_BRIDGE","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":27200.0,"evidence_available_at_that_date":"source_proxy_only: game IP lineup and launch/event premium visible, but bookings, live-service retention, ARPU, and margin bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["game_ip_lineup_premium","launch_event_expectation","relative_strength_short_burst"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","weak_follow_through","monetization_bridge_absent"],"stage4c_evidence_fields":["bookings_bridge_absent","live_service_retention_absent","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2024.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.84,"MFE_90D_pct":1.84,"MFE_180D_pct":1.84,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.4,"MAE_90D_pct":-26.62,"MAE_180D_pct":-39.67,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-12","peak_price":27700.0,"drawdown_after_peak_pct":-45.85,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"game_ip_event_premium_not_stage3_without_bookings_live_service_bridge","four_b_evidence_type":["event_premium","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bookings_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_293490_2024_01_11_27200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"YG_122870_2024_03_11_STAGE2_FALSE_POSITIVE_FANDOM_IP_LINEUP","case_id":"C27_YG_122870_2024_03_11_MUSIC_FANDOM_IP_LINEUP_REVISION_LAG","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MUSIC_FANDOM_IP_LINEUP_WITHOUT_OPERATING_LEVERAGE_BRIDGE","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-11","entry_date":"2024-03-11","entry_price":43800.0,"evidence_available_at_that_date":"source_proxy_only: music/fandom IP lineup and global distribution narrative visible, but touring/album revenue conversion, margin, and revision bridge lagged","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["music_fandom_ip_route","lineup_recovery_narrative","global_distribution_expectation"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["lineup_event_premium","revision_bridge_absent"],"stage4c_evidence_fields":["operating_leverage_bridge_absent","revenue_revision_lag","trust_or_lineup_execution_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122870/2024.csv","profile_path":"atlas/symbol_profiles/122/122870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.47,"MFE_90D_pct":9.47,"MFE_180D_pct":9.47,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.57,"MAE_90D_pct":-13.13,"MAE_180D_pct":-31.62,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":47950.0,"drawdown_after_peak_pct":-37.54,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fandom_ip_lineup_premium_not_stage3_without_revenue_revision_operating_leverage_bridge","four_b_evidence_type":["lineup_event_premium","revision_bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_single_digit_mfe_high_mae_revision_lag","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_122870_2024_03_11_43800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_WEMADE_112040_2024_03_11_GAME_BLOCKCHAIN_IP_MONETIZATION_RERATING","trigger_id":"WEMADE_112040_2024_03_11_STAGE2A_GAME_BLOCKCHAIN_IP_MONETIZATION","symbol":"112040","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":10,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":10,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-watch / 4B audit, not Yellow","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"High-MFE game/blockchain IP rerating worked, but C27 Green requires bookings/recurring monetization bridge and peak-proximity audit.","MFE_90D_pct":46.36,"MAE_90D_pct":-28.18,"score_return_alignment_label":"positive_but_high_mae_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_KAKAOGAMES_293490_2024_01_11_GAME_IP_LINEUP_PREMIUM_FALSE_POSITIVE","trigger_id":"KAKAOGAMES_293490_2024_01_11_STAGE2_FALSE_POSITIVE_GAME_IP_LINEUP","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Game IP/lineup premium without bookings/live-service bridge produced almost no MFE and persistent drawdown.","MFE_90D_pct":1.84,"MAE_90D_pct":-26.62,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_YG_122870_2024_03_11_MUSIC_FANDOM_IP_LINEUP_REVISION_LAG","trigger_id":"YG_122870_2024_03_11_STAGE2_FALSE_POSITIVE_FANDOM_IP_LINEUP","symbol":"122870","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive / lineup risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Music/fandom IP lineup premium needed revenue revision and operating-leverage bridge before Stage2/Yellow promotion.","MFE_90D_pct":9.47,"MAE_90D_pct":-13.13,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R8
completed_loop = 92
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

If this loop is accepted together with local loop 83, C27 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C27 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/293/293490/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/122/122870/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/112/112040.json
  - atlas/symbol_profiles/293/293490.json
  - atlas/symbol_profiles/122/122870.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
