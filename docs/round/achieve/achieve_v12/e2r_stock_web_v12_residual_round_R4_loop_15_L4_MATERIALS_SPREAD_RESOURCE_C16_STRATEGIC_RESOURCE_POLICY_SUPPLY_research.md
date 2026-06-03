# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R4_loop_15_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
scheduled_round: R4
scheduled_loop: 15
completed_round: R4
completed_loop: 15
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: STRATEGIC_RESOURCE_POLICY_DIRECTNESS_VS_THEME_PROXY_DECAY
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are treated as production assumptions, not new proposals:

- `stage2_actionable_evidence_bonus = +2.0`
- `stage3_yellow_total_min = 75.0`
- `stage3_green_total_min = 87.0`
- `stage3_green_revision_min = 55.0`
- `stage3_cross_evidence_green_buffer = +1.5`
- `price_only_blowoff_blocks_positive_stage = true`
- `full_4b_requires_non_price_evidence = true`
- `hard_4c_thesis_break_routes_to_4c = true`

This MD does not reopen those global rules. It stress-tests how C16 should separate direct strategic-resource revenue exposure from policy-theme proxy rallies that never become customer/order/margin evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 15 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY |
| round_sector_consistency | pass |
| output filename consistency | pass |

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, so the round-sector gate is valid. C16 is selected because prior R4 local v12 files were concentrated in C15/C17; this loop fills the strategic-resource/policy-supply gap with one direct-exposure positive and two proxy counterexamples.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts/local v12 outputs were consulted only for scheduling and duplicate avoidance. Local v12 state showed loops 10-14 complete through R1-R13 and loop 15 complete through R3, so this execution is R4 / Loop 15. Prior R4 v12 files mostly covered C15 and C17 with symbols such as 005490, 004020, 103140, 010130, 011170, 011780, 006650, 051910, and 298020. The current case set uses 025860, 047400, and 000910, so there is no same symbol + same trigger_date + same entry_date reuse.

| check | result |
|---|---|
| same symbol + same trigger_date + same entry_date reused | no |
| scheduled round obeyed | yes |
| canonical archetype repeated with new symbols/families | yes, allowed |
| new independent case ratio | 3/3 = 1.00 |
| counterexample included | yes, 2 |
| schema rematerialization only | no |

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
| markets | KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Stock-Web tradable rows are raw/unadjusted FinanceData/marcap OHLCV rows. Corporate-action candidate windows are blocked by default; the tested windows below do not overlap each symbol's corporate-action candidate dates.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | corporate-action candidate status | selected 180D window status | calibration_usable |
|---|---|---|---|---|---|
| 025860 | 남해화학 | atlas/symbol_profiles/025/025860.json | old candidates 1999-2002 only | clean_180D_window | true |
| 047400 | 유니온머티리얼 | atlas/symbol_profiles/047/047400.json | old candidate 2011-04-29 only | clean_180D_window | true |
| 000910 | 유니온 | atlas/symbol_profiles/000/000910.json | old candidates 1997/2008 only | clean_180D_window | true |

