# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R4
scheduled_loop = 76
completed_round = R4
completed_loop = 76
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C
output_file = e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **4** new independent cases, **2** counterexamples, and **2** current-profile residual errors for **R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD**.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This file does **not** re-prove the global Stage2 bonus or Green lateness. The residual question is narrower: in C17 chemical commodity margin-spread cycles, when does a spread headline become a company-level margin bridge, and when is it only a theme beta that should be capped or routed to 4B/4C watch?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 76 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD |
| fine_archetype_id | SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C |
| loop_objective | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill |

R4 maps to L4 materials/spread/resource. Recent local R4 files covered C15/C16 heavily and C17 once with 금호석유/OCI/롯데케미칼/대한유화. This run keeps the same canonical family but adds a different C17 sub-route: **specialty chemical spread bridge vs theme beta / post-peak 4B**.

## 3. Previous Coverage / Duplicate Avoidance Check

No `stock_agent` source code was opened. Local residual MDs show R4 loop 71~75 already completed, and the immediately previous session completed R3/Loop76, so the next sequential slot is R4/Loop76.

```text
previous_completed_round = R3
previous_completed_loop = 76
scheduled_round = R4
scheduled_loop = 76
previous_R4_C17_symbols_seen = 006650|010060|011170|011780
selected_symbols = 298020|004000|298050|001390
hard_duplicate_policy = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "source_name": "FinanceData/marcap",
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
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap"
}
```

The manifest states raw/unadjusted OHLC, stock-web max date 2026-02-20, and calibration-safe tradable shards where zero-volume and invalid OHLC rows are excluded. The schema confirms the calibration basis as `tradable_raw` and requires 180 forward tradable days plus clean corporate-action windows for quantitative calibration.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | profile/corporate-action status | 180D calibration window |
|---|---|---|---|---|
| 298020 | 효성티앤씨 | atlas/symbol_profiles/298/298020.json | corporate_action_candidate_count=0 | clean_180D_window |
| 004000 | 롯데정밀화학 | atlas/symbol_profiles/004/004000.json | candidate dates only in 1996~1999 | clean_2021_2022_window |
| 298050 | HS효성첨단소재 | atlas/symbol_profiles/298/298050.json | corporate_action_candidate_count=0 | clean_180D_window |
| 001390 | KG케미칼 | atlas/symbol_profiles/001/001390.json | candidate=2023-08-28 outside 2022 180D window | clean_180D_window |

All representative rows have entry dates before the stock-web manifest max date, a 180 trading-day forward window, nonzero tradable OHLCV rows, and no 180D corporate-action contamination.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

positive compression:
  spread expansion
  + company-level margin bridge
  + operating leverage / financial visibility
  => Stage2-Actionable or Stage3-Yellow/Green is allowed.

counterexample compression:
  commodity/theme headline
  + price momentum
  - company-level margin bridge
  - durable revision / cash-flow visibility
  => Stage2-Watch or 4B/4C watch, not positive Stage3 promotion.

4B overlay compression:
  after strong MFE, if price nears full-window peak
  + valuation/positioning overheat
  + margin fade or spread normalization risk
  => 4B overlay, not a new Stage3 trigger.
```

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | is_new_independent_case | current_profile_verdict |
|---|---|---|---|---|---:|---|
| CASE_R4L76_C17_298020_HYOSUNG_TNC_SPANDEX_MARGIN_BRIDGE | 298020 | 효성티앤씨 | structural_success | positive | true | current_profile_correct |
| CASE_R4L76_C17_004000_LOTTE_FINE_ECH_CAUSTIC_MARGIN_BRIDGE | 004000 | 롯데정밀화학 | structural_success | positive | true | current_profile_correct |
| CASE_R4L76_C17_298050_HS_ADV_MATERIALS_TIRECORD_HIGH_MAE | 298050 | HS효성첨단소재 | high_mae_success | counterexample | true | current_profile_4B_too_late |
| CASE_R4L76_C17_001390_KG_CHEM_FERTILIZER_THEME_FALSE_PROMOTION | 001390 | KG케미칼 | false_positive_green | counterexample | true | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
representative_trigger_count = 4
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 2
```

