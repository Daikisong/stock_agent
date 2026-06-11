# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R8_loop_141_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
selected_round: R8
selected_loop: 141
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GLOBAL_FANDOM_IP_PLATFORM_MONETIZATION_4B_WITH_ARTIST_GOVERNANCE_EVENT_RISK
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_event_risk_timing_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after an accidental duplicate C19 loop140 materialization path was discarded. C19 reached the local 30-row stability threshold at loop140, so this run moves to the next Priority 0 archetype: C27.

This loop adds 3 new independent C27 rows and moves C27 from static 24 rows to projected 27 rows. It still needs 3 rows to reach the 30-row minimum stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `e2r_2_1_stock_web_calibrated`.

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

C27 is the content/IP global monetization archetype. IP is the seed, fandom/platform distribution is the soil, but recurring revenue, margin, revision and cash conversion are the crop. A hit headline alone is not harvest.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C27 static rows | 24 |
| C27 need to 30 | 6 |
| C27 need to 50 | 26 |
| C27 investigation point | IP 매출화, 글로벌 플랫폼 전환, 일회성 흥행 반례 |
| local previous C27 rows in this session | 0 |
| this loop projected rows | 27 |

Selected C27 symbols:

| symbol | company | status |
|---|---|---|
| 352820 | 하이브 | new local C27 global fandom/IP platform 4B row |
| 035900 | JYP Ent. | new local C27 artist IP monetization counterexample |
| 253450 | 스튜디오드래곤 | new local C27 drama content IP platform counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate. The duplicate C19 loop140 materialization created during this execution is explicitly rejected.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 352820 / 2024-03-06 | true | true | clean_180D_window_zero_corporate_action_candidates | true, weight 1.00 |
| 035900 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 253450 / 2024-03-06 | true | true | clean_180D_window_zero_corporate_action_candidates_market_label_switch_only | true, weight 0.95 |

Corporate-action notes:

- 하이브 has zero corporate-action candidates.
- JYP Ent. has old name-change/corporate-action candidates before the selected 2024 window only.
- 스튜디오드래곤 has zero corporate-action candidates; the 2024-06-14 KOSDAQ GLOBAL label switch is treated as market-label only, not price-adjustment contamination.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GLOBAL_FANDOM_IP_PLATFORM_MONETIZATION_4B_WITH_ARTIST_GOVERNANCE_EVENT_RISK | C27 | fandom/IP platform rerating can work as 4B, but Green needs recurring revenue/margin/revision plus artist-event audit |
| GLOBAL_ARTIST_IP_MONETIZATION_WITHOUT_ALBUM_TOUR_MARGIN_REVISION_BRIDGE | C27 | artist/IP language without album/tour margin and revision bridge is false-positive risk |
| DRAMA_CONTENT_IP_GLOBAL_PLATFORM_WITHOUT_PRODUCTION_MARGIN_REVENUE_BRIDGE | C27 | content/platform distribution without production-margin and revenue conversion is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C27_HYBE_352820_2024_03_06_GLOBAL_FANDOM_IP_PLATFORM_RERATING_4B_TO_EVENT_RISK | 352820 | 하이브 | 4B_to_4C_timing_success | positive_boundary | 27.20% MFE but later event-risk drawdown |
| C27_JYP_035900_2024_03_06_GLOBAL_ARTIST_IP_MONETIZATION_WITHOUT_MARGIN_REVISION_BRIDGE | 035900 | JYP Ent. | failed_rerating | counterexample | 8.08% MFE then -37.81% 180D MAE |
| C27_STUDIODRAGON_253450_2024_03_06_CONTENT_IP_GLOBAL_PLATFORM_FAIL | 253450 | 스튜디오드래곤 | failed_rerating | counterexample | 10.37% MFE then -21.21% 180D MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_boundary_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 352820 | source_proxy_only | global fandom/IP platform and album/tour/platform monetization | required before promotion |
| 035900 | source_proxy_only | global artist/IP monetization but margin/revision bridge absent | required; useful as counterexample |
| 253450 | source_proxy_only | global content/IP distribution but production-margin/revenue bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 352820 | atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv | atlas/symbol_profiles/352/352820.json |
| 035900 | atlas/ohlcv_tradable_by_symbol_year/035/035900/2024.csv | atlas/symbol_profiles/035/035900.json |
| 253450 | atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv | atlas/symbol_profiles/253/253450.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HYBE_352820_2024_03_06_STAGE2A_GLOBAL_FANDOM_IP_PLATFORM_4B | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 187500 | global fandom/IP platform 4B |
| JYP_035900_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_ARTIST_IP | Stage2 | 2024-03-06 | 2024-03-06 | 69300 | artist IP without margin/revision bridge |
| STUDIODRAGON_253450_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_CONTENT_IP | Stage2 | 2024-03-06 | 2024-03-06 | 42900 | content IP platform without production-margin/revenue bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 352820 | 2024-03-06 | 187500 | 25.87 | -2.40 | 27.20 | -4.69 | 27.20 | -15.89 | 2024-04-22 | 238500 | -33.88 |
| 035900 | 2024-03-06 | 69300 | 8.08 | -9.67 | 8.08 | -20.63 | 8.08 | -37.81 | 2024-03-27 | 74900 | -42.46 |
| 253450 | 2024-03-06 | 42900 | 8.97 | -6.99 | 10.37 | -6.99 | 10.37 | -21.21 | 2024-05-27 | 47350 | -28.62 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 352820 | Stage2A possible; IP-platform rerating risks overpromotion | 4B worked, event-risk audit required | current_profile_4B_too_late |
| 035900 | Stage2 risk if artist/IP beta is over-credited | false positive | current_profile_false_positive |
| 253450 | Stage2 risk if content/IP platform language is over-credited | false positive | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C27 interpretation:

- Global IP/fandom platform language can support Stage2A only with recurring revenue, margin, revision and cash-conversion bridge.
- Artist IP or content platform vocabulary without margin/revision conversion should remain Stage1/Stage2-watch.
- A 4B rerating must include artist/governance/event-risk audit before any Yellow/Green promotion.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 352820 | 0.79 | 1.00 | global IP platform rerating | 4B/event-risk audit required |
| 035900 | 0.93 | 1.00 | short artist-IP rebound / bridge absent | not Stage3 |
| 253450 | 0.91 | 1.00 | temporary content-IP rebound / bridge absent | not Stage3 |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 352820 | event_risk_watch_after_4B | positive 4B but Green blocked until event/margin/revision audit |
| 035900 | hard_4c_late | margin/revision/conversion absence should have capped Stage2 earlier |
| 253450 | hard_4c_late | production-margin/revenue bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L8_PLATFORM_CONTENT_SW_SECURITY
confidence = medium
```

Candidate:

> In L8 platform/content names, IP or global-platform narratives should promote Stage2A only when recurring revenue, margin bridge, revision, fan/customer retention and cash conversion are visible. A single artist/content/platform headline should stay Stage1/Stage2-watch unless the monetization bridge is explicit. 4B rerating rows need artist/governance/event-risk audit.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C27_CONTENT_IP_GLOBAL_MONETIZATION
confidence = medium
```

Candidate C27 rule:

```text
C27_IP_monetization_margin_revision_bridge_required =
  content_IP_or_artist_IP_or_fandom_platform_route
  AND (recurring_revenue OR album_tour_margin_bridge OR platform_take_rate OR global_distribution_revenue OR confirmed_revision OR cash_conversion)

if artist_IP_beta and margin_revision_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if content_platform_language and production_margin_revenue_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 20 and IP_event_risk_visible:
    add C27_IP_platform_4B_event_audit = true

if market_label_switch_only:
    keep_usable_but_mark_quality_caveat = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / event-risk | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 15.22 | -10.77 | 15.22 | -24.97 | 2 false positives + 1 4B event audit | C27 bridge too loose |
| P0b e2r_2_1_stock_web_calibrated | rollback | 3 | 15.22 | -10.77 | 15.22 | -24.97 | 2 false positives + 1 4B event audit | over-credits IP/global platform language |
| P1 sector_specific_candidate_profile | L8 | 1 4B buffer + 2 guard | 27.2 | -4.69 | 27.2 | -15.89 | 0 | better with monetization bridge gate |
| P2 canonical_archetype_candidate_profile | C27 | 1 4B buffer + 2 guard | 27.2 | -4.69 | 27.2 | -15.89 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C27 guard | 1 4B buffer + 2 guard | 27.2 | -4.69 | 27.2 | -15.89 | 0 | adds artist/content IP false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 352820 | Stage2A aligned; 4B/event-risk audit before Green | current_profile_4B_too_late |
| 035900 | Stage2 false positive if artist IP bridge not enforced | current_profile_false_positive |
| 253450 | Stage2 false positive if content platform bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive boundary | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | mixed C27 fine ids | 1 | 2 | 2 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 24 -> projected 27; still need 3 to reach 30 |

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
new_axis_proposed: C27_IP_monetization_margin_revision_bridge_required|C27_artist_IP_false_positive_guardrail|C27_content_platform_revenue_bridge_guardrail|C27_IP_platform_4B_event_audit|market_label_switch_quality_caveat
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
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
- Uses C27 Priority 0 coverage gap.
- Uses new local C27 symbols.
- Keeps 035900 with reduced independent weight because old name-change/corporate-action candidates exist outside selected window.
- Keeps 253450 with reduced independent weight because of 2024-06-14 market-label switch.
- Treats 352820 as 4B/event-risk buffer, not Green promotion.
- Discards the accidental duplicate C19 loop140 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated C19 loop140 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_IP_monetization_margin_revision_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"035900/253450 show IP/platform language can fail without revenue, margin and revision bridge while 352820 works only as 4B/event-risk buffer","blocks two false positives while preserving IP platform 4B","HYBE_352820_2024_03_06_STAGE2A_GLOBAL_FANDOM_IP_PLATFORM_4B|JYP_035900_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_ARTIST_IP|STUDIODRAGON_253450_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_CONTENT_IP",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C27_artist_IP_false_positive_guardrail,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"035900 had only 8.08% MFE and -37.81% 180D MAE after global artist/IP language without margin/revision bridge","requires album/tour margin, new-artist conversion, revision and cash bridge before Stage2/Yellow promotion","JYP_035900_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_ARTIST_IP",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,C27_content_platform_revenue_bridge_guardrail,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"253450 had low MFE and negative 180D MAE after content/IP platform language without production-margin and revenue bridge","requires platform distribution revenue, production-margin and slate hit-rate before Stage2/Yellow promotion","STUDIODRAGON_253450_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_CONTENT_IP",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,C27_IP_platform_4B_event_audit,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"352820 produced a 27.20% MFE but later 33.88% peak drawdown, so IP platform rerating needs artist/governance event-risk audit","keeps global fandom/IP platform cases as Stage2A/4B before Green","HYBE_352820_2024_03_06_STAGE2A_GLOBAL_FANDOM_IP_PLATFORM_4B",1,1,0,medium,canonical_shadow_only,"4B/event-risk calibration"
shadow_weight,market_label_switch_quality_caveat,archetype_specific_quality_flag,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"253450 has a 2024-06-14 KOSDAQ GLOBAL label switch during validation window","keeps row usable but slightly lowers independent evidence weight","STUDIODRAGON_253450_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_CONTENT_IP",1,1,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C27_HYBE_352820_2024_03_06_GLOBAL_FANDOM_IP_PLATFORM_RERATING_4B_TO_EVENT_RISK","symbol":"352820","company_name":"하이브","round":"R8","loop":"141","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_FANDOM_IP_PLATFORM_MONETIZATION_4B_WITH_ARTIST_GOVERNANCE_EVENT_RISK","case_type":"4B_to_4C_timing_success","positive_or_counterexample":"positive_boundary","best_trigger":"HYBE_352820_2024_03_06_STAGE2A_GLOBAL_FANDOM_IP_PLATFORM_4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global fandom/IP platform monetization produced a 27.20% MFE, but the subsequent drawdown required C27 4B/event-risk audit before Green promotion","current_profile_verdict":"current_profile_4B_too_late_if_IP_platform_rerating_overpromoted_to_Green","price_source":"Songdaiki/stock-web","notes":"new local C27 symbol; clean profile with zero corporate-action candidates"}
{"row_type":"case","case_id":"C27_JYP_035900_2024_03_06_GLOBAL_ARTIST_IP_MONETIZATION_WITHOUT_MARGIN_REVISION_BRIDGE","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"141","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_ARTIST_IP_MONETIZATION_WITHOUT_ALBUM_TOUR_MARGIN_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"JYP_035900_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_ARTIST_IP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action/name-change candidates before selected window only; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"global artist/IP monetization beta produced only an 8.08% MFE before -37.81% 180D MAE, so album/tour margin and revision bridge were mandatory","current_profile_verdict":"current_profile_false_positive_if_artist_IP_beta_overcredited_without_margin_revision","price_source":"Songdaiki/stock-web","notes":"new local C27 symbol; old profile caveat only, not 2024 window contamination"}
{"row_type":"case","case_id":"C27_STUDIODRAGON_253450_2024_03_06_CONTENT_IP_GLOBAL_PLATFORM_FAIL","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"141","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"DRAMA_CONTENT_IP_GLOBAL_PLATFORM_WITHOUT_PRODUCTION_MARGIN_REVENUE_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"STUDIODRAGON_253450_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_CONTENT_IP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"zero corporate-action candidates; market label changes to KOSDAQ GLOBAL on 2024-06-14, retained with slight quality caveat","independent_evidence_weight":0.95,"score_price_alignment":"global drama/content IP platform narrative produced only 10.37% 90D MFE and then -21.21% 180D MAE without production-margin/revenue bridge","current_profile_verdict":"current_profile_false_positive_if_content_IP_platform_language_overcredited","price_source":"Songdaiki/stock-web","notes":"new local C27 symbol; market-label switch only, no corporate-action candidate"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HYBE_352820_2024_03_06_STAGE2A_GLOBAL_FANDOM_IP_PLATFORM_4B","case_id":"C27_HYBE_352820_2024_03_06_GLOBAL_FANDOM_IP_PLATFORM_RERATING_4B_TO_EVENT_RISK","symbol":"352820","company_name":"하이브","round":"R8","loop":"141","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_FANDOM_IP_PLATFORM_MONETIZATION_4B_WITH_ARTIST_GOVERNANCE_EVENT_RISK","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_event_risk_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":187500.0,"evidence_available_at_that_date":"source_proxy_only: global fandom platform, artist IP monetization, album/tour/platform revenue and relative-strength recovery visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["global_fandom_platform","artist_IP_monetization","album_tour_platform_revenue","relative_strength_recovery"],"stage3_evidence_fields":["revenue_bridge_partial","margin_bridge_pending","revision_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["IP_platform_rerating","valuation_peak_watch","artist_governance_event_risk"],"stage4c_evidence_fields":["artist_governance_event_risk_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv","profile_path":"atlas/symbol_profiles/352/352820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.87,"MFE_90D_pct":27.2,"MFE_180D_pct":27.2,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.4,"MAE_90D_pct":-4.69,"MAE_180D_pct":-15.89,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-22","peak_price":238500.0,"drawdown_after_peak_pct":-33.88,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"global IP platform rerating worked as 4B, but artist/governance event risk and later drawdown require C27 4B audit before Green","four_b_evidence_type":["IP_platform_rerating","global_fandom_monetization"],"four_c_protection_label":"event_risk_watch_after_4B","trigger_outcome_label":"positive_boundary_mfe_then_event_risk_drawdown","current_profile_verdict":"current_profile_4B_too_late_if_IP_platform_rerating_overpromoted_to_Green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_zero_corporate_action_candidates","same_entry_group_id":"C27_352820_2024_03_06_187500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"JYP_035900_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_ARTIST_IP","case_id":"C27_JYP_035900_2024_03_06_GLOBAL_ARTIST_IP_MONETIZATION_WITHOUT_MARGIN_REVISION_BRIDGE","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"141","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_ARTIST_IP_MONETIZATION_WITHOUT_ALBUM_TOUR_MARGIN_REVISION_BRIDGE","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_event_risk_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":69300.0,"evidence_available_at_that_date":"source_proxy_only: global artist IP, tour/album monetization and fan-platform narrative visible, but margin, revision, new-artist conversion and cash bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["global_artist_IP","album_tour_monetization_beta","fan_platform_narrative"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["short_IP_rebound","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["margin_bridge_absent","revision_bridge_absent","new_artist_conversion_absent","cash_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2024.csv","profile_path":"atlas/symbol_profiles/035/035900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.08,"MFE_90D_pct":8.08,"MFE_180D_pct":8.08,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.67,"MAE_90D_pct":-20.63,"MAE_180D_pct":-37.81,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":74900.0,"drawdown_after_peak_pct":-42.46,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"artist IP monetization beta did not become C27 Stage3 without margin, revision and conversion bridge","four_b_evidence_type":["short_IP_rebound","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive_if_artist_IP_beta_overcredited_without_margin_revision","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["old_profile_corporate_action_candidates_before_window_only"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C27_035900_2024_03_06_69300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action/name-change candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"STUDIODRAGON_253450_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_CONTENT_IP","case_id":"C27_STUDIODRAGON_253450_2024_03_06_CONTENT_IP_GLOBAL_PLATFORM_FAIL","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"141","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"DRAMA_CONTENT_IP_GLOBAL_PLATFORM_WITHOUT_PRODUCTION_MARGIN_REVENUE_BRIDGE","sector":"platform / content / software / security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_event_risk_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":42900.0,"evidence_available_at_that_date":"source_proxy_only: drama content IP, global platform distribution and overseas monetization narrative visible, but production margin, slate hit-rate and revenue conversion bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["drama_content_IP","global_platform_distribution","overseas_monetization_narrative"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["temporary_IP_rebound","bridge_absent","platform_margin_pressure"],"stage4c_evidence_fields":["production_margin_bridge_absent","slate_hit_rate_absent","revenue_conversion_absent","cash_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.97,"MFE_90D_pct":10.37,"MFE_180D_pct":10.37,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.99,"MAE_90D_pct":-6.99,"MAE_180D_pct":-21.21,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-27","peak_price":47350.0,"drawdown_after_peak_pct":-28.62,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"content IP/global platform rebound stayed below Stage3 without production margin, slate hit-rate and revenue bridge","four_b_evidence_type":["temporary_IP_rebound","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive_if_content_IP_platform_language_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_label_switch_2024_06_14_not_price_adjustment_contamination"],"corporate_action_window_status":"clean_180D_window_zero_corporate_action_candidates_market_label_switch_only","same_entry_group_id":"C27_253450_2024_03_06_42900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"market-label switch only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C27_HYBE_352820_2024_03_06_GLOBAL_FANDOM_IP_PLATFORM_RERATING_4B_TO_EVENT_RISK","trigger_id":"HYBE_352820_2024_03_06_STAGE2A_GLOBAL_FANDOM_IP_PLATFORM_4B","symbol":"352820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable / global IP platform 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-watch with C27 IP platform 4B/event audit","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"IP platform rerating worked, but Green needs recurring revenue, margin, revision and artist/governance event-risk audit.","MFE_90D_pct":27.2,"MAE_90D_pct":-4.69,"score_return_alignment_label":"positive_boundary_but_4b_event_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_IP_platform_rerating_overpromoted_to_Green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C27_JYP_035900_2024_03_06_GLOBAL_ARTIST_IP_MONETIZATION_WITHOUT_MARGIN_REVISION_BRIDGE","trigger_id":"JYP_035900_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_ARTIST_IP","symbol":"035900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2 false-positive / artist IP monetization risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":42,"stage_label_after":"Stage1/4C-watch, not C27 Yellow","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Global artist/IP language lacked album/tour margin, revision, new-artist conversion and cash bridge.","MFE_90D_pct":8.08,"MAE_90D_pct":-20.63,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive_if_artist_IP_beta_overcredited_without_margin_revision"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C27_STUDIODRAGON_253450_2024_03_06_CONTENT_IP_GLOBAL_PLATFORM_FAIL","trigger_id":"STUDIODRAGON_253450_2024_03_06_STAGE2_FALSE_POSITIVE_GLOBAL_CONTENT_IP","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":56,"stage_label_before":"Stage2 false-positive / global content IP platform risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":41,"stage_label_after":"Stage1/4C-watch, not C27 Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Content IP platform language lacked production-margin, slate hit-rate, revenue and cash-conversion bridge.","MFE_90D_pct":10.37,"MAE_90D_pct":-6.99,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive_if_content_IP_platform_language_overcredited"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"141","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

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
completed_loop = 141
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

If this loop is accepted, C27 moves to projected 27 rows and still needs 3 rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C27 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/035/035900/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/352/352820.json
  - atlas/symbol_profiles/035/035900.json
  - atlas/symbol_profiles/253/253450.json
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R5_loop_140_L5_CONSUMER_BRAND_RETAIL_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