All representative triggers have entry dates inside Stock-Web tradable shards and at least 180 forward trading days before manifest max_date 2026-02-20.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| FERTILIZER_EXPORT_RESTRICTION_DIRECT_REVENUE_EXPOSURE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | strategic resource/supply disruption with direct product pricing and earnings bridge |
| CHINA_EXPORT_CONTROL_THEME_PROXY_NO_DIRECT_REVISION | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | strategic material headline but no direct revision/customer/order evidence |
| RARE_EARTH_TECH_EXPORT_BAN_THEME_DECAY | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | policy headline re-spike that decays without direct revenue conversion |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | current_profile_verdict | why selected |
|---|---:|---|---|---|---|---|
| R4L15_C16_CASE_001_NAMHAE_FERTILIZER_SUPPLY_20220304 | 025860 | 남해화학 | structural_success | FERTILIZER_EXPORT_RESTRICTION_DIRECT_REVENUE_EXPOSURE | current_profile_missed_structural | Direct revenue exposure exists: fertilizer supply shock can become ASP/margin bridge rather than pure theme proxy. |
| R4L15_C16_CASE_002_UNION_MATERIALS_GALLIUM_GERMANIUM_FALSE_BREAK_20230704 | 047400 | 유니온머티리얼 | false_positive_green | CHINA_EXPORT_CONTROL_THEME_PROXY_NO_DIRECT_REVISION | current_profile_false_positive | Policy headline exists, but direct revenue bridge is missing. C16 should not let policy_optional score alone promote Stage3/Green. |
| R4L15_C16_CASE_003_UNION_RARE_EARTH_TECH_BAN_FALSE_BREAK_20231222 | 000910 | 유니온 | 4C_late | RARE_EARTH_TECH_EXPORT_BAN_THEME_DECAY | current_profile_4C_too_late | No direct capacity/order/margin bridge. C16 needs a timed theme-decay 4C route when policy headline is not converted into revenue evidence within 30~60 trading days. |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 1 | 025860 |
| counterexample_or_failed_rerating | 2 | 047400, 000910 |
| 4B_or_4C_case | 2 | 047400, 000910 |
| calibration_usable_case_count | 3 | all representative triggers |

## 9. Evidence Source Map

| trigger_id | evidence timing rule | stage2 evidence | stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|
| R4L15_C16_T001 | evidence treated as same-day or next-tradable-day close depending on public timing; entry row exists in Stock-Web | public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, multiple_public_sources | 4B=valuation_blowoff, positioning_overheat, explicit_event_cap; 4C=none |
| R4L15_C16_T002 | evidence treated as same-day or next-tradable-day close depending on public timing; entry row exists in Stock-Web | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | none at trigger | 4B=price_only_local_peak, positioning_overheat; 4C=thesis_evidence_broken |
| R4L15_C16_T003 | evidence treated as same-day or next-tradable-day close depending on public timing; entry row exists in Stock-Web | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | none at trigger | 4B=price_only_local_peak, positioning_overheat; 4C=thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | price_basis |
|---:|---|---|---|---|
| 025860 | 남해화학 | atlas/ohlcv_tradable_by_symbol_year/025/025860/2022.csv | atlas/symbol_profiles/025/025860.json | tradable_raw |
| 047400 | 유니온머티리얼 | atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv | atlas/symbol_profiles/047/047400.json | tradable_raw |
| 000910 | 유니온 | atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv | atlas/symbol_profiles/000/000910.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 | stage3 | 4B | 4C | aggregate role |
|---|---:|---|---|---|---:|---|---|---|---|---|
| R4L15_C16_T001 | 025860 | Stage2-Actionable | 2022-03-04 | 2022-03-04 | 10,500 | yes | yes | yes | no | representative |
| R4L15_C16_T002 | 047400 | Stage2-Actionable | 2023-07-04 | 2023-07-04 | 4,070 | yes | no | yes | yes | representative |
| R4L15_C16_T003 | 000910 | Stage2-Actionable | 2023-12-22 | 2023-12-22 | 5,500 | yes | no | yes | yes | representative |
| R4L15_C16_T001_4B | 025860 | Stage4B-overlay | 2022-04-15 | 2022-04-15 | 16,150 | no | no | yes | no | 4B_overlay_only |
| R4L15_C16_T002_4B | 047400 | Stage4B-overlay | 2023-07-12 | 2023-07-12 | 4,455 | no | no | yes | no | 4B_overlay_only |
| R4L15_C16_T003_4B | 000910 | Stage4B-overlay | 2024-01-12 | 2024-01-12 | 6,360 | no | no | yes | no | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R4L15_C16_T001 | 10,500 | 57.14% | -7.14% | 61.90% | -14.29% | 61.90% | -23.90% | 2022-04-19 | 17,000 | -53.00% | true |
| R4L15_C16_T002 | 4,070 | 12.04% | -20.15% | 12.04% | -39.56% | 12.04% | -39.56% | 2023-07-12 | 4,560 | -46.05% | true |
| R4L15_C16_T003 | 5,500 | 19.64% | -4.00% | 19.64% | -7.27% | 19.64% | -38.91% | 2024-01-10 | 6,580 | -48.94% | true |