The balance is intentionally mixed. 효성티앤씨 and 롯데정밀화학 show a true spread-to-margin bridge. HS효성첨단소재 and KG케미칼 show why C17 needs a margin-bridge gate and a post-peak overlay; otherwise the profile can mistake a product-cycle or fertilizer theme spike for durable Stage3 quality.

## 9. Evidence Source Map

| evidence family | used for | source note | scoring usage |
|---|---|---|---|
| Spandex margin bridge | 298020 positive | historical public earnings / industry spread narrative | positive promotion allowed |
| ECH / caustic / ammonia spread bridge | 004000 positive | historical public earnings / commodity spread narrative | positive promotion allowed, but 4B later needed |
| Tire-cord / carbon-fiber rerating with high post-peak MAE | 298050 counterexample | historical product-cycle narrative and OHLC peak/drawdown | positive score must be capped unless durable margin bridge confirms |
| Fertilizer / urea / raw-material theme beta | 001390 counterexample | historical commodity-theme spike; no durable margin bridge | watch-only / 4B/4C guard |

## 10. Price Data Source Map

| symbol | shard | profile | entry_date | entry_price | key stock-web rows checked |
|---|---|---|---:|---:|---|
| 298020 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv + 2021.csv | atlas/symbol_profiles/298/298020.json | 2020-11-02 | 155500 | entry row 2020-11-02 c=155500; peak row 2021-07-16 h=963000 |
| 004000 | atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv + 2022.csv | atlas/symbol_profiles/004/004000.json | 2021-07-30 | 72500 | entry row 2021-07-30 c=72500; peak row 2021-09-29 h=101500; later low 2022-01-27 l=66300 |
| 298050 | atlas/ohlcv_tradable_by_symbol_year/298/298050/2021.csv + 2022.csv | atlas/symbol_profiles/298/298050.json | 2021-07-30 | 614000 | entry row 2021-07-30 c=614000; peak row 2021-09-24 h=877000; later low 2022-01-28 l=398000 |
| 001390 | atlas/ohlcv_tradable_by_symbol_year/001/001390/2022.csv | atlas/symbol_profiles/001/001390.json | 2022-04-07 | 41200 | entry row 2022-04-07 c=41200; peak row 2022-04-20 h=52600; later low 2022-10-13 l=20200 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | current_profile_verdict | aggregate_group_role |
|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---|---|
| T298020_STAGE2_20201102_SPANDEX_MARGIN_BRIDGE | 298020 | Stage2-Actionable | 2020-11-02 | 155500 | 251.13 | -5.47 | 519.29 | -5.47 | 2021-07-16 | 963000 | current_profile_correct | representative |
| T298020_4B_20210716_SPANDEX_PEAK_MARGIN_FADE_OVERLAY | 298020 | Stage4B-Overlay | 2021-07-16 | 881000 | 9.31 | -20.54 | 9.31 | -25.09 | 2021-07-16 | 963000 | current_profile_correct | 4B_overlay_only |
| T004000_STAGE2_20210730_ECH_CAUSTIC_MARGIN_BRIDGE | 004000 | Stage2-Actionable | 2021-07-30 | 72500 | 40.00 | -12.14 | 40.00 | -12.14 | 2021-09-29 | 101500 | current_profile_correct | representative |
| T004000_4B_20210929_SPREAD_PEAK_OVERLAY | 004000 | Stage4B-Overlay | 2021-09-29 | 98500 | 3.05 | -32.69 | 3.05 | -32.69 | 2021-09-29 | 101500 | current_profile_correct | 4B_overlay_only |
| T298050_STAGE2_20210730_TIRECORD_CARBONFIBER_BETA_HIGH_MAE | 298050 | Stage2-Actionable | 2021-07-30 | 614000 | 42.83 | -16.45 | 42.83 | -35.18 | 2021-09-24 | 877000 | current_profile_4B_too_late | representative |
| T001390_STAGE2_20220407_FERTILIZER_THEME_BETA_FALSE_PROMOTION | 001390 | Stage2-PriceOnlyWatch | 2022-04-07 | 41200 | 27.67 | -36.53 | 27.67 | -50.97 | 2022-04-20 | 52600 | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | below_entry_30D | below_entry_90D | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---|---|---:|
| T298020_STAGE2_20201102_SPANDEX_MARGIN_BRIDGE | 28.94 | -5.47 | 251.13 | -5.47 | 519.29 | -5.47 | true | true | -27.31 |
| T298020_4B_20210716_SPANDEX_PEAK_MARGIN_FADE_OVERLAY | 9.31 | -18.27 | 9.31 | -20.54 | 9.31 | -25.09 | true | true | -27.31 |
| T004000_STAGE2_20210730_ECH_CAUSTIC_MARGIN_BRIDGE | 19.17 | -12.14 | 40.00 | -12.14 | 40.00 | -12.14 | true | true | -34.68 |
| T004000_4B_20210929_SPREAD_PEAK_OVERLAY | 3.05 | -20.00 | 3.05 | -32.69 | 3.05 | -32.69 | true | true | -34.68 |
| T298050_STAGE2_20210730_TIRECORD_CARBONFIBER_BETA_HIGH_MAE | 11.89 | -16.45 | 42.83 | -16.45 | 42.83 | -35.18 | true | true | -54.62 |
| T001390_STAGE2_20220407_FERTILIZER_THEME_BETA_FALSE_PROMOTION | 27.67 | -20.87 | 27.67 | -36.53 | 27.67 | -50.97 | true | true | -61.60 |

