# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R8_loop_83_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
selected_round: R8
selected_loop: 83
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_MONETIZATION_OPERATING_LEVERAGE_4B_WATCH
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

This loop adds 3 independent cases, 1 global content/game IP success path, and 2 content/IP event-risk counterexamples for R8/L8/C27.

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

C27 is not “there is famous IP.” It is the bridge from content/IP visibility into bookings, ARPU, global distribution, recurring monetization, margin leverage, and cash conversion. The IP is the door sign; monetization is the cash register actually ringing.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C27 current rows | 24 |
| C27 current symbols | 17 |
| C27 good/bad Stage2 | 6 / 7 |
| C27 4B/4C | 3 / 3 |
| C27 URL pending/proxy | 24 / 15 |
| top covered symbols | 035760, 251270, 035900, 194480, 419530, 036420 |

Selected symbols avoid the C27 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 259960 | 크래프톤 | new C27 symbol versus top-covered C27 list |
| 263750 | 펄어비스 | new C27 symbol versus top-covered C27 list |
| 352820 | 하이브 | new C27 symbol versus top-covered C27 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 259960 / 2024-02-13 | true | true | clean_180D_window | true |
| 263750 / 2024-07-09 | true | true | clean_180D_window | true |
| 352820 / 2024-03-25 | true | true | clean_180D_window | true |

Corporate-action notes:

- 크래프톤 has zero corporate-action candidates.
- 펄어비스 has a corporate-action candidate only in 2021; selected 2024 window is clean.
- 하이브 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GAME_IP_GLOBAL_MONETIZATION_OPERATING_LEVERAGE_4B_WATCH | C27 | global game IP, traffic/ARPU monetization, operating leverage |
| GAME_IP_RELEASE_EVENT_PREMIUM_WITHOUT_MONETIZATION_BRIDGE | C27 | game release event premium without bookings/live-service bridge |
| MUSIC_FANDOM_IP_PLATFORM_GOVERNANCE_EVENT_RISK | C27 | fandom/IP platform narrative with governance/trust and operating-leverage risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C27_KRAFTON_259960_2024_02_13_GAME_IP_GLOBAL_MONETIZATION_RERATING | 259960 | 크래프톤 | structural_success | positive | global IP monetization route produced 54% 180D MFE with contained MAE |
| C27_PEARLABYSS_263750_2024_07_09_GAME_IP_RELEASE_EVENT_FALSE_POSITIVE | 263750 | 펄어비스 | failed_rerating | counterexample | release-event premium had only 3% MFE and high MAE |
| C27_HYBE_352820_2024_03_25_FANDOM_IP_PLATFORM_RISK_FALSE_POSITIVE | 352820 | 하이브 | failed_rerating | counterexample | fandom/IP platform narrative had local MFE but trust/event risk drove drawdown |

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

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 259960 | source_proxy_only | global game IP monetization / operating leverage route | required before promotion |
| 263750 | source_proxy_only | game release event premium but bookings/monetization bridge absent | required; useful as counterexample |
| 352820 | source_proxy_only | fandom IP platform narrative but trust/operating leverage bridge weak | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 259960 | atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv | atlas/symbol_profiles/259/259960.json |
| 263750 | atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv | atlas/symbol_profiles/263/263750.json |
| 352820 | atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv | atlas/symbol_profiles/352/352820.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| KRAFTON_259960_2024_02_13_STAGE2A_GAME_IP_GLOBAL_MONETIZATION | Stage2-Actionable | 2024-02-13 | 2024-02-13 | 230000 | global game IP monetization / operating leverage route |
| PEARLABYSS_263750_2024_07_09_STAGE2_FALSE_POSITIVE_GAME_IP_EVENT | Stage2 | 2024-07-09 | 2024-07-09 | 46200 | game IP release event premium without bookings bridge |
| HYBE_352820_2024_03_25_STAGE2_FALSE_POSITIVE_FANDOM_IP_PLATFORM_RISK | Stage2 | 2024-03-25 | 2024-03-25 | 207000 | fandom/IP platform monetization narrative with trust/event risk |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 259960 | 2024-02-13 | 230000 | 15.22 | -8.48 | 30.00 | -8.48 | 54.35 | -8.48 | 2024-08-22 | 355000 | -9.15 |
| 263750 | 2024-07-09 | 46200 | 3.14 | -20.89 | 3.14 | -27.27 | 3.14 | -30.95 | 2024-07-10 | 47650 | -33.05 |
| 352820 | 2024-03-25 | 207000 | 14.01 | -4.83 | 14.01 | -17.97 | 14.01 | -23.82 | 2024-04-01 | 236000 | -33.18 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 259960 | Stage2A/Yellow possible; 4B after rerating | high MFE with contained MAE | current_profile_4B_too_late |
| 263750 | Stage2 risk if release-event premium is over-credited | low MFE and high MAE | current_profile_false_positive |
| 352820 | Stage2 risk if fandom/platform IP is over-credited | local MFE then event/trust drawdown | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C27 interpretation:

- Stage2A can work when global IP monetization is tied to bookings, traffic, ARPU, operating leverage, or distribution expansion.
- Yellow/Green require revenue conversion, margin durability, and low event/trust risk.
- IP release events or fandom narratives without monetization bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 259960 | 1.00 | 1.00 | valuation / operating leverage | good 4B audit after IP monetization rerating |
| 263750 | 1.00 | 1.00 | release event premium | game IP event premium was not Stage3 |
| 352820 | 1.00 | 1.00 | event/trust risk | fandom IP premium was not enough for Stage2/Yellow |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 259960 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 263750 | hard_4c_late | monetization/bookings bridge absence should have capped Stage2 earlier |
| 352820 | hard_4c_late | governance/trust risk should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L8_PLATFORM_CONTENT_SW_SECURITY
confidence = low_to_medium
```

Candidate:

> In L8 content/platform names, famous IP or release-event visibility can open a research route, but Stage2A requires monetization evidence: bookings, ARPU, live-service retention, distribution scale, or operating leverage. Without that bridge, event premium should be capped at Stage1/Stage2-watch and routed to C27 false-positive or 4C-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C27_CONTENT_IP_GLOBAL_MONETIZATION
confidence = low_to_medium
```

Candidate C27 rule:

```text
C27_monetization_bridge_required =
  content_or_game_or_fandom_ip
  AND (bookings_growth OR arpu_bridge OR recurring_monetization OR distribution_expansion OR operating_leverage)

if ip_release_event_premium and monetization_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if event_or_trust_risk_present and operating_leverage_bridge_absent:
    add C27_event_trust_4C_watch = true

if MFE_90D < 15 and MAE_90D < -15:
    classify_as C27_ip_event_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 15.72 | -17.91 | 23.83 | -21.08 | 2 | useful but C27 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 15.72 | -17.91 | 23.83 | -21.08 | 2 | over-credits IP/event narratives |
| P1 sector_specific_candidate_profile | L8 | 1 promoted + 2 guard | 30.0 | -8.48 | 54.35 | -8.48 | 0 | better after monetization bridge gate |
| P2 canonical_archetype_candidate_profile | C27 | 1 promoted + 2 guard | 30.0 | -8.48 | 54.35 | -8.48 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C27 guard | 1 promoted + 2 guard | 30.0 | -8.48 | 54.35 | -8.48 | 0 | adds IP event false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 259960 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 263750 | Stage2 false positive if event premium is over-credited | current_profile_false_positive |
| 352820 | Stage2 false positive if trust/event risk not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | mixed C27 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | 24 -> projected 27 rows; still need 3 to reach 30 |

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
new_axis_proposed: C27_monetization_bridge_required|C27_event_trust_4C_watch|C27_ip_event_false_positive_guardrail
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
- Uses three symbols not in the C27 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_monetization_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"263750 and 352820 show IP/event narratives can fail without bookings/operating-leverage/trust bridge","blocks two false positives while preserving 259960 Stage2A","KRAFTON_259960_2024_02_13_STAGE2A_GAME_IP_GLOBAL_MONETIZATION|PEARLABYSS_263750_2024_07_09_STAGE2_FALSE_POSITIVE_GAME_IP_EVENT|HYBE_352820_2024_03_25_STAGE2_FALSE_POSITIVE_FANDOM_IP_PLATFORM_RISK",3,3,2,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C27_event_trust_4C_watch,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"352820 shows governance/trust event risk can overwhelm fandom/IP platform narrative","adds 4C watch when event/trust risk appears before operating-leverage bridge","HYBE_352820_2024_03_25_STAGE2_FALSE_POSITIVE_FANDOM_IP_PLATFORM_RISK",1,1,1,low_to_medium,canonical_shadow_only,"4C-watch guardrail"
shadow_weight,C27_ip_event_false_positive_guardrail,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"263750 had low MFE and high MAE after game IP release-event premium","requires bookings/live-service monetization proof before Stage2/Yellow promotion","PEARLABYSS_263750_2024_07_09_STAGE2_FALSE_POSITIVE_GAME_IP_EVENT",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C27_KRAFTON_259960_2024_02_13_GAME_IP_GLOBAL_MONETIZATION_RERATING","symbol":"259960","company_name":"크래프톤","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_MONETIZATION_OPERATING_LEVERAGE_4B_WATCH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"KRAFTON_259960_2024_02_13_STAGE2A_GAME_IP_GLOBAL_MONETIZATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global game IP monetization and operating-leverage route captured 54% 180D MFE with contained MAE, but later peak proximity required 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C27 symbol versus top-covered C27 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C27_PEARLABYSS_263750_2024_07_09_GAME_IP_RELEASE_EVENT_FALSE_POSITIVE","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_RELEASE_EVENT_PREMIUM_WITHOUT_MONETIZATION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"PEARLABYSS_263750_2024_07_09_STAGE2_FALSE_POSITIVE_GAME_IP_EVENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"game release/IP event premium produced only 3% MFE before roughly -27% to -31% MAE when booking/monetization bridge did not appear","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C27 symbol; counterexample for IP release event without global monetization proof"}
{"row_type":"case","case_id":"C27_HYBE_352820_2024_03_25_FANDOM_IP_PLATFORM_RISK_FALSE_POSITIVE","symbol":"352820","company_name":"하이브","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MUSIC_FANDOM_IP_PLATFORM_GOVERNANCE_EVENT_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HYBE_352820_2024_03_25_STAGE2_FALSE_POSITIVE_FANDOM_IP_PLATFORM_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"fandom/IP/platform monetization narrative had 14% local MFE but later governance/event risk drove -22% to -24% MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C27 symbol; counterexample for content IP platform narrative without operating-leverage/governance trust bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"KRAFTON_259960_2024_02_13_STAGE2A_GAME_IP_GLOBAL_MONETIZATION","case_id":"C27_KRAFTON_259960_2024_02_13_GAME_IP_GLOBAL_MONETIZATION_RERATING","symbol":"259960","company_name":"크래프톤","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_MONETIZATION_OPERATING_LEVERAGE_4B_WATCH","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":230000.0,"evidence_available_at_that_date":"source_proxy_only: global game IP monetization route, traffic/ARPU operating leverage, and platform distribution strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["global_game_ip_route","operating_leverage_route","traffic_monetization_route","relative_strength"],"stage3_evidence_fields":["revenue_conversion_partial","margin_bridge_partial","cash_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","peak_proximity","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv","profile_path":"atlas/symbol_profiles/259/259960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.22,"MFE_90D_pct":30.0,"MFE_180D_pct":54.35,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.48,"MAE_90D_pct":-8.48,"MAE_180D_pct":-8.48,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":355000.0,"drawdown_after_peak_pct":-9.15,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_game_ip_operating_leverage_rerating","four_b_evidence_type":["valuation_rerating","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_low_mae_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_259960_2024_02_13_230000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"PEARLABYSS_263750_2024_07_09_STAGE2_FALSE_POSITIVE_GAME_IP_EVENT","case_id":"C27_PEARLABYSS_263750_2024_07_09_GAME_IP_RELEASE_EVENT_FALSE_POSITIVE","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_RELEASE_EVENT_PREMIUM_WITHOUT_MONETIZATION_BRIDGE","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-07-09","entry_date":"2024-07-09","entry_price":46200.0,"evidence_available_at_that_date":"source_proxy_only: game IP release/event premium and global launch expectation visible, but bookings, live-service monetization, and revenue conversion bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["game_ip_release_event","global_launch_expectation","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","price_only_peak","monetization_bridge_absent"],"stage4c_evidence_fields":["booking_bridge_absent","launch_timing_risk","cash_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.14,"MFE_90D_pct":3.14,"MFE_180D_pct":3.14,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-20.89,"MAE_90D_pct":-27.27,"MAE_180D_pct":-30.95,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":47650.0,"drawdown_after_peak_pct":-33.05,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"game_ip_event_premium_not_stage3_without_booking_monetization_bridge","four_b_evidence_type":["event_premium","price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_event_premium","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_263750_2024_07_09_46200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HYBE_352820_2024_03_25_STAGE2_FALSE_POSITIVE_FANDOM_IP_PLATFORM_RISK","case_id":"C27_HYBE_352820_2024_03_25_FANDOM_IP_PLATFORM_RISK_FALSE_POSITIVE","symbol":"352820","company_name":"하이브","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MUSIC_FANDOM_IP_PLATFORM_GOVERNANCE_EVENT_RISK","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":207000.0,"evidence_available_at_that_date":"source_proxy_only: music/fandom IP platform monetization narrative visible, but operating-leverage, governance/trust, and recurring revenue bridge were not yet durable","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["music_fandom_ip_route","platform_monetization_route","global_content_distribution"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","trust_governance_risk"],"stage4c_evidence_fields":["governance_trust_break","operating_leverage_bridge_absent","event_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv","profile_path":"atlas/symbol_profiles/352/352820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.01,"MFE_90D_pct":14.01,"MFE_180D_pct":14.01,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.83,"MAE_90D_pct":-17.97,"MAE_180D_pct":-23.82,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":236000.0,"drawdown_after_peak_pct":-33.18,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fandom_ip_platform_premium_not_stage3_without_operating_leverage_and_trust_bridge","four_b_evidence_type":["event_premium","governance_trust_risk"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_event_risk_fandom_ip_platform","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_352820_2024_03_25_207000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_KRAFTON_259960_2024_02_13_GAME_IP_GLOBAL_MONETIZATION_RERATING","trigger_id":"KRAFTON_259960_2024_02_13_STAGE2A_GAME_IP_GLOBAL_MONETIZATION","symbol":"259960","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with C27 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Global IP monetization worked, but C27 Yellow/Green should still require sustained bookings/revenue/margin conversion before ignoring peak proximity.","MFE_90D_pct":30.0,"MAE_90D_pct":-8.48,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_PEARLABYSS_263750_2024_07_09_GAME_IP_RELEASE_EVENT_FALSE_POSITIVE","trigger_id":"PEARLABYSS_263750_2024_07_09_STAGE2_FALSE_POSITIVE_GAME_IP_EVENT","symbol":"263750","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Game IP release event premium without bookings/live-service monetization bridge produced low MFE and high MAE.","MFE_90D_pct":3.14,"MAE_90D_pct":-27.27,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_HYBE_352820_2024_03_25_FANDOM_IP_PLATFORM_RISK_FALSE_POSITIVE","trigger_id":"HYBE_352820_2024_03_25_STAGE2_FALSE_POSITIVE_FANDOM_IP_PLATFORM_RISK","symbol":"352820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":65,"stage_label_before":"Stage2 false-positive / trust-risk watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":51,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Fandom/IP platform narrative lacked durable operating-leverage and trust/governance bridge; event risk should cap Stage2.","MFE_90D_pct":14.01,"MAE_90D_pct":-17.97,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 83
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

If this loop is accepted, C27 moves from 24 to a projected 27 rows. It remains below 30-row minimum stability, so a later run can still add 3 more C27 rows, but the next run should re-read the latest No-Repeat Index before selecting another C27 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/259/259960.json
  - atlas/symbol_profiles/263/263750.json
  - atlas/symbol_profiles/352/352820.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