## 13. Current Calibrated Profile Stress Test

| symbol | P0 likely judgment | realized path | verdict |
|---:|---|---|---|
| 025860 | Stage2-Actionable but likely too slow to promote without explicit revision; policy shock may be treated as theme risk | 61.90% 90D MFE before later drawdown; direct fertilizer revenue exposure mattered | current_profile_missed_structural |
| 047400 | Stage3-Yellow false-positive risk if policy_optional + RS overwhelms missing revenue bridge | 12.04% MFE vs -39.56% 90D MAE | current_profile_false_positive |
| 000910 | Stage3-Yellow/Watch may remain too long after theme fails to convert | 19.64% MFE but -38.91% 180D MAE; 4C needed earlier | current_profile_4C_too_late |

The Stage2 bonus is not rejected. It is conditional: direct resource-price exposure deserves the bonus; policy-proxy headlines without direct revenue evidence should have a C16 decay clock. Yellow 75 and Green 87 are too permissive for proxy baskets when policy_or_regulatory_score is the main positive component. Full 4B non-price requirement is kept for production, but C16 should allow price-only 4B-watch rows to feed 4C decay evidence when no direct evidence arrives.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | Green candidate | green_lateness_ratio | interpretation |
|---:|---:|---:|---|---|
| 025860 | 10,500 | hypothetical 16,150 after fertilizer-price confirmation | 0.87 | Green would have arrived after most upside; C16 directness should allow Stage2/Yellow earlier. |
| 047400 | 4,070 | no supported Green | not_applicable | No confirmed revision/customer/order; any Green label would be outcome-chasing. |
| 000910 | 5,500 | no supported Green | not_applicable | Policy re-spike lacked direct revenue evidence; Green should be blocked. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| R4L15_C16_T001_4B | valuation_blowoff, positioning_overheat, explicit_event_cap | 0.87 | 0.87 | good_full_window_4B_timing |
| R4L15_C16_T002_4B | price_only, positioning_overheat | 0.79 | 0.79 | price_only_local_4B_watch_not_full_4B |
| R4L15_C16_T003_4B | price_only, positioning_overheat | 0.80 | 0.80 | price_only_local_4B_watch_not_full_4B |

The distinction matters. 047400 and 000910 show that price-only local peaks can be useful warnings, but they should not become full 4B production exits unless non-price evidence confirms overheat, thesis cap, dilution, or explicit supply-policy reversal. In C16, those price-only 4B-watch rows are better used as inputs to a timed 4C decay guard.

## 16. 4C Protection Audit

| symbol | 4C date | MAE after 4C | prior peak drawdown | protection label | interpretation |
|---:|---|---:|---:|---|---|
| 025860 | not_applicable | not_applicable | -53.00% after 2022-04-19 peak | thesis_break_watch_only | Positive structural resource shock eventually normalized, but no hard 4C at Stage2 trigger. |
| 047400 | 2023-07-24 proxy break | about -33% from 3,685 to 2,460 | -46.05% | hard_4c_success | Early failure to hold policy-headline move protected large later drawdown. |
| 000910 | 2024-05-27 direct-evidence timeout | about -36.8% from 5,320 to 3,360 | -48.94% | hard_4c_late | 4C should have been available earlier once no revenue bridge appeared after 30-60D. |

## 17. Sector-Specific Rule Candidate

No broad L4 sector rule is proposed from only three C16 cases. The result is narrower: C16 should separate direct strategic-resource revenue exposure from theme-proxy policy headlines. This is canonical-archetype-specific, not a global or L4-wide production change.

## 18. Canonical-Archetype Rule Candidate