## 13. Current Calibrated Profile Stress Test

1. **298020**: current profile is correct because the spread narrative had company-level margin bridge and the OHLC path shows strong MFE with controlled early MAE.
2. **004000**: current profile is mostly correct at entry, but it needs a peak overlay after the spread rerating because upside was concentrated before a large drawdown.
3. **298050**: current profile is too late on 4B because high MFE coexists with severe 180D MAE; the entry should not remain an unqualified Stage3-style positive after valuation/positioning overheats.
4. **001390**: current profile is false positive if commodity-theme beta and relative strength are treated as margin-bridge evidence.
5. Stage2 actionable bonus is kept, but in C17 it should be conditional on margin_bridge_score and spread-to-company capture.
6. Yellow 75 and Green 87/55 are kept; the issue is evidence quality, not the global thresholds.
7. price-only blowoff guard is strengthened.
8. full 4B non-price requirement is strengthened: margin fade, spread normalization, and thesis evidence break are the non-price bridge from local peak to full 4B/4C watch.

```text
existing_axis_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
existing_axis_kept = stage3_yellow_total_min | stage3_green_total_min | stage3_green_revision_min
new_axis_proposed = C17_company_level_margin_bridge_required | C17_theme_beta_stage_cap | C17_post_peak_margin_fade_4B_overlay
```

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | proxy Green / confirmation entry | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| 298020 | 2020-11-02 @ 155500 | 2021-03-16 @ 540000 | 0.42 | Green is later but still before full spread-cycle peak. |
| 004000 | 2021-07-30 @ 72500 | 2021-09-15 @ 90500 | 0.33 | Yellow/Green confirmation was moderately late but still useful. |
| 298050 | 2021-07-30 @ 614000 | 2021-09-24 @ 860000 | 0.54 | Upside existed, but high-MAE risk required 4B overlay. |
| 001390 | 2022-04-07 @ 41200 | no confirmed Green | not_applicable | Theme beta should not become Green without margin bridge. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| T298020_4B_20210716_SPANDEX_PEAK_MARGIN_FADE_OVERLAY | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | 0.90 | 0.90 | good_full_window_4B_timing |
| T004000_4B_20210929_SPREAD_PEAK_OVERLAY | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | 0.90 | 0.90 | good_full_window_4B_timing |
| T298050_STAGE2_20210730_TIRECORD_CARBONFIBER_BETA_HIGH_MAE | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | 0.94 | 0.94 | good timing but current profile was late to downgrade |
| T001390_STAGE2_20220407_FERTILIZER_THEME_BETA_FALSE_PROMOTION | price_only, valuation_blowoff, positioning_overheat | 0.89 | 0.89 | price-only local 4B must not be treated as full 4B unless margin/thesis break confirms |

## 16. 4C Protection Audit

| symbol | 4C label | reason |
|---|---|---|
| 298020 | thesis_break_watch_only | spread cycle still delivered huge MFE before normalization; no hard 4C at Stage2 entry. |
| 004000 | thesis_break_watch_only | spread thesis weakened after peak but the original Stage2 was valid. |
| 298050 | hard_4c_late | large post-peak drawdown suggests earlier thesis-break watch after high-MAE pattern. |
| 001390 | hard_4c_success | theme-beta spike collapsed; 4C routing would have protected after margin bridge failed to appear. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L4_C17_spread_to_company_margin_bridge_gate
candidate_delta = +3 for visible company-level spread/margin bridge
candidate_penalty = -10 to -14 for commodity/theme beta without margin bridge
backtest_effect = preserves 298020/004000 positives; demotes 001390; sends 298050 to 4B-watch after high-MAE peak
confidence = medium
production_scoring_changed = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
new_axis_proposed = C17_company_level_margin_bridge_required
guard_axis = C17_theme_beta_stage_cap
overlay_axis = C17_post_peak_margin_fade_4B_overlay
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected rows | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | score_return_alignment |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | all four representative rows | 90.41 | -17.65 | 157.45 | -25.94 | 50% | high avg MFE but contaminated by severe MAE counters |
| P0b_e2r_2_0_baseline_reference | rollback reference | less strict evidence separation | 90.41 | -17.65 | 157.45 | -25.94 | 50% | weaker guard; not preferred |
| P1_L4_C17_sector_shadow | sector-specific | 298020/004000 positive, 298050 4B-watch, 001390 watch-only | 145.56 | -8.8 | 279.64 | -8.8 | 0% | better MAE control |
| P2_C17_archetype_shadow | canonical-specific | same as P1 | 145.56 | -8.8 | 279.64 | -8.8 | 0% | best explanatory compression |
| P3_counterexample_guard | guard profile | blocks commodity-theme beta from positive stage | 145.56 | -8.8 | 279.64 | -8.8 | 0% | strongest false-positive guard |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 298020 | 83 | Stage3-Yellow | 87 | Stage3-Green | 251.13 | -5.47 | aligned_positive |
| 004000 | 76 | Stage3-Yellow | 79 | Stage3-Yellow | 40.00 | -12.14 | aligned_positive_but_4B_needed |
| 298050 | 72 | Stage2-Actionable | 64 | Stage2-Watch/4B-Watch | 42.83 | -16.45 | improved_by_high_MAE_guard |
| 001390 | 54 | Stage2-Actionable | 40 | Stage2-Watch | 27.67 | -36.53 | improved_by_theme_beta_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C | 2 | 2 | 3 | 2 | 4 | 0 | 6 | 4 | 2 | true | true | C17 now has specialty-chemical spread bridge and theme-beta counterexamples; future R4 can test more non-Korean commodity proxies or hard 4C cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: theme_beta_false_positive, high_mae_success_4B_late
new_axis_proposed: C17_company_level_margin_bridge_required, C17_theme_beta_stage_cap, C17_post_peak_margin_fade_4B_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web manifest and schema basis.
- profile-level corporate-action caveats for selected symbols.
- entry_date / entry_price from actual tradable OHLC rows.
- 30D/90D/180D MFE/MAE using stock-web tradable rows and manually checked extrema.
- positive/counterexample balance and same_entry_group dedupe.