Candidate C16 shadow rules:

1. `C16_direct_revenue_exposure_bonus`: if policy/supply shock maps directly to the company's product ASP, volume, inventory margin, or offtake path, add a shadow directness bonus and allow Stage2-Actionable / Yellow before full revision confirmation.
2. `C16_policy_proxy_decay_guard`: if policy_or_regulatory_score and relative_strength are high but direct revenue/order/margin evidence is absent within 30-60 trading days, cap positive stage at Stage2-Watch and route to timed 4C-watch.
3. `C16_price_only_4B_watch_feeds_decay_not_full_exit`: price-only peaks in policy-proxy baskets remain watch overlays; they do not become full 4B but can strengthen the later 4C decay guard.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | 31.19% | -20.37% | 0.67 | 1 | mixed: direct positive underpromoted, proxy headlines overpromoted |
| P0b e2r_2_0_baseline_reference | rollback reference | 3 | 31.19% | -20.37% | 0.67 | 2 | worse: slower on direct resource shock and still vulnerable to policy proxy |
| P1 sector_specific_candidate_profile | L4 shadow | 3 | 31.19% | -20.37% | 0.67 | 1 | not enough sector breadth for L4-wide change |
| P2 canonical_archetype_candidate_profile | C16 shadow | 3 | 31.19% | -20.37% | 0.00 selected-after-guard | 0 | best: promotes 025860, blocks 047400/000910 |
| P3 counterexample_guard_profile | C16 guard | 3 | 31.19% | -20.37% | 0.00 selected-after-guard | 1 | strong guard; may underpromote direct cases without directness bonus |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_before | stage_before | weighted_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R4L15_C16_T001 | 74 | Stage2-Actionable | 85 | Stage3-Yellow-shadow | 61.90% | -14.29% | P0_missed_structural_P2_better |
| R4L15_C16_T002 | 76 | Stage3-Yellow/false-positive-risk | 55 | Stage2-Watch / 4C-watch | 12.04% | -39.56% | P0_false_positive_P3_guard_blocks |
| R4L15_C16_T003 | 75 | Stage3-Yellow/false-positive-risk | 57 | Stage2-Watch / timed-4C | 19.64% | -7.27% | P0_4C_too_late_P3_better |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | STRATEGIC_RESOURCE_POLICY_DIRECTNESS_VS_THEME_PROXY_DECAY | 1 | 2 | 3 | 2 | 3 | 0 | 6 | 3 | 3 | false | true | C16 now has direct positive + proxy counterexamples; still needs more resource subclasses such as uranium/lithium/nickel offtake cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [current_profile_missed_structural, current_profile_false_positive, current_profile_4C_too_late]
new_axis_proposed: C16_direct_revenue_exposure_bonus; C16_policy_proxy_decay_guard; C16_price_only_4B_watch_feeds_decay_not_full_exit
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c needs C16 directness/proxy-decay timing, not global rollback
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest fields for price basis and max_date.
- Symbol profile availability, selected year shard paths, and non-overlap with corporate-action candidate dates.
- Representative trigger entry_price, sampled peak/low rows, MFE/MAE, and drawdown after peak from tradable rows.
- Round/sector consistency and local duplicate avoidance.

Not validated:

- No production code inspection or scoring implementation patch.
- No live/current stock discovery.
- No brokerage or auto-trading path.
- External article URL enrichment is intentionally deferred; the quantitative calibration uses Stock-Web rows.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_direct_revenue_exposure_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,+1,+1,"direct product/ASP/volume exposure separated 025860 from proxy baskets","promotes direct positive without relying on Green-only revision",R4L15_C16_T001,3,3,2,medium,canonical_shadow_only,"not production; requires more holdout resource subclasses"
shadow_weight,C16_policy_proxy_decay_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,+1,+1,"policy headlines without direct revenue bridge produced 047400/000910 drawdowns","blocks false-positive Yellow/Green and starts timed 4C-watch",R4L15_C16_T002|R4L15_C16_T003,3,3,2,medium,canonical_shadow_only,"not production; proxy guard only"
shadow_weight,C16_price_only_4B_watch_feeds_decay_not_full_exit,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,+1,+1,"price-only peaks helped flag policy-proxy exhaustion but should not become full 4B without non-price evidence","keeps global 4B non-price rule while improving 4C timing",R4L15_C16_T002_4B|R4L15_C16_T003_4B,3,3,2,low,canonical_shadow_only,"watch overlay feeds later thesis-break timing"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R4L15_C16_CASE_001_NAMHAE_FERTILIZER_SUPPLY_20220304", "symbol": "025860", "company_name": "남해화학", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "FERTILIZER_EXPORT_RESTRICTION_DIRECT_REVENUE_EXPOSURE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L15_C16_T001", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_direct_resource_supply_shock", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Direct revenue exposure exists: fertilizer supply shock can become ASP/margin bridge rather than pure theme proxy."}
{"row_type": "case", "case_id": "R4L15_C16_CASE_002_UNION_MATERIALS_GALLIUM_GERMANIUM_FALSE_BREAK_20230704", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CHINA_EXPORT_CONTROL_THEME_PROXY_NO_DIRECT_REVISION", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L15_C16_T002", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_theme_proxy_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Policy headline exists, but direct revenue bridge is missing. C16 should not let policy_optional score alone promote Stage3/Green."}
{"row_type": "case", "case_id": "R4L15_C16_CASE_003_UNION_RARE_EARTH_TECH_BAN_FALSE_BREAK_20231222", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_EARTH_TECH_EXPORT_BAN_THEME_DECAY", "case_type": "4C_late", "positive_or_counterexample": "counterexample", "best_trigger": "R4L15_C16_T003", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_decay_after_no_direct_supply_earnings_bridge", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "No direct capacity/order/margin bridge. C16 needs a timed theme-decay 4C route when policy headline is not converted into revenue evidence within 30~60 trading days."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R4L15_C16_T001", "case_id": "R4L15_C16_CASE_001_NAMHAE_FERTILIZER_SUPPLY_20220304", "symbol": "025860", "company_name": "남해화학", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "FERTILIZER_EXPORT_RESTRICTION_DIRECT_REVENUE_EXPOSURE", "sector": "소재·스프레드·전략자원", "primary_archetype": "strategic_resource_policy_supply", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-03-04", "entry_date": "2022-03-04", "entry_price": 10500, "evidence_available_at_that_date": "러시아·우크라이나 전쟁 이후 비료·곡물·원재료 공급 차질과 수출 제한 가능성이 직접 비료 판매/가격 경로로 연결되던 구간. 2022-03-04 Stock-Web row는 close 10,500, intraday high 11,700, 거래량 7,271,867로 정책/공급 shock가 가격에 처음 반영된 Stage2-Actionable entry로 사용했다.", "evidence_source": "historical public policy/supply-shock context; exact OHLC from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025860/2022.csv", "profile_path": "atlas/symbol_profiles/025/025860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 57.14, "MFE_90D_pct": 61.9, "MFE_180D_pct": 61.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.14, "MAE_90D_pct": -14.29, "MAE_180D_pct": -23.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-19", "peak_price": 17000, "drawdown_after_peak_pct": -53.0, "green_lateness_ratio": "0.87: hypothetical Green after fertilizer price confirmation would have captured little remaining upside", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_direct_resource_supply_shock", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L15_C16_CASE_001_NAMHAE_FERTILIZER_SUPPLY_20220304_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L15_C16_T002", "case_id": "R4L15_C16_CASE_002_UNION_MATERIALS_GALLIUM_GERMANIUM_FALSE_BREAK_20230704", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CHINA_EXPORT_CONTROL_THEME_PROXY_NO_DIRECT_REVISION", "sector": "소재·스프레드·전략자원", "primary_archetype": "strategic_resource_policy_supply", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-07-04", "entry_date": "2023-07-04", "entry_price": 4070, "evidence_available_at_that_date": "중국의 갈륨/게르마늄 수출통제 headline 이후 희토류·전략소재 proxy로 반응했지만, trigger date 기준 고객/주문/ASP revision이 확인되지 않았다. Stock-Web 2023-07-04 row는 close 4,070, 2023-07-12 high 4,560 이후 2023-10-31 low 2,460까지 밀렸다.", "evidence_source": "historical public policy/supply-shock context; exact OHLC from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.04, "MFE_90D_pct": 12.04, "MFE_180D_pct": 12.04, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.15, "MAE_90D_pct": -39.56, "MAE_180D_pct": -39.56, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-12", "peak_price": 4560, "drawdown_after_peak_pct": -46.05, "green_lateness_ratio": "not_applicable: no confirmed Stage3-Green before peak", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "policy_theme_proxy_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L15_C16_CASE_002_UNION_MATERIALS_GALLIUM_GERMANIUM_FALSE_BREAK_20230704_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L15_C16_T003", "case_id": "R4L15_C16_CASE_003_UNION_RARE_EARTH_TECH_BAN_FALSE_BREAK_20231222", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_EARTH_TECH_EXPORT_BAN_THEME_DECAY", "sector": "소재·스프레드·전략자원", "primary_archetype": "strategic_resource_policy_supply", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-22", "entry_date": "2023-12-22", "entry_price": 5500, "evidence_available_at_that_date": "2023-12-21 중국 희토류 가공기술 수출 제한/전략소재 headline 직후 proxy basket이 재반응했다. Stock-Web 2023-12-22 row는 close 5,500, 2024-01-10 high 6,580 이후 2024-08-05 low 3,360까지 내려갔다.", "evidence_source": "historical public policy/supply-shock context; exact OHLC from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv", "profile_path": "atlas/symbol_profiles/000/000910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.64, "MFE_90D_pct": 19.64, "MFE_180D_pct": 19.64, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.0, "MAE_90D_pct": -7.27, "MAE_180D_pct": -38.91, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-10", "peak_price": 6580, "drawdown_after_peak_pct": -48.94, "green_lateness_ratio": "not_applicable: no confirmed Stage3-Green before peak", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "theme_decay_after_no_direct_supply_earnings_bridge", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L15_C16_CASE_003_UNION_RARE_EARTH_TECH_BAN_FALSE_BREAK_20231222_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L15_C16_T001_4B", "case_id": "R4L15_C16_CASE_001_NAMHAE_FERTILIZER_SUPPLY_20220304", "symbol": "025860", "company_name": "남해화학", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "FERTILIZER_EXPORT_RESTRICTION_DIRECT_REVENUE_EXPOSURE", "sector": "소재·스프레드·전략자원", "primary_archetype": "strategic_resource_policy_supply", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2022-04-15", "entry_date": "2022-04-15", "entry_price": 16150, "evidence_available_at_that_date": "local peak / overheat overlay after C16 policy-resource move; not a new long entry.", "evidence_source": "Songdaiki/stock-web OHLC row plus historical policy/supply context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025860/2022.csv", "profile_path": "atlas/symbol_profiles/025/025860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2022-04-19", "peak_price": 17000, "drawdown_after_peak_pct": -53.0, "green_lateness_ratio": "not_applicable: 4B overlay row", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L15_C16_CASE_001_NAMHAE_FERTILIZER_SUPPLY_20220304_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case overlay timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R4L15_C16_T002_4B", "case_id": "R4L15_C16_CASE_002_UNION_MATERIALS_GALLIUM_GERMANIUM_FALSE_BREAK_20230704", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CHINA_EXPORT_CONTROL_THEME_PROXY_NO_DIRECT_REVISION", "sector": "소재·스프레드·전략자원", "primary_archetype": "strategic_resource_policy_supply", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-07-12", "entry_date": "2023-07-12", "entry_price": 4455, "evidence_available_at_that_date": "local peak / overheat overlay after C16 policy-resource move; not a new long entry.", "evidence_source": "Songdaiki/stock-web OHLC row plus historical policy/supply context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2023-07-12", "peak_price": 4560, "drawdown_after_peak_pct": -46.05, "green_lateness_ratio": "not_applicable: 4B overlay row", "four_b_local_peak_proximity": 0.79, "four_b_full_window_peak_proximity": 0.79, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_watch_helped_but_not_full_without_non_price_evidence", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L15_C16_CASE_002_UNION_MATERIALS_GALLIUM_GERMANIUM_FALSE_BREAK_20230704_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case overlay timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R4L15_C16_T003_4B", "case_id": "R4L15_C16_CASE_003_UNION_RARE_EARTH_TECH_BAN_FALSE_BREAK_20231222", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_EARTH_TECH_EXPORT_BAN_THEME_DECAY", "sector": "소재·스프레드·전략자원", "primary_archetype": "strategic_resource_policy_supply", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2024-01-12", "entry_date": "2024-01-12", "entry_price": 6360, "evidence_available_at_that_date": "local peak / overheat overlay after C16 policy-resource move; not a new long entry.", "evidence_source": "Songdaiki/stock-web OHLC row plus historical policy/supply context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv", "profile_path": "atlas/symbol_profiles/000/000910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2024-01-10", "peak_price": 6580, "drawdown_after_peak_pct": -48.94, "green_lateness_ratio": "not_applicable: 4B overlay row", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_watch_helped_but_not_full_without_non_price_evidence", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L15_C16_CASE_003_UNION_RARE_EARTH_TECH_BAN_FALSE_BREAK_20231222_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case overlay timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L15_C16_CASE_001_NAMHAE_FERTILIZER_SUPPLY_20220304", "trigger_id": "R4L15_C16_T001", "symbol": "025860", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 5, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "direct_revenue_exposure_score": 15, "resource_supply_tightness_score": 18, "policy_theme_proxy_risk_score": 0, "inventory_cycle_risk_score": 0, "theme_decay_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 7, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "direct_revenue_exposure_score": 24, "resource_supply_tightness_score": 22, "policy_theme_proxy_risk_score": 0, "inventory_cycle_risk_score": 0, "theme_decay_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 85, "stage_label_after": "Stage3-Yellow-shadow", "changed_components": ["direct_revenue_exposure_score", "resource_supply_tightness_score", "margin_bridge_score"], "component_delta_explanation": "Direct fertilizer revenue exposure converts policy shock into margin bridge; current profile under-weights this C16 directness.", "MFE_90D_pct": 61.9, "MAE_90D_pct": -14.29, "score_return_alignment_label": "P0_missed_structural_P2_better", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L15_C16_CASE_002_UNION_MATERIALS_GALLIUM_GERMANIUM_FALSE_BREAK_20230704", "trigger_id": "R4L15_C16_T002", "symbol": "047400", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "direct_revenue_exposure_score": 0, "resource_supply_tightness_score": 0, "policy_theme_proxy_risk_score": 8, "inventory_cycle_risk_score": 0, "theme_decay_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow/false-positive-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "direct_revenue_exposure_score": 0, "resource_supply_tightness_score": 0, "policy_theme_proxy_risk_score": 26, "inventory_cycle_risk_score": 0, "theme_decay_score": 16, "positioning_overheat_score": 12, "thesis_break_score": 12}, "weighted_score_after": 55, "stage_label_after": "Stage2-Watch / 4C-watch", "changed_components": ["policy_theme_proxy_risk_score", "theme_decay_score", "execution_risk_score"], "component_delta_explanation": "Policy headline without direct revenue bridge is demoted; 30D/90D MAE shows false-positive path.", "MFE_90D_pct": 12.04, "MAE_90D_pct": -39.56, "score_return_alignment_label": "P0_false_positive_P3_guard_blocks", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L15_C16_CASE_003_UNION_RARE_EARTH_TECH_BAN_FALSE_BREAK_20231222", "trigger_id": "R4L15_C16_T003", "symbol": "000910", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 19, "valuation_repricing_score": 7, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "direct_revenue_exposure_score": 0, "resource_supply_tightness_score": 0, "policy_theme_proxy_risk_score": 8, "inventory_cycle_risk_score": 0, "theme_decay_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow/false-positive-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 4, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "direct_revenue_exposure_score": 0, "resource_supply_tightness_score": 0, "policy_theme_proxy_risk_score": 24, "inventory_cycle_risk_score": 0, "theme_decay_score": 22, "positioning_overheat_score": 16, "thesis_break_score": 18}, "weighted_score_after": 57, "stage_label_after": "Stage2-Watch / timed-4C", "changed_components": ["policy_theme_proxy_risk_score", "theme_decay_score", "thesis_break_score"], "component_delta_explanation": "Rare-earth headline re-spike failed to convert to confirmed revision; 4C should trigger earlier after direct-evidence timeout.", "MFE_90D_pct": 19.64, "MAE_90D_pct": -7.27, "score_return_alignment_label": "P0_4C_too_late_P3_better", "current_profile_verdict": "current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_direct_revenue_exposure_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,+1,+1,"direct product/ASP/volume exposure separated 025860 from proxy baskets","promotes direct positive without relying on Green-only revision",R4L15_C16_T001,3,3,2,medium,canonical_shadow_only,"not production; requires holdout"
shadow_weight,C16_policy_proxy_decay_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,+1,+1,"policy headlines without direct revenue bridge produced 047400/000910 drawdowns","blocks false-positive Yellow/Green and starts timed 4C-watch",R4L15_C16_T002|R4L15_C16_T003,3,3,2,medium,canonical_shadow_only,"not production; proxy guard only"
shadow_weight,C16_price_only_4B_watch_feeds_decay_not_full_exit,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,+1,+1,"price-only peaks help flag exhaustion but should not become full 4B without non-price evidence","keeps global 4B non-price rule while improving 4C timing",R4L15_C16_T002_4B|R4L15_C16_T003_4B,3,3,2,low,canonical_shadow_only,"watch overlay feeds later thesis-break timing"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "scheduled_round": "R4", "scheduled_loop": 15, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "current_profile_4C_too_late"], "diversity_score_summary": "estimated +50: new C16 symbols 025860/047400/000910, direct fertilizer supply positive plus two rare-earth/policy proxy counterexamples, 4B and 4C paths included.", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only row
```jsonl
{"row_type": "narrative_only", "case_id": "none", "symbol": null, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "reason": "no narrative-only case in this loop; all representative triggers have clean 180D tradable windows", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R4
completed_loop = 15
next_round = R5
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest read in this execution: max_date=2026-02-20, price_adjustment_status=raw_unadjusted_marcap, calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year, raw_shard_root=atlas/ohlcv_raw_by_symbol_year.
- 025860 profile: corporate-action candidate dates are 1999-09-28, 2000-01-21, 2000-05-02, and 2002-10-07; none overlap the 2022 calibration window. Sampled rows include 2022-03-04 close 10,500, 2022-04-19 high 17,000, and 2022-09-30 low 7,990.
- 047400 profile: corporate-action candidate date is 2011-04-29; it does not overlap the 2023/2024 calibration window. Sampled rows include 2023-07-04 close 4,070, 2023-07-12 high 4,560, 2023-10-31 low 2,460, and 2024-03/04 continuation lows above that trough.
- 000910 profile: corporate-action candidate dates are 1997-01-03 and 2008-05-07; neither overlaps the 2023/2024 calibration window. Sampled rows include 2023-12-22 close 5,500, 2024-01-10 high 6,580, and 2024-08-05 low 3,360.
- Evidence labels are historical calibration labels, not current/live recommendations. No stock_agent source code was inspected or patched.