Not validated:
- No production `stock_agent` scoring code was opened.
- No live stock scan or current recommendation was performed.
- Public evidence text is treated as historical disclosure/industry narrative family; exact DART document IDs are not hydrated in this research file.
- 1Y/2Y fields are narrative-only/null unless directly shown; shadow weight uses 30D/90D/180D only.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_company_level_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+3,"Visible spread-to-company margin bridge separated 298020/004000 positives from 001390 theme beta","P1/P2 preserved positives avg_MFE_180D=279.64 and avg_MAE_180D=-8.8","T298020_STAGE2_20201102_SPANDEX_MARGIN_BRIDGE|T004000_STAGE2_20210730_ECH_CAUSTIC_MARGIN_BRIDGE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_theme_beta_stage_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,-1,-12,"Commodity/theme beta without margin bridge caused high-MAE false promotion","Demotes 001390 and prevents price-only Stage3 promotion","T001390_STAGE2_20220407_FERTILIZER_THEME_BETA_FALSE_PROMOTION",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_post_peak_margin_fade_4B_overlay,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"4B non-price evidence should include spread normalization/margin fade after local/full-window peak","Routes 298050 to 4B-watch earlier and preserves 298020/004000 overlay timing","T298050_STAGE2_20210730_TIRECORD_CARBONFIBER_BETA_HIGH_MAE|T004000_4B_20210929_SPREAD_PEAK_OVERLAY|T298020_4B_20210716_SPANDEX_PEAK_MARGIN_FADE_OVERLAY",6,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"CASE_R4L76_C17_298020_HYOSUNG_TNC_SPANDEX_MARGIN_BRIDGE","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T298020_STAGE2_20201102_SPANDEX_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Spandex spread/mix improvement was visible in operating leverage; price path confirmed strong upside before 4B."}
{"row_type":"case","case_id":"CASE_R4L76_C17_004000_LOTTE_FINE_ECH_CAUSTIC_MARGIN_BRIDGE","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T004000_STAGE2_20210730_ECH_CAUSTIC_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"ECH/caustic/ammonia spread capture was visible enough to permit Stage2/Yellow, but needed peak-risk overlay after spread blowoff."}
{"row_type":"case","case_id":"CASE_R4L76_C17_298050_HS_ADV_MATERIALS_TIRECORD_HIGH_MAE","symbol":"298050","company_name":"HS효성첨단소재","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"T298050_STAGE2_20210730_TIRECORD_CARBONFIBER_BETA_HIGH_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae_guard","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"A tire-cord/carbon-fiber rerating generated MFE, but absence of durable post-peak spread/margin confirmation produced large 180D MAE."}
{"row_type":"case","case_id":"CASE_R4L76_C17_001390_KG_CHEM_FERTILIZER_THEME_FALSE_PROMOTION","symbol":"001390","company_name":"KG케미칼","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T001390_STAGE2_20220407_FERTILIZER_THEME_BETA_FALSE_PROMOTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Fertilizer/urea/raw-material theme beta produced a short spike but lacked company-level margin bridge; later MAE and drawdown were severe."}
{"row_type":"trigger","trigger_id":"T298020_STAGE2_20201102_SPANDEX_MARGIN_BRIDGE","case_id":"CASE_R4L76_C17_298020_HYOSUNG_TNC_SPANDEX_MARGIN_BRIDGE","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","sector":"materials / specialty chemical spread","primary_archetype":"company-level chemical spread margin bridge vs commodity/theme beta","loop_objective":"sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-02","entry_date":"2020-11-02","entry_price":155500,"evidence_available_at_that_date":"Q3-2020/early-4Q public earnings and industry-spread narrative pointed to spandex margin bridge, not only price momentum.","evidence_source":"historical public disclosure / quarterly earnings / industry spread narrative family","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.94,"MFE_90D_pct":251.13,"MFE_180D_pct":519.29,"MFE_1Y_pct":519.29,"MFE_2Y_pct":null,"MAE_30D_pct":-5.47,"MAE_90D_pct":-5.47,"MAE_180D_pct":-5.47,"MAE_1Y_pct":-5.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-27.31,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_spread_margin_bridge_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_298020_2020-11-02_155500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T298020_4B_20210716_SPANDEX_PEAK_MARGIN_FADE_OVERLAY","case_id":"CASE_R4L76_C17_298020_HYOSUNG_TNC_SPANDEX_MARGIN_BRIDGE","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","sector":"materials / specialty chemical spread","primary_archetype":"company-level chemical spread margin bridge vs commodity/theme beta","loop_objective":"sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2021-07-16","entry_date":"2021-07-16","entry_price":881000,"evidence_available_at_that_date":"Local full-window peak occurred after extreme spread rerating; post-peak margin normalization risk became the relevant overlay rather than new positive evidence.","evidence_source":"stock-web price peak plus public spread-cycle normalization watch family","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.31,"MFE_90D_pct":9.31,"MFE_180D_pct":9.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.27,"MAE_90D_pct":-20.54,"MAE_180D_pct":-25.09,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-27.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_298020_2021-07-16_881000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case but 4B overlay row, not counted as new independent case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T004000_STAGE2_20210730_ECH_CAUSTIC_MARGIN_BRIDGE","case_id":"CASE_R4L76_C17_004000_LOTTE_FINE_ECH_CAUSTIC_MARGIN_BRIDGE","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","sector":"materials / specialty chemical spread","primary_archetype":"company-level chemical spread margin bridge vs commodity/theme beta","loop_objective":"sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2021-07-30","entry_date":"2021-07-30","entry_price":72500,"evidence_available_at_that_date":"Q2-2021 and spread-cycle context supported ECH/caustic/ammonia margin bridge, so the row is not pure commodity beta.","evidence_source":"historical public disclosure / quarterly earnings / commodity-spread narrative family","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv","profile_path":"atlas/symbol_profiles/004/004000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.17,"MFE_90D_pct":40.0,"MFE_180D_pct":40.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.14,"MAE_90D_pct":-12.14,"MAE_180D_pct":-12.14,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-29","peak_price":101500,"drawdown_after_peak_pct":-34.68,"green_lateness_ratio":0.33,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_margin_bridge_success_with_peak_overlay_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_004000_2021-07-30_72500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T004000_4B_20210929_SPREAD_PEAK_OVERLAY","case_id":"CASE_R4L76_C17_004000_LOTTE_FINE_ECH_CAUSTIC_MARGIN_BRIDGE","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","sector":"materials / specialty chemical spread","primary_archetype":"company-level chemical spread margin bridge vs commodity/theme beta","loop_objective":"sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2021-09-29","entry_date":"2021-09-29","entry_price":98500,"evidence_available_at_that_date":"Spread/valuation peak proximity and later spread-normalization risk made this a 4B overlay, not a fresh Stage3 promotion.","evidence_source":"stock-web local peak row plus spread-normalization watch family","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv","profile_path":"atlas/symbol_profiles/004/004000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.05,"MFE_90D_pct":3.05,"MFE_180D_pct":3.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.0,"MAE_90D_pct":-32.69,"MAE_180D_pct":-32.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-29","peak_price":101500,"drawdown_after_peak_pct":-34.68,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_004000_2021-09-29_98500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case but 4B overlay row, not counted as new independent case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T298050_STAGE2_20210730_TIRECORD_CARBONFIBER_BETA_HIGH_MAE","case_id":"CASE_R4L76_C17_298050_HS_ADV_MATERIALS_TIRECORD_HIGH_MAE","symbol":"298050","company_name":"HS효성첨단소재","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","sector":"materials / specialty chemical spread","primary_archetype":"company-level chemical spread margin bridge vs commodity/theme beta","loop_objective":"sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2021-07-30","entry_date":"2021-07-30","entry_price":614000,"evidence_available_at_that_date":"Tire-cord/carbon-fiber rerating narrative produced momentum, but durable company-level margin bridge and post-peak risk separation were weaker than the price beta.","evidence_source":"historical public earnings / product-cycle narrative family","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298050/2021.csv","profile_path":"atlas/symbol_profiles/298/298050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.89,"MFE_90D_pct":42.83,"MFE_180D_pct":42.83,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.45,"MAE_90D_pct":-16.45,"MAE_180D_pct":-35.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-24","peak_price":877000,"drawdown_after_peak_pct":-54.62,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing_but_current_profile_late","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"high_mae_success_4B_late_counterexample","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_298050_2021-07-30_614000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T001390_STAGE2_20220407_FERTILIZER_THEME_BETA_FALSE_PROMOTION","case_id":"CASE_R4L76_C17_001390_KG_CHEM_FERTILIZER_THEME_FALSE_PROMOTION","symbol":"001390","company_name":"KG케미칼","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEM_SPREAD_MARGIN_BRIDGE_VS_THEME_BETA_4B_4C","sector":"materials / specialty chemical spread","primary_archetype":"company-level chemical spread margin bridge vs commodity/theme beta","loop_objective":"sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2022-04-07","entry_date":"2022-04-07","entry_price":41200,"evidence_available_at_that_date":"Fertilizer/urea/raw-material theme spike had public-event and relative-strength evidence but weak company-level spread-to-margin bridge; later price path behaved like theme beta.","evidence_source":"historical public event / commodity-theme narrative family","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001390/2022.csv","profile_path":"atlas/symbol_profiles/001/001390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.67,"MFE_90D_pct":27.67,"MFE_180D_pct":27.67,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.87,"MAE_90D_pct":-36.53,"MAE_180D_pct":-50.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-20","peak_price":52600,"drawdown_after_peak_pct":-61.6,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.89,"four_b_timing_verdict":"price_only_local_4B_too_early_unless_margin_break_confirms","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"theme_beta_false_positive_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_001390_2022-04-07_41200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R4L76_C17_298020_HYOSUNG_TNC_SPANDEX_MARGIN_BRIDGE","trigger_id":"T298020_STAGE2_20201102_SPANDEX_MARGIN_BRIDGE","symbol":"298020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":13,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":16,"fcf_conversion_score":7,"positioning_overheat_score":-2,"thesis_break_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":21,"revision_score":13,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18,"fcf_conversion_score":7,"positioning_overheat_score":-2,"thesis_break_score":0},"weighted_score_after":87,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","asp_or_spread_score","execution_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"add C17 margin-bridge confirmation bonus","MFE_90D_pct":251.13,"MAE_90D_pct":-5.47,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R4L76_C17_004000_LOTTE_FINE_ECH_CAUSTIC_MARGIN_BRIDGE","trigger_id":"T004000_STAGE2_20210730_ECH_CAUSTIC_MARGIN_BRIDGE","symbol":"004000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":9,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":14,"fcf_conversion_score":5,"positioning_overheat_score":-5,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":9,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":16,"fcf_conversion_score":5,"positioning_overheat_score":-5,"thesis_break_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","asp_or_spread_score","execution_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"keep positive but require 4B peak overlay after spread blowoff","MFE_90D_pct":40.0,"MAE_90D_pct":-12.14,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R4L76_C17_298050_HS_ADV_MATERIALS_TIRECORD_HIGH_MAE","trigger_id":"T298050_STAGE2_20210730_TIRECORD_CARBONFIBER_BETA_HIGH_MAE","symbol":"298050","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":4,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":-9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":8,"fcf_conversion_score":2,"positioning_overheat_score":-10,"thesis_break_score":-5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":8,"fcf_conversion_score":2,"positioning_overheat_score":-15,"thesis_break_score":-9},"weighted_score_after":64,"stage_label_after":"Stage2-Watch/4B-Watch","changed_components":["margin_bridge_score","asp_or_spread_score","execution_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"deduct for weak durable margin bridge and high-MAE post-peak profile","MFE_90D_pct":42.83,"MAE_90D_pct":-16.45,"score_return_alignment_label":"improved_by_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R4L76_C17_001390_KG_CHEM_FERTILIZER_THEME_FALSE_PROMOTION","trigger_id":"T001390_STAGE2_20220407_FERTILIZER_THEME_BETA_FALSE_PROMOTION","symbol":"001390","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":5,"fcf_conversion_score":0,"positioning_overheat_score":-12,"thesis_break_score":-10},"weighted_score_before":54,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-2,"revision_score":0,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":5,"fcf_conversion_score":0,"positioning_overheat_score":-17,"thesis_break_score":-10},"weighted_score_after":40,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","asp_or_spread_score","execution_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"stage-cap commodity theme beta without company-level margin bridge","MFE_90D_pct":27.67,"MAE_90D_pct":-36.53,"score_return_alignment_label":"improved_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"diversity_score_summary":"new_symbols=4, new_trigger_families=4, counterexample_gap=2, residual_errors=2, wrong_round_penalty=0","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["theme_beta_false_positive","high_mae_success_4B_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 76
next_round = R5
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Manifest checked: `atlas/manifest.json`; max_date = 2026-02-20; price_basis = tradable_raw; price_adjustment_status = raw_unadjusted_marcap.
- Schema checked: `atlas/schema.json`; tradable columns are d,o,h,l,c,v,a,mc,s,m; MFE/MAE definitions match the prompt.
- Profiles checked:
  - `atlas/symbol_profiles/298/298020.json`
  - `atlas/symbol_profiles/004/004000.json`
  - `atlas/symbol_profiles/298/298050.json`
  - `atlas/symbol_profiles/001/001390.json`
- Tradable shards checked:
  - `atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/004/004000/2022.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/298/298050/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/298/298050/2022.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/001/001390/2022.csv`

